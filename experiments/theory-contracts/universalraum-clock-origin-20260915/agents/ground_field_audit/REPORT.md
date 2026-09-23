# Unabhängige Prüfung: Krylov-Verzweigung und Feldwörterbuch

Arbeitsstand 2026-09-15. Geprüft wird die Anlage `7380c383-f364-4ef8-8066-24aa4d180d85` gegen den Vertrag `universalraum-native-operations-ground-response-20260915`. Fremde Quellen und Ausgaben wurden nicht verändert. Die hier angegebenen Matrix- und Graphbefunde beziehen sich auf denselben gepinnten Tensor W mit SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

## 1. Der neue Nichtschluss ist exakt bestätigt

Für `v_n=(T†)^n F` habe ich `u=T T† v_2=T v_3` unmittelbar aus den 480 nativen Paaren neu kontrahiert. Das materialisiert nicht die 15.252.960 Komponenten von v₃. Es arbeitet mit 108.240 Komponenten von v₂ und 293.280 nichtverschwindenden Komponenten des Ergebnisses u. Es wurden 45.771.360 zulässige Erzeugungsübergänge und 139.289.760 anschließende Entnahmebeiträge exakt mit ganzzahliger Fermion-Parität und Boson-Multiplizität zusammengeführt.

Die unabhängige Rechnung liefert

\[
\|v_2\|^2=439680,\quad
\langle v_2,u\rangle=575078400,\quad
\|u\|^2=752194252800.
\]

Damit folgen rein rational

\[
\alpha=\frac{299520}{229},\qquad
w_2=u-\alpha v_2,\qquad
\|w_2\|^2=\frac{5001523200}{229}>0,
\]

und

\[
\frac{\|w_2\|^2}{\nu_3}=\frac{1809}{47632}.
\]

Der Ein-Vektor-pro-Bosonlage-Ansatz ist somit nicht invariant. Da T die native Symmetrie erhält und v₂ und u Singuletts sind, liefert w₂ einen zweiten unabhängigen Singulettvektor in derselben Bosonlage. Das ist ein Strukturresultat, kein physikalischer Mehrteilchen- oder Raumzeitnachweis.

## 2. Das mitgelieferte Ground-JSON ist veraltet und teilweise falsch

Die aktuelle Pythonquelle hat SHA-256 `8ae0f2f103ba0cb0a5cb832681a33130b6756fe627395368b6be635587a2eb02`. Das vorhandene `native_ground_state.json` nennt dagegen `046ffa3f41d9dd365e2c9a199e938734bf735d762f23373a3f85b541c3da30fe` und enthält noch

\[
\|w_2\|^2_{\rm alt}=1145348812800
=229^2\|w_2\|^2.
\]

Sein `closure_defect=1.5226768996658837` ist schon als relative orthogonale Norm unmöglich. Das daraus abgeleitete Ritz-Ergebnis −1,18826198 ist ungültig. Der spätere Anlagentext korrigiert den Normfehler, aber die JSON-Belegkette wurde noch nicht entsprechend neu erzeugt. Das grüne `status: PASS` dieser historischen Ausgabe darf deshalb nicht mit dem korrigierten Text zusammengezogen werden.

Die korrigierte Norm und die folgenden kleinen Matrizen wurden hier unabhängig reproduziert. Die ganze fremde große Ausführung wurde ausdrücklich nicht erneut gestartet.

## 3. Die sechste Dezimalstelle ist richtig — aber nur für die eine zusätzliche Richtung

Die neue numerische Diagonalisierung ergibt:

| g/Δ | vierdimensionale Ritz-Matrix | plus w₂ | Änderung |
| --- | ---: | ---: | ---: |
| 1/20 | −1,0942308394409612 | −1,0942318710142458 | −1,0315733·10⁻⁶ |
| 1/40 | −0,29535718178032033 | −0,29535720496683315 | −2,3186513·10⁻⁸ |
| 1/100 | −0,04789424798601009 | −0,04789424801311775 | −2,7107663·10⁻¹¹ |

Das sind numerische Eigenwerte exakter kleiner Ritz-Matrizen, keine nach außen gerundeten vollständigen Spektraleinschließungen. Durch Eliminieren der einzigen neuen w₂-Koordinate bekommt die v₃-Diagonale die exakt bestimmte energieabhängige Korrektur

\[
-\frac{g^2(1809/47632)}{2\Delta-E}.
\]

Das erklärt die kleine Änderung durch diesen einen Zweig. Es sagt nichts über die ausgelassenen höheren Bosonlagen.

### Eigene einfache Folgeherleitung: Das vollständige Ritz-Residuum

Sei ψ₃ der normierte Ritz-Eigenvektor in `span(v₀,…,v₃)`, und c₃ seine Komponente entlang `v₃/√ν₃`. Außerhalb dieses Raums führt Hψ₃ genau in zwei orthogonale Richtungen: v₄ und w₂. Deshalb gilt exakt

