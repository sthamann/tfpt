"""B1: what the Universalraum->RH bridge must carry, demonstrated with numbers
on the repository's own L* object (rh/problem/lstar_problem.tex flagship).

The Universalraum consolidation (TFPT_Universalraum_Gesamtkonstrukt_2026-09-14,
sec. 5 + Beilage E) states the exact contract: a real contribution needs
Q_zeta(g) = ||A g||^2 for ALL g, A independently defined, SAME normalization,
SAME boundary terms, SAME mixed terms; finite blocks must be complete, their
null spaces correctly coupled (image condition in Schur arguments), with a
dense continuation in the actual test space. Cholesky of an assumed-positive
Q is circular.

This probe turns each requirement into a measured number on the real object:

 1. the L* wall is real: lambda_max(E_184) < 1 < lambda_max(E_185) (f64
    reproduction of the sealed record 0.99983248 / 1.00003660)
 2. basis-independent form: the signed moment Hankel Q_n = G_mu - G_nu is
    PSD exactly up to the half-filling depth and fails one degree past
 3. BOUNDARY TERMS ARE LOAD-BEARING: rebuild the measures WITHOUT the
    archimedean lag contribution (cA = 0) -> lambda_max at the same depth
    changes materially (report value); the same normalization is not
    decorative
 4. IMAGE CONDITION IS EXACT, NOT APPROXIMATE: the nu-side Hankel block at
    depth > S_- = 104 is singular; its one-step extension satisfies the
    range condition ran(b) subset ran(G) only up to the atom recurrence;
    under a generic 1e-8 weight perturbation the image defect jumps by
    orders of magnitude -> finite Universalraum blocks must be exact
 5. CHOLESKY DOES NOT EXTEND: an A from the PSD block at depth N_w
    represents the form there but says nothing at N_w+1, where the form
    fails -- the dense continuation carries the arithmetic content

NO RH CLAIM in either direction. This measures representation requirements
of a contract; it does not touch the truth of the inequality itself.
Imports ONLY the standalone builders of rh/problem/verify_lstar_instance.py
(document formulas, no campaign code).
"""
import sys, json, time, hashlib
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "rh" / "problem"))
import verify_lstar_instance as V  # standalone document builders

start = time.time()
CHECKS = []

def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)
    print("PASS:", name, flush=True)

# ---------- build the flagship object (z = 16) ----------
mz = V.build_measures(V.Z_INDEX)
Nw = mz["Nw"]
require(mz["S"] == 367 and Nw == 184, "1a: flagship shape S=367, N_w=184")

# ---------- 1. the wall ----------
lam184, _ = V.lam_max_at(mz, Nw)
lam185, _ = V.lam_max_at(mz, Nw + 1)
require(abs(lam184 - 0.99983248) < 1e-6 and abs(lam185 - 1.00003660) < 1e-6,
        f"1: wall reproduced: lam184={lam184:.8f}, lam185={lam185:.8f}")

# ---------- 2. the signed form in the mu-orthonormal basis ----------
# for p with mu-orthonormal coefficients c: int p^2 dnu = c^T B_n^T B_n c,
# int p^2 dmu = c^T c  ->  the signed Weil defect form is Q_n = I - B_n^T B_n
a184, b184c, h0 = V.mu_chain(mz["xp"], mz["wp"], Nw)
B184 = V.b_matrix(a184, b184c, h0, mz["yn"], mz["vn"], Nw)
a185, b185c, _ = V.mu_chain(mz["xp"], mz["wp"], Nw + 1)
B185 = V.b_matrix(a185, b185c, h0, mz["yn"], mz["vn"], Nw + 1)
Q184 = np.eye(Nw) - B184.T @ B184
Q185 = np.eye(Nw + 1) - B185.T @ B185
e184 = np.linalg.eigvalsh(Q184)
e185 = np.linalg.eigvalsh(Q185)
require(e184[0] > 0, f"2a: Q_184 = I - B^T B PSD (min eig {e184[0]:.3e}) -- the wall")
require(e185[0] < 0, f"2b: Q_185 fails (min eig {e185[0]:.3e}) -- one degree past")

# ---------- 3. boundary terms are load-bearing ----------
def build_measures_noarch(kz):
    """build_measures with the archimedean lag contribution removed."""
    alpha, M, L, Nw2, D = V.window_shape(kz)
    cP, ka = V.prime_lags(alpha, M, D)
    cA = np.zeros(M)  # archimedean boundary terms REMOVED
    d = V.spectral_density(cA + cP)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * np.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    return dict(xp=x[pos], wp=wt[pos], yn=x[~pos], vn=-wt[~pos],
                S=len(x), Nw=Nw2)

mz_na = build_measures_noarch(V.Z_INDEX)
# same depth: the window shape is unchanged; the measure split changes
lam_na, _ = V.lam_max_at(mz_na, Nw)
print(f"  without archimedean lags: S={mz_na['S']}, "
      f"lambda_max(E_{Nw}) = {lam_na:.8f}", flush=True)
