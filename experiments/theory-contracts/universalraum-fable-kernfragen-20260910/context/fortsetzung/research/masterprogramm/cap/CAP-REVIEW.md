# Cap, hoher Block und physischer Intertwiner

10. September 2026. Gezielter Review des jüngsten Anhangs, insbesondere §§10,16,17 und Schluss. Die Vorschläge im Anhang werden als zu prüfende Aussagen behandelt. Originale und bestehende Ergebnisse wurden nicht verändert.

**Ergebnis:** Die Cap-Normierung und der angegebene Parent sind konsistent. Der Schluss auf eine intrinsisch ausgewählte physische Dynamik ist noch nicht bewiesen. Ein stärkerer eigener Gegenzeuge zeigt sogar: Derselbe vollständige Parent, dieselbe Z₄-Neutralität, dieselbe Norm und Einheitsamplitude können verschiedene markierte Quellströme besitzen. Genau hier muss der vorgeschlagene Intertwiner mehr leisten als eine Matrixidentifikation.

## 1. Die tatsächlich vorliegenden Quellen

Das native `verification/v125_glue_qsystem.py` definiert auf \(Q=\mathbb C[\mathbb Z_4]\) mit orthonormaler Standardbasis
\[
m:Q\otimes Q\to Q,\qquad m(e_a\otimes e_b)=e_{a+b},\qquad\eta(1)=e_0.
\]
`build_mult` und `run` wurden über den aktuellen Codegraph gefunden und vollständig gelesen. \(mm^*=4I_Q\) wird dort tatsächlich geprüft. Die Identifikation mit der Seam–Calderón-Inklusion wird im selben Modul ausdrücklich als verbleibende Aufgabe bezeichnet.

Der native `signed_block` in `verification/v1027_signed_det_car_wall.py` lautet
\[
h(A)=\begin{pmatrix}A+\lambda g^2A^2&\lambda gA\\\lambda gA&(\Delta+\lambda)I\end{pmatrix},
\quad (\Delta,\lambda,g)=(3,1,1/2).
\]
Der originale DET-CAR-Beweis setzt eine neutrale Determinantenprämisse voraus. Seine Fock-Banddiagonalisierung gilt für feste klassische Hintergründe. Der tatsächliche ungeschnittene Rotor/CAR-Parent in `ground-state-loop-response/README.md` besitzt hingegen dynamische elektrische Operatoren und \(A=A_U/12\), \(\|A\|\le1/2\). Sein Materiekoeffizient stimmt exakt mit dem Anhang überein. Die spätere native Untersuchung `det-wall-hh-rule/PROOF.md` vom 10. September benennt den onsite-Hochstrom als zusätzliche DET-Wandprämisse; sie leitet ihn nicht aus P1/P2 her.

Die heutigen Ergebnisse `TFPT-Globaler-Quellabschluss.md` und `TFPT-Markierter-Ursprung-der-Kopplung.md` liefern die im Anhang verkürzt zitierten Sätze. Sie behaupten selbst keinen vollzogenen Cap↔CAR/Rotor-Intertwiner. Die aktuellen Ledgerzeilen `GNET.RAMIFIED.01`, `GNET.MARTINGALE.LIMIT.01` und `CHIRAL4D.MIRROR.SIGNED.CAR.01` bewahren die jeweiligen Identifikations-, Grenz- beziehungsweise Physikgrenzen.

## 2. Was genau B ist — und die scharfe Definitionsgrenze

Hier ist B weder der volle Hamiltonoperator noch eine beliebige positive Antwortform, sondern der **relative beschränkte Materiekoeffizient** gegenüber dem festgehaltenen freien Block \(\mathrm{diag}(A,3I)\):
\[
B(A,D)=\begin{pmatrix}A^2/4&A/2\\A/2&D-3I\end{pmatrix},
\quad A=A^*,\ D=D^*\in\mathcal B(\mathcal H).
\]
Der unbeschränkte elektrische Hamiltonoperator gehört nicht zu D. Gefordert wird Positivität auf dem vollständigen Koeffizientenraum, nicht nur in einem ausgewählten Gausszustand oder räumlich abgeschnittenen Fenster.

**Schärfung des bestehenden Satzes.** Sei \(P\) die orthogonale Projektion auf \(\overline{\mathrm{ran}A}\) und \(Q_0=I-P\) die Projektion auf \(\ker A\). Dann gilt allgemein
\[
\boxed{B(A,D)\ge0\iff D\ge3I+P.}
\]
Denn
\[
\langle(x,y),B(x,y)\rangle
=\|Ax/2+Py\|^2+\langle y,(D-3I-P)y\rangle.
\]
Die Norm lässt sich für jedes y durch geeignete x beliebig klein machen, weil \(Py\in\overline{\mathrm{ran}A}\). Dies beweist die notwendige Ungleichung; die hinreichende folgt direkt. Eine Kommutation von A und D wird nicht gebraucht.

