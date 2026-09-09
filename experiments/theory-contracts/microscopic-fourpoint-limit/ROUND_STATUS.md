# TFPT: mikroskopische Vierpunktfunktionen und die Clock-/Rotor-Schnittstelle

2026-09-09. Ausgangspunkt: HEAD `b803b7e5d0e4ac20c0a1ce7bffee0f91326dcff4`.
Diese Fortsetzung ist lokale Forschung auf dem vorhandenen Stand. Sie ändert
weder den ursprünglichen Hamiltonoperator noch Paper, Webseite oder T1--T8-Status.
Kein Commit, Push oder RH-/TOE-Abschluss dieser Runde.

## 1. Der nächste echte Korrelationsschritt ist analytisch geschlossen

Nach dem neutralen Zweipunktresultat liegt jetzt ein vollständiger Beweis für
die **normalgeordnete neutrale Vierpunktfunktion derselben mikroskopischen
Quelle** vor. Er betrifft weiterhin den width8/mass1/r1-QWZ-Sektor mit
delta=4N^(-3/4) und seinem tatsächlichen negativen Spektralvakuum.

Der [Quellenbeweis](README.md) kontrolliert das vollständige Determinantenwort,
einschließlich Phase, Bottom-Rest und der gesamten rotierenden Historien.
Er ersetzt es nicht durch einen passend gewählten kleinen Randdeterminanten.
Der parallele [Current-Beweis](../current-fourpoint-limit/README.md) berechnet
den Zielkern direkt aus der Weyl-Algebra und behandelt sämtliche Kollisionen.

Der neue technische Hebel ist einfach: Das Hilfsfenster des Beweises darf
kleiner sein als bisher. Das Potenzfenster M~N^(3/8) liefert bereits

```
sup_Gitter |Z_t^4 C_N^circ - K_t| = O(N^(-3/8)).
```

Eine exakt ganzzahlige logarithmische Wahl M~N^(1/4) log N verbessert dies zu

```
sup_Gitter |Z_t^4 C_N^circ - K_t| = O(N^(-3/4) (log N)^3).
```

Nur die Hilfsreferenz ändert sich, nicht das physikalische C_N^circ.
Die Schranken sind asymptotisch; ihre groben Konstanten liefern bei üblichen
Gittergrößen keine kleinen zertifizierten Fehler. Dieser Logarithmus folgt
aus der Kontrolle von Hochenergieresten, nicht aus einer nachgewiesenen
E8-Kaskaden- oder Primzahldynamik.

## 2. Mehr als getrennte Punkte: volle verschmierte Vierpunktgrenze

Für epsilon=(-1,+1,-1,+1) lautet der Grenzkern

```
K_infinity(a1,a2,a3,a4)
 = product_(i<j) (1-exp(2pi i(a_j-a_i)))^(epsilon_i epsilon_j/4).
```

Jeder Faktor besitzt seinen eigenen geordneten analytischen Logarithmuszweig.
Das Produkt darf nicht in eine einzige Hauptwurzel umgeschrieben werden.
Beispielsweise ist der Wert bei (0,1/4,1/2,3/4) gleich exp(i pi/8), nicht 1.

Positive Gaußfaltung, Jensen und zweimal Cauchy--Schwarz liefern eine
uniforme Lp-Schranke für 1<p<2 auf dem gesamten Vier-Endpunkt-Torus.
Daraus folgt die volle komplexe L1-Konvergenz einschließlich aller
Kollisionsumgebungen. Die mikroskopische Gitterinterpolation kostet zusätzlich
O(N^(-5/8)); damit ist auch der ursprüngliche Quellenkern in L1 kontrolliert.

Die richtige positive Paarform verwendet **K_infinity(b,a,c,d)**. Die Umkehr
des ersten Endpunktpaares ist unverzichtbar. Sie ist der Grenzwert echter
endlicher Slater-Gramformen, mit dem Normalphasenfaktor einmal am Fockvektor.
Das ist keine OS-Positivität oder vollständige Rekonstruktion lokaler Felder.

Der Current-L1-Beweis deckt alle sechs neutralen Vierer-Zeichenfolgen ab.
Für die ursprünglichen U_a heben sich die äußeren Rampen jedoch nur im
hier verwendeten alternierenden Wort U_a* U_b U_c* U_d automatisch auf.
Allgemeine signierte F-Wörter sind nicht automatisch dieselben physischen U-Wörter.

## 3. Unabhängige Gegenprüfung und endliche Quellenkontrollen

Der vollständige Quellenbeweis und beide Fenster wurden unabhängig intern
gelesen; dabei wurde keine lasttragende Lücke gefunden. Die allgemeine
L-abhängige Galerkinrate und der Fock-Normalphasenfaktor wurden im Text
präzisiert. Umgekehrt wurde der komplette Current-BCH-/Lp-/Vitali-/Gram-Beweis
vom Hauptzweig unabhängig gelesen. Das ist keine externe Peer Review und
kein formaler Beweisassistenten-Nachweis.

Die vollständigen endlichen Quellmatrizen ergeben für die Viertelkreis-Endpunkte:

| N | Hilfsfenster M | Normierter komplexer Quellen-/Current-Abstand |
|---|---|---|
| 8 | 1 | 0.0858750 |
| 16 | 2 | 0.0346276 |
| 32 | 3 | 0.0123829 |

