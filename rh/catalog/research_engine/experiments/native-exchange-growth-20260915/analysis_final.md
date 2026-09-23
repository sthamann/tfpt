# Universalraum: ein expliziter Austausch mit Gegenstelle und kohärentem Flussregister

## Ergebnis dieser Fortsetzung

**Ein nativer innerer Austausch ist exakt identifiziert; für den räumlichen Austausch liegt ein vollständiger mathematischer Kandidat vor.** Innerhalb der ursprünglichen Bank tauschen der Fermion- und der Bosonenteil eine Ladungseinheit von zwei aus. Ein zusätzlicher räumlicher Baustein steht bereits in einem älteren TFPT-Gittermodell. Dessen Verbindung zur neuen 64-Fermion-Bank lässt sich anhand ihres tatsächlichen Grundzustands und ihrer spektralen Antwort ausdrücklich berechnen.

Die entscheidende Grenze bleibt: **Der Kopplungsterm zwischen zwei Banken und das Linkregister sind eine erklärte Erweiterung. Ihre Erzeugung aus dem ursprünglichen lokalen Compiler ist nicht bewiesen.** Damit ist ein überprüfbarer Anschluss gefunden, aber der gemeinsame ursprüngliche Prozess noch nicht identifiziert.

Diese Fortsetzung enthält fünf konkrete Ergebnisse:

1. Den exakt lösbaren ursprünglichen Paar-Boson-Austausch samt tatsächlicher Kanal-Gram-Matrix und einem Kohärenznachweis auf dem nativen Grundzustand.
2. Einen erneut aus der Quelle aufgebauten vollständigen Zwei-Orte-Austausch im älteren Modell, mit zertifizierter endlicher Zeitentwicklung.
3. Einen exakten Satz über den ersten Austausch zwischen zwei Kopien des neuen nativen Grundzustands: seine Stärke ist strikt positiv und durch die vorhandenen Zustandsgrenzen eingeschlossen.
4. Eine genaue Verbindung zum niedrigen nativen Entnahmepol, einschließlich Ladungsgegenstelle, Projektionsgrenze und Aufzeichnungsbedingung.
5. Eine Erweiterung der arithmetischen Zustandszählgrenze auf endlich viele Banken mit elektrischen Links; außerdem eine Grenze der naiven unendlichen Wiederholung.

„Exakt“ bezeichnet im Folgenden eine ausgeschriebene mathematische Ableitung unter den jeweils genannten Voraussetzungen. Die neuen Ableitungen sind nicht in Lean formalisiert und nicht extern begutachtet. Die endlichen Rechnungen sind reproduziert; ihre Reichweite wird jeweils angegeben.

---

## 1. Welche Quellen tatsächlich miteinander verbunden wurden

### 1.1 Die neue lokale Bank

Verwendet wird unverändert der Stand v1.6.4:

\[
H_x=\Delta N_{b,x}+g\sum_{A=1}^{60}
(b_{x,A}^{\dagger}P_{x,A}+P_{x,A}^{\dagger}b_{x,A}),
\quad P_{x,A}=\sum_{r<s}W_{A,rs}f_{x,s}f_{x,r},
\]

\[
N_x=N_{f,x}+2N_{b,x},\qquad g/\Delta=1/20,\quad\mu=0.
\]

Es gibt 64 CAR-Fermionmoden und 60 CCR-Bosonmoden. Die Markierung \(x\) bezeichnet zunächst eine Kopie dieser Bank. Aus einer Kopie allein folgt noch kein räumlicher Ort.

Der vorhandene Grundzustand \(\Omega\) ist eindeutig, invariant unter der angegebenen inneren Symmetrie und hat \(N\Omega=64\Omega\). Aus `RESULTS.md` und den erneut geprüften v1.6.4-Zertifikaten werden benutzt:

\[
0.842846<\bar b:=\langle N_b\rangle<1.245656,
\quad -1.158089<E_0/\Delta<-1.129636,
\]

\[
\nu:=\langle f_r^{\dagger}f_r\rangle=1-\bar b/32,
\quad \langle f_r^{\dagger}f_s\rangle=\nu\delta_{rs}.
\]

Entnahme und Addition besitzen positive Spektralmaße \(d\nu_-\) und \(d\nu_+\), jeweils pro Fermionkomponente:

\[
\int d\nu_-=\nu,\qquad\int d\nu_+=1-\nu,
\quad\int u\,d\nu_-(u)=\int v\,d\nu_+(v)=a,
\quad64a=\Delta\bar b-E_0.
\]

Die Entnahmeenergien sind größer als \(0.007737\Delta\); alle Additionsenergien sind größer als \(0.329636\Delta\). Der niedrige Entnahmepol hat Gewicht

\[
Z>\frac{40912436089}{46487375000}=0.880076280689\ldots
\]

und gehört zu einem 64-dimensionalen Multiplet im Sektor \(N=63\).

### 1.2 Der bereits vorhandene räumliche Austauschbaustein

In `experiments/theory-contracts/local-window-round37/checker.py`, insbesondere `parent_terms`, steht für eine orientierte Verbindung \(x\to y\):

\[
a_0 U_{xy}c_{L,y}^{\dagger}c_{L,x}
+\eta a_0 U_{xy}c_{H,y}^{\dagger}c_{L,x}
+\eta a_0 U_{xy}c_{L,y}^{\dagger}c_{H,x}+\mathrm{h.c.}
\]

mit \(a_0=1/12,\eta=1/2\), ganzzahligem elektrischem Fluss und \([E,U]=U\). Hinzu kommen die vorhandenen Onsite-Terme und, sofern der Graph entsprechende Pfade hat, die ursprünglichen Zwei-Link-Terme. Die Kopplung ist in diesem Modell gesetzt; dessen Quellen beanspruchen selbst keinen bewiesenen ursprünglichen Vakuumzustand.

Die Quelle `clock-rotor-joint-charge/README.md` erklärt außerdem, warum eine einfache Clock-Phasenidentifikation dieses Modell nicht mit dem anderen Compiler identifiziert. Die gemeinsame Phasenwirkung ist auf dem Gauss-physikalischen Sektor nur Eichwirkung. Dieses Hindernis wird hier nicht durch Umbenennung entfernt.

