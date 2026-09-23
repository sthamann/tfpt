**TFPT: ausführbare Ω-Präparation und ein vorab festgelegter Mehrzeittest**

14. September 2026 · Anschluss an die Universalraum-Rekonstruktion

**Ergebnis und Reichweite.** Es liegt jetzt eine konkrete, in exakter Arithmetik geprüfte Quantenschaltung vor. Sie präpariert aus einem Stabilizer-Eingang mit Erfolgsanzeige den Vierträgerzustand Ω. Dieselbe kontrollierte Vertauschung, die in dieser Präparation verwendet wird, erzeugt anschließend eine binäre Aufzeichnung. Zwei Aufzeichnungen mit demselben kohärenten Pointer ergeben einen Rückkehrwert von 1; zwei Aufzeichnungen mit frischen Pointern ergeben 17/32. Die vollständigen Rohwahrscheinlichkeiten einschließlich fehlgeschlagener Präparation und Endauslese sind berechnet.

Die Herkunft der benötigten physikalischen Kontrolle ist damit noch nicht aus der primitiven TFPT-Quelle bewiesen. Der Versuch hat diese Lücke genauer bestimmt: Die Pauli-Objekte der Quelle bestimmen den Operator der Wechselwirkung, liefern aber bislang keine Ableitung seiner physikalischen Verfügbarkeit, der Präparation der Hilfssysteme und der gewählten Registerausführung. Der Schaltungsnachweis ist positiv; die Behauptung einer vollständig quellenabgeleiteten Physik bleibt offen. Auf Hardware wurde nichts ausgeführt.

**1. Was aus der Quelle übernommen und neu geprüft wurde**

Verwendet wurden die tatsächlichen 60 Projektoren und 15 nichttrivialen Pauli-Richtungen aus dem vorhandenen v783-Quelladapter. Alle vier beteiligten Quelldateien sind durch SHA-256 festgelegt; das Reproduktionspaket enthält diese Fassungen. Der Pauli-Bezug wird nicht durch beliebig erzeugte Ersatzmatrizen hergestellt.

Für zwei vierdimensionale Träger wurde exakt geprüft:

\[
S_{ij}=\frac14\sum_{v=0}^{15}P_v^{(i)}\otimes P_v^{(j)},\qquad P_0=I_4.
\]

\(S_{ij}\) vertauscht die beiden Träger. Auf vier Trägern lautet der vollständig antisymmetrische Zustand

\[
|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}
\operatorname{sgn}(\pi)|\pi(0)\pi(1)\pi(2)\pi(3)\rangle.
\]

Mit \(A_4=|\Omega\rangle\langle\Omega|\) gilt

\[
A_4=\frac1{24}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)U_\pi.
\]

Die vollständige 256×256-Matrixidentität wurde geprüft, nicht nur ihre Wirkung auf einen günstigen Eingang. Der Filter ist ein Projektor von Rang eins. Sein Bild stimmt exakt mit dem Ω des vorhandenen Tetramer-Prüfers überein und wird vom dortigen Hamiltonoperator annihiliert.

Die Existenz von Ω, seine sechs verschwindenden symmetrischen Paarenergien und sein Nicht-Stabilizer-Status sind bereits in den vorhandenen Erweiterungsarbeiten angelegt. Neu ist hier die konkrete Präparationsschaltung samt Ressourcenzerlegung, ausführbarer Auslese und festgeschriebenem Mehrzeitvergleich.

**2. Warum die bisherige Struktur Ω nicht von selbst präpariert**

Auf Ω wirkt jede Trägervertauschung mit Vorzeichen −1. Daher gilt

\[
[S_{ij},A_4]=0.
\]

Für eine beliebige zeitabhängige Austauschdynamik

\[
H(t)=\sum_{i<j}J_{ij}(t)S_{ij}
\]

