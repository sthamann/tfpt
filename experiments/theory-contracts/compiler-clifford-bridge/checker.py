"""NON-RH: exact sigma/Arf-to-Clifford bridge, not a physical bulk construction.

The ordered cocycle is an algebraic representative, not an identified charged
seam cocycle. Formal momenta and the inherited overlap regulator remain inputs.
All certificate guards survive python -OO. Frozen research sources are read-only.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "verification/v774_arf_spinor_compiler.py": "3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c",
    "verification/v775_gaussian_class_d5_purity.py": "f6d503b943d202465e69cd40606572d42eedde7c06af4201db65be539817d2f6",
    "verification/v783_two_qubit_clifford.py": "8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4",
    "verification/v975_dimension_selector_4d.py": "e9e31593b4a2eb4c15384f83a936aeee1474fcce5f2702a6df37147800407673",
    "verification/v14_carrier_uniqueness.py": "68bcdb41dc122a548cb1d3e304c25b2cf4e3a82ae3c9eb47e3d99d772ef1b1e4",
    "verification/v252_full_finite_triple.py": "820254440e178430422e50605067775656236602996307f67c9e69124ba5d163",
    "verification/v1027_signed_det_car_wall.py": "6679297c3c53a86f4ef7d40c169caab64708885e891e68db365acfadfe9f0f4d",
    "verification/v1028_gauss_d4_cap.py": "6884f4bc116c15920a6d7d1669a438a2c7b232f5334ef3156c9585bd93cc6b98",
}
V = tuple(itertools.product((0, 1), repeat=4))
ZERO = (0, 0, 0, 0)
UNIT = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
I4, O4 = s.eye(4), s.zeros(4)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    root = Path(root)
    for name, digest in PINS.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)
    modules = []
    for suffix, name in (("arf", "v774_arf_spinor_compiler.py"),
                         ("weights", "v1028_gauss_d4_cap.py")):
        spec = importlib.util.spec_from_file_location("bridge_source_"+suffix,
                                                      root/"verification"/name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    return tuple(modules)


def xor(*words):
    return tuple(sum(column) % 2 for column in zip(*words))


def cocycle(v, w):
    # Ordered monomials in g1,g2,g3,g4; every gi^2=-1.
    return (sum(v[i]*w[i] for i in range(4))
            + sum(v[i]*w[j] for i in range(4) for j in range(i))) % 2


def finite_data(src, sigma=None, offset=ZERO):
    sigma = src.sig_bits if sigma is None else sigma
    require(tuple(src.W16) == V, "inherited 16-word register")
    q = {v: (sum(src.iota(v))//2 + src.hb(v, offset)) % 2 for v in V}
    require(all(q[xor(v, w)] == (q[v]+q[w]+src.hb(v, w)) % 2
                for v in V for w in V), "quadratic polarization")
    require(all(q[sigma(v)] == q[v] for v in V)
            and q[src.A_BIT] == 1 and q[src.FSIG] == 0, "frozen q selector")
    refinements = [{v: (q[v]+src.hb(v, z)) % 2 for v in V} for z in V]
    selected = [r for r in refinements if all(r[sigma(v)] == r[v] for v in V)
                and r[src.A_BIT] == 1 and r[src.FSIG] == 0]
    require(selected == [q], "unique frozen refinement")
    pfix = {v: xor(v, sigma(v), sigma(sigma(v))) for v in V}
    pmov = {v: xor(sigma(v), sigma(sigma(v))) for v in V}
    fix, mov = tuple(sorted(set(pfix.values()))), tuple(sorted(set(pmov.values())))
    require(len(fix) == len(mov) == 4 and set(fix) & set(mov) == {ZERO},
            "sigma fixed/moving plane dimensions")
    require(all(pfix[pfix[v]] == pfix[v] and pmov[pmov[v]] == pmov[v]
                and xor(pfix[v], pmov[v]) == v for v in V), "complementary projectors")
    require(set(fix) == {ZERO, src.A_BIT, src.FSIG, xor(src.A_BIT, src.FSIG)},
            "fixed plane is anchor/family-sum plane")
    require(all(src.hb(v, w) == 0 for v in fix for w in mov), "orthogonal planes")
    for plane in (fix, mov):
        require(all(any(src.hb(v, w) for w in plane) for v in plane if v != ZERO),
                "nondegenerate plane")
    require(sum(q[v] == 0 for v in fix) == 3 and sum(q[v] == 0 for v in mov) == 1,
            "split Arf types zero/one")
    require(sum(q[v] == 0 for v in V) == 6, "total Arf-one type")
    require(all(cocycle(v, v) == q[v] for v in V), "cocycle diagonal is inherited q")
    require(all((cocycle(v, w)+cocycle(w, v)) % 2 == src.hb(v, w)
                for v in V for w in V), "cocycle commutator is inherited b")
    require(all((cocycle(u, v)+cocycle(xor(u, v), w)) % 2
                == (cocycle(v, w)+cocycle(u, xor(v, w))) % 2
                for u in V for v in V for w in V), "all 4096 associativity cells")
    return {"q": q, "fixed": fix, "moving": mov, "pfix": pfix, "pmov": pmov}


def generators():
    x, y, z, eye = s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1), s.eye(2)
    return (s.I*s.kronecker_product(x, eye), s.I*s.kronecker_product(z, eye),
            s.I*s.kronecker_product(y, x), s.I*s.kronecker_product(y, z))


def monomial(word, gen):
    out = s.eye(gen[0].rows)
    for bit, generator in zip(word, gen):
        if bit:
            out = out*generator
    return out


def regular_generator(label):
    # Independent faithful real 16-dimensional left-regular representation.
    out = s.zeros(16)
    indices = {v: i for i, v in enumerate(V)}
    for j, word in enumerate(V):
        out[indices[xor(label, word)], j] = (-1)**cocycle(label, word)
    return out


def frame(gen=None, reverse_third_unit=False):
    gen = generators() if gen is None else gen
    eye, zero = s.eye(gen[0].rows), s.zeros(gen[0].rows)
    a, f = gen[3], gen[0]*gen[1]*gen[2]
    u = (gen[0]*gen[1], gen[1]*gen[2], gen[2]*gen[0])
    if reverse_third_unit:
        u = (u[0], u[1], -u[2])
    require(a*a == -eye and f*f == eye and a*f == -f*a, "fixed-plane split algebra")
    for j in range(3):
        require(u[j]*u[j] == -eye and u[j]*u[(j+1) % 3] == u[(j+2) % 3],
                "oriented quaternion multiplication")
        require(a*u[j] == u[j]*a and f*u[j] == u[j]*f, "commuting tensor factors")
    lorentz = (f,) + tuple(a*f*v for v in u)
    euclidean = (f,) + tuple(a*v for v in u)
    for matrices, signature in ((lorentz, (1, -1, -1, -1)), (euclidean, (1, 1, 1, 1))):
        for i in range(4):
            for j in range(4):
                require(matrices[i]*matrices[j]+matrices[j]*matrices[i]
                        == (2*signature[i]*eye if i == j else zero), "Clifford anticommutators")
    require(lorentz[0]*lorentz[1]*lorentz[2]*lorentz[3] == a, "Lorentz oriented volume")
    alpha = tuple(f*g for g in lorentz[1:])
    chi = s.I*a
    require(chi*chi == eye and -s.I*alpha[0]*alpha[1]*alpha[2] == chi,
            "Hamiltonian chirality orientation")
    require(all(chi*v == v*chi for v in alpha), "chirality commutes with alpha")
    return {"a": a, "f": f, "u": u, "lorentz": lorentz, "euclidean": euclidean,
            "alpha": alpha, "chi": chi}


def algebra_certificate(src):
    gen = generators()
    basis = {v: monomial(v, gen) for v in V}
    require(all(basis[v]*basis[w] == (-1)**cocycle(v, w)*basis[xor(v, w)]
                for v in V for w in V), "all 256 matrix products")
    require(s.Matrix.hstack(*(m.reshape(16, 1) for m in basis.values())).rank() == 16,
            "faithful complexified algebra dimension 16")
    # Lift sigma by permuting generators, including ordered-word signs.
    permuted = (gen[1], gen[2], gen[0], gen[3])
    lift = {v: monomial(v, permuted) for v in V}
    phases = {}
    for v in V:
        phases[v] = 1 if lift[v] == basis[src.sig_bits(v)] else -1
        require(lift[v] == phases[v]*basis[src.sig_bits(v)], "signed sigma lift")
        require(phases[v]*(-1)**cocycle(src.sig_bits(v), src.sig_bits(v))
                == phases[v]*(-1)**cocycle(v, v), "sigma preserves q")
    for v in V:
        require(phases[v]*phases[src.sig_bits(v)]*phases[src.sig_bits(src.sig_bits(v))] == 1,
                "sigma lift order three")
    require(all(lift[v]*lift[w] == (-1)**cocycle(v, w)*lift[xor(v, w)]
                for v in V for w in V), "sigma lift is algebra automorphism")
    original, rotated = frame(gen), frame(permuted)
    require(rotated["a"] == original["a"] and rotated["f"] == original["f"],
            "sigma fixes anchor and family volume")
    for key in ("u", "alpha"):
        require(rotated[key] == original[key][1:] + original[key][:1], "sigma rotates " + key)
    require(rotated["lorentz"][1:] == original["lorentz"][2:] + original["lorentz"][1:2],
            "sigma rotates Lorentz spatial frame")
    require(rotated["euclidean"][1:] == original["euclidean"][2:] + original["euclidean"][1:2],
            "sigma also rotates Euclidean frame")
    regular = frame(tuple(regular_generator(v) for v in UNIT))
    require(regular["a"] != s.I*s.eye(16), "anchor is not the central complex deck scalar")
    return original, {"matrix_product_cells": 256, "sigma_product_cells": 256,
                      "sigma_negative_word_phases": sum(v == -1 for v in phases.values()),
                      "regular_real_dimension": 16, "complex_irrep_dimension": 4,
                      "real_algebra": "M2(R) tensor H = M2(H)",
                      "Lorentz_signature": [1, -1, -1, -1],
                      "equally_sigma_equivariant_Euclidean_signature": [1, 1, 1, 1],
                      "unique_physical_signature_selected": False}


def symbols_and_wall(fr):
    p0, p1, p2, p3, energy, x = s.symbols("p0 p1 p2 p3 energy x", real=True)
    momenta = (p1, p2, p3)
    radius2 = sum(p*p for p in momenta)
    kinetic = sum((p*m for p, m in zip(momenta, fr["alpha"])), O4)
    dirac = sum((p*m for p, m in zip((p0,)+momenta, fr["lorentz"])), O4)
    require(s.expand(kinetic*kinetic) == radius2*I4, "formal spatial symbol square")
    require(s.expand(dirac*dirac) == (p0*p0-radius2)*I4, "formal Lorentz symbol square")
    require(s.factor(dirac.det()) == (p0*p0-radius2)**2, "formal Dirac determinant")
    require(all(g.H == g for g in fr["alpha"]) and fr["chi"].H == fr["chi"], "Hermitian alpha and chi")
    require(fr["lorentz"][0].H == fr["lorentz"][0]
            and all(g.H == -g for g in fr["lorentz"][1:]), "Lorentz adjoints")
    ranks = []
    for sign in (1, -1):
        projector = (I4+sign*fr["chi"])/2
        require(projector*projector == projector and projector.rank() == 2, "rank-two Weyl projector")
        require(projector*fr["alpha"][0]*fr["alpha"][1]*fr["alpha"][2]
                == sign*s.I*projector, "opposite Weyl orientations")
        ranks.append(projector.rank())
    h = s.Matrix([[x+x*x/4, x/2], [x/2, 4]])
    low = x+s.Rational(3, 16)*x*x-s.Rational(1, 64)*x**3
    residual = s.expand((h-energy*s.eye(2)).det().subs(energy, low))
    require(all(residual.coeff(x, j) == 0 for j in range(4)), "inherited wall low Taylor branch")
    matrix_low = kinetic+s.Rational(3, 16)*kinetic**2-s.Rational(1, 64)*kinetic**3
    require(all(matrix_low.diff(p).subs(dict.fromkeys(momenta, 0)) == alpha
                for p, alpha in zip(momenta, fr["alpha"])), "wall preserves compiler linear jet")
    return {"Dirac_square": "(p0^2-|p|^2) I4", "Dirac_determinant": "(p0^2-|p|^2)^2",
            "Weyl_block_ranks": ranks, "Weyl_orientations": [1, -1],
            "wall_low_series": str(low), "wall_linear_jet_preserved": True,
            "momenta_are_formal_inputs": True, "physical_derivatives_derived": False,
            "net_chiral_matter_constructed": False}


def overlap_bridge(fr):
    # Re-express v1027's existing free vectorlike construction, not a new parent.
    beta = fr["lorentz"][0]
    gamma = tuple(-s.I*g for g in fr["lorentz"][1:])
    require(all(g.H == g and s.I*beta*g == alpha for g, alpha in zip(gamma, fr["alpha"])),
            "overlap linear symbol equals compiler alpha")
    xs = s.symbols("x1:4", real=True)  # xj=1-cos(kj), each in [0,2]
    w = sum(xs)-1
    rad2 = sum(2*x-x*x for x in xs)+w*w
    require(s.expand(rad2) == 1+2*sum(xs[i]*xs[j] for i in range(3) for j in range(i)),
            "uniform Wilson radius square identity")
    zeros = []
    for bits in itertools.product((0, 1), repeat=3):
        corner_w = 2*sum(bits)-1
        corner_a = beta*(1+s.Rational(corner_w, abs(corner_w)))
        require(corner_a == (O4 if sum(bits) == 0 else 2*beta), "exact corner operator")
        if corner_a == O4:
            zeros.append(list(bits))
    # Exact non-corner check with rational unit-circle parametrization on 27 points.
    for ts in itertools.product((s.Rational(-1, 2), s.Integer(0), s.Rational(2, 3)), repeat=3):
        cosines = tuple((1-t*t)/(1+t*t) for t in ts)
        sine = tuple(2*t/(1+t*t) for t in ts)
        wilson = sum(1-c for c in cosines)-1
        radius = s.sqrt(sum(t*t for t in sine)+wilson*wilson)
        op = beta*(I4+(wilson*I4+s.I*sum((t*g for t, g in zip(sine, gamma)), O4))/radius)
        require(op.H == op, "exact overlap Hermiticity")
        require(s.simplify(op*op-2*(1+wilson/radius)*I4) == O4, "exact overlap square")
    return {"inherited_regulator_mass": 1, "radius_bounds": [1, 5],
            "zero_corners": zeros, "exact_noncorner_checks": 27,
            "compiler_alpha_equals_overlap_linear_jet": True,
            "same_existing_free_vectorlike_ansatz": True,
            "spatial_lattice_and_regulator_derived_from_TFPT": False,
            "original_scalar_U1_parent_modified": False,
            "charged_quantum_link_extension_proved_here": False}


def gauge_boundary(src, weights):
    # Internal half-spinor weight labels, not four-dimensional spacetime spinors.
    charge_counts = Counter(sum(x*y for x, y in zip((-2, -2, -2, 3, 3), src.iota(v))) for v in V)
    require(charge_counts == Counter(w[3] for w in weights.WEIGHTS), "inherited SM hypercharge census")
    require(charge_counts == Counter({1: 6, -4: 3, 2: 3, -3: 2, 6: 1, 0: 1}), "six SM charge blocks")
    ec_dim = 3*charge_counts[6]
    require(ec_dim == 3 and (-1)**ec_dim == -1, "odd three-family e-conjugate block")
    # If X,Y commute with hypercharge, their restrictions preserve this block.
    # X^2=Y^2=1 gives nonzero determinants; XY=-YX would imply det(XY)=-det(XY).
    require(ec_dim % 2 != 0, "odd-dimensional invertible anticommutator obstruction")
    return {"sixY_one_generation_counts": dict(sorted(charge_counts.items())),
            "three_generation_internal_labels": 48, "sixY_equals_6_block_dimension": ec_dim,
            "gauge_commuting_Pauli_triple_on_internal_labels_possible": False,
            "obstruction": "two invertible anticommuting operators cannot preserve an odd-dimensional charge block",
            "scope": "ordinary factorized one-particle spin action on exactly three internal generations",
            "emergent_interacting_spin_ruled_out": False,
            "v775_rootclass_matter_purity_restored": False,
            "extra_spinor_tensor_factor_physically_derived": False}


def run(root=ROOT):
    src, weights = inherited(root)
    data = finite_data(src)
    fr, algebra = algebra_certificate(src)
    return {"verdict": "EXACT_COMPILER_CLIFFORD_BRIDGE_WITH_PHYSICAL_EMBEDDING_OPEN",
            "source_pins": PINS,
            "finite_split": {"fixed_plane": data["fixed"], "moving_plane": data["moving"],
                             "Arf_types": [0, 1], "quadratic_zeros": 6, "associativity_cells": 4096},
            "algebra": algebra, "formal_symbols": symbols_and_wall(fr),
            "existing_overlap_bridge": overlap_bridge(fr), "internal_spin_boundary": gauge_boundary(src, weights),
            "T1_T8_closed": [], "RH_in_scope": False, "physical_shared_parent_constructed": False,
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
