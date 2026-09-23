# Gemeinsame Quellenantwort von Paar und Vermittler

21. September 2026 · `UR.SOURCE.JOINT_RESPONSE.01` · **PARTIAL**

## Frage und Herkunft

Die eingesandte Fortsetzung fordert zu Recht, die tatsächliche Quellenantwort zu bestimmen, statt den positiven Vergleichsoperator H+ als obligatorisches Ergebnis vorauszusetzen. Ihre Möbiusschranke und ihre Pauliantwort sind getrennte Aussagen über unterschiedliche Operatoren. Beide werden nicht als vollständige TFPT-Herleitung behandelt.

Der konstruktive Ausgangspunkt dieses Anschlusses ist die **bereits vorhandene**, bedingte Randquelle aus `UR.SOURCE.DRESSED_NATIVE.01` und `UR.SOURCE.PAIR_TRANSFER.01`. Deren vollständige Paarantwort wurde am 20. September hergeleitet. Sie ist kein neues Ergebnis dieser Runde. Neu ist hier die gemeinsame Behandlung dieser bilokalen Paarzustände und des ebenfalls schon vorhandenen lokalen Vermittlerzustands einschließlich ihrer Überlappung.

Die Voraussetzungen bleiben das gewählte Zehnkanalgitter Gamma, seine F(E8)-Einbettung, die Energiematrix Vaux, der Gittervakuumzustand, die Kokzykluskonvention und die zugeordnete konforme Zylinderzeit. Der Ursprung dieser gemeinsamen physikalischen Ausführung aus P1/P2 ist nicht bewiesen. Die zusätzlichen Kanäle werden hier weder neu eingeführt noch nachträglich als aus P1/P2 hergeleitet ausgegeben.

Die entscheidungsrelevante Frage lautet: **Liefert die bereits vorhandene Quelle selbst unabhängige Paar- und Vermittlerzustände samt Zeitantwort, wenn die Koinzidenz nicht zu früh genommen wird?** Erfolg heißt eine quellenseitig definierte, gruppenverträgliche Isometrie und ein kontrollierter Zeitgrenzwert. Abbruch der stärkeren Identifikation ist erforderlich, sobald diese Zustandsabbildung keine Abbildung der tatsächlichen Feldprodukte ist. Ein erfolgreicher Zweiteilchensatz autorisiert keinen frei ergänzten Vielteilchen-Hamiltonoperator.

## 1. Übernommene exakte Quellenantwort

Sei E die 2016-dimensionale äußere Quadratrepräsentation und B der 60-dimensionale Vermittlerlabelraum. Der native Tensor erfüllt

\[
A=W^\dagger W,\quad WW^\dagger=8I_B,\quad
\widehat W=W/\sqrt8,\quad P_b=A/8,\quad P_d=I_E-P_b.
\]

Dabei sind E und B zunächst **Labelräume**, keine behauptete volle CAR/CCR-Algebra der Quelle.

Für die tatsächlich eingesetzten ungeraden Randfelder liefert die antisymmetrische bilokale Einsetzung J_r, mit rho=r² und 0<rho<1,

\[
J_r^\dagger J_s=G(rs),\qquad G(v)=d(v)I_E+o(v)A,
\]
\[
d(v)=\frac{v^2(2-v)}{2(1-v)^3},\qquad
o(v)=\frac{2-v}{2(1-v)^2}.
\]

Schreibe g_b=d+8o und g_d=d. Der normierte Paarzustandsoperator ist

\[
U_r=J_rG(\rho)^{-1/2},\qquad U_r^\dagger U_r=I_E.
\]

Die lokale Vermittlerabbildung M:B→H_s ist durch die vorhandenen normierten Zustände Phi_A definiert. M†M=I_B, H_sM=3M. Im bisherigen Quellenbeweis gilt J_r=Σr^n C_n, C_0=MW und H_sC_n=(3+n)C_n. Somit

\[
M^\dagger U_r=c\widehat W,\qquad
c=\sqrt{\frac8{g_b(\rho)}}\in(0,1).
\]

Die alten Aussagen bleiben erhalten: Am exakten Koinzidenzpunkt fallen der lokale helle Paarzustand und der Vermittler zusammen. Die nichtnormierte Koinzidenzabbildung besitzt deshalb keine zwei unabhängigen Kopien.