bleibt \(\operatorname{Tr}(A_4\rho)\) erhalten. Auch kollektive SU(4)-Transformationen ändern diesen Anteil nicht. Ein Grundzustandsnachweis ist deshalb kein Kühlungs- oder Präparationsmechanismus. Diese Aussage betrifft die angegebene Austausch- und Kollektivklasse; beliebige zusätzliche lokale Steuerungen sind darin nicht enthalten.

Eine zweite Grenze betrifft den Stabilizer-Baukasten. Die Paarmarginale von Ω ist

\[
\rho_{ij}=\frac{I_{16}-S_{ij}}{12}.
\]

Für einen nichttrivialen hermiteschen Ququart-Pauli \(P\) ergibt sich

\[
\langle P^{(i)}\otimes P^{(j)}\rangle_\Omega
=\frac{(\operatorname{Tr}P)^2-\operatorname{Tr}(P^2)}{12}
=-\frac13.
\]

Ein reiner Qubit-Stabilizer-Zustand hat für Pauli-Observablen ausschließlich die Erwartungswerte 0, +1 oder −1. Ω liegt damit außerhalb dieser Klasse in der hier verwendeten Kodierung von vier Ququarts als acht Qubits. Clifford-Gatter, Stabilizer-Hilfszustände und Pauli-Messungen können Ω auch mit Auswahl einzelner Messzweige nicht exakt aus einem Stabilizer-Eingang erzeugen. Die zusätzlich benötigte Ressource darf folglich nicht in einer abstrakt hingeschriebenen Projektionsmessung versteckt werden.

**3. Eine genau angegebene zusätzliche Wechselwirkung**

Wir ergänzen einen binären Pointer R und die kohärent kontrollierte Trägervertauschung

\[
F_{R;ij}=|0\rangle\langle0|_R\otimes I
+|1\rangle\langle1|_R\otimes S_{ij}.
\]

Ein konkreter Hamiltonoperator dafür ist

\[
H_{\mathrm{int}}=\hbar g\,|1\rangle\langle1|_R\otimes P_{ij}^-,
\qquad P_{ij}^-=\frac{I-S_{ij}}2.
\]

Bei \(g\tau=\pi\) gilt exakt

\[
e^{-i\tau H_{\mathrm{int}}/\hbar}=F_{R;ij}.
\]

Der Beweis ist endlich: \(G=|1\rangle\langle1|\otimes P^-\) ist ein hermitescher Projektor. Deshalb ist \(e^{-i\pi G}=I-2G\), und dieser Operator ist die kontrollierte Vertauschung. Projektoreigenschaft und Matrixgleichheit wurden exakt geprüft.

Auch der vollständige Generator lässt sich in den konkreten Quell-Paulis ausdrücken:

\[
G=\frac3{16}(I-Z_R)\otimes I_{16}
-\frac1{16}\sum_{v=1}^{15}I_R\otimes P_v\otimes P_v
+\frac1{16}\sum_{v=1}^{15}Z_R\otimes P_v\otimes P_v.
\]

Die darin vorkommenden Pauli-Terme kommutieren paarweise. Die Gleichung ist eine exakte algebraische Darstellung einer möglichen Kopplung. Sie leitet weder deren physische Erzeugung noch ihre Stärke oder zeitliche Steuerbarkeit aus der Quelle ab. Insbesondere verlangt die kontrollierte Kopplung Zugriff auf Pointer und zwei Träger gemeinsam.

Als Gatterfolge ist die Wechselwirkung vollständig aufgelöst. Eine kontrollierte Vertauschung zweier Qubits entsteht durch

\[
\mathrm{CX}(a,b);\quad\mathrm{CCX}(R,b,a);\quad\mathrm{CX}(a,b).
\]

