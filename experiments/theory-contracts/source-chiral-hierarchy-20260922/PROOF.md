# Chirale Hierarchie aus der ursprünglichen Quelle

22. September 2026 · `UR.SOURCE.CHIRAL_HIERARCHY.01` · **PARTIAL**

## Auftrag und Ergebnis

Verlangt ist die vollständige Herkunftsherleitung des im Nutzertext genannten
chiralen Antwortoperators, einschließlich der Leptonordnungen 2, 3, 5,
der Koeffizienten 7/6, 4/3, 16/7 und des gemeinsamen Zustands-, Zeit- und
Holonomiewörterbuchs. Eine eingesetzte Zielmatrix oder eine neu gewählte
Zwischenkette wäre keine Erfüllung dieses Auftrags.

**Diese vollständige Lösung ist nicht erbracht.** Die vorliegende Arbeit
entscheidet aber einen tatsächlichen vorhandenen Kandidaten wesentlich
stärker als die bisherige endliche Suche: Ein einzelner normaler
Clock-Vertex kann die verlangte Hierarchie für **keinen** komplexen
Quellenvektor erzeugen. Das gilt auch für analytisch variierende unitäre
Clocks und Quellenvektoren sowie nach jeder bei u=0 regulären kinetischen
Normierung. Die Quelle muss einen darüber hinausgehenden Beitrag liefern.

Außerdem werden die nichtlinearen Operatoren und der Z=16-Rest des nativen
Modells eingeordnet und die verlangten Hierarchieordnungen in einen
notwendigen und hinreichenden Test an den ersten fünf Vertexordnungen
übersetzt. Dieser Test berechnet den fehlenden Vertex nicht selbst.

Vor der Rechnung festgelegtes Erfolgskriterium: ein aus den unveränderten
Quelloperatoren berechneter Vertex mit den Zielordnungen und Koeffizienten.
Abbruchkriterium für eine konkrete Kandidatenklasse: ein allgemeines
algebraisches Hindernis, das weitere Parameter- oder Zustandssuche darin
wirkungslos macht. Die neue Entscheidung betrifft genau eine solche Klasse.

## 1. Geprüfter Ausgangspunkt

Die Originalformel aus `tfpt_2_standard_model.tex:311–351` und
`FLAV.LEPTONC.01` lautet, nach Abtrennung des gemeinsamen Maßstabs:

\[
 (y_\tau,y_\mu,y_e)=
 \left(\frac76u^2,\frac43u^3,\frac{16}{7}u^5\right),\qquad
 u=\varphi_0=\frac1{6\pi}+\frac3{256\pi^4}.
\]

Die Koeffizienten sind im bestehenden Compiler über den Hexagonresolventen
und die Produktregel abgeleitet. Diese Resultate werden weder neu beansprucht
noch durch den folgenden Kandidatenausschluss widerlegt. Offen ist der
Anschluss an dieselbe physische geladene Quelle und an Polmassen.

Der bestehende Contract `source-native-clock-flavor-bridge-20260922`
untersucht den symmetrischen Vertex

\[
 A(h)=\begin{pmatrix}0&h_3&-h_2\\-h_3&0&h_1\\h_2&-h_1&0\end{pmatrix},
 \qquad Y_C(h)=C^T A(h)-A(h)C.
\]

Er beweist die Zyklizitätsidentität
\(\det Y_C=2\det[h,Ch,C^2h]\) für beliebiges C und findet bedingte
Vollrang- und CP-Beispiele. Seine Hierarchiesuche umfasst die 24 originalen
Clocks an drei markierten Linien. Die folgenden Sätze erweitern diesen
konkreten Test auf alle h; sie setzen keine neue Dynamik ein.

Die originalen M/U-Matrizen werden im Checker aus den symbolischen
Deklarationen `M0_EXACT` und `U_EXACT` von
`verification/v117_monodromy_weyl_a3.py` gelesen. Die endliche Algebra ist
exakt. Die ursprüngliche ODE-Identifikation bleibt davon getrennt.

## 2. Allgemeiner Clock-Satz

