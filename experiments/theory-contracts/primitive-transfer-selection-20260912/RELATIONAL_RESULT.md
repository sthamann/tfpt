# Fortsetzung: skalare Phasen oder relationaler Grundbaustein?

12. September 2026. Exakte, begrenzte Vorwärtskonstruktion aus den
dokumentierten Compiler-Matrizen; keine vollständige TFPT-Herleitung.

## Zusammenfassung

Die geprüfte skalare μ4-Charakterroute ist entschieden: Auf den drei
Quaterniongeneratoren zusammen mit dem gegebenen Familienzyklus bleibt
nur der triviale μ4-wertige Gruppencharakter. Die spinorielle zentrale
Minuswirkung lässt sich nicht als solcher Charakter ausdrücken.

Ein konkreter positiver Ersatz funktioniert: Auf dem bereits mathematisch
vorhandenen Matrixraum M2(C) wählt eine relationale Vergleichsenergie den
Identitätsvektor eindeutig aus. Die drei relativen Gewichte dieser
festgelegten Vergleichsfamilie werden durch Familienkovarianz gleich.
Dies erzeugt eine explizite positive Transferfamilie ohne H70-Zielparameter.

Es ist zunächst eine tracial-relaxierende Dynamik auf einem Operatorraum,
nicht die physische unitäre Zeitentwicklung des ursprünglichen Zweiersystems.
Ein zusätzlicher Zyklusdefekt lässt wieder ein freies relatives Gewicht zu.
Die einfachste Verkettung physisch interpretierter Paarbausteine hat bereits
bei drei Spins keinen eindeutigen Grundzustand. Diese Grenzen wurden geprüft,
nicht durch Begriffswechsel übergangen.

## 1. Quelle und zusätzliche Annahmen

Quellmatrizen aus `../compiler-cone-object-audit/ORDER_PROOF.md`, §§1,3:

    u1=diag(i,-i), u2=[[0,1],[-1,0]], u3=u1u2,
    w=(I+u1+u2+u3)/2.

`MARKED_BRIDGE.md`, §2, identifiziert den markierten Familienzyklus durch
F(sigma x)=w F(x) w*. Das ist eine echte ererbte Markierung, nicht eine aus
dem gewünschten H70-Spektrum ausgesuchte Richtung. Der markierte Gitter-
Rückweg allein begründet aber keine physische Hilbertraumidentifikation.

Zusätzliche Kandidatenannahmen, noch nicht aus P1/P2 hergeleitet:

1. komplexifizierter Matrixraum mit Hilbert–Schmidt-Skalarprodukt als
   Zustandsraum des Vergleichs;
2. Konjugationsabweichungen zu u1,u2,u3 als elementare positive Kosten;
3. Kovarianz dieser Kosten unter dem dokumentierten Familienzyklus;
4. Exponentiation der Kosten als Transfer;
5. nur im Drei-Spin-Test: lokale Tensorprodukte und Addition über zwei
   überlappende Kanten als konkrete Zusammensetzungsregel.

Keine H70-Kopplung oder aus H70 erzeugte Zustandsantwort wird eingegeben.

## 2. Vollständiger Charaktertest in der bezeichneten Klasse

Die Quaternionrelation liefert [u1,u2]=-I. Jeder eindimensionale komplexe
Gruppencharakter annihiliert Kommutatoren, also chi(-I)=1. Somit
chi(uj)^2=1. Es gibt vier Charaktere auf Q8, mit Zeichen

    (chi(u1),chi(u2),chi(u3)) = (+++),(+--),(-+-),(--+).

Der Familienzyklus w permutiert u1,u2,u3. In einer eindimensionalen
Darstellung muss daher chi(u1)=chi(u2)=chi(u3) gelten. Zusammen mit
chi(u3)=chi(u1)chi(u2) erzwingt dies dreimal +1. Schließlich gilt w^3=-I,
also chi(w)^3=1. In μ4 bleibt chi(w)=1.

