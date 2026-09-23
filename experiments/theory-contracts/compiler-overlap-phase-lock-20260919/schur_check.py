"""Bounded exact audit of the first-order block and Schur-bound arithmetic."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def gaussian_vector(array) -> sp.Matrix:
    """Convert the pinned Gaussian-integer numpy vector without approximation."""
    result = []
    for value in array:
        real = int(round(float(value.real)))
        imag = int(round(float(value.imag)))
        if value != complex(real, imag):
            raise RuntimeError("non-Gaussian-integer source coordinate")
        result.append(sp.Integer(real)+sp.I*sp.Integer(imag))
    return sp.Matrix(result)


def gaussian_key(vector: sp.Matrix) -> tuple[tuple[int, int], ...]:
    keys = []
    for phase in (1, sp.I, -1, -sp.I):
        candidate = []
        for value in phase*vector:
            real, imag = sp.expand_complex(value).as_real_imag()
            if not (real.is_Integer and imag.is_Integer):
                raise RuntimeError("reflection image is not a Gaussian root")
            candidate.append((int(real), int(imag)))
        keys.append(tuple(candidate))
    return min(keys)


def main() -> None:
    checks: list[str] = []
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned native source", checks)
    spec = importlib.util.spec_from_file_location("schur_native_source", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)

    raw_rays = source.source_rays()
    rays = [gaussian_vector(z) for z in raw_rays]
    require(len(rays) == 60, "sixty native Gaussian rays", checks)
    alpha = rays[0]
    reflections = [sp.eye(4)-z*z.conjugate().T/2 for z in rays]
    ray_index = {gaussian_key(z): index for index, z in enumerate(rays)}
    action = [[ray_index[gaussian_key(r*z)] for z in rays]
              for r in reflections]
    orbit = {0}
    while True:
        enlarged = orbit | {action[m][a] for m in range(60) for a in orbit}
        if enlarged == orbit:
            break
        orbit = enlarged
    require(len(orbit) == 60,
            "native reflection group is transitive on the sixty rays", checks)
    fixed = [r for r in reflections if r*alpha == alpha]
    require(len(fixed) == 15, "fifteen events fix the pinned oriented root", checks)

    eye4 = sp.eye(4)
    eye64 = sp.eye(64)
    # M=60K is built directly over the exact Gaussian rationals.  This avoids
    # forming K in binary floating point and rationalizing it afterwards.
    m = 120*eye64
    for r in fixed:
        m -= (sp.kronecker_product(r, r, eye4) +
              sp.kronecker_product(eye4, r, r))
    dyadic_entries = []
    for value in m:
        real, imag = sp.expand_complex(value).as_real_imag()
        dyadic_entries.append(real.is_Rational and imag.is_Rational and
                              real.q in (1, 2, 4, 8, 16) and
                              imag.q in (1, 2, 4, 8, 16))
    require(all(dyadic_entries),
            "60K has only exact dyadic rational entries", checks)

    r_alpha = reflections[0]
    h_ab = eye64-sp.kronecker_product(r_alpha, r_alpha, eye4)
    h_bc = eye64-sp.kronecker_product(eye4, r_alpha, r_alpha)
    h_e = h_ab+h_bc
    require(h_ab == h_ab.conjugate().T and h_bc == h_bc.conjugate().T,
            "both endpoint edge terms are Hermitian", checks)
    require(h_ab*h_ab == 2*h_ab and h_bc*h_bc == 2*h_bc,
            "each endpoint edge term has exact spectrum contained in zero and two", checks)

    psi = alpha/2
    psi3 = sp.kronecker_product(psi, psi, psi)
    require(h_e*psi3 == sp.zeros(64, 1),
            "aligned pinned matter vector is killed by endpoint energy", checks)
    require(m*psi3 == 90*psi3,
            "aligned pinned matter vector has first-order energy 3/2", checks)

    # Exact characteristic polynomial of M=60K.
    x = sp.symbols("x")
    characteristic = DomainMatrix.from_Matrix(x*sp.eye(64)-m).det().as_expr()
    expected = ((x-130)*(x-126)**2*(x-120)**6*(x-118)**2*(x-114)**7*
                (x-112)**6*(x-110)**12*(x-108)**6*(x-106)**3*
                (x-100)**6*(x-90)*(x**2-236*x+13876)**6)
    require(sp.expand(characteristic-expected) == 0,
            "exact 64x64 first-order characteristic polynomial", checks)
    require(sp.degree(characteristic, x) == 64,
            "characteristic polynomial has full degree 64", checks)

    # The bottom eigenvalue is 90/60=3/2, simple.  The next is 100/60=5/3.
    # Because H_E>=0 and annihilates the unique K-ground vector, K+jH_E has
    # the same ground and no smaller first excited energy for every j>=0.
    require(sp.Rational(100-90, 60) == sp.Rational(1, 6),
            "exact first-order gap is 1/6", checks)
    require(18**2 > 48,
            "quadratic factor has lower root 118-sqrt(48) above 100", checks)

    # Arithmetic behind the uniform Schur bounds.  With ||B||<=2,
    # ||A-E||<=4j+11/2, ||(lambda QVQ)^-1||<=2/lambda and
    # ||(QHQ-E)^-1||<=4/lambda, the first remainder is
    # (128j+176)/lambda^2.  The P1 elimination adds at most 867/lambda^2.
    j = sp.symbols("j", nonnegative=True)
    lam = sp.symbols("lambda", positive=True)
    r1_numerator = 4*4*2*(4*j+sp.Rational(11, 2))
    require(sp.expand(r1_numerator-(128*j+176)) == 0,
            "first resolvent remainder numerator is 128j+176", checks)
    require(12*sp.Rational(17, 2)**2 == 867,
            "second Feshbach remainder numerator is 867", checks)
    require((128*j+176)+867 == 128*j+1043,
            "combined remainder is below reported 128j+1100", checks)

    # User threshold implies all subordinate hypotheses for every j>=0.
    threshold_margin = sp.expand(10**6*(j+1)-480*(1100+128*j))
    require(sp.Poly(threshold_margin, j).all_coeffs() == [938560, 472000],
            "one-million threshold implies the spectral-gap threshold", checks)
    require(sp.expand(10**6*(j+1)-1000*(j+1)) == 999000*(j+1),
            "one-million threshold implies the resolvent threshold", checks)

    # Old homogeneous-chain projective obstruction.  Phase balance requires
    # k1+k2=3 mod4.  Equal source sectors, forced by uniqueness in the presence
    # of separately conserved sectors plus mirror exchange, have Weyl central
    # exponent 3-k1-k2=3-2k=1 or 3 mod4, hence zeta=+/-i.
    exponents = [(3-2*k0) % 4 for k0 in range(4)]
    require(exponents == [3, 1, 3, 1],
            "equal sectors have primitive fourth-root Weyl commutator", checks)
    require(not any((2*k0-3) % 4 == 0 for k0 in range(4)),
            "equal sectors cannot satisfy phase balance", checks)

    result = {
        "research_id": "UR.COMPILER.NEW_OVERLAP.SCHUR_AUDIT.20260919",
        "verdict": "EXACT_FIRST_ORDER_AND_CONDITIONAL_GLOBAL_SCHUR_BOUND",
        "first_order_characteristic_polynomial": str(sp.factor(characteristic)),
        "first_order_ground": "3/2, multiplicity 1",
        "first_order_next": "5/3, multiplicity 6",
        "first_order_gap": "1/6 for all j>=0 by min-max",
        "uniform_remainder_bound": "(1043+128j)/lambda^2 < (1100+128j)/lambda^2",
        "D_internal_gap": "1/(120 lambda)",
        "full_gap_bound": "1/(120 lambda)-2(1100+128j)/lambda^2 >= 1/(240 lambda)",
        "sufficient_threshold": "lambda >= 480(1100+128j)",
        "reported_threshold": "lambda >= 1000000(j+1) implies every bound above",
        "global_scope": (
            "Requires the displayed operator bounds uniformly for the chosen low-energy "
            "E-window, positivity/invertibility of Q(H-E)Q and of the P1 Schur block, "
            "and the exact identification P0 Dfull P0=(153I+2A32-F)/3600."
        ),
        "old_homogeneous_no_go": (
            "With separately conserved source-quarter sectors and mirror exchange, unequal "
            "sectors occur in pairs. Equal sectors have Weyl commutator +/-i, so invariant "
            "energy eigenspaces have dimension divisible by four; phase balance also excludes "
            "k1=k2 for a nondegenerate state."
        ),
        "source_sha256": SOURCE_SHA256,
        "checks": checks,
    }
    (HERE / "schur_check.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
