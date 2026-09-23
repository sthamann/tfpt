# Zur kleinen gemeinsamen Regel: Compilerprozesse vor ihren Schatten

Forschungsnotiz v1.0, 14. September 2026. NON-RH. Keine TOE-Promotion.

## Ergebnis

Ein kleiner, direkt an den vorhandenen Compiler angeschlossener Kandidat ist
jetzt ausgeschrieben und exakt geprüft: **Operationen geordnet verknüpfen,
ihre vollständigen komplexen Überlappungen erhalten und erst danach auslesen.**
Unter einer ausdrücklich benannten Schnittunabhängigkeit geschlossener
Prozesse ist deren skalare Bewertung eindeutig.

Der stärkste anschauliche Zeuge besteht aus drei ursprünglichen
Compilerzuständen: Alle drei paarweisen Übergangswahrscheinlichkeiten sind
identisch, aber die orientierte Dreieramplitude unterscheidet sich.
Zweierwahrscheinlichkeiten können die Richtungsinformation verbergen, die
im geordneten Prozess erhalten bleibt.

Das benötigt kein größeres Zellmodell und keinen neuen Hamiltonoperator.
**Nicht bewiesen ist, dass diese algebraische Regel bereits die physische
P1-Randquelle ist oder deren Zeitentwicklung auswählt.** Die kleinen
Gegenkontrollen verhindern genau diese voreilige Identifikation.

## 1. Die ursprünglichen Reflexionen bestimmen einen positiven Kern

Alle 60 Strahlen werden aus dem ursprünglichen Gaussian-E8-Chart rekonstruiert.
Für einen normierten Strahl gilt

\[
P_r=|r\rangle\langle r|,\quad R_r=I-2P_r,\quad P_r=(I-R_r)/2.
\]

Die vorhandenen Reflexionen bestimmen daher die Projektoren als Elemente ihrer
komplexen Algebra. Die Projektoren spannen M4(C). Ihre algebraische Existenz
beweist noch keine physische Ausführbarkeit kohärenter Linearkombinationen.

Für Wörter w,v ist der operatorwertige Kern

\[
\boxed{\mathcal K(w,v)=W(w)^\dagger W(v).}
\]

Er ist positiv: Für jede Wortliste ist [W_i†W_j] die Gram-Matrix
[W_1 ... W_n]†[W_1 ... W_n]. Dafür wird kein skalarer Anfangszustand gewählt.
Die Operationsvorzeichen bleiben in der geordneten Multiplikation erhalten.

Das ist bekannte Operatoralgebra, keine neue mathematische Klasse. Der
konkrete Beitrag ist ihr exakter Anschluss an die unveränderten TFPT-Quellen
und die Trennung der dadurch geschlossenen und weiterhin offenen Aussagen.

## 2. Schnittunabhängigkeit fixiert die geschlossene Bewertung

Fordere auf der schon bestimmten Algebra eine komplex-lineare Bewertung tau
mit tau(I)=1 und tau(ab)=tau(ba). Die letzte Bedingung lässt sich als
Unabhängigkeit davon lesen, wo ein geschlossener Prozess zum Aufschreiben
aufgeschnitten wird. Sie ist ein **benannter Konsistenzvertrag**, noch kein
aus der physischen P1-Naht bewiesenes Gesetz.

Aus [Eii,Eij]=Eij folgt tau(Eij)=0 für i≠j. Aus
[Eij,Eji]=Eii−Ejj folgen gleiche Diagonalgewichte. Also eindeutig

\[
\tau(A)=\tfrac14\operatorname{Tr}(A),\qquad
k(w,v)=\tfrac14\operatorname{Tr}(W(w)^\dagger W(v)).
\]

Positivität und Treue folgen. Ein frei anpassbarer Gramkern entfällt auf dieser
Algebra. Dasselbe Ergebnis folgt für einen normierten Zustand unter voller
Invarianz der tatsächlichen irreduziblen Reflexionsgruppe.

