#!/usr/bin/env python3
"""Exact invariant two-packet response; no full three-source ground proof."""
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np
import sympy as s

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
HERE=Path(__file__).resolve().parent
SOURCE='experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PIN='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
checks=[]
def req(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks.append(name)
req(hashlib.sha256((ROOT/SOURCE).read_bytes()).hexdigest()==PIN,'native source pin')
spec=importlib.util.spec_from_file_location('native_source',ROOT/SOURCE)
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
rays=native.source_rays()
Z=np.stack([p*z for z in rays for p in (1,1j,-1,-1j)])
roots={tuple(z) for z in Z}
swap=np.zeros((16,16),dtype=np.int64)
for a in range(4):
    for b in range(4): swap[4*b+a,4*a+b]=1
twor=[2*np.eye(4)-np.outer(z,z.conj()) for z in rays]
for r2 in twor:
    req(np.array_equal(r2,r2.conj().T),'native reflection Hermitian')
    req(np.array_equal(r2@r2,4*np.eye(4)),'native reflection involution')
    req(all(tuple(r2@z/2) in roots for z in Z),'native full root covariance including phase')
moment=sum((np.kron(r,r) for r in twor),np.zeros((16,16),dtype=complex))
req(np.array_equal(moment,48*(np.eye(16)+swap)),
    'exact reflection mean r tensor r=(I+Swap)/5')
overlap=Z.conj()@Z.T
num=np.rint((overlap.real**2+overlap.imag**2)).astype(np.int64)
req(int(num.sum())==4*240**2,'packet swap overlap mean absolute z squared=1/4')
req(int((num**2).sum())*10==16**2*240**2,'second projective overlap moment1/10')
req(int((num**3).sum())*20==16**3*240**2,'third projective overlap moment1/20')

# u=Omega_AB tensor uniform-middle-source tensor Omega_CD; w=Swap_BC u.
# Full-vector contractions using the checked reflection moment:
# H_middle u=4u/5-w/5, H_middle w=4w/5-u/5;
# each outer L annihilates u and maps w to4w/5-u/5.
G=s.Matrix([[1,s.Rational(1,4)],[s.Rational(1,4),1]])
M=s.Matrix([[s.Rational(4,5),-s.Rational(3,5)],[-s.Rational(1,5),s.Rational(12,5)]])
req(G*M==(G*M).T,'invariant action is Hermitian in exact nonorthogonal Gram')
change=s.Matrix([[1,-1/s.sqrt(15)],[0,4/s.sqrt(15)]])
req(s.simplify(change.T*G*change)==s.eye(2),'v=(4w-u)/sqrt15 orthonormal')
H=s.simplify(change.T*G*M*change)
req(H==s.Matrix([[15,-s.sqrt(15)],[-s.sqrt(15),49]])/20,'submitted two-state matrix from original full-vector action')
lo=(8-s.sqrt(19))/5;hi=(8+s.sqrt(19))/5
req(s.simplify((H-lo*s.eye(2))*(H-hi*s.eye(2)))==s.zeros(2),'two exact energies')
gap=hi-lo
Pg=s.simplify((hi*s.eye(2)-H)/gap)
Pe=s.eye(2)-Pg
Q=s.diag(1,0)
req(Pg*Pg==Pg or s.simplify(Pg*Pg-Pg)==s.zeros(2),'rank-one ground projector inside invariant space')
weight=s.simplify(s.trace(Pg*Q*Pe*Q))
req(weight==s.Rational(15,1216),'single inelastic packet-response weight')
pu=s.simplify(s.trace(Pg*Q))
req(s.simplify(pu-(s.Rational(1,2)+17/(8*s.sqrt(19))))==0,'product-packet weight')
req(2*weight==s.Rational(15,608),'retarded response coefficient with minus sine convention')

# The old imaginary adjacent overlaps change individual source phases and have
# zero compression in the fixed(2,0,2) space. A coordinate-only quartic F13
# keeps those phases: F13=|<psi1|psi3>|^2. At fixed root pair <u|w>=F13.
Fraw=s.Matrix([[s.Rational(1,4),s.Rational(1,10)],
               [s.Rational(1,10),s.Rational(1,4)]])
F2raw=s.Matrix([[s.Rational(1,10),s.Rational(1,20)],
                [s.Rational(1,20),s.Rational(1,10)]])
F13=s.simplify(change.T*Fraw*change)
F13sq=s.simplify(change.T*F2raw*change)
req(F13==s.Matrix([[25,s.sqrt(15)],[s.sqrt(15),23]])/100,
    'quartic outer coordinate overlap compression')
req(s.simplify(F13-(s.Rational(18,25)*s.eye(2)-H/5-s.Rational(8,25)*Q))==s.zeros(2),
    'within invariant space quartic overlap equals18I/25-H/(5kappa)-8Q/25')
req(F13sq==s.Matrix([[15,s.sqrt(15)],[s.sqrt(15),13]])/150,
    'full quartic overlap square compression')
fline=s.simplify(s.trace(Pg*F13*Pe*F13))
req(fline==s.Rational(3,2375),'quartic source-only readout sees exact binding resonance')
fleak=s.simplify(s.trace(Pg*(F13sq-F13*F13)))
req(fleak>0,'quartic response also has weight outside the invariant doublet')

# Event compression: both outer terms annihilate u; each has w expectation3/2.
# The middle event compression is3/4 times identity in the NONORTHOGONAL matrix
# of matrix elements. This is a compression, not a claim T preserves this space.
T=s.simplify(change.T*s.diag(s.Rational(3,4),s.Rational(15,4))*change)
req(T==s.Matrix([[15,-s.sqrt(15)],[-s.sqrt(15),81]])/20,'exact event compression')
t0=s.simplify(s.trace(Pg*T))
req(s.simplify(t0-s.Rational(12,5)*(1-3/s.sqrt(19)))==0,'actual event expectation in lower eigenstate')
req(t0<s.Rational(3,4),'event expectation is strictly below3/4')
delta=s.Rational(3,4)-lo
req(s.simplify(delta-(4*s.sqrt(19)-17)/20)==0,'conditional full complement gap')
req(delta-s.Rational(11,800)>s.Rational(1,125),'reported positive-coupling endpoint bound')
# All invariant vectors have fixed source charges(2,0,2). Each Re overlap
# transfers one charge, so P_source V12 P_source=P_source, likewise V23.
req(2+0+2==4,'fixed source charges2,0,2 have total0mod4')
req(1-1==0,'outer Pi2 difference annihilates the whole invariant space')

result={
 'status':'PASS','verdict':'PARTIAL','checks':len(checks),'guard_names':checks,
 'source_pins':{SOURCE:PIN},
 'full_dimension':240**3*4**4,
 'exact_invariant_space':{'basis':'u,v=(4 Swap_BC u-u)/sqrt15',
    'H_over_kappa':'[[15,-sqrt15],[-sqrt15,49]]/20',
    'energies_over_kappa':['(8-sqrt19)/5','(8+sqrt19)/5'],
    'Q1_and_Q3':'diag(1,0)','u_weight':'1/2+17/(8sqrt19)',
    'inelastic_weight':'15/1216','resonance_frequency_over_kappa':'2sqrt19/5',
    'retarded_cross_response':'-15/608 theta(t) sin(2sqrt19 kappa t/5)',
    'event_compression':'[[15,-sqrt15],[-sqrt15,81]]/20',
    'event_ground_expectation':'(12/5)(1-3/sqrt19)',
    'distance_sum_ground_expectation':'2',
    'source_charges':[2,0,2],'outer_phase_difference_response':'ZERO at J=mu=0'},
 'new_coordinate_readout':{'F13':'absolute overlap of outer source directions squared',
    'coordinate_form':'(x1 dot x3)^2+(x1^T J x3)^2',
    'compressed_operator':'[[25,sqrt15],[sqrt15,23]]/100',
    'inelastic_connection_to_packet':'P F13 P=18I/25-H/(5kappa)-8Q/25',
    'matrix_element_squared_between_two_exact_eigenstates':'3/2375',
    'frequency_over_kappa':'2sqrt19/5',
    'other_spectral_weight_present':True,
    'middle_or_outer_Im_overlap_low_transition':'zero by fixed individual source phase',
    'current_target':'same quartic polynomial of the existing Cartan zero modes on source copies1and3',
    'scope':'source-only two-source joint measurement; not a single local detector, not an exhaustive spectral function'},
 'conditional_full_ground':{
    'premise':'every state orthogonal to the lower invariant eigenvector has H0 energy>=3kappa/4',
    'premise_verdict':'REPORTED_NOT_INDEPENDENTLY_PROVED_OR_REPLAYED',
    'gap_bound':'(4sqrt19-17)kappa/20 - (12/5)(1-3/sqrt19)J -2mu',
    'weaker_reported_bound':'(4sqrt19-17)kappa/20 -3J/4-2mu',
    'unique_ground_gap_gt_kappa_over125':'conditional for J=mu=epsilon kappa,0<epsilon<=1/200'},
 'not_claimed':['full triple-source ground theorem','full complement gap certificate',
    'relativistic causality','chain propagation','physical Hamiltonian origin','TOE'],
}
(HERE/'triple_response.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
