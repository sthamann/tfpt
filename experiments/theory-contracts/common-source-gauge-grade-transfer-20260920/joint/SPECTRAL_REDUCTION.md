# Gemeinsame Zustandsabbildung für zwei benachbarte Quellen

20. September 2026. Bedingter Satz im bestehenden Compiler-Hamiltonoperator;
keine Auswahl seiner Kopplungen oder physische Gesamtherleitung.

## Gegenstand

Verwendet wird genau die offene Kette mit zwei Quellen und drei
Materieregistern aus `compiler-domain-wall-core-20260919`:

\[
H=\kappa(L_1+L_2)+J(E_1+E_2)+\mu V,
\qquad \kappa,J,\mu\geq0.
\]

Hier sind \(E_e=H_{E,e}\), \(0\leq L_e\leq2\), \(0\leq V\leq2\).
Der Transfer ist auf den Quelllabels diagonal und auf Materie skalar:
\(V(\alpha,\beta)=1-\operatorname{Re}\langle\psi_\alpha,\psi_\beta\rangle\).
Setze \(P=\mathbf1_{\{0\}}(E_1+E_2)\), \(Q=I-P\).

Wegen der Positivität ist \(\operatorname{ran}P=\ker E_1\cap\ker E_2\).
Dies ist der gemeinsame Projektor, nicht das im Allgemeinen nichtidempotente
Produkt zweier lokaler Projektoren. Quelllabel-Diagonalität gibt exakt
\([V,P]=0\). Die Reflexionsterme müssen getrennt behandelt werden.

## Exakte Lücke des gemeinsamen Ereignisoperators

Bei festen Quellwurzeln sei \(s=|\langle\psi_\alpha,\psi_\beta\rangle|\).
Auf den äußeren Materieregistern zerlegt man nach den jeweiligen
Reflexionseigenwerten \(a,c\in\{+1,-1\}\). Auf dem mittleren Register bleibt

\[
E_1+E_2=2I-a r_\alpha-c r_\beta.
\]

Die äußeren Multiplizitäten für \((++),(+-),(-+),(--)\) sind \(9,3,3,1\).
Aus \(r=I-2|\psi\rangle\langle\psi|\) folgen die mittleren Spektren:

| Äußere Zeichen | Vier mittlere Eigenwerte |
|---|---|
| \(++\) | \(0,0,2-2s,2+2s\) |
| \(--\) | \(4,4,2-2s,2+2s\) |
| \(+-\), \(-+\) | \(2,2,2-2\sqrt{1-s^2},2+2\sqrt{1-s^2}\) |

Die nativen Überlappungsbeträge sind \(0,1/2,1/\sqrt2,1\).
Die jeweiligen Nullraumdimensionen sind \(24,18,18,28\); die kleinste
positive Eigenzahl über alle Quellpaare ist

\[
\delta=2-\sqrt3>0,\qquad Q(E_1+E_2)Q\geq\delta Q.
\]

Die Endfälle \(s=0,1\) haben zusätzliche Nullmoden; sie dürfen nicht durch
Einsetzen in eine generische Formel für die kleinste positive Eigenzahl
als lückenlos ausgegeben werden. Die vollständigen Spektren oben behandeln
diese Fälle korrekt. Diese Lücke gilt für zwei Quellen, nicht automatisch
für beliebig lange Ketten.

## Kontrollierte Reduktion des gesamten Zweiquellenoperators

Definiere \(B=4\kappa+2\mu\) und \(d=J\delta-B\).
Aus den positiven Summanden folgt

\[
PHP\leq BP,\qquad QHQ\geq J\delta Q.
\]

Da \(JE\) und \(\mu V\) keine P/Q-Kreuzecke haben, ist
\(QHP=\kappa Q(L_1+L_2)P\). Die Spektralbreite von
\(\kappa(L_1+L_2)\) liegt im Intervall \([0,4\kappa]\).
Subtraktion von \(2\kappa I\) ändert die Kreuzecke nicht und ergibt