Ein weiterer bereits vorhandener Ansatz, `v746_phys_gnet_local_functor.py`, besitzt eine endliche räumliche Verschiebung und CAR-Intervallalgebren. Er benutzt jedoch eine andere Zustandsfamilie. Der dortige freie Diracsee-Zustand wird nicht mit \(\Omega\) gleichgesetzt.

**Quellenvergleich:** Dieselbe mathematische Form eines Austauschoperators genügt nicht für dieselbe mikroskopische Herkunft. Der nachfolgende Anschluss ist deshalb als Erweiterung mit offenem Herkunftsnachweis ausgewiesen.

### 1.3 Der Austausch, der im ursprünglichen Modell bereits ohne Erweiterung vorhanden ist

Die Formulierung „zwei operational bestimmte Teile“ muss nicht schon zwei räumliche Banken bedeuten. Die ursprüngliche Bank besitzt bereits die Teile

\[
\mathcal H_{\mathrm F}=\Lambda(\mathbb C^{64}),\qquad
\mathcal H_{\mathrm B}=\mathcal F_s(\mathbb C^{60}).
\]

Gerade Fermionobservablen und Bosonobservablen bestimmen zwei operational verschiedene, miteinander verträgliche Teilsystemalgebren. Ihr tatsächlicher Austauschoperator ist

\[
\boxed{C=\sum_A b_A^\dagger P_A,\qquad C^\dagger=\sum_A P_A^\dagger b_A,
\quad H_{\mathrm{int}}=g(C+C^\dagger).}
\]

Beim Vorgang \(C\) gilt \(\Delta N_f=-2,\Delta N_b=+1\), also \(\Delta(N_f+2N_b)=0\). Die aufnehmende Gegenstelle ist der schon vorhandene Bosonenkanal. Hier ist kein zusätzlicher räumlicher Link eingesetzt.

**Ein exakt geschlossener Anfangsversuch.** Aus den tatsächlichen 480 Einträgen des Tensors wurde erneut für alle 3.600 Matrixeinträge \(WW^\dagger=8I_{60}\) geprüft. Mit dem leeren Fockzustand \(|0\rangle\) definiere

\[
|F_A\rangle=\frac1{\sqrt8}P_A^\dagger|0\rangle,
\qquad |B_A\rangle=b_A^\dagger|0\rangle.
\]

Diese beiden Zustände spannen für jeden Kanal einen exakt invarianten Raum des unveränderten Hamiltonoperators auf:

\[
H_A=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}.
\]

Der gesamte Sektor \(N=2\) besteht aus 60 solchen Zweierblöcken und 1.956 fermionischen dunklen Zuständen, insgesamt 2.076 Dimensionen. Deshalb ist diese Reduktion vollständig und keine Zwei-Zustands-Näherung.

Für den Anfang \(|F_A\rangle\) ist die Wahrscheinlichkeit, das Paar später im Bosonenteil zu finden,

\[
\boxed{P_{F_A\to B_A}(s)=
\frac{32g^2}{\Delta^2+32g^2}
\sin^2\!\left(\frac{s}{2}\sqrt{\Delta^2+32g^2}\right).}
\]

Bei der tatsächlichen Kopplung \(g/\Delta=1/20\) beträgt das Maximum **\(2/27\), also ungefähr 7,4074 %**. Es wird keine zusätzliche Resonanzsteuerung angenommen, um daraus einen vollständigen Transfer zu machen.

Dieser Anfang ist ein ausdrücklich angegebener Zustand im ursprünglichen Hilbertraum. Seine Präparation aus dem echten Grundzustand \(N=64\) folgt nicht aus zahlbewahrenden Operationen; dazu wäre eine Ladungsgegenstelle beziehungsweise ein anderes Präparationsverfahren erforderlich. Er ist nicht als das Vakuum der Theorie ausgegeben.

**Die kohärente Aufzeichnung ist ebenfalls sichtbar.** Acht verschiedene Fermionpaarbeiträge eines Kanals führen zum selben Boson \(A\). Dessen Aufzeichnung unterscheidet diese acht Innenwege nicht. Der Kanal besitzt die Gram-Matrix \(w_A^\dagger w_A\) vom Rang eins, nicht die Diagonalmatrix einer Messung der einzelnen Paare. Der passend kohärente Paarzustand besitzt deshalb den Kopplungsfaktor \(\sqrt8\). Ein vorab gemischtes Register mit orthogonal unterscheidbaren Paaren hätte im kurzen Zeitverlauf nur \(g^2s^2\) statt \(8g^2s^2\) Konversionswahrscheinlichkeit. Diese konkrete native Interferenzstruktur muss eine spätere History erhalten.

**Kohärenz auf dem tatsächlichen Grundzustand.** Aus der unveränderten Energieidentität folgt

\[
\langle\Omega|g(C+C^\dagger)|\Omega\rangle=E_0-\Delta\bar b<0.
\]

Der echte Grundzustand hat damit nachweislich nichtverschwindende Paar-Boson-Kohärenz. Er ist stationär; sein mittlerer Austauschstrom ist null. Eine nichtselektive ideale Messung von \(N_b\) löscht diese Austausch-Kohärenz. Die danach im System verbleibende mittlere Energie ist \(\Delta\bar b\). Ihr Anstieg beträgt exakt

\[
\Delta E_{\mathrm{Messung}}=\Delta\bar b-E_0,
\qquad
\boxed{1.972482\Delta<\Delta E_{\mathrm{Messung}}<2.403745\Delta.}
\]

Das ist ein direkter, quellengebundener Nachweis dafür, dass eine ausgelesene Besetzungshistorie den ursprünglichen kohärenten Zustand verändert. Ein solches Messverfahren ist damit nicht als schon vorhandene native Operation oder als kostenloser Prozess behauptet.

