"""Exact countermodels at the Lie-algebra -> physical-carrier interface.

These reject claimed derivations, not the consistency of a declared hard-core
or edge-local model. No unrestricted TOE impossibility is asserted.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import argparse, json, hashlib
import sympy as s

HERE=Path(__file__).resolve().parent
CHECKS=[]
def need(ok,name):
    if not bool(ok):raise RuntimeError(name)
    CHECKS.append(name)
def bracket(a,b):return a*b-b*a
def matrix_unit(i,j):
    a=s.zeros(3);a[i,j]=1;return a

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'core_origin_audit.json');args=p.parse_args()
    alpha=[Q(1,2)]*8
    beta=[Q(1,2)]*5+[Q(-1,2),Q(-1,2),Q(1,2)]
    norm=lambda v:sum(x*x for x in v)
    need(norm(alpha)==norm(beta)==2,'both same-place E8 carrier vectors have root norm2')
    need(sum(x*y for x,y in zip(alpha,beta))==1,'same-place roots have inner product1')
    need(norm([x+y for x,y in zip(alpha,beta)])==6,'root sum is not a root')
    need(norm([x-y for x,y in zip(alpha,beta)])==2,'root difference is a root')
    # The root-angle subsystem is A2. Its faithful adjoint action already
    # separates vanishing brackets from vanishing products of actions.
    ea,eb,ema=matrix_unit(0,1),matrix_unit(0,2),matrix_unit(1,0)
    need(bracket(ea,eb)==s.zeros(3),'commuting same-angle root generators')
    need(bracket(ea,bracket(eb,ema))==-eb,'ad(Ealpha)ad(Ebeta) is nonzero despite absent root sum')
    need(bracket(ea,bracket(ea,ema))==-2*ea,'even repeated root action is not hard-core nilpotent')
    # Glue with half components is distinct from half the glue generator.
    need(norm(alpha)/2==1 and norm([x/2 for x in alpha])/2==Q(1,4),
         'E8 half-coordinate current h1 is not quarter-coordinate half-glue h1/4')
    # A single boson mode plus explicit pair-hole states has four orthogonal
    # configurations. The address can reside in the material subsystem.
    basis=list(product(range(2),repeat=2))  # h0,h1: pair converted to mediator
    edge=s.zeros(4);shared=s.zeros(4);normalized=s.zeros(4)
    embedded=[]
    for col,(h0,h1) in enumerate(basis):
        n=h0+h1;embedded.append((h0,h1,n))
        for e in range(2):
            h=[h0,h1]
            if h[e]==0:
                h[e]=1;row=basis.index(tuple(h))
                edge[row,col]=edge[col,row]=1
                shared[row,col]=shared[col,row]=s.sqrt(n+1)
                normalized[row,col]=normalized[col,row]=1
    need(len(set(embedded))==4,'one root-labelled boson mode plus matter holes stores four orthogonal configurations')
    need(normalized==edge,'normalized shared shift with matter records reproduces two edge occupancies exactly')
    need(shared!=edge and s.trace(shared**4)!=s.trace(edge**4),'linear shared-boson vertex is dynamically distinct')
    # The normalized shift is an additional nonlinear vertex contract, not
    # secretly the same linear E8-bracket coupling.
    for states in [edge,shared,normalized]:need(states==states.T,'each alternative has a genuine adjoint Hamiltonian')
    # One spatial/internal root generator vs two wavepacket modes is another
    # elementary distinction: the root space remains 1D in g, not in g⊗M.
    one_root=s.Matrix([[1]])
    first=s.kronecker_product(one_root,s.Matrix([1,0]));second=s.kronecker_product(one_root,s.Matrix([0,1]))
    need(s.Matrix.hstack(first,second).rank()==2,'root-label dimension1 does not fix physical multiplicity space')
    output={
      'scope':'no derivation of occupancy, mode multiplicity, or vertex normalization from root counting alone',
      'hard_core_counterexample':'[Ea,Eb]=0 but ad(Ea)ad(Eb)(E-a)=-Eb !=0',
      'E8_vectors':{'alpha':list(map(str,alpha)),'beta':list(map(str,beta))},
      'glue_weights':{'half_components':'h=1','half_glue_generator':'h=1/4'},
      'one_boson_mode_plus_matter_states':embedded,
      'edge_H':str(edge),'linear_shared_H':str(shared),'normalized_shared_H':str(normalized),
      'extra_assumptions':[
        'hard-core restriction or fermionic occupancy realization',
        'single-particle Hilbert space, spatial/memory multiplicities, and chosen Fock functor',
        'linear versus normalized/nonlinear vertex and local conservation contract'],
      'not_claimed':['fullE8native implementation of the toy alternatives','native half-charge theorem','TOE no-go'],
      'checks':CHECKS,'check_count':len(CHECKS),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
if __name__=='__main__':main()
