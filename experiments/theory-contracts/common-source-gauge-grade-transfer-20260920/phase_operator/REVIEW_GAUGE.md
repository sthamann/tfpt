# Unabhängige Prüfung der Gauge-Section-Konstruktion

**Prüfurteil:** `PASS_EXACT_WITH_SCOPE__AUXILIARY_COFRAME_REPAIRS_POSITIVITY_BY_CHANGING_THE_10D_LIFTS`

Geprüft wurden:

- `/Users/stefanhamann/Documents/Codex/2026-09-19/h/work/common_source_20260920/joint/GAUGE_SECTION.md`
  (`sha256 0a7b4186dd11f5b804c69aedd43cd255b327de7c10ee6efc33027f7af9611299`),
- `/Users/stefanhamann/Documents/Codex/2026-09-19/h/work/common_source_20260920/joint/check_gauge_section.py`
  (`sha256 8577bb632ec00a5508ef94deca3375a6defed9c88ae5c680963cecb36affd22f`),
- der vom Checker gelesene alte E8-Stand
  `outputs/TFPT_Drei_Wege_2026-09-20/e8/RESULTS.json`
  (`sha256 5515bba670727a645da566957c8603637a20e21147cfd83197216465ed0220b8`),
- die fest gepinnte native Clockquelle
  `compiler-integral-triality-20260918/certificate.json`
  (`sha256 a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3`).

Normaler Lauf und `python3 -OO check_gauge_section.py` bestanden jeweils dieselben 47 von 47 Prüfungen. Beide erzeugten byte-identisch
`gauge_section.json` mit
`sha256 336ce4046c77864260f1a734df5fb2809aaa342b7c27898af8e3f1b0430e39c8`.

## 1. Der alte Positivitätskonflikt ist korrekt

Im alten Split wirken die festgelegten zehn-dimensionalen Clocks als

\[
S_A=W_{\rm alt}\,\operatorname{diag}(B^{-1}AB,I_2)\,W_{\rm alt}^{-1}.
\]

Die gemeinsame $C/J$-invariante reelle symmetrische Form ist vollständig von der Gestalt

\[
V=W_{\rm alt}^{-T}\operatorname{diag}
\left(tG_{E8},\begin{pmatrix}b&c\\c&d\end{pmatrix}\right)W_{\rm alt}^{-1}.
\]

Die Vollständigkeit dieser Form ist konsistent mit dem alten exakten Befund: Der gemeinsame invariante symmetrische Raum im E8-Block ist eindimensional; der Paarblock ist frei. Kreuzblöcke können nicht auftreten, weil schon die Coxeter-Matrix keinen Fixvektor besitzt.

Der zusätzliche ursprüngliche Farbtausch $P_{12}$ erzwingt exakt

\[
t=-c-d,\qquad b=-2c-d.
\]

Für jede solche Form ergibt die direkte symbolische Rechnung

\[
n^T V n=0.
\]

Da $n\neq0$, ist keine dieser Formen positiv definit. Der Schluss ist daher gültig:

> Die alten **festen 10D-Lifts**, der rohe Farbtausch und eine positive definite gemeinsame Energieform sind miteinander unvereinbar.

Das ist ein bedingter Darstellungs-No-Go. Es betrifft weder E8 selbst noch andere 10D-Lifts, andere Komplemente oder eine nur semidefinite Form.

## 2. Die Hilfsachsen-Reparatur ist algebraisch tragfähig

Mit

\[
e=-e_9,\qquad v=n+e_9
\]

liefert der Checker eine ganzzahlige unimodulare Koframe $W_{\rm aux}$ mit

\[
\det W_{\rm aux}=-1,\qquad
W_{\rm aux}^T K W_{\rm aux}=G_{E8}\oplus\operatorname{diag}(1,-1).
\]

Für

\[
V_{\rm aux}=K+2Kvv^TK
\]

gilt exakt

\[
W_{\rm aux}^T V_{\rm aux}W_{\rm aux}
=G_{E8}\oplus I_2.
\]

Damit ist $V_{\rm aux}$ positiv definit. Die direkte Rechnung bestätigt außerdem seine Invarianz unter den erzeugenden Vertauschungen der drei Farb-, zwei schwachen und drei Familienkoordinaten. Wegen Linearität reicht die Prüfung der acht E8-Basisvektoren aus, um die erhaltene Hyperladungsabbildung auf der ganzen E8-Sektion festzulegen.

Die Eindeutigkeit ist korrekt eng formuliert: Unter den neun vorhandenen vorzeichenrichtig gewählten positiven Koordinatenachsen überlebt nur Achse 9. Es ist keine Klassifikation aller ganzzahligen oder reellen Komplemente.

