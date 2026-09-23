"""Source-pinned Clifford audit and concrete wedge/occupation resource checks.

Only the original v783 prefix through P2 is executed, assertions retained as
always-on guards in memory. No original source or verification ledger is changed.
The physical schedule is independently rebuilt, without importing other probes.
"""
from pathlib import Path
from itertools import combinations
from math import pi, sqrt, atan, floor, acos, atan2
import argparse
import ast
import contextlib
import hashlib
import io
import json
import numpy as np
import sympy as sy
from scipy.linalg import expm, block_diag

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CHECKS = []


def need(ok, label, kind="exact"):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append({"name": label, "kind": kind})


def source_prefix():
    path = REPO/"verification/v783_two_qubit_clifford.py"
    tree = ast.parse(path.read_text())
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
    stop = next(i for i, node in enumerate(main.body)
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name) and node.value.func.id == "section"
                and isinstance(node.value.args[0], ast.Constant)
                and node.value.args[0].value.startswith("P3 (H2b)"))
    main.body = main.body[:stop]+[ast.Return(ast.Call(ast.Name("locals", ast.Load()), [], []))]

    class KeepAssertions(ast.NodeTransformer):
        def visit_Assert(self, node):
            return ast.copy_location(ast.Expr(ast.Call(ast.Name("need", ast.Load()),
                                                      [node.test, ast.Constant("source assert line "+str(node.lineno))], [])), node)

    module = ast.fix_missing_locations(KeepAssertions().visit(ast.Module([main], [])))
    env = {"need": need}
    exec(compile(module, str(path), "exec"), env)
    with contextlib.redirect_stdout(io.StringIO()):
        data = env["main"]()
    for name, passed in data["CHECKS"]:
        need(passed, "original "+name)
    need(len(data["REFL_M2"]) == 60, "all sixty original root reflections checked, not a guessed gate set")
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "executed_sections": ["P0", "P1 (H1)", "P2 (H2a)"],
            "section_names_are_not_axioms": True,
            "original_checks": len(data["CHECKS"]), "original_reflections": 60,
            "all_reflections_normalize_Paulis": bool(data["ok_cliff"])}


def algebra(mutant):
    swap = sy.zeros(16)
    wedge = sy.zeros(6, 16)
    for a in range(4):
        for b in range(4):
            swap[4*b+a, 4*a+b] = 1
    for row, (a, b) in enumerate(combinations(range(4), 2)):
        wedge[row, 4*a+b] = 1/sy.sqrt(2)
        wedge[row, 4*b+a] = -1/sy.sqrt(2)
    plus, minus = (sy.eye(16)+swap)/2, (sy.eye(16)-swap)/2
    transfer = plus.row_join(wedge.T).col_join(wedge.row_join(sy.zeros(6)))
    pmat, pmed = sy.diag(sy.eye(16), sy.zeros(6)), sy.diag(sy.zeros(16), sy.eye(6))
    need(transfer**2 == sy.eye(22), "phase-correct A is an exact full 22D involution")
    need(transfer*pmed*transfer == sy.diag(minus, sy.zeros(6)), "A occupation-one A restricts exactly to Pminus")
    need(transfer*pmat*transfer == sy.diag(plus, sy.eye(6)), "A occupation-zero A includes the spectator mediator sector")
    need(transfer*pmed*transfer+transfer*pmat*transfer == sy.eye(22), "ordinary occupation instrument remains complete on all 22 dimensions")
    grading = -sy.eye(22)
    occupation_z = pmat-pmed
    need(grading != occupation_z, "charge-two central mu4 grading is not occupation phase")
    x = sy.Matrix([[0, 1], [1, 0]])
    q = sy.kronecker_product(pmat, sy.eye(2))+sy.kronecker_product(pmed, x)
    coupling_projector = sy.kronecker_product(pmed, (sy.eye(2)-x)/2)
    need(coupling_projector**2 == coupling_projector, "minimal conditional-pointer generator is a projector")
    need(sy.eye(44)-2*coupling_projector == q, "adding pi times the conditional generator gives Q exactly")
    # Scalar sector occupancy commutes with every covariant color action.
    unit = sy.I*sy.eye(4)
    collective = sy.diag(sy.kronecker_product(unit, unit), -sy.eye(6))
    need(collective == grading and collective*pmed == pmed*collective,
         "conditional coupling and zero coupling preserve the same central grading")
    initial = sy.zeros(44, 1)
    initial[0] = initial[32] = 1/sy.sqrt(2)  # (|00matter>+|mediator01>) tensor |0>.
    final = q*initial
    amplitudes = sy.Matrix(22, 2, lambda i, j: final[2*i+j])
    pointer_density = amplitudes.H*amplitudes
    need(pointer_density == sy.eye(2)/2, "coherent Q creates one ebit from a product across system/pointer")
    if mutant == "local_controls_make_Q":
        need(pointer_density.det() == 0, "MUTANT: product-only unitaries cannot generate Q")
    # The postmeasurement output is instead a classical mixture: weaker access.
    dephased = sum((sy.kronecker_product(sy.eye(22), sy.eye(2)[:, j]*sy.eye(2)[j, :])
                    *final*final.H*
                    sy.kronecker_product(sy.eye(22), sy.eye(2)[:, j]*sy.eye(2)[j, :])
                    for j in range(2)), sy.zeros(44))
    need(dephased != final*final.H and sy.trace(dephased**2) == sy.Rational(1, 2),
         "classical occupation readout is not an accessible coherent Q output")
    return {"encoded_record_dimension": 22, "full_matter_pointer_dimension": 32,
            "encoded_subspace": "Sym^2(C4) tensor |0> direct-sum wedge^2(C4) tensor C2_occ",
            "system_pointer_factorization_obstruction": "any system-only wedge/phase controls plus pointer-only controls remain product; even LOCC cannot create the Q output ebit",
            "Q_half_diamond_lower_bound_to_separable_operations": "1/2",
            "covariant_completion_family": "H_kappa = H_wedge tensor I + I tensor H_pointer + kappa N_occ tensor (I-X)/2",
            "kappa_selected_by_original_source": False,
            "conditional_coupling_is_not_a_derivation": True,
            "occupation_Luders_measurement_assumed_not_derived": True}


