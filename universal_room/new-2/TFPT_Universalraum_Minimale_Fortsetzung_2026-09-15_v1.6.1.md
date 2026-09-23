# TFPT / Universalraum: minimale Forschungsfortsetzung nach v1.6

Forschungsnotiz v1.6.1, 15. September 2026. Keine neue PDF-Hauptrevision.
Das vollständige Hauptdokument und das kurze Update v1.6 bleiben unverändert.

## Ergebnis in einem Satz

**Eine zusätzliche Belegung, nicht eine zusätzliche Wechselwirkung, erzeugt
im ursprünglichen nativen Modell neue Übergänge. Der dabei verbleibende
64-dimensionale Sektor lässt sich aus denselben Clifford-Matrizen konstruieren
und einschließlich aller relevanten Vorzeichen mit E8 verbinden.**

Das ist ein konkreter positiver Fortschritt des Minimalansatzes. Es löst einen
endlichen Vielteilchensektor und eine algebraische Anschlussfrage. Es erzeugt
weder räumliche Orte noch das physische Vakuum oder eine vollständige TOE.
„Neu“ bezeichnet die hier ausgeführte Forschungsfortsetzung, keinen belegten
Prioritätsanspruch gegenüber der gesamten mathematischen Literatur.

## 1. Unveränderte Quelle und präziser Vergleich

Wir behalten genau

\[
H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),
\qquad N=N_f+2N_b,
\]

mit 64 fermionischen Moden, 60 bosonischen Moden und

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad WW^\dagger=8I_{60}.
\]

W wird aus Außenalgebra-Vorzeichen unabhängig rekonstruiert und gegen die
bisherige Tensorquelle geprüft. SHA-256:
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.
Quelle:
`/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz`.

Wir fügen für die Ergebnisse der Abschnitte 2–4 weder Ortsgitter noch Hopping,
neue Kopplungsstärke oder zusätzlichen Hamiltonterm hinzu. Der untersuchte
Eingang beziehungsweise N-Sektor ist trotzdem eine Voraussetzung, keine
hier abgeleitete physische Präparation.

## 2. Was die kleinste Ausführung wirklich kann

### 2.1 N=2: sechzig gleiche Schwingungen

Die 2076 Zustände zerfallen in 60 voneinander getrennte Sterne mit je einem
Vermittler und acht Paarzuständen sowie 1536 isolierte Paarbasiszustände.
Jeder Stern hat einen hellen und sieben dunkle Paarkanäle. Insgesamt sind
1956 Zustände dunkel. Auf dem hellen Raum ist H genau

\[
\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}\otimes I_{60}.
\]

Die unital erzeugte Operatoralgebra aus Konversion und Bosonbesetzung ist
`C auf dem Dunkelraum ⊕ (M2(C) ⊗ I60)` und hat Dimension fünf. Das wurde über
skalierte Matrixeinheiten und ihre ganzzahligen Produkte geprüft. Beliebige
Wörter aus genau diesen Kontrollen beseitigen die 60-fache innere
Ununterscheidbarkeit nicht. Eine einzige fest gewählte Zeitentwicklung hat
noch weniger unabhängige Operatoren; die Fünferangabe betrifft die beiden
erlaubten Generatoren gemeinsam.

Auch ein vermeintlicher Ortsimpuls, der lediglich die acht vorhandenen
Cartan-Gewichte in Phasen umschreibt, erzeugt keinen neuen Schritt. Auf allen
480 Vertizes ist `q_i+q_j-q_A=0`. Daher cancelt
`exp(i k·(q_i+q_j-q_A))` identisch. Das ist die vorhandene Ladungserhaltung,
nicht eine Konstruktion räumlicher Translationen.

Diese Aussage gilt ausdrücklich für N=2. Sie ist kein Stillstandssatz für
die volle ursprüngliche Wechselwirkung.

### 2.2 N=3: derselbe Vertex verbindet die Kanäle

Ein zusätzliches Fermion verändert die Anschlussmöglichkeiten. Der gesamte
Sektor enthält 41664 Dreifermionenzustände und 3840 Zustände mit einem Boson
und einem Fermion. Die ursprünglichen Konversionen ergeben die Matrix

\[
C_3:\Lambda^3\mathbb C^{64}\longrightarrow
\mathbb C^{60}\otimes\mathbb C^{64},
\quad S=C_3C_3^\dagger.
\]

