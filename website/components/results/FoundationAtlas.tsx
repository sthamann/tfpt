import Link from "next/link";
import { groupDecimal } from "@/lib/format-number";
import { foundationIndex, type FoundationClaim, type FoundationIndex } from "@/lib/foundation";
import { researchInventory, type LedgerRecord } from "@/lib/research";
import { sourceLibrary, documentPdf, repositorySource, type SourceLibrary, type SourceSection, type SourceDocument } from "@/lib/source-library";
import summary from "@/lib/research-summary.json";
import { claimLabel } from "@/lib/claim-labels";

type Params = Record<string, string | undefined>;
const number = (value: number) => value.toLocaleString("en-US");
const url = (params: Params) => "/results?" + new URLSearchParams(Object.entries(params).filter((pair): pair is [string, string] => Boolean(pair[1]))).toString();
function claimOpening(value:string){const clean=value.replace(/\s+/g," ").trim();const clipped=clean.length>240?clean.slice(0,240).replace(/\s+\S*$/,"")+"…":clean;return clipped.replace(/\b\d+\.\d{6,}\b/g,match=>groupDecimal(match));}
const sectionUrl = (id: string) => "/documentation?section=" + encodeURIComponent(id);
const topicUrl = (id: string) => url({ tab: "foundation", topic: id });
const claimUrl = (id: string) => url({ claim: id });

function contextFor(claim: FoundationClaim, library: SourceLibrary) {
  const explicit = new Set(claim.explicitClaimSectionIds);
  const active = new Set(claim.activeSectionIds);
  const candidates = library.sections.filter((section) => explicit.has(section.id)).map((section) => {
    const documents = section.owner_documents.flatMap((id) => {
      const document = library.documents.find((item) => item.id === id);
      return document ? [document] : [];
    });
    const document = documents.find((item) => item.role === "active" && !["document:changelog", "document:verification_catalog"].includes(item.id)) ?? documents.find((item) => item.role === "active") ?? documents[0];
    return { section, document, score: (active.has(section.id) ? 4 : 0) + (document?.role === "active" ? 2 : 0) + (section.title.length < 180 ? 1 : 0) };
  }).filter(({ section }) => !/^(?:front matter|frontmatter|[0-9]{4}-[0-9]{2}-[0-9]{2}|changelog)/i.test(section.title.trim())).sort((a, b) => b.score - a.score);
  return candidates[0] as { section: SourceSection; document: SourceDocument | undefined } | undefined;
}


const ledgerDocumentAliases: Record<string, string> = {
  tfpt_1: "document:tfpt_1_architecture_e8",
  tfpt_2: "document:tfpt_2_standard_model",
  tfpt_3: "document:tfpt_3_e8_audit_bootstrap",
  tfpt_4: "document:tfpt_4_frontier",
  tfpt_5: "document:tfpt_5_redteam",
  tfpt_5_redteam: "document:tfpt_5_redteam",
  verification: "document:verification_catalog",
};
function locationsFor(ledger: LedgerRecord | undefined, library: SourceLibrary) {
  const ids = new Set((ledger?.location || "").split(/[;,]/).map((location) => location.trim()).filter(Boolean).map((location) => ledgerDocumentAliases[location] || "document:" + location));
  return library.documents.filter((document) => ids.has(document.id));
}
function LedgerLocations({ ledger, library }: { ledger: LedgerRecord; library: SourceLibrary }) {
  const documents = locationsFor(ledger, library);
  if (!documents.length) return null;
  return <section className="foundation-source-group"><h3>Location recorded in the ledger</h3><p className="foundation-note">These document locations are recorded directly on the ledger row. They are document level navigation, rather than a newly inferred section citation.</p><ul>{documents.map((document) => <li key={document.id}><strong>{document.title}</strong><div className="foundation-links"><Link href={"/documentation?document=" + encodeURIComponent(document.id)}>Browse this document</Link>{documentPdf(document) && <a href={documentPdf(document)}>Read the PDF</a>}<a href={repositorySource(document.canonical_source)}>Original source</a></div></li>)}</ul></section>;
}

export function FoundationTabs({ topic, selected = "foundation", search }: { topic?: string; selected?: string; search?: string }) {
  return <nav className="foundation-tabs" aria-label="Result record type">
    {[["foundation", "Foundational results"], ["questions", "Research questions"], ["results", "Reviewed research"], ["history", "Historical attempts"]].map(([value, label]) => <Link key={value} aria-current={selected === value ? "page" : undefined} href={url({ tab: value, topic, search, all: value === "questions" ? "1" : undefined })}>{label}</Link>)}
    <Link href="/results?coverage=1" aria-current={selected === "coverage" ? "page" : undefined}>Source coverage</Link>
  </nav>;
}

