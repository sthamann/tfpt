import Link from "next/link";

export type CatalogModule = {
  id: string;
  filename: string;
  path: string;
  cluster: string;
  synopsis: string;
  sourceHref: string;
  snapshotSourceHref?:string;
  pubMirrorMatchesSnapshot?:boolean;
  linkedClaimIds: string[];
  sectionIds: string[];
};

type Props = { modules: CatalogModule[]; query?: string; cluster?: string; requestedPage?: string };
function moduleLabel(module: CatalogModule) {
  const words = module.filename.replace(/^v\d+_/, "").replace(/\.py$/, "").replaceAll("_", " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
}

export function ModuleCatalog({ modules, query = "", cluster = "", requestedPage }: Props) {
  const needle = query.trim().toLowerCase();
  const clusters = [...new Set(modules.map(module => module.cluster))].sort();
  const filtered = modules.filter(module => (!cluster || module.cluster === cluster) && (!needle || [module.filename, module.synopsis, module.cluster, ...module.linkedClaimIds, ...module.sectionIds].join(" ").toLowerCase().includes(needle)));
  const pageCount = Math.max(1, Math.ceil(filtered.length / 20));
  const parsedPage = Number.parseInt(requestedPage || "1", 10);
  const page = Math.max(1, Math.min(pageCount, Number.isFinite(parsedPage) ? parsedPage : 1));
  const rows = filtered.slice((page - 1) * 20, page * 20);
  const pageHref = (target: number) => {
    const params = new URLSearchParams();
    if (query) params.set("moduleQuery", query);
    if (cluster) params.set("moduleCluster", cluster);
    params.set("catalogPage", String(target));
    return `/verification?${params.toString()}#module-catalog`;
  };
  return <div>
    <p className="mt-4 max-w-3xl leading-relaxed">Search all {modules.length} registered Python modules by subject, filename, claim or source section. This catalogue records source presence and links. It does not report a new execution or a passing result for every module.</p>
    <form method="get" action="/verification#module-catalog" className="reference-form" role="search" aria-label="Verification module catalogue">
      <div><label htmlFor="module-query">Find a verification module</label><input id="module-query" type="search" name="moduleQuery" defaultValue={query} placeholder="E8 glue, alpha, v1, claim ID…" /></div>
      <div><label htmlFor="module-cluster">Subject</label><select id="module-cluster" name="moduleCluster" defaultValue={cluster}><option value="">All subjects</option>{clusters.map(name => <option key={name} value={name}>{name.replaceAll("_", " ")}</option>)}</select></div>
      <button type="submit">Search modules</button>
    </form>
    <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-300 pb-4 text-sm">
      <p role="status">{filtered.length} matching {filtered.length === 1 ? "module" : "modules"}{filtered.length > 0 ? ` · showing ${(page - 1) * 20 + 1}–${Math.min(page * 20, filtered.length)}` : ""}</p>
      {(query || cluster) && <Link href="/verification#module-catalog" className="inline-flex min-h-11 items-center text-blue-800 underline underline-offset-4">Clear filters</Link>}
    </div>
    {rows.length === 0 ? <p className="py-8">No module matches these filters. Try a shorter subject or filename, or clear the subject filter.</p> : <div>
      {rows.map(module => <article key={module.id} id={`module-${module.id}`} className="scroll-mt-24 border-b border-slate-300 py-5">
        <h3 className="font-serif text-xl font-semibold text-slate-950">{moduleLabel(module)}</h3>
        <p className="mt-1 break-words text-sm text-slate-600">{module.filename} · {module.cluster.replaceAll("_", " ")}</p>
        <details className="mt-2">
          <summary className="cursor-pointer py-2 font-medium text-blue-800">Read the original description and evidence links</summary>
          <p className="mt-3 max-w-3xl whitespace-pre-line text-sm leading-relaxed">{module.synopsis || "No descriptive synopsis is recorded for this module. Inspect the original source for its statement and checks."}</p>
          {module.pubMirrorMatchesSnapshot===false&&<p className="reference-note">This research snapshot and the older executable publication are different versions. Open the source record to inspect both.</p>}
          <a href={module.sourceHref} className="mt-3 inline-flex min-h-11 items-center text-sm text-blue-800 underline underline-offset-4">Read the original Python source</a>
          <dl className="mt-4 text-sm leading-relaxed">
            <div><dt className="font-semibold">Linked claims</dt><dd>{module.linkedClaimIds.length ? <div className="flex flex-wrap gap-x-5 gap-y-1">{module.linkedClaimIds.map(id => <Link key={id} href={`/results?claim=${encodeURIComponent(id)}`} className="inline-flex min-h-11 items-center break-all text-blue-800 underline underline-offset-4">{id}</Link>)}</div> : "No explicit claim link is recorded."}</dd></div>
            <div><dt className="mt-3 font-semibold">Paper sections</dt><dd>{module.sectionIds.length ? <div className="flex flex-wrap gap-x-5 gap-y-1">{module.sectionIds.map((id, index) => <Link key={id} href={`/documentation?section=${encodeURIComponent(id)}`} className="inline-flex min-h-11 items-center text-blue-800 underline underline-offset-4">Source section {index + 1}</Link>)}</div> : "No explicit paper section link is recorded."}</dd></div>
          </dl>
        </details>
      </article>)}
    </div>}
    <nav className="reference-pagination" aria-label="Module catalogue pages">
      {page > 1 ? <Link href={pageHref(page - 1)}>Previous 20 modules</Link> : <span />}
      <span>Page {page} of {pageCount}</span>
      {page < pageCount ? <Link href={pageHref(page + 1)}>Next 20 modules</Link> : <span />}
    </nav>
  </div>;
}
