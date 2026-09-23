# TFPT und Universalraum
## Forschungsfortsetzung auf Basis von v1.4

**Datum:** 14. September 2026  
**Auftrag:** Die sechs Folgefragen und die verbleibenden Fragen T1 bis T8 weiter untersuchen und konkrete Lösungen entwickeln.  
**Status:** Neue modellbedingte Sätze, ein optimierter endlicher Laborvertrag, unabhängige Rechnungen und präzisierte offene Beweispflichten. Kein Abschluss der gesamten Theorie.

## 1. Ergebnisübersicht

Die wichtigste neue Konstruktion ist ein mit Clifford Operationen herstellbarer Eingang \(\xi\), der den Vierträgerzustand \(\Omega\) mit Gewicht **3/8** statt **1/6** trifft. Dieses Gewicht ist nicht nur eine Verbesserung: In der verwendeten Kodierung ist es das **globale Optimum über alle achtqubitigen Stabilizerzustände**, einschließlich ihrer konvexen Mischungen. Der Beweis reduziert die Frage auf sechs Punkte in einem vierdimensionalen binären Raum.

Damit ändern sich mehrere Ergebnisse gleichzeitig:

| Größe | Vertrag in v1.4 | Neue Konstruktion |
|---|---:|---:|
| Bester hier verwendeter Clifford Eingang für den Sternfilter | Überlapp 1/6 | Überlapp 3/8, als Stabilizeroptimum bewiesen |
| Rohwahrscheinlichkeit erfolgreicher Präparation | 0,1619153313 | 0,3643094954 |
| Gemeinsamer Erfolg mit behaltenem Record | 0,1572994471 | 0,3539237559 |
| Gemeinsamer Erfolg mit frischem Record | 0,08356533125 | 0,1880219953 |
| Mittlere Präparationsversuche | 6,1761 | 2,744918847 |
| Selektive Zielphasen bei angepasster idealer Verstärkung | Zwei | Eine |
| Kontrollierte H Aufrufe dieser Zielphasen | 52 | 26 |
| Feedbackkontraktion mit dem jeweiligen Reset | 0,9754207105 bei Überlapp 1/24 | 0,7787863941 bei Überlapp 3/8 |
| Garantierte Zyklen für lokale Infidelität 10⁻⁶ | 556 | 56 |
| Garantierte ideale Zyklen für 4096 unabhängige Zellen, globale Infidelität 10⁻⁶ | 890 | 89 |
| Verstärkung eines dauerhaften Fehlers pro Feedbackzyklus | 40,68465844 | 4,520517604 |
| Kantenlokale äußere Bandschranke | 0,7 Δ | 0,72 Δ, rational zertifiziert |

Die unterschiedlichen alten Eingänge werden nicht vermischt: Der Sternfilter in v1.4 benutzt zwei Paarsinguletts mit Überlapp 1/6. Das dortige Feedback setzt dagegen auf das Basiswort 0123 mit Überlapp 1/24 zurück. Der neue Eingang verbessert beide Verträge, aber um unterschiedliche Faktoren.

Weitere Ergebnisse dieser Fortsetzung:

* Lokale additive Ladungserhaltung liefert ein genaues Auswahlkriterium für kantenadressierte Vermittler. Dieses Kriterium ist stärker als Lokalität und bleibt als zusätzliche Annahme sichtbar.
* Die Vierfachheitsfrage im Clebsch Singulettsektor erhält exakte Projektoren auf die relevanten Multiplizitätsräume von Dimension **80** und **42**. Deren Spektren sind damit noch nicht zertifiziert.
* Die lokale vierte Ordnung besitzt zusätzliche scharfe Operatorabschätzungen. Für den Ausschluss anderer SU(4) Sektoren würde bereits eine zertifizierte nackte Untergrenze **11,6 J** ausreichen, zusammen mit einer passenden zertifizierten Obergrenze für den Viererraum.
* Ein Fehlerbound gilt nun auch für **wirklich gekoppelte** Zellen. Er zertifiziert lokale Nähe zu Ω unter laufender Kopplung und Kühlung, nicht die Präparation eines verschränkten wechselwirkenden Grundzustands.
* Eine endliche Programmuhr führt ein festgelegtes Laborprotokoll autonom aus, bei ausdrücklich bilanziertem Energiebedarf. Sie erklärt nicht die Herkunft ihres Programms aus TFPT.
* Aus dem Austauschrecord entsteht ein konkretes Toffoli Makro. Damit ist universelle Quantenrechnung unter dem erweiterten, skalierbar verfügbaren Kontrollvertrag anschließbar. Eine native TFPT Implementierung oder ein neuer Faktorisierungsalgorithmus folgt daraus nicht.

Diese Ergebnisse sind neu gegenüber den vier vorgelegten Dokumenten. Eine Priorität gegenüber der gesamten Forschungsliteratur wird nicht behauptet.

## 2. Quellenbasis und tatsächlicher Prüfumfang

Gelesen wurden die vier aktuellen Anhänge: das vollständige Hauptdokument v1.4 mit 126 Seiten, das vierseitige Update, der Forschungsbericht und die sechs Folgefragen. Maßgebliche Stellen sind insbesondere Hauptdokument Kapitel 23 bis 27 und Forschungsbericht Abschnitte 3 bis 9.

Zusätzlich wurde der zugängliche GitHub Bestand abgeglichen. Das früher als `tfpt-theoryv4` bezeichnete Repository ist unter `sthamann/tfpt` erreichbar. Der gefundene Hauptstand ist `66b91e40e245569f06ab440ead80f446c9be0ee5` vom 9. September 2026. Dessen Datei `experiments/theory-contracts/RESEARCH_2026-09-09.md` beschreibt tatsächliche ganzzahlige CAR Felder, die separate Rotorfamilie und den weiter fehlenden nativen Halbladungstransport. Der im Buch genannte Pfad zur neuen Prüfung vom 14. September war über diesen Repository Zugriff nicht verfügbar. Auch die gezielte Suche in der Dateibibliothek lieferte kein zusätzliches passendes Quellenpaket.

**Verschiedene Träger bleiben getrennt:** Eingang ξ, Sternfilter und Feedback betreffen die Vierträgerzelle mit 256 nackten beziehungsweise 544 Sternzuständen. Die Band und Symmetriesätze betreffen den Clebsch Cluster mit 16 Trägern und seinem 24.024 dimensionalen Singulettmultiplikitätsraum. Die gekoppelte Probe verbindet zwei Vierträgerzellen. Keine der neuen Präparationszahlen behauptet eine Herstellung des ganzen Clebsch Grundzustands.

Die neuen Rechnungen importieren **keinen Originalprüfer** dieses Repositorys. Die Zahlen zu 8232 alten Bedingungen, den früheren großen Singulettläufen und anderen Originalkampagnen bleiben Ergebnisse der Anhänge. Sie wurden nicht als eigene Wiederholung gezählt.

Die unabhängigen neuen Programme sind:

| Datei | Aufgabe | Evidenz |
|---|---|---|
| `stabilizer_search.py` | Alle 36.720 reinen Stabilizerzustände des reduzierten Vierqubitproblems | Ganze Zahlen und rationale Überlappe |
| `symmetry_dimensions.py` | Charakterrestriction des Spechtmoduls (4,4,4,4) auf die affine Clebsch Symmetrie | Exakte Charakterrekursion |
| `verify_followups.py` | 256D Eingang und Feedback, 544D Sternfilter, gekoppelte 65536D Probe, LDL, Projektorränge, Uhr, Toffoli und Parameterkontrollen | Gemischt: exakte endliche Algebra und deklarierte Numerik |

Der integrierte Prüfer kontrolliert **2189 Bedingungen**. Davon sind 1920 einzelne affine Graphsymmetrien. Die Zahl ist also keine Anzahl unabhängiger Entdeckungen. Alle drei Programme wurden gewöhnlich und mit `-OO` ausgeführt; die jeweiligen JSON Ausgaben sind bytegleich. Es gibt keine neue Lean Formalisierung, keine Hardwareausführung, keine zertifizierte volle Clebsch Diagonalisierung und keinen neuen globalen empirischen Fit.

## 3. Ein optimaler einfacher Eingang

### 3.1 Ziel und Kodierung

Auf vier Trägern mit je vier Farben lautet der Zielzustand

\[
|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}
\operatorname{sgn}(\pi)|\pi(0),\pi(1),\pi(2),\pi(3)\rangle.
\]

Eine Farbe ist ein Element von \(\mathbb F_2^2\). Die vier Farbwerte werden als 0,1,2,3 kodiert; \(\oplus\) bezeichnet bitweises XOR. Jeder Viererträger besteht in dieser Kodierung aus zwei Qubits.

Definiere

\[
|\xi\rangle=\frac14\sum_{d=0}^3\sum_{u,v=0}^1(-1)^{u+v}
|d,\ d\oplus2\oplus u,\ d\oplus1\oplus2v,
\ d\oplus3\oplus u\oplus2v\rangle.
\tag{1}
\]

Die 16 Wörter sind verschieden, also ist ξ normiert. Zwölf Wörter enthalten alle vier Farben; vier besitzen Farbkollisionen. ξ ist ausdrücklich **nicht** Ω. Auf den zwölf gültigen Wörtern passen seine Phasen bis auf ein gemeinsames Vorzeichen zu Ω. Daher

