# Gemeinsame E8-Rollen: kompatible interne Verzweigung, keine doppelte Raumrolle

14.09.2026. NON-RH. Unabhängige endliche Wurzelrechnung und gezielte
Primärquellenprüfung. Quellen bleiben unverändert; kein Commit, keine
Behauptung einer vollständigen Physik oder eines neuen T2-Abschlusses.

## 1. Ein gemeinsamer D5 ist tatsächlich möglich

Das ist mehr als eine Dimensionsähnlichkeit. In der üblichen orthonormalen
R8-Darstellung nehmen wir die 240 E8-Wurzeln

\[
 \{\pm e_i\pm e_j\}\ \cup\
 \{\tfrac12(\pm1,\ldots,\pm1):\text{gerade Anzahl Minuszeichen}\}.
\]

D5 liegt auf den ersten fünf Koordinaten. Sein Zentralisator besteht aus
den D3=A3-Wurzeln auf den letzten drei Koordinaten. Darin wählen wir A2
mit einfachen Wurzeln e6−e7 und e7−e8. Die dazu orthogonalen E8-Wurzeln
haben x6=x7=x8 und bilden E6. Damit gelten in **derselben Einbettung**

\[
 D_5\subset E_6=C_{E_8}(A_2),\qquad
 A_2\subset A_3=C_{E_8}(D_5).
\]

Der Checker prüft Wurzelzahlen, Ränge, Weyl-Abgeschlossenheit und beide
Zentralisatorgleichheiten direkt: D5 hat 40 Wurzeln/Rang5, A3 hat12/Rang3,
A2 hat6/Rang2, E6 hat72/Rang6. Es wird kein Schluss allein aus 248 gezogen.
Die Bezeichnungen der kompakten Gruppen sind Spin(10), SU(4), E6 und SU(3);
die globalen Untergruppen in E8 tragen die bekannten gemeinsamen endlichen
Zentrenquotienten. Die hier bewiesenen Zentralisator- und Verzweigungsaussagen
sind Lie-Algebra-Aussagen, keine Behauptung unabhängig wirkender voller Zentren.

## 2. Beide Verzweigungen sind dieselbe vollständige Gewichtstabelle

Die bereits im Repo stehende Zerlegung ist

\[
248=(45,1)+(1,15)+(10,6)+(16,4)+(\overline{16},\overline4).
\]

Quelle: `tfpt_1_architecture_e8.tex:2001`. Unter SU(4)→SU(3)×U(1),
mit Q=−2(x6+x7+x8), gelten

\[
4=3_1+1_{-3},\quad 6=3_{-2}+\bar3_2,
\quad15=8_0+1_0+3_4+\bar3_{-4}.
\]

Die unabhängige vollständige Wurzelzählung einschließlich aller acht
Cartanrichtungen ergibt folgende Tabelle:

| Spin(10) | SU(3) | Q | Dimension |
|---|---|---:|---:|
|45|1|0|45|
|1|8|0|8|
|1|1|0|1|
|16|3|1|48|
|bar16|bar3|−1|48|
|16|1|−3|16|
|bar16|1|3|16|
|10|3|−2|30|
|10|bar3|2|30|
|1|3|4|3|
|1|bar3|−4|3|

Neu gruppiert ist dies genau

\[
 248=(78,1)+(1,8)+(27,3)+(\overline{27},\bar3),
\]
\[
 78=45_0+1_0+16_{-3}+\overline{16}_{3},\qquad
 27=16_1+10_{-2}+1_4.
\]

