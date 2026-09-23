# Der zentrale Herkunftstest für die nativen Fermionen und die lokalen Randfelder

**Contract:** `UR.SOURCE.FAMILY_INTERTWINER.01`  
**Verdikt:** `PARTIAL; FIXED_SOURCE_TO_COMMON_ODD_EDGE_IDENTIFICATION_REFUTED`.

**Ergebnis:** Im unveränderten nativen 64-CAR/60-CCR-Fockmodell gibt es unter derselben vollständigen Spin(10)×SU(4)-Wirkung keinen Operator, der eines der ungeraden lokalen Felder des fixierten gemeinsamen T(D8)-Randwörterbuchs darstellen kann. Dies gilt auch für nichtlineare Zusammensetzungen. Ein einzelnes zentrales Gruppenelement entscheidet die Frage bereits vor jeder Kopplungs- oder RG-Rechnung.

Der enge Geltungsbereich ist entscheidend: Es geht um diese vorhandene Fockdarstellung und dieses gemeinsame T-Wörterbuch. Eine andere quellenselektierte Gruppenhebung, zusätzliche geladene oder verdrillte Sektoren oder ein anderes physisches Feldwörterbuch werden nicht ausgeschlossen. Das ist kein allgemeiner Unmöglichkeitssatz über TFPT.

## 1. Die tatsächliche Gruppenwirkung

Die Quellgewichte ergeben

\[
F=(\overline{16},\bar4),\qquad B=(10,6).
\]

Der signierte native Tensor `W:Lambda²F→B` ist 60×2016, besitzt 480 Nichtnullkanten und erfüllt `WW^T=8I60`. Auf allen acht Paaren jeder seiner 60 Zeilen wird dasselbe wirkliche Bosongewicht erhalten; der neue Prüfer rekonstruiert diese Gewichte aus den Original-CAR-Formeln.

Wähle die Zentralgeneratoren so, wie sie durch die festgelegten verdoppelten D5-/D3-Gewichte kodiert werden:

| Darstellung | z10 | z4 | diagonales Element zeta=(z10,z4) |
|---|---:|---:|---:|
| natives F=(bar16,bar4) | i | -i | +1 |
| natives B=(10,6) | -1 | -1 | +1 |
| lokaler c-Zweig (bar16,4) | i | i | -1 |
| lokaler c-Zweig (16,bar4) | -i | -i | -1 |

Die inverse Wahl beider Generatoren ändert die Schlussfolgerung nicht. Die zentrale Exponentenprüfung verwendet die wirklichen Quellgewichte, nicht nur Darstellungsnamen.

## 2. Der Ausschluss gilt für die ganze Operatoralgebra

Auf jedem nativen Erzeugungsoperator f† und b† wirkt zeta mit +1; auf ihren Adjungierten ebenso. Seine Fockhebung ist daher die Identität bis auf eine irrelevante gemeinsame Vakuumphase. Für **jeden** Operator O im selben Fockraum gilt

\[
\alpha_{\zeta}^{\rm native}(O)=O.
\]

Das gilt nicht bloß bis zu einem getesteten Polynomgrad. Es gilt für die vollständige Operatoralgebra, ihre Abschlüsse und zulässige unbeschränkte Operatoren mit entsprechend transformiertem Definitionsbereich. Produkte, Paarmittelwerte, Wechselwirkung, Zeitentwicklung oder eine andere Zustandswahl können ein identisch wirkendes Gruppenelement nicht in einen nichttrivialen Operatorautomorphismus verwandeln.

Ein c-Feld psi der geforderten Zielgruppe erfüllt dagegen `alpha_zeta(psi)=-psi`. Für eine equivarianten Abbildung iota müsste gelten

\[
\iota(\psi)=\alpha_\zeta^{\rm native}(\iota(\psi))
=\iota(\alpha_\zeta^{\rm edge}(\psi))=-\iota(\psi),
\]

