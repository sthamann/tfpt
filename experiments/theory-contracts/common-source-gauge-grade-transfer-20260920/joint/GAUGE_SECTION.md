# Gemeinsame Eichmarkierung, E8-Zerlegung und Clock-Lift

20. September 2026 · exakte bedingte Randkonstruktion, physische Herkunft offen.

## Die im letzten Stand zusätzlich gewählte Richtung

Im bisherigen `(9,1)`-Randmodell sind

\[
K=\operatorname{diag}(1^9,-1),\quad
n=(1,1,1,-1,-1,-1,-1,-1,-1,3)^T
\]

festgelegt. Die alte E8-Zerlegung verwendete zusätzlich die positive
Einheitsrichtung \(e=e_1\) und \(v=n-e_1\). Sie zeichnete damit eine der
drei ursprünglichen Farbrichtungen aus. Ihre Energiematrix
\(V_*=K+2Kvv^TK\) ist positiv, aber unter dem ursprünglichen Farbtausch
\(P_{12}\) nicht invariant.

Der Konflikt betrifft nicht nur diesen einen Energiepunkt. Für die bisher
gewählten zehn-dimensionalen Clock-Lifts ist jede gemeinsam invariante
symmetrische Form in der alten Zerlegung von der Gestalt

\[
V=W_{\rm alt}^{-T}\operatorname{diag}
 \left(tG_{E8},\begin{pmatrix}b&c\\c&d\end{pmatrix}\right)W_{\rm alt}^{-1}.
\]

Die gemeinsame Invariantenrechnung dafür stammt aus dem gepinnten vorherigen
Contract. Der neue exakte lineare Test \(P_{12}^TVP_{12}=V\) liefert
\(t=-c-d\) und \(b=-2c-d\). Folglich gilt

\[
n^TVn=0.
\]

Da \(n\neq0\), kann keine dieser Formen positiv definit sein. **Die alten
festen Clock-Lifts und der ursprüngliche Farbtausch lassen sich in dieser
Kombination nicht zu einer gemeinsamen positiven Energie ergänzen.**
Dies ist kein No-Go für E8, für andere Lifts oder für die Randrekonstruktion.

## Konstruktive Reparatur aus dem bereits vorhandenen Zusatzpaar

Man kann stattdessen die zusätzliche rechte Quellrichtung verwenden:

\[
e=-e_9,\qquad v=n+e_9.
\]

Setze \(a=(1,1,1,-1,-1,-1,-1,-1)\),
\(k_a(p)=a\cdot p/2\), \(T_a(p)=(p,-k_a(p),k_a(p))\) und

\[
F_{\rm aux}(p)=T_a(p)-k_a(p)n.
\]

Dies ist genau die Quotienten-Sektion, die im neuen
`source-flavor-origin-20260920`-Entwurf verwendet wird. Aus einer E8-Basis B
erhält man

\[
W_{\rm aux}=(F_{\rm aux}(B),e,v),\quad
\det W_{\rm aux}=-1,\quad
W_{\rm aux}^TKW_{\rm aux}=G_{E8}\oplus\operatorname{diag}(1,-1).
\]

Die Matrix ist ganzzahlig. Die positive Energiematrix

\[
V_{\rm aux}=K+2Kvv^TK
\]

ist jetzt unter allen Vertauschungen der drei Farbkoordinaten, der zwei
schwachen Koordinaten und der drei Familienkoordinaten invariant. Die
einfachen Farb-, schwachen und Familienwurzeln \(e_i-e_j\) bleiben in
dieser Sektion die ursprünglichen Operatorvektoren; sie benötigen keinen
zusätzlichen Faktor in der massiven Nullrichtung.

In der ausdrücklich begrenzten Vergleichsklasse der neun vorhandenen
vorzeichenrichtig gewählten positiven Koordinatenachsen ist \(-e_9\) die
einzige Wahl mit diesen Blockvertauschungen. Das ist keine Eindeutigkeit
unter sämtlichen reellen oder ganzzahligen Komplementwahlen.

## Ladung und Clocks auf derselben Sektion

Mit der ursprünglichen Hyperladungsmarkierung und dem im anderen Entwurf
bedingt ausgewählten Zusatzpaar

\[
Y_{10}=(-1/3,-1/3,-1/3,1/2,1/2,0,0,0,1,1)^T
\]

gilt \(Y_{10}\cdot n=0\), \(Y_{10}\cdot F_{\rm aux}(p)=Y_8\cdot p\).
Die vorzeichenbehafteten Paarladungen sind nun

\[
Y_{10}\cdot e=-1,\qquad Y_{10}\cdot v=+1.
\]

Die Paarvektoren sind gegenüber den ursprünglichen Farb- und schwachen
Wurzeln orthogonal. Damit passt das Paar kinematisch zum geladenen
Lepton-Singulettpaar des Flavor-Entwurfs. Die alte Wahl \(e_1\) lieferte
stattdessen die Paarmarkierungen \(-1/3,+1/3\). Die Randbewegungsrichtungen
sind dabei weiterhin keine vierdimensionalen Lorentz-Chiralitäten.

Die nativen acht-dimensionalen C- und J-Matrizen werden unverändert durch

\[
S_{A,\rm aux}=W_{\rm aux}\operatorname{diag}(B^{-1}AB,I_2)W_{\rm aux}^{-1}
\]

übertragen. Die neuen Lifts sind ganzzahlig, erhalten K, n und die positive
Energiematrix und haben die ursprünglichen Ordnungen. **Ihre Wirkung auf
dem zehn-dimensionalen Quellenraum unterscheidet sich von den alten Lifts.**
Die Reparatur darf daher nicht als unveränderte mikroskopische Clock-Wirkung
oder als bloßes Umschreiben aller festgehaltenen Operatoren verkauft werden.

Auch die neuen Lifts erhalten die feste Hyperladungsmarkierung nicht:
\(S_C^TY_{10}\neq Y_{10}\), \(S_J^TY_{10}\neq Y_{10}\).
Ladungswörterbuch und Clock-Automorphismen sind damit gemeinsam darstellbar,
aber nicht als eine ladungserhaltende interne Clock-Symmetrie identifiziert.

## Was jetzt zusammenpasst und was noch fehlt

E8-Gitter, ursprüngliche Farb-/schwache Markierung, ein positives
Energiebeispiel, die nativen acht-dimensionalen Clocks und die Ladung des
massiven Zusatzpaares können jetzt in derselben bedingten Zerlegung geführt
werden. Dies ist eine konkrete Verbesserung des bisherigen Wörterbuchs.

Es wird weiterhin vorausgesetzt, dass die erweiterte Randquelle und ihre
Interaktion existieren. Die allgemeine positive Paar-Energiematrix bleibt
frei; die konkrete physische Auswahl des geänderten Clock-Lifts ist offen.
Das passend geladene Paar liefert zulässige Lepton-Kopplungsplätze, aber
erzwingt weder deren Matrixelemente noch eine nichtverschwindende
Determinantenphase. Der gemeinsame dreidimensionale Raum und die
vierdimensionale Feldstatistik folgen nicht aus dieser Randrechnung.
