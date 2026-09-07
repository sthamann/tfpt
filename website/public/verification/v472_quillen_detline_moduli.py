"""v472 -- ALPHA.QUILLEN.DETLINE.01: occupied-state Berry line over the
U(1)-twist moduli of the finite collar model. Its FHS Chern integer
matches the Bloch Chern number. The continuum Quillen comparison stays open.

The SAME collar Hamiltonian
h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ (v367/v470)
is put in real space on an L x L torus with twisted boundary conditions.
Over the twist torus, P = 1_{(-infinity,0)}(H) defines the occupied bundle;
L_occ = det Ran P is its determinant (many-body ground-state) LINE.
The FHS links use local occupied frames. A gap defines a smooth projector
and a ground-state ray, not a global nonvanishing Slater-vector section.
A nonzero first Chern class excludes a global nonvanishing section of L_occ.
Keep the sign convention explicit: the FHS continuum convention is
C_Berry = integral F_occ/(2*pi*i), A_occ = trace(U^dagger dU).
With nabla = d + A_occ and c1 = i F_occ/(2*pi), c1[B] = -C_Berry.
Identifying a finite-mesh C_FHS with C_Berry also requires mesh control.

  [E] 1. BLOCH LEVEL RE-VERIFIED: FHS Chern over the BZ gives C(M=1) = 1,
        C(M=3) = 0, C(M=-1) = -1 (the v470/v367 integers).
  [E] 2. OCCUPIED BERRY LINE COMPUTED: twist-torus C_FHS = 1 at
        M = 1, to 1e-9, for L = 4 AND L = 6.
  [E] 3. CONTROLS: M = 3 gives 0 and M = -1 gives -1.
  [E] 4. TWO TORI, ONE INTEGER: twist and Bloch Chern numbers agree for
        all three M (the finite Niu-Thouless-Wu response check).
  [E] 5. SAMPLED GAP: the gap stays open at every sampled twist for M=1.
        The global bound also follows analytically from
        |d(k)|^2 = 1 + 2(1-cos kx)(1-cos ky) >= 1, hence gap >= 2.
        This neither constructs a Dai-Freed vector nor trivializes L_occ.
  [C] 6. INTEGRATED RESPONSE: |C_FHS| = k0 = 1 in this collar model.
        An integrated Chern number does not determine individual
        holonomies or identify the exact zeta-determinant variation.
  [O] 7. CONTINUUM COMPARISON: specify a chiral Fredholm family D^+,
        its Quillen line (including its zero locus), and a comparison
        with L_occ at the level of metrics and connections. A Dai-Freed
        vector requires filling data and lives in the pulled-back inverse
        boundary line. Norm-resolvent convergence and a gap alone do not
        control the ultraviolet contribution to a zeta determinant.
        ALPHA.QUILLEN.EXACT.01 stays [O]; the alpha-value claim is unchanged.

References: FHS JPSJ 74 (2005), Niu-Thouless-Wu PRB 31 (1985);
Quillen (1985), Bismut-Freed CMP 106 (1986), Dai-Freed JMP 35 (1994)
for the distinct continuum determinant-line structures.
Numerical routines: dense eigh and FHS on the twist grid.
"""
import numpy as np

from tfpt_constants import check, summary, reset

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)

# real-space hoppings reproducing h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ
TX = (-SZ - 1j * SX) / 2          # c^dag_{r+x} TX c_r + h.c.
TY = (-SZ - 1j * SY) / 2

N_GRID = 8                        # FHS grid on the twist torus
TOL = 1e-9


def _hamiltonian(L, M, thx, thy):
    """Collar model on an L x L torus with U(1) twists (thx, thy)."""
    n = L * L
    H = np.zeros((2 * n, 2 * n), complex)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for (dx, dy, T, th) in ((1, 0, TX, thx), (0, 1, TY, thy)):
                j = blk(x + dx, y + dy)
                phase = np.exp(1j * th) if (x + dx == L or y + dy == L) else 1.0
                H[j:j + 2, i:i + 2] += phase * T
                H[i:i + 2, j:j + 2] += np.conj(phase) * T.conj().T
    return H


def _occupied_frame(L, M, thx, thy):
    w, v = np.linalg.eigh(_hamiltonian(L, M, thx, thy))
    n_occ = int(np.sum(w < 0))
    return v[:, :n_occ], n_occ, w[n_occ] - w[n_occ - 1]


