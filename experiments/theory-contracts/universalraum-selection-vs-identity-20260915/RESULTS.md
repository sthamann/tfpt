# Fehlendes Selektionsgesetz oder übersehene Identität?

15. September 2026 · Konsolidierte Untersuchung des neuen Forschungsauftrags

**Ergebnis:** Beide Möglichkeiten sind an verschiedenen Stellen real. Innerhalb
der bereits gewählten affinen E₈-Randklasse waren Zustand und konforme
Entwicklung keine unabhängigen Wahlstellen. Die Wahl dieser Klasse als
physische Quelle folgt aber weder aus der bisherigen Compileridentifikation
noch aus Selbstbeschreibung, Fixpunktform oder Minimalität allein. Eine
universelle primitive Selektionsregel ist nicht gefunden. Kein T1–T8-Gate
wird geschlossen.

## 1. Was tatsächlich getan wurde

Der gesamte eingefügte Auftrag wurde gelesen und als Auftrag behandelt. Genau
zwei Forschungsagenten bearbeiteten die verlangten Gegenhypothesen:

- [Worker A](worker_a/REPORT.md): Selektionsprinzipien A–D, mit verschiedenen
  Prozessen unter demselben Kriterium und expliziter Entscheidungenzählung.
- [Worker B](worker_b/RESULTS.md): bereits vorhandene E₈-Identität, mit
  Eindeutigkeitsbeweis und Prüfung der wirklichen Quellenvoraussetzungen.

Der Hauptagent hat beide Berichte und Prüfer vollständig gelesen, die zentralen
Schlussfolgerungen nachgerechnet, die relevanten ursprünglichen Quellenstellen
geprüft und zusätzlich [kausale/Record-Gegenkontrollen](CAUSAL_RECORDS.md)
ausgeführt. Diese Kontrollen sind keine dritte Universalraum-Modellroute.
Alle drei Prüfer wurden durch [replay.py](replay.py) nochmals normal und
optimiert ausgeführt; das maschinenlesbare Ergebnis steht in [REPLAY.json](REPLAY.json).

Neu erzeugt wurde ausschließlich dieser Forschungsordner. Alte Eingaben,
Papers, Webseite und Ledger wurden nicht geändert; kein Commit/Push.

## 2. Eine notwendige Trennung im Forschungsziel

»Physisch zulässig« und »genau unsere Physik ausgewählt« sind unterschiedliche
Ziele. Eine Klasse zulässiger Prozesse darf mehrere Anfangszustände und
Bewegungen enthalten. Für den weitergehenden Anspruch müssen dagegen
Gesetzes-/Parameterwahl und gegebenenfalls Zustandswahl begründet werden.

Ein Korrelationskern mit vollständigen **zeitmarkierten** Operationen enthält
deren zeitliche Antworten bereits. Ein statischer Vakuum-Wortkern ohne
festgelegten Zeitgenerator tut das nicht. Die richtige Unterscheidung ist
nicht »Kernel enthält grundsätzlich keine Dynamik«, sondern »welche
Operationen und Zeitdaten wurden in ihm vorausgesetzt?«.

Auch ein Fixpunkt muss typisiert werden: Der Zustand als stationäre Lösung,
ein invariant bleibender Record, eine idempotente Rekonstruktion und eine
Auswahl des gesamten Prozessgesetzes sind vier verschiedene Behauptungen.

## 3. Strang A: Selbstbeschreibung wählt noch keine Naturgesetze

### 3.1 Exakte Auswahlbilanz in einem festgelegten Vergleichsraum

Worker A verwendet 16 operational verschiedene Zweiniveauprozesse. Vier
binäre Entscheidungen parametrisieren zwei Mischungen, eine relative
Entwicklungsphase und eine Präparation. Das Experimentierwörterbuch ist für
alle identisch. Unterschiedlichkeit wurde über vollständige Pauli-Zustands-
und Kanaltabellen geprüft; globale U-Phasen werden nicht doppelt gezählt.
Diese kleinen Systeme sind Gegenmodelle, keine vorgeschlagene Urphysik.

