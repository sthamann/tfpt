# ChatGPT-Antwort 2 — Optimaler Stabilizer-Eingang und neue Schranken

Datum: 14. September 2026  
Quelle: ChatGPT-Antwort an Stefan, archiviert als lokale Markdown-Datei.

**Stefan, ein konkreter Optimalitätsbeweis ist jetzt gelungen: Der bestmögliche Stabilizer Eingang für euren Vierträgerzustand hat Überlappquadrat \(3/8\). Daraus folgen eine bessere Präparation, eine exakt optimierte Feedbackkontraktion und neue Fehlergrenzen. Zusätzlich habe ich die lokalen Spektralschranken und die äußere Bandtrennung verschärft.**

Die vollständige Schließung **aller** Punkte habe ich damit nicht erreicht. Meine vorherigen Aussagen „T2 praktisch lösbar“ und „Vierfachstruktur technisch fast geschlossen“ waren als Statusangaben zu stark. Eine bekannte mathematische Methode ist noch nicht der fehlende Beweis.

Im Folgenden stehen die tatsächlich hergeleiteten Ergebnisse. Die vollständigen Beweise, die ausführbare Schaltung und die ausgeführten Prüfungen sind im beigefügten Paket enthalten.

## 1. Vollständig gelöst: Welcher Stabilizer Eingang ist für euren Filter optimal?

Der bisherige Eingang ist

\[
|\chi\rangle=
\frac{|01\rangle-|10\rangle}{\sqrt2}
\otimes
\frac{|23\rangle-|32\rangle}{\sqrt2}.
\]

Sein Überlapp mit dem antisymmetrischen Vierträgerzustand beträgt

\[
|\langle\Omega|\chi\rangle|^2=\frac16.
\]

Dieser Eingang und sein Überlapp sind im Hauptdokument festgelegt.

### Neuer Satz

Für **alle reinen Stabilizerzustände der acht Qubits** in der bisherigen Ququartkodierung gilt:

\[
\boxed{
\max_{|s\rangle\ \mathrm{Stabilizer}}
|\langle\Omega|s\rangle|^2=\frac38
}
\]

Dasselbe Maximum gilt für konvexe Mischungen solcher Zustände.

Das ist keine numerische Vermutung und keine Suche, die lediglich einen guten Kandidaten gefunden hat. Es gibt eine vollständige Obergrenze und einen expliziten Zustand, der sie erreicht.

### Der Beweis

Ω besitzt vier unabhängige gemeinsame Pauli Stabilizer. Ihr gemeinsamer Unterraum lässt sich durch die Clifford Isometrie

\[
\mathcal V|b,c\rangle=
\frac12\sum_{a=0}^{3}
|a,\ a\oplus b,\ a\oplus c,\ a\oplus b\oplus c\rangle
\]

als Raum von vier logischen Qubits darstellen. Dabei ist \(\oplus\) die bitweise Addition modulo zwei.

In dieser Darstellung wird Ω zu

\[
\mathcal V^\dagger|\Omega\rangle
=
\frac{
|6\rangle-|7\rangle-|9\rangle
+|11\rangle+|13\rangle-|14\rangle
}{\sqrt6}.
\]

Der relevante Träger besteht also aus den sechs Punkten

\[
S=\{6,7,9,11,13,14\}\subset\mathbb F_2^4.
\]

Ein reiner Stabilizerzustand hat in der Rechenbasis einen affinen Träger \(A\) mit \(2^k\) Punkten und gleich großen Amplitudenbeträgen. Diese Standardbeschreibung der Stabilizerzustände liefert die mathematische Grundlage.

Damit folgt unabhängig von seinen Phasen:

\[
|\langle s|\mathcal V^\dagger\Omega\rangle|^2
\le
\frac{|A\cap S|^2}{6\cdot2^k}.
\]

Für affine Dimensionen \(k=0,1,2,3,4\) sind die maximalen Schnittgrößen

