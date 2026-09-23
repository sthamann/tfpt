"""Exact limited control algebra and a minimal charged-reference witness.

This does not certify that these laboratory controls are primitive compiler
instructions. Composition of a neutral alphabet cannot synthesize charge.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

checks=[]
def need(ok,label):
    if not bool(ok): raise RuntimeError(label)
    checks.append(label)

# The rational representative is similar to the Hermitian C3 singular blocks.
# Multiplicities and C3 spectrum are inherited, not re-derived by this 8x8 test.
B=s.diag(0,1,0,1,0,1,0,1)
X=s.diag(s.zeros(1),s.zeros(1),s.Matrix([[0,7],[1,0]]),
         s.Matrix([[0,10],[1,0]]),s.Matrix([[0,12],[1,0]]))
basis=[s.eye(8)]
flat=s.Matrix(64,1,list(basis[0]))
cursor=0
while cursor<len(basis):
    for gen in (X,B):
        candidate=basis[cursor]*gen
        expanded=flat.row_join(s.Matrix(64,1,list(candidate)))
        if expanded.rank()>len(basis):
            basis.append(candidate);flat=expanded
    cursor+=1
need(len(basis)==14,'complete two-generator algebra dimension fourteen in faithful spectral representative')

# Neutral algebra: every word commutes with N by the Leibniz commutator law.
# Independent tiny exact witness demonstrates source/reference distinction.
ns=s.diag(0,0,1,1)
nr=s.diag(0,1,0,1)
exchange=s.zeros(4);exchange[1,2]=exchange[2,1]=1
need((ns+nr)*exchange==exchange*(ns+nr),'joint reference exchange is neutral')
need(ns*exchange!=exchange*ns,'joint exchange changes the source sector')
source_energy,reference_energy,mu,lam=s.symbols('es er mu lambda',real=True)
one_charge=s.Matrix([[reference_energy,lam],[lam,source_energy+mu]])
need(one_charge[1,1]-one_charge[0,0]==source_energy+mu-reference_energy,'source chemical shift is relative detector detuning')
joint_shift=one_charge+mu*s.eye(2)
need(joint_shift[1,1]-joint_shift[0,0]==one_charge[1,1]-one_charge[0,0],'common conserved-charge shift is unobservable')
centered=one_charge-s.trace(one_charge)*s.eye(2)/2
need(s.simplify(centered**2-((source_energy+mu-reference_energy)**2/4+lam**2)*s.eye(2))==s.zeros(2),
     'exact two-level exchange frequency and detuning')

result={'status':'PASS','checks':len(checks),'check_labels':checks,
        'known_model_controls':['pair conversion X','Nb phase evolution or occupation selection, if granted','number-preserving symmetry/Clock lifts, if granted'],
        'neutral_alphabet_consequence':'every number-preserving word and selected branch maps H_N to itself; cannot send empty N0 to native ground N64',
        'important_qualification':'U1-covariant channels may have charged Kraus operators; the obstruction requires each implemented branch to conserve source N',
        'primitive_operations_not_proved':['source H as time generator','independent modewise controls','initial filled F64 preparation','charged source-reference exchange','imaginary-time filtering as an actual instrument'],
        'minimal_reference_candidate':'lambda*(c^dagger f_r+f_r^dagger c), with explicit detector energy and initial state',
        'state_preparation':'unitary evolution by H keeps ground fidelity constant; normalized exp(-tau H) F64 converges but needs an instrument/resource derivation',
        'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
