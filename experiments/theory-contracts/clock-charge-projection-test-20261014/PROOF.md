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
* In P1 wird C **direkt** geliftet. Der Lift μ + e₁ ist ein unabhängiger
  C-Kontrolllift, **kein** Quadrat der ursprünglichen g-Wirkung (siehe P4). Codex'
  Bild `M R0 q = (−1,−1,2,0,0; 1,−1,0)` hat genau (6,2).
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
* (8,0) tritt nur beim unabhängigen C-Kontrolllift μ + e₁ auf (Familienprojektion 0,
  formal t = 0). Als C = g² derselben Quellen-g-Wirkung zählt er nicht.

## P4 [E] – Operatorkomposition C = g² (Codex)

Die Quelle liefert zuerst g mit `μ_g = (k+α)/8 + c`; C = g² ist erzwungen. Lifts von
g, die die D8-Stromwirkung erhalten, unterscheiden sich um v ∈ D8*/D8 (Vertreter
0, e₁, s, c). Weil D8*/D8 Exponent 2 hat, liegt 2v in D8 ⊂ E8: Alle Lifts von g
haben **denselben** Quadrat-Toruspunkt 2μ_g. Für alle acht Kleidungen und beide α
gilt dann s → (4,4) und c → (6,2). Der Lift 2μ_g + e₁ ist kein Quadrat, denn
`e₁ − 2v` hat ungerade Koordinatensumme und liegt in keinem E8.

## P5 [E] – s-Lemma ohne Einheits-Clutching

Familiennorm 4 = t²(Σm² − 1) mit positiv ungeradem zweitem Faktor erzwingt
|t| = 2 und Σm² = 2, also m = (0,0,−1,−1) bis auf S4. Das Minimalpaket folgt damit
**ohne** die Identifikation x = e_weak. Die Trägerrichtung bleibt offen:
Spur ±2 und Norm 4 erlauben z. B. 2e₃ und (1,1,1,−1,0).

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
* s mit C = g²: besteht Ward- und Pakettest (4,4), Paket m_A ohne Einheits-Clutching (P5), hat aber unter dem Fold-Zeitgesetz
  den Nullzustand p*. Der Nullzustand ist genau das SU(2)₁-Dublett aus P3.
* (8,0): nur unabhängiger C-Kontrolllift, keine Quadratwirkung der Quelle.

Ein unabhängiger Familiengenerator oder eine andere physikalische Ladungsperiode
würde die Voraussetzungen ändern und müsste aus der Quelle folgen.
