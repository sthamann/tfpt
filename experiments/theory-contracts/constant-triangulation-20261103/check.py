import json
from pathlib import Path
import mpmath as mp
import sympy as s

mp.mp.dps = 70
pi = mp.pi
c = mp.mpf('299792458')
h = mp.mpf('6.62607015e-34')
hb = h/(2*pi)
G = mp.mpf('6.67430e-11')
me = mp.mpf('9.1093837139e-31')
ainv = mp.mpf('137.0359992168407')
alphaG = G*me**2/(hb*c)
u = 3/(4*pi**2)*mp.exp(-2*ainv)
rho = u*c**7/(64*pi**2*G**2*hb)
ell = mp.sqrt(hb*G/c**3)
lam = 8*pi*G*rho/c**4
SdS = 3*pi/(lam*ell**2)

# Rows M,L,T,Q,temperature; columns c,hbar,G,kB,e,me,epsilon0,rho_energy.
dim = s.Matrix([[0,1,-1,1,0,1,-1,1],
                [1,2,3,2,0,0,-3,-1],
                [-1,-1,-2,-2,0,0,2,-2],
                [0,0,0,0,1,0,2,0],
                [0,0,0,-1,0,0,0,0]])
vectors = {
    'alpha_without_4pi':s.Matrix([-1,-1,0,0,2,0,-1,0]),
    'alphaG_e':s.Matrix([-1,-1,1,0,0,2,0,0]),
    'rho_electron_units':s.Matrix([-5,3,0,0,0,-4,0,1]),
}
assert dim.rank() == 5
assert len(dim.nullspace()) == 3
assert all(dim*v == s.zeros(5,1) for v in vectors.values())
assert s.Matrix.hstack(*vectors.values()).rank() == 3

# Exact conventional four-dimensional Dirac bulk heat coefficients.
N,m0,chi,T = s.symbols('N m0 chi T', positive=True)
V = m0*chi**4*T/(4*s.pi**2)
Mb2 = m0*chi**2*T/(24*s.pi**2)
ratio = s.simplify(V/Mb2**2)
assert ratio == 144*s.pi**2/(m0*T)
assert s.simplify(V/Mb2-6*chi**2) == 0

# Independent radial heat integrals, exact in every constant mass eigenvalue.
p,z = s.symbols('p z', positive=True)
assert s.simplify(s.integrate(p**3*s.exp(-p*p-z*z),(p,0,s.oo))
                  -s.exp(-z*z)/2) == 0
assert s.simplify(s.integrate(p*s.exp(-p*p-z*z),(p,0,s.oo))
                  -s.exp(-z*z)/2) == 0

# Squared argument F(u)=exp(-sqrt(u)): coefficients exact in constant mass.
x,y = s.symbols('x y', positive=True)
A1 = 2*s.exp(-x)*(x+1)
A2 = 4*s.exp(-x)*(x*x+3*x+3)
assert s.simplify(s.integrate(2*y*s.exp(-y),(y,x,s.oo))-A1) == 0
assert s.simplify(s.integrate(2*y*(y*y-x*x)*s.exp(-y),(y,x,s.oo))-A2) == 0
assert s.simplify(s.diff(A1,x)+2*x*s.exp(-x)) == 0
assert s.simplify(s.diff(A2,x)+4*x*(x+1)*s.exp(-x)) == 0

def p1(z): return 2*mp.exp(-z)*(1+z)
def p2(z): return 4*mp.exp(-z)*(z*z+3*z+3)
# Diagnostic only: freely chosen reference spectra, NOT a TFPT candidate.
b = mp.findroot(lambda z:2*p2(z)-p2(0)-p2(4),(2,3))
d2 = p2(0)+p2(4)-2*p2(b)
d1 = p1(0)+p1(4)-2*p1(b)
assert abs(d2)<mp.mpf('1e-60') and d1>0
# Physical four-dimensional radial integrals independently reproduce A2/2.
for z in (mp.mpf(0),mp.mpf(1),mp.mpf(4)):
    direct=mp.quad(lambda p:p**3*mp.exp(-mp.sqrt(p*p+z*z)),[0,mp.inf])
    assert abs(2*direct-p2(z))<mp.mpf('1e-55')

