# Primzahlereignisse aus π-Ziffern vorhersagen

Stand: 8. September 2026. Ausgeführte Fortsetzung nach dem Fourier-Kostenvergleich.

**Befund:** In den beiden vorher festgelegten Modellen verbessern π-Ziffern die Vorhersage der nächsten Primzahllücke auf dem getrennten Prüfbereich nicht. Die Effekte liegen im Bereich der vollständigen Zufallsstrom-Kontrollen. Ein starkes absichtlich eingebautes Signal wird mit derselben Auswertung erkannt.

## Neue Daten und konkrete Vorhersagefrage

Es wurden je **10.400.000 Nachkommastellen von π, e und √2** berechnet. Gelernt wird auf 13,729 Primzahlpositionen zwischen 2.000.001 und 2.200.000; geprüft auf 12,894 Positionen zwischen 5.000.001 und 5.200.000. Die tatsächlichen äußersten Primzahlen sind [2000003, 2199979] bzw. [5000011, 5199983]. Alle gelesenen Stellen liegen jenseits des alten Zweimillionen-Präfixes. Auch die langen Blöcke aus Lern- und Prüfbereich überschneiden sich nicht.

Für jede Primzahl p ist der Zielwert log((nächste Primzahl−p)/log(p)). Damit wird die Größe der folgenden Lücke relativ zur lokalen logarithmischen Skala untersucht. Dies ist ein Test der statistischen Vorhersage außerhalb des Lernbereichs; Primzahlen und Lücken sind deterministisch berechenbar, und der Test ist kein schnellerer Primzahlgenerator.

Die arithmetische Vergleichsvorhersage nutzt log(p), vier bereits bekannte vorherige Lücken und Restklassen von p modulo 30, 7, 11, 13, 17 und 19. Eine feste Ridge-Regression mit Strafparameter 100 wird ausschließlich auf dem Lernbereich angepasst. Zu ihrer Vorhersage wird jeweils eine getrennt gelernte Ziffernkorrektur addiert. Es gibt keine nachträgliche Modellauswahl.

- **Kurz:** die 32 Ziffern ab Position p und deren zehn Ziffernhäufigkeiten, insgesamt 42 Merkmale.
- **Kurz + lang:** dieselben Merkmale, ergänzt um normalisierte Ziffernsumme, Quadratsumme und Summen beider Hälften des Blocks mit genau p Ziffern ab Position p, insgesamt 46 Merkmale.

Alle Skalierungen und Modellkoeffizienten stammen ausschließlich aus dem Lernbereich. Die folgende Primzahllücke kommt ausschließlich als Lernziel bzw. nachträglicher Prüfwert vor.

## Gemessene Vorhersageleistung

Positive Werte bedeuten weniger mittleren quadratischen Fehler als die arithmetische Vergleichsvorhersage. Negative Werte bedeuten eine Verschlechterung. Der Fehler bezieht sich auf den logarithmischen Zielwert, nicht auf den Anteil exakt vorhergesagter Primzahlen.

| Ziffernquelle | Merkmale | Fehlerreduktion Lernen | Fehlerreduktion Prüfung | Erste Prüfhälfte | Zweite Prüfhälfte |
|---|---|---:|---:|---:|---:|
| π | 32 Ziffern + Häufigkeiten | +0.350 % | -0.226 % | -0.253 % | -0.200 % |
| π | Zusätzlich Blöcke der Länge p | +0.351 % | -0.459 % | -0.482 % | -0.436 % |
| e | 32 Ziffern + Häufigkeiten | +0.299 % | -0.304 % | -0.329 % | -0.280 % |
| e | Zusätzlich Blöcke der Länge p | +0.309 % | -5.363 % | -5.443 % | -5.284 % |
| √2 | 32 Ziffern + Häufigkeiten | +0.247 % | -0.077 % | -0.019 % | -0.133 % |
| √2 | Zusätzlich Blöcke der Länge p | +0.251 % | -0.179 % | -0.178 % | -0.179 % |
| Absichtlich eingebautes Signal | 32 Ziffern + Häufigkeiten | +64.893 % | +64.117 % | +63.928 % | +64.303 % |
| Absichtlich eingebautes Signal | Zusätzlich Blöcke der Länge p | +65.188 % | +29.255 % | +18.766 % | +39.533 % |

