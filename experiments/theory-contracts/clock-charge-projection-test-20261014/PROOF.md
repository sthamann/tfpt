# Gemeinsamer Clock-/Quellenladungs-/Pakettest

Unabhängige Prüfung des Codex-Tests (lokal, 14. Oktober 2026).

## P1 [E] – Projektionsnormen der Quellenladung

Für jede ehrliche, mit U(1) gekleidete Fold-Clock (α = ¼, ¾; alle acht
Achtelwurzeln j; beide Spinlifts) ist der Zentralisator A3 ⊕ D5. Die Quellenladung
`q = (1)⁸` hat die Projektionsnormen `(|q_D5|², |q_A3|²)`:

| Gitter | Lift μ | Lift μ + e₁ |
|---|---|---|
| E8_s | (4, 4) | (8, 0) |
| E8_c | (6, 2) | (6, 2) |

* Bestätigt: Der Index j ändert das Paar nie. Codex' Aussage zur Konjugation der
  acht Kleidungen hält.
* **Ergänzung:** In E8_s entscheidet der Spinlift zwischen (4,4) und (8,0). In E8_c
  ist das Paar liftunabhängig (6,2); Codex' Bild `M R0 q = (−1,−1,2,0,0; 1,−1,0)`
  hat genau (6,2).
* Das Paar ist invariant unter gleichzeitiger Konjugation von Clock und q, weil die
  Faktoren A3 und D5 nicht isomorph sind und daher nicht vertauscht werden können.

## P2 [E] – Paketlemma

Für ganzzahlige m mit Σm = −2 gilt `Σβ_j² = Σm_j² − 1`; das ist positiv und
ungerade, weil Σm² ≡ Σm ≡ 0 (mod 2). Ein Paket nur mit Determinantenanteil und
ganzzahliger Trägerspur t hat `|q_F|² = t²(Σm² − 1)`. Diese Zahl ist **nie 2**:
t = 0 gibt 0, |t| ≥ 2 gibt ≥ 4, und t = ±1 würde Σm² = 3 verlangen, was ungerade ist.

* **c scheitert** am gemeinsamen Test (Familienprojektion 2) für **alle**
  ganzzahligen Trägerrichtungen, ohne die Identifikation x = e_weak.
* s mit Lift μ: (4,4) = Paket m_A mit t = 2 (`4 = 2²·1`).
* s mit Lift μ + e₁: (8,0), Familienprojektion 0. Formal mit t = 0 und beliebigem m
  verträglich; dann trägt aber die Familie keine Quellenladung, und die
  Ward-Identifikation mit m_A (t = 2) entfällt. Der Spinlift ist in E8_s also nicht
  gleichgültig: Nur μ trägt das Ward-Paket.

## P3 [E Buchhaltung] – s-Modell-Dublett (Codex)

Mit β = p* gilt δ·β = −1 für alle α. Die Moden `A = J^β_{−1}` und
`B = J^{−β}_{+1}` verschieben K um `−n ± δ·β = 0`. Bei Level eins gilt
`[A, B] = H^β_0 − 1`. `A|0⟩` hat Ladung β, L0 = 1 und K = 0. Das bestätigt den
neutralen Zweizustandsspeicher **innerhalb** der angenommenen s-Erweiterung. Im
rohen CAR-Raum ist er nicht vorhanden (Cartan-Obstruktion).

## Status

Zusammen mit `ward-chirality-vacuum-no-go-20261014`:
* c: verliert q/2 (W1) und besteht den Projektionstest für keine ganzzahlige
  Paketrichtung (P2).
* s, Lift μ: besteht Ward- und Pakettest (4,4), hat aber unter dem Fold-Zeitgesetz
  den Nullzustand p*. Der Nullzustand ist genau das SU(2)₁-Dublett aus P3.
* s, Lift μ + e₁: Familienprojektion 0, kein Ward-Paket.

Ein unabhängiger Familiengenerator oder eine andere physikalische Ladungsperiode
würde die Voraussetzungen ändern und müsste aus der Quelle folgen.
