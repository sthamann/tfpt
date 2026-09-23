# TFPT / Universalraum: Clock, gemeinsame Quelle und tatsächlicher Transport

## Konsolidierung und eigene Forschungsfortsetzung v1.6.6 — 15. September 2026

**Ergebnis:** Der dokumentierte endliche Clock ist jetzt ausdrücklich als
Element der vorhandenen inneren Spin(10)-Symmetrie konstruiert. Dadurch lässt
sich die bislang offene gemeinsame Clock-/Casimir-Auslesung exakt bestimmen.
Daneben wurde ein kleiner, echter Vierzustandskanal der ursprünglichen
Paarwechselwirkung gefunden, der nach Zulassung eines Bosonmischers eine
Fermionenmarke überträgt. Die Herkunft dieses Mischers ist nicht bewiesen.

Der neue Universalraum-Text enthält eine sinnvolle Suchrichtung — gemeinsame
Quelle statt vorab unabhängiger Banken —, aber Überlappung allein erzeugt
weder Transport noch Raumzeit, Eichkrümmung oder die arithmetische Spur.
Mehrere seiner vermeintlich automatischen Übergänge werden hier präzisiert.

Diese Revision integriert **drei neue Nutzertexte**, die unabhängigen
parallelen Prüfungen und eigene neue Herleitungen. Die vollständige frühere
Konsolidierung v1.6.5 einschließlich v1.6.4 bleibt im historischen Anhang
erhalten. Das ist eine aktualisierte Forschungsfassung in Markdown mit
kurzem Änderungsdokument und einfacher Erklärung; keine behauptete neue
PDF-/Web-Publikation oder vollständige Theory of Everything.

### Leseschlüssel

- **Exakt:** Identität oder mathematische Folgerung im angegebenen Modell.
- **Numerisch:** berechneter Näherungswert, ohne zertifizierte Einschließung.
- **Bedingt:** exakter Satz erst nach ausdrücklich zusätzlicher Ressource.
- **Offen:** fehlende Herleitung oder physikalische Identifikation.

Eine grüne Prüfung ersetzt weder die Voraussetzungen eines Satzes noch eine
ausführbare Operation. Assoziative Algebradimension, dynamische
Kontrollierbarkeit und physische Verfügbarkeit werden getrennt geführt.

## 1. Die unveränderte gemeinsame Grundlage

Mit 64 Fermionmoden, 60 Bosonmoden und demselben gepinnten Tensor gilt

\[
H_{\rm nat}=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
\qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad N=N_f+2N_b.
\]

W besitzt 480 Einträge ±1, acht disjunkte Paare je Zeile, und
`WW†=8 I60`. Die Fermionmarkierung ist `16⊗4`, die Bosonmarkierung `10⊗6`.
Spin(10)×SU(4) ist zunächst eine **innere** Quellsymmetrie, keine bereits
hergeleitete Raumzeit-Lorentzgruppe.

Der frühere native Satz bleibt unverändert maßgeblich: Für Δ>0 und
`0<|g|/Δ≤1/20` hat dieser μ=0-Vertrag einen eindeutigen globalen Grundzustand
Ω bei N=64. Am Prüfpunkt `g/Δ=1/20` gelten unter anderem

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad 0.842846<\langle N_b\rangle_\Omega<1.245656.
\]

Die isolierte niedrige Entnahmelinie im N=63-Sektor hat weiterhin die
bewiesenen Schranken aus v1.6.4/v1.6.5:

\[
0.007737\Delta<\epsilon<0.039079764\Delta,
\qquad
Z_{\rm low}>\frac{40912436089}{46487375000}>0.88007628.
\]

Z bezieht sich auf das gesamte normierte Fermionspektralgewicht pro Mode.
Die gesamte Entnahmenorm ist dagegen
`ν=<f_r†f_r>=1-<Nb>/32`. Die beiden Größen sind nicht austauschbar.
Der Pol ist eine wohldefinierte isolierte Eigenlinie dieses endlichen
Modenmodells; seine relativistische Teilchen-, Massen- oder räumliche
Propagationsdeutung ist eine weitere Aufgabe.

