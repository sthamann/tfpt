# Nachprüfung der beiden zuletzt eingegangenen Untersuchungen

Integrierter Nachtrag zu v1.6.5 · 15. September 2026

Quellen: die Anlagen `8e110ae1-19e2-4d47-bfc8-ebe4fe9ab81b` und
`b928b72a-6669-4c67-a75d-124095791c6f`, unverändert eingefroren. Zusätzlich
wurden die vier genannten Programme `t1_fixed.py`, `stabilizer.py`,
`t5_twobank.py`, `t5_varresp.py` vollständig gelesen und archiviert. Eine
eigene Nachrechnung prüft die kritischen Folgerungen; sie ist **kein
vollständiger Replay aller sechs Sonden** des fremden Arbeitsordners.

## 1. Übersicht: übernehmen, korrigieren oder offenlassen

| Neue Aussage | Ergebnis der Prüfung |
|---|---|
| Innerer Viererzyklus erhält alle 60 W-Kanäle | Bestätigt, jetzt einschließlich der richtigen Fermion-Vorzeichen und explizitem Bosonlift |
| Grundzustandseindeutigkeit/Singulett/Gaplücke weiterhin unbekannt | Überholter Stand: unter dem festgelegten nativen Vertrag bereits bewiesen; voller Vektor weiter unbekannt |
| Leerer Grundzustand für alle μ≥0 | Falsch; bei μ=0 liegt der eindeutige N=64-Grundzustand unter −1,129636Δ |
| Kommutant 7 als absolute Untergrenze | Nur im benannten blocktreuen erweiterten Operationsvertrag; siehe Hauptbericht Abschnitt 8 |
| Beliebige Einteilchenmatrix ist damit als natives Fock-Wort verfügbar | Nicht gezeigt; assoziative Matrixalgebra, Lie-Kontrolle und Fock-Lift sind verschiedene Fragen |
| Kanal-Variationszustand hat E=−0,0196Δ | Die angegebene Phase im Code ergibt gegen den gepinnten P=f_jf_i-Vertrag +0,05736Δ; ein relatives Vorzeichen korrigiert es |
| 99,892-%-Transfer bei t≈2484 | Numerisches Maximum eines Vierzustands-Paarmodells im untersuchten Zeitfenster; kein erster/globaler exakter Maximalsatz und kein nativer Einloch-Transfer |
| Gleiche Zweigableitungen genau bei ε=0 | Algebraisch richtig; die Eigenwertlücke bleibt dort √32·|g|, also kein allgemeiner „Kegel genau dann wenn gaplos“-Satz |
| SU(4)³-Anomalie =16 | Richtig unter A(4)=1 und der zusätzlichen Interpretation aller (16,4) als gleichhändige Weylfelder; Eichung ist eine weitere Voraussetzung |
| Gravitationsanomalie =64 | Keine reine perturbative Gravitationsanomalie in 3+1D; 64 kann bei zusätzlich deklarierter gleichgeladener U(1) die gemischte U(1)-Gravitationsanomalie zählen |
| Mit einer Ableitung kein (1,1)-Tensor bei Dimension ≤4 | Falsch: der Energie-Impuls-Tensor ist ein Gegenbeispiel; daraus folgt aber noch kein dynamisches Graviton |
| Kein lokaler kovarianter kinetischer Term für (1,0) | Zu pauschal: der bilineare Ein-Ableitungs-Term fehlt, ein Zwei-Ableitungs-Skalar existiert; Positivität/Constraints/Herkunft bleiben zu prüfen |

„Negativ geschlossene Route“ bedeutet nicht „T2, T3, T4 oder T7 geschlossen“.
Ein ausgeschlossener Ansatz beantwortet nicht die jeweilige physikalische
Existenzfrage. Die beiden gelieferten Texte widersprechen sich vor allem
beim bereits bewiesenen modellinternen Grundzustand; sie dürfen nicht als
gleichzeitig aktueller einheitlicher Status zitiert werden.

## 2. Positiver neuer Anschluss: der korrekt angehobene Viererzyklus

Die Abbildung der Fermionmarken lautet
\(p(4s+a)=4s+(a+1\bmod4)\). Auf Paaren ist zwingend das Exteriorvorzeichen
zu beachten: Falls \(p(i)>p(j)\), erhält das sortierte Paar ein Minuszeichen.
Der gelieferte `stabilizer.py` lässt dieses Zeichen weg. Das wäre im
Allgemeinen falsch; für den untersuchten Viererzyklus überlebt das positive
Resultat jedoch auch den korrekten Test.

