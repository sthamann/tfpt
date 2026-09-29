"use strict";

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const NS = "http://www.w3.org/2000/svg";

const KINDS = {
  exact: { label: "exakt", help: "Exakte endliche oder algebraische Aussage unter den angegebenen Voraussetzungen." },
  numeric: { label: "numerisch", help: "Numerisch gelöste Gleichung mit ausgewiesenem Vertrag." },
  conditional: { label: "bedingt", help: "Die Rechnung trägt, wenn die angegebene physische Zuordnung gilt." },
  input: { label: "gesetzt", help: "Ausgangsdaten oder Schnittstelle; ihre Herkunft wird hier nicht abgeleitet." },
  open: { label: "offen", help: "Die benötigte physische Verbindung ist noch nicht hergeleitet." }
};

const STAGE_NAMES = {
  origin: "Ursprungsanker", seam: "Naht & gemeinsamer Seed", carrier: "Fünfer-Träger", e8: "E₈-Abschluss",
  clocks: "Coxeter- & Galois-Clocks", flavor: "Flavor-Auslesung", alpha: "α-Fixpunkt", transfer: "Transfer & Rekursion",
  predictions: "Vorhersageregister", gravity: "Gravitationsbrücke", cosmology: "Kosmologischer Zweig",
  hamming: "Binärer Ursprung", rays: "60 Richtungen", code: "Fünfer-Code", observables: "15 Antwortflächen",
  quartic: "Quellenquartik", binding: "Zellbindung", recursion: "Rekursion", space: "Raumkandidat",
  sourcechannel: "Quellenkanal", matterbridge: "Übergang zur Physik",
  observability: "Vollständige Auslese", normalization: "Normierter Vollraum", assembly: "A₃-Montage"
};

const STAGE_EXPLAINERS = {
  origin: "Der Anker (1,1,2) erzeugt die Potenzleiter. Ihre ersten Werte liefern die Zahlen 240, 8 und 248, die später als Wurzelzahl, Rang und Dimension des E₈-Abschlusses geprüft werden.",
  seam: "Vier ausgezeichnete Punkte auf der Naht geben drei unabhängige Zyklen und fünf holomorphe Funktionen. Aus derselben Normierung entsteht der gemeinsame kleine Seed φ₀.",
  carrier: "Die fünf Trägerplätze werden als gerade Außenalgebra gelesen. Dadurch entstehen exakt 16 Zustände mit den angezeigten Hyperladungen; die physische Feldidentifikation ist eine zusätzliche Zuordnung.",
  e8: "D₅ und A₃ werden über vier passende Diskriminantenklassen verklebt. Die explizite Konstruktion ergibt 240 Norm-2-Wurzeln, Rang 8 und Dimension 248.",
  clocks: "Die E₈-Coxeterbewegung schließt nach 30 Schritten. Die vierte Wurzelstruktur μ₄ läuft nicht als Unterzyklus mit, sondern wirkt als Automorphismus auf die Fünfer-Clock.",
  flavor: "Ganzzahlige Familienmatrizen erzeugen die Exponenten der Flavor-Hierarchie. Die Matrixrechnung ist exakt; ihre Lesart als physische Yukawa-Struktur bleibt bedingt.",
  alpha: "Die festgelegte α-Gleichung wird numerisch bis zu ihrer positiven Wurzel gelöst. Die Wurzel ist innerhalb dieses Vertrags eindeutig; die Herleitung genau dieser physikalischen Gleichung bleibt eine eigene Frage.",
  transfer: "Ein festgelegter Transferoperator dämpft zwei Richtungen und lässt eine stationäre Richtung stehen. Der Regler zeigt die Annäherung Schritt für Schritt, setzt aber die Wahl dieses Operators voraus.",
  predictions: "Hier werden die eingefrorenen Ausgaben des gemeinsamen Seeds gesammelt. Jede Zeile behält ihren eigenen Status und ihre physikalische Voraussetzung.",
  gravity: "Eine dimensionslose Compilergröße wird über einen zusätzlichen Skalenanker in GeV gelesen. Die Zahlrechnung ist ausführbar; die Gravitationsidentifikation ist bedingt.",
  cosmology: "Aus dem gewählten e-fold-Wert werden Aₛ, nₛ, r und das Vakuumverhältnis berechnet. Der Regler macht sichtbar, welche Ausgaben von dieser externen Wahl abhängen.",
  hamming: "Der erweiterte binäre Hamming-Code besitzt 16 Wörter mit Gewichten 0, 4 und 8. Er bildet die endliche 4-Bit-Struktur ab, aus der die folgenden Quantenobjekte konstruiert werden.",
  rays: "Aus der endlichen symplektischen Struktur entstehen 60 Strahlen in 15 orthogonalen Viererkontexten. Die Grafik zeigt ihre tatsächlichen Nachbarschaften.",
  code: "Der 256-dimensionale Operator wird vollständig diagonalisiert. Die Balken zeigen seine fünf Eigenwerte und deren Multiplizitäten.",
  observables: "Fünf ausgewählte Antwortkoordinaten werden als konkrete Matrix berechnet. Ihre Eigenwerte trennen zwei positive von drei negativen Richtungen.",
  quartic: "Sechs komplexe Quellenkoordinaten werden auf eine Quartik gesetzt. Der angezeigte Residual prüft die Gleichung numerisch nahe Maschinenpräzision.",
  binding: "Ein endlicher Bindungsoperator bevorzugt gemeinsam beschriftete Zellen gegenüber unabhängigen Labels. Spektrum und Gegenvergleich zeigen die konkrete Energielücke.",
  recursion: "Jede Zelle verzweigt dreifach; ausgewählte Moden werden bei jeder Tiefe weitergetragen. Die Zeichnung zeigt die Struktur schematisch, die angegebenen Zellzahlen stammen aus der vollständigen Rechnung.",
  space: "Matchings und Paare bilden einen endlichen Zustandsgraphen mit markiertem Lauf und Periodenbasis. Seine Deutung als Raum ist eine bedingte Brücke.",
  sourcechannel: "Ein vollständig positiver endlicher Kanal entwickelt Populationen und drei auslesbare Antworten. Er liefert eine echte Dynamik, aber noch keine Herleitung der materiellen Anfangsquelle.",
  matterbridge: "Der bisher berechnete endliche Pfad wird den offenen Übergängen T2–T8 gegenübergestellt. Rot markierte Knoten benennen genau die noch fehlenden physikalischen Verbindungen.",
  observability: "Der geschützte Fünfer entsteht als Schnitt zweier berechneter Räume. Paarbeobachtungen sehen zehn Operatorrichtungen; zwei Kommutatorschritte mit codeerhaltenden Kontrollen öffnen erst 20 und dann alle 25.",
  normalization: "Der unveränderte Lift wirkt auf dem geschützten Code korrekt, ist im vollen 256erraum aber nicht spurtreu. Eine berechnete Normierung in der erzeugten Operatoralgebra repariert den Vollraum und lässt jeden Codezweig gleich.",
  assembly: "Zehn explizite Dreierpfade überdecken alle 30 Knoten des markierten periodischen Netzes genau einmal. Die geänderte Bindung transportiert Matrizen ladungskovariant; die Wahl dieses Netzes als physischer Raum bleibt bedingt."
};

const GROUPS = {
  origin: "01 · Ursprung & Naht", compiler: "02 · Algebraischer Compiler", clocks: "03 · Clocks & Dynamik",
  response: "04 · Auslesung", physics: "05 · Physische Brücken", universalraum: "06 · Endlicher Prozess",
  consolidation: "07 · Konsolidierung"
};

const app = {
  snapshot: null,
  previous: null,
  defaults: null,
  changed: new Set(),
  selected: null,
  journeyIndex: 0,
  tourIndex: 0,
  tourLens: "geometry",
  implicationIndex: 0,
  compositionView: "encoder",
  historyPhase: false,
  markerIndex: 0,
  originLoop: "structural",
  originNode: 0,
  originTransferDepth: 1,
  jointCarrier: 'path',
  sourceReplayStep: 3,
  pairSymmetry: 'full',
  currentBridgeView: 'pair',
  currentGeometryIndex: 8,
  currentClusterIndex: 5,
  flavorPathStep: 0,
  catalog: null,
  catalogPage: 0,
  evidencePageSize: 100,
  lean: null,
  leanTab: "replay",
  timers: new Set(),
  activeView: "overview"
};

function escapeHTML(value) {
  return String(value ?? "").replace(/[&<>'"]/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"})[char]);
}

function fmt(value, precision = 7) {
  if (value === null || value === undefined) return "–";
  if (typeof value === "boolean") return value ? "ja" : "nein";
  if (typeof value === "number") {
    if (!Number.isFinite(value)) return String(value);
    const abs = Math.abs(value);
    if (abs !== 0 && (abs < 1e-5 || abs >= 1e7)) return value.toExponential(4).replace("e+", "e");
    return new Intl.NumberFormat("de-DE", { maximumSignificantDigits: precision }).format(value);
  }
  if (typeof value === "string") return value;
  if (value.fraction !== undefined) return `${value.fraction} ≈ ${fmt(value.value)}`;
  if (value.real !== undefined || value.re !== undefined) {
    const re = value.real ?? value.re ?? 0, im = value.imag ?? value.im ?? 0;
    return `${fmt(re)}${im >= 0 ? "+" : ""}${fmt(im)}i`;
  }
  if (Array.isArray(value)) {
    if (value.length > 10) return `[${value.slice(0, 8).map(v => fmt(v, 5)).join(", ")}, …]`;
    return `[${value.map(v => fmt(v, 5)).join(", ")}]`;
  }
  const entries = Object.entries(value);
  if (entries.length <= 5) return entries.map(([k,v]) => `${k}: ${fmt(v, 5)}`).join(" · ");
  return JSON.stringify(value);
}

function valueHTML(value) { return `<span class="data-value">${escapeHTML(fmt(value))}</span>`; }
function kindBadge(kind) { const meta = KINDS[kind] || {label: kind, help: ""}; return `<span class="kind-badge kind-${escapeHTML(kind)}" title="${escapeHTML(meta.help)}">${escapeHTML(meta.label)}</span>`; }
function stageName(stageOrId) { const id = typeof stageOrId === "string" ? stageOrId : stageOrId.id; return STAGE_NAMES[id] || (stageOrId.title || id); }

async function api(path, options = {}) {
  const response = await fetch(path, options);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
  return data;
}

function toast(message) {
  const node = $("#toast");
  node.textContent = message; node.hidden = false;
  setTimeout(() => { node.hidden = true; }, 4200);
}

function setHeader(status, label) {
  const node = $("#header-state");
  node.innerHTML = `<span class="state-dot is-${status}"></span><span>${escapeHTML(label)}</span>`;
}

const VIEW_ROUTES={gesamtbild:'overview',overview:'overview',tour:'tour',quellgesetz:'tour',zusammenhang:'tour',graphen:'tour',prozesskern:'tour',quellenanschluss:'tour',quellenrekursion:'tour',flavorpfad:'tour','gemeinsame-physik':'tour',raummarker:'tour',zuse:'tour',journey:'journey',evidence:'evidence',lean:'lean'};

function scrollTourRoute(route,behavior='smooth') {
  const target=route==='quellgesetz'?$('#source-program'):route==='zusammenhang'?$('#tour-consequences'):route==='graphen'?$('#source-graph-tour'):route==='prozesskern'?$('#process-kernel'):route==='quellenanschluss'?$('#current-source-geometry'):route==='quellenrekursion'?$('#current-source-recursion'):route==='flavorpfad'?$('#flavorpfad'):route==='gemeinsame-physik'?$('#gemeinsames-woerterbuch'):route==='raummarker'?$('#marker-demo'):route==='zuse'?$('#zuse-aspects'):null;
  if(target&&!target.hidden)target.scrollIntoView({behavior:behavior==='auto'?'instant':behavior,block:'start'});
}

function setView(name, focus = true, route = null) {
  app.activeView = name;
  $$("[data-view-panel]").forEach(panel => { panel.hidden = panel.dataset.viewPanel !== name; panel.classList.toggle("is-active", panel.dataset.viewPanel === name); });
  $$(".nav-link").forEach(button => { const on = button.dataset.view === name; button.classList.toggle("is-active", on); button.setAttribute("aria-current", on ? "page" : "false"); });
  history.replaceState(null, "", `#${route||(name === "overview" ? "gesamtbild" : name)}`);
  if (focus) { const panel = $(`[data-view-panel="${name}"]`); const title = $("h1", panel); title?.focus?.({preventScroll:true}); window.scrollTo({top:0, behavior:"smooth"}); }
  if (name === "evidence") loadCatalog();
  if (name === "lean") loadLean();
  if (name === "tour") {renderTour();scrollTourRoute(route,focus?'smooth':'auto');}
}

function configureControls(values) {
  const map = {clock_step:"clock-step", transfer_steps:"transfer-steps", recursion_depth:"recursion-depth", efolds:"efolds", phase_b:"phase-b", initial_state:"initial-state"};
  Object.entries(map).forEach(([key,id]) => { const node = $(`#${id}`); if (values[key] !== undefined) node.value = key==="phase_b" ? Math.round(Number(values[key])*144) : values[key]; });
  updateControlLabels();
}

function phaseFraction(value) {
  const candidates = [[0,"0"],[1/144,"1/144"],[1/72,"1/72"],[1/48,"1/48"],[1/36,"1/36"],[1/24,"1/24"],[1/18,"1/18"],[1/16,"1/16"],[1/12,"1/12"],[1/9,"1/9"],[1/6,"1/6"],[2/9,"2/9"]];
  const hit = candidates.find(([v]) => Math.abs(v-value)<.0005); return hit ? hit[1] : fmt(value,4);
}

function updateControlLabels() {
  $("#clock-step-value").value = $("#clock-step").value;
  $("#transfer-steps-value").value = $("#transfer-steps").value;
  $("#recursion-depth-value").value = $("#recursion-depth").value;
  $("#efolds-value").value = $("#efolds").value;
  const phase=Number($("#phase-b").value)/144, phaseLabel=phaseFraction(phase);
  $("#phase-b-value").value = phaseLabel;
  $("#phase-b").setAttribute("aria-valuetext",phaseLabel);
}

function getConfig() {
  return {
    clock_step: Number($("#clock-step").value), transfer_steps: Number($("#transfer-steps").value),
    recursion_depth: Number($("#recursion-depth").value), efolds: Number($("#efolds").value),
    phase_b: Number($("#phase-b").value)/144, initial_state: $("#initial-state").value
  };
}

function outputSignature(stage) { return JSON.stringify(stage.outputs || []); }
function computeChanged(previous, next) {
  const before = new Map((previous?.stages || []).map(stage => [stage.id, outputSignature(stage)]));
  return new Set((next?.stages || []).filter(stage => before.has(stage.id) && before.get(stage.id) !== outputSignature(stage)).map(stage => stage.id));
}

function applySnapshot(snapshot) {
  if (!snapshot) return;
  app.previous = app.snapshot;
  app.changed = computeChanged(app.snapshot, snapshot);
  app.snapshot = snapshot;
  app.selected ||= snapshot.stages[0]?.id;
  renderSummary(); renderMap(); renderDetail(); renderJourney(); renderTour(); scrollTourRoute(location.hash.slice(1),'auto');
  if (app.changed.size) {
    const names = [...app.changed].map(id => stageName(id));
    const strip = $("#change-strip"); strip.hidden = false;
    strip.innerHTML = `<strong>${app.changed.size} Schritte verändert:</strong> ${escapeHTML(names.join(", "))}`;
  }
  setHeader(snapshot.summary.failed ? "bad" : "good", `Ablauf ${snapshot.summary.passed}/${snapshot.summary.checks}`);
}

function renderSummary() {
  const s = app.snapshot?.summary; if (!s) return;
  $("#summary-score").textContent = `${s.passed}/${s.checks}`;
  $("#summary-label").textContent = s.failed ? `${s.failed} Prüfung(en) fehlgeschlagen` : "Prüfungen dieses Ablaufs bestanden";
  $("#summary-stages").textContent = s.stages;
  $("#summary-checks").textContent = s.checks;
  $("#summary-time").textContent = `${fmt(s.elapsed_ms)} ms`;
}

function svgEl(name, attrs = {}, text = "") {
  const node = document.createElementNS(NS, name);
  Object.entries(attrs).forEach(([key,value]) => node.setAttribute(key, value));
  if (text) node.textContent = text;
  return node;
}

function mapPositions(stages) {
  const rows = [
    ["origin","seam"], ["carrier","e8"], ["clocks","flavor","alpha","transfer","predictions","gravity","cosmology"],
    ["hamming","rays","code","observables","quartic","binding","recursion","space","sourcechannel","matterbridge"],
    ["observability","normalization","assembly"]
  ];
  const ys = [82, 214, 350, 510, 670], positions = {};
  rows.forEach((ids,row) => ids.forEach((id,index) => positions[id] = {x: 54 + index * 160, y: ys[row]}));
  stages.filter(stage => !positions[stage.id]).forEach((stage,index) => positions[stage.id] = {x:574 + index*160, y:670});
  return positions;
}

function relatedNodes(id) {
  if (!id) {
    const all=new Set((app.snapshot?.stages||[]).map(stage=>stage.id));
    return {all,upstream:new Set(),downstream:new Set()};
  }
  const edges = app.snapshot?.edges || [], upstream = new Set([id]), downstream = new Set([id]);
  let changed = true;
  while (changed) { changed = false; edges.forEach(e => { if (upstream.has(e.target) && !upstream.has(e.source)) { upstream.add(e.source); changed=true; } }); }
  changed = true;
  while (changed) { changed = false; edges.forEach(e => { if (downstream.has(e.source) && !downstream.has(e.target)) { downstream.add(e.target); changed=true; } }); }
  return {all:new Set([...upstream,...downstream]), upstream, downstream};
}

function renderMap() {
  const root = $("#system-map-wrap"), snapshot = app.snapshot; if (!snapshot) return;
  root.innerHTML = "";
  const svg = svgEl("svg", {class:"system-map", viewBox:"0 0 1680 820", role:"group", "aria-labelledby":"map-svg-title map-svg-desc"});
  svg.append(svgEl("title", {id:"map-svg-title"}, `Abhängigkeitskarte der ${snapshot.stages.length} ausführbaren TFPT-Schritte`));
  svg.append(svgEl("desc", {id:"map-svg-desc"}, "Fünf Lesebahnen zeigen Ursprung, algebraischen Compiler, Auslesung, endlichen Prozess und die berechnete Konsolidierung. Knoten sind per Tastatur auswählbar."));
  const defs = svgEl("defs");
  [["arrow","#78958b"],["arrow-amber",getComputedStyle(document.documentElement).getPropertyValue("--amber")],["arrow-lavender",getComputedStyle(document.documentElement).getPropertyValue("--lavender")]].forEach(([id,color]) => {
    const marker=svgEl("marker",{id,viewBox:"0 0 10 10",refX:"9",refY:"5",markerWidth:"6",markerHeight:"6",orient:"auto-start-reverse"}); marker.append(svgEl("path",{d:"M 0 0 L 10 5 L 0 10 z",fill:color})); defs.append(marker);
  }); svg.append(defs);
  const laneInfo = [[25,45,1630,105,"Ursprung · rückgekoppelter Abschluss"],[25,177,1630,105,"Algebraischer Compiler"],[25,313,1630,105,"Clocks, Auslesung & physische Kanäle"],[25,473,1630,105,"Endlicher Prozess · Universalraum-Brücke"],[25,633,1630,105,"Konsolidierung · Auslese, Normierung & Montage"]];
  laneInfo.forEach(([x,y,w,h,label],i) => { svg.append(svgEl("rect",{x,y,width:w,height:h,rx:16,class:`map-lane ${i%2?'alt':''}`})); svg.append(svgEl("text",{x:x+16,y:y+19,class:"map-lane-title"},label)); });
  const positions = mapPositions(snapshot.stages), selected = relatedNodes(app.selected);
  snapshot.edges.forEach((edge,index) => {
    const a=positions[edge.source], b=positions[edge.target]; if (!a||!b) return;
    const sx=a.x+132, sy=a.y+28, tx=b.x, ty=b.y+28;
    const sameRow=Math.abs(sy-ty)<20; const d=sameRow ? `M${sx},${sy} C${sx+20},${sy} ${tx-20},${ty} ${tx},${ty}` : `M${sx-66},${sy+28} C${sx-66},${sy+70} ${tx+66},${ty-48} ${tx+66},${ty}`;
    const edgeState=!app.selected?"":selected.all.has(edge.source)&&selected.all.has(edge.target)?"is-active":"is-muted";
    const path=svgEl("path",{d,class:`map-edge ${edge.relation} ${edgeState}`,"data-edge":index}); path.append(svgEl("title",{},`${stageName(edge.source)} → ${stageName(edge.target)}: ${edge.label || edge.relation}`)); svg.append(path);
  });
  snapshot.stages.forEach((stage,index) => {
    const p=positions[stage.id], selectedClass=!app.selected?"is-overview":stage.id===app.selected?"is-selected":selected.all.has(stage.id)?"is-related":"is-muted";
    const g=svgEl("g",{class:`map-node kind-${stage.kind} ${selectedClass} ${app.changed.has(stage.id)?"is-changed":""}`,transform:`translate(${p.x} ${p.y})`,tabindex:"0",role:"button","aria-label":`${stageName(stage)}, ${KINDS[stage.kind]?.label || stage.kind}`});
    g.append(svgEl("rect",{width:132,height:58,rx:10})); g.append(svgEl("rect",{class:"node-accent",width:5,height:40,x:8,y:9,rx:2}));
    g.append(svgEl("text",{class:"node-order",x:20,y:15},String(index+1).padStart(2,"0")));
    const words=stageName(stage).split(" "), line1=words.slice(0,3).join(" "), line2=words.slice(3).join(" ");
    g.append(svgEl("text",{class:"node-title",x:20,y:32},line1)); if(line2)g.append(svgEl("text",{class:"node-title",x:20,y:46},line2));
    g.append(svgEl("text",{class:"node-kind",x:122,y:15,"text-anchor":"end"},KINDS[stage.kind]?.label||stage.kind));
    const activate=()=>selectStage(stage.id,true); g.addEventListener("click",activate); g.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();activate();}}); svg.append(g);
  });
  root.append(svg);
  const selectedStage=snapshot.stages.find(s=>s.id===app.selected);
  $("#map-inspector").innerHTML = selectedStage ? `<p>${kindBadge(selectedStage.kind)} <strong>${escapeHTML(stageName(selectedStage))}</strong> · ${escapeHTML(STAGE_EXPLAINERS[selectedStage.id]||selectedStage.summary)} <button class="mini-button" id="map-open-detail">Details öffnen</button> <button class="mini-button" id="map-reset">Alle Verbindungen</button></p>` : `<p><strong>Gesamtansicht:</strong> alle ${snapshot.stages.length} Schritte und ${snapshot.edges.length} typisierten Abhängigkeiten. Wähle einen Knoten, um seinen Vor- und Nachlauf hervorzuheben.</p>`;
  $("#map-open-detail")?.addEventListener("click",()=>$("#stage-detail").scrollIntoView({behavior:"smooth",block:"start"}));
  $("#map-reset")?.addEventListener("click",()=>{app.selected=null;renderMap();renderDetail();});
}

function selectStage(id, scroll=false) {
  app.selected=id; renderMap(); renderDetail();
  const index=app.snapshot?.stages.findIndex(stage=>stage.id===id); if(index>=0){app.journeyIndex=index;renderJourney();}
  if(scroll) $("#stage-detail").scrollIntoView({behavior:"smooth",block:"start"});
}

