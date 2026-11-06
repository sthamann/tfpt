import assert from "node:assert/strict";

// Check the delivered site, including metadata and legacy navigation behavior.
const base = (process.argv[2] || "http://localhost:3100").replace(/\/$/, "");
const canonical = "https://www.fixpoint-theory.com";
const paths = ["/", "/fine-structure-constant", "/e8-standard-model", "/three-fermion-generations", "/research", "/research/e8-discriminant-glue", "/research/four-mark-divisor", "/research/alpha-fixed-point-proof", "/authors", "/authors/stefan-hamann", "/authors/alessandro-rizzo", "/faq", "/papers/architecture-e8", "/changelog", "/changelog/2026-06", "/changelog/2026-06-22", "/explain"];
const results = [];
for (const path of paths) {
  const response = await fetch(base + path);
  assert.equal(response.status, 200, `${path}: HTTP status`);
  const html = await response.text();
  const head = html.split("</head>")[0];
  assert.match(head, /<title>[^<]+<\/title>/, `${path}: title`);
  assert.match(head, /<meta name="description" content="[^"]+"/, `${path}: description`);
  const url = head.match(/<link rel="canonical" href="([^"]+)"/)?.[1];
  assert.equal(url?.replace(/\/$/, ""), canonical + (path === "/" ? "" : path), `${path}: canonical`);
  assert.doesNotMatch(head, /<meta name="robots" content="[^"]*noindex/, `${path}: must be indexable`);
  assert.match(html, /<h1\b[^>]*>.+?<\/h1>/s, `${path}: readable H1`);
  const schemas = [...html.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/gs)].map(match => JSON.parse(match[1]));
  assert.ok(schemas.length, `${path}: structured data`);
  if (path.startsWith("/research/") || paths.slice(1, 4).includes(path)) assert.doesNotMatch(html, /\[formula in source\]/, `${path}: readable formulas`);
  // Guard against replacing the existing construction experiences with summaries.
  // These check delivered controls and mathematical markup; their behavior and
  // computed styling require the separate browser checks.
  if (path === "/fine-structure-constant" || path === "/explain") {
    for (const step of ["boundary", "response", "budget", "equation", "root", "comparison"]) {
      assert.ok(html.includes(`id="alpha-${step}"`), `${path}: complete alpha derivation target ${step}`);
    }
    assert.match(html, /<input\b(?=[^>]*\bid="alpha-trial")(?=[^>]*\btype="range")[^>]*>/, `${path}: delivered trial coupling slider`);
    assert.ok(html.includes("Locate the calculated root"), `${path}: root location control`);
    assert.ok(html.includes("Zoom into the root"), `${path}: residual zoom control`);
    assert.ok(html.includes("Provenance of the specified alpha closure"), `${path}: coefficient provenance table`);
    assert.ok(html.includes("katex-mathml"), `${path}: mathematical semantic markup`);
  }
  if (path === "/e8-standard-model") {
    const text = html.replace(/<!--[\s\S]*?-->/g, "").replace(/<[^>]*>/g, " ");
    assert.ok(html.includes('aria-label="Inspect one of the four gluing classes"'), "E8: delivered coset controls");
    for (const label of ["Class 0", "Class 1", "Class 2", "Class 3"]) assert.ok(text.includes(label), `E8: ${label} control`);
    assert.match(html, /<select\b/, "E8: carrier slot selector");
    assert.ok(html.includes('aria-label="Show Q sector"'), "E8: delivered charge sector controls");
    assert.ok(html.includes("From five operator pairs to the D₅ spin action"), "E8: complete Clifford action argument");
  }
  if (path === "/three-fermion-generations") {
    assert.ok(html.includes('aria-label="Five meromorphic basis functions"'), "Families: explicit divisor mode basis");
    assert.ok(html.includes("Which pairing turns the three directions into A₃?"), "Families: residue pairing argument");
  }
  if (path === "/papers/architecture-e8") {
    assert.match(head, /name="citation_author" content="Hamann, Stefan"/);
    assert.match(head, /name="citation_author" content="Rizzo, Alessandro"/);
    assert.match(head, /name="citation_pdf_url"/);
    const article = schemas.find(schema => schema["@type"] === "ScholarlyArticle");
    assert.ok(article.author.every(author => author["@id"]?.includes("/authors/")));
    assert.ok(!article.sameAs?.includes("https://github.com/sthamann/tfpt"));
  }
  results.push({ path, bytes: Buffer.byteLength(html) });
}
const sitemap = await (await fetch(base + "/sitemap.xml")).text();
const locations = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(match => match[1]);
assert.equal(new Set(locations).size, locations.length, "Sitemap URLs are unique");
assert.ok(locations.every(url => !url.includes("?") && !url.includes("#")), "Sitemap contains canonical documents");
for (const path of paths.slice(1, 11)) assert.ok(locations.includes(canonical + path), `${path}: in sitemap`);
const filtered = await (await fetch(base + "/documentation?search=alpha")).text();
assert.match(filtered, /<meta name="robots" content="noindex, follow"/, "Search variants are not independent index pages");
const redirect = await fetch(base + "/documentation?section=section%3A2befc1b3b29d5cae0f23", { redirect: "manual" });
assert.equal(redirect.status, 308, "Curated full section keeps its legacy address working");
assert.ok(redirect.headers.get("location")?.endsWith("/research/e8-discriminant-glue"));
const day = await fetch(base + "/changelog?day=2026-06-22", { redirect: "manual" });
assert.equal(day.status, 308, "Legacy day URL redirects");
assert.ok(day.headers.get("location")?.endsWith("/changelog/2026-06-22"));
assert.equal((await fetch(base + "/no-such-page-seo-check")).status, 404, "Missing pages are real 404s");
assert.equal((await fetch(base + "/changelog/invalid")).status, 404, "Invalid archive is a real 404");
const llms = await (await fetch(base + "/llms.txt")).text();
assert.match(llms, /earlier release/i);
assert.match(llms, /5\.3 \(rev 315\)/);
assert.doesNotMatch(llms, /Every load-bearing claim is machine-checked/);
for (const path of paths.slice(1, 4)) assert.ok(llms.includes(canonical + path));
const robots = await (await fetch(base + "/robots.txt")).text();
assert.match(robots, /User-Agent: OAI-SearchBot\s+Allow: \//i);
console.log(JSON.stringify({ base, checkedPages: results.length, sitemapUrls: locations.length, checks: "passed", pages: results }, null, 2));