| Präzisierte Forderung | Prozesse vorher → nachher | unabhängige Bits vorher → nachher |
|---|---:|---:|
| Positive Zustände, geschlossene unitäre Komposition | 16 → 16 | 4 → 4 |
| Interner historischer Record mit global erhaltener Kohärenz | 16 → 16 | 4 → 4 |
| Vorgegebener **aktueller** Z-Ereigniswert bleibt invariant | 16 → 4 | 4 → 2 |
| Fixpunkt unter demselben festen F_Z(ρ,U)=(ρ,ZUZ) | 16 → 4 | 4 → 2; identisch zur vorherigen Zeile |
| Vollständige Beschreibung und inverse Rekonstruktion | 16 → 16 | 4 → 4 |
| Kleinste zyklische Dimension innerhalb der vier Fixpunkte | 4 → 4 | 2 → 2 |

Die echte Doppel-Elimination lautet in diesem festen Vertrag

    U†Π_jU=Π_j  ⇔  [U,Z]=0  ⇔  (U⊗I)W=WU  ⇔  U=ZUZ,

wobei W|j>=|j>_S|j>_R die vorgegebene Recordisometrie ist. Erhaltung,
Kompositionsverträglichkeit und Fixpunkt sind hier tatsächlich verschiedene
Schreibweisen **einer** Restriktion. Man darf ihre Auswahlwirkung nicht
mehrfach addieren.

### 3.2 Der entscheidende Begriffstausch

Ein dauerhaft lesbares Foto verlangt nicht, dass sich sein Gegenstand niemals
mehr bewegt. Mathematisch bleibt die Speicherhälfte R unter jeder weiteren
Entwicklung U_S⊗I_R unverändert. Das archivierte Ereignis ist stabil, auch
wenn der aktuelle Systemwert wechselt.

Die Forderung U†Π_jU=Π_j ist stärker: Nicht nur das Archiv, sondern der
**aktuelle** Wert bleibt gleich. Erst diese zusätzliche Erhaltungsforderung
entfernt die beiden Mischungsbits. Ferner wurde die Z-Richtung vorgegeben.
Wenn nur irgendeine erhaltene Zweierauslesung existieren soll, kann jede
Unitarität ihre eigenen Spektralprojektoren verwenden; keine der 16
Prozessmöglichkeiten wird dadurch ausgeschlossen.

### 3.3 Derselbe Fixpunkt und dieselbe minimale Größe, aber andere Antworten

Zwei Überlebende haben die gleiche Präparation, dieselbe Recordisometrie und
dieselbe minimale zyklische Dimension zwei:

    U_1=diag(1,i),     U_2=diag(1,−1),
    |Ψ(n)>= (|00>+z^n|11>)/sqrt(2).

Beide sind Fixpunkte desselben F_Z und besitzen identische Recordränder.
Trotzdem ist nach einem markierten Schritt

    <X⊗X>_1 = 0   beziehungsweise   −1.

Die Kanalperioden vier und zwei sind ebenfalls verschieden. Minimale Größe
und Fixpunktform wählen die Phase also nicht aus. Ein anderes Minimalitätsmaß
wie »kleinste Periode« wäre eine neue Auswahl; selbst hier bliebe noch die
Präparationswahl offen.

### 3.4 Starke Selbstbeschreibung hat eine Quanten-Grenze

Soll ein einziger physischer Vorgang jeden unbekannten reinen Zustand exakt
erhalten und dabei einen separaten informativen Record erzeugen, müsste

    V|ψ>=|ψ>|r_ψ>,
    <ψ|φ>=<ψ|φ><r_ψ|r_φ>

