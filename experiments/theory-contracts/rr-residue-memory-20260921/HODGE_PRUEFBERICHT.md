# RR-Hodge und der geladene Quellenanschluss: kleinster tragender Test

21. September 2026 · begrenzte exakte Strukturprüfung · keine Ledger-/Paper-Promotion

## Entscheidung

**Für die fest markierte bestehende Quelle ist die vorgeschlagene Brücke verworfen.** Die Familienkonjugation, die aus dem nativen Zweig

\[
(16,4)+(\overline{16},\overline4)
\]

den benötigten gekreuzten Zweig

\[
(16,\overline4)+(\overline{16},4)
\]

macht, ist keine Automorphie der festgehaltenen primitiven \(D_5+A_3\)-Klebung. Sie vertauscht exakt die beiden möglichen \(E_8\)-Klebungen. Der neue RR-Hodge-Operator behebt das nicht: Im konstruierten RR-\(W\)-Diagramm ist er ein isometrischer Basistransport auf den 60 Bosonenzeilen, keine aktive blocktauschende Symmetrie des unveränderten Quellen-Hamiltonoperators.

**Positiv erlaubt** ist eine ausdrücklich erklärte Umdeutung auf die andere Sheet-Chiralität des \(E_8\)-Überverbandes. Das liefert algebraisch genau die gekreuzte Familienorientierung. Es ändert jedoch die markierte Klebung, die Ramond-Projektion und die Orientierung der gemeinsamen \(\mu_4\)-Identifikation. Es darf deshalb nicht als unveränderter Anschluss an die bisherigen Quellen-, Paritäts- und Clockmarken ausgegeben werden.

Der exakte Checker hat acht Prüfgruppen normal und mit `-OO` bytegleich bestanden. Sein Verdict lautet:

`FIXED_MARKED_GLUE_REJECTS_FAMILY_ONLY_TWIST; RR_HODGE_IS_BOSON_BASIS_TRANSPORT_NOT_A_SOURCED_BLOCK_EXCHANGE; AN_ALGEBRAIC_PIN_LIFT_EXISTS_ONLY_ON_THE_RESTORED_M8`.

## 1. Der kleinste entscheidende Test ist die Klebegruppe

Die maßgebliche Diskriminantenform ist

\[
A_{D_5}\oplus A_{A_3}=\mathbb Z_4\oplus\mathbb Z_4,
\qquad
q(x,y)=\frac{5x^2+3y^2}{8}\pmod1.
\]

Die vollständige endliche Klassifikation enthält genau zwei isotrope Untergruppen der Ordnung vier:

\[
H_+=\langle(1,1)\rangle,
\qquad
H_-=\langle(1,3)\rangle=\langle(1,-1)\rangle.
\]

Beide geben einen geraden unimodularen Rang-8-Überverband, also abstrakt \(E_8\). Ihre **markierten** Darstellungsinhalte unterscheiden sich jedoch:

| Klebung | ungerade Klassen |
|---|---|
| \(H_+\) | \((16,4)+(\overline{16},\overline4)\) |
| \(H_-\) | \((16,\overline4)+(\overline{16},4)\) |

Familienkonjugation wirkt auf der Diskriminantengruppe als

\[
c_F:(x,y)\longmapsto(x,-y),
\qquad c_F(H_+)=H_-\ne H_+.
\]

Trägerkonjugation allein tut dasselbe. Nur die gleichzeitige Konjugation

\[
(x,y)\longmapsto(-x,-y)
\]

erhält \(H_+\). Sie vertauscht aber beide Faktoren zugleich und lässt deshalb den alten ungekreuzten Sektor als Menge erhalten. Sie erzeugt den benötigten gekreuzten Sektor gerade nicht.

Das ist der primitive Lasttest. Gleiche Dimensionen, die reelle Ununterscheidbarkeit von \(4\) und \(\bar4\) auf einer kleinen \(D_4\)-Untergruppe und eine äußere Wirkung auf der Lie-Algebra reichen nicht: Der Überverband enthält die Orientierung der beiden \(\mathbb Z_4\)-Ladungen.

Dieser Befund ist keine neue allgemeine \(E_8\)-Klassifikation. Er wendet die bereits exakte Klassifikation in `verification/v92_glue_uniqueness.py`, Zeilen 10–38 und 92–112, auf genau die neue RR-Frage an.

## 2. Warum der RR-Hodge-Operator die Markierung nicht heimlich repariert