\[
\|QHP\|\leq 2\kappa.
\]

Für \(d>0\) trennen die beiden Min-Max-Abschätzungen die unteren
\(p=\operatorname{rank}P\) Eigenwerte vom Rest:

\[
\lambda_p(H)\leq B<J\delta\leq\lambda_{p+1}(H).
\]

Für einen normierten Grundvektor \(g\) folgt aus der Q-Eigenwertgleichung

\[
\|Qg\|\leq \frac{2\kappa}{d}\|Pg\|,
\qquad
\|Qg\|^2\leq\frac{4\kappa^2}{d^2+4\kappa^2}.
\]

Die energieabhängige Feshbach-Korrektur erfüllt für \(E\leq B\)

\[
\|PHQ(QHQ-E)^{-1}QHP\|\leq\frac{4\kappa^2}{d}.
\]

Damit wird die Komplementelimination in diesem ausdrücklich angegebenen
Bereich kontrolliert. Dies behebt nicht rückwirkend die schwach gekoppelte
Ising-Paketrechnung; dort ist diese Voraussetzung gerade nicht erfüllt.

## Ein einziger linearer Transport für alle Observablen

Sei \(\Pi\) der tatsächliche untere Spektralprojektor vom Rang \(p\).
Für die stärkere hinreichende Bedingung \(d>2\kappa\) gilt
\(\|Q\Pi\|\leq2\kappa/d<1\). Eine elementare Begründung ist die
Sylvester-Gleichung

\[
(QHQ)(Q\Pi)-(Q\Pi)(H|_{\Pi})=-QHP(P\Pi).
\]

Ihre Lösung ist ein konvergentes Integral der beiden Halbgruppen; ihre
Spektren sind um mindestens \(d\) getrennt. Die Norm des Integrals ist
höchstens \(2\kappa/d\). Gleicher Rang und dieser Winkelabstand geben
Invertierbarkeit von \(P\Pi P\) auf \(\operatorname{ran}P\).

Somit existiert die kanonische Isometrie

\[
W=\Pi P(P\Pi P)^{-1/2},\qquad W^*W=P,\qquad WW^*=\Pi.
\]

Jetzt sind \(W^*HW\), \(W^*VW\) und \(W^*OW\) für jede lokale Observable
auf demselben Raum definiert. Insbesondere darf \(V\), obwohl es P erhält,
nach der zusätzlichen echten H-Diagonalisierung nicht ungeprüft unverändert
übernommen werden. Der Satz konstruiert W spektral und kontrolliert seinen
Abstand; er gibt nicht bereits sämtliche Matrixelemente in geschlossener Form.

Jede vorhandene unitäre Symmetrie, die H und P erhält, wird durch W
intertwiniert. Dies gilt insbesondere für die erhaltene gemeinsame
Quell-Vierteldrehung. Es identifiziert diese nicht mit Hyperladung,
physischer Zeit oder der anderen Coxeter-Clock.

## Beitrag zum ursprünglichen Ziel und Grenze

Die zuvor nur lokal mögliche Zustandsabbildung ist damit für den vollständigen
Zweiquellenraum in einem benannten Kopplungsbereich gemeinsam kontrollierbar.
Der entscheidende positive Beitrag ist eine Fehlerkontrolle für Zustand,
Transfer und Antworten zusammen. Die Wahl dieses Bereichs aus P1/P2, eine
gleichmäßige Kettenlücke, die Fermion-/Yukawa-Abbildung und der physische
Raumzeitgrenzwert bleiben eigenständige fehlende Herleitungen. Der Satz darf
nicht als vollständiger Universalraum oder als Beweis der Ising-/E8-Grenze
bezeichnet werden.

Mathematischer Rahmen: [Dusson, Sigal und Stamm, The Feshbach–Schur map and
perturbation theory](https://arxiv.org/abs/2105.02058). Die nativen
Überlappungswerte und die spezifische Ereignislücke stammen aus der hier
angegebenen Quellenrechnung, nicht aus dieser allgemeinen Literatur.
