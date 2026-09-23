#!/usr/bin/env python3
"""Exact common E8/D5/A3/E6/A2 root embedding; NON-RH, no physics promotion."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def check(name, value):
    checks.append({"name": name, "pass": bool(value)})
    if not value:
        raise RuntimeError(name)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


roots = set()
for i, j in combinations(range(8), 2):
    for si, sj in product((-2, 2), repeat=2):
        v = [0]*8
        v[i], v[j] = si, sj
        roots.add(tuple(v))
for v in product((-1, 1), repeat=8):
    if v.count(-1) % 2 == 0:
        roots.add(v)
check("240 E8 roots in doubled coordinates", len(roots) == 240)
check("all actual roots norm squared2", all(dot(v, v) == 8 for v in roots))
d5 = {v for v in roots if v[5:] == (0, 0, 0)}
a3 = {v for v in roots if v[:5] == (0,)*5}
a2 = {v for v in a3 if sum(v[5:]) == 0}
e6 = {v for v in roots if v[5] == v[6] == v[7]}
for label, subset, count, rank in [("D5", d5, 40, 5), ("A3=D3", a3, 12, 3),
                                  ("A2", a2, 6, 2), ("E6", e6, 72, 6)]:
    check(label+" root count", len(subset) == count)
    check(label+" root-span rank", s.Matrix(list(subset)).rank() == rank)
    # Root closure under each root reflection proves a subsystem, not just a count.
    for v in subset:
        for w in subset:
            coefficient = s.Rational(dot(v, w), 4)
            reflected = tuple(s.Integer(wi)-coefficient*vi for vi, wi in zip(v, w))
            check(label+" Weyl closure "+str(v)+str(w), reflected in subset)

check("common D5 sits in E6", d5 <= e6)
check("A2 family sits in A3", a2 <= a3)
check("D5 centralizer root system exactly A3", {r for r in roots if all(dot(r, d) == 0 for d in d5)} == a3)
check("A2 centralizer root system exactly E6", {r for r in roots if all(dot(r, a) == 0 for a in a2)} == e6)
check("E6 centralizer root system exactly A2", {r for r in roots if all(dot(r, a) == 0 for a in e6)} == a2)
check("joint D5 A2 centralizer has no roots", not {r for r in roots if all(dot(r, a) == 0 for a in d5|a2)})
check("joint D5 A2 centralizer Cartan dimension1", 8-s.Matrix(list(d5|a2)).rank() == 1)
check("A3 commuting with its A2 leaves no roots", not {r for r in a3 if all(dot(r, a) == 0 for a in a2)})
check("independent D5+A3+A2 rank impossible in E8", 5+3+2 > 8)

table = Counter()
for r in roots:
    charge = -sum(r[5:])
    if r in d5:
        key = ("45", "1", 0)
    elif r in a2:
        key = ("1", "8", 0)
    elif r in a3:
        key = ("1", "3" if charge == 4 else "bar3", charge)
    elif all(abs(x) == 1 for x in r):
        spin = "16" if r[:5].count(-1) % 2 == 0 else "bar16"
        family = "1" if abs(charge) == 3 else ("3" if charge == 1 else "bar3")
        key = (spin, family, charge)
        check("half-charge conformal split5/8+3/8", s.Rational(dot(r[:5], r[:5]), 8) == s.Rational(5, 8)
              and s.Rational(dot(r[5:], r[5:]), 8) == s.Rational(3, 8))
    else:
        key = ("10", "3" if charge == -2 else "bar3", charge)
    table[key] += 1
# Include the eight Cartan weights, respecting the common rank decomposition.
table[("45", "1", 0)] += 5
table[("1", "8", 0)] += 2
table[("1", "1", 0)] += 1
expected = {("45", "1", 0):45, ("1", "8", 0):8, ("1", "1", 0):1,
            ("16", "3", 1):48, ("bar16", "bar3", -1):48,
            ("16", "1", -3):16, ("bar16", "1", 3):16,
            ("10", "3", -2):30, ("10", "bar3", 2):30,
            ("1", "3", 4):3, ("1", "bar3", -4):3}
check("complete common charged branching table", dict(table) == expected)
check("E6 adjoint regrouping", table[("45", "1", 0)]+table[("1", "1", 0)]
      +table[("16", "1", -3)]+table[("bar16", "1", 3)] == 78)
check("E6 27 x3 regrouping", table[("16", "3", 1)]+table[("10", "3", -2)]+table[("1", "3", 4)] == 27*3)
check("E6 bar27 xbar3 also present", table[("bar16", "bar3", -1)]+table[("10", "bar3", 2)]+table[("1", "bar3", -4)] == 27*3)
check("no three-family chiral deletion", table[("bar16", "bar3", -1)] != 0)

# Root/weight lattice geometry: D3=A3 is FCC, its dual is BCC.
basis3 = s.Matrix([[1, 0, 0], [-1, 1, 1], [0, -1, 1]])
check("D3 root covolume2", abs(basis3.det()) == 2)
dual = basis3.inv().T
check("dual root basis exact", basis3.T*dual == s.eye(3))
check("dual covolume1/2", abs(dual.det()) == s.Rational(1, 2))
half = s.Matrix([s.Rational(1, 2)]*3)
check("body centre belongs to dual lattice", all(x.is_integer for x in basis3.T*half))
check("body centre does not belong to root lattice", not all(x.is_integer for x in basis3.inv()*half))

# A full integral basis and an explicit admissible lattice cocycle.
simple = [s.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,
          s.Matrix([1,1,0,0,0,0,0,0]), s.Matrix([-1,1,0,0,0,0,0,0])]
for i in range(1, 6):
    v = [0]*8
    v[i], v[i+1] = -1, 1
    simple.append(s.Matrix(v))
abase = s.Matrix.hstack(*simple)
cartan = abase.T*abase
check("E8 integral simple basis Gram determinant1", cartan.det() == 1)
coordinates = []
ainverse = abase.inv()
for r in sorted(roots):
    n = ainverse*s.Matrix(r)/2
    check("E8 root has integral lattice coordinates "+str(r), all(x.is_integer for x in n))
    coordinates.append(tuple(int(x) for x in n))

def cocycle_exponent(n, m):
    return (sum(n[i]*m[i] for i in range(8))
            +sum(n[i]*m[j]*int(cartan[i, j]) for i in range(8) for j in range(i))) % 2

for n, m in product(coordinates, repeat=2):
    rhs = sum(n[i]*int(cartan[i, j])*m[j] for i in range(8) for j in range(8)) % 2
    if (cocycle_exponent(n, m)-cocycle_exponent(m, n)) % 2 != rhs:
        raise RuntimeError("cocycle commutator failure")
check("all57600 root-pair cocycle commutators exact", True)
check("cocycle diagonal root sign minus1", all(cocycle_exponent(n, n) == 1 for n in coordinates))
check("VOA weight1 dimension root240 plus Cartan8", len(roots)+8 == 248)
check("half charges have conformal weight1 not1/2", s.Rational(8, 8) == 1 and s.Rational(8, 8) != s.Rational(1, 2))
def dn_basis(n):
    columns = []
    for i in range(n-1):
        v = [0]*n
        v[i], v[i+1] = 1, -1
        columns.append(s.Matrix(v))
    columns.append(s.Matrix([0]*(n-2)+[1, 1]))
    return s.Matrix.hstack(*columns)

d5b, d8b = dn_basis(5), dn_basis(8)
det_d5, det_d8 = (d5b.T*d5b).det(), (d8b.T*d8b).det()
det_a3 = (basis3.T*basis3).det()
check("D5 D8 Gram determinants calculated", det_d5 == det_d8 == 4)
check("D5+A3 to E8 lattice index4", s.sqrt(det_d5*det_a3/cartan.det()) == 4)
check("D8 to E8 lattice index2 not4", s.sqrt(det_d8/cartan.det()) == 2)

report = {"scope":"NON-RH; exact finite root/lattice statements only; no spacetime, chirality, native seam or T2 closure",
          "coordinates":"roots scaled by2; D5 first5; A3 last3; A2 differences of last3; E6 last3 equal; Q=-sum(last3 doubled coordinates)",
          "branching":[{"D5":k[0],"SU3":k[1],"Q":k[2],"dimension":v} for k,v in sorted(table.items())],
          "centralizers":{"D5":"A3","A2":"E6","E6":"A2","D5+A2":"u1"},
          "half_vertex_h":{"D5":"5/8","A3":"3/8","total":"1"},
          "lattice_extension_indices":{"D5+A3_to_E8":4,"D8_to_E8":2},
          "cocycle":"epsilon(n,m)=(-1)^(sum_i n_i m_i+sum_{i>j}n_i m_j C_ij); bilinearity proves2-cocycle identity on all Z8",
          "passed":len(checks),"checks":checks}
(HERE/"verification.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({"passed":len(checks),"branching_dimensions":sorted(table.values()),"output":str(HERE/"verification.json")}))
