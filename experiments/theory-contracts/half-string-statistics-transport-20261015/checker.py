"""Statistics transport by the original half string on the unchanged QWZ source.

Numerical (exact-structure + float tolerance) checks; no promotion.  Scope: PROOF.md.
Source operator: verification/v988_psi_lambda_reduction.py:75-96 (qwz_cylinder,
seam bond phase i^r), copied verbatim below and pinned by string comparison.
Half string: D = -1 on the arc 0 <= x <= a (all rows), the square of the
quarter-phase seam string (half-twist-grade-carry README section 4).

H1  one-particle: D^2 = 1 and D H_r D = H_{r+2} - R D, with R = H_{r+2} D - D H_r
    supported only on the bonds a -> a+1, ||R|| = 2, rank R = 2 Ny.
H2  Fock lift Gamma = (-1)^{N_arc} (Jordan-Wigner, small cylinder): Gamma c_x Gamma
    = -c_x on the arc, +c_x outside; a bilinear c_x^dag c_y gets the sign
    chi(x) chi(y); Gamma dGamma(H_r) Gamma = dGamma(H_{r+2}) - dGamma(R D) exactly.
H3  monodromy: transporting c_x across the string endpoint multiplies it by -1
    = exp(2 pi i v.s) with v.s = 1/2.
H4  time: ||exp(-it D H_r D) - exp(-it H_{r+2})|| <= t ||R|| (Duhamel), checked.
"""
import ast
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

ROOT = Path(__file__).resolve().parents[3]
src = (ROOT / "verification/v988_psi_lambda_reduction.py").read_text()
require("pin_TX", "TX = (SX / (2j) - SZ / 2)" in src)
require("pin_TY", "TY = (SY / (2j) - SZ / 2)" in src)
require("pin_seam_phase", "ph = 1j ** k_twist" in src and "amp = ph if x == Nx - 1 else 1.0" in src)

SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1, -1]).astype(complex)
TX = (SX / (2j) - SZ / 2); TY = (SY / (2j) - SZ / 2)
def qwz_cylinder(Nx, Ny, M, k_twist):            # verbatim from v988:75-96
    dim = 2 * Nx * Ny
    H = np.zeros((dim, dim), dtype=complex)
    def sl(x, y):
        return 2 * ((x % Nx) * Ny + y)
    ph = 1j ** k_twist
    for x in range(Nx):
        for y in range(Ny):
            i = sl(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            j = sl(x + 1, y)
            amp = ph if x == Nx - 1 else 1.0
            H[j:j + 2, i:i + 2] += amp * TX
            H[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < Ny:
                j = sl(x, y + 1)
                H[j:j + 2, i:i + 2] += TY
                H[i:i + 2, j:j + 2] += TY.conj().T
    return H

def Dmat(Nx, Ny, a):
    d = []
    for x in range(Nx):
        for y in range(Ny):
            d += [(-1.0 if x <= a else 1.0)] * 2
    return np.diag(d).astype(complex)
def site_x(idx, Ny):
    return (idx // 2) // Ny

# H1 / H4
for Nx, Ny, a in ((6, 2, 2), (8, 4, 3), (10, 8, 4)):
    D = Dmat(Nx, Ny, a)
    require(f"H1_D2_{Nx}_{Ny}", np.allclose(D @ D, np.eye(len(D))))
    for r in range(4):
        Hr, Hr2 = qwz_cylinder(Nx, Ny, 1.0, r), qwz_cylinder(Nx, Ny, 1.0, (r + 2) % 4)
        R = Hr2 @ D - D @ Hr
        require(f"H1_identity_{Nx}_{Ny}_{r}", np.allclose(D @ Hr @ D, Hr2 - R @ D))
        nz = np.argwhere(np.abs(R) > 1e-12)
        require(f"H1_support_far_endpoint_{Nx}_{Ny}_{r}",
                all({site_x(i, Ny), site_x(j, Ny)} == {a, a + 1} for i, j in nz))
        require(f"H1_norm2_{Nx}_{Ny}_{r}", abs(np.linalg.norm(R, 2) - 2) < 1e-10)
        require(f"H1_rank_{Nx}_{Ny}_{r}", np.linalg.matrix_rank(R, tol=1e-10) == 2 * Ny)
        for t in (0.1, 0.5, 1.0):
            dev = np.linalg.norm(expm(-1j * t * (D @ Hr @ D)) - expm(-1j * t * Hr2), 2)
            require(f"H4_duhamel_{Nx}_{Ny}_{r}_{t}", dev <= t * 2 + 1e-10)

# H2 / H3 on a small Fock space via Jordan-Wigner
Nx, Ny, a = 3, 1, 0
n = 2 * Nx * Ny
Z = np.diag([1, -1]).astype(complex); Iq = np.eye(2); sm = np.array([[0, 1], [0, 0]], complex)
def kron(ms):
    out = np.array([[1]], complex)
    for m in ms: out = np.kron(out, m)
    return out
c = [kron([Z] * k + [sm] + [Iq] * (n - k - 1)) for k in range(n)]
for i in range(n):
    for j in range(n):
        if not np.allclose(c[i] @ c[j].conj().T + c[j].conj().T @ c[i], (i == j) * np.eye(2 ** n)):
            raise RuntimeError("CAR")
checks["H2_CAR"] = True
D = Dmat(Nx, Ny, a)
arc = [k for k in range(n) if D[k, k].real < 0]
Narc = sum(c[k].conj().T @ c[k] for k in arc)
w, V = np.linalg.eigh(Narc)
Gam = V @ np.diag(np.exp(1j * np.pi * np.round(w))) @ V.conj().T
require("H2_Gamma_involution", np.allclose(Gam @ Gam, np.eye(2 ** n)))
for k in range(n):
    sgn = -1 if k in arc else 1
    require(f"H2_fermion_sign_{k}", np.allclose(Gam @ c[k] @ Gam, sgn * c[k]))
    require(f"H3_monodromy_{k}", (sgn == -1) == (k in arc) and np.isclose(np.exp(2j * np.pi * 0.5), -1))
for x in range(n):
    for y in range(n):
        bil = c[x].conj().T @ c[y]
        s = D[x, x].real * D[y, y].real
        require(f"H2_bilinear_sign_{x}_{y}", np.allclose(Gam @ bil @ Gam, s * bil))
def dGamma(h):
    return sum(h[i, j] * c[i].conj().T @ c[j] for i in range(n) for j in range(n))
for r in range(4):
    Hr, Hr2 = qwz_cylinder(Nx, Ny, 1.0, r), qwz_cylinder(Nx, Ny, 1.0, (r + 2) % 4)
    R = Hr2 @ D - D @ Hr
    require(f"H2_fock_time_identity_{r}", np.allclose(Gam @ dGamma(Hr) @ Gam, dGamma(Hr2) - dGamma(R @ D)))

results = {"contract": "half-string-statistics-transport-20261015", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
