import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
export const metadata: Metadata = pageMetadata("/");
import { Hero } from "@/components/Hero";
import { LegacyAnchorRedirect } from "@/components/LegacyAnchorRedirect";
import { ResearchSnapshot } from "@/components/explain/ResearchSnapshot";
import { OutcomeAtlas } from "@/components/explain/TheoryExperience";
import Link from "next/link";
import { SharedStructureBridge } from "@/components/explain/SharedStructureBridge";
import { HomeComparisonDetails } from "@/components/explain/HomeComparisonDetails";
import { PredictionOverview } from "@/components/explain/PredictionOverview";
import { TOPIC_GUIDES } from "@/lib/topic-guides";

export default function HomePage() {
  return (
    <>
      {/* Narrative: Hook → Claim → How → New frontier → Evidence → Honesty →
          Join in. Archive sections live on dedicated routes (/papers,
          /predictions, /architecture, /verification, /orientation). */}
      <LegacyAnchorRedirect />
      <Hero />
      <OutcomeAtlas />
      <section className="experience-shell guide-section" aria-labelledby="topic-questions"><h2 id="topic-questions">Start with a question.</h2><p className="guide-lead">Follow one result from its mathematical inputs to the calculation, the original sources and its physical scope.</p><ul className="mt-6 space-y-4">{TOPIC_GUIDES.map(guide => <li key={guide.id}><Link className="guide-link" href={guide.slug}>{guide.question}</Link></li>)}</ul></section>
      <SharedStructureBridge compact />
      <HomeComparisonDetails><PredictionOverview anchored={false}/></HomeComparisonDetails>
      <section className="experience-shell guide-section" id="worked-paths"><h2>Follow a construction, rather than a list of correspondences.</h2><p className="guide-lead">The detailed guide works through the operations: an exterior operator changes a carrier state; the family matrices produce mass powers; one common seed feeds four observations; one lattice root becomes a Bell ray in the specified chart.</p><div className="flex flex-wrap gap-5 mt-6"><Link className="guide-link" href="/explain#inputs">Carrier and lattice construction</Link><Link className="guide-link" href="/explain#flavor">Calculate a mass relation</Link><Link className="guide-link" href="/explain#seed">Test the common seed</Link><Link className="guide-link" href="/explain#quantum">Follow code into quantum geometry</Link></div></section>
      <div className="guide-shell"><ResearchSnapshot/><p className="my-8"><Link className="guide-link" href="/changelog#publication-presentation">Read the earlier film and presentation in the publication archive</Link></p></div>
    </>
  );
}
