# Quellenadapter zwischen affiner E8-Antwort und RR/W-Dynamik

**Stand:** 21. September 2026  
**Verdict:** `PARTIAL_WITH_EXACT_DIRECT_TIME_OBSTRUCTION`

## Kernaussage

Die ursprüngliche affine E8-Vakuumantwort liefert mehr als nur die Existenz
eines Tensors: Sie bestimmt aus Strom-Gram und Stromklammer eine normierte
E8-Intertwiner-Richtung. Im markierten `D5 x A3`-Typ ist dies die Richtung

\[
\beta:\Lambda^2(\overline{16},\overline4)\longrightarrow(10,6),
\]

also darstellungstheoretisch genau der Typ des nativen Tensors

\[
W:\Lambda^2\mathbb C^{64}\longrightarrow\mathbb C^{60}.
\]

Der bereits explizit zertifizierte Ward/OPE-Kubik testet allerdings nur den
alten Dreifamilien-Ausschnitt `16 x 3` innerhalb der E6-A2-Zerlegung; sein
kompaktes Adjungiertes liefert den zum nativen `W` passenden konjugierten
charged Typ. Die
volle 64-zu-60-Koeffiziententabelle ist in diesem Contract nicht gegen das
archivierte `W` verglichen. Auf Darstellungsebene ist die Richtung eindeutig,
aber die vollständige basis- und kokzyklusgenaue Gleichheit bleibt ein kleiner
endlicher Anschlusscheck.

Die dynamischen Zieljets

\[
\Omega=2\kappa I_{60},\qquad
C_1=\frac{\kappa}{\sqrt2}W,\qquad
V=\frac\kappa4W^\dagger W
\]

folgen daraus nicht. Zwei direkte Identifikationen lassen sich sogar exakt
ausschließen:

1. Die affine Grad-/Konformalzeit erhält den Stromgrad und hat daher keinen
   Übergangsblock zwischen einem Grad-zwei-Stromprodukt und einem
   Grad-eins-Strom. Ihr entsprechender `C1`-Block ist null, während der
   RR/W-Kandidat `C1 != 0` verlangt.
2. Die stärkere globale lineare RR-Feldgleichung für
   `a_A=P_A/sqrt(8)` und `b_A` scheitert am operatorwertigen Kommutator
   `[a_A,a_B^dagger]`. Auf einem vollständig gefüllten Fermionzustand hat ein
   bestimmtes Übergangsmatrixelement das Vorzeichen `-2 kappa` statt
   `+2 kappa`.

Damit ist der genaue Status: **Der Ursprung fixiert eine algebraische
Kopplungsrichtung, aber die direkte lineare Feldzeit ist nicht diese
RR/W-Dynamik.** Eine nichtlineare Quellenabbildung oder eine ausdrücklich nur
auf den hellen `Q=2`-Raum beschränkte GNS-Kompression wird dadurch nicht
ausgeschlossen.

## 1. Was ein wirklicher Source-to-Target-Adapter erfüllen müsste

Seien `F_s` und `B_s` zunächst die **endlichen Labelmodule** der markierten
affinen Ströme vom Typ `(bar16,bar4)` und `(10,6)`, mit Strom-Gram `G_s` und
der durch die E8-Klammer gegebenen Abbildung. Diese konjugierte Wahl stimmt
mit den Markierungen des nativen `W` überein; `(16,4)` wird nicht
stillschweigend damit identifiziert.

\[
\langle z,\beta(x\wedge y)\rangle_s
=\langle\Omega_s|J^{z^\dagger}_1J^x_0J^y_{-1}|\Omega_s\rangle
=\mathcal B_{E8}(z^\dagger,[x,y]).
\]

Targetseitig seien `F_t=C^64` der CAR-Einteilchenraum und `B_t=C^60` der
CCR-Einteilchenraum. Dabei darf `Lambda^2 F_s` nicht stillschweigend als
2016-dimensionaler Quell-Hilbertraum gelesen werden. Für affine Ströme gilt
nämlich bereits

\[
\begin{aligned}
q_s(x\wedge y)
&:=\bigl(J^x_{-1}J^y_{-1}-J^y_{-1}J^x_{-1}\bigr)\Omega_s\\
&=J^{[x,y]}_{-2}\Omega_s.
\end{aligned}
\]

