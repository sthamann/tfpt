# Exakter kausaler Eingriff am unveränderten nativen Hamiltonoperator

## Ergebnis

Im ursprünglichen TFPT-Modell gibt es einen vollständig gelösten kausalen
Test innerhalb des Ladungssektors N=2. Ein Phasenimpuls an Fermionmode 4
ändert die spätere unbedingte Besetzung von Mode 5. Die beiden Observablen
kommutieren vor der Entwicklung. Der Impuls erhält die Ladung und wirkt nur
auf Mode 4; es gibt keine Konditionierung auf Messergebnisse.

Der stärkste hier bewiesene Vergleich endet in **beiden** Armen mit genau
zwei Fermionen und keinem Boson. Gemessen wird eine andere Verteilung der
Fermionen auf disjunkte Paare. Die natürliche Entwicklung zwischen Eingriff
und Messung verwendet ausschließlich das ursprüngliche H und W.

**Bedingung:** Die Präparation des angegebenen Produktzustands, ein gezielter
Phasenimpuls und die einzelne Besetzungsmessung werden als Instrumente
gewährt. Ihre physische Verfügbarkeit aus dem ursprünglichen Operationssatz
ist hier nicht hergeleitet. Der Impuls ist eine ausdrücklich hinzugewährte
Kontrolloperation; er wird nicht als von der ungestörten H-Entwicklung
bereitgestellt ausgegeben. Es wurde kein zusätzlicher Hopping- oder
Linkterm in die freie Dynamik eingeführt.

Das Ergebnis betrifft Moden innerhalb derselben Bank. Es enthält weder eine
räumliche Metrik noch den bereits untersuchten N=64-Grundzustand oder dessen
geladenen Entnahmepol.

## 1. Quelle und vollständiger invarianter Sektor

Die eingefrorene Quelle ist `sources/spinor_tensors.npz` mit SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Es gilt unverändert

\[
H=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad N=N_f+2N_b.
\]

W besitzt 60 Zeilen, 2016 Spalten und 480 Einträge mit Wert ±1.
Jede aktive Spalte gehört genau einer Zeile. Jede Zeile enthält acht
Fermionenpaare mit insgesamt sechzehn verschiedenen Moden. Deshalb zerfällt
der **gesamte** N=2-Sektor in 60 invariante neundimensionale Blöcke und
1536 vollständig dunkle Paarzustände. Die sieben dunklen Richtungen innerhalb
jedes Blocks kommen zusätzlich hinzu: insgesamt bleibt die bekannte dunkle
Dimension 1536+60·7=1956.

Eine solche Gruppe besteht aus einem Boson und acht Paaren. Mit
\(|p_\ell\rangle=f_{i_\ell}^\dagger f_{j_\ell}^\dagger|0\rangle\),
\(s_\ell=W_{A,i_\ell j_\ell}\) und
\(|S\rangle=\sum_\ell s_\ell|p_\ell\rangle/\sqrt8\) gilt

\[
H_A=\begin{pmatrix}0_{8\times8}&g s\\g s^T&\Delta\end{pmatrix},
\qquad H_A|_{\operatorname{span}(S,b_A)}=
\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}.
\]

Die CAR-Vorzeichen wurden für alle 480 aktiven Paare separat geprüft.
Dies ist eine exakte Einschränkung auf einen invarianten Sektor, keine
Abschneidung höherer Bosonstufen.

Die benutzte Zeile A=0 lautet:

| Blatt | Fermionenpaar | Vorzeichen |
|---:|---|---:|
| 0 | (4,57) | −1 |
| 1 | (5,56) | +1 |
| 2 | (8,53) | +1 |
| 3 | (9,52) | −1 |
| 4 | (16,45) | −1 |
| 5 | (17,44) | +1 |
| 6 | (28,33) | +1 |
| 7 | (29,32) | −1 |

## 2. Lokale Algebra und ehrlicher Interventionstest

Die Senderoperation ist

\[
Z_4=(-1)^{n_4}=I-2n_4,\qquad
\mathcal E_4(\rho)=Z_4\rho Z_4^\dagger.
\]

Sie hat genau einen unitären Krausoperator und ist daher vollständig positiv
und spurerhaltend. Sie ist fermionparitätsgerade und erhält N. Auf der ganzen
Fock-Algebra kommutiert sie mit allen disjunkten Modenoperatoren; insbesondere
\([Z_4,n_5]=0\). Ihre Einschränkung auf den ausgewählten Block wechselt allein
das Vorzeichen des Blattes (4,57). Diese Einschränkung wurde gegen den
wirklichen Operator \((-1)^{n_4}\) auf allen 2076 N=2-Basiszuständen geprüft.

