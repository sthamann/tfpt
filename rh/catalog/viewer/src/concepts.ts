import type Sigma from "sigma";
import {
  conceptEdgeVisible,
  conceptMatches,
  edgeKey,
  shortestConceptPaths,
} from "./data";
import {
  addConceptNode,
  addTypedEdge,
  conceptEdgeStyle,
  conceptNodeStyle,
  makeGraph,
  mountSigma,
} from "./gl";
import type { AppState } from "./state";

function esc(s: string): string {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}

export function renderConcepts(host: HTMLElement, state: AppState): () => void {
  host.innerHTML = "";
  host.className = "stage concepts-stage";
  const wrap = document.createElement("div");
  wrap.className = "gl-wrap";
  const gaps = document.createElement("aside");
  gaps.className = "gaps-panel";
  const tooltip = document.createElement("div");
  tooltip.className = "tip";
  const pathbar = document.createElement("div");
  pathbar.className = "path-bar";
  host.append(wrap, gaps, pathbar, tooltip);
  paintGaps(gaps, state);

  const graph = makeGraph();
  let sigma: Sigma | null = null;
  let lastKey = "";
  let lastConceptN = -1;

  function rebuildGraph(): void {
    const f = state.conceptFilters;
    const visible = state.bundle.concepts.nodes.filter((n) => conceptMatches(n, f));
    const vis = new Set(visible.map((n) => n.id));
    graph.forEachNode((id) => {
      if (!vis.has(id) && !id.startsWith("sat:")) graph.dropNode(id);
    });
    graph.forEachNode((id) => {
      if (id.startsWith("sat:") && !f.showAttempts) graph.dropNode(id);
    });
    for (const n of visible) {
      if (!graph.hasNode(n.id)) addConceptNode(graph, n);
    }
    const keep = new Set<string>();
    for (const e of state.bundle.concepts.edges) {
      if (!conceptEdgeVisible(e, f, vis)) continue;
      if (e.rel === "USED_BY" || e.rel === "KILLED_BY") {
        if (!f.showAttempts) continue;
        const sid = `sat:${e.dst}`;
        if (!graph.hasNode(sid)) {
          const rec = state.bundle.graph.nodes.find((r) => r.path === e.dst);
          graph.addNode(sid, {
            x: (graph.getNodeAttribute(e.src, "x") as number) + 12,
            y: (graph.getNodeAttribute(e.src, "y") as number) + 8,
            size: 2.2,
            label: rec?.round || e.dst.split("/").pop() || e.dst,
            color: "#5a6270",
            ctype: "METHOD",
            status: rec?.outcome === "KILLED" ? "KILLED_HERE" : "CLASSICAL",
            alive: true,
            sat: true,
            recPath: e.dst,
          });
        }
        const eid = `${e.rel}|${e.src}|${sid}`;
        keep.add(eid);
        if (!graph.hasEdge(eid)) addTypedEdge(graph, eid, e.src, sid, e.rel, { rel: e.rel, strength: e.strength });
        continue;
      }
      const eid = edgeKey(e);
      keep.add(eid);
      if (!graph.hasEdge(eid)) addTypedEdge(graph, eid, e.src, e.dst, e.rel, { rel: e.rel, strength: e.strength });
    }
    graph.forEachEdge((eid) => {
      if (!keep.has(eid)) graph.dropEdge(eid);
    });
  }

  function pickPath(id: string): void {
    const [a] = state.conceptPathEnds;
    if (!a || a === id) {
      state.setPathEnds(id, null, -1, [id], []);
      return;
    }
    const f = state.conceptFilters;
    const visNodes = state.bundle.concepts.nodes.filter((n) => conceptMatches(n, f));
    const vis = new Set(visNodes.map((n) => n.id));
    const edges = state.bundle.concepts.edges.filter((e) => conceptEdgeVisible(e, f, vis));
    const found = shortestConceptPaths(visNodes, edges, a, id, 5, f.avoidKilled);
    const ids = new Set<string>([a, id]);
    const ekeys: string[] = [];
    for (const p of found.paths) {
      p.forEach((x) => ids.add(x));
      for (let i = 0; i < p.length - 1; i++) {
        for (const e of edges) {
          if ((e.src === p[i] && e.dst === p[i + 1]) || (e.dst === p[i] && e.src === p[i + 1])) ekeys.push(edgeKey(e));
        }
      }
    }
    state.setPathEnds(a, id, found.hops, [...ids], ekeys);
  }

  function paintPathBar(): void {
    const [a, b] = state.conceptPathEnds;
    const hops = state.conceptPathHops;
    const an = a ? state.bundle.concepts.nodes.find((n) => n.id === a)?.name || a : "—";
    const bn = b ? state.bundle.concepts.nodes.find((n) => n.id === b)?.name || b : "shift-click second";
    pathbar.innerHTML = `<span>path</span> <strong>${esc(an)}</strong> → <strong>${esc(bn)}</strong> <em>${
      hops < 0 ? (a && b ? "no path ≤ 5" : "shift-click two nodes") : `${hops} hop${hops === 1 ? "" : "s"}`
    }</em>`;
  }

  function attach(): void {
    sigma?.kill();
    sigma = mountSigma(wrap, graph, {
      renderLabels: state.conceptFilters.showLabels,
      nodeReducer: (id, data) =>
        conceptNodeStyle(data, {
          selected: state.selectedConcept?.id === id || state.conceptPathEnds.includes(id),
          path: state.conceptHighlighted.has(id),
          dim: state.conceptHighlighted.size > 0 && !state.conceptHighlighted.has(id) && !data.sat,
        }),
      edgeReducer: (eid, data) => {
        const pathHide = state.conceptPathEdges.size > 0 && !state.conceptPathEdges.has(eid);
        return conceptEdgeStyle(data, { hidden: pathHide });
      },
      onClick: (id, ev) => {
        if (graph.getNodeAttribute(id, "sat")) {
          const path = String(graph.getNodeAttribute(id, "recPath") || "");
          const rec = state.bundle.graph.nodes.find((r) => r.path === path) || null;
          if (rec) {
            state.select(rec);
            state.setView("network");
          }
          return;
        }
        if ("shiftKey" in ev.event.original && (ev.event.original as MouseEvent).shiftKey) {
          pickPath(id);
          return;
        }
        const node = state.bundle.concepts.nodes.find((n) => n.id === id) || null;
        state.selectConcept(node);
      },
      onEnter: (id) => {
        const n = state.bundle.concepts.nodes.find((x) => x.id === id);
        tooltip.hidden = false;
        tooltip.innerHTML = `<strong>${esc(n?.name || id)}</strong><span>${esc(n?.type || "")} · ${esc(n?.status || "")}</span>`;
      },
      onLeave: () => {
        tooltip.hidden = true;
      },
    });
    wrap.addEventListener("mousemove", (ev) => {
      if (tooltip.hidden) return;
      const rect = host.getBoundingClientRect();
      tooltip.style.left = `${ev.clientX - rect.left + 12}px`;
      tooltip.style.top = `${ev.clientY - rect.top + 10}px`;
    });
  }

  function topoKey(): string {
    const f = state.conceptFilters;
    return [
      [...f.types].join(),
      [...f.statuses].join(),
      [...f.relGroups].join(),
      f.minStrength,
      f.aliveOnly,
      f.showAttempts,
      f.query,
      f.showLabels,
    ].join("|");
  }

  function apply(): void {
    const k = topoKey();
    const n = state.bundle.concepts.nodes.length;
    if (k !== lastKey || n !== lastConceptN) {
      lastKey = k;
      if (n !== lastConceptN) paintGaps(gaps, state);
      lastConceptN = n;
      rebuildGraph();
      if (!sigma) attach();
      else {
        sigma.setSetting("renderLabels", state.conceptFilters.showLabels);
        sigma.refresh();
      }
    } else {
      sigma?.refresh();
    }
    paintPathBar();
  }

  const off = state.on(() => {
    if (state.view !== "concepts") return;
    apply();
  });
  apply();
  return () => {
    off();
    sigma?.kill();
    host.innerHTML = "";
  };
}