Erst bei \(\ker A=0\), also dichtem Bild, wird daraus \(D\ge4I\). Eine **beschränkte Inverse wird nicht benötigt**. Der bestehende globale Bericht behandelt diese Voraussetzung korrekt und beweist sie für den vollen Rotor-Multiplikationsoperator auf geraden kubischen Tori mit unabhängigen Linkphasen.

Mit \(D\ge4I\) und einem vollständigen operatorwertigen Ortsbudget \(D_{xx}=4I\) folgt \(D=4I\): Der positive Operator \(K=D-4I\) hat nur verschwindende Diagonalblöcke; \(K^{1/2}\) verschwindet auf jeder Ortsuntermenge, also überall. Eine treue endliche Spur mit gleichem Gesamtbudget genügt ebenfalls. Eine asymptotische Spurdichte allein reicht nicht.

**Exakter Kontrollfall ohne Injektivität.** Sei C die Adjazenz des ungewichteten Viererrings, \(A=C/12\), \(P=C^2/4\) und \(D=3I+2P\). Dann ist P eine Rang-2-Projektion, alle Ortsdiagonalen von D sind vier und B ist positiv; trotzdem besitzt \(D-4I\) Eigenwert −1. Das verletzt keinen bestehenden globalen Satz: Es handelt sich um einen singulären festen Hintergrund. Es widerlegt die verkürzte Aussage ohne Dichtevoraussetzung sogar bei \(\|A\|=1/6\).

## 3. Cap und Parent: richtige Faktoren, verbleibende Inputs

Setze \(u=\eta\otimes\eta\), \(v=m^*\eta=\sum_a e_a\otimes e_{-a}\). Dann
\[
\|u\|^2=1,\quad\langle u,v\rangle=1,\quad\|v\|^2=4,
\quad\|v-u\|^2=3.
\]
\(m^*/2:Q\to Q\otimes Q\) ist eine Isometrie; \(m/2\) ist ihre **Coisometrie**, keine Isometrie auf dem 16-dimensionalen Definitionsraum. Der normierte Cap ist \(v/2\). Wer diesen ohne Neukalibrierung statt v einsetzt, verändert die Hoch- und Kreuzblöcke.

Für bereits festgelegtes beschränktes A und positive Skalen s,t setze
\[
C_L=s\,u\otimes A,\qquad C_H=t\,v\otimes I.
\]
Dann ist
\[
\mathrm{diag}(A,0)+(C_L,C_H)^*(C_L,C_H)
=\begin{pmatrix}A+s^2A^2&stA\\stA&4t^2I\end{pmatrix}.
\]
Der Anhang setzt korrekt \(s=1/2,t=1\). So entsteht genau der genannte Parent, alternativ als \(\mathrm{diag}(A,3I)+(A/2,I)^*(A/2,I)\). Die Zerlegung \(4=1+3\) ist damit algebraisch vollständig nachvollziehbar.

Sie wählt aber weder A noch s und t aus. Bei bezeichneten Koeffizienten \(\beta=s^2,\eta=st\) folgt nur die relationale Vorhersage \(M\beta=4\eta^2\). In ursprünglichen Linkkoeffizienten gilt \(Mc_{\rm hop}=4b^2\). Die nativen Zahlen erfüllen dies; \(c_{\rm hop}\) darf nicht durch den bereits hochsektorreduzierten Spektralkoeffizienten ersetzt werden.

## 4. Neuer Gegenzeuge: gleicher Parent, anderer markierter Strom

Im **gleichen unveränderten Q-System** wähle als alternativen hohen Quellvektor
\[
w=\sum_{a=0}^3(-1)^a e_a\otimes e_{-a}.
\]
Er hat genau wie v Normquadrat vier, Einheitsamplitude eins, neutralen Gesamtgrad und Symmetrie beim Vertauschen der beiden Schenkel. Für die Z₄-Gradmarkierung \(Re_a=i^ae_a\) sind beide invariant unter \(R\otimes R\).

Behält man den niedrigen Strom bei und ersetzt ausschließlich \(C_H=v\otimes I\) durch \(w\otimes I\), bleibt **die gesamte Parent-Grammatrix identisch**. Auch sämtliche ausschließlich aus diesem h und demselben Materiezustand berechneten Hamiltonantworten sind dadurch identisch.

