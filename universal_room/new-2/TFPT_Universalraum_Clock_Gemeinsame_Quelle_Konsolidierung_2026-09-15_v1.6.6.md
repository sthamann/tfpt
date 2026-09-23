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


---

# Anhang A: Quellenprüfung Symmetrie und Verfügbarkeit

# Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1–T8 geschlossen seien.

## 1. Reproduktion

Alle drei Programme wurden vollständig gelesen und anschließend in isolierten Kopien ausgeführt. Die relevanten Tensoren wurden an ihre von den unveränderten Programmen erwarteten relativen Orte kopiert. Normaler und optimierter Lauf reproduzieren jeweils die gelieferten Ergebnisdateien byteidentisch, ohne Standardfehlerausgabe:

| Programm | Gelieferte Prüfbedingungen | Reproduktion |
|---|---:|---|
| `operation_symmetry.py` | 944 | PASS, identisch |
| `symmetry_availability.py` | 31 | PASS, identisch |
| `lorentz_types.py` | 152 | PASS, identisch |
| Summe | 1127 | normal und `-OO` |

Die Zusatzprüfung `check_scope.py` rechnet kleine exakte Gegenprüfungen zur Reichweite der Aussagen. Das ausführbare Reproduktionsprogramm ist `replay.py`; Quellenpins, Kopien, Originalberichte und Ausgaben liegen in diesem Auditordner. `replay_receipt.json` dokumentiert alle Pins und die Unverändertheit der Eingaben.

Programm-Pins:

| Quelle | SHA-256 |
|---|---|
| `operation_symmetry.py` | `ec93f759d6582f42542a597bf916ee2a62a51c510240aa777ae439e90fe28382` |
| `symmetry_availability.py` | `88cc3e3361a198fe7b1b32a7174f3dd45f341106978d8abd8d5722e0cb631967` |
| `lorentz_types.py` | `43777c81ea8ba2d2ae12b711321a54abd7f7152a326611a296598d5c5dd463da` |
| Nativer Tensor | `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763` |

Die Erzählung über zwei unabhängig entstandene, vollständig übereinstimmende Programme ist durch diese Reproduktion **nicht** geprüft: Vorgelegen hat die erhaltene Fassung mit 944 Guards, nicht die vorherige Fassung mit 528 Guards.

## 2. Bestätigte Mathematik

Der N=3-Raum zerfällt als Darstellung von Spin(10) × SU(4) in sieben Isotypien. Drei haben Multiplizität zwei, die anderen vier Multiplizität eins. Die zwei Fockteile Λ³(C⁶⁴) und C⁶⁰⊗C⁶⁴ sind jeweils multiplizitätsfrei; der gesamte N=3-Raum ist es ausdrücklich **nicht**.

Die irreduziblen Dimensionen sind 24000, 11200, 2688, 2880, 576, 320, 64; die mit Multiplizitäten gewichtete Summe ist 45504. Die Spin(10)-Darstellung mit Dimension 16 in BF und Λ³ ist in den angegebenen Gewichten die konjugierte Spinordarstellung; die Dimensionskurzschreibweise `16` darf diese Information nicht ersetzen.

Bestätigt sind:

- die exakte Zerlegung über Gewichtsmultiplizitäten und Racah-Alternation;
- `C(560)=117/4` in der erklärten Casimir-Normierung;
- die Quellenintertwiner für alle 60 Lie-Erzeuger;
- `rank C3=3776`, `dim ker C3=37888`;
- Spektrum von `C3 C3†`: 0,7,10,12 mit Multiplizitäten 64,2880,576,320;
- die drei dunklen Typen mit Gesamtcasimir 45, aber getrennten Spin-Casimiren 141/4,117/4,165/4;
- für den **gewährten** Satz X,Nb eine assoziative Algebra der komplexen Dimension 14;
- für alle punktweise symmetrieinvarianten Operatoren die Dimension 16;
- nach zusätzlicher Gewährung aller 60 Gruppenerzeuger die assoziative Dimension 743583744 und Kommutantdimension 7.

Die Eigenwertzuordnung im Code prüft pro S-Eigenwert einen Vektor, nicht eine vollständige Basis dieses Eigenraums. Zusammen mit der unabhängig geprüften Multiplizitätsfreiheit, der Kommutation mit allen Erzeugern und der eindeutigen Dimensionszuordnung der BF-Teilsummen ist die Zuordnung trotzdem abgesichert. Die Guard-Beschriftung »entire eigenspace« ist als direkte Beschreibung dieser einen Rechnung zu weit.

## 3. Invarianz und Kovarianz auseinanderhalten

Mit `A0=Alg*(X,Nb)` und Gruppenwirkung ρ bezeichne

`C = End_G(H3) = ⊕_i End(C^{m_i}) ⊗ I_{d_i}`.

Dann gilt `A0 ⊂ C`, `dim A0=14` und `dim C=Σ m_i²=16`. Jedes Wort aus X und Nb kommutiert mit ρ(G). Nichtzentrale Lie-Erzeuger können deshalb aus diesem Alphabet nicht entstehen. Dieser Ausschluss ist korrekt und bleibt richtig, wenn nur ein fixes H statt zweier unabhängiger Kontrollen gewährt ist.

Nach Gewährung der Gruppenerzeuger entsteht dagegen

`Afull = ⊕_i End(C^{m_i} ⊗ V_i)`.

Diese Algebra ist **unter Gruppenkonjugation stabil**, aber ihre Operatoren sind nicht sämtlich invariant. In `symmetry_availability.py` ist die Kennzeichnung `symmetry_invariant: true` für diese Zeile daher falsch. Der Kommutant von Afull ist die sieben-dimensionale skalare Blockmitte.

Sieben ist ein Boden, solange alle zusätzlichen Operationen diese sieben Isotypie-Projektoren erhalten; insbesondere senken zusätzliche punktweise G-invariante Operationen den bereits erreichten Kommutanten nicht weiter. Sieben ist aber **kein** universeller Boden für unter G stabile Algebren oder alle denkbaren nativen Verträge. `End(H3)` ist unter jeder Gruppenkonjugation stabil und hat nur den skalaren Kommutanten. Ein exaktes 2×2-Gegenmodell in der Zusatzprüfung macht die Unterscheidung direkt sichtbar.

Die Zahlen sind zudem Dimensionen **komplexer assoziativer Sternalgebren**, keine nachgewiesenen Dimensionen einer dynamischen Lie-Algebra oder erreichbaren Unitärgruppe. Burnside liefert nicht automatisch beliebige ausführbare Gatter auf jedem irreduziblen Block.

## 4. Verfügbarkeit ist keine universelle Ja/Nein-Frage

Ein vorgegebener Hamiltonoperator allein gewährt nicht bereits das unabhängige Schalten von X und Nb. Am erklärten Punkt g/Δ=1/20 besitzt ein fixes H im N=3-Raum acht verschiedene Energien, also nur eine acht-dimensionale kommutative Spektralalgebra. Die großzügigere Annahme unabhängiger Kontrollen X,Nb ergibt 14.

Eine treue, auf die Multiplizitätsräume reduzierte rationale Matrixrechnung ergibt:

| Zusätzlich gewährter Satz | Assoziative Dimension |
|---|---:|
| Nur fixes H=Nb+X/20 | 8 |
| X,Nb | 14 |
| X,Nb plus Projektor auf genau einen dunklen Typ | 15 |
| X,Nb plus Spin(10)-Casimir | 16 |
| X,Nb plus SU(4)-Casimir | 16 |
| X,Nb plus Gesamtcasimir | 14 |

Bereits **einer** der getrennten Casimire reicht zur vollständigen Trennung der drei dunklen Typen. Die zwei fehlenden Algebradimensionen sind kein Beweis, dass genau zwei physische Griffe fehlen. Die Dimension 15 zeigt eine mögliche invariante Zwischenstufe. Die behauptete universelle Dichotomie »getrennte Griffe ja oder unverändert 14« und das `IF AND ONLY IF` zur Verfügbarkeit der vollen Symmetrie sind daher zu stark.

Die zusätzlichen Projektoren und Casimirkontrollen werden hier nur als algebraische Gegenbeispiele verwendet. Ihre Implementierung aus dem Compiler wird nicht behauptet.

## 5. Der Clock-Satz ist im gelieferten Checker nicht geprüft

`operation_symmetry.py:478` schreibt den Normalisator- und Nichts-hinzufügen-Satz als `need(True, ...)`. Insgesamt enthält diese Datei neun solche als Prüfbedingungen gezählten theoretischen Folgerungen. Einige sind durch die vorausgehende Mathematik gut begründet; der bloße grüne Guard zertifiziert sie jedoch nicht unabhängig.

Die direkte Clock-Definition liegt in `universalraum-native-operations-ground-response-20260915/common.py`, Funktion `clock_lift`, ab Zeile 187: eine Permutation der fünf Oszillatorachsen wird mit Exterior-Vorzeichen auf den geraden Spinorraum gehoben; `GF=G16⊗I4`. Der Bosonlift wird entsprechend gebaut und die Tensorintertwining-Gleichung geprüft. Eine neue direkte Prüfung der Clock-/Casimir-Beziehungen erfolgt im parallelen Hauptstrang, nicht in diesem Audit.

## 6. Feldtyp: was tatsächlich erzwungen ist

Für ein **lokales, ableitungsfreies Bilinear zweier gleichhändiger Weylfelder**, das alle 64 inneren Quellenmarken unverändert als unabhängige innere Komponenten und genau den gegebenen antisymmetrischen Tensor W verwendet, gilt

`(1/2,0) ⊗ (1/2,0) = (1,0) ⊕ (0,0)`.

Die skalare Epsilon-Kontraktion zusammen mit antisymmetrischem W ist im gemeinsamen Index symmetrisch und verschwindet wegen Grassmann-Antikommutation. Der symmetrische Spinortensor, also der (1,0)-Kanal, bleibt nichtverschwindend. Im genannten Vertrag ist dies korrekt. Ein zusätzliches unabhängiges gleichgeladenes Hilfsdublett erlaubt stattdessen wieder die skalare Kontraktion.

Die Zahlen 180/128 beziehungsweise 60/256 zählen **komplexe lokale Feldkomponenten im jeweiligen direkten Tensorprodukt-Ansatz**. Sie zählen nicht automatisch zusätzliche unabhängige physische Oszillatoren oder propagierende Freiheitsgrade. Diese hängen von Kinetik, Nebenbedingungen, positiver Energie, Teilchen-/Antiteilchenstruktur und dem tatsächlichen Feldadapter ab. Deshalb folgt aus der Multiplikation mit zwei oder drei kein allgemeiner Ausschluss jeder relativistischen Lesart mit den nativen Modenzahlen.

Vor allem folgt daraus keine vorgeschriebene Reihenfolge »erst räumliche Skalierung, dann Feldwörterbuch«. Lokale Darstellungstypen und mögliche Kinetik können vor einer Skalierungsrechnung geprüft werden. Welche Feldkomponenten tatsächlich aus dem räumlichen Quellprozess entstehen, muss anschließend gemeinsam mit dem Adapter untersucht werden.

### Konkreter Gegencheck jenseits der ableitungsfreien Klasse

Der allgemeine Satz »ein Vektor verlangt ψ†ψ und scheitert deshalb an der Ladung« ist falsch, sobald Ableitungen zugelassen werden. Beispielsweise ist

`J^A_mu = Σ_IJab M^A_IJ ε_ab ψ_Ia ↔∂_mu ψ_Jb`

ein Lorentzvektor mit Ladung −2. Die Ableitungsantisymmetrisierung macht ihn bei antisymmetrischem M nichtverschwindend. Für M=ε und zwei inneren Marken liefert die exakte Grassmann-Jetrechnung vier nichtverschwindende Monome mit Koeffizienten +2,−2,−2,+2. Ein entsprechend geladener Vektorvermittler könnte algebraisch durch `b†_mu J^mu + h.c.` koppeln, ohne Ladungsverletzung.

Das ist **nur ein Gegenbeispiel gegen den überbreiten Ausschluss**, keine native Lösung: Es fügt eine Ableitung und einen Feldtyp hinzu; bei kanonischen 4D-Felddimensionen ist es ein höherdimensionaler Kopplungsterm. Gesunde Kinetik, Quellenherkunft, Skalierung und T1–T8 werden dadurch nicht bewiesen.

## 7. Konsequenz

Die neuen Quellen verkleinern und präzisieren den endlichen N=3-Operationsraum. Sie schließen weder die physische Verfügbarkeit der Operationen noch den Lorentzadapter. Die sachlich tragfähige Integration übernimmt die Zerlegung, Casimire, 14/16/7 im jeweils erklärten Vertrag sowie den eingeschränkten Feldtypsatz; sie ersetzt die überbreiten Ausschlüsse und die behauptete Programmumkehr durch explizite Bedingungen.


---

# Anhang B: unabhängige Krylov- und Feldprüfung

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


---

# Anhang C: minimaler Transfer und seine Quellen-Grenze

# Minimaler Ursprungsstrang: geteilte Moden und ein echter nativer Vierzustandskanal

Stand: 15. September 2026. Unabhängiger, begrenzter Forschungsstrang.

## Ergebnis und Reichweite

Es gibt zwei verschiedene Ergebnisse, die ausdrücklich nicht verwechselt werden dürfen:

1. **Ein exakt lösbarer Überlappungsbaustein:** Eine gemeinsame Fermionmode und ein gemeinsamer Bosonkanal werden in jedem festen positiven Ressourcensektor zu einer gewöhnlichen effektiven Fermionmode. Dafür ist keine direkte Endpunkt-Hopping-Wechselwirkung nötig. Dieser Dreierstern ist jedoch **kein Ausschnitt einer tatsächlichen nativen W-Zeile**.
2. **Ein tatsächlicher W-basierter Vierzustandskanal:** Im unveränderten 64-Fermion/60-Boson-Paartensor existiert ein exakt invariantes Vierzustandsystem, wenn ein **zusätzlicher reiner Bosonmischer** zwischen Kanal 0 und 1 zugelassen und ein bestimmter Zustand mit Gesamtladung 9 präpariert wird. Der vollständige native Hamiltonoperator plus dieser Mischer überträgt dort eine innere Fermionmarke mit einer streng abgesicherten Wahrscheinlichkeit von **mehr als 99,3 %**.

Das zweite Ergebnis benötigt keine Projektion, die die übrigen nativen Zustände künstlich wegschneidet: Der Vierzustandsraum ist unter allen 60 ursprünglichen Paaroperatoren plus dem Mischer exakt invariant. Es ist aber **weder eine Untersuchung der Entnahmeantwort des N=64-Grundzustands noch ein Transport zwischen zwei unabhängigen Banken**. Die Herkunft des Bosonmischers, die spezielle Präparation und die räumliche Bedeutung der Marken bleiben offen.

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

\[
\Pi_x=(-1)^{N_{f,x}},\qquad \Pi_y=(-1)^{N_{f,y}}
\]

gegeben. Kommutiert jede ausführbare lokale Operation und jeder einzelne realisierte Messzweig mit beiden Paritäten, gilt dies auch für beliebige Produkte, Summen, Adjungierte und starke beschränkte Grenzwerte. Eine Clockoperation, die lediglich innerhalb jeder Bank Fermionmoden zahlenerhaltend permutiert, bleibt in dieser Algebra.

Ein echter Einfermiontransfer erfüllt dagegen

\[
\Pi_x f_y^\dagger f_x=-f_y^\dagger f_x\Pi_x,
\qquad
\Pi_y f_y^\dagger f_x=-f_y^\dagger f_x\Pi_y.
\]

Er kann daher nicht allein durch mehr Kompositionen jener Operationen entstehen. Eine bloß paritätskovariante CP-Abbildung ist nicht die gleiche Voraussetzung: Sie kann ungerade Krauszweige besitzen. Die Aussage gilt nur für den ausdrücklich geraden ausführbaren Operationssatz.

Bei geteilten Fermionmoden sind die beiden lokalen CAR-Algebren von Anfang an nicht unabhängig. Liegt dieselbe Mode s in beiden, kann sie nicht zugleich als zwei unabhängige antikommutierende Kopien behandelt werden: \(\{s,s^\dagger\}=1\). Auch lokale Ladungen, die s doppelt mitzählen, sind keine unabhängigen additiven Bankladungen. Überlappung widerlegt somit den Paritätssatz nicht, sondern ändert seine Voraussetzungen.

## 2. Exakter CAR-Baustein aus einem geteilten Boson und Fermion

Betrachtet werden drei CAR-Moden \(f_x,s,f_y\), ein CCR-Boson b und

\[
Q_x=b^\dagger s f_x,\qquad Q_y=b^\dagger s f_y,
\qquad
H_\star=\Delta N_b+g(Q_x+Q_y+Q_x^\dagger+Q_y^\dagger).
\]

Der Ressourcenzähler

\[
K=N_b+n_s
\]

kommutiert mit allen diesen Operationen. Auf jedem exakten K-Sektor mit ganzzahligem \(K\ge1\) setze

