# Die lokale Primzahldynamik von W und ein schneller Leser aus erhaltenen Potenzen

10. September 2026. Begrenzte Fortsetzung auf den unveränderten ursprünglichen U,V-Gates. Die allgemeinen Zutaten — Cayley-Transformation, Frobenius, Norm-1-Tori, ggT von Rückkehrzeiten und Gram-Paarungen — sind klassische Mathematik. Neu innerhalb dieses Arbeitsdurchgangs sind ihre genaue Verbindung für diese Quelle, der geschärfte lokale Rückkehrsatz und die implementierte Wiederverwendung ihrer Potenzkoeffizienten. Keine weltweite Neuheitsbehauptung und kein neuer allgemeiner schneller Faktorisierungsalgorithmus.

## 1. Die wirkliche Quelle und ihre reelle Kubik

Die ursprünglichen Quellen sind

- `/Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/su3_prime_return_20260909v/MATHEMATIK.md`, Abschnitte 1, 3–4;
- `/Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/su3_selector_20260909w/MATHEMATIK.md`, Abschnitte 1–2;
- `/Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/pfaffian_prime_selector_20260909x/MATHEMATIK.md`, Abschnitt 4.

Sie geben

\[
W=UV=\frac12\begin{pmatrix}i&1+i&i\\-1&1-i&-1\\-1+i&0&1-i\end{pmatrix},
\quad W^*W=I,\quad\det W=1.
\]

Für Y=2W und \(P_n=\operatorname{tr}Y^n=a_n+ib_n\) gilt

\[
P_0=3,\quad P_1=2-i,\quad P_2=-5-8i,
\]
\[
P_n=(2-i)P_{n-1}-(4+2i)P_{n-2}+8P_{n-3},
\quad \det(W^n-I)=\frac{ib_n}{2^{n-1}}.
\]

Für ungerades N ist der Rückkehrleser deshalb exakt gcd(N,b_n). Die bereits vorhandene allgemeine SU(3)-Aussage war: An jeder ungeraden Primstelle p verschwindet die Determinante bei mindestens einem der Exponenten \(p-\chi\) oder \(p^2+\chi p+1\), \(\chi=(-1/p)\). Deren Auswahl und Glattheit waren ausdrücklich offen.

Die unabhängig in dieser Runde beim Root und hier berechnete genauere Normalform ist

\[
T=2(W+W^*)=
\begin{pmatrix}0&i&-1\\-i&2&-1\\-1&-1&2\end{pmatrix},
\]
\[
g(t)=t^3-4t^2+t+4,\quad g(T)=0,\quad\operatorname{disc}(g)=316=4\cdot79,
\]
\[
W=(T-iI)(T+iI)^{-1},\qquad\det(T+iI)=-8.
\]

Die hier zunächst benutzte übliche Cayley-Matrix \(i(W+I)(W-I)^{-1}\) ist genau −T; dies sind zwei Vorzeichenkonventionen desselben Operators. Er wird weder als logarithmischer Zeitgenerator noch als neue unabhängige physikalische Quelle ausgegeben.

g ist über Q irreduzibel: Keine der möglichen ganzzahligen Wurzeln ±1,±2,±4 verschwindet. T ist Hermitesch mit drei verschiedenen reellen Eigenwerten. Der reelle Zerfällungskörper hat daher Galoisgruppe S₃, da die Diskriminante nicht quadratisch ist. Sein Kompositum mit Q(i) hat Gruppe S₃×C₂: Der reelle Körper enthält i nicht, und komplexe Konjugation fixiert ihn punktweise. Der nichtgaloissche Körper Q(t,i) ist ein CM-Feld über dem reellen kubischen Körper; darin ist

\[
u=(t-i)/(t+i),\qquad u\bar u=1,
\]

