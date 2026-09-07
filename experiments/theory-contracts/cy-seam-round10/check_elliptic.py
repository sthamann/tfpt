"""Exact, bounded algebra checks for the pasted elliptic-surface proposal.

This checks identities, not physical or analytic determinant claims.
Run using the tfpt-discovery virtualenv Python (SymPy required).
"""
import json
import sympy as s

t, u, x, y, z = s.symbols("t u x y z")
Q = s.Rational
b2, b4, b6, b8 = 1 + 4*t, t, t**2, t**3
c4 = s.expand(b2**2 - 24*b4)
c6 = s.expand(-b2**3 + 36*b2*b4 - 216*b6)
disc = s.expand(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
assert s.expand(c4**3-c6**2-1728*disc) == 0
assert s.factor(disc) == -t**4*(16*t-1)
assert s.expand(c6 + (8*t-1)*(8*t*t+16*t-1)) == 0
cm = [Q(1,8), -1+3*s.sqrt(2)/4, -1-3*s.sqrt(2)/4]
assert all(s.simplify(c6.subs(t,v)) == 0 for v in cm)
assert all(s.simplify(disc.subs(t,v)) != 0 for v in cm)

# Inversion fixes exactly the three finite roots in completed-square form.
curve = y*y+(x+t)*y-x**3-t*x*x
reduce_curve = s.groebner([curve], y, x, domain=s.QQ.frac_field(t))
def red(expr):
    numerator = s.cancel(expr).as_numer_denom()[0]
    return s.factor(reduce_curve.reduce(numerator)[1])

# Addition by P=(0,0), validated on the curve.
xp = -t*y/x**2
yp = t*t*(x*x-y)/x**3
assert red(curve.subs({x:xp,y:yp}, simultaneous=True)) == 0
assert red((x*x-y)*(x*x+x+y+t)-x**4) == 0
assert red(y*y/(x+t)-(x*x-y)) == 0
# Thus div(x^2-y)=4P-4O, and its inverse-point analogue is below.

# Quotient by T=2P: standard degree-two isogeny.
a, b = Q(1,4)-2*t, t*t
v = s.symbols("v")
isog_x = u+a+b/u
isog_y = v*(1-b/u**2)
isog_equation = isog_y**2-isog_x*(isog_x**2-2*a*isog_x+a*a-4*b)
assert s.factor(isog_equation.subs(v*v,u*(u*u+a*u+b))) == 0
assert s.factor(z*(z*z-2*a*z+a*a-4*b)-z*(z-Q(1,4))*(z-Q(1,4)+4*t)) == 0

# CM automorphism on E[2]=(Z/2)^2 interchanges the two axes.
pts = [(0,0),(1,0),(0,1),(1,1)]
def cycle(T):
    ans, point = [], (0,0)
    while point not in ans:
        ans.append(point)
        point = (point[1]^T[0],point[0]^T[1])
    return ans
assert len(cycle((1,1))) == 2
assert len(cycle((1,0))) == len(cycle((0,1))) == 4
xT = (1-8*t)/12
assert s.simplify(xT.subs(t,cm[0])) == 0
assert all(s.simplify(xT.subs(t,v)) != 0 for v in cm[1:])

# Distinguishes the two surviving elliptic curves WITH P marked.
# x(P)^2/A is invariant under short-Weierstrass origin-preserving isomorphisms.
marked_invariants = [s.simplify((-(1+4*t)**2/(3*c4)).subs(t,v)) for v in cm]
assert s.simplify(marked_invariants[1]-marked_invariants[2]) != 0

# Positive D5+A3 root lattice; glue spinor/fundamental weights of norms 5/4,3/4.
D5 = s.Matrix([[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,-1],[0,0,-1,2,0],[0,0,-1,0,2]])
A3 = s.Matrix([[2,-1,0],[-1,2,-1],[0,-1,2]])
G = s.diag(D5,A3)
glue = s.Matrix(list(D5.inv()[:,4])+list(A3.inv()[:,0]))
assert G.det() == 16 and (glue.T*G*glue)[0] == 2
assert all(v.q == 1 for v in 4*glue) and any(v.q != 1 for v in 2*glue)
assert all(v.q == 1 for v in G*glue)
# Adding the glue generator gives an even integral index-four overlattice.
assert G.det()/4**2 == 1

# Degree-four theta lift on H0(E,O(4O)), basis (1,x,y,x^2).
# Lift is s(z) -> h(z)s(z+P), h=x^2+x+y+t with divisor 4(-P)-4O.
h = x*x+x+y+t
basis = [s.Integer(1),x,y,x*x]
M = s.Matrix([[t,-t*t,0,t**3],[1,-t,t*t,t*t],[1,-t,0,0],[1,0,0,0]])
for j, f in enumerate(basis):
    target = sum(M[k,j]*basis[k] for k in range(4))
    assert red(h*f.subs({x:xp,y:yp},simultaneous=True)-target) == 0
assert s.simplify(M**4-t**6*s.eye(4)) == s.zeros(4)
assert s.factor(M.charpoly(z).as_expr()) == (z*z-t**3)*(z*z+t**3)

report = {
    "status":"all exact algebra assertions passed",
    "c4":str(c4), "c6":str(s.factor(c6)), "Delta":str(s.factor(disc)),
    "at_infinity":{name:str(s.factor(u**weight*expr.subs(t,1/u))) for name,weight,expr in [("c4",4,c4),("c6",6,c6),("Delta",12,disc)]},
    "j1728_parameters":[str(v) for v in cm],
    "marked_P_isomorphism_invariants":[str(v) for v in marked_invariants],
    "two_isogenous_Kummer_branch_set":["infinity","0","1","1-16t"],
    "theta_matrix":[[str(v) for v in row] for row in M.tolist()],
    "theta_characteristic_polynomial":str(s.factor(M.charpoly(z).as_expr())),
    "scope":"Exact algebra only. Kodaira/minimal-model and theta interpretation require the stated mathematical arguments. No physical, analytic determinant, or RH claim."
}
print(json.dumps(report,indent=2))

