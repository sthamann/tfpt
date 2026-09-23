# Nativer Zwei-Quellen-Transfer und gemeinsamer Ereignisnullraum

20. September 2026 · Experiment, keine Ledger- oder Paper-Promotion

**Verdict: `PARTIAL / PASS_EXACT_TWO_SOURCE_TRANSFER_SEPARATION`.**

Der vorhandene Transferterm $V$ bewahrt den gemeinsamen Nullraum zweier
benachbarter Ereignisoperatoren exakt. Die vermutete Leckage kommt nicht von
$V$, sondern bereits von einem benachbarten Reflexionsterm $L$. Dafür gibt
es einen exakten Zeugen mit nur einem Materiebasiseintrag. Zugleich besitzt
der gemeinsame Zwei-Kanten-Ereignisoperator über allen nativen Wurzelpaaren
eine einheitliche positive Lücke

\[
\delta=2-\sqrt3.
\]

Diese Lücke liefert im starken Ereignisbereich eine kontrollierte
Feshbach-Reduktion und eine einzige gemeinsame Isometrie für Hamiltonoperator,
Transfer und lokale Antworten. Das Resultat betrifft genau zwei Quellen. Es
wählt die Kopplungen nicht aus und leitet weder physische Zeit noch Kontinuum,
Chiralität, Gravitation oder eine TOE her.

## 1. Unveränderte Originaloperatoren

Auf zwei Quellen und drei Materieregistern wird genau die Hamiltonfamilie aus
`UR.COMPILER.DOMAIN_WALL_CORE.25` verwendet:

\[
H=\kappa(L_1+L_2)+J(E_1+E_2)+\mu V,
\qquad \kappa,J,\mu\ge0,
\]

\[
L_e=I-\frac1{60}\sum_{\ell}R_\ell^{(e)}\otimes r_\ell\otimes r_\ell,
\qquad
E_e=\sum_\alpha |\alpha\rangle\!\langle\alpha|
       \otimes(I-r_\alpha\otimes r_\alpha),
\]

\[
V(\alpha,\beta)=1-\operatorname{Re}
\langle\psi_\alpha|\psi_\beta\rangle.
\]

Setze

\[
P=\mathbf 1_{\{0\}}(E_1+E_2),\qquad Q=I-P.
\]

Da $E_1,E_2\ge0$, ist
$\operatorname{ran}P=\ker E_1\cap\ker E_2$. Dies ist der wirkliche
gemeinsame Projektor. Das geordnete Produkt der beiden lokalen
Nullprojektoren ist für ein generisches Wurzelpaar nicht idempotent und wird
hier nirgends als Ersatz verwendet.

## 2. Der tatsächliche Transfer $V$ bewahrt den gemeinsamen Nullraum

In der phasenmarkierten Wurzelbasis ist $V$ diagonal auf den beiden
Quellregistern und ein Skalar auf allen Materieregistern. Daher wirkt es auf
jeder Faser $(\alpha,\beta)$ als

\[
V_{\alpha\beta}=v_{\alpha\beta} I_{4^3}.
\]

Der gemeinsame Nullraum ist die direkte Summe seiner Faseranteile
$K_{\alpha\beta}$. Somit gilt ohne Kommutativitätsannahme an die beiden
lokalen Projektoren

\[
[V,P]=0,
\qquad
QVP=(I-P)VP=0,
\qquad
PVP=VP=PV.                                      \tag{2.1}
\]

Dies bleibt mit der bekannten Ladungswirkung vereinbar. Unter der
gleichzeitigen Vierteldrehung beider Quellen ist
$v_{i\alpha,i\beta}=v_{\alpha\beta}$; daher bleibt die gesamte
$\mathbb Z_4$-Ladung erhalten. Die nichtkonstanten Fouriermoden von $V$
verschieben die einzelnen Ladungen um $(+1,-1)$ oder $(-1,+1)$. Eine solche
Ladungsverschiebung ändert nicht die Tatsache, dass jede phasenmarkierte
Faser in ihrem eigenen $K_{\alpha\beta}$ bleibt.

## 3. Vollständiges Zwei-Kanten-Ereignisspektrum

Sei bei festen Quellwurzeln

\[
s=|\langle\psi_\alpha|\psi_\beta\rangle|.
\]

