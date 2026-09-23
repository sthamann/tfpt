# TFPT / Universalraum v1.4 — die sechs nächsten Entscheidungen

14. September 2026. Begleiter zum vollständigen Hauptdokument und zum kurzen Update.

## Lösungen dieser Runde

Die sechs Fragen sind jetzt jeweils mit einem ausführbaren Vertrag beantwortet.
Das ist kein T1–T8-Abschluss und keine Promotion.

| Frage | Vertrag | Entscheidung |
|---|---|---|
| 1 Wer bedient das Labor? | `universalraum-v14-F1-primitive-20260914` | Primitive eingefroren: `U_e`, Zugriffsklasse, Born. Jeder Handgriff hat Umsetzung und Kosten. Filter sind Polynome von `H`, kein versteckter `Ω`-Projektor. `U` selbst nicht aus P1+P2. |
| 2 Welche Bauweise? | `universalraum-v14-F2-architektur-20260914` | Lokalität wählt nicht. Quellen-Selektor (Qv=1-Matching, CAR/Tensor in diagonaler ±1-Klasse, kein Hopping) schreibt **Bank pro Kante** vor. Spektrum ist Folge, nicht Wahl. |
| 3 Vierfachstruktur? | `universalraum-v14-F3-quartett-20260914` | Multiplizität der 4-Isotyp von `W(D₅)` ist exakt 4. Trunkiertes Quartett Kato-isoliert (Residuum `< 5·10⁻¹⁴`). Nacktes Nichtsingulettminimum und `H6`-Rest offen. |
| 4 Fehler und Größe? | `universalraum-v14-F4-fehler-skalierung-20260914` | Unabhängige Zellen brauchbar (556 / 890 Zyklen). Default-Kopplung `λ=J` liegt außerhalb des `10⁻⁶`-Fensters. |
| 5 Eine gemeinsame Welt? | `universalraum-v14-F5-gemeinsame-welt-20260914` | Eine Familie `C16 × (ℤ/Lℤ)^d` trägt die Teiltests, nicht gleichzeitig Kegel, chirales Maß und Spin-2. Verdict: `NO_GO_MISSING_SELECTORS`. |
| 6 Dieselben Parameter? | `universalraum-v14-F6-transfer-20260914` | Fixierte Branche gegen ACT: Spannung `≈ 3.51σ`. Flavour `Y = y·1`, keine Hierarchie. Status Spannung, kein nachträglicher Fit. |

T2 (native Halbladung), RH, Faktorisierung und P versus NP bleiben ungelöst.
Siehe die einzelnen README-Dateien der Verträge für Zahlen, Kills und Reproduktion.

## Das Gesamtbild

Wir haben jetzt ein berechenbares kleines Labor. Es kann einen Zustand herstellen,
eine Aufzeichnung machen und später testen, was diese Aufzeichnung verändert hat.
Neu sind nicht nur Formeln für einzelne Teile, sondern ein gemeinsamer Ablauf mit
vollständigen Erfolgswahrscheinlichkeiten. Uns fehlt weiterhin der Nachweis, dass
die ursprüngliche TFPT-Regel selbst dieses Labor und seine Bedienmöglichkeiten
erzeugt. Eine wachsende Anordnung solcher Labore ist außerdem noch keine
bewiesene Raumzeit mit Materie und Gravitation.

## 1. Wer bedient das Labor? — höchste Priorität

**Schon erreicht:** Ein vollständiger mikroskopischer Filter plus Aufzeichnung und
Endprüfung. Präparation gelingt pro Versuch mit etwa 16,19 %. Die gesamten
Erfolgsraten sind etwa 15,73 % mit behaltenem und 8,36 % mit frischem Record.
Der Unterschied entsteht in demselben deklarierten kontrollierten Modell.

**Offen:** Kontrollierte Zeitentwicklung, isolierte Kanten, Resonanz, Belegungsabfrage,
Messung und Reset sind noch Bedienmöglichkeiten, nicht alle aus dem Compiler abgeleitet.

