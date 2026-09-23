# Review: exakter Drei-Familien-Reduktionssektor im nativen RR–\(W\)-Modell

**Datum:** 2026-09-21  
**Scope:** endliches natives Einteilchendiagramm und dessen CAR/CCR-Fockdarstellung. Geprüft wird nur, ob der globale Residuen-Unterraum \(U=u^\perp\subset F_4\) einen echten reduzierenden Sektor des bereits vorhandenen Hamiltonoperators bestimmt. Daraus folgt weder eine physische Auswahl dieses Sektors noch ein TOE-, 4D-, Lokalitäts- oder Quellenabschluss.

## Urteil

Die vorgeschlagene Reduktion ist mathematisch korrekt, unter den unten präzisierten Fockraum- und Definitionsannahmen:

\[
[Z,H]=0,
\]

und

\[
\ker Z
=\mathcal F_{\rm CAR}(S_+\otimes U)
\otimes
\mathcal F_{\rm CCR}(V_{10}\otimes\Lambda^2U).
\]

Die angegebenen Zahlen \(48\) und \(30\) sind die **Einteilchendimensionen**, nicht die Dimensionen der Fockräume:

\[
\dim(S_+\otimes U)=16\cdot3=48,
\qquad
\dim(V_{10}\otimes\Lambda^2U)=10\cdot3=30.
\]

Der CAR-Fockraum ist endlichdimensional, der CCR-Fockraum bleibt unendlichdimensional. Die Einschränkung von \(H\) auf \(\ker Z\) benutzt dieselben Parameter \(g,\Delta\) und den wörtlich eingeschränkten Tensor \(W\); sie ist keine Schur-, Feshbach- oder nichtlineare Kompression.

Der Befund ist jedoch **nicht derselbe Grundzustandszweig**. Für den bereits bewiesenen schwach gekoppelten eindeutigen \(\operatorname{Spin}(10)\times SU(4)\)-Singulettgrundzustand \(\Omega\) im Sektor \(Q=64\) gilt exakt

\[
Z\Omega=16\Omega.
\]

Damit ist \(\Omega\perp\ker Z\). Der neue Raum ist ein vorhandener, exakt reduzierender Null-\(Z\)-Sektor des nativen Modells; er ist keine Herleitung, dass die physische Quelle gerade diesen Sektor präpariert.

## 1. Einteilchenzerlegung

Setze

\[
F_4=\mathbb C u\oplus U,
\qquad
u=\frac12(1,1,1,1),
\qquad
p_0=|u\rangle\langle u|,
\qquad
U=u^\perp.
\]

Der Fermionraum und der Bosonraum des gepinnten nativen Tensors sind

\[
\mathcal F_1=S_+\otimes F_4,
\qquad
\mathcal B_1=V_{10}\otimes\Lambda^2F_4.
\]

Die äußere Zweierdarstellung des Rang-eins-Projektors ist

\[
d\Gamma_2(p_0)(x\wedge y)=p_0x\wedge y+x\wedge p_0y.
\]

Aus

\[
\Lambda^2F_4
=\Lambda^2U\oplus(u\wedge U)
\]

folgt

\[
d\Gamma_2(p_0)|_{\Lambda^2U}=0,
\qquad
d\Gamma_2(p_0)|_{u\wedge U}=I.
\]

Damit ist \(d\Gamma_2(p_0)\) selbst ein orthogonaler Projektor:

\[
\ker d\Gamma_2(p_0)=\Lambda^2U,
\qquad
\operatorname{im}d\Gamma_2(p_0)=u\wedge U.
\]

Definiere auf den Einteilchenräumen

\[
A_0=I_{16}\otimes p_0,
\qquad
B_0=I_{10}\otimes d\Gamma_2(p_0).
\]

Beide sind orthogonale Projektionen. Sie zählen genau die uniforme Familienrichtung bei Fermionen beziehungsweise den Bosonkanal \(u\wedge U\).

## 2. Warum \([Z,H]=0\) exakt gilt

