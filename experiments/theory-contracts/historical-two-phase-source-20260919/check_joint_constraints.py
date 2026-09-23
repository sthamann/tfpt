"""Scoped joint-source consistency calculation; no TFPT ledger promotion.

The symbolic statements are exact. Cosmological numbers are illustrative
Planck-2018 base-LCDM central inputs, NOT a new observational fit.
"""
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
checks = {}
def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)

# A necessary lower bound for a single canonical massive mode with two endpoints.
x, y, m, d, g, z, lam, kap, mu, v, S = sp.symbols(
    'x y m d g z lam kap mu v S', real=True)
check('endpoint_energy_identity', sp.expand(x*x+y*y-(x-y)**2/2-(x+y)**2/2)==0)
check('torsion_square_completion', sp.simplify(
    -3*mu**2*S**2/(4*kap**2)+lam*mu**2*v*S/2
    -(-3*mu**2*(S-lam*kap**2*v/3)**2/(4*kap**2)
      +lam**2*kap**2*mu**2*v**2/12))==0)

# A fixed-volume local equation and normalized equal-source SK functional
# cannot select a cosmological volume counterterm C: its mixed +/- response remains.
C, Vp, Vm = sp.symbols('C Vp Vm', real=True)
deltaW = -C*(Vp-Vm)
check('sk_diagonal_blind', deltaW.subs(Vp,Vm)==0)
check('sk_metric_response_not_blind', sp.diff(deltaW,Vp)==-C)

# In a local scalar reading, preserving the alpha root is not enough to
# preserve the metric equation off shell.
u, U, Up = sp.symbols('u U Up', real=True)
check('volume_alpha_reciprocity', sp.diff(sp.exp(4*u)*Up,u)==4*sp.exp(4*u)*Up)

c3 = 1/(8*mp.pi)
phi = 1/(6*mp.pi) + 48*c3**4
beta = phi/(4*mp.pi)
Mbar = mp.mpf('2.435e18')
fQCD = c3**mp.mpf('3.5')*Mbar/128
# 5.70 micro-eV at f=1e12 GeV: m*f=5.70e-3 GeV^2.
mf = mp.mpf('5.70e-3')
mass = mf/fQCD
chi = mf**2
g0 = -1/(2*mp.pi)
gphys_r1 = g0/fQCD
hbar = mp.mpf('6.582119569e-25')  # GeV s
Mpc_km = mp.mpf('3.0856775814913673e19')
H0 = mp.mpf('67.4')/Mpc_km*hbar
rho_crit = 3*Mbar**2*H0**2
h = mp.mpf('.674')
omega_c = mp.mpf('.120')/h**2
zrec = mp.mpf('1100') # illustrative recombination epoch, deliberately rounded
rho_cosmic_now = omega_c*rho_crit
rho_rec = rho_cosmic_now*(1+zrec)**3
# Generous observer endpoint: chosen local halo benchmark, not a measured input.
hbarc = mp.mpf('1.973269804e-14')  # GeV cm
rho_halo = mp.mpf('.4')*hbarc**3

theta_rec_harm = mp.sqrt(2*rho_rec/chi)
theta_now_harm = mp.sqrt(2*rho_halo/chi)
theta_rec_cos = 2*mp.asin(mp.sqrt(rho_rec/(2*chi)))
theta_now_cos = 2*mp.asin(mp.sqrt(rho_halo/(2*chi)))
beta_max = abs(g0)*(theta_rec_cos+theta_now_cos)/2
r_max = beta_max/beta
E_min_harm = chi*phi**2/8
E_min_cos = chi*(1-mp.cos(phi/2))
check('cosine_harmonic_agree_at_allowed_amplitude',
      abs(theta_rec_cos/theta_rec_harm-1)<mp.mpf('1e-28'))
check('required_phase_is_small_but_energetically_excluded',
      phi<mp.mpf('.1') and E_min_cos/rho_rec>mp.mpf('1e28'))
check('needed_rotation_exceeds_amplitude_bound', beta/beta_max>mp.mpf('1e14'))
check('cosine_correction_below_one_per_mille', abs(E_min_cos/E_min_harm-1)<mp.mpf('.001'))

# The same-field branch predicts a high oscillation frequency; no arbitrary
# choice of phase removes the endpoint energy bound.
frequency = mass/(2*mp.pi*hbar)
alpha = mp.mpf(1)/mp.mpf('137.0359992168407')
# If the photon and QCD compact-phase normalizations differ by r=f_det/f_QCD,
# g_phys=g0/(r*f_QCD); a field-coordinate rescaling alone does not change r.
Cgamma_needed = 1/(alpha*r_max)

# Necessary two-direction criterion for a QCD-flat but photon-active mode.
# This symbolic example checks the criterion; it is NOT a sourced TFPT model.
n1,n2,c1,c2=sp.symbols('n1 n2 c1 c2',real=True)
n=sp.Matrix([n1,n2]); w=sp.Matrix([-n2,n1]); c=sp.Matrix([c1,c2])
check('qcd_null_direction', (n.T*w)[0]==0)
check('photon_active_iff_nonparallel', (c.T*w)[0]==n1*c2-n2*c1)