Der zugehörige GNS-Raum ist der 16-dimensionale Operatorraum M4(C), **kein
zusätzlich postulierter physischer 16-Zustands-Träger**. Treue gilt auf
Matrizen, nicht auf verschiedenen Wortbeschreibungen derselben Matrix.

### Ein vollständiger Rekonstruktionssatz

Zwei gleichdimensionale irreduzible unitäre Darstellungen desselben markierten
*-Wortalphabets sind unitär äquivalent, wenn ihre normierten komplexen Spuren
für **alle** Wörter einschließlich gemischter Adjunktenwörter übereinstimmen.

Beweis: Alle Wortspuren bestimmen tau(A†A) jeder endlichen Linearkombination.
Treue erkennt genau die Nullkombinationen. Die Wortabbildung ist daher
wohldefiniert und bijektiv und erhält Multiplikation, Adjungierung und Spur.
Der so entstehende *-Isomorphismus voller gleicher Matrixalgebren ist durch
eine gemeinsame Unitary implementiert.

Die Quantoren sind wichtig: komplexe Amplituden aller Wörter, nicht nur
Beträge, Wahrscheinlichkeiten oder drei numerische Momente. Hieraus folgt
kein effizienter allgemeiner Rekonstruktionsalgorithmus.

## 3. Ein ursprüngliches Dreieck trägt die fehlende Orientierung

Im tatsächlichen C4-Chart liegen

\[
|0\rangle=(1,0,0,0),\quad |+\rangle=(1,0,1,0)/\sqrt2,\quad
|+i\rangle=(1,0,i,0)/\sqrt2,\quad |-i\rangle=\overline{|+i\rangle}.
\]

Alle drei paarweisen Born-Überlappungen des Dreiecks 0,+,+i sind 1/2.
Komplexe Konjugation lässt sogar die gesamte paarweise Projektor-Gram-Matrix
aller 60 Strahlen unverändert. Für die **gewöhnliche Spur** gilt dagegen

\[
\operatorname{Tr}(P_0P_+P_{+i})=(1+i)/4,\qquad
\operatorname{Tr}(P_0P_{+i}P_+)=(1-i)/4.
\]

Für tau=Tr/4 sind die Werte (1±i)/16; die Normierungen dürfen nicht vermischt
werden. Die Phasen bleiben ±pi/4. Diese komplexen Amplituden sind nicht schon
Wahrscheinlichkeiten gewöhnlicher sequenzieller Projektivmessungen: Ihre
Auslese verlangt einen kohärenten Interferenzvertrag.

Mit P_n=(I+n·sigma)/2 im kleinen Zweierblock folgt exakt

\[
\operatorname{Tr}(P_aP_bP_c)=
\frac{1+a\cdot b+b\cdot c+c\cdot a+i\,a\cdot(b\times c)}4.
\]

Dieselbe Multiplikation enthält paarweise Geometrie und Orientierung.
Daneben ist det(tI+x sigma_x+y sigma_y+z sigma_z)=t²−x²−y²−z².
Der hier gewählte Zweierblock ist nicht dadurch schon mit dem früheren
reellen Anker-Kommutanten identifiziert; dessen markierter Anschluss bleibt
mitzuführen.

Die Verbindung solcher Amplituden zu geometrischen Phasen ist bekannte
Bargmann-/Pancharatnam-Mathematik:
[Mukunda et al., 2003](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.67.042114).
Der TFPT-Befund ist der konkrete Zeuge aus den ursprünglichen Strahlen.

### Stärker: Zwei echte Reflexionswörter sind intern unterscheidbar

Der Anschluss bleibt nicht auf formal addierte Projektoroperationen beschränkt.
Setze R_j=I−2P_j für die drei obigen ursprünglichen Reflexionen. Dann gilt exakt

\[
W=R_0R_+R_{+i}=\operatorname{diag}(-i,1,-i,1),\qquad
W'=R_0R_{+i}R_+=\operatorname{diag}(i,1,i,1).
\]

