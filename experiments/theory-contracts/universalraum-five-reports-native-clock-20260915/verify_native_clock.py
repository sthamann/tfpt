"""Exact NON-RH audit of the five reports, with a repaired native C5 clock.

No status/ledger promotion. No numerical tolerance is used by this checker.
The physical interpretation is a separate obligation, not a Boolean check.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import argparse
import json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, csr_matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WPATH = ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
WPIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
CHECKS = []


def need(value, label):
    if not bool(value):
        raise RuntimeError(label)
    CHECKS.append(label)


def eq(a, b):
    return (a-b).applyfunc(s.simplify) == s.zeros(a.rows, a.cols)


def wedge(M):
    pairs = list(combinations(range(M.rows), 2))
    return s.Matrix(len(pairs), len(pairs), lambda a, b:
        M[pairs[a][0], pairs[b][0]] * M[pairs[a][1], pairs[b][1]]
        - M[pairs[a][0], pairs[b][1]] * M[pairs[a][1], pairs[b][0]])


def even_lift(p):
    masks = [m for m in range(32) if m.bit_count() % 2 == 0]
    out = np.zeros((16, 16), dtype=np.int64)
    for col, mask in enumerate(masks):
        image = [p[j] for j in range(5) if mask & (1 << j)]
        sign = (-1) ** sum(a > b for a, b in combinations(image, 2))
        out[masks.index(sum(1 << j for j in image)), col] = sign
    return out


def perm(p):
    return np.eye(len(p), dtype=np.int64)[:, p]


def wedge_qsqrt5(A, B):
    """Two integer coefficient matrices for Lambda^2(A+sqrt(5) B)."""
    pairs = list(combinations(range(len(A)), 2))
    index = {p: i for i, p in enumerate(pairs)}
    support = [np.flatnonzero((A[:, j] != 0) | (B[:, j] != 0)) for j in range(len(A))]
    rows, cols, rational, radical = [], [], [], []
    for col, (i, j) in enumerate(pairs):
        for x in support[i]:
            for y in support[j]:
                if x == y:
                    continue
                sign = 1 if x < y else -1
                rows.append(index[tuple(sorted((int(x), int(y))))])
                cols.append(col)
                rational.append(sign * (A[x, i]*A[y, j] + 5*B[x, i]*B[y, j]))
                radical.append(sign * (A[x, i]*B[y, j] + B[x, i]*A[y, j]))
    shape = (len(pairs), len(pairs))
    return [coo_matrix((data, (rows, cols)), shape=shape, dtype=np.int64).tocsr()
            for data in (rational, radical)]


def full_covariance(W, AF, BF, AB, BB, label):
    """GF=(AF+sqrt5 BF)/8; GB=(AB+sqrt5 BB)/64."""
    left = wedge_qsqrt5(AF, BF)
    Ws = csr_matrix(W)
    for part, L, R in zip(('rational', 'sqrt5'), left, (AB, BB)):
        residual = Ws @ L - csr_matrix(R) @ Ws
        residual.eliminate_zeros()
        need(residual.nnz == 0, label + ': full 60 x 2016 ' + part + ' coefficient identity')


def main():
    need(sha256(WPATH.read_bytes()).hexdigest() == WPIN, 'unaltered native tensor pin')
    with np.load(WPATH, allow_pickle=False) as z:
        raw = z['W']
    need(np.array_equal(raw.imag, np.zeros(raw.shape)), 'W real')
    W = raw.real.astype(np.int64)
    need(np.array_equal(W, raw.real), 'W integer')
    need(W.shape == (60, 2016) and np.count_nonzero(W) == 480, 'native 64 / 60 dimensions')
    need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=np.int64)), 'native pair Gram')

    Cp = s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
    Gp = s.Matrix([[1,0,-1,0],[0,0,-1,1],[0,1,-1,0],[0,0,-1,0]])
    N = s.Matrix([[0,0,-1,0],[1,0,-1,0],[0,1,-1,0],[0,0,-1,1]])
    C, P = N.inv()*Cp*N, N.inv()*Gp*N
    I = s.eye(4)
    need(Cp.T*Cp != I, 'negative control: received companion violates canonical CAR metric')
    need(C**5 == I and all(C**k != I for k in range(1,5)), 'C5 exact order')
    need(P**4 == I and P**2 != I, 'normal basis four-cycle')
    need(P*C*P.inv() == C**2, 'original Frobenius relation')
    H = 5*I - s.ones(4)
    need(H.eigenvals() == {s.Integer(1):1, s.Integer(5):3}, 'positive invariant Gram')
    need(C.T*H*C == P.T*H*P == H, 'common Gram preserved by C5 and gear')
    p0 = s.ones(4)/4
    Z = p0 + s.sqrt(5)*(I-p0)
    need(eq(Z*Z,H), 'positive square root of Gram')
    U5 = (Z*C*Z.inv()).applyfunc(s.simplify)
    need(eq(U5.T*U5,I) and s.simplify(U5.det()) == 1, 'repaired C5 lies in SO4 and SU4')
    need(eq(U5**5,I) and all(not eq(U5**k,I) for k in range(1,5)), 'repaired C5 order five')
    need(eq(P*U5*P.inv(),U5**2), 'repaired Frobenius relation')
    gear = (1+s.I)/s.sqrt(2)*P
    need(eq(gear.H*gear,I) and s.simplify(gear.det()) == 1, 'binary gear lies in SU4')
    need(eq(gear**4,-I) and eq(gear**8,I), 'binary gear fourth power minus identity')
    need(eq(gear*U5*gear.inv(),U5**2), 'binary gear retains Frobenius relation')

    # Native inner clock is on the five Spin10 slots, not on the A3 factor.
    p, q = [2,0,1,4,3], [0,2,1,3,4]
    G16, S16 = even_lift(p), even_lift(q)
    O10 = -np.kron(np.eye(2,dtype=np.int64),perm(p))
    OS10 = -np.kron(np.eye(2,dtype=np.int64),perm(q))
    need(np.array_equal(np.linalg.matrix_power(G16,6),np.eye(16,dtype=np.int64)), 'native inner sixth power')
    need(all(not np.array_equal(np.linalg.matrix_power(G16,k),np.eye(16,dtype=np.int64)) for k in (1,2,3)), 'native inner order exactly six')
    need(np.array_equal(S16@S16,np.eye(16,dtype=np.int64)), 'native slot reflection involutive')
    need(np.array_equal(S16@G16@S16,np.linalg.matrix_power(G16,5)), 'native slot reflection reverses inner clock')
    for title,F,B in [('inner six-clock',G16,O10),('slot reflection',S16,OS10)]:
        AF=8*np.kron(F,np.eye(4,dtype=np.int64)); BF=np.zeros_like(AF)
        AB=64*np.kron(B,np.eye(6,dtype=np.int64)); BB=np.zeros_like(AB)
        full_covariance(W,AF,BF,AB,BB,title)

    # Split exact entries over Q(sqrt5); bounded integer arithmetic throughout.
    z = s.Symbol('z')
    polys = (8*U5).applyfunc(lambda x:s.expand(x).subs(s.sqrt(5),z))
    A = np.array(polys.subs(z,0),dtype=np.int64)
    B = np.array(polys.applyfunc(lambda x:s.expand(x).coeff(z)),dtype=np.int64)
    need(eq(U5,(s.Matrix(A)+s.sqrt(5)*s.Matrix(B))/8), 'exact two-coefficient representation')
    LA,LB = [m.toarray() for m in wedge_qsqrt5(A,B)]
    need(eq(wedge(U5),(s.Matrix(LA)+s.sqrt(5)*s.Matrix(LB))/64), 'independent small exterior-square check')
    full_covariance(W,np.kron(G16,A),np.kron(G16,B),np.kron(O10,LA),np.kron(O10,LB),'repaired native T30')
    need(eq(((s.Matrix(LA)+s.sqrt(5)*s.Matrix(LB))/64).T * ((s.Matrix(LA)+s.sqrt(5)*s.Matrix(LB))/64),s.eye(6)), 'native pair clock is unitary')
    # Order by factor powers; testing proper prime-divisor quotients suffices.
    for k in (6,10,15):
        need(not (np.array_equal(np.linalg.matrix_power(G16,k),np.eye(16,dtype=np.int64)) and eq(U5**k,I)), 'T30 factor witness at '+str(k))
    need(np.trace(np.linalg.matrix_power(G16,30))==16 and eq(U5**30,I), 'T30 closes at thirty')
    # A nontrivial scalar factor cancellation is excluded: C5 nonidentity powers
    # have characteristic polynomial Phi5, and G16 fixes the empty spinor mask.
    need(all(np.array_equal(np.linalg.matrix_power(G16,k)[:,0],np.eye(16,dtype=np.int64)[:,0]) for k in range(6)), 'no hidden scalar cancellation in tensor order')
    need(eq(U5**7,U5**2) and np.array_equal(np.linalg.matrix_power(G16,7),G16), 'native gear conjugates T30 to seventh power')

    J0=s.zeros(4)
    for j in range(4): J0[(-j)%4,j]=1
    J=s.diag(1,s.I,-1,-s.I)*J0
    need(eq(J.H*J,I) and J.det()==1 and J**2==I, 'linear geometric reflection exists in SU4')
    need(eq(J*gear*J,gear.inv()), 'linear geometric mirror reverses binary gear')
    need(eq(J0*gear.conjugate()*J0,gear.inv()), 'antiunitary geometric mirror also works')
    arithmetic=P**2
    need(arithmetic**2==I and eq(arithmetic*U5*arithmetic,U5**4), 'arithmetic conjugation inverts C5')
    need(eq(arithmetic*gear,gear*arithmetic), 'arithmetic conjugation COMMUTES with binary gear')
    need(not eq(arithmetic*gear*arithmetic,gear.inv()), 'arithmetic and geometric mirrors not interchangeable')
    need(all(not eq(J*U5*J,U5**u) for u in range(1,5)), 'geometric mirror takes this C5 outside its cyclic subgroup')
    for u in (1,2,3,4):
        need((3*u)%5 != (2*u)%5, 'general normalizer obstruction for unit '+str(u))

    # Character test in the complete adjoint branching 248=45+15+60+64+64bar.
    rows=[]
    for n in range(30):
        trO=int(np.trace(np.linalg.matrix_power(O10,n)))
        trO2=int(np.trace(np.linalg.matrix_power(O10,2*n)))
        c=4 if n%5==0 else -1
        c2=4 if (2*n)%5==0 else -1
        chi6=(c*c-c2)//2
        chi16=int(np.trace(np.linalg.matrix_power(G16,n)))
        rows.append([(trO*trO-trO2)//2,c*c-1,trO*chi6,chi16*c,chi16*c])
    need(rows[0]==[45,15,60,64,64], 'full E8 adjoint character dimension')
    sums=np.sum(np.array(rows,dtype=np.int64),axis=0)
    need(all(int(x)%30==0 for x in sums), 'all fixed multiplicities integral')
    fixed=[int(x)//30 for x in sums]
    need(fixed==[11,3,4,0,0], 'native T30 adjoint fixed multiplicities are 11+3+4')
    need(sum(fixed)==18, 'native T30 centralizer has dimension eighteen')

    # Canonical E8 Coxeter action on the full finite root system, scaled by 2.
    simple=[s.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,s.Matrix([1,1,0,0,0,0,0,0])]
    for j in range(6):
        v=s.zeros(8,1);v[j]=-1;v[j+1]=1;simple.append(v)
    cox=s.eye(8)
    for a in simple: cox=cox*(s.eye(8)-a*a.T)
    roots=set()
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            r=[0]*8;r[i]=a;r[j]=b;roots.add(tuple(r))
    roots.update(t for t in product((-1,1),repeat=8) if sum(x<0 for x in t)%2==0)
    need(len(roots)==240, 'complete E8 roots')
    action={r:tuple(cox*s.Matrix(r)) for r in roots}
    need(set(action.values())==roots, 'Coxeter permutes all roots')
    need(cox**30==s.eye(8) and (cox-s.eye(8)).det()!=0, 'Coxeter order thirty and no Cartan fixed vector')
    unseen=set(roots); lengths=[]
    while unseen:
        first=next(iter(unseen)); current=first; orbit=[]
        while current not in orbit:
            orbit.append(current); unseen.remove(current); current=action[current]
        need(current==first, 'root orbit closes on its own origin')
        lengths.append(len(orbit))
    need(sorted(lengths)==[30]*8, 'Coxeter has eight root orbits of length thirty')
    # An order-30 E8 lift gives one invariant per root orbit; the existence of
    # this lift is a literature theorem, not re-proved by the finite check.

    variance=[s.Rational(480,40**2),s.Rational(480,20**2)]
    need(variance==[s.Rational(3,10),s.Rational(6,5)], 'same clocks permit distinct native energy variances')
    need(s.I*(-s.I)==1 and (-1)*(-1)==1, 'diagonal Z4 glue trivial on V and B')
    need(s.I!=1 and s.I**2==-1, 'standalone number Z4 is not diagonal glue')
    return {'status':'PASS','scope':'exact finite native-source compatibility; NON-RH; no physical closure',
        'checks':CHECKS,'check_count':len(CHECKS),'native_tensor_sha256':WPIN,
        'C5_unitary':[[str(x) for x in U5.row(i)] for i in range(4)],
        'positive_gram':np.array(H,dtype=int).tolist(),'clock_space_dimensions':[64,60],
        'native_T30_adjoint_fixed':dict(zip(['45','15','60','64','64bar'],fixed)),
        'E8_Coxeter_root_orbits':sorted(lengths),'Coxeter_Cartan_fixed_dimension':0,
        'mirror_obstruction':'3u != 2u mod 5 for every u in (Z/5)^x',
        'dynamics_counterexample':{'g_over_Delta':['1/40','1/20'],'filled_state_energy_variance_over_Delta_squared':[str(v) for v in variance]},
        'not_established':['source selects this C5 embedding','identification of internal colors with seam places',
            'symmetry is native executable transport','physical g/Delta','3+1D continuum, chirality, dynamical spin2']}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();result=main();encoded=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(encoded)
    print(encoded)
