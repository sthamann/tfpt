"""T5 two-bank exact transfer (parent-direct). NON-RH. No claims, no repo writes.

H_A 4x4 per channel (v1.6.2 L484-490, EXACT quote):
  [[0, s, 0, 0],[s, D, e, 0],[0, e, D, s],[0, 0, s, 0]], s=sqrt8*g, e=eta.
Verifies (H^3)_{4,1}=8g^2 eta with vanishing lower powers, then computes exact
P_{1->4}(t) = |<4|exp(-iHt)|1>|^2, first-max time, and cone-mismatch readouts.
Also verifies F'_+ = F'_-  <=>  eps = 0 (cone <=> gapless-B lemma).
"""
import numpy as np

checks, verdict = [], 'PASS'


def need(ok, name):
    global verdict
    if not ok:
        verdict = 'FAIL'
        print(f'FAIL: {name}')
    checks.append((name, bool(ok)))


D, g, eta = 1.0, 1.0 / 20.0, 0.1
s = np.sqrt(8) * g
H = np.array([[0, s, 0, 0], [s, D, eta, 0], [0, eta, D, s], [0, 0, s, 0]])

# --- transfer orders ---
H2, H3 = H @ H, H @ H @ H
need(abs(H[3, 0]) < 1e-12 and abs(H2[3, 0]) < 1e-12, 'lower powers (H,H^2)_{4,1} vanish')
need(abs(H3[3, 0] - 8 * g * g * eta) < 1e-12,
     f'(H^3)_{{4,1}} = 8g^2 eta = {8*g*g*eta:.6f} (got {H3[3,0]:.6f})')

# --- exact P(t) ---
ew, ev = np.linalg.eigh(H)
c1 = ev[0, :]            # <n|1>
c4 = ev[3, :]            # <n|4>
amp = lambda t: np.sum(np.conj(c4) * c1 * np.exp(-1j * ew * t))
ts = np.linspace(0, 3000, 60001)
P = np.array([abs(amp(t)) ** 2 for t in ts])
imax = int(np.argmax(P[1:])) + 1
need(P[0] < 1e-12, 'P(0)=0')
need(P[imax] > 0.99, f'near-complete transfer max P={P[imax]:.6f} at t={ts[imax]:.2f}')

# --- cone lemma: F'_+ - F'_- = eps/sqrt(eps^2+32g^2) ---
def dF(eps):
    Om = np.sqrt(eps**2 + 32 * g**2)
    return (1 + eps / Om) / 2, (1 - eps / Om) / 2

fp0, fm0 = dF(0.0)
need(abs(fp0 - fm0) < 1e-12 and abs(fp0 - 0.5) < 1e-12, 'F\'_+ = F\'_- = 1/2 at eps=0')
mismatch = [abs(dF(e)[0] - dF(e)[1]) for e in (0.01, 0.1, 0.5, 1.0)]
need(all(m > 0 for m in mismatch), f'cone mismatch > 0 for eps>0: {[f"{m:.4f}" for m in mismatch]}')

print(f'verdict={verdict} guards={sum(1 for _,ok in checks if ok)}/{len(checks)}')
print(f'first transfer max: t*={ts[imax]:.2f} (units hbar/D), P={P[imax]:.6f}, params g/D={g}, eta/D={eta}')
print(f'even/odd boson-mediator energies: D+eta={D+eta}, D-eta={D-eta}')
print(f'eig(H_A)={np.round(ew,6).tolist()}')
