"""Independent boundary language, original-row transport and replay checks."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import islice,product
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('seventh_bound',HERE/'checker.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

def grade(word):return word.count('M')+2*word.count('E')

class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.third,cls.parents,cls.third_record=r.inherited()
        cls.r49,cls.r48,cls.r47,cls.r46,cls.r45,cls.r44,cls.r43,cls.r42,cls.r41,cls.r40,cls.r39,cls.r38,cls.parent=cls.parents
        cls.record=json.loads((HERE/'validation.json').read_text())
        cls.C=[cls.r38.sqrt_interval(x)[1] for x in (F(107,2048),F(1,96))]

    def test_01_complete_disjoint_boundary_language(self):
        language=['M'+''.join(tail) for n in range(1,12) for tail in product('ME',repeat=n)]
        evaluated={w for w in language if 'E' in w and grade(w)<=7}
        self.assertEqual(len(evaluated),26)
        self.assertEqual({w for w in evaluated if grade(w)==7},set(r.WORDS))
        frontier={w+x for w in evaluated for x in 'ME' if w+x not in evaluated}
        retained={w+'ME' for w in ('MEMM','MMEM','MMME','MEE')}|{w+'E' for w in ('MMMME','MEME','MMEE')}
        expected=retained|{w+x for w in r.WORDS for x in 'ME'}
        self.assertEqual(len(frontier),31);self.assertEqual(frontier,expected)
        for w in language:
            if 'E' not in w or w in evaluated:continue
            matching=[b for b in frontier if w.startswith(b)]
            first_late=w.index('E')>=6
            self.assertEqual(len(matching)+int(first_late),1,w)
        self.assertTrue(all(grade(w) in (8,9) for w in frontier))

    def test_02_all_original_hop_rows_match_W_and_J(self):
        for site in ((0,0,0),(2,-1,3)):
            for species in (0,1):
                a=[F(0)]*2;b=a.copy()
                for mode,current,w in self.r40.cubic_row((site,species)):
                    a[mode[1]]+=F(abs(w),576);b[mode[1]]+=F(abs(w)*self.r42.length(current),576)
                self.assertEqual(tuple(a),self.r40.W[species]);self.assertEqual(tuple(b),self.r40.J[species])

    def test_03_tensor_transport_against_original_M_paths(self):
        for arity,seeds in ((3,self.r45.one_e_paths(self.r42,self.r41,self.r40)),(5,self.r45.two_e_paths(self.r42,self.r41,self.r40))):
            paths=list(islice((p for p in seeds if not self.r48.whole_fock_zero(p['word'],self.r45.CREATES[arity])),24))
            a=[F(0)]*(1<<arity);b=a.copy();f=a.copy()
            for p in paths:
                aa,bb=self.third.moments(p['dots'],tuple(map(self.r42.length,p['prefixes'])))
                s=sum(mode[1]<<j for j,mode in enumerate(p['word']));w=F(abs(p['weight']),576**p['order'])
                a[s]+=w*aa;b[s]+=w*bb;f[s]+=w*aa*self.r42.length(p['flux'])
            upper=r.matter_transport(self.r40,a,b,f,arity)
            measured=[[F(0)]*len(a) for _ in range(3)]
            for p in self.r49.append_M(self.r45,self.r42,self.r40,paths,self.r40.cubic_row):
                aa,bb=self.third.moments(p['dots'],tuple(map(self.r42.length,p['prefixes'])))
                s=sum(mode[1]<<j for j,mode in enumerate(p['word']));w=F(abs(p['weight']),576**p['order'])
                for values,v in zip(measured,(aa,bb,aa*self.r42.length(p['flux']))):values[s]+=w*v
            self.assertTrue(any(measured[0]));self.assertEqual(measured[0],upper[0])
            for exact,bound in zip(measured[1:],upper[1:]):self.assertTrue(all(x<=y for x,y in zip(exact,bound)))

    def test_04_compressed_CAR_bound_for_every_species_pattern(self):
        for arity,order in ((3,5),(5,4)):
            for s in range(1<<arity):
                a=[F(int(j==s)) for j in range(1<<arity)]
                b=[(order**2+3)*x for x in a];f=[(2*order-1)*x for x in a]
                aa,bb,_=r.matter_transport(self.r40,a,b,f,arity)
                actual=sum(w*sum(self.C[(pattern>>j)&1] for j in range(arity)) for pattern,w in enumerate(aa))
                car=[F(sum(((s>>j)&1)==species for j in range(arity))) for species in (0,1)]
                A,B=r.compressed_matter(self.r40,self.C,car,sum(b),order,arity)
                self.assertLessEqual(actual,A);self.assertLessEqual(sum(bb),B)

    def test_05_actual_fifth_M_first_E_paths_obey_transport(self):
        # Complete first-E family for a finite set of actual original pure-M
        # prefixes: stopping at a raw output count could omit part of a prefix.
        def walk(mode,flux,prefixes,weight):
            if len(prefixes)==5:
                yield {'mode':mode,'flux':flux,'prefixes':prefixes,'weight':weight}
                return
            for target,current,w in self.r40.cubic_row(mode):
                final=self.r40.merge(flux,current)
                yield from walk(target,final,prefixes+(final,),weight*w)
        prefixes=list(islice(walk(((0,0,0),1),(),(),1),12))
        phase=[F(0)]*2;a=[F(0)]*8;b=a.copy()
        for p in prefixes:
            self.assertEqual(len(p['prefixes']),5)
            lengths=tuple(map(self.r42.length,p['prefixes']))
            old_weight=F(abs(p['weight']),576**5)
            phase[p['mode'][1]]+=old_weight*sum(lengths)
            for left,right,current,w,dots in self.r42.force_terms(self.r40,self.r40.cubic_row,p['prefixes']):
                final=self.r40.merge(p['flux'],current)
                aa,bb=self.third.moments((dots+(0,),),lengths+(self.r42.length(final),))
                pattern=left[1]|(right[1]<<1)|(p['mode'][1]<<2)
                weight=old_weight*F(abs(w),576)
                a[pattern]+=weight*aa;b[pattern]+=weight*bb
        upper=r.first_E_transport(self.third,phase)
        self.assertTrue(any(a));self.assertTrue(any(b))
        self.assertTrue(all(x<=y for x,y in zip(a,upper[0])))
        self.assertTrue(all(x<=y for x,y in zip(b,upper[1])))

    def test_06_exact_partition_time_order_and_all_infinite_tails(self):
        at_one=r.certificate(self.third,self.parents,self.third_record)
        for t in (F(0),F(1,10),F(1,2),F(1)):
            b=r.certificate(self.third,self.parents,self.third_record,t)
            self.assertEqual(b['old49_upper'],b['removed_grade7_boundary']+b['retained_explicit_grade8_boundary']+b['retained_first_E_after_at_least_6M'])
            self.assertEqual(b['upper'],b['retained_explicit_grade8_boundary']+b['retained_first_E_after_at_least_6M']+sum(x['upper'] for x in b['new_branches'].values()))
            self.assertLessEqual(b['upper'],at_one['upper']*t**8)
            if t:self.assertGreater(b['retained_first_E_infinite_tail'],0)
            for name,x in b['new_branches'].items():
                self.assertEqual(x['next_matter'],at_one['new_branches'][name]['next_matter']*t**8)
                self.assertEqual(x['next_electric'],at_one['new_branches'][name]['next_electric']*t**9)
            self.assertEqual(b,r.certificate(self.third,self.parents,self.third_record,-t))

    def test_07_third_E_boundary_exactly_reproduced(self):
        x=r.certificate(self.third,self.parents,self.third_record)['new_branches']['MEEE']
        y=self.third_record['boundary']
        self.assertEqual(x['next_matter'],F(y['MEEEM']));self.assertEqual(x['next_electric'],F(y['MEEEE']))
        self.assertGreater(x['next_electric'],0)

    def test_08_scope_guards_pins_and_complete_replay(self):
        self.assertEqual(r.run(),self.record)
        for key in ('all_new_full_cubic_raw_censuses_executed','combined_bulk_readout_evaluated','old_probability_reused','full_electric_dynamics_solved','T1_T8_solved'):
            self.assertFalse(self.record[key])
        self.assertNotIn('readout',self.record)
        with patch.dict(r.PINS,{'checker.py':'0'*64}):
            with self.assertRaisesRegex(ValueError,'third-E pin'):r.inherited()
        with self.assertRaises(ValueError):r.first_E_transport(self.third,[F(1),F(0)],4)
        with self.assertRaises(ValueError):r.certificate(self.third,self.parents,self.third_record,2)

if __name__=='__main__':unittest.main()
