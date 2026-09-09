"""Virtual corrections and a physical local-energy obstruction (NON-RH).

Exact rational checks support the conditional arguments in VIRTUAL_READOUT.md
and LOCAL_ENERGY.md. They do not certify a physical T1-T8 completion.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from itertools import product
from pathlib import Path

import sympy as s

PINS = {
    "checker.py": "03735c0ef740b9badcabe0d8d7ce3652c527086ee0464d36009ed38b58e7a5e1",
    "GEOMETRIC_CONTROL.md": "f941b6709e831a376b235654c72d0bad1ec4c1a891211f120563e254a58f6e4e",
    "validation.json": "a1cc920f3b0f52973a812b8a83fcd5100d3dcb796f13216072f7f62021668b30",
}


def require(condition, name):
    if not bool(condition):
        raise ValueError(name)


def inherited(root):
    directory = root / "experiments/theory-contracts/projector-locality-round31"
    for name, expected in PINS.items():
        path = directory/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "Round31 source pin: " + name)
    spec = importlib.util.spec_from_file_location("round31_readout_input", directory/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.inherited(root)


def ad(A, S):
    """Convention for exp(-S) A exp(S): ad_S(A) = [A,S]."""
    return A*S-S*A


def psd2(A):
    return A == A.H and A[0, 0] >= 0 and A[1, 1] >= 0 and A.det() >= 0


def rational_row_bound(A):
    """Rational upper bound on absolute row sum, also for Gaussian rationals.

Bounds the operator norm when the matrix is Hermitian or anti-Hermitian,
because then its absolute row and column norm bounds coincide.
"""
    return max(sum(abs(s.re(x))+abs(s.im(x)) for x in A.row(i))
               for i in range(A.rows))


def matrix_record(A):
    return [[str(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]


def sw_bounds(c, gap):
    c, gap = s.Rational(c), s.Rational(gap)
    require(c > 0 and gap > 0 and 2*c < gap, "ordered, small-coupling SW domain")
    b = c/gap
    return b, 2*c*b*b/(1-2*b), (2*b)**3/(6*(1-2*b))


def virtual_cell(r30):
    z, _, V, h, _ = r30.fixture()
    kappa = s.Rational(1, 100)
    V0 = V.subs(z, 1)
    Ny = s.diag(0, 1, 0, 1)
    H = V0.T*(h.subs(z, 1)+kappa*Ny/2)*V0
    L, D, C = H[:2, :2], H[2:, 2:], H[2:, :2]
    H0 = s.diag(L, D)
    B = H-H0
    gap, c = s.Rational(13, 12), 3*kappa/20
    require(psd2(D-s.Rational(31, 12)*s.eye(2)), "physical high block lower bound")
    require(psd2(s.Rational(3, 2)*s.eye(2)-L), "physical low block upper bound")
    require(C.T*C == c*c*s.eye(2), "exact physical Gauss coupling norm")

    variables = s.symbols("x0:4")
    symbolic = s.Matrix(2, 2, variables)
    solution = s.linsolve(list(D*symbolic-symbolic*L-C), variables)
    require(len(solution) == 1, "unique Sylvester solution")
    X = s.Matrix(2, 2, next(iter(solution)))
    S = s.zeros(4)
    S[:2, 2:], S[2:, :2] = X.T, -X
    require(S.H == -S and ad(H0, S) == -B, "anti-Hermitian cancelling generator")
    effective = H0+ad(B, S)/2
    require(effective == effective.H and effective[:2, 2:] == s.zeros(2),
            "virtual correction is Hermitian and block diagonal")
    Leff = effective[:2, :2]
    require(Leff == L-(C.T*X+X.T*C)/2 and Leff != L, "virtual term retained")
    b, errH, errO = sw_bounds(c, gap)
    require(psd2(b*b*s.eye(2)-X.T*X), "independent rational Sylvester norm enclosure")

    observable = V0.T*Ny*V0
    expanded = observable+ad(observable, S)+ad(ad(observable, S), S)/2
    Oeff = expanded[:2, :2]
    require(Oeff == Oeff.H and Oeff != observable[:2, :2], "readout is dressed too")
    # Source at zero time already detects inconsistent preparation/readout.
    shift = Oeff-observable[:2, :2]
    require(abs(shift[0, 0])-errO > 1000*(2*errH+errO),
            "bare readout cannot inherit encoded-state error guarantee")
    return {"H": H, "L": L, "D": D, "C": C, "B": B, "H0": H0,
            "X": X, "S": S, "Heff": effective, "Leff": Leff,
            "O": observable, "Oeff": Oeff, "V0": V0,
            "c": c, "gap": gap, "b": b, "errH": errH, "errO": errO}


def unitary_polynomial(A, degree):
    """Exact Taylor polynomial and integral-remainder norm enclosure.

