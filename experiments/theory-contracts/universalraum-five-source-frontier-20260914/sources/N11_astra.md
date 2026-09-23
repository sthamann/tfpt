# TFPT und Universalraum: verifizierter Stand und konstruktive Schließungen

**14. September 2026 · Forschungsbericht für Stefan Hamann**

Eigene mathematische Herleitungen und unabhängige endliche Rechnungen. Nicht extern begutachtet. Die neuen Sätze gelten in den hier festgehaltenen Modellen. Eine vollständige TOE, RH oder P gegen NP wird nicht als bewiesen ausgegeben. Keine Änderung eines ursprünglichen Repositorys, Ledgers oder Forschungsstatus.

## 1. Ergebnis

Der neue Stand besteht nicht mehr nur aus getrennten Beispielen für Austausch, Präparation und Gedächtnis. Der jüngste technische Bericht verbindet diese Aufgaben in einem ausdrücklich gewählten endlichen Operationsmodell. Seine wesentlichen Formeln lassen sich unabhängig reproduzieren.

Diese Fortsetzung schließt zusätzlich drei konkrete Teilfragen:

1. **Das niedrige Belegungsband des harten C16 Mikromodells ist bereits bei |t|/Δ ≤ 1/20 rigoros vom übrigen Spektrum getrennt.** Die nachgewiesene Trennung beträgt mindestens 2Δ/5. Dafür ist die früher verwendete, sehr grobe Bedingung ‖V‖ < Δ nicht erforderlich.
2. **Aus den bereits zugelassenen Austauschmessungen und dem Reset auf einen einfachen Produktzustand entsteht ein vollständiger Kanal mit genau Ω als stationärem Zustand.** Alle Anfangszustände konvergieren mit einer expliziten Fehlerschranke. Kein bereits präpariertes Ω Reservoir wird benötigt. Messung, Feedback und Reset bleiben echte physikalische Ressourcen.
3. **Die gemeinsame Aufzeichnungsoperation besitzt eine exakte Schaltungsform und eine explizite resonante Vermittlerrealisierung.** Gleichzeitig lässt sich beweisen, warum dieselbe Operation nicht durch bloßes Warten unter dem schwach gekoppelten, verstimmten Referenzhamiltonoperator entsteht.

Weitere Resultate sind ein exakter endlicher Schurvertrag für alle Vermittlerordnungen, eine konservative Restschranke für seinen energieabhängigen Kern, eine dyadische Grenze endlicher reiner Minusfilter, ein gemeinsamer ausgeglichener Echotest sowie eine konkrete Warnung vor nicht extensiver globaler Vermittlerteilung.

Der verbleibende Unterschied ist grundlegend: Eine mathematisch vollständig definierte Ausführung ist noch nicht die aus TFPT ausgewählte Naturdynamik. Insbesondere entstehen drei Raumrichtungen, chirale Materie, ihre Kopplungen und ein quantisierter Gravitationssektor nicht allein durch die Schließung der endlichen Laboraufgaben.

## 2. Quellen, Versionsordnung und wirkliche Prüfabdeckung

### 2.1 Die sieben Anhänge

| Kürzel | Datei | Rolle |
|---|---|---|
| A | Konsolidierte_Fortsetzung.md | Vollständiger C16 Koeffizient vierter Ordnung, mikroskopischer Stern, Singulettnumerik und Herkunftsgrenzen |
| B | TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md | Globaler Normkandidat, ideale Amplitudenverstärkung, RH und Faktorisierung |
| C | TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf | Forschungsbuch mit 90 Seiten, einschließlich historischer Angaben |
| D | TFPT_Compiler_Universalraum_2026-09-14a_v1.2.pdf | Integriertes Compilerpaper, 35 Seiten |
| E | TFPT_GEMEINSAME_AUSFUEHRUNG_TECHNISCH_2026-09-14_v1.0.md | Nach dem PDF Export entstandene gemeinsame endliche Ausführung |
| F | TFPT_GEMEINSAME_AUSFUEHRUNG_2026-09-14_v1.0.md | Verständliche Zusammenfassung von E |
| G | TFPT_Compiler_Universalraum_2026-09-14_v1.2.pdf | Bytegleich mit D |

Die SHA256 Prüfung zeigt sieben Dateien, aber sechs unterschiedliche Dateiinhalte. Die beiden Compiler PDFs sind exakt identisch. E und F erklären ausdrücklich, dass sie nach dem PDF Export entstanden. Zwischen A und B wird keine unbelegte minutengenaue Reihenfolge konstruiert: Ihre Resultate werden sachlich und nach Ressourcenvertrag konsolidiert.

In D, Seite 31, steht noch, die gesamte C16 Dynamik vierter Ordnung sei nicht berechnet. A liefert genau diese spätere Anschlussrechnung. Im Buch C, physische Seite 25, ist die erste angeregte Singulettenergie noch als Dublett bezeichnet. Die neue eigene Rechnung findet vier orthogonale Eigenvektoren. Die alte Zweizellengrenze λ < 8J in C ist eine Grenze des damaligen Beweises, nicht ein nachgewiesener Übergang des Modells.

### 2.2 Tatsächlich ausgeführt

Der unabhängige Prüfer `verify.py` enthält **49 benannte Bedingungen**: 36 exakte, 12 numerische und eine hochpräzise numerische Bedingung. `algebra.py` ergänzt **20 exakte algebraische beziehungsweise endliche enumerative Bedingungen**. Die 69 Bedingungen sind weder 69 unabhängige Entdeckungen noch 69 physikalische Bestätigungen.

Separat rekonstruiert `spectrum.py` sämtliche 15 zulässigen Youngsektoren für acht Träger und den vollständigen 24.024 dimensionalen C16 Singulettmultiplizitätsraum. `extensions.py` prüft zusätzliche rationale Schranken, den ausgeglichenen endlichen Echotest und einen deklarierten kosmologischen Zahlenvergleich.

Normaler und optimierter Lauf mit `python -OO` wurden verglichen. Die Ergebnisdateien sind in dieser Laufumgebung bytegleich. Das gilt nicht als plattformübergreifende Zusage für letzte Gleitkommastellen.

Unabhängig rekonstruiert wurden insbesondere Wedge und Record auf 22 beziehungsweise 44 Dimensionen, die 256 dimensionale Materieausführung, die reguläre S4 Darstellung, die 60 Standardkontexte, E8 Wurzeln und Grade, alle 65.536 Ortsuntermengen des Clebsch Graphen, vier vollständige C16 Spalten der vierten Ordnung mit CAR und Bosonenpfaden, der 544 dimensionale mikroskopische Stern und die Singulettantwort von F4.

