---
title: "TFPT / Universalraum: eine gemeinsame Quelle auf dem Prüfstand"
subtitle: "Überlappende Paarquellen, geschützter Transport und die verbleibende Auswahlfrage"
author: "Forschungsfortsetzung mit eigenen Herleitungen · erstellt mit Codex"
date: "15. September 2026 · Fortsetzung 1.2"
lang: de-DE
---

# Zusammenfassung

Diese Arbeit führt den vereinbarten Weg aus: Ausgangsdaten festlegen, eine begrenzte Klasse gemeinsamer Quellen konstruieren, ihre Eindeutigkeit prüfen, einen unbedingten Wirkungstest rechnen und die Größenfolge untersuchen. Sie verwendet den ursprünglichen TFPT-Paartensor W, ergänzt jedoch ausdrücklich eine **Kompositionsregel**. Diese zusätzliche Regel wird untersucht und nicht als bereits aus TFPT hergeleitet ausgegeben.

Der positive Befund ist eine gemeinsame, ladungserhaltende kubische Dynamik auf überlappenden Fermionquellen und unabhängigen Bosonbereichen. Ein direkter quadratischer Sprung zwischen den Bosonbereichen ist nicht eingesetzt. Ihre Wechselwirkung folgt innerhalb des Kandidaten aus zwei ursprünglichen Paarvertizes. Im minimalen untersuchten Dreieck trägt derselbe globale Hamiltonoperator einen invarianten 90-dimensionalen Unterraum mit einem geschützten logischen Faktor der Dimension 15. Die logische Information kann sich zwischen Bosonbereichen bewegen und bleibt bei einer bekannten einzelnen Fermionmodenlöschung korrigierbar. Alle 192 ursprünglichen Fermionmoden des Dreiecks wurden dafür einschließlich der CAR-Vorzeichen exakt geprüft.

Ein unbedingter Interventionsvergleich liefert am festgelegten Prüfpunkt eine positive Änderung der Empfängerwahrscheinlichkeit von etwa 0,003014206, also 0,301421 Prozentpunkten. Die beiden Läufe verwenden denselben Eingang und dieselbe Dynamik. Der Unterschied ist ein zusätzlich gewährter lokaler Phaseneingriff. Ein exakter Symmetrie- und Algebraausschluss zeigt zugleich, dass dieser Eingriff aus den bisher gegebenen globalen Kontrollen nicht erzeugt werden kann. Ein aus derselben Quelle abgeleiteter Aktuator und ein dauerhaft auslesbares Messgerät fehlen daher weiterhin.

Die Auswahlfrage wird innerhalb einer klaren Klasse negativ entschieden: Petersen-Graph und fünfeckiges Prisma erfüllen dieselben Anforderungen an Größe, Grad, Zusammenhang, Gleichwertigkeit der Knoten und vollständige Nutzung der Fermionkopien. Dennoch unterscheiden sie sich in einer neutralen Antwortgröße. Ferner können zwei verschiedene Quellphasen dieselbe vollständige bosonische N=2-Antwort besitzen und zugleich verschiedene ungenutzte Fermionrichtungen hinterlassen. Eine lokale Spektralbeschreibung bestimmt die gemeinsame Quelle somit nicht eindeutig.

Für beliebige fest vorgegebene Netze mit beschränktem Grad wird die N=2-Dynamik auf den Graphen der benachbarten Verbindungen zurückgeführt. Daraus folgen eine kontrollierte Ausbreitungsschranke und ein mathematisch wohldefinierter Grenzwert auf unendlichen Netzen. Dies beweist weder den Grundzustandsgrenzwert des gesamten Fockraums noch Raumdimension, Lorentzsymmetrie oder die physische Auswahl des Netzes.

# 1. Was festgehalten und was ergänzt wurde

## 1.1 Unveränderte lokale Daten

Der Ausgangstensor erfüllt

$$P_A(f)=\sum_{i<j}W_{A,ij}f_jf_i,\qquad WW^\dagger=8I_{60}.$$

Es gibt 64 innere Fermionlabels, 60 innere Bosonlabels und 480 ursprüngliche von null verschiedene Tensorstellen. Die innere Gruppe ist $\mathsf G=\mathrm{Spin}(10)\times SU(4)$. W ist durch den bereits verwendeten SHA-256 gesichert. Seine Kovarianz unter den 60 Lie-Erzeugern wurde in Fortsetzung 1.1 unabhängig geprüft. Die aktuelle Arbeit übernimmt diesen Beleg; die Kovarianz der zusammengesetzten Quelle folgt durch Linearität, da Kopienlabels unter $\mathsf G$ trivial sind.

Als lokale Wechselwirkung bleibt die Paar-Boson-Umwandlung erhalten. Die drei globalen Verpflichtungen sind: Selbstadjungiertheit, Erhaltung von $N=N_f+2N_b$ und Erhaltung der genannten inneren Symmetrie. Die native Wahl einer reellen Kopplung g und einer positiven Bosonenergie $\Delta$ wird beibehalten. Ihre physische Auswahl ist keine Folgerung dieser Arbeit.

## 1.2 Der zusätzliche Vertrag

Es werden mehrere kanonisch unabhängige Fermionkopien $f_{x,i}$ und Bosonbereiche $b_{e,A}$ zugelassen. Welcher Bosonbereich welche Fermionkopien gemeinsam nutzt, wird durch eine explizite Regel angegeben. Das ist eine neue globale Modellwahl.

