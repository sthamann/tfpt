# Stationärer Anschluss aus dem vollständigen endlichen TFPT-Parent

10. September 2026. Konstruktiver Satz unter den bereits gegebenen endlichen Gitter-/Hamiltonvoraussetzungen. Der thermische Hochtemperaturgrenzgang ist eine zusätzliche ausdrücklich gewählte Untersuchung, keine aus den ursprünglichen Compilerprinzipien hergeleitete kosmische Temperatur.

## 1. Ergebnis und genaue Quantoren

Fixiere einen kubischen periodischen Torus mit N=L³, L≥5, κ=1/100 und dem unveränderten Rotor/CAR-Parent H. Arbeite auf der **gesamten physikalischen Gauß-Hilbertspace** mit Hintergrundladung eins pro Ort. Sie enthält alle Low-/High-Besetzungen mit insgesamt N Fermionen, nicht nur die All-low-Präparation.

Wähle eine orientierte Plaquette p und einen Link e darin mit p_e=1. Auf dem vollständigen physikalischen Raum wirken

    W|E,mask>=|E+p,mask>,
    S_m^p|E,mask>=|E+(m−1)E_e p,mask>.

Für die konkrete von W und S_m^p erzeugte affine C*-Algebra A_p gilt:

    ρ_β = exp(−βH)/Tr_phys exp(−βH),  β>0,
    lim_{β↓0} ρ_β(A(a,m,n,b)) = δ_{m,n}δ_{a,b}/n,           (1)

wobei A(a,m,n,b)=W^a S_m^p(S_n^p)*W^(−b). Der Limes auf A_p ist genau der zuvor konstruierte kritische arithmetische Zustand τ. Jedes ρ_β ist ein normaler stationärer Zustand der **vollen** H-Dynamik. Jeder schwach*-Häufungspunkt in B(H_phys)* ist daher ein ebenfalls H-stationärer, im Allgemeinen singulärer Erweiterungszustand von τ.

Der ganze Zustand auf B(H_phys) wird nicht als eindeutig konvergent behauptet. Die eindeutige Grenze ist auf A_p bezeichnet. Die arithmetische Normzeit λ_t(W)=W, λ_t(S_m^p)=m^(it)S_m^p wird dadurch nicht mit der elektrischen oder vollen physikalischen Zeit identifiziert.

## 2. Vollständige Gauß-Koordinaten

Der Torus hat E_count=3N Kanten und N Knoten. Für jede der D=binom(2N,N) Materiemasken ist die Gaußquelle ganzzahlig und hat Summe null. Da das Entfernen des Plaquettenlinks e den Graphen verbunden lässt, existiert eine ganzzahlige Lösung f_mask der Gaußgleichung mit (f_mask)_e=0.

Wähle einen Spannbaum ohne e, der die übrigen drei Plaquettenkanten enthält. Der Fundamentalzyklus von e ist dann p. Die übrigen Fundamentalzyklen bilden eine ganzzahlige Basis B der Zyklen mit e-Komponente null. Jeder zulässige elektrische Fluss besitzt eindeutig die Darstellung

    E = f_mask + q p + B z,  q∈Z, z∈Z^(d−1), d=2N+1.     (2)

Dies ist eine unitäre Basisidentifikation der vollen physikalischen Hilbertspace mit C^D⊗ℓ²(Z^d). W addiert eins zu q; S_m^p multipliziert q mit m und lässt mask,z unverändert. (2) ist keine Reduktion auf eine angenommene Lösung eines unbekannten arithmetischen Problems.

Jeder Fundamentalzyklus hat höchstens N Kanten. Daher ist für G_z=B*B die einfache Schranke tr G_z≤(d−1)N=2N² verfügbar. Die Matrix G=[p B]*[p B] ist positiv definit. Ihr Schurkomplement entlang q ist positiv und höchstens ||p||²=4.

## 3. Der vollständige Gibbszustand ist wohldefiniert

Schreibe H=H_el+V mit H_el=κΣ_e E_e²/2. In den Koordinaten (2) ist H_el eine positive quadratische Form auf einem vollen ganzzahligen Gitter, mit endlich vielen Verschiebungen. Also hat H_el kompakten Resolventen, endliche Wärmespur für jedes β>0 und endliche mittlere Energie im Gibbszustand.

Aus den unveränderten Low-/High-Onsitewerten und den gepaarten Hops folgt der sichere endliche Bound

    ||V||≤ C_N := (4+101/192)N = 869N/192.                 (3)

