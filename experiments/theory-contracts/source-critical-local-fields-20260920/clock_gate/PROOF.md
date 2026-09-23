# Kritischer Randpunkt: tatsächliche Clock- und Ladungsverträglichkeit

**Verdikt: PARTIAL; die folgenden Aussagen sind exakt im festgehaltenen Wörterbuch.**
Geprüft werden der bereits vorhandene Konkurrenzpunkt `Vc`, die zwei neutralen
Wechselwirkungen `n,z`, die ursprüngliche Hyperladung und die im vorherigen
gemeinsamen Quellenanschluss konstruierten 10D-Lifts von `C,J`.
Die Rechnung ersetzt keine physikalische Implementierung der Clocks.

Mit `K=diag(1^9,-1)`, `z=e9-e10`, `u=(n+z)/2`, `v=(n-z)/2` ist

\[
V_c=K+2Kvv^T K,\qquad
\Delta_{V_c}(n)=\Delta_{V_c}(z)=1.
\]

Die Metrik ist positiv mit Eigenwerten `1` (achtfach) und `7±4√3`.
Die beiden Vertices haben `q=Y=0`. Dies ist der ausgewählte kritische
Diagnosepunkt aus `UR.SOURCE.GRADED_LOCALITY.01`, kein neu ausgewähltes Modell.

## Feste Clock-Lifts

Die zuvor gespeicherten Lifts fixieren das Hilfspaar
`e_R=-e9`, `m=n+e9` punktweise und wirken auf dem E8-Anteil durch

\[
S_A F_{aux}(p)=F_{aux}(Ap),\qquad A=C,J.
\]

Für alle Potenzen der beiden endlichen Clocks ergibt sich:

| genaue Bedingung | `C^k`, `0≤k<30` | `J^k`, `0≤k<4` |
|---|---|---|
| `S^T Vc S=Vc` | nur `k=0` | nur `k=0` |
| `S z=±z` | nur `k=0` | nur `k=0` |
| `Y(S z)=0` | nur `k=0` | nur `k=0` |

Die letzte Zeile ist strenger als bloß fehlende Energieinvarianz: Eine
Vervollständigung des `z`-Terms durch seine ganze feste Clock-Bahn würde
geladene Vertices hinzufügen. Bei festem Hyperladungs-U(1) ist eine Summe
solcher Cosinus-Terme nicht invariant. Unterschiedliche Vertexladungen
lassen sich nicht durch die bloße Summe ihrer Koeffizienten wegheben.
Ein dynamischer geladener Koeffizient wäre eine zusätzliche Quelle, die hier
nicht vorhanden ist.

Schon die ersten Gegenbeispiele lauten

\[
Y(S_Cz)=-4/3,\quad Y(S_Jz)=-8/3.
\]

Diese feste Bahn ist auch kein gemeinsam pinnbares Nullgitter. Da

\[
z=F_{aux}(-a)-e_R-3m,
\quad z_k=F_{aux}(-A^k a)-e_R-3m,
\]

gilt für zwei verschiedene Bahnelemente exakt

\[
B(z_k,z_l)=a^T A^{l-k}a-8
=-\frac12\|A^k a-A^l a\|^2<0.
\]

Jedes einzelne ist selbstnull, zwei verschiedene sind nicht gegenseitig
null. Das widerlegt nur die entsprechende simultane Nullvektor-Pinning-
Konstruktion; konkurrierende Wechselwirkungen sind dadurch nicht allgemein
verboten. Ihre Ladungsverletzung bleibt im hier festgelegten Modell separat.

## Warum eine reine Paardekoration die Familienfrage nicht umgeht

Ein reines Zusatzpaarfeld `A e_R+B m` hat

\[
Y=B-A,\qquad q=B-A,\qquad (-1)^F=(-1)^{A+B}.
\]

Hyperladungsneutralität verlangt `A=B` und damit gerade Parität. Man kann
also einen festgehaltenen bosonischen E8-Spinorstrom nicht ausschließlich
mit einem neutralen ungeraden Feld dieses Paares fermionisch machen.
Dies ist kein Ausschluss neutraler ungerader Felder im gesamten Gitter:
der gemeinsame Familien-Vektorzweig `(1,6)` enthält solche Felder. Gerade
dieser zusätzliche Familienfaktor verändert aber die Darstellung.

Die Ladung wirkt im gemeinsamen Wörterbuch durch `T(Y8)`, während

\[
F_{aux}(Y_8)=T(Y_8)+n.
\]

Die beiden Cartanwirkungen stimmen auf `n`-orthogonalen Feldern überein,
auf allgemeinen lokalen Feldern nicht. Das erklärt, weshalb man die neue
ungerade `c`-Klasse nicht durch Umbenennen als den alten E8-Spinorzweig
behandeln darf.

## Verhältnis zu früheren Ausschlüssen und offene Identifikation

`UR.COMPILER.CLOCK_CURRENT_CLOSURE.22` hatte bereits gezeigt, dass der
native `C` die feste D8-Stromunteralgebra nicht erhält und ihre
Vervollständigung die gewählte E8-Spinorchiralität braucht. Das wird hier
nicht als neue Entdeckung gezählt. Neu geprüft sind die **konkrete
Konkurrenzmetrik, ihre zweite Wechselwirkung und deren vollständige
Clock-Bahnen im schon konstruierten 10D-Lift**.

Falls die Clocks Symmetrien genau dieses stationären Hamiltonoperators
sein sollen, scheitert dieser Anschluss. Falls ihre physikalische Bedeutung
stattdessen einen Wechsel der Markierung, des Zustands oder des
Hamiltonoperators verlangt, muss genau dieser gemeinsame Transport aus
der Quelle hergeleitet werden. Die Rechnung verbietet eine solche andere
Realisierung nicht und liefert sie auch nicht.

## Reproduktion

`python3 checker.py` und `python3 -OO checker.py` prüfen rationale Matrizen,
alle endlichen Bahnelemente und die Herkunfts-Hashes. Die vielen einzelnen
Paarprüfungen sind Instanzen einer Formel, keine unabhängigen physikalischen
Evidenzen. Keine Datei der tragenden Verifikationssuite wird verändert.
