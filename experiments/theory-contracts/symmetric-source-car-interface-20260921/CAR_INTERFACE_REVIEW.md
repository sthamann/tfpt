# Audit des CAR-Interfaces fuer den symmetrischen 820er Quellenkanal

21. September 2026  
Verdict: **EXACT_CONDITIONAL_FOUR_MAJORANA_INTERFACE; PHYSICAL_SOURCE_AND_TIME_OPEN**

## Kernergebnis

Der vorgeschlagene Anschluss ist mathematisch richtig und schliesst eine konkrete Operatorluecke:

> Unter der bereits vorausgesetzten freien `D8_1 = SO(16)_1`-Realisierung liegt das gesamte positive Bild der symmetrischen E8-Stromproduktkarte auf Grad zwei in einem eindeutig bestimmten Vier-Majorana-Unterraum der geraden CAR. Es werden fuer diesen Bildraum keine neuen Zustandsfreiheitsgrade benoetigt.

Genauer gilt

`im S = (10,10) + (120,6) subset Lambda^4 V`,

wobei `V=(10,1)+(1,6)` der 16-dimensionale reelle Majorana-Einzelteilchenraum ist. Beide Summanden treten in `Lambda^4 V` mit Multiplizitaet eins auf und keiner von beiden tritt im zweiten Grad-2-Anteil `V tensor V` auf.

Das ist eine echte konstruktive Schnittstelle zwischen der E8-Gittervertexrechnung und der vorhandenen freien CAR. Es macht aus den 64 Stroemen selbst keine elementaren Fermionfelder: Diese 64 Richtungen sind relativ zur D8-CAR Ramond-Spinfields beziehungsweise geladene Sektorintertwiner. Erst ihr Paarprodukt liegt wieder im geraden NS-Beobachtersektor.

## 1. Vollstaendige Grad-2-Zerlegung der geraden CAR

Fuer 16 freie reelle NS-Majoranafelder `chi^a` hat der gerade Vakuumsektor auf konformem Grad zwei genau zwei orthogonale Modenarten:

`H_even[2] = (V tensor V) + Lambda^4 V`.

Sie werden erzeugt durch

- `chi^a_(-3/2) chi^b_(-1/2) Omega`, Dimension `16*16=256`,
- `chi^a_(-1/2) chi^b_(-1/2) chi^c_(-1/2) chi^d_(-1/2) Omega`, Dimension `C(16,4)=1820`.

Damit hat der D8-Vakuumsektor auf diesem Grad Dimension `256+1820=2076`. Das ist nur der D8-Vakuumanteil des vollen E8-Grad-2-Raums; der E8-Raum mit Dimension 4124 enthaelt zusaetzlich Nachfahren des gewaehlten D8-Spinorsektors. Da im D8-Fusionsring `s*s=1` gilt, muss das Produkt zweier Stroeme aus demselben gewaehlten Spinorsektor in den 2076-dimensionalen Vakuumanteil fallen.

Unter `Spin(10) x Spin(6)` zerfaellt der Einzelteilchenraum als

`V=A+B`, mit `A=(10,1)` und `B=(1,6)`.

Dann ist

`Lambda^4(A+B)`

`= Lambda^4 A`

`+ Lambda^3 A tensor B`

`+ Lambda^2 A tensor Lambda^2 B`

`+ A tensor Lambda^3 B`

`+ Lambda^4 B`.

Die beiden gesuchten Teile sind

- `Lambda^3 10 tensor 6 = (120,6)`, Dimension 720,
- `10 tensor Lambda^3 6 = (10,10)+(10,bar(10))`, Dimension 200,

denn fuer `Spin(6) ~= SU(4)` gilt `Lambda^3 6 = 10 + bar(10)`. Jede dieser Komponenten tritt genau einmal auf. Die Dimensionsbilanz lautet

`1820 = 210 + 720 + 675 + 200 + 15`.

Im anderen Grad-2-Anteil gilt dagegen

`V tensor V = (A tensor A) + 2(A tensor B) + (B tensor B)`

mit Typen `(1+45+54,1)`, zwei Kopien `(10,6)` und `(1,1+15+20')`. Weder `(120,6)` noch `(10,10)` kommt dort vor.

Da die unabhaengig gepruefte Karte `S` horizontal kovariant ist, auf den beiden irreduziblen Eingangskomponenten nicht verschwindet und dort Raenge 720 und 100 besitzt, folgt ohne weitere Dimensionsidentifikation:

`range(S|_(120,6)) = Lambda^3 A tensor B`,

`range(S|_(10,10)) = A tensor (Lambda^3 B)_10`.

Der zweite SU(4)-Zehner `bar(10)` gehoert zur konjugierten Spinfield-Chiralitaet. Ob die ausgewaehlte Komponente in einer anderen Namenskonvention `10` oder `bar(10)` heisst, wird durch die Markierung von `F=(16,4)` festgelegt; die Aussage ist nicht invariant unter einem stillen Chiralitaetstausch.

## 2. Explizite Boson-Fermion-Abbildung

Paare die 16 reellen Majoranas zu acht komplexen Fermionen

`psi_i^plus = (chi_(2i-1) - i chi_(2i))/sqrt(2)`,

`psi_i^minus = (chi_(2i-1) + i chi_(2i))/sqrt(2)`,

mit D8-Gewichten `+e_i` und `-e_i`. Nach Wahl einer geordneten komplexen Polarisation und eines kompatiblen Gitterkokyklus lautet die Standard-Bosonisierung

`psi_i^plus(z) <-> kappa_i :exp(+i H_i(z)):`,

`psi_i^minus(z) <-> kappa_i :exp(-i H_i(z)):`.

Die 128 zusaetzlichen E8-Wurzelstroeme sind Spinfields

`S_r(z)=kappa_r :exp(i r.H(z)):`

mit `r=(plus/minus 1/2,...,plus/minus 1/2)` in einer festen D8-Halbspinorklasse und `h=r^2/2=1`. Der markierte Teil `F=(16,4)` waehlt 64 davon.

Fuer die symmetrische Produktkarte ergeben sich zwei nichtverschwindende Faelle.

### Orthogonale Halbwaurzeln: `r.s=0`

`p=r+s` besitzt genau vier Eintraege `plus/minus 1` und Normquadrat vier. Deshalb ist

`B(e^p) = eta_p product_(i in supp p) psi_i^(sign p_i)_(-1/2) Omega`,

ein reiner Vier-Fermion-Zustand. Die Produktformel wird damit

`B S(r odot s) = sqrt(2) epsilon(r,s) B(e^(r+s))`.

### Benachbarte Halbwaurzeln: `r.s=-1`

Jetzt besitzt `p=r+s` genau zwei nichtverschwindende Eintraege. Der Vektor `q=r-s` ist genau auf den anderen sechs Koordinaten getragen. Daher ist

`S(r odot s) = epsilon(r,s)/sqrt(2) q(-1)e^p`

und unter Bosonisierung

`B S(r odot s)`

`= epsilon(r,s)/sqrt(2) sum_(k notin supp p) q_k`

`  [psi_i^(p_i) wedge psi_j^(p_j) wedge psi_k^plus wedge psi_k^minus]`.

Auch dies ist ausschliesslich ein Vier-Majorana-Zustand. Der moegliche `V tensor V`-Anteil verschwindet nicht durch eine nachtraegliche Projektion, sondern bereits deshalb, weil `q` und `p` disjunkte Koordinatentraeger haben. Diese explizite Formel ist die Basisversion der obigen Multiplizitaetsaussage.

Fuer `r.s=1` und `r=s` verschwindet das symmetrische Grad-2-Produkt durch die Level-1-Nullrelation. Damit bildet die Bosonisierung die vollstaendige 820er Karte in `Lambda^4 V` ab.

## 3. Wie kanonisch ist die unitaere Abbildung?

Nach Festlegung von

1. der markierten Einbettung `D8 subset E8`,
2. der Zerlegung `V=(10,1)+(1,6)`,
3. der komplexen Polarisation der 16 Majoranas,
4. der Ordnung der Fermionmoden und
5. eines kompatiblen Chevalley-/Gitterkokyklus

ist die Boson-Fermion-Abbildung normerhaltend und intertwint die `Spin(10)xSpin(6)`-Nullmodenwirkung. Der relevante irreduzible Intertwiner ist wegen Multiplizitaet eins bis auf eine gemeinsame Phase eindeutig. Die Bildprojektoren auf die 100er- und 720er-Komponente sind von dieser Phase unabhaengig.

