# Polarer Kontextschatten: gemeinsame Algebra, keine neue physikalische Regel

## Ergebnis in einem Satz

Die vorhandene Regel `K=B/7` besitzt tatsächlich eine kanonische, exakt
intertwiner-kompatible Zerlegung in ein reversibles **lineares** Vorzeichen und
einen positiven Verlust. Das ist eine nützliche gemeinsame algebraische
Normalform der bereits gewählten Regel, aber weder ein klassischer reversibler
Schritt noch eine Herleitung eines physikalischen Unitary auf `C4`.

Die Konstruktion benutzt ausschließlich die vorhandenen 15 Klassen, ihre
Compiler-Familienbits, die ursprünglichen 15 Pauli-Kontexte und den bereits
definierten 60-Strahlen-Übergang. Keine größere Zellgeometrie, keine neuen
physikalischen Zustände und keine Spektralsuche werden eingeführt.

## 1. Kanonisches Vorzeichen und Verlust

Setze `P0=J15/15`, `Q=I-P0`. Aus `B=B^T`, `B1=7·1` und
`B²=4I+3J15` folgt die orthogonale Zerlegung

`B = 7P0 + 2P9 - 2P5`,

mit Projektorrängen `1,9,5`. Explizit:

`P9 = I/2 + B/4 - 9P0/4`,

`P5 = I/2 - B/4 + 5P0/4`.

Damit ist

`S = P0 + (B-7P0)/2 = P0+P9-P5 = B/2-J15/6`,

`|K| = P0 + (2/7)Q`,

und exakt

`S²=I`, `S^T=S`, `|K|²=K^T K`, `S|K|=|K|S=K`.

Weil K invertierbar ist, ist S sein eindeutiger orthogonaler Polaroperator.
Die Einträge von S sind jedoch `1/3` auf der Inzidenz und `-1/6` außerhalb.
S erhält die euklidische Norm, aber nicht den Wahrscheinlichkeitssimplex.
Es ist insbesondere **kein** klassischer Markovschritt und keine Permutation.
`|K|` ist dagegen selbst ein strikt positiver stochastischer Operator:
Diagonalwert `1/3`, sonst `1/21`.

Für jede ganze Zahl `n>=0` folgt direkt aus den drei Projektoren

`K^n = P0+(2/7)^n(P9+(-1)^n P5)`.

Das erklärt die Zweischritt-Vereinfachung und die alternierenden fünf
Kontrastmoden. Es liefert keine unabhängige Wahl der Schrittzeit. Ein
Zweischrittoperator allein unterscheidet K und seinen positiven Quadratwurzel-
Operator nicht.

## 2. Welche positiven Verluste sind wirklich alle möglich?

Die Aussage hängt entscheidend davon ab, welche Symmetrie und welche Art von
Positivität gemeint sind. Hier bedeutet **positiver Verlustoperator** zunächst
selbstadjungiert positiv semidefinit im Hilbertraumsinn und kontraktiv. Das ist
nicht dasselbe wie eintragsweise Markovpositivität oder vollständige
Quantenpositivität.

### Volle Inzidenzsymmetrie, stationär normiert

Für `G=Aut(B)=Sp(4,2)` werden exakt 720 Permutationen erzeugt. Die drei Orbits
auf geordneten Paaren haben Größen `15,90,120`. Deshalb ist der vollständige
Kommutant dreidimensional, `span(I,B,J15)`, und die Darstellung zerfällt
multiplizitätsfrei in `1+9+5`.

**Alle** G-kompatiblen positiven Kontraktionen mit `A1=1` haben daher die Form

`A = P0+alpha P9+beta P5`, `0<=alpha,beta<=1`.

Bei `alpha,beta>0` ist S der eindeutige volle Polaroperator von `M=SA`.
Verschwindet einer der Parameter, ist der kanonische Polaroperator nur noch
partiell; S bleibt dann eine mögliche orthogonale Erweiterung auf dem Kern.
Ohne die stationäre Normierung wäre auch der Koeffizient von P0 frei.

Symmetrie erzwingt also **zwei**, nicht einen Kontrastparameter. Eine beliebige
Einparameterfamilie ist zunächst nur eine Wahl von Funktionen
`alpha(t),beta(t)`. Unter der zusätzlichen Annahme eines stetigen homogenen
positiven Kontraktionssemigruppen-Gesetzes mit `A(0)=I` sind genau

`A(t)=P0+exp(-gamma9 t)P9+exp(-gamma5 t)P5`, `gamma9,gamma5>=0`,

möglich. Die beiden Raten und eine physikalische Zeitkalibrierung sind damit
nicht ausgewählt. Auch ist `S A(t)` selbst keine bei I beginnende Halbgruppe:
das zusätzliche S verschwindet bei zwei aufeinanderfolgenden Schritten.

