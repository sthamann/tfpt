"""Conditional even readouts; exact source geometry and full finite Fock checks."""
import json
import sympy as S
import boundary_access as source


def main():
    J,B,O,P = source.source_matrices()
    Q=S.eye(16)-P
    D=J+B/8
    b=S.eye(16)[:,10]
    v=Q*(S.eye(16)[:,0]+S.eye(16)[:,6])
    norm=(v.T*v)[0]
    source.require(norm==S.Rational(7,6) and (b.T*v)[0]==0, 'orthogonal bridge vectors')
    hidden=S.Matrix.hstack(*(D**k*v for k in range(6)))
    source.require(hidden.rank()==6 and Q*hidden==hidden, 'hidden cyclic rank six')
    M=b*v.T-v*b.T
    source.require(P*M*Q != S.zeros(16), 'even bridge crosses access split')
    source.require(J*M-M*J != S.zeros(16), 'single Majorana bridge not number conserving')
    source.require(sum((O**k*M*(O.T)**k for k in range(6)),S.zeros(16))==S.zeros(16),
                   'clock average of hidden bridge vanishes')
    # Full 256-state CAR representation, bit j records mode j occupation.
    size=256
    annih=[]
    for j in range(8):
        entries={}
        for word in range(size):
            if word & (1<<j):
                entries[word^(1<<j),word]=(-1)**((word & ((1<<j)-1)).bit_count())
        annih.append(S.MutableSparseMatrix(size,size,entries))
    gamma=[]
    for c in annih:
        gamma.extend([c+c.T,-S.I*(c-c.T)])
    gv=sum((v[j]*gamma[j] for j in range(16)),S.zeros(size,size))
    F=S.I*gamma[10]*gv
    parity=S.diag(*[(-1)**n.bit_count() for n in range(size)])
    N=S.diag(*[n.bit_count() for n in range(size)])
    vac=S.eye(size)[:,0]
    source.require(F==F.adjoint() and F*parity==parity*F,'Hermitian parity-even bridge')
    source.require(F*F==norm*S.eye(size),'exact bridge square')
    source.require(N*(F*vac)==2*(F*vac) and (F*vac).norm()**2==norm,
                   'nonzero pure two-particle vacuum output')
    # Even AND number-neutral counterpart, using same real spatial coefficients.
    cv=sum((v[2*j]*annih[j] for j in range(8)),S.zeros(size,size))
    cb=annih[5]
    G=cb.T*cv+cv.T*cb
    source.require(G==G.adjoint() and G*parity==parity*G and G*N==N*G,
                   'neutral hopping bridge')
    source.require(G*vac==S.zeros(size,1),'neutral bridge cannot excite empty vacuum')
    P8=P[::2,::2]
    h=S.eye(8)+(B[::2,1::2]+S.I*B[::2,::2])/8
    v8=S.Matrix([v[2*j] for j in range(8)])
    source.require(S.Matrix.hstack(v8,h*v8,h*h*v8).rank()==3 and P8*v8==S.zeros(8,1),
                   'neutral one-body hidden cyclic rank three')
    print(json.dumps({'checks':source.count,'hidden_real_cyclic_rank':6,
        'conditional_quadratic_algebra_dimension':120,'F_squared':'7/6 I',
        'F_vacuum_particle_number':2,'G_vacuum_zero':True,
        'bridge_TFPT_access_derived':False,'pulse_implementation_derived':False,
        'arbitrary_many_body_control_proved':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
