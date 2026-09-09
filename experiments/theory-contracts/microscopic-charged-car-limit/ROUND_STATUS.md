# T1--T8: erster direkter geladener CAR-Feldvergleich auf der mikroskopischen Quelle

2026-09-09, lokaler Forschungsstand bei HEAD `b803b7e5`.
Keine Änderung ursprünglicher Quellen, des Hamiltonoperators, Papers, Webseite,
Proof-Ledgers oder T1--T8-Status. Kein Commit oder Push dieser Runde.

## Ergebnis

Der [Beweis](README.md) konstruiert aus der unveränderten QWZ-Quelle ein
ganzzahlig geladenes chirales CAR-Randfeld samt tatsächlichem Adjungierten,
gefülltem Vakuum, mikroskopischem Ortszugriff und kontrollierter Zeitentwicklung.
Das ist ein anderer, direkter Feldtyp als die bisher untersuchten neutralen
Dichte-Exponentialwörter. Es ist noch nicht TFPTs E8-Halbladungsoperator lambda.

Der Operator ist zunächst besonders einfach: ein ursprünglicher Fermionoperator,
mit glatter Testfunktion auf der obersten Randreihe verschmiert. Seine Ladung
folgt exakt aus dem vorhandenen Fermionzahloperator. Die bereits konstruierte
Polarisierungsisometrie ordnet ihn der wirklichen gefüllten Quelle zu.
Verwendet wird dieselbe komplexe, teilchenzahlerhaltende Fock-Darstellung wie
bei den neutralen Slater-Determinanten. Die 16N komplexen Einteilchenkoordinaten
dieses Quellenvergleichs sind nicht die sechzehn reellen Compiler-Majoranas.

Für jeden festen Fourier-Modenbereich ergibt der schriftliche Beweis:

| Größe | Kontrolle bei N gegen unendlich |
|---|---|
| Falsche Vakuumbesetzung des rohen Randfelds | O(N^-4) |
| Normabstand zur exakt polarisierten Mode | O(N^-2) |
| Skalierter Generatorrest des exakt lokalen Randfelds | O(N^-1) |
| Skalierter Generatorrest der polarisierten Mode | O(N^-2) |
| Feld und Adjungiertes auf endlichem Energie-Kern | Konvergenz mit derselben Quellenisometrie |
| Endliche Produkte einschließlich endlicher Zeiten | Voller komplexer Vakuum- und Kernvergleich |

Für beliebige glatte Testfunktionen werden Fourier-Tails und Sampling-Aliase
explizit mitgeführt; die festen-Moden-Raten werden nicht pauschal auf jede
wachsende Fourier-Summe übertragen. Die lokalen Vertreter haben exakt den
angegebenen Ortsstützbereich. Die unbeschränkten Grenzgeneratoren besitzen
einen gemeinsamen dichten endlichen Energie-Kern und beschränkte Kommutatoren
mit den glatt verschmierten Feldern.

Die Vielteilchenkontrolle verwendet ausschließlich Teilchen-/Lochanregungen
über dem echten Vakuum. Daher multipliziert sich der Fehler mit ihrer Zahl,
nicht mit der extensiven Zahl 8N besetzter Quellmoden. Die Bulk- und Bottom-
Moden werden weder gelöscht noch neu präpariert.

## Ladungsleiter statt Zusatzregister

Für jede ganze Ladung q entstehen Zustände aus ursprünglichen Teilchen- und
Lochoperatoren. Im Grenzraum des oberen Randfelds haben die ladungsminimalen
Zustände die Energie

```
E_top(q)=q²/2-q/4.
```

Der lineare Term folgt aus der wirklichen r=1-Holonomie. Er wird nicht zum
Abgleich mit dem abstrakten E8-Ziel H0=|q|²/2 entfernt. Die Minimalität gilt
im oberen Randsektor, nicht für alle Ladungszustände des vollständigen
Zylinders. Dessen entgegengesetzter Rand bleibt vorhanden.

## Einordnung in die tatsächlichen acht Pflichten

Die Zielbeschreibungen stammen aus `toe-bridge-round30/README.md`; keine
Pflicht wird durch eine kleinere umdefiniert.

