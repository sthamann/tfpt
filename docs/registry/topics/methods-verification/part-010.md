# Verification, formalization and safeguards — part 10

[Topic entry](../methods-verification.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Reproduktionsbelege

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:341-368](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L341) · `section:d85f88be07929d79fd46` · subsection

late_a/verify.py prüft elf eingefrorene Eingaben, führt die ν1-ν5- Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf. Es gibt 46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische Prüfungen und 10 numerische Konsistenzprüfungen, separat dazu 1239 ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine unabhängigen mathematischen Theoreme.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json#L1) · explicit_file_citation

## Nachtragsprüfung B: Feldprojektor und Lorentz-Händigkeit

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex:369-371](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/013-subsection-beweisumfang-label-beweisumfang.tex#L369) · `section:24c5dbad4c6fe3d45612` · section

No opening prose excerpt; see the source.

## Reproduktion

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/014-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:257-279](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/014-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L257) · `section:1912b4c782961b3d7159` · subsection

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei Quellenpins sowie 36 exakte Bedingungen pro Modus, keine numerischen Bedingungen. Normaler Lauf und -OO ergeben byte-identische JSON-Ausgaben; Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv. Die vollständigen Matrizen stehen in late_field.normal.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py#L1) · explicit_file_citation

## Übernahmeurteil

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/014-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:286-307](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/014-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L286) · `section:a7c3414e2e89d8cff6ee` · subsection

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere Gesprächszusammenfassung. Er bringt keinen neuen H-Term, keine neue Operationsquelle und keinen neuen Transferbeweis. Seine wesentlichen mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendi

Explicit source references:

- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation

## 9. Aktueller Stand T1 bis T8

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/017-subsection-8-die-fundamentale-frage-was-fehlt.tex:56-110](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/017-subsection-8-die-fundamentale-frage-was-fehlt.tex#L56) · `section:6ed2c3a6c24a0590bc37` · subsection

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

## Historischer Anhang: vollständige Fassung v1.6.6

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/019-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:86-94](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/019-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L86) · `section:c699c91fe3777a13f172` · section

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/019-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:199-278](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/019-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L199) · `section:3194a2833ec95e9900fe` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex:45-95](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex#L45) · `section:8f0745b9a7bf731d3833` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex:130-151](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex#L130) · `section:fd81b831cecc5146c252` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex:155-162](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/021-subsubsection-7-4-was-nicht-automatisch.tex#L155) · `section:c9ba288e74a3ebc0ae1e` · section

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/022-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:221-247](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/022-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L221) · `section:4ca2d46d3aa54010bc30` · subsection

Der ältere, gepinnte Beweis lautet: Für Δ 0 und 0 g /Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:1-28](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L1) · `section:83c67d603b0034b137a9` · subsection

contracted_krylov.cpp ist der unabhängige ganzzahlige Kontraktionskern. verify.py prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in audit.json und audit_optimized.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json#L1) · explicit_file_citation

## Anhang C: minimaler Transfer und seine Quellen-Grenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:29-31](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L29) · `section:74a69e796027090f0935` · section

No opening prose excerpt; see the source.

## Minimaler Ursprungsstrang: geteilte Moden und ein echter nativer Vierzustandskanal

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:32-37](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L32) · `section:1becce954dd14f956faa` · section

No opening prose excerpt; see the source.

## Ergebnis und Reichweite

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:38-71](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L38) · `section:c8c4db91e43840400fd1` · subsection

Es gibt zwei verschiedene Ergebnisse, die ausdrücklich nicht verwechselt werden dürfen:

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:72-110](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L72) · `section:6b690ec8e752e7ce51d0` · subsection

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

## 2. Exakter CAR-Baustein aus einem geteilten Boson und Fermion

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:111-173](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L111) · `section:02ba22bfb1e82e46b50c` · subsection

Betrachtet werden drei CAR-Moden [formula in source] , ein CCR-Boson b und

## Vollständige Transferrechnung im Vergleichsmodell

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:174-210](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L174) · `section:af464685433b314ff708` · subsubsection

Im effektiven Einteilchenraum und bei K=1 lautet die Matrix

## Die direkte Quellen-Grenze

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:211-223](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L211) · `section:59222c74d8a2c4243536` · subsubsection

Die tatsächliche native W-Zeile enthält jeweils acht disjunkte Fermionpaare, also 16 verschiedene Marken. Eine einzelne Zeile enthält deshalb niemals zugleich [formula in source] und [formula in source] mit [formula in source] . Das ist an allen 60 Zeilen exakt geprüft.

## 3. Exakter Vierzustandskanal mit dem vollständigen nativen W

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:224-308](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L224) · `section:44fc24a904f33f20b768` · subsection

universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz,

## 4. Strenge vollständige Transfergrenze im tatsächlichen W-Zeugen

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex:309-389](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/023-subsection-reproduktion-und-status-label-reproduktion-un.tex#L309) · `section:16aa60af20e90a63bb50` · subsection

Wähle den vorhandenen Prüfquotienten [formula in source] und die ausdrücklich neu gesetzte Mischerstärke

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:249-288](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L249) · `section:fb15d80718ced13d9615` · subsection

verify.py prüft 307 Bedingungen, verwendet keine Python-Assertions und reproduziert normal sowie mit -OO byteidentische JSON-Ergebnisse. Die Prüfung enthält:

## Anhang D: vollständiger Überlappungs-Audit

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:289-291](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L289) · `section:a6c27f51e173b47bc186` · section

No opening prose excerpt; see the source.

## Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:292-311](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/024-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L292) · `section:7439692fadc68ce2b78a` · section

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py#L1) · explicit_file_citation

## Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/025-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex:259-273](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/025-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex#L259) · `section:fd90691972ef39acb2d1` · section

September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes 59dc0059-8914-48ca-953d-85933f66e00b, kein neuer RH-Beweis und kein neuer arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## 1. Was die endliche Bank tatsächlich ausschließt

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/025-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex:283-311](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/025-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex#L283) · `section:68604973d1f583335217` · subsection

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator mit 64 Fermion- und 60 Bosonmoden, Δ 0. Der Hilbertraum ist wegen der Bosonen nicht endlichdimensional. Endlich ist die Zahl der Moden. Mit C=960g²/Δ folgt aus quadratischem Ergänzen

## Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex:84-92](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex#L84) · `section:c6834d91a743322cbb61` · section

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

## 1. Welche Quellen zusammengeführt werden

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex:163-208](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex#L163) · `section:b99a78128c4df5f41a04` · subsection

Die Benutzeranlage addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt, eingefroren unter sources/user_attachment.txt. Die externe Untersuchung Universalraum_Beweisversuch_2026-09-15.md: Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung. Die externe Untersuchung Universalraum_Urspruenglicher_Austausch_2026-09-15.md: interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beis

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt#L1) · explicit_file_citation

## 3.3 Das ältere 99,8718-\%-Beispiel ist ein anderer Träger

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex:320-330](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/026-subsection-3-die-richtige.tex#L320) · `section:40d479417316e7b522ce` · subsubsection

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs Zustände sind der vollständige Gausssektor eines Vierfermion-Modells mit einem Link. Der zertifizierte Wert bei [formula in source] betrifft diesen Parent und diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist davon unabhängig und benutzt die ta

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/028-subsection-8-w-hrend-der-arbeit-entdeckte-nderung-kommut.tex:321-353](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/028-subsection-8-w-hrend-der-arbeit-entdeckte-nderung-kommut.tex#L321) · `section:c5a5f275e3387c45650e` · subsection

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig; Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg. Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

## Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/029-subsubsection-5-1-anomalien-label-anomalien.tex:139-149](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/029-subsubsection-5-1-anomalien-label-anomalien.tex#L139) · `section:c9b69df333f6d33064c0` · section

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

## 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/029-subsubsection-5-1-anomalien-label-anomalien.tex:248-304](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/029-subsubsection-5-1-anomalien-label-anomalien.tex#L248) · `section:7c7885d45941e68b5507` · subsubsection

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch mit neu kompiliertem Quellcode berechnet:

## 6. Der Polsatz und seine zusätzliche Verschärfung

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/030-subsection-5-dieselbe-antwort-auf-demselben.tex:125-174](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/030-subsection-5-dieselbe-antwort-auf-demselben.tex#L125) · `section:4c8761e40146c1b989dc` · subsection

Der eingegangene Beweis verwendet [formula in source] . Invarianz und Besetzung ergeben

## 3. WP-C: Relativistisches Feldwörterbuch (fertig, 2161 exakte Guards, -OO-stabil)

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/032-subsection-0-gesamtlage-zwei-spuren-label-gesamtlage-zwe.tex:154-205](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/032-subsection-0-gesamtlage-zwei-spuren-label-gesamtlage-zwe.tex#L154) · `section:40ca3a041da6aca37d9d` · subsection

@ > p( - 4 ) * 0.3000 > p( - 4 ) * 0.4000 > p( - 4 ) * 0.3000@ Kanal & Norm² pro Zeile & Status \\ Skalar, gleichhändig ε_\αβ\ψψ & 0 (alle 60 Zeilen, exakt) & verboten \\ Skalar, gepunktet (0,0) & 0 & verboten \\ (1,0) symmetrisch \I, σˣ, σᶻ\ & je 64, Summe 192 & erlaubt - der Vertex ist rein (1,0)+h.c. \\ (0,1) konjugiert & je 64 & erlaubt \\

## 6. Kreuzvalidierung der beiden Spuren

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/032-subsection-0-gesamtlage-zwei-spuren-label-gesamtlage-zwe.tex:295-333](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/032-subsection-0-gesamtlage-zwei-spuren-label-gesamtlage-zwe.tex#L295) · `section:c11ccebd9d03dce1530e` · subsection

@ > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500 > p( - 6 ) * 0.2500@ Befund & Meine Session & Parallelsession & Status \\ N=3-Zerlegung (7 Blöcke, Mults 2,2,2,1,1,1,1) & ✓ & ✓ & identisch \\ Casimirwerte (je Block) & (45,15), (85,15), & C = (C_S+C_U)/4 = 15, 25, 45, 21, 31, 45, 45 & identisch (zwei Normierungen) \\ Kommutant S1 (volle Symmetrie) & 7 & 7 & identisch \\ Kommutant S0 (X, N_b) & 1 452 961 7

## Nutzerquelle C: Multiplizitaeten und Z4

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/033-section-nutzerquelle-c-multiplizitaeten-und.tex:1-332](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/033-section-nutzerquelle-c-multiplizitaeten-und.tex#L1) · `section:967a2574b80f1093c610` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle D: fundamentale Reduktion

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/034-section-nutzerquelle-d-fundamentale.tex:1-180](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/034-section-nutzerquelle-d-fundamentale.tex#L1) · `section:3871de63a8f2ae8a0aa6` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle E: gemeinsamer ausfuehrbarer Prozess

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/035-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:1-363](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/035-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L1) · `section:437eab5c22c17dba1ec3` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## Nutzerquelle F: Operationssatz, Grundzustand und Feldwoerterbuch v1.6.3

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/035-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex:364-370](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/035-section-nutzerquelle-e-gemeinsamer-ausfuehrbarer.tex#L364) · `section:dc0f94519145c443519c` · section

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

## 8. Die jetzt entscheidenden Prüfungen

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/037-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:63-89](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/037-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L63) · `section:0b1d4ed09aadcc68c2ae` · subsection

