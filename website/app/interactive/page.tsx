import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, Atom, Binary, CircleDot, GitBranch, Layers3, Orbit, Waves, Telescope } from "lucide-react";
import { TheoryJourney } from "@/components/interactive/TheoryJourney";
import { BeginnerJourney } from "@/components/interactive/BeginnerJourney";
import { comparisonFor } from "@/lib/measurement-comparisons";
import { ChapterNavigation } from "@/components/interactive/ChapterNavigation";
import { INTERACTIVE_CHAPTERS } from "@/lib/interactive-content";
import { SITE_URL } from "@/lib/utils";
import styles from "@/components/interactive/InteractiveWorld.module.css";

export const metadata: Metadata = {
  title: "Interactive TFPT: Explore the Theory, Alpha, E₈ and Dynamics",
  description: "Understand how TFPT fits together. Follow a visual journey, build E₈ roots, explore particle charges, find the alpha fixed point and run the finite dynamics.",
  alternates: {canonical: `${SITE_URL}/interactive`},
  openGraph: {title:"Explore TFPT interactively",description:"One connected theory, explained through working visual experiments.",url:`${SITE_URL}/interactive`,type:"website"},
};
const icons={alpha:CircleDot,"standard-model":Atom,e8:Orbit,dynamics:Waves,predictions:GitBranch,flavor:Layers3,quantum:Binary,cosmology:Telescope};

export default function InteractivePage(){
  const alpha=comparisonFor("ALPHA_INV");
  return <article className={styles.world}>
    <script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify({"@context":"https://schema.org","@type":"LearningResource",name:"Explore TFPT interactively",url:`${SITE_URL}/interactive`,description:metadata.description,inLanguage:"en",learningResourceType:"Interactive explanation",educationalLevel:"Introductory",isAccessibleForFree:true,hasPart:INTERACTIVE_CHAPTERS.filter(c=>c.id!=="overview").map(c=>({"@type":"LearningResource",name:c.title,url:`${SITE_URL}/interactive/${c.id}`}))})}}/>
    <header className={styles.header}><h1>Follow the whole theory.</h1><p>Follow one continuous journey from four marked points to matter, E₈, alpha and predictions. Watch the branches connect, pause anywhere and explore each calculation.</p></header>
    <BeginnerJourney inverseAlpha={alpha.predicted} comparison={{predicted:alpha.predicted,central:alpha.central,uncertaintyMinus:alpha.uncertaintyMinus,date:alpha.date,measured:alpha.measured}}/>
    <details className={styles.deepDive}><summary>Explore the full connection map</summary><TheoryJourney/></details>
    <section className={styles.index} aria-labelledby="interactive-chapters-heading">
      <ChapterNavigation current="overview"/>
      <h2 id="interactive-chapters-heading">Pick something to try.</h2>
      <p>Each chapter starts with one idea you can see and change. Explore freely, or follow the chapters from the particle structure through its connected readouts.</p>
      <ul className={styles.chapterList}>{INTERACTIVE_CHAPTERS.filter(c=>c.id!=="overview").map(chapter=>{const Icon=icons[chapter.id as keyof typeof icons];return <li key={chapter.id}><Link href={`/interactive/${chapter.id}`}><Icon size={50} strokeWidth={1.2} aria-hidden/><h3>{chapter.question}</h3><p>{chapter.summary}</p><ArrowRight size={22} aria-hidden/></Link></li>})}</ul>
    </section>
    <section className={styles.connections}><h2>Keep the whole construction in view.</h2><div><p>The lattice, representations, numerical readouts and physical source are connected parts of the programme. Each experiment links back to the original argument and the conditions under which it applies.</p><nav aria-label="Continue beyond the interactive introduction"><Link href="/explain">The complete connected explanation<ArrowRight size={15}/></Link><Link href="/results">Results and their evidence<ArrowRight size={15}/></Link></nav></div></section>
  </article>;
}
