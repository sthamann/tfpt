#!/usr/bin/env python3
"""Exact marked-space audit and source QWZ opposite-holonomy reflection.

No prime/zero input, no spectral fitting, no source edits, no RH claim.
The displayed reflection depends on the deployed source wiring and a chosen
boundary Pauli frame. Opposite-flux direct sum is an explicit extension, not
a claim that the physical source already supplies its joint Hilbert space.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

from seam_source import construct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHECKS = []
DATA = {}


def check(name, ok):
    CHECKS.append({'name': name, 'passed': bool(ok)})
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)


def err(M):
    return float(np.max(np.abs(M)))


def thermal(H, beta):
    e, V = np.linalg.eigh(H)
    return (V * (1 / (1 + np.exp(beta * e)))) @ V.conj().T


def exact(M):
    return [[str(x) for x in row] for row in M.tolist()]


src = construct()
A = sp.Matrix(src['A16_dep'])
B = sp.Matrix(src['A_int'])
O = sp.zeros(16)
for i, j in enumerate(src['img']):
    O[j, i] = 1
I = sp.eye(16)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
J = sp.Matrix([[0, 1], [-1, 0]])
P3, P2, PB = [sp.diag(*[int(a <= i < b) for i in range(16)])
              for a, b in ((0, 6), (6, 10), (10, 16))]
check('source_partition_and_C6_exact', P3+P2+PB == I and O**6 == I
      and A*O == O*A and B*O == O*B and A*B == B*A)

# Explicit rational, boundary-preserving reflection. The group reflection T
# exchanges carrier channel seats 2 and 3. Three choices reverse that triangle;
# no uniqueness claim is made. v and w come from uniform coupling to boundary
# and its orthogonal direction in the marked 3+2 carrier plane.
v = sp.Matrix([1]*5 + [0]*3)
w = sp.Matrix([2]*3 + [-3]*2 + [0]*3)
Pv = v*v.T/5
Pw = w*w.T/30
T = sp.eye(8)
T[1, 1] = T[2, 2] = 0
T[1, 2] = T[2, 1] = 1
U = sp.kronecker_product(T-2*Pv-Pw/13, X) - sp.kronecker_product(5*Pw/13, Z)
check('explicit_rational_reflection_involution', U.T == U and U*U == I)
check('explicit_reflection_reverses_full_source_family', U*A*U == -A and U*B*U == -B)
check('explicit_reflection_reverses_clock', U*O*U == O.T)
check('explicit_reflection_preserves_boundary', U*PB == PB*U
      and U[10:, 10:] == sp.kronecker_product(sp.eye(3), X))
check('explicit_reflection_mixes_marked_carrier_blocks', U*P3 != P3*U and U*P2 != P2*U)
check('explicit_reflection_signature_8_8', sp.trace(U) == 0)
DATA['reflection'] = {'U': exact(U), 'formula': '(T - 2 Pv - Pw/13) tensor X - (5 Pw/13) tensor Z',
    'max_denominator_lcm': str(sp.ilcm(*[x.q for x in U])),
    'status': 'boundary-preserving; mixes marked 3 and 2 carrier subspaces; chosen boundary frame and triangle reflection'}

# Explain the 12/13 and 5/13 coefficients through source transport, not fitting.
# In normalized carrier directions v,w the off-diagonal B block is
# D = -sqrt(6) (I + J/5). Boundary coupling fixes U_v=-X; hence
# U_w = D^-1 X D = (12 X - 5 Z)/13.
F = sp.Matrix.hstack(v/sp.sqrt(5), w/sp.sqrt(30))
EF = sp.kronecker_product(F, sp.eye(2))
D = (EF.T*B*EF)[:2, 2:4]
check('source_transport_block_exact', sp.simplify(D + sp.sqrt(6)*(sp.eye(2)+J/5)) == sp.zeros(2))
check('source_transport_fixes_relative_frame', sp.simplify(D.inv()*X*D-(12*X-5*Z)/13) == sp.zeros(2))

# The triangle obstruction applies to ALL invertible complex-linear U that
# commute with the three markers, even if U does not preserve C6 or A alone.
triangle = sp.trace(P3*B*P2*B*PB*B)
u, t = sp.symbols('u t', real=True)
H = -sp.I*(u*A+t*B)
triangle_h = sp.expand(sp.trace(P3*H*P2*H*PB*H))
check('marked_triangle_obstruction_exact', triangle == -36 and triangle_h == -36*sp.I*t**3)
check('family_commuting_reflection_obstruction_exact', O**2 != O**(-2)
      and sp.trace(O**2*A) == 0 and sp.trace(O**2*B) == 6
      and sp.expand(sp.trace(O**2*H)) == -6*sp.I*t)
edges = [P3*B*P2+P2*B*P3, P2*B*PB+PB*B*P2, PB*B*P3+P3*B*PB]
check('independent_edge_family_obstruction_exact', sp.trace(edges[0]*edges[1]*edges[2]) == -36)
DATA['obstruction'] = {'Tr_P3_B_P2_B_PB_B': str(triangle),
    'Tr_P3_H_P2_H_PB_H': str(triangle_h),
    'Tr_family_H': '-6*i*t; family action is O^2 in this constructor',
    'scope': 'No invertible complex-linear U preserving all three marked spaces reverses this H for t != 0. No common reversing U for independently variable three edge couplings. Such variations are only a C6/CAR control, not proved allowed by all TFPT rules.'}

# Exact linear census: real symmetric anti-A matrices have P tensor X + Q
# tensor Z, with P,Q real symmetric. Nullspace dimensions do NOT themselves
# establish invertibility; the explicit U and triangle certificate do that.
coeff = sp.symbols('c:72')
blocks = []
k = 0
for _ in range(2):
    M = sp.zeros(8)
    for i in range(8):
        for j in range(i, 8):
            M[i, j] = M[j, i] = coeff[k]
            k += 1
    blocks.append(M)
M = sp.kronecker_product(blocks[0], X)+sp.kronecker_product(blocks[1], Z)
counts = {}
for name, projectors, expected in [('boundary', [PB], 14), ('all_markers', [P3, P2, PB], 12)]:
    eq = list(M*B+B*M)+list(M*O-O.T*M)
    for P in projectors:
        eq += list(M*P-P*M)
    lin, _ = sp.linear_eq_to_matrix(eq, coeff)
    ns = lin.nullspace()
    counts[name] = len(ns)
    check('linear_census_'+name, len(ns) == expected)
DATA['real_symmetric_census_dimensions'] = counts

# Boundary observability: O is literally the identity on the boundary.
# All Krylov vectors generated by A,B remain in its fixed sector.
Pi0 = sum((O**k for k in range(6)), sp.zeros(16))/6
Krylov = sp.Matrix.hstack(*[(B**k)[:, 10:] for k in range(5)])
check('boundary_clock_fixed_exact', O*PB == PB and Pi0*PB == PB and Pi0.rank() == 10)
check('boundary_cyclic_space_exactly_clock_fixed', Krylov.rank() == 10 and Pi0*Krylov == Krylov)
Fb = sp.Matrix([0]*5+[1]*3)
Eb = sp.kronecker_product(Fb, sp.eye(2))
Kbright = sp.Matrix.hstack(*[B**k*Eb for k in range(4)])
check('bright_boundary_cyclic_rank_six', Kbright.rank() == 6)
Pd = PB-sp.kronecker_product(Fb*Fb.T/3, sp.eye(2))
check('four_boundary_dark_modes_uncoupled', Pd.rank() == 4 and B*Pd == sp.zeros(16) and Pd*B == sp.zeros(16))

# Restrict to the normalized group-uniform plane via a rational basis and its
# Gram left inverse. Bred is not Euclidean antisymmetric: the inherited Gram
# metric is diag(3,2,3) tensor I2. This is only a change of basis.
Fg = sp.Matrix.hstack(sp.Matrix([1]*3+[0]*5), sp.Matrix([0]*3+[1]*2+[0]*3), Fb)
E = sp.kronecker_product(Fg, sp.eye(2))
G = E.T*E
Br = G.inv()*E.T*B*E
Ar = G.inv()*E.T*A*E
check('six_dimensional_source_restriction_exact', B*E == E*Br and A*E == E*Ar and O*E == E)
R = sp.Matrix(3, 3, lambda i, j: Br[2*i, 2*j])
S = sp.Matrix(3, 3, lambda i, j: Br[2*i, 2*j+1])
mu = sp.symbols('mu')
q = sp.expand((mu*sp.eye(3)-(S-sp.I*R)).det())
check('active_spectrum_fixed_cubic_exact', q == mu**3-mu**2-21*mu+9)
DATA['boundary_observability'] = {'clock_fixed_rank': 10, 'bright_cyclic_rank': 6,
    'boundary_dark_rank': 4, 'invisible_nontrivial_clock_rank': 6,
    'reduced_B': exact(Br), 'inherited_Gram': exact(G), 'cubic': str(q),
    'active_H_eigenvalues': '+/-(u+t*lambda_j), lambda_j roots of cubic',
    'scope': 'Boundary spectral measures do not see nontrivial C6 sectors for this family; not a claim about all possible observables.'}

# Source state comparisons and a symmetry-only edge intertwiner. QWZ W uses
# fixed exact zero-mode anchors at p=0, M=1. At this anchor C_edge=I2/2;
# compiler bright-boundary covariance is not isospectral in the given sample.
sys.path.insert(0, str(ROOT/'verification'))
qpath = ROOT/'verification/v998_seam_modular_closure.py'
spec = importlib.util.spec_from_file_location('geometry_qwz', qpath)
qwz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qwz)
qwz.NY = 8
bn = np.array(Eb, float)/np.sqrt(3)
Un = np.array(U, float)
An = np.array(A, float)
Bn = np.array(B, float)
Cn = thermal(-1j*(An+Bn/8), 1)
Cb = bn.T@Cn@bn
check('source_boundary_complement_numeric', err(Un@Cn@Un+Cn-np.eye(16)) < 1e-12
      and err(np.array(X, float)@Cb@np.array(X, float)+Cb-np.eye(2)) < 1e-12)
W = np.zeros((16, 2))
W[:2, 0] = [1/np.sqrt(2), -1/np.sqrt(2)]
W[-2:, 1] = [1/np.sqrt(2), 1/np.sqrt(2)]
H0 = qwz.strip_hamiltonian(0)
Cq = W.T@thermal(H0, 1)@W
Q = sp.diag(1, sp.I)
check('two_dimensional_symmetry_intertwiner_exact', Y*Q == Q*X and Q.conjugate().T*Q == sp.eye(2))
check('QWZ_anchor_zero_modes_exact_float', err(H0@W) < 1e-14 and err(Cq-np.eye(2)/2) < 1e-12)
eig_gap = err(np.linalg.eigvalsh(Cb)-np.linalg.eigvalsh(Cq))
check('anchor_covariances_not_unitarily_equivalent', eig_gap > .01)
DATA['readout_comparison'] = {'compiler_bright_eigenvalues': np.linalg.eigvalsh(Cb).tolist(),
    'QWZ_anchor_eigenvalues': np.linalg.eigvalsh(Cq).tolist(), 'spectral_gap': eig_gap,
    'parameters': {'compiler_u':1,'compiler_t':.125,'beta':1,'QWZ_p':0,'QWZ_mass':1,'QWZ_ny':8},
    'scope': 'Symmetry intertwiners alone do not identify states. This mismatch is at the stated anchor; no universal parameter-map no-go.'}

# A clock-reversing QWZ spatial symmetry exists if one reverses x, rather than
# the earlier y reflection. Non-real holonomy is exchanged with its inverse.
Tx = X/(2*sp.I)-Z/2
Ty = Y/(2*sp.I)-Z/2
check('QWZ_longitudinal_local_identities_exact', X*Z*X == -Z
      and X*Tx.conjugate().T*X == -Tx and X*Ty*X == -Ty)
qwz.NY = 3
rows = []
for nx in (4, 6, 8):
    V = np.kron(np.eye(nx)[::-1], np.kron(np.eye(qwz.NY), np.array(X, float)))
    for alpha in (0, .25, .5, .75):
        Hp = qwz.cylinder_hamiltonian(nx, alpha)
        Hm = qwz.cylinder_hamiltonian(nx, -alpha)
        rows.append({'nx':nx,'ny':qwz.NY,'alpha':alpha,
            'paired_H':err(V@Hp@V+Hm), 'same_H':err(V@Hp@V+Hp),
            'paired_C':err(V@thermal(Hp,1)@V+thermal(Hm,1)-np.eye(len(Hp)))})
check('QWZ_opposite_holonomy_reflection_12_samples', max(max(r['paired_H'], r['paired_C']) for r in rows) < 1e-11)
check('QWZ_real_holonomy_closes_same_sector', max(r['same_H'] for r in rows if r['alpha'] in (0,.5)) < 1e-12)
check('QWZ_nonreal_holonomy_not_same_sector', min(r['same_H'] for r in rows if r['alpha'] in (.25,.75)) > .9)
DATA['QWZ_longitudinal_samples'] = rows

# Exact finite N=4 Ny=2 matrices at seam phases +/-i: independently assemble
# H(T), then prove the doubled symmetry and translation relation as matrices.
nx, ny = 4, 2
shift = sp.zeros(nx)
for j in range(nx):
    shift[(j+1)%nx, j] = sp.I if j == nx-1 else 1
ryshift = sp.Matrix([[0,0],[1,0]])
onsite = sp.kronecker_product(sp.eye(ny), Z)
hy = sp.kronecker_product(ryshift, Ty)+sp.kronecker_product(ryshift.T, Ty.conjugate().T)


def cyl(Txclock):
    return sp.kronecker_product(sp.eye(nx), onsite+hy) + sp.kronecker_product(Txclock, sp.kronecker_product(sp.eye(ny), Tx)) + sp.kronecker_product(Txclock.conjugate().T, sp.kronecker_product(sp.eye(ny), Tx.conjugate().T))


Hp, Hm = cyl(shift), cyl(shift.conjugate())
Rx = sp.zeros(nx)
for j in range(nx):
    Rx[j, nx-1-j] = 1
V = sp.kronecker_product(Rx, sp.kronecker_product(sp.eye(ny), X))
Ud = sp.kronecker_product(X, V)
Hd = sp.diag(Hp, Hm)
Td = sp.diag(sp.kronecker_product(shift, sp.eye(2*ny)), sp.kronecker_product(shift.conjugate(), sp.eye(2*ny)))
check('opposite_flux_double_exact_involution_and_H', Ud**2 == sp.eye(32) and Ud*Hd*Ud == -Hd)
check('opposite_flux_double_exact_clock_reversal', Ud*Td*Ud == Td.conjugate().T)
check('twisted_clock_not_ordinary_Cn', Td**nx != sp.eye(32))
DATA['QWZ_double'] = {'definition': 'Halpha direct_sum Hminusalpha; U = sheet_swap tensor (Rx tensor Iy tensor X)',
    'status': 'explicit finite extension of the available source family; common physical double-cover/state not derived',
    'clock': 'twisted translation satisfies Talpha^Nx=exp(2 pi i alpha) I, not automatically the compiler C6 clock'}

result = {'boundary': 'Finite source algebra only; physical identification, global RH and factoring remain unproved',
    'checks': CHECKS, 'passed': sum(c['passed'] for c in CHECKS), 'total': len(CHECKS),
    'data': DATA, 'provenance': src['provenance'],
    'source_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (Path(__file__), HERE/'seam_source.py', qpath)},
    'versions': {'sympy':sp.__version__,'numpy':np.__version__}}
(HERE/'seam_geometry_results.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
print(f"{result['passed']}/{result['total']} passed. FINITE SOURCE RESULTS ONLY.")
raise SystemExit(0 if result['passed']==result['total'] else 1)
