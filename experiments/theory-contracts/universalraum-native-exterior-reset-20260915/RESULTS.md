# Zurück zur Quelle: vier innere Komponenten, ein Paar-Tensor, zwei verschiedene Feldalgebren

Forschungsnotiz und Korrektur der Arbeitsrichtung · 15. September 2026

Diese Notiz ergänzt, ersetzt aber nicht die ausgelieferten Haupt- und Update-Dokumente v1.6.10. Deren vierbankige Modellrechnung bleibt unter ihren Voraussetzungen gültig. Ihre Priorisierung als nächster fundamentaler TFPT-Schritt wird hier korrigiert. Keine historischen Ergebnisdateien, Paper-PDFs oder fremden Arbeitsstände wurden überschrieben.

## 1. Antwort auf die konkrete Frage

**Die gemeinsame Wirkung auf den ursprünglichen W-Tensor lässt sich ohne zusätzliche Banken konstruieren.** Die bereits vorhandene Zerlegung ist

\[
V=S^+_{10}\otimes\mathbb C^4,\qquad B=\mathbb C^{10}\otimes\Lambda^2\mathbb C^4,
\qquad W:\Lambda^2V\longrightarrow B.
\]

Eine Transformation U der vier inneren Komponenten wirkt auf die zugehörigen Paare durch ihr Außenquadrat. Deshalb werden Eingangs- und Paarwirkung nicht unabhängig gewählt:

\[
G_F=I_{16}\otimes U,\quad G_B=I_{10}\otimes\Lambda^2U,
\qquad \boxed{W\Lambda^2G_F=G_BW.}
\]

Für explizite Clock- und Spiegelungslifts wurde diese Gleichung am vollständigen unveränderten Tensor geprüft. Im unveränderten Fockmodell erhalten diese Wirkungen H und seinen eindeutigen Grundzustand. In der affinen E₈-Randrealisierung sind sie innere Stromsymmetrien und erhalten deren Vakuum und konforme Entwicklung. **Das sind zwei jeweils konsistente Realisierungen; ein zustands- und operatorerhaltender Übergang zwischen ihnen ist damit nicht hergestellt.**

Die stärkere Frage »erzwingt die rohe geometrische Seam genau diesen Feldlift?« wird dadurch nicht vollständig geschlossen. Insbesondere sehen die vier Markierungen eine zentrale Liftphase nicht. Dieser Rest lässt sich hier jedoch vollständig innerhalb der festgelegten monomialen Liftklasse klassifizieren, statt eine neue Mischungsmaschine einzuführen.

## 2. Was an der vorigen Arbeitsrichtung korrigiert wird

Der Originaltensor enthält bereits 16×4 Komponenten und 10×6 Paarkanäle. Die sechs Zweierkombinationen der vier Komponenten sind die Kanten eines vollständigen Vierergraphen K₄. Sie sind zunächst **innere Paarlabels**, keine sechs räumlichen Verbindungen.

Die v1.6.10-Rechnung setzte dagegen vier vollständige Banken mit insgesamt 256 CAR-Fermion- und 240 CCR-Bosonmoden zusammen. Ihr zusätzlicher Viererkreis war nicht das vorhandene A₃-Viererobjekt. Folglich entstand dort eine relative Mischungs- und Spiegelungsfrage, die nicht als unvermeidliche ursprüngliche TFPT-Frage behandelt werden darf.

Die Konsequenz ist nicht, die bewiesenen Sätze dieser Erweiterung zu löschen. Sie werden als Sätze über eine zusätzliche Modellanordnung aufbewahrt. Die Quellenprüfung beginnt wieder bei W selbst.

## 3. Exakte Faktorisierung des nativen Tensors

Die gepinnte Datei `sources/native_tensor.npz` hat SHA-256

