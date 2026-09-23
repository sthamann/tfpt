#!/usr/bin/env python3
"""Minimal exact check of the conditional c-branch flavor tensor."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
checks: Counter[str] = Counter()

PINS = {
    ROOT / "local_modules/PROOF.md":
        "5d458c5fe3ceabfd12b5f637cff1fcad3ea0f618ba0e23d898bcbf6f9ba0ba00",
    ROOT / "local_modules/certificate.json":
        "9d4f000ec16cfdc6e54e8226ac556192195c1a03b57c033081ec8815d058bd9e",
    ROOT / "critical_review/REVIEW.md":
        "6be13b4fcb16ac68c0b267bda02ebd993dcea1bea1d2951d7980c52e2d5ab817",
    ROOT / "critical_review/field_table.json":
        "32ae92fd4767db883de301d1b3f8fe6cee9420a5b906b4c5f1e33618354b0add",
    ROOT / "critical_review/validation.json":
        "3a17ddb7008347082f3213972e176a78379ec885dae0a688632d7c7acde270b2",
    REPO / "experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py":
        "380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672",
    REPO / "experiments/theory-contracts/source-graded-locality-20260920/PROOF.txt":
        "669309ea7f240397b2eb49c61e02b5224d4b9d1c15d50aeca30668fa97fa41bb",
    REPO / "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/certificate.json":
        "150f27876e19fba789b497d53b1dc02b3d9f2f02704b991cc214cfc8e0ab51eb",
    REPO / "experiments/theory-contracts/source-flavor-origin-20260920/certificate.optimized.json":
        "3efa28973698464e873b0ae2bde82469a73e1f1bf3543c85a33e63bfe931a9ca",
    REPO / "experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt":
        "03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2",
}


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def portable_pin_name(path: Path) -> str:
    """Serialize package- or repository-relative pin names, never host paths."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path.relative_to(REPO))


