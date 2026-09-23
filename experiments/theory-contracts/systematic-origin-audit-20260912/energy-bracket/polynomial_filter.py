"""Exact NON-RH improved D=4 variational upper bound using a quadratic filter."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS = 'experiments/theory-contracts/systematic-origin-audit-20260912/uniform-chain/dimer_filter.py'
PREVIOUS_PIN = '53792526398ae08559169493b48a833a05623aa8efc6b3d7747b7a6c7f10aa80'
CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def main():
    for path, pin in ((SOURCE, SOURCE_PIN), (PREVIOUS, PREVIOUS_PIN)):
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    tree = ast.parse((ROOT/SOURCE).read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    a = [s.I*g for g in env['generators']()]
    I, I16 = s.eye(4), s.eye(16)
    ss = [s.kronecker_product(g, s.conjugate(g)) for g in a]
    h = 2*I16-sum(ss, s.zeros(16))/2
    require(h == h.T == s.conjugate(h), 'actual real alternating source pair')
    require(h.eigenvals() == {0:1, 1:4, 2:6, 3:4, 4:1}, 'binomial source multiplicities')
    t, u = s.symbols('t u', real=True)
    F = I16-t*h+u*h*h
    c0, c1, c2 = 1-2*t+5*u, t/2-2*u, u/2
    cross = sum((ss[j]*ss[k] for j, k in itertools.combinations(range(4), 2)), s.zeros(16))
    require(clean(F-c0*I16-c1*sum(ss, s.zeros(16))-c2*cross) == s.zeros(16), 'source polynomial resolves into primitive and bivector synchronizers')
    f = [1-t*k+u*k*k for k in range(5)]
    p = s.expand(sum(s.binomial(4,k)*f[k]**2 for k in range(5))/16)
    w = s.expand(sum(s.binomial(4,k)*k*f[k]**2 for k in range(5))/16)
    b = s.expand(c0*c0-2*c1*c1)
    require(s.expand(p-c0*c0-4*c1*c1-6*c2*c2) == 0, 'normalization from orthogonal source word expansion')
    require(s.expand(s.trace(F*F)/16-p) == 0, 'independent physical filter norm')
    require(s.expand(s.trace(h*F*F)/16-w) == 0, 'independent physical weighted energy moment')
    A = [s.Matrix(4,4,list(F[row,:]))/2 for row in range(16)]
    def transfer(X):
        return clean(sum((K*X*K.H for K in A), s.zeros(4)))
    require(transfer(I) == p*I, 'right normalization with quadratic filter')
    require(clean(sum((K.H*K for K in A), s.zeros(4))-p*I) == s.zeros(4), 'left normalization with quadratic filter')
    # Exact Fourier coefficients of F^2 on four commuting source syndromes.
    d = [s.expand(sum(f[k]**2*sum((-1)**j*s.binomial(r,j)*s.binomial(4-r,k-j)
        for j in range(r+1)) for k in range(5))/16) for r in range(5)]
    for bits in itertools.product((0,1), repeat=4):
        word = I
        for bit, gamma in zip(bits, a):
            if bit:
                word *= gamma
        if word != word.H:
            word = s.I*word
        require(clean(transfer(word)-d[sum(bits)]*word) == s.zeros(4), 'complete sixteen-word quadratic transfer diagonalization')
    def left_insert(O):
        R = s.zeros(4)
        for j,k,l in itertools.product(range(4), repeat=3):
            R += O[l,j]*A[4*j+k]*A[4*l+k].H
        return clean(R)
    def right_insert_adjoint(O):
        R = s.zeros(4)
        for j,k,l in itertools.product(range(4), repeat=3):
            R += O[l,k]*A[4*j+l].H*A[4*j+k]
        return clean(R)
    expectations = []
    for gamma in a:
        left, right = left_insert(s.conjugate(gamma)), right_insert_adjoint(gamma)
        require(clean(left-b*gamma) == s.zeros(4), 'quadratic filter left physical insertion')
        require(clean(right-b*gamma) == s.zeros(4), 'quadratic filter right physical insertion')
        expectations.append(s.simplify(s.trace(right*left)/(4*p*p)))
    between = s.simplify(2-sum(expectations)/2)
    require(s.simplify(between-(2-2*b*b/p**2)) == 0, 'intercell bond correlation cost retained exactly')
    energy = s.factor(w/(2*p)+between/2)
    require(s.simplify(energy-(w/(2*p)+1-b*b/p**2)) == 0, 'general exact quadratic-filter variational energy')
    previous = (191*t**4-260*t**3+140*t*t-36*t+4)/(4*(5*t*t-4*t+1)**2)
    require(s.simplify(energy.subs(u,0)-previous) == 0, 'entire earlier linear-filter family reproduced')
    chosen = {t:s.Rational(8,33), u:s.Rational(1,33)}
    Fc = F.subs(chosen)
    require(Fc == ((h-4*I16)**2+17*I16)/33, 'simple positive completed-square rational filter')
    require(Fc.eigenvals() == {1:1, s.Rational(26,33):4, s.Rational(7,11):6, s.Rational(6,11):4, s.Rational(17,33):1},
            'all chosen filter eigenvalues strictly positive')
    require(Fc.rank() == 16, 'sixteen Kraus matrices span full M4, strict transfer positivity')
    require(p.subs(chosen) == s.Rational(1003,2178), 'chosen exact Perron normalization')
    rates = [s.factor((x/p).subs(chosen)) for x in d]
    require(rates == [1,s.Rational(188,1003),s.Rational(62,1003),s.Rational(12,1003),s.Rational(3,1003)],
            'chosen primitive finite-correlation transfer spectrum')
    require(all(abs(x) < 1 for x in rates[1:]), 'strict spectral dominance, exact thermodynamic contraction justified')
    require(s.factor((b/p).subs(chosen)) == s.Rational(56,59), 'chosen boundary transmission')
    inside_value = s.factor((w/p).subs(chosen))
    between_value = s.factor(between.subs(chosen))
    value = s.factor(energy.subs(chosen))
    require(inside_value == s.Rational(1630,1003) and between_value == s.Rational(690,3481), 'both exact bond energies')
    require(value == s.Rational(53950,59177), 'certified exact improved energy upper bound')
    old_bound = s.Rational(5023,5476)
    improvement = old_bound-value
    require(improvement == s.Rational(1815871,324053252) > 0, 'strict rational improvement over previous certified state')
    require(s.simplify(energy-w/(2*p)) != 0, 'negative control rejects omission of neighboring bond cost')
    print(json.dumps({'checks':CHECKS, 'source_pin':SOURCE_PIN, 'previous_pin':PREVIOUS_PIN,
        'filter':'I-t h+u h^2', 'chosen_filter':'((h-4I)^2+17I)/33',
        'chosen_parameters':{'t':'8/33','u':'1/33'}, 'general_normalization':str(p),
        'general_boundary_numerator':str(b), 'general_weighted_energy':str(w),
        'energy_formula':'w/(2p)+1-b^2/p^2', 'bond_dimension':4,
        'chosen_perron':'1003/2178', 'chosen_normalized_transfer_by_grade':[str(x) for x in rates],
        'chosen_inside_energy':str(inside_value), 'chosen_between_energy':str(between_value),
        'energy_density_upper_bound':str(value), 'previous_bound':str(old_bound), 'improvement':str(improvement),
        'energy_is_thermodynamic_limit':True, 'global_variational_optimality_proved':False,
        'exact_ground_state_claim':False, 'uniform_gap_proved':False,
        'physical_parent_selected':False, 'T1_T8_closed':[]}, sort_keys=True))


if __name__ == '__main__':
    main()
