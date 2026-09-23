# Review: Kompression einer reinen CAR-Kovarianz und `PS.DIRAC.03`

**Datum:** 2026-09-21  
**Geltungsbereich:** endlicher komplexer CAR-Einteilchenraum \(\mathcal H\); orthogonale Projektion \(P\), \(Q=I-P\); selbstadjungierte Matrizen. Dies ist eine Prüfung der ersten linearen Brücke zwischen `v210_mark_local_dtn.py` und `v258_dirac_covariance_induction.py`, kein Abschluss von `PS.DIRAC.03` und keine Aussage über Yukawa-Herkunft, Typ-III-Netze, globale gemischte KMS-Zustände, KK-Theorie oder approximatives IR-Matching.

## Ergebnis

Die vier vorgegebenen Aussagen sind mit den unten genannten Voraussetzungen korrekt. Sie ergeben jedoch eine scharfe Alternative für die noch offene Identifikation

\[
C_F=P C_\Sigma P\big|_{P\mathcal H}.
\]

Ist \(C_\Sigma\) ein **reiner** Projektorzustand und \(C_F\) eine **treue** Fermi-Kovarianz \(0<C_F<I\), dann muss der ausgeschlossene Sektor mit dem Träger koppeln: \(Q C_\Sigma P\) ist injektiv. Soll gleichzeitig die von demselben Einteilchenoperator \(h\) erzeugte Zeitentwicklung auf \(P\mathcal H\) exakt autonom und unitär sein, muss dagegen \(QhP=0\) gelten. Ist \(C_\Sigma\) ein Spektralprojektor dieses selben \(h\), wird dann \(C_F\) selbst zum Projektor und kann keine treue endliche Fermi-Kovarianz mehr sein.

Das ist keine Widerlegung der Kompressionsidee. Es bestimmt, was eine Konstruktion liefern muss: Entweder ist der reduzierte Zustand treu und die komprimierte Zeitentwicklung besitzt Leckage beziehungsweise Gedächtnis, oder der Träger reduziert die volle Dynamik exakt und die komprimierte Kovarianz bleibt rein. Eine dritte Möglichkeit ist, eine der ausdrücklich verwendeten Voraussetzungen zu ändern, etwa eine global gemischte Kovarianz zu verwenden.

## 1. Defekt der komprimierten Projektion

Sei \(C=C^*=C^2\) und

\[
A:=C_F=PCP\big|_{P\mathcal H},\qquad B:=QCP:P\mathcal H\to Q\mathcal H.
\]

Der \(P\)-Block von \(C^2=C\) ist

\[
PCP=PCPCP+PCQCP.
\]

Damit gilt auf \(P\mathcal H\) exakt

\[
\boxed{\;C_F-C_F^2=(QCP)^\dagger(QCP)=B^\dagger B\;}.
\]

Vorzeichen und Adjungierung stimmen: \((QCP)^\dagger=PCQ\). Insbesondere ist der Nicht-Projektivitätsdefekt positiv.

Falls \(0<C_F<I\), ist \(C_F-C_F^2\) positiv definit. Also ist \(B^\dagger B\) invertierbar, \(B\) injektiv und

\[
\operatorname{rank}(QCP)=\dim(P\mathcal H).
\]

Das erzwingt zugleich \(\dim(Q\mathcal H)\geq\dim(P\mathcal H)\). Eine treue \(n\)-dimensionale Kompression eines reinen Zustands benötigt in dieser endlichen Darstellung somit mindestens \(n\) komplementäre Einteilchenrichtungen.

Für die in `v258` benutzte Konvention

\[
C_F=\left(I+e^{D/\mu}\right)^{-1},\qquad D=D^*,\quad 0<|\mu|<\infty,
\]

liefert der Spektralkalkül

\[
\boxed{\;C_F-C_F^2
=\frac{e^{D/\mu}}{(I+e^{D/\mu})^2}
=\frac{1}{4\cosh^2(D/(2\mu))}\;}.
\]

Dies ist daher genau das Gram-Objekt von \(QCP\). In einer Eigenrichtung \(D u=d u\) ist die zugehörige Singularzahl der notwendigen Purifikationskopplung

\[
s(d)=\frac{1}{2\cosh(d/(2\mu))}>0.
\]

Die Aussage ist analytisch exakt und nicht bloß numerisch.

## 2. Exakte Bedingung für Chiralitätsungeradheit

Auf \(P\mathcal H\) sei \(\gamma=\gamma^*=\gamma^{-1}\) eine festgelegte Graduierung und \(0<C_F<I\). Mit der tatsächlich in `v258` verwendeten Konvention

