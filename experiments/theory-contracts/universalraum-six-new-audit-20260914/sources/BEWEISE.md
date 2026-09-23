# TFPT und Universalraum: exakte endliche Fortsetzung

**14. September 2026. Ausgangspunkt: die vier bereitgestellten Dokumente v1.4.**

## Ergebnis und Reichweite

Diese Fortsetzung enthält ausgeschriebene Beweise, eine explizite Quantenschaltung und einen tatsächlich ausgeführten unabhängigen Prüfer. Sie schließt nicht die acht physikalischen Tore T1 bis T8. Insbesondere wird keine native Auswahl eines vollständigen 3+1 dimensionalen mikroskopischen Ursprungs behauptet.

Neu gegenüber den bereitgestellten v1.4 Texten sind:

1. Der exakte optimale Überlapp eines beliebigen Achtqubit Stabilizerzustands mit dem Vierträgerzustand Ω beträgt 3/8. Ein expliziter Eingang erreicht diese Grenze.
2. Beim unveränderten mikroskopischen Filter folgt daraus eine um den Faktor 9/4 höhere Rohwahrscheinlichkeit als mit dem bisherigen Zweisingulett. Die Herstellung des neuen Eingangs verlangt ausdrücklich die angegebene trägerübergreifende Clifford Schaltung.
3. Für den festgelegten Feedbackoperator wird die optimale Einzykluskontraktion bezüglich dieses Stabilizer Eingangs bestimmt. Bereits der in v1.4 vorhandene Zweisingulett Reset verbessert die konservative Fehlerverstärkung um Faktor vier; der optimale Stabilizer Reset verbessert sie um Faktor neun.
4. Für tatsächlich gekoppelte Zellen wird eine größenuniforme Schranke des mittleren lokalen Ω Fehlers bewiesen. Dies betrifft ein getriebenes Austauschmodell mit Rücksetzung, nicht die Präparation seines wechselwirkenden Grundzustands.
5. Das physikalische lokale Sternspektrum liegt bei 0 bis 8 statt der universellen 0 bis 10 Einschließung. Daraus folgen stärkere Operatorabschätzungen und im Matchingsektor eine äußere Bandtrennung von mindestens 19Δ/25.

Die Beweise benutzen die jeweils ausdrücklich angegebenen Modellannahmen. Eine korrekte Folgerung innerhalb eines deklarierten Modells ist keine zusätzliche Hypothese; die Herleitung dieses Modells aus der nativen TFPT Quelle ist aber eine andere Aufgabe. Historische Neuheit gegenüber der gesamten Literatur wird nicht behauptet.

## 1. Quellen und Notation

[Q1] `TFPT_Followups_2026-09-14_v1.4.md`: sechs nächste Entscheidungen.

[Q2] `TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md`: insbesondere Abschnitte 3 bis 8 und die T1 bis T8 Tabelle in Abschnitt 9.

[Q3] `TFPT_Universalraum_Hauptdokument_2026-09-14_v1.4.pdf`: Kapitel 6, 10, 23 sowie 25 bis 27. Physische PDF Seiten und gedruckte Seitenzahlen unterscheiden sich um neun.

[Q4] `TFPT_Universalraum_Update_2026-09-14_v1.4.pdf`: Zusammenfassung der v1.4 Änderungen.

Zusätzlich wurden im verbundenen Repository `sthamann/tfpt` die README und `experiments/theory-contracts/RESEARCH_2026-09-09.md` gelesen. Die zweite Quelle berichtet einen nativen ganzzahlig geladenen CAR Grenzwert einschließlich Adjungierten und Energiekontrolle, aber weiterhin keine vollständige native Halbladung und keinen gemeinsamen Abschluss aller Tore. Ihr Inhalt ist nicht mit den späteren v1.4 Rechnungen gleichzusetzen. Der im Hauptbuch genannte Pfad `experiments/theory-contracts/universalraum-paired-release-20260914` lieferte beim geprüften GitHub Zugriff 404. Der neue Prüfer importiert daher keinen behaupteten v1.4 Großlauf.

Vier Ququarts besitzen den Raum H = (C⁴)^⊗4 mit Dimension 256. Die Standardkodierung verwendet zwei Qubits je Träger und die Farbwerte 0,1,2,3 als Zweibitwörter. XOR bedeutet bitweise Addition modulo zwei. Es gelten

\[
|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
|\pi(0),\pi(1),\pi(2),\pi(3)\rangle,
\quad P=|\Omega\rangle\langle\Omega|.
\]

Sij vertauscht die beiden vollständigen Ququarts. P±ij = (I ± Sij)/2. Die Ausgangsdefinitionen sind [Q2,Q3] entnommen. Die folgenden Optimierungen und Abschätzungen wurden hier daraus entwickelt.

## 2. Optimaler Stabilizer Eingang: vollständiger Beweis

### Satz 1

In der festgelegten Achtqubit Kodierung gilt

\[
\max_{|s\rangle\ \mathrm{Stabilizer}} |\langle\Omega|s\rangle|^2=\frac38.
\]

Dies gilt ebenfalls für das Maximum über konvexe Mischungen von Stabilizerzuständen. Das Maximum ist innerhalb dieser Ressource exakt, nicht nur das beste Resultat einer zufälligen Suche.

### 2.1 Reduktion auf vier logische Qubits

Ω wird von vier unabhängigen kommutierenden Paulioperatoren mit Eigenwert +1 stabilisiert: X auf jeweils demselben internen Bit aller vier Träger sowie Z auf jeweils demselben internen Bit aller vier Träger. Das globale XOR eines nichttrivialen Farbwerts wirkt auf vier Farben als gerade Permutation. Die entsprechenden globalen Z Phasen sind ebenfalls +1, weil in einer Permutation jeder Bitwert zweimal eins ist.