Untergrenzen verschärfen. Die Casimir-Schranke trennt N=64 bei 1/20 nicht von N=62 und N=66. Eine Jacobi-Vergleichsschranke mit rigorosen Normschranken für TT† je Bosonzahl oder eine Temple-Schranke auf der Ritz-Kette würde den Beweisbereich anheben. Den Zwei-Boson-Singulettraum ausschreiben. w₂ ist der erste Zeuge; die volle Lanczos-Kette von H (nicht nur von T†) ab Tiefe 4 braucht w₂ und seine Nachfolger. Operation

## 9. Verifikation und nicht übernommene Behauptungen

[documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/037-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex:90-116](../../../../documents/experiments--theory-contracts--universalraum-source-composition-20260915--tmp--pdfs--TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9/sections/037-subsection-6-spurnetzwerk-normen-label-spurnetzwerk-norm.tex#L90) · `section:e47ac6958bb9f4a17992` · subsection

replay.py führt fünf Prüfer normal und unter -OO aus und verlangt byteidentische Ausgaben; Status, Hashes und Guardsummen stehen in replay_manifest.json. Guardzahlen zählen Prüfbedingungen, keine unabhängigen Theoreme. Exakt heißt ganzzahlig/rational; numerisch heißt float64 mit Toleranz-Guard (Ritz-Eigenwerte ab 3×3, Observablen, Erste-Moment-Auswertungen).

## 1. Was die erneute Grundlagenlektüre verändert

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/001-section-tfpt-universalraum-den-verlorenen-spin-lift-wied.tex:44-89](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/001-section-tfpt-universalraum-den-verlorenen-spin-lift-wied.tex#L44) · `section:0794eefc4054e642456a` · subsection

Die erneute Lektüre umfasst die Grundkonstruktion in README.md, docs/THEORY.md, origin_theory.tex, die D5/A3- und Pascal-Konstruktion, die aktuelle Standardmodell-Masterformel und ihre Projektionsgrenzen, den Kaskadenvergleich im E8-Audit, die Frontier-Verträge sowie die einschlägigen Abschnitte der Archivfassung paper_v1_06_01_09_2025.tex. Nicht sämtliche mehr als 30.000 Zeilen der aktuellen Theorie samt allen einge

Explicit source references:

- [README.md](../../../../README.md#L1) · explicit_file_citation
- [verification/v480_multilocal_four_interval.py](../../../../verification/v480_multilocal_four_interval.py#L1) · explicit_file_citation
- [docs/THEORY.md](../../../../docs/THEORY.md#L1) · explicit_file_citation

## 8.2 Ein eindeutiges mikroskopisches Netz ist nicht zwingend nötig

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex:162-192](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex#L162) · `section:1fcd3ec291c3b502e674` · subsubsection

Die Petersen-/Prisma-Gegenmodelle beweisen eine endliche Unterbestimmtheit, aber keine Verschiedenheit aller denkbaren großskaligen Grenztheorien. Unterschiedliche Mikroregeln können derselben Universalitätsklasse angehören. Das ist ein wesentlicher Grund, nicht immer feinere Graph-Eindeutigkeit zu verlangen, bevor eine physische Grenzrechnung begonnen wird. Siehe den ursprünglichen RG-Rahmen von https://theory.tifr.

## 9. Was die alte E8-Kaskade wirklich beisteuert

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex:193-241](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex#L193) · `section:877ac061657cfd573a19` · subsection

Die gewünschte Archivdatei ist ein LaTeX-Umschlag einer ausdrücklich als bestmögliche PDF-Textextraktion bezeichneten 81-seitigen Fassung. Einige Formeln und Figuren sind in dieser Darstellung beschädigt oder fehlen. Aus solchen Schäden werden hier keine mathematischen Gegenbeweise konstruiert.

Explicit source references:

- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## 10. Einstein, Noether und Dirac als Arbeitsprinzipien

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex:242-265](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex#L242) · `section:8473c1181bddf2dbf3df` · subsection

Noether: Die erhaltene Ladung [formula in source] ist hier kein dekoratives Etikett. Sie reduziert den globalen Grundzustandsvergleich auf untere, mittlere und obere Ladungssektoren und macht den kurzen Beweis möglich.

## 13. Reproduktion und Lesereihenfolge

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex:349-368](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/002-subsection-7-derselbe-grundzustand-besitzt-eine-kontroll.tex#L349) · `section:1d121fa86acdab3e383f` · subsection

verify_spin_lift.py prüft native Tensorpins, die vollständige benötigte Casimir-Grundlage, die N3-Reduktion, Vorzeichenklassen, unabhängige CAR-Kontrollen, exakte Momente, rationale Restkonstanten sowie die Operations- und Archivpräzisierungen. replay.py wiederholt diese Rechnung normal und optimiert und führt den historischen v480-Zeugen separat aus. Der vollständige analytische Grundzustands-/Antwortbeweis steht in

Explicit source references:

- [verification/v480_multilocal_four_interval.py](../../../../verification/v480_multilocal_four_interval.py#L1) · explicit_script_identifier

## 14.2 Die modulare Zeitidee ist relevant, aber noch nicht unser fehlender Hamiltonoperator

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/003-subsection-14-nachpr-fung-der-beiden-zuletzt-zugeschickt.tex:56-125](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/003-subsection-14-nachpr-fung-der-beiden-zuletzt-zugeschickt.tex#L56) · `section:1a03b23c5e989101be90` · subsubsection

Die vorgeschlagene Verbindung zu Connes und Rovelli ist sachlich richtig: Ihre https://arxiv.org/abs/gr-qc/9406019Thermal-Time-Arbeit postuliert eine physische Interpretation des vom Zustand bestimmten modularen Flusses. Das ist eine physische Hypothese auf Grundlage eines mathematischen Satzes, kein allgemeiner Beweis, dass jeder modulare Fluss eine physische Uhr ist.

## Abgeschlossener eigener Replay

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/003-subsection-14-nachpr-fung-der-beiden-zuletzt-zugeschickt.tex:354-369](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/003-subsection-14-nachpr-fung-der-beiden-zuletzt-zugeschickt.tex#L354) · `section:5b645deac4d9e5f4f4ea` · subsubsection

1669 explizite Bedingungen normal und optimiert, byteidentische Ergebnisdateien. Darin enthalten sind wiederholte Quellen-, Vorzeichen- und CAR-Prüfungen; die Zahl zählt keine unabhängigen Theoreme. Der allgemeine Grundzustands- und Antwortbeweis ist in Abschnitten 5-7 ausgeschrieben. Die Zusatzprüfung der beiden späten Perspektivtexte umfasst 61 weitere Bedingungen, ebenfalls normal/optimiert byteidentisch. Ihre all

## Historischer Bestand: vollständige Hauptfassung v1.6.9

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/004-section-historischer-bestand-vollst-ndige-hauptfassung.tex:1-11](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/004-section-historischer-bestand-vollst-ndige-hauptfassung.tex#L1) · `section:78361d4ce34a5362eac3` · section

Die vorherige Hauptfassung folgt vollständig und unverändert. Ihr offener allgemeiner Quellen-/Grundzustandsstatus wird durch v1.6.10 nur für den vorn ausdrücklich definierten Viererzyklus und Kopplungsbereich ergänzt. Aussagen über N=64, g/Delta=1/20, Lorentzfelder und größere Systeme bleiben in ihrem ursprünglichen Vertrag. Die neue N=256-Konstruktion darf nicht rückwirkend in diese alten Sätze eingesetzt werden.

## Vollständiger Beweis: höhere Antwort und positive Kopplungsmatrix

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/005-subsection-7-was-die-vier-rechnungen-gemeinsam-haben-und.tex:206-208](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/005-subsection-7-was-die-vier-rechnungen-gemeinsam-haben-und.tex#L206) · `section:a843b3ad750f655cedf6` · section

No opening prose excerpt; see the source.

## 9. Reproduktion und Grenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/006-subsection-5-allgemeine-car-identit-t-auf.tex:169-185](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/006-subsection-5-allgemeine-car-identit-t-auf.tex#L169) · `section:75a5b17d46805571db9d` · subsection

verify_composition.py führt 67 explizite exakt arbeitende Prüfbedingungen aus, einschließlich Quellenpins und Strukturguards. Es gibt keine numerischen Toleranzprüfungen. Die allgemeine Formel und ihre Inversion sind oben algebraisch hergeleitet; drei vollständige N=3-CAR-Aufbauten kontrollieren Normalisierung, Vorzeichen und komplexe Konvention unabhängig.

## 7. Reproduktion und Prüfgrenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/007-subsection-3-exakt-geschlossener-ablauf-und-messbarer.tex:178-207](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/007-subsection-3-exakt-geschlossener-ablauf-und-messbarer.tex#L178) · `section:3734a1f46b6c06b9d17f` · subsection

python3 verify.py –output results_normal.json und python3 -OO verify.py –output results_optimized.json; REPLAY.json versiegelt Exitcodes, Prüferhash und identische Resultatbytes. replay.py führt beide Varianten lokal aus. Keine Netz-/Live-Repo-Imports, keine große Grundzustandsdiagonalisierung und keine Änderung älterer v1.6.8-Dateien.

## 6. Verifikation und verbleibender Herkunftsschritt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/008-subsection-3-schaltbarkeit-und-arbeit-werden.tex:150-193](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/008-subsection-3-schaltbarkeit-und-arbeit-werden.tex#L150) · `section:216784918ef017883b87` · subsection

Für den parallelen Quellvergleich ist zusätzlich ein dimensionsunabhängiger kleiner Blocksatz geprüft: Bei [formula in source] und einem normierten Eingang v auf der Bosonseite ist die erste und dritte Ableitung der Boson-Überlebenswahrscheinlichkeit null, während [formula in source] . Somit gilt [formula in source] . Dieser reine Blocksatz verbindet dieselbe Nb-Auslese mit einem Kopplungs-Gramoperator; er leitet die

## Nachgereichte Texte: neue Norm, korrigierte Zustandszuordnung und Feldadapter

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/011-subsubsection-warum-nur-ein-schatten-auch-nach-beliebig-.tex:290-299](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/011-subsubsection-warum-nur-ein-schatten-auch-nach-beliebig-.tex#L290) · `section:7ad9bcc07d5bf9f5c569` · section

Die drei während der laufenden Prüfung nachgereichten Texte wurden vollständig gelesen und unverändert eingefroren. Sie sind keine Anweisungen, Ergebnisse ungeprüft zu übernehmen. Zwei Texte vereinfachen ältere Arbeitsstände stark; die dritte längere Forschungsnotiz enthält ausführlichere Beweise einer bereits bekannten grundsätzlichen Diagnose.

## 3. Die kleinste zusätzliche Operation ist schon algebraisch ausreichend

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex:20-67](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex#L20) · `section:6286b00f90233e51fe93` · subsection

Dabei ist der zweite Bosonindex BAR(A). Es gibt dreißig solche ungeordneten Paare. Die vollständige Invarianz von η wird an allen 45+15 ursprünglichen Liegeneratoren geprüft. Die 60 verschiedenen Bosongewichte und der zusammenhängende Lie-Wirkungsgraph beweisen zusätzlich, dass diese Paarung bis auf einen Skalar eindeutig ist.

## Anschluss an das nachgereichte Forschungspaper

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex:219-231](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex#L219) · `section:e0ea4cb658f768d8b822` · subsubsection

Abschnitt 9 des nachgereichten Papers benutzt dasselbe Prinzip einer mitgerechneten Ladungsreferenz. Sein dortiger N=9-Vierzustandstransfer erhält mit der neuen Referenz eine einzelne innere Cartanladung. Unsere Konstruktion betrifft stattdessen N und erhält die vollständige innere Gruppe, erzeugt aber keine räumliche Übertragung. Sie ersetzt den dortigen Transferzeugen nicht und beweist dessen native Herkunft nicht.

## 7. Reproduktion und Beweisumfang

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex:290-325](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/013-subsubsection-instrumente-und-die-genaue.tex#L290) · `section:47648ea2c2cbecf26795` · subsection

Benötigt werden Python, NumPy, SciPy und SymPy. Der Replay liest nur die eingefrorenen Eingaben und braucht weder das ursprüngliche Repository noch Netzwerkzugriff. freeze.py ist nur das Herkunftswerkzeug für die erste Archivierung und gehört nicht zum wissenschaftlichen Replay.

## 2. Exakter Rangbeweis am Tensor

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/014-subsection-1-ein-gemeinsamer-tr-ger-mehrere.tex:56-103](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/014-subsection-1-ein-gemeinsamer-tr-ger-mehrere.tex#L56) · `section:6693e70f7d2c5c59a1a7` · subsection

Die Datei enthält zehn symmetrische 16×16-Matrizen β_k. Mit den sechs antisymmetrischen 4×4-Farbmatrizen ε_c gilt eintragsweise

## 5. Prüfung und unveränderte offene Grenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/015-subsection-2-lokale-algebra-und-ehrlicher.tex:169-206](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/015-subsection-2-lokale-algebra-und-ehrlicher.tex#L169) · `section:bda831a44803967ef835` · subsection

verify_causal.py benutzt explizite Fehlerbedingungen, keine abschaltbaren Assertions. Normaler Python-Lauf und python -OO, jeweils mit Warnungen als Fehler, erzeugen byte-identische JSON-Ergebnisse. Der optimierte Lauf wurde aus einem anderen Arbeitsverzeichnis gestartet; die Quelle wird relativ zum Prüfprogramm aufgelöst. Abhängigkeiten: NumPy, SymPy und SciPy.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/result_OO.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_causal.py#L1) · explicit_file_citation

## Beweisumfang

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:1-20](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L1) · `section:0d70b3cfeb888957aca1` · subsection

verify_common3.py prüft den eingefrorenen W, die Isometrie, alle Intertwining-Identitäten, den ausdrücklichen n5-Leckterm, die zwei kausalen Endwahrscheinlichkeiten, beide symbolischen Determinanten und die rationale Inversen-Normschranke. common3.json und common3_OO.json sind die normalen und optimierten Replays. Der frühere Bericht und Prüfer wurden nicht geändert.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/verify_common3.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3_OO.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/causal/common3.json#L1) · explicit_file_citation

## Nachtragsprüfung A: neue fünfte Norm und richtige Antwortzustände

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:21-23](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L21) · `section:80f75c30f062ea23a512` · section

No opening prose excerpt; see the source.

## Nachtrag A: Was am neuen v1.6.3-Erklärtext wirklich neu ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:24-26](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L24) · `section:f9e99cd2d3f268cbf207` · section

No opening prose excerpt; see the source.

## Urteil

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:27-45](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L27) · `section:971e96d0b0e4252c6f98` · subsection

Ja, ein belastbarer neuer Rechenschritt ist enthalten: Die zuvor fehlende Norm ν5 liegt jetzt mit passendem Quellstand vor. Wir haben ν1 bis ν5 frisch durch die ursprüngliche exakte Spurnetzwerkrechnung reproduziert und daraus unabhängig strengere rationale Ritzgrenzen gewonnen. Die übrigen großen Aussagen des Textes sind teils bereits bekannt, teils durch v1.6.7 korrigiert. Besonders problematisch ist die Vermischun

## 1. ν5 ist jetzt ein Ergebnis, nicht mehr nur eine Programmeinstellung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:46-99](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L46) · `section:751b6eabd39fca269cc8` · subsection

Der v1.6.7-Snapshot hatte zu Recht festgehalten, dass damals norms_by_traces.json und ein abgeschlossener zugehöriger Replay fehlten. Dieser konkrete Quellenstand hat sich geändert. Der neue Checkerhash be72c728e128ae0ef605980a5bae88ea31049e29e2fd17c43167fbd6ad1d0c89 passt jetzt zum Ergebnis; auch der Common-Hash stimmt. Die vorhandenen normalen und optimierten Normausgaben sind byteidentisch. Der gespeicherte JSON-I

## 2. −1,138 ist eine echte bessere Variationsgrenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:100-170](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L100) · `section:0749600b3d2a03e44c1a` · subsection

Die Unterräume aus den normierten bosonweise geordneten Vektoren [formula in source] sind nicht invariant, aber sie sind gültige Variationsräume. Da unterschiedliche k orthogonal sind und H die Bosonzahl höchstens um eins ändert, besitzt die Kompression auf v0, ,v5 exakt

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## 3. Der Text vermischt drei verschiedene Näherungszustände

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:171-236](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L171) · `section:91cb55a1fd2b0834520c` · subsection

Die neuen kleinen Matrizen wurden unabhängig diagonalisiert. Sie bestätigen die gespeicherten numerischen Ritz-Erwartungswerte, aber nicht deren Umdeutung zu exakten Eigenschaften von Ω.

Explicit source references:

- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## Die mittleren Antwortenergien lassen sich ohne riesige Zustandsdateien korrigieren

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:237-276](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L237) · `section:91351fb6a30f88ebb0c8` · subsubsection