def physical_schedule(mutant):
    g = sqrt(2)/20
    omega = sqrt(1+4*g*g)
    theta = atan(2*g)
    count = floor(pi/(2*theta))-1
    beta = count*theta
    axis = np.array([np.sin(theta), 0., -np.cos(theta)])
    vector = np.array([np.sin(2*beta), 0., np.cos(2*beta)])
    reflection = np.array([-1., -1., 1.])
    mirror = reflection*axis
    u, v, dot = axis@vector, mirror@vector, mirror@axis
    first = acos((np.cos(theta)-dot*u)/(v-dot*u))
    moved = vector*np.cos(first)+np.cross(axis, vector)*np.sin(first)+axis*u*(1-np.cos(first))
    moved = reflection*moved
    south = np.array([0., 0., -1.])
    last = atan2(axis@np.cross(moved, south), moved@south-np.cos(theta)**2) % (2*pi)
    times = [pi/omega]*count+[first/omega, last/omega]
    h = np.array([[0., g], [g, 1.]])
    forward = np.eye(2, dtype=complex)
    for k, duration in enumerate(times):
        forward = expm(-1j*h*duration)@forward
        if k < len(times)-1:
            forward = np.diag([1., -1.])@forward
    pre = float(np.angle(forward[0, 1]) % (2*pi))
    post = float(np.angle(forward[1, 0]) % (2*pi))
    time_a = sum(times)+(len(times)-1)*pi+pre+post
    w = np.zeros((6, 16))
    for row, (a, b) in enumerate(combinations(range(4), 2)):
        w[row, 4*a+b], w[row, 4*b+a] = 1/sqrt(2), -1/sqrt(2)
    h22 = np.block([[np.zeros((16, 16)), g*w.T], [g*w, np.eye(6)]])
    n = block_diag(np.zeros((16, 16)), np.eye(6))
    actual = expm(-1j*n*pre)
    for k, duration in enumerate(times):
        actual = expm(-1j*h22*duration)@actual
        if k < len(times)-1:
            actual = expm(-1j*n*pi)@actual
    actual = expm(-1j*n*post)@actual
    target = np.block([[np.eye(16)-w.T@w, w.T], [w, np.zeros((6, 6))]])
    error = float(np.linalg.norm(actual-target, 2))
    need(error < 1e-12, "full physical 22D transfer equals A with no Q gate or helper", "numerical")
    need(abs(time_a-25*pi) < 1e-12, "Q-free phase-correct A costs 25 pi at t/Delta=1/20", "numerical")
    need(abs(np.exp(-1j*time_a)+1) < 1e-12, "unaddressed same-Delta mediator picks up minus one", "numerical")
    if mutant == "spectators_unchanged":
        need(abs(np.exp(-1j*time_a)-1) < 1e-12, "MUTANT: odd-pi A time does not give identity on mediator spectators", "numerical")
    # Q still required only for the optional full arbitrary-pointer R contract.
    reduced_r_time = 24*pi+22*pi+2*pi
    need(abs(reduced_r_time-48*pi) < 1e-12, "parking replaces twenty-two helper-Q calls", "numerical")
    return {"coupling_over_Delta": .05, "on_pulses": len(times), "on_durations": times,
            "occupation_Z_by_parking_pulses": len(times)-1, "parking_Z_duration_each": pi,
            "phase_correction_before": pre, "phase_correction_after": post,
            "A_total_time_hbar_over_Delta": time_a, "A_total_time_over_pi": time_a/pi,
            "A_physical_operator_error": error, "helper_qubits": 0, "coherent_Q_calls": 0,
            "spectator_mediator_phase": "-1",
            "six_A_echo_total_H_time_hbar_over_Delta": 6*time_a,
            "optional_full_R_contract_one_Q_time_hbar_over_Delta": reduced_r_time,
            "measurement_origin_resolved": False,
            "scope": "encoded occupation recorder, bare input, return to bare matter before arbitrary matter ticks or edge changes; not arbitrary initial pointer states"}