Der Standardvergleich steht in Slanskys Tabellen, aber die hiesige gemeinsame
Einbettung und Gewichtstabelle sind eigenständig berechnet; für eine weitere
Primärrechnung mit E8→E6→SO(10)-Verzweigungen siehe
[Stepanyantz, Gleichungen zur SO(10)-Zerlegung](https://arxiv.org/abs/2305.01295).
Diese Referenz wird nicht als Beweis seiner physikalischen Modellwahl übernommen.

**Drei 16er kommen also vor, aber nicht allein:** Ihre konjugierten Partner
sind ebenso vorhanden; zusätzlich enthält der E6-Adjunkt ein weiteres
16+bar16-Paar als SU(3)-Singuletts. Ein interner Spin(10)-Halbspinor ist
zudem noch kein Lorentz-Weyl-Fermion. Die Auswahl eines chiralen, leichten
4D-Materiespektrums braucht einen eigenen lokalen Dynamik-/Projektionssatz;
das Entfernen der konjugierten Hälfte ist keine Verzweigungsregel.

Die Auswahl eines A2 in A3 entspricht der Festlegung einer komplexen Linie
im 4er von SU(4), also einer SU(4)→S(U(3)×U(1))-Struktur. Die Existenz dieser
gemeinsamen Verzweigung bestimmt nicht automatisch den physischen Auswahlmechanismus.

## 3. A3 kann nicht zweimal als unabhängiger interner Faktor verbraucht werden

Exakt aus derselben Wurzelrechnung folgt

\[
C_{E_8}(D_5\oplus A_2)=\mathfrak u(1).
\]

Es gibt keine Wurzeln mehr im Zentralisator und genau eine Cartanrichtung.
Insbesondere gibt es innerhalb dieser E8-Einbettung keinen unabhängigen,
mit Spin(10) und SU(3)_fam kommutierenden A3-Raumfaktor. Bereits die
Rankensumme 5+2+3=10>8 verbietet drei solche unabhängigen kommutierenden
Lie-Faktoren. Ebenso ist der Zentralisator von SU(3) im betreffenden SU(4)
nur U(1), nicht nochmals eine Raumrotationsgruppe.

Dies ist **kein Verbot**, denselben abstrakten Gittertyp als geometrische
Hilfsstruktur zu verwenden. Eine räumliche Translationsstruktur Z3 und ihre
diskrete Punktgruppe sind nicht dasselbe wie die kontinuierliche interne
SU(4)-Wirkung. Aber für diese andere Interpretation muss angegeben werden,
auf welchen Ortsobservablen sie wirkt, wie lokale Nachbarn entstehen und
wie sie sich mit der Familienwirkung verträgt. Ein duales Gitter ist kein
zweiter unabhängiger Lie-Faktor. Das Repo warnt bereits vor solchen
Typgleichsetzungen: `tfpt_research_contracts.tex:11008`–`11036` unterscheidet
A3_family, A3_ALE und externe Gauge-Rollen ausdrücklich.

**FCC/BCC-Korrektur:** Im üblichen R3-Modell ist
\(Q(A_3)=D_3=\{n\in Z^3:\sum n_i\text{ gerade}\}\), also FCC.
Sein duales Gewichtsgitter ist
\(P(A_3)=Z^3\cup(Z^3+(1/2,1/2,1/2))\), also BCC.
Der Checker verifiziert die dualen Basen, Kovolu­men2 und1/2 sowie den
Halbkoordinatenkörpermittelpunkt. „A3 ist BCC“ braucht daher mindestens
den Zusatz **duales Gewichtsgitter**, samt Metrik-/Skalenkonvention.

## 4. Was der E8-VOA-Shortcut wirklich liefert

Für ein gegebenes positives gerades Gitter ist die Gitter-Vertexkonstruktion
ein etablierter mathematischer Anschluss. Die Netzversion liefert für ein
einfach zusammenhängendes einfaches, einfach gelagertes G die Gleichheit
von Wurzelgitternetz und Level-1-Schleifengruppennetz:
[Bischoff, Proposition3.19](https://arxiv.org/pdf/1108.4889).
Die Konstruktion setzt das Gitter und die zugrunde liegende positive
Energie-/Vakuumdarstellung voraus; sie identifiziert nicht automatisch
einen zuvor anders konstruierten TFPT-Collar.

In dieser gegebenen Konstruktion haben Wurzelvertexoperatoren mit
\(\|\alpha\|^2=2\) das konforme Gewicht1. Für die 128 Halbkoordinatenwurzeln
ist das ausdrücklich

\[
h=\tfrac12\sum_{i=1}^8(1/2)^2=1=5/8+3/8.
\]

Sie ergänzen die D8-Ströme120 zum E8-Adjunkten248; insgesamt sind es
240 Wurzelrichtungen plus8 Cartanströme. Die Stücke5/8 und3/8 sind
**konforme Gewichte**, nicht Raumdimensionen; h=1 ist kein Nachweis von
vierdimensionaler fermionischer Spin-Statistik.

Auch der Cocycle ist konkret konstruierbar. Für eine einfache E8-Basis mit
Cartanmatrix C definiert der Checker
\[
 \epsilon(n,m)=(-1)^{\sum_i n_im_i+\sum_{i>j}n_im_jC_{ij}}.
\]
Bilinearität beweist die2-Cocycle-Identität auf ganz Z8. Exakt geprüft sind
die Integralkoordinaten sämtlicher240 Wurzeln, alle57600 Kommutatorzeichen
\(\epsilon(n,m)/\epsilon(m,n)=(-1)^{(n,m)}\) und die Diagonalzeichen.
Diese Bedingungen entsprechen der Primärkonstruktion bei
[Dong–Xu, Abschnitt3](https://arxiv.org/pdf/math/0411499) und
[van Ekeren–Möller–Scheithauer, Abschnitt7](https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/scheithauer/publications/Construction_and_classification_of_holomorphic.pdf).
Der konkrete Cocycle-Vertreter hängt von Basis/Phasenkonvention ab;
Existenz bzw. Äquivalenzklasse ist nicht gleich einer schon nachgewiesenen
Übereinstimmung mit allen nativen Nahtphasen und ihren markierten Symmetrien.

**Kein neuer T2-Abschluss:** Das abstrakte E8-Ziel ist im Repo bereits
vorhanden, also keine neue mathematische Entdeckung und keine notwendige
neue Gitterannahme. `v154_simple_current_theorem.py:7`–`10` und `:37`–`43`
lassen ausdrücklich den Naht-Calderon-Netz-Anschluss offen; ebenso v175.
Wer das tatsächliche Quellnetz nun schlicht als dieses Gitter-VOA definiert,
macht eine Quellidentifikation zur Annahme. Wer sie beweisen möchte, braucht
den nachstehenden Intertwiner. Eine neu bewiesene Zustandsauswahl innerhalb
eines angenommenen endlichen Fockmodells wird dadurch weder bestritten noch
zu einem vollständigen lokalen Netzintertwiner hochgestuft.

**Kleine Quellenkorrektur:** D5⊕A3→E8 hat Gitterindex4, aber D8→E8 hat
Index2. Daher darf v175s verkürzte Formulierung „SO(16)_1 ... mu4 ... index4“
nicht als Index4-Erweiterung des D8-Netzes gelesen werden. Die korrekte
Index4-Kette beginnt bei D5⊕A3; der letzte D8-Schritt ist die Spinor-Z2-Erweiterung.

## Minimaler gemeinsamer Brückenvertrag

**Ein markierter lokaler Quell-Intertwiner mit verträglichen Rollen:**
Aus dem festgelegten operationalen Seed ist eine Abbildung seiner lokalen
positiven Nahtalgebra in das E8-Gitternetz zu konstruieren, welche Produkte
einschließlich Cocycle, Adjungierung/Reflexion, Zustand und zulässige
Zeittranslation erhält und die obige gemeinsame D5–A2-Einbettung realisiert.
Eine zusätzlich behauptete BCC-Raumwirkung muss dabei ausdrücklich auf
Ortsobservablen wirken und mit den internen D5×SU(3)-Observablen verträglich
sein; sie darf kein bereits verbrauchter zweiter interner A3-Faktor sein.
Erst die zugehörige lokale Dynamik darf die leichte chiral-materielle
Teilstruktur auswählen. Dieser Vertrag fordert keinen deterministischen
einzelnen Messausgang und nicht die Beseitigung gewöhnlichen Bornzufalls.

Der **hier erledigte mathematische Teil** ist die explizite gemeinsame
Einbettung, ihre vollständige Gewichtstabelle, die Zentralisatorobstruktion,
die Wurzel-/Gewichtsgitterunterscheidung sowie die endliche h-/Cocycle-Konstruktion.
Der Vertrag selbst ist nicht bewiesen. Es wurden keine fremden Quell- oder
Ledgerdateien geändert und keine vorhandenen endlichen Ergebnisse widerrufen.

Reproduktion: `/opt/homebrew/bin/python3 checker.py`; Ergebnis in
`verification.json`. **7369/7369 Guards bestanden, zuletzt unter `python3 -O`.**
Eine nachträglich ergänzte Indexprüfung lief zunächst wegen Python-Division
in den Float-Typ; die strikte Gleichheitsprüfung fing dies ab. Der minimale
Reproduktionstest bestätigte `sqrt(16.0)` als Float versus `sqrt(Integer(16))`
als exakten Integer. Die endgültigen Indexwerte werden aus den tatsächlich
berechneten Gramdeterminanten gewonnen; der vollständige Replay ist grün.
Eigene Prüfungen sind aktive Guards, keine abschaltbaren
Python-asserts. Prüfanzahl ist keine Anzahl unabhängiger physikalischer Entdeckungen.
