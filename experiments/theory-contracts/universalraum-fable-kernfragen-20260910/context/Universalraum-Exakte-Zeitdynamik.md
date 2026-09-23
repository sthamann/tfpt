# Exakte dyadische Dynamik und natürliche Grenze des ursprünglichen Compiler-Solenoids

10. September 2026. Ein quellspezifischer Satz über die tatsächliche dynamische Zeta-Funktion des ursprünglichen gemeinsamen Gateworts. Er entscheidet keine Aussage über die Riemannsche Zeta-Funktion. Die Methode gehört zur bekannten Untersuchung natürlicher Grenzen in algebraischer Dynamik; die folgenden Formeln und Beweise werden für diese konkrete Quelle ausgeschrieben.

## 1. Unveränderte Quelle und Gegenstand

Verwendet wird genau das Gatewort W=UV aus `compiler_solenoid_20260909/REPORT.md`, mit

\[
W=\frac12\begin{pmatrix}i&1+i&i\\-1&1-i&-1\\-1+i&0&1-i\end{pmatrix},
\quad W^\dagger W=I,\quad\det W=1.
\]

Sei P_n=2^n tr(W^n)=a_n+i b_n. Die originale ganzzahlige Rekursion lautet

\[
P_0=3,\quad P_1=2-i,\quad P_2=-5-8i,
\]
\[
P_n=(2-i)P_{n-1}-(4+2i)P_{n-2}+8P_{n-3}.
\]

Auf dem ursprünglichen Solenoid X=widehat(Z[i,1/2]^3) ist die bekannte genaue Fixpunktzahl

\[
F_n=\operatorname{odd}(|b_n|)^2.
\]

Wir untersuchen ausschließlich

