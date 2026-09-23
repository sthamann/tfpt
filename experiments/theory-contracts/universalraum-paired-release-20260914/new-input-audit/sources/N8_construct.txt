# TFPT und Universalraum: ein gemeinsames, prüfbares Konstrukt

**Konsolidierung der zwölf übergebenen Dokumente mit eigenen Herleitungen und unabhängigen Prüfungen. Stand: 14. September 2026.**

## Ergebnis und Reichweite

Der Arbeitsstand trägt eine zusammenhängende Forschungsarchitektur: Eine markierte Algebra legt zulässige Kanäle fest; eine explizite Dynamik realisiert diese Kanäle; Zustände und zugängliche Aufzeichnungen bestimmen die Mehrzeitstatistik; eingeschränkte Auslesungen liefern die bekannten TFPT-Schatten. Der entscheidende Zusammenhang liegt in der phasenrichtigen Zusammensetzung dieser Ebenen. Ein Spektrum, eine Marginale oder eine positive Einzelmatrix enthält dafür zu wenig Information.

Ein einzelnes, aus den TFPT-Ausgangsdaten eindeutig ausgewähltes Modell, das zugleich die vollständige Physik, RH und einen neuen schnellen Faktorisierungsalgorithmus liefert, ist damit noch nicht konstruiert. Die zwölf Dokumente enthalten mehrere unterschiedliche Modelle und teils bereits überholte Schlussfolgerungen. Ihre Zusammenlegung darf diese Unterschiede nicht verdecken.

Dieser Audit ergänzt den Stand um konkrete Resultate:

1. **Ein Fehler in der neuesten primitiven Regel wird lokalisiert und repariert.** Das gespeicherte innere Eingangslabel `ab` zerstört gerade die antisymmetrische Interferenz, aus der der gewünschte Austausch entstehen soll. Der Rang des betreffenden Gramoperators steigt von 6 auf 12. Ein expliziter unitärer Baustein mit 22 Dimensionen erhält die richtige Interferenz.
2. **Eine globale Normbedingung wird für einen ausdrücklich definierten endlichen Kandidaten geschlossen.** Im harten Clebsch-Modell mit Gesamtladung 16 gilt die konservative Schranke ‖V‖ ≤ 160|t|. Die Wahl |t|/Δ = 1/640 garantiert eine Trennung des niedrigen Besetzungsbands vom Vermittlerband um mindestens Δ/2. Das ist keine Behauptung über den inneren Vielteilchengap oder eine Prozentgenauigkeit aller effektiven Wechselwirkungen.
3. **Die Präparationslücke wird im erweiterten idealen Gattermodell stärker geschlossen als bisher.** Zwei phasenangepasste Verstärkungsschritte bilden den bekannten einfachen Eingang deterministisch auf Ω ab. Die Erfolgswahrscheinlichkeit ist dort exakt 1, ohne Erfolgsselektion. Benötigte kohärente Kontrollen und ihre Kosten bleiben ausdrücklich Teil der Voraussetzung.
4. **Die nächste Symmetriefrage wird sinnvoll präzisiert.** Die volle Kommutante eines Hamiltonoperators kann nicht einfach „SU(4) × W(D₅)“ sein. Für die infinitesimalen lokalen Produkttransformationen des verbundenen Austauschmodells lässt sich dagegen exakt beweisen: Übrig bleibt die kollektive su(4).
5. **Die RH-Verbindung erhält einen exakten mathematischen Vertrag.** Positive Prozessstatistik hilft erst, wenn sie die vollständige signierte Weil-Form phasen- und normierungstreu darstellt. Für singuläre Teilblöcke wird die in kurzen Schur-Argumenten leicht übersehene Bildraumbedingung ergänzt.
6. **Eine naheliegende schnelle E8-Auslesung wird entschieden.** Die vollständige Fourier-Messung des quadratischen E8-Phasenzustands ist bei teilerfremdem Takt gleichverteilt. Sonst liefert sie nur den bereits direkt berechenbaren ggT des Takts mit N. Eine exakte Faktorrückgewinnung aus dem bekannten Zählmoment funktioniert an fünf unabhängig aufgebauten Beispielen; die teure Momentgewinnung bleibt sichtbar.

Die ausgeschriebenen Beweise stehen in **TFPT_Universalraum_Beweise_2026-09-14.md**. Der Prüfer bestätigt **77 exakte Bedingungen und 8 numerische Kontrollen**. Diese 85 Prüfungen sind keine unabhängigen physikalischen Bestätigungen, kein Lean-Beweis und kein RH-Nachweis.

## 1. Das gemeinsame Objekt

### 1.1 Was der Universalraum in dieser Konsolidierung bezeichnet

Die tragfähige operationelle Definition lautet:

