# Ein konkreter Cap-zu-Quellstrom-Anschluss

10. September 2026. Read-only-Prüfung des Originalstands `66b91e40e245569f06ab440ead80f446c9be0ee5`.

**Ergebnis:** Die native index-4-Q-System-Struktur enthält einen konkreten morphischen Kandidaten, aus dem die Wand einschließlich ihrer relativen Positivität und ihres hohen Budgets gemeinsam entsteht. Sein neutrales Cap zerfällt exakt in einen markierten Einheitskanal und drei orthogonale Komplementkanäle. Ein zusätzlicher Satz über die native bedingte Erwartung erklärt, wann die Minimalität einer primitiven Rückkehr dieselbe Norm erzwingt.

Der fehlende Herkunftsnachweis ist jetzt ein bestimmter markierter Intertwiner: Der tatsächliche hohe Mikrostrom muss diesen Cap beziehungsweise die minimale primitive Rückkehr realisieren. Das ist bislang nicht aus P1/P2 bewiesen. Eine explizite alternative Quelle erhält sogar die bekannte normierte hohe Rückkehr und die ganzen niedrigen/gemischten Blöcke, hat aber HH=13 statt 4. Sie zeigt genau, weshalb allgemeine Positivität oder Minimalität der gesamten Quelle den fehlenden Nachweis nicht ersetzt.

## 1. Tatsächliche native Quellen und ihre Grenzen

- `verification/v125_glue_qsystem.py:12–41,50–84` konstruiert A_glue=C[Z4], die Einheit η=δ0, die Multiplikation m(δa⊗δb)=δa+b und die Specialness mm†=4I. Die physische Identifikation mit der Seam-Calderón-Inklusion bleibt dort ausdrücklich eine zusätzliche Aufgabe.
- `tfpt_research_contracts.tex:2388–2487` nennt die gleiche Q-System-Struktur, die index-4-Erwartung auf der CAR-Leiter und ihre kohärenten endlichen Vorstufen. Die vierelementige Gruppenquasibasis ist auf bestimmten endlichen Leitern gerade nicht ohne Weiteres realisiert; die ungleichen Sektordimensionen und die früheste index-3-Anomalie werden ausdrücklich benannt.
- `verification/v993_minimal_defect_selector.py:169–212` und `tfpt_research_contracts.tex:13443–13460` geben die endliche normierte Erwartung E(X)=¼Σ Ad(u^r)(X) auf die Clock-feste Algebra an. Ihre Eindeutigkeit benötigt die Modulbedingung. P1/P2 bleiben deklarierte Eingaben.
- `tfpt_research_contracts.tex:12762–12857` trennt konkrete endliche Dilatationen von der physikalischen Feldanbindung. Derselbe populationsbasierte Transfer besitzt verschiedene kohärente Fortsetzungen. Deshalb wird hier weder aus Stinespring allein noch aus dem klassischen Transfer eine fundamentale Hamiltondynamik abgelesen.
- `tex-artefacts/toe_round4_proofs.tex:243–291` und `verification/v1027_signed_det_car_wall.py:129–148` liefern tatsächliche onsite DET-CAR-Operatoren unter der neutralen Determinantenprämisse. Die angeregten CAR-Moden behalten ihre ursprünglichen Ladungen. Der neutrale DET-Vakuumvektor macht nicht alle hohen Fermionen zu neutralen Teilchen.

## 2. Der native Frobenius-Cap und seine eindeutige Markierung

Allgemein für q=|G| und hier G=Z4 setze
\[
u=\eta\otimes\eta,\qquad
v=m^\dagger\eta=\sum_{a\in\mathbb Z_q}\delta_a\otimes\delta_{-a}.
\]
Die Standardbasis ist orthonormal. Dann gilt
\[
\|v\|^2=q,\quad\langle u,v\rangle=1,\quad
v=u+v_\perp,\quad\|v_\perp\|^2=q-1. \tag{1}
\]
Für q=4 ist dies genau 4=1+3.

**Normierungen:** m†/2 ist die Isometrie vom vierdimensionalen Raum in seinen Tensorquadratraum. m/2 ist die zugehörige Coisometrie, keine Isometrie auf dem sechzehndimensionalen Definitionsraum. Der normierte Cap ist v/2; seine Überlappung mit dem Einheitspaar ist 1/2. Der unnormierte Cap v besitzt dagegen Einheitskanal-Amplitude 1 und Normquadrat 4. Diese beiden Normierungen dürfen nicht vertauscht werden.

Der Cap lässt sich ohne eine neue Positivitäts- oder Spurbedingung charakterisieren. Sei L_gδ_a=δ_(g+a). Ein Vektor w ist gleich v, wenn er