## 2. Der gemeinsame positive Gramquotient

Nun werden die **beiden bereits vorhandenen Einsetzungen** gemeinsam betrachtet:

\[
S_r(x,y)=U_rx+My,\qquad (x,y)\in E\oplus B.
\]

Ihre vollständige Gram-Matrix ist

\[
\mathcal G_r=S_r^\dagger S_r=
\begin{pmatrix}I_E&c\widehat W^\dagger\\c\widehat W&I_B\end{pmatrix}.
\]

Auf den 1956 dunklen Richtungen beträgt der Eigenwert eins. Auf jedem der 60 hellen Paar-/Vermittlerblöcke lauten die Eigenwerte 1+c und 1−c. Da 0<c<1, ist die Matrix positiv definit und hat Rang **2076**. Es wird kein neuer physikalischer Oszillator ergänzt.

Die gemeinsame polare Isometrie

\[
\mathcal V_r=S_r\mathcal G_r^{-1/2}
\]

ist damit exakt definiert. Die Gruppenwirkung und die additiven Quellenladungen werden erhalten, weil S_r äquivariant ist und die Gram-Matrix mit der markierten Darstellung kommutiert.

Die Festlegung zuerst einzeln normierter Paar- und Vermittlereinsetzungen ist hier ausdrücklich Teil des Ableseprotokolls. Sie wird nicht als von P1/P2 ausgewählte Präparationsregel behauptet.

## 3. Die gesamte gemeinsame Zeitantwort

Für die vorhandene Quelle H_s=L_0 gilt, zunächst für tau≥0,

\[
T_r(\tau)=e^{-3\tau}G(\rho e^{-\tau})G(\rho)^{-1}.
\]

Die **unnormierte gemeinsame** Antwort lautet deshalb

\[
\mathcal C_r(\tau)=
\begin{pmatrix}
T_r(\tau)&c e^{-3\tau}\widehat W^\dagger\\
c e^{-3\tau}\widehat W&e^{-3\tau}I_B
\end{pmatrix}.
\]

Die tatsächliche normierte Zeitantwort ist

\[
\mathcal R_r(\tau)=\mathcal G_r^{-1/2}
\mathcal C_r(\tau)\mathcal G_r^{-1/2}
=\mathcal V_r^\dagger e^{-\tau H_s}\mathcal V_r.
\]

Für reelle Zeit setzt man tau=it. Dies ist durch die absolut konvergenten Spektralreihen bei rho<1 gedeckt. Die Formel entsteht aus denselben Quelloperatoren und demselben H_s; es wurde kein Wunschgenerator rückwärts in einen Korrelator übersetzt.

Ein einzelner heller normierter Paarzustand zerfällt als

\[
\chi_r=c\phi+\sqrt{1-c^2}\,\eta_r,
\qquad \eta_r\perp\phi.
\]

Die normierte Antwort von eta_r ist

\[
T_\eta(\tau)=e^{-3\tau}
\frac{g_b(\rho e^{-\tau})-8}{g_b(\rho)-8}.
\]

Sie enthält alle Grade n≥1. Die Dunkelantwort enthält alle Grade n≥2. Bei endlichem rho bleibt die Rückwirkung dieser höheren Grade erhalten. Die gemeinsame Polarabbildung macht diese Zeitantwort nicht zu einer exakten endlichen Hamiltonentwicklung.

## 4. Kontrollierter gemeinsamer Zustands- und Zeitgrenzwert

Die Normen aus dem alten Quellenbeweis sind C_0†C_0=A, C_1†C_1=3A/2 und C_2†C_2=I+2A. Also geht eta_r im Grenzfall rho→0 in den normierten ersten Nachfahren von Phi über, dessen Energie vier ist. Die dunklen Zustände gehen in C_2P_d über, Energie fünf.

In der hellen Labelbasis e_±=(e_pair±e_b)/√2 gilt

\[
\mathcal V_r e_+=
\sqrt{\frac{1+c}{2}}\,\phi+
\sqrt{\frac{1-c}{2}}\,\eta_r,
\]
\[
\mathcal V_r e_-=
-\sqrt{\frac{1-c}{2}}\,\phi+
\sqrt{\frac{1+c}{2}}\,\eta_r.
\]

