# Native Ereignismomente aus dem tatsächlichen W-Tensor

## Verdict

**PASS für die endliche native Algebra; Korrektur des behaupteten Geltungsbereichs von \(349/120\).**

Der gepinnte Tensor
`outputs/TFPT_Gemischte_Quellenantwort/native_tensor.npz`
mit SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`
bestätigt exakt

\[
X^\dagger XF=480F,
\qquad
X^\dagger X^2F=916XF,
\qquad
\|X^2F\|^2=439680.
\]

Die Krylov-Untergrenze \(\dim\mathcal K(H,F)\ge 33\) ist ebenfalls exakt
belegt. Die Zahl \(\mathcal I_F=349/120\) gilt jedoch nur, wenn die allgemeine
Kinetik den Vektor \(XF\) als Eigenvektor erhält. Für allgemeine hermitesche
Matrizen \(h,\Omega\) kommt ein positiver Varianzterm hinzu. Sie ist daher
keine allgemeine Quellenanforderung, sobald nichtskalare räumliche Kinetik
zugelassen wird.

Der Checker arbeitet nur mit den 480 tatsächlichen, von null verschiedenen
W-Koeffizienten und deren sparsamen Folgezuständen. Er baut keine volle
Fockraummatrix auf. Normaler und `-OO`-Lauf liefern bytegleiches JSON und
jeweils `PASS` bei 505 exakten Kontrollen.

## 1. Direkte Vektoridentitäten

Mit

\[
v=XF,\qquad w=X^2F
\]

enthält \(v\) genau 480 Ein-Boson-/Zwei-Loch-Terme mit Koeffizienten
\(\pm1\), also \(\|v\|^2=480\). Für \(w\) entstehen 216480 rohe Wörter, die
zu 106560 gemischten und 1680 doppelten Bosonmonomen zusammenfallen. In der
normierten Boson-Focknorm ergibt das

\[
\|w\|^2=439680.
\]

Die direkte Anwendung von \(X^\dagger\), einschließlich des Faktors zwei
beim Ableiten eines Monoms \((b_A^\dagger)^2\), ergibt ohne Restkoeffizienten

\[
X^\dagger v=480F,
\qquad
X^\dagger w=916v.
\]

Damit ist insbesondere

\[
\beta_1^2=480|g|^2,
\qquad
\beta_2^2=916|g|^2
\]

für die skalare Kinetik bestätigt.

## 2. Explizites 33-dimensionales Krylov-Zertifikat

Sei \(Q_A\) die antisymmetrische 64-mal-64-Paarmatrix des Kanals \(A\).
Die besonders einfache tatsächliche Linearkombination

\[
Q_\Sigma=\sum_{A=0}^{59}Q_A
\]

hat exakt

\[
\det Q_\Sigma
=23283064365386962890625
=5^{32}.
\]

Insbesondere ist ihre Determinante modulo zwei gleich eins; der Betrag der
Pfaffschen Determinante ist \(5^{16}\). Die Kombination ist also
nichtentartet.

Setzt man im bosonischen Polynom \(X\) alle 60 Bosonvariablen gleich eins,
wird \(X\) auf den Paarannihilator zu \(Q_\Sigma\) abgebildet. Wegen der
nichtverschwindenden höchsten Pfaffform gilt

\[
X^mF\ne0\qquad (m=0,\ldots,32).
\]

Für den nativen Generator mit \(g\ne0\) ist der höchste Bosonzahlanteil von
\(H_c^mF\) gleich \(g^mX^mF\). Dieser Anteil kommt in keiner früheren Potenz
vor. Deshalb sind

\[
F,H_cF,\ldots,H_c^{32}F
\]

linear unabhängig und

\[
\dim\mathcal K(H_c,F)\ge33.
\]

Das ist eine Untergrenze. Es wurde keine einfache Fortsetzungsformel für
höhere Lanczos-Koeffizienten angenommen.

## 3. Momente: exakter skalarer Fall

Für

\[
H_c=\delta N_{\rm pair}+gX+\bar gX^\dagger
\]

folgen aus den geprüften Identitäten

\[
\mu_2=480|g|^2,
\qquad
\mu_3=480\delta|g|^2,
\]

\[
\mu_4=480\delta^2|g|^2+670080|g|^4,
\qquad
670080=480^2+439680.
\]

Damit ist

\[
\mathcal I_F
=\frac{\mu_2\mu_4-\mu_3^2}{\mu_2^3}
=\frac{670080}{480^2}
=\frac{349}{120}.
\]

Diese Aussage ist exakt, aber an die skalare Wirkung der Kinetik auf \(XF\)
gebunden.

## 4. Präzise Korrektur für allgemeine \(h,\Omega\)

Nach Abzug der Energie von \(F\) sei

\[
K=d\Gamma_f(h)-\operatorname{tr}(h)+d\Gamma_b(\Omega),
\qquad
H_c=K+gX+\bar gX^\dagger.
\]

Auf dem Ein-Boson-/Zwei-Loch-Sektor setze

\[
\widehat v=\frac{v}{\sqrt{480}},
\quad
\delta_{\rm eff}=\langle\widehat v,K\widehat v\rangle,
\quad
\sigma_K^2=\|(K-\delta_{\rm eff})\widehat v\|^2.
\]

Dann gilt

\[
H_c^2F=480|g|^2F+gKv+g^2w
\]

und daher

\[
\mu_3=480\delta_{\rm eff}|g|^2,
\]

\[
\mu_4
=670080|g|^4
+480(\delta_{\rm eff}^2+\sigma_K^2)|g|^2.
\]

Die beiden korrigierten Invarianten lauten somit

\[
\boxed{
\mathcal I_F
=\frac{349}{120}
+\frac{\sigma_K^2}{480|g|^2}}
\]

und

\[
\boxed{
\beta_2^2=916|g|^2+\sigma_K^2}.
\]

Weil \(K\) hermitesch ist, gilt \(\sigma_K^2=0\) genau dann, wenn

\[
KXF=\delta_{\rm eff}XF.
\]

In Paarmatrixnotation ist das die genaue Intertwinerbedingung. Schreibe

\[
P_A=\frac12\sum_{ij}(Q_A)_{ij}f_jf_i,
\qquad Q_A^T=-Q_A.
\]

Mit den im Checker verwendeten Indexkonventionen muss für jedes \(A\) gelten

\[
\boxed{
\sum_B\Omega_{AB}Q_B-h^TQ_A-Q_Ah
=\delta_{\rm eff}Q_A.}
\]

Äquivalent in der 60-mal-2016-Darstellung: Die Abweichung von
\(\Omega W-Wh^{(2)}\) von einem skalaren Vielfachen von \(W\) ist genau der
Beitrag, dessen normierte quadratische Länge \(\sigma_K^2\) liefert.

### Exaktes Gegenbeispiel innerhalb positiver Bosonkinetik

Setze

\[
h=\operatorname{diag}(1,0,\ldots,0),
\qquad
\Omega=I_{60}.
\]

Im tatsächlichen W-Tensor kommt Fermionmode null in 15 der 480 Wörter vor.
Auf diesen Wörtern ist der K-Eigenwert null, auf den übrigen 465 gleich eins.
Daraus folgen exakt

\[
\delta_{\rm eff}=\frac{31}{32},
\qquad
\sigma_K^2=\frac{31}{1024}>0.
\]

Für \(g=1\) wird deshalb

\[
\mathcal I_F=\frac{285907}{98304}
\ne\frac{349}{120},
\qquad
\beta_2^2=\frac{938015}{1024}\ne916.
\]

Damit ist am tatsächlichen W-Tensor entschieden: Eine allgemeine Matrixkinetik
behält \(349/120\) nur bei Erfüllung der obigen Intertwinerbedingung.

## 5. Korrigierte Kurzzeitordnungen

Für den nativen Generator bleibt die Amplitude

\[
\Pi_2e^{-itH_c}F
=-\frac{g^2t^2}{2}w+O(t^3).
\]

In der Wahrscheinlichkeit verschwindet aber der Term der Ordnung \(t^5\).
Der relevante Skalar ist eine Summe aus
\(\langle w,K_2w\rangle\) und
\(\langle X^\dagger w,K_1v\rangle
=916\langle v,K_1v\rangle\); beide sind reell. Daher lautet die scharfe
Ordnung

\[
\boxed{
\|\Pi_2e^{-itH_c}F\|^2
=109920|g|^4t^4+O(t^6).}
\]

Für die hermitesche Doppelumwandlung

\[
H_\eta=H_c+\eta X^2+\bar\eta X^{\dagger2}
\]

gilt allgemeiner

\[
\|\Pi_2e^{-itH_\eta}F\|^2
=439680|\eta|^2t^2
+439680\operatorname{Im}(\bar\eta g^2)t^3
+O(t^4).
\]

In der im Ausgangstext verwendeten reellen Phasenkonvention
\(g,\eta\in\mathbb R\) verschwindet auch der kubische Term:

\[
\boxed{
\|\Pi_2e^{-itH_\eta}F\|^2
=439680\eta^2t^2+O(t^4).}
\]

Die früheren Reste \(O(t^5)\) beziehungsweise \(O(t^3)\) waren als grobe
Schranken nicht falsch, aber in der reellen nativen Konvention nicht scharf.

## Reichweite

Bewiesen sind endliche algebraische Aussagen für den gepinnten nativen
W-Tensor. Sie zeigen eine notwendige Mehrschrittdynamik und korrigieren den
Geltungsbereich des Momenteninvarianten. Sie leiten weder \(h\), \(\Omega\),
\(g\) noch das elementare Ereignisgesetz aus P1/P2 oder aus einer gemeinsamen
Quelle her. Die TFPT-Gates T1 bis T8 bleiben offen.
