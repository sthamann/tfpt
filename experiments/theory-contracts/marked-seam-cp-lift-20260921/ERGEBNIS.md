# TFPT: ein konkreter Anschluss des Nahttransfers an die markierte Operatoralgebra

21. September 2026 · `UR.SOURCE.MARKED_CP_LIFT.01` · **PARTIAL**

## Was diese Fortsetzung entscheidet

Die vorherige Rechnung konnte die geladenen Korrelatoren der vorhandenen QWZ-Realisierung auswerten, aber diese Realisierung nicht aus P1/P2 auswählen. Hier wird deshalb ein Schritt früher angesetzt: am ursprünglichen Drei-Zustands-Transfer und den bereits vorhandenen markierten Compileroperatoren. Es wird kein zusätzliches Gitter Gamma, Vaux, Oszillator, RR-Hamiltonoperator oder passendes Energiespektrum eingesetzt.

**Ein endlicher positiver Operatoranschluss ist konstruiert. Die vollständige Herkunft der geladenen lokalen Feldtheorie ist damit nicht hergeleitet.** Die Konstruktion zeigt exakt, was eine besonders einfache Erweiterung leistet und wo sie als physische Feldzeit scheitert.

Die erste zusätzliche Annahme steht vor der Rechnung: Der primitive Schritt soll ein unitaler, vollständig positiver, spurtreuer Operatorprozess auf der vorhandenen Algebra M4(C) sein, kovariant unter den Pauli-Konjugationen und der bezeichneten q*-markierten S5-Wirkung. Die beiden nichttrivialen Nahtfaktoren werden dabei den beiden markierten Operatorsektoren zugeordnet. Diese gemeinsame physische Wirkung ist aus P1/P2 noch nicht bewiesen. Die S5-Kovarianz darf insbesondere nicht stillschweigend als physische Symmetrie der gesamten späteren 3+2-Schnittstelle oder der unmarkierten Cliffordgruppe ausgegeben werden.

Erfolgskriterium war ein exakter positiver Anschluss an die **vollständige ursprüngliche Matrix**, anschließend Prüfung von Zustand, Produkten und Zeit. Abbruchkriterium für die Identifikation als geladene Feldzeit war das Scheitern der Produkt- oder Ladungsverträglichkeit. Dieses Kriterium greift; die Konstruktion wird nicht durch zusätzliche Felder oder eine neue Zeit repariert.

## 1. Die ursprünglichen Daten

Der Originaltransfer in v221 besitzt eine in v814 bereits exakt angegebene positive sechste Wurzel:

\[
B=\frac1{18}\begin{pmatrix}13&1&4\\1&13&4\\4&4&10\end{pmatrix},
\qquad T=B^6.
\]

Seine festgelegten Eigenrichtungen sind (1,1,1), (1,−1,0), (1,1,−2), mit Einzelschrittfaktoren 1, 2/3, 1/3. Das ist der ursprüngliche 3×3-Transfer, nicht nur eine neue Matrix mit denselben Eigenwerten. Seine physische Bedeutung als sechs identische Quantenoperationen wird dadurch noch nicht bewiesen.

Die unabhängig vorhandene markierte Clifford-Wortalgebra zerfällt als Operatorraum in die Ränge

\[
M_4(\mathbb C)=\mathcal V_0\oplus\mathcal V_5\oplus\mathcal V_{10}.
\]

Die fünf q*=0-Wörter außerhalb der Identität sind Hermitesche, paarweise antikommutierende Einheiten g_j. Die zehn übrigen Wörter bilden den q*=1-Orbit. Alle Matrizen und Markierungen werden aus dem gepinnten ursprünglichen Compiler übernommen; ein beliebiges neues Pauli-Koordinatensystem wird nicht als Ursprung ausgegeben.

Unter der angegebenen Kovarianz muss der Prozess die Form

\[
\Phi_{a,b}=\Pi_0+a\Pi_5+b\Pi_{10}
\]

haben. Die Notation Pi bezeichnet Projektoren im 16-dimensionalen **Operatorraum**, keine Raumzeitdimensionen oder Teilchensorten. Pauli-Konjugationen erzwingen die Diagonalform durch ihre verschiedenen Vorzeichencharaktere; die markierte S5-Wirkung macht die Koeffizienten innerhalb jedes Orbits gleich.

## 2. Vollständige Positivität entscheidet die Zuordnung

Die normalisierten Choi-Eigenwerte sind im vorhandenen Zweiraten-Theorem bereits bekannt:

\[
p_0=\frac{1+5a+10b}{16},\qquad
p_5=\frac{1-3a+2b}{16},\qquad
p_{10}=\frac{1+a-2b}{16},
\]