\[
|\langle\Omega|\xi\rangle|^2
=\frac{12^2}{16\cdot24}=\boxed{\frac38}.
\tag{2}
\]

### 3.2 Tatsächliche Schaltung

Qubits 0 und 1 kodieren Farbe 0 des ersten Trägers, 2 und 3 den zweiten, 4 und 5 den dritten, 6 und 7 den vierten. Das zuerst genannte Qubit ist jeweils das niederwertige Bit. Ausgang ist das Wort mit acht Nullen.

```text
H auf 0, 1, 2, 5
Z auf 2, 5
CNOT 0 -> 2
CNOT 1 -> 3
CNOT 0 -> 4
CNOT 1 -> 5
CNOT 2 -> 6
CNOT 5 -> 7
X auf 3, 4, 6, 7
```

Die Schaltung benötigt vier Hadamard, zwei Z, sechs CNOT und vier X. Ihr vollständiger Zustandsvektor wurde unabhängig mit (1) verglichen. `optimal_seed.qasm` enthält dieselbe Folge als OpenQASM.

Hier werden adressierbare CNOT zwischen den betroffenen Trägern vorausgesetzt. Die Rechnung zeigt deren geringen endlichen Aufwand, nicht ihre native Herkunft aus dem Compiler. Eine Beschränkung auf ausschließlich innerhalb eines einzelnen Viererträgers wirkende Clifford Operationen wäre ein anderer Ressourcenvertrag.

### 3.3 Warum 3/8 das globale Stabilizeroptimum ist

Die Clifford Relabelung

\[
(x_0,x_1,x_2,x_3)\mapsto
(d,a,b,c)=(x_0,x_1\oplus x_0,x_2\oplus x_0,
x_3\oplus x_0\oplus x_1\oplus x_2)
\tag{3}
\]

ist eine invertierbare binäre lineare Abbildung. Auf Ω gilt \(c=0\). Die Werte d sind gleichverteilt. Die sechs Möglichkeiten von a,b sind genau die invertierbaren zweidimensionalen binären Matrizen. Jede Permutation der vier Farben ist eine affine Abbildung von \(\mathbb F_2^2\); die vier Translationen sind gerade Permutationen. Deshalb faktorisiert der Zustand nach (3) in einen Vierqubitzustand φ sowie zwei feste Plusqubits und zwei feste Nullqubits.

Der Träger des nichttrivialen Zustands φ ist

\[
S=\{6,7,9,11,13,14\}\subset\mathbb F_2^4,
\]

mit Vorzeichen \((-1,+1,+1,-1,-1,+1)\) in dieser Reihenfolge und gemeinsamer Betragsamplitude \(1/\sqrt6\).

Für dieses S gelten zwei direkt prüfbare Eigenschaften: XOR über alle sechs Punkte ist null; der affine Spann ist der ganze Raum \(\mathbb F_2^4\).

Ein Stabilizerzustand hat in der Rechenbasis gleich große Betragsamplituden auf einem affinen binären Unterraum. Dies ist die hier verwendete bekannte Normalform, nicht eine TFPT Annahme [P1]. Hat sein Träger Dimension k und trifft er m Punkte von S, liefert die Dreiecksungleichung

\[
|\langle\phi|s\rangle|^2\le\frac{m^2}{6\,2^k}.
\tag{4}
\]

Die maximalen Schnittgrößen für k=0,1,2,3,4 sind 1,2,3,4,6. Für die entscheidenden zwei Fälle gibt es kurze Beweise:

Eine affine Ebene kann nicht vier Punkte von S enthalten. Deren XOR wäre null; wegen des XORs des gesamten S müssten dann die beiden restlichen Punkte identisch sein. Ein Widerspruch.

Eine affine Hyperebene kann nicht genau fünf Punkte von S enthalten. Für die zugehörige nichttriviale affine lineare Gleichung erzwingt das XOR des gesamten S auch den sechsten Punkt. Alle sechs Punkte würden dann in einer Hyperebene liegen, im Widerspruch zum vollen affinen Spann.

In (4) ergeben sich somit die Obergrenzen

\[
\frac16,\quad\frac13,\quad\frac38,\quad\frac13,\quad\frac38.
\]

Der Eingang (1) erreicht 3/8. Das beweist das Optimum im Vierqubitproblem.

Für einen beliebigen achtqubitigen Stabilizerzustand kann man nach der Clifford Relabelung seine vier zusätzlichen Qubits auf die festen Stabilizerfaktoren von Ω projizieren. Der verbleibende Zustand ist entweder null oder ein unnormierter Vierqubit Stabilizerzustand. Seine Erfolgswahrscheinlichkeit ist höchstens eins. Der Überlapp kann deshalb nicht größer sein als das gerade bewiesene Vierqubitoptimum. Durch Konvexität gilt die Grenze auch für gemischte Stabilizerzustände und für klassische Zufallsauswahl.

**Satz:** In dieser Kodierung ist die Stabilizerfidelität von Ω exakt 3/8. Für eine größere Hilfssystemzahl, deren Hilfssysteme am Ende ignoriert werden, gilt dieselbe Grenze für die dadurch erzeugten Stabilizermischungen auf den acht Systemqubits.

Die unabhängige vollständige Suche über 36.720 reine Vierqubit Stabilizerzustände findet 72 Maximierer. Die kleinere Enumeration der 307 affinen Träger bestätigt die fünf Schnittgrößen. Diese Rechnungen kontrollieren den ausgeschriebenen Beweis; sie ersetzen nicht die Normalformannahme durch numerisches Raten.

## 4. Derselbe mikroskopische Filter, höhere Ausbeute

### 4.1 Unverändertes Mikromodell

Verwendet wird genau der Stern aus v1.4:

\[
H_\star=\begin{pmatrix}0&tM^\dagger\\tM&\Delta I_{288}\end{pmatrix},
\qquad M^\dagger M=6I-2G_\star.
\]

Der Raum besitzt 256 nackte Materiezustände und 288 Vermittlerzustände. Der Betriebspunkt ist \(t/\Delta=1/20\). Die 14 verschiedenen Energien und ihre Multiplizitäten wurden aus M neu aufgebaut und auf allen 544 Eigenwerten kontrolliert.

Der bekannte 13 Faktoren Filter ist

\[
K_d=\prod_{j=1}^{13}\frac{I+e^{-i\tau_j(H_\star-E_0)/\hbar}}2=P_{\Omega_d},
\qquad \tau_j=\frac{\pi\hbar}{E_j-E_0}.
\]

Seine Summe der kontrollierten Entwicklungszeiten bleibt

\[
T_\star=3172{,}829634\,\hbar/\Delta.
\]

Ein nur über die sechs anderen niedrigen Energien gebildeter Filter hat in der neuen Negativkontrolle noch eine unerwünschte Amplitudenübertragung von etwa 0,15523 im oberen Band. Die hohen und dunklen Sektoren dürfen nicht ausgelassen werden.

Mit

\[
w=\frac12\left(1+\frac{\Delta}{\sqrt{\Delta^2+24t^2}}\right)
=0{,}9856429311786321
\]

gilt nach Projektion auf leere Vermittler wieder

\[
A=P_{\rm bare}P_{\Omega_d}P_{\rm bare}=wP_\Omega.
\tag{5}
\]

Die neue volle Matrixrechnung bestätigt (5); der maximale Eintragsfehler des vollständigen numerischen Filters gegen den analytischen Projektor beträgt etwa \(1{,}24\cdot10^{-14}\). Dies ist eine Gleitkommakontrolle, keine Intervallzertifizierung.

### 4.2 Neue Rohwahrscheinlichkeiten

Für ξ ergibt sich exakt

\[
p_{\rm prep}=\frac38w^2=0{,}3643094954184012.
\tag{6}
\]

Nach erfolgreicher Präparation folgen unverändert der lokale Dreierzyklus, zwei Austauschrecords mit behaltenem oder frischem Pointer, der Rücktick und derselbe Schlussfilter. Die gemeinsame Rechnung im vollständigen 256D Materieraum liefert

\[
p_{\rm behalten}=\frac38w^4=0{,}3539237558720279,
\]

\[
p_{\rm frisch}=\frac{51}{256}w^4=0{,}1880219953070148.
\tag{7}
\]

Das Verhältnis bleibt 17/32. Der Eingangswechsel verbessert die Ausbeute um 9/4, nicht den idealen Echoquotienten. Alle fehlgeschlagenen Startfilter, Leerbelegungsabfragen und Schlussfilter bleiben als fehlgeschlagene Versuche enthalten.

Die mittlere Zahl unabhängiger Präparationsversuche ist 2,744918847. Pro vollständig durchlaufenem Start und Schluss bleiben 26 kontrollierte schwache Entwicklungen und das Zeitbudget \(2T_\star\), zusätzlich Recordpulse, Eingangsschaltung, Messungen und Reset. Ein früh abgebrochener Fehlversuch kann kürzer sein; eine genaue mittlere Wandzeit benötigt die Abbruchreihenfolge und Resetdauer.

### 4.3 Nur noch ein idealer Verstärkungsschritt