\[
\|(H-E_{\rm Ritz})\psi_3\|^2
=g^2|c_3|^2\frac{\nu_4+\|w_2\|^2}{\nu_3}.
\]

Hier wird `ν₄=952296652800` aus dem früher vollständig geprüften Momentbeleg übernommen; die vierte Ordnung wurde in dieser Runde nicht erneut enumeriert.

Bei g/Δ=1/20 folgt numerisch ein Residuum von rund **0,373063 Δ**. Der w₂-Zweig trägt weniger als **23 Millionstel** des quadrierten Residuums. Die große ausgelassene Richtung ist v₄, nicht w₂. Aus dem winzigen Nichtschlussanteil darf daher keine praktisch vollständige Konvergenz abgeleitet werden.

Außerdem liegt die neue Fünf-Zustands-Ritzenergie mindestens **0,0354 Δ über** der bereits bewiesenen Obergrenze des wahren Grundzustands. Das ist eine nachweislich noch relevante Lücke, unabhängig von einer Konvergenzschätzung.

## 4. Der bereits bewiesene native Grundsatz bleibt gültig

Der ältere, gepinnte Beweis lautet: Für Δ>0 und 0<|g|/Δ≤1/20 besitzt der unveränderte μ=0-Hamiltonoperator einen eindeutigen globalen Grundzustand in N=64; er ist ein Spin(10)×SU(4)-Singulett. Bei 1/20 bestehen außerdem positive Lücke und die bekannten Energie-, Besetzungs- und Polschranken.

Die neue Ausführung benutzt schwächere Sektor-Untergrenzen und weniger Ritz-Vektoren. Dass diese schwächere Methode bei 1/20 nicht genügt, ist weder eine Widerlegung noch ein Wiederöffnen des früheren Satzes. Insbesondere sind die vorgeschlagenen Ziele `E<−1,2Δ` bzw. `E<−1,1625Δ` unmöglich, weil bereits `E₀>−1,158089Δ` bewiesen ist. Bessere Schranken für die Konkurrenzsektoren sind erforderlich, nicht eine unrealistisch tiefere Energie.

Die neuen Zahlen `Nb≈0,84211266`, `Zh≈0,97368398` und `εh≈0,03107309Δ` gehören zum nichtstationären K₃-Ritz-Zustand. Nb liegt sogar knapp unter der früher bewiesenen Schranke `Nb(Ω)>0,842846`. Zh bezeichnet die gesamte Entnahmenorm dieser Näherung, nicht das Gewicht der isolierten niedrigen Linie. Ein erstes Moment auf einem Ritz-Zustand ist keine neu bestimmte Polenergie auf Ω.

Offen bleiben der vollständige Ω-Vektor, die physische Auswahl des μ=0-Vertrags und die Herkunft ausführbarer räumlicher Operationen.

## 5. Feldwörterbuch: bestätigte Algebra und notwendige Einschränkungen

Frisch exakt geprüft wurden:

- Der Trägergraph ist zusammenhängend, 15-regulär und dreiecksfrei.
- Der Fünf-Zyklus `16→45→0→30→37→16` liegt wirklich im Trägergraphen.
- Für jeden der 60 nativen Kanäle verschwindet der gleichhändige Ein-Kopie-Weyl-Skalaransatz `M_A⊗ε` als Grassmann-Bilinear.
- Bei Dirac-Kernen sind C, Cγ⁵ und alle vier Cγ^μγ⁵ antisymmetrisch; alle vier Cγ^μ und alle sechs Cσ^{μν} sind symmetrisch.
- Die 43 getesteten nichttrivialen Gradierungen ergeben genau die angegebenen Kanalzahlen 24/36, 40/20 bzw. 32/28. Die Stabilisatordimensionen 36, 52 und 28 wurden diesmal durch exakt diagonale reelle Gram-Matrizen der Kommutatorbedingungen bestätigt, nicht durch einen SVD-Schwellwert.

Der Fünf-Zyklus allein schließt nur eine diagonale ±-Händigkeitszuweisung aus, die an jedem Paar entgegengesetzte Händigkeiten verlangt. Er allein ist kein basisunabhängiger Ausschluss und kein Ausschluss zusätzlicher Feldkomponenten.

### Eigener stärkerer Satz: auch ein Basiswechsel repariert den Ein-Kopie-Vektoransatz nicht

Sei Γ eine hermitesche Händigkeit auf dem ursprünglichen 64-dimensionalen internen Raum. Für einen ausschließlich entgegengesetzt-händigen, unveränderten Paartensor müsste

\[
\Gamma^T M_A+M_A\Gamma=0\quad\text{für alle }A
\]

gelten. Adjungieren und Einsetzen zeigt

\[
[\Gamma,M_A^\dagger M_B]=0\quad\text{für alle }A,B.
\]

Die native Faktorisierung wurde exakt rekonstruiert:

\[
M_{k,a}=S_k\otimes C_a,\quad
\sum_k S_k^\dagger S_k=5I_{16},\quad
\sum_a C_a^\dagger C_a=3I_4.
\]

Daher muss Γ sowohl mit allen `S_k†S_l⊗I₄` als auch mit allen `I₁₆⊗C_a†C_b` kommutieren. Die von den ersten Produktmatrizen erzeugte Algebra ist die volle M₁₆; die zweite ist M₄. Hierfür enthält die Prüfung vollständige Rangzertifikate von ganzzahligen Matrixwörtern modulo 101: **256 unabhängige Spinorwörter bis Länge zwei und 16 unabhängige Farbprodukte bis Länge eins**. Voller Rang modulo einer Primzahl beweist vollen Rang über den komplexen Zahlen; es wird ausdrücklich keine Rangdefizienz von einem endlichen Körper übertragen.

Folglich ist Γ skalar. Die ursprüngliche Gleichung erzwingt dann Γ=0. Insbesondere gibt es **keine hermitesche Involution Γ²=I** mit der verlangten Eigenschaft. Diese Schlusskette schließt den Ein-Weyl-pro-Label-Vektoradapter jetzt unabhängig von einer Wahl der internen Basis aus.

Der Satz betrifft unveränderte W-Kanäle und unveränderten 64-dimensionalen Träger. Er schließt **nicht** Diracfelder pro Label, zusätzliche Kopien, Ableitungsadapter oder andere ausdrücklich erweiterte Modelle aus.

## 6. Die minimale Erweiterung darf nicht aus Versehen mit ausgeschlossen werden

Zwei explizite Gegenkontrollen wurden auf allen 60 Kanälen neu gerechnet:

1. **Vierkomponenten-Diracfelder pro Label:** `M_A⊗Cγ⁰` ist nichtverschwindend und antisymmetrisch im gesamten Grassmann-Index. Es enthält zusätzliche linke und rechte Freiheitsgrade pro ursprünglichem Label. Deshalb widerspricht es dem Ein-Kopie-Satz nicht. Eine chirale Standardmodell-Entstehung folgt daraus nicht.
2. **Unabhängige Zweier-Erweiterung:** `M_A⊗ε_aux⊗ε_Lorentz` ist nichtverschwindend und antisymmetrisch. Der skalare Kanal wird möglich, weil die zusätzlich antisymmetrische interne Zweierform die Symmetrie des internen Paarfaktors umkehrt. Das ist die bereits bekannte minimale Reparatur im deklarierten Tensorprodukt-Ansatz, keine aus der Quelle hergeleitete Verdopplung.

Eine solche Zweier-Erweiterung macht auch den Trägergraphen durch `M_A⊗σ_x` bipartit: `Γ=I₆₄⊗diag(1,−1)` antikommutiert exakt mit allen so erweiterten Matrizen. Damit ist sichtbar, welche zusätzliche Ressource den ursprünglichen Ausschluss überwindet.

"Der Vermittler kann nie Skalar sein" muss folglich auf den unveränderten Ein-Kopie-Ansatz begrenzt werden. Ebenso fixiert Schur nur die interne Matrixstruktur innerhalb eines irreduziblen Blocks; es beweist nicht die Einzigartigkeit aller möglichen Lorentz- und Ableitungsterme. Eine gesunde Kinetik, Nebenbedingungen, Eichherkunft und ein dynamischer Spin-2-Sektor sind hier nicht konstruiert.

## Reproduktion und Status

`contracted_krylov.cpp` ist der unabhängige ganzzahlige Kontraktionskern. `verify.py` prüft diesen Kern, die korrigierte Pythagoras-Rechnung, kleine Ritz-Matrizen, sämtliche angeführten Graph-, Kern- und Gradierungsidentitäten sowie die Matrixalgebra-Zertifikate. Die Ergebnisse stehen in `audit.json` und `audit_optimized.json`.

Es bestehen **376 Prüfbedingungen: 371 exakte und fünf numerische**. Für eine eigenständige Reproduktion zuerst den kleinen C++-Kern mit C++17 und Optimierung übersetzen; anschließend `verify.py` normal und mit `-OO` starten. Sämtliche Eingaben liegen eingefroren unter `sources/`; die Ergebnisdateien enthalten ihre SHA-256-Werte. Fremde Pythonprogramme werden hierbei nicht ausgeführt. Die numerischen Ritz-Prüfungen sind als solche markiert, alle Algebra-Zertifikate und die vollständige direkte Kontraktion verwenden exakte Ganzzahl-/Bruchrechnung.

Beide abschließenden Ausführungen bestanden und lieferten byteidentische JSON-Dateien mit SHA-256 `148047028236a887de1b28a0a9c12d84037a7c633892abc51dd9047f0b7a7baf`.

Keine T1–T8-Abschlussbehauptung. Keine Änderungen an fremden Quellen, Hauptpaper, Webseite, Ledger oder Git-Historie.