| Gate | Beitrag dieser Runde | Weiterhin fehlend |
|---|---|---|
| T1: Ursprungs-/Strukturselektion | Keine neue Auswahlbehauptung. | P1/P2, Dimension, Compiler- und Parameterwahl aus Grundprinzipien. |
| T2: mikroskopische geladene Algebra und (E8)_1 | Direkter Ein-Kanal-CAR-Feld-/Vakuum-/Domain-Vergleich, einschließlich echter ganzzahliger Ladungen. | Achtkanal-Auswahl, Halbladungsintertwiner, lambda, E8-Kozyklus, gemeinsame Familien-/Deck-Markierungen. |
| T3: gemeinsamer ausgewählter 3+1D-Parent | Belastbarer Randbaustein, kein neuer Parent. | Physikalische Abbildung zwischen Compiler, Randfeldern und derselben Bulk-Dynamik. |
| T4: chirales SM und Spiegelkontrolle | Chirale Bewegung auf einem Rand des vorhandenen freien Regulators. | Kein chirales 3+1D-SM, keine Weyl-Maßkonstruktion oder Spiegelentkopplung. |
| T5: wechselwirkender 3+1D-Grenzwert | Kontrollierter freier Randfeld-Limes. | Lorentz-Restauration, Einschluss, Clustering und nichttriviale Streuung im gemeinsamen 3+1D-Parent. |
| T6: Eichkopplungen und Neutrinotextur | Kein neuer Fixpunkt oder Massenparameter. | Interne quantitative Parameter-/Flavor-Ableitung. |
| T7: universell gekoppelter quantisierter Spin 2 | Kein Gravitonresultat. | Emergenz, zwei Helizitäten und universelle Kopplung aus demselben Parent. |
| T8: ausgewählter Anfangszustand und gemeinsame Quellen | Geladene und neutrale Untersuchungen verwenden dieselbe vorhandene QWZ-Spektralpräparation. | Eindeutig abgeleiteter physischer Anfangszustand; kein kosmologischer Zustand gewählt. |

## Warum der Compiler-Readout nicht einfach angehängt wird

Der vorausgehende Audit des Zwölf-Majorana-Readouts bleibt gültig: Bild(B)
liefert eine endliche Kopplungsauswahl, aber keinen nichtgaußschen
Wechselwirkungsgenerator und keine mikroskopische QWZ-/Rotor-Identifikation.
Auch die reduzierte Clock hat auf sechs komplexen Moden die Vielfachheiten
3,1,1,1; sie passt nicht durch einen Basiswechsel auf drei lokale L/H-Paare
der bereits klassifizierten ortsfesten Phasenklasse. Diese Tatsachen werden
nicht durch das hier konstruierte Randfeld aufgehoben.

Der Fortschritt ist stattdessen eine wirklich aus der Quelle konstruierte
geladene Vergleichsalgebra. Die nächste T2-Rechnung muss den Halbladungs-
Sektor als Intertwiner zwischen Darstellungen **dieser** Algebra liefern,
mit tatsächlichem Ladungsübertrag, normiertem Kozyklus und Energie-/Stützbereichs-
kontrolle. Ein unrenormierter scharfer Halbtwist reicht wegen der bekannten
divergenten gekreuzten Hilbert--Schmidt-Summe weiterhin nicht aus.

## Evidenz und Grenzen

Die expliziten Formeln und der schriftliche Vielteilchenbeweis stehen in
[README.md](README.md), die vollen Quellenkontrollen in
[diagnostics.json](diagnostics.json). Testtranskripte und Datei-Hashes werden
von [run_verification.py](run_verification.py) in
[verification.json](verification.json) gespeichert.
Frisch ausgeführt: **131 Tests normal und 131 mit Python -OO bestanden**, davon
19 neue und 112 unveränderte Regressionstests je Modus. Siehe
[TEST_RESULTS.md](TEST_RESULTS.md) für die vollständige Aufschlüsselung.
Es gibt in dieser Runde keine unabhängige mathematische Gegenbegutachtung
und keinen Beweisassistenten-Nachweis. Numerische Tests stützen die
Implementierung; die Grenzaussagen beruhen auf den angegebenen Argumenten.