Für den angekleideten Zielzustand ist der neue Eingangsüberlapp

\[
a=|\langle\Omega_d|\xi\rangle|^2=\frac38w
=0{,}369616099191987>\frac14.
\]

Setze \(R_v(z)=I+(z-1)P_v\). In der Ebene aus Ziel und seinem orthogonalen Eingangsanteil ist nach einem Schritt \(R_\xi(z)R_{\Omega_d}(z)\xi\) die unerwünschte Amplitude proportional zu

\[
z+a(z-1)^2.
\]

Für \(|z|=1\) verschwindet sie genau bei

\[
\cos\varphi=1-\frac1{2a}=1-\frac4{3w},
\qquad\varphi=1{,}9313099968443614.
\tag{8}
\]

Damit genügt im erweiterten idealen Phasenvertrag ein Verstärkungsschritt statt zwei. Die selektive Zielphase wird weiterhin durch kohärentes Berechnen aller 13 Filterbits, Phasieren des gemeinsamen Erfolgsrecords und vollständiges Rückrechnen implementiert. Sie braucht 26 kontrollierte H Aufrufe statt der bisherigen 52 für zwei Zielphasen.

Die Eingangsphase \(R_\xi(z)\) ist gesondert zu implementieren: Clifford Vorbereitung rückwärts, selektive Phase auf das Nullwort, Vorbereitung vorwärts. Ihre Mehrfachkontrolle und reelle Phase sind keine kostenlosen Clifford Operationen. Die Aussage halbiert die Anzahl der **Zielphasenaufrufe**, nicht automatisch die gesamten Hardwarekosten.

Nach der deterministischen idealen Präparation des angekleideten Zustands bleibt das anschließende Leerbelegungsherald für nacktes Ω mit Wahrscheinlichkeit w. Deterministisch angekleidet bedeutet nicht deterministisch nackt. In der Negativkontrolle bleibt bei Verwendung der alten Verstärkungsphase eine nichtverschwindende Fehlamplitude.

## 5. Feedback und Fehler bei wirklich gekoppelten Zellen

### 5.1 Allgemeiner Resetüberlapp

Sei

\[
K=P^-_{03}P^-_{02}P^-_{01},\qquad P=P_\Omega,
\]

und \(\rho_s\) irgendein Reset mit \(a=\operatorname{Tr}(P\rho_s)>0\). Der Kanal

\[
\mathcal E_s(\rho)=K\rho K^\dagger+
\operatorname{Tr}[(I-K^\dagger K)\rho]\rho_s
\tag{9}
\]

ist vollständig positiv und spurerhaltend. Aus \(KP=PK=P\) folgt die genaue Gewichtsgleichung

\[
F(\mathcal E_s\rho)=F(\rho)+a\operatorname{Tr}[(I-K^\dagger K)\rho].
\]

Der notwendige Vollraumvergleich lautet

\[
K^\dagger K\le P+\beta(I-P),\qquad
\beta=\frac{9+\sqrt{17}}{32}.
\]

Zusätzlich zum 256D Test wurde sein Spektralpolynom in der treuen regulären S4 Darstellung rational rekonstruiert:

\[
\det(xI-K^\dagger K)=
\frac{x^{12}(x-1)(16x-1)^5(16x^2-9x+1)^3}{2^{32}}.
\]

Der Einsraum im Vierträgerraum ist gerade Ω, weil Gleichheit der Norm bei allen drei orthogonalen Projektionen die gemeinsame Antisymmetrie erzwingt. Die übrigen zulässigen Eigenwerte liegen höchstens bei β. Deshalb gilt

\[
1-F(\mathcal E_s^m\rho)\le r_s^m[1-F(\rho)],\qquad
r_s=1-a(1-\beta).
\tag{10}
\]

Mit \(\rho_s=|\xi\rangle\langle\xi|\) wird

\[
r_\xi=0{,}778786394050207.
\]

56 Zyklen garantieren Infidelität höchstens 10⁻⁶ für jeden Anfangszustand. Ein unabhängiger 256D Lauf aus dem voll symmetrischen Wort 0000 erreicht nach 56 Zyklen etwa \(1{,}21\cdot10^{-11}\). Dieser bessere Einzelwert ersetzt nicht den Worst Case Satz.

### 5.2 Dauerfehler und unabhängige Zellen

Bei höchstens ε Abweichung pro Zyklus in halber Diamantnorm gilt

\[
q_m\le r^m q_0+\epsilon\frac{1-r^m}{1-r},\qquad q=1-F.
\tag{11}
\]

Für den neuen Reset ist der asymptotische Fehlerboden höchstens \(4{,}520517604\epsilon\), neunmal kleiner als zuvor. Eine lokale Zielinfidelität 10⁻⁶ verlangt für den alleinigen asymptotischen Rauschanteil \(\epsilon\le2{,}2121\cdot10^{-7}\). Für einen endlichen Stoppzeitpunkt muss zusätzlich Platz für den noch nicht abgeklungenen Anfangsfehler bleiben.

Für N unabhängig gekühlte Zellen gilt, auch bei anfänglich verschränkten Eingängen,

\[
1-F_{\rm global}\le N\left[r^m+\epsilon\frac{1-r^m}{1-r}\right].
\tag{12}
\]

Bei N=4096 genügen im idealen Fall 89 Zyklen. Die Forderung nach **global** 10⁻⁶ ist unter Rauschen viel strenger als die lokale Forderung: Der asymptotische Fehlbudgetanteil pro Zelle und Zyklus darf dann nur etwa \(5{,}40\cdot10^{-11}\) betragen, bevor der Anfangsfehler eingerechnet wird. Die verbesserte Präparation beseitigt diesen Größeneffekt nicht.

### 5.3 Satz für laufende Zwischenzellkopplung

Nun seien die Zellen wirklich gekoppelt. Ein Zyklus besteht aus der unitären Entwicklung unter einem endlichen, lokal beschränkten \(H_{\rm int}\) für Dauer τ und anschließender paralleler lokaler Kühlung. Für die lokale Zielprojektion \(P_i\) definiere

\[
b_i=\|P_iH_{\rm int}(I-P_i)\|,
\qquad \nu_i=\tau b_i/\hbar.
\]

Eine Summe der Normen der an Zelle i anliegenden Kopplungen ist eine verwendbare obere Schranke für \(b_i\). Bei beschränktem Grad und beschränkten Kopplungsnormen ist sie unabhängig von N.

Für jeden, auch global verschränkten Zustand gilt

\[
|\dot q_i|\le\frac{2b_i}{\hbar}\sqrt{q_i(1-q_i)}.
\]

Das folgt aus dem Offdiagonalblock des Kommutators und Cauchy Schwarz für die beiden Projektionssektoren. Integration liefert die konservative Schranke

\[
\sqrt{q_i(\tau)}\le\sqrt{q_i(0)}+\nu_i.
\]

Nach der Kühlung einschließlich lokalem Kanalfehler ε folgt daher

\[
q_{i,m+1}\le r(\sqrt{q_{i,m}}+\nu_i)^2+\epsilon_i.
\tag{13}
\]

Für gemeinsame Schranken ν und ε besitzt die skalare Hülle den Fixpunkt

\[
x_*=
\frac{r\nu+\sqrt{r\nu^2+(1-r)\epsilon}}{1-r}.
\tag{14}
\]

Die Abbildung \(x\mapsto\sqrt{r(x+\nu)^2+\epsilon}\) ist auf nichtnegativen x höchstens \(\sqrt r\) Lipschitz. Folglich

\[
\sqrt{q_{i,m}}\le x_*+r^{m/2}\max\{0,\sqrt{q_{i,0}}-x_*\}.
\tag{15}
\]

Bei ε=0 ist \(x_*=\sqrt r\nu/(1-\sqrt r)\). Die stationäre lokale Infidelität ist also quadratisch klein in der Kopplungswirkung pro Kühlzyklus. Dies ist eine größenuniforme Aussage für beschränkt gekoppelte Zellen, keine Annahme unabhängiger Systeme.

### 5.4 Tatsächlich ausgeführte gekoppelte Probe

Zwei Ω Zellen wurden als voller Vektor mit 65536 Amplituden aufgebaut und mit einer echten Brücke \(\lambda P^+_{ab}\) entwickelt. Aus dem Produktanfang gilt exakt

\[
q_A=q_B=\frac{15}{16}\sin^2\!\left(\frac{\lambda\tau}{2\hbar}\right).
\tag{16}
\]

