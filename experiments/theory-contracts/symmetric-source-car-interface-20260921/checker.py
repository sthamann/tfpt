#!/usr/bin/env python3
"""Explicit grade-two source to four-Majorana state map in the existing D8 CAR realization.

Uses a fixed bosonization convention. Source column cocycles and a common
phase per charge are suppressed only for same-charge Gram/range checks.
Physical P1 selection and the historical all-operator phase dictionary are not proved.
"""
from itertools import product, combinations, combinations_with_replacement
from collections import Counter,defaultdict
from pathlib import Path
import json,hashlib,argparse
import sympy as s

checks=[]
def need(x,label):
    if not bool(x): raise RuntimeError(label)
    checks.append(label)
def sign_perm(xs):return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def wedge_matrix(U,p):
    rows=list(combinations(range(U.rows),p))
    return s.Matrix(len(rows),len(rows),lambda i,j:U.extract(rows[i],rows[j]).det()).applyfunc(s.simplify)
def add(a,b):return tuple(x+y for x,y in zip(a,b))

def main():
    # Real six-plane x1,y1,x2,y2,x3,y3, charged columns (x +/- i y)/sqrt2.
    trip=list(combinations(range(6),3));index={v:i for i,v in enumerate(trip)}
    star=s.zeros(20)
    for j,t in enumerate(trip):
        c=tuple(k for k in range(6) if k not in t)
        star[index[c],j]=sign_perm(t+c)
    U=s.zeros(6)
    for k in range(3):
        U[2*k,2*k]=U[2*k,2*k+1]=1/s.sqrt(2)
        U[2*k+1,2*k]=s.I/s.sqrt(2);U[2*k+1,2*k+1]=-s.I/s.sqrt(2)
    W=wedge_matrix(U,3);K=(W.H*(s.I*star)*W).applyfunc(s.simplify)
    need(K*K==s.eye(20) and K.H==K,'family Hodge chirality is a Hermitian involution')
    P=(s.eye(20)+K)/2
    need(P.rank()==10,'positive family three-form chirality rank ten')
    high=s.zeros(20,1);high[index[(0,2,4)]]=1
    need(P*high==high,'chosen chirality contains +e1+e2+e3 highest weight')
    # Family torus acts with charges +/-1 on its vector modes.
    char=Counter()
    for i,t in enumerate(trip):
        q=tuple(sum((1 if a%2==0 else -1) for a in t if a//2==k) for k in range(3))
        char[q]+=P[i,i]
    spin3=[t for t in product((1,-1),repeat=3) if t.count(-1)%2==0]
    ten=Counter(tuple((x+y)//2 for x,y in zip(a,b)) for a,b in combinations_with_replacement(spin3,2))
    need(char==ten,'Hodge range has exact Sym2(4) weight character')
    roots=[t for t in product((1,-1),repeat=8) if t[:5].count(-1)%2==0 and t[5:].count(-1)%2==0]
    native=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py')
    need(hashlib.sha256(native.read_bytes()).hexdigest()=='380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672','original marked source SHA256')
    prefix,sep,_=native.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(sep),'native source prefix boundary')
    ns={'__file__':str(native),'__name__':'native_car_interface_prefix'}
    exec(compile(prefix,str(native),'exec',optimize=0),ns)
    need(set(roots)==set(map(tuple,ns['FW'].tolist())),'same 64 marked source weights')
    blocks=defaultdict(list)
    for r,t in combinations_with_replacement(roots,2):blocks[add(r,t)].append((r,t))
    spectra=Counter();car_basis_used=set();types=Counter();nnz=0
    charge_counts=Counter();energy_counts=Counter();sector_charges={'100':Counter(),'720':Counter()}
    for q2,ps in blocks.items():
        q=tuple(a//2 for a in q2)
        cols=[]
        source_gram=s.zeros(len(ps))
        for r,t in ps:
            d=sum(a*b for a,b in zip(r,t))//4
            occupied=[2*k+(0 if a==1 else 1) for k,a in enumerate(q) if a]
            col={}
            if d==0:
                need(len(occupied)==4,'orthogonal roots give four distinct charged creators')
                col[tuple(occupied)]=s.sqrt(2)
            elif d==-1:
                need(len(occupied)==2,'root-sum channel has two occupied charge directions')
                for k in range(8):
                    v=(r[k]-t[k])//2
                    if v:
                        need(q[k]==0,'oscillator is orthogonal to occupied charge coordinates')
                        seq=[2*k,2*k+1]+occupied
                        col[tuple(sorted(seq))]=s.Rational(v,1)/s.sqrt(2)*sign_perm(seq)
            else: need(d in (1,2),'vanishing current-product type')
            # Project all output coordinates onto 3+1 or 1+3 Hodge-plus sector.
            proj=defaultdict(lambda:s.Integer(0))
            for basis,value in col.items():
                cq=tuple(sum((1 if a%2==0 else -1) for a in basis if a//2==k) for k in range(8))
                need(cq==q,'all eight Cartan charges preserved on actual CAR coordinates')
                nspin=sum(x<10 for x in basis)
                need(nspin in (1,3),'all nonzero columns have 1+3 or 3+1 species content')
                if nspin==3:proj[basis]+=value
                else:
                    a=basis[0];ft=tuple(x-10 for x in basis[1:]);j=index[ft]
                    for i,target in enumerate(trip):
                        if P[i,j]:proj[(a,)+tuple(x+10 for x in target)]+=P[i,j]*value
            proj={k:s.simplify(v) for k,v in proj.items() if s.simplify(v)!=0}
            need(proj==col,'actual CAR column lies in 720 plus selected 100 range')
            car_basis_used.update(col);nnz+=len(col);cols.append(col)
        G=s.Matrix(len(ps),len(ps),lambda i,j:s.simplify(sum(s.conjugate(v)*cols[j].get(k,0) for k,v in cols[i].items())))
        d=sum(a*b for a,b in zip(*ps[0]))//4
        if d==-1:
            diffs=[tuple((a-b)//2 for a,b in zip(r,t)) for r,t in ps]
            source_gram=s.Matrix(len(ps),len(ps),lambda i,j:s.Rational(sum(a*b for a,b in zip(diffs[i],diffs[j])),2))
        elif d==0:source_gram=2*s.ones(len(ps))
        need(G==source_gram,'whole charge-block CAR Gram equals current-source Gram')
        for ev,m in G.eigenvals().items():
            spectra[str(ev)]+=m
            if ev:
                Q=sum(q);energy=s.Rational(2)-s.Rational(Q,4)
                charge_counts[str(Q)]+=m;energy_counts[str(energy)]+=m
                sector_charges['100' if ev==8 else '720'][str(Q)]+=m
    need(spectra=={'0':1260,'4':720,'8':100},'full CAR image spectrum agrees with source')
    # The Hodge ten uses four pure-charge and twelve mixed occupation
    # coordinates, not all twenty three-form coordinates.
    need(len(car_basis_used)==720+10*(4+12),'100+720 image uses 880 charged occupation coordinates')
    need(nnz==4000,'explicit CAR map retains all 4000 nonzero source entries')
    need(charge_counts=={'4':35,'2':200,'0':345,'-2':210,'-4':30},'complete charge census on the positive image')
    need(energy_counts=={'1':35,'3/2':200,'2':345,'5/2':210,'3':30},'existing quarter-holonomy time on eight equal source copies')
    # Two highest weights fix phases once a common lattice cocycle is chosen.
    highest={}
    for label,q in [('100',(1,0,0,0,0,1,1,1)),('720',(1,1,1,0,0,1,0,0))]:
        ps=blocks[tuple(2*x for x in q)]
        highest[label]={'momentum':q,'input_pairs':len(ps),'source_column_norm_squared':2,'normalized_sum_coefficient':str(1/s.sqrt(len(ps))),'CAR_four_creator_state': [2*k+(0 if v==1 else 1) for k,v in enumerate(q) if v]}
    need(highest['100']['input_pairs']==4 and highest['720']['input_pairs']==2,'explicit highest-weight normalizations')
    return {'verdict':'PARTIAL','conditional_result':'EXPLICIT_CURRENT_PRODUCT_TO_EXISTING_FOUR_MAJORANA_SECTOR',
      'checks':len(checks),'input_pairs':2080,'blocks':len(blocks),'spectrum':dict(spectra),'CAR_coordinate_support':len(car_basis_used),'map_nonzeros':nnz,
      'family_hodge_projector_rank':10,'highest_weights':highest,
      'operator_types':{'100':'V10 tensor Lambda3_plus(V6)','720':'Lambda3(V10) tensor V6'},
      'source_grade':2,'CAR_creator_count':4,'CAR_mode_energy_each':'1/2','two_point':'delta_ab/(z-w)^4 on orthonormal quartic fields',
      'common_time':'L0 maps to CAR L0 under fixed boson-fermion correspondence; image energy 2',
      'total_source_charge_counts':dict(charge_counts),'sector_charge_counts':{k:dict(v) for k,v in sector_charges.items()},
      'quarter_holonomy_energy_counts':dict(energy_counts),
      'full_time_intertwiner':'For every fixed source Cartan combination Q and delta, U(L0+delta Q)=(L0_CAR+delta Q_CAR)U on the common even D8 sector. No Ramond-sector time selection follows.',
      'quarter_holonomy_assumption':'The existing H=L0-Q/4 is lifted to the previously assumed eight identical complex source channels. Their primitive multiplicity and joint origin are not derived.',
      'premise':'Existing marked D8_1 even-CAR realization, same vacuum/stress and one fixed bosonization convention. Not a derivation of 16 Majorana channels from P1.',
      'phase_scope':'Source input cocycles and charge-wise bosonization phases omitted for same-charge Gram/range checks. Analytic VOA correspondence preserves products after one consistent phase dictionary, not a newly replayed archived sign table.',
      'not_derived':['local 3+1D spinor fields in (16,4)','primitive seam selection of the 16-Majorana source','nonzero physical quartic/Yukawa coupling or mass hierarchy','common physical spacetime','T1-T8 closure']}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('certificate.json'))
    args=ap.parse_args();r=main();args.out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2))
