# TFPT / Universalraum — sechs Forschungsfortsetzungen
15. September 2026 · Fortsetzung 1.1

## Lesen
- `outputs/fortsetzung/TFPT_Universalraum_Sechs_Followups_2026-09-15.pdf`: vollständige Forschung, sechs Aufgaben und vier Quellenabgleiche.
- Gleichnamiges Markdown: bearbeitbare Quelle.
- `outputs/fortsetzung/Abgleich_Fundamentale_Reduktion.md`: kurze Antwort auf den jüngsten Nachtrag.
- `outputs/fortsetzung/Kodierung_15_Kanaele.csv`: alle 480 signierten Paarungen des optimalen Codes.
- Prüfprotokoll, Quellenmanifest und maschinenlesbare Forschungsergebnisse im selben Ordner.
- `reference/`: ursprüngliches 33-seitiges Forschungspaper und Markdown; Fortsetzung aktualisiert dessen §§5.5–5.6, 6.4 und 15.

## Rechnen
Benötigt: Python 3 mit NumPy, SciPy und SymPy; C++17-Compiler mit __int128 (Clang oder GCC). Aus dem entpackten Paket:

    python3 work/followups/run_all.py

In einer Arbeitskopie ausführen: Projektionsdaten und Codearrays werden neu erzeugt. Der Lauf prüft zuerst die eingefrorenen Eingaben, erzeugt die vier nativen Projektionsvektoren und führt die Kontraktion mit -O2 sowie -O0 aus. Danach laufen alle sieben Python-Prüfer normal und mit -OO. Die Rechnung bricht bei einer Abweichung ab. Erwartet: 537 explizite Bedingungen, identische wissenschaftliche JSON-Ergebnisse in allen Vergleichsläufen. Protokolle landen unter `work/followups/replay`.

Die kontrahierten Zustandskoeffizienten verwenden Ganzzahlen; die Auswertung prüft konservative Überlaufgrenzen. Dezimalzahlen in Diagrammen sind nur Darstellungen der exakten Matrizen und isolierten algebraischen Zahlen. Die 537 Bedingungen sind keine 537 unabhängigen Theoreme. Analytische Beweise im Text wurden nicht formalisiert.

Der C++-Lauf verarbeitet mehr als 100 Millionen Wege; er benötigt je nach Rechner etwas Zeit. `matrix_input.txt` und ausführbare Programme werden aus den mitgelieferten Quellen neu erzeugt und sind nicht Teil der Auslieferung.

## PDF und Abbildungen erzeugen
Zusätzlich: Matplotlib, pypandoc oder pypandoc-binary, Pandoc und XeLaTeX einschließlich deutscher Sprachunterstützung, unicode-math, fancyhdr, titlesec und fvextra. Für die Inspektion außerdem PyMuPDF und Pillow. Getestete Python-Paketversionen stehen in `work/followups/runtime_versions.json`.

    python3 work/followups/make_figures.py
    python3 work/followups/build_documents.py
    python3 work/followups/inspect_document.py

## Beweisgrenzen
- Der 15-dimensionale Code ist innerhalb des nativen hellen Paarcodes optimal für den Verlust einer einzelnen bekannten Fermionmode. Die 30-dimensionale Erweiterung schützt den logischen 15er-Faktor; ihr Zweierfaktor ist nicht zusätzlich geschützt.
- Physische Encoder, Decoder, Messgeräte, logische Steuerung und räumliche Herkunft sind nicht abgeleitet.
- Die volle zweite Singulettstufe und ihre gemischte Rückwirkung sind berechnet, nicht sämtliche höheren Stufen.
- Die komplexe Normalform gilt unter dem im Paper genannten Transformationsvertrag, nicht unter allen denkbaren Äquivalenzen.
- Große Grundzustands- und Polzertifikate wurden nicht erneut vollständig ausgeführt. Der alte Voll-Fock-Casimirsatz wird beim chemischen Potential als benannte Quelle vorausgesetzt.
- Vier Nutzernachträge werden geprüft; Haupttext U4 war bereits Quelle S003. Die große geladene Orbitkompression ist nicht berechnet.
- Keine vollständige Raumzeit-, RH-, Faktorisierungs-, P-vs-NP- oder TOE-Lösung. Kein T1–T8-Tor wird geschlossen gemeldet.
