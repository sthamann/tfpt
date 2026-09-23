# Clifford-Quelle, physikalische Graduierung und der nichtlineare Feldanschluss

20. September 2026 · **UR.SOURCE.CLIFFORD_GRADE.01 · PARTIAL**

## 1. Frage und Entscheidungsgrenze

Gesucht bleibt der gemeinsame physikalische TFPT-Ursprung, einschließlich
der tatsächlichen Symmetriewirkung, Fermionparität und Zeitentwicklung.
Der vorherige Contract fand vor der Familienkompression den Tensor
`6 ⊗ bar4 → 4`. Hier wird entschieden, ob das Beibehalten dieser
Clifford-Matrizen den fehlenden lokalen fermionischen `c`-Sektor liefert.

Erfolg wäre ein nichtverschwindender graduierter, äquivarianter Feldtransfer
aus derselben Quelle samt ihrer Zeit. Sobald die Graduierung diesen Transfer
ausschließt, wird kein zusätzlicher Hamiltonian für diese Identifikation
optimiert. Die Fortsetzung prüft stattdessen die bereits vorhandene vollständige
Randbeschreibung auf einen Feldoperator mit der richtigen Wirkung.

Das native Modell, die endliche Seam-CAR-Quelle und die bedingte Randtheorie
sind verschiedene Konstruktionen. Weder eine neue unabhängige Quelle noch
ihre physikalische Identität wird hier angenommen. Die gemeinsame
Produktgruppe in den Vergleichssätzen ist eine explizite Voraussetzung.

## 2. Zwei zentrale Zeichen entscheiden die ganze Produktalgebra

Sei `G=Spin(10)×Spin(6)` mit der bisherigen Identifikation `Spin(6)=SU(4)`.
Verwende die zentralen Elemente

\[
A=(-1_{\mathrm{Spin}(10)},1),\qquad B=(z_{10},z_6).
\]

`A` ist die doppelte volle Drehung im Spin-Lift, nicht das Vektorzeichen.
`z10,z6` sind die zuvor fixierten Generatoren der beiden Zentren der Ordnung
vier. Im relevanten Wörterbuch haben `B` und die physikalische Parität dieselben
Eigenwerte ±1. Die vier benötigten Zeichen sind:

| Darstellung / Modus | A | B | physische Parität in der jeweiligen Quelle |
|---|---:|---:|---:|
| natives `F=(bar16,bar4)` | − | + | − |
| native Bosonen `(10,6)` | + | + | + |
| echte Vektor-CAR-Moden `(10,1)+(1,6)` | + | − | − |
| gesuchter gemeinsamer `c=(bar16,4)+(16,bar4)` | − | − | − im Randgitter |

Die ersten beiden Zeilen werden aus den ORIGINALEN `FW`/`BW`-Gewichten
rekonstruiert. Adjungieren ändert diese reellen Zeichen nicht. Die dritte
Zeile gilt, wenn die unprojizierten Majoranas tatsächlich als der angegebene
Vektor wirken; genau diese vielversprechende Identifikation wird getestet.

In der nativen Operatoralgebra ist `Ad(A)=Π_native`, `Ad(B)=1`. In der
Vektor-CAR-Algebra ist `Ad(A)=1`, `Ad(B)=Π_vector`. Folglich gilt im gewöhnlichen
graduierten Tensorprodukt als AUTOMORPHISMENIDENTITÄT

\[
\Pi_{\rm total}=\operatorname{Ad}(A)\operatorname{Ad}(B). \tag{1}
\]

Beweis: Die Identität stimmt auf sämtlichen Erzeugern und ihren Adjungierten.
Sie stimmt deshalb auf allen Produkten und Summen und auf normstetigen
Abschlüssen. Entsprechende normal implementierte Abschlüsse erben sie.
Für unbeschränkte Polynome gilt sie auf einem gemeinsamen invarianten Kern.
Es ist keine endliche Gradabschätzung und keine Aussage nur über zwei Faktoren.

