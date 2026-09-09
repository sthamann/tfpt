#!/usr/bin/env python3
"""Source-first continuation: finite seam covariance reflection audit.

Separates unitary reflection, antiunitary CAR conjugation, clock equivariance,
and source-dependent algebraic reflection. No zero/prime input. No RH claim.
"""
from __future__ import annotations

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
sys.path.insert(0, str(ROOT / "verification"))
CHECKS = []
DATA = {}


def check(name, cond):
    CHECKS.append({"name": name, "passed": bool(cond)})
    print(f"{'PASS' if cond else 'FAIL'} {name}", flush=True)


def residual(A):
    return float(np.max(np.abs(A)))


def thermal(H, beta):
    vals, vecs = np.linalg.eigh(H)
    return (vecs * (1/(1+np.exp(beta*vals)))) @ vecs.conj().T


def modular(C):
    vals, vecs = np.linalg.eigh(C)
    if vals.min() <= 0 or vals.max() >= 1:
        raise ValueError("Nonfaithful/numerically saturated covariance: do not clip")
    return (vecs*np.log((1-vals)/vals))@vecs.conj().T


def read_module(name, rel):
    path = ROOT/rel
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


src = construct()
A = sp.Matrix(src["A16_dep"])
B = sp.Matrix(src["A_int"])
O = sp.zeros(16)
for i, j in enumerate(src["img"]):
    O[j, i] = 1
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
U0 = sp.kronecker_product(sp.eye(8), X)
check("source_constructor_5_checks", src["provenance"]["source_checks"] == 5)
check("integer_seam_sources_antisymmetric", A.T == -A and B.T == -B)
check("source_C6_covariance_exact", O**6 == sp.eye(16) and O*A == A*O and O*B == B*O)
check("bare_pair_swap_odd_exact", U0*A*U0 == -A)
check("deployed_mixing_breaks_pair_swap_exact", U0*B*U0 != -B)

twists = [sp.trace(O**k*B) for k in range(6)]
check("clock_twisted_trace_obstruction_exact", twists == [0, -6, 6, 0, -6, 6] and sp.trace(O*A) == 0)
# If UOU^-1=O and UHU^-1=-H, Tr(OH)=0. Here H=-i(uA+tB),
# hence Tr(OH)=6it. This rules out ALL invertible complex-linear such U t!=0,
# not only the displayed pair swaps. Antiunitarity invalidates this trace proof.
DATA["clock_obstruction"] = {"traces_Ok_Aint": list(map(str, twists)), "trace_OH": "6*i*t",
    "scope": "No invertible complex-linear U commuting with O can reverse H(u,t) when t != 0; finite beta>0 only for covariance equivalence."}

An = np.array(A, dtype=float)
Bn = np.array(B, dtype=float)
On = np.array(O, dtype=float)
Un = np.array(U0, dtype=float)
rows = []
for u, coupling in ((1, 0), (1, .125), (.5, .05), (2, .2)):
    H = -1j*(u*An+coupling*Bn)
    for beta in (.25, 1, 2):
        C = thermal(H, beta)
        rows.append({"u": u, "t": coupling, "beta": beta,
            "pair_swap": residual(Un@C@Un+C-np.eye(16)),
            "antiunitary_conjugation": residual(C.conj()+C-np.eye(16)),
            "modular_inverse": residual(modular(C)-beta*H)})
check("automatic_CAR_conjugation_full_source_grid", max(r["antiunitary_conjugation"] for r in rows) < 1e-12)
check("finite_beta_modular_inverse_without_clipping", max(r["modular_inverse"] for r in rows) < 1e-10)
check("pair_swap_fails_every_coupled_source_sample", all(r["pair_swap"] > 1e-5 for r in rows if r["t"] > 0))
DATA["finite_seam_grid"] = rows

# A family of source-dependent, NONLOCAL clock-reversing candidates.
# Search only linear equations in real symmetric M, with {M,A}={M,B}=0
# and M O = O^T M; no desired eigenvalues are supplied.
coeff = sp.symbols("a:72")
pair_matrices = []
idx = 0
for _ in range(2):
    P = sp.zeros(8)
    for i in range(8):
        for j in range(i, 8):
            P[i,j] = P[j,i] = coeff[idx]
            idx += 1
    pair_matrices.append(P)
