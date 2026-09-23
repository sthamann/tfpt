# TFPT: Rekonstruktion der Wechselwirkung und der nächste Quellenentscheid

21. September 2026 · Forschungsfortsetzung auf Grundlage des eingereichten Rekonstruktionssatzes

## Ergebnis

Der neue Ansatz trennt zwei vorher leicht vermischte Fragen: Die geometrische Residuenantwort bestimmt einen linearen Speicherkanal; eine gemischte Boson/Fermion-Antwort bestimmt dagegen die tatsächliche Paarwechselwirkung. Das ist ein geeigneter Ansatzpunkt für eine gemeinsame Quellenherleitung.

Die Fortsetzung liefert vier eng zusammenhängende Resultate:

1. Unter präzisen Fockraum- und Domänenvoraussetzungen kann die Annahme eines polynomialen Hamiltonoperators entfallen. Die unteren Antwortidentitäten erzwingen bereits eine endliche Umwandlungshierarchie; die gemischte Antwort wählt daraus den nativen W-Generator.
2. Nach den beiden unteren Operatorantworten genügt sogar ein einzelner positiver Übergangsfehler D_F am vollbesetzten Fermionzustand. D_F=0 bestimmt die gesamte Wechselwirkung; die volle gemischte Antwort muss dann nicht mehr separat vorausgesetzt werden.
3. Die vorhandenen Symmetrien, der native W-Tensor, die RR-Clock und sämtliche Prozesse bis Q=3 reichen noch nicht, diese gemischte Antwort zu erzwingen. Eine ausdrücklich eingegrenzte, stabile Vergleichsfamilie im selben nativen Operatorraum zeigt die erste zusätzliche Unterscheidung bei Q=4.
4. Der Anschluss an den Zustand wird konkret: Das leere kanonische Vakuum ist bei nichtverschwindender nativer Wechselwirkung kein Grundzustand. Ein unabhängig aus der Quelle gewählter globaler Grundzustand würde dagegen im bereits bewiesenen schwachen Kopplungsbereich die native Grundzustandslinie auswählen.

Damit ist ein stärkerer bedingter Rekonstruktionsweg verfügbar. Die aus P1/P2 unabhängig berechnete geladene Quellenantwort ist weiterhin nicht vorhanden. Eine vollständige TFPT-Lösung wird nicht behauptet.

## 1. Was am eingereichten Text übernommen und was unabhängig geprüft wird

Der Text enthält nicht auflösbare chatgpt-content-reference-Verweise auf externe Beweise und Prüfdateien. Diese Verweise gelten hier nicht als Ausführungsbeleg. Geprüft werden die angegebenen Gleichungen am vorhandenen nativen W-Tensor und durch eigene algebraische Argumente.

Der Tensor besitzt 64 Fermion- und 60 Bosonkanäle, 480 getragene reelle Einträge und WW†=8I₆₀. Seine SHA-256 lautet
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die Minimalitätsrechnung für den geometrischen Kern ist korrekt, sofern die genannten Momente auf dem gekoppelten Unterraum definiert sind. Aus
B†B=4Pᵤ, B†DB=8Pᵤ und B†D²B=16Pᵤ folgt für selbstadjungiertes D

\[
B^\dagger(D-2)^2B=0\quad\Rightarrow\quad(D-2)B=0.
\]

Die erreichbare verborgene Richtung ist eindimensional und hat den Wert 2. Zusammen mit dem bereits festgelegten sichtbaren Block und der Invarianz des restlichen Tripels ergibt sich die bekannte Zweiermatrix [[2,2],[2,2]]. Der Kern allein bestimmt nicht den gesamten sichtbaren Operator A oder völlig entkoppelte zusätzliche Richtungen.

Der Wert 2 ist ein Pol der Selbstenergie und eine Nullstelle der sichtbaren Mittelwertresolvente; die gekoppelten Eigenwerte sind 0 und 4. Der Anfangswert der ausgeblendeten Linie bleibt zusätzliche Zustandsinformation. Diese Aussagen sind kein physischer Teilchen- oder Massennachweis.

## 2. Der dynamische Fingerabdruck

Auf dem gemeinsamen endlichen Teilchenkern lauten die drei Antwortfamilien

\[
\mathcal F_{ij}(H)=\{[f_i,H],f_j^\dagger\},\qquad
\mathcal B_{AB}(H)=[[b_A,H],b_B^\dagger],
\]
\[
\Gamma_{Aij}(H)=\{[[b_A,H],f_i^\dagger],f_j^\dagger\}.
\]

Für