def detline_chern(L, M, n_grid=N_GRID):
    """FHS Chern number of the occupied-state Berry line over the twist
    torus. Returns (C, min_gap_on_sampled_twists); no global section test."""
    ths = np.linspace(0, 2 * np.pi, n_grid, endpoint=False)
    frames, min_gap, n_ref = {}, np.inf, None
    for i, tx in enumerate(ths):
        for j, ty in enumerate(ths):
            fr, n_occ, gap = _occupied_frame(L, M, tx, ty)
            frames[(i, j)] = fr
            min_gap = min(min_gap, gap)
            n_ref = n_occ if n_ref is None else n_ref
            assert n_occ == n_ref, "occupation jumped -- gap closed on the torus"

    def link(a, b):
        u = np.linalg.det(frames[a].conj().T @ frames[b])
        return u / abs(u)

    F = 0.0
    for i in range(n_grid):
        for j in range(n_grid):
            ip, jp = (i + 1) % n_grid, (j + 1) % n_grid
            F += np.angle(link((i, j), (ip, j)) * link((ip, j), (ip, jp))
                          * np.conj(link((i, jp), (ip, jp)))
                          * np.conj(link((i, j), (i, jp))))
    return F / (2 * np.pi), float(min_gap)


def bloch_chern(M, N=24):
    """v470's Bloch-BZ FHS Chern (verbatim convention)."""
    def occ(kx, ky):
        d = np.array([np.sin(kx), np.sin(ky), M - np.cos(kx) - np.cos(ky)])
        _, v = np.linalg.eigh(d[0] * SX + d[1] * SY + d[2] * SZ)
        return v[:, 0]

    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    u = [[occ(kx, ky) for ky in ks] for kx in ks]

    def ln(a, b):
        x = np.vdot(a, b)
        return x / abs(x)

    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            F += np.angle(ln(u[i][j], u[ip][j]) * ln(u[ip][j], u[ip][jp])
                          * np.conj(ln(u[i][jp], u[ip][jp]))
                          * np.conj(ln(u[i][j], u[i][jp])))
    return F / (2 * np.pi)


def run():
    reset()
    print("v472 ALPHA.QUILLEN.DETLINE.01: occupied Berry line over U(1) twists; "
          "integrated Chern response (continuum comparison open) [E]/[C]/[O]")

    # 1. Bloch level re-verified
    c_bz = {M: bloch_chern(M) for M in (1.0, 3.0, -1.0)}
    check("BLOCH LEVEL RE-VERIFIED [E]: BZ Chern C(M=1) = 1, C(M=3) = 0, "
          "C(M=-1) = -1 (the v470/v367 integers)",
          abs(c_bz[1.0] - 1) < TOL and abs(c_bz[3.0]) < TOL
          and abs(c_bz[-1.0] + 1) < TOL)

    # 2. the occupied-state Berry line over the twist moduli
    res = {(M, L): detline_chern(L, M) for M in (1.0, 3.0, -1.0) for L in (4, 6)}
    for (M, L), (c, gap) in sorted(res.items()):
        print("   M = %+d, L = %d:  C_detline = %+.9f  (min Fermi gap %.2f)"
              % (int(M), L, c, gap))
    check("OCCUPIED BERRY LINE [E]: twist C_FHS = 1 within tolerance "
          "at M = 1 for L = 4 AND L = 6",
          all(abs(res[(1.0, L)][0] - 1) < TOL for L in (4, 6)))

    # 3. controls
    check("CONTROLS [E]: trivial collar M = 3 gives 0; orientation flip "
          "M = -1 gives -1 (both L)",
          all(abs(res[(3.0, L)][0]) < TOL for L in (4, 6))
          and all(abs(res[(-1.0, L)][0] + 1) < TOL for L in (4, 6)))

    # 4. two tori, one level
    check("TWO TORI, ONE LEVEL [E]: twist-moduli integer == Bloch-BZ integer "
          "for all three M (Niu-Thouless-Wu, exhibited on the S3 collar model)",
          all(round(res[(M, 6)][0]) == round(c_bz[M]) for M in (1.0, 3.0, -1.0)))

    # 5. sampled gap; no inference of a global nonvanishing section
    check("SAMPLED FERMI GAP [E]: gap > 1.9 at M = 1 on all sampled twists "
          "for L = 4,6; this is not a global-section or Dai-Freed test",
          all(res[(1.0, L)][1] > 1.9 for L in (4, 6)))

    # 6. integrated response; individual holonomies are not computed here
    check("INTEGRATED RESPONSE [C]: occupied C_FHS = k0 = 1 "
          "in the collar model; Quillen connections, individual holonomies "
          "and exact zeta-determinant variation are not identified here",
          round(res[(1.0, 6)][0]) == 1)

    # 7. honest [O]
    check("NOT CLOSED [O]: the abstract-seam zeta-determinant identification "
          "(continuum leg, = the SEAM.EQUIV.01 face) stays open; "
          "ALPHA.QUILLEN.EXACT.01 stays [O]; alpha^-1 stays [E]", True)

    return summary("v472 occupied Berry line: twist Chern = Bloch Chern "
                   "(continuum Quillen comparison open) [E]/[C]/[O]")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
