# Bevorzugte Korrektur: vollständiges markiertes D4-Wörterbuch

21. September 2026 · exakter endlicher Transport · keine Repository-Änderung

## Korrigiertes Ergebnis

Der spätere Originalstand enthält bereits die richtige D4-Wirkung auf dem
Compiler-Familienraum:

\[
\Sigma=\operatorname{diag}(1,-1,-1),\qquad
T_A=\begin{pmatrix}0&1&0\\1&0&0\\2&-2&1\end{pmatrix},\qquad
G=T_A\Sigma
=\begin{pmatrix}0&-1&0\\1&0&0\\2&2&-1\end{pmatrix}.
\]

Sie erfüllt

\[
G^4=I,\qquad T_A^2=I,\qquad T_AGT_A=G^{-1}.
\]

Auf den drei `Q_+`-Eigenrichtungen fixiert G die Eigenwert-1-Linie mit
Charakter `-1` und dreht die von den Eigenwerten 2 und 3 aufgespannte Ebene.
Deshalb gilt ausdrücklich

\[
[G,Q_+]\ne0.
\]

Das ist kein Fehler, sondern der Kern der späteren v97/v98/v141-Darstellung.
Die frühere Diagnose, ein einfaches `Q_+` müsse mit der D4-Drehung kommutieren,
darf daher nicht auf den tatsächlichen Compiler angewendet werden.

Die vollständige endliche Brücke zum echten Viermarken-Residuenraum existiert.
Sie transportiert gleichzeitig die beiden D4-Generatoren, `Sigma`, den ganzen
Operator Q, seine wirklichen Teile `Q_+` und `Q_-`, alle daraus gebildeten Wörter
und die kanonische Residuenpaarung. Sie benötigt weder die falsche v69-Normalform
noch eine Umdeutung von `Sigma` zum zentralen Halbturn.

Die Brücke ist unter D4-Kovarianz allein zweiparametrig: Die Parameter enthalten
eine Gesamtskalierung und ein relatives Normierungsverhältnis zwischen der
eindimensionalen B-Richtung und der zweidimensionalen E-Struktur. Nimmt man
zusätzlich die bestehende integrale minimale-Index-Konvention und eine positive
integrale unimodulare Residuenform als Gitterprinzip an, bleibt dagegen genau eine
D4-Bahn bis auf Gesamtvorzeichen. Der unten verwendete ganzzahlige Vertreter ist
ein Repräsentant dieser Bahn. Diese zusätzliche algebraische Auswahl ist kein
P1-Resultat und keine physische Quellenauswahl.

Was weiterhin fehlt, ist die physische Auswahl dieses endlichen Wörterbuchs als
lokaler Hamilton-/Dirac-/Yukawaoperator derselben Quelle. Der finite Transport ist
ein markenkovariantes Modulwörterbuch, keine physische Zeitentwicklung.

## 1. Tatsächlicher Residuenraum

Auf

\[
F_4=\mathbb C^4,\qquad
U=\{x\in\mathbb C^4:\sum_a x_a=0\}
\]

verwenden wir die integrale Residuenbasis

\[
H=(e_0-e_3,\ e_1-e_3,\ e_2-e_3)
=\begin{pmatrix}
1&0&0\\0&1&0\\0&0&1\\-1&-1&-1
\end{pmatrix}.
\]

Die Vierteldrehung ist die zyklische Verschiebung der vier Marken. Die
geometrische Inversion fixiert die Marken 0 und 2 und vertauscht 1 mit 3. In der
H-Basis sind ihre induzierten Matrizen

\[
R_h=\begin{pmatrix}-1&-1&-1\\1&0&0\\0&1&0\end{pmatrix},\qquad
S_h=\begin{pmatrix}1&0&0\\-1&-1&-1\\0&0&1\end{pmatrix}.
\]

Sie erfüllen

\[
R_h^4=S_h^2=I,\qquad S_hR_hS_h=R_h^{-1}.
\]

