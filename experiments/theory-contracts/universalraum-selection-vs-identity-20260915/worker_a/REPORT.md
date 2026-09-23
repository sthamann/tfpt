# Worker A: Selektionsregel, Selbstbeschreibung und Fixpunkt

15. September 2026 · **Exakte beschränkte Prüfung; keine primitive Physik gefunden.**

## Ergebnis

Eine präzise stärkere Recordbedingung eliminiert im vorab definierten,
operational unterscheidbaren Vergleichsraum zwei unabhängige Entscheidungen:
**16 Prozesse → 4 Prozesse, also 4 Bits → 2 Bits**. Sie fordert, dass ein
vorgegebener Ereigniswert unter der weiteren Dynamik unverändert bleibt.
Dieselbe Forderung lässt sich als Fixpunkt eines einzigen festen Operators
schreiben. Recordstabilität und dieser Fixpunkt sind daher dieselbe Bedingung,
nicht zwei unabhängige Begründungen.

Die im Auftrag naheliegende schwächere Forderung, dass ein historischer Record
erhalten bleibt, hat diese Wirkung nicht: **16 → 16**. Ein Archiv kann einen
vergangenen Wert unverändert speichern, obwohl der aktuelle Wert sich ändert.
Wer beides gleichsetzt, erhält eine scheinbare Auswahlwirkung aus einer
verschärften Voraussetzung.

Zwei verbleibende Prozesse haben dieselbe kleinste logische Dimension, dieselbe
Recordoperation und denselben Fixpunktoperator, aber verschiedene kohärente
Antworten. Vollständige zustandserhaltende Selbstbeschreibung eines beliebigen
unbekannten Quantenzustands ist dagegen innerhalb der gewöhnlichen
Quantentheorie unmöglich. Ein allgemeines Verbot jedes selbstbeschreibenden
Prozesses folgt daraus nicht.

## 1. Gegenstand und Abgrenzung

Der eingefügte Auftrag wurde vollständig gelesen. Die Vorarbeit
`universalraum-primitive-source-audit-20260915/RESULTS.md` und `EINSEITER.md`
wurde gelesen; ihre Gramrekonstruktion, Clocklog-Gegenmodelle und beiden
Viereralgebren werden hier nicht als neue Ergebnisse ausgegeben.

Es wird kein Universalraummodell vorgeschlagen. Die folgenden kleinen
Quantensysteme bilden einen **festen adversarialen Vergleichsraum**. Dass
Hilberträume, komplexe Phasen und Born-Auslesung darin bereits vorausgesetzt
sind, wird nicht als ihre Herleitung durch A–D gewertet. Sie dürfen als
Gegenmodelle gegen eine behauptete eindeutige Auswahl aus einer größeren
zulässigen Klasse dienen. Ihre Eignung als Beschreibung unserer Welt wird
nicht behauptet.

Keine RH-Mechanismen, Ledgeränderungen, Paperänderungen, Publikation oder
Commits. Die vorhandenen fremden Änderungen im Repository wurden nicht
bearbeitet. Keine MCP-Codegraph-Werkzeuge waren im Worker verfügbar; benötigt
wurden die vorgegebenen Berichte und ein neuer eigener Prüfer, keine weitere
Codeentdeckung.

## 2. Fester Vergleichsraum und Zählregel

Seien X,Y,Z die Pauli-Matrizen, Π₀=(I+Z)/2 und Π₁=(I−Z)/2. Für vier
unabhängige Bits a,b,c,d setze

    R_x = (√3 I − iX)/2 = exp(−iπX/6),
    R_y = (√3 I − iY)/2 = exp(−iπY/6),
    z_c = i   für c=0;   z_c = −1 für c=1,
    p_d = 1/2 für d=0;   p_d = 1/4 für d=1,
    U_abcd = diag(1,z_c) R_x^a R_y^b,
    |ψ_d⟩ = √p_d |0⟩ + √(1−p_d) |1⟩.

U hängt nicht von d ab, der Zustand nicht von a,b,c. Der Prozess P_abcd enthält
die markierte Ein-Schritt-Operation U, den Zustand und dasselbe
Experimentierwörterbuch. Erlaubt sind die festgelegten Pauli-Präparationen und
-Auslesungen sowie ihre Kompositionen. Eine physische Zeit oder Zeiteinheit
wird daraus nicht hergeleitet; n zählt nur Anwendungen derselben markierten
Operation.

