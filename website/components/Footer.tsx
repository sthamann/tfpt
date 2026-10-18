"use client";

import Link from "next/link";
import { Github } from "lucide-react";
import { Logo } from "./Logo";
import { REPO_URL } from "@/lib/utils";
import { trackPdfInteraction, type DownloadKind } from "@/lib/track";
import { SITE_VERSION } from "@/lib/version";
import { SuiteBadge } from "./SuiteBadge";

interface FooterLink {
  href: string;
  label: string;
  kind: DownloadKind;
}

const READING_GUIDE: FooterLink = {
  href: "/papers/introduction.pdf",
  label: "Reading guide (PDF)",
  kind: "paper",
};
const ORIGIN_THEORY: FooterLink = {
  href: "/papers/origin_theory.pdf",
  label: "Origin Theory",
  kind: "paper",
};
const RESEARCH_CONTRACTS: FooterLink = {
  href: "/papers/tfpt_research_contracts.pdf",
  label: "Research contracts",
  kind: "paper",
};
const HORIZON: FooterLink = {
  href: "/papers/tfpt_horizon_readouts.pdf",
  label: "Appendix H — horizon",
  kind: "paper",
};

function trackFooter(link: FooterLink) {
  trackPdfInteraction({
    file: link.href,
    source: "footer",
    kind: link.kind,
    interaction: "download",
    title: link.label,
  });
}

export function Footer() {
  return (
    <footer className="relative mt-24 border-t border-slate-200/80 bg-slate-50/60">
      <div className="absolute inset-x-0 -top-px h-px bg-gradient-to-r from-transparent via-blue-500/30 to-transparent" />
      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-14 sm:px-6 lg:grid-cols-3 lg:px-8">
        <div>
          <Logo size={40} />
          <p className="mt-4 max-w-md text-sm leading-relaxed text-slate-600">
            Topological Fixed-Point Theory. A discrete compiler that builds E₈
            from two axioms — the seam constant c₃ = 1/(8π) and the carrier rank
            g_car = 5 — and reads off the Standard Model, α⁻¹ = 137.0359992, the
            flavor sector and the scale grammar. No fitted constants; only π is
            irreducible.
          </p>
          <div className="mt-3">
            <SuiteBadge />
          </div>
          <p className="mt-4 text-xs text-slate-600">
            By <span className="text-slate-700">Stefan Hamann</span> &amp;{" "}
            <span className="text-slate-700">Alessandro Rizzo</span>.
          </p>
          <p className="mt-2 text-xs text-slate-600">
            Contact:{" "}
            <Link
              prefetch={false}
              href="mailto:sh@sh-future.de"
              className="text-slate-600 underline decoration-slate-300 underline-offset-2 hover:text-slate-950"
            >
              sh@sh-future.de
            </Link>
          </p>
        </div>

        <div>
          <h3 className="font-serif text-sm font-semibold uppercase tracking-wider text-slate-800">
            Explore
          </h3>
          <ul className="mt-4 space-y-2 text-sm">
            <li>
              <Link prefetch={false} href="/verification" className="text-slate-600 hover:text-slate-950">
                Verification
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/falsification" className="text-slate-600 hover:text-slate-950">
                Kill board
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/replication" className="text-slate-600 hover:text-slate-950">
                Replication
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/papers" className="text-slate-600 hover:text-slate-950">
                Papers
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/predictions" className="text-slate-600 hover:text-slate-950">
                Predictions
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/architecture" className="text-slate-600 hover:text-slate-950">
                Architecture
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/orientation" className="text-slate-600 hover:text-slate-950">
                Reading guide
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/compiler" className="text-slate-600 hover:text-slate-950">
                Compiler
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/review" className="text-slate-600 hover:text-slate-950">
                For reviewers
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/objections" className="text-slate-600 hover:text-slate-950">
                Objection ledger
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/faq" className="text-slate-600 hover:text-slate-950">
                FAQ
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/changelog" className="text-slate-600 hover:text-slate-950">
                Changelog
              </Link>
            </li>
            <li>
              <Link
                prefetch={false}
                href={REPO_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 text-slate-600 hover:text-slate-950"
              >
                <Github size={13} aria-hidden />
                GitHub
              </Link>
            </li>
            <li>
              <a
                href="https://www.hylaean.ai/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-slate-600 hover:text-slate-700"
              >
                Adjacent: Hylaean
              </a>
            </li>
          </ul>
        </div>

        <div>
          <h3 className="font-serif text-sm font-semibold uppercase tracking-wider text-slate-800">
            Downloads
          </h3>
          <ul className="mt-4 space-y-2 text-sm">
            <li>
              <Link
                prefetch={false}
                href={READING_GUIDE.href}
                target="_blank"
                rel="noopener"
                onClick={() => trackFooter(READING_GUIDE)}
                className="text-slate-600 hover:text-slate-950"
              >
                {READING_GUIDE.label}
              </Link>
            </li>
            <li>
              <Link
                prefetch={false}
                href={ORIGIN_THEORY.href}
                target="_blank"
                rel="noopener"
                onClick={() => trackFooter(ORIGIN_THEORY)}
                className="text-slate-600 hover:text-slate-950"
              >
                {ORIGIN_THEORY.label}
              </Link>
            </li>
            <li>
              <Link
                prefetch={false}
                href={RESEARCH_CONTRACTS.href}
                target="_blank"
                rel="noopener"
                onClick={() => trackFooter(RESEARCH_CONTRACTS)}
                className="text-slate-600 hover:text-slate-950"
              >
                {RESEARCH_CONTRACTS.label}
              </Link>
            </li>
            <li>
              <Link
                prefetch={false}
                href={HORIZON.href}
                target="_blank"
                rel="noopener"
                onClick={() => trackFooter(HORIZON)}
                className="text-slate-600 hover:text-slate-950"
              >
                {HORIZON.label}
              </Link>
            </li>
            <li>
              <Link prefetch={false} href="/papers" className="text-slate-600 hover:text-slate-950">
                All papers →
              </Link>
            </li>
          </ul>
        </div>
      </div>

      <div className="border-t border-slate-200/80 px-4 py-6 sm:px-6 lg:px-8">
        <div className="mx-auto flex max-w-7xl flex-col items-start justify-between gap-3 text-xs text-slate-600 sm:flex-row sm:items-center">
          <p>
            <span>© {new Date().getFullYear()}</span>
            {"\u00A0"}
            <span>Stefan Hamann &amp; Alessandro Rizzo.</span>
            {" "}
            <span>All papers and predictions distributed for academic use.</span>
          </p>
          <p className="text-slate-500">
            TFPT {SITE_VERSION} — two axioms · one E₈ compiler · the Standard Model
          </p>
        </div>
        <div className="mx-auto mt-3 max-w-7xl text-[11px] leading-relaxed text-slate-500">
          This site uses{" "}
          <Link
            prefetch={false}
            href="https://vercel.com/docs/analytics/privacy-policy"
            target="_blank"
            rel="noopener"
            className="underline decoration-slate-300 underline-offset-2 hover:text-slate-600"
          >
            Vercel Web Analytics
          </Link>{" "}
          for cookie-free, anonymous aggregate page-view and PDF-download
          counts. No personal identifiers, no IP addresses, and no cookies are
          stored.
        </div>
      </div>
    </footer>
  );
}