Zerlege die beiden äußeren Materieregister nach den
Reflexionseigenwerten $a,c\in\{+1,-1\}$. Auf dem gemeinsamen mittleren
Register reduziert sich $E_1+E_2$ exakt auf

\[
2I-a r_\alpha-c r_\beta.
\]

Die äußeren Multiplizitäten der Sektoren $++,+-,-+,--$ sind $9,3,3,1$.
Die vier Eigenwerte auf dem mittleren Register lauten:

| Sektor | Eigenwerte |
|---|---|
| $++$ | $0,0,2-2s,2+2s$ |
| $--$ | $4,4,2-2s,2+2s$ |
| $+-$, $-+$ | $2,2,2-2\sqrt{1-s^2},2+2\sqrt{1-s^2}$ |

Der Checker rekonstruiert alle 60 nativen Strahlen. Für die 3600 geordneten
Paare treten genau

| $s^2$ | Paarzahl | $\dim K_{\alpha\beta}$ | kleinste positive Eigenzahl |
|---:|---:|---:|---:|
| $0$ | 900 | 24 | $2$ |
| $1/4$ | 1920 | 18 | $2-\sqrt3$ |
| $1/2$ | 720 | 18 | $2-\sqrt2$ |
| $1$ | 60 | 28 | $2$ |

auf. Die zusätzlichen Nullmoden bei $s=0$ und $s=1$ sind in diesen
Dimensionen enthalten. Über die Orthokomplemente aller Faserkerne folgt
deshalb der einheitliche exakte Satz

\[
Q(E_1+E_2)Q\ge(2-\sqrt3)Q.                    \tag{3.1}
\]

## 4. Exakter kleinster Stützzeuge für die $L$-Leckage

Wähle die phasenmarkierten Quelllabels

\[
\alpha=(\text{Strahl }0,\text{Phase }0),\qquad
\beta=(\text{Strahl }1,\text{Phase }0)
\]

und auf den drei Materieregistern den einzelnen Basisvektor

\[
x=|1,2,2\rangle.
\]

Der Checker bestätigt exakt $E_1x=E_2x=0$. Der primitive native
Reflexionsstrahl $\ell=3$ schickt das linke Quelllabel als einziger der 60
Summanden auf das volle Zielquelllabel 218, also Strahl 54 mit Phase 2. Auf
Materie wirkt dieser Zweig als

\[
(r_3\otimes r_3\otimes I)x=-|1,0,2\rangle.
\]

Im Zielquellraum zerfällt der Vektor orthogonal in

\[
-|1,0,2\rangle=
\underbrace{\frac{-|1,0,2\rangle+|1,1,2\rangle}{2}}_{\in K_{54,1}}
+
\underbrace{\frac{-|1,0,2\rangle-|1,1,2\rangle}{2}}_{q}.
\]

Für den zweiten Summanden gilt

\[
E_1q=0,\qquad E_2q=2q,\qquad \|q\|^2=\frac12.
\]

Da kein anderer primitiver Summand dieselbe Zielquellfaser erreicht, kann
dieser Anteil in $L_1=I-\frac1{60}\sum_\ell U_\ell$ nicht wegkürzen. Der
vollständige $L_1$-Zweig außerhalb des gemeinsamen Nullraums ist exakt

\[
Q L_1 P x\big|_{218}
=\frac{|1,0,2\rangle+|1,1,2\rangle}{120},
\qquad
\left\|Q L_1 P x\big|_{218}\right\|^2=\frac1{7200}.       \tag{4.1}
\]

Damit ist $QL_1P\ne0$. Der rechtsgespiegelte Satz gilt für $L_2$.
Der Eingabevektor hat Stützgröße eins in der Materiebasis und ist in diesem
Sinn ein stützminimaler nichttrivialer Zeuge.

Die Viertelphasen-Fouriersumme über beide Quellorbits hebt denselben Zeugen
in jedes Paar individueller Quellladungen
$(k_1,k_2)\in\mathbb Z_4^2$. $L_1$ erhält beide Ladungen, und der
Leckagezweig bleibt von Null verschieden. Die Leckage ist daher kein Artefakt
einer Ladungsmischung durch $V$.

## 5. Kompatible Projektion und kontrollierter echter Unterraum

Die unmittelbare gemeinsame Kompression ist