Die Quellströme sind dennoch als markierte Prozesse unterscheidbar. Mit \(Le_a=e_{a+1}\), \(S=L\otimes L^{-1}\) gilt
\[
Sv=v,\qquad Sw=-w.
\]
Für den selbstadjungierten Prozessleser \(Y=(S+S^*)/2\) folgt
\[
\langle v/2,Yv/2\rangle=+1,
\qquad\langle w/2,Yw/2\rangle=-1.
\]
Der Balancierungsdefekt von w hat Normquadrat 16. **Gleiche Norm, Grade, Einheit und Hamiltonian reichen nicht, um den Quellprozess zu identifizieren.** Dies ist ein algebraischer Instrument-/Stromgegenzeuge, keine behauptete zusätzliche physische Messmöglichkeit in TFPT: Ob Y physisch realisiert wird, gehört gerade zum fehlenden Intertwiner.

w erfüllt das vollständige Frobenius-Balancierungsgesetz nicht. Unter Neutralität, \(Sw=w\) und Einheitsamplitude eins ist v eindeutig. Somit widerlegt der Gegenzeuge nicht die Cap-Eindeutigkeit; er identifiziert die zusätzlich zu prüfende Markierung.

## 5. Der schärfste unmittelbar ausführbare Herkunftstest

Zuerst muss ein Kandidat **tatsächliche native physische Operatoren und deren Definitionsbereiche** für beide Cap-Schenkel, Einheit, Grad, Verschieber und hohe/niedrige Ströme nennen. Ein nachträglich angehängtes \(\mathbb C^4\) mit passend definierten Strömen erfüllt nur das algebraische Bauprinzip.

Für einen angegebenen Kandidaten sind dann folgende endliche Residuen bereits entscheidend:

1. Isometrie und markierte Einheit; positive Paarung auf den wirklichen Quell-/Zielräumen.
2. Produkt-/Adjunkt-Erhaltung sowie **separate** Intertwining-Identitäten für Grad und primitive Verschieber. Der Y-Leser oben ist eine besonders scharfe notwendige Kontrolle; vier Normen allein sind unzureichend.
3. Identifikation der vollen niedrigen, gemischten und hohen Strommatrix, einschließlich \(Mc_{\rm hop}=4b^2\) und ambienter Randwege.
4. Gauge-, Paritäts- und CAR-Identitäten auf einer gemeinsamen invarianten Domäne; anschließend Generator-Intertwining auf einem angegebenen Kern des elektrischen Hamiltonoperators. Matrix-Gramgleichheit ersetzt diese Schritte nicht.

Die native CAR-Leiter besitzt bei der zweiten Stufe die Clock-Sektordimensionen \((6,4,2,4)\). Ein unitärer Verschieber, der auf dem **gesamten** Raum alle vier Sektoren zyklisch vertauscht, ist deshalb unmöglich. Das ist kein Verbot einer geeigneten Einbettung oder asymptotischen Q-System-Korrespondenz, aber ein sofortiger Kill-Test gegen eine allzu einfache volle Raumidentifikation. Die in der Quelle verwendeten gewichteten Quasibasen dürfen nicht durch vier ungewichtete Gruppenoperatoren ersetzt werden.

Im Anhang bedeutet „falls der Intertwiner nicht gelingt“ noch kein bewiesenes Scheitern der Route. Ein expliziter widersprechender Invariant tötet die geprüfte Kandidatenklasse; ein noch nicht konstruierter Intertwiner bleibt eine offene Aufgabe. GNS und Spektralgeometrie können die fehlenden Eingangsdaten nicht automatisch auswählen.

## Quellen- und Prüfgrenze

Aktueller Codegraph für v125, v1027, v779 verwendet; gezielte native Originale, vollständige heutige Cap-/Globalberichte sowie drei vollständige Ledgerzeilen geprüft und gehasht. Keine Vollsuche durch alle historischen Ansätze, kein nativer Kampagnen-/Suite-Lauf, kein Beweis negativer globaler Nicht-Existenz. `check_cap_review.py` importiert keine TFPT-Dateien und bestätigt **30 exakte Kontrollen**, einschließlich beider Cap-Normierungen, vollständiger Grammatrizen, neuer gemischter Prozessantwort, allgemeiner Kernelgrenze anhand des singulären Kontrollfalls und nativer Skalenrelationen. Die allgemeinen Operatorsätze werden oben argumentiert und nicht aus der Anzahl dieser Beispielkontrollen abgeleitet.
