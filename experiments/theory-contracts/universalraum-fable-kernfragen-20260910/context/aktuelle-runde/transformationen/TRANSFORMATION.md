# Eine ausführbare Verbindung: Restklasse → Orbit → Spektrum → Faktor

10. September 2026. **Der Baustein funktioniert vollständig aus der Eingabe N=91: Eine ohne Faktoren oder Ordnung konstruierte Viereruhr wird exakt Fourier-transformiert, um eine halbe Umdrehung entwickelt und zurückgelesen. Das ergibt die Restklasse 64 und daraus die Faktoren 7 und 13.** Die notwendige Suche nach dieser Uhr wird ausdrücklich gezählt. Es liegt keine neue polynomiale Faktorisierungsmethode vor.

## 1. Die Transportidentität für beliebiges N

Für `gcd(a,N)=1` wirkt auf `H_N=C^N`

\[
U_a|x\rangle=|ax\bmod N\rangle,\qquad
F_N|x\rangle=N^{-1/2}\sum_{k=0}^{N-1}e^{2\pi ikx/N}|k\rangle.
\]

**Exakt gilt** `F_N U_a F_N†=U_(a⁻¹)`. Denn `F_N U_a|x>` hat den Koeffizienten `exp(2πikax/N)/√N` an k; denselben Koeffizienten hat `U_(a⁻¹)F_N|x>`. Die additive Fouriertransformation permutiert somit die Charaktere mit dem inversen Multiplikator. Sie diagonalisiert eine allgemeine Multiplikation **nicht**. Für `N=91,a=2` ist `a⁻¹=46 mod 91`.

Die diagonalisierten Objekte erhält man aus dem **multiplikativen Orbit**. Beginne ausdrücklich mit `|1>`. Ist `r=ord_N(a)`, dann sind die r Zustände `|a^j>` verschieden. Die Isometrie `J_r|j>=|a^j>` erfüllt

\[
J_r^\dagger U_aJ_r=S_r,\qquad
F_rS_rF_r^\dagger=\operatorname{diag}(e^{2\pi is/r})_{s=0}^{r-1}.
\]

Dabei verschiebt `S_r|j>=|j+1 mod r>`. Die Eigenzustände sind

\[
|\psi_s\rangle=r^{-1/2}\sum_j e^{-2\pi isj/r}|a^j\rangle,
\quad P_s=\frac1r\sum_{j=0}^{r-1}e^{-2\pi isj/r}U_a^j.
\]

Auf dem Startzustand hat jeder Spektralprojektor das Gewicht `||P_s|1>||²=1/r`. Der kleinste gemeinsame Nenner sämtlicher Eigenphasen in gekürzter rationaler Form ist r. Das folgt direkt aus der enthaltenen Phase `1/r`. Wer klassisch alle diese Phasen aus der vollständigen Orbitbasis herstellt, hat allerdings schon r Schritte bezahlt. `|0>` oder die uniforme Superposition aller Restklassen wären ungeeignete Starts: Beide sind unter jeder solchen Multiplikation unverändert und liefern nur die Phase null.

## 2. Eine Viereruhr lässt sich hier ohne vorher bekannte Ordnung finden

Der zweite, unabhängige Konstruktor verwendet nur N, die feste öffentliche Basis `a=2` und die vorab gesetzte Suchgrenze 64. Er testet nacheinander `b=a^t mod N` auf `b⁴=1` und `b²≠1`. Der Rückgabestatus nach erschöpfter Suche ist ausdrücklich unentschieden.

Für N=91 ergibt die ausgeführte Suche:

| t | b | b² mod N | b⁴ mod N | Ergebnis |
|---:|---:|---:|---:|---|
| 1 | 2 | 4 | 16 | Keine Viereruhr |
| 2 | 4 | 16 | 74 | Keine Viereruhr |
| 3 | 8 | 64 | 1 | Exakte Viereruhr |

Somit ist `C=U_8` von Ordnung vier. Ihr Orbit auf `|1>` lautet `(1,8,64,57)`. Mit der vollständig bekannten Einbettung `J_4|j>=|(1,8,64,57)_j>` ergibt sich der tatsächliche Rechenweg

\[
|0\rangle\xrightarrow{F_4}\tfrac12(1,1,1,1)
\xrightarrow{\operatorname{diag}((-1)^s)}\tfrac12(1,-1,1,-1)
\xrightarrow{F_4^\dagger}|2\rangle
\xrightarrow{J_4}|64\rangle.
\]

Die mittlere Operation ist genau eine halbe Umdrehung `C²`. Der Reader liefert

\[
\gcd(64-1,91)=7,\qquad\gcd(64+1,91)=13.
\]

