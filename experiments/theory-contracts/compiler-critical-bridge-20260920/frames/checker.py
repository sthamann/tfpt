#!/usr/bin/env python3
"""Exact fixed-frame collision and Coxeter-covariant complex-frame family."""
from __future__ import annotations

import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SOURCES = {
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json":
        "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
}
CHECKS = []


def require(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def roots():
    out = []
    for a, b in it.combinations(range(8), 2):
        for u, v in it.product((-1, 1), repeat=2):
            r = [0] * 8
            r[a], r[b] = u, v
            out.append(sp.Matrix(r))
    for signs in it.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            out.append(sp.Matrix([sp.Rational(v, 2) for v in signs]))
    return out


def matrix_key(matrix):
    return tuple(matrix)


def plane(alpha, frame):
    partner = frame * alpha
    return (alpha * alpha.T + partner * partner.T) / (alpha.T * alpha)[0]


def main():
    for path, expected in SOURCES.items():
        require(hashlib.sha256((REPO / path).read_bytes()).hexdigest() == expected,
                "source pin: " + path)
    cert = json.loads((REPO / next(iter(SOURCES))).read_text())
    C, J = [sp.Matrix([[sp.Rational(v) for v in row]
                       for row in cert["clock_matrices"][name]["vector"]])
            for name in ("C", "J")]
    I = sp.eye(8)
    require(J**2 == -I and J.T == -J, "marked J is orthogonal complex structure")
    require(C.T*C == I and C**15 == -I and C**30 == I,
            "original C is orthogonal with C^15=-I and C^30=I")
    standard = roots()
    standard_set = {matrix_key(v) for v in standard}
    require(len(standard_set) == 240, "240 distinct standard roots")
    require({matrix_key(C*v) for v in standard} == standard_set,
            "original C permutes standard E8 roots")
    require({matrix_key(J*v) for v in standard} == standard_set,
            "original J permutes standard E8 roots")

    # A stronger finite-field obstruction: no endomorphism of the E8 root
    # lattice can simultaneously commute with C and square to -I. In an
    # integral root basis C mod31 has eight distinct F31 eigenlines. Its
    # commutant preserves each line, whereas -1 has no square root in F31.
    half = sp.Rational(1,2)
    basis_roots = [
        [half,-half,-half,-half,-half,-half,-half,half],
        [1,1,0,0,0,0,0,0], [-1,1,0,0,0,0,0,0],
        [0,-1,1,0,0,0,0,0], [0,0,-1,1,0,0,0,0],
        [0,0,0,-1,1,0,0,0], [0,0,0,0,-1,1,0,0],
        [0,0,0,0,0,-1,1,0],
    ]
    B = sp.Matrix.hstack(*(sp.Matrix(v) for v in basis_roots))
    require(all(tuple(v) in standard_set for v in basis_roots)
            and abs(B.det()) == 1, "integral E8 basis consists of roots with determinant one")
    Binv = B.inv()
    require(all(v.q == 1 for root in standard for v in Binv*root),
            "every root is integral in selected lattice basis")
    CB = Binv*C*B
    require(all(v.q == 1 for v in CB), "actual Coxeter matrix is integral on root lattice")
    x = sp.symbols("x")
    phi = CB.charpoly(x).as_expr()
    require(phi == sp.cyclotomic_poly(30,x), "actual lattice C characteristic polynomial is Phi30")
    roots31 = [a for a in range(31) if int(phi.subs(x,a)) % 31 == 0]
    require(sp.isprime(31) and len(roots31) == 8,
            "C mod31 has eight distinct eigenvalues in F31")
    require(not any((a*a+1) % 31 == 0 for a in range(31)),
            "minus one has no square root in F31")
    require((-1)**15 == -1 and C**15 == -I,
            "odd scalar half-period also forbids C Jprime=-Jprime C for any nonzero Jprime")

    # Read the actual source constructor; all returned entries are integers,
    # and exact conversion is guarded before rational calculations begin.
    source_path = REPO / list(SOURCES)[1]
    spec = importlib.util.spec_from_file_location("native_source", source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    gaussian = set()
    for ray in source.source_rays():
        for phase in (1, 1j, -1, -1j):
            values = [v for z in phase*ray for v in (z.real, z.imag)]
            require(all(v == int(v) for v in values), "native Gaussian integer conversion")
            gaussian.add(tuple(int(v) for v in values))
    A = I+J
    require(A.T*A == 2*I and A*J == J*A,
            "coordinate bridge A=I+J has scale sqrt(2) and preserves complex frame")
    require({matrix_key(A*v) for v in standard} == gaussian,
            "A maps standard E8 exactly onto actual native Gaussian source")
    CG = A*C*A.inv()
    native = [sp.Matrix(v) for v in sorted(gaussian)]
    require(CG.T*CG == I and CG**15 == -I, "transported C has original metric and half-period")
    require({matrix_key(CG*v) for v in native} == gaussian,
            "transported C permutes all native source labels")

    frames = [CG**k * J * CG.T**k for k in range(15)]
    require(len({matrix_key(f) for f in frames}) == 15, "exactly fifteen distinct C-transported frames")
    return_plus = [k for k in range(1, 31) if CG**k * J == J*CG**k]
    return_minus = [k for k in range(1, 31) if CG**k * J == -J*CG**k]
    require(return_plus == [15, 30] and return_minus == [],
            "no earlier complex or anti-complex return of the marked frame")

    alpha = sp.Matrix([0, 2, 0, 0, 0, 0, 0, 0])
    beta = J*alpha
    ca, cb = CG*alpha, CG*beta
    require(matrix_key(alpha) in gaussian and matrix_key(beta) in gaussian,
            "collision inputs are actual Gaussian source labels")
    require(plane(alpha,J) == plane(beta,J), "collision inputs represent one fixed-J complex ray")
    diff = plane(ca,J)-plane(cb,J)
    require(sp.trace(diff.T*diff) == 3, "C images have distinct fixed-J ray projectors, squared real Frobenius distance three")
    def overlap_sq(a,b,frame):
        return sp.factor(((a.T*b)[0]**2+(a.T*frame*b)[0]**2)/
                         ((a.T*a)[0]*(b.T*b)[0]))
    require(overlap_sq(alpha,beta,J) == 1 and overlap_sq(ca,cb,J) == sp.Rational(1,4),
            "same-ray overlap one is changed to one-quarter by fixed-frame C relabelling")

    census = []
    alphabet_keys = []
    for k, frame in enumerate(frames):
        nxt = frames[(k+1)%15]
        require(frame**2 == -I and frame.T == -frame, f"frame {k} is orthogonal complex")
        require(CG*frame == nxt*CG, f"C is complex-linear between frames {k} and {(k+1)%15}")
        require({matrix_key(frame*v) for v in native} == gaussian,
                f"frame {k} preserves native roots")
        alphabet = {}
        for v in native:
            P = plane(v,frame)
            require(P.T == P and P*P == P and sp.trace(P) == 2,
                    f"frame {k} native complex ray is rank-two real orthoprojector")
            require(CG*P*CG.T == plane(CG*v,nxt), f"frame {k} exact native ray covariance")
            alphabet[matrix_key(P)] = I-2*P
        require(len(alphabet) == 60, f"frame {k} has sixty distinct ray events")
        # Each complex reflection is a product of two orthogonal real-root
        # reflections in v and frame*v. Both are E8 roots, so it preserves
        # the root set. The first frame is also checked by direct census;
        # all subsequent frames are its exact conjugates by C^k.
        if k == 0:
            for r in alphabet.values():
                require({matrix_key(r*v) for v in native} == gaussian,
                        "native complex reflection permutes the complete root source")
        transported_first = {matrix_key(CG**k*r*CG.T**k) for r in first_alphabet.values()} if k else set()
        if k:
            require(transported_first == {matrix_key(r) for r in alphabet.values()},
                    f"frame {k} full sixty-event alphabet is transported original alphabet")
        else:
            first_alphabet = alphabet
        census.append(len(alphabet))
        alphabet_keys.append(frozenset(alphabet))
    require(len(set(alphabet_keys)) == 15, "fifteen transported ray alphabets are distinct")

    return {
        "status": "PASS", "verdict": "FIXED_RAY_CLOCK_MAP_REFUTED_COVARIANT_FRAME_FAMILY_EXACT",
        "exact_checks": len(CHECKS), "failed_checks": 0, "source_sha256": SOURCES,
        "standard_to_native_coordinate_bridge": "A=I+J; A^T A=2I",
        "C_gaussian": [[str(x) for x in row] for row in CG.tolist()],
        "C_orbit_frame_count": 15, "complex_return_powers_1_to_30": return_plus,
        "anti_complex_return_powers_1_to_30": return_minus,
        "lattice_fixed_complex_frame_obstruction": {
            "C_lattice": [[str(v) for v in row] for row in CB.tolist()],
            "prime": 31, "distinct_C_eigenvalues_mod_prime": roots31,
            "square_roots_of_minus_one_mod_prime": [],
            "theorem": "No lattice endomorphism Jprime with Jprime^2=-I commutes with C; anticommutation is impossible even over R by C^15=-I",
        },
        "ray_counts_by_frame": census,
        "collision": {"alpha": list(map(str,alpha)), "Jalpha": list(map(str,beta)),
            "C_alpha": list(map(str,ca)), "C_Jalpha": list(map(str,cb)),
            "input_overlap_squared": "1", "output_overlap_squared": "1/4",
            "output_real_projector_distance_squared": "3"},
        "positive_covariance": "C Pi_alpha^J C^-1=Pi_(C alpha)^(C J C^-1)",
        "cycle_monodromy": "C^15=-I on vector fibers; C^30=I",
        "not_claimed": ["full C/J/c frame-orbit classification", "physical frame degree of freedom",
            "gauge versus physical status of J selected", "frame hopping or Hamiltonian selected",
            "C is a commuting symmetry of the previously chosen fixed-frame Hamiltonian",
            "no-go for other embeddings, full E8 or a continuum limit", "TOE completion"],
        "checks": CHECKS,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
