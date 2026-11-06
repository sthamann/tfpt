"use client";

import { useId, useState } from "react";
import Link from "next/link";
import { Math } from "@/components/Math";
import { familyTransfer } from "@/components/interactive/mechanisms";
import styles from "./TheoryCoverage.module.css";

export function ContinuousTransfer() {
  const id=useId();
  const [time,setTime]=useState(.5);
  // Remove floating point roundoff at zero before drawing percentages.
  const values=familyTransfer([1,0,0],time).map(v=>globalThis.Math.max(0,globalThis.Math.min(1,v)));
  return <section id="dynamics" className={`guide-section ${styles.coverage}`} aria-labelledby={`${id}-title`}>
    <h2 id={`${id}-title`}>What happens between whole transfer steps?</h2>
    <p className="guide-lead">A transfer step redistributes three weights. The original dynamics calculation also gives a continuous path between those steps. Move the slider to see a half step, a whole step and the approach to equal weights.</p>
    <label className={styles.timeControl} htmlFor={`${id}-time`}>Transfer time t = {time.toFixed(2)}<input id={`${id}-time`} type="range" min="0" max="3" step="0.01" value={time} onChange={event=>setTime(Number(event.target.value))}/></label>
    <div className={styles.weights} aria-label="Three continuously evolving weights">{values.map((v,i)=><div key={i}><span>Direction {i+1}</span><div><i style={{width:`${v*100}%`}}/></div><output>{(v*100).toFixed(2)}%</output></div>)}</div>
    <p>The finite three state kernel has a real logarithm Q = log T with positive rates between different states. Each row sums to zero, so probability is conserved. This makes exp(tQ) a valid stochastic transfer for every t ≥ 0, including fractional times.</p>
    <Math block>{String.raw`\begin{aligned}T(t)&=e^{tQ},\quad T(1)=T,\\\operatorname{spec}(T(t))&=\left\{1,\left(\frac23\right)^{6t},\left(\frac13\right)^{6t}\right\}.\end{aligned}`}</Math>
    <p>Time here is measured in transfer steps. The finite dynamics programme also supplies specified collision, interacting and continuous quantum constructions. The thermodynamic field limit and the physical branch identification retain their own conditions. The same population transfer can admit different quantum lifts, so these three bars alone do not select a unique quantum evolution.</p>
    <nav className={styles.actions} aria-label="Continuous dynamics sources"><Link href="/documentation?section=section%3Aa3401d23c565056512c5">Read the Markov proof and later finite dynamics updates</Link><Link href="/interactive/dynamics">Explore the connected dynamics journey</Link></nav>
  </section>;
}