mit Vielfachheiten 1,5,10. Sie sind zugleich die Gewichte der einzelnen Pauli-Konjugationen. Vollständige Positivität bedeutet, dass alle drei nichtnegativ sind.

Die beiden positiven Einzelschrittzuordnungen ergeben:

| Faktor auf V5 | Faktor auf V10 | Gewichte p0, p5, p10 | Ergebnis |
|---:|---:|---|---|
| 2/3 | 1/3 | 23/48, −1/48, 1/16 | Nicht vollständig positiv |
| 1/3 | 2/3 | 7/12, 1/12, 0 | Vollständig positiv |

Damit ist innerhalb der bezeichneten Klasse der positive Einzelschritt eindeutig:

\[
\boxed{\Phi(X)=\frac7{12}X+\frac1{12}\sum_{j=1}^5g_jXg_j.}
\]

Die Gewichte wurden aus den festen Nahtfaktoren und dem bekannten Choi-Kriterium berechnet. Sie sind weder gemessene physische Ereigniswahrscheinlichkeiten noch ein aus P1 hergeleitetes Ausführungsgesetz. Die Übernahme der Einzelschrittfaktoren auf diesen Operatorraum bleibt die ausdrücklich genannte gemeinsame Identifikationsannahme.

Der Schritt ist positiv, unital und spurtreu, und

\[
\Phi^6=\Pi_0+\frac1{729}\Pi_5+\frac{64}{729}\Pi_{10}.
\]

Nur die sechsten Potenzen vorzugeben würde die Zuordnung **nicht** auswählen: Beide vertauschten Makrozuordnungen sind vollständig positiv. Die zusätzliche Prüfung des positiven Einzelschritts ist daher wesentlich. Negative sechste Wurzeln und nicht orbit-skalare Erweiterungen gehören nicht zur angegebenen Klasse.

## 3. Anschluss an die ursprüngliche Matrix, einschließlich ihrer Eigenrichtungen

Die Originalmarkierungen A_BIT und FSIG liegen im festen Compilerzweiraum. Ihre quadratischen Typen sind 1 und 0; ihre symplektische Paarung ist 1. Mit den ursprünglichen signierten Wortmatrizen erhält man

\[
A=iP_{\mathrm{A\_BIT}},\qquad F=P_{\mathrm{FSIG}},
\]
\[
A^\dagger=A,\quad F^\dagger=F,\quad A^2=F^2=I,\quad AF=-FA,
\qquad \Phi(A)=\frac23A,\quad\Phi(F)=\frac13F.
\]

Definiere die drei positiven Messeffekte

\[
E_1=\frac13\left(I+\frac{\sqrt3}{2}A+\frac12F\right),\quad
E_2=\frac13\left(I-\frac{\sqrt3}{2}A+\frac12F\right),\quad
E_3=\frac13(I-F).
\]

Es gilt

\[
E_1+E_2+E_3=I,\qquad
\operatorname{spec}E_i=\{0,0,2/3,2/3\},
\]

und nun **eintragsweise**, nicht lediglich spektral,

\[
\boxed{\Phi(E_i)=\sum_j B_{ij}E_j,\qquad
\Phi^6(E_i)=\sum_j T_{ij}E_j.}
\]

Für die Wahrscheinlichkeiten p_i(rho)=Tr(rho E_i) liefert der zugehörige Zustandsprozess folglich p' = Bp und nach sechs Schritten p' = Tp. Induktion ergibt dieselbe Aussage für alle ganzzahligen Schrittzahlen. Diese Aussagen brauchen keine Simulation langer Folgen.

Die drei Ergebnisse sind Messlabels, keine hier hergeleiteten drei physikalischen Familien. Eine Gleichsetzung mit einer Familien- oder Raumzeitwirkung wird nicht behauptet.

## 4. Zustand und gemeinsame Gram-Antwort

Der Kanal hat nur eine feste Operatorrichtung, die Identität. Sein eindeutig stationärer Dichteoperator ist

\[
\rho_*=I_4/4,\qquad \tau(X)=\operatorname{Tr}(X)/4.
\]

Damit ist der Zustand innerhalb dieser Kanalhypothese bestimmt. Er ist kein neu hergeleitetes reines physisches Vakuum.

Setze J=11^T/3, C2=u2u2^T/2, C3=u3u3^T/6 für u2=(1,−1,0), u3=(1,1,−2). Die tatsächlich gemeinsame Gram-Matrix der Messeffekte lautet

\[
G_{ij}=\tau(E_iE_j),\qquad
G=\frac13J+\frac16(C_2+C_3).
\]

Sie hat Diagonale 2/9 und Nebendiagonale 1/18. Die diskrete Transferkorrelation ist exakt

\[
C(n)_{ij}=\tau(E_i\Phi^n(E_j)),
\]
\[
C(n)=\frac13J+\frac16\left(\frac23\right)^n C_2+
\frac16\left(\frac13\right)^n C_3.
\]

