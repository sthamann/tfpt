# Eine höhere Antwort liest die Zusammensetzung aus

15. September 2026 · v1.6.9 · vollständiger eigener Kompositionsbeweis

## 1. Frage und Ergebnis

Kann die innere W-Struktur schon bestimmen, wie mehrere Vorkommen gemeinsam wirken? Für eine ausdrücklich erklärte, besonders einfache Familie lässt sich die Frage exakt beantworten: **Nein, nicht aus W und auch nicht aus dem gesamten Zweiladungsspektrum allein.** Die Dreiladungsantwort bestimmt jedoch genau die zusätzlich gewählte positive Kopplungsmatrix. Das ist ein konstruktiver Anschluss für die vom Benutzer vorgeschlagene Rückrechnung aus „Schatten“.

Es handelt sich um zwei Aussagen innerhalb einer festgelegten Modellklasse, nicht um eine allgemeine Unmöglichkeit jeder TFPT-Herleitung. Der globale Kopplungstensor ist hier Gegenmodelleingabe; seine compilerseitige Auswahl wurde nicht gefunden. Beide Gegenmodelle haben einen gemeinsamen globalen Träger und echte globale Hamiltonoperatoren.

## 2. Gemeinsame ursprüngliche Daten

Wir verwenden den unveränderten realen Tensor W mit 60 Kanälen und 2016 Fermionpaarspalten. Aus jeder Zeile wird eine antisymmetrische 64-mal-64-Matrix A_A: oberhalb der Diagonale steht W, unterhalb sein negatives Transponiertes. Direkt aus allen 480 Vertices folgt

\[
\tfrac12\operatorname{tr}(A_A A_B^\dagger)=8\delta_{AB},\qquad
\sum_A A_A^\dagger A_A=15I_{64}.
\]

Die native Dreifermion-zu-Boson-Fermion-Abbildung heiße \(T_0\). Ihr Gramoperator ist \(G_0=T_0T_0^\dagger\) auf 3840 Dimensionen. Sämtliche geordneten Fermiontripel und CAR-Vorzeichen werden neu aufgebaut. Es ergeben sich 29760 nichtverschwindende Einträge und das exakt kontrollierte Spektrum

\[
\operatorname{spec}(G_0)=\{0^{[64]},7^{[2880]},10^{[576]},12^{[320]}\}.
\]

Die Hochzahlen in eckigen Klammern sind Multiplizitäten. Der Prüfer kontrolliert das ganzzahlige annihilierende Polynom \(G_0(G_0-7I)(G_0-10I)(G_0-12I)=0\) und die rationalen Spektralprojektorspuren. Eine Zeilensummen-Normschranke sichert die benutzten int64-Produkte und Spuren gegen Überlauf ab; keine Gleitkomma-Eigenwerte begründen diese Aussage.

Setze

\[
K=8I_{3840}-G_0,\qquad \operatorname{tr}K=960.
\]

Unabhängig wird für alle 3600 Kanalblöcke exakt geprüft:

\[
K_{Ai,Bj}=(A_B A_A^\dagger)_{ij}.
\]

## 3. Ein zusätzlicher symmetrischer Kompositionstensor

Fermionen erhalten einen zusätzlichen L-dimensionalen Multiplizitätsfaktor; die 60 Bosonen bleiben **eine einzige gemeinsame Bank**. Wähle eine komplex-symmetrische Matrix C mit \(\operatorname{tr}(C^\dagger C)=1\). Die antisymmetrischen globalen Paarmatrizen lauten

\[
M_A=C\otimes A_A,\qquad
P_A(C)=\sum_{(x,i)<(y,j)}(M_A)_{xi,yj}f_{yj}f_{xi},
\]
\[
H_C=\Delta N_b+g\sum_A\bigl(b_A^\dagger P_A(C)+P_A(C)^\dagger b_A\bigr).
\]