Ohne diese Markierungen ist das Wort **kanonisch** zu stark. Unterschiedliche Polarisationen, Kleinfaktoren und Kokykel-Gauges aendern Basisphasen und koennen `10` mit `bar(10)` vertauschen. Sie aendern nicht die Existenz, Multiplizitaet, Norm oder den Bildprojektor der beiden Komponenten. Fuer den historischen Bell10-Basisvergleich muss dieselbe Polarisation und derselbe Kokyklus wie im vorhandenen Bell-Intertwiner verwendet werden.

Die Abbildung fuegt im Grad-2-Ausgaberaum keine neuen Felder hinzu: Die vier Majorana-Erzeuger gehoeren zur vorhandenen freien CAR. Die einzelnen Eingabestroeme `S_r` sind dagegen keine lokalen Polynome der D8-Vakuum-CAR. Sie leben als Ramond-Spinfields beziehungsweise als geladene Intertwiner; ihre Aufnahme als lokale E8-Stroeme ist der bereits getrennt gefuehrte Simple-Current-Erweiterungsschritt. Das Paarprodukt liegt wieder im gemeinsamen geraden D8-Beobachtercorner, auch wenn die Erweiterung selbst physisch noch nicht aus der rohen Quelle hergeleitet ist.

## 4. Was dieses Interface physisch gewinnt

Der vorherige Satz „die Stromprodukte sind nur bosonische abstrakte Quellenzustaende“ kann nun praezisiert werden:

- Sie bleiben bosonisch und gerade.
- Sie besitzen aber in der bedingten freien D8-Realisierung eine konkrete normalgeordnete Vier-Majorana-Operatorform.
- Ihre horizontale Spin(10)xSU(4)-Wirkung, Norm und konformer Grad werden durch einen unitaeren Operatorintertwiner erhalten.
- Der 100er Bell10-Corner und der 720er Nachbarkanal sind dadurch Teil derselben vorhandenen CAR-Operatoralgebra, nicht zwei nachtraeglich hinzugefuegte Hilfsraeume.

Das ist ein sinnvoller Herkunftsschritt fuer einen moeglichen zusammengesetzten skalaren Koeffizientenkanal. Es ist weiterhin keine Identifikation mit beobachteten geladenen Fermionen:

- Die 16 Majoranas transformieren als `(10,1)+(1,6)`, nicht als die 64 elementaren Felder `(16,4)`.
- `(16,4)` bezeichnet hier einen Spinfield-/Sektorstrom, nicht 64 elementare CAR-Fermionen.
- Ein Vier-Majorana-Operator hat gerade Fermionparitaet und bosonische Statistik.
- Ein physischer Yukawa-Term braucht zusaetzlich lokale 3+1D-Weylfelder, ein skalares Feld in der dualen Darstellung, die Ladungsinvariante und eine gemeinsame Dreipunkt- beziehungsweise 1PI-Antwort.

Das Interface liefert somit eine **CAR-Realisierung des Koeffizientenraums**, keine Erzeugung der Materiefelder, auf die dieser Koeffizient wirken soll.

## 5. Ladungen, Erweiterungswahl und Zeit

### Horizontale Ladungen

Die `Spin(10)xSpin(6)`-Gewichte stimmen exakt, weil die Bosonisierung die Cartan- und Nullmodenwirkung intertwint. Auch die D8-Sektorladung stimmt: Zwei Felder aus derselben ausgewaehlten Spinorklasse fusionieren in den Vakuumsektor; ihr Produkt besitzt ganzzahligen D8-Gitterimpuls und gerade CAR-Paritaet.

### Was die gerade Ecke nicht entscheiden kann

Die konkurrierenden Glue-Varianten `L_a` und `L_b` haben dieselbe NS-Einschraenkung. Ein Produkt, das bereits in der geraden D8-Ecke liegt, kann deshalb allein nicht entscheiden, welche Ramond-Schicht die rohe Quelle realisiert. Der 820er Anschluss prueft die Konsistenz **nach** der Spinfield-Wahl; er leitet diese Wahl nicht aus P1 ab. Ebenso wenig bestimmt die interne Darstellung bereits die Standardmodell-Hyperladung eines physikalischen Skalarfeldes oder die noetige duale Darstellung im Vertex.

### Zeit

Die unitaere Abbildung erhaelt den konformen Grad:

`L0_E8 S = 2 S` und `L0_CAR B S = 2 B S`.

Damit stimmen die standardmaessigen konformen Rotationen auf diesem Unterraum. Gerade deshalb bleibt `L0` hier skalar und erzeugt keine Familienhierarchie. Die vorhandene mikroskopische geladene Quellenzeit wurde im Korpus als