**Operationales Äquivalenzkriterium:** Zwei Kandidaten gelten nur dann als
gleich, wenn sie unter demselben Wörterbuch alle Antworten liefern. Globale
Phasen des U sind unerheblich. Der Prüfer vergleicht deshalb die Zustandstabelle
tr(ρσ_j) und die vollständige Kanaltabelle

    T_ij = tr(σ_i U σ_j U†)/2,   σ_i ∈ {I,X,Y,Z}.

Alle 16 Kombinationen sind verschieden. Die vier Bits parametrisieren also
16 operational inequivalente Fälle, keine mehrfach gezählten Koordinaten.
N_free bezeichnet **nur diese vier binären Entscheidungen**. Die Wahl des
Vergleichsraums, des Ereigniswörterbuchs und der Testwerte selbst wird nicht
als eliminiert gezählt. Dies ist keine globale universumsweite Axiomzahl.

Warum die Rotationswinkel explizit feststehen: Ein erster Versuch mit π/2
statt π/3 hatte eine Kanalaliasierung. Die Kombinationen (a,b,c)=(1,0,1) und
(1,1,0) beschrieben denselben Kanal. Der Prüfer verwarf diese vermeintliche
Vier-Bit-Zählung. Der finale Vergleichsraum verwendet ausschließlich die
oben festgelegten π/3-Rotationen; keine Zahl aus dem verworfenen Raum wird
übernommen.

## 3. Hypothese A: geschlossene Komposition und Konsistenz

Präzisierung A: Zustände sind positiv normiert; die zugelassenen Operationen
und ihre endlichen Kompositionen bilden einen wohldefinierten Prozess.

Für jedes P_abcd ist U unitär; die Matrixkomposition ist assoziativ und
beliebige Worte sind wohldefiniert. Alle präparierten Zustände sind positiv
und normiert. Deshalb bestehen alle 16 Kandidaten dieselbe Regel.

    N_before = 4, N_after(A) = 4, ΔN(A) = 0.

Bereits P_0000 und P_0010 sind verschiedene Gegenprozesse: gleicher Zustand,
U=diag(1,i) beziehungsweise diag(1,−1). Ihre unten angegebenen kohärenten
Recordantworten unterscheiden sie. Die nachfolgend zusätzlich erfüllten
schwachen Record-, Fixpunkt- und Minimalitätsbedingungen beseitigen den
Unterschied ebenfalls nicht.

**Maximale Gültigkeit:** Komposition/Konsistenz sind notwendige
Wohldefiniertheitsbedingungen für diese Klasse. **Erste unbelegte Implikation:**
Wohldefiniertheit bestimme eine konkrete Phase oder einen konkreten Zustand.

## 4. Hypothese B besitzt drei verschiedene Lesarten

### B1: historischer Record und globale Kohärenz

Für alle 16 Kandidaten gilt dieselbe Recordisometrie

    W|0⟩ = |0⟩_S|0⟩_R,   W|1⟩ = |1⟩_S|1⟩_R.

Es ist eine isometrische Aufzeichnung eines Ereignislabels, keine zusätzliche
primitive Weltstruktur. Für |ψ_d⟩ entsteht

    |Ψ_d⟩ = √p_d |00⟩ + √(1−p_d) |11⟩.

Der Record ist intern: W†(I⊗Z)W=Z. Der globale Zustand bleibt rein und enthält
die relative Phase. Die Recordverteilung ist diag(p_d,1−p_d). Für jede spätere
Ein-Schritt-Operation U gilt

    tr_S[(U⊗I) |Ψ_d⟩⟨Ψ_d| (U†⊗I)] = diag(p_d,1−p_d),
    (U†⊗I)(I⊗Z)(U⊗I) = I⊗Z.

Dies gilt allgemein für lokale unitäre Entwicklung, nicht nur für die 16
Fälle. Der historische Record bleibt unverändert; der Systemzustand darf
sich ändern. Alle 16 Kandidaten bestehen B1.

    N_after(A+B1)=4, ΔN(B1|A)=0.

