# TFPT / Universalraum: gemeinsame Schatten und ein ursprünglicher kausaler Prozess

Vollständige Fortschreibung v1.6.8, 15. September 2026. Forschungsbericht und unabhängige Prüfung der nachgereichten Forschungssynthese 1.0. Keine vollständige TOE.

## 1. Ergebnis und Leseschlüssel

Die drei parallel bearbeiteten Aufgaben liefern diesmal konkrete mathematische Anschlüsse: einen kleinen ursprünglichen Singulettmechanismus, die vollständige bedingte Schattenkarte des hellen Raums und einen kausalen Eingriff unter dem unveränderten Hamiltonoperator. Die nachgereichte Forschungssynthese verbindet diese Aufgaben sinnvoll durch gemeinsame Operationsgeschichten. Ihre mitgelieferten Rechnungen sind reproduziert; ein Satz in Abschnitt 8.4 benötigt jedoch eine Korrektur.

Die noch später eingegangenen Texte liefern außerdem eine frisch reproduzierte fünfte Bosonstufennorm. Eine unabhängig zertifizierte größere Variationskompression verbessert die Grundenergieobergrenze auf -1.13847609Δ und unter dem beibehaltenen N=63-Satz die untere Polenergiegrenze auf 0.01657709Δ. Dazu kommt ein neuer exakter Händigkeitstest des Feldprojektors. Der Nachtrag „Neue Norm, korrigierte Zustandszuordnung und Feldadapter“ enthält diese maßgeblichen Ergänzungen; ältere Ritzkennzahlen verschiedener Zustände werden dort ausdrücklich getrennt.

Die zentrale Vereinfachung ist nicht eine neue große Geometrie, sondern eine sorgfältig ausgewählte kleine gemeinsame Ausführung. Ein Zustand, seine messbaren Bilder und seine späteren Antworten müssen aus denselben Operatoren berechnet werden. Zusätzliche Zustände, Kontrollen und Referenzen werden dabei ausdrücklich mitgezählt.

**Exakt** bezeichnet algebraische Identitäten, Invarianzbeweise und rational/modular abgesicherte Ränge im angegebenen Modell. **Numerisch** bezeichnet unabhängige Gleitkomma-Rekonstruktionen und den vollständigen endlichen Dynamikvergleich. **Bedingt** heißt: Der Satz stimmt, benötigt aber ausdrücklich gewährte Präparationen, Kontrollen oder Messungen. **Offen** bleibt deren ursprüngliche Herleitung und die physikalische Fortsetzung. Prüfprogramme sind keine formale Beweisassistenten-Verifikation.

Die vollständige bisherige Hauptfassung v1.6.7 bleibt im historischen Teil wortgetreu erhalten. Die neuen Kapitel, die vollständigen drei Teilberichte, ihr gemeinsames Dreizustands-Addendum und alle drei Nachtragsprüfungen stehen davor. Das Quellenpaper bleibt als unveränderte Eingabe im Prüfpaket, nicht als still korrigierte Originaldatei. Aktuell maßgeblich sind diese Einordnung, die Korrekturen und die neu dokumentierten Ressourcenbedingungen.

## 2. Prüfung des nachgereichten Forschungspapers

Geprüft wurden das 33-seitige PDF, sein vollständiger Markdowntext, Prüfprotokoll, Quellenmanifest und eigene Ergebnisdatei sowie das zusätzlich vorhandene Reproduktionsarchiv. Die vollständige Synthese wurde gelesen; nicht jede der 74 historischen Quellen wurde neu bewiesen. Die relevanten PDF-Seiten 16 bis 20 und 22 wurden zusätzlich bildlich geprüft.

| Behauptung oder Baustein | Ergebnis der unabhängigen Prüfung |
|---|---|
| 74 eingefrorene Quellen | Alle Archivgrößen und SHA-256-Werte stimmen mit dem Manifest überein |
| Markdown, PDF und TeX | Gelieferte bzw. archivierte Dateien stimmen mit dem Prüfprotokoll überein |
| Neuester Stand S074 | Identisch mit der vollständigen hiesigen v1.6.7 einschließlich Prozess-/Schattennachtrag |
| 57 eigene Prüfbedingungen | Aus dem isoliert entpackten Paket normal und optimiert wiederholt; identische Ergebnisbytes |
| 20 übernommene Kettenprüfungen | Ebenso wiederholt; identische Ergebnisbytes |
| Grundzustand und frühere 822er-Suite | In dieser Runde nicht vollständig erneut ausgeführt; keine entsprechende Behauptung |
| Wortkernrekonstruktion | Unter den angegebenen Positivitäts-, Relations- und Beschränktheitsvoraussetzungen korrekt |
| Aussage zu der ersten Gramzeile in §8.4 | Zu korrigieren; siehe unten |
| Ein-Cartan-Referenz und Projektorgeometrie | Korrekte bedingte Konstruktionen, kein nativer physikalischer Ursprung |