Die innere Gruppe wirkt auf dem 64-Faktor, trivial auf der Multiplizität. Daher bleiben die nativen inneren Intertwiner, der diagonal geliftete Clock und \(N=N_f+2N_b\) erhalten. Die vollständige globale Paarabbildung hat für **jedes** solche C den Gramoperator \(8I_{60}\).

Wichtig: Hier bleibt die global normierte Paarantwort gleich. Die einzelne Kopie trägt im Allgemeinen **nicht** jeden lokalen W-Koeffizienten mit unveränderter Stärke g. Genau darin unterscheidet sich diese Familie vom Zwei-Chart-Modell des Quellenstrangs, das jede lokale W-Kopplung unverändert lässt, dafür aber zwei Bosonbanken hat. Beide Klassen prüfen unterschiedliche Eindeutigkeitsbehauptungen und werden nicht vermischt.

## 4. Gleiche vollständige Zweiladungsspektren, unterschiedliche globale Dynamik

Zwei einfache Familien sind

\[
C_{\rm verteilt}=\frac{I_L}{\sqrt L},\qquad
C_{\rm kollektiv}=\frac{J_L}{L},
\]

wobei J_L die Matrix aus lauter Einsen bezeichnet. Beide sind symmetrisch, normiert, invariant unter Permutation der Kopien und stimmen für L=1 mit dem nativen Modell überein. Sie liefern jedoch verschiedene spätere Physik. Permutationssymmetrie ist dabei keine geometrische Lokalität.

Auf N=2 besteht H_C aus 60 identischen hellen Zweierblöcken mit Kopplung \(\sqrt8g\), ergänzt um \(\binom{64L}{2}-60\) dunkle Paarzustände. Bei festem L sind deshalb die **gesamten** N=2-Hamiltonspektren einschließlich sämtlicher Multiplizitäten gleich, nicht nur die hellen Pole. Die Bezeichnung „gleiches Spektrum“ enthält keine Gleichheit aller markierten Präparationen und Instrumente.

Für L=2 hat dieser Sektor 8188 Dimensionen: 8128 Fermionpaare und 60 Bosonen, mit 8068 dunklen Paarzuständen. Die primitive Kopplungsmetrik ist dagegen

\[
\sum_A M_A^\dagger M_A=15(C^\dagger C)\otimes I_{64}.
\]

Der verteilte Fall hat keinen vollständig abgekoppelten primitiven Fermionmodus, der kollektive Fall hat 64 davon. Für allgemeines L sind es im kollektiven Fall 64(L−1). Dies zeigt bereits eine andere CAR-Kopplungsstruktur. Ein stärkerer, nicht auf markierte Einzelmoden angewiesener Zeuge ist das folgende vollständige N=3-Spektrum.

## 5. Allgemeine CAR-Identität auf N=3

Bezeichne die globale Dreifermion-zu-Boson-Fermion-Abbildung mit \(T_C\). Die Boson-Fermion-Zeilen werden als \((x,A,i)\) angeordnet. Aus der Paar-CAR-Kontraktion folgt

\[
\boxed{G_C^{(3)}:=T_CT_C^\dagger
=8I_L\otimes I_{3840}-(C^\dagger C)\otimes K.}
\]

Für die gewählte Vernichtungskonvention ist der Sitefaktor **C†C**, nicht CC†. Aus dem Austauschterm folgt komponentenweise

\[
\sum_z\overline{C_{xz}}C_{yz}
=(\overline C C^T)_{xy}=(C^\dagger C)_{xy},
\]

weil C symmetrisch ist. Der direkte Term ist wegen der Frobeniusnormierung 8I. Der innere Austauschblock ist genau das oben unabhängig geprüfte K. Das beweist die allgemeine Identität. Für reelles C sind beide scheinbar verschiedenen Konventionen identisch; deshalb wird zusätzlich ein komplexes Gegenbeispiel \(C=\left(\begin{smallmatrix}1&i\\i&0\end{smallmatrix}\right)/\sqrt3\) durch vollständigen CAR-Aufbau geprüft. Reale und imaginäre Teile werden separat ganzzahlig multipliziert.

