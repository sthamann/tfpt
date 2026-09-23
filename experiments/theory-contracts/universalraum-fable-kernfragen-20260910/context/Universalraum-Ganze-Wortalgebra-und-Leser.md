# Die ganze Gate-Wortalgebra und die einzelne Rückkehruhr

10. September 2026. Ergänzung aus den ausdrücklich ursprünglichen U,V-Matrizen. Kein neuer physischer Ursprungsanspruch.

Sei R=Z[i,1/2] und seien

\[
U=\frac12\begin{pmatrix}1+i&1+i&0\\-1+i&1-i&0\\0&0&2\end{pmatrix},
\quad V=\frac12\begin{pmatrix}1+i&0&1+i\\0&2&0\\-1+i&0&1-i\end{pmatrix}.
\]

**Satz.** Die von U und V erzeugte unital assoziative R-Algebra ist genau M₃(R). Dagegen hat die Potenzalgebra des einzelnen W=UV über Q(i) Dimension drei.

**Beweis.** Alle Gateeinträge und alle Produkte liegen in M₃(R). Ordne die neun Matrixkoordinaten zeilenweise an. Die neun Spalten zu

\[
I,\ U,\ V,\ U^2,\ UV,\ VU,\ V^2,\ U^2V,\ UV^2
\]

haben exakt Determinante −1/16. Dies ist eine Einheit von R. Die inverse Neunerkoordinatenmatrix hat deshalb ebenfalls Einträge in R; die neun bezeichneten Wörter bilden eine R-Basis von M₃(R). Eine größere Unteralgebra innerhalb M₃(R) gibt es nicht. Für W ist I,W,W² linear unabhängig, und sein charakteristisches Polynom vom Grad drei reduziert alle höheren Potenzen. Also ist Q(i)[W] dreidimensional und kommutativ, während U und V nicht kommutieren. ∎

**Arithmetische Konsequenz.** Die Neunerbasis bleibt nach jeder ungeraden Primreduktion invertierbar, einschließlich p=79; allgemeiner bleibt sie über R/NR für jedes ungerade N eine Basis. Die Stelle 79 ist daher eine Ausnahmestelle der konkreten kubischen W-Spektraldarstellung und ihres Spurgramms mit Determinante316. Sie ist keine singuläre Stelle der vollständigen assoziativen U,V-Wortalgebra. Die gemeinsame Nennerstelle2 ist bereits in R invertiert und hat eine andere Herkunft.

Dies ist für die universelle Interpretation wesentlich: Aus den Besonderheiten einer gewählten Uhr darf man nicht auf ausgezeichnete Primzahlen der vollständigen Quelle schließen. Die natürliche Grenze der W-Zeta bleibt ein korrekter Satz über genau diese Uhr; sie ist kein Ausschluss anderer aus U,V-Wörtern konstruierter Antworten.

**Was dieser Satz nicht liefert.** Ein allgemeines Element der R-Algebra ist eine R-Linearkombination von Gatewörtern. Eine solche Linearkombination ist nicht automatisch ein zulässiger unitärer Prozess oder ein effizient ausführbarer physischer Eingriff. Der Satz bestimmt weder einen Zustand, ein physisches Zeitgesetz, ein Messinstrument noch die Kosten des Zugriffs auf gewünschte Koeffizienten. Er beweist auch keine Treue einer universellen abstrakten Wortalgebra oder eines behaupteten universellen physikalischen Modells.

Die Größe3 oder9 ist zudem die Dimension über dem Koeffizientenkörper beziehungsweise -ring, nicht die Bitlänge aller möglichen Zustände. Die gaußdyadischen Koeffizienten können beliebig große Zähler und Nenner tragen. Kleine algebraische Dimension allein beweist somit keine polynomialen Kosten zur Lösung eines kodierten Problems.

## Ein fester vollständiger Leser und die ganze Wortdynamik

Bezeichne die neun obigen Wörter mit B_j und ihre flach angeordneten Spalten mit der Matrix B. Ihr positives Hilbert–Schmidt-Gram ist

