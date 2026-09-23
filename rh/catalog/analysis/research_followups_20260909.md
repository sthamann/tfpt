# RH: zwei konkrete Anschlussaufgaben nach dem Quellenabgleich

9. September 2026. Forschungsverträge, **kein RH-Beweis**. Alle unten genannten
lokalen Resultate sind aus Originaldokumenten nachgetragen. Quellenprüfsummen
und erfolgreiche Rechenprotokolle ersetzen weder die Prüfung der analytischen
Voraussetzungen noch eine unabhängige Begutachtung. Maschinenlesbare, ausdrücklich
offene Voraussetzungen: `research_followups_20260909.json` im selben Ordner.

## Ausgangslage und Reihenfolge

Die neue Quelle ist der getrennte Codex-Arbeitsordner
`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2`.
Die dortigen Originale bleiben unverändert. Im Folgenden sind Pfade mit
`research/` und `work/` relativ zu diesem Ordner angegeben.

Zuerst muss ein unabhängiger Leser die tragenden Definitions-, Formbereichs-
und Fehlerübergänge prüfen. Danach ist der **neue Randanschluss** die konkrete
Konstruktionsaufgabe; die **Verhinderung einer ersten Nullstelle des
Spektralbodens** ist die globale analytische Aufgabe. Eine positive Antwort auf
die erste Aufgabe allein löst die zweite nicht. Mehr feste Fenster allein
ergeben keine Kontrolle über alle Fenster.

Die Karte dient zur Navigation. Ein ungerichteter Pfad über `REQUIRES`,
`BLOCKED_BY` oder `WOULD_CLOSE` ist **keine Implikationskette**. Die JSON-Verträge
verwenden deshalb ausdrücklich UND-verknüpfte Voraussetzungen; kein Graphweg,
Testzähler oder `alive`-Feld setzt einen Vertrag auf bestanden.

## A. Vollständiger Anschluss eines tatsächlich größeren Fensters

**Vorhandene Grundlage.** `research/rh_whole_odd_coercivity_20260909/PROOF.md`,
Abschnitte 1–4 und 7, berichtet am festen ursprünglichen Weil-Fenster
\(I=(-9/8,9/8)\), nur im ungeraden Sektor:

\[
q_{\rm old}(Wu+w)\geq\frac18\bigl(u^*Mu+\langle w,C_s w\rangle\bigr),
\quad q=Q_W-\mu\|\cdot\|^2,
\quad \mu=10^{-100},\quad C_s\geq(21/256-\mu)I.
\]

Hier ist \(P W=I\), \(P=P_{160}\) ungerade mit 80 Richtungen, und \(w\)
gehört zum **gesamten unendlichen** hohen Formraum. Die Fehlerlast wird für
diese ganze Form neu hergeleitet, nicht aus einer bloßen Schur-Matrix
übernommen. Die daraus berichtete \(L^2\)-Untergrenze \(3\cdot10^{-38}\)
ist weder der gemessene kleinste Eigenwert noch eine Aussage für den geraden
Sektor. Der symbolische Dilatationsschritt ist extrem klein und überschreitet
kein neues Primereignis.

**Jetzt fehlende Konstruktion.** Als ersten endlich festgelegten Versuch wählen
wir \(L_{\rm neu}=12/5\). Das Ziel liegt jenseits von \(\log 11\); die tatsächliche
Ereignisliste ist vor jedem Rechenlauf neu mit Intervallen zu bestätigen.
Erwartete aktive Primzahlpotenzen: \(2,3,4,5,7,8,9,11\). Das ist eine
Arbeitswahl, keine bereits zugelassene Parametererweiterung eines Programms.

1. Einen zulässigen gemeinsamen Formbereich und eine vollständige Zerlegung
   \(f_{\rm neu}=f_{\rm old}+v\) beweisen. Eine scharfe räumliche Abschneidung
   wird nicht ohne Bereichsbeweis verwendet. Die Einschränkung auf den alten
   Träger muss wirklich die alte Form mit derselben Normalisierung sein.
