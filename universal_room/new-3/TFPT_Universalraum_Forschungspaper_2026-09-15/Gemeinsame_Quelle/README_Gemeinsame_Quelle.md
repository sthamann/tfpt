# TFPT / Universalraum: gemeinsame Quelle — Fortsetzung 1.2

## Lesen
- `outputs/komposition/TFPT_Gemeinsame_Quelle_2026-09-15.pdf`: vollständige Herleitungen und Grenzen.
- Gleichnamiges Markdown: editierbarer Text.
- `outputs/komposition/Ergebnis_einfach_erklaert.md`: verständliche Zusammenfassung.
- Aussagen_und_Grenzen.json, Prüfprotokoll, Quellenmanifest und Forschungsergebnisse im selben Ordner.
- `reference/`: vorheriges Hauptpaper und Fortsetzung1.1 als PDF.

## Reproduzieren
Benötigt Python3 mit NumPy, SciPy und SymPy. In einer entpackten Arbeitskopie:

    python3 work/composition/run_all.py

Alle vier wissenschaftlichen Prüfer laufen normal und mit -OO. Erwartet werden 614 explizite Bedingungen und byteidentische Ergebnisse zu den mitgelieferten JSON-Dateien. Wissenschaftliche Eingaben werden zuerst per SHA-256 geprüft. Code- und Tensorarrays werden neu erzeugt; diese Dateien sind keine zu schützenden Originalquellen. Protokolle erscheinen unter work/composition/replay.

Die 614 Bedingungen umfassen wiederholte Moden- und Automorphismenprüfungen. Sie sind keine 614 unabhängigen Theoreme. Allgemeine Beweise über Recovery, Involutionen und den unendlichen N=2-Dynamikgrenzwert stehen im Paper; sie wurden nicht formalisiert.

## Abbildungen und PDF
Zusätzlich benötigt: Matplotlib, Pandoc/pypandoc-binary und XeLaTeX mit den im Header verwendeten Paketen einschließlich needspace. Für die PDF-Inspektion: PyMuPDF und Pillow.

    python3 work/composition/make_figures.py
    python3 work/composition/build_documents.py
    python3 work/composition/inspect_document.py

Die Bildkurven sind numerische Darstellungen. Der Wirkungspunkt tDelta=1 wird separat durch rationale Taylorrechnung mit vollständiger Restschranke zertifiziert. Die Spektralformel der Diagramme wurde gegen diesen unabhängigen Prüfwert abgeglichen.

## Geltungsbereich
Die globale Kompositionsregel ist eine zusätzliche Hypothese, keine abgeleitete TFPT-Quelle. Die Graphen und Quellphasen bleiben Eingaben. Der geschützte Faktor hat Dimension15 innerhalb eines 90-dimensionalen N=2-Unterraums. Es geht um eine einzelne logische Nachricht und einen einzelnen bekannten Modenverlust; native Encoder, Decoder und Hardware fehlen.

Der Wirkungstest setzt einen lokalen Phaseneingriff voraus. Derselbe Prüfer beweist, dass dieser aus dem bisherigen globalen Alphabet X,Nb nicht erzeugbar ist. Das hypothetische Programmregister macht relationale Adressierung konsistent, leitet aber weder das Register noch seine Kopplung ab. Ein dauerhaftes internes Record wurde nicht gebaut.

Der Größenbeweis betrifft die N=2-Dynamik auf einem vorgegebenen Netz mit beschränktem Grad. Ein voller Fock-Grundzustandsgrenzwert und eine Raumzeit-/TOE-Lösung bleiben offen. Der alte Grundzustandssatz der einzelnen Bank wird nicht auf das neue globale Modell übertragen. Der native Casimirsatz wird nur bei der ausdrücklich bezeichneten Vielteilchen-Untergrenze übernommen.

Dateien unter sources/ sind eingefrorene Belege. Die dortigen älteren Prüfer werden nicht vom neuen Runner ausgeführt und sind keine zusätzliche vollständige Wiederholung der alten Forschung.