**Was dieser ursprüngliche Austausch noch nicht liefert:** Die Trennung in Fermion- und Bosonenteil definiert noch keine Entfernung, Nachbarschaft oder räumliche Gegenstelle. Der räumliche Übergang ist deshalb weiterhin ein gesonderter Schritt. Genau diesen Schritt präzisieren die folgenden Abschnitte.

---

## 2. Der vollständig bestimmte Zwei-Banken-Kandidat

### 2.1 Teile, Gegenstelle und Verbindungsregister

Man nehme zwei Kopien der Bank und einen kompakten U(1)-Rotor:

\[
\mathcal H_{\rm kin}=\mathcal H_x\widehat\otimes\mathcal H_y\otimes\ell^2(\mathbb Z),
\quad E|e\rangle=e|e\rangle,\quad U|e\rangle=|e+1\rangle.
\]

Das Dach erinnert an die fermionische, graduierte Zusammensetzung: Fermionfelder verschiedener Banken antikommutieren. Gerade lokale Observablen vertauschen. Ein gewöhnliches Tensorprodukt ohne die entsprechenden Vorzeichen wäre falsch.

Operational unterscheidet man die Teile durch ihre lokalen geraden Observablen, etwa \(N_x,N_{b,x},f_{x,r}^{\dagger}f_{x,s}\), beziehungsweise die entsprechenden Observablen bei \(y\). Die Verbindung trägt den gemeinsamen Fluss. Auf dem physikalischen Raum koppelt die Gauss-Bedingung diese Größen; dort besteht im Allgemeinen keine freie Tensorzerlegung in zwei unabhängige physikalische Teilsysteme.

Für den neutralen Zwei-Banken-Versuch setze

\[
G_x=N_x-64+E,\qquad G_y=N_y-64-E,
\quad\mathcal H_{\rm phys}=\ker G_x\cap\ker G_y.
\]

Die Ladung enthält ausdrücklich auch \(2N_b\). Nur die Fermionenzahl zu verwenden, würde bereits die ursprüngliche lokale Umwandlung falsch bilanzieren.

### 2.2 Austausch und Adjungiertes

\[
\boxed{B_{x\to y}=\sum_{r=1}^{64}f_{y,r}^{\dagger}U f_{x,r},
\qquad B_{x\to y}^{\dagger}=\sum_{r=1}^{64}f_{x,r}^{\dagger}U^{\dagger}f_{y,r}.}
\]

Der neue Hamiltonoperator lautet

\[
\boxed{H_{xy}=H_x+H_y+\frac\kappa2 E^2
+\tau B_{x\to y}+\bar\tau B_{x\to y}^{\dagger},\qquad\kappa>0.}
\]

Für den ersten Summanden des Austauschs ist die Bilanz

| Größe | Änderung |
|---|---:|
| \(N_x\) | \(-1\) |
| \(N_y\) | \(+1\) |
| \(E\) | \(+1\) |
| \(N_x+N_y\) | \(0\) |
| \(G_x,G_y\) | jeweils \(0\) |

Das Adjungierte kehrt jede Änderung um. Insbesondere

\[
[H_{xy},G_x]=[H_{xy},G_y]=[H_{xy},N_x+N_y]=0.
\]

Der Austausch ist beschränkt. Pro Komponente hat \(\tau B_r+\bar\tau B_r^\dagger\) Norm höchstens \(|\tau|\), insgesamt also höchstens \(64|\tau|\). Ein beschränkter selbstadjungierter Zusatz zum vorhandenen selbstadjungierten \(H_x+H_y+\kappa E^2/2\) liefert einen selbstadjungierten Hamiltonoperator auf derselben Domäne. Auf endlichen Graphen gilt dieselbe Argumentation mit einer endlichen Summe von Links. Damit ist der Kandidat als Dynamik definiert, ohne Flussabschneidung oder nur formales Adjungieren.

### 2.3 Wie weit Symmetrie den Anschluss bestimmt

Unter der zusätzlichen Anforderung, dass der bilineare Transport die **gemeinsame globale** innere Spin(10)×SU(4)-Symmetrie der identisch ausgerichteten Banken erhält und der Link ein innerer Skalar ist, muss eine Kopplungsmatrix \(M\) in \(f_y^\dagger M f_x\) mit der irreduziblen 64-dimensionalen Darstellung vertauschen. Nach Schurs Lemma ist \(M=\tau I\).

Dies bestimmt die innere Matrix innerhalb dieser eng angegebenen Klasse. Es bestimmt weder \(\tau\), noch \(\kappa\), noch den Graphen, noch die räumliche Dimension. Unabhängige lokale Spin(10)-Eichtransformationen an den beiden Enden würden zusätzliche nichtabelsche Linkstruktur verlangen. Auch höhere Wechselwirkungen sind durch diesen Bilinearsatz nicht ausgeschlossen.

### 2.4 Anfangszustand

\[
\boxed{\Psi_0=\Omega_x\widehat\otimes\Omega_y\otimes|E=0\rangle.}
\]

Er ist Gauss-physikalisch und Grundzustand des entkoppelten Systems mit Rotor. Er wird hier als Anfangszustand eines Einschaltversuchs benutzt. Er ist nicht als Grundzustand des bereits gekoppelten Systems bewiesen; seine experimentelle Präparation ist ebenfalls keine Folge der Rechnung.

---

## 3. Neuer Anschlusssatz: Der native Grundzustand trägt einen nichtverschwindenden Austausch

### 3.1 Exakte Übergangsstärke

Aus CAR, Produktzustand und der diagonalen Einteilchendichte folgt

\[
\begin{aligned}
\|B\Psi_0\|^2
&=\sum_{r,s}\langle f_{x,r}^{\dagger}f_{x,s}\rangle
\langle f_{y,r}f_{y,s}^{\dagger}\rangle\\
&=64\nu(1-\nu)
=\boxed{2\bar b-\bar b^2/16}=:A.
\end{aligned}
\]

Das Normquadrat des adjungierten Übergangs ist dasselbe. Beide Richtungen enden in orthogonalen Ladungs- und Flusssektoren.

Aus den vorhandenen rationalen Grenzen folgt strikt

\[
\boxed{1.64129266376775<A<2.394333320604.}
\]