Aus den CAR folgen für jeden normierten G-Singulettzustand mit N=64:

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation

## 4. Was bereits überholt ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:277-323](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L277) · `section:90ec09e62f7374419228` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage der Anlage & Prüfung \\ Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt & Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. \\ Mit allen gewährten inneren Kon

## 5. Was daran spannend ist und was als nächstes trägt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:324-340](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L324) · `section:a4a034f9bf291416ebb0` · subsection

Der gute neue Schritt ist die tatsächlich abgeschlossene fünfte Spurnetzwerk-Norm mit der daraus folgenden stärkeren strengen Energie- und Entnahmeschranke. Hinzu kommt unsere kleine CAR-Auswertung, die die geladenen ersten Momente auf den richtigen größeren Ritz-Zustand hebt. Das verbessert nachprüfbar die Rechnung im bestehenden nativen Modell.

## Reproduktionsbelege

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:341-368](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L341) · `section:a278949d0f68d35bb6a5` · subsection

late_a/verify.py prüft elf eingefrorene Eingaben, führt die ν1-ν5- Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf. Es gibt 46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische Prüfungen und 10 numerische Konsistenzprüfungen, separat dazu 1239 ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine unabhängigen mathematischen Theoreme.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py#L1) · explicit_file_citation

## Nachtragsprüfung B: Feldprojektor und Lorentz-Händigkeit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:369-371](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L369) · `section:0ce6fc96b738e14f2bf6` · section