const topicDescriptions:Record<string,string>={
 "topic:origin":"Boundary inputs, the common anchor and source selection.",
 "topic:e8":"The particle carrier, lattice matching and E₈ closure.",
 "topic:clocks":"Finite clock actions, their couplings and dynamics.",
 "topic:flavor":"Particle charges, source mass ratios and mixing.",
 "topic:alpha":"The response equation, its root and physical interpretation.",
 "topic:quantum":"Codes, finite quantum geometry and field structure.",
 "topic:gravity":"Entanglement, geometric flow and gravity interfaces.",
 "topic:cosmology":"Inflation, baryon density and vacuum energy readouts.",
 "topic:validation":"What the formal and numerical checks establish.",
 "topic:universalraum":"A common process, state and observable source.",
 "topic:metrology":"How dimensionless relations meet physical units.",
 "topic:spacetime":"From internal structure to local physical spacetime.",
 "topic:process":"Compiler operations, responses and their assumptions.",
};
export function FoundationOverview() {
  const foundation = foundationIndex();
  const topics = foundation.topics.filter((topic) => topic.id !== "topic:rh");
  return <section className="foundation-overview" aria-labelledby="foundation-overview-heading">
    <h2 id="foundation-overview-heading">Start with the published construction</h2>
    <p>The foundations include the carrier, E₈, flavour, alpha, quantum structure, gravity and cosmology. Open an area to follow its registered statements into the papers and verification sources.</p>
    <ul className="foundation-domains">{topics.map((topic) => <li key={topic.id}><Link href={topicUrl(topic.id)}><strong>{topic.titleEN}</strong><span>{topicDescriptions[topic.id]||"Explore the registered statements and their sources."}</span></Link></li>)}</ul>
    <p className="foundation-note">These are authored navigation links. The complete register contains {number(foundation.coverage.activeClaims)} active claims; {number(foundation.coverage.unmappedClaimIds.length)} do not yet have an authored topic assignment and remain searchable.</p>
    <div className="foundation-links"><Link href="/results?tab=foundation">Search all foundational claims</Link><Link href="/results?tab=foundation&mapping=unmapped">Browse claims without topic assignments</Link><Link href="/results?coverage=1">See exactly what this inventory covers</Link></div>
  </section>;
}

export function FoundationTopicPreview({ topicId }: { topicId: string }) {
  const topic = foundationIndex().topics.find((item) => item.id === topicId);
  if (!topic) return null;
  return <div className="foundation-topic-preview"><h3>The published foundation in this area</h3><p>{number(topic.claimIds.length)} authored claim references lead into the original ledger and paper sections. This source record remains available even where no separate reviewed research packet is attached.</p><Link href={topicUrl(topic.id)}>Read the foundational statements and sources</Link></div>;
}

function PaperSections({ ids, library, label, note }: { ids: string[]; library: SourceLibrary; label: string; note: string }) {
  const sections = ids.flatMap((id) => {
    const section = library.sections.find((item) => item.id === id);
    return section ? [section] : [];
  });
  if (!sections.length) return null;
  return <section className="foundation-source-group"><h3>{label}</h3><p className="foundation-note">{note}</p><ul>{sections.slice(0, 8).map((section) => <li key={section.id}><Link href={sectionUrl(section.id)}>{section.title}</Link><span>{section.owner_documents.map((id) => library.documents.find((item) => item.id === id)?.title).filter(Boolean).join("; ")}</span></li>)}</ul>{sections.length > 8 && <details><summary>All {number(sections.length)} linked sections</summary><ul>{sections.slice(8).map((section) => <li key={section.id}><Link href={sectionUrl(section.id)}>{section.title}</Link></li>)}</ul></details>}</section>;
}

function ClaimRow({ claim, ledger, library, literalMatch = false }: { claim: FoundationClaim; ledger: LedgerRecord | undefined; library: SourceLibrary; literalMatch?: boolean }) {
  const context = contextFor(claim, library);
  const location = locationsFor(ledger, library)[0];
  return <article className="foundation-claim-row">
    <h3><Link href={claimUrl(claim.id)}>{claimLabel(claim.id) || context?.section.title || location?.title || "Registered statement from the publication ledger"}</Link></h3>
    {(context?.document || location) && <p className="foundation-context">{context?.document?.title || location?.title}</p>}
    <details><summary>Original identifier and classification</summary><p className="foundation-identity"><span>{claim.id}</span><span>{ledger?.status || "Read the original ledger classification"}</span></p></details>
    <p className="foundation-note">{literalMatch ? "Literal identifier match, not an authored topic assignment." : claim.topicMappingState === "authored" ? "Topic connection recorded by an authored Atlas relation." : "No authored topic assignment in this snapshot."}</p>
    <Link className="foundation-row-link" href={claimUrl(claim.id)}>Read the statement, conditions and evidence</Link>
  </article>;
}

