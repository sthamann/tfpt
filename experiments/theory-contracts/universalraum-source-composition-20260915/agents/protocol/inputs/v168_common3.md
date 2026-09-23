# Derselbe Dreizustandsraum trägt kausalen Eingriff und Zustandstomografie

## Exakte gemeinsame Reduktion

Der ursprüngliche kausale Paarversuch bleibt vollständig im Raum

\[
\mathcal K_3=\operatorname{span}\{|p_0\rangle,|R_7\rangle,|b_0\rangle\},
\quad |p_0\rangle=|4,57\rangle,\quad
|R_7\rangle=\frac1{\sqrt7}\sum_{q=1}^7s_q|p_q\rangle.
\]

Die acht Paare und ihre Vorzeichen stammen unverändert aus Zeile 0 des
eingefrorenen W; sie stehen im zugehörigen `REPORT.md`. Die Isometrie J hat
diese drei Vektoren als Spalten. Direkt aus W folgt

\[
HJ=Jh_3,\qquad Z_4J=Jz_3,\qquad N_bJ=Jb_3,
\]
\[
h_3=\begin{pmatrix}0&0&-g\\0&0&\sqrt7g\\-g&\sqrt7g&\Delta\end{pmatrix},
\quad z_3=\operatorname{diag}(-1,1,1),\quad
b_3=\operatorname{diag}(0,0,1).
\]

Alle drei Intertwining-Identitäten sind exakt und haben keinen Restterm.
Somit haben beliebige Folgen aus freier H-Entwicklung und Z4 denselben
nativen dreidimensionalen Träger. Hier gilt immer N=2.

Die Empfängerbesetzung besitzt den exakten komprimierten **Effekt**

\[
e_3=J^\dagger n_5J=\operatorname{diag}(0,1/7,0).
\]

Damit reproduziert der Dreizustandsraum ohne Näherung beide kausalen
Wahrscheinlichkeiten aus `REPORT.md`: x(4−x)/64 ohne mittleren Impuls und
9x²/1024 mit Impuls. In beiden Armen sind am dort gewählten Endzeitpunkt
Nf=2 und Nb=0.

## Wesentliche Grenze: ein terminaler Effekt ist kein geschlossenes Instrument

n5 selbst erhält diesen Dreizustandsraum nicht. Es gilt exakt

\[
(n_5J-Je_3)^\dagger(n_5J-Je_3)=\operatorname{diag}(0,6/49,0).
\]

Eine tatsächliche nichtselektive projektive n5-Messung lässt vom Zustand R7
das Gewicht **12/49** außerhalb von K3 zurück. Deshalb gilt die gemeinsame
Reduktion für Entwicklungen und Impulse **bis zur abschließenden Messung**.
Eine weitere Verwendung desselben Exemplars nach diesem Instrument wird
nicht behauptet. Die Tomografie verwendet jeweils frische Exemplare desselben
präparierten Zustands und genau eine abschließende Besetzungsmessung.

Ein tatsächlich grobes Lüders-Instrument für den Projektor auf die gesamten
sieben anderen Paarblätter würde K3 erhalten; sein Effekt ist in K3
diag(0,1,0). Das ist eine zusätzliche mögliche Instrumentenanforderung.
Ein feines Auslesen der sieben Blattlabels und anschließendes Wegwerfen der
Labels ist ein anderes Instrument: Es lässt aus R7 das Gewicht 6/7 aus K3
heraustreten. Keine dieser Implementierungen wird als nativ verfügbar
vorausgesetzt, sofern sie nicht ausdrücklich gewährt wird.

## Vollständige terminale Tomografie auf demselben Träger

Definiere für hermitesche Operatoren

\[
\mathcal L(O)=i[h_3,O],\qquad\mathcal C(O)=z_3Oz_3.
\]

Die folgende Liste besitzt neun linear unabhängige hermitesche Operatoren:

\[
\boxed{e_3,b_3,\mathcal Le_3,\mathcal Lb_3,
\mathcal L^2e_3,\mathcal L^2b_3,\mathcal L^3e_3,
\mathcal C\mathcal L^2e_3,\mathcal C\mathcal L^2b_3.}
\]

Schreibt man O als reellen Koordinatenvektor

\[
(O_{00},O_{11},O_{22},\Re O_{01},\Re O_{02},\Re O_{12},
\Im O_{01},\Im O_{02},\Im O_{12}),
\]

hat die Matrix dieser neun Spalten die Determinante

\[
\boxed{\det M=\frac{8\Delta^3g^{10}}{343}\ne0}
\qquad(\Delta g\ne0).
\]