Bei \(\lambda\tau/\hbar=0{,}02\) ergibt sich \(q_i=9{,}374687504\cdot10^{-5}\). Die lokale Reinheit ist etwa 0,9998125156 und damit kleiner als eins: Die Brücke verschränkt die Zellen wirklich. Die anschließende Anwendung des lokalen Feedbackkanals erfüllt den Bound \(q_i'\le rq_i\) für beide echten Marginalen.

**Grenze des Satzes:** Sein Ziel ist lokale Nähe zu Ω bei laufender Kopplung. Er bereitet nicht den verschränkten Grundzustand des gesamten wechselwirkenden Hamiltonoperators vor. Exakt reine lokale Ω Zustände und nichttriviale Zwischenzellverschränkung sind ohnehin unvereinbar. Für globale Produktfidelität muss zusätzlich über alle lokalen Defekte summiert werden.

## 6. Wer bedient das Labor?

### 6.1 Ein vollständiger endlicher Vertrag ist formulierbar

Für eine ausführbare Erweiterung genügen ausdrücklich deklarierte Träger und Zugriffe: harte leere oder vierfarbige Materieplätze, antisymmetrische Vermittler mit Kantenadresse, Pointerqubits, die oben benötigten Clifford Operationen, resonante und schwache adressierte Wedge Kopplungen, kohärentes Kopieren der Vermittlerbelegung, frische Hilfsregister und eine Programmuhr.

Die lokale Belegungsaufzeichnung kann auf einem Sektor mit \(n_b\in\{0,1\}\) durch

\[
H_Q=\frac{\pi\hbar}{2\tau_Q}\,n_b\otimes(I-X)
\]

realisiert werden: Ihre Entwicklung für \(\tau_Q\) wirkt als Identität bei leerem Vermittler und als X auf dem Pointer bei besetztem Vermittler. Die resonante Kopplung und ihr Adjungiertes ergeben zusammen mit dieser Aufzeichnung den bereits in v1.4 geprüften Austauschrecord. Die Besetzungsinformation unterscheidet nicht die beiden geordneten Farbwege einer antisymmetrischen Paaramplitude.

Kontrolliertes H benötigt den entsprechenden bedingten Hamiltonoperator \(|1\rangle\langle1|\otimes H\) und die Phasenreferenz für die Energieverschiebung. Kantenisolation benötigt Auswahl der jeweiligen Kopplung. Diese Operatoren sind im Vertrag explizit, aber durch ihre Schreibbarkeit noch nicht aus TFPT hergeleitet.

### 6.2 Autonomer Controller statt äußerer Pulsfolge

Für eine endliche Folge unitärer Makros \(U_1,\ldots,U_L\), einschließlich unitärer Erweiterungen von Messungen und endlichen Resetvorgängen, setze

\[
H_{\rm prog}=\sum_{\ell=0}^{L-1}g\sqrt{(\ell+1)(L-\ell)}
\left(|\ell+1\rangle\langle\ell|\otimes U_{\ell+1}+\mathrm{h.c.}\right).
\tag{17}
\]

Die blockdiagonale Transformation mit den Präfixprodukten \(V_\ell=U_\ell\cdots U_1\) bringt (17) auf eine reine Uhrkette mit Hamiltonoperator \(2gJ_x\). Somit gilt nach

\[
T=\frac{\pi\hbar}{2g}
\]

exakt

\[
|0\rangle|\psi\rangle\longmapsto
(-i)^L|L\rangle U_L\cdots U_1|\psi\rangle.
\tag{18}
\]

Die zugrunde liegende perfekte Zustandsübertragung mit festen Kopplungen ist eine bekannte Methode [P3]. Die hier angegebene Anheftung der Labormakros und ihre Ressourcenbilanz sind die konkrete Anschlusskonstruktion. Kettenlängen 3,7,13,26 wurden numerisch kontrolliert.

Wesentlich ist \(\|H_{\rm prog}\|=gL\). Bei festem Energiebudget \(E_{\max}\) ist \(g=E_{\max}/L\) zu wählen, also \(T=\pi\hbar L/(2E_{\max})\). Konstante Laufzeit bei wachsendem L würde ein wachsendes Energiebudget voraussetzen. Außerdem tragen die festen Kopplungen und Makros das Programm selbst. Die Konstruktion beseitigt zeitabhängiges äußeres Schalten, nicht die Auswahl des Programms oder die Herkunft der Zeitkalibrierung.

### 6.3 Reset und Entropie

Ein beliebiger Eingang einer 256D Zelle kann mit einem frischen 256D Register im Nullzustand vertauscht werden; anschließend stellt die feste Clifford Schaltung ξ her. Der alte Quantenzustand liegt dann im Register und ist nicht verschwunden.

Wenn eine globale unitäre Operation jeden der 256 orthogonalen Eingänge auf denselben reinen Systemzustand abbildet, müssen ihre Umgebungszustände orthogonal sein. Eine Umgebungskapazität von mindestens 256 Dimensionen, entsprechend acht Qubits, ist dafür notwendig. Das ist eine Informationskapazitätsschranke, keine allgemeine Behauptung von acht minimalen Wärmebits in jeder konkreten thermischen Ausführung. Eine Wärmebilanz benötigt Reservoirzustand, Hamiltonoperator, Korrelationen und Löschprotokoll [P4].

Ein endliches geschlossenes System mit festem Anfangsregister hat nur ein endliches Frischregisterbudget. Beliebig lange irreversible Kühlung verlangt einen wachsenden Vorrat oder einen physikalisch erklärten Entropieabfluss. Der kosmologische Zeitpfeil ist dadurch nicht ausgewählt.

### 6.4 Was der bisherige reine Clifford Teil nicht leisten kann

Clifford Operationen, Stabilizerhilfen, Pauli Messungen und klassisches Feedback bleiben innerhalb der Stabilizermischungen. Nach Abschnitt 3 können sie Ω nicht mit mehr als 3/8 Fidelität vorbereiten. Eine bessere oder exakte Präparation benötigt eine zusätzliche Ressource. Im untersuchten Labor liefert sie der kohärente Austauschrecord beziehungsweise die kontinuierliche Wedge Entwicklung.

Die Herkunftsfrage wird dadurch entscheidbar: Man muss mindestens einen tatsächlich zugelassenen primitiven Zugriff außerhalb der reinen Clifford Instrumentklasse nachweisen. Eine erneute Aufzählung der 60 Projektoren oder ihrer Symmetrie kann diesen Zugriff nicht ersetzen.

## 7. Welche Vermittlerarchitektur wird ausgewählt?

### 7.1 Was Lokalität nicht entscheidet

Eine Bank pro Zelle und eine Bank pro Kante sind beide lokal, solange die Zellgröße fest bleibt und Zwischenzellkopplungen beschränkt sind. Die beiden Modelle besitzen verschiedene vierte Ordnungen und verschiedene Gapkorrekturen. Die v1.4 Gegenüberstellung bleibt richtig.

### 7.2 Ein stärkeres, hinreichendes Auswahlkriterium

Betrachte Paarabbauoperatoren \(K_e\) für Kanten e=(i,j) und Vermittlermoden \(b_\alpha\):

\[
H_{\rm int}=\sum_{e,\alpha}t_{e\alpha}b_\alpha^\dagger K_e+\mathrm{h.c.}
\]

Nehme zusätzlich erhaltene lokale additive Ladungen an,

\[
Q_v=n_f(v)+\sum_\alpha q_{v\alpha}n_\alpha.
\tag{19}
\]

Dann gilt

\[
[Q_v,b_\alpha^\dagger K_e]=
\left(q_{v\alpha}-\mathbf1_{v=i}-\mathbf1_{v=j}\right)b_\alpha^\dagger K_e.
\tag{20}
\]

Sofern die verschiedenen elementaren Übergänge linear unabhängig sind, verlangt \([Q_v,H]=0\) für alle v und \(t_{e\alpha}\ne0\)

\[
q_{v\alpha}=\mathbf1_{v\in e}\quad\text{für alle }v.
\tag{21}
\]

Verschiedene Kanten haben verschiedene Inzidenzvektoren. Eine Mode kann daher nicht unverändert zwei verschiedenen Kanten als Vermittler dienen. Bei kommutierenden hermiteschen Ladungsmatrizen im Einvermittlerraum gilt dieselbe Aussage nach gemeinsamer unitärer Diagonalisierung. Sie hängt dann nicht nur an diagonalen Vorzeichenwechseln.

**Bedingter Auswahlssatz:** Die erklärte lokale additive Ladungserhaltung und die erklärte Vertexklasse erzwingen Vermittlermoden mit Kantenadresse. Lokalität allein tut das nicht.

Aus der vollständig belegten Quelle \(Q_v=1\) folgt anschließend die Matchingstruktur der besetzten Vermittler. Der in v1.4 bewiesene allordentliche CAR Adapter ist auf genau diesem Sektor anschließbar.

### 7.3 Die neue Voraussetzung darf nicht verschwinden

Die Erhaltung von (19) ist eine zusätzliche physikalische Forderung. Der Compiler muss begründen, warum seine Dynamik sie besitzt. Im Clebsch Modell gibt es 40 Kanten, während jedes der zehn Vektorlabels vier Kanten bezeichnet. Eine kantenadressierte Realisierung benötigt diese zusätzliche Adressinformation im physischen Träger. Daraus folgt kein allgemeines Verbot durch die Zahl 248; Lie Generatorraum und Vielteilchenraum sind verschiedene Objekte.

Vermittlerhopping, gemischte Ladungssektoren oder dynamische Umbindung müssen ihre Ladungstransporte eigens erklären. Sie werden nicht durch den Satz über den unveränderten Vertex abgedeckt. Ebenso ist die Deutung eines D5 Gewichtsplatzes als Ort mit einer beliebigen ungebrochenen inneren Mischung dieser Plätze nicht automatisch verträglich.

## 8. Spektren: neue exakte Reduktionen und Schranken

### 8.1 Ein analytischer Beweis der positiven vierten Ordnung

Für gleich normierte kantenlokale Vermittler gilt aus v1.4

\[
F_4=\sum_v A_v(A_v-I),\qquad A_v=\sum_{e\ni v}(I-S_e).
\tag{22}
\]

Bei einem Vertex mit Grad d ist \(A_v=dI-X_{d+1}\), wobei \(X_{d+1}\) die Summe der d Transpositionen des Sternmittelpunkts mit seinen Nachbarn ist. Dies ist ein Jucys Murphy Operator. In Youngs Basis sind seine Eigenwerte ganzzahlige Kästcheninhalte [P2]. Da \(A_v\ge0\), sind alle seine Eigenwerte nichtnegative ganze Zahlen. Daher ist \(A_v(A_v-I)\ge0\).

Der Beweis gilt für jeden endlichen Graphen in dieser **ungewichteten, gleich normierten** Vertexklasse. Beliebige unterschiedliche Kantengewichte würden die Ganzzahligkeit im Allgemeinen verlieren. Die frühere 720D Kontrolle wird durch diesen analytischen Satz erklärt, nicht zur Grundlage einer unbegrenzten Aussage über andere Kopplungen gemacht.

### 8.2 Zusätzliche Schranken speziell für vier Farben

Ein Clebsch Stern hat sechs beteiligte Viererträger. In \((\mathbb C^4)^{\otimes6}\) treten nur Youngformen mit höchstens vier Zeilen auf. Die relevanten Kästcheninhalte liegen zwischen −3 und 5. Deshalb

\[
\operatorname{spec}(A_v)\subset\{0,1,\ldots,8\}.
\]

Es folgen zwei Operatorungleichungen:

\[
A_v(A_v-I)\le7A_v,
\qquad (A_v-7I)(A_v-8I)\ge0.
\]

Mit \(A=\sum_e(I-S_e)=80I-2H_0\) und \(\sum_vA_v=2A\) ergibt sich

\[
0\le F_4\le1120I-28H_0,
\qquad F_4\ge1344I-56H_0.
\tag{23}
\]

Insbesondere gilt am Betriebspunkt

\[
H_{\rm tr}=H_0+\frac1{800}F_4
\ge\frac{93}{100}H_0+\frac{42}{25}I.
\tag{24}
\]

Eine zertifizierte nackte Nichtsingulettuntergrenze \(H_0\ge58/5=11{,}6\) würde daher

\[
H_{\rm tr}\ge\frac{3117}{250}=12{,}468
\]

ergeben. Das liegt über der in v1.4 berichteten variationalen Viererraumenergie 12,44702377595. Für diesen Ausschluss muss also nicht das nackte Minimum 12,133537149... auf viele Stellen zertifiziert werden. Es genügt die gröbere rationale Schwelle 11,6, **sofern sie tatsächlich für alle Nichtsinguletts bewiesen wird**. Diese Untergrenze und die erforderliche zertifizierte Obergrenze wurden in dieser Runde nicht hergestellt.

### 8.3 Verbesserung der äußeren Bandtrennung

Die kantenlokale Vergleichsmatrix hat Diagonale 1 bis 8 und quadrierte Nebendiagonalen

\[
\frac1{400}(124,144,136,120,84,56,16).
\]

Die Zahl 80 gehört zur Verbindung des nackten Sektors mit dem ersten Vermittlersektor und nicht zur ersten Nebendiagonale des reinen Q Blocks.

Nach Abzug von \(18/25\) sind die LDL Pivots exakt

\[
\frac7{25},\ \frac{121}{700},\ \frac{597}{3025},\
\frac{46483}{29850},\ \frac{4749806}{1162075},\
\frac{2483493993}{474980600},\
\frac{388246124801}{62087349825},\
\frac{70598707363957}{9706153120025}.
\]

Alle sind positiv. Somit gilt im benannten endlichen C16 Modell

\[
QHQ\ge\frac{18}{25}\Delta Q.
\tag{25}
\]

Die äußere Bandtrennung beträgt mindestens **0,72 Δ**. Die versuchte Schwelle 0,8 Δ scheitert weiterhin am zweiten Pivot. Dies ist kein innerer Singulettgap, kein kanonischer Restbound und kein thermodynamischer Satz.

### 8.4 Exakte Projektoren für die Vierfachheitsfrage

Die Clebsch Vertizes sind die geraden Fünfbitwörter. Die 16 geraden Translationen bilden \(T\cong\mathbb F_2^4\); die fünf Koordinaten können durch S5 permutiert werden. Die 1920 so konstruierten affinen Transformationen erhalten alle 40 Kanten. Es genügt diese tatsächlich konstruierte Symmetriegruppe; ihre eventuelle Maximalität ist für die folgenden Projektoren nicht nötig.

Der SU(4) Singulettmultiplikitätsraum ist das Spechtmodul \((4,4,4,4)\). Eine exakte Charakterrechnung liefert

\[
\chi(1^{16})=24024,\qquad\chi(2^8)=280.
\]

Daher besitzt

\[
P_T=\frac1{16}\sum_{t\in T}U_t
\]

den Rang \((24024+15\cdot280)/16=1764\). Jeder nichttriviale einzelne Translationscharakter besitzt Rang 1484.

Im translationsinvarianten Raum lautet die S5 Zerlegung:

| Youngform von S5 | Irreduzible Dimension | Multiplizität | Isotypischer Rang |
|---|---:|---:|---:|
| (5) | 1 | 28 | 28 |
| (4,1) | 4 | 80 | 320 |
| (3,2) | 5 | 86 | 430 |
| (3,1,1) | 6 | 80 | 480 |
| (2,2,1) | 5 | 66 | 330 |
| (2,1,1,1) | 4 | 42 | 168 |
| (1,1,1,1,1) | 1 | 8 | 8 |

Die Symmetrie wirkt auf den nichttrivialen Translationscharakteren in Bahnen der Größen 5 und 10. Ein irreduzibles Vierermultiplett kann deshalb nur aus den beiden vierdimensionalen S5 Typen des translationsinvarianten Raums stammen. Eine zufällige Gleichheit mehrerer eindimensionaler Niveaus wird dadurch nicht ausgeschlossen.

Sei S4 die Untergruppe von S5, die eine Koordinate festhält, und

\[
A_k=\frac1{|S_k|}\sum_{\sigma\in S_k}U_\sigma,
\qquad
A_k^- =\frac1{|S_k|}\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)U_\sigma.
\]