Der gemeinsame Codespace hat Dimension 2^(8−4)=16. Eine Clifford Kodierungsisometrie ist

\[
\mathcal V|b,c\rangle=\frac12\sum_{a=0}^3
|a,a\oplus b,a\oplus c,a\oplus b\oplus c\rangle.
\]

Die sechzehn Vektoren sind orthonormal. Sie erfüllen die zwei XOR Paritätsbedingungen und die zwei Translationsbedingungen. Damit spannen sie genau den Codespace auf.

Durch direkte Auswertung des antisymmetrischen Tensors erhält man

\[
\mathcal V^\dagger|\Omega\rangle=
\frac{|1,2\rangle-|1,3\rangle-|2,1\rangle+|2,3\rangle+|3,1\rangle-|3,2\rangle}{\sqrt6}.
\]

In vier logischen Binärkoordinaten hat dieser Vektor den Träger

\[
S=\{6,7,9,11,13,14\}\subset\mathbb F_2^4.
\]

Für einen beliebigen physischen Stabilizerzustand s projiziere auf die vier gemeinsamen Pauli Bedingungen. Der erfolgreiche normalisierte Ausgang ist wiederum ein Stabilizerzustand, sofern er nicht null ist. Da Ω im Codespace liegt, gilt

\[
|\langle\Omega|s\rangle|^2=p\,|\langle\Omega|s'\rangle|^2
\le |\langle\Omega|s'\rangle|^2,
\]

wobei p die Projektionswahrscheinlichkeit ist. Eine Clifford Dekodierung reduziert s′ auf einen vierqubitigen logischen Stabilizerzustand mit festen Hilfsqubits. Es genügt daher, alle logischen Stabilizerzustände zu begrenzen.

### 2.2 Affine Träger liefern die globale Obergrenze

Ein reiner Stabilizerzustand besitzt in der Rechenbasis einen affinen Träger A von Größe 2^k und Amplituden vom gleichen Betrag 2^(−k/2). Ihre Phasen werden durch binäre lineare und quadratische Formen beschrieben. Diese Standardbeschreibung wird in Dehaene und De Moor [R1] hergeleitet.

Die Dreiecksungleichung liefert unabhängig von allen Phasen

\[
|\langle s|\mathcal V^\dagger\Omega\rangle|^2
\le\frac{|A\cap S|^2}{6\,2^k}.
\]

Die größtmöglichen Schnittgrößen für k = 0,1,2,3,4 sind 1,2,3,4,6.

Der einzige nichttriviale geometrische Teil ist kurz beweisbar. Das XOR aller sechs Punkte von S ist null. Eine affine Zweierdimension hat vier Punkte, deren XOR null ist. Läge eine solche Ebene ganz in S, hätten auch die beiden übrigen verschiedenen Punkte XOR null, was unmöglich ist. Also liegt die Schnittgröße höchstens bei drei. Für eine affine Hyperebene mit nichttrivialer linearer Bedingung ist die Schnittgröße mit S gerade. Alle sechs Punkte passen nicht hinein, denn S hat volle affine Dimension vier. Deshalb liegt ihre Schnittgröße höchstens bei vier. Die übrigen Schranken sind unmittelbar.

Folglich sind die möglichen Obergrenzen

\[
\frac16,\quad\frac13,\quad\frac38,\quad\frac13,\quad\frac38.
\]

Der Prüfer enumeriert zusätzlich alle 307 affinen Unterräume von F₂⁴: 16 Punkte, 120 Geraden, 140 Ebenen, 30 Hyperebenen und den Gesamtraum. Die Enumeration bestätigt genau diese Extremwerte. Der ausgeschriebene Beweis benötigt keine numerische Optimierung.

### 2.3 Ein Eingang erreicht die Grenze

Der logische Stabilizerzustand

\[
|s_*\rangle=\frac{|6\rangle-|7\rangle-|9\rangle+|8\rangle}{2}
\]

hat einen affinen Viererträger und zulässige lineare Phasen. Mit σ = V s* erhält man

\[
|\langle\Omega|\sigma\rangle|^2=\frac38.
\]

Explizit:

\[
|\sigma\rangle=\frac14\sum_{a=0}^3
\bigl(
|a,a\oplus1,a\oplus2,a\oplus3\rangle
-|a,a\oplus1,a\oplus3,a\oplus2\rangle
-|a,a\oplus2,a\oplus1,a\oplus3\rangle
+|a,a\oplus2,a,a\oplus2\rangle
\bigr).
\]

Es gibt sechzehn verschiedene Basiswörter mit Betrag 1/4. Zwölf davon treffen den Ω Träger mit dem richtigen Vorzeichen. Daher ist das Überlappquadrat 12²/(16·24)=3/8. Der letzte Summand enthält wiederholte Farben und liegt außerhalb des Ω Trägers. Es wurde also kein fertiges Ω versteckt eingesetzt.

`omega_seed.qasm` enthält die vollständige Schaltung ab |00000000⟩: vier Hadamards, dreizehn CNOT, zwei X und zwei Z. Der Prüfer liest genau diese exportierte Datei und verifiziert alle 256 Amplituden mit ganzen Zahlen und explizit mitgeführter Normierung. Die Anzahl ist eine konkrete Kostenangabe, keine Behauptung global minimaler Gatterzahl. Routing, Pulsfehler und Fehlerkorrektur sind nicht enthalten.

### 2.4 Welche zusätzliche Ressource die Verbesserung benötigt

Die optimale Aussage erlaubt Clifford Gatter über die gesamten acht Qubits. Ihre native Verfügbarkeit folgt nicht aus einer lokalen Pauli Tabelle. Insbesondere entstehen Korrelationen zwischen den zwei bisherigen Singulettpaaren.