Der Prüfer enumeriert alle μ4-Zuordnungen zu den genannten Generatoren
und prüft die notwendigen Relationen; nur die triviale bleibt und sie ist
offensichtlich eine gültige Darstellung. In ganz U(1) wären kubische
Charaktere für w möglich, aber weiterhin keine spinorielle zentrale
Minuswirkung. Ein Charakter nur der zyklischen Untergruppe <u1> kann
chi(u1)=i tragen, lässt sich so jedoch nicht auf Q8 fortsetzen.

Das gilt NICHT für beliebige projektive/matrixwertige Darstellungen,
lokale Phasen auf einem Groupoid oder einen noch konstruierten Seam-Transport.

## 3. Positiver relationaler Baustein

Auf M2(C) definiere

    Rj(A)=uj A uj*,  D_j=I-Rj,
    Q=sum_j D_j* D_j.

Mit zeilenweiser Vektorisierung ist Rj=uj tensor conjugate(uj). Setze

    Omega=(|00>+|11>)/sqrt(2), P=|Omega><Omega|.

Exakt folgt

    Q=8(I-P),  spec(Q)={0,8,8,8}.

Beweis: Die gemeinsame Fixalgebra der Quaternion-Konjugationen besteht
nur aus skalaren Matrizen, daher ist ihr gemeinsamer Kern span(I).
Auf uj wirken die beiden anderen Konjugationen mit Vorzeichen -1.
Jede dieser beiden Abweichungen trägt 4 bei. Die Basis I,u1,u2,u3
diagonalisiert Q und ergibt die angegebene Formel.

Für Q_alpha=sum alpha_j D_j*D_j sind die drei Nichtnullenergien

    4(alpha_2+alpha_3), 4(alpha_1+alpha_3), 4(alpha_1+alpha_2).

Fordert man Familienkovarianz [Q_alpha,Rw]=0, erzwingt der zyklische
Austausch dieser drei Werte alpha_1=alpha_2=alpha_3. **Innerhalb genau
dieser Familie** sind damit die relativen Gewichte hergeleitet; eine
gemeinsame Energie-/Zeiteinheit bleibt frei.

Das Ergebnis besitzt eine einfache relationale Interpretation: Ein
einzelner Spinor hat unter allen Quaternionoperationen keinen invarianten
Vektor; der Vergleich mit seiner dualen Seite besitzt hingegen genau einen.
Auf beiden Seiten gemeinsam hebt sich das zentrale Minus auf. Auf einer
einzelnen Seite ist -I weiterhin -I. Zugang zu einer einzelnen Seite ist
aber eine zusätzliche Operationsfrage und kein bereits konstruiertes
physisches Half-Charge-Feld.

## 4. Der Transfer ist explizit – aber welcher Typ von Dynamik?

Für t>=0 ist

    T_t=exp(-tQ)=P+exp(-8t)(I-P).

Als Operator auf dem Vergleichs-Hilbertraum ist T_t bei endlichem t strikt
positiv; für t>0 hat er einen einfachen größten Eigenwert 1. Sein
Logarithmus liefert Q, ohne H70 einzusetzen. Bei t=0 ist T_0=I und der
größte Eigenwert nicht einfach.

Als Abbildung auf ursprünglichen Zweiermatrizen lautet dieselbe Formel

    T_t(A)=exp(-8t) A + (1-exp(-8t)) Tr(A) I/2.

Das ist der bekannte depolarisierende Quantenkanal. Der stationäre Zustand
ist I/2. Für eine anfangs reine Dichtematrix beträgt die Reinheit nach t

    Tr(rho_t^2)=(1+exp(-16t))/2 < 1  für t>0.

Damit ist diese Entwicklung KEINE unitäre Entwicklung des einzelnen
Zweiersystems. Der reine Vektor Omega auf dem verdoppelten Raum induziert
auf der linken Algebra gerade den Spurzustand, dessen modularer Generator
bis auf die Konstante trivial ist. Die Operatoren Q auf M2(C) und H auf C2
dürfen nicht identifiziert werden. Man könnte exp(-itQ) als unitäre
Viererdynamik definieren; deren physische Rolle wäre eine neue Annahme.