\[
1,\ 2,\ 3,\ 4,\ 6.
\]

Daraus entstehen die Obergrenzen

\[
\frac16,\quad\frac13,\quad\frac38,\quad\frac13,\quad\frac38.
\]

Die beiden nichttrivialen Schnittgrenzen lassen sich direkt beweisen: Vier Punkte einer affinen Ebene haben XOR null. Vier der sechs Punkte von \(S\) können daher keine vollständige Ebene bilden, weil sonst auch die beiden übrigen verschiedenen Punkte XOR null hätten. Eine affine Hyperebene kann höchstens vier Punkte enthalten, weil der Schnitt gerade groß sein muss und \(S\) den ganzen vierdimensionalen affinen Raum aufspannt.

Der Prüfer hat zusätzlich **alle 307 affinen Unterräume** dieses Raums exakt enumeriert und die Grenzen bestätigt.

Der Zustand

\[
|s_*\rangle=
\frac{|6\rangle-|7\rangle-|9\rangle+|8\rangle}{2}
\]

ist selbst ein Stabilizerzustand und erreicht die Grenze. Somit ist

\[
\boxed{|\sigma\rangle=\mathcal V|s_*\rangle}
\]

ein optimaler Eingang.

### Die Herstellung ist explizit

Die exportierte Schaltung beginnt bei \(|00000000\rangle\) und benötigt:

**4 Hadamards, 13 CNOT, 2 X und 2 Z.**

Alle 256 Ausgangsamplituden wurden aus der exportierten Schaltung mit ganzzahliger Rechnung geprüft.

Wichtig ist der Ressourcenunterschied: Die Schaltung verwendet auch **Clifford Kopplungen zwischen den bisherigen Paaren**. Deren native Verfügbarkeit aus TFPT ist damit nicht bewiesen.

Das ist keine nebensächliche Einschränkung. Über den Schnitt zwischen den beiden Paaren hat Ω sechs gleiche Schmidtkoeffizienten. Daher gilt für jeden dort separablen Eingang höchstens \(1/6\). **Der bisherige Eingang war innerhalb der ungekoppelten Paarpräparation bereits optimal. Die Verbesserung benötigt zusätzliche Verschränkung zwischen den Paaren.**

### Was das am unveränderten Experiment verbessert

Für euren bestehenden mikroskopischen Filter gilt

\[
K_{\mathrm{acc}}=wP_\Omega,
\qquad
w=
\frac12\left(
1+\frac{\Delta}{\sqrt{\Delta^2+24t^2}}
\right).
\]

Diese vollständige akzeptierte Operation einschließlich der Leerbelegungsselektion stammt aus v1.4.

Bei einem Eingang mit Überlappquadrat \(a\) folgt deshalb exakt:

\[
p_{\mathrm{prep}}=aw^2,
\qquad
p_{\mathrm{behalten}}=aw^4,
\qquad
p_{\mathrm{frisch}}=\frac{17}{32}aw^4.
\]

Mit \(a=3/8\) statt \(1/6\) ergibt die eigene Neuberechnung bei \(t/\Delta=1/20\):

| Größe | Bisheriger Eingang | Optimaler Stabilizer Eingang |
|---|---:|---:|
| Präparation erfolgreich | 16,1915 % | **36,4309 %** |
| Gesamterfolg, Record behalten | 15,7299 % | **35,3924 %** |
| Gesamterfolg, Record frisch | 8,3565 % | **18,8022 %** |
| Präparationsversuche im Mittel | 6,1761 | **2,7449** |

**Alle Rohwahrscheinlichkeiten steigen exakt um den Faktor \(9/4\).**

Die Filter selbst wurden nicht ausgetauscht. Ihre Zeitkosten bleiben bestehen. Der Quotient frisch/behalten bleibt exakt \(17/32\), und sämtliche Fehlzweige sind weiterhin mitgerechnet.

