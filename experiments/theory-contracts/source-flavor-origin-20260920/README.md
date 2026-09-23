# Quellenursprung: globale Ladung, Flavor und Komplement

20. September 2026 · **UR.SOURCE.FLAVOR_ORIGIN.01: PARTIAL**

Die neue Rechnung verbindet das ursprüngliche globale Standardmodell-
Ladungswörterbuch mit der vorgeschlagenen lokalen Randrekonstruktion. Sie
prüft anschließend die schon vorhandene E₈-Dreipunktfunktion als möglichen
Ursprung der fehlenden Down-/Leptonoperatoren.

**Die Rand-Wechselwirkung lässt sich mit einer unabhängigen Annahme weniger
auswählen.** Bei minimaler neutraler charakteristischer Nullrichtung und
festem orientiertem Klebewörterbuch bleiben zunächst 25 Richtungen. Wenn die
zusätzlichen Farb-/schwachen Singuletts echte Darstellungen der ursprünglichen
globalen Standardmodellgruppe sind, ist ihre Hyperladung ganzzahlig. Zusammen
bleibt genau die vorgeschlagene Richtung mit Hyperladung eins. Die zuvor
verlangte zusätzliche Block-Permutationssymmetrie wird nicht benötigt.

| Bedingung | Zahl der Kandidaten |
|---|---:|
| Minimal, neutral, charakteristisch, feste Orientierung | 84 |
| Vorgegebene Vierergraduierung | 56 |
| Vollständiges orientiertes D₈-/Spinorwörterbuch | 25 |
| Zusatzfelder stellen die globale Standardmodellgruppe dar | 1 |

Die Reihenfolge kann vertauscht werden: Globale Ladung nach der Graduierung
lässt 5 Kandidaten, erst die Orientierung wählt einen. Wird nur die
Lie-Algebra statt der globalen Gruppe verlangt, sind beispielsweise die
weiteren Kandidaten mit Hyperladung 1/6 zulässig. Die Herkunft der zusätzlichen
Kanäle, der Energie und der dynamischen Rekonstruktion bleibt offen.

**Die ursprüngliche Dreipunktfunktion besitzt die richtigen internen
Down-/Leptonplätze, aber noch nicht deren physische Massenstruktur.** Ihr
vollständiger Familientensor ist antisymmetrisch. Eine direkte Einsetzung
eines einzigen Higgs-Familienvektors ergibt eine 3×3-Matrix mit Singularwerten
`(||h||, ||h||, 0)`. Bei der naiven lokalen Ersetzung durch gemeinsame
vierdimensionale Weylfelder verschwindet sogar die Kopplung durch die
falsche Austauschsymmetrie. Der originale bosonische Current-Tensor bleibt
korrekt; seine direkte Lesart als Yukawaoperator ist damit ausgeschlossen.

**Das Komplement bekommt dadurch eine präzise Aufgabe.** Die ausgewählte
Hyperladung erlaubt im internen Wörterbuch eine Verbindung mit Leptonen;
eine direkte farbtragende Quark-Verbindung benötigt mehr als dieses
Singulettpaar und den vorhandenen farblosen Higgs. Das erlaubt verschiedene
Antworten, beweist aber noch keine tatsächliche Kopplung.

Für eine echte Verbindung zur fehlenden Familienrichtung müssen zwei
konkrete Quellenmatrixelemente ungleich null sein. Im bezeichneten
geordneten Massenslot ist die volle Determinante proportional zu

    -(h^T b)(c^T h).

Die reduzierte Determinante enthält zusätzlich 1/M. Die Phase der massiven
Masse M kürzt sich beim Wiederaufnehmen des Komplements exakt heraus. Gesucht
sind daher die wirklichen Übergänge b und c aus der Quelle und ihre relative
Phase. Ein beliebig komplex geschriebenes M ersetzt sie nicht.

Die Formel betrifft eine endliche chirale Massenmatrix, nicht schon den
vollständigen euklidischen Funktionaldeterminanten oder eine Anomalie.
Insbesondere ist das 1+1D-Randpaar noch kein identifiziertes 4D-Lepton.

[PROOF.txt](PROOF.txt) enthält Herleitungen, Originalstellen, Voraussetzungen
und Primärliteratur. `checker.py` prüft die exakten Auswahl-, Ladungs-,
Koeffizienten-, Rang- und Schuridentitäten; `source_manifest.json` friert die
verwendeten Quellen ein. Separate Prüfungen stehen in den beiden Review-
Dateien. Die aufwendigen vorgelagerten Current-Checker wurden nicht erneut
komplett ausgeführt. Keine Paper-/Ledger-Promotion, keine geschlossenen
physischen Gates und kein behaupteter vollständiger TFPT-Abschluss.
