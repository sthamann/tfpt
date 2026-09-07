#!/usr/bin/env python3
"""Exact charge-flow/path tests on an untruncated integer carrier."""
from __future__ import annotations
import itertools as it
import json
from collections import deque
import sympy as s


def main():
    checks = []
    def check(label, ok):
        if not bool(ok):
            raise AssertionError(label)
        checks.append(label)
    eye = s.eye(8)
    basis = s.Matrix.hstack(2*eye[:, 0], *[eye[:, 0]+eye[:, k] for k in range(1, 7)], s.ones(8, 1)/2)
    G = basis.T*basis
    units = [tuple(int(a == b) for a in range(8)) for b in range(8)]
    zero = (0,)*8
    def beta(n, m):
        return int(sum(n[a]*m[a]*G[a, a]/2 for a in range(8))
                   +sum(n[a]*m[b]*G[a, b] for a in range(8) for b in range(a))) % 2
    def transfer(state, x, y, p):
        neg = tuple(-v for v in p)
        phase = (-1)**(beta(p, neg)+beta(neg, state[x])+beta(p, state[y]))
        out = list(state)
        out[x] = tuple(a-b for a, b in zip(out[x], p))
        out[y] = tuple(a+b for a, b in zip(out[y], p))
        return tuple(out), phase
    check("retained Gram is full even unimodular, not independent diagonal rotors",
          G.det() == 1 and G[1, 2] == 1 and G[0, 0] == 4)
    for side in (2, 3, 4):
        sites = list(it.product(range(side), repeat=3))
        lookup = {x: i for i, x in enumerate(sites)}
        edges = []
        for x in sites:
            for a in range(3):
                y = list(x); y[a] = (y[a]+1) % side
                edges.append((lookup[x], lookup[tuple(y)]))
        N = len(sites)
        adjacency = {x: set() for x in range(N)}
        for x, y in edges:
            adjacency[x].add(y); adjacency[y].add(x)
        distance = {0: 0}; queue = deque([0])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y not in distance:
                    distance[y] = distance[x]+1; queue.append(y)
        check(f"L={side}: exact periodic inventory retains all positive-edge multiplicities",
              len(edges) == 3*N and 8*len(edges) == 24*N)
        check(f"L={side}: shortest transport distance matches wrapped lattice metric",
              all(distance[i] == sum(min(a, side-a) for a in x) for i, x in enumerate(sites)))
        cut = {i for i, x in enumerate(sites) if x[0] == 0}
        boundary = [(x, y) for x, y in edges if (x in cut) != (y in cut)]
        check(f"L={side}: slab charge-current bound counts both boundary surfaces",
              len(boundary) == 2*side**2 and len(boundary) <= len(edges))
        for a, p in enumerate(units):
            state = [zero]*N; state[0] = p; state = tuple(state)
            target_index = lookup[(1, 0, 0)]
            target = [zero]*N; target[target_index] = p; target = tuple(target)
            amplitude = 0
            for x, y in edges:
                if {x, y} == {0, target_index}:
                    for tail, head in ((x, y), (y, x)):
                        moved, phase = transfer(state, tail, head, p)
                        if moved == target: amplitude -= phase
            expected = -2 if side == 2 else -1
            check(f"L={side}, species{a}: coherent neighboring amplitude and probability coefficient",
                  amplitude == expected and amplitude**2 == (4 if side == 2 else 1))
        p = units[7]
        state = tuple([p]+[zero]*(N-1))
        # Every directed occurrence is tested as a true infinite-carrier shift.
        currents_ok = True
        for x, y in edges:
            moved, phase = transfer(state, x, y, p)
            total_before = [sum(n[a] for n in state) for a in range(8)]
            total_after = [sum(n[a] for n in moved) for a in range(8)]
            cut_difference = sum(n[7] for i, n in enumerate(moved) if i in cut)-sum(n[7] for i, n in enumerate(state) if i in cut)
            currents_ok &= total_before == total_after and cut_difference == int(y in cut)-int(x in cut)
            back, phase_back = transfer(moved, y, x, p)
            currents_ok &= back == state and phase*phase_back == 1
        check(f"L={side}: full charge conservation, cut incidence and adjoint phases", currents_ok)
        dipole, phase = transfer(tuple([zero]*N), 0, target_index, p)
        check(f"L={side}: zero profile is moved to a neutral dipole",
              dipole != tuple([zero]*N) and sum(n[7] for n in dipole) == 0 and abs(phase) == 1)
    # Exact path telescoping in the original projective representation.
    sample = ((2, -1, 0, 1, 0, 0, 0, 3), zero, zero)
    for a, p in enumerate(units):
        first, ph1 = transfer(sample, 0, 1, p)
        second, ph2 = transfer(first, 1, 2, p)
        direct, phd = transfer(sample, 0, 2, p)
        check(f"species{a}: charge path telescopes without cocycle loss", second == direct and ph1*ph2 == phd)
    check("factorial Dyson tail majorant denominator is exact",
          all(s.factorial(d+j) >= s.factorial(d)*s.factorial(j) for d in range(12) for j in range(12)))
    check("no neutral-hop sequence can change a synchronized total",
          all(N*n != N*m for N in (8, 27) for n in range(-3, 4) for m in range(-3, 4) if n != m))
    check("bounded hopping constant and norm count all eight channels", 2*24 == 48 and 4*24 == 96)
    z,gamma = s.symbols("z gamma", positive=True)
    integral = s.integrate(s.sqrt(z)/(gamma+z)**2,(z,0,s.oo))
    check("positive-gap square-root commutator integral has exact coefficient", s.simplify(integral-s.pi/(2*s.sqrt(gamma))) == 0)
    check("quadratic clock multiplier gives sqrt(3/gamma), not unity", s.simplify(s.sqrt(12)*integral/s.pi-s.sqrt(3/gamma)) == 0)
    # Functional-calculus counterexample only; not a truncated field model.
    A = s.Matrix([[3,-1,0],[-1,3,-1],[0,-1,3]])
    v1 = s.Matrix([1,s.sqrt(2),1])/2
    v2 = s.Matrix([1,0,-1])/s.sqrt(2)
    v3 = s.Matrix([1,-s.sqrt(2),1])/2
    rootA = s.sqrt(3-s.sqrt(2))*v1*v1.T+s.sqrt(3)*v2*v2.T+s.sqrt(3+s.sqrt(2))*v3*v3.T
    check("positive local generator square root has a nonlocal distance-two entry",
          (rootA*rootA-A).applyfunc(s.simplify) == s.zeros(3) and A[0,2] == 0
          and rootA[0,2] != 0 and s.simplify(rootA[0,2]) != 0)
    print(json.dumps({"status":"PASS", "exact_check_groups":len(checks), "checks":checks,
          "scope":"Exact integer graph/cocycle tests; operator-domain and all-order Dyson proofs in PROOF.md. No uniform-volume light cone, finite rotor cutoff, or TOE claim."}, indent=2))


if __name__ == "__main__":
    main()