Somit faktorisiert die antisymmetrische Zwei-Strom-Abbildung durch `beta`.
Ihr Hilbertraumbild ist der Nachfahrenraum

\[
D_s=\operatorname{span}\{J^z_{-2}\Omega_s:z\in B_s\},
\qquad \dim D_s=60,
\]

nicht ein unabhängiger 2016-dimensionaler CAR-Zweiersektor. Der Kern der
formalen Keilabbildung wird im affinen Quotienten zu Null. Die Niveau-eins-
Norm

\[
\|J^z_{-2}\Omega_s\|^2
=2\mathcal B_{E8}(z^\dagger,z)
\]

ist positiv. Da die nichtverschwindende äquivariante Klammer in das
irreduzible `B_s` surjektiv ist, gilt `ker(q_s)=ker(beta)` und der Quotient hat
exakt Dimension 60. Ein Adapter braucht
daher eine Darstellungseinsetzung `u_F`, eine Isometrie `U_B`, eine
Zustands-/GNS-Abbildung `mathcal U` und einen Quellzeitgenerator `H_s`. Eine
Isometrie eines **vollen** Quell-Paarraums nach `Lambda^2 F_t` wäre zusätzliche
Struktur. Die tragenden Identitäten sind dann:

### 1.1 Metrik, Adjunktion und Ladung

\[
u_F^\dagger u_F=I,
\qquad U_B^\dagger U_B=I,
\qquad \mathcal U\Omega_s=\Omega_t,
\]

zusammen mit der Erhaltung der markierten Ladungen, der Adjunktion und des
`Q`-Grades. Eine bloße Dimensionsgleichheit erfüllt diese Bedingungen nicht.

### 1.2 Ward-/Tensor-Intertwining

Mit dem normierten nativen Koisometrie-Tensor

\[
\widehat W=W/\sqrt8,\qquad \widehat W\widehat W^\dagger=I_{60},
\]

und der analog mit Quell-Gram und Quotientennorm zur Koisometrie normierten
Abbildung `widehat beta`

muss gelten

\[
\boxed{
U_B\,\widehat\beta
=e^{i\phi}\widehat W\,\Lambda^2u_F .
}
\]

Die gemeinsame Phase ist konventionell. Relative Vorzeichen dürfen dagegen
nicht frei angepasst werden; sie müssen aus demselben E8-Kokzyklus und der
gleichen Adjungierung kommen.

### 1.3 Zeit-Intertwining

Für alle erzeugenden Felder müsste auf einer gemeinsamen invarianten Domäne

\[
\boxed{
\Phi([A,H_s])=[\Phi(A),H_t]
}
\]

gelten. Der vorhandene affine Quellraum erlaubt zunächst nur eine helle
Kompression. Mit

\[
P_{\rm br}=\widehat W^\dagger\widehat W,
\qquad
U_{\rm br}:D_s\longrightarrow\operatorname{im}P_{\rm br}
\]

als Isometrie des 60-dimensionalen Nachfahrenquotienten sind die prüfbaren
Blöcke

\[
\begin{aligned}
U_B P_{B_s}H_sP_{B_s}U_B^\dagger&=\Omega,\\
U_B P_{B_s}H_sP_{D_s}U_{\rm br}^\dagger&=C_1P_{\rm br},\\
U_{\rm br}P_{D_s}H_sP_{D_s}U_{\rm br}^\dagger
&=P_{\rm br}(V+\text{benannte kinetische Terme})P_{\rm br}.
\end{aligned}
\]

Erst wenn die Quelle zusätzlich einen echten Paar-Hilbertraum
`H_pair^s` und eine Isometrie
`I_pair:H_pair^s -> Lambda^2 F_t` liefert, dürfen in diesen Formeln die vollen
2016-dimensionalen Blöcke stehen. Die affine Stromalgebra allein liefert
diese Isometrie nicht. Sie liefert jedoch kanonisch den hellen 60-dimensionalen
Quotienten, auf dem `W` nicht verschwindet.

