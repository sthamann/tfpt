# Universalraum: gezielter Beweisversuch einer gemeinsamen Quelle

**15. September 2026 · Untersuchung auf Grundlage v1.6 bis v1.6.4**

## Ergebnis

Eine vollständige gemeinsame Lösung von TFPT, Raumzeit, Gravitation, RH und Faktorisierung ist in dieser Untersuchung **nicht gelungen**. Aus den vorliegenden Voraussetzungen folgt sie bisher auch nicht. Es gibt jedoch konkrete zusätzliche Ergebnisse: einen ausgeschriebenen Ausschlusssatz für die direkte Identifikation des nativen und des logarithmischen Generators, eine präzise phasentreue arithmetische Konstruktion samt Auslesung und eine kontrollierte Näherung für die native Antwort.

Der stärkste neue Schluss dieser Untersuchung lautet:

> Eine Bank mit den vorgegebenen 64 Fermion- und 60 Bosonmoden kann unter ihrem unveränderten Hamiltonoperator nicht das vollständige Spektrum \(E_*\log n\) tragen. Das gilt trotz ihres unendlichdimensionalen Boson-Fockraums. Unter einer Energiegrenze wächst ihre Zustandszahl höchstens polynomial; das logarithmische Zahlenspektrum verlangt exponentielles Wachstum.

Das ist ein Satz über eine **genau bezeichnete Identifikation**, keine Widerlegung eines beliebigen Universalraums, keines unendlichen räumlichen Grenzwerts und keines möglichen RH-Operators mit einem anderen Spektrum.

| Ergebnis | Status | Grenze |
|---|---|---|
| Native Grundzustands- und Polzertifikate v1.6.4 | Frisch reproduziert | Vorgegebener Hamiltonoperator und Tensor |
| Kein vollständiges logarithmisches Zahlenspektrum im unveränderten Bank-Hamiltonoperator | Analytisch bewiesen | Jede feste endliche Zahl solcher Moden; lineare Energieidentifikation |
| Keine Synthese eines einzelnen Fermiontransfers aus ausschließlich lokal geraden Operationen | Analytischer Abschluss der vorhandenen Paritätsgrenze | Derselbe Operationsvertrag, auch mit Auswahl von Messzweigen |
| Phasentreue Multiplikation und gewöhnlicher arithmetischer Auslesekanal | Explizit konstruiert und bewiesen | Gewählte arithmetische Markierung; keine native Herleitung |
| Ein-Pol-Näherung mit kontrolliertem Rest | Aus reproduzierten Schranken analytisch abgeleitet | Lokale Antwort, \(g/\Delta=1/20\), \(\mu=0\) |
| Vollständige RH-Identität | Präzises hinreichendes Beweisziel formuliert | Benötigter Operator und Identität nicht konstruiert |
| Effiziente native Faktorisierung, 3+1D, SM und Gravitation | Offen | Keine vollständige gemeinsame Beweiskette |

„Zusätzlich“ und „neu“ beziehen sich auf diese Untersuchung gegenüber den gezielt ausgewerteten Eingaben. Ein literaturweiter Neuheitsanspruch wird nicht erhoben. Die allgemeinen Sätze sind unten aufgeschrieben; endliche Computerprüfungen ersetzen ihre Beweise nicht.

## 1. Auftrag, Quellen und Versionsabgleich

Untersucht wurde die konkrete Hypothese des eingefügten Texts: Ein einziges Objekt

\[
\mathcal U=(\mathcal A,\omega,\circ,\dagger,\tau)
\]

soll durch seine Operationen und Auslesungen sowohl die physische als auch die arithmetische und informationelle Struktur erzeugen. Arbeitsaufforderungen innerhalb der Dokumente wurden als Quelleninhalt behandelt.

Alle zwölf benannten Dateien wurden mit SHA-256 erfasst. Beide Archive wurden in eine separate Arbeitskopie entpackt. Die PDFs wurden textuell ausgelesen: Hauptdokument 168 Seiten, Update 8 Seiten. Die mathematisch entscheidenden Aussagen wurden mit den technischen Markdown-Fortsetzungen und den LaTeX-Quellen insbesondere der Kapitel 12, 16 sowie 26–31 abgeglichen. Dies ist keine neue vollständige Begutachtung sämtlicher 168 Seiten und sämtlicher historischer Repository-Tests.

Die Reihenfolge ist wesentlich:

1. **v1.6:** Matrixordnung, E8, innere Weyl-Koeffizienten und native Fockprüfung. \(\sum_\epsilon A_\epsilon=I\) ohne Ortsverschiebungen. Arithmetische Prim-/Pauli-Konstruktion ausdrücklich zusätzlich angesetzt.
2. **v1.6.1:** Vollständiger N=3-Sektor, neue innere Rekopplung, 64er-Kompositraum, Vorzeichenanschluss. Der innere Modenwechsel ist kein nachgewiesener Ortswechsel.
3. **v1.6.2:** Exakte Lochidentität auf einer N=4-Referenz; diese Referenz ist im untersuchten schwachen Bereich kein globaler Grundzustand. Eine schöne endliche Antwort auf dieser Referenz darf nicht mit der Antwort auf dem nativen Grundzustand identifiziert werden.
4. **v1.6.4 einschließlich archivierter v1.6.3:** Geladene Antwort auf dem N=64-Modellgrundzustand, isolierter Entnahmepol, drittes Moment, strengere Gewichte und Beweis gegen eine exakt zweilinige Antwort. Der Clock-Kontrollvertrag hat Dimension 84; Dimension 14 gilt weiterhin für den engeren Zweikontrollvertrag.