# General two-phase kinetic mixing does not lift a QCD-null direction.
# Symbols k11>0, detK>0 are the positivity premises, not derived TFPT values.
k11,k12,k22,chiS,gS=sp.symbols('k11 k12 k22 chi g0',real=True)
K=sp.Matrix([[k11,k12],[k12,k22]])
Ki=K.inv(); N=sp.Matrix([0,1]); cph=sp.Matrix([gS,0])
D=(N.T*Ki*N)[0]
B=(cph.T*Ki*N)[0]
Cnorm=(cph.T*Ki*cph)[0]
light_coupling_squared=sp.factor(Cnorm-B**2/D)
heavy_coupling_squared=sp.factor(B**2/D)
mass_operator=Ki*(chiS*N*N.T)
check('qcd_rank_one_for_any_positive_kinetic_matrix', mass_operator.det()==0)
check('qcd_heavy_mass', sp.simplify(sp.trace(mass_operator)-chiS*k11/(k11*k22-k12**2))==0)
check('kinetic_mixing_preserves_light_photon_coupling', sp.simplify(light_coupling_squared-gS**2/k11)==0)
check('massive_tree_photon_coupling_requires_projection',
      sp.simplify(heavy_coupling_squared-gS**2*k12**2/(k11*(k11*k22-k12**2)))==0)
check('unmixed_heavy_has_no_imported_topological_photon_vertex', heavy_coupling_squared.subs(k12,0)==0)

# Exact energy balance for the historical explicitly moving potential minimum.
t=sp.symbols('t',real=True)
theta=sp.Function('theta')(t); driver=sp.Function('s')(t)
ft,L4,phiS,H=sp.symbols('f_t Lambda4 phi0 H',positive=True)
V=L4*(1-sp.cos(theta-phiS*driver))
rho=ft**2*sp.diff(theta,t)**2/2+V
eom_dd=-3*H*sp.diff(theta,t)-sp.diff(V,theta)/ft**2
balance=sp.simplify((sp.diff(rho,t)+3*H*ft**2*sp.diff(theta,t)**2).subs(sp.diff(theta,t,2),eom_dd))
expected=-L4*phiS*sp.sin(theta-phiS*driver)*sp.diff(driver,t)
check('moving_minimum_needs_energy_source', sp.simplify(balance-expected)==0)

numeric = dict(c3=c3,phi0=phi,beta_target_rad=beta,beta_target_deg=mp.degrees(beta),
    f_QCD_GeV=fQCD,mass_GeV=mass,mass_micro_eV=mass*mp.mpf('1e15'),
    chi_GeV4=chi,g_phys_r1_GeV_inverse=gphys_r1,
    rho_critical_now_GeV4=rho_crit,rho_cdm_recomb_GeV4=rho_rec,
    rho_observer_halo_benchmark_GeV4=rho_halo,
    theta_recomb_bound=theta_rec_cos,theta_observer_bound=theta_now_cos,
    beta_max_rad_r1=beta_max,beta_max_deg_r1=mp.degrees(beta_max),
    rotation_shortfall=beta/beta_max,minimum_endpoint_energy_GeV4=E_min_cos,
    energy_excess_over_recomb=E_min_cos/rho_rec,
    r_max_for_target=r_max,f_det_max_GeV=r_max*fQCD,
    Cgamma_min_if_standard_QCD_convention=Cgamma_needed,
    oscillation_frequency_Hz=frequency)
result = dict(status='PASS', verdict='PARTIAL',
    excluded='Same-well local QCD phase with r=1 and declared mass/energy bounds supplies beta=phi0/(4pi)',
    not_excluded=['TFPT compiler','independently derived boundary holonomy',
      'additional photon-active QCD-flat mode','changed potential or coupling proved from source'],
    assumptions=['one canonical scalar','QCD/cosine same minimum branch',
      'no cancellation of its positive excitation energy','g_phys=g0/(r*f_QCD)',
      'energy at emission <= illustrative full CDM density','observer <= chosen halo benchmark'],
    historical_correction='v2.7 and v2.8 already explicitly distinguish atop from aQCD; this bound validates that distinction, not a refutation of the two-field TFPT branch',
    symbolic_checks_and_numeric_controls=checks,
    two_phase_results={'premises':'K positive definite; only QCD rank-one mass term; tree-level photon vector (g0,0)',
      'light_photon_coupling_squared':str(light_coupling_squared),
      'heavy_photon_coupling_squared':str(heavy_coupling_squared),
      'heavy_mass_squared':str(sp.factor(chiS*D)),
      'external_driver_energy_source':str(expected),
      'scope':'necessary structure and conditional quadratic theorem; source selection, other potentials, QCD meson matching and cosmological state not derived'},
    numeric={k:mp.nstr(val,35) for k,val in numeric.items()})
dest=Path(__file__).resolve().parent/'joint_constraints.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