**Bedeutung:** Der native Grundzustand ist kein vollständig mit Fermionen besetztes starres Register. Durch die bosonische Paarumwandlung besitzt er ein nichtverschwindendes Additionsgewicht. Deshalb ist eine aufnehmende Gegenstelle vorhanden. Bei einem rein vollbesetzten Fermionzustand mit \(\bar b=0\) wäre der entsprechende Austausch dagegen durch die Besetzung blockiert.

Der Satz wurde nicht an einer erfundenen Näherung für \(\Omega\) gewonnen. Er verwendet dessen schon bewiesene Symmetrie, Gesamtladung und Bosonenzahlgrenzen. Eine separate kleine Fockrechnung prüft unabhängig die fermionischen Vorzeichen und die Normidentität; sie ersetzt den Satz über die echte Bank nicht.

### 3.2 Die erste Austauschbewegung ist ein Ladungspaar

\[
B\Psi_0\in\{N_x=63,N_y=65,E=1\},
\quad B^\dagger\Psi_0\in\{N_x=65,N_y=63,E=-1\}.
\]

Beide Ausgangsbanken haben \(N=64\); nach dem Übergang steht einer negativen Ladungsabweichung eine positive gegenüber. Die Gesamtladung bleibt erhalten.

Mit \(Q_{\pm}\) als Projektor auf diese beiden Ladungspaarsektoren gilt für die physikalische Zeit \(s\to0\), in Einheiten \(\hbar=1\),

\[
\|Q_{\pm}e^{-isH_{xy}}\Psi_0\|^2
=2|\tau|^2 A s^2+o(s^2).
\]

Der dimensionslose Vorfaktor vor \(|\tau|^2s^2\) liegt zwischen **3.2825853275355 und 4.788666641208**. Dies ist eine genaue Aussage über den ersten nichtverschwindenden Zeitkoeffizienten. Ohne weitere Abschätzung darf sie nicht für beliebig große Zeiten eingesetzt werden.

Bei identischen Anfangsbanken entsteht keine bevorzugte Transportrichtung: Beide Richtungen haben denselben führenden Betrag. Ein gerichteter Transfer benötigt eine entsprechende Anfangsasymmetrie, Anregung oder Ansteuerung. Nichtverschwindende Austauschfluktuation und gerichteter Transport sind verschiedene Aussagen.

### 3.3 Die gemeinsame spektrale Austauschantwort

Betrachte zunächst die entkoppelte Entwicklung inklusive \(\kappa E^2/2\). Die vollständige positive Spektralverteilung des Vektors \(B\Psi_0\), gemessen oberhalb \(2E_0\), ist

\[
\boxed{d\mu_B(w)=64\iint
\delta\bigl(w-u-v-\kappa/2\bigr)\,d\nu_-(u)\,d\nu_+(v).}
\]

Hier ist die Delta-Schreibweise die Kurzform für das unter \((u,v)\mapsto u+v+\kappa/2\) transportierte Produktmaß. Die Formel folgt, weil der Austausch an einer Bank entfernt und an der anderen addiert; die beiden spektralen Matrizen sind durch die innere Symmetrie diagonal. Sie ist keine Gleichsetzung mit einem neu angenommenen freien Teilchen.

Damit folgt

\[
\boxed{\inf\operatorname{supp}\mu_B>0.337373\Delta+\kappa/2.}
\]

Der gesamte erste Moment der **Materieenergie** ist

\[
64[a(1-\nu)+\nu a]=64a=\Delta\bar b-E_0.
\]

Die mittlere Anregungsenergie des normierten gerichteten Austauschzustands lautet deshalb exakt

\[
\boxed{\overline E_B=\frac{\Delta\bar b-E_0}{2\bar b-\bar b^2/16}+\kappa/2.}
\]

Mit den v1.6.4-Grenzen liegt der Materieanteil zwischen ungefähr **0.992047339 Δ und 1.219121394 Δ**; die exakten rationalen Grenzen stehen im Prüfbericht. Die elektrische Energie \(\kappa/2\) kommt hinzu.

**Das ist die erste präzise Antwort auf die Frage nach der Gegenstelle:** Der niedrige Entnahmepol liefert nur die eine Seite. Der geschlossene Austausch aus zwei Grundzuständen benötigt zugleich das höhere Additionsspektrum der anderen Seite. Die räumliche Austauschantwort wird durch deren Faltung bestimmt.

---

## 4. Transport eines bereits vorhandenen niedrigen Lochs

Sei \(P_h\) der vorhandene Projektor auf das niedrige 64-dimensionale Entnahmemultiplet. Wähle

\[
|h_r\rangle=Z^{-1/2}P_h f_r|\Omega\rangle,
\qquad\langle h_r|h_s\rangle=\delta_{rs}.
\]

Dann ist \(\langle\Omega|f_r^\dagger|h_s\rangle=\sqrt Z\delta_{rs}\). Für den Raum, in dem genau eine Bank ein solches Loch trägt, hat der angegebene bilineare Austausch daher die **exakte Kompression**

\[
P_1(\tau B+\bar\tau B^\dagger)P_1
=-Z\sum_r(\tau d_{x,r}^{\dagger}U d_{y,r}
+\bar\tau d_{y,r}^{\dagger}U^\dagger d_{x,r}).
\]

Die \(d^\dagger\) bezeichnen hier Lochübergänge im Ein-Loch-Raum. Das Vorzeichen folgt aus der fermionischen Ordnung; eine relative Basisphase kann es auf einem einzelnen Link umlegen. Ein Loch bewegt sich entgegengesetzt zum übertragenen Fermion.

Insbesondere

\[
\boxed{|\tau_{\rm Loch}|=Z|\tau|>0.880076280689\ldots|\tau|.}
\]

Das ist ein Anschluss der bereits vorhandenen spektralen Größe \(Z\) an eine konkrete räumliche Matrixamplitude. Es ist **keine** Aussage, dass die volle Zeitentwicklung mit höchstens zwölf Prozent Fehler in diesem Raum bleibt. Dafür müsste insbesondere \((1-P_1)H_{xy}P_1\) und eine passende spektrale Trennung kontrolliert werden. Diese Mehrbanken-Abschätzung liegt nicht vor.

