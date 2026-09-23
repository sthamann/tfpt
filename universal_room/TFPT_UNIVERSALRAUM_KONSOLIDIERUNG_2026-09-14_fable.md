# TFPT-Universalraum: Konsolidierung der Arbeitsstände und die allesumfassende Lösungsstruktur

Stand: 14. September 2026, 12:30. Forschungsnotiz, **kein** load-bearing Claim. NON-RH.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

Grundlage: alle 17 Dateien in `universal_room/` (12 Markdown, 3 PDF, 1 LaTeX-Zip, README),
die LaTeX-Quellen der Gesamtdarstellung, die Repo-Contracts `universalraum-fugen-20260914`,
`universalraum-inversion-20260914`, `compiler-origin-audit-20260913` sowie eigene Gegenrechnungen
(Abschnitt 2).

Evidenzkonvention (übernommen aus `Q_AUDIT`): *exakt* = Identität unter genannten Voraussetzungen;
*bedingt* = Folgerung mit zusätzlicher Ausführungsregel; *offen* = ungeschlossene Herkunfts- oder
Existenzfrage; *Gegenmodell* = explizites Gegenbeispiel gegen eine behauptete eindeutige Auswahl;
*tot* = im angegebenen Scope widerlegt.

---

## 0. Ergebnis in fünf Sätzen

1. Alle 15 Dokumente stimmen in der **endlichen Algebra** überein (E8-Hülle, 60/15-Prozess, Zelle
   Ω = Λ⁴ℂ⁴, Clebsch-Graph, Zweizellenmodell, Präparationsschaltung, E8-Gittervertexalgebra); die
   Widersprüche zwischen den Arbeitsständen betreffen Reichweite, Herkunft und Multiplizitäten, nicht
   die Identitäten. Abschnitt 3 löst sie einzeln auf.
2. Jede Linie (Bottom-up ab 13.09., Inversion, drei Gegenaudits, Fugen, TOE, Gesamtdarstellung, drei
   externe Audits) stößt an **dieselbe Wand**: Zusammensetzung, Aufzeichnung und Auswahl sind nicht aus
   der E8-Klammer allein bestimmt.
3. Die allesumfassende Lösung, auf die alle Stände konvergieren, ist die **U-Regel**
   (`Q_AUDIT` Teil II): eine minimale reversible, lokale, phasentreue Kompositionsdynamik auf
   Materie ⊗ Vermittler ⊗ Geschichte, deren elementare Vertexgrammatik die ℤ₄-graduierte E8-Struktur
   ist. E8 ist Grammatik, nicht Dynamik. Sie beseitigt nachweislich fünf der dokumentierten
   Widersprüche (Abschnitt 5).
4. Es bleiben **drei fundamentale Unbekannte** (A: die eine U vollständig hinschreiben; B: der
   thermodynamische Grenzwert mit drei Raumrichtungen und gemeinsamem Kegel; C: der topologische
   Vakuumsektor mit Index 3 und masselosem Spin 2) und **eine Architekturentscheidung** (Spinorgewicht
   = Ort *oder* Spinor = innere Materie), die logisch vor allem Weiteren liegt (Abschnitt 5.3).
5. T1–T8 sind nach wie vor **alle offen**; der Fortschritt ist, dass jedes Tor jetzt einer der drei
   Unbekannten zugeordnet ist und eine konkrete entscheidende Rechnung hat (Abschnitt 7).

---

## 1. Dokumentkarte: sieben Generationen an einem Tag

| Gen. | Zeit | Datei | Rolle | Verfasser | Prüfer im Repo? |
|---|---|---|---|---|---|
| 0 | 13.09. | `tfpt_compiler_universalraum_2026-09-13.pdf` | Manuskript v1.0: 60 Strahlen, 15 Kontexte, K = B/7, Vor-Messung U, Register; T1–T8 definiert | Codex | ja: `compiler-origin-audit-20260913` (11 214 Bedingungen/Modus) |
| 1 | 07:22 | `tfpt_anschluss_zellen_seam_2026-09-14.pdf` | Hüllensatz, relative Uhr, Zelle → Kette → (A3)₁, Zustandsgate, PS-2-Loop, Hecke = Jones | Claude Fable 5.1 | ja: `universalraum-fable-kernfragen-20260910/fable-runde3` |
| 1 | 07:24 | `TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md` | Inversionshypothese: kein autonomer Systemschatten, Kontextregel = kovarianter Abschluss, Rekurrenz 2m; Gatter G1–G5 | — | ja: `universalraum-inversion-20260914` (325 + 147 Checks) |
| 2 | 07:57 | `Analyse_und_Rekonstruktion.md` | Gegenaudit von Gen. 0–1: 30-Koordinaten-Kompression, Kanalkorrektur 4⊗4̄ = 1⊕15, alternative Viereruhr, E8-Rückweg, GNS | — | nein (`audit.py`, `results.json` extern) |
| 2 | 07:58 | `TFPT_Universalraum_Rekonstruktion_2026-09-14.md` | Gegenaudit: operationelle Äquivalenz, CQ 240/45/30, B/7 nicht symmetrieeindeutig, Klammerkanäle korrigiert, Ω kein Stabilizerzustand | — | nein |
| 2 | 07:58 | `TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md` | Synthese von Gen. 0–1 + RH-Katalog-Kills; bedingte Fixpunktthese „Naht = Raum = Compiler“ | — | RH-Katalog (rhcat) |
| 3 | 08:45 | `TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md` | Fünf Fugen gerechnet: E8-Superaustausch → Clebsch (16,5,0,2), J = 2t²/Δ > 0; Sektortrennung Λ²/Sym²; 240-Bijektion äquivariant tot; ℤ₄-Glue = konforme Einbettung | — | ja: `universalraum-fugen-20260914` (27 288 Bedingungen, `clebsch_su4.py`) |
| 4 | 09:54 | `TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md` | Zweizellenmodell: invarianter 2×2-Block, globaler Grundzustand für 0 ≤ λ < 8J, Verschränkung, Uhrsignal; Ω als Netzamplitude (Hypothese) | — | nein (`audit.py` extern) |
| 4 | 09:55 | `TFPT_Fortsetzung.md` | 30-dim Faktorisierung von T, Graphsatz ker = Λᴺℂ⁴, Vermittlermodell, Zweizellenzweig, Uhren, ℤ₄-Grade | — | nein (`pruefer.py` extern, 148 Bedingungen) |
| 4 | 09:55 | `TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md` | Postselektive Ω-Schaltung K_prep = (3/4)A₄, p = 3/32; Echo 1 vs 17/32; 20 Qubits, 574 Toffoli; eingefrorene Vorhersage (SHA) | — | nein (`omega_protocol.py` extern, 598 Bedingungen) |
| 5 | 11:20 | `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf` + `…LaTeX_Quellen….zip` | Buch v1.1, 90 Seiten, 17 Kapitel inkl. 5 „Schatten“-Kapitel; integriert S01–S11 | Codex | im Zip: `verify_synthesis.py` (210), `verify_shadows.py` (128) — heute lokal reproduziert |
| 6 | 11:57 | `TFPT_Sechs_Pruefpunkte_Analyse.md` | Audit des Buchs: expliziter Mikrokandidat H_mic, Lochargument, exakter Swap-Puls, Vierkörperterm, Schur-Komplement-Schranke, Sternfilter 1/6, Einanregungspropagator, Überlagerungs-Gegenmodelle, Experimentvertrag | — | **nein** (`verify.py`, `microscopic_operator.py`, `experiment_contract.json` fehlen) |
| 6 | 12:01 | `TFPT_Rekonstruktion_2026-09-14.md` | Audit des Buchs: allkoppliger Zweizellensatz, Rang-30-Auswahl von 1/7, Spin(10)-Belegungskonflikt, 8-Punkt-Projektor, Gittercocycle, V_E8, Yarotsky-Stabilität, Gegenfamilie Γ_{d,L}; T1–T8-Vertrag | ChatGPT | **nein** (`verify_reconstruction.py` fehlt) |
| 6 | 12:01 | `TFPT_UNIVERSALRAUM_Q_AUDIT_UND_U_REGEL_2026-09-14.md` | Teil I: Audit von Q = [·,·]_E8 (globaler Kern ≠ lokale Kerne, Belegung, Vierkörperterm, Quartett statt Dublett). Teil II: **U-Regel** als primitive Quelle; drei Unbekannte A/B/C | — | **nein** |