\[
h\sim h'\quad\Longleftrightarrow\quad
p(f\mid h)=p(f\mid h')\quad\text{für jede zugelassene zukünftige Eingriffsfolge }f.
\]

Eine Vorgeschichte darf nur dann durch eine kleinere Zustandsbeschreibung ersetzt werden, wenn kein erlaubtes späteres Experiment den Unterschied erkennen kann. Sobald ein altes Register wieder erreichbar wird, kann eine zuvor ausreichende Beschreibung unzureichend werden. Die Zugriffsrechte gehören deshalb zum mathematischen Modell. Das schließt an die etablierte Theorie von Mehrzeitprozessen an; die allgemeine Idee wird hier nicht als TFPT-Erfindung beansprucht. [Pollock et al.](https://arxiv.org/abs/1801.09811)

Eine konkrete Realisierung benötigt mehr als einen Operator mit dem Namen U:

\[
\mathfrak U_n=
(\Gamma_n,\mathcal H_n,H_n,\rho_{0,n},\mathcal I_n,\mathcal E_n,\mathcal C_n),
\qquad U_n(\tau)=e^{-i\tau H_n/\hbar}.
\]

Dabei sind Γ die Zusammensetzung und Nachbarschaft, H der vollständige Zustandsraum samt Vermittlern und Aufzeichnungen, Hₙ der Generator, ρ₀ der Eingang, I die erlaubten Instrumente, E die Auslesungen und C die Kosten. Die doppelte Verwendung des Buchstabens H wird durch die Schreibweisen ℋ und H unterschieden. Für eine skalierende Rechenanwendung braucht es eine einheitlich konstruierbare Familie und eine explizite Kodierung der Eingabe, etwa N. Ein schwer berechenbarer Zustand oder eine schwer berechenbare Messung darf dabei nicht zum kostenlosen Eingang werden.

**TFPT ist in diesem Bild die markierte Grammatik. Der Universalraum ist die Klasse ihrer ausführbaren, operationell unterscheidbaren Realisierungen.** Erst ein weiterer Auswahlbeweis würde aus dieser Klasse den behaupteten einen physikalischen Ursprung machen.

### 1.2 Die Ebenen müssen durch konkrete Abbildungen verbunden sein

| Ebene | Bereits konkret | Erforderliche Verbindung zur nächsten Ebene |
|---|---|---|
| Algebra | Spinor, D₅⊕A₃, E8-Verklebung, Z₄-Grade | normierte Vertizes, Adjunktion, Besetzung und erlaubte Produkte |
| Mikrodynamik | lokale Vermittler, harte Ortsmodelle, reversible Bausteine | ein gemeinsamer Hamiltonoperator mit kontrollierten Korrekturen |
| Zustand und Gedächtnis | Ω, Präparationsprotokolle, kohärente Register | Eingangs- und Umweltzustand, Zugriff, Energieabfuhr |
| Beobachtung | 60-Strahlen-Kanal, 45-/30-Koordinaten, Echos | vollständige Instrumente und Rohwahrscheinlichkeiten |
| Physik | endliche Spektren und bedingte Ausbreitungsmodelle | skalierende Familie, chirales Maß, gemeinsamer Kegel, Wechselwirkungen |
| Arithmetik | E8-Gaußidentität und Weil-Zielvertrag | exakte arithmetische Identität samt effizienter Auslesung bzw. voller Positivität |

Eine passende Zahl auf zwei Ebenen ersetzt keine dieser Verbindungen. Insbesondere sind die 240 E8-Wurzeln und 240 reelle CQ-Koordinaten verschiedene mathematische Objekte.

## 2. Der konsolidierte mathematische Kern

### 2.1 Algebra und korrekte Typen

Aus dem gesetzten komplexen Fünferträger folgt

\[
S^+=\Lambda^{\rm even}\mathbb C^5,\qquad \dim S^+=1+10+5=16.
\]

Die Diskriminantenformen von D₅ und A₃ sind bei passenden Generatoren 5k²/8 und 3k²/8 modulo eins. Die diagonale Z₄-Verklebung ist isotrop. Der Erweiterungsindex 4 macht aus Determinante 4·4 die Determinante 1. Damit entsteht das positive gerade unimodulare Gitter E8. Diese Konstruktion ist wesentlich stärker als die bloße Zahlengleichheit 5+3=8.

Die korrekte Graduierung lautet

\[
\begin{aligned}
\mathfrak g_0&=(45,1)\oplus(1,15),&\mathfrak g_1&=(16,4),\\
\mathfrak g_2&=(10,6),&\mathfrak g_3&=(\overline{16},\overline4).
\end{aligned}
\]

Es gilt [g₁,g₁]⊂g₂ und [g₁,g₃]⊂g₀. Der kurze Text D03 fällt beim abschließenden Vorschlag auf einen falschen gemischten Spinorkanal zurück. Auch eine korrekt berechnete endliche Klammer würde T2, die native analytische Naht, noch nicht schließen. D01, D02, D04–D07 und D12 enthalten die dafür nötigen Präzisierungen.

### 2.2 Der statistische Schatten

Für die festgelegte Messregel gilt

\[
T=\frac{C^\top BC+F^\top F}{28},\quad
CC^\top=4I,\quad FF^\top=12I,\quad CF^\top=0.
\]

Damit hat T Rang 30 und Spektrum

\[
1^{[1]},\quad(3/7)^{[15]},\quad(2/7)^{[9]},\quad(-2/7)^{[5]},\quad0^{[30]}.
\]

Die bekannten Größen gehören zu unterschiedlichen Zugriffsklassen:

| Beschreibung | Lineare Koordinaten | Normalisierte affine Koordinaten |
|---|---:|---:|
| Allgemeine 15 CQ-Blöcke | 240 | 239 |
| Bild nach einer Messrunde | 60 | 59 |
| Passive separate Kontext- und Systemmarginalien über alle Horizonte | 45 | 44 |
| Nächste volle Verteilung aus der bereits gemessenen Strahlenklasse | 30 | 29 |

Die 30 Nullrichtungen des festen T leben nicht als verstecktes Gedächtnis in diesem Kanal weiter. Gedächtnis entsteht in einer reicheren Realisierung mit erreichbaren Korrelationen. Ebenso ist der Faktor 3/7 kein aus E8 allein erzwungener Naturparameter: Die Familie Kₐ=aI+(1−a)(B−I)/6 hat dieselbe angegebene Symmetrie und Inzidenz. Maximale Übergangsentropie oder die besondere Rangreduktion können a=1/7 auswählen, müssen aber als zusätzliche Prinzipien begründet werden.

### 2.3 Zelle, Graph und Austausch

Der Zustand

\[
|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)|\pi(0)\pi(1)\pi(2)\pi(3)\rangle
\]

hat ρᵢ=I₄/4 und ρᵢⱼ=(I−Sᵢⱼ)/12. Auf einem verbundenen Graphen mit N fundamentalen Viererträgern und strikt positiven Gewichten gilt

\[
\ker\sum_{ij}J_{ij}P^+_{ij}=\Lambda^N\mathbb C^4.
\]

Für N=4 ist der Kern CΩ, für N>4 ist er null. „Vier ist die kleinste neutrale Zelle“ verlangt zusätzlich ausschließlich fundamentale Träger und Neutralität; mit elementaren 4 und 4̄ wäre bereits Zweierneutralität möglich. Ein eindeutiger reiner Zellzustand darf zudem nicht unverändert als jede Marginale eines verschränkten Zellnetzes eingesetzt werden: Reine Marginalien erzwingen Faktorisation.

Die Lesart „Spinorgewicht = Ort“ ergibt den Clebsch-Graphen mit 16 Knoten, 40 Kanten und Grad 5. Er ist dreiecksfrei und enthält keinen K₄. Ein Viererstern kann Ω tragen; daraus wird der volle Tetramer-Hamiltonoperator nicht automatisch die native Dynamik. Der voll besetzte Clebsch-Graph ist wegen N>4 frustriert.

Der in D01 berichtete korrigierte erste angeregte Singulettwert 11,561762122802 J ist numerisch mindestens vierfach gefunden; die ältere Dublett-Angabe in D12 ist überholt. Eine Rechnung nur im 24 024-dimensionalen Singulettsektor zertifiziert weder alle Sektoren noch die exakte algebraische Multiplizität. Diese Großrechnung wurde hier nicht wiederholt.

### 2.4 Vermittlung und ihre Reichweite

Für W†W=P₋ und WW†=I₆ ist der isolierte 22-dimensionale Hamiltonoperator

\[
H_{22}=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix}
\]