Dann sind

\[
P_{80}=P_T(A_4-A_5),\qquad
P_{42}=P_T(A_4^--A_5^-)
\tag{26}
\]

orthogonale Projektoren mit Rängen **80** und **42**. Untergruppenmittel sind verschachtelte orthogonale Projektionen; die Differenzen sind deshalb wieder Projektionen. Die Restriktionsregel \(\mathrm{Ind}_{S_4}^{S_5}1=1\oplus(4,1)\), beziehungsweise ihre Signumverdrehung, zeigt, dass sie jeweils eine Zeile pro Kopie des betreffenden Vierertyps auswählen.

Sowohl \(H_0\) als auch \(F_4\) kommutieren mit (26). Ihre Beschränkungen auf diese Räume enthalten daher die beiden tatsächlichen Multiplizitätsmatrizen von Größe 80 und 42. Ein einfacher Eigenwert einer solchen Matrix erzeugt ein vierfaches Niveau im entsprechenden isotypischen Raum.

**Was damit gelöst ist:** Die Projektoren und ihre Ränge sind exakt; die relevante Strukturreduktion ist abgeschlossen.

**Was nicht damit gelöst ist:** Welcher der beiden Räume das erste angeregte Niveau trägt; Einfachheit des entsprechenden reduzierten Eigenwerts; Ausschluss zusätzlicher Gleichheiten mit anderen Symmetrietypen und SU(4) Sektoren; der Rest der vollen Mikrodynamik. Eine kleine Matrix ist noch kein bereits ausgeführter Intervallbeweis ihres Spektrums.

## 9. Die analytische Halbladungsfrage T2

### 9.1 Der richtige Ladungsvektor

Die Halbkomponenten des E8 Glue Operators dürfen nicht mit einem einzelnen freien Bosonfeld der Ladung 1/2 verwechselt werden. Im markierten E8 Referenzgitter ist

\[
\alpha=(1/2,\ldots,1/2),\qquad \|\alpha\|^2=2,
\qquad h_\alpha=1.
\]

Der D5 Anteil trägt Gewicht 5/8, der A3 Anteil 3/8. Gemeinsam liegt ein Gewicht eins Strom vor. Das freie Einbosonvakuumbeispiel aus v1.4 prüft eine andere Normierungsaufgabe.

### 9.2 Energie und Adjunkte im erklärten Referenzmodell

Nehme hier ausdrücklich die unitäre affine E8 Darstellung auf Niveau eins beziehungsweise die äquivalente positive E8 Gittertheorie als **zusätzliche Referenz**. Ihre Unitarität gehört zur etablierten Theorie [P5]. Auf dem gemeinsamen dichten Raum endlicher Energie seien die hermiteschen Strommoden so normiert, dass \((J_n^a)^\dagger=J_{-n}^a\) und der zentrale Term für ein normiertes a gleich n ist.