Zwei solcher Fredkin-Schaltungen vertauschen zwei Ququarts kontrolliert. Die Wahrheitstabelle wurde vollständig geprüft. Eine kohärent kontrollierte Vertauschung ist nicht allein deshalb Clifford, weil die unkontrollierte Vertauschung Clifford ist. Ihre Basiswirkung ist nicht affin; dies liefert hier einen direkten Nicht-Clifford-Zeugen. Diese Zerlegung entspricht auch der dokumentierten kontrollierten Vertauschung in [Google Cirq](https://quantumai.google/cirq/experiments/unitary/quantum_chess/concepts).

Die Toffoli-Gatter wurden zusätzlich in Clifford- und T-Gatter zerlegt. Verwendet wird

\[
T=\operatorname{diag}(1,e^{i\pi/4})
\]

und eine explizite Zerlegung mit sieben T- beziehungsweise T†-Gattern. Ihre vollständige komplexe 8×8-Matrix wurde symbolisch geprüft, einschließlich aller Phasen. Sieben ist hier die gewählte Kostenobergrenze dieser Zerlegung; es wird keine globale Ressourcenminimalität behauptet. Andere Konstruktionen mit anderen Hilfsmitteln können günstiger sein, siehe [Jones, Novel constructions for the fault-tolerant Toffoli gate](https://arxiv.org/abs/1212.5069).

Damit ist eine hinreichende Ressource außerhalb des Stabilizer-Baukastens präzisiert: Zugang zu T-Gattern oder entsprechenden nichtstabilisierenden Hilfszuständen. Beispielsweise kann \(|T\rangle=(|0\rangle+e^{i\pi/4}|1\rangle)/\sqrt2\) über Clifford-Kopplung, Messung und bedingte Korrektur ein T-Gatter bereitstellen. Die Rolle solcher zusätzlicher Zustände ist in [Bravyi und Kitaev, Universal Quantum Computation with ideal Clifford gates and noisy ancillas](https://arxiv.org/abs/quant-ph/0403025) begründet. Die vorliegenden TFPT-Daten liefern bislang keine physische Quelle dieses Hilfszustands oder eines gleichwertigen Nicht-Clifford-Pulses.

Eine zweite, elementare Hamilton-Realisierung des ganzen Gatterbaukastens wäre adressierbare Pauli-Evolution: \(H_Z=\hbar\omega Z/2\) mit Pulsfläche \(\omega\tau=\pi/4\) erzeugt T bis auf eine globale Phase. Mit den angenommenen Clifford-Steuerungen ergibt die nachgewiesene Zerlegung dann Toffoli und die kontrollierten Vertauschungen. Der zusätzliche Inhalt liegt im Zugang zu dieser Nicht-Clifford-Pulsfläche; aus dem Vorhandensein einer Pauli-Matrix oder einer endlichen Clifford-Symmetrie folgt dieser Zugang nicht. Dies ist eine ausdrücklich angegebene physikalische Ergänzung, keine aus der Quelle gewonnene neue Naturkonstante.

Auch mehrere adressierbare Kopien, die gewählte Qubit-Zerlegung, trägereigene und trägerübergreifende Clifford-Kopplungen, Nullzustandspräparation, Messung und Reset sind Voraussetzungen der Schaltung. Der angegebene kontrollierte Austauschoperator allein auf fest verdrahteten Ports beweist noch nicht die Steuerbarkeit aller Hilfsqubits. Die 20-Qubit-Ressourcenangabe gilt für den ausgewiesenen adressierbaren Clifford+Toffoli- beziehungsweise Clifford+T-Baukasten.

**4. Ω wird aus einer Gatterfolge präpariert**

Der Eingang ist

\[
|\chi_0\rangle=
\frac{|01\rangle-|10\rangle}{\sqrt2}
\otimes\frac{|23\rangle-|32\rangle}{\sqrt2}.
\]

Er wird aus dem Nullzustand ausschließlich durch X-, H-, Z- und CNOT-Gatter aufgebaut. Sein Ω-Anteil beträgt genau \(1/6\). Der Prüfer verwendet weder Ω als Initialzustand noch \(A_4\) als eingebautes Präparationsgatter.

Fünf Hilfsqubits erzeugen 32 gleichgewichtete Kontrollzweige. Die ersten 24 kodieren die lexikographisch geordneten Permutationen von vier Trägern. Jeder gültige Zweig führt die betreffende Trägerpermutation aus und erhält ihr Vorzeichen. Acht übrige Zweige werden mit einem Gültigkeitsbit markiert. Vier weitere Hilfsqubits berechnen die Kontrollbedingungen reversibel und werden wieder auf null gebracht.

Nach Interferenz der Kontrollzweige wird nur das Ergebnis „Kontrollbits null und Gültigkeitsbit null“ angenommen. Der tatsächlich implementierte Erfolgsoperator ist

\[
K_{\mathrm{prep}}=\frac1{32}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)U_\pi
=\frac34 A_4.
\]

Diese Identität wurde zusätzlich auf allen 256 Eingangsbasiszuständen durch Ausführung der einzelnen Gatter geprüft. Sie folgt nicht nur aus dem Namen „Antisymmetrisierer“.

Für den angegebenen Eingang gilt

\[
p_{\mathrm{prep}}=\|K_{\mathrm{prep}}\chi_0\|^2
=\frac9{16}\frac16=\frac3{32}=9{,}375\%.
\]

Der angenommene Zustand ist exakt Ω. Vor Normierung stehen auf den 24 Permutationsbasiszuständen die Amplituden ±1/16. Alle sechs symmetrischen Paarenergien verschwinden exakt. Die übrige Wahrscheinlichkeit \(29/32\) gehört zu verworfenen Versuchen. Der gültige Permutationsbereich hat vorher Wahrscheinlichkeit \(3/4\); bedingt darauf gelingt die Interferenzauswahl mit \(1/8\).

Dies ist eine Präparation mit erkennbarem Erfolg. Bei unabhängigen Wiederholungen mit jeweils neuem Eingang benötigt sie im Mittel \(32/3\) Versuche. Die Auswahl erhöht den bedingten Ω-Anteil; sie widerspricht nicht der Erhaltung des unbedingten Anteils durch reine Austauschunitaritäten. Ein deterministischer Relaxationsmechanismus ist damit nicht behauptet.

**5. Dieselbe Wechselwirkung schreibt den Speicher**

Für die Paarvertauschung \(S=S_{01}\) wird

\[
V=H_R F_{R;01}H_R
\]

verwendet. Mit \(P_\pm=(I\pm S)/2\) gilt

\[
V(|0\rangle_R\otimes|\psi\rangle)
=|0\rangle_R\otimes P_+|\psi\rangle
+|1\rangle_R\otimes P_-|\psi\rangle.
\]

Der Pointer zeichnet die symmetrische oder antisymmetrische Paarkomponente auf. \(V^2=I\) wurde auf dem gesamten 32-dimensionalen Raum aus Pointer und Trägerpaar geprüft. Wird ein frisch benutzter Pointer ignoriert, lautet der reduzierte Kanal

\[
\Delta_S(\rho)=P_+\rho P_++P_-\rho P_-
=\frac12(\rho+S\rho S).
\]

Dieser Kanal ist idempotent: \(\Delta_S^2=\Delta_S\). Die kohärente Rückkopplung an denselben Pointer und die zweimalige Nutzung frischer Pointer sind deshalb unterschiedliche Mehrzeitausführungen desselben ersten reduzierten Schrittes.

Hier wird eine neue binäre Swap-Aufzeichnung untersucht. Sie ist nicht identisch mit dem bisherigen 15-Kontext-Kanal mit Dämpfungsfaktor 3/7. Der vorliegende Wert 17/32 gehört zum hier festgelegten Protokoll.

**6. Der vor der Simulation festgelegte Eingriff und Messwert**

Ω allein wäre für diesen Vergleich ungeeignet: Es ist bereits Eigenzustand jedes Swaps. Deshalb wird vor der Aufzeichnung auf Träger 0 der lokale Tick

\[
c=\mathrm{CNOT}_{12}\mathrm{CNOT}_{21},\qquad
0\mapsto0,\;1\mapsto2,\;2\mapsto3,\;3\mapsto1
\]

angewendet. Es gilt \(c^3=I\) und \(\operatorname{Tr}c=1\). Zusätzlich wurde geprüft, dass c die tatsächlichen 60 Quellprojektoren permutiert. Die Wahl dieses Eingriffs wurde vor dem neuen Prüflauf festgeschrieben.

Danach folgt:

1. Zwei Anwendungen von V, entweder mit demselben kohärenten Pointer oder mit zwei frischen Pointern.
2. Keine Messung zwischen diesen beiden Anwendungen im Hauptvergleich.
3. Rücknahme des lokalen Ticks durch \(c^{-1}\).
4. Endauslese mit genau derselben kompilierten S4-Filterschaltung wie bei der Präparation.

Der primäre Rückkehrwert ist

\[
F=\operatorname{Tr}(A_4\rho_{\mathrm{nach\ Rücknahme}}).
\]

Dies ist eine bedingte Zustandsstatistik nach erfolgreicher Eingangspräparation. Ihre tatsächlich ausgeführte Endmessung hat den Effekt

\[
K_{\mathrm{prep}}^\dagger K_{\mathrm{prep}}=\frac9{16}A_4.
\]

Die beobachtbare Endfilter-Erfolgswahrscheinlichkeit ist deshalb \((9/16)F\), nicht F selbst. Diese Kalibrierung wird in der Rechnung und den Rohwahrscheinlichkeiten berücksichtigt.

**7. Ableitung des Werts 17/32**

Sei \(|\chi\rangle=(c\otimes I\otimes I\otimes I)|\Omega\rangle\). Aus der Paarmarginale folgt

\[
\langle\chi|S_{01}|\chi\rangle
=\frac{4-|\operatorname{Tr}c|^2}{12}=\frac14.
\]

Somit sind die beiden aufgezeichneten Gewichte

\[
p_+=\frac58,\qquad p_-=\frac38.
\]

Bei einem frischen Pointer beträgt der Rückkehrwert

\[
F_{\mathrm{frisch}}=p_+^2+p_-^2
=\frac{25+9}{64}=\frac{17}{32}.
\]

Ein zweiter frischer Pointer ändert den bereits dephasierten Systemzustand nicht. Beim kohärent behaltenen Pointer hebt die zweite Anwendung die erste vollständig auf, weil \(V^2=I\). Daher gilt

\[
F_{\mathrm{behalten}}=1,\qquad
F_{\mathrm{behalten}}-F_{\mathrm{frisch}}=\frac{15}{32}.
\]

Die exakte Gatterausführung bestätigt diese unabhängig hergeleiteten rationalen Werte.

| Statistik nach zwei Aufzeichnungen | Kohärent behalten | Zwei frische Pointer |
|---|---:|---:|
| Ω-Rückkehrwert nach erfolgreicher Präparation | 1 | 17/32 = 53,125 % |
| Endfilter-Erfolg, bedingt auf Präparation | 9/16 = 56,25 % | 153/512 = 29,8828125 % |
| Präparation und Endfilter erfolgreich, pro begonnenem Versuch | 27/512 = 5,2734375 % | 459/16384 = 2,801513671875 % |
| Alle übrigen Versuchsausgänge zusammen | 485/512 | 15925/16384 |

Die beiden letzten Zeilen summieren sich in jeder Ausführung zu eins. Ein Unterschied darf nicht durch das Weglassen fehlgeschlagener Versuche vergrößert werden.

Nach einer Aufzeichnung stimmen beide Ausführungen überein. Für beliebig viele Wiederholungen folgt aus den beiden Operatoridentitäten:

\[
F_n^{\mathrm{behalten}}=
\begin{cases}1,&n\text{ gerade},\\17/32,&n\text{ ungerade},\end{cases}
\qquad
F_n^{\mathrm{frisch}}=
\begin{cases}1,&n=0,\\17/32,&n\ge1.\end{cases}
\]

Die Fälle n=0 bis 6 wurden zusätzlich direkt ausgeführt. Sämtliche einzelnen Träger haben vor, zwischen und nach den Aufzeichnungen weiterhin die Marginale \(I_4/4\). Die Unterscheidung steckt in den zugänglichen Korrelationen und ihrer Fortsetzung. Unveränderte Einträgermarginalien bedeuten folglich keine operationelle Gleichheit der beiden Prozesse.

**8. Kontrollen und technische Gegenprüfungen**

Ohne lokalen Tick liefern beide Ausführungen F=1. Vollständige Pointer-Dephasierung zwischen den zwei Anwendungen zerstört das kohärente Echo und liefert F=17/32. Bei verbleibender Pointer-Kohärenz η, modelliert durch I mit Gewicht \((1+\eta)/2\) und Z mit Gewicht \((1-\eta)/2\), lautet die ebenfalls vorab festgelegte Kurve

\[
F(\eta)=\frac{17+15\eta}{32},\qquad0\le\eta\le1.
\]

Der reine Z-Zweig ergibt F=1/16. Die fünf vorab gewählten η-Werte 0, 1/4, 1/2, 3/4 und 1 stimmen exakt mit der Formel überein. η ist hier der Parameter eines vorgegebenen Dephasierungsmodells; es wurden keine Messdaten daran angepasst.

Die Gegenprüfungen ändern tatsächlich Bestandteile der Ausführung: Ohne Permutationsvorzeichen hat der Eingang im angenommenen Filterzweig Wahrscheinlichkeit null. Ohne Aufzeichnungs-Swaps verschwindet der Hauptkontrast. Ein fälschlich wiederverwendeter zweiter Pointer verletzt die Frisch-Pointer-Vorhersage. Die letzten beiden Änderungen werden durch dieselbe Akzeptanzfunktion zurückgewiesen, die den Hauptvergleich bewertet. Ein absichtlich falscher Quellhash wird durch den tatsächlichen Quellschutz zurückgewiesen.

Der abschließende Prüfer besteht 598 benannte Prüfungen. Das schließt vollständige Operatorprüfungen und Schleifen über alle Basiszustände ein; die Zahl allein ist kein Physiknachweis. Die Hauptrechnung verwendet ganzzahlige Amplituden mit expliziten Zweierpotenzen und exakte rationale Wahrscheinlichkeiten. Symbolische komplexe Matrizen prüfen die T-Zerlegung. Akzeptanz hängt nicht von deaktivierbaren Python-Assertions ab.

Die normale Ausführung und die Ausführung mit `-OO` lieferten byteidentische Ergebnisdateien und byteidentische Schaltungen in beiden Gatterbasen. Auch ein weiterer Lauf ausschließlich mit den im Reproduktionspaket enthaltenen Quellen lieferte dieselben Dateien; er benötigt den ursprünglichen Repository-Pfad nicht.

Die exportierten Hauptschaltungen wurden aus ihren OpenQASM-Gatterzeilen erneut ausgeführt und reproduzieren die absoluten gemeinsamen Erfolgswahrscheinlichkeiten. Die vollständig in Clifford+T aufgelösten Varianten sind durch die exakte lokale Toffoli-Matrixidentität und deren kontrollierte Ersetzung zertifiziert; sie wurden nicht zusätzlich als vollständige komplexe 20-Qubit-Zustandsvektoren simuliert.

**9. Ressourcen und Reproduktion**

Eine vollständige Ausführung einschließlich Eingangs- und Endfilter verwendet in der vorliegenden, nicht optimierten Fassung:

| Ressource | Anzahl |
|---|---:|
| Systemqubits für vier Ququarts | 8 |
| Filter-Hilfsqubits, wiederverwendet | 10 |
| Pointerplätze für beide Ausführungsarten | 2 |
| Insgesamt reservierte Qubits | 20 |
| Klassische Erfolgsbits beider Filter | 12 |
| Toffoli-Gatter | 574 |
| Weitere CNOT-Gatter vor Toffoli-Auflösung | 382 |
| H-Gatter vor Toffoli-Auflösung | 26 |
| X-Gatter | 276 |
| Z-Gatter | 26 |
| T/T†-Gatter bei der mitgelieferten Siebener-Zerlegung | 4018 |

Ein einzelner S4-Filter verwendet 285 Toffoli-Gatter. Die Kosten sind eine obere Schranke dieser transparenten Konstruktion; Routing, Fehlerkorrektur, Hilfszustandsherstellung, Laufzeit und reale Pulsfehler sind darin nicht enthalten. Ein physikalischer Hardwareplan müsste diese Größen separat bestimmen.

Das Reproduktionspaket enthält den Prüfer, die festgelegte Vorhersage, die Quellhashes, die nötigen eingefrorenen Quelldateien, Ergebnisse sowie beide OpenQASM-Varianten in beiden Gatterbasen. Benötigt werden Python, NumPy und SymPy. Im entpackten Verzeichnis startet `python3 -B omega_protocol.py` den Prüfer. Die Ausgabe aktualisiert die Ergebnisdatei und die Schaltungen. Die enthaltenen Quelldateien werden dabei gelesen, nicht verändert.

Die Vorhersagedatei wurde am 14. September 2026 um 05:51:45 UTC eingefroren, bevor der neue Schaltungsprüfer ausgeführt wurde. Ihr SHA-256 lautet `2227f0e4e5b384eac536af1bc6b32c10c345158532c1b072736c4bead88ad757`. Das ist ein interner vorab festgelegter Simulationsvertrag mit analytischen Zielwerten, keine externe Studienregistrierung und keine verblindete experimentelle Prognose. Die Hashes der Quelladapter stehen vollständig im Paket.

**10. Was dieser Anschluss für den Universalraum entscheidet**

Die Konstruktion schließt eine konkrete Lücke zwischen abstrakter Zustandsdefinition und endlicher Operation: Aus einem einfachen Eingang entsteht durch eine explizite Folge kontrollierter Veränderungen ein überprüfbar angenommener Ω-Zustand. Dieselbe Art von Veränderung erzeugt anschließend eine experimentell unterscheidbare Mehrzeitstruktur. In diesem bedingten Modell sind Präparation, Aufzeichnung und Endauslese miteinander verbunden.

Zugleich ergibt sich eine präzise Unterbestimmtheit. Die primitive algebraische Quelle allein wählt den neuen Kopplungszugriff nicht aus. Selbst nach Hinzunahme derselben Wechselwirkung wählen ihre Matrizen allein nicht aus, ob ein Pointer kohärent erhalten bleibt, dephasiert wird oder durch einen frischen ersetzt wird. Diese Möglichkeiten stimmen nach dem ersten reduzierten Schritt überein und sagen später verschiedene Resultate voraus. Das ist ein konkretes Hindernis für eine eindeutige Rekonstruktion allein aus dem bisherigen Schatten.

Die Zahlen 1 und 17/32 sind daher Vorhersagen zweier expliziter Ergänzungen der Quelle. Sie sind keine bereits aus TFPT allein erzwungene Naturvorhersage. Die Messung dieses Echos würde die angegebenen Registerausführungen unterscheiden; andere Modelle können dieselbe endliche Statistik reproduzieren. Ein vollständiger Universalraum folgt aus diesem einen Zeugen noch nicht.

Die nächste Herkunftsforderung ist nun scharf formulierbar: Ein Kandidat für den fundamentalen Prozess muss die kontrollierte Kopplung oder eine nachweislich gleichwertige Nicht-Stabilizer-Ressource, die Bereitstellung und Auslese der Hilfssysteme sowie die tatsächlich erhaltenen Registerfreiheitsgrade aus seinen eigenen zulässigen Vorgängen herleiten. Er muss damit die vorliegenden Rohwahrscheinlichkeiten ohne nachträgliche Wahl der Registerausführung bestimmen. Bis dahin steht eine reproduzierbare, endliche Ausführung mit offen ausgewiesener Ergänzung zur Verfügung; eine allesumfassende physikalische Schließung wird nicht behauptet.
