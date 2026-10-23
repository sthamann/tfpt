import { SectionHeader } from "./SectionHeader";

const LINES = [
  { plain: "Two starting assumptions specify a seam normalization c₃ = 1/(8π) and a carrier rank of five.", href: "/papers/architecture-e8", source: "Inputs and E₈ construction" },
  { plain: "A lattice construction joins D₅ and A₃ through their discriminant data to obtain E₈ under the stated assumptions.", href: "/papers/e8-audit-bootstrap", source: "Lattice audit and bootstrap" },
  { plain: "The compiler relates this structure to Standard Model representations, flavor readouts and an electromagnetic fixed-point equation.", href: "/papers/standard-model", source: "Standard Model and flavor" },
  { plain: "The published checks test specific mathematical and numerical claims. Physical interpretations and remaining derivations have separate status in the ledger.", href: "/verification", source: "Reproduce a claim and inspect its status" },
];

/**
 * Four-line plain-English mechanism — no μ₄ / seam jargon in the lead sentence.
 * Technical terms appear in parentheses after the everyday reading.
 */
export function InOneBreath() {
  return (
    <section
      id="in-one-breath"
      className="relative scroll-mt-20 border-t border-slate-200/60 py-14 sm:py-16"
      aria-labelledby="in-one-breath-heading"
    >
      <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="in-one-breath-heading"
          eyebrow="Mechanism"
          title="How does TFPT work?"
          description="Follow the construction from its inputs to the published papers and reproducible evidence."
        />
        <ol className="mt-8 space-y-0 border border-slate-300/50 bg-slate-50/50">
          {LINES.map((line, i) => (
            <li
              key={line.plain}
              className="flex gap-3 border-b border-slate-200/70 px-4 py-3.5 last:border-b-0 sm:gap-4 sm:px-5"
            >
              <span className="mt-0.5 font-mono text-[11px] font-semibold text-slate-600">
                {String(i + 1).padStart(2, "0")}
              </span>
              <p className="text-sm leading-relaxed text-slate-800 sm:text-[15px]">
                {line.plain}
                {" "}<a href={line.href} className="text-blue-800 underline underline-offset-2">{line.source} →</a>
              </p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