1. im neutralen Gesamtsgrad liegt, also w=Σ r_a δ_a⊗δ_−a;
2. das beidseitige Verschiebungsgesetz (L_g⊗L_−g)w=w erfüllt;
3. im markierten Einheitspaar die Amplitude ⟨u,w⟩=1 besitzt.

**Beweis:** Die zweite Bedingung setzt alle r_a gleich; die dritte setzt sie auf 1. Äquivalent ist das Frobenius-Verschiebungsgesetz (L_g⊗I)w=(I⊗L_g)w. Auf dem neutralen Raum ist seine Lösungsdimension genau eins.

Dies gilt auch für operatorwertige Stromkomponenten R_a: Verschieben der beiden Cap-Schenkel erzwingt R_a=R_0. Ist R_0=tI durch den markierten gemischten Quellkanal festgelegt, so sind alle R_a=tI. Damit wird ein allgemeiner hoher Operator auf ein skalares Budget zurückgeführt, ohne seine Diagonalform zuvor anzunehmen.

## 3. Der Cap erzeugt den vollständigen Parent

Sei A=A† der bereits bezeichnete räumliche niedrige Kernel. Für positive Skalen s,t bilde auf denselben beiden Materiespalten
\[
C_L=s\,u\otimes A,\qquad C_H=t\,v\otimes I,
\qquad W=(C_L,C_H).
\]
Dann folgt direkt aus (1)
\[
\operatorname{diag}(A,0)+W^\dagger W
=\begin{pmatrix}
A+s^2A^2&stA\\stA&qt^2I
\end{pmatrix}. \tag{2}
\]
Außerdem ist dieselbe Form
\[
\operatorname{diag}(A,(q-1)t^2I)
 +(sA,tI)^\dagger(sA,tI). \tag{3}
\]
Der positive relative Gramstrom und die freie hohe Ergänzung entstehen somit aus derselben Cap-Zerlegung. Ein zusätzlich angesetztes HH-Spurbudget wird für diesen Satz nicht benötigt.

**Die Skala folgt jedoch nicht aus q allein.** Für die schon festgelegten ganzen niedrigen und gemischten Koeffizienten β=s² und η=st ergibt sich
\[
\boxed{M\beta=q\eta^2,\quad
\lambda=\eta^2/\beta,\quad
\Delta=(q-1)\eta^2/\beta,\quad g=\beta/\eta.} \tag{4}
\]
Mit q=4, β=1/4, η=1/2 liefert dies M=4, λ=1, Δ=3 und g=1/2. Die bekannte niedrige lineare Zeiteinheit und die Koeffizienten β,η sind dabei Eingaben der markierten Quellidentifikation, keine Folgen der abstrakten Specialness.

Für die ursprünglichen Nachbarschaftskoeffizienten A=a Adj, b=ηa und c_hop=βa² wird (4) zur direkt überprüfbaren Relation
\[
\boxed{M c_{\rm hop}=q b^2.} \tag{5}
\]
c_hop ist hier der volle mikroskopische Zwei-Link-Koeffizient. Er darf nicht mit dem nach Eliminierung des hohen Blocks verbleibenden niedrigen Spektralkoeffizienten β−η²/M verwechselt werden. Für letzteren folgt stattdessen M(β−η²/M)=(q−1)η².

Die Gramidentitäten sind Operatoridentitäten für beschränkte A und bewahren die früher bewiesenen ambienten Randkanäle bei Kompression. Sie benötigen keine freie Fock-Diagonalisierung quantisierter Links. Eine Gleichheit der gesamten physikalischen Quelle mit diesen Cap-Strömen bleibt ein separater Intertwiner-Nachweis.

## 4. Ein zweiter positiver Herkunftssatz aus primitiver Rückkehr-Minimalität

Die native endliche Erwartung lautet, mit u^4=I,
\[
E(X)=\frac14\sum_{r=0}^3u^{-r}Xu^r.
\]
Die Summenkonvention entspricht derselben Gruppe wie die native Ad(u^r)-Schreibweise. Sind alle vier Clock-Eigenwerte vorhanden, sind I,u,u²,u³ linear unabhängig. Die Krausoperatoren K_r=u^r/2 sind dann minimal; der Choi-/Krausrang ist vier.

**Satz.** Angenommen, ein bezeichnetes primitives hohes Rückkehrinstrument hat genau vier Krausoperatoren R_r/√M und realisiert genau E. Sein mit dem niedrigen Strom gekoppelter markierter Bein sei R_0=tI mit t>0. Dann gilt M=4t².

