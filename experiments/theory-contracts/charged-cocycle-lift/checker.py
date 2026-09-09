"""NON-RH: charged E8 cocycle refinement and symmetry-compatible compiler lifts.

Finite charge-sign algebra only, not a microscopic field or 3+1D completion.
The Gaussian quotient is retained, but is not mistaken for a quotient of the
charged lattice central extension. All proof guards survive python -OO.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "verification/v774_arf_spinor_compiler.py": "3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c",
    "verification/v983_simple_current_generator.py": "769a9c5cb5e6518d8d2a445d347150f5ce0d1410c95db263ca2db72466e176c8",
    "verification/v1033_charged_disorder.py": "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f",
    "articles/2026-08-30/mmst_charged_scaling_limit_en.tex": "ab2802e14a31715be3552ee2a529e88afeb1a59e5d57ffb9cbea8f32e4df0462",
    "experiments/theory-contracts/compiler-clifford-bridge/checker.py": "bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d",
    "experiments/theory-contracts/compiler-clifford-bridge/validation.json": "a40b338e99cb0bb0e09d63861621d6b228e4ad5afeed7ea0335352ad043d4e0c",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def parity(x):
    return x.bit_count() % 2


def bitword(mask, dimension):
    return tuple((mask >> i) & 1 for i in range(dimension))


def bitmask(word):
    return sum((int(bit) % 2) << i for i, bit in enumerate(word))


def linear(columns, mask):
    result = 0
    for i, col in enumerate(columns):
        if mask >> i & 1:
            result ^= col
    return result


def span(basis):
    return {linear(basis, word) for word in range(1 << len(basis))}


def independent_basis(vectors):
    result, current = [], {0}
    for v in vectors:
        if v not in current:
            result.append(v)
            current |= {x ^ v for x in tuple(current)}
    return tuple(result)


def affine_solutions(rows, width):
    """Exact GF2 affine elimination; rows are (coefficient bitmask, RHS bit)."""
    reduced = {}
    for coefficients, rhs in rows:
        while coefficients:
            pivot = coefficients.bit_length()-1
            if pivot not in reduced:
                reduced[pivot] = (coefficients, rhs)
                break
            old, value = reduced[pivot]
            coefficients ^= old
            rhs ^= value
        else:
            require(rhs == 0, "consistent affine lift equations")
    free = [i for i in range(width) if i not in reduced]
    solutions = []
    for assignment in range(1 << len(free)):
        value = sum(((assignment >> j) & 1) << i for j, i in enumerate(free))
        for pivot in sorted(reduced):
            coefficients, rhs = reduced[pivot]
            value |= (rhs ^ parity((coefficients ^ (1 << pivot)) & value)) << pivot
        solutions.append(value)
    require(all(parity(row & x) == rhs for x in solutions for row, rhs in rows),
            "affine solutions independently satisfy equations")
    return tuple(solutions)


def inherited(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)
    source = Path(root)/"verification/v774_arf_spinor_compiler.py"
    spec = importlib.util.spec_from_file_location("charged_lift_arf", source)
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    # Extract the actual standard doubled E8 basis from the pinned source AST.
    assignments = [node.value for node in ast.walk(ast.parse(source.read_text()))
                   if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == "B_STD" for t in node.targets)]
    require(len(assignments) == 1, "unique inherited standard E8 basis")
    basis = tuple(ast.literal_eval(assignments[0]))
    return src, basis


def build(root=ROOT):
    src, basis = inherited(root)
    in_lattice = lambda x: len({v % 2 for v in x}) == 1 and sum(x) % 4 == 0
    lat = src.make_lattice(in_lattice, list(basis))
    reps = src.label_group(lat)
    zero = lat["label"]((0,)*8)
    sigma_label = lambda v: lat["label"](src.sig_vec(reps[v]))
    _, bits = src.family_anchor_basis(lat, reps, zero, sigma_label)
    gram = tuple(tuple(src.ip(x, y)//4 for y in basis) for x in basis)
    require(all(src.ip(x, y) % 4 == 0 for x in basis for y in basis), "integral physical lattice Gram")
    det, _ = src.mat_det_inv(gram)
    require(det == 1 and all(gram[i][i] % 2 == 0 for i in range(8)), "even unimodular source lattice")
    physical = lambda word: tuple(sum(basis[j][i] for j in range(8) if word >> j & 1) for i in range(8))
    pairing_rows = tuple(bitmask(row) for row in gram)
    pair_products = tuple(linear(pairing_rows, x) for x in range(256))
    beta = lambda x, y: parity(pair_products[x] & y)
    q = lambda x: sum(gram[i][j] for i in range(8) for j in range(8)
                      if x >> i & 1 and x >> j & 1)//2 % 2
    c_rows = tuple(sum((gram[i][j] % 2) << j for j in range(i))
                   | ((gram[i][i]//2 % 2) << i) for i in range(8))
    c_products = tuple(linear(c_rows, x) for x in range(256))
    cocycle = lambda x, y: parity(c_products[x] & y)
    jcols = tuple(bitmask(lat["coords"](src.J_vec(b))) for b in basis)
    sigcols = tuple(bitmask(lat["coords"](src.sig_vec(b))) for b in basis)
    jmap, sigmap = lambda x: linear(jcols, x), lambda x: linear(sigcols, x)
    nmap = lambda x: x ^ jmap(x)
    projection = {x: bitmask(bits[lat["label"](physical(x))]) for x in range(256)}
    kernel = {x for x in range(256) if projection[x] == 0}
    kbasis = independent_basis(sorted(kernel))
    seed = tuple(next(x for x in range(256) if projection[x] == 1 << i) for i in range(4))
    qcompiler = lambda x: sum(src.iota(bitword(x, 4)))//2 % 2
    bcompiler = lambda x, y: src.hb(bitword(x, 4), bitword(y, 4))
    sigma4 = lambda x: bitmask(src.sig_bits(bitword(x, 4)))
    return dict(src=src, basis=basis, lat=lat, gram=gram, physical=physical,
                beta=beta, q=q, cocycle=cocycle, jmap=jmap, sigmap=sigmap,
                nmap=nmap, projection=projection, kernel=kernel, kbasis=kbasis,
                seed=seed, qcompiler=qcompiler, bcompiler=bcompiler, sigma4=sigma4)


def compiler_lifts(data):
    beta, q = data["beta"], data["q"]
    seed, kbasis = data["seed"], data["kbasis"]
    variables = 16  # a kernel vector for each of four section columns
    conditions = []
    for i in range(4):
        row = sum(beta(seed[i], kbasis[a]) << (4*i+a) for a in range(4))
        conditions.append((row, q(seed[i]) ^ data["qcompiler"](1 << i)))
    for i in range(4):
        for j in range(i):
            row = sum(beta(kbasis[a], seed[j]) << (4*i+a) for a in range(4))
            row |= sum(beta(seed[i], kbasis[a]) << (4*j+a) for a in range(4))
            conditions.append((row, beta(seed[i], seed[j]) ^ data["bcompiler"](1 << i, 1 << j)))
    solutions = affine_solutions(conditions, variables)
    sections = tuple(tuple(seed[i] ^ linear(kbasis, (sol >> (4*i)) & 15)
                           for i in range(4)) for sol in solutions)
    for section in sections:
        require(all(data["projection"][linear(section, v)] == v
                    and q(linear(section, v)) == data["qcompiler"](v) for v in range(16)),
                "section preserves inherited projection and quadratic form")
        require(all(beta(linear(section, v), linear(section, w)) == data["bcompiler"](v, w)
                    for v in range(16) for w in range(16)), "section preserves compiler pairing")
    equivariant = tuple(section for section in sections
                        if all(data["sigmap"](linear(section, v))
                               == linear(section, data["sigma4"](v)) for v in range(16)))
    return sections, equivariant


def descent_certificate(d):
    beta, q, project = d["beta"], d["q"], d["projection"]
    kernel = d["kernel"]
    require(len(kernel) == 16 and len(set(project.values())) == 16, "256 to 16 Gaussian quotient")
    require(all(d["jmap"](d["jmap"](x)) == x
                and d["sigmap"](d["sigmap"](d["sigmap"](x))) == x
                and project[d["jmap"](x)] == project[x]
                and project[d["sigmap"](x)] == d["sigma4"](project[x])
                and q(d["jmap"](x)) == q(x) == q(d["sigmap"](x)) for x in range(256)),
            "actual deck and family quotient actions and quadratic invariance")
    require({d["nmap"](x) for x in range(256)} == kernel
            == {x for x in range(256) if d["nmap"](x) == 0}, "image and kernel of 1+J agree")
    require(all(q(x) == 0 and beta(x, y) == 0 for x in kernel for y in kernel), "Gaussian kernel totally singular")
    require({x for x in range(256) if all(beta(x, y) == 0 for y in range(256))} == {0},
            "charged commutator form has zero radical modulo 2L")
    require(all(beta(x, d["nmap"](y)) == d["bcompiler"](project[x], project[y])
                for x in range(256) for y in range(256)), "compiler form is charged pairing with (1+J)y")
    require(sum(q(x) == 0 for x in range(256)) == 136, "full mod-two E8 form is Arf zero")
    y, z = (2, 0, 2, 0, 0, 0, 0, 0), (2, 0, 0, 0, 2, 0, 0, 0)
    other = tuple(-a for a in d["src"].J_vec(y))
    gap = tuple(a-b for a, b in zip(y, other))
    require(all(d["lat"]["in"](x) and d["src"].ip(x, x) == 8 for x in (y, other, z)),
            "three actual norm-two lattice roots")
    ym, om, zm, km = (bitmask(d["lat"]["coords"](x)) for x in (y, other, z, gap))
    require(project[ym] == project[om] != 0 and project[km] == 0,
            "same nonzero compiler label for two actual roots")
    require(beta(ym, zm) == 1 and beta(om, zm) == 0 and beta(km, zm) == 1,
            "root-level charged cocycle non-descent witness")
    return {"root_y_doubled": y, "root_other_doubled": other, "test_root_z_doubled": z,
            "same_compiler_label": bitword(project[ym], 4), "cocycle_commutator_signs": [-1, 1],
            "Gaussian_quotient_preserves_charged_commutator": False,
            "scalar_coboundary_can_repair_commutator": False,
            "smallest_additive_commutator_quotient": "L/2L", "quotient_bits": 8,
            "Gaussian_kernel_bits": 4, "full_quadratic_zeros": 136,
            "compiler_is_configuration_quotient_not_charged_algebra_quotient": True}


def symmetry_certificate(d, sections, equivariant):
    require(len(sections) == 64 and len(equivariant) == 4, "complete 64 lifts and four sigma-equivariant lifts")
    for sec in sections:
        image = tuple(d["jmap"](x) for x in sec)
        require(image in sections and span(image) == {x for x in range(256)
                    if all(d["beta"](x, y) == 0 for y in sec)}, "all 64 lifts have deck complement")
    deck = []
    for sec in equivariant:
        image = tuple(d["jmap"](x) for x in sec)
        require(image in equivariant and image != sec, "deck exchanges distinct sigma lifts")
        complement = {x for x in range(256) if all(d["beta"](x, y) == 0 for y in sec)}
        require(span(image) == complement, "J-image is exact charged orthogonal complement")
        require(span(sec) & complement == {0} and len(span(sec+image)) == 256, "two factors generate all charge signs")
        require(sum(d["q"](x) == 0 for x in complement) == 6, "complement is also Arf one")
        deck.append(equivariant.index(image))
    require(not any(all(d["jmap"](x) == x for x in sec) for sec in sections),
            "no section intertwines the trivial quotient deck with the actual lattice deck")
    return {"all_projection_and_q_preserving_sections": 64,
            "sigma_equivariant_sections": equivariant, "sigma_equivariant_section_count": 4,
            "deck_permutation_on_sections": deck, "unordered_deck_paired_splittings": 2,
            "J_equivariant_section_count": 0,
            "split_real_algebra": "M2(H) tensor M2(H) = M16(R)",
            "one_factor_commutant_dimension": 16, "joint_factor_commutant_dimension": 1,
            "unique_physical_spin_factor_selected": False,
            "microscopic_net_prime_completion_proved": False}


def coherent_deck_lifts(d):
    """Lift both lattice isometries to the sign algebra, retaining cocycle phases."""
    c, j, sig = d["cocycle"], d["jmap"], d["sigmap"]
    def phase_for(transform):
        difference = {(i, k): c(transform(1 << i), transform(1 << k)) ^ c(1 << i, 1 << k)
                      for i in range(8) for k in range(i)}
        phase = {x: sum(value for (i, k), value in difference.items() if x >> i & 1 and x >> k & 1) % 2
                 for x in range(256)}
        require(all((phase[x] ^ phase[y] ^ phase[x ^ y]) == (c(transform(x), transform(y)) ^ c(x, y))
                    for x in range(256) for y in range(256)), "isometry lift preserves all cocycle products")
        return phase
    pj, ps = phase_for(j), phase_for(sig)
    require(all(ps[x] ^ ps[sig(x)] ^ ps[sig(sig(x))] == 0 for x in range(256)), "sigma lift order three")
    mismatch = {x: pj[x] ^ ps[j(x)] ^ ps[x] ^ pj[sig(x)] for x in range(256)}
    require(sum(mismatch.values()) == 128, "unsigned choice of independent lifts is not coherent")
    # Correct J by a character, preserving its square and keeping sigma fixed.
    rows = []
    for i in range(8):
        x = 1 << i
        rows.extend(((x ^ sig(x), mismatch[x]), (x ^ j(x), 0)))
    choices = affine_solutions(rows, 8)
    require(len(choices) == 4, "four character corrections in this phase gauge")
    chosen = min(choices)  # deterministic convention, not a physical selector
    corrected = {x: pj[x] ^ parity(chosen & x) for x in range(256)}
    square = {x: corrected[x] ^ corrected[j(x)] for x in range(256)}
    require(sum(square.values()) == 128, "finite deck lift square is nontrivial")
    require(all(corrected[x] ^ ps[j(x)] ^ ps[x] ^ corrected[sig(x)] == 0
                for x in range(256)), "coherent deck and sigma lifts commute")
    require(all(square[x] ^ square[j(j(x))] == 0 for x in range(256)), "deck lift order four")
    return corrected, ps, {"deck_order_on_binary_labels": 2, "deck_order_on_sign_algebra": 4,
                          "sigma_order_on_sign_algebra": 3, "coherent_lifts_commute": True,
                          "initial_independent_lift_mismatch_count": 128,
                          "character_corrections_in_declared_gauge": sorted(choices),
                          "selected_character_convention": chosen,
                          "microscopic_seam_phase_normalization_identified": False}


def schrodinger_representation(d):
    """Construct a minimal real 16D representation of the standard sign cocycle."""
    beta, q, kbasis = d["beta"], d["q"], d["kbasis"]
    dbasis = []
    for i in range(4):
        candidates = [x for x in range(256) if q(x) == 0
                      and all(beta(k, x) == int(i == j) for j, k in enumerate(kbasis))
                      and all(beta(x, y) == 0 for y in dbasis)]
        require(bool(candidates), "isotropic dual basis exists")
        dbasis.append(candidates[0])
    coords = {linear(dbasis, u) ^ linear(kbasis, v): (u, v) for u in range(16) for v in range(16)}
    require(len(coords) == 256, "four canonical position/momentum pairs")
    canon = lambda x, y: parity(coords[x][1] & coords[y][0])
    require(all(q(x) == parity(coords[x][0] & coords[x][1]) for x in range(256)), "hyperbolic q coordinates")
    difference = {(i, j): d["cocycle"](1 << i, 1 << j) ^ canon(1 << i, 1 << j)
                  for i in range(8) for j in range(i)}
    phase = {x: sum(bit for (i, j), bit in difference.items() if x >> i & 1 and x >> j & 1) % 2
             for x in range(256)}
    require(all((phase[x] ^ phase[y] ^ phase[x ^ y]) == (d["cocycle"](x, y) ^ canon(x, y))
                for x in range(256) for y in range(256)), "all 65536 cocycle coboundary cells")
    # On |t>: (-1)^phase(x) X^u Z^v |t>; a signed permutation, no floats.
    matrices = {x: tuple((t ^ coords[x][0], (-1)**(phase[x] ^ parity(coords[x][1] & t)))
                         for t in range(16)) for x in range(256)}
    for x in range(256):
        for y in range(256):
            sign = (-1)**d["cocycle"](x, y)
            target = matrices[x ^ y]
            for t, (intermediate, sy) in enumerate(matrices[y]):
                row, sx = matrices[x][intermediate]
                require((row, sx*sy) == (target[t][0], sign*target[t][1]), "all 65536 matrix products, every column")
    traces = {x: sum(sign for t, (row, sign) in enumerate(m) if row == t) for x, m in matrices.items()}
    require(traces[0] == 16 and all(traces[x] == 0 for x in range(1, 256)), "Pauli trace orthogonality and faithful full algebra")
    return matrices, {"representation_dimension": 16, "real_algebra_dimension": 256,
                      "minimal_complex_representation_dimension": 16,
                      "verified_products": 65536, "verified_product_columns": 1048576,
                      "verified_coboundary_cells": 65536,
                      "charge_Pauli_pairs": 4, "added_arbitrary_spectator": False,
                      "finite_sign_representation_is_full_vertex_field": False}


def embedded_clifford(d, matrices, equivariant, sigma_phase, root=ROOT):
    import sympy as s
    path = Path(root)/"experiments/theory-contracts/compiler-clifford-bridge/checker.py"
    spec = importlib.util.spec_from_file_location("charged_lift_old_bridge", path)
    bridge = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bridge)
    def matrix(word):
        out = s.zeros(16)
        for col, (row, sign) in enumerate(matrices[word]):
            out[row, col] = sign
        return out
    for sec in equivariant:
        signs = (1, (-1)**sigma_phase[sec[0]], (-1)**(sigma_phase[sec[0]] ^ sigma_phase[sec[1]]), 1)
        require(all(signs[i]*(-1)**sigma_phase[sec[i]] == signs[(i+1) % 3] for i in range(3))
                and sigma_phase[sec[3]] == 0, "operator-level sigma cycle after explicit generator rephasing")
        fr = bridge.frame(tuple(sign*matrix(x) for sign, x in zip(signs, sec)))
        require(((s.eye(16)+fr["chi"])/2).rank() == 8
                and ((s.eye(16)-fr["chi"])/2).rank() == 8, "embedded Clifford has both Weyl sectors")
        require(all(matrix(x)*matrix(y) == matrix(y)*matrix(x)
                    for x in sec for y in (d["jmap"](v) for v in sec)), "commuting deck-paired Clifford factors")
    return {"all_four_compiler_frames_embedded": True, "embedded_Weyl_ranks": [8, 8],
            "net_Weyl_chirality": 0, "SM_gauge_commutation_established": False,
            "spacetime_spin_identification_established": False}


def charged_shift(d, charge, vector):
    """Exact zero-mode translation on the finite-support core of ell^2(L)."""
    out = {}
    for state, amplitude in vector.items():
        target = tuple(a+b for a, b in zip(state, charge))
        out[target] = (-1)**d["cocycle"](bitmask(charge), bitmask(state))*amplitude
    return {x: a for x, a in out.items() if a}


def energy(d, state):
    return Fraction(sum(state[i]*d["gram"][i][j]*state[j] for i in range(8) for j in range(8)), 2)


def charge_dot(d, left, right):
    return sum(left[i]*d["gram"][i][j]*right[j] for i in range(8) for j in range(8))


def zero_mode_certificate(d, extra_charge=10**6):
    zero = (0,)*8
    roots = ((2, 0, 2, 0, 0, 0, 0, 0), (2, 0, 0, 0, 2, 0, 0, 0))
    charges = tuple(d["lat"]["coords"](x) for x in roots)
    states = (zero, charges[0], tuple(-3*x for x in charges[1]),
              (extra_charge, -extra_charge, 2, -3, 5, -7, 11, -13))
    cells = 0
    for alpha in charges:
        require(energy(d, alpha) == 1, "charged root conformal zero-mode weight one")
        for state in states:
            shifted = tuple(x+y for x, y in zip(state, alpha))
            require(energy(d, shifted)-energy(d, state) == charge_dot(d, alpha, state)+energy(d, alpha),
                    "exact [H0,U_alpha] charge Ward identity")
            for axis in range(8):
                h = tuple(int(j == axis) for j in range(8))
                require(charge_dot(d, h, shifted)-charge_dot(d, h, state) == charge_dot(d, h, alpha),
                        "exact [P_h,U_alpha] charge Ward identity")
                cells += 1
            for beta in charges:
                original = {state: Fraction(1)}
                lhs = charged_shift(d, alpha, charged_shift(d, beta, original))
                rhs = charged_shift(d, tuple(a+b for a, b in zip(alpha, beta)), original)
                sign = (-1)**d["cocycle"](bitmask(alpha), bitmask(beta))
                require(lhs == {x: sign*a for x, a in rhs.items()}, "full integer-lattice central-extension action")
    doubled = tuple(2*x for x in charges[0])
    require(bitmask(doubled) == 0 and energy(d, doubled) == 4, "finite sign quotient does not retain zero-mode energy")
    # Any finite unitary replacement violates U* P U - P = (h.alpha) I
    # when h.alpha != 0: trace(left)=0, trace(right)=dimension*(h.alpha).
    return {"charge_Ward_cells": cells, "large_integer_charge_control": extra_charge,
            "finite_charge_cutoff": False, "Hilbert_space": "ell^2(L), with finite-support common core",
            "zero_mode_action_constructed": True,
            "finite_sign_alias_energies": [0, 4],
            "finite_unitary_matrix_can_preserve_nonzero_charge_Ward_identity": False,
            "joint_zero_mode_charge_and_shift_commutant": "scalars (proof in README)",
            "oscillator_fields_or_microscopic_seam_limit_constructed": False,
            "physical_spatial_derivatives_derived": False}


def explore(root=ROOT):
    d = build(root)
    all_sections, equivariant = compiler_lifts(d)
    return {"Gram": d["gram"], "kernel_size": len(d["kernel"]),
            "kernel_basis": d["kbasis"], "q_zeros": sum(d["q"](x) == 0 for x in range(256)),
            "all_sections": len(all_sections), "sigma_sections": equivariant,
            "deck_images": [tuple(d["jmap"](x) for x in sec) for sec in equivariant],
            "complement_equals_deck": [span(tuple(d["jmap"](x) for x in sec))
                == {x for x in range(256) if all(d["beta"](x, y) == 0 for y in sec)} for sec in equivariant]}


def run(root=ROOT):
    d = build(root)
    descent = descent_certificate(d)
    sections, equivariant = compiler_lifts(d)
    symmetry = symmetry_certificate(d, sections, equivariant)
    _, sigma_phase, coherent = coherent_deck_lifts(d)
    matrices, representation = schrodinger_representation(d)
    return {"verdict": "CHARGED_SIGN_REFINEMENT_AND_DECK_PAIRED_CLIFFORD_LIFTS_EXACT_PHYSICAL_BRIDGE_OPEN",
            "source_pins": PINS, "non_descent": descent, "lift_classification": symmetry,
            "coherent_cocycle_symmetries": coherent,
            "minimal_sign_representation": representation,
            "embedded_clifford": embedded_clifford(d, matrices, equivariant, sigma_phase, root),
            "full_lattice_zero_modes": zero_mode_certificate(d),
            "T1_T8_closed": [], "RH_in_scope": False,
            "full_TOE_or_common_3plus1D_parent_constructed": False,
            "sources": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ("checker.py", "test_checker.py", "README.md")}}


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