| Bestandteil | Status |
|---|---|
| Ursprünglicher Tensor W und innere Darstellungen | Aus der vorherigen Quelle übernommen und gepinnt |
| Mehrere unabhängige Fermionkopien und Bosonbereiche | Zusätzlicher Kompositionsvertrag |
| Gleichgewichtete gemeinsame Nutzung zweier Fermionkopien | Gewählte, überprüfbare Kandidatenregel |
| Netz und gegebenenfalls Quellphasen | Zusätzliche Daten; ihre Auswahl wird geprüft |
| Native kubische Dynamik auf diesem Träger | Aus den genannten Daten exakt konstruiert |
| Eingang im Sektor N=2 | Gewählter Prüfzustand, kein hergeleiteter globaler Grundzustand |
| Gezielter Phaseneingriff und abschließende Zeigerauslesung | Im Wirkungstest gewährte Instrumente |

Die große Grundzustandsaussage für die ursprüngliche einzelne Bank wird **nicht auf das neue globale Modell übertragen**. Insbesondere sind die nachfolgenden Rechnungen keine Rechnung auf dessen noch unbekanntem physischem Grundzustand.

# 2. Die Klasse gemeinsamer Quellen

## 2.1 Freie Kopienstruktur im festgehaltenen W-Kanal

Mit Kopienlabels x,y kann der festgehaltene Paarkanal durch symmetrische Matrizen $C_e$ kombiniert werden. Schreibt man $A^A$ für die antisymmetrische Matrix des ursprünglichen W-Kanals, ist der globale Fermionpaartensor

$$M_e^A=C_e\otimes A^A,\qquad C_e^T=C_e.$$

Die Symmetrie von $C_e$ sorgt dafür, dass $M_e^A$ antisymmetrisch bleibt. In dieser ausdrücklich eingeschränkten Klasse kann man also viele globale kubische Modelle bauen, ohne den inneren Tensor zu verändern. Innere Symmetrie und Ladungserhaltung legen die Matrizen $C_e$ nicht fest. Weitere erlaubte Polynomialkanäle oder zusätzliche quadratische Kopplungen werden hier nicht mitklassifiziert.

## 2.2 Ein besonders einfacher Kandidat

Wähle einen einfachen ungerichteten Graphen. Seine Knoten x tragen unabhängige Fermionkopien, seine Kanten e unabhängige Bosonbereiche. Für $e=\{x,y\}$ setze

$$q_{e,i}=\frac{f_{x,i}+f_{y,i}}{\sqrt2},\qquad
P_{e,A}=P_A(q_e).$$

Für jedes einzelne e sind die $q_{e,i}$ kanonische Fermionen. Bei benachbarten Kanten sind sie jedoch **keine unabhängigen Kopien**:

$$\{q_{e,i},q_{f,j}^\dagger\}=s_{ef}\delta_{ij},\qquad
s_{ef}=\begin{cases}1&e=f,\\1/2&e,f\text{ teilen einen Knoten},\\0&\text{sonst}.\end{cases}$$

Die gemeinsame Dynamik lautet

$$\boxed{H_G=\Delta\sum_{e,A}b_{e,A}^\dagger b_{e,A}
+g\sum_{e,A}\big(b_{e,A}^\dagger P_{e,A}+P_{e,A}^\dagger b_{e,A}\big).}$$

Ausgeschrieben enthält $P_A(q_e)$ ursprüngliche Paare innerhalb beider Knoten sowie gemischte Paare zwischen ihnen, mit den durch W bestimmten Vorzeichen. Es wird kein zusätzlicher Term $b_e^\dagger b_f$ eingesetzt. Der gesamte Operator erhält die Gesamtladung und die diagonale innere Gruppe.

**Warum dies mehr als eine Umbenennung von überlappenden Ansichten ist:** Die Bosonbereiche e und f sind unabhängige kanonische Moden. Ihre Besetzungsobservablen kommutieren. Die Fermionquellen werden in einem ausdrücklich gemeinsamen Hamiltonoperator gekoppelt. Erst die unten gerechnete Änderung ihrer Statistik weist Wirkung nach; die Überlappung allein wäre dafür kein Beweis.

![Die Kandidatenregel: Jeder Bosonbereich nutzt zwei kanonische Fermionkopien. Im Dreieck überlappen benachbarte Quellen. Der dargestellte Graph ist ein zusätzlicher Modelleingang und noch kein hergeleiteter Raum.](figures/quellregel.pdf)

```{=latex}
\Needspace{10\baselineskip}
```

# 3. Ein versteckter Defekt und der minimale korrigierte Kandidat

## 3.1 Warum die erste Kette nicht vollständig gekoppelt ist

Für drei Knoten und nur zwei Kanten sind die Quellen proportional zu

$$q_0\sim f_0+f_1,\qquad q_1\sim f_1+f_2.$$

Obwohl der sichtbare Graph zusammenhängt, kommt die kanonische Kombination

$$f_{\rm dunkel}=\frac{f_0-f_1+f_2}{\sqrt3}$$

in keinem Vertex vor. Das gilt für jedes der 64 inneren Labels. Ihre Besetzung ist eine zusätzliche erhaltene Größe. Ein Test nur diagonaler Paritäten in der ursprünglichen Knotenbasis hätte diese ungenutzte gesamte Fermionkopie übersehen.

Dies ist ein konkretes Gegenbeispiel zur Gleichsetzung von verbundenem Paargraphen mit vollständiger Nutzung aller linearen Fermionrichtungen.

## 3.2 Das Dreieck

Ergänzt man $q_2\sim f_0+f_2$, spannen die drei Quellvektoren den vollständigen dreidimensionalen Kopienraum. Ihre paarweisen Überlappungen sind nicht null. Für jede innere Komponente wird nun jede lineare Kopienrichtung von den Quellen genutzt.