**Beweis:** Zwei minimale Krausfamilien derselben CP-Abbildung hängen durch eine unitäre 4×4-Matrix U zusammen. Also
\[
R_0/\sqrt M=\frac12\sum_r U_{0r}u^r=tI/\sqrt M.
\]
Lineare Unabhängigkeit erzwingt U_0r=0 für r≠0 und U_00=2t/√M. Die erste Zeile ist normiert, daher M=4t². Diese Eindeutigkeit folgt auch unmittelbar aus zwei minimalen Faktorisierungen derselben positiven Choi-Matrix und braucht keinen zusätzlichen physikalischen Eindeutigkeitssatz.

Zusammen mit einem ausschließlich an diesen markierten Identitätsbein angeschlossenen niedrigen Strom sA liefert dies erneut (4). Der Satz verwendet einen skalaren kalibrierten Strommaßstab M und eine bekannte vollständige normierte CP-Abbildung. Er wird nicht als Satz über beliebiges operatorwertiges D allein aus einem populationsbasierten Rückkehrkern ausgegeben.

Die konkrete Herkunftsfrage lautet hier: Realisiert der tatsächliche hohe Mikrostrom diese vollständige Erwartung mit einer für diese primitive Rückkehr minimalen Krausdarstellung, und welcher Bein ist der physische Einheitspfad? Weder die abstrakte Existenz einer Stinespring-Dilatation noch Minimalität eines anderen oder größeren Kanals beantwortet das.

Die Voraussetzung aller vier Clock-Eigenwerte ist relevant. Eine Leiterstufe mit fehlendem Grad kann einen kleineren Krausrang haben; die im Korpus ausgewiesene index-3-Anomalie darf nicht durch die Zahl vier übersprungen werden.

## 5. Zwei konkrete alternative Parents und die genau fehlende Information

### 5.1 Gleiche primitive Algebra und Einheitsmarkierung, anderer Cap-Anschluss

Der parameterfreie Vektor
\[
v_{\rm alt}=2m^\dagger\eta-\eta\otimes\eta
=u+2v_\perp
\]
verwendet nur die vorhandenen primitiven Morphismen und lineare Operationen. Er ist weiterhin gesamtsgradneutral, hat denselben markierten Einheitskoeffizienten 1 und Normquadrat 13. Mit C_L=u⊗A/2 und C_H=v_alt⊗I folgt
\[
h_{\rm alt}=
\begin{pmatrix}A+A^2/4&A/2\\A/2&13I\end{pmatrix}
=h_{\rm nat}+\operatorname{diag}(0,9I). \tag{6}
\]
Auch die ursprüngliche relative Kopplungsform gegenüber diag(A,3I) bleibt positiv: Es kommt genau 9I im hohen Block hinzu. Die zusätzliche Energie ist nach CAR-Quantisierung der onsite, gerade und ladungserhaltende Term 9N_H; er benötigt keine neuen Materiearten oder eine Änderung der P1/P2- oder Z4/Q-System-Daten.

Dieser alternative **zusätzliche Parent** hat nicht dieselben vollständigen dynamischen Antworten oder Vorhersagen wie der ursprüngliche Parent. Er zeigt, was die abstrakten Daten noch nicht auswählen. Er verletzt genau die fehlende Cap-Anbindung: Für den primitiven Verschieber beträgt ||(L_1⊗L_−1)v_alt−v_alt||²=2. Die Frobeniusaxiome des zugrunde liegenden Q-Systems bleiben unverändert; der hohe physische Strom wurde lediglich nicht als ihr balancierter Cap identifiziert.

### 5.2 Selbst die gleiche normierte Rückkehr und gemeinsame Minimalität genügen nicht

Behalte dieselbe native Erwartung E und definiere fünf hohe Strombeine
\[
R_0=I,\quad R_1=\tfrac32I,\quad
R_2=\tfrac{\sqrt{13}}2u,\quad
R_3=\tfrac{\sqrt{13}}2u^2,\quad
R_4=\tfrac{\sqrt{13}}2u^3.
\]
Dann gilt exakt
\[
\sum_{r=0}^4R_r^\dagger R_r=13I,\qquad
\frac1{13}\sum_{r=0}^4R_r^\dagger X R_r=E(X).
\]
Der niedrige Strom wird ausschließlich an den markierten Bein R_0=I gekoppelt. Die vollständigen gemeinsamen Krauszeilen lauten
\[
W_0=(A/2,I),\quad W_r=(0,R_r)\quad(r=1,\ldots,4).
\]
Sie reproduzieren ebenfalls (6): gleiche vollständige LL-/LH-Blöcke, gleiche normierte hohe Rückkehr, aber ein anderer HH-Block.