Das fehlende Pluszeichen in der Resolventenformel v1.6.2 wurde entsprechend dem ausdrücklichen Erratum v1.6.4 gelesen.

## 2. Was frisch reproduziert wurde

Die Quellenpins der ursprünglichen Grundzustandsprogramme wurden gegen ihre lokalen Originale geprüft. Die Normenumeration wurde neu kompiliert und für Ordnungen 2, 3 und 4 frisch ausgeführt. Die Normquadrate sind wiederum

\[
1,\quad480,\quad439680,\quad575078400,\quad952296652800.
\]

Anschließend liefen die vier ursprünglichen Grundzustandszertifikate, der zugelieferte Polprüfer und die vier Antwort-/Anschlussprüfer normal und optimiert. Die neun verglichenen fachlichen JSON-Berichte sind **auch byteidentisch zu den Berichten im zugelieferten v1.6.4-Archiv**.

| Prüfung | Frisches Ergebnis |
|---|---|
| Vollständige Normenumeration bis Ordnung vier | Bestanden |
| `general_identities`, `vacuum_sector`, `weak_coupling`, `moment_trace` | Normal/optimiert identisch; der Sektorprüfer zählt 2549 Bedingungen |
| Zugelieferter nativer Pol | 317 Bedingungen, normal/optimiert identisch |
| Geladene Antwort | 831 Bedingungen, normal/optimiert identisch |
| Feldzuordnung | 250 Bedingungen, normal/optimiert identisch |
| Operationsgrenze | 6 Bedingungen, normal/optimiert identisch |
| Polkonsolidierung | 81 Bedingungen, normal/optimiert identisch |
| Eigene ergänzende symbolische/endliche Gegenprüfungen | 1149 Bedingungen, normal/optimiert identisch |

Die Zahlen zählen auch Komponenten und wiederholte Fälle; insbesondere 1000 der eigenen Bedingungen prüfen dieselbe Kokzyklusidentität an verschiedenen Tripeln. Sie sind keine Zahl unabhängiger Entdeckungen.

Der erste Reproduktionsversuch mit dem gebündelten PDF-Python scheiterte an fehlendem SymPy. Der Fehlerstatus wurde bewahrt; die vollständige Wiederholung erfolgte erfolgreich mit dem vorhandenen Python einschließlich NumPy, SciPy und SymPy. Bei der eigenen symbolischen Prüfung musste außerdem eine mathematisch äquivalente, aber unausgewertete Logarithmusdarstellung vor dem Nullvergleich vereinfacht werden. Die endgültigen Prüfungen sind erfolgreich; aus diesen Zwischenfehlern wird kein inhaltlicher Gegenbeweis abgeleitet. Die bekannte ComplexWarning des alten Normprüfers bleibt in dessen Protokoll enthalten.

### 2.1 Bestätigter lokaler Vertrag

\[
H_{\rm nat}=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),
\qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\]

\[
N=N_f+2N_b,\qquad WW^\dagger=8I_{60},\qquad
\operatorname{SHA256}(W\text{-Quelldatei})=
\texttt{3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763}.
\]

Am Prüfpunkt gilt \(g/\Delta=1/20\), ausdrücklich \(\mu=0\). Der modellinterne eindeutige Grundzustand liegt bei N=64. Die reproduzierten Schranken sind

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\quad \operatorname{gap}(H)>0.007737\Delta,
\]

\[
0.842846<\langle N_b\rangle<1.245656,
\]

\[
0.007737<\epsilon_{\rm low}/\Delta<\frac{2403745}{61508688},
\quad Z_{\rm low}>\frac{40912436089}{46487375000}>0.880076280689.
\]

Das ist ein belastbarer lokaler Ausgangspunkt. Präparation, Detektorzugriff, räumliche Ausbreitung und Herkunft des Hamiltonoperators sind dadurch nicht zusätzlich bewiesen.

## 3. Ausschlusssatz: Ein endlicher nativer Modensatz trägt nicht das vollständige Logarithmusspektrum

### Satz 1 — Zustandszählung und Wärmespur

Für den obigen Hamiltonoperator mit endlich vielen Fermionmoden und 60 Bosonmoden ist die Zahl \(\mathcal N_H(E)\) der Eigenzustände mit Energie höchstens E durch ein Polynom vom Grad 60 beschränkt. Seine Wärmespur existiert für jede positive inverse Temperatur. Insbesondere kann es keine isometrische Einbettung

\[
J:\ell^2(\mathbb N_{>0})\longrightarrow\mathcal H_{\rm nat}
\]

mit

\[
H_{\rm nat}J=J(E_{\rm off}+E_*\log n),\qquad E_*>0,
\tag{1}
\]

auf allen Zahlbasiszuständen geben.

### Beweis

**Schritt 1: Eine Energieuntergrenze.** Auf dem endlichen Teilchenkern gilt durch Quadratvervollständigung

