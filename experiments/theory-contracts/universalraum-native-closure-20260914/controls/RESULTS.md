# Feste Verstimmung genügt: endlicher phasenrichtiger Record-Compiler

14. September 2026. Eigene Fortsetzung zu T1/T8. **Bedingter Konstruktionssatz,
keine native TFPT-Schließung und keine TOE-Promotion.**

## Ergebnis in einem Satz

Der bisher zusätzlich verlangte Resonanzschalter Δ→0 und eine negative
Zeitentwicklung sind für den Austauschrecord nicht nötig: **festes Δ>0,
adressiertes An-/Abschalten der Kopplung, Belegungszugriff Q und berechenbare
positive Zeiten liefern eine endliche exakte 44-dimensionale Recordoperation.**
Bei t/Δ=1/20 dauert ihre geplante Hamiltonentwicklung genau 24πℏ/Δ. Damit kehren
auch unadressierte Vermittler mit derselben Verstimmung phasenrichtig zurück.

Das ist eine echte Reduktion des Ressourcenvertrags. An/aus-Steuerung, Q,
Zeitsteuerung und Reset werden dabei **nicht** als bereits native Quelle ausgegeben.

## 1. Quellenvertrag und bisheriger Engpass

Gelesen wurden die tatsächlichen Ressourcenlisten und Quellprüfungen in
`compiler-single-execution-20260914/README.md` und `check.py` sowie die
544D- und 44D-Konstruktionen aus `universalraum-five-source-frontier-20260914`.
Der zusätzliche Record lautet

\[
R=P_+\otimes I_2+P_-\otimes X,
\qquad P_\pm=(I\pm S)/2.
\]

Mit W†W=P− und WW†=I6 zerfällt der lokale Raum in zehn symmetrische Dunkelzustände
und sechs identische helle Materie-/Vermittlerblöcke. Der feste Hamiltonoperator ist

\[
H_{22}=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix},
\qquad g=\sqrt2\,t,
\qquad h=\begin{pmatrix}0&g\\g&\Delta\end{pmatrix}.
\]

Ein einzelner verstimmter Puls erreicht höchstens
4g²/(Δ²+4g²)=1/51 bei t/Δ=1/20. Reine additive Quell-Ladungsphasen sind auf beiden
Ladung-zwei-Alternativen skalar und ändern diese Schranke nicht.

Der vorhandene Belegungszugriff ist dagegen ausreichend für einen diskreten
Belegungs-Z-Kick: Ein Q-Aufruf auf einem separaten Pointer im Zustand |−> erzeugt
Zocc=I16⊕(−I6). Der Pointer bleibt |−> und kann für alle Kicks wiederverwendet werden.
Das ist **keine neue kontinuierliche Belegungsphasenoperation**, aber es setzt Q voraus.

