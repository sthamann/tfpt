"use client";

import { useEffect, useRef } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";
import type { TourStepMeta } from "./tourData";

interface TourNavProps {
  steps: readonly TourStepMeta[];
  activeIndex: number;
  onGo: (index: number) => void;
  onPrev: () => void;
  onNext: () => void;
}

/**
 * Sticky mobile-first stepper: numbered steps + prev/next.
 * Deep links use #step-<id> anchors owned by TourShell.
 */
export function TourNav({
  steps,
  activeIndex,
  onGo,
  onPrev,
  onNext,
}: TourNavProps) {
  const stepListRef = useRef<HTMLOListElement>(null);
  useEffect(() => {
    const list = stepListRef.current;
    const button = list?.querySelector<HTMLButtonElement>('[aria-current="step"]');
    if (!list || !button) return;
    const left = button.offsetLeft;
    if (left < list.scrollLeft || left + button.offsetWidth > list.scrollLeft + list.clientWidth) {
      list.scrollLeft = Math.max(0, left - (list.clientWidth - button.offsetWidth) / 2);
    }
  }, [activeIndex]);
  const atStart = activeIndex <= 0;
  const atEnd = activeIndex >= steps.length - 1;
  const active = steps[activeIndex];

  return (
    <nav
      aria-label="Tour steps"
      className="sticky top-16 z-30 border-b border-slate-200/80 bg-slate-50/90 backdrop-blur-md"
    >
      <div className="mx-auto flex max-w-3xl items-center gap-2 px-3 py-2.5 sm:px-4">
        <button
          type="button"
          onClick={onPrev}
          disabled={atStart}
          aria-label="Previous step"
          className="inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-lg border border-slate-300/60 text-slate-800 transition-colors hover:bg-slate-200/80 disabled:cursor-not-allowed disabled:opacity-30"
        >
          <ChevronLeft size={18} aria-hidden />
        </button>

        <div className="min-w-0 flex-1">
          <div className="flex items-center justify-between gap-2">
            <p className="truncate text-[11px] font-semibold uppercase tracking-widest text-blue-700/90">
              Step {active.n} / {steps.length}
            </p>
            <p className="hidden truncate text-xs text-slate-600 sm:block">
              {active.short}
            </p>
          </div>
          <ol ref={stepListRef} className="relative mt-1 flex items-center gap-1 overflow-x-auto overscroll-x-contain pb-1">
            {steps.map((s, i) => {
              const done = i < activeIndex;
              const current = i === activeIndex;
              return (
                <li key={s.id} className="shrink-0">
                  <button
                    type="button"
                    onClick={() => onGo(i)}
                    aria-label={`${s.n}. ${s.short}`}
                    aria-current={current ? "step" : undefined}
                    title={s.short}
                    className={cn(
                      "flex h-11 w-11 items-center justify-center rounded-lg border text-sm font-semibold transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-700",
                      current && "border-blue-700 bg-blue-700 text-white",
                      done && !current && "border-emerald-700 bg-emerald-50 text-emerald-800",
                      !done && !current && "border-slate-300 bg-white text-slate-700 hover:bg-slate-100",
                    )}
                  >
                    {s.n}
                  </button>
                </li>
              );
            })}
          </ol>
        </div>

        <button
          type="button"
          onClick={onNext}
          disabled={atEnd}
          aria-label="Next step"
          className="inline-flex h-11 w-11 shrink-0 items-center justify-center rounded-lg border border-slate-300/60 text-slate-800 transition-colors hover:bg-slate-200/80 disabled:cursor-not-allowed disabled:opacity-30"
        >
          <ChevronRight size={18} aria-hidden />
        </button>
      </div>
      <p className="sr-only">Use left and right arrow keys to move between steps.</p>
    </nav>
  );
}