### 2.1 Tatsächliche Korrektur: die erste Zeile genügt, wenn sie vollständig ist

Für eine unter Produkt und Adjungieren abgeschlossene Wortalgebra gilt definitionsgemäß

\[
\boxed{\Gamma(u,v)=\omega(u^\dagger v)=\Gamma(1,u^\dagger v).}
\]

Damit bestimmt die Gesamtheit aller Werte \(\Gamma(1,w)\) bereits den gesamten Gramkern. Der Satz in §8.4, Gleichheit nur von \(\Gamma(1,u)\) genüge nicht, ist ohne Einschränkung auf unvollständige Daten falsch. Die richtige Fassung lautet:

> Gleichheit nur endlich vieler Worterwartungswerte, einzelner Zeitkorrelationen oder Ausgangswahrscheinlichkeiten genügt im Allgemeinen nicht zur Identifikation des vollständigen Prozesses.

Die Korrektur betrifft nicht den GNS-Rekonstruktionssatz. Sie zeigt vielmehr: Die zweifach indizierte Grammatrix ist eine hilfreiche Organisation derselben vollständigen Daten, keine zusätzlich notwendige unabhängige Informationsquelle. Die Identität wird im eigenen Ressourcenprüfer auf einem nichtkommutativen Matrixbeispiel zusätzlich kontrolliert; der allgemeine Beweis ist die eine Gleichung oben. Die gelieferten 57 Prüfbedingungen hatten die fehlerhafte Formulierung nicht geprüft.

### 2.2 Welche Gleichheit ist tatsächlich beobachtbar?

Ein markierter komplexer Wortkern ist stärker als eine Liste gewöhnlicher Quantenkanäle. Beispielsweise liefern \(Z\) und \(-Z\) für jeden Zustand denselben Kanal:

\[
Z\rho Z^\dagger=(-Z)\rho(-Z)^\dagger.
\]