function sourceURL(source) {
  const path=source.url||source.path||'';
  const parsedLine=Number.parseInt(source.lines,10),parsedPage=Number.parseInt(source.pages,10);
  const line=source.line??(Number.isFinite(parsedLine)?parsedLine:1),pageValue=source.page??(Number.isFinite(parsedPage)?parsedPage:null);
  if(/^https?:\/\//i.test(path))return pageValue?`${path}#page=${encodeURIComponent(pageValue)}`:path;
  const url=`/source?path=${encodeURIComponent(path)}&line=${encodeURIComponent(line)}`;
  if(!pageValue)return url;
  const page=encodeURIComponent(pageValue);
  return /\.pdf$/i.test(path)?`${url}&page=${page}#page=${page}`:`${url}#page=${page}`;
}

function renderDetailInto(root, stage, journey=false) {
  if (!stage) { root.innerHTML = `<div class="empty-state">Noch kein Schritt gewählt.</div>`; return; }
  const inputs=(stage.inputs||[]).map(x=>`<li><span class="value-name">${escapeHTML(x.name)}</span>${valueHTML(x.value)}${x.origin?`<small> · ${escapeHTML(x.origin)}</small>`:""}</li>`).join("");
  const outputs=(stage.outputs||[]).map(x=>`<li><span class="value-name">${escapeHTML(x.name)}</span>${valueHTML(x.value)}${x.unit?` <small>${escapeHTML(x.unit)}</small>`:""}</li>`).join("");
  const checks=(stage.checks||[]).map(c=>`<div class="check-row"><span class="check-icon ${c.ok?'':'fail'}">${c.ok?'✓':'!'}</span><div><strong>${escapeHTML(c.name)}</strong><div class="check-method">${escapeHTML(c.method||'')}</div></div><div class="check-actual">${valueHTML(c.actual)}</div></div>`).join("");
  const assumptions=(stage.assumptions||[]).map(x=>`<li>${escapeHTML(x)}</li>`).join("");
  const notes=(stage.notes||[]).map(x=>`<li>${escapeHTML(x)}</li>`).join("");
  const formulas=(stage.formulas||[]).map((x,i)=>`<details><summary>Formel ${i+1}</summary><pre class="formula">${escapeHTML(x)}</pre></details>`).join("");
  const sources=(stage.sources||[]).map(s=>`<a class="source-link" href="${sourceURL(s)}" target="_blank" rel="noopener"><strong>${escapeHTML(s.claim||s.label||s.path||s.url)}</strong><small>${escapeHTML(s.path||s.url)}${s.line?` · Zeile ${s.line}`:''} ↗</small></a>`).join("");
  const lean = stage.lean ? `<section class="detail-block"><h4>Auch aus Lean berechnet</h4><p>${escapeHTML(stage.lean.scope||'Originaldefinition nativ ausgeführt.')}</p><div class="checks">${(stage.lean.checks||[]).map(c=>`<div class="check-row"><span class="check-icon ${c.ok?'':'fail'}">${c.ok?'✓':'!'}</span><div><strong>${escapeHTML(c.name)}</strong><div class="check-method">Lean ${escapeHTML(fmt(c.lean))} · Python ${escapeHTML(fmt(c.python))}</div></div></div>`).join('')}</div>${stage.lean.finished_at?`<small>Ausgeführt: ${escapeHTML(new Date(stage.lean.finished_at).toLocaleString('de-DE'))}</small>`:''}${stage.lean.source?`<p><a class="source-link" target="_blank" rel="noopener" href="${sourceURL(stage.lean.source)}">Originale Lean-Quelle öffnen ↗</a></p>`:''}</section>` : '';
  root.innerHTML = `<div class="detail-shell">
    <article class="detail-main"><header class="detail-head"><div><p class="eyebrow">${escapeHTML(GROUPS[stage.group]||stage.group)} · Schritt ${stage.order}</p><h3>${escapeHTML(stageName(stage))}</h3><p>${escapeHTML(stage.subtitle)}</p></div>${kindBadge(stage.kind)}</header>
      <p class="detail-summary">${escapeHTML(STAGE_EXPLAINERS[stage.id]||stage.summary)}</p>
      ${STAGE_EXPLAINERS[stage.id]&&stage.summary?`<details class="technical-summary"><summary>Technischer Originaltext</summary><p>${escapeHTML(stage.summary)}</p></details>`:''}
      <div class="io-flow"><div class="io-box"><h4>Eingang</h4><ul class="value-list">${inputs||'<li>Keine vorgeschaltete Eingabe</li>'}</ul></div><div class="io-arrow" aria-hidden="true">→</div><div class="io-box operation"><h4>Operation</h4><p>${escapeHTML(stage.formulas?.[0]||stage.summary)}</p></div><div class="io-arrow" aria-hidden="true">→</div><div class="io-box"><h4>Ergebnis</h4><ul class="value-list">${outputs}</ul></div></div>
      <div class="visual-panel" id="visual-${escapeHTML(stage.id)}" aria-label="Wissenschaftliche Visualisierung: ${escapeHTML(stageName(stage))}"></div>
      <section class="checks"><h4>Prüfungen dieses Schritts</h4>${checks||'<p>Keine Einzelprüfung ausgewiesen.</p>'}</section>${lean}
    </article>
    <aside class="detail-side"><section class="detail-block" style="border-top:0;margin-top:0;padding-top:0"><h4>Geltungsgrenze</h4><p>${escapeHTML(KINDS[stage.kind]?.help||'')}</p>${assumptions?`<ul>${assumptions}</ul>`:'<p>Keine zusätzliche Annahme in diesem Schritt ausgewiesen.</p>'}</section>
      ${notes?`<section class="detail-block"><h4>Einordnung</h4><ul>${notes}</ul></section>`:''}
      ${formulas?`<section class="detail-block"><h4>Formeln</h4>${formulas}</section>`:''}
      <section class="detail-block"><h4>Originalquellen</h4><div class="source-list">${sources||'<p>Keine Quelle verknüpft.</p>'}</div></section>
      ${!journey?`<section class="detail-block"><button class="button quiet stage-evidence" data-stage="${escapeHTML(stage.id)}">Belege zu diesem Schritt zeigen</button></section>`:''}
    </aside></div>`;
  renderVisual($(`#visual-${CSS.escape(stage.id)}`,root), stage);
  $(".stage-evidence",root)?.addEventListener("click",()=>{ setView("evidence"); $("#evidence-stage").value=stage.id; app.catalogPage=0; renderCatalog(); });
}

function renderDetail() { renderDetailInto($("#detail-content"), app.snapshot?.stages.find(s=>s.id===app.selected)); }

function createChartSVG(title) {
  const svg=svgEl("svg",{viewBox:"0 0 560 300",role:"img"}); svg.append(svgEl("title",{},title)); svg.append(svgEl("text",{x:18,y:23,class:"visual-title"},title)); return svg;
}
function numericArray(value) { return Array.isArray(value) ? value.map(v=>typeof v==="number"?v:Number(v?.value??v)).filter(Number.isFinite) : []; }
function getXY(point,index) { if(Array.isArray(point))return {x:Number(point[0]),y:Number(point[1])}; if(point&&typeof point==='object')return {x:Number(point.x??point.alpha??point.step??index),y:Number(point.y??point.value??point.residual??Object.values(point).find(v=>typeof v==='number'))}; return {x:index,y:Number(point)}; }

function lineChart(title, series, labels={}) {
  const svg=createChartSVG(title), W=520,H=225,L=44,T=42;
  const clean=series.map((s,si)=>({name:s.name||`Reihe ${si+1}`,values:(s.values||[]).map(getXY).filter(p=>Number.isFinite(p.x)&&Number.isFinite(p.y))})).filter(s=>s.values.length);
  const pts=clean.flatMap(s=>s.values); if(!pts.length){svg.append(svgEl("text",{x:24,y:150,class:"chart-note"},"Keine numerische Reihe verfügbar"));return svg;}
  let xmin=Math.min(...pts.map(p=>p.x)),xmax=Math.max(...pts.map(p=>p.x)),ymin=Math.min(...pts.map(p=>p.y)),ymax=Math.max(...pts.map(p=>p.y)); if(xmin===xmax)xmax=xmin+1;if(ymin===ymax)ymax=ymin+1;
  const sx=x=>L+(x-xmin)/(xmax-xmin)*W, sy=y=>T+H-(y-ymin)/(ymax-ymin)*H;
  for(let i=0;i<=4;i++){const y=T+H*i/4;svg.append(svgEl("line",{x1:L,y1:y,x2:L+W,y2:y,class:"grid-line"}));svg.append(svgEl("text",{x:L-6,y:y+3,"text-anchor":"end",class:"axis-label"},fmt(ymax-(ymax-ymin)*i/4,4)));}
  clean.forEach((s,si)=>{const d=s.values.map((p,i)=>`${i?'L':'M'}${sx(p.x)},${sy(p.y)}`).join(' ');svg.append(svgEl("path",{d,class:`chart-line ${si?'secondary':''}`}));s.values.forEach(p=>svg.append(svgEl("circle",{cx:sx(p.x),cy:sy(p.y),r:si?2.5:3.5,class:"chart-point"})));svg.append(svgEl("text",{x:L+si*150,y:288,class:"chart-note"},`${si?'◇':'●'} ${s.name}`));});
  svg.append(svgEl("text",{x:L+W/2,y:288,"text-anchor":"middle",class:"axis-label"},labels.x||"Schritt")); return svg;
}

function matrixVisual(title, matrix) {
  const svg=createChartSVG(title), rows=Array.isArray(matrix)?matrix:[], cols=Math.max(1,...rows.map(r=>Array.isArray(r)?r.length:0));
  const values=rows.flat().map(Number).filter(Number.isFinite), max=Math.max(...values.map(Math.abs),1); const cw=Math.min(65,430/cols),ch=Math.min(50,210/Math.max(rows.length,1)),ox=65,oy=50;
  rows.forEach((row,r)=>row.forEach((value,c)=>{const n=Number(value?.value??value)||0,alpha=.12+.76*Math.abs(n)/max;svg.append(svgEl("rect",{x:ox+c*cw,y:oy+r*ch,width:cw-2,height:ch-2,rx:4,class:"matrix-cell",fill:n<0?`rgba(113,96,165,${alpha})`:`rgba(18,79,66,${alpha})`}));svg.append(svgEl("text",{x:ox+c*cw+(cw-2)/2,y:oy+r*ch+(ch-2)/2,class:"matrix-text",fill:alpha>.55?'white':'#15221d'},fmt(value,4)));})); return svg;
}

function barChart(title, values, xLabel = "Kategorie") {
  const svg=createChartSVG(title), clean=values.filter(item=>Number.isFinite(Number(item.value))).slice(0,16);
  const max=Math.max(...clean.map(item=>Math.abs(Number(item.value))),1), width=440/Math.max(clean.length,1), bar=Math.min(58,width-7);
  clean.forEach((item,index)=>{const value=Number(item.value),height=178*Math.abs(value)/max,x=58+index*width,y=value>=0?245-height:245;
    svg.append(svgEl("rect",{x,y,width:bar,height,rx:4,class:`chart-bar ${index%2?'secondary':''}`}));
    svg.append(svgEl("text",{x:x+bar/2,y:265,"text-anchor":"middle",class:"axis-label"},String(item.label).slice(0,10)));
    svg.append(svgEl("text",{x:x+bar/2,y:Math.max(48,y-5),"text-anchor":"middle",class:"chart-note"},fmt(value,4)));
  });
  svg.append(svgEl("line",{x1:45,y1:245,x2:530,y2:245,class:"grid-line"}));
  svg.append(svgEl("text",{x:285,y:292,"text-anchor":"middle",class:"axis-label"},xLabel));
  return svg;
}

function networkVisual(title, data, type) {
  const svg=createChartSVG(title), nodes=data.nodes||[], edges=data.edges||[], placed=new Map();
  nodes.slice(0,60).forEach((node,index)=>{const count=Math.min(nodes.length,60),angle=2*Math.PI*index/Math.max(count,1)-Math.PI/2;
    const ring=count>30?(index%2?110:73):count>16?(index%3===0?76:108):105;
    placed.set(node.id??node.name??index,{x:280+Math.cos(angle)*ring,y:150+Math.sin(angle)*ring,node});
  });
  edges.slice(0,220).forEach(edge=>{const from=placed.get(edge.source),to=placed.get(edge.target); if(!from||!to)return;
    const open=edge.status==='open'; svg.append(svgEl("line",{x1:from.x,y1:from.y,x2:to.x,y2:to.y,stroke:open?'#a33c35':'#aabdb4',"stroke-width":open?2:1,opacity:.72,"stroke-dasharray":open?'5 4':''}));
  });
  placed.forEach(({x,y,node})=>{const open=node.status==='open',marked=node.marked;
    svg.append(svgEl("circle",{cx:x,cy:y,r:open?7:marked?6:3.6,fill:open?'#a33c35':marked?'#7160a5':'#124f42'}));
    if(nodes.length<22)svg.append(svgEl("text",{x:x+8,y:y+3,class:"chart-note"},String(node.label??node.id??'')));
  });
  const note=type==='bridge'?`${nodes.length} Stationen · rote Knoten sind offene Übergänge`:type==='lattice'?`${nodes.length} Zustände · markierter Lauf und Periodenbasis im Datensatz`:`${nodes.length} Strahlen · Orthogonalitätskanten aus 15 Viererkontexten`;
  svg.append(svgEl("text",{x:280,y:290,"text-anchor":"middle",class:"chart-note"},note));
  return svg;
}

function flowVisual(title, data) {
  const svg=createChartSVG(title), source=data.source_path||[], readout=data.readout_path||[];
  svg.append(svgEl("text",{x:28,y:54,class:"chart-note"},"Quellraum wird eingegrenzt"));
  source.forEach((item,index)=>{
    const x=34+index*172,w=132,h=50,y=72;
    svg.append(svgEl("rect",{x,y,width:w,height:h,rx:10,fill:index===source.length-1?'#e9e3f5':'#e3efe9',stroke:index===source.length-1?'#7160a5':'#8baba0'}));
    svg.append(svgEl("text",{x:x+w/2,y:y+20,"text-anchor":"middle",class:"chart-note"},String(item.label||item.id||'')));
    svg.append(svgEl("text",{x:x+w/2,y:y+41,"text-anchor":"middle",class:"visual-title"},fmt(item.dimension)));
    if(index<source.length-1)svg.append(svgEl("path",{d:`M${x+w},${y+h/2}L${x+166},${y+h/2}`,class:"chart-line"}));
  });
  svg.append(svgEl("text",{x:28,y:164,class:"chart-note"},"Erlaubte Kontrollen schließen die Auslese"));
  readout.forEach((item,index)=>{
    const x=34+index*172,w=132,y=184;
    svg.append(svgEl("circle",{cx:x+66,cy:y+30,r:26+Math.sqrt(Number(item.dimension)||1)*3.2,fill:index===readout.length-1?'#7160a5':'#124f42',opacity:.88}));
    svg.append(svgEl("text",{x:x+66,y:y+36,"text-anchor":"middle",fill:"white","font-size":18,"font-weight":800},fmt(item.dimension)));
    svg.append(svgEl("text",{x:x+66,y:278,"text-anchor":"middle",class:"chart-note"},String(item.label||`Schritt ${index}`)));
    if(index<readout.length-1)svg.append(svgEl("path",{d:`M${x+105},${y+30}L${x+165},${y+30}`,class:"chart-line"}));
  });
  return svg;
}

function sectorBalanceVisual(title, data) {
  const svg=createChartSVG(title), before=data.before||[], after=data.after||[];
  const drawPanel=(items,x,label,accent)=>{
    svg.append(svgEl("rect",{x,y:58,width:205,height:176,rx:14,fill:"#f9fbf9",stroke:"#cbd7d0"}));
    svg.append(svgEl("text",{x:x+102,y:82,"text-anchor":"middle",class:"visual-title"},label));
    items.slice(0,3).forEach((item,index)=>{
      const value=Number(item.weight)||0,barWidth=Math.min(142,128*value),y=111+index*62;
      svg.append(svgEl("rect",{x:x+24,y,width:barWidth,height:22,rx:5,fill:index?accent:'#124f42',opacity:.9}));
      svg.append(svgEl("line",{x1:x+24+128,y1:y-5,x2:x+24+128,y2:y+31,stroke:"#a96508","stroke-width":2,"stroke-dasharray":"4 3"}));
      svg.append(svgEl("text",{x:x+24,y:y+41,class:"chart-note"},`${item.sector}: ${fmt(value,8)}`));
    });
  };
  drawPanel(before,32,"Vor der Normierung","#a33c35");
  svg.append(svgEl("text",{x:280,y:145,"text-anchor":"middle",class:"visual-title"},"→"));
  drawPanel(after,323,"Nach der Normierung","#7160a5");
  const maxLift=Math.max(...numericArray(data.lift_spectrum||[]),0);
  svg.append(svgEl("text",{x:280,y:278,"text-anchor":"middle",class:"chart-note"},`Codezweig bleibt bei 1 · voller Lift zuvor max. ${fmt(maxLift,8)}`));
  return svg;
}

function assemblyLatticeVisual(title, data) {
  const svg=createChartSVG(title), nodes=data.nodes||[], edges=data.strong_edges||[], placed=new Map(), colors=['#124f42','#7160a5','#a96508','#46749b','#6e8750'];
  nodes.forEach((node,index)=>{
    const matching=node.group==='matching', local=matching?index:index-15, x=34+local*35.1, y=matching?92:207;
    placed.set(node.id,{x,y,node});
  });
  edges.forEach(edge=>{const a=placed.get(edge.source),b=placed.get(edge.target);if(!a||!b)return;svg.append(svgEl("line",{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:colors[(edge.trimer||0)%colors.length],"stroke-width":2.4,opacity:.72}));});
  placed.forEach(({x,y,node})=>{const color=colors[(node.trimer||0)%colors.length];svg.append(svgEl("circle",{cx:x,cy:y,r:8,fill:color,stroke:"white","stroke-width":2}));svg.append(svgEl("text",{x,y:y+3,"text-anchor":"middle",fill:"white","font-size":7},String(node.id)));});
  svg.append(svgEl("text",{x:28,y:55,class:"chart-note"},"15 Matchings"));
  svg.append(svgEl("text",{x:28,y:171,class:"chart-note"},"15 Paare"));
  svg.append(svgEl("text",{x:280,y:267,"text-anchor":"middle",class:"chart-note"},`${new Set(edges.map(edge=>edge.trimer)).size} Dreierpfade · ${nodes.length} Knoten · ${edges.length} starke Kanten`));
  return svg;
}

function sourceChannelVisual(title,data) {
  const svg=createChartSVG(title), rows=data.series||[], palette=['#124f42','#4f7d6e','#8aaa9d','#a96508','#7160a5','#927fc3','#b0a3d4'];
  const drawBand=(key,width,top,bottom,label,offset)=>{
    svg.append(svgEl('text',{x:24,y:top-8,class:'chart-note'},label));
    [0,.5,1].forEach(value=>{const y=bottom-value*(bottom-top);svg.append(svgEl('line',{x1:45,y1:y,x2:535,y2:y,class:'grid-line'}));svg.append(svgEl('text',{x:38,y:y+3,'text-anchor':'end',class:'axis-label'},fmt(value,2)));});
    for(let component=0;component<width;component++){
      const points=rows.map((row,index)=>({x:55+index*(465/Math.max(rows.length-1,1)),y:bottom-(Number(row[key]?.[component])||0)*(bottom-top)}));
      svg.append(svgEl('path',{d:points.map((point,index)=>`${index?'L':'M'}${point.x},${point.y}`).join(' '),fill:'none',stroke:palette[offset+component], 'stroke-width':2.3,'stroke-dasharray':key==='readout'?'5 3':''}));
    }
  };
  drawBand('population',rows[0]?.population?.length||0,48,132,'Vier Registerpopulationen',0);
  drawBand('readout',rows[0]?.readout?.length||0,172,256,'Drei wirkliche Auslesewerte',4);
  svg.append(svgEl('text',{x:280,y:290,'text-anchor':'middle',class:'chart-note'},`${rows.length} Kanalzustände · durchgezogen: Population · gestrichelt: Auslese`));
  return svg;
}

function renderVisual(root, stage) {
  if(!root)return; root.innerHTML=""; const type=stage.visual?.type, data=stage.visual?.data||{}, title=stageName(stage); let svg;
  if(type==="anchor"){
    svg=createChartSVG("Anker (1,1,2), Potenzleiter und Invarianten"); const powers=numericArray(data.powers||[]), invariants=numericArray(data.invariants||[]);
    const points=powers.map((value,index)=>({x:68+index*78,y:245-value/Math.max(...powers,1)*150,value}));
    svg.append(svgEl("path",{d:points.map((p,i)=>`${i?'L':'M'}${p.x},${p.y}`).join(' '),class:"chart-line"})); points.forEach((p,i)=>{svg.append(svgEl("circle",{cx:p.x,cy:p.y,r:6,class:"chart-point"}));svg.append(svgEl("text",{x:p.x,y:267,"text-anchor":"middle",class:"axis-label"},`p${i+1}=${fmt(p.value)}`));});
    svg.append(svgEl("text",{x:430,y:90,class:"visual-title"},`a = (${(data.anchor||[]).join(', ')})`));svg.append(svgEl("text",{x:430,y:116,class:"chart-note"},`(e₁,e₂,e₃) = (${invariants.join(', ')})`));svg.append(svgEl("text",{x:280,y:292,"text-anchor":"middle",class:"chart-note"},"p₁p₂p₃ = 240 · p₄−p₃ = 8 · Summe 248"));
  } else if(type==="root_system"){
    svg=createChartSVG("240 E₈-Wurzeln aus vier Verklebungsklassen"); const roots=data.roots||data.sample_roots||[], sizes=data.coset_sizes||[]; const projected=roots.map((r,i)=>{const a=numericArray(r);return{x:(a[0]||0)+.62*(a[2]||0)-.37*(a[4]||0)+.21*(a[6]||0),y:(a[1]||0)-.48*(a[3]||0)+.29*(a[5]||0)-.17*(a[7]||0),i};}); const mx=Math.max(...projected.map(p=>Math.abs(p.x)),1),my=Math.max(...projected.map(p=>Math.abs(p.y)),1),palette=['#124f42','#7160a5','#a96508','#46749b']; let threshold=0,coset=0;
    svg.append(svgEl("line",{x1:35,y1:150,x2:535,y2:150,class:"grid-line"}));svg.append(svgEl("line",{x1:285,y1:38,x2:285,y2:270,class:"grid-line"}));
    projected.forEach(p=>{while(coset<sizes.length-1&&p.i>=threshold+sizes[coset]){threshold+=sizes[coset];coset++;}svg.append(svgEl("circle",{cx:285+p.x/mx*230,cy:150-p.y/my*105,r:2.25,fill:palette[coset%palette.length],opacity:.74}));});
    svg.append(svgEl("text",{x:280,y:289,"text-anchor":"middle",class:"chart-note"},`${roots.length} Wurzeln · Klassen ${sizes.join(' + ')} · lineare Projektion`));
  } else if(type==="seam"){
    svg=createChartSVG("Vier Marken, drei Zyklen und fünf Funktionen"); const cx=200,cy=155,r=90;svg.append(svgEl("circle",{cx,cy,r,fill:"none",stroke:"#124f42","stroke-width":3}));[[0,"1"],[Math.PI/2,"i"],[Math.PI,"−1"],[3*Math.PI/2,"−i"]].forEach(([a,label],i)=>{const x=cx+Math.cos(a)*r,y=cy-Math.sin(a)*r;svg.append(svgEl("circle",{cx:x,cy:y,r:10,fill:i%2?'#7160a5':'#124f42'}));svg.append(svgEl("text",{x:x+14,y:y+4,class:"visual-title"},label));});[0,1,2].forEach(i=>svg.append(svgEl("path",{d:`M${cx-r+15+i*12},${cy-20+i*20} Q${cx},${cy-95+i*15} ${cx+r-15-i*12},${cy+20-i*20}`,fill:"none",stroke:"#a96508","stroke-width":1.5,"stroke-dasharray":"4 4"})));for(let i=0;i<5;i++){svg.append(svgEl("rect",{x:360+i*31,y:118,width:21,height:75-i*8,rx:4,fill:i<3?'#124f42':'#7160a5',opacity:.8}));}svg.append(svgEl("text",{x:425,y:220,"text-anchor":"middle",class:"chart-note"},"h⁰ = 5"));svg.append(svgEl("text",{x:200,y:285,"text-anchor":"middle",class:"chart-note"},"μ₄-Marken · H₁-Rang 3"));
  } else if(type==="clock"){
    svg=createChartSVG("30er-Clock mit acht primitiven Phasen"); const cx=190,cy=155,r=102,phases=data.phases||[];for(let i=0;i<30;i++){const a=2*Math.PI*i/30-Math.PI/2,x=cx+Math.cos(a)*r,y=cy+Math.sin(a)*r;const active=phases.includes(i);svg.append(svgEl("circle",{cx:x,cy:y,r:active?6:2.5,fill:active?'#7160a5':'#b8c5be'}));}const step=(Number(data.step)||0)%30,a=2*Math.PI*step/30-Math.PI/2;svg.append(svgEl("line",{x1:cx,y1:cy,x2:cx+Math.cos(a)*(r-12),y2:cy+Math.sin(a)*(r-12),stroke:"#a96508","stroke-width":4}));svg.append(svgEl("circle",{cx:420,cy:145,r:50,fill:"none",stroke:"#124f42","stroke-width":2}));for(let i=0;i<4;i++){const q=2*Math.PI*i/4-Math.PI/2;svg.append(svgEl("circle",{cx:420+Math.cos(q)*50,cy:145+Math.sin(q)*50,r:6,fill:"#124f42"}));}svg.append(svgEl("text",{x:420,y:220,"text-anchor":"middle",class:"chart-note"},"μ₄ wirkt als Automorphismus"));
  } else if(type==="curve"){
    const curve=(data.curve||[]).map(p=>({x:Number(p.alpha),y:Number(p.F)})); svg=lineChart("α-Schließung F(α)",[{name:"F(α)",values:curve}],{x:"α"});
    if(data.root!==undefined)svg.append(svgEl("text",{x:380,y:25,class:"chart-note"},`Wurzel α⁻¹ = ${fmt(1/Number(data.root),12)}`));
  } else if(type==="trajectory"){
    const raw=data.trajectory||[], width=raw[0]?.state?.length||0, series=Array.from({length:width},(_,j)=>({name:`Eigenkomponente ${j+1}`,values:raw.map((p,i)=>({x:p.step??i,y:Number(p.state[j])}))})); svg=lineChart("Transferkonvergenz",series,{x:"Transfer-Schritt"});
  } else if(type==="timeseries"){
    svg=sourceChannelVisual("Quellenkanal: Population und beobachtbare Antworten",data);
  } else if(type==="matrix") svg=matrixVisual(title,data.R||data.matrix||stage.data?.R||[]);
  else if(type==="charges"){
    svg=createChartSVG("16 Zustände der geraden Außenalgebra"); const states=data.states||[]; states.forEach((s,i)=>{const x=42+(i%8)*62,y=72+Math.floor(i/8)*90,degree=s.degree||0,fill=degree===0?'#7160a5':degree===2?'#124f42':'#a96508';svg.append(svgEl("circle",{cx:x,cy:y,r:22,fill,opacity:.9}));svg.append(svgEl("text",{x,y:y+3,"text-anchor":"middle",fill:"white","font-size":9},s.charge?.fraction??fmt(s.charge)));svg.append(svgEl("text",{x,y:y+36,"text-anchor":"middle",class:"axis-label"},(s.bits||[]).join('')));});svg.append(svgEl("text",{x:280,y:277,"text-anchor":"middle",class:"chart-note"},"1 ⊕ 10 ⊕ 5 = 16 · Kreis: Hyperladung · darunter: Belegung"));
  } else if(type==="tree"){
    svg=createChartSVG("Dreifache Zellrekursion"); const requested=Number(data.depth)||3,depth=Math.min(requested,5);for(let d=0;d<=depth;d++){const count=Math.min(3**d,27),x=35+d*(490/Math.max(depth,1));for(let i=0;i<count;i++){const y=45+(i+.5)*220/count;svg.append(svgEl("circle",{cx:x,cy:y,r:Math.max(2,8-d),fill:d===depth?'#7160a5':'#124f42'}));if(d<depth){const next=Math.min(3**(d+1),27);for(let k=0;k<Math.min(3,next);k++)svg.append(svgEl("line",{x1:x+8,y1:y,x2:x+490/Math.max(depth,1)-8,y2:45+(Math.min(i*3+k,next-1)+.5)*220/next,stroke:"#cad4ce","stroke-width":1}));}}}svg.append(svgEl("text",{x:280,y:290,"text-anchor":"middle",class:"chart-note"},`Berechnet: Tiefe ${requested} · ${3**requested} Zellen · gezeichnet: höchstens 27 je Stufe`));
  } else if(type==="bars"){
    const points=(data.series||[]).flatMap(series=>(series.points||[]).map(point=>({label:point.x,value:point.y}))); svg=barChart(title,points,data.x_label||"Kategorie");
  } else if(type==="spectrum"){
    const values=(data.bars||[]).map(item=>({label:fmt(item.value,4),value:item.multiplicity})); svg=barChart("Spektrum des 256-dimensionalen Codeoperators",values,data.x_label||"Eigenwert");
  } else if(type==="flow"){
    svg=flowVisual(title,data);
  } else if(type==="sector_balance"){
    svg=sectorBalanceVisual(title,data);
  } else if(type==="lattice"&&data.strong_edges){
    svg=assemblyLatticeVisual(title,data);
  } else if(type==="network"||type==="bridge"||type==="lattice"){
    svg=networkVisual(title,data,type);
  } else if(type==="quartic"){
    svg=createChartSVG("Sechs Nullsummenkoordinaten auf der Quartik");const coords=data.coordinates||[];coords.forEach((v,i)=>{const a=2*Math.PI*i/Math.max(coords.length,6)-Math.PI/2,r=45+Math.min(92,Number(v.magnitude||0)*120),x=280+Math.cos(a)*r,y=150+Math.sin(a)*r;svg.append(svgEl("line",{x1:280,y1:150,x2:x,y2:y,stroke:"#cad4ce"}));svg.append(svgEl("circle",{cx:x,cy:y,r:9,fill:i%2?'#7160a5':'#124f42'}));svg.append(svgEl("text",{x:x+11,y:y+3,class:"chart-note"},`z${i+1}=${fmt(v.re,4)}`));});svg.append(svgEl("text",{x:280,y:285,"text-anchor":"middle",class:"chart-note"},`Quartischer Residual: ${fmt(data.residual)}`));
  } else if(type==="binding"){
    const spectrum=(data.spectrum||[]).map(item=>({label:fmt(item.value,3),value:item.multiplicity}));svg=barChart("Bindungsspektrum und Multiplizitäten",spectrum,"Energieeigenwert");
  } else if(type==="predictions"){
    svg=createChartSVG("16 eingefrorene Ausgaben – Status statt Größenvergleich");const rows=data.rows||[];rows.forEach((row,i)=>{const y=45+i*14.2;svg.append(svgEl("rect",{x:30,y:y-8,width:row.layer==='core'?300:180,height:9,rx:3,fill:row.layer==='core'?'#124f42':'#a96508'}));svg.append(svgEl("text",{x:340,y,class:"chart-note"},String(row.id||row.observable).slice(0,29)));});
  } else if(type==="scales"){
    svg=createChartSVG("Dimensionslose Skala und GeV-Lesart"); const logDim=Math.log10(Math.abs(Number(data.dimensionless))),logGev=Math.log10(Math.abs(Number(data.gev))); const vals=[{label:"log₁₀ dimensionslos",value:logDim},{label:"log₁₀ GeV",value:logGev}]; const y=v=>245-(v+6)/22*170; vals.forEach((v,i)=>{const x=120+i*250,py=y(v.value);svg.append(svgEl("line",{x1:x,y1:245,x2:x,y2:py,stroke:i?'#7160a5':'#124f42','stroke-width':28}));svg.append(svgEl("text",{x,y:py-12,"text-anchor":"middle",class:"visual-title"},fmt(v.value,5)));svg.append(svgEl("text",{x,y:270,"text-anchor":"middle",class:"chart-note"},v.label));});svg.append(svgEl("text",{x:280,y:292,"text-anchor":"middle",class:"chart-note"},"Die GeV-Zuordnung ist bedingt; die dimensionslose Rechnung bleibt getrennt."));
  } else if(type==="cosmology"){
    const vals=[{label:"nₛ",value:data.n_s},{label:"r",value:data.r},{label:"Aₛ × 10⁹",value:Number(data.A_s)*1e9},{label:"−log₁₀ ρΛ/ρP",value:-Math.log10(Number(data.rho_ratio))}]; svg=barChart(`Kosmologische Lesart bei N = ${fmt(data.efolds)} e-folds`,vals,"Ausgabe (verschiedene Skalen)");
  } else {
    const outputs=(stage.outputs||[]).filter(x=>typeof x.value==='number'); if(outputs.length)svg=lineChart(title,[{name:"Ausgaben",values:outputs.map((x,i)=>({x:i,y:x.value}))}],{x:"Ausgabeindex"});else svg=createChartSVG(title);
  }
  root.append(svg);
  const table=document.createElement("details"); table.innerHTML=`<summary>Daten als Text</summary><pre class="formula">${escapeHTML(JSON.stringify(stage.visual?.data||{},null,2).slice(0,16000))}</pre>`; root.append(table);
}

const TOUR_LENSES={geometry:"Geometrie",topology:"Topologie",mathematics:"Mathematik",physics:"Physik"};
const STATUS_LABELS={exact:'exakt',numeric:'numerisch',conditional:'bedingt',open:'offen',input:'gesetzt',passed:'bestanden',complete:'abgeschlossen'};

function tourStatusClass(status){return String(status||'').toLocaleLowerCase('de').replace(/[^a-zäöüß]+/g,'-');}
function statusLabel(status){const value=String(status||'offen').toLocaleLowerCase('de');return STATUS_LABELS[value]||status||'offen';}
function tourSourceLink(source){const path=source?.url||source?.path;if(!path)return '';const label=source.label||source.claim||path,title=source.label&&source.claim?` title="${escapeHTML(source.claim)}"`:'';if(path.startsWith('/')&&!/^https?:\/\//i.test(path))return `<span${title}>${escapeHTML(label)}</span>`;return `<a href="${sourceURL(source)}" target="_blank" rel="noopener noreferrer"${title}>${escapeHTML(label)} ↗</a>`;}

function tourControlsHTML(chapter) {
  if(chapter.id==='source'){
    const current=Number($('#phase-b')?.value||0);
    return `<div class="tour-live-controls"><div><strong>Offene Phase b vergleichen</strong><small>Jede Auswahl startet den vollständigen Rechenlauf.</small></div><div class="tour-choice-group" role="group" aria-label="Phase b neu berechnen">${[[0,'0'],[8,'1/18'],[32,'2/9']].map(([step,label])=>`<button type="button" class="mini-button" data-tour-phase="${step}" aria-pressed="${current===step}">b = ${label}</button>`).join('')}</div></div>`;
  }
  if(chapter.id==='recursion'){
    const depth=Number($('#recursion-depth')?.value||1),min=Number($('#recursion-depth')?.min||1),max=Number($('#recursion-depth')?.max||8);
    return `<div class="tour-live-controls"><div><strong>Rekursionstiefe wirklich ändern</strong><small>Die Zellzahlen und Moden werden vom Backend neu berechnet.</small></div><div class="tour-choice-group" role="group" aria-label="Rekursionstiefe neu berechnen"><button type="button" class="mini-button" data-tour-depth="-1" ${depth<=min?'disabled':''}>−</button><output aria-live="polite">Tiefe ${depth}</output><button type="button" class="mini-button" data-tour-depth="1" ${depth>=max?'disabled':''}>+</button></div></div>`;
  }
  return '';
}

function bindTourControls(root) {
  $$('[data-tour-phase]',root).forEach(button=>button.addEventListener('click',()=>{const step=Number(button.dataset.tourPhase);$('#phase-b').value=String(step);updateControlLabels();runPipeline(getConfig());}));
  $$('[data-tour-depth]',root).forEach(button=>button.addEventListener('click',()=>{const input=$('#recursion-depth'),next=Math.max(Number(input.min),Math.min(Number(input.max),Number(input.value)+Number(button.dataset.tourDepth)));input.value=String(next);updateControlLabels();runPipeline(getConfig());}));
}

function renderTour() {
  const tour=app.snapshot?.tour,root=$("#tour-chapter"),path=$("#tour-path");
  if(!root)return;
  if(!tour?.chapters?.length){root.innerHTML='<div class="empty-state">Die geführte Tour wird mit dem aktuellen Rechenlauf geladen.</div>';path.innerHTML='';return;}
  const chapters=tour.chapters;app.tourIndex=Math.max(0,Math.min(app.tourIndex,chapters.length-1));const chapter=chapters[app.tourIndex];
  $("#tour-view-title").textContent=tour.title||'Das ganze Konstrukt als zusammenhängender Weg';$("#tour-intro-text").textContent=tour.intro||'';
  path.innerHTML=chapters.map((item,index)=>`<button type="button" class="tour-path-step ${index<app.tourIndex?'is-done':''} ${index===app.tourIndex?'is-current':''}" data-tour-index="${index}" ${index===app.tourIndex?'aria-current="step"':''} aria-label="Kapitel ${index+1}: ${escapeHTML(item.title)}">${escapeHTML(short(item.title,25))}</button>`).join('');
  $$('[data-tour-index]',path).forEach(button=>button.addEventListener('click',()=>selectTourChapter(Number(button.dataset.tourIndex))));
  const metrics=(chapter.metrics||[]).map(metric=>`<div class="tour-metric"><strong>${escapeHTML(fmt(metric.value,8))}</strong><span>${escapeHTML(metric.label)}</span>${metric.note?`<small>${escapeHTML(metric.note)}</small>`:''}</div>`).join('');
  const sources=(chapter.sources||[]).map(tourSourceLink).filter(Boolean).join('');
  root.innerHTML=`<header class="tour-chapter-head"><div><p class="eyebrow">${escapeHTML(chapter.eyebrow||`Kapitel ${app.tourIndex+1}`)}</p><h2>${escapeHTML(chapter.title)}</h2><p class="tour-question">${escapeHTML(chapter.question||'')}</p></div><span class="tour-status ${escapeHTML(tourStatusClass(chapter.status))}">${escapeHTML(statusLabel(chapter.status))}</span></header>
    <p class="tour-lead">${escapeHTML(chapter.lead||'')}</p>
    <div class="tour-stage" id="tour-scene-${escapeHTML(chapter.id)}" aria-label="Visualisierung: ${escapeHTML(chapter.title)}"></div>
    ${tourControlsHTML(chapter)}
    ${metrics?`<div class="tour-metrics">${metrics}</div>`:''}
    <div class="tour-story"><section><b>Was hatte ich?</b><p>${escapeHTML(chapter.before||'')}</p></section><section><b>Was passiert?</b><p>${escapeHTML(chapter.action||'')}</p></section><section><b>Was kommt heraus?</b><p>${escapeHTML(chapter.after||'')}</p></section><section><b>Warum brauche ich das?</b><p>${escapeHTML(chapter.contribution||'')}</p></section></div>
    <div class="tour-lens-panel"><strong>${escapeHTML(TOUR_LENSES[app.tourLens])}</strong><p>${escapeHTML(chapter.lenses?.[app.tourLens]||'Für diesen Blickwinkel ist noch keine Erklärung hinterlegt.')}</p></div>
    <footer class="tour-foot"><section class="tour-limit"><h3>Was dieser Schritt noch nicht leistet</h3><p>${escapeHTML(chapter.limit||'Keine zusätzliche Grenze angegeben.')}</p></section><section class="tour-sources"><h3>Originalquelle &amp; Status</h3>${sources||'<span>Keine Quelle verknüpft.</span>'}</section></footer>`;
  renderTourScene($(`#tour-scene-${CSS.escape(chapter.id)}`,root),chapter);bindTourControls(root);
  $("#tour-position").textContent=`${app.tourIndex+1} / ${chapters.length}`;$("#tour-prev").disabled=app.tourIndex===0;$("#tour-next").disabled=app.tourIndex===chapters.length-1;
  path.querySelector('.is-current')?.scrollIntoView({block:'nearest',inline:'center'});renderTourConsequences(tour.implications||[],tour.candidates||[],tour.zuse_aspects||[],tour.world_process||{},tour.kernel_aspects||[],tour.kernel_summary||{});renderTourGates(tour.gates||[]);renderTourCoverage(tour.coverage||[]);
}

function selectTourChapter(index,scroll=true){const chapters=app.snapshot?.tour?.chapters||[];if(!chapters.length)return;app.tourIndex=Math.max(0,Math.min(index,chapters.length-1));renderTour();if(scroll)$("#tour-chapter")?.scrollIntoView({behavior:'smooth',block:'start'});}

function rationalNumber(value) {const text=String(value??'').trim(),match=text.match(/^(-?\d+(?:\.\d+)?)\s*\/\s*(-?\d+(?:\.\d+)?)$/);if(match)return Number(match[1])/Number(match[2]);const number=Number(text);return Number.isFinite(number)?number:null;}

function compositionEncoderScene(svg,data) {
  const path=data.quartic_to_path||{},prob=rationalNumber(path.retained_probability),rest=prob===null?null:1-prob,residuals=numericValues(path.residuals||{});
  sceneText(svg,500,48,'Derselbe Inhalt auf Encoder- und Pfadskala','scene-title','middle');sceneBox(svg,65,165,210,125,'G-Encoder',path.identity||'','scene-card');sceneArrow(svg,275,225,405,150);sceneArrow(svg,275,225,405,335);
  sceneBox(svg,420,80,250,145,`W-Pfad · ${prob===null?'–':`${fmt(prob*100)} %`}`,`Energie ${path.path_energies?.W??'–'}`,'scene-card');sceneBox(svg,420,285,250,145,`Erhaltener Rest · ${rest===null?'–':`${fmt(rest*100)} %`}`,`Energie ${path.path_energies?.R??'–'}`,'scene-card');
  sceneArrow(svg,670,150,785,225);sceneArrow(svg,670,355,785,275);sceneBox(svg,800,165,145,145,'Vollständige Zerlegung','W und Rest bleiben getrennte orthogonale Richtungen','scene-card');sceneText(svg,500,475,`Live-Residual maximal ${fmt(residuals.length?Math.max(...residuals.map(Math.abs)):0)}`,'scene-small','middle');
}

function compositionPortsScene(svg,data) {
  const pairs=data.positive_pair_class||{},opposite=pairs.opposite_edges||[],same=pairs.same_edges||[],bridge=data.bridge||{},colors={opposite:'#124f42',same:'#7160a5'};
  sceneText(svg,500,45,'Zwei Dreierblöcke werden über neun Portpaare gekoppelt','scene-title','middle');
  const yForSite=site=>160+(site%3)*95,representation=site=>site%2===0?'U':'Ū',fillFor=site=>representation(site)==='U'?'#7160a5':'#124f42';
  svg.append(svgEl('rect',{x:55,y:75,width:230,height:330,rx:24,class:'scene-card'}));svg.append(svgEl('rect',{x:715,y:75,width:230,height:330,rx:24,class:'scene-card'}));sceneText(svg,170,112,'Block A · U–Ū–U','scene-title','middle');sceneText(svg,830,112,'Block B · Ū–U–Ū','scene-title','middle');
  const links=[...opposite.map(edge=>({kind:'opposite',edge})),...same.map(edge=>({kind:'same',edge}))];links.forEach(({kind,edge})=>{const [left,right]=edge,y1=yForSite(left),y2=yForSite(right),wire=svgEl('path',{d:`M248,${y1} C405,${y1} 595,${y2} 752,${y2}`,fill:'none',stroke:colors[kind],'stroke-width':3,opacity:.76});wire.append(svgEl('title',{},`Port ${left+1} ${representation(left)} mit Port ${right+1} ${representation(right)}`));svg.append(wire);});
  [0,1,2].forEach(site=>{const cy=yForSite(site);svg.append(svgEl('circle',{cx:220,cy,r:28,fill:fillFor(site),stroke:'white','stroke-width':2}));sceneText(svg,220,cy+5,representation(site),'scene-label scene-on-dark','middle');sceneText(svg,180,cy+4,`Port ${site+1}`,'scene-small','end');});[3,4,5].forEach(site=>{const cy=yForSite(site);svg.append(svgEl('circle',{cx:780,cy,r:28,fill:fillFor(site),stroke:'white','stroke-width':2}));sceneText(svg,780,cy+5,representation(site),'scene-label scene-on-dark','middle');sceneText(svg,820,cy+4,`Port ${site+1}`,'scene-small');});
  svg.append(svgEl('circle',{cx:155,cy:418,r:6,fill:colors.opposite}));sceneText(svg,170,422,`${opposite.length} entgegengesetzte Darstellungen`,'scene-small');sceneText(svg,170,440,pairs.opposite_term||'h_opp','scene-small');svg.append(svgEl('circle',{cx:555,cy:418,r:6,fill:colors.same}));sceneText(svg,570,422,`${same.length} gleiche Darstellungen`,'scene-small');sceneText(svg,570,440,pairs.same_term||'h_same','scene-small');
  svg.append(svgEl('rect',{x:300,y:452,width:400,height:70,rx:12,class:'scene-card'}));sceneText(svg,500,479,bridge.projected_identity||'','scene-label','middle');sceneText(svg,500,505,`gleiche logische Bindung + Konstante ${bridge.constant_per_bridge??'–'}`,'scene-small','middle');
}

function compositionSpaceScene(svg,data,levels) {
  const coarse=data.coarse_a3||{},blocks=coarse.blocks||[],edges=coarse.edges||[],placed=new Map(),palette={same:'#7160a5',opposite:'#124f42'};
  sceneText(svg,380,45,'Raumgraph','scene-title','middle');sceneText(svg,860,45,'Levelrichtung','scene-title','middle');
  blocks.forEach((block,index)=>{const x=75+index*67,y=220+(index%2?38:-38);placed.set(block.id,{x,y,block});});edges.forEach(edge=>{const a=placed.get(edge.source),b=placed.get(edge.target);if(!a||!b)return;svg.append(svgEl('path',{d:`M${a.x},${a.y} Q${(a.x+b.x)/2},${Math.min(a.y,b.y)-24} ${b.x},${b.y}`,fill:'none',stroke:palette[edge.orientation]||'#aebdb6','stroke-width':1.7,opacity:.65}));});placed.forEach(({x,y,block})=>{svg.append(svgEl('circle',{cx:x,cy:y,r:15,fill:block.representation==='U'?'#7160a5':'#124f42',stroke:'white','stroke-width':2}));sceneText(svg,x,y+4,block.id,'scene-small scene-on-dark','middle');});
  svg.append(svgEl('path',{d:'M65 330 L710 330',class:'scene-flow'}));sceneText(svg,390,360,`${blocks.length} Blöcke · ${edges.length} Kanten · horizontale Nachbarschaft`,'scene-label','middle');sceneText(svg,390,390,`gleiche Darstellung ${coarse.orientation_counts?.same??'–'} · entgegengesetzte Darstellung ${coarse.orientation_counts?.opposite??'–'}`,'scene-small','middle');
  svg.append(svgEl('path',{d:'M860 440 L860 90',class:'scene-flow'}));(levels||[]).forEach((level,index)=>{const y=415-index*(290/Math.max((levels||[]).length-1,1));svg.append(svgEl('circle',{cx:860,cy:y,r:19,fill:index===(levels||[]).length-1?'#7160a5':'#124f42'}));sceneText(svg,860,y+4,fmt(level.cells),'scene-small scene-on-dark','middle');sceneText(svg,895,y+4,`Tiefe ${level.depth}`,'scene-small');});sceneText(svg,500,495,'Raumgraph schematisch · Rekursionslevel ist keine Raumrichtung.','scene-title','middle');
}

function renderCompositionScene(root,data) {
  if(!root||!data)return;root.innerHTML='';const svg=makeTourSVG({title:'Derselbe Inhalt auf mehreren Skalen'}),levels=app.snapshot?.stages?.find(stage=>stage.id==='recursion')?.visual?.data?.levels||[];
  if(app.compositionView==='ports')compositionPortsScene(svg,data);else if(app.compositionView==='space')compositionSpaceScene(svg,data,levels);else compositionEncoderScene(svg,data);root.append(svg);
}

function readableValue(value) {if(Array.isArray(value))return value.map(readableValue).join(' · ');if(value&&typeof value==='object')return Object.entries(value).map(([key,item])=>`${key}: ${readableValue(item)}`).join(' · ');return String(value??'');}

function renderMarkerSelection(root,data) {
  if(!root||!data?.matching_rows?.length)return;
  const rows=data.matching_rows,minima=new Set(data.disturbance?.minimizers||[]),selected=rows[app.markerIndex]||rows[0];
  root.innerHTML=`<p class="eyebrow">Ladung → mögliche Raummarkierung</p><h4>15 Paarungen. Drei gleich gute Vertreter. Eine Familienklasse.</h4><p>Die sechs Punkte lassen sich auf 15 Arten zu drei Paaren verbinden. Violett ist der bereits gesetzte Quellmarker 5. Grün sind genau die Paarungen, die die native Ladung am wenigsten verändern. Klicke auf eine Paarung, um ihren berechneten Wert zu sehen.</p><div class="marker-grid">${rows.map((row,i)=>`<button type="button" data-marker-index="${i}" class="marker-option ${minima.has(row.matching)?'marker-minimum':''}" aria-pressed="${selected===row}" aria-label="Paarung ${escapeHTML(row.matching)}${minima.has(row.matching)?', minimale Störung':''}"><span class="marker-drawing"></span><strong>${escapeHTML(row.matching)}</strong><small>${minima.has(row.matching)?'Minimum · gleiche Familie':'Größere Ladungsstörung'}</small></button>`).join('')}</div><p class="marker-result" aria-live="polite"><strong>${escapeHTML(selected.matching)}</strong> · Ladungsstörung ${fmt(selected.disturbance_numeric)} · exakt ${escapeHTML(selected.disturbance_exact)}. ${minima.has(selected.matching)?'Dieser Vertreter gehört zur ausgezeichneten Dreierfamilie.':'Dieser Kandidat stört die Ladung stärker als die drei grünen Vertreter.'}</p><small>Exakter Vergleich unter der zusätzlichen Regel „minimale Ladungsstörung“. Die Regel selbst muss aus der Quelle folgen. Punkte und Linien zeigen die Paarung; ihre Positionen sind keine physikalischen Abstände.</small>`;
  $$('.marker-option',root).forEach((button,index)=>{const svg=svgEl('svg',{viewBox:'0 0 120 100','aria-hidden':'true'}),points=Array.from({length:6},(_,i)=>[60+34*Math.cos(i*Math.PI/3-Math.PI/2),50+34*Math.sin(i*Math.PI/3-Math.PI/2)]);rows[index].pairs.forEach(([a,b])=>svg.append(svgEl('line',{x1:points[a][0],y1:points[a][1],x2:points[b][0],y2:points[b][1],stroke:minima.has(rows[index].matching)?'#124f42':'#95a59c','stroke-width':2})));points.forEach(([x,y],i)=>{svg.append(svgEl('circle',{cx:x,cy:y,r:10,fill:i===data.overlaps?.raw_marked_label?'#7160a5':'#124f42'}));sceneText(svg,x,y+3,String(i),'scene-small scene-on-dark','middle');});$('.marker-drawing',button).append(svg);button.addEventListener('click',()=>{app.markerIndex=index;renderMarkerSelection(root,data);});});
}

function renderHistoryKernel(root,calculations) {
  const history=calculations?.history_kernel,matrix=history?.depth1?.kernel;
  if(!root||!Array.isArray(matrix))return;
  const active=app.historyPhase,second=history.depth2||{},largest=Math.max(...matrix.flat().map(Math.abs));
  root.innerHTML=`<div class="history-heading"><div><p class="eyebrow">Interferenz wirklich mitführen</p><h4>Geschichten können sich verstärken oder auslöschen</h4><p>Jedes Quadrat vergleicht zwei Ereignisgeschichten. Die Diagonale zeigt ihre Einzelgewichte; die übrigen Felder halten ihre kohärente Verbindung fest.</p></div><div class="composition-switch" role="group" aria-label="Zusätzliche Phase einer Geschichte"><button type="button" data-history-phase="off" aria-pressed="${!active}">Ohne Zusatzphase</button><button type="button" data-history-phase="on" aria-pressed="${active}">π an Geschichte 1</button></div></div><div class="history-content"><div class="history-matrix"></div><div class="history-explanation"><strong>${matrix.length} Ereignisse → ${second.histories??'–'} Zweierfolgen</strong><p>Der berechnete Geschichtskern der Zweierfolgen hat Rang ${second.rank??'–'}: Er spannt den vollständigen 25-dimensionalen logischen Operatorraum auf.</p><p class="history-phase-response" aria-live="polite">${active?'Die erste Zeile und Spalte wechseln außerhalb der Diagonale ihr Vorzeichen. Alle Einzelgewichte bleiben gleich. Eine spätere kohärente Zusammenführung kann bei fester physischer Phasenreferenz anders reagieren.':'Alle Phasen sind wie im berechneten Ereignisinstrument. Der Umschalter gibt nur der ersten Geschichte zusätzlich die Phase π.'}</p><p>Ein gemeinsamer Energieoffset ist bei einer festen Geschichte unsichtbar. Unterschiedliche Aufenthaltsdauern machen ihn zwischen Geschichten zu einer relativen Phase. Darum muss die vollständige Rekursion auch diese Phase speichern. Beim bloßen Vergessen des Ereignisspeichers ist sie unsichtbar.</p><small>Gezeigt: reeller 15×15-Kern für ρ=I₅/5. Die zusätzliche Phase ist eine deklarierte Demonstration, keine hergeleitete physische Zeitwahl. Der vollständige 225×225-Kern steht beim Quellenkanal.</small></div></div>`;
  const svg=svgEl('svg',{viewBox:'0 0 380 410',role:'img','aria-label':'Berechnete Interferenzmatrix von 15 Ereignisgeschichten'});
  svg.append(svgEl('title',{},'Reeller Geschichtskern; Grün positiv, Violett negativ'));
  matrix.forEach((row,a)=>row.forEach((raw,b)=>{const value=raw*(active&&((a===0)!==(b===0))?-1:1),cell=svgEl('rect',{x:45+b*20,y:38+a*20,width:19,height:19,rx:2,fill:value<0?'#7160a5':'#124f42',opacity:.14+.86*Math.abs(value)/largest});cell.append(svgEl('title',{},`Geschichten ${a+1} und ${b+1}: ${fmt(value)}`));svg.append(cell);}));
  matrix.forEach((_,i)=>{sceneText(svg,55+i*20,26,String(i+1),'scene-small','middle');sceneText(svg,32,52+i*20,String(i+1),'scene-small','end');});
  sceneText(svg,195,368,'Grün: positiv · Violett: negativ','scene-small','middle');sceneText(svg,195,392,'Einzelgewichte auf der Diagonale: je 1/15','scene-small','middle');
  $('.history-matrix',root).append(svg);
  $$('[data-history-phase]',root).forEach(button=>button.addEventListener('click',()=>{app.historyPhase=button.dataset.historyPhase==='on';renderHistoryKernel(root,calculations);}));
}

function originNumber(value, digits=13) {
  const number=Number(value);
  const scientific=number!==0&&Math.abs(number)<1e-8;
  return Number.isFinite(number)?new Intl.NumberFormat('de-DE',{maximumSignificantDigits:scientific?5:digits,notation:scientific?'scientific':'standard'}).format(number):String(value??'–');
}

function jointSourceMarkup(cartan,quartic,process) {
  const deck=cartan?.glue_deck_character,words=deck?.short_closed_word_witness?.equal_naked_words;
  const carry=words?`<section class="joint-carry"><h5>Zuses Gedächtnisfrage bekommt einen konkreten Ort</h5><div class="joint-history-paths">${words.map((word,index)=>`<div><span>Folge ${index+1}</span><code>${word.map(value=>`r${value}`).join(' → ')}</code><b>gleiche Cartanwirkung</b><strong>${index?'mit':'ohne'} relativen Deckcharakter</strong></div>`).join('')}</div><p>Im reduzierten Bild treffen sich beide Wege. In der gewählten geladenen Liftstruktur unterscheiden sie sich exakt: +1 auf ${escapeHTML(deck.glue_even_root_count)} geraden Wurzelfeldern, −1 auf ${escapeHTML(deck.glue_odd_spinor_root_count)} Spinorwurzeln. Bei kohärentem Vergleich der Wege darf diese Phase nicht verloren gehen.</p><p>Der vollständige Charakterkern besitzt ${escapeHTML(deck.full_lift_kernel_order)} Möglichkeiten, gespeichert in ${escapeHTML(deck.full_lift_kernel_rank)} binären Phasenmarken. Der markierte Deckcharakter hat ${escapeHTML(deck.deck_character_G31_orbit_size)} konjugierte Lagen und muss mit der Markierung transportiert werden.</p><small>Exakt in der angegebenen E₈-Gitter-VOA-Realisierung und Liftkonvention. Ein einzelnes globales Vorzeichen eines Zustands ist für sich kein Messergebnis. Die P1-Quelle muss die konkrete Markierung und die erlaubten Vergleichsoperationen festlegen.</small>${process?'<p class="joint-process-ready">Die Fortschreibung dieses Phasenspeichers wird mit denselben Ereignismatrizen ausgeführt und nach Speichern/Laden erneut geprüft.</p>':''}</section>`:'';
  const coefficients=quartic?.molien?.nonzero_coefficients;
  const selection=coefficients?`<section class="joint-quartic"><h5>Warum gerade der Quartikcode?</h5><div>${Object.entries(coefficients).map(([degree,dimension])=>`<article><span>Grad ${escapeHTML(degree)}</span><b>${escapeHTML(dimension)}</b><small>${degree==='0'?'Konstante':degree==='4'?'erste nichtkonstante Koordinaten':'zusammengesetzte Invarianten'}</small></article>`).join('')}</div><p>Fordert man den kleinsten nichtkonstanten Pauli-invarianten Readout, bleiben genau die fünf Quartikkoordinaten. Diese Folgerung ist exakt. Dass P1/P2 gerade diesen Readout verlangen, ist noch kein bewiesener Auswahlsatz.</p></section>`:'';
  const trajectories=process?.path_comparison?.trajectories,step=Math.min(3,Math.max(0,app.sourceReplayStep));
  const replay=trajectories?`<section class="source-replay"><h5>Schritt für Schritt: Gleiche Ankunft, andere geladene Wirkung</h5><p>Zwei Folgen laufen durch dieselben ursprünglichen Spiegelungen. Der Fünfercode allein kann ihre gesamte geladene Wirkung nicht festhalten.</p><div class="composition-switch" role="group" aria-label="Geladene Ereignisfolgen abspielen">${[0,1,2,3].map(index=>`<button type="button" data-source-step="${index}" aria-pressed="${step===index}">${index===0?'Start':`Schritt ${index}`}</button>`).join('')}</div><div class="source-replay-paths" aria-live="polite">${trajectories.map((states,index)=>{const state=states[step],effect=state.root_effect;return `<article><b>Folge ${index+1} · ${step===0?'Identität':`Ereignis r${state.event_label}`}</b><div class="carry-bits" aria-label="Acht Phasenmarken: ${state.carry_bits}">${[...state.carry_bits].map(bit=>`<span class="${bit==='1'?'is-set':''}">${bit}</span>`).join('')}</div><span>Zielwurzel</span><code>(${effect.target_root.map(escapeHTML).join(', ')})</code><strong>Vorzeichen des geladenen Feldes: ${effect.sign===1?'+1':'−1'}</strong></article>`;}).join('')}</div><p>${step===3?'<b>Gleiche Zielwurzel, entgegengesetztes Vorzeichen.</b> Der Unterschied steckt im gespeicherten Charakter. Wer nur das reduzierte Endbild behält, verliert eine später vergleichbare Phase.':'Die Bits zeigen den berechneten Charakteranteil. Das Feldvorzeichen hängt zusätzlich von der aktuellen Gitterwirkung ab; es ist keine Abzählung gesetzter Bits.'}</p><small>Das ist eine exakte Fortschreibung bei vorgegebenen Ereignissen. Welche Ereignisse die physische Quelle auswählt, wird dadurch nicht festgelegt. Speichern, Laden und Fortsetzen ergeben dieselbe Wirkung wie der ununterbrochene Ablauf.</small></section>`:'';
  return carry+replay+selection;
}

function chargeSelectionMarkup(data) {
  const events=data?.event_commutators;
  if(!events)return '';
  return `<section class="joint-charge"><h5>Die feste P2-Ladung sortiert die Ereignisse</h5><p>Grün: Die Ladung bleibt im Fünfer erhalten. Gelb: Ein vollständiger physischer Vorgang muss den Ladungswechsel an einen anderen geladenen Teil weitergeben.</p><div class="charge-event-grid" aria-label="15 Ereignisse und ihre feste P2-Ladung">${events.rows.map(row=>`<article class="${row.commutes_with_native_Y?'charge-preserved':'charge-exchange'}"><b>${escapeHTML(row.label)}</b><span>${row.commutes_with_native_Y?'erhält Y':'braucht Austausch'}</span><small>Störung: ${row.commutes_with_native_Y?'0':originNumber(row.commutator_hs_norm,4)}</small></article>`).join('')}</div><p><b>${events.commuting_count} von 15</b> erhalten Y bereits für sich. Sie erzeugen die endliche Gruppe S₂ × S₃ mit zwölf Elementen. Das ist die ausgewählte Untergruppe des nativen Ereignisalphabetes; die volle kontinuierliche Eichgruppe ist ein anderes Objekt.</p><p>Ein Speicher mit nur dem Ereignislabel kann die fehlende Gegenladung nicht tragen. Die acht Vorzeichenmarken speichern Phasen; sie liefern keine Gegenladung. Im vorhandenen Quartik-Quellenoperator ist der A₃-Begleiter gegenüber dieser Ladung neutral.</p><div class="charge-positive"><b>Der positive Anschluss ist schon vorhanden:</b> Die SU(5)-vervollständigte Paarbindung auf Fünfer und Gegenfünfer erhält ihre gemeinsame Ladung. Auf einem festgelegten Netz liefert sie eine ausführbare Inhaltsentwicklung. Unter voller nativer kollektiver Symmetrie und fester P2-Ladung ist die Form dieser Bindung bereits erzwungen. Warum diese volle Symmetrie für das physische Paargesetz gilt, wie das Quelleninstrument anschließt und welches Netz entsteht, muss derselbe Ursprung festlegen.</div><small>Die Rechnung verwendet den tatsächlichen P2-Polartransport in die Ereignisbasis. Ein gemeinsam bewegter Ladungsrahmen wäre kovariant, ist aber keine Erhaltung derselben festgehaltenen P2-Ladung. Ihre physische Hyperladungsdeutung benötigt den angegebenen Quellenanschluss.</small></section>`;
}

function renderCurrentBlockGeometry(root,data) {
  if(!root||!data?.position_samples?.length)return;
  const samples=data.position_samples,index=Math.min(samples.length-1,Math.max(0,app.currentGeometryIndex)),sample=samples[index],midpoint=Math.abs(sample.s)<1e-12,chain=data.global_four_chain||{};
  root.innerHTML=`<p class="eyebrow">Neuer Zusammenhang · Originalnaht und Originalströme</p><h5>Die vier Nahtmarken liefern genau die vorhandene Dreierform</h5><p>Die ursprünglichen Punkte 1, i, −1, −i werden auf −1, 0, 1 und ∞ abgebildet. Setzt man dort die geprüften E₈-Ströme und ihre Gegenstücke ein, entsteht nach Normierung exakt der bereits berechnete W-Encoder.</p><div class="current-geometry-picture"></div><label class="current-geometry-slider"><span>Gegenprobe: den mittleren Einfügepunkt verschieben <output>${originNumber(sample.s,3)}</output></span><input type="range" min="0" max="${samples.length-1}" step="1" value="${index}" aria-label="Mittleren Einfügepunkt der Stromkorrelation verschieben"></label><button type="button" class="mini-button" data-native-marks>Ursprüngliche Nahtmarken</button><div class="current-geometry-answer" aria-live="polite"><div class="current-geometry-weights"><span><b>${originNumber(sample.W_probability*100,5)} %</b> W-Anteil</span><span><b>${originNumber(sample.Z_probability*100,5)} %</b> ungerader Z-Anteil</span><span><b>${escapeHTML(sample.ratio)}</b> Verhältnis der beiden Pfade</span></div><p>${midpoint?'<b>Die ursprüngliche Markierung wählt W.</b> Beide Pfade haben dasselbe Gewicht. Dafür wurde kein neuer Mittelpunktparameter angepasst.':'Diese Verschiebung verändert die ursprüngliche markierte Geometrie. Die beiden Pfade sind nun verschieden gewichtet; zusätzlich wird der ungerade Z-Anteil sichtbar.'}</p></div><p class="current-geometry-premise"><b>Der noch nötige Anschluss:</b> Die Operatoren der P1-Naht müssen genau mit diesen geladenen E₈-Strömen und ihrer Spiegelung identifiziert werden. Die geometrische Gleichheit liefert diese Feldzuordnung nicht von selbst. Gezeigt werden Anteile einer normierten Antwort, keine hergeleiteten Ereigniswahrscheinlichkeiten.</p><details class="current-global-probe"><summary>Der nächste größere Verbund wird ebenfalls geprüft</summary><p>Für vier Zellen bei ${escapeHTML((chain.positions||[]).join(', '))} ist der ursprüngliche Stromkorrelator <b>kein Eigenzustand</b> der vorhandenen Summe der drei Nachbarbindungen: Seine Energievarianz beträgt exakt <b>${escapeHTML(chain.variance)}</b>, also mehr als null.</p><p>Die identische Dreierform begründet deshalb noch kein identisches Gesetz für den ganzen Verbund. Quellenkorrelation, Ereignisregel und gemeinsame Zeit müssen auch dort zusammenpassen. Ein nachträglich passender Hamiltonoperator würde diese Herleitung nicht ersetzen.</p></details>${tourSourceLink({path:'tfpt_explorer/current_block_geometry.py',line:1,claim:'Originale Ward-Rechnung, Markengeometrie und Verbundprüfung'})}`;
  const svg=svgEl('svg',{viewBox:'0 0 1000 285',role:'img','aria-label':'Vier ursprüngliche Nahtmarken werden auf drei endliche Einfügepunkte und einen Punkt im Unendlichen abgebildet; zwei Pfade tragen die Dreierkodierung'});
  svg.append(svgEl('circle',{cx:135,cy:127,r:67,fill:'none',stroke:'#b8c6bc','stroke-width':2}));
  const marks=[{x:202,y:127,label:'1',type:'X'},{x:135,y:60,label:'i',type:'X†'},{x:68,y:127,label:'−1',type:'X'},{x:135,y:194,label:'−i',type:'X†'}];
  marks.forEach(mark=>{svg.append(svgEl('circle',{cx:mark.x,cy:mark.y,r:21,fill:mark.type==='X'?'#124f42':'#7160a5'}));sceneText(svg,mark.x,mark.y+5,mark.label,'scene-label scene-on-dark','middle');});sceneText(svg,135,244,'Dieselbe geordnete μ₄-Naht','scene-small','middle');
  sceneArrow(svg,250,127,335,127);sceneText(svg,291,99,'Möbius','scene-small','middle');
  const left=410,right=860,middle=635+sample.s*225;
  svg.append(svgEl('line',{x1:left,y1:151,x2:right,y2:151,stroke:'#b8c6bc','stroke-width':2}));
  svg.append(svgEl('path',{d:`M${left} 151 Q${(left+middle)/2} 20 ${middle} 151`,fill:'none',stroke:'#124f42','stroke-width':4}));
  svg.append(svgEl('path',{d:`M${middle} 151 Q${(middle+right)/2} 20 ${right} 151`,fill:'none',stroke:'#7160a5','stroke-width':4}));
  [{x:left,label:'−1',field:'X'},{x:middle,label:originNumber(sample.s,3),field:'X†'},{x:right,label:'1',field:'X'}].forEach((point,i)=>{svg.append(svgEl('circle',{cx:point.x,cy:151,r:20,fill:i===1?'#7160a5':'#124f42'}));sceneText(svg,point.x,157,point.field,'scene-label scene-on-dark','middle');sceneText(svg,point.x,195,point.label,'scene-label','middle');});
  sceneText(svg,937,145,'X†','scene-label','middle');sceneText(svg,937,177,'∞','scene-label','middle');sceneText(svg,645,244,midpoint?'gleiche Pfadgewichte → exakt W':'verschiedene Pfadgewichte → W und Z','scene-label','middle');
  $('.current-geometry-picture',root).append(svg);
  if(data.RP_pair_kernel){const readings=document.createElement('div');readings.className='current-two-readings';readings.innerHTML=`<article><span>Originale Nahtantwort · drei Eingänge, ein Ausgang</span><b>Dreierkodierung W</b><p>Nach Normierung exakt der vorhandene Encoder.</p></article><article><span>Originale Nahtantwort · zwei Eingänge, zwei Ausgänge</span><b>Paarantwort K = 2I + 10P<sub>Ω</sub></b><p>Der normierte Unterschied I − K/12 ist exakt h<sub>cov</sub>.</p></article><details><summary>Trägt dieselbe Kostenregel beide Orientierungen?</summary><p>Für Fünfer und Gegenfünfer liefert sie genau die vorhandene Paarstärke. Für zwei gleich orientierte Fünfer liefert dieselbe Normierungsregel jedoch <b>2 h<sub>same</sub></b>. Beide Bindungsformen sind angebunden; ihre gemeinsame physische Stärke ist so noch nicht hergeleitet.</p><p>Eine positive Antwortmatrix ist außerdem noch kein Zeittransfer. I − B und −log B erfüllen unterschiedliche Aufgaben; ihre physische Rolle muss aus dem Quellenprozess folgen.</p></details>`;$('.current-geometry-answer',root).after(readings);}
  $('input',root).addEventListener('input',event=>{app.currentGeometryIndex=Number(event.target.value);const updated=document.createElement('div');renderCurrentBlockGeometry(updated,data);$('output',root).textContent=$('output',updated).textContent;$('.current-geometry-picture',root).replaceWith($('.current-geometry-picture',updated));$('.current-geometry-answer',root).replaceWith($('.current-geometry-answer',updated));});
  $('[data-native-marks]',root).addEventListener('click',()=>{app.currentGeometryIndex=samples.findIndex(row=>Math.abs(row.s)<1e-12);renderCurrentBlockGeometry(root,data);$('[data-native-marks]',root).focus({preventScroll:true});});
  if(data.raw_source_route){const route=data.raw_source_route,panel=document.createElement('details');panel.className='source-lift-separation';panel.innerHTML=`<summary>${escapeHTML(route.title)}</summary>${['selected_target','exact_boundary_test','positive_constraint','remaining_identity'].map(key=>`<p>${escapeHTML(route[key])}</p>`).join('')}<div>${(route.sources||[]).map(tourSourceLink).join('')}</div>`;$('.current-geometry-premise',root)?.after(panel);}
}

function renderCurrentCluster(root,data) {
  const samples=data?.visualization_samples;
  if(!root||!samples?.length)return;
  const index=Math.min(samples.length-1,Math.max(0,app.currentClusterIndex)),sample=samples[index],w=sample.weights,limit=sample.t===0;
  const sectors=[['WW','Beide Gruppen behalten W','#124f42'],['WZ','Links W · rechts Z','#7160a5'],['ZW','Links Z · rechts W','#9180bd'],['ZZ','Beide Gruppen tragen Z','#b79fce'],['C45','Antisymmetrischer Rest · 45','#be792a'],['R70','Symmetrischer Rest · 70','#c44f47']];
  root.innerHTML=`<p class="eyebrow">Dieselbe Quelle · zwei Dreiergruppen verbinden</p><h6>Was muss die größere Zelle behalten?</h6><p>Jetzt werden sechs Originalströme berechnet. Jede Dreiergruppe rückt zusammen; ihr Abstand zur anderen Gruppe bleibt groß. Im Grenzfall entsteht exakt das vorhandene Paar aus W-Blöcken. Bei endlicher Ausdehnung zeigt dieselbe Rechnung, welche weiteren Anteile mitgeführt werden müssen.</p><div class="current-cluster-picture"></div><label class="current-geometry-slider"><span>Größe der Gruppe relativ zum Abstand <output>${limit?'Grenzfall 0':escapeHTML(sample.t_exact)}</output></span><input type="range" min="0" max="${samples.length-1}" step="1" value="${index}" aria-label="Ausdehnung der beiden Dreiergruppen"></label><div class="current-cluster-result" aria-live="polite"><div class="current-cluster-total"><span><b>${originNumber((1-sample.leakage)*100,5)} %</b> erhaltene W-Blockform</span><span><b>${originNumber(sample.leakage*100,5)} %</b> zusätzlich mitzuführender Anteil</span></div><div class="current-cluster-sectors">${sectors.map(([key,label,color])=>`<div><span>${label}</span><span class="current-sector-track"><i style="width:${100*w[key]}%;background:${color}"></i></span><b>${w[key]===0?'0':w[key]<0.000001?Number(100*w[key]).toExponential(3):originNumber(w[key]*100,6)} %</b></div>`).join('')}</div><p>${limit?'<b>Exakter Grenzfall:</b> Die normierte Sechsstromantwort wird zu (W ⊗ W̄) Ω. Das ist ein Grenzwert; sechs zusammenfallende Einsetzungen werden nicht als regulärer Korrelator ausgewertet.':'<b>Keiner dieser Reste ist frei hinzugefügt.</b> Die Quelle erzeugt sie. Z erscheint am stärksten; auch die 45er- und 70er-Sektoren sind bei jedem endlichen Verhältnis zwischen 0 und 1 strikt beteiligt.'}</p></div><p class="current-geometry-premise">Diese zwei Gruppen sind eine ausdrücklich gewählte Prüfung der Zusammensetzung. Die vier P1-Marken wählen ihre Anordnung und ihren Abstand bislang nicht aus. Die Prozentwerte sind quadrierte Normanteile des berechneten Zustands; 45 und 70 zählen interne Richtungen, keine Teilchensorten.</p><details><summary>Warum das die Gesamtlösung einschränkt</summary><p>Eine exakte endliche Vergröberung darf nicht bei W stehen bleiben. Für diese Quelle benötigt jede Dreiergruppe beide Fünferformen und die 45er- und 70er-Sektoren: insgesamt 125 interne Richtungen. Das schließt diesen festen Sechs-Einsetzungs-Test; fortgesetzte Stromerzeugungen besitzen zusätzlich höhere Anregungsgrade.</p><p>Die vorhandene Neun-Port-Identität wirkt exakt auf dem erhaltenen Anteil: H₉ VΩ = 4 VΩ. Das gesamte Bewegungsgesetz muss außerdem die übrigen Anteile fortschreiben und seine Zeit aus derselben Nahtquelle erhalten. Einfaches Löschen des Rests wäre eine neue physische Annahme.</p><p>Exakt für kleine t = ε/L: zusätzlicher Normanteil = t²/3 + 109t⁴/288 + … . Die sechs Kopplungskanäle werden aus den ursprünglichen Ward-Gleichungen und den vorhandenen lokalen Projektoren berechnet.</p></details>`;
  const svg=svgEl('svg',{viewBox:'0 0 1000 260',role:'img','aria-label':`Zwei Gruppen aus je drei Strömen, relative Ausdehnung ${sample.t_exact}. ${originNumber(sample.leakage*100,5)} Prozent liegen außerhalb der beiden W-Blöcke.`});
  [{center:260,labels:['X','X†','X']},{center:740,labels:['X†','X','X†']}].forEach(group=>{
    const radius=sample.t*220;
    svg.append(svgEl('ellipse',{cx:group.center,cy:90,rx:Math.max(43,radius+38),ry:49,fill:'#edf5f0',stroke:'#97b6a5','stroke-dasharray':'5 5'}));
    if(limit){svg.append(svgEl('circle',{cx:group.center,cy:90,r:20,fill:'#124f42'}));sceneText(svg,group.center,96,'3','scene-label scene-on-dark','middle');}
    else group.labels.forEach((label,i)=>{const x=group.center+(i-1)*radius;svg.append(svgEl('circle',{cx:x,cy:90,r:18,fill:label==='X'?'#124f42':'#7160a5'}));sceneText(svg,x,96,label,'scene-small scene-on-dark','middle');});
    sceneArrow(svg,group.center,148,group.center,190);
    svg.append(svgEl('rect',{x:group.center-70,y:196,width:140,height:40,rx:10,fill:'#124f42'}));sceneText(svg,group.center,222,group.center<500?'W-Block':'W̄-Block','scene-label scene-on-dark','middle');
  });
  svg.append(svgEl('line',{x1:336,y1:216,x2:664,y2:216,stroke:'#124f42','stroke-width':3}));
  sceneText(svg,500,45,limit?'Beide Gruppen im Koaleszenzgrenzwert':'Sechs Einsetzungen in derselben Quelle','scene-label','middle');
  sceneText(svg,500,200,'neutrale Verbindung Ω','scene-small','middle');
  $('.current-cluster-picture',root).append(svg);
  const grading=data.affine_carry_grading;
  if(grading?.minimal_graded_SU5_embedding){const graded=document.createElement('details');graded.className='current-graded-source';graded.innerHTML=`<summary>Wo kommen die zusätzlichen Formen in der Quelle vor?</summary><p><b>Sie sind als echte Anregungen derselben E₈-Quelle vorhanden.</b> Der erste Stromschritt besitzt für den 70er-Sektor Norm null. Beim zweiten Stromschritt erhält dieser Sektor eine strikt positive Norm. Die exakte Rechnung verwendet dieselben ursprünglichen Stromoperatoren.</p><div class="source-grade-flow"><article><span>Quellengrad 1</span><b>5</b><small>ursprünglicher geladener Strom</small></article><i>→</i><article><span>Quellengrad 2</span><b>5 + 45</b><small>erste zusätzliche Stromanregung</small></article><i>→</i><article class="source-grade-new"><span>Quellengrad 3</span><b>70 möglich</b><small>zweite zusätzliche Stromanregung</small></article></div><table><thead><tr><th>Benötigte Form</th><th>Quellengrad</th><th>Normfaktor</th></tr></thead><tbody>${grading.minimal_graded_SU5_embedding.map(row=>`<tr><td>${escapeHTML(({W_5:'W · Fünfer',Z_5:'Z · zweiter Fünfer',C45:'Antisymmetrischer 45er',R70:'Symmetrischer 70er'})[row.trimer_sector]||row.trimer_sector)}</td><td>${row.total_E8_grade}</td><td>${escapeHTML(row.norm_eigenvalue)}</td></tr>`).join('')}</tbody></table><p>Dies belegt einen nach Graden geordneten SU(5)-Träger. Die genaue Zuordnung der vollständigen Sechsstromantwort zu diesen Anregungen ist damit noch nicht konstruiert. Der Quellengrad ist hier keine bereits identifizierte physische Zeit. Die Familienrichtung wird mitgeführt, sobald die volle Ereigniswirkung betrachtet wird.</p>`;root.append(graded);}
  $('input',root).addEventListener('input',event=>{app.currentClusterIndex=Number(event.target.value);const updated=document.createElement('div');renderCurrentCluster(updated,data);$('output',root).textContent=$('output',updated).textContent;$('.current-cluster-picture',root).replaceWith($('.current-cluster-picture',updated));$('.current-cluster-result',root).replaceWith($('.current-cluster-result',updated));});
}

function currentSourceBridgeMarkup(data) {
  if(!data?.bridge)return '';
  const views={pair:'Ein Paar',ope:'Nächste Quellenanregung',time:'Drei Zellen zusammensetzen'},active=app.currentBridgeView,ope=data.ope_boundary?.normalized_Cartan_H,time=data.common_time_boundary;
  const content=active==='ope'?`<div class="source-grade-flow"><article><span>Ausgangsraum</span><b>Vakuum + 24 Ströme</b><small>Grade 0 und 1</small></article><i>→</i><article class="source-grade-new"><span>Noch einmal derselbe Strom</span><b>Grad ${escapeHTML(ope?.grade)}</b><small>Normquadrat ${escapeHTML(ope?.square_norm)} · außerhalb des Ausgangsraums</small></article></div><p>Schon dieser vorhandene Eingriff benötigt zusätzliche Zustände. Wiederholte Cartan-Anregungen besitzen Normquadrat n! und bleiben für jedes n ungleich null. Der vollständige Quellenraum wächst unbegrenzt; seine Erzeugungsregel ist trotzdem endlich beschreibbar.</p><small>Das ist eine Folgerung aus der affinen Stromrelation. Ein fester 25er-Raum beschreibt diese ganze Quelle nicht.</small>`:active==='time'?`<div class="source-grade-flow"><article><span>Wenn Paarenergie als L₀-Zeit identifiziert wird</span><b>H<sub>Quelle</sub> = (5/6) L₀</b><small>Vakuum: 0 · erster Strom: 5/6</small></article><i>?</i><article class="source-grade-new"><span>Der Originaltrimer verlangt</span><b>Gradabstände ${escapeHTML(time?.required_untwisted_L0_grade_gaps?.join(' und ')||'–')}</b><small>Energielücken 1/3 und 1</small></article></div><p><b>Dieser eine Zeitanschluss lässt sich so nicht fortsetzen.</b> In der unverdrehten E₈-Vakuumquelle sind die Gradabstände ganzzahlig. Eine gemeinsame Energieverschiebung ändert die Lücken nicht.</p><small>Ausgeschlossen ist dieselbe L₀-Zeit für Paar und Originaltrimer in dieser Quelle. Andere physische Generatoren und verdrehte Sektoren sind damit nicht ausgeschlossen. Die Stromkorrelationen sind gesondert zu prüfen.</small>`:`<div class="source-grade-flow"><article><span>Fünfer × Gegenfünfer</span><b>1 neutral + 24 Antworten</b><small>Matrix: Spuranteil + spurfreier Anteil</small></article><i>↔</i><article><span>Vorhandene E₈-Quelle</span><b>Vakuum + 24 SU(5)-Ströme</b><small>Grad 0 + Grad 1</small></article></div><p>Die konkrete Abbildung erhält Norm, Ladung und alle 60 alten Quartikereignisse. Ihre Einschränkung hat 15 verschiedene Ereigniswirkungen. Auf diesem Teilraum entspricht I − P<sub>Ω</sub> genau der Quellen-Gradierung L₀.</p><small>Das ist eine bedingte Abbildung in die bereits gewählte affine E₈-Quelle. Dass P1/P2 genau diese Quelle und diese physische Zeit auswählen, folgt daraus noch nicht.</small>`;
  const old=data.lift_separation?.old_quartic_path_lift,cartan=data.lift_separation?.defined_involutive_Cartan_lifts;
  return `<section class="current-source-bridge"><p class="eyebrow">Die Verbindung muss beim nächsten Schritt weitertragen</p><h5>Ein passendes Paar ist noch kein vollständiger Quellenprozess</h5><div class="composition-switch" role="group" aria-label="Quellenanschluss beim Zusammensetzen prüfen">${Object.entries(views).map(([id,title])=>`<button type="button" data-current-bridge="${id}" aria-pressed="${id===active}">${title}</button>`).join('')}</div><div aria-live="polite">${content}</div><details class="source-lift-separation"><summary>Zwei E₈-Hebungen haben verschiedene geladene Wirkungen</summary><table><thead><tr><th></th><th>Quartik-Quellenlift</th><th>Definierte Cartan-Lifts</th></tr></thead><tbody><tr><th>Spur auf 248 Richtungen</th><td>${escapeHTML(old?.E8_adjoint_trace)}</td><td>${escapeHTML(cartan?.full_e8_trace_values?.join(' oder '))}</td></tr><tr><th>Ordnung eines Ereignisses</th><td>${escapeHTML(old?.order)}</td><td>2</td></tr></tbody></table><p>Verschiedene Spuren schließen dieselbe Wirkung auch nach einem Basiswechsel aus. Die Acht-Bit-Fortschreibung weiter unten gehört zum Cartan-Zweig. Der Paaranschluss oben verwendet den älteren Quartik-Zweig.</p></details>${tourSourceLink({path:'tfpt_explorer/current_source_bridge.py',line:1,claim:'Berechnung der Abbildung und ihrer Grenzen'})}</section>`;
}

function renderMarkedClockControls(root,clockData,processData,redraw) {
  const trine=clockData.source_sigma_trine,marking=clockData.marking_compatibility;
  const samples=processData?.native_word_family?.examples||[];
  const sample=samples.find(row=>row.q===app.markedSourceQ)||samples.find(row=>row.q==='1/3')||samples[0];
  root.innerHTML=`<p class="source-graph-equation">Eᵢ = ⅔ Pᵢ · E₁ + E₂ + E₃ = I · T(Eᵢ) = Σⱼ Bᵢⱼ Eⱼ</p><p><b>Wie das zusammenklickt:</b> σ zeichnet den festen Raum aus. Die ursprünglichen Wurzeln zeichnen darin die drei Strahlen aus. Vollständige Normierung bestimmt ihr Gewicht ${escapeHTML(trine.effect_weight)}. Die zugehörigen Spiegelungen und ihre Produkte liefern die alte Ereignisfamilie aus Verifikation v976.</p>${sample?`<div class="source-clock-choice"><h6>Gleiche sichtbare Clock — unterschiedliche vollständige Geschichte</h6><p>Wähle eine zulässige Mischung der tatsächlichen Quellenereignisse. Die beiden bekannten Clock-Antworten bleiben gleich. Die zusätzliche Antwort G = iAF und die Vierpunkt-Operatorantwort F–A–A–F unterscheiden die Mischungen. Letztere wird mit linken Operator-Einsetzungen im GNS-Hilbertraum berechnet; sie ist keine Wahrscheinlichkeit einer Folge von Messausgängen.</p><div class="composition-switch" role="group" aria-label="Native Ereignismischung">${samples.map(row=>`<button type="button" data-marked-q="${escapeHTML(row.q)}" aria-pressed="${row.q===sample.q}">${row.q==='0'?'Nur einzelne Reflexionen':`Zusammengesetzt: q = ${escapeHTML(row.q)}`}</button>`).join('')}</div><div class="source-clock-responses" aria-live="polite"><article><small>Clock A · unverändert</small><b>2/3</b></article><article><small>Clock F · unverändert</small><b>1/3</b></article><article class="source-clock-selected"><small>Zusätzliche Antwort G</small><b>${escapeHTML(sample.q)}</b></article><article class="source-clock-selected"><small>F–A–A–F · Operatorantwort</small><b>${escapeHTML(sample.FAAF_at_unit_intervals)}</b></article></div><p>${sample.q==='0'?'Einzelne native Reflexionen, die den Zweierraum erhalten, erzwingen genau diese Mischung. Sie löscht die dritte Antwort in einem Schritt. Produkte derselben Ereignisse erlauben eine kohärentere Fortsetzung.':`Diese Mischung enthält auch zwei aufeinanderfolgende native Reflexionen. Sie behält den Anteil ${escapeHTML(sample.q)} der dritten Antwort. Die vollständige Familie erlaubt 0 ≤ q ≤ 1/3.`}</p><table class="source-time-meanings"><thead><tr><th>Was bedeutet hier „Zeit“?</th><th>Bei q = ${escapeHTML(sample.q)}</th></tr></thead><tbody><tr><td>Diskrete Mischung der sechs nativen Ereigniswörter</td><td>möglich</td></tr><tr><td>Kontinuierliche Quantenentwicklung auf dem Zweierraum</td><td>${sample.homogeneous_pauli_gksl?'möglich':'kein endlicher homogener Pauli-Generator'}</td></tr><tr><td>Kontinuierliche reversible Sprünge mit denselben sechs Ereigniswörtern</td><td>${sample.homogeneous_native_s3?'möglich':'mit nichtnegativen Ereignisraten ausgeschlossen'}</td></tr></tbody></table><p>Die letzte Forderung ist stärker: Sie erlaubt nur 2/9 ≤ q ≤ 1/4. Bei q=1/3 müsste eine Ereignisrate negativ sein. Die kontinuierliche Quantenentwicklung kann trotzdem existieren, weil ihre Zwischenzeiten nicht Mischungen derselben sechs Ereigniswörter sein müssen.</p><details><summary>Berechnete Gewichte der tatsächlichen Ereigniswörter</summary><table><thead><tr><th>Ereignis</th><th>Gewicht</th></tr></thead><tbody>${sample.weights.map((weight,index)=>`<tr><td>${['Identität','Dreierumlauf vorwärts','Dreierumlauf rückwärts','Spiegelung am Strahl 3','Spiegelung am Strahl 2','Spiegelung am Strahl 1'][index]}</td><td>${escapeHTML(weight)}</td></tr>`).join('')}</tbody></table><p>w(t) = (1/2+t, t, t, 1/18−t, 2/9−t, 2/9−t), q=6t. Die beiden Umlaufrichtungen sind gleich gewichtet; daraus folgt keine physische Händigkeit.</p></details></div>`:''}<p><b>Die zusätzliche Antwort ist in der Quelle vorhanden:</b> G lässt sich auf diesem festen Stromträger exakt aus ladungsneutralen Paaren der ursprünglichen Stromoperatoren rekonstruieren. Ihr tatsächlicher zeitlicher Verlauf und die physische Präparation folgen daraus noch nicht.</p><p><b>Was den Wert 1/3 wirklich auswählen würde:</b> Die ursprüngliche zusätzliche Vorgabe F–A–A–F = 1/27 erzwingt q=1/3. Dasselbe Ergebnis muss jedoch als zeitlich geordnete Operatorantwort der tatsächlichen Quelle folgen. Die bisherige Vorgabe stammt aus dem markierten Compiler-GNS-Prozess; dessen Gleichsetzung mit dieser Quelle ist noch kein bewiesener Schritt.</p><details class="source-marking-correction"><summary>Korrigiert: Der vorherige Viererraum-Anschluss erhält die Originalmarkierung nicht</summary><p>Gleiche Matrixgröße genügt nicht. Original-σ lässt eine Operatoralgebra der Dimension ${marking.source_fixed_algebra_dimension} fest; der bisher verwendete Wort-σ eine der Dimension ${marking.word_fixed_algebra_dimension}. Kein Basiswechsel macht beide markierten Wirkungen gleich. Die unmarkierte M₄-Rechnung bleibt richtig. Der hier gezeigte neue Anschluss verwendet stattdessen den tatsächlichen σ-festen Zweierraum.</p><p>σ-Invarianz allein präpariert diesen Zweierraum noch nicht: Zur gesamten Fixalgebra gehören zusätzlich zwei eindimensionale Sektoren. Auch die Kennung 152 des dritten Strahls bezeichnet nur dieselbe Hecke-Marke wie der Deckcharakter; die Reflexion ist kein geladener Deckoperator.</p></details><details><summary>Warum die drei Anzeigen keine klassische Folge von Messergebnissen sind</summary><p>Jeder der drei Effekte hat größte Eigenzahl 2/3. Deshalb kann nach keiner vorherigen Messung die Wahrscheinlichkeit eines dieser Ausgänge größer als 2/3 sein. Die klassische Matrix B verlangt jedoch für zwei Wiederholungen 13/18. Sie kann daher nicht die Übergangsmatrix wiederholter Messungen derselben drei Effekte sein.</p><p>Gültig bleibt die exakte Fortsetzung ihrer Erwartungswerte ohne eine dazwischengeschaltete Messung. Das ist der oben verwendete Anschluss. Die vollständige Geschichte muss zusätzlich festlegen, welche tatsächlichen Eingriffe erfolgen.</p></details>${tourSourceLink({path:'tfpt_explorer/marked_source_process.py',line:1,claim:'Native Ereignisse, vollständige Zeitfamilie und mehrzeitige Antwort'})}${tourSourceLink({path:'verification/v976_seam_lift_birkhoff.py',line:1,claim:'Ursprüngliche Sechs-Ereignis-Verifikation'})}`;
  $$('[data-marked-q]',root).forEach(button=>button.addEventListener('click',()=>{app.markedSourceQ=button.dataset.markedQ;redraw();$(`[data-marked-q="${app.markedSourceQ}"]`,root).focus({preventScroll:true});}));
}

function renderSourceGraphTour(root,data,coherence,clockData,processData) {
  const map=data.source_rule_map,child=data.marked_d8_child,rec=data.first_child_recursion;
  if(!map||!child||!rec)return;
  const lastStep=clockData?.source_sigma_trine?6:5;
  const rules=map.rule_records||[],step=Math.max(0,Math.min(lastStep,app.sourceGraphStep||0));
  const rule=rules.find(row=>row.rule===app.sourceGraphRule)||rules.find(row=>row.character_mask===child.character_mask)||rules[0];
  const full=app.sourceGraphKeep!==false,phaseFull=app.sourceGraphFullPhase!==false;
  const phaseCarry=data.dual_recursion?.phase_carry_completion;
  const phaseExtension=data.general_phase_extension;
  const phaseExamples=phaseExtension?.examples||[];
  const phaseDepth=Math.max(0,Math.min(app.sourceGraphDepth??2,phaseExamples.length-1));
  const phaseExample=phaseExamples[phaseDepth];
  const frames=[
    {title:'Die Vergröberungsmarken sind in denselben Quelldaten verankert.',body:`Die ${map.event_count} nativen Reflexionen bestimmen ${map.rule_count} mögliche Untergitter. Je vier Reflexionen tragen dieselbe Untergittermarke. Das wurde an der tatsächlichen Wirkung auf allen 240 Wurzeln geprüft. Ihre vier unterschiedlichen Ereigniswirkungen bleiben erhalten.`,meaning:'Ein Ereignis und eine Vergröberung besitzen jetzt eine konkrete gemeinsame Adresse. Die Reflexion wirkt auf Zustände desselben Gitters; die Vergröberung wählt ein Untergitter.'},
    {title:'Eine Marke teilt die Quelle in zwei zusammengehörige Teile.',body:`Die bekannte Deckmarke ${child.character_mask} erhält ${child.even_current_dimension} Stromrichtungen und zeichnet ${child.odd_current_dimension} weitere aus. Der erste Teil ist D₈: 112 Wurzelrichtungen und acht Cartanrichtungen. Die 128 anderen sind genau der Spinoranteil.`,meaning:'Das ist derselbe geladene Unterschied, der schon bei verschiedenen Ereignisgeschichten auftreten kann. Die Zahlen zählen interne Stromrichtungen, keine Orte oder Teilchensorten.'},
    {title:'Der zweite Teil muss weiter wirken können.',body:'Ein geladenes Feld kann zwischen den beiden Teilen wechseln. Löscht man alle ungeraden Felder, verliert man auch ihre gemeinsame Wirkung: Zwei entgegengesetzt geladene Felder können zusammen eine erhaltene Cartanantwort erzeugen.',meaning:full?'Beide Teile samt ihren Übergängen bleiben vorhanden. So ist die Aufteilung verlustfrei. Ein klassischer Zettel mit zwei Sektornamen reicht dafür nicht.':'Der ungerade Teil ist ausgeblendet. Die Rechnung zeigt jetzt, welche mögliche spätere Antwort dadurch fehlen würde. Das ist eine veränderte Quellenalgebra.'},
    {title:'Normierung allein wählt noch kein Ereignisgesetz.',body:`Alle 15 geraden Projektionen zusammen ergeben auf der Nullklasse den Wert ${data.instruments.projector_sum.zero_class}, auf jeder anderen Klasse ${data.instruments.projector_sum.nonzero_class}. Eine gemeinsame Zahl kann daher nicht alle Zustände zugleich normieren. Behält man beide Teile kohärent, ist eine normerhaltende Abbildung möglich.`,meaning:`Wird der zusätzliche Träger danach verworfen, schrumpft die Kohärenz zwischen verschiedenen Klassen auf ${data.instruments.unread_interclass_coherence}. Die Häufigkeit, mit der eine der 15 Marken verwendet wird, bleibt eine eigene Auswahl.`},
    {title:'Der vorhandene Phasenspeicher stellt die nächsten Tests bereit.',body:`Die geerbte Selbstpaarung des Untergitters erreicht nur ${rec.nonzero_polarity_labels} verschiedene nichttriviale Tests. Mit dem eindeutig bestimmten dualen Raum sind wieder ${data.dual_recursion?.nonzero_dual_probes} möglich. Diese Tests lassen sich bereits als Vorzeichenwirkungen auf der ursprünglichen E₈-Quelle ausführen. Neue physische Felder werden dafür nicht eingeführt.`,meaning:phaseFull?`Für jedes erste Untergitter gibt es ${phaseCarry?.per_child_extension_count} solche Fortsetzungen. Über alle 15 Möglichkeiten hinweg bilden sie genau die ${phaseCarry?.total_character_count} Vorzeichencharaktere des vorhandenen Acht-Bit-Trägers. Jede Kindprobe besitzt zwei Fortsetzungen, die sich um ihren Deckcharakter unterscheiden. Das verbindet die vollständige erste Vergröberung mit dem bestehenden Phasenspeicher.`:'Die Selbstpaarung allein sieht nur drei nächste Tests. Zusätzliche gültige Tests werden erst mit den vollständigen Charakteren der ursprünglichen Quelle sichtbar. Rangverlust bedeutet hier daher keine Sackgasse.'},
    {title:'Die Phasenfortsetzung erhält die vollständigen Quellgleichungen.',body:'Die mitgeführten Phasen passen auch zur geladenen Feldwirkung: Treffen zwei Ladungen zusammen, multiplizieren sich ihre Phasen genau zur Phase der Gesamtladung. Entgegengesetzte Ladungen kompensieren sich. Dadurch bleibt die vollständige Quellenantwort bei gemeinsamer Phasentransformation aller Beteiligten erhalten.',meaning:'Dieser Anschluss gilt für jede endliche Phasenfortsetzung und erhält die Stromalgebra und Ward-Gleichungen dieser E₈-Quelle. Die konsistenten KZ-Rechenwege des SU(5)-Anteils wurden zusätzlich geprüft. Die beiden Operationen bleiben verschieden: Eine Vergröberung wählt ein Untergitter; KZ transportiert eine Antwort auf einer vorgegebenen Einfügegeometrie. Das ist noch keine Auswahl physischer Orte oder Zeit.'}
  ];
  if(clockData?.source_sigma_trine)frames.push({title:'Die ursprüngliche Markierung liefert genau die drei Clock-Richtungen.',body:'Die Familienmarkierung σ lässt einen Zweierraum der tatsächlichen Quelle fest. Darin liegen zwölf E₈-Wurzeln, also genau drei unterschiedliche Strahlen. Ihre eindeutig normierten Projektoren ergeben exakt die bisherige Dreier-Auslese. Die Spiegelungen an diesen Strahlen realisieren die schon früher untersuchten sechs Vertauschungsregeln.',meaning:'Geometrie, ursprüngliche Clock und native Ereignisse sind damit verbunden. Welche vollständige Zeitantwort die Quelle realisiert, muss an ihrem gemeinsamen Prozess entschieden werden. Die Auswahl des festen Zweierraums als physisch präpariertem Sektor bleibt dabei ausdrücklich eine Voraussetzung.'});
  const frame=frames[step];
  const stepTitles=['Gemeinsame Adresse','Zwei Teile','Geladene Wirkung','Norm und Erinnerung','Nächster Schritt','Konsistente Wege',...(lastStep===6?['Markierung und Zeit']:[])];
  root.innerHTML=`<p class="eyebrow">Zuse + Wolfram · an den ursprünglichen TFPT-Operationen geprüft</p><h5>Vom Ereignis zur Vergröberung: Was hängt wirklich zusammen?</h5><p>Die bisher getrennten Beschreibungen besitzen einen berechneten gemeinsamen Anschluss. Diese ${frames.length} Schritte zeigen ihn und prüfen sofort, ob er auch beim nächsten Schritt trägt.</p><nav class="source-graph-steps" aria-label="Schritte der Quellen-Graph-Tour">${stepTitles.map((title,i)=>`<button type="button" data-source-graph-step="${i}" aria-pressed="${i===step}"><b>${i+1}</b><span>${title}</span></button>`).join('')}</nav><div class="source-graph-reading" aria-live="polite"><p class="eyebrow">Schritt ${step+1} von ${frames.length}</p><h6>${frame.title}</h6><p>${frame.body}</p></div><div class="source-graph-picture"></div><div class="source-graph-controls"></div><p class="source-graph-meaning">${frame.meaning}</p><div class="source-graph-navigation"><button class="mini-button" type="button" data-graph-prev ${step===0?'disabled':''}>← Zurück</button><button class="mini-button" type="button" data-graph-next ${step===lastStep?'disabled':''}>Weiter →</button></div><div class="source-graph-whole"><b>Wie daraus die gesuchte Gesamtlösung werden müsste</b><p>Der diskrete Bootstrap bestimmt die gemeinsame Struktur. Die Ströme liefern Code, Paarantwort und zusätzliche Anregungen. Der neue Anschluss verbindet dieselbe Quelle mit den Vergröberungsmarken. Die algebraische Fortschreibung ist berechnet. Für ihre physische Ausführung muss dieselbe Quelle bestimmen: Welche Beteiligten treffen sich, mit welchen Amplituden und unter welcher gemeinsamen Zeit? Erst derselbe so ausgewählte Prozess muss räumliche Lokalität, chirale Materie, α, Flavor und Gravitation zugleich wiedergeben.</p><p>Die berechnete Verbindung schließt das Wörterbuch zwischen Ereignismarke, Untergitter und geladenem Sektor sowie dessen algebraische Phasenfortsetzung in jeder endlichen Tiefe. Sie schließt noch keine vollständige 3+1-dimensionale Weltdynamik. Die optionale E₈-Skalenkaskade wird dafür nicht vorausgesetzt.</p></div><details><summary>Welcher Graph ist jeweils gemeint?</summary><table><thead><tr><th>Knoten</th><th>Verbindung</th><th>Was daraus folgt</th></tr></thead><tbody><tr><td>Quellenzustände</td><td>Geladene Operatorwirkung</td><td>Eine tatsächlich berechenbare Änderung</td></tr><tr><td>Untergitter</td><td>Einschluss / Hecke-Schritt</td><td>Arithmetische Vergröberung; noch keine physische Zeit</td></tr><tr><td>Ereignisse</td><td>Ein Ereignis ermöglicht ein anderes</td><td>Kausale Abhängigkeit; gleicher Endzustand allein reicht nicht</td></tr><tr><td>Physische Orte</td><td>Lokale Wechselwirkung</td><td>Dieser Anschluss und sein Grenzfall müssen aus dem Prozess folgen</td></tr></tbody></table><p>Zuse beschreibt schon wachsende Netze mit gespeicherter Information auf Leitungen. Wolframs Mehrwege-Idee hilft, alternative Abläufe zu ordnen. Ihre Übertragung benötigt hier die tatsächlich berechneten komplexen Wirkungen einschließlich der mitgeführten Information.</p><p><a href="https://github.com/maxitg/SetReplace/blob/master/Research/ConfluenceAndCausalInvariance/ConfluenceAndCausalInvariance.md" target="_blank" rel="noopener">Wolfram/SetReplace: Zusammenlaufen ist nicht kausale Invarianz</a> · <a href="https://arxiv.org/html/2512.20587v1" target="_blank" rel="noopener">Multiway-Quantenkonstruktion: zusätzliche Pfadgewichte</a></p></details><details><summary>Exakte Rechnungen und ursprüngliche Quellen</summary><p>60 Ereigniswirkungen × 240 Wurzeln; 15 kanonische Untergitter; geerbte Paarung nach dem ersten Schritt; vollständige Normierung auf 16 Klassen. Die KZ-Rechnung unterscheidet eine physische Fusionslösung von ihren zwei Tensorkoordinaten. Ein Rang oder eine Zahl von Zweigen zählt hier keine Raumdimension.</p>${['tfpt_explorer/hecke_source.py','tfpt_explorer/rewrite_coherence.py','verification/v689_gaussian_code_bridge.py','verification/v753_ramified_polarity.py'].map(path=>tourSourceLink({path,line:1,claim:path.split('/').pop()})).join('')}</details>`;
  const svg=svgEl('svg',{viewBox:'0 0 1000 310',role:'img','aria-label':frame.title});
  const graphDefs=svgEl('defs'),graphMarker=svgEl('marker',{id:'source-graph-arrow',viewBox:'0 0 10 10',refX:8,refY:5,markerWidth:7,markerHeight:7,orient:'auto-start-reverse'});graphMarker.append(svgEl('path',{d:'M 0 0 L 10 5 L 0 10 z',fill:'#78958b'}));graphDefs.append(graphMarker);svg.append(graphDefs);
  const box=(x,y,w,h,title,subtitle,color='#124f42')=>{svg.append(svgEl('rect',{x,y,width:w,height:h,rx:16,fill:color}));sceneText(svg,x+w/2,y+40,title,'scene-title scene-on-dark','middle');sceneText(svg,x+w/2,y+69,subtitle,'scene-small scene-on-dark','middle');};
  if(step===6){
    box(20,88,268,110,'Ursprünglicher σ-Fixraum','12 Wurzeln → 3 Strahlen');
    sceneArrow(svg,298,143,357,143);
    svg.append(svgEl('circle',{cx:475,cy:143,r:80,fill:'#f0f4f2',stroke:'#b8cec2','stroke-width':2}));
    [[-Math.PI/6,'1'],[-5*Math.PI/6,'2'],[Math.PI/2,'3']].forEach(([angle,label])=>{const x=475+67*Math.cos(angle),y=143+67*Math.sin(angle);svg.append(svgEl('line',{x1:475,y1:143,x2:x,y2:y,stroke:'#7160a5','stroke-width':4}));svg.append(svgEl('circle',{cx:x,cy:y,r:16,fill:'#7160a5'}));sceneText(svg,x,y+5,label,'scene-small scene-on-dark','middle');});
    sceneText(svg,475,38,'Drei gleichberechtigte Ausleserichtungen','scene-small','middle');
    sceneText(svg,475,258,'Bloch-Bild: 120° zwischen den Richtungen','scene-small','middle');
    sceneArrow(svg,590,143,646,143);
    box(663,88,315,110,'Clock-Antwort bleibt dieselbe','A → 2/3 A · F → 1/3 F');
    sceneText(svg,500,301,'Die dritte Antwort G wird erst durch das vollständige Ereignisgesetz bestimmt.','scene-label','middle');
  }else if(step===4){
    box(55,90,255,105,'Quelle aufteilen','15 mögliche Untergitter');
    box(385,90,240,105,'Geerbte Selbstpaarung',`${rec.nonzero_polarity_labels} nächste Tests`,'#7160a5');
    box(700,90,250,105,phaseFull?'Voller Phasenspeicher':'Unvollständige Sicht',phaseFull?`${data.dual_recursion?.nonzero_dual_probes} nächste Tests`:'nur 3 sichtbar',phaseFull?'#124f42':'#9a6930');
    sceneArrow(svg,317,141,376,141);sceneArrow(svg,632,141,692,141);
    sceneText(svg,500,255,phaseFull?`${phaseCarry?.total_character_count} mögliche Vorzeichenwirkungen = der vorhandene Acht-Bit-Träger`:'Mit der geerbten Selbstpaarung allein fehlt ein Teil der nächsten Tests.','scene-label','middle');
  }else if(step===5){
    const phase=coherence?.physical_block?.collisions?.[0];
    box(55,100,260,102,'SU(5)-Anteil',`Phase: ${phase?.su5_phase_turns_mod_one||'1/5'} Umlauf`,'#7160a5');
    box(365,100,270,102,'Partneranteil','entgegengesetzte Phase','#95662f');
    box(700,100,250,102,'Volle Antwort','Gesamtphase: 1');
    sceneText(svg,340,158,'×','scene-title','middle');sceneArrow(svg,647,152,691,152);
    sceneText(svg,500,65,'Dieselbe Quellenantwort, vollständig transportiert','scene-title','middle');
    sceneText(svg,500,260,'Lokale KZ-Konsistenz: exakt. Einfügeposition ≠ schon physische Zeit.','scene-label','middle');
  }else{
    box(30,100,210,104,'E₈-Quelle','248 Stromrichtungen');
    box(370,30,265,98,'D₈-Teil','112 Wurzeln + 8 Cartanrichtungen');
    box(370,180,265,98,'Spinoranteil','128 geladene Richtungen',step===2&&!full?'#9ca4a0':'#7160a5');
    box(755,100,210,104,step===2&&!full?'Unvollständig':'Beide Teile',step===2&&!full?'geladene Antwort fehlt':'mit ihren Übergängen',step===2&&!full?'#9a6930':'#124f42');
    sceneArrow(svg,245,140,359,82);sceneArrow(svg,245,166,359,227);sceneArrow(svg,641,82,744,140);
    if(step!==2||full)sceneArrow(svg,641,227,744,166);
    sceneText(svg,502,157,'geladene Felder ↕','scene-label','middle');
    if(step===0)sceneText(svg,300,40,`Marke ${rule.character_mask}`,'scene-small','middle');
    if(step===3)sceneText(svg,852,248,'Kohärenz behalten','scene-small','middle');
  }
  $('.source-graph-picture',root).append(svg);
  const controls=$('.source-graph-controls',root);
  if(step===0){controls.innerHTML=`<label>Eine der 15 tatsächlichen Untergittermarken <select aria-label="Hecke-Untergittermarke">${rules.map(row=>`<option value="${row.rule}" ${row.rule===rule.rule?'selected':''}>Marke ${row.character_mask}${row.character_mask===child.character_mask?' · ursprünglicher Deckcharakter':''}</option>`).join('')}</select></label><p>Zu dieser Marke gehören die nativen Ereignisse <b>${rule.event_indices.join(', ')}</b>. Jede Marke erhält ${rule.root_even_count} Wurzeln; ${rule.root_odd_count} liegen im anderen Teil. Die Abbildung erhält die Gruppenwirkung.</p>`;$('select',controls).addEventListener('change',event=>{app.sourceGraphRule=Number(event.target.value);renderSourceGraphTour(root,data,coherence,clockData,processData);$('select',root).focus({preventScroll:true});});}
  if(step===2){controls.innerHTML=`<div class="composition-switch" role="group" aria-label="Geladene Information erhalten"><button type="button" data-graph-keep="yes" aria-pressed="${full}">Beide Teile erhalten</button><button type="button" data-graph-keep="no" aria-pressed="${!full}">Ungeraden Teil ausblenden</button></div><p class="source-graph-equation">${full?'[eα, e−α] = hα ≠ 0':'[P eα, P e−α] = 0, aber P[eα, e−α] = hα ≠ 0'}</p>${data.charged_record_transport?`<p><b>Die Fortsetzung ist ausdrücklich berechnet:</b> Ändert ein geladenes Feld den Quellenzustand, ändert es zugleich dessen gespeicherte Phasenadresse. Der Speicher bleibt Teil der nächsten Wirkung.</p><p class="source-graph-equation">Feld mit Ladung α: Zustand ändern + Adresse r → r + r(α)</p><p>Beides zusammen ergibt exakt dieselbe Feldwirkung wie vor der Aufteilung. Würde nur der Zustand verändert und die Adresse festgehalten, wäre bereits die Erzeugung eines geladenen Stromzustands falsch.</p>`:''}`;$$('[data-graph-keep]',controls).forEach(button=>button.addEventListener('click',()=>{app.sourceGraphKeep=button.dataset.graphKeep==='yes';renderSourceGraphTour(root,data,coherence,clockData,processData);$(`[data-graph-keep="${app.sourceGraphKeep?'yes':'no'}"]`,root).focus({preventScroll:true});}));}
  if(step===4){controls.innerHTML=`<div class="composition-switch" role="group" aria-label="Fortsetzung der Vergröberung"><button type="button" data-graph-phase="no" aria-pressed="${!phaseFull}">Nur geerbte Selbstpaarung</button><button type="button" data-graph-phase="yes" aria-pressed="${phaseFull}">Vollständiger Phasenspeicher</button></div><p>Die Zahl 15 zählt mögliche Tests. Welche davon als nächstes geschieht und wie sie gewichtet wird, wird damit noch nicht ausgewählt.</p>${phaseExample?`<div class="source-phase-continuation"><h6>Und danach? Die Phasen werden feiner.</h6><p>Vorzeichen sind wie ein Zeiger mit nur zwei Stellungen. Schon nach zwei Vergröberungen braucht das berechnete Beispiel vier Stellungen; später acht. Die Quelle bleibt dieselbe. Wir müssen genauer mitführen, wie ihre geladenen Anteile zueinander stehen.</p><label>Berechnete Tiefe: <b>${phaseExample.depth}</b><input type="range" min="0" max="${phaseExamples.length-1}" value="${phaseDepth}" step="1" aria-label="Vergröberungstiefe im berechneten Beispiel"></label><div class="source-phase-picture"></div><p class="source-graph-equation">θ = K⁻ᵀc · χ(x) = exp(iπ θ·x)</p><p><b>Warum das für jede endliche Tiefe trägt:</b> K beschreibt die tatsächlich gewählte Untergitterbasis. Die Formel berechnet die ursprüngliche Quellenphase so, dass sie auf diesem Untergitter genau den gewünschten Test ergibt: Kᵀθ = c. Acht rationale Phasenkoordinaten ersetzen bei tieferer Rekursion die bloßen acht Bits.</p><p>Ein Quellenzeiger mit ${phaseExample.phase_order} Stellungen muss in ${phaseExample.phase_order} Phasensektoren aufgeteilt werden. Die beiden Teile des ursprünglichen Vorzeichentests reichen auf der gesamten Quelle dann nicht immer. Behält man alle Sektoren kohärent, bleibt die Norm erhalten.</p><small>Die gezeigte Folge verwendet wiederholte (1+i)-Vergröberungen einer ursprünglichen Gauß-Koordinate. Sie demonstriert die allgemeine Formel; sie wählt keinen physischen Ablauf. Diese Phasen sind nicht allein wegen ihrer Anzahl mit der ursprünglichen Clock identifiziert.</small></div>`:''}`;$$('[data-graph-phase]',controls).forEach(button=>button.addEventListener('click',()=>{app.sourceGraphFullPhase=button.dataset.graphPhase==='yes';renderSourceGraphTour(root,data,coherence,clockData,processData);$(`[data-graph-phase="${app.sourceGraphFullPhase?'yes':'no'}"]`,root).focus({preventScroll:true});}));
    if(phaseExample){const phaseSvg=svgEl('svg',{viewBox:'0 0 800 220',role:'img','aria-label':`Tiefe ${phaseExample.depth}: ${phaseExample.phase_order} exakte Phasenstellungen, Untergitterindex ${phaseExample.source_index}`});const count=phaseExample.phase_order;
      phaseSvg.append(svgEl('circle',{cx:140,cy:110,r:72,fill:'none',stroke:'#b8cec2','stroke-width':2}));
      for(let j=0;j<count;j++){const angle=2*Math.PI*j/count-Math.PI/2,x=140+72*Math.cos(angle),y=110+72*Math.sin(angle);phaseSvg.append(svgEl('line',{x1:140,y1:110,x2:x,y2:y,stroke:j===0?'#124f42':'#d6e3dc','stroke-width':j===0?4:2}));phaseSvg.append(svgEl('circle',{cx:x,cy:y,r:7,fill:'#7160a5'}));}
      sceneText(phaseSvg,300,65,`${count} mögliche Phasenstellungen`,'scene-title');sceneText(phaseSvg,300,108,`Untergitterindex: ${phaseExample.source_index} · Tiefe: ${phaseExample.depth}`,'scene-label');sceneText(phaseSvg,300,148,'Alle Stellungen gehören zur selben E₈-Quelle.','scene-label');sceneText(phaseSvg,300,181,phaseExample.restriction_exact?'Gewünschter Kindtest exakt wiederhergestellt.':'Prüfung nicht bestätigt.','scene-small');$('.source-phase-picture',controls).append(phaseSvg);
      $('input[type="range"]',controls).addEventListener('input',event=>{app.sourceGraphDepth=Number(event.target.value);renderSourceGraphTour(root,data,coherence,clockData,processData);$('input[type="range"]',root).focus({preventScroll:true});});
    }
  }
  if(step===5&&coherence?.phase_ward_compatibility){const compatible=coherence.phase_ward_compatibility;controls.innerHTML=`<p class="source-graph-equation">χ(α + β) = χ(α)χ(β) · χ(α)χ(−α) = 1</p><p>Für jede gezeigte Tiefe wurden alle <b>${compatible.examples[0].root_sum_brackets.toLocaleString('de-DE')} geladenen Wurzelklammern</b> und alle 240 geordneten Gegenwurzelpaare exakt geprüft. Die allgemeine Aussage folgt aus der Multiplikation der Charaktere.</p><p><b>Gemeinsam verändern ist entscheidend:</b> Wird die Phase nur an einem Beteiligten verändert, bleibt ihre Wirkung sichtbar. Werden alle Beteiligten samt ihrem Zustand konsistent transformiert, bleibt dieselbe Antwort erhalten. Die ausgeschiedenen geladenen Felder dürfen dabei nicht gelöscht werden.</p><p>Zusätzlich kompensieren sich beim vollen Umlauf die gebrochenen SU(5)- und Partnerphasen. Überlappende Paaroperationen vertauschen einzeln nicht; ihre vollständige Verbindung erfüllt dennoch exakt die Konsistenzgleichungen.</p>`;}
  if(step===6)renderMarkedClockControls(controls,clockData,processData,()=>renderSourceGraphTour(root,data,coherence,clockData,processData));
  const move=index=>{app.sourceGraphStep=index;renderSourceGraphTour(root,data,coherence,clockData,processData);$(`[data-source-graph-step="${index}"]`,root).focus({preventScroll:true});};
  $$('[data-source-graph-step]',root).forEach(button=>button.addEventListener('click',()=>move(Number(button.dataset.sourceGraphStep))));
  $('[data-graph-prev]',root).addEventListener('click',()=>move(step-1));
  $('[data-graph-next]',root).addEventListener('click',()=>move(step+1));
}

function sourceFieldLabel(field) {
  return `${field.kind}${field.kind==='X'?`(${field.i+1},${field.a+1})`:`(${field.a+1})`}${field.dagger?'†':''}`;
}

function sourceHypergraphSVG(result) {
  const fields=result.word||[],n=fields.length,cx=380,cy=180;
  const points=fields.map((field,i)=>({field,x:cx+255*Math.cos(-Math.PI/2+2*Math.PI*i/n),y:cy+135*Math.sin(-Math.PI/2+2*Math.PI*i/n)}));
  return `<svg viewBox="0 0 760 375" role="img" aria-label="${n} Feldeinsetzungen tragen gemeinsam den verbundenen Antwortwert ${escapeHTML(result.connected_value_exact)}. Die Linien bezeichnen rechnerische Beteiligung, keine räumlichen Verbindungen."><title>Ein gemeinsamer Antwortkoeffizient</title>${points.map(p=>`<path d="M${p.x},${p.y} Q${cx},${p.y} ${cx},${cy}" fill="none" stroke="#599785" stroke-width="4" opacity=".65"/>`).join('')}<rect x="286" y="143" width="188" height="74" rx="22" fill="#165646"/><text x="380" y="169" text-anchor="middle" fill="#d4eee3" font-size="13">gemeinsame Antwort</text><text x="380" y="197" text-anchor="middle" fill="white" font-size="23" font-weight="700">${escapeHTML(result.connected_value_exact)}</text>${points.map((p,i)=>`<rect x="${p.x-65}" y="${p.y-26}" width="130" height="52" rx="14" fill="#f7fbf8" stroke="#97b6a7"/><text x="${p.x}" y="${p.y-3}" text-anchor="middle" fill="#173f34" font-size="16" font-weight="700">${escapeHTML(sourceFieldLabel(p.field))}</text><text x="${p.x}" y="${p.y+16}" text-anchor="middle" fill="#55746b" font-size="12">Position ${escapeHTML(result.positions[i])}</text>`).join('')}<text x="380" y="365" text-anchor="middle" fill="#55746b" font-size="13">Feldantworten verbinden sich · die Zeichnung ist kein Raumzeitnetz</text></svg>`;
}

function renderSourceProgram(root,data,unification) {
  if(!root||!data?.example)return;
  const steps=['Eine Quelle','Dieselbe Zeit','Beide Indizes','Echter Hypergraph','Die ganze Physik'];
  const index=Math.max(0,Math.min(app.sourceProgramStep||0,steps.length-1));
  app.sourceProgramStep=index;
  const stress=unification?.shared_stress_tensor||{},extension=unification?.a8_extension||{},quantization=unification?.direct_quantization||{};
  const cards=[
    `<h5>Ein Objekt beantwortet alle Feldfragen</h5><p>Stell dir die Quelle als ein einziges Regelwerk vor. Du gibst an, welche Felder du an welchen Stellen einsetzt. Die Quelle berechnet ihre gemeinsame Antwort. Zustand, Ladungen, Rekursion und konforme Zeit sind Teile desselben Aufbaus.</p><div class="source-program-flow"><article><small>Ursprünglicher Compiler</small><b>Markiertes E₈-Gitter</b><span>Double Cover · P1/P2 · μ₄</span></article><span aria-hidden="true">→</span><article><small>Erklärte Quantisierung</small><b>Hilbertraum + Vakuum + Felder</b><span>minimale lokale Level-1-Quelle</span></article><span aria-hidden="true">→</span><article><small>Ein gemeinsames Gesetz</small><b>Alle Stromantworten</b><span>einschließlich geladener Zwischenzustände</span></article></div><p>Die vier C-Felder und zwanzig X-Felder erzeugen zusammen mit ihren Gegenfeldern die ganze E₈-Stromalgebra. Das ursprüngliche Gitter-VOA-Verfahren konstruiert diese Quelle direkt.</p><p class="source-program-premise"><b>Die präzise zusätzliche Herkunftsannahme:</b> ${escapeHTML(quantization.origin_assumption||'Die physische TFPT-Quelle ist die minimale positive lokale Vakuumquantisierung des ursprünglichen markierten Ladungsgitters.')}</p><details><summary>Die vollständige Rechenregel</summary><pre>F₀ = 1 · F₁ = 0\n${escapeHTML(data.rule)}</pre><p>Ein Feld wird mit einem anderen gepaart oder durch ihre tatsächliche E₈-Klammer mit ihm verschmolzen. Jeder Schritt verkürzt die Anfrage. Die vorhandene Paarung und Klammer bestimmen die Gewichte; es werden keine neuen Graphgewichte gewählt.</p><p>Die Antwortfunktion gilt für beliebige endliche Stromwörter. Eine vorgegebene Position ist eine Eingabe dieser Funktion. Sie ist keine neue Naturgesetzannahme.</p>${tourSourceLink({path:'tfpt_research_contracts.tex',line:1271,claim:'Original: direkter Gitter-VOA-Aufbau'})}${tourSourceLink({path:'tfpt_explorer/source_program.py',line:1,claim:'Ausführbare volle Quellenregel'})}</details>`,
    `<h5>Die alte und die neue Zerlegung laufen mit derselben Uhr</h5><p>Man kann denselben Raum unterschiedlich aufteilen. Entscheidend ist hier: Beide Aufteilungen ergeben exakt denselben mathematischen Zeitgenerator, weil ihre orthogonalen Teile zusammen denselben vollständigen Raum ausfüllen.</p><div class="source-time-decompositions"><article><span>Ursprünglicher Aufbau</span><b>D₅ ⊕ A₃</b><div><i style="flex:5">5</i><i style="flex:3">3</i></div></article><strong aria-hidden="true">=</strong><article><span>Geladene 5 × 4-Struktur</span><b>A₄ ⊕ A₃ ⊕ u(1)</b><div><i style="flex:4">4</i><i style="flex:3">3</i><i style="flex:1">1</i></div></article></div><p class="source-program-equation">T<sub>E₈</sub> = T<sub>D₅</sub> + T<sub>A₃</sub> = T<sub>A₄</sub> + T<sub>A₃</sub> + T<sub>u(1)</sub></p><p><b>Exakte Grundlage:</b> Die drei berechneten Projektoren summieren sich zur Identität. Dadurch stimmen die ganzen Virasoro-Generatoren überein. Die Zahlen 5+3 und 4+3+1 allein wären dafür kein Beweis.</p><div class="source-program-pair"><article><b>Zwanzig X-Felder</b><p>Gewicht: 2/5 + 3/8 + 9/40 = 1</p></article><article><b>Vier C-Felder</b><p>Gewicht: 3/8 + 5/8 = 1</p></article></div><p>Die X-Felder erzeugen A₈. Die volle E₈-Quelle ergänzt seine Wurzelsektoren zu 72 + 84 + 84. Die ursprünglichen C-Felder gehören zu einem der beiden 84er-Sektoren. Auch diese Erweiterung behält denselben Zeitgenerator.</p><small>Die gemeinsame Zeit ist die konforme Zeit dieser Quelle. Ihre Identifikation mit unserer 3+1-dimensionalen Laborzeit bleibt eine physikalische Abbildung. Der relative u(1)-Generator und diese Z₃-Erweiterung werden nicht mit P2-Hyperladung bzw. Familienzahl gleichgesetzt.</small><details><summary>Exakt berechnete Verbindung</summary><pre>${escapeHTML(stress.identity||'Gleicher Virasorovektor im selben E₈-Raum')}\nA₈-Determinante: ${escapeHTML(extension.determinant??'–')}\n${escapeHTML(stress.meaning||'')}</pre>${tourSourceLink({path:'tfpt_explorer/source_unification.py',line:1,claim:'Originalwurzeln, Projektoren und gemeinsame Zeit'})}</details>`,
    `<h5>Die Rekursion erhält beide internen Indizes gemeinsam</h5><p>Jedes geladene Feld X(i,a) besitzt einen Fünferindex und einen Viererindex. Fasst man drei Feldeinsetzungen an den ursprünglichen harmonischen Marken zusammen, rekodiert dieselbe Quellenantwort beide Indizes.</p><div class="source-program-flow source-recursion-flow"><article><small>Eingang</small><b>X(i,a)</b><span>5 × 4 = 20 Komponenten</span></article><span aria-hidden="true">→</span><article><small>Dieselbe Stromantwort</small><b>W₅ ⊗ W₄</b><span>beide Indizes werden weitergetragen</span></article><span aria-hidden="true">→</span><article><small>Drei zusammengehörige Felder</small><b>X ⊗ X̄ ⊗ X</b><span>20³ mögliche Komponenten</span></article></div><p class="source-program-equation">N†N = 120 I₂₀ → W†W = I₂₀</p><p>Nach Normierung bleibt jede Information des zwanzigdimensionalen Eingangs erhalten. Die Rechnung prüft alle ${escapeHTML(data.joint_recursion.coefficient_triples_checked)} Stromausgaben direkt mit den ursprünglichen E₈-Klammern.</p><p>Damit sind die beiden Rekursionen Ausschnitte eines gemeinsamen Gesetzes. Die volle Quelle führt außerdem die C-Felder und alle nötigen Zwischenzustände mit.</p><details><summary>Warum der vollständige Prozessor erhalten bleibt</summary><p>Der gemischte C-X-Vierpunktwert beträgt ${escapeHTML(data.full24_mixed_response.value_exact)}. Ein pauschaler Ersatz durch W₆ ⊗ W₄ würde ${escapeHTML(data.full24_mixed_response.naive_W6_tensor_W4_value)} liefern. Deshalb wird die volle 24er-Signatur durch die ursprüngliche Ward-Regel berechnet. Der W₅ ⊗ W₄-Block ist ihre exakte harmonische X-Ansicht.</p><pre>${escapeHTML(data.joint_recursion.tensor)}</pre><p>Die mittlere Komponente ist konjugiert. Die Skizze zeigt interne Feldkomponenten, keine räumlich erzeugten Teilchen. Bei endlichen Abständen bleiben die weiteren Stromnachkommen erhalten.</p></details>`,
    `<h5>Eine Verbindung, die erst mit allen sechs Feldern entsteht</h5><p>Im festen Referenzbeispiel X(1,1), X(2,1)†, X(2,2), X(3,2)†, X(3,3), X(1,3)† hat jede echte Teilgruppe die Antwort null. Trotzdem antwortet die ganze Sechsergruppe mit ${escapeHTML(data.example.value_exact)}. Ihre Gesamtladung verschwindet; jede echte Teilgruppe trägt noch Ladung. Ein Bild aus bloßen Paarantworten würde diesen Zusammenhang verlieren.</p><h6>Aktuelle Anfrage · anfangs das Referenzbeispiel</h6><div data-live-source-graph>${sourceHypergraphSVG(app.sourceProgramResult||data.example)}</div><p>Diese Hyperkante kommt vollständig aus derselben Paarungs- und Verschmelzungsregel. Sie ist eine verbundene Feldantwort. Sie behauptet weder eine zusätzliche Sechskörperkraft noch einen räumlichen Fernkontakt.</p><div class="source-program-stat"><b>${escapeHTML(data.connected_six_point.proper_subcorrelators_zero)} / ${escapeHTML(data.connected_six_point.proper_subcorrelators_tested)}</b><span>echte Teilgruppen des festen Referenzbeispiels verschwinden identisch; dieser Befund wird nicht auf geänderte Anfragen übertragen</span></div><form class="source-word-form"><h6>Dieselbe Quelle selbst befragen</h6><p>Ändere Felder oder rationale Positionen. Die Antwort wird aus der ursprünglichen E₈-Klammer neu berechnet. Die Feldnummern beginnen hier bei 1.</p><div class="source-word-inputs"></div><button type="submit">Antwort berechnen</button><output class="source-word-result" aria-live="polite"></output></form><details><summary>Was Zuse und Wolfram hier beitragen</summary><p>Zuses Idee einer ausführbaren Weltregel erhält hier einen konkreten mathematischen Kandidaten. Der Hypergraph macht sichtbar, welche Einsetzungen gemeinsam zu einer Antwort gehören. Die Gewichte stammen aus der TFPT-Quelle.</p><p>Verschiedene Ward-Rechenbäume berechnen dieselbe Antwort. Sie sind keine zusätzlich zu gewichtenden Weltgeschichten. Ein räumlicher Graph, ein kausaler Ereignisgraph und dieser Graph der Feldantworten erfüllen unterschiedliche Aufgaben.</p><pre>${escapeHTML(data.connected_six_point.symbolic_rule||'F₆ = 1 / [(z₁−z₂)(z₁−z₆)(z₂−z₃)(z₃−z₄)(z₄−z₅)(z₅−z₆)]')}</pre><p>„Verbunden“ bedeutet der Koeffizient von t₁…tₙ in log Z mit Z = ⟨∏(1+tᵢJᵢ)⟩. Im Beispiel stimmen volle und verbundene Antwort überein. Bei anderen Eingaben können sie sich unterscheiden.</p></details>`,
    `<h5>So muss daraus die vollständige physische Lösung entstehen</h5><p>Der Quellkandidat verbindet jetzt die mathematischen Bausteine in einem Objekt: Ladungsgitter → Felder und Vakuum → Antworten, gemeinsame konforme Zeit und Rekursion. Der gesamte physische Anspruch verlangt, dass dieselbe Quelle auch alle beobachtbaren Antworten gemeinsam liefert.</p><div class="source-whole-bridge"><article><b>Bereits gemeinsam konstruiert</b><p>Originale 24 Felder → alle E₈-Ströme → ein Vakuumgesetz → gemeinsame Zeit → geladene Rekursion → verbundene Hypergraphantworten.</p></article><span aria-hidden="true">↓</span><article class="source-physical-obligation"><b>Eine zusammenhängende physische Abbildung</b><p>Aus derselben Quelle lokale Felder in 3+1 Dimensionen gewinnen und dabei Zustand, Produkte, Ladungen und Zeit erhalten.</p></article><span aria-hidden="true">↓</span><article><b>Ein gemeinsames Antwortfunktional W[J]</b><p>Materie und chirale Eichladungen · α und φ₀ · Flavor und CP · Clocks · räumliche Ausbreitung · Gravitation.</p></article></div><p class="source-program-equation">W₄ᴅ[j] an der Naht = W<sub>E₈,₁</sub>[j]</p><p>Diese Gleichheit betrifft alle markierten Feldantworten samt Zustand und Zeit. Schon die verbundene Sechserantwort aus dem vorigen Schritt muss darin wiederkehren. Die vorhandenen Existenzsätze für thermodynamische Dynamik der gewählten Hamiltonklasse bleiben gültig; sie ersetzen diesen gemeinsamen Anschluss nicht.</p><p>Die Rückkopplungen von P1/P2, Double Cover, μ₄ und α bleiben Bedingungen an diese eine Abbildung. Die optionale E₈-Skalenkaskade wird nicht vorausgesetzt. Die Grenzflächen-Determinante muss dabei aus demselben vierdimensionalen Operator stammen wie die übrigen Antworten.</p><p class="source-program-premise"><b>Der noch unbewiesene Gesamtschritt:</b> Die Originale und die hier berechnete Quellenregel liefern bisher keinen vollständigen Nachweis dieser physischen Abbildung. Der direkte Gitterweg verhindert aber, dass ein spezieller ungeklärter CAR-Kragen fälschlich die gesamte Lösungssuche blockiert.</p><details><summary>Die konkreten gemeinsamen Originalverpflichtungen</summary>${tourSourceLink({path:'tfpt_research_contracts.tex',line:13614,claim:'SEAM.DETLINE.UNIFICATION.01: derselbe Determinantenlinien-Anschluss'})}${tourSourceLink({path:'tfpt_research_contracts.tex',line:13664,claim:'FTRANSFER.GENERATING.01: ein gemeinsames physisches W[J]'})}<p>Die vollständige Regel ist ein festes Gesetz. Eine Rekodierung ihrer Darstellungen muss nicht alle unterscheidbaren Zustände auf einen einzigen Zustand zusammenmischen. Zukunftsvollständiger Zustandsraum, verlustfreie Rekodierung und attraktiver Zustand sind verschiedene Aussagen.</p></details>`
  ];
  root.innerHTML=`<p class="eyebrow">Die Teile greifen ineinander</p><h4>Ein Quellgesetz · mehrere Ansichten</h4><div class="source-program-nav" role="group" aria-label="Tour durch das gemeinsame Quellgesetz">${steps.map((label,i)=>`<button type="button" data-program-step="${i}" aria-pressed="${i===index}"><small>${i+1}</small>${label}</button>`).join('')}</div><section class="source-program-stage" aria-live="polite">${cards[index]}</section><div class="source-program-controls"><button type="button" data-program-prev ${index===0?'disabled':''}>← Zurück</button><span>${index+1} / ${steps.length}</span><button type="button" data-program-next ${index===steps.length-1?'disabled':''}>Weiter →</button></div>`;
  const move=i=>{app.sourceProgramStep=i;renderSourceProgram(root,data,unification);$(`[data-program-step="${i}"]`,root)?.focus({preventScroll:true});};
  $$('[data-program-step]',root).forEach(button=>button.addEventListener('click',()=>move(Number(button.dataset.programStep))));
  $('[data-program-prev]',root).addEventListener('click',()=>move(index-1));
  $('[data-program-next]',root).addEventListener('click',()=>move(index+1));
  const form=$('.source-word-form',root);
  if(form){
    const result=app.sourceProgramResult||data.example,fields=[];
    for(const kind of ['X','C'])for(let i=0;i<(kind==='X'?5:1);i++)for(let a=0;a<4;a++)for(const dagger of [false,true])fields.push({kind,...(kind==='X'?{i}:{}),a,dagger});
    const same=(a,b)=>a.kind===b.kind&&a.i===b.i&&a.a===b.a&&a.dagger===b.dagger;
    $('.source-word-inputs',form).innerHTML=result.word.map((field,i)=>`<label>Feld ${i+1}<select data-word-field="${i}" aria-label="Feld ${i+1}">${fields.map((option,j)=>`<option value="${j}" ${same(field,option)?'selected':''}>${escapeHTML(sourceFieldLabel(option))}</option>`).join('')}</select><input data-word-position="${i}" aria-label="Position von Feld ${i+1}" value="${escapeHTML(result.positions[i])}" maxlength="32" required></label>`).join('');
    const output=$('.source-word-result',form);
    output.textContent=`Volle Antwort: ${result.value_exact} · Verbundene Antwort: ${result.connected_value_exact}`;
    form.addEventListener('submit',async event=>{
      event.preventDefault();const button=$('button[type="submit"]',form);button.disabled=true;output.textContent='Die Quelle wird ausgewertet …';
      try{
        const response=await fetch('/api/source-word',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({word:$$('[data-word-field]',form).map(select=>fields[Number(select.value)]),positions:$$('[data-word-position]',form).map(input=>input.value.trim())})});
        const calculated=await response.json();if(!response.ok)throw new Error(calculated.error||'Auswertung fehlgeschlagen');
        app.sourceProgramResult=calculated;$('[data-live-source-graph]',root).innerHTML=sourceHypergraphSVG(calculated);output.textContent=`Volle Antwort: ${calculated.value_exact} · Verbundene Antwort: ${calculated.connected_value_exact}`;
      }catch(error){output.textContent=error.message;}finally{button.disabled=false;}
    });
  }
}

function renderJointChargedSource(root,data) {
  if(!root||!data?.dimensions)return;
  const dims=data.dimensions,values=data.native_charge?.values||[],closure=data.algebra?.original24_closure;
  const focus=app.jointSourceFocus||'both';
  root.innerHTML=`<p class="eyebrow">Der gemeinsame Ansatzpunkt</p><h4>Eine Quelle verbindet die gesamte Operatorstruktur</h4><p>Die vorhandene E₈-Quelle enthält ${dims.charged_currents} Felder X(i,a). Jedes trägt zugleich einen Fünferindex in der konjugierten Darstellung und einen Viererindex. Zusammen mit den vier ursprünglichen C-Feldern und ihren Gegenfeldern erzeugen sie alle 248 Richtungen der Quelle. Ihre tatsächlichen Operatorprodukte verbinden beide Wirkungen und die P2-Ladung.</p><div class="composition-switch" role="group" aria-label="Gemeinsame geladene Quellenwirkung"><button type="button" data-source-focus="charge" aria-pressed="${focus==='charge'}">P2-Ladung</button><button type="button" data-source-focus="register" aria-pressed="${focus==='register'}">Viererwirkung</button><button type="button" data-source-focus="both" aria-pressed="${focus==='both'}">Gemeinsame Quelle</button></div><div class="joint-source-grid ${focus}" role="img" aria-label="Zwanzig geladene Quellenfelder in fünf Zeilen und vier Spalten. Interne Indizes, kein räumliches Gitter."><span></span>${Array.from({length:dims.register},(_,a)=>`<b>Viererindex ${a+1}</b>`).join('')}${Array.from({length:dims.carrier},(_,i)=>`<strong class="${i<3?'color-charge':'weak-charge'}">i = ${i+1}<small>Y = ${escapeHTML(values[i]||'')}</small></strong>${Array.from({length:dims.register},(_,a)=>`<span class="source-field ${i<3?'color-charge':'weak-charge'}" data-register="${a}">X<sub>${i+1},${a+1}</sub></span>`).join('')}`).join('')}${closure?`<strong>Zusatz C<small>Y = 0</small></strong>${Array.from({length:dims.register},(_,a)=>`<span class="source-field neutral-source">C<sub>${a+1}</sub></span>`).join('')}`:''}</div>${closure?'<p class="source-graph-equation">24 ursprüngliche Felder + Gegenfelder → alle 240 Wurzelströme + 8 Cartanrichtungen</p>':''}<p class="joint-source-basis">Die Tabelle zeigt die Eigenladungen im diagonalen Wurzelrahmen. Für die ursprünglichen Ereignisse wird dieselbe Ladung in deren Prozessrahmen umgerechnet; dort ist ihre Matrix nicht diagonal. Beide Wirkungen sind im Code miteinander verknüpft.</p><p class="joint-source-reading" aria-live="polite">${focus==='charge'?'Die Ladung unterscheidet die drei und zwei Fünferrichtungen. Sie wirkt auf denselben geladenen Feldern für jeden Viererindex. Ihr Generator wird aus den vorhandenen Stromklammern berechnet.':focus==='register'?'Die Viererwirkung verändert den zweiten Index derselben Felder. Sie ist im gemeinsamen Quellenraum vorhanden; diese vier internen Richtungen sind keine vier Raumzeitachsen.':'Beide Wirkungen treffen dieselben Felder. Die X-Felder und ihre Gegenfelder erzeugen die 80-dimensionale A₈-Unteralgebra. Zusammen mit den vier ursprünglichen C-Feldern und ihren Gegenfeldern entstehen alle 248 E₈-Richtungen aus den tatsächlichen Klammern.'}</p><p><b>Die gemeinsame Ereigniswirkung behält ihre Phase:</b> Zwei gleiche ursprüngliche Ereignisse wirken auf den beiden reduzierten Operatoranzeigen identisch. Auf den geladenen X-Feldern bleibt dagegen der Faktor −i. Diese Information gehört zur vollständigen Quellenwirkung.</p><p>Von den ${data.native_events.event_count} ursprünglichen Transporten erhalten ${data.native_charge.fixed_charge_preserving_source_events} die festgehaltene P2-Ladung. Die übrigen transportieren ihren Bezugsrahmen kovariant; sie sind damit noch keine selbstständigen ladungserhaltenden physischen Updates.</p><div class="joint-source-whole"><article><b>Ursprung und Markierung</b><p>P1/P2, Double Cover und μ₄ legen die geprüften diskreten Verträge fest. Der direkte Gitterweg konstruiert eine lokale Quelle; ihre physische Herkunftsidentifikation ist weiter herzuleiten.</p></article><article><b>Ein vollständiger Prozess</b><p>Ein gemeinsamer Zustand bewertet ganze geladene Feldgeschichten. Korrelation, Ereigniswirkung, Rekursion und Zeit stammen aus demselben Objekt. Im lokalen positiven Vakuumrahmen legt der vollständige Generatoranschluss den Zustand mit fest.</p></article><article><b>Gemeinsame physische Antworten</b><p>Die abgeleitete lokale Theorie muss daraus Clocks, Ladungen, α, Flavor, räumliche Ausbreitung und Gravitation zugleich liefern. Separate passende Formeln schließen diesen Schritt nicht.</p></article></div><p><b>Der positive Zeitanschluss:</b> Im gewählten lokalen E₈-Vakuumnetz werden die geometrischen Zeitflüsse durch Netz und Zustand bestimmt. Die ursprüngliche Viertelrotation entsteht als Produkt zweier modularer Spiegelungen an den markierten Schnitten. Das ist ein bedingter Anschluss an dieselbe Quelle; die reduzierte Clock-Matrix benötigt zusätzlich ihre aus der Quelle begründete Auslese.</p><p><b>Warum damit noch keine Gesamtlösung bewiesen ist:</b> Die fehlende Abbildung muss lokale Operatoren, ihren Zustand, alle geladenen Antworten und die Zeit gemeinsam erhalten. Eine Zuordnung nur gleicher Matrizen oder Dimensionen reicht nicht. Die physische 3+1-dimensionale Theorie ist ebenfalls noch nicht aus diesem Randnetz rekonstruiert.</p><details><summary>Was exakt gerechnet wird und welche Identifikationen getrennt bleiben</summary><p>Alle verschachtelten Klammern [[X(i,a),X†(j,b)],X(k,c)] ergeben δ(a,b)δ(j,k)X(i,c) + δ(i,j)δ(b,c)X(k,a). Daraus entstehen die SU(5)- und SU(4)-Generatoren im selben E₈. Die P2-Ladung Qᵧ = −¼ Σᵢₐ yᵢ[X(i,a),X†(i,a)] erfüllt [Qᵧ,X(k,c)] = −yₖX(k,c). Dabei sind yᵢ = (−1/3,−1/3,−1/3,+1/2,+1/2) die fundamentalen P2-Werte; X trägt die konjugierten Ladungen. Seine Gegenfelder tragen die umgekehrten Ladungen.</p><p>Der bereits vorhandene gemeinsame geladene Lift ist von der separaten Cartan-Gitterhebung zu unterscheiden. Auch die neutralen Quartikzustände aus vier Cartan-Strommoden sind keine geladenen P2-Fundamentalzustände. Die Matrix oben zeigt interne Feldkomponenten und kein räumliches Netz. Für einen beliebigen P2-Rahmen gilt Q(Y) = −ΣᵢⱼYᵢⱼSⱼᵢ und damit die Wirkung −Yᵀ ⊗ I₄ auf X. Dieser Basisübergang wird an allen ursprünglichen Strömen geprüft.</p>${tourSourceLink({path:'tfpt_explorer/current_block_geometry.py',line:1,claim:'Originale E₈-Klammern und gemeinsame geladene Quelle'})}<a href="https://arxiv.org/pdf/1503.01260" target="_blank" rel="noopener">Lokales Vakuumnetz und modulare Geometrie: Carpi et al., Abschnitt 3</a></details>`;
  const reconstruction=data.local_reconstruction;
  if(reconstruction){
    const section=document.createElement('section');section.className='source-local-reconstruction';
    section.innerHTML=`<h5>${escapeHTML(reconstruction.title)}</h5><div class="source-reconstruction-chain" role="img" aria-label="Bedingte Rekonstruktion: ursprüngliche lokale Felder und vollständige Stromrelationen mit zyklischem Vakuum bestimmen alle Korrelationen, den Hilbertraum und die geometrische Zeit"><span>Ursprüngliche lokale Felder<br><small>mit vollständigen Stromrelationen + zyklischem Vakuum</small></span><b aria-hidden="true">→</b><span>Alle Korrelationen<br>+ Hilbertraum<br>+ geometrische Zeit</span></div><p>${escapeHTML(reconstruction.consequence)}</p><p><b>Ein gemeinsamer Nachweis:</b> ${escapeHTML(reconstruction.first_missing)}</p><details><summary>Präzise Voraussetzungen des bedingten Rekonstruktionssatzes</summary><ol>${reconstruction.premises.map(text=>`<li>${escapeHTML(text)}</li>`).join('')}</ol><p>${escapeHTML(reconstruction.bulk_scope)}</p>${tourSourceLink({path:'articles/2026-08-30/mmst_charged_scaling_limit_en.tex',line:1847,claim:'CAR-Skalierungsweg: zusätzliche lokale Vollständigkeit FE-GEN / ALG-EXH'})}${tourSourceLink({path:'experiments/lean4-carrier-rigidity/TfptCarrier/SeamScalingLimit.lean',line:63,claim:'Lean: Skalierungs- und E₈-Anschluss als explizite Annahmen'})}${tourSourceLink({path:'tfpt_research_contracts.tex',line:13663,claim:'Eine gemeinsame physische Erzeugungsfunktion für alle Transferantworten'})}<a href="${escapeHTML(reconstruction.source)}" target="_blank" rel="noopener">${escapeHTML(reconstruction.source_detail)}</a></details>`;
    $('.joint-source-whole',root).before(section);
  }
  $$('[data-source-focus]',root).forEach(button=>button.addEventListener('click',()=>{app.jointSourceFocus=button.dataset.sourceFocus;renderJointChargedSource(root,data);$(`[data-source-focus="${app.jointSourceFocus}"]`,root).focus({preventScroll:true});}));
}

function flavorPathSVG(data,step) {
  const side=step%2,activeP=step>0&&side===1,activeQ=step>0&&side===0;
  const port=(x,index,label,value)=>`<g class="flavor-port ${side===index?'is-active':''}"><rect x="${x-96}" y="115" width="192" height="90" rx="16"/><text x="${x}" y="138" text-anchor="middle">${label} · z = ${escapeHTML(value)}</text>${[-36,0,36].map((dx,i)=>`<circle cx="${x+dx}" cy="162" r="9" fill="${['#297565','#7160a5','#a96508'][i]}"/>`).join('')}<text x="${x}" y="191" text-anchor="middle">drei Familienkomponenten</text></g>`;
  return `<svg viewBox="0 0 900 310" role="img" aria-label="Zwei Zugänge mit je drei Komponenten. Der untere Weg P führt von A nach B, der obere Weg Q zurück. Beide umfassen die ursprüngliche Marke plus eins."><defs><marker id="flavor-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs><path class="flavor-arc ${activeP?'is-active':''}" d="M170 205 C200 297 700 297 730 205"/><path class="flavor-arc ${activeQ?'is-active':''}" d="M730 115 C700 23 200 23 170 115"/><text class="flavor-arc-label" x="450" y="46" text-anchor="middle">Q · oberer Rückweg</text><text class="flavor-arc-label" x="450" y="290" text-anchor="middle">P · unterer Hinweg</text><circle cx="357" cy="160" r="8" fill="#a96508"/><text x="450" y="153" text-anchor="middle">Marke +1</text><text x="450" y="179" text-anchor="middle">ein Umlauf: QP = M</text>${port(170,0,'Zugang A',data.paths.basepoint)}${port(730,1,'Zugang B',data.paths.reflected_basepoint)}</svg>`;
}

function neutralSourceResponseMarkup(data) {
  if(!data?.neutral_operator)return '';
  const norm=data.neutral_operator.norms_squared.R,weight=data.source_state.L0_weight,defect=data.defect_state_contrast,joint=data.joint_flavor_response;
  const shared=joint?`<section class="flavor-joint-response"><h6>Der Flavorprozess antwortet auf dieses neutrale Feld</h6><p>${escapeHTML(joint.physical_meaning)}</p><p class="source-graph-equation">Doppelpol-Koeffizient an jeder der vier Nahtmarken: <b>${escapeHTML(joint.local_double_poles[0])}</b></p><p>Das ist eine gemeinsame berechnete Quellenantwort, keine zusätzliche angepasste Zahl. Der dimensionslose Koeffizient ist weder α noch eine bereits bestimmte physische Amplitude.</p><details><summary>Vollständige Antwort aus der originalen Verbindung</summary><code>${escapeHTML(joint.formula)}</code><p>Die Ward-Identität lautet ${escapeHTML(joint.ward_identity)}. Die Antwort enthält alle vier Flavor-Defekte und den zugehörigen geladenen Ausgangszustand; sie ist keine reine Vakuumantwort. R ist eine Differenz von Spannungsfeldern und kein positiver Energieoperator.</p></details></section>`:'';
  return `<section class="flavor-source-response"><p class="eyebrow">Anschluss an denselben Quellkandidaten</p><h6>Was die neutrale Antwort bereits liefert</h6><p>Die ursprünglichen 48 ausgewählten Spinorfelder ergeben im E₈-Vakuum einen konkreten neutralen Zustand R. Seine Norm ist berechnet, sein Gewicht bestimmt die konforme Dämpfung.</p><div class="flavor-evidence"><div><span>Normquadrat von R</span><strong>${escapeHTML(norm)}</strong></div><div><span>Konformes Gewicht</span><strong>${escapeHTML(weight)}</strong></div><div><span>Quellenidentität</span><strong>R = 4T<sub>A₂</sub> − 8T<sub>U₁</sub></strong></div></div>${shared}<h6>Der verbleibende Anschluss an die α-Naht</h6><p class="source-graph-equation">${escapeHTML(data.conditional_port.result)}</p><p><span class="tour-status conditional">bedingt</span> Diese vollständige endliche Antwort folgt, wenn die ursprüngliche Naht gerade über V = c₃²|R⟩⟨p₀| einkoppelt und mit exp(−αL₀) propagiert. Die Auswahl dieses Ports aus dem ursprünglichen Nahtoperator ist dadurch noch nicht bewiesen.</p>${defect?`<details><summary>Warum der Zustand beim gemeinsamen Anschluss mitgeführt wird</summary><p>Im separat geprüften lokalen Defektsektor beträgt das Normquadrat ${escapeHTML(defect.norm_squared)}; der Erwartungswert von R₀ ist ${escapeHTML(defect.R0_mean)}. Die Vakuumzahl 48 darf daher nicht unverändert in eine andere Präparation übernommen werden. Dieser lokale Höchstgewichtstest ist noch nicht der volle Zustand mit vier Defekten.</p><p>Der endliche Zustandsport ist außerdem nicht das lokale Feld R(z): Dessen verbundene Dreipunktantwort ist ungleich null. Die Rang-eins-Determinante allein bestimmt diese lokalen Mehrpunktantworten nicht.</p>${tourSourceLink({path:'tfpt_explorer/neutral_source_response.py',line:1,claim:'Native Wurzeln, neutraler Zustand und bedingter Nahtport'})}</details>`:''}</section>`;
}

function sourceSpinLiftMarkup(data) {
  if(!data?.fuchs_lift||!data?.root_characters)return '';
  const lift=data.fuchs_lift,characters=data.root_characters,spinCharge=data.spin_charge_scope;
  const sign=lift.checks.relative_spin_sign?'−':'?',closed=lift.checks.cube_is_family_centre&&lift.checks.sixth_power_identity;
  return `<section class="flavor-source-response flavor-spin-lift"><p class="eyebrow">Vom Familienweg zur geladenen Quelle</p><h6>Der Weg hinterlässt ein Vorzeichen</h6><p>Die Einheitswindung bleibt beim Übergang zur Spinordarstellung erhalten. Dadurch wirkt derselbe Familienumlauf mit einem überprüfbaren Vorzeichen auf der E₈-Quelle.</p><div class="flavor-derivation"><article><b>1 · Einmal herum</b><p>Die Phase der originalen Determinante läuft einmal um den Kreis.</p><code>Windung: ${fmt(lift.measured_winding,8)}</code></article><article><b>2 · Das Vorzeichen bleibt</b><p>Der Spinlift merkt sich diesen Umlauf: Er erhält ein Minuszeichen gegenüber dem Lift ohne diese Windung.</p><code>${escapeHTML(sign)} · Λ<sup>even</sup>(M)</code></article><article><b>3 · Auf der ganzen Quelle</b><p>Nach drei Familienumläufen wirkt die Deckung η: ${escapeHTML(characters.even_with_Cartan)} Stromrichtungen bleiben gleich, ${escapeHTML(characters.odd_roots)} wechseln das Vorzeichen.</p><code>+${escapeHTML(characters.even_with_Cartan)} &nbsp; / &nbsp; −${escapeHTML(characters.odd_roots)}</code></article></div><p class="source-graph-equation">${closed?'g³ = η; g⁶ = I':'Abschlussprüfung nicht erfüllt'}</p><p>Nach sechs Familienumläufen ist die vollständige Quellenwirkung wieder die Identität. Hier zählt g einen <b>ganzen Umlauf</b>, keinen der Halbwege oben.</p><p class="flavor-path-scope">Das ist ein berechneter interner Spinlift. Die betroffenen E₈-Felder sind bosonische Ströme; ihr Deckvorzeichen leitet keine physische Fermionstatistik her. Der Spinlift g ist auch nicht automatisch der oben dargestellte Zweifaseroperator U₆.</p><details><summary>Was die zusätzliche Spin-Ladungsforderung ändern würde</summary><p>Das zusätzliche Postulat <code>${escapeHTML(spinCharge?.new_postulate||'')}</code> verlangt eine bestimmte Verbindung von innerer Ladung und physischer Fermionparität. Das skalare 16̄<sub>H</sub> der bestehenden Majorana-Route erfüllt sie nicht: Sein inneres Vorzeichen ist −1, seine skalare Drehwirkung +1.</p><p>Mit der gewöhnlichen internen ℤ₄-Symmetrie bleibt die ursprüngliche Route zulässig. Der Konflikt entsteht erst durch diese zusätzliche Gleichsetzung.</p><p>Die Windung wird am Originalpfad integriert; Lift, Deckwirkung und Abschluss werden exakt an den ursprünglichen Matrizen und Wurzeln geprüft.</p>${tourSourceLink({path:'tfpt_explorer/source_spin_lift.py',line:1,claim:'Berechneter Familien-Spinlift und vollständiger Deckcharakter'})}${tourSourceLink({path:'verification/v117_monodromy_weyl_a3.py',line:54,claim:'Originale Familienmonodromie'})}${tourSourceLink({path:'verification/v488_majorana_clebsch_door.py',line:9,claim:'Ursprüngliche skalare Spinor-Higgs-Route'})}</details></section>`;
}

function sourceMajoranaPairsMarkup(data) {
  if(!data?.grade_two||!data?.grade_three||!data?.grade_four)return '';
  const third=data.grade_three.highest_weight,fourth=data.grade_four.highest_weight;
  const firstIsNull=data.grade_two.pair_norms.every(row=>row.every(value=>Number(value)===0));
  const pairTransport=data.family_transport?.checks?.pair_M_intertwining===true;
  const neutralPairs=data.joint_neutral_pair?.symmetric_retained_six||[],response=neutralPairs[0]?.R0_eigenvalue;
  const neutralVerified=neutralPairs.length===6&&neutralPairs.every(row=>row.eigenvector_checked&&row.R0_eigenvalue===response);
  const jointResponse=(pairTransport?'<p>Der berechnete Paartransport stimmt nach dem ausgewiesenen Basiswechsel mit dem ursprünglichen diskreten Familienweg überein.</p>':'')+(neutralVerified?`<p>Derselbe neutrale Alpha-Kandidat antwortet auf die normierten symmetrischen Paare im ausgewählten Dreieranteil mit <b>${escapeHTML(response)}/z²</b>. Das ist eine feste Quellenantwort; sie bestimmt noch keine physische Massenskala.</p>`:'');
  const sourceCoupling=data.native_three_point?.grade4_126x10?.coefficient;

  return `<section class="flavor-source-response flavor-majorana-pairs"><p class="eyebrow">Ein weiterer Anschluss innerhalb derselben Quelle</p><h6>Die Quelle enthält ein passendes geladenes Paar</h6><p>Das einfachste Produkt der ursprünglichen geladenen C-Felder verschwindet. Auf höheren Anregungsstufen entstehen jedoch konkrete Paaroperatoren.</p><div class="flavor-derivation"><article><b>Gewicht 2 · C-Singletpaar noch null</b><p>Die unmittelbare Paarung dieser C-Felder ist exakt null; andere geladene Paarkanäle sind schon auf dieser Stufe vorhanden.</p><code>:C<sub>a</sub>C<sub>b</sub>: ${firstIsNull?'= 0':'· Nullprüfung nicht erfüllt'}</code></article><article><b>Gewicht ${escapeHTML(third.chiral_weight)} · antisymmetrisch</b><p>Die erste nichtverschwindende Stufe trägt ${escapeHTML(data.grade_three.family_pairs.length)} Familienpaare. Beim Vertauschen der beiden Familienplätze wechselt ihr Vorzeichen.</p><code>${escapeHTML(third.D5_dimension)} × ${escapeHTML(third.A3_dimension)}</code></article><article><b>Gewicht ${escapeHTML(fourth.chiral_weight)} · symmetrisch</b><p>Jetzt existiert auch der symmetrische Paarkanal mit ${escapeHTML(data.grade_four.family_pairs.length)} Familienkomponenten.</p><code>${escapeHTML(fourth.D5_dimension)} × ${escapeHTML(fourth.A3_dimension)}</code></article></div><p>Die innere ℤ₄-Ladung dieses Paars ist <b>${escapeHTML(data.charge_and_statistics.Z4_charge)}</b>. Die passende geladene Zusammensetzung ist damit in der vollständigen Quelle vorhanden.</p>${jointResponse}<p class="flavor-path-scope"><b>Gewicht bedeutet hier chirale Anregungsstufe.</b> Es ist keine vierdimensionale Massendimension. Für die physische Majorana-Masse muss der vorhandene Higgs-/Masseneinsatz samt seiner Skala an diesen Quellenkanal angeschlossen werden. Eine geladene Einsetzung oder ein insgesamt neutraler höherer Korrelator kann diesen Anschluss tragen.</p><details><summary>Berechnung und Bezug zur ursprünglichen Paarroute</summary><p>Die Rechnung verwendet die ursprünglichen Strommoden, ihre Phasen und die positive Vakuumform.${sourceCoupling!=null?` Der normierte Drei-Punkt-Koeffizient des symmetrischen Quellenpaars ist bereits fest berechnet: ${escapeHTML(sourceCoupling)}.`:''} Der symmetrische Kanal ist eine zusammengesetzte Quellenanregung; seine Existenz allein ersetzt die bisherige effektive Majorana-Kopplung noch nicht.</p>${tourSourceLink({path:'tfpt_explorer/source_majorana_pairs.py',line:1,claim:'Exakte Nullstufe und vorhandene antisymmetrische und symmetrische Paare'})}${tourSourceLink({path:'verification/v488_majorana_clebsch_door.py',line:9,claim:'Ursprüngliche Majorana-Paarroute und ihr Gewicht-1-Träger'})}</details></section>`;
}

function renderFlavorPathTransport(root,data,neutral,spinLift,majoranaPairs) {
  if(!root||!data?.ode)return;
  const step=Math.max(0,Math.min(6,Number(app.flavorPathStep)||0));app.flavorPathStep=step;
  const turns=Math.floor(step/2),power=['v','Mv','M²v','v'][turns],state=step%2?`P${turns?'('+power+')':'v'}`:power;
  const explanation=[
    'Start an Zugang A: Ein beliebiger dreikomponentiger Familienzustand v liegt bereit.',
    'Der untere Halbweg transportiert denselben Zustand nach B. Seine drei Komponenten bleiben gemeinsam erhalten.',
    'Zurück an A: Ein ganzer Umlauf ist abgeschlossen. Der Zustand lautet jetzt Mv; der Familienzustand ist im Allgemeinen noch verändert.',
    'Der nächste Halbweg erreicht wieder B. Drei Wegschritte sind noch keine Rückkehr des ganzen Zustands.',
    'Nach zwei ganzen Umläufen liegt M²v an A. Die verbleibende Familienwirkung wird weiter mitgeführt.',
    'Der fünfte Halbweg erreicht B. Auch jetzt wurde keine neue Quelle eingesetzt.',
    'Nach drei ganzen Umläufen ist jeder Ausgangszustand zurück: M³ = I und T⁶ = I.'
  ][step];
  const errors=data.ode.errors,character=data.ode.determinant_character,num=value=>Number.isFinite(Number(value))?Number(value).toExponential(2):'–';
  root.innerHTML=`<p class="eyebrow">Originaler Umlauf → ursprünglicher Flavoroperator</p><h5>Vom ursprünglichen Umlauf zum Flavoroperator</h5><p>Die originale Fuchsverbindung transportiert drei Familienkomponenten um die vier Nahtmarken. Zwei Zugänge derselben Verbindung reichen aus, um den bisher endlichen Sechseroperator als wirklichen Wegtransport zu realisieren.</p><div class="flavor-path-picture">${flavorPathSVG(data,step)}</div><div class="composition-switch flavor-step-controls" role="group" aria-label="Anzahl durchlaufener Halbwege">${Array.from({length:7},(_,n)=>`<button type="button" data-flavor-step="${n}" aria-pressed="${step===n}" aria-label="${n} Halbwege">${n}</button>`).join('')}<button type="button" data-flavor-next>${step===6?'Zurück zum Start':'Nächster Halbweg →'}</button></div><div class="flavor-step-reading" aria-live="polite"><strong>${step} / 6 · Zugang ${step%2?'B':'A'} · ${escapeHTML(state)}</strong><p>${explanation}</p></div><small>Die Zeichnung erklärt den berechneten Wegoperator. Die Schritte zählen Halbwege, keine physische Zeit; die drei Punkte stehen für interne Komponenten.</small><div class="flavor-derivation"><article><b>1 · Dieselbe Verbindung</b><p>Unterer Weg P und oberer Weg Q ergeben den ursprünglichen Familienumlauf M.</p><code>QP = M; M³ = I</code></article><article><b>2 · Zwei Zugänge</b><p>Der Wegoperator T wechselt zwischen den beiden Dreierfasern. Sechs Schritte schließen den Umlauf.</p><small>Im parallelen Rahmen:</small><br><code>T² = M ⊕ M; T⁶ = I</code></article><article><b>3 · Der alte Flavoroperator</b><p>Ein exakter unitärer Basiswechsel liefert die originale Clock und den ganzen endlichen Antwortkern.</p><code>J†T⁻¹J = M ⊕ (−M) = U₆</code></article></div><div class="flavor-evidence"><div><span>Berechnete Determinantenwindung</span><strong>${fmt(character.integrated_phase_winding,10)}</strong></div><div><span>Fehler des Familienabschlusses M³ = I</span><strong>${num(errors.monodromy_cube)}</strong></div><div><span>Fehler der Rückkehr T⁶ = I</span><strong>${num(errors.path_period_six)}</strong></div></div><p>Die Determinante der bei z = 0 normierten Lösung derselben Originalverbindung ist <b>1 − z⁴</b>. Ihre Phase windet sich hier genau einmal: derselbe ganzzahlige Windungstyp wie P1. Aus der Clock folgt zugleich <b>D = yI − δU₆</b> samt vollständigem endlichem Greenkernel und Determinante <b>y⁶ − δ⁶</b>.</p><p class="flavor-path-scope"><b>Was damit verbunden ist:</b> der tatsächliche ursprüngliche Umlauf und alle sechs Richtungen des endlichen Flavoroperators. Der vollständige P1-Nahtoperator, die Auswahl genau dieses Weges und die physische Zeit sind damit noch nicht identifiziert. Der folgende Spinlift zeigt, wie die Windung auf den geladenen Quellenfeldern erhalten bleibt.</p><details><summary>Rechnung, Rahmen und Originalstellen</summary><p>Beide Halbwege und ein unabhängiger Vollkreis werden an der originalen Verbindung numerisch integriert. Unterschied der Ergebnisse: ${num(errors.composition_vs_full_circle)}; Rückwärtsumlauf gegen inversen Vorwärtsumlauf: ${num(data.ode.orientation_reversal_error)}. Prüftoleranz: ${num(data.ode.check_tolerance)}.</p><p>${escapeHTML(data.ode.metric)}</p><p>Im exakt unitären Rahmen werden der gesamte positive Operator D†D, der regulierte Greenkernel und seine inverse Quadratwurzel transportiert. Greenkernel-Restfehler: ${num(data.kernels.errors.Green_conjugacy)}. Das ist keine Kompression eines unendlichen Quellraums.</p><p>${escapeHTML(data.paths.basepoint_scope)}</p>${tourSourceLink({path:'verification/v117_monodromy_weyl_a3.py',line:54,claim:'Originale Fuchsverbindung und Familienmonodromie'})}${tourSourceLink({path:'verification/v118_hexagon_family_dictionary.py',line:10,claim:'Ursprüngliche Sechserclock und Flavoroperator'})}${tourSourceLink({path:'tfpt_explorer/flavor_path_transport.py',line:1,claim:'Ausgeführte Wege, vollständiger Intertwiner und numerische Toleranzen'})}</details>${sourceSpinLiftMarkup(spinLift)}${sourceMajoranaPairsMarkup(majoranaPairs)}${neutralSourceResponseMarkup(neutral)}`;
  $$('[data-flavor-step]',root).forEach(button=>button.addEventListener('click',()=>{app.flavorPathStep=Number(button.dataset.flavorStep);renderFlavorPathTransport(root,data,neutral,spinLift,majoranaPairs);$(`[data-flavor-step="${app.flavorPathStep}"]`,root).focus({preventScroll:true});}));
  $('[data-flavor-next]',root).addEventListener('click',()=>{app.flavorPathStep=(step+1)%7;renderFlavorPathTransport(root,data,neutral,spinLift,majoranaPairs);$('[data-flavor-next]',root).focus({preventScroll:true});});
}

function renderJointNeutrinoPhase(root, data) {
  if(!root||!data?.majorana_phase?.examples?.length)return;
  const rows=data.majorana_phase.examples;
  const index=Math.max(0,Math.min(rows.length-1,app.neutrinoPhaseIndex||0)),row=rows[index];
  const ratio=row.response_ratio, magnitude=Math.hypot(...ratio);
  const x=95+62*ratio[0]/magnitude,y=90-62*ratio[1]/magnitude;
  root.innerHTML=`<h6>Was eine unsichtbare Phase verändert</h6><p>Die beiden Massen bleiben gleich. Ihre relative Phase verändert aber eine gemeinsame Antwort. Die drei Beispiele stammen aus der berechneten, ausdrücklich phasenoffenen Neutrinofamilie.</p><div class="composition-switch" role="group" aria-label="Berechnete Majoranaphase">${rows.map((value,i)=>`<button type="button" data-neutrino-phase="${i}" aria-pressed="${index===i}">${Math.round(value.gamma*180/Math.PI)}°</button>`).join('')}</div><div class="flavor-derivation" aria-live="polite"><article><svg viewBox="0 0 270 180" role="img" aria-label="Relative komplexe Paarantwort bei ${Math.round(row.gamma*180/Math.PI)} Grad"><circle cx="95" cy="90" r="62" fill="none" stroke="#b2c5ce" stroke-width="2"/><line x1="21" y1="90" x2="169" y2="90" stroke="#b2c5ce"/><line x1="95" y1="16" x2="95" y2="164" stroke="#b2c5ce"/><line x1="95" y1="90" x2="${x}" y2="${y}" stroke="#087f8c" stroke-width="4"/><circle cx="${x}" cy="${y}" r="6" fill="#087f8c"/><text x="177" y="95" font-size="12" fill="#16324f">gleiche Phase</text></svg><small>Der Zeiger zeigt die Phase von A₂/A₃. Er ist keine räumliche Bahn; seine Länge ist zur Orientierung normiert.</small></article><article><b>Gleiche Masse, andere Interferenz</b><p>m₂ = ${fmt(data.joint_neutrino_input.m2_eV,8)} eV<br>m₃ = ${fmt(data.joint_neutrino_input.m3_eV,8)} eV</p><p>Berechneter Betrag mββ:<br><strong>${fmt(row.m_bb_eV,8)} eV</strong></p><small>Das ist eine Ausgabe der erklärten bedingten Matrixfamilie, kein gemessener Wert. Der vollständige gedruckte Ansatz setzt dagegen bereits einen bestimmten Phasenwert. Die leichte Matrix wird hier als Familientensor ausgelesen; sie wird nicht mit dem geladenen schweren Paarfeld gleichgesetzt.</small></article></div>`;
  $$('[data-neutrino-phase]',root).forEach(button=>button.addEventListener('click',()=>{
    app.neutrinoPhaseIndex=Number(button.dataset.neutrinoPhase);
    renderJointNeutrinoPhase(root,data);
    $(`[data-neutrino-phase="${app.neutrinoPhaseIndex}"]`,root).focus({preventScroll:true});
  }));
}

function jointPhysicalDictionaryMarkup(data) {
  const charge=data.source_charge_response,neutrino=data.source_neutrino_dictionary,correlation=data.source_flavor_correlator;
  if(!charge||!neutrino||!correlation)return '';
  return `<section class="flavor-source-response" id="gemeinsames-woerterbuch"><p class="eyebrow">Was die Anschlüsse gemeinsam bedeuten</p><h5>Ein Instrument – mehrere genau berechnete Antworten</h5><p>Die vorhandenen Massen-, Flavor- und α-Herleitungen sind die Zielvorgaben. Jetzt ist genauer berechnet, wie ihre verschiedenen Antworten innerhalb derselben Quelle zusammenpassen.</p><div class="flavor-derivation"><article><b>1 · Dieselben Materiefelder</b><p>Die 48 zählt die ausgewählten Felder. Für die Eichantwort werden ihre tatsächlichen Ladungen mitgerechnet: Die Ladungsquadrate ergeben ${escapeHTML(charge.physical_beta.fermion_charge_trace)}. Zusammen mit dem erklärten Higgsinhalt entsteht der bekannte Faktor ${escapeHTML(charge.physical_beta.b1)}.</p></article><article><b>2 · Die ganze Neutrinomatrix</b><p>Der schwere Majorana-Kanal besitzt ein genaues Wörterbuch für seine vollständige Massentabelle. Die leichte Neutrinomatrix entsteht über die vorhandene Seesaw-Regel. Sechs kohärente Quellenantworten lesen einen symmetrischen Familientensor einschließlich seiner Phasen vollständig wieder aus.</p></article><article><b>3 · Eine gemeinsame Antwort</b><p>Der ursprüngliche Familienhintergrund verändert auch die neutrale Zweipunktantwort. Dieser Zusatz ist exakt berechnet und benötigt für neutrale Einsetzungen keinen zusätzlich gewählten Weg. Die Quelle darf deshalb nicht bei jedem Ausgabekanal unbemerkt auf einen anderen Vakuumzustand zurückgesetzt werden.</p></article></div><div class="joint-neutrino-phase"></div><h6>Was entscheidet jetzt über die Gesamtlösung?</h6><p>Die Übersetzung einer eingesetzten Massentabelle ist berechnet. Noch zu bestimmen ist, warum der ursprüngliche Prozess gerade diesen Zustand und diese Nahtkopplung erzeugt und wie seine geladenen Defekte zu lokalen Teilchen unserer Raumzeit werden. Dieselbe Regel muss alle drei Antworten gleichzeitig liefern.</p><p class="source-graph-equation">Quelle → ausgewählter Zustand und gemeinsame Kopplung → Massen + Flavor + α</p><details><summary>Die konkrete Verbindung statt bloßer Zahlenähnlichkeit</summary><p>Die zwei neutralen Zustände haben die Gram-Matrix [[48, 10], [10, 35/3]] mit Determinante ${escapeHTML(charge.gram_determinant)}. Sie stammen aus derselben Quelle, bleiben aber unterscheidbar. Auf allen sechs behaltenen Neutrinopaaren wirken sie mit 4 beziehungsweise ${escapeHTML(charge.neutrino_pair_ward.coefficient)}. Beide Antworten erhalten die gesamte Massentabelle, wählen ihre relative Majoranaphase aber noch nicht aus.</p><p>Die Paaroperatoren besitzen inzwischen auch eine explizite Darstellung als gerade Produkte der ursprünglichen CAR-Felder. Die einzelnen Materiefelder bleiben dabei sektorwechselnde Defektfelder; ihre vierdimensionale Fermionstatistik ist eine eigene zu erhaltende Verbindung.</p>${tourSourceLink({path:'tfpt_explorer/source_neutrino_dictionary.py',line:1,claim:'Norm- und phasentreue Übersetzung der Neutrinomatrix'})}${tourSourceLink({path:'tfpt_explorer/source_flavor_correlator.py',line:1,claim:'Gemeinsame neutrale Antwort im ursprünglichen Flavor-Hintergrund'})}${tourSourceLink({path:'tfpt_explorer/source_charge_response.py',line:1,claim:'Tatsächliche Eichladungen und gemeinsamer Paar-Wardanschluss'})}</details></section>`;
}

function renderJointSelection(root,data) {
  if(!root||!data)return;
  const cartan=data.cartan||{},joint=data.trimer||{},carriers=joint.minimal_reachable_carriers||{},clock=joint.sameEuclideanClock;
  const collective=Number(carriers.collective_only?.dimension),path=Number(carriers.with_oriented_path_observable?.dimension);
  const cases={
    collective:{title:'Gemeinsame Ereignisse',size:collective,sectors:[['W',5],['R',70]],text:'Quelle und kollektive Ladungen erreichen W und R. Der ungerade Clock-Kanal wird dabei nicht angeregt.'},
    path:{title:'+ Pfadunterschied',size:path,sectors:[['W',5],['R',70],['Z',5]],text:'Wird die Differenz der beiden Pfadbindungen als Eingriff zugelassen, kommt Z hinzu. Die drei Clock-Raten sind im erreichbaren Träger vorhanden; der zusätzliche 45er bleibt unsichtbar.'},
    local:{title:'+ lokale Ströme',size:path+45,sectors:[['W',5],['R',70],['Z',5],['Rest',45]],text:'Relative lokale Ströme öffnen auch den 45er. Ein einzelner ursprünglicher Link macht seine Rate in einer Rückkehrantwort messbar. Deshalb gilt die 80er-Kürzung nur für den ausdrücklich eingeschränkten Blockprozess.'}
  };
  if(!cases[app.jointCarrier])app.jointCarrier='path';
  const selected=cases[app.jointCarrier],colors={W:'#124f42',R:'#7160a5',Z:'#a96508',Rest:'#64758a'};
  root.innerHTML=`<p class="eyebrow">Gemeinsame Auswahl · live berechnet</p><h4>${escapeHTML(data.title)}</h4><p>${escapeHTML(data.lead)}</p><div class="joint-chain">${(data.chain||[]).map((item,index)=>`<article><span>${index+1} · ${escapeHTML(statusLabel(item.status))}</span><h5>${escapeHTML(item.title)}</h5><p>${escapeHTML(item.text)}</p>${tourSourceLink({path:item.source,line:item.source_line||1,claim:'Berechnung und Voraussetzungen'})}</article>`).join('')}</div><div class="joint-cartan-result"><strong>${escapeHTML(cartan.reflection_checks_passed)} / ${escapeHTML(cartan.reflection_checks_total)} Ereigniswirkungen stimmen exakt überein</strong><span>E₈-Cartanraum: ${escapeHTML(cartan.cartan_real_dimension)} reelle Richtungen → J-Polarisation: ${escapeHTML(cartan.J_positive_polarization_dimension)} komplexe Richtungen</span></div>${jointSourceMarkup(cartan,data.quartic,data.source_process)}${Number.isFinite(path)?`<div class="joint-carrier"><h5>Was spätere Eingriffe sichtbar machen</h5><div class="composition-switch" role="group" aria-label="Erreichbarer Träger nach erlaubten Eingriffen">${Object.entries(cases).map(([id,item])=>`<button type="button" data-joint-carrier="${id}" aria-pressed="${app.jointCarrier===id}">${escapeHTML(item.title)}</button>`).join('')}</div><div class="joint-sector-track" role="img" aria-label="${selected.size} erreichbare interne Richtungen">${selected.sectors.map(([label,size])=>`<span style="flex:${size};background:${colors[label]}" title="${label}: ${size}">${size>=45?`${escapeHTML(label)} ${size}`:escapeHTML(label)}</span>`).join('')}<i style="flex:${125-selected.size}" aria-hidden="true"></i></div><p aria-live="polite"><b>${selected.size} interne Richtungen.</b> ${escapeHTML(selected.text)}</p><small>Die Umschalter vergleichen erklärte Operationsklassen. Die Richtungen sind interne Zustände; sie zählen weder Raumdimensionen noch Teilchensorten.</small></div>`:''}${clock?`<div class="joint-time-result"><h5>Strengerer Test: Sind es wirklich dieselben Zeitschritte?</h5><p>Wenn der Clock-Transfer die euklidische Zeitentwicklung des Pfad-Hamiltonoperators wäre, müssten seine Raten zu dessen Energielücken passen.</p><table><thead><tr><th>Sektor</th><th>Pfadenergie</th><th>Clock-Rate</th></tr></thead><tbody>${['W','Z','R'].map(id=>`<tr><th>${id}</th><td>${escapeHTML(clock.exact_Hpath_energies?.[id])}</td><td>${escapeHTML(clock.exact_C_eigenvalues?.[id])}</td></tr>`).join('')}</tbody></table><p><strong>Diese direkte Gleichsetzung ist ausgeschlossen.</strong> Nötig wäre λ<sub>R</sub> = λ<sub>Z</sub>³. Tatsächlich gilt 2/3 ≠ 1/27; Differenz: ${escapeHTML(clock.decisive_semigroup_identity?.actual_difference_exact||'17/27')}. Eine Änderung der Zeiteinheit repariert das nicht.</p><small>Diese Bedingung gilt nur für dieselbe physikalische euklidische Zeit. Als Überlebens- oder Vergröberungsfilter darf C eine andere Rolle erfüllen. Der aus C bestimmte Generator −log C ist auf dem 80er-Träger berechenbar; seine Quellenherleitung bleibt gesondert zu prüfen.</small></div>`:''}<p class="joint-source-scope">${escapeHTML(data.source_scope)}</p>`;
  $$('[data-joint-carrier]',root).forEach(button=>button.addEventListener('click',()=>{app.jointCarrier=button.dataset.jointCarrier;renderJointSelection(root,data);$(`[data-joint-carrier="${app.jointCarrier}"]`,root).focus({preventScroll:true});}));
  const charge=data.charge_selection;
  if(data.flavor_path_transport){const flavorPanel=document.createElement('section');flavorPanel.className='flavor-path-transport';flavorPanel.id='flavorpfad';flavorPanel.setAttribute('aria-label','Vom ursprünglichen Umlauf zum Flavoroperator');$('.joint-chain',root).before(flavorPanel);renderFlavorPathTransport(flavorPanel,data.flavor_path_transport,data.neutral_source_response,data.source_spin_lift,data.source_majorana_pairs);}
  const physicalDictionary=jointPhysicalDictionaryMarkup(data);
  if(physicalDictionary){$('.joint-chain',root).insertAdjacentHTML('beforebegin',physicalDictionary);}
  renderJointNeutrinoPhase($('.joint-neutrino-phase',root),data.source_neutrino_dictionary);
  if(data.hecke_source){const graphPanel=document.createElement('section');graphPanel.className='source-graph-tour';graphPanel.id='source-graph-tour';$('.joint-chain',root).before(graphPanel);renderSourceGraphTour(graphPanel,data.hecke_source,data.rewrite_coherence,data.cartan_clock,data.marked_source_process);}
  if(data.current_block_geometry){const geometryPanel=document.createElement('section');geometryPanel.className='current-block-geometry';geometryPanel.id='current-source-geometry';$('.joint-chain',root).before(geometryPanel);renderCurrentBlockGeometry(geometryPanel,{...data.current_block_geometry,raw_source_route:data.raw_source_route});const clusterPanel=document.createElement('section');clusterPanel.className='current-cluster';clusterPanel.id='current-source-recursion';geometryPanel.after(clusterPanel);renderCurrentCluster(clusterPanel,data.current_block_geometry.six_current_cluster_test);}
  if(data.current_source_bridge){const sourcePanel=document.createElement('div');sourcePanel.innerHTML=currentSourceBridgeMarkup(data.current_source_bridge);$('.joint-chain',root).before(sourcePanel);$$('[data-current-bridge]',sourcePanel).forEach(button=>button.addEventListener('click',()=>{app.currentBridgeView=button.dataset.currentBridge;renderJointSelection(root,data);$(`[data-current-bridge="${app.currentBridgeView}"]`,root).focus({preventScroll:true});}));}
  if(charge){const section=document.createElement('div');section.innerHTML=chargeSelectionMarkup(charge);$('.joint-cartan-result',root).before(section);}
  const selection=joint.pair_selection;
  if(selection){const panel=document.createElement('section');panel.className='pair-selection-result';const full=app.pairSymmetry==='full';panel.innerHTML=`<p class="eyebrow">Der gemeinsame Auswahlsatz</p><h5>Mehrere Bedingungen wählen tatsächlich dieselbe Bindung</h5><div class="composition-switch" role="group" aria-label="Symmetrieannahme des Paargesetzes"><button type="button" data-pair-symmetry="full" aria-pressed="${full}">Volle native Symmetrie</button><button type="button" data-pair-symmetry="marked" aria-pressed="${!full}">Nur markierte Eichsymmetrie</button></div><div class="pair-selection-answer" aria-live="polite">${full?`<div class="selection-premises"><span>Gleichbehandlung der nativen S₆-Rahmen</span><span>Feste P2-Gesamtladung</span><span>Positivität</span><span>Eindeutiger neutraler Grundzustand</span></div><p class="selected-equation">H = k (I − P<sub>Ω</sub>), k &gt; 0</p><p><b>Die Form der Paarbindung ist damit eindeutig.</b> Die Ladung verbindet die drei vorher getrennten Sektoren. Ihre Energieabstände müssen daher übereinstimmen. Frei bleibt die gemeinsame Skala k.</p><div class="selection-weights">${Object.entries(selection.connecting_weights).map(([label,item])=>`<span>${label==='5_to_10'?'5 ↔ 10':'9 ↔ 10'}: <b>${originNumber(item.actual,7)} &gt; 0</b></span>`).join('')}</div><small>Die Werte werden aus denselben Matrizen berechnet und mit den exakten Radikalformeln der Originalquelle verglichen. Die Wahl k = 5/6 benötigt zusätzlich die ursprüngliche Spurnormierung. Die Gruppe als Ereignisalphabet allein beweist noch nicht ihre volle Symmetrie als Paargesetz.</small>`:`<p class="selected-equation">Eine Familie bleibt übrig</p><p>Verlangt man nur die markierte kontinuierliche Gruppe S(U(3) × U(2)), lässt die ursprüngliche Rechnung acht reelle Richtungen für hermitesche invariante Paaroperatoren zu. Die Form I − P<sub>Ω</sub> ist darin möglich, aber nicht erzwungen.</p><small>Diese acht Richtungen gehören zur kontinuierlichen markierten Eichgruppe; sie werden nicht aus dem endlichen S₂ × S₃ allein abgelesen. Das zeigt genau, welche stärkere Symmetrieannahme die eindeutige Bindungsform auswählt.</small>`}</div>${tourSourceLink({path:'_newest2/TFPT_Gesamtdokumentation2_20260927.md',line:1528,claim:'Originaler gemeinsamer Auswahlsatz und markierte Alternative'})}</section>`;$('.joint-chain',root).before(panel);$$('[data-pair-symmetry]',panel).forEach(button=>button.addEventListener('click',()=>{app.pairSymmetry=button.dataset.pairSymmetry;renderJointSelection(root,data);$(`[data-pair-symmetry="${app.pairSymmetry}"]`,root).focus({preventScroll:true});}));}
  const pair=charge?.conserved_pair_dynamics;
  if(pair){const exchange=document.createElement('div');exchange.className='pair-charge-exchange';exchange.innerHTML=`<article><span>Fünfer-Nachbar U</span><strong>+${escapeHTML(pair.fundamental_charge_shift_exact)}</strong><small>Ladungsänderung</small></article><div aria-hidden="true">⇄</div><article><span>Gegenfünfer-Nachbar Ū</span><strong>${escapeHTML(pair.antifundamental_charge_shift_exact).replace('-','−')}</strong><small>Ladungsänderung</small></article><p>Gemeinsame Änderung: <b>${escapeHTML(pair.total_charge_shift_exact)}</b> · Matrixelement von P<sub>Ω</sub>: <b>${escapeHTML(pair.singlet_projector_color_to_weak_exact)}</b><br>Beide Nachbarblöcke sind bereits Teil der vorhandenen Paardynamik.</p>`;$('.charge-positive',root).after(exchange);}
  if(data.zuse_review?.length){const review=document.createElement('details');review.className='zuse-complete-review';review.innerHTML=`<summary>Zuse nochmals vollständig einordnen · zehn Verbindungen</summary><p>Abgleich mit dem Original <a href="https://sferics.idsia.ch/pub/juergen/zuserechnenderraum.pdf" target="_blank" rel="noopener">Calculating Space / Rechnender Raum</a> und den drei ergänzten Texten.</p><div>${data.zuse_review.map(item=>`<article><h5>${escapeHTML(item.idea)}</h5><p>${escapeHTML(item.book)}</p><p><b>Verbindung zu TFPT:</b> ${escapeHTML(item.connection)}</p></article>`).join('')}</div>`;root.append(review);}
  $$('[data-source-step]',root).forEach(button=>button.addEventListener('click',()=>{app.sourceReplayStep=Number(button.dataset.sourceStep);renderJointSelection(root,data);$(`[data-source-step="${app.sourceReplayStep}"]`,root).focus({preventScroll:true});}));
}

function originFacts(data,loop,index) {
  const integer=data.integer||{},clock=data.clock||{},em=data.electromagnetic||{};
  const structural=[
    [['Blätter',integer.cover],['P1-Normierung',em.c3]],
    [['Marken',integer.marks],['Anker',(integer.anchor||[]).join(', ')]],
    [['Zyklen / Familien',integer.family],['Funktionen / Träger',integer.carrier]],
    [['Verklebungsindex',integer.glue_index],['Normen',(integer.glue_norms||[]).join(' + ')],['Determinante danach',integer.glued_determinant]],
    [['Rang',integer.rank],['Clockordnung',integer.coxeter_order]],
    [['Lebende Phasen',integer.live_phases],['Faktorisierung',`${integer.cover??'–'} · ${integer.family??'–'} · ${integer.carrier??'–'}`]],
    [['c₃',em.c3],['P2-Träger',integer.carrier]]
  ];
  const response=[
    [['Besetzte Komponenten',integer.occupied_components],['Halbspinor',integer.half_spinor]],
    [['φ₀',em.phi0],['Grundanteil',em.phi_base],['Kontaktkorrektur',em.delta_top]],
    [['Trägernorm',integer.glue_norms?.[0]],['U(1)-Budget',integer.abelian_budget]],
    [['q(α)',em.q_alpha],['Deckexponent',integer.cover]],
    [['φs(α)',em.phi_seam_alpha],['α⁻¹',em.alpha_inverse],['Wurzelresiduum',em.root_residual]],
    [['Fixpunktgleichung',em.formula],['Lokale Clock',`${clock.full_turn??'–'} Schritte`]]
  ];
  return (loop==='response'?response:structural)[index]||[];
}

function renderOriginCascade(root,cascade,integer) {
  const spine=(cascade?.spine||[]).map(Number).filter(Number.isFinite);if(!root||!spine.length)return;
  const start=Number(cascade.start??spine[0]),end=Number(cascade.end??spine.at(-1)),span=Math.max(1,start-end),occupied=integer?.occupied_components;
  root.innerHTML=`<div class="origin-cascade-heading"><div><p class="eyebrow">Optionaler Anschluss · keine Auswahlbedingung</p><h5>Interne Skalen von ${escapeHTML(start)} bis ${escapeHTML(end)}</h5></div><span>${spine.length} Stufen</span></div><div class="origin-cascade-chart"></div><div class="origin-cascade-links"><span><b>${escapeHTML(occupied??'–')}</b> besetzte Komponenten</span><i aria-hidden="true">/</i><span><b>${escapeHTML(cascade.start??'–')}</b> Kaskadenstart</span><i aria-hidden="true">→</i><span><b>${escapeHTML(cascade.root_count??'–')}</b> E₈-Wurzeln</span><i aria-hidden="true">/</i><span><b>${escapeHTML(cascade.gauge_dimension??'–')}</b> Gauge-Dimensionen</span></div><p class="origin-cascade-kappa"><b>Adjungierte Dimension ${escapeHTML(cascade.adjoint_dimension??'–')}</b>${cascade.kappa_e8?` · κ<sub>E₈</sub> = ${escapeHTML(originNumber(cascade.kappa_e8))}`:''}</p><p class="origin-cascade-scope">${escapeHTML(cascade.scope||'Diese Kaskade ordnet interne Skalen. Die Gleichsetzung mit räumlicher Vergröberung ist eine eigene Abbildung.')}</p>`;
  const svg=svgEl('svg',{viewBox:'0 0 1000 230',role:'img','aria-label':`E8-Kaskade mit ${spine.length} internen Stufen von ${start} bis ${end}`}),points=spine.map((value,index)=>({value,x:48+index*(904/Math.max(1,spine.length-1)),y:38+(start-value)/span*128}));
  [38,102,166].forEach(y=>svg.append(svgEl('line',{x1:38,y1:y,x2:962,y2:y,stroke:'#d8e0db','stroke-width':1})));
  svg.append(svgEl('path',{d:points.map((point,index)=>`${index?'L':'M'}${point.x},${point.y}`).join(' '),fill:'none',stroke:'#124f42','stroke-width':4,'stroke-linejoin':'round'}));
  points.forEach((point,index)=>{svg.append(svgEl('line',{x1:point.x,y1:point.y,x2:point.x,y2:184,stroke:index%2?'#ded8ef':'#d4e4de','stroke-width':5}));svg.append(svgEl('circle',{cx:point.x,cy:point.y,r:index===0||index===points.length-1?8:5,fill:index%2?'#7160a5':'#124f42',stroke:'#fff','stroke-width':2}));if(index%5===0||index===points.length-1){const label=svgEl('text',{x:point.x,y:207,'text-anchor':'middle',fill:'#4f5e56','font-size':12,'font-weight':750},point.value);svg.append(label);}});
  svg.append(svgEl('text',{x:48,y:24,fill:'#124f42','font-size':12,'font-weight':800},'Beginn'));svg.append(svgEl('text',{x:952,y:180,'text-anchor':'end',fill:'#7160a5','font-size':12,'font-weight':800},'Rang 8'));
  $('.origin-cascade-chart',root).append(svg);
}

function transferEigenvalue(value) {
  if(typeof value==='number')return value;const parts=String(value??'').split('/').map(Number);return parts.length===2&&parts.every(Number.isFinite)&&parts[1]!==0?parts[0]/parts[1]:Number(value);
}

function renderOriginTransfer(root,transfer) {
  const continuation=transfer?.continuation,spectrum=continuation?.spectrum||[],rows=transfer?.iteration?.rows||[];if(!root||!spectrum.length)return;
  const maxDepth=Math.max(1,...rows.map(row=>Number(row.depth)||0)),depth=Math.max(0,Math.min(maxDepth,Number(app.originTransferDepth)||0));app.originTransferDepth=depth;
  const labels={'1':'W-Code','2/3':'gerader Rest','1/3':'ungerader Rest'},tones={'1':'#124f42','2/3':'#7160a5','1/3':'#a96508'},bars=spectrum.map(item=>{const eigenvalue=transferEigenvalue(item.value),amplitude=Number.isFinite(eigenvalue)?Math.pow(eigenvalue,depth):0;return {...item,eigenvalue,amplitude};});
  root.innerHTML=`<div class="origin-transfer-heading"><div><p class="eyebrow">Originalregel auf dem 125-dimensionalen Trimer</p><h5>Bedingte Fortsetzung auf die Codezelle</h5></div><code>${escapeHTML(continuation.formula||'')}</code></div><label class="origin-transfer-slider"><span>Iterationen n <output>${depth}</output></span><input type="range" min="0" max="${maxDepth}" step="1" value="${depth}" aria-label="Anzahl der Transferiterationen" aria-valuetext="${depth} Iterationen"></label><div class="origin-transfer-bars" role="img" aria-label="Amplituden nach ${depth} Iterationen">${bars.map(item=>`<article><div class="origin-transfer-track"><i style="height:${Math.max(0,Math.min(100,item.amplitude*100))}%;background:${tones[item.value]||'#124f42'}"></i></div><strong>${escapeHTML(labels[item.value]||item.sector||item.value)}</strong><b>${escapeHTML(fmt(item.amplitude,7))}</b><small>λ=${escapeHTML(item.value)} · ${escapeHTML(item.multiplicity)} Richtungen</small></article>`).join('')}</div><p class="origin-transfer-boundary"><strong>Amplituden, keine Populationen.</strong> Decktausch ↔ Außentausch und fester Slot ↔ W müssen identifiziert werden. Zusätzlich setzt diese Fortsetzung eine gemeinsame Rate im verbleibenden ungeraden 45er-Sektor voraus.</p><details class="origin-transfer-scope"><summary>Was damit bewiesen ist – und was nicht</summary><p>${escapeHTML(transfer.typed_identification?.scope||'')}</p><p>${escapeHTML(transfer.scope?.cptp_boundary||'')}</p></details>`;
  $('input[type="range"]',root).addEventListener('input',event=>{
    const nextDepth=Number(event.target.value);app.originTransferDepth=nextDepth;
    event.target.setAttribute('aria-valuetext',`${nextDepth} Iterationen`);
    $('output',root).textContent=nextDepth;
    $('.origin-transfer-bars',root).setAttribute('aria-label',`Amplituden nach ${nextDepth} Iterationen`);
    $$('.origin-transfer-bars article',root).forEach((article,index)=>{
      const amplitude=Math.pow(bars[index].eigenvalue,nextDepth);
      $('i',article).style.height=`${Math.max(0,Math.min(100,amplitude*100))}%`;
      $('b',article).textContent=fmt(amplitude,7);
    });
  });
}

function renderOriginClosure(root,data) {
  if(!root||!data)return;
  const loops={structural:data.structural_loop||[],response:data.response_loop||[]},loop=loops[app.originLoop]?.length?app.originLoop:'structural',nodes=loops[loop];
  app.originLoop=loop;app.originNode=Math.max(0,Math.min(app.originNode,Math.max(0,nodes.length-1)));
  const facts=originFacts(data,loop,app.originNode),integer=data.integer||{},clock=data.clock||{},em=data.electromagnetic||{},sources=(data.sources||[]).map(tourSourceLink).filter(Boolean).join('');
  const path=(items,id,title,badge)=>`<section class="origin-loop ${app.originLoop===id?'is-active':''}"><header><div><span>${escapeHTML(badge)}</span><h5>${escapeHTML(title)}</h5></div><b aria-hidden="true">↻</b></header><ol>${items.map((item,index)=>`<li><button type="button" data-origin-loop="${id}" data-origin-node="${index}" aria-pressed="${app.originLoop===id&&app.originNode===index}"><small>${index+1}</small><span>${escapeHTML(item)}</span></button></li>`).join('')}</ol></section>`;
  root.innerHTML=`<div class="origin-closure-head"><p class="eyebrow">Zwei gekoppelte Rückschleifen</p><h4>${escapeHTML(data.title||'Der Ursprung als Selbstkonsistenz')}</h4><p>${escapeHTML(data.lead||'')}</p></div><div class="origin-loop-grid">${path(loops.structural,'structural','Struktur schließt auf ihren Ausgangspunkt','exakt in der angegebenen Klasse')}${path(loops.response,'response','Nahtantwort schließt auf α zurück','skalare U(1)-Gleichung')}</div><p class="origin-coupling"><span>Diskrete Struktur und Clock</span><b aria-hidden="true">↔</b><span>dieselbe Nahtphase und α-Antwort</span></p><article class="origin-node-detail" aria-live="polite"><div><span>${loop==='structural'?'Strukturschleife':'Antwortschleife'} · ${app.originNode+1}/${nodes.length}</span><h5>${escapeHTML(nodes[app.originNode]||'')}</h5></div><dl>${facts.map(([label,value])=>`<div><dt>${escapeHTML(label)}</dt><dd>${escapeHTML(originNumber(value))}</dd></div>`).join('')}</dl><p>${escapeHTML(loop==='structural'?integer.scope:em.scope)}</p></article>${data.cascade?'<details class="origin-optional"><summary>Optional: E₈-Skalenkaskade</summary><section class="origin-cascade" aria-label="Optionale E8-Kaskade der internen Skalen"></section></details>':''}<div class="origin-clock-note"><div><p class="eyebrow">Treue lokale Clock</p><strong>Bleiben ${escapeHTML(clock.stay||'–')} · Wechseln ${escapeHTML(clock.hop||'–')} · Abfluss ${escapeHTML(clock.leak||'–')}</strong><span>Spektrum ${escapeHTML((clock.spectrum||[]).join(' / '))}; voller Umlauf nach ${escapeHTML(clock.full_turn??'–')} Schritten.</span></div><p>${escapeHTML(clock.scope||'')}</p></div>${data.transfer?'<section class="origin-transfer" aria-label="Bedingte Fortsetzung der Originalregel auf die Codezelle"></section>':''}${(data.process_requirements||[]).length?`<details class="origin-requirements"><summary>Was ein vollständiger Prozess zusätzlich bewahren muss</summary><ol>${data.process_requirements.map(item=>`<li>${escapeHTML(item)}</li>`).join('')}</ol></details>`:''}${sources?`<div class="origin-sources"><strong>Originalstellen</strong>${sources}</div>`:''}`;
  renderOriginCascade($('.origin-cascade',root),data.cascade,integer);
  renderOriginTransfer($('.origin-transfer',root),data.transfer);
  $$('[data-origin-loop]',root).forEach(button=>button.addEventListener('click',()=>{app.originLoop=button.dataset.originLoop;app.originNode=Number(button.dataset.originNode);renderOriginClosure(root,data);}));
}

function compositionScope(scope) {return scope&&scope.includes('no primitive source selection')?'Exaktes endliches Resultat für die benannte positive Klasse aus neun Portpaaren und die vorgegebenen W/W̄-Blöcke. Nicht ausgewählt sind die ursprüngliche Quelle, ein globaler Grundzustand, ein physikalischer Generator oder ein Kontinuumsmodell.':scope||'';}

function aspectCardGrid(items) {return `<div class="aspect-card-grid">${items.map(item=>`<details><summary><span><strong>${escapeHTML(item.title)}</strong></span><span class="tour-status ${escapeHTML(tourStatusClass(item.status))}">${escapeHTML(statusLabel(item.status))}</span><span class="zuse-claim">${escapeHTML(readableValue(item.claim))}</span></summary><div class="zuse-detail">${item.assessment?`<section><b>Bewertung</b><p>${escapeHTML(readableValue(item.assessment))}</p></section>`:''}${item.implication?`<section><b>Folgerung</b><p>${escapeHTML(readableValue(item.implication))}</p></section>`:''}<div class="implication-sources">${(item.sources||[]).map(tourSourceLink).filter(Boolean).join('')}</div></div></details>`).join('')}</div>`;}

function renderTourConsequences(implications,candidates,zuseAspects,worldProcess,kernelAspects,kernelSummary) {
  const root=$("#tour-consequences");if(!root)return;
  const composition=app.snapshot?.stages?.find(stage=>stage.id==='assembly')?.data?.composition,originClosure=kernelSummary?.origin_closure||app.snapshot?.stages?.find(stage=>stage.id==='origin')?.data?.origin_closure,hasWorld=worldProcess&&Object.keys(worldProcess).length,hasKernel=kernelAspects.length||(kernelSummary&&Object.keys(kernelSummary).length)||originClosure;
  if(!implications.length&&!candidates.length&&!zuseAspects.length&&!hasWorld&&!hasKernel&&!composition){root.hidden=true;root.innerHTML='';return;}
  root.hidden=false;app.implicationIndex=Math.max(0,Math.min(app.implicationIndex,Math.max(0,implications.length-1)));
  const selected=implications[app.implicationIndex],selectedSources=(selected?.sources||[]).map(tourSourceLink).filter(Boolean).join('');
  const chain=implications.length?`<div class="implication-chain" role="list" aria-label="Folgerungskette">${implications.map((item,index)=>`<button type="button" role="listitem" class="implication-card ${index===app.implicationIndex?'is-active':''}" data-implication-index="${index}" aria-pressed="${index===app.implicationIndex}"><span>Wenn</span><strong>${escapeHTML(item.premise)}</strong><i aria-hidden="true">↓</i><span>Dann</span><b>${escapeHTML(item.consequence)}</b></button>`).join('')}</div>`:'';
  const detail=selected?`<article class="implication-detail" aria-live="polite"><div><span class="tour-status ${escapeHTML(tourStatusClass(selected.status))}">${escapeHTML(statusLabel(selected.status))}</span><p><strong>Wenn:</strong> ${escapeHTML(selected.premise)}</p><p><strong>Dann:</strong> ${escapeHTML(selected.consequence)}</p></div>${selectedSources?`<div class="implication-sources"><strong>Quellen</strong>${selectedSources}</div>`:''}</article>`:'';
  const candidateCards=candidates.map(candidate=>`<article class="solution-candidate"><header><div><span>${escapeHTML(candidate.id||'')}</span><h4>${escapeHTML(candidate.title)}</h4></div><span class="tour-status ${escapeHTML(tourStatusClass(candidate.status))}">${escapeHTML(statusLabel(candidate.status))}</span></header>${candidate.idea?`<p class="candidate-idea">${escapeHTML(readableValue(candidate.idea))}</p>`:''}<div class="candidate-balance"><section><b>Aus der Kette hergeleitet</b><p>${escapeHTML(readableValue(candidate.derived))}</p></section><section><b>Noch erforderlich</b><p>${escapeHTML(readableValue(candidate.requires))}</p></section></div></article>`).join('');
  const compositionSources=(composition?.sources||[]).map(tourSourceLink).filter(Boolean).join('');
  const compositionPanel=composition?`<section class="composition-explorer" aria-labelledby="composition-title"><div class="composition-heading"><div><p class="eyebrow">Gemeinsame Komposition</p><h3 id="composition-title">Derselbe Inhalt – mehrere Skalen</h3></div><div class="composition-switch" role="group" aria-label="Skala auswählen">${[['encoder','Encoder → Pfad'],['ports','Neun Portpaare'],['space','Raum × Level']].map(([id,label])=>`<button type="button" data-composition-view="${id}" aria-pressed="${app.compositionView===id}">${label}</button>`).join('')}</div></div><div class="composition-scene tour-stage" id="composition-scene"></div><p class="composition-scope">${escapeHTML(compositionScope(composition.scope))}</p>${compositionSources?`<div class="composition-sources">${compositionSources}</div>`:''}</section>`:'';
  const processKeys=[['state','Zustand'],['rule','Regel'],['constraints','Nebenbedingungen'],['derived','Abgeleitet'],['selected','Zusätzliche Festlegungen']].filter(([key])=>worldProcess[key]!==undefined),process=hasWorld?`<section class="world-process" aria-labelledby="world-process-title"><h3 id="world-process-title">Bisherige endliche Prozessmodelle</h3><p>Diese bedingten Modelle illustrieren Komposition und Eingriffe. Der darunter dargestellte direkte Quellaufbau bestimmt bereits ein vollständiges Vakuumgesetz; seine Herkunftsannahme wird dort gesondert benannt.</p><div>${processKeys.map(([key,label],index)=>`<article><span>${escapeHTML(label)}</span><p>${escapeHTML(readableValue(worldProcess[key]))}</p>${index<processKeys.length-1?'<i aria-hidden="true">→</i>':''}</article>`).join('')}</div></section>`:'';
  const kernelSteps=Array.isArray(kernelSummary?.steps)?kernelSummary.steps:[],kernelTitle=kernelSummary?.title&&kernelSummary.title!=='Der vollständige Prozesskern'?`<h4>${escapeHTML(kernelSummary.title)}</h4>`:'',kernel=hasKernel?`<section class="kernel-aspects" id="process-kernel" aria-labelledby="process-kernel-title"><p class="eyebrow">Gemeinsamer Ablauf</p><h3 id="process-kernel-title">Der vollständige Prozesskern</h3>${kernelTitle}${kernelSummary?.lead?`<p class="kernel-lead">${escapeHTML(kernelSummary.lead)}</p>`:''}${kernelSummary?.source_program?'<section class="source-program" id="source-program" aria-label="Geführte Tour durch das gemeinsame Quellgesetz"></section>':''}${kernelSummary?.joint_charged_source?'<section class="joint-charged-source" id="joint-charged-source"></section>':''}${kernelSummary?.joint_selection?'<section class="joint-selection" id="joint-selection" aria-label="Gemeinsame Prüfung der Auswahlbedingungen"></section>':''}${originClosure?'<section class="origin-closure" id="origin-closure" aria-label="Gekoppelte Rückschleifen von P1, P2, E₈, φ₀ und Alpha"></section>':''}${kernelSteps.length?`<ol class="kernel-steps">${kernelSteps.map(step=>`<li>${escapeHTML(readableValue(step))}</li>`).join('')}</ol>`:''}<section class="history-demo" id="history-demo" aria-label="Interferenz der Ereignisgeschichten"></section><section class="marker-demo" id="marker-demo" aria-label="Ladung wählt eine Familie von Raummarkierungen"></section>${kernelSummary?.result?`<div class="kernel-result"><b>Ergebnis</b><p>${escapeHTML(readableValue(kernelSummary.result))}</p></div>`:''}${kernelSummary?.scope?`<p class="kernel-scope">${escapeHTML(readableValue(kernelSummary.scope))}</p>`:''}${kernelAspects.length?`<h4>Die tragenden Aussagen im Zusammenhang</h4>${aspectCardGrid(kernelAspects)}`:''}</section>`:'';
  const zuse=zuseAspects.length?`<section class="zuse-aspects" id="zuse-aspects" aria-labelledby="zuse-title"><h3 id="zuse-title">Zuse-Aspekte in der gemeinsamen Kette</h3>${aspectCardGrid(zuseAspects)}</section>`:'';
  root.innerHTML=`<header class="consequences-head"><p class="eyebrow">Folgerungen &amp; mögliche Abschlüsse</p><h2 id="tour-consequences-title">Was aus der ganzen Kette folgt</h2></header>${compositionPanel}${chain}${detail}${process}${kernel}${candidateCards?`<section class="solution-candidates" aria-labelledby="solution-candidates-title"><h3 id="solution-candidates-title">Konditionale Gesamtlösungskandidaten</h3><div>${candidateCards}</div></section>`:''}${zuse}`;
  renderHistoryKernel($('#history-demo',root),kernelSummary?.calculations);
  renderMarkerSelection($('#marker-demo',root),kernelSummary?.marker_selection);
  renderJointSelection($('#joint-selection',root),kernelSummary?.joint_selection);
  renderSourceProgram($('#source-program',root),kernelSummary?.source_program,kernelSummary?.source_unification);
  renderJointChargedSource($('#joint-charged-source',root),kernelSummary?.joint_charged_source);
  renderOriginClosure($('#origin-closure',root),originClosure);
  if(composition){renderCompositionScene($("#composition-scene",root),composition);$$('[data-composition-view]',root).forEach(button=>button.addEventListener('click',()=>{app.compositionView=button.dataset.compositionView;renderTourConsequences(implications,candidates,zuseAspects,worldProcess,kernelAspects,kernelSummary);}));}
  $$('[data-implication-index]',root).forEach(button=>button.addEventListener('click',()=>{app.implicationIndex=Number(button.dataset.implicationIndex);renderTourConsequences(implications,candidates,zuseAspects,worldProcess,kernelAspects,kernelSummary);root.querySelector('.implication-detail')?.scrollIntoView({behavior:'smooth',block:'nearest'});}));
}

function renderTourGates(gates) {
  const root=$("#tour-gates");if(!root)return;if(!gates.length){root.innerHTML='';return;}
  root.innerHTML=`<p class="eyebrow">Entscheidende Übergänge</p><h2 id="tour-gates-title">Was bis zur Gesamtlösung noch ausgewählt oder hergeleitet werden muss</h2><div class="tour-gate-list">${gates.map(gate=>`<article class="tour-gate"><div><h3>${escapeHTML(`${gate.id ? `${gate.id} · ` : ''}${gate.title}`)}</h3><span class="tour-gate-status">${escapeHTML(statusLabel(gate.status))}</span></div><p><strong>Benötigt:</strong> ${escapeHTML(gate.requires||'')}<br><strong>Schon vorhanden:</strong> ${escapeHTML(gate.available||'')}</p><p><strong>Nächster entscheidender Test</strong><br>${escapeHTML(gate.next_decisive||'')}</p></article>`).join('')}</div>`;
}

function renderTourCoverage(coverage) {
  const root=$("#tour-coverage-content");if(!root)return;root.innerHTML=`<div class="tour-coverage-list">${coverage.map(item=>`<div class="tour-coverage-item"><strong>${escapeHTML(item.label||item.path)}</strong><small>${escapeHTML(item.note||'')}</small>${item.path&&!item.path.startsWith('/')?`<a href="${sourceURL({path:item.path,line:1})}" target="_blank" rel="noopener">Original öffnen ↗</a>`:''}</div>`).join('')}</div>`;
}

function makeTourSVG(chapter) {
  const svg=svgEl('svg',{viewBox:'0 0 1000 530',role:'img','aria-label':chapter.title});svg.append(svgEl('title',{},chapter.title));const defs=svgEl('defs'),marker=svgEl('marker',{id:'tour-arrow',viewBox:'0 0 10 10',refX:'9',refY:'5',markerWidth:'7',markerHeight:'7',orient:'auto'});marker.append(svgEl('path',{d:'M0 0L10 5L0 10z',fill:'#78958b'}));defs.append(marker);svg.append(defs);return svg;
}
function sceneText(svg,x,y,text,cls='scene-label',anchor='start'){const node=svgEl('text',{x,y,class:cls,'text-anchor':anchor},String(text??''));svg.append(node);return node;}
function sceneLines(svg,text,x,y,maxChars=34,cls='scene-label',anchor='start',lineHeight=17){const words=String(text??'').split(/\s+/),lines=[];let line='';words.forEach(word=>{if((line+' '+word).trim().length>maxChars&&line){lines.push(line);line=word;}else line=(line+' '+word).trim();});if(line)lines.push(line);const node=svgEl('text',{x,y,class:cls,'text-anchor':anchor});lines.slice(0,4).forEach((row,index)=>node.append(svgEl('tspan',{x,dy:index?lineHeight:0},row)));svg.append(node);return node;}
function sceneBox(svg,x,y,w,h,title,subtitle='',tone='scene-card'){svg.append(svgEl('rect',{x,y,width:w,height:h,rx:15,class:tone}));sceneLines(svg,title,x+w/2,y+30,Math.max(12,Math.floor(w/7)),'scene-label','middle',16);if(subtitle)sceneLines(svg,subtitle,x+w/2,y+h-24,Math.max(14,Math.floor(w/7)),'scene-small','middle',14);}
function sceneArrow(svg,x1,y1,x2,y2,dashed=false){const attrs={d:`M${x1},${y1} C${x1+(x2-x1)*.42},${y1} ${x1+(x2-x1)*.58},${y2} ${x2},${y2}`,class:dashed?'scene-open':'scene-flow'};if(dashed)attrs['marker-end']='url(#tour-arrow)';svg.append(svgEl('path',attrs));}
function numericValues(value){if(Array.isArray(value))return value.map(Number).filter(Number.isFinite);if(value&&typeof value==='object')return Object.values(value).map(Number).filter(Number.isFinite);return Number.isFinite(Number(value))?[Number(value)]:[];}
function stageData(data){return data?.stages&&typeof data.stages==='object'?data.stages:{};}

function sceneBigPicture(svg,data){const branches=data.branches||[],feeds=[];branches.slice(0,2).forEach((branch,column)=>{const x=45+column*315;sceneText(svg,x+122,55,branch.title,'scene-title','middle');const steps=branch.steps||[];steps.forEach((step,index)=>{const y=82+index*82;sceneBox(svg,x,y,245,62,step,'','scene-card');if(index<steps.length-1)sceneArrow(svg,x+122,y+62,x+122,y+78);});feeds.push({x:x+122,y:82+Math.max(0,steps.length-1)*82+62});});feeds.forEach(feed=>svg.append(svgEl('path',{d:`M${feed.x},${feed.y} L${feed.x},430 L640,430`,fill:'none',stroke:'#78958b','stroke-width':2})));svg.append(svgEl('circle',{cx:640,cy:430,r:5,class:'scene-solid'}));svg.append(svgEl('path',{d:'M640,430 L660,430 L660,205 L690,205',class:'scene-flow'}));sceneBox(svg,690,132,270,145,data.meeting||'Gemeinsamer Anschluss','Quelle, Wirkungen und Anfangszustand müssen zusammenpassen','scene-card');sceneArrow(svg,825,277,825,338,true);sceneBox(svg,690,350,270,105,data.destination||'Physikalische Gesamtlösung',data.destination_status==='open'?'entscheidende Übergänge offen':'','scene-card');sceneText(svg,500,500,'Zwei Arbeitsstränge · ein gemeinsamer Herkunfts- und Wirkungsvertrag','scene-small','middle');}

function sceneBoundary(svg,data){const marks=data.marks||[[1,0],[0,1],[-1,0],[0,-1]],cx=205,cy=255,r=118;svg.append(svgEl('circle',{cx,cy,r,fill:'rgba(255,255,255,.55)',stroke:'#124f42','stroke-width':3}));marks.forEach((mark,index)=>{const angle=Math.atan2(-(mark[1]||0),mark[0]||0),x=cx+Math.cos(angle)*r,y=cy+Math.sin(angle)*r;svg.append(svgEl('circle',{cx:x,cy:y,r:13,class:index%2?'scene-accent':'scene-solid'}));sceneText(svg,x+(x>cx?22:-22),y+4,index+1,'scene-label',x>cx?'start':'end');});for(let index=0;index<3;index++)svg.append(svgEl('path',{d:`M${105+index*13},${220+index*22} Q${205},${105+index*22} ${305-index*13},${265-index*16}`,fill:'none',stroke:['#124f42','#7160a5','#a96508'][index],'stroke-width':2,'stroke-dasharray':'6 5'}));sceneText(svg,cx,430,'vier Marken auf einer Naht','scene-small','middle');sceneArrow(svg,340,205,455,170);sceneArrow(svg,340,300,455,350);sceneBox(svg,470,105,210,125,`${data.cycle_rank} unabhängige Umläufe`,'topologischer Rang','scene-card');sceneBox(svg,470,295,210,125,`${data.function_dimension} Funktionenrichtungen`,'anderer Raum, andere Zählung','scene-card');sceneBox(svg,750,200,190,125,`${data.carrier_components} Trägerzustände`,'interne Ladungsbasis','scene-card');sceneText(svg,710,470,'3, 5 und 16 haben verschiedene Rollen','scene-title','middle');}

function sceneAlphabet(svg,data){sceneText(svg,120,55,`${fmt(data.words)} Codewörter`,'scene-title','middle');for(let index=0;index<16;index++){const x=60+(index%4)*38,y=92+Math.floor(index/4)*38;svg.append(svgEl('rect',{x,y,width:27,height:27,rx:4,fill:index%2?'#7160a5':'#124f42',opacity:.35+index/28}));}sceneArrow(svg,225,180,330,180);sceneText(svg,465,55,`${fmt(data.root_count)} E₈-Wurzeln`,'scene-title','middle');const roots=data.roots||[];roots.forEach((root,index)=>{const values=numericArray(root),px=465+((values[0]||0)+.55*(values[2]||0)-.3*(values[4]||0))*85,py=185-((values[1]||0)-.4*(values[3]||0)+.28*(values[6]||0))*75;svg.append(svgEl('circle',{cx:px,cy:py,r:4,fill:index%2?'#7160a5':'#124f42',opacity:.75}));});sceneText(svg,465,305,`${roots.length} Repräsentanten gezeichnet · Gesamtzahl aus Live-Rechnung`,'scene-small','middle');sceneArrow(svg,595,180,710,180);sceneText(svg,830,55,`${fmt(data.ray_count)} Strahlen`,'scene-title','middle');for(let index=0;index<60;index++){const angle=2*Math.PI*index/60-Math.PI/2,ring=index%2?112:82;svg.append(svgEl('circle',{cx:830+Math.cos(angle)*ring,cy:190+Math.sin(angle)*ring,r:index%4===0?4.5:2.8,fill:index%4===0?'#a96508':'#124f42'}));}sceneBox(svg,685,350,290,100,'Reflexion r = I − 2|ψ⟩⟨ψ|','60 konkrete Ereignisoperatoren','scene-card');sceneText(svg,500,495,'Binärer Code → explizite Vektoren → Operatoralphabet','scene-title','middle');}

function sceneProtectedCode(svg,data){sceneText(svg,120,48,`${fmt(data.ambient)} Richtungen`,'scene-title','middle');for(let index=0;index<256;index++){const x=52+(index%16)*9,y=85+Math.floor(index/16)*9;svg.append(svgEl('rect',{x,y,width:6,height:6,rx:1,fill:'#124f42',opacity:.18+(index%5)*.05}));}sceneText(svg,122,252,'voller Vierregisterraum','scene-small','middle');sceneArrow(svg,220,155,735,155);sceneBox(svg,750,92,180,125,`${fmt(data.code)} Richtungen`,'geschützter Fünfer-Code','scene-card');sceneText(svg,840,245,`Energie 0 · Lücke ${fmt(data.gap)}`,'scene-small','middle');sceneArrow(svg,220,325,430,325,true);sceneBox(svg,445,275,185,105,`${fmt(data.symmetric)} symmetrische Richtungen`,'gesondertes Quellenmodell','scene-card');sceneArrow(svg,630,325,750,210,true);const bars=data.spectrum?.bars||[];sceneText(svg,500,390,'Spektrum des Ereignismittels Ū₄','scene-title','middle');sceneText(svg,500,414,'H = 0,6 I − Ū₄: höchster Mittelwert → niedrigste Energie','scene-small','middle');const max=Math.max(...bars.map(item=>item.multiplicity||0),1);bars.forEach((item,index)=>{const x=300+index*90,height=75*(item.multiplicity||0)/max;svg.append(svgEl('rect',{x,y:500-height,width:55,height,rx:4,fill:item.value===data.spectrum?.highlight?'#7160a5':'#124f42',opacity:.85}));sceneText(svg,x+27,515,`${fmt(item.value,3)} · ${item.multiplicity}`,'scene-small','middle');});}

function sceneInformation(svg,data){const live=stageData(data),readout=numericValues(live.readout_ranks||data.readout_ranks||[]),closure=numericValues(live.closure_ranks||[]);sceneText(svg,500,45,'Zwei verschiedene Wege zur vollständigen Sichtbarkeit','scene-title','middle');const lane=(values,y,title,labels,color)=>{sceneText(svg,55,y-48,title,'scene-label');values.forEach((rank,index)=>{const x=150+index*335,radius=21+Math.sqrt(Math.max(rank,1))*4.8;if(index)sceneArrow(svg,x-240,y,x-radius-15,y);svg.append(svgEl('circle',{cx:x,cy:y,r:radius,fill:index===values.length-1?'#7160a5':color,opacity:.88}));sceneText(svg,x,y+7,fmt(rank),'scene-number scene-on-dark','middle');sceneText(svg,x,y+radius+27,labels[index]||`Schritt ${index+1}`,'scene-small','middle');});};lane(readout,145,'Quellenbefund: wie viele Register gemeinsam gelesen werden',['ein Register','zwei Register','drei Register'],'#124f42');lane(closure,335,'Live-Abschluss: Paarbeobachtung plus erlaubte Kontrollen',['Paarbeobachtung','eine Kontrolle','voller Operatorraum'],'#a96508');const ranks=live.projector_ranks||{},relation=live.event_vs_matching||{};sceneText(svg,500,452,`Quellpfad ${fmt(ranks.ambient)} → ${fmt(ranks.symmetric)} → ${fmt(ranks.code)} · Schnitt mit Rang ${fmt(ranks.stabilizer)} ergibt den Fünfer`,'scene-label','middle');sceneText(svg,500,480,`${fmt(relation.events)} Ereignisse ↔ ${fmt(relation.matchings)} Matchings · ${fmt(relation.event_fibre_size)} Ereignisse je Wirkung`,'scene-small','middle');sceneText(svg,500,510,data.readout_rank_scope||'Quellenbefund und berechneter Kontrollabschluss bleiben getrennt.','scene-small','middle');}

function sceneResponse(svg,data){const cx=185,cy=220,r=125;sceneText(svg,cx,55,`${data.mark_count||6} interne Marken`,'scene-title','middle');for(let index=0;index<6;index++){const angle=2*Math.PI*index/6-Math.PI/2,x=cx+Math.cos(angle)*r,y=cy+Math.sin(angle)*r;svg.append(svgEl('circle',{cx:x,cy:y,r:12,class:'scene-solid'}));sceneText(svg,x,y+4,index,'scene-small','middle');}svg.append(svgEl('line',{x1:cx,y1:cy-r,x2:cx+r*.866,y2:cy+r*.5,stroke:'#a96508','stroke-width':4}));sceneText(svg,cx,390,'15 mögliche Einzelvertauschungen','scene-small','middle');sceneArrow(svg,340,220,465,220);const matching=(data.matchings||[])[0]||[[0,1],[2,3],[4,5]],mx=580,my=220,mr=125;for(let index=0;index<6;index++){const angle=2*Math.PI*index/6-Math.PI/2,x=mx+Math.cos(angle)*mr,y=my+Math.sin(angle)*mr;svg.append(svgEl('circle',{cx:x,cy:y,r:12,class:'scene-accent'}));sceneText(svg,x,y+4,index,'scene-small','middle');}matching.forEach(([a,b])=>{const aa=2*Math.PI*a/6-Math.PI/2,bb=2*Math.PI*b/6-Math.PI/2;svg.append(svgEl('line',{x1:mx+Math.cos(aa)*mr,y1:my+Math.sin(aa)*mr,x2:mx+Math.cos(bb)*mr,y2:my+Math.sin(bb)*mr,stroke:'#7160a5','stroke-width':5}));});sceneText(svg,mx,390,`${(data.matchings||[]).length} vollständige Paarungen`,'scene-small','middle');sceneArrow(svg,725,220,805,220);sceneBox(svg,820,150,145,140,`Rang ${fmt(data.rank)}`,'2 aktive + 3 andere Richtungen','scene-card');sceneText(svg,500,470,`${(data.event_fibres||[]).length} Wirkungsgruppen · je ${(data.event_fibres||[])[0]?.length||0} ursprüngliche Ereignisse`,'scene-title','middle');}

function sceneQuartic(svg,data){const coords=data.coordinates||[],cx=320,cy=250;sceneText(svg,cx,55,'Sechs Quellenkoordinaten mit Summe null','scene-title','middle');coords.forEach((coord,index)=>{const angle=2*Math.PI*index/Math.max(coords.length,6)-Math.PI/2,length=90+Number(coord.magnitude||0)*120,x=cx+Math.cos(angle)*length,y=cy+Math.sin(angle)*length;svg.append(svgEl('line',{x1:cx,y1:cy,x2:x,y2:y,stroke:'#aebdb6','stroke-width':2}));svg.append(svgEl('circle',{cx:x,cy:y,r:15,class:index<4?'scene-solid':'scene-accent'}));sceneText(svg,x+Math.cos(angle)*26,y+Math.sin(angle)*26,`z${index+1}=${fmt(coord.re,4)}`,'scene-small',Math.cos(angle)<-.2?'end':Math.cos(angle)>.2?'start':'middle');});sceneArrow(svg,550,250,660,250);sceneBox(svg,690,130,240,125,'(Σzᵢ²)² − 4Σzᵢ⁴ = 0','Quellenfläche','scene-card');sceneBox(svg,690,300,240,105,`Residual ${fmt(data.residual)}`,'numerischer Gleichungstest','scene-card');sceneText(svg,500,480,'Diese Fläche beschreibt die Präparation, nicht sämtliche späteren Codezustände.','scene-title','middle');}

function sceneBinding(svg,data){const comparison=data.comparison||[];sceneText(svg,500,50,'Zwei Zellen · drei klar getrennte Operatorverträge','scene-title','middle');[180,360].forEach((x,index)=>{svg.append(svgEl('circle',{cx:x,cy:165,r:58,class:index?'scene-accent':'scene-solid',opacity:.9}));sceneText(svg,x,170,index?'Zelle B':'Zelle A','scene-label','middle');});svg.append(svgEl('path',{d:'M238 165 C270 115 310 115 302 165 C310 215 270 215 238 165',fill:'none',stroke:'#a96508','stroke-width':8}));sceneArrow(svg,420,165,515,165);sceneBox(svg,535,85,185,160,comparison[0]?.name||'gemeinsame Labels',`E₀=${fmt(comparison[0]?.ground_energy)} · ${fmt(comparison[0]?.selected_states)} Zustand`,'scene-card');sceneBox(svg,755,85,185,160,comparison[1]?.name||'unabhängige Labels',`E₀=${fmt(comparison[1]?.ground_energy)} · ${fmt(comparison[1]?.selected_states)} Zustände`,'scene-card');(data.branches||[]).forEach((branch,index)=>sceneBox(svg,90+index*290,330,240,90,branch,index===0?'Live-Spektrum':'Quellenvertrag','scene-card'));sceneText(svg,500,485,data.branch_comparison_scope||'Gleicher Paarzustand bedeutet nicht gleicher Hamiltonoperator.','scene-small','middle');}

function sceneRecursion(svg,data){const identity=data.tensor_identity||{},weights=identity.weights||data.quartic_weights||[];sceneText(svg,500,43,'Derselbe explizite Ereignistensor G in drei Rollen','scene-title','middle');svg.append(svgEl('circle',{cx:500,cy:96,r:35,class:'scene-solid'}));sceneText(svg,500,103,'G','scene-number scene-on-dark','middle');const roles=[{x:55,title:'4 Ausgänge',body:'Vierzellzustand Γ',tone:'#124f42'},{x:365,title:'1 Eingang + 3 Ausgänge',body:'125 × 5 Encoder',tone:'#7160a5'},{x:675,title:'gleiche Argumente',body:weights.length?`Quellen- und Igusa-Anteil ${fmt(weights[0]*100)} / ${fmt(weights[1]*100)}`:'Quellen- und Igusa-Anteil',tone:'#a96508'}];roles.forEach(role=>{sceneArrow(svg,500,125,role.x+125,165);svg.append(svgEl('rect',{x:role.x,y:170,width:250,height:125,rx:17,class:'scene-card'}));svg.append(svgEl('rect',{x:role.x,y:170,width:250,height:8,rx:4,fill:role.tone}));sceneText(svg,role.x+125,216,role.title,'scene-label','middle');sceneLines(svg,role.body,role.x+125,252,26,'scene-title','middle',19);});sceneText(svg,500,322,'G = C + A/6','scene-title','middle');sceneText(svg,500,348,'Γ = G/√10 = √(3/5) ψ + √(2/5) fᵢ','scene-title','middle');sceneText(svg,500,373,`Normgewichte 3/5 und 2/5 · Encoderfehler ${fmt(identity.encoder_error)} · Zerlegungsfehler ${fmt(identity.decomposition_error)}`,'scene-small','middle');const levels=data.levels||[];levels.forEach((level,index)=>{const x=135+index*(730/Math.max(levels.length-1,1)),r=15+Math.min(28,Math.sqrt(level.cells||1)*3);if(index)sceneArrow(svg,x-150,430,x-r,430);svg.append(svgEl('circle',{cx:x,cy:430,r,fill:index===levels.length-1?'#7160a5':'#124f42',opacity:.84}));sceneText(svg,x,435,fmt(level.cells),'scene-on-dark','middle');sceneText(svg,x,488,`Tiefe ${level.depth}`,'scene-small','middle');});}

function sceneSource(svg,data){const adapter=data.common_adapter||{},registerResidual=adapter.register_residual,codeResidual=adapter.code_residual,series=data.series||[],labels=data.readout_labels||['A','B','C'],colors=['#124f42','#7160a5','#a96508'];sceneText(svg,120,46,`${fmt(adapter.labels||60)} Ereignislabels`,'scene-title','middle');for(let index=0;index<60;index++){const x=48+(index%10)*17,y=72+Math.floor(index/10)*17;svg.append(svgEl('circle',{cx:x,cy:y,r:4.5,fill:index%4===0?'#7160a5':'#124f42',opacity:.78}));}sceneArrow(svg,225,125,340,125);sceneBox(svg,355,45,240,115,`${fmt(adapter.branches||15)} × ${fmt(adapter.labels||60)} Amplituden`,'ein gemeinsamer berechneter Adapter','scene-card');sceneArrow(svg,595,90,700,77);sceneArrow(svg,595,135,700,205);sceneBox(svg,715,28,230,100,'ℂ⁴ · ein Viererregister',registerResidual!==undefined?`Residual ${fmt(registerResidual)}`:'Registeranschluss','scene-card');sceneBox(svg,715,155,230,100,'ℂ⁵ · geschützter Fünfer-Code',codeResidual!==undefined?`Residual ${fmt(codeResidual)}`:'Codeanschluss','scene-card');sceneText(svg,475,190,`Live: b = ${phaseFraction(Number(data.phase_b)||0)}`,'scene-title','middle');sceneText(svg,475,220,`empfindlicher Test: ${fmt(data.probe_response)}`,'scene-label','middle');sceneText(svg,475,245,`lokale Kohärenz: ${fmt(series.at(-1)?.coherence_x12)}`,'scene-small','middle');sceneText(svg,475,268,'Die lokale Diagonaltrajektorie ist b-blind; der getrennte Test reagiert.','scene-small','middle');sceneText(svg,500,310,'Drei grobe Anzeigen Rρ des Registerkanals','scene-title','middle');[0,.5,1].forEach(value=>{const y=485-value*120;svg.append(svgEl('line',{x1:85,y1:y,x2:925,y2:y,class:'scene-grid'}));sceneText(svg,73,y+4,fmt(value,2),'scene-small','end');});labels.slice(0,3).forEach((label,index)=>{const x=335+index*135;svg.append(svgEl('circle',{cx:x,cy:340,r:5,fill:colors[index]}));sceneText(svg,x+11,344,`Anzeige ${label}`,'scene-small');});[0,1,2].forEach(component=>{const points=series.map((row,index)=>({x:100+index*(800/Math.max(series.length-1,1)),y:485-Number(row.readout?.[component]||0)*120}));svg.append(svgEl('path',{d:points.map((p,i)=>`${i?'L':'M'}${p.x},${p.y}`).join(' '),fill:'none',stroke:colors[component],'stroke-width':3}));points.forEach((point,index)=>{svg.append(svgEl('circle',{cx:point.x,cy:point.y,r:3.5,fill:colors[component]}));if(component===0)sceneText(svg,point.x,505,series[index]?.step??index,'scene-small','middle');});});sceneText(svg,500,522,'Ereignisschritte →','scene-small','middle');const axis=sceneText(svg,24,425,'Erwartungswert','scene-small','middle');axis.setAttribute('transform','rotate(-90 24 425)');}

function sceneNormalization(svg,data){const live=stageData(data),anti=Number(live.antisymmetric_weight),normResidual=live.normalization_residual,codeResidual=live.code_branch_residual;sceneText(svg,500,52,'Normierung auf allen erlaubten Eingängen','scene-title','middle');sceneBox(svg,70,115,230,150,'Ausgewählter gleichfaseriger Lift',Number.isFinite(anti)?`Antisymmetrischer Sektor: ${fmt(anti,9)}`:'Sektortest wird geladen','scene-card');sceneArrow(svg,300,190,395,190,true);sceneBox(svg,420,105,240,170,'Algebraische Reparatur','q = ΣL†L · B = Lq⁻¹ᐟ²','scene-card');sceneArrow(svg,660,190,755,190);sceneBox(svg,780,115,155,150,'Gesamtnorm 1',normResidual!==undefined?`Residual ${fmt(normResidual)}`:'Live-Wert folgt','scene-card');const gauges=[{label:'Code vor/nach',value:codeResidual},{label:'Vollraum nachher',value:normResidual}];gauges.forEach((gauge,index)=>{const x=170+index*430;svg.append(svgEl('circle',{cx:x,cy:405,r:62,fill:'none',stroke:'#d2ddd6','stroke-width':15}));const value=Math.max(0,Math.min(1,1-Math.abs(Number(gauge.value)||0)));svg.append(svgEl('path',{d:`M${x},343 A62 62 0 ${value>.5?1:0} 1 ${x+Math.sin(value*2*Math.PI)*62},${405-Math.cos(value*2*Math.PI)*62}`,fill:'none',stroke:index?'#7160a5':'#124f42','stroke-width':15}));sceneText(svg,x,410,fmt(gauge.value),'scene-number','middle');sceneText(svg,x,490,gauge.label,'scene-small','middle');});sceneText(svg,500,315,Number.isFinite(anti)?`Dieser Lift: ${fmt(anti)} ≠ 1 · sein Codezweig bleibt unter der Korrektur gleich`:'Exakte Sektorwerte kommen aus dem aktuellen Konsolidierungslauf','scene-label','middle');}

function sceneSpace(svg,data){sceneText(svg,500,48,'Welche unmittelbare Nachbarschaft wird gewählt?','scene-title','middle');const panels=[{x:55,title:'Clique',type:'clique'},{x:250,title:'Paare',type:'pairs'},{x:445,title:'Leeres Netz',type:'empty'},{x:670,title:'markierter A₃-Kandidat',type:'a3'}];panels.forEach(panel=>{svg.append(svgEl('rect',{x:panel.x,y:90,width:190,height:250,rx:17,class:'scene-card'}));sceneText(svg,panel.x+95,122,panel.title,'scene-label','middle');const nodes=panel.type==='a3'?12:6,coords=[];for(let i=0;i<nodes;i++){const col=panel.type==='a3'?i%4:i%3,row=panel.type==='a3'?Math.floor(i/4):Math.floor(i/3),x=panel.x+45+col*34+(panel.type==='a3'?row*12:0),y=170+row*55;coords.push({x,y});svg.append(svgEl('circle',{cx:x,cy:y,r:7,fill:panel.type==='a3'&&i%4===0?'#7160a5':'#124f42'}));}if(panel.type==='clique')coords.forEach((a,i)=>coords.slice(i+1).forEach(b=>svg.insertBefore(svgEl('line',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:'#b5c3bc','stroke-width':1}),svg.lastChild)));if(panel.type==='pairs')for(let i=0;i<coords.length;i+=2)svg.append(svgEl('line',{x1:coords[i].x,y1:coords[i].y,x2:coords[i+1].x,y2:coords[i+1].y,stroke:'#a96508','stroke-width':3}));if(panel.type==='a3')for(let i=0;i<coords.length-1;i++)if((i+1)%4)svg.append(svgEl('line',{x1:coords[i].x,y1:coords[i].y,x2:coords[i+1].x,y2:coords[i+1].y,stroke:'#7160a5','stroke-width':3}));});sceneText(svg,765,375,`${fmt(data.nodes)} Knoten · ${fmt(data.edges)} Kanten`,'scene-title','middle');sceneText(svg,765,402,`Schleifenrang ${fmt(data.loop_rank)} · ausgewählter Raumrang ${fmt(data.spatial_rank)}`,'scene-small','middle');sceneText(svg,500,485,data.countermodel_status||'Vergleich innerhalb der angegebenen Modellklasse','scene-small','middle');}

function sceneAssembly(svg,data){const live=stageData(data),trimers=live.trimers||[],cover=live.cover_counts||{},coverValues=Object.values(cover).map(Number).filter(Number.isFinite),covered=Object.keys(cover).length,exactCover=coverValues.length>0&&coverValues.every(value=>value===1);sceneText(svg,500,46,'Zehn Dreierpfade überdecken das periodische 30-Knoten-Netz','scene-title','middle');const rows=trimers.length?trimers.slice(0,10):Array.from({length:10},(_,index)=>({left:`L${index+1}`,center:`C${index+1}`,right:`R${index+1}`}));rows.forEach((trimer,index)=>{const column=index<5?0:1,row=index%5,x=65+column*470,y=95+row*66,names=[trimer.left,trimer.center,trimer.right];[0,1,2].forEach(part=>{const px=x+part*72;if(part)svg.append(svgEl('line',{x1:px-56,y1:y,x2:px-15,y2:y,stroke:part===1?'#7160a5':'#124f42','stroke-width':4}));svg.append(svgEl('circle',{cx:px,cy:y,r:14,fill:part===1?'#7160a5':'#124f42'}));sceneText(svg,px,y+4,short(names[part]??'•',4),'scene-label scene-on-dark','middle');});sceneText(svg,x+170,y-10,`Pfad ${index+1} · ${trimer.effective_representation||'–'}`,'scene-small');});sceneText(svg,55,430,'U / Ū: zwei zueinander konjugierte Ladungswirkungen','scene-label');sceneBox(svg,770,365,180,105,'Vollständige Überdeckung',covered?`${covered}/30 Knoten${exactCover?' · je 1×':''}`:`${rows.length} Pfade · ${rows.length*3} Plätze`,'scene-card');const residuals=[];if(live.covariance_residual!==undefined)residuals.push(`Kovarianz ${fmt(live.covariance_residual)}`);if(live.charge_commutator!==undefined)residuals.push(`Ladung ${fmt(live.charge_commutator)}`);sceneText(svg,500,505,residuals.join(' · ')||'Live-Cover, Kanten und Spektrum stammen aus dem Montage-Schritt.','scene-small','middle');}

function scenePhysics(svg,data){const clock=data.clock_completion||{},rr=clock.rr_multiplicities||[],code=clock.code_multiplicities||[],common=clock.common_multiplicities||[],labels=['1','i','−1','−i'];sceneText(svg,500,48,'Gleiche Dimension bedeutet noch nicht gleiche Symmetriewirkung','scene-title','middle');sceneBox(svg,65,90,230,115,'älterer Fünfer-Träger',`C₄-Multiplizitäten ${rr.join(' · ')}`,'scene-card');sceneBox(svg,65,260,230,115,'neuer Fünfer-Code',`C₄-Multiplizitäten ${code.join(' · ')}`,'scene-card');sceneText(svg,320,235,'≠','scene-number','middle');sceneArrow(svg,310,145,440,210,true);sceneArrow(svg,310,315,440,250,true);sceneBox(svg,455,145,220,150,`gemeinsamer Träger ${fmt(clock.dimension)}`,'nur für die isolierte C₄-Wirkung','scene-card');sceneText(svg,800,80,'gemeinsame Multiplizitäten','scene-label','middle');common.forEach((value,index)=>{const x=710+index*62,height=35*Number(value||0);svg.append(svgEl('rect',{x,y:260-height,width:42,height,rx:4,fill:index%2?'#7160a5':'#124f42'}));sceneText(svg,x+21,282,`${labels[index]}: ${value}`,'scene-small','middle');});sceneText(svg,500,415,`α⁻¹ = ${fmt(data.alpha_inverse,13)}`,'scene-number','middle');(data.predictions||[]).forEach((label,index)=>{const x=180+index*160;svg.append(svgEl('rect',{x,y:452,width:130,height:42,rx:21,fill:index<2?'#dcece6':'#eeeaf7',stroke:'#b8c8c0'}));sceneText(svg,x+65,478,label,'scene-label','middle');});}

function sceneClosure(svg,data){const steps=data.steps||[],statuses=data.statuses||[];sceneText(svg,500,48,'Der tragende Pfad zur Gesamtantwort','scene-title','middle');steps.forEach((step,index)=>{const x=70+index*185,y=190,status=statuses[index]||'open';if(index)sceneArrow(svg,x-55,y,x-18,y,status==='open');svg.append(svgEl('circle',{cx:x,cy:y,r:34,fill:status==='conditional'?'#a96508':'#fff',stroke:status==='conditional'?'#a96508':'#a33c35','stroke-width':4,'stroke-dasharray':status==='open'?'7 5':''}));sceneText(svg,x,y+6,index+1,'scene-number','middle');sceneLines(svg,step,x,265,20,'scene-label','middle',16);sceneText(svg,x,350,statusLabel(status),'scene-small','middle');});sceneBox(svg,240,405,520,85,'Eine Quelle · ein Zustand · ein Grenzvertrag','muss alle acht Tore T1–T8 zugleich erfüllen','scene-card');}

const TOUR_SCENES={big_picture:sceneBigPicture,boundary:sceneBoundary,alphabet:sceneAlphabet,protected_code:sceneProtectedCode,information:sceneInformation,response:sceneResponse,quartic:sceneQuartic,binding:sceneBinding,recursion:sceneRecursion,source:sceneSource,normalization:sceneNormalization,space:sceneSpace,assembly:sceneAssembly,physics:scenePhysics,closure:sceneClosure};

function sceneDataForDisplay(value,key='') {
  if(Array.isArray(value)){
    const nested=value.reduce((sum,item)=>sum+(Array.isArray(item)?item.length:1),0);
    if(key==='amplitudes')return {shape:`${value.length} × ${Array.isArray(value[0])?value[0].length:0}`,note:'Komplexe Amplituden vollständig im Rechenlauf; hier nur die Dimension.'};
    if(value.length>80){const numeric=value.map(Number).filter(Number.isFinite);return {count:value.length,min:numeric.length?Math.min(...numeric):undefined,max:numeric.length?Math.max(...numeric):undefined,note:'Vollständiges Array im Export.'};}
    if(nested>160)return {shape:`${value.length} × ${Array.isArray(value[0])?value[0].length:'variabel'}`,preview:value.slice(0,2).map(item=>sceneDataForDisplay(item)),note:'Vollständige Matrix im Export.'};
    return value.map(item=>sceneDataForDisplay(item));
  }
  if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([childKey,child])=>[childKey,sceneDataForDisplay(child,childKey)]));
  return value;
}