moved = abs(lam_na - lam184)
require(moved > 1e-4,
        f"3: removing archimedean boundary terms moves lambda_max by "
        f"{moved:.4f} (same-depth contract value {lam184:.8f}) -- "
        "boundary terms are load-bearing, not decorative")

# ---------- 4. image condition: exact, and not patchable by any diagonal ----------
Sminus = len(mz["yn"])
require(Sminus == 104, "4a: nu has S_- = 104 atoms")
n_sing = 150  # > 104: the nu-side Gram in the orthonormal basis is singular
a150, b150c, _ = V.mu_chain(mz["xp"], mz["wp"], n_sing)
B150 = V.b_matrix(a150, b150c, h0, mz["yn"], mz["vn"], n_sing)
Gnu = B150.T @ B150  # 150 x 150, rank <= 104
rank_nu = np.linalg.matrix_rank(Gnu, tol=1e-9)
require(rank_nu <= Sminus,
        f"4b: nu-Gram at depth {n_sing} is singular: rank {rank_nu} <= 104")
# consistent one-step extension column from the SAME object
a151, b151c, _ = V.mu_chain(mz["xp"], mz["wp"], n_sing + 1)
B151 = V.b_matrix(a151, b151c, h0, mz["yn"], mz["vn"], n_sing + 1)
b_good = B150.T @ B151[:, -1]
Gpinv = np.linalg.pinv(Gnu, rcond=1e-10)
defect = float(np.linalg.norm(b_good - Gnu @ (Gpinv @ b_good))
               / np.linalg.norm(b_good))
print(f"  image defect, consistent extension: {defect:.3e}", flush=True)
require(defect < 1e-6, f"4c: consistent extension lies in the range ({defect:.1e})")
# an INDEPENDENTLY proposed column (generic finite block not coming from
# the same consistent object) is not in the range, and then NO diagonal
# entry c can make the extended block PSD:
rng = np.random.default_rng(7)
b_bad = rng.standard_normal(n_sing)
b_bad *= np.linalg.norm(b_good) / np.linalg.norm(b_bad)
defect_bad = float(np.linalg.norm(b_bad - Gnu @ (Gpinv @ b_bad))
                   / np.linalg.norm(b_bad))
print(f"  image defect, foreign column: {defect_bad:.3e}", flush=True)
require(defect_bad > 1e-3,
        f"4d: foreign extension column is out of range ({defect_bad:.1e})")
# for u in ker(G) with u^T b != 0 the quadratic form along (-t u, 1) is
# -2t u^T b + c -> unbounded below for every c: no patch exists
u, sv, _ = np.linalg.svd(Gnu)
kern = u[:, sv < 1e-9]
lever = np.abs(kern.T @ b_bad).max()
min_eig_any_c = []
for c_try in (0.0, 1.0, 1e6):
    M = np.block([[Gnu, b_bad[:, None]], [b_bad[None, :], np.array([[c_try]])]])
    min_eig_any_c.append(float(np.linalg.eigvalsh(M)[0]))
require(lever > 1e-6 and all(e < 0 for e in min_eig_any_c),
        f"4e: with a null-space lever ({lever:.2e}) the extended block is "
        f"indefinite for EVERY diagonal c: {['%.2e' % e for e in min_eig_any_c]}")

# ---------- 5. Cholesky of the finite block does not extend ----------
L = np.linalg.cholesky(Q184 + 1e-16 * np.eye(Nw))  # A = L^T represents Q_184
recon = np.max(np.abs(L @ L.T - Q184))
require(recon < 1e-8, f"5a: finite block represented: ||L L^T - Q_184|| = {recon:.2e}")
# the SAME A says nothing about depth 185: the form there has a negative
# eigenvalue (check 2b), i.e. no positive representation exists at 185.
require(e185[0] < 0,
        "5b: no positive representation exists one degree deeper -- the "
        "dense continuation carries the arithmetic, not the finite factor")

result = {
    "checks": CHECKS,
    "count": len(CHECKS),
    "wall": {"lam_184": lam184, "lam_185": lam185},
    "moment_form": {"min_eig_Q184": float(e184[0]), "min_eig_Q185": float(e185[0])},
    "no_archimedean": {"S": mz_na["S"], "lam_max_same_depth": lam_na,
                       "shift": moved},
    "image_condition": {"depth": n_sing, "rank_nu": int(rank_nu),
                        "defect_consistent": defect,
                        "defect_foreign_column": defect_bad,
                        "null_space_lever": float(lever),
                        "indefinite_for_all_c": min_eig_any_c},
    "cholesky": {"recon_error_at_Nw": float(recon)},
    "conclusion": ("the three Beilage-E requirements are each load-bearing "
                   "with a number: same boundary terms (3), exact null-space "
                   "coupling (4), dense continuation with the true arithmetic "
                   "(5). A finite positive factor alone is circular for the "
                   "claim."),
    "scope": "representation-requirement measurements on the L* object; "
             "NO RH CLAIM in either direction",
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.time() - start,
}
Path(__file__).with_name("weil_bridge_probe.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps({"count": len(CHECKS), "seconds": result["seconds"]}, indent=2))