Jeder Operator mit den `c`-Zeichen `(A,B)=(-1,-1)` ist damit **gerade**.
Jeder Operator mit den `s`-Zeichen `(-1,+1)` ist **ungerade**. Das gemeinsame
Randgitter hat die umgekehrte Statistik für diese beiden Spinorsektoren:
dort gilt `Π_Gamma=Ad(B)`. Ein G-äquivarianter, paritätserhaltender Transfer
kann daher auf keinem dieser beiden Spinorsektoren nichtverschwindend sein.
Das vertraute Produkt aus zwei ungeraden Faktoren ist nur der kleinste Zeuge.

Insbesondere repariert das bloße Hinzufügen der fehlenden sechs echten
Majorana-Moden die alte native Identifikation nicht. G-äquivariante
Elimination oder Umformung kann (1) ebenfalls nicht ändern. Ein anderer
Gruppenlift, nichtlokale Felder, eine sektorielle Erweiterung oder eine
anders hergeleitete Statistik ändern die Voraussetzungen. Dies ist weder
ein universelles TFPT-Verbot noch ein Verbot emergenter Spinorfelder.
Der alternative `F_aux`-Anschluss ist durch die gemeinsame `T`-Identifikation
nicht automatisch mitbeurteilt.

## 3. Unprojizierte Spinorzustände sind noch keine Spinoroperatoren

Die volle endliche Clifford-Algebra von sechzehn Majoranas ist

\[
\mathrm{Cl}_{16}(\mathbb C)=\operatorname{End}(S),\qquad \dim S=256.
\]

Die Zustandsgewichte sind `w(m)_j=1/2−m_j`, `m_j∈{0,1}`. Nach der
`5+3`-Aufteilung gibt es vier 64-dimensionale Zustandsblöcke. Das ist der
Ort, an dem die zuvor komprimierten Halbspinoren wieder auftauchen.
Der Gewichtscharakter eines Operators `|m><n|` ist dagegen

\[
w(m)-w(n)\in\{-1,0,1\}^8. \tag{2}
\]

Alle 65.536 Matrixeinheiten und alle `3^8` verschiedenen Gewichte werden
gezählt. Keines hat halbzahlige Spinorgewichte. Unabhängiger allgemeiner
Beweis: `-1∈Spin(16)` wirkt auf ganz `S` skalar als `-I`, also durch
Konjugation auf `End(S)` trivial; auf einer Spinordarstellung wirkt es
nichttrivial. Dasselbe Argument gilt bereits für `A` im Produktgruppenvergleich.

Eine Abbildung `ψ → |ψ><Ω|` hilft nicht: Der Referenzzustand transformiert
mit. Sein Gewicht wird subtrahiert; ein Spin(16)-invarianter nichtnuller
Vektor `Ω` existiert in `S` nicht. Eine gewählte Polarisation kann die
Symmetrie reduzieren, liefert aber keinen Intertwiner für die unveränderte
Gruppe. Die Clifford-Vektoren selbst existieren als ungerade Operatoren.
Ausgeschlossen wird ihre Umbenennung in Spinor-FELDoperatoren.

## 4. Die tatsächliche Zeit der endlichen Quelle

Die unveränderte Konstruktionspräfix der Seam-Quelle liefert die reellen
antisymmetrischen Matrizen `A0` und `B0=A_int`. Im deklarierten Beispiel
ist `D=A0+B0/8`; die Familie lautet `u A0+t B0`. Die originale
Einteilchenkonvention ist `h=−D`, `K=i h=−iD`. Die Vorzeichenwahl beim
Schreiben der Heisenbergentwicklung ändert die folgenden Invarianztests nicht.

Es gilt exakt `[A0,B0]=0`. Die ursprüngliche Boundary ist die Sechsebene
der Koordinaten 10 bis 15 (nullbasiert). Ihr Kreuzblock zum Carrier hat
reellen Rang zwei und quadrierte Frobeniusnorm 30 für `B0`, also `15/32`
für `B0/8`. Die ursprüngliche Boundary ist bei nichtverschwindender Kopplung
nicht invariant. Der kleinste mit `D` abgeschlossene lineare Raum wächst:

\[
6\ \longrightarrow\ 8\ \longrightarrow\ 10\ \longrightarrow\ 10.
\]