Auf dem physikalischen Sektor beträgt die gesamte Teilchenzahl N. Die Onsiteenergie ist daher höchstens 4N; der getrennte Hopbound 101N/192 wurde im Dynamikbeweis hergeleitet. Beschränkte selbstadjungierte Störung erhält Definitionsbereich und kompakten Resolventen. Min-Max liefert λ_j(H_el)−C_N≤λ_j(H)≤λ_j(H_el)+C_N, einschließlich Vielfachheiten. Daraus folgt endliche Wärmespur und thermische Energie für H.

Setze σ_β=exp(−βH_el)/Z_el. Die logarithmische relative Entropie erfüllt

    D(σ_β||ρ_β)
      = β Tr(σ_β V)+log Z_H−log Z_el ≤ 2β C_N.

Hier wurden e^(−βC_N)Z_el≤Z_H≤e^(βC_N)Z_el und die Beschränktheit von V benutzt. Quantum Pinsker mit natürlichen Logarithmen ergibt

    ||ρ_β−σ_β||_1 ≤ 2 sqrt(β C_N).                       (4)

Es werden keine kommutierenden H und H_el vorausgesetzt. (4) gilt auf der ganzen physikalischen Hilbertspace und damit für jede beschränkte Messung mit Operatornorm höchstens eins.

Zum verwendeten Standardlemma: Die Messung der positiven Spektralprojektion von ρ−σ hat binären Wahrscheinlichkeitsabstand ||ρ−σ||_1/2. Datenverarbeitung der normalen relativen Entropie unter dieser Zweiausgangsmessung und die klassische binäre Pinsker-Ungleichung ergeben D≥||ρ−σ||_1²/2. Dieses Argument gilt auch für normale Dichteoperatoren auf einem separablen unendlichen Hilbertraum; bei unendlicher relativer Entropie ist die Aussage trivial. Hier ist D durch die oben berechnete beschränkte Logarithmusdifferenz endlich. Die übliche endlichdimensionale Fassung und denselben Messungsbeweis dokumentiert [Watrous, The Theory of Quantum Information, Satz 5.38, Buchseiten 282–283](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf); dessen Logarithmusbasis zwei ist hier in natürliche Logarithmen umgerechnet.

## 4. Gaussianischer Gittergrenzgang

Für jede feste Materiemaske ist σ_β eine diagonale verschobene Gitter-Gaußverteilung auf (q,z). Quadratische Ergänzung in z gibt

    a(q+u_mask)² + positive_quadratic_z + constant_mask,

mit demselben a>0 für alle Masken und a≤2κ. Die Poissonformel in z liefert einen relativen Fehler e(q,mask) mit einem uniformen Bound |e|≤R(β), wobei

    c = π²/(κN²),
    y = exp(−c/β),
    R(β) = [1+2y/(1−y³)]^(d−1)−1.                       (5)

Denn die duale quadratische Form ist mindestens 1/tr G_z mal die euklidische Normquadratsumme; die tatsächliche exponentielle Konstante ist ≥2π²/(κ tr G_z)≥c. Für j≥1 gilt j²≥1+3(j−1), also Σ_{j≥1}e^(−cj²/β)≤y/(1−y³). Alle Phasen aus q und f_mask haben Betrag eins, daher ist die Schranke uniform auch über q und alle Masken.

Bis auf diesen relativen Fehler ist die q-Verteilung die eindimensionale diskrete Gaußverteilung mit Gewicht g(q)=exp[−βa(q+u_mask)²]. Setze

    I0 = sqrt[π/(2κβ)].

Das kontinuierliche Integral von g ist I=sqrt[π/(βa)]≥I0. Für jedes verschobene Gitter und jede Restklasse liefert die Rechteckregel mit totaler Variation TV(g)=2:

    |Σ_q g(q)−I|≤2,
    |Σ_{q≡r mod m}g(q)−I/m|≤2.

Ist I0>2, folgt für die normalisierte eindimensionale Verteilung

    max_q Prob(q)≤1/(I0−2),
    |Prob(q≡r mod m)−1/m|≤4/(I0−2),  für alle m,r.         (6)

Ist R<1, verändert die relative Poissonkorrektur die normalisierte Verteilung in l1-Norm um höchstens 2R/(1−R). Positive Mischung über die endlichen Masken erhält dieselben Bounds.