Mform = sp.kronecker_product(pair_matrices[0], X)+sp.kronecker_product(pair_matrices[1], Z)
eqs = list(Mform*B+B*Mform)+list(Mform*O-O.T*Mform)
lin, _ = sp.linear_eq_to_matrix(eqs, coeff)
basis = lin.nullspace()
check("source_clock_reversing_symmetric_solution_dimension_18", len(basis) == 18)
# Declared coordinate selection, NOT a uniqueness theorem. All-ones was
# tried during exploration and was singular; coefficients 1..18 are recorded.
selection = sum(((i+1)*b for i,b in enumerate(basis)), sp.zeros(72, 1))
M = Mform.subs(dict(zip(coeff, selection)))
check("exact_nonlocal_witness_invertible", M.det() != 0)
check("exact_nonlocal_witness_all_intertwining_relations", M.T == M and M*A == -A*M and M*B == -B*M and M*O == O.T*M)
check("polar_square_commutes_with_source_and_clock", M**2*A == A*M**2 and M**2*B == B*M**2 and M**2*O == O*M**2)
# Thus U=M(M^2)^(-1/2) is an exact real orthogonal involution by functional
# calculus. Only its displayed finite matrix entries are evaluated numerically.
mn = np.array(M, dtype=float)
me, mv = np.linalg.eigh(mn)
U = (mv*np.sign(me))@mv.T
nonlocal_res = {"involution": residual(U@U-np.eye(16)), "odd_A": residual(U@An@U+An),
    "odd_B": residual(U@Bn@U+Bn), "reverse_clock": residual(U@On@U-On.T)}
check("polar_reflection_numeric_regression", max(nonlocal_res.values()) < 1e-10)
C = thermal(-1j*(An+Bn/8), 1)
check("nonlocal_reflection_complements_deployed_covariance", residual(U@C@U+C-np.eye(16)) < 1e-10)
boundary = np.diag([0]*10+[1]*6)
mixing = residual(U@boundary-boundary@U)
check("nonlocal_witness_not_boundary_preserving", mixing > 1e-3)
DATA["nonlocal_witness"] = {"exact_M": [[str(v) for v in row] for row in M.tolist()],
    "det_M": str(M.det()), "basis_dimension": len(basis), "selection": list(range(1,19)),
    "definition": "U = M (M^2)^(-1/2)", "residuals": nonlocal_res,
    "boundary_commutator": mixing,
    "scope": "source-dependent noncanonical real reflection; reverses rather than commutes with C6; no geometric locality proof"}

# Separate parent covariance from the full KMS Hamiltonian family above.
# Existing v911 freedom theorem concerns this covariance block family.
J2 = sp.Matrix([[0,1],[-1,0]])
CC = sp.kronecker_product(sp.eye(5),J2)
BB = sp.kronecker_product(sp.eye(3),J2)
V = B[:10,10:]
kappa, mass, t = sp.symbols("kappa mass t", real=True)
Aparent = (kappa*CC).row_join(t*V).col_join((-t*V.T).row_join(mass*BB))
g = sp.diag(CC,sp.eye(6))
Uframe = g*U0*g.T
check("parent_transported_frame_odd_symbolically", Uframe*Aparent*Uframe == -Aparent)
check("parent_fixed_pair_swap_fails_symbolically", U0*Aparent*U0 != -Aparent)
sample = Aparent.subs({kappa:sp.Rational(1,2),mass:sp.Rational(1,2),t:sp.Rational(1,20)})
Cs = (np.eye(16)+1j*np.array(sample,dtype=float))/2
check("parent_covariance_faithful", np.linalg.eigvalsh(Cs).min()>0 and np.linalg.eigvalsh(Cs).max()<1)
check("parent_transported_frame_complements_covariance", residual(np.array(Uframe,dtype=float)@Cs@np.array(Uframe,dtype=float)+Cs-np.eye(16))<1e-12)
DATA["parent_family"] = {"different_from_full_KMS_family": True,
    "Uframe": "diag(J2,J2,J2,J2,J2,I6) U0 diag(J2,J2,J2,J2,J2,I6)^T",
    "status": "exact identity on parent family; physical frame selection not established"}

# A genuine spatial reflection in the CURRENT QWZ finite-cylinder source.
# This is a different candidate/model, not an identification with the 16-mode
# bit compiler. U=Ry tensor sigma_y reverses y and acts on the onsite spinor.
qwz = read_module("audit_qwz", "verification/v998_seam_modular_closure.py")
SX = sp.Matrix([[0,1],[1,0]])
SY = sp.Matrix([[0,-sp.I],[sp.I,0]])
SZ = sp.diag(1,-1)
Tx = SX/(2*sp.I)-SZ/2
Ty = SY/(2*sp.I)-SZ/2
check("QWZ_local_Pauli_identities_exact", SY**2==sp.eye(2) and SY*SX*SY==-SX and SY*SZ*SY==-SZ and SY*Ty.conjugate().T*SY==-Ty and SY*Tx*SY==-Tx)
# Local identities prove full reflection for any uniform real MASS, any p,
# any finite width; cylinder Nx and twist alpha unaffected by y reflection.
qrows=[]
qcompressed=[]
for ny in (3,4,8,12):
    qwz.NY=ny
    uy=np.kron(np.eye(ny)[::-1],np.array(SY,dtype=complex))
    # Exact p=0, MASS=1 edge anchors, used as a fixed compression for all p.
    W=np.zeros((2*ny,2),dtype=complex)
    W[:2,0]=np.array([1,-1])/np.sqrt(2)
    W[-2:,1]=np.array([1,1])/np.sqrt(2)
    Uedge=W.conj().T@uy@W
    check(f"QWZ_two_edge_subspace_invariant_Ny{ny}", residual(uy@W-W@Uedge)<1e-12)
    for momentum in (0,.2,.7,1.3,2.4):
        H=qwz.strip_hamiltonian(momentum)
        C0=qwz.fermi_projector(H)
        for beta in (.5,1,2):
            C=thermal(H,beta)
            Cp=W.conj().T@C@W
            Kp=modular(Cp)
            qrows.append({"ny":ny,"p":momentum,"beta":beta,
                "Hamiltonian":residual(uy@H@uy+H),
                "covariance":residual(uy@C@uy+C-np.eye(2*ny)),
                "ground_covariance":residual(uy@C0@uy+C0-np.eye(2*ny))})
            qcompressed.append({"ny":ny,"p":momentum,"beta":beta,
                "covariance":residual(Uedge@Cp@Uedge+Cp-np.eye(2)),
                "modular":residual(Uedge@Kp@Uedge+Kp),
                "one_edge_scalar_defect":float(abs(2*Cp[0,0]-1)),
                "compression_log_defect":residual(Kp-W.conj().T@(beta*H)@W)})