function ClaimDetail({ id, foundation, library }: { id: string; foundation: FoundationIndex; library: SourceLibrary }) {
  const claim = foundation.claims.find((item) => item.id === id);
  const ledger = researchInventory().ledger.find((item) => item.id === id && item.active);
  if (!claim || !ledger) return <section><h2>This active claim was not found</h2><p>Search the current foundation register or inspect the historical ledger if this identifier has been retired.</p><div className="foundation-links"><Link href="/results?tab=foundation">Search current claims</Link><Link href={url({ view: "ledger", search: id })}>Search the original ledger view</Link></div></section>;
  const context = contextFor(claim, library);
  const location = locationsFor(ledger, library)[0];
  const modules = claim.moduleIds.flatMap((moduleId) => {
    const module = foundation.modules.find((item) => item.id === moduleId);
    return module ? [module] : [];
  });
  return <section className="foundation-detail">
    <header className="foundation-detail-header"><h2>Statement, assumptions and sources</h2>{(context?.document || location) && <p>Paper context: {context?.document?.title || location?.title}</p>}<p>The exact identifier, original classification and full claim are available below.</p></header>
    <p className="foundation-note">The source wording and classification below are preserved as recorded. A paper link, shared script or authored topic relation does not upgrade the claim or report a new proof run. Read later reviewed findings separately.</p>
    <details className="foundation-disclosure"><summary>Read the exact registered claim and its dependencies</summary><div className="foundation-original"><p className="foundation-identity">{claim.id}</p><p><strong>Original ledger classification:</strong> {ledger.status}</p><h3>Original claim text</h3><p>{ledger.claim}</p><h3>Original classification detail</h3><p>{ledger.canonicalStatus}</p><h3>Dependencies as recorded</h3><p>{ledger.dependencies || "No separate dependency field is recorded."}</p><a href={ledger.sourceHref}>Open the original ledger source, row {ledger.sourceLine}</a></div></details>
    <LedgerLocations ledger={ledger} library={library} />
    <PaperSections ids={claim.explicitClaimSectionIds} library={library} label="Sections that explicitly cite this claim" note="A literal claim identifier is present in these paper sections. The section and its premises determine what the citation supports." />
    <PaperSections ids={claim.sharedScriptSectionIds.filter((sectionId) => !claim.explicitClaimSectionIds.includes(sectionId))} library={library} label="Navigation through a shared verification script" note="These sections cite a script associated with the claim. This is a source navigation join, rather than an explicit citation of the claim or a theorem equivalence." />
    {!claim.sectionIds.length && <p>No paper section is linked to this claim in the current source registry. The ledger statement remains available above.</p>}
    <section className="foundation-source-group"><h3>Registered verification modules</h3>{modules.length ? <ul>{modules.map((module) => <li key={module.id}><a href={module.sourceHref}>{module.filename}</a><span>Registered verification module · {module.cluster}</span>{module.synopsis && <details><summary>Read the description recorded in the module registry</summary><p>{module.synopsis}</p></details>}</li>)}</ul> : <p>No separate module is linked in this claim record. This is a coverage statement, not a verdict about its truth.</p>}<p className="foundation-note">A registered module is a source reference. Its presence does not assert that the module was executed in this snapshot.</p></section>
    <div className="foundation-links">{claim.topicIds.map((topicId) => <Link key={topicId} href={topicUrl(topicId)}>{foundation.topics.find((item) => item.id === topicId)?.titleEN || topicId}</Link>)}<Link href={url({ tab: "results", search: id })}>Search later reviewed research for this identifier</Link><Link href="/results?coverage=1">Read the coverage boundaries</Link></div>
  </section>;
}