Die hohe Rückkehr allein ist mit fünf Beinen nicht minimal: Die beiden Identitätsbeine sind redundant, ihr Krausrang bleibt vier. Die **gemeinsame Zwei-Eingangsquelle ist dagegen minimal mit Rang fünf**. Denn jede lineare Relation zwischen den W_r hat aus der niedrigen Spalte bei A≠0 zunächst Koeffizient null vor W_0; anschließend erzwingt die Unabhängigkeit von I,u,u²,u³ die übrigen Koeffizienten null. Ein pauschales Minimalitätsprinzip für die ganze Quelle scheidet diese Alternative somit nicht aus.

Der Unterschied ist keine Wortwahl: Die Identitätsmarkierung koppelt den niedrigen Eingang gerade an eine Aufspaltung des hohen Rückkehrkanals, die dessen unmarkierte normierte CP-Abbildung nicht sehen kann. Der ursprüngliche primitive Rückkehrkanal muss als markiertes Objekt identifiziert werden.

## 6. Neutralität, CAR und physische Anbindung

Die drei Komplementvektoren δ1⊗δ3, δ2⊗δ2, δ3⊗δ1 sind im Z4-Gesamtgrad neutral. Das ist keine Aussage, dass drei neue physische Fermionen, drei Generationen oder drei unabhängige neutrale Teilchen existieren. Die δ_a sind zunächst Sektorlabels der Q-System-Struktur.

Für einen wirklichen Mikrostrom braucht es einen gauge-, spin- und paritätsverträglichen Intertwiner, der diese abstrakten Cap-Schenkel an die tatsächlichen CAR-/Rotoroperatoren bindet. Die Verbindung muss die native positive Paarung, die markierte Einheit, das beidseitige Verschiebungsgesetz und die räumlichen Kompressionen respektieren. Die tatsächlichen hohen CAR-Anregungen tragen weiterhin die im nativen DET-Konstrukt bewiesenen ursprünglichen Ladungen; eine neutrale Cap-Koeffizientenstruktur kann sie begleiten, aber nicht ihre CAR-Realisierung ersetzen.

Auch die formal vierdimensionalen Cap-/Krauslabels dürfen nicht ohne Nachweis als vier physische Umgebungsmoden eingesetzt werden. Gerade die native endliche Leiter besitzt ungleiche Sektordimensionen und gewichtete Quasibasen. Der verlangte Intertwiner muss diese tatsächliche Darstellung behandeln, nicht nur ein zusätzlich angehängtes abstraktes C4.

## 7. Der konkrete nächste Herkunftsnachweis

Aus der ursprünglichen markierten Seam ist ein Quellmorphismus zu konstruieren, der

1. den hohen Strom auf den neutralen Frobenius-Cap schickt und das beidseitige Verschiebungsgesetz erhält;
2. den niedrigen Transport an den bezeichneten Einheitspaar-/Identitätspfad bindet, mit den tatsächlich hergeleiteten niedrigen und gemischten Normierungen;
3. die originale Gauge-/Spin-/CAR-Realisierung, die positive Paarung und die vollständigen Randkanäle respektiert.

Alternativ kann dieselbe Bindung durch die vollständige native Rückkehrerwartung, ihre **primitive** Minimalität und die identifizierte Krausmarkierung bewiesen werden. Erst dann folgen die relative Grampositivität und der gesättigte HH-Wert aus vorhandenen Strukturen anstatt aus neuen unabhängigen Bedingungen.

Damit liegt mehr als eine neue Gramfaktorisierung vor: Der Anschluss benennt eine eindeutige native primitive Morphismusklasse, ihre erforderliche Normalisierung, ihre überprüfbare Beziehung Mc_hop=4b² und zwei explizite Quellen, die exakt den fehlenden Bindungsschritt verletzen. Eine fundamentale P1/P2-Herleitung dieses Intertwiners wurde in dieser Fortsetzung nicht gefunden oder behauptet.

## 8. Eigene Kontrolle

`check_cap_origin.py` besteht 31 exakte Kontrollen. Geprüft sind unter anderem die tatsächliche primitive Multiplikation, die Isometrie-/Coisometrie-Normierungen, der eindeutige neutrale Cap-Raum, alle vollständigen Grammatrizen, die alternative Cap-Verletzung, die Gleichheit der normierten Rückkehr auf sämtlichen Matrixeinheiten und die unterschiedlichen minimalen Krausränge. Es wird kein TFPT-Code importiert oder ausgeführt. Die allgemeinen Aussagen stehen in den obigen Beweisen; eine Anzahl grüner Kontrollen ist keine physikalische Quellenidentifikation.
