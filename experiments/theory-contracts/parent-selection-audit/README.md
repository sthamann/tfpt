# Parent-selection audit: what TFPT supplied, and what the test model supplied

2026-09-08. **NON-RH / unpromoted theory experiment.**

## Decision

The original compact U(1) low/high cubic parent is a mathematically useful
**declared test model**, not a uniquely reconstructed TFPT Hamiltonian.
Two exact tests identify the present bottleneck:

1. Its explicitly allowed parent-family inputs admit different gauge-invariant
   dynamics. Gauge symmetry, locality, cubic symmetry and signed-wall algebra
   do not select the tested electric/magnetic coefficients.
2. Its actual frozen, translation-invariant matter symbol has no Weyl point.
   All momentum dependence factors through one scalar. Low/high labels and
   a positive high-band gap cannot supply a chiral starting spectrum.

The first statement is **not** nonuniqueness under every TFPT axiom: the
missing charged seam/bulk operator dictionary prevents checking that stronger
premise. The second statement is **not** a no-go for the interacting quantum
parent or for the broader matrix-valued signed-wall family.

The next high-value task is therefore a TFPT-derived **matrix-valued charged
kinetic symbol and observable dictionary**, followed by its chirality test.
Further whole-parent gap estimates are not the next acceptance criterion.

## 1. Provenance, traced to the actual sources

`checker.py` pins eight input files and checks the Round37 parent's transitive
input pins. The original source modules and parameters are never rewritten.
These classifications concern this documented derivation route; absence of
a derivation here is not proof that no derivation could ever exist.

| Ingredient | Actual origin | Classification / missing selection |
|---|---|---|
| Signed wall `[[A+beta A^2, eta A],[eta A,M]]` | `verification/v1027_signed_det_car_wall.py`, `signed_block` and symbolic certificate | Conditional family. `M=Delta+lambda`, `beta=lambda*g^2`, `eta=lambda*g` are identities once positive Delta/lambda and g are supplied. |
| Dynamical compact rotors, electric kinetic energy | Round30 `QUANTUM_GAUGE.md`, sections 1 and 3 | Explicit **new dynamical extension** of the fixed-gauge calculation, not a derived seam-to-4D map. |
| Group U(1), one low/high mode pair per site | Round31 README and its cubic construction; Round37 `parent_terms` | Chosen specialization, not full SM content or a derived chiral representation. |
| Three-dimensional cubic graph | Round31 `cubic_box`; Round37 `cubic_graph` | Chosen geometry. The general family accepts other graphs/dimensions. |
| Hopping `a=1/12` | Round31 `filled_lattice_state_bound`: `1/(4*dimension)` at declared dimension 3 | Normalization of the chosen graph. The same bound construction also works at other declared dimensions. Here **a is hopping, not lattice spacing**. |
| `eta=1/2`, `beta=1/4`, `M=4` | Inherited example `Delta=3, lambda=1, g=1/2` | Fixed example values satisfying hypotheses, not TFPT coupling predictions. They are related through the family; not three unrelated parameters. |
| Low onsite `epsilon_L=1/96` | All six backtracks in `beta A^2` | **Derived within the chosen model:** `6*beta*a^2`. It is not an extra independent fitting parameter. |
| `kappa=1/100` | Round31 declared weak-electric example, retained in Round37 | The parent-family hypothesis only requires `kappa>0`; no TFPT selection in this construction. |
| `V_mag=0` | Round31 cubic test case | Chosen potential. Round30 explicitly permits bounded nonnegative gauge-invariant magnetic multiplication potentials on finite graphs. |
| Background `q_x=1` and `N_L+N_H=N` | Round31 filled-state prescription; Round37 Gauss operator | Background is chosen; total occupation then **follows** by summing Gauss on a torus. |
| Ground-state prescription / periodic subsequence | `neutral-ground-state/README.md` | Existence of states derived conditionally; unique state, boundary independence and cosmological selection not derived. |

The current `TFPT.TOE.COMPLETE.01` ledger explicitly leaves T1--T8 open.
It does not license replacing missing selection by successful computations
inside one member of this family. Nor is an absolute numerical energy unit
the issue here: the witnesses below change dimensionless response ratios.

## 2. Selection witness that survives the full physical Gauss constraint

Use the complete original hopping and the same physical observable dictionary.
For a plaquette p let `W_p=prod_e U_e^(p_e)`, with four signed unit entries,
and `S_p=sum_e p_e E_e`. The full rotor relations give, on the finite-flux
core and then with their indicated domain extensions,

    [E_e,W_p] = p_e W_p,
    [H_kappa,W_p] = kappa W_p (S_p+2),
    [W_p^*,[H_kappa,W_p]] = 4 kappa I.                 (1)

