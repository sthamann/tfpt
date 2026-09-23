# Gemeinsame Zeit: Konsequenz der kompatiblen Eichladung

20. September 2026 · Nachtrag zu **UR.SOURCE.ROTOR_GAUSS.01 — PARTIAL**

Die im Hauptvertrag bestimmte Kandidatenladung `g=K n` wirkt auf sämtliche
transportierten E₈-Wurzelströme neutral. Die vorhandene globale Quellladung
`q=(1,...,1)` wirkt dort hingegen nicht trivial. Deshalb kann eine Korrektur
der Zeitentwicklung um ein beliebiges Vielfaches der Kandidateneichladung
die bekannte Viertelholonomie auf diesen Strömen nicht beseitigen.

Das ist eine neue Konsequenz der Ladungsklassifikation. Die Viertelholonomie,
die Clock-Matrizen und deren unterschiedliche Wurzelenergien stammen bereits
aus `charged-source-time-audit-20260920` und
`compiler-integral-triality-20260918`. Sie werden hier erneut geprüft,
nicht als neue Herkunftsherleitung ausgegeben.

## Genaue Voraussetzungen

Wir verwenden dieselbe bedingte zehnkanalige Randkonstruktion wie der
Hauptvertrag, mit `K=diag(1,...,1,-1)` und

```text
n = (1,1,1,-1,-1,-1,-1,-1,-1,3),
a = (1,1,1,-1,-1,-1,-1,-1),
F(r) = (r-(a.r)a/2, 0, -a.r),
g = K n,       q = (1,...,1).
```

Dabei ist `r` eine der 240 E₈-Wurzeln mit `|r|²=2`. Für einen Wurzelstrom
`V_r` gelten `[Q_g,V_r]=(g.F(r)) V_r` und analog für `Q` mit `q`.
Die weiterhin bedingte achtkanalige Zeit des früheren Vertrags lautet

```text
H_hol = L0 - Q/4,       E(r)=1-q.F(r)/4.
```

Diese Formel setzt die bereits gewählte Randrealisierung und deren
Zeitnormierung voraus. Sie wird hier nicht aus P1/P2 oder aus dem
zweikomponentigen kompakten Rotor neu hergeleitet.

## Kurzer vollständiger Beweis

Die Hauptrechnung ergibt für jede Wurzel `g.F(r)=0`. Daher gilt für jedes
reelle `lambda`

```text
[H_hol + lambda Q_g, V_r] = [H_hol, V_r].
```

Auch die Anregungsenergie relativ zu einer Referenz mit festem `Q_g` bleibt
unverändert. Dagegen ist `q.F(r)=sum r_i`. Die 240 Wurzelzustände haben
folglich dieselbe bereits bekannte Verteilung

| E(r) | 0 | 1/2 | 1 | 3/2 | 2 |
|---|---:|---:|---:|---:|---:|
| Anzahl | 1 | 56 | 126 | 56 | 1 |

Als ausdrücklichen Zeugen verwenden wir `s=(1/2,...,1/2)`. Für die
ursprünglichen, aus dem Triality-Zertifikat geladenen Clock-Matrizen `C,J`
gilt

```text
q.F(s)=4,       q.F(C s)=q.F(J s)=0,
E(s)=0,         E(C s)=E(J s)=1.
```

Alle drei Wurzeln haben `Q_g`-Ladung null. Der Energieunterschied eins
bleibt daher für jedes `lambda` erhalten. Insbesondere macht der Ersatz
`H_hol -> H_hol+lambda Q_g` die bezeichneten statischen Clock-Wirkungen
nicht zu energietreuen Symmetrien dieser Zeitentwicklung.

Das beweist die bezeichnete Einschränkung für alle reellen `lambda`, nicht
nur an ausgewählten Parameterwerten. Es verbietet weder zeitabhängige
Clock-Liftungen noch eine andere aus der Originalquelle hergeleitete Zeit.
Solche Konstruktionen müssten ihre tatsächliche Wirkung auf dieselben
Felder und Zustände ausdrücken.

## Bedeutung für die gemeinsame Quelle

Die kompatible Eichladung und die globale Quellladung haben verschiedene
Aufgaben. Die erste lässt die gesamte E₈-Stromalgebra neutral; die zweite
unterscheidet deren Zeitantworten. Beide dürfen deshalb in einer
Herkunftsherleitung nicht durch dieselbe Ladung ersetzt werden.