**Nicht als ausgeführt behauptet:** der originale phasenmarkierte TFPT Adapter, originale Quellpräfixprüfer, alle Jacobi Identitäten der nativen Klammer, Hardware, ein neuer vollständiger Renormierungsfluss, ein gemeinsamer empirischer Fit oder ein quantisierter Gravitationsgrenzwert. Ein zusätzlicher Versuch, alle 64 SU(4) Sektoren für 16 Träger numerisch zu durchsuchen, lief in die Ausführungszeitgrenze und lieferte kein verwendbares Gesamtergebnis. Deshalb wird kein neuer Ausschluss aller Nichtsingulettkonkurrenten behauptet.

## 3. Was gemeinsam feststeht und was getrennt bleiben muss

### 3.1 Mathematischer Kern

Die markierte diagonale Z4 Verklebung von D5 und A3 bleibt korrekt. Die Diskriminantenformen

\[
q_{D_5}(k)=5k^2/8,\qquad q_{A_3}(k)=3k^2/8
\]

addieren sich auf der Diagonale zu einer ganzen Zahl. Der Erweiterungsindex vier ergibt Determinante eins. Die korrekte graduierte Zerlegung lautet

\[
\mathfrak e_8=(45,1)\oplus(1,15)\oplus(10,6)
\oplus(16,4)\oplus(\overline{16},\overline4).
\]

Die eigene Wurzelenumeration ergibt 960 geordnete Wurzelsummen im Kanal 1+1 nach 2 und 832 im Kanal 1+3 nach 0. Die Gegenwurzelpaare mit Cartanziel sind davon begrifflich zu unterscheiden. Eine Prüfung der Wurzelgrade ersetzt keine erneute Prüfung der Originalphasen.

Für den festgelegten Prozess auf 60 Strahlen gilt

\[
T=\frac{C^\top BC+F^\top F}{28},\quad CC^\top=4I,
\quad FF^\top=12I,\quad CF^\top=0.
\]

Das Spektrum ist

\[
1^{[1]},\quad(3/7)^{[15]},\quad(2/7)^{[9]},
\quad(-2/7)^{[5]},\quad0^{[30]}.
\]

Die Größen 240, 60, 45 und 30 gehören zu verschiedenen Zustandsbeschreibungen und Zugriffsklassen. Sie sind keine konkurrierenden Dimensionen des Universums. Die Auswahl der Kontextgewichte bleibt ein zusätzliches Prinzip; Symmetrie allein legt 1/7 nicht fest. [A §§3.1, B §§2.1–2.2, D §§9–10]

### 3.2 History darf den Vertex nicht verändern

Ohne unterscheidende Farbaufzeichnung ist

\[
K|ab\rangle=|a\wedge b\rangle,\quad
K|ba\rangle=-|a\wedge b\rangle,\quad K^\dagger K=I-S.
\]

Orthogonale Records für `ab` und `ba` entfernen die Kreuzterme. Dann entsteht

\[
\widetilde K^\dagger\widetilde K=I-D_{\rm diag},
\quad D_{\rm diag}=\sum_a|aa\rangle\langle aa|.
\]

Der Rang steigt von sechs auf zwölf. Das ist kein gleichwertiger Ausdruck für denselben Austausch. Das allgemeine Reparaturkriterium aus A lautet

\[
L^\dagger L=K^\dagger K\quad\Longleftrightarrow\quad L=VK
\]

mit einer Isometrie auf dem Bild von K. Die zulässige Aufzeichnung erweitert den kohärenten Ausgang, ohne schon identifizierte Eingänge wieder auseinanderzuziehen. Die spätere Aufzeichnung der Symmetrieklasse P+ oder P− erfüllt diese Bedingung; sie speichert nicht die geordnete Farbe. [A §4; E §2]

### 3.3 Vier unterschiedliche Ressourcenverträge

**Statisches Mikromodell:** harte C16 Belegung, harmonische gemeinsame Vermittler, konstantes Δ und t. Dieses Modell besitzt eine energieabhängige virtuelle Dynamik und echte höhere Ordnungen.

**Kontrollierte gemeinsame Ausführung:** adressierte Vermittlungsoperationen, kohärentes Belegungsregister, lokale Ticks, Messung, Feedback und Reset. E spezifiziert einen 832 dimensionalen Laborträger mit höchstens einem gleichzeitig aktiven Vermittler.

**Ideales verstärktes Präparationsmodell:** B verwendet zusätzliche kohärente selektive Phasen und kontrollierte ideale Entwicklung. Zwei angepasste Verstärkungsschritte können dort exakt Ω erzeugen. Diese besondere Phase ist nicht automatisch eine endliche Cliffordoperation.

**Arithmetischer Zweig:** vollständige signierte Weilform beziehungsweise Eingabekodierung und effiziente Auslesekosten. Eine große positive Matrix des physikalischen Modells beantwortet diese Aufgaben nicht ohne einen richtigen Adapter.

Eine gemeinsame Quelle muss diese Verträge durch konkrete Abbildungen oder erklärte Steuerparameter verbinden. Ein Wechsel des Vertrags darf nicht als bloße Umbenennung durchgehen.

## 4. Neue Schließung: Bandtrennung bei |t|/Δ ≤ 1/20

### 4.1 Festgehaltenes Modell

Wir verwenden das harte endliche Modell aus A §5:

\[
H=\Delta N_b+t(B^\dagger+B),\qquad
B^\dagger=\sum_{e,A}b^\dagger_{r(e),A}K_{e,A},\quad
N_f+2N_b=16.
\]

Es gibt 16 Orte, 40 Kanten, zehn Vermittlertypen r und sechs innere Paarzustände pro Typ. Jeder Vektortyp wird von vier disjunkten Kanten getragen. Pro Ort ist höchstens ein Fermion erlaubt. Die normierten Vertexeinträge haben Betrag eins. Wir setzen Δ>0.

Qn bezeichnet genau n Bosonen. Dort sind 16−2n Orte besetzt und 2n Orte leer. P=Q0 hat Dimension

\[
d=4^{16}=4\,294\,967\,296.
\]

Der Raum ist trotz seiner Größe endlich. Es gilt PHP=0 und es werden nur benachbarte Bosonsektoren gekoppelt.

### 4.2 Bessere Blocknormen statt einer groben Gesamtnorm

Setze

\[
A_n=Q_{n+1}B^\dagger Q_n.
\]

Die exakte Enumeration aller 65.536 Ortsuntermengen liefert für eine Menge mit m Orten die maximal möglichen inneren Kantenzahlen

\[
L(m)=(0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40),
\quad m=0,\ldots,16.
\]

