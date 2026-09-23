# Auswahl des minimalen Randoperators: bedingter Abschluss und engste offene Voraussetzung

22. September 2026 · unabhängige mathematische Prüfung · **CONDITIONAL / PROOF-GAP**

## Ergebnis

Die vier Defekte

\[
\mathfrak D(B)=
(|\operatorname{SF}|,\operatorname{rank}_{\rm ess},
\deg_{\det}^{+},h_\Sigma^{\rm red})
\]

liefern für sich keinen Eindeutigkeitsbeweis für einen vollständigen
Randoperator. Auch für die **explizit aufgezählten** P1- und P2-Invarianten
liegt ein solcher Eindeutigkeitsbeweis nicht vor: P1 fixiert
Reflexionspositivität, Einheitswindung und `c3=1/(8 pi)`, P2 die `3+2`-Schnittstelle.
Diese Daten kontrollieren Topologie, Normierung und Trägertyp, aber nicht alle
Terme nullter Ordnung oder alle dimensionslosen Spektralverhältnisse eines
Dirac-Kragenoperators.

Es gibt jedoch einen präzisen bedingten Eindeutigkeitssatz. Er benutzt eine
Struktur, die im operationalen Seed bereits als `tau_t` vorkommt:

> **Wenn zwei Kandidaten bereits dieselben vollständigen P1-Schwingerdaten
> besitzen, diese Daten die positive euklidische
> Transfersemigruppe bestimmen und der Kragenoperator über eine feste injektive
> Generatorabbildung aus genau dieser Semigruppe rekonstruiert wird, dann ist
> der Kragenoperator relativ zu diesen festgehaltenen Schwingerdaten bis auf
> unitäre Äquivalenz eindeutig.**

Dieser Satz beweist nicht, dass P1/P2 und die Clocks zunächst genau einen
vollständigen Schwingerkern auswählen. Das ist ein logisch früherer Engpass.
Die gelesene Quelle beweist außerdem die anschließende
Generatoridentifikation nicht.
In der Definition des operationalen Seeds stehen `tau_t` und `D_coll` als zwei
getrennte Einträge. Statt einer weiteren ganzzahligen Defektkoordinate fehlen
damit zwei aufeinanderfolgende Aussagen:

\[
\text{P1/P2/Clocks}\stackrel{?}{\longrightarrow}
\{\mathcal K_{\rm full}\},
\tag{K}
\]

also die Auswahl genau eines vollständigen Schwingerkerns, und danach die
Injektivität

\[
\mathcal K_{\rm full}
\longmapsto [\mathcal D_{\rm coll}]_{\rm unitary}.
\tag{G}
\]

Der erreichte Stand ist deshalb in drei Ebenen zu trennen:

1. **Vollständiger P1/P2-Kandidat:** Für einen bereits festgehaltenen
   vollständigen Schwingerkern ist unter (G) die Eindeutigkeit des
   Kragenoperators bewiesen. Offen sind davor die Auswahl genau dieses Kerns
   aus P1/P2/Clocks und danach die Anwendbarkeit von (G).
2. **Minimale Operatorklasse:** Eine beschränkte Nullordnungsfamilie hat bei
   festem Hauptsymbol und fester Domäne nur dann dieselben vier Defekte, wenn
   zusätzlich Kern, Träger-/Determinantenklasse und die ganze markierte
   Fredholmhomotopie erhalten bleiben. Das ist eine bedingte Lemmaform, keine
   schon konstruierte Gegenfamilie.
3. **Physische Gegenfamilie:** Erst ein tatsächlich zugelassenes nichtskalares,
   Clock-äquivariantes `V`,
   das auch die gekoppelte Reflexionspositivität und relative Wirkung erhält,
   würde zwei physisch zulässige minimale Quellen liefern. Dieser letzte
   Existenznachweis liegt nicht vor.

## 1. Was die Originalbedingungen tatsächlich fixieren

`tfpt_1_architecture_e8.tex:167-188` formuliert:

- P1: ein primitiver reflexionspositiver Randkern, Einheitswindung und die
  Selbstverkettungsnormierung `c3=1/(8 pi)`;
- P2: eine fünfstellige Schnittstelle mit `3+2`-Zerlegung.

Die Clock- und Compilerbedingungen fixieren anschließend diskrete Wirkungen,
Markierungen und Darstellungen. Sie sind bei jeder zulässigen Deformation als
Äquivarianzbedingungen beizubehalten. Keine der genannten Bedingungen ist aber
eine vollständige Liste der Eigenwerte und Eigenprojektoren von `B_Sigma`.