Diese Einschränkung ist notwendig: Über den Schnitt 12|34 hat Ω sechs gleiche Schmidtkoeffizienten 1/√6. Deshalb kann kein Produktzustand über diesen Schnitt mehr als 1/6 Überlappquadrat erreichen. Dasselbe gilt für separable Mischungen. Der bisherige Zweisingulettzustand χ erreicht diese kleinere Grenze bereits optimal. Die neue Verbesserung ist folglich kein besser gewählter ungekoppelter Paarzustand, sondern nutzt trägerübergreifende Clifford Verschränkung.

## 3. Unveränderter mikroskopischer Filter: neue vollständige Rohstatistik

[Q2, Abschnitte 6 und 7] liefert im deklarierten kontrollierten Sternmodell den akzeptierten Krausoperator

\[
K_{\rm acc}=P_{\rm bare}P_{0,\rm dressed}P_{\rm bare}=wP,
\qquad w=\frac12\left(1+\frac\Delta{\sqrt{\Delta^2+24t^2}}\right).
\]

Für einen normierten nackten Eingang mit a = ⟨P⟩ folgt daher exakt

\[
p_{\rm prep}=aw^2.
\]

Nach erfolgreicher Präparation ist das System genau Ω. Derselbe Dreierzyklus und dieselben Recordoperationen wie in v1.4 liefern für Start und Schluss gemeinsam

\[
p_{\rm behalten}=aw^4,\qquad
p_{\rm frisch}=\frac{17}{32}aw^4.
\]

Damit gilt für den neuen Eingang a = 3/8:

\[
p_{\rm prep}=\frac{3w^2}{8},\quad
p_{\rm behalten}=\frac{3w^4}{8},\quad
p_{\rm frisch}=\frac{51w^4}{256}.
\]

Bei t/Δ=1/20 ergeben sich:

| Größe | Bisheriger Zweisingulett Eingang | Optimaler Stabilizer Eingang |
|---|---:|---:|
| Überlappquadrat a | 1/6 | 3/8 |
| Präparation | 0,161915331297 | 0,364309495418 |
| Gesamterfolg mit behaltenem Record | 0,157299447054 | 0,353923755872 |
| Gesamterfolg mit frischem Record | 0,083565331248 | 0,188021995307 |
| Mittlere Zahl von Präparationsversuchen | 6,176067405040 | 2,744918846684 |

Alle drei Rohwahrscheinlichkeiten wachsen exakt um 9/4. Die Fehlzweige bleiben erhalten; beispielsweise ist 1−3w²/8 die Präparationsfehlrate. Der Quotient frisch/behalten bleibt 17/32.

Es handelt sich um die optimale Ausbeute dieses festgehaltenen Filters über Stabilizer Eingänge. Es ist keine globale Optimalität über Amplitudenverstärkung, andere Instrumente oder beliebige nichtklassische Ressourcen. Die 13 kontrollierten Entwicklungen pro Filter und ihre Zeitkosten aus v1.4 werden nicht entfernt. Auch der physikalische Aufwand zur Herstellung von σ muss mitgeführt werden.

## 4. Feedback mit beliebigem Reset: exakte und optimale Kontraktion

Setze wie in v1.4

\[
K=P^-_{03}P^-_{02}P^-_{01},\qquad
\beta=\frac{9+\sqrt{17}}{32}.
\]

Es gelten KΩ=K†Ω=Ω und K†K ≤ P + β(I−P). Für einen festen Reset σ mit a=Tr(Pσ)>0 definiere

\[
\mathcal E_\sigma(\rho)=K\rho K^\dagger+
\operatorname{Tr}[(I-K^\dagger K)\rho]\,\sigma.
\]

### Satz 2

Der Kanal ist vollständig positiv und spurerhaltend. Ω ist sein einziger stationärer Zustand. Für die Infidelität e(ρ)=1−Tr(Pρ) gilt

\[
e(\mathcal E_\sigma\rho)\le r(a)e(\rho),\qquad
r(a)=1-a(1-\beta).
\]

Die Konstante r(a) ist als Einzykluskonstante für alle Eingänge scharf.

### Beweis

Der erste Summand ist vollständig positiv. Der zweite ist ein positives Messereignis gefolgt von der Präparation des normierten Zustands σ. Die beiden Effekte summieren sich zu I, also ist der Kanal spurerhaltend.

K†PK=P ergibt exakt

\[
F(\mathcal E_\sigma\rho)=F(\rho)+a\operatorname{Tr}[(I-K^\dagger K)\rho].
\]

Aus I−K†K ≥ (1−β)(I−P) folgt die Kontraktion. Weil r(a)<1, geht die Infidelität gegen null; jeder stationäre Dichteoperator hat F=1 und ist deshalb P. Ein Eigenvektor von K†K zum Eigenwert β liegt orthogonal zu Ω und erreicht die Einzyklusgrenze.

Der Prüfer konstruiert K in der treuen regulären S₄ Darstellung und kontrolliert rational

\[
\det(xI-K^\dagger K)=
\frac{x^{12}(x-1)(16x-1)^5(16x^2-9x+1)^3}{2^{32}}.
\]

Sämtliche S₄ Darstellungen kommen im physischen Vierququart Raum vor. Das spektrale Maximum im Ω Komplement und die Existenz des β Eigenwerts sind dadurch kontrolliert. Die analytischen Operatoraussagen gelten auf allen 256 Dimensionen, nicht nur in einem durch den späteren Tick erhaltenen Farbenraum.

### Konkrete Verbesserung

| Reset | a | r(a) | 1/(1−r) | Zyklen für 10⁻⁶, eine Zelle | Zyklen für 10⁻⁶, 4096 unabhängige Zellen |
|---|---:|---:|---:|---:|---:|
| Basiszustand | 1/24 | 0,975420710450 | 40,684658438426 | 556 | 890 |
| Vorhandener Zweisingulett χ | 1/6 | 0,901682841800 | 10,171164609607 | 134 | 214 |
| Optimaler Stabilizer σ | 3/8 | 0,778786394050 | 4,520517604270 | 56 | 89 |

