import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { CarrierFigure } from "./explain/CarrierFigure";
export function Hero() {
  return <section className="hero-surface figure-hero"><div className="guide-shell figure-hero-layout"><div className="figure-hero-copy">
    <h1>Why these particles and numbers?</h1>
    <p className="figure-hero-lead">Five internal slots. Six charge sectors. Sixteen components in one family.</p>
    <p>Topological Fixed-Point Theory connects this small structure to E₈ geometry, flavour relations and a fixed equation for the electromagnetic coupling. Follow one connection all the way through.</p>
    <div className="hero-actions mt-8 flex flex-wrap gap-3"><Link href="#charge-builder" className="guide-primary">Build a family of charges <ArrowRight size={18} aria-hidden /></Link><Link href="/explain" className="readout-button">Explore the whole theory</Link></div>
    <p className="mt-6 text-sm text-slate-600">A research programme by Stefan Hamann and Alessandro Rizzo. Each step names what is given, what follows and which physical connection remains to be established.</p>
  </div><CarrierFigure introductory />
  </div></section>;
}