Deshalb gilt auf dem positiven Gramraum

\[
\boxed{G^{-1/2}C(n)G^{-1/2}=B^n.}
\]

Das schließt den **endlichen normierten Ausleseanschluss**. Eine allgemeine physische Mehrzeitkorrelation mit beliebigen Feldinsertionen oder ein Prozess mit beliebigen Eingriffen ist damit nicht ausgewählt. Solche Daten setzen eine gemeinsame physische Ausführung voraus.

## 5. Der entscheidende Produkttest

Die Messeffekte sind keine scharfen Ereignisprojektoren:

\[
E_i^2=\frac23E_i\ne E_i.
\]

Auch ist p_i≤2/3 für jeden Zustand; diese konkrete Auslesung realisiert nicht jede Verteilung des ursprünglichen klassischen Dreiecks als Vorbereitung. Ein positiver Ausleseanschluss ist daher keine bijektive Identifikation der klassischen Ereignisalgebra mit einem Teil der Quantenalgebra.

Die Auslesung ist nicht einmal durch die Kanalgleichung eindeutig ausgewählt. Bereits

\[
E_1(u,v)=\frac{I+uA+vF}{3},\quad
E_2(u,v)=\frac{I-uA+vF}{3},\quad
E_3(u,v)=\frac{I-2vF}{3}
\]

erfüllt dieselbe Matrixgleichung. Positivität ist genau u²+v²≤1 und |2v|≤1. Die oben verwendete Trine-Wahl u=√3/2, v=1/2 hat maximale gleiche Schärfe aller drei Effekte. Dieses Messprotokoll wurde zur expliziten Darstellung gewählt; seine physische Auswahl wird nicht als P1-Folge ausgegeben.

Aus den tatsächlichen A,F-Matrizen lässt sich zudem der algebraische CAR-Operator

\[
c=\frac{F+iA}{2},\quad c^2=0,\quad\{c,c^\dagger\}=I,
\quad N=c^\dagger c
\]

bilden. Ein lokales Materiefeld oder physische elektrische Ladung ist diese interne Matrix dadurch noch nicht. Die Kanalwirkung ergibt jedoch einen entscheidenden exakten Test:

\[
\boxed{\Phi(c)=\frac12c-\frac16c^\dagger,\qquad
\Phi(c)^2=-\frac1{12}I.}
\]
\[
\Phi(N)=\frac13N+\frac13I\ne N.
\]

Die reduzierte Operation erhält somit weder das Produkt noch die erklärte interne Zahl. Insbesondere ist sie keine Heisenberg-*Automorphie der gegebenen Feldalgebra. Eine vollständige System-Umgebungs-Entwicklung könnte die CAR auf einem größeren Raum erhalten; deren physische Herkunft, Zustand, Ladungsaustausch und gemeinsame Zeit sind gerade nicht mitgeliefert.

Die zugehörigen **formalen Spur-Transferkorrelationen** sind

\[
\tau(c^\dagger\Phi^n(c))=\frac{(1/3)^n+(2/3)^n}{4},\qquad
\tau(c\Phi^n(c))=\frac{(1/3)^n-(2/3)^n}{4}.
\]

Die zweite wird nach einem Schritt −1/12. Das dokumentiert die Mischung, nicht eine Vorhersage elektrischer Ladungsverletzung in TFPT.

**Ein anderer Fermionbasiswechsel behebt den Produktfehler nicht.** Das lässt sich für alle Operatoren dieses Kanals gleichzeitig beweisen. Schreibe U0=I, Uj=g_j und die positiven Gewichte p0=7/12, pj=1/12. Für Yj=Uj X Uj† gilt die genaue Schwarz-Defekt-Identität

\[
\Phi(X^\dagger X)-\Phi(X)^\dagger\Phi(X)
=\frac12\sum_{j,k}p_jp_k(Y_j-Y_k)^\dagger(Y_j-Y_k).
\]

Der Defekt verschwindet genau dann, wenn alle Yj gleich sind. Wegen U0=I muss X somit mit allen fünf g_j kommutieren. Der gemeinsame Kommutant der tatsächlichen Quellmatrizen ist nur C I4; das lineare Kommutantensystem hat exakt Rang 15. Der gesamte multiplikative Bereich des Kanals besteht also aus Skalaren. Keine nichttriviale *-Unteralgebra von M4(C) kann unter diesem Schritt ihre Produkte erhalten. Ebenso ist jede unter diesem Schritt erhaltene interne Ladungsmatrix skalar, da der Fixraum nur aus der Identität besteht.

