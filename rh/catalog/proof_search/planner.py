"""Bounded AND/OR proof-obligation search, not an autonomous theorem prover.

Only freshly Lean-checked rules participate in forward inference. Research
recipes merely generate obligations, including their own unproved bridge.
Graph navigation and candidate scores can never add a mathematical fact.
"""
from __future__ import annotations

from itertools import product
import time

from .common import digest, need
from .kernel_audit import check_receipt


def validate_knowledge(knowledge):
    goals = knowledge['goals']
    ids = [r['id'] for r in knowledge['rules']]
    need(len(ids) == len(set(ids)), 'DUPLICATE_RULE_ID')
    recipe_ids = [r['id'] for r in knowledge.get('recipes', [])]
    need(len(recipe_ids) == len(set(recipe_ids)), 'DUPLICATE_RECIPE_ID')
    for rule in knowledge['rules']:
        need(type(rule['requires']) is list and len(rule['requires']) == len(set(rule['requires'])), 'BAD_PREMISES')
        for key in [*rule['requires'], rule['conclusion']]:
            need(key in goals and goals[key].get('lean'), 'UNTYPED_EXECUTABLE_RULE_GOAL: ' + key)
    for recipe in knowledge.get('recipes', []):
        need(all(k in goals for k in [recipe['target'], *recipe['requires']]), 'UNKNOWN_RECIPE_GOAL')
    return True


def closure(knowledge):
    """Call only after receipt validation. Status words and recipes are ignored."""
    validate_knowledge(knowledge)
    facts, provenance = set(), {}
    while True:
        changed = False
        for rule in knowledge['rules']:
            goal = rule['conclusion']
            if goal not in facts and set(rule['requires']) <= facts:
                facts.add(goal)
                provenance[goal] = {'rule': rule['id'], 'premises': list(rule['requires'])}
                changed = True
        if not changed: return facts, provenance


class Planner:
    def __init__(self, knowledge, receipt, *, check_files=True, beam=8, max_expansions=500):
        validate_knowledge(knowledge)
        check_receipt(receipt, knowledge, check_files=check_files)
        need(type(beam) is int and 0 < beam <= 64, 'BAD_BEAM')
        need(type(max_expansions) is int and 0 < max_expansions <= 100000, 'BAD_EXPANSION_BUDGET')
        self.knowledge, self.receipt = knowledge, receipt
        self.facts, self.provenance = closure(knowledge)
        self.beam, self.max_expansions = beam, max_expansions
        self.expansions, self.cache_hits = 0, 0
        self.memo = {}
        self.cycle_cuts = []

    @staticmethod
    def rank(plan):
        return (plan['priority'], len(plan['unresolved']), plan['cost'],
                len(plan['steps']), digest(plan))

    def expand(self, goal, ancestors=()):
        need(goal in self.knowledge['goals'], 'UNKNOWN_GOAL: ' + goal)
        if goal in self.facts:
            return [{'goal': goal, 'unresolved': [], 'steps': [], 'reused': [goal], 'cost': 0, 'priority': 0}]
        if goal in ancestors:
            self.cycle_cuts.append([*ancestors, goal])
            return []
        key = (goal, tuple(sorted(ancestors)))
        if key in self.memo:
            self.cache_hits += 1
            return self.memo[key]
        if self.expansions >= self.max_expansions:
            return [{'goal': goal, 'unresolved': [goal], 'steps': [], 'reused': [], 'cost': 1, 'priority': 99,
                     'budget_limited': True}]
        self.expansions += 1
        branches = [('checked_rule', r) for r in self.knowledge['rules'] if r['conclusion'] == goal]
        branches += [('unproved_recipe', r) for r in self.knowledge.get('recipes', []) if r['target'] == goal]
        plans = []
        for kind, rule in branches:
            children = [self.expand(g, (*ancestors, goal)) for g in rule['requires']]
            if any(not p for p in children): continue
            # Each branch is bounded before Cartesian expansion; no exhaustive
            # claim is made when beam pruning or the expansion budget is active.
            partial = [{'unresolved': [], 'reused': [], 'steps': [], 'cost': 0, 'priority': 0}]
            for options in children:
                merged = []
                for left, right in product(partial, options):
                    merged.append({'unresolved': sorted(set(left['unresolved']) | set(right['unresolved'])),
                                   'reused': sorted(set(left['reused']) | set(right['reused'])),
                                   'steps': left['steps'] + right['steps'],
                                   'cost': left['cost'] + right['cost'],
                                   'priority': max(left['priority'], right['priority'])})
                partial = sorted(merged, key=self.rank)[:self.beam]
            for row in partial:
                if kind == 'unproved_recipe':
                    # Listing ingredients is not a proved implication.
                    row['unresolved'] = sorted(set(row['unresolved']) | {'prove_recipe:' + rule['id']})
                row.update(goal=goal, cost=row['cost'] + rule.get('cost', 0),
                           priority=max(row['priority'], rule.get('priority', 0)))
                row['steps'] += [{'kind': kind, 'id': rule['id'], 'requires': rule['requires'], 'target': goal}]
                plans.append(row)
        if not plans:
            plans = [{'goal': goal, 'unresolved': [goal], 'steps': [], 'reused': [], 'cost': 1, 'priority': 0}]
        unique = {digest(p): p for p in plans}
        answer = sorted(unique.values(), key=self.rank)[:self.beam]
        self.memo[key] = answer
        return answer

    def report(self, targets):
        t = time.monotonic()
        routes = {goal: self.expand(goal) for goal in targets}
        return {'status': 'BOUNDED_PROOF_OBLIGATION_PLAN', 'RH_proved': 'rh' in self.facts,
                'known_facts': sorted(self.facts), 'fact_provenance': self.provenance,
                'targets': routes, 'cycle_cuts': self.cycle_cuts, 'expansions': self.expansions,
                'memo_hits': self.cache_hits, 'beam': self.beam, 'max_expansions': self.max_expansions,
                'seconds': round(time.monotonic()-t, 6), 'numerical_jobs_launched': 0,
                'complete_search_claim': False, 'recipes_are_unproved': True}


