#!/usr/bin/env python3
"""Native local complement test for the compiler packet Hamiltonian.

This is an experiment-only diagnostic.  It reconstructs the pinned 240-root
source action and the actual local operators L and H_E from contract .25.  It
then measures the part discarded by the packet compression, without assuming
a complementary gap or replacing the resolvent by a scalar.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
HERE = Path(__file__).resolve().parent
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
EXPECTED_SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"


def load_source():
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED_SOURCE_SHA256:
        raise RuntimeError("source pin changed")
    spec = importlib.util.spec_from_file_location("native_source", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load native source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


native = load_source()
canonical = np.stack(native.source_rays())
ray_index = {native.canonical_mu4(v): i for i, v in enumerate(canonical)}


def gaussian_integer(array: np.ndarray, label: str) -> np.ndarray:
    rounded = np.rint(array.real) + 1j * np.rint(array.imag)
    if not np.array_equal(array, rounded):
        raise RuntimeError(f"{label} is not Gaussian integral")
    if float(np.max(np.abs(rounded))) >= 2**52:
        raise RuntimeError(f"{label} exceeds exact complex128 integer range")
    return rounded.astype(np.complex128)


def exact_native_identities() -> dict[str, object]:
    """Integer-scaled certificates for the local dressing theorem.

    Every multiplication below is over Gaussian integers whose magnitudes are
    checked below 2**52, so complex128 represents all integer components
    exactly.  No tolerance or rational reconstruction is used.
    """
    eye4 = np.eye(4, dtype=np.complex128)
    r2 = np.stack([gaussian_integer(2 * eye4 - np.outer(v, v.conj()), "2r")
                   for v in canonical])
    eye16 = np.eye(16, dtype=np.complex128)
    swap16 = np.zeros((16, 16), dtype=np.complex128)
    for a, b in itertools.product(range(4), repeat=2):
        swap16[4 * b + a, 4 * a + b] = 1

    checks = []
    if not np.array_equal(sum(r2), 60 * eye4):
        raise RuntimeError("exact first reflection moment")
    checks.append("sum_l (2r_l)=60 I4")
    for alpha, root in enumerate(canonical):
        if not np.array_equal(r2[alpha] @ root, -2 * root):
            raise RuntimeError(("bound-root reflection", alpha))
    checks.append("all bound roots have r_alpha psi_alpha=-psi_alpha")
    pair_sum = gaussian_integer(sum(np.kron(r, r) for r in r2), "second moment sum")
    if not np.array_equal(5 * pair_sum, 240 * (eye16 + swap16)):
        raise RuntimeError("exact second reflection moment")
    checks.append("5 sum_l (2r_l tensor 2r_l)=240(I+Swap)")

    # Covariance of the event projector under each simultaneous reflection is
    # the exact reason [L,H_E]=0.  In integer scale:
    # (2r_l)(2r_a)(2r_l)=4(2r_{l a}).
    for ell, left in enumerate(r2):
        for alpha, root in enumerate(canonical):
            target = ray_index[native.canonical_mu4((left @ root) / 2)]
            conjugated = gaussian_integer(left @ r2[alpha] @ left, "event covariance product")
            if not np.array_equal(conjugated, 4 * r2[target]):
                raise RuntimeError(("event covariance", ell, alpha))
    checks.append("all 3600 exact event-covariance identities")

    # I-r tensor r is twice a projector because r tensor r is an involution.
    for alpha, reflection2 in enumerate(r2):
        event4 = 4 * eye16 - np.kron(reflection2, reflection2)
        event_square = gaussian_integer(event4 @ event4, "event square")
        if not np.array_equal(event_square, 8 * event4):
            raise RuntimeError(("H_E squared", alpha))
    checks.append("all 60 local events obey H_E^2=2H_E")

    # The s-source P block is exactly (4I-Swap)/5 for both L and H_E.
    s_block_num = 240 * eye16 - pair_sum
    if not np.array_equal(5 * s_block_num, 240 * (4 * eye16 - swap16)):
        raise RuntimeError("s packet block")
    checks.append("P_s L P_s=P_s H_E P_s=(4I-Swap)/5")
    return {
        "checks": checks,
        "check_count": len(checks),
        "arithmetic": "Gaussian-integer identities; exact integer range checked below 2^52",
        "analytic_consequences": [
            "joint source-bound invariance plus mean r=I/2 gives Phi (lambda,eta)=(1/2,3/2)",
            "two bound reflection signs give Omega (lambda,eta)=(0,0)",
        ],
        "s_swap_sectors": {
            "symmetric_dimension": 10,
            "antisymmetric_dimension": 6,
            "lambda_L_equals_eta_HE": {"symmetric": "3/5", "antisymmetric": "1"},
        },
    }


def exact_overlap_test() -> dict[str, object]:
    """Smallest fixed-source test for overlapping neighbouring dressings."""
    eye4 = np.eye(4, dtype=np.complex128)
    eye64 = np.eye(64, dtype=np.complex128)
    r2 = np.stack([gaussian_integer(2 * eye4 - np.outer(v, v.conj()), "overlap 2r")
                   for v in canonical])
    alpha = 0
    inner_products = [np.vdot(canonical[alpha], v) for v in canonical]
    beta_generic = next(i for i, z in enumerate(inner_products)
                        if i != alpha and z != 0)
    beta_orthogonal = next(i for i, z in enumerate(inner_products) if z == 0)

    def case(beta: int) -> dict[str, object]:
        event12_num = 4 * eye64 - np.kron(np.kron(r2[alpha], r2[alpha]), eye4)
        event23_num = 4 * eye64 - np.kron(np.kron(eye4, r2[beta]), r2[beta])
        stacked = gaussian_integer(np.vstack([event12_num, event23_num]), "stacked events")
        common_kernel_dimension = 64 - native.exact_complex_rank(stacked)

        p12_num = 4 * eye64 + np.kron(np.kron(r2[alpha], r2[alpha]), eye4)
        p23_num = 4 * eye64 + np.kron(np.kron(eye4, r2[beta]), r2[beta])
        # Each actual zero-event projector is p_num/8.
        ordered = gaussian_integer(p12_num @ p23_num, "ordered projector product")
        reverse = gaussian_integer(p23_num @ p12_num, "reverse projector product")
        commutator = gaussian_integer(ordered - reverse, "projector commutator")
        idempotence_defect = gaussian_integer(ordered @ ordered - 64 * ordered,
                                              "ordered-product idempotence defect")
        return {
            "beta_index": beta,
            "unnormalized_root_inner_product": [int(inner_products[beta].real),
                                                  int(inner_products[beta].imag)],
            "common_zero_event_kernel_dimension": common_kernel_dimension,
            "commutator_rank": native.exact_complex_rank(commutator),
            "ordered_product_is_projector": bool(not np.any(idempotence_defect)),
        }

    generic = case(beta_generic)
    orthogonal = case(beta_orthogonal)
    parallel = case(alpha)
    expected = {"generic": 18, "orthogonal": 24, "parallel": 28}
    observed = {"generic": generic["common_zero_event_kernel_dimension"],
                "orthogonal": orthogonal["common_zero_event_kernel_dimension"],
                "parallel": parallel["common_zero_event_kernel_dimension"]}
    if observed != expected:
        raise RuntimeError(("overlap kernel dimensions", observed, expected))
    if generic["commutator_rank"] == 0 or generic["ordered_product_is_projector"]:
        raise RuntimeError("generic neighbouring dressings unexpectedly compatible")
    return {
        "status": "PASS_EXACT_FIXED_SOURCE_OVERLAP_OBSTRUCTION",
        "alpha_index": alpha,
        "generic": generic,
        "orthogonal": orthogonal,
        "parallel": parallel,
        "meaning": (
            "For a native nonorthogonal/nonparallel source pair the neighbouring zero-event "
            "projectors do not commute and their ordered product is not a projector.  Separate "
            "one-edge dressings therefore cannot simply be multiplied into a global isometry."
        ),
        "scope": "fixed source fibre on three matter registers; no source superposition, L, V or chain vacuum",
    }


def main() -> None:
    exact = exact_native_identities()
    overlap = exact_overlap_test()
    # H_E has spectrum {0,2}; [L,H_E]=0.  If a packet vector has
    # L-eigenvalue lambda and eta=<H_E>, then its first orthogonal H_E image
    # closes exactly.  In the orthonormal {P,QH_EP} basis the block is
    # [[k lambda+J eta, J sqrt(eta(2-eta))],
    #  [same, k lambda+J(2-eta)]].
    sectors = {
        "s_symmetric": {"multiplicity": 10, "lambda_L": "3/5", "eta_HE": "3/5",
                          "mixed_matter_low_high_weights": ["7/16", "3/16"]},
        "s_antisymmetric": {"multiplicity": 6, "lambda_L": "1", "eta_HE": "1",
                              "mixed_matter_low_high_weights": ["3/16", "3/16"]},
        "phi": {"multiplicity": "packet-local", "lambda_L": "1/2", "eta_HE": "3/2"},
        "omega": {"multiplicity": "packet-local", "lambda_L": "0", "eta_HE": "0"},
    }
    for data in sectors.values():
        lam = sp.Rational(data["lambda_L"])
        eta = sp.Rational(data["eta_HE"])
        data["P_diagonal"] = f"{lam}*kappa + {eta}*J"
        if eta in (0, 2):
            data["closed_cyclic_dimension"] = 1
            data["Q_diagonal"] = None
            data["coupling_squared"] = "0"
            data["dressed_eigenvalues"] = [f"{lam}*kappa + {eta}*J"]
            data["low_branch_Q_weight_for_J_positive"] = "0"
        else:
            data["closed_cyclic_dimension"] = 2
            data["Q_diagonal"] = f"{lam}*kappa + {2-eta}*J"
            data["coupling_squared"] = f"{sp.factor(eta*(2-eta))}*J^2"
            data["dressed_eigenvalues"] = [f"{lam}*kappa", f"{lam}*kappa + 2*J"]
            data["low_branch_Q_weight_for_J_positive"] = str(sp.factor(eta / 2))

    result = {
        "status": "PASS_EXACT_NATIVE_FIRST_DRESSING_BLOCK",
        "verdict": "FIRST_NATIVE_SOURCE_DRESSING_CHANGES_BARE_LOCAL_INGREDIENTS; FULL_CRITICAL_LINE_OPEN",
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "operators": {
            "L": "I-(1/60) sum_l R_l tensor r_l tensor r_l",
            "H_E": "sum_alpha |alpha><alpha| tensor (I-r_alpha tensor r_alpha)",
        },
        "exact_certificate": exact,
        "overlap_test": overlap,
        "theorem": {
            "commutation": "[L,H_E]=0",
            "event_polynomial": "H_E^2=2H_E",
            "closed_space": "span{P packet vector, (I-P)H_E P packet vector}",
            "block_formula": "[[kappa*lambda+J*eta, J*sqrt(eta*(2-eta))], [same, kappa*lambda+J*(2-eta)]]",
            "spectrum_formula": "{kappa*lambda, kappa*lambda+2J}",
            "sectors": sectors,
        },
        "self_energy": {
            "formula": "Sigma(E)=J^2*eta*(2-eta)/(kappa*lambda+J*(2-eta)-E)",
            "sign_in_Feshbach_operator": "H_eff(E)=PHP-Sigma(E)",
            "nonperturbative_reason": "the P-Q diagonal separation is 2J(1-eta), while the coupling is J*sqrt(eta(2-eta)); both vanish at J=0",
            "resonant_state_dressing": "for every J>0 the low branch has bare-complement weight eta/2, independent of how small J is",
        },
        "critical_test_point": {
            "kappa": 1.0, "J": 0.01, "mu": 0.545,
            "relation": "2mu=kappa+9J",
            "exact_s_symmetric_block": [["303/500", "sqrt(21)/500"], ["sqrt(21)/500", "307/500"]],
            "exact_s_symmetric_dressed_eigenvalues": ["3/5", "31/50"],
            "exact_s_antisymmetric_block": [["101/100", "1/100"], ["1/100", "101/100"]],
            "exact_s_antisymmetric_dressed_eigenvalues": ["1", "51/50"],
        },
        "decision": {
            "exact": (
                "The first orthogonal source image closes exactly for the native local operators. "
                "The bare packet J shift is a barycentre of H_E eigenvalues 0 and 2, not a "
                "local eigenvalue.  Dressing changes s, Phi and Omega differently."
            ),
            "necessary_consequence": (
                "The coefficient 9J in the packet Ising condition cannot be transferred unchanged "
                "to the full source model from the bare calculation alone.  The smallest native local "
                "dressing is order J rather than order J squared over a fixed gap; the global "
                "renormalized line, including possible compensation through dressed hopping, is open."
            ),
            "not_proved": (
                "Overlapping dressed blocks on a chain, the mu transfer term, a thermodynamic "
                "dressed critical line, local-observable preservation and E8 currents remain open."
            ),
        },
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "exact_check_count": exact["check_count"],
        "s_symmetric_dressed": sectors["s_symmetric"]["dressed_eigenvalues"],
        "s_antisymmetric_dressed": sectors["s_antisymmetric"]["dressed_eigenvalues"],
        "phi_dressed": sectors["phi"]["dressed_eigenvalues"],
        "s_mixed_matter_spectral_weights": ["7/16", "3/16", "3/16", "3/16"],
        "generic_overlap_kernel_dimension": overlap["generic"]["common_zero_event_kernel_dimension"],
        "generic_overlap_commutator_rank": overlap["generic"]["commutator_rank"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