Ein präziser schwacher Fixpunkt ist darin schon enthalten: Für jeden solchen
Prozess ist die beobachtete Recordverteilung ein Fixpunkt der weiteren
Ausführung. Das sagt nichts über die Auswahl von U aus.

### B2: derselbe aktuelle Ereigniswert bleibt immer unverändert

Diese **stärkere** Variante fordert bei festgelegten Π₀,Π₁

    U†Π_j U = Π_j   für j=0,1.

Sie ist äquivalent zu [U,Z]=0. Da die linke Diagonalmatrix die Nullstellen der
Nichtdiagonale nicht verändert, genügt die Prüfung von R_x^a R_y^b. Bei
(a,b)=(1,0),(0,1),(1,1) beträgt der gemeinsame Betrag der Nebendiagonalen
jeweils 1/2, 1/2, √6/4. Er ist niemals null. Daher

    B2 ⇔ a=b=0.

Folglich bleiben genau P_0000, P_0001, P_0010, P_0011.

    N_before=4, N_after(B2)=2, ΔN(B2)=2.

Das ist eine wirkliche Reduktion zweier unabhängiger Mischungsentscheidungen
innerhalb dieses Vergleichsraums. Sie folgt aus einer einzigen
Operatorgleichung. Die gleiche Aussage lässt sich in U(2) modulo globaler
Phase kontinuierlich lesen: Stabilität eines vorgegebenen nichttrivialen
Projektorpaares reduziert die Dimension möglicher unitärer Kanäle von 3 auf 1.
Die vorab gewählte Ereignisrichtung und der Vorbereitungszustand sind dabei
nicht hergeleitet.

Für die vier Überlebenden gilt zudem

    (U⊗I) W = W U.

Die Recordabbildung ist mit der Dynamik verträglich: erst aufzeichnen und dann
entwickeln stimmt mit erst entwickeln und dann aufzeichnen überein. Dies ist
eine nichttriviale präzise Gemeinsamkeit von Komposition und Aufzeichnung.

**Kosten und Grenze:** Ein bestimmtes Z wurde vorgeschrieben. Fordert man
stattdessen nur die Existenz *irgendeiner* erhaltenen scharfen Zweierauslesung,
besitzt jede nichtskalare zweidimensionale Unitarität ihre Spektralprojektoren.
Alle acht unterschiedlichen U dieses Vergleichs bestehen dann die
Existenzforderung; die Prozesszahl bleibt 16. Die vorgegebene Ereignisrichtung
darf nicht nachträglich am jeweiligen U ausgewählt und anschließend als
physisch erzwungen ausgegeben werden.

Außerdem sind B1 und B2 nicht austauschbar. Persistente Archive benötigen
keine fortwährende Konstanz des archivierten aktuellen Wertes. Zwei entfernte
Entscheidungsbits aus B2 beweisen deshalb keine entsprechende Auswahlwirkung
der schwächeren ursprünglichen Recordforderung.

### B3: vollständige zustandserhaltende Quanten-Selbstbeschreibung

Präzisierung B3: Ein einziger physischer Kanal soll für jeden unbekannten
reinen Zustand |ψ⟩ den vollständigen Systemzustand exakt erhalten und zugleich
einen nichttrivial zustandsabhängigen, eigenständig zugänglichen Record
erzeugen. Man darf alle unzugänglichen Hilfssysteme in eine Isometriedilatation
einbeziehen. Weil der Systemrand rein bleibt, muss ihr Output die Form

    V|ψ⟩ = |ψ⟩ |r_ψ⟩

besitzen. Isometrie liefert für zwei Eingaben

    ⟨ψ|φ⟩ = ⟨ψ|φ⟩ ⟨r_ψ|r_φ⟩.

Für nichtorthogonale Eingaben folgt ⟨r_ψ|r_φ⟩=1: Die Records sind identisch.
Jede zwei reinen Zustände lassen sich über einen mit beiden nichtorthogonalen
Zustand verbinden; somit ist der Record auf dem gesamten reinen Zustandsraum
konstant. Es kann keine vollständige nichttriviale Selbstbeschreibung dieser
Art geben. Der Zweierfall |0⟩,|+⟩ genügt schon zum Widerlegen einer universellen
Kopiermaschine: Inputüberlappung 1/√2, hypothetische Klonüberlappung 1/2.

