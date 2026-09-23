# Fünf weitere Singuletttypen exakt ausgeschlossen

14. September 2026. Anschluss an `spectral/RESULTS.md`, ausschließlich das
kantenlokale trunkierte Modell Htr=H0+F4/800, epsilon=1/20. Der vorhandene
348D-Beweis bleibt unverändert. Dieser Anschluss kontrolliert jetzt den
**gesamten 1764-dimensionalen Singulettsektor mit trivialem
Translationscharakter**.

## Bewiesenes Ergebnis

| S5-Typ | Multiplizitätsblock | Irrepdimension | Ganze kontrollierte Dimension | Rigorose Untergrenze H0/J | Rigorose Untergrenze Htr/J |
|---|---:|---:|---:|---:|---:|
| (3,2) | 86 | 5 | 430 | 12,69021549 | 13,4888025606 |
| (3,1,1) | 80 | 6 | 480 | 13,21496698 | 13,9820689612 |
| (2,2,1) | 66 | 5 | 330 | 14,05933886 | 14,7757785284 |
| (2,1,1,1) | 42 | 4 | 168 | 14,90966915 | 15,575089001 |
| (1,1,1,1,1) | 8 | 1 | 8 | 16,96304246 | 17,5052599124 |

Alle Ungleichungen sind streng. Die Tabelle verwendet die abschließend für
alle fünf Blöcke vollständig rekonstruierten Polynome und exakten
Wurzelzählungen. Eine unabhängige Spurmoment-Route liefert bereits aus
weniger Primzahlen gröbere, ebenfalls hinreichende Schranken.
Diese **1416 zusätzlichen Dimensionen**
liegen vollständig oberhalb 12,45 J. Zusammen mit den bereits bewiesenen
trivialen und Standardblöcken mit 28+320=348 Dimensionen ergibt das 1764.

Damit liegen im ganzen Nullimpulssektor **genau fünf Eigenwerte unter
12,45 J**: zuerst ein einfaches Niveau, danach ein exakt vierfaches Niveau.
Der Abstand der beiden Niveaus ist größer als 0,486414126928008 J. Die aus dem
vorherigen Zertifikat übernommenen Energieintervalle lauten

\[
11.960507412<E_0/J<11.960507414,
\]

\[
12.446921540928008\le E_1/J\le12.447023843543178.
\]

Das kontrolliert noch **nicht** den ganzen 24024D-Singulettsektor: Die fünf
Typen des Translationscharakterorbits mit Gewicht 1 und die sechs Typen mit
Gewicht 2 fehlen weiterhin, zusammen **11 Typen und 22260 Dimensionen**.
Nichtsinguletts und Mikrorest bleiben ebenfalls offen.

## Exakte primitive Projektoren statt großer isotypischer Räume

Für jedes der fünf Youngdiagramme wird ein festes Tableau mit zeilenweiser
Nummerierung konstruiert. Sei R seine Zeilengruppe, C seine Spaltengruppe und
h das Produkt der Hakenlängen. In der Gruppenalgebra von S5 ist

\[
e_\lambda=\frac1h\left(\sum_{c\in C}\operatorname{sgn}(c)c\right)
                   \left(\sum_{r\in R}r\right)
\]

ein primitives Idempotent. Es wird mit dem Translationsmittel PT kombiniert.
Sein Bild enthält genau eine Richtung pro Irrep-Kopie, also genau den
gewünschten Multiplizitätsblock. Es ist im Allgemeinen kein orthogonaler
Projektor; das ist für den invarianten Spektralblock nicht erforderlich.
Der eigentliche Operator X bleibt bezüglich des induzierten positiven
inneren Produkts selbstadjungiert.

Die Reihen-/Spaltenmittel werden über exakte Kosetfaktorisierungen erzeugt.
`projector_identities.py` prüft außerdem e²=e vollständig in der ganzzahligen
S5-Gruppenalgebra, die Spur 1 auf der gewünschten S5-Irrep und Spur 0 auf
allen anderen Irreps. Eine neue vollständige Specht-Charakterrechnung ergibt
die Ränge 86/80/66/42/8 unabhängig neu und bestätigt die v1.5-Mackey-Tabelle.
Zusätzlich zertifizieren modulare
Pivots den Rang der tatsächlich konstruierten Basis B. An sämtlichen
24024×m Einträgen werden geprüft:

\[
e_\lambda B=B,\quad T_a B=B\ \text{für die vier Translationserzeuger},
\quad XB=B X_{\lambda}.
\]

Damit wurde kein 5240D- oder anderer großer zentraler Projektor als kleiner
Block ausgegeben. Die Matrizen sind tatsächlich 86, 80, 66, 42 und 8 groß.
`modular_*.json` speichert die vollständigen reduzierten X-Matrizen.

