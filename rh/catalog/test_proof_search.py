"""Safety regressions for the planner, not empirical RH evidence."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from proof_search.common import HERE, digest, need, read
from proof_search.kernel_audit import adapter_source, check_receipt, parse_audits
from proof_search.planner import Planner, assess, candidate_id, closure, controls, generate_candidates, scoped_candidate
from proof_search.registry import discover, make_registry, source_declarations, strip_lean


def fixture_receipt(k):
    # Unit-test fixture only. Production entry points always check real files.
    return {'status': 'FRESH_ADAPTERS_KERNEL_CHECKED', 'knowledge_fingerprint': digest(k),
            'audits': {'RHProofSearch.' + r['id']: {'axioms': ['propext'], 'type': 'TEST FIXTURE ONLY'} for r in k['rules']}}


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.k = read(HERE / 'knowledge.json')
        self.p = Planner(self.k, fixture_receipt(self.k), check_files=False)

    def test_only_arch_facts_are_closed(self):
        self.assertEqual(self.p.facts, {'arch_weighted', 'arch_rate', 'arch_convergence'})

    def test_equivalence_cycle_cannot_prove_rh(self):
        report = self.p.report(['rh', 'native_positive'])
        self.assertFalse(report['RH_proved'])
        self.assertTrue(report['cycle_cuts'])
        self.assertTrue(all(p['unresolved'] for p in report['targets']['rh']))

    def test_native_route_retains_both_and_premises(self):
        p = self.p.report(['native_positive'])['targets']['native_positive']
        self.assertTrue(any({'freq', 'eventual_bound'} <= set(r['unresolved']) for r in p))

    def test_recipe_ingredients_do_not_prove_recipe(self):
        for route in self.p.expand('boundary_window'):
            self.assertIn('prove_recipe:complete_boundary_energy', route['unresolved'])
            self.assertIn('both_couplings', route['unresolved'])

    def test_status_words_are_not_proofs(self):
        self.k['goals']['rh']['status'] = 'PROVED'
        facts, _ = closure(self.k)
        self.assertNotIn('rh', facts)

    def test_altered_rules_invalidate_receipt(self):
        receipt = fixture_receipt(self.k)
        self.k['rules'][3]['requires'] = []
        with self.assertRaisesRegex(ValueError, 'KNOWLEDGE_CHANGED'):
            check_receipt(receipt, self.k, check_files=False)

    def test_sorry_and_custom_axioms_cannot_authorize(self):
        for axiom in ['sorryAx', 'Research.assumeRH', 'Lean.ofReduceBool']:
            receipt = fixture_receipt(self.k)
            receipt['audits']['RHProofSearch.arch_weighted_proved']['axioms'] = [axiom]
            with self.assertRaisesRegex(ValueError, 'UNATTESTED_RULE'):
                check_receipt(receipt, self.k, check_files=False)

    def test_empty_source_receipt_is_not_a_proof_receipt(self):
        receipt = fixture_receipt(self.k)
        receipt.update(source_hashes={}, code_hashes={})
        with self.assertRaisesRegex(ValueError, 'AUDIT_SOURCE_SCOPE_CHANGED'):
            check_receipt(receipt, self.k)

    def test_removed_rule_audit_is_not_accepted(self):
        receipt = fixture_receipt(self.k)
        del receipt['audits']['RHProofSearch.rh_from_gabor']
        with self.assertRaisesRegex(ValueError, 'UNATTESTED_RULE'):
            check_receipt(receipt, self.k, check_files=False)

    def test_missing_typed_rule_is_rejected(self):
        del self.k['goals']['freq']['lean']
        with self.assertRaisesRegex(ValueError, 'UNTYPED_EXECUTABLE'):
            closure(self.k)

    def test_adapter_signature_retains_both_hypotheses(self):
        source = adapter_source(self.k)
        self.assertIn('native_from_freq_and_bound (h0 : freq) (h1 : eventual_bound)', source)
        self.assertIn('exact (RHFrontierClosure20260905.eventual_bound_iff_weil_nonneg h0).mp h1', source)

    def test_metadata_only_review_cannot_change_lean_input(self):
        old = adapter_source(self.k)
        self.k['goals']['arch_fixed_constant']['label'] = 'More precise description'
        self.assertEqual(old, adapter_source(self.k))
        self.k['rules'][3]['requires'] = []
        self.assertNotEqual(old, adapter_source(self.k))

    def test_known_failure_and_scope_controls(self):
        expected = ['REUSE_VERIFIED', 'EXCLUDED_REGISTERED_FIXED_CONSTANT', 'FINITE_DIAGNOSTIC_ONLY',
                    'REJECT_CIRCULAR_CONSTRUCTION', 'REJECT_RESTATEMENT',
                    'EXCLUDED_UNDER_REGISTERED_CORE_COUNTEREXAMPLE', 'OPEN_CONSTRUCTION',
                    'NEEDS_TYPED_SCOPE_BRIDGE', 'NEEDS_TYPED_SCOPE_BRIDGE',
                    'ASSUMED_INPUTS_NOT_DISCHARGED', 'EXCLUDED_UNDER_REGISTERED_PHASE_SCOPE', 'OPEN_CONSTRUCTION']
        self.assertEqual([assess(c, self.k, self.p.facts)['status'] for c in controls(self.k)], expected)

    def test_labels_and_fitness_do_not_create_new_candidates(self):
        c = generate_candidates(self.k)[0]
        self.assertEqual(candidate_id(c), candidate_id(dict(c, label='Breakthrough!', fitness=999, parents=['old'])))

    def test_candidates_never_add_a_fact(self):
        candidates = generate_candidates(self.k)
        self.assertEqual(len(candidates), len({candidate_id(c) for c in candidates}))
        for c in candidates:
            result = assess(c, self.k, self.p.facts)
            self.assertFalse(result['proof_accepted'] or result['new_fact'])

    def test_finite_passes_do_not_become_universal_quantifier(self):
        for n in range(1, 51):
            c = scoped_candidate(self.k, 'gabor_positive', finite_data_only=True, successful_samples=n)
            self.assertEqual(assess(c, self.k, self.p.facts)['status'], 'FINITE_DIAGNOSTIC_ONLY')
        self.assertNotIn('rh', self.p.facts)

    def test_missing_and_mismatched_scope_need_explicit_bridge(self):
        c = scoped_candidate(self.k, 'gabor_positive')
        del c['normalization']
        self.assertEqual(assess(c, self.k, self.p.facts)['status'], 'NEEDS_TYPED_SCOPE_BRIDGE')

    def test_bounded_search_never_claims_exhaustiveness(self):
        p = Planner(self.k, fixture_receipt(self.k), check_files=False, max_expansions=1, beam=1)
        report = p.report(['rh', 'boundary_window'])
        self.assertLessEqual(report['expansions'], 1)
        self.assertFalse(report['complete_search_claim'] or report['RH_proved'])

    def test_invalid_budget(self):
        for budget in [0, -1, 100001, True]:
            with self.assertRaisesRegex(ValueError, 'BAD_EXPANSION'):
                Planner(self.k, fixture_receipt(self.k), check_files=False, max_expansions=budget)

    def test_repeated_plans_are_deterministic(self):
        other = Planner(self.k, fixture_receipt(self.k), check_files=False)
        self.assertEqual(self.p.expand('rh'), other.expand('rh'))

    def test_complete_catalog_retrieval_uses_numeric_score(self):
        from search_rh import prior_art
        rows = prior_art()
        self.assertEqual(len(rows), len(self.k['recipes']))
        self.assertTrue(all(isinstance(hit['score'], float) for r in rows for hit in r['hits']))

    def test_historical_axiom_name_not_confused_with_clean_type(self):
        log = "'X.bad' depends on axioms: [propext, sorryAx]\nTYPE_RECORD {\"name\":\"X.bad\",\"type\":\"Prop\"}"
        row = parse_audits(log)['X.bad']
        self.assertFalse(row['standard_only'])
        self.assertEqual(row['type'], 'Prop')


class RegistryTests(unittest.TestCase):
    def test_nested_comments_and_strings_are_not_evidence(self):
        text = '/- theorem fake : False := sorry /- axiom nested : False -/ -/\n' \
               'def text := "sorry axiom Fake"\n-- admit\ntheorem real (h : P) : P := h\n'
        decls, flags = source_declarations(text)
        self.assertEqual([d['local_name'] for d in decls], ['text', 'real'])
        self.assertEqual(flags, [])
        self.assertTrue(all(d['status'] == 'LEXICAL_NOT_PROOF_CHECKED' for d in decls))

    def test_real_sorry_and_native_decide_are_distinguished(self):
        _, flags = source_declarations('theorem a : P := sorry\ntheorem b : 1=1 := by native_decide\n')
        self.assertEqual([f['kind'] for f in flags], ['placeholder', 'native_evaluation'])

    def test_unclosed_comment_fails(self):
        with self.assertRaisesRegex(ValueError, 'UNTERMINATED_LEAN_COMMENT'):
            strip_lean('/- sorry')

    def test_explicit_prop_axiom_is_not_a_proof(self):
        decls, _ = source_declarations('axiom Seam : Prop\naxiom forcing : Seam\n')
        self.assertEqual([d['kind'] for d in decls], ['axiom', 'axiom'])
        self.assertTrue(all(d['status'] == 'LEXICAL_NOT_PROOF_CHECKED' for d in decls))

    def test_file_scope_duplicates_and_missing_root(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            repo, docs = root / 'repo', root / 'docs'
            a = repo / 'rh/lean/RH'
            b = repo / 'experiments/lean4-carrier-rigidity'
            a.mkdir(parents=True); b.mkdir(parents=True); docs.mkdir()
            (a / 'A.lean').write_text('theorem a : True := True.intro')
            (docs / 'Copy.lean').write_text('theorem a : True := True.intro')
            rows = discover(repo, docs, docs / 'task')
            reg = make_registry(rows)
            self.assertEqual(len(reg['duplicate_groups']), 1)
            self.assertEqual(len(reg['catalog_records']), 1)
            self.assertTrue(reg['catalog_records'][0]['needs_review'])
            old = reg['source_fingerprint']
            (a / 'A.lean').write_text('theorem a : True := by trivial')
            self.assertNotEqual(old, make_registry(discover(repo, docs, docs / 'task'))['source_fingerprint'])
            with self.assertRaisesRegex(ValueError, 'LEAN_SOURCE_ROOT_UNAVAILABLE'):
                discover(repo, root / 'absent', docs / 'task')

    def test_need_remains_active_without_assertions(self):
        with self.assertRaisesRegex(ValueError, 'EXPECTED_GATE'):
            need(False, 'EXPECTED_GATE')


if __name__ == '__main__':
    unittest.main()
