"""Exact conditional POVM counterexample: covariance is not effect invariance.

Source geometry is checked here; CAR positivity follows from the documented
Clifford identities, independently checked in even_carrier_bridge.py.
No TFPT apparatus, state preparation, or gauge contract is inferred.
"""
import json
import sympy as S
import boundary_access as source


def main():
    J, B, O, P = source.source_matrices()
    b = S.eye(16)[:, 10]
    v = (S.eye(16)-P)*(S.eye(16)[:, 0]+S.eye(16)[:, 6])
    norm = (v.T*v)[0]
    orbit = [O**k*v for k in range(6)]
    source.require(O**6 == S.eye(16) and O*b == b, 'sixfold action fixes boundary vector')
    source.require(all((w.T*w)[0] == norm and (b.T*w)[0] == 0 for w in orbit),
                   'each normalized Clifford bilinear is an involution')
    source.require(sum(orbit, S.zeros(16, 1)) == S.zeros(16, 1), 'orbit average zero')
    source.require(S.Matrix.hstack(*orbit).rank() == 3, 'three independent readout directions')
    source.require(all(O*orbit[k] == orbit[(k+1)%6] for k in range(6)), 'outcome covariance')
    source.require(all(P*(b*w.T-w*b.T)*(S.eye(16)-P) != S.zeros(16) for w in orbit),
                   'each readout crosses original access split')
    # F_k=i gamma(b)gamma(O^k v)/sqrt(norm); F_k^2=I and tr(F_k)=0.
    # Thus E_{k,s}=(I+s F_k)/12 has spectrum {0,1/6}.
    # rho_r=(I+r F_0)/256 is positive; trace(F_0 F_k)/256 = normalized Gram.
    gram = [(v.T*w)[0]/norm for w in orbit]
    probabilities = {}
    for r in (-1, 1):
        probs = [(1+r*s*g)/12 for g in gram for s in (-1, 1)]
        source.require(all(p >= 0 for p in probs) and sum(probs) == 1,
                       'positive normalized witness statistics')
        source.require(all(sum((1+r*s*g)/12 for g in gram) == S.Rational(1,2)
                           for s in (-1, 1)), 'forgetting orientation loses witness information')
        probabilities[str(r)] = [str(p) for p in probs]
    source.require((1+gram[0])/12 == S.Rational(1,6) and (1-gram[0])/12 == 0,
                   'retained orientation distinguishes witnesses statistically')
    print(json.dumps({'checks': source.count, 'orbit_rank': 3,
        'normalized_orbit_gram': list(map(str, gram)), 'witness_probabilities': probabilities,
        'outcome_order': 'k=0..5, sign=-1,+1', 'POVM_effects': 12,
        'source_apparatus_derived': False, 'witness_preparation_derived': False,
        'clock_is_gauge_proved': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