Der vorhandene Vertrag `rr-continuous-clock-20260921` prüft für jedes \(k\in\mathfrak{gl}_4\) die volle Intertwineridentität

\[
W\,d\Gamma_2(I_{16}\otimes k)
=\bigl(I_{10}\otimes d\Gamma_2(k)\bigr)W.
\]

Man darf daher \(k=p_0\) einsetzen. Es folgt

\[
\boxed{\;W\,d\Gamma_2(A_0)=B_0W.\;}
\]

Auf dem vollen Fockraum sei

\[
Z=d\Gamma_{\rm CAR}(A_0)+d\Gamma_{\rm CCR}(B_0)
=f^\dagger A_0f+b^\dagger B_0b.
\]

Für den Paarvernichtervektor \(P=W(ff)\) lauten die entsprechenden Kommutatoren

\[
[Z_f,P]=-B_0P,
\qquad
[Z_b,b^\dagger]=b^\dagger B_0.
\]

Deshalb heben sich in jedem Summanden die beiden Beiträge auf:

\[
[Z,b^\dagger P]=0,
\qquad
[Z,P^\dagger b]=0.
\]

Außerdem kommutiert \(Z\) mit \(N_b\). Für

\[
H=\Delta N_b+g(b^\dagger P+P^\dagger b)
\]

folgt somit auf dem algebraischen endlichen Teilchenkern

\[
\boxed{[Z,H]=0.}
\]

### Operatorbereich

Der Fermionanteil ist beschränkt. Der Bosonanteil von \(Z\) ist ein Teilchenzahloperator. Die Wechselwirkung ist eine endliche Summe linearer Boson-Erzeuger/-Vernichter mit beschränkten fermionischen Koeffizienten und ist relativ zu \(N_b\) mit relativer Schranke null. Für \(\Delta>0\) besitzt \(H\) daher die übliche selbstadjungierte Realisierung auf der Zahloperatordomäne; der endliche Teilchenkern ist invariant. Alternativ genügt die bereits verwendete sektorweise Lesart: In jedem festen

\[
Q=N_f+2N_b
\]

ist der Raum endlichdimensional, und die Intertwineridentität zeigt dort direkt, dass jeder \(Z\)-Eigenraum erhalten wird. Damit kommutieren auch die Spektralprojektionen von \(Z\) mit der Dynamik.

## 3. Der Kern von \(Z\)

Da \(A_0,B_0\ge0\), ist

\[
Z\ge0.
\]

Die Fockfunktoren faktorisieren über orthogonale Summen. Auf der Fermionseite gilt

\[
\mathcal F_{\rm CAR}(S_+\otimes F_4)
\cong
\mathcal F_{\rm CAR}(S_+\otimes U)
\otimes
\mathcal F_{\rm CAR}(S_+\otimes\mathbb Cu),
\]

und \(d\Gamma_{\rm CAR}(A_0)\) zählt die Teilchen im zweiten Faktor. Auf der Bosonseite gilt

\[
\mathcal F_{\rm CCR}(V_{10}\otimes\Lambda^2F_4)
\cong
\mathcal F_{\rm CCR}(V_{10}\otimes\Lambda^2U)
\otimes
\mathcal F_{\rm CCR}(V_{10}\otimes(u\wedge U)),
\]

und \(d\Gamma_{\rm CCR}(B_0)\) zählt die Bosonen im zweiten Faktor. Weil beide Summanden von \(Z\) nichtnegativ sind, liegt ein Vektor genau dann in \(\ker Z\), wenn beide gezählten Faktoren im Vakuum stehen. Daher

\[
\boxed{\;
\ker Z
=\mathcal F_{\rm CAR}(S_+\otimes U)
\otimes
\mathcal F_{\rm CCR}(V_{10}\otimes\Lambda^2U).
\;}
\]

Da \([Z,H]=0\), ist dieser Kern ein reduzierender Unterraum. Die Familienkeilung im vorhandenen Tensor bildet zwei Fermionen aus \(S_+\otimes U\) direkt in \(V_{10}\otimes\Lambda^2U\) ab. Folglich ist