Die konstruktive Zielbedingung wird damit präziser: Eine gemeinsame Quelle
muss sowohl die kompatible Ladungswirkung als auch die vorhandene geladene
Zeitwirkung mit passenden Operatorabbildungen realisieren. Der Hauptvertrag
hat eine notwendige Ladung ausgewählt. Dieser Nachtrag zeigt, welche offene
Zeitaufgabe dadurch nicht automatisch mitgelöst wird.

## Anschluss an die tatsächlich konstruierten ungeraden Felder

Der aktuelle Vertrag `UR.SOURCE.CRITICAL_FIELDS.01` gibt in
`source-critical-local-fields-20260920/ERGEBNIS.md` zwei lokale
Spinorfeldfamilien an. In genau demselben Gitterwörterbuch lauten sie

```text
T(p)=(p,-a.p/2,a.p/2),       u=(n+z)/2,       v=(n-z)/2,
x_R(p)=T(p)+u,               x_L(p)=T(p)+v.
```

Hier durchläuft `p` die 128 Halbvektoren mit einer ungeraden Zahl negativer
Einträge, also die dort bezeichnete `c`-Spinorklasse. Der Zusatz `R/L`
bezeichnet die übernommenen Feldnamen; er macht nicht beide ganzen Felder
zu rein rechts- beziehungsweise linksbewegenden Weyl-Feldern.

Es gilt für **jedes** reelle `p`

```text
g.T(p)=a.p + a.p/2 - 3 a.p/2 = 0.
```

Mit `g.n=0` und `g.z=2` folgt daher ohne Dimensionsvergleich

```text
g.x_R(p)=+1,                 g.x_L(p)=-1.
```

Die 256 bezeichneten Felder sind ganzzahlig und mikroskopisch ungerade.
Die Kandidatenladung lässt somit die vorhandenen lokalen fermionischen
Felder als **geladene Felder** zu, während sie die E₈-Ströme neutral lässt.
Dies ist eine algebraische Kompatibilität. Nach einer tatsächlichen lokalen
Eichung wären diese einzelnen geladenen Felder keine Gauß-invarianten
lokalen Observablen; ihre physische Realisierung müsste die erforderliche
Ladungssektor- oder Stringstruktur enthalten. Eine solche Realisierung wird
hier nicht gebaut.

Dieselbe Rechnung entscheidet eine Grenze der Kombination mit dem dortigen
bedingten Ising-Punkt: Dieser verlangt beide nackten Vertices `n,z`. Unter
der Kandidateneichladung ist nur `n` neutral. Der unergänzte `z`-Term ist
geladen und darf in einem exakt eichinvarianten Hamiltonoperator nicht
einfach mitgeführt werden. Ein weiterer geladener Faktor könnte einen
neutralen Gesamtterm liefern, wäre aber eine zusätzlich herzuleitende
Quelle. Daraus folgt weder ein allgemeiner Ausschluss kritischer Phasen
noch eine bereits konstruierte alternative Phase.

Damit werden **zwei** Anschlüsse unterschieden: Das Feldwörterbuch verträgt
die notwendige Ladung ausdrücklich; die dort gewählte kritische
Wechselwirkung wird dadurch nicht automatisch zu einer zulässigen
Wechselwirkung derselben geeichten Quelle.

## Reproduktion und Reichweite

```sh
python3 -B experiments/theory-contracts/source-rotor-gauss-20260920/time_gate/checker.py
python3 -B -OO experiments/theory-contracts/source-rotor-gauss-20260920/time_gate/checker.py --output experiments/theory-contracts/source-rotor-gauss-20260920/time_gate/certificate.optimized.json
```

Der Checker verwendet exakte rationale Matrizen und symbolisches `lambda`.
Siebzehn algebraische Kontrollen umfassen die vollständige Wurzelliste,
die tatsächlichen Clock-Matrizen und alle 256 bezeichneten lokalen
Spinorvertreter. Vor der Rechnung werden alle in diesem
Nachtrag verwendeten Quellen sowie der Checker und dieser Text gegen das
eigene Prüfsummenmanifest geprüft. Die Ergebnisse normaler und optimierter
Ausführung sind bytegleich.

Dieser kurze Nachtrag wurde vom Hauptagenten hergeleitet und nachgerechnet.
Die separate interne Gegenprüfung des Hauptvertrags wird nicht als
unabhängige Begutachtung dieses Nachtrags ausgegeben. Kein neuer
Hamiltonoperator, keine mikroskopische Eichrealisierung und kein physisches
T1–T8-Gate wurden hier geschlossen.