Die Sugawara Identität mit \(h^\vee=30\) lautet

\[
62L_0=\sum_a(J_0^a)^2+
2\sum_{m>0,a}J_{-m}^aJ_m^a.
\tag{27}
\]

Für positive Moden folgt \(\|J_m^a\psi\|^2\le31\langle\psi,L_0\psi\rangle\). Für negative Moden kommt durch den Kommutator \(m\|\psi\|^2\) hinzu; für den Nullmodus genügt die Konstante 62. Insgesamt erhält man die sichere Abschätzung

\[
\|J_n^a\psi\|\le\sqrt{62+|n|}\,
\|(L_0+1)^{1/2}\psi\|.
\tag{28}
\]

Für glatte Modenkoeffizienten ergibt sich

\[
\|J^a(f)\psi\|\le
\left(\sum_n|f_n|\sqrt{62+|n|}\right)
\|(L_0+1)^{1/2}\psi\|.
\tag{29}
\]

Damit sind die verschmierten Gewicht eins Felder auf einer gemeinsamen energiegewichteten Domäne kontrolliert, nicht nur auf dem Vakuum. Die durch endliche lineare Kombinationen gewonnenen komplexen Wurzelströme haben entsprechende Bounds mit dem aus ihren Koeffizienten folgenden konstanten Faktor. Ihre positiven und negativen Wurzeln sind die passenden Adjunkte. Die dichte formale Adjungiertenrelation liefert Abschließbarkeit.

Für die vollständige unitäre Erweiterung stehen darüber hinaus allgemeine Sätze zu Energieabschätzungen von Erweiterungen affiner Vertexoperatoralgebren zur Verfügung [P6]. Diese Literatur bestätigt die analytische Referenzmethode, nicht den physikalischen TFPT Ursprung.

### 9.3 Was der native Nachweis zusätzlich leisten muss

Erforderlich bleibt ein aus der tatsächlichen Quellfamilie gewonnener Transport der Halbladungssektoren einschließlich Normierung, Clockmarkierung, Cocycle, gemeinsamer Energiebeherrschung und beiden Adjunkten. Die zugängliche Quellrechnung zum QWZ Streifen liefert ganzzahlige geladene CAR Felder in einem anderen benannten Modell. Acht unabhängig hineingesetzte Kopien oder ein nachträglich ergänztes Ladungsregister sind noch nicht dieser Transport.

Die Paritätsobstruktion aus v1.4 bleibt gültig: Eine Algebra, die mit \((-1)^{2Q}\) kommutiert, erzeugt durch Produkte und geeignete starke Grenzwerte keine Operation, die damit antikommutiert. Ein größerer Quellsektor muss tatsächlich konstruiert werden. Der Referenzsatz (29) löst die Energieabschätzung **nach** dieser Erweiterung, nicht ihre Herkunft.

## 10. Eine gemeinsame Welt: Dimension, Chiralität, Photonen und Gravitation

### 10.1 Warum ein gutes Labor noch keine Feldtheorie ist

Die Produktfamilien \(C_{16}\times(\mathbb Z/L\mathbb Z)^d\) im Buch reproduzieren ihre vorgegebene Dimension d. Ein konstruierter Fluss drei reproduziert Index drei. Ein ausgewähltes zweikomponentiges Hauptsymbol reproduziert einen Lorentzkegel. Diese getrennten Kontrollen sind korrekt, aber sie bestimmen keine gemeinsame native Familie.

Eine vollständige Quelle muss eine Folge \((\mathcal A_L,H_L,\omega_L)\) zusammen mit ihrer physikalischen Skalierung auswählen. Dimension, chirales Maß, Kopplungen und gravitativer Sektor müssen aus den Korrelatoren derselben Folge folgen. Das direkte Produkt unabhängiger passender Referenzmodelle erfüllt diese Auswahlaufgabe nicht.

### 10.2 Eine stärkere Spektralentscheidung

Angenommen, eine ausgewählte Familie besitzt bei festgehaltener physikalischer Zeitkalibrierung einen eindeutigen Grundzustand und eine positive, größenuniforme **vollständige physische** Anregungslücke δ. Dann hat die verbundene Vakuumkorrelation einer Observable O die spektrale Form

\[
C_O(t)=\int_{\delta}^{\infty}e^{-iEt/\hbar}\,d\mu_O(E).
\tag{30}
\]

Solange diese uniform leere Spektralregion und derselbe Energiebegriff im Grenzprozess erhalten bleiben, kann kein normalisierter Grenzkorrelator plötzlich positives Spektralgewicht bei beliebig kleinen Energien entwickeln. Ein Projektor auf Tensorcharakter ändert daran nichts. Auch Wechselwirkungen helfen nicht, solange der vorausgesetzte vollständige Gap bestehen bleibt.

**Folgerung:** Eine überall vollständig gegappte Phase aus den Laborzellen kann in demselben skalierten physikalischen Sektor keine masselosen Photonen oder Gravitonen liefern. Die äußere Vermittlerlücke darf positiv bleiben; die relevanten kollektiven niedrigen Anregungen müssen dagegen einen geeigneten lückenlosen Grenzprozess besitzen. Ein lokaler Bindungsgap und ein global masseloser Sektor sind nicht derselbe Gap.

Dies ist kein Ausschluss des Universalraums. Es entscheidet, welche Art von Phase eine erfolgreiche Fortsetzung suchen muss. Die Verbesserung der äußeren Bandtrennung von 0,7 auf 0,72 Δ beantwortet diese andere Frage nicht.

### 10.3 Gemeinsamer Kegel und chirales Maß

Eine Familie von Propagatoren muss nicht nur für jede Materieart eine lineare Dispersion zeigen, sondern nach gemeinsamer Normierung dieselbe kausale Metrik. Ein gemeinsamer Graph allein lässt unterschiedliche Geschwindigkeiten und damit unterschiedliche Kegel zu. Eine zulässige Flavourkopplung oder Symmetrie könnte Geschwindigkeiten verbinden; diese Wirkung muss aus der Quelle berechnet werden.

Eine numerische Nullmodenzahl ersetzt weder ein vollständiges chirales Maß noch das Ausschalten aller Spiegelpartner. Der schon dokumentierte Fluss null mit zwei Nullmoden bei Nettoindex null ist eine konkrete Warnung. Die üblichen lokalen Anomaliesummen einer Standardmodellfamilie verschwinden auch nach N facher Wiederholung; die Zahl schwacher Dubletts bleibt 4N und damit gerade. Diese Anomalietests wählen daher für sich nicht N=3 aus.

### 10.4 Spin zwei

Notwendig ist ein tatsächlicher masseloser Pol in einem positiven physischen Sektor, mit zwei Helizitäten, passenden Constraints und universeller weicher Kopplung. Die in v1.4 hergeleitete Wardbedingung erzwingt Universalität **unter Annahme** dieses Pols. Sie erzeugt ihn nicht. Ein hier ausgeführter Nachweis des benötigten kritischen Spin zwei Sektors liegt nicht vor.

Eine fertige Einstein Wirkung einfach als Zusatz einzusetzen würde ein Referenzmodell liefern. Sie als danach abgeleitete TFPT Wirkung auszugeben wäre ein Zirkelschluss. Der fehlende gemeinsame Quellkorrelator wird durch keine der neuen endlichen Rechnungen ersetzt.

## 11. Dieselben Parameter: Kosmologie und Flavour

### 11.1 Unveränderter Inflationszweig

Für die im Buch eingefrorene einfache Branche gilt

\[
A_s=\frac{N^2c_3^7}{24\pi^2},\qquad
n_s=1-\frac2N,\qquad r=\frac{12}{N^2},\qquad c_3=\frac1{8\pi}.
\]

Daraus folgen ohne N

\[
A_s(1-n_s)^2=\frac{c_3^7}{6\pi^2},\qquad
r=3(1-n_s)^2.
\tag{31}
\]

Die ACT Referenz ist ausdrücklich Tabelle 5 der Fassung v2, Spalte P-ACT-LB2 [P7]. Die Tabelle wurde visuell geprüft. Sie gibt \(n_s=0{,}9752\pm0{,}0030\) und \(\log(10^{10}A_s)=3{,}062\) an. Dies ist keine Behauptung, damit jede kosmologische Auswertung bis September 2026 abzudecken.

Die unabhängige Rechnung reproduziert

\[
A_s=2{,}1370254959916\cdot10^{-9},\quad
N_A=56{,}6239099001,\quad
n_{s,A}=0{,}9646792317322,\quad
r_A=0{,}00374267001309.
\]

Der Abstand des vorhergesagten Tilts zum genannten marginalen Zentralwert beträgt etwa 3,5069 angegebene Standardabweichungen. Bei Kalibrierung auf den zentralen Tilt entsteht die 2,028415503 fache Amplitude. Das ist der bereits in v1.4 erkannte Branchentest, hier unabhängig nachgerechnet, keine neue gemeinsame Likelihoodauswertung.

### 11.2 Was eine Reparatur tatsächlich ändern müsste

Das Verhältnis beobachtetes zu eingefrorenem Invariantenprodukt beträgt

\[
\frac{A_s^{\rm ref}(1-n_s^{\rm ref})^2}
{c_3^7/(6\pi^2)}=0{,}4929956404243.
\tag{32}
\]