die tatsächliche Norm-1-Einheit im bei 2 lokalisierten Ganzheitsring, deren drei Konjugierte die W-Eigenwerte sind. Eine gewöhnliche globale algebraisch-ganzzahlige Einheit wird damit nicht behauptet. Die Nenner sind außerhalb der Stelle 2 invertierbar. Für die folgende separable Frobeniusklassifikation werden außerdem p=79 ausgeschlossen; gcd(N,79) ist unabhängig davon ein gewöhnlicher öffentlicher Vorabtest. Die beiden besonderen Stellen 2,79 sind **nicht** die Liste möglicher Rückkehrprimzahlen.

## 2. Exakter Torus- und Rückkehrsatz

Sei p≠2,79 eine Primzahl, \(\chi=(-1/p)\). Sei π die gewöhnliche Frobeniuspermutation der drei Wurzeln t_j von g modulo p. Setze \(\lambda_j=(t_j-i)/(t_j+i)\). Dann

\[
\boxed{\lambda_j^p=\lambda_{\pi(j)}^\chi.}
\]

Dies folgt durch Potenzieren des rationalen Ausdrucks: \(t_j^p=t_{\pi(j)}\) und \(i^p=\chi i\). Wegen \(\chi=\pm1\) ist auch \(\lambda_{\pi(j)}=\lambda_j^{\chi p}\). Die Eigenwerte sind verschieden und nichtnull; zudem ist ihr Produkt eins.

| Reelle kubische Faser modulo p | π | Teiler der ganzen Matrixordnung | Exakte Form der Determinantenrückkehr |
|---|---|---:|---|
| Drei lineare Faktoren | Identität | p−χ | Vereinigung der Vielfachen ihrer drei Eigenordnungen r₁,r₂,r₃ |
| Linear × irreduzibel quadratisch | Transposition | p²−1 | Genau die Vielfachen eines einzigen r_p\|p−χ |
| Irreduzibel kubisch | Dreierzyklus | p²+χp+1 | Genau die Vielfachen eines einzigen r_p\|p²+χp+1; zugleich volle Matrixrückkehr |

**Beweis.** Bei einem festen t_j folgt \(\lambda_j^{p-\chi}=1\). Bei einer Zweierbahn folgt \(\lambda^{p^2-1}=1\). Bei einer Dreierbahn ergeben die drei Eigenwerte \(\lambda,\lambda^{\chi p},\lambda^{p^2}\); ihr Produkt eins gibt \(\lambda^{p^2+\chi p+1}=1\). Alle Eigenwerte einer Bahn haben dieselbe Ordnung, da die Potenz χp dazu teilerfremd ist.

Im Transpositionsfall sei s die gemeinsame Ordnung der beiden bewegten Eigenwerte. Der feste Eigenwert ist deren inverses Produkt, also \(\lambda_0=\lambda^{-(1+\chi p)}\). Seine Ordnung ist daher exakt

\[
\boxed{r_p=\frac{s}{\gcd(s,p+\chi)}.}
\]

Insbesondere r_p|s. Sobald einer der beiden bewegten Eigenwerte zurückkehrt, ist daher der feste schon zurückgekehrt. Die ganze Determinante verschwindet genau für r_p|n, nicht für eine zusätzliche unabhängige zweite Indexfamilie. Die ganze Matrixordnung ist s. Im Dreierzyklus haben alle Eigenwerte dieselbe Ordnung, wodurch Determinanten- und Matrixrückkehr zusammenfallen. ∎

Der quadratische Charakter der Diskriminante ist die Signatur von π. Folglich erzwingt \((79/p)=-1\) genau den Transpositionsfall. \((79/p)=1\) unterscheidet vollständige Spaltung und Irreduzibilität noch nicht. Das öffentlich berechenbare Jacobi-Symbol \((79/N)\) ist das Produkt der lokalen Zeichen mit ihren Exponenten; es verrät die einzelnen lokalen Permutationen nicht.

## 3. Ein verkürzter Index aus zwei Gesamtkollisionen

An jeder **nicht vollständig gespaltenen** Primstelle aus Abschnitt 2 gilt jetzt

\[
p\mid b_m\text{ und }p\mid b_n\iff p\mid b_{\gcd(m,n)}.
\]

Denn die linken Bedingungen lauten r_p|m und r_p|n. Damit gilt für jedes quadratfreie N, das nur solche Primstellen besitzt,