def permutation_sign(indices: tuple[int, int, int, int]) -> int:
    inversions = sum(indices[i] > indices[j]
                     for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


def hodge_matrix(H: dict[tuple[int, int], sp.Expr]) -> sp.Matrix:
    """Y_ab=sum_(c<d) epsilon_abcd H_cd: Lambda2(bar4)->6."""
    Y = sp.zeros(4)
    for a, b in combinations(range(4), 2):
        value = 0
        for c, d in combinations(range(4), 2):
            if len({a, b, c, d}) == 4:
                value += permutation_sign((a, b, c, d)) * H[(c, d)]
        Y[a, b], Y[b, a] = value, -value
    return Y


def main() -> None:
    for path, wanted in PINS.items():
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        require(got == wanted, f"pin:{path.parent.name}/{path.name}")

    modules = json.loads((ROOT / "local_modules/certificate.json").read_text())
    fields = json.loads((ROOT / "critical_review/field_table.json").read_text())
    native_text = (REPO / (
        "experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/"
        "native_source.py"
    )).read_text()
    cubic = json.loads((REPO / (
        "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/"
        "certificate.json"
    )).read_text())
    source_flavor = json.loads((REPO / (
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "certificate.optimized.json"
    )).read_text())
    require(modules["explicit_odd_c_fields"]["family_type"] == "(16,bar4)" and
            modules["explicit_odd_c_fields"]["Delta_Vc"] == "3/2",
            "conditional local odd c field is (16,bar4) at Delta 3/2")
    require(modules["not_claimed"][1] ==
            "h=3/2 is a four-dimensional Weyl scaling dimension",
            "Delta 3/2 remains one-plus-one-dimensional")
    c_rows = [row for row in fields["fields"]
              if row["class"] == "f+b" and row["representative"].startswith("x_c")]
    require(len(c_rows) == 2 and all(row["parity"] == "odd" for row in c_rows),
            "critical review retains both local odd c representatives")

    # Exact orientation audit of the implemented old S+ summand.  In the
    # fixed local_modules convention, even D5/D3 minus parity is
    # (bar16,bar4); global root conjugation gives the absent (16,4) partner.
    require("EVEN16 = [m for m in range(32) if m.bit_count() % 2 == 0]" in native_text and
            "for m in range(8) if m.bit_count() % 2 == 0" in native_text and
            "FW = np.array" in native_text and
            "W = np.zeros((60, 2016)" in native_text,
            "pinned native W uses FW64 and the 10x6 mediator")
    require("COLORS = list(combinations(range(4), 2))" in native_text,
            "native family mediator is Lambda2(bar4)=6 in FW convention")
    even16 = [mask for mask in range(32) if mask.bit_count() % 2 == 0]
    cw = [[1 - 2 * ((mask >> j) & 1) for j in range(3)]
          for mask in range(8) if mask.bit_count() % 2 == 0]
    fw = [[1 - 2 * ((mask >> j) & 1) for j in range(5)] + family
          for mask in even16 for family in cw]
    fw_parities = Counter((sum(value < 0 for value in weight[:5]) % 2,
                           sum(value < 0 for value in weight[5:]) % 2)
                          for weight in fw)
    conjugate_parities = Counter((sum(value > 0 for value in weight[:5]) % 2,
                                  sum(value > 0 for value in weight[5:]) % 2)
                                 for weight in fw)
    require(fw_parities == {(0, 0): 64} and
            conjugate_parities == {(1, 1): 64},
            "FW64 is old S+ (bar16,bar4); its global conjugate is (16,4)")
    require(not ({tuple(weight) for weight in fw} &
                 {tuple(-value for value in weight) for weight in fw}),
            "implemented FW64 does not contain its global conjugate")
    require(modules["oriented_D5_A3"]["s_even"] ==
            ["(16,4)", "(bar16,bar4)"] and
            "lambda=(+1/2)^8 is in (bar16,bar4)" in
            modules["oriented_D5_A3"]["orientation"],
            "FW census uses the fixed local_modules orientation convention")

    # The real structure of (10,6) conjugates both tensor factors at once:
    # (k,{a,b}) -> (k+5,{a,b}^c).  It therefore relates a down-type
    # component to an up-type component of complementary family grade; it
    # does not relate the two family triplets while holding k fixed.
    pairs = list(combinations(range(4), 2))
    pair_index = {pair: i for i, pair in enumerate(pairs)}
    # In native CW order (+++),(--+),(-+-),(+--), the bar4 grades are
    # (+3,-1,-1,-1): anchor first.  This is read directly as the signed
    # twice-weight sum, not assumed from the convenient later ordering.
    qbar4_native = [sum(weight) for weight in cw]
    require(qbar4_native == [3, -1, -1, -1],
            "native CW order is bar4 with anchor at index zero")
    q6_native = [qbar4_native[a] + qbar4_native[b] for a, b in pairs]
    bar = []
    simultaneous_flips = []
    for channel in range(60):
        spin10, color = divmod(channel, 6)
        pair = pairs[color]
        complement = tuple(i for i in range(4) if i not in pair)
        partner = 6 * ((spin10 + 5) % 10) + pair_index[complement]
        bar.append(partner)
        simultaneous_flips.append(
            partner // 6 != spin10 and
            q6_native[partner % 6] == -q6_native[color]
        )
    require(all(simultaneous_flips),
            "real structure flips Spin10 and U1F on all 60 channels")
    require(all(bar[bar[channel]] == channel for channel in range(60)),
            "native boson real structure is an involution")
    require(not any(bar[channel] // 6 == channel // 6 for channel in range(60)),
            "reality never supplies complementary family component at fixed Spin10 weight")

    roots = cubic["cubic"]["base_roots_doubled"]
    y5 = [sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2
    hypercharge = lambda root: sum(y * value for y, value in zip(y5, root[:5])) / 2
    require(roots[12][:5] == [-value for value in roots[14][:5]] and
            hypercharge(roots[12]) == -sp.Rational(1, 2) and
            hypercharge(roots[14]) == sp.Rational(1, 2),
            "actual neutral H_d index12 and H_u index14 are opposite Spin10 weights")
    require(sum(c["higgs"] == "d" for c in source_flavor["native_Higgs_couplings"]) == 4 and
            sum(c["higgs"] == "u" for c in source_flavor["native_Higgs_couplings"]) == 4,
            "actual 45 cubic contains both neutral up and down slots")
    require(cubic["cubic"]["factorization"] ==
            "C_(A,i)(B,j)(C,k) = d_ABC epsilon_ijk",
            "actual source family factor is A2 epsilon, not a selected SU4 real six background")

    # Branching count for the new odd-total-minus D8 half-spinor class.
    counts = {(0, 1): 0, (1, 0): 0}
    for mask in range(256):
        if mask.bit_count() % 2 == 0:
            continue
        key = ((mask & 0b11111).bit_count() % 2,
               ((mask >> 5) & 0b111).bit_count() % 2)
        if key not in counts:
            raise RuntimeError("odd D8 half-spinor did not have opposite D5/D3 chirality")
        counts[key] += 1
    require(counts == {(0, 1): 64, (1, 0): 64},
            "c branch splits as 64 plus 64 with opposite family orientation")

    # For the formulas below, explicitly permute native CW by [1,2,3,0]
    # so the family triplet precedes the anchor.  In this declared basis
    # bar4=bar3_(-1)+1_(+3), while its global conjugate is
    # 4=3_(+1)+1_(-3).  No native source selection of this SU3 subgroup is
    # inferred from the notation.
    permutation = [1, 2, 3, 0]
    qbar4 = [qbar4_native[index] for index in permutation]
    q4 = [-value for value in qbar4]
    require(qbar4 == [-1, -1, -1, 3] and q4 == [1, 1, 1, -3],
            "declared triplet-first basis is native permutation 1,2,3,0")
    grade_matches = []
    for a, b in pairs:
        complement = tuple(i for i in range(4) if i not in (a, b))
        grade_matches.append(
            qbar4[a] + qbar4[b] == q4[complement[0]] + q4[complement[1]]
        )
    require(all(grade_matches), "Hodge map conserves declared family-Cartan grade")

    h0, h1, h2, k0, k1, k2 = sp.symbols("h0 h1 h2 k0 k1 k2")
    H = {pair: sp.Integer(0) for pair in pairs}
    # H_i4 is the 3_(-2) output selected by two bar3 matter weights.
    H[(0, 3)], H[(1, 3)], H[(2, 3)] = h0, h1, h2
    # H_ij is the bar3_(+2) output selected by bar3 x anchor.
    H[(1, 2)], H[(0, 2)], H[(0, 1)] = k0, -k1, k2
    Y = hodge_matrix(H)
    h = sp.Matrix([h0, h1, h2])
    k = sp.Matrix([k0, k1, k2])
    A = sp.Matrix([[0, h2, -h1], [-h2, 0, h0], [h1, -h0, 0]])
    expected = A.row_join(k).col_join((-k.T).row_join(sp.zeros(1)))
    require(Y == expected and Y.T == -Y,
            "forced conjugate-family tensor is Hodge-dual skew 4x4 matrix")
    require(A * h == sp.zeros(3, 1) and A.det() == 0,
            "one fixed-grade conjugate-family Higgs triplet retains rank-two null h")
    require(A.subs({h0: 1, h1: 0, h2: 0}).rank() == 2,
            "generic one-triplet family block has rank two")
    require(sp.factor(Y.det()) == (h0 * k0 + h1 * k1 + h2 * k2) ** 2,
            "two opposite-grade triplets can conditionally give full family-plus-anchor rank")
    require(Y.subs({h0: 1, h1: 0, h2: 0,
                    k0: 1, k1: 0, k2: 0}).rank() == 4,
            "nonorthogonal two-triplet witness has rank four")

    # A stronger, separable reality ansatz H_(10,6)=v_10 tensor H_6 with
    # both factors individually real would give k=conjugate(h) and hence
    # a positive determinant.  This is an algebraic counterexample to a
    # rank-two theorem for a full real six, but it is not implied by BAR,
    # nor selected by the pinned A2 source cubic.
    r0, r1, r2, i0, i1, i2 = sp.symbols("r0 r1 r2 i0 i1 i2", real=True)
    hc = sp.Matrix([r0 + sp.I * i0, r1 + sp.I * i1, r2 + sp.I * i2])
    kc = hc.conjugate()
    dot_norm = sp.expand((hc.T * kc)[0])
    require(dot_norm == sum(value ** 2 for value in (r0, r1, r2, i0, i1, i2)),
            "separable real-six ansatz would set k=conjugate h")
    require(sp.factor((hc.T * kc)[0] ** 2) == dot_norm ** 2,
            "conditional separable real-six determinant is norm h to fourth")

    # An existing neutral internal mark repairs combined coefficient symmetry,
    # but it cannot populate the absent opposite U1_F triplet or change rank.
    d = sp.Matrix([[0, 1], [1, 0]])
    S = sp.diag(1, -1)
    one_triplet = Y.subs({k0: 0, k1: 0, k2: 0})
    combined = sp.kronecker_product(S * d, one_triplet)
    require((S * d).T == -(S * d) and combined.T == combined,
            "existing internal mark repairs exchange symmetry on c branch")
    require(one_triplet.rank() == 2,
            "internal mark does not lift one-triplet family rank")
    grade6 = sp.diag(2, 2, 2, -2, -2, -2)
    background = sp.Matrix([k2, -k1, k0, h0, h1, h2])
    h_only = background.subs({k0: 0, k1: 0, k2: 0})
    require(all((grade6 ** power * h_only)[:3, :] == sp.zeros(3, 1)
                for power in range(1, 4)),
            "family-Cartan grade mark cannot create the opposite triplet")

    result = {
        "research_id": "UR.SOURCE.CRITICAL_C_FLAVOR_REVIEW.20260920",
        "status": "PASS_EXACT_BOUNDED",
        "verdict": "CONDITIONAL_ODD_FIELD; FIXED_CHANNEL_ONE_TRIPLET_RANK_TWO; FULL_REAL_SIX_ROUTE_UNSELECTED",
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "source_pins": {portable_pin_name(path): digest
                        for path, digest in PINS.items()},
        "forced_branch": "(16,bar4)+(bar16,4)",
        "forced_tensor": "representation map W_- = Hodge: Lambda2(bar4)->6; not the implemented FW operator without global conjugation",
        "native_FW_orientation": {
            "implemented_summand": "(bar16,bar4)",
            "global_conjugate": "(16,4)",
            "conjugate_present_in_FW64": False,
            "declared_family_cartan_grades_in_native_CW_order": [3, -1, -1, -1],
            "triplet_first_permutation": [1, 2, 3, 0],
            "map_to_new_c": "new (16,bar4) differs by D5 chirality from FW64, or by family dual from global-conjugate (16,4); neither is a derived physical intertwiner",
        },
        "one_triplet_map": "A(h)_ij=epsilon_ijk h_k, rank 2, null h; h labels a triplet and the bar on bar4 is representation notation",
        "second_component": "opposite declared family-Cartan triplet k couples bar3 matter to SU3 singlet anchor",
        "conditional_full_matrix": "[[A(h),k],[-k^T,0]], det=(h dot k)^2",
        "reality_test": {
            "native_BAR": "(H_d,{a,b})* is paired with (H_u,{a,b} complement)",
            "fixed_channel_consequence": "does not force k=conjugate(h) inside H_d or H_u",
            "stronger_separable_ansatz": "would give k=conjugate(h), det=norm(h)^4",
            "source_status": "not selected by the native BAR or the pinned E6 x A2 45 cubic",
        },
        "source_status": {
            "local_odd_c_field": "conditional at selected Vc and critical tuning",
            "selected_source_energy": "does not reach Vc; direct V0-to-Vaux midpoint has Delta_n=Delta_z=2",
            "H_10_6_representation": "native",
            "W_minus_on_c_fields": "representation-forced relative to globally conjugated old (16,4), but not implemented in pinned FW64=(bar16,bar4) operator",
            "opposite_grade_background_k": "not selected",
            "heavy_anchor_or_three-family_reduction": "not derived",
        },
        "decision": "new module repairs the conditional statistics/field leg; a full-real-six rank route exists algebraically but is not source-selected",
        "complete_mass_rank_gap": False,
    }
    (HERE / "critical_flavor_certificate.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps({
        "status": result["status"], "verdict": result["verdict"],
        "checks": result["checks"],
        "certificate": str(HERE / "critical_flavor_certificate.json")
    }, sort_keys=True))


if __name__ == "__main__":
    main()