All matter hoppings commute with W_p: their rotor entries are commuting
multiplication functions, and W_p commutes with fermions. No matter term
is dropped. Closed p has zero divergence, hence W_p preserves every Gauss
sector. Equation (1) is state-independent, so it does not rely on declaring
the all-low preparation a vacuum. The inner commutator is unbounded; the
double commutator extends to the displayed bounded scalar operator.

Both `kappa=1/100` and `kappa=1/50` satisfy the declared family's hypotheses
with the **same** A, beta, eta and M. Equation (1) distinguishes them by
`1/25` versus `2/25`. Dividing by the unchanged hopping a gives `12/25`
versus `24/25`, so this is not an overall choice of energy/time units.
Nonzero matter hopping matrix elements stay unchanged. The generators
differ with the fixed observable dictionary, not just their zero of energy.
No claim about arbitrary nonlocal unitary equivalences without a dictionary
or a difference of infrared universality classes is needed or established.

The independent original-H action is checked on all 70 neutral plaquette
occupations and several flux backgrounds, also at integer flux +/-10^6 in
tests. Full cubic checks retain all 6000 (L5) / 10368 (L6) original directed
hops, including external couplings. These samples check implementations;
the arbitrary-volume/integer-flux statement follows from (1), not a sample.

### A second freedom invisible to that Wilson diagnostic

On every finite cubic torus add the homogeneous potential

    delta H_lambda = lambda sum_p [1-(W_p+W_p^*)/2], lambda>=0.    (2)

Each summand is nonnegative, bounded by 2 lambda, local and gauge invariant.
The whole sum is invariant under translations, axis permutations and
reflections. It is bounded on a finite torus (not uniformly bounded as one
global operator when volume grows), and is a bounded finite-range interaction
per cell in the thermodynamic formulation. It preserves the finite-volume
self-adjoint domain, Gauss sectors, stability and the same matter family.
It does not satisfy the frozen test's extra choice `V_mag=0`; that choice
is precisely one of the inputs whose TFPT provenance is missing.

Because (2) commutes with W_p, diagnostic (1) is blind to lambda. However,

    [delta H_lambda,E_e] = (lambda/2) sum_(p containing e)
                                          p_e (W_p-W_p^*).      (3)

Let |0> be the neutral all-low/E=0 vector, and |p>=W_p|0>.
The normalized **test preparation**, not a selected vacuum,
`psi=(|0>+i|p>)/sqrt(2)` has force-response difference

    <psi| i[delta H_lambda,E_e] |psi> = lambda p_e/2.             (4)

Other incident plaquettes have orthogonal flux outputs, so only p contributes.
The 2x2 check evaluates these matrix elements exactly; it is not a truncated
Hamiltonian used to claim a spectral gap. This supplies a complementary
observable to (1). Electric energy is unbounded, but these finite-support
vectors belong to its common core. No full-time integration is claimed.

**Logical scope:** these are counterexamples to selection by the currently
implemented parent-family assumptions and symmetries. They are NOT verified
examples satisfying all original TFPT axioms and full charged seam response.
Claiming the latter would assume the dictionary that T2/T3 still ask us to derive.

## 3. First physical discriminator: the actual free symbol is not Weyl

Freeze the link multiplication variables at the trivial classical background
U=1, only to inspect the matter kinetic symbol. This is **not** a normalizable
quantum-rotor state, nor a reduction of the full dynamical Gauss problem.

The original full hopping expansion, including onsite backtracks, gives

    x(k) = 2a sum_(j=1)^3 cos(k_j) = sum_j cos(k_j)/6,
    h(k) = [[x+x^2/4, x/2], [x/2, 4]], x in [-1/2,1/2].        (5)

This Laurent-polynomial identity is checked against the original L5 and L6
term builders, not inserted as an independent desired dispersion.
The traceless Pauli vector is

    d(k) = (x/2, 0, (x+x^2/4-4)/2).

Thus `partial_i d = d'(x) partial_i x`: the Pauli Jacobian has rank at most
one. Its derivative cross products vanish. The two eigenprojectors are smooth
functions of one scalar, so their Berry curvature is zero. Moreover, the
band separation is at least `4-9/16=55/16>0` on the entire Brillouin zone:
there is no two-band touching at any energy, hence no Weyl node.

At the arbitrary reference energy zero,

    det h = 4x(1+3x/16),

