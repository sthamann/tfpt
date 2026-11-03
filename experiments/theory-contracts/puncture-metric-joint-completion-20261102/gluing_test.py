"""Diagnostic of gluing versus marginalization on the existing v252 fibers.

The two-point weight is diagnostic. It is not the original Higgs measure,
an admissible primitive P1 source, or a proposed physical source.
"""
import json
import sys
from pathlib import Path
import numpy as np

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
sys.path.insert(0, str(ROOT / 'verification'))
import v252_full_finite_triple as v

rng = np.random.default_rng(252)
ys = [rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3)) for _ in range(4)]
mr = rng.normal(size=(3,3)); mr = mr + mr.T
z3 = np.zeros((3,3),complex); z2 = np.zeros((2,2),complex)
dy = v.full_D(*ys,z3); dm = v.full_D(z3,z3,z3,z3,mr)
swap = v.Kswap(); keep = v.rep(1,z2,z3); gamma = v.grading()

def need(ok, description):
    if not ok:
        raise RuntimeError(description)

def source(r):
    # Same radial H=(0,r), same quaternionic one-form and h as R096.
    a = v.rep(0,np.array([[r,0],[0,r]],complex),z3)
    b = a @ (dy @ keep - keep @ dy)
    b = b + b.conj().T
    phi = b + swap @ b.conj() @ swap + dm
    h = .25*gamma - 1j*gamma @ phi
    need(np.linalg.norm(h-h.conj().T)<1e-12,'Hermitian original source')
    return h

def heat(h,t):
    ev,u = np.linalg.eigh(h)
    return (u*np.exp(-t*ev)) @ u.conj().T

h0,h1 = source(0.),source(1.)
def average(t):
    return .5*(heat(h0,t)+heat(h1,t))

t=.1
a,b=heat(h0,t),heat(h1,t)
k=average(t)
defect=average(2*t)-k@k
variance=.25*(a-b)@(a-b)
need(np.linalg.norm(defect-variance)<1e-10,'exact operator variance identity')
need(np.linalg.eigvalsh(defect).min()>-1e-11,'positive gluing defect')
need(np.trace(defect).real>0,'nonzero gluing defect')
need(np.linalg.norm(heat(h0,2*t)-a@a)<1e-10,'first full fiber glues')
need(np.linalg.norm(heat(h1,2*t)-b@b)<1e-10,'second full fiber glues')

times=[0.,.05,.1]
rp=np.block([[average(s+t_) for t_ in times] for s in times])
need(np.linalg.eigvalsh(rp).min()>-1e-10,'full finite time-Hankel RP kernel')
genvar=.25*(h0-h1)@(h0-h1)
small_t=1e-5
relative_small_t_error=np.linalg.norm((average(2*small_t)-average(small_t)@average(small_t))/small_t**2-genvar)/np.linalg.norm(genvar)
need(relative_small_t_error<1e-4,'analytic leading generator variance')

result={
  'result':'PASS',
  'source_dimension':96,
  'same_original_seed':252,
  'quarter_mode':.25,
  'higgs_radii':[0.,1.],
  'diagnostic_weights':[.5,.5],
  'normal_length':t,
  'gluing_defect_trace':float(np.trace(defect).real),
  'gluing_defect_min_eigenvalue':float(np.linalg.eigvalsh(defect).min()),
  'variance_identity_residual':float(np.linalg.norm(defect-variance)),
  'time_Hankel_min_eigenvalue':float(np.linalg.eigvalsh(rp).min()),
  'generator_variance_trace':float(np.trace(genvar).real),
  'generator_variance_limit_relative_error':float(relative_small_t_error),
  'original_measure_derived':False,
  'primitive_P1_countermodel':False,
  'physical_time_identified':False,
}
print(json.dumps(result,indent=2))