C3 hat genau 29760 nichtverschwindende, vorzeichenrichtige Einträge. Für alle
3840 Zeilenzustände wurde exakt bewiesen:

\[
S(S-7I)(S-10I)(S-12I)=0.
\]

| Eigenwert von S | Exakte Multiplizität |
|---|---:|
| 0 | 64 |
| 7 | 2880 |
| 10 | 576 |
| 12 | 320 |

Die Eigenwerte wurden zunächst numerisch als Kandidaten gefunden. Der
Nachweis verwendet danach ausschließlich die verschwindende ganzzahlige
Polynommatrix und rationale Spuren ihrer Spektralprojektoren. Eine vorher
berechnete Zeilensummen-Schranke verhindert Ganzzahlüberlauf. Gerundete
Eigenwerte sind nicht die Beweisgrundlage.

Damit ist das Spektrum des gesamten 45504-dimensionalen N=3-Hamiltonoperators
bestimmt: 37888 Zustände bei Energie null, 64 bei Delta und für jedes positive
lambda die beiden Energien

\[
E_{\lambda,\pm}=\frac{\Delta\pm\sqrt{\Delta^2+4g^2\lambda}}2
\]

mit der Tabellenmultiplizität. Insbesondere hat der niedrigste N=3-Wert
320-fache Entartung. Auch diese vollständige Sektorlösung wählt keinen
einzelnen Grundzustand der gesamten Theorie aus.

### 2.3 Ein konkreter Übergang ohne neuen Hopping-Term

In der gepinnten Modenordnung gilt:

\[
|b_{36},f_4\rangle
\longrightarrow |f_0f_4f_{57}\rangle
\longrightarrow |b_0,f_0\rangle.
\]

Es gibt für dieses Matrixelement genau den angegebenen Dreifermionenweg.
Sein CAR-Vorzeichen ergibt `S_final,initial=-1`. Daher ist der führende
Zeitentwicklungskoeffizient `+g² t²/(2 hbar²)`, obwohl das direkte
Hamiltonmatrixelement zwischen Anfang und Ende null ist. Eine zweite
Berechnung mit Besetzungsbits bestätigt das Vorzeichen unabhängig von der
Außenalgebra-Matrixkonstruktion. Entfernen eines der beiden Originalvertizes
setzt den führenden Übergang auf null.

Die ganze dazugehörige Komponente hat nur 35 Zustände. Ihr fünf-dimensionaler
Boson-Fermion-Block hat `S=7I+vv†` mit `v†v=5`. Deshalb gilt für alle Zeiten

\[
\mathcal A_{36,4\to0,0}(t)=\frac{q_7(t)-q_{12}(t)}5,
\]

\[
q_\lambda(t)=e^{-i\Delta t/(2\hbar)}
\left[\cos\frac{\Omega_\lambda t}{2\hbar}
-i\frac{\Delta}{\Omega_\lambda}
\sin\frac{\Omega_\lambda t}{2\hbar}\right],
\quad\Omega_\lambda=\sqrt{\Delta^2+4g^2\lambda}.
\]

Bei g/Delta=1/20 und t=hbar/Delta beträgt die Wahrscheinlichkeit numerisch
`1.4661072538691504e-6`. Eine direkte 35D-Zeitentwicklung stimmt in der
Amplitude bis `2.48e-17` überein. Die kleine Wahrscheinlichkeit ist kein
Optimierungsresultat; der Ausdruck für alle Zeiten ist das wesentliche Ergebnis.

**Grenze:** Das Fermion ändert einen inneren Modenindex und der Vermittler
kompensiert seine Ladungsänderung. Kein Teil dieser Rechnung identifiziert
Modenindex 4 oder 0 mit einer Raumposition. Die lokale Paritätsschranke für
getrennte Banken mit ausschließlich lokal geraden Vertizes bleibt bestehen.

## 3. Der 64er-Rest ist nicht beliebig: eine exakte E8-Kompositionsfolge

Der Nullraum von S lässt sich direkt aus den ursprünglichen Spinormatrizen
beta und dem antisymmetrischen Vierfarben-Tensor konstruieren. Für
A=(k,ab), Fermion (s,c), Ausgang (t,d) definieren wir

\[
J_{td;(k,ab),sc}=(\beta_{\bar k})_{st}\epsilon_{abcd},
\qquad \bar k=(k+5)\bmod10.
\]