\[
H|_{\ker Z}
=\Delta N_b^{(30)}
+g\bigl(b_U^\dagger W_U f_Uf_U+\mathrm{h.c.}\bigr),
\]

wobei \(W_U\) die wörtliche Einschränkung des vorhandenen \(W\) ist. Es entstehen weder energieabhängige Selbstenergien noch zusätzliche Mehrkörperterme, weil kein gekoppelter Sektor eliminiert wird: Der Null-\(Z\)-Raum ist bereits exakt invariant.

## 4. Zentralanteil, SU(4)-Ladung und der bekannte Grundzustand

Die Rang-eins-Projektion zerfällt als

\[
p_0=\frac14I_4+t,
\qquad \operatorname{tr}t=0.
\]

Auf \(\Lambda^2F_4\) gilt

\[
d\Gamma_2(p_0)=\frac12I_6+d\Gamma_2(t).
\]

Somit ist auf dem Fockraum

\[
\boxed{\;Z=\frac14Q+J_t,\;}
\]

mit

\[
J_t=f^\dagger(I_{16}\otimes t)f
+b^\dagger(I_{10}\otimes d\Gamma_2(t))b.
\]

Es fehlt kein Determinanten- oder Spurterm: Der Familienfaktor des vorhandenen \(W\)-Tensors trägt genau die volle \(\mathfrak{gl}_4\)-Wirkung; der zentrale Anteil ist bereits \(Q/4\). Die Determinantenlinie im bestehenden RR-Vertrag gehört zum separaten \(GL(5)\)-Trägerfaktor, nicht zu dieser Familienreduktion.

Für \(0<|g|/\Delta\le1/20\) ist der vorhandene globale Grundzustandssatz:

\[
Q\Omega=64\Omega,
\qquad
\Omega\text{ ist ein }\operatorname{Spin}(10)\times SU(4)\text{-Singulett}.
\]

SU(4)-Invarianz liefert \(J_t\Omega=0\) für jedes spurlose hermitesche \(t\). Daher

\[
\boxed{\;Z\Omega=16\Omega.\;}
\]

Da \(Z\) selbstadjungiert ist, sind verschiedene Eigenräume orthogonal. Also

\[
\boxed{\;\Omega\perp\ker Z.\;}
\]

Die Reduktion reproduziert den bekannten Grundzustand somit nicht. Sie definiert einen anderen nativen dynamischen Sektor. Genauer sollte er „reduzierender Null-\(Z\)-Sektor“ heißen: Er enthält viele feste \(Q\)-Sektoren und ist allein aus \([Z,H]=0\) noch kein Superselektionssektor der vollständigen Observablenalgebra.

### 4.1 Der volle \(Z=16\)-Raum und die verbleibende Mischdynamik

Schreibe die Einteilchenräume als

\[
\mathcal F_1=\mathcal F_{\rm d}\oplus\mathcal F_0,
\qquad
\dim\mathcal F_{\rm d}=48,\quad \dim\mathcal F_0=16,
\]

und

\[
\mathcal B_1=\mathcal B_{\rm d}\oplus\mathcal B_0,
\qquad
\dim\mathcal B_{\rm d}=30,\quad \dim\mathcal B_0=30,
\]

wobei \(\mathcal F_0=S_+\otimes\mathbb Cu\), \(\mathcal B_0=V_{10}\otimes(u\wedge U)\). Dann ist

\[
Z=N_{f,0}+N_{b,0}.
\]

Der exakte Eigenraum zum bekannten Grundzustandswert \(Z=16\) faktorisiert daher, mit der üblichen graduierten Fermion-Tensorregel, als

\[
\boxed{\;
\mathcal H_{Z=16}
\cong
\mathcal F_{\rm CAR}(\mathcal F_{\rm d})
\otimes
\mathcal F_{\rm CCR}(\mathcal B_{\rm d})
\otimes
\mathcal H_{\rm aux}^{(16)},
\;}
\]

