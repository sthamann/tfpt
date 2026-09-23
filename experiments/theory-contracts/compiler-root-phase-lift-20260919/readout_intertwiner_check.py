"""Exact finite check of the quartic-to-native-60 readout intertwiner.

The check concerns the already identified grade-2 W5 x Bell10 corner.  It does
not select the POVM physically and does not transport the older Hamiltonian.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[3]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
GRADE2_CHECK = HERE / "grade2_character_check.py"
GRADE2_CERT = HERE / "grade2_character_certificate.json"
PINS = {
    SOURCE: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    GRADE2_CHECK: "3bf66af1035f86056d19c54328c93c048b9124b6265874630ebe92da6fd0d707",
    GRADE2_CERT: "01fb240730c42b4975d05a38cfbf69ca53684e452f8f0017af1a5792cd959827",
}
checks: Counter[str] = Counter()


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks[name] += 1


def tensor_power(a, degree):
    result = np.array([1], dtype=complex)
    for _ in range(degree):
        result = np.kron(result, a)
    return result


def exact_gaussian_matrix(a, scale, name):
    scaled = scale*a
    require(np.array_equal(scaled.real, np.rint(scaled.real)) and
            np.array_equal(scaled.imag, np.rint(scaled.imag)), name)
    return sp.Matrix([[sp.Rational(int(round(scale*a[i, j].real)), scale) +
                       sp.I*sp.Rational(int(round(scale*a[i, j].imag)), scale)
                       for j in range(a.shape[1])] for i in range(a.shape[0])])


def main():
    for path, digest in PINS.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "pinned input " + path.name)
    grade2 = json.loads(GRADE2_CERT.read_text())
    require(grade2["verdict"] == "EXACT_POSITIVE_GRADE2_INTERTWINER",
            "positive grade-2 input verdict")

    spec = importlib.util.spec_from_file_location("readout_native", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]
    bell_actions, _six, _symplectic = source.reflection_actions(rays)
    require(len(rays) == len(reflections) == len(bell_actions) == 60,
            "native sixty reflection data")

    # The five integral quartics and their exact 2+2 Bell-pair matrices K_A.
    words = list(it.product(range(4), repeat=4))
    quartics = np.zeros((256, 5), dtype=np.int64)
    for row, word in enumerate(words):
        counts = tuple(word.count(j) for j in range(4))
        if 4 in counts:
            quartics[row, 0] = 1
        elif counts in ((2,2,0,0), (0,0,2,2)):
            quartics[row, 1] = 1
        elif counts in ((2,0,2,0), (0,2,0,2)):
            quartics[row, 2] = 1
        elif counts in ((2,0,0,2), (0,2,2,0)):
            quartics[row, 3] = 1
        elif counts == (1,1,1,1):
            quartics[row, 4] = 1
    norms = np.diag(quartics.T@quartics)
    require(norms.tolist() == [4,12,12,12,24], "quartic squared norms")

    bell = np.column_stack([np.asarray(p, dtype=complex).reshape(16)/2
                            for p in source.SYMMETRIC_PAULIS])
    require(np.array_equal(bell.conj().T@bell, np.eye(10)), "Bell basis orthonormal")
    pair_coordinates = np.kron(bell, bell).conj().T@quartics
    require(np.array_equal(np.kron(bell, bell)@pair_coordinates, quartics),
            "quartics lie exactly in Bell tensor Bell")
    k_array = pair_coordinates.reshape(10, 10, 5)
    require(np.array_equal(k_array.imag, np.zeros_like(k_array.imag)) and
            np.array_equal(k_array.real, np.rint(k_array.real)), "K_A are integral real matrices")
    k_numpy = tuple(k_array[:, :, A].real.astype(np.int64) for A in range(5))
    require(all(np.array_equal(K, K.T) for K in k_numpy), "K_A are symmetric")
    require(all(int(np.sum(K*K)) == int(norms[A]) for A, K in enumerate(k_numpy)),
            "K_A Frobenius norms")
    K = tuple(sp.Matrix(matrix.tolist()) for matrix in k_numpy)

    # F_(A i),j=sqrt(2/n_A) K_Aij.  Rational identities establish both
    # F^*F=I and the two maximally mixed Bell marginals of Xi=vec(F)/sqrt(10).
    identity10 = sp.eye(10)
    source_gram = sum((sp.Rational(2, int(norms[A]))*(K[A].T*K[A])
                       for A in range(5)), sp.zeros(10))
    require(source_gram == identity10, "F is an exact isometry")
    rho_external = sum((sp.Rational(1, 5*int(norms[A]))*(K[A].T*K[A])
                        for A in range(5)), sp.zeros(10))
    rho_internal = sum((sp.Rational(1, 5*int(norms[A]))*(K[A]*K[A].T)
                        for A in range(5)), sp.zeros(10))
    require(rho_external == identity10/10 and rho_internal == identity10/10,
            "both Bell marginals of Xi are I10 over10")
    require(sp.trace(rho_external) == 1, "Xi is normalized")

    F = sp.Matrix.vstack(*(sp.sqrt(sp.Rational(2, int(norms[A])))*K[A]
                           for A in range(5)))
    Xi = F/sp.sqrt(10)  # coefficient matrix: source W5xBell versus external Bell
    require(sp.simplify(F.H*F) == identity10 and sp.simplify(Xi.H*Xi) == identity10/10,
            "radical normalization agrees with rational isometry certificate")

    # Native Bell rays v_l and their exact tight-frame identity.
    v_numpy = tuple(bell.conj().T@np.kron(z, z)/4 for z in rays)
    require(all(np.array_equal(2*v.real, np.rint(2*v.real)) and
                np.array_equal(2*v.imag, np.rint(2*v.imag)) for v in v_numpy),
            "native Bell-ray coordinates are Gaussian half-integers")
    V = sp.Matrix.hstack(*(exact_gaussian_matrix(v.reshape(10, 1), 2, "exact Bell ray")
                           for v in v_numpy))
    require(V.H*V != sp.eye(60), "native sixty frame is overcomplete")
    require(V*V.H == 6*identity10, "native sixty Bell rays form frame 6I")
    require(all((V[:, ell].H*V[:, ell])[0] == 1 for ell in range(60)),
            "each native Bell ray is normalized")

    # The output frame w_l=F conjugate(v_l) and the POVM M_l=|w_l><w_l|/6.
    W = F*V.conjugate()
    projector_F = F*F.H
    require(sp.simplify(projector_F*projector_F-projector_F) == sp.zeros(50),
            "Pi_F is an orthogonal rank-ten projector")
    require(sp.simplify(W*W.H/6-projector_F) == sp.zeros(50),
            "sixty readout effects sum exactly to Pi_F")
    require(all(sp.simplify((W[:, ell].H*W[:, ell])[0]) == 1 for ell in range(60)),
            "all readout vectors w_l are normalized")

    # Applying the rank-one POVM bra <w_l|/sqrt(6) to Xi gives v_l/sqrt(60).
    # Hence every outcome has probability 1/60 and the normalized external
    # conditional ket is exactly v_l, without a root-current identification.
    for ell in range(60):
        amplitude = sp.simplify(W[:, ell].H*Xi)
        require(amplitude == V[:, ell].T/sp.sqrt(10),
                "conditional external amplitude is v_l over sqrt10")
        probability = sp.simplify((amplitude*amplitude.H)[0]/6)
        require(probability == sp.Rational(1, 60), "uniform readout probability one over60")

    # Exact all-60 intertwining.  If q=4T is the action in the unnormalized
    # quartic basis, Rhat_AB=sqrt(n_A/n_B) q_AB/4.  Multiplication by 96
    # removes every square root from (Rhat tensor U)F=F conjugate(U):
    # sum_B (24 n_A/n_B) q_AB U K_B = 96 K_A conjugate(U).
    intertwiner_cells = 0
    ray_covariance_cells = 0
    q_actions = []
    ray_permutations = []
    for ell, (r, U) in enumerate(zip(reflections, bell_actions)):
        action = tensor_power(2*r, 4)@quartics
        scaled = (24//norms)[:, None]*(quartics.T@action)
        require(np.array_equal(scaled.imag, np.zeros_like(scaled.imag)) and
                np.array_equal(scaled.real, np.rint(scaled.real)), "exact quartic action")
        scaled = scaled.real.astype(np.int64)
        require(np.all(scaled % 96 == 0), "quartic action has quarter entries")
        q = scaled//96
        q_actions.append(q.tolist())
        require(np.array_equal(q.T@np.diag(norms)@q, 16*np.diag(norms)),
                "normalized W5 action is orthogonal")
        for A in range(5):
            lhs = sum(((24*int(norms[A])//int(norms[B]))*int(q[A, B])*(U@k_numpy[B])
                       for B in range(5)), np.zeros((10,10), dtype=complex))
            rhs = 96*k_numpy[A]@U.conj()
            require(np.array_equal(lhs, rhs), "exact readout intertwiner block")
            intertwiner_cells += 100

        permutation = []
        for j, z in enumerate(rays):
            target, phase = source.phase_match(r@z, rays, 1)
            require(np.array_equal(U@v_numpy[j], (phase**2)*v_numpy[target]),
                    "native Bell-ray covariance")
            permutation.append(target)
            ray_covariance_cells += 10
        require(len(set(permutation)) == 60, "native readout labels permuted")
        ray_permutations.append(permutation)

    result = {
        "research_id": "UR.COMPILER.GRADE2.NATIVE60.READOUT.INTERTWINER.20260919",
        "verdict": "EXACT_READOUT_INTERTWINER_POVM_SELECTION_OPEN",
        "input_sha256": {str(path): digest for path, digest in PINS.items()},
        "quartic_norms": norms.tolist(),
        "K_matrices": [matrix.tolist() for matrix in k_numpy],
        "Xi_norm_squared": "1",
        "Bell_marginals": "I10/10 on both Bell factors",
        "F": "F_(A i),j=sqrt(2/n_A) K_Aij; F^*F=I10",
        "intertwining": "(Rhat_r tensor U_r) F = F conjugate(U_r) for all60 native reflections",
        "intertwiner_scalar_cells_checked": intertwiner_cells,
        "native_frame": "sum_l |v_l><v_l|=6 I10",
        "POVM": "M_l=|F conjugate(v_l)><F conjugate(v_l)|/6; sum_l M_l=Pi_F",
        "outcome_on_Xi": "p_l=1/60 and normalized external conditional ket v_l for every l",
        "ray_covariance_scalar_cells_checked": ray_covariance_cells,
        "q_equals_4T_actions": q_actions,
        "native_ray_permutations": ray_permutations,
        "scope": "exact finite grade-2 W5 tensor Bell10 realization only; POVM selection and implementation, preparation, old .17 dynamics, root-current ket identification, locality, continuum and TOE remain open",
        "checks": dict(sorted(checks.items())),
        "check_evaluations": sum(checks.values()),
    }
    (HERE/"readout_intertwiner_certificate.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "verdict", "quartic_norms", "Bell_marginals", "F", "intertwining",
        "native_frame", "POVM", "outcome_on_Xi", "check_evaluations")}, indent=2))


if __name__ == "__main__":
    main()