Diese Vorschrift enthält keine an den Nullraum angepassten Koeffizienten.
Die Rechnung ergibt

\[
JC_3=0,\qquad JJ^\dagger=15I_{64},
\]

und sogar die explizite Projektoridentität

\[
\frac{J^\dagger J}{15}
=-\frac{(S-7I)(S-10I)(S-12I)}{840}.
\]

Aus Rang C3=3776 und Rang J=64 folgt

\[
\Lambda^3\mathbb C^{64}
\xrightarrow{C_3}\mathbb C^{60}\otimes\mathbb C^{64}
\xrightarrow{J}\overline{\mathbb C^{64}}\longrightarrow0.
\]

Diese Folge ist **in der Mitte und am letzten Raum exakt**: Alles, was J
vernichtet, kommt von C3; jeder Ausgang von J wird erreicht. Am ersten Raum
ist sie nicht injektiv — dort bleibt der 37888-dimensionale Kern. Der Balken
bezeichnet hier zunächst die konjugierten acht Gewichtslabels, nicht schon
eine physische Antiteilcheninterpretation.

### 3.1 Mehr als passende Dimensionen: Vorzeichenanschluss an E8

Alle Null- und Nichtnullstellen der zwei Bracket-Typen werden mit E8-
Wurzeladdition verglichen. Zusätzlich werden gleichzeitig 480 ursprüngliche
Koeffizienten und 960 neue J-Koeffizienten mit dem Standard-Gittercocycle

\[
\varepsilon(m,n)=(-1)^{m^TFn},\quad
F_{ii}=1,\quad F_{ij}=\operatorname{Cartan}_{ij}\bmod2\ (i>j)
\]

abgeglichen. Ein diagonaler Vorzeichenwechsel der 188 beteiligten
Wurzelbasisvektoren löst sämtliche 1440 Gleichungen. Das F2-System hat Rang
179; der konkrete Lösungsvektor und die Rücksubstitution stehen im JSON.

Damit stimmen diese beiden aufeinanderfolgenden Bracket-Typen einschließlich
der Jacobi-artigen Kompositionsrelation mit E8 überein. Das ist keine
Überprüfung aller Brackets der 248-dimensionalen Algebra, aller Stern-/
Adjungiertenbeziehungen oder ihres Transfers zur ursprünglichen Clock.
Die Normierung einer Fock-Mehrteilchenabbildung darf auch nach diesem
Vorzeichenanschluss nicht mit einer normierten Lie-Basis verwechselt werden.

### 3.2 Ein explizites zusammengesetztes Feld — mit Grenzen

Die Identität liefert natürliche endliche zusammengesetzte Operatoren

\[
\chi_r^\dagger=\frac1{\sqrt{15}}
\sum_{A,s}J_{r;As}b_A^\dagger f_s^\dagger.
\]

Die 64 Vektoren chi_r†|0> sind orthonormal und exakte Eigenvektoren von H
bei Energie Delta. Sie tragen die konjugierten Cartan-Gewichte. Ihre
fermionische Parität ist ungerade. **Ihre erhaltene Zahl N steigt aber um
drei, nicht um minus eins.** Aus konjugierten Gewichten folgt daher noch
keine Identifikation mit dem ursprünglichen Annihilationsfeld.

Die Schutzrelation ist zugleich eine Präparationsgrenze. Für den Projektor
P_chi auf diesen 64er-Raum gilt `P_chi exp(-iHt/hbar) P_f3=0` zu allen Zeiten.
Man kann ihn mit H allein nicht aus drei freien Fermionen und null Bosonen
erzeugen. Das gilt auch für Wörter mit der binären Bosonbesetzungsprojektion.
Der 35D-Transportzeuge aus Abschnitt 2 liegt dagegen ganz in den gekoppelten
lambda=7/12-Blöcken und wird dadurch nicht beseitigt. Für den 64er-Kompositraum
bleibt ein zulässiger Eingang oder eine zusätzliche, aus der Quelle abzuleitende
Präparationsoperation nötig; bloß seine Existenz schließt diese Lücke nicht.

Jede Zeile verwendet fünfzehn verschiedene Bosonkanäle. Auf dem endlichen
Teilchenkern folgen mit Cauchy–Schwarz und `0<=f†f<=1` die Schranken