so only x=0 is attainable. This is a smooth two-dimensional level surface,
not isolated chiral nodes. Its gradient cannot vanish there: critical points
of sum cos have values -3,-1,1,3, never zero. At `(pi/2,pi/2,pi/2)` the
gradient of x is `(-1/6,-1/6,-1/6)`.

This zero surface must **not** be called the physical neutral Fermi surface.
Even within the frozen matter problem, imposing N fermions on N cells fills
the entire lower band, since every upper-band state lies above every lower
state. That free fixed-number problem is a band insulator, with particle-hole
gap at least 55/16. None of this establishes the full quantum-parent gap.

Retuning coefficients within any 2x2 symbol `h(k)=F(x(k))` cannot create a
three-direction Weyl symbol: the same rank-one chain rule holds, even if F
has a nonzero sigma_y component. Therefore simply adjusting M, eta or beta,
or using another scalar polynomial of the same adjacency, does not fix this
specific free-spectrum deficiency.

### What the signed wall can still do

For the broader matrix-valued family the lower branch has

    f_-(x)=x+3x^2/16-x^3/64+O(x^4).

Consequently an **independently supplied** matrix symbol
`A(k0+q)=sum_i,j v_ij q_j sigma_i+O(|q|^2)` retains its linear Weyl jet
after the wall, if `det v != 0`. The wall can preserve such a symbol; it
does not derive it. The test suite checks this local algebra target only.
It adds no spinor fields to the original physical parent and claims neither
global anomaly cancellation nor a chiral lattice measure/mirror gap.

## 4. Next acceptance gate, in dependency order

1. **Charged kinetic dictionary:** derive the site fields, their gauge/spin
   action and the kinetic A from the actual TFPT seam/compiler data. State
   each additional assumption. The low/high field pair cannot be relabeled
   as physical chirality. A Pauli matrix inserted by hand is not a derivation.
2. **Rank and charge test:** for that derived A, compute the linear Pauli
   Jacobian at every candidate node, its rank and oriented determinant, the
   full node/mirror census, and representations/anomalies. A local linear
   algebra pass is necessary for that free-Weyl route, not sufficient for T4.
3. **Coupling-selection test:** express (1) and (3), or suitable equivalent
   charged-source responses, through the same compiler dictionary. Only then
   can an actual TFPT response fix kappa and the magnetic term. Symmetry
   alone leaves the explicit freedoms above. Different UV responses need
   not mean different IR universality classes; that remains another question.

If there is no microscopic free-Weyl route, an interacting emergence route
must instead specify a physical composite, a state/limit and its chiral pole.
The frozen calculation does not exclude that possibility, but presently
supplies no such mechanism. T5/T7 then require the common continuum and
spin-two/universal-coupling tests, and T6/T8 a shared state/source functional.

**Stop rule:** do not undertake another bulk-gap or long-time precision
round merely to strengthen this scalar prototype. Require an explicit
connection to one of the acceptance items above first.

## 5. Reproduction and scientific limits

From repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/parent-selection-audit/checker.py --output experiments/theory-contracts/parent-selection-audit/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/parent-selection-audit -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/parent-selection-audit -p 'test_*.py' -v
```

No floating eigenvalue threshold, fit, electric cutoff, bulk diagonalization,
or continuum extrapolation is used. New symbolic/rational checks include
independent CAR signs and original-H actions, large integer fluxes, complete
local identities with external cubic hops, homogeneous magnetic symmetry,
the original Bloch polynomial, source mutants and inference-boundary tests.
General statements rest on the analytic arguments above; tests are not a
proof-assistant certificate or external peer review. Complexity of the
full interacting spectral problem has not been solved.

Only this experiment and experiment index/notes are intended to change.
No paper/website/ledger/scorecard/verification promotion, commit or push.
No T1--T8 gate is closed and no RH claim is made.

Primary methodological references (not evidence of TFPT identification):

- [Kogut and Susskind, Hamiltonian formulation of Wilson's lattice gauge theories (1975)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395): electric and magnetic Hamiltonian framework.
- [Zohar and Burrello, A Formulation of Lattice Gauge Theories for Quantum Simulations](https://arxiv.org/html/1409.3085v2): group-coordinate matter/gauge construction; the original Round30 reference.
- [Liu and Vanderbilt, Weyl semimetals from noncentrosymmetric topological insulators (2014)](https://arxiv.org/html/1409.6399): two-band Pauli/Jacobian criterion. Equations (1)--(5) and the application to this parent are derived here, not attributed to that paper.
