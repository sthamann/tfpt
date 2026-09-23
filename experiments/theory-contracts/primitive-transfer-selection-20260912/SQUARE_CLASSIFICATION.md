# Vier markierte Punkte: vollständige Klassifikation einer begrenzten Transferfamilie

12. September 2026. Quelle: `origin_theory.tex` 87–104 und
`verification/v69_d4_q_geometry.py` (eingesehene Viererzyklusmatrix).
Die folgenden Zusatzannahmen sind ausdrücklich NICHT alle TFPT-Postulate:
reelle symmetrische Generatoren auf den vier Punktamplituden, D4-Kovarianz
und Erhaltung des konstanten Vektors.

Seien R der dokumentierte Viererzyklus und S:j->-j die Quadratspiegelung.
Jede reelle symmetrische Matrix, die mit R,S kommutiert und konstante
Vektoren annihiliert, hat exakt die Form

    L(a,b)=a(2I-R-R*)+b(I-R^2).

Das folgt entweder durch Umlauf-/Spiegelgleichheit der Matrixelemente
oder aus dem exakt geprüften zweidimensionalen Lösungsraum der linearen
Gleichungen. Ihre Eigenwerte sind

    0, 4a, 2(a+b), 2(a+b).

Positivität bedeutet a>=0 und a+b>=0. Soll -L zusätzlich ein klassischer
Markovgenerator sein, sind die stärkeren Bedingungen a,b>=0 notwendig
und hinreichend, da alle Übergangsraten dann nichtnegativ sind. Bei a>0
ist das Netzwerk verbunden und der konstante Zustand eindeutig stationär.

**Quadratsymmetrie und positive Übergangsraten lassen das Verhältnis b/a
frei.** Semigruppenkomposition exp(-(t+s)L)=exp(-tL)exp(-sL) gilt für
jede dieser Möglichkeiten und wählt das Verhältnis nicht aus.

## Konstruktive engere Auswahl

Wenn NUR der Uhrschritt R und sein inverser Schritt als elementare lokale
Übergänge zugelassen sind, ist b=0 und L bis auf Skala eindeutig. Dies ist
eine sinnvolle zusätzliche Lokalitätsvorschrift, aber ihre physische
Gültigkeit folgt nicht allein aus der Existenz der vier Punkte.

Eine andere positive, symmetrieverträgliche Wahl ist sqrt(L(1,0)):

    sqrt(L(1,0)) = (1/2)L_edge + ((sqrt(2)-1)/2)L_diag.

Der Prüfer bestätigt Quadrat, Positivität über das angegebene Spektrum
und die Spektralwerte 0,sqrt(2),sqrt(2),2. Wärme-Laplacian und
Poisson-/Wurzelgenerator sind unterschiedliche Dynamiken bei denselben
Punkten. Welcher Typ zum physisch hergeleiteten Randoperator gehört, muss
aus der Rand-/Bulk-Konstruktion folgen. Kein willkürliches Auswählen des
gewünschten Spektrums.

## Vollständig gelöster Vier-Spin-Gegentest

Als weitere ausdrücklich deklarierte Annahme wird an jeden Punkt ein
Spin 1/2 gesetzt und die relationale Paarform h_ij=I-P_singlet,ij verwendet.
Dies ist nicht bereits eine Einbettung der TFPT-Materiefelder. Setze

    H(r)=sum_edges h_ij + r sum_diagonals h_ij, r>=0.

Mit SA=S0+S2, SB=S1+S3 und S=SA+SB folgt

    H(r)=3I + S^2/2 + (r-1)(SA^2+SB^2)/2.

Die möglichen Zwischen-Spins SA,SB sind 0 oder 1. Damit ist das gesamte
Spektrum für jedes r analytisch bestimmt:

| Energie | Multiplizität |
| --- | ---: |
| 3 | 1 |
| 3+r | 6 |
| 1+2r | 1 |
| 2+2r | 3 |
| 4+2r | 5 |

Bei zusammenfallenden Werten werden die Multiplizitäten addiert.

Für 0<=r<1 ist der Grundzustand eindeutig mit Energie 1+2r. Für r>1
ist ein anderer, dazu orthogonaler Grundzustand eindeutig mit Energie 3.
Bei r=1 sind beide entartet. Somit kann der Übergang von drei auf vier
Spins die vorherige Grundzustandsentartung beseitigen; die Eindeutigkeit
ist aber weiter von Zusammensetzung und Gewichtungsverhältnis abhängig.

Insbesondere liefern r=0 und r=sqrt(2)-1 denselben Grundzustand, aber
unterschiedliche Anregungsspektren. Das Paar „eindeutiger Zustand plus
Quadratsymmetrie“ ist daher selbst in dieser kleinen kontrollierten
Familie kein eindeutiges Naturgesetz.

Literaturkontext: Dies sind bekannte Heisenberg-Clustermechanismen, keine
beanspruchte neue Theorie. Die hier benötigte konkrete Formel wurde
unabhängig aus den Spinmatrizen berechnet. Vergleiche beispielsweise
https://www.nature.com/articles/srep03583 (vierseitiges Modell mit
getrennten horizontalen, vertikalen und diagonalen Kopplungen).

`square_composition.py` prüft die lineare Klassifikation und die gesamte
symbolische charakteristische Gleichung; keine numerische Rangschwelle.
Keine dieser Aussagen schließt einen T1–T8-Vertrag.
