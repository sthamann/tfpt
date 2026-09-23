# Geladene Antwort der korrelierten Originalquelle

**Contract:** UR.SOURCE.REGISTER_RESPONSE.01. **Gesamtverdict: PARTIAL.**
Die Formeln sind exakt unter dem angegebenen gemeinsamen Fock-Lift und
Feldwörterbuch. Das ist eine Weiterrechnung der Quelle, keine Herleitung
dieser Voraussetzungen aus P1/P2.

## 1. Quelle, Felder und eine gemeinsame Zeit

Sei V ein endlichdimensionaler Einteilchenraum, z=i und

\[
h_r=b+z^r a+z^{-r}a^\dagger,\qquad
H_R=\sum_{r=0}^3\Pi_r\otimes d\Gamma(h_r).
\]

b und a sind hier die unveränderten v1033-Blöcke. Der zweite Ausdruck ist der
**zusätzlich vorausgesetzte gemeinsame Lift** auf C4 ⊗ Fock(V), nicht die
Fockhebung des gesamten Einteilchenraums C4 ⊗ V. Beide Räume wären verschieden.

Für den tatsächlichen Sharp-Arc-u mit u⁴=1 benutzt die andere Lane

\[
T=\sum_r\Pi_r\otimes\Gamma(u)^r,\quad
F_j^u=T(S\otimes c_j)T^\dagger,\quad
J_s^u|\psi_N\rangle=|s-N\rangle\otimes\Gamma(u)^{s-N}|\psi_N\rangle.
\]

Die Registerexponenten werden modulo vier verstanden. Aus gemeinsamer unitärer
Konjugation folgen die CAR und das Feldintertwining. Bei **festgehaltenem H_R**
gilt