Somit sind für n=0,…,8

\[
L_n=L(16-2n)=(40,31,24,17,12,7,4,1,0).
\]

**Satz:**

\[
\boxed{\|A_n\|^2\le a_n^2
=2(n+1)\min(4,n+1)L_n.}
\]

Die acht Werte a0²,…,a7² lauten

\[
(80,248,432,544,480,336,224,64).
\]

**Beweis.** Verwende die normierte Bosonenbasis und für einen Belegungszustand das positive Gewicht

\[
p(\mathbf n)=\frac1{\sqrt{\prod_A n_A!}}.
\]

Beim Erzeugen eines Bosons hat der Matrixeintrag Betrag √(nA+1). Das Verhältnis von Zielgewicht zu Eingangsgewicht hebt diese Wurzel auf. Die gewichtete Spaltensumme ist daher höchstens die Zahl besetzter erlaubter Kanten, also Ln.

Beim Rückweg ergibt das inverse Gewichtsverhältnis pro besetzter Mode den Faktor nA. Für jedes innere Farbpaar existieren zwei geordnete Rückbelegungen. Im Ziel mit 2(n+1) Löchern können von den vier disjunkten Kanten desselben Vektortyps höchstens min(4,n+1) vollständig leer sein. Die gewichtete Zeilensumme ist deshalb höchstens

\[
2\min(4,n+1)\sum_A n_A=2(n+1)\min(4,n+1).
\]

Der gewichtete Schurtest liefert das Produkt beider Schranken für die quadrierte Norm. CAR Vorzeichen ändern die Betragsabschätzung nicht. Damit ist der Satz für den benannten harten Vertrag bewiesen, ohne die riesigen Matrizen aufzuzählen.

### 4.3 Ein rationales Zertifikat für den ganzen hohen Sektor

Setze ε=|t|/Δ und Q=I−P. Für ψ=Σn≥1ψn mit xn=‖ψn‖ gilt

\[
\frac{\langle\psi,QHQ\psi\rangle}{\Delta}
\ge \mathbf x^\top T_\epsilon\mathbf x,
\]

wobei Tε eine 8×8 Tridiagonalmatrix ist: Diagonale 1,…,8 und Nebendiagonale −εa1,…,−εa7.

Bei ε=1/20 besitzt Tε−(2/5)I die exakten LDL Pivots

\[
\frac35,\ \frac{17}{30},\ \frac{59}{85},\ \frac{484}{295},
\ \frac{4681}{1210},\ \frac{125986}{23405},
\ \frac{292286}{44995},\ \frac{5535436}{730715}.
\]

Alle sind strikt positiv. Für kleinere |ε| wird die untere quadratische Schranke auf den nichtnegativen xn nicht schlechter. Folglich

\[
\boxed{QHQ\ge\frac25\Delta Q\qquad (|t|/\Delta\le1/20).}
\]

Der kleinste numerische Eigenwert der Vergleichsmatrix bei 1/20 ist etwa 0,42420517. Der Beweis verwendet bewusst die schwächere exakte Schranke 2/5.

### 4.4 Konsequenz für H, nicht nur QHQ

Ordne die Eigenwerte von H aufsteigend. Der Minmaxsatz liefert aus PHP=0

\[
\lambda_d(H)\le0.
\]

Der Unterraum Q hat Kodimension d und minimale Rayleighenergie mindestens 2Δ/5. Deshalb

\[
\lambda_{d+1}(H)\ge2\Delta/5.
\]

Damit besitzt H genau d nichtpositive niedrige Eigenwerte, während alle übrigen mindestens 2Δ/5 betragen. Das niedrige Band und sein Komplement sind getrennt. Dieser Beweis umfasst als Bandbehauptung alle SU(4) Sektoren zugleich.

**Wichtig:** Nicht bewiesen ist dadurch die Eindeutigkeit des niedrigsten Zustands innerhalb dieses Bands. Ebenso ist 2Δ/5 nicht die viel kleinere Singulettlücke. Die Aussage zertifiziert auch keine Prozentgenauigkeit des führenden Austauschmodells. Die bisherige Wahl ε=1/640 aus B ist damit für die bloße endliche Bandtrennung nicht mehr erforderlich. Ein thermodynamisch größenuniformer Satz ist diese C16 Rechnung nicht.

## 5. Alle Vermittlerordnungen als exakter endlicher Schurvertrag

Die Blockstruktur liefert mehr als eine formale Störungsreihe. Für e=E/Δ≤0 und x=t/Δ setze

\[
Z_8(e)=(8-e)I,
\]

\[
Z_n(e)=(n-e)I-x^2A_n^\dagger Z_{n+1}(e)^{-1}A_n,
\quad n=7,\ldots,1.
\]

Die vorstehende Positivität sichert die benötigten Inversen. Die exakte niedrige Energiegleichung lautet

\[
\boxed{[-eI-x^2A_0^\dagger Z_1(e)^{-1}A_0]\psi_0=0.}
\]

Die Rekursion endet nach acht Vermittlersektoren. Sie ist eine vollständige Definition des energieabhängigen effektiven Problems, keine Behauptung, die riesigen Inversen vollständig numerisch ausgewertet zu haben.

### Eine explizite, aber noch grobe Restschranke

Definiere bei e=0

\[
\ell_8=8,\qquad \ell_n=n-x^2a_n^2/\ell_{n+1}.
\]

Bei x=1/20 sind alle positiv. Die ersten Werte sind ℓ1≈0,61019536, ℓ2≈1,59054031 und ℓ3≈2,63762227. Für e≤0 bleiben dies konservative Untergrenzen.

Mit a=1−e, b=2−e, D=A0†A0 und Y=A0†A1†A1A0 sei

\[
\Sigma^{[4]}(e)=-\frac{x^2}{a}D-\frac{x^4}{a^2b}Y.
\]

Zwei Resolventenidentitäten geben für den exakten Feshbachkern Σ(e)=−x²A0†Z1(e)⁻¹A0

\[
\|\Sigma(e)-\Sigma^{[4]}(e)\|
\le x^6a_0^2\left[
\frac{a_1^4}{a^2\ell_2^2\ell_1}
+\frac{a_1^2a_2^2}{a^2b\ell_2\ell_3}\right].
\]

Zur Herleitung schreibe Z1=aI−B mit B=x²A1†Z2⁻¹A1. Dann ist

\[
Z_1^{-1}-a^{-1}I-a^{-2}B=a^{-2}B^2Z_1^{-1}.
\]

Ferner ist Z2=bI−x²A2†Z3⁻¹A2, sodass der Austausch von Z2⁻¹ durch b⁻¹I mit x²a2²/(bℓ2ℓ3) beschränkt wird. Die äußeren A0 Faktoren liefern a0².