function renderTourScene(root,chapter) {
  if(!root)return;root.innerHTML='';root.dataset.lens=app.tourLens;let data=chapter.visual?.data||{};if(chapter.id==='source'){const live=app.snapshot?.stages?.find(stage=>stage.id==='sourcechannel')?.visual?.data||{};data={...data,readout_labels:live.readout_labels||data.readout_labels,phase_b:app.snapshot?.config?.phase_b};}const svg=makeTourSVG(chapter),renderer=TOUR_SCENES[chapter.visual?.type]||TOUR_SCENES[chapter.id];
  if(renderer)renderer(svg,data,chapter);else sceneBigPicture(svg,{branches:[{title:'Eingang',steps:[chapter.before]},{title:'Operation',steps:[chapter.action]}],meeting:chapter.after,destination:chapter.contribution,destination_status:chapter.status});
  root.append(svg);const lens=document.createElement('span');lens.className='tour-scene-lens';lens.textContent=`Blick: ${TOUR_LENSES[app.tourLens]}`;root.append(lens);const raw=document.createElement('details');raw.innerHTML=`<summary>Berechnete Szenendaten</summary><pre class="formula">${escapeHTML(JSON.stringify(sceneDataForDisplay(data),null,2))}</pre>`;root.append(raw);
}

function renderJourney() {
  const stages=app.snapshot?.stages||[], list=$("#journey-list"), card=$("#journey-card");
  if(!stages.length){card.innerHTML='<div class="empty-state">Der Ablauf wird geladen …</div>';return;}
  app.journeyIndex=Math.max(0,Math.min(app.journeyIndex,stages.length-1));
  list.innerHTML=stages.map((stage,index)=>`<li><button type="button" class="${index===app.journeyIndex?'is-active':''}" data-journey-index="${index}" ${index===app.journeyIndex?'aria-current="step"':''}><small>${String(index+1).padStart(2,'0')} · ${escapeHTML(KINDS[stage.kind]?.label||stage.kind)}</small><br>${escapeHTML(stageName(stage))}</button></li>`).join('');
  $$('[data-journey-index]',list).forEach(button=>button.addEventListener('click',()=>{app.journeyIndex=Number(button.dataset.journeyIndex);app.selected=stages[app.journeyIndex].id;renderJourney();renderMap();}));
  renderDetailInto(card,stages[app.journeyIndex],true);
  $("#journey-position").textContent=`${app.journeyIndex+1} / ${stages.length}`;
  $("#journey-prev").disabled=app.journeyIndex===0; $("#journey-next").disabled=app.journeyIndex===stages.length-1;
  list.querySelector('.is-active')?.scrollIntoView({block:'nearest',inline:'nearest'});
}