mit

\[
\boxed{\;
\mathcal H_{\rm aux}^{(16)}
=\bigoplus_{k=0}^{16}
\Lambda^k\mathbb C^{16}\otimes
\operatorname{Sym}^{16-k}\mathbb C^{30}.
\;}
\]

Dieser Hilfsfaktor ist endlichdimensional, aber groß:

\[
\dim\mathcal H_{\rm aux}^{(16)}
=\sum_{k=0}^{16}\binom{16}{k}\binom{45-k}{16-k}
=60\,057\,253\,665\,323.
\]

Die Faktorisierung des Hilbertraums faktorisiert den Hamiltonoperator jedoch nicht. Wegen der Familienkeilung besitzt \(H\) genau zwei Typen von Wechselwirkungstermen:

1. zwei dunkle Fermionen \(\to\) ein dunkles Boson, also den bereits beschriebenen \(H_3\)-Term;
2. ein dunkles und ein uniformes Fermion \(\to\) ein gemischtes Boson in \(u\wedge U\).

Ein Term mit zwei uniformen Fermionen fehlt, weil \(u\wedge u=0\). Schematisch gilt damit

\[
H=H_3+\Delta N_{b,0}
+g\sum_{a}\bigl(b_{0a}^\dagger f_a f_0+\mathrm{h.c.}\bigr).
\]

Der zusammengesetzte Operator \(b_{0a}^\dagger f_0\) hat \(Z\)-Ladung \(+1-1=0\) und ist fermionisch ungerade. Er bleibt daher innerhalb eines festen \(Z\)-Sektors dynamisch und koppelt dort an \(f_a\). Das bloße Weglassen des elementaren uniformen Fermionfelds erzeugt folglich keine geschlossene 48-CAR-Dynamik auf dem im vorhandenen nativen Modell ausgewiesenen \(Z=16\)-Zweig.

Dies sieht man auch an der formalen \(U(1)\)-Mittelung

\[
\mathbb E_Z(O)=\frac1{2\pi}\int_0^{2\pi}
e^{i\theta Z}Oe^{-i\theta Z}\,d\theta.
\]

Sie lässt \(H\) und \(b_{0a}^\dagger f_0\) fest, vernichtet aber die einzelnen geladenen Operatoren \(f_0\) und \(b_{0a}\). Die Fixpunktalgebra ist somit größer als die allein von den 48 dunklen CAR-Generatoren erzeugte Algebra. Eine geometrische oder formale Entfernung der elementaren „vierten Richtung“ entfernt die gemischten zusammengesetzten Freiheitsgrade nicht.

### 4.2 Exakte Aufteilung der geladenen Antwort auf demselben \(\Omega\)

Sei \(\bar b=\langle\Omega,N_b\Omega\rangle\). Aus \(Q\Omega=64\Omega\) und der SU(4)-Singulettstruktur folgen die diagonalen Einteilchenkovarianzen

\[
\nu=\frac{\langle N_f\rangle}{64}
=1-\frac{\bar b}{32},
\qquad
n_b=\frac{\bar b}{60}.
\]

Für die Wechselwirkungsableitung eines dunklen elementaren Fermions zerlege

\[
D=D_3+D_{\rm mix},
\]

wobei \(D_3\) den dunklen Partnerkanal \(U\wedge U\) und \(D_{\rm mix}\) den uniformen Partnerkanal \(u\wedge U\) enthält. Die Spin(10)-Kontraktion liefert fünf Einheiten je unabhängiger Partner-Familienrichtung. Ein festes dunkles Familienfeld hat zwei Partner in \(U\) und einen Partner auf \(\mathbb Cu\). Daher gilt im Antikommutator-Skalarprodukt des vollen Grundzustands