\[
H_{\rm nat}=
\frac\Delta2N_b+
\frac\Delta2\sum_A\left(b_A+\frac{2g}\Delta P_A\right)^\dagger
\left(b_A+\frac{2g}\Delta P_A\right)
-\frac{2g^2}\Delta\sum_AP_A^\dagger P_A.
\]

Jeder \(P_A\) ist auf dem endlichen Fermion-Fockraum beschränkt. Deshalb

\[
H_{\rm nat}\ge\frac\Delta2N_b-CI,
\qquad C=\frac{2g^2}\Delta\sum_A\|P_A\|^2<\infty.
\tag{2}
\]

Für eine vollständig elementare Konstante genügt der frisch geprüfte Befund: Jede W-Zeile hat acht Einträge vom Betrag eins. Da \(\|f_jf_i\|\le1\), ist \(\|P_A\|\le8\). Damit darf man

\[
C=7680g^2/\Delta
\tag{3}
\]

verwenden. Die reproduzierte Casimirschranke \(\sum_AP_A^\dagger P_A\le480I\) verbessert C auf \(960g^2/\Delta\), wird für den Ausschluss aber nicht benötigt.

Der Konversionsterm ist relativ zu \(N_b\) mit beliebig kleiner relativer Schranke beschränkt: \(b_A,b_A^\dagger\) wachsen nur wie \((N_b+1)^{1/2}\), die \(P_A\) sind beschränkt. Somit ist H auf dem üblichen Oszillatordomänenabschluss selbstadjungiert und nach unten beschränkt. Die Formabschätzung (2) kontrolliert die kompakte Einbettung der Formdomäne; insbesondere hat H kompakte Resolvente. Das rechtfertigt den folgenden Eigenwertvergleich.

**Schritt 2: Zählen.** Bei insgesamt b Bosonen in 60 Moden gibt es

\[
\binom{b+59}{59}
\]

Bosonbasiszustände. Der Fermionfaktor hat Dimension \(2^{64}\). Der Minimaxsatz angewandt auf (2) liefert daher, für \(E+C\ge0\),

\[
\boxed{
\mathcal N_H(E)\le2^{64}
\binom{\left\lfloor2(E+C)/\Delta\right\rfloor+60}{60}.
}
\tag{4}
\]

Für \(E+C<0\) ist die Zählung null. Wichtig: Die Eigenvektoren von H müssen keine feste Bosonzahl besitzen. (4) folgt aus dem Variationsprinzip und behauptet nicht, dass jeder Eigenvektor strikt unterhalb eines Boson-Cutoffs liegt.

**Schritt 3: Widerspruch.** Aus (1) müssten mindestens

\[
\left\lfloor\exp((E-E_{\rm off})/E_*)\right\rfloor
\]

orthogonale Eigenzustände unterhalb E existieren. Diese Zahl wächst exponentiell, die rechte Seite von (4) höchstens polynomial. Für hinreichend großes E entsteht ein Widerspruch. Damit ist (1) unmöglich.

**Schritt 4: Wärmespur.** Der gleiche geordnete Eigenwertvergleich ergibt für jedes \(\beta>0\)

\[
\operatorname{Tr}e^{-\beta H_{\rm nat}}
\le2^{64}e^{\beta C}(1-e^{-\beta\Delta/2})^{-60}<\infty.
\tag{5}
\]

Die Spur ist holomorph für \(\operatorname{Re}\beta>0\). Sie kann deshalb keine Zeta-Zustandssumme mit einem Pol bei einer positiven inversen Temperatur sein. Hier wird keine unzulässige Operator-Monotonie der Exponentialfunktion vorausgesetzt: Verglichen werden die geordneten Eigenwerte. ∎

### 3.1 Ein endlicher ganzzahliger Zeuge

Für \(g/\Delta=1/20\), \(E_*=\Delta\) und \(E_{\rm off}=0\) genügt schon eine sehr grobe konkrete Energiegrenze. Aus \(\log2<1\) liegen alle Zahlen \(n\le2^{1024}\) im logarithmischen Modell unter \(1024\Delta\). Das wären \(2^{1024}\) Zustände.

Mit der elementaren Konstante \(C/\Delta=96/5\) ergibt (4) dagegen

\[
\mathcal N_H(1024\Delta)\le2^{64}\binom{2146}{60}<2^{455}.
\]

Die letzte Ungleichung wurde exakt mit ganzen Zahlen geprüft. Es wird kein Fockraum dieser Größe numerisch aufgebaut.

### 3.2 Was daraus folgt und was nicht

Dieser Satz betrifft **den gleichen Generator mit einer festen linearen Energieumrechnung**. Er schließt die direkte Identifikation mit dem Primzahl-Besetzungs-Hamiltonoperator aus. Er schließt nicht aus:

- eine unbegrenzt wachsende Zahl räumlicher Banken oder anderer Moden;
- einen anders hergeleiteten Generator auf derselben Hilbertraummenge;
- eine nichtlineare Spektralabbildung, eine relative Spur oder einen Liouvillian auf einem anderen Operatorraum;
- einen RH-Operator, dessen Eigenwerte Nullstellenhöhen statt \(\log n\) wären.

