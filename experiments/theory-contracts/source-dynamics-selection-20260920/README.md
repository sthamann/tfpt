# Welche Dynamik erzeugt die E₈-Randphase?

20. September 2026 · **UR.SOURCE.DYNAMICS_SELECTION.01 — PARTIAL**

Die Untersuchung prüft die Herkunft der zuletzt verwendeten Energie. Das
Ergebnis unterscheidet eine korrekte Übersetzung der Quelle von einer Änderung
ihrer Wechselwirkungen. Die achtfache Quelle samt Zusatzpaar bleibt dabei ein
bereits gewählter Vergleichskandidat. Die tatsächliche bisherige QWZ-Quelle
liefert einen freien chiralen Kanal pro Rand.

**Die Energie muss mitübersetzt werden.** Der bekannte ganzzahlige Wechsel
zum E₈-Wörterbuch führt die ursprüngliche freie Energie auf `WᵀW`. Die zuletzt
verwendete entkoppelte E₈-plus-Paar-Energie ist eine andere Matrix. Das lässt
sich an denselben ursprünglichen Feldern unterscheiden: Ihre Skalendimension
steigt für die acht ursprünglichen Kanäle von `1/2` auf `3/2`. Von den 240
übersetzten E₈-Wurzeln besitzen im freien Ausgangssystem nur 56 Dimension
eins; bei der gewählten rekonstruierten Energie sind es alle 240.

Diese Energiewahl ist somit ein physikalischer Eingriff, keine bloße neue
Schreibweise. Das war als Annahme bereits benannt; jetzt ist ihr Unterschied
für die tatsächlichen ursprünglichen Felder und den ganzen Wurzelsatz
ausgerechnet.

**Der Unterschied lässt sich stark vereinfachen.** Nur eine kollektive
Kombination der rechten Kanäle und der linke Zusatzkanal werden miteinander
vermischt. Acht dazu senkrechte Richtungen bleiben auf diesem Vergleichspfad
unverändert. Zwischen den beiden vorhandenen Energiematrizen gibt es dadurch
eine einfache direkte Verbindung mit einem einzigen Parameter `θ`.

Mit `A = arcosh(3)` lauten die Dimensionen der zwei bereits vorhandenen
konkurrierenden Wechselwirkungen:

\[
\Delta_z(\theta)=\cosh^2\theta,
\qquad
\Delta_n(\theta)=\cosh^2(A-\theta),
\quad 0\le\theta\le A.
\]

| Energiepunkt | Gewöhnlicher Paarterm z | E₈-Rekonstruktionsterm n |
|---|---:|---:|
| Freier Anfang | 1 | 9 |
| Mitte der direkten Verbindung | 2 | 2 |
| Bisher gewählte E₈-Energie | 9 | 1 |

In der ausgedehnten eindimensionalen Randtheorie ist ein solcher Term bei
Dimension unter zwei nach einfacher Skalenzählung relevant. Bei genau zwei
ist er marginal: Erst seine tatsächliche Wechselwirkungsentwicklung
entscheidet über Verstärkung oder Abschwächung.

**Am Mittelpunkt ist die Konkurrenz vollständig eingegrenzt.** Für sämtliche
ganzzahligen, quellenzahl-, hyperladungs- und glue-neutralen selbstnullen
Vertexoperatoren ist die Dimension dort mindestens zwei. Gleichheit erreichen
ausschließlich `±n` und `±z`. Das folgt aus einem allgemeinen Gitterbeweis;
eine endliche Aufzählung dient als zusätzliche Kontrolle.

Der Ausschluss gilt sogar auf der ganzen direkten Verbindung: Jeder andere
zulässige neutrale selbstnulle Vertexoperator besitzt dort Dimension
mindestens `7/2`. Somit können innerhalb dieser genau bezeichneten Klasse
nur `n` und `z` die Relevanzschwelle erreichen. Das ist ein allgemeiner
Beweis für alle solchen Gittervektoren, keine Suche bis zu einer willkürlich
gewählten Größe.

Das beweist keine Ising-Phase und keinen von TFPT ausgewählten kritischen
Punkt. Der Vergleichsparameter ist kein hergeleiteter RG-Fluss. Andere
Operatoren, Kopplungsamplituden und ihre Rückwirkung müssen berücksichtigt
werden. Der zuvor untersuchte gesonderte Ising-Vergleichspunkt hatte für beide
Terme Dimension eins und ist eine andere Energieform.

**Die fehlende Wechselwirkung ist jetzt in der ursprünglichen Sprache
sichtbar.** Der Term `n` umfasst zwölf ursprüngliche Fermionfaktoren und drei
Ableitungen aus der nötigen Punktaufspaltung. Er ist in dieser Sprache kein
gewöhnlicher Zweifermion-Massenterm. Die Zahl zwölf ist innerhalb der
charakteristischen Nullvektorklasse sogar minimal. Das verlangt keinen
fundamentalen Zwölfteilchenterm als neues Postulat: Echte Wechselwirkungen
niedrigerer Ordnung könnten ihn erzeugen. Die bisher freie Quelle tut das
unter den regulären gaußschen Reduktionen jedoch nicht.

Die entsprechende Gaussian-Closure-Grenze war bereits bewiesen und wird hier
als Vorarbeit verwendet. Auch die komplexe Phase des Komplementdeterminanten
ändert diese Grenze nicht. Ein vorhandener anderer Rotor-Parent enthält echte
nichtgaußsche Dynamik; sein gemeinsames Operator-, Ladungs-, Zustands- und
Zeitwörterbuch zu dieser Randquelle fehlt weiterhin.

Der nächste Herkunftsnachweis muss deshalb die tatsächliche kollektive
Dichtekopplung und den erlaubten kohärenten Transfer aus der ursprünglichen
Quelle gewinnen. Eine weitere Anpassung der schon gewählten Randenergie
wäre kein Ersatz dafür. Native Kanalzahl, physikalische Phasenauswahl,
chirale 3+1D-Materie und Gravitation bleiben offen.

[PROOF.txt](PROOF.txt) enthält die Herleitungen und Voraussetzungen.
`SOURCE_INVENTORY.txt` dokumentiert den Abgleich mit den Originalquellen,
`REVIEW.txt` die separate mathematische Prüfung. Die endlichen Kontrollen
belegen ihren ausgewiesenen algebraischen Umfang, keine vollständige TOE.
Keine Paper-, Ledger-, Scorecard- oder T1–T8-Promotion.

Reproduktion aus dem Repository mit Python und SymPy:

```sh
python3 -B experiments/theory-contracts/source-dynamics-selection-20260920/checker.py
python3 -OO -B experiments/theory-contracts/source-dynamics-selection-20260920/checker.py
```

Beide Zertifikate müssen bytegleich sein. Das Quellenmanifest prüft die
festgehaltenen Eingaben; veränderte Dateien werden nicht automatisch neu
gepinnt. Die frühere Gaussian-Closure wird hier durch einen kleinen exakten
Vergleich illustriert, nicht als neuer allgemeiner Satz ausgegeben.
