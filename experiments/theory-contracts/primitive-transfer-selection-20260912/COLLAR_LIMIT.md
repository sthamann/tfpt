# Der punktförmige v331-Collar: exakter Grenzübergang und Reparaturgrenze

12. September 2026. Diagnose der konkret implementierten Familie, kein
allgemeiner Ausschluss eines TFPT-Collars und keine globale TOE-Aussage.

## Ergebnis

Die endliche Fouriermatrix aus `verification/v331_necessity_of_H.py` ist
berechenbar und positiv. Ihre rohe Interpretation als quadratische Form
eines kontinuierlichen |D|-Operators mit positiven Punktbeiträgen ist jedoch
**nicht abschließbar**. Das wird unten durch eine explizite Folge glatter
Testfunktionen bewiesen.

Die naheliegende positive Fourier-Cutoff-Konstruktion besitzt dennoch einen
klaren Normresolventengrenzwert: **den freien Operator |D|**. Die zusätzlichen
Punktmarkierungen verschwinden in diesem Grenzwert. Das gilt sogar für jede
Cutoff-abhängige nichtnegative gemeinsame bloße Punktkopplung.

Damit ist der konkrete Grenzübergang entschieden, nicht nur numerisch
verdächtig. Ein nichttrivialer kontinuierlicher Transfer benötigt eine
anders begründete Regularisierung/Domäne. Eine feste glatte Breite liefert
eine wohldefinierte positive Familie, wählt aber ihre eigene Breite und
Kopplung nicht aus.

## 1. Exakt identifizierte Quelle

Quellhash (Datei unverändert):
`5dee9560ad3ca3a6b19984e251bcdbba65b8b645d188f1f0296bfe7a182e041b`.

Die Funktion `dtn(mark_angles, M=14, eps=0.4)` baut

    Lambda_M[k,l] = |k| delta_kl
                   + eps sum_(j=0)^3 exp(-i(k-l) theta_j),
    theta_j = j*pi/2, -M <= k,l <= M.

Somit ist die Markierungsmatrix exakt 4 bei k-l in 4Z und sonst null.
Die Quellfunktion wird im Prüfer aus ihrem eingesehenen Syntaxbaum isoliert
ausgeführt, ohne den restlichen Verifier zu importieren oder zu verändern.
Bei M=4,8,14 wird ihre Ausgabe mit der exakten Formel verglichen.

Das ist die Diagnose dieser Fourier-/Punktpotentialformel. Die Bezeichnung
„Dirichlet-to-Neumann“ im Quelltext ersetzt keinen Beweis, dass sie der
tatsächliche DtN-Operator einer hergeleiteten glatten Randgeometrie ist.
Die endlichen Z4-Kommutatorkontrollen bleiben davon unberührt.

## 2. Nichtabschließbarkeit der rohen Form

Arbeite auf L2(S1,dtheta/(2pi)) mit e_k(theta)=exp(ik theta). Für
trigonometrische Polynome lautet die wörtliche Quellform

    q(f)=sum_k |k| |fhat_k|^2 + eps sum_j |f(theta_j)|^2,
    eps>0.

Sei h_N=sum_(n=1)^N 1/n und definiere das glatte Polynom

    f_N(theta)=(1/h_N) sum_(n=1)^N cos(4n theta)/n.

Alle vier markierten Punktwerte sind exakt 1. Zugleich gilt

    ||f_N||_2^2 = [sum_(n=1)^N 1/n^2]/(2 h_N^2) -> 0,
    q_0(f_N) = 2/h_N -> 0,
    q(f_N)=2/h_N+4 eps -> 4 eps >0.

Für M>=N haben die Differenzen an allen vier Punkten Wert null und

    q(f_N-f_M)=q_0(f_N-f_M)=2/h_N-2/h_M ->0.

Die Folge ist also q-Cauchy und konvergiert in L2 gegen null, aber ihre
q-Energie konvergiert nicht gegen null. Dies verletzt genau das Kriterium
für Abschließbarkeit einer positiven quadratischen Form.