`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Es gilt: W hat Größe 60×2016, genau 480 nichtverschwindende Einträge ±1 und WWᵀ=8I. Die Eingangslabels sind r=4i+α mit i=0,…,15 und α=0,…,3. Die Ausgangslabels sind (μ;αβ), μ=0,…,9, α<β.

Ergänzt man jede W-Zeile zu einer antisymmetrischen 64×64-Matrix A, erhält man für **alle** 60 Matrizen

\[
A_{\mu;\alpha\beta}=B_\mu\otimes E_{\alpha\beta},
\quad B_\mu^T=B_\mu,
\quad E_{\alpha\beta}=e_\alpha e_\beta^T-e_\beta e_\alpha^T.
\]

Das ist die Komponentenform des Außenprodukts. Die Symmetrie in den Spin(10)-Indizes und Antisymmetrie in den Viererindizes sind bereits vollständig im Original vorhanden. Für beliebiges U folgt die Kovarianz durch Bilinearität des Außenprodukts; die konkreten R/J-Wirkungen wurden zusätzlich an der ganzen W-Matrix ausgewertet.

## 4. Clock, Spiegelung und die verbleibende Liftphase

Eine explizite Wahl ist

\[
R=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\-1&0&0&0\end{pmatrix},\qquad
J=\begin{pmatrix}1&0&0&0\\0&0&0&-1\\0&0&-1&0\\0&-1&0&0\end{pmatrix}.
\]

Beide liegen in SU(4), und

\[
R^4=-I,\quad R^8=I,\quad J^2=I,\quad JRJ^{-1}=R^{-1}.
\]

### 4.1 Warum das Umlaufminus in dieser Klasse nicht frei ist

Für jeden unitären monomialen Lift eines Viererzyklus mit Phasen z₀,…,z₃ gilt

\[
\det R(z)=-\prod_jz_j,\qquad R(z)^4=\Bigl(\prod_jz_j\Bigr)I.
\]

Die SU(4)-Bedingung erzwingt daher R⁴=−I. Unterschiedliche Verteilungen der Phasen mit demselben Produkt sind durch diagonale Basisphasen ineinander überführbar. Das Ergebnis setzt **einen Viererzyklus in der definierenden SU(4)-Darstellung** voraus. Es beweist nicht, dass irgendeine andere geometrische oder physische Clock diese Darstellung realisiert.

### 4.2 Der genaue Anschluss an die vier Markierungen

Setze Dₖ=diag(1,iᵏ,i²ᵏ,i³ᵏ), k=1,2,3. Diese Matrizen sind spurfrei. Direkt gilt

\[
RD_kR^{-1}=i^kD_k,\qquad JD_kJ^{-1}=D_{4-k}.
\]

Das reproduziert die in `v177_seam_marking_kernel.py` berechnete Wirkung auf den Formen wₖ=zᵏ⁻¹dz/(z⁴−1): Der Pullback von ρ:z↦iz liefert die Charaktere i,−1,−i; σ:z↦1/z vertauscht w₁ und w₃ und fixiert w₂.

Damit gibt es einen **expliziten Darstellungsanschluss**, nicht nur gleiche Eigenwertlisten. Die Zuordnung des tatsächlich realisierten Seam-Operators zum Lift auf V bleibt von der bloßen Wirkung auf diesem dreidimensionalen Unterraum verschieden.

Die aktuelle Theorie enthält weitere Clock- und Reflexionsrollen. Insbesondere ist R nicht ohne Weiteres der zuvor konstruierte Spin(10)-Lift des fünfstelligen Compilerpräfixes. Eine lineare innere SU(4)-Symmetrie, eine geometrische Inversion und eine antiunitäre Osterwalder–Schrader- oder Modularreflexion dürfen nicht gleichgesetzt werden.

### 4.3 Vollständige Klassifikation für feste R- und Markwirkung

J und iJ haben dieselbe zugrunde liegende Markpermutation und dieselbe Wirkung auf den Dₖ. Beide liegen in SU(4), beide kehren R durch Konjugation um. Trotzdem gilt

\[
(iJ)^2=-I,\qquad\Lambda^2(iJ)=-\Lambda^2J.
\]

Dies ist ein konkretes Gegenbeispiel gegen »Markwirkung allein bestimmt die Feldwirkung«.

Mehr noch: Hat L dieselbe monomiale Markpermutation wie J, so ist L=DJ mit D diagonal. Aus LRL⁻¹=R⁻¹ folgt, dass D mit R⁻¹ kommutiert. Weil der Zyklus alle vier Komponenten verbindet, ist D=zI. Die Determinante liefert z⁴=1. **Alle** Lifts dieser Klasse sind folglich

\[
J,\ -J,\ iJ,\ -iJ.
\]

Verlangt die Quelle zusätzlich eine **komplex-lineare echte Involution**, L²=I, bleiben ±J. Beide besitzen dieselbe Paarwirkung. In genau dieser Klasse ist die relative Paarspiegelung also eindeutig; auf den einzelnen Komponenten bleibt die zentrale Parität.

Im lexikographisch geordneten K₄-Kantenraum ist Λ²R die vorzeichenfreie Kantenpermutation des Zyklus. Λ²J ist **minus** die vorzeichenfreie Kantenpermutation der Spiegelung. Das Minus darf nicht durch eine Zeichnung ungerichteter Kanten entfernt werden.

Die aktuelle Theorie benennt den Symmetrielift-/Twistklassenrest bereits, unter anderem in den v506–v534-Arbeiten und im P2-Reduktionskasten des Architekturpapers. Die obige Klassifikation ist kein Beweis, dass deren spezifischer geometrischer Rest vollständig mit dieser internen SU(4)-Phase identisch wäre.

## 5. Was daraus im bisherigen Fockmodell wirklich folgt

Der Modellvertrag bleibt

\[
H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
\quad P_A=\sum_{r<s}W_{A,rs}f_sf_r,
\quad N=N_f+2N_b.
\]

Die zweiten Quantisierungen von G_F und G_B erhalten H: Der Intertwiner erhält die Konversion zweier Fermionen in einen Paarboson; die Unitarität erhält N_b. Es werden weder Hopping noch μN noch ein neues Kopplungsprofil ergänzt.

Die ursprünglichen Grundzustandsprogramme wurden in einer isolierten Arbeitskopie mit ihren Quellhashes erneut ausgeführt. Dabei wurden die 635315 Bosonkonfigurationen der Ordnungen 2,3,4 frisch enumeriert. Die vier ausgewählten rationalen Zertifikate wurden jeweils normal und optimiert wiederholt. Sie liefern erneut den Satz:

Für Δ>0 und 0<|g|/Δ≤1/20 besitzt dieses Modell genau einen globalen Grundzustand Ω mit N=64; er ist ein Spin(10)×SU(4)-Singulett.

Unabhängig vom expliziten Grundzustandsvektor folgt die Singulettaussage aus Eindeutigkeit und Symmetrie: Auf einer eindeutigen Grundzustandsgeraden könnte die zusammenhängende semisimple Gruppe nur durch einen eindimensionalen Charakter wirken; dieser ist trivial. Somit erhalten **beide** zentralen Liftklassen oben denselben Ω.

Das Vakuum beseitigt die Liftmehrdeutigkeit nicht nachträglich. Die zentrale SU(4)-Transformation iI wirkt im Modell als iᴺ. Auf N=64 ist dies eins, auf N=63 dagegen −i. Zwei Spiegelungen unterscheiden die beiden Klassen auf einem ungeraden geladenen Sektor, nicht auf der bloßen Vakuumgeraden. Auch eine phasenblinde Zweipunktmessung kann diese zentrale Phase verlieren; eine gemeinsame kohärente Feld-/Reflexionsoperation müsste sie mitführen.

### 5.1 Noether zeigt, warum vier Komponenten nicht vier Orte sind

Für jede Komponente α ist

\[
Q_\alpha=\sum_i n_{i\alpha}
+\sum_{\mu,\beta\ne\alpha}n_{b_{\mu;\{\alpha,\beta\}}}
\]

erhalten. Jeder W-Term entfernt genau ein Fermion der beiden am Paar beteiligten Komponenten und erzeugt einen Paarboson mit deren Gesamtladungen. Deshalb [H,Qα]=0 und ΣαQα=N. Auf dem Singulett Ω gilt QαΩ=16Ω.

Ein Zustand fᵢαΩ hat Qα=15 und die übrigen drei Komponentenladungen 16. Die unveränderte Entwicklung kann ihn nicht in fⱼβΩ mit β≠α umwandeln, ohne andere Ladungen mitzutransportieren. Die interne Symmetrie, die die Labels vertauscht, ist keine nachgewiesene räumliche Reise und keine automatisch verfügbare Steueroperation.

## 6. Der stärkere Quellenanschluss: W ist einschließlich der Vorzeichen ein E₈-Stromkanal

Hier wurde die Quellenfrage weitergeführt als bis zur Tensorzerlegung.

Die 64 Eingangswurzeln sind die Halbzahlvektoren

\[
\lambda_{i\alpha}=\tfrac12(\pm1,\ldots,\pm1),
\]

mit gerader Minusparität in den ersten fünf und separat in den letzten drei Koordinaten. Jede hat Quadratnorm 2. Die 60 Ausgangswurzeln sind die gemischten D₅/D₃-Wurzeln mit genau einer ±1-Komponente in jedem Block.

Für alle 2016 Eingabepaare gilt: W ist genau dann nicht null, wenn die Wurzelsumme wieder eine Wurzel ist. Alle acht Paare jeder nichtverschwindenden Ausgangszeile addieren sich zur selben Ausgangswurzel.

**Die Vorzeichen wurden nicht aus dieser Trägerübereinstimmung geraten.** In einer ganzzahligen unimodularen E₈-Wurzelbasis wurde ein Gitterkozykel

\[
\epsilon(a,b)=(-1)^{a^TEb},\qquad E+E^T=\operatorname{Gram}(E_8)
\]

gewählt. Die Frage nach Phasen sᵣ,t_A∈{±1}, sodass

\[
W_{A,rs}=s_rs_st_A\,\epsilon(\lambda_r,\lambda_s)
\]

für jeden nichtverschwindenden Eintrag gilt, ist ein lineares Gleichungssystem über F₂: 480 Gleichungen, 124 unbekannte Zeichen, Rang 115. Es ist konsistent; ein vollständiger Lösungsvektor ist in `normal.json` gespeichert. Alle 480 Gleichungen wurden danach separat geprüft. Das Umdrehen eines einzelnen ausgewählten W-Vorzeichens macht das System inkonsistent: eine negative Kontrolle gegen einen bloßen Zahlentest.

Damit ist in der E₈-Gitter-Vertexalgebra eine konkrete Phasenwahl gefunden, in der

\[
I_r(z)I_s(w)\sim\frac{\sum_AW_{A,rs}K_A(w)}{z-w},\qquad r<s.
\]

W reproduziert also **einen vollständigen, vorzeichengetreuen Operatorproduktkanal** der originalen algebraischen Hülle. Die übrigen E₈-Kanäle existieren in der Standard-Gitterkonstruktion; der Prüfer beansprucht nicht, durch 480 Gleichungen allein deren gesamte Vertexalgebra neu zu beweisen.

## 7. Der Feldtyp ist entscheidend: ein Spinorlabel ist nicht automatisch ein CAR-Fermion

In der ursprünglichen konformen Randrealisierung haben die 64 Komponenten

\[
h_{(16,4)}=5/8+3/8=1;
\qquad h_{(10,6)}=1/2+1/2=1.
\]

Es handelt sich dort um bosonische affine Ströme. Das ist bereits im ursprünglichen `v469_seam_crossedproduct_route.py` als lokale spinorielle Erweiterung mit Statistikphase +1 dokumentiert. Die 16 freien Majorana-Trägerfelder haben eine andere Rolle als die 128 Spinorfelder der E₈-Erweiterung. Der freie Träger und die bosonische Erweiterung sind nicht dieselbe lokale Feldalgebra. Dies wird auch in der Literatur zur Fermionisierung/Bosonisierung behandelt, etwa in [Shaos TASI-Vorlesungen, Abschnitt 3.2.4](https://arxiv.org/pdf/2308.00747).

Das alte Fockmodell deklarierte stattdessen 64 unabhängige CAR-Moden und 60 CCR-Moden. Dieser zusätzliche Modellvertrag war in dessen Berichten ausdrücklich benannt. **Neu ist hier nicht die Entdeckung, dass der Vertrag eine Annahme war, sondern seine konkrete Prüfung gegen den ursprünglichen Stromkanal.**

### 7.1 Ein explizites Hindernis für die naive Identifikation

Wähle aus demselben 64er-Sektor

\[
\alpha=\tfrac12(1,1,1,1,1,1,1,1),\quad
\beta=\tfrac12(-1,-1,1,1,1,-1,-1,1).
\]

Es gilt α·β=0. In der geraden Gitter-Vertexalgebra gilt

\[
Y(e^\alpha,z)e^\beta
=\epsilon(\alpha,\beta)z^{\alpha\cdot\beta}
\bigl(e^{\alpha+\beta}+O(z)\bigr).
\]

Der Kozykelkommutator ist (−1)^(α·β)=1. Daher folgt auf dem Vakuum

\[
\{J^\alpha_{-1},J^\beta_{-1}\}|0\rangle
=2\epsilon(\alpha,\beta)e^{\alpha+\beta}\ne0.
\]

Zwei unabhängige CAR-Erzeuger erfüllen dagegen {fα†,fβ†}=0. Deshalb ist die direkte Zuordnung fα†↦Jα₋₁ nicht algebra- und vakuumerhaltend. Die Normquadrat-vier-Wurzelsumme erzeugt einen vorhandenen Zustand vom konformen Gewicht zwei; sie darf nicht nur deshalb gelöscht werden, weil sie keine E₈-Wurzel mehr ist.

Die verwendete Gitter- und Kozykelkonstruktion findet sich in [Huang, Lecture notes on vertex algebras, Abschnitt 2](https://sites.math.rutgers.edu/~yzhuang/rci/math/papers/va-lect-notes.pdf). Das Gegenbeispiel ist eine eigene Anwendung auf die konkreten Eingangslabels.

Dies schließt weder eine nichtlokale Fermionisierung noch Defektfelder, andere Sektoren oder physische Bulkfermionen aus. Es schließt die **ungeprüfte direkte Identifikation dieser Erzeuger** aus. Ebenso darf konformes Randgewicht eins nicht mit einem bereits hergeleiteten 3+1D-Lorentzspin verwechselt werden.

## 8. Ein positiver gemeinsamer Prozess ohne zusätzliche Banken

Innerhalb der bereits gewählten affinen E₈-Randrealisierung stehen Algebra, Zustand und konforme Entwicklung gemeinsam zur Verfügung. Für normierte Ströme gelten bei Niveau k=1

\[
[J_m^a,J_n^b]=if^{ab}{}_{c}J_{m+n}^c+m\delta^{ab}\delta_{m+n,0},
\]
\[
T(z)=\frac1{2(1+30)}\sum_a:J^aJ^a:(z),\qquad c=\frac{248}{31}=8,
\qquad[L_0,J_{-n}^a]=nJ_{-n}^a.
\]

Das ist die etablierte Sugawara-Konstruktion, keine neu erfundene TFPT-Dynamik. Sie ist hier der richtige Standardvergleich für die bereits vorhandenen Felder.

### 8.1 Dieselbe Algebra liefert die Zwei- und Dreipunktantwort

Mit passend normierter Adjungierung und dem konformen Vakuum:

\[
\langle I_r^\dagger(z)I_s(w)\rangle=\frac{\delta_{rs}}{(z-w)^2},
\]
\[
\langle K_A^\dagger(z_3)I_r(z_1)I_s(z_2)\rangle
=\frac{W_{A,rs}}{(z_1-z_2)(z_3-z_1)(z_3-z_2)}.
\]

Die Dreipunktantwort enthält genau den oben einschließlich seiner Phasen rekonstruierten Tensor. R und J erhalten diese Antwort gemeinsam, weil sie denselben Intertwiner, das Vakuum und den Stressenergietensor erhalten. Es werden keine unabhängigen Raum-, Paar- und Zustandskarten angepasst.

Auf dem euklidischen Einheitszylinder ergibt sich für einen normierten Strom bei gleichem Winkel

\[
G(\tau)=\sum_{n\ge1}n e^{-n\tau}
=\frac{q}{(1-q)^2},\qquad q=e^{-\tau},\quad\tau>0.
\]

Die Modennorm n folgt aus dem zentralen Stromkommutator; die geometrische Summe liefert die geschlossene Antwort. Die rationale Summenformel und ihre ersten zwölf Koeffizienten wurden im Prüfer kontrolliert; die allgemeine Aussage folgt analytisch aus der geometrischen Reihe, nicht aus zwölf Stichproben.

Bei Kreisumfang L und Geschwindigkeitsnormierung v lautet die Energie n·2πv/L über dem Vakuum. Das ist ein räumlich skalierbarer **konformer Randprozess**, dessen Modenlücke mit 1/L fällt, keine aus der Seam hergeleitete 3+1D-Welt. L und v sind hier Normierungs-/Geometriedaten. Insbesondere ist dies nicht die frühere isolierte N=63-Entnahmelinie des zusätzlich gewählten Fock-Hamiltonoperators.

### 8.2 Was »ein Kernel« leisten kann und was nicht

Ein vollständiger zeitabhängiger Korrelationskern enthält bereits Entwicklungsinformation. Ein bloßer Gleichzeit-Kovarianzkern bestimmt im Allgemeinen nur einen Zustand: Verschiedene positive Energien für dieselben leeren freien Moden besitzen denselben Vakuumprojektor. Die ursprüngliche Aussage »ein quasi-freier Kernel bestimmt alle Wick-Korrelationen« darf deshalb nicht ohne genaue Zeit- und Felddefinition zur eindeutigen Herleitung eines Hamiltonoperators erweitert werden.

Der hier benutzte L₀ ist durch den **gewählten konformen Stromvertrag** vorgegeben. Die Herleitung dieses Vertrags aus dem rohen Seam-Prozess wird nicht durch Umbenennung in »Universalraum« ersetzt.

### 8.3 Die Paarfelder lassen sich rekonstruieren, statt als neue Oszillatoren hinzugefügt zu werden

Der gefundene Operatorproduktkanal und WWᵀ=8I liefern unmittelbar

\[
\boxed{K_A(w)=\frac18\sum_{r<s}W_{A,rs}\,
\operatorname{Res}_{z=w}\bigl(I_r(z)I_s(w)\bigr).}
\]

Beweis: Setze den Operatorproduktkanal aus Abschnitt 6 ein; die Koeffizienten vor K_B sind (WWᵀ)AB/8=δAB. Das gilt gleichzeitig für alle 60 Felder und mit derselben geprüften Phasenkonvention. K_A ist damit ein abgeleiteter lokaler Stromkanal der vorhandenen Randfelder, kein neu postulierter unabhängiger CCR-Oszillator.

Dies ist eine konkret einfachere Fortsetzung der Frage nach einer »Paarbank«: zunächst prüfen, ob überhaupt neue unabhängige Freiheitsgrade nötig sind. Es ist keine Behauptung, dass diese lokale Residuenoperation bereits zwischen zwei endlich getrennten Intervallen ausgeführt werden kann. Dafür fehlen die räumliche Feldzuordnung und ein quellenseitig verfügbares Instrument. Insbesondere wird durch die Formel weder eine Bank in jeder geometrischen Lücke noch der frühere kubische Fock-Hamiltonoperator hergeleitet.

## 9. Entscheidung für die weitere Arbeit

Die bisherige Standardroute »weitere W-Banken bauen → ihre Mischungen auswählen → ihren Grundzustand beweisen → nach Raumzeit fragen« ist nach dieser Prüfung nicht der fundamentale nächste Schritt.

Die konkrete neue Arbeitsgrundlage ist das vorhandene Strom-/Feldsystem mit seinem Originaltensor und dem expliziten Außenproduktlift. Die bisher getrennten Prüfungen haben jetzt eine gemeinsame Referenz:

1. Die Operation muss auf den **tatsächlichen Feldern** definiert sein, nicht nur auf ihren vier sichtbaren Markierungen. Ihre Linearität/Antilinearität und ihr Quadrat müssen mitgeführt werden.
2. Die Feldkarte muss mindestens Produkte und Adjungierung erhalten. Für die naive CAR-Karte liegt bereits ein exaktes Gegenbeispiel vor; dieses darf nicht durch weitere gute Polzahlen übersprungen werden.
3. Aus der geprüften Feldkarte werden Antworten und Entwicklung zusammen übertragen. Zwei- und Dreipunktantworten des originalen Strommodells stehen jetzt als berechenbare Referenz bereit.

Der langfristige physische Schritt ist danach nicht bloß »mehr Kopien rechnen«, sondern die Ableitung einer lokalen Bulkbeobachtungsalgebra und ihres Dynamikadapters aus dieser Referenz. Ein gemeinsamer physischer 3+1D-Ursprung, das chirale Maß und dynamische Gravitation sind nicht konstruiert. Kein vollständiges T1–T8-Ziel wird hier als geschlossen markiert; RH, Faktorisierung und P versus NP werden in dieser Runde nicht bearbeitet.

## 10. Reproduktion und Beweisgrenze

`verify_native_reset.py` prüft **2825 exakte Bedingungen**, darunter alle 2016 Trägerpaare, alle 480 Kozykelvorzeichen und negative Kontrollen. Normaler und optimierter Lauf liefern dieselben JSON-Bytes. Die Zahl zählt viele Komponentenprüfungen und ist keine Zahl unabhängiger Theoreme.

`replay_ground_here.py` wiederholt zusätzlich die ursprüngliche Grundzustandsrechnung in `ground_replay/`; alle zwölf Prozessaufrufe liefen erfolgreich durch, die vier JSON-Zertifikate sind jeweils optimierungsunabhängig. Die alte NumPy-ComplexWarning ist in den gespeicherten Fehlerausgaben erhalten. Der neue Tensorprüfer bestätigt vor jeder Ganzzahlkonversion reelle ganzzahlige Eingaben.

Ausführung im Repository:

```text
/opt/homebrew/bin/python3 experiments/theory-contracts/universalraum-native-exterior-reset-20260915/replay_ground_here.py
/opt/homebrew/bin/python3 experiments/theory-contracts/universalraum-native-exterior-reset-20260915/run_replay.py
```

`sources_manifest.json` fixiert die verwendeten Repositoryquellen. `normal.json` enthält die vollständige Kozykelphasenlösung; `replay.json` die kompakte Ausführungsprüfung. Die analytischen Folgerungen über Fockraum, Singulett, Vertexalgebra und konforme Korrelationen sind oben ausgeschrieben. Sie sind nicht allein durch einen grünen Programmlauf formal bewiesen.

**Kurzurteil:** Der einfache gemeinsame algebraische Anschluss war im Außenprodukt des ursprünglichen Tensors bereits vorhanden. Die größere Verwechslung lag im Übergang von dieser Stromalgebra zu unabhängig gesetzten Oszillatoren und von inneren Labels zu Raumorten. Diese Runde liefert eine explizite Korrektur und einen vorzeichengetreuen Quellenanschluss — keine vollständige TOE.

## 11. Nachtrag: die anschließend eingegangene 331-Prüfungen-Arbeit

Beide anschließend gesendeten Texte beziehen sich auf denselben Ergebnisordner `universalraum-seam-reflection-lift-20260915`, nicht auf zwei unabhängig bereitgestellte vollständige Prüfpakete. Der komplette dortige Prüfer wurde hier unverändert normal und optimiert wiederholt: beide Ausgaben sind byteidentisch mit den gelieferten Ergebnisdateien. Es wurden keine Dateien dieses fremden Forschungsordners verändert.

Das Ergebnis wird **bedingt übernommen**, aber seine Herkunftsbehauptung korrigiert. Der geometrische Lift auf dem vorgegebenen Ring und die sechs inneren W-Lifts funktionieren. `v480_multilocal_four_interval.py` setzt jedoch die antiperiodischen Impulse ein und lässt die rohe Seam-Realisierung ausdrücklich offen; es beweist nicht das in beiden Texten behauptete allgemeine Nullmodenverbot durch RP. Ferner konstruiert die neue Arbeit die Ringwirkung und die innere W-Wirkung getrennt, nicht eine quellenseitige Feldkarte zwischen beiden.

Die vollständig ausgeführte Prüfung, die allgemeine größenunabhängige Ringformel sowie die Integrationsentscheidung stehen in [AUDIT_RECEIVED_REFLECTION.md](AUDIT_RECEIVED_REFLECTION.md). Die Kozykelrekonstruktion und die Residuenformel oben wurden eigenständig erarbeitet und dürfen nicht mit einem Beweis verwechselt werden, dass die vier gezeichneten Ringlücken physische W-Bänke sind.
