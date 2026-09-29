"""Exact affine-level diagnostics on the existing marked E8 current algebra.

These tests compare unitary affine vacuum candidates. They do not derive an
affine field realization, a physical vacuum, or a 4D theory from P1/P2. In
particular, the level-one four-point law must not be fed back as an independent
origin assumption. The original level-one source evaluator remains unchanged.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from typing import Any

import sympy as sp

from .current_block_geometry import (
    _actual_current_source, _bracket, _kappa, _ward_at_infinity,
)
from .source_program import _field, _position


def _positive_level(level: int) -> int:
    if type(level) is not int or level < 1:
        raise ValueError("a nontrivial unitary affine vacuum level is a positive integer")
    return level


def four_point_coefficients(
    word: list[dict[str, Any]], positions: list[Any] = (-1, 0, 1),
) -> tuple[Fraction, Fraction]:
    """Return (P, Q) for F_k=k**2 P+k Q, with the fourth field at infinity.

    The coefficient of the field at infinity is lim(z4**2 F). Kappa and all
    Lie brackets come from the original Chevalley table, not Kronecker guesses.
    """
    if len(word) != 4 or len(positions) != 3:
        raise ValueError("four fields and three distinct finite positions are required")
    z1, z2, z3 = tuple(_position(z) for z in positions)
    if len({z1, z2, z3}) != 3:
        raise ValueError("finite positions must be distinct")
    a, b, c, d = tuple(_field(field)[1] for field in word)
    source = _actual_current_source()
    pair = (
        _kappa(source, a, b) * _kappa(source, c, d) / (z1-z2)**2
        + _kappa(source, a, c) * _kappa(source, b, d) / (z1-z3)**2
        + _kappa(source, a, d) * _kappa(source, b, c) / (z2-z3)**2
    )
    fused = (
        _kappa(source, _bracket(source, _bracket(source, a, b), c), d)
        / ((z1-z2)*(z2-z3))
        + _kappa(source, _bracket(source, _bracket(source, a, c), b), d)
        / ((z1-z3)*(z3-z2))
    )
    return pair, fused


def evaluate_affine_four(
    word: list[dict[str, Any]], positions: list[Any], level: int,
) -> Fraction:
    k = _positive_level(level)
    p, q = four_point_coefficients(word, positions)
    return k*k*p + k*q


def root_power_norm(level: int, power: int) -> int:
    """Norm squared of (e_alpha,-1)**power Omega in the unitary affine module.

    The root sl2 triple gives f_1 e_-1**n Omega =
    n*(k-n+1)*e_-1**(n-1) Omega. Thus null vectors stay null in the quotient.
    This mode relation is not the square of a finite matrix or a CAR label.
    """
    k = _positive_level(level)
    if type(power) is not int or power < 0:
        raise ValueError("power must be a nonnegative integer")
    norm = 1
    for n in range(1, power + 1):
        norm *= n*(k-n+1)
    return norm


def native_spin_anomaly(lift: tuple[int, ...] = (0,0,-1,-1)) -> dict[str, Any]:
    """Characteristic response of the original common real rank-16 carrier.

    V=E_R + Fix(Lambda^2 F), with projective F weights m_j+1/2 and sum m=-2.
    Its global spin lift has lambda(V)=d*c1(E)^2-c2(E), d=sum(m_j^2)/2.
    IF the actual seam symbol is the same-chirality real Dirac symbol on V,
    its Pfaffian anomaly is lambda(V)-p1(T)/3. This function does not infer
    that symbol or CAR quantization from the mere existence of the bundle.

    The original P2 generator is Y=(-1/3,-1/3,-1/3,1/2,1/2). The coefficient
    ratio 5/4 uses exactly this normalization; it is not a U(1)-rescaling
    invariant. The determinant-circle level is 2*d, NOT the single pump 1.
    """
    if (not isinstance(lift, (tuple,list)) or len(lift) != 4
            or any(type(m) is not int for m in lift) or sum(lift) != -2):
        raise ValueError("a native joint lift has four integer entries with sum -2")
    d = Fraction(sum(m*m for m in lift),2)
    paired_exponents = [lift[i]+lift[3]+1 for i in range(3)]
    gravity = Fraction(-16,48)
    p2_gauge = sum(q*q for q in [Fraction(-1,3)]*3+[Fraction(1,2)]*2)/2
    return {
        "lift":list(lift), "real_rank":16,
        "three_real_plane_exponents":paired_exponents,
        "w2_V6_in_units_of_c1_mod_two":sum(paired_exponents)%2,
        "w2_total_in_units_of_c1_mod_two":(1+sum(paired_exponents))%2,
        "lambda_c1_squared_coefficient":str(d),
        "lambda_c2_coefficient":"-1",
        "p1_T_coefficient":str(gravity), "chiral_central_charge":8,
        "determinant_circle_level":int(2*d),
        "P2_Y_charges":["-1/3"]*3+["1/2"]*2,
        "P2_Y_squared_coefficient":str(p2_gauge),
        "P2_gauge_to_gravity_absolute_coefficient_ratio":str(abs(p2_gauge/gravity)),
        "scope":"global native spin bundle; anomaly conditional on its actual chiral Dirac/Pfaffian realization",
        "origin_guard":"Neither the symbol identification nor CAR quantization is derived by characteristic classes alone.",
        "normalization_guard":"The P2 coefficient ratio is 5/4 for Y; for the integral generator 6Y it is 45.",
        "pump_guard":"Every such lift has even determinant-circle level >=2, so it is not the original single level-1 pump in the same normalization.",
    }


def affine_sewing_exclusion() -> dict[str, Any]:
    """Uniform higher-level vacuum-block exclusion with rational certificate.

    Positive affine levels k>=2 have c>=31/2 and vacuum grade-two dimension
    248+Sym^2(248)=31124. The first affine integrability null has grade k+1.
    At i, R_chi=exp(c*epsilon)*sum d_n exp(-2*pi*n).
    512<exp(2*pi)<540 implies epsilon>0 and the rational lower bound below.
    For nonholomorphic theories R_chi is a vacuum block, not the full ratio.
    A full positive left/right sector sum is instead bounded by R_chi**2.
    """
    def exp_bounds(r: Fraction) -> tuple[Fraction,Fraction]:
        term = Fraction(1)
        lower = term
        for n in range(1,33):
            term *= r/n
            lower += term
        first_omitted = term*r/33
        upper = lower+first_omitted/(1-r/34)
        return lower,upper
    # The classical bounds 157/50 < pi < 22/7 bound the two positive series.
    lower = exp_bounds(Fraction(157,25))[0]
    upper = exp_bounds(Fraction(44,7))[1]
    grade_two = 248+248*249//2
    bound = 1+Fraction(248,540)+Fraction(grade_two,540**2)
    return {
        "class":"unitary positive-integer-level affine E8 vacuum modules, k>=2",
        "grade_two":grade_two,"central_charge_lower_bound":"31/2",
        "epsilon":"pi/12 - 3*log(2)/8",
        "exponential_interval":["512","540"],
        "rational_certificate_512_below_exp_157_25":lower>512,
        "rational_certificate_exp_44_7_below_540":upper<540,
        "uniform_vacuum_block_lower_bound":str(bound),
        "margin_above_three_halves":str(bound-Fraction(3,2)),
        "paired_positive_sector_lower_bound":str(bound**2),
        "paired_margin_above_nine_quarters":str(bound**2-Fraction(9,4)),
        "sharper_lower_bound_expression":"exp((31/2)*epsilon)*(1+248*exp(-2*pi)+31124*exp(-4*pi))",
        "scope":"a separating response criterion within the declared affine class, not an independent raw-source measurement",
        "paired_scope":"full unitary left/right E8_k theory with nonnegative sector multiplicities and vacuum multiplicity one; this adds a comparison class, not a right-moving TFPT sector",
        "origin_guard":"Using the E8_1-derived 3/2 as its own origin selector is circular. The target response and sewing interpretation must be independently derived.",
    }


def _x_word(carrier: tuple[int, ...], family: tuple[int, ...]) -> list[dict[str, Any]]:
    return [{"kind": "X", "i": i, "a": a, "dagger": bool(j % 2)}
            for j, (i, a) in enumerate(zip(carrier, family))]


def _equality_types(n: int) -> list[tuple[int, ...]]:
    """Restricted-growth strings: every equality pattern, not random samples."""
    result = [(0,)]
    for _ in range(1, n):
        result = [r + (value,) for r in result for value in range(max(r)+2)]
    return result


@lru_cache(maxsize=1)
def build_source_selection_data() -> dict[str, Any]:
    source = _actual_current_source()
    patterns = _equality_types(4)
    failures = []
    for carrier, family in product(patterns, repeat=2):
        i,j,k,l = carrier
        a,b,c,d = family
        direct = int(i==j and k==l and a==b and c==d)
        crossed = int(i==l and j==k and a==d and b==c)
        mixed_one = int(i==j and k==l and a==d and b==c)
        mixed_two = int(i==l and j==k and a==b and c==d)
        word = _x_word(carrier, family)
        p, q = four_point_coefficients(word)
        vectors = tuple(_field(f)[1] for f in word)
        if (p,q) != (direct+crossed,mixed_one+mixed_two):
            failures.append({"carrier":carrier,"family":family,"kind":"tensor"})
        if p+q != _ward_at_infinity(source, vectors, tuple(map(Fraction,(-1,0,1)))):
            failures.append({"carrier":carrier,"family":family,"kind":"level_one"})

    direct_word = _x_word((0,0,1,1),(0,0,1,1))
    mixed_word = _x_word((0,0,1,1),(0,1,1,0))
    k = sp.symbols("k", positive=True)
    central = 248*k/(k+30)
    neutral_norm = sp.factor((central-8)/2)
    # Tensor-symmetric level-two states, before the first integrability ideal.
    grade_two_universal = 248 + 248*249//2
    shell_four_integer = 16 + comb(8,4)*16
    shell_four_half_integer = 8*128
    grade_two_lattice = (8+8*9//2) + 240*8 + shell_four_integer + shell_four_half_integer
    rows = []
    for level in (1,2,3,4,8):
        straight = evaluate_affine_four(direct_word, (-1,0,1), level)
        mixed = evaluate_affine_four(mixed_word, (-1,0,1), level)
        rows.append({
            "level":level, "central_charge":str(Fraction(248*level,level+30)),
            "direct_four":str(straight), "mixed_four":str(mixed),
            "ratio_mixed_to_direct":str(mixed/straight),
            "root_double_mode_norm_squared":root_power_norm(level,2),
            "neutral_grade_two_norm_squared":str(Fraction(120*(level-1),level+30)),
        })
    return {
        "scope":"exact diagnostics conditional on the actual affine unitary vacuum realization",
        "not_derived":"P1/P2 identification with the affine fields, selected physical state, and 3+1D realization",
        "four_tensor":"k^2(A+D)+k(B+C)",
        "fixed_family_tensor":"k(k+1)(delta_ij delta_kl+delta_il delta_jk)",
        "normalized_W5_selects_level":False,
        "mixed_response_selects_level_one_if_independently_required":True,
        "neutral_norm_formula":str(neutral_norm),
        "root_double_mode_norm_formula":"2*k*(k-1)",
        "rows":rows, "words":{"direct":direct_word,"mixed":mixed_word},
        "equality_pattern_pairs":len(patterns)**2,"failures":failures,
        "grade_two":{"level_one_lattice":grade_two_lattice,
                     "levels_at_least_two":grade_two_universal,
                     "null_representation_at_one":grade_two_universal-grade_two_lattice},
        "origin_guard":"Reusing a tensor derived from E8_1 to select E8_1 would be circular.",
        "vacuum_guard":"Uniqueness of the affine vacuum sector does not prohibit excited physical states.",
        "native_spin_anomaly":native_spin_anomaly(),
        "affine_sewing_exclusion":affine_sewing_exclusion(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(build_source_selection_data(), indent=2))
