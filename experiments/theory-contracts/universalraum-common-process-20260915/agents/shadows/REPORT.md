# Gemeinsame Schattenkarte auf dem ursprünglichen W

Stand: 15. September 2026. Eigenständiger Folgeschritt zu v1.6.7.

## Ergebnis

Der ursprüngliche Tensor liefert jetzt eine vollständig berechnete gemeinsame
Schattenkarte für den inneren hellen N=2-Code. Einzelne Besetzungen unterscheiden
nur 24, sämtliche Einteilchenoperatoren nur 736 von insgesamt 3600 hermiteschen
Operatorrichtungen. Paarbesetzungen zusammen mit ausführbaren Drehungen aus
G=Spin(10)×SU(4) liefern dagegen eine vollständige Zustandsrekonstruktion.
Eine konkrete endliche Familie mit 3599 nichtkonstanten Erwartungswerten liegt
bei. Diese letzte Aussage ist **bedingt auf die Ausführbarkeit der zusätzlichen
Kontrollen und Messungen**. Aus ihrer algebraischen Existenz folgt noch kein
ursprüngliches Messinstrument samt Zustandsänderung.

Das Ergebnis betrifft denselben ursprünglichen W, keine ersatzweise eingeführte
Qubit-Analogie. Der W-Dateipin ist
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.
Die vier gelesenen v1.6.7-Kontextdateien sind ebenfalls unverändert eingefroren.

## 1. Ein gemeinsamer Träger, mehrere Schatten

Mit V=W†/√8 gilt V†V=I auf C^60. Für eine logische Dichtematrix ρ lautet der
Schatten eines Fermionoperators O

\[
  \Phi_{\mathcal O}(\rho)_O=\operatorname{tr}(\rho V^\dagger O V).
\]

Alle folgenden Messfamilien beziehen sich auf genau dieselbe ρ und denselben
Kodierer. Die Dimension der reellen Menge hermitescher 60×60-Matrizen ist 3600;
bekannte Spur eins reduziert die freien Zustandsparameter auf 3599.
Alle angegebenen Familien enthalten die Identität in ihrem linearen Raum,
sodass ihre unsichtbaren Kerne bereits spurfrei sind.

| Messfamilie | Exakter Operatorrang | Unsichtbare Zustandsdifferenzen | Verfügbarkeit |
|---|---:|---:|---|
| Alle 64 Einzelbesetzungen n_r | 24 | 3576 | Konkrete Operatoren; ursprüngliche Messausführung offen |
| Alle hermiteschen Einteilchenbilineare f_r†f_s | 736 | 2864 | Zusätzliche vollständige Bilinearfamilie |
| Alle G-gedrehten Einzelbesetzungen | 736 | 2864 | Bedingt auf ausführbare G-Kontrollen |
| Alle 2016 ungedrehten Paarbesetzungen n_i n_j | 60 | 3540 | Gemeinsame Besetzungsmessung erforderlich |
| Bilineare plus ungedrehte Paarbesetzungen | 772 | 2828 | Beide vorigen Ressourcen zusammen |
| G-gedrehte Paarbesetzungen | 3600 | 0 | Gemeinsame Messung und ausführbare G-Kontrollen |

Der Rang zählt unabhängige lineare Erwartungswerte. Er zählt weder
Messapparaturen noch Messwiederholungen noch physische Raumrichtungen.

## 2. Exakter Rangbeweis am Tensor

Die Datei enthält zehn symmetrische 16×16-Matrizen β_k. Mit den sechs
antisymmetrischen 4×4-Farbmatrizen ε_c gilt eintragsweise

\[
 W_{(k,c),(p,a)(q,b)}=(\beta_k)_{pq}(\epsilon_c)_{ab}
 \quad\text{für }(p,a)<(q,b).
\]

Der Prüfer rekonstruiert hieraus den gesamten W und vergleicht alle Einträge.
Für sämtliche 4096 Bilineare vergleicht er zudem die direkte CAR-Kontraktion
mit der Faktorformel

\[
 8V^\dagger f_{p,a}^\dagger f_{q,b}V
   =F_{pq}\otimes C_{ab},\qquad
 (F_{pq})_{kl}=\sum_t(\beta_k)_{pt}(\beta_l)_{qt},\quad
 (C_{ab})_{cd}=\sum_t(\epsilon_c)_{at}(\epsilon_d)_{bt}.
\]

In den aus den W-Faktoren abgeleiteten orthogonalen reellen Rahmen ist der
Spin-Bildraum genau `Skalar ⊕ i·antisymmetrisch`, Dimension 1+45=46;
der Farbbildraum hat Dimension 1+15=16. In der ursprünglichen Gewichtsbasis
prüft der Code die äquivalente ganzzahlige Identität

\[
 n(A+\eta A^T\eta)=2\operatorname{tr}(A)I_n.
\]

Sie liefert jeweils die obere Ranggrenze. Ein nichtverschwindender modularer
Minor über dem Primkörper mit 1009 Elementen liefert die passende untere Grenze.
Damit sind die Ränge über Q und C exakt bewiesen; es handelt sich nicht um
eine toleranzabhängige numerische Rangschätzung. Produktbildung ergibt 736.