**Warum dieser Reader korrekt ist:** Für ein ungerades N und ein `h²=1 mod N` mit `h≠±1 mod N` sind `gcd(h−1,N)` und `gcd(h+1,N)` nichttriviale Faktoren. Wäre einer der ggT gleich eins, müsste der andere Term durch N teilbar sein; das widerspräche `h≠±1`. Beide dürfen daher weder eins noch N sein. Die Konstruktion prüft diese Ausnahmen tatsächlich. Die Bedingung `b⁴=1,b²≠1` allein erlaubt noch `b²=−1`; dann liefert diese Uhr keinen Faktor.

Erst **nach** dem Fund erklärt die lokale Zerlegung das Geschehen: `64≡1 mod7`, aber `64≡−1 mod13`. Die halbe Umdrehung wirkt auf den beiden unbekannten lokalen Komponenten verschieden. Modulo N konnten wir diese gemeinsame Dynamik ausführen, ohne die Komponenten zuvor einzeln aufzubauen. Der ggT liest ihre Trennung zurück.

Die Spektraldarstellung ist eine vollständig geprüfte Übersetzung dieses Rechenwegs. Klassisch kann man 64 auch direkt als `8² mod91` berechnen; die Fourieroperation erzeugt hier keinen zusätzlichen Laufzeitvorteil.

## 3. Wo der Z₄-Cap konkret anschließen kann

Diese Aussage verwendet ausdrücklich das endliche Gruppenbasis-Modell. Wenn der native Cap die Form `v=Σ_g |g,−g>` auf `Z₄×Z₄` besitzt, hat er Normquadrat vier. Der normierte Zustand `v/2` ist verschränkt. Ein Bein einfach wegzuspuren ergibt `I₄/4`, nicht den reinen Uhrzustand.

Es gibt aber einen expliziten reversiblen Anschluss:

\[
T|g,h\rangle=|g,g+h\bmod4\rangle,
\qquad T(v/2)=|+_4\rangle\otimes|0\rangle,
\quad |+_4\rangle=\tfrac12\sum_g|g\rangle.
\]

T ist eine Permutation der 16 Basiszustände. Damit liefert der Cap zusammen mit dieser reversiblen Gruppenaddition die benötigte reine Uhrpräparation. **Zusätzlich** benötigt man für einen N-abhängigen Prozess die kontrollierte Multiplikation `|j>|x>→|j>|a^j x mod N>`. Ihre Existenz folgt nicht aus der Norm vier des Caps. Im vorliegenden endlichen Modell ist sie aus N und a berechenbar; eine physische native Umsetzung wird hier nicht behauptet.

Präparation `|+₄>`, kontrollierte Evolution und inverse F₄-Messung erzeugen die zulässigen Messoperatoren

\[
A_s=\tfrac14\sum_{j=0}^3i^{-sj}U_a^j,\qquad\sum_s A_s^\dagger A_s=I.
\]

Wenn `U_a⁴=I`, sind dies orthogonale Spektralprojektoren. Bei allgemeinem U_a sind es weiterhin gültige Filter, aber nicht automatisch Projektoren. Für `N=91,a=2` zeigt bereits ein rationaler Eintrag den Unterschied: `(A₀|1>)₁=1/4`, dagegen `(A₀²|1>)₁=1/16`.

Auch ermittelt ein einzelner solcher Vier-Takt-Versuch die allgemeine Ordnung nicht: Bei jedem `r≥4` sind die ersten vier Orbitzustände verschieden; deshalb ist die Uhrmarginale auf frischem `|1>` exakt `(1/4,1/4,1/4,1/4)`. Die geprüften Ordnungen 4 bei N=15 und 12 bei N=91 bleiben in **dieser** Messung ununterscheidbar. Das ist kein Verbot adaptiver Steuerung, längerer kontrollierter Potenzen oder mehrerer gekoppelter Uhren.

## 4. Vollständige Kosten des ausgeführten Beispiels

Der direkte Viereruhrweg zählt einschließlich der erfolglosen Kandidaten:

- **10 modulare Multiplikationen:** drei je Kandidat zur Fortschreibung von b, Berechnung von b² und b⁴; einmal zusätzlich b³ für die vollständige Einbettung.
- **3 ggT-Aufrufe:** Koprimheitsprüfung und zwei Faktorreader.
- **3 Uhrschlusstests**, **16 exakte gaußrationale Produktadditionen** beim inversen F₄-Rücktransport und **eine Division mit Rest** zur abschließenden Faktorkontrolle.
- Vier gespeicherte Orbitreste; zusätzlich speichert der Bericht drei Suchprotokolle. Die Spektralkoeffizienten sind ausschließlich `0,±1/2,±i/2,±1,±i`; hier gibt es kein verborgenes numerisches Präzisionsproblem.