function paintGaps(host: HTMLElement, state: AppState): void {
  const g = state.bundle.gaps;
  const nameOf = (id: string) => state.bundle.concepts.nodes.find((n) => n.id === id)?.name || id;
  const clickIds = (ids: string[]) => {
    const ekeys: string[] = [];
    for (let i = 0; i < ids.length - 1; i++) {
      for (const e of state.bundle.concepts.edges) {
        if ((e.src === ids[i] && e.dst === ids[i + 1]) || (e.dst === ids[i] && e.src === ids[i + 1])) {
          ekeys.push(edgeKey(e));
        }
      }
    }
    if (ids[0]) {
      const n = state.bundle.concepts.nodes.find((x) => x.id === ids[0]) || null;
      if (n) state.selectedConcept = n;
    }
    state.highlightConceptChain(ids, ekeys);
  };
  host.innerHTML = `<h2>Gaps</h2><p class="muted">Research navigation, not a proof chain. Paths traverse relations in both directions; “alive” is not a demonstrated RH route.</p><p><a href="data/proof_obligations.json" target="_blank" rel="noopener">Open proof obligations (all prerequisites required)</a></p>`;
  const freshness = document.createElement("p");
  freshness.className = "muted";
  freshness.textContent = "Research source snapshot: loading; not yet verified in this view.";
  host.append(freshness);
  fetch("data/research_status.json")
    .then((response) => { if (!response.ok) throw new Error("snapshot unavailable"); return response.json(); })
    .then((s) => {
      if (freshness.isConnected) freshness.textContent = `Snapshot ${s.generated_at}: ${s.source_groups} external research groups; ${s.source_groups_curated} source-reviewed, ${s.source_groups_need_review} awaiting review. File freshness is not proof verification. This is a saved snapshot, not a live scan.`;
    })
    .catch(() => { if (freshness.isConnected) freshness.textContent = "Research source snapshot unavailable; freshness unknown."; });
  const sections: { title: string; open: boolean; rows: { label: string; ids: string[] }[] }[] = [
    { title: "G1 zero attempts", open: true, rows: (g.G1 || []).map((x) => ({ label: `${nameOf(x.id)} · ${x.type}`, ids: [x.id] })) },
    { title: "G2 unused criteria", open: false, rows: (g.G2 || []).map((x) => ({ label: `${nameOf(x.id)} · ${x.status}`, ids: [x.id] })) },
    {
      title: "G3 unobserved pairs",
      open: false,
      rows: (g.G3 || []).map((x) => ({ label: `${nameOf(x.pair[0])} × ${nameOf(x.pair[1])} (${x.attempt_score})`, ids: [...x.pair] })),
    },
    { title: "G4 barriers", open: true, rows: (g.G4 || []).map((x) => ({ label: `${nameOf(x.id)} · killed_by ${x.killed_by}`, ids: [x.id] })) },
    {
      title: "G5 TFPT bridges",
      open: true,
      rows: (g.G5 || []).map((x) => ({
        label: `${nameOf(x.id)}${x.hops != null ? ` · ${x.hops} hops` : " · no path"}`,
        ids: x.path?.length ? x.path : [x.id],
      })),
    },
    {
      title: "G6 open closers",
      open: false,
      rows: (g.G6 || []).map((x) => ({
        label: `${nameOf(x.id)} · ${x.alive_targets}/${x.target_count}`,
        ids: [x.id, ...(x.targets || [])],
      })),
    },
  ];
  for (const sec of sections) {
    const det = document.createElement("details");
    det.open = sec.open;
    det.innerHTML = `<summary>${esc(sec.title)} <em>${sec.rows.length}</em></summary>`;
    const ul = document.createElement("ul");
    for (const row of sec.rows.slice(0, 80)) {
      const li = document.createElement("li");
      const b = document.createElement("button");
      b.type = "button";
      b.textContent = row.label;
      b.addEventListener("click", () => clickIds(row.ids));
      li.append(b);
      ul.append(li);
    }
    det.append(ul);
    host.append(det);
  }
}

export function conceptSvgEl(_host: HTMLElement): SVGSVGElement | null {
  return null;
}
