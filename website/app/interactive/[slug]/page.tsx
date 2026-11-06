import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { ChapterNavigation } from "@/components/interactive/ChapterNavigation";
import { ChapterExperience } from "@/components/interactive/ChapterExperience";
import { CosmologyExperience } from "@/components/interactive/CosmologyExperience";
import { BeginnerExperiments } from "@/components/interactive/BeginnerExperiments";
import { comparisonFor } from "@/lib/measurement-comparisons";
import { INTERACTIVE_CHAPTERS } from "@/lib/interactive-content";
import { frozenRegistry, predictionLabel } from "@/lib/frozen-predictions";
import { SITE_URL } from "@/lib/utils";
import styles from "@/components/interactive/InteractiveWorld.module.css";

type Props={params:Promise<{slug:string}>};
const chapters=INTERACTIVE_CHAPTERS.filter(c=>c.id!=="overview");
export const dynamicParams=false;
export function generateStaticParams(){return chapters.map(c=>({slug:c.id}));}
export async function generateMetadata({params}:Props):Promise<Metadata>{const{slug}=await params;const c=chapters.find(c=>c.id===slug);if(!c)return{};return{title:`${c.title}: Explore TFPT Interactively`,description:c.summary,alternates:{canonical:`${SITE_URL}/interactive/${c.id}`},openGraph:{title:c.question,description:c.summary,url:`${SITE_URL}/interactive/${c.id}`,type:"website"}};}

export default async function InteractiveChapterPage({params}:Props){
  const{slug}=await params;const chapter=chapters.find(c=>c.id===slug);if(!chapter)notFound();
  const index=chapters.findIndex(c=>c.id===slug);const next=chapters[(index+1)%chapters.length];
  const predictions=[...frozenRegistry.predictions,...frozenRegistry.assigned_texture_values,...frozenRegistry.conditional_bands].map(p=>({...p,observable:predictionLabel(p.id)}));
  const alpha=comparisonFor("ALPHA_INV");
  return <article className={styles.world}>
    <script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify({"@context":"https://schema.org","@type":"LearningResource",name:chapter.question,url:`${SITE_URL}/interactive/${chapter.id}`,description:chapter.summary,inLanguage:"en",learningResourceType:"Interactive explanation",educationalLevel:"Introductory",isAccessibleForFree:true,isPartOf:{"@type":"LearningResource",name:"Explore TFPT interactively",url:`${SITE_URL}/interactive`}})}}/>
    <ChapterNavigation current={chapter.id}/>
    <header className={styles.chapterHeader}><h1>{chapter.question}</h1><p>{chapter.summary}</p></header>
    <p className={styles.tryThis}><strong>Try this.</strong> {chapter.tryThis}</p>
    <BeginnerExperiments embedded chapter={chapter.id} inverseAlpha={alpha.predicted} comparison={{predicted:alpha.predicted,central:alpha.central,uncertaintyMinus:alpha.uncertaintyMinus,date:alpha.date,measured:alpha.measured}}/>
    <section className={styles.explanation} aria-label="Understand the mechanism">{chapter.steps.map(step=><div key={step.title}><h2>{step.title}</h2><p>{step.body}</p></div>)}</section>
    <details className={styles.deepDive}><summary>Explore the full interactive calculation</summary>{chapter.id === "cosmology" ? <CosmologyExperience inverseAlpha={alpha.predicted}/> : <ChapterExperience chapter={chapter.id} predictions={predictions}/>}</details>
    <section className={styles.connections}><h2>How this fits into the whole theory</h2><div><p>{chapter.connection}</p><details><summary>What this experiment establishes</summary><p>{chapter.scope}</p></details><nav aria-label="Sources and further explanation">{chapter.links.map(link=>/\.(?:json|txt|pdf|py)(?:$|[?#])/.test(link.href)?<a key={link.href} href={link.href}>{link.label}<ArrowRight size={15}/></a>:<Link key={link.href} href={link.href}>{link.label}<ArrowRight size={15}/></Link>)}</nav></div></section>
    <nav className={styles.next} aria-label="Continue your interactive journey"><Link href="/interactive"><ArrowLeft size={17}/>The whole picture</Link><Link href={`/interactive/${next.id}`}>{next.title}<ArrowRight size={17}/></Link></nav>
  </article>;
}