Die Beschränkung auf den Z4-invarianten Unterraum hilft nicht: Jedes f_N
ist selbst bereits Z4-invariant. Die Schwierigkeit liegt bei der kritischen
Punktauswertung im H^(1/2)-Formraum, nicht bei einer verlorenen Uhrsymmetrie.

Der algebraische Beweis gilt für alle N. Die endlichen rationalen Tests
bestätigen seine Formeln; sie ersetzen den Grenzbeweis nicht.

## 3. Trotzdem existiert ein natürlicher Cutoff-Grenzwert – und ist frei

Um verschiedene Cutoffs auf demselben Raum zu vergleichen, setze A=|D|
auf l2(Z), und lasse V_M:C4->l2(Z) die vier Spalten

    (V_M)_(k,j) = 1_(|k|<=M) exp(-ik theta_j)

enthalten. Die selbstadjungierten positiven Operatoren

    A_M=A+eps_M V_M V_M*, eps_M>=0,

stimmen auf dem Fourier-Cutoff mit der Quellmatrix überein und wirken auf
dem orthogonalen Komplement frei. Dies ist eine ausdrücklich festgelegte
Einbettung der endlichen Matrizen, keine beliebige Interpolation.

Betrachte z=-1, also R=(A+I)^(-1), und zunächst eps_M>0. Die endliche
Woodbury-Identität liefert auf dem ganzen Hilbertraum

    (A_M+I)^(-1)-R
      = -R V_M (eps_M^(-1) I + G_M)^(-1) V_M* R,
    G_M=V_M* R V_M.

G_M wird durch die vierdimensionale diskrete Fouriertransformation
diagonalisiert. Seine Eigenwerte sind, bis auf die Reihenfolge,

    g_(r,M)=4 sum_(|k|<=M, k congruent r mod4) 1/(|k|+1), r=0,1,2,3.

Alle vier divergieren logarithmisch. Eine ausdrückliche gemeinsame Schranke
für M>=7, N=floor((M-3)/4), ist

    min_r g_(r,M) >= sum_(n=1)^N 1/(n+1) = h_(N+1)-1 -> infinity.

Denn jede Restklasse enthält die positiven k=4n+r für n=1,...,N, und
4/(4n+r+1)>=1/(n+1).

Außerdem ist gleichmäßig in M

    ||R V_M||^2 <= ||R V_M||_HS^2
      = 4 sum_(|k|<=M) 1/(|k|+1)^2 <= 12.

Daraus folgt die echte unendliche Normschranke

    ||(A_M+I)^(-1)-(A+I)^(-1)||
      <= 12/[eps_M^(-1)+h_(N+1)-1]
      <= 12/[h_(N+1)-1] ->0.

Für eps_M=0 ist die Differenz exakt null. Somit gilt der freie Grenzwert
für JEDE nichtnegative gemeinsame Kopplungsfolge, auch wenn sie wächst.
Das ist stärker als eine Extrapolation des Quellwerts eps=0.4.

Die scharfen endlichen Differenznormen lassen sich ebenfalls mit nur vier
Summen berechnen:

    ||Delta R_M||=max_r b_(r,M)/(eps^(-1)+g_(r,M)),
    b_(r,M)=4 sum_(|k|<=M, k congruent r mod4) 1/(|k|+1)^2.

Dies folgt aus derselben Fourierdiagonalisierung von V_M*R^2 V_M. Die
numerischen Werte bei eps=0.4 sinken langsam: etwa 0.446 bei M=16, 0.301
(genauer 0.30014) bei M=256 und 0.221 bei M=4096. Der allgemeine Beweis
steht jedoch in der Normschranke, nicht in dieser Tabelle.

## 4. Ein positiver wohldefinierter Ersatz – mit zusätzlichem Datum

Glätte die vier Punktmarkierungen mit einem Poissonprofil. Für 0<r<1 sei

    P_r(theta)=(1-r^2)/(1-2r cos(theta)+r^2),
    f_r(theta)=sum_j P_r(theta-theta_j).