also `iota(psi)=0`. Damit scheitert ein injektiver graduierter Feldtransfer bereits an der Gruppenwirkung. Eine höhergradige native Zusammensetzung rettet diesen unveränderten Kandidaten nicht. Auch ein global antilinearer Transfer hilft bei der reellen Phase -1 nicht.

## 3. Der volle gemeinsame Rand macht die Grenze noch deutlicher

Für jeden integralen Randvektor x ist seine gemeinsame T-Projektion p durch

\[
2p=2x_{1:8}-(x_9+x_{10})a,
\quad a=(1,1,1,-1,-1,-1,-1,-1)
\]

gegeben. Wegen `sum(a)=-2` folgt als polynomiale Identität

\[
2\sum p_i=2\sum_{j=1}^{10}x_j.
\]

Das diagonale Zentrum wirkt daher auf dem zugehörigen Vertex mit

\[
i^{2\sum p_i}=(-1)^{\sum_jx_j}=(-1)^{B(x,x)}.
\]

Die letzte Gleichheit gilt modulo zwei für K=diag(1^9,-1). Im **fixierten gemeinsamen T-Wörterbuch** ist diese Zentrumwirkung genau die geerbte Fermionparität: Klassen 0,s tragen +1, Klassen v,c tragen -1. Die native Quelle besitzt dagegen durchaus ungerade CAR-Operatoren, aber auf ihnen wirkt dieses diagonale Gruppenelement mit +1. Es fehlen also nicht einfach Fermionen; es fehlen Fermionen mit derselben Verknüpfung von Gruppenwirkung und Parität.

Dies betrifft nicht automatisch das andere native F_aux-Wörterbuch. Sein Cartantransport enthält zusätzliche n-Anteile und ist auf allgemeinen Randfeldern verschieden. Ein Wechsel zurück zu F_aux oder eine zusätzliche geladene Paarstruktur müsste aus der ursprünglichen Quelle samt Ladung, Zustand und Zeit begründet werden. Er darf nicht stillschweigend in die gemeinsame T-Rechnung eingesetzt werden.

## 4. Warum die einfache Familiendualisierung schon vorher scheitert

Für den Übergang `(bar16,bar4)→(bar16,4)` gilt bei unveränderter voller Produktgruppenwirkung:

- Jeder **lineare** Intertwiner ist wegen des SU(4)-Zentrums null: Quelle -i, Ziel +i. Das exakte System der 15 SU(4)-Generatoren hat Rang 16 bei 16 Unbekannten.
- Jeder **globale antilineare** Intertwiner ist wegen des Spin(10)-Zentrums null: Beide bar16-Faktoren tragen dieselbe nichtreelle Phase i; Antilinearität konjugiert sie zu -i.
- Ein nur teilweise antilinearer Ausdruck `I16 tensor K4` ist über dem komplexen Tensorprodukt nicht wohldefiniert. Die beiden gleichen Vektoren `(i s) tensor f = s tensor (i f)` hätten entgegengesetzte Bilder.

Die Koeffizientenkonjugation auf dem isolierten Familienraum ist korrekt. Sie lässt sich jedoch nicht als unveränderter Operator auf den gesamten komplexen Träger übertragen. Ebenso beweist Gleichheit reeller Cartangewichte keine identische Wirkung der komplexen U(1)-Gruppenphasen.

Diese Korrektur wurde unabhängig in `INDEPENDENT_GROUP_REVIEW.md` bestätigt. Der stärkere Gesamtalgebra-Satz aus Abschnitt2 wurde anschließend separat durch das universelle Zentrumargument gewonnen; er ist keine vom unabhängigen Review bereits geprüfte Aussage.

## 5. Was die Hodge-Tensoren und Clocks tatsächlich liefern

Eine äußere Konjugation der SU(4)-Gruppenwirkung kann einen **anders deklarierten Zielträger** definieren. Auf der reellen Sechs ist die Hodge-Matrix H6 wohldefiniert. Mit `HB=I10 tensor H6` erzeugt sie die formalen Arrays