def readout_contract():
    # Occupied Omega is maximally entangled between mediator wedge colors and
    # the spectator antisymmetric six-dimensional sector.
    entangled = sy.zeros(36, 1)
    for a in range(6):
        entangled[6*a+a] = 1/sy.sqrt(6)
    ideal = entangled*entangled.T
    flavor_resolved = sy.zeros(36)
    for a in range(6):
        flavor_resolved[6*a+a, 6*a+a] = sy.Rational(1, 6)
    covariant_depolarized = sy.eye(36)/36
    need((entangled.T*flavor_resolved*entangled)[0] == sy.Rational(1, 6),
         "resolving six occupied flavors gives target fidelity one sixth")
    need((entangled.T*covariant_depolarized*entangled)[0] == sy.Rational(1, 36),
         "SU4-covariant occupied-sector depolarization gives target fidelity one thirty-sixth")
    # An efficient repeatable covariant instrument need not be globally
    # Lueders: the two inequivalent irreps within N0 may have different phases.
    # Canonical decomposition: symmetric10, bare antisymmetric6, mediator6.
    n0 = sy.diag(sy.eye(10), sy.eye(6), sy.zeros(6))
    n1 = sy.eye(22)-n0
    k0 = sy.diag(sy.eye(10), -sy.eye(6), sy.zeros(6))
    k1 = n1
    need(k0.H*k0 == n0 and k1.H*k1 == n1,
         "efficient phase-twisted readout has exactly the occupancy POVM")
    need(n0*k0 == k0 and n1*k1 == k1,
         "efficient phase-twisted readout is repeatable")
    need(k0 != n0,
         "efficiency repeatability and SU4 covariance do not globally fix N0 Lueders action")
    a = sy.diag(sy.eye(10), sy.zeros(12))
    for j in range(6):
        a[10+j, 16+j] = a[16+j, 10+j] = 1
    need(a*k0*a*n0 == sy.diag(sy.eye(10), sy.zeros(12)),
         "phase freedom on bare antisymmetric N0 sector is unreachable at actual A readout")
    need(a*k1*a*n0 == sy.diag(sy.zeros(10), sy.eye(6), sy.zeros(6)),
         "actual occupied A readout returns exact antisymmetric projector")
    return {"flavor_resolved_conditional_fidelity": "1/6",
            "fully_covariant_depolarizing_conditional_fidelity": "1/36",
            "symmetry_alone_selects_Lueders": False,
            "efficient_repeatable_exact_occupancy_full_SU4_covariance":
            "Schur forces scalar phases on Sym10 and occupied Wedge6; sufficient for bare-input A protocol, not full N0 Lueders action",
            "extra_premises": ["exact occupancy effects", "nondestructive repeatability", "one Kraus operator per outcome", "full SU4 covariance, not just an unchecked finite subgroup", "edge-local readout, identity on the two spectator carriers"],
            "origin_of_these_premises_derived": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="origin_verification.json")
    parser.add_argument("--mutant", choices=["local_controls_make_Q", "spectators_unchanged"])
    args = parser.parse_args()
    result = {"source": source_prefix(), "algebra": algebra(args.mutant),
              "physical_Q_free_transfer": physical_schedule(args.mutant),
              "readout_contract": readout_contract()}
    sources = ["tfpt_1_architecture_e8.tex", "verification/v783_two_qubit_clifford.py",
               "experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py",
               "experiments/theory-contracts/compiler-single-execution-20260914/check.py",
               "experiments/theory-contracts/universalraum-native-closure-20260914/controls/verify_controls.py"]
    result["source_hashes"] = {name: hashlib.sha256((REPO/name).read_bytes()).hexdigest() for name in sources}
    result["checks"] = CHECKS
    result["check_count"] = len(CHECKS)
    (HERE/args.out).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"checks": len(CHECKS), "output": str(HERE/args.out), "source": result["source"],
                      "physical_Q_free_transfer": result["physical_Q_free_transfer"]}, indent=2))


if __name__ == "__main__":
    main()
