"""Bounded adaptive cross-family proposal search and exact falsification.

Grammar candidates are research contracts, not constructed operators. An agent
can submit genuinely new explicit objects outside the grammar. Neither scores,
submitted status strings nor finite controls enter the Lean proof closure.
"""
from fractions import Fraction as F
from itertools import product
import math
from pathlib import Path
import re

from proof_search.common import CATALOG, digest, dump, need, read, sha
from . import source_index

BASE = CATALOG/'research_engine'


def identifier(candidate):
    return digest({k: candidate[k] for k in ('object', 'target', 'method', 'scope', 'obligations')})[:20]


def validate(candidate):
    for key in ('object', 'target', 'method', 'scope', 'difference', 'next_test', 'stop_condition', 'domain'):
        need(isinstance(candidate.get(key), str) and candidate[key].strip(), 'MISSING_CANDIDATE_FIELD: '+key)
    for key in ('obligations', 'sources', 'asserted_claims'):
        need(isinstance(candidate.get(key), list) and all(isinstance(v, str) for v in candidate[key]), 'BAD_CANDIDATE_LIST: '+key)
    need(candidate['obligations'] and candidate['sources'], 'CANDIDATE_REQUIRES_OBLIGATIONS_AND_SOURCES')
    # A proposal may not grant itself proof or bypass status based on prose.
    need(not candidate.get('proof_accepted') and not candidate.get('RH_proved'), 'SELF_PROMOTION_FORBIDDEN')
    return candidate


def assess(candidate, claims, knowledge, constraints):
    validate(candidate)
    by_id = {c['id']: c for c in claims}
    reasons = []
    for claim in candidate['asserted_claims']:
        if claim not in by_id: reasons.append('UNKNOWN_CLAIM:'+claim)
        elif by_id[claim]['state'] in {'REFUTED', 'STALE_SOURCE', 'SOURCE_DISCOVERED'}:
            reasons.append(by_id[claim]['state']+':'+claim)
    if candidate['target'] not in knowledge['goals']:
        reasons.append('UNMAPPED_TARGET_REQUIRES_REVIEW')
    if candidate.get('assumes_target'):
        reasons.append('CIRCULAR_TARGET_PREMISE')
    if candidate.get('finite_only') and candidate.get('claims_global'):
        reasons.append('FINITE_TO_GLOBAL_WITHOUT_PROOF')
    if candidate.get('arithmetic_dependence') == 'none' and candidate.get('claims_global'):
        reasons.append('WORLD_BLIND_GLOBAL_CLAIM')
    if candidate.get('changes_normalization') and not candidate.get('normalization_bridge'):
        reasons.append('NORMALIZATION_BRIDGE_MISSING')
    return {'id': identifier(candidate), 'status': 'BLOCKED_SCOPED_FILTER' if reasons else 'NEEDS_PRIOR_ART_AND_SOURCE_REVIEW',
            'reasons': reasons, 'proof_accepted': False, 'new_fact': False,
            'registered_constraint_ids': [c['id'] for c in constraints['constraints']],
            'constraint_semantic_review_complete': False,
            'all_obligations_required': True,
            'unresolved': list(candidate['obligations'])+['Prove that the proposed object actually implies the declared target.']}


def generate(motifs, methods):
    candidates = []
    for motif, method in product(motifs, methods):
        if method['id'] not in motif['methods']: continue
        candidates.append({**{k: v for k, v in motif.items() if k not in {'id', 'methods', 'cost'}},
                           'method': method['id'], 'method_detail': method['description'],
                           'parents': [motif['id'], method['id']],
                           'cost': motif.get('cost', 1)+method.get('cost', 1),
                           'scope': motif['scope']+'; '+method['scope'], 'kind': 'GENERATED_RESEARCH_CONTRACT',
                           'proof_accepted': False, 'RH_proved': False})
    return candidates


def rank(candidates, history, knowledge, graph):
    """Coverage/cost + novelty history + domain diversity, not probability."""
    nodes = {n['id']: n for n in graph['nodes']}
    ranked = []
    for c in candidates:
        identifier_ = identifier(c)
        old = history.get(identifier_, {})
        target = knowledge['goals'].get(c['target'], {})
        mapped = target.get('graph_id')
        linked = sum(e['dst']==mapped and e['rel'] in {'REQUIRES', 'WOULD_CLOSE', 'REDUCES_TO'}
                     for e in graph['edges']) if mapped in nodes else 0
        score = 4/(1+old.get('exposures', 0)) + min(linked, 5) - 0.3*c.get('cost', 3)
        # A finite falsification is per exact object, not a global ban on its domain.
        evidence = Path(old['result_evidence']) if old.get('result_evidence') else None
        current_result = evidence is not None and evidence.is_file() and sha(evidence)==old.get('result_evidence_sha256')
        if current_result and old.get('result') in {'REFUTED_SCOPED', 'DUPLICATE'}: score -= 100
        ranked.append((score, identifier_, c))
    return sorted(ranked, key=lambda row: (-row[0], row[1]))