Die allgemeine Möglichkeit endlicher Zerlegungen mit zwei Drehachsen ist bekannt;
hier wurde eine konkrete endliche Folge inklusive der vorher gefährlichen
Sektorphasen konstruiert, nicht nur eine Lie-Algebra-Erzeugbarkeit zitiert.
[Primärquelle zum allgemeinen Zerlegungsproblem](https://doi.org/10.1098/rsos.140145)

## 2. Exakte endliche Volltransferfolge

Setze

\[
\omega=\sqrt{\Delta^2+4g^2},\quad
\theta=\arctan(2g/\Delta),\quad
k=\lfloor\pi/(2\theta)\rfloor-1,\quad\beta=k\theta,
\]

mit 0<θ≤π/6. Die Blochachse des spurfreien Hamiltonoperators ist
n=(sinθ,0,−cosθ). Ein Puls der Dauer πℏ/ω, gefolgt von Zocc, bewegt den hellen
Eingang bis auf eine Gesamtphase um den halben Zustandswinkel θ. Nach k solchen
Paaren liegt er bei rβ=(sin2β,0,cos2β).

Es fehlen nur zwei berechenbare Pulswinkel a,b, mit einem Z-Kick dazwischen.
Für m=(−sinθ,0,−cosθ), u=n·rβ, v=m·rβ und d=m·n gilt

\[
\cos a=\frac{\cos\theta-du}{v-du}.
\]

Warum existiert a? Aus δ=π/2−β∈[θ,2θ) folgt
v=cos(2δ+θ)≤cosθ und 2du−v=cos(3θ−2δ)≥cosθ. Der benötigte Achsenwert liegt
also zwischen den Werten bei a=0 und a=π. Nach der ersten Rotation und Z-Kick
besitzt r1 dieselbe n-Komponente wie der Südpol s=(0,0,−1). Deshalb setzt

\[
b=\operatorname{atan2}\bigl(n\cdot(r_1\times s),\;
r_1\cdot s-\cos^2\theta\bigr)\pmod{2\pi}
\]

den Zustand durch eine zweite positive Rotation exakt auf den Südpol. Die Folge U
hat somit n_p=k+2 On-Pulse und n_p−1 Z-Kicks. Sie vertauscht den gesamten
sechsdimensionalen hellen Raum mit dem Vermittlerraum; die symmetrischen Zustände
bleiben unverändert. Alle relativen Farben und verschränkten Zuschauer werden
dabei mitgenommen, nicht einzeln kalibriert.

Bei t/Δ=1/20:

| Größe | Wert |
|---|---:|
| θ | 0.14048970175352038 |
| k; Zahl n_p der Vorwärtspulse | 10; 12 |
| Winkel a | 2.6666937662941215 |
| Winkel b | 5.613297586629477 |
| Dauer eines der zehn Standardpulse | 3.1106402469855037 ℏ/Δ |
| Dauer der beiden Schlusspulse | 2.640420280567338; 5.557992813398072 ℏ/Δ |
| gesamte Vorwärts-On-Zeit | 39.30481556382045 ℏ/Δ |

Dies ist eine analytisch definierte Folge. Die Gleitkommawerte dienen der
Ausführungskontrolle; ihre Dezimalschreibweise ersetzt nicht die exakten Definitionen.

## 3. Positives Rückrechnen: die Sektorphase muss bezahlt werden

Auf einem hellen Zweierblock gilt für T=2πℏ/ω

\[
e^{-ih(T-\tau)/\hbar}
=e^{i\pi(1-\Delta/\omega)}e^{+ih\tau/\hbar}.
\]

Wird jede Vorwärtszeit τ in umgekehrter Operationsreihenfolge durch T−τ ersetzt,
entsteht eine physisch positive Rückfolge V. Die Z-Kicks sind selbstinvers.
Auf dem gesamten 22D-Raum gilt **nicht** einfach V=U†, sondern

\[
V=D_{\rm act}(\gamma)U^\dagger,
\quad \gamma=n_p\pi(1-\Delta/\omega),
\quad D_{\rm act}(\gamma)=P_++e^{i\gamma}(P_-+P_{\rm med}).
\]

Bei t/Δ=1/20 ist γ=0.3714288792514706. Die unkorrigierte Makrooperation VQU
verfehlt R⊕I um 0.36929747025993703 in Operatornorm. Dieser Fehler wird im Prüfer
absichtlich erzeugt; er darf nicht als unsichtbare globale Phase verschwinden.

Wenn alle adressierten Kopplungen für eine positive Wartezeit abgeschaltet werden
können, liefert derselbe feste Detuningterm ohne neue Spektraloperation

\[
A=e^{-i(\gamma/\Delta)(\Delta P_{\rm med})}
=P_{\rm mat}+e^{-i\gamma}P_{\rm med}.
\]

Nun ist die vollständige Folge, von rechts nach links gelesen,

\[
\boxed{\;V\,A\,Q\,U\,A
\;=\;(P_+\otimes I+P_-\otimes X)\oplus I_{12}.\;}
\]

Der erste A-Puls korrigiert einen möglichen Vermittlereingang. Der zweite
korrigiert den nach U dorthin transportierten antisymmetrischen Materiezweig.
Darum gilt die Identität auch für beliebige anfängliche Pointerzustände und
nicht nur für den ausgewählten Erfolgszweig. Für bereits nackte Materie wäre die
erste Korrektur redundant; wir behalten sie, um den gemeinsamen Vollraumvertrag
zu erhalten.

Besonders einfach wird die Zeitsumme:

\[
T_{\rm evo}
=n_p\frac{2\pi\hbar}{\omega}+\frac{2\gamma\hbar}{\Delta}
=\boxed{\frac{2\pi n_p\hbar}{\Delta}}.
\]

Für n_p=12 sind das **24πℏ/Δ=75.39822368615503 ℏ/Δ**. Deshalb erhalten alle
unadressierten Vermittler mit gleicher Verstimmung Δ über die ganze Folge die
Phase exp(−iΔT_evo/ℏ)=1. Das bewahrt den vorhandenen gemeinsamen 832D-Träger:
die ausgewählte Kante realisiert ihren Record, andere Vermittlersektoren bleiben
am Ende phasenrichtig unverändert. Voraussetzung ist derselbe Detuningwert in
diesen Sektoren; beliebige Splitter der Vermittlerenergien sind nicht eingeschlossen.

## 4. Ressourcen und Fehler: der Bedienteil ist kleiner, nicht verschwunden

Eine vollständige Record-Makrooperation benötigt bei 1/20:

- 24 positive On-Pulse mit derselben nichtverschwindenden Kopplung t;
- zwei Off-Intervalle von je 0.3714288792514706 ℏ/Δ;
- 22 diskrete Belegungs-Z-Kicks, realisiert durch 22 Q-Aufrufe auf |−>;
- einen weiteren Q-Aufruf auf dem tatsächlichen Recordpointer;
- einen wiederverwendbaren Helperpointer und den Recordpointer;
- adressiertes t-an/aus und genaue Zeit-/Kantensteuerung.

**Die 23 Q-Aufrufe haben nicht null physische Kosten.** Die exakte Zeitformel
zählt die vorgeschriebenen Hamilton-Evolutionsintervalle im idealen Kickmodell,
nicht deren unbekannte Gatezeiten, Controllerenergie oder die Dauer der
An-/Abschaltflanken. Endlich dauernde Q-Pulse benötigen einen kontrollierten
Implementierungsvertrag; sonst wirken Drift und Kopplung während der Gates
zusätzlich. Die behauptete feste Gesamtphase darf dann nicht unverändert übernommen
werden. Das gilt ebenso für Pointerpräparation, Messung und Reset.

**Dieser endliche Gatevertrag lässt sich zusätzlich explizit schließen.** Während Q
wird t=0 geparkt. Besitzt die Q-Realisierung einen belegungserhaltenden Generator,
kommutiert sie mit ΔPmed. Eine mögliche, ausdrücklich zusätzlich gewählte
Realisierung ist H_Q=πℏ(I−Q)/(2τ_Q); dann gilt exp(−iH_Q τ_Q/ℏ)=Q.
Verlängere das Q-Zeitfenster durch freies Parken auf

\[
T_Q=\frac{2\pi m_Q\hbar}{\Delta},\qquad
m_Q=\left\lceil\frac{\Delta\tau_Q}{2\pi\hbar}\right\rceil.
\]

Die Drift liefert über dieses Fenster die Identität, und das Q-Gatter bleibt
erhalten. Es wird keine Nullzeit vorausgesetzt. Die vollständige Makrozeit ist nun

\[
T_{\rm macro}=\frac{2\pi\hbar}{\Delta}
\left(n_p+\sum_{j=1}^{23}m_{Q,j}\right).
\]

Für τQ=ℏ/Δ pro Gatter reichen mQ=1 und deshalb **Tmacro=70πℏ/Δ
=219.9114857512855 ℏ/Δ**, einschließlich aller 23 Q-Fenster. Die gesamte 88D-Folge
mit tatsächlichem Record und wiederverwendetem |−>-Helper wurde mit diesen
endlichen Gatter-Hamiltonoperatoren aufgebaut; ihr Abweichungsrest vom gewünschten
Record samt unverändertem Helper beträgt 9.70·10⁻¹⁵. Die Zuschauerphasen schließen
weiterhin exakt. Die Wahl von H_Q ist ein konkreter zusätzlicher physischer
Gatevertrag, kein Herkunftsbeweis aus TFPT. Nichtinstantane Schaltflanken bleiben
ebenfalls zu modellieren.

Eine einfache Duhamel-/Hybridabschätzung für ideale Basisgatter ist

\[
\|\widetilde R-R\|\le
\frac{T_{\rm evo}}\hbar\delta H
+\frac{24\|h\|+2\Delta}{\hbar}\delta\tau
+23\epsilon_Q,
\]

mit einheitlicher On-/Off-Hamiltonabweichung δH, maximalem Timingfehler δτ
pro geplantem Evolutionssegment und Operatorfehler εQ pro Q-Aufruf. Helperfehler
und Umschalttransienten kommen gesondert hinzu. Bei 1/20 ist der Timingkoeffizient
26.119405926034496 Δ. Wenn ausschließlich δH fehlerhaft ist, genügt
δH≤1.3262911924324612·10⁻⁵Δ für Zustandsinfidelität höchstens 10⁻⁶ eines Recordaufrufs.
Das ist keine Gesamtfehlergarantie für viele postselektierte Versuche.
Beim endlichen Q-Fenstervertrag ist stattdessen Tmacro einzusetzen und dessen
Timingfehler sind mitzuführen. Bei ausschließlich gleichmäßig begrenztem δH
genügt dann konservativ δH≤10⁻³/(70π) Δ≈4.55·10⁻⁶Δ.

**Wenn t niemals abgeschaltet werden darf, ist dieser exakte Abschluss nicht
bewiesen.** Die gewählte Ganzperioden-Rückfolge plus alleinige Clifford-Belegungsphasen
kann ihre Restphase bei 1/20 nicht exakt entfernen: Δ/ω=10/√102 ist irrational.
Das ist eine Obstruktion dieser Folge, kein Ausschluss aller möglichen Kompositwörter.
Ein positiver Rekurrenzersatz ohne Off-Phasen erreicht mit 8.241.802 vollen Perioden
einen Phasenfehler 7.55·10⁻⁷, kostet aber ca. 5.127·10⁷ ℏ/Δ. Das ist ein endlicher,
absichtlich unattraktiver Fallback, weder Effizienzbeweis noch native Ableitung.

## 5. Präparation und Mehrzeitantwort ohne kontrollierten H-Spektralfilter

Weil die neue Makrooperation genau denselben R erzeugt, lässt sich die ursprüngliche
gemeinsame Compiler-Ausführung jetzt mit **festem Δ** anschließen:

1. einfacher Quellzustand |0,1,2,3>;
2. N Sternrunden mit den Records 01,02,03, akzeptiert wird jeweils 111;
3. der tatsächliche lokale C3-Quelltick, zwei gleiche oder zwei frische Records;
4. inverser C3-Tick und dasselbe N-Runden-Filter;
5. bei fehlgeschlagener Präparation vollständiger Reset und neuer Versuch.

K=P−03 P−02 P−01 und K^N sind dabei unverändert. **Anders als beim 544D-Spektralfilter
benötigt diese Variante weder kontrolliertes exp(−iHτ) noch die 14 bekannten
Sternenergien.** Dafür ist die Präparation bei endlichem N nur kontrolliert
angenähert. Das alte Spektralfilter wird nicht als falsch oder wertlos verworfen;
es bleibt eine andere, unter stärkeren Kontrollen exakt selektive Variante.

Die neue Rechnung verwendet exakte Brüche auf den tatsächlichen vierfarbigen
Wörtern, einschließlich wiederholter Farben nach dem C3-Tick. Rohwahrscheinlichkeiten
und Abbruchkosten wurden neu berechnet:

| Sternrunden N | Infidelität der tatsächlichen Präparation | frische bedingte Rückkehr | mittlere Recordaufrufe bis zur erfolgreichen Präparation |
|---|---:|---:|---:|
| 8 | 7.5512047993·10⁻⁷ | 0.5312581678314172 | 66.7916146523 |
| 12 | 2.2418477182·10⁻¹⁰ | 0.5312504083796606 | 78.7916666486 |
| 20 | 1.2233966909·10⁻¹⁷ | 0.5312499999780164 | 102.7916666667 |
| 40 | 9.8290407971·10⁻³⁶ | 0.53125 bis auf ca. −1.52·10⁻²⁰ | 162.7916666667 |

Bei N=20 sind durchschnittlich nahezu 24 Präparationsversuche erforderlich.
Die Zahl der Recordaufrufe ist nicht 24×60: Fehlgeschlagene Versuche brechen früh
ab. Genau gilt mit den Zwischen-Erfolgsgewichten p_j

\[
\mathbb E[N_{\rm Records,prep}]
=\frac{\sum_{j=0}^{3N-1}p_j}{p_{3N}}.
\]

Mit anschließend höchstens 2+3N Recordaufrufen für Echo und Schlussfilter beträgt
die mittlere geplante Evolutionszeit für N=20 höchstens 12424.998944947632 ℏ/Δ,
zuzüglich sämtlicher Q-/Controller-/Mess-/Resetzeiten. Das ist eine ausführbare
Ressourcenbilanz im erklärten Modell, kein Nullkosten-Attraktor.
Mit den oben konstruierten endlichen Q-Fenstern steigt dieselbe Obergrenze auf
36239.58025609726 ℏ/Δ; Q ist dann bereits enthalten. Umschalttransienten,
Pointerpräparation, Messungen, Reset und übriger Controller bleiben zusätzlich.

Die Gesamterfolgsgewichte pro gestartetem Versuch bleiben im Grenzwert 1/24
(erhaltener Record) und 17/768 (frischer Record). Der Quotient der bedingten
Grenzwerte ist 17/32. Die sehr hohe ideale N=20-Fidelität berücksichtigt keine
experimentellen Fehler; diese akkumulieren zusätzlich und werden durch eine
Konditionierung auf seltene Erfolge im ungünstigen Fall verstärkt.

## 6. Gemischte Gramprüfung und verbleibendes Herkunftstor

Die Konstruktion ist eine einzige unitäre Vollraumoperation. Deshalb erhält sie
alle Skalarprodukte nicht nur innerhalb eines einzelnen Zweiges, sondern auch
zwischen den gemeinsam realisierten Wörtern. Numerisch wurde zusätzlich die
gemischte Grammatrix der Worte I, R, R² auf zwölf komplexen 44D-Eingängen mit
beliebigen Pointerzuständen geprüft. Rest: 2.73·10⁻¹⁴. Eine eigenmächtige relative
Phase nur des mittleren Wortes lässt dessen interne Grammatrix unverändert,
verletzt aber diese gemeinsame Grammatrix; die Negativkontrolle erkennt sie.

Der volle Matrixvergleich ergab 1.10·10⁻¹⁴ Operatorrest. Der Guard-Prüfer umfasst
**88 Bedingungen**, einschließlich rationaler Prozessrechnungen, endlicher
Q-Zeitfenster auf 88 Dimensionen und negativer
Kontrollen. Normal und Python -OO erzeugten bytegleiche Ergebnisdateien.
Die analytischen Transfer-/Phasenidentitäten stehen oben; numerische Residuen
allein werden nicht als exakte Beweise ausgegeben.

Die verbleibenden wesentlichen Fragen sind jetzt enger:

1. Liefert die ursprüngliche Quelle überhaupt die nichtstabilisierende
   Wedge-Kopplung und den kohärenten Belegungszugriff Q?
2. Kann derselbe Controller die Kantenwahl und t-an/aus mit den erforderlichen
   Zeiten realisieren, einschließlich seiner eigenen Dynamik und Energie?
3. Wie werden Pointer, Reset und abgespeicherte Resultate physisch angeschlossen,
   ohne eine externe Mess-/Thermodynamikmaschine stillschweigend hinzuzufügen?
4. Wie verträgt sich diese lokale programmierte Ausführung mit der gekoppelten
   Vielzellenfamilie und deren lokalen Fehlergrenzen?

Clifford-/Stabilizeroperationen allein bleiben unzureichend: R bildet einen
quellseitigen Stabilizereingang auf einen Zustand mit 13 Rechenbasisamplituden ab.
Das Herkunftsproblem kann daher nicht durch bloßes Umbenennen dieser zusätzlichen
Kopplung oder von Q gelöst werden. **Die jetzige Konstruktion entfernt unnötige
Kontrollen; sie erfindet keine native Herkunft.**

## Reproduktion

`verify_controls.py` importiert keine fremden Forschungsprüfer. Benötigt werden
NumPy, SciPy und SymPy. `verification.json` und `verification_optimized.json`
enthalten vollständige Pulsfolgen, Ressourcen, exakte rationale Rohwerte,
Quellhash und Scope-Felder. Der Prüfer schreibt seine Ergebnisdatei selbst;
Assertions werden nicht verwendet.
