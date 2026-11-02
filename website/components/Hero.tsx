import Link from "next/link";
import { ArrowRight } from "lucide-react";
export function Hero() {
  return <section className="hero-surface py-14 sm:py-20"><div className="guide-shell">
    <h1 className="max-w-4xl font-serif text-4xl leading-tight text-slate-950 sm:text-6xl">Why these particles, charges and constants?</h1>
    <p className="mt-6 max-w-3xl text-lg leading-relaxed text-slate-700">Topological Fixed-Point Theory connects the structure of matter, its families and the electromagnetic coupling through a small geometric and algebraic starting structure.</p>
    <p className="mt-4 max-w-3xl leading-relaxed">Follow how the mathematical construction works, what has been established under its assumptions, and which connections to a common physical theory remain open.</p>
    <div className="mt-8 flex flex-wrap gap-3"><Link href="/explain" className="guide-primary">Follow a derivation <ArrowRight size={18} aria-hidden /></Link><Link href="/results" className="readout-button">Explore results and open questions</Link><Link href="/papers" className="readout-button">Read the papers</Link></div>
    <p className="mt-7 text-sm text-slate-600">By Stefan Hamann and Alessandro Rizzo. Mathematical proofs, numerical readouts and physical identifications retain their individual scope.</p>
  </div></section>;
}