Sind γ die Eigenwerte von C†C und λ die von G_0, so sind die Eigenwerte des globalen Gramoperators

\[
8-\gamma(8-\lambda),
\]

mit den entsprechenden Produktmultiplizitäten. Bei L=2 ergibt sich:

| Fall | Vollständiges Spektrum von \(G_C^{(3)}\) |
|---|---|
| Verteilt | 4 [128]; 15/2 [5760]; 9 [1152]; 10 [640] |
| Kollektiv | 0 [64]; 7 [2880]; 8 [3840]; 10 [576]; 12 [320] |

Der Prüfer baut beide Abbildungen auf allen \(\binom{128}{3}=341376\) Dreifermionzuständen und 7680 Boson-Fermionzuständen direkt auf. Die zugrundeliegenden vollständigen N=3-Hamiltonoperatoren haben jeweils 349056 Dimensionen. Die Rechnung braucht nur dünn besetzte Gramoperatoren, keine große dichte Diagonalisierung.

Für Δ>0 und g≠0 ist der Eigenraum von H_C bei der **exakten** Energie Δ isomorph zu \(\ker G_C^{(3)}\). Denn die Eigenwertgleichungen lauten für Paarteil u und Bosonteil v

\[
gT_C^\dagger v=\Delta u,\qquad gT_Cu=0.
\]

Daraus folgen \(G_C^{(3)}v=0\), dann \(T_C^\dagger v=0\) und u=0. Also hat das verteilte Modell **keinen** solchen Zustand, das kollektive Modell **genau 64**. Beide gesamten N=3-Spektren sind verschieden. Eine Umbenennung von Ports oder eine passive Basiswahl kann diesen spektralen Unterschied nicht entfernen.

## 6. Positive Rückrechnung: der Schatten bestimmt Q

Die obige Identität lässt sich tatsächlich invertieren. Mit \(Q=C^\dagger C\) gilt

\[
\boxed{Q=\frac1{960}\operatorname{Tr}_{\mathbb C^{60}\otimes\mathbb C^{64}}
\left(8I-G_C^{(3)}\right).}
\]

Der Teiltrace ist **unnormiert** und lässt den Kopienfaktor stehen. Die Zahl 960 ist die exakt aus W gerechnete Spur von K. Für beide vollständigen L=2-Gegenmodelle wird Q eintragsweise aus dem direkt aufgebauten Gramoperator wiedergewonnen.

Das ist die gesuchte Art von Brücke: Eine höhere dynamische Antwort verrät etwas über die gemeinsame Zusammensetzung, das die gesamte niedrigere Spektralantwort nicht verrät. Sie liefert Q innerhalb der erklärten faktorisierten Familie. Sie wählt weder C aus dem Compiler aus noch rekonstruiert sie alle phasenmarkierten Operationen oder eine einzigartige Welt. Insbesondere kann dasselbe Q mehrere markierte C-Matrizen zulassen. Nach vollständigem unmarkiertem unitärem Kopienquotienten bestimmen die Singulärwerte die Takagi-Klasse; ein solcher Quotient muss zum Operationsvertrag passen.

### Anschluss an dieselbe Bosonzahl-Auslese

Auf N=3 hat H_C die Blockform \(\left(\begin{smallmatrix}0&gT_C^\dagger\\gT_C&\Delta I\end{smallmatrix}\right)\). Für einen normierten Eingang v auf der Boson-Fermion-Seite gilt exakt im Taylor-Anfang

\[
p_{N_b=1}(t)=1-g^2\langle v,G_C^{(3)}v\rangle t^2+O(t^4).
\]

Die erste und dritte Ableitung verschwinden. Der Protokollstrang hat diesen Blocksatz unabhängig für beliebige endliche Blockdimensionen symbolisch geprüft. Durch zugängliche Superpositionen und Polarisation könnte man die Matrixelemente aus der Anfangskrümmung rekonstruieren und dann Q berechnen. **Vorausgesetzt** wären solche Präparationen, eine kalibrierte Bosonzahlmessung, g und ein Zeitmaß. Bloße Spektraleigenwerte liefern nur die γ-Werte, nicht das markierte Q.

