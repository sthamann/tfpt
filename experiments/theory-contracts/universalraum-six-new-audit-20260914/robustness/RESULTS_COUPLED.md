# Ein Record genügt für ξ: exakte Präparation, Ressourcenabstand und Kopplungsbudget

14. September 2026. Unabhängige Fortsetzung zur nachgelieferten
`TFPT_Universalraum_Forschungsfortsetzung_2026-09-14.md`, Abschnitte 3 und 5.
Alle Konstruktionen bleiben im ausdrücklich angegebenen Operationsvertrag.

## 1. Stärkere neue Vereinfachung: exakte Ω-Präparation mit nur einem Record

Für die neue Quelle

\[
\xi=\frac14\sum_{d=0}^3\sum_{u,v=0}^1(-1)^{u+v}
|d,d\oplus2\oplus u,d\oplus1\oplus2v,d\oplus3\oplus u\oplus2v\rangle
\]

gilt die vollständige **ganzzahlige 256D-Identität**

\[
(I-S_{03})\xi_{num}=-\Omega_{num},\qquad
\boxed{P^-_{03}\xi=-\sqrt{3/8}\,\Omega.}
\]

Hier sind ξ_num=4ξ und Ω_num=√24Ω die jeweiligen ganzzahligen Vektoren.
Der Prüfer vergleicht alle Komponenten, nicht nur den Überlapp.
Damit liefert **ein einziger adressierter Record auf Kante 03** mit akzeptiertem
Minus-Ausgang den exakten Zielzustand. Die Rohwahrscheinlichkeit ist 3/8, die
Abbruchwahrscheinlichkeit 5/8 und die ideale bedingte Fidelity eins.

Das entfernt für diese Quelle jede K^n-Approximation aus der Präparation.
Es benötigt weder einen primitiven PΩ-Projektor noch kontrollierte Sternentwicklung.
Das bereits konstruierte feste-Δ-Recordmakro kann unverändert eingesetzt werden.
Die Clifford-Vorbereitung von ξ und die native Verfügbarkeit der Recordprimitive
bleiben explizite Voraussetzungen.

Pro Präparationsversuch genügt somit ein Makro. Bis zum Erfolg benötigt man im
Mittel 8/3 Makros und im endlichen Q-Fenstervertrag

\[
\mathbb E[T_{prep,H}]=\frac83\,70\pi\hbar/\Delta
=586.4306286700947\,\hbar/\Delta.
\]

Die Zeit zur Herstellung von ξ, sämtliche Resets, Schaltflanken und der Controller
sind darin zusätzlich zu berücksichtigen. P−03 allein ist kein allgemeiner
Ω-Projektor: Die Identität gilt für diesen speziellen Eingang. Die separate
Rücktransformation zur ξ-Messbasis für einen allgemeinen Endtest wird im
Root-Protokoll behandelt.

## 2. Der quantitative Stabilizer-Abstand ist gültig und lässt sich verstärken

Als gesicherte Ressourcenbasis gilt
max_stabilizer Tr(PΩρ)=3/8, auch für Mischungen. Die Probe kontrolliert unabhängig
die zugehörigen 307 affinen Träger und die Schnittmaxima (1,2,3,4,6); der
Reduktions-/Normalformbeweis bleibt derselbe ausdrücklich benannte Stabilizervertrag.

Betrachte ein **vollständiges Instrument** mit akzeptiertem und abgelehntem Flag und
den Effektzeugen

\[
W=|acc\rangle\langle acc|\otimes(P_\Omega-3I/8),
\]

der auf dem abgelehnten Ausgang null ist. Jede Realisierung allein durch
Stabilizeroperationen, Stabilizerhilfen, Cliffordgatter, Paulimessungen, klassisches
Feedforward und Verwerfen hat Tr(Wρ_out)≤0, wenn der Eingang ξ ein Stabilizer ist.
Postselektion ändert dies nicht, weil der akzeptierte Ausgang ein **unnormiertes**
Stabilizergemisch bleibt.