Ein zusätzlicher unsymmetrischer Test bei N=24 und Endpunkten
(1,5,13,21)/24 ergibt 0.0137880. Die exakte gemeinsame Restblockreduktion
wird bis auf Gleitkommafehler von höchstens 2.32e-13 reproduziert.
Diese Zahlen kontrollieren Implementierung und Phase; die Tabelle beweist
weder die asymptotische Rate noch Kollisionsintegrabilität.

Der Testlauf und alle Herkunftspins werden in [TEST_RESULTS.md](TEST_RESULTS.md)
mit vollständig gespeicherten Ergebnissen dokumentiert.
Alle zehn beteiligten Testsuiten wurden frisch ausgeführt: **112 Tests normal
und 112 Tests mit -OO bestanden**, einschließlich der separaten Clock-Klassifikation.

## 4. Was der Vergleich noch eröffnet, ohne es vorwegzunehmen

Mit dem logarithmischen Fenster lässt sich dieselbe Quellvergleichskette
für jedes feste neutrale signierte F-Wort gerader Länge L<28 abschätzen:

```
Z_t^L |C_source^circ-C_current| = O(N^((L-28)/32) (log N)^3).
```

Das eröffnet die Vergleichsseite bis einschließlich 26 Faktoren. Es liefert
**nicht automatisch** die zugehörigen höheren Kollisionsgrenzen, gemeinsame
Operatorbereiche, geladene Nullmoden oder vollständige Felder. Die Zahl 28
ist die Grenze dieses groben Fehlerbudgets, kein physikalisches No-go.

Die bereits vorhandene E8-Ladungs-/Nullmodus-Zieldarstellung in
[charged-cocycle-lift](../charged-cocycle-lift/README.md) muss aus der Quelle
identifiziert werden; sie als unabhängigen Tensorfaktor anzuhängen würde
diese Pflicht nicht erfüllen. Der nächste entscheidende Test dieser Front
ist deshalb eine mikroskopische, adjungiertenverträgliche Ladungsabbildung
mit Ladungs-Ward-Identität, richtigem Kozyklus und gemeinsamen Energie-/Domain-Schranken.

Selbst ein vollständiger Abschluss dieser Front wäre noch keine TOE:
Clock, Materie, Raumzeit und Gravitation müssen dieselbe physikalische
Algebra und denselben ausgewählten Parent teilen. Getrennt richtige Modelle
werden hier nicht zu einem vermeintlichen gemeinsamen Beweis addiert.

## 5. Clock/Rotordynamik: die einfache lokale Identifikation ist ausgeschlossen

Der parallele [Clock-/Rotor-Strukturbeweis](../clock-rotor-joint-charge/README.md)
prüft ausdrücklich den vorhandenen Zwei-Spezies-Parent einschließlich aller
gemischten L/H-Hoppings, Zweischrittpfade und unbeschränkten elektrischen Flüsse.
Es wird kein zusätzlicher Kopplungsterm eingefügt.

Die drei wirklichen Vorwärtsterme pro Kante erzwingen für die C6-Grade

```
h_x=l_x=:q_x, k_(u->v)=q_v-q_u.
```

Damit sind alle Rotorphasen exakte Gradienten und sämtliche geschlossenen
Wegphasen null, auch auf nichtkontrahierbaren Toruszyklen. Noch wichtiger:
Der gemeinsame Implementierer ist exakt

```
W=exp[-i theta sum_x q_x] exp[-i theta sum_x q_x G_x], theta=2pi/6.
```

Auf dem physikalischen Gauss-Raum G_x=0 bleibt nur ein globaler Skalar.
Die gemeinsame Symmetrie ist deshalb **keine zusätzliche physikalische Clock**.
Sie erhält den Hamiltonoperator, wirkt nach der Eichreduktion aber trivial.

Außerdem müssen auf vier nichtisolierten L/H-Zellen alle Clock-Eigenwerte
gerade Vielfachheit besitzen. Die tatsächliche ursprüngliche Clock hat
die Grade (0,0,0,0,0,2,3,4), also Vielfachheiten 5,1,1,1.
Eine basiswechselnde unitäre Achtmodenabbildung kann dies nicht reparieren.
Die vorhandenen verschiedenen Onsite-Energien schließen auch eine
rotorunabhängige ortsfeste U(2)-Mischung als Ausweg innerhalb dieser Klasse aus.

Diese Grenze ist eng definiert: Nichtlokale oder räumlich permutierende
Wirkungen, Bogoliubov-Abbildungen, flussabhängige Dressings oder andere
Parent-Modelle werden dadurch nicht allgemein widerlegt. Die zuvor
nachgewiesene elektrische Wechselwirkung verschwindet nicht; ihre
physikalische Identifikation mit der ursprünglichen Clock bleibt offen.

Die Prüfung umfasst alle 7776 Phasenzuordnungen einer vollständigen Kante
(genau 36 Lösungen), alle 1296 Ortsgradzuordnungen des Quadrats, symbolische
Gauss-Identitäten für beliebige ganzzahlige Flüsse und vollständige
Hamilton-Aktionen einschließlich großer positiver/negativer Flüsse.
Der nächste Clock-Kandidat muss zuerst **nichttrivial auf der physikalischen
Gauss-Algebra wirken** und die volle ursprüngliche Clock-Darstellung tragen.
Ein formal erhaltener lokaler Phasengenerator allein besteht diesen Test nicht.
