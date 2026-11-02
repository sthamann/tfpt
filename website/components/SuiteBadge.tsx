import Link from "next/link";
import { SCRIPT_TOTAL } from "@/lib/suite";
import { SITE_DATE } from "@/lib/version";
import { cn } from "@/lib/utils";

/**
 * Static per-release suite status. Values are build-time imports from
 * suite.ts / version.ts — not live-fetched. Honest: green for this release cut.
 */
export function SuiteBadge({
  className,
  href = "/verification",
}: {
  className?: string;
  href?: string;
}) {
  const label = `${SCRIPT_TOTAL} registered scripts · publication ${SITE_DATE}`;
  return (
    <Link
      prefetch={false}
      href={href}
      title="Registered script inventory for the publication snapshot. This badge does not report a new test execution."
      className={cn(
        "inline-flex items-center gap-1.5 border border-slate-400/50 bg-slate-50/70 px-2 py-0.5 font-mono text-[10px] tracking-wide text-slate-700 transition-colors hover:border-slate-500 hover:text-slate-900",
        className,
      )}
    >
      <span
        aria-hidden
        className="h-1.5 w-1.5 flex-none rounded-full bg-emerald-400"
      />
      <span>{label}</span>
    </Link>
  );
}