Der vollständige bedingte Zwei-Banken-Satz aus v1.6.5 bleibt erhalten:
mit deklariertem Fermionlink und Rotorvertrag gelingt der reine niedrige
Transfer mit Wahrscheinlichkeit >99,267 %, die unfiltrierte ursprüngliche
Entnahme mit >89,726 %. Der Link war und ist **zusätzlich vorausgesetzt**.
Die neuen Vierzustandszahlen unten gehören zu einem anderen Vertrag und
ersetzen diese Ergebnisse nicht.

## 2. Quellenprüfung der beiden neuen Ergebnisrunden

### 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-,
Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch
reproduziert. Darunter befinden sich neun wörtliche `need(True, ...)`-Guards
mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als
neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu;
Abschnitt 3 ersetzt sie durch eine explizite Konstruktion.

Im gesamten N=3-Raum gilt die Zerlegung:

| Typ | irreduzible Dimension | Multiplizität | Spin-Casimir | Farb-Casimir |
|---|---:|---:|---:|---:|
| (1200,20) | 24000 | 1 | 141/4 | 39/4 |
| (560,20′) | 11200 | 1 | **117/4** | 63/4 |
| (672,4̄) | 2688 | 1 | 165/4 | 15/4 |
| (144,20) | 2880 | 2 | 85/4 | 39/4 |
| (144,4̄) | 576 | 2 | 85/4 | 15/4 |
| (16̄,20) | 320 | 2 | 45/4 | 39/4 |
| (16̄,4̄) | 64 | 1 | 45/4 | 15/4 |

Die gewichtete Gesamtdimension ist 45504. Nur die getrennten Teile Λ³64 und
60⊗64 sind jeweils multiplizitätsfrei, nicht ihre direkte Summe. Die drei
dunklen Typen besitzen alle Gesamtcasimir 45, werden aber bereits durch
**einen** getrennten Casimir unterschieden.

Eine unabhängige rationale Rechnung auf den kleinen Multiplizitätsräumen
liefert für die jeweils **gewährten** Operationen:

| Operationsvertrag | komplexe assoziative Algebradimension |
|---|---:|
| Ein fixes H=Nb+X/20 | 8 |
| X und Nb unabhängig | 14 |
| Zusätzlich ein dunkler Isotypieprojektor | 15 |
| Zusätzlich ein getrennter Casimir | 16 |
| Zusätzlich nur Gesamtcasimir | 14 |

Somit gibt es keine universelle binäre Frage „alle Symmetriegriffe oder gar
kein Fortschritt“. Die Dimension 15 ist ein konkretes Gegenbeispiel.
Die vollständige Gruppen-Generatoralgebra hat mit X,Nb die Dimension
743583744 und Kommutantdimension 7. Sie ist unter Gruppenkonjugation
**stabil**, aber nicht punktweise invariant. Sieben ist kein universeller
Boden für beliebige symmetriestabile Algebren: End(H) wäre ebenfalls stabil
und hätte einen eindimensionalen Kommutanten. Keine dieser Zahlen beweist,
dass die zugehörigen Operationen im Compiler ausführbar sind.

### 2.2 Der Grundzustandsbericht enthält einen Versionskonflikt

Der neue Text hat die Nichtschlussnorm bereits korrigiert, das danebenliegende
`native_ground_state.json` stammt jedoch von einer älteren Codefassung. Sein
als PASS markierter Wert ist um `229²` zu groß; die dortige relative
orthogonale Norm ist sogar größer als eins. Der daraus berechnete Ritzwert
−1,18826198 wird **nicht** übernommen.

Eine neue direkte ganzzahlige Kontraktion umgeht die 15,25 Millionen
Komponenten von v₃. Sie berechnet `u=T T†v₂` auf 293280 nichtverschwindenden
Komponenten und bestätigt exakt

\[
\|u\|^2=752194252800,\quad
\langle v_2,u\rangle=575078400,\quad
w_2=u-\frac{299520}{229}v_2,
\quad\|w_2\|^2=\frac{5001523200}{229}>0.
\]

Der eine Vektor je Bosonlage schließt daher nicht. w₂ ist ein zweiter
Singulettvektor derselben Lage. Für die kleine vier- bzw. fünfdimensionale
Ritzmatrix ergeben sich bei g/Δ=1/20 **numerisch**

\[
E_{R,4}/\Delta=-1.0942308394409612,
\qquad E_{R,5}/\Delta=-1.0942318710142458.
\]