**Satz.** Sei C eine normale komplexe 3×3-Matrix in einem orthonormalen
Familienrahmen und A eine beliebige komplexe antisymmetrische 3×3-Matrix.
Für die absteigend geordneten Singularwerte von \(Y=C^TA-AC\) gilt

\[
 \boxed{\sigma_1=\sigma_2+\sigma_3.}
 \tag{1}
\]

Insbesondere gilt \(1\le\sigma_1/\sigma_2\le2\), solange Y nicht null ist.
Normale C umfassen sämtliche unitären Clockwörter, unabhängig von ihrer
Ordnung. Die Aussage setzt kein reelles h voraus.

**Beweis.** Schreibe \(C=V D V^\dagger\) mit unitärem V und diagonalem D.
Unter der unitären Kongruenz entstehen

\[
 V^TYV=D(V^TAV)-(V^TAV)D.
\]

Die rechte Seite ist symmetrisch und hat eine verschwindende Diagonale.
Ihre Singularwerte sind dieselben wie diejenigen von Y. Eine allgemeine
solche Matrix ist

\[
 B=\begin{pmatrix}0&a&b\\a&0&c\\b&c&0\end{pmatrix}.
\]

Mit einer diagonalen unitären Kongruenz können alle drei nichtverschwindenden
Einträge a,b,c gleichzeitig reell und nichtnegativ gemacht werden: Die drei
Gleichungen für die Summen der Diagonalphasen sind lösbar. Bei verschwindenden
Einträgen sind entsprechend weniger Gleichungen zu erfüllen.

Für abc>0 ist B reell symmetrisch, \(\operatorname{tr}B=0\) und
\(\det B=2abc>0\). Seine Eigenwerte haben somit die Form p,−q,−r mit
p,q,r>0 und p=q+r. Die Singularwerte sind p,q,r. Für abc=0 folgt die Aussage
durch Stetigkeit; für eine nichtverschwindende Matrix sind die beiden
nichtverschwindenden Werte dann gleich. Damit ist (1) bewiesen.

Ein unabhängiger algebraischer Kontrollweg ist

\[
 2\operatorname{tr}[(B^\dagger B)^2]
 -[\operatorname{tr}(B^\dagger B)]^2=0.
\]

Mit \(x\ge y\ge z\ge0\) faktorisiert die äquivalente Gleichung als
\((x+y+z)(-x+y+z)(x-y+z)(x+y-z)=0\), also wiederum x=y+z.
Der Checker expandiert diese Identität für sechs unabhängige reelle
Komponenten der drei komplexen Einträge, nicht nur für Stichproben.

Die Null-Diagonal-Struktur ist aus der mathematischen Literatur bekannt;
die Anwendung auf die tatsächliche TFPT-Clockklasse ist der hier ergänzte
Schritt. Siehe R. C. Thompson, *Singular values and diagonal elements of
complex symmetric matrices*, Linear Algebra Appl. 26 (1979), 65–106,
doi:10.1016/0024-3795(79)90173-3. Der Beweis oben ist selbstständig.

## 3. Warum reguläre Normierung diesen Ausschluss nicht aufhebt

Sei \(Y(u)=C(u)^TA(h(u))-A(h(u))C(u)\) analytisch und C(u) normal für
reelle u nahe null. Punktweise folgt aus (1)

\[
 \sigma_2(u)\le\sigma_1(u)\le2\sigma_2(u).
\]

Die beiden größten Singularwerte haben daher dieselbe führende Potenzordnung.
Die Ordnung des dritten kann größer sein oder der dritte Wert identisch null.
Definiere v_k als die kleinste u-Verschwindungsordnung unter allen
k×k-Minoren von Y. Das ist die Summe der ersten k Singularwertordnungen.
Für diese Determinantenbewertungen bedeutet dies

\[
 \boxed{v_2(Y)=2v_1(Y)}
 \tag{2}
\]

bei einem nicht identisch verschwindenden analytischen Vertex. Die
Zielformel verlangt dagegen \(v_1=2,v_2=5,v_3=10\), also 5≠2·2.