Soll zusätzlich A(t) selbst für alle Zeiten ein **klassischer Markovkernel**
sein, lautet die vollständige weitere Bedingung
`3gamma9<=5gamma5<=9gamma9`. Die beiden Offdiagonalraten des Generators sind
`(-3gamma9+5gamma5)/30` auf inzidenten Paaren und
`(9gamma9-5gamma5)/60` auf nichtinzidenten Paaren. Ihre Nichtnegativität ist
notwendig und hinreichend; die übliche Exponentialreihe nach Verschiebung um
eine genügend große skalare Rate schreibt den Prozess als positive Mischung
stochastischer Schritte. Dies macht S A(t) nicht zu einer bei t=0 positiven
Markovfamilie, denn ihr Anfangswert bleibt das vorzeichenbehaftete S.

### Zusätzliche Isotropie der beiden Kontrastsektoren

Erst `alpha=beta=rho` reduziert den Verlust auf

`A_rho=P0+rho Q`, `0<=rho<=1`.

Dann gilt

`M_rho=S A_rho = (rho/2)B + ((2-7rho)/30)J15`.

Dieser Operator ist genau für `0<=rho<=2/7` ein Markovkernel. Den **exakten**
ursprünglichen B-Support besitzt er nur bei `rho=2/7`; dort sind alle sieben
erlaubten Einträge gleich `1/7`. Bei `rho=0` ist der volle Polaroperator wieder
nicht eindeutig, da nur P0 übrig bleibt.

Dies ist eine bedingte Eindeutigkeit: **Isotropie + ursprünglicher Support**
selektieren K. Isotropie folgt nicht bereits aus G-Kovarianz.

### Ohne Isotropie bleibt sogar bei gleichem Support eine ganze Familie

Für `M=P0+alpha P9-beta P5` lauten die drei Eintragstypen:

| Eintragstyp | Wert |
| --- | --- |
| diagonal | `(1+9alpha-5beta)/15` |
| inzident, nicht diagonal | `(2+3alpha+5beta)/30` |
| nicht inzident | `(4-9alpha-5beta)/60` |

Unter `alpha,beta>=0` ist M genau dann Markov, wenn
`9alpha+5beta<=4` und `5beta-9alpha<=1`.
Exakter B-Support und eindeutiges volles S lassen weiterhin

`beta=(4-9alpha)/5`, `1/6<alpha<4/9`,

zu. In der schon vorhandenen Verweilwahrscheinlichkeits-Notation ist dies

`K_a=aI+(1-a)(B-I)/6`, `0<a<1/3`,

`|K_a|=P0+((1+5a)/6)P9+((1-3a)/2)P5`.

Alle diese Kernel haben denselben vollen Polaroperator S und denselben
Support. Nur bei `a=1/7` sind die beiden Kontrastverluste gleich. Der Prüfer
enthält `a=1/6` als exakte Gegenkontrolle gegen eine vermeintliche Auswahl
allein durch Support, Symmetrie und Polarzeichen.

### Mit der tatsächlichen q*-Markierung ist die Freiheit größer

Die Compiler-Markierung erhält nur die 120-elementige Untergruppe S5.
Ihre neun Paarorbits liefern einen neundimensionalen Kommutanten. Die
reelle Darstellung zerfällt als `1+1+4+4+5`.

Der Prüfer konstruiert die fünf orthogonalen Projektoren explizit aus dem
vorhandenen markierten Fünfersatz sowie eine normierte partielle Isometrie W
zwischen den beiden Standard-Viererräumen. Hier wirkt S auf einem Viererraum
positiv und dem anderen negativ. Nach Fixierung von `A1=1` sind **alle reellen
symmetrischen** kompatiblen Verluste

`A=P0+a R1+b R5+c R4plus+d R4minus+e(W+W^T)`,

mit `a,b in[0,1]` und `0<= [[c,e],[e,d]] <=I2`.

Die Vollständigkeit der fünf Parameter wird unabhängig durch den Rang der
Kommutanten-, Symmetrie- und Stationaritätsbedingungen geprüft. Die zusätzliche
Forderung `[A,S]=0` setzt `e=0` und lässt vier freie Verluste. Über komplexen
Hermiteschen Matrizen darf e komplex sein; dann stehen eW und sein Adjungiertes
anstelle des reellen Kreuzterms. Bloße Sigma-Kovarianz wäre nochmals schwächer.

Die zweiparametrige volle-Sp-Klassifikation darf daher nicht stillschweigend
als Klassifikation aller compilerseitig markierten Verluste ausgegeben werden.

## 3. Exakte vorhandene Intertwiner

Die Permutationsmatrix P wird nicht durch einen beliebigen Graphisomorphismus
geraten: Sie entsteht aus der ursprünglichen Gaußwurzelklasse, deren konkreter
Pauli-Kontextzuordnung und den ursprünglichen Compiler-Familienbits. Exakt gilt

`B_context P=P B_compiler`,

`S_context P=P S_compiler`, `|K|_context P=P |K|_compiler`,