Bei x=1/20 und e≤0 ergibt sich die einheitliche Schranke

\[
\frac{49542517723}{753339283500}\Delta
\approx0,0657638846\Delta.
\]

Sie ist endlich und explizit, aber noch etwa 13,15J bei J=2t²/Δ. Sie zertifiziert somit **nicht** die innere Lücke. Außerdem ist dies eine Restschranke des energieabhängigen Feshbachkerns, nicht der Rest des kanonisch symmetrisch normalisierten Hamiltonoperators vierter Ordnung. Eine Vermischung dieser beiden Operatoren wäre ein neuer Fehler. Der etablierte allgemeine Rahmen für effektive Hamiltonoperatoren ist die Arbeit von Bravyi, DiVincenzo und Loss [W1].

## 6. Unabhängige Kontrolle der vollständigen vierten Ordnung

Für das feste Modell aus A lauten

\[
\mathcal D=M^\dagger M,\quad \mathcal C=NM,
\]

\[
H_{\rm eff}=-\frac{t^2}{\Delta}\mathcal D
+\frac{t^4}{\Delta^3}\left(\mathcal D^2-\frac12\mathcal C^\dagger\mathcal C\right)
+O(t^6/\Delta^5).
\]

Mit Ee=I−Se lautet der dort hergeleitete vollständige Koeffizient

\[
F_4=2\sum_e E_e
+\sum_{e<f,\ e\cap f\ne\varnothing}\{E_e,E_f\}
-2\sum_{e<f,\ r(e)=r(f)}E_eE_fT_{ef}.
\]

Tef vertauscht die ganzen disjunkten Paare. Die drei Summen enthalten genau 40, 160 und 60 Beiträge. Die 160 überlappenden Kantenpaare dürfen nicht durch den isolierten Vierkörperterm ersetzt werden.

Der neue unabhängige Prüfer konstruiert vier vollständige Matrixspalten einmal über CAR und unnormierte Bosonenpfade und einmal über diese Permutationsformel. Beide Rechnungen sind exakt gleich. Die größte geprüfte Ausgangsspalte hat 318 nichtverschwindende Komponenten. Das ist keine Enumeration aller 4^16 Spalten; der allgemeine Operatorbeweis liegt in A §5.

Die eigene Youngdarstellung liefert im vollständigen Singulettmultiplizitätsraum

\[
E_{0,s}/J=11,045398337068416,
\]

\[
E_{1,s}/J=11,56176212280256\ldots,
\]

mit vier orthogonalen gefundenen Zuständen am zweiten Niveau. Die Residuen der ersten fünf Vektoren sind kleiner als 3,1·10⁻¹⁴; die Orthogonalitätsabweichung der zehn berechneten Vektoren liegt unter 4,5·10⁻¹⁵. Dies bestätigt die Vierfachkorrektur numerisch, nicht intervallarithmetisch und nicht als algebraischen Multiplizitätssatz.

Weiter ergibt sich

\[
\langle0_s|F_4|0_s\rangle=555,4885003638358,
\]

während die vier projizierten angeregten Eigenwerte numerisch übereinstimmen bei 583,29203866638…. Daraus folgt für den verfolgten Singulettabstand

\[
\Delta_s/J=0,51636378573414+13,9017691513\epsilon^2+O(\epsilon^4).
\]

Bei ε=0,05 liefert der angezeigte Korrekturterm ungefähr 0,55111821J. Dieser Wert ist keine zertifizierte exakte Lücke des vollständigen Mikromodells. Die neue Bandtrennung und die noch offene innere Lückenfrage sind miteinander konsistent.

Der ebenfalls neu nachgerechnete 544 dimensionale mikroskopische Stern bestätigt

\[
\Delta_\star^{\rm mic}
=\frac{\sqrt{\Delta^2+24t^2}-\sqrt{\Delta^2+20t^2}}2.
\]

Bei Δ=1 und t=0,05 ist dies 0,00243396875137. Sein Grundzustand trägt nur etwa 0,9856429312 Gewicht im nackten voll besetzten Raum. Ein ideales Sternfilter darf deshalb nicht ohne Entkleidung oder Fehlerrechnung auf dieses angekleidete Spektrum übertragen werden.

## 7. Neue Schließung: ein vollständiger Feedbackkanal mit eindeutigem Ziel

### 7.1 Von bedingten Erfolgen zu einer unverwerfenden Ausführung

Der jüngste Bericht E verwendet

\[
K=P^-_{03}P^-_{02}P^-_{01},\qquad v_0=|0,1,2,3\rangle.
\]

Drei aufeinanderfolgende Austauschmessungen besitzen einen Erfolgszweig 111 mit Krausoperator K. Bei allen anderen Zweigen erlauben die bereits erklärten lokalen Messungen und Pauli Korrekturen einen Reset auf ρ0=|v0〉〈v0|.

Anstatt fehlgeschlagene Versuche nur zu verwerfen, wiederhole ohne Erfolgsselektion den Kanal

\[
\boxed{\mathcal E(\rho)=K\rho K^\dagger+
\operatorname{tr}[(I-K^\dagger K)\rho]\,\rho_0.}
\]

Der erste Term ist vollständig positiv. Der zweite ist ein positiver Messeffekt mit festem Ausgabezustand, also ebenfalls vollständig positiv. Beide Spuren summieren sich zu Trρ. Operativ sind alle acht Recordzweige enthalten: Erfolg bleibt erhalten, jeder Fehlschlag wird gemessen und zurückgesetzt.

### 7.2 Vollständiger Attraktorbeweis

Sei A=|Ω〉〈Ω|. Es gilt

\[
K\Omega=K^\dagger\Omega=\Omega,\qquad
\operatorname{tr}(A\rho_0)=1/24.
\]

Damit gilt exakt

\[
\operatorname{tr}[A\mathcal E(\rho)]
=\operatorname{tr}(A\rho)+
\frac1{24}\operatorname{tr}[(I-K^\dagger K)\rho].
\]

Das Zielgewicht nimmt bei jeder nicht vollständig erfolgreichen Eingabe zu. Der in E angegebene und hier exakt reproduzierte reguläre S4 Gramoperator besitzt außerhalb des Eigenraums zu eins den größten Eigenwert

\[
\beta=(9+\sqrt{17})/32\approx0,4100970508.
\]

Weil die reguläre Darstellung der Gruppenalgebra treu ist, gilt ihre polynomiale Identität auch in der Vierträgerdarstellung. Der Eigenraum zu eins ist dort genau die gemeinsame Antisymmetrie, also CΩ. Deshalb

