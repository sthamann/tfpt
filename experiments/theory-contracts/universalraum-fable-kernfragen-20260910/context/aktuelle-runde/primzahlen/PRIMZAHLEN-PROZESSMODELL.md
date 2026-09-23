# Ein konkretes Prozessmodell für Primzahlen, Z₄ und Zetadynamik

Stand: 10. September 2026. Mathematische Konstruktion mit Beweisen und begrenzten exakten Kontrollen. Die Operatorenkonstruktion ist bekannt; ihr hier ausgearbeiteter Zustands- und Dynamikvergleich prüft einen konkreten TFPT-Anschluss. Das ist keine vollständige TFPT-Integration und kein RH- oder Faktorisierungsdurchbruch.

## 1. Die Operationen sind vollständig definiert

Auf \(\mathcal H=\ell^2(\mathbb N_{>0})\) mit orthonormaler Basis \(|m\rangle\) setzen wir

\[
S_n|m\rangle=|nm\rangle,\qquad
S_n^*|k\rangle=\begin{cases}|k/n\rangle&n\mid k,\\0&n\nmid k.\end{cases}
\]

Damit gelten als Gleichheiten beschränkter Operatoren

\[
S_n^*S_n=I,\quad S_nS_n^*=P_{n\mid\cdot},\quad
S_mS_n=S_{mn},\quad
S_m^*S_n=S_{n/d}S_{m/d}^*,\quad d=\gcd(m,n).
\tag{1}
\]

**Beweis:** Multiplikation mit \(n\) bildet die Basis injektiv auf die durch \(n\) teilbaren Basisindizes ab. Für die letzte Gleichung ist \(m\mid nk\) genau dann erfüllt, wenn \(m/d\mid k\); beide Seiten liefern dann \(|nk/m\rangle\), sonst null. Basisgleichheiten setzen sich wegen Beschränktheit auf ganz \(\mathcal H\) fort.

Die Isometrie \(S_n\) erhält das Skalarprodukt. Für \(n>1\) ist sie nicht surjektiv; ihr Adjungierter ist deshalb kein überall invertierender Rückweg. Die Algebra \(\mathcal T_\times=C^*(S_n:n\ge1)\) ist ein konkretes Semigruppenmodell. Weil alle \(S_m,S_n\) kommutieren, beschreibt dieser Sektor insbesondere keine beliebige Reihenfolge nichtkommutierender physikalischer Operationen.

## 2. Primzahlen sind exakt die irreduziblen Bausteine

Eindeutige Primfaktorzerlegung gibt eine explizite unitäre Transformation

\[
V|n\rangle=\bigotimes_{p\in\mathcal P}|v_p(n)\rangle.
\tag{2}
\]

Rechts steht das unvollständige Tensorprodukt \(\bigotimes_p(\ell^2(\mathbb N_0),|0\rangle)\), also der Hilbertraum mit Basis aller endlich unterstützten Besetzungslisten. Die Abbildung ist unitär, weil sie zwei orthonormale Basen bijektiv aufeinander abbildet. Sie zerlegt

\[
S_n=\prod_p S_p^{v_p(n)},\qquad VS_pV^*=\text{einseitiger Shift im }p\text{-Faktor}.
\]

Für verschiedene Primzahlen kommutieren auch \(S_p^*\) und \(S_q\). Der Shift ist der polare Isometrieanteil eines bosonischen Erzeugungsoperators; er enthält dessen Besetzungsfaktor \(\sqrt{k+1}\) nicht. Damit ist „Primzahl = unabhängiger elementarer Multiplikationsbaustein“ hier ein bewiesener Satz über einen definierten Prozessraum.

**Woher kommt die Arithmetik?** In dieser Präsentation ist \(\mathbb N_{>0}\) mit Multiplikation ein Eingang. Es wurde keine unabhängige Primzahlliste gewählt, aber auch nicht die Existenz dieses Monoids aus einem vierdimensionalen Cap bewiesen.