No opening prose excerpt; see the source.

## Reproduktion

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:257-279](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L257) · `section:c6260e25e90627165dc9` · subsection

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei Quellenpins sowie 36 exakte Bedingungen pro Modus, keine numerischen Bedingungen. Normaler Lauf und -OO ergeben byte-identische JSON-Ausgaben; Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv. Die vollständigen Matrizen stehen in late_field.normal.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json#L1) · explicit_file_citation

## Übernahmeurteil

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:286-307](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L286) · `section:f4e2353eddc385df8327` · subsection

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere Gesprächszusammenfassung. Er bringt keinen neuen H-Term, keine neue Operationsquelle und keinen neuen Transferbeweis. Seine wesentlichen mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendi

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt#L1) · explicit_file_citation

## 9. Aktueller Stand T1 bis T8

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:56-110](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L56) · `section:be988edcf21afe0f230a` · subsection

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

## Historischer Anhang: vollständige Fassung v1.6.6

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:86-94](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L86) · `section:6c6e891c0496b6a29275` · section

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:199-278](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L199) · `section:69587dcaabdec10ff0b4` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:45-95](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L45) · `section:647b51d5509c9a9c81db` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:130-151](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L130) · `section:54f4776c1da819c64ef6` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:155-162](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L155) · `section:a44fbc0812f8307d9880` · section

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:221-247](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L221) · `section:884e73a5ff01a268e3c2` · subsection