Die Basis H ist nicht orthonormal. Ihre kanonische Residuenpaarung ist

\[
G_h=H^\dagger H
=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},
\]

und beide geometrischen Generatoren sind bezüglich dieser Form unitär.

## 2. Alle gleichzeitigen markierten Intertwiner

Gesucht ist eine einzige Matrix X, welche beide benannten Generatoren verbindet:

\[
XG=R_hX,\qquad XT_A=S_hX.
\]

Die vollständige Lösung ist zweidimensional:

\[
X(a,b)=
\begin{pmatrix}
-a-2b&-a-4b&b\\
a+2b&-a&-b\\
a+2b&a&b
\end{pmatrix},
\]

mit

\[
\det X(a,b)=4b(a+2b)^2.
\]

Ein besonders einfacher invertierbarer ganzzahliger Vertreter ist

\[
X=X(-1,1)
=\begin{pmatrix}-1&-3&1\\1&1&-1\\1&-1&1\end{pmatrix},
\qquad \det X=4.
\]

Mit `c=a+2b` zeigt die Skalierung besonders klar die verbleibende Freiheit:
Eine gemeinsame Multiplikation `(a,b)->lambda(a,b)` skaliert X insgesamt,
während das Verhältnis

\[
\rho=\frac{b}{a+2b}
\]

die relative B/E-Normierung bestimmt. Für einen invertierbaren Intertwiner gilt
`b != 0` und `a+2b != 0`. Die D4-Gleichungen bestimmen weder `rho` noch die
Gesamtskala.

Für ganzzahlige `a,b` ist auch `c=a+2b` ganzzahlig. Deshalb folgt aus

\[
|\det X|=4|b|c^2
\]

für jeden invertierbaren ganzzahligen Intertwiner `|det X|>=4`. Gleichheit gilt
genau für `|b|=|c|=1`. Die vier Parameterpaare

\[
(a,b)=(-1,1),\ (-3,1),\ (1,-1),\ (3,-1)
\]

bilden bis auf Gesamtvorzeichen und die zentrale Drehung `G^2` eine einzige Bahn:

\[
X(-3,1)=X(-1,1)G^2,\qquad
X(1,-1)=-X(-1,1),\qquad
X(3,-1)=-X(-3,1).
\]

Das Gesamtvorzeichen ist dabei eine getrennte Basisorientierungswahl; `-I` wird
nicht stillschweigend als Element der ursprünglichen D4-Gruppe gezählt.

Damit ist `X(-1,1)` unter der **zusätzlich übernommenen minimalen
Gitterindex-Konvention** ein kanonischer Bahnenvertreter. D4 allein liefert diese
diskrete Auswahl nicht.

v97 beweist für die **einzelne zyklische** Intertwinerbedingung eine minimale
Determinante 2. Hier werden gleichzeitig Rotation und die festgelegte Spiegelung in
der angegebenen H-Basis verlangt; die Lösungsfamilie hat minimale nichtverschwindende
ganzzahlige Determinante 4. Diese beiden Indexaussagen betreffen verschiedene
Gleichungssysteme. Ein weiterer Abgleich zwischen Quotientenhomologie- und
Residuenlattice wird hier nicht geraten oder als hergeleitet ausgegeben.

## 3. Die vollständige D4-Wirkung wird transportiert

Neben den beiden definierenden Gleichungen folgt

\[
X\Sigma=\Sigma_hX,\qquad
\Sigma_h=S_hR_h
=\begin{pmatrix}-1&-1&-1\\0&0&1\\0&1&0\end{pmatrix}.
\]

Damit bleiben die beiden späteren geometrischen Spiegelklassen erhalten:
`T_A` geht in die Inversion `S_h` über, `Sigma=T_AG` in `S_hR_h`. Es wird kein
Generator neu erfunden und keine vorhandene D4-Relation ersetzt.

Dies ist die genaue endliche Fortsetzung der bereits vorhandenen Ergebnisse:

