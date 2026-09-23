# Zwei native Zellsterne: die ursprüngliche Kante liefert Transfer und Paarerzeugung

14. September 2026. Explizite Projektion der **nackten** vierfarbigen
Vier-Site-Sternzelle und eines physikalischen Zwischenzell-P+-Terms.
Keine Ersetzung durch C16 oder durch eine frei erfundene Kettenzelle.

## Ergebnis

**Die einzelne ursprüngliche Blatt-Blatt-Bindung liefert für die ersten
Zellanregungen den festen Transfer J/9, nicht frei J/2.** Von den 30
ersten Anregungen sind für diese Bindung 15 hell und 15 dunkel. Eine
Zentrum-Zentrum-Bindung hat in diesem ersten Band gar keinen Transfer.

Gleichzeitig erzeugt die Blatt-Blatt-Bindung aus dem Produktvakuum
Anregungspaare mit Norm J√15/9. Es gibt ferner Farbwechselwirkungen und
Übergänge zwischen Ein- und Zweianregungssektor. **Der aus der Quelle
projizierte Operator ist deshalb nicht der zahlenerhaltende selektive
Transferoperator aus v1.5.** Diese neue Rechnung bestimmt die bisher
fehlenden Koeffizienten an einer echten Quellenbindung und zeigt genau,
welcher zusätzliche Teil der Referenzfamilie nicht einfach übernommen
werden darf.

## Verwendeter Quellenoperator und Umfang

Die lokale nackte Zelle hat 4⁴=256 Zustände und den tatsächlichen
Drei-Kanten-Stern

\[
H_\star=J\sum_{j=1}^3P^+_{0j}
=\frac J2(3I+X),\qquad X=S_{01}+S_{02}+S_{03}.
\]

Der eindeutige Grundzustand Ω ist das vollständig antisymmetrische
Vierfarbensingulett. Die erste Energie ist g=J/2 mit Multiplizität 30.
Pro Zelle werden Ω und dieses ganze erste Band behalten: 31 Zustände,
somit **961 Zustände für zwei Zellen**. Die Zusatzbindung ist exakt der
physikalische führende Superaustausch λP+ij zwischen einem Site beider
Zellen, bei der Default-Auswertung λ=J=2t²/Δ. λ wird nicht an ein
gewünschtes kritisches Verhalten angepasst.

Dies ist die vom Auftrag zugelassene nackte Projektion. Die 544D-
Vermittlerdressingstruktur und neue Zwischenzellvermittler werden hier
nicht vollständig auf 544² und zusätzliche Zwischenzustände erweitert.
Insbesondere liegt für λ=J keine bewiesene kleine Fehlergrenze der
Zellbandprojektion vor. Die vollständige 961D-Matrix ist ein exakt
definierter komprimierter Operator; ihre Eigenwerte sind noch keine
zertifizierten Eigenwerte des unkomprimierten mikroskopischen Modells.

## Exakte Projektoren und Kopplungsvektoren

Der erste Bandprojektor wird als ganzzahliges Polynom in X aufgebaut:

\[
P_1=-\frac1{120}\prod_{c\in\{-3,-1,0,1,2,3\}}(X-cI).
\]

Der Prüfer kontrolliert P1²=P1, Rang 30 und XP1=−2P1 exakt mit ganzen
Zahlen. Der Grundvektor enthält die 24 vorzeichenbehafteten Permutationen
von (0,1,2,3), normiert durch √24.

Normiere die fünfzehn SU(4)-Generatoren durch tr(TATB)=δAB/2 und schreibe
ψiA=TiAΩ. Wegen der Singulettbedingung ist ΣiψiA=0. Der Zentralvektor
ψ0A besitzt Sternenergie 2J und hat daher keine Komponente im ersten
Band. Für ein Blatt i=1,2,3 ist der erste Bandanteil exakt

\[
\chi_i^A=P_1T_i^A\Omega=\psi_i^A+\tfrac13\psi_0^A.
\]

Das Skript kontrolliert diese Vektoridentität rational für einen normierten
Generator. Die SU(4)-Invarianz des Sterns und die eindeutige invariante
Form übertragen sie auf alle A. Die zugehörige exakte Grammatrix ist

\[
\langle\chi_i^A,\chi_j^B\rangle
=\delta^{AB}
\begin{cases}
0,&i=0\ \text{oder}\ j=0,\\
1/9,&i=j\ne0,\\
-1/18,&i\ne j,\ i,j\ne0.
\end{cases}
\]

Die drei Blattvektoren liegen damit in einem zweidimensionalen
Multiplizitätsraum mit Winkelskalarprodukt −1/2 zwischen den normierten
Richtungen. Die ersten 30 Zustände tragen 15 Farbrichtungen mal zwei
solche Blattkombinationen.

## Der vollständige feste Zweizellenoperator

Aus der exakten Identität

\[
P^+_{ij}=\frac58I+\sum_{A=1}^{15}T_i^A\otimes T_j^A
\]

folgt für P=|Ω⟩⟨Ω|+P1 und LiA=PTiAP unmittelbar

\[
V_{ij}=\frac58I_{961}+\sum_A L_i^A\otimes L_j^A.
\]

