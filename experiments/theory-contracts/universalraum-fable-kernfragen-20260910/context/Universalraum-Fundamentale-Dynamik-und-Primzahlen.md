# Universalraum: fundamentale Dynamik, Primzahlen und konkrete Abkürzungen

Stand: 10. September 2026. Fortsetzung anhand der ursprünglichen Compiler-Gates, der lokalen Forschungsgraphen und der bezeichneten TFPT-/RH-Originalquellen.

**Wir haben konkrete neue Sätze und nutzbare Abkürzungen gefunden. Eine vollständige gemeinsame Lösung von TFPT-Dynamik, RH, allgemeiner Faktorisierung und P versus NP liegt damit noch nicht vor.** Der stärkste neue Befund für die Vogelperspektive ist eine exakt belegte Unterscheidung zwischen der ganzen Gate-Algebra und einer einzelnen Rückkehruhr. Sie verhindert, dass Eigenschaften einer Darstellung voreilig zu fundamentalen Eigenschaften des Universalraums erklärt werden.

## 1. Was am ursprünglichen gemeinsamen Nenner trägt

Die Ausgangsidee war, in den RH-, TFPT- und Faktorisierungsversuchen dieselben Strukturen zu suchen: Operationen und ihre Komposition, Zustände, Rückkehr, positive Paarungen, ganzzahlige Daten und die jeweils daraus gelesenen Antworten. Diese Verbindung bleibt produktiv. Die jetzige Fortsetzung findet jedoch eine schärfere mathematische Trennung innerhalb dieser gemeinsamen Quelle.

Seien U,V genau die ursprünglichen Compiler-Gates und R=Z[i,1/2]. Dann gilt jetzt mit einem expliziten endlichen Beweis:

\[
\boxed{R\langle U,V\rangle=M_3(R).}
\]

Die neun Wörter I,U,V,U²,UV,VU,V²,U²V,UV² bilden eine Basis. Ihre Koordinatendeterminante ist −1/16, also eine Einheit von R. Die gesamte assoziative Wort-Algebra ist damit vollständig bestimmt.

Die bisher intensiv untersuchte Uhr W=UV enthält einen kleineren Ausschnitt:

\[
\dim_{\mathbb Q(i)}\mathbb Q(i)[W]=3.
\]

Ihre Potenzen kommutieren miteinander; die ursprünglichen U,V tun das nicht. **Die Untersuchung einer W-Uhr ist daher eine Untersuchung einer bestimmten Darstellung der gemeinsamen Quelle.** Das ist kein Beweis, dass diese endliche Matrixdarstellung bereits der vollständige physikalische Universalraum ist. Auch eine Linearkombination von Gatewörtern ist nicht automatisch ein zulässiger physischer Prozess.

Diese Unterscheidung passt genau zur Frage nach den „Schatten“: Eine Eigenschaft kann im W-Spektrum auftreten, ohne eine ausgezeichnete Eigenschaft der ganzen Wort-Algebra zu sein.

Darauf aufbauend ist inzwischen auch ein vollständiger Leser ausgerechnet: **Neun feste gemischte Quellantworten rekonstruieren jeden Operationszustand dieser Darstellung exakt.** Die zugehörige positive Gram-Determinante ist1/256; die vollständige Rekonstruktion gilt deshalb modulo jedem ungeraden N, einschließlich79. Zwei explizite feste9×9-Matrizen beschreiben sämtliche U- und V-Schritte und erhalten dieselbe positive Paarung. Damit sind die gesamte Wortdynamik und ihr Leser in diesem konkreten Träger bestimmt. Die Herstellung eines gewünschten unbekannten Zustands oder seiner Antworten ist eine weitere Aufgabe; die Koordinatenformel löst sie nicht kostenlos.

## 2. Die genaue Rolle der Primzahlen

Die W-Uhr besitzt eine exakte Hermitesche Cayley-Darstellung

\[
W=(T-iI)(T+iI)^{-1},\qquad
T^3-4T^2+T+4I=0.
\]

Die kubische Diskriminante ist 316=4·79. Der tatsächlich aus I,Y,Y² mit Y=2W gebildete Spur-Gram hat ebenfalls Determinante316. Die Gleichheit ist über die Eigenwertdifferenzen bewiesen; sie ist kein numerisches Zusammentreffen.

| Primstelle | Genaue Rolle im geprüften Modell |
|---|---|
| 2 | Bereits in den Gate-Nennern und im Träger R ausgezeichnet; bestimmt die dyadische Zeitgewichtung der Fixpunktzahl. |
| 79 | Verzweigungsstelle der gewählten W-Kubik und Degenerationsstelle ihres Spur-Gramms. |
| Andere ungerade p | Lokale Rückkehrkanäle, deren Eigenordnungen vom Frobeniustyp der Kubik modulo p abhängen. |

