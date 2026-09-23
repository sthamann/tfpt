# Ein gemeinsames Compiler-Objekt: algebraisch rekonstruiert, physikalisch offen

9. September 2026. Prüfung der eingereichten Notiz über den positiven Kegel
des integralen Anker-Kommutanten. Drei unabhängige Arbeitsstränge wurden
mit einer eigenen exakten Rechnung zusammengeführt. Keine Änderung an
Paper, Webseite, Originalquellen oder T1–T8-Status.

## Ergebnis

**Der Ansatz trägt mathematisch weiter, als die eingereichte Notiz bereits
zeigt.** Eine klar definierte ganzzahlige Vervollständigung liefert nicht
nur einen Lorentz-Kegel: Ihr Operationsgitter ist das tatsächlich verwendete
TFPT-E₈-Gitter, einschließlich Metrik, Gauß-Struktur, Familienwirkung und
Anker. Dafür liegt eine explizite bijektive Abbildung vor.

Als vollständiges physikalisches Ursprungsobjekt aller Arbeitsfronten ist
die Konstruktion trotzdem nicht validiert. Zustand, erlaubte Prozesse,
lokale Felder und gemeinsame Dynamik folgen nicht aus der algebraischen
Eindeutigkeit. Für eine naheliegende Identifikation mit der ganzen
vorhandenen Clock-Quelle gibt es sogar einen präzisen Ausschluss.

## Welches Objekt wir jetzt bestimmen können

Im rationalen Anker-Kommutanten beginnt die Notiz mit der Ordnung
O=Z[a]⟨1,u₁,u₂,u₃⟩, a²=uⱼ²=−1. Eine „Ordnung“ ist hier eine ganzzahlige
Menge von Operationen, die unter Addition und Multiplikation geschlossen ist.
Die Einbettung in 2×2-komplexe Matrizen behält die geerbte Adjungierung.

Es gibt die genaue Kette

```
O  ⊂  R = O[w]  ⊂  M = P M₂(Z[i]) P⁻¹,
w=(1+u₁+u₂+u₃)/2,      P=[[1,1/(1+i)],[0,1/(1+i)]].
```

R ist die eindeutige minimale integrale Erweiterung, in der der festgelegte
Familienzyklus durch eine Einheit der Ordnung ausgeführt wird. M ist die
eindeutige maximale Ordnung darüber. Beide Schritte haben Gitterindex 4;
zwischen R und M liegt keine weitere Ordnung. Beide erhalten die Adjungierung.

Das sind **bedingte Eindeutigkeitssätze**. Ohne die Auswahlregel „minimal“
oder „maximal“ sind R und M zwei verschiedene zulässige Operationsmengen.
Die Forderung, mit der natürlichen Spurform wieder das selbstduale
E₈-Gitter zu erhalten, wählt innerhalb dieser Klasse M aus: R ist noch
nicht unimodular. Die tatsächliche mikroskopische Ausführbarkeit sämtlicher
Operationen von M ist dadurch nicht bewiesen. [Vollständiger Ordnungsbeweis](ORDER_PROOF.md).

## Drei Strukturen aus derselben Operationsordnung

| Blick auf M | Exaktes Ergebnis | Bedeutung dieser Prüfung |
|---|---|---|
| Ganzzahlige Operationen mit positiver Spurform ReTr(AB*) | E₈-Gitter, Determinante 1, 240 Wurzeln | Explizite Rückabbildung zum ursprünglichen TFPT-Gitter |
| Selbstadjungierte positive Elemente im reellen Raum | Vierdimensionaler Lorentz-Kegel | Geometrie möglicher positiver Wirkungen, noch keine Ereignisraumzeit |
| Invertierbare Operationen mit ν(A)=\|det A\|² | Multiplikative Gauß-Norm und additive logarithmische Skala | Algebraische Verbindung von Komposition, Geometrie und Arithmetik |

Diese beiden Normen sind verschieden. Von den 240 E₈-Wurzeln sind hier
96 unitäre Operationen und 144 Rang-eins-Operationen. Beispielsweise hat
ein nilpotentes Matrixeinheit-Element E₈-Normquadrat 2, aber Determinantnorm
0. Das ist keine positiv definite multiplikative Oktaven-Norm. Ebenso ist
ein E₈-Gitter nicht bereits die E₈-Liealgebra oder ein System aus acht
physikalischen chiralen Strömen.

Die neue markierte Abbildung lautet in den ursprünglichen ganzzahligen
Construction-A-Koordinaten, mit zⱼ=x₂ⱼ+i x₂ⱼ₊₁:

```
F_A(x) = (z₃ 1 + z₀ u₁ + z₁ u₂ + z₂ u₃) w* / 2.
```