- v97 konstruiert `T_A`, `G=T_A Sigma` und den zyklischen Index-Zeugen;
- v98 identifiziert `G` mit den Klassen `2,1,3` und trennt die beiden
  Spiegelklassen;
- v141 beweist, dass die Eigenwert-1-Linie von `Q_+` den Charakter 2 trägt und
  die Eigenwert-2/3-Ebene die konjugierten Charaktere 1 und 3;
- v146 realisiert die volle Möbius-D4-Wirkung geometrisch, lässt aber die
  physische Herkunftsbehauptung `Generation = H_1` bedingt.

Die hier ergänzte Aussage ist enger: Derselbe Intertwiner trägt zusätzlich den
**vollständigen tatsächlichen Q-Operator samt seinem `Sigma`-Split** in den
konkreten Residuenrahmen.

## 4. Transport des wirklichen Q-Paars

Aus

\[
Q=\begin{pmatrix}3&1&0\\3&2&0\\3&2&1\end{pmatrix},\qquad
Q_\pm=\frac12(Q\pm\Sigma Q\Sigma)
\]

entstehen

\[
Q_h=XQX^{-1}
=\begin{pmatrix}2&-3&-4\\0&2&1\\-1&0&2\end{pmatrix},
\]

\[
A_h=XQ_+X^{-1}
=\frac12\begin{pmatrix}3&-1&-2\\1&5&2\\-1&1&4\end{pmatrix},
\]

\[
B_h=XQ_-X^{-1}
=\frac12\begin{pmatrix}1&-5&-6\\-1&-1&0\\-1&-1&0\end{pmatrix}.
\]

Exakt gelten

\[
Q_h=A_h+B_h,
\]

\[
A_h=\frac12(Q_h+\Sigma_hQ_h\Sigma_h),\qquad
B_h=\frac12(Q_h-\Sigma_hQ_h\Sigma_h).
\]

Die charakteristischen Polynome bleiben

\[
\chi_{A_h}(t)=(t-1)(t-2)(t-3),\qquad
\chi_{B_h}(t)=t(t^2-3).
\]

Entscheidend ist, dass nicht nur diese Einzelspektren transportiert werden. Für
jeden nichtkommutativen Ausdruck W gilt

\[
XW(Q_+,Q_-)X^{-1}=W(A_h,B_h).
\]

Insbesondere werden alle drei Spektralprojektoren von `Q_+` und die gerichteten
Blöcke `P_aQ_-P_b` erhalten. Ein vollständiger Siebenerzeuge-Zeuge besteht aus
den drei Projektoren sowie den vier nichtverschwindenden gerichteten
Projektorwörtern. Seine lineare Dimension bleibt 7. Damit bleibt gerade der in der
separaten v69-Normalform verlorene gerichtete Block erhalten.

## 5. Transportierte Residuenpaarung

Die kanonische H-Paarung zieht sich auf den Compilerraum zurück zu

\[
G_{\rm gen}=X^\dagger G_hX
=\begin{pmatrix}4&0&0\\0&20&-8\\0&-8&4\end{pmatrix}.
\]

Alle reellen symmetrischen Formen, die gleichzeitig unter `G` und `T_A`
invariant sind, haben exakt die Gestalt

\[
M(u,v)=
\begin{pmatrix}
u&0&0\\
0&u+4v&-2v\\
0&-2v&v
\end{pmatrix},
\qquad \det M(u,v)=u^2v.
\]

Sie sind positiv definit genau für `u>0` und `v>0`. Ist die Form zusätzlich
integral und unimodular, dann sind `u=M_11` und `v=M_33` positive ganze Zahlen
mit `u^2 v=1`. Folglich gilt eindeutig

\[
u=v=1,\qquad
M_0=M(1,1)=
\begin{pmatrix}1&0&0\\0&5&-2\\0&-2&1\end{pmatrix}.
\]

