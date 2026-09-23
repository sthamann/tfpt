"""A conditional covariant mixed-unitary channel from existing source edges.

Exact one-particle sector; no claim that source implements the channel.
"""
import json
import sympy as S
import boundary_access as source


def main():
    J, B, O16, P16 = source.source_matrices()
    O, P = O16[::2,::2], P16[::2,::2]
    I = S.eye(8)
    Q = I-P
    E = S.zeros(16)
    for i in (0,1):
        for j in (6,7):
            E[i,j],E[j,i] = B[i,j],B[j,i]
    K = E[::2,1::2]+S.I*E[::2,::2]
    source.require(K == K.adjoint() and K**3 == K, 'existing neutral edge spectrum 0,+1,-1')
    c,s = S.symbols('c s',real=True)
    def reduce(z):
        return S.rem(S.Poly(S.expand(z),s), S.Poly(s*s+c*c-1,s)).as_expr().expand()
    def reduced(M):
        return M.applyfunc(reduce)
    U = I+(c-1)*K*K-S.I*s*K
    source.require(reduced(U*U.adjoint()-I) == S.zeros(8), 'unitarity for c^2+s^2=1')
    orbit = [O**k*U*(O.T)**k for k in range(6)]
    source.require(all(O*orbit[k]*O.T == orbit[(k+1)%6] for k in range(6)),
                   'unitary orbit covariance')
    def channel(rho):
        return reduced(sum((V*rho*V.adjoint() for V in orbit), S.zeros(8))/6)
    source.require(reduced(sum((V.adjoint()*V for V in orbit),S.zeros(8))/6-I)==S.zeros(8),
                   'Kraus completeness')
    avgK = sum((O**k*K*(O.T)**k for k in range(6)),S.zeros(8))/6
    source.require(P*avgK*Q == S.zeros(8), 'averaged Hamiltonian cannot transfer')
    p = S.Matrix([1,1,1,0,0,0,0,0])/S.sqrt(3)
    rho = p*p.T
    out = channel(rho)
    source.require(P*rho == rho and O*out*O.T == out, 'invariant input and output')
    leakage = reduce(S.trace(Q*out))
    source.require(S.expand(leakage-(c*c-8*c+7)/18)==0,
                   'accessible to hidden population formula')
    hidden_out = channel(Q/3)
    signal = reduce(S.trace(P*hidden_out))
    source.require(O*hidden_out*O.T == hidden_out and S.trace(hidden_out)==1,
                   'hidden witness remains normalized and invariant')
    source.require(signal.subs(c,0)>0 and signal.subs(c,1)==0,
                   'hidden occupation produces accessible population after pulse')
    source.require(S.trace(P*Q/3)==0, 'hidden witness initially invisible in accessible modes')
    # Direct original-boundary readout after the stipulated pulse and free flow.
    h = I+(B[::2,1::2]+S.I*B[::2,::2])/8
    RB = S.diag(0,0,0,0,0,1,1,1)
    pulse_out = hidden_out.subs({c:0,s:1})
    source.require(RB*pulse_out == S.zeros(8), 'pulse alone leaves literal boundary empty')
    coefficient = S.simplify(S.trace(RB*h*pulse_out*h))
    source.require(coefficient > 0, 'positive leading literal-boundary response')
    source.require(RB*h*Q == S.zeros(8), 'without pulse hidden state stays boundary dark')
    print(json.dumps({'checks': source.count, 'accessible_to_hidden_probability':str(leakage),
        'hidden_to_accessible_probability':str(signal), 'at_angle_pi_over_2':str(signal.subs(c,0)),
        'c': 'cos(theta)', 'clock_orientation_record_required':False,
        'literal_boundary_probability_leading_tau_squared':str(coefficient),
        'channel_implementation_derived':False, 'occupied_preparation_derived':False,
        'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