Hier wirkt der rechte Faktor zuerst. Die beiden zeitlichen Folgen sind also
R_+i → R_+ → R_0 beziehungsweise R_+ → R_+i → R_0.
Die internen Bezugsstrahlen

\[
|\psi\rangle=(1,1,0,0)/\sqrt2,\qquad
|\phi\rangle=(1,i,0,0)/\sqrt2
\]

gehören ebenfalls zu den ursprünglichen 60 Strahlen. Für dieselbe Präparation
psi und dieselbe Auslese phi gilt

\[
\boxed{|\langle\phi|W|\psi\rangle|^2=1,\qquad
|\langle\phi|W'|\psi\rangle|^2=0.}
\]

Die beiden Abläufe verwenden die gleichen drei Reflexionen jeweils einmal.
Der Unterschied liegt ausschließlich in der Reihenfolge. Ein bereits im
originalen C4 vorhandener Querblock-Bezug genügt; für diesen mathematischen
Zeugen braucht es kein zusätzlich postuliertes Referenzregister und keine
kohärente Summe verschiedener Operationen.

Das ist eine Aussage über die Vorhersagen zweier konkreter Quellwörter,
**gegeben** den Zugang zu dieser Präparation und Messung. Deren physische
Implementierung wird damit nicht hergeleitet. Eine globale zentrale Phase
iI4 bleibt unsichtbar. Wer das gesamte Experiment einschließlich Gates,
Präparation und Auslese komplex konjugiert, erhält wieder dieselben Bornwerte.
Der Zeuge wählt daher keine absolute komplexe Orientierung und beweist weder
physische Chiralität noch eine Zwölferuhr.

## 4. Die korrekte Uhrenbrücke ist eine Dualität, keine Gleichsetzung

Die Quellen benutzen dieselbe Gitterpermutation PI_SIG. Sie fixiert drei
nichttriviale Quotientenklassen. Im Gaussian-C4-Chart fixiert ihre Konjugation
keinen nichttrivialen Paulioperator, aber drei Pauli-Kontexte.
Die tatsächliche Klassen-zu-Kontext-Bijektion ist an allen 240 Wurzeln erneut
geprüft und äquivariant.

Der abstrakte Wortlift realisiert die Familienbitdrehung auf einer anderen
C4-Darstellung. Die beiden Implementierer besitzen |Tr sigma|=1 bzw.2 und
lassen sich nicht durch unitären oder antiunitären Basiswechsel, skalare
Deckphase oder Inversion gleichsetzen.

Das ist **kein Fehler in v774 oder v783**. Die Originalquelle nennt
Punkt-Linien-Dualität und äußeren S6-Twist ausdrücklich. Eine gemeinsame Regel
darf unterschiedliche Darstellungen besitzen; ihre korrekte Brücke verläuft
hier über Klassen und Kontexte, nicht über identifizierte Einzelvektoren.

Belege: [Uhren- und Kernaudit](redteam/RESULTS.md).

## 5. Der einfache Polarzerfall von B/7 bleibt typgebunden

Auf den 15 Kontextlabels gilt B²=4I+3J. Mit P0=J/15 und Q=I−P0 ist

\[
S=B/2-J/6,\quad S^2=I,\qquad
K=B/7=S\big(P_0+(2/7)Q\big).
\]

Das ist eine exakte Vorzeichen-/Kontraktionszerlegung. S hat negative
Einträge und ist kein Markovschritt. Im tatsächlichen 60-Strahlen-Lift
verschwindet das nichttriviale Kontextvorzeichen beim Decode in die
Materiedichtematrix. Der materielle Kontrast ist 3/7, nicht 2/7.
Auch der Betrag des 60-Strahlen-Operators besitzt negative Einträge
(Minimum −1/42): Operatorpositivität ist nicht Eintragspositivität.

Volle Inzidenzsymmetrie lässt zwei Verluste auf den 9er- und 5er-Sektoren zu.
Erst zusätzliche Isotropie reduziert sie auf eine Zahl rho. In diesem
eingeschränkten Ansatz wählt exakt der B-Support rho=2/7. Ohne Isotropie
bleibt eine Familie mit gleichem Support und gleichem Polarzeichen.
Mit q*-Markierung ist die Freiheit größer, nicht kleiner.

Belege: [Polar- und Schattentest](polar_shadow/RESULTS.md). Das Ergebnis
erklärt die vorhandene Regel, nicht ihre physische Auswahl.

## 6. Zwei tatsächliche Anschlussstellen dürfen nicht übersprungen werden

### Gewöhnliche Positivität ist nicht automatisch P1-Reflexionspositivität

Die parabolische Quelle benutzt
U=[[3,0,0],[3,0,0],[3,0,0]], Sigma=diag(1,−1,−1), a=(1,1,2) und
Theta(X)=Sigma X^T Sigma. Auf dem echten Compilerbuchstaben gilt

\[
a^T\Theta(U)Ua=-9,\qquad a^TU^\dagger Ua=27.
\]

Der positive gewöhnliche Gram und die getestete Nahtreflexionsform sind
verschieden. Dies widerlegt weder P1 noch OS-Reflexionspositivität: Eine
passende positive Halbseitenalgebra kann kleiner sein. Es verbietet aber,
die ganze Wortalgebra ungeprüft als diese Hälfte auszugeben.

### Dreiercompiler und Viererträger brauchen einen typgerechten Anschluss

Der ursprüngliche U,V-Ankercompiler erzeugt eine parabolische Algebra der
Dimension7. Ihre kleinste †-Abschließung im bestehenden C3 ist M3(C),
Dimension9. Ein unitaler *-Homomorphismus M3(C) nach M4(C) existiert nicht:
Drei äquivalente minimale Projektoren hätten gleichen Bildrang r, also 3r=4.

Andere Verträge bleiben möglich: nichtunitale Einbettung, M3⊕C nach M4,
nichtmultiplikative positive Abbildung oder Modulbrücke. Keiner davon ist
automatisch ein unital getreues Gleichsetzen der Compiler.

Auch die vorhandene Z4-Mittelung muss typgerecht bleiben: Für den zentralen
Deckoperator iI4 ist der Durchschnitt seiner Konjugationen die Identität.
Die nichttriviale Sektormittelung in v993 verwendet eine nichtzentrale Clock.
Ihre positive operatorwertige Regel E(X†Y) ist ein möglicher Baustein; die
erforderliche Sektorwirkung entsteht nicht durch Umbenennen der Zentralphase.

## 7. Was noch nicht ausgewählt ist

Der eindeutige Spurkern besitzt triviale modulare Dynamik. Auch c=i sigma
mit linearer Ordnung12 erzeugt ohne relative Referenz nur drei verschiedene
Prozessstrahlen, denn c^(n+3)=−i c^n.

Positive kovariante Gluing-Regeln existieren schon als Familie
T_gamma(t)=P+exp(−gamma t)(I−P). Verschiedene positive gamma können nur
verschiedene Zeiteinheiten sein; dieses Beispiel allein beweist keine
dimensionslos unterschiedliche Physik. Die gesonderte relative-Ratenprüfung
liefert jetzt eine stärkere und genauer eingegrenzte Aussage.

Auf der tatsächlichen q*-markierten Clifford-Wortalgebra sei

\[
\mathcal L=\gamma_5\sum_{v\in O_5}(\operatorname{Ad}_{P_v}-I)
+\gamma_{10}\sum_{v\in O_{10}}(\operatorname{Ad}_{P_v}-I),
\quad \gamma_5,\gamma_{10}\ge0.
\]

O5 und O10 sind die beiden ursprünglichen markierten Wortorbits. Jede
Halbgruppe exp(t L) ist als Poissonmischung unitärer Wortoperationen vollständig
positiv, unital und spurtreu. Die tatsächliche signierte S5-Kovarianz wurde
mitgeprüft. Die beiden Kontrastzerfallsraten sind exakt

\[
r_5=8(\gamma_5+\gamma_{10}),\qquad
r_{10}=4\gamma_5+12\gamma_{10}.
\]

Die Wahl (gamma5,gamma10)=(1,0) gibt r5/r10=2, die Wahl (0,1) gibt 2/3.
Diese Verhältnisse lassen sich nicht durch Ändern der Zeiteinheit angleichen.
Wenn derselbe 10er-Kontrast auf 1/8 gefallen ist, beträgt der 5er-Kontrast
in den beiden Fällen 1/64 beziehungsweise 1/4.

**Die positive Vereinfachung ist ebenso wichtig:** Bei zusätzlich voller
unmarkierter Clifford-Kovarianz müssen die beiden Raten in dieser Familie
zusammenfallen. Dann bleibt nur eine gemeinsame Zeitskala. Eine stärkere
Symmetrie kann die Freiheit also tatsächlich beseitigen; sie darf nur nicht
behauptet werden, wenn zugleich eine widersprechende markierte Dynamik
verwendet wird.

Damit entsteht eine konkrete Vereinfachungsfrage: Gehört q* zur universellen
Bewegungsregel selbst, oder markiert q* lediglich den Randzustand und dessen
Auslese, während die Grundregel vollsymmetrisch bleibt? Die zweite Lesart
ist ein kleiner Kandidat, aber hier nicht aus P1 hergeleitet.

Der [Zweiraten-Nachtrag](redteam/TWO_RATE_ADDENDUM.md) enthält 284 exakte
Prüfungen, Normal/-OO-Replay und drei abgefangene Mutanten. Seine vollständige
Positivität ist ausdrücklich stärker als bloße Positivität einer
Prozess-Gram-Matrix. Dies konstruiert eine Gegenfamilie unter benannten
Annahmen, keine von TFPT physisch ausgewählte Dynamik.

Ein vorhandener Transfer bestimmt seine Iterationen. Weder diese algebraische
Bestimmtheit noch Schnittunabhängigkeit erklärt jedoch schon, weshalb genau
dieser Ablauf stattfindet, welche offene Randpräparation vorliegt und welche
lokalen Teile physisch miteinander verknüpft werden.

## 8. Der nächste entscheidende Suchauftrag

**Kann die tatsächliche orientierte P1-Naht eine positive Halbseiten- und
Kompositionsregel auswählen, deren geschlossene Bewertungen mit dem
eindeutigen Compiler-Loopkern übereinstimmen und deren offene Ausführung
keinen nachträglich passend gewählten Zustand oder Transfer braucht?**

Ein Anschluss muss die geordnete Dreierphase, die Klassen–Kontext-Dualität
und den Unterschied zwischen zentraler Deckphase und beobachtbarer
Sektorwirkung erhalten. Paarweise Wahrscheinlichkeiten oder einige gleiche
Konstanten genügen nicht. Veränderte Adjungierung, unbenannte Halbseite oder
passend gesetzte relative Raten zählen nicht als Herleitung.

T1–T8 bleiben offen. Kein gemeinsamer lokaler 3+1D-Ursprung, kein vollständiges
chirales Maß, keine vollständigen Standardmodellparameter und kein dynamischer
masseloser Spin-2-Sektor wurden aus diesem endlichen Kern gewonnen.
RH, Faktorisierung und P/NP wurden in dieser Runde nicht bearbeitet.

## 9. Reproduzierbarkeit

Der Hauptprüfer relational_kernel.py verwendet kleine exakte Matrizen und
ursprüngliche Projektoren: 209 neue Bedingungen plus 1073 geerbte aktive
P0/P1-Prüfungen. Normal/-OO-Ausgaben sind byteidentisch. Quelle und Loader
sind gepinnt. Die vollständige ursprüngliche v783-Gruppen-/Hom-Zählung
wird nicht als neu ausgeführt ausgegeben.

Die eigenständigen Redteam- und Polarbelege enthalten ihre Quellpins,
Prüfprogramme und Grenzen. Keine Originalquelle, kein TOE-Marker, kein
Hauptpaper und keine Website wurden geändert.
