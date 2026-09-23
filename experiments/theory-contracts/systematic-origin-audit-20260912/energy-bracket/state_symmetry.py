"""NON-RH exact symmetries of the t=1/8 filtered-dimer variational state."""
import ast
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[4]
PINS = {
    "experiments/theory-contracts/compiler-clifford-bridge/checker.py":
    "bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d",
    "experiments/theory-contracts/systematic-origin-audit-20260912/uniform-chain/dimer_filter.py":
    "53792526398ae08559169493b48a833a05623aa8efc6b3d7747b7a6c7f10aa80",
}
CHECKS = 0


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


def run():
    for path, pin in PINS.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    source = next(iter(PINS))
    node = next(n for n in ast.parse((ROOT/source).read_text()).body
                if isinstance(n, ast.FunctionDef) and n.name == "generators")
    env = {"s": s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), source, "exec"), env)
    g = env["generators"]()
    a = tuple(s.I*x for x in g)
    I, I16 = s.eye(4), s.eye(16)
    h = 2*I16-sum((s.kronecker_product(x, x.conjugate()) for x in a), s.zeros(16))/2
    F = I16-h/8
    require(h == h.conjugate() == h.T, "same real matrix on reversed alternating edge")
    phi = I.reshape(16, 1)/2
    w = (I+g[0]*g[1]+g[1]*g[2]+g[2]*g[0])/2
    for u in (*g, w):
        dual = s.kronecker_product(u, u.conjugate())
        require(dual*phi == phi, "initial Bell vector source invariant")
        require(dual*F == F*dual, "filter primitive/family covariance")
    for i, j in itertools.combinations(range(4), 2):
        k = a[i]*a[j]
        generator = s.kronecker_product(k, I)+s.kronecker_product(I, k.conjugate())
        require(k.H == -k, "anti-Hermitian Spin4 bivector generator")
        require(generator*phi == s.zeros(16, 1), "Bell vector infinitesimal Spin4 invariance")
        require(generator*F == F*generator, "continuous Spin4 filter covariance")
    k = s.I*a[0]
    not_spin = s.kronecker_product(k, I)+s.kronecker_product(I, k.conjugate())
    require(not_spin*F != F*not_spin, "negative control: arbitrary U4 is not filter symmetry")
    tensors = [s.Matrix(4, 4, list(F[row, :]))/2 for row in range(16)]
    p = s.trace(F*F)/16
    require(p == s.Rational(37, 64), "actual filter norm")
    require(sum((A*A.H for A in tensors), s.zeros(4)) == p*I,
            "right transfer fixed matrix")
    require(sum((A.H*A for A in tensors), s.zeros(4)) == p*I,
            "left transfer fixed matrix")
    rho = F*F/(16*p)
    require(not_spin*rho != rho*not_spin, "state itself is not fully U4 invariant")
    left = s.Matrix(4, 4, lambda i,j: sum(rho[4*i+k,4*j+k] for k in range(4)))
    right = s.Matrix(4, 4, lambda i,j: sum(rho[4*k+i,4*k+j] for k in range(4)))
    require(left == right == I/4, "single-register states already maximally mixed")
    inside = s.trace(h*rho)
    products = []
    for gamma in a:
        L, R = s.zeros(4), s.zeros(4)
        for x, y, z in itertools.product(range(4), repeat=3):
            L += gamma.conjugate()[z,x]*tensors[4*x+y]*tensors[4*z+y].H
            R += gamma[z,y]*tensors[4*x+z].H*tensors[4*x+y]
        products.append(s.trace(R*L)/(4*p*p))
    between = 2-sum(products)/2
    require(inside == s.Rational(62, 37), "exact intracell bond expectation")
    require(between == s.Rational(435, 2738), "independent boundary insertion expectation")
    delta = inside-between
    mean = (inside+between)/2
    require(delta == s.Rational(4153, 2738), "nonzero thermodynamic dimer contrast")
    require(mean == s.Rational(5023, 5476), "mixture uniform bond expectation")
    plateau = (inside**2+between**2)/2-mean**2
    require(plateau == delta**2/4 > 0, "same-parity mixture connected plateau")
    require(inside*between-mean**2 == -plateau, "opposite-parity plateau sign")
    require(s.Matrix.hstack(*(A.reshape(16, 1) for A in tensors)).rank() == 16,
            "one-cell injectivity of selected branch")
    grades = [p,s.Rational(3,32),s.Rational(1,128),0,0]
    for bits in itertools.product((0, 1), repeat=4):
        word=I
        for bit, x in zip(bits,a):
            if bit:
                word *= x
        require(sum((A*word*A.H for A in tensors),s.zeros(4)) == grades[sum(bits)]*word,
                "complete exact clustering transfer spectrum")
    # Four-site periodic positive filter state: a finite control, not the
    # thermodynamic energy formula. Trace cyclicity gives two-site symmetry.
    tuples = list(itertools.product(range(4), repeat=4))
    state = {v:s.trace(tensors[4*v[0]+v[1]]*tensors[4*v[2]+v[3]]) for v in tuples}
    shifted = {v:state[v[-1:]+v[:-1]] for v in tuples}
    require(all(state[v] == state[v[2:]+v[:2]] for v in tuples), "finite two-site translation")
    norm = sum(abs(z)**2 for z in state.values())
    overlap = sum(s.conjugate(state[v])*shifted[v] for v in tuples)
    require(overlap**2 < norm**2, "finite shifted branch is a distinct ray")
    cat = {v:state[v]+shifted[v] for v in tuples}
    require(all(cat[v] == cat[v[-1:]+v[:-1]] for v in tuples), "finite plus-cat one-site symmetry")
    return {"checks":CHECKS,"pins":PINS,"t":"1/8",
            "primitive_family_invariant":True,"internal_Spin4_invariant":True,
            "single_site_reduced_state":"I4/4","two_site_translation":True,
            "one_site_branch_translation":False,"bond_contrast":str(delta),
            "mixture_uniform_energy":str(mean),"mixture_plateau":str(plateau),
            "branch_injective_in_two_site_cells":True,
            "original_chain_ground_proven":False,"original_chain_gap_proven":False,
            "unique_symmetric_ground_proven":False,"T1_T8_closed":[]}


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