SCOPE_KEYS = ('domain', 'normalization', 'extent', 'quantifiers')


def candidate_id(candidate):
    """Provenance labels and fitness do not create a distinct mathematical object."""
    return digest({k: v for k, v in candidate.items() if k not in {'id', 'label', 'parents', 'fitness', 'notes'}})


def assess(candidate, knowledge, facts):
    target = candidate.get('target')
    need(target in knowledge['goals'], 'CANDIDATE_UNKNOWN_TARGET')
    goal = knowledge['goals'][target]
    result = {'id': candidate_id(candidate), 'target': target, 'label': candidate.get('label', ''),
              'status': 'OPEN_CONSTRUCTION', 'proof_accepted': False, 'new_fact': False, 'reasons': []}
    if goal.get('status') == 'REFUTED':
        result.update(status='EXCLUDED_REGISTERED_FIXED_CONSTANT', reasons=['r475-repair: fixed constant, not the corrected existential rate'])
        return result
    missing = [k for k in SCOPE_KEYS if goal.get(k) is not None and candidate.get(k) is None]
    mismatch = [k for k in SCOPE_KEYS if candidate.get(k) is not None and goal.get(k) is not None and candidate[k] != goal[k]]
    if missing or mismatch:
        result.update(status='NEEDS_TYPED_SCOPE_BRIDGE', reasons=[*('missing:' + k for k in missing), *('mismatch:' + k for k in mismatch)])
        return result
    if 'target_positivity' in candidate.get('construction_requires', []):
        result.update(status='REJECT_CIRCULAR_CONSTRUCTION', reasons=['r404: target positivity is a construction input'])
        return result
    if candidate.get('method') == 'heat_normalization_only':
        result.update(status='REJECT_RESTATEMENT', reasons=['2026-09-05-external-heat-A: no new arithmetic remainder control'])
        return result
    if candidate.get('bound_scope') == 'all_form_core_vectors' and candidate.get('chart') == 'relative_window_flow_20260907':
        result.update(status='EXCLUDED_UNDER_REGISTERED_CORE_COUNTEREXAMPLE', reasons=['actual prime-2 whole-core counterexample; minimizers are a different premise'])
        return result
    if candidate.get('method') == 'finite_gram_compactness' and candidate.get('dimension_mode') == 'growing':
        result.update(status='NEEDS_TYPED_SCOPE_BRIDGE', reasons=['Fintype is fixed in GramCompactness; countable/infinite compatibility is missing'])
        return result
    if candidate.get('method') == 'deployed_phase_head_v856' and candidate.get('head_variant') == 'original_A':
        result.update(status='EXCLUDED_UNDER_REGISTERED_PHASE_SCOPE', reasons=['v856 deployed phase-head scope; a changed head must be reviewed separately'])
        return result
    if candidate.get('assumed_research_axioms'):
        result.update(status='ASSUMED_INPUTS_NOT_DISCHARGED', reasons=list(candidate['assumed_research_axioms']))
        return result
    if candidate.get('finite_data_only'):
        result.update(status='FINITE_DIAGNOSTIC_ONLY', reasons=['finite data do not instantiate a global forall or complete-tail theorem'])
        return result
    if target in facts:
        result.update(status='REUSE_VERIFIED', reasons=['already derived from fresh checked rules; no new search required'])
        return result
    result['reasons'] = ['No proof supplied; a source-specific construction and all listed obligations remain required']
    return result


