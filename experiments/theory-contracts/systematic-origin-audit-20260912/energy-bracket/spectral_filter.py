"""Exact NON-RH arbitrary five-value source filter and positive rational witnesses."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS = 'experiments/theory-contracts/systematic-origin-audit-20260912/energy-bracket/polynomial_filter.py'
PREVIOUS_PIN = '58ca267c804d224b3f5acd60174145e538abc980fe459ed2079735c3eb381c60'
CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def clean(m):
    return m.applyfunc(s.simplify)


def main():
    for path, pin in ((SOURCE, SOURCE_PIN), (PREVIOUS, PREVIOUS_PIN)):
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    tree = ast.parse((ROOT/SOURCE).read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s':s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    aa = [s.I*g for g in env['generators']()]
    I, I16 = s.eye(4), s.eye(16)
    h = 2*I16-sum((s.kronecker_product(a,s.conjugate(a)) for a in aa),s.zeros(16))/2
    require(h.eigenvals() == {0:1,1:4,2:6,3:4,4:1}, 'actual primitive five-level spectrum')
    projectors = []
    for k in range(5):
        P = I16
        for j in range(5):
            if j != k:
                P = P*(h-j*I16)/(k-j)
        require(P == P.H and P*P == P and h*P == k*P, 'exact source polynomial spectral projector')
        require(s.trace(P) == s.binomial(4,k), 'exact projector multiplicity')
        projectors.append(P)
    require(sum(projectors,s.zeros(16)) == I16, 'full spectral resolution')
    f = s.symbols('f0:5', real=True)
    F = sum((f[k]*projectors[k] for k in range(5)),s.zeros(16))
    p = sum(s.binomial(4,k)*f[k]**2 for k in range(5))/16
    q = sum(k*s.binomial(4,k)*f[k]**2 for k in range(5))/16
    b = (f[0]*f[3]+3*f[1]*f[2]+f[1]*f[4]+3*f[2]*f[3])/8
    A = [s.Matrix(4,4,list(F[row,:]))/2 for row in range(16)]
    def transfer(X):
        return clean(sum((K*X*K.H for K in A),s.zeros(4)))
    require(clean(transfer(I)-p*I) == s.zeros(4), 'full-filter right transfer normalization')
    require(clean(sum((K.H*K for K in A),s.zeros(4))-p*I) == s.zeros(4), 'full-filter left transfer normalization')
    require(s.simplify(s.trace(h*F*F)/16-q) == 0, 'full-filter intracell weighted moment')
    d = [s.expand(sum(f[k]**2*sum((-1)**j*s.binomial(r,j)*s.binomial(4-r,k-j)
        for j in range(r+1)) for k in range(5))/16) for r in range(5)]
    for bits in itertools.product((0,1),repeat=4):
        word = I
        for bit,a in zip(bits,aa):
            if bit:
                word *= a
        if word != word.H:
            word = s.I*word
        require(clean(transfer(word)-d[sum(bits)]*word) == s.zeros(4), 'general five-value sixteen-word transfer spectrum')
    def left_insert(O):
        out = s.zeros(4)
        for j,k,l in itertools.product(range(4),repeat=3):
            out += O[l,j]*A[4*j+k]*A[4*l+k].H
        return clean(out)
    def right_adjoint(O):
        out = s.zeros(4)
        for j,k,l in itertools.product(range(4),repeat=3):
            out += O[l,k]*A[4*j+l].H*A[4*j+k]
        return clean(out)
    cross = []
    for a in aa:
        left, right = left_insert(s.conjugate(a)), right_adjoint(a)
        require(clean(left-b*a) == s.zeros(4), 'general physical left insertion proves five-value boundary formula')
        require(clean(right-b*a) == s.zeros(4), 'general physical right insertion proves five-value boundary formula')
        cross.append(s.simplify(s.trace(left*right)/(4*p*p)))
    between = 2-sum(cross)/2
    energy = 1+q/(2*p)-(b/p)**2
    require(s.simplify(energy-(q/p+between)/2) == 0, 'general energy from both independent bond contractions')
    t,u = s.symbols('t u',real=True)
    quadratic = {f[k]:1-t*k+u*k*k for k in range(5)}
    require(s.expand(b.subs(quadratic)-((1-2*t+5*u)**2-2*(t/2-2*u)**2)) == 0,
            'general boundary formula reduces to previously certified quadratic family')
    baseline = s.Rational(53950,59177)
    records = []
    for integers, expected in (([16,11,9,8,7],s.Rational(2134375,2343961)),
                               ([52,36,30,27,23],s.Rational(254850665,279993289))):
        subs = {f[k]:s.Rational(integers[k],integers[0]) for k in range(5)}
        filter_matrix = F.subs(subs)
        require(filter_matrix.rank() == 16 and all(subs[x] > 0 for x in f), 'positive full-rank filter, full Kraus span and strict primitivity')
        require(filter_matrix.eigenvals() == {subs[f[k]]:s.binomial(4,k) for k in range(5)}, 'chosen actual source filter spectrum')
        rates = [s.factor((dr/p).subs(subs)) for dr in d]
        require(rates[0] == 1 and all(abs(z)<1 for z in rates[1:]), 'chosen complete normalized transfer is strictly primitive')
        value = s.factor(energy.subs(subs))
        require(value == expected < baseline, 'exact rational improvement over quadratic upper bound')
        within_value = s.factor((q/p).subs(subs))
        between_value = s.factor(between.subs(subs))
        require((within_value+between_value)/2 == value, 'both chosen source bond costs sum to reported density')
        records.append({'integer_filter_weights':integers,'energy_upper_bound':str(value),
            'inside_bond_energy':str(within_value),'between_bond_energy':str(between_value),
            'perron':str(s.factor(p.subs(subs))),'normalized_transfer_by_grade':[str(z) for z in rates],
            'improvement_over_quadratic':str(baseline-value)})
    require(s.Rational(records[1]['energy_upper_bound']) < s.Rational(records[0]['energy_upper_bound']), 'sharper integer witness improves simpler witness')
    require(s.simplify(b-f[0]*f[3]/8) != 0, 'negative control rejects incomplete cross-spectral boundary numerator')
    print(json.dumps({'checks':CHECKS,'source_pin':SOURCE_PIN,'previous_pin':PREVIOUS_PIN,
        'general_boundary_numerator':str(b),'energy_formula':'1+q/(2p)-(b/p)^2',
        'bond_dimension':4,'quadratic_baseline':str(baseline),'certified_witnesses':records,
        'thermodynamic_fixed_point_only':True,'global_variational_optimality_proved':False,
        'exact_ground_state_claim':False,'uniform_gap_proved':False,
        'physical_parent_selected':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