\[
c^\dagger=\frac{b^\dagger s}{\sqrt K},\qquad
c=\frac{s^\dagger b}{\sqrt K}.
\]

Direkt aus CCR und CAR folgen

\[
(c^\dagger)^2=c^2=0,\qquad
\{c,c^\dagger\}=\frac{N_b+n_s}{K}=1.
\]

Die Mode c antikommutiert mit beiden Endpunktmoden. Ferner

\[
N_b=K-1+n_c,
\qquad
N_f+2N_b=2K-1+n_x+n_c+n_y.
\]

Damit gilt exakt

\[
\boxed{
H_\star=\Delta(K-1)+\Delta n_c
 +g\sqrt K\big(c^\dagger f_x+c^\dagger f_y+\mathrm{h.c.}\big).
}
\]

Die gewöhnliche Drei-Moden-Transferkette wurde hier aus einer überlappenden Paarumwandlung erhalten. Ein nützlicher Operatorausdruck derselben Tatsache ist

\[
\boxed{[Q_y^\dagger,Q_x]=K f_y^\dagger f_x.}
\]

Das ist zunächst eine Operatoridentität. Die Verfügbarkeit getrennter Kommutator-Kontrollsequenzen folgt daraus nicht automatisch. Schon der konstante Summen-Hamiltonoperator zeigt jedoch Transfer. Der minimale positive Ressourcensektor K=1 benötigt am Anfang eine besetzte gemeinsame Fermionmode s und ein leeres Boson.

### Vollständige Transferrechnung im Vergleichsmodell

Im effektiven Einteilchenraum und bei K=1 lautet die Matrix

\[
\begin{pmatrix}0&g&0\\g&\Delta&g\\0&g&0\end{pmatrix}.
\]

Der antisymmetrische Endpunktzustand ist dunkel. Der symmetrische koppelt mit \(\sqrt2g\) an c. Für \(g/\Delta=1/20\), \(m=101\) und

\[
t=\frac{202\pi}{\Delta\sqrt{51/50}}
\]

verschwindet die mittlere Besetzung wieder exakt. Die Zielwahrscheinlichkeit ist

\[
p_\star=\sin^2\left[\frac\pi2\,101\left(1-\sqrt{50/51}\right)\right].
\]

Durch Quadrieren rationaler Schranken erhält man

\[
\frac{199}{200}<101\left(1-\sqrt{50/51}\right)<1.
\]

Mit \(|\sin u|\le|u|\) und \(\pi<355/113\) folgt

\[
p_\star>1-\left(\frac{355/113}{400}\right)^2>0.9999.
\]

Diese Zahl gehört **nur zum Vergleichsmodell mit gemeinsamem b**.

### Die direkte Quellen-Grenze

Die tatsächliche native W-Zeile enthält jeweils acht disjunkte Fermionpaare, also 16 verschiedene Marken. Eine einzelne Zeile enthält deshalb niemals zugleich \(s f_x\) und \(s f_y\) mit \(x\ne y\). Das ist an allen 60 Zeilen exakt geprüft.

Ein gemeinsamer-b-Dreierstern darf somit nicht allein wegen der Form \(b^\dagger f f\) als nativer Baustein bezeichnet werden. Insbesondere wäre ein Wechsel von zwei Bosonkanälen zu einer gemeinsamen Mode ohne Kontrolle des orthogonalen Kanals eine zusätzliche Modellannahme.

## 3. Exakter Vierzustandskanal mit dem vollständigen nativen W

Die gepinnte Quelle ist

`universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz`,

SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die zwei relevanten Quellenzeilen sind

\[
\begin{aligned}
P_0={}&-f_{57}f_4+f_{56}f_5+f_{53}f_8-f_{52}f_9
       -f_{45}f_{16}+f_{44}f_{17}+f_{33}f_{28}-f_{32}f_{29},\\
P_1={}&-f_{58}f_4+f_{56}f_6+f_{54}f_8-f_{52}f_{10}
       -f_{46}f_{16}+f_{44}f_{18}+f_{34}f_{28}-f_{32}f_{30}.
\end{aligned}
\]

Die Konvention ist \(P_A=\sum_{i<j}W_{A,ij}f_jf_i\). Das gemeinsame aktive Fermion ist s=4; die Endpunktmarken sind 57 und 58.

Präpariert werden sieben unveränderte Pauli-Blocker

\[
S=\{8,16,28,32,44,52,56\}.
\]

Sei \(|S\rangle\) der geordnet erzeugte Fockzustand dieser Moden. Die vier Basiszustände sind

\[
\begin{array}{c|c|c}
\text{Zustand}&\text{besetzte Fermionmoden}&\text{Bosonen}\\\hline
L&S\cup\{4,57\}&0\\
B_0&S&1\text{ in Kanal }0\\
B_1&S&1\text{ in Kanal }1\\
R&S\cup\{4,58\}&0
\end{array}
\]

Jeder Zustand besitzt die native Gesamtladung \(N=N_f+2N_b=9\).

Zugelassen wird nun genau eine zusätzliche Hamiltonoperation,

\[
H_J=J(b_1^\dagger b_0+b_0^\dagger b_1).
\]

Alle ursprünglichen 60 nativen Paaroperatoren bleiben erhalten:

\[
H=\Delta N_b+g\sum_{A=0}^{59}(b_A^\dagger P_A+P_A^\dagger b_A)+H_J.
\]

Der Prüfer wendet sämtliche 480 signierten Paarkanäle einschließlich aller CAR-Vorzeichen und der Bosonfaktoren auf jeden der vier Zustände an. Es entstehen **keine Zustände außerhalb ihres linearen Spanns**. Die Pauli-Blocker verhindern insbesondere die sieben unerwünschten Rückpaarungen jedes aktiven Bosonkanals.

Es ergibt sich exakt

\[
\boxed{
H_4=\begin{pmatrix}
0&g&0&0\\
g&\Delta&J&0\\
0&J&\Delta&g\\
0&0&g&0
\end{pmatrix}_{(L,B_0,B_1,R)}.
}
\]

Ohne Mischer, J=0, zerfällt die Matrix in zwei getrennte 2×2-Blöcke. Dann ist \(\langle R|e^{-itH}|L\rangle\) zu jeder Zeit exakt null. Mit J ungleich null beginnt die Transferamplitude bei dritter Ordnung; die Wahrscheinlichkeit hat den führenden Term \(g^4J^2t^6/36\).

**Die Quelle enthält hier also die beiden Endstücke und eine exakt funktionierende Pauli-Blockierung, aber nicht die geprüfte Bosonverbindung als bereits verfügbare Operation.**

## 4. Strenge vollständige Transfergrenze im tatsächlichen W-Zeugen

Unter Spiegelung L↔R und B₀↔B₁ zerfällt H₄ in

\[
H_+=\begin{pmatrix}0&g\\g&\Delta+J\end{pmatrix},\qquad
H_-=\begin{pmatrix}0&g\\g&\Delta-J\end{pmatrix}.
\]

Wähle den vorhandenen Prüfquotienten \(g/\Delta=1/20\) und die ausdrücklich neu gesetzte Mischerstärke

\[
J=\Delta-\frac{2g}{\sqrt3}
 =\Delta\left(1-\frac1{10\sqrt3}\right),
\qquad t=\frac{\pi\sqrt3}{g}=\frac{20\pi\sqrt3}{\Delta}.
\]

Da \(0<J<\Delta\), bleiben die Eigenfrequenzen des Bosonmischers \(\Delta\pm J\) positiv. Es wurde **keine Nullfrequenz durch exakte Aufhebung von \(\Delta N_b\)** erzeugt. Auch auf dem ganzen Fockraum bleibt die hinzugefügte Hamiltonfamilie nach unten beschränkbar: Das Bosonquadrat ist strikt positiv und die endlichen Fermionoperatoren können durch quadratische Ergänzung kontrolliert werden. Das bedeutet nicht, dass ihr Grundzustand noch der unveränderte native Grundzustand ist.

Für H₋ ist \(\Delta-J=2g/\sqrt3\). Zu der gewählten Zeit kehrt dessen Endpunktkomponente exakt mit Phase −1 zurück, ohne mittlere Restbesetzung.

Für H₊ setze

\[
a=\Delta-\frac g{\sqrt3},\quad
\omega=\sqrt{a^2+g^2},\quad
w_- =\frac{1-a/\omega}{2}.
\]

Die Endpunktamplitude lautet

\[
A_+=(1-w_-)e^{i(\omega-a)t}+w_-e^{-i(\omega+a)t}.
\]

Mit \(\omega-a\le g^2/(2a)\), \(w_-\le g^2/(4a^2)\),
\(\cos u\ge1-u^2/2\) und
\(|A_+|^2\ge1-g^2/a^2\) folgt

\[
\begin{aligned}
p_{L\to R}
 &=\left|\frac{A_++1}{2}\right|^2\\
 &\ge1-\frac{g^4t^2}{16a^2}-\frac{g^2}{2a^2}\\
 &=1-\frac{3\pi^2+8}{6400(a/\Delta)^2}.
\end{aligned}
\]

Aus \(\sqrt3>17/10\) folgt \(a/\Delta>33/34\). Somit ergibt sich rein rational

\[
\boxed{
p_{L\to R}>
1-\frac{3(355/113)^2+8}{6400(33/34)^2}
=\frac{2009992727}{2022609600}
>0.9937620819>0.993.
}
\]

Die Aussage ist eine **analytische Schranke der vollständigen Dynamik auf einem exakt invarianten Quellen-Unterraum**. Es gibt hier keinen numerisch abgeschnittenen Restzustandsraum. Die 64-Fermion/60-Boson-Quelle ist nicht durch vier frei erfundene Matrixeinträge ersetzt worden: Ihre exakte Einschränkung wurde zuerst vollständig geprüft.

Die Zeit in Einheiten \(\hbar=1\) ist ungefähr \(108.83/\Delta\). Diese numerische Orientierung und die gesetzte Mischerstärke sind keine vorhergesagten Naturkonstanten.

## 5. Was dies für die fundamentale Suche ändert

Der konstruktive Anschluss ist klein: **Paarumwandlung → geteilte Zwischenressource → Paar-Rückumwandlung** kann einen Einfermion-Endpunktwechsel bewirken. Für die tatsächliche W-Quelle braucht man dazu weder einen neuen direkten Fermion-Hopping-Term noch die Kontrolle jedes einzelnen der 480 Paarmonome. Ein einzelner Bosonmischer plus eine spezielle Pauli-blockierte Präparation reicht im belegten internen Zeugen.

Offen bleiben aber genau die folgenden Herkunftsfragen:

1. **Operationssatz:** Ist der reine Mischer \(b_1^\dagger b_0+\mathrm{h.c.}\) tatsächlich verfügbar? Eine simultane Fermion-und-Boson-Symmetrie ist nicht automatisch eine unabhängige Bosonoperation.
2. **Präparation:** Wie wird der N=9-Blockerzustand mit dem zugelassenen Operationssatz erzeugt? Ladungserhaltende native Evolution präpariert ihn nicht aus dem N=64-Grundzustand.
3. **Operationaler Raum:** Sind die Endpunktmarken 57 und 58 überhaupt verschiedene räumliche Teile oder nur interne Marken derselben Bank? Die Rechnung allein liefert keine Raumposition.
4. **Gemeinsamer Grundzustand:** Besteht ein entsprechender Mechanismus für die ursprüngliche Entnahmeantwort des nativen N=64-Grundzustands, statt für diesen besonders präparierten Zeugen?
5. **Zwei Banken:** Eine Bosonverbindung zwischen wirklich unabhängigen Banken erhält deren lokale Fermionparitäten. Dieser interne Zeuge hebt jene Schranke nicht auf. Dafür wäre eine ursprünglich geteilte Fermionstruktur oder eine andere insgesamt gerade, lokal ungerade Quelloperation zu konstruieren.

T1–T8, das relativistische Feldwörterbuch und die Herkunft der Raumzeit sind damit nicht geschlossen. Das Ergebnis verkleinert eine konkrete Suche: Statt eines völlig beliebigen neuen Fermionlinks kann jetzt ein bestimmter Bosonmischer mitsamt seinem Quellen- und Präparationsvertrag geprüft werden. Die nachfolgende Quellenprüfung weist diesen Mischer jedoch ausdrücklich **nicht** als Synthese der bisher gewährten Kontrollen aus.

## 6. Anschluss des neuen Chart-/Glue-Vorschlags und exakter Quellen-No-go

Der neue Nutzeranhang vom 15. September 2026 wurde vollständig gelesen:

`/Users/stefanhamann/.codex/attachments/59dc0059-8914-48ca-953d-85933f66e00b/pasted-text.txt`,