Damit spannt der Orbit aus zeitentwickelten terminalen Effekten und lokaler
Impulskonjugation **Herm(3)** vollständig auf. Der bereits bewiesene kausale
Zeuge und diese Schattenrekonstruktion benutzen denselben ursprünglichen
Tensor, Hamiltonoperator, Träger, Phasenimpuls und dieselben
Besetzungsobservablen. Es handelt sich um Zustandstomografie bei bekanntem
H und bekannten Instrumenten, nicht um eine gleichzeitige unbekannte
Hamilton- und Instrumentenkalibrierung.

Die Operatorwörter sind durch Ableitungen von wirklichen Endwahrscheinlichkeiten
zugänglich: \(\partial_t^k p_e(0)=\operatorname{tr}(\rho\mathcal L^ke_3)\).
Für die beiden letzten Wörter wird Z4 **vor** der freien Entwicklung
angewandt; \(p_e^Z(t)=\operatorname{tr}(\rho z_3e^{ith_3}e_3e^{-ith_3}z_3)\).
Die zugehörige zweite Ableitung liefert das verlangte Wort. Es genügt also
der Zugriff auf die Kurven von n5 und Nb mit und ohne anfänglichen Impuls,
mit Ableitungen bis zur Ordnung drei. Die vollständige Bestimmung dieser
Ableitungen wird als Messdatenanforderung benannt; ein optimiertes endliches
Abtast- und Schätzverfahren wird hier nicht behauptet.

### Der Impuls ist für normierte Zustandstomografie nicht zwingend

Die rein autonome Zeitfamilie aus e3 und b3 besitzt Dimension acht. Ihre
einzige fehlende hermitesche Richtung kann durch

\[
Q=\begin{pmatrix}6\Delta&\sqrt7\Delta&-g\\
\sqrt7\Delta&0&\sqrt7g\\-g&\sqrt7g&0\end{pmatrix}
\]

dargestellt werden: \([h_3,Q]=0\), \(\operatorname{tr}(e_3Q)=
\operatorname{tr}(b_3Q)=0\), aber \(\operatorname{tr}Q=6\Delta\ne0\).
Für die Differenz zweier normierter Zustände ist diese Richtung daher
ausgeschlossen. Tatsächlich bilden

\[
I,e_3,b_3,\mathcal Le_3,\mathcal Lb_3,\mathcal L^2e_3,
\mathcal L^2b_3,\mathcal L^3e_3,\mathcal L^4e_3
\]

ebenfalls eine Basis; ihre Determinante ist 6Δ³g¹⁰/343. Der bekannte Wert
Trρ=1 ersetzt somit eine weitere Messrichtung. Der Impuls erlaubt hier eine
konkrete Basis mit Ableitungen nur bis Ordnung drei; aus Rang acht allein
folgt kein Tomografiehindernis für normierte Zustände.

## Bedingte Fehlergrenze

Verwende dimensionslose Zeit u=Δt und den Prüfpunkt g/Δ=1/20. Sei y der
Vektor der neun oben angegebenen Operatorerwartungswerte und δy sein Fehler.
Der exakte lineare Inversenrechner liefert mit der Frobenius-Normschranke

\[
\|\widehat\rho-\rho\|_{\mathrm{HS}}
\le\frac{\sqrt{9818033}}2\|\delta y\|_2,
\]
\[
\frac12\|\widehat\rho-\rho\|_1
\le\frac{\sqrt{29454099}}4\|\delta y\|_2.
\]

Sind alle neun Dateneinträge mit Fehler höchstens ε bekannt, gilt für die
zweite Schranke 3√29454099·ε/4. Diese konservative Schranke belegt Stabilität
für die ausdrücklich gegebenen Daten, aber auch eine mögliche starke
Fehlerverstärkung bei schwacher Kopplung. Sie enthält **keine** kostenlose
Gewinnung genauer Zeitableitungen aus endlich vielen verrauschten Messungen.
Messdauer, Anzahl frischer Exemplare, Ableitungsschätzung und mögliche
Verbesserungen der Messauswahl bleiben eigene Ressourcenfragen.

## Beweisumfang

`verify_common3.py` prüft den eingefrorenen W, die Isometrie, alle
Intertwining-Identitäten, den ausdrücklichen n5-Leckterm, die zwei
kausalen Endwahrscheinlichkeiten, beide symbolischen Determinanten und die
rationale Inversen-Normschranke. `common3.json` und `common3_OO.json` sind
die normalen und optimierten Replays. Der frühere Bericht und Prüfer wurden
nicht geändert.

Geschlossen ist eine **gemeinsame bedingte Ausführung**: Zustandsrekonstruktion
und kausaler Eingriff im gleichen nativen N=2-Träger. Offen bleiben die
native Auswahl und Präparation der Zustände, ausführbare Modenkontrolle,
kalibrierte terminale Instrumente und die Ressourcen ihrer Wiederholung.
Es folgt keine vollständige Instrumentenalgebra nach Messung, keine
N=64-Grundzustands-/Polidentifikation und keine räumliche Interpretation.
