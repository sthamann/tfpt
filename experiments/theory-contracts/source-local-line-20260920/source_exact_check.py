"""Exact source-symbol checks; analytic limits are proved in SOURCE_LINE_PROOF.txt."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import sympy as sp

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
SOURCE = ROOT / 'verification/v1033_charged_disorder.py'
CLOCKS = ROOT / 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'
CHECKS = []

def require(condition, label):
    if not condition:
        raise ValueError(label)
    CHECKS.append(label)

def exact_matrix(a):
    return sp.Matrix(a).applyfunc(sp.nsimplify)

def run():
    sys.path.insert(0, str(SOURCE.parent))
    spec = importlib.util.spec_from_file_location('original_v1033_local_line', SOURCE)
    source = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = source
    spec.loader.exec_module(source)
    tx, ty, sz = map(exact_matrix, (source.TX, source.TY, source.SZ))
    sx = sp.Matrix([[0, 1], [1, 0]])
    require(tx == -sp.I*sx/2 - sz/2, 'actual source TX')
    require(ty == sp.Matrix([[-1, -1], [1, 1]])/2, 'actual source TY')
    h0 = sp.zeros(16)
    for y in range(8):
        h0[2*y:2*y+2, 2*y:2*y+2] = sz + tx + tx.conjugate().T
        if y < 7:
            h0[2*y+2:2*y+4, 2*y:2*y+2] = ty
            h0[2*y:2*y+2, 2*y+2:2*y+4] = ty.T
    require(h0.T == h0, 'zero-momentum source Hermitian')
    require(h0**3 == h0, 'exact polynomial h0 cubed equals h0')
    require(h0.rank() == 14 and sp.trace(h0) == 0, 'two zero modes and seven at each sign')
    top, bottom, opposite = sp.zeros(16, 1), sp.zeros(16, 1), sp.zeros(16, 1)
    top[14], top[15] = 1/sp.sqrt(2), 1/sp.sqrt(2)
    opposite[14], opposite[15] = 1/sp.sqrt(2), -1/sp.sqrt(2)
    bottom[0], bottom[1] = 1/sp.sqrt(2), -1/sp.sqrt(2)
    v = sp.Matrix.hstack(top, bottom)
    require(v.T*v == sp.eye(2), 'orthonormal spatially distinct edge rows')
    require(sp.eye(16)-h0**2 == v*v.T, 'complete zero-mode projector')
    hprime = -sp.kronecker_product(sp.eye(8), sx)
    require(v.T*hprime*v == sp.diag(-1, 1), 'one left and one right slope, not eight species')
    u, z = sp.symbols('u z', real=True)
    hp = h0-u*sp.kronecker_product(sp.eye(8), sx)+z*sp.kronecker_product(sp.eye(8), sz)
    require(hp*top == -u*top + z*opposite, 'actual top-row identity for sin p and 1-cos p')
    a, k, sinp, cosp = sp.symbols('a k sinp cosp', real=True, nonzero=True)
    residual = (hp.subs({u:sinp,z:1-cosp})/a + k*sp.eye(16))*top
    require(sp.simplify((residual.T*residual)[0] - ((k-sinp/a)**2+((1-cosp)/a)**2)) == 0,
            'orthogonal exact residual norm')
    clocks = json.loads(CLOCKS.read_text())['clock_matrices']
    delta = sp.ones(8, 1)/4
    details = {}
    for label in ('C', 'J'):
        g = sp.Matrix(clocks[label]['vector'])
        require(g.T*g == sp.eye(8), label+' actual orthogonal charge action')
        d = g*delta-delta
        require((d.T*d)[0] == 1, label+' exact radius-defect constant')
        details[label] = {'squared_displacement': str((d.T*d)[0])}
    t, aa = sp.symbols('t aa', real=True)
    series = sp.series(sp.exp(aa*t)*t*t/(4*sp.sinh(t/2)**2),t,0,3).removeO().expand()
    require(sp.simplify(series-(1+aa*t+(aa*aa/2-sp.Rational(1,12))*t*t)) == 0,
            'charged local two-point asymptotic coefficients')
    iota = sp.diag(-1,-1,-1,1,1)
    pplus = (sp.eye(5)+iota)/2
    w = sp.eye(5)[:,3:5]
    require(iota*pplus == pplus and pplus*w == w and w.T*iota*w == sp.eye(2),
            'literal same-involution positive compression loses the negative carrier')
    return {'status':'PASS', 'checks':CHECKS,
        'source':{'path':str(SOURCE),'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
        'clock_certificate':{'path':str(CLOCKS),'sha256':hashlib.sha256(CLOCKS.read_bytes()).hexdigest()},
        'h0_spectrum':{'-1':7,'0':2,'1':7},'top_bottom_slopes':[-1,1],
        'polarization_gate':'General conditional proof in POLARIZATION_GATE.txt; finite five-slot witness checked here.',
        'clock_displacements':details,
        'scope':'Exact finite source-symbol and clock checks only; limits are analytic, no rank-eight microscopic source claim.'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
