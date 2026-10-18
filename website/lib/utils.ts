import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Canonical source repository: the full theory documents plus the independent
 * verification stack (Python suite, Wolfram mirror, Lean carrier proof) and the
 * versioned status ledger.
 */
export const REPO_URL = "https://github.com/sthamann/tfpt";

/**
 * Canonical public site origin (no trailing slash). Single source for canonical
 * URLs, Open Graph / Twitter tags, the sitemap and robots.txt. Override with the
 * NEXT_PUBLIC_SITE_URL env var in Vercel; the fallback is the production domain.
 */
export const SITE_URL =
  (process.env.NEXT_PUBLIC_SITE_URL || "https://www.fixpoint-theory.com").replace(/\/+$/, "");

/** Independent prime-number and RH research project. */
export const PRIME_FRONT_URL = "https://prime.fixpoint-theory.com";
