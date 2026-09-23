# Halb-Ladung aus der tatsächlichen Randdichte

9. September 2026. Anschluss an
[source-half-sector-bridge](../source-half-sector-bridge/README.md) und
[half-loop-source-transport](../half-loop-source-transport/README.md).
Repo-Basis `66b91e40e245569f06ab440ead80f446c9be0ee5`.

**Neuer Fortschritt:** Die bisherige Halb-Ladungszuordnung lässt sich im
ursprünglichen fermionischen Streifen durch eine geometrisch definierte
Messgröße begründen. Vergleicht man seine beiden vorhandenen
Hintergrundsektoren mit derselben Referenz, erhält die obere Hälfte im
Grenzübergang +1/2 und die untere −1/2. Die zeitgemittelte Messung hat dort
verschwindende Streuung und wird auf den kontrollierten Randanregungen
erhalten. Noch nicht konstruiert ist das lokale Feld, das die beiden
Sektoren verbindet. T1–T8 bleiben offen.

## Das Bild dazu

Der Streifen besitzt einen oberen und einen unteren Rand. Wir zählen
zunächst die vorhandene Materie in seiner oberen Hälfte. Diese Messung
reagiert auch auf schnelle Anregungen des gefüllten Inneren. Eine bereits
im Projekt verwendete Zeitmittelung unterdrückt diese schnellen Beiträge,
ohne die langsamen Randanregungen zu entfernen.

Dann werden die beiden ursprünglichen Hintergrundsektoren verglichen.
Die gemeinsame Referenz ist die Dichte des ersten Grundzustands — nicht
eine nachträglich eingesetzte Zahl 1/2. Die Halb-Ladung entsteht aus dem
vollen Quellspektrum.

| Umfang N | Änderung oben, zweiter gegen ersten Quellgrundzustand |
| --- | ---: |
| 16 | 0.499990152881… |
| 32 | 0.499999999851… |
| 64 | 0.500000000000… |

Diese Zahlen sind numerische Kontrollen. Die Ableitung verwendet den
exakten Sprung des ursprünglichen Randzweigs und einen kontrollierten
Rest der vollständigen Spektralsumme. Sie erklärt den Grenzwert, statt
ihn aus der Zahlenfolge zu extrapolieren.

## Was jetzt gemeinsam nachgewiesen ist

- **Geometrischer Ursprung:** Der Operator beginnt als Dichte einer
  wirklichen Streifenhälfte, nicht als frei nummeriertes Energiespektrum.
- **Vollständige Quelle:** Alle 8N gefüllten und 8N ungefüllten Moden bleiben
  enthalten. Ein direkter vollständiger Zylinderlauf prüft die Zerlegung.
- **Halb-Ladung mit verschwindender Streuung:** Nicht nur der Erwartungswert
  stimmt; die zeitgemittelte Vakuumfluktuation geht gegen null.
- **Kontrollierte Dynamik:** Auf jedem festen endlichen Teilchen-/Lochkern
  konvergiert die Ladungswirkung einschließlich Energie-Graphnorm. Beide
  adjungierten Feldrichtungen sind berücksichtigt.
- **Unveränderte Gesamtladung:** Oben +1/2 und unten −1/2 ergänzen sich zu
  null. Die gesamte mikroskopische Ladung bleibt ganzzahlig.
- **Keine Feinabstimmung der Trennlinie:** Jede der sieben möglichen
  Trennlinien zwischen den vorhandenen acht Zeilen liefert denselben
  asymptotischen Halb-Unterschied.

Die Quellenparameter bleiben Breite 8, Masse 1, Hintergründe r=1,3 und
die vorhandene Filterbreite `4 N^(-3/4)`. Kein neuer Hamiltonian-Term,
keine acht hinzugefügten Kopien und kein zusätzlicher Ladungsspeicher.

## Präzise Verbesserung gegenüber den vorherigen Runden

Die ältere +1/2/−1/2-Zuordnung stützte sich auf Energiekompatibilität und
eine deklarierte Punktspaltungsreferenz. Jetzt gibt es eine eigenständige
Realisierung durch die vollständige endliche Quell-Dichte und einen
anschließenden Grenzübergang. Diese zwei Berechnungswege dürfen nicht
miteinander verwechselt werden: Ein vorheriges Abschneiden der gefüllten
Moden berechnet nicht dieselbe Größe.

Die erfolglose Ladungsnummer des kleinen Rotor-Quadrats ist damit nicht
repariert worden. Das Rotor-Modell und dieser fermionische Streifen sind
weiterhin verschiedene Quellen. Der neue Nachweis betrifft genau die
Quelle, aus der die bisherige Randfeld-Konstruktion stammt.

## Die verbleibende Brücke

Bildlich: **Wir können jetzt die beiden Ufer mit derselben Messlatte
vermessen. Das Schiff zwischen ihnen fehlt noch.**

Gesucht ist ein aus der Quelle gebautes V_N, das die beiden Hintergründe
verbindet und nach geeigneter Verschmierung ein nichtverschwindendes Feld
liefert. Es muss die neue Ladung um 1/2 verschieben, seine adjungierte
Gegenrichtung kontrollieren und beim zweiten Übertrag die richtige ganze
Randladung tragen. Der Vergleich zweier Grundzustände führt diesen
Transport noch nicht aus.

Auch eine exakte Ladungserhaltung auf dem gesamten endlichen Fockraum
wird nicht behauptet. Die entsprechenden globalen Kommutatornormen werden
als Gegenkontrolle ausgewiesen und gehen in den Stichproben nicht gegen
null. Der Satz betrifft den präzisierten niederenergetischen Kern.
Die Messung ist eine integrierte, zeitgemittelte Ladung, kein bereits
bewiesenes lokales E₈-Feld. Ein gemeinsamer TFPT-ausgewählter 3+1D-Ursprung
und die achtfach markierte E₈-/Clock-Zuordnung bleiben ebenfalls offen.

## Dateien und Reproduktion

- [PROOF.md](PROOF.md): Ableitung einschließlich vollständiger Vakuum- und
  Energieabschätzungen, Referenzwahl und Geltungsbereich.
- [TEST_RESULTS.md](TEST_RESULTS.md): ausgeführte Prüfungen und Gegenkontrollen.
- [NEXT_FIELD_TEST.md](NEXT_FIELD_TEST.md): nächster konkreter Feldtest mit
  der neuen Ladungsmessung; noch nicht ausgeführt.
- [validation.json](validation.json), [validation_optimized.json](validation_optimized.json): Replays.

Aus dem Repo-Root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/source-edge-charge-transport/run.py --output /tmp/tfpt-source-charge.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/source-edge-charge-transport -p test_checker.py -v
```

Die Forschungsrunde ergänzt ausschließlich diesen Ordner. Vorhandene
Quellen, Paper, Webseite und fremde Änderungen bleiben unverändert.
Kein Commit und kein Push. Die Resultate sind keine neue Entdeckung
fraktionaler Randantworten als allgemeines physikalisches Phänomen,
sondern eine konkrete zusätzliche Quellbrücke im TFPT-Programm.
