"""Exact first/second-moment audit of the stipulated source-edge ensemble."""
import json
import sympy as S
import boundary_access as source


def main():
    _, b, o16, p16 = source.source_matrices()
    eye=S.eye(8)
    o,p=o16[::2,::2],p16[::2,::2]
    q=eye-p
    edge=S.zeros(16)
    for i in (0,1):
        for j in (6,7):
            edge[i,j],edge[j,i]=b[i,j],b[j,i]
    k=edge[::2,1::2]+S.I*edge[::2,::2]
    ks=[o**j*k*(o.T)**j for j in range(6)]
    mean=sum(ks,S.zeros(8))/6
    ds=[a-mean for a in ks]
    variance=sum((a*a for a in ds),S.zeros(8))/6
    source.require(all(a==a.adjoint() and a**3==a for a in ks), 'Hermitian generators with norm at most one')
    source.require(sum(ds,S.zeros(8))==S.zeros(8), 'centered fluctuations sum to zero')
    source.require(variance==sum((a*a for a in ks),S.zeros(8))/6-mean*mean, 'exact noncommutative variance identity')
    source.require(variance.eigenvals()=={S.Rational(1,6):1,S.Rational(1,3):3,S.Rational(1,2):1,S.Integer(0):3}, 'variance spectrum')
    source.require(mean*p==p*mean, 'mean Hamiltonian preserves accessible block')
    def ad(a):
        return S.kronecker_product(eye,a)-S.kronecker_product(a.T,eye)
    # Column-vectorized matrix action: 64x64 equality tests every input operator.
    discrepancy=-sum((ad(a)**2 for a in ks),S.zeros(64))/12+ad(mean)**2/2
    noise=-sum((ad(a)**2 for a in ds),S.zeros(64))/12
    source.require(discrepancy==noise and noise!=S.zeros(64), 'full second-order channel discrepancy')
    source.require(noise==noise.adjoint(), 'Hermitian Hilbert-Schmidt noise coefficient')
    rho=q/3
    def second(a,r):
        return a*r*a-(a*a*r+r*a*a)/2
    moment=sum((second(a,rho) for a in ks),S.zeros(8))/6
    mean_moment=second(mean,rho)
    source.require(mean*rho==rho*mean and mean_moment==S.zeros(8), 'mean leaves hidden mixed witness stationary')
    source.require(S.trace(p*moment)==S.Rational(1,6), 'edge ensemble leakage coefficient')
    source.require(S.trace(moment)==0, 'second-order trace preservation')
    source.require(S.trace(p*sum((a*rho*a for a in ds),S.zeros(8))/6)==S.Rational(1,6), 'same leakage from fluctuation cross blocks')
    h=eye+(b[::2,1::2]+S.I*b[::2,::2])/8
    rb=S.diag(0,0,0,0,0,1,1,1)
    source.require(rb*moment==S.zeros(8), 'pulse second-order term has no literal boundary support')
    source.require(S.simplify(S.trace(rb*h*moment*h))==S.Rational(7,384), 'literal boundary mixed theta-squared tau-squared coefficient')
    theta=S.symbols('theta', real=True)
    known=(35-34*S.cos(theta)-S.cos(theta)**2)/108
    source.require(S.diff(known,theta,2).subs(theta,0)/2==S.Rational(1,6), 'independent comparison with previous all-angle formula')
    print(json.dumps({'checks':source.count,'source_sha256':source.PIN,
        'first_moments_equal':True,'second_order_channels_equal':False,
        'variance_spectrum':['0 (x3)','1/6','1/3 (x3)','1/2'],
        'hidden_leakage_theta_squared':'1/6',
        'literal_boundary_theta_squared_tau_squared':'7/384',
        'source_event_law_derived':False,'blind_holdout':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