Der ältere, gepinnte Beweis lautet: Für Δ 0 und 0 g /Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:1-28](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L1) · `section:9f672783c6423ece6888` · subsection

contracted_krylov.cpp ist der unabhängige ganzzahlige Kontraktionskern. verify.py prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in audit.json und audit_optimized.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/ground_field_audit/audit_optimized.json#L1) · explicit_file_citation

## Anhang C: minimaler Transfer und seine Quellen-Grenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:29-31](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L29) · `section:e1ea9047acf99bcfeabc` · section

No opening prose excerpt; see the source.

## Minimaler Ursprungsstrang: geteilte Moden und ein echter nativer Vierzustandskanal

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:32-37](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L32) · `section:c886bb7b9c9833a451ac` · section

No opening prose excerpt; see the source.

## Ergebnis und Reichweite

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:38-71](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L38) · `section:38d8b53d29c06cce50cf` · subsection

Es gibt zwei verschiedene Ergebnisse, die ausdrücklich nicht verwechselt werden dürfen:

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:72-110](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L72) · `section:12a65f17cd329e1e2ad5` · subsection

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

## 2. Exakter CAR-Baustein aus einem geteilten Boson und Fermion

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:111-173](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L111) · `section:edcf77c78f81c5bdcd23` · subsection

Betrachtet werden drei CAR-Moden [formula in source] , ein CCR-Boson b und

