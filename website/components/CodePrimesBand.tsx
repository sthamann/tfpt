import Link from "next/link";
import { ArrowRight, Binary } from "lucide-react";
import { SectionHeader } from "./SectionHeader";

/** The exact E8/Hamming code result retained within TFPT. */

const MARKER_TONE: Record<string, string> = {
  "[E]": "text-emerald-800 bg-emerald-500/15 ring-emerald-400/30",
  "[C]": "text-amber-800 bg-amber-500/15 ring-amber-400/30",
  "[E]/[C]": "text-amber-800 bg-amber-500/15 ring-amber-400/30",
  "[O]": "text-rose-800 bg-rose-500/15 ring-rose-400/30",
};

interface CardItem {
  marker: string;
  text: string;
}

interface Card {
  icon: typeof Binary;
  kicker: string;
  title: string;
  items: CardItem[];
  scope: string;
  refs: string;
  tone: string;
}

const CARDS: Card[] = [
  {
    icon: Binary,
    kicker: "The code",
    title: "E₈ is an error-correcting code — a theorem",
    items: [
      {
        marker: "[E]",
        text: "Construction A on the self-dual extended Hamming code [8,4,4] yields E₈ exactly — shell counts 240 and 2160 reproduce the compiler's theta series.",
      },
      {
        marker: "[E]",
        text: "Every single-bit error is exhaustively correctable: all 16 × 8 corrupted words decode to a unique nearest codeword.",
      },
      {
        marker: "[E]",
        text: "The bit dictionary is exact: the unique compiler-equivariant placement is Reed–Muller RM(1,3), with one information bit per μ₄ pair — three families plus one anchor — and decoding as literal projection.",
      },
      {
        marker: "[C]",
        text: "The compiler ties are typed, not oversold: 8 = rank E₈, 4 = code distance = |μ₄|, 16 = the half-spinor count.",
      },
    ],
    scope: "A lattice/coding theorem about the compiler's own hull — no physics claim rides on the reading. Only 2 of 30 code placements carry the equivariant structure; the naive placement fails it — published, not buried.",
    refs: "v626 · v638",
    tone: "border-cyan-400/25 bg-cyan-500/[0.04]",
  },

];

export function CodePrimesBand() {
  return (
    <section
      id="code-primes"
      className="relative scroll-mt-20 py-14 sm:py-16"
      aria-labelledby="code-primes-heading"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="code-primes-heading"
          eyebrow="The compiler hull"
          title="E₈ as an error-correcting code"
          description="Construction A connects the E₈ lattice to the extended Hamming code. Exact coding identities and the physical interpretation retain their separate status."
        />

        <div className="mt-8 grid gap-4 lg:grid-cols-1">
          {CARDS.map((c) => {
            const Icon = c.icon;
            return (
              <article
                key={c.title}
                className={`flex flex-col border p-5 ${c.tone}`}
              >
                <div className="flex items-center justify-between gap-2">
                  <span className="inline-flex items-center gap-2 font-mono text-[10px] font-semibold uppercase tracking-widest text-slate-600">
                    <Icon size={14} className="text-slate-600" aria-hidden />
                    {c.kicker}
                  </span>
                  <span className="font-mono text-[10px] text-slate-600">{c.refs}</span>
                </div>
                <h3 className="mt-3 font-serif text-lg font-semibold leading-snug text-slate-950">
                  {c.title}
                </h3>
                <ul className="mt-3 flex-1 space-y-2.5">
                  {c.items.map((it) => (
                    <li key={it.text} className="flex items-start gap-2">
                      <span
                        className={`mt-0.5 flex-none rounded-sm px-1.5 py-0.5 font-mono text-[10px] font-semibold ring-1 ${
                          MARKER_TONE[it.marker] ?? MARKER_TONE["[E]"]
                        }`}
                      >
                        {it.marker}
                      </span>
                      <span className="text-xs leading-relaxed text-slate-700">
                        {it.text}
                      </span>
                    </li>
                  ))}
                </ul>
                <p className="mt-4 border-t border-slate-200/60 pt-3 text-[11px] leading-relaxed text-slate-600">
                  {c.scope}
                </p>
              </article>
            );
          })}
        </div>

        <div className="mt-6">
          <Link
            prefetch={false}
            href="/verification"
            className="inline-flex items-center gap-1.5 text-sm font-semibold text-blue-700 transition-colors hover:text-blue-800"
          >
            Run these checks in the browser
            <ArrowRight size={14} aria-hidden />
          </Link>
        </div>
      </div>
    </section>
  );
}
