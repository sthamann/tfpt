"""Exact source audit and charge-closure certificate for the minimal mechanism.

Run with Python, NumPy, SciPy and SymPy. No repository imports or network.
Only frozen inputs are read. All checks survive -OO. This proves algebraic
statements; it does not infer laboratory controls from available matrices.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, factorial
from fractions import Fraction
import argparse
import ast
import contextlib
import io
import itertools
import json
import numpy as np
import sympy as s
from scipy.sparse import csr_matrix

HERE = Path(__file__).resolve().parent
CHECKS = []
W_PIN = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def zero(matrix):
    matrix = matrix.tocsr()
    matrix.eliminate_zeros()
    return matrix.nnz == 0


def assignment_name(node):
    if isinstance(node, ast.Assign):
        return {x.id for x in node.targets if isinstance(x, ast.Name)}
    return set()


def native_constructor():
    """Execute the unchanged constructor through its final Casimir guard.

    Omit only the trailing PINS dictionary, whose optional C3.toarray hash
    would allocate an unnecessary 1.28 GB, and the command-line print block.
    All constructor operations and all constructor guards are retained.
    """
    path = HERE / "inputs/native_source.py"
    tree = ast.parse(path.read_text())
    stop = next(i for i, node in enumerate(tree.body) if "PINS" in assignment_name(node))
    body = tree.body[:stop]
    need(not any(isinstance(x, ast.Assert) for n in body for x in ast.walk(n)),
         "native constructor has no optimization-sensitive assert")
    env = {"__file__": str(path), "__name__": "frozen_native_constructor"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(ast.Module(body=body, type_ignores=[]), str(path), "exec"), env)
    return env, body[-1].end_lineno


def original_clock():
    """Execute original finite construction S0.1--S0.4, no seam physics run.

    Select original helper definitions/constants and the unchanged main
    statements from refs=... through S0.4. Replace only main's wrapper with
    a return of locals; the original four mathematical check calls remain.
    The unrelated original import/firewall and later numerical probes are
    outside this explicitly recorded replay boundary.
    """
    path = HERE / "inputs/source_clock.py"
    tree = ast.parse(path.read_text())
    functions = {"pc", "sig", "polar_shift", "iota_bits", "iota_support",
                 "compose", "perm_order", "cycle_type", "edge_orbits"}
    constants = {"HT", "A_BIT", "FSIG", "LOWIDX", "SIGP", "IOTA_MSG"}
    prelude = [n for n in tree.body if
               (isinstance(n, ast.FunctionDef) and n.name in functions)
               or bool(assignment_name(n) & constants)]
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    start = next(i for i, n in enumerate(main.body) if "refs" in assignment_name(n))
    stop = next(i for i, n in enumerate(main.body) if "Aint_f" in assignment_name(n))
    selected = main.body[start:stop]
    begin_line, end_line = selected[0].lineno, selected[-1].end_lineno
    main.body = selected + [ast.Return(value=ast.Call(func=ast.Name(id="locals", ctx=ast.Load()), args=[], keywords=[]))]
    main.name = "construct_clock"
    calls = []

    def check(name, ok, detail="", kill=None):
        need(ok, "original Clock " + name)
        calls.append(name)

    env = {"np": np, "itertools": itertools, "check": check}
    reduced = ast.fix_missing_locations(ast.Module(body=prelude + [main], type_ignores=[]))
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(reduced)),
         "selected Clock construction has no optimization-sensitive assert")
    exec(compile(reduced, str(path), "exec"), env)
    data = env["construct_clock"]()
    need(len(calls) == 4, "all four selected original Clock mathematical guards replayed")
    return data, [begin_line, end_line]


# Exact Weyl algebra, with at most one commuting fermion-pair tag per product.
# A tag is (dagger, A) and denotes P_A or P_A^dagger. Every product needed
# below has at most one tag, so no CAR product of two composite pairs is used.
# Monomial key = (sorted boson creators, sorted boson annihilators, tag).
UNIT = ((), (), None)


def clean(poly):
    return {k: v for k, v in poly.items() if v}


def add(left, right, scale=1):
    result = defaultdict(int, left)
    for key, value in right.items():
        result[key] += scale * value
    return clean(result)


def mul(left, right):
    result = defaultdict(int)
    for (cl, al, tl), vl in left.items():
        for (cr, ar, tr), vr in right.items():
            if tl is not None and tr is not None:
                raise RuntimeError("pair-pair product is outside this Weyl certificate")
            ca, cc = Counter(al), Counter(cr)
            overlap = sorted(set(ca) & set(cc))
            for ks in product(*(range(min(ca[j], cc[j]) + 1) for j in overlap)):
                factor = 1
                aa, ccc = ca.copy(), cc.copy()
                for j, k in zip(overlap, ks):
                    factor *= comb(ca[j], k) * comb(cc[j], k) * factorial(k)
                    aa[j] -= k
                    ccc[j] -= k
                creation = tuple(sorted(cl + tuple(ccc.elements())))
                annihilation = tuple(sorted(tuple(aa.elements()) + ar))
                result[(creation, annihilation, tl if tl is not None else tr)] += vl * vr * factor
    return clean(result)


def comm(left, right):
    return add(mul(left, right), mul(right, left), -1)


def charge(key):
    creators, annihilators, tag = key
    fermion_charge = 0 if tag is None else (2 if tag[0] else -2)
    return 2 * (len(creators) - len(annihilators)) + fermion_charge


def charge_action(poly):
    return clean({key: charge(key) * value for key, value in poly.items()})


def partial_system(matrix):
    return s.Matrix(2, 2, lambda i, j: sum(matrix[2*i+r, 2*j+r] for r in range(2)))


def native_action(state, source, dagger):
    """Exact original Tplus/Tminus on unnormalized creation monomials.

    State key = (fermion bitmask, sorted occupied boson multiset).
    Boson creation has coefficient one; annihilation has multiplicity n.
    The resulting inner product must therefore include boson factorials.
    """
    W, pairs = source["W"], source["PAIRS"]
    support = [[(pairs[j], int(W[A, j])) for j in np.flatnonzero(W[A])] for A in range(60)]
    out = defaultdict(int)
    for (mask, bosons), coefficient in state.items():
        channels = Counter(bosons) if dagger else {A: 1 for A in range(60)}
        for A, multiplicity in channels.items():
            for pair, value in support[A]:
                acted = source["pair_action"](mask, pair, dagger=dagger)
                if acted is None:
                    continue
                new_bosons = list(bosons)
                if dagger:
                    new_bosons.remove(A)
                else:
                    new_bosons.append(A)
                key = (acted[0], tuple(sorted(new_bosons)))
                out[key] += coefficient * multiplicity * value * acted[1]
    return clean(out)


def main():
    manifest = json.loads((HERE / "inputs_manifest.json").read_text())
    for name, record in manifest.items():
        data = (HERE / "inputs" / name).read_bytes()
        need(sha256(data).hexdigest() == record["sha256"] and len(data) == record["bytes"],
             "frozen source pin " + name)
    need(manifest["spinor_tensors.npz"]["sha256"] == W_PIN, "authoritative v1.6.7 W pin")
    src, native_end = native_constructor()
    W = src["W"]
    with np.load(HERE / "inputs/spinor_tensors.npz", allow_pickle=False) as archive:
        raw = archive["W"]
    need(np.count_nonzero(raw.imag) == 0 and np.array_equal(raw.real, W),
         "actual original Clifford-color constructor reproduces every pinned W entry")
    need(W.shape == (60, 2016) and np.count_nonzero(W) == 480,
         "native shape 60 by 2016 and 480 nonzero coefficients")
    need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), "native row Gram 8 I60 independently rechecked")
    need(all(np.count_nonzero(W[:, j]) <= 1 for j in range(2016)), "native pair columns have at most one channel")
    need(zero(csr_matrix(src["J"]) @ src["C3"]), "original cubic J kills original three-fermion conversion image")
    need(np.array_equal(src["J"] @ src["J"].T, 15*np.eye(64, dtype=int)), "original J is nonzero with row Gram 15 I64")
    pairs, bar, signs = src["PAIRS"], src["BAR"], src["ETA"]
    eta = np.zeros((60, 60), dtype=np.int64)
    for A in range(60):
        eta[A, bar[A]] = signs[A]
    need(np.array_equal(eta, eta.T) and np.array_equal(eta @ eta, np.eye(60, dtype=int)),
         "original boson pairing is symmetric and involutive")
    need(np.trace(eta) == 0 and sum(A < bar[A] for A in range(60)) == 30,
         "original pairing consists of thirty distinct opposite-mode pairs")

    # All 480 interaction monomials have physical number change -2 + 2 = 0.
    charges = np.array([1]*64 + [2]*60)
    incidence = np.zeros((480, 124), dtype=np.int64)
    for row, (A, col) in enumerate(zip(*np.nonzero(W))):
        i, j = pairs[col]
        incidence[row, i] = incidence[row, j] = -1
        incidence[row, 64+A] = 1
    need(np.array_equal(incidence @ charges, np.zeros(480, dtype=int)),
         "all 480 signed native vertices conserve physical Nf plus 2 Nb")
    need(np.array_equal(incidence @ np.vstack([src["FW"], src["BW"]]), np.zeros((480, 8), dtype=int)),
         "all eight source Cartans are conserved at every native vertex")

    # Actual finite source Clock, followed by the documented type-correct lift.
    clock, clock_lines = original_clock()
    O16 = np.zeros((16, 16), dtype=np.int64)
    for i, j in enumerate(clock["img"]):
        O16[j, i] = 1
    O8 = O16[::2, ::2]
    need(np.array_equal(O16, np.kron(O8, np.eye(2, dtype=int))), "original Clock is complex-linear on the eight coordinate pairs")
    p = [int(np.flatnonzero(O8[:, i])[0]) for i in range(5)]
    need(p == [2, 0, 1, 4, 3], "reconstructed original five-slot Clock permutation")
    even = src["EVEN16"]
    index = {m: j for j, m in enumerate(even)}
    spin_clock = np.zeros((16, 16), dtype=np.int64)
    for col, mask in enumerate(even):
        mapped = [p[j] for j in range(5) if mask >> j & 1]
        sign = (-1)**sum(mapped[i] > mapped[j] for i in range(len(mapped)) for j in range(i+1, len(mapped)))
        spin_clock[index[sum(1 << j for j in mapped)], col] = sign
    GF = np.kron(spin_clock, np.eye(4, dtype=int))
    GB = np.zeros((60, 60), dtype=np.int64)
    for A in range(60):
        k, c = divmod(A, 6)
        GB[6*(p[k % 5]+5*(k//5))+c, A] = -1
    need(np.array_equal(np.linalg.matrix_power(GF, 6), np.eye(64, dtype=int)), "source fermion Clock has sixth power identity")
    need(not np.array_equal(np.linalg.matrix_power(GF, 3), np.eye(64, dtype=int)), "source fermion Clock does not have order three")
    need(not np.array_equal(np.linalg.matrix_power(GF, 2), np.eye(64, dtype=int)), "source fermion Clock does not have order two")
    need(zero(csr_matrix(W) @ src["wedge2"](GF) - csr_matrix(GB) @ csr_matrix(W)),
         "actual Clock intertwines original W on all two-fermion basis states")
    need(np.array_equal(GF.T @ GF, np.eye(64, dtype=int)) and np.array_equal(GB.T @ GB, np.eye(60, dtype=int)),
         "documented Clock lift is passive separately on fermions and bosons")

    # One-body representation matrices remain passive after second quantization.
    # Also re-prove that the proposed pair/quartet coefficients are invariant
    # under the entire actual 45+15 infinitesimal group, not only Cartans.
    Ws, etas = csr_matrix(W), csr_matrix(eta)
    need(len(src["LIE1"]) == 60, "all sixty one-body Lie matrices reconstructed from source")
    max_gaussian = 0
    boson_edges = np.zeros((60, 60), dtype=np.int64)
    for j, Xf in enumerate(src["LIE1"]):
        L = src["exterior_square"](Xf)
        B8 = Ws @ L @ Ws.T
        rr, cc = B8.nonzero()
        boson_edges[rr, cc] = 1
        max_gaussian = max(max_gaussian, int(np.max(np.abs(B8.data))) if B8.nnz else 0)
        need(zero(B8 @ Ws - 8*Ws @ L), "source Lie covariance " + str(j))
        need(zero(B8 @ etas + etas @ B8.T), "source invariant boson pairing " + str(j))
        need(zero(B8 @ etas @ Ws + 8*etas @ Ws @ L.T), "source invariant quartet coefficient " + str(j))
    need(max_gaussian <= 16, "Gaussian-integer Lie arithmetic stays exactly representable")
    reached, frontier = {0}, [0]
    while frontier:
        j = frontier.pop()
        for k in np.flatnonzero(boson_edges[j] + boson_edges[:, j]):
            if int(k) not in reached:
                reached.add(int(k)); frontier.append(int(k))
    need(len({tuple(row) for row in src["BW"]}) == 60,
         "sixty distinct boson weights reduce invariant-pairing freedom to opposite-weight diagonal coefficients")
    need(len(reached) == 60,
         "source Lie support connects all sixty boson weights, proving the invariant pairing unique up to scale")

    # Infinite boson CCR certificate; no truncated oscillator matrices used.
    nb = {((A,), (A,), None): 1 for A in range(60)}
    tplus = {((A,), (), (False, A)): 1 for A in range(60)}
    tminus = {((), (A,), (True, A)): 1 for A in range(60)}
    bplus = {(tuple(sorted((A, bar[A]))), (), None): signs[A] for A in range(60) if A < bar[A]}
    bminus = {((), key[0], None): value for key, value in bplus.items()}
    rplus = {((bar[A],), (), (True, A)): signs[A] for A in range(60)}
    rminus = {((), (bar[A],), (False, A)): signs[A] for A in range(60)}
    X, Q, R = add(tplus, tminus), add(bplus, bminus), add(rplus, rminus)
    need(charge_action(X) == {}, "entire original X is physical-number neutral")
    need(charge_action(nb) == {}, "original Nb control is physical-number neutral")
    need(charge_action(bplus) == {k: 4*v for k, v in bplus.items()}, "all original-metric boson pair terms carry N charge four")
    need(charge_action(rplus) == {k: 4*v for k, v in rplus.items()}, "all original-W quartet terms carry N charge four")
    need(comm(nb, bplus) == {k: 2*v for k, v in bplus.items()}, "CCR identity [Nb,Bplus]=2 Bplus")
    need(comm(bminus, bplus) == add(nb, {UNIT: 30}), "CCR identity [Bminus,Bplus]=Nb+30 I")
    need(comm(tminus, bplus) == rplus, "full sixty-channel CCR identity [Tminus,Bplus]=Rplus")
    need(comm(Q, X) == add(rminus, rplus, -1), "CCR identity [Q,X]=Rminus-Rplus")
    need(comm(nb, comm(Q, X)) == {k: -v for k, v in R.items()},
         "single extra Q control derives entire quartic-charge cubic channel: -[Nb,[Q,X]]=Rplus+Rminus")
    need(sum(v*v for v in bplus.values()) == 30, "actual boson-pair creation vacuum norm squared is thirty")
    need(int(np.sum((eta @ W)**2)) == 480, "actual quartet-creation vacuum norm squared is 480")
    need(not np.any(np.all(src["BW"] == 0, axis=1)), "no degree-one boson singlet even at weight zero")
    need(all((int(sum(src["FW"][i, 5:])) + int(sum(src["FW"][j, 5:]))) % 4 == 2 for i, j in pairs),
         "SU4 center excludes every fermion pair from degree-two singlets")

    # Structural closure proof is [N,AB]=[N,A]B+A[N,B]. This exact generic
    # 3x3 polynomial identity verifies the derivation rule, not an empirical
    # enumeration of short words. Induction then covers every finite word.
    n0, n1, n2 = s.symbols("n0 n1 n2")
    NN = s.diag(n0, n1, n2)
    AA = s.Matrix(3, 3, s.symbols("a0:9"))
    BB = s.Matrix(3, 3, s.symbols("b0:9"))
    residual = NN*AA*BB-AA*BB*NN-(NN*AA-AA*NN)*BB-AA*(NN*BB-BB*NN)
    need(residual.applyfunc(s.expand) == s.zeros(3), "generic commutator derivation identity supporting arbitrary-word induction")

    # New native N=4 singlet block: prove its entire action, not a compression.
    # The four-fermion Fierz cancellation is recomputed from every source term.
    four = defaultdict(int)
    four_terms = 0
    for A in range(60):
        for a in np.flatnonzero(W[A]):
            for b in np.flatnonzero(W[bar[A]]):
                modes = pairs[a] + pairs[b]
                if len(set(modes)) < 4:
                    continue
                sign = (-1)**sum(modes[i] > modes[j] for i in range(4) for j in range(i+1, 4))
                four[tuple(sorted(modes))] += int(signs[A]*W[A, a]*W[bar[A], b])*sign
                four_terms += 1
    need(four_terms == 3840 and len(four) == 960, "native Fierz audit enumerates 3840 signed terms across 960 fermion quartets")
    need(not clean(four), "native Fierz identity sum eta_AB P_A^dag P_B^dag = zero exactly")
    vacuum = {(0, ()): 1}
    beta = {(0, key[0]): value for key, value in bplus.items()}
    rho = {}
    for A, col in zip(*np.nonzero(W)):
        i, j = pairs[col]
        rho[((1 << i) | (1 << j), (bar[A],))] = int(signs[A]*W[A, col])
    need(native_action(vacuum, src, False) == {} and native_action(vacuum, src, True) == {},
         "full original interaction annihilates the vacuum")
    need(native_action(beta, src, False) == {}, "full original Tplus annihilates unnormalized Bplus vacuum")
    need(native_action(beta, src, True) == rho, "full original Tminus takes Bplus vacuum exactly to Rplus vacuum")
    need(native_action(rho, src, False) == {key: 16*value for key, value in beta.items()},
         "full original Tplus takes Rplus vacuum exactly to sixteen Bplus vacuum")
    need(native_action(rho, src, True) == {}, "full original Tminus annihilates Rplus vacuum by exact Fierz cancellation")
    need(all(mask.bit_count()+2*len(bosons) == 4 for mask, bosons in list(beta)+list(rho)),
         "both constructed native singlets have physical number four")
    need(s.sqrt(480)/s.sqrt(30) == 4 and 16*s.sqrt(30)/s.sqrt(480) == 4,
         "normalization yields the exact native singlet coupling four g")
    delta, coupling, kappa, er = s.symbols("Delta g kappa E_R", real=True)
    singlet_H = s.Matrix([[2*delta, 4*coupling], [4*coupling, delta]])
    singlet_center = singlet_H-3*delta*s.eye(2)/2
    need(singlet_center**2 == (delta**2+64*coupling**2)*s.eye(2)/4,
         "native singlet two-level spectral polynomial is exact")
    need(s.cancel((64*coupling**2/(delta**2+64*coupling**2)).subs(coupling, delta/20)) == s.Rational(4,29),
         "native N4 singlet conversion maximum at g/Delta=1/20 is four over twenty-nine")
    H3 = s.Matrix([[er, kappa*s.sqrt(30), 0],
                   [kappa*s.sqrt(30), 2*delta, 4*coupling],
                   [0, 4*coupling, delta]])
    need(H3 == H3.H, "new relational three-state parent is Hermitian")
    need(H3*s.diag(4,4,4)-s.diag(4,4,4)*H3 == s.zeros(3),
         "new relational process has total physical number four on every state")
    need(s.expand((H3**2)[2, 0]) == 4*s.sqrt(30)*kappa*coupling,
         "joint source-to-quartet amplitude has nonzero second-order coefficient")
    need(s.expand(((H3**2)[2, 0]/2)**2) == 120*kappa**2*coupling**2,
         "initial relational quartet population is 120 kappa squared g squared t fourth")
    rel_a, rel_b, rel_c = s.symbols("a b c", complex=True)
    psi_rel = s.Matrix([0, rel_a, rel_b, 0, rel_c, 0])
    rho_rel = psi_rel*psi_rel.H
    reduced_rel = s.Matrix(3,3,lambda i,j:sum(rho_rel[2*i+r,2*j+r] for r in range(2)))
    need(reduced_rel[0,1] == reduced_rel[0,2] == 0,
         "tracing the sharp-charge reference erases system cross-number coherences")
    need(reduced_rel[1,2] == rel_b*s.conjugate(rel_c),
         "tracing the reference retains coherence inside the native number-four singlet block")

    # Exact native two-state mechanism follows from W W^dagger = 8 I.
    d, g = s.symbols("Delta g", real=True)
    H2 = s.Matrix([[0, s.sqrt(8)*g], [s.sqrt(8)*g, d]])
    centered = H2 - d*s.eye(2)/2
    need(centered**2 == (d*d+32*g*g)*s.eye(2)/4, "exact native two-level spectral polynomial")
    need(s.cancel((32*g*g/(d*d+32*g*g)).subs(g, d/20)) == s.Rational(2, 27),
         "native bright-pair conversion maximum at g/Delta=1/20 is two over twenty-seven")
    need(Fraction(2, 27)/8 == Fraction(1, 108), "single primitive pair has one-eighth bright weight")

    # Resource ledger: a charge-4 ancilla may exchange number while total
    # charge is conserved. A number eigenstate gives an incoherent channel;
    # a phase reference supplies first-order coherence but is a new resource.
    raised = s.Matrix([[0, 0], [1, 0]])
    lowered = raised.T
    n = s.diag(0, 4)
    v = s.kronecker_product(raised, lowered)+s.kronecker_product(lowered, raised)
    total = s.kronecker_product(n, s.eye(2))+s.kronecker_product(s.eye(2), n)
    need(total*v-v*total == s.zeros(4), "charge-four exchange conserves total system-plus-reference number")
    quarter = s.Matrix([[1,0,0,0], [0,1/s.sqrt(2),-s.I/s.sqrt(2),0],
                        [0,-s.I/s.sqrt(2),1/s.sqrt(2),0], [0,0,0,1]])
    need(quarter.H*quarter == s.eye(4), "reference-exchange unitary is exact")
    z = s.Matrix([1, 0]); one = s.Matrix([0, 1]); plus = (z+one)/s.sqrt(2)
    psi_number = quarter*s.kronecker_product(z, one)
    rho_number = partial_system(psi_number*psi_number.H)
    need(rho_number == s.eye(2)/2, "number eigenstate reservoir changes population without generating phase coherence")
    psi_phase = quarter*s.kronecker_product(z, plus)
    rho_phase = partial_system(psi_phase*psi_phase.H)
    need(s.simplify(rho_phase.det()) == s.Rational(1, 16),
         "finite coherent reservoir is not silently a reusable exact unitary control")
    tau = plus*plus.T
    heff = partial_system(v*s.kronecker_product(s.eye(2), tau))
    need(heff == (raised+lowered)/2, "coherent charge-four reference supplies extra control only at first order here")
    need(partial_system(v*s.kronecker_product(s.eye(2), one*one.T)) == s.zeros(2),
         "charge-four number eigenstate supplies no first-order coherent control")

    result = {
        "status": "PASS", "exact_checks": len(CHECKS), "checks": CHECKS,
        "source_replay": {"native_constructor_through_line": native_end,
                          "native_constructor_retained_guards": len(src["checks"]),
                          "clock_main_lines": clock_lines,
                          "clock_source_mathematical_guards": 4,
                          "clock_permutation": p,
                          "original_source_programs_replayed_in_full": False},
        "source_input_count": len(manifest),
        "closure": {"native_word_algebra_subset": "{Nf+2Nb}'",
                    "neutral_ancilla_kraus_still_number_preserving": True,
                    "all_charge_conserving_ancilla_channels_preserve_system_number": False,
                    "Bplus_in_native_word_algebra": False,
                    "Rplus_in_native_word_algebra": False,
                    "closure_scope": "declared passive Fock lifts, X, Nb and charge-neutral Kraus compositions"},
        "minimal_extra_control": {
            "name": "Q=Bplus+Bminus",
            "lowest_G_invariant_number_changing_polynomial_degree": 2,
            "conditional_word": "Rplus+Rminus=-[Nb,[Q,X]]",
            "extra_assumptions": ["Q execution", "independent X and Nb control for this nested-commutator synthesis",
                                  "pulse sign/time control and convergence if interpreted as gate synthesis"],
            "source_supplies_metric_coefficients": True,
            "source_supplies_executable_Q": False,
            "full_E8_operator_representation_constructed": False,
            "boson_pair_vacuum_norm_squared": 30,
            "quartet_vacuum_norm_squared": 480},
        "new_native_singlet_block": {
            "basis": ["Bplus|0>/sqrt(30)", "Rplus|0>/sqrt(480)"],
            "physical_number": 4,
            "H": "[[2 Delta,4 g],[4 g,Delta]]",
            "invariant_under_entire_native_H": True,
            "native_conversion_max_at_g_over_Delta_1_over_20": "4/29",
            "entire_N4_singlet_sector_dimension_claimed": False,
            "fierz_signed_terms": four_terms, "fierz_quartets": len(four), "fierz_residual_terms": 0},
        "new_relational_process": {
            "reference": "two G-singlets with physical number 0 and 4",
            "extra_interaction": "kappa*(Bplus tensor |0><4| + Bminus tensor |4><0|)",
            "basis": ["vacuum tensor ref4", "beta tensor ref0", "rho tensor ref0"],
            "H": "[[E_R,sqrt(30) kappa,0],[sqrt(30) kappa,2 Delta,4 g],[0,4 g,Delta]]",
            "total_N": 4, "full_Spin10_times_SU4_invariant": True,
            "source_reference_and_joint_interaction_derived": False,
            "isolated_Hext_implemented": False,
            "sharp_reference_returns_unchanged_on_number_injection": False,
            "reduced_cross_number_coherence": "zero",
            "initial_quartet_probability": "120 kappa^2 g^2 t^4 + O(t^6)",
            "spatial_transfer_claimed": False,
            "paper_section_9_relation": "same resource principle, different conserved charge and different process"},
        "smallest_native_mechanism": {
            "carrier": "one normalized bright pair and the matching one-boson state",
            "H": "[[0,sqrt(8)*g],[sqrt(8)*g,Delta]]",
            "bright_conversion_probability": "32*g^2/(Delta^2+32*g^2)*sin(sqrt(Delta^2+32*g^2)*t/2)^2",
            "bright_max_at_g_over_Delta_1_over_20": "2/27",
            "primitive_pair_max_at_same_point": "1/108",
            "native_preparation_readout_and_time_calibration_derived": False},
        "resource_reference_example": {"total_charge_conserved": True,
                                       "system_charge_changes": True,
                                       "number_reference_produces_coherence": False,
                                       "finite_phase_reference_output_determinant": "1/16"},
        "boundaries": {"new_source_mechanism_beyond_declared_Fock_lift_excluded": False,
                       "whole_repository_no_go": False,
                       "native_spatial_transport_proved": False,
                       "new_extended_ground_state_theorem": False,
                       "T1_T8_closed": []},
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(main(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")
