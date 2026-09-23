"""Native boson-phase intervention and coherent composition recording.

The phase belongs to the documented X,Nb control algebra. Its switchability,
the ready pointer, its conditional coupling, and terminal readout remain
explicit resources; fixed-H evolution alone supplies none of those controls.
"""
from argparse import ArgumentParser
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import math

import numpy as np
import sympy as s
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
W_PIN = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
checks = []


def need(condition, name, kind="exact"):
    if not condition:
        raise RuntimeError(name)
    checks.append({"name": name, "kind": kind})


def equal(A, B, name):
    difference = A - B
    ok = all(s.simplify(x) == 0 for x in difference) if isinstance(difference, s.MatrixBase) else s.simplify(difference) == 0
    need(ok, name)


def main():
    manifest = json.loads((HERE / "inputs_manifest.json").read_text())
    for name, record in manifest.items():
        data = (HERE / "inputs" / name).read_bytes()
        need(sha256(data).hexdigest() == record["sha256"] and len(data) == record["bytes"], "frozen input " + name)
    need(manifest["spinor_tensors.npz"]["sha256"] == W_PIN, "original native W pin")
    with np.load(HERE / "inputs/spinor_tensors.npz", allow_pickle=False) as archive:
        raw = archive["W"]
    need(raw.shape == (60, 2016), "native carrier dimensions")
    need(np.count_nonzero(raw.imag) == 0 and np.array_equal(raw.real, np.rint(raw.real)), "lossless integer W")
    W = raw.real.astype(np.int64)
    need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)), "exact native W Gram")
    pairs = list(combinations(range(64), 2))
    cols = list(map(int, np.flatnonzero(W[0])))
    need(len(cols) == 8 and np.count_nonzero(W[1:, cols]) == 0, "closed native eight-leaf star")
    leaves = [pairs[k] for k in cols]
    need(leaves[0] == (4, 57) and leaves[1] == (5, 56), "same pair seed and receiver as v168")
    need(len(set(i for pair in leaves for i in pair)) == 16, "disjoint native leaf modes")
    signs = s.Matrix([int(W[0, k]) for k in cols])
    Delta, g = s.symbols("Delta g", real=True, nonzero=True)
    H9 = s.zeros(9)
    H9[:8, 8] = g * signs
    H9[8, :8] = g * signs.T
    H9[8, 8] = Delta
    J = s.zeros(9, 3)
    J[0, 0] = 1
    J[8, 2] = 1
    for q in range(1, 8):
        J[q, 1] = signs[q] / s.sqrt(7)
    I = s.eye(3)
    B = s.diag(0, 0, 1)
    E = s.diag(0, s.Rational(1, 7), 0)
    X = s.Matrix([[0, 0, -1], [0, 0, s.sqrt(7)], [-1, s.sqrt(7), 0]])
    H = Delta * B + g * X
    Z = I - 2 * B
    oldZ = s.diag(-1, 1, 1)
    equal(J.T * J, I, "same common3 adapter is isometric")
    equal(H9 * J, J * H, "same original H preserves common3 exactly")
    B9 = s.diag(*([0] * 8), 1)
    equal(B9 * J, J * B, "native total boson number preserves common3")
    equal((s.eye(9) - 2 * B9) * J, J * Z, "native boson parity preserves common3")
    n5 = s.diag(0, 1, *([0] * 7))
    equal(J.T * n5 * J, E, "same terminal receiver compression")
    equal(Z.T * Z, I, "boson phase is a unitary one-Kraus CPTP intervention")
    equal(Z * E - E * Z, s.zeros(3), "boson sender phase commutes with fermion receiver effect")
    equal(Z * E * Z, E, "no immediate receiver-statistic change for any input")
    equal(Z * H * Z, Delta * B - g * X, "phase reverses interaction but leaves detuning intact")
    need(H * Z - Z * H != s.zeros(3), "boson phase does not commute with fixed H")
    equal(s.diag(1, 1, s.exp(s.I * s.pi)), Z, "Zb equals exp(i pi Nb)")

    # X,Nb preserve the native bright/dark decomposition. The old single-mode
    # phase does not; replacing it truly removes a separate operator type.
    dark = I - X * X / 8
    equal(dark * dark, dark, "dark projector idempotence")
    equal(s.trace(dark), 1, "one-dimensional dark subspace")
    equal(dark * X, s.zeros(3), "X annihilates native dark direction")
    equal(dark * B, s.zeros(3), "Nb annihilates native dark direction")
    equal(dark * Z - Z * dark, s.zeros(3), "new phase stays in documented block algebra")
    need(oldZ * dark - dark * oldZ != s.zeros(3), "old single-mode Z4 lies outside the X,Nb algebra")
    algebra_basis = [I, B, X, s.I * (B * X - X * B), X * X]
    def flatten(A):
        return s.Matrix(list(A))
    algebra_matrix = s.Matrix.hstack(*map(flatten, algebra_basis))
    need(algebra_matrix.rank() == 5, "documented common3 control algebra has complex dimension five")
    for a, A in enumerate(algebra_basis):
        for b, BB in enumerate(algebra_basis):
            need(algebra_matrix.row_join(flatten(A * BB)).rank() == 5, "control algebra multiplication closure " + str((a, b)))

    # tau=pi/(2Omega), d=Delta/(2Omega), r=sqrt8 g/Omega,
    # u=exp(-i pi d/2), r^2=1-d^2. Derive all formulas algebraically.
    d, r = s.symbols("d r", real=True)
    u = s.symbols("u", nonzero=True)
    bright = s.Matrix([-1, s.sqrt(7), 0]) / s.sqrt(8)
    boson = s.Matrix([0, 0, 1])
    Pbright = bright * bright.T
    equal(Pbright + B + dark, I, "bright boson dark decomposition")
    U = dark + u * (s.I * d * Pbright - s.I * r * (bright * boson.T + boson * bright.T) - s.I * d * B)
    def reduce(expression):
        return s.simplify(s.expand(expression).subs(r * r, 1 - d * d))
    def dagger(A):
        return A.conjugate().T.subs(s.conjugate(u), 1 / u)
    equal((dagger(U) * U).applyfunc(reduce), I, "exact half-period propagator unitarity")
    seed = s.Matrix([1, 0, 0])
    midpoint = U * seed
    free = (U * midpoint).applyfunc(reduce)
    pulse = (U * Z * midpoint).applyfunc(reduce)
    equal(free[2], 0, "unintervened full-period endpoint has no boson")
    equal(pulse[2], -d * r * u**2 / s.sqrt(2), "phase-intervened endpoint boson amplitude")
    probability = lambda state, O: reduce((dagger(state) * O * state)[0])
    c = s.symbols("c", real=True)
    cos_identity = (u**2 + u**-2) / 2
    p0 = (1 + c) / 32
    p1 = (1 + (1 - 2*d*d)**2 - 2 * (1 - 2*d*d) * c) / 64
    delta = -(1 - d*d) * (d*d + c) / 16
    equal(probability(free, E), p0.subs(c, cos_identity), "untouched n5 probability")
    equal(probability(pulse, E), p1.subs(c, cos_identity), "boson-phase n5 probability")
    equal(p1 - p0, delta, "unconditional delayed fermion response formula")
    equal(probability(pulse, B), d*d * (1 - d*d) / 2, "explicit final composition change in pulsed arm")
    equal(probability(midpoint, B), (1 - d*d) / 8, "midpoint boson probability")
    H_in_omega_units = 2*d*B + r*X/s.sqrt(8)
    equal(probability(midpoint, H_in_omega_units), 0, "native midpoint has unchanged zero system energy")
    equal(probability(Z*midpoint, H_in_omega_units), d*(1-d*d)/2,
          "phase work in Omega units equals Delta(1-d^2)/4")
    equal(Z * seed, seed, "phase on the initial empty-boson seed has no effect")
    equal(Delta**2 / (4 * (Delta**2/4 + 8*g*g)) - s.Rational(4, 9),
          (5*Delta**2 - 128*g*g) / (9*(Delta**2 + 32*g*g)), "d>=2/3 translates to g^2<=5Delta^2/128")
    need(s.Rational(22, 7)**2 < 10, "rational upper bound for pi squared used in positivity proof")
    equal(1 + d - s.Rational(242, 49) * (1-d), (291*d - 193) / 49, "strict positive response lower-bound factor")
    need(291*s.Rational(2, 3) - 193 == 1, "lower-bound factor positive throughout d>=2/3")
    need(s.Rational(1, 400) < s.Rational(5, 128), "original g/Delta=1/20 belongs to positive-response interval")

    # A REAL coarse composition-recording instrument. All pair alternatives
    # couple to the SAME pointer state; none are measured and relabelled.
    Q0, Q1 = I - B, B
    pointer_x = s.Matrix([[0, 1], [1, 0]])
    ptr0 = s.Matrix([1, 0])
    ptr1 = s.Matrix([0, 1])
    record_unitary = s.kronecker_product(Q0, s.eye(2)) + s.kronecker_product(Q1, pointer_x)
    record = record_unitary * s.kronecker_product(I, ptr0)
    record_generator = s.pi/2 * s.kronecker_product(B, s.eye(2)-pointer_x)
    equal((-s.I*record_generator).exp(), record_unitary, "explicit finite neutral pointer coupling implements the claimed instrument")
    equal(record_unitary.H * record_unitary, s.eye(6), "neutral two-state pointer coupling is unitary")
    equal(record.H * record, I, "coherent record isometry preserves the complete joint Gram kernel")
    equal(record * s.Matrix([1, 0, 0]), s.kronecker_product(s.Matrix([1, 0, 0]), ptr0), "first pair direction has pointer zero")
    equal(record * s.Matrix([0, 1, 0]), s.kronecker_product(s.Matrix([0, 1, 0]), ptr0), "coherent sum R7 has same pointer zero")
    equal(record * boson, s.kronecker_product(boson, ptr1), "boson direction has pointer one")
    equal(record.H * s.kronecker_product(E, s.eye(2)) * record, E, "recording has no immediate receiver effect for any state")
    equal(Q0.H * Q0 + Q1.H * Q1, I, "discarding pointer gives a complete trace-preserving coarse instrument")
    m = s.symbols("rho:9")
    rho = s.Matrix(3, 3, m)
    reduced_record = Q0 * rho * Q0 + Q1 * rho * Q1
    equal(reduced_record, (rho + Z * rho * Z) / 2, "unconditional recording equals equal mixture of identity and boson phase")
    record_mid_energy = (probability(midpoint, H_in_omega_units) + probability(Z*midpoint, H_in_omega_units))/2
    equal(record_mid_energy, d*(1-d*d)/4, "record work in Omega units equals Delta(1-d^2)/8")
    eta = s.symbols("eta", real=True)
    soft_record = Q0*rho*Q0 + Q1*rho*Q1 + eta*(Q0*rho*Q1 + Q1*rho*Q0)
    equal(soft_record, (1+eta)*rho/2 + (1-eta)*Z*rho*Z/2, "partial record overlap controls pair-boson coherence exactly")
    joint_end = s.kronecker_product(U, s.eye(2)) * record * midpoint
    joint_end_dagger = joint_end.conjugate().T.subs(s.conjugate(u), 1/u)
    p_record = reduce((joint_end_dagger * s.kronecker_product(E, s.eye(2)) * joint_end)[0])
    equal(p_record, ((p0 + p1)/2).subs(c, cos_identity), "coherently evolved record yields average unconditional receiver probability")
    equal((p0+p1)/2 - p0, delta/2, "full composition recording causes half the phase-intervention signal without postselection")

    # General algebraic induction for the symmetry no-delayed-effect theorem.
    # If [V,H]=[V,B]=0, this Jacobi identity propagates commutation to every
    # time derivative and hence to the finite-sector exponential.
    Vn, Hn, On = s.symbols("V H O", commutative=False)
    comm = lambda A, BB: A*BB - BB*A
    equal(s.expand(comm(Vn, comm(Hn, On)) - comm(Hn, comm(Vn, On)) - comm(comm(Vn, Hn), On)),
          0, "exact Jacobi induction identity for symmetry impulse no-delayed-signal theorem")

    # General source-comparison adapter: an initial state on the boson side
    # of [[0,g Cdag],[g C,Delta I]] reveals C Cdag in its loss curvature.
    nleft, nright = s.symbols("nleft nright", integer=True, positive=True)
    coupling = s.MatrixSymbol("C", nright, nleft)
    coupling_dag = s.Adjoint(coupling)
    block_H = s.BlockMatrix([[s.ZeroMatrix(nleft, nleft), g*coupling_dag],
                            [g*coupling, Delta*s.Identity(nright)]])
    block_B = s.BlockMatrix([[s.ZeroMatrix(nleft, nleft), s.ZeroMatrix(nleft, nright)],
                            [s.ZeroMatrix(nright, nleft), s.Identity(nright)]])
    block_L1 = s.block_collapse(s.I*(block_H*block_B - block_B*block_H))
    block_L2 = s.block_collapse(s.I*(block_H*block_L1 - block_L1*block_H))
    block_L3 = s.block_collapse(s.I*(block_H*block_L2 - block_L2*block_H))
    need(block_L1.blocks[1, 1] == s.ZeroMatrix(nright, nright), "general block initial boson survival first derivative zero")
    need(block_L2.blocks[1, 1] == -2*g*g*coupling*coupling_dag, "general block boson survival second derivative is -2g^2 C Cdag")
    need(block_L3.blocks[1, 1] == s.ZeroMatrix(nright, nright), "general block initial boson survival third derivative zero")

    # Independent small-matrix numerical evolution, no symbolic half-period
    # formula used to form the time evolution.
    omega = math.sqrt(1/4 + 8/400)
    tau = math.pi / (2 * omega)
    dn = 1 / (2 * omega)
    hn = np.array(H.subs({Delta: 1, g: s.Rational(1, 20)}), dtype=float)
    un = expm(-1j * tau * hn)
    zn = np.diag([1, 1, -1])
    en = np.diag([0, 1/7, 0])
    sn = np.array([1, 0, 0], dtype=complex)
    fn, pn = un @ un @ sn, un @ zn @ un @ sn
    expected0 = float(p0.subs(c, math.cos(math.pi*dn)))
    expected1 = float(p1.subs({c: math.cos(math.pi*dn), d: dn}))
    need(abs(float(np.vdot(fn, en@fn).real)-expected0) < 1e-14, "independent expm untouched response", "numeric")
    need(abs(float(np.vdot(pn, en@pn).real)-expected1) < 1e-14, "independent expm boson-phase response", "numeric")
    rn = np.array(record, dtype=float)
    jointn = np.kron(un, np.eye(2)) @ rn @ un @ sn
    expected_record = (expected0 + expected1)/2
    need(abs(float(np.vdot(jointn, np.kron(en, np.eye(2)) @ jointn).real) - expected_record) < 1e-14,
         "independent six-state coherent recording response", "numeric")
    need(abs(np.linalg.norm(fn)-1) < 1e-14 and abs(np.linalg.norm(pn)-1) < 1e-14 and abs(np.linalg.norm(jointn)-1) < 1e-14,
         "independent unconditional probability normalization", "numeric")
    result = {"status": "PASS", "exact_checks": sum(x["kind"] == "exact" for x in checks),
              "numeric_checks": sum(x["kind"] == "numeric" for x in checks), "checks": checks,
              "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(), "W_sha256": W_PIN,
              "main": {"carrier": "same native N2 span p0,R7,b0", "intervention": "Zb=exp(i pi Nb)=diag(1,1,-1)",
                       "seed": "f4dag f57dag vacuum", "receiver": "n5, terminal effect diag(0,1/7,0)",
                       "sequence": "U(tau), optional Zb, U(tau), unconditional n5 readout", "tau": "pi/(2Omega)",
                       "Omega_squared": "Delta^2/4+8g^2", "d": "Delta/(2Omega)",
                       "free_n5": "(1+cos(pi d))/32",
                       "phase_n5": "[1+(1-2d^2)^2-2(1-2d^2)cos(pi d)]/64",
                       "causal_difference": "-(1-d^2)(d^2+cos(pi d))/16",
                       "strict_positive_interval": "Delta>0, 0<g^2<=5Delta^2/128",
                       "final_phase_Nb": "d^2(1-d^2)/2", "both_arms_same_final_species": False,
                       "phase_system_work": "Delta(1-d^2)/4; Delta/54 at g/Delta=1/20",
                       "test_point": {"Delta": "1", "g": "1/20", "tau": format(tau, ".16g"),
                                      "free_n5": format(expected0, ".16g"), "phase_n5": format(expected1, ".16g"),
                                      "difference": format(expected1-expected0, ".16g"),
                                      "record_n5": format(expected_record, ".16g"),
                                      "record_difference": format((expected1-expected0)/2, ".16g")}},
              "record": {"joint_dimension": 6, "isometry": "(I-Nb)psi tensor |0> + Nb psi tensor |1>",
                         "all_pair_coherence_preserved": True, "full_joint_Gram_preserved": True,
                         "isolated_pair_boson_coherence_preserved_when_record_discarded": False,
                         "discarded_record_channel": "(rho+Zb rho Zb)/2", "postselection": False,
                         "record_system_work": "Delta(1-d^2)/8; Delta/108 at g/Delta=1/20",
                         "unconditional_signal": "one half of phase signal",
                         "partial_pointer_overlap_eta_signal": "(1-eta)/2 times phase signal"},
              "operation_boundary": {"documented_control_algebra": "C on dark direct-sum M2 on bright-boson",
                                     "complex_dimension": 5, "Zb_in_X_Nb_algebra": True, "old_Z4_in_X_Nb_algebra": False,
                                     "Zb_is_fixed_H_word": False,
                                     "independent_X_Nb_switchability_compiler_derived": False,
                                     "pointer_preparation_and_conditional_Nb_coupling_derived": False,
                                     "terminal_n5_readout_derived": False,
                                     "pure_G_impulse_delayed_signal_when_commuting_receiver": False},
              "block_curvature_adapter": {"Hamiltonian": "[[0,g Cdag],[g C,Delta I]]", "input": "normalized boson-side v",
                                          "p_Nb": "1-g^2 <v,C Cdag v> t^2 + O(t^4)",
                                          "second_derivative": "-2g^2 <v,C Cdag v>",
                                          "dimension": "arbitrary finite block dimensions", "derivative_measurement_resource_derived": False},
              "scope": {"new_mode_selector_or_hopping_added": False, "same_native_H_between_operations": True,
                        "global_Nb_phase_not_spatially_local_gate": True,
                        "N64_ground_or_pole_used": False, "spacetime_derived": False}}
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"status": "PASS", "exact_checks": result["exact_checks"], "numeric_checks": result["numeric_checks"],
                          "result_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