SHA-256 `1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

Die Hypothese, Banken zunächst als überlappende lokale Beschreibungen einer gemeinsamen CAR-Struktur zu untersuchen, passt zum hier konstruierten gemeinsamen Fermion-/Boson-Zwischenraum. **Sie löst den Übergang von Überlappung zu Dynamik aber nicht automatisch.** Bereits zwei nichtorthogonale lokale Moden \(f_A=f_1\), \(f_B=\cos\theta f_1+\sin\theta f_2\) bei H=0 besitzen ein nichtverschwindendes Kreuz-Antikommutator \(\{f_A,f_B^\dagger\}=\cos\theta\), obwohl überhaupt keine Zustandsentwicklung stattfindet. Eine Änderung der Beschreibung und ein dynamischer Transfer müssen getrennt geprüft werden.

### 6.1 Eine nötige Korrektur des vorgeschlagenen Paritätstests

Der Anhang fordert für überlappende Charts einen Intertwiner, der lokal Paritäten ändert, aber mit \(\Pi_A\Pi_B\) kommutiert. **Bei Überlappung ist dieses Produkt nicht automatisch die Gesamtparität.** Im kleinsten gemeinsamen-Moden-Zeugen

\[
A=\{x,s\},\qquad B=\{s,y\}
\]

gilt

\[
\Pi_A\Pi_B=(-1)^{n_x+n_y},
\qquad
\Pi_{\rm global}=(-1)^{n_x+n_s+n_y}.
\]

Die gemeinsame Mode s wurde im Produkt zweimal gezählt und fällt heraus. Die Paarumwandlung \(b^\dagger s f_x\) ist bezüglich \(\Pi_{\rm global}\) gerade, kommutiert aber nicht mit \(\Pi_A\Pi_B\). Der vorgeschlagene Kill-Test würde hier einen legitimen global geraden Überlappungsmechanismus fälschlich aussortieren. Alle vier Identitäten wurden auf dem vollständigen Drei-Fermion-CAR-Raum exakt geprüft.

**Der korrigierte Test muss die globale Parität aus der gemeinsamen CAR-Darstellung selbst verwenden**, nicht aus einem ungeprüften Produkt lokaler Paritäten. Zusätzlich benötigt er eine definierte Anfangspräparation, dynamisch unterschiedliche Endpunktbeobachtungen und einen aus der Quelle stammenden Generator. Passive Chartwechsel allein reichen nicht.

### 6.2 Tatsächlicher endlicher Clock statt unterstellter voller Gruppe

Die Prüfung lädt den gepinnten ursprünglichen Clock-Konstruktor über

`sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py`,

SHA-256 `2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994`.

Der Konstruktor kontrolliert seine ursprünglichen Quellenpins und die exakte W-Kovarianz. Er liefert tatsächlich

\[
p=(2,0,1,4,3),\qquad s_{\rm Clock}=-1,
\]

und auf Bosonmoden \(A=6k+c\)

\[
G_B e_{6k+c}=-e_{6(p(k\bmod5)+5\lfloor k/5\rfloor)+c}.
\]

Es wird **nicht** vorausgesetzt, dass der Clock der volle Spin(10)×SU(4)-Operationssatz ist. Sein endlicher, direkt reproduzierter Lift reicht für den folgenden Ausschluss.

Schreibe \(M_{ij}=|i\rangle\langle j|+|j\rangle\langle i|\) auf dem Boson-Einteilchenraum. Exakt gilt

\[
G_BM_{01}G_B^\dagger=M_{12,13},\quad
G_BM_{12,13}G_B^\dagger=M_{6,7},\quad
G_BM_{6,7}G_B^\dagger=M_{01}.
\]

Insbesondere

\[
\|[G_B,M_{01}]\|_F^2=4\ne0.
\]

Die native W-Kovarianz impliziert \([G,H]=[G,N_b]=0\) für den gemeinsamen Fock-Lift G. Auch ein gewährter getrennter Gesamt-Casimir von Spin(10) oder SU(4) kommutiert mit diesem tatsächlichen G. Daher liegt

\[
\operatorname{Alg}(H,N_b,G,C_{\rm Spin},C_{\rm Color})\subset\{G\}'
\]

und der spezifische Einzelmischer \(b_1^\dagger b_0+\mathrm{h.c.}\) liegt **nicht** in dieser erzeugten Algebra. Auf den endlichen Ladungssektoren gibt es dabei keine Domänenprobleme; für die volle Hilbert-Darstellung formuliert man dieselbe Aussage mit den erzeugten beschränkten Zeitentwicklungen und Spektraloperationen.

### 6.3 Clock-Mittelung ist möglich, aber der Farb-Cartan sperrt sie weiterhin

Der Clock-Ausschluss allein wäre zu schwach. Die Orbitsumme

\[
M_{\rm orb}=M_{01}+M_{12,13}+M_{6,7}
\]

kommutiert exakt mit \(G_B\). Ihre beiden zusätzlichen Linkblöcke wirken auf den vier Zuständen aus Abschnitt 3 null. Ein neu zugelassener globaler Bosonmischer \(J b^\dagger M_{\rm orb}b\) erzeugt deshalb **denselben** exakt invarianten Vierzustandskanal und dieselbe Transfergrenze. Ein neuer globaler Zusammenhang muss also nicht zwingend den endlichen Clock brechen.

Es gibt jedoch einen zweiten, stärkeren gemeinsamen Erhaltungssatz. Aus dem tatsächlichen Quell-Gewichtswörterbuch wählen wir die zweite SU(4)-Cartankomponente und definieren den gemeinsamen Ladungsoperator

\[
Q=\sum_r q_r n_{f,r}+\sum_A q_A n_{b,A}.
\]

Jeder ursprüngliche Paarterm erfüllt exakt \(q_i+q_j=q_A\); dies wird für alle 480 Quellenpaare geprüft. Der tatsächliche Clock wirkt auf dem Spinindex und lässt die SU(4)-Farbkomponente unverändert. Daher

\[
[Q,H]=[Q,N_b]=[Q,G]=0.
\]

Die getrennten Gesamt-Casimire kommutieren ebenfalls mit diesem Cartan. Diese Aussage erfordert **keine** Verfügbarkeit aktiver kontinuierlicher SU(4)-Kontrollen.

Auf den beiden Bosonkanälen gilt dagegen

\[
q_0=0,\qquad q_1=2,
\]

und auf dem ganzen Boson-Einteilchenraum

\[
\|[Q_B,M_{01}]\|_F^2=8,\qquad
\|[Q_B,M_{\rm orb}]\|_F^2=24.
\]

**Damit sind sowohl der Einzelmischer als auch seine Clock-invariante Orbitsumme aus dem genannten Operationssatz ausgeschlossen.** Die Mittelung beseitigt das Clock-Hindernis, nicht den separaten Farb-Cartan-Erhaltungssatz.

Die tatsächlichen Cartanladungen im Vierzustandsraum sind

\[
(Q_L,Q_{B_0},Q_{B_1},Q_R)=(7,7,9,9).
\]

Dieser Zeuge verändert also eine innere SU(4)-Quantenzahl. Er ist noch deutlicher als ein bloßer Markenwechsel vom Transport **derselben** niedrigenergetischen Fermionmode zwischen zwei räumlichen Banken zu unterscheiden.

### 6.4 Kleinste noch zu suchende Quellressource

Für den hier exakt spezifizierten Zeugen fehlt mindestens eine Operation, die nicht mit dem betrachteten Farb-Cartan des ursprünglichen Systems kommutiert, oder eine aus einer erweiterten globalen Quelle abgeleitete Kopplung mit einer **expliziten Ausgleichsressource für diese Cartanladung**. Ein zusätzlicher aktiver SU(4)-Generator wäre ein neuer Operationsvertrag; außerdem bewegt sein simultaner Fermion-/Boson-Lift im Allgemeinen auch die Blocker und ist nicht mit dem reinen Bosonmischer gleichzusetzen.

Die Befunde schließen nicht alle globalen Glue-Modelle aus. Sie zeigen präzise, warum der konkret schon gelöste Vierzustandstransfer noch keine Herkunftslösung ist und welche neue algebraische Eigenschaft eine echte Quellenfortsetzung besitzen müsste. Für eine überwiegend kinematische Chart-Interpretation muss zusätzlich gezeigt werden, dass diese Erweiterung eine tatsächliche Dynamik und nicht bloß eine Basisumbenennung erzeugt.

## Reproduktion und Status

`verify.py` prüft **307 Bedingungen**, verwendet keine Python-Assertions und reproduziert normal sowie mit `-OO` byteidentische JSON-Ergebnisse. Die Prüfung enthält:

- CAR und Ladungsbuchhaltung für den geteilten Baustein in K=1,2,3;
- die rationale Transfergrenze des klar getrennten Vergleichssterns;
- die Matching-Eigenschaft aller 60 nativen W-Zeilen;
- die volle symbolische Wirkung aller 480 nativen Paarterme auf alle vier Zeugen-Zustände;
- die zusätzliche Mischerwirkung, exakte Invarianz und vollständige Spiegelungszerlegung;
- die rationale Schranke größer 99,3 % bei strikt positiver Bosonfrequenz.
- den tatsächlich konstruierten Clock, den Einzelmischer-Ausschluss und die Clock-invariante Orbitsumme;
- die gemeinsame Farb-Cartan-Erhaltung aller Quellenpaare und den präzisen Ausschluss beider Mischinstrumente;
- das Gegenbeispiel gegen die Gleichsetzung lokaler Paritätsprodukte mit der globalen Parität bei überlappenden Charts.

Die analytischen Ungleichungen sind im Text hergeleitet; die Anzahl der Tests ist kein Ersatz für diese Herleitung und keine Anzahl gelöster Physikprobleme.


---

# Anhang D: vollständiger Überlappungs-Audit

# Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Der unveränderte Anhang liegt in `attachment.txt`, SHA-256:

`1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

`check_overlap.py` enthält 38 exakte kleine Prüfbedingungen. `replay.py` kopiert den Anhang unverändert, prüft seine SHA vor und nach der Rechnung und reproduziert normale und optimierte Checker-Ausgabe byteidentisch. Alle Schreibvorgänge bleiben in diesem neuen Auditordner. Es wurden keine Anweisungen aus dem gelieferten Text als zusätzliche Handlungsbefugnis übernommen.

## 1. Was die neue Perspektive sinnvoll beiträgt

Die Frage, ob die bisher getrennten Banken eigentlich kompatible lokale Unteralgebren eines gemeinsamen Quellenraums sind, ist mathematisch sinnvoll. Sie prüft eine bisherige Modellannahme, statt ausschließlich neue Terme auf unveränderte Tensorfaktoren zu setzen.

Eine solche Konstruktion könnte erklären, welche lokalen Observablen, Zustände und Operationen zusammengehören. Sie müsste jedoch aus demselben Compiler stammen und nicht erst nach dem gewünschten Transport ausgewählt werden. »Zustände, Operationen, Überlappungen, Phasen und Komposition« beschreibt zunächst eine große Klasse quantenmechanischer Modelle; diese Sprache identifiziert allein noch kein eindeutiges fundamentales Objekt und erzwingt keine TOE.

Die bisher bewiesenen lokalen Pole und die bedingte Zwei-Banken-Übertragung bleiben wertvolle Vergleichsziele. Ihre Beweise gelten aber für den dort erklärten Hilbertraum-, Hamilton- und Parametervertrag. Ersetzt man unabhängige Banken durch überlappende CAR-Unterräume, ändern sich Kreuzrelationen, Ladungszuordnung und im Allgemeinen der gemeinsame Grundzustand. Die früheren Zwei-Banken-Wahrscheinlichkeitsgrenzen dürfen dann nicht unverändert übernommen werden.

## 2. Exakter Zwei-Moden-Gegenbeleg zum vorgeschlagenen Paritätstest

Seien c₁,c₂ zwei orthogonale CAR-Moden. Setze

`a=c₁`, `b=(c₁+c₂)/√2`.

Jeder Chart ist für sich ein gültiger Einmoden-CAR-Raum, aber

`{a,b†}=I/√2`.

Die beiden Charts sind also keine unabhängigen Fermionfaktoren. Definiere ihre lokalen Paritäten

`Π_A=I−2a†a`, `Π_B=I−2b†b`.

In der Besetzungsbasis `|00>,|10>,|01>,|11>` ist die wirkliche globale Parität

`Π_global=diag(1,−1,−1,1)`.

Das Produkt der lokalen Paritäten lautet dagegen

```
Π_A Π_B = [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0,-1, 0, 0],
           [0, 0, 0, 1]].
```

Es ist weder die globale Parität noch hermitesch, und sein Quadrat ist nicht die Identität. Auch `[Π_A,Π_B]≠0`.

Der vorgeschlagene Test `[U_AB,Π_AΠ_B]=0` charakterisiert deshalb bei solchen Überlappungen **keine globale Geradheit**. Das lässt sich noch direkter widerlegen: Der Hamiltonoperator

`H=a†a+b†b`

ist global gerade, kommutiert mit keiner der beiden lokalen Paritäten und auch nicht mit ihrem Produkt. Sein Cayley-Transform

`U=(I−iH)(I+iH)⁻¹`

ist eine exakt unitäre, global gerade Operation mit denselben drei Nichtkommutationen. Der im Anhang vorgeschlagene Kill-Test würde diese zulässige globale Operation fälschlich ausschließen.

Die richtige Reihenfolge ist daher: zuerst die gemeinsame CAR-Einbettung und ihre echte globale Graduierung bestimmen. Erst danach lässt sich entscheiden, welche lokalen Paritätskriterien anwendbar sind. Bei einer disjunkten orthogonalen Zerlegung gilt die gewohnte Produktformel; bei überlappenden Charts im Allgemeinen nicht.

## 3. Noch wichtiger: Ein Überlappungsmatrixelement ist kein Transport

Für dieselben zwei Moden seien

`|A>=a†|0>`, `|B>=b†|0>`.

Dann ist ihre Gram-Matrix

`S=[[1,1/√2],[1/√2,1]]`.

Wähle den vollkommen trivialen Hamiltonoperator `H₀=ωN`, mit `N=c₁†c₁+c₂†c₂`. Die Matrix der Hamilton-Matrixelemente in diesen beiden Chartvektoren ist

`K_ij=<i|H₀|j>=ω S_ij`.

K hat also eine nichtverschwindende Offdiagonale, obwohl auf dem gesamten Einteilchenraum nur dieselbe Phase `e^(−iωt)` entsteht. Das korrekte Eigenproblem ist `Kv=E Sv`, nicht `Kv=Ev`. Es liefert ausschließlich die entartete Energie ω. Die Wahrscheinlichkeit

`|<B|exp(−itH₀)|A>|²=1/2`

ist für jede Zeit gleich groß. Es hat keine Übertragung stattgefunden; die Hälfte war schon bei t=0 als statische Überlappung vorhanden.

Das ist unmittelbar für den bisherigen nativen TFPT-Pol relevant. Dieser besitzt im erklärten N=63-Vertrag eine einzelne Energie E_h auf einem 64-dimensionalen Polraum:

`P_h H P_h = E_h P_h`.

Sind A und B lediglich zwei Beschreibungen oder Sonden innerhalb desselben Polraums, gilt wiederum `K=E_h S`: ein gemeinsamer Phasenfaktor, keine durch H verursachte Ausbreitung zwischen den Marken. Diese Aussage braucht keine große Diagonalisierung. Sie folgt allein aus der bereits bewiesenen Entartung.

Ein passiver Chartwechsel verändert nur die Beschreibung. Ein aktiv implementierter Rotationsoperator kann Zustände verändern; dann müssen jedoch genau dieser Operator, seine physische Verfügbarkeit, Zeit- oder Ressourcenskala und sein Instrument aus der Quelle nachgewiesen werden. Das ist nicht durch den Namen »Intertwiner« erledigt.

Die mögliche globale Überlappungskonstruktion ist dadurch nicht ausgeschlossen. Sie müsste tatsächliche zusätzliche globale Dynamik beziehungsweise eine Bandaufspaltung aus der Quelle zeigen und die lokalen Polbeweise darin erneut absichern.

## 4. Chartwechsel, Verbindungen und Krümmung sind verschiedene Daten

Wenn mehrere Charts lediglich vollständige orthonormale Rahmen R_x desselben festen Vektorraums sind, lauten die Basiswechsel

`U_xy=R_x† R_y`.

Dann teleskopiert jedes Dreiecksprodukt:

`U_12 U_23 U_31=I`.

Das gilt auch bei nichtkommutierenden R_x; der Checker prüft ein konkretes solches Beispiel. Durch bloße lokale Basiswahl entsteht daher nicht automatisch ein physisch gekrümmtes Eichfeld. Auf einem Bündel beschreiben Übergangsfunktionen seine Verklebung; eine Verbindung enthält zusätzliche Paralleltransportdaten. Eine nichttriviale Bündeltopologie ist ebenfalls nicht dasselbe wie bereits gewählte lokale Krümmung.

Bei tatsächlich variierenden **echten Unterräumen** ist die Situation interessanter. Überlappungen `ι_x†ι_y` müssen dann nicht unitär sein. Drei Strahlen `(1,0)`, `(1,1)/√2`, `(1,i)/√2` besitzen das nichtreelle Schleifenprodukt `(1+i)/4`. Das liefert eine geometrische Phase, aber sein Betragsquadrat ist 1/8 und nicht eins. Eine solche Unterraumgeometrie kann Ansatzpunkt für eine geometrische Verbindung sein; sie ist kein automatisch ausgeführter normerhaltender Transport und keine schon gewonnene Eichfeldkinetik.

Zudem legt eine interne Eichverbindung alleine keine Raumzeitmetrik fest. Verschiedene Linkphasen können auf demselben Graphen bei denselben Operationskosten existieren. »Die U_xy ändern sich« bedeutet ohne weiteren Nachweis nicht bereits »die Raumzeitgeometrie ändert sich«.

## 5. Zeit: Ein Grundzustand bewegt sich unter seinem H nicht beobachtbar

Die im Anhang skizzierte Entwicklung `Ω -> exp(−itH)Ω` erzeugt bei einem Energieeigenzustand lediglich `exp(−itE₀)Ω`. Der Dichteoperator bleibt exakt gleich. Der Checker bestätigt das an einem kleinen Fockzustand.

Damit wird weder die Zeitordnung noch ein Zeitpfeil erzeugt. Nichtstationäre Zustände und mehrzeitige Korrelationsfunktionen können natürlich eine Dynamik anzeigen; eine gerichtete Record- oder Präparationsgeschichte braucht ihre eigenen Bedingungen. Auch eine relationale Zeit aus bedingten Zuständen wäre als Forschungsansatz möglich, verlangte aber eine explizite Uhr, ihren gemeinsamen Zustand mit dem System und eine Konditionierungsregel. Der bloße globale Eigenzustandsphasenfaktor reicht dafür nicht.

Die nun geprüfte endliche Clock kann eine aktive Operation auf inneren Marken darstellen, falls sie physisch gewährt ist; dass sie zur Quellsymmetrie gehört, macht sie nicht automatisch identisch mit der Hamiltonzeit.

## 6. Der binäre Index muss als Freiheitsgrad bewiesen werden

Die skalare Hilfsdublett-Reparatur braucht zwei unabhängige, gleichgeladene Komponenten, auf denen eine nichtentartete antisymmetrische Form wirkt. Eine Orientierung der Überlappungsgeometrie **könnte** so etwas liefern, tut es aber nicht allein durch das Vorhandensein zweier Bezeichnungen.

Die drei einfachen Verwechslungen sind:

- Zwei Namen oder ±-Vorzeichen für dieselbe Mode bilden nur eine eindimensionale, redundante Beschreibung. Der Rückzug der antisymmetrischen Zweiform auf diesen Raum ist null.
- Ist Rückwärts die Adjungierte der Vorwärtsoperation, haben f und f† entgegengesetzte U(1)-Ladungen. Das ist kein gleichgeladenes Hilfsdublett. Ihr bilinearer Kanal ist neutral, nicht von Ladung −2.
- Bedeutet Vorwärts/Rückwärts links-/rechtshändige Weylfelder, wurden zwei verschiedene Lorentzdarstellungen eingeführt. Das ist nicht die zusätzliche gleichartige Hilfskopie des bereits geprüften Tensorvertrags.

Eine geometrisch hergeleitete Zweifachheit könnte also eine gute Erklärung des Hilfsindex sein. Nötig wären zwei tatsächliche unabhängige Kanäle, ihre CAR-/Ladungsrelationen, die Spin-Lorentz-Wirkung und die nichtverschwindende Kopplung auf demselben Quellraum. Ein Orientierungsbit liefert weder automatisch Weylspin noch die Transformationsregel unter einer vollen Lorentzdrehung.

## 7. Operationsgeometrie benötigt mehr als Erreichbarkeit

Minimale Kosten erfüllen unter geeigneter Komposition eine Dreiecksungleichung. Ohne reversible Operationen mit symmetrischen Kosten ist die resultierende Funktion jedoch nur eine gerichtete Distanz; der Checker liefert den gerichteten Dreierzyklus mit `d(A,B)=1`, `d(B,A)=2`. Unerreichbarkeit ergibt unendliche Distanzen. Kostenfreie Chartwechsel können verschiedene Beschreibungen auf Distanz null setzen; dann muss zunächst nach physischer Äquivalenz quotiert werden.

