#!/usr/bin/env python3
"""Exact native-input tests, not a physical origin or TOE certificate."""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import ast
import hashlib
import json
import sys
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
checks={}
def ck(name, value):
    checks[name]=bool(value)
    if not value:
        raise RuntimeError(name)

def main():
    eta=S.diag(*([1]*9+[-1]))
    grade=S.Matrix([2,2,2,2,2,0,0,0,3,3])
    ys=S.Matrix([-S.Rational(1,3)]*3+[S.Rational(1,2)]*2+[0]*3)
    roots=[]
    for i,j in combinations(range(8),2):
        for si,sj in product([-1,1],repeat=2):
            r=S.zeros(8,1);r[i]=si;r[j]=sj;roots.append(r)
    roots.extend(S.Matrix(r)/2 for r in product([-1,1],repeat=8) if r.count(-1)%2==0)
    ck('original_E8_root_count',len(roots)==240)
    candidates=[];global_rows=[];chosen=[]
    for plus in combinations(range(9),3):
        n=S.Matrix([1 if i in plus else -1 for i in range(9)]+[3])
        ck('minimal_null_'+','.join(map(str,plus)),sum(n)==0 and n.dot(n)==18 and (n.T*eta*n)[0]==0)
        if grade.dot(n)%4: continue
        c=sum(n[i]==1 for i in range(3));w=sum(n[i]==1 for i in range(3,5));f=sum(n[i]==1 for i in range(5,8))
        ck('glue_forces_aux_minus_'+','.join(map(str,plus)),n[8]==-1 and c+w+f==3)
        y=S.Rational(c,3)-S.Rational(w,2)
        Y=S.Matrix(list(ys)+[y,y])
        ck('required_y_'+','.join(map(str,plus)),Y.dot(n)==0)
        oriented=(c+w)%2==1
        row={'n':list(map(int,n)),'c':c,'w':w,'f':f,'y':str(y),'oriented':oriented}
        candidates.append(row)
        if y.q!=1: continue
        a=n[:8,0]
        defects=set()
        for p in roots:
            k=a.dot(p)/2
            lift=S.Matrix(list(p)+[-k,k])-k*n
            ck('global_lift_integral_'+str(len(global_rows))+'_'+str(roots.index(p)),all(z.q==1 for z in lift))
            ck('global_lift_hypercharge_'+str(len(global_rows))+'_'+str(roots.index(p)),Y.dot(lift)==ys.dot(p))
            defects.add(int((grade.dot(lift)-2*sum(p[:5]))%4))
        ck('oriented_full_root_test_'+str(len(global_rows)),defects==({0} if oriented else {0,2}))
        global_rows.append(row)
        if oriented: chosen.append(row)
    ck('56_glue_candidates',len(candidates)==56)
    ck('25_oriented_glue_candidates',sum(r['oriented'] for r in candidates)==25)
    ck('five_global_singlet_candidates',len(global_rows)==5)
    ck('global_hypercharge_counts',Counter(r['y'] for r in global_rows)==Counter({'-1':3,'0':1,'1':1}))
    wanted=[1,1,1,-1,-1,-1,-1,-1,-1,3]
    ck('unique_without_block_symmetry',len(chosen)==1 and chosen[0]['n']==wanted and chosen[0]['y']=='1')
    ck('fractional_countercandidate',any(r['oriented'] and r['y']=='1/6' for r in candidates))
    # Genuine group descent: a singlet sees the Z6 generator as exp(2*pi*i*y).
    ck('nonintegral_singlet_rejected',S.simplify(S.exp(2*S.pi*S.I*S.Rational(1,6))-1)!=0)
    # Read actual native cubic coefficients; no chosen replacement tensor.
    native=json.loads((ROOT/'experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/certificate.json').read_text())['cubic']
    rr=native['base_roots_doubled'];terms=native['monomials']
    ck('native_factorization_retained',native['factorization']=='C_(A,i)(B,j)(C,k) = d_ABC epsilon_ijk')
    ck('native_cubic_size',len(rr)==27 and len(terms)==45 and native['Ward_rank']==44)
    labels={}
    for i,r in enumerate(rr):
        if all(abs(t)==1 for t in r[:5]):
            occ=[(t+1)//2 for t in r[:5]]
            labels[i]={(0,0):'nu',(1,1):'Q',(2,0):'u',(0,2):'e',(2,2):'d',(3,1):'L'}[(sum(occ[:3]),sum(occ[3:]))]
    ck('actual_SM16_slots',Counter(labels.values())==Counter({'nu':1,'Q':6,'u':3,'e':1,'d':3,'L':2}))
    hd=[i for i,r in enumerate(rr) if r[:5]==[0,0,0,0,-2]]
    hu=[i for i,r in enumerate(rr) if r[:5]==[0,0,0,0,2]]
    ck('neutral_Higgs_components',hd==[12] and hu==[14])
    couplings=[]
    spinors=sorted(labels)
    sd=S.zeros(16);su=S.zeros(16)
    for tag,hh,mat in [('d',hd[0],sd),('u',hu[0],su)]:
        for term in terms:
            ids=term['indices']
            if hh not in ids:continue
            ij=[j for j in ids if j!=hh]
            if not all(j in labels for j in ij):continue
            i,j=ij;v=term['coefficient']
            mat[spinors.index(i),spinors.index(j)]=v
            mat[spinors.index(j),spinors.index(i)]=v
            couplings.append({'higgs':tag,'indices':ij,'species':[labels[i],labels[j]],'coefficient':v})
    ck('four_down_pairs',sum(x['higgs']=='d' for x in couplings)==4)
    ck('four_up_pairs',sum(x['higgs']=='u' for x in couplings)==4)
    ck('down_lepton_equal_coefficient_magnitudes',all(abs(x['coefficient'])==1 for x in couplings))
    ck('symmetric_internal_Higgs_tensors',sd.T==sd and su.T==su and sd.rank()==8 and su.rank()==8)
    h1,h2,h3=S.symbols('h1 h2 h3')
    h=S.Matrix([h1,h2,h3])
    A=S.Matrix(3,3,lambda i,j:sum(S.LeviCivita(i,j,k)*h[k] for k in range(3)))
    ck('family_skew',A.T==-A)
    ck('family_determinant_zero',A.det()==0)
    ck('family_right_null',A*h==S.zeros(3,1))
    norm=(h.conjugate().T*h)[0]
    ck('complex_singular_value_identity',S.simplify(A.conjugate().T*A-(norm*S.eye(3)-h*h.conjugate().T))==S.zeros(3))
    combined=S.kronecker_product(sd,A)
    ck('whole_48_field_coefficient_antisymmetric',combined.T==-combined)
    ck('weyl_symmetric_contraction_zero',combined+combined.T==S.zeros(48))
    # Required complementary coupling, retaining the FULL chiral mass block.
    ck('family_adjugate',A.adjugate()==h*h.T)
    b=S.Matrix(S.symbols('b1 b2 b3'));c=S.Matrix(S.symbols('c1 c2 c3'))
    heavy=S.symbols('M',nonzero=True)
    mass=A.row_join(b).col_join(c.T.row_join(S.Matrix([[heavy]])))
    overlap=(h.T*b)[0]*(c.T*h)[0]
    ck('full_mass_complement_identity',S.expand(mass.det()+overlap)==0)
    eff=A-b*c.T/heavy
    ck('reduced_mass_complement_identity',S.factor(eff.det()+overlap/heavy)==0)
    ck('heavy_mass_phase_cancels_in_full_mass_determinant',S.diff(mass.det(),heavy)==0)
    # The allowed internal one-Higgs singlet structures, not a spacetime lift.
    YL=-S.Rational(1,2);YH=S.Rational(1,2);YEc=S.Integer(1);YE=-YEc;Yec=S.Integer(1)
    ck('lepton_Higgs_heavy_hypercharge',YL-YH+YEc==0)
    ck('heavy_light_singlet_hypercharge',YE+Yec==0)
    ck('vectorlike_heavy_mass_hypercharge',YE+YEc==0)
    # Original mass-exponent matrix, extracted from its source AST assignment.
    tree=ast.parse((ROOT/'verification/v46_grand_mass_volume.py').read_text())
    kval=None
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='K' for t in node.targets) and isinstance(node.value,ast.Call):
            kval=ast.literal_eval(node.value.args[0]);break
    ck('native_mass_exponents',kval==[[4,2,0],[4,3,2],[5,3,2]])
    ck('native_positive_mass_determinant_powers',[sum(row) for row in kval]==[6,9,10])
    manifest=json.loads((HERE/'source_manifest.json').read_text())
    for item in manifest['files']:
        ck('pin:'+item['path'],hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'])
    result={'research_id':'UR.SOURCE.FLAVOR_ORIGIN.01','verdict':'PARTIAL','status':'PASS_EXACT_SCOPED_CONTROLS',
        'global_singlet_candidates':global_rows,'selected':chosen,'fractional_oriented_counterexamples':[r for r in candidates if r['y']=='1/6' and r['oriented']],
        'native_Higgs_couplings':couplings,'mass_exponents':kval,'family_higgs_matrix':str(A),
        'full_chiral_mass_determinant':str(-overlap),'full_Euclidean_source_determinant_computed':False,
        'direct_cubic_yukawa_identification':'REFUTED_FOR_STATED_LOCAL_SUBSTITUTION',
        'boundary_origin_selection':'UNIQUE_UNDER_GLOBAL_GROUP_AND_FIXED_GLUE_PREMISES',
        'full_upstream_cubic_checker_replayed':False,'physical_gates_closed':[],'complete_TFPT_solution':False,
        'checks':checks,'count':len(checks)}
    out=HERE/('certificate.optimized.json' if sys.flags.optimize else 'certificate.json')
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'count':len(checks),'unique_candidates':len(chosen),'direct_family_determinant':0,'output':str(out)}))

if __name__=='__main__':main()