Der erhaltene Zehnerraum ist sogar unter `A0` und `B0` einzeln invariant.
Damit ist der Abschluss analytisch für alle Zeiten und die ganze Familie
gesichert, nicht nur zu vier Stichprobenzeiten. Das ist ein tatsächlicher
Quellbefund, kein Nachweis einer zehn-dimensionalen Raumzeit oder von zehn
physikalischen Teilchensorten. Insbesondere ist die originale Boundary-Sechs
nicht ohne weiteren Gruppen-/Zeitintertwiner die Hilfsfamilien-Sechs des
nativen Clifford-Tensors. Die Quelle besitzt im Präfix eine C6-Wirkung;
die volle Spin(10)×SU(4)-Symmetrie ihrer Dynamik wurde nicht hergeleitet.

## 5. Ein vorhandener neutraler Faktor repariert die Statistik nicht kostenlos

Im gemeinsamen Randwörterbuch gilt

\[
K=\operatorname{diag}(1^9,-1),\quad a=(1,1,1,-1,-1,-1,-1,-1),
\]
\[
n=(a,-1,3),\quad z=e_9-e_{10},\quad
T(p)=(p,-a\cdot p/2,a\cdot p/2).
\]

Der gemeinsame Cartan-Anteil von `x∈Gamma=Z^10` ist
`p=x_(1:8)−(x9+x10)a/2`. Die Bedingung `p=0` erzwingt

\[
x=\alpha n+\beta z,\quad \alpha,\beta\in\mathbb Z,
\qquad x^TKx=4\alpha\beta. \tag{3}
\]

Die Ganzzahligkeit folgt bereits aus `x1=alpha`, `x9=−alpha+beta`.
Alle diese Felder sind gerade. Ein G-Singulett muss insbesondere
Cartan-Gewicht null haben; Cartan-Oszillatornachkommen ändern die Parität
nicht. Im vorhandenen lokalen Gitter existiert deshalb kein ungerader
neutraler Singulettfaktor, der (1) repariert. Die formal ungeraden
Halbvektoren `u=(n+z)/2`, `v=(n−z)/2` sind einzeln nicht integral und
keine unabhängigen lokalen Gamma-Felder. Ihre geklebten Kombinationen
sind entscheidend; siehe Abschnitt 7.

Auch das Umetikettieren der nativen CAR-Annihilatoren als kommutierende
Bosonen ist keine Erhaltung des Modells. Der originale kovariante Tensor
`W:Λ²F→B` ist antisymmetrisch. Die volle Kontraktion desselben Tensors
mit kommutierenden Boson-Annihilatoren verschwindet. Eine nur geordnete
Summe `i<j` wäre dann ein anderer, nicht dieser kovariante Bilineartensor.

## 6. Ein endlicher Halb-Twist hat zwar eine Zeitfortsetzung, aber keinen neuen Feldsektor

Dieser mögliche Ausweg wird ebenfalls vor einem Modellbau entschieden.
Jeder *-Automorphismus einer vollen endlichen Matrixalgebra `M_d(C)` ist
inner: `σ=Ad(w)`. Betrachte die Erweiterungsrelationen
`S a=σ(a) S`, `S²=u`, `σ²=Ad(u)`, `σ(u)=u` für unitäres `S`.
Es folgt `u=λ w²`. Dann kommutiert `Z=w* S` mit der ganzen Ausgangsalgebra
und `Z²=λ`. Nach einer skalaren Phasenwahl ist das nur

\[
M_d(\mathbb C)\otimes\mathbb C[\mathbb Z_2]
\cong M_d(\mathbb C)\oplus M_d(\mathbb C). \tag{4}
\]

Ein Quotient wählt einen der beiden zentralen Blöcke. Im gewöhnlichen
ungraduierten Erweiterungsproblem entsteht kein neuer lokaler Spinoroperator
unter der unveränderten kontinuierlichen Gruppenwirkung. Eine zusätzliche
physikalische Graduierung oder ein anderer Feldtyp ist zusätzliche Struktur,
nicht Inhalt von (4).

Die bestehende Zeit `α_t` lässt sich dennoch exakt fortsetzen. Mit
`c_t=α_t(w)w*` setzt man `αtilde_t(S)=c_t S`. Direkt folgt

\[
\operatorname{Ad}(c_t)\sigma=\alpha_t\sigma\alpha_{-t},\quad
c_t\sigma(c_t)u=\alpha_t(u),\quad
c_{t+s}=\alpha_t(c_s)c_t.
\]