Die Ward-Kubik ist nur die Identität aus Abschnitt 1.2. Sie ist nicht bereits
die mittlere Zeitidentität dieses Abschnitts.

### 1.4 Antwortjets

Alternativ kann der Adapter über Korrelatoren formuliert werden. Dann müssen
nicht nur Gleichzeitkorrelatoren, sondern ihre Ableitungen unter derselben
Zeit übereinstimmen:

\[
\frac{d^n}{dt^n}
\langle\Omega_s|A_s(t)B_s|\Omega_s\rangle\big|_{t=0}
=
\frac{d^n}{dt^n}
\langle\Omega_t|\Phi(A_s)(t)\Phi(B_s)|\Omega_t\rangle\big|_{t=0}.
\]

Genau diese Zusatzforderung trennt einen OPE-Koeffizienten von einem
Hamilton-Matrixelement.

## 2. Der tatsächlich unabhängige positive Adapterteil

Die Originalquelle liefert auf Niveau eins die affine Relation

\[
[J^a_m,J^b_n]
=J^{[a,b]}_{m+n}+m k_{\rm aff}\mathcal B_{E8}(a,b)\delta_{m+n,0},
\]

mit `k_aff=1`. Die invariante E8-Bilinearform `mathcal B_E8` ist nicht die
RR-Kopplungsskala `kappa` des Zieloperators. Außerdem liefert die Quelle den
positiven Grad-eins-Gram und die Kubik

\[
G_{ab}=\mathcal B_{E8}(a^\dagger,b),
\qquad
C(a,b,c)=\mathcal B_{E8}(a,[b,c]).
\]

Das ist ein echter Operatorbefund, kein Dimensionsfit. Die gepinnte E8-Klammer
ist mit den Chevalley-Vorzeichen ausgewertet. Im expliziten Kubik-Contract wird
auf dem E6-A2-Ausschnitt

\[
C_{(A,i)(B,j)(C,k)}=d_{ABC}\epsilon_{ijk}
\]

einschließlich aller Nullstellen und relativen Vorzeichen geprüft.

Für den vollen markierten Typ gilt die klassische Verzweigung

\[
248=(45,1)\oplus(1,15)\oplus(10,6)
\oplus(16,4)\oplus(\overline{16},\overline4).
\]

Außerdem

\[
\Lambda^2(\overline{16}\otimes\overline4)
=\bigl(\operatorname{Sym}^2 \overline{16}\otimes\Lambda^2 \overline4\bigr)
\oplus
\bigl(\Lambda^2 \overline{16}\otimes\operatorname{Sym}^2 \overline4\bigr).
\]

Der reelle Vektor `10` tritt in `Sym^2 bar16` einmal auf und die
selbstkonjugierte `6=Lambda^2 bar4` ebenfalls einmal. Daher ist

\[
\dim\operatorname{Hom}_{\mathrm{Spin}(10)\times SU(4)}
\left(\Lambda^2(\overline{16},\overline4),(10,6)\right)=1.
\]

Die nichtverschwindende E8-Klammer und der native Clifford-Epsilon-Tensor `W`
liegen somit auf derselben eindeutigen Intertwiner-Geraden. Das ist der
unabhängige positive Teil des Quellenadapters: **Die Tensorform von `C1` ist
bis auf Skala und gemeinsame Phase nicht mehr frei.**

Die affine Operatorrelation liefert sogar einen kanonischen hellen
Hilbertraumkanal, aber nur diesen:

\[
\Lambda^2F_s/\ker\beta
\xrightarrow{\ \beta\ } B_s,
\qquad
x\wedge y\longmapsto
\bigl(J^x_{-1}J^y_{-1}-J^y_{-1}J^x_{-1}\bigr)\Omega_s
=J^{[x,y]}_{-2}\Omega_s.
\]

Dieser Quotient hat Dimension 60 und entspricht strukturell
`im(W^dagger)` im targetseitigen CAR-Paarraum. Die Quelle liefert damit einen
kanonischen Kandidaten für den **hellen** `W`-Kanal. Sie liefert weder die
1956 dunklen targetseitigen Paarrichtungen noch einen unabhängigen zweiten
60-dimensionalen Feldraum, der mit diesem Nachfahrenkanal durch eine
Hamiltonzeit gemischt würde.