Für σ lautet die exakte Rate

\[
r_* = \frac{187+3\sqrt{17}}{256}.
\]

Schon χ braucht keinen neuen Zielzustand jenseits des in v1.4 vorhandenen Präparationsvertrags. Für σ kommt die oben ausgewiesene Schaltung hinzu. Satz 1 und die Schärfe von r(a) beweisen, dass σ die beste solche Einzykluskontraktion unter Stabilizer Resets liefert. Das ist nicht die Optimalität der gesamten mehrzyklischen Strategie mit veränderlichem K.

Die ganzen Zykluszahlen wurden nicht nur mit Gleitkommalogarithmen ermittelt. Der Prüfer schließt √17 durch rationale Zahlen mit Nenner 10⁴⁰ ein und prüft N r_upper^m ≤ 10⁻⁶ sowie N r_lower^(m−1)>10⁻⁶. Es sind die kleinsten Zyklen für diese konkrete Worst Case Schranke, nicht die exakte Mischzeit jedes Eingangszustands.

### Fehler pro Zyklus

Bei höchstens ε Abweichung vom idealen Kanal in halber Diamantnorm gilt

\[
e_m\le r^m e_0+\varepsilon\frac{1-r^m}{1-r}.
\]

Beweis: Eine Effektwahrscheinlichkeit kann sich durch diese Kanalabweichung höchstens um ε ändern. Iteration von e_(m+1)≤r e_m+ε ergibt die Formel. Damit verbessert χ den konservativen Verstärkungsfaktor um exakt vier, σ um exakt neun gegenüber dem Basisreset.

Dies ist bei gleichem Gesamtfehler ε pro Zyklus zu verstehen. Die zusätzliche Schaltung kann ε, Dauer und Entropiebudget verändern. Ein neunmal kleinerer mathematischer Verstärkungsfaktor ist keine automatisch neunmal bessere Hardware.

## 5. Tatsächlich wechselwirkende Zellen: ein uniformer Belastungssatz

Die unabhängige Mehrzellenschranke aus v1.4 kontrolliert keinen wechselwirkenden Grundzustand. Für ein ausdrücklich festgehaltenes getriebenes Austauschmodell lässt sich aber bereits ein nichttrivialer Satz beweisen.

Es gebe N Zellen mit lokalen Projektoren P_i auf Ω und Q_i=I−P_i. Setze

\[
D=\sum_iQ_i,\qquad q(\rho)=\operatorname{Tr}(D\rho)/N.
\]

q ist die mittlere lokale Infidelität. Die Zellen dürfen anfangs beliebig verschränkt sein. Ein Zyklus besteht aus lokalen Feedbackkanälen und anschließender gekoppelter Entwicklung für eine Zeit τ unter

\[
H=\sum_i H_i+\sum_{e=(i,j)}\lambda_e V_e,
\]

wobei [H_i,P_i]=0, 0≤λ_e≤λ und V_e der Brückenprojektor P⁺ auf einem Paar von Materieträgern der benachbarten Zellen ist. Der Zellgraph habe maximalen Grad z. Dieses ist das nackte Austauschmodell; der volle ungefilterte Vermittlerraum wird nicht stillschweigend damit identifiziert.

### Satz 3

Wenn die implementierten lokalen Feedbackkanäle jeweils höchstens ε Fehler in halber Diamantnorm besitzen und ihr gemeinsamer Schritt das Tensorprodukt dieser lokalen Kanäle ist, gilt

\[
q_m\le r^m q_0+
\left(\varepsilon+\frac{z\lambda|\tau|}{2\hbar}\right)
\frac{1-r^m}{1-r}.
\]

### Beweis

Die lokale Kontraktion ist äquivalent zu E_i*(Q_i)≤rQ_i. Deshalb gilt auch auf beliebig verschränkten Eingängen E_N*(D)≤rD. Die lokalen Kanalfehler ändern den Mittelwert höchstens um ε.

Für eine Kante trägt nur Q_i+Q_j zum Kommutator bei. Da V_e ein Projektor ist, gilt ||V_e−I/2||=1/2. Da Q_i und Q_j kommutieren und Projektoren sind, gilt ||Q_i+Q_j−I||≤1. Also

\[
\|[V_e,Q_i+Q_j]\|\le 2\cdot\frac12\cdot1=1.
\]

Daraus folgen ||[H,D]||≤Σ_e λ_e≤Nzλ/2 und durch Integration der Heisenberggleichung

\[
|q(U\rho U^\dagger)-q(\rho)|\le\frac{z\lambda|\tau|}{2\hbar}.
\]

Zusammen ergibt das die skalare Rekursion, deren geometrische Summe den Satz beweist.

### Was damit tatsächlich geschlossen ist

Die Abschätzung gilt bei echter Wechselwirkung, beliebiger Zellzahl und anfänglicher Verschränkung. Die Koeffizienten hängen nicht von N ab. Ein Zeitfehler |δτ| kann konservativ durch Ersetzen von |τ| durch |τ|+|δτ| berücksichtigt werden. Andere Pulsfehler müssen in ε oder in einem zusätzlichen Kommutatorbudget erscheinen.

Nicht bewiesen ist damit globale reine Produktfidelität bei festem nichtverschwindendem Fehlerboden: Dafür liefert der Vereinigungsbound nur 1−F_global ≤ N q. Ebenso ist der Zielzustand das lokale Ω Muster und nicht der verschränkte Grundzustand von H. Der Satz beweist weder einen thermodynamischen Gap noch eine Feldtheorie oder eine natürliche Umgebung.

## 6. Das lokale Sternspektrum ist schärfer als die universelle Einschließung

Im kantenlokalen Clebschmodell definiert [Q2]

\[
A_v=\sum_{e\ni v}(I-S_e),\qquad A=\sum_e(I-S_e),\qquad
F_4=\sum_v A_v(A_v-I).
\]

