"""Exact local ingredients of the boundary-access irreducibility proof.

General chain-length induction is in README.md. This checker does not form
the exponentially large full operator algebra or claim efficient control.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'


def require(ok,message):
    if not ok:
        raise ValueError(message)


def main():
    raw=SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PIN,'unchanged original compiler')
    tree=ast.parse(raw)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generators')
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for name,pin in pins.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==pin,'inherited '+name)
    env={'s':s}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),env)
    generators=env['generators']()
    words=[]
    for bits in itertools.product((0,1),repeat=4):
        word=s.eye(4)
        for bit,g in zip(bits,generators):
            if bit:
                word=word*g
        words.append(word.reshape(16,1))
    require(s.Matrix.hstack(*words).rank()==16,'actual boundary generators span full M4')
    cases=[]
    for d in (2,3,4):
        phi=s.Matrix([1 if i//d==i%d else 0 for i in range(d*d)])
        p=phi*phi.T/d
        units={}
        for a,b in itertools.product(range(d),repeat=2):
            e=s.zeros(d); e[a,b]=1
            units[a,b]=e
            require(p[a*d:(a+1)*d,b*d:(b+1)*d]==e/d,
                    'Bell first-site coefficient is exactly next-site Eab/d')
        off=[e for (a,b),e in units.items() if a!=b]
        generated=off+[units[a,(a+1)%d]*units[(a+1)%d,a] for a in range(d)]
        require(s.Matrix.hstack(*[e.reshape(d*d,1) for e in generated]).rank()==d*d,
                'off-diagonal coefficients generate full next-site matrix algebra')
        require(all(e==s.zeros(d) for e in
            [s.eye(d)*units[a,b]-units[a,b]*s.eye(d) for a,b in units]),
            'scalar commutant positive control')
        test=s.diag(*range(d))
        require(test*units[0,1]!=units[0,1]*test,'non-scalar spectator rejected')
        cases.append({'d':d,'coefficient_and_generation_checks':True})
    print(json.dumps({'scope':'NON-RH exact local verification plus analytic finite-chain induction',
        'source_pin':PIN,'cases':cases,'boundary_source_algebra_dimension':16,
        'chain_length_five_d4_common_invariant_space_dimension':1024,
        'assumptions':['open Bell chain','all edge weights nonzero','full first-site compiler algebra'],
        'proper_nonzero_common_invariant_subspace_exists':False,
        'efficient_or_native_controllability_proved':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