\[
\|\chi_r\psi\|^2\le\langle\psi,N_b\psi\rangle,
\qquad
\|\chi_r^\dagger\psi\|^2
\le\langle\psi,(N_b+15)\psi\rangle.
\]

Insbesondere ist die Erzeugung aus einem festen N-Sektor durch
`sqrt(floor(N/2)+15)` beschränkt. Die expliziten Ausdrücke liefern dort
Adjungiertenpaarung und Abschließbarkeit auf dem gemeinsamen Teilchenkern.
Mit `H >= (Delta/2) Nb - 960g²/Delta` erhält man auch Kontrolle durch eine
verschobene Energieform. Das sind endliche Feld- und Domäneninformationen,
keine uniforme Kontinuumsrenormierung.

Eine wichtige Gegenprobe: Sowohl chi als auch chi† vernichten den vollständig
mit 64 Fermionen gefüllten Nullboson-Zustand. Ihr Antikommutator ist dort null,
also nicht die Identität. Es handelt sich **nicht um auf dem ganzen Fockraum
kanonische freie Fermionmoden**. Insbesondere ist T2 damit nicht geschlossen.

## 4. Warum „einfach eine positive Energie nehmen“ nicht genügt

Ein naheliegender Minimalversuch lautet

\[
H_+=\Delta\sum_A(b_A+\lambda P_A)^\dagger(b_A+\lambda P_A),
\qquad\lambda=g/\Delta.
\]

Dieser Operator ist positiv, aber er ist `H + (g²/Delta) sum P†P`, nicht
derselbe Hamiltonoperator mit verschobenem Energienullpunkt.

Weil alle reinen Paarannihilatoren miteinander kommutieren, gilt exakt

\[
|\Psi_\eta\rangle=
\exp[-\lambda\sum_A b_A^\dagger P_A]
\bigl(|0_b\rangle\otimes|\eta_f\rangle\bigr)
\in\ker H_+
\]

für jeden fermionischen Eingang eta. Der Exponentialausdruck ist wegen der
64 Fermionmoden ein endliches Polynom mit höchstens 32 Paarannihilationen.
Sein Nullbosonkoeffizient ist eta, also ist die Abbildung injektiv.

Umgekehrt wird jede Lösung der Bargmann-Gleichungen
`(d/dz_A+lambda P_A) Psi(z)=0` eindeutig durch ihren Wert bei z=0 bestimmt.
Da die P kommutieren und gemeinsam nilpotent sind, ist die obige endliche
Polynomform die gesamte Lösung. Daher

\[
\dim\ker H_+=2^{64},\qquad
\dim(\ker H_+\cap\mathcal H_N)=\binom{64}{N}\quad(0\le N\le64).
\]

Oberhalb von N=64 gibt es keine Nullzustände. Das ist ein analytischer Satz,
keine numerische Durchmusterung von 2^64 Zuständen. Ein unabhängig aufgebautes
Beispiel mit vier Fermionmoden, zwei überlappenden Paarkanälen und 96 Zuständen
prüft die gesamte Lösung, Rang und Ladungserhaltung exakt.

**Folge:** Positivität wählt keinen einzigen Eingang aus. Zudem ist die
Zeitentwicklung innerhalb des gesamten Nullraums die Identität. Die einfache
Quadratregel beschreibt hier einen großen geschützten Zustandsraum, aber
nicht von selbst einen ausgewählten dynamischen Grundzustand.

### 4.1 Die Zustandsgegenprobe kann sogar verschärft werden

Für H_mu=H+mu N und den bereits in v1.6 geprüften Casimirsatz
`sum P†P <= (15/2) Nf` ergibt Quadratvervollständigung mit Delta+2mu:

\[
H_\mu=(\Delta+2\mu)\sum_A
\left(b_A+\frac g{\Delta+2\mu}P_A\right)^\dagger
\left(b_A+\frac g{\Delta+2\mu}P_A\right)
+\mu N_f-\frac{g^2}{\Delta+2\mu}\sum_A P_A^\dagger P_A.
\]

Setze `mu_*=(sqrt(Delta²+60g²)-Delta)/4`. Dann ist H_mu* positiv und
`H_mu >= (mu-mu_*) N` für mu>mu_*. Bei g/Delta=1/20 und mu/Delta=1/50 folgt

