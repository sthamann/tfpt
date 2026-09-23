# Native Familienclocks, Flavorcompiler und symmetrischer Quellenkanal

22. September 2026 · `UR.SOURCE.NATIVE_CLOCK_FLAVOR.01` · **PARTIAL**

## Frage und Ergebnisgrenze

Die Frage ist, ob die bereits vorhandenen Familienclocks und Flavoroperatoren
eine gemeinsame, korrekt typisierte Quelle für einen Yukawa-Vertex liefern
können. Der ältere relative-Clock-Ausdruck wird nicht als neue Entdeckung
ausgegeben. Neu geprüft werden sein Anschluss an die originalen Matrizen,
die vollständige diskrete Clockklasse, ihr CP-Verhalten und ihre Grenze
gegenüber der bestehenden TFPT-Massenleiter.

Das Ergebnis ist ein gemeinsames endliches Wörterbuch mit expliziter
Determinantenlinie, ein universelles Rangkriterium und eine exakte bedingte
CP-Konstruktion. Die physische Auswahl des Zustands, des Vertizes und seiner
Zeitkorrelatoren ist damit nicht hergeleitet. Insbesondere sind interne
Clock-Wirkungen keine bereits bewiesene physische Zeitentwicklung.

## 1. Ein gemeinsames Wörterbuch für die tatsächlichen Originaloperatoren

Die Originale aus v50 und der späteren D4-Konstruktion sind

\[
 Q=\begin{pmatrix}3&1&0\\3&2&0\\3&2&1\end{pmatrix},\quad
 \Sigma=\operatorname{diag}(1,-1,-1),\quad
 T=\begin{pmatrix}0&1&0\\1&0&0\\2&-2&1\end{pmatrix},\quad G=T\Sigma.
\]

Der vorherige gemeinsame Residuen-Audit liefert unter seiner benannten
Ganzzahligkeits-/Unimodularitätsbedingung die positive Form

\[
 N=\begin{pmatrix}1&0&0\\0&5&-2\\0&-2&1\end{pmatrix}.
\]

Die exakten Monodromievertreter aus v117 heißen hier, zur Vermeidung einer
Verwechslung mit dieser Metrik,

\[
 M=\begin{pmatrix}
 0&-(1+i)/2&(1-i)/2\\
 -(1+i)/2&-i/2&-1/2\\
 (1-i)/2&-1/2&i/2
 \end{pmatrix},\qquad U=\operatorname{diag}(1,i,-i).
\]

Es gibt **keinen** gewöhnlichen invertierbaren Intertwiner von G nach U:
det G = tr G = −1, während det U = tr U = 1.
Die passende Darstellung ist E⊗det(E), also die ursprüngliche
Dreierdarstellung mit ihrer Orientierungsgeraden. Auf G und T multipliziert
der Determinantencharakter jeweils mit −1. Auf geraden Dreierzyklen ist er +1.
Diese Gerade ist eine vorhandene kanonische Tensorkonstruktion; ihre Verwendung
im physischen Feld ist eine zu prüfende Identifikation, keine CAR-Parität.

Setze b=(1+i)/2 und

\[
 S=\begin{pmatrix}0&-2&1\\-b&ib&0\\-ib&b&0\end{pmatrix},\quad
 B=\begin{pmatrix}1&0&0\\0&0&-1\\0&-1&0\end{pmatrix}.
\]

Dann gelten exakt

\[
 S^\dagger S=N,\quad\det S=-i,\quad
 S(-G)S^{-1}=U,\quad S(-T)S^{-1}=-B=U^2MUM.
\]

Auch die Dreierclock erhält einen originalen ganzzahligen Vertreter:

\[
 P=S^{-1}MS=\begin{pmatrix}0&-2&1\\1&0&0\\2&1&0\end{pmatrix},\quad
 P^3=I,\quad P^TNP=N.
\]

Dies ist tatsächlich ein Dreierzyklus auf demselben Viermarkenraum.
Mit den schon vorher verwendeten Matrizen