Eine Änderung ausschließlich der E Faltungszahl, etwa durch eine andere Reheatingzuordnung bei unveränderten Formeln, kann (32) nicht reparieren. Sie verschiebt den Punkt nur entlang derselben Kurve.

Ein rein algebraisches Treffen beider Zentralwerte durch Änderung von c3 verlangt

\[
c_3'/c_3=0{,}9039001112201.
\]

Als Gegenkontrolle wurde genau diese Änderung in die **wörtlich im Hauptdokument angegebene** elektromagnetische Gleichung eingesetzt; ihre übrigen Terme, darunter \(1/(6\pi)\), blieben unverändert. Der Kehrwert der positiven Zielwurzel ändert sich dann von

\[
137{,}0359992168407\quad\text{zu}\quad167{,}8032986296329.
\tag{33}
\]

Das ist keine zulässige neue physikalische Parametrisierung: P1 fixiert c3 bereits. Es ist eine Sensitivitätskontrolle, die zeigt, dass c3 nicht als folgenloser separater Kosmologieschalter benutzt werden kann. Eine konsistente Korrektur muss eine neue Wirkung samt gemeinsamen Veränderungen ihrer Ausgaben herleiten. Ein Theoriefehler, eine neue Transferrechnung oder ein korrelierter Fit wurde hier nicht erzeugt.

### 11.3 Drei Massen sind noch keine Mischung

Der konstante gemeinsame Skalarüberlapp aus v1.4 ergibt \(Y_f=y_fI\). Auch eine bloße gemeinsame nichtkonstante Matrix löst die Mischungsfrage nicht. Gelten in zwei Sektoren

\[
Y_u=c_uY_0,\qquad Y_d=c_dY_0,
\]

so folgt

\[
[Y_uY_u^\dagger,Y_dY_d^\dagger]=0.
\tag{34}
\]

Beide linken Massenmatrizen sind gleichzeitig diagonalierbar. Eine physikalisch nichttriviale CKM Mischung und ein entsprechendes CP verletzendes Jarlskoginvariant entstehen daraus nicht. Degenerierte Massen erlauben Basisfreiheit, aber keine dadurch messbar gewonnene Mischung.

Ein erfolgreicher gemeinsamer Flavourvertrag benötigt folglich sektorabhängige, nicht gleichzeitig diagonalisierbare Überlappungen aus **derselben** Quelle. Verschiedene Ladungen, rechte Moden, Felder oder Quellkopplungen können das leisten; sie müssen aber abgeleitet und nicht als unabhängige Wunschtexturen eingesetzt werden. Die vollständigen Neutrinotexturen und ihre Skala bleiben ebenfalls zu bestimmen.

## 12. Arithmetik und eine konkrete Rechenbrücke

### 12.1 Aus dem Record folgt ein Toffoli Makro

Für den Austauschrecord

\[
R=P_+\otimes I+P_-\otimes X
\]

gilt nach Hadamard auf dem Pointer c

\[
H_cRH_c=|0\rangle\langle0|_c\otimes I+
|1\rangle\langle1|_c\otimes S.
\tag{35}
\]

Dies ist ein kontrollierter Swap. Werden pro Viererträger nur die Farben 0 und 1 als logisches Qubit benutzt, bleibt der entsprechende Zweizustandsraum unter diesem Swap invariant. Mit adressierbarem CNOT folgt die exakte Identität

\[
\mathrm{CCX}_{c,b\to a}
=\mathrm{CX}_{a\to b}\,H_cR_{c;ab}H_c\,\mathrm{CX}_{a\to b}.
\tag{36}
\]

Die Wirkung ist \(a\mapsto a\oplus bc\), während b und c unverändert bleiben. Die vollständige 32D Recordidentität und alle acht logischen Eingänge von (36) wurden kontrolliert.

Das ist ein endlicher nichttrivialer Compilerbaustein: zwei CNOT, zwei Hadamard und ein Recordmakro. Zusammen mit dem geeigneten Einqubitrepertoire ist universelle Quantenrechnung anschließbar; die allgemeine Universalitätsaussage ist bekannt [P8]. Für eine polynomiell skalierende Implementierung müssen dieselben adressierten Makros auf wachsenden Registern verfügbar sein, das Routing polynomiell bleiben und die gewünschte Genauigkeit mit kontrolliertem Aufwand erreichbar sein. Der kleine Sternfilter allein beweist das nicht.

### 12.2 Was dies für Faktorisierung heißt

Unter einem solchen skalierbaren universellen Quantenvertrag ist der bekannte Shor Algorithmus für Faktorisierung anschließbar [P9]. Das ist eine konkrete bedingte Rechenroute, aber kein neuer klassischer Faktorisierungsalgorithmus und keine aus TFPT bewiesene physische Maschine. Ihre Laufzeit darf nicht von unbezahlt präzisen Zeiten, unendlich großen Registern oder einem faktorkodierten Anfangszustand abhängen.

Die alte quadratische E8 Gaußauslesung wird durch (36) nicht nachträglich verbessert: Ihre Fourierwahrscheinlichkeit hängt im beschriebenen Vertrag nur vom bereits aus t,N berechenbaren \(\gcd(t,N)\) ab. Sie bleibt für sich kein Faktorisierungsgewinn.

### 12.3 RH und P versus NP

Für RH fehlt weiterhin die Identität der vollständigen signierten Weil Form mit einer unabhängig definierten nichtnegativen Norm auf dem gesamten zulässigen Testraum, einschließlich Rändern, Adjungierten und Grenzwerten. Die Positivität von F4 oder einer endlichen Quanten Gram Matrix ist eine andere Form. Es wurde hier kein arithmetischer Positivitätsbeweis konstruiert.

Die bedingte Quantenuniversalität entscheidet P versus NP nicht. Ein Quantenverfahren für Faktorisierung ist weder ein deterministischer polynomialer Algorithmus für sämtliche NP Probleme noch ein Beweis, dass ein solcher Algorithmus nicht existiert. Auch diese Frage ist durch die neuen Laborresultate nicht geschlossen.

## 13. Weitere im Hauptdokument offene Physik

| Frage | Eine tatsächliche Lösung müsste liefern | Stand dieser Fortsetzung |
|---|---|---|
| Dunkle Materie | Stabilen oder ausreichend langlebigen Sektor, Kopplungen, Produktion und Reliktdichte | Kein solcher gemeinsamer Sektor konstruiert |
| Dunkle Energie | Gravitativ wirksame Vakuumantwort mit kontrollierter radiativer Stabilität | Keine entsprechende Wirkung hergeleitet |
| Baryogenese | Quellseitige CP Verletzung, Nichtgleichgewicht und berechnete Asymmetrieausbeute | Ein Baryonenanteil als Formel ersetzt diese Dynamik nicht |
| Starkes CP | Schutz beziehungsweise Auswahl im vollständigen fermionischen Maß, einschließlich Korrekturen | Kein vollständiger Schutzsatz aus dem E8 Vorzeichenmuster |
| Schwarze Löcher | Tatsächlichen Gravitationssektor, Horizonte, Entropiebeziehung und kontrollierte Informationsdynamik | Endliche Records genügen dafür nicht |
| Messproblem und Zeitpfeil | Konsistente Ereignisstatistik sowie Auswahl und Stabilität der Aufzeichnungen | Der neue Controller erklärt eine unitäre Ausführung, nicht die Auswahl eines Ereignisses oder kosmologischen Anfangszustands |
| Higgs, Protonzerfall und weitere negative Zahlenzweige | Vorab festgelegte Wirkung, Schwellen, RG und Unsicherheiten | Die im Buch dokumentierten ungünstigen Zweige bleiben bestehen; kein neuer vollständiger Transferlauf |

Diese Punkte werden nicht durch eine Umbenennung des Registerzustands zu dunkler Materie, der Entropie zu Vakuumdruck oder eines Tensorprojektors zu Gravitation gelöst. Ein konsistentes erweitertes Referenzmodell wäre möglich, würde aber als zusätzliches Modell und nicht als aus TFPT abgeleitete Realität geführt.

## 14. Ergebnis nach den sechs Folgefragen und T1 bis T8

### 14.1 Sechs Fragen

**Wer bedient das Labor?** Eine autonome endliche Programmausführung ist konstruiert, der optimale einfache Eingang samt Schaltung ist gefunden, und ein konkretes nichtlineares logisches Makro ist abgeleitet. Die native Auswahl der dafür erforderlichen primitiven Kopplungen und des Programms ist nicht geschlossen.

**Welche Bauweise ist vorgeschrieben?** Lokale additive Ladungserhaltung wählt die kantenadressierte Variante innerhalb der deklarierten Vertexklasse. Ohne diese oder eine andere aus der Quelle gewonnene Zusatzbedingung bleiben beide lokalen Architekturen zulässig.

**Ist die Vierfachstruktur beweisbar?** Exakte Symmetrieprojektoren und die relevanten Multiplizitätsränge sind konstruiert. Die vollständige Spektralzertifizierung und der mikroskopische Rest fehlen. Die neue rationale Ausschlussschwelle reduziert den benötigten numerischen Präzisionsaufwand erheblich.

