# Spinstruktur des Nahtdoppels entscheidet die E8-Klasse der Clock

Operatoren exakt wie in `verification/v506_seam_clock_rigidity.py`, Teil B:
16 reelle Majorana-Plätze auf dem Nahtdoppel, Deck D = halbe Verschiebung,
Clock C = Viertelverschiebung, Randvorzeichen −1 (NS, v506) oder +1 (R).

## Ergebnis [E]

| Operator | NS (v506, Theorem B) | R (periodisch) |
|---|---|---|
| Fock-Lift des Decks | U² ∝ γ₁…γ₁₆ = (−1)^F, nicht spaltend | U² skalar, spaltend |
| E8-Klasse der Clock C (beide Spinlifts) | A1 ⊕ D6 bzw. A1 ⊕ A7 | **A3 ⊕ D5** (beide Lifts) |
| E8-Klasse des Decks D | A1 ⊕ E7 bzw. D8 | D8 |

Die TFPT-Glueklasse (Gradierung C mit μ = (½⁵, 0³), Zentralisator A3 ⊕ D5) ist
also **genau** die Klasse der geometrischen Viertelverschiebung auf einem
**periodischen** Nahtdoppel. Die NS-Version des Originals liegt in einer anderen
Konjugationsklasse von Ordnung-4-Elementen von E8.

## Konflikt im Original

* `SEAM.CLOCK.RIGIDITY.01` (v506), Theorem B: Die Himmelssphäre hat eine
  eindeutige Spinstruktur, ihre Einschränkung auf jeden Kreis ist NS. Daraus
  folgt U² = (−1)^F: „the clock's order fermionically forced".
* `v993` (Kopf): „glue group cyclic of order 4 on BOTH factors, from the finite
  shadow of U² = (−1)^F".
* Glueklasse A3 ⊕ D5 als Fixalgebra der Clock.

Als E8-Elemente schließen sich diese Aussagen am selben Operator aus: Mit
U² = (−1)^F (NS) liegt die Clock **nicht** in A3 ⊕ D5. Die Folgerung von
U² = (−1)^F auf die Glueklasse trägt nur auf Diskriminantenebene
(`[λ]² = [v]`), nicht als Konjugationsklasse in E8.

## Auflösung durch die Überlagerungslesart [E Rechnung, B Identifikation]

Theorem B betrifft Kreise, die in S² **eingebettet** sind. Das Nahtdoppel wird
im Original zugleich als **Überlagerung** beschrieben (`SEAM.BIT.FREEDOM.01`:
„the collar deck … is the deck transformation of a COVERING", tfpt_3
„cylinder + one Z2 seam"). Eine zusammenhängende Doppelüberlagerung ist nicht
eingebettet. Ihre Spinstruktur ist der Rückzug von der Basis, und der Rückzug von
NS ist R: Die Holonomie (−1)² = +1. Der Checker zeigt zusätzlich, dass das
R-Doppel unter dem Deck in den Basis-NS-Sektor (Deck −1) und den
Basis-R-Sektor (Deck +1) zerfällt.

**Folge der Überlagerungslesart:**
1. Die geometrische Clock liegt in der TFPT-Glueklasse A3 ⊕ D5, für beide
   Spinlifts.
2. Der Feldraum des Doppels enthält automatisch NS- **und** R-Sektor der
   eingebetteten Naht, also genau die Summe, die eine E8-Erweiterung über
   gewöhnliche Fermionen hinaus braucht. Das Deck unterscheidet die Sektoren;
   seine Fixalgebra ist D8.
3. Ordnung 4 der Clock kommt dann aus der Geometrie (`SEAM.CLOCK.RIGIDITY.01`,
   Theorem A: Quadratwurzeln des Decks in PGL2 haben automatisch Ordnung 4),
   nicht aus U² = (−1)^F. Der fermionische Zwang aus Theorem B entfällt; er wird
   für die Ordnung nicht gebraucht.
4. Konsistent mit `seam-u1-clock-splitting-20261014`: R auf dem Doppel ist dort
   die echte Z8 (Deck² = 1 auf den Fermionen).

**Folge der eingebetteten Lesart (v506 wie geschrieben):** Die Clock fixiert
A1 ⊕ D6 oder A1 ⊕ A7. Träger D5 und Familien-A3 sind dann nicht ihre
Fixalgebra; die Glueklasse müsste aus einer anderen Z4 kommen.

## Verbleibende Ursprungsfrage

> Liegen die 16 Trägerplätze auf dem in die Himmelssphäre **eingebetteten**
> Nahtkreis (NS, Glueklasse ausgeschlossen) oder auf seiner
> **Doppelüberlagerung** (R, Glueklasse genau getroffen)?

Das ist eine einzige topologische Entscheidung über das Original. Sie legt die
E8-Klasse der Clock fest. Das Original verwendet bisher beide Lesarten.