function short(value,limit=150){const text=String(value??'');return text.length>limit?`${text.slice(0,limit-1)}…`:text;}
function dateText(value){if(!value)return '–';const date=new Date(value);return Number.isNaN(date.valueOf())?String(value):date.toLocaleString('de-DE');}
function localSource(item){return (item.sources||[]).find(source=>source.path&&!source.path.startsWith('/'))||(item.path&&!item.path.startsWith('/')?{path:item.path,line:1}:null);}

function fillSelect(node,values,label) {
  const current=node.value, unique=[...new Set(values.filter(Boolean).map(String))].sort((a,b)=>a.localeCompare(b,'de'));
  node.innerHTML=`<option value="">${escapeHTML(label)}</option>`+unique.map(value=>`<option value="${escapeHTML(value)}">${escapeHTML(short(value,110))}</option>`).join('');
  if(unique.includes(current))node.value=current;
}

async function loadCatalog(refresh=false) {
  if(app.catalog&&!refresh){renderCatalog();return;}
  const feedback=$("#catalog-feedback"), button=$("#catalog-refresh"); button.disabled=true; feedback.textContent=refresh?'Belegbestand wird neu eingelesen …':'Belegbestand wird geladen …';
  try{
    const catalog=await api(`/api/catalog${refresh?'?refresh=1':''}`);
    if(catalog.loading){feedback.textContent='Katalog wird im Hintergrund aufgebaut …';setTimeout(()=>loadCatalog(refresh),900);return;}
    if(catalog.error)throw new Error(catalog.error);
    app.catalog=catalog; app.catalogPage=0;
    fillSelect($("#evidence-type"),catalog.items.map(item=>item.type),'Alle Typen');
    fillSelect($("#evidence-status"),catalog.items.map(item=>item.original_status||item.status),'Alle Status');
    fillSelect($("#evidence-stage"),catalog.stage_ids||[],'Alle Schritte');
    renderCatalog(); await loadRuns(); feedback.textContent=`Stand ${dateText(catalog.generated_at)}`;
  }catch(error){$("#evidence-results").innerHTML=`<div class="error-state">${escapeHTML(error.message)}</div>`;feedback.textContent='Katalog konnte nicht geladen werden.';}
  finally{button.disabled=false;}
}

