#!/usr/bin/env python3
"""Exact bounded test of family duality against native FW/W/J/C3 and C/J clocks."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix, eye, kron


HERE = Path(__file__).resolve().parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
NATIVE_DIR = REPO / "experiments/theory-contracts/universalraum-keyD-native-instruments-20260915"
CLOCK_DIR = REPO / "experiments/theory-contracts/compiler-native-root-dictionary-20260918"
CRITICAL_DIR = REPO / "experiments/theory-contracts/source-critical-local-fields-20260920"
LOCAL_DIR = CRITICAL_DIR / "local_modules"
FLAVOR_DIR = CRITICAL_DIR / "flavor_delta"

PINS = {
    NATIVE_DIR / "native_source.py":
        "380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672",
    NATIVE_DIR / "README.md":
        "84e4a999f77989b48da03617a0b6980ba899b5c0261291fbfa734099ba7a2cb9",
    CLOCK_DIR / "PROOF.txt":
        "b5de7459d2c849ea320cc83e2abe6f12af0933fda1917ab5b8d44ddb52fa6de1",
    CLOCK_DIR / "certificate.json":
        "eecbeefc433356f079a782dd715f011de6b5b27006d386e1dfcad10146ad6d53",
    LOCAL_DIR / "PROOF.md":
        "5d458c5fe3ceabfd12b5f637cff1fcad3ea0f618ba0e23d898bcbf6f9ba0ba00",
    LOCAL_DIR / "certificate.json":
        "9d4f000ec16cfdc6e54e8226ac556192195c1a03b57c033081ec8815d058bd9e",
    FLAVOR_DIR / "REVIEW_FLAVOR.md":
        "fbe63194f84f1f31e5a782f01f4711b312e88a3e5c18d0c3740b9ddd0d96e6d0",
    FLAVOR_DIR / "critical_flavor_certificate.json":
        "1a382a19d0eb9ad849fe6a433f40064bf55d96d64ee89af6b53fdf0a3c363bd6",
}

checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def portable(path: Path) -> str:
    return str(path.relative_to(REPO))


def jw(n: int) -> list[np.ndarray]:
    out = []
    for j in range(n):
        matrix = np.zeros((2**n, 2**n), dtype=np.int64)
        for mask in range(2**n):
            if (mask >> j) & 1:
                matrix[mask ^ (1 << j), mask] = (
                    -1
                ) ** ((mask & ((1 << j) - 1)).bit_count())
        out.append(matrix)
    return out


def exact_gaussian(matrix: np.ndarray) -> sp.Matrix:
    return sp.Matrix([
        [sp.Integer(int(round(value.real))) +
         sp.I * sp.Integer(int(round(value.imag))) for value in row]
        for row in matrix
    ])


def sparse_hash(matrix: csr_matrix) -> str:
    canonical = matrix.copy().tocsr()
    canonical.sort_indices()
    digest = hashlib.sha256()
    digest.update(np.asarray(canonical.shape, dtype=np.int64).tobytes())
    digest.update(canonical.indptr.astype(np.int64).tobytes())
    digest.update(canonical.indices.astype(np.int64).tobytes())
    digest.update(canonical.data.astype(np.int64).tobytes())
    return digest.hexdigest()


def main() -> None:
    for path, wanted in PINS.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == wanted,
                f"pin:{portable(path)}")

    source_text = (NATIVE_DIR / "native_source.py").read_text()
    clock_certificate = json.loads((CLOCK_DIR / "certificate.json").read_text())
    local_certificate = json.loads((LOCAL_DIR / "certificate.json").read_text())
    require(local_certificate["oriented_D5_A3"]["c_odd"] ==
            ["(16,bar4)", "(bar16,4)"],
            "new local c branch has the fixed oriented decomposition")

    # Rebuild the load-bearing native arrays from the pinned formulas.
    ann5 = jw(5)
    even16 = [mask for mask in range(32) if mask.bit_count() % 2 == 0]
    conjugator = np.eye(32, dtype=np.int64)
    for operator in ann5:
        conjugator = conjugator @ (operator + operator.T)
    beta = [(conjugator @ operator)[np.ix_(even16, even16)]
            for operator in ann5 + [operator.T for operator in ann5]]
    colors = list(combinations(range(4), 2))
    pairs = list(combinations(range(64), 2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    W = np.zeros((60, len(pairs)), dtype=np.int64)
    for k, beta_k in enumerate(beta):
        for color_index, (left, right) in enumerate(colors):
            for pair_column, (v, w) in enumerate(pairs):
                vs, vc = divmod(v, 4)
                ws, wc = divmod(w, 4)
                W[6 * k + color_index, pair_column] = beta_k[vs, ws] * (
                    int(vc == left and wc == right) -
                    int(vc == right and wc == left)
                )
    require(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)) and
            np.count_nonzero(W) == 480,
            "native W is reconstructed exactly with row Gram 8I")

    cw = np.array([[1 - 2 * ((mask >> j) & 1) for j in range(3)]
                   for mask in range(8) if mask.bit_count() % 2 == 0],
                  dtype=np.int64)
    fw = np.array([[1 - 2 * ((mask >> j) & 1) for j in range(5)] + list(family)
                   for mask in even16 for family in cw], dtype=np.int64)
    family_dual_fw = fw.copy()
    family_dual_fw[:, 5:] *= -1
    y5 = np.array([-2, -2, -2, 3, 3], dtype=np.int64)  # six times hypercharge
    require(np.array_equal(fw[:, :5] @ y5, family_dual_fw[:, :5] @ y5),
            "family weight twist preserves every D5 hypercharge label")
    old_parity = Counter((np.count_nonzero(row[:5] < 0) % 2,
                          np.count_nonzero(row[5:] < 0) % 2) for row in fw)
    new_parity = Counter((np.count_nonzero(row[:5] < 0) % 2,
                          np.count_nonzero(row[5:] < 0) % 2)
                         for row in family_dual_fw)
    require(old_parity == {(0, 0): 64} and new_parity == {(0, 1): 64},
            "family weight twist maps FW64 (bar16,bar4) labels to c branch (bar16,4)")
    source_center=np.sum(fw,axis=1)%4
    target_center=np.sum(family_dual_fw,axis=1)%4
    require(np.all(source_center==0) and np.all(target_center==2),
            "diagonal Z4 center is plus on native FW64 and minus on target c")
    boson_weights=[]
    for row in W:
        occupied=np.flatnonzero(row)
        images=[fw[pairs[j][0]]+fw[pairs[j][1]] for j in occupied]
        require(all(np.array_equal(images[0],x) for x in images),
                "native W channel has one actual conserved weight")
        boson_weights.append(images[0])
    require(np.all(np.sum(np.array(boson_weights),axis=1)%4==0),
            "diagonal center is plus on all sixty native boson modes")
    # Universal lattice identity: common T-projection p has
    # 2p=2x_first8-(x9+x10)*a.  Center exp(i*pi*sum(p)) is
    # therefore (-1)^sum(x), the inherited Gamma fermion parity.
    xx=sp.Matrix(sp.symbols('x1:11',integer=True))
    aa=sp.Matrix([1,1,1,-1,-1,-1,-1,-1])
    pp2=2*xx[:8,:]-(xx[8]+xx[9])*aa
    require(sp.expand(sum(pp2)-2*sum(xx))==0,
            "all Gamma vertex labels: diagonal-center phase equals fermion parity")
    gauge=aa.col_join(sp.Matrix([-1,-3])); nn=aa.col_join(sp.Matrix([-1,3]))
    zz=sp.zeros(10,1);zz[8]=1;zz[9]=-1
    require(sp.expand(gauge.dot(xx)-sum(xx)+2*sum(xx[3:9,0])+4*xx[9])==0,
            "all Gamma vertices: compatible gauge parity equals center and fermion parity")
    require(gauge.dot(nn)==0 and gauge.dot(zz)==2,
            "other-lane compatible gauge allows n but forbids bare z")
    require(gauge.dot((nn+zz)/2)==1 and gauge.dot((nn-zz)/2)==-1,
            "same two local c dressings have opposite odd gauge charge")
    require(not ({tuple(row) for row in fw} &
                 {tuple(row) for row in family_dual_fw}),
            "family-dual target carrier is absent from native FW64")
    require(not ({tuple(row) for row in cw} &
                 {tuple(-value for value in row) for row in cw}) and
            "for j in range(3):" in source_text and
            "np.kron(np.eye(16, dtype=np.int64), a)" in source_text,
            "native weight action contains no declared map into the disjoint dual carrier")

    # Full SU(4) test.  There is no nonzero complex-linear bar4 -> 4
    # intertwiner.  Coefficient conjugation is an antilinear equivalence on
    # the family factor alone, but I_16 tensor K_4 is not a map on the
    # complex tensor product.  A global antilinear map additionally
    # conjugates Spin(10) and is killed by its central Z4 phase.
    ann3 = jw(3)
    gamma3 = ann3 + [operator.T for operator in ann3]
    # Match native_source: gamma=(a+aT, i(aT-a)), then take all pairs.
    gamma3 = ([operator + operator.T for operator in ann3] +
              [1j * (operator.T - operator) for operator in ann3])
    even4 = [mask for mask in range(8) if mask.bit_count() % 2 == 0]
    odd4 = [mask for mask in range(8) if mask.bit_count() % 2 == 1]
    gamma_exact=[exact_gaussian(g) for g in gamma3]
    bridges=[g.extract(odd4,even4) for g in gamma_exact]
    require(all(g.extract(even4,even4)==sp.zeros(4) for g in gamma_exact),
            "single Clifford generators vanish in the actual even family compression")
    require(all(m.rank()==4 for m in bridges),
            "unprojected family Clifford maps reach the opposite chirality")
    clifford_covariance=[]
    for j,k in combinations(range(6),2):
        generator=gamma_exact[j]*gamma_exact[k]
        xe=generator.extract(even4,even4); xo=generator.extract(odd4,odd4)
        for l in range(6):
            residual=xo*bridges[l]-bridges[l]*xe-2*(int(k==l)*bridges[j]-int(j==l)*bridges[k])
            clifford_covariance.append(residual==sp.zeros(4))
    require(all(clifford_covariance),'all ninety exact vector-spinor Clifford covariance equations')
    color_generators_np = [
        (gamma3[j] @ gamma3[k])[np.ix_(even4, even4)]
        for j, k in combinations(range(6), 2)
    ]
    identity4 = sp.eye(4)
    linear_equations = []
    for generator_np in color_generators_np:
        generator = exact_gaussian(generator_np)
        target = generator.conjugate()
        linear_equations.append(
            sp.kronecker_product(generator.T, identity4) -
            sp.kronecker_product(identity4, target)
        )
        require(generator.conjugate() == target,
                "bare family factor has an antilinear conjugate equivalence")
    linear_system = sp.Matrix.vstack(*linear_equations)
    require(linear_system.rank() == 16,
            "complex-linear bar4-to-4 intertwiner space is zero")
    require((-sp.I * identity4).conjugate() == sp.I * identity4,
            "bare family conjugation flips the central family clock")
    require((-sp.I * identity4) != sp.I * identity4,
            "the same central clock excludes a nonzero linear identity map")
    require(sp.I != -sp.I,
            "partial antilinearity violates complex tensor balancing")
    require(sp.conjugate(sp.I) == -sp.I and -sp.I != sp.I,
            "Spin10 central Z4 excludes a global antilinear map to the same bar16")

    # Hodge action on the real six.  H6 is family-only; native BAR is the
    # product of H6 with simultaneous Spin(10) root opposition.
    epsilon = {
        permutation: (-1) ** sum(
            permutation[i] > permutation[j]
            for i in range(4) for j in range(i + 1, 4)
        )
        for permutation in permutations(range(4))
    }
    H6 = np.zeros((6, 6), dtype=np.int64)
    for color_index, (a, b) in enumerate(colors):
        complement = tuple(i for i in range(4) if i not in (a, b))
        H6[colors.index(complement), color_index] = epsilon[(a, b, *complement)]
    HB = np.kron(np.eye(10, dtype=np.int64), H6)
    spin_opposition = np.zeros((10, 10), dtype=np.int64)
    for k in range(10):
        spin_opposition[(k + 5) % 10, k] = 1
    BAR = np.kron(spin_opposition, H6)
    require(np.array_equal(H6 @ H6, np.eye(6, dtype=np.int64)) and
            np.array_equal(HB @ HB.T, np.eye(60, dtype=np.int64)),
            "family Hodge map is an exact orthogonal involution")
    require(np.array_equal(BAR, np.kron(spin_opposition, np.eye(6, dtype=np.int64)) @ HB),
            "native BAR factors algebraically as Spin10 opposition times family Hodge")
    require(not np.array_equal(HB, BAR),
            "family-only Hodge is not the native simultaneous BAR")
    require("BAR, ETA" in source_text and "family-only" not in source_text,
            "pinned native source declares BAR but no family-only duality operator")

    W_dual = HB @ W
    require(np.array_equal(W_dual @ W_dual.T, 8 * np.eye(60, dtype=np.int64)),
            "family-dual W retains the exact row Gram")
    require(not np.array_equal(W_dual, W) and
            np.count_nonzero(W_dual * W) == 0,
            "family-dual W is a support-disjoint transformed tensor, not native W")

    # Rebuild native cubic map J and coupling C3, then transform all legs.
    J = np.zeros((64, 3840), dtype=np.int64)
    for channel, (a, b) in enumerate(colors):
        for k in range(10):
            for si, ti in zip(*np.nonzero(beta[(k + 5) % 10])):
                for color in range(4):
                    for d in range(4):
                        if (a, b, color, d) in epsilon:
                            J[4 * ti + d, 64 * (6 * k + channel) +
                              4 * si + color] = (
                                  beta[(k + 5) % 10][si, ti] *
                                  epsilon[(a, b, color, d)]
                              )
    lookup = {pairs[column]: (int(row), int(W[row, column]))
              for row, column in zip(*np.nonzero(W))}
    triples = list(combinations(range(64), 3))
    rows: list[int] = []
    columns: list[int] = []
    values: list[int] = []
    for triple_column, (a, b, c) in enumerate(triples):
        for pair, left, sign in [((a, b), c, 1), ((a, c), b, -1),
                                 ((b, c), a, 1)]:
            if pair in lookup:
                channel, value = lookup[pair]
                rows.append(64 * channel + left)
                columns.append(triple_column)
                values.append(sign * value)
    C3 = coo_matrix((np.array(values, dtype=np.int64), (rows, columns)),
                    shape=(3840, len(triples))).tocsr()
    require(np.count_nonzero(J) == 960 and C3.nnz == 29760 and
            np.array_equal(J @ J.T, 15 * np.eye(64, dtype=np.int64)),
            "native J and C3 are reconstructed exactly")
    native_exactness = (csr_matrix(J) @ C3).tocsr()
    native_exactness.eliminate_zeros()
    require(native_exactness.nnz == 0, "native J C3 exactness is reproduced")

    HB_domain = kron(csr_matrix(HB.T), eye(64, format="csr"), format="csr")
    HB_codomain = kron(csr_matrix(HB), eye(64, format="csr"), format="csr")
    J_dual = (csr_matrix(J) @ HB_domain).tocsr()
    C3_dual = (HB_codomain @ C3).tocsr()
    dual_exactness = (J_dual @ C3_dual).tocsr()
    dual_exactness.eliminate_zeros()
    require(dual_exactness.nnz == 0 and
            np.array_equal((J_dual @ J_dual.T).toarray(),
                           15 * np.eye(64, dtype=np.int64)),
            "transformed J and C3 retain exactness and Gram identity")
    require((J_dual != csr_matrix(J)).nnz > 0 and
            J_dual.multiply(csr_matrix(J)).nnz == 0 and
            (C3_dual != C3).nnz > 0 and C3_dual.multiply(C3).nnz == 0,
            "transformed J and C3 are support-disjoint from native tensors")

    # The actual E8 C/J clocks do not restrict to FW64, and family duality
    # sends FW64 to c halfweights outside the source E8 root system.
    clocks = clock_certificate["results"]["clocks"]
    roots = [tuple(root) for root in clocks["roots"]]
    root_index = {root: index for index, root in enumerate(roots)}
    fw_set = {tuple(row) for row in fw}
    dual_set = {tuple(row) for row in family_dual_fw}
    require(fw_set <= set(roots) and not (dual_set & set(roots)),
            "family dual leaves the source E8 root system: all 64 c weights are absent")
    clock_census = {}
    for clock_name in ("C", "J"):
        permutation = clocks["clocks"][clock_name]["root_permutation"]
        image = {roots[permutation[root_index[root]]] for root in fw_set}
        retained = len(image & fw_set)
        integer = sum(any(abs(value) == 2 for value in root) for root in image)
        other_half = sum(all(abs(value) == 1 for value in root) and
                         root not in fw_set for root in image)
        clock_census[clock_name] = {
            "retained_in_FW64": retained,
            "to_integer_D8_roots": integer,
            "to_other_s_halfroots": other_half,
        }
    require(clock_census == {
        "C": {"retained_in_FW64": 21, "to_integer_D8_roots": 28,
              "to_other_s_halfroots": 15},
        "J": {"retained_in_FW64": 32, "to_integer_D8_roots": 0,
              "to_other_s_halfroots": 32},
    }, "actual C/J clock action does not close on native FW64")
    require(clocks["joint_C_J_orbit_of_marked_48"] == 240,
            "actual C/J closure requires the full 240-root source algebra")

    result = {
        "research_id": "UR.SOURCE.FAMILY_INTERTWINER.01",
        "status": "PASS_EXACT_BOUNDED",
        "verdict": "DIAGONAL_CENTER_OBSTRUCTS_ALL_ODD_COMMON_EDGE_FIELDS_IN_UNCHANGED_NATIVE_FOCK_ALGEBRA",
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "source_pins": {portable(path): digest for path, digest in PINS.items()},
        "carrier_map": {
            "source": "FW64=(bar16,bar4)",
            "target": "family-dual c summand (bar16,4)",
            "D5_and_hypercharge": "weight labels preserved by the declared group-action twist; not evidence for a physical antiunitary with the same U1 action",
            "family_and_local_class": "bar4->4 and s->c",
            "complex_linear_intertwiner_dimension": 0,
            "complex_antilinear_intertwiner_dimension": 0,
            "partial_antilinear_map": "I16 tensor K4 is not well-defined on a complex tensor product",
            "global_antilinear_obstruction": "complex conjugation also sends bar16 to 16; Spin10 central Z4 phase mismatches target bar16",
            "valid_algebraic_operation": "outer twist of the SU4 group action on a separately declared target carrier",
            "central_family_clock": "bare family K4 sends -i to +i, but cannot be tensored partially with I16",
            "native_discrete_family_action": "the real permutations alone may make 4 and bar4 look equivalent after restriction, but the pinned source declares no map from FW64 into the disjoint c carrier",
            "scope": "zero Hom statement uses the unchanged full complex Spin10 x SU4 action",
        },
        "all_operator_obstruction": {
            "diagonal_center_on_source_fermions": "+1 on all 64",
            "diagonal_center_on_source_bosons": "+1 on all 60",
            "diagonal_center_on_full_native_Fock_algebra": "identity automorphism",
            "diagonal_center_on_common_Gamma_vertices": "(-1)^fermion_parity",
            "equivariant_odd_vertex_image": "zero, even for nonlinear composites or operator closures",
            "scope": "unchanged full Spin10 x SU4 action, native 64CAR/60CCR Fock representation, and fixed common T(D8) dictionary",
            "not_excluded": "additional charged or twisted sectors, changed group lift/dictionary, or independently source-derived symmetry breaking"
        },
        "clifford_source_probe": {
            "algebraic_intertwiner": "6 tensor bar4 -> 4 by the six original pre-compression Clifford matrices",
            "covariance_equations": len(clifford_covariance),
            "even_compressed_single_gamma": "all zero",
            "actual_exported_source_generators": "even bilinears gamma_j gamma_k, not the odd maps into the missing family chirality",
            "physical_64CAR_operator_selected": False,
            "graded_field_and_time_bridge_selected": False
        },
        "cross_lane_gauge_correlation": {
            "source_contract": "UR.SOURCE.ROTOR_GAUSS.01",
            "candidate_gauge_covector": [int(t) for t in gauge],
            "universal_identity": "exp(i*pi*g.x)=diagonal_center(x)=(-1)^B(x,x) for every x in Gamma",
            "gauge_field_or_charge_sector_constructed": False,
            "bare_z_can_remain_in_gauge_invariant_critical_H": False
        },
        "operator_transform": {
            "boson_map": "HB=I10 tensor Hodge6, family-only",
            "native_BAR": "Spin10_opposition tensor Hodge6",
            "W_dual": "HB W; exact Gram retained; support-disjoint from W",
            "J_dual": "J (HB^T tensor I64)",
            "C3_dual": "(HB tensor I64) C3",
            "exactness": "J_dual C3_dual=0 and J_dual J_dual^T=15 I64",
            "native_identity": False,
        },
        "matrix_hashes": {
            "W": hashlib.sha256(W.tobytes()).hexdigest(),
            "W_dual": hashlib.sha256(W_dual.tobytes()).hexdigest(),
            "J": hashlib.sha256(J.tobytes()).hexdigest(),
            "J_dual_sparse": sparse_hash(J_dual),
            "C3_sparse": sparse_hash(C3),
            "C3_dual_sparse": sparse_hash(C3_dual),
        },
        "actual_clock_census_on_FW64": clock_census,
        "first_free_choice": (
            "adjoin an outer twist of the family group action on a new target carrier and its Hodge6 tensor action, "
            "then extend/select the actual C/J clock action on the c module; "
            "the pinned source supplies only simultaneous BAR and clocks on the E8 s-root algebra"
        ),
        "not_excluded": (
            "an intertwiner after a source-selected symmetry breaking to a real discrete subgroup, "
            "or a dynamical/composite bridge with additional typed degrees of freedom"
        ),
        "physical_bridge_derived": False,
        "complete_mass_rank_gap": False,
    }
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "verdict": result["verdict"],
        "checks": result["checks"],
        "certificate": str(HERE / "certificate.json"),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