2. Die vollständige neue Form herleiten und implementieren:

   \[
   q_{\rm neu}(Wu+w+v)=q_{\rm old}(Wu+w)+d_{\rm neu}(v)
      +2\Re\{u^*B_{\rm low}v+\langle w,B_{\rm high}v\rangle\}.
   \]

   Alle Gamma-, Primzahlpotenz-, signierten Pol- und Verschiebungsterme sowie
   gegebenenfalls nichtorthogonale Normkreuzterme bleiben enthalten.
3. Für **jedes** \(v\) im vollständigen neuen Komplement nachweisen:

   \[
   d_{\rm neu}(v)\geq
       8(B_{\rm low}v)^*M^{-1}(B_{\rm low}v)
       +8\|B_{\rm high}v\|^2_{C_s^{-1}}.
   \]

   Der zweite Ausdruck darf eine Energie-Dualnorm sein; es wird nicht
   vorausgesetzt, dass die Kopplung ein gewöhnlicher beschränkter
   \(L^2\)-Operator ist. Zwei quadratische Ergänzungen liefern dann
   \(q_{\rm neu}\geq0\). Wichtig ist die anisotrope Gewichtung: nicht jede
   Kopplung muss mit dem schlechten globalen Faktor \(1/m\) bezahlt werden.

**Abnahme.** Vollständige Formel und Bereichsbeweis zuerst; danach vorab
eingefrorene neue Ereignispartition, alle niedrigen/hohen Kreuzprodukte,
analytischer unendlicher Rest, unverringerte Fehlerlast, Intervallprüfung
und Wiederholung mit unveränderten Zeugen. Mindestens eine zweite Ableitung
der neuen Kopplungen muss unabhängig von der bisherigen Matrixmontage sein.
Ein begrenzter vollständiger negativer Vergleichszeuge verwirft nur diesen
Vergleich, nicht RH. Unentschiedene Intervalle bleiben unentschieden.

**Vorgänger und tatsächlicher Unterschied.** r490 (`LOSSY_CONSTANT`) verlor
am ausgelassenen Galerkin-Außenrest. Hier müssen beide vollständigen alten
Kopplungen und das ganze neue Komplement vorkommen. r623
(`STRUCTURAL_MISMATCH`) verwirft eine andere semilokale Einbettung; er ist
keine Erlaubnis, einen neuen Randblock einfach anzusetzen. Fehlende
Bereichsverträglichkeit beendet den Versuch vor einer Positivitätsbehauptung.

**Kein globaler Schluss.** Selbst Erfolg bei \(12/5\) liefert zunächst nur
ein weiteres ungerades Fenster. Für RH fehlen eine nachweislich kofinale
Familie, die vollständige Testklassen-/Paritätsabdeckung und der präzise
Form-/Grenzübergang. Eine odd-only-Äquivalenz darf nur mit ihrem tatsächlich
bewiesenen Satz und allen Voraussetzungen benutzt werden.

## B. Eine erste Nullstelle des wirklichen Spektralbodens ausschließen

**Überlebende Frage.** Für den fest definierten vollständigen Weil-Operator
sei \(m(L)=\inf_{\|f\|=1}Q_L(f)\) in der jeweils erklärten Testklasse.
Eine hinreichende, noch nicht bewiesene Route wäre:

\[
m\in AC_{\rm loc},\qquad m'(L)\geq-c(L)m(L)\ \text{fast überall},
\qquad c\in L^1_{\rm loc},\quad c\geq0.
\]

Aus einem unabhängig zertifizierten \(m(L_0)>0\) folgt dann für endliches
\(L\geq L_0\):

\[
m(L)\geq m(L_0)\exp\!\left(-\int_{L_0}^{L}c(u)\,du\right)>0.
\]

