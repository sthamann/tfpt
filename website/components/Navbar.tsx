"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { ChevronDown, Github, Menu, X } from "lucide-react";
import { cn, REPO_URL, PRIME_FRONT_URL } from "@/lib/utils";
import { SITE_VERSION, SITE_DATE, SITE_REV } from "@/lib/version";
import { Logo } from "./Logo";
import { SuiteBadge } from "./SuiteBadge";
import researchSummary from "@/lib/research-summary.json";

const primaryLinks = [
  { href: "/", label: "Start" },
  { href: "/explain", label: "Understand" },
  { href: "/results", label: "Research atlas" },
  { href: "/papers", label: "Papers" },
  { href: "/verification", label: "Verification" },
];

const moreLinks = [
  { href: "/empirical-audit", label: "Empirical audit" },
  { href: "/tour", label: "Guided tour" },
  { href: "/method", label: "Method" },
  { href: "/falsification", label: "Kill board" },
  { href: "/replication", label: "Replication" },
  { href: "/faq", label: "FAQ" },
  { href: PRIME_FRONT_URL, label: "Prime Front ↗" },
  { href: "/orientation", label: "Reading guide" },
  { href: "/documentation", label: "Document library" },
  { href: "/predictions", label: "Predictions" },
  { href: "/architecture", label: "Architecture" },
  { href: "/compiler", label: "Compiler" },
  { href: "/review", label: "For reviewers" },
  { href: "/objections", label: "Objections" },
  { href: "/changelog", label: "Changelog" },
  { href: "/orientation#rosetta", label: "Glossary / Rosetta" },
];