Dies ist eine echte gemeinsame Operatorverbindung zwischen Kompositionsrechnung und Aufzeichnungsrechnung. Die konkreten Abläufe liegen trotzdem in verschiedenen Ladungssektoren und sind noch kein gemeinsamer nativer Grundzustandsversuch.

## 7. Warum ein einzelnes C möglicherweise zu einfach für gerichteten Ladungstransport ist

Jede komplex-symmetrische endliche Matrix besitzt eine Takagi-Zerlegung \(U^T C U=D\) mit unitärem U und nichtnegativem diagonalem D. Eine Standardreferenz ist [Haber, A tale of three diagonalizations, Abschnitt 7](https://arxiv.org/abs/2009.03990). Der Prüfer kontrolliert zusätzlich ein nichtreelles rationales Beispiel. Der allgemeine Existenzsatz wird aus der linearen Algebra übernommen, nicht aus diesem Beispiel abgeleitet.

In der entsprechenden Fermionbasis enthält jeder Vertex zwei Fermionen aus derselben Takagi-Kopie. Deshalb bleibt **jede dieser Kopienparitäten** unter H_C, X, Nb und innerem G erhalten. Das gemeinsame Bosonsystem kann weiterhin koppeln und korrelieren; dieser Satz bedeutet nicht vollständige Faktorisierung des gesamten Modells. Er verhindert aber einen behaupteten einzelnen Fermionwechsel zwischen genau diesen konservierten Kopiensektoren mit diesem Alphabet.

Die Takagi-Achsen sind nicht automatisch räumliche Orte. Für andere markierte, nichtorthogonale Teile folgt kein universelles Transferverbot. Mehrere nicht gleichzeitig diagonalisierbare Kopplungstensoren können diese spezielle Paritätszerlegung aufbrechen. Das Zwei-Chart-Modell liefert genau ein solches kleines Beispiel: Die beiden Rang-eins-Projektoren auf e1 und (3/5,4/5) kommutieren nicht und besitzen nur den skalaren gemeinsamen Kommutanten. Ihre Auswahl bleibt zusätzliche Komposition.

## 8. Präzise nächste Entscheidung

Der einfachste nächste Auftrag ist kein neuer großer Tensorraum. Er ist eine typisierte Quellvorschrift für **zwei** Einbettungen E_L,E_R und ihre Überlappung \(E_L^\dagger E_R\), einschließlich der Bosonbankzuordnung. Die vorhandenen Quellstrahlen enthalten diskrete Überlappungszahlen, aber der direkte Import ihrer internen C4-Projektoren als neue triviale Kopien ist nicht äquivariant begründet.

Wenn der nächste Quellschritt existiert, muss er die hier berechneten Antworten vorhersagen, ohne c oder C anschließend anzupassen. Wenn er nur symmetrieverträgliche freie C zulässt, ist die Herkunftsfrage nicht geschlossen. Die Rückrechnungsformel stellt dann einen Mess- oder Identifikationsvertrag bereit, keinen Ersatz für die Herleitung.

## 9. Reproduktion und Grenze

`verify_composition.py` führt 67 explizite exakt arbeitende Prüfbedingungen aus, einschließlich Quellenpins und Strukturguards. Es gibt keine numerischen Toleranzprüfungen. Die allgemeine Formel und ihre Inversion sind oben algebraisch hergeleitet; drei vollständige N=3-CAR-Aufbauten kontrollieren Normalisierung, Vorzeichen und komplexe Konvention unabhängig.

Ein neuer Grundzustand für diese erweiterten Familien wurde nicht berechnet. Die früheren nativen N=64- und Polschranken dürfen nicht auf sie übertragen werden. Es ist keine physische Raumdimension, keine lokale Kausalstruktur, kein chirales Maß und keine Gravitation hergeleitet. Alle T1–T8-Gesamtpflichten bleiben offen.