**79 ist keine Ausnahmestelle der ganzen U,V-Wortalgebra:** Die Neunerbasis mit Determinante−1/16 bleibt auch modulo79 invertierbar. Die Ausnahmestellung entsteht beim Übergang zu dieser einzelnen Uhr. Die lokale Rückkehranalyse muss zudem Primstellen und Rückkehrzeiten unterscheiden: Eine Primzahl ist hier zunächst eine arithmetische Beobachtungsstelle; ihre Uhrzeit ist nicht automatisch log p.

Für p≠2,79 und χ=(−1/p) gilt der genaue Frobeniussatz

\[
\lambda_j^p=\lambda_{\pi(j)}^{\chi}.
\]

Bei vollständig gespaltenem kubischem Polynom können drei verschiedene Eigenrichtungen zu verschiedenen Zeiten zurückkehren. Im linear-quadratischen Fall gibt es für die Determinantenrückkehr genau eine grundlegende Ordnung r_p, die p−χ teilt. Im irreduzibel kubischen Fall teilt diese Ordnung p²+χp+1 und ist zugleich die ganze Matrixrückkehrordnung. Hier ist die Primzahldynamik konkret berechenbar beschrieben; die unbekannten Primteiler einer Eingabe N werden dadurch nicht kostenlos bekannt.

## 3. Ein bisher offener Punkt der tatsächlichen Dynamik ist geschlossen

Schreibe P_n=2ⁿtr(Wⁿ)=a_n+i b_n. Aus der ursprünglichen Rekursion und einer geschlossenen Modulo-8-Induktion folgt für **alle** n≥1:

\[
v_2(b_n)=\begin{cases}0&n\text{ ungerade},\\v_2(n)+2&n\text{ gerade}.\end{cases}
\]

Die ursprüngliche Solenoid-Fixpunktzahl F_n=odd(|b_n|)² besitzt damit eine explizite dyadische Gewichtung. Daraus entsteht eine Darstellung ihrer ganzen dynamischen Antwort D(z)=ΣF_nzⁿ als endliche Kombination dyadischer geometrischer Reihen.

Zwei Ergebnisse folgen daraus:

1. **Exakte analytische Grenze:** Die ursprüngliche dynamische Zeta und D haben die natürliche Grenze |z|=1/4, auch gegen meromorphe Fortsetzung. Ein direkter Beweis schließt Phasenauslöschungen aus und zeigt an einer dichten Menge nichtverschwindende radiale Singularitätssignaturen. Damit ist die in der Originalquelle offene Fortsetzungsfrage für diese Zeta entschieden.
2. **Zertifizierte schnelle Auswertung:** Bei z=0.24999975 genügen 24 dyadische Ebenen mit insgesamt72 Inversionen von 9×9-Matrizen. Ergebnis: D(z)=756696.049495159035840020989±4.75·10⁻²². Rundung und der gesamte unendliche Rest sind eingeschlossen; der gemessene Test dauerte etwa0.025Sekunden.

Die einfache geometrische Restschranke einer direkten Periodensumme liefert am zweiten Testpunkt eine ausreichende Grenze von62.064.406Termen für Genauigkeit10⁻²⁰. Das ist ein fair bezeichneteter Vergleich mit dieser einfachen Methode, kein gemessener Beschleunigungsfaktor gegen alle Algorithmen. Eine unabhängige direkte Rekursionssumme prüfte zusätzlich einen kleineren Testpunkt.

