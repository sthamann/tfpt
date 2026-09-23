# Gemeinsamer Prozess, v1.6.8

Forschung und unabhängiger Audit vom 15. September 2026. Haupttext: RESULTS.md.
Teilberichte stehen in agents/mechanism, agents/shadows und agents/causal.
Die kausale Dreizustands-Zusammenführung steht zusätzlich in ADDENDUM_COMMON3.md.

## Reproduktion

Mit Python 3.10 oder neuer, NumPy, SciPy und SymPy:

```sh
python3 -B replay.py
```

Der Replay verwendet ausschließlich eingefrorene Eingaben aus diesem Paket.
Er führt alle eigenen Prüfer normal und mit -OO, Warnungen als Fehler, aus
und verlangt identische Ergebnisbytes. Zusätzlich wird das gelieferte
Synthesepaket isoliert entpackt und seine beiden ausgewählten Prüfer
wiederholt. Die eigenen Prüfer sind gelesen und erhalten explizite Fehlerbedingungen.
Die Archivpfade werden vor dem Entpacken validiert.

Die Ergebniszahlen messen Prüfbedingungen, nicht unabhängige physikalische
Entdeckungen. Viele Bedingungen betreffen einzelne Einträge oder Generatoren.
Der große historische Grundzustandsbeweis und die frühere gesamte
822er-Suite werden hier nicht erneut ausgeführt.

## Dokumente

Die Vollfassung bewahrt die ganze frühere v1.6.7 und enthält davor den
aktuellen Forschungsbericht, alle drei Teilberichte sowie das Dreizustands-
Addendum. Kurzupdate und einfache Erklärung werden getrennt geliefert.
Die später nachgereichten Texte sind in LATE_UPDATES.md und drei
ausführlichen Nachtragsprüfungen integriert. Ihre neue fünfte Norm,
Ritzmomente und Lorentz-Projektorprüfung sind ebenfalls im Replay enthalten;
faktische Quellenpins, numerische Vergleiche und erhaltene Quellguards
werden ausdrücklich unterschieden.
Die mitgelieferte Forschungssynthese bleibt unverändert eingefroren;
ihre Korrektur zu Gamma(1,w) steht im neuen Haupttext.

PDF-Erstellung benutzt den bestehenden Formel-Satz mit Pandoc/XeLaTeX;
PDF-Prüfung benötigt die separat bereitgestellten PDF-Bibliotheken.
Die wissenschaftliche Reproduktion benötigt weder PDF-Tools noch Netzwerk.

## Grenzen

Exakte Sätze betreffen die angegebenen endlichen Modelle. Ursprüngliche
Präparationen, gezielte Modenphasen, Messinstrumente, N=64-Poltransport,
relativistischer Grenzwert und alle vollständigen T1–T8-Tore bleiben offen.
Keine Veröffentlichung, kein Commit oder Push und keine Änderung der
ursprünglichen Nutzerdateien ist Bestandteil dieser Lieferung.