Die arithmetische Vergleichsvorhersage selbst senkt den Prüf-MSE gegenüber dem konstanten Lernmittel um 4.18 % (0.735356 → 0.704626). Der Zusatzvergleich findet also gegen eine tatsächlich nützliche, aber begrenzte arithmetische Vorhersage statt.

Die kleinen Lernverbesserungen von π übertragen sich auf keine der beiden Prüfhälften. Bei den langen Merkmalen kann die Verschlechterung deutlich größer ausfallen, etwa für e. Das passt zur starken Abhängigkeit und langsamen Veränderung benachbarter Millionen-Ziffern-Blöcke: Ein solcher Zusatz kann im Lernfenster günstig aussehen und in einem entfernten Bereich schlecht extrapolieren. Diese Erklärung ist eine Einordnung des festen Modells, keine Behauptung über eine besondere Eigenschaft von e.

## Kalibrierung mit vollständigen Zufallsströmen

999 voneinander unabhängig erzeugte, gleichverteilte Dezimalströme durchlaufen jeweils die gesamte Auslese, Skalierung, Modellanpassung und Prüfung. Innerhalb eines Stroms bleiben alle tatsächlichen Überlappungen erhalten. Einzelne Primzahlzeilen oder Millionen-Ziffern-Blöcke wurden nicht als unabhängig resampelt.

| π-Merkmale | Unkorrigierter p-Wert | Holm über beide Tests | Mittlere 95 % der Null-Fehlerreduktionen | Kandidatenkriterium |
|---|---:|---:|---:|---|
| 32 Ziffern + Häufigkeiten | 0.358 | 0.716 | -0.515 bis -0.069 % | nicht erfüllt |
| Zusätzlich Blöcke der Länge p | 0.546 | 0.716 | -6.660 bis +0.732 % | nicht erfüllt |

Vorab verlangt waren mindestens 1 % Fehlerreduktion im Prüfbereich, korrigiertes p<0,05 und eine Verbesserung in beiden Prüfhälften. Keine π-Variante erfüllt diese Bedingungen. Die angegebenen Nullbereiche sind Verteilungen simulierter Vergleichsergebnisse; sie sind keine Konfidenzintervalle für einen unbekannten universellen π-Effekt.

Die Positivkontrolle schreibt an den Primzahlpositionen gezielt eine 9 oder 0, je nachdem ob die folgende Lücke oberhalb oder unterhalb eines im Lernbereich bestimmten Schwellenwerts liegt. Hier ist die Zielinformation absichtlich enthalten. Beide Modelle erkennen sie mit korrigiertem p=0,002 und Verbesserungen in beiden Prüfhälften. Das zeigt die Erkennbarkeit dieses starken eingebauten Signals; eine Leistungsgarantie für beliebig schwache oder nichtlineare Korrelationen folgt daraus nicht.

## Warum Normalität die ursprüngliche Frage nicht erledigt