Jeder Stern besitzt fünf Nachbarn und wirkt auf sechs physische Ququarts. Nach Umnummerierung ist A_v = 5I−J₆ mit dem Jucys Murphy Element J₆=Σ_{i=1}^5(i,6). Seine Eigenwerte sind die Inhalte der jeweils letzten Tableau Box [R2]. In (C⁴)^⊗6 kommen nur Youngformen mit höchstens vier Zeilen vor. Der Inhalt liegt daher zwischen −3 und 5. Folglich gilt

\[
\operatorname{spec}(A_v)\subseteq\{0,1,2,3,4,5,6,7,8\}.
\]

Die genauen Multiplizitäten sind:

| a | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplizität | 84 | 560 | 1050 | 360 | 250 | 912 | 190 | 600 | 90 |

Sie summieren sich zu 4096. Die Einschränkung auf vier lokale Farben ist wesentlich. Die universelle reguläre S₆ Darstellung enthält weitere Spektralanteile.

### Ein unabhängiges ganzzahliges Zertifikat

Setze p(x)=∏_(k=0)^8(x−k). Der Prüfer expandiert p(5I−Σ_(j=1)^5(0,j)) exakt in der Gruppenalgebra von S₆ und benutzt

\[
\operatorname{Tr}_{(\mathbb C^d)^{\otimes6}}\rho(\pi)=d^{c(\pi)}.
\]

Die vollständige ganzzahlige Rechnung ergibt

\[
\operatorname{Tr}(p(A)^\dagger p(A))
=21946982400\,d(d-4)^2(d-3)(d-2)(d-1).
\]

Bei d=4 ist diese Spur null. Da p(A)†p(A) positiv ist, folgt p(A)=0. Das ist eine exakte physische Polynomidentität ohne Gleitkommaeigenwerte. Bei d=5 ist die Spur positiv; die entsprechende Negativkontrolle verhindert eine unzulässige Übertragung auf beliebige Dimension.

### Satz 4: neue Operatorgrenzen

Für a=0,…,8 gilt 0≤a(a−1)≤7a≤56. Mit Σ_v A_v=2A und A=80I−2H₀ erhält man

\[
0\le F_4\le14A=1120I-28H_0\le896I,
\qquad H_0\ge8I.
\]

Ferner gilt für jede ganze Zahl k=0,…,7 die punktweise Ungleichung (a−k)(a−k−1)≥0. Somit

\[
F_4\ge 4kA-16k(k+1)I.
\]

Für k=7 wird daraus

\[
F_4\ge1344I-56H_0.
\]

Bei ε=t/Δ=1/20 lautet der trunkierte Operator in J Einheiten H_tr=H₀+F₄/800. Daher

\[
H_{\rm tr}\ge\frac{93}{100}H_0+\frac{42}{25}I.
\]

Diese Gerade ist im relevanten Bereich 8<h<12 stärker als die zuvor verwendete quadratische Untergrenze; sie wird nicht als auf jedem Spektralbereich stärker ausgegeben. Mehrere solche Operatoruntergrenzen dürfen ohne weiteren Beweis auch nicht durch ein punktweises Operatormaximum ersetzt werden.

### Keine fälschliche Vierfachzertifizierung

Wäre das nackte Nichtsingulettminimum rigoros mindestens 579/50=11,58, ergäbe sich rigoros die korrigierte Untergrenze

\[
\frac{93}{100}\frac{579}{50}+\frac{42}{25}
=\frac{62247}{5000}=12,4494.
\]

Sie liegt über der in v1.4 berichteten variationalen Viererenergie 12,447023775951228. Der nackte Bound 11,58 und eine rigorose obere Viererenergie wurden hier jedoch nicht zertifiziert. Dieser Zahlenvergleich ist eine konditionale Konsequenz des neuen Operatorsatzes, nicht der fehlende Sektorausschluss.

Auch eine Inertiadifferenz vier über ein Intervall würde nur vier Eigenwerte in diesem Intervall beweisen. Vier verschiedene, sehr eng liegende Eigenwerte erfüllen dieselbe Aussage. Exakte Entartung verlangt zusätzlich einen exakten Symmetriebeweis oder einen anderen Gleichheitsnachweis. Meine vorige Antwort hatte diese Unterscheidung zu schwach behandelt.

## 7. Stärkere äußere Bandtrennung im erreichbaren Matchingsektor

Hier wird ausschließlich die kantenlokale Architektur ohne Vermittlerhopping mit erhaltener Ladung

\[
Q_v=n_f(v)+\sum_{e\ni v}n_e=1
\]

betrachtet. Die Bosonen bilden Matchings; eine besetzte Kante trägt genau einen Vermittlerzustand. Das ist derselbe erreichbare Sektor, auf dem v1.4 den allordentlichen CAR zu Tensor Adapter beweist.

Für ein Matching M mit n Bosonen seien S die 16−2n verbleibenden Materieplätze. Der Schritt A_n in den nächsten Bosonensektor addiert eine neue freie Kante. In einem Zielmatching M′ gibt es höchstens n+1 Vorgänger. Cauchy Schwarz liefert

\[
\|A_n\psi\|^2\le(n+1)\sum_M\left\langle\psi_M,
\sum_{e\subset S}(I-S_e)\psi_M\right\rangle.
\]

Für einen Stern mit Grad d_v auf vier lokalen Farben gilt A_v≤[d_v+min(3,d_v)]I. Summation liefert für den induzierten Materiegraphen

\[
\left\|\sum_{e\subset S}(I-S_e)\right\|
\le |E(S)|+\frac12\sum_{v\in S}\min(3,d_v).
\]

Die vollständige Enumeration aller 65536 Ortsmengen bestätigt damit

\[
a_n^2=(64,104,126,128,120,84,56,16).
\]