**Bleibt das Labor unter Fehlern und bei wachsender Größe brauchbar?** Ja, unter dem angegebenen lokalen Kontroll und Kopplungsvertrag existieren die Bounds (11) bis (15). Sie unterscheiden lokale und globale Fehler. Eine native Clock und Reservoirbilanz sowie die Präparation eines beliebigen wechselwirkenden Grundzustands sind nicht dadurch bewiesen.

**Entsteht eine einzige gemeinsame Welt?** Die benötigte gemeinsame native skalierende Familie ist nicht konstruiert. Der neue allgemeine Gapsatz entscheidet jedoch, dass eine vollständig gegappte Laborphase nicht zugleich der gesuchte masselose physische Sektor sein kann.

**Treffen dieselben Parameter mehrere Beobachtungen?** Die einfache unveränderte Inflationsbranche besteht den zentralen gemeinsamen Amplituden und Tilttest nicht durch bloße Wahl von N. Der neue Gegenversuch zeigt zusätzlich die große Auswirkung einer erzwungenen c3 Änderung auf die wörtliche Alpha Gleichung. Ein vollständiger korrigierter gemeinsamer empirischer Transfer liegt nicht vor.

### 14.2 Vollständige Tore

| Tor | Konkreter Beitrag dieser Runde | Verbleibende entscheidende Beweispflicht |
|---|---|---|
| T1 | Ladungsbasiertes Architekturkriterium, Stabilizergrenze, expliziter endlicher Controller | Primitive Auswahl einschließlich P1/P2, Ortslesart, Ladungen und Kontrollen |
| T2 | Energie und Adjunktenkontrolle des richtigen Gewicht eins Referenzfelds | Nativer Halbladungstransport samt markiertem Skalierungslimes |
| T3 | Präzisierung einer gemeinsamen skalierten Operatorfamilie und ihrer Kegelprüfung | Eine tatsächlich ausgewählte 3+1D Familie |
| T4 | Trennung von Anomaliefreiheit, Familienzahl, Nullmoden und vollständigem Maß | Gemeinsames chirales Maß, richtige Ladungen und Spiegelentkopplung |
| T5 | Rationale 0,72 Δ Bandschranke, neue F4 Bounds, exakte 80/42 Reduktion, gekoppelte lokale Robustheit | Spektralzertifikate, kanonischer Rest und wechselwirkender Kontinuumslimes |
| T6 | Gemeinsamer Invariantentest, Alpha Sensitivität und Mischungsobstruktion | Gemeinsame Wirkung, alle Kopplungen, vollständige Flavour und Neutrinostruktur |
| T7 | Allgemeiner spektraler Ausschluss masseloser Pole bei festem vollständigem Gap | Tatsächlicher masseloser Spin zwei Sektor samt Constraints und Universalität |
| T8 | Optimaler einfacher Reset, vollständige Rohwahrscheinlichkeiten, endliche autonome Ausführung und Fehlerbudgets | Aus derselben Quelle ausgewähltes physikalisches Zustandsfunktional und Entropieabfluss |

Die logisch nächste Zertifizierung ist nicht eine weitere Dezimalstelle des alten großen Singulettlaufs. Sie besteht aus den expliziten reduzierten Operatoren in (26), zertifizierter Einfachheit und Anordnung ihrer relevanten Eigenwerte, den übrigen Symmetrietypen sowie einer sektorübergreifenden nackten Untergrenze von mindestens 11,6. Danach bleibt die volle mikroskopische Restkontrolle separat erforderlich.

Für den Ursprung ist der entscheidende Nachweis ein tatsächlicher primitiver Adapter für den erklärten nicht Clifford Zugriff, der auch Kantenadresse, Ladung, Adjunktion, Clock und Reservoirzugriff erhält. Dieser Nachweis ist nicht durch einen noch ausführlicheren Referenzvertrag ersetzbar.

## 15. Reproduktion und Auslieferung

Vorausgesetzt sind Python mit NumPy, SciPy, SymPy und mpmath. Die beiden exakten Suchprogramme benötigen nur die Python Standardbibliothek. Ein üblicher Lauf lautet:

```bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
python stabilizer_search.py > stabilizer_search_results.json
python symmetry_dimensions.py > symmetry_dimensions_results.json
python verify_followups.py > verification_results.json
python -OO verify_followups.py > verification_results_optimized.json
cmp verification_results.json verification_results_optimized.json
```

Alle Akzeptanzbedingungen benutzen explizite Fehlerauslösung, keine wegoptimierbaren Assertions. Die gespeicherten Ausgaben wurden wie angegeben erzeugt. Die zusätzliche Ausführung der zwei exakten Programme mit `-OO` lieferte ebenfalls bytegleiche Ausgaben. Die QASM Datei ist die aus den geprüften Gattern exportierte Eingangsfolge; sie wurde nicht zusätzlich durch einen externen QASM Simulator geparst.

Die numerischen Fehler beziehen sich jeweils auf den deklarierten Test. Die 544D Matrixkontrolle ist keine Intervallrechnung; die 65536D Zweizellenprobe ist kein N Zellen Produktionslauf. Der gekoppelte Größenbound ist ein ausgeschriebener analytischer Satz, der durch eine Zweizellenprobe und die skalare Fehlerhülle kontrolliert wurde. Die neuen kleinen Spektralprojektoren wurden über exakte Charaktere bestimmt, ihre Energiematrizen noch nicht ausgewertet.

## Primärreferenzen und Herkunft

**Dokumentbasis:** Die vier Dateien `TFPT_Followups_2026-09-14_v1.4.md`, `TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md`, `TFPT_Universalraum_Update_2026-09-14_v1.4.pdf` und `TFPT_Universalraum_Hauptdokument_2026-09-14_v1.4.pdf`. Quellgleichungen insbesondere Hauptdokument Kapitel 23 bis 27 sowie Kapitel 10, 14 und 16. Ihre SHA256 Werte stehen im Manifest.

**Repository Abgleich:** `sthamann/tfpt`, Commit `66b91e40e245569f06ab440ead80f446c9be0ee5`, Datei `experiments/theory-contracts/RESEARCH_2026-09-09.md`. Gelesener Quellenstand, kein erneuter vollständiger Repositorylauf.

[P1] J. Dehaene, B. De Moor: *The Clifford group, stabilizer states, and linear and quadratic operations over GF(2).* Physical Review A 68, 042318 (2003), arXiv:quant-ph/0304125. Verwendet für die affine Träger und Phasennormalform, nicht als Quelle des hier berechneten Ω Optimums.

[P2] A. M. Vershik, A. Yu. Okounkov: *A New Approach to the Representation Theory of the Symmetric Groups. 2.* arXiv:math/0503040v3 (2005). Verwendet für Kästcheninhalte, Verzweigung und Charakterrekursion. Die Clebsch Ränge wurden hier eigenständig exakt berechnet.

[P3] M. Christandl, N. Datta, A. Ekert, A. J. Landahl: *Perfect state transfer in quantum spin networks.* Physical Review Letters 92, 187902 (2004), arXiv:quant-ph/0309131. Methodischer Hintergrund der fest gekoppelten Programmuhr.

[P4] D. Reeb, M. M. Wolf: *An improved Landauer Principle with finite size corrections.* New Journal of Physics 16, 103011 (2014), arXiv:1306.4352. Voraussetzungen und Grenzen thermodynamischer Löschkosten.

[P5] C. Dong, X. Lin: *Unitary vertex operator algebras.* arXiv:1308.2361 (2013). Unitarität der verwendeten affinen und positiven Gitterreferenzen.

[P6] S. Carpi, L. Tomassini: *Energy bounds for vertex operator algebra extensions.* Letters in Mathematical Physics 113, 59 (2023), arXiv:2303.14097v2. Energieabschätzungen unitärer Erweiterungen affiner Vertexoperatoralgebren.

[P7] T. Louis et al.: *The Atacama Cosmology Telescope: DR6 Power Spectra, Likelihoods and ΛCDM Parameters.* arXiv:2503.14452v2, Tabelle 5, Spalte P-ACT-LB2. Hier datierter Branchentest, keine Auswertung der vollständigen gemeinsamen Likelihood.

[P8] Y. Shi: *Both Toffoli and Controlled-NOT need little help to do universal quantum computation.* arXiv:quant-ph/0205115v2 (2002). Verwendet für den universellen Anschluss des expliziten Toffoli Makros, nicht für dessen native TFPT Verfügbarkeit.

[P9] P. W. Shor: *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.* SIAM Journal on Computing 26, 1484 bis 1509 (1997), arXiv:quant-ph/9508027v2. Standardalgorithmus unter einem universellen Quantenrechenvertrag; kein neuer TFPT Faktorisierungsbeweis.

**Schluss:** Der endliche Laborzweig ist jetzt leistungsfähiger, seine Clifford Ressourcengrenze ist exakt bestimmt, und mehrere Spektral und Skalierungsfragen sind auf schärfere Sätze reduziert. Die vollständige gemeinsame Herkunft von Raumzeit, chiraler Materie, Parametern und Gravitation ist durch diese Fortsetzung nicht bewiesen. Der Fortschritt besteht in den oben angegebenen konkreten Konstruktionen und den enger gefassten, noch fehlenden Nachweisen.