Sie ist eine Isometrie des gesamten Gitters, nicht nur der 240 Wurzeln;
ihre ganzzahlige Basismatrix hat Determinante 1. Sie erhält den ursprünglichen
Gauß-Operator und den Familienzyklus und bildet den tatsächlich ausgewählten
Anker exakt auf a ab. Das ist eine Rekonstruktionsschleife aus vorhandenen
Compiler-Daten, kein voraussetzungsfreier neuer Beweis, warum die Natur E₈
verwenden müsse. [Exakte Abbildung und Markierungen](MARKED_BRIDGE.md).

## Was die Identifikation begrenzt

Eine einzelne M₂(C)-Algebra hat bei eigener autonomer unitärer Entwicklung
nur einen verschiedenen positiven Übergangsfrequenzbetrag. Die vorhandene
Clock-Quelle besitzt zwei: (√3−1)\|h\| und (√3+1)\|h\|. Ihr Verhältnis
2+√3 identifiziert die beiden Dynamiken deshalb nicht.

Zusätzlich schließt das genaue Spektrum der Clock eine unitale, von der
ganzen Clock beziehungsweise Familie normalisierte M₂-Einbettung in den
komplexen Achtmodenraum aus, wenn die internen komplexen Strukturen
identifiziert werden. Dies ist ein beschränkter Darstellungssatz, kein
Ausschluss größerer, komprimierter oder unendlichdimensionaler Realisierungen.

Konstruktiv findet man in derselben Quelle zwei überlappende Zweimoden-Ecken,
die jeweils eine der langsamen Frequenzen tragen. Behält man beide Transfers,
ihre Adjungierten und ihre Produkte, erzeugen sie zusammen M₃(C). Das zeigt
eine konkrete Kompositionsaufgabe für einfache Bausteine. Es leitet weder
neun Raumzeitdimensionen noch eine neue physikalische Grundzustandswahl ab.

Auch Positivität und Familiensymmetrie wählen noch keinen eindeutigen Zustand.
Für die Operationen der Notiz können vollständige Quanteninstrumente und
eine kohärente Siebenpfad-Realisierung angegeben werden. Ihre Präparation,
Kontrolle und Postselektion sind aber zusätzliche Prozessannahmen. Nach
Normierung enthält die logarithmische Skalenänderung einen zustandsabhängigen
Erfolgswahrscheinlichkeitsterm. Ein endlicher Phasenoperator ersetzt außerdem
keinen invertierbaren Halb-Ladungstransport mit nichttrivialem Integer-Carry.
[Prozesssätze und Gegenbeispiele](PROCESS_BOUNDARIES.md).

## Der nächste entscheidende Nachweis

Die aussichtsreiche Lesart ist jetzt: **ein einfacher lokaler Operationsbaustein
mit einer präzisen Kompositionsregel**, nicht eine einzelne kleine Matrixalgebra
als bereits vollständige Welt.

Der nächste Quellenbeweis muss die oben konstruierte markierte Ordnung mit
tatsächlich zugänglichen Operationen verbinden. Besonders trennscharf ist der
kleine Vierteldrehungsoperator q=(1+a)(1+u₁)/2: Er liegt in M, aber nicht in R.
Seine physikalisch erlaubte Realisierung würde zwischen den beiden Ordnungen
unterscheiden; das bloße Beobachten desselben positiven Kegels tut es nicht.
Anschließend muss die Komposition der beiden realen Clock-Ecken ihren
Hamiltonoperator, Zustand und zugänglichen Messungen erhalten. Die aktuelle
Half-Charge-Quelle verlangt weiterhin einen sektortreuen Feld-Intertwiner.

Für RH bleiben vollständige arithmetische Spur und globale Positivität offen;
für Faktorisierung fehlen N-abhängiger Zugriff und ein kostenkontrollierter
Faktorleser. Hylæans aktuellen Quellcode haben wir hier nicht auditiert und
keine Realisierung dieser Algebra in seinem Zustandssystem nachgewiesen.
[Korpusabgleich und Abdeckungsgrenzen](RESEARCH_SCOPE.md).

## Reproduzierbarkeit

Alle 44 ursprünglichen exakten Prüfungen reproduziert; zehn direkte
Quellpins und zehn archivierte Quellkopien passen zum Checkout. Zusätzlich
16 neue Tests, jeweils normal und unter Python -OO, sowie zwei bytegleiche
vollständige Ergebnisdateien. [Testbericht](TEST_RESULTS.md),
[exaktes Ergebnis](validation.json), [optimierter Replay](validation_optimized.json).

Basis-Commit: 66b91e40e245569f06ab440ead80f446c9be0ee5, mit ausdrücklich
gepinnten lokalen Vorarbeiten. Kein Commit/Push oder Projektstatus-Upgrade.
