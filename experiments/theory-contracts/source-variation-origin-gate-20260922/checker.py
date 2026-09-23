#!/usr/bin/env python3
"""Exact finite source-variation/origin gate.

The checks distinguish ambient frame flatness from curvature after projection,
and distinguish an isospectral path from the Hessian of a linearized path.
They are algebraic identities and finite rank computations only; they do not
derive a physical field, sector, or spacetime interpretation.
"""

from pathlib import Path
import argparse
import json

import sympy as sp


I = sp.I
HERE = Path(__file__).resolve().parent


def need(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def matrix_string(matrix):
    return str(matrix)


def real_coordinates(matrix):
    """Flatten a complex matrix into real and imaginary symbolic coordinates."""
    return sp.Matrix([
        part
        for entry in matrix
        for part in (sp.re(entry), sp.im(entry))
    ])


def real_span_rank(matrices):
    if not matrices:
        return 0
    return sp.Matrix.hstack(*[real_coordinates(matrix) for matrix in matrices]).rank()


def hermitian_matrix(diagonal, real_parts, imaginary_parts):
    matrix = sp.zeros(4)
    for index in range(4):
        matrix[index, index] = diagonal[index]
    for index in range(4):
        for other in range(index + 1, 4):
            real_part = real_parts[index, other]
            imaginary_part = imaginary_parts[index, other]
            matrix[index, other] = real_part + I * imaginary_part
            matrix[other, index] = real_part - I * imaginary_part
    return matrix


def divided_difference_fprime(a, b):
    # f(x)=x^4, f'(x)=4x^3, including the diagonal limit.
    if a == b:
        return 12 * a ** 2
    return sp.factor(4 * (a ** 2 + a * b + b ** 2))


def main():
    P0 = sp.diag(0, 1, 1, 1)
    p0 = sp.eye(4) - P0
    need(P0 * P0 == P0 and p0 * p0 == p0 and P0 * p0 == sp.zeros(4),
         'P0 and p0 are complementary projectors')

    generators = []
    generator_names = []
    for index in range(1, 4):
        E_j0 = sp.zeros(4)
        E_0j = sp.zeros(4)
        E_j0[index, 0] = 1
        E_0j[0, index] = 1
        generators.append(E_j0 - E_0j)
        generator_names.append('X' + str(index))
        generators.append(I * (E_j0 + E_0j))
        generator_names.append('Y' + str(index))
    need(len(generators) == 6, 'six anti-Hermitian generators')
    need(all(generator.H == -generator for generator in generators),
         'all six generators are anti-Hermitian')

    dP = [generator * P0 - P0 * generator for generator in generators]
    need(all(matrix.H == matrix for matrix in dP), 'projector variations are Hermitian')
    curvatures = []
    for index in range(6):
        for other in range(index + 1, 6):
            curvatures.append(P0 * (dP[index] * dP[other] - dP[other] * dP[index]) * P0)
    curvature_rank = real_span_rank(curvatures)
    traceless_curvatures = [matrix - sp.trace(matrix) * P0 / 3 for matrix in curvatures]
    traceless_rank = real_span_rank(traceless_curvatures)
    need(curvature_rank == 9, 'projected curvature real span has rank 9')
    need(traceless_rank == 8, 'traceless projected curvature real span has rank 8')

    ambient = [-generator for generator in generators]
    D = [dP[index] + ambient[index] * P0 - P0 * ambient[index]
         for index in range(6)]
    need(all(matrix == sp.zeros(4) for matrix in D),
         'frame-transformed ambient variation is zero')
    # For U(q)=exp(sum q_a G_a), A=-dU U^dagger. Its derivatives matter:
    # at the base point d_a A_b=-[G_a,G_b]/2, so F^ambient=0.
    ambient_curvatures = []
    for index in range(6):
        for other in range(index + 1, 6):
            bracket = generators[index] * generators[other] - generators[other] * generators[index]
            derivative_difference = -bracket
            ambient_curvatures.append(derivative_difference + ambient[index] * ambient[other] - ambient[other] * ambient[index])
    need(all(matrix == sp.zeros(4) for matrix in ambient_curvatures),
         'Maurer-Cartan derivative cancels ambient connection commutator')
    flat_curvatures = []
    for index in range(6):
        for other in range(index + 1, 6):
            flat_curvatures.append(D[index] * D[other] - D[other] * D[index])
    need(all(matrix == sp.zeros(4) for matrix in flat_curvatures),
         'flat ambient frame has zero projected curvature')

    b = sp.symbols('b', nonzero=True, real=True)
    r = sp.symbols('r', real=True)
    beta = b * (sp.eye(4) - 4 * p0)
    m = sp.diag(-2 - 3 * r, r, r, r)
    need(beta == sp.diag(-3 * b, b, b, b), 'beta has the specified singlet-first form')
    need(m == sp.diag(-2 - 3 * r, r, r, r), 'm is reordered with singlet first')
    need(beta * P0 == P0 * beta and m * P0 == P0 * m,
         'beta and m commute with P0')

    # A generic Hermitian 4 by 4 matrix has 16 real coordinates.
    diagonal = sp.symbols('h0:4', real=True)
    real_parts = {}
    imaginary_parts = {}
    for index in range(4):
        for other in range(index + 1, 4):
            real_parts[index, other] = sp.symbols(
                'u' + str(index) + str(other), real=True)
            imaginary_parts[index, other] = sp.symbols(
                'v' + str(index) + str(other), real=True)
    H_generic = hermitian_matrix(diagonal, real_parts, imaginary_parts)
    commutant_variables = list(diagonal)
    for index in range(4):
        for other in range(index + 1, 4):
            commutant_variables += [real_parts[index, other], imaginary_parts[index, other]]

    def coefficient_matrix(expression, variables):
        coordinates = real_coordinates(expression)
        return sp.Matrix([
            [sp.expand(entry).coeff(variable) for variable in variables]
            for entry in coordinates
        ])

    p_constraint = coefficient_matrix(P0 * H_generic - H_generic * P0,
                                      commutant_variables)
    beta_constraint = coefficient_matrix((beta * H_generic - H_generic * beta).subs(b, 1),
                                         commutant_variables)
    need(p_constraint.rank() == 6, 'P0 commutant off-diagonal constraint rank is 6')
    need(16 - p_constraint.rank() == 10, 'Hermitian P0 commutant dimension is 10')
    need(beta_constraint.rank() == 6, 'beta commutant off-diagonal constraint rank is 6 for b=1')
    need((beta * H_generic - H_generic * beta - 4 * b * (P0 * H_generic - H_generic * P0)).applyfunc(sp.expand) == sp.zeros(4),
         'beta and P0 commutants coincide for b nonzero')
    need(all(sp.factor(entry).has(b) for entry in
             real_coordinates(beta * H_generic - H_generic * beta)
             if entry != 0),
         'beta commutator constraints vanish only through b or zero coordinates')

    # The preceding symbolic rank check is the iff statement: for b != 0,
    # the six off-diagonal real coordinates must vanish.  State it directly
    # with the exact substituted commutator to avoid a numerical implication.
    offdiag_zero = H_generic.subs({
        real_parts[index, other]: 0
        for index in range(1) for other in range(index + 1, 4)
    })
    offdiag_zero = offdiag_zero.subs({
        imaginary_parts[index, other]: 0
        for index in range(1) for other in range(index + 1, 4)
    })
    need(beta * offdiag_zero - offdiag_zero * beta == sp.zeros(4),
         'beta commutes with every block-diagonal Hermitian matrix')

    # Isospectral conjugation path in the (0,1) plane.
    e0, e1 = sp.symbols('e0 e1', real=True)
    t = sp.symbols('t', real=True)
    c_t, s_t = sp.cos(t), sp.sin(t)
    rotation = sp.eye(4)
    rotation[0, 0] = c_t
    rotation[0, 1] = -s_t
    rotation[1, 0] = s_t
    rotation[1, 1] = c_t
    h0 = sp.diag(e0, e1, e1, e1)
    h_path = rotation * h0 * rotation.T
    h_char = sp.factor(h_path.charpoly(sp.Symbol('lambda')).as_expr())
    h0_char = sp.factor(h0.charpoly(sp.Symbol('lambda')).as_expr())
    need(h_char == h0_char, 'isospectral path has constant characteristic polynomial')
    X1 = generators[0]
    h_prime = sp.simplify(h_path.diff(t).subs(t, 0))
    h_second = sp.simplify(h_path.diff(t, 2).subs(t, 0))
    nested_prime = X1 * h0 - h0 * X1
    nested_second = X1 * nested_prime - nested_prime * X1
    need(h_prime == nested_prime, 'h prime equals the commutator variation')
    need(h_second == nested_second, 'h second derivative equals nested commutator')
    trace_path_second = sp.factor(2 * sp.trace(h_prime * h_prime + h0 * h_second))
    linearized_hessian = sp.factor(2 * sp.trace(h_prime * h_prime))
    need(trace_path_second == 0,
         'second derivative of Tr(h(t)^2) vanishes including h second derivative')
    need(linearized_hessian == 4 * (e0 - e1) ** 2,
         'linearized Hessian 2 Tr(h prime squared) is nonzero')

    # General Frechet Hessian for f(x)=x^4.  V and W are symbolic Hermitian
    # matrices; the diagonal h0 is the rational witness diag(0,1,2,3).
    rational_h0 = sp.diag(0, 1, 2, 3)
    vdiag = sp.symbols('q0:4', real=True)
    wdiag = sp.symbols('z0:4', real=True)
    vreal = {}
    vimag = {}
    wreal = {}
    wimag = {}
    for index in range(4):
        for other in range(index + 1, 4):
            vreal[index, other] = sp.symbols('q' + str(index) + str(other), real=True)
            vimag[index, other] = sp.symbols('qI' + str(index) + str(other), real=True)
            wreal[index, other] = sp.symbols('z' + str(index) + str(other), real=True)
            wimag[index, other] = sp.symbols('zI' + str(index) + str(other), real=True)
    V = hermitian_matrix(vdiag, vreal, vimag)
    W = hermitian_matrix(wdiag, wreal, wimag)
    path = rational_h0 + t * V + t ** 2 * W / 2
    lhs = sp.expand(2 * sp.trace(path ** 4)).coeff(t, 2)
    rhs = sp.trace(4 * rational_h0 ** 3 * W)
    eigenvalues = [0, 1, 2, 3]
    for index in range(4):
        for other in range(4):
            rhs += divided_difference_fprime(eigenvalues[index], eigenvalues[other]) * V[index, other] * V[other, index]
    rhs = sp.expand(rhs)
    need(sp.expand(lhs - rhs) == 0,
         'Frechet Hessian formula for Tr(h^4)')

    result = {
        'verdict': 'PASS_SCOPED_SOURCE_VARIATION_ORIGIN_ALGEBRAIC_GATE',
        'projector': {
            'P0': matrix_string(P0),
            'p0': matrix_string(p0),
            'generator_names': generator_names,
            'generator_count': len(generators),
        },
        'projected_curvature': {
            'unordered_generator_pairs': 15,
            'real_span_rank': curvature_rank,
            'traceless_real_span_rank': traceless_rank,
            'formula': 'F_ab=P0 [dP_a,dP_b] P0',
        },
        'ambient_frame': {
            'A_a': '-G_a',
            'd_a_A_b_minus_d_b_A_a': '-[G_a,G_b]',
            'ambient_curvature_including_derivatives': '0',
            'D_a_P': '0 for all six generators',
            'projected_curvature': '0',
        },
        'operators': {
            'beta': matrix_string(beta),
            'm': matrix_string(m),
            'beta_commutes_with_P0': True,
            'm_commutes_with_P0': True,
            'generic_hermitian_real_dimension': 16,
            'P0_commutant_dimension': 10,
            'P0_offdiagonal_constraint_rank': 6,
            'beta_offdiagonal_constraint_rank_for_b1': 6,
            'beta_commutant_iff': 'for b != 0, [beta,H]=0 iff H is block diagonal for P0',
        },
        'isospectral_path': {
            'h0': matrix_string(h0),
            'characteristic_polynomial': str(h0_char),
            'h_prime': matrix_string(h_prime),
            'h_second': matrix_string(h_second),
            'trace_h2_second_derivative_including_h_second': str(trace_path_second),
            'linearized_hessian_2_trace_hprime2': str(linearized_hessian),
        },
        'frechet_hessian': {
            'function': 'f(x)=x^4',
            'rational_h0': matrix_string(rational_h0),
            'formula': 'sum_ij (f\')^[1](lambda_i,lambda_j)V_ij V_ji + Tr(f\'(h0)W)',
            'symbolic_hermitian_V_W': True,
            'verified': True,
        },
        'scope': [
            'Finite exact algebraic identities and rank checks only.',
            'The flat ambient frame and nonzero projected curvature are different constructions.',
            'No source-derived P1 field, physical sector, or 4D identification is asserted.',
        ],
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE / 'certificate.json')
    args = parser.parse_args()
    certificate = main()
    args.out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'verdict': certificate['verdict'],
        'curvature_rank': certificate['projected_curvature']['real_span_rank'],
        'traceless_rank': certificate['projected_curvature']['traceless_real_span_rank'],
        'P0_commutant_dimension': certificate['operators']['P0_commutant_dimension'],
        'flat_ambient_variation': certificate['ambient_frame']['D_a_P'],
        'frechet_hessian_verified': certificate['frechet_hessian']['verified'],
    }, sort_keys=True, separators=(',', ':')))