function Coverage({ foundation }: { foundation: FoundationIndex }) {
  const coverage = foundation.coverage;
  return <section className="foundation-coverage"><h2>What is inventoried, and what has been reviewed?</h2>
    <p>The foundation inventory, later research review and proof execution answer different questions. The following counts retain those distinctions.</p>
    <dl>
      <div><dt>Active published claims</dt><dd>{number(coverage.activeClaims)} original ledger entries, all accessible in the foundation register.</dd></div>
      <div><dt>Source reviewed research findings</dt><dd>{number(summary.counts.reviewedFindings)} findings from the separate authored research programme. These are not a semantic review of every paper section.</dd></div>
      <div><dt>Registered verification modules</dt><dd>{number(coverage.registeredModules)} modules with source navigation. Registration is distinct from execution.</dd></div>
      {coverage.modulePublication&&<div><dt>Publication source correspondence</dt><dd>{number(coverage.modulePublication.matchingPublicationMirrorCount)} executable publication copies match the frozen source. {number(coverage.modulePublication.olderPublicationMirrorCount)} is older; its exact research source is separately available as a source document, without asserting a new execution. {coverage.modulePublication.olderPublicationMirrorIds.map(id=><Link key={id} href={`/verification?moduleQuery=${encodeURIComponent(id)}#module-catalog`}>Inspect {id}</Link>)}</dd></div>}
      <div><dt>Public paper sections</dt><dd>{number(coverage.publicPaperRegistry.physical_sections)} physical sections in {number(coverage.publicPaperRegistry.document_views)} document views, including active and historical material.</dd></div>
      <div><dt>Authored topic assignments</dt><dd>{number(coverage.authoredTopicMappedClaims)} claims have authored topic links. {number(coverage.unmappedClaimIds.length)} remain unassigned; they are preserved and searchable without invented semantic memberships.</dd></div>
      <div><dt>Paper navigation</dt><dd>{number(coverage.claimsWithPaperNavigation)} claims have at least one paper navigation link. {number(coverage.activeClaims - coverage.claimsWithPaperNavigation)} have no linked section. Explicit claim citations and shared script joins are labeled separately.</dd></div>
      <div><dt>Paper sections semantically reviewed by this registry</dt><dd>{number(coverage.semanticReviewedPaperSections)}. Literal source extraction and navigation coverage do not imply a completed scientific review of those sections.</dd></div>
      <div><dt>Proofs rerun by this export</dt><dd>{coverage.proofsChecked ? "The source coverage record flags proof checking; inspect its exact execution scope." : "No. This inventory does not rerun mathematical proofs, Python checks, Wolfram or Lean."}</dd></div>
    </dl>
    <p className="foundation-note">{coverage.notice}</p>
    <div className="foundation-links"><Link href="/results?tab=foundation&mapping=unmapped">Browse all unassigned claims</Link><Link href="/results?view=ledger">Inspect the original ledger view</Link><a href="/research/coverage.json">Download the detailed coverage record</a><a href="/research/foundation-index.json">Download the foundation navigation index</a><a href={foundation.registryHref}>Download the source library registry</a></div>
    <details><summary>Snapshot and registry fingerprint</summary><p>Snapshot generated {foundation.meta.generatedAt}. Source revision {foundation.meta.sourceRevision}.</p><p className="foundation-fingerprint">{foundation.registrySha256}</p></details>
  </section>;
}

function matchesFoundationSearch(claim: FoundationClaim, ledger: LedgerRecord | undefined, library: SourceLibrary, needle: string): boolean {
  if (!needle) return true;
  const context = contextFor(claim, library);
  return [claim.id, claimLabel(claim.id), ledger?.claim, ledger?.status, context?.section.title, context?.document?.title, ...claim.moduleIds].join(" ").toLocaleLowerCase("en-US").includes(needle);
}

/** A research search must also expose matching original foundation records. */
export function FoundationSearchMatches({ search }: { search: string }) {
  const query = search.slice(0, 300).trim();
  if (!query) return null;
  const foundation = foundationIndex();
  const library = sourceLibrary();
  const ledgerById = new Map(researchInventory().ledger.filter((entry) => entry.active).map((entry) => [entry.id, entry]));
  const needle = query.toLocaleLowerCase("en-US");
  const count = foundation.claims.filter((claim) => matchesFoundationSearch(claim, ledgerById.get(claim.id), library, needle)).length;
  return <aside className="foundation-topic-preview" aria-label="Matching foundational claims">
    <h3>Also search the published foundations</h3>
    <p>{number(count)} matching active claims in the original register. This separate source record includes claims without an authored topic assignment and is distinct from the reviewed research results below.</p>
    <Link href={url({ tab: "foundation", search: query })}>Open the {number(count)} matching foundation records</Link>
  </aside>;
}

