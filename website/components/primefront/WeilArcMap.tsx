"use client";

import { motion } from "motion/react";

const BEATS = [
  {
    id: "T51–53",
    title: "Reframe",
    detail: "Family + relative trace formula — not one operator.",
    tone: "step" as const,
  },
  {
    id: "T51",
    title: "Infinite carrier",
    detail: "Waldspurger family kernel K_D: rank grows 8→192, no collapse.",
    tone: "step" as const,
  },
  {
    id: "T55",
    title: "Self-generating space",
    detail: "Positive RTF pairing builds ℓ²(d, b²/|d|) by GNS.",
    tone: "step" as const,
  },
  {
    id: "T57",
    title: "Both infinities",
    detail: "Double series Z(s,w): p-towers + d-family in one identity.",
    tone: "step" as const,
  },
  {
    id: "T61–62",
    title: "Exact GL(1) core",
    detail: "Trivial Sato–Tate isotype = G₀; fibre twist-mix ≈ 0.",
    tone: "step" as const,
  },
  {
    id: "T63",
    title: "Two obstructions named",
    detail: "Q_fam = 2Q_ζ − 2Q_ζ(♭) + Arch + Corr — minus + extra term.",
    tone: "obstruction" as const,
  },
  {
    id: "T64",
    title: "One resolved",
    detail: "Corr = det/det₂ Jacobian (Hilbert–Carleman). Minus stays.",
    tone: "resolved" as const,
  },
  {
    id: "T65–66",
    title: "π-front closed",
    detail: "Digits uniform / placebos null; primes are arithmetic, not π-noise.",
    tone: "resolved" as const,
  },
  {
    id: "T67–69",
    title: "Square level closes",
    detail: "Dirac exact; every coefficient square deletes (Cauchy–Littlewood).",
    tone: "resolved" as const,
  },
  {
    id: "T70–71",
    title: "Linear plus-carrier",
    detail: "Θ = −48 L(−1,χ_d); plus-only ζ-balance; FE exact.",
    tone: "step" as const,
  },
  {
    id: "T72",
    title: "Gap = λ*",
    detail:
      "Cone library saturates 5/24; residual is λ* on n ≡ 6 mod 8 (promoted: v540).",
    tone: "obstruction" as const,
  },
  {
    id: "T73–75",
    title: "Doors A/B furnished",
    detail: "Spectral sign-blindness + R1–R5; λ* closed form with own FE.",
    tone: "step" as const,
  },
  {
    id: "T76",
    title: "Universal recipe",
    detail: "Hybrid 91/91; Matching Lemma named; transport wall open.",
    tone: "obstruction" as const,
  },
  {
    id: "T77–78",
    title: "Lemma window-proved",
    detail: "Matching Lemma machine-proved on [4, 10⁶]; tail ingredient named.",
    tone: "resolved" as const,
  },
  {
    id: "T79",
    title: "Ledger closes",
    detail: "Wall = I5 (prime↔arch coupling), typed ⟺ Weil positivity ⟺ RH.",
    tone: "obstruction" as const,
  },
  {
    id: "T80",
    title: "Signed tail",
    detail: "Tail to ~10²³; last gap = χ₋₄-coherent class.",
    tone: "resolved" as const,
  },
  {
    id: "T81",
    title: "Avoidance fails",
    detail: "Coherent targets need coherent m — freedom absent on coherent demand.",
    tone: "resolved" as const,
  },
  {
    id: "T82–84",
    title: "Three perspectives",
    detail: "Arch internal; wall FE-transversal; last class = Z[i] home.",
    tone: "step" as const,
  },
  {
    id: "T85",
    title: "λ-channel closes",
    detail:
      "LEMMA-CLOSES-LAMBDA — coherent class closed; 90/90 certificates (core checks promoted: v541).",
    tone: "resolved" as const,
  },
  {
    id: "T86",
    title: "Q-pairing closes",
    detail:
      "LEMMA-FULLY-CLOSED — non-coherent tail paired; remainder = λ-support; all classes covered.",
    tone: "resolved" as const,
  },
  {
    id: "T87–93",
    title: "I5 geography",
    detail:
      "Band map survives self-check; a_neg → 0.7486; finite blocks wrong instrument.",
    tone: "step" as const,
  },
  {
    id: "T94",
    title: "Blind prime demo",
    detail: "753/753 primes, zero errors, no division — structure, not speed.",
    tone: "resolved" as const,
  },
  {
    id: "T95–96",
    title: "Relay confirmed",
    detail: "C1 proved; α* edge withdrawn; handover windows positive.",
    tone: "step" as const,
  },
  {
    id: "T97–98",
    title: "Induction skeleton",
    detail:
      "8 pieces proved; target = D_k ≤ μ_k/2; circular lemma replaced.",
    tone: "step" as const,
  },
  {
    id: "T99–101",
    title: "Induction closeout",
    detail:
      "Zones 2–4 closed; zone-5 tip = equality; asymptotics = bound (A); 2428 checks.",
    tone: "resolved" as const,
  },
  {
    id: "open",
    title: "One object remains: I5",
    detail: "I5 ⟺ RH; hardness localized in arithmetic bound (A) — no RH claim.",
    tone: "open" as const,
  },
] as const;