Der genaue Beweisstand ist enger als eine vollständige Tabellenidentität:

- Der affine Contract prüft den Gram auf allen markierten 64 Stromrichtungen.
- Seine Kubikprüfung verwendet die drei alten A2-Familienrichtungen und deckt
  damit den `16 x 3`-Ausschnitt ab. Für den `bar16 x bar3`-Ausschnitt wird die
  kompakte Adjunktion verwendet; das ist keine lineare Gleichsetzung der
  beiden chiralen Module.
- Das native `W` ist unabhängig als vollständiger `60 x 2016`-Tensor mit
  `WW^dagger=8I` aufgebaut und erfüllt die volle Spin(10)- und SU(4)-Kovarianz.
- Die eindeutige Intertwiner-Gerade identifiziert beide auf
  Darstellungsebene. Ein basisweiser Vergleich der vierten Familienrichtung
  mit demselben Chevalley-Kokzyklus ist in den gelesenen Zertifikaten nicht
  ausgeführt.

Diese Restprüfung betrifft relative Basisphasen. Sie erzeugt keine Zeit und
keinen Hamiltonoperator.

## 3. Erster Zeit-Test: Die affine Gradzeit hat `C1=0`

Die Quelle unterscheidet klar:

- `J^a_{-1}Omega_s` liegt in Grad eins;
- ein geordnetes Produkt zweier Erzeugermoden
  `J^x_{-1}J^y_{-1}Omega_s` liegt in Grad zwei;
- seine für einen CAR-Paarraum relevante antisymmetrische Kombination ist
  kein neuer 2016-dimensionaler Sektor, sondern
  `J^[x,y]_{-2}Omega_s` im 60-dimensionalen Nachfahrenquotienten `D_s`;
- die Kubik verwendet dagegen einen **Nullmodus**,
  `J^x_0`, innerhalb eines Grad-eins-Matrixelements.

Für den affinen Gradoperator `D_aff` gilt

\[
[D_{\rm aff},J^a_{-n}]=nJ^a_{-n}.
\]

Damit ist `D_aff` gradblockdiagonal und folglich

\[
\boxed{
P_{\text{Grad }1}D_{\rm aff}P_{\text{Grad }2}=0.
}
\]

Identifiziert man den Bosonstrom mit einem Grad-eins-Zustand und das
helle Fermionpaarbild mit dem Grad-zwei-Nachfahrenquotienten, ergibt die
direkte affine Zeit also

\[
C_1^{\rm aff}=0,
\]

während der positive RR/W-Kandidat

\[
C_1^{(+)}=\frac\kappa{\sqrt2}W\ne0
\]

verlangt. Die OPE-Kubik `mathcal B_E8(z,[x,y])` ist deshalb kein verstecktes
Zeitmatrixelement: Sie misst die Lieklammer durch einen Nullmodus.

Die naheliegende Gradreparatur ändert diesen Befund nicht. Ordnet man dem
Boson statt `J^z_{-1}Omega_s` einen Nachfahren `J^z_{-2}Omega_s` zu, liegen
beide Labels zwar in Grad zwei. Der vorhandene Nachfahr ist dann aber gerade
derselbe 60-dimensionale Quotient, nicht die zweite orthogonale Kopie des
targetseitigen Direktprodukts. Postuliert man eine solche zweite Kopie
zusätzlich, wirkt `D_aff` dort als `2I`; zwischen orthogonalen Paar- und
Bosonbildern bleibt sein Übergangsblock null. Auch eine Cartanverschiebung
`D_aff+J^h_0` erzeugt keinen
`beta`-Vertex: Sie erhält den Grad und wirkt auf Gewichtsvektoren linear über
ihre Cartanladungen. Die nichtabelsche Drei-Stromantwort kann vollständig aus
Stromklammer, Vakuum und Ward-Identität entstehen, ohne dass sie ein
Hamilton-Vertex ist.