Die früheren kantenlokalen Grenzen waren (80,124,144,136,120,84,56,16). Die Verbesserung verwendet die physische Vierfarbenstruktur und den Matchingvertrag, nicht bloß einen günstigeren numerischen Eigenwert.

Der Vergleichsoperator auf Bosonenzahlen 1 bis 8 hat Diagonale 1,…,8 und Nebendiagonale −ε a₁,…,−ε a₇. Bei ε=1/20 sind sämtliche LDL Pivots nach Subtraktion von 19/25 positiv:

\[
\frac6{25},\frac{47}{300},\frac{539}{2350},\frac{24859}{13475},
\frac{5067983}{1242950},\frac{1314760571}{253399150},
\frac{204215752051}{32869014275},\frac{36930182106956}{5105393801275}.
\]

Folglich gilt im benannten Sektor QHQ≥19ΔQ/25. Wegen PHP=0 und dim(P)=4¹⁶ liefert Minmax genau ein niedriges Band dieser Dimension mit nichtpositiven Eigenwerten und alle weiteren Eigenwerte mindestens 0,76Δ. Der negative Kontrollwert 0,77Δ scheitert am Vergleichstest. Für kleinere |ε| bleiben dieselben rationalen Grenzen gültig, wie die positive Pivotrekursion beziehungsweise der tridiagonale Vergleich zeigt.

Die neue Schranke gilt nicht automatisch für andere Ladungssektoren mit mehrfach besetzten Vermittlern. Die alte breiter gefasste 0,7Δ Aussage wird daher nicht stillschweigend ersetzt.

Setzt man die neuen Normen in dieselbe energieabhängige Feshbach Restabschätzung von v1.4 ein, erhält man für e≤0 am Betriebspunkt

\[
\frac{\|R_{\rm kernel}\|}{J}
\le\frac{571104807416}{608986335525}
\approx0,937795766671.
\]

Das ist kleiner als der zuvor angegebene Wert 1,716010622510, aber weiterhin nicht der kanonische Rest nach H₂+H₄ und kein Zertifikat des inneren Gaps. Die Verbesserung ist damit echt und ihre Grenze ebenfalls eindeutig.

## 8. Vollständige Aussagen zu den übrigen behaupteten Abkürzungen

### 8.1 Autonomer Clock: korrekte Konstruktion, aber keine Quellenherleitung

Für bereits vorgegebene unitäre Gatter U₁,…,U_m definiere V₀=I, V_k=U_k⋯U₁ und

\[
H_{\rm prog}=J\sum_{k=0}^{m-1}\sqrt{(k+1)(m-k)}
\left(|k+1\rangle\langle k|\otimes U_{k+1}+\mathrm{h.c.}\right).
\]

Mit T=Σ_k |k⟩⟨k|⊗V_k gilt

\[
T^\dagger H_{\rm prog}T=2J J_x\otimes I
\]

für Spin m/2. Daher folgt bei τ=πℏ/(2J) exakt

\[
e^{-i\tau H_{\rm prog}/\hbar}|0\rangle|\psi\rangle
=(-i)^m|m\rangle U_m\cdots U_1|\psi\rangle.
\]

Dies ist die passende Anwendung der bekannten perfekten Transferkonstruktion [R3]. Eine gleichgewichtete unkontrollierte Clockkette garantiert nicht bereits denselben deterministischen Transfer. Die neue Formel behebt diese mathematische Lücke, indem sie die erforderlichen Gewichte sichtbar macht. Ihr Normbudget ist mJ; begrenzt man die Norm stattdessen größenunabhängig, wächst die Transferzeit entsprechend.

Aber sämtliche U_k, die Kopplungsgewichte und der Clockeingang wurden eingesetzt. Der Satz kompiliert einen gegebenen Ablauf. Er leitet diesen Ablauf nicht aus P1/P2 ab. Auch reine unitäre Speicherung aller Messausgänge entscheidet nicht das Messproblem oder die kosmologische Zustandswahl.

### 8.2 Reset braucht Speicher oder eine Umgebung

Eine unitäre Rücksetzung eines beliebigen d dimensionalen Eingangs hat auf Basisvektoren die Form

\[
U|i\rangle|0\rangle_E=|\sigma\rangle|e_i\rangle_E.
\]

Unitarität erzwingt ⟨e_i|e_j⟩=δ_ij. Deshalb ist dim(E)≥d. Für n beliebige unabhängige Eingaben ist mindestens d^n Dimension nötig, solange keine Information das berücksichtigte Gesamtsystem verlässt. Für d=256 bedeutet dies mindestens acht Speicherqubits pro vollständig beliebiger Rücksetzung. Es ist eine Kapazitätsuntergrenze, keine universelle Wärmezahl. Physische Löschenergie hängt unter anderem von Zustand, Temperatur und zugänglichen Korrelationen ab.

Ein eingebautes Band verschiebt die Information; es erzeugt keinen unbegrenzten Vorrat frischer reiner Speicherzellen aus einem abgeschlossenen endlichen System.

### 8.3 Strikte Kantenfaktorisierung wählt ihren eigenen Zusatzvertrag

Eine Vorgabe unabhängiger Vermittlersysteme auf disjunkten Kanten schließt eine gemeinsam benutzte Bank innerhalb dieser Vorgabe aus. Aus gewöhnlicher Lokalität folgt die Vorgabe nicht: v1.4 enthält ausdrücklich eine lokale Bank pro Zelle als Gegenmodell. Kommutierende Teiloperatoren allein beweisen außerdem keine vollständige Tensorfaktorisierung oder die Anzahl der primitiven Modi.

Deshalb war meine vorherige Darstellung von „strikter kompositionaler Lokalität“ als praktisch gelöster primitiver Auswahl zu stark. Es ist ein zusätzlicher Vertrag, solange seine native Herleitung fehlt.