Vollständig gelöst ist damit die **optimale Eingangswahl für diesen festgehaltenen Filter innerhalb der Stabilizerklasse**, nicht die primitive Herkunft sämtlicher Kontrollen.

## 2. Vollständig gelöst: Die optimale Feedbackkontraktion für diesen Resetvertrag

Der bisherige Feedbackkanal setzt bei Misserfolg auf \(|0123\rangle\) zurück. Das kostet viel Konvergenzgeschwindigkeit, weil dessen Ω Anteil nur \(1/24\) beträgt. Der zugehörige Operator und die ursprüngliche Kontraktionsschranke sind in v1.4 ausdrücklich angegeben.

Die Verbesserung lässt sich allgemein beweisen.

Setze wie bisher

\[
K=P^-_{03}P^-_{02}P^-_{01},
\qquad
\beta=\frac{9+\sqrt{17}}{32}.
\]

Für einen beliebigen festen Resetzustand \(\sigma\) mit

\[
a=\operatorname{Tr}(P_\Omega\sigma)>0
\]

lautet der Kanal

\[
\mathcal E_\sigma(\rho)
=
K\rho K^\dagger+
\operatorname{Tr}[(I-K^\dagger K)\rho]\,\sigma.
\]

### Neuer Satz

Dieser Kanal besitzt Ω als einzigen stationären Zustand und erfüllt

\[
\boxed{
1-F(\mathcal E_\sigma\rho)
\le
r(a)\,[1-F(\rho)],
\qquad
r(a)=1-a(1-\beta).
}
\]

Die Konstante ist als Einzyklusgrenze für beliebige Eingänge **scharf**.

Der Beweis benötigt nur zwei Zeilen. Weil \(K\Omega=K^\dagger\Omega=\Omega\), gilt exakt

\[
F(\mathcal E_\sigma\rho)
=
F(\rho)+
a\,\operatorname{Tr}[(I-K^\dagger K)\rho].
\]

Zusammen mit

\[
I-K^\dagger K\ge(1-\beta)(I-P_\Omega)
\]

folgt die Behauptung. Ein Eigenvektor von \(K^\dagger K\) zum Eigenwert \(\beta\) erreicht die Grenze.

Das charakteristische Polynom wurde hier in der treuen 24 dimensionalen Darstellung exakt neu berechnet. Die Identität und ihre Übertragung auf den physischen Vierququart Raum stehen im Beweisbericht.

### Das Ergebnis

| Reset | Kontraktionsfaktor \(r\) | Fehlerverstärkung \(1/(1-r)\) | Zyklen für Fehler \(10^{-6}\), eine Zelle | Zyklen für global \(10^{-6}\), 4096 unabhängige Zellen |
|---|---:|---:|---:|---:|
| Bisheriger Basisreset | 0,975421 | 40,6847 | 556 | 890 |
| Bereits vorhandener Eingang \(\chi\) | 0,901683 | **10,1712** | **134** | **214** |
| Optimaler Stabilizer Eingang \(\sigma\) | 0,778786 | **4,5205** | **56** | **89** |

Für den optimalen Stabilizer Reset lautet die exakte Rate

\[
\boxed{
r_*=\frac{187+3\sqrt{17}}{256}.
}
\]

Die Optimalität folgt unmittelbar aus dem vorherigen Satz: Größer als \(a=3/8\) kann kein Stabilizer Reset sein, und die Einzyklusgrenze ist scharf.

**Bereits die Verwendung des vorhandenen Zweisinguletts verbessert den konservativen Fehlerverstärkungsfaktor um vier. Der optimale Stabilizer Reset verbessert ihn um neun.**

Die Zykluszahlen sind nicht nur gerundete Logarithmen. Im Prüfer wird \(\sqrt{17}\) rational eingeschlossen und anschließend mit exakten Potenzen geprüft, dass die genannte Zykluszahl die Schranke erfüllt und die vorherige sie noch verfehlt.