Alle 60 W-Zeilen werden mit ihren Vorzeichen wieder auf W-Zeilen abgebildet.
Wir haben den zugehörigen signierten Bosonoperator \(R_b\) explizit gebildet
und exakt geprüft:

\[
 W'=R_bW,\qquad R_bR_b^T=I_{60},\qquad R_b^4=I_{60},
 \qquad R_b^2\ne I_{60}.
\]

Damit existiert ein **gemeinsamer nativer Tensor-Automorphismus** auf
Fermionen und Bosonen, nicht nur eine Übereinstimmung von Zeilenzahlen.
Die gleichzeitige Transformation erhält Paarwechselwirkung und Bosonzahl.
Sie beweist eine Ordnung-vier-Symmetrie, nicht deren operative Verfügbarkeit.

Dieser Permutationszyklus ist nicht die zentrale Matrix \(iI_4\) von SU(4).
Seine Determinante auf dem Viererfaktor ist −1. Mit einer zusätzlichen
Ladungsphase kann man geeignete Gruppenlifts vergleichen; die Permutation,
die zentrale Phase, der Clock und die geometrische Glue-Markierung sind
dadurch aber nicht schon identifiziert. Genau diese Intertwiner-Frage ist
ein sinnvoller neuer Anschluss, statt noch einmal nur vier zu zählen.

## 3. Warum der Einteilchen-Abschluss den Fock-Operationssatz nicht schließt

Die Irreduzibilität der Einteilchendarstellung kann ihre assoziative
Matrixalgebra zu \(B(\mathbb C^{64})\) machen. Daraus folgt nicht, dass jede
Matrix als ein zulässiges physisches Wort verfügbar ist, und auch nicht,
dass ihre zweite Quantisierung bereits erzeugt wird.

Ein kleinstes exaktes Gegenbeispiel zur falschen Liftregel:
\(A=|1\rangle\langle1|\), \(B=|2\rangle\langle2|\) auf zwei Moden.
Dann \(AB=0\), also \(d\Gamma(AB)=0\), aber
\(d\Gamma(A)d\Gamma(B)=n_1n_2\ne0\).
Der zweite Quantisierungsschritt ist ein Lie-, nicht ein assoziativer
Algebra-Homomorphismus dieser Art.

Auch \(\operatorname{diag}(i,1,1,1)\) und
\(\operatorname{diag}(i,i,1,1)\) haben Determinanten i beziehungsweise −1.
Ihre Zugehörigkeit zur **linearen Matrixalgebra** aus SU(4)-Generatoren und
Identität ist kein exaktes SU(4)-Gruppenwort. Projektive Gleichheit oder eine
zusätzliche U(1)-Phase kann helfen, muss aber mit der Bosonwirkung, Ladung
und Referenz gemeinsam ausgewiesen werden.

Der fremde Code folgert außerdem die Irreduzibilität des 37.888-dimensionalen
dunklen Dreifermionraums aus der vollen Einteilchenmatrixalgebra. Diese
Schlussregel ist nicht begründet. Bereits die im anderen neuen Text
angegebenen drei dunklen irreduziblen Typen widersprechen der pauschalen
Eins-Block-Lesart unter der bloßen Quellsymmetrie. Die Zahl 8.732.673 mag als
sehr schwache obere Schranke anderweitig verträglich sein; die im Code
angegebene Herleitung belegt sie nicht. Die SVD-/Toleranzprüfungen des Codes
sind zudem numerisch, nicht allein wegen „PASS“ exakte Lie-Beweise.

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und
positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette
Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig;
Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg.
Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

Das grobe Sandwich \([-1.2,-.0196]\Delta\) ist nach einer Phasenkorrektur
zwar verträglich, aber wesentlich schwächer als
\((-1.158089,-1.129636)\Delta\). Es ist keine Verschärfung.

Im tatsächlich angegebenen Variationscode werden die Fermionen in der
Reihenfolge j, dann i gelöscht. Das liefert \(f_if_jF=-f_jf_iF\), während
der native Vertrag \(P_A=\sum W_{A,ij}f_jf_i\) verwendet. Bei unverändertem
\(g=+\Delta/20\) und den angegebenen Variationskoeffizienten folgt deshalb

