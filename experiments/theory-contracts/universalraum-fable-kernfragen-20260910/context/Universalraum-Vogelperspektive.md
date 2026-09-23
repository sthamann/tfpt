# Universalraum: gemeinsame Prozessstruktur, Gesetzesauswahl und die Grenzen der Vereinheitlichung

**Ausarbeitung vom 10. September 2026.** Grundlage ist die eingereichte Fassung von *Universalraum und TFPT*, Version 1.0, mit 293 PDF-Seiten. Die hier ausgeschriebenen zusätzlichen Folgerungen betreffen den mathematischen Begriff des Universalraums und zwei konkrete Auswahlfragen. Eine vollständige physikalische Fundamentaltheorie, ein RH-Beweis oder ein neuer allgemeiner effizienter Faktorisierer wurden nicht gewonnen.

**Das Ergebnis vorweg.** Der tragfähige Universalraum ist die Gesamtheit der unterscheidbaren, komponierbaren Prozessantworten innerhalb eines ausdrücklich festgelegten experimentellen Vertrags. Dieser Begriff lässt sich mathematisch abschließen. Er erklärt, wann verschiedene Darstellungen dieselbe Sache beschreiben. Die Auswahl der tatsächlich geltenden Naturgesetze bleibt eine zusätzliche Aufgabe. Insbesondere wählt der im PDF untersuchte Minimax-Ansatz die bisherigen Kopplungen nur unter einer bereits eingeschränkten Operationsfamilie. Und die universelle Geschichtskodierung repräsentiert eine vorher gewählte Dynamik; sie bestimmt diese Dynamik nicht.

Die Umrsuchung führt diese Grenze über eine bloße Bestandsaufnahme hinaus: Sie löst die gemeinsame Minimierung über die zusätzliche HH-Kopplung, zeigt deren Verhalten unter zwei ausdrücklich zusätzlich eingeführten Strafkosten und beweist einen allgemeinen Ausschluss für eine feste, ungeänderte Isometrie als Ersatz aller Zieldynamiken. Außerdem wird eine präzise positive Vervollständigung des Universalraumbegriffs formuliert. Die mathematischen Beiträge sind elementare Folgerungen beziehungsweise bekannte Strukturprinzipien in der hier passenden Form, ohne weltweiten Neuheitsanspruch.

**1. Was die Vogelperspektive sichtbar macht**

Im bisherigen Projekt laufen mehrere verschiedene Fragen unter demselben Namen:

| Frage | Was als Antwort nötig ist |
|---|---|
| Können algebraische, geometrische und arithmetische Beschreibungen dieselben Vorgänge darstellen? | Gemeinsame Schnittstellen und Abbildungen, welche die relevanten Operationen und Antworten erhalten. |
| Welche Information ist für die Zukunft erforderlich? | Eine gegenüber allen erlaubten Fortsetzungen ausreichende Prozessbeschreibung. |
| Welche Handlungen kann eine reale Quelle ausführen? | Ein Präparations-, Steuerungs- und Auslesevertrag aus tatsächlichen Wechselwirkungen. |
| Warum gilt gerade dieses Naturgesetz? | Ein unabhängig begründetes Auswahlprinzip für Modellklasse, Dynamik und nötige Anfangsdaten. |
| Wie teuer ist die Ausführung? | Eine uniforme Ressourcenanalyse der konkreten Realisierung. |
| Folgt daraus RH oder effiziente Faktorisierung? | Die jeweiligen globalen beziehungsweise algorithmischen Beweise. |

Diese Fragen hängen zusammen. Keine davon darf jedoch als bereits gelöst gelten, nur weil eine andere beantwortet ist. Ein gemeinsames Zahlenformat ist eine schwächere Leistung als ein erhaltener Prozess. Ein erhaltener Prozess ist eine schwächere Leistung als seine native Ausführung. Die native Ausführung eines ausgewählten Modells ist wiederum etwas anderes als dessen fundamentale Auswahl.

Eine vollständige Umkoordinatisierung kann weder einen falschen Modellwert korrigieren noch von allein neue Faktorinformation erzeugen. Bei einer invertierbaren Abbildung müssen Dynamik und Auslese mittransformiert werden; dann bleiben sämtliche Antworten gleich. Verbesserungen verlangen eine zusätzliche wirksame Operation, eine andere Informationsquelle, veränderte Dynamik oder eine nachweislich günstigere Darstellung der Ausführungskosten.

**2. Ein abgeschlossener allgemeiner Begriff des Universalraums**

Fixiere eine Klasse kompatibel typisierter Prozesse \(\mathcal P\) und eine Klasse zulässiger Experimente \(\mathcal C\). Ein Experiment kann Vorbereitungen, Zwischeninterventionen, Speicher, Referenzen, adaptive Entscheidungen und abschließende Messungen enthalten. Die Klasse muss unter den beanspruchten zulässigen Einsetzungen abgeschlossen sein. Ein betrachteter Ausgang umfasst alle für das Experiment relevanten Ergebniszweige, auch Fehlschläge.

Jedem Prozess ordnen wir seine gesamte Antwortfunktion zu:

\[
\operatorname{Ev}(P): C\longmapsto p_C^P.
\]

Hier ist \(p_C^P\) die vollständige Ausgangsverteilung des Experiments \(C[P]\). Definiere

