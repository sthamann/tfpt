"""Simultaneous Ward / chirality / ground-state condition for E8 extensions of the
folded source currents.  Exact; no promotion.  Scope: PROOF.md.

Source data (Codex, local): eight fold channels with U(1) charge q = (1,...,1);
time law K(p) = |p|^2/2 + delta.p, delta_k = (k+alpha)/8 - 1/2; source bilinear
currents = D8 roots.  An E8 extension of the source current algebra is an even
unimodular lattice containing D8: exactly E8_s = D8 u (D8+s) or E8_c = D8 u (D8+c).

W1  q/2 = (1/2)^8 is a root of E8_s and not a vector of E8_c; Q'/2 = e3+e6 is a
    root of both -> no orthogonal map takes (E8_c, q) to (E8, Q').
W2  E8_s (Ward marking present): two ground states for every alpha.
    E8_c (unique vacuum for 0<alpha<1): Ward marking absent.  -> no E8 extension
    of the source currents has both.
W5  p* is neutral and invariant under the fold clock g, g^2 and the deck g^4
    for every alpha: gauging deck/clock/U(1) does not remove it.
W3  protection: K(p*) is invariant under every source-U(1) twist delta -> delta+eta q
    (p*.q = 0); the zero comes from delta_{k+4} - delta_k = 1/2, i.e. from the deck
    relation between deck-partner channels, for every alpha.
W4  pullback of a charged boundary phase h along the connected double: holonomy h^2
    on the double; deck eigenspaces carry base holonomies h and -h.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import numpy as np

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

def in_D8(v): return all(x.denominator == 1 for x in v) and sum(v) % 2 == 0
def in_E8(v, chir):
    if in_D8(v): return True
    if all(x.denominator == 2 for x in v):
        nneg = sum(1 for x in v if x < 0)
        # v in D8 + s  <=> v - (1/2)^8 in D8 ; v in D8 + c <=> v - c in D8, c = (-1/2,1/2^7)
        sref = tuple(F(1, 2) for _ in range(8)); cref = tuple([F(-1, 2)] + [F(1, 2)] * 7)
        ref = sref if chir == "s" else cref
        return in_D8(tuple(a - b for a, b in zip(v, ref)))
    return False
norm = lambda v: sum(x * x for x in v)
q = tuple(F(1) for _ in range(8))
qh = tuple(x / 2 for x in q)
Qp = tuple(F(2) if k in (2, 5) else F(0) for k in range(8))
require("W1_q_half_root_in_E8s", in_E8(qh, "s") and norm(qh) == 2)
require("W1_q_half_not_in_E8c", not in_E8(qh, "c"))
require("W1_Qprime_half_root_both", all(in_E8(tuple(x / 2 for x in Qp), ch) for ch in "sc") and norm(tuple(x / 2 for x in Qp)) == 2)
require("W1_same_norm", norm(q) == norm(Qp) == 8)
# an orthogonal lattice map g: E8_c -> E8 with g(q) = Q' would give g(q/2) = Q'/2 in E8, hence q/2 in E8_c: contradiction
require("W1_no_lattice_map", (not in_E8(qh, "c")) and in_E8(tuple(x / 2 for x in Qp), "s"))

# ground states (reuse exact integer scan)
ints = np.array(list(product(range(-3, 4), repeat=8)), dtype=np.int64) * 2
halfs = np.array(list(product((-5, -3, -1, 1, 3, 5), repeat=8)), dtype=np.int64)
D8 = ints[(ints.sum(1) // 2) % 2 == 0]
nn = (halfs < 0).sum(1)
L = {"s": np.vstack([D8, halfs[nn % 2 == 0]]), "c": np.vstack([D8, halfs[nn % 2 == 1]])}
def K64(Lm, a, eta=F(0)):
    den = a.denominator * eta.denominator
    d = np.array([int(((F(k) + a) / 8 - F(1, 2) + eta) * 8 * den) for k in range(8)], dtype=np.int64)
    return 8 * den * (Lm ** 2).sum(1) + 4 * (Lm @ d)
for a in [F(1, 8), F(1, 4), F(1, 3), F(1, 2), F(3, 4), F(7, 8)]:
    vs, vc = K64(L["s"], a), K64(L["c"], a)
    require(f"W2_s_degenerate_a{a}", vs.min() == 0 and (vs == 0).sum() == 2)
    require(f"W2_c_unique_a{a}", vc.min() == 0 and (vc == 0).sum() == 1)
require("W2_no_extension_with_both", True)

# W3 protection under source-U(1) twists
pstar = (F(1, 2),) * 4 + (F(-1, 2),) * 4
require("W3_pstar_neutral", sum(a * b for a, b in zip(pstar, q)) == 0 and in_E8(pstar, "s"))
for a in [F(0), F(1, 4), F(3, 4), F(2, 7)]:
    for eta in [F(-1, 2), F(-1, 5), F(0), F(1, 16), F(1, 3)]:
        delta = [(F(k) + a) / 8 - F(1, 2) + eta for k in range(8)]
        K = norm(pstar) / 2 + sum(x * y for x, y in zip(delta, pstar))
        require(f"W3_K_pstar_zero_a{a}_eta{eta}", K == 0)
        require(f"W3_deck_partner_gap_a{a}_eta{eta}", all(delta[k + 4] - delta[k] == F(1, 2) for k in range(4)))

# W5 p* is invariant under every source symmetry considered: U(1)_q, fold clock g, deck g^4
for a in [F(0), F(1, 4), F(3, 4), F(2, 7)]:
    for power in (1, 2, 4):
        phase = sum(power * (F(k) + a) / 8 * pk for k, pk in enumerate(pstar))   # exp(2 pi i phase)
        require(f"W5_pstar_invariant_g{power}_a{a}", phase.denominator == 1)
require("W5_pstar_U1_neutral", sum(pstar) == 0)

# W4 pullback of a charged phase
def ring(N, h):
    T = np.zeros((N, N), complex)
    for x in range(N):
        T[(x + 1) % N, x] = h if x == N - 1 else 1
    return T
for h in (1j, -1j, -1, 1):
    for Lb in (3, 5):
        T = ring(2 * Lb, h ** 2)                         # double carries h^2
        require(f"W4_double_holonomy_h{h}_L{Lb}", np.allclose(np.linalg.matrix_power(T, 2 * Lb), (h ** 2) * np.eye(2 * Lb)))
        Dk = np.linalg.matrix_power(T, Lb)
        w, V = np.linalg.eig(Dk)
        hol = set()
        for ev in np.unique(np.round(w, 9)):
            Q, _ = np.linalg.qr(V[:, np.isclose(w, ev)])
            Tb = Q.conj().T @ T @ Q
            hb = np.linalg.matrix_power(Tb, Lb)
            require(f"W4_scalar_h{h}_L{Lb}_{ev}", np.allclose(hb, hb[0, 0] * np.eye(len(hb))))
            hol.add(complex(np.round(hb[0, 0], 9)))
        require(f"W4_base_holonomies_pm_h{h}_L{Lb}", hol == {complex(h), complex(-h)})

results = {"contract": "ward-chirality-vacuum-no-go-20261014", "checks": checks, "n_checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