\[
K:=\operatorname{logit}_{v258}(C_F)
=\log\!\left((I-C_F)C_F^{-1}\right)
=\log(I-C_F)-\log C_F
\]

gilt

\[
\boxed{\;\gamma K\gamma=-K
\quad\Longleftrightarrow\quad
\gamma C_F\gamma=I-C_F\;}.
\]

**Hinrichtung.** Aus \(\gamma C_F\gamma=I-C_F\) und dem Funktionalkalkül folgt

\[
\gamma K\gamma
=\operatorname{logit}_{v258}(I-C_F)
=-\operatorname{logit}_{v258}(C_F).
\]

**Rückrichtung.** Die inverse Funktion ist \(C_F=(I+e^K)^{-1}\). Daher folgt aus \(\gamma K\gamma=-K\)

\[
\gamma C_F\gamma=(I+e^{-K})^{-1}=I-(I+e^K)^{-1}=I-C_F.
\]

Für die entgegengesetzte, ebenfalls gebräuchliche Logit-Konvention \(\log(C_F(I-C_F)^{-1})\) gilt dieselbe Äquivalenz; nur das Vorzeichen von \(K\) wechselt.

Diese Präzisierung korrigiert eine mögliche Überlesart von `v258`: Eine bloß „graduierte“ Kovarianz oder \([\gamma,C_F]=0\) macht den modularen Hamiltonian nicht ungerade. Bei \([\gamma,C_F]=0\) ist auch der Logit im Allgemeinen **gerade**. Benötigt wird die stärkere Komplementaritätsrelation \(\gamma C_F\gamma=I-C_F\). Das Skript erzeugt \(C_F\) bereits aus einem vorgegebenen ungeraden Dirac-Block; dadurch gilt die Relation automatisch, sie wird aber nicht aus einem unabhängigen \(C_\Sigma\) und \(P_F\) hergeleitet. Ein nachträgliches Projizieren des Logits auf seinen ungeraden Anteil erhält die exakte KMS-Inversion im Allgemeinen ebenfalls nicht.

## 3. Exakte autonome Zeitentwicklung

Sei \(h=h^*\) auf \(\mathcal H\) und

\[
U_P(t):=P e^{-ith}P\big|_{P\mathcal H}.
\]

Dann gilt

\[
\boxed{\;U_P(t)\text{ ist für alle }t\in\mathbb R
\text{ eine autonome unitäre Gruppe auf }P\mathcal H
\quad\Longleftrightarrow\quad QhP=0\;}.
\]

Ist \(QhP=0\), so ist wegen der Selbstadjungiertheit auch \(PhQ=0\). Der Raum \(P\mathcal H\) reduziert \(h\), und

\[
U_P(t)=e^{-it(PhP)|_{P\mathcal H}}.
\]

Umgekehrt sei \(U_P(t)\) für jedes \(t\) unitär. Für \(x\in P\mathcal H\) gilt durch orthogonale Zerlegung

\[
\|x\|^2=\|e^{-ith}x\|^2
=\|Pe^{-ith}x\|^2+\|Qe^{-ith}x\|^2.
\]

Die Unitarität von \(U_P(t)\) macht den ersten Term bereits zu \(\|x\|^2\); deshalb ist \(Qe^{-ith}P=0\) für alle \(t\). Ableiten bei \(t=0\) ergibt \(QhP=0\).

Der zugehörige infinitesimale Defekt lautet exakt

\[
\boxed{\;Ph^2P-(PhP)^2
=PhQhP
=(QhP)^\dagger(QhP)\;}.
\]

Sei nun \(C=\chi_\Delta(h)\) ein Spektralprojektor desselben \(h\); beim `v210`-Typ ist insbesondere

\[
C=\frac{I+\operatorname{sgn}(h)}2
\]

für ein bei null gegapptes \(h\). Aus \(QhP=0\) folgt, dass \(P\) mit jedem Spektralprojektor von \(h\) kommutiert. Somit

\[
(PCP)^2=PC^2P=PCP.
\]

Also ist \(C_F=PCP|_{P\mathcal H}\) ein Projektor. Sein Logit besitzt an den Eigenwerten \(0\) und \(1\) unendliche Grenzwerte und definiert keinen endlichen treuen modularen Diracoperator.

Die genaue No-go-Aussage lautet daher: Auf einem endlichen Einteilchenraum können nicht gleichzeitig

1. \(C\) ein reiner gegappter Spektralprojektor von \(h\),
2. \(Pe^{-ith}P\) für alle Zeiten eine exakt autonome unitäre Dynamik auf \(P\mathcal H\), und
3. \(PCP|_{P\mathcal H}=(I+e^{D/\mu})^{-1}\) mit endlichem \(D\) und \(0<C_F<I\)

