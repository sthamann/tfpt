"""Gaussian source closure and a separately sourced electric/rotor exit edge."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/clock-neutral-access/checker.py": "6f60772c639e9eb19745e363010e8ed0e39ed9cb51b38ca7997f7baecdd48f50",
    "experiments/theory-contracts/local-window-round37/checker.py": "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    "verification/v988_psi_lambda_reduction.py": "eae02e79be5703ccec67f1f11470e3ffd99895b17575c9ce1d553720bd1752cd",
    "verification/v1033_charged_disorder.py": "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(index):
    for path, digest in PINS.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, "source pin: " + path)
    path = ROOT/list(PINS)[index]
    spec = importlib.util.spec_from_file_location("interaction_provenance_"+str(index), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sign(a, b):
    return (-1)**sum((b & ((1 << i)-1)).bit_count() for i in range(16) if (a >> i) & 1)


def quadratic_lie_record():
    m = load(0)
    j, b, data = m.source()
    basis = [sum(1 << i for i in pair) for pair in itertools.combinations(range(16), 2)]
    nonzero = 0
    for left, right in itertools.product(basis, repeat=2):
        coefficient = sign(left, right)-sign(right, left)
        if coefficient:
            require((left ^ right).bit_count() == 2, "every quadratic commutator remains quadratic")
            nonzero += 1
    require(nonzero == 3360, "complete 120-by-120 bracket census")
    require(j*b == b*j and sp.Matrix.hstack(j.reshape(256, 1), b.reshape(256, 1)).rank() == 2,
            "actual two-generator source Lie algebra is abelian and two-dimensional")
    return {"quadratic_basis_dimension": 120, "ordered_bracket_cells": 14400,
            "nonzero_quadratic_brackets": nonzero, "quartic_bracket_cells": 0,
            "original_J_B_Lie_dimension": 2, "source": data["provenance"]}


def grassmann_mul(left, right):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            if not a & b:
                out[a | b] = out.get(a | b, 0)+sign(a, b)*x*y
    return {mask: sp.expand(value) for mask, value in out.items() if sp.expand(value) != 0}


def grassmann_add(*ops):
    out = {}
    for weight, op in ops:
        for mask, value in op.items():
            out[mask] = out.get(mask, 0)+weight*value
    return {mask: sp.expand(value) for mask, value in out.items() if sp.expand(value) != 0}


def grassmann_elimination_record():
    m = load(0)
    j, b, _ = m.source()
    # Actual six-coordinate restriction; the general Schur proof is in README.
    matrix = (j+b/8)[:6, :6]
    q = {(1 << i) | (1 << k): matrix[i, k]
         for i in range(6) for k in range(i+1, 6) if matrix[i, k] != 0}
    term, exponential = {0: sp.Integer(1)}, {0: sp.Integer(1)}
    for degree in range(1, 4):
        term = grassmann_mul(term, q)
        exponential = grassmann_add((1, exponential), (1/sp.factorial(degree), term))
    # Integration convention: coefficient of eta_1 eta_2, placed last.
    eliminated = 3 << 4
    integral = {mask ^ eliminated: value for mask, value in exponential.items()
                if mask & eliminated == eliminated}
    require(integral.get(0, 0) == matrix[4, 5] != 0, "nonzero Pfaffian normalization")
    normalized = {mask: value/integral[0] for mask, value in integral.items()}
    y = grassmann_add((1, normalized), (-1, {0: 1}))
    logarithm = grassmann_add((1, y), (-sp.Rational(1, 2), grassmann_mul(y, y)))
    a, cross, fast = matrix[:4, :4], matrix[:4, 4:], matrix[4:, 4:]
    effective = a+cross*fast.inv()*cross.T
    expected = {(1 << i) | (1 << k): effective[i, k]
                for i in range(4) for k in range(i+1, 4) if effective[i, k] != 0}
    require(logarithm == expected, "exact Gaussian Schur exponent")
    require(normalized.get(15, 0) != 0 and logarithm.get(15, 0) == 0,
            "raw quartic weight is not a connected quartic generator")
    return {"source_coordinates": [0, 1, 2, 3, 4, 5], "integrated_coordinates": [4, 5],
            "normalized_raw_quartic_coefficient": str(normalized[15]),
            "normalized_log_quartic_coefficient": "0", "exact_Schur_exponent": True}


def clean_vector(vector):
    result = {key: sp.expand(value) for key, value in vector.items()}
    return {key: value for key, value in result.items() if value != 0}


def add_vectors(*weighted):
    result = {}
    for weight, vector in weighted:
        for key, value in vector.items():
            result[key] = result.get(key, 0)+weight*value
    return clean_vector(result)


def electric_exit_record():
    parent = load(1)
    parent.inherited(ROOT)  # Validate the real parent's transitive pins.
    data = parent.parent_terms([(0, 0, 0), (1, 0, 0)], [(0, 1)], ambient_degree=[6, 6])
    link_terms = [term for term in data["terms"] if term[0] < 2 and term[1] < 2]
    require(len(link_terms) == 2 and all(term[3] == parent.A for term in link_terms),
            "actual low-low Hermitian link pair, no invented coupling")
    a, kappa = sp.Rational(parent.A), sp.Rational(parent.KAPPA)
    e = sp.Symbol("E", integer=True)

    def hopping(vector, terms):
        result = {}
        for (mask, flux), amplitude in vector.items():
            for target, source, shifts, weight, _ in terms:
                moved = parent.move(mask, source, target)
                if moved is None:
                    continue
                shift = sum(s for _, s in shifts)
                key = moved[0], sp.expand(flux+shift)
                result[key] = result.get(key, 0)+amplitude*moved[1]*sp.Rational(weight)
        return clean_vector(result)

    def electric(vector):
        return clean_vector({(mask, flux): amplitude*kappa*flux**2/2
                             for (mask, flux), amplitude in vector.items()})

    def double(vector, terms):
        v = lambda x: hopping(x, terms)
        return add_vectors((2, v(electric(v(vector)))),
                           (-1, v(v(electric(vector)))), (-1, electric(v(v(vector)))))

    full_low_quartic = 0
    for mask in range(16):  # All four actual L0,L1,H0,H1 modes, every Fock mask.
        n_source, n_target = mask & 1, (mask >> 1) & 1
        expected = kappa*a*a*(n_source+n_target-2*n_source*n_target+2*e*(n_source-n_target))
        actual = double({(mask, e): 1}, link_terms)
        require(actual == clean_vector({(mask, e): expected}), "all-flux link double commutator")
        # Exact Hilbert-Schmidt projection of the FULL original edge hopping
        # double commutator onto q_L0 q_L1. Tr(q_L0 q_L1)^2=1 on 16 states.
        full = double({(mask, e): 1}, data["terms"])
        full_low_quartic += (n_source-sp.Rational(1, 2))*(n_target-sp.Rational(1, 2))*full.get((mask, e), 0)
    require(sp.expand(full_low_quartic) == -2*kappa*a*a,
            "quartic coefficient survives all other actual edge hopping terms")
    return {"actual_parent": list(PINS)[1], "original_modes": ["L0", "L1", "H0", "H1"],
            "Fock_masks": 16, "electric_flux": "arbitrary integer E; no cutoff",
            "a": str(a), "kappa": str(kappa),
            "link_formula": "kappa*a^2*(n0+n1-2*n0*n1+2*E*(n0-n1))",
            "full_edge_qL0_qL1_coefficient": str(-2*kappa*a*a),
            "quartic_term_is_generated_commutator_not_added_Hamiltonian": True,
            "mapping_to_sixteen_Clock_Majoranas_proved": False}


def fixed_algebra_record():
    m = load(0)
    d = m.build()
    permutation = d["source"]["img"]
    cube = [permutation[permutation[permutation[i]]] for i in range(16)]
    parity = m.scale(-2, d["q"]["d3"])
    require(m.mul(parity, parity) == {0: 1}, "unique grade3-mode parity")
    for i in range(16):
        gamma = {1 << i: sp.Integer(1)}
        require(m.mul(parity, m.mul(gamma, parity)) == m.clock(gamma, cube),
                "O cubed implemented by grade3 occupation parity on all original generators")
    # This witnesses a direction in the already classified 81D space, not a
    # selected source term. It complements, rather than replaces, provenance.
    zeta = (-1+sp.I*sp.sqrt(3))/2
    dark_minus = m.annihilator(sp.Matrix([1, sp.conjugate(zeta), zeta, 0, 0, 0, 0, 0])/sp.sqrt(3))
    transfer = m.mul(m.dagger(d["modes"]["b1"]), m.mul(m.dagger(d["modes"]["b2"]),
               m.mul(dark_minus, d["modes"]["d4"])))
    candidate = m.add(transfer, m.dagger(transfer))
    require(candidate and {mask.bit_count() for mask in candidate} == {4}, "class-space quartic witness")
    require(m.clock(candidate, permutation) == candidate, "full O preserved by pair-transfer direction")
    require(not m.comm(m.quadratic(d["j"]), candidate), "N preserved by pair-transfer direction")
    require(not m.comm(m.quadratic(d["b"]), candidate), "exact bare pair resonance")
    require(m.comm(d["q"]["d4"], candidate), "not every invariant quartic is occupation diagonal")
    require(not m.comm(d["q"]["d3"], candidate), "O-fixed central grade3 occupation retained")
    return {"O_cubed_equals_grade3_parity_on_all_16_generators": True,
            "grade3_occupation_central_in_O_fixed_algebra": True,
            "all_81_quartics_QND": False, "explicit_pair_transfer_direction": True,
            "generic_non_QND_means_complement_of_proper_linear_kernel_only": True,
            "generic_full_O_fixed_algebra_generated_proved": False,
            "pair_transfer_added_to_original_source": False}


def record():
    return {"quadratic_closure": quadratic_lie_record(),
            "Gaussian_elimination": grassmann_elimination_record(),
            "existing_noncentral_coefficient_exit": electric_exit_record(),
            "invariant_class_scope": fixed_algebra_record(),
            "pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": {"original_16_Majorana_quartic_dynamical_source_found": False,
                      "separate_rotor_parent_nonGaussian_edge_found": True,
                      "rotor_Clock_dictionary_derived": False,
                      "TOE_or_RH_proved": False, "T1_T8_closed": []}}


if __name__ == "__main__":
    print(json.dumps(record(), sort_keys=True, indent=2))
