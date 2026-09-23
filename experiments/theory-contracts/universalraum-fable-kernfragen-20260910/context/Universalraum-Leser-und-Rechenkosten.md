# Prüfung der Leser, Zahlen und Kompressionskosten

10. September 2026. **Die drei konkreten Vorbefunde sind in ihren Originaloutputs belegt. Ihre Zusammenfassung als einheitlicher „Informationsverlust“ überschreitet jedoch die Beweise. Das vorgeschlagene Darstellungsminimum ist ein Forschungsziel; die Kosten seiner Herstellung und Nutzung müssen Teil des Ziels sein.** Geprüft sind Abschnitte 7 und 13–15 des neuesten Anhangs [S0].

## 1. Welche Zahlen tatsächlich gelten

**Gauss-Koordinaten.** [S1–S2] verwenden eine uniforme 2×2-Matrix über `(Z/NZ)[i]`, deren acht reelle Einträge unabhängig gezogen werden. Für `det A=x+iy` vergleicht man `gcd(N,x²+y²)` mit den Koordinatenlesern `gcd(N,x), gcd(N,y)`. Die genaue Formel gilt für `N=pq`, verschiedene ungerade Primzahlen `p,q≡3 mod 4`. Setzt man

\[
a_p=p^{-2}+p^{-4}-p^{-6},\quad c_p=(p-1)(p^{-2}-p^{-6}),\quad d_p=(p-1)c_p,
\]

dann sind die Erfolgswahrscheinlichkeiten

\[
\rho_N=a_p+a_q-2a_pa_q,\qquad
\rho_C=1-a_pa_q-2c_pc_q-d_pd_q,
\]

und `ρC−ρN=2(p+q−1)c_p c_q>0`. Für balancierte Faktoren `p≤q≤2p` folgt tatsächlich **Θ(N⁻¹) → Θ(N⁻¹/²)**. Das bedeutet bei unabhängigen Wiederholungen **Θ(N) → Θ(√N) erwartete Proben**; beide wachsen exponentiell in der Eingabebitlänge. Zwei gewöhnliche uniforme skalare Proben erreichen bereits dieselbe führende Größenordnung wie die Koordinaten. Es ist somit ein belegter Vorteil gegenüber dem Normleser derselben Quelle, kein allgemeiner Faktorisierungsdurchbruch. Die Verteilung ist auch nicht automatisch die eines beliebigen nativen Compilerworts. Für gespaltene Primstellen und Primzahlpotenzen gelten diese Formeln nicht unverändert. Den Normleser zusätzlich beizubehalten verhindert jedenfalls den Verlust seiner bisherigen Erfolge.

**RH-Budget.** [S3–S4] fixieren `I=(−9/8,9/8)`, `J=(−6/5,6/5)`, die vollständigen nativen Matrizen W/M und den unteren Koerzivitätskoeffizienten `1/8`. Für einen expliziten rationalen Polynomzeugen liefert bereits der endliche positive Lastanteil die Untergrenze

\[
L=8\|g\|^2/(1+10^{-6})>8.404\cdot10^{-9},
\quad Q_S(v)<1.083\cdot10^{-9},
\quad L/Q_S(v)=7.76241762266858\ldots
\]

Damit scheitert **dieses eingefrorene vollständige untere Zertifikat**, auch gegen die tatsächliche Schalenergie. Die ursprüngliche gesamte Weilform desselben Zeugen ist dagegen positiv: `Q_J(F)=5.8304…·10⁻¹⁴`. Weder RH noch die globale Weil-Positivität sind widerlegt. Das Dokument benutzt nicht den inversen wahren Altoperator, sondern das benannte untere Zertifikat. „Eine weggelassene Richtung war teuer“ unterschlägt diese Unterscheidung: vollständiges Wiederaufnehmen der Last allein repariert die zu schwache Schranke nicht.

**Dynamische Zeta.** [S5–S6] behandeln exakt den ursprünglichen Solenoidautomaten `W=UV` auf dem Dual von `Z[i,1/2]³`. Seine Fixpunktfolge ist `F_n=odd(|b_n|)²`. Die ausgeschriebene Bewertungsinduktion und die nichtverschwindenden radialen Signaturen an allen dyadischen Einheitswurzeln ergeben für

\[
Z_\alpha(z)=\exp\!\sum_{n\ge1}F_nz^n/n
\]

die natürliche Grenze `|z|=1/4`, sogar gegen meromorphe Fortsetzung. Dies verhindert die direkte Gleichsetzung **dieser** Zeta mit der Riemannschen Zeta. Andere hergeleitete Leser oder relative Spuren werden nicht ausgeschlossen. Eine natürliche Grenze beweist zudem keine vorangegangene unzulässige Kompression: Sie kann eine exakte Eigenschaft einer korrekt bestimmten Antwort sein. Dieselbe Quelle enthält bereits eine begrenzte, rigorose Beschleunigung ihrer Auswertung innerhalb des Konvergenzkreises.

## 2. Der praktisch nutzbare Transformationsvertrag