Damit besitzt die gemeinsame Zustandsabbildung einen wohldefinierten isometrischen Grenzwert. In diesem Grenzwert sind die Spektralmultiplizitäten

| Quellenenergie | Dimension | Herkunft |
|---|---:|---|
| 3 | 60 | vorhandene lokale Vermittler-/helle Paarprimärzustände |
| 4 | 60 | deren vorhandene erste Nachfahren |
| 5 | 1956 | dunkle antisymmetrische zweite Produktkoeffizienten |

Der abgeleitete Generator im orthonormalisierten hellen Paar-/Vermittlerlabelraum ist

\[
K_{b,0}=\begin{pmatrix}7/2&-1/2\\-1/2&7/2\end{pmatrix},
\qquad K_{d,0}=5I_{1956}.
\]

Auf dem gesamten E⊕B-Raum lässt er sich schreiben als

\[
K_0=
3I+\frac12
\begin{pmatrix}P_b&-\widehat W^\dagger\\-\widehat W&I_B\end{pmatrix}
+2\begin{pmatrix}P_d&0\\0&0\end{pmatrix}.
\]

Die Quellenladungsverschiebung −q/4 aus dem älteren Vertrag kann blockweise auf beiden Seiten mitgeführt werden. q meint dabei die dortige additive Quellenladung, nicht den nativen Fock-Zähler N_f+2N_b. Sie ändert die Energiedifferenz der beiden hellen Nachfahren nicht.

### Gleichmäßige Zeitkontrolle

Der Gewichtsanteil des niedrigsten Zustands in eta_r ist

\[
q_1(\rho)=\frac{12\rho}{g_b(\rho)-8}
=\frac{24(1-\rho)^3}{(4-3\rho)(6-5\rho)}.
\]

Für 0<rho<1 gilt 1−q_1≤2rho. Ein exakter positiver Rest beweist dies:

\[
2\rho-(1-q_1)=
\frac{\rho(2-\rho)(7-6\rho)}{(4-3\rho)(6-5\rho)}>0.
\]

Deshalb beträgt der Fehler der reellen eta-Antwort gegenüber e^(−4it) höchstens 4rho, gleichmäßig über alle Zeiten. Die zusätzliche Rotation mit sin(theta)=sqrt((1−c)/2) hat Fehler höchstens 2sin(theta)≤sqrt(3rho), weil 1−c≤1−c²≤3rho/2. Der alte Dunkelkanalfehler ist höchstens 5rho und wird von 4rho+sqrt(3rho) dominiert. Folglich

\[
\boxed{\sup_{t\in\mathbb R}
\|\mathcal R_r(it)-e^{-itK_0}\|
\le \min\{2,\,4\rho+\sqrt{3\rho}\}.}
\]

Die Abschätzung benutzt die vollständigen positiven Spektralreihen. Endliche Koeffizientenprüfungen ersetzen diesen Beweis nicht.

## 5. Warum dies die falsche RR-Identifikation nicht wieder einführt

Der absolute Quellenblock hat Eigenwerte drei und vier. Er besitzt **keinen** zusätzlichen Nullzustand und widerspricht daher nicht dem eingesandten Satz über einen positiven Generator mit eindeutigem Vakuum.

Subtrahiert man ausschließlich zum Vergleich die Summe der beiden Quellen-Einteilchenenergien, also drei, entsteht auf dem hellen Block ein positiver rang-eins Rest. Das ist eine verbundene Zweiteilchenenergie, keine erlaubte globale Verschiebung des ganzen Quellen-Hamiltonoperators. Im dunklen Kanal bleibt zugleich ein Rest zwei. Der vollständige Quellenblock ist folglich nicht der frühere H+-Block.

Im Grenzwert kann K_b,0 die **orthogonalisierten** Paar-/Vermittlerlabels bei t=pi vollständig vertauschen. Diese Aussage ist jedoch von der Präparation abhängig. Die resultierenden Zustände sind (phi+eta_0)/√2 und (phi−eta_0)/√2. Sie sind nicht identisch mit den ursprünglich einzeln eingesetzten lokalen Feldern. Der ursprüngliche lokale Vermittler phi ist weiterhin ein Energieeigenzustand.