Bei einem Gesamtfehler von höchstens \(\varepsilon\) pro Zyklus in halber Diamantnorm bleibt

\[
1-F_m
\le
r^m(1-F_0)
+
\varepsilon\frac{1-r^m}{1-r}.
\]

Die zusätzliche Präparationsschaltung kann allerdings den tatsächlichen Zyklusfehler und die Dauer verändern. **Neunmal weniger mathematische Fehlerverstärkung ist nicht automatisch neunmal bessere Hardware.**

## 3. Neu bewiesen: Eine Fehlergrenze für tatsächlich wechselwirkende Zellen

Hier lässt sich die unabhängige Zellrechnung wirklich erweitern, ohne eine Wechselwirkung lediglich zu behaupten.

Betrachte \(N\) Zellen. Für Zelle \(i\) sei \(P_i\) der Ω Projektor und

\[
q(\rho)=\frac1N\sum_i\operatorname{Tr}[(I-P_i)\rho]
\]

die mittlere lokale Infidelität.

Ein Zyklus besteht aus den lokalen Feedbackkanälen und anschließender Entwicklung unter dem gekoppelten Austauschoperator

\[
H=
\sum_i H_i+
\sum_{e=(i,j)}\lambda_e V_e.
\]

Dabei gelten die ausdrücklich benannten Voraussetzungen:

\(H_i\) erhält den lokalen Ω Unterraum. \(V_e\) ist der positive Austauschprojektor einer Brücke zwischen zwei Zellen. Der Zellgraph hat höchstens \(z\) Nachbarn je Zelle, und \(0\le\lambda_e\le\lambda\).

### Neuer Satz

Für die Entwicklung während einer Zeit \(\tau\) und lokale Kanalfehler höchstens \(\varepsilon\) gilt

\[
\boxed{
q_m\le
r^m q_0+
\left(
\varepsilon+\frac{z\lambda|\tau|}{2\hbar}
\right)
\frac{1-r^m}{1-r}.
}
\]

**Die Schranke gilt unabhängig von \(N\), auch bei anfänglich verschränkten Zellen.**

Der entscheidende Schritt ist eine Operatornormabschätzung. Setze \(Q_i=I-P_i\). Weil \(V_e\) ein Projektor ist,

\[
\|V_e-I/2\|=\frac12.
\]

Und weil \(Q_i,Q_j\) kommutierende Projektoren sind,

\[
\|Q_i+Q_j-I\|\le1.
\]

Daraus folgt

\[
\|[V_e,Q_i+Q_j]\|\le1.
\]

Nach Summation über die Brücken und Integration der Heisenberggleichung verändert die Wechselwirkung den mittleren lokalen Fehler deshalb um höchstens \(z\lambda|\tau|/(2\hbar)\) pro Zyklus. Zusammen mit der Feedbackkontraktion ergibt sich die Formel.

Das beantwortet eine konkrete bisher offene Belastungsfrage:

**Wie stark dürfen die Zellen zwischen zwei Rücksetzungen miteinander wechselwirken, bevor die lokale Präparationsgenauigkeit verloren geht?**

Die Grenze ist jetzt berechenbar.

Sie beweist aber nicht, dass der verschränkte Grundzustand des gekoppelten Systems präpariert wird. Das Ziel dieses Protokolls bleibt das lokale Ω Muster. Auch folgt daraus keine größenunabhängige globale Produktfidelität bei festem Fehlerboden. Dafür gilt lediglich

\[
1-F_{\mathrm{global}}\le Nq.
\]

Ebenso bleibt dies ein Satz über das benannte nackte Austauschmodell mit Rücksetzung, nicht über einen bereits hergeleiteten vollständigen kosmologischen Ursprung.

## 4. Neu bewiesen: Schärfere lokale Spektren und eine bessere äußere Bandtrennung