Ein genauer Ausschluss gilt in der folgenden Klasse: Betrachte eine $\mathsf G$-verträgliche lineare unitäre Fermioninvolution, welche die Bosonen unverändert lässt. Weil jede Paarquelle eine Rang-eins-Matrix $q_eq_e^T$ besitzt, muss die Involution jeden $q_e$ auf $+q_e$ oder $-q_e$ abbilden. Eigenvektoren einer unitären Involution mit verschiedenen Vorzeichen sind orthogonal. Die nichtverschwindenden Überlappungen erzwingen daher dasselbe Vorzeichen für alle drei Quellen. Da sie den Kopienraum aufspannen, bleiben nur $+I$ und $-I$.

Der direkte vollständige Tensor-Replay bestätigt zusätzlich Rang 191 der reinen Modenparitätsbedingungen auf 192 ursprünglichen Fermionmoden. Der lineare Satz ist stärker als dieser Koordinatentest, bleibt aber auf die bezeichneten Transformationen mit unveränderten Bosonen beschränkt.

Innerhalb der gewählten einfachen positiven Zweiknoten-Regel ist das Dreieck der kleinste zusammenhängende Graph, der keinen ungenutzten linearen Fermionkopienraum besitzt. Das ist ein Minimalitätsbefund für den Kandidatenvertrag. Es ist keine Auswahl einer dreieckigen Welt durch TFPT.

# 4. Die vollständige kleine Dynamik

## 4.1 Die gemeinsame Rückwirkung folgt aus W

Im globalen Sektor N=2 gilt

$$\langle0|P_{e,A}P_{f,B}^\dagger|0\rangle
=8s_{ef}^{\,2}\delta_{AB}.$$

Für komplexe Quellvektoren ist $s_{ef}=\{q_e,q_f^\dagger\}$ und die Formel verwendet das komplexe Quadrat, nicht den Betragsquadrat. Im hier zunächst reellen Dreieck ist

$$\boxed{B=\begin{pmatrix}8&2&2\\2&8&2\\2&2&8\end{pmatrix},
\qquad\operatorname{spec}B=\{12,6,6\}.}$$

Die tatsächlichen globalen Paartensoren wurden aus den ursprünglichen W-Einträgen neu aufgebaut. Sie besitzen 180 Bosonzeilen, 192 Fermionmoden und 5760 nichtverschwindende Koeffizienten $\pm1/2$. Ihre gesamte Gram-Matrix ist exakt $B\otimes I_{60}$.

Für jedes innere Label spannen die drei Paarzustände $P_e^\dagger|0\rangle$ und die drei Bosonzustände einen geschlossenen Raum auf. In dieser unnormierten Basis sind

$$J=\begin{pmatrix}0&gI_3\\gB&\Delta I_3\end{pmatrix},
\qquad \mathcal G=\begin{pmatrix}B&0\\0&I_3\end{pmatrix},
\qquad J^\dagger\mathcal G=\mathcal GJ.$$

Die vollständige helle N=2-Dynamik ist dieser sechsdimensionale Prozess mal dem inneren 60er-Faktor. Dunkle Zweifermionrichtungen außerhalb dieses Bildes sind entkoppelt. Der endliche Raum ist exakt invariant; es ist keine kleine Ritz-Näherung an eine ausgelassene N=2-Kette.

## 4.2 Tatsächlicher Übergang zwischen unabhängigen Bosonbereichen

Für verschiedene e,f gilt

$$\langle b_f|H_G|b_e\rangle=0,\qquad
\langle b_f|H_G^2|b_e\rangle=2g^2.$$

Die Übergangsamplitude beginnt daher mit $-g^2t^2$. Der Informationsübergang entsteht durch zwei kubische Vertizes über die gemeinsame Paarquelle.

Setze

$$F_\lambda(t)=e^{-i\Delta t/2}\left[
\cos\frac{\Omega_\lambda t}{2}
-i\frac{\Delta}{\Omega_\lambda}\sin\frac{\Omega_\lambda t}{2}\right],
\quad \Omega_\lambda=\sqrt{\Delta^2+4g^2\lambda}.$$

Die vollständige Bosonamplitude im Dreieck ist

$$U_{bb}(t)=F_6(t)I_3+
\frac{F_{12}(t)-F_6(t)}3\,\mathbf1\mathbf1^T.$$

Bei $g/\Delta=1/20$ und $t\Delta=1$ liegt die Übergangswahrscheinlichkeit von einem bestimmten Bosonbereich in einen anderen zwischen

$$0.000005866890950\quad\text{und}\quad0.000005866890951.$$

Sie ist klein, aber streng positiv und ohne erfolgreiche Ausgänge nachträglich herauszufiltern berechnet. Eine Optimierung der Übertragungszeit wurde nicht durchgeführt. Die gesamte innere Zustandsinformation wird im Übergang mitgeführt; die Amplitude hängt nicht vom inneren Label ab.

Auf dem leeren Hintergrund bleibt N=1 dagegen ohne Bewegung: Jeder kubische Vertex benötigt entweder einen Boson- oder einen Zweifermionanteil. Diese Konstruktion liefert deshalb noch keine freie Einfermion-Dispersion aus dem Vakuum. Die geladene Antwort auf einem physisch ausgewählten gemeinsamen Grundzustand ist eine andere, hier offene Aufgabe.

# 5. Der geschützte Code bewegt sich mit

## 5.1 Derselbe logische Faktor auf der gemeinsamen Quelle

Die Fortsetzung 1.1 konstruierte einen 15-dimensionalen inneren Paarcode $Q_\alpha$ aus 15 vorzeichenbehafteten perfekten Paarungen der 64 inneren Fermionlabels. Es gilt

$$\langle Q_\alpha,n_rQ_\beta\rangle=\frac1{32}\delta_{\alpha\beta}.$$