function filteredCatalog() {
  const query=$("#evidence-search").value.trim().toLocaleLowerCase('de'),type=$("#evidence-type").value,status=$("#evidence-status").value,stage=$("#evidence-stage").value;
  return (app.catalog?.items||[]).filter(item=>{
    if(type&&item.type!==type)return false;if(status&&(item.original_status||item.status)!==status)return false;if(stage&&!(item.stage_ids||[]).includes(stage))return false;
    if(!query)return true; const hay=[item.id,item.title,item.description,item.path,item.status,item.verdict,item.last_run?.round,item.last_run?.status,...(item.claims||[]),...(item.scripts||[])].join(' ').toLocaleLowerCase('de'); return hay.includes(query);
  });
}

function renderCatalog() {
  if(!app.catalog)return;
  const summary=app.catalog.summary||{},counts=summary.counts||{},items=filteredCatalog(),pages=Math.max(1,Math.ceil(items.length/app.evidencePageSize));app.catalogPage=Math.min(app.catalogPage,pages-1);
  $("#evidence-summary").innerHTML=`<div class="metric-card"><strong>${fmt(summary.items||0)}</strong><span>Katalogeinträge</span></div><div class="metric-card"><strong>${fmt(counts.script||0)}</strong><span>Prüfmodule</span></div><div class="metric-card"><strong>${fmt(summary.source_counts?.experiment_units??((counts.experiment||0)+(counts.contract||0)))}</strong><span>Versuchseinheiten</span></div><div class="metric-card"><strong>${fmt(summary.source_counts?.lean_source_files||0)}</strong><span>Lean-Quelldateien</span></div>`;
  const start=app.catalogPage*app.evidencePageSize,pageItems=items.slice(start,start+app.evidencePageSize);
  $("#evidence-count").textContent=`${fmt(items.length)} Treffer · ${items.length?`${fmt(start+1)}–${fmt(Math.min(start+pageItems.length,items.length))}`:'keine Einträge'}`;
  $("#evidence-results").innerHTML=pageItems.length?pageItems.map(item=>{
    const source=localSource(item),runtime=item.last_run,runStatus=runtime?.status||item.execution_status||'nicht in diesem Explorer ausgeführt',freshClass=['passed','complete','executed'].includes(runStatus)?'fresh-pass':['failed','timeout'].includes(runStatus)?'fresh-fail':'fresh-none';
    const checked=runtime&&Number.isFinite(Number(runtime.checks_passed))?Number(runtime.checks_passed)+Number(runtime.checks_failed||0):null;
    const freshDetail=runtime?`${runtime.round?`${runtime.round} · `:''}${runStatus}${checked!==null?` · ${fmt(runtime.checks_passed)}/${fmt(checked)} ${runtime.scope==='rh_fast_probe_exit_gate'?'Modul-Ausführung':'Prüfungen'}`:''}${runtime.completed_at||runtime.finished_at?` · ${dateText(runtime.completed_at||runtime.finished_at)}`:''}`:runStatus;
    const module=item.type==='script'&&/^script:v\d+_[A-Za-z0-9_]+$/.test(item.id)?item.id.slice(7):null;
    return `<article class="evidence-row" data-evidence-id="${escapeHTML(item.id)}"><div><span class="evidence-id">${escapeHTML(item.id)}</span><h3>${escapeHTML(item.title||item.id)}</h3><div class="chips"><span class="chip">${escapeHTML(item.type)}</span>${(item.stage_ids||[]).slice(0,4).map(id=>`<span class="chip" title="Automatische thematische Zuordnung; keine zusätzliche Beweiskante">${escapeHTML(stageName(id))}</span>`).join('')}</div></div><div><p>${escapeHTML(short(item.description||item.scope||item.verdict||'Keine Kurzbeschreibung.',520))}</p></div><div class="status-pair"><span><b>Originalstatus</b><span title="${escapeHTML(item.original_status||item.status||'')}">${escapeHTML(short(item.original_status||item.status||'unbekannt',180))}</span></span><span><b>Frische Ausführung</b><span class="${freshClass}">${escapeHTML(short(freshDetail,180))}</span></span></div><div class="row-actions">${source?`<a class="mini-button" href="${sourceURL(source)}" target="_blank" rel="noopener">Quelle ↗</a>`:''}${runtime?.log_path?`<a class="mini-button" href="${sourceURL({path:runtime.log_path,line:runtime.log_line||1})}" target="_blank" rel="noopener">Laufprotokoll ↗</a>`:''}<button class="mini-button graph-button" type="button">Beziehungen</button>${module?`<button class="mini-button verify-button" type="button" data-module="${escapeHTML(module)}">Neu prüfen</button>`:''}</div></article>`;
  }).join(''):'<div class="empty-state">Keine Einträge entsprechen den Filtern.</div>';
  $$('.graph-button',$("#evidence-results")).forEach(button=>button.addEventListener('click',()=>toggleRelations(button.closest('.evidence-row'))));
  $$('.verify-button',$("#evidence-results")).forEach(button=>button.addEventListener('click',()=>runVerification(button.dataset.module,button)));
  renderPagination(pages);
}

