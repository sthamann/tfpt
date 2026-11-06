"use client";

import { useEffect, useRef, useState } from "react";

const chapters = [["inputs", "Starting principles"], ["standard-model", "Standard Model"], ["matter", "Charges"], ["e8", "Shared structure"], ["seed", "One seed"], ["flavor", "Mass relations"], ["budget", "Budget 41"], ["alpha", "Alpha"], ["predictions", "Predictions"], ["cosmology", "Scale hierarchy"], ["inflation", "Joint tests"], ["physical-readouts", "Horizons and transfers"], ["dynamics", "Continuous dynamics"], ["clocks", "Clocks"], ["quantum", "Quantum example"], ["code-families", "Code and families"], ["source", "Common source"], ["parameter-account", "Input account"], ["status", "Status"]];

export function GuideNav() {
  const [active, setActive] = useState("inputs");
  const navRef = useRef<HTMLElement>(null);
  useEffect(() => {
    let frame = 0;
    const update = () => {
      frame = 0;
      let current = chapters[0][0];
      for (const [id] of chapters) {
        const element = document.getElementById(id);
        if (element && element.getBoundingClientRect().top <= 160) current = id;
      }
      setActive(current);
    };
    const schedule = () => { if (!frame) frame = window.requestAnimationFrame(update); };
    schedule();
    window.addEventListener("scroll", schedule, { passive: true });
    window.addEventListener("resize", schedule);
    return () => {
      window.cancelAnimationFrame(frame);
      window.removeEventListener("scroll", schedule);
      window.removeEventListener("resize", schedule);
    };
  }, []);
  useEffect(() => {
    const nav = navRef.current;
    const link = nav?.querySelector<HTMLElement>('[aria-current="location"]');
    if (nav && link) nav.scrollTo({ left: link.offsetLeft - nav.clientWidth / 2 + link.clientWidth / 2, behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  }, [active]);
  return <div className="guide-navigation"><label className="guide-chapter-picker">Jump to a chapter<select aria-label="Explanation chapter" value={active} onChange={event => { setActive(event.target.value); window.location.hash = event.target.value; }}>{chapters.map(([id,title]) => <option key={id} value={id}>{title}</option>)}</select></label><nav ref={navRef} aria-label="Explanation chapters" className="guide-chapters">{chapters.map(([id, title]) => <a key={id} href={`#${id}`} aria-current={active === id ? "location" : undefined} onClick={() => setActive(id)}>{title}</a>)}</nav></div>;
}
