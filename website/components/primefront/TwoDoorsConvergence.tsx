"use client";

import { motion } from "motion/react";
import { StatusBadge } from "./StatusBadge";

export function TwoDoorsConvergence() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <p className="mb-3 font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
        Two doors, one object · T102 + T103
      </p>

      <div className="grid grid-cols-2 gap-2">
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.4 }}
          className="rounded-xl border border-violet-400/40 bg-violet-500/10 p-3"
        >
          <p className="font-mono text-[10px] uppercase tracking-wider text-violet-700/90">
            Door A · handover mechanism
          </p>
          <p className="mt-1.5 text-xs leading-relaxed text-violet-800">
            The onset is manufactured by the Schur dressing against E₀⊕E₊ —
            it takes 35.7%…97.3% of the bare eigenvalue.
          </p>
          <p className="mt-1.5 font-mono text-[10px] text-slate-600">
            T102 · arithmetic_bound_probe.py
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 8 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.4, delay: 0.15 }}
          className="rounded-xl border border-sky-400/40 bg-sky-500/10 p-3"
        >
          <p className="font-mono text-[10px] uppercase tracking-wider text-sky-700/90">
            Door C · instrument race
          </p>
          <p className="mt-1.5 text-xs leading-relaxed text-sky-800">
            The remaining loss is the wing slack S = 1 − ρ (falls
            0.2091 → 0.0392); the pencil is nearly saturated, the bulk is not
            low-rank.
          </p>
          <p className="mt-1.5 font-mono text-[10px] text-slate-600">
            T103 · instrument_probe.py
          </p>
        </motion.div>
      </div>

      {/* converging arrows */}
      <svg
        viewBox="0 0 320 52"
        className="w-full"
        aria-hidden
      >
        <motion.path
          d="M 80 4 C 80 28, 120 40, 152 46"
          fill="none"
          stroke="rgba(196,181,253,0.7)"
          strokeWidth={1.6}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.7, delay: 0.5, ease: "easeInOut" }}
        />
        <motion.path
          d="M 240 4 C 240 28, 200 40, 168 46"
          fill="none"
          stroke="rgba(125,211,252,0.7)"
          strokeWidth={1.6}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.7, delay: 0.65, ease: "easeInOut" }}
        />
        <motion.circle
          cx={160}
          cy={47}
          r={3.5}
          fill="#34d399"
          initial={{ opacity: 0, scale: 0 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.3, delay: 1.3 }}
          style={{ transformBox: "fill-box", transformOrigin: "center" }}
        />
        <motion.text
          x={64}
          y={30}
          fontSize="8"
          className="fill-slate-600 font-mono"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.3, delay: 0.9 }}
        >
          same object,
        </motion.text>
        <motion.text
          x={222}
          y={30}
          fontSize="8"
          className="fill-slate-600 font-mono"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.3, delay: 0.9 }}
        >
          two sides
        </motion.text>
      </svg>

      <motion.div
        initial={{ opacity: 0, y: 8 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.4 }}
        transition={{ duration: 0.45, delay: 1.4 }}
        className="rounded-xl border border-emerald-400/40 bg-emerald-500/10 p-3 text-center"
      >
        <p className="font-mono text-[10px] uppercase tracking-wider text-emerald-700/90">
          The wing near-null direction
        </p>
        <p className="mt-1.5 text-sm leading-relaxed text-emerald-900">
          One scalar per zone: a lower bound on σ_k just above atom entry.
        </p>
      </motion.div>

      <div className="mt-2 flex flex-wrap items-start gap-2 rounded-xl border border-dashed border-sky-400/35 bg-slate-100/50 p-3">
        <StatusBadge badge="sandbox" />
        <p className="min-w-0 flex-1 text-xs leading-relaxed text-slate-600">
          T104 · SCHUR.PROFILE.BOUND — CHAIN-PARTIAL (two independent arms,
          21/21 + 47/47): the naive margin route is dead, exact spectral-split
          chains close 16/16 with finite data, and the hard core moves to a
          bare_k lower bound plus the soft dressing scalar L. T105 ·
          BARE.AVOIDANCE.CORE — ONE-OF-TWO (28/28): bare is certified in closed
          form and the avoidance law becomes a theorem, leaving one
          Friedrichs-angle statement. Everything after that — the twenty-one
          parts that compress this one statement down to one sign plus one
          declared accounting convention, drive the certified ladder to zone
          155,921, and finally assemble the whole chain end to end (T125 ·
          GRAND.ASSEMBLY — ASSEMBLY-GREEN, 34/34: all five stages on 52 of 52
          zones, 430 completed Cholesky certificates, the load-bearing spine
          96.2% identity-or-Cholesky with the Harnack pair no longer in it) — is
          told in{" "}
          <a
            href="#compression"
            className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
          >
            sections 20–22
          </a>
          . Series complete at 125 parts / 3139 sandbox checks; the mandate
          T ≤ 125 is fulfilled. Phase 2 — the full proof — is now open: T126 ·
          UNIFORMITY.SEAMS (SEAMS-CERTIFIED, 31/31) finishes the seam
          architecture, T127 · TWO.INEQUALITIES (BOTH-SHAPED, 28/28) dissects
          the two genuinely new inequalities it left — U5-as-stated is refuted
          and replaced by a band plus an enumeration, U3 collapses to a coarse
          floor —           and T128 · TEML (THREE-OF-FOUR, 27/27) works the resulting
          four-point list cheapest first: three of the four points stand at
          their preregistered bars (the exception list derived and closed, the
          retention bound exact bookkeeping, the boundary-layer exclusion now
          a proof with an 11.6× floor margin), while the kappa bar was missed
          honestly — by 3.6%, systematically in the ratio. T129 ·
          KAPPA.DEEP.SEAMS (KAPPA-WILD, 28/28) is the most productive break
          of the phase:           the fitted kappa law falls once on 331 fresh
          transports — bar frozen, violation counted — but the theorem
          underneath stands: flat is exactly 1, linear is exactly 2,
          everything above is curvature, and the curvature chain is a
          per-transport theorem on all 436; the two affordable deep seams
          carry complete certificates on the graded space, honestly
          downgraded with a measured 8% false-positive rate declared before
          the results. T130 · CURVATURE.BRIDGE (ONE-OF-TWO, 30/30) then
          attacked the two named pieces and exactly one stands: the
          graded-to-uniform bridge stands as an identity — the matrix-form
          Céa/Strang defect reproduces the uniform floor on 84 pairs with
          zero overshoot, explains the 8% false positives completely, and
          carries both deep seams to positive fine floors at up to 3.8× the
          factorization cap — while the curvature bound honestly broke its
          frozen shape band on 13/545 and is reduced to a uniform bound on
          one exponent. T131 · SELF.SUPPLY (SUPPLY-PARTIAL, 25/25) then
          built the self-supply loop and left it one number short of
          closed, with two new theorems: the epsilon-to-floor secular
          sandwich (sharp to ~1.3, sign half an equivalence) replaces the
          Lanczos estimate on all 84 bridge pairs with zero brackets lost —
          exposing that the old Ritz value overestimated the floor by up to
          7.9× — and sign constancy is proved via Perron–Frobenius on the
          inverse (575/575); the one-hump honestly broke at depth, S*
          rose to 1.8472 over its frozen 1.1926, and M25 is reduced to
          positivity of the pole-free section with nine decades of slack.
          Two irreducibles remain (the word &ldquo;for all&rdquo;, the RH
          address). The phase then ran in reverse: the identity block underneath
          the map is promoted as load-bearing v542
          (PRIME.MARGIN.IDENT.01, 44 checks — nine per-instance identities and
          theorems, no fit, no graded floor, nothing uniform in the zone
          index), T132 · BD.SEAM (SPECTRUM-ONLY, 21/21) made the
          Beurling–Deny triad an operator discriminator for the seam DtN (same
          spectrum to 7.5e-13, different operator, the N-stable gap 0.1746
          sitting in the killing measure — and KERNEL coupled to MARKS), and
          T133 · CERT.FLOOR (MIXED, 23/23) audited the suite&apos;s own PSD
          rows: the Hankel matrix v379 tests is, as a matrix of doubles,
          certifiably not positive semidefinite, the mathematical matrix is
          fine, and the exact positive-mixture Gram certificate now hardens
          that module — marker unchanged. T134 · POLE.FREE.FLOOR (PARTIAL,
          21/21) then attacked the pole-free floor and closed its existence
          half: every Cholesky pivot of the pole-free form is positive on
          79/79 windows (T119&apos;s negative pivot belonged to the form with
          the pole), but all six cheap lower-bound routes fail by sign, not
          size — the nine decades of slack are worthless to them — and the
          anatomy names the one surviving opening: an M-matrix question,
          with the lumped Stieltjes comparison S_B = S + L_Δ certified on
          900/900 blocks and the whitening honestly correcting T131&apos;s
          diagnosis (the comb dominates the pole in the norm, 4.7–81×; the
          rest is a localisation statement). T135 · COMB.COMPRESS
          (BOUNDED-STATE, 13/13) ported the T116 Riccati machinery verbatim
          to the seam DtN and found the bounded faithful state the Weil
          window provably lacks — m_cert = 12, from the pre-declared set
          {'{8, 12, 16, 24, 32}'}, error falling out to h = 1e5 — with the
          honest caveats stated: the driver is weight summability, the value
          is partly circular, and QEC.SEAM.01 is not advanced. T136 ·
          M.MATRIX.PAIR (ONE-CARRIES, 30/30) closed one of the M-matrix
          question&apos;s three items outright — Varga&apos;s regular splitting
          makes ρ(J) = τ/(1+τ) an identity and the Collatz–Wielandt bound at the
          anchor vector is sharp to 1.00–1.03 on 900/900, flat in D and in the
          zone — while the exact split λ_min ~ D^−0.56 × D^2.72 × D^0.12 puts the
          whole degradation in the margin and M17 closes negatively (the bad
          subspace is delocalised). T137 · LONG.LAG (BOTH-RESIST, 22/22) made
          the support explicit — anti-diagonal comb stripes at the prime-power
          atoms, each a perfect matching, amplitude certified — and certified
          the whole absolute-value envelope family DEAD from below
          (ρ(|E|) ≥ 1.32 on 35/35), leaving one named residue: a sign-preserving
          bound. Thirteen statements from both parts are promoted as v543 and
          v544. T138 · SIGN.COMPENSATION (PAIR-EXACT, 26/26) found the
          mechanism: the coupling sign follows the interval geometry of the
          two edges, and the m-paired Neumann certificate removes the
          arithmetic wall on all 77 dead blocks (pool 563 → 875/900) — the
          margin question returns one level down as ρ(W_S). T139 · GREEN.DECAY
          (DENSE-RESISTS, 30/30) refuted the classical decay lemma at its
          hypothesis, arithmetically — while deriving T138&apos;s sign law from
          one exact telescoping identity and killing the layer series from
          below; the core shrinks to one signed inequality at stripe distance
          b ≤ 16. T140 · SIGNED.BAND (FINITE-CORE, 31/31) attacked exactly
          that inequality and gave it an exact finite core per zone: the
          telescope identity lifts to the form level (Gram = CHCᵀ exactly,
          rank ≤ h−1), ρ(W) = λ_max(K^½HK^½) with K a closed-geometry
          coverage kernel and H a mass-plus-Dirichlet form, the checkerboard
          split replaces the O(nb) Weyl steps by three D-independent ones
          (R2 solved), and all the D-dependence sits in the geometry
          (blocks ~ D^0.13, λ_max(K) ~ D^−2.99); what remains is a
          zone-uniform discrete Hardy inequality. T141 · DISCRETE.HARDY
          (HARDY-RESISTS, 22/22) attacked that ingredient: four exact
          identities put it in classical two-weight shape, but the certified
          constant is not zone-uniform (D^−0.366 ± 0.036 against a bar of
          0.25) while the exact object it bounds is (D^−0.229 ± 0.007) — the
          growth is manufactured by the diagonal profile — the additive shape
          is dead as a shape at its own exact Weyl floor (1.694–3.855× the
          target), and the joint shape fails at the normalisation alone
          (Ω = 20.71–2723.99). The residue collapses to one closed conductance
          profile with Y ⪯ K⁺ and Ω ≈ 1; the identity blocks of both parts are
          promoted as v545. T142 · CONDUCTANCE.PROFILE (PROFILE-RESISTS,
          24/24) then constructed that profile instead of guessing it: the
          capacity decomposition K⁻¹ = DᵀJ⁻¹D + xxᵀ/cap exhibits the optimal
          Hardy weight exactly — Ω = 1 exactly by a projection identity,
          against T141&apos;s guessed 20.7–2724 — the certified chain misses
          by a constant factor 2.27–2.45 (flat in D), and the rank ladder
          closes the whole comparison path: no comparison argument can
          deliver D-uniformity, so the next move is the sharp
          capacity-Rayleigh route. T143 · SHARP.CAPACITY (SHARP-CARRIES,
          24/24) then ran exactly that route, and it carries: the exact
          capacity-Rayleigh form is an identity on all 26 windows (with a
          structurally new bookkeeping — the minimiser orthogonal to the
          equilibrium charge, the mass share negative, the gap a
          cancellation of two O(1) shares, the naive split certified dead
          at 6–67× ρ), Maz&apos;ya&apos;s capacity criterion applied to the
          gap form lands inside its window [1/4, 1] on 26/26
          (Φ_sup·λ = 0.5438–0.6457) for a non-Markovian form, with a
          zone-uniform loss factor (D^−0.048 ± 0.010); the supremum lives
          on closed families — in node coordinates plain INTERVALS dominate
          by 8.3–129.5 (Muckenhoupt&apos;s one-dimensional structure) — and
          is certified by full enumeration on 6 border blocks, while
          Miclo&apos;s constructive chain loses 46–2561× (the conclusion
          holds, the classical proof mechanism does not). D-uniformity is
          reduced to one named inequality — cap_E(A) ≥ |A|·λ₀/c₀ with an
          absolute c₀. T144 · CAPACITY.INEQUALITY (INTERVAL-CARRIES, 31/31)
          then ran the interval route at exactly that inequality, and it
          carries: the interval class is exhausted exactly on every window
          (11,390,676 intervals via a Cholesky prefix-sum identity, verified
          to 1e-11), the closed two-weight sup lands inside the Maz&apos;ya
          window on the whole surface and flat in D (B_res·λ̂ =
          0.6694–0.7813, D^0.013 ± 0.005, coordinate-robust against
          T143&apos;s 0.5438–0.6457), the pointwise hull comparison is FALSE
          (up to 425, D^−1.137) while the best-interval comparison is
          zone-uniform (c_glob = 1.0000–1.6876, exact on the enumerated
          blocks), the family restriction falls entirely — the
          Cauchy–Schwarz floor makes Φ_sup a maximum-density-subgraph value
          (Charikar 2000; Goldberg 1984), so all 2^m sets are covered with a
          cited absolute constant (Ψ_all·λ̂ = 0.7399–0.8515, the flattest
          number of the probe) — and the Markov perturbation route is
          certified dead (λ_min(E−P) &lt; 0 everywhere; the positive
          couplings carry 36.7–64.5% of the off-diagonal mass). The
          certified chain λ ≥ 1/(c₀·κ_up·c_glob·B_res) delivers
          0.1002–0.2653 of the exact gap per window with exactly ONE
          unproven input — the absolute Maz&apos;ya constant c₀, whose
          sharpest shape S1′ is a capacitary strong-type inequality under a
          Green mean-density bound, a Muckenhoupt-type rather than a
          Markov-type hypothesis — and T145 (mazya_proof_probe.py) is
          running at exactly S1′.
        </p>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The convergence is a measured typing of where the hardness sits — not
        progress on it. Sandbox; not RH evidence.
      </p>
    </div>
  );
}