Dieser Ausschluss betrifft den hier ausgewählten reduzierten Kanal. Er schließt weder eine vollständige TFPT-Dynamik noch einen physisch hergeleiteten größeren Träger aus. Er verhindert aber, denselben Anschluss lediglich durch Umbenennen interner Operatoren zur geschlossenen Feldzeit zu erklären.

## 6. Warum der Logarithmus auch hier keine physische Zeit liefert

Für eine stetige vollständig positive Halbgruppe, die auf derselben markierten Zerlegung skalar bleibt, lautet der vorhandene Ratenkegel

\[
\frac12r_5\le r_{10}\le\frac32r_5.
\]

Der ausgewählte diskrete Schritt hätte r5=log3 und r10=log(3/2), also r10/r5<1/2. Besonders direkt zeigt sich der Fehler an der positiven Quadratwurzel: Ihr zehnfacher normalisierter Choi-Eigenwert wäre

\[
\boxed{\frac{1+1/\sqrt3-2\sqrt{2/3}}{16}<0.}
\]

Eine Halbgruppe in dieser Klasse kann daher nicht schon nach einem halben Schritt positiv bleiben. Kontinuität und die Halbgruppenregel erzwingen die positiven Wurzeln ihrer reellen skalaren Eigenwerte; ein anderer Logarithmuszweig innerhalb derselben Klasse beseitigt den Fehler nicht.

Das ist kein Beweis diskreter physischer Zeit und kein Ausschluss jeder größeren oder zwischenzeitlich anders kovarianten Dynamik. Allgemein ist ein einzelner Quantenkanal von seiner Einbettbarkeit in eine stetige Quantenentwicklung zu unterscheiden; siehe [Wolf–Cirac, Dividing Quantum Channels](https://arxiv.org/abs/math-ph/0611057). Der hier verwendete höherdimensionale markierte Test wird direkt an den Quellmatrizen bewiesen; ein Ein-Qubit-Satz wird nicht übertragen.

## 7. Konsequenz für das eigentliche Ziel

Der Anschluss ist enger bestimmt als zuvor: Unter einer offen genannten gemeinsamen Kanalannahme lassen sich die markierten Operatoren, die diskreten Gewichte, der stationäre Zustand, eine echte positive Auslesung und ihre volle ganzzahlige Gram-Antwort zusammen angeben. Die drei ursprünglichen Transfermoden werden nicht nur über ihre Zahlen verglichen.

Der entscheidende nächste Schluss hält jedoch **nicht**: Dieser Ausleseprozess ist keine ladungserhaltende, produktverträgliche Zeitentwicklung der algebraischen Fermionen. Ein kanonischer Kraus- oder Stinespringbau wäre eine mathematische Realisierung, aber noch keine Herkunft dieser Realisierung aus P1/P2. Deshalb wird nach dem Produkttest keine neue Umgebung oder Feldbank ergänzt.

Die physische Auswahl des Operatorprozesses aus dem rohen Nahtkern und eine lokale geladene Erweiterung bleiben offen. Auch die Verbindung zum bezeichneten 64/60-Randkandidaten wird nicht hergestellt. Seine Energien 3,4,5 wurden in keiner Rechnung verwendet. Die vollständige TFPT-Lösung ist weiterhin nicht bewiesen.

## 8. Herkunft und Reproduktion

Vorleistungen:

- v774 und `compiler-clifford-bridge`: signierte Wörter, q*-Markierung, A_BIT/FSIG, feste und bewegte Ebene.
- `compiler-kernel-foundation-20260914/redteam/TWO_RATE_ADDENDUM.md`: Choi-Gewichte, Ratenkegel und markierte Kovarianz; diese werden nicht als neue Entdeckung gezählt.
- v221 und v814: ursprüngliches T und exakte sechste Wurzel B in der festgelegten Basis.

Hier ausgewertet wurden die spezielle CP-Zuordnung zu den Einzelschrittfaktoren, der explizite Operatoranschluss an B und T, sein gemeinsamer Gram sowie seine Produkt-/Ladungsgrenze. Ein Neuheitsanspruch außerhalb der geprüften Quellen wird nicht erhoben.

`checker.py` importiert diese Originale mit festen Prüfsummen und bewahrt die acht ursprünglichen Quellenpins der Clifford-Brücke. Normaler und optimierter Lauf liefern identische Zertifikate. Vier gezielte falsche Schlussfolgerungen werden vom Checker verworfen: vertauschte Einzelschrittzuordnung sei CP; stetige markierte Interpolation sei CP; die Messeffekte seien Projektoren; die Zahl werde erhalten. Die allgemeinen diskreten Aussagen folgen aus den bewiesenen Matrixidentitäten, nicht aus Stichproben großer Schrittzahlen.

Keine Änderung an Papers oder Statusledger, keine empirische Evidenz, keine Promotion eines T1–T8-Gates.
