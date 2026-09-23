# TFPT / Universalraum — Quellenkomposition v1.6.9

## Lesen

- `RESULTS.md`: aktuelle gemeinsame Einordnung und T1–T8-Zuordnung.
- `COMPOSITION.md`: vollständiger eigener CAR-/Gram-/Inversionsbeweis.
- `agents/source/REPORT.md`: ursprüngliche Quelle und exaktes Zwei-Chart-Modell.
- `agents/protocol/REPORT.md`: kleiner Eingriff und Recorder samt Arbeit.
- `agents/field/REPORT.md`: Lorentzadapter, Vertexprüfung und freier Nulltest.
- `UPDATE.md`, `EINFACH.md`: kurze beziehungsweise einfach erklärte Fassung.
- `deliverables/`, `output/pdf/`: vollständige Hauptfassung und beide Kurzfassungen.

Die gesamte v1.6.8-Hauptfassung und ihr früheres Prüfpaket liegen unverändert unter `sources/`. Historische Behauptungen sind nur mit ihrem damaligen Modellvertrag zu lesen; den aktuellen Status liefern die vorangestellten v1.6.9-Kapitel.

## Mathematische Reproduktion

Python mit NumPy, SciPy und SymPy. Kein Netzwerk, kein Graphdienst, keine ursprünglichen absoluten Repository-Pfade erforderlich:

```sh
python3 -B replay.py
```

Vier Stränge werden normal und mit `-OO` ausgeführt, Warnungen sind Fehler. Die Ergebnisse müssen bytegleich sein. Der gemeinsame Replay zählt 514 eigene exakt arbeitende Bedingungen und vier numerische Kontrollen pro Modus. Separat: 17 native und 1073 P0/P1-Quellguards sowie 13 unabhängige kleine Bitmasken-CAR-Kontrollen. Prüfer-, Ergebnis- und Eingabehashes stehen in den Manifesten. Die gesamte alte v1.6.8-Suite wird nicht erneut ausgeführt.

`freeze.py` und die agenteneigenen Freeze-Skripte dokumentieren ausschließlich die ursprüngliche Eingabesicherung. Sie werden nach dem Entpacken nicht benötigt. Die endgültige ZIP-Lieferung wird aus einem frisch entpackten Paket erneut abgespielt. `package_files.json` sichert sämtliche enthaltenen Dateien.

## Dokumentaufbau

Für die langen Formelpapiere wird der bewährte Pandoc-/XeLaTeX-Aufbau beibehalten, ergänzt durch vollständige Textextraktion und gerenderte PDF-Prüfung. `build_documents.py` verwendet die dokumentierte lokale Schrift-/TeX-Umgebung. Diese optionalen Layoutwerkzeuge sind keine Voraussetzung für den wissenschaftlichen Replay.

Hauptdokument, kurzes Update und einfache Erklärung haben dieselbe Version. Vorherige Fassungen werden nicht überschrieben. `documents_manifest.json`, `pdf_qa.json` und `visual_qa.json` gelten für die tatsächlich ausgelieferten PDF-Hashes; die PDF-Prüfung beweist korrekte Lieferung, nicht die physikalische Theorie.

## Unveränderte Grenzen

Keine ausgewählte globale CAR-Komposition aus dem Compiler; kein autonomer Controller; keine ursprüngliche Präparation der Modellversuche. Kein neuer Grundzustandsbeweis für die globalen Gegenmodelle. Keine abgeleitete Raumzeit, chirales Maß, dynamische Gravitation oder vollständige TOE. Kein RH-/Faktorisierungs-/P-vs-NP-Resultat. Keine vorhandenen physikalischen Abschlussmarker wurden promoviert, kein Commit/Push und keine Web-Veröffentlichung.