Die operative Quellklasse in
`01_boundary_kernel_source.tex:480-520` besteht aus

\[
\mathfrak S=(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,
[u_\Sigma],\mathcal D_{\rm coll}).
\]

Reflexionspositivität ist eine Bedingung an `omega`; `D_coll` wird separat nur
als erstordentlicher elliptischer, reflexionsregulärer Kragengenerator verlangt.
Der Text sagt, dass `D_coll` den Randoperator bestimmt. Er sagt nicht, dass
`tau_t` oder `omega` umgekehrt `D_coll` bestimmen.

Der Defektbeweis in `01_boundary_kernel_source.tex:543-682` erhält daher nur
diskrete Homotopie- und Rangdaten. Die Kragen-Normalform

\[
D_+=\gamma_n(\partial_n+B_\Sigma)
\]

setzt einen selbstadjungierten adaptierten Operator ein; sie klassifiziert
dessen Terme nullter Ordnung nicht. Die spätere Barriere aus
`02_carrier_source.tex:3021-3062` setzt bereits
`B \cong B_min` voraus.

## 2. Exakter bedingter Eindeutigkeitssatz

**Satz.** Seien zwei operationale Seeds auf derselben markierten positiven
Quellenalgebra gegeben. Es gelte:

1. ihre vollständigen P1-Schwingerfunktionen stimmen überein, einschließlich
   der positiven Zeitverschiebungen;
2. die OS-Nullräume werden quotiert und die Zeitverschiebungen induzieren eine
   stark stetige symmetrische Kontraktionssemigruppe `T_s`;
3. auf dem rekonstruierten Hilbertraum gilt
   \[
   T_s=e^{-sH},\qquad s\ge0,
   \]
   und `D_coll` wird durch eine für die ganze zulässige Klasse feste injektive
   Abbildung `F` aus `H` gewonnen:
   \[
   H=F(D_{\rm coll});
   \]
4. Domäne, reale Struktur, Graduierung, P1-Normierung und Clock-Markierungen
   werden von dieser Rekonstruktion mitgeführt.

Dann sind die beiden Kragenoperatoren **relativ zu den bereits als gleich
vorausgesetzten vollständigen Schwingerdaten** unitär äquivalent.

**Beweis.** Gleiche vollständige reflexionspositive Schwingerdaten ergeben
dasselbe OS-Skalarprodukt und dieselbe Darstellung der positiven
Zeitverschiebungen, also bis auf die kanonische OS-Einheit dasselbe `T_s`.
Eine stark stetige symmetrische Kontraktionssemigruppe besitzt einen eindeutigen
nichtnegativen selbstadjungierten Generator `H`. Wegen der Injektivität von
`F` ist damit auch `D_coll` einschließlich seiner Domäne und der mitgeführten
Strukturen bis auf dieselbe Einheit bestimmt. ∎

Der Satz ist nicht zirkulär, wenn zuerst der vollständige Kern unabhängig
ausgewählt oder ausdrücklich als P1-Eingabe deklariert wird und `F` unabhängig vom gewünschten
Randoperator bewiesen wird, etwa wenn `D_coll` selbst der Transfergenerator
auf einer fest bezeichneten Komponente ist. Wird dagegen „P1-Randkern“ schon
als vollständige unitäre Klasse von `D_coll` definiert, ist die Eindeutigkeit
zwar wahr, aber als P1-Eingabe vorausgesetzt; die Defektminimierung leistet dann
keine zusätzliche Auswahl.

## 3. Warum eine nichttriviale Deformation bis zu genau diesem Gate reicht

Der vorherige Contract
`source-boundary-lift-selection-20260922/PROOF.md:58-80` beweist den passenden
analytischen Schritt: Bei festem Bündel, Clifford-Hauptsymbol und gültiger
selbstadjungierter Domäne unterscheiden sich glatte Verbindungen durch einen
beschränkten symmetrischen Term nullter Ordnung. Daher hat

\[
D_t=D_0+tV,\qquad
B_t=B_0+tV_\Sigma
\tag{1}
\]

für hinreichend kleines `t` dieselbe Domäne, dasselbe Hauptsymbol,
Selbstadjungiertheit und kompakten Resolventen. Fordert man zusätzlich

\[
V^*=V,\qquad
V\text{ ist }(J,\Gamma,\Theta)\text{-verträglich},\qquad
V\text{ ist Clock-äquivariant},
\tag{2}
\]

