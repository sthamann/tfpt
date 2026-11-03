"""Exact signs in the existing full96 chart; FUNCTOR.txt proves operator scope."""
from pathlib import Path
import hashlib
import json
import sympy as s
import numpy as np

repo = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
source = repo / 'experiments/theory-contracts/tfpt-unified-source-derivation-20261029/graded_boundary_functor/check_finite_typing.py'
native = {'__file__': str(source)}
# Reuse the existing constructor prelude, without its canonical result writer.
exec(compile(source.read_text().split('checks={')[0], str(source), 'exec'), native)
v, exact, g, E, N, Z, S, n = [native[k] for k in
                             ['v', 'exact', 'g', 'E', 'N', 'Z', 'S', 'n']]
I = s.eye(n)
I2 = s.eye(2*n)
zero = s.zeros(n)
NN = s.kronecker_product(N, I)
SS = s.kronecker_product(S, I)
GG = s.kronecker_product(Z, g)
U = E.row_join(NN * E)
K = exact(v.Kswap())
Jold = SS * s.diag(K, K)
c = -s.I * K
q, dr, p, m, ell, mu = s.symbols('q dr p m ell mu', real=True)
ys = [np.diag(x).astype(complex) for x in
      ([1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6])]
mr = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]], complex)
DY = exact(v.full_D(*ys, np.zeros((3, 3), complex)))
DM = exact(v.full_D(*[np.zeros((3, 3), complex)] * 4, mr))
Phi = (p+m)*DY+DM
Phitau = (p-m)*DY+DM


def eq(a, b):
    # Matrix structural equality does not expand products over p+m.
    return a.shape == b.shape and all(s.expand(z) == 0 for z in a-b)


def Dop(ph, drsign=1):
    return (drsign*s.kronecker_product(N, dr*I)
            + s.kronecker_product(S, q*I)+s.kronecker_product(Z, ph))


def hd(ph):
    return q*g-s.I*g*ph


def Db(ph):
    h = hd(ph)
    return zero.row_join(-dr*I+h).col_join((dr*I+h).row_join(zero))


checks = {
    'actual_full96': n == 96,
    'full_U_unitary': eq(U.H*U, I2) and eq(U*U.H, I2),
    'transported_grading': eq(U.H*GG*U, s.diag(I, -I)),
    'normal_matrix_transport': eq(U.H*NN*U, zero.row_join(-I).col_join(I.row_join(zero))),
    'tauS_transport': eq(U.H*SS*U, zero.row_join(g).col_join(g.row_join(zero))),
    'tauT_transport': eq(U.H*SS*s.diag(g, g)*U, zero.row_join(I).col_join(I.row_join(zero))),
    'native_Jloc_transport': eq(U.H*Jold*s.conjugate(U), s.diag(c, -c)),
    'native_JF_anti_grading': eq(K*s.conjugate(g), -g*K),
    'native_JF_Phi': eq(K*s.conjugate(Phi), Phi*K),
    'whole_D_transport': eq(U.H*Dop(Phi)*U, Db(Phi)),
}
for label, phref in {'S': m*DY, 'T': p*DY+DM}.items():
    tau = SS if label == 'S' else SS*s.diag(g, g)
    ave = (Dop(Phi)+tau*Dop(Phitau, -1)*tau)/2
    ug = (I-s.I*g)/s.sqrt(2)
    R = -2*ell*mu*s.I*g*phref
    checks[f'actual_tau_{label}_reference'] = eq(ave, Dop(phref))
    checks[f'reference_{label}_whole_transport'] = eq(U.H*ave*U, Db(phref))
    checks[f'reference_{label}_complete_reader'] = eq(
        2*ell*mu*(hd(phref)-g*hd(phref)*g)/2, R)
    checks[f'reference_{label}_reader_comparison'] = eq(R, 2*ell*mu*ug*phref*ug.H)
    # Clear only the declared nonzero scalar denominator.
    checks[f'reference_{label}_inverse'] = eq(ug.H*R*ug, 2*ell*mu*phref)

result = {
    'all_passed': all(checks.values()), 'checks': checks,
    'n_checks': len(checks), 'source': str(source),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'constructor_sha256': hashlib.sha256(
        (repo/'verification/v252_full_finite_triple.py').read_bytes()).hexdigest(),
    'scope': 'Exact symbolic coefficients of actual full96 constructor, both R032 lifts and actual JF. Operator-domain, normal propagation and functional calculus are proved analytically in FUNCTOR.txt.',
}
Path(__file__).with_name('FUNCTOR-check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
if not result['all_passed']:
    raise SystemExit(1)