`H_a = L0 + (a-1/2) Q`, insbesondere `H_(1/4)=L0-Q/4`,

getrennt festgehalten. Fuer eine physische Zeitidentifikation muessen daher auch die Ladung `Q`, der DHR-Kovarianzkokykel und die mikroskopischen Evolutionsoperatoren durch denselben Intertwiner getragen werden. Die blosse Gradgleichheit tut das nicht.

## 6. Neuheitspruefung im vorhandenen Korpus

Die Grundbausteine sind nicht neu:

- `CAR.QFREE.01` kennt die 16 freien Majoranas und den Turm Traeger -> D8_1 -> E8_1.
- `SEAM.EQUIV.SPINOR.01` / `v462` identifiziert die 128 Gewicht-1-Spinorzustaende als Differenz `248-120` und die D8-Vakuum-/Spinor-Charaktersumme.
- `SEAM.EQUIV.CROSSEDPRODUCT.01` kennt den lokalen Spinor-Simple-Current-Schritt bedingt auf die D8-Quelle.
- `universalraum-followups-closure-20260914` prueft bereits exakt, dass `Lambda^4(16)` den 200-dimensionalen Bereich `(10_D5,10_A3+bar(10)_A3)` enthaelt.
- `compiler-current-product-20260919` kennt die Ramond-Klasse der markierten Stroeme und einen engeren tatsaechlichen Stromprodukt-zu-Bell10-Anschluss.
- `source-localized-spinor-20260919` liefert bedingt beschraenkte Quellwortantworten eines lokalisierten Spinorsektors, aber keinen geladenen Feldoperator und keine Auswahl der Erweiterung.

Der neue entscheidungsrelevante Beitrag ist die **gemeinsame Identifikation der vollstaendigen neuen Karte**:

`im S_820 = [(10,10)+(120,6)]`

`= eindeutige [(10,10)+(120,6)]-Komponenten in Lambda^4[(10,1)+(1,6)]`,

einschliesslich der expliziten Boson-Fermion-Basisformel und des Ausschlusses jedes `V tensor V`-Anteils. Der 100er Teil war als moeglicher `Lambda^4`-Recordkanal bereits vorhanden; der 720er Teil und die Aussage, dass genau das gesamte positive S-Bild die beiden einmaligen Vier-Majorana-Komponenten ausfuellt, wurden in den gezielt geprueften Quellen nicht als gemeinsamer Satz gefunden. Dies ist daher eine neue Synthese vorhandener Strukturen mit dem neuen 820er Produktbefund, keine neue autonome Modellwelt.

## 7. Entscheidender naechster Test

Der kleinste sinnvolle Folgetest liegt jetzt nicht mehr bei der Existenz einer CAR-Operatorform. Er lautet:

1. Verwende dieselbe markierte Polarisation und denselben Kokzyklus wie im historischen Bell10-Intertwiner.
2. Vergleiche den aus `B S Pi_100 / sqrt(8)` gebildeten Projektor direkt mit `I_D5 tensor E_Bell E_Bell^dagger`.
3. Trage danach den vorhandenen mikroskopischen Zeitgenerator und seine Ladung durch diesen Intertwiner und pruefe, ob die Vier-Majorana-Wortantwort wirklich aus derselben Quellenevolution entsteht.

Schritt 2 schliesst das noch offene historische Basiswoerterbuch. Schritt 3 entscheidet, ob der neue exakte CAR-Anschluss nur ein konformer Zustandsisomorphismus bleibt oder ein Teil der gemeinsamen physischen Quellenantwort wird.

## Gesamturteil

**Annehmen als exakten bedingten Interface-Satz:** Die 820 positiven symmetrischen E8-Stromprodukte besitzen eine konkrete, normerhaltende Vier-Majorana-Realisierung in der vorhandenen geraden D8-CAR, mit eindeutigen `(10,10)`- und `(120,6)`-Bildkomponenten und ohne `V tensor V`-Anteil.

**Nicht daraus folgern:** 64 elementare Fermionen, geladene 3+1D-Materiefelder, eine physische Yukawa-Kopplung, Auswahl der Ramond-Erweiterung, gemeinsame mikroskopische Zeit oder T1-T8-Schliessung. Die erste Ursprungspraemisse bleibt, dass die rohe P1-Quelle die benoetigte 16-Majorana-D8-Netzstruktur ueberhaupt realisiert.