### 8.4 Halbladung entsteht nicht durch Umbenennen einer Erweiterung

Für Π=(−1)^(2Q) kommutiert jede ausschließlich ganzzahlige Ladungsverschiebung mit Π. Produkte, Summen und beschränkte starke Grenzwerte solcher Operatoren bleiben im Kommutanten von Π. Ein nichtverschwindender Halbladungsoperator antikommutiert mit Π und liegt deshalb nicht in dieser abgeschlossenen geraden Operationsklasse.

Eine ungerade Erweiterung oder ein zusätzlicher Intertwiner kann mathematisch definiert werden. Eine Vertexoperatoralgebra benötigt dabei ihre eigenen Voraussetzungen für Energieabschätzungen und Erweiterung; siehe [R4]. Keiner dieser Existenzsätze liefert von selbst die Identifikation mit dem ursprünglichen geladenen Quellfeld, dessen Normierung, Clock und Cocycle. Für unbeschränkte Grenzoperatoren dürfen die Domänenbedingungen nicht durch das Wort Grenzwert ersetzt werden.

### 8.5 Zwei Bänder wählen nicht die gesamte Raumdimension

Ein generisches Zweibandkreuzen hat Kodimension drei. Das ist eine Aussage unter der Zweibandvoraussetzung, keine Ableitung dieser Voraussetzung aus einem Viererträger.

Ein exaktes Gegenbeispiel gegen den weitergehenden Schluss benutzt vier antikommutierende hermitesche 4×4 Matrizen

\[
\Gamma_1=X\otimes X,\quad\Gamma_2=X\otimes Y,\quad
\Gamma_3=X\otimes Z,\quad\Gamma_4=Z\otimes I.
\]

Für H(k)=Σ_(j=1)^4 k_j Γ_j gilt H(k)²=|k|²I. Es gibt also in vier Impulsrichtungen einen isolierten Nullpunkt innerhalb dieser Cliffordklasse. Das Beispiel behauptet keine allgemeine Stabilität unter beliebigen symmetriebrechenden Störungen; es zeigt, dass die Dimension der physischen Grundstruktur nicht aus einer ungeprüften Zweibandreduktion folgt.

Schon der Clebschgraph allein hat E−V+1=25 unabhängige Zyklen. Sein freier Fundamentalgruppenträger erlaubt reguläre abelsche Überlagerungen mit Deckgruppe Z^d für d=1,…,25 durch Wahl verschiedener surjektiver Homomorphismen. Lokale Inzidenz fixiert diese Verklebung nicht. Das ist ein Nichtauswahlsatz für die Inzidenzdaten, nicht gegen zusätzliche native Auswahlregeln.

### 8.6 Drei Nullmoden, Flavour und Gravitation bleiben verschiedene Aussagen

Im in v1.4 gebauten Flusstest stammt der Index drei vom eingesetzten Fluss drei. Ein flaches Z₄ Linienbündel auf T² hätte L^⊗4 trivial, also 4c₁(L)=0 und wegen Torsionsfreiheit von H²(T²,Z) sogar c₁(L)=0. Eine solche reine diskrete Markierung würde daher nicht den benötigten U(1) Fluss drei erzeugen. Dies ist ein genau abgegrenztes Gegenbeispiel, keine Behauptung, alle möglichen TFPT Bündel seien flach.

Bei identischen orthonormalen linken und rechten inneren Moden und konstantem Skalarprofil folgt Y_ab=yδ_ab. Dieser konkrete Flavourzweig besitzt keine Hierarchie. Bei verschiedenen linken und rechten Moden darf die Aussage nicht pauschal aus bloßer Konstanz gefolgert werden.

Ein frequenzunabhängiger regulärer Tensorprojektor verändert nicht den Träger einer spektralen Dichte. Ist diese unterhalb einer positiven Energieschwelle null, kann die Projektion dort keinen masselosen Pol erzeugen. Ein Term proportional zu R in einer Wirkung für einen bereits vorgegebenen Hintergrund genügt zudem nicht zur Quantisierung eines dynamischen metrischen Freiheitsgrads. Der gemeinsame materielle Grenzwert macht T7 deshalb nicht automatisch zu einem geschlossenen Folgesatz.

## 9. Gemeinsamer Parametervergleich, ohne neue Kalibrierung

Die unveränderte führende Inflationsbranche aus [Q2] lautet

\[
A_s=\frac{N^2c_3^7}{24\pi^2},\qquad
n_s=1-\frac2N,\qquad r=\frac{12}{N^2},\qquad c_3=\frac1{8\pi}.
\]

Elimination von N liefert exakt

\[
A_s(1-n_s)^2=\frac{c_3^7}{6\pi^2},\qquad
r=3(1-n_s)^2.
\]

Die Primärquelle ACT DR6 v2, Tabelle 5, PDF Seite 31, Spalte P-ACT-LB2 wurde visuell geprüft [R5]. Sie gibt ln(10¹⁰ A_s)=3,062 und n_s=0,9752±0,0030 im dortigen Basismodell an. Die Amplitude wurde hier mit hoher Präzision erneut eingesetzt. Es folgen N≈56,62391 und n_s≈0,96467923. Der Abstand entspricht etwa 3,5069 der genannten marginalen Standardunsicherheiten. Kalibrierung am zentralen Tilt liefert stattdessen die 2,02842 fache Amplitude.

Die Wahl von N allein kann diese beiden Zentralwerte in der unveränderten Formel nicht gemeinsam treffen. Diese algebraische Nichtpassung ist bewiesen. Ein statistischer Ausschluss der gesamten TFPT Theorie ist es nicht. Es wurden weder eine gemeinsame Likelihood noch ein Transfer mit Theoriefehlern, Reheating oder Schleifen gerechnet. Eine frei eingeführte Korrektur wird nicht als Lösung ausgegeben.

## 10. Abschlussmatrix: Was vollständig bewiesen wurde und was nicht