Eine geometrische Herkunft desselben Monoids ist möglich: Die stetigen, positiv orientierten Gruppen-Selbstüberlagerungen von \(U(1)\) sind genau \(f_m(z)=z^m\), \(m\ge1\). Denn ein angehobener stetiger Gruppenhomomorphismus hat die Form \(\theta\mapsto a\theta\), und Periodizität erzwingt \(a\in\mathbb Z\); positive Überlagerung erzwingt \(a>0\). Es gilt \(f_m\circ f_n=f_{mn}\). Nichttriviale, nicht weiter zerlegbare Überlagerungen sind somit exakt die Primgrade. Der Haar-Pullback auf \(L^2(U(1))\) wirkt in Fourierkoordinaten als \(|k\rangle\mapsto|mk\rangle\), jetzt mit \(k\in\mathbb Z\).

Dies erklärt die Primgrade aus einer angegebenen geometrischen Operationsklasse. Dass **alle** diese Selbstüberlagerungen erlaubte Operationen eines gegebenen physikalischen Modells sind, bleibt eine zusätzliche Modellannahme. Ein vorhandener Kreis allein beweist deren physikalische Zulässigkeit nicht.

**Vorhandene interne Vorarbeit:** Der [Round17-Audit vom 6. September, §4](</Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/work/e8_relative_trace_20260906/round17_delta_audit.md>) enthält bereits den globalen Integer-Cover für die dortigen \(U(1)^8\)-Linkrotoren, seine Verträglichkeit mit dem Null-Gauss-Sektor und die quadratische Energieskalierung. Diese Konstruktion ist somit keine neue TFPT-Entdeckung dieses Berichts. Der dortige Cover hat kinematischen Grad \(n^{8M}\) und physischen Gitterindex \(n^8\). Ein Primgrad \(p\) unseres einzelnen Kreises darf nicht als Gitterindex \(p\) des vollständigen E₈-Ladungsmodells ausgegeben werden. Außerdem dokumentiert die Vorarbeit bei geraden Faktoren eine Obstruktion für den unveränderten geladenen Kokzyklus. Hier wurde der historische Audit gelesen; eine neue Validierung aller aktuellen nativen Quelldateien gehört zum parallelen Integrationsstrang.

## 3. Die logarithmische Dynamik und ihre Partition

Definiere die Zahlobservable \(\mathsf N|m\rangle=m|m\rangle\) auf ihrer maximalen Domain \(\{\psi:\sum_m m^2|\psi_m|^2<\infty\}\) und

\[
H=\log\mathsf N,\qquad
\operatorname{Dom}H=\left\{\psi:\sum_m(\log m)^2|\psi_m|^2<\infty\right\}.
\]

Dieser diagonale Operator ist selbstadjungiert, nichtnegativ und hat kompakten Resolventen. Sein Spektrum besteht aus den einfachen Eigenwerten \(\log m\), die gegen unendlich gehen. Auf \(\operatorname{Dom}H\) gilt

\[
HS_n=S_n(H+\log n),\qquad
e^{itH}S_ne^{-itH}=n^{it}S_n,
\qquad VHV^*=\sum_p(\log p)N_p.
\tag{3}
\]

Dabei erhält \(S_n\) die angegebene Domain: \(\log(nm)=\log n+\log m\). Die letzte Summe bezeichnet den diagonalen selbstadjungierten Operator mit dieser Domain, keine unbegründete Summe unbeschränkter Operatoren.

Für \(\beta>1\) folgt

\[
Z(\beta)=\operatorname{Tr}(e^{-\beta H})
=\sum_{m\ge1}m^{-\beta}
=\prod_p(1-p^{-\beta})^{-1}=\zeta(\beta).
\tag{4}
\]

**Beweis des Produkts:** Für jede endliche Primzahlmenge multipliziert man absolut konvergente geometrische Reihen. Eindeutige Zerlegung ordnet deren Terme den Zahlen mit genau diesen erlaubten Primteilern zu. Monotone Konvergenz liefert das vollständige Produkt. Für komplexes \(s\) trägt absolute Konvergenz denselben Beweis auf \(\Re s>1\). Die positive Reihe ist genau für \(\beta>1\) summierbar.

Der normale Gibbszustand lautet \(\rho_\beta=\zeta(\beta)^{-1}\mathsf N^{-\beta}\). In (2) sind seine Primzahlbesetzungen unabhängig und haben Verteilung \((1-p^{-\beta})p^{-k\beta}\). Für \(\beta\le1\) gibt es diese normierte Spurformel nicht; daraus folgt kein Ausschluss algebraischer KMS-Zustände.