Die neue zentrale Variable bleibt dabei konstant. Das trennt die beiden
Fragen: Zeitkovarianz allein ist hier lösbar, die gesuchte Feldherkunft
wird durch dieses endliche Verdoppeln trotzdem nicht geliefert.

Der externe E8-Bauplan von Jones–Sopenko–Thorngren beginnt dagegen mit
sechzehn chiralen Feldern auf `L²(R)` und verwendet eine zweite verdrehte
GNS-Darstellung plus Intertwiner. Er setzt keine endliche 256-Zustandsquelle
mit dieser Erweiterung gleich. Seine Relationen sind daher eine passende
Quelle für die Feldsektor-Frage, aber keine TFPT-Herkunftsherleitung.
[Primärquelle, §7.3](https://arxiv.org/html/2608.26456v1#S7.SS3).

## 7. Konstruktive Fortsetzung: ein originales Randfermion erzeugt das c-Multiplett

Nun wird die vorhandene bedingte Gamma-Randtheorie mit ihrem bereits gewählten
kritischen Operator `Vc=K+2KvvᵀK` untersucht. Es wird kein weiterer Parent
eingeführt. Der entscheidende explizite Keim ist

\[
\boxed{e_9=T(-a/2)+v.} \tag{5}
\]

Der Vektor `-a/2` hat drei negative Halbkoordinaten und gehört somit zum
`c`-Halbspinor. Sei `p` irgendein Halbgewicht mit ungerader Anzahl negativer
Einträge. Dann sind sämtliche 128 Vektoren

\[
x_p=T(p)+v
\]

integral, ungerade und haben am kritischen Punkt

\[
x_p^TKx_p=1,\quad x_p^TV_cx_p=3,
\qquad (h,\bar h)=(1,1/2). \tag{6}
\]

Für eine D8-Wurzel `r=±e_i±e_j` ist `T(r)` integral und rein rechtslaufend
mit Gewicht eins. Die bekannte Gitter-Vertex-OPE enthält bei `r·p=−1`
einen einfachen Pol mit nichtverschwindendem Kokzykluskoeffizienten und
dem Feld `x_(p+r)`. Die Nullmoden liefern deshalb die Spinor-Wurzelstrings.
Das Standard-Gitter/affine-Algebra-Wörterbuch wird verwendet, nicht neu
bewiesen; die konkrete TFPT-Koordinatenidentifikation und ihr Orbit werden
vollständig geprüft. [Chu–Zheng, Einleitung und §5](https://arxiv.org/html/0808.1458v2).

Der D8-Orbit von (5) erreicht alle 128 Gewichte. Die kleinere tatsächliche
Produktgruppe Spin(10)×SU(4) erreicht nur **64** davon; der andere 64er-Zweig
wird durch die zusätzlichen D8-Wurzeln verbunden. Die beiden Zweige sind
`(16,bar4)` und `(bar16,4)`. Wir behaupten ausdrücklich keinen 128er-Orbit
unter der kleineren Produktgruppe.

Das umgeht den endlichen Clifford-Ausschluss, weil die Gruppe auf den
ursprünglichen Randfermionen **nichtlinear** wirkt. Von den 112 D8-Wurzel-
strömen `T(r)` sind in den ursprünglichen Fermionkoordinaten 56 bilinear
und 56 quartisch. Schon die 52 Wurzelströme der Produktgruppe benötigen
26 bilineare und 26 quartische Felder. Beispielsweise wird `r=e1−e4`
zum lokalen Vektor `e1−e4−e9+e10`, einem Quartikfeld. Es ist kein
linearer Bogoliubov-Generator der ursprünglichen endlichen Vektor-CAR-Quelle.

Der gesamte Spinororbit lässt sich ohne ein frei angehängtes 128er-Feld
als Zusammensetzungen derselben zehn Randfelder schreiben. Sei `k` die
gerade Anzahl gegenüber `p0=−a/2` umgedrehter Halbzeichen:

| k | Anzahl Felder | Fermionfaktoren | nötige Ableitungen bei normalgeordneten gleichen Faktoren | freie Dimension | Dimension bei Vc |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 1/2 | 3/2 |
| 2 | 28 | 3 | 0 | 3/2 | 3/2 |
| 4 | 70 | 7 | 1 | 9/2 | 3/2 |
| 6 | 28 | 11 | 4 | 19/2 | 3/2 |
| 8 | 1 | 15 | 9 | 33/2 | 3/2 |

Herleitung: `a·p=−4+k`, die ersten acht Koordinaten von `x_p` haben genau
`k` Einträge ±1, und `(x9,x10)=(1−k/2,k/2)`. Daher ist die freie Dimension
`(1+k²/2)/2=1/2+k²/4`. Ein Exponentbetrag `m` benötigt `m` gleiche
Fermionfaktoren mit zusammen `m(m−1)/2` Ableitungen. Dies ist eine
normalgeordnete freie Bosonisierungsidentität, kein Produkt identischer
Grassmannvariablen ohne Ableitungen.

Die notwendige Wechselwirkung ist damit klar sichtbar: Am freien Punkt
bilden diese Felder KEIN entartetes Strommultiplett. Gerade die vierfachen
Ströme haben dort Dimension zwei und werden erst bei der festgehaltenen
kritischen Dynamik zu chiralen Strömen der Dimension eins. Der fehlende
Ableitungsschritt ist die Herkunft dieser gemeinsamen Dynamik, nicht das
willkürliche Hinzufügen weiterer Spinorfelder.

## 8. Verbindung zur anderen Quellenlane und zur Zeit

Die neue Rotor/Gauss-Lane liefert als notwendigen Kandidaten `g=K n`.
Für den gesamten expliziten Orbit gilt exakt

\[
g\cdot x_p=n^TKx_p=-1,\qquad g\cdot T(r)=0. \tag{7}
\]

Die vorgeschlagenen Stromoperationen erhalten also diese Ladung und
organisieren einen **geladenen Feldsektor**. Bei wirklicher Eichung sind
diese Felder Intertwiner zwischen Ladungssektoren bzw. brauchen passende
Rand-/Stringdaten; sie sind keine lokalen Gauss-invarianten Observablen.
Die im Gauss-Contract bewiesene exakte Rotorreduktion konstruiert diese
Spinorströme und ihren kritischen Operator nicht automatisch.

Die unabhängige Quellenladung `q=sum x_i` verteilt sich im Orbit als
`q=−3,−1,+1,+3` mit Multiplizitäten `8,56,56,8`. Ein tatsächlicher
Quellzeitterm `−Qq/4` gibt daher unterschiedliche Frequenzverschiebungen.
Weil `g=-1` für das ganze Multiplett gleich ist, kann das Addieren von
`λ Qg` diese relativen Unterschiede nicht beseitigen. Dies konkretisiert
den bereits bekannten Einwand der Charged-Time- und Rotor-Time-Contracts;
es ist kein neu erfundener chemischer Potentialterm.

### Neu eingetroffener Flussindex-Vertrag: gleicher Quotient, verschiedene Feldwirkung

Während dieser Runde wurde `UR.SOURCE.FLUX_INDEX.01` registriert. Sein
gesamter algebraischer Checker wurde hier erneut ausgeführt; die 40
Prädikatsgruppen bestanden und der Replay stimmt mit dem gespeicherten
Zertifikat überein. Der analytische Indexbeweis wurde gelesen, aber hier
nicht als neuer eigener oder formal geprüfter Beweis ausgegeben.

Das Ergebnis verfeinert die Auswahl von `g`: Bei festem `F(E8)` erzwingt
Erhaltung der ursprünglichen q- oder Y-Markierung `g=±Kn`, ohne zusätzlich
die Neutralität des bereits gewünschten n-Terms anzunehmen. Ein bedingt
eingeführter kompakter Einheitsfluss hat den signierten Index n. Der
gesamte neutrale Gitterquotient ist `ker(g)/Zn ≅ E8`. Die kompakte
Eichquelle und ihre Flussamplitude bleiben dort selbst offen.

Die Verbindung zum hiesigen Spinor-Keim lässt sich jetzt mit einem
kleinsten exakten Operatorvergleich prüfen. Für D8-Wurzeln r gilt

\[
F(r)=T(r)-\frac{a\cdot r}{2}n.
\]

Da `a·r/2` ganzzahlig ist, sind `T(r)` und `F(r)` dieselbe Klasse im
neutralen E8-Quotienten. Ihre Wirkung auf geladene Felder ist trotzdem
nicht aus dieser Klasse bestimmt. Wähle `r=e1−e4` und `x=e9`:

\[
T(r)-F(r)=n,\qquad
B(T(r),e_9)=-1,\qquad B(F(r),e_9)=0. \tag{8}
\]

Die erste Vertex-OPE besitzt damit einen einfachen Pol, die zweite ist
regulär. Am vorhandenen kritischen Vc sind die Skalendimensionen der beiden
neutralen Vertreter außerdem **eins und zwei**. Ein identischer neutraler
Quotient ist deshalb noch keine identische geladene Operatorwirkung oder
Zeitentwicklung. Das ist ein konkreter Gegenzeuge, kein bloßer Hinweis
auf unbestimmte spätere Schwierigkeiten.

Allgemein ändert `x→x+ell n` für `g·x=−1` den halben K-Normwert um
`−ell`. Der quadratische Wert steigt daher nicht als reeller Wert auf den
geladenen Quotienten ab, obwohl seine Restklasse modulo ganzen Zahlen
wohldefiniert bleibt. Für den neutralen Quotienten ist der Wert hingegen
unverändert. Man darf den bewiesenen neutralen Gitterquotienten somit
nicht ohne weitere Daten auf den gesamten geladenen Feldraum übertragen.

Die Beziehung zum älteren E8-plus-Paar-Wörterbuch ist ebenfalls explizit.
Für `x_p=T(p)+v` setze `r=p+a/2`, `Bpair=a·r/2`, `Apair=Bpair−1`.
Dann ist r ein ganzzahliger D8-Vektor und

\[
x_p=F(r)+A_{\rm pair}e_R+B_{\rm pair}m,
\quad e_R=-e_9,\quad m=n+e_9.
\]

Insbesondere ist der Keim `e9=−e_R` im ursprünglichen E8-plus-Paar-
Wörterbuch ein reines Paarfeld. Erst die andere gemeinsame kritische
Stromwirkung organisiert seinen Spinororbit. Dies setzt die beiden
Wörterbücher präzise in Beziehung, ohne sie als dieselbe physikalisch
gewählte Phase oder denselben Hamiltonian auszugeben.

`Vc`, der Kontinuumslimes und die zehn ursprünglichen Randkanäle sind
weiterhin Voraussetzungen der bedingten Randkonstruktion. Der ursprüngliche
einzelne QWZ-Kanal und die endliche Seam-Quelle liefern sie nicht durch
bloßes Umbenennen. Ebenso ist die kritische D8-Stromsymmetrie nicht schon
der vollständige dynamische E8-Stromsektor der n-gepinnten Phase.

## 9. Urteil und verbleibender entscheidender Schritt

Die einfache Wiederaufnahme der komprimierten Clifford-Moden als zusätzliche
fermionische Faktoren ist bei festem G und gleicher Statistik ausgeschlossen.
Eine endliche innere Twist-Erweiterung ändert das nicht. Zugleich ist in
der vorhandenen bedingten Randtheorie ein konkreter Quellkeim mit dem
gesuchten Spinororbit identifiziert: `e9` unter den zusammengesetzten
D8-Strömen. Das ist ein konstruktiver, überprüfbarer Anschluss mit einer
anderen, ausdrücklich nichtlinearen Gruppenwirkung.

Das nächste Herkunftskriterium ist daher ein gemeinsamer Quelltransfer,
der die genannten quartischen Stromoperatoren, ihre chirale Gewicht-eins-
Wirkung, den richtigen n-Vertreter auf geladenen Feldern und die geladenen
Zeitfrequenzen aus demselben ursprünglichen Prozess liefert. Ein passender
numerischer Massenblock oder ein weiterer
freier Spinorfaktor genügt nicht. Bis dieser Transfer steht, bleiben
`Vc_source_derived=false` und `original_time_intertwined=false`.

Dies sind interne exakte und bedingte Forschungsergebnisse, keine
4D-Teilchentheorie, keine Erklärung aller Kopplungen oder Gravitation und
keine Schließung von T1–T8. Ein exakter Checker ist keine externe Evidenz
und kein formaler Beweisassistent. Die allgemeinen Sätze stehen oben;
der Checker prüft die konkreten Quellen und algebraischen Rechnungen.