Das macht eine Kontrolle besonders wichtig: Ersetzt man das Einsetzungsprotokoll durch S_(lambda,r)=(lambda U_r,M), mit lambda>0, entsteht im Grenzfall

\[
K_\lambda=4I-v_\lambda v_\lambda^\dagger,
\qquad v_\lambda=\frac{(\lambda,1)^T}{\sqrt{1+\lambda^2}}.
\]

Die höchste Austauschwahrscheinlichkeit der orthogonalisierten Labels beträgt nun

\[
\frac{4\lambda^2}{(1+\lambda^2)^2}.
\]

Sie ist bei lambda=1 gleich eins, bei lambda=2 dagegen 16/25, obwohl die Quelltheorie und ihr Energieinhalt unverändert sind. Der Austausch allein ist deshalb kein Beweis einer von der Quelle ausgewählten elementaren Paarumwandlung. Die Möbiusschranke 8/27 betrifft andere, festgehaltene Ausgangs- und Zielzustände und wird hier nicht widerlegt.

Die Polarabbildung ist eine Zustandsisometrie. Insbesondere beweist sie nicht

\[
\Phi(f_i^\dagger f_j^\dagger)=
\Phi(f_i^\dagger)\Phi(f_j^\dagger)
\]

auf einer gemeinsamen invarianten Domäne. Die bekannten nichtkanonischen OPEs der zusammengesetzten Randfelder und der lokale Paar-/Vermittler-Produktzusammenhang bleiben bestehen. Eine beliebige Fortsetzung von K_0 auf höhere Focksektoren würde neue Dynamik hinzufügen; sie wird hier nicht vorgenommen.

## 6. Ergebnis und Fortsetzungskriterium

Dieser Satz schließt im **festgehaltenen bedingten Randkandidaten** die gemeinsame endliche Zustands-/Zeitrekonstruktion des vollständigen Paar-plus-Vermittlerlabelraums im kontrollierten Grenzfall. Die zweite helle Kopie stammt aus vorhandenen Nachfahren; sie muss nicht als neuer physikalischer Oszillator eingeführt werden.

Der nächste Ursprungsschritt wird dadurch nicht zu einer Suche nach einem schöneren Zweierblock. Er muss die gemeinsame Quellenalgebra, ihren Zustand und ihren Generator aus den ursprünglichen Naht-/Transferdaten auswählen und ihre tatsächlichen Feldprodukte erhalten. Ein bloßer spektraler oder polarer Zustandsanschluss erfüllt das nicht. Die Herkunft von Gamma/Vaux sowie die räumliche 3+1D-Ausführung bleiben ausdrücklich offen. **Keines der physischen T1–T8-Gates ist geschlossen.**

## Belege und reproduzierbare Kontrollen

- Originale vollständige Paarantwort: `experiments/theory-contracts/source-pair-transfer-20260920/PROOF.md`, insbesondere Gleichungen (5)–(16).
- Tatsächliche Felder, signierter Tensor und Produktgrenzen: `experiments/theory-contracts/source-dressed-native-20260920/PROOF.md`.
- `joint_response_check.py`: exakte symbolische Kontrollen der neuen gemeinsamen Blockform, der Restfaktorisierungen, der Normierungskontrolle und der eingesandten Möbiusschranke sowie des zweiten Zeitjets. Normal- und optimierter Lauf liefern identische Ergebnisdateien.
- Standardgrundlage der Möbiusleiter: [Ojeda-Guillén et al., SU(1,1) and SU(2) Perelomov number coherent states](https://arxiv.org/html/1206.1555), Leiterrelationen und disentanglierte kohärente Zustände; hier k=1. Diese Literatur ist keine TFPT-Herkunftsherleitung.
- Standardrahmen der Gittervertexfelder: [Anagiannis et al., Vertex operator superalgebra/sigma model correspondences](https://arxiv.org/abs/2009.00186), Appendix B; konkrete Felder und Zeit werden durch die genannten lokalen Originalverträge festgelegt.

Experiments-Firewall: keine Paper-, Ledger-, empirische oder physische Promotion. Kein Beweisassistent wurde ausgeführt. Die unendlichen Aussagen beruhen auf dem ausgeschriebenen analytischen Argument.
