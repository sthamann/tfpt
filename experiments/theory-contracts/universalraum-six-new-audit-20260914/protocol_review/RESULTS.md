# Unabhängiger Review: ein Record zur Präparation und ein destruktiver Endtest

14. September 2026. Keine Änderungen an den Root-Prüfern.

## Urteil

Die vorgeschlagene Konstruktion ist innerhalb ihres deklarierten
Operationsvertrags korrekt. Sie liefert **exakte bedingte Präparation**
aus dem bekannten Stabilizerseed ξ und einen **exakten destruktiven
Zieltest** auf jedem nackten 256D-Materieeingang. PΩ wird dabei nicht
zirkulär als ausführbare Ressource eingesetzt.

Sei Cξ die tatsächlich angegebene Clifford-Schaltung mit Cξ|0⁸⟩=|ξ⟩.
Aus der unabhängig nachgerechneten Identität

\[
P^-_{03}|\xi\rangle=-\sqrt{3/8}|\Omega\rangle
\]

folgt mit Adjungieren

\[
\langle\xi|P^-_{03}=-\sqrt{3/8}\langle\Omega|.
\]

Der **ausgeführte** Endablauf lautet: R03 auf einem initialisierten
Pointer, Minusresultat auswählen, Cξ† auf Materie, alle acht
Rechenbasisbits messen und nur 00000000 akzeptieren. Sein Krausoperator ist

\[
K_{\rm end}=|0^8\rangle\langle0^8|C_\xi^\dagger P^-_{03}
=-\sqrt{3/8}|0^8\rangle\langle\Omega|,
\quad E_{\rm end}=K^\dagger K=(3/8)P_\Omega.
\]

Der Projektor steht auf der **bewiesenen rechten Seite** einer
Operatoridentität. Auf der Implementierungsseite stehen nur Record,
bekannte inverse Clifford-Schaltung und Rechenbasisauslesung. Das ist
eine zulässige Synthese eines Messeffekts, kein Projektororakel.

## Was genau damit geschlossen wird

- Die Präparation aus **diesem ξ** wird mit einem Record exakt; Erfolgsrate
  3/8 und idealer akzeptierter Zustand Ω.
- Der Endtest benötigt kein K^N, keinen kontrollierten Spektralfilter
  und keine asymptotische Konvergenz. Die Effektidentität gilt auf jedem
  nackten Materieeingang, auch für gemischte oder mit Zuschauern
  verschränkte Eingänge.
- Der Test hat auf Ω selbst nur Erfolgswahrscheinlichkeit 3/8.
  Er ist ideal frei von falschen Zielakzeptanzen, besitzt aber
  zielunabhängig die erklärte Detektionseffizienz.

**Nicht geschlossen:** R03 allein ist kein Zielprojektor auf beliebigem
Input; P−03 hat Rang 96. Der zusätzliche inverse Seedtest ist entscheidend.
Ein Beispiel |0,0,0,1⟩ passiert P−03 mit Wahrscheinlichkeit 1/2,
hat aber keine Ω-Komponente und wird vom vollständigen Endtest verworfen.

Der akzeptierte Endzustand ist 00000000, **nicht Ω**. Die Konstruktion
ist daher keine nondestruktive Lüdersmessung und keine universelle
zustandserhaltende Projektionspräparation. Will man nach dem Endtest
erneut Ω behalten, muss man die bekannte ξ-Präparation und einen neuen
Record anschließen und die zusätzlichen Kosten und den weiteren
Erfolgsfaktor 3/8 bilanzieren.

Die Vollraumgeltung betrifft hier den nackten 256D-Materieraum. Ein
beliebiger 544D-Eingang mit belegten Vermittlern wurde nicht allein
durch diese Gleichung als zusätzlicher akzeptierter Zieltest behandelt.

## Vollständiges Mehrzeitexperiment und Rohwahrscheinlichkeiten

Ein gestarteter Versuch präpariert ξ, behält das Minusresultat von R03,
führt C3 auf Site 0 aus, zweimal R01, C3† und den obigen Endtest.

Bei **behaltenem kohärentem Pointer** hebt R01² die Zwischenaufzeichnung
exakt auf. Beim **frischen Pointer** werden zwei getrennte Pointer
benutzt und ihre Endzustände verworfen beziehungsweise ungelesen
ausgewertet. Die resultierende Kanalwirkung ist die entsprechende
Dephasierung. Es gilt

\[
p_{\rm retained}=\frac38\frac38=\frac9{64},\qquad
p_{\rm fresh}=\frac38\frac{17}{32}\frac38
=\frac{153}{2048}.
\]

Das Verhältnis bleibt 17/32. Bedingt auf erfolgreiche Präparation sind
die abschließenden Akzeptanzen 3/8 beziehungsweise 51/256; sie dürfen
nicht als 1 und 17/32 ausgegeben werden. Die letzteren Zahlen betreffen
die ideale Rückkehr vor Berücksichtigung der Enddetektionseffizienz.

