import Link from "next/link";
import { researchInventory } from "@/lib/research";
const kindLabel: Record<string,string> = { established_scoped: "Established within the stated premises", conditional: "Conditional result", excluded_scoped: "Excluded in the stated class" };

export default async function RawResearchRecords({ searchParams }: { searchParams: Promise<Record<string,string | string[] | undefined>> }) {
  const params = await searchParams;
  const get = (key: string) => typeof params[key] === "string" ? params[key] as string : "";
  const search = get("search").slice(0,300), type = get("type"), status = get("status");
  const data = researchInventory(), counts = data.meta.counts;
  const needle = search.toLowerCase();
  const records = [
    ...data.ledger.filter(x => x.active).map(x => ({id:x.id,title:x.id,text:x.claim,scope:"",status:x.status,type:"ledger",ledger:x,finding:null})),
    ...data.findings.map(x => ({id:x.id,title:x.titleEN,text:x.statementEN,scope:x.scopeEN,status:x.status,type:"finding",ledger:null,finding:x})),
  ].filter(x => (!type || x.type === type) && (!status || x.status === status) && (!needle || `${x.id} ${x.title} ${x.text} ${x.scope} ${x.finding?.topicIds.join(" ") || ""}`.toLowerCase().includes(needle)));
  const size = 20, pages = Math.max(1,Math.ceil(records.length/size));
  const page = Math.min(pages,Math.max(1,Number.parseInt(get("page"),10)||1));
  const href = (p:number) => `/results?${new URLSearchParams({view:"ledger",search,type,status,page:String(p)})}`;
  const premises = new Map(data.premises.map(x => [x.id,x]));
  return <div className="guide-shell">
    <header className="pt-8 pb-6"><Link className="guide-link inline-flex min-h-11 items-center" href="/results">Back to the knowledge atlas</Link><h1 className="font-serif text-4xl sm:text-5xl">Original claim records.</h1>
      <p className="guide-lead mt-5">The original technical record remains available here. For explanations, reviewed conclusions and the history of research questions, start with the knowledge atlas.</p>
      <p className="mt-5 text-sm text-slate-600">Research snapshot {data.meta.generatedAt.slice(0,10)} · {counts.ledgerActive} active ledger claims · {counts.reviewedFindings} scientific findings · {counts.registeredScripts} registered scripts. These are different inventories, not counts of independent physical confirmations.</p>
      <div className="mt-5 flex flex-wrap gap-4 text-sm"><Link className="guide-link" href="/explain">Understand the connections</Link><a className="guide-link" href="/research/inventory.json">Download the complete inventory</a><a className="guide-link" href="/research/coverage.json">Inspect the coverage checks</a><a className="guide-link" href="/research/status-ledger.csv">Original ledger snapshot</a></div>
    </header>
    <details className="guide-details mb-8"><summary>What does this inventory cover?</summary>
      <p>Every one of the {counts.ledgerActive} active ledger IDs is included. All {counts.ledgerTotal} ledger rows, including superseded rows, remain in the download. The reviewed research corpus contains {counts.reviewedFindingsBeforePrivacyFilter} findings; {counts.excludedAdministrativeFindings} administrative record is excluded from public scientific content, with the omission recorded in the coverage file.</p>
      <p>The scientific findings include {counts.findingStatuses.established_scoped} established scoped results, {counts.findingStatuses.conditional} conditional results and {counts.findingStatuses.excluded_scoped} scoped exclusions. These labels describe the recorded finding. They do not upgrade its parent physical goal or overwrite the original ledger.</p>
      <p>Sources were matched to their recorded hashes and line ranges at this snapshot. Bounded text excerpts make sources available even when a source is not in the earlier public release. Any omitted administrative lines are explicitly marked. This is source coverage, not a new execution of Python, Lean or Wolfram proofs.</p>
      <p className="break-all text-xs">Atlas revision {data.meta.sourceRevision} · snapshot SHA256 {data.meta.snapshotSha256}</p>
    </details>
    <form action="/results" method="get" className="mb-8 grid items-end gap-4 sm:grid-cols-[2fr_1fr_1fr_auto]">
      <input type="hidden" name="view" value="ledger" /><label className="text-sm font-medium">Search claims, findings and topics<input className="mt-2 w-full rounded-md border border-slate-400 bg-white px-3 py-3 font-normal" name="search" defaultValue={search} placeholder="Alpha, Higgs, 4/5/20, claim ID…" /></label>
      <label className="text-sm font-medium">Record<select name="type" defaultValue={type} className="mt-2 w-full rounded-md border border-slate-400 bg-white px-3 py-3 font-normal"><option value="">All records</option><option value="ledger">Original ledger</option><option value="finding">Reviewed findings</option></select></label>
      <label className="text-sm font-medium">Finding status<select name="status" defaultValue={status} className="mt-2 w-full rounded-md border border-slate-400 bg-white px-3 py-3 font-normal"><option value="">All statuses</option><option value="established_scoped">Established, scoped</option><option value="conditional">Conditional</option><option value="excluded_scoped">Scoped exclusion</option></select></label>
      <button type="submit" className="guide-primary justify-center">Search</button>
    </form>
    <p className="mb-6 text-sm text-slate-600">{records.length} matching records · page {page} of {pages}</p>
    {records.length === 0 && <p className="my-12">No records match these filters. <Link className="guide-link" href="/results">Show the full inventory</Link>.</p>}
    <div className="divide-y divide-slate-300">{records.slice((page-1)*size,page*size).map(record => <article className="py-7" key={record.id} id={record.id}>
      <p className="text-sm font-medium text-blue-800">{record.type === "ledger" ? "Original ledger status" : kindLabel[record.status] || record.status}</p>
      <h2 className="mt-2 break-words font-serif text-xl sm:text-2xl"><Link href={`/results?search=${encodeURIComponent(record.id)}`}>{record.title}</Link></h2>
      <p className="mt-2 break-all text-xs text-slate-600">{record.id}</p>
      <p className="raw-claim-copy mt-4 whitespace-pre-wrap break-words leading-relaxed">{record.text}</p>
      {record.ledger && <><p className="mt-4 text-sm"><strong>Recorded status:</strong> {record.status}</p>
        {(record.text.includes("v337") || record.text.includes("1.648")) && <p className="mt-3 text-sm"><Link className="guide-link" href="/results?search=metric-dtn-form-bound-needs-transfer-comparison-for-gap">Later scope correction: the DtN form estimate alone does not prove the transfer gap.</Link></p>}
        <details className="guide-details mt-4"><summary>Dependencies, status detail and source</summary><p>Canonical status: {record.ledger.canonicalStatus || record.status}</p><p>Dependencies: {record.ledger.dependencies || "None recorded"}</p><p>Scripts: {record.ledger.scripts.length ? record.ledger.scripts.join(", ") : "See original ledger entry"}</p><p>Location: {record.ledger.location}</p><a href={record.ledger.sourceHref} className="guide-link">Original CSV, line {record.ledger.sourceLine}</a></details></>}
      {record.finding && <><p className="mt-4"><strong>Scope:</strong> {record.scope}</p>
        <details className="guide-details mt-4"><summary>Required premises and original source excerpts</summary>
          <ul>{record.finding.premiseIds.map(id => <li key={id} className="my-3"><strong>{premises.get(id)?.titleEN || id}</strong><p>{premises.get(id)?.statementEN || "See the source premise definition."}</p><span className="text-xs text-slate-600">{id}</span></li>)}</ul>
          <ul>{record.finding.sources.map(source => <li key={source.id} className="my-4"><a className="guide-link break-all" href={source.href || undefined}>{source.path}, lines {source.lineStart}–{source.lineEnd}</a><p className="text-xs break-all">Source SHA256: {source.sha256}</p><p className="text-xs">{source.publicationState} · {source.freshness}{source.omittedOriginalLines?.length ? ` · ${source.omittedOriginalLines.length} administrative lines explicitly omitted` : ""}</p></li>)}</ul>
          {record.finding.publicationNotes.map((note,i) => <p className="text-sm" key={i}>{note}</p>)}
        </details></>}
    </article>)}</div>
    <nav className="mt-8 flex items-center justify-between gap-4 border-t border-slate-300 pt-6" aria-label="Result pages">
      {page > 1 ? <Link className="readout-button" href={href(page-1)}>Previous page</Link> : <span />}
      <span className="text-sm">Page {page} of {pages}</span>{page < pages ? <Link className="readout-button" href={href(page+1)}>Next page</Link> : <span />}
    </nav>
    <section className="guide-section"><h2>Open questions preserve their achieved subresults</h2><p className="guide-lead">Each research problem has its own scope. A resolved task does not close its whole physical parent. Historical tasks remain explicitly historical in the source record.</p>
      {data.problems.map(problem => <details className="guide-details my-3" key={problem.id}><summary>{problem.titleEN}</summary><p>{problem.questionEN}</p><ul>{problem.tasks.map(task => <li className="my-3" key={task.id}><strong>{task.status === "resolved" ? "Resolved in scope" : task.status}: </strong>{task.titleEN}{task.resolutionIds.map(id => <Link className="guide-link ml-2" key={id} href={`/results?search=${encodeURIComponent(id)}`}>Read result</Link>)}</li>)}</ul></details>)}
    </section>
  </div>;
}