direkt lösbar. Relativ zum unteren antisymmetrischen Band entsteht

\[
J_{\rm eff}=\frac{\sqrt{\Delta^2+4g^2}-\Delta}{2}
=\frac{g^2}{\Delta}-\frac{g^4}{\Delta^3}+\cdots.
\]

Bei g=√2t ist 2t²/Δ der führende Term, nicht die exakte Formel. Auf mehreren Kanten mit gemeinsamem Boson entstehen echte zusätzliche Terme. Im in D06 gerechneten Zweikantenblock ist der verbundene Beitrag vierter Ordnung −8t⁴S₆/Δ³. Gegenüber J=2t²/Δ entspricht der Koeffizient 4(t/Δ)². Die alternative Projektorform besitzt den Faktor 8; ihre skalare Verschiebung gilt zunächst innerhalb des betrachteten Paarsektors. Die pauschale Ein-Prozent-Angabe bei t/Δ=0,1 ist daher nicht korrekt.

Ein kleiner lokaler Koeffizient zertifiziert noch keine globale Näherung. Abschnitt 3.2 liefert dafür erstmals in diesem Audit eine transparente, bewusst konservative Normkontrolle eines vollständig benannten Kandidaten.

### 2.5 Zwei Zellen und Zeit

Für zwei vollständige Tetramer mit genau einer positiven Brücke gilt nach dem stärkeren Nachweis in D05, übernommen in D01/D02,

\[
E_0=\frac{4J+\lambda-\sqrt{16J^2-2J\lambda+\lambda^2}}2,
\quad
E_1=3J+\frac\lambda2-\frac{\sqrt{4J^2+\lambda^2}}2.
\]

Der Grundzustand bleibt für alle λ≥0 eindeutig und der Gap ist strikt größer als J/2. Die ältere Grenze λ<8J war eine Grenze eines schwächeren Beweises. Bei λ=8J beträgt der tatsächliche Gap etwa 0,876894J. Der all-λ-Satz gehört zu diesem Zweizellenmodell und beweist keinen thermodynamischen Gap eines Netzes.

Aus einem Produktanfangszustand entsteht unter demselben H ein dynamisches Signal