export function Navbar() {
  const pathname = usePathname();
  const isCurrent = (href: string) => href === "/"
    ? pathname === "/"
    : !href.includes("#") && (pathname === href || pathname.startsWith(`${href}/`));
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const [moreOpen, setMoreOpen] = useState(false);
  const moreRef = useRef<HTMLLIElement>(null);
  const mobileButtonRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    if (!moreOpen) return;
    const onDoc = (e: MouseEvent) => {
      if (moreRef.current && !moreRef.current.contains(e.target as Node)) {
        setMoreOpen(false);
      }
    };
    document.addEventListener("mousedown", onDoc);
    return () => document.removeEventListener("mousedown", onDoc);
  }, [moreOpen]);

  useEffect(() => {
    const dismiss = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        if (open) { setOpen(false); mobileButtonRef.current?.focus(); }
        if (moreOpen) { setMoreOpen(false); moreRef.current?.querySelector("button")?.focus(); }
      }
    };
    document.addEventListener("keydown", dismiss);
    return () => document.removeEventListener("keydown", dismiss);
  }, [open, moreOpen]);

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-40 h-16 transition-all duration-300",
        scrolled
          ? "glass-strong backdrop-saturate-200 border-b border-slate-300/40"
          : "bg-white/95 border-b border-slate-200/70",
      )}
    >
      <nav
        aria-label="Primary"
        className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8"
      >
        <div className="flex items-center gap-2.5">
          <Link
            prefetch={false}
            href="/"
            className="group flex min-h-11 min-w-11 items-center"
            aria-label="TFPT home"
          >
            <Logo size={36} />
          </Link>
          <span
            className="hidden shrink-0 select-none items-baseline gap-1.5 whitespace-nowrap border border-slate-300/40 bg-slate-200/50 px-2.5 py-1 font-mono text-[10px] tracking-wide text-slate-600 xl:inline-flex"
            title={`TFPT ${SITE_VERSION}; papers ${SITE_DATE} (build ${SITE_REV}); research snapshot ${researchSummary.generatedAt}`}
          >
            <span className="font-semibold text-slate-700">v{SITE_VERSION}</span>
            <span aria-hidden>·</span>
            <span>Papers <time dateTime={SITE_DATE}>{SITE_DATE}</time></span>
            <span aria-hidden>·</span>
            <span>Research <time dateTime={researchSummary.generatedAt}>{researchSummary.generatedAt.slice(0,10)}</time></span>
          </span>
          <SuiteBadge className="hidden 2xl:inline-flex" />
        </div>

        <ul className="hidden items-center gap-0.5 lg:flex">
          {primaryLinks.map((l) => (
            <li key={l.href}>
              <Link
                prefetch={false}
                href={l.href}
                aria-current={isCurrent(l.href) ? "page" : undefined}
                className="inline-flex min-h-11 items-center whitespace-nowrap rounded-md px-2.5 py-2 text-sm font-medium text-slate-700 transition-colors hover:bg-slate-900/5 hover:text-slate-950 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
              >
                {l.label}
              </Link>
            </li>
          ))}
          <li ref={moreRef} className="relative">
            <button
              type="button"
              onClick={() => setMoreOpen((v) => !v)}
              aria-expanded={moreOpen}
              aria-controls="more-menu"
              className="inline-flex min-h-11 items-center gap-1 whitespace-nowrap rounded-md px-2.5 py-2 text-sm font-medium text-slate-700 transition-colors hover:bg-slate-900/5 hover:text-slate-950"
            >
              More
              <ChevronDown
                size={14}
                className={cn("transition-transform", moreOpen && "rotate-180")}
                aria-hidden
              />
            </button>
            {moreOpen && (
              <ul id="more-menu" className="absolute right-0 top-full mt-1 max-h-[calc(100dvh-5rem)] min-w-[12rem] overflow-y-auto overscroll-contain border border-slate-300/50 bg-slate-50/95 py-1 shadow-xl backdrop-blur">
                {moreLinks.map((l) => (
                  <li key={l.href}>
                    <Link
                      prefetch={false}
                      href={l.href}
                      aria-current={isCurrent(l.href) ? "page" : undefined}
                      onClick={() => setMoreOpen(false)}
                      className="flex min-h-11 items-center px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 hover:text-slate-950 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
                <li>
                  <Link
                    prefetch={false}
                    href={REPO_URL}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={() => setMoreOpen(false)}
                    className="flex min-h-11 items-center gap-1.5 px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 hover:text-slate-950 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
                  >
                    <Github size={14} aria-hidden />
                    GitHub
                  </Link>
                </li>
              </ul>
            )}
          </li>
        </ul>

        <button
          ref={mobileButtonRef}
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="inline-flex h-11 w-11 items-center justify-center rounded-md text-slate-700 hover:bg-slate-900/5 hover:text-slate-950 lg:hidden"
          aria-controls="mobile-menu"
          aria-label={open ? "Close menu" : "Open menu"}
          aria-expanded={open}
        >
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </nav>

      {open && (
        <div
          id="mobile-menu"
          className="glass-strong max-h-[calc(100dvh-4rem)] overflow-y-auto overscroll-contain border-t border-slate-300/40 px-4 pb-[max(1rem,env(safe-area-inset-bottom))] pt-2 lg:hidden"
        >
          <ul className="flex flex-col gap-1">
            {primaryLinks.map((l) => (
              <li key={l.href}>
                <Link
                  prefetch={false}
                  href={l.href}
                  aria-current={isCurrent(l.href) ? "page" : undefined}
                  onClick={() => setOpen(false)}
                  className="flex min-h-11 items-center rounded-md px-3 py-2 text-base text-slate-800 hover:bg-slate-900/5 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
                >
                  {l.label}
                </Link>
              </li>
            ))}
            <li className="mt-2 border-t border-slate-200/60 pt-2">
              <div className="px-3 pb-1 font-mono text-[10px] uppercase tracking-widest text-slate-600">
                More
              </div>
            </li>
            {moreLinks.map((l) => (
              <li key={l.href}>
                <Link
                  prefetch={false}
                  href={l.href}
                  aria-current={isCurrent(l.href) ? "page" : undefined}
                  onClick={() => setOpen(false)}
                  className="flex min-h-11 items-center rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
                >
                  {l.label}
                </Link>
              </li>
            ))}
            <li>
              <Link
                prefetch={false}
                href={REPO_URL}
                target="_blank"
                rel="noopener noreferrer"
                onClick={() => setOpen(false)}
                className="flex min-h-11 items-center gap-2 rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 aria-[current=page]:bg-blue-50 aria-[current=page]:text-blue-800"
              >
                <Github size={16} aria-hidden />
                GitHub
              </Link>
            </li>
          </ul>
        </div>
      )}
    </header>
  );
}