\[
H_P=PHP,\qquad L_{e,P}=PL_eP,\qquad V_P=PVP=VP.             \tag{5.1}
\]

Sie ist selbstadjungiert und verwendet für alle Operatoren denselben Raum.
Wegen (4.1) ist sie allein noch kein Beweis, dass der rohe Nullraum unter dem
vollen $H$ invariant wäre.

Hier liefert (3.1) einen konstruktiven nächsten Schritt. Setze

\[
B=4\kappa+2\mu,\qquad
d=J(2-\sqrt3)-B.
\]

Aus $0\le L_e\le2$, $0\le V\le2$ und (3.1) folgen

\[
PHP\le BP,\qquad QHQ\ge J(2-\sqrt3)Q.
\]

Nur $H_0=\kappa(L_1+L_2)$ besitzt eine $P/Q$-Kreuzecke. Seine
Spektralbreite liegt in $[0,4\kappa]$; nach Subtraktion von
$2\kappa I$ folgt

\[
\|QHP\|\le2\kappa.                                       \tag{5.2}
\]

Ist $d>0$, trennen Min-Max und Operatorordnung die unteren
$p=\operatorname{rank}P$ Eigenwerte vom Komplement:

\[
\lambda_p(H)\le B<J(2-\sqrt3)\le\lambda_{p+1}(H).
\]

Für jeden normierten Grundvektor $g$ gilt dann

\[
\|Qg\|^2\le
\frac{4\kappa^2}{d^2+4\kappa^2}.                         \tag{5.3}
\]

Die energieabhängige exakte Feshbach-Wirkung auf $P$ ist für $E\le B$

\[
H_{\mathrm{eff}}(E)=PHP-PHQ(QHQ-E)^{-1}QHP,
\]

mit Korrekturschranke $4\kappa^2/d$.

Unter der stärkeren hinreichenden Bedingung $d>2\kappa$ sei $\Pi$ der
tatsächliche untere Spektralprojektor vom Rang $p$. Die
Sylvester-Gleichung für $Q\Pi$ und die Spektraltrennung geben

\[
\|Q\Pi\|\le\frac{2\kappa}{d}<1.
\]

Damit ist $P\Pi P$ auf $\operatorname{ran}P$ invertierbar und

\[
W=\Pi P(P\Pi P)^{-1/2},
\qquad W^*W=P,
\qquad WW^*=\Pi                                             \tag{5.4}
\]

eine kanonische gemeinsame Isometrie. Nun werden Hamiltonoperator, Transfer
und jede lokale Antwort mit demselben $W$ transportiert:

\[
H_{\rm low}=W^*HW,\qquad V_{\rm low}=W^*VW,\qquad
O_{\rm low}=W^*OW.
\]

Jede unitäre Symmetrie, die sowohl $H$ als auch $P$ erhält, wird durch
$W$ verflochten. Dazu gehört die gemeinsame Quell-Vierteldrehung. Dies ist
keine Identifikation mit Hyperladung, physischer Zeit oder der Coxeter-Clock.

## 6. Aussagegrenze

Das Ergebnis entscheidet die lokale Transferfrage:

- $V$ erhält den gemeinsamen Ereignisnullraum exakt.
- Benachbarte $L$-Terme erhalten ihn im Allgemeinen nicht.
- Die kleinste native Zwei-Quellen-Lücke ermöglicht in einem ausdrücklich
  benannten starken Ereignisbereich eine kontrollierte gemeinsame
  Zustands- und Observable-Abbildung.

Es folgt keine Auswahl der Bedingung
$J(2-\sqrt3)>4\kappa+2\mu$ aus P1/P2. Der Satz gilt nicht automatisch für
eine beliebig lange Kette oder den thermodynamischen Grenzwert. Er ändert
den positiven endlichen Vierquellen-Grundzustandssatz aus dem gepinnten
Contract `.28` nicht; dieser wird hier weder neu ausgeführt noch
abgeschwächt. Ebenso werden keine E8-Ströme, chirale Materie, Gravitation
oder vollständige physische Herkunft behauptet.

Ausführung:

```text
python3 -B checker.py --out results.json
python3 -OO checker.py --out results_optimized.json
```

Beide Läufe müssen `PASS_EXACT_TWO_SOURCE_TRANSFER_SEPARATION` melden.
