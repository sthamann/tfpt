# Rotor-Gauß-Brücke: exakte Reduktion und Ladungsgate

20. September 2026 · **UR.SOURCE.ROTOR_GAUSS.01 — PARTIAL**

**Im bereits definierten Randmodell ist die kompatible primitive Eichladung
bis auf ihr Vorzeichen eindeutig:** `g=+/-K n`, wenn sämtliche E₈-Ströme und
der gewünschte Rekonstruktionsterm `n` neutral bleiben sollen. Diese Ladung
erlaubt den nackten `n`-Term und verbietet den nackten Konkurrenten `z`.
Ihre mikroskopische Realisierung und die Erzeugung des erlaubten Terms sind
damit noch nicht hergeleitet.

Diese Untersuchung prüft, was der bereits vorhandene dynamische
kompakte-U(1)-Rotor tatsächlich liefert, bevor er als Quelle für die
bedingte E₈-Randkonstruktion verwendet wird. Das positive Ergebnis ist eine
exakte Beschreibung des vollständigen Gauß-physischen Raums auf jedem
endlichen zusammenhängenden Graphen: Besetzungen, ganzzahlige
Zykluskoordinaten, alle ursprünglichen Hoppings, Zustände und dieselbe Zeit
werden durch eine unitäre Koordinatenabbildung mitgeführt. Auf einem Baum
verschwindet der Zyklusteil; auf Graphen mit Zyklen bleibt ein ganzzahliges
Winding-Gitter.

Das ist eine echte Quelleigenschaft des gewählten Rotors, aber noch keine
Identifikation mit dem QWZ-/Clock-Quelloperator, keine P1/P2-Herleitung und
keine Auswahl eines E₈-Zustands oder einer Wechselwirkung. Die bekannte
Zweikanten- und Quadratmechanik wird als ältere Provenienz geführt:
`local-window-round37`, `matter-resummation-round43` und
`common-engine-threeway` werden hier nicht als neue Resultate ausgegeben.

Die exakte Reduktion lautet für Inzidenzmatrix `B`, Ladung
`rho=N-1`, Baumfluss `E_T(rho)` und fundamentale Zyklusmatrix `C`

```text
E = E_T(rho) + C w,                         w in Z^b,
|E|^2 = rho^T Lplus rho
       + (w+theta(rho))^T (C^T C) (w+theta(rho)),
theta(rho) = (C^T C)^(-1) C^T E_T(rho).
```

Die Hoppings verschieben die Zykluskoordinaten durch den tatsächlichen
integeren Pfadvektor. Damit bleiben CAR-Zeichen, ursprüngliche Koeffizienten,
Onsite-Backtracks und die Zeitentwicklung erhalten. Die Formel ist eine
Koordinatenreduktion des deklarierten Parents, kein neues Kraftgesetz.

Der neue entscheidende Ladungstest betrifft die direkte gemeinsame Quelle.
Für die bedingte zehn-dimensionale Randkonstruktion gilt mit `q(x)=sum_i x_i`
für die transportierten E₈-Wurzeln die Ladungsverteilung

```text
q       -4   -2    0    2    4
Wurzeln  1   56  126   56    1.
```

Alle acht Cartan-Richtungen sind neutral; 114 der 240 Wurzelströme tragen
also diese Quellladung. Falls genau dieses `q` mit der gauged rotorischen
Gesamtladung identifiziert wird und die Bilder strikt endlich-supportige,
Gauß-invariante Observablen sein sollen, können nur ladungsneutrale Bilder
überleben. Eine injektive Abbildung aller E₈-Ströme unter diesen Prämissen
scheitert daher an den 114 geladenen Strömen.

Das ist ein konditionales Typ- und Ladungsgate. Es behauptet weder, dass
Fermionen in einer beliebigen Eichtheorie unmöglich sind, noch dass E₈ in
einer beliebigen geladenen, nichtlokalen oder erweiterten Algebra unmöglich
ist. Charged-sector-Intertwiner, Randstrings und eine anders hergeleitete
globale Symmetrie bleiben andere Zielalgebren. Auch der neutrale Rest ist
noch nicht als E₇- oder E₈-Operatorabbildung konstruiert.

## Konstruktive Umkehr: welche Ladung die volle E₈-Verklebung verträgt

Die direkte `q=sum x`-Identifikation ist nicht die einzige logisch mögliche
Ladungswahl. Innerhalb derselben bereits deklarierten zehnkanaligen
E₈-Verklebung kann man alle ganzzahligen Covektoren `g` klassifizieren, die
alle transportierten E₈-Wurzeln neutral lassen. Mit
`a=(1,1,1,-1,-1,-1,-1,-1)` ergibt die Bedingung für den vollständigen
Wurzelsatz exakt

```text
g=(v a,u,-3v),  u,v in Z.
```

Fordert man zusätzlich, dass der bestehende `n`-Transfer neutral bleibt, und
verlangt man einen nichttrivialen primitiven Covektor, bleibt bis auf das
Vorzeichen nur