function renderPagination(pages) {
  const root=$("#evidence-pagination"); if(pages<=1){root.innerHTML='';return;}
  const current=app.catalogPage,shown=new Set([0,pages-1,current-2,current-1,current,current+1,current+2]);let html=`<button type="button" data-page="${current-1}" ${current===0?'disabled':''} aria-label="Vorherige Seite">←</button>`;let previous=-2;
  [...shown].filter(page=>page>=0&&page<pages).sort((a,b)=>a-b).forEach(page=>{if(page>previous+1)html+='<span aria-hidden="true">…</span>';html+=`<button type="button" data-page="${page}" ${page===current?'aria-current="page"':''}>${page+1}</button>`;previous=page;});
  html+=`<button type="button" data-page="${current+1}" ${current===pages-1?'disabled':''} aria-label="Nächste Seite">→</button>`;root.innerHTML=html;
  $$('button[data-page]',root).forEach(button=>button.addEventListener('click',()=>{const page=Number(button.dataset.page);if(page>=0&&page<pages){app.catalogPage=page;renderCatalog();$("#evidence-results").scrollIntoView({block:'start'});}}));
}

function relationGraphic(data,centerId) {
  const svg=svgEl('svg',{viewBox:'0 0 760 330',role:'img','aria-label':'Direkte Beziehungen im Theoriegraphen'}),nodes=data.nodes||[],edges=data.edges||[],center=nodes.find(node=>node.id===centerId)||nodes[0],placed=new Map();
  if(!center)return svg;placed.set(center.id,{x:380,y:165,node:center});const others=nodes.filter(node=>node.id!==center.id);
  others.forEach((node,index)=>{const angle=2*Math.PI*index/Math.max(others.length,1)-Math.PI/2,ring=others.length>14?(index%2?136:102):126;placed.set(node.id,{x:380+Math.cos(angle)*ring*2.2,y:165+Math.sin(angle)*ring,node});});
  edges.forEach(edge=>{const a=placed.get(edge.source),b=placed.get(edge.target);if(!a||!b)return;svg.append(svgEl('line',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:'#aebdb6','stroke-width':1.3}));});
  placed.forEach(({x,y,node})=>{const isCenter=node.id===center.id;svg.append(svgEl('circle',{cx:x,cy:y,r:isCenter?11:6,fill:isCenter?'#7160a5':'#124f42'}));svg.append(svgEl('text',{x:x+(isCenter?15:9),y:y+4,class:'chart-note'},short(node.label||node.id,28)));});return svg;
}