v1.4 enthält die wichtige positive Darstellung

\[
F_4=\sum_v A_v(A_v-I),
\qquad
A_v=\sum_{e\ni v}(I-S_e).
\]

Die dortige universelle Kontrolle benutzt eine Einschließung des Sternspektrums zwischen null und zehn.

**Auf dem tatsächlich verwendeten Vierfarbenraum lässt sich diese Grenze verschärfen.**

### Das physische Sternspektrum liegt zwischen null und acht

Ein Clebsch Stern besteht aus einem Zentrum und fünf Nachbarn. Sein Operator ist bis auf Umnummerierung

\[
A_v=5I-J_6,
\]

wobei \(J_6\) die Summe der fünf Sterntranspositionen ist.

Die Eigenwerte solcher Summen werden durch die Inhalte von Youngtableaus bestimmt. Auf sechs Ququarts treten nur Formen mit höchstens vier Zeilen auf. Damit folgt

\[
\boxed{
\operatorname{spec}(A_v)\subseteq\{0,1,\ldots,8\}.
}
\]

Die verwendete Inhaltsformel ist ein etablierter Darstellungssatz; die Anwendung auf den physischen TFPT Stern und die folgenden Grenzen wurden hier ausgeführt.

Zusätzlich habe ich ein unabhängiges ganzzahliges Zertifikat gebaut. Für

\[
p(x)=\prod_{k=0}^{8}(x-k)
\]

liefert die vollständige Rechnung in der Gruppenalgebra

\[
\operatorname{Tr}(p(A)^\dagger p(A))
=
21946982400\,d(d-4)^2(d-3)(d-2)(d-1).
\]

Bei der physischen lokalen Dimension \(d=4\) ist die Spur exakt null. Weil der Operator positiv ist, folgt \(p(A)=0\). Dafür werden keine Gleitkommaeigenwerte benötigt.

### Konsequenz für die vierte Ordnung

Aus \(0\le a\le8\) und ganzzahligem \(a\) folgt

\[
0\le a(a-1)\le7a\le56.
\]

Für die 16 Clebsch Sterne erhält man deshalb

\[
\boxed{0\le F_4\le896I.}
\]

Eine zweite exakte Ungleichung lautet

\[
\boxed{F_4\ge1344I-56H_0.}
\]

Am Betriebspunkt \(t/\Delta=1/20\) ergibt sich für den trunkierten Operator in \(J\) Einheiten:

\[
\boxed{
H_{\mathrm{tr}}
=
H_0+\frac{F_4}{800}
\ge
0{,}93H_0+1{,}68I.
}
\]

Das ist eine zusätzliche rigorose Operatorgrenze, keine weitere Dezimalstelle einer Diagonalisierung.

### Konsequenz für das Vermittlerband

Im erreichbaren Matchingsektor mit

\[
Q_v=n_f(v)+\sum_{e\ni v}n_e=1
\]

kann dieselbe physische Vierfarbenbeschränkung auch die Normen zwischen den Bosonensektoren verbessern.

Die eigenen exakten Grenzen lauten jetzt

\[
a_n^2=
(64,104,126,128,120,84,56,16)
\]

statt

\[
(80,124,144,136,120,84,56,16).
\]

Ein rationaler LDL Test ergibt damit

\[
\boxed{
QHQ\ge\frac{19}{25}\Delta Q
=
0{,}76\Delta Q.
}
\]

Diese Aussage gilt bei \(|t|/\Delta\le1/20\), kantenlokalen Vermittlern, ohne Hopping und im genannten Matchingsektor.

**Die Sektorgrenze ist wesentlich.** Die neue \(0{,}76\Delta\) Aussage ersetzt nicht stillschweigend die breiter gefasste \(0{,}7\Delta\) Aussage von v1.4 für andere Belegungssektoren.

Die entsprechende energieabhängige Feshbach Restabschätzung sinkt außerdem von ungefähr \(1{,}71601J\) auf