sowie die entsprechende Gleichung für den ursprünglichen Sigma-Dreizyklus.
Diese gemeinsame Darstellung ist also wirklich im vorhandenen Wörterbuch
verankert.

Für den **bereits definierten** 60-Strahlen-Übergang gelten mit den vorhandenen
Auslesematrizen C und F

`T=(C^T B C+F^T F)/28`,

`P_C=C^T C/4`, `P_F=F^T F/12`, `P_H=I-P_C-P_F`, `rank(P_H)=30`.

Seine kanonische Polarzerlegung lautet

`|T|=C^T |K| C/4+(3/7)P_F`,

`sign(T)=C^T S C/4+P_F`.

Dabei ist `sign(T)^2=P_C+P_F`, nicht I. Der kanonische Polarteil ist wegen
des 30-dimensionalen Kerns nur eine partielle Isometrie. Eine reversible
Erweiterung auf diesem Kern wäre eine zusätzliche, nicht von T bestimmte Wahl.
Auch `|T|` ist nur im Hilbertraumsinn positiv: Sein kleinster Eintrag ist
exakt `-1/42`. Anders als das 15-dimensionale `|K|` ist der gemeinsame
60-Strahlen-Verlust daher kein klassischer Markovschritt.

Exakt geprüft sind die gemeinsamen Kontext-Intertwiner

`C sign(T)=S C`, `C|T|=|K| C`.

Für den tatsächlichen Quantendecode E auf Hermitesche `4x4`-Operatoren ist
der Befund besonders klar:

**`E sign(T)=E`, `E|T|=D E`,**

mit `D(rho)=(3/7)rho+(4/7)I4/4` auf normierten Zuständen. Außerdem gilt

`E C^T(I-P0)=0`.

Der ganze nichtuniforme Kontextkontrast ist in diesem Quantendecode unsichtbar.
Das nichttriviale Kontext-Vorzeichen wird also nicht als nichttrivialer
physikalischer C4-Schritt weitergereicht. Die Kontrastverluste der beiden
Schatten unterscheiden sich: `2/7` auf Kontexten, `3/7` auf Quantenzuständen.

Noch stärker: `det(S)=-1`, während jede unitäre C4-Adjunktwirkung auf dem
15-dimensionalen Raum traceless Hermitescher Operatoren Determinante +1 hat.
Nach Diagonalisierung des Unitary sind die sechs reellen Offdiagonal-Zweiebenen
Rotationen, die drei Diagonalrichtungen bleiben fest. Daher kann dieses S
auch nicht einfach in einer anderen Pauli-Basis als `Ad_U` realisiert werden.
Als abstraktes Unitary auf einem **zusätzlich postulierten** kohärenten C15-
Labelregister wäre S möglich; ein solcher physikalischer Registerlift folgt
hieraus nicht.

## 4. Woher kommen 7 und 2/7 — und wo nicht?

Für die bereits vorhandene nichtentartete F2-Paarung auf vier Bits hat die
orthogonale Hyperebene eines nichtnullen Labels acht Elemente einschließlich
null. Daher besitzt B genau `2^3-1=7` erlaubte Nachfolger. Zwei verschiedene
nichtnullige Labels sind über F2 unabhängig; ihr gemeinsames Orthogonales hat
`2^2-1=3` nichtnullige Elemente. Das ergibt `B²=4I+3J`, also Kontrastbetrag 2.

Wenn **die ungewichtete Inzidenzzählregel B bereits feststeht**, ist ihre
stochastische Normierung zwingend B/7 und der Kontrastverlust zwingend 2/7.
Beide Zahlen sind dann abgeleitet, keine Fitparameter.

Wenn dagegen nur der erlaubte Support und die Symmetrie feststehen, sind die
Gewichte noch nicht festgelegt: Die oben vollständig ausgewiesene K_a-Familie
ist die exakte Gegenkontrolle. Eine physikalische Auswahl des Readouts, der
Gleichgewichtung, der Isotropie, des kohärenten Lifts oder einer Zeiteinheit
wird durch die Polarzerlegung nicht ersetzt.

## Reproduktion und Grenzen

`checker.py` und `verification.json` liegen in diesem Ordner. Reproduktion aus
dem Repository-Verzeichnis:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 -B experiments/theory-contracts/compiler-kernel-foundation-20260914/polar_shadow/checker.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 -B -O experiments/theory-contracts/compiler-kernel-foundation-20260914/polar_shadow/checker.py
```

Der abschließende Lauf und der Lauf unter `-O` bestanden jeweils **1203**
aktive Guards. Alle neuen Guards bleiben unter Optimierung aktiv. Originalquellen werden
hashgeprüft bzw. mit Hashprovenienz dokumentiert, ausschließlich gelesen und
nicht verändert. Es gibt keine TOE-Promotion, keine neue physikalische
Dynamikbehauptung und keine große Spektralrechnung.