\[
 E_{\rm Code}/\Delta=\frac12-\frac{23\sqrt3}{90}
 =+.057364793621\ldots,
\]

nicht der behauptete negative Wert. Mit korrigierter relativer Phase lautet
er \(1/2-3\sqrt3/10=-.019615242271\ldots\). Alternativ wäre eine konsequente
andere P/g-Phasenkonvention möglich; die Quelle muss sie dann überall führen.
Die gleichzeitige Einteilchendichte des einfachen Variationszustands bleibt
von dieser Phasenreparatur unberührt, weil seine Bosonzahlkomponenten
orthogonal sind. Sie ist keine dynamische Greenfunktion auf dem nativen
Grundzustand und ersetzt dessen schon kontrollierte Antwort nicht.

## 5. Feldtheorie: falsche Verbote entfernen, echte Bedingungen behalten

### 5.1 Anomalien

Für die zusätzlich angenommene 3+1D-Weylinterpretation lautet das lokale
Anomaliepolynom bis auf Konventionsvorzeichen

\[
 I_6=[\widehat A(T)\,\mathrm{ch}_R(F)]_6
 =\mathrm{ch}_3(F)-\frac{p_1(T)}{24}\,\mathrm{ch}_1(F).
\]

Der reine gravitative Anteil \([\widehat A]_6\) verschwindet; seine
Formgrade sind Vielfache von vier. Das ist die bekannte dimensionale
Unterscheidung bei [Álvarez-Gaumé und Witten](https://collaborate.princeton.edu/en/publications/gravitational-anomalies/).
Eine Spur-/Weylanomalie ist nochmals ein anderer Begriff.

Auf (16,4) ist der SU(4)-Kubikkoeffizient 16 bei Normierung A(4)=1.
Der exakte Test \(t=\operatorname{diag}(1,1,1,-3)\) hat
\(\operatorname{tr}t=0\), \(\operatorname{tr}t^3=-24\).
Ist SU(4) **dynamisch geeicht**, muss die vollständige Theorie diese
Eichanomalie kompensieren. Als globale Symmetrie kann sie eine
't-Hooft-Anomalie tragen; dann folgt keine pauschale Spiegelpflicht.
Ein vollständiger konjugierter Spiegel ist ein möglicher Ausgleich,
aber hier nicht als einzige oder allgemein minimale Lösung bewiesen.

„Gravitativ 64“ kann sinnvoll eine **gemischte U(1)-Gravitationsanomalie**
meinen, wenn alle 64 linksgetragenen Weylfelder explizit U(1)-Ladung eins
erhalten. Das muss samt Eich-/Globalstatus gesagt werden. Für SU(4) allein
ist der gemischte lineare Spurkoeffizient null. Die Quellenmarke N darf
nicht ohne Beweis in eine dynamisch geeichte chirale U(1) umgedeutet werden.

### 5.2 Der behauptete Spin-2-Ausschluss ist falsch

Die Lorentzdarstellungen liefern exakt

\[
 (\tfrac12,\tfrac12)\otimes(\tfrac12,\tfrac12)
 =(0,0)\oplus(1,0)\oplus(0,1)\oplus(1,1).
\]

Eine Ableitung des Vektorbilinears \(\psi^\dagger\bar\sigma_\mu\psi\)
kann daher einen symmetrischen spurfreien (1,1)-Tensor bilden. Insbesondere
hat der Energie-Impuls-Tensor
\(T_{\mu\nu}\sim i\psi^\dagger\bar\sigma_{(\mu}
\overleftrightarrow\partial_{\nu)}\psi\), mit passender Spurbehandlung,
Dimension \(3/2+3/2+1=4\). Ein Energie-Impuls-Tensor kann bereits in einer
festen Hintergrundraumzeit definiert werden; dynamische Diffeomorphismen
müssen nicht vorausgesetzt werden, um dieses Gegenbeispiel zu formulieren.

Das schließt **T7 nicht**. Ein vorhandener Tensor ist kein masseloser
Spin-2-Pol. Das sinnvolle Ziel ist später sein transversaler, spurfreier
Korrelator auf demselben räumlichen Parent, mit positiver Norm, beiden
Helizitäten und universeller Kopplung. Wir entfernen hier eine falsche
Darstellungsobstruktion, nicht die dynamischen Nachweispflichten.

### 5.3 (1,0)-Kinetik ist nicht generell verboten

Der bilineare Ein-Ableitungs-Term mit einem (1,0)-Feld und seinem Adjungierten
besitzt keinen Lorentzskalar. Mit zwei Ableitungen existiert aber etwa

\[
 \mathcal L_2\propto
 (\partial^{\alpha\dot\alpha}\Phi_{\alpha\beta})
 (\partial^{\beta\dot\beta}\bar\Phi_{\dot\alpha\dot\beta})
\]

für symmetrisches \(\Phi\). Alle Spinorindizes sind kontrahiert. Bei rein
zeitartigem Impuls ist sein Symbol proportional zu
\(\omega^2(|\Phi_{11}|^2+2|\Phi_{12}|^2+|\Phi_{22}|^2)\), also nicht
identisch null. Das ist ein Gegenbeispiel zum uneingeschränkten Satz „kein
lokaler kovarianter kinetischer Term“. Es beweist **nicht** Positivität des
vollen Hamiltonoperators, korrekte Constraints, gewünschte Freiheitsgrade
oder eine native Quelle. Diese bleiben die entscheidenden Tests.

## 6. Die Vierzustandsrechnung richtig lesen

Das Modell mit \(s=\sqrt8g\), Bosonverbindung η und Diagonalen (0,Δ,Δ,0)
erlaubt kohärenten **Paartransport**. Die exakte Identität
\((H^3)_{41}=8g^2\eta\) stimmt. Unsere unabhängige Fließkomma-Abtastung
reproduziert auf \([0,3000]\) mit Schrittweite .05 den größten gefundenen
Wert .998920021869 bei 2484.05. Der erste Gitter-Lokalhöchstwert liegt
bereits bei 6.05. Weder „erster Maximalzeitpunkt“ noch ein globales exaktes
Maximum ist damit bewiesen. Diese kleine Rechnung wird nicht mit dem
vollständigen Einloch-Satz des Hauptberichts verwechselt.

Für \(F_\pm(\epsilon)=(\epsilon\pm\sqrt{\epsilon^2+32g^2})/2\)
gilt \(F'_+-F'_-=\epsilon/\sqrt{\epsilon^2+32g^2}\). Bei ε=0 stimmen
die Ableitungen überein, aber die **Eigenwertlücke** beträgt
\(\sqrt{32}|g|>0\). Ein verschwindender nackter Vermittlerparameter und
eine verschwindende wechselwirkende Anregungslücke sind verschieden.
Ein allgemeiner relativistischer Kegelsatz oder ein zwingendes neues
Renormierungsprogramm folgt aus dieser Ableitungsidentität nicht.

## 7. Konsequenz für die nächste Forschungsrevision

Die sinnvollen positiven Anschlüsse sind jetzt schärfer:

1. Den expliziten Ordnung-vier-Lift mit dem tatsächlich markierten Clock
   und der Herkunft des A3-Index vergleichen: vollständige Intertwiner,
   Ladungsphase und Bosonwirkung, nicht nur Gruppennamen.
2. Einen Quellenoperator finden, der die lokale Parität beider operational
   bestimmten Teile gleichzeitig ändert. Die native Z4-Symmetrie selbst
   tut das nicht. Der kontrollierte Einloch-Transfer ist bereits als
   Akzeptanztest für einen solchen Operator verfügbar.
3. Den Zwei-Ableitungs-Feldkandidaten auf Positivität und Constraints prüfen,
   bevor er als relativistischer Adapter zählt. Ein bloßes Nichtnull-Symbol
   ist noch keine gesunde Feldtheorie.
4. Den Energie-Impuls-Tensor als zulässigen **Kandidaten** behalten, aber erst
   auf dem gemeinsam konstruierten räumlichen Träger nach einem dynamischen
   Spin-2-Pol suchen. Kein vorhandener Spin-2-No-go rechtfertigt hier das
   Aufgeben dieses Anschlusses.

62 zusätzliche Prüfbedingungen bestehen normal und optimiert identisch.
Exakte Identitäten, bedingte Darstellungsargumente und die numerische
Zeitfenstersuche sind im Ergebnisbericht getrennt. Der externe Status
„alle Restfragen geschlossen oder auf genau ein Stück reduziert“ wird
nicht übernommen. Die vollständige TOE bleibt offen.