\[
K^\dagger K\le A+\beta(I-A).
\]

Folglich

\[
\boxed{1-F(\mathcal E^m\rho)
\le r^m[1-F(\rho)],\qquad
r=1-\frac{1-\beta}{24}\approx0,97542071045.}
\]

Jeder stationäre Zustand muss F=1 haben und ist daher A. Alle Anfangszustände konvergieren zu A. Insbesondere reichen 556 Zyklen für eine garantierte Infidelität unter 10⁻⁶. Das ist eine konservative Schranke, kein behauptetes Optimum.

Dieser Kanal benötigt **kein Ω als Eingang und keinen Sprungoperator mit einem vorbereiteten Ω Reservoir**. Seine Zutaten sind die in E ohnehin zugelassenen Recordoperationen und der einfache Produktreset. Die allgemeine Idee dissipativer Zustandspräparation ist etabliert [W2]; die hier ausgeschriebene Rückkopplung und Schranke sind die konkrete Spezialisierung auf diesen Vertrag.

### 7.3 Was damit nicht behauptet wird

Das Weglassen von Messung und Feedback liefert weiterhin den anderen, unitalen Kanal, der das Ω Gewicht erhält. Dessen Fixalgebra bleibt 3876 dimensional. Beide Aussagen widersprechen sich nicht.

Die neue Attraktivität ist nicht die Behauptung, ein geschlossenes endliches unitäres System verliere Entropie. Der Controller, das Resetmedium und die ausgehenden Records tragen den Entropiehaushalt. Ohne deren Herkunft ist T8 als kosmologische Zustandsauswahl nicht geschlossen. Mit ihnen ist die endliche kontrollierte Präparationsaufgabe dagegen vollständig definiert und ihr stationäres Problem gelöst.

## 8. Neue Schließung und neue Grenze: Was die Aufzeichnungsoperation wirklich benötigt

### 8.1 Exakte Schaltungsform

Die Materieoperation aus E ist

\[
R=P_+\otimes I_2+P_-\otimes X.
\]

Mit einem Hadamard H am Record gilt exakt

\[
(I\otimes H)R(I\otimes H)
=I_{16}\otimes|0\rangle\langle0|
+S\otimes|1\rangle\langle1|.
\]

R ist somit ein im Recordbasiswechsel ausgeführter kontrollierter Ququart Swap. Kodiert man jeden Ququart als zwei Qubits, genügen zwei Fredkinoperationen mit gemeinsamem Steuerqubit. Jede lässt sich als CNOT, Toffoli, CNOT schreiben.

Die genaue Toffolirealisierung folgt aus der Phasenidentität

\[
4abc=a+b+c-(a\oplus b)-(a\oplus c)-(b\oplus c)
+(a\oplus b\oplus c)\pmod8.
\]

Die sieben Paritätsterme werden mit T beziehungsweise T† Phasen umgesetzt; die kubische Phase ist CCZ. Hadamards am Ziel erzeugen Toffoli. Damit besitzt R eine exakte obere Schranke von **14 Tartigen Phasenoperationen plus Cliffordoperationen**. Dies ist keine Minimalitätsbehauptung. Die benötigten Verbindungen zwischen den Trägern und die T Ressource werden ausdrücklich vorausgesetzt.

Die Nichtverfügbarkeit aus ausschließlich Cliffordoperationen, Stabilizerzuständen und Pauli Messungen bleibt richtig: R erzeugt am bekannten einfachen Eingang 13 nichtverschwindende Rechenbasisamplituden und erfüllt R(I⊗Z)R†=S⊗Z. Das ist keine Pauliabbildung. Der neue Schaltungsnachweis benennt die zusätzliche Ressource, statt sie als geometrische Umbenennung zu verstecken. [E §6; W3]

### 8.2 Warum der schwache statische Vermittler nicht genügt

Im statischen Zweiniveaukanal

\[
H_{22}=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix}
\]

ist die maximale Vermittlerbesetzung bei einem antisymmetrischen reinen Paareingang

\[
\boxed{p_{\rm med}^{\max}=\frac{4g^2}{\Delta^2+4g^2}.}
\]

Bei g=√2t und t/Δ=1/20 folgt exakt pmax=1/51. Die volle Umsetzung U0 verlangt dagegen eine vollständige Übertragung des antisymmetrischen Sektors. Deshalb kann sie aus diesem festgehaltenen H22 nicht durch bloßes Warten entstehen.

Die neue Bandtrennung sagt also nicht, die pulsierte Aufzeichnung sei automatisch im selben konstanten Betriebszustand vorhanden. Der Unterschied zwischen virtueller Vermittlung und resonantem Volltransfer ist dynamisch und quantitativ.

### 8.3 Explizite resonante Reparatur

Setze

\[
J_W=\begin{pmatrix}0&-W^\dagger\\W&0\end{pmatrix},
\quad J_W^\dagger=-J_W,\quad J_W^3=-J_W.
\]

Bei resonantem Zugriff Δ=0 erzeugt der hermitesche Hamiltonoperator Hrot=igJW für gτ/ℏ=π/2

\[
U_{\rm rot}=e^{\pi J_W/2}
=\begin{pmatrix}P_+&-W^\dagger\\W&0\end{pmatrix}.
\]

Mit der relativen Belegungsphase

\[
D=I_{16}\oplus(-I_6)=e^{-i\pi N_b}
\]

gilt UrotD=U0. Die Belegungskopie ist ebenfalls ein expliziter Puls:

\[
Q=\exp[-i\pi N_b\otimes(I-X)/2].
\]

Der Exponent ist π mal ein Projektor. Daher ergibt sich exakt Q=I16⊗I2⊕I6⊗X. Die Makrooperation U0QU0 reproduziert auf allen 44 Dimensionen den Record und führt den Vermittler zurück.

Das zentrale iI4 der Clock liefert auf beiden Ladung zwei Alternativen dieselbe Phase −1. Es ersetzt D gerade nicht.

### 8.4 Gemeinsamer kontrollierter Vertrag

Ein einziger ausdrücklich gesetzter Steuervertrag kann die schwache uniforme Dynamik und die adressierten resonanten Pulse derselben Wedgefamilie enthalten. Benötigt werden wählbare Detuningwerte, Kopplungsquadraturen, Kantenadressierung, relative Belegungsphase, Recordkopplung und initialisierte Register. Während eines adressierten Makros können die anderen Kanten abgeschaltet sein; der Vermittler kehrt vor dem nächsten Makro zurück.