Sind \(Z_L(0),Z_R(0)>0\), sind ihre inversen Quadratwurzeln und deren
Inverse in einer Umgebung von null gleichmäßig beschränkt. Reguläre
Links-/Rechtsmultiplikation ändert keine Singularwertordnungen. Alternativ
folgt dies exakt aus Cauchy–Binet für die Minorideale und den inversen
Transformationen. Auch ein regulärer, nichtverschwindender gemeinsamer
Higgsfaktor ändert keine Ordnungsdifferenzen.

Somit kann \(Z_L^{-1/2}Y Z_R^{-1/2}\) keine Ordnungen (2,3,5) haben.
Die Aussage verlangt, dass tatsächlich eine von der Quelle begründete
analytische u-Familie vorliegt. Der einzelne Zahlenwert φ₀ definiert sie nicht.
Die allgemeine Beziehung zwischen lokalen Smith-Invarianten und
Singularwertordnungen ist etabliert, siehe
[Kaveh–Makhnatch, arXiv:1811.07706](https://arxiv.org/abs/1811.07706).

**Endlicher Wert und asymptotische Ordnung sind verschieden.** An u=φ₀
liefert das vorhandene Ziel

\[
 \frac{y_\mu+y_e}{y_\tau}=0.06106247089073437\ldots,
\]

während ein nackter normaler Clock-Vertex exakt 1 verlangt. Eine frei gewählte
stark anisotrope, aber bei null reguläre Kinetik könnte einzelne Zahlen bei
einem festen u verändern. Dies ist kein allgemeiner Ausschluss jedes
solchen endlichen Fits. Notwendig für den Zielwert von \(y_\tau/y_\mu\)
wäre mindestens

\[
 \sqrt{\kappa(Z_L)\kappa(Z_R)}\ge
 \frac{y_\tau}{2y_\mu}=8.2280221449254\ldots.
\]

Die Schranke folgt aus den oberen/unteren Singularwertschranken für P Y Q.
Solche kinetischen Daten und ihre Herkunft wären eigenständig zu berechnen.
Im symmetrischen nativen Familienblock sind sie skalar. Die asymptotische
Unmöglichkeit (2) besteht bei jeder regulären Kinetik unverändert.

**Weitere feste Compileroperatoren.** Ist C lediglich diagonalisierbar und
u-unabhängig, bringt eine konstante invertierbare Kongruenz Y ebenfalls in
eine symmetrische Null-Diagonal-Form. Die Dreiecksidentität muss dann nicht
für die physisch normierten Singularwerte gelten. Aber jede erste
nichtverschwindende Taylor-Matrix hat Rang mindestens zwei: Eine symmetrische
Rang-eins-Matrix \(vv^T\) mit Nulldiagonale wäre null. Daher bleibt auch hier
\(\alpha_1=\alpha_2\). Die tatsächlichen Q,Q₊,Q₋ aus dem vorhandenen
Clock-Wörterbuch haben einfache Spektren; ihre charakteristischen
Diskriminanten sind 13,4,108. Ein bloßer Austausch der festen Clock durch
einen dieser drei Operatoren löst das Problem folglich ebenfalls nicht.

## 4. Grenzen des Satzes: eine wirkliche weiter erlaubte Klasse

Es wäre falsch, (1) auf jede Summe aus mehreren Clock-Vertizes oder jede
nichtnormale dynamische Matrix zu übertragen. Als reine Gegenprobe dieser
zu starken Aussage setze h=(0,0,1) und

\[
 C(u)=\begin{pmatrix}0&u^3/2&u^4\\-u^2/2&0&0\\0&0&0\end{pmatrix}.
\]

Dann ist exakt

\[
 Y_C(h)=\begin{pmatrix}u^2&0&0\\0&u^3&u^4\\0&u^4&0\end{pmatrix},
 \qquad(v_1,v_2,v_3)=(2,5,10).
\]

C(u) ist nicht normal. Dieses Beispiel ist ausschließlich eine
Geltungsbereichskontrolle: Es zeigt, dass der bewiesene Ausschluss keine
allgemeine mathematische Unmöglichkeit der Zielhierarchie ist. Weder die
Potenzen noch C sind hier aus TFPT abgeleitet. Es wird deshalb ausdrücklich
kein neues physisches Modell vorgeschlagen und kein Lösungsfortschritt durch
das Einsetzen der gewünschten Potenzen behauptet.

Der vorhandene symmetrische Quellenproduktkanal
\(\operatorname{Sym}^2(16\otimes3)\) besitzt weiterhin das geprüfte Bild
\((10,6)\oplus(120,\bar3)\) mit Dimension 420. Darin sind insbesondere die
sechs symmetrischen Familienkoeffizienten algebraisch vorhanden. Ein
tatsächlich ausgewählter Quellenvertex muss nicht in der ausgeschlossenen
einzelnen Clockklasse liegen. Der nichtverschwindende physische Dreipunkt-
beziehungsweise 1PI-Vertex und seine Auswahl sind dadurch aber nicht gegeben.

## 5. Nichtlineare Felder und die zustandserhaltende Restwirkung

Der native Hamiltonoperator und sein eindeutiger Grundzustand im bewiesenen
Bereich \(0<|g|/\Delta\le1/20\) sind Spin(10)×SU(4)-invariant.
Das bereits bekannte Schur-Argument für die ursprünglichen f-Felder lässt
sich präzise auf zusammengesetzte Felder erweitern.

Sei der Raum der gewählten geladenen Operatoren eine unitäre G-Darstellung

\[
 \mathcal O=\bigoplus_\lambda V_\lambda\otimes\mathcal M_\lambda.
\]

Für \(C_{ab}(t)=\langle\Omega|O_a^\dagger F_t(H)O_b|\Omega\rangle\)
und wohldefinierte Operatoren auf dem betrachteten Zustand gilt

\[
 \boxed{C(t)=\bigoplus_\lambda
 I_{V_\lambda}\otimes K_\lambda(t).}
\]

Dies folgt aus Invarianz und Schurs Lemma auf jedem isotypischen Block.
Bei Nullnormen wird zunächst auf dem positiven Träger der Gramform
quotientiert. Beliebig viele verschiedene Pole sind in Kλ möglich.
Sie unterscheiden Darstellungen oder deren Mehrfachvorkommen, nicht die
drei Komponenten eines einzelnen irreduziblen Familientripletts.

Eine Zuordnung dreier solcher unterschiedlichen Operatoren zu den drei
Leptonfamilien könnte prinzipiell weiterführen. Sie braucht aber genau die
aus der Quelle abgeleitete Ladungs-, Produkt-, Zustands-, Zeit- und
Holonomieabbildung. Die Bezeichnung dreier ausgewählter Operatoren als
e,μ,τ liefert diese Abbildung nicht.

Auch der im Nutzertext genannte Z=16-Sektor wurde am Original geprüft:
`rr-three-family-state-20260921/HERLEITUNG.md` beschreibt die exakte
Hilfsraumzerlegung und die nichtverschwindende gemischte Kopplung.
Nach Wahl der vierten Familienlinie verbleibt ihre SU(3)-Stabilisatorwirkung
auf dem Dreierunterraum. Der ursprüngliche Zustand bleibt invariant.
Eine exakte zustandserhaltende Eliminierung ist daher SU(3)-äquivariant,
und ihre Tripletantwort bleibt skalar in den Familienkomponenten.
Die Rückwirkung und ihre Zeitabhängigkeit verschwinden nicht; sie liefern
unter diesen Voraussetzungen aber keine Aufspaltung dieses Tripletts.

Nichtinvariante Zustände, aktive nichtskalare Randquellen und begründete
andere Operatorzuordnungen liegen außerhalb dieses Ausschlusses. Sie
benötigen eine Herkunftsherleitung. Außerhalb des bewiesenen schwachen
Kopplungsbereichs wird keine beliebige reine Grundzustandsbranche als
invariant vorausgesetzt.

## 6. Vollständiger lokaler Test für die Ordnungen 2,3,5

Der positive Bewertungssatz aus dem Nutzertext ist korrekt. Er lässt sich
zu einem notwendigen und hinreichenden Test für diese drei führenden
Ordnungen ausarbeiten. Dies ist ein Test für einen **gegebenen** aus der
Quelle berechneten Vertex, keine Herleitung dieses Vertizes.

Arbeite mit dem analytischen kanonischen Vertex \(\widehat Y(u)\).
Er muss zunächst \(\widehat Y_0=\widehat Y_1=0\) und
\(\operatorname{rank}\widehat Y_2=1\) erfüllen. Bringe seinen führenden
Koeffizienten durch konstante unitäre Links-/Rechtsrotation in die Form
diag(a,0,0), a>0. Schreibe

\[
 \widehat Y/u^2=\begin{pmatrix}a(u)&r(u)\\c(u)&D(u)\end{pmatrix},
\]

mit a(0)=a, r(0)=c(0)=D(0)=0. Alle Größen sind analytisch. Definiere

\[
 R(u)=D(u)-c(u)a(u)^{-1}r(u)
     =uR_1+u^2R_2+u^3R_3+O(u^4).
\]

Mit r=ur₁+u²r₂+…, c=uc₁+u²c₂+…, D=uD₁+u²D₂+u³D₃+… gilt

\[
 R_1=D_1,\qquad R_2=D_2-c_1r_1/a,
\]
\[
 R_3=D_3-(c_1r_2+c_2r_1)/a+a_1c_1r_1/a^2.
\]

Jetzt ist \(\operatorname{rank}R_1=1\) notwendig. Bringe R₁ im
verbleibenden Zweierraum durch unabhängige konstante unitäre Links- und
Rechtsrotationen in diag(b,0), b>0,
und bezeichne die mitrotierten R₂,R₃ weiterhin so. Der letzte
Schurkomplement-Skalar ist

\[
 s(u)=u^2(R_2)_{22}
 +u^3\left((R_3)_{22}
      -\frac{(R_2)_{21}(R_2)_{12}}b\right)+O(u^4).
\]

Zusammen mit den vorangehenden Bedingungen
\(\widehat Y_0=\widehat Y_1=0\), \(\operatorname{rank}\widehat Y_2=1\)
und \(\operatorname{rank}R_1=1\) lautet die noch fehlende Bedingung exakt

\[
 \boxed{(R_2)_{22}=0,\qquad
 \gamma=(R_3)_{22}-(R_2)_{21}(R_2)_{12}/b\ne0.}
 \tag{3}
\]

**Notwendigkeit und Hinreichendheit.** Die beiden Schur-Eliminationen sind
reguläre Links-/Rechtstransformationen. Ihre nichtkonstanten Mischfaktoren
gehen für u→0 gegen die Identität. Die pivots sind a+O(u),
u(b+O(u)) und u³(γ+O(u)). Einschließlich des gemeinsamen u² folgen

\[
 \sigma_1=a|u|^2(1+O(|u|)),\quad
 \sigma_2=b|u|^3(1+O(|u|)),\quad
 \sigma_3=|\gamma||u|^5(1+O(|u|)).
\]

Umgekehrt erzwingen diese Ordnungen zuerst Rang eins des ersten
Koeffizienten, dann Rang eins von R₁, das Verschwinden des u²-Terms in s
und das Nichtverschwinden des u³-Terms. Damit ist (3) äquivalent zum
gewünschten lokalen Rangverlauf. Ein vorzeitiger \((R_2)_{22}\ne0\)
ergäbe (2,3,4); γ=0 verschöbe die letzte Ordnung weiter nach hinten.

Für die **führenden** Vorfaktoren der TFPT-Formel muss die Quelle außerdem
a=7/6, b=4/3 und |γ|=16/7 liefern, nach korrekter Higgsnormierung und
Abtrennung des gemeinsamen Maßstabs. Die volle Formel bei u=φ₀ benötigt
zusätzlich die höheren Koeffizienten oder eine kontrollierte Restabschätzung.
Der Fünf-Ordnungen-Test allein bestimmt weder endliche Polmassen noch die
physische Chiralität oder die CP-Orientierung.

## 7. Die verbleibende erste Herleitung

Die zentrale unbekannte Größe ist weiterhin die geladene Quellwirkung auf
einem gemeinsamen Raum mit begründeten physischen Feldern, Zustand und Zeit.
Ohne sie sind weder die Einfügungsableitung nach dem Higgsfeld noch die
zulässige analytische u-Variation bestimmt. Die exakte Schurformel
\(A-BE^{-1}C\) kann diese Daten weiterverarbeiten, aber nicht auswählen.

Die vorhandenen Originalaudits `source-variation-origin-gate-20260922`
und `source-native-retarded-selection-20260922` haben den behaupteten
Variationsabschluss geprüft: Die archivierte Master-Barriere setzt die
minimale Operatorfaser bereits voraus. Eine wohlfundierte Auswahl eines
minimalen Defektvektors beweist nicht die Eindeutigkeit dieser ganzen Faser.
Die Originalpassagen wurden auch in dieser Arbeit erneut direkt gelesen:
`_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:543–682`
und `02_carrier_source.tex:3020–3095`. Dies ist die dokumentierte offene
Herkunftsstelle, kein aus erfolgloser Dateisuche abgeleiteter allgemeiner
Unmöglichkeitsbeweis.

Der begründete weitere Ansatz ist deshalb der schon vorhandene symmetrische
geladene Quellenkanal. Benötigt werden seine tatsächlich erzeugten
Koeffizienten \(\widehat Y_2,\ldots,\widehat Y_5\) und die Quelle ihrer
erzwungenen Nullstellen in (3). Eine Summe mehrerer Beiträge kann den
Clock-Ausschluss umgehen; die relativen Gewichte, die Unterdrückungsordnungen
und die Feldabbildung dürfen dafür nicht aus den Zielmassen eingesetzt werden.

Die zugänglichen und hier benannten Quellen liefern diese gemeinsame
Herleitung nicht. Auch diese Arbeit liefert sie nicht. Deshalb bleiben
T1–T8 und der Auftrag einer vollständigen physischen Lösung offen.

## 8. Reproduzierbarkeit, Neuheit und Reichweite

`checker.py` prüft 35 endliche algebraische Aussagen, darunter:
symbolische Null-Diagonal-Identität für allgemeine komplexe Einträge;
dieselbe Identität an den originalen M/U-Wörtern für allgemeines h;
Minorbewertungen; exakte Schurkoeffizienten; Gegenproben mit vorzeitiger
und fehlender dritter Richtung sowie einer wirklich nichtnormalen Matrix.
Die mathematischen Allgemeinaussagen sind oben bewiesen. Die Zahl der
Kontrollen ist kein Maß für physische Vollständigkeit.

Die Kontrollmatrizen mit eingesetzten Potenzen sind ausschließlich
Testeingaben. Auch die zwei im Checker aus dem markierten A_or gebildeten
Endomorphismen zeigen nur, dass Kovarianz allein keine Potenzordnung wählt;
sie sind keine konstruierten physischen Yukawa-Abbildungen und keine
Gegenmodelle gegen alle P1/P2-Bedingungen.

Die im Nutzertext angegebene Energielücke
15|g|²/Δ−435|g|⁴/Δ³ wurde hier **nicht neu am vollständigen W-Tensor
reproduziert**. Sie wurde nicht benötigt, um den Clock-Satz zu beweisen,
und wird nicht zu drei Familienmassen umgedeutet.

Bereits bekannt: native Schur-Entartung der linearen Felder; konstante
Filternormierung; der parallele Holonomieausschluss; die endliche Clocksuche;
die Compiler-Leptonformel; Minorinvarianz und lokale Smith-Theorie.

Hier ergänzt: allgemeiner Clock-Ausschluss für alle komplexen h, sein
normierungsfester Ordnungswiderspruch, der feste diagonalisierbare
Compilerfall, explizite Abgrenzung durch eine nichtnormale Gegenprobe,
die gemeinsame Anwendung auf nichtlineare Multiplikitätskanäle und Z=16
sowie der vollständige lokale Zweischritt-Test (3).

Eine getrennte mathematische Agentenprüfung hat den allgemeinen Clockbeweis
und die native SU(3)-/Multiplizitätsgrenze geprüft. Das ist kein externes
Peer Review und keine Prüfung einer vollständigen Quantenfeldtheorie.

Quellenhashes und Checkerhash stehen im Zertifikat. Die Ergebnisse bleiben
im Experimentbereich; keine Paper-, Ledger-, Scorecard- oder physische
Gate-Promotion. Die bestehenden Flavorergebnisse bleiben in ihrem
jeweiligen Compilervertrag erhalten.