### Zwei notwendige Korrekturen einer zu schnellen Interpretation

**Ladungsgegenstelle:** Ein einzelnes Loch und eine unveränderte zweite Bank haben Gesamtladung \(127\). Bei zwei Hintergrundladungen 64 ist \(G_x+G_y=-1\); ein solcher Zustand gehört nicht zum neutralen geschlossenen Zwei-Orte-Sektor. Benötigt wird entweder eine äußere Gegenladung/Randfluss, ein anders erklärter Hintergrund mit Summe 127 oder eine zusätzliche positive Anregung. Der Link allein kann keine fehlende Gesamtladung aufnehmen.

**Keine automatische volle Fockalgebra:** Auf \(\operatorname{span}\{\Omega,h_1,\ldots,h_{64}\}\) sind die gefilterten Felder

\[
F_r=P_hf_rP_\Omega=\sqrt Z|h_r\rangle\langle\Omega|.
\]

Für \(r\ne s\) gilt

\[
\{F_r,F_s^\dagger\}=Z|h_r\rangle\langle h_s|\ne0.
\]

Sie sind dort Übergangsoperatoren mit ausgeschlossenen weiteren Besetzungen, keine 64 vollständigen CAR-Moden. Eine Viel-Loch-Theorie muss die weiteren nativen Ladungssektoren tatsächlich einbeziehen. Auch die spektralen Filter \(P_h,P_\Omega\) sind zunächst mathematisch definierte Projektoren, keine nachgewiesenen Compileroperationen.

---

## 5. Kohärenzerhaltende Aufzeichnung: Was das Register speichern darf

### 5.1 Das Linkregister bleibt Teil des Quantenzustands

Ein elementarer kohärenter Übergang hat schematisch die Form

\[
\alpha|\text{vorher},e\rangle+\beta|\text{nachher},e+1\rangle.
\]

Die Ladungs- und Flusszweige sind verschränkt. Der Gesamtzustand bleibt kohärent. Eine passende physikalische Beobachtung ist das gauge-invariante \(B+B^\dagger\), beziehungsweise der Strom. Aus der Gleichung für \(N_y\) folgt

\[
\dot N_y=J_{x\to y},\qquad
J_{x\to y}=i(\bar\tau B^\dagger-\tau B),\qquad\dot E=J_{x\to y}.
\]

Die Aufzeichnung erfüllt somit dieselbe Bilanz wie der Stofftransport. Die bloße reduzierte Materiedichte, nachdem der Link ignoriert wurde, zeigt nicht alle physikalisch verfügbaren relativen Kohärenzen.

Wird \(E\) dagegen gemessen und das Ergebnis anschließend verworfen, wirkt die Dephasierung \(\rho\mapsto\sum_eP_e\rho P_e\). Da \(B\) den Fluss ändert, verschwinden seine Erwartungswerte danach. Eine jederzeit klassisch lesbare vollständige Flusshistorie ist deshalb nicht ohne Weiteres eine interferenzerhaltende History.

### 5.2 Interne Austauschalternativen müssen dieselbe relevante Aufzeichnung behalten

Für Alternativen \(p,q\) mit Amplituden \(a_p,a_q\) und Registerzuständen \(r_p,r_q\) wird der Interferenzterm mit

\[
\langle r_q|r_p\rangle
\]

multipliziert. Für unveränderte relative Kohärenz muss dieses Überlapp einschließlich seiner Phase passend gleich eins sein. Eine orthogonale Aufzeichnung von `ab` und `ba` löscht genau deren Interferenz.

Der vorliegende Link ist für mehrere innere Komponenten mit **derselben Nettoübertragung** blind: Alle benutzen dasselbe \(U\). Das ist eine konkrete Möglichkeit, die innere Unterscheidung nicht im Register abzulegen. Es ist noch kein Nachweis, dass jede ausgedehnte History auf einem ganzen Netz diese Eigenschaft besitzt.

### 5.3 Ein echter Unterschied zwischen Innenalternativen und räumlich verschiedenen Wegen

Zwei Wege mit denselben Endpunkten, aber unterschiedlichem Umlauf können sich in einem Wilson-Loop-Operator \(W\) unterscheiden. Ihre Registerüberlappung ist dann \(\langle\chi|W|\chi\rangle\), nicht automatisch eins.

Im einfachen Schleifenrotor \(\ell^2(\mathbb Z)\) hat der bilaterale Shift \(W\) keinen normalisierbaren Eigenvektor. Exakte Einheitssichtbarkeit für einen solchen nichttrivialen Schleifenunterschied folgt daher nicht aus einem beliebigen endlichen Energiezustand. Für

\[
|\chi_R\rangle=(2R+1)^{-1/2}\sum_{e=-R}^R|e\rangle
\]

gilt beispielhaft

\[
\langle\chi_R|W|\chi_R\rangle=\frac{2R}{2R+1},
\qquad\langle E^2\rangle=\frac{R(R+1)}3.
\]

Diese Zustände zeigen eine kontrollierte Annäherung, mit wachsendem Energieaufwand. Auf dem vollständigen physikalischen Graphen müssen dazu auch die korrelierten Ladungen beziehungsweise der zulässige Schleifenfreiheitsgrad mitgeführt werden. Ein Protokoll kann einen Wegunterschied eventuell kohärent zurückführen; dieses zusätzliche Protokoll ist dann ausdrücklich zu beweisen.

---

## 6. Tatsächlich ausgeführter Austausch aus dem älteren Quellmodell

Um nicht bei einem neu aufgeschriebenen Hamiltonoperator stehenzubleiben, wurde der vorhandene Round37-Generator auf einem offenen Zwei-Orte-Graphen erneut ausgewertet. Er behält beide Spezies \(L,H\), alle drei ursprünglichen Koppelterme, ihre Adjungierten, die Onsite-Energien und die elektrische Energie. Zwei-Schritt-Pfade zwischen verschiedenen Endpunkten gibt es auf diesem Graphen nicht; die Onsite-Rückwege bleiben erhalten.

