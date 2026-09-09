"""NON-RH: sourced half twist, charge carry, and a one-edge low-mode bound.

Exact target-lattice and one-particle statements. Neither a microscopic
charged field nor a many-body scaling-limit / T1-T8 closure certificate.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "verification/v983_simple_current_generator.py": "769a9c5cb5e6518d8d2a445d347150f5ce0d1410c95db263ca2db72466e176c8",
    "verification/v1033_charged_disorder.py": "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f",
    "verification/v988_psi_lambda_reduction.py": "eae02e79be5703ccec67f1f11470e3ffd99895b17575c9ce1d553720bd1752cd",
    "verification/v469_seam_crossedproduct_route.py": "180a65f5e56dce6cca8c519875ab31e3e0834fb8818175f2a63c896133e72089",
    "articles/2026-08-30/mmst_charged_scaling_limit_en.tex": "ab2802e14a31715be3552ee2a529e88afeb1a59e5d57ffb9cbea8f32e4df0462",
    "experiments/theory-contracts/charged-cocycle-lift/checker.py": "4be4fa0ea26e4ce302b59f53f86787953544c7ea355168ccc24501501cc8d1dc",
    "experiments/theory-contracts/charged-cocycle-lift/validation.json": "170bc4f5a63727c8d26265bf87ba5c36a737b8d55de810a7a2ba214dbe2b4ef9",
}
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.diag(1, -1)
TX = -sp.I*SX/2-SZ/2
TY = sp.Matrix([[-1, -1], [1, 1]])/2
S2 = (1,)*8  # All lattice vectors below are in doubled physical coordinates.
T = sp.Matrix([[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])/2


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(relative, name, root=ROOT):
    spec = importlib.util.spec_from_file_location(name, Path(root)/relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # dataclass source v1033 needs this entry.
    old_path = list(sys.path)
    try:
        sys.path.insert(0, str(Path(root)/"verification"))
        spec.loader.exec_module(module)
    finally:
        sys.path[:] = old_path
    return module


def inherited(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: "+name)
    glue = load("verification/v983_simple_current_generator.py", "half_glue", root)
    qwz = load("verification/v1033_charged_disorder.py", "half_qwz", root)
    old_qwz = load("verification/v988_psi_lambda_reduction.py", "half_old_qwz", root)
    charged = load("experiments/theory-contracts/charged-cocycle-lift/checker.py", "half_charged", root)
    return glue, qwz, old_qwz, charged, charged.build(root)


def in_e8(q2):
    return (len(q2) == 8 and all(isinstance(v, int) for v in q2)
            and len({v % 2 for v in q2}) == 1 and sum(q2) % 4 == 0)


def in_l0(q2):
    return in_e8(q2) and all(v % 2 == 0 for v in q2) and sum(q2[:5]) % 4 == 0


def grade(q2):
    require(in_e8(q2), "grade requires a doubled E8 vector")
    return sum(q2[:5]) % 4


def split(q2):
    k = grade(q2)
    neutral = tuple(v-k for v in q2)
    require(in_l0(neutral), "Z4 representative has L0 remainder")
    return neutral, k


def roots():
    out = []
    for i, j in itertools.combinations(range(8), 2):
        for a, b in itertools.product((-2, 2), repeat=2):
            q = [0]*8
            q[i], q[j] = a, b
            out.append(tuple(q))
    out.extend(q for q in itertools.product((-1, 1), repeat=8) if sum(q) % 4 == 0)
    return tuple(out)


def geometry_certificate(glue):
    require(T*T.T == sp.eye(3) and T.T*T == sp.eye(4)-sp.ones(4)/4,
            "A3 hyperplane isometry")
    image = list(glue.OMEGA_S)+list(T*sp.Matrix(glue.OMEGA_F))
    require(image == [sp.Rational(1, 2)]*8, "sourced lambda maps to half twist")
    a3_roots = {tuple(T*(sp.eye(4)[:, i]-sp.eye(4)[:, j]))
                for i in range(4) for j in range(4) if i != j}
    d3_roots = {tuple(v//2 for v in q[5:]) for q in roots()
                if q[:5] == (0,)*5}
    require(a3_roots == d3_roots and len(a3_roots) == 12, "A3 roots map onto D3 roots")
    census = Counter(grade(q) for q in roots())
    require([census[k] for k in range(4)] == [52, 64, 60, 64], "source glue census")
    require(len(set(roots())) == 240 and all(sum(v*v for v in q) == 8 for q in roots()),
            "complete standard E8 root set")
    # Inverse map checks the actual v983 L0 definition, not just a renamed grade.
    for q in roots()+tuple(tuple(k*v for v in S2) for k in range(5)):
        neutral, k = split(q)
        old = [sp.Rational(v, 2) for v in neutral[:5]]
        old += list(T.T*sp.Matrix([sp.Rational(v, 2) for v in neutral[5:]]))
        require(glue.in_L0(old), "grade remainder satisfies original D5+A3 source")
    require([in_l0(tuple(k*v for v in S2)) for k in range(1, 5)] == [False, False, False, True],
            "order four relative to L0, not relative to D8")
    return {"A3_to_D3_matrix": [[str(x) for x in T.row(i)] for i in range(3)],
            "lambda_image": ["1/2"]*8, "rank": 8,
            "half_twist_weight": 1, "quarter_twist_weight": "1/4",
            "quarter_ansatz_repaired_without_change": False,
            "root_census": [census[k] for k in range(4)],
            "weight_one_census_with_Cartan": [60, 64, 60, 64],
            "glue_order_over_L0": 4, "spinor_order_over_D8": 2,
            "D8_spinor_extension_already_in_v469": True,
            "projection_alone_supplies_Ramond_extension": False}


def charge_certificate(charged, data):
    lam = tuple(data["lat"]["coords"](S2))
    require(charged.energy(data, lam) == 1, "inherited lambda energy")
    require(data["cocycle"](charged.bitmask(lam), charged.bitmask(lam)) == 1,
            "inherited odd cocycle square for a root")
    states = [(0,)*8, lam, tuple(-5*v for v in lam),
              (10**12, -10**12, 2, -3, 5, -7, 11, -13)]
    for state in states:
        original = {state: 1}
        twice = charged.charged_shift(data, lam, charged.charged_shift(data, lam, original))
        direct2 = charged.charged_shift(data, tuple(2*v for v in lam), original)
        require(twice == {q: -a for q, a in direct2.items()}, "U_s squared is -U_2s")
        four = original
        for _ in range(4):
            four = charged.charged_shift(data, lam, four)
        require(four == charged.charged_shift(data, tuple(4*v for v in lam), original)
                and four != original, "four shifts carry charge, not identity")
        dest = tuple(a+b for a, b in zip(state, lam))
        require(charged.energy(data, dest)-charged.energy(data, state)
                == charged.charge_dot(data, lam, state)+1, "lambda energy Ward identity")
    # C(q)=i**grade(q)=i**b*(-1)**sum(n_first5), q=n+b*s.
    controls = roots()+tuple(tuple(j*v for v in S2) for j in (-10**12, -3, 0, 1, 2, 3, 4, 10**12))
    changes = set()
    for q2 in controls:
        b = q2[0] % 2
        n = tuple((v-b)//2 for v in q2)
        require(sum(n) % 2 == 0, "NS/R integer remainder is in D8")
        require(grade(q2) == (b+2*sum(n[:5])) % 4, "internal clock is parity with spin lift")
        flip = tuple(2*v+(1-b) for v in n)
        changes.add((b, (grade(flip)-grade(q2)) % 4))
        shifted = tuple(v+1 for v in q2)
        require((grade(shifted)-grade(q2)) % 4 == 1, "full charge shift has uniform grade one")
        old_neutral, k = split(q2)
        new_neutral, new_k = split(shifted)
        require(new_k == (k+1) % 4 and new_neutral == tuple(v+(4 if k == 3 else 0) for v in old_neutral),
                "carry through Z4 wrap")
    require(changes == {(0, 1), (1, 3)}, "plain NS/R flip has alternating charge grade")
    return {"lambda_in_inherited_integral_basis": list(map(int, lam)),
            "U_s_square": "-U_2s (inherited cocycle convention)",
            "U_s_fourth_power": "U_4s, not I", "neutral_carry_doubled": [4]*8,
            "ray_zero_mode_energies": [0, 1, 4, 9, 16],
            "these_ray_energies_are_not_minimal_sector_weights": True,
            "plain_boundary_flip_grade_changes": [[0, 1], [1, 3]],
            "carry_corrected_grade_change": 1, "large_charge_control": 10**12,
            "internal_grade_identified_with_Gaussian_deck_or_time_clock": False,
            "full_microscopic_charge_carry_constructed": False}


def phase_vector(nx, ny, endpoint, width):
    require(nx >= 4 and 0 <= endpoint < nx-1 and 1 <= width <= ny, "valid arc and strip")
    phase = np.ones(2*nx*ny, complex)
    for x in range(endpoint+1):
        phase[2*(x*ny+ny-width):2*((x+1)*ny)] = -1
    return phase


def residual_parts(qwz, nx, ny, endpoint, width, sector):
    phase = phase_vector(nx, ny, endpoint, width)
    h = qwz.qwz_cylinder(nx, ny, 1, sector)
    hn = qwz.qwz_cylinder(nx, ny, 1, sector+2)
    residual = hn*phase[None, :]-phase[:, None]*h
    end, vertical, seam = (np.zeros_like(h) for _ in range(3))
    for y in range(ny-width, ny):
        i = 2*(endpoint*ny+y)
        j = i+2*ny
        end[j:j+2, i:i+2] = -2*qwz.TX
        end[i:i+2, j:j+2] = 2*qwz.TX.conj().T
    if width < ny:
        for x in range(endpoint+1):
            i = 2*(x*ny+ny-width-1)
            j = i+2
            vertical[j:j+2, i:i+2] = 2*qwz.TY
            vertical[i:i+2, j:j+2] = -2*qwz.TY.conj().T
    for y in range(ny-width):
        i = 2*((nx-1)*ny+y)
        j = 2*y
        seam[j:j+2, i:i+2] = -2*(1j**sector)*qwz.TX
        seam[i:i+2, j:j+2] = -2*((-1j)**sector)*qwz.TX.conj().T
    return residual, end, vertical, seam


def microscopic_certificate(qwz, old_qwz):
    for actual, expected in ((qwz.TX, TX), (qwz.TY, TY)):
        require(np.array_equal(actual, np.array(expected, complex)), "exact source hopping entries")
    require(TX.rank() == TY.rank() == 1 and (TX.H*TX)**2 == TX.H*TX
            and (TY.H*TY)**2 == TY.H*TY, "rank-one unit-singular-value hopping blocks")
    rows = []
    for nx, ny, endpoint in ((5, 8, 1), (7, 8, 2), (9, 8, 3)):
        for sector in range(4):
            require(np.array_equal(qwz.qwz_cylinder(nx, ny, 1, sector),
                                   old_qwz.qwz_cylinder(nx, ny, 1, sector)), "v988 and v1033 actual matrices agree")
            phase = phase_vector(nx, ny, endpoint, ny)
            require(np.array_equal(phase, np.diag(qwz.sharp_arc_phase(nx, ny, endpoint))**2),
                    "full half string is source quarter string squared")
            for width in (1, 2, 4, ny):
                residual, end, vertical, seam = residual_parts(qwz, nx, ny, endpoint, width, sector)
                require(np.array_equal(residual, end+vertical+seam), "exact three-part microscopic residual")
                if width == ny:
                    require(not np.any(vertical) and not np.any(seam), "whole-width endpoint cancellation")
                    require(np.vdot(residual, residual).real == 8*ny, "whole-width exact squared HS norm")
                else:
                    require(np.count_nonzero(vertical) == 8*(endpoint+1)
                            and np.vdot(vertical, vertical).real == 8*(endpoint+1), "extended vertical defect, not endpoint only")
        rows.append({"nx": nx, "ny": ny, "arc_length": endpoint+1,
                     "whole_width_residual_rank_per_copy": 2*ny,
                     "whole_width_residual_operator_norm": 2,
                     "vertical_defect_rank_per_copy": 2*(endpoint+1),
                     "vertical_defect_squared_HS_norm": 8*(endpoint+1),
                     "sectors_tested": 4, "widths_tested": [1, 2, 4, ny]})
    return {"actual_source_cases": 48, "arithmetic": "exact dyadic complex entries; symbolic block ranks/norms",
            "cases": rows, "finite_whole_width_string_endpoint_local": True,
            "finite_one_edge_strip_string_endpoint_local": False,
            "no_go_scope": "on-site scalar phase strings with exact endpoint-only intertwining",
            "general_charged_field_no_go": False}


def edge_polynomial_certificate(ny=8, widths=(1, 2, 4)):
    require(ny >= 2 and all(1 <= w < ny for w in widths), "edge strip widths below cylinder width")
    rho, sine, cosine = sp.symbols("rho sine cosine", real=True)
    plus, minus = sp.Matrix([1, 1]), sp.Matrix([1, -1])
    require(sp.expand((cosine-sp.I*sine)*TX+(cosine+sp.I*sine)*TX.H+SZ
                      +sine*SX-(1-cosine)*SZ) == sp.zeros(2), "source Fourier sign and edge symbol")
    h = sp.zeros(2*ny)
    for y in range(ny):
        h[2*y:2*y+2, 2*y:2*y+2] = -sine*SX+rho*SZ
        if y+1 < ny:
            h[2*y+2:2*y+4, 2*y:2*y+2] = TY
            h[2*y:2*y+2, 2*y+2:2*y+4] = TY.H
    v = sp.Matrix.vstack(*(rho**(ny-1-y)*plus for y in range(ny)))
    target = sp.Matrix.vstack(rho**ny*minus, sp.zeros(2*ny-2, 1))
    require(sp.simplify((h+sine*sp.eye(2*ny))*v-target) == sp.zeros(2*ny, 1),
            "finite-width top-edge quasimode residual exactly rho^ny at opposite edge")
    norm = sum(rho**(2*j) for j in range(ny))
    for w in widths:
        d = sp.diag(*(1 if y < ny-w else -1 for y in range(ny) for _ in range(2)))
        target = sp.zeros(2*ny, 1)
        target[2*(ny-w):2*(ny-w)+2, 0] = -2*rho**w*minus
        require(sp.simplify((h*d-d*h)*v-target) == sp.zeros(2*ny, 1),
                "vertical defect on top profile is order rho^w, not rho^(w-1)")
        tail = sum(rho**(2*j) for j in range(w, ny))
        positive_remainder = sum(rho**(2*j) for j in range(ny, ny+w))
        require(sp.expand(rho**(2*w)*norm-tail-positive_remainder) == 0,
                "normalized tail norm <= rho^w by nonnegative polynomial")
    bounds = []
    for n in (16, 32, 64, 128):
        # K=11 covers n=-1,0,1 in all four sectors since 7*pi/2 < 11.
        rmax = sp.Rational(121, 2*n*n)  # |p|<=11/N, 1-cos(p)<=p^2/2.
        bounds.append({"N": n, "scaled_unwanted_defect_cap_w2_pmax_11_over_N": str(sp.Rational(n, 6)*4*rmax**2),
                       "scaled_quasimode_residual_cap_pmax_11_over_N": str(sp.Rational(n, 6)*rmax**ny)})
    return {"ny": ny, "widths": list(widths), "source_edge_energy": "-sin(p), top edge for exp(+ipx)",
            "source_sector_momenta": "p=(2*pi*n-r*pi/2)/N",
            "top_profile": "rho^(ny-1-y)*(1,1)/sqrt(2*sum_j rho^(2*j)); rho=1-cos(p)",
            "normalized_quasimode_residual_bound": "rho^ny",
            "one_particle_vertical_defect_bound": "2*rmax^w",
            "one_particle_unwanted_vertical_plus_seam_bound": "4*rmax^w",
            "strip_versus_whole_string_bound_on_low_modes": "2*rmax^w",
            "scaled_unwanted_bound_fixed_pmax_K_over_N": "2^(1-w)*K^(2*w)/pi * N^(1-2*w)",
            "w2_scaled_rate": "O(N^-3) on each fixed one-particle Fourier core",
            "exact_low_mode_caps_using_pi_greater_than_3": bounds,
            "one_particle_result_proves_many_body_vacuum_or_adjoint_tail_control": False,
            "true_finite_width_eigenvector_claimed": False}


def run(root=ROOT):
    glue, qwz, old_qwz, charged, data = inherited(root)
    return {"schema": 1, "scope": "NON-RH; target charge algebra and sourced microscopic one-particle bridge",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "source_pins": PINS,
            "geometry": geometry_certificate(glue), "charge_carry": charge_certificate(charged, data),
            "microscopic": microscopic_certificate(qwz, old_qwz), "edge_scaling": edge_polynomial_certificate(),
            "remaining": ["same-parent microscopic charged carry and cocycle",
                          "nonzero smeared field plus adjoint on full many-body finite-energy core",
                          "vacuum, ultraviolet and oscillator tail control",
                          "support-preserving generated local algebra, not edge projection by fiat",
                          "3+1D reconstruction, chiral matter, gravity and common-source dynamics"],
            "T1_T8_closed": False, "microscopic_charged_field_constructed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(args.root), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(result)
    print(result)


if __name__ == "__main__":
    main()
