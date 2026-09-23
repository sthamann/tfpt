"""Research infrastructure regressions, never evidence for RH."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import paper_knowledge as papers
from proof_search.common import CATALOG, dump, read, sha
from research_engine import explorer, source_index
from analysis.analyze_paths import t5_conflicts
from research_cycle import locked, concise


class PaperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root/'paper.tex'; self.source.write_text('A \\label{claim} original statement')
        self.reviews = self.root/'reviews.json'
        dump(self.reviews, {'papers':[{'path':'paper.tex','id':'paper-one','title':'Paper',
            'aliases':['copy.tex'],'review_sha256':sha(self.source), 'claims':[{
                'id':'claim-one','title':'Claim','anchor':'\\label{claim}', 'statement':'Finite scope.',
                'requires':['Positive input','Full domain'],'state':'SOURCE_REVIEWED'}]}]})
        (self.root/'copy.tex').write_text(self.source.read_text())

    def build(self):
        with patch.object(papers,'CATALOG',self.root), patch.object(papers,'REPO',self.root):
            return papers.build(self.root,self.reviews)

    def test_review_is_not_proof(self):
        c=self.build()['claims'][0]
        self.assertEqual(c['state'],'SOURCE_REVIEWED')
        self.assertFalse(c['proof_rule_eligible'])
        self.assertEqual(c['premise_logic'],'ALL_REQUIRED')
        self.assertEqual(len(c['requires']),2)

    def test_source_change_invalidates_review(self):
        self.source.write_text('Changed \\label{claim}')
        self.assertEqual(self.build()['claims'][0]['state'],'STALE_SOURCE')

    def test_source_removal_is_visible(self):
        self.source.unlink()
        self.assertEqual(self.build()['claims'][0]['state'],'STALE_SOURCE')

    def test_anchor_must_exist_even_if_hash_is_updated(self):
        self.source.write_text('Different statement without a label')
        r=read(self.reviews); r['papers'][0]['review_sha256']=sha(self.source); dump(self.reviews,r)
        self.assertEqual(self.build()['claims'][0]['state'],'STALE_SOURCE')

    def test_alias_identity_is_not_assumed(self):
        self.assertTrue(self.build()['documents'][0]['aliases_current'][0]['identical'])
        (self.root/'copy.tex').write_text('different revision')
        self.assertFalse(self.build()['documents'][0]['aliases_current'][0]['identical'])

    def test_new_root_paper_enters_freshness_boundary(self):
        before=self.build()['source_fingerprint']
        (self.root/'new.tex').write_text('Not reviewed')
        after=self.build()
        self.assertNotEqual(before,after['source_fingerprint'])
        self.assertIn('new.tex',after['unreviewed_root_tex'])

    def test_pdf_and_style_changes_enter_boundary(self):
        (self.root/'paper.pdf').write_bytes(b'%PDF diagnostic only')
        style=self.root/'tex-artefacts/a.sty'; style.parent.mkdir(); style.write_text('A')
        first=self.build()['source_fingerprint']; style.write_text('B')
        self.assertNotEqual(first,self.build()['source_fingerprint'])

    def test_unreviewed_environments_and_sections_are_visible_not_proven(self):
        self.source.write_text(self.source.read_text()+r'\section{New section}\begin{lemma}\label{new} Unreviewed assertion.\end{lemma}')
        result=self.build()
        discovered=[c for c in result['claims'] if c['state']=='SOURCE_DISCOVERED']
        self.assertEqual(len(discovered),1)
        self.assertIn('Unreviewed assertion',discovered[0]['source_body'])
        self.assertFalse(discovered[0]['proof_rule_eligible'])
        self.assertEqual(result['summary']['section_review_targets'],1)

    def test_graph_summary_is_bounded_but_full_source_is_retained(self):
        self.source.write_text(r'\begin{lemma}'+('Long statement '*100)+r'\end{lemma}')
        result=self.build()
        with patch.object(papers,'read',return_value=result):
            nodes,_=papers.graph_rows()
        self.assertTrue(all(len(n['definition'].split())<=60 for n in nodes))
        self.assertTrue(any(len(c['statement'].split())>100 for c in result['claims']))

    def test_reviewed_environment_is_not_duplicated(self):
        self.source.write_text(r'\begin{lemma}\label{claim} original statement\end{lemma}')
        result=self.build()
        self.assertEqual(len(result['claims']),1)

    def test_result_evidence_drift_is_not_a_current_refutation(self):
        c=explorer.generate(read(CATALOG/'research_engine/motifs.json')['motifs'],read(CATALOG/'research_engine/motifs.json')['methods'])[0]
        cid=explorer.identifier(c)
        dump(self.root/'research_engine/submissions'/f'{cid}.json',c)
        evidence=self.root/'evidence.md'; evidence.write_text('Exact scoped negative')
        dump(self.root/'research_engine/results'/f'{cid}-receipt.json',
             {'result':'REFUTED_SCOPED','evidence':str(evidence),'evidence_sha256':sha(evidence)})
        self.assertEqual(self.build()['submissions'][0]['results'][0]['effective_result'],'REFUTED_SCOPED')
        evidence.write_text('Changed evidence')
        self.assertEqual(self.build()['submissions'][0]['results'][0]['effective_result'],'STALE_EVIDENCE')


class ClaimIdentityTests(unittest.TestCase):
    def test_different_claims_same_paper_are_not_one_object(self):
        records=[{'path':'paper.tex#claim-a','role':'paper_claim','outcome':'RESTATED'},
                 {'path':'paper.tex#claim-b','role':'paper_claim','outcome':'KILLED'}]
        self.assertEqual(t5_conflicts(records),[])

    def test_same_claim_conflict_is_kept(self):
        records=[{'path':'paper.tex#claim-a','role':'paper_claim','outcome':'RESTATED'},
                 {'path':'paper.tex#claim-a','role':'paper_claim','outcome':'KILLED'}]
        self.assertTrue(t5_conflicts(records))

    def test_shared_ledger_still_conflicts(self):
        records=[{'path':'paper.tex#a','role':'paper_claim','outcome':'RESTATED','ledger_ids':['same']},
                 {'path':'paper.tex#b','role':'paper_claim','outcome':'KILLED','ledger_ids':['same']}]
        self.assertTrue(t5_conflicts(records))


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name); self.sources=self.root/'sources'; self.sources.mkdir()
        self.db=self.root/'db.sqlite'
        self.config={'roots':[{'id':'test','path':str(self.sources)}], 'extensions':['.md','.json','.pdf'],
                     'explicit_files':[], 'document_text_cap':200, 'other_text_cap':20,
                     'include_registered_lean':False}
        (self.sources/'note.md').write_text('Signed arithmetic correlation and rank three geometry.')

    def scan(self): return source_index.discover(self.config)
    def refresh(self): return source_index.refresh(self.scan(), database=self.db,publish=False)

    def test_search_and_incremental_noop(self):
        self.refresh()
        self.assertTrue(source_index.search('arithmetic',database=self.db))
        self.assertEqual(self.refresh()['changed_files'],[])

    def test_new_changed_deleted_files(self):
        self.refresh(); p=self.sources/'new.md'; p.write_text('new observation')
        self.assertIn(str(p),self.refresh()['changed_files'])
        p.write_text('new changed observation')
        self.assertIn(str(p),self.refresh()['changed_files'])
        p.unlink(); self.assertIn(str(p),self.refresh()['deleted_files'])

    def test_binary_and_partial_coverage_reported(self):
        (self.sources/'large.json').write_text('x'*80)
        (self.sources/'paper.pdf').write_bytes(b'%PDF data')
        r=self.refresh()
        self.assertEqual(r['coverage'],{'full_text':1,'partial_text':1,'hash_only':1})
        self.assertFalse(r['all_sources_semantically_reviewed'])

    def test_changes_after_text_cap_are_detected(self):
        p=self.sources/'large.json'; p.write_text('a'*100)
        before=self.scan()['fingerprint']; p.write_text('a'*99+'b')
        self.assertNotEqual(before,self.scan()['fingerprint'])

    def test_unavailable_root_fails(self):
        self.config['roots'][0]['path']=str(self.root/'missing')
        with self.assertRaisesRegex(ValueError,'INDEX_ROOT_UNAVAILABLE'): self.scan()

    def test_custom_named_python_environments_are_excluded(self):
        env=self.sources/'custom-env'; env.mkdir(); (env/'pyvenv.cfg').write_text('include-system-site-packages=false')
        p=env/'dependency.md'; p.write_text('Not project research')
        self.assertNotIn(str(p),self.scan()['files'])

    def test_text_coverage_config_is_part_of_freshness(self):
        first=self.scan()['fingerprint']
        self.config['document_text_cap']=1000
        self.assertNotEqual(first,self.scan()['fingerprint'])

    def test_symlink_is_explicitly_skipped(self):
        target=self.root/'elsewhere.md'; target.write_text('Outside scope')
        link=self.sources/'link.md'; link.symlink_to(target)
        snap=self.scan()
        self.assertIn(str(link),snap['skipped_symlinks'])
        self.assertNotIn(str(link),snap['files'])

    def test_query_syntax_is_not_executable(self):
        self.refresh()
        self.assertEqual(source_index.search('\" OR * )',database=self.db),[])
        self.assertTrue(source_index.search('rank',database=self.db))

    def test_retrieval_prefers_joint_terms_and_collapses_identical_copies(self):
        (self.sources/'copy.md').write_text((self.sources/'note.md').read_text())
        (self.sources/'distractor.md').write_text('arithmetic '*100)
        self.refresh()
        hits=source_index.search('arithmetic geometry',database=self.db)
        self.assertEqual(len(hits),1)
        self.assertEqual(hits[0]['match_mode'],'ALL_TERMS')
        self.assertEqual(len(hits[0]['identical_source_paths']),2)


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.config=read(CATALOG/'research_engine/motifs.json')
        self.knowledge=read(CATALOG/'proof_search/knowledge.json')
        self.constraints=read(CATALOG/'proof_search/constraints.json')
        self.candidates=explorer.generate(self.config['motifs'],self.config['methods'])
        self.c=copy.deepcopy(self.candidates[0])

    def assess(self,c=None,claims=None):
        return explorer.assess(c or self.c,claims or [],self.knowledge,self.constraints)

    def test_grammar_is_diverse_and_no_proofs(self):
        self.assertEqual(len(self.candidates),24)
        self.assertEqual(len({explorer.identifier(c) for c in self.candidates}),24)
        self.assertEqual(len({c['domain'] for c in self.candidates}),8)
        for c in self.candidates:
            self.assertFalse(self.assess(c)['proof_accepted'])
            self.assertFalse(self.assess(c)['new_fact'])

    def test_labels_do_not_make_new_math_objects(self):
        cid=explorer.identifier(self.c); self.c['label']='miracle breakthrough'
        self.c['fitness']=999
        self.assertEqual(cid,explorer.identifier(self.c))

    def test_self_promotion_is_rejected(self):
        self.c['proof_accepted']=True
        with self.assertRaisesRegex(ValueError,'SELF_PROMOTION_FORBIDDEN'): self.assess()

    def test_refuted_or_stale_premise_is_blocked(self):
        self.c['asserted_claims']=['bad']
        for state in ('REFUTED','STALE_SOURCE','SOURCE_DISCOVERED'):
            self.assertEqual(self.assess(claims=[{'id':'bad','state':state}])['status'],'BLOCKED_SCOPED_FILTER')

    def test_target_assumption_and_finite_global_claims_blocked(self):
        self.c['assumes_target']=True
        self.assertIn('CIRCULAR_TARGET_PREMISE',self.assess()['reasons'])
        self.c['finite_only']=True; self.c['claims_global']=True
        self.assertIn('FINITE_TO_GLOBAL_WITHOUT_PROOF',self.assess()['reasons'])

    def test_new_domain_is_allowed_but_unmapped_goal_needs_review(self):
        self.c['domain']='unlisted new approach'; self.c['target']='novel_target'
        self.assertIn('UNMAPPED_TARGET_REQUIRES_REVIEW',self.assess()['reasons'])

    def test_exposure_changes_ranking_and_diversity(self):
        graph={'nodes':[], 'edges':[]}
        initial=explorer.rank(self.candidates,{},self.knowledge,graph)
        top=initial[0][1]
        ranked=explorer.rank(self.candidates,{top:{'exposures':20}},self.knowledge,graph)
        self.assertNotEqual(top,ranked[0][1])
        selected=explorer.choose(ranked,6)
        self.assertEqual(len({r[2]['domain'] for r in selected}),6)

    def test_exact_controls_do_not_claim_prime_or_global_tests(self):
        result=explorer.exact_controls()
        self.assertTrue(result['rank_two_counterexample'])
        self.assertEqual(result['zero_rung'],'0')
        self.assertEqual(result['real_prime_windows_tested'],0)
        self.assertFalse(result['RH_proved'])

    def test_historical_penalty_requires_unchanged_evidence(self):
        graph={'nodes':[], 'edges':[]}
        baseline=explorer.rank([self.c],{},self.knowledge,graph)[0][0]
        with tempfile.TemporaryDirectory() as folder:
            evidence=Path(folder)/'negative.md'; evidence.write_text('Scoped evidence')
            history={explorer.identifier(self.c):{'result':'REFUTED_SCOPED',
                      'result_evidence':str(evidence),'result_evidence_sha256':sha(evidence)}}
            self.assertEqual(explorer.rank([self.c],history,self.knowledge,graph)[0][0],baseline-100)
            evidence.write_text('Changed evidence')
            self.assertEqual(explorer.rank([self.c],history,self.knowledge,graph)[0][0],baseline)

    def test_cycle_lock_rejects_overlap(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'lock'
            with locked(path):
                with self.assertRaisesRegex(ValueError,'ANOTHER_RESEARCH_CYCLE'):
                    with locked(path): pass

    def test_output_is_bounded_without_mutating_full_checkpoint(self):
        full={'source_index':{'changed_files':['a','b'], 'file_count':2}}
        result=concise(full)
        self.assertNotIn('changed_files',result['source_index'])
        self.assertEqual(result['source_index']['changed_files_count'],2)
        self.assertEqual(full['source_index']['changed_files'],['a','b'])


if __name__=='__main__': unittest.main()