\[
H_RJ_s^u=J_s^uH_s^u,\qquad
H_s^u\big|_N=d\Gamma(h'_{s-N})\big|_N,\qquad
h'_r=u^{-r}h_ru^r.
\]

Es gibt nur die von H_R bestimmte Zeit; keine sektorweise Nachkalibrierung.
Erzeugung erhöht N um eins und wechselt r→r−1. Vernichtung wechselt r→r+1.
Der Endzustand entwickelt **alle** verbleibenden besetzten Moden mit dem neuen
h'-Block. Obwohl jeder feste N-Block frei ist, kann daher seine geladene Antwort
nicht durch Einfrieren des ursprünglichen Randoperators berechnet werden.

Die Summe der vier J_s-Bilder ist der vollständige Quellraum. Ein einzelnes s
ist nur relativ zur konstruierten CAR invariant. Der vorgegebene Disorder-
Operator D=S⊗Γ(u) erfüllt D J_s^u=J_(s+1)^u und verbindet die vier Bilder.
Sie werden hier nicht aus der vollständigen Observablealgebra entfernt.

## 2. Allgemeine Determinantenformel

Sei W eine d×N-Matrix mit linear unabhängigen besetzten Spalten w_a und

\[
g=\det(W^\dagger W)>0,\qquad
|\Phi\rangle=g^{-1/2}w_1\wedge\cdots\wedge w_N.
\]

Der Buchstabe W bezeichnet in diesem Abschnitt nur besetzte Orbitale, **nicht**
den nativen Kopplungstensor. Sei U eine beliebige Einteilchenmatrix und
A=W†UW. Dann gelten mit der klassischen Adjunkten adj(A):

\[
\begin{aligned}
\langle\Phi|c_k^\dagger\Gamma(U)c_j|\Phi\rangle
 &=\big[W\,\operatorname{adj}(A)W^\dagger\big]_{jk}/g,\\
\langle\Phi|c_j\Gamma(U)c_k^\dagger|\Phi\rangle
 &=\big[\det(A)U-UW\operatorname{adj}(A)W^\dagger U\big]_{jk}/g.
\end{aligned}
\]

**Beweis der ersten Formel.** c_j entfernt nacheinander die a-te besetzte
Spalte mit Vorzeichen (−1)^(a−1) und Koeffizient W_ja. Die Überlappung der zwei
verbleibenden Slaterdeterminanten ist der entsprechende (N−1)-Minor von A.
Die beiden Vorzeichen ergeben den Kofaktor. Summation über die beiden
entfernten Spalten ergibt W adj(A) W†.

**Beweis der zweiten Formel.** Beide durch c† ergänzten Slaterzustände haben
N+1 Spalten. Ihre Überlappung ist die geränderte Determinante

\[
\det\begin{pmatrix}
A&W^\dagger U e_k\\
e_j^\dagger U W&e_j^\dagger U e_k
\end{pmatrix}.
\]

Entwicklung nach letzter Zeile/Spalte liefert den angegebenen Ausdruck.
Beide Identitäten sind polynomial in U und den Orbitalen; sie benötigen kein
A⁻¹. Sie gelten auch für det(A)=0. Für N=0 lauten die Grenzfälle direkt
Entnahme=0 und Hinzufügen=U. Der Checker prüft zusätzlich eine singuläre
Überlappung mit nichtverschwindender Antwort exakt.

Sei jetzt |Φ⟩ ein Energieeigenzustand des Anfangsblocks h'_r mit Energie E0.
Für positive Anregungsenergien definieren wir

\[
K^+_{jk}(t)=\langle\Phi|c_j e^{-it(H_s^u-E_0)}c_k^\dagger|\Phi\rangle,
\quad
K^-_{jk}(t)=\langle\Phi|c_k^\dagger e^{-it(H_s^u-E_0)}c_j|\Phi\rangle.
\]

In der Hinzufügeformel ist U=exp(−it h'_(r−1)); in der Entnahmeformel
U=exp(−it h'_(r+1)). Beide werden mit exp(it E0) multipliziert. Das ist die
gesuchte **gemeinsame Quell-, Zustands- und Zeitantwort**, unter den benannten
Voraussetzungen. Die Vollantwort enthält die Determinante des besetzten
Meeres, nicht nur eine propagierte zusätzliche Einteilchenwelle.

Bei t=0 ist P=W(W†W)⁻¹W†, K⁻(0)=P und K⁺(0)=1−P. Der retardierte
Antikommutator lautet in dieser Konvention

\[
G^R_{jk}(t)=-i\theta(t)[K^+_{jk}(t)+K^-_{jk}(-t)].
\]

Er hat die richtige CAR-Sprungnormierung. Die positiven Entnahmeenergien
werden in G^R folglich zu negativen Frequenzen; diese Vorzeichen dürfen beim
Vergleich mit einem geladenen Spektrum nicht vertauscht werden.

Dies ist eine Anwendung bekannter Slater-/Determinantenidentitäten, kein
neues allgemeines Theorem über wechselwirkende Systeme. Verwandte
Fockraum-Determinantenmethoden: [Klich, cond-mat/0209642](https://arxiv.org/abs/cond-mat/0209642).
Der physikalische Vorgang ist ein durch das Feld ausgelöster Wechsel der
Randbedingung. Der Bezug zu solchen Operatoren ist Standardliteratur:
[Affleck, hep-th/9611064](https://arxiv.org/abs/hep-th/9611064).
Ein thermodynamischer Orthogonalitäts- oder CFT-Exponent folgt daraus hier
noch nicht.

## 3. Vollständiger Grundzustand des originalen endlichen Diagnosesystems

Verwendet werden nx=3, ny=1, **Masse +1**, genau wie in der ursprünglichen
Funktion register_hamiltonian, und der vorhandene Sharp-Arc-Endpunkt 0.
Keine neue Kopplung und kein chemisches Potential werden eingesetzt.

| Register r | Charakteristisches Polynom von h_r | Kleinste Fockenergie |
|---|---|---|
| 0 | x²(x²−3)² | −2√3 |
| 1 | (x²−2)(x⁴−4x²+1) | −√6−√2 |
| 2 | (x−2)(x−1)²(x+1)²(x+2) | −4 |
| 3 | wie r=1 | −√6−√2 |

Die minimale Fockenergie ist jeweils die Summe aller negativen
Einteilchenenergien; Nullmoden verändern die Energie nicht. Deshalb ist der
**globale Grundzustand des gesamten gelifteten Systems eindeutig**: r=2,
N=3, E0=−4. Die zwei negativen entarteten −1-Moden werden beide besetzt und
erzeugen daher keine Mehrdeutigkeit des gefüllten Slaterzustands. Die globale
Lücke beträgt exakt 4−√6−√2. Die kodierte Klasse ist s=r+N=1 modulo vier.
Sie ist hier eine Folge der vollständigen Grundzustandsrechnung, keine
vorherige Einschränkung auf ein gewünschtes s.

Im kodierten Wörterbuch gilt h0=h'_2 und

\[
P=\frac12\left[1-\frac{7h_0-h_0^3}{6}\right].
\]

Das Polynom hat für die vier Eigenwerte −2,−1,1,2 genau die Werte der
negativen Spektralprojektion. Es liefert einen rational-komplexen Projektor
mit Rang 3. Seine dritte äußere Potenz ist die reine, normierte
Grundzustandsdichte. Die ersten drei unabhängigen Spalten haben Gram-
Determinante 1/144; ihre äußere Potenz mal 12 ist ein exakt normierter
Grundzustandsvektor.

Dieser Befund betrifft das **endliche Originaldiagnosesystem mit dem
vorausgesetzten Lift**. Er selektiert weder einen unendlichen physikalischen
Vakuumzustand noch die Originalparameter aus P1/P2.

## 4. Exakte geladene Momente und dreizehn Spektrallinien

Für r=2,N=3 wird die Hinzufügeantwort im vollständigen N=4-Fockblock von h'_1
berechnet, die Entnahmeantwort im N=2-Fockblock von h'_3. Über alle sechs
Felder summiert stimmen die positiven Hinzufüge- und Entnahmemaße exakt
überein. Ihre Momente sind:

| Ordnung k | Tatsächliche Quelle, beide Antworten | Fälschlich festgehaltenes h'_2 |
|---|---:|---:|
| 0 | 3 | 3 |
| 1 | 16/3 | 4 |
| 2 | 115/9 | 6 |
| 3 | 115/3 | 10 |
| 4 | 1220/9 | 18 |

Diese sind nicht normierte Momente; die Gesamtgewichte sind jeweils 3.
Normiert ist die mittlere Energie 16/9 statt 4/3. Bereits die erste Ableitung
der Zeitantwort entscheidet also die falsche Abkürzung. Besetzungen allein
(k=0) würden diesen Unterschied übersehen.

Der Unterschied geht über eine Verschiebung oder Skalierung zweier freier
Linien hinaus. Schreibe x=ω−4. Der reduzierte Nenner des exakten
Spurresolventen lautet

\[
D(x)=x(x^2-2)(x^2-6)(x^4-4x^2+1)(x^4-12x^2+9).
\]

Der zugehörige Zähler ist

\[
\begin{aligned}
P_{12}(x)={}&3x^{12}-\tfrac{20}{3}x^{11}-\tfrac{485}{9}x^{10}
+109x^9+\tfrac{2798}{9}x^8-559x^7\\
&-\tfrac{6376}{9}x^6+1063x^5+\tfrac{1969}{3}x^4
-711x^3-\tfrac{677}{3}x^2+126x+20.
\end{aligned}
\]

Für beide Antworten gilt R(ω)=P12(ω−4)/D(ω−4). Herleitung: Die tatsächlichen
15×15-Fockmatrizen haben charakteristisches Polynom x²D(x). Sie sind
hermitesch, also diagonalisierbar; D annihiliert sie. Die dreizehn ersten
exakten Momente bestimmen den Zähler der rationalen Resolvente. Exakte
Polynomdivision ergibt gcd(P12,D)=1 und gcd(D,D')=1. Somit existieren **alle
dreizehn verschiedenen Pole** tatsächlich. Ihre Gewichte sind wegen der
positiven spektralen Darstellung positiv. Die Einzelgewichte in der Grafik
werden numerisch angezeigt; ihre Anzahl und ihr Nichtverschwinden hängen
nicht von einer numerischen Schwelle ab.

Die kleinste geladene Anregungsenergie ist

\[
\Delta_\mathrm{charged}=4-\sqrt{2+\sqrt3}-\sqrt2
\approx0.6539347850.
\]

Das eingefrorene freie Modell hätte nur die Energien 1 und 2 mit Gewichten
2 und 1. Die Zahl dreizehn zeigt außerdem, dass die volle Antwort dieser
sechs kanonischen Felder nicht diejenige eines einzigen zahlenerhaltenden
quadratischen Sechsmoden-Hamiltonoperators ist. Dessen lineare geladene
Felder hätten höchstens sechs Einteilchenfrequenzen. Auf festem N bleiben
die vorliegenden Blöcke trotzdem frei; eine lokale Kollision oder Bindung
wird hieraus nicht abgeleitet.

## 5. Der ursprüngliche Disorder-Operator bleibt enthalten

Für D und D† bleibt N=3 gleich, während r=2 nach 3 beziehungsweise 1 wechselt.
In den J^u-Koordinaten ist ihr Materievektor unverändert. Ihre normierten
Antworten sind daher

\[
K_D(t)=e^{-4it}\frac{\det(W^\dagger e^{-it h'_3}W)}{g},\qquad
K_{D^\dagger}(t)=e^{-4it}\frac{\det(W^\dagger e^{-it h'_1}W)}{g}.
\]

Beide erreichen tatsächlich die erste globale Anregung

\[
\Delta_D=4-\sqrt6-\sqrt2\approx0.1362966948.
\]

Ihr Gewicht am niedrigsten Pol ist exakt

\[
\frac{245}{1296}+\frac{35\sqrt3}{324}
+\frac{343\sqrt2}{2592}+\frac{25\sqrt6}{324}
\approx0.7522945319>0.
\]

Zur exakten Berechnung dient der negative Spektralprojektor des Endblocks:
sgn(h)=c0 h+c1 h³+c2 h⁵ mit

\[
c_0=\sqrt6-\sqrt2/6,\quad
c_1=(4\sqrt2-5\sqrt6)/6,\quad
c_2=(\sqrt6-\sqrt2)/6.
\]

Für seine drei positiven Eigenwerte (√6±√2)/2 und √2 gibt das Polynom +1,
für die negativen −1. Das Gewicht ist det(W†P_final W)/g. Diese Formel
vergleicht zwei vollständige gefüllte Meere, ohne einen Fockeigenvektor
numerisch auswählen zu müssen. Die ersten Momente der D-Antwort sind
1, 2/3, 13/9, 4 und 110/9.

Damit sind die kleinste globale Lücke und die kleinste geladene Lücke
verschieden, aus einem klaren Grund: D erhält N und wechselt s, während F^u
die Teilchenzahl wechselt und s erhält. Die vier Sektoren als vollständig
unzugänglich zu erklären würde eine vorhandene Quellobservable und ihre
berechnete niederenergetische Antwort entfernen.

## 6. Prüfumfang und Herkunftsgrenze

Die Originalmatrizen werden nicht nur anhand ähnlicher Formeln nachgebaut:
Der gepinnte bestehende Helfer führt die einschlägigen Definitionen aus dem
unveränderten v1033-Quelltext aus und vergleicht sämtliche Matrixeinträge mit
der exakten rational-komplexen Rekonstruktion.

Die allgemeinen Identitäten in Abschnitt 2 werden analytisch bewiesen.
Der Checker kontrolliert sie zusätzlich an den Quellmatrizen, an einem
komplexen nichtorthogonalen Beispiel und an einer singulären Überlappung.
Die Zeitantwort wird mit unabhängigen Exponentialmatrizen des vollständigen
N=2-/N=4-Fockoperators verglichen. Endlich viele numerische Zeitpunkte sind
Kontrollen des Codes; der Allzeitaussage liegt die äußere Algebra zugrunde.

Die korrelierte Register-Lane war beim ersten Einfrieren ihres Textstands noch
ohne ausführbares Zertifikat. Ihre gelesenen Dokumente liegen als gepinnte
Snapshots bei. Noch vor Abschluss dieses Contracts wurde ihr fertiger Checker
verfügbar: Seine 183 Kontrollen wurden normal und optimiert erneut ausgeführt;
beide Ausgaben sind byteidentisch mit ihrem Originalzertifikat. Der zusätzliche
Herkunftsnachweis steht in upstream_replay_manifest.json, getrennt von den
ursprünglichen Textsnapshots. Die für diesen Contract verwendeten Gleichungen
werden in Abschnitt 1 algebraisch nachvollzogen.

Die fertiggestellte Lane liefert außerdem einen relevanten analytischen
Grenzsatz. Bei fester beschränkter Zylinderbreite, wachsendem Umfang, festem t
und neutralen lokalen Observablen in wachsender Entfernung vom Schnitt folgt
aus dem Duhamel-/Lieb-Robinson-Bound

\[
\|\tau_t^{H_s^u}(O_X)-\tau_t^{d\Gamma(h'_0)}(O_X)\|
\le C_X(e^{v|t|}-1)e^{-a\,\mathrm{dist}(X,Y)}.
\]

Diese neutrale lokale Dynamik nähert sich der ungetwisteten freien Quelle.
Die dreizehn geladenen Pole widersprechen dem nicht: Sie betreffen Felder,
die den Randoperator des ganzen Meeres wechseln. Eine neue lokale Kraft im
Inneren durch bloßes Vergrößern dieser unveränderten Quelle ist im genannten
Grenzfall ausgeschlossen. Der Satz behauptet weder Gaussianisierung
beliebiger Zustände noch eine Grenze für Zeiten, die mit der Entfernung
wachsen. Seine Quelle ist Abschnitt 4a des beigefügten fremden PROOF-Snapshots;
er wird hier als analytischer Befund der anderen Lane integriert.

Offen bleiben insbesondere die ursprüngliche Auswahl des gemeinsamen
Fock-Lifts und der physischen geladenen Feldalgebra, die Herkunft einer lokalen
Wechselwirkung jenseits dieses reinen Randschnittmechanismus, deren lokales Eich-
Wörterbuch, die Herkunft der für E8 benötigten Kanäle sowie ein gemeinsamer
Anschluss an Flavor, alpha und 3+1D-Dynamik. Eine native Hilfsbank muss nicht
zwingend das Ziel dieser Quelle sein. Ihre schon geprüften Ausschlüsse sind
deshalb keine Ausschlüsse dieses Quellweges insgesamt.
