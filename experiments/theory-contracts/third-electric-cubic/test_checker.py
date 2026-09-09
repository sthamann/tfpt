"""Independent whole-CAR, raw-force, phase, finite-matrix and replay checks."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import islice, product
import json
from math import factorial, prod
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('third_E',HERE/'checker.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parents=r.inherited(r.ROOT)
        cls.r49,cls.r48,cls.r47,cls.r46,cls.r45,cls.r44,cls.r43,cls.r42,cls.r41,cls.r40,cls.r39,cls.r38,cls.parent=cls.parents
        cls.record=json.loads((HERE/'validation.json').read_text())

    def test_01_seven_leg_zero_rule_and_partial_isometry_exhaustively(self):
        nonzero=0;zero=0
        for word in product(range(4),repeat=7):
            outputs=[]
            for initial in range(16):
                current=initial
                for mode,create in zip(word[::-1],r.CREATES[::-1]):
                    step=self.r41.fermion_action(current,mode,create)
                    if step is None:break
                    current,sign=step;self.assertIn(sign,(-1,1))
                else:outputs.append(current)
            self.assertEqual(self.r48.whole_fock_zero(word,r.CREATES),not outputs)
            self.assertEqual(len(set(outputs)),len(outputs))
            nonzero+=bool(outputs);zero+=not outputs
        self.assertGreater(nonzero,0);self.assertGreater(zero,0)

    def test_02_polynomial_moments_match_independent_assignments(self):
        for n in (3,4,5):
            for k in (1,2,3,4):
                dots=tuple(tuple((-1)**(i+j)*(i+j+1) for j in range(n)) for i in range(k))
                lengths=tuple(range(n));a=b=0
                for choice in product(range(n),repeat=k):
                    counts=tuple(choice.count(j) for j in range(n))
                    w=prod(abs(dots[i][choice[i]]) for i in range(k))*prod(factorial(m) for m in counts)
                    a+=w;b+=w*sum((m+1)*ell for m,ell in zip(counts,lengths))
                self.assertEqual(r.moments(dots,lengths),(a,b))
                if k<3:self.assertEqual((a,b),self.r45.moment_factors(dots,lengths))

    def test_03_full_cubic_census_matches_original_force_scan(self):
        with tempfile.TemporaryDirectory() as folder:
            paths=r.append_E(self.parents,self.r45.two_e_paths(self.r42,self.r41,self.r40),indexed=False)
            census,groups=r.census_groups(self.parents,paths,folder)
            self.assertEqual(self.r38.encode(census),self.record['census'])
            self.assertEqual(groups['cost']['groups'],self.record['frequency_group_count'])

    def test_04_whole_zero_and_initial_zero_counts_are_different(self):
        c=self.record['census']
        self.assertEqual(c['raw_count'],441456)
        self.assertEqual(c['whole_fock_zero_count'],346236)
        self.assertEqual(c['nonzero_bare_action_count'],4980)
        self.assertGreater(c['raw_count']-c['whole_fock_zero_count'],c['nonzero_bare_action_count'])
        self.assertGreater(sum(map(F,c['vectors']['raw_matter'])),sum(map(F,c['vectors']['nonzero_matter'])))

    def test_05_eight_phase_branches_and_missing_branch_mutant(self):
        paths=r.append_E(self.parents,self.r45.two_e_paths(self.r42,self.r41,self.r40))
        for p in islice(paths,40):
            self.assertEqual(len(p['frequencies']),8)
            self.assertEqual(len(p['word']),7)
            self.assertTrue(all(not self.r49.electric_jet([p],j) for j in range(7)))
            bad={**p,'frequencies':p['frequencies'][:-1],'signs':p['signs'][:-1]}
            self.assertTrue(self.r49.electric_jet([bad],4))

    def test_06_original_complete_physical_edge_witness(self):
        self.assertEqual(r.edge_gate(self.parents),self.record['edge'])
        self.assertEqual(self.record['edge']['raw_count'],216)
        self.assertTrue(any(map(F,self.record['edge']['physical_matrix'])))

    def test_07_literal_simplexes_match_grouped_physical_source(self):
        paths=[]
        for p in r.append_E(self.parents,self.r45.two_e_paths(self.r42,self.r41,self.r40)):
            if self.r47.relative_action(p['word'],r.CREATES):paths.append(p)
            if len(paths)==8:break
        self.assertEqual(len(paths),8)
        expected=defaultdict(lambda:(F(0),F(0)))
        for p in paths:
            flips,parity=self.r47.relative_action(p['word'],r.CREATES)
            for f,sign in zip(p['frequencies'],p['signs']):
                value,_=self.r39.simplex_integral(tuple(F(x,2400) for x in f),F(1),24)
                key=flips,p['flux'];a,b=expected[key]
                w=F(-sign*parity*p['weight'],576**4)
                expected[key]=a+w*value[0],b+w*value[1]
        expected={key:value for key,value in expected.items() if value!=(0,0)}
        with tempfile.TemporaryDirectory() as folder:
            _,grouped=r.census_groups(self.parents,iter(paths),folder,1)
            compiled=self.r47.compile_groups(self.r41,self.r39,grouped,degree=24)
            actual={self.r47.decode_output(key):tuple(F(x,compiled['denominator']) for x in value)
                    for key,value in compiled['vector'].items()}
        self.assertEqual(actual,expected);self.assertTrue(actual)

    def test_08_fourth_electric_boundary_and_time_orders(self):
        c=dict(self.record['census']);c['vectors']={k:list(map(F,v)) for k,v in c['vectors'].items()}
        b=r.boundary(self.parents,c)
        self.assertEqual(self.r38.encode(b),self.record['boundary'])
        self.assertGreater(b['MEEEE'],0);self.assertLess(b['upper'],b['old_MEEE_upper'])
        for t in (F(0),F(1,10),F(1,2),F(1)):
            x=r.boundary(self.parents,c,t)
            self.assertEqual(x['MEEEM'],b['MEEEM']*t**8)
            self.assertEqual(x['MEEEE'],b['MEEEE']*t**9)
            self.assertEqual(x['old_MEEE_upper'],b['old_MEEE_upper']*t**7)
            self.assertEqual(x,r.boundary(self.parents,c,-t))

    def test_09_isolated_column_is_not_a_combined_probability_claim(self):
        x=self.record
        self.assertGreater(F(x['isolated_source_squared_norm']),0)
        self.assertTrue(x['whole_cubic_source_evaluated'])
        for key in ('combined_bulk_readout_evaluated','new_global_time_order_claimed','full_electric_dynamics_solved','T1_T8_solved'):
            self.assertFalse(x[key])
        self.assertNotIn('readout',x)

    def test_10_pins_domains_and_incomplete_census_guard(self):
        with patch.dict(r.PINS,{'checker.py':'0'*64}):
            with self.assertRaisesRegex(ValueError,'frontier pin'):r.inherited(r.ROOT)
        with self.assertRaises(ValueError):r.moments(((1,2),),(1,-1))
        c={**self.record['census'],'raw_count':1}
        with self.assertRaisesRegex(ValueError,'complete whole-cubic'):r.boundary(self.parents,c)

    def test_11_complete_deterministic_replay(self):
        self.assertEqual(r.run(),self.record)

    def test_12_original_link_incidence_matrices(self):
        for origin in ((0,0,0),(2,-1,3)):
            for axis in range(3):
                for sign in (-1,1):
                    flux=((origin+(axis,),sign),)
                    a=[[F(0)]*2 for _ in range(2)];b=[[F(0)]*2 for _ in range(2)]
                    for left,right,current,w,dots in self.r42.force_terms(self.r40,self.r40.cubic_row,(flux,)):
                        value=F(abs(w*dots[0]),576)
                        a[left[1]][right[1]]+=value;b[left[1]][right[1]]+=value*self.r42.length(current)
                    self.assertEqual(tuple(map(tuple,a)),r.FORCE_INCIDENCE)
                    self.assertEqual(tuple(map(tuple,b)),r.FORCE_LENGTH_INCIDENCE)

    def test_13_new_E_transport_against_actual_original_paths(self):
        tr=self.record['positive_E_transport']['MEEE']['tensors']
        for actual,upper in (('nonzero_matter','matter_upper'),('nonzero_phase','phase_upper')):
            self.assertTrue(all(F(x)<=F(y) for x,y in zip(self.record['census']['vectors'][actual],tr[upper])))
        selected=[]
        for p in self.r45.one_e_paths(self.r42,self.r41,self.r40):
            if not self.r48.whole_fock_zero(p['word'],self.r45.CREATES[3]):selected.append(p)
            if len(selected)==12:break
        phase=[F(0)]*8;a=[F(0)]*32;b=a.copy()
        for p in selected:
            _,old_b=r.moments(p['dots'],tuple(map(self.r42.length,p['prefixes'])))
            s=sum(mode[1]<<j for j,mode in enumerate(p['word']))
            phase[s]+=F(abs(p['weight'])*old_b,576**4)
            for left,right,current,w,dots in self.r42.force_terms(self.r40,self.r40.cubic_row,p['prefixes']):
                final=self.r40.merge(p['flux'],current)
                new_dots=tuple(d+(0,) for d in p['dots'])+(dots+(0,),)
                aa,bb=r.moments(new_dots,tuple(map(self.r42.length,p['prefixes']+(final,))))
                target=(s<<2)|left[1]|(right[1]<<1);weight=F(abs(p['weight']*w),576**5)
                a[target]+=weight*aa;b[target]+=weight*bb
        upper=r.electric_transport(phase,4,1)
        self.assertTrue(any(a));self.assertTrue(any(b))
        self.assertTrue(all(x<=y for x,y in zip(a,upper['matter_upper'])))
        self.assertTrue(all(x<=y for x,y in zip(b,upper['phase_upper'])))

    def test_14_every_group_preserves_original_charged_Gauss_sector(self):
        with tempfile.TemporaryDirectory() as folder:
            _,grouped=r.census_groups(self.parents,r.append_E(self.parents,self.r45.two_e_paths(self.r42,self.r41,self.r40)),folder)
            checked=0
            for key,_,_ in self.r47.iter_groups(grouped):
                flips,flux=self.r47.decode_output(key);charge=defaultdict(int)
                for site,species in flips:charge[site]+=1 if species else -1
                for edge,value in flux:
                    a=edge[:3];b=tuple(a[j]+int(j==edge[3]) for j in range(3))
                    charge[a]+=value;charge[b]-=value
                self.assertEqual({site:value for site,value in charge.items() if value},{(0,0,0):-1})
                checked+=1
            self.assertEqual(checked,2355)

if __name__=='__main__':unittest.main()