Der minimale ganzzahlige Vertreter und alle vier Vertreter seiner oben
beschriebenen Bahn induzieren dieselbe Form

\[
X^\dagger G_hX=4M_0.
\]

Die Eindeutigkeit ist daher exakt, aber bedingt: **D4 plus positive integrale
Unimodularität plus minimale-Index-Konvention** wählen die eine Gitterbahn. D4
allein tut das nicht.

Für die ganze reelle Zweiparameterfamilie lautet die induzierte Form exakt

\[
G_{\rm gen}(a,b)=4
\begin{pmatrix}
(a+2b)^2&0&0\\
0&(a+2b)^2+4b^2&-2b^2\\
0&-2b^2&b^2
\end{pmatrix}.
\]

Ihre Determinante ist

\[
\det G_{\rm gen}(a,b)=64b^2(a+2b)^4>0
\]

für jeden reellen invertierbaren X. Nach Ausklammern der Gesamtskala
`4(a+2b)^2` hängt die Form nur noch von `rho^2` ab. Die D4-Gleichungen lassen
dieses Verhältnis kontinuierlich frei. Das zusätzliche Gitterprinzip setzt
`rho^2=1` und reduziert die Freiheit auf die obige diskrete Bahn.

Das wirkt sich bereits auf die kanonisch normierte Vertexmatrix aus. In der
ursprünglichen `Q_+`-Eigenbasis V gilt mit `c=a+2b`

\[
V^\dagger G_{\rm gen}(a,b)V
=4\operatorname{diag}(c^2,c^2,b^2).
\]

Für positive reelle c und b ist der Orthonormalisierungstransport daher, bis auf
den irrelevanten gemeinsamen Faktor 2, `D=diag(c,c,b)`. Auf den tatsächlichen
ungeraden Operator

\[
B=\begin{pmatrix}0&1&0\\3&0&0\\-3&0&0\end{pmatrix}
\]

wirkt er als

\[
B_{\rm can}=DBD^{-1}
=\begin{pmatrix}
0&1&0\\3&0&0\\-3b/c&0&0
\end{pmatrix}.
\]

Die Singulärwerte sind exakt

\[
\left\{1,\ 3\sqrt{1+(b/c)^2},\ 0\right\}.
\]

Damit ist die D4-Restfreiheit operational sichtbar. Unter der zusätzlichen
minimalen Gitterwahl wird daraus `{1,3 sqrt(2),0}`. Auch diese diskrete
Normauswahl macht `B_can` nicht zu einem aus P1 gewählten physischen Vertex; sie
ist die Normierungsfolge derselben endlichen Intertwinerfamilie.

Die Form `G_gen` ist positiv definit und erfüllt

\[
G^\dagger G_{\rm gen}G=G_{\rm gen},\qquad
T_A^\dagger G_{\rm gen}T_A=G_{\rm gen},\qquad
\Sigma^\dagger G_{\rm gen}\Sigma=G_{\rm gen}.
\]

Das ist die exakt transportierte **kanonische endliche Residuenpaarung** der
gewählten H-Basis. Sie ist kein aus P1 hergeleitetes physisches Einteilchenmaß und
keine lokale Feldmetrik. Insbesondere folgt daraus weiterhin nicht, dass `Q_+` und
`Q_-` zwei selbstadjungierte Observablen desselben physischen Hilbertraums sind.

Vor allem ist `M_0` nicht automatisch der geometrische Viermarken-Greenkern. Für
den vorhandenen zirkulanten Kern mit Diagonale `d`, Nachbareinträgen `-ell/2` und
Gegenüber-Einträgen `-ell`,

\[
K_4(d,\ell)=
\begin{pmatrix}
d&-\ell/2&-\ell&-\ell/2\\
-\ell/2&d&-\ell/2&-\ell\\
-\ell&-\ell/2&d&-\ell/2\\
-\ell/2&-\ell&-\ell/2&d
\end{pmatrix},
\]