W hat Spektrum {−3/8,0,5/8}, also Durchmesser eins. Für zwei vollständige
spurerhaltende Ausgänge ist deshalb

\[
|\operatorname{Tr}[W(\rho-\sigma)]|
\le\tfrac12\|\rho-\sigma\|_1.
\]

**Der vorgeschlagene Drei-Record-Zeuge stimmt:** Die unabhängige rationale Probe
ergibt p_acc=51/128 und p_good=3/8. Damit ist

\[
\langle W\rangle=3/8-(3/8)(51/128)=231/1024.
\]

Der Abstand dieses vollständigen Instruments zu jedem entsprechenden
Stabilizerinstrument in halber Diamantnorm ist mindestens 231/1024. Falls alle
drei primitiven Aufrufe durch vergleichbare Stabilizerkanäle mit Fehler ≤δ_R
ersetzt werden und die übrige Verdrahtung innerhalb dieser Operationsklasse liegt,
liefert die Teleskopsumme den korrekten hinreichenden Widerspruch bei
δ_R<77/1024. Anders gesagt: Mindestens ein benötigter Aufruf hat Abstand ≥77/1024;
für drei identische, Clifford-konjugierte Primitive ist dies eine Schranke an deren
gemeinsamen Minimalabstand zur abgeschlossenen Vergleichsklasse.

**Der neue Ein-Record-Zeuge ist stärker.** Auf ξ liefert bereits R03 im Minusflag
p_acc=p_good=3/8. Deshalb ist

\[
\boxed{\langle W\rangle=\frac38\left(1-\frac38\right)
=\frac{15}{64}=0.234375.}
\]

Somit hat das einzelne vollständige Recordinstrument Abstand mindestens **15/64**
in halber Diamantnorm zu jedem solchen Stabilizerinstrument. Für eine kohärente
Recordprimitive gilt derselbe untere Bound, wenn anschließende Pointermessung und
Flagbildung kostenlose Stabilizeroperationen der Vergleichsklasse sind:
Nachverarbeitung kann die Diamantdistanz nicht vergrößern.

Die Aussage betrifft eine genau definierte Operationsklasse. Sie ist **kein**
Unmöglichkeitssatz für allgemeine P1/P2, einen Compiler mit einer nichtstabilisierenden
Wedge-/Belegungsprimitive oder beliebige zusätzliche Quellressourcen.
Unvollständige, separat normalisierte Erfolgszweige dürfen nicht als vollständige
Vergleichsinstrumente eingesetzt werden. Ein darauf beruhender Mutant wird erkannt.

## 3. Robuster Anschluss der Ein-Record-Präparation

Im Instrumentvertrag aus `RESULTS.md` gilt jetzt p0=3/8, b0=0 und L=1. Daher

\[
1-F_{cond}\le\frac{\eta^2+q}{(\sqrt{3/8}-\eta)^2-q},
\quad \eta<\sqrt{3/8},
\]

wenn der Nenner positiv ist. Für das komplette Makro einschließlich aller
endlichen Q-Fenster gilt η≤70πδH/Δ plus gesonderte Eingangs-, Schalt- und
Controllerfehler. Der Normbound umfasst auch nichtkommutierende Leakage.

Eine gemeinsame ausreichende Wahl ist δH/Δ≤10⁻⁶ und q≤10⁻⁷ bei ansonsten
idealen Ressourcen. Die ausgegebene JSON-Datei enthält den daraus berechneten
bedingten Fehlerbound; er liegt unter 10⁻⁶. Die Bedingung betrifft die ganze
Operation samt Fehlerflag und ist keine reine Zeittoleranz.

Für ausschließlich symmetrisch fehlgelesene Recordbits mit Wahrscheinlichkeit f
ist die Bilanz noch genauer und exakt:

\[
p_{good}=(1-f)\frac38,\qquad p_{bad}=f\frac58,
\quad p_{acc}=\frac{3+2f}{8},\qquad
\boxed{1-F_{cond}=\frac{5f}{3+2f}.}
\]

