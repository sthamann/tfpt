"""Shared float64 core for the v1.6.9 autonomous-controller contract.

Single time-independent total Hamiltonian H_tot on the 18-dimensional product
space K3 (system) x C3 (controller switch: free / impulse / recorder) x R2
(neutral pointer), with basis ordering idx = (c*3+s)*2+r.

  H_tot = H_F (+) H_Z (+) H_R   (block-diagonal over controller branches)

  H_F = h3 (x) I_R            free arm: U(2t) (x) I, pointer untouched
  H_Z = (i/T) Log W_Z         impulse arm: W_Z = (U Zb U) (x) I_R
  H_R = (i/T) Log W_R         recorder arm: W_R = (U(x)I) C_R (U(x)I)

with U = exp(-i t h3), T = 2t, Zb = I-2B, C_R = (I-B)(x)I + B(x)X.
Principal-branch matrix logarithm; blocks re-symmetrized to Hermitian.

No guards here (builders only); guards live in the checkers. Deterministic:
same calls return bit-identical arrays. No stdout on import.
"""
import math
import numpy as np
from scipy.linalg import expm, block_diag

DELTA = 1.0
G = 0.05
S7 = math.sqrt(7.0)

# K3 operators (3x3 float64). h3 is literally symmetric entry by entry.
H3 = np.array([[0.0, 0.0, -G],
               [0.0, 0.0, S7 * G],
               [-G, S7 * G, DELTA]], dtype=np.float64)
B3 = np.diag([0.0, 0.0, 1.0])
ZB3 = np.diag([1.0, 1.0, -1.0])
E3 = np.diag([0.0, 1.0 / 7.0, 0.0])
X3 = (H3 - DELTA * B3) / G

I2 = np.eye(2, dtype=np.float64)
I3 = np.eye(3, dtype=np.float64)
XR = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.float64)

OMEGA = math.sqrt(DELTA * DELTA / 4.0 + 8.0 * G * G)
D_PAR = DELTA / (2.0 * OMEGA)
TAU = math.pi / (2.0 * OMEGA)
T_TOT = 2.0 * TAU

U1 = expm(-1j * TAU * H3)
U2 = expm(-1j * T_TOT * H3)
CR = np.kron(I3 - B3, I2) + np.kron(B3, XR)
W_F = np.kron(U2, I2)
W_Z = np.kron(U1 @ ZB3 @ U1, I2)
W_R = np.kron(U1, I2) @ CR @ np.kron(U1, I2)


def principal_log_hamiltonian(W, T):
    """Hermitian H with exp(-i T H) = W (principal branch, symmetrized)."""
    lam, V = np.linalg.eig(W)
    phases = np.angle(lam)
    H = (V * (-phases / T)) @ np.linalg.inv(V)
    return (H + H.conj().T) / 2.0


H_F = np.kron(H3, I2).astype(np.complex128)
H_Z = principal_log_hamiltonian(W_Z, T_TOT)
H_R = principal_log_hamiltonian(W_R, T_TOT)
H_TOT = block_diag(H_F, H_Z, H_R)

# Full-space observables for idx = (c*3+s)*2+r, i.e. kron(C, kron(S, R)).
E_FULL = np.kron(np.eye(3), np.kron(E3, I2))
HSYS_FULL = np.kron(np.eye(3), np.kron(H3, I2))
NB_FULL = np.kron(np.eye(3), np.kron(B3, I2))
HINT_FULL = H_TOT - HSYS_FULL
N_TOT = 2 * np.eye(18, dtype=np.int64)
PROP_FULL = expm(-1j * T_TOT * H_TOT)


def basis_index(c, s, r):
    return (c * 3 + s) * 2 + r


def initial_state(c):
    psi = np.zeros(18, dtype=np.complex128)
    psi[basis_index(c, 0, 0)] = 1.0
    return psi


def evolve_branch(c):
    return PROP_FULL @ initial_state(c)


def expect(O, psi):
    return complex(np.vdot(psi, O @ psi))


def as_csr(psi):
    """Reshape an 18-dim state to A[c,s,r]."""
    return psi.reshape(3, 3, 2)


def reduced_sys(A):
    return np.einsum('csr,ctr->st', A, A.conj())


def reduced_ptr(A):
    return np.einsum('csr,cst->rt', A, A.conj())


def reduced_ctrl(A):
    return np.einsum('csr,tsr->ct', A, A.conj())


def branch_projector(c):
    P = np.zeros((3, 3))
    P[c, c] = 1.0
    return np.kron(P, np.eye(6))


def fmt(x):
    return repr(float(x))