f_r ist eine positive beschränkte Funktion mit
||f_r||_infinity <=4(1+r)/(1-r). Die Form

    q_r(f)=q_0(f)+eps integral f_r(theta)|f(theta)|^2 dtheta/(2pi)

ist abgeschlossen auf H^(1/2), weil ihr zweiter Term beschränkt und positiv
ist. Der Operator A+eps M_(f_r) ist selbstadjungiert auf H1, positiv und
hat kompakten Resolventen. Er kommutiert exakt mit der Viereruhr. Für festes
r sind damit Operator und Wärmetransfer mathematisch wohldefiniert.

Das ist ein positiver Existenzschritt für EINE DEKLARIERTE Ersatzfamilie,
nicht der Beweis ihrer Auswahl durch TFPT und nicht automatisch ein
geometrisch hergeleiteter DtN-Operator.

Ihre Fouriermatrix hat den Markierungsanteil

    4 eps r^|k-l| 1_(k-l in4Z).

Schon beim Cutoff M=2 enthalten die beiden äußeren Moden die Eigenwerte
2+4eps ±4eps r^4. r=1/3 und r=1/2 liefern unterschiedliche Spektren bei
identischer Uhrsymmetrie und Positivität. Diese endliche Unterscheidung
ist ein Kontrollbefund, kein daraus behaupteter universeller
Spektralsatz für die ganze unendliche Familie.

Die Glättungsbreite und ihre Herleitung sind somit echte zusätzliche
Informationen. Eine nichttriviale singuläre Punktwechselwirkung müsste
stattdessen durch eine eigene renormierte Konstruktion einschließlich
Domäne und Stabilität hergeleitet werden. Die positive nackte Cutoff-
Kopplung allein kann sie nach §3 nicht liefern.

Literaturkontext (keine ungeprüfte Übertragung von R^d auf S1):
Michelangeli und Scandone, *Point-like perturbed fractional Laplacians
through shrinking potentials of finite range*,
https://arxiv.org/abs/1803.10191 . Die hier benötigten Kreisaussagen sind
oben eigenständig hergeleitet.

## 5. Bedeutung für den Universalraum-Vorwärtstest

Dieser Befund erklärt nicht sämtliche TFPT-Hindernisse. Er schließt einen
konkreten, zuvor naheliegenden Transferweg aus: Die endliche positive
Punktmatrix darf nicht als bereits konstruierte nichttriviale kontinuierliche
Quelle übernommen werden.

Eine vollständige Lösung müsste nun aus den primitiven Daten entweder

- eine reale endliche Breite beziehungsweise Randgeometrie auswählen, oder
- eine kontrollierte renormierte Wechselwirkung mit festgelegter Domäne
  und Parametern erzeugen, oder
- einen anderen quellenseitigen Operator herleiten.

Der Existenznachweis der geglätteten Familie erledigt nur den mathematischen
Definitionsschritt. Seine physische Auswahl, ein H70-Anschluss und der
gemeinsame 3+1D-Ursprung bleiben offen. Keine Statusmarker geändert.

## 6. Prüfung und Herkunft

`collar_limit.py`: 47 Kontrollen, darunter rationale Testfolgenidentitäten,
direkter Vergleich mit der isolierten ORIGINAL-Quellfunktion, direkte
gegen Woodbury-Inversion sowie Glättungs-Gegenkontrollen. Fließkommatests
werden als solche ausgewiesen. Keine Behauptung, alle Kontrollen seien
exakt rationale Beweise. Die allgemeinen Beweise sind §§2–4.

Der Skill systematic-debugging führte hier zur Prüfung der Ursache und
zum direkten Quellvergleich vor einem Reparaturvorschlag. Die ursprüngliche
Datei und die öffentlichen Texte bleiben unverändert. Die alternative
Form wird nicht stillschweigend als ursprüngliche TFPT-Theorie ausgegeben.
