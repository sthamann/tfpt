"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { ChevronDown, Github, Menu, X } from "lucide-react";
import { cn, REPO_URL } from "@/lib/utils";
import { SITE_VERSION, SITE_DATE, SITE_REV } from "@/lib/version";
import { Logo } from "./Logo";
import { SuiteBadge } from "./SuiteBadge";

/**
 * Primary nav — six entries. Tour is appended only when the guided-tour
 * route exists (set TOUR_IN_NAV after website/app/tour/page.tsx lands).
 */
const TOUR_IN_NAV = true;

const primaryLinks = [
  { href: "/", label: "Start" },
  ...(TOUR_IN_NAV ? [{ href: "/tour", label: "Tour" }] : []),
  { href: "/method", label: "Method" },
  { href: "/verification", label: "Verification" },
  { href: "/falsification", label: "Kill board" },
  { href: "/replication", label: "Replication" },
  { href: "/papers", label: "Papers" },
  { href: "/faq", label: "FAQ" },
];

const moreLinks = [
  { href: "/orientation", label: "Reading guide" },
  { href: "/predictions", label: "Predictions" },
  { href: "/architecture", label: "Architecture" },
  { href: "/compiler", label: "Compiler" },
  { href: "/prime-front", label: "Prime Front" },
  { href: "/review", label: "For reviewers" },
  { href: "/objections", label: "Objections" },
  { href: "/changelog", label: "Changelog" },
  { href: "/orientation#rosetta", label: "Glossary / Rosetta" },
];

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const [moreOpen, setMoreOpen] = useState(false);
  const moreRef = useRef<HTMLLIElement>(null);

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
      if (event.key === "Escape") { setOpen(false); setMoreOpen(false); }
    };
    document.addEventListener("keydown", dismiss);
    return () => document.removeEventListener("keydown", dismiss);
  }, []);

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-40 transition-all duration-300",
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
            className="group flex items-center"
            aria-label="TFPT home"
          >
            <Logo size={36} />
          </Link>
          <span
            className="hidden shrink-0 select-none items-baseline gap-1.5 whitespace-nowrap border border-slate-300/40 bg-slate-200/50 px-2.5 py-1 font-mono text-[10px] tracking-wide text-slate-600 xl:inline-flex"
            title={`TFPT ${SITE_VERSION} — document set last synced ${SITE_DATE} (build rev ${SITE_REV})`}
          >
            <span className="font-semibold text-slate-700">v{SITE_VERSION}</span>
            <span aria-hidden>·</span>
            <time dateTime={SITE_DATE}>{SITE_DATE}</time>
          </span>
          <SuiteBadge className="hidden 2xl:inline-flex" />
        </div>

        <ul className="hidden items-center gap-0.5 lg:flex">
          {primaryLinks.map((l) => (
            <li key={l.href}>
              <Link
                prefetch={false}
                href={l.href}
                className="whitespace-nowrap rounded-md px-2.5 py-2 text-sm font-medium text-slate-700 transition-colors hover:bg-slate-900/5 hover:text-slate-950"
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
              aria-haspopup="true"
              className="inline-flex items-center gap-1 whitespace-nowrap rounded-md px-2.5 py-2 text-sm font-medium text-slate-700 transition-colors hover:bg-slate-900/5 hover:text-slate-950"
            >
              More
              <ChevronDown
                size={14}
                className={cn("transition-transform", moreOpen && "rotate-180")}
                aria-hidden
              />
            </button>
            {moreOpen && (
              <ul className="absolute right-0 top-full mt-1 min-w-[12rem] border border-slate-300/50 bg-slate-50/95 py-1 shadow-xl backdrop-blur">
                {moreLinks.map((l) => (
                  <li key={l.href}>
                    <Link
                      prefetch={false}
                      href={l.href}
                      onClick={() => setMoreOpen(false)}
                      className="block px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 hover:text-slate-950"
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
                    className="flex items-center gap-1.5 px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5 hover:text-slate-950"
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
          className="glass-strong border-t border-slate-300/40 px-4 pb-4 pt-2 lg:hidden"
        >
          <ul className="flex flex-col gap-1">
            {primaryLinks.map((l) => (
              <li key={l.href}>
                <Link
                  prefetch={false}
                  href={l.href}
                  onClick={() => setOpen(false)}
                  className="block rounded-md px-3 py-2 text-base text-slate-800 hover:bg-slate-900/5"
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
                  onClick={() => setOpen(false)}
                  className="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5"
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
                className="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-900/5"
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
