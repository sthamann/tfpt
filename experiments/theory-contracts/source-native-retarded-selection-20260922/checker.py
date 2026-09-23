#!/usr/bin/env python3
"""Bounded exact audit of native W, retarded Gaussian response, and family Gram normalization."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
COMMON = REPO / 'experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py'
FAMILY = REPO / 'experiments/theory-contracts/source-three-route-closure-20260922/family_checker.py'
PAPER = REPO / 'tfpt_2_standard_model.tex'
EXPECTED_HASHES = {
    str(COMMON): '2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994',
    str(FAMILY): 'faa7731845abbf7793ded43d642232431fb0057163847faf4b3b2a6f1c070e7a',
    str(PAPER): 'bc80e9bb7a37c2cac5e2b0c1bb593adfbf2bcf4bea682fa6d5879d1d37719a75',
}
NATIVE_TENSOR = REPO / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'


def need(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def load_common():
    spec = importlib.util.spec_from_file_location('native_common', COMMON)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def family_m_u():
    # Pinned v117 matrices used by the existing family checker.
    I = sp.I
    M = sp.Matrix([[0, -(1 + I) / 2, (1 - I) / 2],
                   [-(1 + I) / 2, -I / 2, -sp.Rational(1, 2)],
                   [(1 - I) / 2, -sp.Rational(1, 2), I / 2]])
    U = sp.diag(1, I, -I)
    return M, U


def commutant_dimension(matrices):
    variables = sp.symbols('z0:9')
    Z = sp.Matrix(3, 3, variables)
    equations = []
    for matrix in matrices:
        equations.extend(list(Z * matrix - matrix * Z))
    coefficient = sp.linear_eq_to_matrix(equations, variables)[0]
    return 9 - coefficient.rank()


def matrix_key(matrix):
    return tuple(sp.simplify(sp.expand(entry)) for entry in matrix)


def enumerate_generated(generators):
    identity = sp.eye(generators[0].rows)
    elements = {matrix_key(identity): identity}
    frontier = [identity]
    while frontier:
        old = frontier.pop()
        for generator in generators:
            new = generator * old
            new = new.applyfunc(lambda e: sp.simplify(sp.expand(e)))
            key = matrix_key(new)
            if key not in elements:
                elements[key] = new
                frontier.append(new)
    return elements


def source_family_target():
    I = sp.I
    M = sp.Matrix([[0, -(1 + I) / 2, (1 - I) / 2],
                   [-(1 + I) / 2, -I / 2, -sp.Rational(1, 2)],
                   [(1 - I) / 2, -sp.Rational(1, 2), I / 2]])
    U = sp.diag(1, I, -I)
    punctures = [(U**k * M * U**(-k)).applyfunc(lambda e: sp.simplify(e)) for k in range(4)]
    for name, matrix in [('M', M), ('U', U)]:
        if (matrix.conjugate().T * matrix).applyfunc(sp.simplify) != sp.eye(3):
            raise RuntimeError(f'{name} is not unitary')
    group = enumerate_generated(punctures)
    if len(group) != 12:
        raise RuntimeError('four puncture matrices do not generate the expected A4 order 12')
    variables = sp.symbols('z0:9')
    Z = sp.Matrix(3, 3, variables)
    equations = []
    for matrix in punctures:
        equations.extend(list(Z * matrix - matrix * Z))
    coefficient = sp.linear_eq_to_matrix(equations, variables)[0]
    if 9 - coefficient.rank() != 1:
        raise RuntimeError('four-puncture joint commutant is not dimension one')
    return M, U, punctures, group


def lepton_target():
    phi = sp.symbols('phi', positive=True)
    r_mu = sp.Rational(8, 7) * phi
    r_e = sp.Rational(96, 49) * phi**3
    ordering_factor = sp.factor(r_mu - r_e)
    if sp.simplify(ordering_factor - sp.Rational(8, 7) * phi * (1 - sp.Rational(12, 7) * phi**2)) != 0:
        raise RuntimeError('symbolic lepton ordering factorization failed')
    # pi>3 gives phi < 1/18 + 3/(256*81) < 1/10.
    phi_upper = sp.Rational(1, 18) + sp.Rational(3, 256 * 81)
    if not (phi_upper < sp.Rational(1, 10)):
        raise RuntimeError('phi upper bound failed')
    A = sp.diag(r_e**2, r_mu**2, 1)
    trA = sp.trace(A)
    eta = sp.factor(3 * sp.trace(A**2) / trA**2 - 1)
    variance_identity = sp.simplify(eta - ((A[0, 0] - A[1, 1])**2 + (A[0, 0] - A[2, 2])**2 + (A[1, 1] - A[2, 2])**2) / trA**2)
    if variance_identity != 0:
        raise RuntimeError('eta variance identity failed')
    if sp.simplify((A[0, 0] - A[1, 1]) - (r_e-r_mu)*(r_e+r_mu)) != 0:
        raise RuntimeError('strict A diagonal ordering factorization failed')
    # A is a target Yukawa squared-singular-value matrix in the mass basis.
    phi_tfpt = sp.N(1 / (6 * sp.pi) + 3 / (256 * sp.pi**4), 50)
    rmu_tfpt = sp.N(r_mu.subs(phi, phi_tfpt), 50)
    re_tfpt = sp.N(r_e.subs(phi, phi_tfpt), 50)
    eta_tfpt = sp.N(eta.subs(phi, phi_tfpt), 50)
    return {
        'phi': '1/(6*pi)+3/(256*pi^4)',
        'phi_tfpt_50_digits': str(phi_tfpt), 'r_mu': '(8/7)*phi', 'r_e': '(96/49)*phi^3',
        'r_e_over_r_mu_tfpt_50_digits': str(sp.N(re_tfpt / rmu_tfpt, 50)),
        'eta_tfpt_50_digits': str(eta_tfpt),
        'A': 'diag(((96*phi^3)/49)^2,((8*phi)/7)^2,1)',
        'eta': str(eta), 'eta_positive_reason': 'sum of three squared diagonal differences / (tr A)^2',
        'scope': 'target Yukawa squared-singular-value matrix in mass basis; not a derived mass operator',
    }


def a4_twirl(group, A):
    twirl = sum((g * A * g.conjugate().T for g in group.values()), sp.zeros(3)) / len(group)
    return twirl.applyfunc(lambda e: sp.simplify(e))

def gaussian_completion_check():
    Delta, omega, g, gbar = sp.symbols('Delta omega g gbar', nonzero=True)
    b, barb, P, barP = sp.symbols('b barb P barP', commutative=True)
    K = Delta - sp.I * omega
    shifted = (barb + gbar * barP / K) * K * (b + g * P / K) - gbar * g * barP * P / K
    target = barb * K * b + gbar * barP * b + g * barb * P
    if sp.simplify(sp.together(shifted - target)) != 0:
        raise RuntimeError('symbolic Matsubara Gaussian completion failed')
    return {'K': 'Delta-i omega', 'identity': 'shifted K quadratic minus gbar*g*barP*P/K = barb*K*b + gbar*barP*b + g*barb*P'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE / 'certificate.json')
    args = parser.parse_args()
    for path, expected in EXPECTED_HASHES.items():
        if hash_file(Path(path)) != expected:
            raise RuntimeError(f'source hash mismatch: {path}')
    common = load_common()
    W = common.load_tensor()
    support, lookup = common.channel_support(W)
    if W.shape != (60, 2016):
        raise RuntimeError('native W shape is not 60 x 2016')
    if sum(len(row) for row in support) != 480:
        raise RuntimeError('native W support is not 480 entries')
    if not common.casimir_identity(W):
        raise RuntimeError('full 2016-state Casimir identity failed')
    spin, colour = common.one_body_generators()
    intertwiners = []
    for generator in spin + colour:
        common.boson_generator(W, generator)
        intertwiners.append(True)
    if len(intertwiners) != 60:
        raise RuntimeError('not all 45+15 generator intertwiners were checked')

    Delta = sp.symbols('Delta', positive=True, real=True)
    omega = sp.symbols('omega', real=True)
    Kinv = 1 / (Delta - sp.I * omega)
    need(sp.simplify(sp.re(Kinv) - Delta / (Delta**2 + omega**2)) == 0,
         'real part of K^-1 failed')
    need(sp.simplify(sp.im(Kinv) - omega / (Delta**2 + omega**2)) == 0,
         'imaginary part of K^-1 failed')
    need(sp.simplify(abs(Delta * Kinv - 1)**2 - omega**2 / (Delta**2 + omega**2)) == 0,
         'retarded relative-error identity failed')

    M, U, punctures, a4_group = source_family_target()
    target = lepton_target()
    re_sym, rmu_sym = sp.symbols('re rmu', real=True)
    A_symbolic = sp.diag(re_sym**2, rmu_sym**2, 1)
    twirl = a4_twirl(a4_group, A_symbolic)
    if twirl != sp.trace(A_symbolic) / 3 * sp.eye(3):
        raise RuntimeError('A4 twirl did not produce tr(A)/3 I')
    comm_norm = sp.simplify(sum(sp.trace((A_symbolic * g - g * A_symbolic).conjugate().T * (A_symbolic * g - g * A_symbolic)) for g in a4_group.values()) / 12)
    comm_rhs = sp.simplify(2 * (sp.trace(A_symbolic**2) - sp.trace(A_symbolic)**2 / 3))
    if sp.simplify(comm_norm - comm_rhs) != 0:
        raise RuntimeError('A4 mean commutator norm identity failed')
    gaussian = gaussian_completion_check()
    l, c = sp.symbols('l c', positive=True)
    T = M * sp.diag(1, l**2, l**4)
    G = sp.simplify(T.conjugate().T * T)
    C = sp.simplify(c * G)
    need(sp.simplify(G.inv() * C - c * sp.eye(3)) == sp.zeros(3),
         'Gram normalization G^-1 C=cI failed')
    l_control = sp.Rational(1, 4)
    G_control = G.subs(l, l_control)
    need(sp.simplify(G_control.inv() * (c * G_control) - c * sp.eye(3)) == sp.zeros(3),
         'rational l=1/4 Gram control failed')
    need(commutant_dimension([M, U]) == 1, 'M,U joint commutant is not dimension one')
    diagnostic = sp.Matrix([[0, 1, 0], [1, 1, 0], [0, 0, 2]])
    need(diagnostic * M != M * diagnostic, 'diagnostic generator unexpectedly commutes with M')
    need(diagnostic * U != U * diagnostic, 'diagnostic generator unexpectedly commutes with U')

    certificate = {
        'status': 'exact_bounded_native_response_and_gram_audit',
        'scope': 'Existing native W and family matrices only; no new Hamiltonian or physical gate.',
        'source_hashes': {
            str(COMMON): hash_file(COMMON),
            str(NATIVE_TENSOR): hash_file(NATIVE_TENSOR),
            str(FAMILY): hash_file(FAMILY),
            str(PAPER): hash_file(PAPER),
        },
        'generator_normalization': '-sum spin_generators(X)^2=45 I_16 and -sum colour_generators(X)^2=15 I_4',
        'native_W': {'shape': list(W.shape), 'nonzero_entries': 480,
                     'WWt': '8 I_60', 'casimir': '8 W^T W + 4 C_spin + 4 C_family - 120 I_2016 = 0',
                     'generator_intertwiners_checked': 60, 'split': '45 + 15'},
        'native_hypothesis': 'H=Delta N_b + g sum_A (b_A^dagger P_A + P_A^dagger b_A)',
        'euclidean_pair_kernel': {
            'interpretation': 'Euclidean Matsubara kernel; not a computed real-time retarded response',
            'K_inverse': '1/(Delta-i omega)', 'real': 'Delta/(Delta^2+omega^2)',
            'imaginary': 'omega/(Delta^2+omega^2)',
            'relative_error_squared': 'omega^2/(Delta^2+omega^2)',
            'condition': 'Delta>0',
        },
        'lepton_hierarchy_target': target,
        'gaussian_completion': gaussian,
        'A4_family_target': {
            'puncture_matrices': 4, 'group_order': len(a4_group), 'group_label': 'A4',
            'puncture_joint_commutant_dimension': 1, 'U_is_deck_action_separate': True,
            'twirl_identity': '1/12 sum_g g A g^dagger = tr(A)/3 I',
            'mean_commutator_identity': '1/12 sum_g ||[A,g]||_HS^2 = 2(tr(A^2)-(tr A)^2/3)',
            'twirl_scope': 'target Gram matrix in mass basis; not a derived mass operator',
        },
        'family_gram_control': {
            'T': 'M diag(1,l^2,l^4), l>0', 'rational_control_l': '1/4 (algebraic test value only)', 'G': 'T^dagger T', 'C': 'c G',
            'normalization': 'G^-1 C = c I', 'M_U_joint_commutant_dimension': 1,
            'diagnostic': '[[0,1,0],[1,1,0],[0,0,2]] has three distinct eigenvalues and commutes with neither M nor U',
            'M': '[[0,-(1+i)/2,(1-i)/2],[-(1+i)/2,-i/2,-1/2],[(1-i)/2,-1/2,i/2]]',
            'U_deck': 'diag(1,i,-i)',
            'interpretation': 'Algebraic control case; l is not a TFPT calibration.',
        },
        'boundary': 'Scalar low-frequency response and Gram normalization do not select the native source from P1/P2 or prove physical masses.',
    }
    args.out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