Die Energieeinheit ist hier eins. Für \(H_{\rm phys}=E_0\log\mathsf N\) erscheint \(\zeta(\beta_{\rm phys}E_0)\). Nullpunkt und Energie-/Zeitskala sind weitere Festlegungen.

**Komposition allein erzwingt den Logarithmus nicht:** Jede additive Länge des Multiplikationsmonoids ist

\[
\tau(n)=\sum_pv_p(n)a_p
\]

mit frei wählbaren \(a_p\). Erst Monotonie in der gewöhnlichen Zahlenordnung erzwingt \(\tau(n)=c\log n\), \(c\ge0\): Aus \(2^{j_k}\le n^k<2^{j_k+1}\), \(j_k=\lfloor k\log_2n\rfloor\), folgt \(j_k\tau(2)\le k\tau(n)\le(j_k+1)\tau(2)\); Teilen durch \(k\) und Grenzübergang beweisen die Behauptung. Bei Nichttrivialität ist \(c>0\). Die Zahlenordnung ist dabei zusätzliche arithmetische Struktur. Beispielsweise sind \(a_p=1\) ebenfalls positive additive Gewichte, ergeben aber unendlich viele unabhängige Zustände der Energie eins und keine endliche Gibbs-Spur.

## 4. Phasen machen den Anschluss zu Bost–Connes explizit

Für \(r\in\mathbb Q/\mathbb Z\) setze

\[
E(r)|m\rangle=e^{2\pi irm}|m\rangle.
\]

Direkte Berechnung ergibt

\[
E(r)S_n=S_nE(nr),\qquad S_n^*E(r)S_n=E(nr),
\]
\[
S_nE(r)S_n^*=\frac1n\sum_{ns=r}E(s).
\tag{5}
\]

Für die letzte Gleichung schreibt man \(s=(r+j)/n\), \(0\le j<n\). Die Summe der \(n\)-ten Einheitswurzeln verschwindet außer für \(n\mid m\); dann ergibt sie genau die Phase \(e^{2\pi ir(m/n)}\). Insbesondere ist \(S_nE(0)S_n^*=P_{n\mid\cdot}\), nicht die Identität.

Die Phasenalgebra ist \(C^*(\mathbb Q/\mathbb Z)\cong C(\widehat{\mathbb Z})\). In dieser Darstellung ist sie treu: Positive ganze Zahlen treffen jede endliche Restklasse, liegen also dicht in \(\widehat{\mathbb Z}\); eine stetige Funktion, die dort verschwindet, verschwindet überall. Die Abbildung \(a\mapsto S_naS_n^*\) ist auf ihr ein nichtunitärer, nichtunitaler Endomorphismus. Die gemeinsame Algebra \(C^*(S_n,E(r))\) realisiert damit konkrete Semigruppen-Kovarianzrelationen. Für \(\alpha_t=\operatorname{Ad}(e^{itH})\) sind die Phasen zeitfest und \(\alpha_t(S_n)=n^{it}S_n\); auf der erzeugten C*-Algebra ist die Gruppe punktnormstetig.

**Primärquellenabgleich:** Bost und Connes geben die Primzahl-Shifts und Toeplitzzerlegung in Proposition 7 an; Proposition 18 enthält die Relationen (5), Proposition 23 genau die obige Darstellung. Abschnitt 6, Gleichungen (3)–(5), verwendet den logarithmischen Hamiltonoperator, und Theorem 25 konstruiert die Gibbszustände für \(\beta>1\). Der Artikel behandelt außerdem algebraische Gleichgewichtszustände außerhalb dieses normalen Spurregimes. Unsere Basisrechnungen prüfen die hier benötigten Identitäten unmittelbar; die vollständige Phasenklassifikation wird nicht benötigt. [Original, IHES/M/95/38 (1995), S. 8–9, 21–24 und 31–33](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf).

## 5. Ein echter Z₄-Sektor — mit nachweisbarer Zustandslücke

Wähle \(Q=E(1/4)\). Dann

\[
Q|m\rangle=i^m|m\rangle,\quad Q^4=I,\quad
P_r=\frac14\sum_{j=0}^3i^{-jr}Q^j,
\quad P_r|m\rangle=\mathbf1_{m\equiv r\;(4)}|m\rangle.
\]

Alle vier Projektionen sind ungleich null. Daher ist \(C^*(Q)\cong\mathbb C[\mathbb Z_4]\cong\mathbb C^4\), und die Multiplikationsoperationen erfüllen exakt