\[
\begin{aligned}
\langle\{D,D^\dagger\}\rangle_\Omega
   &=15(\nu+n_b)=:S,\\
\langle\{D_3,D_3^\dagger\}\rangle_\Omega
   &=10(\nu+n_b)=\frac{2S}{3},\\
\langle\{D_{\rm mix},D_{\rm mix}^\dagger\}\rangle_\Omega
   &=5(\nu+n_b)=\frac{S}{3},\\
\langle\{D_3,D_{\rm mix}^\dagger\}\rangle_\Omega
   &=0.
\end{aligned}
\]

Die letzte Orthogonalität ist sogar operatoralgebraisch: In der allgemeinen Antikommutatorform verschwinden zwischen den beiden Kanälen sowohl der Term mit \(\delta_{AB}\), weil \(\Lambda^2U\perp u\wedge U\), als auch der Term mit \(\delta_{jk}\), weil \(U\perp\mathbb Cu\).

Dabei ist

\[
S=15\left(1-\frac{\bar b}{32}+\frac{\bar b}{60}\right)
=15-\frac{7\bar b}{32}.
\]

Schon \(0\le\bar b\le32\) ergibt

\[
\boxed{\;\frac{S}{3}\ge\frac83.\;}
\]

Am vorhandenen schwach gekoppelten Prüfpunkt mit

\[
0.842846<\bar b<1.245656
\]

ist die Schranke deutlich schärfer:

\[
4.9091709<\frac{S}{3}<4.9385425.
\]

Das Weglassen des gemischten Kanals verwirft auf demselben \(\Omega\) somit die strikt positive quadrierte Antwortnorm

\[
\boxed{\;|g|^2\frac{S}{3}\ge\frac83|g|^2.\;}
\]

Diese Größe ist auf dem **vollen** stationären Grundzustand \(\Omega\) gemessen. Da \(\Omega\notin\ker Z\), ist sie kein Moment eines stationären Zustands von \(H_3=H|_{\ker Z}\). Sie ist ein gemeinsamer-Zustand-Operatorvergleich, der quantifiziert, wie viel der nativen vollen Antwort die Null-\(Z\)-Trunkierung nicht enthält.

### 4.3 Optimale native Drei-Familien-Trunkierung

Erlaube als Vergleich die allgemeinste Trunkierung derselben engen nativen Form:

