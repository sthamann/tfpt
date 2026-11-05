"use client";

import { motion } from "motion/react";
import { CheckCircle2, XCircle } from "lucide-react";
import { Math } from "@/components/Math";
import { SectionHeader } from "@/components/SectionHeader";

const CLAIMS = [
  "TFPT starts with P1, a structured primitive reflection-positive boundary kernel, and P2, its declared physical 3+2 readout. c₃ = 1/(8π) is a normalization of P1. The common four-mark geometry, anchor and finite W-bridge already provide conditional derivations; the original operative source includes state and time (REC20261105C3).",
  "The carrier gives D₅, the family geometry gives A₃, and the μ₄ glue closes E₈ = (D₅ ⊕ A₃) + μ₄ as a lattice theorem — 240 = 16·5·3, 248 = 240 + 8 are carrier traces.",
  "α⁻¹ = 137.0359992168 is the unique root of a parameter-free cubic (existence + uniqueness proved), and the flavor matrix, masses and θ₁₂ = 1/3 − φ₀/2 follow from one φ₀-ladder.",
  "The common divisor gives family rank three and five carrier modes. Anchor, Pascal and E₈ closure further constrain these data. v1014/v1015 close both finite W-bridge premises modulo MMST identification; the physical source and readout retain their declared scope.",
];

const NOT_CLAIMS = [
  "E₈ is the unimodular audit/compiler hull, not an unbroken physical gauge group — so the no-go results against literal E₈ world-formulas do not apply.",
  "The dimensionful EW/QCD masses (m_W, m_Z, m_H, sin²θ_W, α_s) sit on the RG scheme layer; the absolute quark amplitude scale reduces to the U_point anchor.",
  "The frontier items — η_B, m_p/m_e, Koide, dark matter — are honest handles, not forced compiler powers, now runnable typed solvers (F_transfer = F_pole ⊕ F_Boltzmann ⊕ F_relic ⊕ F_QCD, v371–v374) with kill tests; the classical covariant field equation carries no free dimensionless Newton coupling under the named QFT/entanglement premises [C] (Gₐᵦ + Λgₐᵦ = c₃⁻¹Tₐᵦ, both coefficients fixed under those premises).",
  "No strict physical TOE is certified end-to-end. The MMST seam route is closed modulo its cited theorems; the later charged master theorem states its ALG-EXH and concrete field-identification premises. Its net/KMS rigidity result does not identify the full P1 determinant response with an additive four-channel response. The unconditional SEAM.EQUIV.01 parent and the twistor route retain [O]. The scale interface is a closed metrological R₊ torsor requiring one dimensionful calibration (v153/v725), while dimensionless hierarchy predictions remain obligations. TFPT.TOE.COMPLETE.01 names the conjunction T1–T8; finite compiler closure does not close that whole physical goal. The historical ambient-measure redundancy claim (v369/v379) retains its stated conditional scope.",
];

export function WhatTfptClaims() {
  return (
    <section
      id="claims"
      className="relative scroll-mt-24 py-20 sm:py-24"
      aria-labelledby="claims-heading"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          eyebrow="What TFPT claims"
          title="One compiler, not a list of fits"
          description="The introduction makes two things explicit: what TFPT does claim at the compiler level, and what it explicitly does not promote past its grade. The split is what makes the falsification surface auditable."
        />

        <div className="mt-12 grid gap-5 lg:grid-cols-2">
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.05 }}
            transition={{ duration: 0.6 }}
            className="rounded-2xl border border-emerald-400/20 bg-emerald-500/5 p-6"
          >
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-emerald-500/15 ring-1 ring-emerald-400/30">
                <CheckCircle2 size={18} className="text-emerald-700" />
              </div>
              <h3 className="font-serif text-xl font-semibold text-slate-950">
                Claimed at the primitive level
              </h3>
            </div>
            <ul className="mt-5 space-y-3 text-sm leading-relaxed text-slate-700">
              {CLAIMS.map((c, i) => (
                <li key={i} className="flex gap-3">
                  <span
                    className="mt-1.5 h-1.5 w-1.5 flex-none rounded-full bg-emerald-400"
                    aria-hidden
                  />
                  <span>{c}</span>
                </li>
              ))}
            </ul>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 16 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.05 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="rounded-2xl border border-orange-400/20 bg-orange-500/5 p-6"
          >
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-orange-500/15 ring-1 ring-orange-400/30">
                <XCircle size={18} className="text-orange-700" />
              </div>
              <h3 className="font-serif text-xl font-semibold text-slate-950">
                Not claimed at this level
              </h3>
            </div>
            <ul className="mt-5 space-y-3 text-sm leading-relaxed text-slate-700">
              {NOT_CLAIMS.map((c, i) => (
                <li key={i} className="flex gap-3">
                  <span
                    className="mt-1.5 h-1.5 w-1.5 flex-none rounded-full bg-orange-400"
                    aria-hidden
                  />
                  <span>{c}</span>
                </li>
              ))}
            </ul>
          </motion.div>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.05 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="mt-10 rounded-2xl border border-slate-300/40 bg-slate-50/40 p-6 sm:p-8"
        >
          <h3 className="font-serif text-lg font-semibold text-slate-950">
            The source and its numerical readouts
          </h3>
          <p className="mt-2 max-w-3xl text-sm leading-relaxed text-slate-700">
            P1 contains the primitive boundary kernel; its normalization is c₃.
            The same marked divisor supplies three cycle directions and five
            meromorphic modes. The typed anchor a = (1,1,2) relates these data
            through e₁ = 4 and e₂ = 5. The later A₀⋆ descent establishes finite
            S₄ monodromy and mathematical unitarizability. Matching that module
            and its metric to the physical source remains a separate step.
          </p>
          <div className="mt-5 grid gap-3 lg:grid-cols-2">
            <div className="rounded-lg border border-slate-300/40 bg-slate-50/60 p-4">
              <div className="text-[10px] font-semibold uppercase tracking-widest text-blue-700/80">
                P1 kernel: its normalization
              </div>
              <div className="mt-2 overflow-x-auto">
                <Math block>
                  {"c_3 = \\frac{1}{|\\mathbb{Z}_2|\\oint_{S^2}K\\,dA} = \\frac{1}{8\\pi}"}
                </Math>
              </div>
            </div>
            <div className="rounded-lg border border-slate-300/40 bg-slate-50/60 p-4">
              <div className="text-[10px] font-semibold uppercase tracking-widest text-blue-700/80">
                P2: declared physical readout
              </div>
              <div className="mt-2 overflow-x-auto">
                <Math block>
                  {"g_{\\mathrm{car}} = 5 = 3 + 2, \\quad \\dim S^+ = 2^{g-1} = 16"}
                </Math>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