Man könnte stattdessen elementare Felder vom Gewicht `1/2` postulieren, deren
Produkt ein Gewicht-eins-Strom ist. Dann wären aber genau deren CAR-Algebra,
GNS-Darstellung, Lokalität und Zeitwirkung zusätzliche Adapterdaten. Die
affinen Ströme selbst sind in den geprüften Quellen bosonische
Dimension-eins-Randoperatoren und nicht bereits die 64 targetseitigen
Raumzeit-CAR-Felder.

Dieser Test widerlegt nur die direkte Gleichsetzung der affinen Gradzeit mit
der RR/W-Zeit. Er ist kein allgemeiner Ausschluss einer nichtlinearen oder
erweiterten Quellenrekonstruktion.

## 4. Zweiter Zeit-Test: Die globale lineare Zweierquelle scheitert an CAR

Setze auf dem targetseitigen Fockraum

\[
a_A=P_A/\sqrt8,\qquad B_A=b_A+a_A,
\qquad
H_+=2\kappa\sum_C B_C^\dagger B_C.
\]

Da die geraden Paarvernichter untereinander kommutieren,
`[a_A,a_C]=0`, gilt auf dem endlichen Teilchenkern exakt

\[
[b_A,H_+]=2\kappa B_A,
\]

aber

\[
\boxed{
[a_A,H_+]=2\kappa\sum_C M_{AC}B_C,
\qquad
M_{AC}=[a_A,a_C^\dagger].
}
\]

Der zweite Ausdruck ist nicht linear geschlossen, weil `M_AC`
operatorwertig ist. Auf dem leeren Fermionvakuum gilt wegen
`WW^dagger=8I`

\[
M_{AC}|0_F\rangle=\delta_{AC}|0_F\rangle.
\]

Das erklärt, warum der helle `Q=2`-Block genau wie die gewünschte lineare
Zweierquelle aussieht. Auf dem vollständig gefüllten 64-Fermionzustand
`|F>` gilt dagegen

\[
a_C^\dagger|F\rangle=0,
\qquad
\langle a_C F|a_A F\rangle=\delta_{CA},
\]

also

\[
\boxed{M_{AC}|F\rangle=-\delta_{AC}|F\rangle.}
\]

Nun betrachte den normierten Eingang

\[
|\mathrm{in}\rangle=|F\rangle\otimes b_A^\dagger|0_b\rangle
\]

und den Ausgang

\[
|\mathrm{out}\rangle=|F\rangle\otimes|0_b\rangle.
\]

Dann folgt

\[
\langle\mathrm{out}|[a_A,H_+]|\mathrm{in}\rangle=-2\kappa.
\]

Eine global lineare RR-Zweierquelle mit

\[
[a_A,H]_{\rm lin}=2\kappa(a_A+b_A)
\]

würde für dasselbe Matrixelement dagegen `+2 kappa` ergeben. Die Abweichung
ist daher exakt

\[
\boxed{-4\kappa.}
\]

Das ist stärker als der frühere abstrakte CCR-Swap-Einwand: Es prüft direkt
den ersten Heisenberg-Zeitjet des vorgeschlagenen `H_+`. Die bedingte
Positivität von `H_+`, seine innere RR-Symmetrie und seine korrekte helle
`Q=2`-Dynamik bleiben bestehen. Ausgeschlossen ist die **globale lineare**
Operatoridentifikation `a <-> b` mit derselben Zweierquellenmatrix.

Die Prämisse dieses Tests ist stärker als die ursprüngliche affine
Stromantwort: Sie setzt zusätzlich voraus, dass die lineare aktive
RR-Zweiermatrix als globale Heisenberg-Gleichung gerade auf die
zusammengesetzten Operatoren `(a_A,b_A)` übertragen wird. Widerlegt ist diese
konkrete globale Übertragung, nicht die affine E8-Stromalgebra.

Eine nichtlineare Quellgleichung mit dem tatsächlichen Faktor `M_AC` oder eine
nur auf den Vakuum-/`Q=2`-GNS-Raum komprimierte Isometrie wird durch diesen Test
nicht ausgeschlossen. Deren eingeschränkter Geltungsbereich müsste jedoch als
Teil des Adapters angegeben werden.