Bei L Eingabebits und T getesteten Potenzen kostet diese Konstruktion mit elementarer Ganzzahlarithmetik `O(T L²)` Bitoperationen und mit gespeichertem Protokoll `O(TL)` Bits. Sie braucht keine Tabelle sämtlicher N Restklassen. Ein passendes t ist jedoch nicht generell klein; auch garantiert diese Suche in einer festen zyklischen Untergruppe keinen nützlichen Viererorbit. Gerade die Suche darf daher nicht als kostenlose „Transformation in den Raum“ gelten.

Zum Vergleich wurde separat die vollständige Orbit-Spektrum-Pipeline ausgeführt: zwölf Orbitreste, zwölf Spektraleinträge, r=12; inklusive rationaler Phasenkürzung, Nenner-LCM und Reader **17 modulare Multiplikationen und 27 ggT**. Diese einfache Konstruktion kostet `O(r L²)` Bitoperationen und `O(rL)` Speicher; r kann mit N wachsen. Die bloße Existenz einer kleinen formalen Operatorbeschreibung liefert weder ihre vollständige Spektralausgabe noch die passende Basis kostenlos.

Die getrennte Überprüfung umfasst 8.281 exakte Fourier-Eintragsidentitäten und 144 zyklische Eigenvektoridentitäten sowie die Cap-, Filter-, Projektor- und Ausnahmeprüfungen. Diese zusätzlichen Prüfkosten gehören zum Reproduktionslauf, nicht zu den oben getrennt gezählten Löserkosten. Eine dichte klassische F_N-Matrix würde schon N² Einträge beanspruchen; der implementierte Transport nutzt die symbolische Identität und baut sie nicht auf.

## 5. Der Unterschied zu Shors funktionierendem Transfer

Shor transformiert das **Exponentenregister**, nicht schlicht das Restklassenregister: Man wählt eine Zweierpotenz `N²≤Q<2N²`, präpariert `Q⁻¹/²Σ_j |j>|1>`, berechnet kohärent `|j>|a^j modN>` und Fourier-transformiert j. Gemessene Werte liefern Näherungen an `s/r`; Kettenbrüche, Ordnungsprüfung und Wiederholungen ermöglichen das Rücklesen. Ein gekürzter Phasennenner kann zunächst nur einen Teiler von r liefern. Die effiziente kohärente modulare Exponentiation und die skalierbare Fouriertransformation sind dabei zusätzliche ausführbare Bausteine. Der Originalbeweis zählt deren Aufwand polynomial in der Eingabebitlänge im Quantenrechenmodell. [Shor, §§3–5, Gleichungen 5.1–5.13](https://arxiv.org/pdf/quant-ph/9508027)

Hier wurde **kein Quantencomputer ausgeführt oder effizient klassisch simuliert**. Die klassische Orbitliste bezahlt die Zustandsbeschreibung ausdrücklich; die Viereruhrsuche bezahlt alle getesteten Potenzen. Damit liegt ein konkreter, ohne bekannte Faktoren hergestellter Übersetzungsbaustein vor. Der nächste Effizienzsatz müsste das Auffinden eines informativen eingebetteten Orbits oder den Zugriff auf seine geeigneten Phasen für eine wachsende Eingabefamilie günstiger machen.

## Reproduktion und Grenzen

`python3 orbit_fourier.py 91 --audit` läuft ausschließlich mit der Python-Standardbibliothek. Ausgaben sind `orbit-result-91.json`, `four-clock-result.json` und `exact-checks.json`. Der erste Algorithmus meldet ungerade Ordnung oder die triviale Halbordnung als `BASE_RETRY_REQUIRED`; getestet sind N=7,33,9. Dies ist kein vollständiger allgemeiner Primzahlpotenz- oder Faktorisierungsfrontend. Der Viereruhrkonstruktor meldet nach 64 erfolglosen Kandidaten `BOUNDED_SEARCH_NO_FACTOR`, ohne daraus einen Unmöglichkeitssatz zu machen.

Alle endlichen Kontrollen verwenden ganze Zahlen beziehungsweise exakte rationale Real-/Imaginärteile. Die Fourieridentitäten werden durch identische Wurzelexponenten und die ausgeschriebenen algebraischen Beweise kontrolliert. Die ursprüngliche TFPT/Cap-Quelle wird nur unter der oben ausdrücklich angegebenen Gruppenbasis-Annahme angeschlossen. Originalbelege, Forschungsregister und frühere Dateien wurden nicht verändert.