## 5. Noch immer keine globale Eindeutigkeit der Kostenfamilie

Auch w ist in der Quelle vorhanden. Erlaubt man zusätzlich

    Q_beta=Q+beta (I-Rw)* (I-Rw), beta>=0,

bleiben Familienkovarianz, Positivität und derselbe eindeutige Nullzustand
erhalten. Die Energien sind jedoch

    0, 8, 8+3beta, 8+3beta.

Ein gemeinsamer Skalenwechsel entfernt beta nicht. Man muss also begründen,
ob der Zyklus nur eine Symmetrie oder selbst ein primitiver Kostenterm ist.
Volle Kovarianz unter ALLEN Quaternion-Konjugationen wäre stärker und
würde diesen Zusatz einschränken; auch diese Forderung benötigt eine
physische Begründung. Der positive Dreierfamilien-Satz ist keine
Klassifikation sämtlicher aus TFPT zulässiger Transfers.

## 6. Frühzeitiger Zusammensetzungstest

Durch einen festen unitären Basiswechsel auf einer Seite wird Omega zum
Zwei-Spin-Singulett s=(|01>-|10>)/sqrt(2). Der normierte Paarterm ist

    h=I-|s><s|=(3I+sigma_x tensor sigma_x
                       +sigma_y tensor sigma_y
                       +sigma_z tensor sigma_z)/4.

Dies ist die bekannte antiferromagnetische Heisenberg-Paarform, keine
neue physikalische Theorie. Primärer Literaturkontext für solche
SU(2)-invarianten Spin-Zustände:
https://arxiv.org/abs/quant-ph/0212114 .

Teste nun ausdrücklich die neue Hypothese H3=h12+h23 auf drei Spins.
Die exakte charakteristische Gleichung ist

    det(xI-H3)=(x-1/2)^2 (x-3/2)^2 (x-2)^4.

Der Grundwert ist 1/2, zweifach entartet. Kein Zustand erfüllt beide
Paarbedingungen perfekt. Insbesondere gilt P12 P23 P12=P12/4.
Der mittlere Spin kann nicht mit beiden Nachbarn zugleich in einem reinen
Singulett stehen. Die Einzigartigkeit des isolierten Paares überträgt sich
also nicht durch diese einfache Verkettung auf das Gesamtsystem.

Die positive Untergrenze ist konstruktive Frustration, nicht Inkonsistenz.
Andere Graphen, Randbedingungen oder globale Zustände sind dadurch nicht
ausgeschlossen. Deren Wahl aus der Quelle bleibt aber eine eigene Pflicht.

## 7. Stand und nächste Abnahme

Gelöst sind in dieser Runde die bezeichnete skalare Charakterklassifikation,
der relationale Zweiervergleich einschließlich Transfer und relativer
Dreiergewichte unter Familienkovarianz, und der exakte Drei-Spin-Gegentest.

Nicht gelöst: vollständige primitive Kostenfamilie, physische Interpretation
der zwei Seiten, Zusammensetzungsgeometrie, unitäre Materie-/Rotorzeit,
H70-Einbettung, T1–T8 oder irgendeine arithmetische globale Vermutung.

Der nächste Herkunftstest darf deshalb nicht bloß einen größeren Graphen
nach einer schönen Lücke durchsuchen. Er muss aus der markierten Quelle
entscheiden, **welche Seiten gekoppelt werden und welche Operationen
Kosten statt bloßer Symmetrie sind**. Erst danach ist eine physisch
typgerechte Vorwärtsrechnung auf dem daraus bestimmten Verbund sinnvoll.

## Reproduktion

`python3 -B phase_relational.py` und `python3 -B -OO phase_relational.py`:
30 exakte Prüfungen, explizite Fehlerzweige statt abschaltbarer Assertions.
Quellhashes stehen im JSON; keine Fremdquellen werden verändert.
Das Paket ist Forschungscode, nicht unabhängig Lean-formalisierte Mathematik.