Für einen echten Beweis muss die Schranke durch eine **hypothetische erste
Nullstelle** hindurch gültig und integrierbar sein. Die Definition
\(c=-m'/m\) im bereits positiven Bereich löst diese Aufgabe nicht.
Stetigkeit allein verhindert eine Nullstelle nicht. Ebenso wenig folgt
aus der erfolgreichen Berechnung endlich vieler Eigenvektoren, dass der
Minimierer existiert, eindeutig ist oder eine differenzierbare Kurve bildet.

**Der entscheidende Ausschluss.**
`work/relative_window_flow_20260907/relative_flow_proof.md` konstruiert
hochfrequente Zweipakete im tatsächlichen Prim-2-Kanal. Dabei wächst ihre
Formenergie nur logarithmisch, ihre Dilatationsableitung jedoch negativ
linear in der Frequenz. Damit scheitert die stärkere Ungleichung
\(\dot Q(f)\geq-CQ(f)-B\|f\|^2\) für alle Kernvektoren und beliebige feste
endliche \(C,B\). Gamma und signierte Pole sind im Argument enthalten.
Diese Pakete sind **keine nachgewiesenen Minimierer**. Genau das ist die
abweichende Voraussetzung des noch offenen Grundzustandsansatzes.

**Nächster beweisfähiger Teilschritt.** Aus der tatsächlichen
Euler-Lagrange-Gleichung, oder aus entsprechend kontrollierten minimierenden
Folgen, eine arithmetische Schätzung ihrer verschobenen Korrelationen
ableiten. Sie muss die negative Primkanal-Ableitung relativ zu \(m(L)\)
kontrollieren, einschließlich Gamma, signierten Polen, Bereichswechseln und
neu auftretenden Primzahlpotenzen. Ein endliches Niedrigfrequenzmodell darf
Minimierer-Lokalisierung nicht ersetzen. Zuerst ist festzustellen, welche
Regularität und kompakte Kontrolle die Originalform tatsächlich liefert.

**Abnahme.** Die Funktionsklasse, die positive Startschranke, die Regularität
und die nullstellenunabhängige integrierbare Kontrolle sind einzeln zu
beweisen. Eine Aussage nur für das alte ungerade Fenster bleibt genau darauf
beschränkt. Der globale Schluss ist erst nach der nachgewiesenen
Testklassenidentifikation zulässig. Fehlende Informationen werden als offene
Voraussetzungen geführt, nicht aus erfolgreicher numerischer Suche ergänzt.

## Was die anderen neuen Resultate leisten und was nicht

- Der arithmetische Relativvergleich bei \(L=9/4\) liefert laut Quelle
  \(9/32<\delta<289/1024\). Eine anschließende Gram-/Wurzeliteration nutzt
  die bereits bewiesene Vergleichspositivität; sie erzeugt sie nicht neu.
- Der TFPT-Seam-Korrekturraum löst eine endliche Sylvester-/Fixpunktaufgabe
  in einer erweiterten neundimensionalen Symmetrieklasse. Ihre physikalische
  Zulässigkeit und eine Identifikation mit der Weil-Form fehlen.
- Der kompakte Momentcompiler besitzt 1.225 positive endliche Tests, die
  auch eine komplexpolige Kontrolle besteht. Die nötige Aussage für alle
  Momente bleibt offen. Der Bernstein-Kandidat reproduziert gewöhnliche
  Momente nicht exakt.
- Die autonome ursprüngliche Momentkampagne hatte 1.048 Parameterkandidaten,
  nicht 1.048 unabhängige Mechanismen. Alle 15 endlichen Treffer scheiterten
  an der nachträglichen Restkanaldiagnose. Dieser Kill betrifft die erklärte
  Familie und die erklärte Diagnose, nicht alle Spektralansätze.

## Quellen und Prüfstatus

Die Hauptquellen sind direkt als Katalogeinträge und Graphkanten referenziert:
`rh_whole_odd_coercivity_20260909`, `rh_arithmetic_relative_correction_20260909`,
`rh_residual_response_20260908`, `rh_seam_gram_correction_20260909`,
`rh_zero_temperature_readout_20260908`, `rh_fermion_event_identity_20260908`,
`rh_autonomous_search_20260907` und `relative_window_flow_20260907`.
Ihre vollständigen Dateien und Prüfsummen stehen in `external_sources.json`.
Die Erfassung ist keine Wiederholung sämtlicher Experimente. Ungeprüfte
Gruppen bleiben `DISCOVERED_NOT_REVIEWED`; die Quellenprüfung eines
zusammenfassenden Eintrags ist keine unabhängige Prüfung aller Beweise.