haben die B- und E-Anteile die Eigenwerte `d` beziehungsweise `d+ell`. Exakt gilt

\[
X_0^\dagger H^\dagger K_4(d,\ell)HX_0
=4M(d+\ell,d).
\]

Für `ell>0` ist diese Form bei keinem endlichen `d` proportional zu `M_0`: Der
untere rechte Eintrag würde den Proportionalitätsfaktor auf `d` setzen, der obere
linke verlangt dagegen `d+ell`. Der Quellenaudit muss deshalb den tatsächlichen
`K_source` bestimmen. `M_0` ist die kanonische Residuen-Norm unter dem genannten
Gitterprinzip, kein vorgeschriebener Kovarianzwert.

## 6. Einordnung der früheren Diagnose

Die separate v69-Konstruktion

\[
A_{69}=\operatorname{diag}(1,2,3),\qquad
B_{69}=\begin{pmatrix}0&0&0\\0&0&\sqrt3\\0&\sqrt3&0\end{pmatrix}
\]

hat dieselben Einzelspektren wie das v50-Paar, aber nicht dieselbe gemeinsame
Wortalgebra. Sie darf nicht als Ersatz für den vollständigen Q-Transport verwendet
werden. Dieser enge Gegenbefund bleibt gültig.

Sogar die ganze zweiparametrige Büscheldeterminante ist identisch:

\[
\det(zI-A-tB)
=(z-1)\bigl((z-3)(z-2)-3t^2\bigr)
=\det(zI-A_{69}-tB_{69}).
\]

Gerade deshalb ist der gerichtete Projektorblock beziehungsweise die Dimension
der gemeinsamen Wortalgebra der entscheidende stärkere Test. Spektren und die
vollständige Büscheldeterminante allein liefern keine simultane Ähnlichkeit.

Die zuvor angegebene Halbturn-Lesart `Sigma=r^2` kann A als
orientierungsgebrochene C4-Konstruktion darstellen. Sie wird jetzt nur noch als
Diagnose dafür aufbewahrt, warum die falsche kommutierende Normalform attraktiv
wirkte. Sie ersetzt weder `G,T_A,Sigma` noch den obigen Intertwiner.

Auch die exakte zweiseitige Vertex-Äquivalenz zur symmetrischen v69-Form bleibt nur
ein Diagnosewerkzeug. Ihr Frequenzfaktor `LR=I-E_32` zeigt, warum der
Spektrenvergleich ohne gemeinsames Modul unvollständig war. Der bevorzugte Weg ist
die echte Ähnlichkeit `XQX^{-1}` im vollständigen markierten D4-Wörterbuch.

## 7. Familienantwort-Gate nach der Korrektur

Die richtige Symmetrieaussage lautet nun:

- Ein **D4-invarianter hermitescher Antwortoperator** auf dem geometrischen
  Augmentationsraum `U=B1+E` besitzt höchstens ein `1+2`-Spektrum.
- Der Compileroperator `Q_+` ist jedoch nicht D4-invariant und muss diese
  Entartung nicht besitzen. Sein einfaches Spektrum widerspricht der tatsächlichen
  späteren D4-Wirkung nicht.
- Daraus folgt noch keine physische Auswahl von `Q_+` als Hamilton-/Diracoperator.

Unabhängig davon bleibt der All-orders-Satz für die vorhandene native Bank bestehen.
Auf demselben unveränderten `H_W` und dem Spin(10)×SU(4)-Singulettzustand `Omega`
faktorisiert der Antikommutator-Antwortraum als

\[
\mathbb C^{64}\otimes\mathcal K_{\rm resp},\qquad
\mathcal L=I_{64}\otimes J.
\]

Eine exakte Feshbach-Elimination auf die drei Residuenfamilien bleibt daher skalar,
und ein konstanter nichtorthogonaler Feldrahmen erzeugt nur ein Gram, das bei
kanonischer CAR-Normierung verschwindet. Mehr Genauigkeit in derselben skalaren
Memory-Kette erzeugt keine ungleichen Flavorpole.