Dies ist ein konstruktiver Anschluss auf der Ebene einer gemeinsamen **kontrollierten Modellfamilie**. Es ist weder ein Nachweis, dass alle Pulse unter einem unveränderten statischen H ablaufen, noch eine native Ableitung dieser Kontrollen aus der ursprünglichen endlichen Cliffordklasse. Eine autonome Programmuhr kann die Steuerfolge in ein größeres festes U kompilieren; das erklärt ihre Programmeingabe und den anfänglichen Ressourcenzustand noch nicht.

## 9. Präparation und Echo: konsolidierte Zahlen und zusätzliche Lösung

### 9.1 Der neueste endliche Vergleich ist reproduziert

Für K und v0 aus E ergeben sich bei acht Erfolgsrunden

\[
p_8=\frac{2932033221441}{70368744177664},
\qquad F_8=\frac{8796093022208}{8796099664323}.
\]

Damit ist F8≈0,9999992448795201, während die Ausbeute pro begonnenem Versuch ungefähr 1/24 bleibt.

Für die echte lokale Dreierzyklusmatrix C und dieselbe achtfache Schlussprüfung erhält die unabhängige Rechnung

| Größe | Wert |
|---|---:|
| Rückkehr, erhaltenes Record, bedingt | 0,9999992448795637 |
| Rückkehr, frisches Record, bedingt | 0,5312581678314172 |
| Grenzwert, erhalten, bedingt | 1 |
| Grenzwert, frisch, bedingt | 17/32 |
| Grenzwert, erhalten, pro angefangenem Versuch | 1/24 |
| Grenzwert, frisch, pro angefangenem Versuch | 17/768 |

Der lokale Tick verlässt den 24 dimensionalen Sektor verschiedener Farben. Die Rechnung benutzt daher den vollen 256 dimensionalen Materieraum. Die alten Rohwerte 27/512 beziehungsweise die idealen Werte mit vorgelagertem Erfolg 1/6 gehören zu anderen Protokollen.

### 9.2 Der ausgeglichene Vergleich passt ebenfalls in dieselbe neue Ausführung

Für einen lokalen unitären Tick A gilt am idealen Ω

\[
p_+(A)=\frac{16-|\operatorname{Tr}A|^2}{24},
\quad p_{\rm frisch}=p_+^2+(1-p_+)^2.
\]

C hat Spur eins und gibt 17/32. Z⊗I hat Spur null und gibt 5/9. Die auf dem lokalen Zweiqubitträger erlaubte CNOT Matrix hat Spur zwei. Sie liefert deshalb mit **demselben Austauschrecord R** den ausgeglichenen Grenzwert 1/2.

Die neue exakte endliche Rechnung bei acht Runden ergibt für diesen CNOT Tick

\[
p_{\rm frisch,8}
=\frac{68774458651737171666048091}{137548997119995860238729216}
\approx0,49999970986149234.
\]

Der erhaltene Wert bleibt 0,9999992448795637. Die unbedingten Grenzwerte lauten 1/24 und 1/48. Das ist ein neues benanntes Ticksetting innerhalb desselben Record und Filtervertrags, keine rückwirkende Änderung des Dreierzyklusversuchs.

### 9.3 Weshalb endliche reine Minusfilter nicht exakt werden können

Jeder endliche Ausdruck als Produkt von P−e=(I−Se)/2 besitzt in der Rechenbasis dyadisch rationale Einträge. Zugleich fixieren der Ausdruck L und sein Adjungiertes Ω.

Würde L|0123〉 exakt proportional zu Ω, erzwingt der erhaltene Überlapp

\[
L|0123\rangle=\frac1{\sqrt{24}}|\Omega\rangle
=\frac1{24}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)|\pi(0123)\rangle.
\]

Die nichtverschwindenden Einträge wären ±1/24 und damit nicht dyadisch. Das ist unmöglich. Dieser Satz betrifft endliche ausschließliche Minuszweigprodukte aus genau diesen Paarprojektoren und diesem Eingang. Er verbietet weder asymptotische Präparation noch die ideale exakte Amplitudenverstärkung mit zusätzlichen Phasen aus B.

## 10. Die skalierende Familie muss Vermittlerlokalität erklären

Eine konkrete Gegenprobe macht die Warnung aus A §12 quantitativ. Erweitere das Modell ausdrücklich auf M disjunkte Kanten, die alle denselben harmonischen Vermittlertyp teilen. Auf einem Produkt gleicher antisymmetrischer Paarzustände gilt Ee=2 und Tef=1. Dann ist

\[
H^{(2)}=-2M\,t^2/\Delta,
\]

während der ausgeschriebene Koeffizient vierter Ordnung

\[
F_4=4M-8\binom M2=8M-4M^2
\]

wird. Die Zahl gemeinsam vermittelter Cluster wächst quadratisch.

Dies beweist nicht, dass die volle exakte Energie in jedem Grenzprozess quadratisch wächst: Gerade die schwache Entwicklung kann mit M ihre Gleichmäßigkeit verlieren. Es beweist aber, dass eine feste globale Vermittlerbank nicht ohne Weiteres denselben lokalen extensiven Grenzwert hat wie Vermittlerkopien pro Zelle.

Eine ausdrücklich lokale Reparatur besteht aus lokalen Vermittlern pro Zelle oder Kante und kontrolliertem Transport mit beschränkter Reichweite. Dann muss man eine lokale Wechselwirkungsnorm statt einer mit der Gesamtzellzahl wachsenden Gesamtnorm kontrollieren. Die Wahl dieser Reparatur ist ein Architektureingang. Sie wählt keine Raumdimension und erzeugt keine masselosen Felder allein durch ihre Form.

## 11. Physikalische Zahlen: erneute Prüfung und aktuellerer Gegenvergleich

### 11.1 Alpha

Die eingefrorene Gleichung aus D liefert erneut

\[
\alpha^{-1}=137,03599921684071250353786030380388037\ldots.
\]

Die aktuell abgerufene offizielle NIST Tabelle der CODATA Anpassung 2022 nennt 137,035999177 mit Standardunsicherheit 0,000000021. Die Differenz beträgt in diesen experimentellen Einheiten 1,8971767859. Das ist eine genaue Formelreproduktion, keine neu hergeleitete Thomsonkopplung und keine Theoriefehlerrechnung. [W4]

Eine implizite Selbstkonsistenzgleichung ist mathematisch nicht verdächtig, nur weil α auf beiden Seiten steht. Die offene Frage bleibt, weshalb gerade diese Gleichung nach Renormierung, Schwellen und Schemaumrechnung die gemessene Kopplung liefern muss.

### 11.2 Inflation: nicht nur den alten Planck Vergleich fortschreiben

Der historische einfache Zweig besitzt