\[
\boxed{\gcd(N,b_m,b_n)=\gcd(N,b_{\gcd(m,n)}).}
\]

Im allgemeinen quadratfreien Fall können bei der Indexverkürzung **nur vollständig gespaltene kubische Fasern** herausfallen. Dort können zwei verschiedene Eigenrichtungen an zwei Zeiten zurückkehren, ohne eine gemeinsame Rückkehrrichtung am ggT-Index zu besitzen.

Die zugrunde liegende Prozessidentität ist noch allgemeiner:

\[
\ker(W^m-I)\cap\ker(W^n-I)=\ker(W^{\gcd(m,n)}-I).
\]

Sie folgt für jede invertierbare Matrix über jedem Körper aus Bézout für die beiden Exponenten. Die skalare Determinante speichert nur die Existenz einer Richtung, nicht welche Richtung zurückkehrt. Der ggT-Schritt fragt nach der gemeinsamen Richtung.

**Öffentlicher Zusatz.** Ist N ungerade, zu 79 teilerfremd, \((79/N)=-1\) und sind beide bisherigen Rückkehrreste null modulo N, dann ist \(\gcd(N,b_{\gcd(m,n)})>1\). Das negative Jacobi-Symbol garantiert mindestens eine Transpositionsprimstelle; sie bleibt nach der Verkürzung erhalten. Das Ergebnis darf weiterhin N sein. Die Aussage benötigt für dieses bloße Nichttrivialitätsminimum keine Quadratfreiheit; die exakte ggT-Gleichheit oben bleibt auf quadratfreie N beschränkt.

Das ist eine aus vorhandenen öffentlichen Kollisionsindizes berechenbare Verkürzung. Es wird weder p als bekannt eingesetzt noch Glattheit von p±1 angenommen. Die Herstellung geeigneter m,n wird dadurch jedoch nicht gelöst.

## 4. Noch schneller: Eine gemischte Spur aus dem erhaltenen Potenz-Lift

Der vorhandene schnelle Rekursionsleser berechnet beim binären Potenzieren ohnehin die drei Gaußkoeffizienten

\[
Y^k=r_{k,0}I+r_{k,1}Y+r_{k,2}Y^2.
\]

Wer nur P_k speichert, verwirft einen Teil dieser Daten. Behalte stattdessen die drei Koeffizienten. Der **tatsächliche**, fest durch die Quelle gegebene Hilbert–Schmidt-Gram ist

\[
G_{ij}=\operatorname{tr}(Y^i(Y^j)^*)
=\begin{pmatrix}
3&2+i&-5+8i\\
2-i&12&8+4i\\
-5-8i&8-4i&48
\end{pmatrix}_{ij},\qquad\det G=316.
\]

Die Gleichheit der Zahl 316 mit der Cayley-Diskriminante hat einen exakten Grund. Wegen der Normalität von Y ist G das Gram der Vandermonde-Zeilen \((1,y_j,y_j^2)\) seiner Eigenwerte; daher

\[
\det G=|\operatorname{disc}(f_Y)|=316.
\]

Unter \(y_j=2(t_j-i)/(t_j+i)\) gilt
\(y_j-y_k=4i(t_j-t_k)/[(t_j+i)(t_k+i)]\).
Mit \(\prod_j(t_j+i)=-8\) folgt

\[
\operatorname{disc}(f_Y)=\frac{(4i)^6}{(-8)^4}\operatorname{disc}(g)
=-\operatorname{disc}(g)=-316.
\]

Damit werden **drei verschiedene Primrollen** präzise getrennt: 2 ist die durch die dyadischen Gates gesetzte Nenner- und Lokalisierungsstelle; 79 ist die Verzweigungsstelle der kubischen Quelle und zugleich eine Degenerationsstelle ihres Koeffizienten-Grams modulo p; gewöhnliche Rückkehrprimstellen wie 11 oder 647 werden hingegen durch die multiplikativen Eigenordnungen bestimmt. Die Diskriminante legt keine universelle Primzeit fest. Der Leser selbst invertiert G nicht; seine gemischte Spuridentität bleibt auch modulo 79 richtig. Nur die separable Drei-Faser-Klassifikation aus Abschnitt 2 schließt 79 aus.