| Punkt | Ergebnis dieser Fortsetzung | Verbleibender vollständiger Nachweis |
|---|---|---|
| T1 | Explizite Nichtauswahl der Architektur durch Lokalität; korrekter Compiler für einen bereits gegebenen Ablauf | Native primitive Auswahl statt nachträglich eingesetzter Programme und Zustände |
| T2 | Strenge Paritätsgrenze; Unterscheidung von mathematischer Erweiterung und nativem Intertwiner | Gemeinsame dichte Domäne, beide Adjungierte, Energiekontrolle und native Halbladung samt Clock und Cocycle |
| T3 | Konkrete Gegenbeispiele zur Dimensionsauswahl aus Inzidenz oder ungeprüfter Zweibandreduktion | Eine native skalierende Familie und gemeinsamer Lorentzkegel aller Sektoren |
| T4 | Indexwahl und Flavourauswahl sauber getrennt; diskrete flache Markierung liefert nicht von selbst Fluss drei | Chirales Standardmodellmaß, korrekte Ladungen, Spiegelentkopplung und native Familienzahl |
| T5 | Neue lokale Operatorgrenzen, äußere Matchingbandtrennung, uniformer lokaler Fehlerbound mit echter Austauschkopplung | Exakte Vierfachheit, zertifizierte Nichtsingulettgrenze, kanonischer mikroskopischer Rest und wechselwirkender physikalischer Kontinuumslimes |
| T6 | Unveränderte Inflationsrelation gemeinsam ausgewertet; konkreter konstanter Flavourzweig ohne Hierarchie | Gemeinsamer interner Transfer aller Eichkopplungen, Massen, Mischungen und Neutrinoskala |
| T7 | Projektionsargument erzeugt keinen Pol; autonome Berechenbarkeit ersetzt keine dynamische Geometrie | Masseloser quantisierter Spin zwei, zwei Helizitäten, Constraints und universelle Kopplung aus demselben Ursprung |
| T8 | Optimale Stabilizer Präparation und Resetkontraktion im benannten Kontrollmodell; Speicherbedarf explizit | Physische Herkunft von Umgebung, Anfangszustand und einem gemeinsamen Quellfunktional |

RH, allgemeine Faktorisierung und P versus NP wurden nicht gelöst. Die vollständige signierte Weil Form wurde nicht als unabhängig positive Norm identifiziert. Die bereits bekannte quadratische Gaußauslesung trägt in der angegebenen Variante nur gcd(t,N), das aus t und N bereits direkt berechenbar ist. Ein endlicher physikalischer Filter ändert diesen algorithmischen Vertrag nicht. Für dunkle Materie, dunkle Energie, Baryogenese, starkes CP und schwarze Löcher wurde kein fertiger dynamischer Ursprung berechnet. Das Fehlen dieser Ergebnisse wird nicht in einen allgemeinen Unmöglichkeitssatz umgedeutet.

## 11. Tatsächlich ausgeführte Reproduktion

`verify_exact.py` wurde normal und mit `python -OO` ausgeführt. Beide Läufe bestehen 162 benannte Akzeptanzprüfungen und erzeugen bytegleiche Ergebnisdateien. Der Prüfer verwendet explizite Ausnahmen statt abschaltbarer Assertions.

Die Akzeptanztests sind ganzzahlig, rational oder symbolisch. Die ausgegebenen Dezimalzahlen sind getrennt als hochpräzise Formelauswertungen markiert. Die Zahl 162 zählt Kontrollbedingungen, nicht unabhängige Entdeckungen. Die uniformen analytischen Sätze sind oben ausgeschrieben; sie wurden nicht in Lean formalisiert. Die Großdiagonalisierung des 24024 dimensionalen Singulettoperators wurde nicht neu ausgeführt.

Reproduktion:

```sh
python verify_exact.py --output results.json
python -OO verify_exact.py --output results_optimized.json
cmp results.json results_optimized.json
```

Benötigt werden Python mit SymPy und mpmath. Die genauen Versionen des ausgeführten Laufs stehen in `ENVIRONMENT.txt`. Das Paket enthält keinen Zugangsschlüssel, keinen Zugriff auf externe private Quellpfade und keine veränderten Originaldokumente. SHA256 Werte der Eingaben und Ausgabedateien stehen im Manifest.

## Literatur und zusätzliche Quellen

[R1] J. Dehaene, B. De Moor: The Clifford group, stabilizer states, and linear and quadratic operations over GF(2). Physical Review A 68, 042318 (2003). https://arxiv.org/abs/quant-ph/0304125

[R2] S. Arfaee, E. Nestoridi: Shuffling via Transpositions. arXiv:2504.07918v1 (2025), insbesondere die Tableau Inhaltsformel in Theorem 1.1. https://arxiv.org/html/2504.07918v1

[R3] M. Christandl et al.: Perfect Transfer of Arbitrary States in Quantum Spin Networks. Physical Review A 71, 032312 (2005). https://arxiv.org/abs/quant-ph/0411020

[R4] S. Carpi, L. Tomassini: Energy bounds for vertex operator algebra extensions. arXiv:2303.14097. https://arxiv.org/abs/2303.14097

[R5] ACT Collaboration: Atacama Cosmology Telescope DR6 cosmological parameter analysis, arXiv:2503.14452v2, Tabelle 5, P-ACT-LB2. https://arxiv.org/pdf/2503.14452v2

[R6] Verbundene TFPT Quellübersicht: https://github.com/sthamann/tfpt/blob/main/experiments/theory-contracts/RESEARCH_2026-09-09.md . Gelesener Inhaltsblob: `db6c14e8e55e835d146dd58e1fc77a9a1247ad85`. Die Übersichtsdatei ist eine geprüfte Quelle über den angegebenen Archivstand, kein unabhängiger Neulauf ihrer kompletten Beweiskette.