\[
H_\mu\ge\left(\frac{27}{100}-\frac{\sqrt{115}}{40}\right)\Delta N.
\]

Der Koeffizient ist positiv und etwa 0,00190. Er verbessert die zuvor gültige
Schranke 1/800. mu_* ist eine **hinreichende Schwelle**, keine bewiesene exakte
Phasengrenze und kein abgeleiteter TFPT-Parameter.

Prüfkorrektur vor Auslieferung: Der zuerst ermittelte Fermionkoeffizient
41/20800 war im Entwurf unzulässig zu einer Gesamt-N-Schranke befördert worden.
Eine explizite Gegenprüfung des dafür benötigten Quadratresiduums liefert
`-123/1730560`. Der Bericht verwendet nur die oben bewiesene Gesamt-N-Schranke;
ein bleibender Regressionstest verhindert den früheren Schluss. v1.6 selbst
war von diesem Entwurfsfehler nicht betroffen.

## 5. Skalierung: was sich vollständig übertragen lässt und was nicht

Als getrennte, ausdrücklich bedingte Gegenrechnung wurden L Banken mit einem
vorgegebenen Bosonoperator B>=delta I untersucht. Diese Verbindung B wird
hier nicht aus dem Compiler hergeleitet. Die lokale W-Kopplung bleibt gleich.

Im gesamten N=2-Sektor bildet die helle Isometrie `V=W†/sqrt8` jeden
Eigenvektor von B mit Eigenwert epsilon auf zwei exakt bekannte Zweige ab:

\[
F_\pm(\epsilon)=\frac{\epsilon\pm\sqrt{\epsilon^2+32g^2}}2.
\]

Die restlichen `binomial(64L,2)-60L` Fermionpaarzustände sind dunkel, darunter
alle Paare mit einem Fermion in jeder von zwei verschiedenen Banken.
Auf dem vollen Fockraum gilt die extensive Stabilitätsschranke
`H >= -480g² L/delta`. Voraussetzung ist eine von L unabhängige positive
Untergrenze von B. Das ist keine Kontrolle aller Kontinuumskorrelationen.

Für translationsinvariantes B und k-unabhängiges V ist der hybride
Eigenvektor `(u(epsilon)V phi, v(epsilon)phi)` mit reellen normierten u,v.
Deshalb bleibt die Berry-Verbindung jeder isolierten Eigenlinie genau die
von phi; `u du + v dv=0`. Beide Ableitungen F' sind strikt positiv. Vorhandene
Weyl-Kreuzungen werden daher übernommen, nicht durch diese spezielle Kopplung
erzeugt oder beseitigt. Die Geschwindigkeiten erhalten unterschiedliche
Faktoren F'_+ beziehungsweise F'_-. Ein gemeinsamer Lichtkegel folgt nicht.

