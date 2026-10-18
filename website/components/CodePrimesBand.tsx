import Link from "next/link";
import { ArrowRight, Binary, Hash, Radio } from "lucide-react";
import { SectionHeader } from "./SectionHeader";

/**
 * Two independent 2026-08 readings of the same E₈ object — as a literal
 * error-correcting code (E8.CODE.01) and as the geometry whose shadow is the
 * primes (PRIME.SHADOW.01) — plus the first measured contact with the Weil
 * operator (PRIME.WEIL.CONTACT/DICT). Honest typing throughout: theorems are
 * called theorems, readings are typed [C], and the RH-hard steps are named
 * open — no RH claim anywhere.
 */

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
  {
    icon: Hash,
    kicker: "The primes",
    title: "Primes are the shadow of the finished geometry",
    items: [
      {
        marker: "[E]",
        text: "The E₈ theta series is the Eisenstein series E₄: shell counts 240·σ₃(n), multiplicative over coprime addresses — the 'address space' reading is unique factorization.",
      },
      {
        marker: "[E]",
        text: "Primes act as commuting Hecke channels — T_p Θ = (1 + p³) Θ — with the compiler's theta as simultaneous eigenvector.",
      },
      {
        marker: "[E]",
        text: "L(E₄, s) = ζ(s) ζ(s − 3): the zeta function is the factorized shadow of the E₈ counting function. Primes enter after the geometry, not before.",
      },
    ],
    scope: "Classical Jacobi/Hecke facts, realized verbatim by the compiler's own objects; the speculative framings stay typed hypotheses.",
    refs: "v625",
    tone: "border-emerald-400/25 bg-emerald-500/[0.04]",
  },
  {
    icon: Radio,
    kicker: "The operator",
    title: "First contact with the Weil operator — no RH claim",
    items: [
      {
        marker: "[E]",
        text: "The atom layer of the TFPT window form is Suzuki's prime measure, literally: positions log(prime powers), weights Λ(n)/√n — exact, atom by atom.",
      },
      {
        marker: "[E]/[C]",
        text: "The smooth half closes through an exact Lerch dictionary — corrected by a same-day erratum (eq. (1.3) carries +1/4, not −1; every number transfers verbatim) to the single scalar +1/D — and W1 is proved as a measure-level theorem: A_arch = −g″_smooth exactly, κ = 0, form equality 1.28e−10.",
      },
      {
        marker: "[O]",
        text: "Honest scope: W2 is started (density slices measured, Mosco remainder named), W3 — uniform positivity, the RH-hard step — stays open (the sign-uncertainty toolbox provably does not transfer at d = 1), and closing W1 does not move it. No RH statement anywhere.",
      },
    ],
    scope: "A window-portable operator identification inside a preregistered research contract (PRIME.WEIL.OPERATOR.01) — typed, killable, and explicitly not a Riemann-hypothesis claim.",
    refs: "v630 · v631 · v640–v644 · v648",
    tone: "border-amber-400/25 bg-amber-500/[0.04]",
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
          eyebrow="Two new readings"
          title="The code and the primes"
          description="Two independent 2026-08 results read the same E₈ hull in new ways: one as a literal error-correcting code, one as the finished geometry whose arithmetic shadow is the primes — with a first measured contact to the Weil operator. Exact where stated, typed where they are readings."
        />

        <div className="mt-8 grid gap-4 lg:grid-cols-3">
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