\[
\boxed{0{,}937795766671J.}
\]

Sie ist weiterhin **kein** kanonischer Rest nach \(H_2+H_4\) und zertifiziert den inneren Gap noch nicht.

### Die Vierfachheit ist damit ausdrücklich noch nicht bewiesen

Hier muss ich einen Fehler meiner vorherigen Antwort korrigieren:

**Vier Eigenwerte in einem zertifizierten Intervall beweisen keine vierfache Entartung.**

Vier verschiedene Werte

\[
\lambda,\quad\lambda+\delta,\quad
\lambda+2\delta,\quad\lambda+3\delta
\]

können im selben Intervall liegen. Ein Inertiatest zählt sie korrekt, beweist aber nicht ihre Gleichheit.

Dafür braucht es zusätzlich einen exakten Symmetriebeweis oder einen anderen Gleichheitsnachweis. Die neue Operatorgrenze hilft beim Sektorausschluss; der erforderliche vollständige Zertifizierungslauf wurde hier nicht ausgeführt. Auch v1.4 unterscheidet die numerische Vierfachstruktur ausdrücklich von einer rigorosen Zertifizierung.

## 5. Was sich an der primitiven Quelle nicht durch einen Namen oder einen Clock lösen lässt

Die vorherige Antwort hat zwei Probleme zu leicht behandelt.

**Erstens: Ein Programm in einen Hamiltonoperator einzubauen leitet das Programm nicht her.**

Für vorgegebene Gatter \(U_1,\ldots,U_m\) lässt sich eine autonome perfekte Ausführung konstruieren. Die korrekte Konstruktion verwendet geeignete Kopplungsgewichte proportional zu

\[
\sqrt{(k+1)(m-k)}.
\]

Im Beweisbericht steht der vollständige Operator samt exakter Transferidentität. Das ist eine Anwendung der bekannten perfekten Transferkonstruktion. Aber sämtliche \(U_k\), die Gewichte und der Clockeingang bleiben Eingaben.

Damit wird externe Ablaufsteuerung in interne Dynamik übersetzt. **Die native Herkunft der Kontrollen wird dadurch nicht bewiesen.**

**Zweitens: Strikte Kantenfaktorisierung ist selbst eine zusätzliche Vorgabe.**

Eine unabhängige Vermittlerfaser pro Kante schließt eine gemeinsame Bank innerhalb dieses Vertrags aus. Aus gewöhnlicher Lokalität folgt dieser Vertrag nicht. Genau dafür enthält v1.4 das lokale Gegenmodell einer Bank pro Zelle.

Die Nichtauswahl ist auch direkt sichtbar. Die in den Unterlagen untersuchte Familie

\[
U_\theta=
\begin{pmatrix}
e^{i\theta}P^+&W^\dagger\\
W&0
\end{pmatrix}
\]

liefert denselben ersten blockweise dephasierten Ausgang, aber verschiedene Fortsetzungen:

\[
U_0^2=I,
\qquad
U_{\pi/2}^2=-S
\]

auf dem Materieraum. Derselbe erste Schatten bestimmt die weitere Maschine also nicht. Das ist ein exaktes Gegenbeispiel unter dem dort festgelegten Auslesevertrag.

Es folgt daraus kein allgemeines Verbot einer reicheren eindeutigen TFPT Quelle. Es folgt, dass **die bisher genannten Bedingungen ihre Auswahl noch nicht leisten**.

## 6. T2, Raumzeit, Chiralität und Gravitation: Die fehlenden Beweise bleiben konkret

### T2: Eine zusätzliche Vertexoperatoralgebra ist noch nicht das native Halbladungsfeld

Die Paritätsgrenze ist streng:

\[
[A,\Pi]=0,\qquad \Pi=(-1)^{2Q}
\]

bleibt unter Produkten und geeigneten beschränkten starken Grenzwerten erhalten. Ein nichtverschwindender Halbladungsoperator antikommutiert dagegen mit \(\Pi\).