gelten. Für nichtorthogonale Eingaben ist der Record identisch; über verbindende
nichtorthogonale Zustände gilt dies auf dem ganzen reinen Zustandsraum.
Vollständige unbekannte Quantenmikrozustände lassen sich so nicht auslesen.
Das ist eine Anwendung der bekannten No-broadcast-/Nichtstörungsgrenze,
keine neue TFPT-Entdeckung. [Barnum et al.](https://arxiv.org/abs/quant-ph/9511010)

Ein klassisches Programm, ein Record einer kommutierenden Teilalgebra oder
globale Phaseninformation in verschränkten Korrelationen bleiben möglich.
Der Satz verbietet daher nicht jede Selbstreferenz. Er verhindert aber, eine
störungsfreie vollständige Selbstbeschreibung beliebiger Quantenzustände als
kostenlose zusätzliche Eigenschaft anzunehmen.

## 4. Strang B: Eine wirkliche vorhandene Identität

### 4.1 Aus einer kurzen ausgewählten Stromregel folgen alle Wortantworten

Fixiert man die volle markierte affine E₈-Stromalgebra, die kompakte
Adjungierung, Niveau eins und das normierte zyklische Vakuum mit

    [J_m^a,J_n^b]=i f^{ab}{}_c J_(m+n)^c + m δ_ab δ_(m+n,0),
    J_n^a Ω=0  für n≥0,

dann sind sämtliche Vakuum-Wortmomente durch Normalordnung bestimmt.
Kommutatoren verkürzen die Wörter; positive und Nullmoden verschwinden rechts
am Vakuum, negative links. Existenz und Positivität liefert die ausgewählte
integrable Gitterrealisierung. Der ganze Kern wird hier also tatsächlich aus
einer kurzen Regel berechnet, nicht frei als Tabelle eingesetzt.

Verlangt man außerdem geometrische Stromrotation

    [H,J_n^a]=−nJ_n^a,      HΩ=0,

folgt auf jedem erzeugten Wort seine Energie als Summe der Modenzahlen. Die
zyklische Erzeugung legt H eindeutig fest: H=L₀, identisch mit Sugawara.
Die Paarströme sind bereits aus dem W-Residuum rekonstruierbar. Zusätzliche
Paarbanken oder ein unabhängig angepasster kubischer Hamiltonoperator sind
für diese Randrealisierung nicht erforderlich.

Das ist die gesuchte Art von Identität **innerhalb eines vollständigen
Vertrags**. Der Beweis samt Domänen- und Selbstadjungiertheitsgrenze steht im
Worker-B-Bericht. Er ist eine Anwendung etablierter affiner Theorie, keine
neue allgemeine Rekonstruktionsmathematik.

### 4.2 Konkrete gemeinsame Antwort statt weiterer Zahlenähnlichkeit

Für zwei ausdrücklich angegebene Wurzeln aus dem vorhandenen 64er-Sektor mit
α·β=−1 und γ=α+β einer vorhandenen Paarwurzel sei

    u=J^α_−1 J^β_−1 Ω,
    v=J^β_−1 J^α_−1 Ω.

Die Gitter-Vertexformel liefert mit einem gemeinsamen Zeichen ε

    u=ε α(−1)e^γ,      v=−ε β(−1)e^γ.

Der Hauptagent hat diese Ableitung unabhängig aus der Erzeugungsfunktion
Y(e^α,z)e^β=ε z^(α·β) exp(Σ α(−n)z^n/n)e^γ nachgerechnet. Daraus folgt

    G_(u,v) = [[2,1],[1,2]],
    ||u−v||²=2,     ||u+v||²=6.

Das sind Quadrate unnormierter erzeugter Vektoren, keine Wahrscheinlichkeiten
größer eins. Die Zahlen verbinden Reihenfolge, Phasen und Paarantwort im
gleichen Zustand. Sie sind ein scharfer Test für eine behauptete Quellenkarte.
Sie sind **kein** unabhängiger empirischer Holdout: Sie folgen aus der bereits
gewählten E₈-VOA und ihrem Vakuum. Eine Quelle müsste diese Daten mit ihren
eigenen, vorher identifizierten Operationen erzeugen.

### 4.3 Warum der geometrische Vertrag wirklich gebraucht wird

Auf demselben E₈-Hilbertraum bleiben beide Generatoren möglich, wenn nur
Algebra, Vakuum, Positivität und diskrete Clock festgehalten werden:

    H_A=L₀,      H_B=L₀+4L₀(L₀−1).

Beide haben dasselbe eindeutige Vakuum und dieselbe erste positive Energie.
Außerdem gilt als volle Operatoridentität

    exp(−iπ H_A/2)=exp(−iπ H_B/2).

Auf Grad zwei sind die Energien aber zwei und zehn. Die Zeitantwort eines
normierten Grad-zwei-Stromzustands unterscheidet sich bei t=π/8 um ein
Minuszeichen. Eine Zeiteinheitenänderung erklärt das nicht, weil Grad eins
unverändert bleibt.

H_B ist ausdrücklich **keine** alternative lokal-konforme Netzentwicklung.
Das Gegenbeispiel beweist die Notwendigkeit der zusätzlichen geometrischen
Wirkungsbedingung, nicht das Scheitern des vollständigen konformen Vertrags.
Es ist kein vorgeschlagenes neues Universalraum-Modell.

## 5. Wo der tatsächliche TFPT-Quellenbeweis endet

Die vorhandene Theorie enthält die Zielklasse und viele ihrer Invarianten.
Das ist nicht bereits ihre physische Herkunft. Die ursprüngliche
`origin_theory.tex` benennt die Rohseam-Zustands- und Clock-/Alignmentreste.
Ältere Passagen verwenden teilweise eine zu starke Formulierung, als genüge
die gleiche topologische Phase für denselben vollständigen Randprozess.

Die spätere Quellenaudit-Datei `verification/v973_seam_route_narrowing.py`
trennt bereits ausdrücklich:

- gedeckte bilineare so(16)₁-Ströme und ihre Konvergenzaussagen;
- offene μ₄/GSO-Netzerweiterung;
- offene Twist-/Spinorfelder;
- die einseitige Randrealisierung;
- den Holomorphieselektor.

Der Hauptagent hat diese Stellen selbst gelesen. Die Prüfer dort machen
Literaturabdeckung als Buchführung überprüfbar; sie sind keine neuen Beweise
der fehlenden Erweiterung. Der aktuell dokumentierte T2-Rest verlangt
renormierte Halbladungsfelder zwischen Sektoren mit Quellenergie- und
Adjungierungskontrolle, anschließend E₈-Kanäle und Familie-/Clockzuordnung.

Auch E₈-Eindeutigkeit ist eine bedingte positive Aussage: Dong–Mason erzwingt
V_E8 in einer holomorphen, C₂-kofiniten VOA vom CFT-Typ bei c=8. Diese
Voraussetzungen ersetzen nicht ihre Herleitung aus der Quelle. Minimalität
der zentralen Ladung wäre ihrerseits eine Auswahlregel. Ein unmarkierter
Isomorphietyp legt außerdem noch keine markierte TFPT-Feldkarte fest.
[Dong–Mason, Theorem 1](https://arxiv.org/pdf/math/0203005)

## 6. Der angeforderte ΔN-Vergleich ohne Scheinerfolg

| Ebene | N_free vorher | N_free nachher | Bedeutung |
|---|---:|---:|---|
| Worker A, fester 16er-Raum, historischer Record | 4 Bits | 4 Bits | Keine Auswahlwirkung |
| Worker A, zusätzlich festgelegter aktueller Z-Wert invariant | 4 Bits | 2 Bits | Echte lokale Reduktion; Z-Wahl und stärkere Forderung werden nicht hergeleitet |
| Worker B, irrtümlich separat auszufüllende Felder ω,H_conf | 2 Felder | 0 Felder | Beschreibungsredundanz beseitigt |
| Worker B, wirkliche Moduli im bereits vollständigen affinen Vakuum-/Konformalvertrag | 0 | 0 | Diese beiden Größen waren innerhalb dieses Vertrags schon bestimmt |
| Primitive physische Entscheidungen von der Rohquelle bis TFPT/Realität | nicht vollständig parametrisiert | nicht vollständig parametrisiert | ΔN_phys≥2 ist nicht nachgewiesen |

Die beiden lokalen »Zweier« sind weder addierbar noch dieselbe Maßeinheit.
Eine Vier-Bit-Gegenmodellfamilie zählt nicht die Axiome des Universums.
Ein ausformulierter bereits vollständiger Vertrag darf nicht kostenlos als
eine primitive Annahme gezählt werden. Der user-seitig geforderte globale
Durchbruchstest ist dadurch **noch nicht erfüllt**.

## 7. Fingerabdrücke und zurückgehaltene Prüfungen

Die wenigen sinnvollen Gruppen sind:

1. **Gitter-/Darstellungsgruppe:** Rang acht, 240 Wurzeln, Dimension 248,
   Zerlegung, Theta-Reihe und daraus gebildeter Vakuumcharakter. Nach Auswahl
   der normierten E₈-Gitterrealisierung sind das abhängige Konsequenzen.
2. **Markierte Operationsgruppe:** Kozykelzeichen, W-Kanal, richtige
   Adjungierung und die obige Zwei-Reihenfolgen-Antwort. Sie prüft die
   Feldzuordnung, ist aber nach Vorgabe der vollen markierten VOA kein
   unabhängiger Auswahlbeweis für diese VOA.
3. **Physischer Quellen-/Readout-Anschluss:** die Quellzeit als dieselbe
   Stromrotation oder ein separat aus der Quelle bestimmtes Ward-Funktional
   mit seinen Normierungen. Hier wurde kein unabhängiger Ableitungs- oder
   Holdout-Test bestanden.

Es gab in dieser Runde keinen verblindeten oder neuen empirischen Holdout.
Die bekannten TFPT-Werte waren bereits sichtbar. Sie werden nicht nachträglich
zu ungesehenen Vorhersagen erklärt. Der neue Vierstrom-Test ist ein
vorab festlegbarer Akzeptanzwert für künftige Quellenkandidaten, nicht die
Behauptung eines bereits erzielten Out-of-sample-Erfolgs.

## 8. Die zusätzliche kausale Prüfung verändert zwei Gleichsetzungen

G_AB≠G_A⊗G_B kann aus einer korrelierten Anfangspräparation entstehen, ohne
dass während der beobachteten Entwicklung eine Wechselwirkung stattfindet.
Andererseits kann ein ausgewählter blinder Zustand eine vorhandene
Wechselwirkung nicht zeigen. Der belastbare Unterschied ist eine geänderte
Antwort auf einen kontrollierten lokalen Eingriff unter gleichem übrigen
Vertrag. Der vollständige Beweis und exakte Beispiele stehen in
[CAUSAL_RECORDS.md](CAUSAL_RECORDS.md).

Ebenso definiert fehlerfreie Rekonstruierbarkeit von Records eine
Informationsvorordnung, aber nicht automatisch physische Kausalität. Ein
späterer perfekter Record ist zu seinem früheren Original informationsgleich.
Die zwei Richtungen »X zufällig, Y kopiert X« und »Y zufällig, X kopiert Y«
haben identische passive Daten und verschiedene Interventionsantworten.

»Wechselwirkung = Nichtfaktorisierung« und »Zeit = Recordinformation« sind
deshalb ohne Typisierung keine vollständigen Identitäten.

## 9. Entscheidung und nächster tatsächlich begründeter Angriff

Die zwei Hypothesen sind nicht global exklusiv. Die **Identitätsseite** trägt
innerhalb der ausgewählten Randklasse: keine getrennte Erfindung von
Vakuum, Paarbank und konformem Hamiltonoperator. Die **Selektionsseite** bleibt
für den physisch realisierten Quellenvertrag offen. Schwache Selbstbeschreibung
löst sie nicht; starke unbekannte Zustandsselbstbeschreibung ist keine
zulässige kostenlose Quantenoperation.

Die Priorität liegt deshalb nicht auf einer weiteren unbestimmten Bedingung
»P ist selbstkonsistent«, sondern auf der vorhandenen **markierten
Quellenidentität** als falsifizierbarer Gegenhypothese: Liefert eine gemeinsame
ursprüngliche Feld-/Zustands-/Zeitzuordnung den ausgewählten Stromvertrag?

Ein Kandidat muss dabei aus eigener Vorschrift dieselben erzeugenden Felder,
Adjungierung und Quellzustandsantworten liefern. Die Vierstrom-Gram-Matrix
oben darf nicht als Kalibrierung hineingesteckt werden. Zusätzlich muss der
Zeitadapter [H_source,J_n]=−nJ_n tragen, statt nur einen diskreten Clock zu
treffen. Normalordnung und Sugawara würden dann alle Randantworten gemeinsam
übernehmen. Scheitert der Adapter, ist genau diese Identität ausgeschlossen;
es werden keine frei angepassten Reparaturfelder ergänzt.

Damit wird keine bereits vorhandene T2-Lücke als neue Entdeckung ausgegeben.
Die neue Untersuchung begründet, **warum** diese vorhandene Lücke der
richtige gemeinsame Prüfpunkt ist und warum der vorgeschlagene abstrakte
Record-Fixpunkt sie bislang nicht ersetzt.

Alle T1–T8 bleiben offen. Insbesondere: kein gemeinsamer physischer 3+1D-
Ursprung, kein vollständiges chirales Maß, kein dynamischer universell
gekoppelter Spin-2-Sektor. RH, Faktorisierung, P-vs-NP und Hylæan-Fähigkeiten
erhalten durch diese Runde keine Abschlusszertifikate.

Die verlangte Endformel »Eine physikalische Realität existiert genau dann,
wenn ihr vollständiger Prozess ___« lässt sich nicht seriös mit einem der
geprüften Begriffe schließen. **Beweisbar ist die bedingte Darstellungsstarrheit
des markierten E₈-Vakuum-/Konformalprozesses, nicht seine Auswahl als Realität.**

## 10. Verifikation

Die Worker-Berichte enthalten die allgemeinen Beweise und Primärquellen.
Der Hauptagent hat ihre ausführbaren Prüfer unabhängig erneut ausgeführt.
Der Replay verlangt erfolgreiche Exitcodes und byteidentische Ergebnisse
zwischen normalem und optimiertem Lauf; ausgewählte Quellen und alle drei
Prüfer bleiben vor/nach unverändert. Die Bedingungen sind Komponentenprüfungen,
keine Anzahl unabhängiger Theoreme. Kein statistischer oder physischer
Abschluss wird aus einem grünen Replay abgeleitet.

Der abgeschlossene Replay besteht aus **395 einmal gezählten exakten
Komponentenbedingungen**: 341 bei Worker A, 20 bei Worker B und 34 kausalen/
Record-Kontrollen. Alle sechs frischen Ausführungen waren erfolgreich; alle
drei Paare aus normalem und optimiertem Lauf lieferten byteidentische
Ergebnisdateien. Das bestätigt diese endlichen algebraischen Kontrollen,
nicht allein die allgemeinen analytischen Sätze oder eine vollständige TOE.

Die anfängliche Worker-A-Vergleichsfamilie wurde durch einen Gleichheitstest
als nicht injektiv erkannt; der verworfene Parametercount wird nicht
übernommen. Die finale Familie ist vollständig operational auf Verschiedenheit
geprüft. Kleine symbolische Prüferfehler in Worker B wurden berichtspflichtig
korrigiert; Zielwerte und Mathematik wurden nicht nachjustiert.
