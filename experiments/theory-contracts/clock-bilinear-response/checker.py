"""Exact primitive Clock operators and state-dependent response of the frozen source.

The CAR lift and grandcanonical Gibbs choice are explicit. No TFPT selection,
continuum, RH or identification of E8 sign states with Majorana coordinates.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INPUT = ROOT / "experiments/theory-contracts/compiler-involution-types/checker.py"
PIN = "9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def source():
    require(hashlib.sha256(INPUT.read_bytes()).hexdigest() == PIN, "source adapter pin")
    spec = importlib.util.spec_from_file_location("bilinear_frozen_source", INPUT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = module.exact_source_prefix()
    a, b = sp.Matrix(data["A16_dep"]), sp.Matrix(data["A_int"])
    o = sp.zeros(16)
    for i, j in enumerate(data["img"]):
        o[j, i] = 1
    return a, b, o, data["provenance"]


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def number_hamiltonian(u, t, b):
    """Fock c^* h c matrix; transpose acts on gamma(v) coefficients."""
    real, imag = b[::2, ::2], b[::2, 1::2]
    return u*sp.eye(8)+t*(imag+sp.I*real)


def vectors():
    eta = (-1 - sp.I*sp.sqrt(3))/2  # Clock grade 4.
    f3 = sp.Matrix([0, 0, 0, 1, -1, 0, 0, 0])/sp.sqrt(2)
    f4 = sp.Matrix([1, eta, sp.expand(eta**2), 0, 0, 0, 0, 0])/sp.sqrt(3)
    v3, v4 = {}, {}
    for sign in (1, -1):
        internal = sp.Matrix([1, sp.I*sign])/sp.sqrt(2)
        v3[sign] = sp.kronecker_product(f3, internal)
        v4[sign] = sp.kronecker_product(f4, internal)
    return v3, v4


def exact_record():
    a, b, o, provenance = source()
    v3, v4 = vectors()
    u, t = sp.symbols("u t", real=True)
    d = u*a + t*b
    omega = (1 + sp.I*sp.sqrt(3))/2
    p3 = sp.diag(*([1]*6 + [0]*10))
    p2 = sp.diag(*([0]*6 + [1]*4 + [0]*6))
    pb = sp.eye(16) - p3 - p2
    require(a*b == b*a and o*b == b*o, "original commuting symmetries")
    pi0 = sum((o**k for k in range(6)), sp.zeros(16))/6
    krylov = sp.Matrix.hstack(*[(b**k)[:, 10:] for k in range(5)])
    require(pi0.rank() == krylov.rank() == 10 and pi0*krylov == krylov,
            "boundary-generated fixed coordinate space")
    rows = []
    for s in (1, -1):
        for r in (1, -1):
            v, w = v3[s], v4[r]
            l3, l4 = s*(u-t), r*u - sp.sqrt(3)*t
            total = sp.expand(l3 + l4)
            wedge = v*w.T - w*v.T
            require(clean(d*v - sp.I*l3*v) == sp.zeros(16, 1), "grade 3 eigenmode")
            require(clean(d*w - sp.I*l4*w) == sp.zeros(16, 1), "grade 4 eigenmode")
            require(clean(o*wedge*o.T - omega*wedge) == sp.zeros(16), "primitive Clock grade")
            require(clean(d*wedge + wedge*d.T - sp.I*total*wedge) == sp.zeros(16), "sum frequency")
            require(clean(v.conjugate().T*v)[0] == 1 and clean(w.conjugate().T*w)[0] == 1,
                    "normalized coordinate vectors")
            require(clean(v.T*v)[0] == 0 and clean(w.T*w)[0] == 0 and clean(v.T*w)[0] == 0,
                    "canonical independent isotropic modes")
            require(wedge*pb == pb*wedge == sp.zeros(16), "no boundary support")
            require(clean(pi0*wedge) == clean(wedge*pi0) == sp.zeros(16),
                    "commutes with full generated boundary CAR algebra")
            rows.append({"s": s, "r": r, "lambda3": str(l3), "lambda4": str(l4),
                         "Omega": str(total), "number_commutator": -(s+r),
                         "N3_commutator": -r, "N2_commutator": -s,
                         "clock_grade": 1, "parity_even": True})
    # In the A0 complex structure, this is the ORIGINAL number-conserving h8.
    h8 = number_hamiltonian(1, sp.Rational(1, 8), b)
    minors = [sp.factor(h8[:k, :k].det()) for k in range(1, 9)]
    require(h8 == h8.conjugate().T and all(x > 0 for x in minors), "source-point vacuum certificate")
    ratio = sp.simplify((sp.sqrt(3)+1)/(sp.sqrt(3)-1))
    require(ratio == 2+sp.sqrt(3), "exact ratio")
    return {
        "source": provenance, "rows": rows,
        "source_point_u1_t_one_eighth_h8_leading_minors": [str(x) for x in minors],
        "marker_commutator_ranks": [int((b*p-p*b).rank()) for p in (p3, p2, pb)],
        "boundary_generated_coordinate_dimension_for_nonzero_t": 10,
        "full_complex_CAR_boundary_relative_commutant_dimension": 64,
        "slow_frequency_ratio": str(ratio),
        "scope": {"actual_finite_bilinear_dynamics_derived": True,
                  "original_source_point_slow_vacuum_response": False,
                  "grandcanonical_Gibbs_preparation_TFPT_selected": False,
                  "crossing_parameter_window_TFPT_selected": False,
                  "separate_marker_numbers_original_symmetries": False,
                  "E8_charged_field_dictionary_derived": False,
                  "primitive_bilinear_reachable_by_existing_boundary_algebra": False,
                  "physical_hyperbolic_or_prime_dynamics_from_ratio": False,
                  "T1_T8_closed": [], "RH_proved": False},
    }


def fermi(beta, energy):
    require(beta >= 0 and math.isfinite(energy), "finite energy and nonnegative beta")
    x = beta*energy
    if x >= 0:
        y = math.exp(-x)
        return y/(1+y)
    return 1/(1+math.exp(x))


def response(u, t, beta, s, r):
    require(s in (-1, 1) and r in (-1, 1), "internal signs")
    l3, l4 = s*(u-t), r*u-math.sqrt(3)*t
    freq = l3+l4
    weight = fermi(beta, l3)*fermi(beta, l4)
    reverse = fermi(beta, -l3)*fermi(beta, -l4)
    return {"s": s, "r": r, "frequency": freq, "weight": weight,
            "reverse_weight": reverse, "commutator_norm_squared": freq*freq*weight}


def jordan_wigner(modes=8):
    """Independent sparse CAR representation, with 2^8 states, not 16 states."""
    size = 2**modes
    annihilators = []
    for mode in range(modes):
        rows, cols, signs = [], [], []
        for state in range(size):
            if (state >> mode) & 1:
                rows.append(state ^ (1 << mode))
                cols.append(state)
                signs.append((-1)**((state & ((1 << mode)-1)).bit_count()))
        annihilators.append(sparse.csr_matrix((signs, (rows, cols)), shape=(size, size), dtype=complex))
    gamma = []
    for op in annihilators:
        gamma.extend([op+op.conjugate().T, -1j*(op-op.conjugate().T)])
    return annihilators, gamma


def full_fock(u=1.0, t=0.125, betas=(0.0, 1.0, 8.0)):
    a, b, _, _ = source()
    d = np.asarray(u*a+t*b, dtype=complex)
    annihilators, gamma = jordan_wigner()
    size = gamma[0].shape[0]
    h = sparse.csr_matrix((size, size), dtype=complex)
    for i in range(16):
        for j in range(i+1, 16):
            if d[i, j] != 0:
                h += (0.5j*d[i, j])*(gamma[i]@gamma[j])
    h = h.toarray()
    require(np.linalg.norm(h-h.conj().T) < 1e-12, "Hermitian CAR lift")
    single = [1 << k for k in range(8)]
    one_particle = h[np.ix_(single, single)]-h[0, 0]*np.eye(8)
    expected_h8 = np.asarray(number_hamiltonian(u, t, b), dtype=complex)
    h8_residual = float(np.max(abs(one_particle-expected_h8)))
    transpose_residual = float(np.max(abs(one_particle-expected_h8.T)))
    require(h8_residual < 1e-12, "Fock one-particle block, not coefficient transpose")
    energy, basis = np.linalg.eigh(h)
    number = sum((c.conjugate().T@c for c in annihilators), sparse.csr_matrix((size, size), dtype=complex)).toarray()
    v3, v4 = vectors()
    rows = []
    for s in (1, -1):
        for r in (1, -1):
            factors = []
            for vector in (v3[s], v4[r]):
                coeffs = np.asarray(vector, dtype=complex).ravel()/math.sqrt(2)
                factors.append(sum((coeffs[i]*gamma[i] for i in range(16)),
                                   sparse.csr_matrix((size, size), dtype=complex)))
            op = (factors[0]@factors[1]).toarray()
            expected = response(u, t, 0, s, r)
            freq = expected["frequency"]
            comm = h@op-op@h
            residual = float(np.linalg.norm(comm+freq*op))
            number_residual = float(np.linalg.norm(number@op-op@number+(s+r)*op))
            ob = basis.conj().T@op@basis
            kb = basis.conj().T@comm@basis
            # Column norms give the diagonal of A^*A without a covariance formula.
            normcols = np.sum(abs(ob)**2, axis=0)
            commcols = np.sum(abs(kb)**2, axis=0)
            for beta in betas:
                weights = np.exp(-beta*(energy-energy[0]))
                weights /= weights.sum()
                observed = float(weights@normcols)
                observed_comm = float(weights@commcols)
                exact = response(u, t, beta, s, r)
                rows.append({"u": u, "t": t, "beta": beta, "s": s, "r": r,
                             "observed_weight": observed, "formula_weight": exact["weight"],
                             "weight_error": abs(observed-exact["weight"]),
                             "commutator_error": abs(observed_comm-exact["commutator_norm_squared"]),
                             "operator_commutator_residual": residual,
                             "number_commutator_residual": number_residual})
    return {"fock_dimension": size, "rows": rows,
            "one_particle_block_residual": h8_residual,
            "wrong_coefficient_transpose_residual": transpose_residual,
            "number_conservation_residual": float(np.linalg.norm(h@number-number@h)),
            "ground_energy": float(energy[0]),
            "max_weight_error": max(x["weight_error"] for x in rows),
            "max_commutator_error": max(x["commutator_error"] for x in rows)}


def record(with_fock=False):
    result = exact_record()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["thermal_source_point"] = [{"beta": beta, **response(1, 1/8, beta, s, r)}
                                      for beta in (0, 1, 8, 64) for s in (1, -1) for r in (1, -1)]
    if with_fock:
        result["independent_full_Fock"] = [full_fock(), full_fock(3/16, 1/8, (1.0, 64.0))]
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fock", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(record(args.fock), indent=2)+"\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
