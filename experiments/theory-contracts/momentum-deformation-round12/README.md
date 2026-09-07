# Round12: first-order momentum repair and second-order obstruction

[The complete proof](PROOF.md) fixes the actual H_+, all Fourier and TT
conventions, and the zeroth-order centered-difference total momentum including
the tensor contribution. A smooth cubic correction repairs its order-g
conservation equation at each fixed finite volume. At order g^2, however,
an exact resonant coefficient excludes every globally smooth time-independent
correction to a strongly conserved quantity, not only a chosen polynomial
ansatz. This is not a theorem excluding every constraint-proportional (weak)
closure on a deformed constraint surface.

The coefficient includes both the existing positive static term R and all
relevant tensor exchange channels. On 6^3 at m^2=4/7 a compact periodic orbit
has mean forcing 301 sqrt(3)/599040 != 0. An integral of a derivative of a
smooth single-valued correction on that orbit must vanish. A separate two-angle
torus proof extends the result to all finite m^2>=0 and cubes of side divisible
by six. It uses no ergodicity, thermodynamic limit or untested denominator limit.

To obtain a strongly conserved smooth momentum with this prescribed seed,
one must therefore change the interaction or leave the theorem's regularity
and seed assumptions. A merely weakly closing constraint needs a separate
analysis; it has not been ruled out. Exact finite lattice translations remain symmetries.
No prohibition of every gravitational parent, every conserved quantity or
every nonperturbative construction follows.

`momentum_deformation_check.py` checks the exact normal-form algebra and
resonances. `redteam_momentum_check.py` independently imports the original Ward
source, reconstructs three relevant TT projectors from their nullspaces,
rederives the Fourier normalization and independently sums contact/exchange
coefficients. These are unpromoted mathematical research contracts, not a
full T3/T7 closure or empirical evidence.
