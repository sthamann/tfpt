# A3/BCC und Weyl: positiver Kandidat, kein nativer 3D-Auswahlsatz

Unabhängiger, begrenzter Mathematik-/Primärquellencheck, 2026-09-14.
Keine physische Tensorfaktorisierung, Ortsausführung oder TFPT-Dynamik wird
hiermit abgeleitet. Es wurden keine Originalquellen verändert.

## 1. Die richtige Gitteridentität

In einer orthogonalen Realisierung des dreidimensionalen Summe-null-Raums
von A3 sind die vier Gewichte der fundamentalen Darstellung

    w1=(1,1,1)/2, w2=(1,-1,-1)/2,
    w3=(-1,1,-1)/2, w4=(-1,-1,1)/2.

Es gilt wi·wj=delta_ij−1/4. Die zwölf Differenzen wi−wj sind die
FCC-Nachbarvektoren mit zwei Einträgen ±1 und einem Eintrag 0. Die
Wurzellattice ist {x in Z³: sum x gerade}, mit Zellvolumen 2. Ihre duale
Gewichtslattice ist Z³ vereinigt mit [Z³+(1/2,1/2,1/2)], also BCC, mit
Zellvolumen 1/2 und Index 4 gegenüber der Wurzellattice. Der Prüfer
verifiziert die Gram-Matrix, duale Paarung und beide Determinanten exakt.
Die Root-/Weight-Zuordnung wird auch in der ursprünglichen mathematischen
Lattice-Arbeit von [Koca, Koca und Koç](https://squjs.squ.edu.om/squjs/vol19/iss1/1/)
behandelt.

Wichtig: **vier Darstellungsgewichte sind nicht acht Nachbarschritte**.
Die vier wi bilden ein Tetraeder; BCC hat hier die acht nächsten Nachbarn
±wi. Die negativen Gewichte liegen selbstverständlich schon in derselben
Gewichtslattice, sie müssen nicht als neuer physischer Antispinor angesetzt
werden. Aber inverse Ortsverschiebungen und ihre Übergangsmatrizen müssen
in einer Ausführung tatsächlich vorhanden sein. Auch die Identifikation
dieser internen Gewichte mit physischen Ortsverschiebungen ist zusätzlich.
Die drei fundamentalen Gewichte einer Gewichtsbasis wiederum sind nicht
mit diesem Orbit aus vier Gewichten zu verwechseln.

## 2. Was die Primärklassifikation wirklich voraussetzt

[D’Ariano–Erba–Perinotti, arXiv:1708.00826v2](https://arxiv.org/html/1708.00826v2)
klassifizieren in Proposition 5 ausdrücklich QWs auf Cayley-Graphen von
Z^d **für d=1,2,3**, mit Coin C². Isotropie bedeutet dort eine transitive
Automorphismenwirkung auf dem ausgezeichneten Vorwärts-Generatorsatz,
kovariante Übergangsmatrizen und eine passende treue projektive
Coin-Darstellung; zusätzlich müssen verschiedene Richtungen dynamisch
unterscheidbar sein. Für den bereits angenommenen Fall d=3 bleiben die
beiden Weyl-Walks bis auf die genannten diskreten Äquivalenzen. Auch d=1
und d=2 haben zulässige Lösungen. Der Satz wählt nicht d=3 unter allen
Dimensionen aus. Der Artikel beseitigt eine zusätzliche technische
Graphannahme der früheren [Dirac-Ableitung von 2014](https://arxiv.org/abs/1306.1934).

Das source-marked q* verwendet dagegen die fünf Slots der ursprünglichen
Abbildung iota und deren S5-Permutationen, siehe
`verification/v774_arf_spinor_compiler.py:743-822`. Das ist eine interne
Wort-/Markierungswirkung, kein nachgewiesener räumlicher BCC-Isotropievertrag.
Schon eine treue S5-Permutation der vier tetraedrischen Vorwärtsrichtungen
ist unmöglich: 120>24. Auch S5 als Ganzes ist keine treue dreidimensionale
kristallographische Punktgruppe: Eine nichttriviale ganzzahlige Matrix
der Ordnung 5 braucht eine primitive fünfte Einheitswurzel als Eigenwert;
deren Minimalpolynom hat Grad 4 und passt nicht in Dimension 3.
Man kann S5 intern behalten und eine
andere räumliche Isotropie ansetzen; man darf beides nur nicht identifizieren.
Die Wahl eines S4-Untergruppenstabilisators oder einer kleineren räumlichen
Gruppe wäre eine zusätzliche Auswahl, keine Folge von q* allein.

## 3. Ein vollständig kontrollierter kleinster Coin-Kandidat

Auf der skalierten BCC-Lattice L={x in Z³: alle Koordinaten haben gleiche
Parität} setze, mit Pauli-Matrizen X,Y,Z und dimensionslosen Impulsen,

    U(k)=exp(-i kx X) exp(-i ky Y) exp(-i kz Z),
    A_epsilon=(I+epsilon_x X)(I+epsilon_y Y)(I+epsilon_z Z)/8,
    epsilon in {−1,+1}³,
    U(k)=sum_epsilon exp(-i epsilon·k) A_epsilon.

Das ist eine konstruktive, exakt unitäre Ausführung mit acht nichtverschwindenden
Rang-eins-Übergangsmatrizen und Coin-Dimension 2. Der Beweis gilt für ALLE
k: Produktunitarität und unabhängig alle 27 Laurent-Koeffizienten beider
Unitaritätsidentitäten. Die projektiven Coin-Operationen I,X,Y,Z realisieren
die vier räumlichen Doppelvorzeichenwechsel; diese Klein-Vierergruppe ist
transitiv auf den vier Vorwärtsrichtungen mit Produkt epsilon_i=+1.

Für kleine k ist U=I−i k·sigma+O(|k|²). Damit entsteht der Weyl-Operator
als kontrollierter Niederimpulsgrenzfall. Eine physische Geschwindigkeit
benötigt zusätzlich die Wahl von Gitterabstand und Taktzeit. Volle
kontinuierliche Rotationssymmetrie gilt für den linearen Grenzterm, nicht
für das gesamte endliche Gitterprodukt. Insbesondere wird hier keine
räumliche S5-Kovarianz behauptet.

Der konkrete Produktansatz entspricht der bekannten Weyl-Walk-Bauform;
[Bisio et al., Quantum Walks, Weyl Equation and the Lorentz Group](https://wordpress.qubit.it/wp-content/uploads/publications-dariano/10.1007-s10701-017-0086-3.pdf)
geben Produktform, Niederimpulsgrenze und vier fermionische Zweige an.
Die folgenden Werte sind unabhängig berechnet, mit ausdrücklich definierter
lokaler Floquet-Konvention.

Schreibe U=uI−in·sigma. Die reziproke Lattice ist
pi {m in Z³: sum m gerade}; der große Würfel [−pi,pi)^3 enthält vier
primitive Brillouin-Zellen und darf nicht zum unbereinigten Knotenzählen
verwendet werden. Vier inequivalente Knoten sind:

| k/pi | U am Knoten | det Jac(n) | Chirality des zentrierten lokalen Generators |
|---|---:|---:|---:|
| (0,0,0) | +I | +1 | +1 |
| (1,0,0) | −I | −1 | +1 |
| (1/2,1/2,1/2) | −I | +1 | −1 |
| (−1/2,−1/2,−1/2) | +I | −1 | −1 |

Die letzte Spalte definiert U(k0+q)=s[I−i Hloc(q)]+O(q²),
s=±1, und Hloc=(s Jac(n) q)·sigma. Das ist nicht einfach det Jac(n)
ohne Quasienergie-Zentrierung; Literaturkonventionen dürfen nicht gemischt
werden. Bei Quasienergie 0 und bei pi gibt es je ein Paar entgegengesetzter
Chirality. Die Vollständigkeit folgt direkt aus
exp(−ikxX)exp(−ikyY)=±exp(+ikzZ): Die X/Y-Koeffizienten erzwingen
entweder alle drei k_i ganzzahlige Vielfache von pi oder alle drei
halb-ungerade Vielfache von pi. Modulo der reziproken Lattice bleiben
genau zwei Klassen jeder Art. Ein einzelner Weylzweig wird also nicht
ohne zusätzliche Sektorwahl isoliert.

## 4. Zwei kurze Gegenbeispiele gegen zu starke Dimensionsschlüsse

Ein allgemeines hermitesches 2×2-Hamiltonian ist

    H(k)=d0(k)I+d1(k)X+d2(k)Y+d3(k)Z,

aber k darf beliebig viele Komponenten haben. Drei Pauli-Koeffizienten
begrenzen nicht die Dimension ihres Definitionsraums. Zum Beispiel

    H(k1,k2,k3,k4)=k1 X+k2 Y+(k3²+k4²)Z

hat sogar einen isolierten entarteten Punkt bei k=0 im vierdimensionalen
Impulsraum. Der Punkt ist nicht regulär Weyl-artig: Der lineare Rang ist
nur 2; die anderen Richtungen sind quadratisch. Umgekehrt hat
H(kx,ky)=kxX+kyY einen isolierten zweidimensionalen Diracpunkt.

Der KORREKTE bedingte Satz lautet: Wenn d(k) eine reguläre Abbildung nach
R³ mit Rang 3 am Nullpunkt ist, besitzt die Nullmenge lokal Dimension
d_space−3. Ein isolierter REGULÄRER Weylpunkt setzt dann d_space=3 voraus.
Alternativ erzwingen drei Pauli-Matrizen bei einem in jeder Richtung
nichtentarteten linearen isotropen Clifford-Symbol d_space≤3; dabei ist
genau diese lineare Nichtentartung die zusätzliche Prämisse. Ein
Weylpunkt heißt bereits per Definition ein solcher dreidimensionaler
Monopol-/Kegelpunkt. Seine Bezeichnung liefert keine unabhängige native
Dimensionsableitung. Die vierdimensionale Gegenprobe beansprucht nicht,
die stärkeren Isotropieannahmen der QW-Klassifikation zu erfüllen.

## 5. Ein einziger D erzwingt keinen gemeinsamen Lichtkegel

Bereits

    D(k)=diag(v1 k·sigma, v2 k·sigma), v1,v2>0,

ist EIN lokaler, hermitescher, homogener und rotationskovarianter Operator.
Sein charakteristisches Polynom lautet exakt

    det(omega I−D)=(omega²−v1²|k|²)(omega²−v2²|k|²).

v1=1, v2=2 gibt unterschiedliche Kegel bei demselben gemeinsamen Takt.
Das Verhältnis 2 ist durch eine gemeinsame Zeiteinheit nicht entfernbar.
Auch strikt diskrete lokale Ausführungen können verschiedene Geschwindigkeiten
haben: diag(U(k),U(k)²) nutzt denselben BCC-Ortsraum und Takt, mit endlicher
Reichweite und linearen Geschwindigkeiten 1 und 2. Gleiche Kegel folgen
erst aus einem gemeinsamen, entsprechend normierten Hauptsymbol oder
einer Sektoren mischenden Symmetrie, die dessen Koeffizienten gleichsetzt.
Dass man alle Sektoren in dieselbe Matrix schreibt, ist kein solcher Beweis.

## Prüfstatus und engste offene Kante

`check_weyl.py`: 149 exakte Guards, normal und unter `python -OO` identisch;
keine schwebenden Residuen als Beweise. Drei falsifizierte Mutationen:
inverse Schritte entfernen; nur einen Knoten behalten; beide freien
Geschwindigkeiten unberechtigt gleichsetzen. Größte verwendete Matrix: 4×4.

Der konstruktive nächste Vertrag wäre eine source-native Zuordnung von
konkreten TFPT-Operationen zu den acht A_epsilon und den Ortsverschiebungen,
einschließlich des Coin-C2-Trägers und der räumlichen Isotropiewirkung.
Ohne diese Kante bleibt der Walk ein konsistentes bedingtes Modell und
keine aus TFPT ausgewählte Raumzeit. Weder native 3D noch universelle
Lichtkegel noch eine einzelne Chirality sind durch die geprüften Kurzargumente
geschlossen.