Mit \(\Omega=|0\rangle\) sind die markierten Wortwerte dagegen +1 und -1. Bei verfügbarer kohärenter Kontrolle der Zweige können diese Phasen relativ werden und verschiedene Interferenz ergeben. Ohne diese zusätzliche Kontrollmöglichkeit ist ihre Unterscheidung kein zugängliches Experiment. Diese Ressourcenfrage ist auch aus der Literatur zur Kontrolle unbekannter Operationen bekannt; unser konkreter Zwei-Zustandszeuge wird unabhängig direkt nachgerechnet. [Araújo, Feix, Costa und Brukner, 2014](https://arxiv.org/abs/1309.7976).

Folglich ist Kernelgleichheit ein hinreichender starker Identifikationsvertrag für phasenmarkierte gemeinsame Ausführungen. Sie ist nicht ohne Weiteres die notwendige Minimalbeschreibung jedes eingeschränkten Instrumentenvertrags. Man darf weder beobachtbare Interferenz wegquotientieren noch unzugängliche globale Kanalphasen als neue physikalische Unterschiede ausgeben.

### 2.3 Referenzsystem: richtige Bilanz, keine kostenlose Operation

Die Synthese ergänzt den früher zusätzlich gemischten Vierzustandskanal um eine zweistufige Referenz. Das acht-dimensionale Gesamtmodell erhält die betrachtete innere Cartanladung. Auf einem invarianten vierdimensionalen Unterraum ist sein Hamiltonoperator exakt der alte Transferblock plus ein skalares Energieglied. Die frühere Transferschranke wird deshalb korrekt übertragen, nicht neu aus der nativen Quelle erzeugt.

Der gewählte innere Cartanwert ist nicht die physische Zahl \(N=N_f+2N_b\). Die gesamte nichtabelsche Gruppe bleibt in dieser Konstruktion ungeprüft. Der Referenzwechsel wird bezahlt: Scharfe verschiedene Referenzladungen sind orthogonal. Nach Wegspuren der Referenz fehlen die Kreuzterme zwischen verschiedenen Systemladungen. Die gemeinsame kohärente Entwicklung ist somit kein unverändert wiederverwendbarer kohärenter Antrieb des isolierten Systems. Das Original benennt diese Grenzen bereits; sie werden bei der Integration beibehalten.

### 2.4 Projektorgeometrie: tragfähig, aber noch nicht nativ

Für eine Isometriefamilie J mit \(P=JJ^\dagger\) gilt

\[
A=iJ^\dagger dJ,\qquad
F=dA-iA\wedge A=i\,dJ^\dagger(I-P)\wedge dJ.
\]

Das verbindet Quantenmetrik und geometrische Phase eines wirklich bewegten Unterraums. Eine reine Basisdrehung im festen vollständigen Raum erzeugt keine solche Krümmung. Der im Paper gerechnete Kugelzeuge mit \(u=(\cos(\theta/2),e^{i\phi}\sin(\theta/2))\) und seiner selektiven Schleifenausbeute 1/8 stimmt. Die Parameterfamilie wird jedoch hinzugegeben. Die Projektorformulierung entspricht etablierten Verfahren der Quantengeometrie. [Graf und Piéchon, 2021](https://arxiv.org/abs/2102.09899).

Eine neue genaue Einschränkung folgt aus unserem ursprünglichen hellen Block: Sein Blochvektor hat bei reellen Kopplungen nur zwei Komponenten, \(n\propto(2a,0,-\Delta)\). Daher ist

\[
n\cdot(\partial_a n\times\partial_\Delta n)=0.
\]

Die glatte lokale Berry-Zweiform dieser realen Zweiparameterfamilie verschwindet außerhalb einer Entartung. Eine komplexe Kontrollphase oder eine andere tatsächlich bewegte Projektorfamilie wäre eine zusätzliche, noch herzuleitende Ressource. Globale Vorzeichenphasen auf anderen Parametergebieten werden dadurch nicht allgemein ausgeschlossen; eine gekrümmte Raumzeit folgt weder aus dem Kugelbeispiel noch aus diesem Nullbefund.

### 2.5 Weitere übernommene Richtungen

Die Blockresolventenformel und der endliche Duhamel-Adapterfehlervertrag sind korrekt und brauchbar. Die einfache Restschranke \(\|B\|^2/|\operatorname{Im}z|^3\) wird nahe der reellen Achse schwach; sie bestimmt keinen scharfen physikalischen Pol. Gemischte Wort- und Matrixmomente sind eine passende Fortsetzung der verzweigten Hamiltonkette. Das neue Paper hat diese größere Kontraktionsrechnung selbst noch nicht ausgeführt. Es liefert auch kein neues chirales Maß, keinen Spin-2-Sektor und keinen gemeinsamen 3+1D-Ursprung. Seine Zurückhaltung an diesen Stellen ist sachlich richtig.

## 3. Der gemeinsame ursprüngliche Ausgangspunkt

Alle drei eigenen Stränge verwenden denselben eingefrorenen Tensor W mit 60 Zeilen, 2016 Paarspalten und 480 signierten Einträgen. Es gilt exakt

\[
WW^\dagger=8I_{60},\quad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad
H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
\quad N=N_f+2N_b.
\]

Der Dateipin ist `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`. Der ursprüngliche Clifford-/Farbkonstruktor wurde im Mechanismusstrang erneut ausgeführt und reproduziert W eintragsweise. Die endliche Clockkonstruktion wurde in ihren vier angegebenen mathematischen Stufen wiederholt. Diese Wiederholung liefert die konkreten Koeffizienten und den passiven Lift; sie wählt weder die physikalische Kopplung noch Apparate oder eine Raumzeit.

Die neue Arbeit betrifft mehrere sauber bezeichnete Teilräume. Gleiche Quelle heißt nicht gleicher Zustand:

| Teilraum | Inhalt | Wofür benutzt |
|---|---|---|
| Heller Raum bei N=2, Dimension 120 | Kohärente Fermionpaare und ein Boson, je 60 innere Richtungen | Gemeinsame Schatten- und Zeitrekonstruktion |
| Ein nativer Stern bei N=2, Dimension 9 | Acht disjunkte Paare und ein gemeinsames Boson | Kausaler Phasenimpuls, einschließlich dunkler Richtungen |
| Neuer Singulett-Unterraum bei N=4, Dimension 2 | Zwei Bosonen bzw. ein Boson und zwei Fermionen | Kleinster hier explizit geschlossener voller G-Singulettmechanismus |
| N=4 mit neuer Referenz, Dimension 3 | Vakuum/Referenz plus die beiden Singulettzustände | Bedingter neutraler Ressourcenübergang |
| Früherer Grundzustand bei N=64 | Native geladene Polantwort | Nicht durch die neuen N=2-/N=4-Zeugen ersetzt |

Der Stern enthält sieben dunkle Paarrichtungen und ist nicht vollständig im hellen 120-Raum enthalten. Ein lokaler Phasenimpuls kann helle in dunkle Komponenten überführen. Deshalb darf die helle Tomographie nicht ohne weiteren Adapter als vollständige Tomographie des kausalen Sternversuchs ausgegeben werden.

## 4. Einfachster Mechanismus: zwei Zustände und eine genaue Operationsgrenze

Mit der aus W hergeleiteten invarianten Paarung \(\eta\) definiere

\[
B_+=\tfrac12 b^\dagger\eta b^\dagger,\qquad
R_+=\sum_{AB}\eta_{AB}b_A^\dagger P_B^\dagger.
\]

Die vollständige Anwendung der nativen Terme ergibt

\[
\sum_{AB}\eta_{AB}P_A^\dagger P_B^\dagger=0,
\quad T_-B_+|0\rangle=R_+|0\rangle,
\quad T_+R_+|0\rangle=16B_+|0\rangle.
\]

Die jeweils anderen Übergänge sind null. Die erste Identität wurde durch Normalordnung sämtlicher 3840 signierten Beiträge auf 960 Fermionquartetten geprüft. Mit

\[
\beta=B_+|0\rangle/\sqrt{30},\quad
\rho=R_+|0\rangle/\sqrt{480}
\]

ist der ganze H auf diesem invarianten Unterraum genau

\[
\boxed{H_4=\begin{pmatrix}2\Delta&4g\\4g&\Delta\end{pmatrix}.}
\]

Beide Zustände haben N=4 und sind volle innere G-Singuletts. Keine höhere Konfiguration wurde weggelassen. Am Prüfpunkt \(g/\Delta=1/20\) beträgt die maximale Umwandlungswahrscheinlichkeit exakt 4/29. Ihre Vorbereitung aus dem Vakuum ist dadurch nicht bewiesen.

Tatsächlich folgt für das dokumentierte Alphabet aus passiven Focklifts, X und Nb ein geschlossener Erhaltungssatz:

\[
\mathcal A_0\subseteq\{N\}'.
\]

Er gilt für beliebige Produkte, Adjungierte und Kommutatoren; weitere Wortlängen können ihn nicht umgehen. B+ und R+ ändern N um vier und liegen nicht in dieser Algebra. Der Ausschluss gilt für dieses geprüfte Alphabet, nicht für jede denkbare alternative Compilerrealisierung.

Eine minimale zusätzliche G-invariante, fermionparitätsgerade Operation ist nach Polynomialgrad \(Q=B_++B_-\). Unter zusätzlich separat zugänglichen X und Nb gilt exakt

\[
\boxed{R_++R_-=-[N_b,[Q,X]].}
\]

Man braucht also nicht zwei neue unabhängige Kopplungstensoren. Ein zusätzlicher Paargriff reicht algebraisch. Das ist keine bereits ausgeführte endliche Pulsynthese und keine Herkunft von Q.

Eine zweistufige, innerlich G-triviale Referenz mit N-Ladungen 0 und 4 bilanziert diesen einen zusätzlichen Griff. Auf \(|0,4_R\rangle,|\beta,0_R\rangle,|\rho,0_R\rangle\) folgt der exakte gemeinsame Block

\[
H_{\rm ref}=\begin{pmatrix}
E_R&\sqrt{30}\kappa&0\\
\sqrt{30}\kappa&2\Delta&4g\\
0&4g&\Delta
\end{pmatrix}.
\]

Er erhält volle innere G-Symmetrie und Gesamt-N=4. Referenz, Energie ER und Kopplung κ sind neue Ressourcen. Er löst ein anderes Ladungsproblem als die Ein-Cartan-Referenz im gelieferten Paper und erzeugt noch keinen räumlichen Transfer. Sein vollständiger Beweis und die reduzierte Zustandsbilanz stehen im Mechanismus-Teilbericht.

## 5. Gemeinsame Schattenkarte: welche Bilder reichen?

Der native Kodierer \(V=W^\dagger/\sqrt8\) bildet den inneren 60-Raum isometrisch in den Fermionpaarraum ab. Für jeden gewährten Operator O wird dessen Schatten auf demselben Zustand berechnet:

\[
\Phi_O(\sigma)=\operatorname{tr}(\sigma V^\dagger O V).
\]

Die Ränge sind am echten W exakt berechnet und durch obere Darstellungsgrenzen plus nichtverschwindende modulare Minoren abgesichert:

| Familie | Rang | Unsichtbarer Kern |
|---|---:|---:|
| Einzelbesetzungen | 24 | 3576 |
| Alle Einteilchenbilineare | 736 | 2864 |
| Ungedrehte Paarbesetzungen | 60 | 3540 |
| Bilineare und ungedrehte Paarbesetzungen | 772 | 2828 |
| G-gedrehte Paarbesetzungen | 3600 | 0 |

Die Identität ist jeweils enthalten. Bei bekannter Spur benötigt ein allgemeiner Zustand 3599 unabhängige reelle Parameter. Eine konkrete Familie aus 3465 gemeinsamen Projektorwerten, 99 Spin-Summen und 35 Farb-Summen erreicht diese Zahl. Die Minimalität bezieht sich auf unabhängige lineare Erwartungswerte, nicht auf Geräte oder Messwiederholungen.

Die orthogonalen Zustände \((|0\rangle\pm|30\rangle)/\sqrt2\) besitzen dieselben Bilinear- und ungedrehten Paarschatten. Eine explizite gedrehte Paarsonde unterscheidet sie mit Erwartungswerten 1/16 und 0. Das ist ein konkreter Interferenzzeuge dafür, welche Information vorher fehlte.

Acht vorher unbenutzte Zustände wurden numerisch aus der festen Familie rekonstruiert; der größte Matrixeintragsfehler lag unter \(7.6\cdot10^{-16}\). 96 zurückgehaltene Paarvorhersagen lagen unter \(5.8\cdot10^{-17}\) Fehler. Diese rauschfreien numerischen Kontrollen sind keine experimentelle Messung. Die G-Kontrollen und gemeinsamen Besetzungsmessungen werden weiterhin vorausgesetzt. Ihre Instrumente einschließlich Rückwirkung sind nicht hergeleitet.

## 6. Eigenes Bindeglied: aus Schatten zu mehreren Zeiten die fehlende Phase zurückgewinnen

Auf dem hellen Raum gilt

\[
H_{\rm hell}=h\otimes I_{60},\qquad
h=\begin{pmatrix}0&a\\a&\Delta\end{pmatrix},\qquad a=\sqrt8g.
\]

Schreibe die gemeinsame Zustandsmatrix in Paar-/Bosonblöcken. Die vier inneren hermiteschen Matrizen

\[
S=\sigma_{PP}+\sigma_{BB},\quad Z=\sigma_{PP}-\sigma_{BB},
\quad X=\sigma_{PB}+\sigma_{BP},\quad
Y=i(\sigma_{PB}-\sigma_{BP})
\]

erfüllen exakt die geschlossene, matrixwertige Gleichung

\[
\boxed{\dot S=0,\quad\dot X=\Delta Y,\quad
\dot Y=-\Delta X-2aZ,\quad\dot Z=2aY.}
\]

Dies ist derselbe ursprüngliche H, kein passend erfundener Ersatzprozess. Die Zustände \((|P\rangle\pm i|B\rangle)/\sqrt2\) liefern dieselben momentanen Paar- und Bosonbilder. Ihre anfänglichen Änderungen der Paarwahrscheinlichkeit unterscheiden sich jedoch um 2a. Momentane Schatten allein besitzen daher keine autonome Entwicklung.

Mit \(\omega=\sqrt{\Delta^2+4a^2}\), \(\theta=\omega t\) lautet die später sichtbare Z-Matrix

\[
Z(t)=-\frac{2a\Delta(1-\cos\theta)}{\omega^2}X(0)
+\frac{2a\sin\theta}{\omega}Y(0)
+\frac{\Delta^2+4a^2\cos\theta}{\omega^2}Z(0).
\]

Die drei Zeiten mit \(\theta=0,\pi/2,\pi\) liefern eine lineare Antwortmatrix R mit

\[
\det R=\frac{8a^2\Delta}{\omega^3}\ne0
\quad(a\Delta\ne0).
\]

Damit sind X,Y,Z und zusammen mit S der vollständige gemeinsame Zustand bestimmbar. Eine exakt positive, intern korrelierte Testdichtematrix wurde symbolisch rekonstruiert; ihre nicht zum Aufbau benutzte Antwort bei \(\theta=\pi/3\) wurde exakt vorhergesagt.

**Die entscheidende Kalibrierung:** Paarsonden liefern \(\tfrac18 P\otimes|q\rangle\langle q|\), Bosonsonden dagegen \(B\otimes|q\rangle\langle q|\). Es werden unnormierte Zweigmatrizen einschließlich Zweigwahrscheinlichkeit gebraucht. Nur bedingt normierte Zustände reichen nicht. Die Messungen setzen wiederholbar präparierte Exemplare, bekannte a und Δ und kalibrierte Zeiten voraus.

Die vollständigen inneren Sondefamilien aus Abschnitt 5 ergeben zusammen mit beiden Zweigen Operatorrang \(4\cdot3600=14400\), also 14399 freie normierte Zustandsparameter auf dem 120-Raum. Dies ist ein bedingter Tomographiesatz, keine Vergrößerung der physikalischen Raumdimension.

### Warum nur ein Schatten auch nach beliebig langer Zeit nicht reicht

Für alle t gilt exakt \(\operatorname{tr}[P(t)h]=0\). Der Operatororbit einer einzigen Paarsonde hat auf dem Zweizustandsfaktor Rang drei statt vier. Mit sämtlichen inneren Sonden bleibt der unsichtbare Raum

\[
h\otimes\operatorname{Herm}(60).
\]

Selbst bekannte Gesamtspur eins lässt 3599 unsichtbare Richtungen übrig. Man benötigt eine Information über die zweite Zweigmatrix, nicht bloß noch mehr Zeitpunkte desselben unvollständigen Bildes. Bei a=0 oder Δ=0 verliert die angegebene Drei-Zeit-Rekonstruktion weitere Richtungen. Das sind genaue Grenzen, keine mangelnde numerische Genauigkeit.

## 7. Echter kausaler Eingriff ohne zusätzlichen Hoppingterm

Jede aktive W-Spalte gehört genau einer Zeile; jede Zeile enthält acht disjunkte Fermionpaare. Der ganze N=2-Raum zerfällt deshalb in 60 invariante neundimensionale Sterne und 1536 ungekoppelte Paare. Einschließlich der sieben dunklen Richtungen je Stern ergibt sich wieder dunkle Dimension 1956.

Im ersten Stern starte man in \(f_4^\dagger f_{57}^\dagger|0\rangle\). Nach nativer Vorentwicklung wird entweder nichts getan oder die gezielte lokale Phase \(Z_4=(-1)^{n_4}\) angewendet. Nach weiterer identischer Entwicklung wird \(n_5\) ausgelesen:

\[
|4,57\rangle\ \xrightarrow{U_T}\
\{I\text{ oder }Z_4\}\ \xrightarrow{U_T}\ n_5.
\]

Z4 erhält N, ist eine unitäre spurtreue Operation und kommutiert mit n5. Unmittelbar beim Eingriff bleibt die Besetzungsstatistik von Mode 5 deshalb für jeden Zustand gleich. Der spätere Effekt ist somit kein direkter Zugriff auf den Empfänger.

Setze

\[
\Omega=\sqrt{\Delta^2/4+8g^2},\quad T=\pi/\Omega,
\quad d=\Delta/(2\Omega),\quad x=4\cos^2(\pi d/2).
\]

In beiden Armen gilt am Ende exakt Nf=2 und Nb=0, ohne Nachselektion. Die Wahrscheinlichkeiten und ihre Differenz sind

\[
p_{\rm frei}=\frac{x(4-x)}{64},\quad
p_{\rm Impuls}=\frac{9x^2}{1024},\quad
\boxed{\delta_{4\to5}=\frac{x(25x-64)}{1024}.}
\]

Für \(0<g^2\le3\Delta^2/32\) ist die Differenz strikt negativ. Bei Δ=1 und g=1/20 erhält man numerisch

\[
T\approx6.0459978807807,\quad
p_{\rm frei}\approx0.00087491599417248,\quad
p_{\rm Impuls}\approx0.0000017344871305812.
\]

Das entspricht etwa 0.08749 Prozent gegenüber 0.0001734 Prozent Besetzungswahrscheinlichkeit. Der Effekt ist klein, aber der Nichtnullnachweis ist exakt. Ein unabhängiger numerischer Lauf auf dem gesamten 2076-dimensionalen Hamiltonoperator bestätigt die vollständigen Zustände und die Negativkontrolle ohne Vorentwicklung.

**Geschlossen ist die bedingte mathematische Frage:** Der ursprüngliche H kann eine nachweisbare Moden-zu-Moden-Wirkung vermitteln; ein zusätzlicher Linkterm ist für diesen Zeugen nicht nötig. **Nicht geschlossen ist die Herkunft** der Produktpräparation, der einzeln adressierbaren Phase und des Besetzungsinstruments. Der Phasenimpuls ist eine hinzugewährte Kontrolle, auch wenn die freie Dynamik unverändert bleibt. Die Moden sind noch keine nachgewiesenen räumlich getrennten Labore. Dies ist außerdem nicht die Ausbreitung des früher bewiesenen N=64-Entnahmepols.

### 7.1 Noch kleiner: derselbe Dreizustandsraum trägt Schatten und Eingriff

Für den gerade beschriebenen Versuch genügt sogar der gemeinsame Raum

\[
\mathcal K_3=\operatorname{span}\{|p_0\rangle,|R_7\rangle,|b_0\rangle\},
\quad |R_7\rangle=\tfrac1{\sqrt7}\sum_{q=1}^7s_q|p_q\rangle.
\]

Die s sind die ursprünglichen W-Vorzeichen. Dieser Raum enthält die notwendige dunkle Richtung; er wird nicht mit einem einzelnen hellen Zweizustandsblock verwechselt. Mit der expliziten Isometrie J gilt ohne Rest HJ=Jh3 und Z4J=Jz3, wobei

\[
h_3=\begin{pmatrix}0&0&-g\\0&0&\sqrt7g\\-g&\sqrt7g&\Delta\end{pmatrix},
\quad z_3=\operatorname{diag}(-1,1,1),\quad
e_3=J^\dagger n_5J=\operatorname{diag}(0,1/7,0),
\quad b_3=\operatorname{diag}(0,0,1).
\]

Definiere L(O)=i[h3,O] und C(O)=z3Oz3. Die neun hermiteschen Operatoren

\[
e_3,b_3,Le_3,Lb_3,L^2e_3,L^2b_3,L^3e_3,CL^2e_3,CL^2b_3
\]

besitzen in den angegebenen reellen Matrixkoordinaten die Determinante

\[
\boxed{\det M=8\Delta^3g^{10}/343\ne0.}
\]

Sie bestimmen folglich jeden Zustand auf genau dem Träger des kausalen Versuchs. Die benötigten Daten sind terminale Besetzungswahrscheinlichkeiten und ihre zeitlichen Ableitungen bis Ordnung drei, mit und ohne vorangestellten Phasenimpuls. Bei bekannter Normierung genügt sogar die autonome Zeitfamilie mit Ableitungen bis Ordnung vier. Der Impuls ist für diesen normierten Tomographiesatz also nicht zwingend, wohl aber der untersuchte Eingriff im kausalen Vergleich.

Dies verbindet die beiden Aufgaben auf derselben kleinen Ausführung, nicht nur auf Teilräumen mit ähnlichen Spektren. Es setzt bekannte Dynamik, identische frische Zustände, kalibrierte Zeiten und präzise Ableitungsdaten voraus. Ein endliches robustes Abtastverfahren ist noch nicht konstruiert. Die im Teilbericht exakt gerechnete konservative Fehlergrenze kann bei schwacher Kopplung große Fehlerverstärkung zulassen.

**Wichtige Instrumentengrenze:** n5 erhält den Raum nicht. Es gilt

\[
(n_5J-Je_3)^\dagger(n_5J-Je_3)=\operatorname{diag}(0,6/49,0).
\]

Eine nichtselektive projektive n5-Messung lässt aus R7 das Gewicht 12/49 außerhalb von K3 zurück. Die Reduktion gilt bis zur Endmessung und für Tomographie mit frischen Exemplaren, nicht für beliebige weitere Messfolgen desselben Exemplars. Ein wirklich grobes Lüders-Instrument auf alle sieben Restpaare würde den Raum erhalten; feines Auslesen mit anschließendem Vergessen der Labels ist ein anderes Instrument und verliert sogar Gewicht 6/7. Gerade diese Unterscheidung muss ein ursprüngliches Aufzeichnungsinstrument respektieren.

## 8. Was Holografie hier sinnvoll bedeutet

Bildlich sind die verschiedenen Beschreibungen Ansichten derselben Maschine. Eine Ansicht zeigt Besetzungen, eine andere innere Paarstruktur, eine dritte das spätere Verhalten nach einem Eingriff. Ihre gemeinsame Kalibrierung kann die verborgenen Phasen bestimmen. Abschnitt 6 realisiert genau diese Idee im endlichen hellen Raum.

Das ist zunächst Informationsrekonstruktion, nicht bereits gravitative Holografie. Es wurden weder eine physische Raumgrenze noch ein Flächengesetz oder eine Bulk-Rand-Dualität hergeleitet. Das Wort Schatten bekommt hier einen überprüfbaren Inhalt: eine konkrete Operatorabbildung, ihren Kern, ein gezieltes zusätzliches Messergebnis und eine zurückgehaltene Vorhersage. Ähnliche Zahlen oder Spektren ohne gemeinsame Abbildung genügen weiterhin nicht.

## 9. Nächste entscheidende Nachweise

**Übergeordnete Frage: Welche ursprüngliche Kompositionsregel erzeugt gemeinsam unterscheidbare Vorkommen, ihre Bewegung, ihren Zustand und ihre Instrumente?** Die letzte nachgereichte fundamentale Reduktion trifft diese Frage. Ein genaueres lokales Spektrum kann sie nicht ersetzen. Die folgenden kleinen Prüfungen dienen als überprüfbare Annahmekriterien für eine solche Regel; sie sind keine Ersatzdefinition von Raum und kein Beweis, dass es zwingend getrennte kopierte Banken sein müssen.

**Erste Priorität: den kleinen Versuch an den Compiler anschließen.** Ein einziger vollständiger Vertrag für Präparation, Phase und terminale Auslesung wäre aussagekräftiger als eine weitere allgemeine Matrixfamilie. Als Ziel dienen der konkrete N=2-Eingriff und sein abgesicherter Effekt. Zu liefern ist ein ursprüngliches Instrument oder ein expliziter Adapter aus dem vorhandenen Kontextträger einschließlich Zustand, Ladung und Aufzeichnung. Ein Matrixeintrag oder eine Gruppenzugehörigkeit allein besteht diesen Test nicht. Eine begründete globale Zustandsregel darf dabei nicht mit einer externen Laborpräparation des ganzen Universums verwechselt werden.

**Zweite Priorität: dieselbe niedrige geladene Anregung bewegen.** Die neuen kleinen Sektoren lösen den früheren N=64-Anschluss nicht automatisch. Gesucht ist ein nichtskalarer Übergang auf der tatsächlich abgesicherten geladenen Antwort, mit kontrollierter Restkopplung und auf demselben Grundzustand. Reine Überlappung innerhalb eines exakt entarteten Polraums erzeugt weiter kein Hopping. Matrixmomente und die geprüfte Blockresolvente sind dafür ein konkreter Ansatz.

**Dritte Priorität: den Feldadapter einschließlich Boosts schließen.** Der neue Händigkeitstest unterscheidet einen gültigen gleichhändigen Projektor von einem nur unter Drehungen gültigen Adapter. Die konkrete geladene Mode muss mit richtigen Indizes, CAR, W-Kontraktion und ihrem Matrixelement auf Ω abgebildet werden. Parallel kann ein aus verfügbaren Operationen oder dynamischen Freiheitsgraden hervorgehendes P(λ) mit kontrollierter Lücke und nichtverschwindender Krümmung untersucht werden. Die reale Zweikomponentenfamilie allein liefert keinen solchen nativen Geometrieschritt. Feld- und Geometrieprüfung müssen an derselben Konstruktion bleiben.

Die separaten mathematischen Fragen dieser Runde werden damit beantwortet, ohne einen Abschluss der übergeordneten Physik zu behaupten.

## 10. T1 bis T8 nach dieser Runde

Die Bezeichnungen folgen der Arbeitszuordnung der geprüften Synthese; die jeweiligen vollständigen Tore bleiben offen.

| Tor | Neuer Beitrag | Noch fehlender entscheidender Inhalt |
|---|---|---|
| T1 Ursprung/Auswahl | Tatsächlicher W-/Clock-Replay, vollständiger N-Erhaltungsausschluss des dokumentierten Alphabets | Auswahl des Prozesskerns und ausführbarer Primitive; physisches g/Δ |
| T2 Half-Charge/E8 | Neue exakte Operator- und Ressourcenbilanz | Renormierter geladener Adapter mit Energie-, Adjungierten-, E8- und Clockkontrolle |
| T3 gemeinsamer 3+1D-Ursprung | Kausaler Eingriff unter ursprünglichem H im festen N=2-Sektor | Abgeleitete lokale Teile, Distanz, Raumdimension und gemeinsamer 3+1D-Parent |
| T4 chirale Materie | Exakter gleichhändiger Ausleseprojektor und gegengängiger Boost-Gegenzeuge | Nativer relativistischer Feldadapter, chirales Maß, Anomalien, Spiegelentkopplung |
| T5 Kontinuum/Dynamik | Exakte endliche Schließungen, bedingte Mehrzeitrekonstruktion | Größenuniforme Fehler, relativistischer wechselwirkender Limes, Streuung |
| T6 Parameter/Spektren | Neue ν5, strengere Ritz-/Polschranke und korrigierte geladene Variationsmomente | Physische Kopplungsauswahl und einheitliche Übertragung zu gemessenen Größen |
| T7 Gravitation | Projektorgeometrie bestätigt, native reale Berry-Zweiform eingegrenzt | Positiver dynamischer Spin 2 und universelle Kopplung aus demselben Parent |
| T8 Zustand/Instrumente | Referenzverbrauch, explizite Messressourcen und Phasenkontrolle bilanziert | Ursprüngliche Präparation, Apparate, Aufzeichnung und Wiederverwendung |

Es gibt auch keinen neuen Beweis von RH, effizienter allgemeiner Faktorisierung oder einer P-versus-NP-Aussage. Diese Runde testet eine konkrete TFPT-Prozesskette und überträgt endliche Ergebnisse nicht auf andere offene Probleme.

## 11. Reproduktionsumfang

Der gemeinsame Replay führt alle eigenen mathematischen Prüfer normal und optimiert mit Warnungen als Fehler aus. Die Teilberichte unterscheiden exakte Identitäten von numerischen Kontrollen. Die 57 Prüfbedingungen des gelieferten Papers und dessen 20 übernommene Kettenprüfungen werden separat ausgewiesen, nicht als neue eigene Entdeckungen addiert. Sie decken nicht automatisch jeden Satz des Papers ab; die Korrektur in §8.4 zeigt dies ausdrücklich.

Das Paket enthält sämtliche unveränderten Eingaben, Teilberichte und Ergebnisdateien. Der Extraktions-Replay verwendet nur eingefrorene Dateien, keine sich verändernden Repositoryquellen. Die große ursprüngliche Grundzustandsprüfung und die gesamte frühere 822er-Suite wurden in dieser Runde nicht erneut ausgeführt. Frühere entsprechende Befunde werden als Vorbefunde bewahrt, nicht als frisch bestätigt ausgegeben.