\[
\mathsf G_{jk}=\operatorname{tr}(B_j^\dagger B_k),\qquad
\det\mathsf G=|\det B|^2=1/256.
\]

Setze D_j=Σ_k B_k(\mathsf G⁻¹)_{kj}. Dann gilt exakt

\[
\operatorname{tr}(D_j^\dagger B_k)=\delta_{jk},\qquad
\boxed{X=\sum_{j=1}^9B_j\operatorname{tr}(D_j^\dagger X).}
\]

Damit rekonstruieren neun festgelegte gemischte Antworten jede Matrix X dieser ursprünglichen Darstellung. Die Proben D_j sind feste Linearkombinationen derselben kurzen Gatewörter. Die ausgerechneten Leser und ihre Koeffizienten benötigen in Real- und Imaginärteilen höchstens den Nenner2. Insbesondere werden keine unbekannten Primfaktoren, keine kubischen Eigenwerte und keine Division durch79 benötigt. Der Satz gilt nach Reduktion modulo jedem ungeraden N, auch bei Primzahlpotenzen und zusammengesetztem N.

Noch stärker ist die Dynamik in diesen Koordinaten vollständig festgelegt. Schreibe X=Σ_j c_j B_j. Linkskomposition mit U beziehungsweise V ergibt

\[
\boxed{c_{k+1}=L_{g_k}c_k,\quad g_k\in\{U,V\},\qquad
L_g=B^{-1}\bigl(\operatorname{vec}(gB_1),\ldots,\operatorname{vec}(gB_9)\bigr).}
\]

Die zwei festen 9×9-Matrizen sind vollständig im Ergebnis gespeichert. Sie erfüllen

\[
L_g^\dagger\mathsf G L_g=\mathsf G,\qquad L_g^6=I,
\qquad L_U L_V\ne L_V L_U.
\]

Die positive Paarung und die nichtkommutierende Operationsdynamik stammen somit aus derselben ursprünglichen Darstellung. Ein einzelnes W ist nur die Wahl, immer dieselbe Zweischrittfolge anzuwenden. Für jede vorgegebene endliche U,V-Wortfolge gibt es jetzt einen expliziten vollständigen Zustandsübergang und Leser in diesen Koordinaten, einschließlich der ganzen ungeraden modularen Arithmetik.

Diese Rekonstruktion ist klassische lineare Algebra, hier für die unveränderte Quelle exakt ausgerechnet. Sie garantiert nicht, dass ein unbekannter gewünschter X-Zustand oder seine neun Antworten billig hergestellt werden können. Wenn X bereits als Matrix gegeben ist, lesen direkte Matrixzugriffe seine Einträge ohnehin aus. Der Gewinn dieser Darstellung ist die nachgewiesene verlustfreie Verbindung zu festen Quellwörtern und ihrer Dynamik; ein Geschwindigkeitsvorteil für allgemeine Suchprobleme folgt daraus nicht.

## Kontrolle und Begutachtungsgrenze

Die exakte Koordinatendeterminante und beide Dimensionen werden in check_word_algebra.py kontrolliert; word-algebra.json enthält die Basis und das Ergebnis. check_full_reader.py prüft zusätzlich20 exakte Identitäten einschließlich beider ganzer Übergangsmatrizen, der vollständigen Dualität und ausgewählter ungerader modularer Reduktionen. Der allgemeine modulare Satz folgt aus der invertierbaren dyadischen Determinante, nicht aus den ausgewählten Beispielen. full-reader.json enthält sämtliche Proben, das Gram und beide Übergangsmatrizen.

Dies ist ein endlicher algebraischer Beweis mit reproduzierbaren exakten Matrizen, keine numerische Rangschätzung. Die geplante weitere unabhängige Agentenlektüre konnte wegen eines Nutzungslimits nicht stattfinden; für diesen Ergänzungssatz wird keine abgeschlossene unabhängige Lektüre behauptet. Die zuvor abgeschlossene unabhängige Prüfung der Naturgrenze ist davon getrennt.