\[
H_W=\Delta N_b+gX+\bar gX^\dagger,\qquad
X=\sum_A b_A^\dagger P_A,\quad
P_A=\sum_{i<j}W_{A,ij}f_jf_i
\]

gilt exakt

\[
\mathcal F_{ij}=0,\qquad
\mathcal B_{AB}=\Delta\delta_{AB}I,\qquad
\Gamma_{Aij}=gW_{A,ij}I.
\]

Die Antikommutatoren sind wesentlich. Dies sind Operatoridentitäten; weder ein passender Erwartungswert noch ein passendes Spektrum ersetzt sie.

Ist die volle skalare Antwort unabhängig vorhanden, ergibt sich

\[
g=\frac1{480}\sum_{A,i<j}\overline{W_{A,ij}}\,\Gamma_{Aij}.
\]

Zusätzlich müssen sämtliche W-orthogonalen und nichtskalaren Beiträge verschwinden. Aus dem Zielmodell berechnet ist diese Gleichung eine Identität, kein Herkunftsnachweis für g.

Für allgemein skalare untere Antworten ε_f und ε_b ist die relative Umwandlungsenergie δ=ε_b−2ε_f. Das Verhältnis g/δ ist, sofern δ≠0, unter gemeinsamer Energieskalierung sowie Addition μQ unverändert. Die Addition μQ ist damit nicht als physisch bedeutungslos erklärt: Sie verändert geladene Energien und kann die globale Grundzustandswahl ändern. Insbesondere ist der zitierte native Grundzustandssatz auf ε_f=0 und ε_b=Δ festgelegt.

## 3. Verstärkung: Die Polynomannahme ist unter vollen Fockvoraussetzungen entbehrlich

Verwendet wird der volle irreduzible Fockraum endlich vieler kanonischer Boson- und Fermionmoden, ohne unbeobachteten Zusatzfaktor. H sei selbstadjungiert und reduziere die Sektoren von Q=N_f+2N_b. Alle Klammeridentitäten gelten auf dem invarianten endlichen Teilchenkern. Jeder Q-Sektor ist endlichdimensional.

Nach Abzug von ε_fN_f+ε_bN_b erzwingt die erste Antwortidentität, dass keine normalgeordneten Fermionwörter mit gleichzeitig Erzeugern und Vernichtern übrig bleiben. Die Fermionalgebra ist endlichdimensional; dieser Schritt setzt kein Polynom in den Bosonoperatoren voraus.

Für einen verbleibenden bosonischen Koeffizienten T mit positiver Zahlverschiebung m liefert die zweite Antwortidentität

\[
[N_b,T]=mT,\qquad [[b_A,T],b_B^\dagger]=0.
\]

Setze U_A=[b_A,T]. Dieser Operator kommutiert mit allen Erzeugern und ist deshalb auf dem Teilchenkern durch U_A|0⟩ bestimmt. Dieser Vektor hat Bosonzahl m−1. Also ist U_A ein homogenes Erzeugerpolynom G_A(b†) vom Grad m−1. Die Jacobiidentität liefert ∂_AG_B=∂_BG_A. Das Polynom

\[
F(b^\dagger)=\frac1m\sum_A b_A^\dagger G_A(b^\dagger)
\]

besitzt dieselben Kommutatoren mit allen Vernichtern wie T. Der Rest T−F kommutiert mit allen Vernichtern und erhöht die Zahl um m>0; eine Induktion über die Eingangs-Bosonzahl erzwingt T−F=0. Negative Verschiebungen folgen durch Adjunktion; bei Verschiebung null bleibt eine Konstante.

Damit ist die vollständige verbleibende Hierarchie bereits von der Form

\[
H=cI+\epsilon_fN_f+\epsilon_bN_b+
\sum_{m=1}^{32}\sum_{|\alpha|=m,\ |I|=2m}
\left[C_{\alpha I}(b^\dagger)^\alpha f_I+\mathrm{h.c.}\right].
\]

Die Grenze 32 folgt aus 64 Fermionmoden und der erhaltenen Ladung, nicht aus einer vorher angesetzten kubischen Abschneidung. Die skalare gemischte Antwort setzt alle m≥2-Koeffizienten auf null und wählt bei m=1 genau gW.

Die Domänen- und Vollständigkeitsvoraussetzungen tragen den Satz. Eine endliche Bosonbesetzungs-Abschneidung erfüllt die exakten CCR am oberen Rand nicht. Ohne irreduzible vollständige Feldalgebra ist der unbeobachtbare Rest außerdem größer als cI: H_W⊗I+I⊗D besitzt dieselben drei Antworten auf den sichtbaren Feldern für beliebiges D. Eine globale Quellen- oder Zustandsrekonstruktion folgt daraus nicht.