\[
Z_\alpha(z)=\exp\sum_{n\ge1}\frac{F_n}{n}z^n,
\qquad D(z)=\frac{zZ'_\alpha(z)}{Z_\alpha(z)}=\sum_{n\ge1}F_nz^n.
\]

Die zugrunde liegenden Originale, ihr unveränderter SHA-256 und die eigenen exakten Kontrollen sind im Prüfer dokumentiert. Die Quelle und ihr Fixpunktsatz werden erhalten; es wird keine neue physische Auswahl des Solenoids behauptet.

## 2. Der vollständige Zweieranteil für jede Zeit

**Satz 1.** Für jedes n≥1 gilt

\[
\boxed{v_2(b_n)=\begin{cases}0,&n\text{ ungerade},\\v_2(n)+2,&n\text{ gerade}.\end{cases}} \tag{1}
\]

**Beweis.** Für jede unitäre Dreiermatrix T mit Determinante 1 gilt tr(T²)=tr(T)²−2 overline(tr(T)). Angewandt auf T=W^n ergibt dies die exakte Verdopplung

\[
b_{2n}=2b_n(a_n+2^n). \tag{2}
\]

Die ursprüngliche Rekursion besitzt modulo 8 ab n=3 den geschlossenen Viererzyklus

\[
(a_n,b_n)\equiv (4,5),(1,0),(4,3),(7,0),\ldots\pmod8.
\]

Der Anfang folgt durch direktes Rechnen; Einsetzen der vier Zustände in die Rekursion bestätigt die periodische Fortsetzung. Es handelt sich um einen endlichen Induktionsbeweis, keine Extrapolation. Für ungerade n ist b_n folglich ungerade und a_n+2^n≡4 mod8; beim Sonderanfang n=1 ist a_1+2=4 ebenfalls exakt. Für gerade n ist a_n ungerade. Die erste Verdopplung eines ungeraden Index erzeugt damit Bewertung 3, jede weitere Verdopplung erhöht sie genau um 1. Das beweist (1). ∎

Insbesondere ist b_n für alle n ungleich null. Der ursprüngliche All-n-Ausschluss endlicher Fixräume erhält so einen zweiten elementaren Beweis. Aus der originalen Identität det(W^n−I)=i b_n/2^(n−1) folgt zugleich, dass kein Eigenwert von W eine Einheitswurzel ist.

Setze für k≥0

\[
c_0=1,\qquad c_k=2^{-2k-4}\ (k\ge1).
\]

Damit lautet die vollständige originale Fixpunktfolge jetzt ohne unevaluierte Zweierbewertung

\[
\boxed{F_n=c_{v_2(n)}\,b_n^2.} \tag{3}
\]

Die Lokalisierung bei 2 ist also eine exakt bestimmbare zeitabhängige Gewichtung. Die ungeraden Primzahlen bleiben als Teiler der b_n und mit ihren jeweiligen Bewertungen erhalten.

## 3. Die Phasen können den dyadischen Anteil nicht auslöschen

Seien λ_1,λ_2,λ_3 die Eigenwerte von W. Sie liegen auf dem Einheitskreis und haben Produkt 1. Dann ist

\[
\frac{b_n^2}{4^n}
=\frac12\sum_{i,j}(\lambda_i/\lambda_j)^n
-\frac14\sum_{i,j}\left[(\lambda_i\lambda_j)^n+(\lambda_i\lambda_j)^{-n}\right]. \tag{4}
\]

Der nichtoszillierende Anteil ist genau 3/2, aus i=j in der ersten Summe. Keiner der übrigen Phasenfaktoren ist eine Einheitswurzel von Zweierpotenzordnung:

- Für i≠j ist λ_iλ_j=λ_k⁻¹, und für i=j ist es λ_i². Jede dyadische Einheitswurzel in diesen beiden Fällen würde λ_k beziehungsweise λ_i zu einer Einheitswurzel machen; Satz 1 schließt das aus.
- Für die sechs Quotienten λ_i/λ_j, i≠j, ergibt der exakte Resultant des ursprünglichen charakteristischen Polynoms
  \[
  f(x)=2x^3-(2-i)x^2+(2+i)x-2
  \]
  die Identität
  \[
  \operatorname{Res}_x(f(x),t^3f(x/t))=-4(t-1)^3Q(t),
  \]
  \[
  Q(t)=16t^6+28t^5+4t^4-17t^3+4t^2+28t+16.
  \]
  Weil Q rational und vom Grad 6 ist, kommen als dyadische Einheitswurzeln nur Ordnungen 1,2,4,8 in Betracht. Die Resultanten mit den entsprechenden zyklotomischen Polynomen sind 79,1,5329,1; keiner verschwindet. Dies schließt auch Wiederholungen der Eigenwerte aus.

Diese endlichen Zertifikate gelten für alle dyadischen Ordnungen; eine große numerische Phasenprobe ist nicht nötig.

## 4. Eine explizite dyadische Antwortfunktion

Definiere für |w|<1

\[
C(w)=\sum_{n\ge1}c_{v_2(n)}w^n
=\frac{w}{1-w^2}+\sum_{k\ge1}2^{-2k-4}
\frac{w^{2^k}}{1-w^{2^{k+1}}}. \tag{5}
\]

Diese Reihe konvergiert lokal gleichmäßig. Sei ζ eine primitive Einheitswurzel der Ordnung 2^r; für r=0 ist ζ=1. Direktes Auswerten der geometrischen Summen ergibt die radialen Grenzwerte

\[
A_r:=\lim_{t\uparrow1}(1-t)C(t\zeta)
=\begin{cases}
113/224,&r=0,\\
-111/224,&r=1,\\
-\dfrac67\,2^{-3r-2},&r\ge2.
\end{cases} \tag{6}
\]

**Begründung des Grenzübergangs.** Für jeden Summanden gilt

\[
\left|(1-t)\frac{(tu)^{2^k}}{1-(tu)^{2^{k+1}}}\right|\le1
\quad (|u|=1,\ 0<t<1).
\]

Da Σ c_k<∞, ist dominierte Konvergenz anwendbar. Beim primitiven 2^r-Punkt liefern für r≥1 der Term k=r−1 den Wert −c_(r−1)/2^r und die Terme k≥r die Summe Σ c_k/2^(k+1). Die niedrigeren Terme verschwinden. Bei r=0 bleibt die gesamte positive Summe. Daraus folgt (6), einschließlich der beiden gesonderten Anfangswerte.

Für jedes u auf dem Einheitskreis, das **keine** dyadische Einheitswurzel ist, verschwindet dagegen jeder einzelne radiale Grenzwert und folglich

\[
\lim_{t\uparrow1}(1-t)C(tu)=0. \tag{7}
\]

Dies verlangt keinen Diophantischen Abstand von u zu den dyadischen Wurzeln; Summierbarkeit der c_k genügt.

## 5. Natürliche Grenze der tatsächlichen dynamischen Zeta

Aus (3)–(5) folgt die vollständige, innerhalb |z|<1/4 gültige Darstellung

\[
D(z)=\frac32C(4z)+\frac12\sum_{i\ne j}C(4z\lambda_i/\lambda_j)
-\frac14\sum_{i,j}\left[C(4z\lambda_i\lambda_j)+C(4z/(\lambda_i\lambda_j))\right]. \tag{8}
\]

Am Punkt z=tζ/4 gilt nach den Nichtresonanzzertifikaten aus Abschnitt 3 und (7): Sämtliche gedrehten Summanden haben verschwindenden radialen Grenzwert. Deshalb bleibt exakt

\[
\boxed{\lim_{t\uparrow1}(1-t)D(t\zeta/4)=\frac32A_r\ne0.} \tag{9}
\]

Die dyadischen Einheitswurzeln sind dicht auf dem Einheitskreis. Somit hat D an einer dichten Menge des Kreises |z|=1/4 eine nichtverschwindende radiale Polsignatur. Jede meromorphe Fortsetzung durch einen Punkt dieses Kreises würde in einer offenen Umgebung unendlich viele solche Pole mit einem Häufungspunkt enthalten. Das ist unmöglich, da die Pole einer meromorphen Funktion isoliert sind.

**Satz 2.** D besitzt exakt den Konvergenzradius 1/4 und der Kreis |z|=1/4 ist seine natürliche Grenze, sogar gegen meromorphe Fortsetzung. Dasselbe gilt für Z_α: Eine meromorphe Fortsetzung von Z_α würde eine meromorphe Fortsetzung von zZ'_α/Z_α=D erzeugen und damit widersprechen. ∎

Insbesondere

\[
\limsup_{n\to\infty}\frac1n\log F_n=\log4.
\]

Diese letzte Aussage ist das hier bewiesene exponentielle Fixpunktwachstum. Ein zusätzlicher topologischer Entropiesatz wird für sie nicht vorausgesetzt.

## 6. Eine wirkliche Rechenverkürzung für die Dynamik

Die neue Darstellung (8) ersetzt das explizite Summieren sehr vieler Perioden durch eine dyadische Reihe mit geometrischen Teilsummen. Bei Abschneiden von (5) nach k=K≥1 und |w|≤ρ<1 gilt

\[
|C(w)-C_K(w)|\le
\frac{4^{-K}}{48}\,
\frac{\rho^{2^{K+1}}}{1-\rho^{2^{K+2}}}. \tag{10}
\]

Denn die Summe der ausgelassenen c_k ist 4^(-K)/48 und der verbleibende Quotient ist für alle k>K durch den gezeigten ersten begrenzt. Die Summe der Absolutbeträge aller Koeffizienten in (8) ist 9. Daher ist der Gesamtfehler der entsprechenden D-Auswertung durch neunmal (10), mit ρ=4|z|, beschränkt. Fehler in der numerischen Ermittlung der algebraischen Phasen müssten zusätzlich kontrolliert werden; der Satz schenkt keine exakten Eigenwerte.

Der implementierte Auswerter vermeidet eine numerische Eigenwertbestimmung ganz. Setze T₁=W⊗overline(W), T₂=W⊗W und T₃=overline(W)⊗overline(W). Mit derselben rationalen Matrixfunktion C_K gilt

\[
D_K(z)=\tfrac12\operatorname{tr}C_K(4zT_1)
-\tfrac14\operatorname{tr}C_K(4zT_2)
-\tfrac14\operatorname{tr}C_K(4zT_3).
\]

Jeder dyadische Term wird als Q(I−Q²)⁻¹ auf einer 9×9-Matrix berechnet; anschließend wird Q durch Q² ersetzt. Alle Ausgangsmatrizen sind exakt gaußrational. Komplexe Intervallarithmetik mit 256 Bit erfasst Rundungsfehler; (10) bezahlt den gesamten unendlichen Rest. Der zusätzliche direkte Vergleich bei z=1/16 verwendet die ursprüngliche ganzzahlige Rekursion und einen unabhängig begrenzten Periodenrest.

Bei z=0.24999975, also 4z=0.999999, liefern 24 dyadische Ebenen beziehungsweise 72 Matrixresolventen

\[
D(z)=756696.049495159035840020989\ \pm 4.75\cdot10^{-22}.
\]

Der gesamte Test mit zwei Auswertestellen brauchte im beobachteten Lauf etwa 0.024 Sekunden. Die einfache geometrische Restschranke einer direkten Periodensumme würde für das Ziel 10⁻²⁰ eine ausreichende Grenze von 62.064.406 Termen angeben. Das ist ein Vergleich mit dieser ausdrücklich bezeichneten Auswertemethode und ihrer konservativen Restschranke; weder wurden 62 Millionen Terme tatsächlich gemessen noch wird eine untere Schranke gegen alle anderen Algorithmen behauptet.

Das ist eine mathematisch begründete Abkürzung zur Auswertung **dieser** dynamischen Antwort. Sie liefert weder die unbekannten Primfaktoren eines Eingabe-N noch einen Zugriff auf Riemannsche Nullstellen.

## 7. Konsequenz für den universellen Ursprung

Die genaue Rollenverteilung ist jetzt deutlicher: Die komplexen Eigenphasen bestimmen Oszillationen; die ausgezeichnete Primstelle 2 bestimmt die dyadische Gewichtung; die ungeraden Primstellen sind lokale Faktoren der Rückkehrkokernel. Diese Informationen sind im selben Quellenmodell gekoppelt, aber ihre mathematischen Rollen sind verschieden.

Die ursprüngliche dynamische Zeta lässt sich deshalb nicht schlicht mit der Riemannschen Zeta identifizieren. Auch nach z=4^(-s) besitzt sie die entsprechende natürliche Grenze an Re s=1. Eine direkte Gleichsetzung mit einer global meromorph fortsetzbaren Funktion ist damit ausgeschlossen. Dies schließt weder einen anderen relativen Trace, ein anderes hergeleitetes Zeitgesetz, eine Kohomologie noch eine neue Darstellung des gesamten Quellenprozesses aus. Solche Übergänge müssen jedoch die vorhandenen arithmetischen Informationen erhalten und mathematisch definiert werden.

Die relevante Primfrage lautet daher genauer: Welcher ursprüngliche relative Leser überführt die lokalen Rückkehrbewertungen in die verlangten Primzahlpotenzgewichte und die Zeit log p, einschließlich Gamma- und Polbeiträgen? Die hier bewiesene natürliche Grenze löst diese Frage nicht, verhindert aber die Gleichsetzung der beiden Zeta-Funktionen und liefert eine exakte Dynamikformel als Ausgangspunkt.

## 8. Quellen, Neuheit und Kontrolle

Originalquelle: `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/compiler_solenoid_20260909/REPORT.md`, insbesondere Abschnitte 3–6. Dort waren die Fixpunktfolge und die Konvergenz mindestens für |z|<1/4 bereits bewiesen; eine volle analytische Fortsetzung beziehungsweise Rationalitätsentscheidung war ausdrücklich offen.

Die natürliche-Grenze-Methode ist etablierte Mathematik; zum Kontext siehe [Bell, Miles und Ward, *Towards a Pólya–Carlson dichotomy for algebraic dynamics*](https://arxiv.org/abs/1307.2369). Hier wird der konkrete offene Quellenfall durch einen direkten radialen Beweis geschlossen; es wird keine weltweite Neuheit der Methode beansprucht.

Vorab wurden native RH-Triage, die aktuellen offenen Graphkanten und der Faktorisierungsgraph durchsucht. `PRIME.CLOCK.COMBINATION.SPECTRUM.01` betrifft den fehlenden log-p-Anschluss endlicher beziehungsweise kommensurabler Uhren; `r448 companion` betrifft eine andere dyadische Fortsetzungsbehauptung. Hier wird weder eine kommensurable Zeit als log-p-Fluss ausgegeben noch ein positiver Weil-Nachweis vorgeschlagen. Der Gegenstand ist die tatsächlich konstruierte Solenoid-Zeta und ihre eigene analytische Grenze. Ähnlichkeitssuchen ersetzen keine Beweisprüfung.

Der eigene Prüfer kontrolliert die Originalmatrix, die geschlossene Modulo-8-Induktion, die Resultanten und die radialen Konstanten exakt. Zusätzliche endliche Kontrollen der ersten 512 Indizes dienen der Fehlerkontrolle; die All-n-Aussagen beruhen auf den ausgeschriebenen Induktions- und Analysebeweisen. Die unabhängige konzeptionelle Prüfung von Bewertung, Nichtresonanz, dominierten Grenzübergängen, natürlicher Grenze und Restkonstante hat keine notwendige mathematische Korrektur gefunden; der separate Befund liegt in FROBENIUS-REVIEW.md. Dies ist eine unabhängige Agentenlektüre, keine externe Begutachtung oder formale Lean-Verifikation.