async function toggleRelations(row) {
  const existing=$('.relation-panel',row);if(existing){existing.remove();return;}const panel=document.createElement('section');panel.className='relation-panel';panel.innerHTML='<p>Direkte Beziehungen werden geladen …</p>';row.append(panel);
  try{const data=await api(`/api/relations?id=${encodeURIComponent(row.dataset.evidenceId)}&limit=30`);if(!data.nodes?.length){panel.innerHTML=`<p>${escapeHTML(data.scope||'Keine direkte Beziehung im erfassten Theoriegraphen.')}</p>`;return;}panel.innerHTML=`<h4>Direkte Nachbarschaft · ${fmt(data.total)} Kanten</h4><p>${escapeHTML(data.scope||'')}</p>`;panel.append(relationGraphic(data,row.dataset.evidenceId));const list=document.createElement('ul');list.className='relation-list';list.innerHTML=(data.edges||[]).map(edge=>`<li><code>${escapeHTML(edge.source)}</code> — ${escapeHTML(edge.relation)} → <code>${escapeHTML(edge.target)}</code></li>`).join('');panel.append(list);}catch(error){panel.innerHTML=`<div class="error-state">${escapeHTML(error.message)}</div>`;}
}

async function loadRuns() {
  try{const data=await api('/api/runs'),runs=[...(data.runs||[]).filter(run=>run.file.endsWith('_summary.json')).reverse(),...(data.runs||[]).filter(run=>!run.file.endsWith('_summary.json')).slice(-12).reverse()];$("#run-history").innerHTML=runs.length?runs.map(run=>{const result=run.data?.result||run.data||{},counts=result.counts||{},passed=result.checks_passed??counts.checks_passed??counts.rh_checks_passed,failed=result.checks_failed??counts.checks_failed??counts.rh_checks_failed,total=passed!==undefined?Number(passed)+Number(failed||0):null;
    const progress=counts.modules_total?`${fmt(counts.modules_completed||0)}/${fmt(counts.modules_total)} Module`:counts.stages_total?`${fmt(counts.stages_completed||0)}/${fmt(counts.stages_total)} Stufen`:null;
    const stages=result.stages&&!Array.isArray(result.stages)?Object.entries(result.stages).map(([name,status])=>`<span class="chip">${escapeHTML(name)}: ${escapeHTML(status)}</span>`).join(''):'';
    const facts=[total!==null?`${fmt(passed)}/${fmt(total)} Prüfungen`:null,progress,result.count_source?`Zählung: ${result.count_source}`:null].filter(Boolean).join(' · ');
    return `<details class="run-card"><summary><strong>${escapeHTML(result.module||run.file)}</strong> · ${escapeHTML(result.status||'gespeichert')} · ${escapeHTML(dateText(result.finished_at||result.completed_at||result.generated_at))}</summary>${facts?`<p><strong>${escapeHTML(facts)}</strong></p>`:''}${stages?`<div class="chips">${stages}</div>`:''}${result.scope?`<p>${escapeHTML(result.scope)}</p>`:''}${result.log_path?`<p><a class="source-link" href="${sourceURL({path:result.log_path,line:1})}" target="_blank" rel="noopener">Laufprotokoll öffnen ↗</a></p>`:''}${result.output?`<pre>${escapeHTML(result.output)}</pre>`:''}</details>`;}).join(''):'<div class="empty-state">Noch keine einzelnen Prüfläufe gespeichert.</div>';}catch(error){$("#run-history").innerHTML=`<div class="error-state">${escapeHTML(error.message)}</div>`;}
}