\[
n_s=1-2/N,\quad r=12/N^2,\quad
A_s=N^2c_3^7/(24\pi^2),\quad c_3=1/(8\pi).
\]

Daraus folgen ohne N

\[
r=3(1-n_s)^2,\qquad
A_s(1-n_s)^2=c_3^7/(6\pi^2).
\]

Der negative Befund bei festem N=51,4 widerlegt nicht automatisch das ganze Intervall N=50 bis 60. Setzt man As=2,10·10⁻⁹ ein, erhält man N≈56,13124 und ns≈0,96436922. As ist dann eine Kalibrierung, keine unabhängige Vorhersage. [D §7.3 und Nachtrag N6]

Der aktuelle Gegenvergleich dieser Prüfung nutzt ACT DR6, Version 2, Tabelle 5, Spalte P ACT LB2: die dort erklärte Kombination aus ACT, Planck, CMB Lensing und DESI DR2, innerhalb des Basismodells ΛCDM. Sie nennt ns=0,9752±0,0030 und log(10¹⁰As)=3,062 mit asymmetrischen Unsicherheiten. Es handelt sich nicht um ACT allein. [W5]

Kalibriert man den einfachen TFPT Zweig auf den zentralen As Wert dieser Spalte, folgen N≈56,62391, ns≈0,96467923 und r≈0,00374267. Der Unterschied im ns Zentralwert beträgt etwa 3,51 der tabellierten marginalen Standardunsicherheiten. Dies ist ausdrücklich **kein gemeinsamer Likelihoodtest**: Parameterkorrelationen, die Amplitudenunsicherheit, Theorieordnung und Reheating wurden nicht neu gefittet. Es ist eine relevante Spannung dieses festgehaltenen einfachen Zweigs, keine globale Widerlegung sämtlicher TFPT Varianten.

Historische Leptonverhältnisse, der ältere Higgszweig und Protonzerfallsbefunde bleiben als dokumentierte Probleme erhalten. Hier wurden keine neuen Schleifenrechnungen erfunden, um sie zu beseitigen. Der vollständige neue Neutrinofit wurde ebenfalls nicht durchgeführt.

## 12. TOE: Der gemeinsame Abschlussvertrag nach diesen Fortschritten

| Tor | Jetzt zusätzlich geschlossen | Noch erforderliche gemeinsame Konstruktion |
|---|---|---|
| T1 Quelle | Kohärenter Vertex, exakte Recordschaltung, ausdrücklicher kontrollierter Vermittleradapter | Native Auswahl von Träger, Statistik, globaler Geometrie, Zugriffen, Parametern und Anfangsdaten |
| T2 Naht | Korrekte E8 Grade und deutliche Trennung von endlicher Algebra und Dynamik | Phasentreuer analytischer Adapter mit demselben chiralen Grenzwert und kontrollierten Domänen |
| T3 Raumzeit | Keine falsche Gleichsetzung lokaler Dimensionen; explizite Lokalitätsanforderung | Eine ausgewählte skalierende Familie mit drei räumlichen Richtungen, kohärenten Propagatoren und gemeinsamem Lorentzkegel |
| T4 Materie | Ladungszuordnungen und historische Anomaliesummen bleiben korrekt im gesetzten Wörterbuch | Drei propagierende chirale Familien, Spiegelentkopplung, Fermionmaß und tatsächliche Eichdynamik |
| T5 Dynamik | Bandtrennung bis ε=1/20, exakter Schurvertrag, kontrollierter endlicher Kernelrest, unabhängige F4 und Singulettrechnung | Enge Kontrolle des inneren Gaps, alle konkurrierenden Sektoren, lokaler wechselwirkender Vielzellen und Kontinuumsgrenzwert |
| T6 Parameter | Alpha reproduziert; Inflation auf einem benannten neueren Datensatz gegengeprüft | Gemeinsamer Transfer von Eichkopplungen, Yukawas, Neutrinos und Skalen mit Theorieunsicherheit |
| T7 Gravitation | Kein neuer Abschluss behauptet | Positiver masseloser Spin zwei Pol, physische zwei Helizitäten, Ward Identitäten, universelle Kopplung und quantisierter Grenzwert |
| T8 Zustand | Konkreter Feedbackkanal mit eindeutigem Ω Attraktor und quantitativer Konvergenz | Herkunft von Resetumgebung, Controller, kosmischer Randbedingung und großskaligem Zustandsfunktional |

### 12.1 Materie und Chiralität

Die konkrete E8 Gittererweiterung liefert nicht allein die volle vierdimensionale Materiedynamik. Ein chiraler Rand in 1+1 Dimensionen und propagierende Standardmodellfelder in 3+1 Dimensionen sind verschiedene Aufgaben.

Die in den Quellen genannte neue Arbeit von Araki und Mitautoren ist als Preprint vom 30. August 2026 tatsächlich vorhanden. Sie untersucht ein zweidimensionales euklidisches Gitter und zeigt in ihrer Simulation ein gezieltes Gappen der Spiegelwand. Das ist ein nützlicher Mechanismustest, kein vierdimensionaler Standardmodellabschluss. [W6]

Drei Familien benötigen beispielsweise drei interne Nullmoden χa eines konkret abgeleiteten Operators, sodass Ψ(x,y)=Σaψa(x)χa(y)+massive Moden tatsächlich drei unabhängige vierdimensionale Felder trägt. Ein Raumzeitinstanton mit Index drei zählt nicht automatisch drei Familien. Auch ein interner Nettoindex drei schließt zusätzliche vektorartige Paare nicht allein aus. Diese Präzisierung stammt aus A §10.3 und bleibt gültig.

### 12.2 Gravitation und kosmologischer Zustand

Die Identität det(tI+x·σ)=t²−|x|² ist eine kinematische Verbindung, kein Nachweis eines dynamischen metrischen Feldes. Ein tatsächlicher Gravitationskandidat muss aus derselben Mikrodynamik einen physikalischen Korrelator mit positivem masselosem Spin zwei Pol liefern, die unphysikalischen Komponenten entfernen und die universelle Kopplung zeigen. Die Spektralwirkung kann ein Ziel organisieren; ein eingesetzter Diracoperator ist nicht seine eigene Herleitung. [A §§10.1–10.4]

Dunkle Materie braucht einen stabilen, entsprechend gekoppelten Sektor samt Produktion; ein ungelesenes Register reicht nicht. Dunkle Energie braucht eine kontrollierte Vakuumwirkung und radiative Stabilität. Materieüberschuss braucht eine quantitative dynamische Ausbeute. Starke CP braucht den Schutzmechanismus im wirklichen fermionischen Maß. Schwarze Löcher brauchen zuerst einen tatsächlichen gravitativen Sektor. Diese Aufgaben werden durch den endlichen Präparationserfolg nicht implizit erledigt. [A §10.6]