**Wichtig für die Umsetzung:** Den behaltenen Pointer zwischen seinen
zwei R01-Aufrufen zu messen oder zu dephasieren zerstört die kohärente
R²-Aufhebung. Ein bloß klassisch aufgehobenes oder erneut initialisiertes
Bit wäre ein anderer Ablauf. Bei frischen Pointern sind die beiden
Resultate wegen derselben Projektoren korreliert; man darf keine zwei
statistisch unabhängigen 3/8-Erfolgsfaktoren einsetzen.

Der unabhängige Prüfer führt die tatsächlichen Pointeramplituden mit,
testet die Endbra auf allen 256 Rechenbasisvektoren und erhält die zwei
Rohwahrscheinlichkeiten mit exakten Brüchen. Er importiert keine
Root-Rechenfunktionen.

## Verbleibende physische Ressourcen

Benötigt werden die erklärte trägerübergreifende ξ-Clifford-Schaltung
und ihr Inverses, der C3-Zugriff, adressierte Records auf zwei Kanten
(03 für Präparation und Ende, 01 für die beiden Zwischenrecords),
initialisierte und geeignet kohärent gehaltene beziehungsweise frische
Pointer, Reset nach Fehlversuchen, Born-Auslesung und die acht abschließenden
Rechenbasismessungen samt klassischer Akzeptanzlogik.

Bei Realisierung der Records durch den v1.5-Fest-Δ-Compiler bleiben
dessen Wedge-Kopplung, Q-Belegungszugriff, adressiertes t-an/aus,
Gatezeiten und Phasenkorrekturen Voraussetzung. Die neue Konstruktion
verringert die Zahl und Art der benötigten Makrooperationen; sie leitet
diese Kontrollen nicht aus P1/P2 her und entfernt keine realen
Mess-/Controller-/Resetfehler.

Eine vollständige erfolgreich präparierte Durchführung enthält vier
Recordmakros: Präparation, zwei Zwischenrecords, Endtest. Bei sofortigem
Abbruch einer erfolglosen Präparation beträgt der Mittelwert pro
gestartetem Versuch 1+(3/8)·3=17/8 Recordmakros. Zusätzliche Gates und
Resetzeiten sind darin nicht enthalten.

## Tatsächliche Zuordnung zu T1–T8

`docs/OPEN_PROBLEMS.md` erklärt weiterhin alle T1–T8 für offen und
verweist für die aktuellen Anforderungen ausdrücklich auf
`experiments/theory-contracts/RESEARCH_2026-09-09.md`, Abschnitt
**Current T1–T8 acceptance map**. Die dortigen konkreten Verpflichtungen
lauten, knapp ins Deutsche übertragen:

| Tor | Verpflichtung der tatsächlichen Quellenkarte |
|---|---|
| T1 | P1/P2, Dimensions- und Compilerentscheidungen ableiten; Eleganz von Auswahl trennen. |
| T2 | Die wirkliche halbgeladene, markierte E8-Seamalgebra samt Skalierungslimes konstruieren, mit Energie-, beiderseitiger Adjungierten- und Ladungs-/Cocyclekontrolle. |
| T3 | Einen TFPT-ausgewählten lokalen beziehungsweise quasi-lokalen unitären 3+1D-Parent für alle Sektoren herleiten. |
| T4 | Dessen chirales SM-Eich-/Weylmaß, Anomalien/Index und uniforme Spiegelentkopplung konstruieren. |
| T5 | Wechselwirkenden physikalischen Kontinuumslimes, Lorentzverhalten, Confinement/Clustering und erforderliche Streuung beweisen. |
| T6 | Alle drei Eichkopplungen und die vollständige Neutrinotextur samt Skala intern ableiten. |
| T7 | Masselosen quantisierten Spin zwei mit beiden Helizitäten und universeller Kopplung aus demselben Parent gewinnen. |
| T8 | Den physischen Anfangszustand auswählen und ein Quellenfunktional für sämtliche Auslesungen herleiten. |

Die Ein-Record-Konstruktion ist somit ein konkreter **bedingter
Operations- und Auslesefortschritt in Richtung T1/T8**. Sie schließt
weder die natürliche Auswahl des Anfangszustands noch ein gemeinsames
Quellenfunktional. Keine der übrigen sechs Verpflichtungen folgt aus
diesem endlichen Labor. Insbesondere bezeichnet T6 in dieser
Quellenkarte ausdrücklich Eichkopplungen und Neutrinos; ein
Kosmologie-Amplituden-/Tiltvergleich ist nicht allein die T6-Abnahme.

Die neuere Quellenkarte benennt zudem explizit den Half-Charge-Zielvektor
s=(1/2)⁸ mit Gewicht 1. Das stützt die vorherige Warnung, ihn nicht mit
dem halbierten gesamten Gluegenerator von Gewicht 1/4 zu verwechseln.