\[
QS_n=S_nQ^n. \tag{6}
\]

Das ist eine gemeinsame Operatorstruktur. Der übliche gleichgewichtete Zustand des endlichen Z₄-Gruppenmodells hat \(h(P_r)=1/4\). Dagegen ist der vom normalen Zetazustand induzierte Zustand

\[
w_r=\omega_\beta(P_r)
=\frac{\sum_{m\equiv r\;(4)}m^{-\beta}}{\zeta(\beta)},
\quad w_0=4^{-\beta},\quad w_2=2^{-\beta}-4^{-\beta}.
\tag{7}
\]

Für \(\beta>1\) gilt \(w_0<1/4\). Die natürliche Restklasseneinbettung erhält den gleichgewichteten Zustand somit **nicht**. Die Aussage betrifft genau diese Einbettung und dieses normale Gibbsregime; sie schließt andere Zustände oder Erweiterungen nicht aus.

Noch präziser: Sei auf \(\mathbb C^4\) die Basis aus minimalen Projektionen \(e_r\), die Multiplikation \(m(e_r\otimes e_s)=\delta_{rs}e_r\) und das Skalarprodukt \(\langle e_r,e_s\rangle=\delta_{rs}w_r\), \(w_r>0\), \(\sum_rw_r=1\). Dann

\[
m^\dagger e_r=w_r^{-1}e_r\otimes e_r,\quad
\|m^\dagger1\|^2=\sum_r w_r^{-2}w_r^2=4,
\quad mm^\dagger e_r=w_r^{-1}e_r.
\tag{8}
\]

**Folge:** Das Cap-Normquadrat vier bleibt für beliebige treue Gewichte gleich. Erst die stärkere Identität \(mm^\dagger=4I\) erzwingt \(w_r=1/4\). Eine Übereinstimmung der einzelnen Zahl vier beweist daher keine Gleichheit von Zustand und Frobenius-Dynamik. Beim natürlichen Gibbszustand scheitert bereits diese stärkere Identität.

Auf einem festen endlichdimensionalen Raum ist außerdem jede Isometrie surjektiv (Rangargument). Die echten \(S_n\) für \(n>1\) lassen sich dort nicht als solche realisieren. Eine unendliche Erweiterung muss angegeben werden; eine vorhandene endliche Algebra genügt nicht.

### Konstruktive Ergänzung: Addition und KMS reparieren die gleichmäßigen Gewichte