Die Diagonale einer affinen Grundoperation A(a,m,n,b) hat höchstens einen festen q-Wert, sofern m≠n, keinen sofern m=n aber a≠b, und ist die Restklassenprojektion q≡b mod n sofern m=n,a=b. Im ersten Fall existiert ein fester Basiswert genau dann, wenn n−m die Zahl a−b teilt; er ist dann q=b+n(a−b)/(n−m). Aus (4)–(6) folgt daher **uniform über alle einzelnen affinen Grundoperationen**

    |ρ_β(A)−τ(A)| ≤ δ_N(β)
       := 2sqrt(βC_N)+4/(I0−2)+2R/(1−R).                 (7)

Für jede feste endliche Linearkombination Σ_j c_j A_j multipliziert sich die Schranke mit Σ_j|c_j|. Der Normabschluss wird durch die Zustandsnorm eins behandelt. Damit ist (1) bewiesen. Dies ist keine Totalvariationskonvergenz auf der gesamten profiniten Mengenalgebra und keine Konvergenz in Zustandsnorm zu einer normalen Dichtematrix.

## 5. Explizite endliche Wahl für eine gewünschte Genauigkeit

Für rationales 0<ε≤1 genügt beispielsweise die folgende vollständig berechenbare positive inverse Temperatur:

    β ≤ min{
      ε²/(36 C_N),
      3/[2κ(12/ε+2)²],
      9ε/[48 d κ N²]
    }.                                                   (8)

Der erste Term beschränkt den Gibbs-Störungsfehler auf ε/3. Aus π>3 und dem zweiten Term folgt 4/(I0−2)≤ε/3. Aus π²>9 und e^(−x)≤1/x folgt beim dritten Term y≤ε/(48d)≤1/2. Daher 2y/(1−y³)≤3y und

    R≤1/[1−3(d−1)y]−1≤ε/(16−ε).

Also 2R/(1−R)≤ε/(8−ε)≤ε/7<ε/3. Die allgemeine Grundanfragen-Genauigkeit ist damit mindestens ε. Die Konstanten sind bewusst konservativ; keine optimale Temperatur oder schnelle Gibbspräparation wird behauptet.

Jedes so gewählte β besitzt endliche Energie. Für N fest gilt im Hochtemperaturlimes

    β Tr(ρ_β H_el) → d/2.

Dies folgt zunächst für die Gitter-Gaußspur durch Poisson und dann für die beschränkt gestörten Eigenwerte durch Min-Max; H−H_el ist beschränkt. Die Energiekosten wachsen somit unbeschränkt, wenn die arithmetische Grenzantwort immer genauer verlangt wird. Eine physische oder effiziente algorithmische Herstellung von ρ_β bleibt eine zusätzliche Aufgabe; seine mathematische Definition ist kein kostenloser Präparationsalgorithmus.

## 6. Stationarität und verbleibende Grenzen

Jedes ρ_β kommutiert mit H. Für jede feste Zeit t und jeden B∈B(H_phys) ist ρ_β(e^(itH)Be^(−itH))=ρ_β(B). Diese Gleichungen bleiben unter schwach*-Subnetzgrenzen erhalten. Banach-Alaoglu liefert einen Häufungspunkt des Zustandsnetzes. Seine Einschränkung auf A_p ist nach (1) τ.

Das korrigiert keine der bisherigen Nichtstationaritätsrechnungen: Diese betrafen die ganz bestimmte **All-low-Schleifenpräparation**, während hier sämtliche zulässigen Materiemasken thermisch beteiligt sind. Ein reiner verschränkter Cap wird durch die stationäre thermische Einschränkung ebenfalls nicht identifiziert.

Erreicht ist die Existenz eines stationären, durch die normale Gibbsfamilie des gegebenen vollständigen endlichen Parents angenäherten arithmetischen Extensionszustands. Offen bleiben:

- die Auswahl dieser Temperatur-/Grenzroute durch die ursprünglichen TFPT-Prinzipien;
- eine eindeutige volle Zustandserweiterung und ein kontrollierter unendlicher Volumen-/Kontinuumslimes;
- die physikalische Gleichsetzung der Normzeit mit der gegebenen Zeitentwicklung;
- Präparations- und Operationskosten, ursprüngliche Cap-Kohärenz und gravitative Raumzeit;
- der zusätzliche globale RH-Positivitäts-/Nullstellensatz und allgemeine Faktorisierungskomplexität.