Abhängigkeitsgraph (wer liest wen): Gen. 2 liest Gen. 0–1; `GESAMTSYNTHESE` arbeitet die Korrekturen
der beiden anderen Gen.-2-Dokumente **nicht** ein; Gen. 3 liest Gen. 0–2; Gen. 4 liest Gen. 0–3
(`TOE` zitiert `Fortsetzung` nicht); Gen. 5 integriert alle elf Vorlagen S01–S11; Gen. 6 liest nur
Gen. 5 (das Buch) und rechnet unabhängig ohne Repo-Code.

Konsequenz für die Lesereihenfolge: **Gen. 6 überschreibt Gen. 5 an den in Abschnitt 3 benannten
Stellen; Gen. 5 überschreibt Gen. 0–4.** Wo Gen. 6 dem Buch widerspricht, hat heute eine
Gegenrechnung entschieden (Abschnitt 2).

---

## 2. Heute unabhängig nachgerechnet

Skripte ad hoc unter `/tmp/ur_consol/` (nicht im Repo; NumPy 2.4.2, SciPy 1.17.0, SymPy). Sie
verwenden für den Clebsch-Singulettsektor den Young-orthogonalen Operator aus
`experiments/theory-contracts/universalraum-fugen-20260914/clebsch_su4.py`, sonst keinen Repo-Code.

| Nr. | Aussage | Quelle der Behauptung | Ergebnis |
|---|---|---|---|
| R1 | Zweizellensatz für **alle** λ ≥ 0: E₀ = (4J+λ−R)/2, E₁ = 3J + λ/2 − Q/2, R = √(16J²−2Jλ+λ²), Q = √(4J²+λ²) | `Rekonstruktion` 12:01, `Q_AUDIT` §4 | **bestätigt.** Lanczos auf 4⁸ = 65 536 dim bei λ/J ∈ {0, 0.5, 1, 2, 6, 8, 12, 30, 100}; Abweichung < 10⁻⁷; Δ(8J) = 0.876894374 J; Δ(100J) = 0.527865 J > J/2; keine Kreuzung bei 8J |
| R2 | Tetramerspektrum J{0¹, 2⁴⁵, 3⁴⁰, 4¹³⁵, 6³⁵}; 8-Punkt-Projektor (1/8)Σₖ e^{−2πikH/(8J)} = \|Ω⟩⟨Ω\| | alle | **bestätigt** (atol 10⁻¹⁰) |
| R3 | Sternspektrum J{0¹, ½³⁰, 1⁴⁵, 3/2⁴⁰, 2¹⁵, 5/2⁹⁰, 3³⁵}; (1/8)Σₖ Uᵏ = A₄ mit U = e^{−iπH⋆/(2J)}; \|⟨Ω\|χ₀⟩\|² = 1/6 | `Sechs_Pruefpunkte` §3 | **bestätigt** |
| R4 | Erstes angeregtes Clebsch-**Singulett** bei 11.561762 J ist ein Dublett (Buch S. 18, `clebsch_su4.json`) bzw. mindestens ein Quartett (`Q_AUDIT` §5) | Konflikt | **Quartett.** dim Singulettsektor 24 024; E₀ = 11.045398337068 J; E₁ = 11.561762122802 J mit Multiplizität **4** in allen sechs Lanczos-Konfigurationen (ncv ∈ {64, 128}, drei Startvektoren), Residuen ≤ 2.7·10⁻¹¹. Nächstes Niveau 12.456024 J mit ≥ 7 gefundenen Kopien. Ursache des Buchwerts: `k_per_irrep=4` in `clebsch_su4.py` fordert nur vier Eigenwerte an |
| R5 | Verbundener Vierkörperterm zweier Kanten mit gemeinsamem Vermittler: H⁽⁴⁾ = −(2g⁴/Δ³) S₆ (`Sechs`) bzw. (16t⁴/Δ³) P₋ (`Q_AUDIT`) | zwei Schreibweisen | **konsistent** (g = √2 t, S₆ = I − 2P₋). Sym-Zweig ohne g⁴-Term, Antisym-Zweig +4g⁴/Δ³, Einzelbond +g⁴/Δ³; numerisch bei g = 0.05: −1.238·10⁻⁵ vs −1.25·10⁻⁵. Verhältnis \|K₄\|/J = **4 (t/Δ)²** |
| R6 | „K₄/J ≈ ε², bei ε = 0.1 ≈ 1 %“ | `Q_AUDIT` Teil II §4 | **Vorfaktor fehlt.** Bei t/Δ = 0.1 sind es ≈ 4 % (S₆-Normierung) bzw. 8 % (P₋-Normierung); 1 % gilt beim Referenzwert t/Δ = 1/20 aus `Sechs` §1.2 |
| R7 | 210 Bedingungen `verify_synthesis.py`, 128 Bedingungen `verify_shadows.py` | Buch, `Q_AUDIT` §1 | **210/210 und 128/128 bestanden** (lokaler Lauf, α⁻¹ = 137.03599921684071…, 1.8971768 σ zu CODATA 2022) |

Nicht nachgerechnet (nur extern dokumentiert): 2 511 496 Jacobi-Tripel (`Q_AUDIT`), 129-dim
Zweibondmatrix und Schur-Komplement-Schranke (`Sechs`), Cocycle-Kontrolle aller 57 600 Wurzelpaare,
Yarotsky-Anwendung, Überlagerungs-Bloch-Banden, 20-Qubit-Schaltungsexport, PS-Zweischleifenlauf.

---