Bilde daraus auf jeder gemeinsamen Quelle den Zustand $|e,\alpha\rangle=Q_\alpha(q_e)^\dagger|0\rangle$. Seine Kreuz-Gram-Matrix lautet

$$\langle e,\alpha|f,\beta\rangle=s_{ef}^2\delta_{\alpha\beta}.$$

Zusammen mit den passenden kodierten Bosonzuständen entsteht im Dreieck ein 90-dimensionaler invarianter Raum:

$$\mathcal K\simeq\mathbb C^6\otimes\mathbb C^{15},\qquad
H_G|_{\mathcal K}=h_{\rm Zusammensetzung}\otimes I_{15}.$$

Der Faktor sechs beschreibt Ort im vorgegebenen Netz und Zusammensetzung Paar/Boson. „Ort“ meint hier den ausdrücklich eingesetzten Kopien- beziehungsweise Bosonbereich, keinen hergeleiteten physikalischen Raum. Die 15 logischen Dimensionen werden durch die Dynamik erhalten. Eine normierte Koordinatisierung erhält man durch die positive Quadratwurzel der Paar-Gram-Matrix.

## 5.2 Alle 192 bekannten einzelnen Modenverluste

Schreibe $q_e=\sum_x u_{ex}f_x$. Für die ursprüngliche Fermionmode (x,r) folgt mit den CAR-Vorzeichen

$$\langle e,\alpha|n_{x,r}|f,\beta\rangle
=\frac{u_{ex}\bar u_{fx}s_{ef}}{32}\delta_{\alpha\beta}.$$