### Ein einzelner vollbesetzter Übergang bestimmt den verbleibenden Generator

Sei F der normierte Zustand mit allen 64 Fermionmoden besetzt und keiner Bosonbesetzung. Setze v=XF; der tatsächliche native Tensor liefert exakt ||v||²=480. Definiere

\[
E_F=\langle F|H|F\rangle,\qquad
g_F=\frac{\langle v|H|F\rangle}{480},
\]
\[
\boxed{D_F(H)=\|(H-E_F)F\|^2-
\frac{|\langle v|H|F\rangle|^2}{480}\ge0.}
\]

Der erste Term ist die Energievarianz, der zweite der Anteil in der bekannten Paar/Boson-Richtung v. D_F ist das Normquadrat des übrigen Übergangs. Nach den beiden unteren Operatoridentitäten gilt unter den genannten vollen Fock- und Domänenvoraussetzungen exakt

\[
D_F=0\quad\Longleftrightarrow\quad
H=cI+\epsilon_fN_f+\epsilon_bN_b+g_FX+\overline{g_F}X^\dagger.
\]

Der Beweis benutzt die oben klassifizierte Hierarchie: Jeder vorwärts gerichtete Term erzeugt aus F einen eindeutig markierten Bosonen-/Lochzustand. Verschiedene (α,I) ergeben orthogonale Zustände. Alle adjungierten Terme vernichten F wegen des Bosonvakuums. Deshalb bestimmt H|F⟩ jeden verbleibenden Koeffizienten. Ein verschwindender Projektionsrest setzt alle m≥2-Koeffizienten auf null und bindet die m=1-Koeffizienten an g_FW. Auch c folgt aus E_F−64ε_f, wenn E_F aus der Quelle bekannt ist.

Dies ist stärker als eine notwendige Bedingung: In der präzise angegebenen Klasse ist es ein hinreichender Rekonstruktionssatz. Für den gesuchten wechselwirkenden Zweig ist zusätzlich g_F≠0 nötig; D_F=0 allein lässt den freien Fall g_F=0 zu.

Die gemischte Antwort liefert eine zweite, gewichtete Form desselben Tests:

\[
E_\Gamma(F;g)=\sum_{A,i<j}\|(\Gamma_{Aij}-gW_{Aij})F\|^2
=\sum_{m=1}^{32}m^2(2m-1)
\sum_{|\alpha|=m,\,|I|=2m}\alpha!\,|D_{\alpha I}|^2.
\]

Hier ist D_{αI}=C_{αI}−gW_{Aij} für m=1 und D_{αI}=C_{αI} für m≥2. Der Gewichtsfaktor folgt aus Σ_A α_A²(α−e_A)!=mα! und der Zahl der Fermionpaare, binom(2m,2)=m(2m−1). Alle Gewichte sind strikt positiv. Nach den unteren Operatoridentitäten genügt daher dieser eine Prüfzustand, obwohl er die gesamte Operatoralgebra nicht trennt.

**Herkunftsgrenze:** F ist ein algebraischer Prüfzustand, kein behaupteter Weltanfang und keine bereits bewiesene native Präparation. H, die kanonischen Quellenfelder, die beiden unteren Operatoridentitäten, D_F und g_F müssen unabhängig aus derselben Quelle gewonnen werden. Der Quellenwert von D_F und der physische Kopplungswert wurden hier nicht berechnet. Das leere Vakuum würde die höheren Umwandlungen übersehen und kann F in diesem Satz nicht ersetzen.

### Eine endliche, aber nicht automatisch kleine Nachweisaufgabe

Jeder Koeffizient C_{αI} ist durch das direkte Matrixelement zwischen einem reinen 2m-Fermionzustand und einem reinen m-Bosonzustand bestimmt, mit dem bekannten Faktor √(α!). Unter den unteren Antwortidentitäten reichen deshalb prinzipiell die Sektoren Q≤64, um sämtliche verbleibenden Wechselwirkungen zu unterscheiden. Das ist eine strukturelle endliche Schranke; die Zahl der Matrixelemente ist sehr groß und wird nicht als bereits ausgeführte Vollprüfung ausgegeben.

## 4. Warum der erste neue Quellentest bei vier Ladungseinheiten liegt

Um zu prüfen, ob die gemischte Antwort schon aus den vorhandenen Symmetrien folgt, wird ausschließlich als Gegenprobe betrachtet