For anti-Hermitian A, the exponential in the integral has norm one.
No floating diagonalization or exponential estimate is used.
"""
    require(A.H == -A, "Taylor certificate requires anti-Hermitian input")
    require(isinstance(degree, int) and degree >= 0, "nonnegative Taylor degree")
    term, result = s.eye(A.rows), s.eye(A.rows)
    for k in range(1, degree+1):
        term = term*A/k
        result += term
    bound = rational_row_bound(A)
    remainder = bound**(degree+1)/s.factorial(degree+1)
    return result, remainder


def real_time_certificate(cell):
    """Independent t=1 comparison for ALL initial vectors in encoded low cell."""
    J = s.eye(4)[:, :2]
    PS, tailS = unitary_polynomial(cell["S"], 8)
    PH, tailH = unitary_polynomial(-s.I*cell["H"], 36)
    PL, tailL = unitary_polynomial(-s.I*cell["Leff"], 36)
    full = PH*PS*J
    difference = (full.H*cell["O"]*full-PL.H*cell["Oeff"]*PL).applyfunc(s.expand)
    require(difference == difference.H, "readout comparison is Hermitian")
    delta = tailS+tailH*(1+tailS)
    tail = delta*(2+delta)+tailL*(2+tailL)*(1+cell["errO"])
    upper = rational_row_bound(difference)+tail
    analytic = 2*cell["errH"]+cell["errO"]
    require(upper < analytic, "independent all-low-state t=1 rational readout certificate")
    # Store short outward rational enclosures; no giant Taylor fractions required.
    scale = 10**15
    rounded_upper = s.ceiling(upper*scale)/scale
    require(upper <= rounded_upper < analytic, "outward rounded rational certificate")
    require(tail < s.Rational(1, 10**18), "Taylor arithmetic error negligible and certified")
    return {"time": "1", "preparation": "V0 exp(S) J psi for any normalized low psi",
            "observable": "gauge-invariant site occupation Ny (operator norm 1)",
            "uniform_low_state_readout_error_upper": str(rounded_upper),
            "Taylor_error_upper": "1/1000000000000000000",
            "Taylor_degrees_S_H_Leff": [8, 36, 36],
            "method": "exact rational matrix polynomials plus unitary integral remainders"}


def spectral_certificate(cell):
    intervals = lambda A: s.Poly(A.charpoly().as_expr()).intervals(eps=s.Rational(1, 10**14))
    physical, effective = intervals(cell["H"]), intervals(cell["Leff"])
    require(len(physical) == 4 and len(effective) == 2, "all physical roots isolated")
    result = []
    for ((a, b), multiplicity), ((c, d), eff_multiplicity) in zip(physical[:2], effective):
        require(multiplicity == eff_multiplicity == 1, "simple ordered physical low roots")
        error = max(abs(a-d), abs(b-c))
        require(error < cell["errH"], "independent Sturm virtual-energy certificate")
        result.append({"physical_interval": [str(a), str(b)],
                       "effective_interval": [str(c), str(d)],
                       "absolute_error_upper": str(s.ceiling(error*10**15)/10**15)})
    return result


def resonant_cell(n):
    require(isinstance(n, int) and n >= 400, "integer physical cycle flux n>=400")
    kappa, hop, beta, eta = map(s.Rational, ("1/100", "1/4", "1/4", "1/2"))
    c = eta*hop
    D = kappa*(s.Integer(n)-s.Rational(1, 2))
    M = D+beta*hop**2
    # Basis low_x, low_y, high_x, high_y; exact physical one-fermion sector.
    A = s.Matrix([[0, hop], [hop, 0]])
    h = (A+beta*A*A).row_join(eta*A).col_join((eta*A).row_join(M*s.eye(2)))
    E1, E2 = s.diag(-n, 1-n, -n, 1-n), n*s.eye(4)
    Nx, Ny = s.diag(1, 0, 1, 0), s.diag(0, 1, 0, 1)
    require(E1+E2+Nx-s.eye(4) == s.zeros(4), "Gauss x with background qx=1")
    require(-E1-E2+Ny == s.zeros(4), "Gauss y with background qy=0")
    electric = kappa*(E1**2+E2**2)/2
    energy = kappa*n*n+beta*hop**2
    H = h+electric-energy*s.eye(4)
    expected = s.Matrix([[0, hop, 0, c], [hop, -D, c, 0],
                         [0, c, D, 0], [c, 0, 0, 0]])
    require(H == expected, "actual Gauss rotor reduction has exact resonance")
    fast = H.extract([1, 2], [1, 2])
    require(fast*fast == (D*D+c*c)*s.eye(2), "off-resonant inverse norm <=1/D")
    coupling = H.extract([0, 3], [1, 2])
    require(coupling*coupling.T == s.diag(hop*hop, 0), "resonant-fast coupling norm")
    Tmax = s.Rational(88, 7)  # T=4*pi < 88/7, from pi<22/7.
    numerator = hop**2*(2*Tmax+(c+hop)*Tmax**2/2)
    require(numerator == s.Rational(671, 196) and numerator < D,
            "positive resonant-amplitude lower bound")
    probability = (1-numerator/D)**2
    B0 = hop+beta*hop**2
    qdistance = c/(M-B0)
    dressed_local = probability-2*qdistance
    strict_low_local = probability-6*qdistance
    require(M > B0 and beta-eta**2/M > 0, "inherited signed-wall fiber regime")
    return {"n": n, "D": D, "M": M, "H": H, "E1": E1, "E2": E2,
            "energy": energy, "sites": n*n, "density": energy/(n*n),
            "probability_lower": probability, "dressed_local_lower": dressed_local,
            "strict_low_initial_dressed_local_lower": strict_low_local,
            "strict_low_initial_energy_density_upper": kappa+(M+c)/(n*n),
            "projector_distance_upper": qdistance, "Nhigh_density_upper": s.Rational(1, n*n)}


def periodic_translation_certificate(sides):
    require(len(sides) == 3 and all(isinstance(v, int) and v >= 3 for v in sides),
            "periodic cubic sides >=3 avoid doubled two-site bonds")
    sites = list(product(*(range(v) for v in sides)))
    index = {site: i for i, site in enumerate(sites)}
    edges = []
    for i, site in enumerate(sites):
        for axis in range(3):
            target = list(site)
            target[axis] = (target[axis]+1) % sides[axis]
            edges.append((i, index[tuple(target)], axis))
    lookup = {edge: j for j, edge in enumerate(edges)}
    n = len(sites)
    A = s.zeros(n)
    for i, j, _ in edges:
        A[i, j] += s.Rational(1, 12)
        A[j, i] += s.Rational(1, 12)
    translations = []
    for direction in range(3):
        perm = []
        for site in sites:
            target = list(site)
            target[direction] = (target[direction]+1) % sides[direction]
            perm.append(index[tuple(target)])
        edge_perm = [lookup[(perm[i], perm[j], axis)] for i, j, axis in edges]
        require(sorted(perm) == list(range(n)) and sorted(edge_perm) == list(range(len(edges))),
                "translation bijects vertices and oriented rotor variables, for arbitrary link U")
        T = s.zeros(n)
        for i, j in enumerate(perm):
            T[j, i] = 1
        require(T*A*T.T == A, "homogeneous hopping translation covariance")
        translations.append(T)
    for T in translations:
        for U in translations:
            require(T*U == U*T, "commuting coordinate translations")
    require(len(edges) == 3*n and s.trace(A*A) == s.Rational(n, 24),
            "periodic filled-state cost has the inherited cubic bound")
    require(rational_row_bound(A) == s.Rational(1, 2) and s.trace(A) == 0,
            "uniform periodic hopping norm and zero trace")
    return {"sides": list(sides), "sites": n, "electric_links": len(edges),
            "vertex_and_oriented_link_permutations_checked": 3,
            "A_squared_trace": str(s.trace(A*A)),
            "scope": "Finite witnesses for the general translation argument, not a flux truncation"}


def uniform_local_population(M, kappa=s.Rational(1, 100)):
    M, kappa = s.Rational(M), s.Rational(kappa)
    require(M >= 4 and kappa > 0, "inherited filled-state regime")
    delta = M-s.Rational(9, 16)
    energy = s.Rational(1, 96)+11*kappa/(256*delta**2)
    ebar = energy+s.Rational(1, 2)
    rate2 = (s.Rational(3, 8)/delta)**2*6*kappa*ebar
    return {"M": str(M), "total_energy_per_site_upper": str(energy),
            "local_high_readout_static_upper": str(ebar/M),
            "local_high_readout_rate_upper_squared": str(rate2),
            "identity": "expectation(dGamma(Q Pi_x Q)) = expectation(N_high)/N for every x,t",
            "initial_state": "translation-invariant density matrix of the filled-low rotated Haar state",
            "geometry": "homogeneous periodic cubic graph, all sides >=3, hopping 1/12, V_mag=0, q_x=1",
            "not_all_observable_effective_dynamics": True}


def run(root):
    r30 = inherited(root)
    cell = virtual_cell(r30)
    resonances = [resonant_cell(n) for n in (3200, 6400, 12800)]
    return {"status": "PASS", "verdict": "CONDITIONAL_DRESSED_READOUT_AND_LOCAL_ENERGY_OBSTRUCTION",
            "inherited_pins": PINS,
            "virtual_physical_cell": {
                "kappa": "1/100", "gap_lower": str(cell["gap"]), "coupling_norm": str(cell["c"]),
                "generator_norm_upper": str(cell["b"]),
                "Sylvester_X": matrix_record(cell["X"]),
                "low_Hamiltonian_with_virtual_term": matrix_record(cell["Leff"]),
                "site_readout_with_virtual_terms": matrix_record(cell["Oeff"]),
                "Hamiltonian_remainder_norm_upper": str(cell["errH"]),
                "norm_one_readout_remainder_upper": str(cell["errO"]),
                "encoded_readout_error_bound": "2*Hamiltonian_remainder*abs(time)+readout_remainder",
                "encoded_readout_t1_upper": str(2*cell["errH"]+cell["errO"]),
                "bare_initial_state_has_same_low_only_guarantee": False,
                "bare_state_safe_comparison": "retain both transformed blocks and all transformed initial data",
                "bare_readout_t0_error_lower": str(abs((cell["Oeff"]-cell["O"][:2, :2])[0, 0])-cell["errO"])},
            "independent_real_time_certificate": real_time_certificate(cell),
            "independent_low_energy_Sturm_certificates": spectral_certificate(cell),
            "resonant_physical_cycle_family": [{
                key: (value if isinstance(value, int) else str(value))
                for key, value in row.items() if key not in ("H", "E1", "E2")}
                for row in resonances],
            "resonant_time": "4*pi (fixed model units)",
            "positive_periodic_translation_witnesses": [periodic_translation_certificate(v) for v in ((3, 3, 3), (3, 3, 4))],
            "positive_homogeneous_local_population": [uniform_local_population(M) for M in (4, 40, 400)],
            "padding_scope": "Connected gauge graph, zero matter hopping on spectator links; not homogeneous cubic matter lattice",
            "counterexample_claim": "Global average energy and a growing fiber gap alone do not uniformly suppress every local high readout",
            "Round31_filled_Haar_cubic_state_refuted": False,
            "physical_gates_closed": [],
            "scope": "Exact four-dimensional Gauss cells and conditional analytic bounds. No general connected-lattice EFT, chiral measure, continuum, selected vacuum, graviton, TOE or RH proof."}


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "VIRTUAL_READOUT.md", "LOCAL_ENERGY.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = payload(args.repo)
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