Auf \(\Lambda^2\mathbb C^4\) ist die lineare Komplementabbildung \(K\) eine orthogonale Involution mit

\[
K^2=1,\qquad \det K=-1.
\]

Mit der natürlichen antilinearen Realstruktur

\[
\mathcal J(v)=K\overline v
\]

ist \(K\) auf dem reellen Sechser tatsächlich orientierungsumkehrend. Algebraisch besitzt es daher auf dem vollen vorkomprimierten

\[
\mathrm{Cl}_6(\mathbb C)=M_8
\]

einen ungeraden Pin-Lift \(C_K\). Der Checker konstruiert ihn explizit und bestätigt

\[
C_K^2=-1,\qquad C_KP_+C_K^{-1}=P_-,
\qquad C_K\gamma(v)C_K^{-1}=\gamma(Kv).
\]

Das ist die konstruktive Möglichkeit, die der frühere Offset-Satz verlangt: **Wenn** dieses \(C_K\) als quellenselektierte Symmetrie vorläge und zusätzlich \(C_KHC_K^{-1}=H\) gälte, könnte ein unabhängiger \(\Delta P_-\)-Offset nicht bestehen.

Genau die zweite Hälfte fehlt. Der RR-Checker verwendet

\[
W^\sharp=(I_{10}\otimes K)W.
\]

Das ist kein Fixpunktsatz \((I_{10}\otimes K)W=W\). Exakt gilt:

- \(W^\sharp\ne W\);
- alle 480 getragenen Koeffizienten werden auf andere Bosonenzeilen verschoben;
- `Wsharp - W` hat 960 Nichtnullstellen;
- die Gram-Matrix bleibt erhalten: \(W^\sharp W^{\sharp T}=WW^T=8I_{60}\).

Damit ist \(K\) im RR-Anschluss ein sauberer, vollständig mit den Ladungsmarken mittransportierter Bosonenbasiswechsel. Er ist keine aktive Symmetrie des fest geschriebenen \(W\)-Tensors. Das ausgeführte native Modell enthält außerdem nur den \(P_+\)-Familienblock in seinen 64 Fermionmoden; \(P_-\) und die sechs ungeraden Übergänge sind Hilfsdaten vor der Kompression, keine ausgeführten Felder oder Hamiltonoperatoren. Aus der algebraischen Existenz von \(C_K\) folgt daher weder \(C_KHC_K^{-1}=H\) noch eine Auswahl des relativen Sektoroffsets.

## 3. Der D4-Fallstrick entscheidet gegen einen automatischen Pin-Lift

Für einen reellen Viermarken-Generator \(P\) mit \(\det P=-1\) hat die rohe Wirkung \(\Lambda^2P\) ebenfalls Determinante \(-1\). Sie antikommutiert jedoch mit der natürlichen Realstruktur:

\[
K\Lambda^2P=-\Lambda^2P K.
\]

Sie ist daher nicht bereits die reelle \(SO(6)\)-Wirkung des vollständig komplexen \(SU(4)\)-Faktors. Nach der notwendigen Determinantennormalisierung ist

\[
\widetilde P=e^{-i\pi/4}P\in SU(4),
\qquad
\Lambda^2\widetilde P=-i\Lambda^2P.
\]

Diese Wirkung erhält \(\mathcal J\) und hat reelle Determinante \(+1\). Die markierte \(D_4\)-Kovarianz liefert somit keinen automatischen orientierungsumkehrenden Pin-Operator, der die beiden Spinorblöcke vertauscht. Der separate Operator \(K\) kann einen solchen Pin-Lift haben; seine Auswahl als physische Quellensymmetrie ist dadurch aber nicht bewiesen.

## 4. Clocks und Gradierung

Da bereits die Klebeprüfung scheitert, ist kein weiterer \(C/J\)-Optimierungslauf gerechtfertigt. Auf der zentralen \(\mathbb Z_4\)-Marke wirkt die Familienkonjugation als \(J\mapsto J^{-1}\); das ist dieselbe Abbildung \(y\mapsto-y\), die \(H_+\) nach \(H_-\) schickt. Sie erhält die festgelegte Clockmarkierung also nicht.

