# RH: geprüfte Bausteine und nächste Beweispflichten

**Kein RH-Beweis.** Dieser Lauf plant Forschung; er startet keine numerischen Jobs.

## Was der Planer verwenden darf

Nur exakt typisierte, frisch in Lean geprüfte Regeln. Alle Voraussetzungen werden gemeinsam benötigt. Ein Graphpfad, ein offenes Prop, eine numerische Stichprobe und eine Rezeptliste erzeugen keinen Satz.

Bewiesen und wiederverwendbar: ARCH-Fehler verschwindet pro festem Test; Existenzielle ARCH-Rate; Korrigierte gewichtete ARCH-Interpolation.

Die ARCH-Konstante darf vom festen Test abhängen; FREQ und globale Positivität bleiben offen.

## Priorisierte Forschungsrichtungen

### Vollständige rationale Gabor-Positivität

Weg 1: Alle folgenden Pflichten müssen erfüllt sein.

- Exakte arithmetische Blockzerlegung inklusive Pole und Gamma.
- Vollständige Kontrolle der Gabor-Parametergrenzen.
- Bewiesener unendlicher arithmetischer Rest.
- Beweis, dass die vorgeschlagene Konstruktion diese Zutaten tatsächlich zum Ziel verbindet (gabor_arithmetic_blocks).

Weg 2: Alle folgenden Pflichten müssen erfüllt sein.

- Eventuelle untere Read-Schranke.
- FREQ-Kegelvoraussetzung.
- Bewiesener unendlicher arithmetischer Rest.
- Exakter Native-zu-Gabor-Übergang mit Gauge und Testbereich.
- Beweis, dass die vorgeschlagene Konstruktion diese Zutaten tatsächlich zum Ziel verbindet (gabor_via_native_adapter).

### Native Positivität

Weg 1: Alle folgenden Pflichten müssen erfüllt sein.

- Eventuelle untere Read-Schranke.
- FREQ-Kegelvoraussetzung.

### Vollständige neue Randankopplung

Weg 1: Alle folgenden Pflichten müssen erfüllt sein.

- Beide niedrigen und unendlichen hohen Randkopplungen.
- Vollständige Energie-Dualnorm-Schranke des neuen Rands.
- Unabhängige Wiederholung mit gleicher Fehlerlast.
- Unabhängiger Audit der Originalform und ihres Bereichs.
- Zulässiger vollständiger neuer Formbereich.
- Beweis, dass die vorgeschlagene Konstruktion diese Zutaten tatsächlich zum Ziel verbindet (complete_boundary_energy).

### Schranken nur für tatsächliche Minimierer

Weg 1: Alle folgenden Pflichten müssen erfüllt sein.

- Lokale absolute Stetigkeit des tatsächlichen Spektralbodens.
- Vollständige Paritäts-, Testklassen- und Grenzabdeckung.
- Unabhängiger Audit der Originalform und ihres Bereichs.
- Arithmetische Kontrolle tatsächlicher Minimierer.
- Unabhängig bewiesener positiver Startwert.
- Beweis, dass die vorgeschlagene Konstruktion diese Zutaten tatsächlich zum Ziel verbindet (minimizer_relative_flow).
- Nullstellenunabhängige integrierbare Schranke durch eine erste Nullstelle.

## Grenzen und Kontrolle

8 unterscheidbare Konstruktionsvorlagen, keine neu gefundenen Operatoren oder Beweise. 12 bekannte Grenz- und Fehlerfälle werden getrennt klassifiziert. Die Einstufung OPEN_CONSTRUCTION bedeutet nur, dass die registrierten Filter diese genaue Vorlage nicht ausschließen.

Rangfolge und Kosten sind transparente heuristische Prioritäten, keine gemessenen Durchbruchswahrscheinlichkeiten. Die Suche ist begrenzt; sie beweist keine Vollständigkeit über alle möglichen Ansätze.

Das breite Register erfasst auch nicht einzeln geprüfte und historische Lean-Dateien. Nur die gesondert attestierten Regeln sind Beweisschritte; Quellenkopien zählen nicht als unabhängige Belege.

Vollständige maschinenlesbare Pflichten, Typen, Quellenabdrücke, Katalogtreffer und Kontrollfälle stehen in plan.json.
