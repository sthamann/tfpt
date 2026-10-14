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

## Nachtrag: Was das Original über die Lage von Γ sagt [Zitat E, Schluss B]

`tfpt_3_e8_audit_bootstrap.tex:12349`: „the orientable double cover of the Möbius
fibre is a cylinder with two boundaries plus one Z2 seam Γ"; `:12559`: „the
collar deck is the deck transformation of a covering (the Z2 seam of the Möbius
double)".

1. Γ liegt im **Zylinder**, der orientierbaren Doppelüberlagerung der
   Möbiusfaser, nicht in der Himmelssphäre. Der Zylinder hat b₁ = 1; auf seinem
   nicht zusammenziehbaren Kreis Γ sind NS und R beide zulässig. Das Argument von
   Theorem B (b₁(S²) = 0 ⇒ NS auf jedem Kreis) erzwingt NS auf Γ deshalb nicht.
2. Γ überlagert die Seele der Möbiusfaser zweifach; das Deck ist eine
   orientierungsumkehrende Decktransformation. Der Fermiontransport einmal um Γ ist
   das Quadrat des Pin-Lifts r dieser Schleife: r² = +1 (Pin+) ergibt R auf Γ,
   r² = −1 (Pin−) ergibt NS. v506 rechnet mit D² = −1, also der Pin−-Wahl.
3. Mit diesem Contract: **Pin+ der Möbiusfaser ⇔ R auf Γ ⇔ Clock in der
   TFPT-Glueklasse A3 ⊕ D5**; Pin− ⇔ NS ⇔ A1 ⊕ D6 / A1 ⊕ A7.
4. Physikalisches Wörterbuch (Literatur, hier nicht geprüft): Euklidisches Pin+
   entspricht nach Wick-Rotation einer Zeitumkehr mit T² = (−1)^F
   (Kramers, gewöhnliche Spin-½-Fermionen), Pin− entspricht T² = 1
   (Kapustin–Thorngren–Turzillo–Wang 2015; Witten 2016). Falls die
   Originalforderung „U² = (−1)^F" physikalisch als Kramers-Bedingung gemeint ist,
   gehört sie zur **Pin+**-Wahl. v506 hat sie als euklidisches D² = −1
   umgesetzt, also als Pin−. Dieser Vorzeichenwechsel zwischen euklidischer und
   lorentzscher Lesart ist der konkrete Kandidat für die übersehene
   Fehlabstraktion.

**Entscheidender Test:** die Pin-Struktur der Möbiusfaser aus der ursprünglichen
Reflexionspositivität bestimmen, also ob die OS-Reflexion Θ auf den Nahtfermionen
als Pin+ (Θ-Spiegelung quadriert zu +1) oder Pin− wirkt. Ein bereits vorhandener
Baustein ist die Reflexion Θ des Originals; ihre Wirkung auf Fermionen ist in v506
nicht als Möbius-Deck verwendet worden.