## 3. Widersprüche zwischen den Arbeitsständen und ihre Auflösung

| # | Streitpunkt | Positionen | Konsolidierte Auflösung |
|---|---|---|---|
| C1 | Reichweite des Zweizellen-Grundzustandssatzes | `TOE`, `Fortsetzung`, Buch Kap. 5/8: global nur für 0 ≤ λ < 8J. `Rekonstruktion` 12:01, `Q_AUDIT`: alle λ ≥ 0, plus exakte E₁ und Δ > J/2 | **Alle λ** (R1). Die Marke 8J ist die Grenze eines alten Beweises, kein physischer Übergang. Buch Kap. 5, 8 und die Tabelle in `TOE` sind zu ergänzen |
| C2 | Multiplizität des ersten angeregten Clebsch-Singuletts | Buch S. 18 / `clebsch_su4.json`: Dublett. `Q_AUDIT` §5: ≥ 4 | **Quartett** (R4). Lanczos-Artefakt bei k = 4. Die Multiplizität 4 ist mit einer vierdimensionalen Darstellung von Aut(Clebsch) ≅ 2⁴:S₅ = W(D₅) (Ordnung 1920) verträglich; exakte Zertifizierung offen |
| C3 | Gemischter Klammerkanal 4 ⊗ 4̄ → (10,6) | `Seam` 07:22 und `GESAMTSYNTHESE` 07:58 verwenden ihn. `Analyse`, `Rekonstruktion` 07:58, `Fugen`, `Fortsetzung`, Buch: [g₁, g₃] ⊂ g₀ = (45,1) ⊕ (1,15) | **Nur 1 + 1 → 2 erreicht (10,6)**: 960 geordnete Paare; 1 + 3 → 0 liefert 640 + 192 Summen und 64 Cartan-Paare. `GESAMTSYNTHESE` ist an dieser Stelle veraltet |
| C4 | Konjugierter Sektor (16, 4̄) vs (16̄, 4̄) | Gen. 0–1 teils (16, 4̄) | **(16̄, 4̄)** (`Fugen` Korrektur 1, Buch Kap. 2) |
| C5 | „Minimalität“ des vollen CQ-Zustands 15 × 16 = 240 | `Inversion`, `GESAMTSYNTHESE`: minimal. `Analyse`, `Rekonstruktion`, `Fortsetzung`, `TOE`, Buch: 240 = allgemeiner Eingangsraum | **240 ist nicht minimal.** Passive System-/Kontextmarginalien 45/44, gemessene Strahlenklasse 30/29, Bild nach einer Runde 60/59; kohärente Register sind gar nicht CQ. „Minimal“ ist immer relativ zur Zugriffsklasse |
| C6 | Herkunft von K = B/7 | `Inversion`, `GESAMTSYNTHESE`: kovarianter Abschluss „leitet ab“. `Analyse`, `Rekonstruktion`, Buch: K_a = aI + (1−a)(B−I)/6 ist Gegenbeispiel. `Rekonstruktion` 12:01: a = 1/7 ist in K_a die eindeutige Wahl mit Rang 30 (sonst 55 oder 60). `Q_AUDIT`: Maximierung der Übergangsentropie bei genau sieben Nachfolgern wählt 1/7 | **B/7 = kovarianter Abschluss + genau ein Zusatzprinzip.** Zwei äquivalente Kandidaten (maximale Einmalkompression / maximale Übergangsentropie); keiner ist aus Symmetrie hergeleitet. Der Wert 1/2 bleibt symmetrisch zulässig |
| C7 | c = 8 als Kondo-RG-Fixpunkt | `Seam`: RG-Fluss. `Fugen` Korrektur 3, Buch Kap. 7: konforme Einbettung (D₅)₁ × (A₃)₁ ⊂ (E₈)₁ mit ℤ₄-Eichung, kein Fluss | **Konforme Einbettung.** „Es gibt keinen RG-Fixpunkt zu suchen“ |
| C8 | 240-Bijektion (CQ-Koordinaten ↔ E8-Wurzeln ↔ Ankerprodukt) | `GESAMTSYNTHESE`: offen/Numerologie. `Fugen`: äquivariant tot (Orbits 15 + 45 + 180 vs 60 Strahlen × 4 Phasen). Buch: äquivariant scheitert, andere Abbildungen nicht ausgeschlossen | **Äquivariante Version tot; nicht-äquivariante Version wird nicht gesucht** (hätte ohne Struktur keine Aussagekraft, `Fortsetzung`) |
| C9 | Cross-Register-Aufzeichnung „innerhalb der 248 unmöglich“ | `Fugen` Fuge 3: exakt negativ (Aufzeichnung braucht Sym²(4), 248 liefert nur Λ²(4)). Buch Kap. 4/11, `Rekonstruktion` 12:01: geht über den Beweis hinaus; Q ist als Polynom trägerübergreifender Generatoren schreibbar; fehlende Darstellung in der 248 verbietet keine Tensorproduktzustände | **Algebraisch darstellbar, physisch nicht ausgewählt.** Die Sektortrennung Λ²/Sym² bleibt als Satz richtig; sie ist ein Herkunfts-, kein Unmöglichkeitsresultat |
| C10 | Welcher Vierergraph trägt den exakten Filter? | `Rekonstruktion` 12:01, `Q_AUDIT`: vollständiger Tetramer H_tet, Periode 8J. `Sechs`: Viererstern H⋆ (Clebsch ist dreiecksfrei, enthält kein K₄) | **Beide exakt (R2, R3); die Sternversion ist die einzige, die im Clebsch-Graphen nativ existiert.** Ebenso ist der Zweizellensatz ein Satz über zwei K₄ mit Brücke, kein Eigenwerttest des Clebsch-Modells (`Sechs` §2.6) |
| C11 | Belegungsmodell | `Rekonstruktion` 12:01: weiches Hubbard-U, Δ_eff = Δ_b + U. `Sechs`: harte Projektion. `Q_AUDIT`: H_s = \|∅⟩ ⊕ ℂ⁴ | **Dasselbe Ergebnis** H⁽²⁾ = (2t²/Δ_eff) Σ_e P⁺_e in allen drei Fassungen; verschieden ist nur, was Δ_eff bedeutet |
| C12 | Rolle von Spin(10) | `Rekonstruktion` 12:01 §5: feste Belegung auf Gewichtsplätzen und ungebrochene kontinuierliche Spin(10)-Wirkung sind unvereinbar ([H_U, T_{ss'}]P = U T_{ss'}P ≠ 0) → Lesart „Spinor = innere Materie“ sei strukturell sauberer. `Q_AUDIT` Teil II §2: U-Regel behält „Spinorort s“ (Gewicht = Ort) | **Offene Architekturentscheidung**, die beiden neuesten Dokumente zeigen in verschiedene Richtungen. Siehe Abschnitt 5.3 |
| C13 | Größe des Vierkörperterms | `Q_AUDIT` Teil II: ≈ 1 % bei ε = 0.1 | **4–8 % bei 0.1; 1–2 % bei 1/20** (R5, R6). Ändert die qualitative Aussage „kontrollierte effektive Theorie“ nicht |
| C14 | „Sym² fehlt in der 248 ⇒ Mehrträgerzustände verboten“ | `Fugen`, `Seam` | **Zurückgenommen** durch `Analyse` §6, Buch Kap. 11, `Rekonstruktion` 12:01 §2: eine Adjungierte ist nicht der Mehrteilchenraum |
| C15 | Protonzerfall der geeichten SO(10)/PS-Zweige | `GESAMTSYNTHESE`: Faktor 2.4–6 unter 2.4·10³⁴ a. `Seam`, Buch Kap. 9, `Sechs` §6.2: Faktoren 80, 3.4, 2.4 zu kurz für M_PS = 3.7; 3.5; 4.4 ·10¹³ GeV | **80 / 3.4 / 2.4** (drei Zweige; `GESAMTSYNTHESE` nennt nur die beiden günstigeren). Negativer Befund bleibt |
| C16 | Uhr | `Seam`: Familienzyklus Perioden 3/12. `Inversion`: Drei-Niveau-Obstruktion für vier PW-Anzeigen. `Analyse`: Obstruktion gilt nur für den gewählten Generator, alternative Viereruhr R⁴ = I. `TOE`: Zweizellen-Brückenoszillation p₁(t). `Omega`: Pointer-Echo | **Keine Konkurrenz**, fünf verschiedene Uhrbegriffe für verschiedene Protokolle (siehe Abschnitt 10). Gemeinsam: jede braucht Präparation, Basis und Skala als Quelldaten; ein Grundzustand tickt nicht |
| C17 | Präparation von Ω | `Rekonstruktion` 07:58: Stabilizer-Ressource ausgeschlossen. `Omega`: postselektiv mit Nicht-Clifford-Steuerung, 3/32. `Sechs`, `Rekonstruktion` 12:01, `Q_AUDIT`: exakter Spektralfilter, 1/6, saturiert die Schranke Tr(A₄ρ). `Q_AUDIT` Teil II §7: Relaxation in Vermittler/Geschichte | **Stufenfolge, kein Widerspruch:** reiner Austausch erhält den Ω-Anteil (exakt) → postselektive Filter (3/32 → 1/6, optimal für A₄-kommutierende Instrumente) → dissipative Relaxation als Kandidat für den kosmologischen Mechanismus (Hypothese) |

---

## 4. Konsolidierter Stand: was trägt (Schicht 0, exakt)

### 4.1 Algebra
- P1: c₃ = 1/(8π), orientierter Rand, positiver Kern. P2: fünfteiliger Träger, 3 + 2-Lesart. Beide **gesetzt**; sie enthalten mehr als „zwei Zahlen“ (Buch Kap. 11).
- S⁺ = Λ^even ℂ⁵, dim 16. D₅ ⊕ A₃: Determinanten 4, Diskriminantengruppen ℤ₄, q_{D₅} = 5k²/8, q_{A₃} = 3k²/8; Index-4-Erweiterung → gerades unimodulares Gitter Rang 8 = **E₈** (112 + 128 = 240 Wurzeln, 248). **Exakt** unter markierten Ausgangsdaten.
- 𝔢₈ = (45,1) ⊕ (1,15) ⊕ (10,6) ⊕ (16,4) ⊕ (16̄,4̄), ℤ₄-Grade g₀…g₃; [g₁,g₁] ⊂ g₂ (960 Paare), [g₁,g₃] ⊂ g₀. Jacobi auf allen 2 511 496 Basisdreiern geprüft (`Q_AUDIT`, extern).
- Familienzähler (16−1)/5 = 3: **Zählung, kein Indexsatz**; endlicher chiraler Block mit gleich großen Räumen hat Index 0.

### 4.2 Prozess
- 60 Strahlen, 15 Kontexte, Sp(4,2) ≅ S₆. T = (CᵀBC + FᵀF)/28, Rang 30, Spektrum {1¹, (3/7)¹⁵, (2/7)⁹, (−2/7)⁵, 0³⁰}; Kontextschatten K = B/7, Paulischatten 3/7. **Exakt.**
- Kein autonomer Systemschatten für alle Registerfortsetzungen; bei stets frischem Register existiert die Dephasierungsregel 𝒟ⁿ. Rekurrenz zyklischer m-Register: 2m. **Exakt im Modell.**
- K ist kein reelles Matrixexponential (det K < 0); −log K ist kein Generator. Kein endliches geschlossenes System erzeugt exaktes (3/7)ⁿ für alle n (Satz P1, `Inversion`).

### 4.3 Zelle und Graph
- **Hüllensatz:** P⁺_{ij}ψ = 0 auf den Kanten eines zusammenhängenden positiven Graphen ⇒ ψ ∈ Λᴺℂ⁴; N = 4 eindeutig (Ω), N ≥ 5 leer, N = 1, 2, 3 ebenfalls antisymmetrisch möglich. **Bewiesen.**
- „Warum vier“: Zentrum iI wirkt als iⁿ ⇒ Singulett verlangt n ≡ 0 mod 4; kleinste nichtleere antisymmetrische Struktur Λ⁴ℂ⁴. **Bedingt** auf ausschließlich fundamentale Träger (4 ⊗ 4̄ = 1 ⊕ 15 würde Zweierneutralität erlauben).
- Ω: Einzelmarginalen I₄/4, Paarmarginalen (I−S)/12 Rang 6, Paulikorrelation −1/3; kein Stabilizerzustand (16 statt 256 Stabilisatoren). **Exakt.**
- Unter „Ort = D₅-Spinorgewicht“: Clebsch-Graph (16, 5, 0, 2), 40 Kanten, Spektrum 5¹ 1¹⁰ (−3)⁵, dreiecksfrei, fünf perfekte Matchings, zehn Kantenlabels ±eᵢ mit je vier Kanten; Aut ≅ W(D₅), Ordnung 1920. **Exakt unter Lesart.**
- Frustration: ker Σ_e J_e P⁺_e = Λ¹⁶ℂ⁴ = 0 ⇒ ein voll besetzter Clebsch ist nirgends defektfrei. Ω ist deshalb **lokale Verknüpfungsamplitude**, nicht reine Dichtematrix jeder Region.
- Clebsch-Singulett: E₀ = 11.045398337 J, eindeutig; erstes angeregtes Singulett 11.561762 J, **Quartett** (R4); erste magnetische Lücke 12.133537 J (Adjungierte). ⟨P⁺_Kante⟩ = 0.27613, ⟨P⁺_Nichtkante⟩ = 0.61193.

### 4.4 Kopplung
- Einzelkante: K_e: ℂ⁴ ⊗ ℂ⁴ → ℂ⁶ mit K_e†K_e = I − S_e = 2P₋ **exakt** aus den Strukturkonstanten.
- Globaler Kern ≠ Summe lokaler Kerne: rank Q₁₁ = 60, dim ker Q₁₁ = 4036; 40 Kanten mit gemeinsam benutztem Ziel haben Rang 60 (Kern 580), mit unterscheidbaren Kantenspuren Rang 240 (Kern 400). **Gegenbeispiel** gegen H = P_ker Q als Algebrafolge.
- Belegung (Löcher als Kantenlabel) tötet Kreuzterme zweiter Ordnung: H⁽²⁾ = (2t²/Δ) Σ_e P⁺_e, **J = 2t²/Δ > 0**. Vierte Ordnung: verbundener Term −(2g⁴/Δ³) S₆ pro Kantenpaar mit gemeinsamem Vermittler; |K₄|/J = 4(t/Δ)² (R5). Fehlerschranke ‖H_F(E) − H⁽²⁾‖ ≤ 2v⁴/[Δ²(Δ−v)] unter v = ‖V‖ < Δ (für t/Δ = 1/20 global **nicht zertifiziert**).
- Isolierter Vermittler: g = (√3/2)Δ, τ = 2πℏ/Δ ⇒ exakter Swap S auf dem Paarraum ohne Restbesetzung.
- **Zweizellensatz (alle λ ≥ 0):** E₀ = (4J+λ−R)/2, E₁ = 3J + λ/2 − Q/2, Δ = J + (R−Q)/2 > J/2; λ → ∞: E₀ → 5J/2, E₁ → 3J, Δ → J/2. Verschränkung q = ½[1 − (4J − λ/4)/R], spec ρ_A = {1−q, (q/15)¹⁵, 0²⁴⁰}, q → 5/8. **Bewiesen und numerisch bestätigt (R1).**
- Viele Zellen: globale Schranke Δ ≥ 2J − (5/8)(N−1)λ ist nicht fundamental; für translationsinvariante schwach gekoppelte Tetramerfamilien auf ℤᵈ liefert Yarotsky einen größenunabhängigen Gap (**bedingt**; ein gapped Produkt ist **nicht** das Vakuum, es schließt masselose Photon-/Gravitonmoden aus).

### 4.5 Präparation, Aufzeichnung, Zeit
- Reiner Austausch und kollektive SU(4)-Drehungen erhalten den Ω-Anteil: **Präparationshindernis exakt.**
- Exakte Filter: P_Ω = (1/8)Σₖ e^{−2πikH_tet/(8J)} (Tetramer) bzw. A₄ = (1/8)Σₖ Uᵏ, U = e^{−iπH⋆/(2J)} (Stern, drei Kontrollbits, Zweig 000). Erfolg für χ₀: **1/6** statt 3/32 (Faktor 16/9); Schranke Tr(A₄ρ) saturiert. Acht Kontrollausgänge (1/6, 1/6, 0, 0, 1/6, 1/6, 1/6, 1/6).
- Echo: behalten 1 vs frisch 17/32 (Dreierzyklus) bzw. 1 vs 1/2 (CNOT-Tick, Kontrastmaximum). Rohwahrscheinlichkeiten pro begonnenem Versuch: alt 27/512 vs 459/16384 bzw. 27/1024; mit exaktem Filter 1/6 vs 17/192 bzw. 1/12. Beide Verträge getrennt archiviert; **kein nachträgliches Umschreiben**.
- Reversible Geschichte: für KK† = 8I ist Vψ = (Wψ) ⊕ (Pψ) mit W = K/√8, P = I − W†W eine Isometrie. „Frisches Register“ = zukünftige Operationsalgebra greift nicht mehr auf H_alt zu. **Konstruiert, nicht ausgewählt.**
- Uhren: Familienlift c = iσ (Perioden 3/12); lokale Pauli-Uhr Periode πℏ/J; relationale PW-Uhr mit vier Anzeigen; Zweizellensignal p₁(t) = 15λ² sin²(Rt/2ℏ)/(16R²). Alle **bedingt** auf Präparation, Basis, Skala.

### 4.6 Naht
- Gittervertexalgebra V_{E₈} = ℱ₈ ⊗ ℂ_ε[E₈], Cocycle ε(m,n) = (−1)^{mᵀBn} mit B = tril(G,−1) + I, Kommutatorfaktor (−1)^{mᵀGn}, Adjunktion e_α† = ε(−α,α)⁻¹e_{−α}, OPE V_α(z)V_β(w) ~ ε(α,β)(z−w)^{α·β}V_{α+β}(w). Θ_{E₈} = 1 + 240q + 2160q² + 6720q³, χ = q^{−1/3}(1 + 248q + 4124q² + 34752q³). ℤ₄-Sektoren mit Gesamtgewicht 0, 1, 1, 1 (5/8 + 3/8, 1/2 + 1/2). **Standardmathematik, explizit ausgeführt.**
- SU(4)-Kette: endliche Daten passen zu (A₃)₁-WZW (Δn ≈ 3.70 vs 3π²/8 = 3.70110; e_∞ = 0.087439 vs 0.08773; c_fit = 3.16). Aber c_L = c_R = 3: **nicht chiral.** Eine chirale (E₈)₁-Naht mit c_L − c_R = 8 verlangt eine Bulk–Rand-Architektur (invertierbarer 2+1-Bulk mit K = G_{E₈}). **Vorausgesetzt, nicht hergeleitet.**

### 4.7 Geometrie
- M₂(ℂ) hermitesch: det(tI + x·σ) = t² − |x|², SL(2,ℂ)-invariant. **Exakt**, Kinematik.
- Einanregungspropagator auf Clebsch: H_ein = 40J·I − (J/2)L, Laplace-Eigenwerte 0, 4, 8 (1, 10, 5), U(t) = P₀ + e^{2iJt/ℏ}P₄ + e^{4iJt/ℏ}P₈, Rückkehramplitude (1 + 10e^{2iJt/ℏ} + 5e^{4iJt/ℏ})/16. **Exakt**; drei kohärente Pole, quadratische statt Weyl-Dispersion.
- **Gegenmodelle zur Dimension:** (i) Überlagerungen des Clebsch-Graphen (Zyklusrang 25; Spannbaum + ℤᵈ-Verschiebungen) mit d = 1, 2, 3, 4 und derselben lokalen Inzidenz; Baumüberlagerung |B(r)| = 1 + 5(4ʳ−1)/3. (ii) Γ_{d,L} = (ℤ/L)ᵈ □ Γ_Cl mit P_d(τ) ~ (4πτ)^{−d/2}/16, d_s → d. **Die innere Struktur wählt d nicht.**

---

## 5. Die allesumfassende Lösung: U statt Q, E₈ als Grammatik

### 5.1 Warum jede Linie an derselben Stelle endet
- Bottom-up (Gen. 0–1): Compiler liefert Algebra, Zelle, Graph — aber nicht Kopplungsstärke, Präparation, Registerversorgung, Zeitskala (die fünf Fugen).
- Inversion (Gen. 1): der Systemschatten ist nur relativ zur Zugriffsklasse autonom; der Universalraum ist ein Prozessobjekt mit Gedächtnis.
- Gegenaudits (Gen. 2): rekonstruierbar ist die minimale beobachtbare Prozessdarstellung (GNS), nicht eine eindeutige Mikrophysik; jede „Ableitung“ hatte ein Gegenmodell (K_a, gleiche Kerne mit verschiedenen Spektren, 105 Qubit-Paarungen).
- Fugen/TOE/Buch (Gen. 3–5): unter der Lesart „Ort = Spinorgewicht“ wird alles Endliche eindeutig — aber die Lesart selbst, Belegung, Fockstruktur, t und Δ bleiben Eingaben.
- Audits (Gen. 6): Q = [·,·]_{E₈} als Energie ist eine Zusatzregel (globaler Kern ≠ lokale Kerne); Belegung liefert die fehlende Unterscheidbarkeit; Dimension ist nicht identifizierbar.

Gemeinsamer Befund: **Die E₈-Klammer bestimmt Vertizes und relative Phasen, nicht die Zustandsentwicklung.** Alles, was in den 15 Dokumenten fehlt, ist eine Aussage darüber, wie Vertizes reversibel ausgeführt, unterschieden, besetzt und zu Geschichten zusammengesetzt werden.

### 5.2 Die U-Regel (konsolidierte Formulierung)
Primitive Quelle ist eine unitäre Ereignisregel

U : H_matter ⊗ H_mediator ⊗ H_history → H_matter ⊗ H_mediator ⊗ H_history, U†U = I,

mit
- lokalem Ort s: H_s = |∅⟩ ⊕ ℂ⁴ (leer oder genau ein A₃-Zustand; elementare Population 4, nicht 4 ⊕ 4̄);
- elementarem Vertex |a⟩_s|b⟩_t|0⟩_m|0⟩_h → Σ_μ C^μ_{st;ab} |∅⟩_s|∅⟩_t|μ⟩_m|st,ab,μ⟩_h plus exakt unitärer Rückweg;
- Koeffizienten C^μ_{st;ab} = normierte E₈-Strukturkonstanten (keine freien Kopplungen);
- History-Label (s, t, a, b, μ); die Lochkonfiguration |∅_s, ∅_t⟩ ist selbst das physikalische Kantenlabel.

Was sie **nachweislich** auflöst (jeweils mit Verweis auf den Widerspruch aus Abschnitt 3):
1. Globaler vs lokaler Kern (`Q_AUDIT` §2): zwei Kanten interferieren nur bei identischen Endzuständen inkl. Löchern und Geschichte ⇒ lokale Summe Σ_e P⁺_e ist Folge, nicht Zusatzregel. Energie = effektive Kosten virtueller Prozesse: J = 2t²/Δ, höhere Ordnung 4(t/Δ)² kontrolliert (R5).
2. Register behalten / frisch (C5, C9, C17): global unitär, lokal ρ_S = Tr_H ρ_SH; „Vergessen“ = operationelle Unzugänglichkeit. Der Registerstreit der Gen. 1–2 wird zu einer Aussage über die Zukunftsalgebra.
3. Präparation (C17): Ω ist unter reinem Austausch erhalten, aber mit Vermittler- und History-Sektor ist Relaxation ρ → |Ω⟩⟨Ω| als offener effektiver Kanal möglich; die 20-Qubit-Schaltung bleibt Laborprotokoll.
4. Kein autonomer Systemschatten (`Inversion`): folgt, weil der Schatten nur relativ zur Zugriffsklasse auf H_history autonom ist — die CQ-Zahlen 240/60/45/30 sind Zugriffsklassen derselben U.
5. Zeit (C16): Zeit ist die kausale Ordnung der Ereignisse U₁, U₂, …, nicht eine vierte Graphachse; daher strukturell 3 + 1 statt euklidischer Viererraum.

Was sie **nicht** liefert (und ehrlich als offen führt): Eindeutigkeit/Minimalität von U; den thermodynamischen Grenzwert; den topologischen Vakuumsektor; jede Zahl (α, Massen) — die bislang extrem genaue α-Gleichung bleibt eine Formel ohne hergeleiteten Transfer.

### 5.3 Die eine Architekturentscheidung, die vorher fällt (C12)
`Rekonstruktion` 12:01 zeigt: auf dem Sektor „ein Fermion pro Gewichtsplatz“ ist [H_U, T_{ss'}]P = U·T_{ss'}P ≠ 0 — feste Belegung und ungebrochene kontinuierliche Spin(10) sind unvereinbar. Die U-Regel in `Q_AUDIT` verwendet aber genau diese Belegung auf Spinororten.

Konsolidierte Einordnung:
- Unter „Gewicht = Ort“ bleibt von Spin(10) exakt die diskrete Restsymmetrie **W(D₅) = 2⁴:S₅ = Aut(Clebsch)** (Ordnung 1920) zusammen mit lokalem SU(4). Das ist konsistent mit der Quartettstruktur des ersten Singulettanregungsniveaus (R4). Spin(10) ist dann kombinatorische Herkunft, kein dynamischer Eichsektor; Eichfelder müssten emergent aus internen Frames entstehen (`Q_AUDIT` Teil II §16).
- Unter „Spinor = innere Materie“ wirkt Spin(10) intern auf ψ_{x,α}; dann müssen räumliche Träger x und ihre Nachbarschaft aus einer **anderen** gemeinsamen Regel kommen — die Clebsch-Herleitung des Graphen entfällt.
- Eine dritte Lesart (Brechung Spin(10) → W(D₅) mit emergenter Wiederherstellung) verlangt einen eigenen Mechanismus und darf die beiden ersten nicht sprachlich vermischen.

**Entscheidende Rechnung:** Symmetriealgebra (Kommutante) von H_eff⁽²⁾ + H_eff⁽⁴⁾ auf dem harten Belegungssektor des C16 ausrechnen. Ist sie SU(4) × W(D₅) (erwartet), ist Lesart 1 der U-Regel intern konsistent und Spin(10) als Eichgruppe muss emergent begründet werden; enthält sie unerwartet kontinuierliche Anteile, ist Lesart 3 einschlägig. Erst danach lohnt die Eich- und Raumzeitrekonstruktion.

---

## 6. Die drei fundamentalen Unbekannten und ihre entscheidenden Rechnungen

| | Unbekannte | Tore | Was schon steht | Entscheidende Rechnung (vorab festgelegt) |
|---|---|---|---|---|
| **A** | Die eine mikroskopische Regel U vollständig hinschreiben und danach nichts mehr wechseln (nicht Clebsch/Tetramer/Kette/Register je nach Ergebnis) | T1, T8 | H_mic aus `Sechs` §1.2 (64 Fermionmoden + 60 Bosonmoden, Ladungssektor 16, t/Δ = 1/20); isometrische Erweiterung W ⊕ P; Rang-30- bzw. Entropieprinzip für 1/7 | (A1) H_mic auf dem vollen Belegungssektor bis vierter Ordnung als **einen** effektiven Operator berechnen (nicht ein Cluster). (A2) Kommutante bestimmen (Abschnitt 5.3). (A3) Zertifizieren, ob ‖V‖ < Δ bei 1/20 global gilt; sonst Referenzwert neu setzen. (A4) Aus derselben U die Registerprotokolle „behalten/frisch“ als Zugriffsklassen ableiten und die Rohwahrscheinlichkeiten 1/6 und 1/12 ohne Nachwahl reproduzieren |
| **B** | Thermodynamischer Grenzwert: G⁻¹ → γ^μp_μ mit drei Raumrichtungen, gemeinsamer Geschwindigkeit, chiralen Polen | T3, T5 | Zweizellensatz für alle λ; Yarotsky-Gap für schwach gekoppelte Produktfamilien (gapped ≠ Vakuum); Gegenmodelle d = 1…4; Kodimension-3-Argument (d₁ = d₂ = d₃ = 0) als Auswahlbedingung; Lorentz-IR-Fixpunkt v_i(ℓ) → c als Ziel | (B1) Bloch-Banden der Überlagerungsfamilien mit dem **mehrkomponentigen** SU(4)-Niedrigenergiesektor (nicht skalar): lineare Kreuzungen vs quadratische Banden. (B2) Existiert ein lückenloser oder kritischer Sektor jenseits des Yarotsky-Bereichs? Gap als Funktion von λ/J für N = 2, 3, 4 Zellen auf den drei Graphfamilien. (B3) Spektraldimension und Volumenskalierung aus tatsächlichen Korrelatoren, nicht aus eingesetztem Gitter |
| **C** | Topologischer Vakuumsektor: index D_eff = 3 und kollektiver masseloser Spin-2-Modus | T2, T4, T6, T7 | V_{E₈} mit Cocycle/Adjunktion/OPE; Bulk–Rand-Vorlage (invertierbarer Bulk mit K = G_{E₈}, Plamadeala–Mulligan–Nayak); Familie = Index statt (16−1)/5; Gravitation = Variation des Propagatorframes e^a_μ(x); Kopplungen = Vakuumsteifigkeiten ∂²Γ/∂A² | (C1) Bulkterm mit K = G_{E₈} aus derselben U konstruieren; (D₅)₁ × (A₃)₁ ⊂ (E₈)₁ am Rand nachweisen, nicht annehmen. (C2) Diracoperator des emergenten Sektors mit dim ker D_L − dim ker D_R berechnen; Zielwert 3 vorab fixiert, Spiegelentkopplung nichtabelsch (Lüscher ist abelsch). (C3) Zweipunktfunktion der kollektiven Frameschwankung: positiver Spin-2-Pol bei p² = 0 mit zwei Helizitäten — oder negativ |

Reihenfolge: **A vor B vor C.** B ohne A wechselt das Modell unterwegs; C ohne B hat keinen Impulsraum.

---

## 7. T1–T8 konsolidiert

| Tor | Definition (Buch Kap. 10) | Konsolidierter Fortschritt (alle Stände) | Fehlt | Unbekannte |
|---|---|---|---|---|
| T1 | Herkunft von P1/P2, Dimensionen, Markierungen und Auswahlregeln | Exakte Konsequenzen des markierten Objekts; Gegenmodelle K_a, gleiche Kerne/verschiedene Spektren, 105 Paarungen; zwei Zusatzprinzipien für 1/7; ausführbares Belegungsmodell mit expliziten Eingaben | Native Notwendigkeit von Belegung, Statistik, Energien, Hilfsregistern, Zustandswahl | A |
| T2 | Native half-charge-markierte E₈-Naht mit Skalierungslimes | V_{E₈} vollständig (Cocycle, Adjunktion, OPE, ℤ₄-Sektoren, Charaktere); konforme Einbettung statt Kondo; Bulk–Rand als Architektur | Phasentreuer Adapter zum Compiler; native Moden, Level, chirale Ausführung; Bulkterm aus U | C |
| T3 | Ausgewählter lokaler unitärer Ursprung in 3 + 1 | Lorentzkegel exakt; Einanregungspropagator; Gegenmodelle d = 1…4; Kodimension-3-Kriterium; Zeit = Prozessordnung | Globale Verklebung, Impulsraum, universeller Kegel, Lorentz-Fixpunkt | B |
| T4 | Chirales Standardmodellmaß, Index, Spiegelentkopplung | Anomaliesummen; endliches Indexhindernis exakt (Index 0 bei gleich großen Räumen); Belegungsprüfung verhindert Gleichsetzung Gewichtsplatz/innere Materie | Chiraler Diracoperator, topologische Ladung 3, nichtabelsche Spiegelentkopplung | C (+ Entscheidung 5.3) |
| T5 | Wechselwirkender Kontinuumsgrenzwert | Zweizellen für alle λ exakt; Vermittlung bis 4. Ordnung mit Schranke; Yarotsky-Bereich | Lückenloser/kritischer Sektor, Streuung, Clusterstruktur | A, B |
| T6 | Alle Eichkopplungen, Neutrinotextur und Skala intern | α⁻¹ = 137.03599921684 (1.897 σ) reproduziert; Kopplungen als Steifigkeiten formuliert | Physikalisches Schema, Thomson-Transfer, Theorieunsicherheit; g₁, g₂, g₃, Yukawas, Neutrinos | C |
| T7 | Masseloser quantisierter Spin 2, zwei Helizitäten, universelle Kopplung | Notwendige Bedingungen präzisiert; Frame-Variation als Mechanismuskandidat; Weinberg schränkt nur einen vorhandenen Pol ein | Der Pol selbst | C |
| T8 | Physikalischer Zustand und gemeinsames Quellfunktional | Exakter Projektor; alle bedingten und rohen Echowerte; reversible Erweiterung; Relaxationskandidat; GNS bestimmt minimale Darstellung | Ursprung von Anfang, Reservoir, Kontrolle, Funktional | A |

---

## 8. Fünf Fugen konsolidiert

| Fuge | Erreicht | Offen |
|---|---|---|
| 1 Kopplungsstärke λ | J = 2t²/Δ > 0 uniform auf Clebsch-Kanten unter Belegung; exakter Puls; Vierkörperterm; symmetrische Konkurrenzkanäle würden J_rel = j(g₋,Δ₋) − j(g₊,Δ₊) mit unbestimmtem Vorzeichen geben | t, Δ, Abwesenheit symmetrischer Vermittler |
| 2 Graph | Clebsch exakt unter „Ort = Gewicht“; Tetramer/Kette/Clebsch sauber getrennt; Frustration unvermeidbar | Lesart (5.3), skalierende Graphfamilie (B1) |
| 3 Cross-Register | Q als Polynom trägerübergreifender Generatoren schreibbar; Sektortrennung Λ²/Sym² als Satz; isometrische Erweiterung | Primitive Zugriffserlaubnis |
| 4 Präparation | Filterkette 3/32 → 1/6 (optimal); Relaxationskandidat | Nicht-Stabilizer-Ressource aus der Quelle; kosmologischer Mechanismus |
| 5 Zeitskala | Alle Uhren auf J/ℏ bzw. t²/Δ lokalisiert; Zeit = Ereignisordnung | Absolute Skala nur mit externer M̄_Pl; Uhrwerkswahl |

---

## 9. Eingefrorene Zahlen und negative Zweige (bleiben stehen)

- α⁻¹ = 137.0359992168407125… aus α³ − 2c₃³α² − (4/5)·41c₃⁶ log(1/φ_s) = 0 mit φ_s = 1/(6π) + q(1−q)^{−5/4}, q = 48c₃⁴e^{−2α}; CODATA 2022: 137.035999177(21); Abstand **1.897 σ**. Historischer Konsistenzvergleich, keine neue Vorhersage, keine Theorieunsicherheit.
- Negativ: m_μ/m_τ ≈ 2.2 % über Polverhältnis; Higgs-Linie 129–134 GeV vs ≈ 125 GeV; A_s ≈ 1.76·10⁻⁹ (16 % unter 2.10·10⁻⁹); PS-Protonzweige um Faktoren 80 / 3.4 / 2.4 zu kurz. Die Eichgruppe nach dem Protonvergleich zu wechseln wäre keine Vorhersage.
- Vorab festgelegter endlicher Test (`Sechs` §6.3, `experiment_contract.json`, extern): ausgeglichene Sternvariante, p_behalten = 1/6, p_frisch = 1/12 pro begonnenem Versuch; 2 × 10 000 Versuche; exakte Binomialintervalle 99.5 %, Bonferroni ≥ 99 %; systematisches Budget ≤ 1/200 muss **vor** Datenerhebung zertifiziert sein. Ohne Zertifikat nicht auswertbar.
- Ursprüngliche eingefrorene Vorhersage (`Omega`, SHA 2227f0e4…): 27/512 vs 459/16384 — bleibt als eigener Vertrag archiviert.

---

## 10. Begriffsnormierung (für alle weiteren Dokumente)

| Begriff | Verwendungen in den Ständen | Normierte Bedeutung |
|---|---|---|
| Zelle | Λ⁴ℂ⁴-Tetramerzustand; 16-Orte-Clebsch-Cluster; Systemträger einer Schaltung | **Zelle** = Ω ∈ Λ⁴ℂ⁴ als lokale Verknüpfungsamplitude. Der Clebsch-Cluster heißt **C16**, die Schaltung **Protokoll** |
| Träger | Fünferträger P2; ℂ⁴-Trägerzustand; Spinorgewicht-Ort; frisches Register | **Träger** = ℂ⁴ (A₃-Fundamentaldarstellung). **Ort** = Spinorgewicht s. **Register** = Pointer/History |
| Kopplung | Kontextübergang K; Registerkopplung Q; Austausch J; Brücke λ; Vertexamplitude t | Immer mit Symbol angeben: K (Kontext), Q_C (Aufzeichnung), J (Austausch), λ (Brücke), t (Vertex), Δ (Vermittlerenergie) |
| Uhr | Familienlift c (3/12); lokale Pauli-Uhr (πℏ/J); relationale PW-Uhr (4 Anzeigen); Zweizellensignal p₁(t); Pointer-Echo | Fünf **Protokolle**, nicht eine Uhr; Zeit = kausale Ordnung der U-Ereignisse |
| Hülle | Zellconstraint (Hüllensatz); autonome Prozessbeschreibung; E₈-Gitterhülle | **Hüllensatz** (Zelle), **Gitterhülle** (E₈), sonst „Schatten“ |
| Universalraum | Prozess mit Gedächtnis; minimale beobachtbare Darstellung (GNS); Naht-Fixpunkt | **Universalraum** = die U-Regel samt Zustandsfunktional; Schatten sind seine Zugriffsklassen |
| erzwungen | algebraische Identität bis physikalische Auswahl | Nur für Identitäten; sonst *exakt*, *bedingt*, *offen*, *Gegenmodell*, *tot* |
| Register frisch/behalten | irreversible Umgebung; kohärenter Speicher; Pointer | **Zugriffsklasse** auf H_history (5.2, Punkt 2) |

---

## 11. Empfohlene Reihenfolge (keine weitere Gesamtsynthese)

1. **Korrekturen in bestehende Artefakte** (klein, sofort): Buch Kap. 5/8 um den allkoppligen Satz und E₁ ergänzen, „8J“ als Beweisgrenze markieren; Buch S. 18 „Dublett“ → „Quartett“; `universalraum-fugen-20260914/clebsch_su4.py` mit `k_per_irrep ≥ 8` für den Singulettsektor neu laufen lassen und `clebsch_su4.json`/README nachziehen; `GESAMTSYNTHESE` mit Verweis auf C3/C5 als überholt kennzeichnen; ε²-Vorfaktor in `Q_AUDIT` Teil II §4.
2. **Prüfer der Gen. 6 ins Repo holen** (`verify_reconstruction.py`, `verify.py`, `microscopic_operator.py`, `experiment_contract.json`, `evaluate_experiment.py`) als `experiments/theory-contracts/universalraum-audit-20260914/` mit den SHA-Angaben aus den Dokumenten. Bis dahin gelten die Gen.-6-Zahlen als extern gerechnet, R1–R6 ausgenommen.
3. **Entscheidung 5.3** durch Rechnung A2 (Kommutante), dann A1, A3, A4.
4. B1–B3, dann C1–C3, jeweils mit vorab fixierten Erfolgs-/Ablehnungskriterien.
5. Erst nach A und B: Frozen-Output-Vertrag für eine **neue** Zahl (Quelldefinition, Schema, externe Inputs, Transfer, Theoriefehler, Ablehnungskriterium), nicht eine weitere Nachkommastelle von α.

---

## 12. Reproduktion

Heutige Läufe (alle unter `/tmp/ur_consol/`, nicht im Repo):

```sh
# Gesamtdarstellung-Prüfer aus dem Zip
python3 verify_synthesis.py      # 210/210 passed
python3 verify_shadows.py        # 128/128 passed
# Zweizellen, Tetramer, Stern, Filter (65 536-dim Lanczos, 9 Kopplungen)
python3 two_cell_check.py
# Clebsch-Singulett-Multiplizität (24 024-dim, 6 Konfigurationen)
python3 singlet_multiplicity.py
```

Repo-Artefakte mit Bezug: `experiments/theory-contracts/universalraum-fugen-20260914/clebsch_su4.json`
(`per_irrep["(4, 4, 4, 4)"].lowest = [11.045398337068386, 11.561762122802525, 11.561762122802545,
12.456023796267301]`, k = 4), `universalraum-inversion-20260914/PROOF.md`,
`compiler-origin-audit-20260913/verification.json`, `output/pdf/tfpt_compiler_universalraum_2026-09-13_manifest.json`.

Nicht ausgeführt: Lean, RH-Suite, Hardware, PS-Schleifen, 20-Qubit-Export, vollständige C16-
Diagonalisierung in vierter Ordnung, Überlagerungs-Bloch-Banden.
