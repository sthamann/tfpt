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

export default function HomePage() {
  return (
    <>
      {/* Narrative: Hook → Claim → How → New frontier → Evidence → Honesty →
          Join in. Archive sections live on dedicated routes (/papers,
          /predictions, /architecture, /verification, /orientation). */}
      <LegacyAnchorRedirect />
      <Hero />
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
    </>
  );
}
