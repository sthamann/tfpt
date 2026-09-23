"""Exact rational certificate for a CONDITIONAL two-native-bank transfer.

The analytic proof of comparison, spectral rotation and Duhamel control is
in RESULTS.md. These tests do not synthesize the link or a state preparer.
No floating-point eigenvalue is used to prove a bound.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
checks = []


def need(ok, label):
    if not ok:
        raise RuntimeError(label)
    checks.append(label)


def box(value):
    return {'exact': str(value), 'decimal_for_reading': float(value)}


def ldl(number, first, shift):
    bs = list(range(first, number//2+1))
    need(bool(bs), 'comparison block nonempty N=' + str(number))
    pivots = [F(bs[0])-shift]
    for b in bs[:-1]:
        off2 = F((b+1)*15*(number-2*b-number % 2), 800)
        need(off2 >= 0, 'nonnegative squared coupling N=' + str(number) + ' b=' + str(b))
        need(pivots[-1] > 0, 'strictly positive pivot N=' + str(number) + ' b=' + str(b))
        pivots.append(F(b+1)-shift-off2/pivots[-1])
    need(pivots[-1] > 0, 'final positive pivot N=' + str(number))
    return {'N': number, 'boson_min': first, 'boson_max': bs[-1],
            'energy_lower_bound_Delta': str(shift),
            'pivots': list(map(str, pivots))}


native = json.loads((HERE / 'sources/native_pole_consolidation.json').read_text())
pole = json.loads((HERE / 'sources/native_external_pole.json').read_text())
need(native['status'] == 'PASS', 'pinned consolidated native certificate is PASS')
need(pole['isolated_native_removal_pole']['native_N63_low_level_degeneracy'] == 64,
     'one isolated dual64 eigenlevel, not sixty-four unrelated pole energies')
Zlo, Zhi = map(F, native['pole_weight_of_full_CAR_measure']['strict_interval'])
need(Zlo == F(40912436089, 46487375000), 'source lower residue copied exactly')
need(Zhi == F(15578577, 16000000), 'source upper residue copied exactly')

# Low charge numbers, including the vacuum, are bounded without enumeration.
# E_N >= -(N-eta)/4*(sqrt(23/20)-1), with N-eta<=62.
elow = F(-1121899, 1000000)
need(F(23, 20) < (1-2*elow/31)**2,
     'rational outward comparison for all N<=62')

# All high charge numbers permitted by total charge 127, not just N65.
high = [ldl(n, max(0, (n-63)//2), F(-4, 5)) for n in range(65, 128)]
need(len(high) == 63, 'all sixty-three high-charge sectors exhausted')
central = [ldl(63, 1, F(-3, 4)), ldl(64, 1, F(-3, 4))]

E0hi = F(-1129636, 1000000)
Ehhi = F(-1095812, 1000000)
tau = F(1, 10**8)
kappa = F(1, 10**10)
T = F(169500000)
external_floor = elow-F(4, 5)
external_gap = external_floor-(E0hi+Ehhi)-kappa/2
hole_excited_gap = F(-3, 4)-Ehhi-kappa/2
ground_excited_gap = F(-3, 4)-E0hi-kappa/2
delta = min(external_gap, hole_excited_gap, ground_excited_gap)
need(delta == F(303549, 1000000)-kappa/2, 'full charge and excitation complement gap')

# Gauss constraints eliminate the rotor coordinate on this one-edge tree.
for nx in range(128):
    ny = 127-nx
    flux = 63-nx
    need(nx-63+flux == ny-64-flux == 0,
         'full physical sector Gauss law N_x=' + str(nx))
    if nx < 127:
        need((nx+1)-63+(flux-1) == (ny-1)-64-(flux-1) == 0,
             'unit transfer preserves Gauss at N_x=' + str(nx))
need(63-63 == 0 and 63-64 == -1, 'low one-hole orientations have flux zero and minus one')
need(63+64 != 64+64, 'one-hole sector needs charged background or external reference')

# Algebraic norm proof: each mode's Hermitian exchange is a unitary flux
# shift between |10> and |01>, zero on |00>,|11>. Thus each has norm |tau|.
v = 64*tau
need(2*v < delta, 'perturbed low cluster remains isolated in the full physical sector')
rotation = v/(delta-2*v)
leak_amplitude = 2*rotation
leak_probability = leak_amplitude**2
eta = T*v*leak_amplitude

# Uniform Rabi bound for every unknown residue in the strict source interval.
# Rational classical pi bounds 333/106 < pi < 355/113 are sufficient.
def atan_bounds(x):
    terms = [(-1)**k*x**(2*k+1)/F(2*k+1) for k in range(21)]
    return sum(terms[:20], F(0)), sum(terms, F(0))


a_lo, a_hi = atan_bounds(F(1, 5))
b_lo, b_hi = atan_bounds(F(1, 239))
tan_four_a = (4*F(1, 5)-4*F(1, 5)**3)/(1-6*F(1, 5)**2+F(1, 5)**4)
need((tan_four_a-F(1, 239))/(1+tan_four_a*F(1, 239)) == 1,
     'Machin tangent identity; its angle is in the principal first quadrant')
pi_lo, pi_hi = F(333, 106), F(355, 113)
need(pi_lo < 4*(4*a_lo-b_hi) < 4*(4*a_hi-b_lo) < pi_hi,
     'rational alternating-series certificates for both pi bounds')
theta_lo = T*tau*Zlo
theta_hi = T*(tau*Zhi+(kappa/4)**2/(2*tau*Zlo))
angle_error = F(2, 25)
need(theta_lo > pi_hi/2-angle_error, 'uniform angle lower bound within 0.08 of pi/2')
need(theta_hi < pi_lo/2+angle_error, 'uniform angle upper bound within 0.08 of pi/2')
need(0 < theta_lo < theta_hi, 'positive ordered angle enclosure')
prefactor_lo = 1-(kappa/(4*tau*Zlo))**2
need(prefactor_lo > 0, 'detuning bound gives a positive transition prefactor')
p_projected_lo = prefactor_lo*(1-angle_error**2)
p_full_lo = p_projected_lo-2*eta
need(p_full_lo > F(992, 1000), 'complete conditional two-bank transfer probability exceeds 99.2 percent')
need(leak_probability < F(18, 10**12), 'all-time out-of-band probability below 1.8e-11')
need(p_full_lo < p_projected_lo < 1, 'full evolution bound distinct from projected Rabi result')

# No initial energy filter: f_r Omega / sqrt(nu). The low-pole fraction is
# w=Z/nu >= Zlo/nu_hi and nu_hi=Zhi (the latter is an upper bound, not Z).
nu_hi = Zhi
wlo = Zlo/nu_hi
unfiltered_lo = wlo*p_full_lo-leak_amplitude
need(0 < wlo < 1, 'original unfiltered removal has controlled low-pole fraction')
need(wlo*p_full_lo > leak_amplitude**2, 'reverse triangle bound positive before squaring')
need(unfiltered_lo > F(897, 1000), 'unfiltered original removal reaches target low-pole bank with probability above 89.7 percent')
need(unfiltered_lo < p_full_lo, 'unfiltered removal is not silently replaced by the exact pole state')

# Exact small CAR/flux witness of the link norm and symmetry selection rule.
# This is an independent algebraic control, not the 64-mode evolution itself.
import sympy as s
I = s.eye(2)
a = s.Matrix([[0, 1], [0, 0]])
z = s.diag(1, -1)
fx = s.kronecker_product(a, I)
fy = s.kronecker_product(z, a)
hop = fy.T*fx+fx.T*fy
px = s.kronecker_product(z, I)
py = s.kronecker_product(I, z)
need(hop**2 == s.diag(0, 1, 1, 0), 'single mode exchange norm exactly one after tree Gauss elimination')
need(hop*px == -px*hop and hop*py == -py*hop, 'link reverses both local parities')
need(hop*(px*py) == (px*py)*hop, 'link preserves total fermion parity')
for k in range(1, 9):
    K = s.diag(1, s.Rational(1, 2), s.Rational(1, 3), s.Rational(1, 4))**k
    need(K*px == px*K and K*py == py*K, 'exact parity-preserving branch control length ' + str(k))

# Merely covariant channels need NOT conserve each local parity sector.
K0, K1 = s.diag(1, 0), a
need(K0.T*K0+K1.T*K1 == I, 'reset example is trace preserving')
need(K1*z == -z*K1, 'reset contains an odd Kraus operator')
for i in range(2):
    for j in range(2):
        R = s.zeros(2); R[i, j] = 1
        reset = lambda M: K0*M*K0.T+K1*M*K1.T
        need(reset(z*R*z) == z*reset(R)*z, 'reset is parity covariant on matrix unit')
need(K1*s.Matrix([0, 1]) == s.Matrix([1, 0]),
     'parity covariance alone does not forbid a parity-changing branch')

result = {
    'status': 'PASS', 'checks': len(checks), 'check_labels': checks,
    'proof_class': 'rational certificates plus analytic comparison/minmax/Sylvester/Duhamel proof, not Lean',
    'contract': {'native_banks': 2, 'fermions_per_bank': 64, 'bosons_per_bank': 60,
                 'g_over_Delta': '1/20', 'mu': '0', 'total_charge': 127,
                 'background_charges': [63, 64], 'added_rotor_links': 1,
                 'link_term': 'tau sum_r f_y,r^dagger U f_x,r + h.c.',
                 'tau_over_Delta': str(tau), 'kappa_over_Delta': str(kappa),
                 'time_times_Delta_hbar1': str(T), 'initial_state': 'normalized exact low-pole hole x, native ground y, flux 0'},
    'native_inputs': {'Z_lower': str(Zlo), 'Z_upper': str(Zhi), 'E0_upper_Delta': str(E0hi),
                      'Eh_upper_Delta': str(Ehhi), 'fully_rederived_this_revision': False},
    'comparison_high_sectors': high, 'comparison_central_complements': central,
    'full_gap_Delta': box(delta), 'link_norm_upper_Delta': box(v),
    'all_time_leakage_amplitude_upper': box(leak_amplitude),
    'all_time_leakage_probability_upper': box(leak_probability),
    'projected_amplitude_error_upper_at_T': box(eta),
    'uniform_projected_target_probability_lower_at_T': box(p_projected_lo),
    'full_target_probability_lower_at_T': box(p_full_lo),
    'unfiltered_original_removal': {'initial_state': 'f_x,r Omega_x tensor Omega_y tensor flux 0, divided by sqrt(nu)',
                                   'low_pole_fraction_lower': box(wlo),
                                   'target_low_pole_probability_lower_at_T': box(unfiltered_lo),
                                   'initial_spectral_filter_required': False,
                                   'charged_preparation_instrument_derived': False},
    'angle_interval': [box(theta_lo), box(theta_hi)],
    'conditional_acceptance': 'full one-hole transfer with leakage control within explicitly added two-bank link model',
    'not_proved': ['native derivation of the rotor link, graph, tau or kappa',
                   'native preparation of the charged background or isolated-pole initial state',
                   'relativistic field dictionary or spatial continuum', 'T1-T8', 'RH', 'efficient factoring', 'P versus NP'],
    'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
}
print(json.dumps(result, indent=2) + '\n', end='')