# An explicitly dated flat LambdaCDM benchmark; no covariance-based significance.
Mpc = mp.mpf('3.0856775814913673e22')
H0 = mp.mpf('67.4')*1000/Mpc
OmL = mp.mpf('0.685')
rho_bench = 3*OmL*H0**2*c**2/(8*pi*G)
u_bench = 64*pi**2*G**2*hb*rho_bench/c**7
I = rho*hb**3/(me**4*c**5)
assert abs((8*pi)**2*alphaG**2*I/u-1)<mp.mpf('1e-60')
assert abs(SdS/(32*pi**4*mp.exp(2*ainv))-1)<mp.mpf('1e-60')

def st(v):return mp.nstr(v,28)
out={
 'scope':'Conditional source-class analysis; no fundamental TFPT closure, no ledger promotion.',
 'constants_sources':{'SI':'https://www.bipm.org/en/measurement-units/si-defining-constants',
 'CODATA2022':'https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
 'dated_cosmology_benchmark':'https://arxiv.org/abs/1807.06209'},
 'dimensional_rank':dim.rank(),'independent_dimensionless_invariants':3,
 'alpha_inverse_tfpt_input':st(ainv),'alpha_inverse_CODATA2022':'137.035999177 +/- 0.000000021',
 'alpha_CODATA_marginal_sigma_difference':st((ainv-mp.mpf('137.035999177'))/mp.mpf('0.000000021')),
 'alphaG_e':st(alphaG),'uLambda_tfpt':st(u),'rhoLambda_J_m3_conditional_on_measured_G':st(rho),
 'rhoLambda_electron_units_conditional_on_measured_G':st(I),
 'Lambda_geometry_m_minus2':st(lam),'deSitter_entropy_in_kB':st(SdS),
 'deSitter_entropy_scope':'Einstein de Sitter horizon for constant positive Lambda; downstream rewrite, not independent evidence.',
 'benchmark_inputs':{'H0_km_s_Mpc':'67.4','OmegaLambda':'0.685'},
 'uLambda_dated_benchmark':st(u_bench),'relative_difference_to_dated_benchmark':st(u/u_bench-1),
 'heat_equal_rank_bound':{'N':96,'m0':1,'lower_bound':st(144*pi**2/96),
 'lower_bound_div_tfpt_target':st(144*pi**2/(96*u)),
 'required_m0_at_N96_at_least':st(144*pi**2/(96*u)),
 'symbolic_ratio':str(ratio),
 'premises':['Ordinary 4D spin Dirac product, same metric and trace for bound reference',
 'Spacetime-constant self-adjoint internal M and Mref, same finite rank N',
 'Single heat profile F(u)=m0 exp(-u) in squared argument',
 'Vacuum and Einstein bulk coefficients from this source alone, no extra contributions',
 'Curvature expansion near flat space; exact dependence on all constant internal masses'],
 'proof':'T=Tr exp(-M^2/chi^2)-Tr exp(-Mref^2/chi^2); T<=N. Positive Einstein coefficient requires T>0. V/Mbar^4=144pi^2/(m0 T)>=144pi^2/(m0 N).'},
 'poisson_relative_escape_control':{'physical_TFPT_candidate':False,'rank':2,
 'mass_over_chi':[0,4],'reference_mass_over_chi':[st(b),st(b)],
 'vacuum_coefficient_difference':st(d2),'Einstein_coefficient_difference':st(d1),
 'scope':'Numerical witness against extending the heat obstruction to all relative profiles; existence follows by strict monotonicity and intermediate value theorem. Freely chosen spectra cannot select the physical reference.'},
 'verification':'Dimension rank and basis exact; heat identity exact; Poisson integrals and derivatives symbolic; direct radial quadrature at 0,1,4; dimensionless identities checked at 70 digits.',
}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
