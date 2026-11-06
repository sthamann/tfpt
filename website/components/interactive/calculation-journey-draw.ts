import { C3, FIXED_SEED, alphaResidual, alphaRoot, familyTransfer, seedReadouts } from "./mechanisms";
import { clampJourney as clamp, journeyColors as colors } from "./chapter-journey-types";
import type { DrawKit, JourneyComparison } from "./chapter-journey-types";
const root=alphaRoot(), inverse=1/root, base=1/(6*Math.PI), delta=48*C3**4;
const initial=[.8,.15,.05], outputs=seedReadouts(FIXED_SEED);
const f=(value:number,digits=6)=>value.toFixed(digits);
const lerp=(a:number,b:number,p:number)=>a+(b-a)*p;
function verticalBar(k:DrawKit,x:number,y:number,w:number,h:number,value:number,color:string){k.ctx.fillStyle="#28435d";k.ctx.fillRect(x,y,w,h);k.ctx.fillStyle=color;k.ctx.fillRect(x,y+h*(1-value),w,h*value);}
function weightBars(k:DrawKit,values:number[],before?:number[]){values.forEach((value,i)=>{const x=-78+i*60;verticalBar(k,x,-44,35,79,value,colors[i]);if(before){k.ctx.strokeStyle="#b4cce3";k.ctx.setLineDash([3,4]);k.ctx.strokeRect(x,35-before[i]*79,35,before[i]*79);k.ctx.setLineDash([]);}k.text(`${(100*value).toFixed(2)}%`,x+17.5,52,12,colors[i]);});}
function dotRow(k:DrawKit,n:number,y:number,color:string){for(let i=0;i<n;i++)k.dot((i-(n-1)/2)*20,y,6,color);}
function comparisonGlyph(k:DrawKit,c:JourneyComparison){const z=(c.predicted-Number(c.central))/Number(c.uncertaintyMinus);k.ctx.fillStyle="#29594f";k.ctx.fillRect(-27,-24,54,28);k.line(-84,4,84,4);k.line(0,-32,0,10,colors[1]);k.dot(27*Math.max(-3,Math.min(3,z)), -10,4,colors[2]);k.text("measured",-35,-48,12,colors[1]);k.text("calculated",44,-48,12,colors[2]);[-3,0,3].forEach(v=>k.text(String(v),v*27,23,12));k.text(`${z.toFixed(2)} uncertainties`,0,51,14,colors[2]);}
function alpha(k:DrawKit,i:number,c:JourneyComparison){const {text,dot,line,bar,progress:p}=k;
  if(i===0){text("c₃ = 1 / (8π)",0,-42,17);dotRow(k,3,-9,colors[0]);dotRow(k,2,15,colors[1]);text("γ = 3/9 + 2/4 = 5/6",0,39,13);text("(3/2) × γ = 5/4",0,59,14,colors[2]);}
  else if(i===1){text("3 × 16 = 48",0,-43,18);text("bY = 20/3 + 1/6 = 41/6",0,-10,13);text("b₁ = (3/5)bY = 41/10",0,19,13);text("M = 10b₁ = 41",0,49,18,colors[2]);}
  else if(i===2){for(let n=0;n<4;n++){dot(-60+n*40,-36,10,colors[0]);text("c₃",-60+n*40,-36,12,"#102439");}text(`δ = ${delta.toExponential(5)}`,0,-3,15,colors[2]);line(-60,13,60,13);text(`base = ${f(base,9)}`,0,37,15,colors[1]);text("c₃ / (3/4) = 1/(6π)",0,58,12);}
  else if(i===3){const q=delta*Math.exp(-2/130),response=base+q*(1-q)**(-5/4);text("trial α = 1/130",0,-48,15);text(`q = ${q.toExponential(5)}`,0,-24,14,colors[2]);line(0,-10,0,3,colors[2]);text("base + q(1−q)⁻⁵/⁴",0,21,14);text(`φₛ = ${f(response,9)}`,0,51,16,colors[1]);}
  else if(i===4){const a=1/130,q=delta*Math.exp(-2*a),phi=base+q*(1-q)**(-5/4),lhs=a**3-2*C3**3*a**2,rhs=4/5*41*C3**6*Math.log(1/phi);text("trial inverse α = 130",0,-49,14);bar(-78,-29,156,13,lhs/lhs,colors[2]);bar(-78,-3,156,13,rhs/lhs,colors[1]);text("local term ≠ response",0,37,14);text("F = local − response",0,59,12);}
  else if(i===5){const x=(a:number)=>-82+a/.014*164,y=(v:number)=>36-v/2e-6*72;line(-82,36,84,36);line(-82,-51,-82,36);k.ctx.beginPath();for(let n=0;n<=70;n++){const a=n/70*.014;k.ctx[n?'lineTo':'moveTo'](x(a),y(alphaResidual(a)));}k.ctx.strokeStyle=colors[1];k.ctx.lineWidth=2;k.ctx.stroke();dot(x(root),36,4,colors[2]);text("negative → one crossing",0,-48,12);text("convex beyond t",0,59,13,colors[1]);}
  else if(i===6){let lo=1/145,hi=1/130;const n=Math.floor(p*35);for(let j=0;j<n;j++){const mid=(lo+hi)/2;if(alphaResidual(mid)>0)hi=mid;else lo=mid;}const x=(a:number)=>-83+(a-1/145)/(1/130-1/145)*166;line(-83,-15,83,-15);line(x(lo),-35,x(lo),5,colors[1]);line(x(hi),-35,x(hi),5,colors[2]);k.ctx.fillStyle="#315b65";k.ctx.fillRect(x(lo),-25,Math.max(.5,x(hi)-x(lo)),20);text(`${n} bisections`,0,-52,14);text(`α⁻¹ ≈ ${f(2/(lo+hi),6)}`,0,27,17,colors[2]);text("retain the sign change",0,55,12);}
  else comparisonGlyph(k,c);
}
function flavor(k:DrawKit,i:number){const {text,line,bar,progress:p}=k;
  if(i===0){text("c₃ = 1/(8π)",0,-33,18,colors[0]);line(-65,-8,65,-8);text("3 × 16 = 48",0,23,18,colors[1]);}
  else if(i===1){text(`base ${f(base,8)}`,0,-35,16,colors[1]);text("+",0,-3,24);text(`48c₃⁴ ${f(delta,8)}`,0,30,16,colors[2]);}
  else if(i===2){text("base + correction",0,-39,15);line(-65,-17,65,-17);text(f(FIXED_SEED,9),0,9,23,colors[1]);text("same u in every branch",0,45,13);}
  else if(i===3){bar(-84,-38,168,13,FIXED_SEED,colors[0]);text(`u = ${f(FIXED_SEED,5)}`,0,-50,12);bar(-84,-1,168,13,1-FIXED_SEED,colors[1]);text("1 − u",0,28,13);text(`√[u(1−u)] = ${f(outputs[0],6)}`,0,54,15,colors[2]);}
  else if(i===4){text("γ = 5/6",0,-48,16);bar(-83,-24,166,13,1,colors[0]);bar(-83,2,166,13,Math.exp(-5/6),colors[1]);text("multiply by e⁻⁵/⁶",0,32,13);text(f(outputs[1],8),0,57,18,colors[1]);}
  else if(i===5){const frac=1/(4*Math.PI);k.ctx.fillStyle=colors[2];k.ctx.fillRect(-83,-24,166*frac,22);k.ctx.fillStyle=colors[1];k.ctx.fillRect(-83+166*frac,-24,166*(1-frac),22);text("partition of the seed",0,-48,13);text(`β = ${f(outputs[2],6)}°`,0,25,16,colors[2]);text(`Ωb = ${f(outputs[3],7)}`,0,54,16,colors[1]);}
  else{const places=[[-64,-42],[64,-42],[-64,26],[64,26]],labels=["λC","sin² θ₁₃","β (°)","Ωb"];k.dot(0,-7,12,colors[1]);text("u",0,-7,13,"#102439",600);places.forEach(([x,y],j)=>{line(0,-7,x*.55,y<0?-17:8,colors[j]);k.dot(x*.55,y<0?-17:8,2,colors[j]);text(labels[j],x,y-12,12,colors[j]);text(f(outputs[j],5),x,y+9,14,colors[j]);});}
}
function dynamics(k:DrawKit,i:number){const {text,line,bar,progress:p}=k;
  if(i===0){weightBars(k,initial);text("total = 1",0,-61,14);}
  else if(i===1){weightBars(k,[1/3,1/3,1/3],initial);text("the unchanged equal part",0,-62,12);}
  else if(i===2){text("u₂: (1, −1, 0) / √2",0,-44,13,colors[0]);text("u₃: (1, 1, −2) / √6",0,-18,13,colors[1]);text("a₂ = 0.459619",0,15,15,colors[0]);text("a₃ = 0.347011",0,44,15,colors[1]);}
  else if(i===3){text("64 / 729",0,-45,16,colors[0]);bar(-83,-26,166,13,64/729,colors[0]);text("1 / 729",0,13,16,colors[1]);bar(-83,33,166,13,1/729,colors[1]);}
  else if(i===4){const after=familyTransfer(initial,1),values=initial.map((v,j)=>lerp(v,after[j],p));weightBars(k,values,initial);text("one exact transfer step",0,-61,12);}
  else{const n=Math.floor(p*8),values=familyTransfer(initial,n);weightBars(k,values);text(`step ${n} · total 1`,0,-61,14);}
}
function predictions(k:DrawKit,i:number,c:JourneyComparison,freeze:string){const {text,line,dot}=k;
  if(i===0){text("F(α) = 0",0,-36,25,colors[0]);text("fixed response and inputs",0,6,13);text("quantity: inverse alpha",0,38,14);}
  else if(i===1){text("solve → reciprocal",0,-37,14);text(f(inverse,8),0,3,21,colors[2]);text("calculation output",0,39,13);}
  else if(i===2){k.ctx.strokeStyle=colors[0];k.ctx.strokeRect(-83,-53,166,106);text("ALPHA_INV",0,-32,14);text(f(c.predicted,8),0,-3,18,colors[2]);text(freeze,0,30,13);}
  else if(i===3){text("measured separately",0,-46,13,colors[1]);text(Number(c.central).toFixed(9),0,-11,18,colors[1]);text(`± ${Number(c.uncertaintyMinus).toExponential(2)}`,0,20,14);text("CODATA 2022",0,49,13);}
  else if(i===4)comparisonGlyph(k,c);
  else{const date=freeze.slice(0,4);line(-76,0,76,0);dot(-49,0,5,colors[1]);dot(49,0,5,colors[2]);text("measurement",-47,-29,12,colors[1]);text("record",49,-29,12,colors[2]);text("2022",-49,26,14);text(date,49,26,14);text("known data comparison",0,57,12);}
}
function cosmology(k:DrawKit,i:number){const {text,line,dot,progress:p}=k;const n=55,ns=1-2/n,r=12/n**2;
  if(i===0){line(-75,0,75,0);[50,55,60].forEach(v=>{const x=-75+(v-50)/10*150;line(x,-7,x,7);text(String(v),x,27,14);});dot(0,0,7,colors[1]);text("external N★",0,-35,17);text("same input for both outputs",0,56,12);}
  else if(i===1){text("2 / 55",0,-42,19,colors[0]);text("1 − 0.036364",0,-8,17);text(`nₛ = ${f(ns,6)}`,0,35,21,colors[1]);}
  else if(i===2){text("55² = 3025",0,-42,18);text("12 / 3025",0,-8,18);text(`r = ${f(r,6)}`,0,35,21,colors[2]);}
  else if(i===3){const x=(q:number)=>-74+(1-2/q-.96)/(.966667-.96)*148,y=(q:number)=>47-(12/q**2-.003333)/(.0048-.003333)*86;line(-79,48,79,48);line(-79,-45,-79,48);k.ctx.beginPath();for(let j=0;j<=60*p;j++){const q=50+10*j/60;k.ctx[j?'lineTo':'moveTo'](x(q),y(q));}k.ctx.strokeStyle=colors[1];k.ctx.lineWidth=2;k.ctx.stroke();if(p>=.5)dot(x(55),y(55),4,colors[2]);text("one curve: r = 3(1−nₛ)²",0,-60,13);text("nₛ →",60,60,12);text("r",-92,-43,12);}
  else if(i===4){text("c₃ = 1/(8π)",0,-43,16);text("raise to 7/2",0,-9,14);text((C3**3.5).toExponential(6),0,26,21,colors[1]);text("mass / reference mass",0,56,12);}
  else if(i===5){text("exp(−2/α)",0,-43,19);text("× 3/(4π²)",0,-8,17);text((3/(4*Math.PI**2)*Math.exp(-2*inverse)).toExponential(5),0,27,20,colors[2]);text("density / reference⁴",0,57,12);}
  else{const scalar=Math.log10(C3**3.5),vac=(Math.log10(3/(4*Math.PI**2))-2*inverse/Math.LN10)/4,x=(v:number)=>-82-v/34*164;line(-82,14,82,14);[0,-10,-20,-30].forEach(v=>text(String(v),x(v),39,12));dot(x(scalar),14,5,colors[1]);dot(x(vac),14,5,colors[2]);text("same energy units",0,-45,15);text("mass",x(scalar),-13,12,colors[1]);text("vacuum",x(vac),-13,12,colors[2]);text("log₁₀(energy / M̄)",0,61,12);}
}
function ring(k:DrawKit,n:number,cx:number,cy:number,r:number,position:number,labels?:number[]){k.ctx.strokeStyle="#53708b";k.ctx.beginPath();k.ctx.arc(cx,cy,r,0,2*Math.PI);k.ctx.stroke();for(let j=0;j<n;j++){const a=-Math.PI/2+j*2*Math.PI/n,x=cx+r*Math.cos(a),y=cy+r*Math.sin(a);k.dot(x,y,9,j===position?colors[1]:"#29435b");k.text(String(labels?.[j]??j),x,y,11,j===position?"#102439":"#d2e2f4");}}
function quantum(k:DrawKit,i:number){const {text,line,dot,bar,progress:p}=k;
  if(i===0){[1,1,0,0,0,0,1,1].forEach((v,j)=>{text(String(v),-84+j*24,-15,21,v?colors[0]:"#7e98b2");});text("11000011",0,-48,15);text("norm²: 4 / 2 = 2",0,33,17,colors[2]);}
  else if(i===1){["1+i","0","0","1+i"].forEach((v,j)=>{text(v,-72+j*48,-10,20,j===0||j===3?colors[1]:"#809bb5");text(["00","01","10","11"][j],-72+j*48,25,13);});text("pair adjacent coordinates",0,-46,13);}
  else if(i===2){text("|1+i|² = 2",0,-43,18);text("2 + 0 + 0 + 2 = 4",0,-10,15);text("divide amplitudes by 2",0,22,14,colors[1]);text("total squared norm = 1",0,52,13);}
  else if(i===3){[.5,0,0,.5].forEach((v,j)=>{verticalBar(k,-85+j*47,-43,28,72,v,colors[j%4]);text(`${v*100}%`,-71+j*47,45,12);text(["00","01","10","11"][j],-71+j*47,-57,12);});}
  else if(i===4){const a=-Math.PI/2+p*Math.PI/2;k.ctx.strokeStyle="#6484a3";k.ctx.beginPath();k.ctx.arc(-42,-8,35,0,2*Math.PI);k.ctx.stroke();line(-42,-8,-42+31*Math.cos(a),-8+31*Math.sin(a),colors[1]);dot(-42+31*Math.cos(a),-8+31*Math.sin(a),4,colors[1]);text("50%",51,-24,18,colors[0]);text("50%",51,9,18,colors[0]);text("one J: same odds",0,51,12);}
  else if(i===5){text("XX",-60,-31,17);text("ZZ",0,-31,17);text("YY",60,-31,17);text("+1",-60,6,21,colors[1]);text("+1",0,6,21,colors[1]);text("−1",60,6,21,colors[2]);text("exact amplitude checks",0,48,13);}
  else if(i===6){const n=Math.min(30,Math.floor(p*30));ring(k,5,-48,-9,31,n%5);ring(k,6,48,-9,31,n%6);text(`step ${n} / 30`,0,48,15);text("5 positions",-48,-59,12);text("6 positions",48,-59,12);}
  else{const n=Math.min(4,Math.floor(p*4)),m=[1,2,4,3,1][n];ring(k,5,0,-4,39,0,Array.from({length:5},(_,j)=>j*m%5));text(`multiply labels by ${m}`,0,52,14,colors[1]);text("positions stay fixed",0,-59,12);}
}
export function drawCalculationStep(chapter:string,index:number,kit:DrawKit,comparison:JourneyComparison,freezeDate:string){
  if(chapter==="alpha")alpha(kit,index,comparison);else if(chapter==="flavor")flavor(kit,index);else if(chapter==="dynamics")dynamics(kit,index);else if(chapter==="predictions")predictions(kit,index,comparison,freezeDate);else if(chapter==="cosmology")cosmology(kit,index);else if(chapter==="quantum")quantum(kit,index);
}