bleiben reale Struktur, Graduierung, Reflexionsmarkierung und die angegebenen
Clock-Wirkungen erhalten. Die einzelnen Defekte bleiben nur unter den jeweils
zusätzlichen Erhaltungsbedingungen konstant:

- Die Spektralflussklasse bleibt konstant, wenn `D_t` zu einer Homotopie der
  **ganzen markierten Fredholmfamilie** mit den benötigten invertiblen
  Endpunkten erweitert wird; das folgt nicht aus der kleinen Störung eines
  einzelnen Operators allein.
- Der wesentliche endliche Rang bleibt konstant, wenn der endliche
  Trägerblock in der Familie festgehalten wird.
- Die Determinanten-Chernklasse bleibt konstant, wenn das zugrunde liegende
  markierte Bündel festgehalten und nur seine Verbindung variiert wird.
- Der Gap-Projektorrang bleibt konstant, wenn keine deklarierte Gap-Schwelle
  gekreuzt wird.
- Die reduzierte Nullität bleibt nur konstant, wenn der Vergleichssektor
  invertibel ist oder die Kernräume explizit erhalten werden, etwa durch
  \[
  \ker B_t=\ker B_0
  \]
  für das betrachtete Intervall. Eine beliebig kleine beschränkte Störung kann
  sonst ursprüngliche Nullmoden anheben.

Diese Aussage gilt analytisch zunächst auf dem in der Quelle verwendeten
kompakten Cutoff. Für einen glatten, hinreichend abfallenden Spektraltest ist
dort die Spektralspur jedes `D_t` endlich. Im ungeschnittenen oder
nichtkompakten Problem folgt die Endlichkeit der **relativen** Wirkung nicht
allein aus der Beschränktheit von `V`; dort muss zusätzlich die benötigte
relative Spur-/Wärmekernklasse gleichmäßig in `t` bewiesen werden.

P2 und die ausdrücklich genannte P1-Selbstverkettungsnormierung `c3` können in
diesem bedingten Test festgehalten werden, indem Bündel, `3+2`-Trägerdarstellung
und Normierung nicht variiert werden. Daraus folgt nicht, dass der nicht weiter
ausgeschriebene **vollständige** P1-Kern fest bleibt; dessen Auswahl ist Gate
(K), seine Operatorinjektivität Gate (G). Die aus
`B_t` definierte Skala

\[
\chi_{\rm seed}(t)=\lambda_1^+(|B_t|)^{-1}
\]

kalibriert nur eine Dimension. Eine echte nichtskalare Deformation wird durch
ein veränderliches Verhältnis

\[
r_k(t)=
\frac{\lambda_k^+(|B_t|)}{\lambda_1^+(|B_t|)}
\tag{3}
\]

erkannt. Ist `r_k(t)` nicht konstant, können `B_t` und `B_0` auch nach der
Skalenablesung nicht unitär äquivalent sein.

Damit wäre (1), falls eine solche Richtung in der tatsächlichen Quellklasse
existiert, mehr als die frühere bloße positive Reskalierung. Die Quelle liefert
diese zusätzliche Variationsfreiheit bisher nicht. Es ist daher kein
vollständiges physisches Gegenmodell. Zwei Anwendbarkeitsfragen
müssen am tatsächlichen minimalen Seed geprüft werden:

1. Der Raum lokaler, Clock-äquivariant sowie `J/Gamma/Theta`-verträglicher
   Verbindungsterme `V` muss eine Richtung enthalten, für die (3) variiert.
2. Die physische Reflexionspositivität muss mit `D_t` gekoppelt sein und für
   diese Richtung erhalten bleiben. In der derzeitigen Definition kann man
   `omega` formal festhalten, weil keine Generatorgleichung zu `D_coll`
   verlangt wird. Das zeigt eine fehlende Kompatibilitätsbedingung in der
   deklarierten Kategorie, aber noch keine tatsächlich erlaubte
   Quellenvariation und kein zweites TFPT-Vakuum.

Unter der Existenz eines Terms aus (2) und den zusätzlich genannten Kern-, Gap- und Homotopievoraussetzungen sind am kompakten Cutoff die übrigen
analytischen und diskreten Bedingungen der lokalen Deformation durch
beschränkte Nullordnungsstörung und Homotopieinvarianz kontrolliert. Der
verbleibende physische Engpass ist die gemeinsame Existenz einer nichtskalaren,
Clock-äquivarianten Richtung und ihrer Kompatibilität mit Reflexionskern,
Zeitsemigruppe, relativer Wirkung und Kragenoperator.