\[
p_1(t)=\frac{15\lambda^2}{16R^2}\sin^2\!\frac{Rt}{2\hbar},\qquad R^2=16J^2-2J\lambda+\lambda^2.
\]

Der stationäre Grundzustand tickt nicht. Ein lokaler Familienzyklus, eine relationale Viereruhr und dieser Brückenoszillator sind verschiedene Protokolle. Der vollständige Tetramer erhält seine Paarenergien; eine Tabelle von externen Ticks ist deshalb keine freie Bewegung gerade dieser Anzeige.

## 3. Drei konkrete konstruktive Ergänzungen

### 3.1 Die History-Regel muss Interferenz erhalten

D04, Zeilen 671–685, und D01, Zeilen 182–184, schreiben ein History-Label |st,ab,μ⟩. Für die beiden Wege |ab⟩ und |ba⟩ in denselben antisymmetrischen Vermittler ist jedoch gerade ihre Ununterscheidbarkeit erforderlich:

\[
K=(1,-1),\qquad K^\dagger K=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

Wird das geordnete Paar `ab` orthogonal gespeichert, verschwinden die gemischten Einträge und die Gram-Matrix wird I₂. Dann ist der symmetrische Zustand nicht mehr dunkel. Auf C⁴⊗C⁴ wird aus I−S der Operator I−D mit D=Σₐ|aa⟩⟨aa|. Der Rang steigt von 6 auf 12; kollektive SU(4)-Invarianz geht verloren.

**Reparatur:** Verschiedene Kanten dürfen durch ihre Lochkonfiguration unterscheidbar sein. Die beiden inneren vertauschten Wege derselben Kante müssen dagegen dieselbe kohärente Aufzeichnung hinterlassen, oder eine zwischenzeitliche Aufzeichnung muss vor der relevanten Interferenz tatsächlich rückgängig gemacht werden. Bloß auf eine spätere globale Unitarität zu verweisen genügt nicht.

Ein ausdrücklich unitärer Baustein ist

\[
U_\theta=\begin{pmatrix}
P_++\cos\theta\,P_-&-\sin\theta\,W^\dagger\\
\sin\theta\,W&\cos\theta\,I_6
\end{pmatrix}.
\]

Für θ=π/2 liefert seine zweimalige Anwendung auf dem Materiesektor genau den Swap und setzt den Vermittler zurück. Die Beweise und eine Bedingung für teilweise unterscheidbare Aufzeichnungen stehen in Beilage A.

### 3.2 Ein wohldefinierter globaler Kandidat mit garantiert getrenntem Vermittlerband

Eine konsistente endliche Reparatur ist ein **hartes Tensorproduktmodell** mit ℋₛ=C|∅⟩⊕C⁴ auf den 16 Clebsch-Orten und sechs Bosonmoden pro Vektorlabel r∈{±e₁,…,±e₅}. Diese Wahl ist ausdrücklich eine konkrete Realisierung; sie wird nicht mit einer bereits hergeleiteten fundamentalen Fermionstatistik gleichgesetzt.

Der lokale Operator Kₑ,A wandelt den inneren antisymmetrischen Paarzustand in zwei Löcher um. Es wird kein unterscheidendes `ab`-Label geschrieben. Für Gesamtladung

\[
\sum_s n_s+2\sum_{r,A}b^\dagger_{r,A}b_{r,A}=16
\]

ist der Zustandsraum endlich. Setze

\[
H_0=\Delta\sum_{r,A}b^\dagger_{r,A}b_{r,A},\qquad
V=t\sum_{e,A}\bigl(b^\dagger_{r(e),A}K_{e,A}+K^\dagger_{e,A}b_{r(e),A}\bigr).
\]

Damit ist H=H₀+V selbstadjungiert und U(τ)=exp(−iτH/ℏ) unitär. t bezeichnet die reelle Kopplung, τ die Zeit. Der höchstens achtfache Bosonbesatz ergibt für jeden der 40 Kantenbeiträge die Normschranke 4|t|. Daher

\[
\|V\|\le160|t|,\qquad |t|/\Delta=1/640\Longrightarrow\|V\|\le\Delta/4.
\]

Die Weyl-Schranke trennt das niedrige Band vom ersten Vermittlerband um mindestens Δ−2‖V‖≥Δ/2. Der oft genannte Wert 1/20 ist mit dieser groben Abschätzung nicht zertifiziert; daraus folgt nicht, dass er tatsächlich versagt. Die neue Wahl ist ein Existenzzeuge eines kontrolliert isolierten Bands und kein optimierter Betriebswert. Sie macht den führenden Austausch sehr langsam: J/Δ=1/204 800.

Die vollständige effektive Vielteilchendynamik, ihre höheren Ordnungen und eine native Auswahl der Kopplung bleiben eigene Aufgaben. Der Nachweis löst die Normfrage für diesen Kandidaten, nicht T5 oder T8. Beilage B enthält die vollständige Begründung.

### 3.3 Ω ohne verworfene Präparationsversuche

Die ältere konkrete Schaltung liefert p=3/32. Der bereits neuere exakte Sternfilter erreicht p=1/6. Beides beginnt im leicht herstellbaren Zustand

\[
|\chi\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}\otimes
\frac{|23\rangle-|32\rangle}{\sqrt2},\qquad|\langle\Omega|\chi\rangle|^2=1/6.
\]

