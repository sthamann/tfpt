"""Exact fixed-algebra audit: signal transport is not unique state selection."""
import json
import sympy as S
import boundary_access as source


def main():
    J,B,O16,P = source.source_matrices()
    I=S.eye(8)
    O=O16[::2,::2]
    E=S.zeros(16)
    for i in (0,1):
        for j in (6,7):
            E[i,j],E[j,i]=B[i,j],B[j,i]
    K=E[::2,1::2]+S.I*E[::2,::2]
    Ks=[O**k*K*(O.T)**k for k in range(6)]
    Us=[I-A*A-S.I*A for A in Ks]
    h=I+(B[::2,1::2]+S.I*B[::2,::2])/8
    def commutant_dim(gs):
        equations=S.Matrix.vstack(*[S.kronecker_product(I,g)-S.kronecker_product(g.T,I) for g in gs])
        return 64-equations.rank()
    source.require(commutant_dim(Ks)==10,'edge-only fixed algebra dimension ten')
    source.require(commutant_dim(Ks+[h])==5,'edge and source fixed algebra dimension five')
    source.require(commutant_dim(Us+[h])==5,'finite pulse has same joint fixed algebra')
    R=S.zeros(8)
    for i in range(5,8):
        for j in range(5,8):
            R[i,j]=S.Integer(i==j)-S.Rational(1,3)
    source.require(R*R==R and R.T==R and R.rank()==2,'unchanged two-dimensional dark boundary plane')
    source.require(h*R==R and all(A*R==S.zeros(8) for A in Ks), 'dark plane is common invariant')
    def channel(rho):
        return sum((U*rho*U.adjoint() for U in Us),S.zeros(8))/6
    rho_a,rho_b=R/2,(I-R)/6
    source.require(S.trace(rho_a)==S.trace(rho_b)==1 and rho_a*rho_b==S.zeros(8),
                   'orthogonal normalized positive projector states')
    source.require(all(channel(rho)==rho and h*rho==rho*h for rho in (rho_a,rho_b)),
                   'two distinct stationary states for any positive Poisson rate')
    Phi=sum((S.kronecker_product(S.conjugate(U),U) for U in Us),S.zeros(64))/6
    source.require(Phi != Phi.adjoint(), 'channel is not the selfadjoint positive transfer of log theorem')
    print(json.dumps({'checks':source.count, 'edge_fixed_algebra_dimension':10,
        'joint_fixed_algebra_dimension':5,'joint_fixed_algebra':'C direct_sum M2(C)',
        'stationary_state_unique':False,'selfadjoint_HS_transfer':False,
        'new_channel_source_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