check("QWZ_source_grid_60_Hamiltonian_and_covariance_wards", len(qrows)==60 and max(max(r[k] for k in ('Hamiltonian','covariance','ground_covariance')) for r in qrows)<1e-11)
check("QWZ_invariant_compression_keeps_modular_reflection", max(max(r['covariance'],r['modular']) for r in qcompressed)<1e-10)
check("QWZ_single_edge_not_internal_complementary", min(r['one_edge_scalar_defect'] for r in qcompressed if r['p']==.7)>.01)
check("compression_and_modular_log_not_interchangeable", max(r['compression_log_defect'] for r in qcompressed)>.01)
DATA['qwz_strip_grid']=qrows
DATA['qwz_compression_grid']=qcompressed

qwz.NY=4
cylinders=[]
for nx in (4,8,12):
    for alpha in (.25,.75):
        H=qwz.cylinder_hamiltonian(nx,alpha)
        uu=np.kron(np.eye(nx),np.kron(np.eye(qwz.NY)[::-1],np.array(SY,dtype=complex)))
        C=thermal(H,1)
        cylinders.append({'nx':nx,'ny':qwz.NY,'alpha':alpha,
            'H':residual(uu@H@uu+H),'C':residual(uu@C@uu+C-np.eye(len(H)))})
check("QWZ_real_space_twisted_cylinders", max(max(r['H'],r['C']) for r in cylinders)<1e-11)
DATA['qwz_cylinders']=cylinders

# Symmetry-breaking local boundary perturbation: diagnostic, not claimed
# admissible under all TFPT conditions. Its nonzero trace rules out ANY
# unitary anticommuting Hamiltonian symmetry on this finite space.
H=qwz.strip_hamiltonian(.7)
pert=np.zeros_like(H);pert[:2,:2]=.1*np.eye(2)
Hp=H+pert
uu=np.kron(np.eye(qwz.NY)[::-1],np.array(SY,dtype=complex))
Cp=thermal(Hp,1)
defect=residual(uu@Cp@uu+Cp-np.eye(len(Hp)))
check("boundary_potential_breaks_QWZ_reflection", defect>1e-3 and abs(np.trace(Hp)-.2)<1e-12)
# Ground projector has eigenvalues 0/1: a global finite modular logarithm
# cannot be obtained by silently clipping them.
C0=qwz.fermi_projector(H)
check("QWZ_ground_projector_not_faithful", residual(C0@C0-C0)<1e-12 and np.linalg.eigvalsh(C0).min()<1e-12)
DATA['qwz_controls']={'boundary_covariance_defect':defect,'trace_perturbed_H':float(np.trace(Hp).real),
    'ground_modular_log':'not defined on full finite one-particle space; no clipping',
    'source_typing':'finite QWZ regulator, not identified with iota=(12Y-I)/5 or full physical TFPT seam'}

source_files=["seam_covariance_probe.py","seam_source.py"]
DATA['provenance']=src['provenance']
DATA['source_hashes']={f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in source_files}
DATA['external_source_hashes']={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in (
    'verification/v998_seam_modular_closure.py','verification/v911_wiring_freedom.py','verification/v258_dirac_covariance_induction.py')}
result={'boundary':'Finite mathematical identities and finite source models; no RH/continuum/factoring claim',
    'checks':CHECKS,'passed':sum(r['passed'] for r in CHECKS),'total':len(CHECKS),'data':DATA,
    'versions':{'sympy':sp.__version__,'numpy':np.__version__}}
(HERE/'seam_covariance_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f"{result['passed']}/{result['total']} passed. NO RH CLAIM.",flush=True)
raise SystemExit(0 if result['passed']==result['total'] else 1)
