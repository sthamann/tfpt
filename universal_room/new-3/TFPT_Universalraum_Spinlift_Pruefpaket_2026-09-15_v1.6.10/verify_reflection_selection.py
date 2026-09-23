"""Clock alone versus an explicit vertex/edge reflection, exact bounded audit."""
import json
import sympy as s

checks=[]


def need(condition,name):
    if not bool(condition):raise RuntimeError(name)
    checks.append(name)


def run():
    a,b=s.symbols('a b',real=True)
    results={}
    for eta in (1,-1):
        R=s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[eta,0,0,0]])
        J=s.Matrix([[1,0,0,0],[0,0,0,eta],[0,0,eta,0],[0,eta,0,0]])
        L=R*J
        U=a*s.eye(4)+b*R
        need(U*R==R*U,'arbitrary two weights preserve clock '+str(eta))
        need(J*J==s.eye(4) and J*R*J==R.inv(),'signed reflection dihedral relation '+str(eta))
        need(L*L==s.eye(4),'edge reflection involution '+str(eta))
        need(U*J==L*(b*s.eye(4)+a*R),'reflection exchanges weights '+str(eta))
        mismatches=[]
        for row in range(4):
            v=(U*J)[row,:];w=(L*U)[row,:]
            diff=s.simplify(v.T*v-w.T*w)
            need(diff.subs(b,a)==s.zeros(4) and diff.subs(b,-a)==s.zeros(4),
                 'equal magnitude weights preserve pair reflection row '+str((eta,row)))
            for entry in diff:
                if entry!=0:
                    quotient=s.cancel(entry/(a*a-b*b))
                    need(quotient in (1,-1),'pair mismatch exactly a squared minus b squared '+str((eta,row)))
                    mismatches.append(quotient)
        need(len(mismatches)>0,'pair reflection forces equal magnitudes '+str(eta))
        # The relative placement matters: same vertex reflection on pair banks
        # is NOT the shifted edge reflection and forces b=0 in this ansatz.
        v=(U*J)[0,:];w=(J*U)[0,:]
        same_vertex=s.simplify(v.T*v-w.T*w)
        need(same_vertex[3,3]==b*b,'same vertex reflection detects nonzero neighbor weight '+str(eta))
        need(same_vertex.subs(b,0)==s.zeros(4),'same vertex reflection permits onsite-only source '+str(eta))
        # Explicit positive full-rank frame with untwisted clock.
        unequal=U.subs({a:s.Rational(3,5),b:s.Rational(4,5)})
        S=unequal*unequal.T
        need(all(S[i,i]==1 for i in range(4)),'unequal frame individually CAR normalized '+str(eta))
        need(S.det()>0,'unequal frame no linear spectator '+str(eta))
        balanced=U.subs({a:s.sqrt(2)/2,b:s.sqrt(2)/2})
        need(balanced.rank()==(3 if eta==1 else 4),'balanced frame twist discriminates rank '+str(eta))
        results[str(eta)]={'unequal_frame_spectrum':{str(k):v for k,v in S.eigenvals().items()},
                           'balanced_rank':balanced.rank()}
    delta=s.Rational(15,2)*s.Rational(1,25)
    M=1920;t=s.Rational(1,10000)
    margin=delta-M*M*t*t
    need(margin==s.Rational(8223,31250)>0,'untwisted asymmetric candidate also has unique full ground at weak g')
    return {'status':'PASS','exact_checks':len(checks),'checks':checks,'frames':results,
            'untwisted_asymmetric_ground_gap_coefficient_lower_bound':str(margin),
            'conditional_selection':'real two-site frames + specified vertex/edge reflection + no linear dark modes select antiperiodic balanced frame up to source signs',
            'not_derived':['physical availability of reflected pair operation','raw-seam to vertex/edge action','nearest-neighbor frame ansatz','physical g/Delta']}


if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