Jede dieser Varianten benötigt einen eigenen Herkunfts- und Verträglichkeitsbeweis. Eine bloße unitäre Umbenennung vorhandener Zustände ändert ihre Energiezählung nicht. Für jede feste endliche Zahl L solcher Banken bleibt bei entsprechender Oszillatoruntergrenze die Zählung polynomial, nun mit Grad \(60L\). Erst ein kontrollierter unendlicher Grenzwert kann diesem Argument entgehen.

## 4. Warum mehr Belegung die Ortslücke nicht automatisch schließt

### Satz 2 — Abschluss der lokalen Paritätsgrenze

Für getrennte Banken x setze \(\Pi_x=(-1)^{N_{f,x}}\). Angenommen, jeder verfügbare Generator und jeder einzeln implementierte Krauszweig kommutiert mit allen \(\Pi_x\). Dann gilt dies auch für alle daraus aufgebauten Wörter, linearen Kombinationen und die üblichen beschränkten Operatorgrenzwerte.

**Beweis.** Aus \([A,\Pi_x]=[B,\Pi_x]=0\) folgt
\([AB,\Pi_x]=A[B,\Pi_x]+[A,\Pi_x]B=0\). Summen und Grenzwerte erhalten die Relation. Jede konkrete adaptive Messgeschichte ist wieder ein Produkt ihrer einzelnen Krauszweige und Kontrollen. Ein Übergang zwischen entgegengesetzten lokalen Paritätseigenwerten hat deshalb Matrixelement null. ∎

Lokale Vertizes \(b_x^\dagger f_xf_x+\mathrm{h.c.}\) enthalten zwei Fermionoperatoren an x; reine Bosontransfers enthalten keinen. Sie erfüllen die Voraussetzungen. Ein Fermionhop \(f_y^\dagger f_x+\mathrm{h.c.}\) verändert dagegen die Parität an x und y und liegt außerhalb dieser Algebra.

Der in v1.6.1 bewiesene N=3-Rekopplungsweg widerspricht dem Satz nicht: Seine Labels sind innere Moden einer Bank. Eine höhere Belegung hebt einen exakten Kommutanten nicht auf. Auch gemeinsame Anfangsverschränkung ändert die Operatorrelation nicht.

Ein mikroskopisches gemeinsames Fermion, eine bereits primitive Kantenoperation mit ungeradem Anteil an beiden Enden oder eine andere Definition der operationalen Teile könnte dem Satz entgehen. Das wären konkrete neue Herkunftsdaten. Der Satz verbietet nicht sämtliche Bewegung, insbesondere keinen Paar- oder Bosontransfer, und er behandelt nicht beliebige topologische Kodierungen emergenter Teilchen.

**Engstes Experiment im Modell:** Ein tatsächliches Quellenwort K finden und an ihm \([K,\Pi_x]\ne0\), gemeinsame Ladungserhaltung, das gewünschte Transfermatrixelement und eine kohärenzerhaltende Recordstruktur nachweisen. Besteht das zugelassene Alphabet weiterhin nur aus lokal geraden Zweigen, ist diese Suche innerhalb dieses Alphabets bereits mathematisch entschieden.

## 5. Positive Konstruktion: Multiplikation mit Phase und genauer Auslesung

Der konstruktive Teil des eingefügten Texts lässt sich sauber durchführen. Er erklärt zugleich, warum dabei RH noch nicht folgt.

### Satz 3 — Eine explizite phasentreue arithmetische Algebra

Seien \(\nu_2(n),\nu_3(n)\) die Exponenten von 2 und 3 in n. Definiere

\[
c(m,n)=(-1)^{\nu_2(m)\nu_3(n)},
\qquad T_m|n\rangle=c(m,n)|mn\rangle
\]

auf \(\ell^2(\mathbb N_{>0})\). Es gilt

\[
c(l,m)c(lm,n)=c(m,n)c(l,mn),
\tag{6}
\]

denn die Exponenten addieren sich jeweils zu
\(\nu_2(l)\nu_3(m)+\nu_2(l)\nu_3(n)+\nu_2(m)\nu_3(n)\) modulo zwei. Daher ist die Komposition assoziativ und

\[
T_lT_m=c(l,m)T_{lm},\qquad T_2T_3=-T_3T_2.
\]

Jeder \(T_m\) ist eine Isometrie; \(T_m^\dagger T_m=I\), während \(T_mT_m^\dagger\) auf die durch m teilbaren Zahlen projiziert. Der selbstadjungierte Operator

\[
H_{\rm ar}|n\rangle=\log n\,|n\rangle,
\quad \mathcal D(H_{\rm ar})=\{\psi:\sum_n(\log n)^2|\psi_n|^2<\infty\}
\]

erfüllt

\[
[H_{\rm ar},T_m]=(\log m)T_m,
\quad \tau_t(T_m)=m^{it}T_m.
\]

Für \(\beta>1\) ist

\[
\omega_\beta(A)=\frac{\operatorname{Tr}(e^{-\beta H_{\rm ar}}A)}{\zeta(\beta)}
\]

ein positives normiertes invariantes Funktional. Somit ist ein Objekt aus Algebra, Adjunktion, Komposition, positivem Zustand und Dynamik explizit vorhanden. Die hier markierten Primzahlen 2 und 3 und der Parameter \(\beta\) sind gewählt; die Konstruktion ist nicht aus dem nativen W abgeleitet.

