"""Exact countermodels to root-dimension and charge-normalization inference."""
from itertools import product,combinations
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    checks.append(label)

def main():
    # Any E8 root contains an sl2 subalgebra; four exterior location labels
    # do not change the internal root dimension of that underlying algebra.
    E=s.Matrix([[0,1],[0,0]]);G=E.T;H=E*G-G*E
    Ps=[]
    for i in range(4):
        p=s.zeros(4);p[i,i]=1;Ps.append(p)
    Es=[s.kronecker_product(E,p) for p in Ps]
    Gs=[s.kronecker_product(G,p) for p in Ps]
    globalH=s.kronecker_product(H,s.eye(4))
    for i,j in product(range(4),repeat=2):
        need(Es[i]*Gs[j]-Gs[j]*Es[i] == (s.kronecker_product(H,Ps[i]) if i==j else s.zeros(8)),
             'current algebra localized bracket '+str((i,j)))
    for i in range(4):
        need(globalH*Es[i]-Es[i]*globalH==2*Es[i], 'same internal root weight at location '+str(i))
    need(s.Matrix.hstack(*[e.reshape(64,1) for e in Es]).rank()==4,'four independent spatial modes with one internal root generator')
    roots=set()
    for i,j in combinations(range(8),2):
        for a,b in product([-2,2],repeat=2):
            v=[0]*8;v[i]=a;v[j]=b;roots.add(tuple(v))
    for v in product([-1,1],repeat=8):
        if v.count(-1)%2==0:roots.add(v)
    alpha=(1,)*8
    beta=(1,)*5+(-1,-1,1)
    need(alpha in roots and beta in roots,'same-place root witness uses two actual E8 spinor roots')
    need(tuple(a+b for a,b in zip(alpha,beta)) not in roots,'same-place sum is not a root')
    need(tuple(a-b for a,b in zip(alpha,beta)) in roots,'same-place difference is a root')
    need(F(sum(a*b for a,b in zip(alpha,beta)),4)==1,'same-place root inner product one')
    # Concrete A2 subalgebra witness: vanishing bracket is not vanishing product
    # of operators in the adjoint representation.
    A=s.zeros(3);A[0,1]=1
    B=s.zeros(3);B[0,2]=1
    Z=s.zeros(3);Z[1,0]=1
    comm=lambda a,b:a*b-b*a
    need(comm(A,B)==s.zeros(3),'A2 raising generators commute')
    need(comm(A,comm(B,Z))==-B,'their adjoint operators have a nonzero ordered product')
    glue=tuple(F(1,2) for _ in range(8));half=tuple(x/2 for x in glue)
    need(sum(x*x for x in glue)==2,'actual E8 glue root squared norm two')
    need(sum(x*x for x in glue)/2==1,'actual E8 glue conformal weight one')
    need(glue[0]==F(1,2),'actual E8 glue has half-unit individual Cartan component')
    need(sum(x*x for x in half)/2==F(1,4),'halving the whole glue vector instead gives weight one quarter')
    need(sum(half[i] for i in [0,1])==F(1,2),'quarter-vector is not integral against a D5 root')
    out={'status':'EXACT_INFERENCE_COUNTERMODELS','checks':checks,'count':len(checks),
         'root_dimension':{'base_internal_root_dimension':1,'external_label_dimension':4,
            'active_modes_for_the_same_internal_root':4,
            'new_label_is_an_explicit_resource':True,
            'countermodel_disproves':'root-space dimension alone fixes the spatial/Fock mode count',
            'does_not_disprove':'Fock over one explicitly frozen finite adjoint has one mode per basis generator'},
         'hard_core':{'sum_not_root_proves':'vanishing Lie bracket',
                      'does_not_prove':'vanishing product or exclusion of double occupation',
                      'already_postulated_hard_core_model_refuted':False},
         'half_charge':{'glue_vector':['1/2']*8,'glue_norm_squared':'2','glue_weight':'1',
                        'half_glue_vector':['1/4']*8,'half_glue_weight':'1/4',
                        'ordinary_half_Cartan_charge_equals_half_glue_generator':False,
                        'universal_T2_obstruction_proved':False,
                        'native_T2_field_domain_energy_and_charge_mapping_proved':False}}
    (HERE/'source_claims.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
