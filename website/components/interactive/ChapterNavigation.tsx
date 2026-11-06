"use client";

import Link from "next/link";
import { useEffect, useRef } from "react";
import { INTERACTIVE_CHAPTERS, type InteractiveChapterId } from "@/lib/interactive-content";
import styles from "./InteractiveWorld.module.css";

export function ChapterNavigation({ current }: { current: InteractiveChapterId }) {
  const navigation=useRef<HTMLElement>(null);
  useEffect(()=>{const nav=navigation.current;const active=nav?.querySelector<HTMLElement>('[aria-current="page"]');if(nav&&active&&nav.scrollWidth>nav.clientWidth)nav.scrollLeft=active.offsetLeft-nav.offsetLeft-nav.clientWidth/2+active.clientWidth/2;},[current]);
  const labels: Record<string,string> = {overview:"The whole theory",alpha:"Alpha","standard-model":"Standard Model",e8:"E₈",dynamics:"Dynamics",predictions:"Predictions",flavor:"Flavour",cosmology:"Cosmology",quantum:"Quantum & clocks"};
  return <nav ref={navigation} className={styles.chapterNav} aria-label="Interactive theory chapters">
    {INTERACTIVE_CHAPTERS.map(chapter=><Link key={chapter.id} href={chapter.id==="overview"?"/interactive":`/interactive/${chapter.id}`} aria-current={current===chapter.id?"page":undefined}>{labels[chapter.id] ?? chapter.title}</Link>)}
  </nav>;
}