Für einen bekannten Projektor Pᵥ=|v⟩⟨v| definiere Rᵥ(z)=I+(z−1)Pᵥ. Wähle

\[
|z|=1,\qquad \operatorname{Re}z=\frac{3\sqrt5-7}{2},\qquad
z=e^{i\phi},\quad\phi\approx1.717216986.
\]

Dann gilt **exakt**

\[
[R_\chi(z)R_\Omega(z)]^2|\chi\rangle=e^{i\gamma}|\Omega\rangle
\]

für eine irrelevante globale Phase γ. Beilage C zeigt die verschwindende Fehleramplitude als Polynomidentität und konstruiert die Ω-Phasenoperation aus dem vorhandenen Sternspektrum. Drei wiederverwendbare Kontrollqubits reichen für deren Selektionsregister; zusätzlicher Platz und Aufwand für die Realisierung der kontrollierten Dynamik sind damit nicht mitgezählt.

Das ist eine konkrete Anwendung bekannter Amplitudenverstärkung, kein Anspruch auf die Erfindung dieser Methode. Die allgemeine Grundlage findet sich bei [Brassard, Høyer, Mosca und Tapp](https://arxiv.org/abs/quant-ph/0005055). Neu in diesem Arbeitsprodukt ist die ausgeschriebene Spezialisierung auf diesen Ω-Eingang samt passender Phase und unabhängiger Kontrolle.

| Protokoll | Ideale Präparationswahrscheinlichkeit | Zusätzlicher Zugriff |
|---|---:|---|
| Alte 32-Zweig-Schaltung | 3/32 ≈ 9,375 % | kontrollierte Permutationen und Erfolgsselektion |
| Exakter Sternprojektor | 1/6 ≈ 16,667 % | kontrollierte Sternentwicklung und Erfolgsselektion |
| Ein gewöhnlicher Verstärkungsschritt | 49/54 ≈ 90,741 % | kohärente Reflexionen |
| Zwei angepasste Schritte | 1 | vier selektive Phasenoperationen, vollständige Kohärenz |

Das sind verschiedene Ressourcenverträge. Aus 100 % idealem Erfolg folgt kein Hardwarevorteil. Eine exakte Realisierung in einem endlichen Clifford+T-Alphabet wird nicht behauptet; die besondere Phase benötigt dort eine Approximationsrechnung. Ebenso ist eine kontrollierbare isolierte Viererzelle nicht automatisch aus der festen globalen Clebsch-Regel verfügbar.

Mit idealer deterministischer Vorbereitung und ebenso genauer Endprojektion werden die normierten Echos zu Rohwahrscheinlichkeiten: 1 gegen 17/32 beim Dreierzyklus und 1 gegen 1/2 in der ausgeglichenen Variante. Die alten Rohwerte 27/512 gegen 459/16 384 gehören weiterhin zum alten Protokoll und bleiben als Referenz erhalten.

## 4. Symmetrie, Naht und Raumzeit bleiben unterschiedliche Aufgaben

Die volle Kommutante eines endlichen H enthält auf jedem entarteten Energieraum alle linearen Abbildungen und insbesondere jede Funktion von H. Die Forderung, sie müsse nur „SU(4) × W(D₅)“ sein, ist deshalb falsch gestellt. Für die **lokalen** Generatoren X=Σᵢhᵢ mit spurfreien hermiteschen hᵢ gilt im verbundenen Austauschmodell dagegen

\[
[X,H_2]=0\quad\Longleftrightarrow\quad h_i=h_j\ \text{für alle }i,j.
\]

Die 240 lokalen Parameter werden durch 225 unabhängige Bedingungen auf 15 kollektive Parameter reduziert. Ortspermutationen werden separat durch die Graphautomorphismen beschrieben. Das beweist weder das Fehlen beliebiger nichtlokaler Symmetrien noch die Symmetrie eines vollständig ausgerechneten H₂+H₄. Die harte Lesart „Spinorgewicht ist besetzter Ort“ trägt außerdem nicht automatisch die kontinuierliche Spin(10)-Mischung dieser Gewichte.

Die E8-Gitter-Vertexalgebra mit c=8 ist eine konkrete mathematische Erweiterung; 5+3=8 ist jedoch noch keine native chirale Naht. Eine SU(4)-Kette mit c_L=c_R=3 ist kein einzelner chiraler Randsektor. Eine 2+1-dimensionale Bulk-Rand-Architektur wäre ein zusätzlicher Kandidat, keine 3+1-dimensionale Ableitung.

Für einen linearen Zweibandpropagator lautet die korrekte lokale Determinante

\[
\det G^{-1}(\omega,q)=(\omega-w\cdot q)^2-q^\top V^\top Vq.
\]

In diagonaler Form steht dort Σᵢvᵢ²qᵢ². Ein Ausdruck (Σᵢvᵢqᵢ)² wäre im Allgemeinen ein anderes, rangarmes Objekt. Die Formel liefert unter ihren Voraussetzungen einen lokalen Kegel. Sie wählt weder die globale Raumdimension noch einen gemeinsamen Kegel sämtlicher Sektoren. Verschiedene Überlagerungen desselben endlichen Graphen können unterschiedliche Volumen- und Spektralskalierung besitzen.

Die Identität det(tI+x·σ)=t²−|x|² bleibt ein sauberer Lorentz-Anschluss. Ein masseloser Spin-2-Sektor mit zwei Helizitäten und universeller Kopplung folgt daraus nicht. Auch ein isoliertes niedriges Vermittlerband ist kein Beweis masseloser Photonen oder Gravitonen.

## 5. RH: der gemeinsame Gedanke und die fehlende entscheidende Identität

Der hilfreiche gemeinsame Gedanke ist die Kontrolle gemischter Terme. Im Austauschmodell entscheidet der gemischte Eintrag über destruktive Interferenz. In RH entscheidet die vollständige signierte Form darüber, ob eine positive Darstellung tatsächlich die ursprüngliche arithmetische Frage beantwortet.

Mit einer festgelegten Mellin-Normierung sei G(s)=∫₀∞g(x)xˢ⁻¹dx. Die relevante quadratische Form lautet

\[
Q_\zeta(g)=\sum_\rho G(\rho)\overline{G(1-\bar\rho)}.
\]

Die nichttrivialen Nullstellen werden mit Multiplizität gezählt. Die explizite Formel identifiziert diese Größe mit einer signierten Kombination der Primstellen, des archimedischen Beitrags und gegebenenfalls der Randterme. Im klassischen Weil-Kriterium muss die Positivität für den ganzen vorgeschriebenen Testraum gelten. Die Primärquelle [Connes–Consani](https://arxiv.org/abs/2006.13771) erläutert den Rahmen und untersucht einen besonderen archimedischen Fall; sie liefert keinen allgemeinen RH-Abschluss.

Für einen wirklichen Universalraum-Beitrag wäre nachzuweisen

\[
Q_\zeta(g)=\|Ag\|^2
\]

für **alle** erforderlichen g, mit einem unabhängig definierten A und exakt derselben Normierung, denselben Randtermen und denselben gemischten Beiträgen. A aus einer vermeintlich schon positiven Qζ durch Cholesky zu definieren würde die offene Behauptung voraussetzen. Nullstellen durch reelle Frequenzen zu ersetzen würde ebenfalls voraussetzen, was zu zeigen ist.

Beilage E gibt eine präzisere schrittweise Alternative: kompatible vollständige endliche Blöcke, korrekte Kopplung ihrer Nullräume, Schur-Positivität und eine dichte Fortsetzung im tatsächlichen Testraum. Dafür braucht man keinen überall strikt positiven Grenzgap. Man braucht aber einen Beweis über alle Stufen, die richtige Kontinuität und die arithmetische Identität. Die bislang berichteten endlichen oder ungeraden Fenster erfüllen diese Gesamtheit nicht.

**Nicht gelöst bleibt die Existenz der phasentreuen positiven Darstellung der vollständigen Weil-Form.** Die hier bewiesene Reparatur verhindert einen falschen Schluss und macht die nächste Behauptung präzise; sie beweist RH nicht.

## 6. Faktorisierung: Informationsgehalt und Auslesekosten

### 6.1 Was die E8-Gaußdaten tatsächlich leisten

Die ausgewählte verfügbare Originalroute r647 enthält

\[
S_N(t)=N^4\gcd(t,N)^4.
\]

Die Identität wurde hier unabhängig für alle Takte bei N=2,3,4,5 mit ganzzahligen Koeffizienten modulo Kreisteilungspolynom geprüft. Für versprochenes N=pq mit verschiedenen Primzahlen kann das Moment M₄(N)=ΣₜggT(t,N)⁴ die Faktoren exakt kodieren. Diese Kodierung ist kein kostenloses Messverfahren.

Der neue Test beginnt bei N allein, berechnet das Moment durch N ggT-Aufrufe und invertiert anschließend eine explizite Quartik ohne vorgegebene Faktoren:

| N | Tatsächlich wiedergewonnene Faktoren | ggT-Aufrufe zur Momentgewinnung |
|---:|---|---:|
| 15 | 3 × 5 | 15 |
| 35 | 5 × 7 | 35 |
| 143 | 11 × 13 | 143 |
| 899 | 29 × 31 | 899 |
| 10 403 | 101 × 103 | 10 403 |

Das ist ein echter erfolgreicher endlicher Durchlauf und zugleich kein schneller Faktorisierungsalgorithmus: O(N) Aufrufe sind exponentiell in der Eingabelänge log₂N. Bereits ein nichttrivialer ggT während der Momentgewinnung liefert einen Faktor; der Umweg über das Moment verbessert das nicht.

### 6.2 Warum die direkte Fourier-Abkürzung hier nicht trägt

Sei G eine ganzzahlige gerade unimodulare E8-Grammatrix, q(x)=xᵀGx/2 und

\[
|\psi_t\rangle=N^{-4}\sum_{x\in(\mathbb Z/N)^8}e^{2\pi itq(x)/N}|x\rangle.
\]

Nach der vollständigen endlichen Fourier-Transformation gilt mit d=ggT(t,N) genau

\[
\Pr(b)=
\begin{cases}
(d/N)^8,&d\mid b_1,\ldots,d\mid b_8,\\
0,&\text{sonst}.
\end{cases}
\]

Bei d=1 ist die gesamte Verteilung gleichförmig. Bei d>1 ist ihre Stütze durch den ggT bestimmt, der aus dem bereits bekannten Takt t und N direkt berechnet werden kann. Die Beilage beweist die Aussage für jedes N≥2, auch gerade N, durch Charakterorthogonalität. Zusätzliche numerische Vollverteilungen bis N=6 bestätigen sie; die größte beobachtete absolute Abweichung beträgt etwa 8,7·10⁻¹⁸.

Dieser Satz betrifft genau diese Phasenpräparation, Fourier-Transformation und anschließende Messung. Er ist kein Verbot anderer kohärenter E8-Rechenmodelle und keine allgemeine Quantenuntergrenze. Weitere Interferenz vor einer Messung wäre ein neues, vollständig zu spezifizierendes Verfahren.

Bei gleichförmig gewähltem Takt ist die Chance eines echten ggT für N=pq gleich (p+q−2)/N. Für ausgeglichene Faktoren ist das von Größenordnung N⁻¹/². Unstrukturierte Verstärkung dieser seltenen Takte würde nur auf N¹/⁴ Versuche führen, weiterhin exponentiell in der Bitlänge.

### 6.3 Was für einen starken positiven Rechennachweis nötig wäre

Ein ernsthafter Kandidat muss vor dem Test festlegen: N-Kodierung, Zustandspräparation, kohärente Schritte, Genauigkeit, Auslesung, Erfolgsrate und Gesamtaufwand in log N. Große bereits bekannte Faktoren dürfen ausschließlich zur abschließenden Kontrolle benutzt werden.

Die bekannte positive Referenz ist kohärente modulare Exponentiation mit Periodenauslesung und klassischer Nachverarbeitung, wie in [Shors Originalarbeit](https://arxiv.org/abs/quant-ph/9508027). Ein TFPT-Gerät, das diese Operationen nachweislich mit geeigneten Kosten realisiert, wäre eine Implementierungsleistung. Ein zusätzlicher Vorteil müsste gegen diese Referenz gemessen werden. RH ist dafür keine erforderliche Voraussetzung, und aus Faktorisierung folgt kein P=NP-Satz.

## 7. Weitere Anwendungen und das verbleibende Gesamtprogramm

Die unmittelbar belegbaren Anwendungen sind kleiner, aber konkret:

- **Zustandspräparation und Kalibrierung:** exakte Ω-Zielzustände, der bekannte Energie-Fidelity-Bound und nun eine deterministische ideale Vorbereitung unter benannten Kontrollen.
- **Gedächtnisdiagnostik:** Mehrzeit-Echos unterscheiden erreichbare Kohärenz von frischen oder entwerteten Aufzeichnungen; negative Kontrollen ohne Tick müssen mitlaufen.
- **Hamiltonoperator-Identifikation:** Der gemeinsame Grundzustand verschiedener Graphen reicht nicht aus; Anregungen und lokale Symmetrieantworten unterscheiden die Kandidaten.
- **Diskrete Logarithmen:** ein mögliches Rechenziel bei nachgewiesener allgemeiner kohärenter Arithmetik, bereits durch Shors bekannte Methode abgedeckt; hier kein neues Verfahren.
- **RH und verwandte L-Funktionen:** erst nach einer funktionstreuen positiven Darstellung interessant. Die zusätzliche Arithmetik anderer L-Funktionen wird nicht durch das Wort Universalraum übernommen.

Physikalische Zahlennähe bleibt als eigener Prüfstrang erhalten. Die dokumentierte α-Formel ergibt α⁻¹≈137,0359992168407; gegenüber der ausdrücklich datierten CODATA-2022-Referenz 137,035999177(21) sind das etwa 1,897 experimentelle Standardabweichungen. Ohne Herleitung des Transfers zur Thomson-Kopplung und Theorieunsicherheit ist dies kein abgeschlossener Vorhersagenachweis. [Offizielle NIST-Tabelle](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)

Die ungünstigen Ergebnisse verschwinden nicht: etwa 2,2 % Spannung beim einfachen μ/τ-Verhältnis, die alte Higgs-Linie bei 129–134 statt ungefähr 125 GeV, eine einfache Inflationsamplitude 1,76·10⁻⁹ statt der verwendeten Referenz 2,10·10⁻⁹ sowie in den dokumentierten Zweischleifenzweigen zu kurze Protonlebensdauern um die Faktoren 80, 3,4 und 2,4. Das sind hier aus den Dokumenten übernommene, nicht neu ausgeführte physikalische Rechnungen.

| Tor | Noch fehlender Nachweis | Beitrag dieser Konsolidierung |
|---|---|---|
| T1 | eindeutige primitive Quelle samt Markierungen und Zugriffen | konsistente lokale Reparatur und expliziter endlicher Kandidat |
| T2 | native analytische E8-Naht, Phasen, Domänen und Skalierung | korrekte Grade; endliche Algebra von chiraler Realisierung getrennt |
| T3 | ausgewählte lokale 3+1-Dynamik und gemeinsamer Kegel | richtige Propagatorform und sichtbare Graph-/Skalierungswahl |
| T4 | chirales Standardmodellmaß, Index und Spiegelentkopplung | endliche Ladungs- und Anomaliestruktur bleibt bedingt |
| T5 | wechselwirkender skalierender Grenzwert | globale Vermittlerband-Schranke für einen endlichen Kandidaten |
| T6 | vollständige Kopplungs- und Neutrinoselektion | Zahlen und negative Transferbefunde gemeinsam erhalten |
| T7 | masseloser Spin 2 mit universeller Kopplung | kein neuer Abschluss |
| T8 | ausgewählter physischer Zustand samt zugänglicher Geschichte | deterministische ideale Vorbereitung; natürliche Zustandsauswahl offen |

Die nächstentscheidende Integrationsaufgabe lautet: **Kann dieselbe unveränderte mikroskopische Regel den kohärenten Austausch, die benötigten selektiven Phasenoperationen und eine vollständige Rohstatistik gemeinsam realisieren?** Der neue History-Gegentest und die deterministische Präparation liefern dafür überprüfbare Sollwerte. Erst danach wäre eine Behauptung gemeinsamer Rechen- oder Physikleistung gerechtfertigt.

## 8. Quellen, Aktualität und Reproduktion

Alle elf Markdown-Dateien und das 90-seitige PDF wurden inhaltlich ausgewertet. Überlappende Fassungen wurden verglichen; im PDF wurde zusätzlich eine zentrale RH-Seite visuell kontrolliert. Während des Audits wurde D02 außerhalb dieser Arbeit aktualisiert. Die Änderungen wurden gesondert gelesen und berücksichtigt; beide Lesestände sind im Paket dokumentiert. Dateiprüfsummen und Lesekopien stehen im Quellenmanifest bzw. Reproduktionspaket. Die Quellenkürzel dieses Dokuments gelten nur hier:

| Kürzel | Übergebene Datei | Rolle |
|---|---|---|
| D01 | TFPT_UNIVERSALRAUM_KONSOLIDIERUNG_2026-09-14_fable.md | jüngere Gesamtkorrektur, globale U-Fragen |
| D02 | TFPT_Universalraum_Rekonstruktion_2026-09-14_sol.md | ausführliche Rekonstruktion und Kriterien |
| D03 | TFPT_Universalraum_Konsolidierung_2026-09-14.md | Kurzfassung mit benannten Rückfällen |
| D04 | TFPT_UNIVERSALRAUM_Q_AUDIT_UND_U_REGEL_2026-09-14.md | Rang-/Vermittleraudit und primitive History-Regel |
| D05 | TFPT_Rekonstruktion_2026-09-14.md | stärkere Zweizellenbeweise, Fourier-Präparation |
| D06 | TFPT_Sechs_Pruefpunkte_Analyse.md | Fockmodell, Vierkörperterm, Symmetriegrenze |
| D07 | TFPT_Fortsetzung.md | T-Faktorisierung, Vermittler, Uhren |
| D08 | TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md | ursprüngliche Schaltung und Rohwahrscheinlichkeiten |
| D09 | TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md | Energie, Verschränkung, Uhr und TOE-Vertrag |
| D10 | TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md | frühere Gesamtthese und arithmetische Grenzen |
| D11 | TFPT_Universalraum_Rekonstruktion_2026-09-14.md | weitere Rekonstruktionsfassung |
| D12 | TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf | Gesamtbuch einschließlich RH-/Faktor-Anschluss |

Zusätzlich wurde der vorhandene TFPT-Codegraph abgefragt und die ausgewählte verfügbare Originalimplementierung der E8-Gaußroute r647 gelesen. Der RH-Katalog wurde live auf Aktualität geprüft. Eine vollständige Aktualisierung scheitert an fehlenden referenzierten Quelldateien; der Claim-Aufruf W1 meldet außerdem Quellen-/Review-Drift. Der separate Faktorgraph fehlt an seinem konfigurierten Speicherort. Deshalb wird keine vollständige Kenntnis sämtlicher früherer Versuche und kein aktueller globaler Beweisstatus behauptet. Verfügbare Originale und die zwölf neuen Eingaben bilden die tatsächliche Abdeckung.

Die in den Quellen genannten 210, 598 oder 27 288 Bedingungen wurden nicht zu einer gemeinsamen Erfolgszahl addiert. Der neue Prüfer importiert keinen Original-Forschungscode. Er rekonstruiert die kleinen Objekte selbst und beendet sich bei einem fehlgeschlagenen Kriterium mit einem Fehler. Normaler und optimierter Lauf sind nach dem letzten Stand bytegleich; Details stehen im Prüfergebnis.

Das Reproduktionspaket enthält beide Texte, Prüfer, Ergebnis, Quellenmanifest und lokale Lesekopien. Es verändert keine der zwölf Originaldateien und keinen RH-Abschlussmarker. Die mathematischen Ergänzungen sind überprüfbare Arbeitsresultate; eine weltweite Neuheitsbehauptung wird für sie nicht erhoben.
