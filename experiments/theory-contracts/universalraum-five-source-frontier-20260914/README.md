# TFPT / Universalraum — geprüfte Forschungsrevision v1.4

14. September 2026. Vollständiges Hauptbuch plus kurzes Änderungs-Paper.
Keine Promotion zu abgeschlossener TOE, RH, Faktorisierung oder P-versus-NP-Lösung.

## Ergebnis und Lesereihenfolge

Die fünf neuesten Nutzertexte wurden vollständig gelesen, unverändert als N9–N13
archiviert und gegen Originalartefakte sowie unabhängige Rechnungen geprüft.
Vor Beginn des PDF-Updates wurden neue Forschungsresultate auf allen acht TFPT-
Fronten und zu den sechs eigenen nächsten Fragen ausgearbeitet.

1. [Einfach erklärte Follow-ups](FOLLOWUPS.md).
2. [Vollständiger neuer Forschungsbericht](RESULTS.md).
3. Hauptbuch in `main-v1.4/main.pdf`: ganze v1.3-Basis plus drei neue Kapitel,
   aktualisierte Querverweise und klar markierte historische Prüfprovenienz.
4. Kurzpaper in `main-v1.4/update.pdf`: ausschließlich die Änderungen gegenüber v1.3.
5. [Prüfzusammenfassung](replay.json) und [neuer Spektrallauf](spectrum_followup.json).

## Neue positive Resultate, jeweils im benannten Modell

- Kantenlokale vierte Ordnung als positive Summe lokaler Sternpolynome, mit
  exakter Operatoruntergrenze für den Sektorvergleich.
- Neue niedrige Eigenpaare von H2+H4 im vollständigen 24.024D-Singulettoperator;
  nicht bloß Rayleighkorrekturen auf alten Eigenvektoren.
- Äußere kantenlokale Vermittlerbandtrennung mindestens 0,7 Δ bei |t|/Δ ≤ 1/20.
- CAR/Tensor-Kreuzungsgauge in allen Ordnungen im ladungserhaltenden Matchingsektor.
- Vollständiger 13-Faktor-Zeitfilter auf dem 544D-Stern und Verbindung zu barem
  Zielzustand, resonantem Record und Mehrzeitprüfung mit unbedingten Erfolgsraten.
- Feedback-Fehlerboden und unabhängige Mehrzellen-Skalierung.
- Neue Vakuum-Ladungs-, Wärmekern-, chirale Fluss-, Flavour-, ACT- und Tensorproben.

Die lokale Architektur wird durch Lokalität allein nicht ausgewählt; die
Vierfachheit bleibt numerisch; Kontrolloperationen sind noch nicht vollständig
native Compileroperationen. Alle T1–T8-Tore bleiben offen. Einige gepinnte RH-/
Faktorquellen fehlen lokal; fehlende Prüfungen sind ausdrücklich nicht als Erfolg verbucht.

## Ausführen

Wissenschaftliche Tests benötigen Python mit numpy, scipy, sympy:

```sh
python3 replay.py
python3 spectrum_followup.py
```

`replay.py` führt die drei leichten Prüfer normal und mit `-OO` aus, verlangt
bytegleiche Ausgaben und prüft sieben absichtliche Fehler. Resultat: 8232 Bedingungen.
Der separate Spektrallauf ist erheblich schwerer, numerisch und nicht Teil des
leichten Replay-Zählers. Keine dieser Prüfungen ist ein vollständiger Lean-Beweis.

Dokumentbuild mit Python plus pypdf/Pillow, LuaLaTeX und Poppler:

```sh
python3 build_release.py
```

Der Build prüft alle Überschriften der v1.3-Kapitel, unveränderte Basisabbildungen,
Referenzen, problematische Überläufe und extrahierbaren Text; anschließend rendert
er jede Seite. Die zusätzliche visuelle Prüfung ist im Release-Manifest getrennt
markiert und wird durch einen neuen Build zunächst wieder auf ausstehend gesetzt.

## Quellen und Grenzen

`sources/N*.md`: alle fünf Originaleingaben, bytegetreu mit SHA-256 in `replay.json`.
`sources/evidence/validation_sectors_f4.json`: unveränderte Original-Sektortabelle
für den Abdeckungsaudit; ihr Vorhandensein ist kein erneuter Lauf des Fremdprüfers.
`baseline-v1.3`: Kapitel und Abbildungen der vollständigen vorherigen Buchfassung.
`release_manifest.json`: PDFs, Version, Abdeckung, neue Prüfungen und Evidenzgrenzen.

Die v1.4-Verifikation importiert keinen fremden TFPT-Forschungsprüfer. Sie baut ihre
kleinen mathematischen Objekte selbst. Die 64-Sektor-Quelltabelle wird nur gelesen.
Die Bibliotheken und allgemeinen externen Methoden bleiben Abhängigkeiten.

Ältere Versionen werden nicht überschrieben. Keine Änderungen an Theorie-Ledgern,
verbindlichen T1–T8-Abschlussmarkern, Website oder Git-Historie sind Teil dieser Revision.