So genügt f≤3·10⁻⁶/(5−2·10⁻⁶)≈6.0000024·10⁻⁷ für 10⁻⁶ konditionierten Fehler.
Diese Zahl darf nicht zugleich als Budget für weitere Fehlerklassen ausgegeben
werden; deren gemeinsame Kombination steht in der vorigen Ungleichung.

## 4. Quadratischer lokaler Kopplungsbound: korrekt und konkretisiert

Die Quelle betrachtet **erst** eine unitäre Zwischenzellphase für Dauer τ und
**danach** einen parallelen lokalen Kühlkanal mit Kontraktion r und zusätzlichem
lokalem Kanalfehler ε. Für P_i=PΩ,i und q_i=1−Tr(P_iρ) liefert

\[
b_i=\|P_iH_{int}(I-P_i)\|,\qquad
|\dot q_i|\le2b_i\sqrt{q_i(1-q_i)}/\hbar.
\]

Für reine Zustände folgt dies aus Cauchy–Schwarz zwischen den beiden
Projektionssektoren; für gemischte aus einer Purifikation. Lokale Hamiltonterme,
die mit P_i kommutieren, tragen nicht bei. Integration ergibt

\[
\sqrt{q_{i,m+1}}\le\sqrt{r(\sqrt{q_{i,m}}+\nu)^2+\epsilon},
\qquad \nu\ge\tau b_i/\hbar.
\]

Der positive Fixpunkt und die vollständige endliche Hülle sind tatsächlich

\[
x_* =\frac{r\nu+\sqrt{r\nu^2+(1-r)\epsilon}}{1-r},
\quad
\sqrt{q_{i,m}}\le x_*+r^{m/2}(\sqrt{q_{i,0}}-x_*)_+.
\]

Die Abbildung ist monoton und höchstens √r-Lipschitz. Dies rechtfertigt den
Fixpunktvergleich für beliebige Anfangszustände, nicht nur einen stationären Ansatz.

Die ursprüngliche P+-Brücke erlaubt einen besseren Normwert als ||V||=1:
Die einzelne Trägermarginale von Ω ist exakt I4/4, daher

\[
P_iVP_i=\frac58P_i,\qquad P_iV^2P_i=\frac58P_i,
\quad P_iV(I-P_i)VP_i=\frac{15}{64}P_i.
\]

Also ist **b=√15/8** pro normierter Brücke, nicht bloß ein geschätzter Wert.
Bei maximalem Grad z und Kopplung λ folgt

\[
\boxed{\nu=\frac{z\lambda\tau\sqrt{15}}{8\hbar}.}
\]

Für den optimalen Reset r=(187+3√17)/256≈0.778786394050207 und ε=0 gilt
x*=√r ν/(1−√r). Mit τ=3·70πℏ/Δ und J/Δ=0.005 erhält man
ν=1.5969628536646099 zλ/J. Die ausreichenden **asymptotischen** Budgets für
lokal q≤10⁻⁶ sind:

| ε pro Kühlzyklus | maximaler Wert von zλ/J aus dieser Schranke |
|---:|---:|
| 0 | **8.33826039581766·10⁻⁵** |
| 10⁻⁸ | 7.982583346255096·10⁻⁵ |
| 10⁻⁷ | 4.69697478386458·10⁻⁵ |
| (1−r)·10⁻⁶/2 | 4.2991292121830396·10⁻⁵ |

Für ein gegebenes z sind diese Werte durch z zu teilen. Gleichheit am
asymptotischen Grenzwert garantiert keinen endlichen Stoppzeitpunkt. Ein konkreter
endlicher Vertrag ist ε=0 und zλ/J≤4.16913019790883·10⁻⁵: Der Fehlerboden ist
dann 2.5·10⁻⁷, und **61 Zyklen** garantieren lokal höchstens 10⁻⁶ aus jedem Eingang.