Die zusätzliche w₂-Richtung ändert diese Näherung tatsächlich erst um etwa
10⁻⁶. Das bedeutet **keine** Konvergenz zum wahren Grundzustand: Beide Werte
liegen noch über dessen bereits bewiesener Obergrenze.

Die neue einfache Restformel zeigt die Ursache. Für den normierten
Vier-Vektor-Ritzeigenzustand mit letzter Komponente c₃ gilt

\[
\|(H-E_R)\psi_3\|^2
=g^2|c_3|^2\frac{\nu_4+\|w_2\|^2}{\nu_3}.
\]

Mit dem früher geprüften vierten Moment ist die Restnorm numerisch rund
0,373063 Δ. Der kleine w₂-Zweig trägt weniger als 23 Millionstel des
quadrierten Restes; die ausgelassene v₄-Richtung dominiert. Die neuen
Zahlen `Zh≈0,9737` und `εh≈0,031Δ` gehören ebenfalls zur Ritz-Näherung:
Gesamtentnahmenorm und erstes Moment, nicht neu bestimmte Polgrößen auf Ω.

Die Suche nach `E<−1,2Δ` oder `E<−1,1625Δ` wäre sogar mit der bestehenden
unteren Schranke unvereinbar. Die schwächere neue Beweismethode öffnet den
bereits geschlossenen nativen Grundzustandssatz nicht wieder.

## 3. Neuer exakter Anschluss: Der Clock liegt bereits in Spin(10)

### 3.1 Ausgangspunkt ist der tatsächliche Quell-Clock

Der gepinnte endliche Compilerpräfix liefert auf fünf Hilfsachsen

\[
p=(0\mapsto2,\ 1\mapsto0,\ 2\mapsto1,\ 3\mapsto4,\ 4\mapsto3),
\qquad\det p=-1.
\]

Seine vorzeichenrichtige Exteriorhebung auf dem geraden 5-Moden-Hilfsfockraum
ist Γ(p)|even. Auf den nativen Fermionen ist `GF=Γ(p)|even⊗I4`; auf den
Bosonen ist `GB=(-P10)⊗I6`, wobei P10 beide Fünfergruppen permutiert.
Diese Darstellung wird aus dem vorhandenen Clockpräfix erneut extrahiert,
nicht aufgrund passender Eigenwerte ausgewählt.

### 3.2 Ein ausdrückliches Spinwort

Auf dem 32-dimensionalen Hilfsfockraum seien

\[
\gamma_j=a_j+a_j^\dagger,\qquad
\gamma_{j+5}=i(a_j^\dagger-a_j),\qquad 0\le j<5,
\]

und Π dessen Fermionparität. Setze

\[
\Omega_{10}=\gamma_0\gamma_1\cdots\gamma_9=i\Pi,
\qquad
R_{ab}=\frac{(\gamma_a-\gamma_b)(\gamma_{a+5}-\gamma_{b+5})}{2}.
\]

R_ab ist das Produkt zweier reeller Einheitsvektoren der Cliffordalgebra,
also ein Spin(10)-Element. Direkt gilt
`R_ab=i Γ((ab))`. Da `p=(01)(02)(34)` mit rechts zuerst angewandter Permutation,
folgt

\[
\boxed{S=\Omega_{10}R_{01}R_{02}R_{34}=\Pi\Gamma(p)\in\mathrm{Spin}(10).}
\]

S ist ein Produkt von 16 reellen Clifford-Einheitsvektoren. Die Matrixprüfung
bestätigt ohne Rundungstoleranzen

\[
S_{even}=\Gamma(p)_{even},\qquad S_{odd}=-\Gamma(p)_{odd},
\qquad S\gamma_jS^\dagger=-\gamma_{p(j)}
\]

mit entsprechender Fortsetzung auf die zweite Fünfergruppe. Damit stimmen
**beide nativen Darstellungen** und die ursprüngliche Kopplung überein:

\[
G_F=S_{even}\otimes I_4,\qquad
G_B=(-P_{10})\otimes I_6,\qquad
W\Lambda^2G_F=G_BW.
\]

S hat Ordnung sechs. Die Konjugation aller 45 Spin-Erzeuger und die
Kommutation mit allen 15 Farb-Erzeugern wurden zusätzlich direkt geprüft.
Die Aussage ist stärker und präziser als ein lediglich behaupteter
Normalisatorsatz.

