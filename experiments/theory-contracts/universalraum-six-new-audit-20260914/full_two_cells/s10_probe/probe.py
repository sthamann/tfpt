"""Bounded probe only: exact one-cut polynomial positivity in S10(4,3,2,1)."""
from pathlib import Path
import sys,json,time
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from checker import young,graph_operator
HERE=Path(__file__).resolve().parent;tic=time.time()
source=HERE.parents[1]/'spectral'/'nonsinglet_frontier'/'cluster_scout_10.json'
record=json.loads(source.read_text())['motifs'][7];edges=record['edges']
print('BUILD_START',flush=True)
gens=young((4,3,2,1),True)
print('GENERATORS_BUILT',round(time.time()-tic,3),flush=True)
X=graph_operator(gens,edges)
print('X_BUILT',round(time.time()-tic,3),flush=True)
z=s.Symbol('z');cut=-s.Rational(403,50)
# det(zI+(X-cutI)), roots = cut-eigenvalues(X).
poly=(-X+cut*s.eye(X.rows)).charpoly(z).as_poly()
positive=all(c>0 for c in poly.all_coeffs())
if not positive:raise RuntimeError('coefficient sign certificate failed')
out={'status':'EXACT_ONE_CUT_CERTIFICATE','shape':[4,3,2,1],'dimension':X.rows,
     'edges':edges,'strict_lower_bound_H_over_J':'447/100','X_cut':'-403/50',
     'all_shifted_charpoly_coefficients_positive':True,
     'coefficients':[str(c) for c in poly.all_coeffs()],'elapsed_seconds':time.time()-tic}
(HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print('CERTIFIED',round(time.time()-tic,3),flush=True)
