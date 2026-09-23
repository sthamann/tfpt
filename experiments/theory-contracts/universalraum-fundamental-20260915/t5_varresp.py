"""Charged response on N=64 variational state (parent-direct). NON-RH. No repo writes.

|psi> = a|F> + b|B_A>, |F> = filled 64 (Nf=64,Nb=0),
|B_A> = b†_A P_A|F>/sqrt8 (Nf=62,Nb=1), (a,b) = lower 2x2 eigenvector of
[[0,g√8],[g√8,D]].  Fermions as 64-bit masks,chen linear JW order 0..63.
Computes hole norms ||f_r|psi>||^2 and 2-point G_rs = <psi|f†_s f_r|psi>.
BEDINGT: variational state, NOT the true N=64 GS (GS still open).
"""
import numpy as np
from hashlib import sha256
from itertools import combinations

TENSOR = '/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
assert sha256(open(TENSOR, 'rb').read()).hexdigest() == PIN
W = np.load(TENSOR, allow_pickle=False)['W'].real.astype(np.int64)
pairs = list(combinations(range(64), 2))

D, g = 1.0, 1.0 / 20.0
A0 = 0  # reference boson channel
Om = np.sqrt(D**2 + 32 * g**2)
Emin = (D - Om) / 2
# lower eigenvector of [[0,g√8],[g√8,D]]
x = -np.sqrt(8) * g / Emin
a, b = x / np.sqrt(x**2 + 1), -1.0 / np.sqrt(x**2 + 1)
print(f'2x2: E={Emin:.6f} a={a:.6f} b={b:.6f} <Nb>=b^2={b**2:.6f}')

FULL = (1 << 64) - 1


def sign_below(mask, r):
    n = bin(mask & ((1 << r) - 1)).count('1')
    return -1.0 if n % 2 else 1.0


# P_A0|F> = sum over 8 disjoint pairs p: W_p (ff)_p |F>  (two-hole dets)
terms = []  # (coeff, mask)
for c in np.flatnonzero(W[A0]):
    i, j = pairs[int(c)]
    v = int(W[A0, int(c)])
    m = FULL ^ (1 << i) ^ (1 << j)
    s = sign_below(FULL ^ (1 << j), i) * sign_below(FULL, j)
    terms.append((v * s, m))
nP2 = sum(c * c for c, _ in terms)  # cross terms vanish (distinct dets)
print(f'||P|F>||^2 = {nP2} (expect 8)')
assert nP2 == 8

# f_r|psi> = a f_r|F> + b/sqrt8 b† f_r P|F>; bosonic parts orthogonal (Nb 0 vs 1)
# G_rs = a^2 <F|f†_s f_r|F> + b^2/8 <P F|f†_s f_r|P F>  (cross Nb terms vanish)
G = np.zeros((64, 64))
for r in range(64):
    for s_ in range(64):
        val = a * a * (1.0 if r == s_ else 0.0)
        # <P F| f†_s f_r |P F> = sum over term pairs
        acc = 0.0
        fr = []  # f_r|term>: list of (coeff, mask)
        fs = []
        for c, m in terms:
            if (m >> r) & 1:
                fr.append((c * sign_below(m, r), m ^ (1 << r)))
            if (m >> s_) & 1:
                fs.append((c * sign_below(m, s_), m ^ (1 << s_)))
        d = {m: c for c, m in fs}
        for c, m in fr:
            if m in d:
                acc += c * d[m]
        val += b * b / 8.0 * acc
        G[r, s_] = val

print(f'G diagonal: min={np.diag(G).min():.6f} max={np.diag(G).max():.6f} (filled-state value 1)')
print(f'G off-diag absmax={np.abs(G-np.diag(np.diag(G))).max():.6f}')
print(f'G symmetric: {np.allclose(G,G.T)} eigmin={np.linalg.eigvalsh(G).min():.6f} (must be >=0)')
print(f'sum diag(G) = {np.trace(G):.6f} (= <Nf> = {64*a*a+62*b*b:.6f})')
# hole spectral weight per mode: ||f_r|psi>||^2 = G_rr
w = np.diag(G)
print(f'hole weight: modes with w<0.999: {int(np.sum(w<0.999))}/64, min={w.min():.6f}')