\[
 H=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\-1&-1&-1\end{pmatrix},\quad
 X=\begin{pmatrix}-1&-3&1\\1&1&-1\\1&-1&1\end{pmatrix}
\]

gilt ΠHX=HXP, wobei Π die Marken 0→1→3→0 permutiert und 2 festhält.
Damit ist die Identifikation nicht bloß eine Übereinstimmung von Dimensionen
oder Eigenwerten. Sobald diese drei markierten Generatorzuordnungen festliegen,
ist der Intertwinerraum eindimensional; die Isometrie ist bis auf eine globale
Phase bestimmt. Eine physische Auswahl gerade dieser Markenzuordnung folgt
daraus nicht. Eine Permutation der vier Labels ist zudem nicht automatisch
eine konforme Automorphie der festgehaltenen quadratischen Punktkonfiguration.

Auch die relative Phase von S lässt sich innerhalb dieses endlichen Vertrags
bestimmen. Alle D4-Intertwiner haben die oben angegebene Form S(a,b), wobei
die erste Zeile (0,−2a,a) lautet. Die Isometrie erzwingt |a|=1 und
|b/a|²=1/2. Mit z=(1+i)/(2b/a) wird der zurücktransportierte Dreierzyklus

\[
 P(z)=\begin{pmatrix}0&-2z&z\\1&0&0\\2&z^{-1}&0\end{pmatrix}.
\]

Ganzzahligkeit auf dem bestehenden Z³-Gitter verlangt z und z⁻¹ ganzzahlig,
also z=±1. Damit ist b/a=±(1+i)/2. Die beiden Möglichkeiten sind
D4-konjugiert; es ist kein kontinuierlicher Phasenfit erforderlich.
Dies ist eine Auswahl im bestehenden endlichen Gittervertrag, keine
Herleitung einer physikalischen CP-brechenden Vakuumphase.

Der **unveränderte** Compiler wird durch Ähnlichkeit mitgeführt:

\[
 Q_c=SQS^{-1}=\begin{pmatrix}
 1&(3-3i)/2&(-3-3i)/2\\
 0&5/2-i&-2-i/2\\
 0&-2+i/2&5/2+i
 \end{pmatrix},\quad \Sigma_c=S\Sigma S^{-1}.
\]

Für jedes nichtkommutative Polynom p ist
p(Q_c,Σ_c,U,−B,M)=S p(Q,Σ,−G,−T,P) S⁻¹.
Dasselbe gilt für Q±=(Q±ΣQΣ)/2. Mit N wird das korrekte Adjungieren
transportiert: S(N⁻¹A†N)S⁻¹=(SAS⁻¹)†.
Hier wird **nicht** Q durch Λ²Q ersetzt; die Außenpotenz eines Operators
hätte andere Eigenwerte und wäre nicht diese gemeinsame Produktabbildung.
Q selbst ist weder N-unitär noch N-selbstadjungiert. Er bleibt ein
Compileroperator und wird nicht zu einer selbstadjungierten Observable erklärt.
Bei y=Sx gilt für einen bilinearen Vertex Y_y=S⁻ᵀY_xS⁻¹ und folglich
h_y=det(S⁻¹)S h_x=iS h_x. Das Volumenzeichen gehört zum Quellenwörterbuch.

**Herkunftsgrenze:** v117 beweist die Eigenschaften von M,U exakt. Seine
Identifikation mit der analytischen ODE-Monodromie ist weiterhin numerisch.
N ist die frühere endliche Gitterauswahl, nicht die bereits aus P1 abgeleitete
physische Kovarianz. Der Code-/G31-Dreierzyklus auf acht Bits wird hier nicht
zusätzlich mit M identifiziert.

## 2. Der vorhandene symmetrische E8-Kanal hat Platz für den Vertex

Der vorherige Quellenprodukt-Audit ergibt

\[
 \operatorname{Sym}^2(16\otimes4)
 =(10,10)\oplus(120,6)\oplus(126,10)
\]