Diese Einschränkung ist wichtig: Andere Kopplungen mit momentumabhängiger
Phasenwindung können durchaus neue Topologie erzeugen. Ein konkretes
Primärbeispiel ist [Karzig et al., Topological Polaritons](https://arxiv.org/abs/1406.4156).
Die hier bewiesene Aussage betrifft nur die konstante Isometrie und den
flachen Fermionpaarblock, nicht beliebige Hybridmodelle.

Für eine gegebene Kette liegt der erste Paartransfer über Entfernung d in
Ordnung t^(d+2): zwei Konversionen plus d Vermittlerschritte. Das wurde für
2, 3, 4 und 7 Banken mit exakten Matrixpotenzen geprüft, ergänzt durch
separat als numerisch bezeichnete Spektralvergleiche. Bekannte
Atom-Molekül-Modelle verwenden ebenfalls Paar-Konversionsvertizes; diese
Analogie begründet keine TFPT-Herkunft. Siehe etwa
[Duan, Effective Hamiltonian … across Feshbach resonance](https://arxiv.org/abs/cond-mat/0508745).

## 6. Die jetzt sinnvollste minimale Fortsetzung

1. **Den nativen N=3-Feldkandidaten auf den tatsächlich gewählten Hintergrund
   setzen.** Zu berechnen sind gemeinsame Mehrzeitantworten mit H, chi und
   einem expliziten Eingang. Erfolg wäre ein quellenseitig zulässiger Zustand
   samt energetisch kontrollierter Feldantwort. Der leere Referenzzustand
   beweist weder Präparierbarkeit noch das physische Vakuum.
2. **Den E8-Vorzeichenanschluss auf Adjungierte und die wirkliche Clock
   ausdehnen.** Die jetzigen 1440 Koeffizienten sind ein konkreter Start;
   gefragt ist derselbe Adapter für die physische Sternoperation, die markierten
   Sektoren und die tatsächlichen Compilerkontrollen. Die Differenz zwischen
   Ladung +3 und -1 muss ausdrücklich aufgelöst werden, nicht nur modulo vier
   umbenannt werden.
3. **Innere Rekopplung und echten Ortstransport trennen.** Zuerst muss eine
   räumliche Erreichbarkeitsstruktur aus erlaubten gemeinsamen Moden oder
   Quelloperationen folgen. Für getrennte Banken verbietet die alte lokale
   Parität weiterhin den behaupteten einfachen Fermionhop. Ein frei gewähltes
   B ist nur eine bedingte Testumgebung.

Das Leitmotiv wird damit konkreter: **Die Anregung ist eine Änderung in einem
gemeinsam belegten System.** Die Quelle muss nicht erweitert werden, um den
hier nachgewiesenen inneren Rekopplungsprozess zu erhalten. Ob derselbe
Mechanismus auch physische Raumgeometrie trägt, ist nun die nächste scharfe
Frage — keine bereits bewiesene Schlussfolgerung.

## 7. T1–T8 und Evidenzgrenzen

| Tor | Beitrag dieser Runde | Weiterhin fehlend |
|---|---|---|
| T1 | Zwei aufeinanderfolgende E8-Bracket-Typen, Nullstellen und Vorzeichen gemeinsam geprüft | Auswahl von Quelle, Markierungen, Dimension und tatsächlichen Operationen |
| T2 | Expliziter konjugiert-gewichteter 64er-Kompositsektor, endliche Norm- und Adjungiertenkontrolle | Richtiger Half-Charge-/Clock-Anschluss, physischer Zustand, Renormierung und Grenzraum |
| T3 | Echte innere Zweivertex-Übergänge ohne neuen Hamiltonterm | Abgeleiteter lokaler räumlicher 3+1D-Träger |
| T4 | Kein neuer Nachweis eines chiralen Maßes | Anomalie-, Index- und Spiegelproblem im gemeinsamen Modell |
| T5 | Endliche exakte N=3-Lösung; bedingte extensive Mehrbank-Stabilität | Wechselwirkender Kontinuumsgrenzwert, Lorentzstruktur und Streuung |
| T6 | Keine neue Konstantenauswahl | Vollständige Eichkopplungs- und Neutrinostruktur |
| T7 | Kein dynamischer Spin-2-Nachweis | Masseloser quantisierter Spin 2 und universelle Kopplung |
| T8 | Positive-Quadrat- und chemische Gegenproben schärfer gelöst | Eindeutiges physisches Zustands-/Quellfunktional |

**Kein T1–T8-Tor wird als vollständig gelöst markiert.** Es gibt hier auch
keinen RH-, Faktorisierungs- oder P-versus-NP-Beweis und keine abgeleitete
Hylæan-Fähigkeit. Andere laufende Aufgaben wurden für diese Runde nicht neu
auditiert oder verändert.

## 8. Reproduktion und Lieferung

`replay.py` führt drei Prüfer normal und unter `-OO` aus, bewahrt jeden echten
Fehlerstatus und verlangt je Prüfer bytegleiche Berichte. Es speichert
`normal.json`, `native_three_normal.json`, `native_cubic_normal.json` sowie
die optimierten Gegenstücke und `replay_manifest.json`.

Die Fallzahlen sind Prüfbedingungen, nicht unabhängige Entdeckungen.
Die großen endlichen Spektren werden durch kleine Polynome zertifiziert;
die Voll-Fock-Nullraum- und Normsätze werden analytisch bewiesen und an einem
kleinen vollständigen Überlappungsbeispiel zusätzlich kontrolliert. Weder
eine formale Lean-Prüfung noch eine externe Begutachtung wurde durchgeführt.

Die Forschungsnotiz und ihre einfache Erklärung werden separat direkt nach
Documents kopiert. Die freigegebenen v1.6-PDFs werden nicht stillschweigend
durch einen kürzeren Forschungsbericht ersetzt. Kein Commit oder Push wurde
in dieser Runde vorgenommen.