## 3. Unveränderte 8D-Clocks, geänderte 10D-Wirkung

Die nativen acht-dimensionalen Matrizen $C$ und $J$ werden nicht verändert. Auch ihre E8-Basismatrizen $B^{-1}CB$ und $B^{-1}JB$ bleiben dieselben. Geändert wird die Einbettung in den zehn-dimensionalen Raum:

\[
S_{A,{\rm aux}}=W_{\rm aux}\operatorname{diag}(B^{-1}AB,I_2)W_{\rm aux}^{-1}.
\]

Die neuen $S_C,S_J$ sind ganzzahlig und unimodular, fixieren $n$, erhalten $K$ und $V_{\rm aux}$ und unterscheiden sich beide von den alten vollständigen Lifts. Die unabhängige Zusatzprüfung ergibt:

- $S_C$ hat weiterhin exakte Ordnung 30;
- $S_J$ hat weiterhin exakte Ordnung 4;
- $S_C^{15}=S_J^2$ bleibt auf Vektorebene exakt erhalten.

Damit ist die Reparatur keine bloße Umbenennung der alten mikroskopischen Clockwirkung. Sie ersetzt genau die zuvor konfliktbehaftete 10D-Realisierung, während die 8D-E8-Clocks fest bleiben.

## 4. Ladungsaussage und notwendige Grenze

Für die gewählte Markierung

\[
Y_{10}=(-1/3,-1/3,-1/3,1/2,1/2,0,0,0,1,1)^T
\]

werden die Aussagen

\[
Y_{10}\cdot n=0,\qquad
Y_{10}\cdot F_{\rm aux}(p)=Y_8\cdot p,\qquad
Y_{10}\cdot e=-1,\quad Y_{10}\cdot v=+1
\]

exakt bestätigt. Das Zusatzpaar besitzt also in dieser Koframe die kinematischen vorzeichenbehafteten Ladungen eines Singulettpaares, und die einfachen Farb-/schwachen Wurzeln bleiben unangezogen.

Die neuen vollständigen Clocks erhalten diese feste Hyperladungsmarkierung jedoch **nicht**:

\[
S_C^T Y_{10}\neq Y_{10},\qquad S_J^T Y_{10}\neq Y_{10}.
\]

„Ladung und Clocks auf derselben Sektion“ bedeutet daher gemeinsame Darstellung und konsistente Buchhaltung, nicht eine ladungserhaltende interne Clock-Symmetrie. Diese Grenze sollte in der Hauptdarstellung ausdrücklich stehen. Der alte Befund, dass die Clock eine feste U(1)-Markierung mitdreht, wird durch die neue Koframe nicht aufgehoben.

Aus den Paarladungen folgen außerdem weder Lepton-Feldstatistik noch ein Yukawa-Operator, ein Matrixelement, eine Determinantenphase oder eine CP-Phase. Es gibt weiterhin keine Abbildung dieser Koframe-Phase auf $a_0$.

## 5. Reproduzierbarkeitskorrektur

Die native Clockquelle ist im Checker gegen einen festen erwarteten Hash geprüft. Der alte `RESULTS.json`-Stand wird dagegen nur eingelesen und sein **aktueller** Hash in die Ausgabe geschrieben. Eine Veränderung dieser Datei würde deshalb nicht am Eingang scheitern.

Das ist kein Fehler der jetzt nachgerechneten Algebra, aber eine reale Provenienzlücke. Der Checker sollte den erwarteten Hash

`5515bba670727a645da566957c8603637a20e21147cfd83197216465ed0220b8`

fest hinterlegen und vor der Rechnung prüfen.

## 6. Endgültiger Scope

Die Konstruktion beweist exakt eine bedingte Kompatibilitätsverbesserung im gewählten $(9,1)$-Randmodell:

- E8-Gitter und ursprüngliche SM-/Familienmarkierung können mit einer blockpermutationssymmetrischen positiven Energieform zusammengeführt werden;
- die nativen 8D-Clocks bleiben erhalten;
- dafür müssen ihre vollständigen 10D-Lifts geändert werden;
- das Zusatzpaar trägt in der gewählten Markierung die Ladungen $(-1,+1)$.

Nicht hergeleitet sind die Randquelle aus P1/P2, die physische Auswahl dieser Koframe und Energieform, ein vollständiger gemischter Clock-/Cocycle-Lift, eine ladungserhaltende Zeitentwicklung, Yukawas, eine Phase, 3+1D-Feldstatistik oder ein T1–T8-Abschluss.
