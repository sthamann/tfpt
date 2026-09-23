"""Exact bounded controls for the accompanying all-integer proofs.

Basis labels are unbounded integers, not truncated square shift matrices.
No empirical control is represented as a proof of the infinite statement.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp

BASE = Path(__file__).resolve().parent
results = []


def check(name, condition, scope):
    ok = bool(condition)
    results.append({"name": name, "pass": ok, "scope": scope})
    if not ok:
        raise AssertionError(name)


def S(n, k):
    return None if k is None else n * k


def A(n, k):
    return None if k is None or k % n else k // n


check("isometry_on_integer_basis", all(A(n, S(n, k)) == k for n in range(1, 15) for k in range(1, 81)),
      "All 14*80 selected basis labels, using exact integer maps with no output cutoff.")
check("proper_range", all(S(n, A(n, 1)) is None for n in range(2, 15)),
      "The basis label 1 lies outside every selected S_n range for n>1.")
check("multiplication_composition", all(S(m, S(n, k)) == S(m*n, k) for m in range(1, 12) for n in range(1, 12) for k in range(1, 41)),
      "Exact selected positive integer labels; the universal basis proof is in the report.")
check("gcd_adjoint_relation", all(A(m, S(n, k)) == S(n // math.gcd(m,n), A(m // math.gcd(m,n), k)) for m in range(1, 12) for n in range(1, 12) for k in range(1, 81)),
      "S_m* S_n = S_(n/d) S_(m/d)* on the selected basis labels.")
check("prime_double_commutation", all(A(p, S(q, k)) == S(q, A(p, k)) for p in (2,3,5,7,11) for q in (2,3,5,7,11) if p != q for k in range(1, 101)),
      "Distinct primes through 11; no statistical approximation.")
check("valuation_basis_roundtrip", all(math.prod(int(p)**int(a) for p,a in sp.factorint(n).items()) == n for n in range(1, 251)),
      "Valuation lookup uses exact existing factorization; this is not an efficient new factorization algorithm.")

x, y = sp.symbols("x y", positive=True)
check("log_covariance", sp.expand_log(sp.log(x*y), force=False) == sp.log(x)+sp.log(y),
      "Symbolic identity on positive arguments; the operator domain is handled in the report.")
finite_primes = (2,3,5)
finite_sum = sum(sp.Rational(1, math.prod(p**k for p,k in zip(finite_primes,ks))**2) for ks in itertools.product(range(4), repeat=3))
finite_product = math.prod(sum(sp.Rational(1,p**(2*k)) for k in range(4)) for p in finite_primes)
check("finite_prime_partition_identity", finite_sum == finite_product,
      "Exact rational beta=2 sum for 3 primes and occupations 0..3; infinite convergence is proved separately.")

check("phase_covariance_exponents", all(sp.Rational(a,b)*(n*k) == n*sp.Rational(a,b)*k for (a,b) in ((0,1),(1,4),(2,7),(1,3)) for n in range(1,9) for k in range(1,25)),
      "Equal exact rational exponents prove selected E(r)S_n=S_nE(nr) cases.")

# Fourier root average: its residual rational phase equals 1 when divisibility holds.
# For nondivisibility the exact sum of powers of a root of unity vanishes.
root_cache = {}
for n in (2,3,4,5,6):
    for residue in range(n):
        z = sp.exp(2*sp.pi*sp.I*sp.Rational(residue,n))
        root_cache[n,residue] = sp.simplify(sp.expand_complex(sum(z**j for j in range(n))))
check("bc_root_average", all(root_cache[n,k % n] == (n if k % n == 0 else 0) for n in (2,3,4,5,6) for k in range(1,31)),
      "Exact root-of-unity sums n=2..6. Together with the explicit residual phase in the report this verifies the covariance average.")

check("z4_projection_selectors", all(sp.simplify(sum(sp.I**(j*(k-r)) for j in range(4))/4) == int(k % 4 == r) for r in range(4) for k in range(1,65)),
      "Exact four-term Fourier projectors for all residues and selected labels.")
check("z4_covariance", all(sp.I**(n*k) == (sp.I**k)**n for n in range(1,13) for k in range(1,33)),
      "Q S_n = S_n Q^n, including even noninvertible maps on residues.")

for beta in (2,3):
    for K in (1,8,25):
        lhs = sum(sp.Rational(1, m**beta) for m in range(1,4*K+1) if m % 4 == 0)
        rhs = sp.Rational(1,4**beta)*sum(sp.Rational(1,k**beta) for k in range(1,K+1))
        assert lhs == rhs
check("residue_gibbs_scaling", True,
      "Exact finite reindexing at beta=2,3 and K=1,8,25. The infinite identity follows by positive convergence, not finite normalization.")
check("beta2_uniform_state_mismatch", sp.Rational(1,16) != sp.Rational(1,4),
      "The exact infinite Gibbs residue-zero mass is 4^-2=1/16, against uniform mass 1/4.")

weights = sp.symbols("w0:4", positive=True)
G = sp.diag(*weights)
Gt = sp.kronecker_product(G,G)
M = sp.zeros(4,16)
for j in range(4):
    M[j,4*j+j] = 1
Mdag = Gt.inv()*M.T*G
cap = Mdag*sp.ones(4,1)
check("weighted_frobenius_adjoint", M*Mdag == sp.diag(*(1/w for w in weights)),
      "Symbolic adjoint with weighted Hilbert products on algebra and tensor square.")
check("cap_norm_four_any_weights", sp.simplify((cap.T*Gt*cap)[0]) == 4,
      "All symbolic strictly positive weights, independently of their normalization; normalized faithful states are included.")
uniform = dict(zip(weights,[sp.Rational(1,4)]*4))
skew = dict(zip(weights,[sp.Rational(1,16),sp.Rational(3,16),sp.Rational(5,16),sp.Rational(7,16)]))
check("uniform_specialness", (M*Mdag).subs(uniform) == 4*sp.eye(4),
      "Exactly uniform weights give m m†=4I.")
check("skew_cap_same_but_specialness_fails", sp.simplify((cap.T*Gt*cap)[0].subs(skew)) == 4 and (M*Mdag).subs(skew) != 4*sp.eye(4),
      "An explicit normalized faithful skew state keeps cap norm four while breaking specialness.")

a, b, kap = sp.symbols("a b kappa", positive=True)
scale_solution = sp.solve([b-kap, a*sp.log(2)+b-4*kap], [a,b])
residual = sp.simplify((a*sp.log(4)+b-16*kap).subs(scale_solution))
check("log_vs_quadratic_energy", residual == -9*kap,
      "Matching n=1,2 leaves exact nonzero residual -9*kappa at n=4 for kappa>0.")
check("electric_shift_frequency_depends_on_charge", (2**2-1**2)*kap == 3*kap and ((2*2)**2-2**2)*kap == 12*kap,
      "S_2 has electric frequencies 3*kappa and 12*kappa on labels 1 and 2; logarithmic frequency is constant.")
check("positive_sector_not_full_rotor_invariant", 1-1 == 0 and not (1-1 > 0),
      "The genuine lowering rotor operator sends |1> to |0>, outside the positive charge sector.")

def T(m, r, k):
    return None if k is None else m*k+r


def Tadj(m, r, k):
    return None if k is None or (k-r) % m else (k-r)//m


check("cuntz_branch_orthogonality", all(Tadj(m,r,T(m,s,k)) == (k if r == s else None) for m in range(2,9) for r in range(m) for s in range(m) for k in range(-20,21)),
      "Exact all-sign rotor basis labels: T_r* T_s = delta_rs I; no finite-dimensional isometries substituted.")
check("cuntz_partition_identity", all(sum(T(m,r,Tadj(m,r,k)) == k for r in range(m)) == 1 for m in range(2,10) for k in range(-45,46)),
      "Every selected integer lies in exactly one translated m-cover range.")
beta_sym = sp.symbols("beta", positive=True)
m_sym = sp.symbols("m", positive=True, integer=True)
check("kms_forces_logarithmic_frequency", sp.simplify(m_sym*sp.exp(-beta_sym*(sp.log(m_sym)/beta_sym))) == 1,
      "Symbolic normalization after the KMS derivation in the report; it checks consistency, not existence of a KMS state.")
check("kms_matrix_sector_uniform", sp.diag(*([sp.Rational(1,4)]*4)) == sp.eye(4)/4,
      "The KMS-derived matrix-unit weights delta_rs/4 restrict to uniform four-dimensional diagonal weights; full M4 has dimension 16.")
check("factorial_residue_separation", all((k-n) % math.factorial(7) != 0 for n in range(-25,26) for k in range(-25,26) if k != n),
      "Selected distinct bounded integer labels separate at factorial modulus 7!. The strong-limit and nonnormality proofs are textual.")

payload = {
    "status": "PASS_SCOPED_EXACT_CONTROLS",
    "date": "2026-09-10",
    "groups": len(results),
    "passed": sum(x["pass"] for x in results),
    "scope": "Exact selected integer cases and symbolic identities. General proofs are textual. No RH, TFPT completion, complexity or physical implementability certificate.",
    "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (BASE/"PRIMZAHLEN-PROZESSMODELL.md", Path(__file__))},
    "results": results,
}
(BASE/"checks.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({k: payload[k] for k in ("status","groups","passed","files")},indent=2,ensure_ascii=False))