Er entsteht deshalb nicht durch immer weitere Produkte ausschließlich ganzzahliger Ladungsverschiebungen. Diese Obstruktion ist in v1.4 ausdrücklich ausgearbeitet.

Das Hinzufügen eines ungeraden Intertwiners kann eine mathematische Erweiterung definieren. Es ersetzt aber nicht den Nachweis seiner nativen Normierung, gemeinsamen Definitionsmenge, Adjungierten und Energiebeherrschung.

Ich habe hierzu auch die verbundene Quellübersicht des TFPT Repositorys gelesen. Sie berichtet bereits einen nativen **ganzzahlig geladenen** CAR Grenzwert mit Energiekontrolle und beiden Adjungierten. Die Halbladung und ihre gemeinsame Clock und Cocycle Identifikation bleiben dort ausdrücklich getrennt. Diese Vorarbeit ist also vorhanden; sie ist nicht schon der fehlende T2 Abschluss.

### T3 und T4: Zwei Bänder und Fluss drei sind keine abgeleiteten Auswahlregeln

Die Kodimension drei einer generischen Zweibandberührung ist korrekt. Daraus folgt aber nur dann eine Dimensionsauswahl, wenn die Quelle selbst den betreffenden Zweibandsektor und die weiteren Voraussetzungen auswählt.

Ebenso berechnet der vorhandene Overlap Test drei Nullmoden **bei eingesetztem Fluss drei**. Die Kontrollflüsse eins und vier liefern entsprechend andere Zahlen. Der Mechanismus funktioniert, aber er erklärt die Wahl der Familienzahl nicht.

Die vollständige native skalierende Familie mit gemeinsamem Lorentzkegel und chiralem Maß habe ich hier nicht konstruiert.

### T7: Ein Tensorprojektor erzeugt keinen gravitativen Freiheitsgrad

Ein regulärer Projektor kann vorhandenes Spektralgewicht auswählen. Er kann nicht eine positive Energieschwelle in einen masselosen Pol verwandeln.

Auch ein Term proportional zu \(R\) in einer Wirkung für einen vorgegebenen Hintergrund beweist noch nicht, dass die Metrik ein dynamischer quantisierter Freiheitsgrad der ursprünglichen Quelle ist. Genau dieser Unterschied bleibt im vorhandenen Tensor und Ward Test offen.

Meine vorherige Verkürzung „T7 folgt dann aus T3 plus T5“ war daher ebenfalls zu stark. Dafür fehlt ein eigener dynamischer Nachweis.

## 7. Der gemeinsame Parametervergleich lässt sich entscheiden, aber nicht passend machen

Für die unveränderte führende Inflationsbranche gilt

\[
A_s=\frac{N^2c_3^7}{24\pi^2},
\qquad
n_s=1-\frac2N,
\qquad
c_3=\frac1{8\pi}.
\]

Elimination von \(N\) liefert exakt

\[
\boxed{
A_s(1-n_s)^2=\frac{c_3^7}{6\pi^2}.
}
\]

Damit ist bewiesen: **Eine andere Wahl von \(N\) allein kann Amplitude und Neigung nicht unabhängig anpassen.**

Ich habe die angegebene ACT Primärtabelle erneut visuell geprüft. In der Spalte P-ACT-LB2 stehen \(\ln(10^{10}A_s)=3{,}062\) und \(n_s=0{,}9752\pm0{,}0030\).

Die eigene Neuberechnung ergibt bei Kalibrierung an der Amplitude

\[
N\approx56{,}62391,
\qquad
n_s\approx0{,}96467923.
\]

Der Abstand entspricht etwa **3,5069 der genannten marginalen Standardunsicherheiten**. Umgekehrt führt die Kalibrierung am zentralen Tilt zur etwa **2,02842 fachen Amplitude**.