def choose(ranked, limit):
    selected, used = [], set()
    for score, cid, c in ranked:
        if c['domain'] not in used:
            selected.append((score, cid, c)); used.add(c['domain'])
            if len(selected)==limit: return selected
    ids = {r[1] for r in selected}
    for row in ranked:
        if row[1] not in ids:
            selected.append(row); ids.add(row[1])
            if len(selected)==limit: break
    return selected


def catalog_hits(candidate, records, limit=6):
    words = set(re.findall(r'[a-z]{3,}', (candidate['object']+' '+candidate['difference']).lower()))
    out = []
    for r in records:
        text = ' '.join(str(r.get(k,'')) for k in ('mechanism','solved','failed_because','reusable','path'))
        tokens = set(re.findall(r'[a-z]{3,}', text.lower()))
        score = len(words & tokens)/math.sqrt(max(1, len(words)*len(tokens)))
        if score:
            out.append((score, r['path'], {k: r.get(k) for k in
                        ('path','round','outcome','failure_class','solved','failed_because')}))
    return [r for _, _, r in sorted(out, key=lambda x: (-x[0], x[1]))[:limit]]


def exact_controls():
    # Mechanism-level rational counterexample search, not real zeta-window data.
    j = ((0,1,0),(1,0,0),(0,0,-2))
    def form(a, b): return sum(F(a[i])*j[i][k]*F(b[k])/2 for i in range(3) for k in range(3))
    tested = 0; witness = None
    for a, b in product(product((-1,0,1), repeat=3), repeat=2):
        tested += 1
        x, y, z = form(a,a), form(b,b), form(a,b)
        determinant = x*y-z*z
        if x < 0 and determinant > 0:
            witness = {'P_columns': [a,b], 'K': [[str(x),str(z)],[str(z),str(y)]],
                       'determinant': str(determinant)}
            break
    need(witness is not None, 'MISSED_KNOWN_RANK_TWO_COUNTEREXAMPLE')
    # A positive inverse does not make a zero residual strictly positive.
    zero_rung = F(0)*F(1)*F(0)
    need(zero_rung==0, 'ZERO_RUNG_CONTROL_FAILED')
    # Correct relative cone criterion: x>=0, y>=0, xy>=z^2 certifies this
    # 2x2 matrix only, not its source identification or other test directions.
    x, y, z = F(3), F(2), F(1)
    need(x>0 and y-z*z/x>0, 'SCHUR_POSITIVE_CONTROL_FAILED')
    return {'kind': 'EXACT_RATIONAL_MECHANISM_CONTROLS', 'rank_two_counterexample': witness,
            'matrices_tested_before_witness': tested, 'zero_rung': str(zero_rung),
            'positive_relative_cone': {'diagonal': [str(x),str(y)], 'off_diagonal': str(z),
                                      'schur': str(y-z*z/x)},
            'real_prime_windows_tested': 0, 'RH_proved': False}


def explore(limit=6):
    need(type(limit) is int and 1 <= limit <= 12, 'BAD_CANDIDATE_LIMIT')
    import paper_knowledge
    paper_knowledge.check()
    config = read(BASE/'motifs.json')
    papers = read(paper_knowledge.OUTPUT)
    knowledge = read(CATALOG/'proof_search/knowledge.json')
    constraints = read(CATALOG/'proof_search/constraints.json')
    graph = read(CATALOG/'map/rh_concept_map.json')
    records = read(CATALOG/'rh_semantic_catalog.json')['records']
    history_file = BASE/'generated/history.json'
    history = read(history_file) if history_file.exists() else {}
    candidates = generate(config['motifs'], config['methods'])
    for p in sorted((BASE/'submissions').glob('*.json')):
        candidates.append(validate(read(p)))
    unique = {identifier(c): c for c in candidates}
    rows = []
    for score, cid, c in choose(rank(list(unique.values()), history, knowledge, graph), limit):
        assessment = assess(c, papers['claims'], knowledge, constraints)
        prior = catalog_hits(c, records)
        hits = source_index.search(c.get('retrieval_query', c['object']+' '+c['domain']), limit=4)
        rows.append({'proposal': c, 'assessment': assessment, 'priority_score': round(score,5),
                     'score_meaning': 'Graph target connectivity / cost / exposure; not breakthrough probability',
                     'catalog_precedents': prior, 'source_excerpts': hits,
                     'review_action': 'Read original sources and articulate scope difference for each relevant kill before any new experiment.'})
        history.setdefault(cid, {})['exposures'] = history.get(cid, {}).get('exposures',0)+1
    report = {'status': 'BOUNDED_ADAPTIVE_RESEARCH_QUEUE', 'candidates_in_registered_grammar': len(candidates),
              'unique_objects': len(unique), 'selected': rows, 'exact_controls': exact_controls(),
              'paper_source_fingerprint': papers['source_fingerprint'],
              'input_hashes': {str(p): sha(p) for p in [BASE/'motifs.json', CATALOG/'rh_semantic_catalog.json',
                                                      CATALOG/'map/rh_concept_map.json', paper_knowledge.OUTPUT]},
              'all_constraints_semantically_checked': False, 'new_facts': [], 'RH_proved': False,
              'autonomous_arbitrary_code_execution': False,
              'creative_extension': 'The scheduled agent can submit explicit new objects outside the finite motif grammar.'}
    dump(BASE/'generated/queue.json', report)
    dump(history_file, history)
    return report