- derselbe eingeschränkte Tensor \(W_3\), aber mit beliebigem komplexem \(g'\);
- ein beliebiger selbstadjungierter Einteilchenterm \(f_U^\dagger h f_U\);
- eine beliebige Bosonenkinetik, die mit den Fermionfeldern kommutiert.

Für ein dunkles elementares Fermion ist die Differenz der ersten Liouvillian-Wirkungen dann

\[
R=(g-g')D_3+gD_{\rm mix}-hf.
\]

Im Antikommutator-Skalarprodukt auf \(\Omega\) gilt nicht nur \(D_3\perp D_{\rm mix}\), sondern auch \(f\perp D_3,D_{\rm mix}\). Letzteres folgt bereits operatoralgebraisch aus CAR und der unterschiedlichen zusammengesetzten Operatorstruktur. Daher

\[
\|R\|_\Omega^2
=|g-g'|^2\frac{2S}{3}
+|g|^2\frac{S}{3}
+\|hf\|_\Omega^2
\ge |g|^2\frac{S}{3}.
\]

Das Minimum wird in dieser Klasse bei \(g'=g\) und \(h=0\) erreicht. Weder eine Neuanpassung der einzigen Kopplung noch ein beliebiger linearer 48-CAR-Term kann den gemischten Kanal reproduzieren. Eine geänderte Bosonenkinetik beeinflusst diese erste Fermionableitung nicht.

Der präzise Ausschluss lautet deshalb: **Keine Hamiltonfunktion derselben nativen Drei-Familien-Form mit nur \(W_3\), neuem \(g'\), linearem Fermionterm und Bosonenkinetik reproduziert die volle gemeinsame-Zustand-Operatorantwort exakt.** Nicht ausgeschlossen sind allgemeinere nichtlineare effektive Operatoren, zusätzliche zusammengesetzte Felder, Gedächtniskerne oder eine andere Zustandspräparation.

## 5. Hodge-Transport und Markierungstwists

Für die durch \(u\) bestimmte orthogonale Zerlegung vertauscht der vierdimensionale Hodge-Operator \(K=*\) die beiden Dreidimensionalen:

\[
K(\Lambda^2U)=u\wedge U,
\qquad
K(u\wedge U)=\Lambda^2U.
\]

Daher gilt auf \(\Lambda^2F_4\)

\[
\boxed{\;K,d\Gamma_2(p_0),K^{-1}=I-d\Gamma_2(p_0).\;}
\]

Der Hodge-Operator erhält also den bosonischen Null-\(Z\)-Unterraum nicht, sondern tauscht ihn mit dem komplementären 30-dimensionalen Bosonraum. Das passt zum bestehenden Hodge-Prüfbericht: Dort ist

\[
W^\sharp=(I_{10}\otimes K)W
\]

ein isometrischer **Basistransport**, aber \((I_{10}\otimes K)W\ne W\). Ein aktives Anwenden von \(K\) nur auf die Bosonen wäre keine Symmetrie des fest geschriebenen Hamiltonoperators. Wer den Hodge-Operator benutzt, muss \(W\), Zustände und Markierungen gemeinsam transportieren.

Auch der bekannte Spiegelungstwist bleibt relevant. Der logarithmische Residuenraum

\[
H^0\!\left(\mathbb P^1,\Omega^1(\log\mu_4)\right)
\cong U
\]

trägt die unverdrehte Augmentationsdarstellung. Der dunkle Teil des in `rr-residue-memory-20260921` verwendeten RR-Hauptteilquotienten trägt dagegen \(U\otimes\chi\) mit \(\chi(S)=-1\). Der skalare Twist ändert den Unterraum \(U\) und den Projektor \(p_0\) nicht; er ändert aber die markierte \(D_4\)-Darstellung. Die neue Reduktion beseitigt diesen Identifikationsunterschied daher nicht.

Bei einer orientierungsumkehrenden Familienpermutation kommt zusätzlich die im vorhandenen Hodge-Bericht dokumentierte Determinantennormalisierung hinzu: Die rohe \(\Lambda^2P\)-Wirkung ist nicht ohne Phase die reelle \(SO(6)\)-Wirkung des SU(4)-Faktors. Das beeinträchtigt den \(Z\)-Erhaltungssatz nicht, verbietet aber eine unmarkierte Gleichsetzung von Hodge-, Spiegel- und nativer Familienwirkung.

## 6. Rolle des globalen Residuensatzes

Der globale Residuensatz ist genau die mathematische Quelle der Kodimension eins:

\[
\sum_{a\in\mu_4}\operatorname{Res}_a\omega=0.
\]

Für vier logarithmische Pole auf \(\mathbb P^1\) ist das Bild der Residuenkarte deshalb der dreidimensionale Augmentationsraum

\[
U=\{(r_a)\in\mathbb C^4:\sum_ar_a=0\}.
\]

Dies ist Standardliteratur, keine neue TFPT-spezifische Behauptung. Die lokale Residuenabbildung für logarithmische Formen wird durch die Residuensequenz beschrieben; der globale Summenzwang folgt auf der kompakten Kurve aus dem Residuensatz. Siehe etwa:

- [Stacks Project, Tag 0FMU: Log poles along a divisor](https://stacks.math.columbia.edu/tag/0FMU), für die kanonische lokale Residuensequenz;
- [Lecture notes on Riemann surfaces, Theorem 13.9](https://orbilu.uni.lu/bitstream/10993/22995/1/LectureNotes15-16.pdf), für \(\sum_x\operatorname{res}_x\omega=0\) auf einer kompakten Riemannschen Fläche.

Die Literatur rechtfertigt damit \(U\) als natürlichen logarithmischen RR-Residuenraum. Sie identifiziert ihn nicht von selbst mit dem physisch ausgeführten Familienfaktor des nativen \(W\)-Hamiltonoperators. Dieser letzte Schritt benutzt weiterhin die markierte, bedingte RR–Familien-Zuordnung des bestehenden Projekts.

## 7. Ist der Satz bereits bekannt?

Im begrenzt geprüften Bestand waren die tragenden Zutaten bereits vorhanden:

1. `rr-residue-memory-20260921/RESIDUEN_PRUEFBERICHT.md` identifiziert \(U\) exakt als globalen Residuensummen-Nullraum und trennt den Spiegelungstwist.
2. `rr-continuous-clock-20260921/ALGEBRA.md` beweist die volle \(\mathfrak{gl}_4\)-Äquivarianz von \(W\).
3. `universalraum-native-ground-response-20260915` belegt den eindeutigen schwach gekoppelten \(Q=64\)-Singulettgrundzustand.

In diesen geprüften Quellen fand sich jedoch keine explizite Formulierung des Operators

\[
Z=f^\dagger(I_{16}\otimes p_0)f
+b^\dagger(I_{10}\otimes d\Gamma_2(p_0))b,
\]

seines Kerns oder der Aussage \(Z\Omega=16\Omega\). Der vorliegende Satz ist daher eine neue direkte **Korollarformulierung** aus bereits bewiesenen endlichen Identitäten, kein neuer unabhängiger Mechanismus und kein neuer physischer Auswahlbeweis.

## 8. Zur möglichen Zugabe \(\mu Z\)

Weil \([Z,H]=0\) und \(\operatorname{spec}Z\subset\mathbb N_0\), verschiebt

\[
H_\mu=H+\mu Z,
\qquad \mu>0,
\]

jeden festen \(Z=z\)-Sektor relativ um \(\mu z\). Ein hinreichend großes positives \(\mu\) würde bei vorhandenem Kern-Grundzustand den Null-\(Z\)-Sektor energetisch bevorzugen. Daraus folgt keine Auswahl bei beliebigem kleinen \(\mu\), und der notwendige Kreuzungswert hängt vom Spektrum der verschiedenen \(Z\)-Sektoren ab.

Vor allem ist \(\mu Z\) ein neuer, die volle SU(4)-Symmetrie auf den Stabilisator von \(u\) reduzierender Hamiltonterm mit einer zusätzlichen freien Skala. Er ist nicht aus dem globalen Residuensatz oder aus dem bisherigen nativen Grundzustandssatz abgeleitet. Deshalb ist er kein Bestandteil dieses Ergebnisses und darf nicht als bereits vorhandene physische Familienauswahl ausgegeben werden.

## Endverdict

**Exakt korrekt:** Der globale Residuensummen-Nullraum erzeugt über den bereits bewiesenen \(\mathfrak{gl}_4\)-Intertwiner einen nativen, linearen, exakt reduzierenden \(48\)-CAR-/\(30\)-CCR-Einteilchensektor mit unveränderten \(g,\Delta,W\)-Koeffizienten.

**Entscheidende Grenze:** Dieser Sektor ist orthogonal zum bekannten schwach gekoppelten Grundzustand, wird vom Hodge-Operator auf der Bosonseite mit seinem Komplement vertauscht und ist physisch nicht ausgewählt. In dem im vorhandenen nativen Modell ausgewiesenen \(Z=16\)-Grundzustandszweig bleiben \(Z\)-neutrale gemischte Kompositoperatoren erhalten; ihre quadrierte Antwortnorm ist mindestens \(8|g|^2/3\) und kann in der eng definierten nativen 48-CAR-/30-CCR-Form weder durch ein neues \(g'\) noch durch einen Einteilchenterm absorbiert werden. Die Existenz der Reduktion ist ein echter Strukturfortschritt, aber keine Herleitung von drei beobachteten Fermiongenerationen oder des bisherigen nativen Vakuums und kein Ausschluss allgemeiner nichtlinearer Effektivbeschreibungen.