Das ist eine bewiesene Nichtpassung der beiden Zentralwerte innerhalb der unveränderten Formel. Es ist **keine gemeinsame Likelihoodauswertung und kein Ausschluss der gesamten TFPT Theorie**.

Beim Flavour gilt ebenso konkret: Identische orthonormale linke und rechte innere Moden mit konstantem Skalarprofil liefern

\[
Y_{ab}=y\delta_{ab}.
\]

Dieser konkrete Zweig besitzt keine Massenhierarchie. Eine bislang nicht hergeleitete neue Textur ist keine Lösung dieser Lücke.

## 8. Vollständiger Status aller Punkte nach dieser Rechnung

| Tor | Tatsächlich erreicht | Nicht geschlossen |
|---|---|---|
| **T1** | Exakte Trennung zwischen Ablaufkompilation und primitiver Auswahl; Gegenbeispiele zur Auswahl allein durch Lokalität | Native Quelle sämtlicher Operationen, Markierungen und Auswahlregeln |
| **T2** | Präzise Paritätsgrenze und Abgleich mit der vorhandenen nativen CAR Vorarbeit | Native Halbladung einschließlich Domänen, Adjungierten, Energie und Phasentransport |
| **T3** | Die bisher verwendeten Dimensionsargumente sind auf ihre Voraussetzungen eingegrenzt | Eine ausgewählte skalierende Quelle mit gemeinsamem 3+1 dimensionalem Lorentzkegel |
| **T4** | Indexmechanismus und Familienauswahl sind sauber getrennt | Vollständiges chirales Standardmodellmaß und native Familienzahl |
| **T5** | Neue lokale Operatorgrenzen, bessere äußere Matchingbandtrennung und ein Fehlerbound mit echter Austauschkopplung | Exakte Vierfachheit, vollständiger mikroskopischer Rest und wechselwirkender Kontinuumslimes |
| **T6** | Gemeinsame Inflationsrelation erneut ausgewertet; konkreter konstanter Flavourzweig ohne Hierarchie | Interne gemeinsame Herleitung sämtlicher Kopplungen, Massen und Mischungen |
| **T7** | Die Projektor und Hintergrundwirkungsschlüsse sind als unzureichend abgegrenzt | Dynamischer masseloser quantisierter Spin zwei aus derselben Quelle |
| **T8** | **Optimaler Stabilizer Eingang, vollständige neue Rohstatistik und optimale Resetkontraktion im benannten Modell** | Physischer Ursprung von Umgebung, Anfangszustand und gemeinsamem Quellfunktional |

Auch RH, allgemeine Faktorisierung und P versus NP wurden durch diese Rechnung nicht gelöst. Insbesondere wurde keine vollständige signierte Weil Form als unabhängig positive Norm identifiziert. Die offenen Anforderungen an dunkle Materie, dunkle Energie, Baryogenese, starkes CP und schwarze Löcher werden durch die verbesserte endliche Präparation ebenfalls nicht erfüllt. Die entsprechenden Aufgaben sind in den Ausgangsunterlagen getrennt ausgewiesen.

### Beweise und Reproduktion

Der unabhängige Prüfer wurde **normal und mit `python -OO` ausgeführt**. Beide Läufe bestehen 162 benannte Prüfbedingungen und erzeugen bytegleiche Ergebnisdateien. Die Akzeptanzprüfungen sind ganzzahlig, rational oder symbolisch; Dezimalausgaben sind getrennt als Formelauswertungen ausgewiesen. Es gab keinen neuen vollständigen Clebsch Großlauf, keine Hardwareausführung und keine Lean Formalisierung.

**Der belastbare Fortschritt ist diesmal nicht ein weiterer Architekturvorschlag: Es sind ein vollständiger Optimalitätsbeweis und mehrere neue quantitative Sätze. Die vollständige Physik aller acht Tore ist damit weiterhin nicht abgeleitet.**