Der Empfänger liest \(B=n_5\) aus. Im gewählten invarianten Block ist dies
der Projektor auf Blatt (5,56). Die Operation enthält keinen Verweis auf
Mode 5. Zu ihrem Zeitpunkt bleibt dessen gesamte Besetzungsstatistik für
jeden Zustand identisch, weil \(Z_4^\dagger n_5 Z_4=n_5\).

Mit \(\rho_T=U_T|p_0\rangle\langle p_0|U_T^\dagger\) ist die gemessene
Differenz genau

\[
\delta_{4\to5}(T)=
\operatorname{tr}\!\left[n_5U_T\mathcal E_4(\rho_T)U_T^\dagger\right]
-\operatorname{tr}\!\left[n_5U_T\rho_TU_T^\dagger\right].
\]

Das ist ein Vergleich von unbedingten Wahrscheinlichkeiten nach einem
kontrollierten lokalen Eingriff. Eine Zweipunktkorrelation wird dafür nicht
als Ersatz benutzt. Die vor dem Impuls erzeugte Kohärenz wird ausdrücklich
durch die native Vorentwicklung präpariert. Ein Phasenimpuls direkt auf
dem anfänglichen Produktzustand hätte nur ein globales Vorzeichen und
überhaupt keinen Effekt; diese Negativkontrolle wird ebenfalls geprüft.

## 3. Exakter Test mit gleicher Endzusammensetzung

Setze für \(\Delta>0\) und reelles \(g\ne0\)

\[
\Omega=\sqrt{\Delta^2/4+8g^2},\quad
T=\frac\pi\Omega,\quad d=\frac\Delta{2\Omega},\quad
z=-e^{-i\pi d},\quad
x=|z-1|^2=4\cos^2\frac{\pi d}{2}.
\]

Nach T wirkt der helle Zweizustandsblock als z mal Identität; die dunklen
Paarzustände bleiben unverändert. Es gibt dann für **jede** anfängliche
Paarkombination keine Bosonamplitude. Auf der Paarseite ist

\[
U_T^{(f)}=I_8+(z-1)|S\rangle\langle S|.
\]

Beide Arme beginnen in demselben vollständig angegebenen Produktzustand
\(|p_0\rangle=f_4^\dagger f_{57}^\dagger|0\rangle\), alle anderen
Moden leer. Sie unterscheiden sich nur durch den mittleren Phasenimpuls:

\[
\begin{array}{lll}
\text{unberührt:}&U_T\;I\;U_T|p_0\rangle,&\text{danach }n_5,\\
\text{Eingriff:}&U_T\;Z_4\;U_T|p_0\rangle,&\text{danach }n_5.
\end{array}
\]

Für jedes andere Blatt q sind die exakten Endamplituden

\[
\langle p_q|U_T^2|p_0\rangle
=s_0s_q\frac{z^2-1}{8},\qquad
\langle p_q|U_TZ_4U_T|p_0\rangle
=s_0s_q\frac{3(z-1)^2}{32}.
\]

Damit lautet insbesondere die unbedingte Empfängerwahrscheinlichkeit

\[
p_{\rm frei}(n_5=1)=\frac{x(4-x)}{64},\qquad
p_{\rm Impuls}(n_5=1)=\frac{9x^2}{1024},
\]

und die kausale Differenz ist

\[
\boxed{\delta_{4\to5}(T)=\frac{x(25x-64)}{1024}}.
\]

Für \(0<g^2\le3\Delta^2/32\) gilt \(1/2\le d<1\), also
\(0<x\le2\) und folglich **strikt \(\delta_{4\to5}<0\)**. Das ist eine
exakte endliche Zeit, kein unkontrollierter Schluss aus einer numerisch
kleinen Antwort oder einer asymptotischen Reihe. Außerhalb dieses Intervalls
gilt weiterhin die exakte Formel, kann aber auch das Vorzeichen wechseln
oder an x=64/25 verschwinden.

Am bisherigen Prüfpunkt \(\Delta=1,g=1/20\) ist
\(d=5/(3\sqrt3)\) und \(T\approx6.0459978807807\):

| Größe | Wert |
|---|---:|
| Ohne mittleren Impuls | 0.00087491599417248 |
| Mit mittlerem Impuls | 0.0000017344871305812 |
| Differenz | −0.00087318150704190 |
| Endbesetzung in beiden Armen | Nf=2, Nb=0 exakt |

Die Wellenfunktion kann zwischen den Ablesezeiten einen Boson enthalten.
Das natürliche H vermittelt dadurch die Umverteilung von einem
Fermionenpaar in andere. Die Endmessung benötigt keine Selektion auf
„kein Boson“: Dieser Zustand gilt in beiden Armen mit Wahrscheinlichkeit eins.