Der Verlust kann damit etwas über den Zusammensetzungsfaktor erfahren, aber nichts über den logischen Faktor. Die Kompressionen der ungeraden Fehleroperatoren verschwinden wegen der festen Gesamtladung. Nach Normierung der Kopienbasis ist dies genau die Subsystem-Fehlerkorrekturbedingung. Methodischer Rahmen: [Kribs, Laflamme, Poulin und Lesosky](https://arxiv.org/abs/quant-ph/0504189).

Der neue Prüfer baut die tatsächlichen globalen Codevektoren auf und überprüft diese Gleichung für jede der 192 ursprünglichen Fermionmoden, einschließlich sämtlicher Kreuzterme der drei Quellen und der Vorzeichen im Einfermion-Ausgang des Verlustzweigs.

Die logische Information bleibt somit auch während beliebiger bekannter nativer Entwicklung auf diesem N=2-Unterraum gegen eine einzelne bekannte Modenlöschung korrigierbar. Die native Entwicklung vor dem Verlust verändert nur den Zusammensetzungsfaktor. Ein Fehler zu unbekannter Zeit, weitere Fehler nach dem Verlust oder die physische Ausführung der Korrektur sind davon nicht umfasst.

## 5.3 Recovery und Grenzen

Seien $A_0,A_1$ die beiden Erasure-Abbildungen für eine leere beziehungsweise besetzte verlorene Mode. Auf dem Code erfüllen sie

$$A_i^\dagger A_i=R_i\otimes I_{15},\qquad R_0+R_1=I_6.$$

Ihre Bilder liegen in den verbleibenden Gesamtladungssektoren zwei und eins und sind orthogonal. Die Polarzerlegungen $A_i=V_i(\sqrt{R_i}\otimes I)$ liefern eine Recovery: auf dem jeweiligen Fehlerbild $V_i^\dagger$ anwenden und den Zusammensetzungsfaktor ausspuren. Die Summe der beiden Zweige erhält den logischen Zustand exakt, auch bei Verschränkung mit einer Referenz. Außerhalb der Fehlerbilder lässt sich die Abbildung spurtreu ergänzen.

Damit ist eine mathematische Rekonstruktion angegeben. Ein nativer Apparat dafür wurde nicht konstruiert. Der gewählte 15er-Code bleibt außerdem nicht unter der gesamten inneren Gruppe invariant; seine konkrete Präparation benötigt weiterhin einen Bezugsvertrag. Die Schutzdimension 15 wurde hier nicht für alle denkbaren globalen Codes als optimal bewiesen. Die frühere Optimalität bezog sich auf den ursprünglichen hellen Code einer einzelnen Bank.

Für einen beliebigen endlichen einfachen Graphen mit M Kanten liefert dieselbe Konstruktion einen $2M\times15$-dimensionalen invarianten Bereich. Dieser enthält **eine geschützte logische Nachricht** mit beweglicher Zusammensetzung. Er ist kein Beweis für M unabhängig nutzbare logische Register oder für wechselwirkende Mehrnachrichtenverarbeitung.

# 6. Der vollständige unbedingte Wirkungstest — und seine fehlende Ressource

## 6.1 Gleicher Eingang, gleicher Hamiltonoperator, eine gezielte Änderung

Der Kopieneingang ist der gleichmäßige Einbosonzustand

$$|+\rangle_b=\frac{|b_0\rangle+|b_1\rangle+|b_2\rangle}{\sqrt3}.$$

Für einen vollständig innerlich symmetrischen Test kann der innere 60er-Faktor maximal gemischt gewählt werden. Alternativ kann eine konkrete logische Nachricht im 15er-Code verwendet werden; dann ist die Präparation nicht unter der gesamten inneren Gruppe invariant. Beide Zustandsverträge haben dieselbe Kopienstatistik und werden nicht als derselbe Symmetrievertrag ausgegeben.

In beiden Läufen wird derselbe globale Eingang verwendet. Im zweiten Lauf wird zusätzlich

$$U_A=e^{-i\pi N_{b,0}}$$

angewandt. Anschließend entwickelt sich das System in beiden Fällen mit demselben $H_G$. Gemessen wird die Bosonbesetzung $N_{b,1}$ im unabhängig kanonischen Empfängerbereich. Im N=2-Sektor ist dies ein Ja/Nein-Zeiger. Die erste und die zweite Observable kommutieren, und der Eingriff verändert die Empfängerstatistik zum Eingriffszeitpunkt nicht.

Für $g/\Delta=1/20$, $t\Delta=1$ wurden rationale Intervalle berechnet:

| Empfängerwahrscheinlichkeit | Zertifiziertes Intervall |
|---|---|
| Ohne Eingriff | [0.324232510511849, 0.324232510511850] |
| Mit Eingriff | [0.327246716499345, 0.327246716499346] |
| Differenz | [0.003014205987496, 0.003014205987497] |

Die Differenz ist ungefähr **0,301421 Prozentpunkte**. Ihre Entwicklung beginnt mit $\Delta^2t^2/300$. Die positive Änderung ist eine unbedingte Statistik, keine normierte Auswahl eines seltenen Erfolgszweigs.

Die Zeitentwicklung wurde als Taylorpolynom zwanzigster Ordnung mit exakt rationalen komplexen Koeffizienten ausgewertet. Im physisch normierten Raum gilt $\|H_G/\Delta\|<6/5$. Der Operatorrest wird durch

$$\epsilon\le\frac{25}{4}\frac{(6/5)^{21}}{21!}$$

begrenzt; für die Differenz zweier Wahrscheinlichkeiten wird $4\epsilon+2\epsilon^2$ angesetzt. Die angegebenen Dezimalintervalle enthalten den vollständigen Rest. Alle dargestellten Kurven außerhalb dieses Prüfpunktes sind lediglich numerische Veranschaulichung.

![Unbedingter Empfängerzeiger mit und ohne gewährten lokalen Phaseneingriff. Die Kurven sind numerische Veranschaulichung; der markierte Punkt bei tΔ=1 besitzt die ausgeschriebenen rationalen Fehlerschranken.](figures/wirkung.pdf)

## 6.2 Die Gegenkontrollen

Bei g=0 gibt es keine spätere Wirkung. Wenn die drei Quellen unabhängige Fermionkopien statt überlappender q-Quellen verwenden, zerfällt die Dynamik in getrennte Bereiche; ein Phaseneingriff in A beeinflusst B dann ebenfalls nicht. Damit wird die Wirkung dem gemeinsamen dynamischen Vermittler zugeordnet.

Eine anfängliche Kohärenz ist im gewählten Eingang vorhanden. Sie wird nicht mit Signalübertragung gleichgesetzt: Beide Vergleichsläufe beginnen mit genau dieser Kohärenz, der gezielte Eingriff ist lokal zum Bosonbereich A, die Statistik in B ist zunächst gleich und unterscheidet sich erst nach gemeinsamer Dynamik. Ein vollständig intern hergeleiteter Vorbereitungsprozess für diesen Eingang fehlt weiterhin.

## 6.3 Warum der lokale Eingriff noch nicht aus der Quelle folgt

Sei R die Spiegelung, welche die Bosonbereiche 0 und 1 und die entsprechenden Fermionkopien vertauscht. Die ursprünglichen globalen Kontrollen

$$X=\sum_{e,A}(b_{e,A}^\dagger P_{e,A}+\mathrm{h.c.}),
\qquad N_b=\sum_{e,A}b_{e,A}^\dagger b_{e,A}$$

kommutieren beide mit R. Jedes Wort und jede zeitlich geschaltete Folge aus diesen globalen Kontrollen respektiert deshalb die Spiegelung. Der lokale Phaseneingriff $U_A$ tut dies nicht. Er kann aus diesem Alphabet nicht erzeugt werden.

Die tatsächliche assoziative Kontrollalgebra im sechsdimensionalen Kopienprozess hat Dimension acht. Der lokale Operator $N_{b,0}$ liegt außerhalb dieser Algebra. Dies wurde zusätzlich zur Symmetriebegründung exakt berechnet. Ein einzelner fester Hamiltonoperator gewährt ohnehin noch nicht das unabhängige Schalten von X und $N_b$.

**Das ist die erste fehlende Stelle im ausgeführten Wirkungstest:** Die Quelle überträgt eine gesetzte Änderung, aber ihre eigene Vorrichtung zum gezielten Setzen dieser Änderung wurde nicht abgeleitet.

## 6.4 Interne Referenz und Aufzeichnung sind eigene Aufgaben

Ein hypothetisches neutrales Programmregister mit drei Zuständen „aus“, „links“, „rechts“ könnte das kontrollierte Instrument

$$U_{\rm prog}=|\mathrm{aus}\rangle\langle\mathrm{aus}|\otimes I
+|\mathrm{links}\rangle\langle\mathrm{links}|\otimes U_A
+|\mathrm{rechts}\rangle\langle\mathrm{rechts}|\otimes U_B$$

tragen. Es ist invariant unter gemeinsamer Spiegelung von Programm und Quelle. Das wurde exakt geprüft. Diese Ergänzung erklärt, wie Symmetrieverträglichkeit mit relationaler Adressierung vereinbar sein kann. Sie konstruiert weder das Programmregister noch seine bedingte Wechselwirkung aus den ursprünglichen Vertizes.

Auch der geschützte innere 15er-Faktor ist kein automatisch beschreibbares Messbuch. Auf ihm wirkt H als Identität. Ein anfangs festgelegter logischer Zeiger kann durch diese Dynamik allein keine neue Verteilung von Aufzeichnungen erhalten. Ein exakt erhaltener Zeiger lässt sich ohne zusätzliche Kopplung nicht beschreiben.

Der Bosonzeiger des Wirkungstests ist dynamisch und kann sich verändern. Er ist aber reversibel und nicht als dauerhaftes Record bewiesen. Seine stabile Auslesung, sein Energieaufwand und die native Realisierung eines Detektors bleiben offen. Der vollständige Ablauf von ursprünglicher Quellregel bis zu internem Record wird daher ausdrücklich **nicht als geschlossen** gemeldet.

# 7. Die Unterbestimmtheit lässt sich trotz starker Anforderungen beweisen

## 7.1 Zwei gleichmäßige Quellen mit verschiedenen Vorhersagen

Fordere zusätzlich: zehn Fermionkopien, fünfzehn Bosonbereiche, drei Verbindungen pro Knoten, Zusammenhang, gleiche lokale Regel und Gleichwertigkeit aller Knoten unter Graphsymmetrien. Fordere außerdem, dass keine ungenutzte lineare Fermionkopie übrig bleibt.

Sowohl der Petersen-Graph als auch das fünfeckige Prisma erfüllen diese Bedingungen. Beide sind nicht bipartit; ihre ungerichteten Knoten-Kanten-Inzidenzmatrizen haben Rang zehn. Die Knoten-Transitivität wurde durch explizite Automorphismen geprüft. Ihre gemeinsamen Rückwirkungen erfüllen dennoch

| Größe | Petersen | Fünfeckiges Prisma |
|---|---:|---:|
| $\operatorname{tr}B$ | 120 | 120 |
| $\operatorname{tr}B^2$ | 1200 | 1200 |
| $\operatorname{tr}B^3$ | 13920 | 13920 |
| $\operatorname{tr}B^4$ | 175680 | 176320 |

Beide Modelle verwenden dieselben g und $\Delta$. Die Differenz ist deshalb kein bloßer Wechsel der Einheiten. Verschiedene Spektren von B erzeugen verschiedene N=2-Dynamiken.

Ein konkreter neutraler Beobachtungsvertrag beginnt mit einer gleichmäßig gemischten Einbosonbelegung und liest die gesamte Bosonzahl aus. Für $\Delta=1$ unterscheidet sich der Koeffizient von $t^8$ in ihrer Rückkehrwahrscheinlichkeit um

$$\boxed{\frac{128}{945}g^8.}$$

Die Modelle stimmen in früheren entsprechenden Momenten überein und sind dennoch beobachtbar verschieden. Innere Symmetrie, Gleichmäßigkeit, lokale Einfachheit und vollständige Nutzung der Kopien reichen in dieser Klasse nicht zur Auswahl einer einzigen Quelle.

![Zwei konkrete Gegenmodelle mit denselben Größen- und Gleichmäßigkeitsbedingungen. Die Zeichnungen zeigen Modellgraphen, keine aus TFPT abgeleiteten Raumgeometrien. Ihre vierte Rückwirkungsspur ist verschieden.](figures/gegenmodelle.pdf)

## 7.2 Phasen erzeugen eine weitere Auswahlfrage

Erlaube auf einer Dreieckskante relative Phasen:

$$q_0=(f_0+f_1)/\sqrt2,\quad
q_1=(f_1+f_2)/\sqrt2,\quad
q_2=(f_2+e^{i\Phi}f_0)/\sqrt2.$$

Die innere Grammatik und Gesamtladung bleiben gleich. Die induzierte bosonische Schleife besitzt

$$B_{01}B_{12}B_{20}=8e^{2i\Phi}.$$

Dieser Ausdruck ist unter unabhängigen Phasenkonventionen der Bosonbereiche invariant. Die Paarumwandlung verdoppelt hier die Quellphase. Es handelt sich um eine aus gesetzten Quellphasen folgende Verbindungsgröße; ein dynamisches Raumzeit-Eichfeld wird damit nicht hergeleitet.

```{=latex}
\Needspace{10\baselineskip}
```

Drei Fälle wurden exakt ausgewertet:

| Quellphase | Rang der drei Fermionquellen | Bosonische Eigenwerte |
|---|---:|---|
| $\Phi=0$ | 3 | 12, 6, 6 |
| $\Phi=\pi/2$ | 3 | 10, 10, 4 |
| $\Phi=\pi$ | 2 | 12, 6, 6 |

Bei null und pi ist B sogar identisch. Die gesamte Antwort mit ausschließlich bosonischen Eingängen, bosonischen Instrumenten und bosonischer Auslesung im N=2-Bereich kann diese beiden Quellen deshalb nicht unterscheiden. Trotzdem besitzt nur die pi-Quelle die ungenutzte Fermionkombination $(f_0-f_1+f_2)/\sqrt3$.

Das ist ein präziser Test der Beobachtungsäquivalenz: Gleichheit einer vollständigen eingeschränkten Antwort ist noch keine Gleichheit des gesamten markierten Fermion-Boson-Prozesses. Eine künftige Auswahlregel muss entweder weitere physische Instrumente bestimmen oder erklären, warum die zusätzliche Unterscheidung irrelevant sein soll.

# 8. Die Größenfolge tatsächlich weitergeführt

## 8.1 Ein exakter Graphoperator für jeden endlichen Kandidaten

Sei V die ungewichtete Knoten-Kanten-Inzidenz, hier als Matrix mit Kantenzeilen und Knotenspalten. Für die positive Zweiknoten-Regel gilt

$$\boxed{B=8I+2A_{\rm Linie}=4I+2VV^T.}$$

$A_{\rm Linie}$ verbindet zwei Bosonbereiche genau dann, wenn ihre Kanten einen Fermionknoten gemeinsam haben. Die Gleichung folgt direkt aus der quadrierten Überlappung. Sie ist keine angenommene effektive Sprungmatrix.

Insbesondere gilt für maximalen Knotengrad d

$$4I\le B\le4(d+1)I.$$

Damit ist die Gram-Matrix $B/8$ der Paarquellen gleichmäßig positiv. Die gemeinsame N=2-Dynamik erfüllt unabhängig von der Zahl der Knoten

$$\|H_G|_{N=2}\|\le\Delta+2|g|\sqrt{d+1}.$$

Das ist eine wirkliche Größenkontrolle für diesen Sektor. Im vollständigen Fockraum sind Bosonbesetzungen unbeschränkt; die gleiche Normschranke gilt dort nicht.

## 8.2 Wirkung beginnt erst nach ausreichend vielen Vertizes

Sind zwei Bosonbereiche im Liniengraphen im Abstand r, verschwinden ihre Hamiltonmatrixelemente bis zur Ordnung $2r-1$:

$$\langle b_f|H_G^n|b_e\rangle=0\qquad(n<2r).$$

Jeder räumliche Schritt im eingesetzten Liniengraphen benötigt zwei kubische Vertizes. Auf einer einfachen Kette ist der erste Koeffizient

$$\langle b_f|H_G^{2r}|b_e\rangle=2^rg^{2r}.$$

Die ersten fünf Abstände wurden exakt geprüft. Das allgemeine Argument folgt aus der Blockstruktur: Jeder Wechsel zwischen Bosonbereichen enthält einen Faktor B, dessen nichtdiagonale Einträge nur benachbarte Kanten verbinden.

Im Wechselwirkungsbild bezüglich $\Delta N_b$ hat die Kopplung die gleichmäßige Normschranke $a=2|g|\sqrt{d+1}$. Aus der Dysonreihe folgt

$$\boxed{|\langle b_f|e^{-itH_G}|b_e\rangle|
\le e^{a|t|}\frac{(a|t|)^{2r}}{(2r)!}.}$$

Die Formel gibt keine strikt verschwindende Fernwirkung für positive Zeit; sie begrenzt die kleinen Ausläufer. Sie ist eine Aussage über den N=2-Bosonkanal, keine allgemeine Vielteilchen-Lieb–Robinson-Schranke. Der etablierte allgemeinere Rahmen setzt ebenfalls definierte Lokalitätsbedingungen voraus. [Bravyi, Hastings und Verstraete](https://arxiv.org/abs/quant-ph/0603121).

## 8.3 Ein unendliches Netz ist in N=2 mathematisch beherrschbar

Auf einem abzählbaren, lokal endlichen Graphen mit beschränktem Grad ist $VV^T$ beschränkt. Wegen der obigen Schranken definiert der vollständige N=2-Operator einschließlich der dunklen Paarzustände einen beschränkten selbstadjungierten Operator. Seine unitäre Entwicklung existiert daher für alle Zeiten.

Für eine Folge endlicher induzierter Teilgraphen, die das Netz ausschöpft, sind die Hamiltonoperatoren gleichmäßig beschränkt. Auf Zuständen mit endlichem Träger stimmen ihre Wirkungen ab einer hinreichend großen Umgebung mit der unendlichen Wirkung überein. Dichte dieses Trägers und die gemeinsame Normschranke geben starke Konvergenz der Operatoren; die Exponentialreihe liefert starke Konvergenz der Zeitentwicklung, gleichmäßig auf kompakten Zeitintervallen.

Das ist ein analytischer Beweis eines N=2-Dynamikgrenzwerts **für den vorgegebenen Graphen**. Es ist keine Berechnung des thermodynamischen Grundzustands, keine Ableitung eines Kontinuums und keine Auswahl einer räumlichen Dimension.

Die frühere exakte Anhängeisometrie unabhängiger Kopien gilt beim Anhängen einer gekoppelten Kante nicht unverändert. Im Vierknotentest bleibt der alte B-Block erhalten, aber eine neue Nachbarkopplung von zwei tritt hinzu. Die bisherige endliche Dynamik ist dann nicht exakt invariant. Ihr lokaler Grenzwert wird stattdessen durch die erläuterte Konvergenz kontrolliert.

## 8.4 Erste Vielteilchenkontrolle, ausdrücklich mit übernommener Voraussetzung

Aus dem bereits separat bewiesenen nativen Casimirsatz

$$\sum_A P_A(q)^\dagger P_A(q)\le\frac{15}{2}N_q$$

und $\sum_eN_{q_e}\le dN_f$ folgt durch quadratische Ergänzung

$$H_G\ge-\frac{15dg^2}{2\Delta}N_f
\ge-480d\frac{g^2}{\Delta}L,$$

wobei L die Zahl der Fermionknoten bezeichnet. Damit ist eine extensive untere Schranke vorhanden. Der Casimirsatz wird aus der gepinnten Quelle übernommen; der neue Rechner prüft seine Koeffizientenfolge, nicht nochmals die gesamte alte Identität.

Diese Schranke wählt keinen Zustand aus. Fügt man $\mu N$ hinzu, reicht beispielsweise $\mu>15dg^2/(2\Delta)$ für ein eindeutig bevorzugtes leeres Vakuum. Der chemische Potentialvertrag bleibt damit auch nach Zusammensetzung eine zusätzliche physikalische Entscheidung.

# 9. Ergebnis der fünf vereinbarten Schritte

| Schritt | Ergebnis dieser Arbeit | Grenze |
|---|---|---|
| Ausgangsdaten festhalten | W, Symmetrien, Ladung und zusätzliche Daten getrennt | Kein neuer Ursprungsgrundsatz bewiesen |
| Kompositionsregel untersuchen | Explizite gemeinsame Quelle; versteckten dunklen Modus gefunden; Dreieck korrigiert ihn | Graph und Quellphasen sind gesetzt |
| Eindeutigkeit entscheiden | Zwei gleichmäßige Quellen sind neutral unterscheidbar; eingeschränkte Antwort kann weitere Unterschiede verdecken | Zusätzliche Auswahlregel erforderlich |
| Internen Wirkungstest rechnen | Streng positive unbedingte Änderung mit vollständiger kleiner Dynamik und Fehlerintervall | Lokaler Aktuator, Zustand und Messapparat nicht hergeleitet |
| Größenfolge und Vorhersage | N=2-Grenzdynamik, Ausbreitungsschranke, extensive Formschranke und unterscheidende Modellvorhersage | Kein voller Vielteilchen-Grenzwert, keine empirische Bestätigung |

Der stärkste neue zusammenhängende positive Strang lautet:

$$\begin{aligned}
\text{ursprünglicher W-Kanal + gesetzte Kompositionsregel}
&\longrightarrow\text{gemeinsame kubische Dynamik}\\
&\longrightarrow\text{geschützte bewegliche Information}\\
&\longrightarrow\text{Wirkung bei gewährtem Eingriff}\\
&\longrightarrow\text{kontrollierte N=2-Größenfolge}.
\end{aligned}$$

Der Instrumentenvertrag ist eine Voraussetzung. Innerhalb dieses Vertrags wird die vollständige unbedingte Statistik berechnet. Es wird kein erfolgreicher Zweig selektiv normiert.

Die unterstellte gemeinsame Quellregel ist weiterhin nicht aus TFPT ausgewählt. Der gezielte Eingriff ist durch einen konkreten Algebraausschluss als zusätzliche Ressource identifiziert. Ein dauerhaftes internes Record fehlt. Diese drei Herkunftsfragen werden durch den Transport- und Codebeweis nicht geschlossen.

Der nächste entscheidende Herkunftsnachweis müsste deshalb eine tatsächlich aus dem Quellmodell stammende **relationale Adressierung samt beschreibbarem Zeiger** liefern und die dafür notwendige Zustandsregel offenlegen. Wenn dies nur mit einer neuen Grundannahme möglich ist, muss diese Annahme als solche benannt und an unterscheidenden Vorhersagen geprüft werden. Die Gegenmodelle dieser Arbeit verhindern, dass bloße Gleichmäßigkeit oder ein gutes lokales Spektrum als bereits ausreichende Auswahl ausgegeben wird.

# 10. Reproduzierbarkeit und Quellen

Die vier neuen Rechner bestätigen zusammen **614 explizite Bedingungen**: 402 für die gemeinsame Quelle und den Code, 22 für Intervention und Operationsgrenze, 176 für Gegenmodelle und Größenidentitäten sowie 14 für Quellphasen. Die vollständige Wiederholung in einer frischen Paketkopie liefert dieselben Ergebnisse.

Vier neue Rechner prüfen die globale Tensorhebung und alle 192 Modenverluste, die kontrollierte Zeitentwicklung samt Instrumentengrenze, die Graph-Gegenmodelle und Größenidentitäten sowie die Quellphasen. Alle Bedingungen verwenden explizite Fehlermeldungen und bleiben bei Python-Optimierung aktiv. Die normale und die optimierte Ausführung müssen identische wissenschaftliche JSON-Ergebnisse liefern. Die Prüfzähler enthalten wiederholte Moden- und Automorphismenbedingungen; sie sind keine Anzahl unabhängiger Theoreme.

Die allgemeinen Sätze über Involutionen, Recovery, Graphnormen, Dysonreste und starke Konvergenz sind im Text bewiesen und werden durch endliche exakte Zeugen gestützt. Sie sind nicht in einem formalen Beweisassistenten verifiziert. Die numerischen Diagrammkurven ersetzen keine der angegebenen rationalen Intervallschranken.

**R1:** Forschungspaper *TFPT und Universalraum*, Synthese 1.0 vom 15.09.2026. Gemeinsamer Prozessvertrag und Quellenübersicht.

**R2:** *TFPT und Universalraum: sechs Forschungsfortsetzungen*, Fortsetzung 1.1 vom 15.09.2026. Ursprünglicher optimaler 15er-Code, Lie-Replay, Matrixmomente und Prüfung der fundamentalen Reduktion. Dazu die eingefrorenen Rechner und Ergebnisdateien der Code- und Lie-Prüfung.

**R3:** Quelle S038, *TFPT / Universalraum: Ergebnisse v1.6*. Voll-Fock-Casimiridentität und chemisches Potential. Ihre Rolle als übernommene Voraussetzung ist in §8.4 ausdrücklich markiert.

**R4:** Quelle S003, *Die fundamentale Reduktion*. Unterscheidung innerer Labels, gemeinsamer Quelle und unabhängiger räumlicher Vorkommen.

**R5:** Quelle S074, v1.6.7 einschließlich Prozess-, Schatten- und Z4-Nachtrag. Ursprüngliche Tensor- und Operationsverträge.

**E1:** D. W. Kribs, R. Laflamme, D. Poulin, M. Lesosky: *Operator quantum error correction*. [Primärarbeit](https://arxiv.org/abs/quant-ph/0504189).

**E2:** S. Bravyi, M. B. Hastings, F. Verstraete: *Lieb–Robinson bounds and the generation of correlations and topological quantum order*. [Primärarbeit](https://arxiv.org/abs/quant-ph/0603121).

Diese Fortsetzung berichtet neue Rechnungen gegenüber dem ausgewerteten lokalen Korpus, keinen weltweit überprüften Prioritätsanspruch. Sie liefert keine vollständige Raumzeit-, RH-, Faktorisierungs-, P-vs-NP- oder TOE-Lösung. Kein T1–T8-Tor wird geschlossen gemeldet.