## 4. Welche Originalbedingungen die Familie unterscheiden könnten

| Bedingung | Wirkung auf (1) | Stand |
|---|---|---|
| Dirac-Hauptsymbol | unverändert bei einer Verbindungsvariation | unterscheidet die Familie nicht |
| selbstadjungierte Domäne | bleibt bei beschränktem `V` gleich | kontrolliert |
| P1-Einheitswindung und `c3` | topologische Klasse und Normierung bleiben fest | unterscheidet dimensionslose Spektralform nicht |
| P2 und Clocks | erzwingen (2) | der vollständige äquivariante Kommutant des realen Kragenproblems ist nicht klassifiziert |
| Gap und vier Defekte | nur bei schwellenfreier Bewegung, expliziter Kernelerhaltung und Homotopie der ganzen markierten Fredholmfamilie konstant | bedingte Erhaltung, nicht automatisch |
| primitive Spektralwirkung für ein festes Profil | kann sich mit `t` ändern | es ist kein Variationsminimum über alle `D_coll` formuliert |
| spätere Master-Barriere | schließt alle anderen `B` per Definition aus | setzt die gesuchte Auswahl voraus |
| vollständiger OS-Kern plus (G) | bestimmt den Transfergenerator | hinreichend, aber in der Quelle nicht angewandt |

Eine einzelne Spektralwirkung `Tr f(D/chi)` ist kein Ersatz für (G). Selbst
wenn sie einen stationären Punkt besitzt, braucht Eindeutigkeit eine bewiesene
strikte Konvexität beziehungsweise globale Trennung auf der vollständigen
minimalen Operatorfaser. Eine solche Aussage steht in den geprüften Passagen
nicht.

## 5. Entscheidendes Akzeptanz-Gate

Eine Entscheidung über die ursprüngliche Auswahl verlangt einen der beiden folgenden Nachweise:

### Gate A: Kernwahl und relative Eindeutigkeit

Zuerst ist zu zeigen, dass P1/P2 und die Clocks einen vollständigen
Schwingerkern `K` eindeutig auswählen, oder dieser vollständige Kern muss
offen als P1-Eingabe deklariert werden. Erst danach konstruiere aus `K` die
OS-Semigruppe und beweise auf der P1/P2-/Clock-minimalen Klasse

\[
F(D_1)=F(D_2)
\quad\Longrightarrow\quad
D_1\cong D_2,
\]

einschließlich Domäne, `J`, `Gamma`, Markierungen und absoluter Normierung.
Damit ist `D_coll` relativ zum ausgewählten `K` eindeutig. Die vollständige
minimale Quelle ist erst eindeutig, wenn auch der logisch vorherige Schritt
`P1/P2/Clocks -> K` eindeutig ist. Die vier Defekte dienen nur dazu, die
richtige diskrete Schicht zu erreichen.

### Gate B: echter Restmodulus

Gib einen nichtverschwindenden zulässigen Term `V` aus (2) an und zeige für
ein Intervall von `t`:

\[
\text{RP}(D_t),\qquad
S_{\rm rel}(D_t)<\infty,\qquad
\mathfrak D(D_t)=\mathfrak D(D_0),\qquad
\ker B_t=\ker B_0,\qquad
r_k(t)\ne r_k(0).
\]

Dann besitzt die minimale Schicht ein dimensionsloses kontinuierliches Modul,
und eine zusätzliche Variationsgleichung oder ein zusätzlicher Quellenwert ist
notwendig.

Der gegenwärtige Text erreicht Gate A noch nicht: Weder die eindeutige Auswahl
des vollständigen Kerns noch dessen injektive Generatorabbildung ist bewiesen.
Gate B ist ebenfalls nur ein konditionaler Test. Es ist nicht bewiesen, dass
die ursprüngliche Quelle überhaupt eine solche nichtskalare,
Clock-äquivariante Verbindungskomponente zulässt oder dass diese Kern,
markierte Fredholmhomotopie, gekoppelte Reflexionspositivität und außerhalb des
kompakten Cutoffs die relative Spurklasse erhält.
Deshalb ist das belastbare Resultat ein Eindeutigkeitssatz relativ zu bereits
gleichen vollständigen Schwingerdaten und ein separat bedingter
Deformationstest. Weder die zusätzliche Quellenfreiheit noch eine gekoppelte
Reflexionspositivität werden behauptet. Es folgt kein universelles
Gegenmodell und kein No-Go für TFPT.
