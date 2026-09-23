# Halb-Ladung: einfacherer Träger, besserer Feldkandidat

9. September 2026. NON-RH-Forschung auf dem ursprünglichen QWZ-Zylinder.
**Ein neuer Operator-Kandidat und eine grundlegende Auswahlfrage; keine
vollständige lokale Feldkonstruktion und kein Abschluss von T1–T8.**

## Der konkrete Fortschritt

Der ursprüngliche Operator hatte zwei Aufgaben gleichzeitig: den
Ladungssektor wechseln und das räumliche Feldprofil tragen. Wir trennen
beides jetzt sauber. Die vorhandene Phasenrampe kennt bereits den
globalen Übertrag. Eine allein aus den vorhandenen Spektralprojektoren
berechnete polare Korrektur führt zusätzlich das gesamte gefüllte Meer
exakt mit. Dafür werden weder neue Zustände noch ein Hilfs-Ladungszähler
eingeführt. Der Hamiltonoperator bleibt unverändert.

Bildlich: Der Sektorwechsel ist der Transport zwischen zwei Stockwerken;
das lokale Feldprofil beschreibt, wo und wie man dort etwas ablegt. Der
neue Träger ordnet den Transport. Die vollständige lokale Ablage müssen
wir noch konstruieren.

Ein besonders nützlicher Punkt: Der Träger ist für alle Endpunkte gleich.
Deshalb bleiben die bisherigen **quellenseitigen neutralen Paare exakt
gleich**, einschließlich ihrer endlichen komplexen Phasen:

```
U'_a = W exp(i F_a),
(U'_a)* U'_b = U_a* U_b.
```

Wir können damit den geladenen Anteil verbessern, ohne die bisherigen
neutralen Paaroperatoren zu verändern. Die Aussage gilt nicht pauschal
für beliebige Operatorreihenfolgen oder unveränderte Zielzustände.

## Was die neue Ladungsprüfung ergibt

Gemessen wird das Quadrat der Norm des vollständigen Ladungsfehlers auf
dem gefüllten Meer — einschließlich Fluktuationen, nicht nur ein Mittelwert.

| Umfang N | Vorher: Fehlerquadrat vorwärts | Neuer Kandidat: vorwärts | Neuer Kandidat: adjungiert |
|---|---:|---:|---:|
| 16 | 7,11 × 10⁻³ | 6,92 × 10⁻⁶ | 1,64 × 10⁻⁵ |
| 32 | 2,75 × 10⁻³ | 2,52 × 10⁻⁷ | 6,90 × 10⁻⁷ |
| 64 | 1,19 × 10⁻³ | 2,37 × 10⁻¹⁰ | 6,01 × 10⁻¹⁰ |

Bei N=64 fällt außerdem die reskalierte Energie dieses Punktzustands von
3,945 auf 0,550. Das ist ein endlicher Vergleich: Die neue Punktenergie
steigt innerhalb der drei Größen von 0,329 auf 0,550. Ein beschränkter
Energiegrenzwert ist daraus **nicht** bewiesen.

Für den globalen Träger selbst gibt es mehr als diese Zahlen: eine exakte
Projektoralgebra, einen Existenznachweis für hinreichend große Umfänge und
Norm-/Energiekontrolle auf jedem festen endlichen Teilchen-Loch-Kern. Zwei
Vorwärtsschritte ergeben den tatsächlichen ganzzahligen Randübertrag;
der zweite Schritt darf nicht als Rückwärtsschritt oder als Zurücksetzen
auf das Vakuum behandelt werden. Die lokale Feldgrenze folgt daraus noch
nicht. [Herleitung und Grenzen](PROOF.md).

## Was der parallele Grundlagenstrang gefunden hat

Der bisherige Beweis arbeitet bei fester Breite mit dem exakt kritischen
Massenwert m=1. Das ist eine echte Voraussetzung. Bei der separat geprüften
Abwandlung m=1,5 sieht man zunächst noch fast eine halbe Ladung; bei
Umfang 4096 bleiben aber nur etwa 0,000017 übrig. Eine anfängliche
Zahlenübereinstimmung hätte hier den falschen Grenzwert nahegelegt.

Es gibt deshalb eine interessantere Alternative zur bloßen Feineinstellung:
Die Breite langsam, logarithmisch mit dem Umfang wachsen lassen. Dafür
sind die ersten spektralen Abschätzungen abgeleitet. Ob auch das komplette
gefüllte Meer und das lokale Feld diesen Grenzübergang tragen, bleibt offen.
Der ursprüngliche Beweis bei m=1 wird durch diese Gegenprobe nicht widerlegt.

Ein zweiter Grundlagenpunkt: Acht Querreihen sind nicht acht unabhängige
chirale Ströme. Die E8-Kanäle müssen aus der tatsächlich erzeugten
Stromalgebra folgen; das Einsetzen von acht Kopien wäre keine Herleitung.
[Parallele Grundlagenprüfung und konkrete Alternativen](FUNDAMENTAL_REVIEW.md).

## Nächste Abnahme und Einordnung

Als Nächstes muss der verbesserte Kandidat auf einem wachsenden Fenster
von Strommoden kontrolliert werden: vorwärts, adjungiert, mit Energie und
einer aus der Quelle abgeleiteten Normierung. Ziel ist ein nichtverschwindendes
raumzeitlich verschmiertes Feld mit nachgewiesener Lokalität. Daneben steht
die volle Prüfung des vorgeschlagenen Breiten-/Massen-Grenzübergangs.

56 Tests bestehen normal und unter Python `-OO`; die beiden vollständigen
neuen Messprotokolle sind bytegleich. Das belegt die ausgeführten Kontrollen,
nicht die offenen Grenzwertbehauptungen. [Testbericht](TEST_RESULTS.md),
[Messprotokoll](validation.json), [optimierter Kontrolllauf](validation_optimized.json).

Arbeitsbasis: `66b91e40e245569f06ab440ead80f446c9be0ee5`, einschließlich
der ausdrücklich gepinnten lokalen Vorarbeiten. Alle neuen Dateien dieses
Schritts liegen in diesem Ordner. Paper, Webseite, globale Beweisstände
und fremde Änderungen bleiben unberührt; kein Commit oder Push in diesem
Schritt. Der gemeinsame physikalische 3+1D-Ursprung und T1–T8 bleiben offen.
