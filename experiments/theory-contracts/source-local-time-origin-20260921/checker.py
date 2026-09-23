#!/usr/bin/env python3
"""Exact finite witnesses for the attachment audit; general proofs are in PROOF.md.

No target RR block, Gamma, Vaux, or desired energies are inputs. Standard library.
Run normally and with -OO. Checks never depend on Python assertions.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json


def require(value, message):
    if not value:
        raise RuntimeError(message)


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def power(a, n):
    out = [[F(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out = multiply(out, a)
    return out


def even_weights(vector_weights, spin_lift=False):
    offset = F(sum(vector_weights), 2) if spin_lift else F(0)
    return [sum(vector_weights[i] for i in group) - offset
            for degree in (0, 2, 4)
            for group in combinations(range(5), degree)]


def run():
    # This checks pinned input bytes, not their mathematical correctness.
    here = Path(__file__).resolve().parent
    pins_path = here / "source_pins.json"
    pins = json.loads(pins_path.read_text())["sources"]
    require(bool(pins), "source pins must not be empty")
    for pin in pins:
        actual = hashlib.sha256(Path(pin["path"]).read_bytes()).hexdigest()
        require(actual == pin["sha256"], "source changed: " + pin["label"])

    # All-mode proof: m=1,n=1-k gives 2(k-1)q_k for every k>=2.
    # The following window is only an arithmetic sanity check of that proof.
    for k in range(2, 101):
        n = 1-k
        require(abs(n) - n == 2*(k-1), "Fourier necessity coefficient")
    q = {-1: F(1, 5), 0: F(1), 1: F(1, 5)}
    for m in range(-32, 33):
        for n in range(-32, 33):
            require((abs(m)*abs(n)-m*n)*q.get(m-n, 0) == 0,
                    "first-harmonic sufficiency witness")
    require(set((-1, 0, 1)).intersection(range(-8, 9, 4)) == {0},
            "quarter-clock intersection")
    weighted_defect = (abs(1)*abs(-3)-1*(-3))*F(3, 20)
    require(weighted_defect == F(9, 10), "positive weighted counterexample")
    require(F(1)-F(3, 10) > 0, "positive q bound")
    # The additive compression has determinant -epsilon^2/2<0.
    additive_det = -F(3, 10)**2/F(2)
    require(additive_det == -F(9, 200), "invalid additive DtN witness")

    # Polyakov-Alvarez witness sigma=epsilon*(1-r^2)^2.
    # Radial integrand |grad sigma|^2*r /epsilon^2 =16r^3-32r^5+16r^7.
    radial = F(16, 4)-F(32, 6)+F(16, 8)
    energy_over_pi_eps2 = 2*radial
    logdet_over_eps2 = -energy_over_pi_eps2/12
    require(energy_over_pi_eps2 == F(4, 3), "Dirichlet energy")
    require(logdet_over_eps2 == -F(1, 9), "Polyakov determinant")

    # Original recovery eigenmodes, not a fitted physical Hamiltonian.
    b = [[F(13,18),F(1,18),F(4,18)],
         [F(1,18),F(13,18),F(4,18)],
         [F(4,18),F(4,18),F(10,18)]]
    t = power(b, 6)
    vectors = ((1,1,1),(1,-1,0),(1,1,-2))
    roots = (F(1),F(2,3),F(1,3))
    for v, root in zip(vectors, roots):
        for i in range(3):
            require(sum(b[i][j]*v[j] for j in range(3)) == root*v[i], "B eigenpair")
            require(sum(t[i][j]*v[j] for j in range(3)) == root**6*v[i], "T eigenpair")
    expected = [[F(x,4374) for x in row] for row in
                ((1651,1267,1456),(1267,1651,1456),(1456,1456,1462))]
    require(t == expected, "exact original transfer")
    # General obstruction uses v_2(lambda2^m)=6m and v_2(lambda3^n)=0.
    require((roots[1]**6).numerator == 64, "nonzero 2-adic valuation")
    require((roots[2]**6).numerator == 1, "zero 2-adic valuation")

    # Internal winding, exterior algebra, and spin lift are different maps.
    y = (-2,-2,-2,3,3)
    require(sum(y) == 0, "actual hypercharge determinant winding")
    charge_counts = {}
    for weight in even_weights(y):
        charge_counts[str(weight)] = charge_counts.get(str(weight), 0)+1
    require(charge_counts == {"0":1,"-4":3,"1":6,"6":1,"2":3,"-3":2},
            "sixteen algebraic hypercharges retained")
    require(all(w.denominator == 1 for w in even_weights(y, True)),
            "hypercharge spin lift closes")
    weak_clutch = (0,0,0,1,0)
    require(all(w.denominator == 2 for w in even_weights(weak_clutch, True)),
            "odd determinant gives endpoint minus identity")
    require(all(w.denominator == 1 for w in even_weights(weak_clutch)),
            "Spin-c exterior action closes")
    require(sum(even_weights(weak_clutch)) == 8, "det exterior halfspin has degree eight")
    for k in range(-10, 11):
        a, bb = 1+2*k, -1-3*k
        require(3*a+2*bb == 1, "determinant-one winding family")
    require(1 % 2 == 1, "odd c1 prevents pure global spin lift on sphere")

    # Bilateral shift on a finite cyclic regulator: the lower-edge term matters.
    nmax = 5
    modes = list(range(-nmax,nmax+1))
    occupied = {n for n in modes if n < 0}
    shifted = {n+1 if n < nmax else -nmax for n in occupied}
    delta = {n:int(n in shifted)-int(n in occupied) for n in modes}
    require({n:v for n,v in delta.items() if v} == {-nmax:-1,0:1},
            "finite lower edge compensation")
    require(sum(delta.values()) == 0, "finite trace conservation")
    # A K-real covariance C=I/2 saturates distance 1/2 to each chirality.
    require(max(abs(F(1,2)-x) for x in (0,1)) == F(1,2), "sharp K-real bound")

    return {
        "contract": "UR.SOURCE.LOCAL_TIME_ORIGIN.01",
        "verdict": "PARTIAL",
        "finite_arithmetic_checks": "PASS",
        "general_proofs": "PROOF.md; not inferred from finite windows",
        "source_pins_checked": len(pins),
        "weighted_local_time": {
            "allowed_Fourier_support": [-1,0,1],
            "quarter_invariant_support": [0],
            "valid_geometric_counterexample_defect": str(weighted_defect),
            "invalid_additive_compression_determinant": str(additive_det)
        },
        "recovery_transfer": {
            "eigenvalues": [str(r**6) for r in roots],
            "direct_single_energy_lattice_intertwiner": "EXCLUDED",
            "two_exact_compressed_steps_also_excluded": True,
            "is_declared_physical_field_time_in_originals": False
        },
        "winding": {
            "hypercharge_determinant_degree": 0,
            "hypercharge_spin_endpoint": 1,
            "conditional_weak_clutch_degree": 1,
            "conditional_internal_spin_endpoint": -1,
            "global_pure_internal_spin_lift_for_odd_c1": False,
            "canonical_exterior_Spin_c_module_exists": True,
            "bundle_class_on_S2_fixed_by_rank_and_c1": True,
            "physical_seam_to_clutching_map_derived": False,
            "exterior_halfspin_charge_multiplicities": charge_counts
        },
        "scalar_determinant": {
            "Dirichlet_energy_over_pi_eps_squared": str(energy_over_pi_eps2),
            "logdet_change_over_eps_squared": str(logdet_over_eps2),
            "logZ_change_over_eps_squared": str(-logdet_over_eps2/2),
            "full_TFPT_measure_or_cancellation_decided": False
        },
        "finite_shift_charge_trace": sum(delta.values()),
        "complete_TFPT_solution": False,
        "physical_charged_source_selected": False
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