const TONE = {
  step: {
    ring: "border-sky-400/40 bg-slate-50 text-sky-800",
    pill: "text-sky-700/80",
    box: "border-slate-300/40 bg-slate-100/50",
  },
  obstruction: {
    ring: "border-amber-400/50 bg-slate-50 text-amber-800",
    pill: "text-amber-700/90",
    box: "border-amber-400/35 bg-amber-500/10",
  },
  resolved: {
    ring: "border-emerald-400/45 bg-slate-50 text-emerald-800",
    pill: "text-emerald-700/90",
    box: "border-emerald-400/30 bg-emerald-500/10",
  },
  open: {
    ring: "border-violet-400/40 bg-slate-50 text-violet-800",
    pill: "text-violet-700/90",
    box: "border-violet-400/30 bg-violet-500/10",
  },
} as const;

export function WeilArcMap() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-6">
      <p className="mb-1 font-mono text-[10px] uppercase tracking-widest text-sky-700/90">
        July 25–26 arc · Teile 51–101
      </p>
      <p className="mb-4 text-xs leading-relaxed text-slate-600">
        <span className="text-amber-800/90">Two isolated</span>
        {" "}
        <span className="font-mono text-[9px] text-emerald-700/80">
          [machine-verified]
        </span>
        {" → "}
        <span className="text-emerald-800/90">v540 / λ* / v541</span>
        {" → "}
        <span className="text-sky-800/90">I5 geography + relay</span>
        {" "}
        <span className="font-mono text-[9px] text-amber-700/80">[sandbox]</span>
        {" → "}
        <span className="text-sky-800/90">induction closeout (T99–T101)</span>
        {" → "}
        <span className="text-violet-800/90">one object remains: I5</span>
        . Geography ≠ attack. Not almost-RH.
      </p>
      <ol className="relative space-y-0">
        <div
          aria-hidden
          className="absolute bottom-3 left-[1.15rem] top-3 w-px bg-gradient-to-b from-sky-400/50 via-amber-400/40 to-violet-400/40"
        />
        {BEATS.map((b, i) => {
          const t = TONE[b.tone];
          return (
            <motion.li
              key={b.id}
              initial={{ opacity: 0, x: -10 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.35 }}
              transition={{ duration: 0.4, delay: i * 0.06 }}
              className="relative flex gap-4 pb-4 last:pb-0"
            >
              <span
                className={`relative z-10 mt-1 flex h-9 w-9 shrink-0 items-center justify-center rounded-full border font-mono text-[10px] ${t.ring}`}
              >
                {i + 1}
              </span>
              <div className={`min-w-0 flex-1 rounded-xl border px-3 py-2.5 ${t.box}`}>
                <div className="flex flex-wrap items-baseline gap-x-2 gap-y-1">
                  <span className="font-mono text-[10px] text-slate-600">
                    {b.id}
                  </span>
                  <span className="font-serif text-base text-slate-900">
                    {b.title}
                  </span>
                  <span
                    className={`ml-auto font-mono text-[9px] uppercase tracking-wider ${t.pill}`}
                  >
                    {b.tone === "obstruction"
                      ? "NAMED"
                      : b.tone === "resolved"
                        ? "RESOLVED"
                        : b.tone === "open"
                          ? "OPEN"
                          : "SANDBOX"}
                  </span>
                </div>
                <p className="mt-1 text-sm leading-relaxed text-slate-600">
                  {b.detail}
                </p>
              </div>
            </motion.li>
          );
        })}
      </ol>
    </div>
  );
}