Die Parameter sind exakt

\[
a_0=1/12,\quad\eta=1/2,\quad\beta=1/4,
\quad\kappa=1/100,\quad M=4.
\]

### 6.1 Vollständiger physikalischer Raum statt Rotorabschneidung

Die Reihenfolge der Fermionmoden lautet \((L_x,L_y,H_x,H_y)\). Die Gauss-Gleichungen erzwingen

\[
N_x+N_y=2,\qquad E=1-N_x=N_y-1.
\]

Es gibt genau sechs Belegungsmasken \(3,5,6,9,10,12\), mit Flüssen \(0,-1,0,0,1,0\). Dies ist auf diesem Baumgraphen der **gesamte** neutrale physikalische Hilbertraum. Dass nur drei Flusswerte auftreten, folgt aus der Ladungsbedingung und ist keine eingesetzte Abschneidung eines Schleifenrotors.

In dieser Reihenfolge liefert die Originalquelle exakt

\[
H=\begin{pmatrix}
1/288&1/24&0&0&-1/24&0\\
1/24&57697/14400&1/12&0&0&-1/24\\
0&1/12&2305/576&0&0&0\\
0&0&0&2305/576&1/12&0\\
-1/24&0&0&1/12&57697/14400&1/24\\
0&-1/24&0&0&1/24&8
\end{pmatrix}.
\]

Eine unabhängige Implementierung der CAR-Vorzeichen, Flussänderungen und diagonalen Energien liefert dieselbe Matrix für jeden ihrer sechs Ausgangszustände.

### 6.2 Anfang, Gegenstelle und Ergebnis

Der Anfangszustand ist

\[
|L_x,H_y;E=0\rangle,
\]

also eine in der Quellbeschreibung zugelassene vorbereitete L/H-Belegung. Als Ziel wird

\[
|0_x,L_yH_y;E=1\rangle
\]

abgelesen. Das L-Fermion hat die Verbindung überquert. Die Gegenstelle enthält anschließend beide Spezies; die gesamte Ladung bleibt zwei. Dies ist keine räumliche Ableitung aus dem neuen \(\Omega\).

| Zeit in den Quelleneinheiten | Wahrscheinlichkeit des vollständigen Zielzustands |
|---:|---:|
| 1 | 0.006924792654825 |
| 12 | 0.707587070196364 |
| 19 | **0.998717948143930** |

Diese Zahlen stammen aus rationaler Taylorrechnung für die gesamte Matrix. Für \(H-4I\) wird eine obere Zeilensummennorm verwendet. Der Rest ab Grad \(p+1\), mit \(x=|s|\|H-4I\|\), ist für \(x<p+2\) beschränkt durch

\[
\varepsilon\le\frac{x^{p+1}}{(p+1)!}\frac1{1-x/(p+2)}.
\]

Benutzt wurden die Grade 70, 220 und 300. Die Fehlerbudgets für normbeschränkte Observablen liegen unter \(6.1\cdot10^{-59}\), \(1.8\cdot10^{-50}\) und \(2.0\cdot10^{-48}\). Die angezeigten Dezimalzahlen werden nur mit einem gröberen absoluten Rundungsbudget von \(10^{-14}\) beansprucht. Der ausgeschriebene analytische Rest ist größer zu gewichten als ein bloßer kleiner Gleitkommaresidual.

Die gauge-invariante gerichtete Kohärenz \(\langle Uc_{L,y}^{\dagger}c_{L,x}\rangle\) ist vor einer Flussmessung ungleich null, beispielsweise bei Zeit 12 ungefähr \(-0.02122777+0.45425097i\). Nach Flussdephasierung ist sie exakt null. Damit ist auch der Unterschied zwischen kohärentem Verbindungsregister und gelesener klassischer Aufzeichnung im selben Quellmodell nachgewiesen.

**Reichweite:** erfolgreicher endlicher Austausch in einem bereits erklärten räumlichen Parent. Keine Ausführung der großen 3D-Fensterrechnung, kein neuer 64-Moden-Banklauf, keine experimentelle Messung.

---

## 7. Was den ursprünglichen Zusammenhang weiterhin verhindert

In der ursprünglichen lokalen Bank bewahren \(b^\dagger ff+\mathrm{h.c.}\) und lokale zahlbewahrende Clock-Operationen die lokale Fermionparität

\[
\Pi_x=(-1)^{N_{f,x}}.
\]

Auch ein reiner Bosonentransport zwischen getrennten Banken ändert \(\Pi_x\) nicht. Produkte, Grenzwerte und unter dieser Algebra gebildete Kontrolloperationen bleiben mit \(\Pi_x\) verträglich. Der neue Fermiontransport \(B\) ändert hingegen die Parität an beiden Enden.

**In dieser angegebenen Operationsklasse ist der gewünschte ungerade Einzeltransfer daher nicht erzeugbar.** Das ist ein exakter Hindernissatz für diese Klasse. Er schließt einen größeren tatsächlich vorhandenen Compiler mit zusätzlichen bankübergreifenden Operationen nicht aus.

Die Quellen enthalten somit beide Seiten der fehlenden Identifikation:

- einen geprüften lokalen Zustand mit Ladungsantwort;
- einen vorhandenen, anders eingeführten räumlichen Parent mit tatsächlichem Austausch.

Die hier bewiesenen Norm-, Spektral- und Projektionsformeln verbinden ihre mathematischen Schnittstellen. Um daraus einen ursprünglichen gemeinsamen Prozess zu machen, fehlt eine **quellengebundene Operation**, die den Link und \(B\) wirklich erzeugt oder einen äquivalenten Übergang herleitet. Ein neuer Matrixeintrag oder eine bloße Umbenennung der beiden Parent-Modelle erfüllt das nicht.

### Der nächste entscheidende Nachweis

Eine konkrete ursprüngliche Operation \(W_{xy}\), mit definiertem Hintergrund und kohärentem Register, muss gleichzeitig:

1. auf zwei operational unterschiedenen Teilen wirken und deren lokale Paritäten gemeinsam ändern können;
2. die tatsächliche Ladung \(N_f+2N_b\) und die physikalische Gauss-Bedingung erhalten;
3. einen nichtverschwindenden Austauschmatrixeintrag im beschriebenen nativen Zustandsraum liefern;
4. das Adjungierte als ebenfalls zulässige Operation besitzen;
5. die Gram-Matrix der interferierenden Innenalternativen erhalten;
6. den Übergang zur Mehrbanken-Zeitentwicklung mit kontrollierter Abweichung belegen.

Erst danach sind Auswahl des Graphen, räumliche Dimension, Kontinuumsgrenze und Gravitation die nächsten Fragen. Die hier fehlende erste Operation wird durch diese späteren Ziele nicht ersetzt.

---

## 8. Arithmetische Erweiterung mit der richtigen Zustandszählung

### 8.1 Endlich viele zusätzliche Links beseitigen die bewiesene Grenze nicht

Für \(L\) Banken, \(m\) ganzzahlige Rotorlinks und \(\kappa>0\) folgt aus der vorhandenen Bankabschätzung \(\sum_A P_A^\dagger P_A\le480\) und der beschränkten Kopplung

\[
H\ge\frac\Delta2\sum_xN_{b,x}+\frac\kappa2\sum_eE_e^2-C,
\quad C=\frac{960Lg^2}{\Delta}+64\sum_e|\tau_e|.
\]

Die Zahl der Zustände unter Energie \(\mathcal E\) ist daher höchstens

\[
\boxed{
N_H(\mathcal E)\le 2^{64L}
\binom{\left\lfloor2(\mathcal E+C)/\Delta\right\rfloor+60L}{60L}
\left(2\left\lfloor\sqrt{2(\mathcal E+C)/\kappa}\right\rfloor+1\right)^m
}
\]

für \(\mathcal E+C\ge0\). Die Gauss-Bedingung kann diese obere Schranke nur verkleinern. Der Schrankenoperator hat kompakte Resolvente; die Formabschätzung und das Minimaxprinzip übertragen die Zählobergrenze auf den selbstadjungierten, nach unten beschränkten Kandidaten.

Bei festen \(L,m\) wächst die Schranke höchstens wie \(\mathcal E^{60L+m/2}\). Ein voller arithmetischer Generator \(H_{\rm ar}|n\rangle=\log n\,|n\rangle\) besitzt dagegen \(\lfloor e^{\mathcal E}\rfloor\) Zustände unter dieser Energie. Auch mit positivem festem Energie-Maßstab und endlicher Verschiebung bleibt der Unterschied exponentiell gegen polynomial.

**Folge:** Der neue Austauschlink liefert eine räumliche Erweiterung, aber keine Lösung des arithmetischen Zustandsproblems auf einem festen endlichen Graphen.

### 8.2 Unendlich viele identische Banken lösen das Problem ebenfalls nicht automatisch

Ein einfacher allgemeiner Satz lautet: Gibt es für einen nach unten beschränkten selbstadjungierten \(K\) unendlich viele orthonormale Zustände \(\psi_j\) mit gleichmäßig beschränkter mittlerer Energie \(\langle K\rangle_j\le C_0\), so gilt für jedes \(\beta>0\)

\[
\operatorname{Tr}e^{-\beta K}\ge
\sum_j\langle\psi_j,e^{-\beta K}\psi_j\rangle
\ge\sum_j e^{-\beta C_0}=\infty.
\]

Die zweite Ungleichung folgt aus Jensen für das Spektralmaß. Sie gilt auch mit Form-Erwartungswerten.

Auf unendlich vielen entkoppelten identischen Banken kann man eine feste endliche Anregung an beliebig viele verschiedene Orte setzen. Bei einer festen Ladungsbedingung kann man stattdessen eine gleiche neutrale Anregung oder ein gleiches endliches Ladungspaar an disjunkten Stellen benutzen. Diese orthogonalen Anregungen haben dieselbe endliche Energie. Ein beschränkter effektiver Einteilchen-Hoppingoperator auf einem unendlichen Graphen löst dieses Problem ebenfalls nicht: sein gesamtes Band bleibt energetisch beschränkt.

Dieser Satz wird nicht ohne Prüfung auf jeden wechselwirkenden thermodynamischen GNS-Generator übertragen. Für die naive Wiederholung und die bezeichneten effektiven Bänder ist die fehlende globale Spur jedoch bereits sichtbar. Algebraische thermodynamische Gleichgewichtszustände oder Zustandsdichten pro Volumen sind andere Objekte als die globale Zeta-Spur.

### 8.3 Eine konsistente wachsende Vergleichsfamilie

Eine mathematisch passende, schon bekannte arithmetische Konstruktion ist

\[
\mathcal F_r=\bigotimes_{j=1}^r\ell^2(\mathbb N_0),
\qquad H_r=\sum_{j=1}^r(\log p_j)N_j.
\]

Die Einbettung fügt neue Moden im Vakuum an. Für jede endliche Besetzungsfolge gilt

\[
\sum_j n_j\log p_j=\log\Bigl(\prod_jp_j^{n_j}\Bigr).
\]

Auf der vollständigen bosonischen Fockbasis über den Primmoden liefert die eindeutige Primzerlegung den selbstadjungierten diagonalen Operator mit Energien \(\log n\). Für reelles \(\beta>1\) gilt monoton

\[
\lim_{r\to\infty}\operatorname{Tr}_{\mathcal F_r}e^{-\beta H_r}
=\prod_p(1-p^{-\beta})^{-1}
=\sum_{n\ge1}n^{-\beta}=\zeta(\beta).
\]

Für \(\beta\le1\) ist die globale positive Spur divergent. Analytische Fortsetzung ist keine konvergente Gibbs-Spur bei diesen Temperaturen.

Der Unterschied zu identischen räumlichen Banken ist deutlich: Die Energieskala der neuen Primmoden wächst. Die unendlich vielen unabhängigen Kanäle mit Energie \(\log p\) sind hier eine zusätzliche arithmetische Vorgabe. Auf diesem Weg werden die Primzahlen nicht aus dem nativen Austausch hergeleitet. Die Konstruktion ist ein Vergleichsobjekt für die nötige Erweiterung und kein neuer Faktorisierungsalgorithmus.