### 5.1 Der arithmetische Schatten funktioniert exakt auf Kanälen

Die Kanäle

\[
\mathcal E_m(\rho)=T_m\rho T_m^\dagger
\]

sind vollständig positiv und spurtreu. Da die globale Kokzyklusphase im Produkt mit dem Adjungierten wegfällt,

\[
\mathcal E_l\circ\mathcal E_m=\mathcal E_{lm}.
\tag{7}
\]

Auf diagonalen Zahlzuständen ist dies genau die klassische Abbildung \(n\mapsto mn\). Bei kohärenter Kontrolle der beiden Implementierungswege bleibt dagegen das relative Minus sichtbar: Für \(w_0=T_2T_3|1\rangle\), \(w_1=T_3T_2|1\rangle=-w_0\) gilt

\[
P_+=\tfrac14\|w_0+w_1\|^2=0,\qquad
P_-=\tfrac14\|w_0-w_1\|^2=1.
\]

Damit ist ein wesentlicher Gedanke des Texts konkret bewiesen: **Phasentreue Implementierungen können einen gewöhnlichen kommutativen Multiplikationsschatten besitzen.** Die kohärent kontrollierte Implementierung enthält mehr Information als ihr isoliert betrachteter Kanal.

Die Projektion darf allerdings nicht als komplex-linearer Algebra-Homomorphismus missverstanden werden. Ein solcher Homomorphismus mit \(T_2\mapsto S_2\), \(T_3\mapsto S_3\) und \(S_2S_3=S_3S_2=S_6\ne0\) würde aus der Antikommutation \(S_6=-S_6\) ableiten. Der genaue Typ der Auslesung ist also ein Teil des mathematischen Vertrags.

### 5.2 Warum die Phase die Nullstellen nicht bestimmt

Die Zustandssumme ist unabhängig von c:

\[
\operatorname{Tr}e^{-\beta H_{\rm ar}}
=\sum_{n\ge1}n^{-\beta}=\zeta(\beta),\qquad\beta>1.
\]

Man kann c durch den trivialen Kokzyklus ersetzen: Die Interferenz ändert sich, das Hamiltonspektrum und die Zustandssumme bleiben genau gleich. Deshalb identifiziert die gezeigte Wegphase weder den fehlenden Weil-Term noch einen Nullstellenoperator.

Ein C*-dynamisches System mit Zeta-Zustandssumme wurde bereits von Bost und Connes konstruiert. Die bloße Existenz eines Tupels aus Algebra, Zustand und Dynamik ist deshalb keine neue RH-Schließung. Die zusätzliche Aufgabe ist eine **native gemeinsame Herkunft und exakte arithmetische Spuridentität**. [Bost–Connes, Publikation und Abstract auf der Autorenseite](https://alainconnes.org/publications/).

### 5.3 Multiplikationsschritte sind noch keine primitiven periodischen Bahnen

Ein gerichteter Weg mit Multiplikatoren \(m_j>1\) sendet n auf \(n\prod_jm_j>n\). Er kann nicht zum Ausgang zurückkehren. Der strikt wachsende Wert \(\log n\) beweist diese Aussage unmittelbar. Die \(T_p\) sind daher in dieser Konstruktion keine geschlossenen periodischen Bahnen.

Durch Adjungierte können Vergleichsschleifen entstehen. Diese muss man mit ihrer Länge, ihrem Gewicht und ihrer Spurwirkung neu definieren. Auch der aus \(\tau_t(T_p)=e^{it\log p}T_p\) abgelesene Schwingungstakt ist \(2\pi/\log p\), während in der Primzahlseite der expliziten Formel die Größen \(r\log p\) als Bahnlängen auftreten. Beide Rollen sind verträglich mit einer Fourierdualität, aber nicht schon dieselbe abgeleitete Dynamik.

## 6. RH: der tatsächlich erforderliche gemeinsame Satz

Im eingefügten Text steckt eine wichtige sprachliche Verkürzung: Ein selbstadjungierter Operator mit den **Imaginärteilen** aller Zeta-Nullstellen als Eigenwerten würde für sich allein RH nicht beweisen. Imaginärteile sind immer reell, auch bei Nullstellen abseits der kritischen Geraden.

Benötigt wird die vollständige Zuordnung

\[
\rho=\tfrac12+i\lambda,
\]

für **alle** nichttrivialen Nullstellen mit ihren Multiplizitäten, ohne die Realteilbedingung bereits in die Konstruktion hineinzustecken.

### 6.1 Ein exakt formuliertes hinreichendes Beweisziel

Setze

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Xi(z)=\xi(\tfrac12+iz).
\]

Wenn man aus der Quelle einen strikt positiven selbstadjungierten Operator A mit kompakter Inverser, \(A^{-2}\) von Spurklasse und der ganzen Funktionsidentität

\[
\boxed{\frac{\Xi(z)}{\Xi(0)}=\det(I-z^2A^{-2})\quad\text{für alle }z\in\mathbb C}
\tag{8}
\]

