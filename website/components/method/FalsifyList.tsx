import Link from "next/link";
import { ArrowRight } from "lucide-react";

/**
 * "What would falsify this" — the standing kill criteria of the open
 * contracts and the frozen prediction registry. Concrete thresholds live on
 * the kill board (/falsification) and in the contract rows of the ledger.
 */

const CRITERIA: { title: string; body: string; refs: string }[] = [
  {
    title: "JUNO measures θ₁₂ outside the frozen band",
    body: "Exactly one solar-angle prediction of record is frozen (sin²θ₁₂ = 0.306747, registry frozen 2026-06-09, re-derived from the two axioms on every suite run). A JUNO result outside the declared band kills the neutrino texture.",
    refs: "REG.FREEZE.01 · v84",
  },
  {
    title: "A tensor ratio far from r ≈ 0.0037",
    body: "The scalaron sector predicts r inside the declared N★ band. CMB-S4 / LiteBIRD sensitivity reaches it; a detection well outside the band kills the inflation readout.",
    refs: "freeze file · v65 / v86",
  },
  {
    title: "A fresh complete window breaks C = 1",
    body: "The W3 candidate mechanism (kill test K2 of the Weil-operator contract) dies if a complete fresh window stably exceeds the frozen C = 1 bound — the complete-comb surface is definitional, so there is no room to re-fit.",
    refs: "PRIME.WEIL.OPERATOR.01 · v618 / v619",
  },
  {
    title: "The operator identification fails beyond a fit",
    body: "Kill test K1: if the window form is not the Galerkin matrix of the localized Weil operator on the declared bases (exactly, or up to the named rank-one transform), the W1–W4 chain is dead. K3: losing the explicit-formula bookkeeping in the odd sector kills it too.",
    refs: "PRIME.WEIL.OPERATOR.01 · v631 / v643",
  },
  {
    title: "Strong-CP, ordering, or w ≠ −1",
    body: "The remaining frozen criteria of the falsification surface: a strong-CP signal inconsistent with the null, an inverted neutrino ordering, or dark energy measurably away from w = −1 each kill their sector outright.",
    refs: "freeze file · v65",
  },
];

export function FalsifyList() {
  return (
    <div>
      <ul className="grid gap-4 md:grid-cols-2">
        {CRITERIA.map((c) => (
          <li
            key={c.title}
            className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-5"
          >
            <h3 className="text-sm font-semibold text-slate-900">{c.title}</h3>
            <p className="mt-2 text-sm leading-relaxed text-slate-600">
              {c.body}
            </p>
            <div className="mt-3 font-mono text-[11px] text-slate-600">
              {c.refs}
            </div>
          </li>
        ))}
        <li className="flex items-center justify-center rounded-2xl border border-dashed border-slate-300/50 bg-slate-50/30 p-5">
          <Link
            prefetch={false}
            href="/falsification"
            className="inline-flex items-center gap-1.5 text-sm font-semibold text-rose-800 underline decoration-rose-400/40 underline-offset-2 hover:text-rose-800"
          >
            The full kill board with thresholds
            <ArrowRight size={14} aria-hidden />
          </Link>
        </li>
      </ul>
    </div>
  );
}