mit Gramwerten 8,4,0 und Multiplizitäten 100,720,1260.
Der neue Checker beschränkt die tatsächlichen markierten Quellgewichte auf
eine koordinative Dreierfamilie. Er prüft alle 1176 symmetrischen Paare und
ihre vollständigen Gewichtscharaktere, nicht nur die Dimensionen:

\[
 \operatorname{Sym}^2(16\otimes3)
 =(10,6)\oplus(120,\bar3)\oplus(126,6),
\]

\[
 \operatorname{spec} G_{\rm sym}=8^{[60]}\oplus4^{[360]}\oplus0^{[756]}.
\]

Das Bild ist somit 420-dimensional. Der (10,6)-Kanal enthält alle sechs
symmetrischen Familienkoeffizienten. Der (120,bar3)-Kanal hat antisymmetrische
Spin- und Familienfaktoren, insgesamt ebenfalls symmetrischen Austausch.
Genau diesen Gesamt-Austauschtyp braucht ein lokaler Lorentzskalar aus zwei
linkshändigen 4D-Weyl-Feldern. Die Rechnung wählt solche Felder nicht aus.

Die Dreierunterraumwahl bleibt bedingt. SU4-Äquivarianz überträgt den Satz auf
andere Dreierunterräume, bestimmt aber keinen physischen. Cocycle-Spaltenphasen
sind im Gram-/Charaktertest unitarisch entfernt; die vollständige signierte
historische Operatorabbildung wird dadurch nicht erneut zertifiziert. Die
Zahlen 8 und 4 sind Gramnormen, keine Massen oder hergeleiteten Kopplungen.

## 3. Voller Rang ist exakt eine Bedingung an die Quelle und ihre Clock-Bahn

Für die Konvention

\[
 A(h)=\begin{pmatrix}0&h_3&-h_2\\-h_3&0&h_1\\h_2&-h_1&0\end{pmatrix},
 \qquad Y_C(h)=C^TA(h)-A(h)C
\]

gilt für **jede** komplexe 3×3-Matrix C

\[
 Y_C(h)^T=Y_C(h),\qquad
 \boxed{\det Y_C(h)=2\det[h,Ch,C^2h]}.
\]

Beweis: Für diagonales C ist dies die Vandermonde-Identität nach direkter
Einsetzung. Unter einer beliebigen invertierbaren Basisänderung F gilt
A'=FᵀAF, h'=det(F)F⁻¹h und C'=F⁻¹CF. Beide Determinanten skalieren mit
det(F)². Damit gilt die Identität für alle diagonalisierbaren C; ihre beiden
Seiten sind Polynome, also gilt sie durch Dichtheit für alle C.
Zusätzlich expandiert der Checker die Identität mit neun unabhängigen
C-Einträgen und drei h-Variablen vollständig.

Folglich kann dieser Vertex genau dann drei Massenrichtungen tragen, wenn
h,Ch,C²h linear unabhängig sind. Für eine unitäre Clock dritter Ordnung
mit einfachem Spektrum ist dies gleichbedeutend mit nichtverschwindender
Überlappung des Zustands mit allen drei Clock-Eigenlinien. In deren
orthonormaler Basis ist |det[h,Ch,C²h]|²=27|h₀h₁h₂|².

Der Ausdruck ist linear in h und verändert dessen Higgs-Ladungsgrad nicht.
Er führt die Clock aber aktiv relativ auf den beiden Beinen ein; eine
gemeinsame Basisänderung erzeugt ihn nicht. Dass die ursprüngliche Quelle
gerade diese Operation enthält, bleibt die zentrale physische Zusatzfrage.
Die Bedeutung des Volumenfaktors in h' darf beim eben konstruierten
Orientierungswörterbuch nicht weggelassen werden.

## 4. Die Viertelphasen allein brechen CP nicht