\[
P\simeq_{\mathcal C}Q
\quad\Longleftrightarrow\quad
p_C^P=p_C^Q\ \text{für jedes }C\in\mathcal C.
\]

Dann ist

\[
\mathfrak U_{\mathcal P,\mathcal C}
=\mathcal P/\simeq_{\mathcal C}
\cong\operatorname{Ev}(\mathcal P)
\]

der Universalraum des bezeichneten experimentellen Vertrags. Er ist zunächst ein Raum von Verhaltensklassen. Eine lineare Struktur, ein Hilbertraum, eine Tensorzerlegung, eine Raumzeit oder ein physikalisches Maß sind damit noch nicht behauptet.

**Satz A: Vollständigkeit, Minimalität und Komposition.** Die Antwortfunktion ist eine vollständige Darstellung der bezeichneten experimentellen Unterscheidungen. Jede andere ausreichende Darstellung bildet auf sie ab. Erlaubte Fortsetzungen wirken wohldefiniert auf den Äquivalenzklassen.

**Beweis.** Sei \(F:\mathcal P\to X\) eine ausreichende Darstellung: Aus \(F(P)\) lassen sich alle \(p_C^P\) bestimmen. Dann impliziert \(F(P)=F(Q)\) die Gleichheit sämtlicher Antworten. Deshalb ist

\[
\pi:F(\mathcal P)\longrightarrow\mathfrak U_{\mathcal P,\mathcal C},
\qquad \pi(F(P))=[P]
\]

wohldefiniert und surjektiv. Hat \(F\) außerdem keine zusätzlichen unterscheidbaren Zustände für äquivalente Prozesse, ist \(\pi\) bijektiv. Für eine zulässige Fortsetzung \(D\) folgt aus \(P\simeq Q\) auch \(D[P]\simeq D[Q]\): Ein unterscheidender späterer Test wäre durch Einsetzen von \(D\) bereits ein zulässiger Test für \(P,Q\). Genau dafür wird der Kontextabschluss gebraucht. ∎

Das ist ein präziser universeller Eigenschaftssatz. Er setzt keine besondere TFPT-Arithmetik voraus. Sein Inhalt ist: Eine Darstellung darf genau diejenigen Unterschiede vergessen, die in keinem zugelassenen Experiment mehr wirksam werden können.

Im endlichen linearen Spezialfall liefert das PDF bereits die stärkere Minimalrealisierung

\[
V_{\mathrm{pred}}=R/N,
\quad
R=\operatorname{span}\{A_h\rho_0\},
\quad
N=\{v\in R:\ell(A_wv)=0\ \forall w\}.
\]

