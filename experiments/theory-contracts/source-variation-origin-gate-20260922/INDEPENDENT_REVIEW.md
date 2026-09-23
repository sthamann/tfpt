# Unabhängige mathematische Kurzprüfung des Quellenvariations-Gates

22. September 2026 · unabhängige interne Prüfung · keine externe Peer Review

## Urteil

Die kovariante Projektorformel, die Isospektriegrenze der endlichen
Spektralwirkung und der Kommutantensatz sind unter ihren jeweils genannten
Voraussetzungen korrekt. Sie schließen keine allgemeine TFPT-Quellenableitung
aus. Sie zeigen enger, dass die bisher inventarisierten skalaren Quellen- und
Determinantenlifts weder den gekrümmten `CP3`-Berry-Mechanismus noch die
Gross--Neveu-Massenkopplung von selbst erzeugen.

Dabei sind zwei mögliche Familienanschlüsse strikt zu trennen:

1. Der vorgeschlagene `CP3`-Mechanismus besitzt lokale, im Allgemeinen
   nichtverschwindende Berry-Krümmung.
2. Das vorhandene Flavor-Lokalsystem kann flach sein und dennoch nichtabelsche
   globale Daten tragen. Dort ist `M` eine Punktierungsmonodromie und `U` eine
   Deck-Äquivarianz. `U` muss nicht als gewöhnliche Schleifenholonomie
   dargestellt werden.

Nichtverschwindende Berry-Krümmung ist daher nur ein Akzeptanzkriterium für den
ersten Mechanismus, nicht für die bestehende flache Flavor-Verbindung.

## 1. Projektorkrümmung und Eichgrenze

Für einen hermiteschen Projektor `P` in einem Umgebungsbündel mit Verbindung
`nabla` gilt für die induzierte Verbindung auf `im P`

\[
F^P=P F^{\nabla}P+P(\nabla P)\wedge(\nabla P)P.
\]

Ist `P'=U P0 U^dagger` und wird zugleich die vollständige
Umgebungsverbindung als `nabla'=U d U^dagger` transformiert, dann gilt bei
konstantem `P0`