Für die originalen M,U gilt MᵀBM=UᵀBU=B. B ist symmetrisch und unitär;
J=B K mit komplexer Konjugation K ist eine Antiunitarität mit J²=I und
kommutiert mit beiden Clocks. Eine gemeinsame J-reelle orthonormale Basis
besteht aus e₁,(e₂−e₃)/√2,i(e₂+e₃)/√2. In ihr sind beide Clocks reell.

Falls Jh=h, gilt für jedes reell gewichtete Clockwort C

\[
 B^T\overline{Y_C(h)}B=-Y_C(h).
\]

Eine gemeinsame Phase i macht deshalb sämtliche solchen Yukawa-Matrizen
gleichzeitig CP-gerade. Insbesondere verschwinden alle CP-ungeraden
schwachen Basisinvarianten. Dies betrifft die Klasse mit demselben J-reellen
h, einem A(h)-Einsatz und reellen Koeffizienten; es ist kein allgemeines
TFPT-Verbot von CP-Verletzung.

## 5. Vollständige endliche Suche und ein bedingter CP-Kandidat

Untersucht wurden alle 24 C in ⟨M,U⟩ an den drei durch U markierten
Eigenlinien h=e₁,e₂,e₃: 72 Matrizen und je 276 ungeordnete Paare für den
Kommutatortest, insgesamt 828 Paarprüfungen. Keine Zielmassen oder
bevorzugten Energien gingen in die Suche ein.

| Markierte Linie | Rang 3 | Rang 2 | Nullmatrix | Paare mit CP-Invariante ≠0 |
|---|---:|---:|---:|---:|
| U=1, h=e₁ | 8 | 14 | 2 | 0 |
| U=i, h=e₂ | 12 | 11 | 1 | 48 |
| U=−i, h=e₃ | 12 | 11 | 1 | 48 |

Für e₁ ist die M-Bahn sogar orthonormal. Y_M hat aber die quadrierten
singulären Werte 1,1,4. Drei Nichtnullmassen bedeuten hier noch keine
aufgelöste Hierarchie.

Ein einfacher Parameter-freier **bedingter** Kandidat ist

\[
 h=e_2,\quad Y_u=Y_M(h),\quad Y_d=Y_{M^2}(h).
\]

Beide quadrierten Spektren besitzen das Polynom

\[
 p(x)=x^3-6x^2+9x-1,\quad\operatorname{disc}(p)=81.
\]

Mit H_f=Y_fY_f† gilt exakt

\[
 \det[H_u,H_d]=27i/4,\qquad |J_{\rm alg}|=1/24.
\]

Der zweite Wert ist die übliche normierte Dreifamilieninvariante:
|det[H_u,H_d]|/(2√disc(p_u)√disc(p_d)). Für h=e₃ kehrt sich das
Vorzeichen um. J bildet e₂ auf −e₃ ab; beide Zustandswahlen sind CP-konjugiert.
Die sektoralen Bezeichnungen u,d sind hier Testzuordnungen, keine aus der
Quelle abgeleiteten physikalischen Identifikationen. Unter einer **unitären**
gemeinsamen Familienbasisänderung bleibt die Kommutatordeterminante invariant;
bei allgemeinen Koordinatenänderungen muss die Metrik mitgeführt werden.

## 6. Der Hierarchietest schließt einen falschen Endpunkt aus

In der vollständig durchsuchten Klasse lauten die einzigen vollen
quadrierten Spektralpolynome

\[
 (x-4)(x-1)^2,\quad x^3-6x^2+9x-1,\quad
 (x-2)(x^2-4x+1).
\]

Das größte Verhältnis von größtem zu kleinstem singulärem Wert ist
numerisch 5,411474… (aus dem mittleren Polynom); exakt ist es kleiner als 6.
Eine gemeinsame Sektornormierung ändert dieses Verhältnis nicht.
Demgegenüber verlangt schon die bestehende TFPT-Leptonenleiter

\[
 \widehat m_\tau/\widehat m_e=
 \frac{49}{96}\phi_0^{-3}\simeq3395,29,
 \qquad\phi_0=\frac1{6\pi}+\frac3{256\pi^4}.
\]