Die Differentialungleichung liefert sogar die leicht schärfere Winkelhülle
q_i(τ)≤sin²(min(π/2,arcsin√q_i(0)+ν)). Für das Ziel Q beträgt ihr zulässiger
ν-Wert arcsin√((Q−ε)/r)−arcsin√Q. Bei Q=10⁻⁶ ist die Verbesserung klein;
sie wird als zusätzliche Kontrolle im JSON aufgeführt, nicht als großer Gewinn.

**Zeit-/Implementierungsgrenze:** Die eingesetzten 210π sind eine konkret gewählte
Zeit für die kohärente Kopplungsphase. Soll die Brücke stattdessen gleichzeitig
während aller lokalen Record- und Resetpulse aktiv bleiben, muss die Komposition
mit diesen nichtkommutierenden Kontrollgeneratoren gesondert bewiesen oder über
das vollständige Instrumentfehlerbudget erfasst werden. Die bloße Gleichsetzung
von Kopplungsfenster und Makrodauer beweist diesen gleichzeitigen Ablauf nicht.
Eine separate Kopplungsphase von 210π plus drei Kühlrecords braucht bereits
420πℏ/Δ Hamiltonzeit, zuzüglich Reset-/Quell-/Controllerzeiten. Ist λ größer als
die hier ausgewiesene ausreichende Grenze, wird die Garantie schwächer; daraus
folgt kein Scheitern des tatsächlichen Systems.

## 5. Neues exaktes Ergebnis für die wirklich gekoppelte Zweizellendynamik

Aus Ω_AΩ_B erzeugt eine Brücke λP+ zwischen je einem Materieträger

\[
q_A=q_B=\frac{15}{16}\sin^2(\lambda\tau/(2\hbar)).
\]

Die eigene Rechnung geht weiter und berechnet den anschließenden ξ-/σ-Feedback
genau. Schreibe den Brückenzustand als Kombination von ΩΩ und dessen Träger-Swap.
Der reine Swapzweig hat bei Anwendung von K auf Zelle A das exakte
Erfolgsgewicht **23/128**, also Fehlergewicht **105/128**. Diese Zahlen wurden
mit ganzen Zahlen auf allen **65536 Amplituden** geprüft.

Die Feedbackidentität F'=F+(3/8)p_fail ergibt dann für beide Zellen

\[
\boxed{q_A'=q_B'=\left(\frac{15}{16}-\frac38\frac{105}{128}\right)
\sin^2(\lambda\tau/(2\hbar))
=\frac{645}{1024}\sin^2(\lambda\tau/(2\hbar)).}
\]

Damit ist die tatsächliche Kontraktion in diesem gekoppelten Ein-Schrittversuch
**43/64=0.671875**, stärker als der allgemeine Wert r≈0.778786394050207.
Lokale Kühlung der anderen Zelle ändert die betrachtete Marginale nicht.
Zusätzliche vollständige numerische Dichtematrixprüfungen bestätigen die Formel
bei λτ/ℏ=0.002,0.02,0.2 und weisen die durch die Brücke entstandene gemischte
lokale Marginale aus.

Dies ist ein exakter dynamischer Fortschritt für den angegebenen Produktanfang
und genau einen gekoppelten Zyklus. Nach dem Reset entsteht im Allgemeinen eine
andere Mischzustandsfamilie; die bessere Konstante 43/64 wird daher nicht ohne
zusätzlichen Beweis über beliebig viele Zyklen fortgeschrieben. Der Zielvertrag
bleibt lokale Nähe zu Ω, nicht der verschränkte Grundzustand des gekoppelten H.

## Reproduktion

`coupled_and_instrument.py` importiert keine Forschungsimplementierung. Es erzeugt
`coupled_and_instrument.json`. Der separate Replay führt normale und `-OO`-Läufe
aus und fordert gleiche Ergebnisse; Mutanten für eine falsche Brückennorm und
die Verwechslung konditionierter mit unbedingten Gewichten müssen scheitern.
Exakte rationale Identitäten, analytische Bounds und numerische Gegenprüfungen
sind getrennt gekennzeichnet.
