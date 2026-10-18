import Link from "next/link";
import { SCRIPT_TOTAL } from "@/lib/suite";
import { VerbatimRecap } from "./VerbatimRecap";

export function HonestyBanner() {
  return (
    <aside
      role="note"
      aria-label="Research honesty notice"
      className="relative overflow-hidden rounded-2xl border border-amber-400/40 bg-gradient-to-br from-amber-500/15 via-slate-50/80 to-slate-50/90 p-5 sm:p-6"
    >
      <div
        aria-hidden
        className="pointer-events-none absolute -right-8 -top-8 h-32 w-32 rounded-full bg-amber-400/10 blur-2xl"
      />
      <p className="font-mono text-[10px] font-semibold uppercase tracking-[0.2em] text-amber-700">
        Honesty first
      </p>
      <p className="mt-2 max-w-3xl text-sm leading-relaxed text-amber-900/95 sm:text-base">
        Research diary. Everything here is exploratory sandbox work unless
        explicitly marked as machine-verified (currently:{" "}
        <Link
          prefetch={false}
          href="/verification"
          className="font-mono text-emerald-700 underline decoration-emerald-400/40 underline-offset-2 hover:text-emerald-800"
        >
          v535–v970 on this front
        </Link>
        , inside an {SCRIPT_TOTAL}-script suite, all green). One
        identification theorem
        is closed on this front (W1, after a same-day erratum); the RH-hard
        step (W3, uniform positivity) is open, and closing W1 does not move
        it.{" "}
        <strong className="font-semibold">
          No claim of progress toward the Riemann Hypothesis is made.
        </strong>
      </p>
      <p className="mt-3 max-w-3xl text-sm leading-relaxed text-amber-900/80">
        How this discipline works — the sandbox firewall, the kill criteria
        declared before execution, the graveyard of buried coincidences, and
        the suite module that measures all of it (v649) — is documented on{" "}
        <Link
          prefetch={false}
          href="/method"
          className="font-semibold text-emerald-700 underline decoration-emerald-400/40 underline-offset-2 hover:text-emerald-800"
        >
          The verification framework
        </Link>
        .
      </p>
      <details className="group mt-4">
        <summary className="cursor-pointer list-none font-mono text-[11px] uppercase tracking-[0.18em] text-amber-700/80 transition-colors hover:text-amber-800">
          <span
            aria-hidden
            className="mr-1.5 inline-block transition-transform group-open:rotate-90 motion-reduce:transition-none"
          >
            ▸
          </span>
          The full status paragraph (v535–v648), preserved verbatim
        </summary>
        <p className="mt-3 max-w-3xl text-sm leading-relaxed text-amber-900/80">
          The sprint T102–T125
          compressed the remaining arithmetic bound to one sign plus one declared
          accounting convention; phase 2 (T126–T176) closed its measurement
          programme as planned and stands as a certified map with one open
          object (R1, classified as a near-degeneracy, not a size). Since then
          the diary runs as backflow rounds: the uniform constant C = 1,
          exception-free on the complete surface (v618/v619); the Lorentz
          congruence identifying the prime determinant form with the cover
          polarization lattice, and the Hodge chamber it buys (v624/v627,
          v635–v637); E₈ as a literal error-correcting code with a
          compiler-native bit dictionary (v626/v638); the sixty-line reflection
          group G31 with the order-coincidence numerology killed (v633/v634);
          and the Suzuki W1 identification — atom layer literal, smooth layer
          derived, portable and closed at the matrix level (v630/v631,
          v640–v642), then corrected by a same-day erratum and proved as a
          measure-level theorem (v643: Suzuki&apos;s eq. (1.3) carries Lerch
          +1/4, not −1; every measured number transfers verbatim, the true
          dictionary is the single scalar +1/D with κ = 0), with W2 started
          (v644) and the W3 sign-uncertainty toolbox typed as not
          transferring at d = 1 (v648). Honest fence: closing W1 does not
          move W3 (uniform positivity, the RH-hard step). No claim of
          progress toward the Riemann Hypothesis is made.
        </p>
      </details>
      <VerbatimRecap
        id="sprintPhase2"
        tone="amber"
        className="mt-2"
        label="The full sprint + phase-2 recap (T102–T176), preserved verbatim"
      />
    </aside>
  );
}