## Globale Blockuntergrenzen durch ein gerades Spurmoment

Für jeden selbstadjungierten Block gilt für **jeden** Eigenwert x:

\[
|x|^{32}\le M_\lambda=\operatorname{tr}X_\lambda^{32}.
\]

Der Wert M ist eine ganze Zahl: X ist ein ganzzahliger Gruppenalgebraoperator
auf einem rationalen invarianten Raum und erhält dessen Schnittgitter mit
einem ganzzahligen Spechtgitter. Die bereits bewiesene Singulett-Sternschranke
gibt ||X||<=24. Für einen m-dimensionalen Block gilt deshalb die vorab
festgelegte Schranke

\[
0\le M_\lambda\le m24^{32}.
\]

Der Prüfer berechnet X^32 durch fünf exakte modulare Quadrierungen und
rekonstruiert M aus **sechs Primzahlen** nahe 10^8. Das Produkt ist größer
als zweimal die jeweilige Ganzzahlschranke. Eine **siebte unbenutzte
Primzahl** bestätigt M unabhängig.

Ein rationaler Radius r wird anschließend durch den rein ganzzahligen
Vergleich r^32>M zertifiziert. Damit X>-rI und H0>20-r/2. Die schon vorher
bewiesenen affinen Operatoruntergrenzen für Htr liefern aus den Spurmomenten
bereits 13,23026168 / 13,84235819 / 14,61685474 / 15,42623657 / 17,44274901.
Die Tabelle oben zeigt die stärkeren abschließenden Polynomgrenzen.
Beide Geraden dürfen für diesen skalaren Schluss einzeln angewandt werden;
es wird kein punktweises nichtkommutatives Operatormaximum gebildet.

Dieses Verfahren kontrolliert sämtliche Eigenwerte des reduzierten Blocks.
Die numerischen Minima aus `floating.json` dienen als Vergleich, nicht als
Zählbeweis. Eine absichtlich eingefügte versteckte Mode x=-20 verletzt die
Spurschranke, obwohl beliebige andere exakt bekannte Ritzvektoren weiterhin
Residual null besitzen können. Dies ist als Negativkontrolle enthalten.

Weitere Negativkontrollen verändern einen reduzierten X-Matrixeintrag, einen
Polynomkoeffizienten und einen rekonstruierten Spurwert; die jeweiligen
exakten Identitäten bzw. die unabhängige Primzahl weisen sie zurück.

## Zusätzlich vollständig rekonstruierte Polynome

Alle fünf Blöcke wurden außerdem mit vollständigen ganzzahligen
charakteristischen Polynomen zertifiziert:

| Typ | Rigoroses Intervall des nackten Minimums H0/J | Daraus Htr/J größer als |
|---|---|---:|
| (3,2), 86D | (12,69021549; 12,69021552) | 13,4888025606 |
| (3,1,1), 80D | (13,21496698; 13,21496701) | 13,9820689612 |
| (2,2,1), 66D | (14,05933886; 14,05933889) | 14,7757785284 |
| (1,1,1,1,1), 8D | (16,96304246; 16,96304249) | 17,5052599124 |
| (2,1,1,1), 42D | (14,90966915; 14,90966918) | 15,575089001 |

Diese Werte stehen in den fünf `exact_*.json`-Dateien. Für den größten
86D-Block reichen 15 Primzahlen zur eindeutigen Rekonstruktion, eine
16. unbenutzte Primzahl bestätigt alle Koeffizienten. Der ganze abschließende
Zertifikatslauf wurde erfolgreich mit Exitstatus 0 beendet. Insgesamt liegen
16 vollständige modulare Sätze mit je fünf reduzierten Matrizen vor.

## Reproduktion

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 power_certificate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 -O power_certificate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 projector_identities.py
```

Neubau eines gesamten modularen Satzes der fünf Blöcke:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py modular --prime 99999989
```

Für das konkrete 42D-Polynom:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py certify --shape 2111
```

Normale und optimierte Ausführung bestanden. Es wurden ausschließlich Dateien
in diesem eigenen Unterordner erzeugt. Keine fremden Quellen geändert, keine
Commits, keine PDF- oder globale Physikpromotion.

Der nächste endliche Schritt ist die gleiche Konstruktion mit einem
nichttrivialen Translationscharakter und primitiven Projektoren der kleinen
Gruppen S4 beziehungsweise S2×S3. Ihre Multiplizitäten und Impulsorbitgewichte
sind bereits bekannt; ihre vollständigen Matrizen und Untergrenzen wurden
in diesem begrenzten Anschluss noch nicht gebaut.