```
W_D=HB W,
J_D=J (HB^T tensor I64),
C3_D=(HB tensor I64) C3.
```

Ihre Gram- und Komplexidentitäten bleiben exakt (`W_D W_D^T=8I`, `J_D J_D^T=15I`, `J_D C3_D=0`). Die drei transformierten Arrays sind in den fixierten Koordinaten jeweils support-disjunkt vom ursprünglichen Array. Ein Koordinatentausch erhält solche Identitäten ohnehin; dies beweist keine neue physische Kopplung und keinen Gruppenintertwiner bei fester Wirkung. Die native simultane `BAR` ist Spin10-Opposition tensor H6 und ist nicht HB allein.

Auch die wirklichen E8-Compiler-Clocks besitzen nicht die benötigte Restriktion:

| Clock | in FW64 | in ganzzahlige D8-Wurzeln | in andere s-Halbgewichte |
|---|---:|---:|---:|
| C | 21 | 28 | 15 |
| J | 32 | 0 | 32 |

Alle 64 familienkonjugierten c-Gewichte liegen außerhalb des ursprünglichen E8-Wurzelsystems. Der gemeinsame C/J-Abschluss des markierten 48er-Ausschnitts umfasst 240 Wurzelrichtungen. Ein interner Spin10×SU4-kovarianter Lift des W-Tensors ist deshalb nicht automatisch derselbe Operator wie diese vollständigen Compiler-Clocks.

## 6. Konsequenz für die Gesamtherleitung

Der Versuch, das unveränderte native W-Modell auf die neuen gemeinsamen ungeraden T-Randfelder abzubilden, ist unter dem festgehaltenen Gruppendictionary ausgeschlossen. Es wäre sachlich falsch, jetzt weitere native Polynomgrade, Kopplungswerte oder Zustände nach diesem Feld zu durchsuchen: Das zentrale Zeichen bleibt dabei unverändert.

Der nächste erforderliche Herkunftsnachweis ist eine ursprüngliche Struktur, die das fehlende zentrale Zeichen trägt — etwa ein bereits begründeter geladener/twisted Sektor oder eine explizite quellenselektierte andere Gruppenhebung/Feldzuordnung. Diese Struktur muss tatsächlich in der Quelle vorhanden sein; ihre freie Ergänzung wäre ein neuer Modellvertrag. Eine bloß reelle diskrete Untergruppe kann die Unterscheidung verdecken; dann wurde die verlangte vollständige Gruppenwirkung geändert und dies muss ausgewiesen werden.

Offen bleiben die Auswahl des Energiepunkts Vc, der beiden normierten n/z-Kopplungen, dieselbe physische Zeit, die vollständige IR-Sektorregel und der vierdimensionale Anschluss. Kein physikalisches Gate wird geschlossen.

## 7. Gezielter Folgetest: die ursprünglichen Clifford-Matrizen vor der Projektion

Der stärkere Zentrumtest wurde weiterverfolgt, statt nur als offene Grenze stehenzubleiben. Der Quellcode `_gamma_pairs(3)` konstruiert tatsächlich sechs 8×8-Clifford-Matrizen gamma_a und projiziert anschließend ihre geraden Produkte auf den vierdimensionalen geraden Familienraum. Vor dieser Projektion existiert die bekannte, exakt kovariante **Tensorabbildung**

\[
6\otimes\bar4\longrightarrow4,\qquad
M_a=P_{\rm odd}\gamma_aP_{\rm even}.
\]

Für alle 15 Familiengeneratoren und alle 6 Komponenten gilt exakt

\[
X^{\rm odd}_{jk}M_l-M_lX^{\rm even}_{jk}
=2(\delta_{kl}M_j-\delta_{jl}M_k).
\]

Das ist eine komplex-lineare Abbildung mit einem **zusätzlichen Vektorbein**, keine verbotene partielle Konjugation. Die Sechs trägt gerade das fehlende zentrale Minuszeichen. Der konkrete Kleinsttest der Quelle liefert jedoch gleichzeitig

