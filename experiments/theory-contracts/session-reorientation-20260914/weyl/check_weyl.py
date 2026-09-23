#!/usr/bin/env python3
"""Exact, bounded A3/BCC/Weyl audit; no native TFPT realization asserted."""
import argparse
import itertools as it
import json
import sympy as s

p = argparse.ArgumentParser()
p.add_argument('--mutant', choices=['drop_inverse', 'single_node', 'same_cone'])
args = p.parse_args()
checks = 0

def require(value, label):
    global checks
    checks += 1
    if not bool(value):
        raise RuntimeError(label)

def eq(a, b):
    if isinstance(a, s.MatrixBase):
        return all(s.simplify(x) == 0 for x in a-b)
    return s.simplify(a-b) == 0

I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
pauli = [X, Y, Z]
h = [s.Matrix(t) for t in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
w = [v/2 for v in h]
for i, j in it.product(range(4), repeat=2):
    require(w[i].dot(w[j]) == int(i==j)-s.Rational(1,4), 'tetrahedron weight Gram')
root_basis = s.Matrix.hstack(*[w[i]-w[i+1] for i in range(3)])
weight_basis = s.Matrix.hstack(w[0], w[0]+w[1], w[0]+w[1]+w[2])
require(abs(root_basis.det()) == 2, 'FCC covolume')
require(abs(weight_basis.det()) == s.Rational(1,2), 'BCC covolume')
require(abs(root_basis.det()/weight_basis.det()) == 4, 'weight/root index four')
require(all(x.is_Integer for x in root_basis.T*weight_basis), 'root weight dual pairing')
require((root_basis.T*weight_basis).det() in [-1, 1], 'full dual, not merely sublattice')
roots = {tuple(w[i]-w[j]) for i in range(4) for j in range(4) if i != j}
require(len(roots) == 12, 'twelve FCC roots')
require(all(sum(t)==0 or sum(t) in [-2,2] for t in roots), 'FCC even coordinate sum')
require(all(sum(a*a for a in t)==2 for t in roots), 'FCC nearest root length')
require(len({tuple(v) for v in w}) == 4, 'only four fundamental representation weights')
require(len({tuple(sign*v) for sign in [-1,1] for v in w}) == 8, 'eight BCC nearest steps need negatives')
require(abs(s.Matrix.hstack(*h[:3]).det()) == 4, 'scaled BCC primitive volume')

steps = list(it.product([-1,1], repeat=3))
A = {e: ((I+e[0]*X)/2)*((I+e[1]*Y)/2)*((I+e[2]*Z)/2) for e in steps}
if args.mutant == 'drop_inverse':
    A = {e:a for e,a in A.items() if e[0]*e[1]*e[2] == 1}
for e, a in A.items():
    require(a.rank() == 1, 'all eight coefficients nonzero rank one')
require(eq(sum(A.values(), s.zeros(2)), I), 'zero momentum normalization')
for delta in it.product([-2,0,2], repeat=3):
    left, right = s.zeros(2), s.zeros(2)
    for e, f in it.product(A, repeat=2):
        if tuple(e[i]-f[i] for i in range(3)) == delta:
            left += A[e]*A[f].H
            right += A[e].H*A[f]
    expected = I if delta == (0,0,0) else s.zeros(2)
    require(eq(left, expected), 'all-momentum UUdagger Laurent coefficient')
    require(eq(right, expected), 'all-momentum UdaggerU Laurent coefficient')
flips = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
for flip, coin in zip(flips, [I,X,Y,Z]):
    for e in steps:
        target = tuple(flip[i]*e[i] for i in range(3))
        require(eq(A[target], coin*A[e]*coin.H), 'projective D2 isotropy')
require({tuple(f[i]*h[0][i] for i in range(3)) for f in flips} == {tuple(v) for v in h}, 'D2 transitive forward tetrahedron')

k = s.symbols('kx ky kz', real=True)
c = [s.cos(x) for x in k]
t = [s.sin(x) for x in k]
u = c[0]*c[1]*c[2]-t[0]*t[1]*t[2]
n = s.Matrix([t[0]*c[1]*c[2]+c[0]*t[1]*t[2],
              c[0]*t[1]*c[2]-t[0]*c[1]*t[2],
              c[0]*c[1]*t[2]+t[0]*t[1]*c[2]])
product = I
for j in range(3):
    product = product*(c[j]*I-s.I*t[j]*pauli[j])
require(eq(product, u*I-s.I*sum((n[j]*pauli[j] for j in range(3)), s.zeros(2))), 'explicit Weyl symbol')
require(eq(n.jacobian(k).subs(dict.fromkeys(k,0)), s.eye(3)), 'linear Weyl low momentum symbol')
nodes = [(0,0,0),(s.pi,0,0),(s.pi/2,s.pi/2,s.pi/2),(-s.pi/2,-s.pi/2,-s.pi/2)]
records = []
for point in nodes:
    subs = dict(zip(k,point))
    sign = u.subs(subs)
    jac = n.jacobian(k).subs(subs)
    require(eq(n.subs(subs), s.zeros(3,1)), 'Weyl node exact zero')
    require(sign in [1,-1], 'node quasienergy zero or pi')
    # U(k0+q)=sign*[I-i (sign*Jac(n))*q.sigma]+O(q^2).
    centered = sign*jac
    require(abs(centered.det()) == 1, 'nondegenerate centered Floquet Weyl cone')
    records.append({'k_over_pi':[str(s.simplify(x/s.pi)) for x in point],
                    'U_sign':int(sign), 'det_Jn':int(jac.det()),
                    'centered_chirality':int(centered.det())})
for i,j in it.combinations(range(4),2):
    m = [s.simplify((nodes[i][r]-nodes[j][r])/s.pi) for r in range(3)]
    reciprocal = all(x.is_Integer for x in m) and sum(m)%2 == 0
    require(not reciprocal, 'nodes inequivalent modulo actual BCC reciprocal lattice')
if args.mutant == 'single_node':
    records = records[:1]
require(sum(r['centered_chirality'] for r in records) == 0, 'two opposite chiralities, not one')

omega, v1, v2 = s.symbols('omega v1 v2', real=True)
H = sum((k[j]*pauli[j] for j in range(3)), s.zeros(2))
D = s.diag(v1*H, v2*H)
if args.mutant == 'same_cone':
    D = s.diag(v1*H, v1*H)
r2 = sum(x*x for x in k)
require(eq((omega*s.eye(4)-D).det(), (omega**2-v1**2*r2)*(omega**2-v2**2*r2)), 'one D permits two characteristic cones')
require((D.subs({v1:1,v2:2,k[0]:1,k[1]:0,k[2]:0})).eigenvals() == {-2:1,-1:1,1:1,2:1}, 'concrete common-clock different speeds')
q = s.symbols('q1:5', real=True)
four_dim_coefficients = s.Matrix([q[0],q[1],q[2]**2+q[3]**2])
require(four_dim_coefficients.jacobian(q).subs(dict.fromkeys(q,0)).rank() == 2, 'isolated 4D counterexample is singular, not regular Weyl')
require(four_dim_coefficients[2].is_nonnegative, '4D isolated zero uses sum of squares')
require(s.factorial(5) > s.factorial(4), 'faithful S5 cannot permute four forward directions')

print(json.dumps({'status':'PASS','checks':checks,'exact_arithmetic':True,
  'scope':'conditional BCC construction; no native TFPT spatial realization',
  'nodes':records,'primitive_reciprocal':'pi * {m in Z^3: sum(m) even}',
  'root_covolume':'2','weight_covolume':'1/2','mutant':args.mutant}, indent=2))