**Bedeutung:** Der dokumentierte Clock und die innere Spin-Symmetrie brauchen
hier keine getrennten zusätzlichen mathematischen Träger. Es handelt sich
um einen konkreten endlichen Schritt derselben Darstellung. Daraus folgen
aber weder kontinuierliche Spin-Kontrollen noch die Identifikation des
Clocks mit Hamiltonzeit. Die Hilfs-Cliffordachsen sind nicht bereits fünf
Raumrichtungen.

## 4. Clock und getrennte Casimire lassen sich gemeinsam auslesen

Weil G aus Spin(10) stammt und auf SU(4) trivial wirkt, kommutiert es mit
beiden getrennten Casimiren, auch auf ihren Fockhebungen. Die Frage aus dem
neuen Text ist damit auf algebraischer Ebene beantwortet.

Die exakten Charakterfolgen von S_even, S_odd und dem Vektor sind

\[
(16,0,4,0,4,0),\quad(16,0,4,0,4,0),\quad(10,0,4,-6,4,0).
\]

Die schon unabhängig nachgerechneten Zerlegungen
`Sym³16=672+144`, `Λ³16=560`, `S21(16)=1200+144+16̄` und
`10⊗16=144+16̄` bestimmen die Charaktere der sieben Typen. Die diskrete
Fourierinversion erfolgt exakt in Z[ζ6], nicht durch gerundete komplexe
Eigenwerte. Für die drei zuvor gemeinsam dunklen Räume ergibt sich:

| Dunkler Typ | Phase 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| (1200,20) | 4000 | 4000 | 4000 | 4000 | 4000 | 4000 |
| (560,20′) | 1920 | 1840 | 1840 | 1920 | 1840 | 1840 |
| (672,4̄) | 464 | 440 | 440 | 464 | 440 | 440 |
| Summe, bisherige Clock-Auslesung | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |

Ein separater Casimir trennt jede der sechs dunklen Clockzellen in genau
drei Teile. Die hellen Zweier-Multiplizitätsräume bleiben erhalten. Daraus
folgt im N=3-Sektor