konstruierte, wäre RH bewiesen. Denn der Fredholm-Determinant auf der rechten Seite verschwindet genau bei den reellen Werten \(z=\pm\lambda_j(A)\), mit den richtigen Multiplizitäten. Über die linke Seite wären sämtliche nichttrivialen Zeta-Nullstellen erfasst.

**(8) ist hier nicht bewiesen.** Es ist ein scharfes Ziel für die vorgeschlagene gemeinsame Quelle. A nach bereits angenommenen reellen Nullstellenhöhen zu definieren wäre zirkulär. Insbesondere ist \(H_{\rm ar}=\log n\) nicht der in (8) benötigte Operator.

Eine alternative Route ist die norm- und phasentreue positive Darstellung der vollständigen signierten Weil-Form auf dem erforderlichen Testraum. Positivität eines beliebigen Zustandsfunktionals reicht nicht. Connes–Consani–Marcolli formulieren RH als Positivität der entsprechenden Spurpaarung; die Arbeit von Connes–Consani zur archimedischen Stelle kontrolliert einen präzisen Teil dieses Programms. Diese Arbeiten liefern Anschlüsse, keinen aus unseren lokalen Daten folgenden Gesamtbeweis. [Spurpaarung](https://arxiv.org/abs/math/0703392), [archimedische Weil-Positivität](https://arxiv.org/abs/2006.13771).

### 6.2 Ein kleines Gegenmodell zur falschen Abkürzung

Schon der positive selbstadjungierte Hamiltonoperator \(H=\operatorname{diag}(0,1,1)\) hat Zustandssumme

\[
Z(s)=1+2e^{-s}.
\]

Ihre Nullstellen liegen bei \(s=\log2+(2k+1)i\pi\), nicht auf einer durch Selbstadjungiertheit erzwungenen Geraden \(\operatorname{Re}s=1/2\). Reelle **Energien** sind nicht dasselbe wie reelle **Nullstellen einer transformierten Funktion**.

Die RH wird auch in der aktuell eingesehenen offiziellen Übersicht weiterhin als ungelöst geführt. Das ersetzt kein Argument über die vorliegenden Unterlagen, bestätigt aber die Grenze des Literaturstands. [Clay Mathematics Institute](https://www.claymath.org/problem/unsolved/).

## 7. Konkrete positive Fortsetzung der nativen Antwort

Die vollständige Selbstenergie \(\Sigma_2\) wurde in dieser Untersuchung nicht berechnet. Es lässt sich aber eine erlaubte Näherung mit genauer Fehlergrenze aus den frisch reproduzierten Resultaten gewinnen.

### Satz 4 — Kontrollierte lokale Ein-Pol-Darstellung

Für die diagonale retardierte Antwort schreibe

\[
G(z)=\frac{Z}{z+\epsilon}+R(z),
\qquad Z=Z_{\rm low},\quad\epsilon=\epsilon_{\rm low}.
\]

Das verbleibende positive Spektralmaß hat Masse \(1-Z<0.119923719311\). Seine Entnahmelinien liegen bei Frequenzen kleiner als \(-0.379636\Delta\), seine Additionslinien oberhalb \(0.329636\Delta\).

Der Abstand dieser restlichen Spektralmenge vom niedrigen Pol \(-\epsilon\) ist daher strikt größer als

\[
\delta=\min\left(0.379636-\frac{2403745}{61508688},\;0.329636+0.007737\right)\Delta
=0.337373\Delta.
\]

Für \(|z+\epsilon|\le r<\delta\) ist R holomorph und

\[
\boxed{|R(z)|<\frac{1-Z_{\min}}{\delta-r}.}
\tag{9}
\]

**Beweis.** Jeder Nenner \(z-x\) im restlichen Spektralintegral hat Betrag mindestens \(\delta-r\). Integration dieser Abschätzung gegen das positive Maß liefert (9). Der positive Abstand gibt lokale holomorphe Fortsetzung. ∎

Insbesondere folgt für \(r=0.1\Delta\)

\[
\boxed{|R(z)|<0.505213/\Delta.}
\]

Für \(0<|z+\epsilon|\le0.1\Delta\) ist damit der Fehler relativ zum zurückbehaltenen Polterm kleiner als

\[
\frac{|R(z)|}{|Z/(z+\epsilon)|}
<\frac{0.505213\cdot0.1}{0.880076280689}<0.0575.
\]

Das sind höchstens 5,75 Prozent **relativ zum Polterm** im angegebenen komplexen Frequenzfenster, nicht eine globale relative Fehlerschranke bezogen auf G. Z und \(\epsilon\) sind dabei die tatsächlichen, weiterhin nur eingeschlossenen Polparameter. Das Einsetzen ihrer Intervallmitten braucht eine zusätzliche Fehlerrechnung, gerade nahe am Pol.

Dies erlaubt ein kontrolliertes lokales effektives Bild. Es behauptet weder \(R=0\) noch \(\Sigma_2=0\), keine exakt zweilinige Antwort und keine räumliche Quasiteilchentheorie.

## 8. Faktorisierung: welche Auslesung tatsächlich fehlt

Die Basisidentität

\[
|n\rangle\longleftrightarrow|\nu_2(n),\nu_3(n),\nu_5(n),\ldots\rangle
\]

ist mathematisch richtig. Bei einem bekannten Primkandidaten p lässt sich \(\nu_p(n)\) durch wiederholte Division effizient bestimmen. Das schwierige Stück ist die vollständige Liste unbekannter Primfaktoren und eine zugängliche Messung dieser Liste.

Ein präziser Ressourcenvertrag wäre:

1. Eingabe: gewöhnliche Binärdarstellung von n, Länge \(L=\lceil\log_2(n+1)\rceil\).
2. Präparation und sämtliche Kontrollen: Aufwand polynomial in L.
3. Ausgabe: eine endliche Liste \((p_j,\nu_j)\), einschließlich der Primlabels, mit kontrollierter Fehlerwahrscheinlichkeit.
4. Präzision, Messwiederholungen, Hilfsregister und eventuelle Erfolgspostselektion werden mitgezählt.

Existiert ein solcher Konverter zur auslesbaren Primbelegung, existiert unmittelbar ein Faktorisierungsalgorithmus mit demselben Aufwand. Umgekehrt kann ein effizientes Faktorisierungsverfahren die klassische Liste herstellen und in ein Register schreiben. Die schlichte Benennung eines „Primbelegungs-Observablen“ verlagert diese Aufgabe deshalb, ohne sie zu lösen. Für eine kohärente Konversion beliebiger Überlagerungen wäre zusätzlich ein reversibler, fehlerkontrollierter Vertrag nötig; die klassische Ausgabeäquivalenz allein behauptet diesen nicht.

Für das allgemeine Quantenrechenmodell ist effiziente Faktorisierung bereits durch Shors Algorithmus bekannt. Die neue Aufgabe wäre eine native Realisierung der benötigten Operationen und Ressourcen in diesem Universalraum. Ein RH-Beweis ist dafür nicht Voraussetzung. [Shor, Primärarbeit](https://arxiv.org/abs/quant-ph/9508027).

## 9. Zeit, Dimension und Gravitation: was das gemeinsame Objekt zusätzlich leisten müsste

### 9.1 Zeit aus einem Zustand

Die Idee einer vom Zustand mitbestimmten Zeit besitzt einen konkreten Anschluss in der modularen Dynamik. Für eine treue Gibbsdichte \(\rho_\beta\propto e^{-\beta H}\) gilt auf der entsprechenden Algebra

\[
\sigma_t(A)=\rho_\beta^{it}A\rho_\beta^{-it}=e^{-it\beta H}Ae^{it\beta H}.
\]

Das zeigt eine genaue Beziehung zwischen Zustand und Dynamik. Es leitet weder die gewählte Dichte noch die physische Zeiteinheit ab. Die Thermal-Time-Hypothese untersucht diese Idee ausdrücklich. [Connes–Rovelli](https://arxiv.org/abs/gr-qc/9406019).

Der reine Grundzustand auf \(B(\mathcal H)\) ist nicht treu. Schon \(\operatorname{diag}(0,1,2)\) und \(\operatorname{diag}(0,3,7)\) besitzen denselben eindeutigen Grundzustand, aber verschiedene Anregungszeiten. Die Kenntnis von \(\Omega\) allein wählt H nicht aus. Auf einer anders gewählten lokalen Algebra können die modularen Voraussetzungen anders sein; auch diese Algebra muss identifiziert werden.

### 9.2 Raum und gemeinsamer Lichtkegel

Ein positives Funktional liefert über die GNS-Konstruktion eine Hilbertraumdarstellung. Es liefert dadurch noch keine ausgezeichneten räumlichen Teilalgebren, keine örtliche Reichweite und keine wachsende Familie mit Dimension drei.

Die kontrollierte Weyl-Walk-Klassifikation behandelt vorausgesetzte Gitterdimensionen 1, 2 und 3 und liefert im dreidimensionalen Fall die Weyl-Walks. Sie wählt nicht allein aus zwei inneren Komponenten die physische Dimension drei aus. [D’Ariano–Erba–Perinotti](https://arxiv.org/html/1708.00826v2).

Das bereits in den Quellen enthaltene Gegenmodell

\[
D(k)=\operatorname{diag}(v_1k\cdot\sigma,v_2k\cdot\sigma)
\]

ist ein gemeinsamer hermitescher Operator und hat bei \(v_1\ne v_2\) zwei verschiedene Kegel. Ein gemeinsamer Takt genügt nicht. Erforderlich wäre eine hergeleitete Relation oder Symmetrie, die die Hauptsymbole sämtlicher relevanter Sektoren passend gleichsetzt.

### 9.3 Gravitation

Eine von Belegung abhängige effektive Nachbarschaft kann im Modell eine Geometrie verändern. Für Gravitation müsste man darüber hinaus im selben Grenzwert einen dynamischen masselosen Spin-2-Anteil mit zwei physikalischen Helizitäten, positivem physikalischem Zustandsraum und universeller Kopplung nachweisen. Keine dieser zusätzlichen Aussagen folgt aus dem lokalen Entnahmepol oder der phasentreuen Multiplikation. Hier wurde kein solcher Sektor konstruiert.

## 10. Welches gemeinsame Konstrukt nach diesen Beweisen übrig bleibt

Ein einzelnes endliches Bankmodell reicht für die vorgeschlagene direkte Vereinigung nicht. Ein weiterzuverfolgender Kandidat müsste mindestens eine **unbegrenzt erweiterbare Familie kompatibler Operationsalgebren** besitzen:

\[
\mathcal A_1\hookrightarrow\mathcal A_2\hookrightarrow\cdots,
\qquad\mathcal A=\overline{\bigcup_L\mathcal A_L},
\]

mit kompatiblen positiven Zuständen, einer wohldefinierten Dynamik und tatsächlich identifizierten Instrumenten. Dies ist eine notwendige Richtung für das Entgehen der endlichen Zählschranke, keine bereits aus TFPT ausgewählte Konstruktion.

Die nächsten konkreten Beweise lauten:

| Verbindung | Präziser nächster Nachweis |
|---|---|
| Compiler → lokale Bank | Zulässige Fockoperationen, ihr Adjungiertes und Ladungsvertrag; H und Anfangszustand aus derselben Quelle |
| Bank → Nachbarbank | Ein tatsächliches Quellenwort mit nichtverschwindendem Ein-Loch-Transfer und passenden lokalen Paritäten; erhaltene innere Interferenz |
| Lokale Familie → Geometrie | Operational bestimmte Teile und wachsende Familie; reproduzierbare Ausbreitung, stabile Dimensionsdiagnose und gemeinsames Hauptsymbol |
| Primitive Wörter → Arithmetik | Aus der Quelle bestimmte Multiplikationssemigruppe samt voller Primfamilie; Wahl des Generators begründen und Satz 1 berücksichtigen |
| Arithmetik → RH | Ganze Determinantenidentität (8) oder vollständige signierte Weil-Positivität, mit allen Rand-, Normierungs- und Grenztermen |
| Arithmetik → effiziente Auslesung | Binäre Eingabe bis vollständige Faktor-Ausgabe mit Gesamtaufwand polynomial in der Eingabelänge |
| Geometrie → Gravitation | Derselbe dynamische Spin-2-Sektor und universelle Kopplung |

Ein Tensorprodukt aus einer Bank, einem fertigen Bost–Connes-System und einem fertigen Raumzeitmodell wäre mathematisch möglich. Es würde ihre gemeinsame Herkunft nicht beweisen. Gefordert sind die gemeinsamen Relationen und die kontrollierten Antworten auf Eingriffe zwischen den Bereichen.

## 11. Gesamturteil

Der Text enthält eine tragfähige **Architekturhypothese**: Operationen, ihre Zusammensetzung und kohärente Auslesung können eine gemeinsame Sprache für mehrere Bereiche liefern. Der arithmetische Phasen-/Ausleseteil lässt sich darin exakt bauen, und die native lokale Antwort ist inzwischen wesentlich besser abgesichert.

Die stärkere Aussage, diese Bereiche seien bereits dieselbe bewiesene Struktur oder würden mit einem schon vorhandenen Satz gemeinsam fallen, ist nicht gerechtfertigt. Die erste direkte Generatoridentifikation scheitert sogar an Satz 1. Der Ortsanschluss scheitert unter dem bisherigen lokal geraden Operationsvertrag an Satz 2. Die RH-Brücke benötigt die vollständige Identität (8); sie wird durch einen positiven Zustand oder eine Wegphase nicht ersetzt.

**Der konkrete Ertrag dieser Untersuchung ist daher:** bestätigte lokale Beweise, eine zusätzliche quantitative Antwortschranke, eine präzise konstruktive arithmetische Projektion und ein ausgeschriebener Ausschluss einer zentralen Abkürzung. Die vollständige Lösung bleibt offen. Für den nächsten nativen Fortschritt ist ein aus der tatsächlichen Quelle bestimmter Austauschprozess zwischen zwei operational definierten Teilen das engste entscheidende Ziel.

## Anhang: Dateien und Reproduzierbarkeit

- `input_manifest.json`: Hashes sämtlicher zwölf benannter Eingaben; ergänzend Hash des eingefügten Texts.
- `work/verify_unification.py`, `work/replay_new_proofs.py`: eigene zusätzliche symbolische/endliche Prüfungen.
- `work/new_proofs_normal.json`, `work/new_proofs_optimized.json`, `work/new_proofs_replay.json`: Ergebnisse der eigenen Prüfungen.
- Extrahierter v1.6.4-Arbeitsordner: originale Prüfer sowie frische Ausgaben und Manifeste.
- `verification_summary.json`: kompakte maschinenlesbare Zusammenfassung mit Vergleich der fachlichen Berichte gegen das Originalarchiv.

Die eigenen Prüfungen lassen sich aus dem entpackten Paket mit `python3 work/replay_new_proofs.py` wiederholen; erforderlich sind NumPy und SymPy. Die ursprünglichen vollständigen Replay-Skripte verwenden zusätzlich die in ihren Manifesten genannten lokalen Originalpfade, SciPy und für die Normenumeration Apple clang/libdispatch. Das Paket bezeichnet diese Abhängigkeit ausdrücklich und behauptet keine portable Vollinstallation sämtlicher Originalquellen.

Die analytischen Beweise sind nicht in Lean oder einem anderen Beweisassistenten formalisiert. Eine unabhängige fachliche Begutachtung ist hier nicht erfolgt. Keines der T1–T8-Tore wird als vollständig geschlossen markiert.