async function runVerification(module,button) {
  button.disabled=true;button.textContent='Läuft …';
  try{const job=await api('/api/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({module})});await waitForJob(job.id);toast(`${module} wurde abgeschlossen.`);await loadCatalog(true);}catch(error){toast(`Prüfung fehlgeschlagen: ${error.message}`);}finally{button.disabled=false;button.textContent='Neu prüfen';}
}

async function waitForJob(id,onProgress) {
  for(let attempt=0;attempt<360;attempt++){const job=await api(`/api/jobs/${encodeURIComponent(id)}`);onProgress?.(job);if(job.status==='complete')return job;if(job.status==='failed')throw new Error(job.error||'Berechnung fehlgeschlagen.');await new Promise(resolve=>setTimeout(resolve,700));}throw new Error('Der Lauf antwortet noch nicht.');
}

async function loadLean(force=false) {
  if(app.lean&&!force){renderLean();return;}$("#lean-content").innerHTML='<div class="skeleton summary-skeleton"></div>';
  try{app.lean=await api('/api/lean');renderLeanOverview();renderLean();}catch(error){$("#lean-content").innerHTML=`<div class="error-state">${escapeHTML(error.message)}</div>`;}
}

function renderLeanOverview() {
  const summary=app.lean?.summary||{},replay=app.lean?.latest_replay,exports=replay?.automatic_exports||{};
  $("#lean-overview").innerHTML=`<div class="metric-card"><strong>${fmt(summary.files||0)}</strong><span>Lean-Quelldateien</span></div><div class="metric-card"><strong>${fmt(summary.declarations||0)}</strong><span>Deklarationen</span></div><div class="metric-card"><strong>${fmt(summary.counts?.theorem||0)}</strong><span>Theoreme</span></div><div class="metric-card"><strong>${fmt(summary.counts?.axiom||0)}</strong><span>explizite Axiome</span></div><div class="metric-card"><strong>${fmt(summary.counts?.sorry_sites||0)}</strong><span>offene sorry-Stellen</span></div><div class="metric-card"><strong>${fmt(exports.executed||0)}/${fmt(exports.count||0)}</strong><span>automatisch ausgeführte Definitionen</span></div>`;
}

function renderReplay() {
  const replay=app.lean?.latest_replay;if(!replay)return '<div class="empty-state">Noch kein Lean-Lauf vorhanden.</div>';const origin=replay.original_definition;
  const phases=(replay.phases||[]).map(phase=>`<article class="phase-card ${escapeHTML(phase.status)}"><h3>${escapeHTML(phase.name)}</h3><p>${escapeHTML(phase.status)} · ${fmt(phase.elapsed_seconds)} s</p>${phase.path?`<a class="source-link" href="${sourceURL({path:phase.path,line:1})}" target="_blank" rel="noopener">Laufprotokoll öffnen ↗</a>`:''}</article>`).join('');
  const checks=(replay.cross_checks||[]).map(check=>`<article class="cross-card ${check.ok?'passed':'failed'}"><h3>${check.ok?'✓':'!'} ${escapeHTML(check.name)}</h3><p>Lean ${escapeHTML(fmt(check.lean))}<br>Python ${escapeHTML(fmt(check.python))}</p></article>`).join('');
  const counts=app.lean?.summary?.counts||{};
  return `<section><h2>Letzter Original-Lauf: ${escapeHTML(replay.status)}</h2><p>${escapeHTML(replay.scope||'')}</p><p><strong>Inventargrenze:</strong> Ein grüner Build typprüft den angegebenen Stand. Das Inventar weist zugleich ${fmt(counts.axiom||0)} explizite Axiome und ${fmt(counts.sorry_sites||0)} offene <code>sorry</code>-Stellen aus; sie werden dadurch nicht geschlossen.</p><p><strong>Originaldefinition:</strong> <a href="${sourceURL(origin)}" target="_blank" rel="noopener">${escapeHTML(origin?.path||'–')} · Zeile ${fmt(origin?.line)}</a><br><strong>Quellhash:</strong> <code>${escapeHTML(origin?.sha256||'–')}</code><br><strong>Ausgeführt:</strong> ${escapeHTML(dateText(replay.finished_at))}</p><div class="phase-grid">${phases}</div><h2>Lean ↔ Python</h2><div class="cross-checks">${checks}</div></section>`;
}

function renderLeanModules(classifications) {
  const modules=(app.lean?.modules||[]).map(module=>({...module,declarations:(module.declarations||[]).filter(decl=>classifications.includes(decl.classification))})).filter(module=>module.declarations.length);
  return `<p>${fmt(modules.reduce((sum,module)=>sum+module.declarations.length,0))} Deklarationen in ${fmt(modules.length)} Quelldateien. Die Signaturen stammen direkt aus dem statischen Inventar; Kompilierbarkeit entscheidet der Lean-Lauf.</p>`+modules.map(module=>{const sorry=(module.sorry_lines||[]);return `<details class="lean-module"><summary>${escapeHTML(module.module)} · ${fmt(module.declarations.length)} Einträge${sorry.length?` · ${fmt(sorry.length)} sorry`:''}</summary><p><a href="${sourceURL({path:module.path,line:1})}" target="_blank" rel="noopener">Originalquelle öffnen ↗</a> · <code>${escapeHTML(module.sha256.slice(0,16))}…</code>${sorry.length?`<br><strong>Offene Stellen:</strong> ${sorry.map(line=>`<a href="${sourceURL({path:module.path,line:Number(line.line??line)})}" target="_blank" rel="noopener">Zeile ${fmt(line.line??line)}</a>`).join(', ')}`:''}</p>${module.declarations.map(decl=>`<div class="declaration"><span class="chip">${escapeHTML(decl.kind)}</span><code>${escapeHTML(decl.signature)}</code><a href="${sourceURL({path:module.path,line:decl.line})}" target="_blank" rel="noopener">Zeile ${fmt(decl.line)} ↗</a></div>`).join('')}</details>`;}).join('');
}

function renderLeanExports() {
  const exports=app.lean?.latest_replay?.automatic_exports,candidates=exports?.candidates||[];if(!exports)return '<div class="empty-state">Noch keine automatischen Exporte vorhanden.</div>';
  return `<p><strong>${fmt(exports.executed)} von ${fmt(exports.count)}</strong> geeigneten Definitionen wurden direkt aus ihren Lean-Modulen ausgeführt. Zwei Definitionen benötigen zuerst ein konkretes Objekt ihres Lean-Typs.</p><p>${escapeHTML(exports.scope||'')}</p>`+candidates.map(item=>`<article class="lean-module"><div class="declaration"><span class="chip ${item.status==='executed'?'fresh-pass':'fresh-none'}">${escapeHTML(item.status)}</span><div><strong>${escapeHTML(item.name)}</strong><br><code>${escapeHTML(item.status==='executed'?fmt(item.value):item.reason||'')}</code>${item.required_input_type?`<br><small>Benötigt: ${escapeHTML(item.required_input_type)}</small>`:''}</div><a href="${sourceURL({path:item.path,line:item.line})}" target="_blank" rel="noopener">Original · Zeile ${fmt(item.line)} ↗</a></div></article>`).join('');
}

function renderLean() {
  if(!app.lean)return;let html='';
  if(app.leanTab==='replay')html=renderReplay();else if(app.leanTab==='proof')html=renderLeanModules(['proof']);else if(app.leanTab==='definition')html=renderLeanModules(['definition','computation_candidate']);else if(app.leanTab==='noncomputable')html=renderLeanModules(['noncomputable','assumption']);else html=renderLeanExports();
  $("#lean-content").innerHTML=html;
}

async function runPipeline(config) {
  const button=$("#run-button"),feedback=$("#run-feedback"),tourButtons=$$('.tour-live-controls button');button.disabled=true;tourButtons.forEach(node=>node.disabled=true);$('.tour-live-controls')?.setAttribute('aria-busy','true');feedback.textContent='Python-Ablauf läuft …';setHeader('loading','Berechnung läuft');
  try{const queued=await api('/api/run',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({config})});const job=await waitForJob(queued.id,current=>{feedback.textContent=current.status==='queued'?'Lauf wartet …':'Schritte werden berechnet …';});applySnapshot(job.result);feedback.textContent=`Fertig · ${fmt(job.result.summary.elapsed_ms)} ms`;}catch(error){feedback.textContent=error.message;setHeader('bad','Berechnung fehlgeschlagen');toast(error.message);}finally{button.disabled=false;if(tourButtons.some(node=>node.isConnected))renderTour();}
}

async function runLean() {
  const button=$("#lean-run"),feedback=$("#lean-feedback");button.disabled=true;feedback.textContent='Lean-Projekte werden gebaut und Definitionen ausgeführt …';
  try{const queued=await api('/api/lean/run',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});await waitForJob(queued.id,current=>{feedback.textContent=current.status==='queued'?'Lean-Lauf wartet …':'Lean kompiliert und führt Originaldefinitionen aus …';});app.lean=null;await loadLean(true);feedback.textContent=`Fertig · ${dateText(app.lean?.latest_replay?.finished_at)}`;}catch(error){feedback.textContent=error.message;toast(error.message);}finally{button.disabled=false;}
}

function bindEvents() {
  $$('.nav-link').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();setView(link.dataset.view);}));
  $$('.tour-shortcuts a').forEach(link=>link.addEventListener('click',event=>{
    event.preventDefault();setView('tour',false,link.hash.slice(1));
  }));
  window.addEventListener('hashchange',()=>{const route=location.hash.slice(1),view=VIEW_ROUTES[route];if(!view)return;if(view!==app.activeView)setView(view,false,route);else{if(view==='tour')renderTour();scrollTourRoute(route);}});
  $('.brand').addEventListener('click',event=>{event.preventDefault();setView('overview');});
  $('#start-tour').addEventListener('click',()=>setView('tour'));$('#start-journey').addEventListener('click',()=>setView('journey'));$$('[data-scroll]').forEach(button=>button.addEventListener('click',()=>$("#"+button.dataset.scroll)?.scrollIntoView({behavior:'smooth'})));
  ['clock-step','transfer-steps','recursion-depth','efolds','phase-b'].forEach(id=>$(`#${id}`).addEventListener('input',updateControlLabels));
  $('#control-form').addEventListener('submit',event=>{event.preventDefault();runPipeline(getConfig());});
  $('#reset-button').addEventListener('click',()=>{configureControls(app.defaults||{});runPipeline(app.defaults||{});});
  $('#journey-prev').addEventListener('click',()=>{if(app.journeyIndex>0){app.journeyIndex--;app.selected=app.snapshot.stages[app.journeyIndex].id;renderJourney();renderMap();}});
  $('#journey-next').addEventListener('click',()=>{if(app.journeyIndex<(app.snapshot?.stages.length||1)-1){app.journeyIndex++;app.selected=app.snapshot.stages[app.journeyIndex].id;renderJourney();renderMap();}});
  $('#tour-prev').addEventListener('click',()=>selectTourChapter(app.tourIndex-1));$('#tour-next').addEventListener('click',()=>selectTourChapter(app.tourIndex+1));
  const lensTabs=$$('.tour-lenses [role="tab"]');lensTabs.forEach((tab,index)=>{tab.addEventListener('click',()=>selectTourLens(tab));tab.addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;event.preventDefault();const next=event.key==='Home'?0:event.key==='End'?lensTabs.length-1:(index+(event.key==='ArrowRight'?1:-1)+lensTabs.length)%lensTabs.length;lensTabs[next].focus();selectTourLens(lensTabs[next]);});});
  let searchTimer;$('#evidence-search').addEventListener('input',()=>{clearTimeout(searchTimer);searchTimer=setTimeout(()=>{app.catalogPage=0;renderCatalog();},180);});
  ['evidence-type','evidence-status','evidence-stage'].forEach(id=>$(`#${id}`).addEventListener('change',()=>{app.catalogPage=0;renderCatalog();}));
  $('#catalog-refresh').addEventListener('click',()=>loadCatalog(true));$('#lean-run').addEventListener('click',runLean);
  const tabs=$$('.lean-tabs [role="tab"]');tabs.forEach((tab,index)=>{tab.addEventListener('click',()=>selectLeanTab(tab));tab.addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;event.preventDefault();let next=event.key==='Home'?0:event.key==='End'?tabs.length-1:(index+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;tabs[next].focus();selectLeanTab(tabs[next]);});});
}

function selectLeanTab(tab) {app.leanTab=tab.dataset.leanTab;$$('.lean-tabs [role="tab"]').forEach(node=>node.setAttribute('aria-selected',String(node===tab)));renderLean();}
function selectTourLens(tab) {app.tourLens=tab.dataset.tourLens;$$('.tour-lenses [role="tab"]').forEach(node=>node.setAttribute('aria-selected',String(node===tab)));renderTour();}

async function initialize() {
  bindEvents();const route=location.hash.slice(1),view=VIEW_ROUTES[route]||'overview';setView(view,false,VIEW_ROUTES[route]?route:null);
  try{const state=await api('/api/state');app.defaults=state.defaults||{};configureControls(state.latest?.config||app.defaults);if(state.latest)applySnapshot(state.latest);else{setHeader('loading','Erster Lauf läuft');const running=(state.jobs||[]).find(job=>job.kind==='pipeline'&&['queued','running'].includes(job.status));if(running){const job=await waitForJob(running.id);applySnapshot(job.result);}else await runPipeline(app.defaults);}}
  catch(error){setHeader('bad','Backend nicht erreichbar');$('#system-map-wrap').innerHTML=`<div class="error-state">${escapeHTML(error.message)}</div>`;toast(`Start fehlgeschlagen: ${error.message}`);}
}

initialize();