Für n≥m folgt unmittelbar aus \(Y^*Y=4I\):

\[
\boxed{r_n^TG\bar r_m
=\operatorname{tr}(Y^n(Y^m)^*)=4^mP_{n-m}.}
\]

Für ungerades N ist 4^m eine reelle Einheit. Deshalb

\[
\boxed{\gcd\bigl(N,\Im(r_n^TG\bar r_m)\bigr)=\gcd(N,b_{n-m}).}
\]

Die enorme Zahl 4^m muss **weder berechnet noch invertiert werden**. Der neue Leser benötigt keine erneute Potenzierung zum Differenzindex. Matrix–Vektor-Produkt und Skalarprodukt kosten genau zwölf Gaußmultiplikationen, also 48 reelle modulare Produkte in der hier durchgängig verwendeten einfachen Vierproduktkonvention; Multiplikation mit festen Konstanten wird dabei ebenfalls voll gezählt. Hinzu kommen Additionen und ein ggT. Pro behaltenem Lift werden sechs Reste modulo N gespeichert.

Dies ist eine konstante Zahl modularer Produkte **bei gegebenen beiden Lifts**; ihre Erzeugung kostet weiterhin O(log m+log n) Kubikringmultiplikationen. Der Prozess bleibt in der schon bekannten relativen SU(3)-Rückkehrfamilie: Das Original `su3_selector_20260909w/MATHEMATIK.md`, Abschnitt 1, beschreibt bereits det(A−B) als Rückkehr von B⁻¹A. Neu hier ist die genaue gespeicherte Gram-Paarung und die geprüfte Kosteneinsparung für dieses feste W. Keine neue ganze Algorithmusklasse wird aus der Identität behauptet.

## 5. Ein vollständiger exakter Erfolgszeuge

Für die öffentliche Eingabe N=7117 und die öffentlichen Indizes m=81,n=108 gilt

\[
b_{81}\equiv b_{108}\equiv0\pmod{7117}.
\]

Beide alten Leser liefern nur 7117. Dagegen ist d=gcd(81,108)=108−81=27 und

\[
b_{27}\equiv1122\pmod{7117},\qquad\gcd(7117,1122)=11.
\]

Der neue Gramleser berechnet direkt

\[
r_{108}^TG\bar r_{81}\equiv3110+4807i\pmod{7117},
\qquad\gcd(7117,4807)=11.
\]

Die beiden skalaren P-Spuren sind zuvor reell modulo N; ihre einfache Produktpaarung würde deshalb keinen Imaginärrest erzeugen. Die vollständige Quell-Gram-Paarung erhält die benötigte Richtungsinformation.

| Derselbe vorgegebene Versuch | Reelle modulare Produkte |
|---|---:|
| Beide ursprünglichen Potenz-Lifts und Spurauslesen | 1164 |
| Danach b₂₇ durch erneute Binärpotenz | zusätzlich 492, insgesamt 1656 |
| Danach gemischte Gram-Spur | zusätzlich 48, insgesamt 1212 |

Die drei ggT mit N und die einfache Indexarithmetik kommen hinzu. Die Zusatzstufe spart in dieser deklarierten Implementierung den Faktor 10,25 an modularen Produkten; der Gesamtvergleich 1212 statt 1656 betrifft **denselben festgelegten Versuch**, keinen Laufzeitvorteil gegenüber Pollard, ECM oder GNFS.

Zur Erklärung des Zeugen: 7117=11·647. Bei 11 liegt der Transpositionsfall mit r₁₁=3 und ganzer Matrixordnung 30 vor. Bei 647 ist die reelle Kubik vollständig gespalten; ihre Eigenordnungen sind 324,81,108. Deshalb kehren dort unterschiedliche Richtungen bei 81 und 108 zurück, keine jedoch bei 27. \((79/7117)=-1\) passt zum öffentlichen Zusatzsatz.