\[
P_{\rm even}\gamma_aP_{\rm even}=0
\]

für alle sechs Matrizen. Der implementierte native Familiengenerator exportiert die geraden Bivektoren; das gegenüberliegende Vierer-Modul und diese sechs Übergänge sind kein Feld-/Hamiltonoperator des ausgeführten 64-CAR/60-CCR-Modells.

Das unterscheidet einen im Rechenaufbau vorhandenen Hilfsraum von einer zusätzlichen physikalischen Teilchensorte. Die Hilfsraum-Majoranas sind dort ungerade; die native Fockquelle hat zusätzlich die 64 **als Fermionoperatoren** eingesetzten Moden. Eine einfache Multiplikation zweier ungerader physischer Operatoren wäre gerade. Auch die gewünschte Fermionparität folgt deshalb nicht aus dem vorgefundenen Matrixbaustein allein.

Der Folgetest liefert somit einen konkreten Ort der fehlenden Herkunft: **der Übergang von der unprojizierten Clifford-Quelle zur tatsächlich ausgeführten Feldalgebra**, einschließlich des Vektorbeins, der Graduierung und der Zeitentwicklung. Die 90 Kovarianzgleichungen und der Nullbefund nach Projektion sind nachgerechnet; kein zusätzliches Feld und kein neuer Hamiltonterm wurden in die Quelle eingesetzt.

## 8. Neuer Abgleich mit der anderen Lane: Zentrumzeichen ist Eichladungsparität

Der inzwischen registrierte Vertrag `UR.SOURCE.ROTOR_GAUSS.01` bestimmt unter seinen ausdrücklich zusätzlichen Randannahmen die notwendige primitive Kandidaten-Eichladung `g=±K n`. Seine zeitbezogene Ergänzung prüft die Ladungen+1/-1 der beiden lokalen c-Feldfamilien. Beide Originalzertifikate und ihre Quellenmanifeste wurden hier unverändert geprüft; ihre73 beziehungsweise17 Kontrollen werden nicht als neue eigene Läufe ausgegeben.

Die zusätzliche gemeinsame Schlussfolgerung gilt für **jeden** x in Gamma:

\[
g\cdot x=\sum_jx_j-2\sum_{j=4}^{9}x_j-4x_{10},
\]

also

\[
\exp(i\pi g\cdot x)=(-1)^{\sum_jx_j}
=\text{diagonales Zentrum auf }V_x
=(-1)^{B(x,x)}.
\]

Die beiden zuvor getrennt wirkenden Probleme — fehlendes zentrales Zeichen der Quelle und fehlender geladener Randsektor — treffen sich damit in genau derselben notwendigen Struktur. Das ist eine Korrelation der **fixierten Zielwörterbücher**, keine bereits realisierte Eichladung im nativen Fockmodell. Die Kandidaten-Eichung selbst und ihre Feldalgebra bleiben herzuleiten.

Zugleich gilt `g.n=0`, `g.z=2`: Eine tatsächliche Eichung dieser Ladung würde den nackten kritischen z-Term verbieten. Ein gemeinsamer Ising-Punkt mit beiden nackten Termen ist unter dieser zusätzlichen Voraussetzung daher nicht unverändert zulässig. Ein ladungskompensierender Faktor wäre eine weitere herzuleitende Quellstruktur. Die neue Korrelation liefert somit eine präzise gemeinsame Bedingung, keine automatische Gleichsetzung aller bisherigen Hilfsmodelle.

## Reproduktion

`python3 -B check_family_intertwiner.py` und `python3 -B -OO check_family_intertwiner.py` müssen dasselbe Zertifikat liefern. Die Rechnungen rekonstruieren die Originaltensoren, prüfen ihre zentralen Gewichte und die C/J-Permutationen und zertifizieren die universelle Randparitätsidentität. Der allgemeine Operatorausschluss folgt aus der angegebenen Equivarianzgleichung, nicht aus endlichem Sampling.
