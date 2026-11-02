"use client";

import { useEffect, useRef, useState } from "react";

const chapters = [["inputs", "Starting principles"], ["matter", "Charges"], ["e8", "Shared structure"], ["seed", "One seed"], ["flavor", "Mass relations"], ["budget", "Budget 41"], ["alpha", "Alpha"], ["cosmology", "Scale hierarchy"], ["inflation", "Joint tests"], ["clocks", "Clocks"], ["quantum", "Quantum example"], ["source", "Common source"], ["parameter-account", "Input account"], ["status", "Status"]];

export function GuideNav() {
  const [active, setActive] = useState("inputs");
  const navRef = useRef<HTMLElement>(null);
  useEffect(() => {
    const initial = window.location.hash.slice(1);
    if (chapters.some(([id]) => id === initial)) setActive(initial);
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) setActive(entry.target.id);
    }, { rootMargin: "-145px 0px -65% 0px" });
    chapters.map(([id]) => id).forEach(id => { const element = document.getElementById(id); if (element) observer.observe(element); });
    return () => observer.disconnect();
  }, []);
  useEffect(() => {
    const nav = navRef.current;
    const link = nav?.querySelector<HTMLElement>('[aria-current="location"]');
    if (nav && link) nav.scrollTo({ left: link.offsetLeft - nav.clientWidth / 2 + link.clientWidth / 2, behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  }, [active]);
  return <nav ref={navRef} aria-label="Explanation chapters" className="guide-chapters">{chapters.map(([id, title]) => <a key={id} href={`#${id}`} aria-current={active === id ? "location" : undefined} onClick={() => setActive(id)}>{title}</a>)}</nav>;
}