**Auswahlgrenze:** Dieses kleine Beispiel wurde gezielt über lokale Diagnosen ausgewählt. Es ist keine vorab eingefrorene blinde Faktorisierungskampagne. Der ausführbare Leser erhält ausschließlich N,m,n; die Faktoren und Eigenordnungen befinden sich nur im getrennten Prüfer. Ein schneller universeller Produzent solcher nützlichen Ausgangsindizes ist nicht entstanden.

## 6. Exakte Kontrollen, Vorarbeiten und verbleibende Frage

`gcd_index_reader.py` führt beide öffentlichen Leser aus; `--retained-lifts` wählt die neue Gramstufe. `check_local_returns.py` enthält ausschließlich eigenen Quellcode und symbolische/elementare Kontrollen. Es importiert keine fremden Versuchsskripte. Er prüft:

- die ursprüngliche SU(3)-Matrix, ihre exakte Cayley- und Kubikform, beide Diskriminanten und das vollständige native Gram;
- 27 ausdrücklich geprüfte kleine Primstellen, darunter sämtliche ungeraden p≤101 außer 79 sowie 227,647,1087; für jede zwei **vollständige Matrixordnungsperioden**, zusammen 81.820 aufeinanderfolgende Rückkehrindizes;
- Frobeniustyp, exakte Matrix- und Eigenordnungen, den Transpositionsquotienten und die ggT-Eigenschaft;
- 42 Gramvergleiche gegen eine separat implementierte direkte Matrixpotenz, einschließlich zusammengesetzter N, N=79 und Indizes über 2¹²⁸;
- alle Zahlen und Produktkosten des oben angegebenen öffentlichen Erfolgszeugen.

Die Ergebnisse liegen in `local-return-checks.json`, `local-return-stdout.json`, `public-reader-demo.json` und `retained-lift-demo.json`. Die allgemeinen Sätze beruhen auf den ausgeschriebenen Beweisen; die endlichen Kontrollen sind keine Extrapolation zu allen Primstellen.

Der Forschungsgraph wurde mit einer englischen und einer deutschen Torusanfrage, einer Cayleyanfrage und einer gesonderten Rückkehr-/ggT-Anfrage durchsucht. Gefunden wurden die ursprüngliche Kubikreduktion, die Zweiexponenten-Abdeckung, der bekannte relative Leser sowie frühere ordnungsbasierte Leser aus vollständigen skalaren Kollisionen. Kein Treffer wird als Beweis weltweiter Neuheit behandelt. Beim Statusabruf waren 26.971 Quellen erfasst, 22.653 als Volltext; die übrigen besitzen die in `graph-status.json` ausgewiesene teilweise oder reine Metadatenabdeckung. Keine veraltete kuratierte Quelle wurde gemeldet. Drei unmittelbar verwendete Originalberichte sind mit SHA-256 im Ergebnis gebunden. Es erfolgte keine native Registrierung.

Die Literaturfamilie cyclotomischer Faktorisierungsverfahren ist schon in [Bach–Shallit, *Factoring with Cyclotomic Polynomials* (1989)](https://www.ams.org/journals/mcom/1989-52-185/S0025-5718-1989-0947467-1/S0025-5718-1989-0947467-1.pdf) vorhanden; der Primärquellen-Suchindex belegt Titel, Autoren und Gegenstand, der direkte Volltextabruf blieb 403. Aus dieser ungelesenen Vollfassung wird hier kein Laufzeitsatz übernommen.

Der neue konkrete Übergang lautet: **behaltene Operationskoeffizienten → richtige gemischte Gramantwort → zusätzliche Rückkehrrelation zum konstanten Lesepreis**. Offen bleibt eine aus N allein begründete Strategie, die geeignete Ausgangslifts häufig genug und insgesamt günstiger als die bestehenden Faktorisierungsverfahren erzeugt. Die Torusklassifikation liefert genaue Bedingungen dafür, aber keine versteckte Lösung ihrer Index- oder Glattheitsauswahl.