Dies ist eine Anwendung bekannter Quantengrenzen, kein neues No-go-Theorem.
Für gemischte Zustände können genau gemeinsam kommutierende Zustandsfamilien
durch denselben Kanal auf zwei Ränder ausgesendet werden; nichtkommutierende
Familien können dies nicht. Siehe [Barnum et al., PRL 76 (1996)
2818–2821](https://arxiv.org/abs/quant-ph/9511010). Für teilweise bekannte
Familien trennt die zustandserhaltende Operationsstruktur klassische,
nichtklassische und informationslose Komponenten; die klassische Information
ist auslesbar, die nichtklassische ist unter dieser Erhaltungsforderung
unzugänglich. Siehe [Koashi und Imoto, PRA 66 (2002)
022318](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.66.022318).

**Nicht überdehnen:** Ein konkreter bekannter Zustand, ein klassischer
Programmbeschreibungstext, ein Record einer kommutierenden Teilalgebra oder
globale Phasenerhaltung in verschränkten Korrelationen sind dadurch nicht
verboten. Ein einzelner klassischer Auslesewert beschreibt auch eine gemischte
Verteilung nicht vollständig. Das eingeschränkte klassische Broadcast ist
keine exakte Zustandstomographie einer einzelnen Probe. Ein Prozess kann
seine Erzeugungsregel als klassisches Programm enthalten, ohne beliebige
unbekannte Quantenmikrozustände auszulesen. Ein derartiges Programm muss aber
zunächst vorliegen; Selbstbeschreibung allein wählt seinen Inhalt nicht aus.

Ein allgemeines Prinzip außerhalb der Quantentheorie ist durch B3 nicht
widerlegt. Es kann nur nicht gleichzeitig B3 und die übliche Quantenklasse
aller unbekannten Eingaben unbeschränkt übernehmen.

### Quantitative Bedeutung von »kohärenter Record«

Die Zustände (|0⟩|r₀⟩ + |1⟩|r₁⟩)/√2 haben bei reellem Recordüberlapp
γ=⟨r₀|r₁⟩ lokale Interferenzsichtbarkeit V=|γ|. Für reine Recordzustände ist
ihre optimale binäre Unterscheidbarkeit D=√(1−|γ|²), daher

    V² + D² = 1.

Dies folgt hier direkt aus der partiellen Spur und den beiden Eigenwerten der
Differenz der Recorddichten. Der Prüfer kontrolliert γ=0,1/2,1 exakt.
Perfekt unterscheidbare Records haben V=0 im Systemrand; globale Kohärenz
kann trotzdem in gemeinsamen Messungen sichtbar bleiben. Die früheren
History-/Gramwarnungen entsprechen genau dieser Unterscheidung; sie werden
nicht als neuer Befund ausgegeben.

## 5. Hypothese C: Was steckt im Fixpunktoperator?

### C1: fester inhaltlicher Operator mit zwei verschiedenen Fixpunkten

Auf dem festen Vergleichsraum sei

    F_Z(ρ,U) = (ρ, ZUZ).

F_Z ist derselbe Operator für alle Kandidaten. Er ist auf der umgebenden
Klasse unitärer Prozesse definiert und muss den endlichen Testausschnitt
nicht außerhalb seiner Fixpunkte invariant lassen. Dann gilt

    P = F_Z(P) ⇔ [U,Z]=0 ⇔ B2.

Damit sind C1 und B2 zwei Schreibweisen genau derselben Restriktion. Sie
eliminieren zusammen zwei Bits, nicht vier. P_0000 und P_0010 sind zugleich
Fixpunkte desselben F_Z und erfüllen dieselbe Aufzeichnungs-/Kompositions-
Verträglichkeit. F_Z wurde jedoch aus dem gegebenen Recordprojektor
gebildet; der Operator ist keine von allen Vorgaben unabhängige Quelle.

**Kein vollständiger autonomer Ereignis→Record→Prozess-Selektor hergeleitet:**
Die feste Konjugation präzisiert Recordinvarianz, sie beweist nicht, dass
die physische Welt ihren vollständigen Generator aus einem Record erzeugt.
Diese erste fehlende Implikation darf nicht in der Schreibweise F versteckt
werden.

### C2: vollständige Beschreibung und Rekonstruktion

Für alle Kandidaten ist auch ein einziger beschreibender Loop möglich. E
bildet P auf die vollständige Zustandstabelle tr(ρσ_j) und Kanaltabelle T_ij
aus Abschnitt 2 ab. D rekonstruiert linear:

    ρ = (1/2) Σ_j tr(ρσ_j) σ_j,
    ℰ(σ_j) = Σ_i T_ij σ_i.

Dann ist F_rec=D∘E auf den operationalen Prozessen die Identität. Der
Prüfer kontrolliert alle 16 Fälle. Diese F ist nicht pro Kandidat angepasst;
ihre vollständigen Eingabewerte enthalten aber schon dessen Zustand und
Kanal. Sie entfernt keine der vier physischen Entscheidungen.

Die Tabellen sind mathematische Prozessbeschreibungen oder durch viele
präparierte Proben bestimmbare Statistiken. Sie sind **kein** Beweis, dass ein
einzelner Prozess seinen unbekannten Zustand störungsfrei selbst tomographiert.
Mit einem physischen Ein-Proben-Recordloop würde C2 wieder auf B3 treffen.

Allgemein gilt: Wenn E eine vollständige Beschreibung und D eine inverse
Rekonstruktion liefert, ist D∘E=id auf Äquivalenzklassen eine
**Darstellungsidentität**. Sie kann eine redundante zusätzliche Hilbert- oder
Operatorwahl beseitigen; sie erklärt nicht die Antwortwerte. Das ist mit der
bereits vorhandenen Gramrekonstruktion vereinbar und kein Ersatz für eine
Selektionsregel.

### C3: nackte Fixpunktform ohne angegebenes F

Für jede nichtleere Zielteilmenge S einer Menge X kann man mit einem s₀∈S
die Abbildung F_S(x)=x für x∈S, sonst F_S(x)=s₀, definieren. Sie ist
idempotent und hat genau S als Fixpunktmenge. Auch Idempotenz erzwingt daher
keine besondere Physik. Im viergliedrigen endlichen Universum prüft der
Checker alle 15 nichtleeren Fixpunktmengen.

Diese Metabeobachtung ersetzt das stärkere C1-Gegenbeispiel nicht. Ihr Punkt
ist die Annahmenbuchhaltung: Die gewünschte Auswahl kann vollständig in F
stehen. Ein Fixpunktsatz mit Eindeutigkeit würde ebenfalls zunächst nur das
gegebene F charakterisieren. Auswahl und Rechtfertigung von F blieben zu
beweisen.

## 6. Hypothese D: minimale nichttriviale Lösung

### Gleiche kleinste logische Dimension, unterschiedliches Verhalten

Betrachte die vier B2/C1-Fixpunkte. Ihr Recordzustand nach n Operationen ist

    |Ψ(n)⟩ = √p |00⟩ + √(1−p) z^n |11⟩.

Sowohl der Recordrand als auch der Systemrand sind für alle n gleich
diag(p,1−p). Die globale kohärente Auslesung ist dagegen

    ⟨X⊗X⟩_n = 2√(p(1−p)) Re(z^n).

Bei p=1/2 und n=1 liefern z=i und z=−1 die Antworten **0 und −1**.
Die kleinste Kanalperiode ist 4 beziehungsweise 2. Das sind invarianten
Unterschiede unter demselben markierten Schritt. Ein Basiswechsel kann sie
nicht entfernen. Das Wörterbuch während des Vergleichs zu ändern würde
eine andere Frage beantworten.

Alle vier Prozesse haben dieselbe zyklische logische Dimension 2, denn
|ψ⟩ und U|ψ⟩ sind linear unabhängig:

    det[|ψ⟩,U|ψ⟩] = √(p(1−p))(z−1) ≠ 0.

Dimension 1 kann zwei orthogonale Ereignisse und die beobachtete nichttriviale
Kanalentwicklung nicht darstellen. Die Recordcodierung W hat denselben
zweidimensionalen Bildraum span{|00⟩,|11⟩}; bei einer Darstellung als getrennt
auslesbare System- und Recordregister verwendet jeder dieselben zwei
zweidimensionalen Faktoren. Es wird keine universelle minimale Gesamtdimension
über alle möglichen Ontologien behauptet.

    N_before innerhalb Fixpunktklasse=2,
    N_after minimaler zyklischer Darstellung=2,
    ΔN(D|B2,C1)=0.

Die Wahl »minimale Kanalperiode« wäre ein anderes, zusätzlich festgelegtes
Kostenmaß. Im vorliegenden Viererraum ließe sie die beiden z=−1-Prozesse
übrig: noch immer verschiedene p. Über allgemeine kontinuierliche Phasen
gibt es ohne weitere Vorgabe keine ausgezeichnete kleinste positive
nichttriviale Winkelgröße.

### Minimale Beschreibungslänge

Eine längenbasierte Auswahl benötigt ein festes Alphabet, einen Decoder,
Kosten für das Versuchswörterbuch und eine Regel für Gleichstände. Für jede
endliche Kandidatenmenge kann ein Decoder umbezeichnet werden, sodass ein
beliebiger Kandidat das kürzeste Wort bekommt. Ein einfaches Zweierbeispiel:
Decoder A liest `0` als P_0000 und `10` als P_0010; Decoder B vertauscht die
Bedeutungen. Beide Codes sind präfixfrei; ihre abstrakte Größe ist gleich.
Die Präferenz kehrt sich um. Eine unabhängige Begründung des Decoders oder
eine robuste Vorhersage ist erforderlich.

Die Zwei-Entscheidungen-Reduktion durch B2 besteht unabhängig davon; es gibt
aber noch keinen gerechtfertigten Nenner für »maximale Reduktion pro
minimaler primitiver Beschreibungslänge«. Daher wird hier kein globaler
Gewinner nach einem willkürlich erfundenen Score ernannt.

## 7. Gemeinsame Bilanz ohne Doppelzählung

| Präzisierte Forderung | Kandidaten vorher → nachher | Unabhängige Bits vorher → nachher | Echte Aussage |
|---|---:|---:|---|
| A: positive Zustände und geschlossene unitäre Komposition | 16 → 16 | 4 → 4 | Hier keine Auswahl |
| B1: interner historischer Record, global kohärent | 16 → 16 | 4 → 4 | Archiv erhält Vergangenheit bei beliebigem U |
| B2: vorgegebenes aktuelles Z-Ereignis bleibt unverändert | 16 → 4 | 4 → 2 | Zwei Mischungsentscheidungen ausgeschlossen |
| C1: fester F_Z-Fixpunkt | 16 → 4 | 4 → 2 | Identisch zu B2; nicht addieren |
| C2: vollständige Beschreibung/Rekonstruktion | 16 → 16 | 4 → 4 | Repräsentationsidentität |
| D: minimale logische Dimension nach B2/C1 | 4 → 4 | 2 → 2 | Phase und Zustand bleiben verschieden |
| B3: vollständiger nichttrivialer Record bei Zustandserhaltung für alle unbekannten Eingaben | Kein zulässiger Kanal | kein sinnvoller Erfolgs-Δ | Mit gewöhnlicher Quantenklasse unverträglich |

Welche getrennten Forderungen fallen tatsächlich zusammen?

    Erhaltung der festgelegten aktuellen Ereignisse
    ⇔ Kommutieren mit ihrer Projektoralgebra
    ⇔ Verträglichkeit (U⊗I)W=WU
    ⇔ Fixpunkt unter F_Z.

Das ist eine konkrete Antwort auf die gewünschte Suche nach einer Forderung
mit mehreren Erscheinungsformen. Sie vereint diese vier Begriffe innerhalb
des ausgeschriebenen Vertrags, erzwingt aber nicht die Wahl des Vertrags.
Nichts daran wählt von selbst E₈, einen TFPT-Anker, Quantisierung, Raumzeit
oder beobachtete Wechselwirkungen. Die selektierten Prozesse besitzen sogar
über die Phasen hinaus eine frei bleibende Präparationswahl.

Eine weitere Verschärfung »alle nichtkommutierenden aktuellen Ereignisse
bleiben unverändert« beseitigt in M₂ die nichttriviale Dynamik: [U,X]=[U,Z]=0
impliziert U=λI. Die allgemeine Erhaltung aller Operatoren einer irreduziblen
vollen Matrixalgebra lässt nur deren skalares Kommutant. Das ist ein
bereichsgebundener Erhaltungssatz, kein Verbot von E₈ oder von Records unter
einer konkreten zeitlichen Entwicklung.

## 8. Status der gewünschten Endformel

Der Satz »Eine physikalische Realität existiert genau dann, wenn ihr
vollständiger Prozess **selbstkonsistent** ist« ist durch diese Prüfung nicht
bewiesen. Für **selbstbeschreibend**, **fixpunktförmig** und **minimal** gilt
dasselbe. Je nach Präzisierung sind die Bedingungen zu schwach, von
vorgegebenen Strukturen abhängig oder in ihrer stärksten Quantenfassung
unmöglich.

Die maximal belegte kurze Aussage lautet:

> Eine vorgegebene scharfe Ereignisauslesung bleibt genau dann während einer
> unitären Entwicklung unverändert, wenn diese Entwicklung mit ihren
> Projektoren kommutiert.

Sie ist ein exakter bedingter Selektionssatz und verbindet mehrere Begriffe.
Sie ist keine hinreichende Existenzbedingung für physikalische Realität.

**Erste unbelegte Kante der großen Kette:** Aus bloßer Selbstkonsistenz oder
der Existenz interner Records folgt weder die konkrete Ereignis-/Operations-
Algebra noch der gewählte Generator oder der Zustand. Unter der stärkeren
vorgegebenen Recordinvarianz bleiben Phase und Zustand explizit unbestimmt.

Ein TFPT-Test wurde in diesem Worker nicht angepasst und kein
zurückgehaltener TFPT-Befund als Vorhersage beansprucht. Ein Kandidat müsste
seine konkrete Regel samt erlaubten Daten vor einem solchen Test festlegen.
Diese lokale Zwei-Bit-Reduktion ist noch kein bestandener TFPT-Test und kein
Beleg für das verlangte universelle primitive Selektionsprinzip.

## 9. Reproduktion und Quellen

Der exakte Prüfer verwendet SymPy, ganze Zahlen, rationale Zahlen und
algebraische Wurzeln. Keine numerische Toleranz und kein Python-`assert`
entscheidet den Status. Beide Läufe bestanden und erzeugten byteidentische
JSON-Dateien:

    python3 -B checker.py --output normal.json
    python3 -B -OO checker.py --output optimized.json
    cmp normal.json optimized.json

Die Ausgaben enthalten Eingabe- und Prüferhashes. 341 geprüfte Bedingungen
sind Komponentenprüfungen, keine 341 unabhängigen Theoreme. Die allgemeinen
Beweise stehen im Bericht; endliche Matrixprüfungen werden nicht als Ersatz
für sie ausgegeben. Der Status `PASS_SCOPED_EXACT_AUDIT` bedeutet ausschließlich
Bestehen der angegebenen Gegenbeispiele und Zählungen.

Primärliteratur, am 15. September 2026 recherchiert:

- [Barnum, Caves, Fuchs, Jozsa, Schumacher: Noncommuting mixed states cannot
  be broadcast](https://arxiv.org/abs/quant-ph/9511010), PRL 76 (1996),
  2818–2821; allgemeine gemischte Broadcast-Grenze. Die einfache reine
  Zustandsgrenze wurde hier selbst vollständig hergeleitet.
- [Koashi, Imoto: Operations that do not disturb partially known quantum
  states](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.66.022318),
  PRA 66 (2002), 022318; Trennung klassisch zugänglicher und unter Erhaltung
  unzugänglicher Quanteninformation. Für den Bericht wurde der offizielle
  Abstract geprüft, nicht das gesamte 17-seitige Argument neu verifiziert.
- [Fuchs: Information Gain vs. State Disturbance in Quantum
  Theory](https://arxiv.org/abs/quant-ph/9605014), 1996; Informationsgewinn
  und Störung. Dient zur Einordnung, nicht als behauptete TFPT-Herleitung.
