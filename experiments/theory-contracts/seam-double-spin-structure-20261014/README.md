# Spinstruktur des Nahtdoppels (14. Oktober 2026)

Status: **PARTIAL**, keine Promotion. `python3 checker.py`: 24 Prüfungen, ca. 3 s
(numpy, scipy). Grundlage sind die Originaloperatoren aus `v506`, einschließlich
der Fock-Lifts in Cl(16).

**Ergebnis.** Dieselbe Viertelverschiebung auf den 16 Majorana-Plätzen liegt
* bei **periodischem** Rand (R) genau in der TFPT-Glueklasse **A3 ⊕ D5**, für
  beide Spinlifts; das Deck spaltet (U² skalar);
* bei **antiperiodischem** Rand (NS, wie in v506) in A1 ⊕ D6 oder A1 ⊕ A7, also
  **nicht** in der Glueklasse; das Deck spaltet nicht (U² = (−1)^F).

**Konflikt.** Das Original leitet die Ordnung-4-Glue aus U² = (−1)^F ab (v506,
v993). Als E8-Klassen schließen sich „U² = (−1)^F" und „Clock = Glueklasse" aus.

**Auflösung.** Das Original beschreibt das Nahtdoppel zugleich als Überlagerung.
Der Rückzug der NS-Struktur längs einer Doppelüberlagerung ist R. In dieser
Lesart trifft die geometrische Clock die Glueklasse genau. Das Doppel enthält
dann NS- und R-Sektor der Naht, und die Ordnung 4 ist rein geometrisch.

**Offene Entscheidung.** Liegen die 16 Plätze auf dem eingebetteten Nahtkreis
oder auf seiner Doppelüberlagerung? Details: `PROOF.md`.