\[
H_\eta=H_W+\eta(X^2+X^{\dagger2}),\qquad\eta\in\mathbb R.
\]

Dies ist keine vorgeschlagene Änderung des TFPT-Hamiltonoperators. X ist bereits ein Skalar der nativen inneren Gruppenwirkung und kommutiert mit Q und der vorhandenen RR-Clock K. Dasselbe gilt deshalb für X². Die Vergleichsfamilie erhält die gleichen Symmetrien und beide unteren Antwortidentitäten.

X² vernichtet vier Fermionen und erzeugt zwei Bosonen. Sein Adjungiertes tut das Umgekehrte. Daher verschwindet der Zusatz exakt in allen Sektoren Q≤3. Die gesamte dort bekannte Austauschdynamik kann ihn nicht erkennen. Auch die gemischte Antwort auf dem leeren Vakuum sieht den höheren Beitrag nicht.

Bei Q=4 entsteht dagegen bereits ein direkter Übergang zwischen vier Fermionen und zwei Bosonen, den H_W in einem einzelnen Hamiltonschritt nicht besitzt. Für zwei disjunkte getragene Paare derselben W-Zeile ergibt die gemischte Antwort einen nichtverschwindenden Übergang zwischen dem verbleibenden Fermionpaar und einem Boson. Seine Normierung wird im beigefügten exakten Test am tatsächlichen W bestimmt.

Die neue unabhängige Rechnung am tatsächlichen W ergibt

\[
\|X^2F\|^2=106560\cdot4+1680\cdot2!\cdot4=439680,
\]
\[
D_F(H_\eta)=439680\eta^2,\qquad
E_\Gamma(H_\eta;F)=5276160\eta^2.
\]

Für jedes η≠0 ist der Fehler strikt positiv. Das ist eine gezielte Kontrolle, dass der neue Satz genau die vorher unsichtbare Freiheit erkennt. Es wurde keine vollständige Q=64-Matrix aufgebaut. Der direkte Hamiltonübergang beginnt bei Q=4; der Gamma-Zeuge kann Q=2 als äußeren Ein- und Ausgang haben, durchläuft aber Q=4 im Inneren des Klammerworts.

Die Familie ist kein bloß instabiles Gegenbeispiel. Mit C=∑ₐ||Pₐ||²≤3840 gilt

\[
|\langle X^2+X^{\dagger2}\rangle|\le C(2\langle N_b\rangle+60).
\]

Für hinreichend kleines |η|, etwa |η|<Δ/(4C), lässt sich der Zusatz zusammen mit dem linearen X-Term durch ΔN_b kontrollieren. Die sektorweise hermitesche direkte Summe ist selbstadjungiert und nach unten beschränkt. Das beweist keine gemeinsame räumliche Lokalität.

**Genauer Geltungsbereich:** Diese Familie widerlegt den Schluss von den ausdrücklich genannten Symmetrie-, Clock- und Q≤3-Daten auf die vollständige W-Dynamik. Sie wurde nicht als Gegenmodell zu allen TFPT-Bedingungen konstruiert; insbesondere muss sie weder denselben wechselwirkenden Grundzustand noch dessen gesamte höhere Antwort erhalten. Der neue gemischte Operator-Test unterscheidet sie gerade.

## 5. Der Zustandsanschluss kann nicht das leere Vakuum benutzen

Im Q=2-Sektor stehen ein normiertes natives Fermionpaar und ein Boson im Block

\[
H_2=\begin{pmatrix}2\epsilon_f&\sqrt8\,\bar g\\\sqrt8\,g&\epsilon_b\end{pmatrix}.
\]

Soll das leere kanonische Vakuum ein globaler Grundzustand sein, muss dieser Block nach Abzug seiner Vakuumenergie positiv sein. Notwendig sind daher

\[
\epsilon_f\ge0,\quad\epsilon_b\ge0,\qquad
2\epsilon_f\epsilon_b\ge8|g|^2.
\]

Im nativen Vertrag ε_f=0, ε_b=Δ>0 ist das bei g≠0 unmöglich. Dort hat der Block die negative Eigenenergie

\[
E_-=(\Delta-\sqrt{\Delta^2+32|g|^2})/2<0.
\]

Wenn die ursprüngliche Quelle einen physisch positiven Grundzustand vorgibt, können deshalb nicht zugleich alle identifizierten nativen Vernichter diesen Quellenzustand annihilieren. Die Quelle muss den wechselwirkenden Zustand und das passende Feldwörterbuch gemeinsam tragen.