def scoped_candidate(knowledge, target, **extra):
    goal = knowledge['goals'][target]
    return {'target': target, **{k: goal[k] for k in SCOPE_KEYS if k in goal}, **extra}


def generate_candidates(knowledge):
    """Small explicit construction grammar; proposals, not discovered operators."""
    rows = []
    for method, representation in product(('prime_block_telescope', 'source_relative_comparison'),
                                          ('direct_gabor', 'normalized_with_explicit_inverse')):
        rows.append(scoped_candidate(knowledge, 'gabor_positive', method=method, representation=representation,
                                    required_recipe='gabor_arithmetic_blocks'))
    for high_control in ('full_energy_dual', 'complete_form_schur'):
        rows.append(scoped_candidate(knowledge, 'boundary_window', method='complete_boundary', high_control=high_control,
                                    required_recipe='complete_boundary_energy'))
    for minimizer in ('attained_minimizer', 'controlled_minimizing_sequence'):
        rows.append(scoped_candidate(knowledge, 'positive_bottom', method='minimizer_relative', minimizer=minimizer,
                                    bound_scope='actual_minimizers', chart='relative_window_flow_20260907',
                                    required_recipe='minimizer_relative_flow'))
    return rows


def controls(knowledge):
    """Real audited failure patterns, not a numerical success benchmark."""
    c = lambda target, **kw: scoped_candidate(knowledge, target, **kw)
    return [
        c('arch_weighted', label='closed ARCH'), c('arch_fixed_constant', label='old fixed ARCH'),
        c('gabor_positive', label='finite packets', finite_data_only=True),
        c('native_positive', label='circular Cholesky', construction_requires=['target_positivity']),
        c('gabor_positive', label='heat rename', method='heat_normalization_only'),
        c('positive_bottom', label='whole core', bound_scope='all_form_core_vectors', chart='relative_window_flow_20260907'),
        c('positive_bottom', label='minimizers', bound_scope='actual_minimizers', chart='relative_window_flow_20260907'),
        c('gabor_positive', label='growing finite Gram', method='finite_gram_compactness', dimension_mode='growing'),
        c('gabor_positive', label='wrong native gauge', normalization='native_selected'),
        c('gabor_positive', label='axiomatic seam', assumed_research_axioms=['collar_gapped', 'mmst_scaling_limit', 'adamo_holomorphic_e8']),
        c('native_positive', label='old phase head', method='deployed_phase_head_v856', head_variant='original_A'),
        c('native_positive', label='new phase head', method='deployed_phase_head_v856', head_variant='changed_not_reviewed')]