[Cuntz, Definition 3.1 und Proposition 4.2](https://arxiv.org/pdf/math/0611541) behandelt den größeren Baukasten mit unitärem \(U\), \(S_mU=U^mS_m\) und
\[
\sum_{r=0}^{m-1}U^rS_mS_m^*U^{-r}=I.
\]
Er besitzt einen 1-KMS-Zustand für \(\alpha_t(U)=U\), \(\alpha_t(S_m)=m^{it}S_m\). Ein unmittelbarer bedingter Beweis erklärt den Logarithmus: Für \(\alpha_t(S_m)=e^{it\varepsilon_m}S_m\) und einen \(\beta\)-KMS-Zustand, \(\beta>0\), gilt
\[
\omega(S_mS_m^*)=e^{-\beta\varepsilon_m},\quad
1=m e^{-\beta\varepsilon_m},\quad
\varepsilon_m=\frac{\log m}{\beta}.
\]
Die mittlere Gleichung folgt aus KMS-Invarianz unter Konjugation mit dem zeitfesten \(U\). Für \(T_r=U^rS_m\) folgt ebenfalls \(\omega(T_rT_s^*)=\delta_{rs}/m\). Bei \(m=4\) ist somit der **vierdimensionale diagonale Sektor** gleichgewichtet; die gesamte Matrixalgebra \(M_4\) hat hingegen Dimension 16.

Dieser Zustand ist in der Rotorrepräsentation kein normaler Dichteoperatorzustand: Für festes \(n\in\mathbb Z\) fallen \(U^nS_{k!}S_{k!}^*U^{-n}\) stark gegen \(|n\rangle\langle n|\), ihre Gewichte \(1/k!\) gegen null. Normalität ergäbe sämtliche Diagonaleinträge null, entgegen Spur eins.

Damit ist (7) kein allgemeines Hindernis. Ein anderer algebraischer Zustand repariert die endlichen Gewichte. Die additive Struktur und KMS-Annahme ersetzen hier die gewöhnliche Ordnungsannahme; ihre Herleitung aus TFPT bleibt offen, ebenso der Abgleich mit dessen tatsächlichem Zustand und elektrischer Zeit.

## 6. Die Zeitentwicklung passt noch nicht zur elektrischen Rotorenergie

Für den geometrischen Rotor \(\ell^2(\mathbb Z)\), \(E_{\rm rot}|n\rangle=n|n\rangle\), verschiebt der Kreisoperator \(U|n\rangle=|n+1\rangle\) die Ladung. Der positive Ladungssektor \(\ell^2(\mathbb N_{>0})\) ist für die Cover-Isometrien invariant, aber nicht für beide \(U\) und \(U^*\): Schon \(U^*|1\rangle=|0\rangle\) verlässt ihn. Die Zetadarstellung ist deshalb keine unveränderte Darstellung aller Rotoroperationen.

Die elektrische Energie \(H_{\rm el}=\kappa E_{\rm rot}^2\), \(\kappa>0\), liefert auf diesem Sektor

\[
\operatorname{Ad}(e^{itH_{\rm el}})(S_2)|n\rangle
=e^{it3\kappa n^2}|2n\rangle,
\]

während (3) die für alle \(n\) gleiche Frequenz \(\log2\) liefert. Bereits \(n=1,2\) unterscheiden \(3\kappa\) von \(12\kappa\). Selbst eine konstante Zeit-/Energieskalierung mit Nullpunktverschiebung behebt dies nicht: \(a\log n+b=\kappa n^2\) für \(n=1,2,4\) erzwingt \(b=\kappa\), \(a\log2=3\kappa\), aber \(2a\log2=15\kappa\), einen Widerspruch.

Damit ist eine Identifikation **dieser** Operatoren mit **derselben** physikalischen Zeit ausgeschlossen. Eine alternative Dynamik, größere Darstellung oder weitere Zeitvariable müsste eigens aus TFPT begründet werden. Die bloße gemeinsame Kreis-/Z₄-Struktur leistet das nicht.

## 7. Was sich damit lösen und was sich noch nicht lösen lässt

Das Modell löst das präzise Übersetzungsproblem zwischen Multiplikation, unabhängigen Primzahlbesetzungen, Kreisüberlagerungen und Restklassenoperatoren. Zu einem **bekannten** Primwert \(p\) selektiert \(P_{p^k}-P_{p^{k+1}}\) genau die Besetzungszahl \(v_p(n)=k\).

Die Transformation (2) aus binär eingegebenem \(n\) effizient zu implementieren, würde jedoch bereits seine Primzerlegung berechnen. Ein abstrakt expliziter Basiswechsel ist noch kein effizienter klassischer oder quantenmechanisch realisierter Algorithmus. Zulässige Gatter, Präparation, Auslesen und Kosten fehlen für eine neue Faktorisierungsmethode.

Ebenso ist \(\zeta(s)\) hier eine analytisch fortsetzbare Zustandssumme; ihre Nullstellen sind nicht Eigenwerte von \(H\). Positivität von \(H\), Gibbszustand und Eulerprodukt liefern keine RH-Folgerung. Eine weitere, response-erhaltende spektrale Zuordnung mit den richtigen vollständigen arithmetischen Termen bleibt offen. P versus NP und die vollständige gravitative TFPT-Dynamik sind dadurch nicht entschieden.

**Der nächste konkrete Integrationsschritt:** Aus den tatsächlichen TFPT-Operationen die Zulässigkeit der vollständigen Cover-/Translationsstruktur sowie deren kompatiblen KMS-Zustand und Zeitgenerator ableiten. Die algebraische Reparatur existiert; ihre Übereinstimmung mit den markierten TFPT-Operationen, deren Zustand und elektrischer Dynamik ist noch nicht bewiesen.

## Prüfgrenze

Die allgemeinen Beweise stehen im Text. `check_prime_process.py` kontrolliert zusätzlich exakte endliche Beispiele und symbolische Identitäten, ohne abgeschnittene quadratische Shiftmatrizen als unendliche Isometrien auszugeben. `checks.json` enthält Ergebnisse und Dateihashes. Kein endlicher Test ersetzt hier den allgemeinen Beweis oder einen offenen RH-/TFPT-Satz.