Wachstum `V(R)~R³` ist ein Nachweis einer dreidimensionalen **Wachstumsdimension im gewählten Kostenmaß**, nicht automatisch einer glatten dreidimensionalen Mannigfaltigkeit, einer 3+1D-Lorentzmetrik oder einer universellen Lichtgeschwindigkeit. Schon ein kubisches Gitter mit Laplace-Hamiltonoperator hat dieses Volumenwachstum, aber bei kleinen Impulsen

`E(k)=Σ_j(2−2cos k_j) ~ |k|²`,

nicht eine lineare relativistische Dispersion. Der eindimensionale Taylor-Koeffizient dieser separierbaren Gegenkonstruktion wird exakt geprüft.

Eine lokale Spektrallücke ist ebenso noch keine relativistische Teilchenmasse. Dazu braucht es die gemeinsame Energie-/Impulsdeutung, den entsprechenden Dispersionszweig und den Ladungs-/Referenzvertrag. »Kopieren« sollte bei Teilchenpropagation nur bildlich verwendet werden: kohärenter Transfer erzeugt nicht zwei unabhängige Kopien eines unbekannten Quantenzustands.

## 8. Gravitation bleibt eine dynamische Verpflichtung

Die linearen Fluktuationen einer aus der Quelle bestimmten globalen Geometrie zu prüfen, ist ein sinnvoller Forschungsauftrag. Eine transversale spurfreie Tensorzerlegung allein garantiert aber weder einen masselosen physikalischen Spin-2-Pol noch positive Norm, genau zwei Helizitäten oder universelle Kopplung. Selbst ein gesunder linearer Spin-2-Sektor ersetzt nicht den Nachweis seiner nichtlinearen Eich-/Zwangsstruktur und konsistenten Materiekopplung.

Das vorgeschlagene wechselseitige Schema Materie -> bevorzugte Überlappungen -> Geometrie ist daher ein mögliches Wirkungsprinzip, noch keine aus dem vorhandenen nativen H gewonnene Gleichung.

## 9. P versus NP: eine konkrete Korrektur

Der Anhang sagt, P≠NP würde einen intrinsisch exponentiellen Suchaufwand bedeuten. Das ist falsch. P≠NP würde ausschließen, dass **jedes** NP-Entscheidungsproblem deterministisch in Polynomialzeit gelöst werden kann. Es folgt daraus keine exponentielle untere Schranke: Eine hypothetische Laufzeit wie `2^(√n)` ist superpolynomiell und zugleich subexponentiell. Stärkere Exponentialzeitaussagen benötigen zusätzliche Sätze beziehungsweise Hypothesen.

NP bezieht sich zudem auf polynomial lange, polynomial prüfbare Zertifikate in der Länge einer wohldefinierten Eingabekodierung. Beliebige Erreichbarkeit in einem knapp beschriebenen Graphen mit möglicherweise exponentiell langen Wegen ist nicht allein deshalb ein NP-Problem. Eine geometrische Umformulierung muss Eingabelänge, Zertifikatlänge, erlaubte Operationen und deren Kosten erhalten. Eine Pfadmetapher löst diese Verpflichtungen nicht.

## 10. Ein korrigierter, wirklich entscheidbarer Anschluss-Test

Ein sinnvoller nächster Versuch besteht nicht nur aus einem unbeschrifteten `P U_AB P`. Er sollte zusammen liefern:

1. **Globale Quelle und Einbettungen:** konkrete primitive Algebra und zwei CAR-/Tensor-erhaltende Abbildungen; alle Kreuzrelationen und die tatsächliche globale Graduierung.
2. **Gemeinsamer Zustand:** derselbe globale H und Zustand; Nachweis, welche bisherigen lokalen Pole und Lücken darin noch gelten. Kein stiller Rückgriff auf den Produktgrundzustand unabhängiger Banken.
3. **Physische Operation:** aus einem erklärten Quellenwort erzeugter aktiver Operator oder Generator, mit Zeit- beziehungsweise Ressourcenskala. Passive Chartwechsel bleiben getrennt.
4. **Gram-bereinigte Dynamik:** `S_ij=<h_i|h_j>` und `K_ij=<h_i|H|h_j>` berechnen; das generalisierte Eigenproblem beziehungsweise eine orthonormalisierte Darstellung verwenden. Prüfen, ob mehr als `K=E_h S` entsteht.
5. **Operativer Transfer:** dieselbe Anfangspräparation und Zielmessung; zeitabhängige Änderung gegenüber der statischen Überlappung und Fehlerkontrolle gegenüber dem übrigen Zustandsraum. Erst dann mit dem bekannten bedingten Zwei-Banken-Transfer vergleichen.

Das nimmt die mögliche gemeinsame Herkunft ernst, korrigiert aber die falschen Automatismen. Der stärkste sofortige Erkenntnisgewinn dieses Audits ist negativ und präzise: **Allein durch Überlappung oder Umbenennung eines entarteten nativen Polraums entsteht keine Transportdynamik.** Ob der Compiler darüber hinaus genau die passende globale Dynamik besitzt, ist die konkrete offene Frage.


---

# Anhang E: arithmetischer Schleifenvorschlag

# Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

15. September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes
`59dc0059-8914-48ca-953d-85933f66e00b`, kein neuer RH-Beweis und kein neuer
arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale
Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## Urteil

**Ein globaler Wegraum ist eine sinnvolle Suchklasse; ein Eulerprodukt über
primitive Wege ist noch nicht das Eulerprodukt der Riemannschen Zetafunktion.**
Die im Text vorgeschlagene Xi-Determinante bleibt ein hinreichendes Ziel unter
expliziten Operatorannahmen. Das Umbenennen ihres noch fehlenden Operators in
„Generator der primitiven Schleifen“ konstruiert ihn nicht.

## 1. Was die endliche Bank tatsächlich ausschließt

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator
mit 64 Fermion- und 60 Bosonmoden, Δ>0. Der Hilbertraum ist wegen der Bosonen
**nicht endlichdimensional**. Endlich ist die Zahl der Moden. Mit
`C=960g²/Δ` folgt aus quadratischem Ergänzen

\[
H\ge\frac\Delta2N_b-C,
\qquad
N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60}.
\]

Dies widerspricht einem vollständigen energieerhaltenden Spektrum
`E_* log n + E_off`, E_*>0, weil dessen Zählfunktion exponentiell wächst.
Es ist kein Ausschluss beliebiger arithmetischer Untersektoren oder eines
anderen Operators mit nichtlinearer Energiezuordnung.

Ein großer Wegraum kann eine andere Zählfunktion besitzen. Die Gleichsetzung
„mehr Wege = mehr orthogonale Zustände unter derselben Energie“ muss aber
bewiesen werden. Verschiedene Wörter können denselben Operator oder Zustand
darstellen; ein Quantenüberlagerungsraum ist nicht ohne Weiteres der freie
Wortraum. Bei unendlich vielen identischen Zellen kann stattdessen die globale
Wärmespur divergieren. Der Text entfernt diese Fragen nicht durch Vergrößerung.

## 2. Der kleinste Gegencheck zur Primzahl-Automatik

Nehmen wir einen gerichteten Knoten mit zwei erlaubten Schleifen a und b.
Neben a und b ist auch ab ein primitiver periodischer Weg: Es ist keine Potenz
eines kürzeren Wortes. Ebenso entstehen weitere gemischte primitive Wörter.
Setzen wir nachträglich L(a)=log 2, L(b)=log 3, so hat ab die Länge log 6.
Die 6 ist keine Primzahl. „Primitiver Weg“ bedeutet nicht „arithmetische
Primzahl“.

Schon formal unterscheiden sich die zugehörigen erzeugenden Funktionen:

\[
Z_{\rm Wege}(x,y)=\frac1{1-x-y},\qquad
Z_{\rm zwei\ Primarten}(x,y)=\frac1{(1-x)(1-y)}.
\]

Der Koeffizient von xy ist links 2 und rechts 1. Links werden die beiden
Wörter ab und ba gezählt; rechts eine kommutative Besetzung. Im periodischen
Eulerprodukt bilden ab und ba eine zyklische Klasse, aber diese ist ein
**neuer primitiver Faktor**. Die Abweichung verschwindet damit nicht.

Eine kommutative freie Halbgruppe über vorgegebenen Primarten reproduziert
eindeutige Faktorzerlegung. Sie leitet aber weder die natürliche arithmetische
Markierung noch die logarithmischen Längen oder die passende Spur her.
Eine gekoppeltere Geometrie müsste gemischte Bahnen mit den richtigen
Amplituden, Relationen oder nachgewiesenen Auslöschungen behandeln. Dies ist
kein allgemeiner Ausschluss von Schleifenmodellen mit Interferenz.