gelten.

Ohne die zweite Voraussetzung ist eine treue gemischte Kompression eines reinen globalen Zustands völlig möglich; dann ist die reduzierte Dynamik aber nicht die Kompression einer geschlossenen autonomen unitären Gruppe. Ohne die erste Voraussetzung, etwa bei einem global gemischten KMS-Zustand, folgt die Projektivität ebenfalls nicht.

## 4. Volle Zeitprüfung: komprimierte Resolvente und Feshbach-Term

Schreibe \(h\) relativ zu \(\mathcal H=P\mathcal H\oplus Q\mathcal H\) als

\[
h=\begin{pmatrix}
A&B\\
B^*&D_Q
\end{pmatrix},
\qquad
A=PhP,\ B=PhQ,\ D_Q=QhQ.
\]

Für \(z\) so, dass \(z-D_Q\) und der folgende Schur-Komplement-Operator invertierbar sind, ergibt die Blockinversion

\[
\boxed{\;
P(z-h)^{-1}P\big|_{P\mathcal H}
=\left[z-h_{\mathrm{eff}}(z)\right]^{-1},
\;}
\]

mit

\[
\boxed{\;
h_{\mathrm{eff}}(z)
=PhP+PhQ\,(z-QhQ)^{-1}QhP.
\;}
\]

Das Pluszeichen im effektiven Operator ist korrekt: Der Schur-Komplement-Nenner von \(z-h\) ist

\[
z-PhP-PhQ(z-QhQ)^{-1}QhP
=z-h_{\mathrm{eff}}(z).
\]

Andere Feshbach-Schreibweisen können äußerlich ein Minuszeichen zeigen, wenn sie mit \(h-z\) oder \((QhQ-z)^{-1}\) beginnen; sie sind algebraisch äquivalent.

Die komprimierte Resolvente bestimmt die gesamte komprimierte Spektralmaß- und Zeitinformation. Im endlichen Fall kann \(Pe^{-ith}P\) durch Spektralinversion beziehungsweise eine Konturintegration der Resolvente rekonstruiert werden. Der energieabhängige Selbstenergieterm

\[
\Sigma(z)=PhQ(z-QhQ)^{-1}QhP

\]

ist deshalb die korrekte Größe für die volle Zeitprüfung. Nur \(PhP\) zu vergleichen prüft weder Leckage noch Gedächtniseffekte des ausgeschlossenen Sektors.

## Konsequenz für die vorhandene Brücke

- `v210_mark_local_dtn.py:98-103` baut mit \(C=(I+\operatorname{sgn}(h))/2\) einen reinen endlichen Projektorzustand.
- `v258_dirac_covariance_induction.py:65-76` prüft korrekt die gegenseitige Inversion zwischen einem **bereits vorgegebenen** endlichen \(D\) und \(C_F=(I+e^{D/\mu})^{-1}\).
- `v258_dirac_covariance_induction.py:149-155` konstruiert jedoch weder \(C_\Sigma\) noch \(P_F\); die Gleichung \(C_F=P_FC_\Sigma P_F\) wird dort ausdrücklich nur mit `check(..., True)` registriert.

Für eine tatsächliche Schließung von `PS.DIRAC.03` muss ein Kandidat \((C_\Sigma,P_F)\), mit \(Q=I-P_F\), daher mindestens die exakte Gram-Bedingung

\[
(Q C_\Sigma P_F)^\dagger(Q C_\Sigma P_F)
=\frac{1}{4\cosh^2(D_F/(2\mu))}
\]

und, für einen ungeraden induzierten Diracoperator, die Komplementarität

\[
\gamma_F(P_FC_\Sigma P_F)\gamma_F=I-P_FC_\Sigma P_F
\]

erfüllen. Wird zusätzlich behauptet, dass derselbe volle Generator \(h\) eine exakt autonome Trägerzeit erzeugt, ist außerdem \(QhP_F=0\) zu prüfen; bei einem reinen Spektralprojektor \(C_\Sigma=\chi_\Delta(h)\) wäre dies mit der treuen Fermi-Kovarianz unvereinbar. Falls \(QhP_F\neq0\), muss die Zeitbehauptung stattdessen über die komprimierte Resolvente und den Feshbach-Term formuliert werden.

**Verdict:** Die lineare Algebra liefert eine echte notwendige Schnittstelle, aber noch keine physische Herleitung des offenen Kompressionspfeils. Die exakte modulare Inversion in `v258` bleibt richtig. Ihre Anwendung auf den `v210`-artigen reinen Zustand verlangt eine explizite, vollrangige Purifikationskopplung und schließt bei demselben \(h\) eine zugleich exakt autonome komprimierte unitäre Zeit aus.
