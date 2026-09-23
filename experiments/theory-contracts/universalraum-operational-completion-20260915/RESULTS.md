# Ist die Theorie selbst der Fixpunkt?

## Prüfung des operationalen Completion-Vorschlags

15. September 2026. Forschungsanalyse; keine Beförderung in Paper, Ledger
oder abgeschlossene TFPT-/RH-Behauptungen.

**Ergebnis:** Der Vorschlag enthält einen brauchbaren gemeinsamen
Konsistenzrahmen, aber noch keine eindeutig auswählende Regel. Exakte
operationale Äquivalenz und anziehende Skalenuniversalität müssen getrennt
werden. Für eine konservative, vollständig saturierte Completion ist der
Fixpunkt eine Abschlusseigenschaft. Für eine echte Skalenreduktion sind
mehrere verschiedene stabile Fixpunkte sogar unter derselben Regel möglich.

Neu sind hier die auf den Vorschlag zugeschnittenen Beweise und Kontrollen,
nicht der allgemeine Begriff der operationalen Theorie oder Renormierung.
Es wurde kein neuer Universalraum als physikalische Kandidatentheorie gebaut.
Die kleinen Gegenmodelle dienen ausschließlich der Prüfung von Implikationen.

## 1. Quellenabgleich

Der genannte [Kompass](/Users/stefanhamann/Documents/TFPT_Universalraum_Kompass_2026-09-15.pdf)
wurde textlich auf allen 16 Seiten gelesen; Seite 14 mit H1–H3 wurde zusätzlich
gerendert und visuell geprüft. Maßgeblich sind:

- S. 6: bedingter E₈-Randprozess und Clock-Gegenbeispiel;
- S. 9–10: volle Weil-Form und Ressourcen der Faktorisierung;
- S. 12: unverändert offene T1–T8;
- S. 13: gemeinsame Operation, zurückgehaltene Antwort, Apparatur und Skalierung;
- S. 14: H2 ist ausdrücklich eine **Hypothese über große Skalen**, nicht die
  Behauptung vollständiger operationaler Gleichheit sämtlicher Mikronetze.

Die vorherige eigene [Runde](../universalraum-selection-vs-identity-20260915/RESULTS.md)
wurde berücksichtigt. Eine kleine Versionsunterscheidung ist wesentlich:
Im Kompass steht H′=L₀+4L₀². Das besitzt dieselbe Vierteldrehung und dasselbe
Vakuum wie L₀, aber erste Lücke 5 statt 1. Die vorige Runde verwendete
H″=L₀+4L₀(L₀−1); **dieses** Gegenmodell erhält zusätzlich die erste Lücke.
Die beiden Formeln dürfen nicht mit identischen Zusatzbehauptungen vermischt werden.

Primärliteratur wurde zur Einordnung geprüft:

- [Abramsky–Coecke, A categorical semantics of quantum protocols](https://arxiv.org/abs/quant-ph/0402130):
  Komposition, Tensorstruktur und interne klassische Informationsflüsse.
- [Coecke–Pavlovic–Vicary, A new description of orthogonal bases](https://arxiv.org/abs/0810.0812):
  Basis-Recordstrukturen als spezielle kommutative Dagger-Frobenius-Strukturen.
- [Chiribella–D’Ariano–Perinotti, Informational derivation of Quantum Theory](https://arxiv.org/html/1011.6451):
  operative Äquivalenz in §II.2; zusätzliche Prinzipien in §III.
  Die Rekonstruktion verwendet fünf Axiome plus Purifikation. Der bloße
  operationale Quotient ist dort bereits Teil des Rahmens, nicht der ganze
  auswählende Inhalt.
- [Chiribella–D’Ariano–Perinotti, Probabilistic theories with purification](https://arxiv.org/abs/0908.1583):
  reversible Realisierung mit Umgebung unter dem Purifikationsprinzip.
- [Shor, Polynomial-Time Algorithms…](https://arxiv.org/abs/quant-ph/9508027):
  Quanten-Perioden-/Faktorisierungsroute, keine P=NP-Folgerung.

Das ist eine Prüfung ausgewählter relevanter Literaturstellen, kein vollständiges
Refereeing dieser Arbeiten.

## 2. Zuerst den Typ von P festlegen

Drei unterschiedliche Objekte werden im Vorschlag teilweise mit P bezeichnet:

1. **Prozesskalkül / Theorie:** Welche Systeme, Kompositionen, Zustände,
   Instrumente und Wahrscheinlichkeiten sind zulässig?
2. **Markierte Ausführung:** Welche konkrete Präparation, Dynamik und
   Recordbelegung liegen vor?
3. **Universalitätsklasse:** Welche Unterschiede verschwinden in einem
   festgelegten Skalengrenzwert und für welche Tests?

Ein Kalkül kann nach einer Ausführung derselbe bleiben, obwohl der Recordzustand
anders ist. Eine Universalitätsklasse kann dieselbe bleiben, obwohl ein genügend
feiner Versuch zwei mikroskopische Ausführungen unterscheidet. Eine Gleichung
zwischen diesen Ebenen benötigt Abbildungen; dass alle drei »Prozess« heißen,
ist keine solche Abbildung.

Auch Pr(C|P) ist nicht allein aus den Zeichen ◦, ⊗ und † definiert. Man braucht
typisierte Ein-/Ausgänge, zulässige Tests und deren positive normalisierte
Bewertung. Diese Bewertung könnte Gegenstand einer Herleitung sein; sie darf
nicht gleichzeitig als bereits gegebene Definition und als neue Folgerung zählen.

### Adjunktion und Normalisierung

Die Hilbert-Schmidt-Adjungierte einer CP-Abbildung ist CP, aber die Adjungierte
eines spurtreuen Kanals ist im Allgemeinen nicht wieder spurtreu. Eine
dagger-abgeschlossene Ereignisalgebra und die normalisierten physikalischen
Tests sind daher zu unterscheiden. Schon Präparation und Effekt besitzen
verschiedene Ein-/Ausgangstypen. Der Prüfer verwendet eine algebraische
Record-Counit (1,1) ausdrücklich **nicht** als physikalischen Löschkanal.

## 3. Was der exakte operationale Quotient tatsächlich leistet

Fixiere eine gemeinsame Klasse K vollständig spezifizierter, typverträglicher
interner Testkontexte. Dazu gehören die beanspruchten Fortsetzungen, Referenzen
und Record-Auslesungen. Definiere

    P ~_K Q  genau dann, wenn  Pr(C|P)=Pr(C|Q) für alle C∈K.

Für unter Einsetzen abgeschlossene Kontextklassen ist diese Relation eine
Kongruenz für sequentielle und parallele Komposition: Ein unterscheidender
Kontext nach einer Komposition wäre durch Einsetzen bereits ein unterscheidender
Kontext davor. Der Quotient ist damit eine gute Methode, überflüssige
Realisierungsdetails zu entfernen.

**Aber:** Die zulässigen Kontexte sind tragende Daten. Hat eine Erweiterung
plötzlich einen neuen phasensensitiven Kontext, kann sie vorher gleichgesetzte
Objekte unterscheiden. Dann war der alte Quotient nur relativ zur alten Klasse
gültig. Die Formulierung »was intern möglich ist« darf diese Änderung nicht
verbergen.

Im Zweiniveaubeispiel haben |+〉 und |−〉 dieselben Z-Häufigkeiten. Die zulässige
Fortsetzung »Hadamard, danach Z lesen« unterscheidet sie mit Wahrscheinlichkeiten
1 und 0. Ein Quotient nur der aktuellen Records wäre falsch; der vollständige
Fortsetzungsquotient behält den Unterschied. Genau das verlangt auch der
Schattenzeuge im Kompass.

## 4. Satz: konservative Completion ist noch kein physikalischer Selektor

**Voraussetzungen.** C ist die saturierte Schließung einer typisierten
Operationspräsentation unter vorgegebenen Kompositions-, Tensor-, Dagger- und
zulässigen Recordregeln. »Saturiert« bedeutet: auch die neu entstandenen Terme
werden erneut geschlossen. Alle Regeln sind semantisch konservativ; alte
Kontextwahrscheinlichkeiten ändern sich nicht. Q ist der exakte Quotient für
diese abgeschlossenen Kontexte, mit wohldefinierten Operationen auf Klassen.

**Aussage.** Für R_cl=Q∘C gilt bis auf operationale Isomorphie

    R_cl(R_cl(P)) ≃ R_cl(P).

**Beweis.** Jede neu zusammengesetzte Operation aus bereits abgeschlossenen
Termen lässt sich in deren ursprüngliche Ausdrücke einsetzen. Wegen Saturierung
liegt der eingesetzte Term schon in C(P). Alle Record- und Daggerregeln sind dort
ebenfalls geschlossen. Q identifiziert genau semantisch gleiche Terme, und
die Kongruenzeigenschaft macht Komposition auf den Klassen unabhängig von der
gewählten Darstellung. Erneute Schließung fügt daher keine neue operationale
Klasse hinzu; erneutes Quotientieren entfernt keine weitere. □

**Wichtige Einschränkung:** Ein einmaliges CompositionClosure gefolgt von einem
einmaligen RecordClosure muss noch nicht saturiert sein. Zwei Schließungen
müssen nicht kommutieren. Der Satz setzt entweder vollständige Saturierung
oder deren Nachweis voraus. Er behauptet nicht, jede beliebige Rekursion R sei
idempotent.

**Folgerung.** Jede bereits vollständige zulässige Theorie ist ein Fixpunkt.
Das kann eine starke Prüfung einer unvollständigen Präsentation sein, wählt
aber noch nicht unter verschiedenen vollständigen Theorien oder markierten
physikalischen Gesetzen aus.

Bei einer konservativen Erweiterung gilt außerdem für jeden alten Kontext C

    Pr(C|R_cl(P)) = Pr(C|P).

Unterscheiden sich zwei markierte Ausgangspräparationen etwa um 5/12 in einer
zulässigen Antwort, bleibt dieser Unterschied erhalten. Er darf nicht durch
einen exakten Quotienten verschwinden.

### Stabilität eines idempotenten Abschlusses

Auf dem Raum vollständiger operationaler Klassen wirkt R_cl als Identität.
Gibt es beliebig nahe verschiedene Fixpunkte P_θ in einer Hausdorff-Topologie,
kann keiner davon alle diese Nachbarn anziehen: R_clⁿ(P_θ)=P_θ für jedes n.
Ein Anschluss von »stabil« im Sinne bloßer Lyapunov-Stabilität ändert daran nichts;
Neutralität ist keine Attraktion. Eine Projektion kann außerhalb ihrer Fixmenge
anziehend wirken, aber wählt damit nicht automatisch einen Punkt innerhalb
einer kontinuierlichen Fixmenge aus.

## 5. Nichttriviale geschlossene Quantenstruktur erfordert noch kein E₈

Als Konsistenzgegenmodell genügt der übliche endliche Qubit-Prozesskalkül mit
seinen zusammengesetzten Systemen, CP-Ereignissen und normalisierten Tests.
Er enthält echte Phase, nichtkommutierende Operationen, reversible Wechselwirkung
und interne Register. Dies ist ein bekanntes mathematisches Gegenmodell, keine
neu postulierte TFPT-Architektur und keine Herleitung der Quantenmechanik.

Die kohärente Recordisometrie

    C|0〉=|00〉, C|1〉=|11〉

entsteht aus einem internen CNOT mit bereitgestelltem |0〉-Register. Sie kopiert
die gewählten Basisdaten, nicht einen beliebigen unbekannten Quantenzustand.
Zusammensetzung, Adjunktion und weitere interne Register bleiben im Kalkül.
Die Präparation des Registers ist als Ressource benannt, nicht autonom bewiesen.

Schon der kleinste nichttriviale komplexe Matrixblock ist M₂(C). Seine unitalen
*-Automorphismen sind innere Konjugationen modulo globale Phase, also PU(2).
Mit ausgezeichneter Recordbasis verbleibt eine Untergruppe. Daraus folgt weder
D₅⊕A₃ noch ein ausgezeichnetes E₈. Größere zusammengesetzte Systeme können
weitere Darstellungen enthalten; »enthalten können« ist nicht »als fundamentale
Signatur erzwingen«.

**Reichweite:** Das widerlegt die E₈-Folgerung aus dem bloßen algebraischen
Abschluss plus Records. Es ist kein Gegenbeweis gegen einen erst noch konkret
definierten, inhaltlich stärkeren Skalenoperator.

## 6. Echte Skalenreduktion: eine Regel, zwei stabile Zufallsprozesse

Hier wird die stärkere Attraktionsforderung wirklich geprüft, nicht durch
Neutralität ersetzt.

Betrachte unabhängige Bits mit Pr(1)=p. Ein Block aus drei Bits besitzt k Einsen.
Die **ein für alle Mal festgelegte** stochastische Blockoperation gibt eine Eins
mit der Wahrscheinlichkeit

    b₀=1/12, b₁=5/24, b₂=29/36, b₃=7/8

aus. Alle Einträge liegen in [0,1]; die beiden Ausgänge summieren sich jeweils
zu eins. Mit unabhängigen Hilfsregistern auf disjunkten Blöcken erhält man
wieder eine unabhängige Bitquelle. Auf ihrem Parameter wirkt exakt

    f(p) = Σ binom(3,k) p^k(1−p)^(3−k) b_k
         = p − (p−1/4)(p−1/2)(p−2/3).

**Dies ist kein TFPT-Kandidat.** Die Brüche werden offen als Gegenprobe eingesetzt,
um die behauptete Implikation »Stabilität ⇒ eindeutige Klasse« zu testen.
Die Formel ist auch kein exakter Quotient gegenüber allen mikroskopischen
Tests; sie ist eine echte, informationsverlierende Blockoperation.

Fixpunkte und Ableitungen:

| p* | f′(p*) | Ergebnis |
|---|---:|---|
| 1/4 | 43/48 | anziehend |
| 1/2 | 25/24 | abstoßend |
| 2/3 | 67/72 | anziehend |

Beide anziehenden Quellen sind nichtdeterministisch. Ihre Wahrscheinlichkeiten
sind weder gleich noch komplementär: bloßes Umbenennen von 0 und 1 identifiziert
sie nicht. Beide besitzen dieselbe elementare Zustandsraumgröße.

### Beweis der gesamten Einzugsgebiete

f′ ist eine konkave quadratische Funktion, an 0 und 1 strikt positiv, also auf
[0,1] positiv. Ferner f(0)=1/12, f(1)=7/8; f bildet [0,1] in sich ab.
Die Faktorisierung von f(p)−p zeigt:

- unter 1/4 wächst p monoton, ohne 1/4 zu überschreiten;
- zwischen 1/4 und 1/2 fällt p monoton, ohne 1/4 zu unterschreiten;
- zwischen 1/2 und 2/3 wächst p monoton, ohne 2/3 zu überschreiten;
- oberhalb 2/3 fällt p monoton, ohne 2/3 zu unterschreiten.

Die Grenzen müssen Fixpunkte sein. Somit konvergiert jedes p<1/2 gegen 1/4
und jedes p>1/2 gegen 2/3. p=1/2 bleibt exakt stehen. Das ist ein analytischer
Beweis über die ganzen Intervalle, nicht bloß eine Stichprobe.

**Ergebnis:** Ein konkret definierter Skalenoperator kann mehrere stabile,
nichttriviale Prozessklassen haben. Einzigkeit und Einzugsgebiet müssen eigens
bewiesen werden. Dass »die Natur den stabilen Fixpunkt wählt« folgt nicht aus
dem Wort stabil.

## 7. Der noch wichtigere Unterschied: alle Tests versus feste endliche Tests

Die vorangehende Attraktion gilt in der Topologie aller **jeweils festgehaltenen
endlichen** Ausgangsversuche. Für m Ausgänge ist die totale Variation zwischen
den Bernoulli-Produktmaßen höchstens m|p−q|. Daraus folgt für jedes feste m
Konvergenz der Antworten, wenn p gegen q geht.

Sie gilt nicht gleichmäßig über beliebig große m. Für p≠q kann man beide
Quellen durch ausreichend viele unabhängige Wiederholungen nahezu sicher
unterscheiden. Mit δ=|p−q| und einem Test der Stichprobenhäufigkeit gegen den
Mittelpunkt liefert bereits Chebyshev

    TV(Bern(p)^⊗m, Bern(q)^⊗m) ≥ 1 − 2/(m δ²).

Also ist das Supremum über alle endlichen m gleich 1. Die topologische und
operative Aussage lautet deshalb

    für jedes feste C: Grenzwert der Antwortdifferenz = 0

und nicht

    Grenzwert des Supremums über alle C der Antwortdifferenz = 0.

**Das ist für den Vorschlag zentral:** Der exakte Quotient »kein interner
Versuch kann unterscheiden« identifiziert nicht automatisch zwei Quellen
derselben großen-Skalen-Grenzklasse. Eine Theorie der Universalität muss sagen,
welche Auflösung, Versuchsdauer und Ressourcen beim Grenzübergang festgehalten
oder mit skaliert werden. Das ist keine technische Nebensache.

## 8. Kausalität, Geometrie, Chiralität und Gravitation

### Kausalität

Kontrollierbare Recordabhängigkeit ist eine bessere Anforderung als passive
Korrelation. Aber man muss zulässige Eingriffe, kompatible Randbedingungen,
Feedback und Referenzen definieren. Azyklizität und die Verträglichkeit mit
einer partiellen Ereignisordnung sind zu beweisen, nicht aus dem Wort
Informationsfluss zu übernehmen. Eine reversible kausale Ordnung bestimmt
außerdem noch keinen eindeutigen thermodynamischen Zeitpfeil oder Anfangszustand.

### Geometrie

Aus einem positiven Gramkern entsteht auf seinem Quotienten die Hilbertdistanz
||[u]−[v]||. Das ist ein belastbarer mathematischer Anschluss. Es macht aber
weder die Wortlabels automatisch zu Raumorten noch diese Distanz zu einer
physikalischen Lorentzmetrik.

Eine beliebige Funktion maximaler Korrelation ist nicht automatisch eine
Metrik. Beispiel: A=X, B=(X,Y), C=Y für unabhängige faire Bits. Die maximale
klassische Korrelation ist für A,B und B,C jeweils 1, für A,C aber 0.
Eine Vorschrift F mit F(1)=0<F(0) würde die Dreiecksungleichung verletzen.
Ein Wegabstand aus einer bereits gegebenen lokalen Graphstruktur wäre möglich,
setzt dann aber eben diese Struktur und eine operational passende Gewichtung voraus.

### Chiralität

Ein exakter Quotient entfernt nur ununterscheidbare Unterschiede. Wenn ein
zulässiger Strom oder ein Eingriff einen Spiegelkanal nachweist, darf Q ihn
nicht einfach löschen. Die Kanäle im Grenzwert unzugänglich zu machen erfordert
die dynamische Entkopplung, die T4 ohnehin verlangt. Geschlossener Kalkül allein
erzwingt keine Paritätsverletzung und keinen Index einer chiralen Feldtheorie.

### Gravitation

Zustandsabhängige Korrelationen können eine rekonstruierte Geometrie ändern.
Daraus allein folgen kein masseloser Spin-2-Pol, keine zwei Helizitäten, keine
universelle Kopplung und keine Einstein-Dynamik. Diese Auslesungen müssten aus
derselben kontrollierten Skalierungsfolge berechnet werden.

## 9. Arithmetik: was der neue Atom-Begriff verbessert und was er voraussetzt

**Die Unterscheidung ist sinnvoll:** Ein primitives zyklisches Wort ist nicht
dasselbe wie ein irreduzibles Element eines Kompositionsmonoids. Im freien
kommutativen Monoid auf a,b ist ab zusammengesetzt. Dadurch verschwindet die
konkrete Verwechslung, ab müsse einen weiteren »Primzahlgenerator« darstellen.
Auch »atomare Transformation« in der operationalen Quantenliteratur bedeutet
häufig Unzerlegbarkeit unter Verfeinerung/Coarse-graining, **nicht** unter
sequentieller Komposition. In der oben zitierten Informationsrekonstruktion
wird gerade die Komposition zweier solcher atomarer Transformationen wieder
atomar. Dieser Begriff darf nicht mit einem multiplikativen Primatom verwechselt werden.

Aber die allgemeine Operationsalgebra besitzt nicht notwendig solche Atome:

- In einer Gruppe unitärer Operationen sind alle Operationen Einheiten. Jede
  endlichdimensionale unitäre Matrix hat zudem unitäre Wurzeln. Ohne
  eingeschränkten elementaren Operationssatz gibt es keine ausgezeichneten
  unteilbaren Zeitschritte.
- Selbst irreversible Kanäle können beliebig weiter teilbar sein. Für
  K_a = 1/2 [[1+a,1−a],[1−a,1+a]], 0<a<1, gilt
  K_a K_b=K_ab und K_a=K_sqrt(a)². Beide Faktoren sind nichttrivial.

Um gewöhnliche Primzahlen zu erhalten, braucht es daher unter anderem eine
begründete diskrete multiplikative Teilstruktur, ihren Atom-/Faktorisierungssatz
und eine arithmetisch normierte Längenabbildung. Ein freies kommutatives Monoid
mit willkürlichen Generatorgewichten hat ebenfalls Eulerprodukte:

    Z(s)=∏_a (1−exp(−s ℓ_a))^(−1).

Seine logarithmische Ableitung erzeugt Vielfache kℓ_a. Das erzwingt weder
ℓ_a=log p noch das gewöhnliche ζ. Bei ℓ_a=log p ist die Primzahlinformation
bereits über die Gewichte eingeführt, sofern deren Herkunft nicht eigens
bewiesen wird.

### RH-Grenze und vorhandene Vorarbeiten

Die installierten Forschungsgraph-Skills wurden angewendet. Die aktuelle
RH-Indexprüfung stoppt bei `SOURCE_UNAVAILABLE` für
`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`.
Der Faktorisierungsgraph liegt am konfigurierten Ort ebenfalls nicht mehr vor.
Es wurden keine Pins erneuert und keine fehlenden Quellen fingiert. Stattdessen
wurden erreichbare Originalstellen und Archivberichte gelesen.

`rh/catalog/analysis/prime_story.md` und `event_log_function.md` führen diese
Quellenlücke schon als fehlende autonome Skalen-/Primzahlwirkung. Ausgewählte
Stellen von `rh/lean/RH/Source.lean` unterscheiden explizite Primzahlpotenzdaten,
ihre Rationalapproximation und die noch offenen analytischen Brücken.

Besonders relevant ist **r607**, Familie `PRIME_EVENT_LOG_DECODING`,
`WORLD_BLIND`, `KILLED(RECOORDINATIZATION)`. Das erhaltene Original
`experiments/tfpt-discovery/event_lindblad_twokey_probe.py` beschreibt die
versuchte Lindblad-/Weil-Identifikation: CP-Positivität wird dort gerade dann
erreicht, wenn die zu beweisende Fensterpositivität eingesetzt wird. Dieser
Befund wird hier als Quellenbefund verwendet, **nicht frisch nachgespielt**.
Er ist kein generelles Verbot einer neuen arithmetisch spezifischen Konstruktion.

Für den aktuellen Vorschlag bleibt deshalb dieselbe präzise Pflicht:

    Q_Weil(f)=||D f||²

mit unabhängig konstruiertem D, richtigen Vorzeichen und Gewichten,
archimedischen und Randtermen sowie voller benötigter Testabdeckung und
kontrollierten Grenzübergängen. Die Positivität einer beliebigen Prozess-Gramform
liefert diese Identität nicht. Diese Runde baut keinen neuen RH-Kandidaten und
registriert deshalb keinen erfundenen globalen Operator im Forschungsgraphen.

### Faktorisierung und Komplexität

Atomare Zerlegbarkeit ist keine Laufzeitschranke. Präparation, Implementierung,
Auslese und Wiederholung sind in der Bitlänge zu bezahlen. Auch eine effiziente
Realisierung der bekannten Quanten-Periodenbestimmung wäre noch kein P=NP-Beweis.
Das postulierte Finden eines stabilen Fixpunkts braucht ebenfalls einen
algorithmischen Zugangs- und Konvergenznachweis; eine abstrakte Existenz macht
einen Fixpunkt nicht kostenlos berechenbar.

## 10. Was sich über G korrigieren lässt

Ein bloßer statischer Gramkern ohne operationales Produkt-, Zeit- und
Kontextwörterbuch bestimmt die Entwicklung nicht. Das bleibt richtig.

Die stärkere Behauptung »aus einer vollständigen Prozessdarstellung kann man
den Prozess grundsätzlich nicht zurückgewinnen« wäre aber falsch formuliert:
Hat man alle Kontextantworten samt Einsetzen und Komposition, ist der Prozess
bis zur **so definierten operationalen Äquivalenz** gerade bestimmt. Es können
mehrere interne Realisierungen übrig bleiben; diese hat Q absichtlich gleichgesetzt.

Es fehlen also nicht zwangsläufig Informationen *hinter* einer wirklich
vollständigen operationalen Darstellung. Es fehlen die unabhängig hergeleitete
Antwortfunktion und der Nachweis, dass sie aus der gemeinsamen Quelle entsteht.
Rekonstruktion und physische Auswahl bleiben verschiedene Fragen.

## 11. Der tragfähige gemeinsame Auftrag

Nicht alle Tore durch Umbenennen zu einem gelösten Fixpunktsatz machen.
Stattdessen muss ein konkreter Kandidat gleichzeitig liefern:

1. **Konservative Darstellung:** Derselbe vollständige Prozess besitzt
   kompatible Feld-, Zustands-, Record- und Zeitdarstellungen. Q darf dabei
   keine tatsächlich messbare Differenz entfernen.
2. **Begründete Skalenabbildung B:** Welche Eingriffe und Records bleiben auf
   welcher Skala verfügbar? Wie entstehen B und ihre Kosten aus der Quelle?
3. **Universalität mit Quantoren:** Für welche anfänglichen Variationen und
   welche Testklasse konvergieren dieselben dimensionslosen Antworten, mit
   welcher Fehlerschranke und wie vielen verbleibenden relevanten Parametern?

Die kurze präzisierte Struktur ist

    R_cl = exakte konservative Completion,
    R_scale = begründete Blockierung plus zugehörige effektive Auslese.

R_cl beseitigt Darstellungsredundanz. R_scale kann physikalische Unterschiede
irrelevant machen. Dass beide aus einer primitiven Regel folgen, wäre ein
starker neuer Satz; es ist im Vorschlag aber noch nicht gezeigt.

Der billigste entscheidende TFPT-Test wäre eine **einzige native Blockabbildung**,
an der man zwei tatsächlich unterschiedliche erlaubte Quellenvariationen
vergleicht. Mindestens eine phasensensitive Antwort, eine geladene Mehrzeitantwort
und die Record-Rückkehr müssen unter derselben Skalierung kontrolliert werden.
Keine individuelle Umdeutung der Messung und keine Anpassung von g/Δ je Test.
Solange der gemeinsame Quellenadapter dafür fehlt, gibt es keine gerechtfertigte
native Skalenrechnung. Der vorliegende Bericht ersetzt ihn nicht durch ein Spielmodell.

## 12. Bilanz unabhängiger Entscheidungen

| Kandidat | Was wirklich wegfällt | Was nicht wegfällt |
|---|---|---|
| Vollständiger operationaler Quotient | nicht unterscheidbare interne Darstellungen | messbare Dynamik-/Zustandsunterschiede |
| Konservative saturierte Completion | fehlende syntaktische Zusammensetzungen | Auswahl zwischen vollständigen Theorien |
| Attraktion unter einer festgelegten Blockregel | einige Anfangsparameter innerhalb eines Einzugsgebiets | Wahl der Regel, Klasse, Tests und gegebenenfalls des Einzugsgebiets |
| Vorliegender TFPT-/E₈-Anschluss | in dieser Runde keine neue primitive Auswahl | gemeinsamer Quellenvertrag und alle T1–T8-Gesamtziele |

Im bistabilen Gegenmodell reduziert die feste Regel einen kontinuierlichen
Anfangsparameter innerhalb jedes Einzugsgebiets auf dessen Grenzwert. Es bleibt
eine binäre Klassenwahl (außer dem instabilen Separatrixfall), und die Regel
selbst war gegeben. Das ist kein gemessener ΔN-Wert für TFPT.

**Keine primitive unabhängige TFPT-Entscheidung ist durch den aktuellen
Vorschlag bereits nachweislich eliminiert.** Ebenso kein echter neuer Holdout:
bekannte Compilerwerte werden durch nachträgliches Verbergen nicht unabhängig.

## 13. Status der großen Folgerungen

| Ziel | Status nach dieser Prüfung |
|---|---|
| T1 | Completion und Auswahl getrennt; keine eindeutige physische Quelle |
| T2 | Algebraischer Record-/Stromrahmen ersetzt nicht den nativen Feldadapter |
| T3 | Kein gemeinsamer 3+1D-Prozess aus einer kausalen Recordordnung hergeleitet |
| T4 | Kein positiver chiraler Grenzwert oder Spiegelentkopplung hergeleitet |
| T5 | Stabilität ist sinnvoll formalisiert; keine native Kontinuumsfolge konstruiert |
| T6 | Keine physikalischen Kopplungen als neue Fixpunktinvarianten berechnet |
| T7 | Kein dynamischer universell gekoppelter Spin 2 |
| T8 | Interne Apparatur als Modellierungsanforderung, keine autonome Zustandsauswahl |
| RH | Keine volle positive Weil-Identifikation |
| Faktorisierung / P versus NP | Kein neuer algorithmischer oder Komplexitätssatz |

## 14. Verifikation und Grenzen

`checker.py` prüft **65 exakte endliche Bedingungen**: Qubit-/Recordidentitäten,
phasensensitive Unterscheidbarkeit, die stochastische Blockmatrix, ihr exaktes
Polynom, Fixpunkte und Steigungen, unabhängige Blöcke, monotone Kontrollschritte,
teilbare Kanäle, formale Eulerproduktkontrollen und beide Clock-Gegenformeln.
Normaler Lauf und `-OO` liefen erfolgreich und ergaben byteidentische JSONs.
Die Quellenhashes werden vor und nach jedem Lauf verglichen.

Die allgemeinen Completion-, Einzugsgebiets- und Testtopologiesätze sind oben
bewiesen; sie werden nicht allein durch eine Prüfzahl legitimiert. Es gab
keinen vollständigen Lean-Neubau, keine neue Messreihe und keine frische
Wiederholung sämtlicher historischer TFPT-/RH-Experimente.

Die PDF-Skills dienten dem Quellenabgleich, die beiden Forschungsgraph-Skills
der Vorarbeits- und Herkunftsprüfung. Wegen der beschriebenen fehlenden
Graphquellen kann keine vollständige aktuelle Korpusabdeckung behauptet werden.
Bestehende Paper, PDF, Webseite, Ledger und fremde Änderungen blieben unangetastet.
Kein Commit oder Push.

**Schlusssatz:** »Eine konsistente vollständige Prozessbeschreibung ist unter
ihren zulässigen Operationen abgeschlossen« ist hier tragfähig. Das stärkere
»Eine physikalische Realität existiert genau dann, wenn …« ist damit weder
mathematisch ausgewählt noch empirisch begründet.