Jedes Li zerfällt in eine Ω↔χ-Komponente und den festen
Farboperator DiA=P1TiAP1 innerhalb der Anregungen. Diese Formel und die
ausgegebenen vollständigen Matrizen bestimmen **alle** Transfer-,
Paar-, Dichte- und Farbmatrixelemente gemeinsam; kein Koeffizient wird
einzeln frei gewählt.

Für ein Blatt und die normierten hellen Zustände |eA⟩=3χiA gilt

\[
\langle\Omega,e_B|\lambda V|e_A,\Omega\rangle
=\frac\lambda9\delta_{AB},\qquad
\langle e_A,e_B|\lambda V|\Omega,\Omega\rangle
=\frac\lambda9\delta_{AB}.
\]

Die zweite Identität ist die Paarerzeugung. Ihre Norm ist λ√15/9,
bei λ=J also ungefähr 0.43033J. Sie lässt sich nicht mit der Behauptung
eines starren Produktvakuums vereinbaren. Die übrigen 15 ersten
Anregungskombinationen sind nur bezüglich **dieser einen Bindung** dunkel.
Andere Blattanschlüsse können sie erreichen.

Weitere vollständig überprüfte Koeffizienten:

| Anteil der Blatt-Blatt-Bindung | Wert |
|---|---:|
| Grund-Grund-Diagonale | 5λ/8 |
| Gesamte Einanregungsdiagonale | (5λ/8) I30 |
| Einanregungsdiagonale relativ zum Produktvakuum | 0 |
| Transferblock | Rang 15, Singulärwerte λ/9 |
| Grund→Einanregung | 0 |
| Grund→Zweianregung | Norm λ√15/9 |
| Skalares Dichtezentrum von ΣADiA⊗DjA | 0 |

Das verschwindende skalare Dichtezentrum bedeutet nur, dass die Spur des
zusätzlichen Farboperators auf dem gesamten 30×30-Anregungsraum null ist.
Der Operator selbst verschwindet nicht. Die vollständigen Farbmatrizen
liegen in `projected_pair.npz`; beispielsweise beträgt die numerische
Frobeniusnorm dieses Farbanteils 6.23980650. Auch der
Ein→Zweianregungsblock ist nicht null (Frobeniusnorm 1.63865347).

## Was die feste Kopplung mit dem v1.5-Kritikalitätskriterium macht

Betrachtet man **diagnostisch nur den zahlenerhaltenden Einanregungsteil**
einer Kette mit demselben Blattanschluss links und rechts, erhält man

\[
\kappa=J/9,\qquad g=J/2,\qquad
\kappa/g=2/9<1/2.
\]

Dieser Anteil erreicht die freie Ketten-Schwelle κ=g/2 daher nicht.
Sein niedrigster Bandwert ist g−2κ=5J/18. Bei zwei verschiedenen
Blattanschlüssen pro Zelle beträgt das Skalarprodukt der hellen Richtungen
−1/2; die maximale Absenkung ist dann 3κ/2, der niedrigste Bandwert J/3.
Bei zentralen Anschlüssen ist der erste Transfer null.

Diese Werte sind **kein positiver Gapbeweis für die ganze Quelle**: Die
tatsächliche Quellenbindung enthält gleichzeitig Paarerzeugung und
Farbwechselwirkungen. Genau deshalb darf weder die freie Kettendispersion
noch ihr Kritikalitätskriterium ohne weitere Reduktion als vollständiges
Ergebnis übernommen werden. Die Projektion liefert nun die konkreten
Koeffizienten für diese nächste wechselwirkende Rechnung.

## Vollständige 961D-Zweizellendiagnose

Für λ=J wurde die gesamte projizierte Matrix einschließlich aller
Anregungszahländerungen diagonalisiert. Numerisch:

- Produktvakuum-Erwartungswert: 0.625J;
- Grundenergie: 0.41666666666666646J;
- nächste Energie: 0.75207294645443J;
- projizierte Zweizellenlücke: 0.33540627978776355J.

Die Grundenergie liegt deutlich unter dem Produktvakuumerwartungswert;
das Vakuum wird also tatsächlich durch die Quellenbindung verändert.
Die Nähe zur rationalen Zahl 5/12 wird nicht als bereits bewiesene
algebraische Eigenwertidentität ausgegeben. Die endliche positive Lücke
entscheidet keine thermodynamische Kritikalität.

## Verifikation und Artefakte

`checker.py` enthält 23 explizite Bedingungen mit ganzzahligen
Projektor-/Vektorgleichungen und getrennten numerischen Restprüfungen.
Die vollständige physikalische P+-Kompression ist hermitesch und besitzt
Spektrum in [0,1]. Das Weglassen der Paarterme würde die geprüfte
Nichtkommutation mit der Zellanregungszahl verlieren.

`verification.json` enthält die Zahlen und Annahmen.
`projected_pair.npz` enthält die 256×31-Basis, V, den ganzen
Zweizellen-Hamiltonoperator, Transferblock und Paarerzeugungsvektor.
Reproduktion: `/opt/homebrew/bin/python3 -B checker.py`.

Die ergänzende Prüfung der neuesten Wurzelraum-, Hard-Core- und
Halbladungsbehauptungen steht unabhängig in `SOURCE_CLAIMS.md`,
`source_claims.py` und `source_claims.json` (32 exakte Bedingungen).
