# Project research routing

For RH, Weil, prime-front, Hilbert–Polya, arithmetic-geometry proposals or
autonomous RH research, read and use the installed skill
`/Users/stefanhamann/.codex/skills/rh-graph-research/SKILL.md` before proposing
or testing a new mechanism. If unavailable, read
`rh/catalog/research_engine/README.md` and the existing RH corpus-search skill.
Do not interpret a fresh source index as complete semantic review or a proof.

Prefer available MCP codegraph tools for code discovery; if this repository is
not indexed, fall back to targeted local discovery. The project RH semantic
graph is `rh/catalog/map/rh_concept_map.json`; this is distinct from a code
call graph. Preserve the source hashes, conjunctive premises and scope of
negative results when using it.

This routing does not authorize unrelated changes, paper/ledger promotion,
paid computation, external publication or new delegated tasks.

<!-- tfpt-semantic-context:start -->
# TFPT: aktueller Theoriegraph und gemeinsame Projektregeln

Bei TFPT, Universalraum oder TFPT/RH auch außerhalb des Projektordners zuerst
`/Users/stefanhamann/.codex/skills/tfpt-theory-context/SKILL.md` vollständig lesen
und anwenden. Das ist der gemeinsame Einstieg in die aktuellen Regeln, Skills
und den gesamten typisierten Theoriegraphen. Bereits gelesene unveränderte
Anweisungen nicht rekursiv erneut laden.

- Gesamtkontext zuerst: `/Users/stefanhamann/.codex/context/tfpt-gesamtkontext.md`.
- Originalregeln: `/Users/stefanhamann/Projekte/tfpt-theoryv4/.cursor/rules/`;
  alle `alwaysApply: true` und die zum Thema bzw. zu Dateipfaden passenden
  weiteren Regeln lesen. Relative Befehle dort im TFPT-Repository ausführen.
- Die acht Projektskills liegen global unter `/Users/stefanhamann/.codex/skills/`
  als Verweise auf die Originale; passende Skills vor der Arbeit vollständig lesen.
- Abfragen aus jedem Arbeitsverzeichnis:
  `python3 -B /Users/stefanhamann/.codex/skills/tfpt-theory-context/scripts/query.py <Befehl>`.
  Einstieg `check`, `stats --json`; vor Mechanismusarbeit `tried` und `kills`;
  Status `claim`/`dossier`; alle Knotentypen `search`. Aktuellen Primer lesen.
- Fehlende Verdicts, Drafts und veraltete Quellen offen ausweisen. Graphpfade,
  Suchtreffer und Scriptverweise sind keine Beweise; der Originalledger entscheidet.
  RH zusätzlich mit `rh-graph-research` und `rh-corpus-search` bearbeiten.
- Ergebnisse mit Claim-/Contract-IDs und präzisem Verdict übergeben; neue
  Theorie-Contracts mit `contract_index.json` im Graphen auffindbar machen.
- Cursor-Modellnamen, Hooks und AgentStores sind keine automatisch übernommene
  Codex-Laufzeit. Die Anpassungsregeln im Einstiegsskill beachten; geltende
  Nutzeraufträge und höherrangige Sessionvorgaben behalten Vorrang.
<!-- tfpt-semantic-context:end -->