Der bestehende Originaltest ist bereits stärker als eine bloße Zentralphase: `family_intertwiner/PROOF.md`, Zeilen 87–106, zeigt, dass die familienkonjugierten Arrays nur basistransportierte Identitäten liefern, dass die native `BAR`-Operation gleichzeitig die Spin(10)-Opposition enthält und dass alle 64 familienkonjugierten Gewichte außerhalb des ursprünglichen \(E_8\)-Wurzelsystems liegen. Der gemeinsame feste \(C/J\)-Abschluss umfasst wieder 240 Wurzelrichtungen. Daran wird hier kein neuer Claim angehängt.

Die notwendige Zeitbedingung bleibt genau die bereits benannte:

\[
C P_+ C^{-1}=P_-,\qquad CHC^{-1}=H.
\]

Der erste Satz ist für einen algebraischen Pin-Lift auf \(M_8\) konstruierbar; der zweite Satz ist für die RR-Konstruktion und die native physische Quelle nicht vorhanden. Deshalb bleibt `delta_offset_selected=false`.

## 5. Genaue positive und negative Reichweite

**Erlaubte positive Lesart:** Als unmarkierte Gitter oder holomorphe \(c=8\)-Netze sind die beiden Überverbände isomorph. Mit einem ausdrücklich deklarierten Sheet-Wechsel \(H_+\leftrightarrow H_-\) kann man die native Darstellungsorientierung in die gekreuzte Orientierung überführen. Danach müssen jedoch alle betroffenen Daten gemeinsam neu transportiert werden: Glue-/Ramond-Projektion, Familienzentrum, Parität, Clocks, Feldwörterbuch, Zustand und Hamiltonoperator. Das ist eine andere markierte Quellenidentifikation.

**Verbotene Lesart:** \(K\) nur auf den Bosonen anwenden, die 64 Fermionen und die Klebung fest lassen und daraus eine Identität mit den ungeraden gemeinsamen T-Feldern folgern. Das würde gleichzeitig \(H_+\) und \(H_-\) benutzen.

**Nicht ausgeschlossen:** Eine zukünftige Quelle könnte beide Chiralenblöcke physisch ausführen und genau den konstruierten Pin-Lift samt gemeinsamem Hamiltonoperator auswählen. Der heutige RR-Befund liefert dafür die endliche Algebra, aber nicht die Auswahl, Zeit, Lokalität oder physische Gradierung.

## 6. Das alternative \(F_{\rm aux}\)-Wörterbuch

Die vorhandenen Quellen beantworten diese Alternative bereits bis zur richtigen Grenze:

- `source-boundary-selection-20260920/PROOF.md`, Zeilen 116–154, konstruiert \(F_{\rm aux}(p)=T_a(p)-k_a(p)n\) als integrale Isometrie mit einer zusätzlichen \(n\)-Komponente und einer kompatiblen positiven Matrix \(V_{\rm aux}\).
- Zeilen 176–202 geben den lokalen quartischen Spinorstrom, erhalten Ladung und Grad auf allen 240 Wurzeln und halten fest, dass die Identifikation mit den nativen \(C/J\)-Wirkungen separat bleibt.
- `family_intertwiner/PROOF.md`, Zeilen 71–73, sagt ausdrücklich, dass der gemeinsame-T-Zentrumsausschluss dieses andere Wörterbuch nicht automatisch trifft.
- Die Herkunft ist dennoch nicht geschlossen: \(V_{\rm aux}\) ist nach Auswahl von \(n\) konstruiert, nicht aus P1/P2 oder der ursprünglichen QWZ-/nativen \(W\)-Quelle gewählt; Zustand, Zeit und geladene Paarstruktur fehlen.

Damit ist \(F_{\rm aux}\) der bereits bekannte bedingt positive alternative Wörterbuchweg. Er ist kein Beleg, dass das vorhandene native \(W\) ohne neue Feld-/Zeitabbildung direkt die gemeinsamen ungeraden c-Felder erzeugt.

## Reproduktion und Scope

Im Ordner liegen:

- `checker.py`: exakte Diskriminanten-, Hodge-/Realstruktur-, Pin- und \(W\)-Tests;
- `certificate.json`: acht bestandene Prüfgruppen, `PASS_EXACT_SCOPED`.

Ausführung:

```sh
python3 -B checker.py
python3 -B -OO checker.py
```

Beide Läufe erzeugen bytegleiches `certificate.json`. Verifiziert wurden sieben Quellenpins. Kein Repository, Theoriegraph, Ledger, Paper oder Originalvertrag wurde verändert. Das Ergebnis entscheidet nur den neu gestellten markierten Hodge-Anschluss. Es schließt kein physisches T1–T8-Gate und behauptet keine vollständige TFPT-Lösung.
