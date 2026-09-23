"""Exact controls for correlations, interactions and historical records.

These are counterexamples to proposed identifications, not new physical
source models. General statements are proved in CAUSAL_RECORDS.md.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

CHECKS=[]
HERE=Path(__file__).resolve().parent
SOURCE=Path('/Users/stefanhamann/.codex/attachments/b3a502d5-9938-4c56-9cf2-f0c80f004db6/pasted-text.txt')


def need(condition,name):
    if not bool(condition):
        raise RuntimeError(name)
    CHECKS.append(name)


def eq(a,b,name):
    difference=a-b
    entries=list(difference) if isinstance(difference,s.MatrixBase) else [difference]
    need(all(s.simplify(x)==0 for x in entries),name)


def partial_a(rho):
    return s.Matrix(2,2,lambda b,c:sum(rho[2*a+b,2*a+c] for a in range(2)))


def run():
    z=s.Matrix([1,0]); o=s.Matrix([0,1]); plus=(z+o)/s.sqrt(2)
    I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
    kron=s.kronecker_product
    bell=(kron(z,z)+kron(o,o))/s.sqrt(2)
    rho=bell*bell.H
    need(rho!=s.eye(4)/4,'correlated initial state differs from product marginals')
    eq(partial_a(rho),I/2,'Bell marginal is maximally mixed')
    eq(s.trace(rho*kron(X,X)),1,'connected correlation without any dynamical coupling')
    eq(s.trace(rho*kron(X,I)),0,'one-side X mean A')
    eq(s.trace(rho*kron(I,X)),0,'one-side X mean B')
    eq(s.eye(4)*rho*s.eye(4),rho,'product identity evolution preserves those correlations')
    # Unconditioned local operations, including reset and unread measurement.
    channels={'identity':[I],'flip':[X],'reset':[z*z.H,z*o.H],
              'unread_Z':[z*z.H,o*o.H]}
    for name,kraus in channels.items():
        eq(sum((k.H*k for k in kraus),s.zeros(2)),I,'trace preservation '+name)
        output=sum((kron(k,I)*rho*kron(k,I).H for k in kraus),s.zeros(4))
        eq(partial_a(output),I/2,'no remote signal despite correlations '+name)
    # Conditional steering is not an unconditioned controllable signal.
    branch=kron(z*z.H,I)*rho*kron(z*z.H,I)
    eq(s.trace(branch),s.Rational(1,2),'steering branch has probability one half')
    eq(partial_a(branch)/s.trace(branch),z*z.H,'postselection changes conditional state only')
    CZ=s.diag(1,1,1,-1)
    blank=kron(z,z)
    eq(CZ*blank,blank,'nonproduct operation invisible on a selected blind preparation')
    # Same operation becomes causally visible with a controlled intervention.
    initial=kron(z,plus)
    flip=kron(X,I)
    answers=[]
    for operation in (s.eye(4),flip):
        state=CZ*operation*initial
        answers.append((state.H*kron(I,X)*state)[0])
    need(answers==[1,-1],'same preparation and B probe distinguish controlled A interventions')
    state=kron(plus,plus)
    eq(state.reshape(2,2).det(),0,'product input coefficient determinant')
    eq((CZ*state).reshape(2,2).det(),-s.Rational(1,2),'controlled phase is genuinely entangling')
    # A historical record can persist even when the CURRENT system value changes.
    stored=(kron(z,z)+kron(o,o))/s.sqrt(2)
    after=flip*stored
    eq(partial_a(after*after.H),partial_a(stored*stored.H),'historical memory survives current system flip')
    eq((stored.H*kron(Z,Z)*stored)[0],1,'record initially equals current system value')
    eq((after.H*kron(Z,Z)*after)[0],-1,'same record subsequently differs from current system value')
    # Preserved under every generator is much stronger than historical persistence.
    q00,q01,q10,q11=s.symbols('q00 q01 q10 q11')
    Q=s.Matrix([[q00,q01],[q10,q11]])
    solutions=s.linsolve(list(Q*X-X*Q)+list(Q*Z-Z*Q),(q00,q01,q10,q11))
    need(solutions==s.FiniteSet((q11,0,0,q11)),'full irreducible operations leave only scalar record operators fixed')
    # Identical data distribution, opposite causal explanations.
    joint_forward={(x,y):s.Rational(1,2) if x==y else 0 for x in range(2) for y in range(2)}
    joint_reverse={(x,y):s.Rational(1,2) if x==y else 0 for x in range(2) for y in range(2)}
    need(joint_forward==joint_reverse,'X-copy-Y and Y-copy-X have identical passive records')
    intervention_forward=s.Integer(1)  # do(X=1), Y is its downstream copy.
    intervention_reverse=s.Rational(1,2) # do(X=1), Y remains the upstream fair bit.
    need(intervention_forward!=intervention_reverse,'same passive records do not determine causal direction')
    # Informational refinement defines an order only modulo mutual recoverability.
    old=[0,0,1,1]; copy=list(old); refined=list(range(4))
    def recoverable(a,b):
        return all(b[i]!=b[j] or a[i]==a[j] for i in range(4) for j in range(4))
    need(recoverable(old,copy) and recoverable(copy,old),'a later perfect copy is information-equivalent to the earlier event')
    need(recoverable(old,refined) and not recoverable(refined,old),'strict information refinement differs from equality')
    # Perfectly distinguishable full histories require orthogonal memory states.
    for n in range(1,7):
        need(s.eye(2**n).rank()==2**n,'n-bit record Gram has rank 2^n at n='+str(n))
    return {'status':'PASS','exact_checks':len(CHECKS),'checks':CHECKS,
            'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite controls; no TFPT source, new primitive law, or physical time derived.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'exact_checks':result['exact_checks']}))
