# Gemischter Gewicht-1-Strom als Auswahlregel (14. Oktober 2026)

Status: **PARTIAL** – exakter Satz in der benannten Gitterklasse; keine
physikalische Gesamtlösung, keine Ledger-Promotion. Prüfung: `python3 checker.py`
(25 exakte Prüfungen, ca. 4 s).

## Einfach gesagt

Die Naht wird zweimal gelesen: als Wegeplan um d Marken (Zyklengitter
`A_{d-1}`) und als Register erlaubter Funktionen (Trägergitter `D_{d+1}`).
Bisher wurde d = 4 und E8 ausgewählt, indem man zusätzlich einen vollständigen
holomorphen (geraden unimodularen) Abschluss verlangte (`E8.ONEOBJECT.01`,
Satz 1–3 der Synthese).

Neu: Diese globale Forderung ist unnötig. Es reicht **eine einzige elementare
Operation vom Gewicht eins, die auf beide Lesarten gleichzeitig wirkt**. So eine
Operation gibt es nur bei vier Marken. Trägt sie zusätzlich Spinorladung, so
erzeugt sie allein E8; der unimodulare Abschluss folgt daraus.

Die Kopplung beider Lesarten ist wesentlich: Bei d = 7 gibt es einen reinen
Spinorstrom nur auf der Trägerseite (`D8 → E8`), die Markenseite `A6` bleibt
abgekoppelt. Dasselbe Muster (zerfallend) bei d = 8 und d = 9.

```
Naht ──► zwei Lesarten  A_{d-1}  ⊕  D_{d+1}
                 ▲             ▲
                 └── ein Strom J, Gewicht 1, Ladung auf BEIDEN Seiten
                         │
             existiert nur bei d = 4
                         │
      Vektortyp (Grad 2) ─► D8      Spinortyp (Grad 1/3) ─► E8 (unimodular folgt)
```

## Verbindung zum korrigierten Suchfehler

Unter der internen Z4-Gluegraduierung liegen die 240 E8-Ströme auf den Graden
0/1/2/3 als 52/64/60/64. Grad 0 sind die Ströme von `A3 ⊕ D5` selbst; die gibt es
für jedes d. **Die neutrale Auslese `E0` behält genau diese und entfernt alle
auswählenden Ströme.** Der auswählende Strom ist wie der Zeuge `X` aus `v993`:
einzeln unsichtbar (`E0(J)=0`), als Paar sichtbar. Die bereits bewiesene
mikroskopische Paarantwort `(1−e^{2πi(b−a)})^{-2}` ist genau dieser sichtbare
Schatten. Eine Suche, die nur die neutrale Auslese betrachtet, kann d = 4
prinzipiell nicht auswählen.

## Verbleibende minimale Bedingung und entscheidender Test

Die Ursprungsfrage reduziert sich in dieser Klasse auf:

> **Erzeugt die ursprüngliche mikroskopische Nahtoperation einen lokalen
> Gewicht-1-Strom ungeraden Gluegrads mit nichttrivialer Marken- und
> Spinorladung?**

Das ist ein Bit enger als Satz 3 der Synthese (keine Unimodularität mehr nötig)
und benennt die eine verbleibende Wahl ausdrücklich: Spinortyp (E8) vs.
Vektortyp (D8), d. h. ob die elementare Operation den vollen Z4-Grad oder nur
den Z2-Doppeldeckungsgrad trägt.

Entscheidender Test: Im deklarierten Acht-Kopien-QWZ-Modell den lokalisierten
Ein-Rand-Sektoroperator vom Gluegrad 1 konstruieren und prüfen, ob (a) seine
Paarantwort mit der bewiesenen Gewicht-1-Kernform übereinstimmt und (b) seine
Ladung unter den drei `A3`-Zyklenrichtungen nichttrivial ist. Fällt (b) weg,
liegt der zerfallende d = 7-Typ vor und die Auswahl trägt nicht.

## Abgrenzung

Nicht bewiesen: mikroskopische Herkunft des Stroms (`SEAM.SIMPLECURRENT.GENERATOR.01`,
`SEAM.MMST.TYPEIII.CHARGED.01` offen), die Vergleichsklasse selbst,
Identifikation der Gluegraduierung mit der Clock `u` aus `v993`, P1-Normierung,
Zustand, Zeit, 3+1D. Details: `PROOF.md`.

## Nachtrag (14. Oktober 2026, nach externer Prüfung)

Der oben vorgeschlagene Test (a)+(b) ist **unzureichend**: Ein neutraler Strom
kann dieselbe skalare Paarantwort haben, und das Acht-Kopien-Modell mit
eingesetzter 5+3-Aufteilung prüft bereits das gewählte d = 4-Ziel. Der bessere
Identifikationstest ist die Ladungsantwort gegenüber den acht Cartan-Strömen
(Befund `UR.SEAM.MIXED_CURRENT_ORIGIN.01`). Der Gittersatz M selbst bleibt
unverändert. Fortsetzung zur Kanalzahl: `../moebius-clock-fold-20261014`.