Abschnitt 13 trifft den Mechanismus der elliptischen Faktorisierung: Aus N werden Kurve und Punkt aufgebaut; eine modulo N nicht invertierbare Größe liefert über einen ggT den Faktor. Unser vorhandener vollständiger Lauf [S7] beginnt mit `N=10403`, `E:y²=x³+x−1`, `P=(2,3)`; der Nenner `5050` liefert `gcd(10403,5050)=101`, danach den Kofaktor 103. Die Faktoren werden erst anschließend zur lokalen Erklärung verwendet. Der gespeicherte Lauf benötigt eine Kurve, 15 Gruppenadditionsaufrufe, 14 ggT-Aufrufe und 12 Inversionen. Das ist ein konkretes Lösungsbeispiel; die günstige erste Kurve ist keine garantierte Laufzeit für beliebige N.

Für das universelle `argmin C(Φ(P))` braucht jede zugelassene Darstellung Encoder, ausführbaren Löser und Reader mit

\[
\operatorname{Read}_\Phi\bigl(\operatorname{Solve}_\Phi(\operatorname{Enc}_\Phi(P))\bigr)=\operatorname{Ans}(P).
\]

Erhalten werden müssen die ausgewiesenen Antworten und Eingriffe; nicht jede problemspezifische Reduktion benötigt die gesamte ursprüngliche Prozessinformation. Die Gesamtkosten umfassen **Darstellungssuche einschließlich verworfener Kandidaten, Herstellung, benötigte Korrektheitsprüfungen, Lösen, Rücklesen und Ergebnisprüfung**. Bitgrößen, Präzisionsbedarf, Wiederholungen und eventuell amortisierte Vorarbeit müssen ausdrücklich enthalten sein.

Ein einfacher Gegenzeuge gegen eine verkürzte Kostenfunktion ist `Φ(P)=Ans(P)`: Der nachfolgende Löser liest nur eine Konstante. Die Konstruktion von Φ enthält jedoch bereits das ursprüngliche Problem. Antworterhaltung allein verhindert dieses versteckte Lösungsorakel nicht. Ohne konstruierbare Kandidatenklasse, vollständige Kosten und ausführbare Auswahlregel bezeichnet das Minimum daher noch keinen Algorithmus.

## 3. Was ein Zukunftsrang von 37 erlauben würde

Die Zahl 37 aus 10.000 Pfaden ist im Anhang **ein hypothetisches Beispiel**, kein gemessener Befund. Für einen bekannten, unter allen erlaubten Fortsetzungen geschlossenen linearen Antwortspan können 37 Basisrichtungen genügen. Der klassische PSR-Satz konstruiert entsprechende Vorhersagekoordinaten aus einem gegebenen endlichen POMDP; er behauptet keine kostenlose Identifikation aus beliebigen Messungen. [Littman–Sutton–Singh, Theorem 1](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf)

Der bereits bewiesene Interventionsquotientensatz [S8] verlangt gleiche Antworten **und** wieder gleiche komprimierte Nachfolger unter jeder erlaubten Aktion. Ein kleiner Rang einer bisher gemessenen Tabelle ersetzt diesen Abschluss nicht.

Auch positiver Speicherbedarf ist keine reine Rangzahl. Betrachte die vier Präparations-/Antwortverteilungen

\[
M=\tfrac12\begin{pmatrix}0&0&1&1\\1&0&0&1\\1&1&0&0\\0&1&1&0\end{pmatrix}.
\]

Ihr linearer Rang ist 3: `r₃=r₀+r₂−r₁`. Ihr **nichtnegativer Rang ist 4**. Beweis: Die vier positiven Einträge `(0,2),(1,3),(2,0),(3,1)` können paarweise nicht im selben positiven Rang-eins-Rechteck liegen, weil mindestens ein Kreuzfeld null ist. Eine nichtnegative Zerlegung kann dort nichts wegkürzen und braucht mindestens vier Summanden; die vier Originalzeilen liefern eine solche Zerlegung. Somit genügen drei lineare Koordinaten, aber keine drei klassischen verborgenen Zustände mit positiver Präparation und positiver Ausgabe. Dies ist ausdrücklich kein Satz über minimale Quanten-Hilbertraumdimensionen.

Schließlich bleibt `B_δ=((1,1),(0,δ))` für `δ=2⁻ᵐ` stets vom Rang 2, während `B_δ⁻¹=((1,−2ᵐ),(0,2ᵐ))`. Ein Fehler `2⁻ᵐ/4` in der zweiten Messkoordinate wird zum Rekonstruktionsfehler `1/4`. Koeffizientenlänge und benötigte Präzision wachsen mit m, obwohl der Rang konstant bleibt. Eine andere Basis kann helfen; ihr Auffinden und ihr Anschluss an die verfügbaren Messungen müssen bezahlt werden.

Die beiden Gegenbeispiele sind mit rationaler Arithmetik vollständig geprüft. Originalkampagnen wurden nicht wiederholt. Die konkreten Originalbelege und ihre Prüfausgaben wurden gelesen und mit SHA-256 gebunden; die vorliegenden numerischen RH-Zertifikate wurden in diesem Audit nicht neu berechnet. `SOURCES.json` nennt den jeweiligen Lesescope; `rank-cost-checks.json` dokumentiert nur die neuen endlichen Kontrollen.