## 4. Zwei ergänzende Kontrollen

### Boson als einfachere Referenz

Ausgehend vom Produktzustand \(b_0^\dagger|0\rangle\) wähle die beiden
Verzögerungen \(\tau=\pi/(2\Omega)\). Der unberührte Arm kehrt exakt
zum Boson zurück, also \(p_{\rm frei}(n_5=1)=0\). Ein mittleres Z4 erzeugt

\[
p_{\rm Impuls}(n_5=1)
=\frac{(1-d^2)\left[1+d^2-2d\sin(\pi d/2)\right]}{128}
\ge\frac{(1-d^2)(1-d)^2}{128}>0.
\]

Dies gilt für jedes \(g\ne0\) und \(\Delta>0\). Auch dieser Test ist
ladungserhaltend und unbedingt. Er hat allerdings unterschiedliche
Fermion/Boson-Zusammensetzungen am Ende; für die stärkere Aussage über reine
Paarumverteilung wird deshalb der Test aus Abschnitt 3 benutzt.

### Lokales Auffüllen und kurze Zeiten

Auf der Referenz \(f_{57}^\dagger|0\rangle\) füllt das lokale CPTP-Instrument
mit Krausoperatoren \(n_4,f_4^\dagger\) Mode 4. Ohne Eingriff ist der
Einfermionzustand stationär. Mit Eingriff entsteht \(|p_0\rangle\), woraus

\[
\delta n_5(t)=\frac{|a(t)-1|^2}{64},\qquad
a(t)=e^{-i\Delta t/2}\left[\cos\Omega t+i d\sin\Omega t\right].
\]

Die führenden Beiträge sind
\(\delta n_5(t)=g^4t^4/4+O(t^6)\) und
\(\delta N_{b_0}(t)=g^2t^2+O(t^4)\).
Der Pfad in ein anderes Fermionenpaar hat somit zwei native H-Anwendungen
in der Amplitude; die erste Umwandlung zum Boson hat eine.

Dieses Auffüllen tauscht eine Ladungseinheit mit einem angenommenen Reservoir
aus. Es wird nicht als zahlenerhaltende Operation ausgegeben und ist für den
Hauptnachweis nicht erforderlich.

## 5. Prüfung und unveränderte offene Grenze

`verify_causal.py` benutzt explizite Fehlerbedingungen, keine abschaltbaren
Assertions. Normaler Python-Lauf und `python -OO`, jeweils mit Warnungen als
Fehler, erzeugen byte-identische JSON-Ergebnisse. Der optimierte Lauf wurde
aus einem anderen Arbeitsverzeichnis gestartet; die Quelle wird relativ zum
Prüfprogramm aufgelöst. Abhängigkeiten: NumPy, SymPy und SciPy.

Die symbolischen Identitäten und die vollständige W-Struktur werden exakt
geprüft. Zusätzlich läuft ein unabhängiger numerischer Vergleich auf dem
vollen 2076-dimensionalen N=2-Hamiltonoperator, direkt aus W aufgebaut.
Er bestätigt beide vollständigen Endzustände, die Wahrscheinlichkeiten,
Normerhaltung, verschwindende Bosonamplituden und die Negativkontrolle.
Der abschließende Lauf enthält **662 exakte und 10 numerische Prüfbedingungen**.
Prüfzahlen und Quellhash stehen in `result.json`; `result_OO.json` ist dessen
identischer optimierter Replay. Beide Ergebnisdateien haben SHA-256
`b37ae758117e4c35d1063e76756cd6a39f133c964d331a9d400e67a0b157a4a6`.

**Geschlossen:** Im ausdrücklich gewährten Instrumentenvertrag existiert am
selben ursprünglichen H ein kausaler Moden-zu-Moden-Eingriff. Ein weiteres
Hopping-Glied ist für diesen N=2-Zeugen mathematisch nicht notwendig. Reine
Paarumverteilung wird am Endzeitpunkt getrennt von Speziesumwandlung bewiesen.

**Weiter offen:** Auswahl und Präparation dieses N=2-Referenzzustands,
ausführbare einzelne Modenphasen und Besetzungsinstrumente aus dem nativen
Operationssatz; Anschluss an den N=64-Grundzustand und dessen geladenen Pol;
Interpretation der Modenalgebren als räumlich unabhängige Labore; Distanz,
Raumdimension, endliche Ausbreitungsgeschwindigkeit und gemeinsame Raumzeit.
Die bloße Tatsache, dass ein Kontrolloperator zur mathematischen Fock-Algebra
gehört, schließt diese Operationsfrage nicht.
