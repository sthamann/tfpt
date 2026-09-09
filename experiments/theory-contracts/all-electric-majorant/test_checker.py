"""Exact algebra, original rows, all-flux controls and complete replay."""
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from math import factorial,prod
from pathlib import Path
import unittest
from unittest.mock import patch
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('all_E',HERE/'checker.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parents=r.inherited()
        cls.r49,cls.r48,cls.r47,cls.r46,cls.r45,cls.r44,cls.r43,cls.r42,cls.r41,cls.r40,cls.r39,cls.r38,cls.parent=cls.parents
        cls.record=json.loads((HERE/'validation.json').read_text())
        cls.data=cls.r43.geometry(cls.parent,'edge');cls.row=staticmethod(cls.r40.parent_rows(cls.data))

    def test_01_all_order_positive_polynomial_identities(self):
        n,k=s.symbols('n k',integer=True);m=s.symbols('m',nonnegative=True,integer=True)
        beta=n*n+k*(2*n-1)
        self.assertEqual(s.expand((n+k+1)*(n+k+2)-beta),k*k+3*n+4*k+2)
        self.assertEqual(s.expand((n+k+1)-(2*k+1)),n-k)
        self.assertEqual(s.expand((n-k).subs(n,k+m+1)),m+1)
        self.assertEqual(r.MU+r.KAPPA*r.FORCE_L1,F(11603,14400))
        self.assertLess(r.MU+r.KAPPA*r.FORCE_L1,1)
        for n in (1,2,5,16,200,10000):
            for k in set((0,(n-1)//2,n-1)):
                a,b=r.ratios(n,k);self.assertLessEqual(a+b,F(11603,14400))
                self.assertEqual((a,b),r.ratios(n,k,-1))

    def test_02_original_full_cubic_constants(self):
        for species in (0,1):
            actual=sum(F(abs(w),576) for _,_,w in self.r40.cubic_row(((0,0,0),species)))
            self.assertEqual(actual,sum(self.r40.W[species]))
            self.assertLessEqual(actual,r.MU)
        for axis in range(3):
            flux=(((0,0,0,axis),1),)
            actual=sum(F(abs(w*dots[0]),576) for _,_,_,w,dots in self.r42.force_terms(self.r40,self.r40.cubic_row,(flux,)))
            self.assertEqual(actual,r.FORCE_L1)
        self.assertEqual(sum(F(abs(p['weight']),576) for p in r.advance(self.parents,r.initial(),'M')),F(1,4))

    def test_03_general_moments_against_complete_assignments(self):
        for n in (3,4):
            lengths=tuple(2*j+1 for j in range(n))
            for k in range(7):
                dots=tuple(tuple((-1)**(a+j)*(1+(a+j)%3) for j in range(n)) for a in range(k))
                A=B=0
                for assignment in product(range(n),repeat=k):
                    powers=tuple(assignment.count(j) for j in range(n))
                    value=prod(abs(dots[a][assignment[a]]) for a in range(k))*prod(factorial(m) for m in powers)
                    A+=value;B+=value*sum((m+1)*ell for m,ell in zip(powers,lengths))
                self.assertEqual(r.moments(dots,lengths),(A,B))
                self.assertLessEqual(B,(n*n+k*(2*n-1))*A)
        self.assertEqual(r.moments(((0,0),),(1,3)),(0,0))

    def test_04_raw_sign_and_phase_dictionary_matches_old_sources(self):
        def canonical(paths,old=False):
            values=defaultdict(int)
            for p in paths:
                branches=zip(p['frequencies'],p['signs']) if old else r.branches(p)
                for f,sign in branches:values[p['word'],p['flux'],tuple(sorted(f))]+=p['weight']*sign*(-1 if old else 1)
            return {k:v for k,v in values.items() if v}
        for depth in range(1,5):
            old=self.r49.first_e_paths(self.r45,self.r42,self.r40,depth,self.row,0,range(2),False)
            self.assertEqual(canonical(r.paths_for_word(self.parents,'M'*depth+'E',self.row,0,range(2))),canonical(old,True))
        old=list(self.r45.one_e_paths(self.r42,self.r41,self.r40,self.row,0,range(2),False))
        old+=list(self.r45.two_e_paths(self.r42,self.r41,self.r40,self.row,0,range(2),False))
        for word in ('MEMM','MMEM','MMME','MEE'):
            self.assertEqual(canonical(r.paths_for_word(self.parents,word,self.row,0,range(2))),canonical((p for p in old if p['kind']==word),True))

    def test_05_whole_flux_Fock_commutator_with_up_to_seventeen_legs(self):
        phase=((1,0),(0,1),(-1,0),(0,-1))
        terms=[(a,b,dict(current).get(0,0),w) for site in range(2) for species in (0,1)
               for a in ((site,species),) for b,current,w in self.row(a)]
        add=self.r41.add;mul=self.r41.multiply
        def literal(word,mask):
            sign=1
            for (site,species),create in zip(word[::-1],r.creates(word)[::-1]):
                step=self.r41.fermion_action(mask,site+2*species,create)
                if step is None:return None
                mask,parity=step;sign*=parity
            return mask,sign
        def bilinear(a,b,mask):
            first=self.r41.fermion_action(mask,b[0]+2*b[1],False)
            if first is None:return None
            last=self.r41.fermion_action(first[0],a[0]+2*a[1],True)
            return None if last is None else (last[0],first[1]*last[1])
        for k in range(9):
            word=((0,0),(0,0))*k+((0,1),)
            for theta in (1,3):
                for electric in (-3,0,4):
                    for mask in range(16):
                        exact=defaultdict(lambda:(0,0));split=defaultdict(lambda:(0,0));R=1
                        original=literal(word,mask)
                        for a,b,p,w in terms:
                            if original:
                                step=bilinear(a,b,original[0])
                                if step:
                                    key=step[0],electric+R+p
                                    exact[key]=add(exact[key],tuple(w*original[1]*step[1]*x for x in phase[(theta*electric)%4]))
                            first=bilinear(a,b,mask)
                            if first:
                                step=literal(word,first[0])
                                if step:
                                    key=step[0],electric+p+R
                                    exact[key]=add(exact[key],tuple(-w*first[1]*step[1]*x for x in phase[(theta*(electric+p))%4]))
                            # Electric part: original bilinear prepended, no arity cap.
                            step=literal((a,b)+word,mask)
                            if step:
                                delta=add(phase[(theta*electric)%4],tuple(-x for x in phase[(theta*(electric+p))%4]))
                                key=step[0],electric+R+p
                                split[key]=add(split[key],tuple(w*step[1]*x for x in delta))
                        for leg,(mode,create) in enumerate(zip(word,r.creates(word))):
                            for target,current,w in self.row(mode):
                                p=dict(current).get(0,0)*(-1 if create else 1)
                                step=literal(word[:leg]+(target,)+word[leg+1:],mask)
                                if step:
                                    key=step[0],electric+R+p
                                    split[key]=add(split[key],tuple(w*(1 if create else -1)*step[1]*x for x in phase[(theta*(electric+p))%4]))
                        clean=lambda v:{key:z for key,z in v.items() if z!=(0,0)}
                        self.assertEqual(clean(exact),clean(split))

    def test_06_eighth_E_normal_form_and_no_initial_E(self):
        self.assertEqual(list(r.advance(self.parents,r.initial(),'E')),[])
        p=next(r.advance(self.parents,r.initial(0),'M',self.row,range(2)))
        for _ in range(8):
            p=next(q for q in r.advance(self.parents,p,'E',self.row,range(2))
                   if not self.r48.whole_fock_zero(q['word'],r.creates(q['word'])))
        self.assertEqual(len(p['word']),17);self.assertEqual(len(p['dots']),8)
        self.assertEqual(len(list(r.branches(p))),256)
        self.assertTrue(all(d[-1]==0 for d in p['dots']))
        self.assertTrue(all(self.r42.length(current)<=2*j+1 for j,current in enumerate(p['prefixes'])))

    def test_07_refined_majorant_and_whole_tail(self):
        for T in (F(0),F(1,4),F(1)):
            x=r.majorant(40,T);rho=x['rho']
            for row in x['rows']:
                self.assertEqual(row['level_norm_upper'],sum(row['electric_count_weights'].values()))
                self.assertLessEqual(row['level_norm_upper'],row['coarse_level_upper'])
                self.assertEqual(row['all_later_events_tail_upper'],row['level_norm_upper']*rho/(1-rho))
                if T:self.assertGreater(row['electric_count_weights'][row['events']-1],0)
            self.assertEqual(x,r.majorant(40,-T))
            self.assertLessEqual(sum(row['level_norm_upper'] for row in x['rows'][16:]),x['rows'][15]['all_later_events_tail_upper'])

    def test_08_unsplit_Hamiltonian_controls_and_exact_replay(self):
        self.assertEqual(r.run(),self.record)
        gate=self.record['independent_physical_gate']
        self.assertTrue(gate['four_E_source_executed_in_finite_control'])
        for item in gate['checks']:
            self.assertTrue(item['all_coefficients_match']);self.assertEqual(item['all_input_columns'],6)
            self.assertEqual(item['interaction_depth'],5);self.assertEqual(item['time_jet_degree'],12)
        self.assertEqual({x['background_flux'] for x in gate['checks']},{0,3,-4})

    def test_09_scope_hashes_and_guards(self):
        for name,digest in self.record['sources'].items():self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest)
        for key in ('global_automorphism_group_constructed','continuum_dynamics_constructed','new_bulk_occupation_evaluated','parameters_or_preparation_selected','T1_T8_solved'):
            self.assertFalse(self.record[key])
        self.assertFalse(self.record['majorant']['tail_may_be_applied_to_Round50_column'])
        with patch.dict(r.PINS,{'checker.py':'0'*64}):
            with self.assertRaisesRegex(ValueError,'frontier-bound pin'):r.inherited()
        for args in ((0,0),(2,2),(3,-1)):
            with self.assertRaises(ValueError):r.ratios(*args)
        with self.assertRaises(ValueError):r.majorant(4,2)

    def test_10_many_phase_factors_and_missing_branch_mutant(self):
        p=next(r.advance(self.parents,r.initial(0),'M',self.row,range(2)))
        for _ in range(8):
            p=next(q for q in r.advance(self.parents,p,'E',self.row,range(2))
                   if not self.r48.whole_fock_zero(q['word'],r.creates(q['word'])))
        values={p['base']:1}
        for d in p['dots']:
            updated=defaultdict(int);delta=(0,)+tuple(24*x for x in d)
            for f,w in values.items():
                updated[f]+=w;updated[tuple(x+y for x,y in zip(f,delta))]-=w
            values={f:w for f,w in updated.items() if w}
        bitmask=defaultdict(int)
        branch_list=list(r.branches(p))
        for f,w in branch_list:bitmask[f]+=w
        self.assertEqual(values,{f:w for f,w in bitmask.items() if w})
        self.assertTrue(values)
        # The first n-th time coefficient is proportional to this sum.
        self.assertEqual(sum(w for _,w in branch_list),0)
        self.assertNotEqual(sum(w for _,w in branch_list[:-1]),0)
        q=next(r.advance(self.parents,p,'M',self.row,range(2)))
        self.assertEqual(len(q['word']),17);self.assertEqual(len(q['dots']),8)
        self.assertEqual(q['order'],10)
        with self.assertRaisesRegex(ValueError,'electric-event implementation guard'):
            list(r.advance(self.parents,p,'E',self.row,range(2)))

if __name__=='__main__':unittest.main()
