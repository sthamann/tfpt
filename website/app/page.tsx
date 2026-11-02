import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
export const metadata: Metadata = pageMetadata("/");
import { Hero } from "@/components/Hero";
import { IntroVideo } from "@/components/IntroVideo";
import { InOneBreath } from "@/components/InOneBreath";
import { WhyThisMatters } from "@/components/WhyThisMatters";
import { TrustContract } from "@/components/TrustContract";
import { ClaimStack } from "@/components/ClaimStack";
import { GeometryArc } from "@/components/GeometryArc";
import { CodePrimesBand } from "@/components/CodePrimesBand";
import { HonestyBand } from "@/components/HonestyBand";
import { MethodBand } from "@/components/MethodBand";
import { Safeguards } from "@/components/Safeguards";
import { Overview } from "@/components/Overview";
import { PathChooser } from "@/components/PathChooser";
import { DownloadsTeaser } from "@/components/DownloadsTeaser";
import { LegacyAnchorRedirect } from "@/components/LegacyAnchorRedirect";
import { TheoryMap } from "@/components/explain/TheoryGuide";
import { ResearchSnapshot } from "@/components/explain/ResearchSnapshot";
import { OutcomeAtlas, ConnectionStory } from "@/components/explain/TheoryExperience";
import { StartingStructures } from "@/components/explain/StartingStructures";
import { PatternConnections } from "@/components/explain/PatternConnections";
import { PredictionOverview } from "@/components/explain/PredictionOverview";
import { DerivationPreview } from "@/components/explain/DerivationPreview";

export default function HomePage() {
  return (
    <>
      {/* Narrative: Hook → Claim → How → New frontier → Evidence → Honesty →
          Join in. Archive sections live on dedicated routes (/papers,
          /predictions, /architecture, /verification, /orientation). */}
      <LegacyAnchorRedirect />
      <Hero />
      <PredictionOverview />
      <OutcomeAtlas />
      <StartingStructures />
      <ConnectionStory />
      <PatternConnections />
      <div className="guide-shell"><ResearchSnapshot />
      <details className="guide-details my-8"><summary>Work through a concrete derivation: charges, the family and the alpha budget</summary><DerivationPreview /></details>
      <details className="guide-details my-8"><summary>Explore the full theory map and its source links</summary><TheoryMap compact /></details></div>
      <div className="guide-shell py-8"><details className="guide-details">
      <summary>Open the detailed publication overview and historical film</summary>
      <p>The following sections preserve the publication narrative and its dated comparisons. The current result library also includes later source reviewed research and scope corrections. Script totals describe an inventory; they do not announce a new suite run.</p>
      <IntroVideo />
      <InOneBreath />
      <WhyThisMatters />
      <TrustContract />
      <ClaimStack />
      <GeometryArc />
      <CodePrimesBand />
      <HonestyBand />
      <MethodBand />
      <Safeguards compact />
      <Overview />
      <PathChooser />
      <DownloadsTeaser />
      </details></div>
    </>
  );
}