Ein unabhängiger exakter Minimalcheck mit zwei CAR-Moden und einem
Bosonkanal reproduziert die vier entscheidenden Zahlen
`M|0>=+1`, `M|F>=-1`, tatsächliches Matrixelement `-2` und lineares Ziel
`+2` bei `kappa=1`; die Differenz ist `-4`. Das maschinenlesbare Zertifikat
liegt in
`/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/work/pdf_consolidation_20260921/source_adapter_minimal_check.json`
mit SHA-256
`7ee54c4c1c43272e32f22c7c987a0cac59ff1496f82646e91dd110cf658ff864`.
Der eng begrenzte Replay-Checker
`source_adapter_minimal_check.py` hat SHA-256
`fce2c2d773e2ea969a39355a626570d0e3d625a96180e040217c43a08737c338`;
Normal- und `-OO`-Lauf sind byteidentisch. Er ist eine Algebra-Kontrolle und
keine neue native Vollprüfung.

## 5. Was sich über `Omega` und `V` tatsächlich sagen lässt

### `Omega`

Der affine Zwei-Strom-Gram legt eine invariante positive Metrik fest. Nach
Identifikation des irreduziblen `(10,6)`-Raums folgt aus Symmetrie für einen
zusätzlich gewählten invariant-quadratischen Zielblock nur

\[
\Omega=\omega I_{60}.
\]

Weder die Interpretation des Grams als Hamiltonblock noch der Wert
`omega=2 kappa` folgt aus dem Gram. Der Originalbericht warnt ausdrücklich,
dass der normierte Grad-eins-Gram keine reduzierte Vakuumdichtematrix ist.

### `V`

Aus der Klammer kann algebraisch der positive Operator

\[
\beta^\dagger\beta\ \sim\ W^\dagger W
\]

gebildet werden. Damit ist die **Form** des möglichen elastischen Kanals
natürlich. Der volle affine Vierstromkorrelator ist aber nicht einfach eine
Gaussianische Wick-Kontraktion. Er enthält den zusätzlichen verschachtelten
Klammerterm

\[
\mathcal B_{E8}(a^\dagger,[[b^\dagger,c],d]).
\]

Dieser Term ist in der Niveau-eins-Quelle unverzichtbar und erzeugt dort auch
Nullrelationen. Deshalb darf die volle affine Vierpunktantwort ohne eine
benannte Kompression oder Normalordnung nicht mit
`V=(kappa/4)W^dagger W` gleichgesetzt werden.

Die Schur-Sättigung

\[
V=C_1^\dagger\Omega^{-1}C_1
\]

ist eine exakte Konsequenz des positiven Lifts `H_+`. Sie ist keine bisher
geprüfte Ward-Identität der affinen Quelle.

## 6. Bilanz der drei Zieljets

| Zielgröße | Aus ursprünglicher Stromantwort belastbar | Nicht bestimmt / direkter Test |
|---|---|---|
| `Omega` | invariante Metrik, daher bei zusätzlichem invariantem Hamiltonblock skalare Form | Hamiltoninterpretation und Skala `2 kappa` offen |
| `C1` | eindeutige Spin(10)-SU(4)-Intertwiner-Richtung `W` bis Skala/Phase und kanonischer heller 60D-Nachfahrenquotient; explizite Kubik bisher nur im Dreifamilien-Ausschnitt plus Adjunktion | kein voller 2016D-CAR-Quellsektor; affine Gradzeit gibt auf dem Paar/Boson-Direktprodukt exakt `C1=0`; Skala `kappa/sqrt(2)` nicht aus OPE |
| `V` | natürliche algebraische Form `W^dagger W` aus Klammer-Gram | Koeffizient und Schur-Sättigung nicht aus Ward; voller Vierpunkt enthält Zusatzterm |

## 7. Der jetzt entscheidende Herkunftstest

Der nächste Test ist kein weiteres Spektrum von `H_+`. Er besteht darin, in
der ursprünglichen P1/P2-/Randquelle einen **bereits unabhängig definierten**
Transfer oder Generator `H_s` zu benennen und genau die drei Kompressionen aus
Abschnitt 1.3 auszuwerten.

Der naheliegende vorhandene Kandidat, die affine Grad-/Konformalzeit, fällt am
mittleren Block bereits aus:

\[
P_{B_s^{(1)}}D_{\rm aff}P_{D_s^{(2)}}=0.
\]