**Entscheidender Test:** Eine Liste primitiver Operationen einfrieren und für jeden
dieser Handgriffe eine explizite Umsetzung samt Kosten angeben. Kein zusätzlich
eingeführter Zielzustandsprojektor darf die eigentliche Aufgabe verstecken.

**Lösung:** Primitive `U_e` + Zugriffsklasse + Born. Alle neun Handgriffe sind
umgesetzt; der Tetramer- und der 13-Faktor-Sternfilter sind Polynome von `H`.
Vertrag `universalraum-v14-F1-primitive-20260914`. `U` bleibt nicht aus P1+P2.

## 2. Welche Bauweise ist wirklich vorgeschrieben?

**Schon erreicht:** Drei Architekturen sauber getrennt: gemeinsame globale Bank,
eine Bank pro Zelle, Vermittler pro Kante. Die letzten beiden können beide lokal sein.
Die kantenlokale äußere Bandschranke wurde auf 0,7 Δ verbessert.

**Offen:** Lokalität allein wählt die dritte Variante nicht aus. Unterschiedliche
Bauweisen geben unterschiedliche Korrekturen zur niedrigen Dynamik.

**Entscheidender Test:** Beide lokalen Varianten an identischen Quellanforderungen
messen. Eine Wahl nach dem angenehmsten Spektrum wäre keine Herleitung.

**Lösung:** An identischem C16 gemessen. Der Selektor liest kein Spektrum und
schreibt die kantenlokale Bank vor (CAR/Tensor, diagonale ±1-Klasse, kein
Hopping). Vertrag `universalraum-v14-F2-architektur-20260914`.

## 3. Können wir die Vierfachstruktur wirklich beweisen?

**Schon erreicht:** Die lokale vierte Ordnung ist eine Summe positiver lokaler
Operatoren. Die korrigierte 24.024-dimensionale Singulettrechnung liefert ein
vierfach gefundenes erstes Niveau und einen Gap von etwa 0,48648 J.

**Offen:** Gleitkommazahlen sind noch kein exakter Multiplizitätsbeweis. Die bisherigen
nackten Untergrenzen anderer Sektoren benötigen zertifizierte Fehlerintervalle;
der mikroskopische Rest bleibt eine weitere Aufgabe.

**Entscheidender Test:** Exakte Symmetrieprojektoren plus zertifizierte Spektralgrenzen.
Die neue positive Form reduziert dafür die algebraische Schwierigkeit deutlich.

**Lösung:** Die erste Anregung ist die irreduzible Standard-4 von `S₅` (`χ(01)=+2`).
`F4` ist `Aut`-invariant, die 4-Isotyp bleibt exakt vierfach. Kato isoliert das
trunkierte Quartett. Nacktes Nichtsingulettminimum und `H6` offen.
Vertrag `universalraum-v14-F3-quartett-20260914`.

## 4. Bleibt das Labor bei Fehlern und wachsender Größe brauchbar?

**Schon erreicht:** Ein vollständiger Sternfilter mit 13 physikalischen Zeitfaktoren;
ein gemeinsamer Start-/Endversuch benötigt 26 solcher Schritte. Beim alternativen
Feedbackweg ist die Fehlerverstärkung pro dauerhaftem Zyklusfehler auf etwa 40,68
beschränkt. Unabhängige Zellen lassen sich mit einer logarithmisch wachsenden
Zykluszahl kontrollieren.

**Offen:** Reale Clockfehler, Entropieabfluss und wechselwirkende Zellen sind nicht
durch den unabhängigen Zelltest erledigt. Exakte Zeitwahl ist eine starke Ressource.

**Entscheidender Test:** Eine wachsende, wirklich gekoppelte Probe mit vollständig
ausgewiesenen Fehlern, Resetkosten und Zeitskalen — nicht nur ideale Einzelzellen.