export default function FoundationAtlas({ params }: { params: Params }) {
  const foundation = foundationIndex();
  const library = sourceLibrary();
  const inventory = researchInventory();
  const topic = foundation.topics.find((item) => item.id === params.topic);
  const search = (params.search || "").slice(0, 300).trim();
  const needle = search.toLocaleLowerCase("en-US");
  const authoredIds = new Set(topic?.claimIds || []);
  const literalIds = new Set(topic?.id === "topic:cosmology" ? foundation.claims.filter((claim) => claim.id.startsWith("COSMO.")).map((claim) => claim.id) : []);
  const ledgerById = new Map(inventory.ledger.filter((entry) => entry.active).map((entry) => [entry.id, entry]));
  const claims = foundation.claims.filter((claim) => {
    if (params.mapping === "unmapped" && claim.topicMappingState === "authored") return false;
    if (topic && !authoredIds.has(claim.id) && !literalIds.has(claim.id)) return false;
    return matchesFoundationSearch(claim, ledgerById.get(claim.id), library, needle);
  });
  const pages = Math.max(1, Math.ceil(claims.length / 20));
  const page = Math.max(1, Math.min(pages, Number.parseInt(params.page || "1", 10) || 1));
  const coverageView = params.coverage === "1";
  return <article className="foundation-shell">
    <header className="foundation-header"><h1>{coverageView ? "Source coverage, with its actual boundaries" : params.claim ? claimLabel(params.claim) || "A registered result in its source context" : "The published foundations of TFPT"}</h1>{params.claim&&ledgerById.get(params.claim)?<><p><strong>Original ledger classification:</strong> {ledgerById.get(params.claim)?.status}</p><p><strong>Recorded statement:</strong> {claimOpening(ledgerById.get(params.claim)?.claim||"")}</p></>:<p>Read the original registered statements beside their paper sections, assumptions and verification sources. The later reviewed research stays connected through a separate record.</p>}</header>
    <FoundationTabs topic={topic?.id} selected={coverageView ? "coverage" : "foundation"} search={search} />
    {coverageView ? <Coverage foundation={foundation} /> : params.claim ? <ClaimDetail id={params.claim} foundation={foundation} library={library} /> : <>
      {topic ? <section className="foundation-topic"><h2>{topic.titleEN}</h2><p>{number(authoredIds.size)} authored claim references in the foundation record. The membership comes from explicit Atlas authoring relations.</p>{literalIds.size > 0 && <p className="foundation-note">The list also shows literal COSMO identifier matches. Those entries remain unassigned in the authored topic mapping and are labeled accordingly.</p>}<div className="foundation-links"><Link href={url({ topic: topic.id, tab: "questions", all: "1" })}>Follow later research questions in this area</Link><Link href="/results?tab=foundation">All foundation areas</Link></div></section> : !search && params.mapping !== "unmapped" ? <FoundationOverview /> : null}
      <section className="foundation-register" aria-labelledby="foundation-register-heading">
        <h2 id="foundation-register-heading">{params.mapping === "unmapped" ? "Claims without an authored topic assignment" : "Search the complete foundation register"}</h2>
        <form action="/results" className="foundation-search" role="search"><input type="hidden" name="tab" value="foundation" />{topic && <input type="hidden" name="topic" value={topic.id} />}{params.mapping && <input type="hidden" name="mapping" value={params.mapping} />}<label htmlFor="foundation-query">Search the registered claims, original text and paper headings</label><div><input id="foundation-query" name="search" defaultValue={search} placeholder="Cosmology, alpha, a claim identifier…" /><button type="submit">Search foundations</button></div></form>
        <p className="foundation-note">{number(claims.length)} matching active claims. Showing at most 20 per page. Original statement text and long numerical details open within each claim.</p>
        {claims.slice((page - 1) * 20, page * 20).map((claim) => <ClaimRow key={claim.id} claim={claim} ledger={ledgerById.get(claim.id)} library={library} literalMatch={Boolean(topic && literalIds.has(claim.id) && !authoredIds.has(claim.id))} />)}
        {!claims.length && <p>No foundational claim matches these filters. <Link href={url({ tab: "results", search })}>Search the later reviewed research</Link> or <Link href="/results?tab=foundation">clear the foundation filters</Link>.</p>}
        {pages > 1 && <nav className="foundation-pagination" aria-label="Foundation claim pages">{page > 1 ? <Link href={url({ ...params, tab: "foundation", page: String(page - 1) })}>Previous</Link> : <span />}<span>Page {number(page)} of {number(pages)}</span>{page < pages ? <Link href={url({ ...params, tab: "foundation", page: String(page + 1) })}>Next</Link> : <span />}</nav>}
      </section>
    </>}
  </article>;
}
