"""Independent integer grouping, CAR embeddings and all-later-M tail tests."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import islice, product
import json
from math import lcm
from pathlib import Path
import struct
import subprocess
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("bulk_word47", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def append_M(r45, r42, r40, paths, row):
    out = []
    for p in paths:
        creates = r45.CREATES[len(p["word"])]
        for leg, (mode, create) in enumerate(zip(p["word"], creates)):
            for target, shift, weight in row(mode):
                if create:
                    shift = tuple((edge, -value) for edge, value in shift)
                word = p["word"][:leg]+(target,)+p["word"][leg+1:]
                flux = r40.merge(p["flux"], shift)
                delta = (0,)+tuple(24*r42.dot(prefix, shift) for prefix in p["prefixes"])
                energy = sum((1 if c else -1)*(25 if m[1] == 0 else 9600) for m, c in zip(word, creates))
                final = 12*r42.dot(flux, flux)+energy
                out.append({**p, "word": word, "flux": flux, "order": p["order"]+1,
                    "weight": p["weight"]*weight*(1 if create else -1),
                    "prefixes": p["prefixes"]+(flux,), "dots": tuple(d+(0,) for d in p["dots"]),
                    "frequencies": tuple(tuple(a+b for a, b in zip(f, delta))+(final,) for f in p["frequencies"])})
    return out


def scalar_source(r41, r39, r45, paths, degree=80):
    values, error = defaultdict(lambda: (F(0), F(0))), F(0)
    for p in paths:
        n = p["order"]
        phase = ((-1, 0), (0, -1), (1, 0), (0, 1))[n % 4]
        for f, sign in zip(p["frequencies"], p["signs"]):
            z, tail = r39.simplex_integral(tuple(F(x, 2400) for x in f), F(1), degree)
            a, b = r41.multiply(phase, z)
            weight = F(sign*p["weight"], 576**n)
            key = p["word"], p["flux"]
            values[key] = r41.add(values[key], (weight*a, weight*b))
            error += abs(weight)*tail
    den = lcm(*(x.denominator for z in values.values() for x in z))
    return {"coefficients": {key: (int(a*den), int(b*den)) for key, (a, b) in values.items()},
            "denominator": den, "numerical_error": error, "time": F(1), "creates": r45.CREATES[len(paths[0]["word"])]}


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r46, cls.r45, cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.tmp = tempfile.TemporaryDirectory(prefix="tfpt47-tests-")
        cls.exe = r.build_native(cls.tmp.name)
        cls.one = list(islice(cls.r45.one_e_paths(cls.r42, cls.r41, cls.r40), 48))
        cls.two = list(islice(cls.r45.two_e_paths(cls.r42, cls.r41, cls.r40), 48))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def grouped(self, paths, steps=1):
        arity = len(paths[0]["word"])
        return r.group_native(self.r45, self.r42, self.exe, self.tmp.name, iter(paths), arity,
                              paths[0]["order"], steps, multiplicity=1)

    def reference_groups(self, paths):
        values = defaultdict(int)
        for p in paths:
            result = r.relative_action(p["word"], self.r45.CREATES[len(p["word"])])
            if result:
                for f, sign in zip(p["frequencies"], p["signs"]):
                    values[result[0], p["flux"], tuple(sorted(f))] += p["weight"]*sign*result[1]
        return {key: value for key, value in values.items() if value}

    def test_native_free_grouping_against_python(self):
        for paths in (self.one, self.two):
            g = self.grouped(paths, 0)
            actual = {(*r.decode_output(key), f): weight for key, f, weight in r.iter_groups(g)}
            self.assertEqual(actual, self.reference_groups(paths))

    def test_native_suffix_grouping_against_explicit_python_paths(self):
        for paths in (self.one, self.two):
            g = self.grouped(paths)
            explicit = append_M(self.r45, self.r42, self.r40, paths, self.r40.cubic_row)
            actual = {(*r.decode_output(key), f): weight for key, f, weight in r.iter_groups(g)}
            self.assertEqual(actual, self.reference_groups(explicit))
            self.assertEqual(g["cost"]["raw_extensions"], len(explicit))

    def test_relative_CAR_against_full_filled_cube(self):
        sites = tuple(product(range(-2, 3), repeat=3))
        index = {site: j for j, site in enumerate(sites)}
        bare = sum(1 << (2*j) for j in range(len(sites)))
        for p in self.one+self.two:
            word = tuple((tuple(max(-2, min(2, x)) for x in site), species) for site, species in p["word"])
            creates = self.r45.CREATES[len(word)]
            mask, parity = bare, 1
            for (site, species), create in zip(word[::-1], creates[::-1]):
                step = self.r41.fermion_action(mask, 2*index[site]+species, create)
                if step is None:
                    expected = None
                    break
                mask, sign = step
                parity *= sign
            else:
                flips = tuple((site, species) for site in sites for species in (0, 1)
                              if ((mask ^ bare) >> (2*index[site]+species)) & 1)
                expected = flips, parity
            self.assertEqual(r.relative_action(word, creates), expected)

    def test_rotation_cocycle_against_rotating_literal_words(self):
        for p in self.one+self.two:
            creates = self.r45.CREATES[len(p["word"])]
            old = r.relative_action(p["word"], creates)
            if not old:
                continue
            for axis in range(3):
                for sign in (-1, 1):
                    word = tuple((self.r45.rotate_point(site, axis, sign), species) for site, species in p["word"])
                    new = r.relative_action(word, creates)
                    (flips, flux), parity = r.rotate_output(self.r45, old[0], p["flux"], axis, sign)
                    self.assertEqual((flips, old[1]*parity), new)
                    self.assertEqual(flux, self.r45.rotate_flux(p["flux"], axis, sign))

    def test_rotations_preserve_all_prefix_dot_products(self):
        for p in self.one+self.two:
            for axis in range(3):
                rotated = [self.r45.rotate_flux(f, axis, -1) for f in p["prefixes"]]
                for i, a in enumerate(p["prefixes"]):
                    for j, b in enumerate(p["prefixes"]):
                        self.assertEqual(self.r42.dot(a, b), self.r42.dot(rotated[i], rotated[j]))

    def test_species_tensor_step_against_unreduced_hops(self):
        for paths in (self.one, self.two):
            g = self.grouped(paths)
            arity = g["arity"]
            explicit = append_M(self.r45, self.r42, self.r40, paths, self.r40.cubic_row)
            expected = [F(0)]*(1 << arity)
            for p in explicit:
                moment, _ = self.r45.moment_factors(p["dots"], [self.r42.length(f) for f in p["prefixes"]])
                species = sum(mode[1] << j for j, mode in enumerate(p["word"]))
                expected[species] += F(abs(p["weight"])*moment, 576**p["order"])
            self.assertEqual(r.species_multiply(g["seed_species_moments"], self.r40.W, arity), expected)

    def test_species_tensor_row_bounds(self):
        for arity in (3, 5):
            for i in range(1 << arity):
                v = [F(j == i) for j in range(1 << arity)]
                self.assertLessEqual(sum(r.species_multiply(v, self.r40.W, arity)), arity*self.r46.MU)

    def test_all_later_M_tail_convergence_and_time_order(self):
        for paths in (self.one, self.two):
            g = self.grouped(paths)
            arity = g["arity"]
            args = (self.r46, self.r40, self.r38, g["seed_species_moments"], arity, (arity-1)//2)
            coarse, fine = r.suffix_tail(*args, through=10), r.suffix_tail(*args, through=18)
            self.assertLessEqual(fine["upper"], coarse["upper"])
            self.assertGreater(fine["upper"], 0)
            for t in (F(0), F(1, 10), F(1, 2)):
                self.assertLessEqual(r.suffix_tail(*args, time=t)["upper"], fine["upper"]*t**7)

    def test_tail_against_independent_complete_edge_resummation(self):
        data = self.r43.geometry(self.parent, "edge")
        row = self.r40.parent_rows(data)
        for paths in (list(self.r45.one_e_paths(self.r42,self.r41,self.r40,row,0,range(2),False)),
                      list(self.r45.two_e_paths(self.r42,self.r41,self.r40,row,0,range(2),False))):
            arity = len(paths[0]["word"])
            exact = self.r46.compile_edge(self.r42,self.r41,self.r40,self.r38,data,paths)
            finite = scalar_source(self.r41,self.r39,self.r45,paths+append_M(self.r45,self.r42,self.r40,paths,row))
            den = lcm(exact["denominator"],finite["denominator"])
            coefficients = {}
            for key in exact["coefficients"].keys() | finite["coefficients"].keys():
                a,b=exact["coefficients"].get(key,(0,0)); c,d=finite["coefficients"].get(key,(0,0))
                coefficients[key]=(a*(den//exact["denominator"])-c*(den//finite["denominator"]),
                                   b*(den//exact["denominator"])-d*(den//finite["denominator"]))
            difference={"coefficients":coefficients,"denominator":den,"time":F(1),"numerical_error":F(0),"creates":self.r45.CREATES[arity]}
            zero={"coefficients":{},"denominator":1,"time":F(1),"numerical_error":F(0)}
            response=self.r45.response_matrix(self.r41,zero,[difference],(0,1))
            moments=[F(0)]*(1<<arity)
            for p in paths:
                moment,_=self.r45.moment_factors(p["dots"],[self.r42.length(f) for f in p["prefixes"]])
                moments[sum(m[1]<<j for j,m in enumerate(p["word"]))]+=F(abs(p["weight"])*moment,576**p["order"])
            tail=r.suffix_tail(self.r46,self.r40,self.r38,moments,arity,(arity-1)//2)["upper"]
            error=tail+exact["numerical_error"]+finite["numerical_error"]
            for i in range(4):
                ray=[(int(j==i),0) for j in range(4)]
                self.assertLessEqual(self.r41.ray_value(response,ray),error**2)

    def test_phase_compilation_against_scalar_simplexes(self):
        g=self.grouped(self.two)
        native=r.compile_groups(self.r41,self.r39,g,F(1),30)
        raw=append_M(self.r45,self.r42,self.r40,self.two,self.r40.cubic_row)
        source=scalar_source(self.r41,self.r39,self.r45,raw,30)
        expected=defaultdict(lambda:(F(0),F(0)))
        for (word,flux),(a,b) in source["coefficients"].items():
            action=r.relative_action(word,source["creates"])
            if action:
                key=action[0],flux
                expected[key]=self.r41.add(expected[key],(F(action[1]*a,source["denominator"]),F(action[1]*b,source["denominator"])))
        actual={r.decode_output(key):(F(a,native["denominator"]),F(b,native["denominator"])) for key,(a,b) in native["vector"].items()}
        self.assertEqual(actual,{key:value for key,value in expected.items() if value!=(0,0)})

    def test_negative_and_zero_phase_time(self):
        g=self.grouped(self.two)
        positive=r.compile_groups(self.r41,self.r39,g,F(1),20)
        negative=r.compile_groups(self.r41,self.r39,g,F(-1),20)
        self.assertEqual(negative["denominator"],positive["denominator"])
        self.assertEqual(negative["vector"],{k:(a,-b) for k,(a,b) in positive["vector"].items()})
        zero=r.compile_groups(self.r41,self.r39,g,F(0),20)
        self.assertEqual(zero["vector"],{})
        self.assertEqual(zero["numerical_error"],0)

    def test_phase_degree_error_control(self):
        g=self.grouped(self.two)
        low=r.compile_groups(self.r41,self.r39,g,F(1),20)
        high=r.compile_groups(self.r41,self.r39,g,F(1),40)
        distance=F(0)
        for key in low["vector"].keys() | high["vector"].keys():
            a,b=low["vector"].get(key,(0,0)); c,d=high["vector"].get(key,(0,0))
            distance+=abs(F(a,low["denominator"])-F(c,high["denominator"]))+abs(F(b,low["denominator"])-F(d,high["denominator"]))
        self.assertLessEqual(distance,low["numerical_error"]+high["numerical_error"])

    def test_native_rejects_invalid_protocol(self):
        result=subprocess.run([str(self.exe),str(Path(self.tmp.name)/'bad.bin'),'1'],input=b'bad',capture_output=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn(b'truncated',result.stderr)

    def test_guards_and_immutable_parent(self):
        with self.assertRaises(ValueError):
            r.suffix_tail(self.r46,self.r40,self.r38,[F(0)]*8,3,1,F(2))
        with patch.dict(r.PINS,{"checker.py":"0"*64}):
            with self.assertRaisesRegex(ValueError,"Round46 pin"):
                r.inherited(ROOT)

    def test_native_cancellation_and_deterministic_group_order(self):
        g=self.grouped(self.two)
        first=g['path'].read_bytes()
        again=self.grouped(self.two)
        self.assertEqual(first,again['path'].read_bytes())
        self.assertGreaterEqual(g['cost']['groups_before_cancellation'],g['cost']['groups'])

    def test_recorded_first_M_moment_matches_previous_full_cubic_CAR_census(self):
        x=json.loads((HERE/'validation.json').read_text())
        cl,ch=self.r38.sqrt_interval(F(107,2048))[1],self.r38.sqrt_interval(F(1,96))[1]
        for tail,expected in zip(x['suffix_tails'],(self.r45.EXPECTED_ONE,self.r45.EXPECTED_TWO)):
            self.assertEqual(F(tail['first_M_CAR_moment']),expected[0][0]*cl+expected[0][1]*ch)

    def test_recorded_old_column_matches_pinned_bulk_result(self):
        x=json.loads((HERE/'validation.json').read_text())
        old=json.loads((HERE.parent/'higher-electric-round45/validation.json').read_text())
        self.assertEqual(x['old45_column']['probability'],old['readouts'][-1]['examples']['bare']['approximate_probability'])

    def test_recorded_new_interval_is_narrower_with_every_error_included(self):
        x=json.loads((HERE/'validation.json').read_text()); new=x['readout']
        error=F(new['ideal_electric_error'])+F(new['M_suffix_evaluation_error'])+F(new['configuration_and_arithmetic_error'])
        self.assertEqual(F(new['total_amplitude_error']),error)
        old=json.loads((HERE.parent/'higher-electric-round45/validation.json').read_text())['readouts'][-1]['examples']['bare']
        self.assertLess(F(new['high_occupation_upper'])-F(new['high_occupation_lower']),F(old['high_occupation_upper'])-F(old['high_occupation_lower']))
        self.assertTrue(x['bare_cubic_readout_executed']); self.assertTrue(x['all_later_M_layers_bounded'])
        self.assertFalse(x['new_bulk_Bell_readout_executed']); self.assertFalse(x['full_electric_dynamics_solved'])
        self.assertEqual(x['retained_suffix_M_steps'],1)

    def test_recorded_seed_counts_are_not_initially_pruned(self):
        x=json.loads((HERE/'validation.json').read_text())
        self.assertEqual(x['native_groups'][0]['raw_seed_counts'],{'MEMM':2199312,'MMEM':1852848,'MMME':941664})
        self.assertEqual(x['native_groups'][1]['raw_seed_counts'],{'MEE':6936})

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT),json.loads((HERE/'validation.json').read_text()))


if __name__=='__main__':
    unittest.main()