**Lösung:** Unabhängige Zellen: bewiesen. Gekoppelte Default-`λ=J`-Probe: explizit
außerhalb von `10⁻⁶`. Vertrag `universalraum-v14-F4-fehler-skalierung-20260914`.

## 5. Entsteht daraus eine einzige gemeinsame Welt?

**Schon erreicht:** Skalierende Wärmetrace-Tests; ein expliziter zweidimensionaler
chiraler Flussoperator; Kontrollen gegen ungewollte Weyl-Arten; ein Tensor-Spektraltest.

**Offen:** Die Testfamilie gibt jede hineingesteckte Dimension wieder. Drei chirale
Nullmoden folgen bisher aus hineingestecktem Fluss drei. Ein Tensorprojektor erzeugt
noch keinen masselosen Gravitationsmodus. Das sind hilfreiche Kontrollmodelle,
aber nicht drei schon abgeleitete Eigenschaften des Universalraums.

**Entscheidender Test:** EINE native skalierende Familie muss Dimension und gemeinsamen
Lichtkegel, chirales Maß und Spin-2-Dynamik gleichzeitig tragen. Hier liegen T3, T4,
T5 und T7 zusammen. Ein positiver Test für nur einen dieser Punkte bleibt ein Teilresultat.

**Lösung:** Dieselbe Familie `C16 × (ℤ/Lℤ)^d` trägt Wärme, Overlap, Weyl und Tensor
gleichzeitig — und selektiert trotzdem weder Dimension noch Fluss noch Spin-2.
Verdict `NO_GO_MISSING_SELECTORS`. Vertrag `universalraum-v14-F5-gemeinsame-welt-20260914`.

## 6. Stimmen dieselben Parameter mit mehreren Beobachtungen überein?

**Schon erreicht:** Drei Nullmoden sind von einer Massenhierarchie unterschieden.
Ein konstanter Überlapp liefert im kontrollierten Beispiel gleiche Massen. In der
einfachen Inflationsbranche wurde die frei scheinende Wahl der E-Faltungszahl N
eliminiert und eine Spannung zwischen Amplitude und Spektralneigung sichtbar.

**Offen:** Vollständige Flavourstruktur und gemeinsamer empirischer Transfer.
Einzeln passend gewählte Parameter sind keine unabhängigen Vorhersagen.

**Entscheidender Test:** Amplitude, Neigung, Tensoranteil und Flavour mit derselben
fixierten Parametrisierung und ihren Korrekturen berechnen. ACT-Vergleich siehe
[Primärquelle, Tabelle 5 v2](https://arxiv.org/abs/2503.14452v2).

**Lösung:** Dieselbe Branche, kein Retuning: `ns` 3,51σ neben zentralem `As`;
kalibriert auf `ns` ist `As` um 2,028× zu groß. Flavour bleibt `Y=y·1`.
Status Spannung. Vertrag `universalraum-v14-F6-transfer-20260914`.

## Was das für die großen Ziele bedeutet

T1–T8 sind einzeln im Hauptbuch und Forschungsbericht zugeordnet; keines ist vollständig
geschlossen. Der Halbladungsoperator für T2 braucht weiter eine native analytische
Erweiterung. RH, Faktorisierung und P versus NP sind nicht durch die endlichen
physikalischen Tests gelöst. Neuere externe RH-/Faktorquellen sind lokal teilweise
nicht verfügbar und deshalb nicht als unabhängig verifizierter Fortschritt verbucht.

**Nächster Schritt nach diesen sechs Verträgen:** A2 der Konsolidierung
(Kommutante von `H_eff` auf dem harten C16-Belegungssektor) und ein zertifiziertes
nacktes Nichtsingulettminimum. Frage 5 und 6 sind als Physik *dieser* Quelle
jetzt negativ bzw. unter Spannung beantwortet, nicht als offene Wunschmodelle.
T1–T8 bleiben offen, weil `U` nicht aus P1+P2 kommt und T2/T4/T7 keine native
Naht, keinen Index 3 und keinen gravitativen Pol aus derselben Regel haben.
