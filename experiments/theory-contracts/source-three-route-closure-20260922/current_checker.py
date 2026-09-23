#!/usr/bin/env python3
"""Bounded real-Gaussian R/L sign gate; conditional, not a source model."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path


def check_sector(k_plus: float, k_minus: float, mass: float = 2.0, omega_max: float = 0.25) -> dict:
    if k_plus < 0 or k_minus < 0 or mass <= 0 or omega_max < 0:
        raise ValueError("PSD eigenvalues, mass, and frequency bound must be valid")
    a = (k_plus + k_minus) / 2.0
    c = (k_plus - k_minus) / 2.0
    g = -c  # -g/2 B^2 = +g J_R J_L
    return {"a": a, "c": c, "k_plus": k_plus, "k_minus": k_minus,
            "psd": True, "gn_attractive": g > 0, "g": g,
            "zero_frequency_kernel": 1.0 / mass**2,
            "low_frequency_relative_error_bound": omega_max**2 / (mass**2 + omega_max**2)}


def different_mass_witness(omega_sq: Fraction) -> Fraction:
    """Witness g(x) for y_minus^2=1,m_minus^2=1,y_plus^2=2,m_plus^2=4."""
    c_minus = Fraction(1, 1) / (omega_sq + 1)
    c_plus = Fraction(2, 1) / (omega_sq + 4)
    return (c_minus - c_plus) / 2


def check_different_mass_witness() -> dict:
    # Genuine symbolic identity, with numerical values used only for sign samples.
    import sympy as sp
    x = sp.symbols("x")
    lhs = (1 / (x + 1) - 2 / (x + 4)) / 2
    rhs = (2 - x) / (2 * (x + 1) * (x + 4))
    if sp.factor(lhs - rhs) != 0:
        raise RuntimeError("different-mass rational identity failed symbolically")
    g0 = different_mass_witness(Fraction(0))
    g2 = different_mass_witness(Fraction(2))
    g3 = different_mass_witness(Fraction(3))
    if not (g0 > 0 and g2 == 0 and g3 < 0):
        raise RuntimeError("different-mass witness did not show low-frequency sign reversal")
    # |g(w)-g(0)| <= w^2/2*(y_-^2/m_-^4+y_+^2/m_+^4).
    x_sample = Fraction(1, 4)
    bound = x_sample / 2 * (Fraction(1) + Fraction(2, 16))
    if abs(different_mass_witness(x_sample) - g0) > bound:
        raise RuntimeError("general different-mass memory bound failed")
    return {
        "parameters": {"y_minus_squared": 1, "m_minus_squared": 1,
                       "y_plus_squared": 2, "m_plus_squared": 4},
        "identity": "g(x)=(2-x)/(2*(x+1)*(x+4)), x=omega^2",
        "identity_check": "sympy.factor(lhs-rhs)==0",
        "sign_samples": {"x=0": str(g0), "x=2": str(g2), "x=3": str(g3)},
        "general_bound": "|g(omega)-g(0)| <= omega^2/2*(y_minus^2/m_minus^4+y_plus^2/m_plus^4)",
        "bound_at_sample_x_1_4": str(bound),
        "psd_parity_covariances": True,
    }


def build_certificate() -> dict:
    attractive = check_sector(1.0, 2.0)
    repulsive = check_sector(2.0, 1.0)
    illustrative = {name: check_sector(1.0, 2.0) for name in ("45", "15", "60")}
    different_mass = check_different_mass_witness()
    if not (attractive["gn_attractive"] and not repulsive["gn_attractive"]):
        raise RuntimeError("GN sign gate failed: PSD examples did not separate signs")
    if not (attractive["psd"] and repulsive["psd"]):
        raise RuntimeError("PSD gate failed: k_plus,k_minus >= 0 was not preserved")
    if not (attractive["low_frequency_relative_error_bound"] < 0.016):
        raise RuntimeError("common-mass low-frequency error bound exceeded threshold")
    return {
        "status": "conditional_response_formula",
        "reflection_swap": [[0, 1], [1, 0]],
        "conditions": ["k_plus>=0", "k_minus>=0", "mass>0", "omega_max>=0"],
        "covariance": "Sigma=[[a,c],[c,a]], k_plus=a+c>=0, k_minus=a-c>=0",
        "effective_action": "-1/2 J^T Sigma J; cross coefficient=-c J_R J_L",
        "gn_convention": "-g/2 B^2 = +g J_R J_L; g=-c=(k_minus-k_plus)/2",
        "positive_semidefinite_does_not_select_sign": {
            "attractive_example": attractive, "repulsive_example": repulsive},
        "illustrative_invariant_channel_coefficients": illustrative,
        "different_parity_mass_witness": different_mass,
        "reflection_warning": "Spatial/chiral exchange and OS time reflection are distinct typings; D_rel oddness alone does not establish a physical odd mediator.",
        "source_boundary": "No native covariance or 45/15/60 invariant source-response reduction is derived by this bounded checker.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("current_certificate.json"))
    args = parser.parse_args()
    certificate = build_certificate()
    args.out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