\[
\nabla'P'=0,\qquad F^{P'}=0.
\]

Das ist eine reine Rahmenänderung, sofern `U` eine Eichredundanz der
vollständigen Quelle ist und Verbindung, Zustand und Observablen gemeinsam
mittransformiert werden. Bleibt die Umgebungsverbindung physisch fest, kann
dieselbe Bewegung `P(q)=U(q)P0U(q)^dagger` dagegen eine echte
Quellenvariation sein. Die `CP3`-Rechnung ist deshalb ein korrekter bedingter
Zeuge, aber noch kein Herkunftsnachweis.

Eine flache Verbindung mit `F=0` kann zugleich nichtkommutierende globale
Monodromien besitzen. Aus `F=0` folgt somit kein Ausschluss des bestehenden
nichtabelschen Flavor-Lokalsystems.

## 2. Spektralwirkung

Für einen endlichen internen Operator

\[
D_F(q)=U(q)D_{F,0}U(q)^\dagger
\]

hängt `Tr f(D_F/chi)` nur von den Eigenwerten ab. Diese endliche Spur kann die
Eigenprojektorkarte nicht auswählen.

Für den vollständigen Differentialoperator sind zwei Fälle zu unterscheiden:

- Wird der ganze Operator einschließlich des induzierten Ableitungsterms als
  `D'=U D U^dagger` transformiert, bleibt er unitär äquivalent und die
  Spektralwirkung kann `U` nicht auswählen.
- Wird nur der interne Nullordnungsterm gedreht, während die physische
  Ableitung beziehungsweise Umgebungsverbindung fest bleibt, ist der volle
  Operator nicht unitär konjugiert. Dann können Wärme-Kern-Terme Gradienten
  und Krümmung sehen.

Dies ist kein allgemeines Spektralwirkungs-No-Go. Ein Gradiententerm allein
wählt jedoch ohne Rand-, Topologie- oder weitere Quelldaten noch keine
bestimmte nichtkonstante Projektorkarte aus.

## 3. Kommutantensatz und natürlicher Lift

Für einen festen Projektor `P` folgt aus

\[
[P,a]=[P,D]=[P,JaJ^{-1}]=0
\]

für alle Algebraelemente auch

\[
[P,[D,b]]=0.
\]

Lineare innere Fluktuationen und aus denselben kommutierenden Bausteinen
gebildete quadratische Terme erhalten daher `P`. Der Satz gilt nicht ohne
Weiteres für ein ortsabhängiges `P`, für eine Algebra mit echten
Offdiagonaloperatoren oder bei einer nichtkommutierenden Gegenalgebra.

Beim natürlichen Lift

\[
A_W=\rho(A_E)\otimes I_4
 +I_{16}\otimes\operatorname{diag}(r,r,r,-2-3r)\,\operatorname{tr}A_E
\]

bleibt der interne Projektor `P3=diag(1,1,1,0)` erhalten. Der Lift liefert
keine `3<->1`-Vertizes. Innerhalb des Dreierraums wirkt sein Familienanteil als

\[
r\,\operatorname{tr}(A_E)I_3,
\]

also skalar. Eine getrennt gelieferte nichtabelsche Verbindung im Dreierraum
ist damit vereinbar, wird durch diesen Lift aber nicht hergeleitet.

## 4. Bedeutung von `h=qD`

Ist `q` nur eine globale reelle Amplitude vor einem festen `D`, bleiben die
Spektralprojektoren konstant. Ist `q=q(theta)` ein positives räumliches Profil,
können räumliche Projektoren unter einer fest gewählten
Hilbertraumtrivialisierung variieren; die Bogenlängenabbildung ist dann selbst
`q`-abhängig. Ob diese Reparametrisierung Eichung oder Physik ist, entscheidet
die ursprüngliche Umgebungsgeometrie.

Für die Familienfrage genügt die engere, robuste Aussage: `qD` wirkt skalar im
internen `3+1`-Faktor. Daher gilt dort

\[
(1-P_3)\,\delta(qD)\,P_3=0.
\]

Räumliche Projektorbewegung erzeugt somit nicht automatisch eine
nichtabelsche interne Familienverbindung.

## 5. Gross--Neveu-Kanal

Eine skalare Lapse- oder Metrikfluktuation des freien nichtchiralen Systems
erhält die getrennten internen Symmetrien

\[
SO(10)_R\times SO(10)_L,
\qquad
SO(6)_R\times SO(6)_L.
\]

Ihre Elimination erzeugt kinetische beziehungsweise Stress-Tensor-Vertizes.
Der Gross--Neveu-Baustein

\[
B_D=i\chi_R^a\chi_L^a
\]

koppelt dagegen rechte und linke Felder und erhält nur die diagonale
Untergruppe. Bei symmetrieerhaltender Regularisierung kann eine reine
Metrikfluktuation diesen verbotenen Massenvertex nicht erzwingen. Eine
zusätzlich aus der Quelle hergeleitete chiralitätswechselnde skalare Kopplung
würde diese konkrete Ausschlussvoraussetzung verlassen.

## 6. Korrigiertes Akzeptanz-Gate

Der nächste Herkunftstest muss zuerst entscheiden, welcher der beiden
Familienmechanismen beansprucht wird.

### Flaches vorhandenes Flavor-Lokalsystem

Aus derselben ursprünglichen Quelle sind eine flache Rang-3-Verbindung, ihre
Punktierungsdaten und ihr Decklift herzuleiten. Im bereits geprüften
determinantengedrehten gemeinsamen Rahmen müssen gelten:

- die bezeichnete Punktierungsmonodromie ist die native Matrix `M`;
- die Decktransformation wirkt durch die native Matrix `U` und erfüllt die
  Äquivarianzbedingung der Verbindung;
- beide Wirkungen tragen dieselbe Metrik, Markierung und Quellenprovenienz.

Hier wird weder `F != 0` verlangt noch `U` als Schleifenholonomie behandelt.

### Gekrümmter `CP3`-Mechanismus

Soll stattdessen der neue gekrümmte Mechanismus verwendet werden, braucht es
eine physisch feste Umgebungsverbindung und mindestens zwei unabhängige
projektorbewegende Quellenrichtungen `Y_A=delta D/delta q_A` mit

\[
K_A=(1-P)Y_AP,
\qquad
K_A^\dagger K_B-K_B^\dagger K_A\ne0.
\]

Zusätzlich ist zu zeigen, dass die Bewegung nicht durch eine gemeinsame
Eichtransformation aller Quelldaten entfernt wird.

Für den Gross--Neveu-Anschluss muss dieselbe Quelle außerdem einen echten
Rechts--Links-Massenvertex liefern. Die bisher identifizierten skalaren
`qD`- und Determinantenlifts erfüllen diese Bedingungen nicht.

## 7. Logische Lücke der behaupteten minimalen Bordismuseindeutigkeit

Die ursprüngliche Defektabbildung

\[
\mathfrak D(B)=(|\operatorname{SF}|,\operatorname{rank}_{\rm ess},
\deg_{\det}^{+},h_\Sigma^{\rm red})\in\mathbb N^4
\]

liefert wegen der Wohlordnung der lexikographischen Ordnung die Existenz eines
minimalen **Defektvektors**. Der Invarianzsatz zeigt außerdem, dass
Präsentationsäquivalenzen die Menge der Minimierer erhalten. Beides beweist
nicht, dass die Faser über dem minimalen Defektvektor nur eine unitäre
Äquivalenzklasse enthält.

Der Originalbeweis benennt diese Restpflicht selbst: Die Eindeutigkeit werde
auf eine Klassifikation der finalen minimalen Schicht durch die einseitigen
Randdaten reduziert. Der spätere Beweis der „unique essentialized
defect-minimal representative“ führt in den gelesenen Passagen aber nur
Wohlordnung, Essentialisierung, Collar-Normalform, Reflexionspositivität und
Rekonstruktion eines induzierten Randdatums an. Eine Injektivitätsaussage

\[
\mathfrak D(B)=\mathfrak D(B_{min})
\quad\Longrightarrow\quad
B\cong B_{min}
\]

oder eine Klassifikation aller kontinuierlichen Spektralmoduln der minimalen
Schicht wird dort nicht bewiesen. Sofern kein getrennter Klassifikationssatz
diese Implikation liefert, bleibt die behauptete Eindeutigkeit eine offene
Voraussetzung.

Die spätere Barriere

\[
\mathbb B_{\rm lex}(B)=0\ \text{für }B\cong B_{min},
\qquad +\infty\ \text{sonst}
\]

schließt diese Lücke nicht. Sie setzt die ausgezeichnete Äquivalenzklasse
bereits in ihrer Definition voraus. Auch die anschließende Beschränkung der
kontinuierlichen Variablen auf `alpha`, `chi_geo`, `delta_ph` und `rho_vac`
klassifiziert keine möglicherweise weiteren Moduli der minimalen Schicht;
sie entfernt sie durch die gewählte Domäne des Funktionals.

Ein bedingter Diagnosetest ist die positive Skalierung `B -> aB`, `a>0`:
Sie erhält formal Vorzeichenprojektor, Nullität und die vier diskreten Defekte,
ändert aber im Allgemeinen die positiven Eigenwerte und ist daher nicht
unitär äquivalent. Dies ist nur dann ein echtes Gegenbeispiel, wenn die
Admissibilitätsklasse solche Skalierungen zulässt und dabei Hauptsymbol,
Reflection Positivity und relative Aktion erhalten bleiben. Eine bereits
fixierte Normierung oder Principal-Symbol-Bedingung kann die Familie
ausschließen. Der rigorose Befund ist deshalb die fehlende
Klassifikationsimplikation, kein globales Skalierungsgegenbeispiel.

## Reichweite

Bestätigt sind die bedingten Projektor-, Spektral- und Kommutantenaussagen.
Ausgeschlossen ist nur, dass die aktuell inventarisierten skalaren Daten den
gekrümmten Berry- und Gross--Neveu-Mechanismus bereits von selbst liefern.
Eine Herkunft der bestehenden flachen, global nichtabelschen
Flavor-Verbindung aus der Quelle bleibt ein zulässiger offener Weg. Es wird
kein universelles TFPT-No-Go, keine physische Quellenwahl und kein geschlossenes
T1--T8-Gate behauptet.

## Nachtrag der Hauptprüfung: alternativer Stromkanal

Nach dieser getrennten Prüfung wurde die exakte Grassmann-Identität
`B_a B_b = -J_R^{ab} J_L^{ab}` für alle 120 Paare und für die drei unabhängigen
45/15/60-Kopplungen in `current_channel.py` geprüft. Die Forderung in Abschnitt 6
nach einem elementaren Rechts-links-Massenvertex ist deshalb nur für den dort
betrachteten **skalaren Vermittlungsweg** notwendig. Allgemein kann eine
gemeinsame Stromvermittlung dieselbe normalgeordnete GN-Quartike erzeugen,
ohne einen elementaren solchen Zweifermionvertex einzuführen. Diese Aussage
ändert den Metrik-allein-Ausschluss nicht; gemeinsam gekoppelte dynamische
Eichfelder können dessen unabhängige R/L-Symmetrieannahme verlassen.
Propagator, Vorzeichen, Zustand und ursprüngliche Herkunft dieser Vermittlung
bleiben offen. Dieser Nachtrag ist die Integration durch die Hauptprüfung;
er wird nicht als nachträglich unabhängig geprüfter Quellennachweis ausgegeben.
