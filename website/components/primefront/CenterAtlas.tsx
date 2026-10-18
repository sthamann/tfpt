"use client";

import { useState } from "react";
import { cn } from "@/lib/utils";

type AtlasObject = {
  id: string;
  name: string;
  centre: number;
  weight: string;
  note: string;
  channel: "abelian" | "cuspidal" | "other";
};

const OBJECTS: AtlasObject[] = [
  {
    id: "mellin-th3",
    name: "Mellin(θ₃)",
    centre: 0.5,
    weight: "≤1",
    note: "→ π⁻ˢΓ(s)ζ(2s) — classical Riemann θ proof; centre 1/2.",
    channel: "abelian",
  },
  {
    id: "zeta-qi",
    name: "ζ_{ℚ(i)} = ζ L(χ₄)",
    centre: 0.5,
    weight: "1",
    note: "Dedekind zeta of the μ₄-field; FE about 1/2. Abelian drop closed.",
    channel: "abelian",
  },
  {
    id: "rs-ab",
    name: "RS abelian product",
    centre: 1,
    weight: "normed",
    note: "After weight normalisation: shifts {+1,+1,−1,−1} — no ξ-line factor.",
    channel: "abelian",
  },
  {
    id: "epstein",
    name: "E₈ Epstein / total census",
    centre: 2,
    weight: "4",
    note: "Λ_E8(s)=Λ_E8(4−s); fix line Re s = 2 = k/2.",
    channel: "other",
  },
  {
    id: "signed",
    name: "Signed census L-series",
    centre: 2,
    weight: "4",
    note: "ηη − 8L(f₈) — pole-killed; still weight 4.",
    channel: "cuspidal",
  },
  {
    id: "f8",
    name: "L(f₈, s)",
    centre: 2,
    weight: "4",
    note: "Where a_p lives. Needs its own cuspidal bridge — still open.",
    channel: "cuspidal",
  },
];

const TICKS: { centre: number; label: string }[] = [
  { centre: 0.5, label: "½" },
  { centre: 1, label: "1" },
  { centre: 2, label: "2" },
];

/** Map a functional-equation centre in [0, 2] onto the padded track. */
const AXIS_INSET_LEFT = 10;
const AXIS_INSET_RIGHT = 10;
const AXIS_MAX_CENTRE = 2;
const trackPosition = (centre: number) =>
  AXIS_INSET_LEFT +
  (centre / AXIS_MAX_CENTRE) * (100 - AXIS_INSET_LEFT - AXIS_INSET_RIGHT);

/** Labels right of the dot would overflow past this point, so they flip left. */
const LABEL_FLIP_THRESHOLD = 55;

const CHANNEL_STYLE = {
  abelian: {
    dot: "border-violet-300/70 bg-violet-400",
    text: "text-violet-800",
    ring: "ring-violet-300/60",
  },
  cuspidal: {
    dot: "border-rose-300/70 bg-rose-400",
    text: "text-rose-800",
    ring: "ring-rose-300/60",
  },
  other: {
    dot: "border-slate-600/70 bg-slate-600",
    text: "text-slate-700",
    ring: "ring-slate-700/60",
  },
} as const;

const formatCentre = (centre: number) => (centre === 0.5 ? "½" : String(centre));

export function CenterAtlas() {
  const [active, setActive] = useState(OBJECTS[0].id);
  const selected = OBJECTS.find((o) => o.id === active) ?? OBJECTS[0];

  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-violet-700/90">
          Centre atlas · click an object
        </p>
        <ul className="flex gap-3 font-mono text-[10px] text-slate-600">
          <li className="flex items-center gap-1.5">
            <span className="h-1.5 w-1.5 rounded-full bg-violet-400" aria-hidden />
            abelian
          </li>
          <li className="flex items-center gap-1.5">
            <span className="h-1.5 w-1.5 rounded-full bg-rose-400" aria-hidden />
            cuspidal
          </li>
        </ul>
      </div>

      {/* axis */}
      <div className="relative h-5">
        {TICKS.map((tick) => (
          <span
            key={tick.centre}
            style={{ left: `${trackPosition(tick.centre)}%` }}
            className={cn(
              "absolute top-0 -translate-x-1/2 font-mono text-[10px]",
              tick.centre === 0.5 ? "text-violet-700" : "text-slate-600",
            )}
          >
            {tick.label}
          </span>
        ))}
      </div>
      <div className="relative h-1.5 rounded-full bg-slate-200">
        <span
          style={{
            left: `${trackPosition(0)}%`,
            width: `${trackPosition(0.5) - trackPosition(0)}%`,
          }}
          className="absolute inset-y-0 rounded-full bg-gradient-to-r from-transparent to-violet-500/70"
          aria-hidden
        />
      </div>
      <div className="mt-1.5 flex justify-between gap-3 font-mono text-[9px] uppercase tracking-widest text-slate-500">
        <span className="text-violet-700/80">ξ-line · Re s = ½</span>
        <span>weight 4</span>
      </div>

      {/* one lane per object — nothing can overlap */}
      <div className="relative mt-3">
        {TICKS.map((tick) => (
          <span
            key={tick.centre}
            style={{ left: `${trackPosition(tick.centre)}%` }}
            className={cn(
              "absolute inset-y-0 w-px",
              tick.centre === 0.5 ? "bg-violet-500/25" : "bg-slate-300/40",
            )}
            aria-hidden
          />
        ))}

        {OBJECTS.map((o) => {
          const position = trackPosition(o.centre);
          const flipLabel = position > LABEL_FLIP_THRESHOLD;
          const style = CHANNEL_STYLE[o.channel];
          const isActive = active === o.id;
          return (
            <button
              key={o.id}
              type="button"
              aria-pressed={isActive}
              onClick={() => setActive(o.id)}
              className={cn(
                "relative block h-8 w-full rounded-md text-left transition hover:bg-slate-900/[0.04]",
                isActive && "bg-slate-900/[0.06]",
              )}
            >
              <span
                style={{ left: `${position}%` }}
                className={cn(
                  "absolute top-1/2 h-2.5 w-2.5 -translate-x-1/2 -translate-y-1/2 rounded-full border transition",
                  style.dot,
                  isActive && `ring-2 ${style.ring}`,
                )}
                aria-hidden
              />
              <span
                style={
                  flipLabel
                    ? {
                        right: `calc(${100 - position}% + 12px)`,
                        maxWidth: `calc(${position}% - 12px)`,
                      }
                    : {
                        left: `calc(${position}% + 12px)`,
                        maxWidth: `calc(${100 - position}% - 12px)`,
                      }
                }
                className={cn(
                  "absolute top-1/2 -translate-y-1/2 overflow-hidden text-ellipsis whitespace-nowrap font-mono text-[10px] transition",
                  isActive ? style.text : "text-slate-600",
                )}
              >
                {o.name}
              </span>
            </button>
          );
        })}
      </div>

      <div className="mt-3 rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
        <div className="flex flex-wrap items-baseline gap-2">
          <h3 className="font-serif text-lg text-slate-900">{selected.name}</h3>
          <span className="font-mono text-[10px] text-slate-600">
            weight {selected.weight} · centre {formatCentre(selected.centre)}
          </span>
        </div>
        <p className="mt-1 text-sm leading-relaxed text-slate-600">
          {selected.note}
        </p>
      </div>
    </div>
  );
}