\[
\boxed{\dim\operatorname{Alg}^*(X,N_b,G,C_S)=96,}
\qquad
\boxed{\dim\operatorname{Alg}^*(X,N_b,G,C_S)'=119597824.}
\]

Zum Vergleich: ohne C_S sind es 84 und 240742144. C_C kann C_S ersetzen.
Die Lagrangeprojektoren auf den drei dunklen C_S-Werten bestätigen die
Trennung ausdrücklich; beide Casimire zugleich werden nicht benötigt.

**Es handelt sich um eine gelöste Kombinationsfrage, nicht um eine neue
Kontrollfreigabe.** Der benötigte Casimir ist noch kein vom Compiler
bereitgestelltes Messinstrument. Der große verbleibende Kommutant zeigt
weiterhin viele nicht aufgelöste Freiheitsgrade. Die Dimensionszahlen gelten
für N=3, nicht als vollständige Klassifikation aller Ladungssektoren.

## 5. Neuer kleiner Transportzeuge mit tatsächlichen W-Kanälen

Ein gemeinsamer Fermion-/Boson-Dreierstern hätte die einfache Identität

\[
Q_x=b^\dagger s f_x,\quad Q_y=b^\dagger s f_y,
\qquad [Q_y^\dagger,Q_x]=(N_b+n_s)f_y^\dagger f_x.
\]

Auf festem `K=Nb+n_s≥1` ist `c†=b†s/√K` exakt eine CAR-Mode. Das ergibt
eine gewöhnliche Dreimoden-Transferkette. **Aber dieser Stern ist nicht
in einer nativen W-Zeile enthalten:** Jede Zeile ist ein Matching aus acht
disjunkten Paaren. Die Analogie allein wäre daher eine falsche Herkunftsangabe.

Im echten W gibt es stattdessen die Paare `(4,57)` in Kanal 0 und `(4,58)`
in Kanal 1. Mit den sieben besetzten Pauli-Blockern

\[
S_b=\{8,16,28,32,44,52,56\}
\]

und einem **zusätzlichen** Mischer `J(b1†b0+b0†b1)` schließt die volle
native Wechselwirkung exakt auf den vier Zuständen

\[
S_b+\{4,57\}\ \longleftrightarrow\ S_b+b_0
\ \longleftrightarrow\ S_b+b_1
\ \longleftrightarrow\ S_b+\{4,58\}.
\]

Alle haben N=9. Die vollständige Wirkung sämtlicher 480 signierter Paarterme
bleibt in diesem Raum, mit Matrix

\[
H_4=\begin{pmatrix}
0&g&0&0\\g&\Delta&J&0\\0&J&\Delta&g\\0&0&g&0
\end{pmatrix}.
\]

Für `g/Δ=1/20`, `J/Δ=1-1/(10√3)` und `tΔ=20π√3` gilt analytisch

\[
P(57\to58)>\frac{2009992727}{2022609600}
=0.9937620819\ldots>99.3\%.
\]

Die Eigenfrequenzen Δ±J bleiben positiv. Dies ist keine unkontrollierte
Vierzustandsabschneidung: Zuerst ist die Invarianz unter der vollständigen
Wechselwirkung bewiesen, danach wird deren exakte Einschränkung gelöst.
Ohne Mischer zerfällt sie in zwei getrennte Blöcke und der Transfer ist null.

Der reine Einzelmischer kommutiert nicht mit dem ursprünglichen Clock.
Die Clock-Orbitsumme der Mischer `(0,1)+(12,13)+(6,7)` ist dagegen
Clock-invariant und hat auf diesem Vierzustandsraum dieselbe Wirkung.
Somit wäre „jeder solche Transfer muss den Clock brechen“ falsch. Beide
Mischer sind jedoch noch zusätzliche Operationen; Clock-Invarianz allein
beweist keine Erzeugbarkeit. Ein gemeinsamer SU(4)-Cartan Q kommutiert mit
H, Nb, Clock und beiden getrennten Casimiren. Auf den vier Zuständen besitzt
er aber die Werte `(7,7,9,9)`. Die beiden Mischer ändern diese Quantenzahl:
`||[Q_B,M01]||²_F=8`, `||[Q_B,Morb]||²_F=24`. **Auch die Clock-invariante
Orbitsumme ist damit aus diesem Operationssatz ausgeschlossen.**

Die noch fehlende Ressource ist hier konkret: eine Operation, die diese
innere Cartanladung verändert, oder eine global hergeleitete Kopplung an
einen ausdrücklich mitgerechneten Ladungsausgleich. Mehr Wörter aus
dem unveränderten erhaltenden Alphabet können beide Mischer nicht liefern.

Dieser Zeuge ist **keine** Propagation der N=64-Grundzustands-Lochanregung,
keine räumliche Zwei-Banken-Übertragung und keine Konstruktion ihrer
Präparation. Er zeigt konstruktiv, wie nah eine kleine Paarumwandlung an
einem Transfermechanismus liegen kann, und benennt die fehlende Ressource.

## 6. Das Feldwörterbuch: eine Basisänderung allein reicht nicht

Der bestätigte Grundfehler bleibt: `M_A⊗ε_Lorentz` ist symmetrisch und
verschwindet als Grassmann-Bilinear. Das betrifft die lokale ableitungsfreie
Zuordnung einer gleichhändigen Weylkopie je ursprünglichem Label bei
unverändertem antisymmetrischem W. Der nichtverschwindende gleichhändige
Kanal trägt `(1,0)`; daraus folgt noch keine gesunde Kinetik.

Der neue Fünf-Zyklus im Trägergraphen widerlegt eine rein diagonale
Zuweisung entgegengesetzter Händigkeiten an jedes Paar. Ein neuer eigener
Satz geht darüber hinaus. Für irgendeine hermitesche interne Händigkeit Γ
müsste im unveränderten Ein-Kopie-Vektoransatz gelten

\[
\Gamma^TM_A+M_A\Gamma=0\quad\forall A.
\]

Adjungieren und Einsetzen liefert `[Γ,M_A†M_B]=0`. Der ursprüngliche Tensor
faktorisiert exakt als

\[
M_{ka}=S_k\otimes C_a,\quad
\sum_kS_k^\dagger S_k=5I_{16},\quad
\sum_aC_a^\dagger C_a=3I_4.
\]

Die S_k†S_l erzeugen M16; die C_a†C_b erzeugen M4. Dafür wurden vollständige
Rangzertifikate modulo 101 mit 256 bzw. 16 unabhängigen ganzzahligen
Matrixwörtern konstruiert. Ein nichtverschwindender Determinant modulo 101
beweist Nichtverschwindung über C; keine Rangdefizienz wird übertragen.
Damit ist Γ skalar, und die ursprüngliche Gleichung erzwingt Γ=0.

**Keine hermitesche Involution Γ²=I auf demselben Träger repariert diesen
Ein-Kopie-Vektoransatz.** Der Ausschluss ist nun basisunabhängig, aber
weiterhin vertragsgebunden.

Nicht ausgeschlossen sind zusätzliche Dirackomponenten, ein unabhängiger
Zweierfaktor oder Ableitungsterme. Insbesondere ist

\[
M_A\otimes\epsilon_{aux}\otimes\epsilon_{Lorentz}
\]

antisymmetrisch und nicht null. Ein ableitungshaltiger gleichgeladener
Vektorstrom `M_IJ ε_ab ψ_Ia ↔∂_μ ψ_Jb` ist ebenfalls nicht null; der
pauschale Vektorausschluss durch Ladung gilt nicht außerhalb der
ableitungsfreien Klasse.

Die Zahlen 180/128 oder 60/256 zählen Komponenten eines bestimmten
Feldansatzes, nicht automatisch unabhängige propagierende Oszillatoren.
Schur fixiert interne Intertwiner, nicht alle Lorentz-/Ableitungsterme.
Der behauptete Zwang „zuerst räumlich skalieren, danach Feldtyp prüfen“ folgt
nicht daraus. Zuerst bleibt ein kleiner konsistenter Typ-/Kinetiktest sinnvoll;
seine reale räumliche Herkunft muss anschließend gemeinsam geprüft werden.

## 7. Was der nachgereichte Universalraum-Text trägt

### 7.1 Eine sinnvolle Hypothese, kein bereits identifiziertes universelles Objekt

Nichtorthogonale oder überlappende lokale Einbettungen in eine gemeinsame
Algebra sind eine ernstzunehmende Alternative zu unabhängigen Banken. Sie
können Voraussetzungen der lokalen Paritätsschranke ändern. Das ist ein
Forschungsauftrag, kein Widerspruch zur bisherigen Schranke.

Bei Einbettungen `J_A:V_A→V` gilt für die CAR jedoch

\[
\{f_A(u),f_B(v)^\dagger\}=\langle J_Au,J_Bv\rangle.
\]

Die Überlappungs-Grammatrix gehört also zwingend zum Modell. Die alten
Produktzustände `Ω_A⊗Ω_B`, ihre beiden unabhängigen Ladungssektoren und
der Zwei-Banken-Polraum dürfen nicht ungeprüft in einen überlappenden
Träger übernommen werden. Der gemeinsame Hamiltonoperator und sein Zustand
müssen dort neu beziehungsweise durch einen bewiesenen Adapter konstruiert
werden.

### 7.2 Der vorgeschlagene Kill-Test muss korrigiert werden

Für unabhängige orthogonale Banken kann Π_AΠ_B deren gemeinsame Parität
sein. Für überlappende Unterräume gilt das nicht allgemein; ihre lokalen
Paritäten müssen nicht einmal kommutieren. Der Test
`[U,Π_AΠ_B]=0` ist deshalb im neuen Bild nicht der richtige universelle Test.
Stattdessen muss die tatsächliche globale Parität Π_global separat definiert
und erhalten werden. Ein nichtverschwindender Kommutator mit einer lokalen
Parität belegt zudem allein noch keinen gerichteten Transfer.

### 7.3 Der einfachste False-Positive: Ein Signal ohne Bewegung

Seien `a=c1`, `b=(c1+c2)/√2` auf zwei globalen CAR-Moden und `H=ωN`.
Dann haben die beiden Einteilchen-Chartzustände bereits Überlappung `1/√2`.
In ihrer nichtorthogonalen Basis ist `K=ωS` mit einem nichtverschwindenden
Offdiagonalelement. Trotzdem bleibt die betreffende Wahrscheinlichkeit
zu jeder Zeit genau 1/2. Es wurde nichts transportiert.

Ein belastbarer gemeinsamer Test muss daher mindestens

\[
S_{AB}=\langle\psi_A,\psi_B\rangle,\qquad
K_{AB}=\langle\psi_A,H\psi_B\rangle
\]

und die tatsächliche Zeitantwort gemeinsam bestimmen. Auf einem positiv
definiten Gramträger ist `S^{-1/2}KS^{-1/2}` der korrekte orthonormierte
Operator; bei singulärem S ist zunächst der Nullraum zu quotientieren.
Im Gegenbeispiel ergibt dies nur ωI. Die Offdiagonale von K war kein Hop.

Das trifft sogar unmittelbar den vorhandenen nativen Pol. Dessen
64-dimensionaler Raum besitzt genau **eine** Energie E_h, also
`P_h H P_h=E_h P_h`. Sind A und B nur neue Charts innerhalb dieses selben
Polraums, gilt zwangsläufig `K=E_h S`. Bloßes Umbenennen der 64 entarteten
Polrichtungen erzeugt daher keine Ausbreitung durch H. Eine tatsächliche
globale Dynamik beziehungsweise eine verfügbare aktive Operation muss
hinzukommen und aus der Quelle ausgewiesen werden.

Für die eigentliche TFPT-Lochantwort wäre der gemeinsame Gegenstand

\[
G_{AB}(t)=\langle\Omega,
 f_B^\dagger e^{-it(H-E_0)}f_A\Omega\rangle,
\]

mit einer einzigen Quelle, einem H und einem Ω. `G(0)` bezahlt die schon
vorhandene Überlappung; die dynamische Änderung muss davon unterschieden
werden. Das ist die geschärfte, kleinere nächste Forschungsaufgabe.

### 7.4 Was nicht automatisch folgt

- **Zeit:** Für einen Grundzustand ist `e^{-itH}Ω=e^{-itE0}Ω`; sein physischer
  Zustand bleibt gleich. Das ist kein eigener Zeitpfeil. Nichtstationäre
  Präparation, Korrelationen und Records müssen ausgewiesen werden.
- **Eichfeld:** Für bloße Basiswechsel `Uxy=Vx†Vy` teleskopiert jede
  geschlossene Holonomie zu I. Echte Krümmung braucht zusätzliche
  Verbindungs-/Transportdaten oder einen nachgewiesenen Mechanismus.
- **Spin:** Zwei Orientierungsmarken liefern nicht von selbst einen
  SL(2,C)-Spinor, dessen Transformationsgesetz und Kinetik. Der zusätzliche
  antisymmetrische Zweierfaktor muss unabhängig konstruiert sein.
- **Raum:** Minimale Operationskosten sind ohne Reversibilität zunächst
  gerichtete Kosten, nicht notwendig eine symmetrische Metrik. Kubisches
  Volumenwachstum allein beweist keine 3D-Mannigfaltigkeit, keine
  Lorentzstruktur und keinen gemeinsamen Lichtkegel.
- **Gravitation:** Dynamische Beziehungen sind ein möglicher Träger, aber
  ein masseloser Spin-2-Sektor, zwei Helizitäten, Energiepositivität und
  universelle konsistente Kopplung bleiben zu beweisen.
- **Arithmetik:** Primitive Schleifen besitzen generisch neue gemischte
  primitive Zyklen. Sie sind nicht automatisch Primzahlen. Die Xi-Determinante
  bleibt eine unbewiesene vollständige Operatoridentität. Der getrennte
  RH-Anhang dokumentiert Vorarbeiten, Beispiele und Quellenstatus.

Der Text wird deshalb als **präzisierter globaler Forschungsansatz**
integriert, nicht als Nachweis, dass derselbe unbekannte Baustein schon alle
T1–T8-, RH-, Faktorisierungs-, P/NP- und Hylæan-Fragen beantwortet.

## 8. T1–T8: gemeinsamer Fortschritt ohne Statusinflation

| Front | In dieser Revision weitergekommen | Noch erforderlicher Nachweis |
|---|---|---|
| T1 — Ursprung und Auswahl | Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer | Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand |
| T2 — Half-Charge/E8-Feld | Bestehender geladener Pol bleibt abgesichert, innere Darstellung präzisiert | Renormiertes Half-Charge-Feld mit Energie-/Adjungiertenkontrolle und E8-/Clock-Adapter |
| T3 — gemeinsamer 3+1D-Parent | Kleiner exakter Paartransferzeuge und korrigierter Überlappungstest | Quellenseitig ausgewählter räumlicher Parent auf einem gemeinsamen Hilbertraum und Zustand |
| T4 — chirale Materie | Basisunabhängiger Ausschluss eines konkreten Ein-Kopie-Vektoradapters | Konsistenter chiraler Feldadapter, Maß/Anomalien/Index und Spiegelentkopplung |
| T5 — Kontinuum und Dynamik | Exakte endliche Clock-/Casimir-Kombination und bedingter invarianten Transferblock | Kontrollierter wechselwirkender Grenzübergang, Lorentzverhalten, Clustering und Streuung |
| T6 — Kopplungen und Texturen | Keine neue Herleitung; neue Mischparameter sichtbar zusätzlich | Herkunft aller Kopplungen und vollständiger Neutrinostruktur/-skala |
| T7 — Gravitation | Der falsche pauschale Tensor-Ausschluss bleibt zurückgenommen | Masseloser dynamischer Spin zwei, beide Helizitäten, konsistente universelle Kopplung im selben Parent |
| T8 — Präparation und Auslesung | Gram-/Antworttest gemeinsam formuliert; spezielle Blockerressource konkret | Natives geladenes Instrument, Quellzustandswahl, Records und ein gemeinsames Auslesefunktional |

Keiner der acht vollständigen Abschlussverträge wird in dieser Revision auf
„gelöst“ gesetzt. Gelöst wurden ausdrücklich benannte Teilfragen.

## 9. Die nächsten drei Arbeiten — klein, gemeinsam und entscheidbar

**A. Den gemeinsamen Quellenvertrag wirklich hinschreiben.** Zwei lokale
Einbettungen, ihr CAR-Gram, globale Parität und Ladung, ursprüngliche
Operationen und ein einziges H angeben. Abbruch für eine Kandidatenfassung,
wenn sie nur zwei Koordinatenansichten desselben unveränderten Signals
umbenennt. Die gemeinsamen Generatoren müssen einen nachweislich neuen
Antwortprozess ermöglichen, nicht nur eine andere Beschriftung.

**B. Die fehlende Zwischenoperation ausweisen.** Der Vierzustandszeuge gibt
eine konkrete positive Zieloperation vor. Zu prüfen ist, ob der Compiler
ein geeignetes Mischinstrument oder eine andere geteilte Paarstruktur
wirklich liefert. Clock und Casimire alleine sind kein Herkunftsbeweis.
Zeigt ein erhaltener gemeinsamer Generator die Unmöglichkeit für einen
festen Operationssatz, endet dessen weitere Kommutator-Suche; dann muss
ein anderer bereits vorhandener Quellbestandteil benannt werden.

**C. Dieselbe Anregung und denselben Zustand behalten.** Auf dem Kandidaten
`G_AB(0)` und `G_AB(t)` einschließlich vollständiger Restantwort bestimmen.
Der N=9-Zeuge darf nicht still zum N=64-Lochpol umgedeutet werden. Ein
minimaler Lorentz-/Kinetikadapter muss die nachgerechneten Tensorbedingungen
erfüllen. Erst mit diesem gemeinsamen Anschluss trägt eine großräumige
Skalierungsrechnung.

Der stärkste Vereinfachungsgewinn dieser Runde ist damit konkret:
**Clock und innere Symmetrie sind nicht zwei voneinander unabhängige
Mechanismen; reine Überlappung und echte Bewegung sind dagegen zwei
verschiedene Dinge.** Die weitere Suche sollte diese erste Identität nutzen
und die zweite Unterscheidung im selben kleinen Modell erzwingen.

## 10. Belege und Reproduzierbarkeit

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit
reproduziert die 1127 gelieferten Guards; eigene Programme behandeln
Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion,
basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und
die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den
jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählungen
und Bytevergleiche stehen im Auslieferungs-/Replayprotokoll; interne erneute
Aufrufe der 944 Guards werden nicht mehrfach als neue Tests gezählt.

Die drei ausführlichen parallelen Berichte und der Überlappungs-/RH-Nachtrag
folgen im vollständigen Dokument. Ihr Status ersetzt widersprechende
historische Deutungen, nicht unveränderte ältere Beweise. Das native frühere
Archiv bleibt zusätzlich unverändert im Paket; dessen große frühere
Enumeration wird nicht als in dieser Revision erneut durchgeführt ausgegeben.