Ein positiver physischer Herkunftsbeweis muss zusätzlich zeigen:

1. warum das minimale integrale Gitterprinzip physisch auf genau diesen
   Familienraum anzuwenden ist und warum diese endliche Modulabbildung die
   Generationen aus der Quelle beschreibt;
2. welcher Zustand und welche Zeitentwicklung dazu gehören;
3. welcher rohe Quellenkern `K_source` gilt und wo ein nichtskalarer
   Familienanteil in der damit kanonisch normierten inversen
   Zweipunktfunktion entsteht;
4. dass dieser Anteil ohne Zielmassen oder Ziel-Yukawamatrix konstruiert wurde;
5. dass Komplement-Memory und alle Grams vollständig mitgeführt wurden.

Der kleinste akzeptable dynamische Zeuge bleibt eine quellenberechnete
familiennichtskalare Selbstenergie oder ein quellengewählter Hamilton-/Diracterm,
der nach exakter Elimination und Normierung tatsächlich verschiedene Pole besitzt.

## 8. Physischer Status

Der native Hamiltonoperator

\[
H_W=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A)
\]

enthält den W-Tensor, aber keinen der Compileroperatoren `Q,R,K,L` als ausgewählten
physischen Familien-Hamiltonterm. Die endliche markierte Brücke verbessert die
Darstellungszuordnung; sie schließt nicht den offenen Vorwärtspfeil von der
ursprünglichen Quelle zu einem lokalen Dirac-/Yukawaoperator.

Die vorhandenen arithmetischen Flavorverhältnisse bleiben unverändert. Das offene
Gate ist ihre physische Realisierung in `H` beziehungsweise in einer aus derselben
Quelle berechneten Kovarianz/Selbstenergie. Dimensionsgleichheit, Moduläquivalenz
und exakte Operatortransportierbarkeit wählen diesen physischen Pfeil nicht allein.
Insbesondere beweist die endliche D4-Modulabbildung samt eindeutiger minimaler
Gitterbahn nicht die physische Herkunftsaussage `Generation = H_1`; diese bleibt
an den fehlenden Quellenpfeil gebunden.

## Reproduktion und Verdict

`checker.py` prüft mit exakter SymPy-Arithmetik und expliziten `if/raise`-Gates:

- die Viermarken-Permutationsdarstellung und die induzierten Matrizen `R_h,S_h`;
- die vollständige Zweiparameterlösung der beiden Intertwinerbedingungen;
- die Klassifikation aller invarianten reellen Gramformen und die eindeutige
  positive integrale unimodulare Form `M_0`;
- die eine minimale ganzzahlige D4-Bahn mit Determinante 4;
- den Transport von `G,T_A,Sigma,Q,Q_+,Q_-`;
- die kanonische Residuenpaarung, ihre Trennung vom Viermarken-Greenkern und alle
  drei Unitaritätsidentitäten;
- die Spektralprojektoren und den siebendimensionalen gerichteten Wortzeugen;
- die trotz Nichtäquivalenz identische symbolische Büscheldeterminante beider Paare;
- separat die enge v69-Nichtäquivalenz und die früheren Diagnosen;
- das weiterhin gültige Normierungs-Gate für konstante Familienrahmen.

**Verdict:** `EXACT` für das vollständige endliche markiert-kovariante Wörterbuch
und `EXACT unter den genannten zusätzlichen Gitterbedingungen` für seine eine
minimale integrale Bahn; `PARTIAL` für die physische Herkunftsfrage und die
Auswahl des tatsächlichen Quellenkerns; `REFUTED` nur für die Behauptung, das
separat gebaute v69-Paar sei bereits die gemeinsame Darstellung des tatsächlichen
v50-Paars. Die späteren gültigen Originalresultate v97/v98/v141/v146 werden bewahrt.
Kein T1-T8-Gate wird dadurch geschlossen.