Es gibt einen positiven bedingten Anschluss: Der bestehende native Grundzustandssatz liefert bei ε_f=0, Δ>0 und 0<|g|/Δ≤1/20 eine eindeutige globale Spin(10)×SU(4)-invariante Grundzustandslinie Ω mit Q=64. Wenn eine unabhängig hergeleitete volle Quellenabbildung die drei Antworten und die globale Grundzustandseigenschaft transportiert, muss sie diese Linie treffen. Der native Zustand wäre dann nicht mehr separat zu wählen. Die Quellenabbildung, ihr Kopplungswert und die Grundzustandseigenschaft sind jedoch Voraussetzungen dieses Schlusses. Ein kosmologischer Anfangszustand oder das vollständige T8-Funktional folgt daraus nicht.

## 6. Der vorhandene positive Quellenbestand und die erste fehlende Gleichung

Die bestehende affine E8-Rechnung liefert echte normierte Vakuum-Stromantworten und einen durch Wardbedingungen festgelegten kubischen Tensor. Die native 3+2-Markierung korrigiert im vorhandenen Anschluss den vollständigen Austauschtyp. Diese Resultate bestimmen relative algebraische Koeffizienten und Vorzeichen; sie sind kein Beleg dafür, dass die ursprüngliche physische Zeit einen kanonischen Bosonoperator in genau das native Fermionpaar überführt.

Die fehlende Gleichung ist, nach Konstruktion eines gemeinsamen graduierten Feldwörterbuchs,

\[
\Pi_{\Psi\Psi}[\mathcal B_A,H_{\rm Quelle}]
=g\sum_{i<j}W_{A,ij}\Psi_j\Psi_i,
\]

zusammen mit dem Ausschluss weiterer operatorwertiger gemischter Antwortanteile. Eine radiale Drei-Strom-OPE, eine Wurzelklammer und ein Hamilton-Kommutator auf kanonischen Feldern sind verschiedene Objekte. Ihr Zusammenhang muss bewiesen werden.

Ein linear auf kanonischen Bosonen wirkender Clocklift hat bei mit den Fermionen kommutierenden Bosonen Γ=0. Die neue Residuen-Rückwirkung ändert daran allein nichts. Die bereits bekannten Ausschlüsse des freien Quellenersatzes, der festen falschen Zentralwirkung und des Hodge-Klebungswechsels werden durch den Rekonstruktionssatz nicht aufgehoben und nicht als neue Entdeckungen gezählt.

Der nächste belastbare Herkunftsnachweis muss daher die gemischte Antwort aus den unabhängig definierten Quellenfeldern und ihrer tatsächlich ausgewählten Zeit berechnen. Alternativ genügen nach bewiesenen unteren Operatoridentitäten die unabhängigen Quellenwerte D_F=0 und g_F≠0. Dabei ist Q=4 der erste zusätzliche Entscheidungstest gegenüber den bisher untersuchten niedrigen nativen Austauschsektoren. P1/P2 werden nicht um einen passenden kubischen oder höheren Hamiltonterm ergänzt, um anschließend dessen Herkunft zu behaupten.

## 7. Reichweite für die Gesamtlösung

Rekonstruktion aus vollständigen Antworten ist eine eigenständige mathematische Aufgabe. Sie setzt verfügbare Antworten und eine spezifizierte Operatoralgebra voraus. Auch die einschlägige Literatur zur Hamiltonrekonstruktion arbeitet mit solchen Strukturannahmen; etwa Qi und Ranard behandeln die Rekonstruktion lokaler Hamiltonoperatoren aus Zustandskorrelationen in einer vorgegebenen Klasse, nicht die voraussetzungslose Erzeugung der Felder ([Originalarbeit](https://arxiv.org/abs/1712.01850)). Der vorliegende Fockraum-Satz wird durch die hier ausgeschriebenen Argumente begründet, nicht aus dieser Literatur zitiert.

Die Fortschrittskette lautet jetzt präziser: unabhängig definierte geladene Quellenfelder und Zeit → zwei untere Operatorantworten und D_F=0 (oder die vollständige gemischte Antwort) → nativer Generator; bei zusätzlich unabhängig begründeter Grundzustandseigenschaft und passendem Kopplungsbereich → native Grundzustandslinie. Die erste Quellenimplikation ist weiterhin offen.

Die physischen T1–T8-Gates bleiben offen. Insbesondere werden Raumzeitdimension, chirales Eichmaß, wechselwirkendes Kontinuum, vollständige Kopplungsherkunft, Quantengravitation und kosmologischer Anfangszustand nicht durch einen endlichen Rekonstruktionssatz ersetzt. Es erfolgt keine Ledger- oder Paper-Promotion.