Soll stattdessen eine nichtlineare Quelle benutzt werden, muss ihr erster
Feldjet den operatorwertigen Faktor

\[
[a_A,H_+]=2\kappa\sum_C[a_A,a_C^\dagger](a_C+b_C)
\]

reproduzieren. Soll nur eine Kompression benutzt werden, muss sie ausdrücklich
auf den hellen Vakuum-/`Q=2`-Raum beschränkt werden; dann darf daraus keine
globale lineare Feldautomorphie gefolgert werden.

Das ist ein abgeschlossenes Entscheidungskriterium: Ein vorgeschlagener
Quellenadapter muss entweder diese nichtlineare Identität oder die klar
begrenzte Kompression mitsamt Zustands- und Mehrzeitantwort liefern. Ein
erneuter Nachweis allein der Ward-Kubik erfüllt das Kriterium nicht.

## 8. Quellenpins und Prüfgrenze

Es wurden gezielt die folgenden Dateien im angegebenen Stand verwendet. Diese
Liste ist keine globale Vollsuche aller TFPT-Unterlagen.

| Quelle | verwendete Stellen | SHA-256 |
|---|---:|---|
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/PROOF.txt` | 19–39, 41–59, 66–100, 115–131 | `d65189b806facbb1eb718eec50221bb85b3a8c3417f98fb6627e01c72c98ef62` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/checker.py` | 100–128, 135–188, 250–280 | `cfe406a6302c9bec7ceb404074f83e28006351e13dbc4b8a143231d758d8e119` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-current-product-20260919/PROOF.txt` | 42–119, 209–235, 271–291 | `940131acfceba1937d36b44447ecce39b25571ef7c95e870667b838f4e9ae0db` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-native-root-dictionary-20260918/PROOF.txt` | 50–89, 142–175 | `b5de7459d2c849ea320cc83e2abe6f12af0933fda1917ab5b8d44ddb52fa6de1` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-singlet-observable-20260915/sources/native_source.py` | 36–85, 162–220 | `380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/rr-continuous-clock-20260921/HERLEITUNG.md` | 56–92, 108–135 | `8e133bd50713e7e16fc6808bdbb38f38efb878b9cc0b189d46c062dc1043bde8` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/rr-continuous-clock-20260921/ALGEBRA.md` | 20–39, 108–120, 134–197 | `52de68fe2688829be9193796bb2239471df5e6a2dc6c4bcb98bd3ec2be83e2fb` |
| `/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/work/rr_positive_20260921/source/REPORT.md` | 300–390, 430–498 | `d87f20f8b1a8256605b56560ea0e74b72696f75e802ca0aa7f08140b8e4b03ea` |

Der Theoriegraph wurde nach der zwischenzeitlichen Contract-Änderung neu
erzeugt und am Abschluss erneut geprüft: `THEORY-GRAPH OK`, 5.948 Knoten und
64.043 Kanten. Die gezielten Abfragen `tried` und `kills` auf
`affine current source adapter Ward OPE RR W` lieferten jeweils null Treffer.
Dieser Nulltreffer ist kein Beweis; der mathematische Befund oben beruht auf
den gepinnten Originaldateien.

Zur unabhängigen Literaturkontrolle wurde die Standardherkunft der affinen
Strom-Wardidentitäten im Originalartikel von Knizhnik und Zamolodchikov,
*Current Algebra and Wess-Zumino Model in Two Dimensions*,
[DOI 10.1016/0550-3213(84)90374-2](https://doi.org/10.1016/0550-3213(84)90374-2),
und die verwendete Gewicht-eins-Gradwirkung zusätzlich in
Borisov--Halpern--Schweigert,
[*Systematic Approach to Cyclic Orbifolds*, Abschnitt 3.5 und Gleichung
(3.59)](https://arxiv.org/abs/hep-th/9701061), gegengeprüft.
Diese Literatur bestätigt den allgemeinen Current-Algebra-/Ward-Rahmen; die
konkreten E8-Koeffizienten und Markierungen stammen weiterhin aus den lokalen
gepinnten Verträgen.

Die physischen T1–T8-Gates bleiben offen.