Eine vollständig spezifizierte primitive Theorie darf Ausgangsaxiome und Randbedingungen besitzen. Nicht jeder Parameter muss aus einer kleineren Zahlensammlung folgen. Sie muss jedoch kenntlich machen, welche Festlegungen Axiome sind und welche Resultate, und sie muss gemeinsame unterscheidbare Vorhersagen ermöglichen.

## 13. RH, Faktorisierung und Berechenbarkeit

Der RH Zweig bleibt an die vollständige signierte Weilform gebunden. Mit dem festgelegten Mellintransformierten G lautet der Zielvertrag schematisch

\[
Q_\zeta(g)=\sum_\rho G(\rho)\overline{G(1-\overline\rho)}
=\|Ag\|^2
\]

für den gesamten erforderlichen Testraum, bei exakter arithmetischer Identität, gemischten Termen, Randbeiträgen und Normierung. Der Operator A muss unabhängig definiert sein. Ihn aus einer schon als positiv angenommenen Weilform per Quadratwurzel zu definieren, setzt die Behauptung voraus. B §§4–5 enthält den präzisen offenen Vertrag; die Arbeit von Connes und Consani behandelt einen besonderen archimedischen Zusammenhang, nicht den gesamten RH Abschluss. [W7]

Die geprüfte E8 Gaußroute liefert bei einer vollständigen Fouriermessung und teilerfremdem Takt eine Gleichverteilung. Bei nicht teilerfremdem Takt hängt die Stütze vom schon klassisch berechenbaren ggT ab. Ein exakt faktorkodierendes Moment bleibt ohne effiziente Gewinnung des Moments kein schneller Algorithmus. Diese negative Entscheidung betrifft die benannte Ausleseroute, nicht alle möglichen kohärenten Programme. [B §6]

Ein mit Zusatzressourcen universell steuerbares Gerät könnte bekannte Periodenalgorithmen ausführen. Die positive Referenz ist Shors Algorithmus mit polynomialem Aufwand in der Bitlänge unter seinem Quantenrechenmodell [W8]. Eine mögliche TFPT Implementierung wäre damit nicht schon ein neuer Komplexitätssatz. Weder Faktorisierung noch eine physikalische TOE impliziert automatisch P=NP.

## 14. Ausführbarer Forschungsentscheid

Der sinnvollste feste Prüfgegenstand ist jetzt nicht noch eine neue lose U Skizze, sondern der folgende benannte Vertrag:

**Die harte C16 Vertexfamilie mit korrekt kohärenter innerer Wedge, explizit deklarierter lokaler Vermittlerarchitektur und getrennt dokumentierten schwachen sowie adressierten resonanten Steuereinstellungen.**

Er muss zugleich die zweite Ordnung, den vollständigen F4 Koeffizienten, die 2Δ/5 Bandtrennung, beide Recordausgänge, den 13 Amplitudenzeugen und die neuesten endlichen Echos bestehen. Der neue Feedbackkanal ist als kontrollierte Präparation mit ausgewiesenem Resetbudget hinzuzunehmen, nicht als verborgenes Naturgesetz.

Für die eigentliche Naturtheorie muss danach auf **derselben** skalierenden Familie entschieden werden, ob der gemeinsame physische Zustandssektor die richtige Chiralität, Ausbreitung, Kopplung und Gravitation liefert. Die bisherigen Daten wählen diese Familie noch nicht eindeutig aus. Das ist der konkret fehlende Schluss, nicht ein prinzipielles Verbot einer Lösung.

**Gesamturteil:** Mehrere vorher offene endliche Anschlussfragen sind jetzt geschlossen oder wesentlich enger kontrolliert. Insbesondere ist der frühere operative Wert ε=1/20 als isoliertes Belegungsband rigoros abgesichert, und die kontrollierte Zustandsauswahl besitzt einen expliziten eindeutigen Attraktor. Die vollständige TOE wird durch diese Resultate nicht behauptet. Ein späterer Abschluss muss diese neuen Sätze erhalten, statt für jede nächste Aufgabe zu einem anderen unmarkierten Modell zu wechseln.

## 15. Primärliteratur und Datenreferenzen

Die Literatur stützt die jeweiligen allgemeinen Methoden oder Referenzdaten, nicht die neue TFPT Quellauswahl und nicht automatisch die hier neu hergeleiteten C16 Aussagen.

W1. Sergey Bravyi, David P. DiVincenzo, Daniel Loss: *Schrieffer–Wolff transformation for quantum many body systems*. Annals of Physics 326 (2011). arXiv:1105.0675.

W2. Frank Verstraete, Michael M. Wolf, J. Ignacio Cirac: *Quantum computation, quantum state engineering, and quantum phase transitions driven by dissipation*. Nature Physics 5 (2009). arXiv:0803.1447.

W3. Scott Aaronson, Daniel Gottesman: *Improved Simulation of Stabilizer Circuits*. Physical Review A 70 (2004). arXiv:quant-ph/0406196. Die im Bericht verwendete 7T Phasenidentität wird zusätzlich direkt bewiesen; keine Behauptung einer optimalen T Zahl.

W4. NIST: *Fundamental Physical Constants, Complete Listing, 2022 CODATA adjustment*. Zeile inverse fine structure constant, am 14. September 2026 online abgerufen. Referenzwert 137.035999177, Standardunsicherheit 0.000000021.

W5. Thibaut Louis et al.: *The Atacama Cosmology Telescope: DR6 Power Spectra, Likelihoods and ΛCDM Parameters*. arXiv:2503.14452v2, Revision 24. Juni 2025. Tabelle 5, physische PDF Seite 31, Spalte P ACT LB2. Die Tabelle wurde visuell geprüft. Basismodell und Datenkombination sind Teil des Vergleichs; hier kein neuer Likelihoodlauf.

W6. Sho Araki, Hidenori Fukaya, Tetsuya Onogi, Satoshi Yamaguchi: *Symmetric Mass Generation for Domain Wall Fermions*. arXiv:2608.29963, 30. August 2026. Preprint, zweidimensionales euklidisches Gitter.

W7. Alain Connes, Caterina Consani: *Weil positivity and Trace formula, the archimedean place*. arXiv:2006.13771.

W8. Peter W. Shor: *Polynomial Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*. arXiv:quant-ph/9508027.

Die vollständigen Eingabeprüfsummen stehen in `source_manifest.json`. Die eigene Reproduktion wird in `README.md` erklärt.