```text
g = +/- K n
  = +/- (1,1,1,-1,-1,-1,-1,-1,-1,-3).
```

Für diese notwendige Kandidatenladung verschwinden die reinen und gemischten
bilinearen Anomaliebeiträge mit `g` gegen `q` und `Y`. Die chirale
Gravitationsanomalie ist damit nicht aufgehoben: die Signatur von `K` bleibt
`9-1=8`. Außerdem gilt `g.n=0`, aber `g.z=2`; ein nacktes `cos(n)` ist unter
dieser Kandidatenladung erlaubt, das nackte konkurrierende `cos(z)` nicht.

Das ist eine positive Umkehrbedingung und ein schärferes nächstes Quellgate.
Sie ist weder im alten gleich geladenen L/H-Rotor realisiert noch eine
Herleitung einer Eichfeldquelle. Sie erzeugt keinen Kopplungskoeffizienten,
kein Gauging, keinen `cos(n)`-Term und keine Lücke. Eine geladen-dressierte
Variante könnte die Aussage zu `cos(z)` verändern und müsste separat
hergeleitet werden.

Damit bleibt das Verdict **PARTIAL**: Die Rotorseite ist exakt reduziert und
liefert reale Dichte-Rotor-Rückwirkung; der gemeinsame Feld-, Ladungs-,
Clock- und Zeit-Intertwiner zur E₈-Quelle fehlt weiterhin. Die im alten
Clock-Rotor-Vertrag ausgeschlossene standortfixierte, rotorunabhängige
C6-Liftung wird nicht erneut behauptet. Die begrenzte lokale U(1)-Korollar-
prüfung innerhalb der deklarierten Onsite-Klasse repariert den Ladungs-
Intertwiner ebenfalls nicht; sie ist keine allgemeine Symmetrieklassifikation.

## Nachtrag zur gemeinsamen Zeit

Der [exakte Zeitabgleich](time_gate/README.md) verbindet die ausgewählte
Kandidatenladung mit der bereits dokumentierten Viertelholonomie. Weil
sämtliche E₈-Ströme unter `g` neutral sind, verändert `H -> H+lambda Q_g`
keine ihrer Antwortenergien. Die bekannte Energiedifferenz zwischen einer
Spinorwurzel und ihren ursprünglichen `C`-/`J`-Bildern bleibt für jedes
reelle `lambda` gleich eins. Globale Quellladung und kompatible Eichladung
können deshalb in dieser Konstruktion nicht gleichgesetzt werden.

Der Nachtrag besitzt siebzehn eigene exakte Kontrollen, ein eigenes
Prüfsummenmanifest und bytegleiche normale/optimierte Ergebnisse. Er ist
vom Hauptagenten hergeleitet und geprüft; die unabhängige interne
Gegenprüfung des Hauptvertrags wird dafür nicht erneut beansprucht.
Zeitabhängige Clock-Liftungen bleiben ausdrücklich außerhalb des
Ausschlusses. Zusätzlich verbindet derselbe Nachtrag die Kandidatenladung
mit den 256 expliziten lokalen Spinorvertretern aus
`source-critical-local-fields-20260920`: Die beiden ungeraden Feldfamilien
tragen exakt `+1` beziehungsweise `-1`. Ihr Feldwörterbuch ist somit mit der
Ladung verträglich; der dort gewählte kritische Punkt mit beiden nackten
Termen `n,z` wäre unter dieser Eichung jedoch nicht unverändert zulässig,
weil `z` Ladung 2 trägt. Auch dieser Nachtrag hat Verdict **PARTIAL**.

## Reproduktion

Aus dem Repository mit Python und SymPy:

```sh
python3 -B experiments/theory-contracts/source-rotor-gauss-20260920/checker.py --output experiments/theory-contracts/source-rotor-gauss-20260920/certificate.json
python3 -B -OO experiments/theory-contracts/source-rotor-gauss-20260920/checker.py --output experiments/theory-contracts/source-rotor-gauss-20260920/certificate.optimized.json
```

Die 73 exakten Kontrollen wurden normal und optimiert ausgeführt; die
Ergebnisse sind bytegleich. Geprüft werden alle Besetzungen der bezeichneten
kleinen Bäume, alle ihre Kantenorientierungen, die ausdrücklich angegebenen
Windungsrepräsentanten von Quadrat und Leiter sowie die komplette E₈-Liste.
Die allgemeinen Graph-, Lokalitäts-, Symmetrie- und Zeittransportsätze stehen
im [analytischen Beweis](PROOF.txt). Endliche Kontrollen ersetzen ihn nicht.

Die [Quelleninventur](SOURCE_INVENTORY.txt), die [interne Gegenprüfung](REVIEW.txt)
und die Originaldateien sind mit Prüfsummen in `source_manifest.json` gebunden.
Die Gegenprüfung ist keine externe Begutachtung oder Formalisierung.
Keine Promotion in Paper, Ledger, Website oder physische T1–T8-Gates.
