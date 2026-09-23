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


---

# Nachgereichte Texte: neue Norm, korrigierte Zustandszuordnung und Feldadapter

Die drei während der laufenden Prüfung nachgereichten Texte wurden vollständig gelesen und unverändert eingefroren. Sie sind keine Anweisungen, Ergebnisse ungeprüft zu übernehmen. Zwei Texte vereinfachen ältere Arbeitsstände stark; die dritte längere Forschungsnotiz enthält ausführlichere Beweise einer bereits bekannten grundsätzlichen Diagnose.

## A. Ein tatsächlich neuer Rechenwert trägt eine stärkere Schranke

Die Norm der fünften reinen Bosonstufe ist gegenüber dem hiesigen v1.6.7-Snapshot neu:

\[
\nu_5=1\,866\,738\,327\,552\,000.
\]

Die eingefrorene ursprüngliche Spur-/Wick-Rechnung wurde unabhängig erneut ausgeführt: alle Normen von ν1 bis ν5, bei ν5 genau 840 Wick-Netzwerke in 93 vorzeichentreuen Isomorphieklassen, mit Python-Ganzzahlen statt gerundeter Netzwerkarithmetik. Normaler und optimierter Lauf liefern identische Ergebnisbytes. Dies ist ein frischer Replay derselben Methode, keine zweite unabhängige Methode für ν5. Die kleineren Normen stimmen mit den bereits vorhandenen unabhängigen Zertifikaten überein.

Aus den sechs normierten Vektoren v0 bis v5 entsteht eine echte Variationskompression. Ihre Diagonale ist kΔ, ihre benachbarte Kopplung \(g\sqrt{\nu_{k+1}/\nu_k}\). Fügt man den bereits exakt konstruierten orthogonalen Zwei-Boson-Rücklaufrest w2 hinzu, ergibt sich eine siebendimensionale Kompression. Seine zusätzliche Kopplung liegt zu v3; sie ist \(g\|w_2\|/\sqrt{\nu_3}\). Die übrigen angegebenen Nullstellen folgen aus Bosonzahl und Orthogonalität.

Unabhängige rationale Sturm-Zählung liefert

\[
-1.13847420<E_{6,\rm Ritz}/\Delta<-1.13847419,
\]
\[
-1.13847610<E_{7,\rm Ritz}/\Delta<-1.13847609.
\]

Dies sind **keine invarianten Unterräume** und nicht die sechste bzw. siebte Stufe der vollständigen Hamilton-Lanczoskette. Sie sind dennoch gültige Variationsräume. Deshalb folgt streng

\[
\boxed{E_0<-1.13847609\Delta.}
\]

Zusammen mit dem beibehaltenen, in dieser Runde nicht vollständig neu bewiesenen N=63-Satz \(E_h>-1.121899\Delta\) erhält man die verbesserte Entnahmegrenze

\[
\boxed{\epsilon=E_h-E_0>0.01657709\Delta.}
\]

Sie ersetzt im aktuellen Stand die schwächere untere Schranke 0.00773911Δ aus v1.6.7. Die obere Grenze 0.039079764Δ und das bisherige Liniengewicht über 88.007628 Prozent werden dadurch nicht automatisch verändert. Es wurde kein exakter Zentralwert des Grundzustands oder Pols gefunden.

## B. Die einfache Darstellung vermischt zwei Näherungszustände

Die Werte um -1.138476Δ, mittlere Bosonzahl 1.0177445, Überlappung mit F von 0.3498904 und Bosonzahl-Shannonwert 1.8712436 Bit gehören zum größeren siebendimensionalen Ritz-Zustand. Die im selben Text genannten Gewichte 0.973684 und 0.026316 gehören dagegen ausdrücklich zu der älteren fünfdimensionalen Basis v0 bis v3 plus w2. Deren Energie liegt um -1.0942319Δ und ihre mittlere Bosonzahl um 0.8421159.

Die unterschiedlichen Werte wurden aus den beiden kleinen Matrizen unabhängig nachgerechnet. Für den **größeren selben Ritz-Zustand** folgen stattdessen die gesamten Entnahme-/Additionsnormen ungefähr 0.9681955 und 0.0318045. Keine dieser Näherungszahlen ist das Gewicht des isolierten Pols auf dem wahren stationären Grundzustand. Auch die angegebenen Entnahme-/Additionsenergiemittel aus der kleineren Basis sind keine exakten Polenergien.

Eine zusätzliche CAR-Summenregelrechnung bestimmt die ersten geladenen Momente aus genau denselben kleinen Matrizen, ohne Millionen Besetzungsamplituden neu zu konstruieren. Sie reproduziert die gespeicherten Mittelwerte der Fünferbasis und ergibt für den größeren Siebener-Ritz-Zustand stattdessen mittlere Entnahmekosten von etwa 0.03479766990Δ und Additionskosten von etwa 1.05931330814Δ. Das sind korrigierte numerische Variationszustandswerte, keine Ω-Polenergien. Die allgemeinen Identitäten und die reproduzierbare Auswertung stehen im ausführlichen Nachtrag A.

Die Aussage „unser schwächerer Sektorvergleich schließt die Lücke nicht“ ist korrekt. Sie widerlegt aber keinen stärkeren vorherigen Grundzustandssatz für denselben Modellvertrag. Das eingefrorene fremde Gesamt-Replaymanifest stand noch auf RUNNING. Deshalb wird hier nur unser abgeschlossener isolierter Norm- und Ritz-Replay behauptet, nicht der Abschluss der fremden Gesamtrunde.

Der Text nennt eine fast geschlossene Leiter. Der bereits bewiesene Rücklaufrest bleibt jedoch ungleich null. 33 mögliche Bosonzahlstufen bedeuten nicht 33 Vektoren für den gesamten Prozess. Auch alle 33 skalaren Normen würden zunächst einen bestimmten Variationsraum beschreiben, nicht automatisch die volle Antwort.

## C. Ein neuer entscheidender Test am Feldprojektor

Der Spin-1/2-Projektor im zweiten Text trägt unter einer bestimmten Händigkeit. Für

\[
(1,0)\otimes(1/2,0)=(3/2,0)\oplus(1/2,0)
\]

wurde eine explizite Epsilon-Auslese C samt Wiedereinsetzung R konstruiert. Alle gleichhändigen sl(2)-Intertwining-Gleichungen gelten, CR=I2 und RC=P1/2. Die Gram-Matrix der sechs verwendeten unnormierten Koordinaten ist diag(1,1,2,2,1,1); diese Metrik darf nicht durch die Einheitsmatrix ersetzt werden.

Wird der zweite Faktor jedoch als **wörtlich adjungiertes linkes Weylfeld** gelesen, hat er entgegengesetzte Händigkeit. Dann gilt

\[
(1,0)\otimes(0,1/2)=(1,1/2),
\]

ein irreduzibler Lorentzraum. Unter Drehungen gibt es weiterhin Spin 3/2 und Spin 1/2; der Rotationsprojektor ist aber nicht boostinvariant. Der neue exakte Prüfer findet

\[
[P_{1/2},J_z]=0,\qquad
\operatorname{rank}[P_{1/2},K_z]=4.
\]

Das ist ein konkreter Test, weshalb „das Feldwörterbuch ist fertig“ zu weit geht. Es ist **kein pauschaler Ausschluss des ursprünglichen Modenkomposits**: Ein Fock-Erzeuger f† ist nicht automatisch ein adjungiertes lokales Weylfeld. Eine linke Weylfeldentwicklung enthält bereits Erzeugungs- und Vernichtungsterme mit passenden Spinorwellenfunktionen. Eine unabhängige oder korrekt ladungskonjugierte gleichhändige Konstruktion bleibt möglich; sie benötigt den tatsächlichen Adapter mit Ladung, CAR, W und Dynamik. Die Konventionen entsprechen [Dreiner, Haber und Martin, Abschnitte 2 und 3](https://arxiv.org/abs/0812.1594).

Der nächste Test ist damit konkret: denselben geladenen Operator samt gepunkteten/ungepunkteten Indizes abbilden, sowohl Drehungen als auch Boosts verschränken, dann sein wirkliches Matrixelement am nativen Grundzustand bestimmen. Ein Projektorrang von zwei aus sechs ist kein zustandsunabhängiges Spektralgewicht von einem Drittel. Positive Zustände mit Gewicht null und eins sind explizit geprüft.

## D. Weitere Übernahmegrenzen

- Die Clock ist nach der späteren konkreten Konstruktion ein Element der inneren Spin(10)-Darstellung. Die ältere Formulierung „äußerer Handgriff“ wird nicht als neue Herkunftstatsache übernommen.
- Die große Kommutantdimension zählt nicht direkt physische Freiheitsgrade. Ein skalarer Kommutant bedeutet nicht automatisch beliebige dynamische Kontrolle. Als exakter Gegenzeuge haben Spin-1-Kontrollen einen skalaren Kommutanten, aber Lie-Dimension drei statt acht.
- Die Viererregel N=0 modulo vier ist eine notwendige Singulettregel. Ohne globalen Eindeutigkeitssatz darf sie tiefere entartete Nichtsingulett-Grundzustände nicht ausschließen.
- Das skalare Grassmann-Nullresultat ist korrekt in der angegebenen lokalen, ableitungsfreien, gleichhändigen Ein-Kopie-Klasse mit unverändertem W. Es verbietet nicht jede denkbare skalare Erweiterung mit anderen Feldern, Ableitungen oder unabhängigen Komponenten.
- Die angegebenen getrennten Casimire sind wertvolle minimale Sonden; nicht jede sinnvolle Kontrolle erfordert sofort die ganze Gruppe. Schon ein einzeln hinreichend trennender Casimir kann die betrachteten dunklen Typen unterscheiden.

## E. Die dritte Notiz: richtige Richtung, überwiegend bereits berücksichtigt

Die längere fundamentale Reduktion ergänzt den bereits eingefrorenen früheren Kommentar um die ausführliche Herleitung. Ihr stärkster Satz trägt: Bei invariantem H, invariantem Ω und irreduzibler innerer Entnahmefamilie gilt für die **gesamte** lokale Antwort

\[
T^\dagger F(H-E_0)T=\gamma_F I_{64},\qquad
C_{rs}(t)=\delta_{rs}c(t).
\]

Dieser Satz umfasst Nebenlinien. Beliebig genaues c(t) erzeugt deshalb keinen Ortsindex in den 64 inneren Labels. Er verbietet weder die neu geprüften N=2-Interventionen auf anderen präparierten Zuständen noch Bewegung auf zusätzlichen Multiplizitätsräumen.

Auch die Unterscheidung zwischen dem Kommutanten der inneren Symmetrie und demjenigen der verfügbaren Operationen ist richtig. Der eine lässt symmetrieverträgliche Dynamik auf unabhängigen Vorkommen zu, der andere beschreibt die Reichweite der gewährten Zugriffe. Viele Vorkommen sind noch keine räumlichen Orte.

Die bekannte Paritätsstruktur einer Bank wird korrekt eingegrenzt: Wenn Bosonen unverändert bleiben, erhält der verbundene Paargraph nur globale Fermionparität, keine echte Teilmengenparität. Unabhängig kopierte Banken können durch ihre gewählte Zusammensetzung neue lokale Erhaltungsgrößen bekommen. Deshalb ist die Herleitung einer globalen Kompositionsregel eine echte Alternative zur bloßen Ergänzung eines Links zwischen fertigen Kopien.

Die Zustandsfrage darf ebenfalls einfacher gestellt werden: Bei festem Gesamt-N ist μN nur ein skalares Energieglied. Eine fundamentale Theorie muss keine unbeobachtbare Energiekonvention auswählen. Sie muss aber den physisch relevanten Zustand oder die Randbedingung begründen. Dazu wird kein Experimentator außerhalb des Universums gebraucht, der das Universum aus dem leeren Fockzustand präpariert. Die interne Präparation eines konkreten Tests bleibt eine davon verschiedene Aufgabe.

Auch das konkrete Gegenbeispiel zur sektorübergreifenden Zustandswahl ist korrekt. Die beibehaltene Voll-Fock-Casimirschranke ergibt bei g/Δ=1/20 und μ/Δ=1/50

\[
H_\mu\ge\left(\mu-\frac{15g^2}{2\Delta}\right)N_f+2\mu N_b
\ge\frac{\Delta}{800}N.
\]

Der leere Zustand ist dann eindeutig energetisch bevorzugt. Die Quellenpins des früheren Zertifikats wurden abgeglichen; sein großer Lauf wurde nicht wiederholt. Der genaue Koeffizient 1/800 wurde erneut rational geprüft. In der Interventionsformulierung ist „nichtverschwindende Differenz“ die passende Bedingung; auch unser negativer Effekt ist ein Nachweis.

**Übernahmeentscheidung:** Diese Notiz trägt als Priorisierung. Eine zusätzliche globale Quell-/Kompositionsregel muss voneinander unterscheidbare Vorkommen, ihre Kopplung, den Zustand und die internen Instrumente gemeinsam liefern. Sie ist im Text noch nicht konstruiert. Der neu gelöste Dreizustandsversuch ist ein kleiner positiver Referenzvertrag, keine solche wachsende Welt. Den exakten lokalen Pol weiter zu verfeinern bleibt nützlich, ersetzt aber diese Herkunftsfrage nicht.


### Automatisch aus dem abgeschlossenen Replay

| Eigener Strang | Exakte Bedingungen | Numerische Bedingungen |
|---|---:|---:|
| causal | 662 | 10 |
| common3 | 43 | 0 |
| late_field | 36 | 0 |
| late_moments | 2 | 2 |
| late_norm | 36 | 10 |
| mechanism | 261 | 0 |
| phase_bridge | 32 | 0 |
| resource_boundary | 24 | 0 |
| shadows | 5417 | 17 |

Je normalem und optimiertem Lauf: 6513 eigene exakte beziehungsweise faktische und 39 numerische Bedingungen. Die erste Kategorie enthält Quellenpins und Strukturprüfungen, nicht nur mathematische Identitäten. Hinzu kommen 17 erhaltene native Konstruktorguards und 1239 erhaltene Spurnetzwerk-Quellguards, separat 57 Synthese- und 20 historische Kettenbedingungen.


---

# Teilbericht A: ursprünglicher Mechanismus und Referenzbilanz

# Ursprünglicher Mechanismus, Erhaltung und die kleinste zusätzliche Ressource

## Ergebnis

**Exakt neu:** Am unveränderten Tensor schließt ein zweidimensionaler
G-Singulett-Unterraum mit physischer Ladung N=4 unter dem gesamten nativen H.
Seine Matrix ist

\[
H_{4,\mathrm{klein}}=
\begin{pmatrix}2\Delta&4g\\4g&\Delta\end{pmatrix}.
\]

Der Koeffizient 4 und die Invarianz wurden aus sämtlichen ursprünglichen
Paartermen berechnet. Es handelt sich um einen invarianten Unterraum, keine
abgeschnittene Näherung. Damit liegt ein kleiner ursprünglicher Mechanismus
zwischen zwei verschiedenen Zusammensetzungen desselben Singuletttyps vor.
Seine Vorbereitung aus dem Vakuum ist durch diese Rechnung nicht geliefert.

**Exakt ausgeschlossen:** Kein Wort aus X, Nb und den dokumentierten passiven
Focklifts von Clock und innerer Gruppe kann den Systemsektor N verändern.
Das gilt für beliebige Wortlängen. Die zusätzlichen Terme B+ und R+ aus
v1.6.7 können daher in diesem festen Alphabet nicht durch weitere
Kommutatorsuche gefunden werden.

**Bedingt konstruiert:** Ein zusätzliches Bosonpaarinstrument ist die
einfachste invariant mögliche Erweiterung nach Polynomialgrad. Zusammen
mit einer zweistufigen G-trivialen Referenz entsteht ein exakt geschlossener
Dreizustandsprozess mit voller Spin(10)×SU(4)-Invarianz und Ngesamt=4.
Die Referenz und die gekoppelte Operation sind ausdrücklich neue Ressourcen.
Dieser gemeinsame Prozess implementiert keinen kostenlosen kohärenten
Bosonpaarantrieb auf dem isolierten System.

## 1. Was die tatsächlichen Quellen konstruieren

Alle zwölf verwendeten Eingaben sind unter `inputs/` unverändert eingefroren;
`inputs_manifest.json` enthält ihre ursprünglichen Pfade, Größen und SHA-256.
Das maßgebliche Tensorarchiv besitzt weiter den SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

| Quellstelle | Tatsächlich konstruierter Gegenstand | Grenze dieses Anschlusses |
|---|---|---|
| `universalraum-singlet-observable-20260915/sources/native_source.py`, Zeilen 36-67 | Fünf Jordan-Wigner-Hilfsoperatoren, deren 16-dimensionaler gerader Spinorraum, zehn BETA-Matrizen und der Farbkeil ergeben W | Die Hilfs-CAR auf fünf Bits sind keine Ausführung der 64 physischen Fermionoperatoren |
| Dieselbe Datei, Zeilen 87-99 | BAR und ETA aus entgegengesetztem Vektorgewicht und komplementärem Farbpaar | Eine invariante Koeffizientenmatrix ist noch kein Bosonpaarinstrument |
| Dieselbe Datei, Zeilen 101-129 | J und C3 mit JC3=0 sowie JJ†=15I | Ein weiterer E8-Koeffiziententensor ist keine vollständige E8-Operatordarstellung auf dem Fockraum |
| `seam_state_derivation_probe.py`, Helfer ab Zeile 380 und Hauptkonstruktion 486-627 | Markierte endliche Clockpermutation aus der ursprünglichen Duad-/Aut-Konstruktion | Keine Auswahl einer physikalischen Zeiteinheit oder des Hamiltonoperators |
| `native-operations-ground-response-20260915/common.py`, Zeilen 104-170 und 187-219 | 60 innere Lie-Matrizen, ihr Bosonlift und der Clocklift | Die konkreten Lifts erhalten Fermion- und Bosonzahl jeweils; aktive unabhängige Kontrolle bleibt eine weitere Voraussetzung |
| `operations_commutant.py`, Zeilen 6-18 | Ausdrücklich unterschiedene Kontrollstufen: fixes Modell, X/Nb, Clock, Gruppenmatrizen | Die Stufen klassifizieren gewährte Operatoren, nicht deren Compilerverfügbarkeit |
| `compiler-origin-audit-20260913/context_instrument.py`, Zeilen 1-6 und 109 ff. | Instrumente auf dem ursprünglichen vierdimensionalen Kontextträger unter Born-/Wiederholbarkeitsannahmen | Kein gegebener Adapter zu B+, R+ oder der 64f/60b-Bank |
| `compiler-kernel-foundation-20260914/relational_kernel.py`, Zeilen 99-121 | Konkrete geordnete Reflexionswörter und ihr interner Phasenzeuge | Ihre vorhandene C4-Wirkung liefert nicht automatisch einen ladungsändernden Fockgriff |

Die letzten beiden Quellen werden hier zur Typ- und Verfügbarkeitsprüfung
gelesen, nicht erneut als Gesamtprogramme ausgeführt. Die Quellenprüfung ist
auf diese konkret bezeichnete Kette begrenzt; sie ist keine Behauptung, dass
jedes denkbare andere Compilerabbild oder jede Datei des Repositories
ausgeschlossen wurde. Die verfügbaren MCP-Codegraphtools enthielten keine
aufrufbaren Graphsuchfunktionen; deshalb wurde gezielt lokal gelesen.

Der eigene Replay führt die tatsächliche `native_source.py` bis einschließlich
Zeile 220 mit allen 17 dortigen Guards aus. Nur die nachfolgende optionale
Hashbildung des dichten C3-Arrays und der Druckblock entfallen. Der erhaltene
W-Tensor stimmt in jedem Eintrag mit dem gepinnten Archiv überein. Der
ursprüngliche Clockkern wird einschließlich seiner vier mathematischen
S0.1-S0.4-Guards wiederholt; die übrigen numerischen Seam-Proben laufen nicht.
Das ergibt erneut p=(2,0,1,4,3) und den dokumentierten passiven Focklift.

## 2. Geschlossener Erhaltungssatz für das dokumentierte Alphabet

Es gilt auf dem endlichen Besetzungszustandskern

\[
N=N_f+2N_b,\quad
[N,f_i]=-f_i,\quad [N,b_A]=-2b_A.
\]

Mit den unveränderten Definitionen

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad
T_+=\sum_A b_A^\dagger P_A,\quad T_-=T_+^\dagger,
\quad X=T_++T_-
\]

hat jedes der 480 signierten Wechselwirkungsmonome Ladung +2−1−1=0.
Nb, alle Modenbesetzungen und alle passiven Bilineare f†Af beziehungsweise
b†Cb sind ebenfalls neutral. Die dokumentierten inneren Liegeneratoren
werden genau auf diese Weise zweitquantisiert. Die Clock schickt
f† nach GF f† und b† nach GB b†, mischt also keine Erzeuger mit Vernichtern.

Sei A0 die von diesen gewährten Operationen erzeugte *-Algebra. Aus

\[
[N,AB]=[N,A]B+A[N,B]
\]

folgt induktiv

\[
\boxed{\mathcal A_0\subseteq\{N\}'.}
\]

Der Beweis umfasst Produkte, Summen, Adjungierte und Kommutatoren jeder
endlichen Länge. Auf jedem festen N-Sektor sind die betreffenden nativen
Hamiltonoperatoren endlichdimensional; ihre exponentiellen Entwicklungen
und endliche Pulsfolgen erhalten daher ebenfalls diesen Sektor. Es ist
keine numerische Suche nur bis zu einer endlichen Wortlänge.

Für die in v1.6.7 geprüften Kandidaten gilt hingegen

\[
[N,B_+]=4B_+,\qquad [N,R_+]=4R_+.
\]

Ihre Nichtnullwirkung ist direkt sichtbar:

\[
\|B_+|0\rangle\|^2=30,\qquad
\|R_+|0\rangle\|^2=480.
\]

Also gehören B+, R+ und ihre nichttrivialen hermiteschen Quadraturen nicht
zu A0. Ein fixes H bietet nicht mehr Erreichbarkeit als das großzügigere
Alphabet mit X und Nb als unabhängigen Kontrollen. Selbst alle gewährten
inneren Gruppenoperationen beseitigen dieses N-Hindernis nicht.

### Instrumente und die genaue Ancilla-Grenze

Ein Instrument mit Krausoperatoren Kx aus A0 kann aus einem scharfen
N-Sektor keinen anderen erzeugen. Eine spurtreue Summe solcher Zweige erhält
die gesamte Sektorverteilung. Selektive Konditionierung kann die Gewichte
einer bereits vorhandenen Mischung verändern, aber keine neue Sektorstütze
erzeugen.

Dasselbe gilt für einen zusätzlichen Zeiger, dessen Ladungsoperator auf
seinem ganzen Hilbertraum null ist, sofern auch die gemeinsame Kopplung
N erhält. Es gilt ausdrücklich **nicht** für eine beliebige mitgeführte
Ladungsreferenz. Bei deren Ladungswechsel kann die Systemladung wechseln,
während die Gesamtladung unverändert bleibt. Abschnitt 5 gibt dafür einen
expliziten positiven Zeugen. Ein Zeiger, der anfangs Ladung null hat, aber
andere Ladungszustände besitzt, ist nicht mit einem auf dem ganzen Raum
ladungstrivialen Zeiger gleichzusetzen.

## 3. Die kleinste zusätzliche Operation ist schon algebraisch ausreichend

In der ursprünglichen Basis ist

\[
B_+=\frac12 b^\dagger\eta b^\dagger
=\sum_{A<\bar A}\eta_A b_A^\dagger b_{\bar A}^\dagger,
\qquad Q=B_++B_-.
\]

Dabei ist der zweite Bosonindex BAR(A). Es gibt dreißig solche ungeordneten Paare.
Die vollständige Invarianz von η wird an allen 45+15 ursprünglichen
Liegeneratoren geprüft. Die 60 verschiedenen Bosongewichte und der
zusammenhängende Lie-Wirkungsgraph beweisen zusätzlich, dass diese
Paarung bis auf einen Skalar eindeutig ist.

Unter den G-invarianten, fermionparitätsgeraden, normalgeordneten
Polynomen ist Grad zwei der kleinste mögliche Grad einer N-ändernden
Operation: Es gibt kein lineares Bosonsingulett; fermionische Paarterme
haben nichttriviale SU(4)-Zentrumsladung; die verbleibenden Bilineare f†f
und b†b erhalten N. Die minimale Klasse ist daher
κB+ + κ̄B−. Eine Phase, Stärke oder Ausführungszeit wird dadurch nicht gewählt.

Die exakten CCR liefern am gesamten 60-Kanal-Tensor

\[
[T_-,B_+]=R_+,\qquad
[Q,X]=R_--R_+,\qquad
\boxed{R_++R_-=-[N_b,[Q,X]].}
\]

Der ursprünglich zusätzlich vorgeschlagene kubische Quartettkanal braucht
somit keinen zweiten unabhängigen Koeffiziententensor. Ein einziger
zusätzlich gewährter Bosonpaargriff Q reicht algebraisch, sobald X und Nb
separat zugänglich sind. Der Nachweis benutzt exakte Normalordnung auf dem
unendlichen Boson-Fockraum, keine abgeschnittenen Oszillator-CCR.

Das ist eine konkrete minimale **Erweiterung** des Operationsvertrags.
Die Quelle liefert η und W; sie liefert in der geprüften Kette keine
Ausführung von Q. Aus der Kommutatoridentität allein folgt außerdem kein
endliches exaktes Pulswort für exp(−itR). Eine Interpretation als
Kontrollsynthese benötigt schaltbare Vorzeichen/Zeiten und eine bewiesene
Konvergenz samt Fehlerkontrolle. Bereits der statische Zusatz κQ bricht N;
die separate X/Nb-Verfügbarkeit ist nur für die genannte Synthese nötig.

## 4. Ein neuer kleiner ursprünglicher Singulettmechanismus

Definiere am wirklichen Vakuum der 64f/60b-Bank

\[
|\beta\rangle=\frac{B_+|0\rangle}{\sqrt{30}},\qquad
|\rho\rangle=\frac{R_+|0\rangle}{\sqrt{480}}.
\]

Beide Zustände sind volle G-Singuletts und haben N=4. β enthält zwei
Bosonen; ρ enthält einen Boson und zwei Fermionen. Ihre Orthogonalität
folgt schon aus den unterschiedlichen Besetzungszahlen.

Der Schließungsschritt beruht auf der tatsächlichen Fierz-Identität

\[
\sum_{AB}\eta_{AB}P_A^\dagger P_B^\dagger=0.
\]

Der Prüfer enumeriert hierfür **3840 signierte Quellterme auf 960
Fermionquartetts**. Nach vollständiger CAR-Normalordnung bleibt kein
einziger Koeffizient übrig. Zusätzlich wird die gesamte ursprüngliche
Wechselwirkung direkt auf alle 30 Komponenten von B+|0⟩ und alle 480
Komponenten von R+|0⟩ angewendet. Das ergibt genau

\[
\begin{aligned}
T_+B_+|0\rangle&=0,&T_-B_+|0\rangle&=R_+|0\rangle,\\
T_+R_+|0\rangle&=16B_+|0\rangle,&T_-R_+|0\rangle&=0.
\end{aligned}
\]

Es gibt keine ausgelassenen Übergänge. Nach Normierung beträgt die
Kopplung in beiden Richtungen 4g. Deshalb ist span{β,ρ} unter dem ganzen
Hnat invariant und besitzt die eingangs angegebene Zweizustandsmatrix.
Eine Behauptung über die Dimension des gesamten N=4-Singulettsektors ist
für diesen Schluss nicht erforderlich und wird hier nicht erhoben.

Für einen anfangs verfügbaren β-Zustand lautet die Umwandlung

\[
P_{\beta\to\rho}(t)=
\frac{64g^2}{\Delta^2+64g^2}
\sin^2\!\left(\frac{t}{2}\sqrt{\Delta^2+64g^2}\right).
\]

Am ursprünglichen Prüfpunkt g/Δ=1/20 ist ihr Maximum exakt **4/29**.
Das ist Veränderung der Zusammensetzung in einer Bank; die Rechnung
führt keine Orte ein. Dieser N=4-Startzustand ist auch nicht der frühere
N=64-Grundzustand Ω.

Zum Vergleich bleibt der elementare N=2-Kanal
W†|A⟩/√8 ↔ |bA⟩ mit Matrix [[0,√8g],[√8g,Δ]] erhalten. Sein Maximum
beträgt am selben Prüfpunkt 2/27; ein einzelnes ursprüngliches Paar besitzt
nur 1/8 des hellen Gewichts und erreicht 1/108. Auch hier sind Vorbereitung,
Auslesung und Zeitkalibrierung zusätzliche Teile eines ausgeführten
Prozessvertrags.

## 5. Exakter gemeinsamer Dreizustandsprozess mit voller innerer Symmetrie

Man gewähre eine Referenz R mit zwei **G-trivialen** Zuständen |0⟩R und
|4⟩R, deren N_R-Ladungen null beziehungsweise vier sind. Setze

\[
L_-=|0\rangle_R\langle4|,\qquad
V=\kappa(B_+\otimes L_-+B_-\otimes L_-^\dagger),
\]

\[
H_{\rm joint}=H_{\rm nat}\otimes I+
E_R I\otimes|4\rangle_R\langle4|+V.
\]

Für reelle g, κ und ER ist Hjoint auf jedem festen Gesamt-N-Sektor eine
endliche hermitesche Matrix. V erhält Ngesamt und die **ganze** innere
Gruppe: B± sind bereits G-Skalare, die Referenz ist G-trivial. Anders als
ein ausschließlich auf Cartanladungen beruhender Ansatz ist hier kein
ungeprüfter Rest der nichtabelschen Gruppe übrig.

Der gemeinsame Raum

\[
\mathcal K=\operatorname{span}\{
|0\rangle_S|4\rangle_R,
|\beta\rangle_S|0\rangle_R,
|\rho\rangle_S|0\rangle_R\}
\]

hat durchgehend Ngesamt=4 und ist unter Hjoint invariant. Denn B−β=√30|0⟩,
B−ρ=0, L−|0⟩R=0 und die nativen Übergänge sind vollständig in Abschnitt 4
bewiesen. In dieser orthonormalen Basis lautet der **exakte ganze Block**

\[
\boxed{
H_{\rm joint}|_{\mathcal K}=
\begin{pmatrix}
E_R&\sqrt{30}\kappa&0\\
\sqrt{30}\kappa&2\Delta&4g\\
0&4g&\Delta
\end{pmatrix}.}
\]

Die zweite Kopplung ist unverändert aus Hnat abgeleitet. Die erste stammt
aus dem ausdrücklich neuen gemeinsamen Instrument V. Für den Start
|0⟩S|4⟩R ist die Quartettwahrscheinlichkeit bei kleinen Zeiten

\[
P_{\rho,0_R}(t)=120\kappa^2g^2t^4+O(t^6).
\]

Das positive führende Glied ist exakt aus (Hjoint²)31 berechnet; die
Geradheit folgt bei reellen Parametern aus der reellen symmetrischen Matrix.
Es wird weder eine besondere Auswahl der Energie ER noch ein universeller
hoher Übertragungsgrad behauptet.

### Die Referenz verschwindet nicht aus der Rechnung

Ein allgemeiner gemeinsamer Zustand in K hat die Form

\[
a|0,4_R\rangle+b|\beta,0_R\rangle+c|\rho,0_R\rangle.
\]

Nach Ausspuren der Referenz bleibt

\[
\rho_S=|a|^2|0\rangle\langle0|+
(b|\beta\rangle+c|\rho\rangle)
(\bar b\langle\beta|+\bar c\langle\rho|).
\]

Die N=0/N=4-Kohärenzen sind null; die β/ρ-Kohärenz innerhalb N=4 bleibt.
Ein erfolgreicher Ladungseintrag hinterlässt die Referenz bei null statt
vier. Der Prozess implementiert deshalb keinen unveränderten katalytischen
Q-Antrieb des isolierten Systems. Eine zusätzliche kohärente Referenz kann
einen effektiven Antrieb in erster Ordnung liefern; eine beliebige endliche
Referenz ist aber nicht automatisch ein exakter wiederverwendbarer Antrieb.
Ein ergänzender exakter Vierzustandszeuge zeigt beides: Eine scharfe
Ladungsreferenz erzeugt eine inkohärente Populationsänderung; für die
gleichgewichtete kohärente Referenz hat die reduzierte Systemdichte nach
dem gewählten Puls Determinante 1/16 und ist somit gemischt.

### Anschluss an das nachgereichte Forschungspaper

Abschnitt 9 des nachgereichten Papers benutzt dasselbe Prinzip einer
mitgerechneten Ladungsreferenz. Sein dortiger N=9-Vierzustandstransfer
erhält mit der neuen Referenz **eine einzelne innere Cartanladung**.
Unsere Konstruktion betrifft stattdessen N und erhält die vollständige
innere Gruppe, erzeugt aber keine räumliche Übertragung. Sie ersetzt den
dortigen Transferzeugen nicht und beweist dessen native Herkunft nicht.
Das Paper benennt seine Ein-Cartan-Grenze und den Referenzverbrauch selbst
ausdrücklich. Hier wurde nur dieser begrenzte Anschluss gelesen; sein
Gesamtaudit liegt außerhalb dieses Strangs.

## 6. Ressourcenbilanz und der jetzt konkrete nächste Nachweis

| Ressource | Herkunft im geprüften Vertrag | Was noch zu liefern wäre |
|---|---|---|
| W, η, innere Darstellung, endliche Clock | Tatsächliche Quellkonstruktion und erneuter exakter Replay | Physische Identifikation des Trägers |
| Hnat mit Δ,g | Bestehender ausdrücklich festgelegter Modellvertrag | Physische Auswahl und Kalibrierung |
| Zweizustandsblock β↔ρ | Neue vollständige Anwendung aller nativen Terme | Ursprüngliche Vorbereitung von β oder ρ |
| Unabhängige X/Nb-Kontrollen | Gewährte Kontrollstufe, nicht aus fixes H abgeleitet | Instrumente und Schaltvertrag |
| Q oder der gemeinsame Übergang V | Hier genau ausgeschriebene zusätzliche Operation | Compilerwort oder Instrument, das diesen Übergang wirklich erzeugt |
| G-triviale Referenz mit N_R=0,4 | Minimaler zusätzlicher Ladungsspeicher für diese Konstruktion | Träger, Präparation, Energie ER und alle Ressourcenkosten |
| Anfang | Vakuum × scharfe Referenzladung vier | Herkunft dieses Gesamtzustands |
| Ausgang | Gemeinsame Besetzungen und Referenzwechsel | Ausführbare gemeinsame Auslesung, ohne stilles Ausspuren relevanter Information |

Die Minimalität ist präzise begrenzt: Grad zwei ist der kleinste zugelassene
G-invariante paritätsgerade N-ändernde Systemgrad; zwei verschiedene
Referenzladungen sind die kleinste Dimension für den einmaligen scharfen
Ausgleich; die Dreizustandsmatrix ist der kleinste von diesem konkreten
Anfang durch die beiden nichtverschwindenden Kopplungen erzeugte Raum.
Das ist keine globale Minimierung aller möglichen Universen oder Compiler.

**Nächster Herkunftsnachweis:** Ein vorhandener ursprünglicher Quellbaustein
muss einen getypten Adapter zu V einschließlich Referenzzustand und
gemeinsamer Auslesung liefern. Ein Vorschlag allein aus den bereits
N-neutralen Fockwörtern scheitert jetzt am bewiesenen Erhaltungssatz und
braucht keine weitere Wortsuche. Ein anderer getypter Quellbaustein bleibt
eine offene Möglichkeit; bloße E8-Grade oder gleiche Matrizenabmessungen
reichen als Adapter nicht aus.

## 7. Reproduktion und Beweisumfang

Aus diesem Ordner:

```sh
python3 -B -W error verify.py --output results_normal.json
python3 -OO -B -W error verify.py --output results_optimized.json
cmp results_normal.json results_optimized.json
```

Benötigt werden Python, NumPy, SciPy und SymPy. Der Replay liest nur die
eingefrorenen Eingaben und braucht weder das ursprüngliche Repository noch
Netzwerkzugriff. `freeze.py` ist nur das Herkunftswerkzeug für die erste
Archivierung und gehört nicht zum wissenschaftlichen Replay.

Es gibt **261 explizite exakte Prüfbedingungen pro Modus**, zusätzlich zu
den separat ausgewiesenen 17 erhaltenen nativen Konstruktorguards. Die vier
Clockguards sind in den 261 enthalten. Normaler und `-OO`-Lauf erzeugen
byteidentische JSON-Dateien. Die Bosonidentitäten nutzen die exakte Weyl-
Normalordnung; die nativen Zustandsaktionen nutzen alle CAR-Vorzeichen
und Bosonmultiplikitäten. Keine Prüfung benutzt ein wegoptimierbares
`assert`, und Warnungen werden als Fehler behandelt.

Die Bedingungen prüfen konkrete algebraische Tatsachen und Quellenpins;
die allgemeinen Induktions- und Verfügbarkeitsargumente stehen oben.
Die Zahl 261 ist keine Zahl unabhängiger Theoreme oder physischer
Realisierungen. Kein neuer Grundzustandssatz für die Erweiterung, keine
native Raumzeit, keine vollständige E8-Operatordarstellung und kein T1-T8-
Abschluss wird behauptet. Fremde Quellen, v1.6.7, zentrale Ledger und
Webseiten wurden nicht verändert.


---

# Teilbericht B: vollständige innere Schattenkarte

# Gemeinsame Schattenkarte auf dem ursprünglichen W

Stand: 15. September 2026. Eigenständiger Folgeschritt zu v1.6.7.

## Ergebnis

Der ursprüngliche Tensor liefert jetzt eine vollständig berechnete gemeinsame
Schattenkarte für den inneren hellen N=2-Code. Einzelne Besetzungen unterscheiden
nur 24, sämtliche Einteilchenoperatoren nur 736 von insgesamt 3600 hermiteschen
Operatorrichtungen. Paarbesetzungen zusammen mit ausführbaren Drehungen aus
G=Spin(10)×SU(4) liefern dagegen eine vollständige Zustandsrekonstruktion.
Eine konkrete endliche Familie mit 3599 nichtkonstanten Erwartungswerten liegt
bei. Diese letzte Aussage ist **bedingt auf die Ausführbarkeit der zusätzlichen
Kontrollen und Messungen**. Aus ihrer algebraischen Existenz folgt noch kein
ursprüngliches Messinstrument samt Zustandsänderung.

Das Ergebnis betrifft denselben ursprünglichen W, keine ersatzweise eingeführte
Qubit-Analogie. Der W-Dateipin ist
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.
Die vier gelesenen v1.6.7-Kontextdateien sind ebenfalls unverändert eingefroren.

## 1. Ein gemeinsamer Träger, mehrere Schatten

Mit V=W†/√8 gilt V†V=I auf C^60. Für eine logische Dichtematrix ρ lautet der
Schatten eines Fermionoperators O

\[
  \Phi_{\mathcal O}(\rho)_O=\operatorname{tr}(\rho V^\dagger O V).
\]

Alle folgenden Messfamilien beziehen sich auf genau dieselbe ρ und denselben
Kodierer. Die Dimension der reellen Menge hermitescher 60×60-Matrizen ist 3600;
bekannte Spur eins reduziert die freien Zustandsparameter auf 3599.
Alle angegebenen Familien enthalten die Identität in ihrem linearen Raum,
sodass ihre unsichtbaren Kerne bereits spurfrei sind.

| Messfamilie | Exakter Operatorrang | Unsichtbare Zustandsdifferenzen | Verfügbarkeit |
|---|---:|---:|---|
| Alle 64 Einzelbesetzungen n_r | 24 | 3576 | Konkrete Operatoren; ursprüngliche Messausführung offen |
| Alle hermiteschen Einteilchenbilineare f_r†f_s | 736 | 2864 | Zusätzliche vollständige Bilinearfamilie |
| Alle G-gedrehten Einzelbesetzungen | 736 | 2864 | Bedingt auf ausführbare G-Kontrollen |
| Alle 2016 ungedrehten Paarbesetzungen n_i n_j | 60 | 3540 | Gemeinsame Besetzungsmessung erforderlich |
| Bilineare plus ungedrehte Paarbesetzungen | 772 | 2828 | Beide vorigen Ressourcen zusammen |
| G-gedrehte Paarbesetzungen | 3600 | 0 | Gemeinsame Messung und ausführbare G-Kontrollen |

Der Rang zählt unabhängige lineare Erwartungswerte. Er zählt weder
Messapparaturen noch Messwiederholungen noch physische Raumrichtungen.

## 2. Exakter Rangbeweis am Tensor

Die Datei enthält zehn symmetrische 16×16-Matrizen β_k. Mit den sechs
antisymmetrischen 4×4-Farbmatrizen ε_c gilt eintragsweise

\[
 W_{(k,c),(p,a)(q,b)}=(\beta_k)_{pq}(\epsilon_c)_{ab}
 \quad\text{für }(p,a)<(q,b).
\]

Der Prüfer rekonstruiert hieraus den gesamten W und vergleicht alle Einträge.
Für sämtliche 4096 Bilineare vergleicht er zudem die direkte CAR-Kontraktion
mit der Faktorformel

\[
 8V^\dagger f_{p,a}^\dagger f_{q,b}V
   =F_{pq}\otimes C_{ab},\qquad
 (F_{pq})_{kl}=\sum_t(\beta_k)_{pt}(\beta_l)_{qt},\quad
 (C_{ab})_{cd}=\sum_t(\epsilon_c)_{at}(\epsilon_d)_{bt}.
\]

In den aus den W-Faktoren abgeleiteten orthogonalen reellen Rahmen ist der
Spin-Bildraum genau `Skalar ⊕ i·antisymmetrisch`, Dimension 1+45=46;
der Farbbildraum hat Dimension 1+15=16. In der ursprünglichen Gewichtsbasis
prüft der Code die äquivalente ganzzahlige Identität

\[
 n(A+\eta A^T\eta)=2\operatorname{tr}(A)I_n.
\]

Sie liefert jeweils die obere Ranggrenze. Ein nichtverschwindender modularer
Minor über dem Primkörper mit 1009 Elementen liefert die passende untere Grenze.
Damit sind die Ränge über Q und C exakt bewiesen; es handelt sich nicht um
eine toleranzabhängige numerische Rangschätzung. Produktbildung ergibt 736.

Für die diagonalen Einzelbesetzungen bleiben nur Skalar plus Cartan:
(1+5)(1+3)=24. Die Adjungierten von so(10) und so(6) sind irreduzibel;
jede ursprüngliche Einzelbesetzung hat einen nichtverschwindenden Skalar-
und Cartananteil in beiden Faktoren. Ihr G-Orbit erzeugt deshalb alle vier
Summanden von (1⊕45)⊗(1⊕15), insgesamt 736, und keine weiteren.

Der Eingabekern der gesamten Einteilchenkompression hat Dimension
4096−736=3360=(256−46)·16. Er ist vom unsichtbaren *Zustandskern* mit
Dimension 3600−736=2864 zu unterscheiden.

### Was genau fehlt?

Die gesamte Hermitesche Algebra zerfällt in den beiden reellen Faktoren als

\[
 (1\oplus i\Lambda^2\mathbb R^{10}\oplus\operatorname{Sym}^2_0\mathbb R^{10})
 \otimes
 (1\oplus i\Lambda^2\mathbb R^6\oplus\operatorname{Sym}^2_0\mathbb R^6).
\]

Die letzten symmetrischen, spurlosen Komponenten haben Dimension 54 und 20.
Dem Bilinearschatten fehlen exakt die drei disjunkten Räume

\[
 54\otimes(1\oplus15),\quad (1\oplus45)\otimes20,
 \quad54\otimes20,
\]

mit Dimension 864+920+1080=2864. Das ist eine konkrete Beschreibung des
vollständigen unsichtbaren Kerns, nicht bloß eine Dimensionsdifferenz.

Ein Verzicht auf alle imaginären Phasen wäre nochmals stärker: In demselben
reellen Gesamtrahmen haben reelle symmetrische Operatoren Dimension
55·21+45·15=1830; imaginäre antisymmetrische Operatoren haben Dimension
55·15+45·21=1770. Ein ausschließlich reeller Schatten könnte diese 1770
Richtungen nicht sehen. Die native G-Familie enthält die nötigen
phasenempfindlichen Richtungen; ihre Ausführbarkeit wird damit nicht bewiesen.

## 3. Zwei orthogonale Zustände mit identischen eingeschränkten Schatten

In der ursprünglichen logischen Gewichtsbasis, nullbasiert mit A=6k+c, setze

\[
 |\psi_\pm\rangle=\frac{|0\rangle\pm|30\rangle}{\sqrt2},
 \qquad \rho_\pm=|\psi_\pm\rangle\langle\psi_\pm|.
\]

Beide Matrizen sind exakt positiv, rein und zueinander orthogonal. Es gilt
für alle r,s und für alle i<j

\[
 \operatorname{tr}[(\rho_+-\rho_-)V^\dagger f_r^\dagger f_sV]=0,
 \qquad
 \operatorname{tr}[(\rho_+-\rho_-)V^\dagger n_in_jV]=0.
\]

Insbesondere ändern beliebig viele G-gedrehte Einteilchenmessungen daran
nichts. Die Zustände unterscheiden sich in einer fehlenden Spin-54-Richtung.

Der normierte logische Vektor

\[
 |z\rangle=\tfrac12(|0\rangle+|30\rangle+i|6\rangle+i|36\rangle)
\]

liegt hingegen im G-Orbit eines ursprünglichen Kanalvektors. Die zugehörige
gedrehte Paarbesetzung komprimiert zu |z⟩⟨z|/8 und liefert die exakt
verschiedenen Erwartungswerte 1/16 und 0. Dies ist ein positiver Zustandszeuge
für die Verbesserung durch die zusätzliche Paarressource.

## 4. Endliche, minimale Familie für vollständige Rekonstruktion

Jede unterstützte Paarspalte des W hat genau einen Eintrag±1. Daher gilt

\[
 V^\dagger n_i n_jV=\tfrac18|A\rangle\langle A|
\]

für den zugehörigen Kanal A. Jeder der 60 Kanäle tritt auf. Ungedrehte
Paarbesetzungen erzeugen also exakt alle Diagonalmatrizen. Ihr Schnitt mit
dem Bilinearraum hat Dimension 24: Diagonalprojektion erhält die oben
angegebenen Faktor-Bildräume und hat in ihnen Rang 6 und 4. Damit folgt der
kombinierte Rang 736+60−24=772.

Der Prüfer leitet die reellen Rahmen aus den invarianten Faktormetriken ab.
Er prüft außerdem das W-Intertwining für sämtliche 45+15 Lie-Generatoren
und ihre vollständigen Bilder so(10), so(6). G wirkt im logischen Raum
folglich als SO(10)×SO(6), jeweils mit seiner Spin/SU(4)-Überlagerung.

Ein ursprünglicher Gewichtskanal ist in jedem Faktor ein zirkularer Vektor
(e_i+i e_j)/√2. Sein SO(n)-Orbit besteht aus (u+i v)/√2 mit reellen,
orthonormalen u,v. Für n=10 und n=6 erzeugt der Prüfer eine rationale Liste
solcher Projektoren:

1. Alle (e_i±i e_j)/√2.
2. Für jedes i<j und ein drittes k den Vektor
   `(3e_i+4e_j+5i e_k)/sqrt(50)`.

Alle 50P haben ganzzahlige reelle und imaginäre Einträge. Der Code prüft
`P²=P`, `tr(P)=1` und die Isotropie `tr(P Pᵀ)=0` exakt nach Skalierung.
Die Isotropie und die Norm kennzeichnen diese SO(n)-Gewichtsorbits; durch
Orientierungswahl auf dem orthogonalen Komplement existiert eine Drehung
mit Determinante+1. Beliebige U(10)- oder U(6)-Kontrollen werden nicht benutzt.

Modulare Zeilenauswahl liefert folgende konkrete unabhängige Basen:

\[
 \mathcal B_{10}=\{I_{10},P_1,\ldots,P_{99}\},\qquad
 \mathcal B_6=\{I_6,Q_1,\ldots,Q_{35}\}.
\]

Die ausgewählten Vektoren und Indizes stehen vollständig im Ergebnis-JSON.
Ihre Produkte bilden eine Basis aller hermiteschen 60×60-Matrizen. Bei
bekannter Spur bleibt eine minimale Familie von 3599 nichtkonstanten Zahlen:

- 99·35=3465 gedrehte Paarprojektoren P_a⊗Q_b;
- 99 Spinwerte P_a⊗I_6, als Summe über die sechs Farbkanäle;
- 35 Farbwerte I_10⊗Q_b, als Summe über die zehn Spinkanäle.

Alle physisch angesetzten Paarerwartungswerte besitzen denselben Faktor 1/8;
die Rekonstruktion kalibriert ihn ausdrücklich zurück. Da ein offener
Bereich um I/60 alle 3599 spurlosen hermiteschen Richtungen enthält, kann
keine feste Familie linearer Skalarerwartungswerte mit weniger als 3599
Zahlen jeden Zustand identifizieren. **Minimalität bezieht sich genau auf
diese Zahlenzahl**, nicht auf Geräteeinstellungen oder Messkosten.

### Unabhängige Rekonstruktionsprüfung

Die Familie wird ohne Zustandsdaten festgelegt. Anschließend werden die
beiden obigen reinen Zustände sowie sechs deterministisch zufällige Zustände
der Ränge 1, 2, 5, 17, 60, 60 in derselben ursprünglichen W-Codebasis verwendet.
Aus ihren 3599 kalibrierten Schatten rekonstruiert der Prüfer die vollständigen
Dichtematrizen. Zusätzlich sagt er je zwölf vorher unbenutzte, G-gedrehte
Paarerwartungswerte dieser selben Zustände voraus.

Diese Tests sind **numerisch**, nicht als exakte Zustandsbeweise ausgegeben.
Im dokumentierten Lauf beträgt der größte Matrixeintragsfehler unter
7.6×10⁻¹⁶; der größte Fehler der 96 unbenutzten Paarvorhersagen liegt unter
5.8×10⁻¹⁷. Die Antwortmatrizen der Faktoren haben Konditionszahlen ungefähr
40.47 und 20.72. Das ist ein rauschfreier Rekonstruktionstest; statistische
Messkosten, Zustandspräparation und Robustheit gegen reales Rauschen sind
hier nicht nachgewiesen.

## 5. Was native Zeitentwicklung hinzufügt

Der gemeinsame helle N=2-Prozess besitzt H=h⊗I_60. Für jeden Zweigoperator B
und inneren Operator O gilt exakt

\[
 [h\otimes I,B\otimes O]=[h,B]\otimes O.
\]

Beliebige Zeitableitungen und Zeiten verändern daher nur den Zweigfaktor.
Sie erweitern den inneren Schattenrang 24 beziehungsweise 736 nicht.
Die zusätzlichen Paarsonden können den inneren Rang dagegen bis 3600 erhöhen.
Zweigkohärenz und ihre Rekonstruktion erfordern eine gesonderte
Prozessbetrachtung; eine innere Zustandsrekonstruktion allein bestimmt noch
keine vollständige Mehrzeitgeschichte oder ein Messinstrument.

## Reproduktion und Grenze

Mit Python 3.10 oder neuer und NumPy, aus diesem Ordner:

```sh
python3 -B replay.py
```

Der Lauf überprüft die fünf eingefrorenen Quellenpins, führt den eigenen
Prüfer normal und mit `-OO` aus und verlangt byte-identische Ausgaben.
Warnungen gelten als Fehler; keine Prüfbedingung benutzt abschaltbare
Python-Assertions. Die Prüfzahlen stehen im Replay-Manifest.
Die vier Kontextdateien werden gehasht, nicht als fremde Gesamtsuite erneut
ausgeführt. Die mathematische Prüfung benutzt nur die lokale W-Archivdatei.

Damit ist eine gemeinsame, am Ursprungstensor kalibrierte *innere*
Schattenkarte konstruiert. Ein räumlicher Rand, ursprüngliche ausführbare
Instrumente, eine universelle Prozessidentifikation, 3+1D-Raumzeit oder ein
Abschluss von T1-T8 folgt daraus nicht.


---

# Teilbericht C: kausaler Eingriff

# Exakter kausaler Eingriff am unveränderten nativen Hamiltonoperator

## Ergebnis

Im ursprünglichen TFPT-Modell gibt es einen vollständig gelösten kausalen
Test innerhalb des Ladungssektors N=2. Ein Phasenimpuls an Fermionmode 4
ändert die spätere unbedingte Besetzung von Mode 5. Die beiden Observablen
kommutieren vor der Entwicklung. Der Impuls erhält die Ladung und wirkt nur
auf Mode 4; es gibt keine Konditionierung auf Messergebnisse.

Der stärkste hier bewiesene Vergleich endet in **beiden** Armen mit genau
zwei Fermionen und keinem Boson. Gemessen wird eine andere Verteilung der
Fermionen auf disjunkte Paare. Die natürliche Entwicklung zwischen Eingriff
und Messung verwendet ausschließlich das ursprüngliche H und W.

**Bedingung:** Die Präparation des angegebenen Produktzustands, ein gezielter
Phasenimpuls und die einzelne Besetzungsmessung werden als Instrumente
gewährt. Ihre physische Verfügbarkeit aus dem ursprünglichen Operationssatz
ist hier nicht hergeleitet. Der Impuls ist eine ausdrücklich hinzugewährte
Kontrolloperation; er wird nicht als von der ungestörten H-Entwicklung
bereitgestellt ausgegeben. Es wurde kein zusätzlicher Hopping- oder
Linkterm in die freie Dynamik eingeführt.

Das Ergebnis betrifft Moden innerhalb derselben Bank. Es enthält weder eine
räumliche Metrik noch den bereits untersuchten N=64-Grundzustand oder dessen
geladenen Entnahmepol.

## 1. Quelle und vollständiger invarianter Sektor

Die eingefrorene Quelle ist `sources/spinor_tensors.npz` mit SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Es gilt unverändert

\[
H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad N=N_f+2N_b.
\]

W besitzt 60 Zeilen, 2016 Spalten und 480 Einträge mit Wert ±1.
Jede aktive Spalte gehört genau einer Zeile. Jede Zeile enthält acht
Fermionenpaare mit insgesamt sechzehn verschiedenen Moden. Deshalb zerfällt
der **gesamte** N=2-Sektor in 60 invariante neundimensionale Blöcke und
1536 vollständig dunkle Paarzustände. Die sieben dunklen Richtungen innerhalb
jedes Blocks kommen zusätzlich hinzu: insgesamt bleibt die bekannte dunkle
Dimension 1536+60·7=1956.

Eine solche Gruppe besteht aus einem Boson und acht Paaren. Mit
\(|p_\ell\rangle=f_{i_\ell}^\dagger f_{j_\ell}^\dagger|0\rangle\),
\(s_\ell=W_{A,i_\ell j_\ell}\) und
\(|S\rangle=\sum_\ell s_\ell|p_\ell\rangle/\sqrt8\) gilt

\[
H_A=\begin{pmatrix}0_{8\times8}&g s\\g s^T&\Delta\end{pmatrix},
\qquad H_A|_{\operatorname{span}(S,b_A)}=
\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}.
\]

Die CAR-Vorzeichen wurden für alle 480 aktiven Paare separat geprüft.
Dies ist eine exakte Einschränkung auf einen invarianten Sektor, keine
Abschneidung höherer Bosonstufen.

Die benutzte Zeile A=0 lautet:

| Blatt | Fermionenpaar | Vorzeichen |
|---:|---|---:|
| 0 | (4,57) | −1 |
| 1 | (5,56) | +1 |
| 2 | (8,53) | +1 |
| 3 | (9,52) | −1 |
| 4 | (16,45) | −1 |
| 5 | (17,44) | +1 |
| 6 | (28,33) | +1 |
| 7 | (29,32) | −1 |

## 2. Lokale Algebra und ehrlicher Interventionstest

Die Senderoperation ist

\[
Z_4=(-1)^{n_4}=I-2n_4,\qquad
\mathcal E_4(\rho)=Z_4\rho Z_4^\dagger.
\]

Sie hat genau einen unitären Krausoperator und ist daher vollständig positiv
und spurerhaltend. Sie ist fermionparitätsgerade und erhält N. Auf der ganzen
Fock-Algebra kommutiert sie mit allen disjunkten Modenoperatoren; insbesondere
\([Z_4,n_5]=0\). Ihre Einschränkung auf den ausgewählten Block wechselt allein
das Vorzeichen des Blattes (4,57). Diese Einschränkung wurde gegen den
wirklichen Operator \((-1)^{n_4}\) auf allen 2076 N=2-Basiszuständen geprüft.

Der Empfänger liest \(B=n_5\) aus. Im gewählten invarianten Block ist dies
der Projektor auf Blatt (5,56). Die Operation enthält keinen Verweis auf
Mode 5. Zu ihrem Zeitpunkt bleibt dessen gesamte Besetzungsstatistik für
jeden Zustand identisch, weil \(Z_4^\dagger n_5 Z_4=n_5\).

Mit \(\rho_T=U_T|p_0\rangle\langle p_0|U_T^\dagger\) ist die gemessene
Differenz genau

\[
\delta_{4\to5}(T)=
\operatorname{tr}\!\left[n_5U_T\mathcal E_4(\rho_T)U_T^\dagger\right]
-\operatorname{tr}\!\left[n_5U_T\rho_TU_T^\dagger\right].
\]

Das ist ein Vergleich von unbedingten Wahrscheinlichkeiten nach einem
kontrollierten lokalen Eingriff. Eine Zweipunktkorrelation wird dafür nicht
als Ersatz benutzt. Die vor dem Impuls erzeugte Kohärenz wird ausdrücklich
durch die native Vorentwicklung präpariert. Ein Phasenimpuls direkt auf
dem anfänglichen Produktzustand hätte nur ein globales Vorzeichen und
überhaupt keinen Effekt; diese Negativkontrolle wird ebenfalls geprüft.

## 3. Exakter Test mit gleicher Endzusammensetzung

Setze für \(\Delta>0\) und reelles \(g\ne0\)

\[
\Omega=\sqrt{\Delta^2/4+8g^2},\quad
T=\frac\pi\Omega,\quad d=\frac\Delta{2\Omega},\quad
z=-e^{-i\pi d},\quad
x=|z-1|^2=4\cos^2\frac{\pi d}{2}.
\]

Nach T wirkt der helle Zweizustandsblock als z mal Identität; die dunklen
Paarzustände bleiben unverändert. Es gibt dann für **jede** anfängliche
Paarkombination keine Bosonamplitude. Auf der Paarseite ist

\[
U_T^{(f)}=I_8+(z-1)|S\rangle\langle S|.
\]

Beide Arme beginnen in demselben vollständig angegebenen Produktzustand
\(|p_0\rangle=f_4^\dagger f_{57}^\dagger|0\rangle\), alle anderen
Moden leer. Sie unterscheiden sich nur durch den mittleren Phasenimpuls:

\[
\begin{array}{lll}
\text{unberührt:}&U_T\;I\;U_T|p_0\rangle,&\text{danach }n_5,\\
\text{Eingriff:}&U_T\;Z_4\;U_T|p_0\rangle,&\text{danach }n_5.
\end{array}
\]

Für jedes andere Blatt q sind die exakten Endamplituden

\[
\langle p_q|U_T^2|p_0\rangle
=s_0s_q\frac{z^2-1}{8},\qquad
\langle p_q|U_TZ_4U_T|p_0\rangle
=s_0s_q\frac{3(z-1)^2}{32}.
\]

Damit lautet insbesondere die unbedingte Empfängerwahrscheinlichkeit

\[
p_{\rm frei}(n_5=1)=\frac{x(4-x)}{64},\qquad
p_{\rm Impuls}(n_5=1)=\frac{9x^2}{1024},
\]

und die kausale Differenz ist

\[
\boxed{\delta_{4\to5}(T)=\frac{x(25x-64)}{1024}}.
\]

Für \(0<g^2\le3\Delta^2/32\) gilt \(1/2\le d<1\), also
\(0<x\le2\) und folglich **strikt \(\delta_{4\to5}<0\)**. Das ist eine
exakte endliche Zeit, kein unkontrollierter Schluss aus einer numerisch
kleinen Antwort oder einer asymptotischen Reihe. Außerhalb dieses Intervalls
gilt weiterhin die exakte Formel, kann aber auch das Vorzeichen wechseln
oder an x=64/25 verschwinden.

Am bisherigen Prüfpunkt \(\Delta=1,g=1/20\) ist
\(d=5/(3\sqrt3)\) und \(T\approx6.0459978807807\):

| Größe | Wert |
|---|---:|
| Ohne mittleren Impuls | 0.00087491599417248 |
| Mit mittlerem Impuls | 0.0000017344871305812 |
| Differenz | −0.00087318150704190 |
| Endbesetzung in beiden Armen | Nf=2, Nb=0 exakt |

Die Wellenfunktion kann zwischen den Ablesezeiten einen Boson enthalten.
Das natürliche H vermittelt dadurch die Umverteilung von einem
Fermionenpaar in andere. Die Endmessung benötigt keine Selektion auf
„kein Boson“: Dieser Zustand gilt in beiden Armen mit Wahrscheinlichkeit eins.

## 4. Zwei ergänzende Kontrollen

### Boson als einfachere Referenz

Ausgehend vom Produktzustand \(b_0^\dagger|0\rangle\) wähle die beiden
Verzögerungen \(\tau=\pi/(2\Omega)\). Der unberührte Arm kehrt exakt
zum Boson zurück, also \(p_{\rm frei}(n_5=1)=0\). Ein mittleres Z4 erzeugt

\[
p_{\rm Impuls}(n_5=1)
=\frac{(1-d^2)\left[1+d^2-2d\sin(\pi d/2)\right]}{128}
\ge\frac{(1-d^2)(1-d)^2}{128}>0.
\]

Dies gilt für jedes \(g\ne0\) und \(\Delta>0\). Auch dieser Test ist
ladungserhaltend und unbedingt. Er hat allerdings unterschiedliche
Fermion/Boson-Zusammensetzungen am Ende; für die stärkere Aussage über reine
Paarumverteilung wird deshalb der Test aus Abschnitt 3 benutzt.

### Lokales Auffüllen und kurze Zeiten

Auf der Referenz \(f_{57}^\dagger|0\rangle\) füllt das lokale CPTP-Instrument
mit Krausoperatoren \(n_4,f_4^\dagger\) Mode 4. Ohne Eingriff ist der
Einfermionzustand stationär. Mit Eingriff entsteht \(|p_0\rangle\), woraus

\[
\delta n_5(t)=\frac{|a(t)-1|^2}{64},\qquad
a(t)=e^{-i\Delta t/2}\left[\cos\Omega t+i d\sin\Omega t\right].
\]

Die führenden Beiträge sind
\(\delta n_5(t)=g^4t^4/4+O(t^6)\) und
\(\delta N_{b_0}(t)=g^2t^2+O(t^4)\).
Der Pfad in ein anderes Fermionenpaar hat somit zwei native H-Anwendungen
in der Amplitude; die erste Umwandlung zum Boson hat eine.

Dieses Auffüllen tauscht eine Ladungseinheit mit einem angenommenen Reservoir
aus. Es wird nicht als zahlenerhaltende Operation ausgegeben und ist für den
Hauptnachweis nicht erforderlich.

## 5. Prüfung und unveränderte offene Grenze

`verify_causal.py` benutzt explizite Fehlerbedingungen, keine abschaltbaren
Assertions. Normaler Python-Lauf und `python -OO`, jeweils mit Warnungen als
Fehler, erzeugen byte-identische JSON-Ergebnisse. Der optimierte Lauf wurde
aus einem anderen Arbeitsverzeichnis gestartet; die Quelle wird relativ zum
Prüfprogramm aufgelöst. Abhängigkeiten: NumPy, SymPy und SciPy.

Die symbolischen Identitäten und die vollständige W-Struktur werden exakt
geprüft. Zusätzlich läuft ein unabhängiger numerischer Vergleich auf dem
vollen 2076-dimensionalen N=2-Hamiltonoperator, direkt aus W aufgebaut.
Er bestätigt beide vollständigen Endzustände, die Wahrscheinlichkeiten,
Normerhaltung, verschwindende Bosonamplituden und die Negativkontrolle.
Der abschließende Lauf enthält **662 exakte und 10 numerische Prüfbedingungen**.
Prüfzahlen und Quellhash stehen in `result.json`; `result_OO.json` ist dessen
identischer optimierter Replay. Beide Ergebnisdateien haben SHA-256
`b37ae758117e4c35d1063e76756cd6a39f133c964d331a9d400e67a0b157a4a6`.

**Geschlossen:** Im ausdrücklich gewährten Instrumentenvertrag existiert am
selben ursprünglichen H ein kausaler Moden-zu-Moden-Eingriff. Ein weiteres
Hopping-Glied ist für diesen N=2-Zeugen mathematisch nicht notwendig. Reine
Paarumverteilung wird am Endzeitpunkt getrennt von Speziesumwandlung bewiesen.

**Weiter offen:** Auswahl und Präparation dieses N=2-Referenzzustands,
ausführbare einzelne Modenphasen und Besetzungsinstrumente aus dem nativen
Operationssatz; Anschluss an den N=64-Grundzustand und dessen geladenen Pol;
Interpretation der Modenalgebren als räumlich unabhängige Labore; Distanz,
Raumdimension, endliche Ausbreitungsgeschwindigkeit und gemeinsame Raumzeit.
Die bloße Tatsache, dass ein Kontrolloperator zur mathematischen Fock-Algebra
gehört, schließt diese Operationsfrage nicht.


---

# Teilbericht D: derselbe Dreizustandsraum für Schatten und Eingriff

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


---

# Nachtragsprüfung A: neue fünfte Norm und richtige Antwortzustände

# Nachtrag A: Was am neuen v1.6.3-Erklärtext wirklich neu ist

## Urteil

**Ja, ein belastbarer neuer Rechenschritt ist enthalten:** Die zuvor fehlende
Norm ν5 liegt jetzt mit passendem Quellstand vor. Wir haben ν1 bis ν5 frisch
durch die ursprüngliche exakte Spurnetzwerkrechnung reproduziert und daraus
unabhängig strengere rationale Ritzgrenzen gewonnen. Die übrigen großen
Aussagen des Textes sind teils bereits bekannt, teils durch v1.6.7 korrigiert.
Besonders problematisch ist die Vermischung verschiedener Ritz-Zustände
zu einem vermeintlich vollständig bestimmten Grundzustand.

Die gesamte neue Anlage wurde gelesen. Sie stimmt mit der derzeitigen
`EINFACH_ERKLAERT.md` im Ordner
`/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/`
überein. Alle für den neuen Nachweis verwendeten Programme und Ergebnisse
sind separat unter `late_a/inputs/` eingefroren. Die vorhandenen v1.6.7- und
Mechanismus-Snapshots wurden nicht verändert.

## 1. ν5 ist jetzt ein Ergebnis, nicht mehr nur eine Programmeinstellung

Der v1.6.7-Snapshot hatte zu Recht festgehalten, dass damals
`norms_by_traces.json` und ein abgeschlossener zugehöriger Replay fehlten.
Dieser konkrete Quellenstand hat sich geändert. Der neue Checkerhash
`be72c728e128ae0ef605980a5bae88ea31049e29e2fd17c43167fbd6ad1d0c89`
passt jetzt zum Ergebnis; auch der Common-Hash stimmt. Die vorhandenen
normalen und optimierten Normausgaben sind byteidentisch. Der gespeicherte
JSON-Inhalt ist identisch; nur ein abschließender Zeilenumbruch unterscheidet
die Druckausgabe von der geschriebenen Datei.

Zusätzlich zu dieser Quellenprüfung wurde die wirkliche Rechnung in unserem
isolierten Paket normal und mit `-OO` frisch ausgeführt. Geändert wurde nur
der Tensorpfad auf das eingefrorene Originalarchiv; der eigentliche
Spurnetzwerkcode blieb unverändert. Ergebnis:

\[
(\nu_0,\nu_1,\nu_2,\nu_3,\nu_4,\nu_5)=
(1,480,439680,575078400,952296652800,1866738327552000).
\]

Die fünfte Norm benötigt 840 Wick-Netzwerke, die auf 93 Klassen unter
vorzeichenfreien Graphsymmetrien reduziert werden. Jede tatsächlich
ausgewertete Kontraktion benutzt dünnbesetzte Dictionaries und beliebig
große Python-Ganzzahlen. Hier wurde keine Float-Kontraktion oder Rundung
als exakte fünfte Norm ausgegeben.

Die Methode hat einen nachvollziehbaren Ursprung: Für die antisymmetrische
Paarmatrix M(z) liefert die fermionische Exponentialnorm
\(\det(I+M(z)^\dagger M(z))^{1/2}\). Nach Logarithmusentwicklung und
bosonischer Gaußintegration entstehen die im Quellcode benutzten
Spurzyklen, rationalen Faktoren und Wick-Permutationen. Die signierte
Φ-Kontraktion ist deshalb eine Normberechnung desselben Paartensors.

**Reproduktionsgrenze:** Das ist ein frischer Replay der geprüften
ursprünglichen Methode, keine zweite unabhängig neu erfundene Methode für
ν5. Die früheren ν1-ν4-Werte liefern unabhängige bekannte Vergleichspunkte.
Die Quelle vergleicht außerdem 39 kanonische Netzwerke nur bis n=4 mit
ihrem anderen dichten Pfad; daraus folgt kein zweiter n=5-Beweis. Der
Hilfsname `brute_force_nu2` ist irreführend: Sein Aufbau lässt explizite
CAR-Umordnungszeichen aus. Dieser Helfer wurde nicht als tragender
unabhängiger Normnachweis benutzt. Die signierten Spurnetzwerke bleiben
davon getrennt.

Das Gesamt-Replaymanifest der fremden Suite stand beim Einfrieren weiterhin
auf **RUNNING** mit leerer Laufübersicht. Wir erklären damit nicht die ganze
fremde Suite für abgeschlossen. Unser isolierter Norm-/Ritznachweis ist
hingegen abgeschlossen und reproduziert.

## 2. −1,138 ist eine echte bessere Variationsgrenze

Die Unterräume aus den normierten bosonweise geordneten Vektoren
\(v_k=T_+^kF\) sind nicht invariant, aber sie sind gültige Variationsräume.
Da unterschiedliche k orthogonal sind und H die Bosonzahl höchstens um
eins ändert, besitzt die Kompression auf v0,…,v5 exakt

\[
(H_6)_{kk}=k\Delta,\qquad
(H_6)_{k,k+1}=g\sqrt{\nu_{k+1}/\nu_k}.
\]

Aus der jetzt frisch geprüften ν5 wurde die charakteristische Gleichung
dieser **sechsdimensionalen reinen Leiterkompression** neu mit rationaler
Arithmetik aufgebaut. Eine unabhängige Sturm-Zählung beweist bei
g/Δ=1/20:

\[
\boxed{-1.13847420<E_{6}/\Delta<-1.13847419.}
\]

Die optional zusätzlich enthaltene Richtung w2 ergibt einen siebendimensionalen
Variationsraum. Ihre Norm ist weiterhin \(5001523200/229\). Ihre einzige
Kopplung innerhalb dieses Raums führt zu v3:

\[
\langle\widehat w_2,H\widehat v_3\rangle
=g\sqrt{\|w_2\|^2/\nu_3}.
\]

Die v1-Kopplung verschwindet durch w2⊥v2; alle anderen verschwinden schon
wegen der Bosonzahl. Der diagonale Wert ist 2Δ. Damit ist auch diese
Kompression vollständig bestimmt, ohne eine Schließung zu behaupten.
Ihre unabhängige rationale Wurzeleinschließung lautet

\[
\boxed{-1.13847610<E_{7}/\Delta<-1.13847609.}
\]

Nach Rayleigh-Ritz folgt die neue strenge Obergrenze

\[
\boxed{E_0<-1.13847609\Delta.}
\]

Die frühere Grundzustandsuntergrenze −1,158089Δ bleibt ein ausdrücklich
übernommener älterer exakter Eingang. Ebenso wird der ältere N=63-Floor
\(E_h>-1.121899\Delta\) übernommen. Zusammen ergibt sich neu

\[
\boxed{\epsilon=E_h-E_0>0.01657709\Delta.}
\]

Schon die reine Sechserkompression liefert ε>0,01657519Δ. Der Siebenerwert
ist etwas stärker; beide verbessern den v1.6.7-Floor 0,00773911Δ erheblich.
Der ältere N=63-Beweis und das große Grundzustandsarchiv wurden dabei nicht
erneut ausgeführt. Die neue Folgerung hängt ausdrücklich von diesem
beibehaltenen exakten Floor ab.

**Entscheidende Unterscheidung:** H6/H7 sind keine sechste oder siebte
Fortsetzung der in v1.6.7 berechneten vollständigen H-Lanczos-Kette. Schon
deren fünfter Vektor enthält v4+w2. Die Leiterkompression ist dennoch eine
gültige Ritzrechnung und darf deshalb ihre Energieobergrenze verbessern.
Ein kleines lokales Nichtschlussverhältnis oder eine flacher werdende
Ritzfolge beweist keine Konvergenz zum wahren Grundzustand. Die Behauptung
„nur sehr nahe an mit fünf Zahlen lösbar“ bleibt unbegründet.

## 3. Der Text vermischt drei verschiedene Näherungszustände

Die neuen kleinen Matrizen wurden unabhängig diagonalisiert. Sie bestätigen
die gespeicherten numerischen Ritz-Erwartungswerte, aber nicht deren
Umdeutung zu exakten Eigenschaften von Ω.

| Größe | Fünferbasis v0,…,v3,w2 | Sechserbasis v0,…,v5 | Siebenerbasis zusätzlich w2 |
|---|---:|---:|---:|
| Ritzenergie/Δ | −1,0942318710 | −1,1384741999 | −1,1384760929 |
| ⟨Nb⟩ | 0,8421158543 | 1,0177373262 | 1,0177445059 |
| Gewicht für Addition | 0,02631612045 | 0,03180429144 | 0,03180451581 |
| Gewicht für Entnahme | 0,97368387955 | 0,96819570856 | 0,96819548419 |
| Quadrat der F-Überlappung | hier nicht benötigt | 0,3498924448 | 0,3498903640 |
| Shannon-Entropie der Bosonzahl | hier nicht benötigt | 1,8712372972 Bit | 1,8712435534 Bit |

Die Werte **0,974/0,026 und 0,03Δ/1,15Δ gehören ausdrücklich zur kleineren
Fünferbasis**, wie `compute_charged_response` ab Zeile 900 und das Feld
`charged_response.basis` zeigen. Die höhere Norm allein macht diese
expliziten Vielteilchenvektoren nicht länger; die Funktion setzt Kc=min(3,Kmax).

Für einen G-Singulettzustand im N=64-Sektor gelten die exakten Summenregeln

\[
Z_\mathrm{add}=\langle N_b\rangle/32,\qquad
Z_\mathrm{rem}=1-\langle N_b\rangle/32.
\]

Damit sind die verschiedenen Tabellenwerte unmittelbar nachrechenbar.
Die Summe eins ist die CAR-Summenregel für das gesamte spektrale Gewicht;
sie bestimmt keine einzelne Spektrallinie und liefert noch kein natives
Präparations- oder Messinstrument. Der kleine Näherungswert Zadd≈0,026316
liegt sogar unter dem früheren exakten Ω-Floor
0,842846/32=0,0263389375. Er kann daher nicht als derselbe exakte
Grundzustandswert übernommen werden.

Die Shannon-Entropie der Bosonzahl ist wegen der verschiedenen Lochzahlen
eine Untergrenze für die Boson/Fermion-Verschränkungsentropie **dieses
jeweiligen reinen Ritz-Zustands**. Der Zahlenwert 1,87 Bit ist keine hier
bewiesene Untergrenze für den wahren nativen Grundzustand. Das gilt genauso
für die 35-Prozent-Überlappung.

### Die mittleren Antwortenergien lassen sich ohne riesige Zustandsdateien korrigieren

Aus den CAR folgen für jeden normierten G-Singulettzustand mit N=64:

\[
\begin{aligned}
\sum_r\langle f_r^\dagger Hf_r\rangle
&=\Delta(64\langle N_b\rangle-2\langle N_b^2\rangle)
+2g\operatorname{Re}\langle T_+(62-2N_b)\rangle,\\
\sum_r\langle f_rHf_r^\dagger\rangle
&=2\Delta\langle N_b^2\rangle
+2g\operatorname{Re}\langle T_+(2N_b)\rangle.
\end{aligned}
\]

Dabei folgt die erste Identität aus
Σf†T+f=T+(Nf−2) und Σf†T−f=T−Nf; die zweite aus den entsprechenden
CAR-Identitäten für f…f†. Die G-Invarianz macht alle 64 Modenantworten
gleich. Nb und die benötigten T+-Matrixelemente sind bereits in den
kleinen Ritzkompressionen enthalten.

Die separate kleine Rechnung `late_a/moment_audit.py` reproduziert so die
gespeicherten Fünferwerte 0,03107315818Δ und 1,14969200224Δ ohne Millionen
Besetzungsamplituden. Für den **Siebener-Ritz-Zustand** ergibt dieselbe
Rechnung stattdessen die mittleren Kosten

\[
\overline\epsilon_{\rm rem}\approx0.03479766990\Delta,\qquad
\overline\epsilon_{\rm add}\approx1.05931330814\Delta.
\]

Das korrigiert die Basisverwechslung und ist eine nützliche kleine
Ausleserechnung. Es sind numerische erste Momente eines Variationszustands,
keine neu bewiesenen Ω-Polenergien. Sie dürfen insbesondere nicht mit der
strengen unteren Entnahmeliniengrenze aus Abschnitt 2 gleichgesetzt werden.

## 4. Was bereits überholt ist

| Aussage der Anlage | Prüfung |
|---|---|
| Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt | Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. |
| Mit allen gewährten inneren Kontrollen bleiben im N=3-Sektor sieben Kommutantparameter | Bekannte bedingte Algebraaussage; beweist keine physische Verfügbarkeit dieser Griffe. Die Milliardenangaben sind Algebradimensionen, keine Zahl physischer Orte. |
| Auf der zweiten Bosonstufe gibt es einen zweiten Zustand | Richtig, aber unvollständig: v1.6.7 hat bereits genau vier Singulett-Richtungen und ihre vollständige Projektion berechnet. |
| Der N=64-Grundzustand sei bei g/Δ=1/20 nun wieder grundsätzlich offen | Die hier benutzten groben Konkurrenzschranken reichen dort nicht; das widerlegt den früheren stärkeren nativen Satz nicht. Der Quellwert g*≈0,02705688 gehört zu diesem schwächeren, numerisch ausgewerteten Schrankenverfahren. |
| Einheitlicher Vermittler müsse universell ein antisymmetrischer Tensor sein | Der Fünfzyklus ist ein echter bekannter Ausschluss der angegebenen binären Händigkeit auf primitiven Labels. Die Feldschlussfolgerung bleibt an diesen ableitungsfreien, unvergrößerten Ansatz gebunden; kein allgemeines relativistisches Wörterbuch wird klassifiziert. |
| Alle drei fundamentalen Vorfragen seien jetzt exakt beantwortet | Zu stark: Kontrollverfügbarkeit, tatsächliche Ω-Erwartungswerte und ein umfassender relativistischer Feldanschluss bleiben verschieden weit offen. |

## 5. Was daran spannend ist und was als nächstes trägt

Der gute neue Schritt ist **die tatsächlich abgeschlossene fünfte
Spurnetzwerk-Norm mit der daraus folgenden stärkeren strengen Energie- und
Entnahmeschranke**. Hinzu kommt unsere kleine CAR-Auswertung, die die
geladenen ersten Momente auf den richtigen größeren Ritz-Zustand hebt.
Das verbessert nachprüfbar die Rechnung im bestehenden nativen Modell.

Die Grundlage für die fundamentale Fortsetzung bleibt dagegen der gerade
in v1.6.8 präzisierte gemeinsame Prozess: ursprüngliches Operationsalphabet,
getypter Referenzträger, Zustand, gemeinsame Auslesung und überprüfbare
Interferenz. ν5 ersetzt weder den Herkunftsnachweis eines zusätzlichen
Griffs noch den neuen genauen Unterschied zwischen gemeinsamer Referenz-
dynamik und einem isolierten Systemantrieb.

## Reproduktionsbelege

`late_a/verify.py` prüft elf eingefrorene Eingaben, führt die ν1-ν5-
Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf.
Es gibt **46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische
Prüfungen und 10 numerische Konsistenzprüfungen**, separat dazu 1239
ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine
unabhängigen mathematischen Theoreme.

Normal/-OO laufen mit Warnungen als Fehler und liefern byteidentische
Ergebnisdateien mit SHA-256
`eaa83083d8232d17772d11f8c7c27015a9fe852162586a545d20d39a203f3471`.
Die zusätzliche Momentkontrolle benötigt nur kleine Matrizen und zwei
Quellenpins; sie führt den großen Norm- oder Grundzustandslauf nicht erneut
aus. Kein fremder Lauf wurde als abgeschlossen umetikettiert.

```sh
python3 -B -W error late_a/verify.py --output late_a/results_normal.json
python3 -OO -B -W error late_a/verify.py --output late_a/results_optimized.json
cmp late_a/results_normal.json late_a/results_optimized.json
python3 -B -W error late_a/moment_audit.py --output late_a/moments_normal.json
python3 -OO -B -W error late_a/moment_audit.py --output late_a/moments_optimized.json
cmp late_a/moments_normal.json late_a/moments_optimized.json
```


---

# Nachtragsprüfung B: Feldprojektor und Lorentz-Händigkeit

# Nachgereichter Text B: Korrekturen und ein neuer prüfbarer Feldadapter

Der Text mit 45 Zeilen wurde vollständig gelesen. Seine unveränderte Kopie
steht in `late_sources/attachment_B.txt`, SHA-256
`9aaf5e18cbc6a84d610b88429872df9b69e6078365bfdc8133c8f17e2c1c3801`.
Die für die neue Prüfung maßgebliche `field_dictionary.py` ist gesondert
eingefroren, SHA-256
`a581bacd17c08dd9a766ae439bfe1e8e35e6d30b9509cb9d98053b897d8ecc13`.
Die bereits abgeschlossenen Schatten-Dateien wurden nicht verändert.

## Übernahmeentscheidung

| Aussage im Text | Belastbare Fassung / konkrete Folge |
|---|---|
| 1,44 Milliarden unsichtbare Freiheiten im kleinsten nichttrivialen Sektor | 1444233216 ist die komplexe Kommutantdimension des gewährten Kontrollsatzes X,Nb im N=3-Sektor. Im N=2-Sektor lautet die entsprechende Zahl 3829536. Weder Zahl zählt direkt physische Freiheitsgrade. |
| Mit voller Symmetrie sieben, mit Modenzählern eins; damit nichts Physisches verborgen | Die assoziativen Algebren sind unter den ausdrücklich ergänzten Ressourcen bestimmt. Ein skalarer Kommutant beweist weder vollständige dynamische Lie-Kontrolle noch ausführbare Präparation/Messinstrumente. Ein neuer exakter Spin-1-Gegenzeuge unten trennt diese Aussagen. |
| Die Kontrollfrage ist eine einzige Ja/Nein-Frage | Bereits v1.6.6/7 enthalten Zwischenstufen: einzelner Dunkelprojektor, ein getrennter Casimir, nur SU(4), nur Spin(10). Auch X und Nb unabhängig schalten zu können ist stärker als ein fixes H. |
| Nur beide getrennten Casimire können die drei dunklen Typen unterscheiden | Bereits einer der getrennten Casimire genügt, da seine drei Eigenwerte verschieden sind. Der Gesamtcasimir allein genügt nicht. |
| Der Skalarkanal ist endgültig verboten; Vermittler muss (1,0) sein | Exakt im lokalen, ableitungsfreien Ansatz gleicher Weylhändigkeit mit unverändertem antisymmetrischem W und ohne zusätzliche unabhängige Komponenten. Der symmetrische Kanal trägt dort. Dies ist kein vollständiges Feldwörterbuch jedes möglichen Kontinuumsadapters. |
| Das Lochkomposit besitzt einen brauchbaren Spin-1/2-Projektor | Der angegebene Projektor ist für den **gleichhändigen** Tensorproduktraum korrekt. Für das wörtlich adjungierte Weylfeld ist zunächst die Händigkeit zu klären; die neue exakte Boost-Prüfung unten macht die Konsequenz sichtbar. |
| N=0 modulo vier verkürzt die Grundzustandskonkurrenz auf Singulettsektoren | Die Regel gilt für Singuletts. Erst ein unabhängiger globaler Eindeutigkeitssatz erzwingt für die zusammenhängende halbeinfache Gruppe einen Singulett-Grundzustand. Ohne ihn kann ein tieferes nichtsinguläres, entartetes Multiplett gewinnen. Zudem ist die Liste bosonischer Ladungssektoren nach oben unbeschränkt. |
| 480, 916, 299520/229 sind drei exakte Energiesprossen | Es sind dimensionslose quadrierte Kopplungskoeffizienten, nach Ausklammern von g², keine drei Eigenenergien. Sie stimmen mit dem Anfang der richtigen Voll-H-Lanczoskette überein. |
| Nur die gesamte 33-Sprossen-Leiter fehlt noch | 33 zählt die Bosonzahlstufen k=0,…,32 bei N=64. Eine Zustandsrichtung je Stufe schließt unter H nicht. Schon k=2 hat vier Singuletts; das Rücklaufresiduum besitzt exakt positive Norm 5001523200/229. Die tatsächliche vierte Voll-H-Lanczosdiagonale ist 105168998/26292551·Δ, nicht 4Δ. |
| Ritzüberlappung 39,7 Prozent bestätigt den wahren Grundzustand | Der Wert gehört zum benannten Ritz-Zustand. Ohne Residuum und Spektralabstand ist er keine entsprechende Überlappungsaussage über Ω. Die zitierte Ritzenergie setzt außerdem g/Δ=1/20 voraus. |
| Schwächere Nachbarsektorfloors lassen Grundzustandssatz wieder offen | Sie lassen diese schwächere Sonde offen. Das widerlegt oder ersetzt den stärkeren vorherigen Satz im unveränderten Modellvertrag nicht. |
| Operationssatz und Feldwörterbuch fertig; räumliche Skalierung jetzt freigegeben | Die erforderlichen Ressourcen und der Lorentzadapter sind weiterhin konkrete offene Verbindungen. Die neue gemeinsame Schattenkarte bestimmt deren nächste Prüfung wesentlich genauer als diese pauschale Freigabe. |

Die normierte direkte Summe der drei Feldkanäle hat weiterhin Norm
8√3 bei Normquadrat 192. Die eingefrorene Feldquelle enthält noch die
bereits korrigierte Addition von drei Normen zu 24; ihr gesamtes grünes
Ergebnis wurde daher nicht als unkritischer Vertrauensbeweis übernommen.

## 1. Neuer exakter Kontrollgegenzeuge

Die gewöhnlichen drei Spin-1-Matrizen J_x,J_y,J_z auf C³ erfüllen
[J_x,J_y]=iJ_z und zyklisch. Bereits J_x und J_z haben ausschließlich
skalare gemeinsame Kommutanten. Der dynamische Lie-Raum ist trotzdem nur
su(2) mit Dimension drei, nicht su(3) mit Dimension acht. Das wird im
neuen Prüfer durch exakte Ränge und alle drei Kommutatoren kontrolliert.

Damit ist die Unterscheidung praktisch: Ein assoziativer Abschluss kann
vollständig sein, während die tatsächlich durch Hamiltonpulse erreichbaren
Unitären eine echte Untergruppe bilden. Für den nativen Kontrollvertrag
braucht es weiterhin die konkret gewährten Generatoren, ihre dynamische
Lie-Algebra und eine ausgeführte Puls-/Instrumentenfolge.

## 2. Was am Spin-1/2-Projektor stimmt

Die Feldquelle verwendet die sechs unnormierten Koordinaten

`(00,0), (00,1), (01,0), (01,1), (11,0), (11,1)`,

wobei `(01)` die Summe `|01>+|10>` bezeichnet. Die korrekte Gram-Matrix ist

\[
 G_6=\operatorname{diag}(1,1,2,2,1,1).
\]

Der neue Prüfer baut den vollständigen Symmetrisierer auf drei Spinorindizes
unabhängig neu auf. Zugleich konstruiert er die direkte Epsilon-Auslese

\[
 C=\begin{pmatrix}0&1&-1&0&0&0\\0&0&0&1&-1&0\end{pmatrix},
 \qquad R=\frac23G_6^{-1}C^T.
\]

Exakt gelten

\[
 CR=I_2,\quad P_{1/2}=RC,\quad
 P_{3/2}=I_6-P_{1/2},\quad
 CP_{3/2}=0,\quad CP_{1/2}=C.
\]

Beide Projektoren sind idempotent, komplementär und haben Rang zwei
beziehungsweise vier. P_{1/2} ist selbstadjungiert bezüglich G_6;
seine nicht symmetrische 6×6-Koordinatenmatrix ist kein Fehler.
Die Epsilon-Auslese und Wiedereinsetzung intertwinen exakt alle drei
sl(2)-Generatoren. Dies liefert eine ausführbare algebraische Extraktionsregel
im **angenommenen gleichhändigen** Raum

\[
 (1,0)\otimes(1/2,0)=(3/2,0)\oplus(1/2,0).
\]

Die Zahl 1/3 ist nur der Ranganteil im isotropen Zustand. Der neue Prüfer
zeigt positive reine Vektoren mit Spin-1/2-Gewicht null und eins. Deshalb
ersetzt der Projektorrang keine Berechnung seines Gewichts im nativen
Grundzustand oder im geladenen Spektralpol.

## 3. Die neue präzise Händigkeitsschranke

Die eingefrorene Tabelle in `field_dictionary.py`, Zeile 327, bezeichnet
den zweiten Faktor als `f^dagger (1/2,0)`. Dafür muss die Feldabbildung
explizit festgelegt werden. Für ein tatsächliches adjungiertes linkes
Weylfeld gilt dagegen ψ† in (0,1/2). Hermitesche Konjugation vertauscht
diese Darstellungen; siehe [Dreiner, Haber und Martin, Abschnitt 2](https://arxiv.org/pdf/0812.1594#page=9).

In diesem **wörtlichen Feldadjungierten-Fall** ist das Produkt

\[
 (1,0)\otimes(0,1/2)=(1,1/2)
\]

ein irreduzibler Lorentzraum mit komplexer Dimension sechs. Unter der
Rotationsuntergruppe zerfällt er weiterhin in Spin 3/2 und Spin 1/2;
diese beiden Rotationsräume sind aber nicht getrennt boostinvariant.
Der Prüfer verifiziert den skalaren Kommutanten sämtlicher sechs
Generatoren des komplexifizierten Lorentzraums; die beiden unabhängigen
sl(2)-Faktoren wirken als irreduzibles äußeres Tensorprodukt.

Ein konkreter Zeuge genügt bereits. In obiger Basis setze

\[
 J_z=J_z^{(1)}\otimes I_2+I_3\otimes J_z^{(1/2)},\qquad
 K_z=J_z^{(1)}\otimes I_2-I_3\otimes J_z^{(1/2)}.
\]

Bis auf den konventionellen Faktor i ist K_z der Boostgenerator für
entgegengesetzte Händigkeit. Dann gilt exakt

\[
 [P_{1/2},J_z]=0,\qquad
 [P_{1/2},K_z]=
 \begin{pmatrix}
 0&0&0&0&0&0\\
 0&0&4/3&0&0&0\\
 0&-2/3&0&0&0&0\\
 0&0&0&0&2/3&0\\
 0&0&0&-4/3&0&0\\
 0&0&0&0&0&0
 \end{pmatrix}.
\]

Dieser Kommutator hat Rang vier. Der Rotationsprojektor kann deshalb
in diesem Vertrag nicht als Lorentz-kovarianter Weyl-Ausleseprojektor
verwendet werden.

**Das ist kein pauschaler Ausschluss des ursprünglichen Modenkomposits.**
Ein bloßer Fock-Erzeuger f† ist noch kein adjungiertes lokales Weylfeld.
Bereits die übliche linke Weylfeldentwicklung enthält Erzeugungs- und
Vernichtungsterme mit passenden Spinorwellenfunktionen; siehe
[Dreiner, Haber und Martin, Gleichungen 3.1.3-3.1.5](https://arxiv.org/pdf/0812.1594#page=24).
Eine unabhängige oder passend ladungskonjugierte gleichhändige Komponente
kann den gleichhändigen Projektor erhalten. Sie muss aber als konkreter
Adapter mit korrekter Ladung, CAR, W-Kontraktion und Dynamik gezeigt werden.
Aus dem Symbol † allein folgt weder ihr Vorliegen noch ihr Ausschluss.

## 4. Konkreter nächster Annahmetest

Der Anschlussauftrag ist jetzt endlich und entscheidbar formuliert:

1. Den tatsächlichen Feldadapter für `D_r ∼ b f†` beziehungsweise den davon
   verschiedenen `χ† ∼ b†ηf†` hinschreiben: gepunktete/ungepunktete Indizes,
   Ladung, Fourieranteile, erlaubte Zusatzkomponenten.
2. Für genau diesen Adapter alle Rotations- **und Boostgeneratoren** auf
   dem zusammengesetzten Träger berechnen. Ein Kandidat mit Lorentz-Auslese
   C muss `C L_composite = L_Weyl C` erfüllen. Der neue gleiche-/gegengängige
   Test liefert dafür positive und negative Referenzfälle.
3. Die Kontraktion am unveränderten W ausführen und anschließend das
   tatsächliche Matrixelement `C D_r†|Ω>` beziehungsweise den entsprechenden
   Ladungskanal berechnen. Erst dessen normiertes Spektralgewicht kann den
   vorhandenen geladenen Pol mit einem Spin-1/2-Feld verbinden.
4. Falls der wörtlich adjungierte Fall gewählt wird, keinen bloßen
   Rotationsprojektor als Lorentzprojektor verwenden. Ein zusätzlicher
   Impuls-/Ableitungsadapter oder eine andere Händigkeit kann untersucht
   werden, zählt aber als ausdrückliche neue Struktur.

Dieser Test ergänzt die gemeinsame Schattenrekonstruktion: Die dort
bewiesene vollständige innere Tomographie ersetzt die hier fehlende
Lorentz-Intertwining-Abbildung nicht. Umgekehrt definiert ein richtiger
Lorentzprojektor noch kein ausführbares natives Messinstrument.

## Reproduktion

```sh
python3 -B replay_late_field.py
```

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei
Quellenpins sowie **36 exakte Bedingungen pro Modus**, keine numerischen
Bedingungen. Normaler Lauf und `-OO` ergeben byte-identische JSON-Ausgaben;
Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv.
Die vollständigen Matrizen stehen in `late_field.normal.json`.

Das Ergebnis-JSON hat SHA-256
`cfd9e15cec5c2b0ce3de9397614836b16b24b4adb8f6711eb704925589965774`.
Der Prüfer hat SHA-256
`f18e6fd2af7c1a28a81e85654df68fe805e59b1d957801611d2668678550dfc2`.
Die fremde Feldsuite wird nur eingefroren und punktuell unabhängig geprüft,
nicht als vollständig fehlerfreie Gesamtreproduktion ausgegeben.


---

# Nachtragsprüfung C: fundamentale Reduktion und globale Quelle

# Nachtrag C: überwiegend bereits abgedeckte fundamentale Reduktion

## Übernahmeurteil

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen
fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere
Gesprächszusammenfassung. Er bringt **keinen neuen H-Term, keine neue
Operationsquelle und keinen neuen Transferbeweis**. Seine wesentlichen
mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen
Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendig.

Neue Eingabe: 299 Zeilen,
SHA-256 `a10f702306c7409535df9f4d26f0995970833a62297a1cb93d8c95cdce746d4d`.
Quelle: `/Users/stefanhamann/.codex/attachments/b0d7e533-3ca8-4a84-966c-2546b066dd08/pasted-text.txt`.

Bereits eingefrorene Kurzfassung:
`universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt`,
99 Zeilen, SHA-256
`0081cebd9759e8fa776995ee8efb3231c7611a82bea9cdeea86967073d1459a2`.
Die Dateien sind nicht bytegleich; der Neuheitsbefund betrifft ihren Inhalt.

## Was bestätigt und bereits abgedeckt ist

| Aussage | Urteil und Grenze |
|---|---|
| Volle Schur-Antwort T†F(H−E0)T=γF I64 | Richtig bei gruppeninvariantem H und Grundzustand sowie irreduziblem ursprünglichem Entnahmemultiplett. Gilt für die volle beschränkte Spektralfunktion, nicht nur einen dominanten Pol. Schon in v1.6.7 BIG_PICTURE B2 und der eingefrorenen Kurzfassung enthalten. |
| Aus C_rs(t)=δ_rs c(t) folgt kein Ortsindex in diesen 64 Labels | Richtig. Eine andere lineare Benennung erzeugt nur einen Gramfaktor. Keine pauschale Sperre gegen Vielteilchendynamik, nichtinvariante Referenzzustände oder andere Operatorfamilien. |
| Symmetriekommutant und Operationskommutant haben verschiedene Bedeutung | Richtig und bereits unterschieden. Erstgenannter erlaubt Dynamik zwischen Vorkommen desselben Typs; ein großer Kommutant eines eingeschränkten Operationssatzes kann fehlenden Zugriff anzeigen. Seine Größe beweist weder Raum noch ausführbare Kontrolle. |
| μN ist bei festem Gesamt-N eine Konstante | Richtig. Auf demselben präparierten Eingang bleiben freie Heisenbergentwicklungen neutraler Observablen identisch. Für ganze Interventionsfolgen muss auch deren zugelassener Gesamtvertrag respektiert werden. |
| Eine globale Zustandsregel braucht keinen äußeren Präparator | Richtig. Das Verbot, mit N-erhaltenden Operationen aus N=0 nach N=64 zu gelangen, ist ein Satz über einen bestimmten Präparationsweg. Es verbietet weder eine globale Randbedingung noch eine andere begründete Zustandsregel. Interne Detektoren und Präparationen bleiben trotzdem herzuleiten. |
| Keine nichttriviale Fermion-Teilparität in einer nativen Bank bei festen Bosonen | Bereits exakt geprüft: zusammenhängender W-Paargraph und binärer Rang 63. Ein Paritätsverbot getrennt kopierter Banken darf nicht auf beliebige Teilmengen derselben Bank übertragen werden. |

Das eigene v1.6.8-Ergebnis ergänzt diese Diagnose: Der bedingte lokale
Phasenimpuls und die terminale Tomografie benutzen einen gemeinsamen
invarianten N=2-Dreizustandsraum. Dessen Startzustand ist nicht der in
Schurs Aussage vorausgesetzte invariante N=64-Grundzustand. Es gibt daher
keinen Widerspruch und keine Berechtigung, die neue Umverteilung auf dessen
geladenen Einlochpol oder auf räumliche Bewegung zu übertragen.

## μ=Δ/50: gegen die älteren gepinnten Zertifikate bestätigt

Das ältere
`universalraum-native-ground-response-20260915/ground_replay/weak_coupling_ground_normal.json`
enthält genau die genannte Grenze: g/Δ=1/20, μ/Δ=1/50 und neuer Grundsektor
N=0. Sein SHA-256 ist
`e1cd19988edd33c6799ec6b80f0a52d56e1a532bfe1b56870623a4efaf06bd0c`;
dies stimmt mit `ground_replay_manifest.json` überein. Normaler und
optimierter vorhandener Bericht sind weiterhin bytegleich. Der eingetragene
Programmpin
`794554393c495ba395f34e6a58d490da821408d4f8effbc394653cd4cec4e80a`
stimmt mit der vorhandenen `ground_replay/work/many_pair/weak_coupling.py`
überein.

Die stärkere und direktere Begründung ist bereits in
`universalraum-v16-integrated-20260915/RESULTS.md` §3 und dessen
`new_checks.json` dokumentiert. Der Checkerhash
`c3304a1cf502e5c4fffd63391cfb29db02ad3f2b3517f96e047c07170b63416e`
stimmt mit dem vorhandenen Programm und `replay_manifest.json` überein.
Aus der dort geprüften Voll-Fock-Schranke

\[
A=\sum_A P_A^\dagger P_A\le\frac{15}{2}N_f
\]

und quadratischer Ergänzung folgt

\[
H_\mu\ge\left(\mu-\frac{15g^2}{2\Delta}\right)N_f+2\mu N_b.
\]

Die einzige erneut benötigte Rechnung ist rational:

\[
\frac1{50}-\frac{15}{2}\left(\frac1{20}\right)^2=\frac1{800},
\qquad2\mu/\Delta=\frac1{25}.
\]

Also gilt \(H_\mu\ge\Delta N/800\). Da N=0 nur das leere Fockvakuum
enthält und Hμ dieses mit Energie null annihiliert, ist es eindeutig
minimal. Der globale Zustandsgegenvergleich ist damit bestätigt. Der
vollständige ältere Grundzustands-/Casimir-Prüflauf wurde für diesen
Nachtrag nicht neu ausgeführt; Pins, vorhandene Aussagen und die relevante
exakte Ungleichung wurden geprüft.

## Zwei Präzisierungen bei der Übernahme

1. In §7 sollte „ein positiver Unterschied“ durch **„eine
   nichtverschwindende Differenz“** ersetzt werden. Ein negativer signierter
   Unterschied ist ebenso ein kausaler Interventionsnachweis; genau dies
   zeigt der neue N=2-Phasenversuch.
2. Die globale Sektorwahl und die Beobachtbarkeit innerhalb eines festen
   Gesamtsektors getrennt halten. Ein System-Referenz-Vergleich kann relative
   Ladungsenergien aufdecken; ein Zusatz μN_total auf einem festgehaltenen
   Gesamtsektor bleibt dennoch eine unbeobachtbare gemeinsame Phase.

**Fazit:** Hauptpunkt abgedeckt, keine neue globale Schließung. Die
ausführlichere Quelle stärkt die Dokumentation der Voraussetzungen und die
Abgrenzung der Zustandsregel. Die tatsächliche neue Konstruktion dieser
Runde bleibt die gemeinsame bedingte N=2-Ausführung aus kausalem Eingriff
und terminaler Zustandstomografie.


---

# Historischer Teil: vollständige Hauptfassung v1.6.7

Die folgende Fassung bleibt wortgetreu erhalten. Den aktuellen Stand liefern die vorangestellten Kapitel v1.6.8. Frühere Aussagen, Fragen und Vorhaben werden dadurch nicht rückwirkend neu bewiesen. Die neue Synthese ist separat vollständig im eingefrorenen Prüfpaket enthalten.

# TFPT / Universalraum: die richtige einfache Kette

## Vollständige Konsolidierung v1.6.7 - 15. September 2026

### Ergebnis und Leseschlüssel

Die zuletzt ergänzte Vogelperspektive steht im Teil B dieser Fassung:
**Gesucht wird der kleinste gemeinsame beobachtbare Prozess hinter den
verschiedenen Ansichten.** Ein nativer Rang-60-Kodierer ist bereits vorhanden.
Seine Informationsverluste, die minimalen symmetrieverträglichen Dynamiken
und der Unterschied zwischen Korrelation und kausalem Eingriff wurden neu
berechnet. Das verschiebt die fundamentale Priorität von weiteren lokalen
Näherungswerten zur Herkunft der Operationen und zur gemeinsamen Schattenkarte.

Die neue Runde schließt zwei kleine Strukturfragen vollständig: Der symmetrische
Zustandsraum bei zwei Bosonen hat exakt vier Dimensionen; der bisher unbestimmte
Rest von 4035 bilinearen Komponenten zerfällt vollständig in drei Darstellungen.
Die vier Zustandsrichtungen und ihre Kopplungen wurden zusätzlich am ursprünglichen
Tensor berechnet. Daraus folgt ein vollständiger sechs-dimensionaler Ausschnitt.

Die gewünschte einfache Kette existiert ebenfalls, aber anders als vorgeschlagen:
Man muss den **ganzen Hamiltonoperator** wiederholen, nicht Bosonzahl und
Iterationsnummer gleichsetzen. Die ersten fünf Lanczos-Glieder sind jetzt exakt
bekannt. Sie bestimmen zehn Energiemomente des gefüllten Startzustands und
verschärfen die obere Grundzustandsgrenze geringfügig.

**Das ist keine vollständige TOE.** Insbesondere fehlen die physische Auswahl
des Modellvertrags, ausführbare ursprüngliche Instrumente, derselbe geladene
Transport im gemeinsamen Träger und die relativistische Kontinuumskonstruktion.
Dass die bisherigen Grunddaten dafür noch nicht eindeutig genügen, wird unten
an einer einfachen Familie verschiedener Dynamiken nachgewiesen.

Kennzeichnungen: **exakt** bezeichnet eine bewiesene Aussage im genannten
Modell; **bedingt** eine Aussage mit zusätzlich gewährter Operation oder
bekanntem früherem Satz; **numerisch** eine Näherung; **offen** einen fehlenden
Nachweis. Komplexe Algebradimensionen zählen weder physikalische Raumrichtungen
noch unabhängig hergeleitete Teilchen oder ausführbare Operationen.

Die Fassung baut auf dem vollständigen Hauptdokument v1.6.6 auf. Die aktuelle
Gesamtdarstellung steht voran; die frühere Fassung einschließlich ihrer
Herleitungen, Gegenbeispiele und älteren Anhänge bleibt vollständig erhalten.
Alle sechs in dieser Runde eingesandten Texte werden unverändert dokumentiert und
hier mit überprüften Ergänzungen und ausdrücklich benannten Korrekturen gelesen.

## 1. Das Gesamtbild: Grammatik, Prozess, Zustand, Antwort

TFPTs Compiler beschreibt zunächst eine markierte algebraische Grammatik:
welche Bausteine zusammenpassen, welche Symmetrien gelten und welche Zahlen
innerhalb dieser Konstruktion folgen. Der Universalraum soll diese Grammatik
als einen ausführbaren Prozess realisieren. Der entscheidende Unterschied ist
der zwischen einem erlaubten Zusammenhang und einer tatsächlich erzeugten
physikalischen Entwicklung.

Im hier untersuchten Modell ist die Grundregel weiterhin sehr einfach:
**Zwei Fermionen können in einen Vermittler umgewandelt werden und zurück.**
Mit 64 Fermionmoden und 60 Bosonmoden lautet sie

\[
H=\Delta N_b+g(T_++T_-),\qquad
T_+=\sum_A b_A^\dagger P_A,\quad T_-=T_+^\dagger,
\qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i.
\]

Es gelten \(\Delta>0\), reelles \(g\) und die erhaltene Ladung
\(N=N_f+2N_b\). Der Tensor W besitzt 480 Einträge mit Werten +1 oder -1,
acht disjunkte Paare pro Zeile, und \(WW^\dagger=8I_{60}\).
Seine innere Darstellung ist \((16,4)\) für Fermionen und \((10,6)\)
für Bosonen unter Spin(10) mal SU(4).

Die heutige Beweiskette sieht so aus:

| Verbindung | Was bereits trägt | Was dadurch nicht automatisch folgt |
|---|---|---|
| Compiler zu Paarregel | Konkreter Tensor, Symmetrie und Ladungserhaltung | Physische Wahl von Energie, Kopplung und Instrumenten |
| Paarregel zu Zustand | Früherer eindeutiger Grundzustandssatz im festgelegten Vertrag | Herleitung dieses Vertrags oder dessen Präparation |
| Zustand zu geladener Antwort | Isolierte niedrige Fermion-Entnahmelinie mit hohem Gewicht | Räumlich laufendes relativistisches Teilchen |
| Antwort zu Bewegung | Zusätzliche Links erlauben nachgewiesenen Transfer | Dass derselbe Link aus dem ursprünglichen Operationssatz entsteht |
| Bewegung zu Raumzeit | Prüfprogramm und bedingte Modelle | Gemeinsame 3+1D-Welt, chirales Maß und dynamische Gravitation |

Der endliche dokumentierte Clock gehört zur inneren Spin(10)-Symmetrie.
Er ist damit kein zusätzliches äußeres Symmetrieobjekt. Seine Periode sechs
ist aber auch noch keine Herleitung einer physikalischen Zeiteinheit oder
einer Raumzeit. Innere Spin(10)-Labels sind nicht von selbst Lorentzspin.

## 2. Was die beiden neuen Texte beitragen

### 2.1 Quellenstand und Reproduktionsgrenzen

17 ausgewählte Eingaben wurden mit SHA-256 eingefroren: beide Nutzertexte,
die zugehörigen Programme und Ergebnisdateien, der native Tensor sowie die
vollständige frühere Fassung mit Prüfpaket. Keine fremde Quelldatei wurde
verändert. Die Herkunftsdateien gehören zu parallel fortgeschriebenen
Arbeitsständen; Dateipins sind deshalb wichtiger als Versionsnamen allein.

Der neue Grundzustandslauf war beim ersten Blick noch ohne Ergebnisdatei.
Beim Einfrieren lag bereits sein fertiges Ergebnis vor: **382 Guards,
davon 379 exakt und drei numerisch**. Sein Quellenhash stimmt mit der
eingefrorenen Programmdatei überein. Er findet ebenfalls die Multiplizitäten
1, 1 und 4. Der Zwischenhinweis dieser Prüfung auf eine noch leere Datei
war bei der späteren Übernahme bereits überholt und wird hier korrigiert.

Das Operations-JSON enthält **306**, nicht die im Begleittext genannten
307 Guards; sein interner Checkerhash passt nicht zur gleichzeitig
eingefrorenen Programmdatei. Das ist ein Versionskonflikt des Berichts,
kein Beweis, dass seine Mathematik falsch ist. Die tragenden Aussagen
werden deshalb unabhängig geprüft, nicht als exakter Gesamtreplay
dieses fremden Programms ausgegeben. Das Feld-JSON meldet 2161 Guards
und besitzt einen passenden Quellenhash; es enthält dennoch den unten
korrigierten Normfehler und zu weit formulierte Interpretationen.

Mit den weiteren Texten und zugehörigen Auditdateien sind es insgesamt 24 eingefrorene Eingaben.
Unsere eigene neue Suite hat **822 exakte Prüfbedingungen pro Python-Modus**.
Normaler und optimierter Lauf erzeugen identische Ergebnisdateien; Warnungen
werden als Fehler behandelt. Zusätzlich wurde die ältere ganzzahlige
Kontraktionsrechnung frisch kompiliert und wiederholt, mit identischen Zahlen.
Die vier-Boson-Norm aus dem früheren Zertifikat bleibt ein gekennzeichneter
Eingang: Ihre vollständige Enumeration wurde in dieser Runde nicht wiederholt.
Auch die gesamten fremden Programme mit ihren Guards wurden nicht alle erneut
ausgeführt. Prüfzahl und Beweisumfang werden ausdrücklich getrennt.

### 2.2 Übernahmeentscheidung

| Aussage aus den Eingaben | Entscheidung für v1.6.7 |
|---|---|
| Korrigierter Anfangskommutant 3829536 / 1444233216 | Bestätigt; keine neue Größe gegenüber v1.6.6 |
| Nur SU(4) oder nur Spin(10) als zusätzliche Kontrollen | Übernommen; echte Zwischenstufen statt binärer Verfügbarkeit |
| Volle Gruppe plus alle Modenbesetzungen erzeugt volle Sektoralgebra | Unabhängig bestätigt, ausdrücklich bedingt |
| Clock außerhalb der zusammenhängenden Gruppe, weil nicht skalar | Verworfen; das explizite Spin-Wort aus v1.6.6 widerlegt den Schluss |
| Vier Singuletts auf der zweiten Bosonstufe | Unabhängig bestätigt und durch konkrete Zustandsprojektionen ergänzt |
| Eine Zustandsrichtung pro Bosonzahl könnte bis Stufe 32 genügen | Verworfen; schon Stufe zwei hat vier Richtungen |
| Feldnorm 24 bei quadrierter Norm 192 | Korrigiert: Norm ist 8 mal Wurzel 3 in derselben Konvention |
| 4035 bilineare Komponenten unbestimmt | Jetzt vollständig in drei innere Darstellungen zerlegt |
| Jeder relativistische Abschluss müsse den Tensorfeldkanal verwenden | Nur unter dem festgelegten gleichhändigen, ableitungsfreien Ansatz gültig |
| Schwächere Sektorschranken trennen N=64 nicht | Richtig für diese Sonde; widerlegt den stärkeren früheren Satz nicht |

Die Entropie von ungefähr 1,66 Bit im ersten Text gehört zum dortigen
Ritz-Näherungszustand. Die Blockdiagonalität der reduzierten Bosondichte
rechtfertigt die Shannon-Untergrenze für diesen Zustand, nicht ungeprüft
denselben Zahlenwert für den wahren nativen Grundzustand.
Ebenso ist eine Kreuzung mit dem leeren Zustand bei einem bestimmten
chemischen Potential kein Beweis für die vollständige Sektor-Stabilitätszone.

## 3. Vollständig gelöst: der erste verzweigte Singulettbereich

### 3.1 Warum vier und nicht eins?

Im Ladungssektor N=64 schreiben wir Zustände relativ zur gefüllten
Fermionreferenz \(F\). Bei k Bosonen gibt es 2k Löcher. Der Singulettbereich
auf dieser Stufe liegt in

\[
\mathcal S_k=
\left[\Lambda^{2k}(\overline{16\otimes4})
\otimes\operatorname{Sym}^k(10\otimes6)\right]^{G},
\qquad G=\operatorname{Spin}(10)\times SU(4).
\]

Die ersten Dimensionen sind **1, 1, 4**. Dies ist eine Aussage über alle
Singuletts dieser Stufen, nicht über vier verschiedene Grundzustände.
Ein eindeutiger Grundzustand kann durchaus in einem größeren Singulettbereich
liegen. Die Zentrumsregel N gleich 0 modulo 4 ist nur eine notwendige
Bedingung für Singuletts, kein Auswahlprinzip für N=64.

Der Beweis für k=2 benötigt keinen riesigen Matrixkern. Die Bosonseite zerfällt
nach der symmetrischen Cauchy-Identität in

\[
\operatorname{Sym}^2(10\otimes6)=
(1,1)\oplus(54,1)\oplus(1,20')\oplus(54,20')\oplus(45,15).
\]

Die Dimensionen 1, 54, 20, 1080 und 675 ergeben zusammen 1830.
Die vierte äußere Potenz der Fermionseite wird durch die fünf Partitionen
von vier beschrieben. Für die benötigten Überschneidungen reichen drei
Spinor-Schurfunktoren:

| Bosontyp | Spinor-Schurfunktor auf der Fermionseite | Anzahl gemeinsamer Typen |
|---|---|---:|
| (1,1) | Sym hoch 4 von 16 | 0 |
| (54,1) | Sym hoch 4 von 16 | 1 |
| (1,20') | S mit Partition (2,2) von 16 | 1 |
| (54,20') | S mit Partition (2,2) von 16 | 1 |
| (45,15) | S mit Partition (3,1) von 16 | 1 |

Die Charaktere wurden aus den fünf Konjugationsklassen von S4 mit ganzzahliger
Arithmetik aufgebaut, durch eine unabhängige Jacobi-Trudi-Rechnung kontrolliert
und mit der Weyl-Alternierung ausgewertet. Die volle äußere Potenz hat
635376 Dimensionen; der gemeinsame Singulettbereich hier nur vier.
Die Berechnung des anderen Workers über den vollständigen Gewicht-Null-Raum
kommt unabhängig auf denselben Wert.

### 3.2 Nicht nur gezählt: die vier Zustände und ihre Kopplungen

In der durch eine Bosonparität äquivalenten Lochdarstellung sei
\(v_k=(T_+)^kF\). Alle 108240 von null verschiedenen Koeffizienten von
\(v_2\) wurden neu berechnet, einschließlich der Boson-Fakultätsnormen.
Das ergibt \(\|v_2\|^2=439680\).

Sei \(P_R\) der orthogonale Projektor auf den jeweiligen inneren Typ der
Zwei-Boson-Seite. Dann sind die vier Vektoren \(P_Rv_2\) nicht null,
orthogonal und bilden wegen der bewiesenen Multiplizität eins die gesamte
Singulettbasis auf Stufe zwei. Ihre Normen und die Kopplungen vom normierten
Ein-Boson-Zustand lauten:

| Typ R | Normquadrat von P_R v2 | Quadrierte Kopplung geteilt durch g hoch 2 |
|---|---:|---:|
| (54,1) | 17280 | 36 |
| (1,20') | 7680 | 16 |
| (54,20') | 241920 | 504 |
| (45,15) | 172800 | 360 |
| Summe | 439680 | 916 |

Diese Zahlen sind abgeleitet, nicht angepasst. Die Projektoren benutzen
nur Symmetrisierung sowie die beiden vorhandenen invarianten Spurbildungen.
Die gemeinsame skalare Projektion (1,1) verschwindet identisch.

Nach Wahl der vier Basisphasen ist der Kopplungsvektor

\[
g\,(6,\,4,\,6\sqrt{14},\,6\sqrt{10}).
\]

Alle vier Richtungen sind in v2 enthalten, aber von Stufe eins wird nur ihre
eine feste Linearkombination angeregt. Drei dazu orthogonale Kombinationen
sind **nach unten** dunkel. Sie sind nicht deshalb auch gegenüber den
höheren Stufen entkoppelt.

### 3.3 Der vollständig bestimmte Sechszustands-Ausschnitt

Die Kompression auf alle Singuletts mit k kleiner oder gleich zwei ist exakt
äquivalent zu

\[
P_{\leq2}HP_{\leq2}\simeq
\begin{pmatrix}
0&g\sqrt{480}&0\\
g\sqrt{480}&\Delta&g\sqrt{916}\\
0&g\sqrt{916}&2\Delta
\end{pmatrix}
\oplus 2\Delta I_3.
\]

Damit ist dieser Ausschnitt vollständig gelöst. **Er ist nicht invariant:**
H führt von k=2 auch nach k=3. Seine Eigenwerte sind folglich nicht automatisch
Eigenwerte der ganzen Bank. Eine räumliche Interpretation oder zusätzliche
Wechselwirkung wurde für diese Reduktion nicht eingeführt.

Explizit besitzt die Kompression dreimal den Wert 2 Delta und die drei
reellen Nullstellen des Polynoms

\[
E^3-3\Delta E^2+(2\Delta^2-1396g^2)E+960\Delta g^2.
\]

## 4. Die richtige einfache Kette: Wiederholung von H

### 4.1 Der Fehler war die Gleichsetzung zweier verschiedener Stufen

Die Vektoren \(v_k=T_+^kF\) sind nach Bosonzahl geordnet. Schon bekannt ist

\[
T_-v_3=\frac{299520}{229}v_2+w_2,\qquad
\langle v_2,w_2\rangle=0,\qquad
\|w_2\|^2=\frac{5001523200}{229}>0.
\]

Diese Rechnung wurde frisch reproduziert. Aus einer kleinen relativen
Norm dieses Seitenzweigs folgt keine Konvergenz der gesamten Grundzustands-
oder Spektralrechnung. Insbesondere fehlt dann immer noch der große Übergang
nach v4.

Eine Lanczos-Kette entsteht stattdessen aus
\(F,HF,H^2F,\ldots\) durch Orthogonalisierung. Für einen selbstadjungierten
endlichen Hamiltonoperator beschreibt sie dessen zyklischen Teilraum exakt.
Das ist ein zulässiges einfaches Rechenbild, aber keine Behauptung, dass ihre
Indizes physikalische Orte oder Bosonzahlen seien. Auch die gesamte Bank muss
nicht mit diesem einen zyklischen Teilraum übereinstimmen.

### 4.2 Die ersten fünf Glieder sind jetzt exakt bestimmt

Für die normierte Lanczos-Basis \(u_n\) schreiben wir

\[
Hu_n=b_nu_{n-1}+a_nu_n+b_{n+1}u_{n+1},\qquad b_n>0.
\]

Die ersten Diagonalen lauten

\[
\frac{(a_0,a_1,a_2,a_3,a_4)}{\Delta}
=\left(0,1,2,3,\frac{105168998}{26292551}\right).
\]

Die ersten quadrierten Nebendiagonalen sind

\[
\frac{(b_1^2,b_2^2,b_3^2,b_4^2)}{g^2}
=\left(480,916,\frac{299520}{229},\frac{78877653}{47632}\right).
\]

Bis u3 stimmen die Vektoren, bis auf die Phase bei negativem g, mit den
normierten vk überein. Der nächste Vektor ist proportional zu \(v_4+w_2\).
Dabei liegen v4 und w2 auf verschiedenen Bosonstufen. Deshalb gilt

\[
\frac{b_4^2}{g^2}
=\frac{\|v_4\|^2+\|w_2\|^2}{\|v_3\|^2},
\qquad
\langle u_4,N_bu_4\rangle
=\frac{4\|v_4\|^2+2\|w_2\|^2}{\|v_4\|^2+\|w_2\|^2}.
\]

Die Bosonzahlvarianz dieses Vektors ist exakt

\[
\operatorname{Var}_{u_4}(N_b)
=\frac{63416178576}{691298238087601}>0.
\]

Die frühere Quotientenfortsetzung mit nur \(\|v_4\|^2/\|v_3\|^2\)
ließ den positiven Zusatz \(1809/47632\) weg. Die korrigierte Kette bleibt
einfach, verliert aber gerade deshalb nicht die wirkliche Mehrkanalstruktur.
Ihre Länge ist nicht durch die 33 möglichen Bosonzahlen festgelegt.

### 4.3 Zehn vollständige Energiemomente der gefüllten Referenz

Die Fünfer-Kompression bestimmt
\(\mu_n=\langle F,H^nF\rangle\) für n von 0 bis 9 exakt. Ein Weg, der
den nächsten nicht enthaltenen Lanczos-Vektor erreicht und nach F zurückkehrt,
benötigt mindestens zehn Schritte. Aus der Tridiagonalität folgt deshalb die
angegebene Momentengenauigkeit, ohne die übrige Kette zu erfinden.

Beispielsweise gilt

\[
\mu_0=1,\quad \mu_1=0,\quad
\mu_2=480g^2,\quad \mu_3=480\Delta g^2,
\quad \mu_4=480\Delta^2g^2+670080g^4.
\]

Vollständig lauten die Koeffizienten in
\(\mu_n/\Delta^n=c_2x^2+c_4x^4+c_6x^6+c_8x^8\),
mit \(x=g/\Delta\), für n von 2 bis 9:

| n | c2 | c4 | c6 | c8 |
|---|---:|---:|---:|---:|
| 2 | 480 | 0 | 0 | 0 |
| 3 | 480 | 0 | 0 | 0 |
| 4 | 480 | 670080 | 0 | 0 |
| 5 | 480 | 2219520 | 0 | 0 |
| 6 | 480 | 5527680 | 1510510080 | 0 |
| 7 | 480 | 12353280 | 10437173760 | 0 |
| 8 | 480 | 26213760 | 48253363200 | 4615972423680 |
| 9 | 480 | 54144000 | 187581404160 | 54295325184000 |

Diese Momente gehören **F**, nicht dem nativen Grundzustand Omega. Sie sind
auch nicht mit den geladenen Antwortmomenten aus der früheren Fassung zu
verwechseln. Sie machen eine endliche Modellrechnung genauer, beweisen aber
keine physische Präparation von F und keine Vollständigkeit des Feldwörterbuchs.

### 4.4 Kleine, rigorose Verschärfung der Energiegrenze

Am Prüfpunkt g geteilt durch Delta gleich 1/20 hat die niedrigste Eigenenergie
der Fünfer-Kompression die durch rationale Sturm-Zählung zertifizierte Lage

\[
-1.12963813<\frac{E_{\mathrm{Ritz},5}}{\Delta}<-1.12963811.
\]

Rayleigh-Ritz liefert für den wahren Grundzustand daher

\[
E_0<-1.12963811\Delta.
\]

Die frühere untere Schranke bleibt \(E_0>-1.158089\Delta\).
Zusammen mit dem früheren strengen N=63-Floor
\(E_h>-1.121899\Delta\) folgt nun

\[
\epsilon=E_h-E_0>0.00773911\Delta.
\]

Die Verbesserung gegenüber 0.007737 ist klein. Die obere Polgrenze
0.039079764 und das Gewicht über 88.007628 Prozent werden dadurch nicht
ungeprüft verändert. Auch die niedrigste Ritz-Energie ist kein berechneter
Zentralwert von E0.

## 5. Vollständig gelöst: die innere bilineare Zerlegung

Für den 64-dimensionalen Fermionträger gilt

\[
\operatorname{End}(16\otimes4)
=(1,1)\oplus(45,1)\oplus(210,1)
\oplus(1,15)\oplus(45,15)\oplus(210,15).
\]

Die sechs Dimensionen sind 1, 45, 210, 15, 675 und 3150. Der offene Rest ist
also nicht mehr unbestimmt:

\[
4035=210+675+3150.
\]

Eine kurze konkrete Konstruktion genügt. Auf dem chiralen 16er-Raum liefern
Cliffordprodukte der Grade 0, 2 und 4 genau 1, 45 und 210 unabhängige
Matrizen. Ihr ganzzahliger Hilbert-Schmidt-Gram ist \(16I_{256}\).
Unter Spin(10)-Konjugation bleiben diese Gradräume invariant. Auf der
Farbseite zerfällt End(4) in die skalare Matrix und die 15 spurlosen Matrizen.
Die Tensorprodukte ergeben die gesamte Zerlegung. Die Weyl-Multiplizitäten
wurden zusätzlich überprüft.

Die verwendete Spinorzerlegung ist etablierte Darstellungstheorie, keine neue
Vorhersage von 210 physikalischen Teilchen. Der Literaturabgleich bestätigt
die drei Spin(10)-Kanäle 1, 45 und 210; unsere Rechnung ordnet sie der
tatsächlichen 16-mal-4-Bank zu. Siehe
[Nath und Syed, vollständige Spinorkopplungen](https://arxiv.org/abs/hep-th/0109116).

Aus dieser Zerlegung folgt weder, dass alle Bilineare verfügbare Kontrollen
sind, noch, dass jede Darstellung ein propagierendes Feld ist. Produkte
einfacher Matrizen im Einteilchenraum dürfen insbesondere nicht automatisch
als dieselben Produkte ihrer Vielteilchen-Hamiltonoperatoren gelesen werden.

## 6. Welche Operationen wirklich verfügbar sein müssten

### 6.1 Die algebraische Frage ist präziser beantwortet

Im N=3-Sektor bleiben für verschiedene **angenommene** Operationsalphabete
folgende komplexe Kommutantdimensionen:

| Angenommenes Alphabet | Kommutantdimension |
|---|---:|
| X und Nb | 1444233216 |
| Zusätzlich dokumentierter Clock | 240742144 |
| Stattdessen zusätzlich SU(4)-Generatoren | 2247168 |
| Stattdessen zusätzlich Spin(10)-Generatoren | 1648 |
| Zusätzlich beide vollständigen Gruppen | 7 |
| Volle Gruppen und alle Modenbesetzungen | 1 |

Die physische Verfügbarkeit ist somit nicht auf eine binäre Alternative
zusammengeschrumpft. Es gibt geprüfte Zwischenstufen, darunter auch die in
v1.6.6 behandelten einzelnen Casimir-Auslesungen.

Die volle Algebra nach Hinzunahme aller Besetzungen wurde unabhängig mit
einem kleineren Beweis kontrolliert. Der Einteilchen-Supportgraph der
gewährten Gruppengeneratoren ist verbunden, ebenso der Bosongraph.
Ein verbundener Graph hat verbundene Besetzungsgraphen mit k ununterscheidbaren
Fermionen, solange 0 kleiner k kleiner 64. Der native Tensor verbindet die
Fermion- und Bosonseiten. Die Besetzungsoperatoren trennen alle Basiszustände.
Polynomiale Spektralprojektoren und die nichtverschwindenden Verbindungseinträge
erzeugen daher alle Matrixeinheiten.

So folgt bedingt die volle Algebra in N=2 und N=3. Gewährt man zusätzlich
geladene f-Instrumente, verbinden sich auch die beiden Sektoren. Das ist eine
vollständige **assoziativ-algebraische** Aussage, kein Nachweis beliebiger
unitärer Steuerbarkeit, effizienter Messung oder nativer Instrumentenherkunft.

### 6.2 Warum bloßes Lesen noch keine fehlende Bewegung erzeugt

Ohne die zusätzlich gewährten Gruppenkontrollen erhalten X, Nb, der Clock
und alle Modenbesetzungen weiterhin mindestens eine nichtskalare Farb-Cartanladung.
Jede Komposition dieser Operatoren behält diese Erhaltung. Die alleinige
Erlaubnis, mehr Moden zu unterscheiden, hebt das Hindernis also nicht auf.

Das ist die präzise Grenze zwischen **Auslesen** und **Eingreifen**.
Ein mathematisch definierter Projektor ist nicht schon ein physisch
ausführbares Messinstrument. Dass das Modell unter einer Transformation
symmetrisch ist, bedeutet nicht, dass es diese Transformation als kontrollierten
Eingriff erzeugt. Die bedingten Zwei-Banken- und Vierzustands-Transferbeispiele
aus v1.6.5 und v1.6.6 bleiben nützlich, aber ihre zusätzlichen Links bleiben
auch zusätzliche Voraussetzungen.

## 7. Feldwörterbuch: gesicherte Teile und korrigierte Reichweite

Für die unveränderte antisymmetrische Paarmatrix und gleichhändige Weylfelder
verschwindet die ableitungsfreie skalare Kontraktion. Die drei symmetrischen
Spinortensoren tragen einen nichtverschwindenden Kanal des Typs (1,0), mit
konjugiertem Typ (0,1). Das ist am gesamten ursprünglichen Tensor neu geprüft.

In der Konvention des gelieferten Programms hat jeder der drei Kanäle pro
Zeile Normquadrat 64. Die Summe ist 192 und die direkte Summennorm folglich
\(8\sqrt3\), **nicht 24**. Die Summe von drei einzelnen Normen darf nicht
mit der Norm ihrer orthogonalen direkten Summe verwechselt werden. Eine
anders normierte Vertexdefinition ändert diese Zahlen, nicht den Nullkanal.

Der Satz gilt unter den genannten Feld- und Ableitungsannahmen. Zusätzliche
unabhängige Komponenten oder Ableitungskopplungen sind andere Modelle und
nicht generell ausgeschlossen. Keine dieser Möglichkeiten ist dadurch
bereits aus der ursprünglichen Bank hergeleitet.

Auch die Zerlegung eines Vermittler-mal-Weyl-Komposits in die Lorentztypen
(3/2,0) und (1/2,0) ist eine Darstellungsaussage. Der Ranganteil 2/6 gleich
1/3 ist das Gewicht im maximal gemischten Zustand dieses Sechserraums.
Für allgemeine Zustände kann derselbe Projektor Gewichte von null bis eins
haben. Er liefert nicht automatisch ein Drittel des nativen Polgewichts.
Die frühere Ladungsunterscheidung bleibt bestehen: Die EOM-Größe D trägt
Ladung minus eins, das ältere erzeugende Komposit chi-dagger plus drei.

## 8. Die fundamentale Frage: was fehlt wirklich?

### 8.1 Ein überprüfbarer Unterbestimmtheitssatz

Betrachte bei festem W dieselbe Familie
\(H_{\Delta,g}=\Delta N_b+gX\). Alle diese Hamiltonoperatoren besitzen die
gleiche innere Quellsymmetrie, dieselbe Ladungserhaltung und denselben
kommutierenden endlichen Clock. Dennoch unterscheiden sie sich dynamisch.
Schon für dieselbe gefüllte Referenz F ist die dimensionslose Momentenkombination

\[
\frac{\mu_4\mu_2}{\mu_3^2}
=1+1396\left(\frac{g}{\Delta}\right)^2.
\]

Bei g geteilt durch Delta gleich 1/20 ist sie 4,49, bei 1/40 dagegen 1,8725.
Beide Parameterpunkte liegen im früher abgesicherten Grundzustandsintervall.
Weil die Größe dimensionslos ist, handelt es sich nicht lediglich um eine
Änderung der Maßeinheit. Die gleiche Grammatik und Symmetrie lässt also
unterschiedliche Antworten auf dieselbe Präparation zu.

**Damit ist die eindeutige physische Dynamik aus diesen Grunddaten allein
nicht ableitbar.** Das widerlegt nicht die Möglichkeit einer einfachen
zusätzlichen Ursprungsregel. Es identifiziert genau deren Aufgabe:
Sie muss den Prozess samt verfügbarem Operationssatz und Zustand auswählen,
statt nur seine Symmetrie zu benennen. Im fest gesetzten Prüfvertrag sind g
und Delta natürlich definiert; offen ist ihre physische Herkunft.

### 8.2 Der kleinste tragfähige Forschungsansatz

Für eine einzelne Antwortrechnung sollte der relevante Raum nicht von
vornherein der gesamte Fockraum sein. Der zyklische Raum der tatsächlichen
Operationen auf dem angegebenen Startzustand ist der kleinere Arbeitsraum.
Die H-Lanczos-Kette ist eine exakte Darstellung eines solchen Raums.
Mehrere Präparationen, Messungen oder Compileroperationen können jedoch einen
größeren gemeinsamen Prozessraum verlangen. Ihre Kompatibilität muss dann
nachgewiesen werden; getrennte kleine Modelle dürfen nicht einfach
zusammengefügt werden.
Eine vollständige Rekonstruktion des Grundzustands aus dieser Referenz
verlangt außerdem einen Nachweis ihrer nichtverschwindenden Überlappung
mit Omega; die Ritz-Obergrenze allein ersetzt ihn nicht.

Die nächste physikalische Schließung bleibt dieselbe konkrete Bedingung:
Auf einer gemeinsam hergeleiteten Quelle und demselben Zustand muss eine
verfügbare Operation eine geladene Anregung zwischen operational bestimmten
Teilen übertragen. Der Test muss die Mehrzeitantwort von bloßem Überlapp
unterscheiden und ein konsistentes relativistisches Feldwörterbuch verwenden.
Koordinatenwechsel, Gram-Überlapp oder ein innerer Clock allein erfüllen
diese Bedingung nicht.

## 9. Aktueller Stand T1 bis T8

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen
Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

| Tor | Beitrag dieser Runde | Weiter fehlender entscheidender Nachweis |
|---|---|---|
| T1 | Exakte bedingte Kontrollalgebra; Auslese- und Eingriffslücke präzisiert | Tatsächlich erzeugbare Compileroperationen und Instrumente |
| T2 | Bessere lokale Struktur und Antwortgrenze in der endlichen Bank | Quellseitiges Half-Charge-Feld mit Energie- und Adjungiertenkontrolle sowie E8-/Clock-Zuordnung |
| T3 | Kleiner gemeinsamer Rechenraum innerhalb einer Bank | Gemeinsamer physischer 3+1D-Ursprung |
| T4 | Vollständige innere Bilineare; korrekte Feldkanäle | Vollständiges chirales Maß mit dynamischen Eichfreiheitsgraden |
| T5 | Exakter lokaler Hamilton-Lanczos-Anfang | Kontrollierter relativistischer Kontinuums- und Streuungsgrenzfall |
| T6 | Expliziter Nachweis, dass die bisherigen Grunddaten g/Delta nicht auswählen | Physische Kopplungs-, Skalen- und Spektralzuordnung, einschließlich offener Neutrinofragen |
| T7 | Keine neue Schließung | Aus derselben Quelle erzeugter dynamischer Spin-2-Sektor und universelle Kopplung |
| T8 | Unterscheidung Startzustand, Grundzustand und Ausleseinstrument verschärft | Gemeinsame physische Präparation, Aufzeichnung und Zustandsauswahl |

Alle acht Tore bleiben offen. Die heutigen Ergebnisse schließen begrenzte
mathematische Fragen innerhalb des Programms, nicht diese physikalischen
Gesamtnachweise. Frühere RH-, Faktorisierungs- oder P-versus-NP-Grenzen
werden durch die endlichen Rechnungen ebenfalls nicht verändert. Der begrenzte
RH-Registerabgleich und seine Aktualitätsgrenze sind in Teil B dokumentiert;
ein vollständiger Neuaudit dieser Arbeitsfronten fand nicht statt.

## 10. Die drei nächsten entscheidenden Untersuchungen

1. **Den minimalen Ursprungsvertrag auswählen.** Teil B klassifiziert die
   kleinen symmetrieverträglichen Terme und trennt echte Erweiterungen von
   einem bloßen Wechsel der Bosonvariablen. Der Compiler muss diese Auswahl
   und die relativen Parameter begründen. Symmetrie allein tut das noch nicht.
2. **Die gemeinsame Schattenkarte am vorhandenen Tensor prüfen.** Derselbe
   Zustand und dieselben Operationen müssen die verschiedenen Ausleseansichten
   tragen. Gesucht sind ergänzende statt nur duplizierte Informationen, ein
   kontrollierter gemeinsamer Kern und Vorhersagen ohne nachträgliche Anpassung.
3. **Einen echten Eingriffstransfer und denselben Feldadapter konstruieren.**
   Eine aus der Quelle abgeleitete lokale Operation muss später die unbedingte
   Statistik eines anderen operational bestimmten Teils verändern. Selbst
   zeitabhängige Kreuzkorrelation bei Anfangswert null reicht nicht; Teil B
   enthält ein exaktes Gegenbeispiel. Dazu müssen Ladung, Kinetik und
   relativistische Feldzuordnung passen, bevor räumliche Skalierung trägt.

Die korrekte H-Kette mit Restschranke bleibt eine nützliche parallele
Rechenaufgabe. Die zehn bekannten Momente sind feste Gegenprüfungen. Sie
ersetzt aber nicht die jetzt vorrangige Ursprungs- und Kompositionsfrage.

## 11. Reproduktion und Veröffentlichung

Das Prüfpaket enthält sechs neue Python-Prüfer, die eingefrorenen Quellen,
die alte und neu wiederholte Kontraktion, Ergebnisdateien, Quellenmanifest
und die vollständige v1.6.6 als historische Basis. `replay.py` prüft alle
Pins, beide Python-Modi und die C++-Kontraktion. Die ausgelieferte ZIP wird
nach dem Entpacken erneut geprüft.

Die vollständige Hauptfassung, das kurze Änderungsdokument und die einfache
Erklärung werden gemeinsam versioniert direkt in Documents abgelegt, jeweils
als Markdown und PDF. Die PDF-Ausgaben werden zusätzlich auf Darstellung,
Textabdeckung und Seitenaufbau geprüft. Frühere Fassungen bleiben erhalten.
Es erfolgt keine Änderung der zentralen TOE-Abnahmemarker, kein Commit,
kein Push und keine externe Web-Veröffentlichung.

Der Statusleitfaden beeinflusst die Trennung zwischen mathematischer
Struktur, angenommenen Ressourcen und nachgewiesener Fähigkeit. Der
Debugging-Leitfaden führte zur ausdrücklichen Sicherung reell-ganzzahliger
Tensorwerte vor der Typumwandlung; keine Imaginärteile werden still verworfen.

### Schluss in einem Satz

**Die einfache Regel ist vorhanden; ihr erster verzweigter Zustandsbereich
und die richtige kleine Rechenkette sind jetzt genauer gelöst. Was noch
fehlt, ist die aus dem Ursprung folgende Auswahl und Ausführung dieses
Prozesses als dieselbe physikalische Welt.**


---

# Neue Vogelperspektive: derselbe Prozess in verschiedenen Ansichten

## B1. Was sich durch die drei weiteren Texte ändert

Die nachgereichten Texte werden als Vorschläge geprüft, nicht als bewiesene
Ergebnisse oder neue Arbeitsanweisungen übernommen. Die stärkste gemeinsame
Idee trägt: **Innere Identität, Zusammensetzung, Ort, Zeit und Auslese dürfen
nicht stillschweigend dasselbe Label erhalten.** Eine immer genauere Rechnung
innerhalb einer Bank ersetzt diese Verbindungen nicht. Die voranstehenden
lokalen Ergebnisse bleiben gültig; die fundamentale Priorität verschiebt
sich auf die gemeinsame Operations- und Kompositionsregel.

| Vorschlag | Prüfung und Konsequenz |
|---|---|
| Ort in Multiplizitäten statt in den 64 inneren Labels suchen | Sinnvolle Möglichkeit, aber Multiplizität beschreibt bereits chemische Umwandlung ohne Raum |
| Der große Kommutant könnte verborgenen Raum enthalten | Hamilton- und Symmetriekommutant sind verschieden; die Größe allein trägt diesen Schluss nicht |
| Den ganzen Z4-Ursprung statt nur den ladungserhaltenden Ausschnitt betrachten | Konkrete zusätzliche Terme existieren am selben W; ihre Verfügbarkeit ist noch nicht hergeleitet |
| Ladung +3 und Ladung -1 sind modulo vier gleich | Ein zusätzlicher Term kann sie dynamisch verbinden; die Operatoren sind nicht identisch |
| Zeitabhängige Kreuzantwort zeigt Transport | Im Allgemeinen falsch; unten steht ein exaktes Gegenbeispiel sogar bei Anfangskorrelation null |
| Mehrere Schatten könnten einen gemeinsamen Ursprung bestimmen | Möglich bei gemeinsamem Vertrag und ausreichender Unterscheidbarkeit; Übereinstimmung allein genügt nicht |
| Holografie könnte die fehlende Verbindung sein | Ein nativer isometrischer Kodierungsbaustein ist vorhanden; Raumgrenze, Schutz und gemeinsame Raumzeit fehlen |

Die zusätzlich eingefrorenen Texte heißen im Prüfpaket `multiplicity_z4.txt`,
`fundamental_reduction.txt` und `runtime_synthesis.txt`. Sie werden im
Hauptdokument vollständig angehängt. Die anschließende Schatten- und
Holografiefrage des Nutzers wurde durch eigene Rechnungen weiterverfolgt.

## B2. Noethers Frage: Welche Unterschiede kann die Dynamik überhaupt verändern?

Bei ungebrochener innerer Gruppe G zerfällt ein Zustandsraum als

\[
\mathcal H=\bigoplus_\lambda V_\lambda\otimes M_\lambda,
\qquad H=\bigoplus_\lambda I_{V_\lambda}\otimes h_\lambda,
\qquad \operatorname{End}_G(\mathcal H)
=\bigoplus_\lambda I_{V_\lambda}\otimes\operatorname{End}(M_\lambda).
\]

G-invariante Entwicklung darf die Kopien eines Typs verändern, nicht die
inneren Komponenten dieses Typs willkürlich auseinanderziehen. Das macht
Multiplizitäten zu einem möglichen Träger weiterer Dynamik. Es macht sie
noch nicht zu Orten. Schon die drei hellen N=3-Typen enthalten zwei Kopien:
einmal drei Fermionen, einmal einen Fermion plus einen Boson. Ihre jeweilige
Hamiltonmatrix lautet

\[
h_\lambda=\begin{pmatrix}0&g\sqrt\lambda\\g\sqrt\lambda&\Delta\end{pmatrix},
\qquad \lambda=7,10,12.
\]

Am Prüfpunkt g/Delta gleich 1/20 sind die maximalen Umwandlungswahrscheinlichkeiten
7/107, 1/11 und 3/28. Das ist echte symmetrieverträgliche Dynamik, zunächst
aber eine Veränderung der Zusammensetzung und kein Ortswechsel.

Wichtig ist die Richtung des Kommutanten: Im N=3-Sektor hat der Kommutant
der vollen inneren Gruppe die Dimension 16. Die viel größere Zahl
1444233216 betrifft den kleineren Kontrollsatz aus X und Bosonzahl.
Auf dem isolierten irreduziblen 64er-Pol ist der G-Kommutant sogar nur skalar,
während der Kommutant der dort skalaren Energie alle 64-mal-64-Matrizen
enthält. Die große Energiedegeneration ist kein Nachweis vieler Orte.

Für einen G-Singulett-Grundzustand und die ursprünglichen irreduziblen
Fermionoperatoren folgt aus Schurs Lemma

\[
C_{rs}(t)=\delta_{rs}\,c(t).
\]

Feste lineare Umbenennungen liefern lediglich einen Gramfaktor mal derselben
Zeitfunktion. Auch eine perfekte Kenntnis aller lokalen Spektrallinien würde
aus den 64 inneren Komponenten deshalb noch keine räumliche Anordnung machen.
Ein stationärer Grundzustand kann zeitabhängige Korrelationsfunktionen haben;
Nichtstationarität ist keine notwendige Voraussetzung dafür. Physische
Uhrenablesung und Zeitrichtung sind weitere Fragen.

## B3. Korrelation ist noch kein Eingriff: ein exakt gelöstes Gegenbeispiel

Zwei nicht miteinander wechselwirkende Qubits genügen:

\[
H=\tfrac12(Z_A+Z_B),\qquad
|\Omega\rangle=(|01\rangle+|10\rangle)/\sqrt2,
\qquad A=X_A,\quad B=Y_B.
\]

Der Zustand ist stationär. Trotzdem ist

\[
\langle\Omega|B e^{-itH}A|\Omega\rangle=\sin t.
\]

Die Kreuzkorrelation startet bei null und verändert sich mit der Zeit.
Es gibt dennoch keinerlei Signal von A nach B: Alle A-lokalen Operationen
kommutieren mit jedem zeitentwickelten B-lokalen Observablen. Für jedes
spurtreue lokale Quanteninstrument bleibt daher die unbedingte B-Statistik
unverändert. Eine Konditionierung auf ein Messergebnis in A wäre etwas anderes.

Der belastbare Übertragungstest ist stattdessen

\[
\delta_{A\to B}(t)=
\operatorname{tr}\!\left[B U_t\mathcal E_A(\rho)U_t^\dagger\right]
-\operatorname{tr}\!\left[B U_t\rho U_t^\dagger\right].
\]

A und B müssen zuerst als unabhängig adressierbare Teile definiert sein;
das Instrument muss verfügbar sein, ohne durch seine Definition schon B
anzusteuern. Erfolg bedeutet eine nichtverschwindende unbedingte Änderung
nach dem A-Eingriff. Die lineare Antwort misst entsprechend einen retardierten
Kommutator, nicht bloß eine Zweipunktkorrelation. Lieb-Robinson-Abschätzungen
können anschließend die Ausbreitung in einem bereits lokal gekoppelten
Modell begrenzen; sie erzeugen diese Lokalität oder drei Raumdimensionen
nicht von selbst. Siehe die Primärarbeit von
[Bravyi, Hastings und Verstraete](https://arxiv.org/abs/quant-ph/0603121).

Ein weiterer exakter Befund verhindert ein zu starkes Paritäts-No-go:
Der native Graph der 480 Fermionpaare verbindet alle 64 Moden. Eine
Vorzeichenumkehr auf einer Fermionteilmenge, bei unveränderten Bosonen,
erhält jede Kante genau dann, wenn sie trivial oder die globale Fermionparität
ist. Die binäre Inzidenzmatrix hat Rang 63. Zusätzliche unabhängige
Bankparitäten entstehen beim Kopieren von Banken; sie sind nicht als solche
ein Hindernis innerhalb der einen ursprünglichen Bank. Werden auch Bosonen
umgezeichnet, sind andere gemeinsame Gradierungen möglich.

## B4. Die einfachste fehlende Auswahl: Warum genau dieser Hamiltonoperator?

Die Z4-Idee besitzt einen präzisen Kern. Ein ganzzahliger, auf jedem Grad
konstanter Ladungslift mit neutralem Grad null müsste bei den entsprechenden
nichtverschwindenden Klammern erfüllen

\[
2q_1=q_2,\qquad q_1+q_3=0,\qquad 2q_3=q_2.
\]

Die Koeffizientenmatrix hat Determinante 4 und Rang drei. Über den ganzen
Zahlen bleibt nur q1=q2=q3=0; modulo vier gilt dagegen die gewohnte Belegung
1, 2, 3. Das verbietet nicht andere kontinuierliche Cartanladungen und beweist
nicht, dass der aktuelle Operator-Hamiltonian schon alle E8-Klammern realisiert.

Eine wörtliche Identifikation der Grad-eins-Labels mit primitiven CAR-
Vernichtern scheitert bereits an einem kleinen Beispiel: Die native
W-Spalte des Paares (0,1) ist null, aber
\([f_0,f_1]=2f_0f_1\ne0\). Die innere Lieklammer und die gewöhnliche
Operatoralgebra der Fermionfelder dürfen nicht gleichgesetzt werden.
Eine andere, zusammengesetzte E8-Realisierung wird dadurch nicht ausgeschlossen.

### B4.1 Zwei zusätzliche Terme am unveränderten Tensor

Der Bosonträger (10,6) besitzt eine symmetrische reelle invariante Paarung
eta. In der nativen Gewichtsbasis koppelt sie entgegengesetzte Spin-
Vektorgewichte und komplementäre Farbpaare. Es gilt eta Quadrat gleich eins.
Damit sind bereits

\[
B_+=\tfrac12\sum_{AB}b_A^\dagger\eta_{AB}b_B^\dagger,
\qquad
R_+=\sum_{AB}b_A^\dagger\eta_{AB}P_B^\dagger
\]

G-invariant. Bplus erzeugt zwei Bosonen, Rplus einen Boson und zwei Fermionen.
Beide ändern N um vier; beide erhalten N modulo vier. Die vollständige
Lie-Invarianz wurde an allen 45 plus 15 Generatoren überprüft, nicht nur
an den Cartanladungen. Rplus wirkt auf dem leeren Zustand nicht trivial:
Das Normquadrat beträgt exakt 480. Der quadratische Bosonpaarterm ist sogar
einfacher als der vorgeschlagene zusätzliche kubische Kanal.

Auf dem unveränderten Träger lautet die allgemeine G-invariante,
fermionparitätsgerade, normalgeordnete Hamiltonfamilie vom Grad höchstens drei

\[
H_{\rm ext}=c+\varepsilon N_f+\Delta N_b
+\kappa B_++\bar\kappa B_-
+g\sum_A b_A^\dagger P_A+\bar g\sum_A P_A^\dagger b_A
+\lambda R_++\bar\lambda R_-.
\]

Die Vollständigkeit gilt nur innerhalb dieser ausdrücklichen Polynomialklasse:
End(F) und End(B) haben jeweils einen Skalar, Sym hoch zwei von B einen
Skalar, und B tritt in Lambda hoch zwei von F genau einmal auf. Konkret
zerfällt letzterer Raum in (10,6), (126,6) und (120,10). Die SU(4)-Zentrumsregel
schließt die verbleibenden bosonisch-kubischen und gemischten
Besetzungs-Boson-Terme aus. Höhere Polynome, räumliche Kopien und neue
Feldträger sind damit nicht klassifiziert.

Für das native Modell hat das lineare System aller diagonalen Modenphasen
exakt neun unabhängige kontinuierliche Erhaltungen: die acht inneren Cartans
und N. Bei zusätzlichem nichtverschwindendem Rplus-Kanal oder Bosonpaar-Kanal
bleiben exakt acht. Die Ränge sind 115 beziehungsweise 116 auf 124 Moden;
explizite ganzzahlige Kerne und modulare Rangzertifikate beweisen sie.
Dies ist keine Behauptung, die volle nichtabelsche Gruppe schrumpfe auf acht
Dimensionen. Sie bleibt erhalten. Außerdem ist N modulo vier bereits die
Wirkung des SU(4)-Zentrums und keine neu hinzugewonnene unabhängige Symmetrie.

Für reelle Kopplungen und epsilon gleich null enthält die Fermiongleichung
nun zwei verschiedene Beiträge:

\[
[H_{\rm ext},f_r]=-gD_r-\lambda\widetilde\chi_r^\dagger,
\qquad D_r\sim bf^\dagger,\quad
\widetilde\chi_r^\dagger\sim b^\dagger\eta f^\dagger.
\]

Sie haben N-Ladungen -1 und +3. Eine Dynamik kann diese Kanäle bei bloßer
Z4-Erhaltung verbinden, ohne die Operatoren oder ihre Referenzzustände
fälschlich gleichzusetzen. **Zulässig ist aber noch nicht aus dem Compiler
abgeleitet.** Die Grundzustands- und Polschranken des unveränderten Modells
gelten für diese Erweiterung nicht ungeprüft weiter.

Auch ein mu-N-Term bleibt G- und Z4-invariant. Bereits der Zwei-Zustandsblock
aus leerem Zustand und einer normierten Quartetterzeugung im kleinen Modell
zeigt

\[
H+\mu N=\begin{pmatrix}0&\lambda\\\lambda&\Delta+4\mu\end{pmatrix}.
\]

Seine niedrigere Eigenenergie hängt von mu ab. Der Übergang zu Z4 allein
wählt also weder ein chemisches Potential noch einen eindeutigen physikalischen
Grundzustand aus. Für Delta größer als Betrag kappa ist die bosonische
Quadratik positiv; die linearen Bosonkopplungen an beschränkte Fermionoperatoren
lassen sich relativ dazu abschätzen. Das gibt eine untere Energieschranke,
aber noch keinen neuen eindeutigen Grundzustandssatz.

### B4.2 Eine weitere Vereinfachung: neue Dynamik oder andere Teilchenvariablen?

Manche scheinbaren Erweiterungen beschreiben nur andere Bosonvariablen.
Auf der reellen, phasengleichen Teilfamilie setze man

\[
b=c\cosh r+\eta c^\dagger\sinh r.
\]

Dies ist eine G-verträgliche kanonische Bogoliubov-Transformation. Sie ergibt

\[
\Delta'=\Delta\cosh2r+\kappa\sinh2r,\quad
\kappa'=\Delta\sinh2r+\kappa\cosh2r,
\]
\[
g'=g\cosh r+\lambda\sinh r,\quad
\lambda'=g\sinh r+\lambda\cosh r.
\]

Die additive Konstante ist 30 mal (Delta prime minus Delta). Bei g Quadrat
größer lambda Quadrat verschwinden kappa prime und lambda prime gemeinsam
genau dann, wenn

\[
\mathcal I=\kappa(g^2+\lambda^2)-2\Delta g\lambda=0.
\]

Beispiel: Delta=1, kappa=4/5, g=2, lambda=1 und tanh r=-1/2 ergeben
Delta prime=3/5, g prime=Wurzel 3, kappa prime=lambda prime=0.
Obwohl die alte Zahl N nicht erhalten ist, gibt es dann die verborgene
kontinuierliche Erhaltung Nf plus zweimal Nc. Daher wäre auch die Folgerung
„N ist gebrochen, also ist das Fundament nur Z4“ ohne Prüfung zu schnell.
Für I ungleich null ist nur diese uniforme kanonische Reduktion ausgeschlossen,
nicht jede denkbare nichtlineare verborgene Symmetrie.

Der sehr einfache reelle Quadraturansatz lambda=g bei kappa=0 ist dagegen
nicht durch eine endliche solche Transformation auf den nativen Ansatz
reduzierbar. Er ist ein prüfbarer Kandidat, kein hergeleitetes Naturgesetz.
Ein weiterer Herkunftstest ist besonders schlicht: Bei freiem
H0=epsilon Nf+Delta Nb haben die beiden kubischen Terme die Frequenzen
Delta minus 2 epsilon und Delta plus 2 epsilon. Am verwendeten epsilon=0
gibt es keine schnelle gegen langsame Frequenz, die das Weglassen des zweiten
Kanals durch eine Rotating-Wave-Näherung rechtfertigen würde. Ein exaktes
U(1)-Prinzip könnte das dennoch rechtfertigen; dieses Prinzip wäre dann
auszuweisen und abzuleiten.

## B5. Holografie und Schatten: die konkrete native Verbindung

### B5.1 Ein Kodierer ist bereits vorhanden

Der vorhandene, frisch geprüfte Tensor erfüllt WW dagger gleich 8 I60.
Daher ist

\[
V=W^\dagger/\sqrt8:\ \mathbb C^{60}\longrightarrow\Lambda^2\mathbb C^{64},
\qquad V^\dagger V=I_{60},\quad
\Pi=VV^\dagger=W^\dagger W/8
\]

eine exakte Isometrie mit einem Rang-60-Projektor Pi. Ein 60-dimensionaler
logischer Zustand kann verlustfrei als kohärente Überlagerung von
Fermionpaaren dargestellt werden. Die andere Richtung sieht aber nicht den
ganzen 2016-dimensionalen Paarraum: Ihr Kern hat Dimension 1956.
Diese „dunklen“ Richtungen sind nicht deshalb generell unphysikalisch;
sie sind für genau diese Abbildung unsichtbar.

Die beiden Ansichten sind durch W also bereits verbunden. Die native
N=2-Dynamik im hellen Paar-plus-Boson-Bereich ist sogar exakt

\[
H_{N=2,\mathrm{hell}}=
\begin{pmatrix}0&\sqrt8 g\\\sqrt8 g&\Delta\end{pmatrix}\otimes I_{60}.
\]

Sie wandelt die Kodierungsform um; am Prüfpunkt erreicht die entsprechende
Übergangswahrscheinlichkeit höchstens 2/27. Der nur in die Paarseite
eingebettete Code ist bei g ungleich null kein invarianter H-Unterraum.
Dieser kleine gemeinsame dynamische Träger ist ein positiver Befund. Er
ist N=2, nicht der native N=64-Grundzustand und nicht dessen geladener Pol.
Insbesondere ist er noch kein Transport durch physikalischen Raum.

### B5.2 Warum das noch kein holografischer Fehlerkorrekturcode ist

Für jeden der 64 Fermionmoden wurde die logische Kompression seiner
Besetzungsmessung berechnet:

\[
V^\dagger n_rV\quad\hbox{hat Spektrum}\quad
0\ (45\text{-fach}),\quad 1/8\ (15\text{-fach}).
\]

Das Resultat ist nicht skalar. Die Umgebung kann daher schon durch Ablesen
einer einzigen verlorenen Mode etwas über den logischen Zustand erfahren.
Die notwendige Fehlerkorrekturbedingung für die vollständige 60er-Codemenge
ist verletzt: Der Code korrigiert nicht die beliebige Löschung dieser einen
Mode. Fermionparität ändert dieses Besetzungsargument nicht, denn n_r ist gerade.
Kleinere geeignete Untercodes oder ein aus nativen Operationen erzeugtes
größeres Kodierungsnetz sind dadurch nicht ausgeschlossen, aber noch nicht
konstruiert. Bloßes Aneinanderhängen desselben Tensors garantiert keinen Code.

In etablierten holografischen Spielzeugmodellen sind isometrische Kodierung,
Rekonstruktion logischer Operationen aus verschiedenen Randteilen und
Fehlerkorrektur genau kontrollierte Eigenschaften. Das ist ein hilfreiches
Prüfschema, keine direkte Identifikation mit TFPT. Siehe
[Pastawski, Yoshida, Harlow und Preskill](https://arxiv.org/abs/1503.06237).
Die Rekonstruktion aus einem Teilrand ist auch in der AdS/CFT-Arbeit von
[Dong, Harlow und Wall](https://arxiv.org/abs/1601.05416) an konkrete
Quanteninformations- und geometrische Voraussetzungen gebunden.
Diese Voraussetzungen wurden für TFPT nicht nachgewiesen.

### B5.3 Was mehrere Schatten gemeinsam eindeutig machen können

Seien Ri festgelegte Mess- oder Reduktionsabbildungen eines gemeinsamen
Zustands rho. Für eine endliche, nicht eingeschränkte Zustandsklasse sind
alle Zustände aus den Schatten Ri(rho) genau dann unterscheidbar, wenn
auf den hermiteschen spurlosen Differenzen gilt

\[
\bigcap_i\ker R_i=\{0\}.
\]

Das ist das einfache gemeinsame-Kern-Kriterium. Anschaulich: Was eine
Ansicht nicht sieht, muss eine andere sehen. Zwei Qubitansichten auf (x,z)
und (y,z) genügen gemeinsam zur Bloch-Rekonstruktion, jede für sich nicht.
Zweimal dieselbe Ansicht auf (x,z) genügt weiterhin nicht. Das gilt ebenso
für zwei Theorieberichte, deren Übereinstimmung bereits aus denselben
eingesetzten Annahmen stammt: Sie liefern keine zweite unabhängige Messung.

Drei exakt nachgerechnete Grenzen sind wesentlich:

1. Die orthogonalen Zustände (000 plus 111)/Wurzel 2 und
   (000 minus 111)/Wurzel 2 haben dieselben reduzierten Zustände auf
   sämtlichen echten Teilmengen der drei Qubits. Eine gemeinsame
   phasensensitive XXX-Messung unterscheidet sie mit Erwartungswert +1 oder -1.
   Auch sehr viele lokale Schatten können also eine globale Phase übersehen.
2. Paarweise passende Überschneidungen garantieren nicht einmal einen
   gemeinsamen Ursprung. Drei binäre Variablen können nicht paarweise
   ausnahmslos verschieden sein. Jede einzelne perfekte Antikorrelation
   besitzt aber dieselben gleichverteilten Einzelmarginalen. Gemeint ist
   hier ein gemeinsames klassisches Tripel, nicht eine Behauptung gegen
   kontextuelle Quantenexperimente.
3. Selbst die vollständige Antwort einer Referenz bestimmt keinen völlig
   entkoppelten dunklen Zusatzsektor. H und H direkt plus K besitzen vom
   Startvektor (F,0) aus dieselben Energiemomente und dieselbe Zeitantwort.
   Ein exaktes kleines Matrixbeispiel prüft diesen Sachverhalt.

Das erreichbare Ziel ist daher zunächst der **kleinste gemeinsame
beobachtbare Prozess**, nicht ein aus endlichen Schatten bewiesener
einzigartiger ontologischer Innenraum. Zwei Historien gelten operational
als gleich, wenn alle verfügbaren künftigen Eingriffs- und Auslesefolgen
dieselben Wahrscheinlichkeiten liefern. Das ist eine eindeutige
Unterscheidungsregel für gegebenes Verhalten; sie garantiert weder eine
eindeutige Hilbertraumdarstellung noch von selbst eine einfache Geometrie.

### B5.4 Die drei Wände müssen unterschiedlich geprüft werden

| Gemeinte Wand | Was sie gegenwärtig bedeutet | Welcher Anschluss fehlt |
|---|---|---|
| Universalraum | Grenze zwischen gemeinsamem Operatorobjekt und seinen reduzierten Ansichten | Ein gemeinsamer verfügbarer Operationssatz, Zustand und Rekonstruktionsvertrag |
| TFPT | Grenze zwischen interner Compilerstruktur und physikalischer Realisierung | Herleitung der Ausführung, relativer Parameter und operationaler Teilung |
| Beobachtete Realität | Endlicher Zugang über Messungen, Präparationen und Korrelationen | Ein quantitatives, nicht nachträglich angepasstes Feld- und Messwörterbuch |

Diese Erkenntnisgrenzen sind nicht schon drei bewiesene physikalische
Holografieschirme. Ein kosmologischer Horizont, ein Code-Rand und eine offene
mathematische Beweispflicht sind verschiedene Dinge. Ebenso sind
Universalraum und TFPT Kandidatenbeschreibungen der Realität, nicht bereits
drei experimentell etablierte wechselwirkende Welten.

Eine stärkere holografische Deutung müsste eine einzige Kodierung mit
Zuständen, Operationen und Zeitentwicklung verbinden. Auf einem invarianten
Codesektor wäre etwa V dagger V=I und Hrand V=V Hin eine passende
Intertwining-Bedingung. Bei nichtinvarianten reduzierten Ansichten muss die
entstehende Erinnerung mitgeführt werden; autonome reduzierte Dynamik darf
nicht einfach vorausgesetzt werden. Zusätzlich braucht es eine Bedeutung
von Randteilen, kontrollierte Rekonstruktion und eine skalierende Geometrie.

## B6. Die einfachste neue Arbeitsrichtung und ihre Abnahmekriterien

Der plausible übersehene Punkt ist kein weiterer großer Tensor:
**Wir brauchen die gemeinsame Regel, die festlegt, welche Operationen,
Teilchenvariablen und Ansichten tatsächlich dieselbe Ausführung beschreiben.**
Noethers Symmetrieprüfung sagt, was erhalten bleibt. Die Schattenprüfung sagt,
was überhaupt unterscheidbar ist. Der Eingriffstest sagt, was etwas anderes
beeinflussen kann. Zusammen sind diese drei kleinen Fragen strenger und
informativer als weitere isolierte Zahlenübereinstimmungen.

1. **Den minimalen Ursprungsvertrag auswählen.** Den tatsächlichen Compiler
   auf den nativen kubischen Term, den zweiten kubischen Kanal und den
   quadratischen Paarterm prüfen. Die vollständige kleine Familie und der
   Bogoliubov-Test verhindern, dass derselbe Prozess mehrfach gezählt wird.
   Erfolg ist eine Ableitung oder ein präziser Ausschluss samt relativen
   Parametern, nicht nur die Feststellung erlaubter Symmetrie.
2. **Die Schattenkarte am vorhandenen W aufbauen.** Für denselben Vertrag
   Präparationen, Aufzeichnungen und kontrollierte Mehrzeitantworten in den
   verschiedenen Ansichten auflisten. Gemeinsam unsichtbare Richtungen und
   unverträgliche Überlappungen berechnen. Aus einem Teil der Daten eine
   Aussage bestimmen, die eine andere Ansicht ohne Nachjustierung testet.
   Der jetzt bewiesene Rang-60-Code und sein Einmoden-Leck sind Ausgangsdaten,
   kein Anlass, Raum oder perfekte Fehlerkorrektur bereits anzunehmen.
3. **Daraus einen gemeinsamen kausalen Teilträger gewinnen.** Eine verfügbare
   Operation muss die unbedingte Statistik eines anderen operational
   bestimmten Teils verändern. Derselbe Träger muss das relativistische
   Feldwörterbuch tragen. Erst dann sind Skalierung, chirales Maß und ein
   Spin-2-Sektor belastbare nächste Rechnungen.

Die lokale Lanczos-Fortsetzung bleibt als kontrolliertes Diagnoseinstrument
nützlich, steht aber nicht mehr an erster Stelle der fundamentalen Suche.
Die drei Schritte ersetzen keine einzelnen T1-T8-Nachweise. Auch eine
erfolgreiche endliche Kodierung würde RH, effiziente Faktorisierung oder
P-versus-NP nicht automatisch lösen.

Der RH-Absatz der Eingabe enthält keine neue vollständige arithmetische
Beweiskonstruktion. Das vorhandene Forschungsregister wurde begrenzt
abgeglichen; sein Aktualitätslauf scheitert derzeit an einer nicht verfügbaren
historischen Quelle beziehungsweise Quellen-/Review-Drift. Bestehende
endliche Determinantsonden sind ausdrücklich Diagnosemodelle. Es wurde
kein neuer RH-Beweis, kein umfassender RH-Neulauf und keine Erneuerung
der entsprechenden Vertrauensmarker behauptet.

**Bilanz:** Ein gemeinsamer Kodierungsbaustein ist schon da; außerdem sind
die minimalen symmetrieverträglichen Dynamiken und zwei wichtige
Verwechslungen jetzt wesentlich schärfer bestimmt. Die vollständige
universelle physikalische Lösung bleibt offen. Der nächste Schritt ist
kleiner und konkreter geworden: dieselbe Ausführung durch mehrere
kalibrierte, dynamisch konsistente Ansichten rekonstruieren und testen.

## B7. Abgleich des zuletzt eingesandten Berichts v1.6.3

Der sechste Text dieser Runde, „Operationssatz, nativer Grundzustand und
Feldwörterbuch“, enthält überwiegend bereits berücksichtigte Befunde:
die Kommutantenleiter, das Lochbild, die Normen der ersten Stufen, den
nichtverschwindenden Seitenzweig und den verschwindenden Weyl-Skalarkanal.
Seine zweite vorgeschlagene Folgeaufgabe wurde inzwischen wesentlich
weitergeführt: Alle vier Zwei-Boson-Singuletts sind konstruiert und der
richtige H-Lanczos-Anfang ist fünf Glieder weit bestimmt.

Vier Präzisierungen verhindern eine Übernahme veralteter Schlüsse:

1. **Sieben und sechzehn sind verschiedene Kommutanten.** Sieben gilt
   für volle innere Gruppe zusammen mit X und Nb; sechzehn für die Gruppe
   allein. Die drei hellen inneren Typen kommen auf beiden Seiten der
   Umwandlung vor. Einzelne Tabellenzeilen sind multiplizitätsfrei, der
   ganze N=3-Sektor aber nicht. Der Schluss vom nichtskalaren Clock auf
   eine äußere, nicht zusammenhängende Symmetrie ist weiterhin falsch.
2. **Eine kleine Zweignorm beweist keine globale Konvergenz.** Der
   genannte Defekt 2,90 mal 10 hoch -5 betrifft eine bestimmte Kontraktion.
   Die höhere Bosonstufe ist weiterhin gekoppelt. „Numerisch fast allein
   durch die Normen lösbar“ und „vernachlässigbar“ sind ohne Restschranke
   zu stark. Auch Zh plus Zadd gleich eins ist eine Summenregel, keine
   Bestimmung sämtlicher Spektrallinien. Ritz-Erwartungswerte bleiben
   Erwartungswerte des Ritz-Zustands, nicht automatisch von Omega.
3. **Der Feldschluss ist ansatzabhängig.** Der angegebene Fünfzyklus
   (16,45,0,30,37) wurde frisch am W überprüft. Damit ist eine einzige
   binäre Chiralitätsbelegung der primitiven Labels mit entgegengesetzter
   Händigkeit auf jeder Kante unmöglich. Das verbietet kein allgemeines
   Dirac-Wörterbuch mit erweiterten Trägern, Ableitungen oder zusammengesetzten
   Feldern. Der Tensorfeldkanal ist unter dem angegebenen engen Ansatz
   sinnvoll, nicht schon der universell einzige physikalische Feldtyp.
4. **Der gespeicherte Rechnerstand ist älter als der Text.** Die lokal
   zugehörige Datei `native_ground_state.json` hat einen anderen Checkerhash
   als das aktuelle Programm. Ihr gespeichertes w2-Normquadrat ist um
   229 Quadrat gegenüber der physikalischen Norm skaliert. Das aktuelle
   Programm enthält bereits die richtige Entskalierung; die alte Datei
   ist also kein aktueller Replaynachweis. Sie meldet außerdem
   `norms_by_traces_used=false` und Ritz-Tiefe drei. Die im Text erwähnte
   Datei `norms_by_traces.json` und das dortige Replaymanifest waren bei
   dieser Prüfung nicht vorhanden. Diese Beobachtung schließt ein
   Resultat an anderem Ort nicht aus, liefert hier aber keines.

Daher wird insbesondere die Behauptung, nu4 sei in dieser Quelle auf zwei
unabhängigen Wegen vollständig reproduziert, nicht übernommen. Der Text
selbst bezeichnet nu4 zugleich als „nur Spurnetzwerk“ und beschreibt den
Brute-Force-Abgleich nur bis nu3. Der frühere gepinnte exakte nu4-Eingang
unserer eigenen Rechnung bleibt davon getrennt und wurde nicht als neue
Enumeration ausgegeben. Ein fertig berechnetes nu5 wird aus dem vorhandenen
Programm mit `MAX_N=5` nicht abgeleitet; eine Einstellung ist kein Ergebnis.

**Die interessante verbleibende Richtung ist die Spurnetzwerk-Methode.**
Sie kann Normen durch Kontraktionen des vorhandenen Tensors berechnen,
statt alle Vielteilchenamplituden zu speichern. Zur fundamentalen
Vereinfachung wird sie erst dann, wenn sie auch gemischte H-Momente,
Seitenzweige und kontrollierte Mehrzeitantworten liefert. Der konkrete
nächste Test ist daher kein bloßer weiterer Normwert: Eine zweite kleine
Kontraktionsrechnung soll die schon exakt bekannten zehn H-Momente
reproduzieren und dann mindestens ein noch nicht bekanntes gemischtes
Matrixelement samt Fehlerkontrolle bestimmen. Diese Methode lässt sich
mit der Schattenkarte verbinden, ersetzt aber keine native Operation.

Das Prüfpaket bewahrt neben dem Text die beiden widersprechenden
Programmstempel und das vorhandene Spurnetzwerkprogramm. Diese fremden
Dateien wurden nicht verändert oder als vollständig neu ausgeführt ausgegeben.


---

# Historischer Anhang: vollständige Fassung v1.6.6

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

# TFPT / Universalraum: Clock, gemeinsame Quelle und tatsächlicher Transport

## Konsolidierung und eigene Forschungsfortsetzung v1.6.6 - 15. September 2026

**Ergebnis:** Der dokumentierte endliche Clock ist jetzt ausdrücklich als
Element der vorhandenen inneren Spin(10)-Symmetrie konstruiert. Dadurch lässt
sich die bislang offene gemeinsame Clock-/Casimir-Auslesung exakt bestimmen.
Daneben wurde ein kleiner, echter Vierzustandskanal der ursprünglichen
Paarwechselwirkung gefunden, der nach Zulassung eines Bosonmischers eine
Fermionenmarke überträgt. Die Herkunft dieses Mischers ist nicht bewiesen.

Der neue Universalraum-Text enthält eine sinnvolle Suchrichtung - gemeinsame
Quelle statt vorab unabhängiger Banken -, aber Überlappung allein erzeugt
weder Transport noch Raumzeit, Eichkrümmung oder die arithmetische Spur.
Mehrere seiner vermeintlich automatischen Übergänge werden hier präzisiert.

Diese Revision integriert **drei neue Nutzertexte**, die unabhängigen
parallelen Prüfungen und eigene neue Herleitungen. Die vollständige frühere
Konsolidierung v1.6.5 einschließlich v1.6.4 bleibt im historischen Anhang
erhalten. Das ist eine aktualisierte Forschungsfassung in Markdown mit
kurzem Änderungsdokument und einfacher Erklärung; keine behauptete neue
PDF-/Web-Publikation oder vollständige Theory of Everything.

### Leseschlüssel

- **Exakt:** Identität oder mathematische Folgerung im angegebenen Modell.
- **Numerisch:** berechneter Näherungswert, ohne zertifizierte Einschließung.
- **Bedingt:** exakter Satz erst nach ausdrücklich zusätzlicher Ressource.
- **Offen:** fehlende Herleitung oder physikalische Identifikation.

Eine grüne Prüfung ersetzt weder die Voraussetzungen eines Satzes noch eine
ausführbare Operation. Assoziative Algebradimension, dynamische
Kontrollierbarkeit und physische Verfügbarkeit werden getrennt geführt.

## 1. Die unveränderte gemeinsame Grundlage

Mit 64 Fermionmoden, 60 Bosonmoden und demselben gepinnten Tensor gilt

\[
H_{\rm nat}=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
\qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad N=N_f+2N_b.
\]

W besitzt 480 Einträge ±1, acht disjunkte Paare je Zeile, und
`WW†=8 I60`. Die Fermionmarkierung ist `16⊗4`, die Bosonmarkierung `10⊗6`.
Spin(10)×SU(4) ist zunächst eine **innere** Quellsymmetrie, keine bereits
hergeleitete Raumzeit-Lorentzgruppe.

Der frühere native Satz bleibt unverändert maßgeblich: Für Δ>0 und
`0<|g|/Δ≤1/20` hat dieser μ=0-Vertrag einen eindeutigen globalen Grundzustand
Ω bei N=64. Am Prüfpunkt `g/Δ=1/20` gelten unter anderem

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad 0.842846<\langle N_b\rangle_\Omega<1.245656.
\]

Die isolierte niedrige Entnahmelinie im N=63-Sektor hat weiterhin die
bewiesenen Schranken aus v1.6.4/v1.6.5:

\[
0.007737\Delta<\epsilon<0.039079764\Delta,
\qquad
Z_{\rm low}>\frac{40912436089}{46487375000}>0.88007628.
\]

Z bezieht sich auf das gesamte normierte Fermionspektralgewicht pro Mode.
Die gesamte Entnahmenorm ist dagegen
`ν=<f_r†f_r>=1-<Nb>/32`. Die beiden Größen sind nicht austauschbar.
Der Pol ist eine wohldefinierte isolierte Eigenlinie dieses endlichen
Modenmodells; seine relativistische Teilchen-, Massen- oder räumliche
Propagationsdeutung ist eine weitere Aufgabe.

Der vollständige bedingte Zwei-Banken-Satz aus v1.6.5 bleibt erhalten:
mit deklariertem Fermionlink und Rotorvertrag gelingt der reine niedrige
Transfer mit Wahrscheinlichkeit >99,267 %, die unfiltrierte ursprüngliche
Entnahme mit >89,726 %. Der Link war und ist **zusätzlich vorausgesetzt**.
Die neuen Vierzustandszahlen unten gehören zu einem anderen Vertrag und
ersetzen diese Ergebnisse nicht.

## 2. Quellenprüfung der beiden neuen Ergebnisrunden

### 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-,
Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch
reproduziert. Darunter befinden sich neun wörtliche `need(True, ...)`-Guards
mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als
neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu;
Abschnitt 3 ersetzt sie durch eine explizite Konstruktion.

Im gesamten N=3-Raum gilt die Zerlegung:

| Typ | irreduzible Dimension | Multiplizität | Spin-Casimir | Farb-Casimir |
|---|---:|---:|---:|---:|
| (1200,20) | 24000 | 1 | 141/4 | 39/4 |
| (560,20′) | 11200 | 1 | **117/4** | 63/4 |
| (672,4̄) | 2688 | 1 | 165/4 | 15/4 |
| (144,20) | 2880 | 2 | 85/4 | 39/4 |
| (144,4̄) | 576 | 2 | 85/4 | 15/4 |
| (16̄,20) | 320 | 2 | 45/4 | 39/4 |
| (16̄,4̄) | 64 | 1 | 45/4 | 15/4 |

Die gewichtete Gesamtdimension ist 45504. Nur die getrennten Teile Λ³64 und
60⊗64 sind jeweils multiplizitätsfrei, nicht ihre direkte Summe. Die drei
dunklen Typen besitzen alle Gesamtcasimir 45, werden aber bereits durch
**einen** getrennten Casimir unterschieden.

Eine unabhängige rationale Rechnung auf den kleinen Multiplizitätsräumen
liefert für die jeweils **gewährten** Operationen:

| Operationsvertrag | komplexe assoziative Algebradimension |
|---|---:|
| Ein fixes H=Nb+X/20 | 8 |
| X und Nb unabhängig | 14 |
| Zusätzlich ein dunkler Isotypieprojektor | 15 |
| Zusätzlich ein getrennter Casimir | 16 |
| Zusätzlich nur Gesamtcasimir | 14 |

Somit gibt es keine universelle binäre Frage „alle Symmetriegriffe oder gar
kein Fortschritt“. Die Dimension 15 ist ein konkretes Gegenbeispiel.
Die vollständige Gruppen-Generatoralgebra hat mit X,Nb die Dimension
743583744 und Kommutantdimension 7. Sie ist unter Gruppenkonjugation
**stabil**, aber nicht punktweise invariant. Sieben ist kein universeller
Boden für beliebige symmetriestabile Algebren: End(H) wäre ebenfalls stabil
und hätte einen eindimensionalen Kommutanten. Keine dieser Zahlen beweist,
dass die zugehörigen Operationen im Compiler ausführbar sind.

### 2.2 Der Grundzustandsbericht enthält einen Versionskonflikt

Der neue Text hat die Nichtschlussnorm bereits korrigiert, das danebenliegende
`native_ground_state.json` stammt jedoch von einer älteren Codefassung. Sein
als PASS markierter Wert ist um `229²` zu groß; die dortige relative
orthogonale Norm ist sogar größer als eins. Der daraus berechnete Ritzwert
−1,18826198 wird **nicht** übernommen.

Eine neue direkte ganzzahlige Kontraktion umgeht die 15,25 Millionen
Komponenten von v₃. Sie berechnet `u=T T†v₂` auf 293280 nichtverschwindenden
Komponenten und bestätigt exakt

\[
\|u\|^2=752194252800,\quad
\langle v_2,u\rangle=575078400,\quad
w_2=u-\frac{299520}{229}v_2,
\quad\|w_2\|^2=\frac{5001523200}{229}>0.
\]

Der eine Vektor je Bosonlage schließt daher nicht. w₂ ist ein zweiter
Singulettvektor derselben Lage. Für die kleine vier- bzw. fünfdimensionale
Ritzmatrix ergeben sich bei g/Δ=1/20 **numerisch**

\[
E_{R,4}/\Delta=-1.0942308394409612,
\qquad E_{R,5}/\Delta=-1.0942318710142458.
\]

Die zusätzliche w₂-Richtung ändert diese Näherung tatsächlich erst um etwa
10⁻⁶. Das bedeutet **keine** Konvergenz zum wahren Grundzustand: Beide Werte
liegen noch über dessen bereits bewiesener Obergrenze.

Die neue einfache Restformel zeigt die Ursache. Für den normierten
Vier-Vektor-Ritzeigenzustand mit letzter Komponente c₃ gilt

\[
\|(H-E_R)\psi_3\|^2
=g^2|c_3|^2\frac{\nu_4+\|w_2\|^2}{\nu_3}.
\]

Mit dem früher geprüften vierten Moment ist die Restnorm numerisch rund
0,373063 Δ. Der kleine w₂-Zweig trägt weniger als 23 Millionstel des
quadrierten Restes; die ausgelassene v₄-Richtung dominiert. Die neuen
Zahlen `Zh≈0,9737` und `εh≈0,031Δ` gehören ebenfalls zur Ritz-Näherung:
Gesamtentnahmenorm und erstes Moment, nicht neu bestimmte Polgrößen auf Ω.

Die Suche nach `E<−1,2Δ` oder `E<−1,1625Δ` wäre sogar mit der bestehenden
unteren Schranke unvereinbar. Die schwächere neue Beweismethode öffnet den
bereits geschlossenen nativen Grundzustandssatz nicht wieder.

## 3. Neuer exakter Anschluss: Der Clock liegt bereits in Spin(10)

### 3.1 Ausgangspunkt ist der tatsächliche Quell-Clock

Der gepinnte endliche Compilerpräfix liefert auf fünf Hilfsachsen

\[
p=(0\mapsto2,\ 1\mapsto0,\ 2\mapsto1,\ 3\mapsto4,\ 4\mapsto3),
\qquad\det p=-1.
\]

Seine vorzeichenrichtige Exteriorhebung auf dem geraden 5-Moden-Hilfsfockraum
ist Γ(p)|even. Auf den nativen Fermionen ist `GF=Γ(p)|even⊗I4`; auf den
Bosonen ist `GB=(-P10)⊗I6`, wobei P10 beide Fünfergruppen permutiert.
Diese Darstellung wird aus dem vorhandenen Clockpräfix erneut extrahiert,
nicht aufgrund passender Eigenwerte ausgewählt.

### 3.2 Ein ausdrückliches Spinwort

Auf dem 32-dimensionalen Hilfsfockraum seien

\[
\gamma_j=a_j+a_j^\dagger,\qquad
\gamma_{j+5}=i(a_j^\dagger-a_j),\qquad 0\le j<5,
\]

und Π dessen Fermionparität. Setze

\[
\Omega_{10}=\gamma_0\gamma_1\cdots\gamma_9=i\Pi,
\qquad
R_{ab}=\frac{(\gamma_a-\gamma_b)(\gamma_{a+5}-\gamma_{b+5})}{2}.
\]

R_ab ist das Produkt zweier reeller Einheitsvektoren der Cliffordalgebra,
also ein Spin(10)-Element. Direkt gilt
`R_ab=i Γ((ab))`. Da `p=(01)(02)(34)` mit rechts zuerst angewandter Permutation,
folgt

\[
\boxed{S=\Omega_{10}R_{01}R_{02}R_{34}=\Pi\Gamma(p)\in\mathrm{Spin}(10).}
\]

S ist ein Produkt von 16 reellen Clifford-Einheitsvektoren. Die Matrixprüfung
bestätigt ohne Rundungstoleranzen

\[
S_{even}=\Gamma(p)_{even},\qquad S_{odd}=-\Gamma(p)_{odd},
\qquad S\gamma_jS^\dagger=-\gamma_{p(j)}
\]

mit entsprechender Fortsetzung auf die zweite Fünfergruppe. Damit stimmen
**beide nativen Darstellungen** und die ursprüngliche Kopplung überein:

\[
G_F=S_{even}\otimes I_4,\qquad
G_B=(-P_{10})\otimes I_6,\qquad
W\Lambda^2G_F=G_BW.
\]

S hat Ordnung sechs. Die Konjugation aller 45 Spin-Erzeuger und die
Kommutation mit allen 15 Farb-Erzeugern wurden zusätzlich direkt geprüft.
Die Aussage ist stärker und präziser als ein lediglich behaupteter
Normalisatorsatz.

**Bedeutung:** Der dokumentierte Clock und die innere Spin-Symmetrie brauchen
hier keine getrennten zusätzlichen mathematischen Träger. Es handelt sich
um einen konkreten endlichen Schritt derselben Darstellung. Daraus folgen
aber weder kontinuierliche Spin-Kontrollen noch die Identifikation des
Clocks mit Hamiltonzeit. Die Hilfs-Cliffordachsen sind nicht bereits fünf
Raumrichtungen.

## 4. Clock und getrennte Casimire lassen sich gemeinsam auslesen

Weil G aus Spin(10) stammt und auf SU(4) trivial wirkt, kommutiert es mit
beiden getrennten Casimiren, auch auf ihren Fockhebungen. Die Frage aus dem
neuen Text ist damit auf algebraischer Ebene beantwortet.

Die exakten Charakterfolgen von S_even, S_odd und dem Vektor sind

\[
(16,0,4,0,4,0),\quad(16,0,4,0,4,0),\quad(10,0,4,-6,4,0).
\]

Die schon unabhängig nachgerechneten Zerlegungen
`Sym³16=672+144`, `Λ³16=560`, `S21(16)=1200+144+16̄` und
`10⊗16=144+16̄` bestimmen die Charaktere der sieben Typen. Die diskrete
Fourierinversion erfolgt exakt in Z[ζ6], nicht durch gerundete komplexe
Eigenwerte. Für die drei zuvor gemeinsam dunklen Räume ergibt sich:

| Dunkler Typ | Phase 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| (1200,20) | 4000 | 4000 | 4000 | 4000 | 4000 | 4000 |
| (560,20′) | 1920 | 1840 | 1840 | 1920 | 1840 | 1840 |
| (672,4̄) | 464 | 440 | 440 | 464 | 440 | 440 |
| Summe, bisherige Clock-Auslesung | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |

Ein separater Casimir trennt jede der sechs dunklen Clockzellen in genau
drei Teile. Die hellen Zweier-Multiplizitätsräume bleiben erhalten. Daraus
folgt im N=3-Sektor

\[
\boxed{\dim\operatorname{Alg}^*(X,N_b,G,C_S)=96,}
\qquad
\boxed{\dim\operatorname{Alg}^*(X,N_b,G,C_S)'=119597824.}
\]

Zum Vergleich: ohne C_S sind es 84 und 240742144. C_C kann C_S ersetzen.
Die Lagrangeprojektoren auf den drei dunklen C_S-Werten bestätigen die
Trennung ausdrücklich; beide Casimire zugleich werden nicht benötigt.

**Es handelt sich um eine gelöste Kombinationsfrage, nicht um eine neue
Kontrollfreigabe.** Der benötigte Casimir ist noch kein vom Compiler
bereitgestelltes Messinstrument. Der große verbleibende Kommutant zeigt
weiterhin viele nicht aufgelöste Freiheitsgrade. Die Dimensionszahlen gelten
für N=3, nicht als vollständige Klassifikation aller Ladungssektoren.

## 5. Neuer kleiner Transportzeuge mit tatsächlichen W-Kanälen

Ein gemeinsamer Fermion-/Boson-Dreierstern hätte die einfache Identität

\[
Q_x=b^\dagger s f_x,\quad Q_y=b^\dagger s f_y,
\qquad [Q_y^\dagger,Q_x]=(N_b+n_s)f_y^\dagger f_x.
\]

Auf festem `K=Nb+n_s≥1` ist `c†=b†s/√K` exakt eine CAR-Mode. Das ergibt
eine gewöhnliche Dreimoden-Transferkette. **Aber dieser Stern ist nicht
in einer nativen W-Zeile enthalten:** Jede Zeile ist ein Matching aus acht
disjunkten Paaren. Die Analogie allein wäre daher eine falsche Herkunftsangabe.

Im echten W gibt es stattdessen die Paare `(4,57)` in Kanal 0 und `(4,58)`
in Kanal 1. Mit den sieben besetzten Pauli-Blockern

\[
S_b=\{8,16,28,32,44,52,56\}
\]

und einem **zusätzlichen** Mischer `J(b1†b0+b0†b1)` schließt die volle
native Wechselwirkung exakt auf den vier Zuständen

\[
S_b+\{4,57\}\ \longleftrightarrow\ S_b+b_0
\ \longleftrightarrow\ S_b+b_1
\ \longleftrightarrow\ S_b+\{4,58\}.
\]

Alle haben N=9. Die vollständige Wirkung sämtlicher 480 signierter Paarterme
bleibt in diesem Raum, mit Matrix

\[
H_4=\begin{pmatrix}
0&g&0&0\\g&\Delta&J&0\\0&J&\Delta&g\\0&0&g&0
\end{pmatrix}.
\]

Für `g/Δ=1/20`, `J/Δ=1-1/(10√3)` und `tΔ=20π√3` gilt analytisch

\[
P(57\to58)>\frac{2009992727}{2022609600}
=0.9937620819\ldots>99.3\%.
\]

Die Eigenfrequenzen Δ±J bleiben positiv. Dies ist keine unkontrollierte
Vierzustandsabschneidung: Zuerst ist die Invarianz unter der vollständigen
Wechselwirkung bewiesen, danach wird deren exakte Einschränkung gelöst.
Ohne Mischer zerfällt sie in zwei getrennte Blöcke und der Transfer ist null.

Der reine Einzelmischer kommutiert nicht mit dem ursprünglichen Clock.
Die Clock-Orbitsumme der Mischer `(0,1)+(12,13)+(6,7)` ist dagegen
Clock-invariant und hat auf diesem Vierzustandsraum dieselbe Wirkung.
Somit wäre „jeder solche Transfer muss den Clock brechen“ falsch. Beide
Mischer sind jedoch noch zusätzliche Operationen; Clock-Invarianz allein
beweist keine Erzeugbarkeit. Ein gemeinsamer SU(4)-Cartan Q kommutiert mit
H, Nb, Clock und beiden getrennten Casimiren. Auf den vier Zuständen besitzt
er aber die Werte `(7,7,9,9)`. Die beiden Mischer ändern diese Quantenzahl:
`||[Q_B,M01]||²_F=8`, `||[Q_B,Morb]||²_F=24`. **Auch die Clock-invariante
Orbitsumme ist damit aus diesem Operationssatz ausgeschlossen.**

Die noch fehlende Ressource ist hier konkret: eine Operation, die diese
innere Cartanladung verändert, oder eine global hergeleitete Kopplung an
einen ausdrücklich mitgerechneten Ladungsausgleich. Mehr Wörter aus
dem unveränderten erhaltenden Alphabet können beide Mischer nicht liefern.

Dieser Zeuge ist **keine** Propagation der N=64-Grundzustands-Lochanregung,
keine räumliche Zwei-Banken-Übertragung und keine Konstruktion ihrer
Präparation. Er zeigt konstruktiv, wie nah eine kleine Paarumwandlung an
einem Transfermechanismus liegen kann, und benennt die fehlende Ressource.

## 6. Das Feldwörterbuch: eine Basisänderung allein reicht nicht

Der bestätigte Grundfehler bleibt: `M_A⊗ε_Lorentz` ist symmetrisch und
verschwindet als Grassmann-Bilinear. Das betrifft die lokale ableitungsfreie
Zuordnung einer gleichhändigen Weylkopie je ursprünglichem Label bei
unverändertem antisymmetrischem W. Der nichtverschwindende gleichhändige
Kanal trägt `(1,0)`; daraus folgt noch keine gesunde Kinetik.

Der neue Fünf-Zyklus im Trägergraphen widerlegt eine rein diagonale
Zuweisung entgegengesetzter Händigkeiten an jedes Paar. Ein neuer eigener
Satz geht darüber hinaus. Für irgendeine hermitesche interne Händigkeit Γ
müsste im unveränderten Ein-Kopie-Vektoransatz gelten

\[
\Gamma^TM_A+M_A\Gamma=0\quad\forall A.
\]

Adjungieren und Einsetzen liefert `[Γ,M_A†M_B]=0`. Der ursprüngliche Tensor
faktorisiert exakt als

\[
M_{ka}=S_k\otimes C_a,\quad
\sum_kS_k^\dagger S_k=5I_{16},\quad
\sum_aC_a^\dagger C_a=3I_4.
\]

Die S_k†S_l erzeugen M16; die C_a†C_b erzeugen M4. Dafür wurden vollständige
Rangzertifikate modulo 101 mit 256 bzw. 16 unabhängigen ganzzahligen
Matrixwörtern konstruiert. Ein nichtverschwindender Determinant modulo 101
beweist Nichtverschwindung über C; keine Rangdefizienz wird übertragen.
Damit ist Γ skalar, und die ursprüngliche Gleichung erzwingt Γ=0.

**Keine hermitesche Involution Γ²=I auf demselben Träger repariert diesen
Ein-Kopie-Vektoransatz.** Der Ausschluss ist nun basisunabhängig, aber
weiterhin vertragsgebunden.

Nicht ausgeschlossen sind zusätzliche Dirackomponenten, ein unabhängiger
Zweierfaktor oder Ableitungsterme. Insbesondere ist

\[
M_A\otimes\epsilon_{aux}\otimes\epsilon_{Lorentz}
\]

antisymmetrisch und nicht null. Ein ableitungshaltiger gleichgeladener
Vektorstrom `M_IJ ε_ab ψ_Ia ↔∂_μ ψ_Jb` ist ebenfalls nicht null; der
pauschale Vektorausschluss durch Ladung gilt nicht außerhalb der
ableitungsfreien Klasse.

Die Zahlen 180/128 oder 60/256 zählen Komponenten eines bestimmten
Feldansatzes, nicht automatisch unabhängige propagierende Oszillatoren.
Schur fixiert interne Intertwiner, nicht alle Lorentz-/Ableitungsterme.
Der behauptete Zwang „zuerst räumlich skalieren, danach Feldtyp prüfen“ folgt
nicht daraus. Zuerst bleibt ein kleiner konsistenter Typ-/Kinetiktest sinnvoll;
seine reale räumliche Herkunft muss anschließend gemeinsam geprüft werden.

## 7. Was der nachgereichte Universalraum-Text trägt

### 7.1 Eine sinnvolle Hypothese, kein bereits identifiziertes universelles Objekt

Nichtorthogonale oder überlappende lokale Einbettungen in eine gemeinsame
Algebra sind eine ernstzunehmende Alternative zu unabhängigen Banken. Sie
können Voraussetzungen der lokalen Paritätsschranke ändern. Das ist ein
Forschungsauftrag, kein Widerspruch zur bisherigen Schranke.

Bei Einbettungen `J_A:V_A→V` gilt für die CAR jedoch

\[
\{f_A(u),f_B(v)^\dagger\}=\langle J_Au,J_Bv\rangle.
\]

Die Überlappungs-Grammatrix gehört also zwingend zum Modell. Die alten
Produktzustände `Ω_A⊗Ω_B`, ihre beiden unabhängigen Ladungssektoren und
der Zwei-Banken-Polraum dürfen nicht ungeprüft in einen überlappenden
Träger übernommen werden. Der gemeinsame Hamiltonoperator und sein Zustand
müssen dort neu beziehungsweise durch einen bewiesenen Adapter konstruiert
werden.

### 7.2 Der vorgeschlagene Kill-Test muss korrigiert werden

Für unabhängige orthogonale Banken kann Π_AΠ_B deren gemeinsame Parität
sein. Für überlappende Unterräume gilt das nicht allgemein; ihre lokalen
Paritäten müssen nicht einmal kommutieren. Der Test
`[U,Π_AΠ_B]=0` ist deshalb im neuen Bild nicht der richtige universelle Test.
Stattdessen muss die tatsächliche globale Parität Π_global separat definiert
und erhalten werden. Ein nichtverschwindender Kommutator mit einer lokalen
Parität belegt zudem allein noch keinen gerichteten Transfer.

### 7.3 Der einfachste False-Positive: Ein Signal ohne Bewegung

Seien `a=c1`, `b=(c1+c2)/√2` auf zwei globalen CAR-Moden und `H=ωN`.
Dann haben die beiden Einteilchen-Chartzustände bereits Überlappung `1/√2`.
In ihrer nichtorthogonalen Basis ist `K=ωS` mit einem nichtverschwindenden
Offdiagonalelement. Trotzdem bleibt die betreffende Wahrscheinlichkeit
zu jeder Zeit genau 1/2. Es wurde nichts transportiert.

Ein belastbarer gemeinsamer Test muss daher mindestens

\[
S_{AB}=\langle\psi_A,\psi_B\rangle,\qquad
K_{AB}=\langle\psi_A,H\psi_B\rangle
\]

und die tatsächliche Zeitantwort gemeinsam bestimmen. Auf einem positiv
definiten Gramträger ist `S^{-1/2}KS^{-1/2}` der korrekte orthonormierte
Operator; bei singulärem S ist zunächst der Nullraum zu quotientieren.
Im Gegenbeispiel ergibt dies nur ωI. Die Offdiagonale von K war kein Hop.

Das trifft sogar unmittelbar den vorhandenen nativen Pol. Dessen
64-dimensionaler Raum besitzt genau **eine** Energie E_h, also
`P_h H P_h=E_h P_h`. Sind A und B nur neue Charts innerhalb dieses selben
Polraums, gilt zwangsläufig `K=E_h S`. Bloßes Umbenennen der 64 entarteten
Polrichtungen erzeugt daher keine Ausbreitung durch H. Eine tatsächliche
globale Dynamik beziehungsweise eine verfügbare aktive Operation muss
hinzukommen und aus der Quelle ausgewiesen werden.

Für die eigentliche TFPT-Lochantwort wäre der gemeinsame Gegenstand

\[
G_{AB}(t)=\langle\Omega,
 f_B^\dagger e^{-it(H-E_0)}f_A\Omega\rangle,
\]

mit einer einzigen Quelle, einem H und einem Ω. `G(0)` bezahlt die schon
vorhandene Überlappung; die dynamische Änderung muss davon unterschieden
werden. Das ist die geschärfte, kleinere nächste Forschungsaufgabe.

### 7.4 Was nicht automatisch folgt

- **Zeit:** Für einen Grundzustand ist `e^{-itH}Ω=e^{-itE0}Ω`; sein physischer
  Zustand bleibt gleich. Das ist kein eigener Zeitpfeil. Nichtstationäre
  Präparation, Korrelationen und Records müssen ausgewiesen werden.
- **Eichfeld:** Für bloße Basiswechsel `Uxy=Vx†Vy` teleskopiert jede
  geschlossene Holonomie zu I. Echte Krümmung braucht zusätzliche
  Verbindungs-/Transportdaten oder einen nachgewiesenen Mechanismus.
- **Spin:** Zwei Orientierungsmarken liefern nicht von selbst einen
  SL(2,C)-Spinor, dessen Transformationsgesetz und Kinetik. Der zusätzliche
  antisymmetrische Zweierfaktor muss unabhängig konstruiert sein.
- **Raum:** Minimale Operationskosten sind ohne Reversibilität zunächst
  gerichtete Kosten, nicht notwendig eine symmetrische Metrik. Kubisches
  Volumenwachstum allein beweist keine 3D-Mannigfaltigkeit, keine
  Lorentzstruktur und keinen gemeinsamen Lichtkegel.
- **Gravitation:** Dynamische Beziehungen sind ein möglicher Träger, aber
  ein masseloser Spin-2-Sektor, zwei Helizitäten, Energiepositivität und
  universelle konsistente Kopplung bleiben zu beweisen.
- **Arithmetik:** Primitive Schleifen besitzen generisch neue gemischte
  primitive Zyklen. Sie sind nicht automatisch Primzahlen. Die Xi-Determinante
  bleibt eine unbewiesene vollständige Operatoridentität. Der getrennte
  RH-Anhang dokumentiert Vorarbeiten, Beispiele und Quellenstatus.

Der Text wird deshalb als **präzisierter globaler Forschungsansatz**
integriert, nicht als Nachweis, dass derselbe unbekannte Baustein schon alle
T1-T8-, RH-, Faktorisierungs-, P/NP- und Hylæan-Fragen beantwortet.

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

| Front | In dieser Revision weitergekommen | Noch erforderlicher Nachweis |
|---|---|---|
| T1 - Ursprung und Auswahl | Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer | Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand |
| T2 - Half-Charge/E8-Feld | Bestehender geladener Pol bleibt abgesichert, innere Darstellung präzisiert | Renormiertes Half-Charge-Feld mit Energie-/Adjungiertenkontrolle und E8-/Clock-Adapter |
| T3 - gemeinsamer 3+1D-Parent | Kleiner exakter Paartransferzeuge und korrigierter Überlappungstest | Quellenseitig ausgewählter räumlicher Parent auf einem gemeinsamen Hilbertraum und Zustand |
| T4 - chirale Materie | Basisunabhängiger Ausschluss eines konkreten Ein-Kopie-Vektoradapters | Konsistenter chiraler Feldadapter, Maß/Anomalien/Index und Spiegelentkopplung |
| T5 - Kontinuum und Dynamik | Exakte endliche Clock-/Casimir-Kombination und bedingter invarianten Transferblock | Kontrollierter wechselwirkender Grenzübergang, Lorentzverhalten, Clustering und Streuung |
| T6 - Kopplungen und Texturen | Keine neue Herleitung; neue Mischparameter sichtbar zusätzlich | Herkunft aller Kopplungen und vollständiger Neutrinostruktur/-skala |
| T7 - Gravitation | Der falsche pauschale Tensor-Ausschluss bleibt zurückgenommen | Masseloser dynamischer Spin zwei, beide Helizitäten, konsistente universelle Kopplung im selben Parent |
| T8 - Präparation und Auslesung | Gram-/Antworttest gemeinsam formuliert; spezielle Blockerressource konkret | Natives geladenes Instrument, Quellzustandswahl, Records und ein gemeinsames Auslesefunktional |

Keiner der acht vollständigen Abschlussverträge wird in dieser Revision auf
„gelöst“ gesetzt. Gelöst wurden ausdrücklich benannte Teilfragen.

## 9. Die nächsten drei Arbeiten - klein, gemeinsam und entscheidbar

**A. Den gemeinsamen Quellenvertrag wirklich hinschreiben.** Zwei lokale
Einbettungen, ihr CAR-Gram, globale Parität und Ladung, ursprüngliche
Operationen und ein einziges H angeben. Abbruch für eine Kandidatenfassung,
wenn sie nur zwei Koordinatenansichten desselben unveränderten Signals
umbenennt. Die gemeinsamen Generatoren müssen einen nachweislich neuen
Antwortprozess ermöglichen, nicht nur eine andere Beschriftung.

**B. Die fehlende Zwischenoperation ausweisen.** Der Vierzustandszeuge gibt
eine konkrete positive Zieloperation vor. Zu prüfen ist, ob der Compiler
ein geeignetes Mischinstrument oder eine andere geteilte Paarstruktur
wirklich liefert. Clock und Casimire alleine sind kein Herkunftsbeweis.
Zeigt ein erhaltener gemeinsamer Generator die Unmöglichkeit für einen
festen Operationssatz, endet dessen weitere Kommutator-Suche; dann muss
ein anderer bereits vorhandener Quellbestandteil benannt werden.

**C. Dieselbe Anregung und denselben Zustand behalten.** Auf dem Kandidaten
`G_AB(0)` und `G_AB(t)` einschließlich vollständiger Restantwort bestimmen.
Der N=9-Zeuge darf nicht still zum N=64-Lochpol umgedeutet werden. Ein
minimaler Lorentz-/Kinetikadapter muss die nachgerechneten Tensorbedingungen
erfüllen. Erst mit diesem gemeinsamen Anschluss trägt eine großräumige
Skalierungsrechnung.

Der stärkste Vereinfachungsgewinn dieser Runde ist damit konkret:
**Clock und innere Symmetrie sind nicht zwei voneinander unabhängige
Mechanismen; reine Überlappung und echte Bewegung sind dagegen zwei
verschiedene Dinge.** Die weitere Suche sollte diese erste Identität nutzen
und die zweite Unterscheidung im selben kleinen Modell erzwingen.

## 10. Belege und Reproduzierbarkeit

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit
reproduziert die 1127 gelieferten Guards; eigene Programme behandeln
Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion,
basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und
die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den
jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählungen
und Bytevergleiche stehen im Auslieferungs-/Replayprotokoll; interne erneute
Aufrufe der 944 Guards werden nicht mehrfach als neue Tests gezählt.

Die drei ausführlichen parallelen Berichte und der Überlappungs-/RH-Nachtrag
folgen im vollständigen Dokument. Ihr Status ersetzt widersprechende
historische Deutungen, nicht unveränderte ältere Beweise. Das native frühere
Archiv bleibt zusätzlich unverändert im Paket; dessen große frühere
Enumeration wird nicht als in dieser Revision erneut durchgeführt ausgegeben.


---

# Anhang A: Quellenprüfung Symmetrie und Verfügbarkeit

# Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 1. Reproduktion

Alle drei Programme wurden vollständig gelesen und anschließend in isolierten Kopien ausgeführt. Die relevanten Tensoren wurden an ihre von den unveränderten Programmen erwarteten relativen Orte kopiert. Normaler und optimierter Lauf reproduzieren jeweils die gelieferten Ergebnisdateien byteidentisch, ohne Standardfehlerausgabe:

| Programm | Gelieferte Prüfbedingungen | Reproduktion |
|---|---:|---|
| `operation_symmetry.py` | 944 | PASS, identisch |
| `symmetry_availability.py` | 31 | PASS, identisch |
| `lorentz_types.py` | 152 | PASS, identisch |
| Summe | 1127 | normal und `-OO` |

Die Zusatzprüfung `check_scope.py` rechnet kleine exakte Gegenprüfungen zur Reichweite der Aussagen. Das ausführbare Reproduktionsprogramm ist `replay.py`; Quellenpins, Kopien, Originalberichte und Ausgaben liegen in diesem Auditordner. `replay_receipt.json` dokumentiert alle Pins und die Unverändertheit der Eingaben.

Programm-Pins:

| Quelle | SHA-256 |
|---|---|
| `operation_symmetry.py` | `ec93f759d6582f42542a597bf916ee2a62a51c510240aa777ae439e90fe28382` |
| `symmetry_availability.py` | `88cc3e3361a198fe7b1b32a7174f3dd45f341106978d8abd8d5722e0cb631967` |
| `lorentz_types.py` | `43777c81ea8ba2d2ae12b711321a54abd7f7152a326611a296598d5c5dd463da` |
| Nativer Tensor | `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763` |

Die Erzählung über zwei unabhängig entstandene, vollständig übereinstimmende Programme ist durch diese Reproduktion **nicht** geprüft: Vorgelegen hat die erhaltene Fassung mit 944 Guards, nicht die vorherige Fassung mit 528 Guards.

## 2. Bestätigte Mathematik

Der N=3-Raum zerfällt als Darstellung von Spin(10) × SU(4) in sieben Isotypien. Drei haben Multiplizität zwei, die anderen vier Multiplizität eins. Die zwei Fockteile Λ³(C⁶⁴) und C⁶⁰⊗C⁶⁴ sind jeweils multiplizitätsfrei; der gesamte N=3-Raum ist es ausdrücklich **nicht**.

Die irreduziblen Dimensionen sind 24000, 11200, 2688, 2880, 576, 320, 64; die mit Multiplizitäten gewichtete Summe ist 45504. Die Spin(10)-Darstellung mit Dimension 16 in BF und Λ³ ist in den angegebenen Gewichten die konjugierte Spinordarstellung; die Dimensionskurzschreibweise `16` darf diese Information nicht ersetzen.

Bestätigt sind:

- die exakte Zerlegung über Gewichtsmultiplizitäten und Racah-Alternation;
- `C(560)=117/4` in der erklärten Casimir-Normierung;
- die Quellenintertwiner für alle 60 Lie-Erzeuger;
- `rank C3=3776`, `dim ker C3=37888`;
- Spektrum von `C3 C3†`: 0,7,10,12 mit Multiplizitäten 64,2880,576,320;
- die drei dunklen Typen mit Gesamtcasimir 45, aber getrennten Spin-Casimiren 141/4,117/4,165/4;
- für den **gewährten** Satz X,Nb eine assoziative Algebra der komplexen Dimension 14;
- für alle punktweise symmetrieinvarianten Operatoren die Dimension 16;
- nach zusätzlicher Gewährung aller 60 Gruppenerzeuger die assoziative Dimension 743583744 und Kommutantdimension 7.

Die Eigenwertzuordnung im Code prüft pro S-Eigenwert einen Vektor, nicht eine vollständige Basis dieses Eigenraums. Zusammen mit der unabhängig geprüften Multiplizitätsfreiheit, der Kommutation mit allen Erzeugern und der eindeutigen Dimensionszuordnung der BF-Teilsummen ist die Zuordnung trotzdem abgesichert. Die Guard-Beschriftung »entire eigenspace« ist als direkte Beschreibung dieser einen Rechnung zu weit.

## 3. Invarianz und Kovarianz auseinanderhalten

Mit `A0=Alg*(X,Nb)` und Gruppenwirkung ρ bezeichne

`C = End_G(H3) = ⊕_i End(C^{m_i}) ⊗ I_{d_i}`.

Dann gilt `A0 ⊂ C`, `dim A0=14` und `dim C=Σ m_i²=16`. Jedes Wort aus X und Nb kommutiert mit ρ(G). Nichtzentrale Lie-Erzeuger können deshalb aus diesem Alphabet nicht entstehen. Dieser Ausschluss ist korrekt und bleibt richtig, wenn nur ein fixes H statt zweier unabhängiger Kontrollen gewährt ist.

Nach Gewährung der Gruppenerzeuger entsteht dagegen

`Afull = ⊕_i End(C^{m_i} ⊗ V_i)`.

Diese Algebra ist **unter Gruppenkonjugation stabil**, aber ihre Operatoren sind nicht sämtlich invariant. In `symmetry_availability.py` ist die Kennzeichnung `symmetry_invariant: true` für diese Zeile daher falsch. Der Kommutant von Afull ist die sieben-dimensionale skalare Blockmitte.

Sieben ist ein Boden, solange alle zusätzlichen Operationen diese sieben Isotypie-Projektoren erhalten; insbesondere senken zusätzliche punktweise G-invariante Operationen den bereits erreichten Kommutanten nicht weiter. Sieben ist aber **kein** universeller Boden für unter G stabile Algebren oder alle denkbaren nativen Verträge. `End(H3)` ist unter jeder Gruppenkonjugation stabil und hat nur den skalaren Kommutanten. Ein exaktes 2×2-Gegenmodell in der Zusatzprüfung macht die Unterscheidung direkt sichtbar.

Die Zahlen sind zudem Dimensionen **komplexer assoziativer Sternalgebren**, keine nachgewiesenen Dimensionen einer dynamischen Lie-Algebra oder erreichbaren Unitärgruppe. Burnside liefert nicht automatisch beliebige ausführbare Gatter auf jedem irreduziblen Block.

## 4. Verfügbarkeit ist keine universelle Ja/Nein-Frage

Ein vorgegebener Hamiltonoperator allein gewährt nicht bereits das unabhängige Schalten von X und Nb. Am erklärten Punkt g/Δ=1/20 besitzt ein fixes H im N=3-Raum acht verschiedene Energien, also nur eine acht-dimensionale kommutative Spektralalgebra. Die großzügigere Annahme unabhängiger Kontrollen X,Nb ergibt 14.

Eine treue, auf die Multiplizitätsräume reduzierte rationale Matrixrechnung ergibt:

| Zusätzlich gewährter Satz | Assoziative Dimension |
|---|---:|
| Nur fixes H=Nb+X/20 | 8 |
| X,Nb | 14 |
| X,Nb plus Projektor auf genau einen dunklen Typ | 15 |
| X,Nb plus Spin(10)-Casimir | 16 |
| X,Nb plus SU(4)-Casimir | 16 |
| X,Nb plus Gesamtcasimir | 14 |

Bereits **einer** der getrennten Casimire reicht zur vollständigen Trennung der drei dunklen Typen. Die zwei fehlenden Algebradimensionen sind kein Beweis, dass genau zwei physische Griffe fehlen. Die Dimension 15 zeigt eine mögliche invariante Zwischenstufe. Die behauptete universelle Dichotomie »getrennte Griffe ja oder unverändert 14« und das `IF AND ONLY IF` zur Verfügbarkeit der vollen Symmetrie sind daher zu stark.

Die zusätzlichen Projektoren und Casimirkontrollen werden hier nur als algebraische Gegenbeispiele verwendet. Ihre Implementierung aus dem Compiler wird nicht behauptet.

## 5. Der Clock-Satz ist im gelieferten Checker nicht geprüft

`operation_symmetry.py:478` schreibt den Normalisator- und Nichts-hinzufügen-Satz als `need(True, ...)`. Insgesamt enthält diese Datei neun solche als Prüfbedingungen gezählten theoretischen Folgerungen. Einige sind durch die vorausgehende Mathematik gut begründet; der bloße grüne Guard zertifiziert sie jedoch nicht unabhängig.

Die direkte Clock-Definition liegt in `universalraum-native-operations-ground-response-20260915/common.py`, Funktion `clock_lift`, ab Zeile 187: eine Permutation der fünf Oszillatorachsen wird mit Exterior-Vorzeichen auf den geraden Spinorraum gehoben; `GF=G16⊗I4`. Der Bosonlift wird entsprechend gebaut und die Tensorintertwining-Gleichung geprüft. Eine neue direkte Prüfung der Clock-/Casimir-Beziehungen erfolgt im parallelen Hauptstrang, nicht in diesem Audit.

## 6. Feldtyp: was tatsächlich erzwungen ist

Für ein **lokales, ableitungsfreies Bilinear zweier gleichhändiger Weylfelder**, das alle 64 inneren Quellenmarken unverändert als unabhängige innere Komponenten und genau den gegebenen antisymmetrischen Tensor W verwendet, gilt

`(1/2,0) ⊗ (1/2,0) = (1,0) ⊕ (0,0)`.

Die skalare Epsilon-Kontraktion zusammen mit antisymmetrischem W ist im gemeinsamen Index symmetrisch und verschwindet wegen Grassmann-Antikommutation. Der symmetrische Spinortensor, also der (1,0)-Kanal, bleibt nichtverschwindend. Im genannten Vertrag ist dies korrekt. Ein zusätzliches unabhängiges gleichgeladenes Hilfsdublett erlaubt stattdessen wieder die skalare Kontraktion.

Die Zahlen 180/128 beziehungsweise 60/256 zählen **komplexe lokale Feldkomponenten im jeweiligen direkten Tensorprodukt-Ansatz**. Sie zählen nicht automatisch zusätzliche unabhängige physische Oszillatoren oder propagierende Freiheitsgrade. Diese hängen von Kinetik, Nebenbedingungen, positiver Energie, Teilchen-/Antiteilchenstruktur und dem tatsächlichen Feldadapter ab. Deshalb folgt aus der Multiplikation mit zwei oder drei kein allgemeiner Ausschluss jeder relativistischen Lesart mit den nativen Modenzahlen.

Vor allem folgt daraus keine vorgeschriebene Reihenfolge »erst räumliche Skalierung, dann Feldwörterbuch«. Lokale Darstellungstypen und mögliche Kinetik können vor einer Skalierungsrechnung geprüft werden. Welche Feldkomponenten tatsächlich aus dem räumlichen Quellprozess entstehen, muss anschließend gemeinsam mit dem Adapter untersucht werden.

### Konkreter Gegencheck jenseits der ableitungsfreien Klasse

Der allgemeine Satz »ein Vektor verlangt ψ†ψ und scheitert deshalb an der Ladung« ist falsch, sobald Ableitungen zugelassen werden. Beispielsweise ist

`J^A_mu = Σ_IJab M^A_IJ ε_ab ψ_Ia ↔∂_mu ψ_Jb`

ein Lorentzvektor mit Ladung −2. Die Ableitungsantisymmetrisierung macht ihn bei antisymmetrischem M nichtverschwindend. Für M=ε und zwei inneren Marken liefert die exakte Grassmann-Jetrechnung vier nichtverschwindende Monome mit Koeffizienten +2,−2,−2,+2. Ein entsprechend geladener Vektorvermittler könnte algebraisch durch `b†_mu J^mu + h.c.` koppeln, ohne Ladungsverletzung.

Das ist **nur ein Gegenbeispiel gegen den überbreiten Ausschluss**, keine native Lösung: Es fügt eine Ableitung und einen Feldtyp hinzu; bei kanonischen 4D-Felddimensionen ist es ein höherdimensionaler Kopplungsterm. Gesunde Kinetik, Quellenherkunft, Skalierung und T1-T8 werden dadurch nicht bewiesen.

## 7. Konsequenz

Die neuen Quellen verkleinern und präzisieren den endlichen N=3-Operationsraum. Sie schließen weder die physische Verfügbarkeit der Operationen noch den Lorentzadapter. Die sachlich tragfähige Integration übernimmt die Zerlegung, Casimire, 14/16/7 im jeweils erklärten Vertrag sowie den eingeschränkten Feldtypsatz; sie ersetzt die überbreiten Ausschlüsse und die behauptete Programmumkehr durch explizite Bedingungen.


---

# Anhang B: unabhängige Krylov- und Feldprüfung

# Unabhängige Prüfung: Krylov-Verzweigung und Feldwörterbuch

Arbeitsstand 2026-09-15. Geprüft wird die Anlage `7380c383-f364-4ef8-8066-24aa4d180d85` gegen den Vertrag `universalraum-native-operations-ground-response-20260915`. Fremde Quellen und Ausgaben wurden nicht verändert. Die hier angegebenen Matrix- und Graphbefunde beziehen sich auf denselben gepinnten Tensor W mit SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

## 1. Der neue Nichtschluss ist exakt bestätigt

Für `v_n=(T†)^n F` habe ich `u=T T† v_2=T v_3` unmittelbar aus den 480 nativen Paaren neu kontrahiert. Das materialisiert nicht die 15.252.960 Komponenten von v₃. Es arbeitet mit 108.240 Komponenten von v₂ und 293.280 nichtverschwindenden Komponenten des Ergebnisses u. Es wurden 45.771.360 zulässige Erzeugungsübergänge und 139.289.760 anschließende Entnahmebeiträge exakt mit ganzzahliger Fermion-Parität und Boson-Multiplizität zusammengeführt.

Die unabhängige Rechnung liefert

\[
\|v_2\|^2=439680,\quad
\langle v_2,u\rangle=575078400,\quad
\|u\|^2=752194252800.
\]

Damit folgen rein rational

\[
\alpha=\frac{299520}{229},\qquad
w_2=u-\alpha v_2,\qquad
\|w_2\|^2=\frac{5001523200}{229}>0,
\]

und

\[
\frac{\|w_2\|^2}{\nu_3}=\frac{1809}{47632}.
\]

Der Ein-Vektor-pro-Bosonlage-Ansatz ist somit nicht invariant. Da T die native Symmetrie erhält und v₂ und u Singuletts sind, liefert w₂ einen zweiten unabhängigen Singulettvektor in derselben Bosonlage. Das ist ein Strukturresultat, kein physikalischer Mehrteilchen- oder Raumzeitnachweis.

## 2. Das mitgelieferte Ground-JSON ist veraltet und teilweise falsch

Die aktuelle Pythonquelle hat SHA-256 `8ae0f2f103ba0cb0a5cb832681a33130b6756fe627395368b6be635587a2eb02`. Das vorhandene `native_ground_state.json` nennt dagegen `046ffa3f41d9dd365e2c9a199e938734bf735d762f23373a3f85b541c3da30fe` und enthält noch

\[
\|w_2\|^2_{\rm alt}=1145348812800
=229^2\|w_2\|^2.
\]

Sein `closure_defect=1.5226768996658837` ist schon als relative orthogonale Norm unmöglich. Das daraus abgeleitete Ritz-Ergebnis −1,18826198 ist ungültig. Der spätere Anlagentext korrigiert den Normfehler, aber die JSON-Belegkette wurde noch nicht entsprechend neu erzeugt. Das grüne `status: PASS` dieser historischen Ausgabe darf deshalb nicht mit dem korrigierten Text zusammengezogen werden.

Die korrigierte Norm und die folgenden kleinen Matrizen wurden hier unabhängig reproduziert. Die ganze fremde große Ausführung wurde ausdrücklich nicht erneut gestartet.

## 3. Die sechste Dezimalstelle ist richtig - aber nur für die eine zusätzliche Richtung

Die neue numerische Diagonalisierung ergibt:

| g/Δ | vierdimensionale Ritz-Matrix | plus w₂ | Änderung |
| --- | ---: | ---: | ---: |
| 1/20 | −1,0942308394409612 | −1,0942318710142458 | −1,0315733·10⁻⁶ |
| 1/40 | −0,29535718178032033 | −0,29535720496683315 | −2,3186513·10⁻⁸ |
| 1/100 | −0,04789424798601009 | −0,04789424801311775 | −2,7107663·10⁻¹¹ |

Das sind numerische Eigenwerte exakter kleiner Ritz-Matrizen, keine nach außen gerundeten vollständigen Spektraleinschließungen. Durch Eliminieren der einzigen neuen w₂-Koordinate bekommt die v₃-Diagonale die exakt bestimmte energieabhängige Korrektur

\[
-\frac{g^2(1809/47632)}{2\Delta-E}.
\]

Das erklärt die kleine Änderung durch diesen einen Zweig. Es sagt nichts über die ausgelassenen höheren Bosonlagen.

### Eigene einfache Folgeherleitung: Das vollständige Ritz-Residuum

Sei ψ₃ der normierte Ritz-Eigenvektor in `span(v₀,…,v₃)`, und c₃ seine Komponente entlang `v₃/√ν₃`. Außerhalb dieses Raums führt Hψ₃ genau in zwei orthogonale Richtungen: v₄ und w₂. Deshalb gilt exakt

\[
\|(H-E_{\rm Ritz})\psi_3\|^2
=g^2|c_3|^2\frac{\nu_4+\|w_2\|^2}{\nu_3}.
\]

Hier wird `ν₄=952296652800` aus dem früher vollständig geprüften Momentbeleg übernommen; die vierte Ordnung wurde in dieser Runde nicht erneut enumeriert.

Bei g/Δ=1/20 folgt numerisch ein Residuum von rund **0,373063 Δ**. Der w₂-Zweig trägt weniger als **23 Millionstel** des quadrierten Residuums. Die große ausgelassene Richtung ist v₄, nicht w₂. Aus dem winzigen Nichtschlussanteil darf daher keine praktisch vollständige Konvergenz abgeleitet werden.

Außerdem liegt die neue Fünf-Zustands-Ritzenergie mindestens **0,0354 Δ über** der bereits bewiesenen Obergrenze des wahren Grundzustands. Das ist eine nachweislich noch relevante Lücke, unabhängig von einer Konvergenzschätzung.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

Der ältere, gepinnte Beweis lautet: Für Δ>0 und 0<|g|/Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

Die neue Ausführung benutzt schwächere Sektor-Untergrenzen und weniger Ritz-Vektoren. Dass diese schwächere Methode bei 1/20 nicht genügt, ist weder eine Widerlegung noch ein Wiederöffnen des früheren Satzes. Insbesondere sind die vorgeschlagenen Ziele `E<−1,2Δ` bzw. `E<−1,1625Δ` unmöglich, weil bereits `E₀>−1,158089Δ` bewiesen ist. Bessere Schranken für die Konkurrenzsektoren sind erforderlich, nicht eine unrealistisch tiefere Energie.

Die neuen Zahlen `Nb≈0,84211266`, `Zh≈0,97368398` und `εh≈0,03107309Δ` gehören zum nichtstationären K₃-Ritz-Zustand. Nb liegt sogar knapp unter der früher bewiesenen Schranke `Nb(Ω)>0,842846`. Zh bezeichnet die gesamte Entnahmenorm dieser Näherung, nicht das Gewicht der isolierten niedrigen Linie. Ein erstes Moment auf einem Ritz-Zustand ist keine neu bestimmte Polenergie auf Ω.

Offen bleiben der vollständige Ω-Vektor, die physische Auswahl des μ=0-Vertrags und die Herkunft ausführbarer räumlicher Operationen.

## 5. Feldwörterbuch: bestätigte Algebra und notwendige Einschränkungen

Frisch exakt geprüft wurden:

- Der Trägergraph ist zusammenhängend, 15-regulär und dreiecksfrei.
- Der Fünf-Zyklus `16→45→0→30→37→16` liegt wirklich im Trägergraphen.
- Für jeden der 60 nativen Kanäle verschwindet der gleichhändige Ein-Kopie-Weyl-Skalaransatz `M_A⊗ε` als Grassmann-Bilinear.
- Bei Dirac-Kernen sind C, Cγ⁵ und alle vier Cγ^μγ⁵ antisymmetrisch; alle vier Cγ^μ und alle sechs Cσ^{μν} sind symmetrisch.
- Die 43 getesteten nichttrivialen Gradierungen ergeben genau die angegebenen Kanalzahlen 24/36, 40/20 bzw. 32/28. Die Stabilisatordimensionen 36, 52 und 28 wurden diesmal durch exakt diagonale reelle Gram-Matrizen der Kommutatorbedingungen bestätigt, nicht durch einen SVD-Schwellwert.

Der Fünf-Zyklus allein schließt nur eine diagonale ±-Händigkeitszuweisung aus, die an jedem Paar entgegengesetzte Händigkeiten verlangt. Er allein ist kein basisunabhängiger Ausschluss und kein Ausschluss zusätzlicher Feldkomponenten.

### Eigener stärkerer Satz: auch ein Basiswechsel repariert den Ein-Kopie-Vektoransatz nicht

Sei Γ eine hermitesche Händigkeit auf dem ursprünglichen 64-dimensionalen internen Raum. Für einen ausschließlich entgegengesetzt-händigen, unveränderten Paartensor müsste

\[
\Gamma^T M_A+M_A\Gamma=0\quad\text{für alle }A
\]

gelten. Adjungieren und Einsetzen zeigt

\[
[\Gamma,M_A^\dagger M_B]=0\quad\text{für alle }A,B.
\]

Die native Faktorisierung wurde exakt rekonstruiert:

\[
M_{k,a}=S_k\otimes C_a,\quad
\sum_k S_k^\dagger S_k=5I_{16},\quad
\sum_a C_a^\dagger C_a=3I_4.
\]

Daher muss Γ sowohl mit allen `S_k†S_l⊗I₄` als auch mit allen `I₁₆⊗C_a†C_b` kommutieren. Die von den ersten Produktmatrizen erzeugte Algebra ist die volle M₁₆; die zweite ist M₄. Hierfür enthält die Prüfung vollständige Rangzertifikate von ganzzahligen Matrixwörtern modulo 101: **256 unabhängige Spinorwörter bis Länge zwei und 16 unabhängige Farbprodukte bis Länge eins**. Voller Rang modulo einer Primzahl beweist vollen Rang über den komplexen Zahlen; es wird ausdrücklich keine Rangdefizienz von einem endlichen Körper übertragen.

Folglich ist Γ skalar. Die ursprüngliche Gleichung erzwingt dann Γ=0. Insbesondere gibt es **keine hermitesche Involution Γ²=I** mit der verlangten Eigenschaft. Diese Schlusskette schließt den Ein-Weyl-pro-Label-Vektoradapter jetzt unabhängig von einer Wahl der internen Basis aus.

Der Satz betrifft unveränderte W-Kanäle und unveränderten 64-dimensionalen Träger. Er schließt **nicht** Diracfelder pro Label, zusätzliche Kopien, Ableitungsadapter oder andere ausdrücklich erweiterte Modelle aus.

## 6. Die minimale Erweiterung darf nicht aus Versehen mit ausgeschlossen werden

Zwei explizite Gegenkontrollen wurden auf allen 60 Kanälen neu gerechnet:

1. **Vierkomponenten-Diracfelder pro Label:** `M_A⊗Cγ⁰` ist nichtverschwindend und antisymmetrisch im gesamten Grassmann-Index. Es enthält zusätzliche linke und rechte Freiheitsgrade pro ursprünglichem Label. Deshalb widerspricht es dem Ein-Kopie-Satz nicht. Eine chirale Standardmodell-Entstehung folgt daraus nicht.
2. **Unabhängige Zweier-Erweiterung:** `M_A⊗ε_aux⊗ε_Lorentz` ist nichtverschwindend und antisymmetrisch. Der skalare Kanal wird möglich, weil die zusätzlich antisymmetrische interne Zweierform die Symmetrie des internen Paarfaktors umkehrt. Das ist die bereits bekannte minimale Reparatur im deklarierten Tensorprodukt-Ansatz, keine aus der Quelle hergeleitete Verdopplung.

Eine solche Zweier-Erweiterung macht auch den Trägergraphen durch `M_A⊗σ_x` bipartit: `Γ=I₆₄⊗diag(1,−1)` antikommutiert exakt mit allen so erweiterten Matrizen. Damit ist sichtbar, welche zusätzliche Ressource den ursprünglichen Ausschluss überwindet.

"Der Vermittler kann nie Skalar sein" muss folglich auf den unveränderten Ein-Kopie-Ansatz begrenzt werden. Ebenso fixiert Schur nur die interne Matrixstruktur innerhalb eines irreduziblen Blocks; es beweist nicht die Einzigartigkeit aller möglichen Lorentz- und Ableitungsterme. Eine gesunde Kinetik, Nebenbedingungen, Eichherkunft und ein dynamischer Spin-2-Sektor sind hier nicht konstruiert.

## Reproduktion und Status

`contracted_krylov.cpp` ist der unabhängige ganzzahlige Kontraktionskern. `verify.py` prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in `audit.json` und `audit_optimized.json`.

Es bestehen **376 Prüfbedingungen: 371 exakte und fünf numerische**. Für eine eigenständige Reproduktion zuerst den kleinen C++-Kern mit C++17 und Optimierung übersetzen; anschließend `verify.py` normal und mit `-OO` starten. Sämtliche Eingaben liegen eingefroren unter `sources/`; die Ergebnisdateien enthalten ihre SHA-256-Werte. Fremde Pythonprogramme werden hierbei nicht ausgeführt. Die numerischen Ritz-Prüfungen sind als solche markiert, alle Algebra-Zertifikate und die vollständige direkte Kontraktion verwenden exakte Ganzzahl-/Bruchrechnung.

Beide abschließenden Ausführungen bestanden und lieferten byteidentische JSON-Dateien mit SHA-256 `148047028236a887de1b28a0a9c12d84037a7c633892abc51dd9047f0b7a7baf`.

Keine T1-T8-Abschlussbehauptung. Keine Änderungen an fremden Quellen, Hauptpaper, Webseite, Ledger oder Git-Historie.


---

# Anhang C: minimaler Transfer und seine Quellen-Grenze

# Minimaler Ursprungsstrang: geteilte Moden und ein echter nativer Vierzustandskanal

Stand: 15. September 2026. Unabhängiger, begrenzter Forschungsstrang.

## Ergebnis und Reichweite

Es gibt zwei verschiedene Ergebnisse, die ausdrücklich nicht verwechselt werden dürfen:

1. **Ein exakt lösbarer Überlappungsbaustein:** Eine gemeinsame Fermionmode und ein gemeinsamer Bosonkanal werden in jedem festen positiven Ressourcensektor zu einer gewöhnlichen effektiven Fermionmode. Dafür ist keine direkte Endpunkt-Hopping-Wechselwirkung nötig. Dieser Dreierstern ist jedoch **kein Ausschnitt einer tatsächlichen nativen W-Zeile**.
2. **Ein tatsächlicher W-basierter Vierzustandskanal:** Im unveränderten 64-Fermion/60-Boson-Paartensor existiert ein exakt invariantes Vierzustandsystem, wenn ein **zusätzlicher reiner Bosonmischer** zwischen Kanal 0 und 1 zugelassen und ein bestimmter Zustand mit Gesamtladung 9 präpariert wird. Der vollständige native Hamiltonoperator plus dieser Mischer überträgt dort eine innere Fermionmarke mit einer streng abgesicherten Wahrscheinlichkeit von **mehr als 99,3 %**.

Das zweite Ergebnis benötigt keine Projektion, die die übrigen nativen Zustände künstlich wegschneidet: Der Vierzustandsraum ist unter allen 60 ursprünglichen Paaroperatoren plus dem Mischer exakt invariant. Es ist aber **weder eine Untersuchung der Entnahmeantwort des N=64-Grundzustands noch ein Transport zwischen zwei unabhängigen Banken**. Die Herkunft des Bosonmischers, die spezielle Präparation und die räumliche Bedeutung der Marken bleiben offen.

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

\[
\Pi_x=(-1)^{N_{f,x}},\qquad \Pi_y=(-1)^{N_{f,y}}
\]

gegeben. Kommutiert jede ausführbare lokale Operation und jeder einzelne realisierte Messzweig mit beiden Paritäten, gilt dies auch für beliebige Produkte, Summen, Adjungierte und starke beschränkte Grenzwerte. Eine Clockoperation, die lediglich innerhalb jeder Bank Fermionmoden zahlenerhaltend permutiert, bleibt in dieser Algebra.

Ein echter Einfermiontransfer erfüllt dagegen

\[
\Pi_x f_y^\dagger f_x=-f_y^\dagger f_x\Pi_x,
\qquad
\Pi_y f_y^\dagger f_x=-f_y^\dagger f_x\Pi_y.
\]

Er kann daher nicht allein durch mehr Kompositionen jener Operationen entstehen. Eine bloß paritätskovariante CP-Abbildung ist nicht die gleiche Voraussetzung: Sie kann ungerade Krauszweige besitzen. Die Aussage gilt nur für den ausdrücklich geraden ausführbaren Operationssatz.

Bei geteilten Fermionmoden sind die beiden lokalen CAR-Algebren von Anfang an nicht unabhängig. Liegt dieselbe Mode s in beiden, kann sie nicht zugleich als zwei unabhängige antikommutierende Kopien behandelt werden: \(\{s,s^\dagger\}=1\). Auch lokale Ladungen, die s doppelt mitzählen, sind keine unabhängigen additiven Bankladungen. Überlappung widerlegt somit den Paritätssatz nicht, sondern ändert seine Voraussetzungen.

## 2. Exakter CAR-Baustein aus einem geteilten Boson und Fermion

Betrachtet werden drei CAR-Moden \(f_x,s,f_y\), ein CCR-Boson b und

\[
Q_x=b^\dagger s f_x,\qquad Q_y=b^\dagger s f_y,
\qquad
H_\star=\Delta N_b+g(Q_x+Q_y+Q_x^\dagger+Q_y^\dagger).
\]

Der Ressourcenzähler

\[
K=N_b+n_s
\]

kommutiert mit allen diesen Operationen. Auf jedem exakten K-Sektor mit ganzzahligem \(K\ge1\) setze

\[
c^\dagger=\frac{b^\dagger s}{\sqrt K},\qquad
c=\frac{s^\dagger b}{\sqrt K}.
\]

Direkt aus CCR und CAR folgen

\[
(c^\dagger)^2=c^2=0,\qquad
\{c,c^\dagger\}=\frac{N_b+n_s}{K}=1.
\]

Die Mode c antikommutiert mit beiden Endpunktmoden. Ferner

\[
N_b=K-1+n_c,
\qquad
N_f+2N_b=2K-1+n_x+n_c+n_y.
\]

Damit gilt exakt

\[
\boxed{
H_\star=\Delta(K-1)+\Delta n_c
 +g\sqrt K\big(c^\dagger f_x+c^\dagger f_y+\mathrm{h.c.}\big).
}
\]

Die gewöhnliche Drei-Moden-Transferkette wurde hier aus einer überlappenden Paarumwandlung erhalten. Ein nützlicher Operatorausdruck derselben Tatsache ist

\[
\boxed{[Q_y^\dagger,Q_x]=K f_y^\dagger f_x.}
\]

Das ist zunächst eine Operatoridentität. Die Verfügbarkeit getrennter Kommutator-Kontrollsequenzen folgt daraus nicht automatisch. Schon der konstante Summen-Hamiltonoperator zeigt jedoch Transfer. Der minimale positive Ressourcensektor K=1 benötigt am Anfang eine besetzte gemeinsame Fermionmode s und ein leeres Boson.

### Vollständige Transferrechnung im Vergleichsmodell

Im effektiven Einteilchenraum und bei K=1 lautet die Matrix

\[
\begin{pmatrix}0&g&0\\g&\Delta&g\\0&g&0\end{pmatrix}.
\]

Der antisymmetrische Endpunktzustand ist dunkel. Der symmetrische koppelt mit \(\sqrt2g\) an c. Für \(g/\Delta=1/20\), \(m=101\) und

\[
t=\frac{202\pi}{\Delta\sqrt{51/50}}
\]

verschwindet die mittlere Besetzung wieder exakt. Die Zielwahrscheinlichkeit ist

\[
p_\star=\sin^2\left[\frac\pi2\,101\left(1-\sqrt{50/51}\right)\right].
\]

Durch Quadrieren rationaler Schranken erhält man

\[
\frac{199}{200}<101\left(1-\sqrt{50/51}\right)<1.
\]

Mit \(|\sin u|\le|u|\) und \(\pi<355/113\) folgt

\[
p_\star>1-\left(\frac{355/113}{400}\right)^2>0.9999.
\]

Diese Zahl gehört **nur zum Vergleichsmodell mit gemeinsamem b**.

### Die direkte Quellen-Grenze

Die tatsächliche native W-Zeile enthält jeweils acht disjunkte Fermionpaare, also 16 verschiedene Marken. Eine einzelne Zeile enthält deshalb niemals zugleich \(s f_x\) und \(s f_y\) mit \(x\ne y\). Das ist an allen 60 Zeilen exakt geprüft.

Ein gemeinsamer-b-Dreierstern darf somit nicht allein wegen der Form \(b^\dagger f f\) als nativer Baustein bezeichnet werden. Insbesondere wäre ein Wechsel von zwei Bosonkanälen zu einer gemeinsamen Mode ohne Kontrolle des orthogonalen Kanals eine zusätzliche Modellannahme.

## 3. Exakter Vierzustandskanal mit dem vollständigen nativen W

Die gepinnte Quelle ist

`universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz`,

SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die zwei relevanten Quellenzeilen sind

\[
\begin{aligned}
P_0={}&-f_{57}f_4+f_{56}f_5+f_{53}f_8-f_{52}f_9
       -f_{45}f_{16}+f_{44}f_{17}+f_{33}f_{28}-f_{32}f_{29},\\
P_1={}&-f_{58}f_4+f_{56}f_6+f_{54}f_8-f_{52}f_{10}
       -f_{46}f_{16}+f_{44}f_{18}+f_{34}f_{28}-f_{32}f_{30}.
\end{aligned}
\]

Die Konvention ist \(P_A=\sum_{i<j}W_{A,ij}f_jf_i\). Das gemeinsame aktive Fermion ist s=4; die Endpunktmarken sind 57 und 58.

Präpariert werden sieben unveränderte Pauli-Blocker

\[
S=\{8,16,28,32,44,52,56\}.
\]

Sei \(|S\rangle\) der geordnet erzeugte Fockzustand dieser Moden. Die vier Basiszustände sind

\[
\begin{array}{c|c|c}
\text{Zustand}&\text{besetzte Fermionmoden}&\text{Bosonen}\\\hline
L&S\cup\{4,57\}&0\\
B_0&S&1\text{ in Kanal }0\\
B_1&S&1\text{ in Kanal }1\\
R&S\cup\{4,58\}&0
\end{array}
\]

Jeder Zustand besitzt die native Gesamtladung \(N=N_f+2N_b=9\).

Zugelassen wird nun genau eine zusätzliche Hamiltonoperation,

\[
H_J=J(b_1^\dagger b_0+b_0^\dagger b_1).
\]

Alle ursprünglichen 60 nativen Paaroperatoren bleiben erhalten:

\[
H=\Delta N_b+g\sum_{A=0}^{59}(b_A^\dagger P_A+P_A^\dagger b_A)+H_J.
\]

Der Prüfer wendet sämtliche 480 signierten Paarkanäle einschließlich aller CAR-Vorzeichen und der Bosonfaktoren auf jeden der vier Zustände an. Es entstehen **keine Zustände außerhalb ihres linearen Spanns**. Die Pauli-Blocker verhindern insbesondere die sieben unerwünschten Rückpaarungen jedes aktiven Bosonkanals.

Es ergibt sich exakt

\[
\boxed{
H_4=\begin{pmatrix}
0&g&0&0\\
g&\Delta&J&0\\
0&J&\Delta&g\\
0&0&g&0
\end{pmatrix}_{(L,B_0,B_1,R)}.
}
\]

Ohne Mischer, J=0, zerfällt die Matrix in zwei getrennte 2×2-Blöcke. Dann ist \(\langle R|e^{-itH}|L\rangle\) zu jeder Zeit exakt null. Mit J ungleich null beginnt die Transferamplitude bei dritter Ordnung; die Wahrscheinlichkeit hat den führenden Term \(g^4J^2t^6/36\).

**Die Quelle enthält hier also die beiden Endstücke und eine exakt funktionierende Pauli-Blockierung, aber nicht die geprüfte Bosonverbindung als bereits verfügbare Operation.**

## 4. Strenge vollständige Transfergrenze im tatsächlichen W-Zeugen

Unter Spiegelung L↔R und B₀↔B₁ zerfällt H₄ in

\[
H_+=\begin{pmatrix}0&g\\g&\Delta+J\end{pmatrix},\qquad
H_-=\begin{pmatrix}0&g\\g&\Delta-J\end{pmatrix}.
\]

Wähle den vorhandenen Prüfquotienten \(g/\Delta=1/20\) und die ausdrücklich neu gesetzte Mischerstärke

\[
J=\Delta-\frac{2g}{\sqrt3}
 =\Delta\left(1-\frac1{10\sqrt3}\right),
\qquad t=\frac{\pi\sqrt3}{g}=\frac{20\pi\sqrt3}{\Delta}.
\]

Da \(0<J<\Delta\), bleiben die Eigenfrequenzen des Bosonmischers \(\Delta\pm J\) positiv. Es wurde **keine Nullfrequenz durch exakte Aufhebung von \(\Delta N_b\)** erzeugt. Auch auf dem ganzen Fockraum bleibt die hinzugefügte Hamiltonfamilie nach unten beschränkbar: Das Bosonquadrat ist strikt positiv und die endlichen Fermionoperatoren können durch quadratische Ergänzung kontrolliert werden. Das bedeutet nicht, dass ihr Grundzustand noch der unveränderte native Grundzustand ist.

Für H₋ ist \(\Delta-J=2g/\sqrt3\). Zu der gewählten Zeit kehrt dessen Endpunktkomponente exakt mit Phase −1 zurück, ohne mittlere Restbesetzung.

Für H₊ setze

\[
a=\Delta-\frac g{\sqrt3},\quad
\omega=\sqrt{a^2+g^2},\quad
w_- =\frac{1-a/\omega}{2}.
\]

Die Endpunktamplitude lautet

\[
A_+=(1-w_-)e^{i(\omega-a)t}+w_-e^{-i(\omega+a)t}.
\]

Mit \(\omega-a\le g^2/(2a)\), \(w_-\le g^2/(4a^2)\),
\(\cos u\ge1-u^2/2\) und
\(|A_+|^2\ge1-g^2/a^2\) folgt

\[
\begin{aligned}
p_{L\to R}
 &=\left|\frac{A_++1}{2}\right|^2\\
 &\ge1-\frac{g^4t^2}{16a^2}-\frac{g^2}{2a^2}\\
 &=1-\frac{3\pi^2+8}{6400(a/\Delta)^2}.
\end{aligned}
\]

Aus \(\sqrt3>17/10\) folgt \(a/\Delta>33/34\). Somit ergibt sich rein rational

\[
\boxed{
p_{L\to R}>
1-\frac{3(355/113)^2+8}{6400(33/34)^2}
=\frac{2009992727}{2022609600}
>0.9937620819>0.993.
}
\]

Die Aussage ist eine **analytische Schranke der vollständigen Dynamik auf einem exakt invarianten Quellen-Unterraum**. Es gibt hier keinen numerisch abgeschnittenen Restzustandsraum. Die 64-Fermion/60-Boson-Quelle ist nicht durch vier frei erfundene Matrixeinträge ersetzt worden: Ihre exakte Einschränkung wurde zuerst vollständig geprüft.

Die Zeit in Einheiten \(\hbar=1\) ist ungefähr \(108.83/\Delta\). Diese numerische Orientierung und die gesetzte Mischerstärke sind keine vorhergesagten Naturkonstanten.

## 5. Was dies für die fundamentale Suche ändert

Der konstruktive Anschluss ist klein: **Paarumwandlung → geteilte Zwischenressource → Paar-Rückumwandlung** kann einen Einfermion-Endpunktwechsel bewirken. Für die tatsächliche W-Quelle braucht man dazu weder einen neuen direkten Fermion-Hopping-Term noch die Kontrolle jedes einzelnen der 480 Paarmonome. Ein einzelner Bosonmischer plus eine spezielle Pauli-blockierte Präparation reicht im belegten internen Zeugen.

Offen bleiben aber genau die folgenden Herkunftsfragen:

1. **Operationssatz:** Ist der reine Mischer \(b_1^\dagger b_0+\mathrm{h.c.}\) tatsächlich verfügbar? Eine simultane Fermion-und-Boson-Symmetrie ist nicht automatisch eine unabhängige Bosonoperation.
2. **Präparation:** Wie wird der N=9-Blockerzustand mit dem zugelassenen Operationssatz erzeugt? Ladungserhaltende native Evolution präpariert ihn nicht aus dem N=64-Grundzustand.
3. **Operationaler Raum:** Sind die Endpunktmarken 57 und 58 überhaupt verschiedene räumliche Teile oder nur interne Marken derselben Bank? Die Rechnung allein liefert keine Raumposition.
4. **Gemeinsamer Grundzustand:** Besteht ein entsprechender Mechanismus für die ursprüngliche Entnahmeantwort des nativen N=64-Grundzustands, statt für diesen besonders präparierten Zeugen?
5. **Zwei Banken:** Eine Bosonverbindung zwischen wirklich unabhängigen Banken erhält deren lokale Fermionparitäten. Dieser interne Zeuge hebt jene Schranke nicht auf. Dafür wäre eine ursprünglich geteilte Fermionstruktur oder eine andere insgesamt gerade, lokal ungerade Quelloperation zu konstruieren.

T1-T8, das relativistische Feldwörterbuch und die Herkunft der Raumzeit sind damit nicht geschlossen. Das Ergebnis verkleinert eine konkrete Suche: Statt eines völlig beliebigen neuen Fermionlinks kann jetzt ein bestimmter Bosonmischer mitsamt seinem Quellen- und Präparationsvertrag geprüft werden. Die nachfolgende Quellenprüfung weist diesen Mischer jedoch ausdrücklich **nicht** als Synthese der bisher gewährten Kontrollen aus.

## 6. Anschluss des neuen Chart-/Glue-Vorschlags und exakter Quellen-No-go

Der neue Nutzeranhang vom 15. September 2026 wurde vollständig gelesen:

`/Users/stefanhamann/.codex/attachments/59dc0059-8914-48ca-953d-85933f66e00b/pasted-text.txt`,

SHA-256 `1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

Die Hypothese, Banken zunächst als überlappende lokale Beschreibungen einer gemeinsamen CAR-Struktur zu untersuchen, passt zum hier konstruierten gemeinsamen Fermion-/Boson-Zwischenraum. **Sie löst den Übergang von Überlappung zu Dynamik aber nicht automatisch.** Bereits zwei nichtorthogonale lokale Moden \(f_A=f_1\), \(f_B=\cos\theta f_1+\sin\theta f_2\) bei H=0 besitzen ein nichtverschwindendes Kreuz-Antikommutator \(\{f_A,f_B^\dagger\}=\cos\theta\), obwohl überhaupt keine Zustandsentwicklung stattfindet. Eine Änderung der Beschreibung und ein dynamischer Transfer müssen getrennt geprüft werden.

### 6.1 Eine nötige Korrektur des vorgeschlagenen Paritätstests

Der Anhang fordert für überlappende Charts einen Intertwiner, der lokal Paritäten ändert, aber mit \(\Pi_A\Pi_B\) kommutiert. **Bei Überlappung ist dieses Produkt nicht automatisch die Gesamtparität.** Im kleinsten gemeinsamen-Moden-Zeugen

\[
A=\{x,s\},\qquad B=\{s,y\}
\]

gilt

\[
\Pi_A\Pi_B=(-1)^{n_x+n_y},
\qquad
\Pi_{\rm global}=(-1)^{n_x+n_s+n_y}.
\]

Die gemeinsame Mode s wurde im Produkt zweimal gezählt und fällt heraus. Die Paarumwandlung \(b^\dagger s f_x\) ist bezüglich \(\Pi_{\rm global}\) gerade, kommutiert aber nicht mit \(\Pi_A\Pi_B\). Der vorgeschlagene Kill-Test würde hier einen legitimen global geraden Überlappungsmechanismus fälschlich aussortieren. Alle vier Identitäten wurden auf dem vollständigen Drei-Fermion-CAR-Raum exakt geprüft.

**Der korrigierte Test muss die globale Parität aus der gemeinsamen CAR-Darstellung selbst verwenden**, nicht aus einem ungeprüften Produkt lokaler Paritäten. Zusätzlich benötigt er eine definierte Anfangspräparation, dynamisch unterschiedliche Endpunktbeobachtungen und einen aus der Quelle stammenden Generator. Passive Chartwechsel allein reichen nicht.

### 6.2 Tatsächlicher endlicher Clock statt unterstellter voller Gruppe

Die Prüfung lädt den gepinnten ursprünglichen Clock-Konstruktor über

`sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py`,

SHA-256 `2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994`.

Der Konstruktor kontrolliert seine ursprünglichen Quellenpins und die exakte W-Kovarianz. Er liefert tatsächlich

\[
p=(2,0,1,4,3),\qquad s_{\rm Clock}=-1,
\]

und auf Bosonmoden \(A=6k+c\)

\[
G_B e_{6k+c}=-e_{6(p(k\bmod5)+5\lfloor k/5\rfloor)+c}.
\]

Es wird **nicht** vorausgesetzt, dass der Clock der volle Spin(10)×SU(4)-Operationssatz ist. Sein endlicher, direkt reproduzierter Lift reicht für den folgenden Ausschluss.

Schreibe \(M_{ij}=|i\rangle\langle j|+|j\rangle\langle i|\) auf dem Boson-Einteilchenraum. Exakt gilt

\[
G_BM_{01}G_B^\dagger=M_{12,13},\quad
G_BM_{12,13}G_B^\dagger=M_{6,7},\quad
G_BM_{6,7}G_B^\dagger=M_{01}.
\]

Insbesondere

\[
\|[G_B,M_{01}]\|_F^2=4\ne0.
\]

Die native W-Kovarianz impliziert \([G,H]=[G,N_b]=0\) für den gemeinsamen Fock-Lift G. Auch ein gewährter getrennter Gesamt-Casimir von Spin(10) oder SU(4) kommutiert mit diesem tatsächlichen G. Daher liegt

\[
\operatorname{Alg}(H,N_b,G,C_{\rm Spin},C_{\rm Color})\subset\{G\}'
\]

und der spezifische Einzelmischer \(b_1^\dagger b_0+\mathrm{h.c.}\) liegt **nicht** in dieser erzeugten Algebra. Auf den endlichen Ladungssektoren gibt es dabei keine Domänenprobleme; für die volle Hilbert-Darstellung formuliert man dieselbe Aussage mit den erzeugten beschränkten Zeitentwicklungen und Spektraloperationen.

### 6.3 Clock-Mittelung ist möglich, aber der Farb-Cartan sperrt sie weiterhin

Der Clock-Ausschluss allein wäre zu schwach. Die Orbitsumme

\[
M_{\rm orb}=M_{01}+M_{12,13}+M_{6,7}
\]

kommutiert exakt mit \(G_B\). Ihre beiden zusätzlichen Linkblöcke wirken auf den vier Zuständen aus Abschnitt 3 null. Ein neu zugelassener globaler Bosonmischer \(J b^\dagger M_{\rm orb}b\) erzeugt deshalb **denselben** exakt invarianten Vierzustandskanal und dieselbe Transfergrenze. Ein neuer globaler Zusammenhang muss also nicht zwingend den endlichen Clock brechen.

Es gibt jedoch einen zweiten, stärkeren gemeinsamen Erhaltungssatz. Aus dem tatsächlichen Quell-Gewichtswörterbuch wählen wir die zweite SU(4)-Cartankomponente und definieren den gemeinsamen Ladungsoperator

\[
Q=\sum_r q_r n_{f,r}+\sum_A q_A n_{b,A}.
\]

Jeder ursprüngliche Paarterm erfüllt exakt \(q_i+q_j=q_A\); dies wird für alle 480 Quellenpaare geprüft. Der tatsächliche Clock wirkt auf dem Spinindex und lässt die SU(4)-Farbkomponente unverändert. Daher

\[
[Q,H]=[Q,N_b]=[Q,G]=0.
\]

Die getrennten Gesamt-Casimire kommutieren ebenfalls mit diesem Cartan. Diese Aussage erfordert **keine** Verfügbarkeit aktiver kontinuierlicher SU(4)-Kontrollen.

Auf den beiden Bosonkanälen gilt dagegen

\[
q_0=0,\qquad q_1=2,
\]

und auf dem ganzen Boson-Einteilchenraum

\[
\|[Q_B,M_{01}]\|_F^2=8,\qquad
\|[Q_B,M_{\rm orb}]\|_F^2=24.
\]

**Damit sind sowohl der Einzelmischer als auch seine Clock-invariante Orbitsumme aus dem genannten Operationssatz ausgeschlossen.** Die Mittelung beseitigt das Clock-Hindernis, nicht den separaten Farb-Cartan-Erhaltungssatz.

Die tatsächlichen Cartanladungen im Vierzustandsraum sind

\[
(Q_L,Q_{B_0},Q_{B_1},Q_R)=(7,7,9,9).
\]

Dieser Zeuge verändert also eine innere SU(4)-Quantenzahl. Er ist noch deutlicher als ein bloßer Markenwechsel vom Transport **derselben** niedrigenergetischen Fermionmode zwischen zwei räumlichen Banken zu unterscheiden.

### 6.4 Kleinste noch zu suchende Quellressource

Für den hier exakt spezifizierten Zeugen fehlt mindestens eine Operation, die nicht mit dem betrachteten Farb-Cartan des ursprünglichen Systems kommutiert, oder eine aus einer erweiterten globalen Quelle abgeleitete Kopplung mit einer **expliziten Ausgleichsressource für diese Cartanladung**. Ein zusätzlicher aktiver SU(4)-Generator wäre ein neuer Operationsvertrag; außerdem bewegt sein simultaner Fermion-/Boson-Lift im Allgemeinen auch die Blocker und ist nicht mit dem reinen Bosonmischer gleichzusetzen.

Die Befunde schließen nicht alle globalen Glue-Modelle aus. Sie zeigen präzise, warum der konkret schon gelöste Vierzustandstransfer noch keine Herkunftslösung ist und welche neue algebraische Eigenschaft eine echte Quellenfortsetzung besitzen müsste. Für eine überwiegend kinematische Chart-Interpretation muss zusätzlich gezeigt werden, dass diese Erweiterung eine tatsächliche Dynamik und nicht bloß eine Basisumbenennung erzeugt.

## Reproduktion und Status

`verify.py` prüft **307 Bedingungen**, verwendet keine Python-Assertions und reproduziert normal sowie mit `-OO` byteidentische JSON-Ergebnisse. Die Prüfung enthält:

- CAR und Ladungsbuchhaltung für den geteilten Baustein in K=1,2,3;
- die rationale Transfergrenze des klar getrennten Vergleichssterns;
- die Matching-Eigenschaft aller 60 nativen W-Zeilen;
- die volle symbolische Wirkung aller 480 nativen Paarterme auf alle vier Zeugen-Zustände;
- die zusätzliche Mischerwirkung, exakte Invarianz und vollständige Spiegelungszerlegung;
- die rationale Schranke größer 99,3 % bei strikt positiver Bosonfrequenz.
- den tatsächlich konstruierten Clock, den Einzelmischer-Ausschluss und die Clock-invariante Orbitsumme;
- die gemeinsame Farb-Cartan-Erhaltung aller Quellenpaare und den präzisen Ausschluss beider Mischinstrumente;
- das Gegenbeispiel gegen die Gleichsetzung lokaler Paritätsprodukte mit der globalen Parität bei überlappenden Charts.

Die analytischen Ungleichungen sind im Text hergeleitet; die Anzahl der Tests ist kein Ersatz für diese Herleitung und keine Anzahl gelöster Physikprobleme.


---

# Anhang D: vollständiger Überlappungs-Audit

# Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Der unveränderte Anhang liegt in `attachment.txt`, SHA-256:

`1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

`check_overlap.py` enthält 38 exakte kleine Prüfbedingungen. `replay.py` kopiert den Anhang unverändert, prüft seine SHA vor und nach der Rechnung und reproduziert normale und optimierte Checker-Ausgabe byteidentisch. Alle Schreibvorgänge bleiben in diesem neuen Auditordner. Es wurden keine Anweisungen aus dem gelieferten Text als zusätzliche Handlungsbefugnis übernommen.

## 1. Was die neue Perspektive sinnvoll beiträgt

Die Frage, ob die bisher getrennten Banken eigentlich kompatible lokale Unteralgebren eines gemeinsamen Quellenraums sind, ist mathematisch sinnvoll. Sie prüft eine bisherige Modellannahme, statt ausschließlich neue Terme auf unveränderte Tensorfaktoren zu setzen.

Eine solche Konstruktion könnte erklären, welche lokalen Observablen, Zustände und Operationen zusammengehören. Sie müsste jedoch aus demselben Compiler stammen und nicht erst nach dem gewünschten Transport ausgewählt werden. »Zustände, Operationen, Überlappungen, Phasen und Komposition« beschreibt zunächst eine große Klasse quantenmechanischer Modelle; diese Sprache identifiziert allein noch kein eindeutiges fundamentales Objekt und erzwingt keine TOE.

Die bisher bewiesenen lokalen Pole und die bedingte Zwei-Banken-Übertragung bleiben wertvolle Vergleichsziele. Ihre Beweise gelten aber für den dort erklärten Hilbertraum-, Hamilton- und Parametervertrag. Ersetzt man unabhängige Banken durch überlappende CAR-Unterräume, ändern sich Kreuzrelationen, Ladungszuordnung und im Allgemeinen der gemeinsame Grundzustand. Die früheren Zwei-Banken-Wahrscheinlichkeitsgrenzen dürfen dann nicht unverändert übernommen werden.

## 2. Exakter Zwei-Moden-Gegenbeleg zum vorgeschlagenen Paritätstest

Seien c₁,c₂ zwei orthogonale CAR-Moden. Setze

`a=c₁`, `b=(c₁+c₂)/√2`.

Jeder Chart ist für sich ein gültiger Einmoden-CAR-Raum, aber

`{a,b†}=I/√2`.

Die beiden Charts sind also keine unabhängigen Fermionfaktoren. Definiere ihre lokalen Paritäten

`Π_A=I−2a†a`, `Π_B=I−2b†b`.

In der Besetzungsbasis `|00>,|10>,|01>,|11>` ist die wirkliche globale Parität

`Π_global=diag(1,−1,−1,1)`.

Das Produkt der lokalen Paritäten lautet dagegen

```
Π_A Π_B = [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0,-1, 0, 0],
           [0, 0, 0, 1]].
```

Es ist weder die globale Parität noch hermitesch, und sein Quadrat ist nicht die Identität. Auch `[Π_A,Π_B]≠0`.

Der vorgeschlagene Test `[U_AB,Π_AΠ_B]=0` charakterisiert deshalb bei solchen Überlappungen **keine globale Geradheit**. Das lässt sich noch direkter widerlegen: Der Hamiltonoperator

`H=a†a+b†b`

ist global gerade, kommutiert mit keiner der beiden lokalen Paritäten und auch nicht mit ihrem Produkt. Sein Cayley-Transform

`U=(I−iH)(I+iH)⁻¹`

ist eine exakt unitäre, global gerade Operation mit denselben drei Nichtkommutationen. Der im Anhang vorgeschlagene Kill-Test würde diese zulässige globale Operation fälschlich ausschließen.

Die richtige Reihenfolge ist daher: zuerst die gemeinsame CAR-Einbettung und ihre echte globale Graduierung bestimmen. Erst danach lässt sich entscheiden, welche lokalen Paritätskriterien anwendbar sind. Bei einer disjunkten orthogonalen Zerlegung gilt die gewohnte Produktformel; bei überlappenden Charts im Allgemeinen nicht.

## 3. Noch wichtiger: Ein Überlappungsmatrixelement ist kein Transport

Für dieselben zwei Moden seien

`|A>=a†|0>`, `|B>=b†|0>`.

Dann ist ihre Gram-Matrix

`S=[[1,1/√2],[1/√2,1]]`.

Wähle den vollkommen trivialen Hamiltonoperator `H₀=ωN`, mit `N=c₁†c₁+c₂†c₂`. Die Matrix der Hamilton-Matrixelemente in diesen beiden Chartvektoren ist

`K_ij=<i|H₀|j>=ω S_ij`.

K hat also eine nichtverschwindende Offdiagonale, obwohl auf dem gesamten Einteilchenraum nur dieselbe Phase `e^(−iωt)` entsteht. Das korrekte Eigenproblem ist `Kv=E Sv`, nicht `Kv=Ev`. Es liefert ausschließlich die entartete Energie ω. Die Wahrscheinlichkeit

`|<B|exp(−itH₀)|A>|²=1/2`

ist für jede Zeit gleich groß. Es hat keine Übertragung stattgefunden; die Hälfte war schon bei t=0 als statische Überlappung vorhanden.

Das ist unmittelbar für den bisherigen nativen TFPT-Pol relevant. Dieser besitzt im erklärten N=63-Vertrag eine einzelne Energie E_h auf einem 64-dimensionalen Polraum:

`P_h H P_h = E_h P_h`.

Sind A und B lediglich zwei Beschreibungen oder Sonden innerhalb desselben Polraums, gilt wiederum `K=E_h S`: ein gemeinsamer Phasenfaktor, keine durch H verursachte Ausbreitung zwischen den Marken. Diese Aussage braucht keine große Diagonalisierung. Sie folgt allein aus der bereits bewiesenen Entartung.

Ein passiver Chartwechsel verändert nur die Beschreibung. Ein aktiv implementierter Rotationsoperator kann Zustände verändern; dann müssen jedoch genau dieser Operator, seine physische Verfügbarkeit, Zeit- oder Ressourcenskala und sein Instrument aus der Quelle nachgewiesen werden. Das ist nicht durch den Namen »Intertwiner« erledigt.

Die mögliche globale Überlappungskonstruktion ist dadurch nicht ausgeschlossen. Sie müsste tatsächliche zusätzliche globale Dynamik beziehungsweise eine Bandaufspaltung aus der Quelle zeigen und die lokalen Polbeweise darin erneut absichern.

## 4. Chartwechsel, Verbindungen und Krümmung sind verschiedene Daten

Wenn mehrere Charts lediglich vollständige orthonormale Rahmen R_x desselben festen Vektorraums sind, lauten die Basiswechsel

`U_xy=R_x† R_y`.

Dann teleskopiert jedes Dreiecksprodukt:

`U_12 U_23 U_31=I`.

Das gilt auch bei nichtkommutierenden R_x; der Checker prüft ein konkretes solches Beispiel. Durch bloße lokale Basiswahl entsteht daher nicht automatisch ein physisch gekrümmtes Eichfeld. Auf einem Bündel beschreiben Übergangsfunktionen seine Verklebung; eine Verbindung enthält zusätzliche Paralleltransportdaten. Eine nichttriviale Bündeltopologie ist ebenfalls nicht dasselbe wie bereits gewählte lokale Krümmung.

Bei tatsächlich variierenden **echten Unterräumen** ist die Situation interessanter. Überlappungen `ι_x†ι_y` müssen dann nicht unitär sein. Drei Strahlen `(1,0)`, `(1,1)/√2`, `(1,i)/√2` besitzen das nichtreelle Schleifenprodukt `(1+i)/4`. Das liefert eine geometrische Phase, aber sein Betragsquadrat ist 1/8 und nicht eins. Eine solche Unterraumgeometrie kann Ansatzpunkt für eine geometrische Verbindung sein; sie ist kein automatisch ausgeführter normerhaltender Transport und keine schon gewonnene Eichfeldkinetik.

Zudem legt eine interne Eichverbindung alleine keine Raumzeitmetrik fest. Verschiedene Linkphasen können auf demselben Graphen bei denselben Operationskosten existieren. »Die U_xy ändern sich« bedeutet ohne weiteren Nachweis nicht bereits »die Raumzeitgeometrie ändert sich«.

## 5. Zeit: Ein Grundzustand bewegt sich unter seinem H nicht beobachtbar

Die im Anhang skizzierte Entwicklung `Ω -> exp(−itH)Ω` erzeugt bei einem Energieeigenzustand lediglich `exp(−itE₀)Ω`. Der Dichteoperator bleibt exakt gleich. Der Checker bestätigt das an einem kleinen Fockzustand.

Damit wird weder die Zeitordnung noch ein Zeitpfeil erzeugt. Nichtstationäre Zustände und mehrzeitige Korrelationsfunktionen können natürlich eine Dynamik anzeigen; eine gerichtete Record- oder Präparationsgeschichte braucht ihre eigenen Bedingungen. Auch eine relationale Zeit aus bedingten Zuständen wäre als Forschungsansatz möglich, verlangte aber eine explizite Uhr, ihren gemeinsamen Zustand mit dem System und eine Konditionierungsregel. Der bloße globale Eigenzustandsphasenfaktor reicht dafür nicht.

Die nun geprüfte endliche Clock kann eine aktive Operation auf inneren Marken darstellen, falls sie physisch gewährt ist; dass sie zur Quellsymmetrie gehört, macht sie nicht automatisch identisch mit der Hamiltonzeit.

## 6. Der binäre Index muss als Freiheitsgrad bewiesen werden

Die skalare Hilfsdublett-Reparatur braucht zwei unabhängige, gleichgeladene Komponenten, auf denen eine nichtentartete antisymmetrische Form wirkt. Eine Orientierung der Überlappungsgeometrie **könnte** so etwas liefern, tut es aber nicht allein durch das Vorhandensein zweier Bezeichnungen.

Die drei einfachen Verwechslungen sind:

- Zwei Namen oder ±-Vorzeichen für dieselbe Mode bilden nur eine eindimensionale, redundante Beschreibung. Der Rückzug der antisymmetrischen Zweiform auf diesen Raum ist null.
- Ist Rückwärts die Adjungierte der Vorwärtsoperation, haben f und f† entgegengesetzte U(1)-Ladungen. Das ist kein gleichgeladenes Hilfsdublett. Ihr bilinearer Kanal ist neutral, nicht von Ladung −2.
- Bedeutet Vorwärts/Rückwärts links-/rechtshändige Weylfelder, wurden zwei verschiedene Lorentzdarstellungen eingeführt. Das ist nicht die zusätzliche gleichartige Hilfskopie des bereits geprüften Tensorvertrags.

Eine geometrisch hergeleitete Zweifachheit könnte also eine gute Erklärung des Hilfsindex sein. Nötig wären zwei tatsächliche unabhängige Kanäle, ihre CAR-/Ladungsrelationen, die Spin-Lorentz-Wirkung und die nichtverschwindende Kopplung auf demselben Quellraum. Ein Orientierungsbit liefert weder automatisch Weylspin noch die Transformationsregel unter einer vollen Lorentzdrehung.

## 7. Operationsgeometrie benötigt mehr als Erreichbarkeit

Minimale Kosten erfüllen unter geeigneter Komposition eine Dreiecksungleichung. Ohne reversible Operationen mit symmetrischen Kosten ist die resultierende Funktion jedoch nur eine gerichtete Distanz; der Checker liefert den gerichteten Dreierzyklus mit `d(A,B)=1`, `d(B,A)=2`. Unerreichbarkeit ergibt unendliche Distanzen. Kostenfreie Chartwechsel können verschiedene Beschreibungen auf Distanz null setzen; dann muss zunächst nach physischer Äquivalenz quotiert werden.

Wachstum `V(R)~R³` ist ein Nachweis einer dreidimensionalen **Wachstumsdimension im gewählten Kostenmaß**, nicht automatisch einer glatten dreidimensionalen Mannigfaltigkeit, einer 3+1D-Lorentzmetrik oder einer universellen Lichtgeschwindigkeit. Schon ein kubisches Gitter mit Laplace-Hamiltonoperator hat dieses Volumenwachstum, aber bei kleinen Impulsen

`E(k)=Σ_j(2−2cos k_j) ~ |k|²`,

nicht eine lineare relativistische Dispersion. Der eindimensionale Taylor-Koeffizient dieser separierbaren Gegenkonstruktion wird exakt geprüft.

Eine lokale Spektrallücke ist ebenso noch keine relativistische Teilchenmasse. Dazu braucht es die gemeinsame Energie-/Impulsdeutung, den entsprechenden Dispersionszweig und den Ladungs-/Referenzvertrag. »Kopieren« sollte bei Teilchenpropagation nur bildlich verwendet werden: kohärenter Transfer erzeugt nicht zwei unabhängige Kopien eines unbekannten Quantenzustands.

## 8. Gravitation bleibt eine dynamische Verpflichtung

Die linearen Fluktuationen einer aus der Quelle bestimmten globalen Geometrie zu prüfen, ist ein sinnvoller Forschungsauftrag. Eine transversale spurfreie Tensorzerlegung allein garantiert aber weder einen masselosen physikalischen Spin-2-Pol noch positive Norm, genau zwei Helizitäten oder universelle Kopplung. Selbst ein gesunder linearer Spin-2-Sektor ersetzt nicht den Nachweis seiner nichtlinearen Eich-/Zwangsstruktur und konsistenten Materiekopplung.

Das vorgeschlagene wechselseitige Schema Materie -> bevorzugte Überlappungen -> Geometrie ist daher ein mögliches Wirkungsprinzip, noch keine aus dem vorhandenen nativen H gewonnene Gleichung.

## 9. P versus NP: eine konkrete Korrektur

Der Anhang sagt, P≠NP würde einen intrinsisch exponentiellen Suchaufwand bedeuten. Das ist falsch. P≠NP würde ausschließen, dass **jedes** NP-Entscheidungsproblem deterministisch in Polynomialzeit gelöst werden kann. Es folgt daraus keine exponentielle untere Schranke: Eine hypothetische Laufzeit wie `2^(√n)` ist superpolynomiell und zugleich subexponentiell. Stärkere Exponentialzeitaussagen benötigen zusätzliche Sätze beziehungsweise Hypothesen.

NP bezieht sich zudem auf polynomial lange, polynomial prüfbare Zertifikate in der Länge einer wohldefinierten Eingabekodierung. Beliebige Erreichbarkeit in einem knapp beschriebenen Graphen mit möglicherweise exponentiell langen Wegen ist nicht allein deshalb ein NP-Problem. Eine geometrische Umformulierung muss Eingabelänge, Zertifikatlänge, erlaubte Operationen und deren Kosten erhalten. Eine Pfadmetapher löst diese Verpflichtungen nicht.

## 10. Ein korrigierter, wirklich entscheidbarer Anschluss-Test

Ein sinnvoller nächster Versuch besteht nicht nur aus einem unbeschrifteten `P U_AB P`. Er sollte zusammen liefern:

1. **Globale Quelle und Einbettungen:** konkrete primitive Algebra und zwei CAR-/Tensor-erhaltende Abbildungen; alle Kreuzrelationen und die tatsächliche globale Graduierung.
2. **Gemeinsamer Zustand:** derselbe globale H und Zustand; Nachweis, welche bisherigen lokalen Pole und Lücken darin noch gelten. Kein stiller Rückgriff auf den Produktgrundzustand unabhängiger Banken.
3. **Physische Operation:** aus einem erklärten Quellenwort erzeugter aktiver Operator oder Generator, mit Zeit- beziehungsweise Ressourcenskala. Passive Chartwechsel bleiben getrennt.
4. **Gram-bereinigte Dynamik:** `S_ij=<h_i|h_j>` und `K_ij=<h_i|H|h_j>` berechnen; das generalisierte Eigenproblem beziehungsweise eine orthonormalisierte Darstellung verwenden. Prüfen, ob mehr als `K=E_h S` entsteht.
5. **Operativer Transfer:** dieselbe Anfangspräparation und Zielmessung; zeitabhängige Änderung gegenüber der statischen Überlappung und Fehlerkontrolle gegenüber dem übrigen Zustandsraum. Erst dann mit dem bekannten bedingten Zwei-Banken-Transfer vergleichen.

Das nimmt die mögliche gemeinsame Herkunft ernst, korrigiert aber die falschen Automatismen. Der stärkste sofortige Erkenntnisgewinn dieses Audits ist negativ und präzise: **Allein durch Überlappung oder Umbenennung eines entarteten nativen Polraums entsteht keine Transportdynamik.** Ob der Compiler darüber hinaus genau die passende globale Dynamik besitzt, ist die konkrete offene Frage.


---

# Anhang E: arithmetischer Schleifenvorschlag

# Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

15. September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes
`59dc0059-8914-48ca-953d-85933f66e00b`, kein neuer RH-Beweis und kein neuer
arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale
Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## Urteil

**Ein globaler Wegraum ist eine sinnvolle Suchklasse; ein Eulerprodukt über
primitive Wege ist noch nicht das Eulerprodukt der Riemannschen Zetafunktion.**
Die im Text vorgeschlagene Xi-Determinante bleibt ein hinreichendes Ziel unter
expliziten Operatorannahmen. Das Umbenennen ihres noch fehlenden Operators in
„Generator der primitiven Schleifen“ konstruiert ihn nicht.

## 1. Was die endliche Bank tatsächlich ausschließt

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator
mit 64 Fermion- und 60 Bosonmoden, Δ>0. Der Hilbertraum ist wegen der Bosonen
**nicht endlichdimensional**. Endlich ist die Zahl der Moden. Mit
`C=960g²/Δ` folgt aus quadratischem Ergänzen

\[
H\ge\frac\Delta2N_b-C,
\qquad
N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60}.
\]

Dies widerspricht einem vollständigen energieerhaltenden Spektrum
`E_* log n + E_off`, E_*>0, weil dessen Zählfunktion exponentiell wächst.
Es ist kein Ausschluss beliebiger arithmetischer Untersektoren oder eines
anderen Operators mit nichtlinearer Energiezuordnung.

Ein großer Wegraum kann eine andere Zählfunktion besitzen. Die Gleichsetzung
„mehr Wege = mehr orthogonale Zustände unter derselben Energie“ muss aber
bewiesen werden. Verschiedene Wörter können denselben Operator oder Zustand
darstellen; ein Quantenüberlagerungsraum ist nicht ohne Weiteres der freie
Wortraum. Bei unendlich vielen identischen Zellen kann stattdessen die globale
Wärmespur divergieren. Der Text entfernt diese Fragen nicht durch Vergrößerung.

## 2. Der kleinste Gegencheck zur Primzahl-Automatik

Nehmen wir einen gerichteten Knoten mit zwei erlaubten Schleifen a und b.
Neben a und b ist auch ab ein primitiver periodischer Weg: Es ist keine Potenz
eines kürzeren Wortes. Ebenso entstehen weitere gemischte primitive Wörter.
Setzen wir nachträglich L(a)=log 2, L(b)=log 3, so hat ab die Länge log 6.
Die 6 ist keine Primzahl. „Primitiver Weg“ bedeutet nicht „arithmetische
Primzahl“.

Schon formal unterscheiden sich die zugehörigen erzeugenden Funktionen:

\[
Z_{\rm Wege}(x,y)=\frac1{1-x-y},\qquad
Z_{\rm zwei\ Primarten}(x,y)=\frac1{(1-x)(1-y)}.
\]

Der Koeffizient von xy ist links 2 und rechts 1. Links werden die beiden
Wörter ab und ba gezählt; rechts eine kommutative Besetzung. Im periodischen
Eulerprodukt bilden ab und ba eine zyklische Klasse, aber diese ist ein
**neuer primitiver Faktor**. Die Abweichung verschwindet damit nicht.

Eine kommutative freie Halbgruppe über vorgegebenen Primarten reproduziert
eindeutige Faktorzerlegung. Sie leitet aber weder die natürliche arithmetische
Markierung noch die logarithmischen Längen oder die passende Spur her.
Eine gekoppeltere Geometrie müsste gemischte Bahnen mit den richtigen
Amplituden, Relationen oder nachgewiesenen Auslöschungen behandeln. Dies ist
kein allgemeiner Ausschluss von Schleifenmodellen mit Interferenz.

Der Unterschied ist in den Originalarbeiten sichtbar: Kuipers, Hummel und
Richter konstruieren Quantengraphen mit dem passenden oszillierenden Anteil
der Nullstellendichte, weisen aber auf den anderen glatten Anteil und damit
das andere Spektrum hin. Das ist ein nützlicher Vorläufer, kein RH-Operator.
[Originalarbeit, Phys. Rev. Lett. 112, 070406](https://arxiv.org/abs/1307.6055)

Graphische Eulerprodukte besitzen ihre eigene Theorie. Auch eine aus einer
Graph-Zetafunktion bestimmbare Größe ist nicht automatisch effizient auslesbar.
Storm trennt in seiner Arbeit ausdrücklich berechenbare Zeta-Darstellung und
teure Auswertung bestimmter Graphinformationen.
[Originalarbeit zu Edge-Zetafunktionen](https://arxiv.org/abs/0708.1923)

## 3. Die richtige RH-Zielbedingung

Sei A strikt positiv und selbstadjungiert, mit kompakter Inverser und
`A^{-2}` von Spurklasse. Dann ist der Fredholm-Ausdruck

\[
D(z)=\det(I-z^2A^{-2})
\]

ganz, und seine Nullstellen liegen bei den reellen Zahlen ±λ_j(A), mit ihren
Multiplizitäten. Würde unabhängig und auf ganz C bewiesen

\[
\Xi(z)/\Xi(0)=D(z),\qquad \Xi(z)=\xi(1/2+iz),
\]

so folgte RH. Das ist die korrekte bedingte Implikation. Nicht ausreichend
sind ein paar passende Eigenwerte, die imaginären Teile bereits eingesetzter
Nullstellen, ein Eulerprodukt nur für Re(s)>1 oder eine Formaldeterminante ohne
Domäne, Spurklasse und vollständige archimedische Faktoren.

Der vorgelegte Text liefert A nicht, bestimmt keine Domäne und leitet weder
die vollständige Spurformel noch die ganze Funktionsidentität her. Die
allgemeine Selbstadjungiertheit eines anderen Operators hilft dabei nicht.

## 4. Vorarbeiten und aktuelle Grenze der Quellenprüfung

Der installierte Leitfaden `rh-graph-research` und die projektspezifische
Korpussuche wurden angewandt. Die aktuelle Konsistenzprüfung und der
anschließende Wiederaufbauversuch brachen mit

`SOURCE_UNAVAILABLE: /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`

ab. Die gesonderte Paper-Abfrage meldete `PAPER_SOURCE_OR_REVIEW_DRIFT`.
Keine dieser Prüfungen wurde durch Ersetzen von Pins grün gemacht. Der
Forschungsindex darf hier **nicht als global aktuell geprüft** bezeichnet
werden. Vorhandene Suchresultate dienten lediglich zum Auffinden real
verfügbarer Originaldateien; die aktuelle Queue ist keine Beweisquelle.

Gezielt gelesen wurden die relevanten Abschnitte von
`rh/catalog/analysis/geometry_audit.md` (Quantengraphen) und
`rh/catalog/analysis/event_log_function.md` (arithmetische Ereignisse), sowie
die vollständige maßgebliche Zählungs-/Determinantenpassage aus v1.6.5.
Die Dateien werden für diese Revision eingefroren. Ihre historischen
Korpus-Abwesenheitsangaben werden nicht als aktueller Vollständigkeitsbeweis
übernommen.

Im bestehenden Index berühren `r618 / STRUCTURAL_MISMATCH` die Verwechslung
RH-neutraler E8-Daten mit einer Xi-Identität und
`ledger:E8.COXETER.EULER.COMPLETION.01 / NO_BRIDGE` die fehlende globale
Vervollständigung. Solche Treffer allein widerlegen kein neues Objekt; die
hier tragende Prüfung ist der explizite Unterschied zwischen gemischten
primitiven Wegen und arithmetischen Primarten. Es wird kein neuer globaler
RH-Beweisstatus registriert oder freigegeben.

## 5. Tragfähiger Anschluss, ohne acht Versprechen an ein unbekanntes Objekt

Der nächste arithmetische Test wäre erst nach Definition einer tatsächlichen
Quell-Wegstruktur sinnvoll: primitive Bahnen, ihre Längen, Amplituden und die
Spur gemeinsam bestimmen, ohne Primlisten oder Nullstellen einzusetzen.
Ein positiver Kontrolltest muss insbesondere gemischte Zyklen erklären und
den archimedischen Anteil auf demselben Träger liefern. Gelingt nur ein
generisches Graph-Eulerprodukt, ist das ein Graphresultat und bleibt von RH
getrennt.

Faktorisierung und P versus NP werden dadurch nicht gelöst. Außerdem ist
„P≠NP bedeutet notwendigerweise exponentielle Suchkosten“ zu stark: Aus einer
fehlenden polynomialen Zeitgrenze folgt nicht allein eine exponentielle
untere Schranke. Für Hylæan enthält der Text ein mögliches Operationsbild,
aber keinen neu überprüften Lern- oder Gedächtnisnachweis.


---

# Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

# TFPT / Universalraum: kontrollierter Zwei-Banken-Transfer

Forschungsfortsetzung und Quellenaudit · 15. September 2026 · v1.6.5

## Ergebnis und Geltungsbereich

Eine konkrete bisher offene Rechnung lässt sich schließen: **Im ausdrücklich
um einen Rotor-Link erweiterten Modell zweier nativer Fermion-Boson-Banken
ist der Transfer der isolierten Lochanregung mit einer Fehlergrenze gegenüber
dem vollständigen physikalischen Zustandsraum kontrollierbar.** Dafür ist
keine Diagonalisierung dieses enorm großen Raums nötig. Die vorhandene
Casimiridentität, Ladungserhaltung und eine Spektrallücke reichen aus.

Am unten vollständig angegebenen, bewusst sehr schwachen Kopplungspunkt gilt:

| Aussage | Strenge Schranke | Status |
|---|---:|---|
| Zielwahrscheinlichkeit aus dem normierten Zustand der isolierten Lochlinie | > 99,2677105 % | Analytisch mit rationalen Zertifikaten, im zusätzlichen Linkmodell |
| Zielwahrscheinlichkeit aus der normierten ursprünglichen Entnahme \(f_r\Omega/\sqrt\nu\), **ohne anfänglichen Energiefilter** | > 89,7260353 % | Gleicher vollständiger Hamiltonoperator, Ziel ist die niedrige Lochlinie rechts |
| Verlassen des ungestörten niedrigen Bandes, aus einem Zustand dieses Bandes | < \(1{,}8\cdot10^{-11}\) zu jeder Zeit | Voller erlaubter Ladungssektor, keine Bosonen- oder Flussabschneidung |
| Herkunft des Links, der Bankzerlegung und der Präparation | nicht hergeleitet | Offen |
| Relativistische Felder, gemeinsamer 3+1D-Ursprung, T1-T8 | nicht konstruiert | Offen |

Die Zahlen sind **untere beziehungsweise obere Einschließungen**, keine
berechneten Zentralwerte. Sie beschreiben kein durchgeführtes physisches
Experiment. „Vollständig“ bezieht sich hier auf die Fehlerkontrolle im
deklarierten Zwei-Banken-Ladungssektor, nicht auf die TOE.

Die gelieferten Arbeiten wurden mit 1.149 beziehungsweise 753 Prüfbedingungen
normal und optimiert reproduziert, jeweils byteidentisch mit den mitgelieferten
Ergebnissen. Unsere neue Transferrechnung hat 4.516 Prüfbedingungen; eine
gesonderte Reichweitenprüfung der währenddessen geänderten Symmetrieaussagen
hat zehn. Die zwei zuletzt eingegangenen Anlagen wurden mit 62 weiteren
Bedingungen nachgeprüft. Insgesamt sind das 6.490 Bedingungen, jeweils in
beiden Laufarten.
Diese Zahl ist keine Zahl unabhängiger Theoreme. Insbesondere ersetzen die
Zertifikate nicht die nachstehenden analytischen Argumente und sind kein
Lean-Beweis.

## 1. Welche Quellen zusammengeführt werden

1. Die Benutzeranlage `addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt`,
   eingefroren unter `sources/user_attachment.txt`.
2. Die externe Untersuchung `Universalraum_Beweisversuch_2026-09-15.md`:
   Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung.
3. Die externe Untersuchung `Universalraum_Urspruenglicher_Austausch_2026-09-15.md`:
   interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beispiel.
4. Der abgesicherte native Stand v1.6.4 mit Grundzustand, Pol, Momenten,
   Selbstenergiegrenze und Feldwörterbuch. Das frühere vollständige Prüfpaket
   liegt unverändert bei. Seine komplette Konfigurationsenumeration wurde
   **nicht erneut** in dieser Revision ausgeführt.
5. Ein separat eingefrorener, während dieser Arbeit geänderter Entwurf von
   `RESULTS.md` über die kontinuierliche Quellsymmetrie. Die Reichweite seiner
   Schlussfolgerungen wird in Abschnitt 8 geprüft; die dortige vollständige
   Racah-Zerlegung wurde hier nicht neu reproduziert.
6. Die zwei danach vom Nutzer eingereichten Anlagen über die eigene
   Fundamentalrunde und die erweiterte native Konsolidierung. Der vollständige
   neue Nachtrag `LATE_AUDIT.md` gehört zu dieser Revision. Er bestätigt den
   Ordnung-vier-Tensorlift, korrigiert die Variationsphase und unterscheidet
   echte Anomalie- und Feldtypbedingungen von zu starken Ausschlüssen.

Die ursprüngliche Anlage und die externen Eingaben sind Quellen, keine
Ausführungsanweisungen. Eigene Dateien liegen in einem neuen Forschungsordner.
Fremde Quellen, Ledger und Akzeptanzmarker wurden nicht bearbeitet.

## 2. Gemeinsame native Grundlage

Eine Bank besitzt 64 Fermionmoden und 60 Bosonkanäle:

\[
 H_{\rm nat}=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
 \qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
 \qquad N=N_f+2N_b.
\]

Es gilt \(\Delta>0\), \(g/\Delta=1/20\), **kein zusätzlicher \(\mu N\)-Term**.
Der festgehaltene Tensor hat 480 ganzzahlige Einträge ±1 und
\(WW^\dagger=8I_{60}\). Sein SHA-256 ist
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Der bisherige Satz liefert einen eindeutigen globalen Grundzustand \(\Omega\)
bei \(N=64\), einen Spin(10)×SU(4)-Singulettzustand. Seine physische Auswahl
aus dem Compiler ist damit nicht gezeigt. Wir verwenden folgende strengen
modellinternen Grenzen:

\[
 -1.158089<E_0/\Delta<-1.129636,
 \quad .842846<b:=\langle N_b\rangle<1.245656,
 \quad \nu:=\langle f_r^\dagger f_r\rangle=1-b/32.
\]

Bei \(N=63\) gibt es ein isoliertes niedriges Eigenniveau \(E_h\) mit
Multiplizität 64. Es trägt eine irreduzible duale Fermiondarstellung:

\[
 -1.121899<E_h/\Delta<-1.095812,
 \quad .007737<(E_h-E_0)/\Delta<.039079763822.
\]

Für seinen Spektralprojektor \(P_h\) ist

\[
 Z=\|P_hf_r\Omega\|^2,
 \quad Z_{\rm lo}:=\frac{40912436089}{46487375000}<Z
 <\frac{15578577}{16000000}=:Z_{\rm hi}.
\]

Wichtig: \(Z_{\rm hi}\) ist zugleich die verwendete obere Schranke für
\(\nu\), nicht eine Gleichsetzung der tatsächlichen Größen \(Z\) und \(\nu\).
Das niedrige Gewicht ist >88,0076 % des gesamten normierten CAR-Spektralmaßes.
Innerhalb der **Entnahmeantwort** ist sein Anteil \(w=Z/\nu>90,38836\,\%\).

Alle weiteren Eigenwerte von \(H_{63}\) sind >\(-.75\Delta\);
alle angeregten Eigenwerte von \(H_{64}\) ebenfalls. Die Entnahme-Restantwort
beginnt relativ zu \(E_0\) oberhalb \(.379636\Delta\), die Additionsantwort
oberhalb \(.329636\Delta\).

Diese Schranken gehören zu demselben Hamiltonoperator und demselben Zustand.
Die ursprüngliche Größe \(\chi_r^\dagger\Omega\) bei Ladung 67 wird nicht mit
\(f_r\Omega\) bei Ladung 63 identifiziert.

## 3. Prüfung der gelieferten neuen Resultate

### 3.1 Die interne Paarumwandlung ist wirklich nativ

Bei Gesamtladung 2 zerfällt der 2.076-dimensionale Raum in 60 helle
Zweizustandsblöcke und 1.956 dunkle Zustände. In jedem hellen Block gilt

\[
 H_A=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix},
 \qquad p_{\max}=\frac{32g^2}{\Delta^2+32g^2}=\frac2{27}.
\]

Das wurde aus dem unveränderten Tensor reproduziert. Es ist die Umwandlung
zweier Fermionen in einen Bosonkanal, **kein abgeleiteter Ortswechsel einer
Ladung eins**, und der Ladung-2-Zustand ist nicht der native Grundzustand.
Die acht internen Pfade pro Kanal müssen kohärent bleiben; getrennte
Pfadaufzeichnungen verändern den Gramoperator und damit die Dynamik.

Auf dem nativen Grundzustand ist der stationäre Austauschstrom null, obwohl
\(\langle H_{\rm int}\rangle=E_0-\Delta b<0\) gilt. Eine vollständige
\(N_b\)-Dephasierung erhöht die Energie um
\(\Delta b-E_0\in(1.972482,2.403745)\Delta\). Statische Kohärenz ist nicht
dasselbe wie ein gerichteter Strom.

### 3.2 Der neue Link ist konsistent, aber zusätzlich

Die externe Arbeit definiert ein Rotorpaar \(E,U\) auf \(\ell^2(\mathbb Z)\):
\(E|e\rangle=e|e\rangle\), \(U|e\rangle=|e+1\rangle\), \([E,U]=U\).
Mit zwei **gradiert** zusammengesetzten nativen Banken lautet der Zusatz

\[
 B=\sum_{r=1}^{64}f_{y,r}^\dagger U f_{x,r},
 \qquad V=\tau B+\bar\tau B^\dagger,
 \qquad H=H_x+H_y+\frac\kappa2E^2+V.
\]

Dieser Operator erhält die Gesamtladung und die passend definierten lokalen
Gaussgrößen. Er ist beschränkt mit \(\|V\|\le64|\tau|\). Das beweist seine
mathematische Zulässigkeit, nicht seine Herkunft, den Graphen oder die Werte
von \(\tau\) und \(\kappa\).

Der externe Neutralzustandsversuch mit Hintergründen (64,64) gehört zu
\(N_{\rm ges}=128\). Dort sind die erzeugten Loch-Additions-Paare eine
andere Antwort als eine bereits vorhandene einzelne Lochanregung. Die
berechnete Gewichtsnorm \(64\nu(1-\nu)=2b-b^2/16\), das Faltungsmaß und
die Schwelle \(>.337373\Delta+\kappa/2\) sind damit vereinbar. Sie werden
nicht als Einloch-Transferwahrscheinlichkeit ausgegeben.

### 3.3 Das ältere 99,8718-%-Beispiel ist ein anderer Träger

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs
Zustände sind der vollständige Gausssektor eines **Vierfermion-Modells** mit
einem Link. Der zertifizierte Wert bei \(t=19\) betrifft diesen Parent und
diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation
noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist
davon unabhängig und benutzt die tatsächlich nativen \(E_0,E_h,Z\)-Schranken.

## 4. Neuer Satz: vollständige Kontrolle des Einloch-Transfers

### 4.1 Den richtigen physikalischen Sektor festlegen

Für genau ein Loch ist eine Ladungsreferenz notwendig. Wir deklarieren
Hintergründe \((q_x,q_y)=(63,64)\) und fordern

\[
 G_x=N_x-63+E=0,\qquad G_y=N_y-64-E=0.
\]

Dann ist \(N_x+N_y=127\) und **\(E=63-N_x\) exakt festgelegt**. Auf diesem
Ein-Kanten-Baum verbleibt kein unabhängiger unbeschränkter Flussindex.
\(0\le N_x,N_y\le127\) beschränkt auch die Bosonenzahlen. Der gesamte
physikalische Sektor ist endlichdimensional; keine Flussabschneidung und
kein willkürlicher Bosonen-Cutoff werden eingeführt.

Definiere \(h_r=P_hf_r\Omega/\sqrt Z\). Die 64 Vektoren sind orthonormal.
Das niedrige Band \(P\) wird von

\[
 |L,r\rangle=h_{x,r}\otimes\Omega_y\otimes|0\rangle,
 \qquad |R,r\rangle=\Omega_x\otimes h_{y,r}\otimes|-1\rangle
\]

aufgespannt und besitzt Dimension 128. Für den ungekoppelten Operator
\(H_0=H_x+H_y+\kappa E^2/2\) sind die Energien \(e_*=E_h+E_0\) und
\(e_*+\kappa/2\).

Nach einheitlicher Wahl der relativen Fermionphase wirkt die exakte
Kompression \(PHP\), abzüglich \(e_*\), wie

\[
 \begin{pmatrix}0&-\bar\tau Z\\-\tau Z&\kappa/2\end{pmatrix}
 \otimes I_{64}.
\]

Das Vorzeichen ist für die Population unerheblich. Das \(I_{64}\) zeigt,
dass die Rechnung für jeden normierten internen Überlagerungszustand gilt.
Die projizierten Fermionoperatoren sind Hubbard-Übergänge und keine
vollständige CAR-Algebra auf diesem 128-dimensionalen Band.

### 4.2 Die Lücke zum gesamten übrigen Raum

Die native, nicht nur perturbative Casimiridentität lautet

\[
 \sum_AP_A^\dagger P_A=\tfrac12(15N_f-C_{\rm Spin(10)}-C_{\rm SU(4)}).
\]

In einem Block \(N=n,N_b=b\) ist die rechte Seite höchstens
\(\tfrac{15}2(n-2b-\eta)\) mit \(\eta=n\bmod2\). Bei ungerader
Fermionzahl kommt der Casimir-Mindestwert 15 hinzu. Die Norm des
Boson-Erzeugungszeilenoperators auf dem Zielblock ist \(\sqrt{b+1}\).
Damit liefert die Blocknorm-Abschätzung eine skalare Jacobi-Untergrenze
mit Diagonale \(b\) und quadrierten Nebendiagonalen

\[
 a_b^2=\frac{15(b+1)(n-2b-\eta)}{800}
\]

in Einheiten \(\Delta=1\). Man nimmt negative Nebendiagonalen; die
Quadratformabschätzung benutzt die Normen der vollen Bosonzahlkomponenten
eines beliebigen Zustands, nicht einzelne Testvektoren.

Für **jedes \(n=65,\ldots,127\)** wurden sämtliche LDL-Pivots der
Vergleichsmatrix oberhalb \(-4/5\) exakt positiv nachgewiesen. Der erste
Bosonindex ist \(\lceil(n-64)/2\rceil\), der letzte \(\lfloor n/2\rfloor\).
Somit gilt \(H_n>-.8\Delta\) in allen 63 hohen Ladungssektoren.

Für alle \(n\le62\) liefert die Minimierung der Cauchy-Schwarz-Schranke

\[
 H_n/\Delta\ge-\frac{n-\eta}{4}(\sqrt{23/20}-1)>-1.121899.
\]

Jede andere Ladungsverteilung als (63,64) oder (64,63) enthält eine Bank
mit \(n\le62\) und eine mit \(n\ge65\). Ihre Gesamtenergie liegt also
oberhalb \(-1.921899\Delta\). Die elektrische Energie ist nichtnegativ.
Das obere Bandende von \(P\) ist kleiner als
\(-2.225448\Delta+\kappa/2\).

Für die beiden zentralen Ladungsverteilungen wurden außerdem die
Vergleichsmatrizen ab \(b=1\) bei \(n=63,64\) oberhalb \(-3/4\) erneut
rational geprüft. Durch Minmax mit Kodimension 64 beziehungsweise eins
ergeben sich die bekannten angeregten Energieböden; es wird nicht behauptet,
dass der exakte Spektralprojektor mit dem Null-Bosonenprojektor identisch ist.

Zusammen ergibt sich eine Lücke zwischen \(P\) und \(Q=I-P\) von mindestens

\[
 \boxed{\delta=.303549\Delta-\kappa/2>0.}
\]

Die anderen beiden Vergleichslücken sind
\(.345812\Delta-\kappa/2\) und \(.379636\Delta-\kappa/2\), also größer.
Diese Schranke umfasst **alle** Ladungsaufteilungen, Bosonzustände und
internen Moden des deklarierten physikalischen Sektors.

### 4.3 Gleichmäßige Auslaufkontrolle und endliche Transferzeit

Setze \(v=64|\tau|\) und fordere \(2v<\delta\). Sei \(a\) das obere
Eigenwertende von \(H_0|_P\). Minmax liefert ein Spektralband \(P'\) von
\(H\) derselben Dimension 128, dessen oberer Rand ≤\(a+v\) ist.
Die Kompression \(QHQ\) liegt ≥\(a+\delta-v\).

Mit \(Y=QP'\), als Abbildung aus \(\operatorname{Ran}P'\), gilt die
Sylvestergleichung

\[
 (QHQ)Y-Y(H|_{P'})=-QVP\,PP'.
\]

Die beiden Spektren sind geordnet und mindestens \(\delta-2v\) getrennt.
Die Lösung über das konvergente Exponentialintegral liefert
\(\|Y\|\le v/(\delta-2v)\): nach einem gemeinsamen Skalarshift ist der
Integrand durch \(v e^{-s(\delta-2v)}\) beschränkt. Wegen gleicher endlicher
Ränge gilt dieselbe Schranke für \(\|P'-P\|\).

Da \(P'\) mit \(H\) kommutiert, folgt zu **jeder** Zeit

\[
 \boxed{\|Qe^{-itH}P\|\le L:=\frac{2v}{\delta-2v}.}
\]

Aus der projizierten Schrödingergleichung und Duhamel folgt weiter

\[
 \|Pe^{-itH}\psi-e^{-itPHP}\psi\|
 \le |t|vL=:\eta(t),\qquad \psi\in P,\ \|\psi\|=1.
\]

Für den Zielprojektor \(P_R\subset P\) weichen die Wahrscheinlichkeiten
damit höchstens um \(2\eta(t)\) ab. Dies ist eine nichtperturbative
Fehlergrenze für die volle Entwicklung; nur der ausgewählte Kopplungsbereich
ist klein. Es handelt sich nicht um das Weglassen eines unbekannten
höheren Störungsterms.

### 4.4 Ein vollständig numerisch spezifizierter, rational zertifizierter Punkt

Mit \(\hbar=1\) wähle

\[
 \tau/\Delta=10^{-8},\quad \kappa/\Delta=10^{-10},
 \quad T:=t\Delta=169500000.
\]

Diese Zahlen sind ein konservativer Existenzpunkt, **keine aus TFPT
abgeleiteten Konstanten und keine Behauptung schneller oder optimaler
Übertragung**. Die physikalische Sekundenskala ist nicht bestimmt.

Die genaue komprimierte Rabi-Wahrscheinlichkeit ist

\[
 p_P(t)=\frac{|\tau|^2Z^2}{|\tau|^2Z^2+(\kappa/4)^2}
 \sin^2\!\left(t\sqrt{|\tau|^2Z^2+(\kappa/4)^2}\right).
\]

Für **jedes** zulässige unbekannte \(Z\) liegt der Winkel weniger als
0,08 von \(\pi/2\) entfernt. Das folgt aus \(Z_{\rm lo},Z_{\rm hi}\),
\(\sqrt{x^2+y^2}\le x+y^2/(2x)\) und rationalen Pi-Grenzen. Letztere
wurden zusätzlich mit der Machin-Identität und endlichen alternierenden
Arctan-Reihen eingeschlossen; Fließkomma-Pi ist keine Beweisvoraussetzung.

Mit \(\sin^2(\pi/2+u)\ge1-u^2\) folgt

\[
 p_P(T)>\left(1-\frac{\kappa^2}{16\tau^2Z_{\rm lo}^2}\right)
 (1-.08^2)>.993591982278.
\]

Die vollständigen Fehlergrenzen sind

\[
 L=\frac{25600}{6070954399}<4.216800\cdot10^{-6},
 \quad L^2<1.8\cdot10^{-11},
 \quad\eta(T)=\frac{2777088}{6070954399}<.000457438455.
\]

Also

\[
 \boxed{p_{\rm voll}(T)>p_P^{\rm lo}-2\eta(T)
 =\frac{25218291754002904578202303151726961}
 {25404324948782158166703488466197500}>.992677105368.}
\]

Die unbekannten \(E_0,E_h\) treten nur als gemeinsame Phase auf und müssen
für diese Schranke nicht genau ausgerechnet werden. Eine arbiträr hohe
Treue ist innerhalb des zusätzlichen Modells prinzipiell erreichbar: bei
bekanntem \(Z\), \(\kappa/|\tau|\to0\), \(|\tau|/\Delta\to0\) und
\(t\sim\pi/(2|\tau|Z)\) verschwinden sowohl Detuning als auch der Fehler
\(tv^2/\delta\). Das ist eine bedingte Grenzaussage mit wachsender Laufzeit,
kein ausführbares natives Optimierungsverfahren.

### 4.5 Dieselbe ursprüngliche Fermionantwort ohne anfänglichen Filter

Für
\(\psi_f=(f_{x,r}\Omega_x/\sqrt\nu)\otimes\Omega_y\otimes|0\rangle\)
gilt

\[
 \psi_f=\sqrt w\,|L,r\rangle+\sqrt{1-w}\,q,
 \quad q\in Q,\quad w=Z/\nu\ge Z_{\rm lo}/Z_{\rm hi}.
\]

Die Auslaufnorm in umgekehrter Richtung erfüllt ebenfalls
\(\|Pe^{-itH}Q\|\le L\), indem man die obige Schranke adjungiert und
die Zeit umkehrt. Der unerwünschte Anteil kann also nicht beliebig stark
destruktiv in das niedrige Zielband einstreuen. Mit der Dreiecksungleichung,
\(2\sqrt{w(1-w)}\le1\) und der gesondert geprüften Positivität vor dem
Quadrieren folgt

\[
 \boxed{\|P_Re^{-itH}\psi_f\|^2
 \ge w\,p_{\rm voll}^{\rm lo}-L
 >.897260353455>.897.}
\]

Damit ist **kein vorbereitender Projektor auf die isolierte Linie** nötig,
um eine starke Übertragungsaussage über die ursprüngliche Entnahmeantwort zu
erhalten. Noch benötigt werden die deklarierte geladene Präparation und der
zusätzliche Link. Die Aussage betrifft das niedrige Zielband; sie behauptet
nicht, dass die vollständige hochenergetische Restantwort ebenfalls formtreu
übertragen wird. Für diesen ungefilterten Anfangszustand gilt die extrem
kleine Auslaufwahrscheinlichkeit aus 4.3 nicht: Er startet bereits teilweise
außerhalb von \(P\).

## 5. Warum die Herkunftslücke nicht durch längeres Rechnen verschwindet

Sei \(\Pi_x=(-1)^{N_{f,x}}\) die lokale Fermionparität. Die bisher angegebenen
bankinternen Paarumwandlungen, Zahloperationen, zahlenerhaltenden
Symmetrielifts sowie reine Bosonverbindungen kommutieren mit jeder
\(\Pi_x\). Jede endliche Komposition, lineare Kombination, Adjungierung
und jeder durch solche Operatoren realisierte einzelne Messzweig tut das
ebenfalls. Starke beschränkte Grenzwerte bleiben im Kommutanten der Parität.

Der benötigte Link erfüllt dagegen
\(\Pi_xB=-B\Pi_x\) und \(\Pi_yB=-B\Pi_y\), während er die Gesamtparität
erhält. **Er liegt nicht in dieser bekannten lokalen geraden Algebra.**
Auch adaptives Wiederholen und Nachselektieren gerader Krauszweige kann
die Sektorgrenze nicht überwinden.

Die Voraussetzung „jeder realisierte Zweig ist gerade“ ist wesentlich.
Eine bloß paritätskovariante CP-Abbildung kann ungerade Krausoperatoren
besitzen. Der im Prüfer enthaltene Reset-Kanal auf einer Fermionmode ist
ein exaktes Gegenbeispiel zur unzulässigen stärkeren Behauptung.

Das beweist keinen universellen Unmöglichkeitssatz für den Compiler. Es
beweist, **welche neue Quelleneigenschaft gesucht werden muss**: eine
gerade Gesamtoperation, die bezüglich der zwei operational definierten
Teilbereiche ungerade ist, oder eine ursprüngliche Überlappung, durch die
die angenommene Zerlegung in unabhängig gerade Banken falsch war. Eine
andere bloße Clockphase oder weitere Boson-Paarumwandlung reicht nicht.

## 6. Was von der arithmetischen Untersuchung trägt

### 6.1 Eine einzelne endliche Bank ist nicht der volle Logarithmusgenerator

Quadratisches Ergänzen liefert mit der nativen Casimirnorm
\(\|\sum P_A^\dagger P_A\|\le480\)

\[
 H_{\rm nat}\ge\tfrac\Delta2N_b-C,
 \qquad C=960g^2/\Delta.
\]

Die externe Rechnung verwendet teilweise die schwächere Dreiecksgrenze
\(C=7680g^2/\Delta\), die ebenfalls gültig ist. Über Minmax, **nicht** eine
allgemeine Operator-Monotonie der Exponentialfunktion, folgen

\[
 N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60},
 \qquad \operatorname{Tr}e^{-\beta H}
 \le\frac{2^{64}e^{\beta C}}{(1-e^{-\beta\Delta/2})^{60}}.
\]

Das Zustandswachstum ist polynomial, während ein vollständiges Spektrum
\(E_*\log n+E_{\rm off}\), \(E_*>0\), exponentiell viele Zustände unter
wachsender Energie verlangt. Die ursprüngliche Bank kann dieses komplette
Spektrum daher nicht energieerhaltend mit nur affiner Skalenänderung tragen.
Diese Schranke widerlegt nicht jeden arithmetischen Untersektor, jede
nichtlineare Umparametrisierung oder jeden Nullstellenoperator.

Endlich viele solche Banken und endlich viele energetisch kontrollierte
Rotoren ändern den qualitativen Gegensatz nicht. Unendlich viele identische
Banken lösen ihn nicht automatisch: Bei gleichmäßig beschränkten lokalen
Anregungskosten divergiert bereits die globale Wärmespur. Ein geeigneter
relativer oder lokaler Spurbegriff wäre ein zusätzlicher Gegenstand.

### 6.2 Primzahlen können eine gewählte Dynamik organisieren, erzwingen sie aber nicht

Auf \(\ell^2(\mathbb N)\) kann man \(H_{\rm ar}|n\rangle=\log n|n\rangle\)
definieren. Die additive Primfaktorbesetzung erklärt dann die Eulerstruktur.
Der Definitionsbereich lautet \(\sum_n(\log n)^2|\psi_n|^2<\infty\).
Dass quantenstatistische Systeme mit Zeta-Zustandssumme existieren, ist
bereits ein Ergebnis von [Bost und Connes](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
Das ist ein relevanter Anschluss, nicht die fehlende native Herleitung.

Der gelieferte Cocycle \(c(m,n)=(-1)^{v_2(m)v_3(n)}\) ist assoziativ, weil
Bewertungen unter Multiplikation additiv sind. Für
\(T_m|n\rangle=c(m,n)|mn\rangle\) gilt
\(T_lT_m=c(l,m)T_{lm}\), insbesondere \(T_2T_3=-T_3T_2\).
Die unkontrollierten CP-Kanäle verlieren diese globale Phase und erfüllen
\(\mathcal E_l\mathcal E_m=\mathcal E_{lm}\). In kohärent kontrollierten
Wegen bleibt die relative Phase messbar. Das ist eine exakte Phasenstruktur,
aber kein Beweis einer Quellenauswahl dieses Cocycle oder von RH.

Strikt multiplikative Schritte \(m>1\) ergeben auch keine geschlossenen
Bahnen: \(n\mapsto mn>n\). Die Frequenz \(\log p\) eines Operators, eine
Bahnlänge \(r\log p\) und der Schwingungszeitraum \(2\pi/\log p\) müssen
auseinandergehalten werden. Hier hat der RH-Graph-Skill die Prüfung auf
Generator, Spur und Phase getrennt und eine bloße Analogieschließung verhindert.

### 6.3 Der RH-Zielsatz bleibt unbewiesen

Die vorgeschlagene Identität

\[
 \frac{\Xi(z)}{\Xi(0)}=\det(I-z^2A^{-2}),\quad
 \Xi(z)=\xi(\tfrac12+iz),
\]

für einen strikt positiven selbstadjungierten Operator \(A\) mit kompakter
Inverser und \(A^{-2}\) von Spurklasse wäre tatsächlich hinreichend:
Die gesamte rechte Funktion hat ihre Nullstellen nur bei reellen
\(\pm\lambda_j(A)\), einschließlich Multiplizitäten. Aber dieser Operator
und die gesamte Funktionsidentität sind **nicht konstruiert**. Ein Operator
mit lediglich den Imaginärteilen der Nullstellen wäre unzureichend.

Weder diese Prüfung noch die im externen Code bereits verwendete
Faktorisierung kleiner Testzahlen liefert einen neuen effizienten
Faktorisierungsalgorithmus, eine native Quantenoperation dafür oder eine
Lösung von P versus NP. Hylæan wurde in dieser Revision nicht neu geprüft.

## 7. Die lokale Polnäherung wird präziser, das relativistische Feld bleibt offen

Die externe Resolventenabschätzung ist korrekt: Im Kreis mit Radius
\(.1\Delta\) um den **tatsächlichen**, unbekannten negativen Pol \(-\epsilon\)
gilt

\[
 G(z)=\frac{Z}{z+\epsilon}+R(z),\qquad
 |R(z)|<.505213/\Delta.
\]

Der übrige Spektralträger ist mindestens \(.337373\Delta\) vom Pol entfernt.
Die relative Abweichung vom echten Polterm beträgt im Kreis unter 5,75 %.
Die Abschätzung setzt keine Intervallmitte anstelle von \(Z,\epsilon\) ein
und ist keine globale Vernachlässigbarkeit der Selbstenergie.

Aus v1.6.4 bleibt bestehen: Die exakte Zwei-Feld-Resolvente besitzt einen
nichtverschwindenden Rest \(\Sigma_2(z)\). Seine komplette Funktion ist
noch nicht bestimmt. Das neue kontrollierte Transportlemma benötigt sie
nicht vollständig, weil es den Rest durch eine Spektrallücke kontrolliert.

Ebenso bleibt der Feldtypentest bestehen: Der native antisymmetrische
Paartensor zusammen mit zwei gleichhändigen Weylfeldern und einem skalaren
Vermittler ergibt den verschwindenden Kanal. Ein symmetrischer Lorentz-
Spinortensor oder eine zusätzliche gleichgeladene zweidimensionale
Antisymmetriemarke eröffnet einen nichtverschwindenden Kanal, führt aber
zusätzliche Struktur ein. Ein internes Spin(10)-Spinorlabel ist kein
Lorentz-Weylindex. Der neue Link behebt diese Typfrage nicht.
Die Konventionen des bisherigen Tests sind mit der Primärübersicht von
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) verbunden;
ein neuer vollständiger relativistischer Adapter wurde hier nicht konstruiert.

Die spätere Feldtypenprüfung in `LATE_AUDIT.md` zeigt außerdem einen
Lorentz-erlaubten Zwei-Ableitungs-Kandidaten für den symmetrischen
Spinortensor und widerlegt einen pauschalen (1,1)-Ausschluss: Der
Energie-Impuls-Tensor ist schon bei Dimension vier zulässig. Weder ein
gesunder nativer Feldadapter noch ein dynamischer Gravitonpol folgt daraus.

## 8. Während der Arbeit entdeckte Änderung: „Kommutant 7“ richtig einordnen

Die strikte Originalquellenprüfung stoppte korrekt, als eine andere Arbeit
den früheren nativen Bericht ergänzte. Der alte Stand mit Hash
`1062e13fe0fb79cce015657a7b4d40a61e9639922ff95fa60c689c0068c38ffc`
blieb eingefroren. Der gesonderte geänderte Entwurf hat Hash
`ab745e74b1232b1ddf35dd0e0d0da4ace0176c797d769e5db8bedd0010bcba6a`.
Die in dieser Revision verwendeten Energie- und Polzertifikate änderten
sich bei dieser Prüfung nicht. Der Fehlerbeleg wurde aufbewahrt.

Der neue Entwurf listet drei dunkle Darstellungstypen mit Dimensionen
24.000, 11.200, 2.688; drei helle mit 2.880, 576, 320; und einen χ-Typ mit 64.
**Unter Voraussetzung dieser Zerlegung** lässt sich seine Folgerung exakt
nachprüfen:

\[
 \mathcal H_{N=3}\simeq
 \bigoplus_{d\in D}V_d\ \oplus\
 \bigoplus_{b\in B}(\mathbb C^2\otimes V_b)\ \oplus V_\chi.
\]

Die Summe ist \(37888+2\cdot3776+64=45504\). Die drei hellen Typen
kommen im **vollen** Raum jeweils zweimal vor. Daraus folgen:

- Nur die Gruppenwirkung hat einen Kommutanten der Dimension
  \(3+3\cdot4+1=16\), nicht sieben.
- Werden zusätzlich die nichtverschwindenden hellen Paarmischungen und
  \(N_b\) als Operationen zugelassen, erzeugen sie die vollständigen
  \(M_2\)-Multiplizitätsalgebren. Dann bleiben sieben zentrale Skalare.
- Sieben ist **keine absolute Untergrenze für beliebige weitere Operationen**.
  Ein erlaubter Operator, der diese sieben Blöcke verbunden mischt, zwingt
  die sieben Skalarwerte zur Gleichheit und lässt nur einen übrig. Der
  endliche Inzidenzmatrix-Test hat Rang sechs und beweist dieses Gegenargument.
- Die Zerlegung allein beweist weder operative Verfügbarkeit der
  kontinuierlichen Symmetrie noch einen Einzelfermion-Link. Selbst alle
  bankinternen Symmetrieoperationen erhalten die lokale Fermionparität.

Der interessante Wert sieben wird dadurch nicht verworfen. Korrigiert
werden die Aussagen „voller N=3-Raum multiplizitätsfrei“, „absolute Grenze
für jede Operation“ und eine unbewiesene Gleichsetzung von Symmetrie und
verfügbarem Instrument. Die genaue Darstellungszerlegung selbst bleibt in
diesem Zusatz eine externe Voraussetzung, kein frisch reproduzierter Satz.

Der Debugging-Skill führte hier zur Versionsprüfung statt zum Ersetzen
eines Pins. Das neue Manifest trennt deshalb einen erfolgreichen
**eingefrorenen Quellenreplay** von `originals_unchanged=false`.

## 9. T1-T8: was dieses Ergebnis beiträgt und nicht beiträgt

Die Begriffe folgen der aktuellen offenen Problemliste und ihrer
Forschungszuordnung. Keine Akzeptanzmarkierung wurde heraufgesetzt.

| Tor | Fehlender Nachweis | Beitrag dieser Revision |
|---|---|---|
| T1 | Ursprung von P1/P2, Dimension, Compiler- und Zustandswahl | Bekannte gerade Operationsalgebra ist für Einzeltransport unzureichend; ursprüngliche Auswahl weiter offen |
| T2 | Tatsächlich halbgeladenes, markiertes E8-Feld samt Renormierung, Energie- und Adjungiertenkontrolle | Der Ladung-eins-Lochzustand ist kontrolliert, aber nicht mit dem fehlenden Half-Charge-Feld identifiziert |
| T3 | Ein gemeinsamer, aus TFPT ausgewählter lokaler unitärer 3+1D-Parent | Vollständiger bedingter Zwei-Banken-Transfertest; kein ausgewählter räumlicher Parent |
| T4 | Chirales SM-Maß, Anomalien/Index, gleichmäßige Spiegelentkopplung | Feldtyp-Widerspruch weiter sichtbar; kein chirales Maß |
| T5 | Wechselwirkender Kontinuumsübergang, Lorentzverhalten, Clustering, Confinement und Streuung | Endliche-Sektor-Fehlerkontrolle ist ein Baustein, aber kein räumlicher Grenzübergang |
| T6 | Interne Herleitung aller Eichkopplungen und vollständiger Neutrinotextur/-skala | Keine neue Herleitung; \(\tau,\kappa\) sind deklarierte Testparameter |
| T7 | Masseloser dynamischer Spin zwei, beide Helizitäten, universelle Kopplung im selben Parent | Offen; der neue pauschale Ausschluss eines Dimension-vier-(1,1)-Tensors wurde korrigiert |
| T8 | Physische Präparation/Anfangszustand und ein gemeinsames Quellfunktional aller Auslesungen | Anfänglicher Polfilter wird für >89,7 % unnötig; geladene Präparation und Messinstrument weiter offen |

## 10. Nächste entscheidende Arbeiten mit klaren Abbruchkriterien

**A. Die Quelle des geraden Gesamtlinks finden.** Nicht noch eine riesige
Kontrollmatrix bauen, sondern für jeden tatsächlich ursprünglichen Generator
\(O\) prüfen, ob \([O,\Pi_x]\ne0\) bei erhaltener Gesamtparität möglich ist.
Eine positive Antwort muss Generator, Teilbereichsdefinition, Hilbertraum,
Gaussreferenz und Matrixelement liefern. Bleiben alle Generatoren lokal
gerade, ist die Suche nach dem Link durch deren weitere Komposition beendet.
Dann muss die ursprüngliche Teilraumdefinition oder der Quellenvertrag
explizit geändert werden; man darf keinen Hopterm als Ergebnis ausgeben.

**B. Die ursprüngliche Entnahme als gemeinsames Instrument realisieren.**
Eine Referenzmode könnte Ladung erhalten, während \(f_r\Omega\) präpariert
und ausgelesen wird. Zu prüfen sind ihre Herkunft, Energiekosten,
Erfolgshäufigkeit und Erhaltung der internen Kohärenz. Der neue Satz entfernt
bereits die zusätzliche Pflicht eines perfekten anfänglichen Energiefilters.
Er entfernt nicht die Pflicht, ein geladenes Instrument auszuweisen.

**C. Den Feldtyp vor räumlichen Rechnungen entscheiden.** Entweder folgt ein
passender Lorentzträger wirklich aus derselben Quelle, oder der skalare
Weyl-Ansatz wird in seiner jetzigen Form verworfen. Eine bloße zusätzliche
Verdopplung ohne Herkunft ist ein Modellvorschlag, keine Ableitung.

**D. Erst dann viele Banken.** Der nächste räumliche Test benötigt dieselbe
Quelle, einen bestimmten Graphen, Lokalisierung der Operationen und mit dem
Volumen verträgliche Fehler- und Energiebounds. Ein einziges neues Linklemma
liefert weder Raumdimension noch Lichtkegel, chirale Materie oder Gravitation.

**E. Arithmetik getrennt scharf halten.** Eine echte Verbindung müsste eine
gemeinsame Quellabbildung mit Generator, Zustands-/Spurstruktur, Phasen und
Domänen liefern. Die volle signierte Weilform oder die ganze Determinanten-
identität bleibt das Beweisziel. Der bloße Auftritt von Primzahlen erfüllt
keines davon. Der globale RH-Index ließ sich wegen einer fehlenden
historischen Quelle und veränderter Review-Quellen nicht vollständig
aktualisieren; die gezielte Originalquellenprüfung ist enger als ein
frischer Gesamtindex. Es wurde kein RH-Abschlusskandidat registriert.

## 11. Reproduktion und ehrliche Liefergrenze

`replay.py --frozen-only` führt die fünf Prüfer normal und mit `-OO` aus,
vergleicht beide JSON-Ergebnisse und die zwei externen Originalberichte,
prüft alle eingefrorenen Quellen und protokolliert Änderungen der
Originalorte gesondert. Ein Fehler führt zu FAIL. Der zuvor aufgetretene
Live-Quellenfehler bleibt in `source_drift_failure_receipt.json` sichtbar.

Die abgesicherten Zahlen stehen vollständig rational in
`two_bank_transfer_normal.json`; Dezimalwerte dienen nur der Lesbarkeit.
Die analytische Beweiskette steht in Abschnitt 4. Das Paket umfasst die
unveränderten externen Arbeiten, deren Programme, die native v1.6.4-Abhängigkeit
und alle neuen Berichte. NumPy, SymPy und für das ältere native Paket dessen
separat dokumentierte Voraussetzungen sind zu unterscheiden.

Die versionierte ausführliche Markdown-Lieferung enthält zusätzlich den
vollständigen eingefrorenen nativen Herleitungsbericht v1.6.4 als historischen
Anhang. Daneben gibt es ein kurzes Update und eine bildliche Erklärung.
**Die großen TFPT-Haupt-PDFs und die Webseite werden in dieser Revision nicht
als aktualisiert ausgegeben. Es gab keinen Commit oder Push.**


---

# Nachprüfung der beiden zuletzt eingegangenen Untersuchungen

Integrierter Nachtrag zu v1.6.5 · 15. September 2026

Quellen: die Anlagen `8e110ae1-19e2-4d47-bfc8-ebe4fe9ab81b` und
`b928b72a-6669-4c67-a75d-124095791c6f`, unverändert eingefroren. Zusätzlich
wurden die vier genannten Programme `t1_fixed.py`, `stabilizer.py`,
`t5_twobank.py`, `t5_varresp.py` vollständig gelesen und archiviert. Eine
eigene Nachrechnung prüft die kritischen Folgerungen; sie ist **kein
vollständiger Replay aller sechs Sonden** des fremden Arbeitsordners.

## 1. Übersicht: übernehmen, korrigieren oder offenlassen

| Neue Aussage | Ergebnis der Prüfung |
|---|---|
| Innerer Viererzyklus erhält alle 60 W-Kanäle | Bestätigt, jetzt einschließlich der richtigen Fermion-Vorzeichen und explizitem Bosonlift |
| Grundzustandseindeutigkeit/Singulett/Gaplücke weiterhin unbekannt | Überholter Stand: unter dem festgelegten nativen Vertrag bereits bewiesen; voller Vektor weiter unbekannt |
| Leerer Grundzustand für alle μ≥0 | Falsch; bei μ=0 liegt der eindeutige N=64-Grundzustand unter −1,129636Δ |
| Kommutant 7 als absolute Untergrenze | Nur im benannten blocktreuen erweiterten Operationsvertrag; siehe Hauptbericht Abschnitt 8 |
| Beliebige Einteilchenmatrix ist damit als natives Fock-Wort verfügbar | Nicht gezeigt; assoziative Matrixalgebra, Lie-Kontrolle und Fock-Lift sind verschiedene Fragen |
| Kanal-Variationszustand hat E=−0,0196Δ | Die angegebene Phase im Code ergibt gegen den gepinnten P=f_jf_i-Vertrag +0,05736Δ; ein relatives Vorzeichen korrigiert es |
| 99,892-%-Transfer bei t≈2484 | Numerisches Maximum eines Vierzustands-Paarmodells im untersuchten Zeitfenster; kein erster/globaler exakter Maximalsatz und kein nativer Einloch-Transfer |
| Gleiche Zweigableitungen genau bei ε=0 | Algebraisch richtig; die Eigenwertlücke bleibt dort √32·|g|, also kein allgemeiner „Kegel genau dann wenn gaplos“-Satz |
| SU(4)³-Anomalie =16 | Richtig unter A(4)=1 und der zusätzlichen Interpretation aller (16,4) als gleichhändige Weylfelder; Eichung ist eine weitere Voraussetzung |
| Gravitationsanomalie =64 | Keine reine perturbative Gravitationsanomalie in 3+1D; 64 kann bei zusätzlich deklarierter gleichgeladener U(1) die gemischte U(1)-Gravitationsanomalie zählen |
| Mit einer Ableitung kein (1,1)-Tensor bei Dimension ≤4 | Falsch: der Energie-Impuls-Tensor ist ein Gegenbeispiel; daraus folgt aber noch kein dynamisches Graviton |
| Kein lokaler kovarianter kinetischer Term für (1,0) | Zu pauschal: der bilineare Ein-Ableitungs-Term fehlt, ein Zwei-Ableitungs-Skalar existiert; Positivität/Constraints/Herkunft bleiben zu prüfen |

„Negativ geschlossene Route“ bedeutet nicht „T2, T3, T4 oder T7 geschlossen“.
Ein ausgeschlossener Ansatz beantwortet nicht die jeweilige physikalische
Existenzfrage. Die beiden gelieferten Texte widersprechen sich vor allem
beim bereits bewiesenen modellinternen Grundzustand; sie dürfen nicht als
gleichzeitig aktueller einheitlicher Status zitiert werden.

## 2. Positiver neuer Anschluss: der korrekt angehobene Viererzyklus

Die Abbildung der Fermionmarken lautet
\(p(4s+a)=4s+(a+1\bmod4)\). Auf Paaren ist zwingend das Exteriorvorzeichen
zu beachten: Falls \(p(i)>p(j)\), erhält das sortierte Paar ein Minuszeichen.
Der gelieferte `stabilizer.py` lässt dieses Zeichen weg. Das wäre im
Allgemeinen falsch; für den untersuchten Viererzyklus überlebt das positive
Resultat jedoch auch den korrekten Test.

Alle 60 W-Zeilen werden mit ihren Vorzeichen wieder auf W-Zeilen abgebildet.
Wir haben den zugehörigen signierten Bosonoperator \(R_b\) explizit gebildet
und exakt geprüft:

\[
 W'=R_bW,\qquad R_bR_b^T=I_{60},\qquad R_b^4=I_{60},
 \qquad R_b^2\ne I_{60}.
\]

Damit existiert ein **gemeinsamer nativer Tensor-Automorphismus** auf
Fermionen und Bosonen, nicht nur eine Übereinstimmung von Zeilenzahlen.
Die gleichzeitige Transformation erhält Paarwechselwirkung und Bosonzahl.
Sie beweist eine Ordnung-vier-Symmetrie, nicht deren operative Verfügbarkeit.

Dieser Permutationszyklus ist nicht die zentrale Matrix \(iI_4\) von SU(4).
Seine Determinante auf dem Viererfaktor ist −1. Mit einer zusätzlichen
Ladungsphase kann man geeignete Gruppenlifts vergleichen; die Permutation,
die zentrale Phase, der Clock und die geometrische Glue-Markierung sind
dadurch aber nicht schon identifiziert. Genau diese Intertwiner-Frage ist
ein sinnvoller neuer Anschluss, statt noch einmal nur vier zu zählen.

## 3. Warum der Einteilchen-Abschluss den Fock-Operationssatz nicht schließt

Die Irreduzibilität der Einteilchendarstellung kann ihre assoziative
Matrixalgebra zu \(B(\mathbb C^{64})\) machen. Daraus folgt nicht, dass jede
Matrix als ein zulässiges physisches Wort verfügbar ist, und auch nicht,
dass ihre zweite Quantisierung bereits erzeugt wird.

Ein kleinstes exaktes Gegenbeispiel zur falschen Liftregel:
\(A=|1\rangle\langle1|\), \(B=|2\rangle\langle2|\) auf zwei Moden.
Dann \(AB=0\), also \(d\Gamma(AB)=0\), aber
\(d\Gamma(A)d\Gamma(B)=n_1n_2\ne0\).
Der zweite Quantisierungsschritt ist ein Lie-, nicht ein assoziativer
Algebra-Homomorphismus dieser Art.

Auch \(\operatorname{diag}(i,1,1,1)\) und
\(\operatorname{diag}(i,i,1,1)\) haben Determinanten i beziehungsweise −1.
Ihre Zugehörigkeit zur **linearen Matrixalgebra** aus SU(4)-Generatoren und
Identität ist kein exaktes SU(4)-Gruppenwort. Projektive Gleichheit oder eine
zusätzliche U(1)-Phase kann helfen, muss aber mit der Bosonwirkung, Ladung
und Referenz gemeinsam ausgewiesen werden.

Der fremde Code folgert außerdem die Irreduzibilität des 37.888-dimensionalen
dunklen Dreifermionraums aus der vollen Einteilchenmatrixalgebra. Diese
Schlussregel ist nicht begründet. Bereits die im anderen neuen Text
angegebenen drei dunklen irreduziblen Typen widersprechen der pauschalen
Eins-Block-Lesart unter der bloßen Quellsymmetrie. Die Zahl 8.732.673 mag als
sehr schwache obere Schranke anderweitig verträglich sein; die im Code
angegebene Herleitung belegt sie nicht. Die SVD-/Toleranzprüfungen des Codes
sind zudem numerisch, nicht allein wegen „PASS“ exakte Lie-Beweise.

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und
positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette
Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig;
Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg.
Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

Das grobe Sandwich \([-1.2,-.0196]\Delta\) ist nach einer Phasenkorrektur
zwar verträglich, aber wesentlich schwächer als
\((-1.158089,-1.129636)\Delta\). Es ist keine Verschärfung.

Im tatsächlich angegebenen Variationscode werden die Fermionen in der
Reihenfolge j, dann i gelöscht. Das liefert \(f_if_jF=-f_jf_iF\), während
der native Vertrag \(P_A=\sum W_{A,ij}f_jf_i\) verwendet. Bei unverändertem
\(g=+\Delta/20\) und den angegebenen Variationskoeffizienten folgt deshalb

\[
 E_{\rm Code}/\Delta=\frac12-\frac{23\sqrt3}{90}
 =+.057364793621\ldots,
\]

nicht der behauptete negative Wert. Mit korrigierter relativer Phase lautet
er \(1/2-3\sqrt3/10=-.019615242271\ldots\). Alternativ wäre eine konsequente
andere P/g-Phasenkonvention möglich; die Quelle muss sie dann überall führen.
Die gleichzeitige Einteilchendichte des einfachen Variationszustands bleibt
von dieser Phasenreparatur unberührt, weil seine Bosonzahlkomponenten
orthogonal sind. Sie ist keine dynamische Greenfunktion auf dem nativen
Grundzustand und ersetzt dessen schon kontrollierte Antwort nicht.

## 5. Feldtheorie: falsche Verbote entfernen, echte Bedingungen behalten

### 5.1 Anomalien

Für die zusätzlich angenommene 3+1D-Weylinterpretation lautet das lokale
Anomaliepolynom bis auf Konventionsvorzeichen

\[
 I_6=[\widehat A(T)\,\mathrm{ch}_R(F)]_6
 =\mathrm{ch}_3(F)-\frac{p_1(T)}{24}\,\mathrm{ch}_1(F).
\]

Der reine gravitative Anteil \([\widehat A]_6\) verschwindet; seine
Formgrade sind Vielfache von vier. Das ist die bekannte dimensionale
Unterscheidung bei [Álvarez-Gaumé und Witten](https://collaborate.princeton.edu/en/publications/gravitational-anomalies/).
Eine Spur-/Weylanomalie ist nochmals ein anderer Begriff.

Auf (16,4) ist der SU(4)-Kubikkoeffizient 16 bei Normierung A(4)=1.
Der exakte Test \(t=\operatorname{diag}(1,1,1,-3)\) hat
\(\operatorname{tr}t=0\), \(\operatorname{tr}t^3=-24\).
Ist SU(4) **dynamisch geeicht**, muss die vollständige Theorie diese
Eichanomalie kompensieren. Als globale Symmetrie kann sie eine
't-Hooft-Anomalie tragen; dann folgt keine pauschale Spiegelpflicht.
Ein vollständiger konjugierter Spiegel ist ein möglicher Ausgleich,
aber hier nicht als einzige oder allgemein minimale Lösung bewiesen.

„Gravitativ 64“ kann sinnvoll eine **gemischte U(1)-Gravitationsanomalie**
meinen, wenn alle 64 linksgetragenen Weylfelder explizit U(1)-Ladung eins
erhalten. Das muss samt Eich-/Globalstatus gesagt werden. Für SU(4) allein
ist der gemischte lineare Spurkoeffizient null. Die Quellenmarke N darf
nicht ohne Beweis in eine dynamisch geeichte chirale U(1) umgedeutet werden.

### 5.2 Der behauptete Spin-2-Ausschluss ist falsch

Die Lorentzdarstellungen liefern exakt

\[
 (\tfrac12,\tfrac12)\otimes(\tfrac12,\tfrac12)
 =(0,0)\oplus(1,0)\oplus(0,1)\oplus(1,1).
\]

Eine Ableitung des Vektorbilinears \(\psi^\dagger\bar\sigma_\mu\psi\)
kann daher einen symmetrischen spurfreien (1,1)-Tensor bilden. Insbesondere
hat der Energie-Impuls-Tensor
\(T_{\mu\nu}\sim i\psi^\dagger\bar\sigma_{(\mu}
\overleftrightarrow\partial_{\nu)}\psi\), mit passender Spurbehandlung,
Dimension \(3/2+3/2+1=4\). Ein Energie-Impuls-Tensor kann bereits in einer
festen Hintergrundraumzeit definiert werden; dynamische Diffeomorphismen
müssen nicht vorausgesetzt werden, um dieses Gegenbeispiel zu formulieren.

Das schließt **T7 nicht**. Ein vorhandener Tensor ist kein masseloser
Spin-2-Pol. Das sinnvolle Ziel ist später sein transversaler, spurfreier
Korrelator auf demselben räumlichen Parent, mit positiver Norm, beiden
Helizitäten und universeller Kopplung. Wir entfernen hier eine falsche
Darstellungsobstruktion, nicht die dynamischen Nachweispflichten.

### 5.3 (1,0)-Kinetik ist nicht generell verboten

Der bilineare Ein-Ableitungs-Term mit einem (1,0)-Feld und seinem Adjungierten
besitzt keinen Lorentzskalar. Mit zwei Ableitungen existiert aber etwa

\[
 \mathcal L_2\propto
 (\partial^{\alpha\dot\alpha}\Phi_{\alpha\beta})
 (\partial^{\beta\dot\beta}\bar\Phi_{\dot\alpha\dot\beta})
\]

für symmetrisches \(\Phi\). Alle Spinorindizes sind kontrahiert. Bei rein
zeitartigem Impuls ist sein Symbol proportional zu
\(\omega^2(|\Phi_{11}|^2+2|\Phi_{12}|^2+|\Phi_{22}|^2)\), also nicht
identisch null. Das ist ein Gegenbeispiel zum uneingeschränkten Satz „kein
lokaler kovarianter kinetischer Term“. Es beweist **nicht** Positivität des
vollen Hamiltonoperators, korrekte Constraints, gewünschte Freiheitsgrade
oder eine native Quelle. Diese bleiben die entscheidenden Tests.

## 6. Die Vierzustandsrechnung richtig lesen

Das Modell mit \(s=\sqrt8g\), Bosonverbindung η und Diagonalen (0,Δ,Δ,0)
erlaubt kohärenten **Paartransport**. Die exakte Identität
\((H^3)_{41}=8g^2\eta\) stimmt. Unsere unabhängige Fließkomma-Abtastung
reproduziert auf \([0,3000]\) mit Schrittweite .05 den größten gefundenen
Wert .998920021869 bei 2484.05. Der erste Gitter-Lokalhöchstwert liegt
bereits bei 6.05. Weder „erster Maximalzeitpunkt“ noch ein globales exaktes
Maximum ist damit bewiesen. Diese kleine Rechnung wird nicht mit dem
vollständigen Einloch-Satz des Hauptberichts verwechselt.

Für \(F_\pm(\epsilon)=(\epsilon\pm\sqrt{\epsilon^2+32g^2})/2\)
gilt \(F'_+-F'_-=\epsilon/\sqrt{\epsilon^2+32g^2}\). Bei ε=0 stimmen
die Ableitungen überein, aber die **Eigenwertlücke** beträgt
\(\sqrt{32}|g|>0\). Ein verschwindender nackter Vermittlerparameter und
eine verschwindende wechselwirkende Anregungslücke sind verschieden.
Ein allgemeiner relativistischer Kegelsatz oder ein zwingendes neues
Renormierungsprogramm folgt aus dieser Ableitungsidentität nicht.

## 7. Konsequenz für die nächste Forschungsrevision

Die sinnvollen positiven Anschlüsse sind jetzt schärfer:

1. Den expliziten Ordnung-vier-Lift mit dem tatsächlich markierten Clock
   und der Herkunft des A3-Index vergleichen: vollständige Intertwiner,
   Ladungsphase und Bosonwirkung, nicht nur Gruppennamen.
2. Einen Quellenoperator finden, der die lokale Parität beider operational
   bestimmten Teile gleichzeitig ändert. Die native Z4-Symmetrie selbst
   tut das nicht. Der kontrollierte Einloch-Transfer ist bereits als
   Akzeptanztest für einen solchen Operator verfügbar.
3. Den Zwei-Ableitungs-Feldkandidaten auf Positivität und Constraints prüfen,
   bevor er als relativistischer Adapter zählt. Ein bloßes Nichtnull-Symbol
   ist noch keine gesunde Feldtheorie.
4. Den Energie-Impuls-Tensor als zulässigen **Kandidaten** behalten, aber erst
   auf dem gemeinsam konstruierten räumlichen Träger nach einem dynamischen
   Spin-2-Pol suchen. Kein vorhandener Spin-2-No-go rechtfertigt hier das
   Aufgeben dieses Anschlusses.

62 zusätzliche Prüfbedingungen bestehen normal und optimiert identisch.
Exakte Identitäten, bedingte Darstellungsargumente und die numerische
Zeitfenstersuche sind im Ergebnisbericht getrennt. Der externe Status
„alle Restfragen geschlossen oder auf genau ein Stück reduziert“ wird
nicht übernommen. Die vollständige TOE bleibt offen.


---

# Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

# TFPT / Universalraum: nativer Pol, Bewegungsgleichung und minimale Feldtypen

**Konsolidierte Forschungsfortsetzung v1.6.4 · 15. September 2026**

Diese Revision verbindet den während der Arbeit neu eingegangenen Polsatz
v1.6.3 mit einer unabhängig begonnenen Untersuchung der nativen
Bewegungsgleichung. Sie ergänzt die bisherigen Hauptdokumente; sie ist
keine verkürzte Neufassung des vollständigen Hauptbuchs. Die vorhandenen
Haupt- und Update-PDFs wurden in dieser Runde nicht verändert.

## 1. Ergebnis in einem Satz

Auf dem abgesicherten Grundzustand des festgelegten nativen Fockmodells
existiert eine isolierte ursprüngliche Fermion-Entnahmelinie; nach
Kombination beider Rechnungen trägt sie **mehr als 88,007628 % des gesamten
normierten Spektralgewichts pro Mode**. Die zusätzliche Antwort ist jedoch
nicht exakt auf eine einzige weitere Linie reduzierbar. Ihr erster
Rückwirkungsschritt wird direkt von derselben ursprünglichen Wechselwirkung
bestimmt.

Am Prüfpunkt \(g/\Delta=1/20\), ausdrücklich ohne \(\mu N\)-Zusatz:

| Größe | Eingegangene v1.6.3 | Konsolidierte strengere Grenze |
|---|---:|---:|
| Mittlere Bosonenzahl | \(0.77<\bar b<1.45\) | \(0.842846<\bar b<1.245656\) |
| Energie der niedrigen Entnahmelinie | \(0.007737<\epsilon/\Delta<0.062277\) | \(0.007737<\epsilon/\Delta<0.039079764\) |
| Gewicht dieser Linie im gesamten CAR-Maß | \(Z_{\rm low}>0.864972353\ldots\) | \(Z_{\rm low}>0.880076280689\ldots\) |
| Obere Gewichtsgrenze | \(Z_{\rm low}<0.9759375\) | \(Z_{\rm low}<0.9736610625\) |
| Übrige Entnahmeenergien | \(>0.379636\Delta\) | unverändert |
| Sämtliche Additionsenergien | \(>0.329636\Delta\) | unverändert |

Die Dezimalzahlen sind gerundete Darstellungen rationaler Schranken.
Es sind weder exakte Polpositionen noch angepasste Zentralwerte. Der Pol
steht im retardierten Spektrum bei negativer Frequenz \(-\epsilon\).
Das niedrige Niveau im N=63-Hilbertraum ist 64-fach entartet; jede
diagonale Modenantwort sieht dieselbe Linie.

**Nicht bewiesen:** die physische Herleitung des Hamiltonoperators, sein
vollständiger Operationssatz, native Präparation, räumliche Ausbreitung,
ein vollständiges relativistisches Feldwörterbuch oder eine TOE. T1-T8
bleiben als vollständige Aufgaben offen.

## 2. Ein unveränderter Modellvertrag

Es werden keine Hopping-, Massen-, Ladungs- oder Projektionsglieder zu H
hinzugefügt:

\[
H=\Delta N_b+g(Q_++Q_-),\quad Q_+=\sum_A b_A^\dagger P_A,
\quad Q_-=Q_+^\dagger,
\]
\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad N=N_f+2N_b,
\quad WW^\dagger=8I_{60}.
\]

Es gibt 64 CAR-Fermionmoden, 60 CCR-Bosonmoden und 480 von null
verschiedene reelle W-Einträge mit ihren ursprünglichen Vorzeichen.
\(\Delta>0\), g ist reell; die Zahlen beziehen sich auf \(g/\Delta=1/20\).
Die Tensorquelldatei ist durch SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`
fixiert.

Die Fockrealisierung, H, der sektorenübergreifende Energievergleich und
der Prüfparameter sind weiterhin Modellvoraussetzungen. Die geometrische
oder arithmetische Herkunft eines W-Tensors leitet diese Voraussetzungen
nicht allein her. Insbesondere sind die fünf elementaren CAR in einer
Spinor-Matrixkonstruktion nicht mit den hier verwendeten 64 Fockmoden
gleichzusetzen.

## 3. Was tatsächlich erneut geprüft wurde

### 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine
eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch
mit neu kompiliertem Quellcode berechnet:

| Ordnung | Vollständig enumerierte Bosonkonfigurationen | Normquadrat von \(Q_+^kF\) |
|---|---:|---:|
| 0 | analytischer Ausgangszustand | 1 |
| 1 | 60 Kanäle / 480 Paare | 480 |
| 2 | 1830 | 439680 |
| 3 | 37820 | 575078400 |
| 4 | 595665 | 952296652800 |

Zusätzlich wurden unabhängige Wortentwicklungen, Überlaufgrenzen, die
vollständige Zweikörper-Casimiridentität, rationale Sektorvergleiche und
die unabhängige Symmetriespurrechnung wiederholt. Die vier ausgewählten
ursprünglichen Zertifikate bestehen normal und unter `-OO` mit identischen
JSON-Bytes. Dies ist eine gezielte erneute Grundzustandsprüfung, nicht die
Behauptung, alle historischen Repository-Tests erneut ausgeführt zu haben.
Der unveränderte alte Normprüfer gibt unter dem aktuellen NumPy eine
ComplexWarning bei der Ganzzahlkonversion aus. Die neuen Prüfer bestätigen
vor jeder Konversion exakt verschwindende Imaginärteile und ganzzahlige
Realteile des gepinnten W. Die Warnung ist gespeichert und wird nicht
als verlorener Tensoranteil oder als unterdrückter Prüffehler ausgegeben.

Der modellinterne Satz bleibt bestehen: Für
\(0<|g|/\Delta\le1/20\) ist der globale Grundzustand \(\Omega\)
eindeutig, hat N=64 und ist Spin(10)×SU(4)-invariant. Am Zahlenprüfpunkt:

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad \operatorname{gap}(H)>0.007737\Delta.
\]

Der volle Grundzustandsvektor ist damit nicht ausgerechnet. Die fünf
Versuchsvektoren sind keine behauptete invariante Fünferbasis für H.

### 3.2 Das neu eingegangene Polergebnis

Der vollständige technische Bericht v1.6.3 und sein 248-zeiliger Prüfer
wurden gelesen; Quellen, Bericht, Ergebnismatrix und Prüfpaket wurden
unverändert archiviert. Der Prüfer wurde normal und optimiert wiederholt:
**317 Prüfbedingungen, identische JSON-Bytes auch zum gelieferten Bericht**.

Der Herkunftspin des Prüfers ist
`fdbcabd244450c302182086d67c68284634c994e3fee026200c42c508f731654`.
Er verwendet denselben ursprünglichen `verify_hole.py`-Quellstand wie
die bisherige Fortsetzung. Die neuen eigenen Sektorvergleiche wurden
zusätzlich unabhängig mit rationalen LDL-Pivots berechnet.

Die Prüfzahlen zählen auch Komponenten und Wiederholungen; sie sind
keine Zahl unabhängiger Entdeckungen. Die analytischen Argumente sind
ausgeschrieben, aber nicht vollständig in einem Beweisassistenten formalisiert.

## 4. Der einfache native Anschluss: Bewegungsgleichung statt Umdeutung

Erweitere jede W-Zeile zur antisymmetrischen Matrix \(M_A\) mit
\((M_A)_{ij}=W_{A,ij}\) für i<j. Definiere

\[
D_r=\sum_{A,j}(M_A)_{rj}b_Af_j^\dagger,
\qquad \phi_r=D_r/\sqrt{15}.
\]

Direkte CAR/CCR-Normalordnung liefert **Operatoridentitäten auf dem
endlichen Teilchenkern**, nicht nur Gleichheiten auf Testzuständen:

\[
\boxed{[H,f_r]=-gD_r,\qquad [H,f_r^\dagger]=gD_r^\dagger,}
\]
\[
[N,D_r]=-D_r,\qquad \{f_r,D_s^\dagger\}=0.
\]

Der neue Vergleichsoperator hat also dieselbe Ladung −1 wie f.
Er ist nicht das früher auf dem leeren Referenzzustand betrachtete
\(\chi^\dagger\sim b^\dagger f^\dagger\) mit Ladung +3.
Auf dem Grundzustand liegen \(f\Omega\) und \(D\Omega\) in N=63,
\(\chi^\dagger\Omega\) dagegen in N=67. Neutrale Zeitentwicklung
hebt diese Unterscheidung nicht auf.

Die Normalordnungsprüfung erfasst alle 64 ursprünglichen f-Operatoren
und die tatsächlichen W-Vorzeichen. Für die Kompositnorm gilt exakt

\[
\{D_r,D_s^\dagger\}=
\sum_{A,B,j,k}(M_A)_{rj}(M_B)_{sk}
\left(\delta_{AB}f_j^\dagger f_k+\delta_{jk}b_B^\dagger b_A\right).
\]

Mit \(\bar b=\langle N_b\rangle\) und der Grundzustandssymmetrie:

\[
\langle\{D_r,D_s^\dagger\}\rangle=\delta_{rs}S,
\qquad S=15-\frac7{32}\bar b.
\]

\(\phi\) hat entsprechend Norm \(1-7\bar b/480\), nicht globale
kanonische CAR. Der normierte Zustandserwartungswert ersetzt keine
Operatorrelation.

## 5. Dieselbe Antwort auf demselben Grundzustand

Für Im z>0 und \(H_n=H|_{N=n}\):

\[
G_{rs}(z)=\langle\Omega|f_r(z+E_0-H_{65})^{-1}f_s^\dagger|\Omega\rangle
+\langle\Omega|f_s^\dagger(z-E_0+H_{63})^{-1}f_r|\Omega\rangle.
\]

Die innere Symmetrie macht G diagonal und alle Diagonalelemente gleich.
Schreibe mit positiven Entnahme- und Additionsmaßen auf \(\epsilon>0\)

\[
G(z)=\int\frac{d\nu_+(\epsilon)}{z-\epsilon}
+\int\frac{d\nu_-(\epsilon)}{z+\epsilon}.
\]

Dann gelten exakt

\[
Z_+=\bar b/32,\quad Z_-=1-\bar b/32,
\quad a:=\int\epsilon\,d\nu_+=\int\epsilon\,d\nu_-
=\frac{\Delta\bar b-E_0}{64}.
\]

Für das gesamte signierte Spektralmaß:

\[
\boxed{m_0=1,\quad m_1=0,\quad m_2=g^2S,\quad
m_3=g^2(\Delta S+7a).}
\]

Die ersten beiden Momente und die Kanalgewichte stimmen mit der
eingegangenen unabhängigen Rechnung überein. **Das dritte Moment ist der
zusätzliche eigene Schritt dieser Revision.**

### 5.1 Herleitung des dritten Moments

Setze \(\mathcal L A=[A,H]\). Stationarität macht diesen Operator
symmetrisch in der positiven, nach Nullvektoren quotientierten Metrik
\((A,B)=\langle\{A^\dagger,B\}\rangle\). Direkte Normalordnung ergibt

\[
\sum_r\{[D_r,X],D_r^\dagger\}=-14Q_+.
\]

Die beiden Beiträge sind \(16Q_+\) und \(-30Q_+\). Ihre Koeffizienten
folgen aus den vollständig geprüften Kontraktionen
\(\sum_{rj}M_{A,rj}M_{B,rj}=16\delta_{AB}\) und
\(\sum_{Ar}M_{A,rj}M_{A,rk}=15\delta_{jk}\).
Mit \([D,N_b]=D\) und
\(\langle Q_+\rangle=(E_0-\Delta\bar b)/(2g)\) folgt die Formel.

Als unabhängige Kontrolle wurden sämtliche Formeln einschließlich m3
an der früher exakt geschlossenen N=4/N=5-Antwort symbolisch geprüft.
Diese Kontrolle verwendet den früheren Referenzzustand nur als Test
der Identitäten, nicht als Ersatz für den nativen Grundzustand.

Die allgemeine Methode, Spektralmomente aus Bewegungsgleichungen zu
gewinnen, ist etabliert; siehe
[Freericks und Turkowski, Phys. Rev. B 80, 115119](https://arxiv.org/abs/0907.1284).
Die hier angegebenen W-Kontraktionen und Konstanten wurden eigenständig
für dieses Modell berechnet; die zitierte Arbeit beweist keine TFPT-Aussage.

### 5.2 Neue engere Dichte- und Gewichtsgrenzen

Positivität der beiden Antwort-Grammatrizen beziehungsweise zweimal
Cauchy-Schwarz liefern

\[
m_2\ge a^2\left(\frac1{Z_-}+\frac1{Z_+}\right),
\]
\[
\boxed{(\Delta\bar b-E_0)^2\le
60g^2\bar b(32-\bar b)(1-7\bar b/480).}
\]

Mit der bereits bewiesenen Energieobergrenze und \(g/\Delta=1/20\)
muss das folgende rationale Polynom positiv sein:

\[
P(b)=\frac7{3200}b^3-\frac{61}{50}b^2
+\frac{317591}{125000}b-\frac{79754843281}{62500000000}>0.
\]

Seine beiden im alten zulässigen Bereich liegenden Nullstellen liegen
bei ungefähr 0.842846697 und 1.245655664. Exakte rationale Wurzelisolation
ergibt die nach außen gerundete strenge Schranke

\[
\boxed{0.842846<\bar b<1.245656.}
\]

Damit:

| Größe pro Mode | Strenges offenes Intervall |
|---|---:|
| Gesamtes Additionsgewicht | (0.0263389375, 0.03892675) |
| Gesamtes Entnahmegewicht | (0.96107325, 0.9736610625) |
| \(\langle\{\phi,\phi^\dagger\}\rangle\) | (0.981834183333…, 0.987708495833…) |
| Frühere \(\chi\)-Kompositnorm, nicht \(\phi\) | (0.040386370833…, 0.059687683333…) |

Das sind Erwartungswerte und integrierte Spektralgewichte, keine direkten
Nachweise von Produktionsraten oder von bereits verfügbaren Messinstrumenten.

## 6. Der Polsatz und seine zusätzliche Verschärfung

Der eingegangene Beweis verwendet
\(u_{k,r}=Q_+^kf_rF=f_rQ_+^kF\). Invarianz und Besetzung ergeben

\[
\langle u_{k,r},u_{k,s}\rangle=
\delta_{rs}\frac{64-2k}{64}\|Q_+^kF\|^2.
\]

Die Normen lauten 1, 465, 412200, 521164800, 833259571200.
Die daraus gebildete fünfdimensionale Variationsmatrix gibt 64 unabhängige
Richtungen unter \(-1.095812\Delta\). Das gesamte N=63-Komplement des
Nullbosonraums liegt über \(-3\Delta/4\). Minimax begrenzt den niedrigen
Raum auf genau 64 Dimensionen; seine injektive symmetrieverträgliche
Projektion auf die irreduzible duale 64 erzwingt ein einziges Energieniveau.

Das beweist Existenz und Isolation. Seine Sichtbarkeit folgt aus den
positiven Entnahmemomenten. Mit

\[
d=0.007737\Delta,\quad c=0.379636\Delta,
\quad a_{\max}=\frac{1.245656+1.158089}{64}\Delta
\]

gilt

\[
Z_{\rm low}>\frac{c(1-1.245656/32)-a_{\max}}{c-d}
=\frac{40912436089}{46487375000}
=0.8800762806891118\ldots.
\]

Außerdem ist der niedrige Pol die kleinste Entnahmeenergie. Daher
\(a\ge\epsilon_{\rm low}Z_-\), also bereits ohne vollständige
Polauswertung

\[
\frac{\epsilon_{\rm low}}\Delta
<\frac{1.245656+1.158089}{64-2(1.245656)}
=\frac{2403745}{61508688}=0.039079763821332\ldots.
\]

Diese Verschärfungen entstehen aus dem **Zusammenführen kompatibler
Beweise**, nicht aus einem neuen gewählten Parameter. Das Restgewicht
des gesamten CAR-Maßes ist somit kleiner als 0.119923719311… .

## 7. Einfache Organisation, aber keine falsche Zwei-Linien-Lösung

Die ersten zwei orthonormalen Operatoren sind f und \(D/\sqrt S\).
Die erste Resolventenreduktion hat deshalb die exakte Form

\[
\boxed{G(z)=\frac1{z-\displaystyle\frac{g^2S}{z-a_1-\Sigma_2(z)}}},
\qquad a_1=\Delta+\frac{7a}{S}.
\]

\(\Sigma_2\) ist die Resolvente des verbleibenden nativen Operatorraums,
gekoppelt an den dazu orthogonalen Rest von
\(\mathcal L(D/\sqrt S)\). Es wurde kein äußeres Bad hinzugefügt.
Dies ist eine genaue Ordnung der Rechnung, **keine abgeschlossene
Berechnung von \(\Sigma_2\)** und keine Vereinigung sämtlicher TOE-Aufgaben
in einer einzigen bereits gelösten Funktion.

### 7.1 Warum man die Rückwirkung nicht exakt weglassen darf

Angenommen, es gäbe nur je eine Entnahme- und Additionslinie mit
Energien \(\epsilon_-,\epsilon_+\). Symmetrie macht diese für alle r gleich.
Dann liefern die Bewegungsgleichungen auf demselben Grundzustand

\[
D_r\Omega=-\frac{\epsilon_-}{g}f_r\Omega,
\qquad D_r^\dagger\Omega=\frac{\epsilon_+}{g}f_r^\dagger\Omega.
\]

Summe nach Multiplikation mit \(f_r^\dagger\) beziehungsweise \(f_r\)
und N=64 ergeben

\[
H\Omega=\left[-32\epsilon_-+
(\Delta-\epsilon_++\epsilon_-)N_b\right]\Omega.
\]

Ein Eigenzustand mit negativer Energie kann keine feste Bosonenzahl haben:
Dann wäre \(\langle Q_++Q_-\rangle=0\) und seine Energie
\(\Delta\langle N_b\rangle\ge0\). Daher sind \(\Omega\) und
\(N_b\Omega\) unabhängig. Die angenommene Zweilinienform erzwingt
\(\epsilon_+-\epsilon_-=\Delta\).

Andererseits geben \(m_0=1,m_1=0\) für ein Zweilinienmaß
\(m_3/m_2=\epsilon_+-\epsilon_-\). Die exakt bestimmte Formel lautet
jedoch

\[
\frac{m_3}{m_2}=\Delta+7a/S>\Delta.
\]

Widerspruch. Damit ist \(\Sigma_2\not\equiv0\) bewiesen. Mindestens
ein Kanal besitzt mehr als eine Energielinie. Der dominante isolierte
Entnahmepol und diese unvermeidliche Reststruktur widersprechen einander nicht.
Eine Zweilinienform könnte höchstens eine zu zertifizierende Näherung sein.

## 8. Was der Operationssatz jetzt tatsächlich hergibt

| Vertrag | Mathematisch abgesichert | Nicht dadurch verfügbar |
|---|---|---|
| Markierter endlicher Matrixcompiler | Matrizen, Ordnungen, konkrete endliche Syntheseidentitäten | Vollständiges Fockinstrument, Präparation, physischer Zeitgenerator |
| H allein | Modellzeitentwicklung | Unabhängiges Schalten von X und \(N_b\) |
| X und \(N_b\), wenn als Kontrollen gewährt | N=3-Kontrollalgebra der Dimension 14 | Beliebige Modenoperationen |
| Zusätzlich dokumentierter vorzeichenrichtiger Clock-Lift | N=3-Kontrollalgebra der Dimension **84** | Vollständige Zustandsunterscheidung oder Ladung-eins-Instrument |

Die neue Clock-Rechnung wurde übernommen und reproduziert. Die fünf
Multiplizitätszeilen für die sechs Clockphasen sind:

| Teilraum | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Dunkle F3 | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |
| Dunkle BF | 16 | 8 | 8 | 16 | 8 | 8 |
| Aktiv 7 | 560 | 440 | 440 | 560 | 440 | 440 |
| Aktiv 10 | 112 | 88 | 88 | 112 | 88 | 88 |
| Aktiv 12 | 80 | 40 | 40 | 80 | 40 | 40 |

Die aktiven Zeilen tragen zusätzlich einen Zweiniveaufaktor. Alle 45504
N=3-Zustände sind erfasst; der Kommutant hat weiterhin Dimension
240742144. Die alte Zahl 14 beschreibt den engeren Zweikontrollvertrag,
nicht den jetzt zusätzlich geprüften Clockvertrag.

### 8.1 Konkrete Präparationsgrenze

Alle genannten Fockkontrollen erhalten N. Ein Wort aus ihnen und jeder
einzeln zahlenerhaltende ausgewählte Messzweig bleiben im Ausgangssektor.
Sie können aus dem leeren N=0-Zustand **nicht** den N=64-Grundzustand
erzeugen. Diese Aussage betrifft zahlenerhaltende Krauszweige; eine bloß
U(1)-kovariante offene Dynamik kann sehr wohl geladene Krausoperatoren haben.

Auch aus dem voll besetzten F führt bloßes \(e^{-itH}\) nicht zur
Konvergenz auf \(\Omega\): Der Grundzustandsüberlapp bleibt konstant.
Normiertes \(e^{-\tau H}F\) konvergiert mathematisch mit der bewiesenen
Lücke, benötigt aber eine gesonderte Instrument- und Ressourcenherleitung.

### 8.2 Der kleinste konkrete Ladungstest

Ein Kandidat ist eine explizite Referenzmode c mit
\(T=\lambda(c^\dagger f_r+f_r^\dagger c)\). Sie erhält die gemeinsame
Ladung, verändert aber die Ladung der ursprünglichen Bank. Der endliche
Austausch- und Detuningtest ist exakt; **dieses T wurde nicht als neuer
nativer Hamiltonterm eingeführt**.

Für dieselbe N=64-Präparation unter \(H+\mu N\) gilt
\(G_\mu(z)=G_0(z-\mu)\), insbesondere \(m_1=\mu\).
Das misst nur gegen eine festgelegte Referenz: Ein gemeinsamer Zusatz
\(\mu(N_{\rm Bank}+N_{\rm Referenz})\) bleibt unsichtbar. Die Spektral-
schranken dieses Berichts gelten als Grundzustandsschranken nur für μ=0.

## 9. Relativistisches Wörterbuch: Ausschluss und zwei präzise Alternativen

Die Indexfrage darf nicht nachträglich durch einen Namen beantwortet werden.
Die Konventionen für Zweikomponentenspinoren wurden mit
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) abgeglichen;
die folgenden speziellen W-Tests sind eigene exakte Tensorrechnungen.

### 9.1 Was nicht funktioniert

Für 64 gleichhändige Weylfelder mit innerem Index I und einen skalaren
Vermittler ist \(M_A\otimes\varepsilon_{\rm Lorentz}\) symmetrisch.
Die Grassmann-Antisymmetrisierung verschwindet daher identisch, für alle
60 W-Zeilen. Außerdem lässt die volle irreduzible innere Darstellung
\(16\otimes4\) auf denselben 64 Komponenten nach Schur keine zusätzliche
kommutierende nichttriviale Lorentzspinorwirkung zu.

### 9.2 Bereits bekannter nichtverschwindender Typ

Ein symmetrischer Lorentzspinortensor koppelt an das antisymmetrische M.
Der Vermittler hat dann einen passenden dualen (1,0)-Typ samt adjungiertem
Typ. Diese Variante besteht den algebraischen Nichtnulltest, aber noch
keinen vollständigen Kinetik-, Positivitäts-, Constraints- oder Herkunftstest.

### 9.3 Neue minimale skalare Alternative - ausdrücklich zusätzlich

Will man zugleich W, gleiche Weylhand, lokale Bilinearität und einen
skalaren Vermittler behalten, kann man einen **unabhängigen** Hilfsindex
a=1,2 mit alternierender Form einführen:

\[
b_A^\dagger(M_A)_{IJ}\varepsilon_{ab}
\varepsilon_{\alpha\beta}\psi_{I a\alpha}\psi_{J b\beta}
+\mathrm{h.c.}
\]

M und \(\varepsilon_{ab}\) sind jeweils antisymmetrisch; ihr Produkt
ist als innerer Kopplungstensor symmetrisch. Zusammen mit der Lorentz-
Epsilonform ist der Gesamttensor antisymmetrisch und nicht null.
Alle 60 Kanäle bestehen den Test. Eine nichtverschwindende alternierende
Form existiert nicht in Dimension eins; in Dimension zwei ist sie bis
auf Normierung eindeutig. **In dieser eng benannten Klasse von
Tensorfaktor-Reparaturen ist die binäre Ergänzung minimal.**

Das ist noch keine gefundene native Lösung: Sie verdoppelt die inneren
Weylkomponenten von 64 auf 128, zusätzlich zu deren Lorentzspinorindex.
Ein Double-Cover-Minuszeichen stellt nicht automatisch zwei unabhängige
Felder bereit. Auch Nambu-Umbenennung \((f,f^\dagger)\) genügt nicht:
Das gemischte Produkt hat Ladung null statt −2, sodass derselbe
\(b^\dagger ff\)-Ladungsvertrag nicht erhalten bleibt.

Der entscheidende Quellenauftrag ist daher eng: Gibt es diese zweite
gleichgeladene, CAR-unabhängige Komponente bereits im tatsächlichen
Compilerprozess? Und liefert ihre Projektion genau das bisherige H und
die geprüfte Antwort? Ohne beides bleibt die skalare Alternative ein
zusätzliches Modell, nicht eine Erklärung des ursprünglichen.

## 10. Nächste Schritte mit eindeutiger Erfolgskontrolle

1. **Native Quelle des Austauschoperators bestimmen.** Ein tatsächliches
   Operationswort mit Anfangszustand, Detektor, Adjungiertem, Ladungsbilanz
   und Record angeben. Ein weiteres neutrales Wort oder bloßer
   Algebraabschluss schließt diese Aufgabe nicht.
2. **Den Rest der nativen Antwort kontrollieren.** Das nächste Ziel ist
   \(\Sigma_2\) beziehungsweise sein erster Norm- und Momentkoeffizient,
   gemeinsam in N=63,64,65. Die vorliegenden Summenregeln und Polschranken
   sind zwingende Akzeptanztests. Den Rest auf null zu setzen ist exakt
   ausgeschlossen; eine Näherung braucht eine Restfehlergrenze.
3. **Die beiden Feldtypen an der Quelle entscheiden.** Entweder der
   symmetrische Vermittler mit korrektem Adjungierten und Kinetik, oder
   der skalare Typ mit wirklich nachgewiesener zweiter Komponente.
   Erst Nichtnullkopplung, Symmetrie, Ladung, CAR und positive Kinetik
   gemeinsam zählen als Feldadapter.
4. **Erst danach zwei operational bestimmte Teile verbinden.** Für einen
   tatsächlich hergeleiteten ungeraden Austausch wäre das projizierte
   Ein-Loch-Transfermatrixelement proportional zum jetzt eingeschlossenen
   Residuum. Ein solches formales Matrixelement beweist weder Verfügbarkeit
   des Austauschs noch einen isolierten Zweibank-Gesamtraum oder höhere
   Störungsordnungen. Eine räumliche Skalierung wurde hier nicht vorgezogen.

| Tor | Nutzen dieser Revision | Entscheidender verbleibender Nachweis |
|---|---|---|
| T1 | Exakter Clock-Kontrollabschluss und engere Ressourcenfrage | Ursprüngliches vollständiges Operations- und Rahmenwörterbuch |
| T2 | Geladene native Antwort, sichtbarer Pol, drittes Moment | Quelleneinbettung und renormiertes Half-Charge-Feld mit Energie/Adjungiertem |
| T3 | Präzise Anforderung an ungeraden Austausch | Gemeinsamer operationaler räumlicher, schließlich 3+1D-Träger |
| T4 | Falscher Skalartyp ausgeschlossen, minimale Alternativen | Chirales Maß, Anomalien, Spiegelkontrolle, vollständige Feldkinetik |
| T5 | Pole und Reststruktur lokal kontrolliert | Gemeinsamer wechselwirkender Grenzwert, Clusterstruktur, Streuung |
| T6 | Strengere interne/Lorentz-Indexbilanz | Familien, Massen und Kopplungen auf demselben physikalischen Träger |
| T7 | Keine neue Spin-2-Konstruktion | Dynamischer Spin 2, Helizitäten und universelle Kopplung |
| T8 | Eindeutiger Modellgrundzustand; Präparationslücke konkret | Primitive Zustandswahl, Ressourcen, Records und Instrumente |

## 11. Erratum und Versionsdisziplin

Im eigenen v1.6.2-Text fehlte in Abschnitt 5.2 zwischen Entnahme- und
Additionsresolvente ein Pluszeichen. Richtig ist auf der dortigen
N=4-Referenz
\(G=Z_h/(z+\epsilon_h)+a^\dagger(z+E_--H_5)^{-1}a\).
Die früheren Prüfrechnungen verwendeten die additive CAR-Gewichtsregel;
der Darstellungsfehler wird hier ausdrücklich korrigiert. Die archivierte
v1.6.2 wird nicht stillschweigend umgeschrieben.

Die zugelieferte v1.6.3 bleibt ebenfalls unverändert. Ihre Pol- und
Clockbefunde sind als übernommene und frisch reproduzierte Ergebnisse
kenntlich. Die engeren Schranken, das dritte Moment, der Ausschluss der
exakten Zweilinienantwort und die minimale skalare Hilfsindexalternative
sind die eigenen zusätzlichen Ergebnisse dieser Konsolidierung.
Kein literaturweiter Neuheitsanspruch, keine experimentelle Bestätigung
und kein Gesamtabschluss werden behauptet.


---

# Nutzerquelle A: vollständige Runde v1.6.3

Unveränderte Quelle. Nicht alle Aussagen darin werden übernommen. Entscheidend sind die Quellenprüfung und Korrekturen in v1.6.7.

A. Rahmen der Runde v1.6.3
Ausgangspunkt ist v1.6.2 §14 mit den vier Prioritäten in deiner Reihenfolge: (1) Operationssatz und Kommutant, (2) nativer Grundzustand und geladene Antwort darauf, (3) Feldwörterbuch am Tensor, (4) räumliche Skalierung erst danach. (4) ist ausdrücklich nicht Gegenstand. Modell unverändert: H = ΔN_b + gΣ_A(b_A†P_A + P_A†b_A), P_A = Σ_{i<j}W_{A,ij}f_jf_i, 64 Fermionmoden, 60 Bosonmoden, N = N_f + 2N_b. Kein neuer Term.

Fundament common.py (PASS, 6 Prüfgruppen): Tensor W repo-lokal, SHA 3f00a089…; WWᵀ = 8·I₆₀; 60 Kanäle × 8 disjunkte Paare auf 16 Moden, jede Mode in genau 15 Kanälen; Gewichtserhaltung q_i+q_j = q_A auf allen 480 Paaren; Casimir-Identität 8WᵀW + 𝒞_S + 𝒞_C − 120·I = 0 auf allen 2016 Zweiteilchenzuständen; induzierte Bosongeneratoren X_B = WΛ²(X)Wᵀ/8 gaußganzzahlig mit exakter Kovarianz; gepinnter Clock (SHA 9bf99de7…) mit Periode 6, Slot-Permutation [2,0,1,4,3], Vorzeichen −1, WΛ²G_F = G_B·W exakt.

B. Operationssatz und Kommutant (operations_commutant.py, PASS, 162 Guards, 0 Bareiss-Fallbacks)
Frage: Welche „unsichtbare“ Freiheit bleibt, wenn nur bestimmte Operationen verfügbar sind? Gemessen als Dimension des Kommutanten der von der Stufe erzeugten Algebra auf dem N-Sektor. Kleiner Kommutant = mehr unterscheidbar.

Spektralzertifikat N=3 (exakt): S = C₃C₃ᵀ annulliert durch ∏(S−r) für r ∈ {0,7,10,12} (Residuum 0 nnz), Multiplizitäten 64/2880/576/320 aus rationalen Projektorspuren, tr S = 29760, tr S² = 244800.

Irreduzibel-Zerlegung (Höchstgewichtsvektoren, exakt; Gewichte in verdoppelten Koordinaten):

Sektor	Block	Dim	Zerlegung unter so(10)⊕su(4)	Casimir (𝒞_S, 𝒞_C)
N=2
helle Paare↔Bosonen
60
(10, 6) ×1
(36, 20)
N=2
dunkle Paare
1956
(120, 10) ⊕ (126, 6), je ×1
(84,36), (100,20)
N=3
dunkle Tripel = ker C₃
37888
(560, 20″) ⊕ (1200, 20) ⊕ (672, 4̄), je ×1
(117,63), (141,39), (165,15)
N=3
ker S (der χ-Raum)
64
(16, 4̄) ×1
(45, 15)
N=3
λ=12
320
(16, 20) ×1
(45, 39)
N=3
λ=10
576
(144, 4̄) ×1
(85, 15)
N=3
λ=7
2880
(144, 20) ×1
(85, 39)
Alle Multiplizitäten sind 1; Summenprobe über Weyl-Dimensionsformel bestanden. Meine vorab formulierte Hypothese stimmt in allen Blöcken.

Kommutanten-Leiter:

Stufe (verfügbare Operationen)	N=2	N=3
A: nur {X, N_b} (die zwei bisher geprüften Kontrollen)
3 829 536
1 444 233 216
B: A + Clock (Ordnung 6)
641 760
240 742 144
Cc: A + 15 su(4)-Generatoren
30 376
2 247 168
Cs: A + 45 so(10)-Generatoren
172
1 648
C: A + alle 60 Generatoren
3
7
D: B + C
3
7
volle Algebra B(H_N)
1
1
Lesart: Die zwei Kontrollen lassen ~1,4·10⁹ unsichtbare Freiheitsgrade in N=3; der Clock allein reduziert um einen Faktor 6 (seine Eigenwertmultiplizitäten sind fast gleichverteilt, z.B. 6384/6280/6280/6384/6280/6280 auf dem Dunkelraum); erst die volle innere Symmetrie als Operationssatz kollabiert alles auf 7 Skalare - je einen pro (Energieblock, Irrep). so(10) ist dabei die weit wirksamere Hälfte (1648 vs. 2,2 Mio). Das ist genau die in v1.6.2 §10.3 geforderte Abgrenzung: Mehrfachwiederholung der zwei Kontrollen beseitigt nichts; die Existenz der Symmetrieoperationen als Operationen ist damit nicht bewiesen, aber ihr Effekt ist jetzt exakt beziffert.

Clock-Befund: Der Clock wirkt auf keinem irreduziblen Block als Skalar (er verschiebt Gewichte, Zeuge z.B. [−2,−2,0,−2,0]); er liegt also nicht in der zusammenhängenden Symmetriegruppe, sondern ist ein äußeres Element (Slot-Permutation). D = C gilt trotzdem, weil alle Multiplizitäten 1 sind und der Clock jeden Block in sich abbildet.

C. Nativer Grundzustand N=64 (native_ground_state.py, PASS, 128 Guards: 119 exakt, 9 numerisch)
C.1 Lochbild (Operatoridentität, geguardet). Mit h_i = f_i† ist |F⟩ = f_0†…f_63†|0⟩ das Lochvakuum und P_A = −Q_A†, Q_A† = Σ_{i<j}W_{A,ij}h_i†h_j†. Unter (−1)^{N_b}: H ≅ H_hole = ΔN_b + gΣ(b_A†Q_A† + Q_Ab_A). Die Teilchen-Loch-Unitäre trägt das Vorzeichen s(μ) = (−1)^{i+j} pro Zweilochzustand; Negativkontrolle: ohne s(μ) ist die Komplement-Abbildung keine Identität.

C.2 Exakte Krylov-Kette v_n = (T†)ⁿ|F⟩, T† = Σb_A†Q_A†:

n	Einträge in v_n	ν_n = ‖v_n‖²	ν_n/ν_{n−1}
0
1
1
-
1
480
480
480
2
108 240
439 680
916 = 4·229
3
15 252 960
575 078 400
299520/229 ≈ 1307,95
4
(nicht speicherbar)
952 296 652 800 (Spurnetzwerk)
≈ 1656,0
ν₃ wurde zweifach unabhängig erhalten: durch die 15-Millionen-Einträge-Vektorrechnung und durch die Onishi/Wick-Spurnetzwerkformel (Abschnitt E). Exakte Übereinstimmung.

C.3 Exakte Guards: T v₁ = 480 v₀; T v₂ = 916 v₁ (Eindeutigkeit des Ein-Boson-Singuletts (60⊗Λ²64̄)^G, zuvor gruppentheoretisch vorhergesagt); Adjungiertheit ⟨v₂|Tv₃⟩ = ν₃; v₁, v₂ werden von 3 so(10)- und 3 su(4)-Generatoren annulliert (Singuletts); ⟨v₁|Σ_A Q_AQ_A†|v₁⟩ = 458·480 = 219 840 - bestätigt die korrigierte Formel Σ_A Q_AQ_A† = 480 − (15N_h + C_std^{Loch})/2 mit dem Loch-Casimir 14 der (10,6) (meine erste Annahme „480 − 15k“ war falsch und ist durch die Rechnung ersetzt).

C.4 Schließungstest. T v₃ = α v₂ + w₂ mit α = 299520/229 und w₂ ⊥ v₂, ‖w₂‖² = 5001523200/229 ≈ 2,184·10⁷ (exakt, Pythagoras-Identität ‖w₂‖² = ‖Tv₃‖² − ν₃²/ν₂ als Guard). Defekt ‖w₂‖²/‖Tv₃‖² = 2,90·10⁻⁵. Folge: Der Zwei-Boson-Singulettraum ist > 1-dimensional, die Kette ist exakt nicht geschlossen und das Modell nicht allein durch die ν_n lösbar; numerisch ist die Korrektur vernachlässigbar (Kopplung g·√(‖w₂‖²/ν₃) = 0,195g, Energieänderung in der 6. Stelle).

C.5 Exakte Ritz-Matrix (Δ=1, g herausfaktorisiert, Basis v₀…v₃, w₂): Diagonale 0, 1, 2, 3, (2 für w₂); Nebendiagonalen 4√30, 2√229, 48√29770/229; w₂ koppelt nur an v₃ mit 3√598377/11908.

C.6 Ritz-Obergrenzen E_K(64) (rigoros, Rayleigh-Ritz):

g/Δ	K=1	K=2	K=3 (+w₂)	Störungstheorie 2. Ordnung −480g²
1/20
−0,704159
−0,985178
−1,094232
−1,2
1/40
−0,241620
−0,288824
−0,295357
−0,3
1/100
−0,045894
−0,047851
−0,047894
−0,048
1/400
−0,002991
−0,003000
−0,003000
−0,003
Bei g/Δ = 1/20 ist die Kette nicht konvergiert (Kopplungen ≈ 1,1Δ … 1,6Δ je Stufe); dafür laufen ν₅ (und mit ν₄ die Verlängerung auf K=5). Bei ≤ 1/40 ist die Konvergenz praktisch erreicht.

C.7 Observablen bei g/Δ = 1/20 auf dem K=3-Ritz-Zustand Ω (Näherung): ⟨N_b⟩ = 0,8421 (Hellmann-Feynman ∂E/∂Δ = 0,8421 ✓); Überlapp |⟨F|Ω⟩|² = 0,397; Bosonzahlverteilung p₀…p₃ = 0,397 / 0,397 / 0,172 / 0,034; Shannon-Untergrenze der Boson-Loch-Verschränkung 1,66 bit (rigorose Untergrenze, da die reduzierte Bosondichte in N_b blockdiagonal ist). Worker-Behauptungen „Überlapp > 1/4“ und „> 0,811 bit“: konsistent, aber nicht konvergiert.

C.8 Geladene Ein-Teilchen-Antwort auf Ω (Guard auf r = 0, 5, 63, Transitivität): Entnahme f_r|Ω⟩ (nach N=63): Z_h = 1 − ⟨N_b⟩/32 = 0,97368; Addition f_r†|Ω⟩ (nach N=65): Z_add = ⟨N_b⟩/32 = 0,02632; Z_h + Z_add = 1 exakt. Mittlere Anregungsenergie der Entnahme ε_h = 0,0311Δ, der Addition ε_add = 1,1497Δ. Kompositnorm Z_χ = 23⟨N_b⟩/480 = 0,0404 (v1.6.2-N=4-Referenz 0,0301 - anderer Zustand, nur zur Einordnung).

C.9 Sektorauswahl und Worker-Behauptung. Untergrenzen aus H ≥ (1−θ)ΔN_b − (15g²/2θΔ)N_f (Casimir-Identität + quadratische Ergänzung), korrekt als max_θ min_{N_b}:

g/Δ	Ritz E(64)	schärfster Konkurrent	N=64 bewiesen global?
1/400
−0,0029996
N=63: −0,0029531
ja
1/100
−0,047894
N=63: −0,04725
ja
1/40
−0,295357
N=63: −0,2953125
ja (Abstand 4,5·10⁻⁵)
1/20
−1,094232
N=66: −1,2; N=62: −1,1625
nein
Bewiesener Bereich mit diesen Schranken: g/Δ ≤ 0,0251 (Bisektion). Die Worker-Behauptung „eindeutiger N=64-Singulett-Grundzustand für 0 < |g|/Δ ≤ 1/20“ ist damit nicht reproduziert und nicht widerlegt: Die verwendeten Untergrenzen sind zu grob; bei 1/20 müsste E(64) < −1,2 (gegen N ≥ 66) und < −1,1625 (gegen N=62) gezeigt werden. Ob die konvergierte Kette dorthin kommt, entscheidet der laufende ν₅-Schritt. Chemisches Potential: μ* = −E/64 = 0,0171Δ < Δ/50, die frühere Aussage „μ = Δ/50 wählt den leeren Zustand“ bleibt konsistent.

D. Feldwörterbuch am Tensor (field_dictionary.py, PASS, 29 Guards)
D.1 Allgemeine Regel (bewiesen, auf allen 60 Zeilen explizit nachgerechnet): Für Grassmann-Felder ψ_{I,a} koppelt der antisymmetrische Tensor W_{IJ} genau an den symmetrischen Teil des Spinorkerns K_{ab}.

Zuordnung	Spinorkern K	Symmetrie	Kopplung an W
gleichhändige Weyl, Boson Skalar (0,0)
ε_{αβ}
antisym.
0 (60/60 Zeilen)
gleichhändige Weyl, Boson (1,0)
σ^{μν}ε
sym.
≠ 0 (Koeffizientenrang 32 je Komponente)
Dirac/Majorana, Skalar C
antisym.
0
Dirac/Majorana, Pseudoskalar Cγ⁵
antisym.
0
Dirac/Majorana, Axialvektor Cγ^μγ⁵
antisym.
0
Dirac/Majorana, Vektor Cγ^μ
sym.
≠ 0
Dirac/Majorana, Tensor Cσ^{μν}
sym.
≠ 0
Der Vermittler kann also nur ein Vektor- oder antisymmetrisches Tensorfeld sein, niemals Skalar/Pseudoskalar/Axialvektor. Er trägt U(1)_N-Ladung 2 (komplexes Feld); Vorbehalt (kein Satz): ein masseloser geladener Vektor ist kein konsistentes freies Eichfeld.

D.2 Chiralitätsgradierungen. Trägergraph: 64 Moden, 480 Kanten, Grad 15, dreiecksfrei, nicht bipartit - ungerader Zyklus [16, 45, 0, 30, 37] (Länge 5, alle Kanten geprüft; unabhängig per BFS bestätigt). Folge: Es gibt keine globale Chiralitätsaufteilung, unter der alle 60 Bosonen Vektoren wären. Für jede der 44 getesteten G-kovarianten Gradierungen ist jeder Kanal rein (0 gemischte Kanäle), aber der Bosonmultiplett zerfällt in Typen:

Gradierung	Vektor-Kanäle	Tensor-Kanäle	Stabilisator-Dim.	Kommutant der 64
Identität (keine Aufspaltung)
0
60
60
1 (Schur; direkt gegengeprüft)
Pati-Salam-Spinorsplit Γ_pq (10 Varianten)
24
36
36 = so(6)⊕so(4)⊕su(4)
2
Farbsplit (3 Varianten)
40
20
52 = so(10)⊕(su(2)²⊕u(1))
2
gemischt (30 Varianten)
32
28
28
4
Ein einheitlicher Lorentztyp für alle 60 Vermittler erzwingt die gleichhändige Zuordnung → nur (1,0)⊕(0,1), also ein antisymmetrischer Tensor B_{μν}. Das ist kein symmetrisches Spin-2-Feld. Kinetische Terme: einer pro irreduziblem Block des Stabilisators (1, 2 oder 4), keine Familienaufspaltung 4 → 1+3.

E. Spurnetzwerk-Normen (norms_by_traces.py, läuft: n=5)
Methode: ν_n/(n!)² = Σ_{|m|=n} ‖Q†^m F‖²/m! über bosonische Kohärenzzustände, Onishi-Determinante det(1 − M̄M)^{1/2} = exp(−½Σ_k tr((M̄M)^k)/k) und Wick-Paarung → Summe über Zyklentypen und Permutationen von Spurnetzwerken; alle Vorfaktoren exakte Fraction. Auswertung auf dem Φ-Tensor Φ_{ij,kl} = Σ_A(M_A){ij}(M_A){kl} (Einträge in {−1,0,1}, geguardet) mit optimalem Pfad; Exaktheit über a-priori-Schranke < 2⁵³ pro Schritt, sonst Fallback modulo fünf Primzahlen < 2¹³ mit CRT (Eindeutigkeit über |Netzwerk| ≤ 60ⁿ·64^{#Zyklen}). Validierung: ν₁ = 480, ν₂ = 439 680 (brute force im Besetzungsbild), ν₃ = 575 078 400 (identisch mit der Vektorrechnung), CRT-Route allein reproduziert ν₃. n=4 in 22 s (112 kanonische Netzwerke), ν₄ = 952 296 652 800. n=5 läuft seit 17 CPU-Minuten.

F. Reparaturen an den Worker-Skripten (relevant für die Bewertung der Zahlen)
Vor dem Cursor-Absturz hinterlassene Skripte hatten folgende Fehler, alle behoben und durch Guards abgesichert: Zyklus-Slots im Spurnetzwerk (ergab ν₂ = 466560 statt 439680); Bosonengewicht ∏m_A! konstant 1; T wirkte bei wiederholtem Boson doppelt (Faktor 4 statt 2 → T nicht adjungiert zu T†, ⟨v₁|Tv₂⟩ = 453120 statt 439680); Merge-Join mit inkonsistenter Ordnung für Loch in Mode 63; Teilchen-Loch-Guard ohne s(μ); Guard ⟨v₁|ΣQQ†|v₁⟩ als Norm der Summe statt Summe der Normen; Sektorschranke min-max statt max-min (unzulässig optimistisch) und als Stub; w₂-Norm um q² = 229² skaliert und an falsches Kettenglied gekoppelt; sympy-Eigenwerte für ≥5×5 Radikalmatrizen (Hänger); JSON-Tupelschlüssel; Schur-Kommutant über instabile inkrementelle SVD; ungültiger „ungerader“ 4-Zyklus-Zeuge; komplexe Generatoren mit vermischten Real-/Imaginärteilen im Singulett-Guard.

Nebenbefund: Das replay_manifest.json der Vorrunde v1.6.2 war um 10:06 durch einen Lauf ohne Zugriff auf den gesperrten Documents-Tensorpfad auf FAIL gesetzt und normal.json geleert. Aus den intakten optimized.json (PASS-Bedingung war Byteidentität) rekonstruiert; Summen 27143/27139/4 stimmen mit dem Delivery-Manifest.

G. Einordnung gegenüber T1-T8
Tor	Beitrag dieser Runde	Weiter offen
T1
Exakte Kommutanten-Leiter A→B→Cc→Cs→C; Clock als äußeres Element identifiziert
Welche Symmetrieoperationen der Compiler tatsächlich bereitstellt
T2
Lochbild bewiesen; Z_h + Z_add = 1; ε_h, ε_add auf dem Ritz-Zustand
Konvergierter Zustand, Renormierung, Grenzraum
T3
-
räumlicher Träger (ausgeklammert)
T4
Vollständige Kern-Symmetrieregel; Nichtbipartitheit → kein einheitliches Vektor-Wörterbuch
chirales Maß, Anomalien
T5
Exakte Krylov-Kette, ν₁…ν₄ zweifach unabhängig
Kontinuumslimes
T7
(1,0)⊕(0,1) ist B_{μν}, kein Spin 2
dynamischer Spin 2
T8
Sektorauswahl bewiesen für g/Δ ≤ 0,0251; Worker-Bereich 1/20 nicht reproduziert; μ*-Fenster
Zustandsfunktional, native Präparation
Kein Tor geschlossen. Keine RH-, Faktorisierungs- oder P-vs-NP-Aussage.

H. Was noch aussteht
ν₅ (läuft) → Verlängerung der Ritz-Kette auf K=5, Neubewertung von E(64) bei 1/20 und der Sektorfrage.
replay.py über alle fünf Prüfer normal + -OO mit Byteidentität, replay_manifest.json.
RESULTS.md / EINFACH_ERKLAERT.md, Kopie nach universal_room/new/ als v1.6.3, Eintrag in universal_room/README.md.

---

# Nutzerquelle B: Korrektur und Zwischenbericht

Unveränderte Quelle. Nicht alle Aussagen darin werden übernommen. Entscheidend sind die Quellenprüfung und Korrekturen in v1.6.7.

Korrektur verifiziert: S0 jetzt **3 829 536 / 1 444 233 216** (deckt sich mit dem v1.6.2-Originalwert und der Parallelsession), 307 Guards, PASS in beiden Modi. Hier der ausführliche Zwischenbericht.

---

# Zwischenbericht: TFPT/Universalraum - fundamentale Lösung, Stand 15.09.2026, ~11:45

## 0. Gesamtlage: zwei Spuren

Es existieren jetzt **zwei Contract-Ordner**, die sich unabhängig auf denselben Kernpunkt zubewegt haben:

| Ordner | Ursprung | Stand |
|---|---|---|
| `universalraum-operations-groundstate-20260915` | **diese Session** (meine drei Arbeitspakete) | WP-A + WP-C fertig, WP-B-Sonde läuft |
| `universalraum-native-ground-response-20260915` | **Parallelsession** (andere Cursor-Sitzung, v1.6.4) | Grundzustand + geladene Antwort + Polsatz bereits konsolidiert |

Die Parallelsession hat dabei einen extern eingegangenen **Polsatz v1.6.3** reproduziert (317 Prüfbedingungen, byteidentisch) und eigene Verschärfungen beigetragen. Beide Spuren validieren sich gegenseitig - mit einer unten dokumentierten Abweichung, die ich inzwischen korrigiert habe.

**Modellvertrag (unverändert in beiden Spuren):** \(H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A)\), \(P_A=\sum_{i<j}W_{A,ij}f_jf_i\), \(N=N_f+2N_b\), 64 Fermionmoden, 60 Bosonmoden, \(WW^\dagger=8I_{60}\), 480 Vertizes, Prüfpunkt \(g/\Delta=1/20\), kein \(\mu N\).

---

## 1. Fundament meiner Session: `native_source.py` (neu, npz-frei)

Problem: der gepinnte Tensor (`spinor_tensors.npz`, SHA-256 `3f00a089…`) liegt unter `~/Documents` - **für die Agenten-Shell macOS-gesperrt** (TCC). Die bisherigen Verträge sind von dieser Shell nicht reproduzierbar.

Lösung: vollständige in-repo-Rekonstruktion aller Objekte aus der Clifford/Außenalgebra-Konstruktion (die Rekonstruktion war in früheren Runden bereits byte-exakt gegen das npz geprüft worden). **17 Guards, PASS**, darunter die volle Zwei-Teilchen-Casimiridentität \(8W^\dagger W+4C_{\text{Spin}(10)}+4C_{\text{SU}(4)}=120\,I\) auf allen 2016 Paarzuständen. Exportiert: `W`, `J`, `C3`, Gewichte `FW/BW`, `BAR/ETA`, die 7 diskreten Symmetriegeneratoren, 60 Lie-Erzeuger, alle CAR-Helfer. Alle drei Checker bauen nur darauf.

---

## 2. WP-A: Der verfügbare Operationssatz (fertig, 307 exakte Guards)

**Frage (v1.6.2 §10.3/§14):** Wie groß ist die unsichtbare Freiheit (Kommutant) unter dem tatsächlich verfügbaren Operationssatz?

### Die Kommutanten-Leiter (N=3-Sektor, 45 504-dim)

| Operationssatz | erzeugte Algebra | Kommutante |
|---|---:|---:|
| S0: {X, N_b} | 14 | **1 444 233 216** |
| S1: + Spin(10)×SU(4)-Rahmen | 743 583 744 | **7** |
| S2: + Clock-Lift | unverändert | 7 |
| S3: + Modenbesetzungen {n_r, m_A} | M₄₅₅₀₄ (2 070 614 016) | **1** |
| S4: + geladene f-Instrumente | M₄₇₅₈₀ (N=2∪N=3) | 1 |

N=2 analog: 3 829 536 → 3 → 3 → 1.

**Korrektur durch mich (Judge):** der Subagent hatte S0 als `Σ 2m²` statt `Σ m²` gerechnet (1 452 961 792 statt 1 444 233 216) - der Guard war eine Tautologie. Jetzt korrigiert und gegen den v1.6.2-Originalwert (`minimal_interfaces.py`) sowie die Parallelsession abgesichert; alle drei Quellen stimmen: **1 444 233 216**.

### Die Isotypie-Zerlegung von N=3 (beide Spuren unabhängig, identisch)

| Block | Dim | Mult | S-Eigenwert | (C_S, C_U) | Rolle |
|---|---:|---:|---:|---|---|
| (144, 20) | 2880 | 2 | **7** | (85, 39) | hell, X-gekoppelt |
| (144, 4̄) | 576 | 2 | **10** | (85, 15) | hell, X-gekoppelt |
| (16′, 20) | 320 | 2 | **12** | (45, 39) | hell, X-gekoppelt |
| (16′, 4̄) | 64 | 1 | 0 (ker S) | (45, 15) | χ-Kompositblock |
| (672, 4̄) | 2688 | 1 | - | (165, 15) | dunkel |
| (1200, 20) | 24 000 | 1 | - | (141, 39) | dunkel |
| (560, 20′) | 11 200 | 1 | - | (117, 63) | dunkel |

Schur-Funktor-Zerlegung exakt geschält: Sym³(16) = 144⊕672, S₂₁(16) = 16′⊕144⊕1200, Λ³(16) = 560. In Λ³(16,4) multiplizitätsfrei; die drei hellen Typen kommen je zweimal vor (eine Kopie pro Seite, X-verknüpft). **Bemerkenswerter Befund (Parallelsession, von meiner Zerlegung bestätigt): alle drei dunklen Blöcke tragen denselben Gesamtcasimir 45** - die eine erhaltene Summeninvariante kann sie prinzipiell nicht trennen; getrennt gelesen (141/4, 117/4, 165/4 bzw. 39/4, 63/4, 15/4) trennen sie sofort.

### Das Verfügbarkeits-Theorem (Parallelsession, `symmetry_availability.py`)

Die gewährte Dynamik (Wörter aus X, N_b) liegt in der Verflechteralgebra (Dim Σmᵢ² = **16**); die 60 Lie-Erzeuger liegen **nicht** darin - keine Komposition gewährter Dynamik erzeugt sie. Die Symmetrie ist ein eigenständiges Primitiv: *gewährt oder nicht gewährt*. Der gesamte verbleibende symmetrieverträgliche Spielraum ist **exakt 2 Dimensionen breit** = die Fähigkeit, die drei dunklen Blöcke getrennt anzusprechen (= beide Casimire getrennt statt nur ihre Summe). Die Clock sitzt im Normalisator, nicht im Zentralisator (mit X, N_b allein: Algebra 84, Kommutant 240 742 144; über voller Symmetrie fügt sie nichts hinzu).

**Antwort auf die §10.3-Frage:** die operative Mehrdeutigkeit ist auf die binäre Alternative „kontinuierliche Symmetrie verfügbar ja/nein" kollabiert - eingeklammert zwischen Kommutant **7** und **1 444 233 216**.

---

## 3. WP-C: Relativistisches Feldwörterbuch (fertig, 2161 exakte Guards, -OO-stabil)

Am tatsächlichen Tensor, vor jeder Kontinuumsrechnung:

| Kanal | Norm² pro Zeile | Status |
|---|---:|---|
| Skalar, gleichhändig ε_{αβ}ψψ | **0** (alle 60 Zeilen, exakt) | **verboten** |
| Skalar, gepunktet (0,0) | 0 | verboten |
| (1,0) symmetrisch {I, σˣ, σᶻ} | je 64, Summe **192** | erlaubt - der Vertex ist **rein (1,0)+h.c.** |
| (0,1) konjugiert | je 64 | erlaubt |

Korrektur meines Spec-Fehlers durch den Agenten: σʸ = −iε ist *anti*symmetrisch; die symmetrische Basis ist {I, σˣ, σᶻ}. Dimensionsidentität C(128,2) = 2080 + 3·2016 = 8128 exakt. Kompositfeld χ = Vermittler × Weyl: zerfällt (3/2,0)⊕(1/2,0), Projektoren Rang 4/2 exakt idempotent, flacher Spin-1/2-Anteil 1/3 (als Konvention deklariert). Bilineare: 4096 = 1 (Singulett) + 45 + 15 (Adjungierte) + 4035 (Rest, ehrlich unbestimmt). Schur-Folge: kinetischer Operator auf dem irreduziblen 64er-Multiplett = I₆₄ ⊗ d(p).

**Konsequenz:** jede relativistische Vervollständigung muss den 60 Vermittlern eine selbstduale Tensor-/feldstärkeartige Lorentzstruktur ((1,0), 3 Komponenten pro internem Label) geben - **der skalare Kopplungskanal ist auf dem tatsächlichen Tensor exakt null und darf nicht wieder verwendet werden**. Die Parallelsession ergänzte eine minimale skalare Alternative mit extra alternierendem Hilfsindex (128 Komponenten) - ausdrücklich als *zusätzliches* Modell markiert, nicht als native Lösung.

---

## 4. WP-B: Nativer Grundzustand (Parallelsession v1.6.4 + meine laufende Sonde)

**Reproduziert (Parallelsession, frische Enumeration statt Statusübernahme):**

| k | Bosonkonfigurationen vollständig enumeriert | ‖Q₊ᵏF‖² |
|---:|---:|---:|
| 0 | analytisch | 1 |
| 1 | 60 Kanäle / 480 Paare | 480 |
| 2 | 1 830 | 439 680 |
| 3 | 37 820 | 575 078 400 |
| 4 | 595 665 | 952 296 652 800 |

**Modellinterner Satz:** für \(0<|g|/\Delta\le 1/20\) ist der globale Grundzustand Ω **eindeutig, N=64, Spin(10)×SU(4)-invariant**; am Prüfpunkt \(-1{,}158089\,\Delta < E_0 < -1{,}129636\,\Delta\), Lücke \(> 0{,}007737\,\Delta\). (Der volle Grundzustandsvektor ist damit nicht ausgerechnet - ehrlich markiert.)

**Meine Session beigesteuert (Sonde, Teil 1):** die **Z4-Zentrumsregel** - Singuletts existieren nur in Sektoren \(N\equiv 0 \bmod 4\) (SU(4)-Zentrumsphase i^N, niveauunabhängig, exakt an Basiszuständen geprüft). Das erklärt, warum die Sektorwahl nur unter N = …, 56, 60, 64, 68, … stattfindet; alle anderen Sektoren haben Casimir-Floors.

**Noch laufend** ([WP-B Sonde](aa1ce128-e016-4c52-ae8f-04d625b04c23)): exakte Singulett-Multiplizitäten mult₁ (=1, der R-Zustand) und mult₂ (Gewicht-0-Unterraum + Casimir-Kern), die exakten Lanczos-Koeffizienten β₂², β₃² (Erwartung aus der Normsequenz: β₁²=480, β₂²=439680/480=**916**, β₃²=299520/229 ≈ 1307,95 - diese Verhältnisform gilt genau dann, wenn die Singuletts pro Niveau eindimensional bleiben, also ist mult₂ der Zwickel), Casimir-Floor c_min=56 auf Λ², Sektorfloors N=56…72, Gruppen-Census. Damit prüfe ich die Kernzahlen der Parallelsession unabhängig nach.

---

## 5. WP-D: Geladene Antwort auf dem Grundzustand (Parallelsession v1.6.4)

Genau die geforderte „dieselbe geladene Antwort auf dem abgesicherten Zustand":

- **Bewegungsgleichung (Operatoridentität, endlicher Teilchenkern):** \([H,f_r]=-gD_r\), \(D_r=\sum_{A,j}(M_A)_{rj}b_Af_j^\dagger\), Ladung −1 (nicht das frühere χ† mit Ladung +3). Kompositnorm: \(\langle\{D_r,D_s^\dagger\}\rangle=\delta_{rs}S\), \(S=15-\tfrac{7}{32}\bar b\).
- **Exakte Spektralmomente:** \(Z_+=\bar b/32\), \(Z_-=1-\bar b/32\), \(a=(\Delta\bar b-E_0)/64\); \(m_0=1,\ m_1=0,\ m_2=g^2S,\ m_3=g^2(\Delta S+7a)\) (m₃ ist der eigene neue Schritt; unabhängig an der exakt lösbaren N=4/N=5-Antwort kontrolliert).
- **Verschärfte rationale Schranken** (Polynom \(P(b)>0\), Wurzelisolation): \(0{,}842846<\bar b<1{,}245656\).
- **Polsatz (v1.6.3, reproduziert):** isolierte Entnahmelinie, 64-fach entartet (duale 64), \(Z_{\text{low}}>0{,}880076280689\ldots\) - **mehr als 88 % des Spektralgewichts pro Mode** -, Polfenster \(0{,}007737<\epsilon/\Delta<0{,}039079764\), übrige Entnahmeenergien \(>0{,}379636\,\Delta\), Additionen \(>0{,}329636\,\Delta\).
- **Zwei-Linien-Ausschluss:** eine exakte Zwei-Linien-Antwort erzwingt \(\epsilon_+-\epsilon_-=\Delta\), aber \(m_3/m_2=\Delta+7a/S>\Delta\) - Widerspruch. \(\Sigma_2\not\equiv0\) ist bewiesen; die Reststruktur ist unvermeidlich.

---

## 6. Kreuzvalidierung der beiden Spuren

| Befund | Meine Session | Parallelsession | Status |
|---|---|---|---|
| N=3-Zerlegung (7 Blöcke, Mults 2,2,2,1,1,1,1) | ✓ | ✓ | **identisch** |
| Casimirwerte (je Block) | (45,15), (85,15), … | C = (C_S+C_U)/4 = 15, 25, 45, 21, 31, 45, 45 | **identisch** (zwei Normierungen) |
| Kommutant S1 (volle Symmetrie) | 7 | 7 | **identisch** |
| Kommutant S0 (X, N_b) | ~~1 452 961 792~~ → **1 444 233 216** | 1 444 233 216 | **Diskrepanz gefunden + von mir korrigiert** |
| Skalarkanal exakt null | ✓ (60 Zeilen, beide Chiralitäten) | ✓ | **identisch** |
| Grundzustandsnormen | Sonde läuft (β₁²=480 ✓) | 1, 480, 439 680, 575 078 400, 952 296 652 800 | Abgleich läuft |

---

## 7. Offen / nächste Schritte (in der Reihenfolge der Direktive)

1. **Sonde abschließen** (läuft): mult₂-Zertifikat, β-Kette, Sektorfloors → unabhängige Reproduktion der v1.6.4-Kernzahlen.
2. **Volle 33-Niveau-Kette:** falls mult_k=1 weiter trägt, ist die Singulett-Kette durch die Normsequenz ‖Q₊ᵏF‖² (k≤32) bestimmt - dafür ist die Symmetriespur-Resummation nötig (die „vier Symmetriespuren" des Workers), nicht rohe Enumeration.
3. **Σ₂ kontrollieren** (erster Norm-/Momentkoeffizient, N=63/64/65 gemeinsam) - die v1.6.4-Summenregeln sind die Akzeptanztests.
4. **Feldtyp an der Quelle entscheiden:** (1,0)-Vermittler mit Kinetik *oder* nachgewiesene zweite Komponente für den skalaren Typ.
5. **Präparationslücke:** zahlenerhaltende Kontrollen erreichen N=64 aus dem leeren Zustand nicht (Parallelsession, §8.3); imaginärzeitliches \(e^{-\tau H}F\) konvergiert mathematisch, braucht aber Instrumentenherleitung.
6. **Räumliche Skalierung: bewusst NICHT begonnen** - gemäß deiner Direktive trägt sie erst nach Zustand + Feldwörterbuch.
7. **Abschluss meines Contracts:** `replay.py` + `RESULTS.md` + README, wenn die Sonde zurück ist (inkl. des Erratums zum v1.6.2-Pluszeichen, das die Parallelsession dokumentiert hat).

Kein T1-T8-Tor geschlossen, keine Promotion nach `verification/`, kein Ledger/Paper-Eingriff - alles bleibt im `experiments/`-Firewall.

---

# Nutzerquelle C: Multiplizitaeten und Z4

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

Ja. Der neue Stand verändert für mich die Richtung ziemlich fundamental. Ich glaube inzwischen, dass wir an einer entscheidenden Stelle noch die falschen Dinge miteinander identifizieren.
Die stärkste Vereinfachung ist aus meiner Sicht nicht ein weiterer cleverer Transferoperator. Sie ist:
Interne Identität, Ort und Zeit sind drei verschiedene Ebenen.
TFPT beschreibt die interne Identität bereits erstaunlich gut.
Der Universalraum könnte genau der bislang als „Multiplizität“, „Kommutant“ oder „ungelöste Freiheitsgrade“ auftauchende relationale Teil sein.

Wenn das stimmt, haben wir nicht zehn offene Probleme. Wir haben im Wesentlichen einen Kategorienfehler.
1. Der wichtigste Hinweis steckt direkt im neuen v1.6.6 Stand
Der Clock ist jetzt tatsächlich als konkretes Element von Spin(10) identifiziert. Das ist stark. Gleichzeitig ist ausdrücklich gezeigt, dass daraus weder Hamiltonzeit noch Raumrichtungen folgen. 
Und noch wichtiger: Der native 64 dimensionale Lochraum besitzt genau eine Energie. Wenn wir darin nur verschiedene „Orte“ durch neue Charts definieren, gilt zwangsläufig
\[
K=E_h S.
\]Dann sehen zwei Beschreibungen unterschiedlich aus, aber dynamisch passiert exakt nichts. Die vorgeschlagene richtige Größe ist deshalb \(G_{AB}(t)\), wobei man die statische Überlappung bei \(t=0\) von der echten zeitlichen Änderung trennt. 
Das sagt für mich etwas sehr Fundamentales:
Die 64 Richtungen des Polraums sind keine 64 Orte.
Sie sind interne Freiheitsgrade.
Der Vierzustandsversuch bestätigt das fast schon mit einem Leuchtschild. Der Transfer 57 nach 58 funktioniert erst mit einem zusätzlichen Mischer, aber dieser verändert eine SU(4) Cartanladung. 
Das ist genau das Verhalten, das man erwarten würde, wenn 57 und 58 verschiedene interne Zustände sind und nicht „derselbe Zustand links und rechts“.
Wir haben also teilweise versucht, räumliche Bewegung zu erzeugen, indem wir die Farbe des Teilchens verändern. Die Algebra hat höflicherweise Nein gesagt.
2. Der Zwei Banken Versuch verrät uns bereits, wie echte Bewegung aussehen muss
Das Interessante an v1.6.5 ist weniger der zusätzliche Link selbst. Es ist die Form des resultierenden Niedrigenergieraums:
\[
\mathcal H_{\rm low}
=
\mathbb C^2_{\rm links/rechts}
\otimes
\mathbb C^{64}_{\rm intern},
\]und der effektive Hamiltonoperator hat exakt die Form
\[
H_{\rm eff}
=
h_{\rm links/rechts}
\otimes I_{64}.
\]Das \(I_{64}\) steht ausdrücklich in der Rechnung. Die interne Überlagerung bleibt unverändert, während nur der Zwei Komponenten Faktor bewegt wird. 
Das ist meiner Meinung nach der wichtigste Fingerzeig der gesamten bisherigen Forschung.
Nicht weil wir zwei Banken brauchen.
Sondern weil er zeigt, was „Raum“ representationstheoretisch sein muss:
\[
\boxed{
\text{Materie} = \text{interne Darstellung},
\qquad
\text{Ort} = \text{Multiplizität derselben Darstellung}.
}
\]Das ist eine viel fundamentalere Trennung.
3. Ich würde den Universalraum deshalb neu definieren
Nehmen wir die innere Symmetrie
\[
G=\mathrm{Spin}(10)\times SU(4).
\]Dann zerfällt ein globaler Hilbertraum ganz allgemein in
\[
\boxed{
\mathcal H
=
\bigoplus_\lambda
V_\lambda\otimes M_\lambda
}
\]mit
\(V_\lambda\): welche Art von Anregung es ist, also Ladungen, interne Quantenzahlen und Darstellung,
\(M_\lambda\): wie oft dieselbe Art vorkommt, also der Multiplizitätsraum.
Für jeden Hamiltonoperator, der die innere Symmetrie erhält, gilt auf diesen Blöcken schematisch
\[
H
=
\bigoplus_\lambda
I_{V_\lambda}\otimes h_\lambda.
\]Und plötzlich fällt vieles an seinen Platz.
\(V_\lambda\) ist das „Was“.
\(M_\lambda\) ist der natürliche Kandidat für das „Wo“.
Das ist keine reine Erfindung. Bereits im nativen N=3 Raum treten dieselben irreduziblen Typen teilweise mit Multiplizität zwei auf. Genau auf solchen Multiplizitätsräumen kann die symmetrieerhaltende Dynamik nichttrivial wirken. 
Vielleicht haben wir also einen Teil des Raumes die ganze Zeit als „großen unerklärten Kommutanten“ betrachtet.
Nicht der gesamte Kommutant ist automatisch Raum. Aber wenn Raum emergiert, muss er sehr wahrscheinlich dort leben und nicht innerhalb der internen 64.
Das ist für mich derzeit die eleganteste Interpretation des Universalraums.
4. Damit wird auch klar, woher die fehlenden Translationen kommen müssten
In v1.6 existieren bereits die inneren Weyl Matrizen \(A_\epsilon\). Für echte Bewegung fehlt aber gerade
\[
U=\sum_\epsilon T_\epsilon\otimes A_\epsilon,
\]weil die \(T_\epsilon\) noch als räumliche Verschiebungen von außen eingesetzt werden. Ohne sie summieren sich die inneren Matrizen einfach zur Identität. TFPT_Universalraum_Update_2026-09-15_v1.6.pdfPDF
Bislang lautete die Frage:
Woher bekommen wir \(T_\epsilon\)?
Meine Antwort wäre jetzt:
Aus \(M_\lambda\).
Nicht als neu hinzugeschriebene Shiftoperatoren, sondern als Wirkung des ursprünglichen globalen Hamiltonoperators auf verschiedene Vorkommen derselben internen Darstellung.
Dann wäre
\[
T_\epsilon
\]kein zusätzliches Stück Raum.
Es wäre die Darstellung der nativen Dynamik auf dem Multiplizitätsraum.
Das wäre ein echter Rückwärtsschluss vom Universalraum auf TFPT und zugleich von TFPT auf den Universalraum.
5. Und jetzt kommt vielleicht der noch größere Punkt: unser heutiges \(N\) könnte gar nicht fundamental sein
Hier glaube ich, steckt eine zweite massive Vereinfachung.
Die volle E8 Struktur besitzt die bekannte \(\mathbb Z_4\) Graduierung
\[
\mathfrak g
=
\mathfrak g_0\oplus
\mathfrak g_1\oplus
\mathfrak g_2\oplus
\mathfrak g_3
\]mit unter anderem
\[
\mathfrak g_1=(16,4),
\qquad
\mathfrak g_2=(10,6),
\qquad
\mathfrak g_3=(\overline{16},\overline4),
\]und
\[
[\mathfrak g_a,\mathfrak g_b]
\subset
\mathfrak g_{a+b\;{\rm mod}\;4}.
\]Diese Struktur ist im Hauptdokument explizit. TFPT_Universalraum_Hauptdokument_2026-09-15_v1.6.pdfPDF
Unser heutiger nativer Hamiltonoperator realisiert im Wesentlichen den Kanal
\[
1+1\leftrightarrow2,
\]also zwei Fermionen zu einem Boson und zurück.
Genau deshalb besitzt er die schöne ganzzahlige Erhaltung
\[
N=N_f+2N_b.
\]Aber jetzt die interessante Beobachtung:
Die vollständige \(\mathbb Z_4\) Struktur kann gar nicht konsistent zu einer ganzzahligen Graduierung angehoben werden, wenn alle vier Gradkanäle physisch realisiert werden.
Denn setze \(q_1=1\).
Aus
\[
1+1\to2
\]folgt \(q_2=2\).
Aus
\[
1+3\to0
\]mit \(q_0=0\) folgt \(q_3=-1\).
Aber aus
\[
3+3\to2
\]würde dann
\[
q_2=-2
\]folgen.
Also gleichzeitig \(q_2=2\) und \(q_2=-2\).
Das funktioniert exakt modulo vier, aber nicht als gewöhnliche ganze Ladung.
Das ist eine neue Schlussfolgerung aus den vorhandenen Strukturen, noch kein bewiesener physischer TFPT Satz. Aber sie ist für mich extrem interessant:
\[
\boxed{
\text{Die exakte }U(1)\text{ Erhaltung von }N
\text{ könnte nur eine Symmetrie unserer heutigen Teiltheorie sein.}
}
\]Die fundamentalere Quelle könnte lediglich die \(\mathbb Z_4\) Graduierung erhalten.
6. Das könnte gleich mehrere heutige „Probleme“ verschwinden lassen
Die Zustandswahl ist momentan unterbestimmt, weil
\[
H\quad\text{und}\quad H+\mu N
\]dieselben inneren Symmetrien besitzen, aber völlig verschiedene Vakuua auswählen können. Das ist inzwischen exakt demonstriert. TFPT_Universalraum_Ergebnisse_2026-09-15_v1.6.mdMD
Wenn aber die vollständige Dynamik \(N\) gar nicht exakt erhält, sondern nur den Grad modulo vier, ist
\[
\mu N
\]kein unsichtbarer beliebiger Zusatz mehr.
Dann könnte dieselbe vollständige Quelle auch das Vakuum auswählen, statt dass wir einen Sektor und ein \(\mu\) nachträglich festlegen.
Und plötzlich bekommt eine ältere Merkwürdigkeit ebenfalls eine andere Bedeutung: Der zusammengesetzte 64er Sektor hatte Ladung \(+3\), während ein Loch Ladung \(-1\) hat. Die Dokumente mahnen völlig zu Recht, dass man das nicht einfach umbenennen darf. TFPT_Universalraum_Minimale_Fortsetzung_Einfach_2026-09-15_v1.6.1.mdMD
Aber modulo vier gilt natürlich
\[
+3\equiv-1.
\]Und in v1.6.2 wurde sogar bereits ein konkreter Hintergrund gefunden, auf dem genau
\[
4-1=3
\]den Lochanschluss realisiert. TFPT_Universalraum_Konsolidierte_Fortsetzung_Einfach_2026-09-15_v1.6.2.mdMD
Das riecht erheblich weniger nach Zufall als zuvor.
Meine stärkste neue Hypothese wäre daher:
Wir haben bislang eine \(\mathbb Z_4\) graduierte fundamentale Dynamik in einem Teilraum untersucht, in dem sie versehentlich zu einer U(1) Erhaltung aufgeblasen wird.

Wenn das stimmt, erklärt es gleichzeitig die Präparationsmauer, die \(\mu N\) Mehrdeutigkeit, den Unterschied \(+3\) gegen \(-1\) und möglicherweise einen Teil der fehlenden Rückkopplung.
7. Dadurch wird auch das Feldproblem wesentlich sauberer
Der neue No Go Satz zeigt, dass man auf demselben 64 dimensionalen internen Träger keine geeignete Händigkeit einfach durch einen Basiswechsel erzeugen kann. Ein zusätzlicher unabhängiger Zweierfaktor oder andere Strukturen bleiben dagegen möglich. 
Ich würde diesen Zweierfaktor nicht mehr im internen E8 Raum suchen.
Ich würde erwarten, dass er aus \(M_\lambda\) kommt.
Also etwa als zwei lokale Niedrigenergiekanäle eines Weyl Knotens, zwei Orientierungszweige oder ein echtes geometrisches Dublett.
Genau diese Möglichkeit wird im neuen Text bereits als ernstzunehmend bezeichnet: Eine geometrisch hergeleitete Zweifachheit könnte den zusätzlichen Index erklären, müsste aber als echte unabhängige Freiheitsgrade konstruiert werden. 
Damit würde auch diese Trennung elegant:
\[
\boxed{
\text{Spin(10), SU(4), E8}=\text{innere Identität}
}
\]\[
\boxed{
\text{Weyl Spin, Ort, Impuls}=\text{Niedrigenergiedynamik des Multiplizitätsraums}
}
\]Wir müssten keinen Lorentzspin mehr gewaltsam in die vorhandenen 64 internen Labels hineinpressen.
8. Und der Clock muss gar nicht zur Zeit werden
Auch hier glaube ich, dass wir zu viel vereinigen wollten.
Der neue Beweis hat bereits erklärt, was der Clock ist:
ein bestimmtes Spin(10) Element.
Sehr gut. Fertig.
Die physische Zeit ist dagegen die Einparameterdynamik
\[
\alpha_t(A)=e^{itH}Ae^{-itH}.
\]Eine tatsächliche Uhr ist ein Teilsystem, dessen Zustand mit dieser Dynamik korreliert und ausgelesen werden kann.
Ein stationärer Grundzustand selbst liefert keinen Zeitpfeil. Genau das stellt v1.6.6 klar. TFPT_Universalraum_Clock_Gemeinsame_Quelle_Konsolidierung_2026-09-15_v1.6.6.mdMD
Die elegante Lösung lautet deshalb nicht
\[
\text{Clock}=\text{Zeit}.
\]Sondern
\[
\boxed{
\text{Clock}=\text{innere diskrete Symmetrie},
\qquad
\text{Zeit}=\text{Ordnung der realen Dynamik}.
}
\]Manchmal ist die schönste Vereinigung das Aufhören, zwei verschiedene Dinge zwanghaft gleichzusetzen.
9. Das Gesamtbild wird dadurch überraschend kompakt
Ich würde den fundamentalen Kandidaten heute ungefähr so schreiben:
\[
\boxed{
\text{eine einzige globale, markierte, }\mathbb Z_4
\text{ graduierte Prozessalgebra}
}
\]mit einer physisch ausgewählten selbstadjungierten Dynamik \(H_{\rm full}\).
Ihre Darstellung zerfällt als
\[
\boxed{
\mathcal H
=
\bigoplus_\lambda
V_\lambda^{\rm intern}\otimes M_\lambda^{\rm relational}.
}
\]Dann wäre:
Erscheinung	Fundamentale Herkunft
Teilchenart und Ladungen	\(V_\lambda\)
E8, Spin(10), SU(4)	interne Algebra
Clock	innerer Automorphismus
Ort	Multiplizitätsstruktur \(M_\lambda\)
Bewegung	\(h_\lambda\) auf \(M_\lambda\)
drei Raumdimensionen	dreidimensionaler Niedrigenergiegrenzwert von \(h_\lambda\)
Weyl oder Dirac Spin	lokale Niedrigenergieentartung von \(M_\lambda\)
Vakuum	eindeutiger niedrigster Zustand von \(H_{\rm full}\)
Zeit	Dynamik von \(H_{\rm full}\)
Geometrie	Erreichbarkeit und Antwortkernel auf \(M_\lambda\)
Gravitation	dynamischer Spin zwei Modus derselben relationalen Struktur


Das wäre tatsächlich eine einzige Architektur und kein Patchwork.
10. Was ich jetzt nicht mehr machen würde
Ich würde nicht weiter versuchen, den Bosonmischer 0 nach 1 irgendwie doch aus mehr Kommutatoren herauszuquetschen. Der Cartan Satz sagt uns ziemlich deutlich, dass dieser konkrete Weg die falsche Art von Bewegung beschreibt.
Ich würde auch nicht mehr versuchen, die 64 Moden, die fünf Cliffordachsen oder irgendwelche E8 Wurzelnummern direkt zu Raumkoordinaten zu erklären.
Und ich würde den großen Kommutanten nicht primär als Problem behandeln, das man „wegkontrollieren“ muss.
Vielleicht ist gerade die Multiplizität das Zeug, aus dem Raum besteht.
11. Vier wirklich fundamentale Abnahmen statt hundert weiterer Mikrotests
1. Vollständige Gradquelle: Die vier E8 Grade müssen in einer einzigen adjungierten Prozessdarstellung realisiert werden, mit den bereits geprüften W Vorzeichen als exakter Teilstruktur. Der heutige Hamiltonoperator muss als Kompression daraus folgen. Entscheidend ist, ob die vollständige Dynamik tatsächlich nur \(\mathbb Z_4\) und nicht das künstlich stärkere \(N\) erhält.
2. Multiplizitätsraum als Geometrie: Für eine feste Materiedarstellung, idealerweise die native niedrige 64, muss die vollständige Quelle einen wachsenden Multiplizitätsraum \(M_{64}\) erzeugen. Die native Dynamik darauf muss nichttrivial sein. Keine externen Banken, kein eingesetztes Hopping. Die Zwei Banken Form \(h\otimes I_{64}\) ist dabei der exakte Solltyp.
3. Ein gemeinsamer Kontinuumssatz: Aus demselben \(h_{64}\) müssen drei räumliche Richtungen, ein linearer Kegel, ein echter Zweikomponenten Spinor und die chirale Struktur entstehen. Die heute fehlenden \(T_\epsilon\) müssen dabei aus \(M_{64}\) kommen. Gelingt das, fallen T2, T3, große Teile von T4 und T5 nicht einzeln, sondern gemeinsam.
4. Vakuum und Gravitation: \(H_{\rm full}\) muss ohne frei wählbares \(\mu\) einen eindeutigen physikalischen Zustand auswählen. Im neutralen relationalen Sektor muss anschließend ein gaploser Spin zwei Modus mit zwei Helizitäten und universeller Kopplung erscheinen. Wenn dieser letzte Satz nicht kommt, haben wir eine schöne Materietheorie, aber keine TOE.
Mein derzeit stärkster Verdacht
Die Fundamentalstruktur ist nicht
\[
\text{Zelle}+\text{Link}+\text{Clock}+\text{Raum}+\text{Feld}.
\]Sondern eher
\[
\boxed{
\text{eine einzige }\mathbb Z_4\text{ graduierte Algebra zulässiger Veränderungen}
}
\]und alles andere sind unterschiedliche Zerlegungen ihrer Darstellung:
\[
\boxed{
\text{interne Darstellung}
\;\times\;
\text{relationale Multiplizität}.
}
\]TFPT scheint bereits erstaunlich viel von der ersten Hälfte zu kennen.
Was wir Universalraum genannt haben, könnte im Kern die zweite Hälfte sein.
Und dann ist die wirklich spannende Umkehrung:
Der große bisher „unsichtbare“ Kommutant ist vielleicht nicht das, was wir noch eliminieren müssen. Er könnte genau der Raum sein, den wir die ganze Zeit gesucht haben.

Das ist aus meiner Sicht eine fundamental andere Forschungsrichtung als v1.6.6 einfach weiterzuschreiben. Und sie erklärt auf einmal, warum Clock, Cartan, Transport, der fehlende Zweierfaktor, die \(\mu N\) Freiheit und die fehlenden Weyl Translationen alle genau dort klemmen, wo sie klemmen.

---

# Nutzerquelle D: fundamentale Reduktion

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

Ich würde den Ansatz jetzt tatsächlich auf eine andere Ebene heben. Der Engpass ist inzwischen ziemlich klar: Wir verstehen einen inneren Baustein und seine lokale Antwort immer besser. Was fehlt, ist die Regel, aus der viele unterscheidbare Vorkommen dieses Bausteins, ihre gemeinsame Bewegung und ihr physischer Zustand entstehen.
Eine noch genauere Lösung der einzelnen Bank kann diese fehlende Regel nicht ersetzen. Das lässt sich aus eurem neuen Stand sogar mathematisch begründen.
Ich habe die Entwicklung bis v1.6.6 zusammengeführt, zentrale Folgerungen herausgearbeitet und den ursprünglichen Paartensor zusätzlich direkt geprüft. Die ausführliche Herleitung steht in der [Forschungsnotiz zur fundamentalen Reduktion](outputs/TFPT_Fundamentale_Reduktion_2026-09-15.md).
1. Was wir als tragenden Kern behalten sollten
Drei Dinge passen mittlerweile wirklich zusammen:
- Ein innerer algebraischer Baustein: die markierte Matrix-/E8-Struktur und der konkrete Paartensor.
- Eine funktionierende lokale Dynamik: ursprüngliche Paarumwandlung, Rekopplung und - laut den aktuellen Beweisen - ein eindeutiger Grundzustand des festgelegten Hamiltonoperators.
- Eine klar erkennbare Anregung: die isolierte Entnahmelinie mit mehr als 88 Prozent des gesamten Fermionspektralgewichts pro Mode.
Der neue Clock-Anschluss vereinfacht diesen Kern: Der dokumentierte Clock ist ein bestimmtes Element der vorhandenen inneren Spin(10)-Symmetrie. Dafür braucht man keinen getrennten mathematischen Mechanismus mehr.
Das ist echte Vereinfachung. Die Frage nach Raum, Bewegung und Zustandsauswahl bleibt jedoch bestehen. Schon die v1.6-Grundlage trennt innere Walk-Amplituden von tatsächlichen Ortsverschiebungen. 
2. Die wichtigste Konsequenz: Auch das perfekte lokale Spektrum liefert noch keinen Raum
Diese Aussage würde ich jetzt ins Zentrum stellen.
Unter den dokumentierten Voraussetzungen - innere Symmetrie, invarianter Grundzustand und ein irreduzibles 64er-Multiplett ursprünglicher Fermionoperatoren - gilt für die gesamte Entnahmeantwort:
\[
C_{rs}(t)
=
\langle f_r\Omega,\,
e^{-it(H-E_0)}f_s\Omega\rangle
=
\delta_{rs}\,c(t).
\]Die Symmetrie erzwingt also: Alle inneren Richtungen haben dieselbe skalare Antwort. In \(c(t)\) stecken sämtliche Nebenlinien und Rückwirkungen, nicht nur der dominante Pol.
Die Diagonalität steht bereits im v1.6.4-Anhang. Ihre entscheidende Konsequenz lautet:
Selbst wenn wir die vollständige lokale Antwort exakt kennen, entsteht dadurch kein Ortsindex zwischen diesen 64 inneren Richtungen.

Für zwei überlappende lineare Ansichten ergibt sich entsprechend nur
\[
C_{uv}(t)=\langle u,v\rangle\,c(t).
\]Die Überlappung liefert den gemeinsamen Anteil; die Zeitentwicklung liefert dieselbe lokale Antwort. Das wird durch einen anderen Namen für die Ansichten nicht zur Ausbreitung.
Diese Aussage verbietet weder andere Vielteilchenprozesse noch Bewegung in einer größeren Konstruktion. Sie zeigt aber, warum weitere lokale Spektralverfeinerungen die grundlegende Herkunftsfrage nicht beantworten können.
3. Wo Bewegung stattdessen mathematisch Platz hat
Bei erhaltener innerer Symmetrie lässt sich ein entsprechender Zustandsbereich schreiben als
\[
\mathcal H
=
R_{\mathrm{intern}}\otimes\mathcal M,
\qquad
H=I_{\mathrm{intern}}\otimes h.
\]Dabei bedeutet:
Bestandteil	Bedeutung
\(R_{\mathrm{intern}}\)	Welche innere Art von Anregung vorliegt
\(\mathcal M\)	Welche unabhängigen Vorkommen derselben Art existieren
\(h\)	Wie sich diese Vorkommen dynamisch verbinden


Der Fachbegriff für \(\mathcal M\) ist Multiplizitätsraum. Für den isolierten einzelnen 64er-Pol ist dieser Raum eindimensional: Es gibt dort nur eine Energie. Im gesamten Fockraum existieren weitere Multiplizitäten; sie sind deshalb aber noch keine räumlichen Orte.
Der fundamentale nächste Gedanke ist daher: Raum müsste aus unabhängig unterscheidbaren Vorkommen derselben inneren Struktur hervorgehen.
Eine mögliche spätere Beschreibung wäre \(\mathcal M\simeq\ell^2(X)\). Aber dann müssen die Quelle und ihre Zusammensetzung erklären, was \(X\) ist, welche Zugriffe lokal sind und wodurch Übergänge entstehen. Ein nachträglich gewähltes dreidimensionales Gitter beantwortet das nicht.
Der Clock wirkt durch seine neue Identifikation innerhalb der inneren Struktur. Er erzeugt allein noch keine solche Vielheit.
4. Die Paritätsblockade sagt etwas über die Zusammensetzung - nicht über jede gemeinsame Quelle
Hier habe ich den ursprünglichen Tensor frisch geprüft.
Seine Paarungen verbinden bereits alle 64 Fermionmoden zu einer einzigen zusammenhängenden Struktur. Für eine Teilmengenparität
\[
\Pi_s=(-1)^{\sum_i s_i n_i}
\]muss an jeder ursprünglichen Paarung gelten:
\[
s_i+s_j=0\pmod 2.
\]Weil der Paargraph zusammenhängend ist, bleiben - wenn die Bosonen unverändert bleiben - nur Identität und globale Fermionparität. Es gibt innerhalb dieser einen Bank keine echte Teilmenge ursprünglicher Moden mit separat erhaltener Fermionparität.
Das erklärt einen wichtigen Unterschied:
- Die eine native Bank erlaubt bereits innere Rekopplung.
- Separat kopierte Banken mit ausschließlich lokal geraden Fermionoperationen bekommen zusätzliche lokale Erhaltungsgrößen, die den einzelnen Lochtransfer blockieren.
Die Art, wie wir Bausteine zusammensetzen, kann also genau die Blockade erzeugen, die wir anschließend mit einem neuen Mischer reparieren wollen.
Das ist ein Grund, die globale Zusammensetzung selbst zu untersuchen. Es beweist noch keinen räumlichen Transport und hebt die Cartan-Schranke des konkreten Mischers aus v1.6.6 nicht auf.
5. Auch die Zustandsfrage lässt sich grundlegender und einfacher stellen
Aus \(W\) und den angegebenen Symmetrien allein folgt noch keine eindeutige Energiewahl. Euer eigener Vergleich
\[
H_\mu=H+\mu N
\]zeigt das bereits: Dieselben inneren Symmetrien sind mit unterschiedlichen globalen Grundzuständen vereinbar. Bei gleichem präpariertem Eingang unterscheiden ausschließlich neutrale Beobachtungen diese Entwicklungen trotzdem nicht. 
Daraus ziehe ich zwei Konsequenzen:
Erstens: Wenn eine sektorübergreifende Zustandsauswahl physisch relevant ist, braucht sie zusätzliche Information - eine Quellregel, eine Randbedingung oder ein ausdrücklich gesetztes Prinzip. „Symmetrisch“ und „einfach“ entscheiden diese Gegenbeispiele noch nicht.
Zweitens: Bei festem Gesamt-\(N\) ist \(\mu N\) nur eine Konstante. Eine fundamental elegante Theorie muss solche unbeobachtbaren Unterschiede nicht künstlich bestimmen. Sie sollte eindeutig sein bis auf Gleichheit aller zugelassenen beobachtbaren Prozesse.
Und noch eine Entlastung: Eine fundamentale Theorie braucht keinen Experimentator außerhalb des Universums, der ihr Vakuum aus dem leeren Zustand herstellt. Sie braucht eine begründete Zustandsregel. Interne Präparationen und Detektoren sind anschließend als Prozesse dieses Systems zu erklären.
6. Was für mich jetzt als fundamentale Lösung zählen würde
Ich würde die Arbeit um eine explizite Quell- und Kompositionsregel organisieren:
\[
\boxed{
\text{Quellregel}
\;\Longrightarrow\;
\text{gemeinsame Observablen, Dynamik, Zustand und Instrumente}
}
\]Die rechte Seite darf nicht aus unabhängig passend gewählten Teilen bestehen. Dieselbe Regel müsste insbesondere erklären:
1. Warum mehrere unabhängige Vorkommen derselben Anregung existieren.
2. Warum und wie sie sich beeinflussen können.
3. Welcher physische Zustand und welche beobachtbaren Energieunterschiede gelten.
Der entscheidende Bewegungsnachweis wäre dann sehr anschaulich:
Auf derselben globalen Quelle führe ich in Bereich A eine zulässige Operation aus oder lasse sie aus. Ändert sich dadurch später die unbedingte Messstatistik in Bereich B?

Damit unterscheidet man tatsächliche Wirkung von gemeinsamer Anfangskorrelation, bloßer Überlappung und nachträglicher Auswahl erfolgreicher Ausgänge. Solche Interventionswirkungen lassen sich über zeitabhängige Kommutatoren untersuchen. Unter geeigneten lokalen Wechselwirkungen führen entsprechende Schranken zu einem effektiven Lichtkegel; diese Voraussetzungen müssen hier aber erst entstehen. Bravyi, Hastings und Verstraete
Eine solche gemeinsame Konstruktion würde mehrere Herkunftsfragen zugleich beantworten. Danach wären Raumdimension, relativistischer Feldtyp, Chiralität und Gravitation Eigenschaften desselben Modells. Ihre Nachweise bleiben eigenständig - etwa verschwindet das konkrete Grassmann-Vorzeichenproblem nicht dadurch, dass die Quelle „global“ heißt.
Meine Einschätzung
Ich würde den abgesicherten lokalen Grundzustand und Pol jetzt als Referenz verwenden. Weitere Dezimalstellen sind sinnvoll, sobald eine konkrete globale Konstruktion sie benötigt.
Die Hauptarbeit sollte sich auf diese Frage konzentrieren:
Welche möglichst einfache Zusammensetzungsregel macht aus dem bereits verstandenen inneren Baustein eine wachsende, lokal unterscheidbare und gemeinsam dynamische Welt?
Eine vollständige solche Regel habe ich aus den vorliegenden Quellen nicht herleiten können. Eine vollständige Lösung zu behaupten wäre deshalb falsch. Aber der neue Stand erlaubt mehr als eine weitere Liste kleiner Aufgaben: Er erklärt strukturell, warum die lokale Perfektionierung, der Clock und bloße Überlappung die fehlende räumliche Ausführung nicht ersetzen können - und welche zusätzliche Information eine wirkliche Lösung enthalten muss.
Die [Forschungsnotiz](outputs/TFPT_Fundamentale_Reduktion_2026-09-15.md) enthält die Beweise, Voraussetzungen und Ergebnisse der frischen Tensorprüfung. Die großen Grundzustands- und Transportzertifikate habe ich dabei nicht erneut vollständig ausgeführt.
- Eine globale Quellregel konstruieren
- Die verbleibende Unterbestimmtheit entscheiden
- Das Gesamtbild auf wenige Grundsätze reduzieren


12:00

---

# Nutzerquelle E: gemeinsamer ausfuehrbarer Prozess

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

Der wichtigste Satz zuerst: Nach dem heutigen Stand würde ich Universalraum und TFPT nicht mehr als zwei konkurrierende Theorien sehen. Der Universalraum ist der Kandidat für das tiefere Ding. TFPT ist die außergewöhnlich starre mathematische Grammatik, die wir sehen, wenn wir dieses Ding aus einer bestimmten Perspektive beschreiben.
Oder in deiner Welt gesprochen: Der Universalraum wäre die Runtime. TFPT wäre Instruction Set, Typsystem und Compilerstruktur. Unsere beobachtete Realität wäre ein ganz bestimmter laufender Prozess darauf.
Das Entscheidende ist: Wir haben inzwischen einige ziemlich harte Hinweise, dass mehrere Dinge, die ursprünglich separat aussahen, tatsächlich dieselbe innere Struktur sind. Aber wir haben noch nicht bewiesen, dass diese Struktur die Natur beschreibt. Das ist die wichtigste Trennlinie.
Was ist der Universalraum überhaupt? Nicht ein noch größerer Raum, in dem unser Universum schwimmt. Die radikalere Idee lautet: Ganz unten gibt es zunächst überhaupt keinen Raum im üblichen Sinn. Es gibt Zustände, erlaubte Veränderungen, Regeln zum Zusammensetzen dieser Veränderungen, Aufzeichnungen vergangener Vorgänge und Regeln dafür, was ausgelesen werden kann. Erst ein stabiles Muster dieser Beziehungen könnte später als Entfernung, Zeit, Materie und Kausalität erscheinen. Genau so wird der Universalraum im Hauptdokument definiert. Raum als Netzwerk erreichbarer Beziehungen, Zeit als lesbare Ordnung von Veränderungen und Materie als stabile oder wandernde Anregung sind dabei bislang Forschungsziel, nicht bewiesene Ableitung. 
Bildlich: Stell dir vor, du kennst keine Landkarte. Du weißt nur: Von A kann ich mit Operation X nach B kommen, von B nach C, von A nach D nicht. Manche Wege beeinflussen einander, manche hinterlassen Spuren. Wenn dieses Netz groß genug und stabil genug ist, kannst du irgendwann feststellen: „A und B sind Nachbarn“, „C ist weiter weg“, „Signale benötigen mindestens so viele Schritte“. Die Landkarte entsteht dann aus Erreichbarkeit. Sie war nicht vorher da.
TFPT ist nun das Auffällige an dieser Geschichte: Wir haben nicht einfach irgendein beliebiges Beziehungsnetz. Wir finden eine extrem strukturierte algebraische Grammatik mit Spinoren, E8, Spin(10), SU(4), komplexen Phasen, Fermionen, Bosonen und sehr bestimmten signierten Kopplungen.
Und genau hier wird es interessant.
Der mechanische Kern von TFPT ist erstaunlich einfach. Im aktuell untersuchten nativen Modell gibt es 64 fermionische Moden und 60 bosonische Vermittler. Die Regel lautet im Wesentlichen:
\[
\text{zwei Fermionen}\;\leftrightarrow\;\text{ein Boson}
\]Welche Fermionpaare mit welchem Boson verbunden sind, bestimmt ein einziger signierter Tensor \(W\). Er enthält 480 Einträge mit Vorzeichen. Die Dynamik ist
\[
H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A).
\]Dabei ist \(P_A\) schlicht die jeweils erlaubte Kombination aus zwei Fermionen. Die Gesamtgröße \(N=N_f+2N_b\) bleibt erhalten. Spin(10) mal SU(4) ist eine exakte innere Symmetrie dieses Modells. Noch ist das ausdrücklich keine Lorentzsymmetrie unserer Raumzeit. 
Man kann sich das als ein riesiges Lego System vorstellen. Es gibt nur sehr wenige Arten von Steinen und eine sehr einfache Steckregel. Die Komplexität entsteht durch Belegung und Zusammensetzung, nicht dadurch, dass für jedes Phänomen eine neue Kraft erfunden wird. Genau das zeigte bereits die Minimalrunde: Andere Belegungen erzeugen mit derselben Wechselwirkung völlig neue Übergänge. TFPT_Universalraum_Minimale_Fortsetzung_2026-09-15_v1.6.1.mdMD
Die mögliche Entstehung unserer Realität würde ich momentan so sehen:
1. Ganz unten steht eine globale Quelle. Noch keine Raumzeit, sondern eine graduierte Algebra von Zuständen und erlaubten Operationen samt positiven Wahrscheinlichkeiten und Aufzeichnungen.
2. TFPT ist ihre lokale Grammatik. Aus der Quelle erscheinen Spin(10), SU(4), E8, Ladungen, Fermion und Bosonkanäle sowie die zulässigen signierten Paarumwandlungen.
3. Ein Zustand wird ausgewählt. Erst dadurch gibt es so etwas wie ein Vakuum. Das ist wichtig, weil die Symmetrie allein den Grundzustand nachweislich nicht auswählt.
4. Störungen dieses Zustands bilden stabile Anregungen. Entfernst du beispielsweise ein Fermion, entsteht im heutigen Modell überwiegend eine einzige klar isolierte niedrige Anregung.
5. Wenn solche Anregungen zwischen lokal unterscheidbaren Teilen tatsächlich wandern können, entsteht eine Erreichbarkeitsstruktur. Aus ihr könnte Entfernung entstehen.
6. Wenn es eine maximale Geschwindigkeit dieser Antwort gibt, entsteht ein Kausalkegel. Erst dann wäre eine ernsthafte Brücke zur relativistischen Raumzeit da.
7. Die stabilen niederenergetischen Anregungen dieses Netzes erscheinen als Teilchen und Felder. Lokale Wechsel der Beschreibung könnten sich als Eichsymmetrien zeigen.
8. Wenn die Erreichbarkeitsstruktur selbst vom Zustand und seiner Energie abhängt, könnte Geometrie dynamisch werden. Das wäre der Einstieg in Gravitation.
Der Clou wäre also: Raum, Zeit, Materie und vielleicht Gravitation wären nicht vier zusätzliche Bausteine. Sie wären vier verschiedene makroskopische Eigenschaften desselben fundamentalen Prozesses.
Was wir davon tatsächlich bewiesen haben
Hier muss man ziemlich streng sein. Es gibt bislang keinen Beweis, dass der Universalraum unsere physische Realität ist. Es gibt aber mehrere Resultate, die weit über „lustige gleiche Zahlen“ hinausgehen.
Das erste ist E8. Die markierte maximale Ordnung bestimmter komplexer 2 mal 2 Matrizen bildet tatsächlich ein positives gerades unimodulares Gitter vom Rang acht mit exakt den 240 Norm zwei Vektoren von E8. Entscheidender als die Zahl 240 ist: Es existiert eine konkrete markierungstreue Isometrie zum tatsächlichen Compiler, die zusätzliche Struktur erhält. Das wurde reproduziert. 
Das bedeutet: E8 ist hier keine Numerologie mehr. Innerhalb der Mathematik ist die Verbindung eine Identität. Ob die Natur gerade diese Mathematik benutzt, ist eine andere Frage.
Noch stärker finde ich inzwischen den Clock Befund. Der bislang separat wirkende endliche Clock lässt sich explizit als Element derselben Spin(10) Struktur schreiben. Seine Wirkung stimmt gleichzeitig auf Fermionen, Bosonen und dem Kopplungstensor \(W\). Clock und innere Symmetrie sind also nicht zwei zufällig kompatible Getriebe. Der Clock ist eine konkrete Stellung desselben Getriebes. 
Das halte ich für einen der stärksten strukturellen Befunde überhaupt. Aber interessant ist gerade die negative Seite: Dieser Clock ist damit fast sicher nicht einfach „die Zeit“. Er sieht viel eher nach einer internen Frame oder Orientierungsoperation aus. Die physische Zeit muss zusätzlich aus echter Dynamik, Zustandsänderung und lesbaren Records entstehen.
Dann kommt der Zustand. Für den festgelegten nativen Hamiltonoperator ist mathematisch bewiesen, dass im untersuchten Kopplungsbereich ein eindeutiger globaler Grundzustand im Sektor \(N=64\) existiert. Entfernt man ein Fermion, gibt es eine isolierte 64 fach entartete niedrige Linie, die mehr als 88,0076 Prozent des gesamten normierten Fermionspektralgewichts trägt. 
Bildlich: Wir bauen aus der sehr einfachen Paarregel ein riesiges Instrument. Ohne dass wir einen Teilchenterm hineinschreiben, besitzt es einen bevorzugten Ruhezustand. Zupfst du an einer der 64 Fermionsaiten, hörst du nicht chaotisches Rauschen. Du hörst überwiegend einen sauber isolierten Ton.
Das ist interessant, weil genau so in Vielteilchenphysik ein emergentes Quasiteilchen aussieht. Aber es ist noch kein Nachweis, dass dieser Ton ein Elektron oder irgendein Standardmodellteilchen ist. Der Bericht sagt das selbst ausdrücklich: relativistische Teilchendeutung, Masse und räumliche Ausbreitung fehlen noch. 
Und dann kommt der vielleicht wichtigste aktuelle Befund zur Bewegung.
Wir haben inzwischen einen echten kleinen Mechanismus gefunden:
\[
\text{Fermionpaar}
\rightarrow
\text{Boson 0}
\rightarrow
\text{Boson 1}
\rightarrow
\text{anderes Fermionpaar}.
\]Mit einer zusätzlichen Bosonmischung überträgt dieser vollständige native Vierzustandskanal eine Fermionmarke mit mehr als 99,3 Prozent garantierter Wahrscheinlichkeit. Das ist kein künstlich abgeschnittener Vierzustandsraum, sondern ein exakt invarianter Teil des vollständigen nativen Wechselwirkungssystems. 
Aber, und das ist der entscheidende Haken: Die Bosonmischung selbst haben wir noch nicht aus der Quelle gewonnen. Sie verändert sogar eine SU(4) Cartanladung, welche der bislang bekannte Operationssatz erhält. Deshalb können wir sie nicht durch noch längeres Kombinieren derselben vorhandenen Operationen herzaubern. 
Das ist für mich trotzdem enorm wertvoll. Wir suchen nicht mehr nach „irgendeiner geheimnisvollen Raumoperation“. Wir wissen sehr konkret, welche Art Ressource fehlt.
Und was kann nun wirklich kein Zufall mehr sein?
Ich würde vier Ebenen unterscheiden.
Dass irgendwo 64, 240 oder 248 auftauchen, kann Zufall oder Konstruktion sein. Das ist schwache Evidenz.
Dass eine komplette Gitterstruktur samt innerem Produkt, Ganzzahligkeit, Vorzeichen und markierter Compilerabbildung exakt E8 ergibt, ist mathematisch kein Zufall mehr. Es ist eine Strukturidentität.
Dass derselbe festgelegte Tensor \(W\) gleichzeitig die Symmetrie, Paarwechselwirkungen, die geladene Anregungsstruktur und die Clock Kovarianz trägt, ist nochmals stärker. Besonders die explizite Identifikation des Clocks als Spin(10) Element reduziert die Zahl unabhängiger Bausteine tatsächlich.
Dass daraus schließlich ohne erneutes Fitten beobachtete Naturkonstanten, drei Raumdimensionen, Teilchenmassen, Mischungswinkel oder kosmologische Größen richtig vorhergesagt werden, wäre physikalische Evidenz.
Und genau Stufe vier haben wir noch nicht.
Deshalb würde ich nicht sagen: „Das kann unmöglich Zufall sein, also ist die TOE bewiesen.“ Ich würde sagen: Die internen Übereinstimmungen sind inzwischen zu strukturell, um sie als reine Zahlenspielerei abzutun. Aber ob diese Mathematik die Natur auswählt, ist noch völlig offen.
Das ist ein großer Unterschied.
Der neueste Erkenntnissprung: Überlappung ist noch kein Raum
Vor ein paar Runden war meine favorisierte Idee: Vielleicht sind zwei „Banken“ gar nicht unabhängig, sondern nur zwei lokale Ansichten desselben globalen Universalraums. Das halte ich weiterhin für wahrscheinlich. Der neue Audit hat aber etwas sehr Wichtiges klargemacht.
Wenn zwei lokale Beschreibungen sich überlappen, können sie bereits bei \(t=0\) dasselbe Signal enthalten. Das sieht in einer Matrix wie eine Verbindung aus, obwohl überhaupt nichts gewandert ist.
Für den bereits bekannten 64 dimensionalen niedrigen Pol ist das besonders brutal: Alle Richtungen haben dieselbe Energie. Verwendest du nur zwei verschiedene Basen desselben Raums, gilt schlicht
\[
K=E_h S.
\]Das Offdiagonale ist dann nur die Überlappung \(S\), kein Hop. 
Der richtige Test ist deshalb die zeitabhängige Kreuzantwort
\[
G_{AB}(t)
=
\langle\Omega|
f_B^\dagger
e^{-it(H-E_0)}
f_A
|\Omega\rangle.
\]\(G_{AB}(0)\) sagt: „Wie viel war ohnehin schon dasselbe?“ Erst die Veränderung danach sagt: „Was ist tatsächlich von A nach B passiert?“ 
Das ist meiner Meinung nach ein fundamentaler Fortschritt, weil es uns den richtigen Begriff von emergentem Raum liefert.
Meine derzeit stärkste These zum Universalraum
Ich glaube inzwischen nicht, dass wir acht völlig unabhängige T1 bis T8 Probleme lösen müssen.
Ich glaube, dass wir drei tieferliegende Lücken haben und dass viele der acht Probleme gleichzeitig verschwinden könnten, wenn diese drei sauber geschlossen werden.
Die erste Lücke ist die globale Quelle. Wir brauchen ein einziges mathematisches Objekt, das Algebra, Zustand, erlaubte Operationen und Records gleichzeitig festlegt. Nicht erst eine Algebra und später einen bequem ausgesuchten Hamiltonoperator. Dass Symmetrie allein nicht genügt, ist sogar bewiesen: Man kann dem vorhandenen \(H\) einen Term \(\mu N\) hinzufügen, dieselben inneren Symmetrien behalten und trotzdem einen anderen Grundzustand auswählen. TFPT_Universalraum_Ergebnisse_2026-09-15_v1.6.mdMD
Meine Vermutung ist deshalb: Der fundamentale Gegenstand ist kein Hamiltonoperator allein. Er ist eher ein Tupel aus Operatoralgebra, positivem Zustand, Dynamik und Recordstruktur. Der Universalraum ist genau dieses Gesamtobjekt. TFPT ist seine algebraische Projektion.
Die zweite Lücke ist der native Transport. Mein stärkster Kandidat ist nicht ein primitiver Term \(f_y^\dagger f_x\), also kein von Gott gegebener Hoppingbefehl. Ich vermute, dass echter Transport immer eine zusammengesetzte Operation ist:
\[
\text{lokale Anregung}
\rightarrow
\text{gemeinsame Ressource}
\rightarrow
\text{lokale Anregung}.
\]Genau diese Architektur sehen wir im Vierzustandszeugen bereits funktionieren. Das fehlende Teil könnte eine global erhaltene Ressource sein, die lokal eine Cartanladung verändert und sie anderswo kompensiert. Dann wäre die scheinbare lokale Symmetrieverletzung auf globaler Ebene gar keine Verletzung.
Das würde sehr elegant erklären, warum wir den Mixer innerhalb einer einzelnen Bank nicht finden: Wir suchen lokal nach einer Operation, deren Erhaltungsgesetz erst global geschlossen wird.
Das ist aktuell meine interessanteste konkrete Hypothese.
Die dritte Lücke ist die Übersetzung von Antwort zu Geometrie. Ich würde Raum nicht aus den Labels 0 bis 63 und auch nicht unmittelbar aus A3 oder drei Pauli Matrizen ableiten. Das Hauptdokument warnt inzwischen selbst ausdrücklich davor, innere Dreidimensionalität mit physischem Raum gleichzusetzen. 
Stattdessen würde ich physische Entfernung aus dem dynamischen Antwortkernel definieren.
Zwei Regionen sind nah, wenn eine lokale Änderung mit wenigen nativen Operationen und kurzer dynamischer Antwort die andere beeinflusst. Sie sind weit entfernt, wenn viele Schritte nötig sind. Wenn die Anzahl erreichbarer Regionen mit Radius \(r\) wie \(r^3\) wächst, bekommen wir einen ersten Hinweis auf drei Dimensionen. Wenn gleichzeitig die Front der Antwort eine universelle maximale Geschwindigkeit besitzt, bekommen wir einen Lichtkegel.
Dann wäre Raum wirklich emergent und nicht hineingemalt.
Dadurch bekommt auch Zeit eine viel sauberere Bedeutung
Die aktuelle Clock Entdeckung bringt mich zu einer ziemlich klaren These:
Der TFPT Clock ist vermutlich nicht Zeit. Er ist eine interne diskrete Frame Operation.
Physische Zeit entsteht erst, wenn drei Dinge zusammenkommen: ein Hamiltonoperator, ein nichtstationärer Zustand und Records, anhand derer sich „vorher“ und „nachher“ unterscheiden lassen.
Das passt auffällig gut dazu, dass ein stationärer Grundzustand unter \(H\) nur eine globale Phase bekommt. Daraus entsteht kein Zeitpfeil. Ebenso erzeugen bloße Basiswechsel keine echte Eichkrümmung. Diese Grenzen sind im neuesten Audit ausdrücklich festgehalten. 
Also vielleicht:
Clock = Orientierung.
Hamiltondynamik = Veränderung.
Record = beobachtbare Zeit.
Das wäre wesentlich sauberer als zu versuchen, aus einer einzelnen zyklischen Symmetrie sofort Sekunden zu bauen.
Materie würde dann ebenfalls ziemlich natürlich entstehen
Das N64 Ergebnis zeigt bereits den Prototyp.
Das Vakuum ist nicht „nichts“. Es ist ein stark korrelierter Grundzustand \(\Omega\).
Ein Teilchen ist dann nicht notwendig ein primitives Objekt. Es kann ein stabiler Pol in der Antwort des Vakuums sein.
Ein Elektron wäre in dieser Lesart ungefähr so fundamental wie eine Schallwelle in einem Kristall: real, stabil und messbar, aber nicht notwendigerweise der Grundbaustein des darunterliegenden Systems.
Der Unterschied zum banalen Quasiteilchenbild wäre: Wenn derselbe Quellprozess zugleich Lorentzstruktur, Ladungen, Statistik und Wechselwirkungen erzwingt, könnte das Quasiteilchen bei niedriger Energie exakt wie ein fundamentales relativistisches Teilchen aussehen.
Noch haben wir diesen relativistischen Adapter nicht. Der einfache Versuch, die 64 Labels einfach als gleichhändige Weylfelder zu deklarieren, scheitert sogar basisunabhängig. Zusätzliche Dirackomponenten, ein unabhängiger Zweierfaktor oder Ableitungsterme sind dagegen nicht ausgeschlossen. 
Das sehe ich positiv: Die Mathematik zwingt uns gerade dazu, den Lorentzspinor aus der globalen Dynamik entstehen zu lassen, statt ihn nachträglich auf die internen Labels zu kleben.
Meine These zu Eichfeldern und Chiralität
Eichfelder würde ich ebenfalls nicht als neue Substanz hineinbauen.
Wenn verschiedene lokale TFPT Ansichten \(J_x\) in dieselbe globale Algebra eingebettet sind, muss man festlegen, wie interne Frames beim Übergang von \(x\) zu \(y\) miteinander verglichen werden.
Diese Vergleichsoperation ist im Grunde eine Connection.
Aber: reine Basiswechsel teleskopieren um eine geschlossene Schleife wieder zur Identität. Das wurde ausdrücklich klargestellt. Für echte Krümmung braucht man eine dynamisch ausgewählte Transportstruktur, nicht nur Koordinatenwechsel. 
Meine Vermutung wäre deshalb: Eichfelder sind die interne Phase des realen Transportoperators. Raumgeometrie ist seine Erreichbarkeitsstruktur.
Dasselbe Objekt hätte dann einen äußeren Teil, „wohin kann ich gelangen?“, und einen inneren Teil, „wie dreht sich mein Zustand dabei?“.
Das wäre sehr elegant.
Chiralität würde ich anschließend nicht durch eine manuelle „links“ Markierung lösen, sondern als Index oder spektralen Fluss dieses globalen Transportoperators. Damit könnte aus einer global nahezu symmetrischen Quelle bei niedriger Energie ein asymmetrischer chiraler Sektor entstehen.
Und Gravitation?
Hier wäre meine Arbeitsthese:
Wenn Raum selbst aus dem Antwortoperator entsteht und der Antwortoperator vom Zustand abhängt, dann verändert Energie automatisch die effektive Geometrie.
Dann ist
\[
\text{Materie}
\rightarrow
\text{verändert Antwortkernel}
\rightarrow
\text{verändert effektive Abstände und Kausalstruktur}.
\]Das klingt schon verdächtig nach Gravitation.
Aber das allein reicht nicht. Eine echte Lösung muss im Niedrigenergielimes einen masselosen Spin zwei Sektor mit genau zwei Helizitäten, positiver Energie und universeller Kopplung liefern. Genau diese Anforderungen bleiben explizit offen. TFPT_Universalraum_Clock_Gemeinsame_Quelle_Konsolidierung_2026-09-15_v1.6.6.mdMD
Ich würde Gravitation deshalb ganz bewusst als letzten Test und nicht als nächsten Trick behandeln. Wenn wir native Geometrie, Kegel und chirale Materie haben, kann man fragen, ob kleine kollektive Schwankungen dieser Geometrie automatisch Spin zwei ergeben.
Wenn ja, wird es richtig spannend.
Und RH, Primzahlen, Faktorisierung und P gegen NP?
Hier würde ich momentan bremsen. Die gemeinsame Universalraumidee kann erklären, warum Arithmetik als Schatten derselben Kompositionsstruktur auftauchen könnte. Primitive Operationen könnten in einem kommutativen Schatten wie Primfaktoren wirken. Das ist ein reizvoller Gedanke. Das Hauptdokument formuliert genau diese engere Hypothese. TFPT_Universalraum_Hauptdokument_2026-09-15_v1.6.pdfPDF
Aber primitive Schleifen eines allgemeinen Netzes sind nicht automatisch Primzahlen. Gemischte primitive Zyklen entstehen ebenfalls.
Für RH gibt es immerhin ein messerscharfes Endziel: Würden wir aus derselben Quelle einen positiven selbstadjungierten Operator \(A\) konstruieren und exakt
\[
\frac{\Xi(z)}{\Xi(0)}
=
\det(I-z^2A^{-2})
\]beweisen, wäre das tatsächlich hinreichend. Diesen Operator und diese Identität haben wir nicht. Ebenso existieren aktuell weder ein neuer effizienter Faktorisierer noch eine P gegen NP Lösung. TFPT_Universalraum_Zwei_Banken_Konsolidierung_2026-09-15_v1.6.5.mdMD
Ich würde deshalb Physik und Arithmetik vorerst parallel aus derselben Quelle ableiten wollen, statt eine Seite gewaltsam aus der anderen zu erklären. Treffen beide später auf exakt denselben Operator, wäre das ein sehr starker Befund.
Wenn ich alles auf eine fundamentale Vermutung verdichten müsste
Dann wäre es diese:
Die fundamentale Realität besteht nicht aus Teilchen in einem Raum. Sie besteht aus einer kleinen Algebra erlaubter, phasenbehafteter Veränderungen und einem globalen Zustand, in dem diese Veränderungen stattfinden.
TFPT ist vermutlich eine erstaunlich starre algebraische Darstellung dieser Regeln.
Der Universalraum ist die vollständige Ausführung dieser Regeln, einschließlich Zustand, echter Operationsverfügbarkeit, Gedächtnis und Auslesung.
Raum ist das großskalige Muster dynamischer Erreichbarkeit.
Zeit ist die relationale Ordnung tatsächlich stattfindender und aufgezeichneter Veränderungen.
Materie sind stabile Pole und topologisch geschützte Anregungen.
Eichfelder beschreiben, wie interne Frames bei realem Transport gegeneinander gedreht werden.
Gravitation entsteht, wenn der Zustand selbst diese Transportgeometrie verändert.
Und der nächste fundamentale Durchbruch wäre deshalb meiner Ansicht nach nicht „noch eine größere E8 Rechnung“.
Er wäre eine einzige globale Quellenkonstruktion, in der wir zwei lokale TFPT Ansichten \(A\) und \(B\) definieren und aus genau derselben primitiven Regel gleichzeitig
\[
G_{AB}(0)
\qquad\text{und}\qquad
G_{AB}(t)
\]berechnen können, wobei \(G_{AB}(t)\) eine echte neue Antwort enthält und nicht nur die ursprüngliche Überlappung umbenennt. Genau diesen Test benennt auch die aktuelle v1.6.6 Konsolidierung als nächsten entscheidenden Schritt. TFPT_Universalraum_Clock_Gemeinsame_Quelle_Update_2026-09-15_v1.6.6.mdMD
Wenn dieser eine Mechanismus nativ gelingt, würde ich unsere Einschätzung deutlich hochstufen. Denn dann hätten wir erstmals in derselben Quelle: innere Symmetrie, Clock, ausgewählten Zustand, stabile Materieanregung und echte Bewegung.
Dann fehlt nicht mehr „irgendwie Raumzeit“.
Dann hätten wir zum ersten Mal etwas, aus dem man Raumzeit tatsächlich ableiten kann.

---

# Nutzerquelle F: Operationssatz, Grundzustand und Feldwoerterbuch v1.6.3

Unveraenderte Nutzerquelle, als Vorschlag und nicht als Beweis uebernommen. Die Pruefung und eigene Fortsetzung stehen in Teil B.

# TFPT / Universalraum: Operationssatz, nativer Grundzustand und Feldwörterbuch

**Forschungsfortsetzung v1.6.3 · 15. September 2026**

Diese Runde bearbeitet die vier Prioritäten aus v1.6.2 §14 in der dort
festgelegten Reihenfolge: den tatsächlich verfügbaren Operationssatz exakt
abgrenzen, den berichteten nativen Grundzustand mit seinem ursprünglichen
Hamilton- und Sektorvertrag reproduzieren und darauf die geladene Antwort
berechnen, das relativistische Feldwörterbuch am tatsächlichen Tensor
festhalten. Eine räumliche Skalierungsrechnung ist ausdrücklich **nicht**
Gegenstand; sie trägt erst, wenn Zustand, Operationen und Feldtyp stehen.
Haupt- und Update-PDF v1.6 bleiben unverändert. Kein vollständiges T1-T8-Tor
wird geschlossen.

## 1. Ergebnis in einem Absatz

Der N=64-Sektor des nativen Modells ist exakt als Loch-Paarerzeugung auf dem
gefüllten Zustand realisiert; seine Krylov-Kette ist bis zu 15 252 960
Einträgen exakt berechnet, ihre Normen ν₁…ν₄ sind auf zwei völlig
unabhängigen Wegen (Besetzungsbild und Onishi/Wick-Spurnetzwerke) identisch.
Die Kette schließt bei zwei Bosonen **exakt nicht** (Defekt 2,9·10⁻⁵), das
Modell ist also nicht allein durch seine Normen lösbar, numerisch aber fast.
Rigorose Ritz-Obergrenzen, Bosonbesetzung, Überlapp, Verschränkungsuntergrenze
und die vollständige Ein-Teilchen-Antwort (Z_h + Z_add = 1) liegen vor. Die
Worker-Behauptung eines eindeutigen N=64-Grundzustands bis g/Δ = 1/20 ist mit
Casimir-Schranken nur bis g/Δ ≤ 0,0251 beweisbar und bei 1/20 **nicht
reproduziert** (nicht widerlegt). Die Kommutanten-Leiter zeigt exakt, wie viel
unsichtbare Freiheit jede Operationsstufe beseitigt: zwei Kontrollen lassen
1,44·10⁹ Freiheitsgrade in N=3, die volle innere Symmetrie sieben. Das
Feldwörterbuch ist am Tensor entschieden: der Vermittler kann nur Vektor oder
antisymmetrischer Tensor sein; ein einheitliches Vektor-Wörterbuch existiert
nicht (Trägergraph nicht bipartit, 5-Zyklus [16,45,0,30,37]); der einzige
einheitliche Typ ist (1,0)⊕(0,1), ein B_{μν}, kein Spin 2.

## 2. Unveränderte Quelle und Konventionen

\[
H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad N=N_f+2N_b,\qquad WW^{\mathsf T}=8I_{60}.
\]

Der Tensor wird repo-lokal gelesen (SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`), der
Clock-Konstruktor ist gepinnt (`9bf99de7…`). `common.py` prüft: 60 Kanäle × 8
disjunkte Paare, jede Mode in 15 Kanälen; Gewichtserhaltung auf allen 480
Paaren; die Casimir-Identität 8WᵀW + 𝒞_S + 𝒞_C − 120 I = 0 auf allen 2016
Zweiteilchenzuständen (𝒞 = −ΣL², d. h. viermal der Standard-Casimir);
induzierte Bosongeneratoren X_B = WΛ²(X)Wᵀ/8 gaußganzzahlig und exakt
kovariant; Clock-Lift Periode sechs, Slot-Permutation (2,0,1,4,3),
Vorzeichen −1, WΛ²G_F = G_B W.

## 3. Operationssatz und Kommutant

Gemessen wird die Dimension des Kommutanten der von einer Operationsstufe
erzeugten Algebra auf dem Sektor: kleiner Kommutant bedeutet weniger
unsichtbare Freiheit. Das Spektralzertifikat für N=3 ist reproduziert
(S = C₃C₃ᵀ wird von ∏(S−r), r ∈ {0,7,10,12}, exakt annulliert;
Multiplizitäten 64, 2880, 576, 320 aus rationalen Projektorspuren).

### 3.1 Exakte Irreduzibel-Zerlegung (Höchstgewichtsvektoren)

| Sektor | Block | Dim | Zerlegung unter so(10)⊕su(4) | (𝒞_S, 𝒞_C) |
|---|---|---:|---|---|
| N=2 | helle Paare ↔ Bosonen | 60 | (10, 6) | (36, 20) |
| N=2 | dunkle Paare | 1956 | (120, 10) ⊕ (126, 6) | (84,36), (100,20) |
| N=3 | dunkle Tripel = ker C₃ | 37888 | (560, 20″) ⊕ (1200, 20) ⊕ (672, 4̄) | (117,63), (141,39), (165,15) |
| N=3 | ker S | 64 | (16, 4̄) | (45, 15) |
| N=3 | λ = 12 | 320 | (16, 20) | (45, 39) |
| N=3 | λ = 10 | 576 | (144, 4̄) | (85, 15) |
| N=3 | λ = 7 | 2880 | (144, 20) | (85, 39) |

Alle Multiplizitäten sind eins; Σ m·dim stimmt in jedem Block mit der
Weyl-Dimensionsformel. Höchstgewichte in verdoppelten Koordinaten, z. B.
(560,20″) ↔ ([3,3,1,1,−1],[3,3,3]), (672,4̄) ↔ ([3,3,3,3,3],[1,1,−1]).

### 3.2 Kommutanten-Leiter

| Verfügbare Operationen | N=2 | N=3 |
|---|---:|---:|
| A: {X, N_b} (die zwei bisher geprüften Kontrollen) | 3 829 536 | 1 444 233 216 |
| B: A + Clock (Ordnung 6) | 641 760 | 240 742 144 |
| Cc: A + 15 su(4)-Generatoren | 30 376 | 2 247 168 |
| Cs: A + 45 so(10)-Generatoren | 172 | 1 648 |
| C: A + alle 60 Generatoren | 3 | 7 |
| D: B + C | 3 | 7 |
| B(H_N) | 1 | 1 |

Für A ist die Blockstruktur M₃₇₈₈₈ ⊕ M₆₄ ⊕ (I₂⊗M₂₈₈₀) ⊕ (I₂⊗M₅₇₆) ⊕ (I₂⊗M₃₂₀);
für B folgen die Zahlen aus exakten Spuren der Clock-Potenzen je Block (z. B.
Multiplizitäten 6384/6280/6280/6384/6280/6280 auf dem Dunkelraum); für die
Lie-Stufen aus Σ m_i². Der Clock ist auf **keinem** irreduziblen Block ein
Skalar (er verschiebt Gewichte; Zeugen im JSON), also ein äußeres Element der
Symmetrie, nicht in ihrer zusammenhängenden Gruppe. D = C gilt trotzdem, weil
alle Multiplizitäten eins sind und der Clock jeden Block in sich abbildet.

**Folgerung.** Mehrfachwiederholung der zwei Kontrollen beseitigt nichts; der
Clock allein reduziert um einen Faktor sechs; erst die innere Symmetrie als
Operationssatz kollabiert die Freiheit auf je einen Skalar pro
(Energieblock, Irrep). so(10) ist dabei die wirksamere Hälfte. Ob der Compiler
diese Symmetrieoperationen tatsächlich bereitstellt, ist damit nicht
bewiesen; ihr Effekt ist exakt beziffert.

## 4. Der native N=64-Grundzustand

### 4.1 Lochbild

Mit h_i = f_i† ist |F⟩ = f₀†…f₆₃†|0⟩ das Lochvakuum und als Operatoridentität
P_A = −Q_A† mit Q_A† = Σ_{i<j}W_{A,ij}h_i†h_j†. Unter (−1)^{N_b} ist H
äquivalent zu

\[
H_{\rm hole}=\Delta N_b+g\sum_A(b_A^\dagger Q_A^\dagger+Q_Ab_A),\qquad N_h=2N_b.
\]

Die Teilchen-Loch-Unitäre trägt das Vorzeichen s(μ) = (−1)^{i+j} je
Zweilochzustand; die naive Komplement-Abbildung ohne s(μ) ist keine Identität
(Negativkontrolle bestanden).

### 4.2 Exakte Krylov-Kette

v_n = (T†)ⁿ|F⟩ mit T† = Σ_A b_A†Q_A†:

| n | Einträge in v_n | ν_n = ‖v_n‖² | ν_n/ν_{n−1} |
|---:|---:|---:|---|
| 0 | 1 | 1 | - |
| 1 | 480 | 480 | 480 |
| 2 | 108 240 | 439 680 | 916 = 4·229 |
| 3 | 15 252 960 | 575 078 400 | 299520/229 |
| 4 | (nur Spurnetzwerk) | 952 296 652 800 | ≈ 1656,0 |
| 5 | (nur Spurnetzwerk) | siehe `norms_by_traces.json` | |

ν₁…ν₃ sind auf zwei unabhängigen Wegen identisch (Besetzungsbild mit
exakten Ganzzahlamplituden; Spurnetzwerke, §6). Exakte Guards: T v₁ = 480 v₀;
T v₂ = 916 v₁ (das Ein-Boson-Singulett (60⊗Λ²64̄)^G ist eindimensional);
⟨v₂|T v₃⟩ = ν₃ (Adjungiertheit); v₁, v₂ sind Singuletts unter je drei
so(10)- und su(4)-Generatoren; ⟨v₁|Σ_A Q_AQ_A†|v₁⟩ = 458·480, was die
Formel Σ_A Q_AQ_A† = 480 − (15N_h + C_std^{Loch})/2 mit dem Loch-Casimir 14
der (10,6) bestätigt - der Lochanteil von v₁ ist kein Singulett, nur der
Gesamtzustand.

### 4.3 Schließung

T v₃ = α v₂ + w₂ mit α = 299520/229, w₂ ⊥ v₂ und exakt

\[
\|w_2\|^2=\|Tv_3\|^2-\frac{\nu_3^2}{\nu_2}=\frac{5001523200}{229}\approx 2{,}18\cdot10^7,
\qquad \frac{\|w_2\|^2}{\|Tv_3\|^2}=2{,}90\cdot10^{-5}.
\]

Der Zwei-Boson-Singulettraum ist also mehr als eindimensional; die Kette ist
**exakt nicht geschlossen**, und das Modell ist nicht allein durch die ν_n
lösbar. Numerisch ist die Korrektur vernachlässigbar: w₂ koppelt nur an v₃
mit g·√(‖w₂‖²/ν₃) = 0,195 g.

### 4.4 Ritz-Obergrenzen

In der orthonormierten Basis {v₀…v_K, w₂} ist H (Δ = 1) tridiagonal plus
w₂-Zweig: Diagonale n bzw. 2; Nebendiagonalen g·4√30, g·2√229,
g·48√29770/229, …; w₂-Kopplung g·3√598377/11908.

| g/Δ | K=1 | K=2 | K=3 (+w₂) | −480g² |
|---|---|---|---|---|
| 1/20 | −0,704159 | −0,985178 | −1,094232 | −1,2 |
| 1/40 | −0,241620 | −0,288824 | −0,295357 | −0,3 |
| 1/100 | −0,045894 | −0,047851 | −0,047894 | −0,048 |
| 1/400 | −0,002991 | −0,003000 | −0,003000 | −0,003 |

Bei g/Δ = 1/20 ist die Kette bei K=3 nicht konvergiert (die Stufenkopplungen
liegen bei 1,1Δ…1,6Δ); die Verlängerung mit ν₄, ν₅ steht in
`native_ground_state.json` (Schlüssel `ritz`). Bei g/Δ ≤ 1/40 ist die
Konvergenz praktisch erreicht.

### 4.5 Observablen auf dem Ritz-Zustand (g/Δ = 1/20, K=3)

⟨N_b⟩ = 0,8421 (Hellmann-Feynman ∂E/∂Δ = 0,8421); |⟨F|Ω⟩|² = 0,397;
Bosonzahlverteilung 0,397 / 0,397 / 0,172 / 0,034; Shannon-Untergrenze der
Boson-Loch-Verschränkung 1,66 bit (rigoros, weil die reduzierte Bosondichte in
N_b blockdiagonal ist). Die Worker-Angaben „Überlapp > 1/4“ und
„Verschränkung > 0,811 bit“ sind damit konsistent, aber auf einem
nichtkonvergierten Zustand.

### 4.6 Geladene Ein-Teilchen-Antwort

Für jede Mode r (Guard r ∈ {0, 5, 63}; Transitivität der Quellsymmetrie):

\[
Z_h=\|f_r\Omega\|^2=1-\frac{\langle N_b\rangle}{32}=0{,}97368,\qquad
Z_{\rm add}=\|f_r^\dagger\Omega\|^2=\frac{\langle N_b\rangle}{32}=0{,}02632,\qquad
Z_h+Z_{\rm add}=1.
\]

Mittlere Anregungsenergien: Entnahme ε_h = 0,0311 Δ, Addition
ε_add = 1,1497 Δ. Kompositnorm Z_χ = 23⟨N_b⟩/480 = 0,0404 (die
N=4-Referenz aus v1.6.2 ergab 0,0301; verschiedene Zustände).

### 4.7 Sektorauswahl und die Worker-Behauptung

Untergrenzen aus der Casimir-Identität und quadratischer Ergänzung,
H ≥ (1−θ)ΔN_b − (15g²/2θΔ)N_f, ausgewertet als max_θ min_{N_b} je Sektor:

| g/Δ | Ritz E(64) | schärfster Konkurrent | N=64 bewiesen global? |
|---|---|---|---|
| 1/400 | −0,0029996 | N=63: −0,0029531 | ja |
| 1/100 | −0,047894 | N=63: −0,04725 | ja |
| 1/40 | −0,295357 | N=63: −0,2953125 | ja |
| 1/20 | −1,094232 | N=66: −1,2; N=62: −1,1625 | **nein** |

Bewiesener Bereich mit diesen Schranken: g/Δ ≤ 0,0251. Die Behauptung
„eindeutiger Spin(10)×SU(4)-Singulett-Grundzustand für 0 < |g|/Δ ≤ 1/20“ ist
damit **nicht reproduziert und nicht widerlegt**; bei 1/20 müsste
E(64) < −1,2 gegen N ≥ 66 und < −1,1625 gegen N = 62 gezeigt werden.
μ* = −E/64 = 0,0171 Δ liegt unter Δ/50; die frühere Aussage „μ = Δ/50 wählt
den leeren Zustand“ bleibt konsistent.

## 5. Feldwörterbuch am tatsächlichen Tensor

### 5.1 Symmetrieregel

Für Grassmann-Felder ψ_{I,a} ist Σ_{IJ}Σ_{ab} W_{IJ}K_{ab}ψ_{I,a}ψ_{J,b}
= ½Σ(T − Tᵀ) mit T_{(Ia),(Jb)} = W_{IJ}K_{ab}. Weil W antisymmetrisch ist,
verschwindet die Kopplung genau dann, wenn K antisymmetrisch ist; **nur der
symmetrische Teil des Spinorkerns koppelt**. Auf allen 60 Zeilen explizit
geprüft:

| Zuordnung | Kern K | Kopplung |
|---|---|---|
| gleichhändige Weyl, Boson Skalar (0,0) | ε antisym. | 0 |
| gleichhändige Weyl, Boson (1,0) | σ^{μν}ε sym. | ≠ 0 (Rang 32 je Komponente) |
| Dirac/Majorana: Skalar C, Pseudoskalar Cγ⁵, Axialvektor Cγ^μγ⁵ | antisym. | 0 |
| Dirac/Majorana: Vektor Cγ^μ, Tensor Cσ^{μν} | sym. | ≠ 0 |

Der Vermittler ist damit Vektor oder antisymmetrischer Tensor, niemals
Skalar, Pseudoskalar oder Axialvektor. Er trägt U(1)_N-Ladung 2; ein
masseloser geladener Vektor ist kein konsistentes freies Eichfeld (Vorbehalt,
kein Satz).

### 5.2 Chiralitätsgradierungen

Der Trägergraph (64 Moden, 480 Kanten, Grad 15, dreiecksfrei) ist **nicht
bipartit**; ein ungerader Zyklus ist [16, 45, 0, 30, 37]. Es gibt daher keine
globale Chiralitätsaufteilung, unter der alle 60 Bosonen Vektoren wären. Für
jede der 44 G-kovarianten Gradierungen ist jeder Kanal rein (nie gemischt),
aber der Bosonmultiplett zerfällt:

| Gradierung | Vektor-Kanäle | Tensor-Kanäle | Stabilisator | Kommutant der 64 |
|---|---:|---:|---|---:|
| Identität | 0 | 60 | 60 | 1 |
| Pati-Salam-Spinorsplit (10 Varianten) | 24 | 36 | 36 = so(6)⊕so(4)⊕su(4) | 2 |
| Farbsplit (3) | 40 | 20 | 52 | 2 |
| gemischt (30) | 32 | 28 | 28 | 4 |

Ein einheitlicher Lorentztyp für alle 60 Vermittler erzwingt die
gleichhändige Zuordnung und damit (1,0)⊕(0,1): ein antisymmetrischer Tensor
B_{μν}, kein symmetrisches Spin-2-Feld. Kinetische Terme: einer pro
irreduziblem Block des Stabilisators, keine Familienaufspaltung 4 → 1+3. Ein
Modenindex ist kein Raumpunkt.

## 6. Spurnetzwerk-Normen

\[
\frac{\nu_n}{(n!)^2}=\sum_{|m|=n}\frac{\|Q^{\dagger m}F\|^2}{m!}
=\Big[\text{Koeffizient von }s^n\Big]\int d\mu(z)\,
\exp\Big(-\tfrac12\sum_{k\ge1}\frac{s^k}{k}\operatorname{tr}\big((\bar ZM)(ZM)\big)^k\Big),
\]

über bosonische Kohärenzzustände, die Onishi-Determinante
det(1 − M̄M)^{1/2} und Wick-Paarung der z-Variablen. Jedes Netzwerk ist eine
Kontraktion von n Kopien des Tensors Φ_{ij,kl} = Σ_A(M_A)_{ij}(M_A)_{kl}
(Einträge in {−1,0,1}). Netzwerke werden als 4-Bein-Multigraphen unter
Knotenumbenennung und Slot-Tausch kanonisiert (n=4: 120 → 27 Klassen).
Exaktheit: float64-Kontraktion mit Absolutwert-Begleitkontraktion
(|Σa_kb_k| ≤ Σ|a_k||b_k| < 2⁵³ je Schritt), sonst Auswertung modulo fünf
Primzahlen < 2¹³ mit CRT (Eindeutigkeit aus |Netzwerk| ≤ 60ⁿ·64^{#Zyklen}).
Validierung: ν₁, ν₂ per Brute Force, ν₃ gegen die Vektorrechnung, CRT-Route
allein reproduziert ν₃.

## 7. T1-T8

| Tor | Beitrag dieser Runde | Weiter offen |
|---|---|---|
| T1 | Exakte Kommutanten-Leiter A→B→Cc→Cs→C; Clock als äußeres Symmetrieelement | Welche Symmetrieoperationen der Compiler tatsächlich bereitstellt |
| T2 | Lochbild bewiesen; Z_h + Z_add = 1; ε_h, ε_add | Konvergierter Zustand, Renormierung, Grenzraum |
| T3 | - (ausgeklammert) | Räumlicher Träger |
| T4 | Kern-Symmetrieregel; kein einheitliches Vektor-Wörterbuch | Chirales Maß, Anomalien |
| T5 | Exakte Krylov-Kette; ν₁…ν₄ zweifach unabhängig | Kontinuumslimes |
| T6 | Feldtyp-Census je Gradierung | Kopplungs- und Familiendaten |
| T7 | (1,0)⊕(0,1) ist B_{μν}, kein Spin 2 | Dynamischer masseloser Spin 2 |
| T8 | Sektorauswahl bewiesen bis g/Δ ≤ 0,0251; μ*-Fenster | Zustandsfunktional, native Präparation |

**Kein Tor wird als geschlossen markiert.** Keine RH-, Faktorisierungs- oder
P-versus-NP-Aussage; keine abgeleitete Hylæan-Fähigkeit.

## 8. Die jetzt entscheidenden Prüfungen

1. **Untergrenzen verschärfen.** Die Casimir-Schranke trennt N=64 bei 1/20
   nicht von N=62 und N=66. Eine Jacobi-Vergleichsschranke mit rigorosen
   Normschranken für TT† je Bosonzahl oder eine Temple-Schranke auf der
   Ritz-Kette würde den Beweisbereich anheben.
2. **Den Zwei-Boson-Singulettraum ausschreiben.** w₂ ist der erste Zeuge; die
   volle Lanczos-Kette von H (nicht nur von T†) ab Tiefe 4 braucht w₂ und
   seine Nachfolger.
3. **Operationen aus der Quelle.** Die Leiter sagt exakt, was so(10)-Operationen
   leisten würden; zu klären bleibt, welche davon der Compiler als
   markierte Operationen liefert. Der Clock ist ein äußeres Element und
   ersetzt sie nicht.
4. **Feldtyp vor Geometrie.** Jede chirale Aufspaltung macht den Bosontyp
   kanalabhängig (24/36 oder 40/20); eine räumliche Rechnung muss diese
   Aufteilung oder den einheitlichen Tensortyp explizit wählen.

## 9. Verifikation und nicht übernommene Behauptungen

`replay.py` führt fünf Prüfer normal und unter `-OO` aus und verlangt
byteidentische Ausgaben; Status, Hashes und Guardsummen stehen in
`replay_manifest.json`. Guardzahlen zählen Prüfbedingungen, keine
unabhängigen Theoreme. Exakt heißt ganzzahlig/rational; numerisch heißt
float64 mit Toleranz-Guard (Ritz-Eigenwerte ab 3×3, Observablen,
Erste-Moment-Auswertungen).

Nicht übernommen: der Worker-Beweis des N=64-Grundzustands bis 1/20; eine
physische Herleitung des Zustandsfunktionals; ein räumlicher Träger; ein
dynamischer Spin 2; die Existenz der Symmetrieoperationen als Compiler-
Primitive. Während der Runde festgestellte und behobene Fehler der zunächst
gelieferten Prüfer (u. a. Zyklus-Slots im Spurnetzwerk, Bosonengewicht,
doppelte T-Wirkung bei Bosonwiederholung, Teilchen-Loch-Vorzeichen,
min-max-Sektorschranke, skalierte w₂-Norm, ungültiger Zykluszeuge) sind durch
bleibende Guards abgesichert; keine mathematische Aussage wurde an eine
Erwartung angepasst.

Das `replay_manifest.json` der Vorrunde v1.6.2 war durch einen Lauf ohne
Zugriff auf den externen Tensorpfad auf FAIL gesetzt worden; es wurde aus den
intakten `optimized.json` (PASS-Bedingung war Byteidentität) rekonstruiert,
Summen 27143/27139/4 stimmen mit dem Delivery-Manifest.