Der Unterschied ist in den Originalarbeiten sichtbar: Kuipers, Hummel und
Richter konstruieren Quantengraphen mit dem passenden oszillierenden Anteil
der Nullstellendichte, weisen aber auf den anderen glatten Anteil und damit
das andere Spektrum hin. Das ist ein nützlicher Vorläufer, kein RH-Operator.
[Originalarbeit, Phys. Rev. Lett. 112, 070406](https://arxiv.org/abs/1307.6055)

Graphische Eulerprodukte besitzen ihre eigene Theorie. Auch eine aus einer
Graph-Zetafunktion bestimmbare Größe ist nicht automatisch effizient auslesbar.
Storm trennt in seiner Arbeit ausdrücklich berechenbare Zeta-Darstellung und
teure Auswertung bestimmter Graphinformationen.
[Originalarbeit zu Edge-Zetafunktionen](https://arxiv.org/abs/0708.1923)

## 3. Die richtige RH-Zielbedingung

Sei A strikt positiv und selbstadjungiert, mit kompakter Inverser und
`A^{-2}` von Spurklasse. Dann ist der Fredholm-Ausdruck

\[
D(z)=\det(I-z^2A^{-2})
\]

ganz, und seine Nullstellen liegen bei den reellen Zahlen ±λ_j(A), mit ihren
Multiplizitäten. Würde unabhängig und auf ganz C bewiesen

\[
\Xi(z)/\Xi(0)=D(z),\qquad \Xi(z)=\xi(1/2+iz),
\]

so folgte RH. Das ist die korrekte bedingte Implikation. Nicht ausreichend
sind ein paar passende Eigenwerte, die imaginären Teile bereits eingesetzter
Nullstellen, ein Eulerprodukt nur für Re(s)>1 oder eine Formaldeterminante ohne
Domäne, Spurklasse und vollständige archimedische Faktoren.

Der vorgelegte Text liefert A nicht, bestimmt keine Domäne und leitet weder
die vollständige Spurformel noch die ganze Funktionsidentität her. Die
allgemeine Selbstadjungiertheit eines anderen Operators hilft dabei nicht.

## 4. Vorarbeiten und aktuelle Grenze der Quellenprüfung

Der installierte Leitfaden `rh-graph-research` und die projektspezifische
Korpussuche wurden angewandt. Die aktuelle Konsistenzprüfung und der
anschließende Wiederaufbauversuch brachen mit

`SOURCE_UNAVAILABLE: /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`

ab. Die gesonderte Paper-Abfrage meldete `PAPER_SOURCE_OR_REVIEW_DRIFT`.
Keine dieser Prüfungen wurde durch Ersetzen von Pins grün gemacht. Der
Forschungsindex darf hier **nicht als global aktuell geprüft** bezeichnet
werden. Vorhandene Suchresultate dienten lediglich zum Auffinden real
verfügbarer Originaldateien; die aktuelle Queue ist keine Beweisquelle.

Gezielt gelesen wurden die relevanten Abschnitte von
`rh/catalog/analysis/geometry_audit.md` (Quantengraphen) und
`rh/catalog/analysis/event_log_function.md` (arithmetische Ereignisse), sowie
die vollständige maßgebliche Zählungs-/Determinantenpassage aus v1.6.5.
Die Dateien werden für diese Revision eingefroren. Ihre historischen
Korpus-Abwesenheitsangaben werden nicht als aktueller Vollständigkeitsbeweis
übernommen.

Im bestehenden Index berühren `r618 / STRUCTURAL_MISMATCH` die Verwechslung
RH-neutraler E8-Daten mit einer Xi-Identität und
`ledger:E8.COXETER.EULER.COMPLETION.01 / NO_BRIDGE` die fehlende globale
Vervollständigung. Solche Treffer allein widerlegen kein neues Objekt; die
hier tragende Prüfung ist der explizite Unterschied zwischen gemischten
primitiven Wegen und arithmetischen Primarten. Es wird kein neuer globaler
RH-Beweisstatus registriert oder freigegeben.

## 5. Tragfähiger Anschluss, ohne acht Versprechen an ein unbekanntes Objekt

Der nächste arithmetische Test wäre erst nach Definition einer tatsächlichen
Quell-Wegstruktur sinnvoll: primitive Bahnen, ihre Längen, Amplituden und die
Spur gemeinsam bestimmen, ohne Primlisten oder Nullstellen einzusetzen.
Ein positiver Kontrolltest muss insbesondere gemischte Zyklen erklären und
den archimedischen Anteil auf demselben Träger liefern. Gelingt nur ein
generisches Graph-Eulerprodukt, ist das ein Graphresultat und bleibt von RH
getrennt.

Faktorisierung und P versus NP werden dadurch nicht gelöst. Außerdem ist
„P≠NP bedeutet notwendigerweise exponentielle Suchkosten“ zu stark: Aus einer
fehlenden polynomialen Zeitgrenze folgt nicht allein eine exponentielle
untere Schranke. Für Hylæan enthält der Text ein mögliches Operationsbild,
aber keinen neu überprüften Lern- oder Gedächtnisnachweis.


---

# Historischer vollständiger Herleitungsstand v1.6.5 einschließlich v1.6.4

Der folgende Text wird unverändert bewahrt. Neue Gesamtstatusaussagen und Reichweitenkorrekturen stehen in der vorangestellten Revision v1.6.6. Historische Arbeitsaufträge oder Verfügbarkeitsannahmen werden dadurch nicht erneut zu aktuellen Beweisen erklärt.

# TFPT / Universalraum: kontrollierter Zwei-Banken-Transfer

Forschungsfortsetzung und Quellenaudit · 15. September 2026 · v1.6.5

## Ergebnis und Geltungsbereich

Eine konkrete bisher offene Rechnung lässt sich schließen: **Im ausdrücklich
um einen Rotor-Link erweiterten Modell zweier nativer Fermion-Boson-Banken
ist der Transfer der isolierten Lochanregung mit einer Fehlergrenze gegenüber
dem vollständigen physikalischen Zustandsraum kontrollierbar.** Dafür ist
keine Diagonalisierung dieses enorm großen Raums nötig. Die vorhandene
Casimiridentität, Ladungserhaltung und eine Spektrallücke reichen aus.

Am unten vollständig angegebenen, bewusst sehr schwachen Kopplungspunkt gilt:

| Aussage | Strenge Schranke | Status |
|---|---:|---|
| Zielwahrscheinlichkeit aus dem normierten Zustand der isolierten Lochlinie | > 99,2677105 % | Analytisch mit rationalen Zertifikaten, im zusätzlichen Linkmodell |
| Zielwahrscheinlichkeit aus der normierten ursprünglichen Entnahme \(f_r\Omega/\sqrt\nu\), **ohne anfänglichen Energiefilter** | > 89,7260353 % | Gleicher vollständiger Hamiltonoperator, Ziel ist die niedrige Lochlinie rechts |
| Verlassen des ungestörten niedrigen Bandes, aus einem Zustand dieses Bandes | < \(1{,}8\cdot10^{-11}\) zu jeder Zeit | Voller erlaubter Ladungssektor, keine Bosonen- oder Flussabschneidung |
| Herkunft des Links, der Bankzerlegung und der Präparation | nicht hergeleitet | Offen |
| Relativistische Felder, gemeinsamer 3+1D-Ursprung, T1–T8 | nicht konstruiert | Offen |

Die Zahlen sind **untere beziehungsweise obere Einschließungen**, keine
berechneten Zentralwerte. Sie beschreiben kein durchgeführtes physisches
Experiment. „Vollständig“ bezieht sich hier auf die Fehlerkontrolle im
deklarierten Zwei-Banken-Ladungssektor, nicht auf die TOE.

Die gelieferten Arbeiten wurden mit 1.149 beziehungsweise 753 Prüfbedingungen
normal und optimiert reproduziert, jeweils byteidentisch mit den mitgelieferten
Ergebnissen. Unsere neue Transferrechnung hat 4.516 Prüfbedingungen; eine
gesonderte Reichweitenprüfung der währenddessen geänderten Symmetrieaussagen
hat zehn. Die zwei zuletzt eingegangenen Anlagen wurden mit 62 weiteren
Bedingungen nachgeprüft. Insgesamt sind das 6.490 Bedingungen, jeweils in
beiden Laufarten.
Diese Zahl ist keine Zahl unabhängiger Theoreme. Insbesondere ersetzen die
Zertifikate nicht die nachstehenden analytischen Argumente und sind kein
Lean-Beweis.

## 1. Welche Quellen zusammengeführt werden

1. Die Benutzeranlage `addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt`,
   eingefroren unter `sources/user_attachment.txt`.
2. Die externe Untersuchung `Universalraum_Beweisversuch_2026-09-15.md`:
   Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung.
3. Die externe Untersuchung `Universalraum_Urspruenglicher_Austausch_2026-09-15.md`:
   interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beispiel.
4. Der abgesicherte native Stand v1.6.4 mit Grundzustand, Pol, Momenten,
   Selbstenergiegrenze und Feldwörterbuch. Das frühere vollständige Prüfpaket
   liegt unverändert bei. Seine komplette Konfigurationsenumeration wurde
   **nicht erneut** in dieser Revision ausgeführt.
5. Ein separat eingefrorener, während dieser Arbeit geänderter Entwurf von
   `RESULTS.md` über die kontinuierliche Quellsymmetrie. Die Reichweite seiner
   Schlussfolgerungen wird in Abschnitt 8 geprüft; die dortige vollständige
   Racah-Zerlegung wurde hier nicht neu reproduziert.
6. Die zwei danach vom Nutzer eingereichten Anlagen über die eigene
   Fundamentalrunde und die erweiterte native Konsolidierung. Der vollständige
   neue Nachtrag `LATE_AUDIT.md` gehört zu dieser Revision. Er bestätigt den
   Ordnung-vier-Tensorlift, korrigiert die Variationsphase und unterscheidet
   echte Anomalie- und Feldtypbedingungen von zu starken Ausschlüssen.

Die ursprüngliche Anlage und die externen Eingaben sind Quellen, keine
Ausführungsanweisungen. Eigene Dateien liegen in einem neuen Forschungsordner.
Fremde Quellen, Ledger und Akzeptanzmarker wurden nicht bearbeitet.

## 2. Gemeinsame native Grundlage

Eine Bank besitzt 64 Fermionmoden und 60 Bosonkanäle:

\[
 H_{\rm nat}=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
 \qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
 \qquad N=N_f+2N_b.
\]

Es gilt \(\Delta>0\), \(g/\Delta=1/20\), **kein zusätzlicher \(\mu N\)-Term**.
Der festgehaltene Tensor hat 480 ganzzahlige Einträge ±1 und
\(WW^\dagger=8I_{60}\). Sein SHA-256 ist
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Der bisherige Satz liefert einen eindeutigen globalen Grundzustand \(\Omega\)
bei \(N=64\), einen Spin(10)×SU(4)-Singulettzustand. Seine physische Auswahl
aus dem Compiler ist damit nicht gezeigt. Wir verwenden folgende strengen
modellinternen Grenzen:

\[
 -1.158089<E_0/\Delta<-1.129636,
 \quad .842846<b:=\langle N_b\rangle<1.245656,
 \quad \nu:=\langle f_r^\dagger f_r\rangle=1-b/32.
\]

Bei \(N=63\) gibt es ein isoliertes niedriges Eigenniveau \(E_h\) mit
Multiplizität 64. Es trägt eine irreduzible duale Fermiondarstellung:

\[
 -1.121899<E_h/\Delta<-1.095812,
 \quad .007737<(E_h-E_0)/\Delta<.039079763822.
\]

Für seinen Spektralprojektor \(P_h\) ist

\[
 Z=\|P_hf_r\Omega\|^2,
 \quad Z_{\rm lo}:=\frac{40912436089}{46487375000}<Z
 <\frac{15578577}{16000000}=:Z_{\rm hi}.
\]

Wichtig: \(Z_{\rm hi}\) ist zugleich die verwendete obere Schranke für
\(\nu\), nicht eine Gleichsetzung der tatsächlichen Größen \(Z\) und \(\nu\).
Das niedrige Gewicht ist >88,0076 % des gesamten normierten CAR-Spektralmaßes.
Innerhalb der **Entnahmeantwort** ist sein Anteil \(w=Z/\nu>90,38836\,\%\).

Alle weiteren Eigenwerte von \(H_{63}\) sind >\(-.75\Delta\);
alle angeregten Eigenwerte von \(H_{64}\) ebenfalls. Die Entnahme-Restantwort
beginnt relativ zu \(E_0\) oberhalb \(.379636\Delta\), die Additionsantwort
oberhalb \(.329636\Delta\).

Diese Schranken gehören zu demselben Hamiltonoperator und demselben Zustand.
Die ursprüngliche Größe \(\chi_r^\dagger\Omega\) bei Ladung 67 wird nicht mit
\(f_r\Omega\) bei Ladung 63 identifiziert.

## 3. Prüfung der gelieferten neuen Resultate

### 3.1 Die interne Paarumwandlung ist wirklich nativ

Bei Gesamtladung 2 zerfällt der 2.076-dimensionale Raum in 60 helle
Zweizustandsblöcke und 1.956 dunkle Zustände. In jedem hellen Block gilt

\[
 H_A=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix},
 \qquad p_{\max}=\frac{32g^2}{\Delta^2+32g^2}=\frac2{27}.
\]

Das wurde aus dem unveränderten Tensor reproduziert. Es ist die Umwandlung
zweier Fermionen in einen Bosonkanal, **kein abgeleiteter Ortswechsel einer
Ladung eins**, und der Ladung-2-Zustand ist nicht der native Grundzustand.
Die acht internen Pfade pro Kanal müssen kohärent bleiben; getrennte
Pfadaufzeichnungen verändern den Gramoperator und damit die Dynamik.

Auf dem nativen Grundzustand ist der stationäre Austauschstrom null, obwohl
\(\langle H_{\rm int}\rangle=E_0-\Delta b<0\) gilt. Eine vollständige
\(N_b\)-Dephasierung erhöht die Energie um
\(\Delta b-E_0\in(1.972482,2.403745)\Delta\). Statische Kohärenz ist nicht
dasselbe wie ein gerichteter Strom.

### 3.2 Der neue Link ist konsistent, aber zusätzlich

Die externe Arbeit definiert ein Rotorpaar \(E,U\) auf \(\ell^2(\mathbb Z)\):
\(E|e\rangle=e|e\rangle\), \(U|e\rangle=|e+1\rangle\), \([E,U]=U\).
Mit zwei **gradiert** zusammengesetzten nativen Banken lautet der Zusatz

\[
 B=\sum_{r=1}^{64}f_{y,r}^\dagger U f_{x,r},
 \qquad V=\tau B+\bar\tau B^\dagger,
 \qquad H=H_x+H_y+\frac\kappa2E^2+V.
\]

Dieser Operator erhält die Gesamtladung und die passend definierten lokalen
Gaussgrößen. Er ist beschränkt mit \(\|V\|\le64|\tau|\). Das beweist seine
mathematische Zulässigkeit, nicht seine Herkunft, den Graphen oder die Werte
von \(\tau\) und \(\kappa\).

Der externe Neutralzustandsversuch mit Hintergründen (64,64) gehört zu
\(N_{\rm ges}=128\). Dort sind die erzeugten Loch-Additions-Paare eine
andere Antwort als eine bereits vorhandene einzelne Lochanregung. Die
berechnete Gewichtsnorm \(64\nu(1-\nu)=2b-b^2/16\), das Faltungsmaß und
die Schwelle \(>.337373\Delta+\kappa/2\) sind damit vereinbar. Sie werden
nicht als Einloch-Transferwahrscheinlichkeit ausgegeben.

### 3.3 Das ältere 99,8718-%-Beispiel ist ein anderer Träger

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs
Zustände sind der vollständige Gausssektor eines **Vierfermion-Modells** mit
einem Link. Der zertifizierte Wert bei \(t=19\) betrifft diesen Parent und
diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation
noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist
davon unabhängig und benutzt die tatsächlich nativen \(E_0,E_h,Z\)-Schranken.

## 4. Neuer Satz: vollständige Kontrolle des Einloch-Transfers

### 4.1 Den richtigen physikalischen Sektor festlegen

Für genau ein Loch ist eine Ladungsreferenz notwendig. Wir deklarieren
Hintergründe \((q_x,q_y)=(63,64)\) und fordern

\[
 G_x=N_x-63+E=0,\qquad G_y=N_y-64-E=0.
\]

Dann ist \(N_x+N_y=127\) und **\(E=63-N_x\) exakt festgelegt**. Auf diesem
Ein-Kanten-Baum verbleibt kein unabhängiger unbeschränkter Flussindex.
\(0\le N_x,N_y\le127\) beschränkt auch die Bosonenzahlen. Der gesamte
physikalische Sektor ist endlichdimensional; keine Flussabschneidung und
kein willkürlicher Bosonen-Cutoff werden eingeführt.

Definiere \(h_r=P_hf_r\Omega/\sqrt Z\). Die 64 Vektoren sind orthonormal.
Das niedrige Band \(P\) wird von

\[
 |L,r\rangle=h_{x,r}\otimes\Omega_y\otimes|0\rangle,
 \qquad |R,r\rangle=\Omega_x\otimes h_{y,r}\otimes|-1\rangle
\]

aufgespannt und besitzt Dimension 128. Für den ungekoppelten Operator
\(H_0=H_x+H_y+\kappa E^2/2\) sind die Energien \(e_*=E_h+E_0\) und
\(e_*+\kappa/2\).

Nach einheitlicher Wahl der relativen Fermionphase wirkt die exakte
Kompression \(PHP\), abzüglich \(e_*\), wie

\[
 \begin{pmatrix}0&-\bar\tau Z\\-\tau Z&\kappa/2\end{pmatrix}
 \otimes I_{64}.
\]

Das Vorzeichen ist für die Population unerheblich. Das \(I_{64}\) zeigt,
dass die Rechnung für jeden normierten internen Überlagerungszustand gilt.
Die projizierten Fermionoperatoren sind Hubbard-Übergänge und keine
vollständige CAR-Algebra auf diesem 128-dimensionalen Band.

### 4.2 Die Lücke zum gesamten übrigen Raum

Die native, nicht nur perturbative Casimiridentität lautet

\[
 \sum_AP_A^\dagger P_A=\tfrac12(15N_f-C_{\rm Spin(10)}-C_{\rm SU(4)}).
\]

In einem Block \(N=n,N_b=b\) ist die rechte Seite höchstens
\(\tfrac{15}2(n-2b-\eta)\) mit \(\eta=n\bmod2\). Bei ungerader
Fermionzahl kommt der Casimir-Mindestwert 15 hinzu. Die Norm des
Boson-Erzeugungszeilenoperators auf dem Zielblock ist \(\sqrt{b+1}\).
Damit liefert die Blocknorm-Abschätzung eine skalare Jacobi-Untergrenze
mit Diagonale \(b\) und quadrierten Nebendiagonalen

\[
 a_b^2=\frac{15(b+1)(n-2b-\eta)}{800}
\]

in Einheiten \(\Delta=1\). Man nimmt negative Nebendiagonalen; die
Quadratformabschätzung benutzt die Normen der vollen Bosonzahlkomponenten
eines beliebigen Zustands, nicht einzelne Testvektoren.

Für **jedes \(n=65,\ldots,127\)** wurden sämtliche LDL-Pivots der
Vergleichsmatrix oberhalb \(-4/5\) exakt positiv nachgewiesen. Der erste
Bosonindex ist \(\lceil(n-64)/2\rceil\), der letzte \(\lfloor n/2\rfloor\).
Somit gilt \(H_n>-.8\Delta\) in allen 63 hohen Ladungssektoren.

Für alle \(n\le62\) liefert die Minimierung der Cauchy-Schwarz-Schranke

\[
 H_n/\Delta\ge-\frac{n-\eta}{4}(\sqrt{23/20}-1)>-1.121899.
\]

Jede andere Ladungsverteilung als (63,64) oder (64,63) enthält eine Bank
mit \(n\le62\) und eine mit \(n\ge65\). Ihre Gesamtenergie liegt also
oberhalb \(-1.921899\Delta\). Die elektrische Energie ist nichtnegativ.
Das obere Bandende von \(P\) ist kleiner als
\(-2.225448\Delta+\kappa/2\).

Für die beiden zentralen Ladungsverteilungen wurden außerdem die
Vergleichsmatrizen ab \(b=1\) bei \(n=63,64\) oberhalb \(-3/4\) erneut
rational geprüft. Durch Minmax mit Kodimension 64 beziehungsweise eins
ergeben sich die bekannten angeregten Energieböden; es wird nicht behauptet,
dass der exakte Spektralprojektor mit dem Null-Bosonenprojektor identisch ist.

Zusammen ergibt sich eine Lücke zwischen \(P\) und \(Q=I-P\) von mindestens

\[
 \boxed{\delta=.303549\Delta-\kappa/2>0.}
\]

Die anderen beiden Vergleichslücken sind
\(.345812\Delta-\kappa/2\) und \(.379636\Delta-\kappa/2\), also größer.
Diese Schranke umfasst **alle** Ladungsaufteilungen, Bosonzustände und
internen Moden des deklarierten physikalischen Sektors.

### 4.3 Gleichmäßige Auslaufkontrolle und endliche Transferzeit

Setze \(v=64|\tau|\) und fordere \(2v<\delta\). Sei \(a\) das obere
Eigenwertende von \(H_0|_P\). Minmax liefert ein Spektralband \(P'\) von
\(H\) derselben Dimension 128, dessen oberer Rand ≤\(a+v\) ist.
Die Kompression \(QHQ\) liegt ≥\(a+\delta-v\).

Mit \(Y=QP'\), als Abbildung aus \(\operatorname{Ran}P'\), gilt die
Sylvestergleichung

\[
 (QHQ)Y-Y(H|_{P'})=-QVP\,PP'.
\]

Die beiden Spektren sind geordnet und mindestens \(\delta-2v\) getrennt.
Die Lösung über das konvergente Exponentialintegral liefert
\(\|Y\|\le v/(\delta-2v)\): nach einem gemeinsamen Skalarshift ist der
Integrand durch \(v e^{-s(\delta-2v)}\) beschränkt. Wegen gleicher endlicher
Ränge gilt dieselbe Schranke für \(\|P'-P\|\).

Da \(P'\) mit \(H\) kommutiert, folgt zu **jeder** Zeit

\[
 \boxed{\|Qe^{-itH}P\|\le L:=\frac{2v}{\delta-2v}.}
\]

Aus der projizierten Schrödingergleichung und Duhamel folgt weiter

\[
 \|Pe^{-itH}\psi-e^{-itPHP}\psi\|
 \le |t|vL=:\eta(t),\qquad \psi\in P,\ \|\psi\|=1.
\]

Für den Zielprojektor \(P_R\subset P\) weichen die Wahrscheinlichkeiten
damit höchstens um \(2\eta(t)\) ab. Dies ist eine nichtperturbative
Fehlergrenze für die volle Entwicklung; nur der ausgewählte Kopplungsbereich
ist klein. Es handelt sich nicht um das Weglassen eines unbekannten
höheren Störungsterms.

### 4.4 Ein vollständig numerisch spezifizierter, rational zertifizierter Punkt

Mit \(\hbar=1\) wähle

\[
 \tau/\Delta=10^{-8},\quad \kappa/\Delta=10^{-10},
 \quad T:=t\Delta=169500000.
\]

Diese Zahlen sind ein konservativer Existenzpunkt, **keine aus TFPT
abgeleiteten Konstanten und keine Behauptung schneller oder optimaler
Übertragung**. Die physikalische Sekundenskala ist nicht bestimmt.

Die genaue komprimierte Rabi-Wahrscheinlichkeit ist

\[
 p_P(t)=\frac{|\tau|^2Z^2}{|\tau|^2Z^2+(\kappa/4)^2}
 \sin^2\!\left(t\sqrt{|\tau|^2Z^2+(\kappa/4)^2}\right).
\]

Für **jedes** zulässige unbekannte \(Z\) liegt der Winkel weniger als
0,08 von \(\pi/2\) entfernt. Das folgt aus \(Z_{\rm lo},Z_{\rm hi}\),
\(\sqrt{x^2+y^2}\le x+y^2/(2x)\) und rationalen Pi-Grenzen. Letztere
wurden zusätzlich mit der Machin-Identität und endlichen alternierenden
Arctan-Reihen eingeschlossen; Fließkomma-Pi ist keine Beweisvoraussetzung.

Mit \(\sin^2(\pi/2+u)\ge1-u^2\) folgt

\[
 p_P(T)>\left(1-\frac{\kappa^2}{16\tau^2Z_{\rm lo}^2}\right)
 (1-.08^2)>.993591982278.
\]

Die vollständigen Fehlergrenzen sind

\[
 L=\frac{25600}{6070954399}<4.216800\cdot10^{-6},
 \quad L^2<1.8\cdot10^{-11},
 \quad\eta(T)=\frac{2777088}{6070954399}<.000457438455.
\]

Also

\[
 \boxed{p_{\rm voll}(T)>p_P^{\rm lo}-2\eta(T)
 =\frac{25218291754002904578202303151726961}
 {25404324948782158166703488466197500}>.992677105368.}
\]

Die unbekannten \(E_0,E_h\) treten nur als gemeinsame Phase auf und müssen
für diese Schranke nicht genau ausgerechnet werden. Eine arbiträr hohe
Treue ist innerhalb des zusätzlichen Modells prinzipiell erreichbar: bei
bekanntem \(Z\), \(\kappa/|\tau|\to0\), \(|\tau|/\Delta\to0\) und
\(t\sim\pi/(2|\tau|Z)\) verschwinden sowohl Detuning als auch der Fehler
\(tv^2/\delta\). Das ist eine bedingte Grenzaussage mit wachsender Laufzeit,
kein ausführbares natives Optimierungsverfahren.

### 4.5 Dieselbe ursprüngliche Fermionantwort ohne anfänglichen Filter

Für
\(\psi_f=(f_{x,r}\Omega_x/\sqrt\nu)\otimes\Omega_y\otimes|0\rangle\)
gilt

\[
 \psi_f=\sqrt w\,|L,r\rangle+\sqrt{1-w}\,q,
 \quad q\in Q,\quad w=Z/\nu\ge Z_{\rm lo}/Z_{\rm hi}.
\]

Die Auslaufnorm in umgekehrter Richtung erfüllt ebenfalls
\(\|Pe^{-itH}Q\|\le L\), indem man die obige Schranke adjungiert und
die Zeit umkehrt. Der unerwünschte Anteil kann also nicht beliebig stark
destruktiv in das niedrige Zielband einstreuen. Mit der Dreiecksungleichung,
\(2\sqrt{w(1-w)}\le1\) und der gesondert geprüften Positivität vor dem
Quadrieren folgt

\[
 \boxed{\|P_Re^{-itH}\psi_f\|^2
 \ge w\,p_{\rm voll}^{\rm lo}-L
 >.897260353455>.897.}
\]

Damit ist **kein vorbereitender Projektor auf die isolierte Linie** nötig,
um eine starke Übertragungsaussage über die ursprüngliche Entnahmeantwort zu
erhalten. Noch benötigt werden die deklarierte geladene Präparation und der
zusätzliche Link. Die Aussage betrifft das niedrige Zielband; sie behauptet
nicht, dass die vollständige hochenergetische Restantwort ebenfalls formtreu
übertragen wird. Für diesen ungefilterten Anfangszustand gilt die extrem
kleine Auslaufwahrscheinlichkeit aus 4.3 nicht: Er startet bereits teilweise
außerhalb von \(P\).

## 5. Warum die Herkunftslücke nicht durch längeres Rechnen verschwindet

Sei \(\Pi_x=(-1)^{N_{f,x}}\) die lokale Fermionparität. Die bisher angegebenen
bankinternen Paarumwandlungen, Zahloperationen, zahlenerhaltenden
Symmetrielifts sowie reine Bosonverbindungen kommutieren mit jeder
\(\Pi_x\). Jede endliche Komposition, lineare Kombination, Adjungierung
und jeder durch solche Operatoren realisierte einzelne Messzweig tut das
ebenfalls. Starke beschränkte Grenzwerte bleiben im Kommutanten der Parität.

Der benötigte Link erfüllt dagegen
\(\Pi_xB=-B\Pi_x\) und \(\Pi_yB=-B\Pi_y\), während er die Gesamtparität
erhält. **Er liegt nicht in dieser bekannten lokalen geraden Algebra.**
Auch adaptives Wiederholen und Nachselektieren gerader Krauszweige kann
die Sektorgrenze nicht überwinden.

Die Voraussetzung „jeder realisierte Zweig ist gerade“ ist wesentlich.
Eine bloß paritätskovariante CP-Abbildung kann ungerade Krausoperatoren
besitzen. Der im Prüfer enthaltene Reset-Kanal auf einer Fermionmode ist
ein exaktes Gegenbeispiel zur unzulässigen stärkeren Behauptung.

Das beweist keinen universellen Unmöglichkeitssatz für den Compiler. Es
beweist, **welche neue Quelleneigenschaft gesucht werden muss**: eine
gerade Gesamtoperation, die bezüglich der zwei operational definierten
Teilbereiche ungerade ist, oder eine ursprüngliche Überlappung, durch die
die angenommene Zerlegung in unabhängig gerade Banken falsch war. Eine
andere bloße Clockphase oder weitere Boson-Paarumwandlung reicht nicht.

## 6. Was von der arithmetischen Untersuchung trägt

### 6.1 Eine einzelne endliche Bank ist nicht der volle Logarithmusgenerator

Quadratisches Ergänzen liefert mit der nativen Casimirnorm
\(\|\sum P_A^\dagger P_A\|\le480\)

\[
 H_{\rm nat}\ge\tfrac\Delta2N_b-C,
 \qquad C=960g^2/\Delta.
\]

Die externe Rechnung verwendet teilweise die schwächere Dreiecksgrenze
\(C=7680g^2/\Delta\), die ebenfalls gültig ist. Über Minmax, **nicht** eine
allgemeine Operator-Monotonie der Exponentialfunktion, folgen

\[
 N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60},
 \qquad \operatorname{Tr}e^{-\beta H}
 \le\frac{2^{64}e^{\beta C}}{(1-e^{-\beta\Delta/2})^{60}}.
\]

Das Zustandswachstum ist polynomial, während ein vollständiges Spektrum
\(E_*\log n+E_{\rm off}\), \(E_*>0\), exponentiell viele Zustände unter
wachsender Energie verlangt. Die ursprüngliche Bank kann dieses komplette
Spektrum daher nicht energieerhaltend mit nur affiner Skalenänderung tragen.
Diese Schranke widerlegt nicht jeden arithmetischen Untersektor, jede
nichtlineare Umparametrisierung oder jeden Nullstellenoperator.

Endlich viele solche Banken und endlich viele energetisch kontrollierte
Rotoren ändern den qualitativen Gegensatz nicht. Unendlich viele identische
Banken lösen ihn nicht automatisch: Bei gleichmäßig beschränkten lokalen
Anregungskosten divergiert bereits die globale Wärmespur. Ein geeigneter
relativer oder lokaler Spurbegriff wäre ein zusätzlicher Gegenstand.

### 6.2 Primzahlen können eine gewählte Dynamik organisieren, erzwingen sie aber nicht

Auf \(\ell^2(\mathbb N)\) kann man \(H_{\rm ar}|n\rangle=\log n|n\rangle\)
definieren. Die additive Primfaktorbesetzung erklärt dann die Eulerstruktur.
Der Definitionsbereich lautet \(\sum_n(\log n)^2|\psi_n|^2<\infty\).
Dass quantenstatistische Systeme mit Zeta-Zustandssumme existieren, ist
bereits ein Ergebnis von [Bost und Connes](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
Das ist ein relevanter Anschluss, nicht die fehlende native Herleitung.

Der gelieferte Cocycle \(c(m,n)=(-1)^{v_2(m)v_3(n)}\) ist assoziativ, weil
Bewertungen unter Multiplikation additiv sind. Für
\(T_m|n\rangle=c(m,n)|mn\rangle\) gilt
\(T_lT_m=c(l,m)T_{lm}\), insbesondere \(T_2T_3=-T_3T_2\).
Die unkontrollierten CP-Kanäle verlieren diese globale Phase und erfüllen
\(\mathcal E_l\mathcal E_m=\mathcal E_{lm}\). In kohärent kontrollierten
Wegen bleibt die relative Phase messbar. Das ist eine exakte Phasenstruktur,
aber kein Beweis einer Quellenauswahl dieses Cocycle oder von RH.

Strikt multiplikative Schritte \(m>1\) ergeben auch keine geschlossenen
Bahnen: \(n\mapsto mn>n\). Die Frequenz \(\log p\) eines Operators, eine
Bahnlänge \(r\log p\) und der Schwingungszeitraum \(2\pi/\log p\) müssen
auseinandergehalten werden. Hier hat der RH-Graph-Skill die Prüfung auf
Generator, Spur und Phase getrennt und eine bloße Analogieschließung verhindert.

### 6.3 Der RH-Zielsatz bleibt unbewiesen

Die vorgeschlagene Identität

\[
 \frac{\Xi(z)}{\Xi(0)}=\det(I-z^2A^{-2}),\quad
 \Xi(z)=\xi(\tfrac12+iz),
\]

für einen strikt positiven selbstadjungierten Operator \(A\) mit kompakter
Inverser und \(A^{-2}\) von Spurklasse wäre tatsächlich hinreichend:
Die gesamte rechte Funktion hat ihre Nullstellen nur bei reellen
\(\pm\lambda_j(A)\), einschließlich Multiplizitäten. Aber dieser Operator
und die gesamte Funktionsidentität sind **nicht konstruiert**. Ein Operator
mit lediglich den Imaginärteilen der Nullstellen wäre unzureichend.

Weder diese Prüfung noch die im externen Code bereits verwendete
Faktorisierung kleiner Testzahlen liefert einen neuen effizienten
Faktorisierungsalgorithmus, eine native Quantenoperation dafür oder eine
Lösung von P versus NP. Hylæan wurde in dieser Revision nicht neu geprüft.

## 7. Die lokale Polnäherung wird präziser, das relativistische Feld bleibt offen

Die externe Resolventenabschätzung ist korrekt: Im Kreis mit Radius
\(.1\Delta\) um den **tatsächlichen**, unbekannten negativen Pol \(-\epsilon\)
gilt

\[
 G(z)=\frac{Z}{z+\epsilon}+R(z),\qquad
 |R(z)|<.505213/\Delta.
\]

Der übrige Spektralträger ist mindestens \(.337373\Delta\) vom Pol entfernt.
Die relative Abweichung vom echten Polterm beträgt im Kreis unter 5,75 %.
Die Abschätzung setzt keine Intervallmitte anstelle von \(Z,\epsilon\) ein
und ist keine globale Vernachlässigbarkeit der Selbstenergie.

Aus v1.6.4 bleibt bestehen: Die exakte Zwei-Feld-Resolvente besitzt einen
nichtverschwindenden Rest \(\Sigma_2(z)\). Seine komplette Funktion ist
noch nicht bestimmt. Das neue kontrollierte Transportlemma benötigt sie
nicht vollständig, weil es den Rest durch eine Spektrallücke kontrolliert.

Ebenso bleibt der Feldtypentest bestehen: Der native antisymmetrische
Paartensor zusammen mit zwei gleichhändigen Weylfeldern und einem skalaren
Vermittler ergibt den verschwindenden Kanal. Ein symmetrischer Lorentz-
Spinortensor oder eine zusätzliche gleichgeladene zweidimensionale
Antisymmetriemarke eröffnet einen nichtverschwindenden Kanal, führt aber
zusätzliche Struktur ein. Ein internes Spin(10)-Spinorlabel ist kein
Lorentz-Weylindex. Der neue Link behebt diese Typfrage nicht.
Die Konventionen des bisherigen Tests sind mit der Primärübersicht von
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) verbunden;
ein neuer vollständiger relativistischer Adapter wurde hier nicht konstruiert.

Die spätere Feldtypenprüfung in `LATE_AUDIT.md` zeigt außerdem einen
Lorentz-erlaubten Zwei-Ableitungs-Kandidaten für den symmetrischen
Spinortensor und widerlegt einen pauschalen (1,1)-Ausschluss: Der
Energie-Impuls-Tensor ist schon bei Dimension vier zulässig. Weder ein
gesunder nativer Feldadapter noch ein dynamischer Gravitonpol folgt daraus.

## 8. Während der Arbeit entdeckte Änderung: „Kommutant 7“ richtig einordnen

Die strikte Originalquellenprüfung stoppte korrekt, als eine andere Arbeit
den früheren nativen Bericht ergänzte. Der alte Stand mit Hash
`1062e13fe0fb79cce015657a7b4d40a61e9639922ff95fa60c689c0068c38ffc`
blieb eingefroren. Der gesonderte geänderte Entwurf hat Hash
`ab745e74b1232b1ddf35dd0e0d0da4ace0176c797d769e5db8bedd0010bcba6a`.
Die in dieser Revision verwendeten Energie- und Polzertifikate änderten
sich bei dieser Prüfung nicht. Der Fehlerbeleg wurde aufbewahrt.

Der neue Entwurf listet drei dunkle Darstellungstypen mit Dimensionen
24.000, 11.200, 2.688; drei helle mit 2.880, 576, 320; und einen χ-Typ mit 64.
**Unter Voraussetzung dieser Zerlegung** lässt sich seine Folgerung exakt
nachprüfen:

\[
 \mathcal H_{N=3}\simeq
 \bigoplus_{d\in D}V_d\ \oplus\
 \bigoplus_{b\in B}(\mathbb C^2\otimes V_b)\ \oplus V_\chi.
\]

Die Summe ist \(37888+2\cdot3776+64=45504\). Die drei hellen Typen
kommen im **vollen** Raum jeweils zweimal vor. Daraus folgen:

- Nur die Gruppenwirkung hat einen Kommutanten der Dimension
  \(3+3\cdot4+1=16\), nicht sieben.
- Werden zusätzlich die nichtverschwindenden hellen Paarmischungen und
  \(N_b\) als Operationen zugelassen, erzeugen sie die vollständigen
  \(M_2\)-Multiplizitätsalgebren. Dann bleiben sieben zentrale Skalare.
- Sieben ist **keine absolute Untergrenze für beliebige weitere Operationen**.
  Ein erlaubter Operator, der diese sieben Blöcke verbunden mischt, zwingt
  die sieben Skalarwerte zur Gleichheit und lässt nur einen übrig. Der
  endliche Inzidenzmatrix-Test hat Rang sechs und beweist dieses Gegenargument.
- Die Zerlegung allein beweist weder operative Verfügbarkeit der
  kontinuierlichen Symmetrie noch einen Einzelfermion-Link. Selbst alle
  bankinternen Symmetrieoperationen erhalten die lokale Fermionparität.

Der interessante Wert sieben wird dadurch nicht verworfen. Korrigiert
werden die Aussagen „voller N=3-Raum multiplizitätsfrei“, „absolute Grenze
für jede Operation“ und eine unbewiesene Gleichsetzung von Symmetrie und
verfügbarem Instrument. Die genaue Darstellungszerlegung selbst bleibt in
diesem Zusatz eine externe Voraussetzung, kein frisch reproduzierter Satz.

Der Debugging-Skill führte hier zur Versionsprüfung statt zum Ersetzen
eines Pins. Das neue Manifest trennt deshalb einen erfolgreichen
**eingefrorenen Quellenreplay** von `originals_unchanged=false`.

## 9. T1–T8: was dieses Ergebnis beiträgt und nicht beiträgt

Die Begriffe folgen der aktuellen offenen Problemliste und ihrer
Forschungszuordnung. Keine Akzeptanzmarkierung wurde heraufgesetzt.

| Tor | Fehlender Nachweis | Beitrag dieser Revision |
|---|---|---|
| T1 | Ursprung von P1/P2, Dimension, Compiler- und Zustandswahl | Bekannte gerade Operationsalgebra ist für Einzeltransport unzureichend; ursprüngliche Auswahl weiter offen |
| T2 | Tatsächlich halbgeladenes, markiertes E8-Feld samt Renormierung, Energie- und Adjungiertenkontrolle | Der Ladung-eins-Lochzustand ist kontrolliert, aber nicht mit dem fehlenden Half-Charge-Feld identifiziert |
| T3 | Ein gemeinsamer, aus TFPT ausgewählter lokaler unitärer 3+1D-Parent | Vollständiger bedingter Zwei-Banken-Transfertest; kein ausgewählter räumlicher Parent |
| T4 | Chirales SM-Maß, Anomalien/Index, gleichmäßige Spiegelentkopplung | Feldtyp-Widerspruch weiter sichtbar; kein chirales Maß |
| T5 | Wechselwirkender Kontinuumsübergang, Lorentzverhalten, Clustering, Confinement und Streuung | Endliche-Sektor-Fehlerkontrolle ist ein Baustein, aber kein räumlicher Grenzübergang |
| T6 | Interne Herleitung aller Eichkopplungen und vollständiger Neutrinotextur/-skala | Keine neue Herleitung; \(\tau,\kappa\) sind deklarierte Testparameter |
| T7 | Masseloser dynamischer Spin zwei, beide Helizitäten, universelle Kopplung im selben Parent | Offen; der neue pauschale Ausschluss eines Dimension-vier-(1,1)-Tensors wurde korrigiert |
| T8 | Physische Präparation/Anfangszustand und ein gemeinsames Quellfunktional aller Auslesungen | Anfänglicher Polfilter wird für >89,7 % unnötig; geladene Präparation und Messinstrument weiter offen |

## 10. Nächste entscheidende Arbeiten mit klaren Abbruchkriterien

**A. Die Quelle des geraden Gesamtlinks finden.** Nicht noch eine riesige
Kontrollmatrix bauen, sondern für jeden tatsächlich ursprünglichen Generator
\(O\) prüfen, ob \([O,\Pi_x]\ne0\) bei erhaltener Gesamtparität möglich ist.
Eine positive Antwort muss Generator, Teilbereichsdefinition, Hilbertraum,
Gaussreferenz und Matrixelement liefern. Bleiben alle Generatoren lokal
gerade, ist die Suche nach dem Link durch deren weitere Komposition beendet.
Dann muss die ursprüngliche Teilraumdefinition oder der Quellenvertrag
explizit geändert werden; man darf keinen Hopterm als Ergebnis ausgeben.

**B. Die ursprüngliche Entnahme als gemeinsames Instrument realisieren.**
Eine Referenzmode könnte Ladung erhalten, während \(f_r\Omega\) präpariert
und ausgelesen wird. Zu prüfen sind ihre Herkunft, Energiekosten,
Erfolgshäufigkeit und Erhaltung der internen Kohärenz. Der neue Satz entfernt
bereits die zusätzliche Pflicht eines perfekten anfänglichen Energiefilters.
Er entfernt nicht die Pflicht, ein geladenes Instrument auszuweisen.

**C. Den Feldtyp vor räumlichen Rechnungen entscheiden.** Entweder folgt ein
passender Lorentzträger wirklich aus derselben Quelle, oder der skalare
Weyl-Ansatz wird in seiner jetzigen Form verworfen. Eine bloße zusätzliche
Verdopplung ohne Herkunft ist ein Modellvorschlag, keine Ableitung.

**D. Erst dann viele Banken.** Der nächste räumliche Test benötigt dieselbe
Quelle, einen bestimmten Graphen, Lokalisierung der Operationen und mit dem
Volumen verträgliche Fehler- und Energiebounds. Ein einziges neues Linklemma
liefert weder Raumdimension noch Lichtkegel, chirale Materie oder Gravitation.

**E. Arithmetik getrennt scharf halten.** Eine echte Verbindung müsste eine
gemeinsame Quellabbildung mit Generator, Zustands-/Spurstruktur, Phasen und
Domänen liefern. Die volle signierte Weilform oder die ganze Determinanten-
identität bleibt das Beweisziel. Der bloße Auftritt von Primzahlen erfüllt
keines davon. Der globale RH-Index ließ sich wegen einer fehlenden
historischen Quelle und veränderter Review-Quellen nicht vollständig
aktualisieren; die gezielte Originalquellenprüfung ist enger als ein
frischer Gesamtindex. Es wurde kein RH-Abschlusskandidat registriert.

## 11. Reproduktion und ehrliche Liefergrenze

`replay.py --frozen-only` führt die fünf Prüfer normal und mit `-OO` aus,
vergleicht beide JSON-Ergebnisse und die zwei externen Originalberichte,
prüft alle eingefrorenen Quellen und protokolliert Änderungen der
Originalorte gesondert. Ein Fehler führt zu FAIL. Der zuvor aufgetretene
Live-Quellenfehler bleibt in `source_drift_failure_receipt.json` sichtbar.

Die abgesicherten Zahlen stehen vollständig rational in
`two_bank_transfer_normal.json`; Dezimalwerte dienen nur der Lesbarkeit.
Die analytische Beweiskette steht in Abschnitt 4. Das Paket umfasst die
unveränderten externen Arbeiten, deren Programme, die native v1.6.4-Abhängigkeit
und alle neuen Berichte. NumPy, SymPy und für das ältere native Paket dessen
separat dokumentierte Voraussetzungen sind zu unterscheiden.

Die versionierte ausführliche Markdown-Lieferung enthält zusätzlich den
vollständigen eingefrorenen nativen Herleitungsbericht v1.6.4 als historischen
Anhang. Daneben gibt es ein kurzes Update und eine bildliche Erklärung.
**Die großen TFPT-Haupt-PDFs und die Webseite werden in dieser Revision nicht
als aktualisiert ausgegeben. Es gab keinen Commit oder Push.**


---

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


---

# Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

# TFPT / Universalraum: nativer Pol, Bewegungsgleichung und minimale Feldtypen

**Konsolidierte Forschungsfortsetzung v1.6.4 · 15. September 2026**

Diese Revision verbindet den während der Arbeit neu eingegangenen Polsatz
v1.6.3 mit einer unabhängig begonnenen Untersuchung der nativen
Bewegungsgleichung. Sie ergänzt die bisherigen Hauptdokumente; sie ist
keine verkürzte Neufassung des vollständigen Hauptbuchs. Die vorhandenen
Haupt- und Update-PDFs wurden in dieser Runde nicht verändert.

## 1. Ergebnis in einem Satz

Auf dem abgesicherten Grundzustand des festgelegten nativen Fockmodells
existiert eine isolierte ursprüngliche Fermion-Entnahmelinie; nach
Kombination beider Rechnungen trägt sie **mehr als 88,007628 % des gesamten
normierten Spektralgewichts pro Mode**. Die zusätzliche Antwort ist jedoch
nicht exakt auf eine einzige weitere Linie reduzierbar. Ihr erster
Rückwirkungsschritt wird direkt von derselben ursprünglichen Wechselwirkung
bestimmt.

Am Prüfpunkt \(g/\Delta=1/20\), ausdrücklich ohne \(\mu N\)-Zusatz:

| Größe | Eingegangene v1.6.3 | Konsolidierte strengere Grenze |
|---|---:|---:|
| Mittlere Bosonenzahl | \(0.77<\bar b<1.45\) | \(0.842846<\bar b<1.245656\) |
| Energie der niedrigen Entnahmelinie | \(0.007737<\epsilon/\Delta<0.062277\) | \(0.007737<\epsilon/\Delta<0.039079764\) |
| Gewicht dieser Linie im gesamten CAR-Maß | \(Z_{\rm low}>0.864972353\ldots\) | \(Z_{\rm low}>0.880076280689\ldots\) |
| Obere Gewichtsgrenze | \(Z_{\rm low}<0.9759375\) | \(Z_{\rm low}<0.9736610625\) |
| Übrige Entnahmeenergien | \(>0.379636\Delta\) | unverändert |
| Sämtliche Additionsenergien | \(>0.329636\Delta\) | unverändert |

Die Dezimalzahlen sind gerundete Darstellungen rationaler Schranken.
Es sind weder exakte Polpositionen noch angepasste Zentralwerte. Der Pol
steht im retardierten Spektrum bei negativer Frequenz \(-\epsilon\).
Das niedrige Niveau im N=63-Hilbertraum ist 64-fach entartet; jede
diagonale Modenantwort sieht dieselbe Linie.

**Nicht bewiesen:** die physische Herleitung des Hamiltonoperators, sein
vollständiger Operationssatz, native Präparation, räumliche Ausbreitung,
ein vollständiges relativistisches Feldwörterbuch oder eine TOE. T1–T8
bleiben als vollständige Aufgaben offen.

## 2. Ein unveränderter Modellvertrag

Es werden keine Hopping-, Massen-, Ladungs- oder Projektionsglieder zu H
hinzugefügt:

\[
H=\Delta N_b+g(Q_++Q_-),\quad Q_+=\sum_A b_A^\dagger P_A,
\quad Q_-=Q_+^\dagger,
\]
\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad N=N_f+2N_b,
\quad WW^\dagger=8I_{60}.
\]

Es gibt 64 CAR-Fermionmoden, 60 CCR-Bosonmoden und 480 von null
verschiedene reelle W-Einträge mit ihren ursprünglichen Vorzeichen.
\(\Delta>0\), g ist reell; die Zahlen beziehen sich auf \(g/\Delta=1/20\).
Die Tensorquelldatei ist durch SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`
fixiert.

Die Fockrealisierung, H, der sektorenübergreifende Energievergleich und
der Prüfparameter sind weiterhin Modellvoraussetzungen. Die geometrische
oder arithmetische Herkunft eines W-Tensors leitet diese Voraussetzungen
nicht allein her. Insbesondere sind die fünf elementaren CAR in einer
Spinor-Matrixkonstruktion nicht mit den hier verwendeten 64 Fockmoden
gleichzusetzen.

## 3. Was tatsächlich erneut geprüft wurde

### 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine
eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch
mit neu kompiliertem Quellcode berechnet:

| Ordnung | Vollständig enumerierte Bosonkonfigurationen | Normquadrat von \(Q_+^kF\) |
|---|---:|---:|
| 0 | analytischer Ausgangszustand | 1 |
| 1 | 60 Kanäle / 480 Paare | 480 |
| 2 | 1830 | 439680 |
| 3 | 37820 | 575078400 |
| 4 | 595665 | 952296652800 |

Zusätzlich wurden unabhängige Wortentwicklungen, Überlaufgrenzen, die
vollständige Zweikörper-Casimiridentität, rationale Sektorvergleiche und
die unabhängige Symmetriespurrechnung wiederholt. Die vier ausgewählten
ursprünglichen Zertifikate bestehen normal und unter `-OO` mit identischen
JSON-Bytes. Dies ist eine gezielte erneute Grundzustandsprüfung, nicht die
Behauptung, alle historischen Repository-Tests erneut ausgeführt zu haben.
Der unveränderte alte Normprüfer gibt unter dem aktuellen NumPy eine
ComplexWarning bei der Ganzzahlkonversion aus. Die neuen Prüfer bestätigen
vor jeder Konversion exakt verschwindende Imaginärteile und ganzzahlige
Realteile des gepinnten W. Die Warnung ist gespeichert und wird nicht
als verlorener Tensoranteil oder als unterdrückter Prüffehler ausgegeben.

Der modellinterne Satz bleibt bestehen: Für
\(0<|g|/\Delta\le1/20\) ist der globale Grundzustand \(\Omega\)
eindeutig, hat N=64 und ist Spin(10)×SU(4)-invariant. Am Zahlenprüfpunkt:

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad \operatorname{gap}(H)>0.007737\Delta.
\]

Der volle Grundzustandsvektor ist damit nicht ausgerechnet. Die fünf
Versuchsvektoren sind keine behauptete invariante Fünferbasis für H.

### 3.2 Das neu eingegangene Polergebnis

Der vollständige technische Bericht v1.6.3 und sein 248-zeiliger Prüfer
wurden gelesen; Quellen, Bericht, Ergebnismatrix und Prüfpaket wurden
unverändert archiviert. Der Prüfer wurde normal und optimiert wiederholt:
**317 Prüfbedingungen, identische JSON-Bytes auch zum gelieferten Bericht**.

Der Herkunftspin des Prüfers ist
`fdbcabd244450c302182086d67c68284634c994e3fee026200c42c508f731654`.
Er verwendet denselben ursprünglichen `verify_hole.py`-Quellstand wie
die bisherige Fortsetzung. Die neuen eigenen Sektorvergleiche wurden
zusätzlich unabhängig mit rationalen LDL-Pivots berechnet.

Die Prüfzahlen zählen auch Komponenten und Wiederholungen; sie sind
keine Zahl unabhängiger Entdeckungen. Die analytischen Argumente sind
ausgeschrieben, aber nicht vollständig in einem Beweisassistenten formalisiert.

## 4. Der einfache native Anschluss: Bewegungsgleichung statt Umdeutung

Erweitere jede W-Zeile zur antisymmetrischen Matrix \(M_A\) mit
\((M_A)_{ij}=W_{A,ij}\) für i<j. Definiere

\[
D_r=\sum_{A,j}(M_A)_{rj}b_Af_j^\dagger,
\qquad \phi_r=D_r/\sqrt{15}.
\]

Direkte CAR/CCR-Normalordnung liefert **Operatoridentitäten auf dem
endlichen Teilchenkern**, nicht nur Gleichheiten auf Testzuständen:

\[
\boxed{[H,f_r]=-gD_r,\qquad [H,f_r^\dagger]=gD_r^\dagger,}
\]
\[
[N,D_r]=-D_r,\qquad \{f_r,D_s^\dagger\}=0.
\]

Der neue Vergleichsoperator hat also dieselbe Ladung −1 wie f.
Er ist nicht das früher auf dem leeren Referenzzustand betrachtete
\(\chi^\dagger\sim b^\dagger f^\dagger\) mit Ladung +3.
Auf dem Grundzustand liegen \(f\Omega\) und \(D\Omega\) in N=63,
\(\chi^\dagger\Omega\) dagegen in N=67. Neutrale Zeitentwicklung
hebt diese Unterscheidung nicht auf.

Die Normalordnungsprüfung erfasst alle 64 ursprünglichen f-Operatoren
und die tatsächlichen W-Vorzeichen. Für die Kompositnorm gilt exakt

\[
\{D_r,D_s^\dagger\}=
\sum_{A,B,j,k}(M_A)_{rj}(M_B)_{sk}
\left(\delta_{AB}f_j^\dagger f_k+\delta_{jk}b_B^\dagger b_A\right).
\]

Mit \(\bar b=\langle N_b\rangle\) und der Grundzustandssymmetrie:

\[
\langle\{D_r,D_s^\dagger\}\rangle=\delta_{rs}S,
\qquad S=15-\frac7{32}\bar b.
\]

\(\phi\) hat entsprechend Norm \(1-7\bar b/480\), nicht globale
kanonische CAR. Der normierte Zustandserwartungswert ersetzt keine
Operatorrelation.

## 5. Dieselbe Antwort auf demselben Grundzustand

Für Im z>0 und \(H_n=H|_{N=n}\):

\[
G_{rs}(z)=\langle\Omega|f_r(z+E_0-H_{65})^{-1}f_s^\dagger|\Omega\rangle
+\langle\Omega|f_s^\dagger(z-E_0+H_{63})^{-1}f_r|\Omega\rangle.
\]

Die innere Symmetrie macht G diagonal und alle Diagonalelemente gleich.
Schreibe mit positiven Entnahme- und Additionsmaßen auf \(\epsilon>0\)

\[
G(z)=\int\frac{d\nu_+(\epsilon)}{z-\epsilon}
+\int\frac{d\nu_-(\epsilon)}{z+\epsilon}.
\]

Dann gelten exakt

\[
Z_+=\bar b/32,\quad Z_-=1-\bar b/32,
\quad a:=\int\epsilon\,d\nu_+=\int\epsilon\,d\nu_-
=\frac{\Delta\bar b-E_0}{64}.
\]

Für das gesamte signierte Spektralmaß:

\[
\boxed{m_0=1,\quad m_1=0,\quad m_2=g^2S,\quad
m_3=g^2(\Delta S+7a).}
\]

Die ersten beiden Momente und die Kanalgewichte stimmen mit der
eingegangenen unabhängigen Rechnung überein. **Das dritte Moment ist der
zusätzliche eigene Schritt dieser Revision.**

### 5.1 Herleitung des dritten Moments

Setze \(\mathcal L A=[A,H]\). Stationarität macht diesen Operator
symmetrisch in der positiven, nach Nullvektoren quotientierten Metrik
\((A,B)=\langle\{A^\dagger,B\}\rangle\). Direkte Normalordnung ergibt

\[
\sum_r\{[D_r,X],D_r^\dagger\}=-14Q_+.
\]

Die beiden Beiträge sind \(16Q_+\) und \(-30Q_+\). Ihre Koeffizienten
folgen aus den vollständig geprüften Kontraktionen
\(\sum_{rj}M_{A,rj}M_{B,rj}=16\delta_{AB}\) und
\(\sum_{Ar}M_{A,rj}M_{A,rk}=15\delta_{jk}\).
Mit \([D,N_b]=D\) und
\(\langle Q_+\rangle=(E_0-\Delta\bar b)/(2g)\) folgt die Formel.

Als unabhängige Kontrolle wurden sämtliche Formeln einschließlich m3
an der früher exakt geschlossenen N=4/N=5-Antwort symbolisch geprüft.
Diese Kontrolle verwendet den früheren Referenzzustand nur als Test
der Identitäten, nicht als Ersatz für den nativen Grundzustand.

Die allgemeine Methode, Spektralmomente aus Bewegungsgleichungen zu
gewinnen, ist etabliert; siehe
[Freericks und Turkowski, Phys. Rev. B 80, 115119](https://arxiv.org/abs/0907.1284).
Die hier angegebenen W-Kontraktionen und Konstanten wurden eigenständig
für dieses Modell berechnet; die zitierte Arbeit beweist keine TFPT-Aussage.

### 5.2 Neue engere Dichte- und Gewichtsgrenzen

Positivität der beiden Antwort-Grammatrizen beziehungsweise zweimal
Cauchy–Schwarz liefern

\[
m_2\ge a^2\left(\frac1{Z_-}+\frac1{Z_+}\right),
\]
\[
\boxed{(\Delta\bar b-E_0)^2\le
60g^2\bar b(32-\bar b)(1-7\bar b/480).}
\]

Mit der bereits bewiesenen Energieobergrenze und \(g/\Delta=1/20\)
muss das folgende rationale Polynom positiv sein:

\[
P(b)=\frac7{3200}b^3-\frac{61}{50}b^2
+\frac{317591}{125000}b-\frac{79754843281}{62500000000}>0.
\]

Seine beiden im alten zulässigen Bereich liegenden Nullstellen liegen
bei ungefähr 0.842846697 und 1.245655664. Exakte rationale Wurzelisolation
ergibt die nach außen gerundete strenge Schranke

\[
\boxed{0.842846<\bar b<1.245656.}
\]

Damit:

| Größe pro Mode | Strenges offenes Intervall |
|---|---:|
| Gesamtes Additionsgewicht | (0.0263389375, 0.03892675) |
| Gesamtes Entnahmegewicht | (0.96107325, 0.9736610625) |
| \(\langle\{\phi,\phi^\dagger\}\rangle\) | (0.981834183333…, 0.987708495833…) |
| Frühere \(\chi\)-Kompositnorm, nicht \(\phi\) | (0.040386370833…, 0.059687683333…) |

Das sind Erwartungswerte und integrierte Spektralgewichte, keine direkten
Nachweise von Produktionsraten oder von bereits verfügbaren Messinstrumenten.

## 6. Der Polsatz und seine zusätzliche Verschärfung

Der eingegangene Beweis verwendet
\(u_{k,r}=Q_+^kf_rF=f_rQ_+^kF\). Invarianz und Besetzung ergeben

\[
\langle u_{k,r},u_{k,s}\rangle=
\delta_{rs}\frac{64-2k}{64}\|Q_+^kF\|^2.
\]

Die Normen lauten 1, 465, 412200, 521164800, 833259571200.
Die daraus gebildete fünfdimensionale Variationsmatrix gibt 64 unabhängige
Richtungen unter \(-1.095812\Delta\). Das gesamte N=63-Komplement des
Nullbosonraums liegt über \(-3\Delta/4\). Minimax begrenzt den niedrigen
Raum auf genau 64 Dimensionen; seine injektive symmetrieverträgliche
Projektion auf die irreduzible duale 64 erzwingt ein einziges Energieniveau.

Das beweist Existenz und Isolation. Seine Sichtbarkeit folgt aus den
positiven Entnahmemomenten. Mit

\[
d=0.007737\Delta,\quad c=0.379636\Delta,
\quad a_{\max}=\frac{1.245656+1.158089}{64}\Delta
\]

gilt

\[
Z_{\rm low}>\frac{c(1-1.245656/32)-a_{\max}}{c-d}
=\frac{40912436089}{46487375000}
=0.8800762806891118\ldots.
\]

Außerdem ist der niedrige Pol die kleinste Entnahmeenergie. Daher
\(a\ge\epsilon_{\rm low}Z_-\), also bereits ohne vollständige
Polauswertung

\[
\frac{\epsilon_{\rm low}}\Delta
<\frac{1.245656+1.158089}{64-2(1.245656)}
=\frac{2403745}{61508688}=0.039079763821332\ldots.
\]

Diese Verschärfungen entstehen aus dem **Zusammenführen kompatibler
Beweise**, nicht aus einem neuen gewählten Parameter. Das Restgewicht
des gesamten CAR-Maßes ist somit kleiner als 0.119923719311… .

## 7. Einfache Organisation, aber keine falsche Zwei-Linien-Lösung

Die ersten zwei orthonormalen Operatoren sind f und \(D/\sqrt S\).
Die erste Resolventenreduktion hat deshalb die exakte Form

\[
\boxed{G(z)=\frac1{z-\displaystyle\frac{g^2S}{z-a_1-\Sigma_2(z)}}},
\qquad a_1=\Delta+\frac{7a}{S}.
\]

\(\Sigma_2\) ist die Resolvente des verbleibenden nativen Operatorraums,
gekoppelt an den dazu orthogonalen Rest von
\(\mathcal L(D/\sqrt S)\). Es wurde kein äußeres Bad hinzugefügt.
Dies ist eine genaue Ordnung der Rechnung, **keine abgeschlossene
Berechnung von \(\Sigma_2\)** und keine Vereinigung sämtlicher TOE-Aufgaben
in einer einzigen bereits gelösten Funktion.

### 7.1 Warum man die Rückwirkung nicht exakt weglassen darf

Angenommen, es gäbe nur je eine Entnahme- und Additionslinie mit
Energien \(\epsilon_-,\epsilon_+\). Symmetrie macht diese für alle r gleich.
Dann liefern die Bewegungsgleichungen auf demselben Grundzustand

\[
D_r\Omega=-\frac{\epsilon_-}{g}f_r\Omega,
\qquad D_r^\dagger\Omega=\frac{\epsilon_+}{g}f_r^\dagger\Omega.
\]

Summe nach Multiplikation mit \(f_r^\dagger\) beziehungsweise \(f_r\)
und N=64 ergeben

\[
H\Omega=\left[-32\epsilon_-+
(\Delta-\epsilon_++\epsilon_-)N_b\right]\Omega.
\]

Ein Eigenzustand mit negativer Energie kann keine feste Bosonenzahl haben:
Dann wäre \(\langle Q_++Q_-\rangle=0\) und seine Energie
\(\Delta\langle N_b\rangle\ge0\). Daher sind \(\Omega\) und
\(N_b\Omega\) unabhängig. Die angenommene Zweilinienform erzwingt
\(\epsilon_+-\epsilon_-=\Delta\).

Andererseits geben \(m_0=1,m_1=0\) für ein Zweilinienmaß
\(m_3/m_2=\epsilon_+-\epsilon_-\). Die exakt bestimmte Formel lautet
jedoch

\[
\frac{m_3}{m_2}=\Delta+7a/S>\Delta.
\]

Widerspruch. Damit ist \(\Sigma_2\not\equiv0\) bewiesen. Mindestens
ein Kanal besitzt mehr als eine Energielinie. Der dominante isolierte
Entnahmepol und diese unvermeidliche Reststruktur widersprechen einander nicht.
Eine Zweilinienform könnte höchstens eine zu zertifizierende Näherung sein.

## 8. Was der Operationssatz jetzt tatsächlich hergibt

| Vertrag | Mathematisch abgesichert | Nicht dadurch verfügbar |
|---|---|---|
| Markierter endlicher Matrixcompiler | Matrizen, Ordnungen, konkrete endliche Syntheseidentitäten | Vollständiges Fockinstrument, Präparation, physischer Zeitgenerator |
| H allein | Modellzeitentwicklung | Unabhängiges Schalten von X und \(N_b\) |
| X und \(N_b\), wenn als Kontrollen gewährt | N=3-Kontrollalgebra der Dimension 14 | Beliebige Modenoperationen |
| Zusätzlich dokumentierter vorzeichenrichtiger Clock-Lift | N=3-Kontrollalgebra der Dimension **84** | Vollständige Zustandsunterscheidung oder Ladung-eins-Instrument |

Die neue Clock-Rechnung wurde übernommen und reproduziert. Die fünf
Multiplizitätszeilen für die sechs Clockphasen sind:

| Teilraum | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Dunkle F3 | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |
| Dunkle BF | 16 | 8 | 8 | 16 | 8 | 8 |
| Aktiv 7 | 560 | 440 | 440 | 560 | 440 | 440 |
| Aktiv 10 | 112 | 88 | 88 | 112 | 88 | 88 |
| Aktiv 12 | 80 | 40 | 40 | 80 | 40 | 40 |

Die aktiven Zeilen tragen zusätzlich einen Zweiniveaufaktor. Alle 45504
N=3-Zustände sind erfasst; der Kommutant hat weiterhin Dimension
240742144. Die alte Zahl 14 beschreibt den engeren Zweikontrollvertrag,
nicht den jetzt zusätzlich geprüften Clockvertrag.

### 8.1 Konkrete Präparationsgrenze

Alle genannten Fockkontrollen erhalten N. Ein Wort aus ihnen und jeder
einzeln zahlenerhaltende ausgewählte Messzweig bleiben im Ausgangssektor.
Sie können aus dem leeren N=0-Zustand **nicht** den N=64-Grundzustand
erzeugen. Diese Aussage betrifft zahlenerhaltende Krauszweige; eine bloß
U(1)-kovariante offene Dynamik kann sehr wohl geladene Krausoperatoren haben.

Auch aus dem voll besetzten F führt bloßes \(e^{-itH}\) nicht zur
Konvergenz auf \(\Omega\): Der Grundzustandsüberlapp bleibt konstant.
Normiertes \(e^{-\tau H}F\) konvergiert mathematisch mit der bewiesenen
Lücke, benötigt aber eine gesonderte Instrument- und Ressourcenherleitung.

### 8.2 Der kleinste konkrete Ladungstest

Ein Kandidat ist eine explizite Referenzmode c mit
\(T=\lambda(c^\dagger f_r+f_r^\dagger c)\). Sie erhält die gemeinsame
Ladung, verändert aber die Ladung der ursprünglichen Bank. Der endliche
Austausch- und Detuningtest ist exakt; **dieses T wurde nicht als neuer
nativer Hamiltonterm eingeführt**.

Für dieselbe N=64-Präparation unter \(H+\mu N\) gilt
\(G_\mu(z)=G_0(z-\mu)\), insbesondere \(m_1=\mu\).
Das misst nur gegen eine festgelegte Referenz: Ein gemeinsamer Zusatz
\(\mu(N_{\rm Bank}+N_{\rm Referenz})\) bleibt unsichtbar. Die Spektral-
schranken dieses Berichts gelten als Grundzustandsschranken nur für μ=0.

## 9. Relativistisches Wörterbuch: Ausschluss und zwei präzise Alternativen

Die Indexfrage darf nicht nachträglich durch einen Namen beantwortet werden.
Die Konventionen für Zweikomponentenspinoren wurden mit
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) abgeglichen;
die folgenden speziellen W-Tests sind eigene exakte Tensorrechnungen.

### 9.1 Was nicht funktioniert

Für 64 gleichhändige Weylfelder mit innerem Index I und einen skalaren
Vermittler ist \(M_A\otimes\varepsilon_{\rm Lorentz}\) symmetrisch.
Die Grassmann-Antisymmetrisierung verschwindet daher identisch, für alle
60 W-Zeilen. Außerdem lässt die volle irreduzible innere Darstellung
\(16\otimes4\) auf denselben 64 Komponenten nach Schur keine zusätzliche
kommutierende nichttriviale Lorentzspinorwirkung zu.

### 9.2 Bereits bekannter nichtverschwindender Typ

Ein symmetrischer Lorentzspinortensor koppelt an das antisymmetrische M.
Der Vermittler hat dann einen passenden dualen (1,0)-Typ samt adjungiertem
Typ. Diese Variante besteht den algebraischen Nichtnulltest, aber noch
keinen vollständigen Kinetik-, Positivitäts-, Constraints- oder Herkunftstest.

### 9.3 Neue minimale skalare Alternative — ausdrücklich zusätzlich

Will man zugleich W, gleiche Weylhand, lokale Bilinearität und einen
skalaren Vermittler behalten, kann man einen **unabhängigen** Hilfsindex
a=1,2 mit alternierender Form einführen:

\[
b_A^\dagger(M_A)_{IJ}\varepsilon_{ab}
\varepsilon_{\alpha\beta}\psi_{I a\alpha}\psi_{J b\beta}
+\mathrm{h.c.}
\]

M und \(\varepsilon_{ab}\) sind jeweils antisymmetrisch; ihr Produkt
ist als innerer Kopplungstensor symmetrisch. Zusammen mit der Lorentz-
Epsilonform ist der Gesamttensor antisymmetrisch und nicht null.
Alle 60 Kanäle bestehen den Test. Eine nichtverschwindende alternierende
Form existiert nicht in Dimension eins; in Dimension zwei ist sie bis
auf Normierung eindeutig. **In dieser eng benannten Klasse von
Tensorfaktor-Reparaturen ist die binäre Ergänzung minimal.**

Das ist noch keine gefundene native Lösung: Sie verdoppelt die inneren
Weylkomponenten von 64 auf 128, zusätzlich zu deren Lorentzspinorindex.
Ein Double-Cover-Minuszeichen stellt nicht automatisch zwei unabhängige
Felder bereit. Auch Nambu-Umbenennung \((f,f^\dagger)\) genügt nicht:
Das gemischte Produkt hat Ladung null statt −2, sodass derselbe
\(b^\dagger ff\)-Ladungsvertrag nicht erhalten bleibt.

Der entscheidende Quellenauftrag ist daher eng: Gibt es diese zweite
gleichgeladene, CAR-unabhängige Komponente bereits im tatsächlichen
Compilerprozess? Und liefert ihre Projektion genau das bisherige H und
die geprüfte Antwort? Ohne beides bleibt die skalare Alternative ein
zusätzliches Modell, nicht eine Erklärung des ursprünglichen.

## 10. Nächste Schritte mit eindeutiger Erfolgskontrolle

1. **Native Quelle des Austauschoperators bestimmen.** Ein tatsächliches
   Operationswort mit Anfangszustand, Detektor, Adjungiertem, Ladungsbilanz
   und Record angeben. Ein weiteres neutrales Wort oder bloßer
   Algebraabschluss schließt diese Aufgabe nicht.
2. **Den Rest der nativen Antwort kontrollieren.** Das nächste Ziel ist
   \(\Sigma_2\) beziehungsweise sein erster Norm- und Momentkoeffizient,
   gemeinsam in N=63,64,65. Die vorliegenden Summenregeln und Polschranken
   sind zwingende Akzeptanztests. Den Rest auf null zu setzen ist exakt
   ausgeschlossen; eine Näherung braucht eine Restfehlergrenze.
3. **Die beiden Feldtypen an der Quelle entscheiden.** Entweder der
   symmetrische Vermittler mit korrektem Adjungierten und Kinetik, oder
   der skalare Typ mit wirklich nachgewiesener zweiter Komponente.
   Erst Nichtnullkopplung, Symmetrie, Ladung, CAR und positive Kinetik
   gemeinsam zählen als Feldadapter.
4. **Erst danach zwei operational bestimmte Teile verbinden.** Für einen
   tatsächlich hergeleiteten ungeraden Austausch wäre das projizierte
   Ein-Loch-Transfermatrixelement proportional zum jetzt eingeschlossenen
   Residuum. Ein solches formales Matrixelement beweist weder Verfügbarkeit
   des Austauschs noch einen isolierten Zweibank-Gesamtraum oder höhere
   Störungsordnungen. Eine räumliche Skalierung wurde hier nicht vorgezogen.

| Tor | Nutzen dieser Revision | Entscheidender verbleibender Nachweis |
|---|---|---|
| T1 | Exakter Clock-Kontrollabschluss und engere Ressourcenfrage | Ursprüngliches vollständiges Operations- und Rahmenwörterbuch |
| T2 | Geladene native Antwort, sichtbarer Pol, drittes Moment | Quelleneinbettung und renormiertes Half-Charge-Feld mit Energie/Adjungiertem |
| T3 | Präzise Anforderung an ungeraden Austausch | Gemeinsamer operationaler räumlicher, schließlich 3+1D-Träger |
| T4 | Falscher Skalartyp ausgeschlossen, minimale Alternativen | Chirales Maß, Anomalien, Spiegelkontrolle, vollständige Feldkinetik |
| T5 | Pole und Reststruktur lokal kontrolliert | Gemeinsamer wechselwirkender Grenzwert, Clusterstruktur, Streuung |
| T6 | Strengere interne/Lorentz-Indexbilanz | Familien, Massen und Kopplungen auf demselben physikalischen Träger |
| T7 | Keine neue Spin-2-Konstruktion | Dynamischer Spin 2, Helizitäten und universelle Kopplung |
| T8 | Eindeutiger Modellgrundzustand; Präparationslücke konkret | Primitive Zustandswahl, Ressourcen, Records und Instrumente |

## 11. Erratum und Versionsdisziplin

Im eigenen v1.6.2-Text fehlte in Abschnitt 5.2 zwischen Entnahme- und
Additionsresolvente ein Pluszeichen. Richtig ist auf der dortigen
N=4-Referenz
\(G=Z_h/(z+\epsilon_h)+a^\dagger(z+E_--H_5)^{-1}a\).
Die früheren Prüfrechnungen verwendeten die additive CAR-Gewichtsregel;
der Darstellungsfehler wird hier ausdrücklich korrigiert. Die archivierte
v1.6.2 wird nicht stillschweigend umgeschrieben.

Die zugelieferte v1.6.3 bleibt ebenfalls unverändert. Ihre Pol- und
Clockbefunde sind als übernommene und frisch reproduzierte Ergebnisse
kenntlich. Die engeren Schranken, das dritte Moment, der Ausschluss der
exakten Zweilinienantwort und die minimale skalare Hilfsindexalternative
sind die eigenen zusätzlichen Ergebnisse dieser Konsolidierung.
Kein literaturweiter Neuheitsanspruch, keine experimentelle Bestätigung
und kein Gesamtabschluss werden behauptet.