**Auch eine normale Zahl kann an sämtlichen Primzahlpositionen vorgeschriebene Ziffern tragen.** Primzahlpositionen haben asymptotische Dichte null. Ändert man dort die Ziffern einer normalen Zahl, bleiben ihre Grenzhäufigkeiten endlicher Ziffernblöcke erhalten. Zur Erhaltung von Normalität unter dünn verteilten Änderungen siehe [Aistleitner, On modifying normal numbers](https://www.math.tugraz.at/~aistleitner/Publications/Modified_normal_numbers_revised_2.pdf).

Der direkte Zählgrund: Für eine feste Blocklänge k berührt eine geänderte Ziffer höchstens k Blockanfänge. Bis zur Stelle M ändern sich deshalb höchstens k·P(M) Blockvorkommen, wobei P(M) die Anzahl der Primzahlen bis M ist. Wegen P(M)/M→0 verschwinden die Änderungen in der relativen Häufigkeit.

Damit könnte eine eigens konstruierte normale Zahl an Primzahlpositionen sogar ein vorgegebenes binäres Ereignislog kodieren. Das ist ein bekanntes mathematisches Prinzip, kein neuer Satz über π. Selbst bewiesene Normalität von π würde solche speziellen Korrelationen nicht allein ausschließen; entscheidend bleibt eine direkte Untersuchung der ausgewählten Positionen.

## Prüfung und Grenzen

- 104 Rand-/Stichprobenpositionen unabhängig mit SymPy auf Primzahligkeit, nächste Primzahl und vier vorherige Lücken geprüft.
- 12 vollständige lange Ziffernblöcke unabhängig durch direkte Python-Ganzzahlsummen gegen die Präfixsummen-Auslese geprüft.
- 32 Vorhersagemetriken aus den gespeicherten Einzelvorhersagen erneut berechnet; Monte-Carlo-Ränge und Holm-Korrektur ebenfalls nachgerechnet.
- Fünf Testgruppen prüfen Auslesegrenzen, Ziffernmomente, Ridge-Lösung gegen ein unabhängiges erweitertes Least-Squares-System, Unabhängigkeit der Vorhersage von Prüfzielwerten und Korrekturauflösung.
- π mit höherer Rechengenauigkeit vollständig wiederholt; alle drei alten Zweimillionen-Präfixe stimmen mit den zuvor hashgeprüften Daten überein. Für die neuen Suffixe ist die Präzisionswiederholung keine unabhängige Berechnungsmethode.
- Alle Code-, Daten- und Protokollhashes stimmen. Modell und Protokoll wurden nach den Ergebnissen nicht verändert.
- Begrenzte Aussage: zwei feste lineare Merkmalsmodelle, ein Lernbereich und ein entfernter Prüfbereich. Kein Nachweis allgemeiner Unabhängigkeit, kein Normalitätsbeweis, keine RH-Folgerung und keine Faktorisierungsbeschleunigung.

Die verbleibende Forschungsfrage betrifft ausdrücklich andere, vorab begründete Mechanismen, etwa eine nichtlineare Beziehung mit unabhängiger Replikation. Beliebiges weiteres Durchprobieren von Fenstern, Merkmalskombinationen und Zielgrößen würde eine neue, vollständig mitzukalibrierende Suchfamilie erzeugen.

## Rechenkosten und Reproduktion

Datenerzeugung: π 8.399 s, e 4.264 s, √2 1.170 s; π-Präzisionswiederholung 9.359 s. Modell- und Kontrolllauf insgesamt 62.946 s, davon 62.573 s für die 999 Nullströme und abschließende Kalibrierung. Diese Messungen schließen den separaten Audit nicht ein. Umgebung: Python 3.14.3, NumPy 2.4.2, gmpy2 2.3.1, macOS-26.4.1-arm64-arm-64bit-Mach-O.

```sh
cd experiments/pi-prime-event-log-2026-09-08/prediction-gate
PYTHONPATH=/tmp/tfpt-pi-event-deps python3 prepare_data.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -m unittest -v test_prediction.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 predict.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit.py
python3 write_report.py
```

gmpy2 liegt in dieser Sitzung unter `/tmp/tfpt-pi-event-deps`; alternativ in der eigenen Umgebung installieren und PYTHONPATH entsprechend anpassen. Vorhandene geprüfte Zifferndateien erlauben das Überspringen der Datenerzeugung. Erneute Läufe überschreiben die Ergebnisdateien dieses Unterordners.

Artefakte: [Protokoll](PROTOCOL.md), [Zusammenfassung](summary.json), [Audit](audit.json), [Datenmanifest](data_manifest.json), [Einzelvorhersagen](predictions.npz), [999 Null-Läufe](null_runs.jsonl), [Auslesebeispiele](examples.csv). Die drei vollständigen Zifferndateien liegen ebenfalls im Unterordner.