Die natürliche-Grenze-Methode ist etablierte Mathematik; die konkrete Quellrechnung ist hier ausgeschrieben. Kontext: [Bell, Miles und Ward, *Towards a Pólya–Carlson dichotomy for algebraic dynamics*](https://arxiv.org/abs/1307.2369).

Die Konsequenz für RH ist präzise: Diese W-Zeta kann nicht unmittelbar die meromorph fortsetzbare Riemannsche Zeta sein. Ein anderer aus der gesamten Quelle hergeleiteter relativer Leser oder ein anderes Zeitgesetz bleibt möglich. Dafür müssen insbesondere Primzahlpotenzgewichte, log-p-Zeiten, Gamma- und Polbeiträge tatsächlich entstehen.

## 4. Eine ausführbare Abkürzung für die Faktorauslese

Der Potenzalgorithmus berechnet ohnehin drei Gaußkoeffizienten r_n, welche Yⁿ in der Basis I,Y,Y² darstellen. Wenn man sie erhält, statt nur ihre skalare Spur zu speichern, gilt mit dem echten Quell-Gram G:

\[
r_n^T G\overline{r_m}=4^mP_{n-m},\qquad
\gcd\!\left(N,\Im(r_n^TG\overline{r_m})\right)=\gcd(N,b_{n-m})
\]

für ungerades N und n≥m. Die große Zahl4^m braucht man nicht auszurechnen. Die zusätzliche Auslese kostet in der angegebenen Implementierung48 modulare Produkte und einen ggT, wenn beide Potenzzustände schon vorliegen.

Ein vollständiger Erfolgszeuge:

- Eingabe7117, bereits gewählte Zeiten81 und108.
- Beide Einzelantworten liefern nur7117 und trennen keinen Faktor.
- Die gemeinsame Antwort ist3110+4807i modulo7117.
- gcd(7117,4807)=11: Die gemeinsame Antwort trennt den Faktor.
- Derselbe festgelegte Versuch benötigt insgesamt1212 statt1656 modulare Produkte; die Zusatzstufe48 statt492.

Die Erklärung ist dynamisch: An einer Primstelle kehren bei81 und108 verschiedene Richtungen zurück, an der anderen besitzen sie eine gemeinsame Rückkehr bei27. Die Einzelspuren hatten die Richtungsinformation verworfen; die gemischte Paarung erhält sie.

Das Beispiel wurde gezielt anhand lokaler Diagnosen ausgewählt. Der öffentliche Leser verwendet ausschließlich N und die beiden Indizes; eine allgemein günstige Auswahl solcher Indizes wurde nicht gefunden. Ein Geschwindigkeitsvorteil gegenüber ECM, GNFS oder anderen etablierten vollständigen Faktorisierern ist nicht nachgewiesen.

## 5. TFPT: ein konkreter Ursprungskandidat für die Kopplung

Im vorhandenen Q-System C[Z₄] ist ein bestimmter neutraler Paarvektor v=m†η ausgezeichnet. Er zerfällt in den markierten Einheitskanal und drei orthogonale Komplementkanäle, mit Normquadrat4=1+3. Wird der tatsächliche hohe Quellstrom mit genau diesem Paarvektor verbunden, erzeugt dieselbe Konstruktion die ganze Parent-Form

\[
\begin{pmatrix}A+A^2/4&A/2\\A/2&4I\end{pmatrix}.
\]

Allgemein folgt die skalenunabhängige Beziehung **M c_hop=4b²** zwischen hohem Budget, vollem mikroskopischem Zwei-Link-Koeffizienten und gemischter Kopplung. Die Zahl4 setzt jedoch keine absolute Energieeinheit fest.

Der entscheidende fehlende Schritt ist nun ausdrücklich benannt: eine aus der ursprünglichen markierten Seam hergeleitete, gauge-, spin-, CAR- und randverträgliche Abbildung dieses Paarvektors auf den wirklichen hohen Strom. Das ist die benötigte Verbindung zwischen vorhandener Struktur und tatsächlicher Dynamik.

Warum dieser Nachweis wesentlich ist, zeigt eine exakte Alternative: Dieselben abstrakten Q-System-Daten, niedrigen/gemischten Blöcke und sogar dieselbe normierte hohe Rückkehr lassen einen zusätzlichen Parent mit hohem Wert13 statt4 zu. Die physische Markierung und die Minimalität des primitiven hohen Rückkehrkanals müssen diese Alternative ausschließen. Eine bloße Minimalität der größeren Gesamtquelle reicht dafür nicht.

Die vorhandenen TFPT-Struktur- und Zahlenresultate bleiben Randbedingungen für eine solche Herkunftsherleitung. Ihre bloße Zusammenstellung bestimmt diesen fehlenden Stromanschluss noch nicht. Die27 Vorhersagekarten wurden in dieser Fortsetzung nicht erneut empirisch validiert oder als27 unabhängige Bestätigungen behandelt.

## 6. RH: stärkerer gemeinsamer Vergleich mit erhaltener Kopplung

Die bisherige schwache Aufteilung der alten Form verliert einen Faktor8. Aus der tatsächlichen Originalform wurde jetzt die Kopplung zwischen niedrigen und hohen Anteilen erhalten. Eine festgelegte neue Fehleraufteilung mit κ=10⁻⁶⁰ besteht die ganze80×80-Fehlerprüfung. Damit steigt der hohe Vergleichskoeffizient von127/128 auf1−10⁻⁶⁰, ohne die ursprüngliche Fehlerladung zu überschreiten.

Auf der bezeichneten niedrigen Diagnosequelle sinkt die obere Antwort von8.40479853·10⁻⁹ auf1.32687704·10⁻⁹. Das gewinnt gegenüber dem Faktor8-Vergleich einen Faktor6.33427 zurück. **Eine ältere reine Schur-Rechnung enthielt bereits einen minimal stärkeren niedrigen Wert.** Der neue Fortschritt besteht im stärkeren gemeinsamen Vergleich einschließlich des hohen Anteils und seiner Kopplung; die niedrige Zahl allein wird nicht als neue Entdeckung ausgegeben.

Für die wirkliche gesamte Schalenquelle fehlen weiterhin gemeinsam zertifizierte inverse Antworten e und b. Die neue obere Antwort hat die konkrete Form

\[
e/t+(\ell-b/t)^*S^{-1}(\ell-b/t),\qquad t=1-10^{-60}.
\]

Der gemischte Term b darf nicht verschwinden, nur weil er unbequem ist. Genau hier liegt der nächste zu beweisende Anschluss. Der gesamte schon berechnete endliche Träger ist außerdem nahezu orthogonal; sein winziger Rest ersetzt jedoch nicht den noch vorhandenen unendlichen Rest. Weder ein größeres vollständiges RH-Fenster noch RH ist mit dieser Fortsetzung bewiesen.

## 7. Was sich wirklich zusammenfügt

Die gemeinsame produktive Richtung ist jetzt konkreter: **Operationen und ihre gemischten Antworten erhalten, bevor man auf einzelne Zahlen reduziert.**

| Gebiet | Was die vollständige Verbindung zusätzlich trägt | Was zum vollständigen Problem fehlt |
|---|---|---|
| Ganze Gatequelle | Nichtkommutierende Wörter und eine exakte integrale Basis | Physische Auswahl, Zustand, Zeitgesetz und zulässige Instrumente |
| Faktorisierung | Gemischte Antwort erhaltener Potenzkoeffizienten | Günstige Herstellung nützlicher Ausgangsindizes aus N allein |
| RH | Gekoppelte inverse Antwort statt verlustreicher Einzelabschätzungen | Ganzes gemischtes inverses Gram, vollständige Schale und anschließender globaler Grenzübergang |
| TFPT | Markierter primitiver Paarvektor statt nur einer unmarkierten normierten Rückkehr | Physischer Herkunftsbeweis seines Stromanschlusses |
| P versus NP | Exakte Trennung von kompakter Darstellung und Zugriff auf eine Antwort | Allgemeiner Algorithmus samt Laufzeitbeweis oder gültiger unterer Schranke |

Das ist ein durch Beispiele und Sätze gestütztes Arbeitsprinzip. Es ist noch kein Satz, dass alle diese Paarungen aus einem einzigen universellen Zustand stammen oder in polynomialer Zeit zugänglich sind. Kleine algebraische Dimension bedeutet insbesondere nicht geringe Bitkosten oder billigen Zugriff auf den entscheidenden Koeffizienten.

Der nächste grundlegende Fortschritt muss daher eine tatsächliche neue Quelloperation liefern: für TFPT den markierten Stromanschluss, für RH das gemeinsame vollständige inverse Gram, für Faktorisierung eine begründete Herstellung hilfreicher Rückkehrzustände. An genau diesen drei Stellen kann der jetzige Ansatz seine behauptete universelle Wirkung beweisen.

## 8. Prüfstand und Unterlagen

Die Ergebnisse umfassen ausgeschriebene All-n-Beweise,814 exakte Dyadikkontrollen,440 Kontrollen der lokalen Rückkehranalyse,31 exakte Cap-/Krauskontrollen, die exakte Neunerbasis und20 weitere Leser-/Dynamikidentitäten sowie RH-Intervallläufe mit2048 und3072Bit. Der Hauptagent wiederholte den finalen RH-Lauf zusätzlich. Diese Zahlen bezeichnen Fehlerkontrollen und ersetzen nicht die allgemeinen Beweise. Die natürliche Grenze und der schnelle Auswerter erhielten unabhängige Agentenlektüren; die abschließende Gesamt-Radiuskontrolle des Auswerters wurde daraufhin ergänzt und erneut ausgeführt. Die zusätzliche unabhängige Lektüre der Wort-Algebra und dieses letzten kleinen Prüfschritts endete am Nutzungslimit. Für sie werden daher nur der ausgeschriebene Beweis und die exakten eigenen Prüfungen beansprucht. Eine externe Begutachtung oder vollständige formale Beweisverifikation wird nicht behauptet.

Die Originalquellen wurden erhalten. Der Forschungsgraph dient der Recherche und Herkunftskontrolle; seine teilweise Textabdeckung und ungeprüften Behauptungen werden nicht in eine vollständige Corpus-Prüfung umgedeutet. Die neuen nativen Resultate werden als geprüfte Forschungskandidaten dokumentiert, ohne neue RH-Beweisinferenz.

Die zugehörigen Detailbeweise und das Prüfpaket liegen neben diesem Bericht im Ausgabeordner. Das Paket enthält eigene Prüfer, Ergebnisse und Quellenverweise; die bezeichneten ursprünglichen RH-Daten und die lokale Intervallbibliothek bleiben explizite Voraussetzungen für deren Wiederholung.