**Damit kann kein einzelner Kandidat dieser diskreten Klasse allein die
vorhandene vollständige Massenleiter ersetzen.** Das widerlegt weder die
Compilerleiter noch allgemeine kombinierte Quellvertizes. Es beendet den
naheliegenden, aber falschen Versuch, die 24 Clockmatrizen bereits als fertige
Yukawas auszugeben. Ein genetischer Algorithmus würde diese endliche Klasse
nicht erweitern und könnte ihre fehlende Auswahlregel nicht herleiten.

## 7. Was als Nächstes tatsächlich zusammengeführt werden muss

Das gemeinsame Wörterbuch liefert jetzt die passende Stelle für einen
weiteren Quellenvergleich: originaler Q/Σ-Compiler, ursprüngliche Clocks,
Metrik, symmetrischer Produktkanal und mögliche CP-Orientierung können
ausdrücklich zusammen beschrieben werden. Diese finite Verbindung ersetzt
nicht die noch fehlende geladene Quellenfunktion.

Der nächste entscheidende Gegenstand ist ein aus dem Originalkern mit seinen
geladenen Einfügungen berechneter gemeinsamer Dreipunktvertex. In demselben
Wörterbuch muss er (a) seinen Clock-/Volumentyp, (b) seine Familien- und
Spin10-Ladungen, (c) seine Gramnorm und (d) die tatsächliche Zeitantwort
liefern. Erst daraus darf festgestellt werden, ob er eine relative
Clockoperation enthält und ob die vorhandenen Transportwörter die
λY^L-Unterdrückung an genau diesem Vertex erzeugen.

Ein nachträgliches Einsetzen dieser Unterdrückungsfaktoren in Y_C würde
Massenhierarchien konstruieren, aber die verlangte Herkunft nicht beweisen.
Ebenso wenig darf e₂ statt e₃ anhand der gewünschten CP-Zahl ausgesucht
werden. Ein berechneter Vertex, der nur in einem unpassenden Kanal liegt,
beendet diesen Kandidaten; dann ist der andere vorhandene symmetrische
(120,bar3)-Kanal zu prüfen, ohne den E8- oder Transfervertrag umzuschreiben.

Unabhängig davon bleiben die gemeinsame physische Quellen-/Zustandswahl,
geladene sektorwechselnde Felder, lokale chirale 3+1D-Dynamik sowie die
Rückbedingungen aus α, Gravitation und Kosmologie offen. Kein T1–T8-Gate
wird geschlossen, kein Ledgerstatus oder empirischer Claim hochgestuft.

## Originale und wissenschaftliche Einordnung

- `verification/v117_monodromy_weyl_a3.py`: exakte Clockmatrizen;
  numerische ODE-Identifikation bleibt numerisch.
- `source-flavor-joint-dictionary-20260921/PROOF.md`: tatsächlicher Q-Compiler,
  markiertes D4-Modul, Residuenwörterbuch und bedingte Metrikauswahl.
- `symmetric-source-product-audit-20260921`: vorhandener voller symmetrischer
  Quellenkanal und bereits bekannter relativer Clock-Ausdruck.
- `tfpt_2_standard_model.tex`, Massen-Masterformel und Leptonenverhältnisse:
  bereits vorhandene TFPT-Hierarchie, die zu erhalten ist.
- [Dreiner, Haber, Martin: Two-component spinor techniques](https://arxiv.org/abs/0812.1594):
  Lorentz-/Grassmann-Austauschregel; kein Beleg für ihre TFPT-Herkunft.
- [Babu, Bajc, Saad: Yukawa Sector of Minimal SO(10) Unification](https://arxiv.org/abs/1612.04329):
  Einordnung der 10/120/126-Tensorkanäle. Deren phänomenologisches Modell
  wird hier nicht als zusätzliche TFPT-Theorie übernommen.
- [Jarlskog: Commutator of the Quark Mass Matrices](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.1039):
  basisunabhängiger CP-Test; die hier eingesetzten Matrizen und Werte
  werden separat exakt nachgerechnet.
