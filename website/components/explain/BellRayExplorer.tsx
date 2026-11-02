"use client";
import { useState } from "react";
import Link from "next/link";
import { Math } from "@/components/Math";
import styles from "./BellRayExplorer.module.css";
type Complex = [number,number];
const root = [1,1,0,0,0,0,1,1];
const jTurn = (r:number[]) => r.flatMap((_,i)=>i%2===0?[-r[i+1],r[i]]:[]);
const complex = ([re,im]:Complex) => re===0 && im===0 ? "0" : `${re===1?"1":"−1"}${im===1?"+i":"−i"}`;
export function BellRayExplorer(){
 const [turn,setTurn]=useState(0),[operator,setOperator]=useState<"XX"|"ZZ"|"YY">("XX");
 let r=[...root];for(let i=0;i<turn;i++)r=jTurn(r);
 const z:Complex[]=Array.from({length:4},(_,i)=>[r[2*i],r[2*i+1]]);
 const transformed:Complex[]=Array.from({length:4},()=>[0,0]);
 z.forEach((value,i)=>{const target=operator==="ZZ"?i:i^3;const sign=operator==="ZZ"?(i===1||i===2?-1:1):operator==="YY"?(i===0||i===3?-1:1):1;transformed[target]=[sign*value[0],sign*value[1]];});
 const norm=z.reduce((sum,[re,im])=>sum+re*re+im*im,0);
 const probabilities=z.map(([re,im])=>(re*re+im*im)/norm);
 const eigenvalue=operator==="YY"?-1:1;
 const exact=transformed.every((v,i)=>v[0]===eigenvalue*z[i][0]&&v[1]===eigenvalue*z[i][1]);
 return <div className={styles.root}>
  <h4>Follow one codeword into a Bell state.</h4><p>The valid word <strong>11000011</strong> lifts to the integer vector below. In the Construction A scaling r/√2 it is an E₈ root of squared norm two.</p>
  <div className={styles.coordinates} aria-label={`Integer root coordinates: ${r.join(", ")}`}>{r.map((v,i)=><div key={i}><small>r{i+1}</small><strong>{v===0?0:v}</strong></div>)}</div>
  <p>The specified chart pairs adjacent real coordinates: zₖ = r₂ₖ₋₁ + i r₂ₖ for k = 1, …, 4. It produces four complex amplitudes, ordered as |00⟩, |01⟩, |10⟩, |11⟩.</p>
  <div className={styles.amplitudes}>{z.map((v,i)=><div key={i}><span>|{i.toString(2).padStart(2,"0")}⟩</span><strong>{complex(v)}</strong><small>{(probabilities[i]*100).toFixed(0)}% probability</small><i style={{width:`${probabilities[i]*100}%`}}/></div>)}</div>
  <Math block>{String.raw`\frac{z}{\|z\|}\ \sim\ |\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}`}</Math>
  <p>After normalization, the two nonzero amplitudes have the same phase. Ignoring that one common phase gives the Bell ray. Measuring in this basis yields 00 or 11 with equal probabilities; the outcomes are perfectly correlated.</p>
  <button type="button" className={styles.action} onClick={()=>setTurn((turn+1)%4)}>Apply the lattice quarter turn J</button><p aria-live="polite" className={styles.state}>{turn} quarter turns. Every amplitude is multiplied by i at each turn. The four probabilities and the phase independent ray stay the same.</p>
  <h5>Check the quantum meaning with an operator.</h5><div className={styles.controls} role="group" aria-label="Pauli operator to test">{(["XX","ZZ","YY"] as const).map(op=><button key={op} type="button" aria-pressed={operator===op} onClick={()=>setOperator(op)}>{op[0]} ⊗ {op[1]}</button>)}</div>
  <p aria-live="polite"><strong>Eigenvalue {eigenvalue===1?"+1":"−1"}; exact vector check {exact?"passes":"fails"}.</strong> {operator==="XX"?"X ⊗ X swaps 00 and 11, leaving their equal superposition unchanged.":operator==="ZZ"?"Z ⊗ Z gives +1 on both 00 and 11: the two minus signs on 11 cancel.":"Y ⊗ Y exchanges 00 and 11 with a minus sign. Thus −(Y ⊗ Y) stabilizes the same state with +1."}</p>
  <details><summary>What does this prove about the larger dictionary?</summary><p>The common +1 stabilizers are XX, ZZ and −YY. This is one worked example in the exact sixty ray correspondence. J relates four phase representatives of each Gaussian line. The specified chart and its equivariance are essential; equal counts alone would not produce a quantum dictionary.</p><p>This is a finite representation correspondence. A physical preparation or measurement instrument has the premises of the source and reader construction.</p><Link href="/documentation?section=section%3A9cfcbfb68fe8471a4d4f">Codeword and allowed support</Link><Link href="/documentation?section=section%3Ae200cccfccb890e62271">Complex structure J</Link><Link href="/documentation?evidence=python_verification%3Averification%2Fv783_two_qubit_clifford.py">The exact chart and Pauli checks</Link></details>
 </div>;
}
