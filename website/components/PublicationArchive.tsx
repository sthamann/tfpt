import Link from "next/link";
import { IntroVideo } from "./IntroVideo";
import { InOneBreath } from "./InOneBreath";
import { WhyThisMatters } from "./WhyThisMatters";
import { TrustContract } from "./TrustContract";
import { ClaimStack } from "./ClaimStack";
import { GeometryArc } from "./GeometryArc";
import { CodePrimesBand } from "./CodePrimesBand";
import { HonestyBand } from "./HonestyBand";
import { MethodBand } from "./MethodBand";
import { Safeguards } from "./Safeguards";
import { Overview } from "./Overview";
import { PathChooser } from "./PathChooser";
import { DownloadsTeaser } from "./DownloadsTeaser";

export function PublicationArchive(){return <section id="publication-presentation" className="reference-section scroll-mt-24">
 <h2>Earlier publication presentation</h2><p>This archive preserves the earlier film and presentation with their original counts, comparisons, candidate phases and claim language. They describe their historical snapshots. The current register keeps its own frozen values and the empirical audit names the selected later data.</p><nav className="reference-links" aria-label="Current records alongside the archive"><Link href="/predictions">Current register and assigned textures</Link><Link href="/empirical-audit">Dated comparisons</Link><Link href="/results">Source reviewed results</Link></nav>
 <details className="guide-details my-6"><summary>Open the historical film and presentation</summary><p className="mt-5">The film's module total, earlier approximate pulls, later neutrino candidates and grammar dependent null scores belong to this presentation. They are not replacement values or a combined probability for the current theory.</p><IntroVideo/><InOneBreath/><WhyThisMatters/><TrustContract/><ClaimStack/><GeometryArc/><CodePrimesBand/><HonestyBand/><MethodBand/><Safeguards compact/><Overview/><PathChooser/><DownloadsTeaser/></details>
 </section>;}
