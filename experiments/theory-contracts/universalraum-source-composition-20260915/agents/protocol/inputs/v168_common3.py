"""One native three-dimensional carrier for causal response and tomography.

Only free H, local Z4, and Nb preserve this carrier. n5 is an exact terminal
effect there, but its actual projective instrument leaks. No native control
or preparation availability is inferred from these algebraic statements.
"""
from argparse import ArgumentParser
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
PIN = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
checks = []


def need(condition, label):
    if not condition:
        raise RuntimeError(label)
    checks.append(label)


def zero(matrix):
    return all(s.simplify(value) == 0 for value in matrix)


def vector(O):
    return s.Matrix([O[0, 0], O[1, 1], O[2, 2], s.re(O[0, 1]), s.re(O[0, 2]),
                     s.re(O[1, 2]), s.im(O[0, 1]), s.im(O[0, 2]), s.im(O[1, 2])])


def main():
    source = HERE / "sources" / "spinor_tensors.npz"
    need(sha256(source.read_bytes()).hexdigest() == PIN, "native W source SHA256")
    with np.load(source, allow_pickle=False) as archive:
        raw = archive["W"]
    need(raw.shape == (60, 2016), "full native W dimensions")
    need(np.count_nonzero(raw.imag) == 0 and np.array_equal(raw.real, np.rint(raw.real)), "lossless real integer W")
    W = raw.real.astype(np.int64)
    need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)), "native row Gram equals 8I")
    pairs = list(combinations(range(64), 2))
    columns = list(map(int, np.flatnonzero(W[0])))
    leaves = [pairs[k] for k in columns]
    need(len(columns) == 8, "chosen native boson couples eight leaves")
    need(np.count_nonzero(W[1:, columns]) == 0, "chosen leaves have no coupling to other bosons")
    need(len(set(j for pair in leaves for j in pair)) == 16, "all eight native leaf pairs are disjoint")
    need(leaves[0] == (4, 57) and leaves[1] == (5, 56), "same sender pair and terminal receiver as causal witness")
    signs = s.Matrix([int(W[0, k]) for k in columns])
    need(signs[0] == -1 and signs[1] == 1, "source signs for first two leaves")
    Delta, g = s.symbols("Delta g", real=True, nonzero=True)
    H9 = s.zeros(9)
    H9[:8, 8] = g * signs
    H9[8, :8] = g * signs.T
    H9[8, 8] = Delta
    Z9 = s.diag(-1, *([1] * 8))
    n5 = s.diag(0, 1, *([0] * 7))
    Nb9 = s.diag(*([0] * 8), 1)
    Nf9 = s.diag(*([2] * 8), 0)
    J = s.zeros(9, 3)
    J[0, 0] = 1
    for q in range(1, 8):
        J[q, 1] = signs[q] / s.sqrt(7)
    J[8, 2] = 1
    H = s.Matrix([[0, 0, -g], [0, 0, s.sqrt(7) * g], [-g, s.sqrt(7) * g, Delta]])
    Z = s.diag(-1, 1, 1)
    E = s.diag(0, s.Rational(1, 7), 0)
    B = s.diag(0, 0, 1)
    P = J * J.T
    need(J.T * J == s.eye(3), "three-dimensional adapter is exactly isometric")
    need(zero(H9 * J - J * H), "native H intertwines with H3 without leakage")
    need(zero(Z9 * J - J * Z), "local Z4 intertwines without leakage")
    need(zero(Nb9 * J - J * B), "Nb preserves common3 exactly")
    need(zero(J.T * Nf9 * J - s.diag(2, 2, 0)), "common3 fermion composition")
    need(zero(J.T * (Nf9 + 2 * Nb9) * J - 2 * s.eye(3)), "common3 total N is exactly two")
    need(zero(J.T * n5 * J - E), "n5 terminal effect compression is exact")
    residual = n5 * J - J * E
    need(zero(residual.T * residual - s.diag(0, s.Rational(6, 49), 0)), "n5 instrument leakage squared is 6/49 on R7")
    need(not zero(residual), "n5 is not an invariant instrument on common3")
    r7 = J[:, 1]
    rhor7 = r7 * r7.T
    measured = n5 * rhor7 * n5 + (s.eye(9) - n5) * rhor7 * (s.eye(9) - n5)
    need(s.simplify(s.trace((s.eye(9) - P) * measured)) == s.Rational(12, 49), "nonselective n5 measurement leaks weight 12/49 from initial R7")
    coarse = s.diag(0, *([1] * 7), 0)
    need(zero(coarse * J - J * s.diag(0, 1, 0)), "genuinely coarse seven-leaf projector preserves common3")
    finely_measured = s.zeros(9)
    for q in range(1, 8):
        pq = s.zeros(9)
        pq[q, q] = 1
        finely_measured += pq * rhor7 * pq
    need(s.simplify(s.trace((s.eye(9) - P) * finely_measured)) == s.Rational(6, 7), "fine leaf measurement with discarded labels is not the coarse Luders instrument")

    # This is the *same* causal protocol, restricted via a true intertwiner.
    z = s.symbols("z", nonzero=True)
    bright3 = s.Matrix([-1, s.sqrt(7), 0]) / s.sqrt(8)
    active3 = bright3 * bright3.T + B
    UT = s.eye(3) + (z - 1) * active3
    initial = s.Matrix([1, 0, 0])
    free = UT * UT * initial
    pulse = UT * Z * UT * initial
    need(free[2] == 0 and pulse[2] == 0, "same causal echo ends boson-free in both common3 arms")
    prob0 = s.simplify((free.T.subs(z, 1 / z) * E * free)[0])
    prob1 = s.simplify((pulse.T.subs(z, 1 / z) * E * pulse)[0])
    xz = 2 - z - 1 / z
    need(s.simplify(prob0 - xz * (4 - xz) / 64) == 0, "common3 reproduces exact untouched n5 probability")
    need(s.simplify(prob1 - 9 * xz * xz / 1024) == 0, "common3 reproduces exact pulsed n5 probability")

    def L(O):
        return s.I * (H * O - O * H)

    def C(O):
        return Z * O * Z

    LE, LB = L(E), L(B)
    L2E, L2B = L(LE), L(LB)
    L3E = L(L2E)
    names = ["E", "B", "L(E)", "L(B)", "L^2(E)", "L^2(B)", "L^3(E)", "C L^2(E)", "C L^2(B)"]
    basis = [E, B, LE, LB, L2E, L2B, L3E, C(L2E), C(L2B)]
    for name, O in zip(names, basis):
        need(zero(O.H - O), "Hermitian observable word " + name)
    M = s.Matrix.hstack(*map(vector, basis))
    det = s.factor(M.det())
    need(s.simplify(det - 8 * Delta**3 * g**10 / 343) == 0, "pulse temporal observable determinant 8 Delta^3 g^10 /343")
    need(det != 0, "pulse and time observable orbit spans Herm3 for nonzero Delta and g")

    # Identity is available from normalization. It is therefore wrong to say
    # that the pulse is necessary for tomography of normalized states.
    autonomous = [s.eye(3), E, B, LE, LB, L2E, L2B, L3E, L(L3E)]
    auto_matrix = s.Matrix.hstack(*map(vector, autonomous))
    need(s.simplify(auto_matrix.det() - 6 * Delta**3 * g**10 / 343) == 0,
         "autonomous temporal observables plus identity already span Herm3")
    invisible = s.Matrix([[6 * Delta, s.sqrt(7) * Delta, -g],
                          [s.sqrt(7) * Delta, 0, s.sqrt(7) * g],
                          [-g, s.sqrt(7) * g, 0]])
    need(zero(H * invisible - invisible * H), "unaugmented autonomous orbit has an exactly conserved orthogonal direction")
    need(s.trace(E * invisible) == 0 and s.trace(B * invisible) == 0, "orthogonal direction invisible in every autonomous terminal E and B observation")
    need(s.trace(invisible) == 6 * Delta, "autonomous invisible direction changes trace and is excluded for normalized state differences")
    need(s.Matrix.hstack(*map(vector, autonomous[1:])).rank() == 8, "unaugmented autonomous observable span has dimension eight")

    # Error map in dimensionless time u=Delta*t, at g/Delta=1/20.
    # xi stores the three diagonal entries and six real/imaginary offdiagonal
    # entries of rho. y_a=tr(rho O_a), so y=M^T D xi.
    metric = s.diag(1, 1, 1, 2, 2, 2, 2, 2, 2)
    point = {Delta: 1, g: s.Rational(1, 20)}
    measurement = (M.T * metric).subs(point)
    inverse = measurement.inv()
    need(zero(inverse * measurement - s.eye(9)), "exact linear tomography inverse at g/Delta=1/20")
    hs_frobenius_squared = s.simplify(sum(metric[i, i] * inverse[i, j]**2 for i in range(9) for j in range(9)))
    need(hs_frobenius_squared == s.Rational(9818033, 4), "exact squared Frobenius bound for output-to-Hilbert-Schmidt reconstruction map")
    need(s.simplify((s.sqrt(3) * s.sqrt(hs_frobenius_squared) / 2)**2 - s.Rational(29454099, 16)) == 0,
         "trace-distance reconstruction bound coefficient squared")

    result = {"status": "PASS", "exact_checks": len(checks), "checks": checks,
              "source_sha256": PIN,
              "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "carrier": {"dimension": 3, "basis": ["p0=(4,57)", "R7=sum(q=1..7) s_q p_q /sqrt7", "b0"],
                          "H3": [[str(v) for v in row] for row in H.tolist()],
                          "Z4": "diag(-1,1,1)", "E_n5": "diag(0,1/7,0)", "B_Nb": "diag(0,0,1)",
                          "H_leakage": "0", "Z4_leakage": "0", "Nb_leakage": "0",
                          "n5_leakage_residual_gram": "diag(0,6/49,0)",
                          "nonselective_n5_leakage_on_R7": "12/49",
                          "fine_seven_leaf_readout_leakage_on_R7": "6/7"},
              "tomography": {"L": "i[H3,.]", "C": "Z4(.)Z4", "basis": names,
                             "determinant": str(det), "rank": 9,
                             "autonomous_plus_identity_basis": ["I", "E", "B", "LE", "LB", "L2E", "L2B", "L3E", "L4E"],
                             "autonomous_plus_identity_determinant": "6 Delta^3 g^10/343",
                             "unaugmented_autonomous_rank": 8,
                             "pulse_necessary_for_normalized_state_tomography": False,
                             "time_unit_for_error_bound": "u=Delta t at g/Delta=1/20",
                             "HS_error_bound": "sqrt(9818033)/2 * ||delta y||_2",
                             "trace_distance_error_bound": "sqrt(29454099)/4 * ||delta y||_2",
                             "per_component_error_bound": "3 sqrt(29454099)/4 * epsilon",
                             "derivative_estimation_cost_included": False},
              "scope": {"same_carrier_as_native_pair_causal_witness": True,
                        "same_original_H_and_W": True,
                        "terminal_effect_tomography_complete": True,
                        "n5_instrument_closed_on_common3": False,
                        "postmeasurement_reuse_claimed": False,
                        "native_preparation_control_readout_derived": False,
                        "finite_sampling_protocol_optimized": False,
                        "N64_pole_or_spacetime_claim": False}}
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"status": "PASS", "exact_checks": len(checks), "result_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