Für die diagonalen Einzelbesetzungen bleiben nur Skalar plus Cartan:
(1+5)(1+3)=24. Die Adjungierten von so(10) und so(6) sind irreduzibel;
jede ursprüngliche Einzelbesetzung hat einen nichtverschwindenden Skalar-
und Cartananteil in beiden Faktoren. Ihr G-Orbit erzeugt deshalb alle vier
Summanden von (1⊕45)⊗(1⊕15), insgesamt 736, und keine weiteren.

Der Eingabekern der gesamten Einteilchenkompression hat Dimension
4096−736=3360=(256−46)·16. Er ist vom unsichtbaren *Zustandskern* mit
Dimension 3600−736=2864 zu unterscheiden.

### Was genau fehlt?

Die gesamte Hermitesche Algebra zerfällt in den beiden reellen Faktoren als

\[
 (1\oplus i\Lambda^2\mathbb R^{10}\oplus\operatorname{Sym}^2_0\mathbb R^{10})
 \otimes
 (1\oplus i\Lambda^2\mathbb R^6\oplus\operatorname{Sym}^2_0\mathbb R^6).
\]

Die letzten symmetrischen, spurlosen Komponenten haben Dimension 54 und 20.
Dem Bilinearschatten fehlen exakt die drei disjunkten Räume

\[
 54\otimes(1\oplus15),\quad (1\oplus45)\otimes20,
 \quad54\otimes20,
\]

mit Dimension 864+920+1080=2864. Das ist eine konkrete Beschreibung des
vollständigen unsichtbaren Kerns, nicht bloß eine Dimensionsdifferenz.

Ein Verzicht auf alle imaginären Phasen wäre nochmals stärker: In demselben
reellen Gesamtrahmen haben reelle symmetrische Operatoren Dimension
55·21+45·15=1830; imaginäre antisymmetrische Operatoren haben Dimension
55·15+45·21=1770. Ein ausschließlich reeller Schatten könnte diese 1770
Richtungen nicht sehen. Die native G-Familie enthält die nötigen
phasenempfindlichen Richtungen; ihre Ausführbarkeit wird damit nicht bewiesen.

## 3. Zwei orthogonale Zustände mit identischen eingeschränkten Schatten

In der ursprünglichen logischen Gewichtsbasis, nullbasiert mit A=6k+c, setze

\[
 |\psi_\pm\rangle=\frac{|0\rangle\pm|30\rangle}{\sqrt2},
 \qquad \rho_\pm=|\psi_\pm\rangle\langle\psi_\pm|.
\]

Beide Matrizen sind exakt positiv, rein und zueinander orthogonal. Es gilt
für alle r,s und für alle i<j

\[
 \operatorname{tr}[(\rho_+-\rho_-)V^\dagger f_r^\dagger f_sV]=0,
 \qquad
 \operatorname{tr}[(\rho_+-\rho_-)V^\dagger n_in_jV]=0.
\]

Insbesondere ändern beliebig viele G-gedrehte Einteilchenmessungen daran
nichts. Die Zustände unterscheiden sich in einer fehlenden Spin-54-Richtung.

Der normierte logische Vektor

\[
 |z\rangle=\tfrac12(|0\rangle+|30\rangle+i|6\rangle+i|36\rangle)
\]

liegt hingegen im G-Orbit eines ursprünglichen Kanalvektors. Die zugehörige
gedrehte Paarbesetzung komprimiert zu |z⟩⟨z|/8 und liefert die exakt
verschiedenen Erwartungswerte 1/16 und 0. Dies ist ein positiver Zustandszeuge
für die Verbesserung durch die zusätzliche Paarressource.

## 4. Endliche, minimale Familie für vollständige Rekonstruktion

Jede unterstützte Paarspalte des W hat genau einen Eintrag±1. Daher gilt

\[
 V^\dagger n_i n_jV=\tfrac18|A\rangle\langle A|
\]

für den zugehörigen Kanal A. Jeder der 60 Kanäle tritt auf. Ungedrehte
Paarbesetzungen erzeugen also exakt alle Diagonalmatrizen. Ihr Schnitt mit
dem Bilinearraum hat Dimension 24: Diagonalprojektion erhält die oben
angegebenen Faktor-Bildräume und hat in ihnen Rang 6 und 4. Damit folgt der
kombinierte Rang 736+60−24=772.

Der Prüfer leitet die reellen Rahmen aus den invarianten Faktormetriken ab.
Er prüft außerdem das W-Intertwining für sämtliche 45+15 Lie-Generatoren
und ihre vollständigen Bilder so(10), so(6). G wirkt im logischen Raum
folglich als SO(10)×SO(6), jeweils mit seiner Spin/SU(4)-Überlagerung.

Ein ursprünglicher Gewichtskanal ist in jedem Faktor ein zirkularer Vektor
(e_i+i e_j)/√2. Sein SO(n)-Orbit besteht aus (u+i v)/√2 mit reellen,
orthonormalen u,v. Für n=10 und n=6 erzeugt der Prüfer eine rationale Liste
solcher Projektoren:

1. Alle (e_i±i e_j)/√2.
2. Für jedes i<j und ein drittes k den Vektor
   `(3e_i+4e_j+5i e_k)/sqrt(50)`.

Alle 50P haben ganzzahlige reelle und imaginäre Einträge. Der Code prüft
`P²=P`, `tr(P)=1` und die Isotropie `tr(P Pᵀ)=0` exakt nach Skalierung.
Die Isotropie und die Norm kennzeichnen diese SO(n)-Gewichtsorbits; durch
Orientierungswahl auf dem orthogonalen Komplement existiert eine Drehung
mit Determinante+1. Beliebige U(10)- oder U(6)-Kontrollen werden nicht benutzt.

Modulare Zeilenauswahl liefert folgende konkrete unabhängige Basen:

\[
 \mathcal B_{10}=\{I_{10},P_1,\ldots,P_{99}\},\qquad
 \mathcal B_6=\{I_6,Q_1,\ldots,Q_{35}\}.
\]

Die ausgewählten Vektoren und Indizes stehen vollständig im Ergebnis-JSON.
Ihre Produkte bilden eine Basis aller hermiteschen 60×60-Matrizen. Bei
bekannter Spur bleibt eine minimale Familie von 3599 nichtkonstanten Zahlen:

- 99·35=3465 gedrehte Paarprojektoren P_a⊗Q_b;
- 99 Spinwerte P_a⊗I_6, als Summe über die sechs Farbkanäle;
- 35 Farbwerte I_10⊗Q_b, als Summe über die zehn Spinkanäle.

Alle physisch angesetzten Paarerwartungswerte besitzen denselben Faktor 1/8;
die Rekonstruktion kalibriert ihn ausdrücklich zurück. Da ein offener
Bereich um I/60 alle 3599 spurlosen hermiteschen Richtungen enthält, kann
keine feste Familie linearer Skalarerwartungswerte mit weniger als 3599
Zahlen jeden Zustand identifizieren. **Minimalität bezieht sich genau auf
diese Zahlenzahl**, nicht auf Geräteeinstellungen oder Messkosten.

### Unabhängige Rekonstruktionsprüfung

Die Familie wird ohne Zustandsdaten festgelegt. Anschließend werden die
beiden obigen reinen Zustände sowie sechs deterministisch zufällige Zustände
der Ränge 1, 2, 5, 17, 60, 60 in derselben ursprünglichen W-Codebasis verwendet.
Aus ihren 3599 kalibrierten Schatten rekonstruiert der Prüfer die vollständigen
Dichtematrizen. Zusätzlich sagt er je zwölf vorher unbenutzte, G-gedrehte
Paarerwartungswerte dieser selben Zustände voraus.

Diese Tests sind **numerisch**, nicht als exakte Zustandsbeweise ausgegeben.
Im dokumentierten Lauf beträgt der größte Matrixeintragsfehler unter
7.6×10⁻¹⁶; der größte Fehler der 96 unbenutzten Paarvorhersagen liegt unter
5.8×10⁻¹⁷. Die Antwortmatrizen der Faktoren haben Konditionszahlen ungefähr
40.47 und 20.72. Das ist ein rauschfreier Rekonstruktionstest; statistische
Messkosten, Zustandspräparation und Robustheit gegen reales Rauschen sind
hier nicht nachgewiesen.

## 5. Was native Zeitentwicklung hinzufügt

Der gemeinsame helle N=2-Prozess besitzt H=h⊗I_60. Für jeden Zweigoperator B
und inneren Operator O gilt exakt

\[
 [h\otimes I,B\otimes O]=[h,B]\otimes O.
\]

Beliebige Zeitableitungen und Zeiten verändern daher nur den Zweigfaktor.
Sie erweitern den inneren Schattenrang 24 beziehungsweise 736 nicht.
Die zusätzlichen Paarsonden können den inneren Rang dagegen bis 3600 erhöhen.
Zweigkohärenz und ihre Rekonstruktion erfordern eine gesonderte
Prozessbetrachtung; eine innere Zustandsrekonstruktion allein bestimmt noch
keine vollständige Mehrzeitgeschichte oder ein Messinstrument.

## Reproduktion und Grenze

Mit Python 3.10 oder neuer und NumPy, aus diesem Ordner:

```sh
python3 -B replay.py
```

Der Lauf überprüft die fünf eingefrorenen Quellenpins, führt den eigenen
Prüfer normal und mit `-OO` aus und verlangt byte-identische Ausgaben.
Warnungen gelten als Fehler; keine Prüfbedingung benutzt abschaltbare
Python-Assertions. Die Prüfzahlen stehen im Replay-Manifest.
Die vier Kontextdateien werden gehasht, nicht als fremde Gesamtsuite erneut
ausgeführt. Die mathematische Prüfung benutzt nur die lokale W-Archivdatei.

Damit ist eine gemeinsame, am Ursprungstensor kalibrierte *innere*
Schattenkarte konstruiert. Ein räumlicher Rand, ursprüngliche ausführbare
Instrumente, eine universelle Prozessidentifikation, 3+1D-Raumzeit oder ein
Abschluss von T1–T8 folgt daraus nicht.