Die Beziehung von Zeta-Partitionsfunktionen und arithmetischer statistischer Mechanik ist etablierte Vorarbeit, insbesondere [Bost–Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf). Hier wird nur die ausgeschriebene Fock-/Eulerprodukt-Realisierung verwendet; ihre Identifikation mit einem vollständigen Bost–Connes-Observablenmodell wird nicht behauptet.

### 8.4 Faktorisierung bleibt eine gesonderte Leistung

Die Abbildung eines schon bekannten Faktorexponentenvektors auf \(n\) ist einfach. Die Umkehrung für binär gegebenes \(n\) ist gerade Faktorisierung. Die Prüfrechnung rekonstruiert 500 kleine ganze Zahlen aus durch eine Standardbibliothek bestimmten Faktoren; das ist eine Kontrolle des Wörterbuchs und kein Geschwindigkeitsnachweis.

Die nächste arithmetische Verpflichtung bleibt eine quellengebundene wachsende Darstellung mit erklärten Einbettungen, Energieskalen und Operationskosten. Eine endliche Zählgleichheit oder ein Zeta-Name liefert weder vollständige Weil-Positivität noch effiziente native Faktorisierung.

---

## 9. Prüfung, Herkunft und bekannte Grenzen des Suchstands

Das neue Prüfprogramm führt **753 Prüfbedingungen** aus. Darin enthalten sind viele einzelne kleine Zustands- und Rekonstruktionskontrollen; dies sind nicht 753 unabhängige mathematische Sätze. Normaler und optimierter Python-Lauf liefern bytegleiche JSON-Dateien.

Die Prüfung umfasst:

- die vollständige 60×60-Gram-Matrix aus den tatsächlichen 480 nativen Tensoreinträgen und die exakte Zerlegung des Sektors \(N=2\);
- den vollständigen sechs-dimensionalen neutralen Quellsektor und eine unabhängige CAR-/Fluss-Auswertung;
- rationale vollständige Zeitentwicklung mit analytischem Rest;
- eine unabhängige kleine Fockkontrolle der Produktgrundzustands-Normformel;
- die rationalen neuen Grenzen aus den v1.6.4-Eingaben;
- Aufzeichnungs-Gegenkontrollen und die verletzte volle CAR-Behauptung für die gefilterten Übergänge;
- endliche arithmetische Wörterbuch- und Eulerproduktkontrollen.

Das Paket enthält die benutzte unveränderte Quellkopie, relevante Quellauszüge als vollständige Dokumente, Prüfer, Ergebnisse und SHA-256-Manifest. Die Vorgängerdokumente bleiben unverändert. Die frühere vollständige Replay-Prüfung des nativen Pakets wird nicht als neue Zwei-Banken-Simulation ausgegeben.

Der strukturelle Codegraph wurde zur gezielten Quellsuche benutzt. Der RH-Forschungskatalog wurde auf verwandte Ansätze und bekannte Gegenbefunde geprüft. Relevant bleiben unter anderem `r647 / STRUCTURAL_MISMATCH` für die dortige endliche Faktorisierungsdarstellung und die dokumentierte fehlende native Identifikation im `hecke_index_theorem.md`. Die vorliegende Konstruktion erhebt gerade keinen aus diesen endlichen Modellen gewonnenen Effizienz- oder Weil-Positivitätsanspruch.

Der Katalogpfad `riemann-zeta → explicit-formula → weil-quadratic-form → weil-positivity` beschreibt Beziehungen und offene Verpflichtungen. Er ist kein Beweis aus einer Partitionsfunktion. Ein erster Suchversuch mit dem nicht vorhandenen Konzeptnamen `bost_connes` wurde durch die vorhandenen IDs ersetzt.

Der Gesamtrefresh des RH-Index scheitert weiterhin an der fehlenden historischen Quelle `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`. Der fehlende Ordner wurde nicht künstlich angelegt, und keine Quellenprüfung wurde durch geänderte Pins grün gemacht. Die gezielt gelesenen Originaldateien sind überprüfbar; ein vollständiger aktueller Gesamtkorpus wird nicht behauptet.

Als externe Einordnung des Austauschbausteins wurde zusätzlich [Mazzola et al., *Gauge invariant quantum circuits for U(1) and Yang–Mills lattice gauge theories*](https://arxiv.org/abs/2105.05870) gelesen. Dort stehen matter-link-matter-Terme, Gauss-Bedingungen und gauge-invariante Zustandspräparation im bekannten Gitterrahmen. Das stützt die fachliche Einordnung, ersetzt aber nicht den fehlenden Herkunftsnachweis innerhalb TFPT.

## 10. Präzises Fazit

**Der ursprüngliche innere Austausch ist im unveränderten Modell mit Anfangszustand, Gegenstelle, Adjungiertem, Ladungsbilanz und kohärenter Kanalaufzeichnung exakt identifiziert.** Die Interpretation seiner beiden Teile als räumliche Orte folgt daraus noch nicht.

**Für einen zusätzlichen räumlichen Link sind dieselben Bestandteile ausdrücklich konstruiert.** Unter dieser erklärten Erweiterung erzwingt die tatsächliche native Zustandsantwort einen nichtverschwindenden Austausch und bestimmt dessen Zweibanken-Spektralmaß als Faltung. Für einen vorhandenen niedrigen Lochzustand ergibt sie den exakten projizierten Transportfaktor \(Z\).

**Offen bleibt die ursprüngliche Auswahl und Erzeugung dieses Austauschs.** In der bisher angegebenen lokalen Operationsklasse verhindert die getrennte Parität den erforderlichen Transfer. Der nächste Fortschritt muss genau an dieser Stelle eine tatsächliche Operation liefern. Gravitation, gemeinsamer arithmetisch-physikalischer Ursprung und effiziente native Faktorisierung sind durch die vorliegenden Ergebnisse weiterhin nicht bewiesen.