Die Dimension ist der Rang der Zukunfts-Hankelmatrix. Das ist ein minimaler linearer Vorhersageraum. Seine Dimension ist nicht automatisch die kleinste physische Speicherdimension; seine Koordinaten müssen keine Dichtematrizen sein. Diese Einordnung entspricht der etablierten Theorie gewichteter Automaten und der Quantenprozessbeschreibung. [Externe Einordnung: Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, [Primärquelle](https://arxiv.org/abs/2009.01217); Chiribella, D'Ariano und Perinotti, *Theoretical framework for quantum networks*, [Primärquelle](https://arxiv.org/abs/0904.4483).]

**3. Warum der ganze Prozess die richtige Einheit ist**

Zwei Zustände können heute dieselbe sichtbare Dichte besitzen und morgen unterschiedliche Antworten erzeugen, wenn ihre Umgebung erneut eingreift. Das PDF gibt das elementare Beispiel \(|00\rangle\) und \(|01\rangle\): Das erste Qubit ist in beiden Fällen gleich. Nach SWAP und Messung dieses Qubits sind die beiden Fälle sicher unterscheidbar.

Damit ist auch erklärt, warum gleiche reduzierte Einzelkanäle keine vollständige mehrzeitige Beschreibung garantieren. Die Wirkung eines Eingriffs hängt unter Umständen von einer bereits korrelierten Umgebung ab. Eine Messung ist zusätzlich zu ihrer Wahrscheinlichkeit durch ihren ausgegebenen Zustand bestimmt. Bei späterer Wiederverwendung einer Referenz müssen ihre Korrelationen mitgeführt werden. Die operationelle Bedeutung solcher Gedächtniseffekte ist in der Process-Tensor-Literatur ausdrücklich untersucht. [Pollock et al., *Operational Markov condition for quantum processes*, [Primärquelle](https://arxiv.org/abs/1801.09811).]

Es folgt jedoch keine Pflicht, jede Umgebung ewig aufzubewahren. Ein Register darf verworfen werden, sobald seine spätere Kopplung und Auslese ausgeschlossen sind oder eine ausreichende Ersatzbeschreibung bewiesen ist. Das Kriterium ist zukünftig wirksame Information.

Auch die Unterschiede zwischen klassischen und quantenmechanischen Antworten bleiben erhalten. Eine skalare Spur ist nicht automatisch eine Wahrscheinlichkeit. Die relative Phase eines kontrolliert gerouteten Aufrufs kann sichtbar sein, obwohl dessen gewöhnlicher Kanal dieselbe globale Phase vergessen hat. Die erlaubte kontrollierte Schnittstelle muss deshalb eigens feststehen.

**4. Ein Universalraum mit wachsenden Beobachtungsmöglichkeiten**

Bei einem festen Vergleichsträger und einer Erweiterung der Tests von \(\mathcal C\) zu \(\mathcal C'\) gilt

\[
P\simeq_{\mathcal C'}Q\ \Longrightarrow\ P\simeq_{\mathcal C}Q.
\]

Es gibt eine natürliche Abbildung vom feineren zum gröberen Verhaltensraum. Die verlorene Information lässt sich aus dem gröberen Raum im Allgemeinen nicht wiedergewinnen. Werden gleichzeitig neue Quellen oder Träger zugelassen, ist zunächst eine gemeinsame Vergleichsschnittstelle erforderlich; die Abbildung folgt dann nicht automatisch. Diese Einschränkung steht schon in Q019.

Eine nützliche zusätzliche Präzisierung betrifft unendliche Vervollständigung. Angenommen, eine abzählbare Familie \(C_1,C_2,\ldots\) mit jeweils endlich vielen Ausgängen erfasst die beanspruchten Unterscheidungen. Auf Antwortfunktionen definiere

\[
d(p,q)=\sum_{i=1}^{\infty}2^{-i}\operatorname{TV}(p_{C_i},q_{C_i}).
\]

Der Umgebungsraum \(\prod_i\Delta(O_i)\) ist kompakt und durch diese Metrik vollständig. Der Abschluss von \(\operatorname{Ev}(\mathcal P)\) darin ist folglich eine mathematisch wohldefinierte Vervollständigung. Jede Cauchy-Folge von Antworten besitzt dort einen eindeutigen Grenzwert. Geschlossene Normierungs- und Kompatibilitätsgleichungen bleiben erhalten.

Der Preis dieser Aussage ist sichtbar: Der Grenzpunkt braucht keine Realisierung innerhalb der ursprünglich zugelassenen Quellen- oder Ressourcenklasse zu besitzen. Betrachte als einfaches Beispiel die deterministischen Bitfolgen, die irgendwann nur noch Nullen ausgeben. Die Folgen mit jeweils \(n\) anfänglichen Einsen konvergieren in allen endlichen Präfixtests zur Folge aus lauter Einsen. Jeder endliche Test passt zu einem zugelassenen Prozess; der Grenzprozess gehört trotzdem nicht zu der festgelegten Klasse.

Noch stärker: Endliche Programme können jeden vorgegebenen endlichen Bitpräfix hart kodieren. Es gibt aber nur abzählbar viele endliche Programme und überabzählbar viele unendliche Bitfolgen. Daher folgt aus der Realisierbarkeit jedes endlichen Präfixes keine gemeinsame effektive Realisierung einer beliebigen unendlichen Folge.

Diese Beispiele beweisen weder Unberechenbarkeit der Natur noch eine Grenze des konkret gegebenen TFPT-Modells. Sie widerlegen den allgemeinen Schluss von beliebig vielen konsistenten endlichen Darstellungen auf eine einheitlich verfügbare Maschine. Für einen physikalischen oder algorithmischen Grenzübergang müssen Quellen, Kompatibilität und Ressourcen zusätzlich kontrolliert werden.

**5. Was ein fundamentales Auswahlprinzip tatsächlich leisten müsste**

Sei \(A\) eine ausdrücklich angegebene Menge von Grundannahmen und \(\mathfrak M(A)\) die Klasse ihrer zulässigen markierten Modelle. Ein Modell enthält beispielsweise Träger, lokale Struktur, Zustände, Dynamik, mögliche Apparaturen und Auslesen. Fundamentale Eindeutigkeit bedeutet sinnvollerweise

\[
\mathfrak M(A)/\simeq_{\mathrm{phys}}\ \text{enthält genau eine Klasse}.
\]

Die Äquivalenz darf reine Koordinaten- und Eichunterschiede identifizieren. Sie darf unterschiedliche experimentelle Vorhersagen nicht verdecken.

Der Universalraum von Abschnitt 2 existiert für jedes einzelne konsistent definierte Modell. Daher kann seine Existenz allein diese Klasse nicht auf ein Modell reduzieren. Das ist ein logischer Unterschied zwischen Rekonstruktion und Auswahl.

Ein kleines Gegenmodell verdeutlicht ihn. Auf einem Qubit seien dieselbe Präparation \(|0\rangle\), dieselbe Messung von \(Z\), dieselbe Skala \(\omega>0\), aber alternativ

\[
H_0=\omega Z,\qquad H_1=\omega X
\]

gegeben. Beide Modelle haben dieselbe Dimension, dieselben Energieeigenwerte, unitäre Zeitentwicklung und vollständige Prozessdarstellungen. Die Wahrscheinlichkeit für das Messergebnis \(1\) ist jedoch \(0\) beziehungsweise \(\sin^2(\omega t)\). Eine Basisrotation würde zugleich Präparation und Auslese verändern; bei der festgehaltenen Markierung sind die Vorhersagen verschieden.

Auch die Rekonstruktion der Quantenmechanik aus informationellen Axiomen wählt zunächst die theoretische Struktur. Sie enthält nicht automatisch den konkreten Hamiltonoperator eines TFPT-Modells. In der bekannten Rekonstruktion von Chiribella, D'Ariano und Perinotti sind mehrere ausdrückliche Axiome einschließlich Purifikation nötig. Das ist ein Beispiel für eine nachvollziehbare Herleitung mit Prämissen, kein Ersatz der hier offenen Kopplungs- und Zustandsauswahl. [*Informational derivation of Quantum Theory*, [Primärquelle](https://arxiv.org/abs/1011.6451).]

Für die Behauptung, alle ursprünglichen TFPT-Axiome seien unzureichend, müsste man zwei Modelle konstruieren, die tatsächlich jedes dieser Axiome erfüllen. Das wurde hier nicht getan. Die vorliegenden Gegenbeispiele gelten für die ausdrücklich geprüften schwächeren Kriterien. Ein zusätzliches wirksames Fundamentalprinzip bleibt möglich.

**6. Vollständige Lösung des erweiterten Minimax-Problems**

Q048 und Q050 des PDFs untersuchen eine HH-Verbindung zwischen den hohen Materiesorten. Die übernommene vollständige Defektformel lautet bei reellen Koeffizienten

\[
F(a,b,h,c)=2(a-h)^2+8\left[b-\frac{a+h}{2}\right]^2+4c^2.
\]

Der Ausgangsansatz setzt \(h=0\). Bei festem \(a\ne0,c\) folgt dann eindeutig \(b=a/2\). Dies ist der vorhandene relative Minimax-Satz.

Die folgende Rechnung optimiert zusätzlich über \(h\). Setze

\[
\alpha=h/a,\qquad \beta=b/a,\qquad \gamma=c/a.
\]

Dann ist

\[
F/a^2=2(1-\alpha)^2+8\left[\beta-\frac{1+\alpha}{2}\right]^2+4\gamma^2.
\]

**Satz B: Eindeutiges Optimum bei freier HH-Kopplung.** Bei festem \(a\ne0,c\) und frei variierenden reellen \(h,b\) ist

\[
\boxed{h=a,\qquad b=a,\qquad F_{\min}=4c^2.}
\]

**Beweis.** Beide Quadrate sind nichtnegativ. Das erste verschwindet genau für \(\alpha=1\), das zweite dann genau für \(\beta=1\). Alternativ besitzt die Hessische Matrix in der Reihenfolge \((\alpha,\beta)\)

\[
\begin{pmatrix}8&-8\\-8&16\end{pmatrix}
\]

positive führende Hauptminoren \(8,64\); die Zielfunktion ist streng konvex. ∎

Am bisherigen Punkt \((h,b)=(0,a/2)\) liegt der Defekt um \(2a^2\) höher. Bereits die Ableitung des normierten Defekts nach \(\alpha\) ist dort \(-4\). Der Punkt ist in der erweiterten Klasse nicht einmal stationär.

**Bedeutung.** Der Wunsch nach kleinem Reihenfolgefehler wählt innerhalb dieser erweiterten Familie eine andere Kopplung. Er begründet das Weglassen der HH-Verbindung nicht. Das ist keine Widerlegung eines TFPT-Axioms, welches \(h=0\) bereits unabhängig erzwingt; es zeigt genau, warum ein solches Axiom oder eine andere belegte Einschränkung erforderlich wäre. Die Zusatzformel aus dem PDF wird hierbei übernommen, ihre vollständige native Fock-/Rotor-Herleitung wurde nicht erneut ausgeführt.

Man kann außerdem präzise beantworten, ob eine zusätzliche Vorliebe für kleine HH-Kopplungen genügt. Diese Strafkosten werden jetzt ausdrücklich neu eingeführt und nicht als TFPT-Regeln ausgegeben.

Bei einer quadratischen Strafe \(\lambda\alpha^2\), \(\lambda\ge0\), ergibt die Minimierung

\[
\alpha_\lambda=\frac{2}{\lambda+2},
\qquad
\beta_\lambda=\frac{\lambda+4}{2(\lambda+2)}.
\]

Für jedes endliche \(\lambda\) bleibt \(h\ne0\). Der ursprüngliche Punkt entsteht erst im Grenzfall unendlicher Strafstärke. Bei einer Betragsstrafe \(\lambda|\alpha|\) erhält man hingegen

\[
\alpha_\lambda=\max(1-\lambda/4,0),
\qquad
\beta_\lambda=(1+\alpha_\lambda)/2.
\]

Ab \(\lambda=4\) ist die ursprüngliche Nullkopplung optimal. Die neue Strafart und ihre Stärke übernehmen dann jedoch die Auswahl. Sie müssten selbst aus dem Fundamentalprinzip folgen; das Optimieren beseitigt diese Herkunftsfrage nicht.

Damit ist diese konkrete Kandidatenklasse vollständig analysiert: Nur die Reihenfolgeminimierung liefert den ursprünglichen Punkt nicht. Eine zusätzliche glatte quadratische Strafe liefert bei endlicher Stärke ebenfalls keinen exakten Nullwert. Ein hartes Verbot oder eine hinreichend starke Betragsstrafe kann ihn auswählen, ist aber zusätzliche Struktur.

**7. Warum die Herkunft der HH-Null besonders aufschlussreich ist**

Der im PDF referenzierte ursprüngliche Block wurde im aktuellen lokalen Quellcode über den Codegraphen gefunden und im Original gegengeprüft. Er lautet

\[
h(A)=
\begin{pmatrix}
A+\lambda g^2A^2&\lambda gA\\
\lambda gA&(\Delta+\lambda)I
\end{pmatrix}.
\]

Der hohe Block ist in diesem Ansatz ein skalares Vielfaches der Identität. Deshalb gibt es darin kein eigenes HH-Hopping. Die Null folgt hier aus einer bereits getroffenen Wahl des Ansatzes.

Q050 zeigt weiter: Eine gleichförmige innere Artensymmetrie, welche die nichtentarteten Onsite-Energien und die vorhandene Kreuzkopplung erhält, hat nur einen skalaren Kommutanten. Diese Symmetrieklasse kann deshalb nicht die fehlende HH-Verbindung schützen, während sie die Kreuzkopplung erlaubt. Andere Compiler-Regeln sind damit nicht ausgeschlossen.

Die ebenfalls im PDF konstruierte Familie

\[
h_{\xi,m}(A)=
\begin{pmatrix}A+A^2/4&A/2\\A/2&4I+\xi A^m\end{pmatrix}
\]

behält für \(\|A\|\le1/2,\ |\xi|\le1\) die bezeichneten niedrigen Nullstellen und eine getrennte hohe Einteilchenbande. Der Unterschied der niedrigen Eigenzweige beginnt bei

\[
f_{\xi,m}(x)-f_0(x)=\frac{\xi}{64}x^{m+2}+O(x^{m+3}).
\]

Ohne abgeleitete Schranke an Reichweite oder Polynomgrad kann deshalb jede vorab feste Taylorordnung durch eine spätere Abweichung unterlaufen werden. Diese Aussage betrifft die eingefrorene Einteilchenfamilie, nicht eine schon bewiesene Bandlücke des vollständigen wechselwirkenden Systems.

Die Folgerung für die Forschung ist konkret: Zuerst die zulässige Mikrofamilie unabhängig begründen, danach ihre Parameter durch genügend trennende Antworten identifizieren. Weitere passende niedrige Koeffizienten ohne Kontrolle der Modellklasse genügen nicht.

**8. Was die Geschichtskodierung wirklich universell macht**

Das PDF konstruiert für eine vorgegebene unitäre Zieloperation \(U\), eine positive Normisometrie \(T\) und \(L\) Normstufen

\[
J_L(U)\psi=\sum_{j=0}^{L-1}c_jT^j\kappa U^{-j}\psi,
\qquad
c_j=\sqrt{\frac2{L+1}}\sin\frac{(j+1)\pi}{L+1}.
\]

Diese Kodierung erreicht unter dem dort festgelegten Vertrag den optimalen vollständigen Kanalfehler

\[
\frac12\|\Phi_{TJ_L(U)}-\Phi_{J_L(U)U}\|_\diamond
=\sin\frac\pi{L+1}.
\]

Die mitgeführten Operationen enthalten ebenfalls \(U^{-j}QU^j\). Das Zielgesetz steckt deshalb in der Vorbereitung und den stufenabhängigen Operationen. Der Satz bleibt gültig und nützlich: Er macht die benötigte Information und den Fehlerpreis sichtbar.

Die Quantoren sind entscheidend:

\[
\forall U\ \exists J_L(U)\ :\ \text{kontrollierte Darstellung von }U.
\]

Daraus folgt weder eine Auswahl von \(U\) noch dieselbe unveränderte Implementierung für alle \(U\).

**Satz C: Maximale Unterscheidbarkeit für eine unveränderte Implementierung.** Sei der logische Hilbertraum mindestens zweidimensional. Halte \(T\) und die isometrische Kodierung \(J\) fest. Dann gilt

\[
\boxed{
\sup_{U\ \mathrm{unitär}}
\frac12\|\Phi_{TJ}-\Phi_{JU}\|_\diamond=1.
}
\]

**Beweis.** Wähle einen normierten logischen Eingang \(\psi\). Es gibt einen normierten Vektor \(\varphi\), der orthogonal zu \(J^\dagger TJ\psi\) ist; die Dimension ist mindestens zwei. Erweitere \(\psi\mapsto\varphi\) zu einer unitären Operation \(U\). Dann

\[
\langle JU\psi,TJ\psi\rangle
=\langle\varphi,J^\dagger TJ\psi\rangle=0.
\]

Beide vollständigen Ausgänge sind normierte reine Zustände und haben halben Spurabstand eins. Schon dieser einzelne Eingang liefert die untere Diamantgrenze eins. Für zwei Kanäle ist eins zugleich die obere Grenze des halben Diamantabstands. ∎

Dies ist kein Verbot programmierbarer Quantencomputer. Bei ihnen wird das Programm, die Pulsfolge oder eine andere zugelassene Steuervorgabe verändert. Satz C hält gerade die gesamte Implementierung unverändert. Die separate klassische Grenze für exakt deterministische Programmierung beliebiger Unitaries mit einem endlichen Programmregister beschreibt Nielsen und Chuang. Die gewöhnliche approximative universelle Schaltkreisberechnung wird dadurch ebenfalls nicht ausgeschlossen. [*Programmable quantum gate arrays*, [Primärquelle](https://arxiv.org/abs/quant-ph/9703032).]

Für eine beliebige eingeschränkte Zielfamilie gibt es außerdem die einfache notwendige Bedingung: Werden \(U,V\) durch dieselbe Implementierung jeweils mit Fehler höchstens \(\varepsilon\) approximiert, dann

\[
\tfrac12\|\Phi_U-\Phi_V\|_\diamond\le2\varepsilon.
\]

Das folgt aus der Dreiecksungleichung und der Abstandserhaltung einer gemeinsamen isometrischen Ausgabe-Kodierung. Für eine Familie gut unterscheidbarer Gesetze braucht man entsprechend unterschiedliche Programme oder Ressourcen.

**9. Wie eine positive, selbstenthaltene Lösung aussehen müsste**

Der konstruktive nächste Schritt ist ein Modell, in dem auch Vorbereitung, Uhr, Steuerung und Auslese aus bezeichneten Teilen der Quelle entstehen. Dann sind die vermeintlich extern erlaubten Handlungen selbst physikalische Prozesse im Gesamtmodell. Ein abstraktes Pulsalphabet allein reicht dafür nicht.

Die dafür notwendigen Daten lassen sich als markierte Gesamtheit formulieren: eine Zustands- oder Observablenstruktur; ein zulässiger Anfangsbereich; eine Dynamik; eine Zerlegung in zugängliche und weitere Freiheitsgrade; erlaubte Apparatezustände; und beobachtbare Ausgänge. Der Universalraum ist dann die operationelle Beschreibung dieser Gesamtheit.

Das macht die Herkunftsfrage prüfbar, aber nicht voraussetzungslos. Beliebige Zielantworten könnten sonst bereits in einen Anfangszustand oder ein Programmregister geschrieben werden. Deshalb muss nachvollziehbar sein, welche Daten aus dem Grundprinzip stammen, welche als kontingente Eingaben erlaubt sind und welche aus Messungen identifiziert werden.

Eine Theorie muss dabei nicht jede zufällige Einzelmessung deterministisch auswählen. Sie muss die behaupteten Gesetze, Verteilungen und zulässigen Anfangsdaten bestimmen. Falls mehrere empirisch unterschiedliche Modelle verbleiben, braucht es eine weitere begründete Auswahlregel oder zusätzliche Beobachtung. Eine Liste aller möglichen Modelle wäre eine universelle Beschreibungssprache, aber noch keine Einzelvorhersage.

**10. Ein konkret lösbarer Anschluss: Identifikation statt bloßer Rückbestätigung**

Für eine begründete endliche Generatorfamilie

\[
H(\theta)=H_0+\sum_{j=1}^{r}\theta_jG_j
\]

und fest zugelassene Eingaben \(\rho_k\), beschränkte Auslesen \(O_k\) ergeben anfängliche Antwortsteigungen

\[
s_k=i\operatorname{tr}(\rho_k[H(\theta),O_k])
=s_{0,k}+\sum_jM_{kj}\theta_j,
\quad
M_{kj}=i\operatorname{tr}(\rho_k[G_j,O_k]).
\]

Die Schreibweise setzt die nötigen Definitionsbereiche beziehungsweise differenzierbaren Erwartungen voraus. Bei einem beschränkten endlichen Modell ist das automatisch erfüllt. Hat \(M\) vollen Spaltenrang, sind die bezeichneten Parameter eindeutig identifizierbar. Bei Steigungsfehler \(\|e\|\le\eta\) gilt für die lineare Rekonstruktion

\[
\|\widehat\theta-\theta\|\le\|M^+\|\eta.
\]

Das ist ein positiver allgemeiner Abschluss einer begrenzten Identifikationsfrage. Er gilt nicht für zusätzliche unbekannte Generatorrichtungen außerhalb der festgelegten Familie. Eine schlechte Konditionierung kann die erforderliche Messgenauigkeit stark erhöhen.

Im tatsächlichen HH-Test des PDFs ist \(M=-1/6\), also

\[
\widehat\xi=-6\widehat s,
\qquad |\widehat\xi-\xi|\le6\eta.
\]

Damit lässt sich ein Blindversuch präzise vereinbaren: Die verborgene Variante wird vorab aus einer bezeichneten Klasse gewählt; Quelle, Zustand und Auslese sind fest; der Leser rekonstruiert den Parameter und sagt anschließend andere, nicht zum Anpassen benutzte Antworten voraus. Das PDF enthält dafür Modellwerte, aber keine unabhängige Hardwaremessung. Die Herkunft einer Nullsteigung aus ursprünglichen TFPT-Regeln wäre weiterhin mehr als das erfolgreiche Identifizieren einer bereits gewählten Modellvariante.

Auch die endliche Messzeit lässt sich korrekt bezahlen. Sei \(y(0)=0\), \(y'(0)=-\xi/6\) und \(|y''(t)|\le B\) im festgelegten Zeitbereich. Wird \(y(t)\) mit absolutem Fehler höchstens \(\delta\) erfasst, dann liefert

\[
\widehat\xi=-6\widehat y(t)/t,
\qquad
|\widehat\xi-\xi|\le6\delta/t+3Bt.
\]

Für \(B,\delta>0\) ist innerhalb des zulässigen Zeitbereichs die ideale Wahl \(t=\sqrt{2\delta/B}\), mit Schranke \(6\sqrt{2B\delta}\). Liegt diese Zeit außerhalb, muss am Rand des zulässigen Bereichs optimiert werden. Messrauschen kann hier nicht durch beliebig kleine Zeit kostenlos beseitigt werden.

Bei einem unbeschränkten selbstadjungierten \(H\), einem normierten \(u\in\operatorname{Dom}(H^2)\) und beschränktem \(Y\) gibt es die zustandsbezogene ausreichende Schranke

\[
B=2\|Y\|\bigl(\|H^2u\|+\|Hu\|^2\bigr).
\]

Sie folgt durch zweimaliges Differenzieren von \(\langle e^{-itH}u,Y e^{-itH}u\rangle\) und Cauchy-Schwarz. Die Normen der Zeitableitungen sind wegen der unitären Entwicklung konstant. Für eine unbekannte Parameterfamilie muss dieselbe obere Schranke für alle zugelassenen Parameter bewiesen werden. Hier wurde dafür keine neue native Zahl berechnet. Die Formel ist ein vollständiger bedingter Messfehlervertrag, keine bereits ausgeführte Apparatur.

**11. Zeit, Raum, Arithmetik und Schutz im gemeinsamen Bild**

**Zeit.** Die Reihenfolge von Eingriffen, ein reversibler Fluss \(U(t)\), ein positiver Normshift und ein stochastischer Teilerabstieg sind verschiedene mathematische Strukturen. Eine Identifizierung braucht einen nachgewiesenen Zusammenhang von Generator, Uhr, Zuständen und Auslese. \(F(mn)=F(m)+F(n)\) auf positiven ganzen Zahlen allein erzwingt nicht \(F(n)=c\log n\): Man darf jedem Primfaktor ein anderes Gewicht geben. Zusätzliche Regularität auf einer reicheren Normgruppe oder eine markierte Energieauswahl wäre erforderlich. Das PDF behauptet eine solche Auswahl ausdrücklich nicht kostenlos.

**Raum und Lokalität.** Eine abstrakte Matrixalgebra bestimmt ihre physikalische Zerlegung in Teilsysteme nicht eindeutig. Derselbe vierdimensionale Hilbertraum kann als ein Vierniveausystem oder als zwei Qubits beschrieben werden. Welche Operatoren lokal verfügbar sind, ergänzt physikalischen Inhalt. Daher kann ein gemeinsames algebraisches Modell Raumzeit und Lokalität erst erklären, wenn diese Struktur und ihre Wirkung aus den ursprünglichen Regeln folgen.

**Arithmetik.** Normen, Restklassen und Primkomponenten können auf einem gemeinsamen Träger repräsentiert werden. Die drei noch verschiedenen Leistungen sind die Darstellung arithmetischer Daten, die Erzeugung informativer Daten aus einer öffentlichen Eingabe und die effiziente Auslese dieser Information. Ein schneller Nachprozessor ist kein schneller Lieferant seiner Voraussetzungen.

**Geschützter Speicher.** Der F15-Entwurf zeigt ein brauchbares endliches Modell: Ein logischer Faktor bleibt unter einer bezeichneten Störalgebra erhalten; zusätzlich gewählte Steuerungen verarbeiten ihn. Der Schutz gilt relativ zur Störklasse. Wird jede mögliche Störung zugelassen, kann auch eine vollständige Löschung auftreten. Ein universeller Speicher, der unter beliebigen Störungen dieselbe Information erhält, folgt daraus nicht. Der TFPT-Anschluss von Encoder und Steuerungen ist weiterhin offen.

**12. Warum RH und Faktorisierung getrennte Ziele bleiben**

Für RH geht es um die tatsächliche signierte Weil-Form einschließlich Primanteilen, Gamma-Beitrag, Polen und vollständigem Definitionsbereich. Die Positivität irgendeines gemeinsamen Gram-Kerns impliziert deren Positivität nicht. Die im PDF gewählte Route über alle kompakten glatten ungeraden Tests ist nach dem dort referenzierten Yoshida-Kriterium ausreichend; eine zusätzlich unabhängige gerade Positivitätskampagne ist für genau diese Route nicht nötig. Diese Einordnung wurde in Suzukis aktuellem Primärtext kontrolliert. [*Weil’s quadratic form via the screw function*, insbesondere Einleitung und Verweis auf Yoshida Proposition 1, [Primärquelle](https://arxiv.org/html/2606.09096v2).]

Der aktuelle lokale Forschungskatalog bestätigt als offenen nächsten Anschluss die echte \(160\times160\)-Gram-Matrix bei \(J=320\) und die vollständige Restnorm. Die Werte \(0{,}35\) und \(0{,}18\) sind ausreichende Zielbudgets, keine bereits gemessenen Normen. Auch ein erfolgreicher nächster Fensteranschluss müsste noch zu einer alle notwendigen Fenster erfassenden Regel erweitert werden. In dieser Untersuchung wurde keine neue RH-Rechnung begonnen und keine neue Beweisregel registriert.

Für Faktorisierung liefern die bisherigen Sätze einen starken bedingten Auslese- und Nachverarbeitungsvertrag. Offen ist eine aus \(N\) und öffentlicher Historie erzeugte Quelle mit ausreichend großer bedingter Primtrennung und günstigen vollständigen Bitkosten. Wird ein benötigter erster Teilerprozess-Sprung bereits anhand der unbekannten Primfaktoren bereitgestellt, steckt die gesuchte Information in der Voraussetzung. Die Existenz seiner Formel ist noch keine Implementierung. Klassische Ergebnisse über die Nachverarbeitung gegebener Ordnungsinformation ändern diese Trennung ebenfalls nicht. [Ekerå, *On completely factoring any integer efficiently in a single run of an order finding algorithm*, [Primärquelle](https://arxiv.org/abs/2007.10044).]

Beide Aufgaben können durch bessere gemeinsame Werkzeuge profitieren. Sie sind aber keine automatischen Folgerungen aus der Existenz des Universalraums und müssen nicht beide gelöst sein, damit eine begrenzte Prozessdarstellung mathematisch vollständig ist.

**13. Der erste noch fehlende Schritt und seine Abnahme**

Für die fundamentale Linie ist der erste fehlende Übergang:

\[
\text{ursprüngliche TFPT-Regeln}
\quad\Longrightarrow\quad
\text{zulässige lokale Quellfamilie und tatsächlich verfügbare Operationen}.
\]

Innerhalb der bisher betrachteten Umgebung lässt sich die nächste Abnahme konkret formulieren:

1. Die erlaubte Reichweite und Kopplungsfamilie müssen vor der Anpassung der gewünschten Antwort aus den Originalregeln folgen.
2. Eine Quelle samt bezeichnetem Anfangszustand und Auslese muss eine trennende Antwort liefern. In der festgelegten HH-Nachbarfamilie wäre eine unabhängig hergeleitete Nullsteigung hinreichend, um \(\xi=0\) auszuwählen.
3. Die vorhandene gemeinsame Acht-Eingaben-Familie muss mit beiden Operationsreihenfolgen, allen Ausgängen und den Fehlergrenzen erhalten werden. Der neue Einparameter-Test ersetzt diesen Vertrag nicht.
4. Ein zusätzlicher unabhängiger Vorhersagetest muss zeigen, dass die Auswahl mehr leistet als eine Wiedergabe ihrer Eingabedaten.

Scheitert bereits die erste Ableitung, sind weitere Compiler-Vergleiche weiterhin Darstellungsfortschritte. Scheitert nur ein bestimmtes vorgeschlagenes Prinzip, wird dieses Prinzip in seinem Umfang verworfen; daraus folgt kein allgemeiner Ausschluss jeder Fundamentaltheorie.

**14. Quellen, eigene Prüfung und Aussageumfang**

Die PDF wurde vollständig textuell erschlossen, aber nicht jeder ihrer 68 Forschungsberichte erneut fachlich geprüft. Inhaltlich vertieft wurden die Hauptargumentation zur Prozessdefinition und Auswahl sowie insbesondere Q019, Q048–Q050, Q056–Q057 und Q067–Q068. Ausgewählte zentrale PDF-Seiten wurden zusätzlich gerendert und visuell kontrolliert. Die historischen großen Kampagnen, Hardwareversuche und externen Prüfungen wurden nicht wiederholt.

| Beleg | Verwendung |
|---|---|
| Eingereichte PDF, Seiten 7–10 und Q019, Seiten 122–125 | Operative Äquivalenz, Minimalrealisierung, Schnittstellen und Ressourcen. |
| PDF, Seiten 13–14 und Q048–Q050, Seiten 226–232 | Minimax-Formel, HH-Herkunft, Symmetriegrenze und trennende Antwort. |
| PDF, Seiten 15–17 und Q056–Q057, Seiten 253–260 | Feste Normisometrie, Sinuscode, mitgeführte Operationen und Quantoren. |
| PDF, Seiten 23–28 und Q067–Q068, Seiten 290–293 | Anwendungsspezifische Lücken, F15 und begrenzter Geschichtsreview. |
| Aktueller TFPT-Codegraph und Originalfunktion `signed_block` in `verification/v1027_signed_det_car_wall.py`, Zeilen 50–55 | Der skalare hohe Block ist tatsächlich Bestandteil des deklarierten Ansatzes. |
| Aktueller RH-Forschungskatalog und `generated/NEXT.md` | Quellenindex aktuell; nicht alle Quellen semantisch geprüft. Der RH-Kopplungsschritt ist weiterhin offen. |

Die Seitenangaben beziehen sich auf die tatsächlichen PDF-Seiten beziehungsweise die dort gedruckten Seitenzahlen. Manche Anhang-Verweise im Inhaltsverzeichnis weisen gegenüber diesen einen Versatz auf; für diese Ausarbeitung wurden die realen Seiten verwendet.

SHA-256 der eingereichten PDF:

`bee5246fcf4a4943dccd90548424ae99048e5aac9d2fc7ad6d71220ef7ba43c3`

Ein neu geschriebener exakter Prüfer führt 41 begrenzte Kontrollen aus: die vollständigen symbolischen Minimax-Ableitungen und Strafkosten, neun Geschichtskodierungen mit drei Tiefen und drei verschiedenen vorgegebenen Unitaries sowie ein Gegenbeispiel zur Auswahl durch gleiche Spektren. Insbesondere werden isometrische Vollausgänge und exakt orthogonale alternative Zielausgänge kontrolliert. Diese Zahl ist eine Beschreibung des Prüfprogramms, kein Maß für unabhängige Beweise oder gelöste Fundamentalprobleme. Die allgemeinen Beweise stehen in dieser Ausarbeitung.

Die Ergebnisdatei und der Reproduzierer liegen im beigefügten Prüfarchiv. Es gibt keine externe unabhängige Begutachtung dieser neuen Ausarbeitung und keine Lean-Formalisierung. Die Originalquellen, Forschungsregister und fremden Arbeitsstände wurden nicht verändert.

Der mathematische Universalraum ist damit als relative vollständige Prozesssemantik präzisiert. Die konkrete TFPT-Welt ist aus den bisher geprüften Voraussetzungen noch nicht eindeutig hergeleitet. Die entscheidende weitere Arbeit besteht in einem unabhängig begründeten, trennenden Übergang von den Originalregeln zur Quelle und ihren Handlungen.