## Vollständige Transferrechnung im Vergleichsmodell

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:174-210](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L174) · `section:d05e7d0ed3cc010464bd` · subsubsection

Im effektiven Einteilchenraum und bei K=1 lautet die Matrix

## Die direkte Quellen-Grenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:211-223](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L211) · `section:e9bc91d94034038e78eb` · subsubsection

Die tatsächliche native W-Zeile enthält jeweils acht disjunkte Fermionpaare, also 16 verschiedene Marken. Eine einzelne Zeile enthält deshalb niemals zugleich [formula in source] und [formula in source] mit [formula in source] . Das ist an allen 60 Zeilen exakt geprüft.

## 3. Exakter Vierzustandskanal mit dem vollständigen nativen W

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:224-308](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L224) · `section:f406da5b91f370f65406` · subsection

universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz,

## 4. Strenge vollständige Transfergrenze im tatsächlichen W-Zeugen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex:309-389](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/026-subsection-reproduktion-und-status-label-reproduktion-un.tex#L309) · `section:8616471cb8a8b6312533` · subsection

Wähle den vorhandenen Prüfquotienten [formula in source] und die ausdrücklich neu gesetzte Mischerstärke

## Reproduktion und Status

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:249-288](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L249) · `section:78490bc57ecf41018a59` · subsection

verify.py prüft 307 Bedingungen, verwendet keine Python-Assertions und reproduziert normal sowie mit -OO byteidentische JSON-Ergebnisse. Die Prüfung enthält:

## Anhang D: vollständiger Überlappungs-Audit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:289-291](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L289) · `section:be11e94265de18da4b05` · section

No opening prose excerpt; see the source.

## Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex:292-311](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/027-subsection-5-was-dies-f-r-die-fundamentale-suche.tex#L292) · `section:d860b2e249489700477e` · section

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/overlap_audit/check_overlap.py#L1) · explicit_file_citation

## Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/028-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex:259-273](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/028-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex#L259) · `section:b1559e93664b821ba487` · section

September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes 59dc0059-8914-48ca-953d-85933f66e00b, kein neuer RH-Beweis und kein neuer arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## 1. Was die endliche Bank tatsächlich ausschließt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/028-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex:283-311](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/028-subsection-3-noch-wichtiger-ein-berlappungsmatrixelement.tex#L283) · `section:c0454137144db03e0764` · subsection

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator mit 64 Fermion- und 60 Bosonmoden, Δ 0. Der Hilbertraum ist wegen der Bosonen nicht endlichdimensional. Endlich ist die Zahl der Moden. Mit C=960g²/Δ folgt aus quadratischem Ergänzen

## Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex:84-92](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex#L84) · `section:d2a156e75004b899c2d6` · section

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

## 1. Welche Quellen zusammengeführt werden

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex:163-208](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex#L163) · `section:b6d20e6827aeff2134ad` · subsection

Die Benutzeranlage addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt, eingefroren unter sources/user_attachment.txt. Die externe Untersuchung Universalraum_Beweisversuch_2026-09-15.md: Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung. Die externe Untersuchung Universalraum_Urspruenglicher_Austausch_2026-09-15.md: interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beis

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/sources/user_attachment.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md](../../../../experiments/theory-contracts/universalraum-two-bank-transfer-20260915/LATE_AUDIT.md#L1) · explicit_file_citation

## 3.3 Das ältere 99,8718-\%-Beispiel ist ein anderer Träger

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex:320-330](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/029-subsection-3-die-richtige.tex#L320) · `section:24c79216c6a79f0c724c` · subsubsection

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs Zustände sind der vollständige Gausssektor eines Vierfermion-Modells mit einem Link. Der zertifizierte Wert bei [formula in source] betrifft diesen Parent und diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist davon unabhängig und benutzt die ta

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/031-subsection-8-w-hrend-der-arbeit-entdeckte-nderung-kommut.tex:321-353](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/031-subsection-8-w-hrend-der-arbeit-entdeckte-nderung-kommut.tex#L321) · `section:26c294848c4ee57b51a8` · subsection

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig; Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg. Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

## Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/032-subsubsection-5-1-anomalien-label-anomalien.tex:139-149](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/032-subsubsection-5-1-anomalien-label-anomalien.tex#L139) · `section:eb47e1c679e877d523c3` · section

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.
