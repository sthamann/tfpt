# Ward-Markierung → nativer W-Bosonmode → Familiengewicht → geometrischer Vektor h

Positiver Bestand, an den angeschlossen wird:
`source-native-clock-flavor-bridge-20260922/PROOF.md:20–129` (Operatorwörterbuch
Q/Σ/G/T/P ↔ M/U mit N-Metrik und S), `:136–169` (Kanäle von Sym²(16⊗4)),
`source-native-retarded-selection-20260922/PROOF.md` §1–3 (nativer W-Operator
`H = ΔN_b + Σ_A (g b_A† P_A + h.c.)`, `P_A = Σ W_{A,ij} f_j f_i`, 64 CAR-Moden in
(16,4), 60 Bosonen in (10,6), `WW† = 8 I₆₀`, Erhaltungsgröße `N_f + 2N_b`, exakte
Bosonenelimination mit Kern `D_Δ`).

## Satz V [E]

* **V1 – Grobe Clock-Implementierung (präzisiert).** Im TFPT-Rahmen ist Grad 2 der
  Glue-Graduierung C genau die Menge der 60 (10,6)-Wurzeln, Grad 1 die 64
  (16,4)-Wurzeln. Auf den Erzeugern des nativen Modells ist `i^{N_f + 2N_b}` eine
  korrekte grobe Implementierung dieser Gradphasen. **Das macht die fermionischen
  f ∈ (16,4) nicht zu bosonischen E8-Stromfeldern** und beweist nicht dieselbe
  vollständige g-Wirkung auf den D8-Strömen. `N_f + 2N_b` ist eine zusätzliche native
  Teilchenzahl und **nicht** die Quellenladung H_q.
* **V2 – Familiengewichte.** Die D3-Anteile der (10,6)-Wurzeln sind die sechs
  Vektorgewichte ±e_j der 6 = Λ²4. Tᵀ bildet sie bijektiv auf die sechs
  A3-Gewichte mit zweimal +½ und zweimal −½ ab. Das sind genau die sechs minimalen
  Familienlifts `β_F = m + ½`, m eine Permutation von (0,0,−1,−1).
* **V3 – Ward-Gewicht (präzisiert).** `λ_A = (e₃; 1,0,0)` ist eine (10,6)-Wurzel und
  `Q' = 2λ_A`. Codex hat unabhängig hergeleitet: Nach Auswahl von L_s ist `q/2` eine
  Norm-2-Wurzel; im clock-verträglichen D5/D3-Split hat sie die Projektionen (1,1),
  muss also eine der 60 gemischten ganzzahligen (10,6)-Wurzeln sein. Damit sind
  `q = 2λ` und die primitive Trägernorm 1 in dieser Vergleichsklasse **hergeleitet**.
  λ ist ein **Gewichtsvektor**, nicht die U(1)-Ladung eines Bosonenzählers:
  `H_q E_λ` hat Ladung `q·λ = 4`; E_λ ist ein bosonischer h = 1-Strom vom Grad 2, und
  das rohe Zeitgesetz gibt `K(λ) = 3/4 + α/2` (7/8 bzw. 9/8). Das konforme Gewicht
  ist keine native Energie Δ.
* **V4 – Codex' Wörterbuch exakt bestätigt.** `LᵀL = N = S†S`; die sechs β_F sind
  `±L a_i` mit `a = (e₁, e₃, e₂+2e₃)`; `h_i = S a_i` ist orthonormal; v117:
  `M: h₁ → h₃ → h₂ → h₁`, `U: h₁ → −h₃, h₂ → h₂, h₃ → h₁`.
* **V5 – Kanalbuchhaltung.** `Λ²(16⊗4) = (10,6) ⊕ (120,10) ⊕ (126,6)` (2016),
  `Sym²(16⊗4) = (10,10) ⊕ (120,6) ⊕ (126,10)` (2080). Der native Paarvertex liegt im
  **antisymmetrischen** (10,6), nicht in den symmetrischen Yukawa-Kanälen.

## Die positive Kette

    Quellenladung q  ──Ward──►  q = 2λ_A,  λ_A ∈ (10,6)  =  Ladung eines nativen b_A
                                   │ Familienanteil (6 = Λ²4)
                                   ▼
                          β_F = m_A + ½   (Minimalpaket, zwei ±½)
                                   │ Codex: β_F = ±L a_i
                                   ▼
                          h = S a_i ∈ {±h₁, ±h₂, ±h₃} = ±M^j e₁ (S-Bild)

**Präzisierung (Codex):** Die Kette verbindet **Gewichtslabels**. β_F ist das
Cartanlabel des Ward-gewählten Bosonmodes, und L/S bildet Labels mit Rang 3 ab. Das
ist keine lineare Isometrie der sechs nativen Bosonamplituden; h_geom ist damit
**nicht** schon die native Bosonamplitude im Einsatz A(h). Der tatsächliche
Feldvergleich steht in `../native-field-projector-test-20261014`: Der einzige
clockkovariante Feldprojektor ist nicht ladungskovariant, und die kovariante Abbildung
Zustand → Cartanvektor ist die quadratische Impulsabbildung.

## Was der native Vertex **nicht** liefert

1. **Die relative Clock auf einem Bein.** Der native Vertex ist antisymmetrisch
   (Λ², (10,6)) und liefert die A(h)-Struktur. Der symmetrische Yukawa-Ausdruck
   `Y_C(h) = CᵀA(h) − A(h)C` braucht zusätzlich eine Clock C auf nur einem Bein
   (`source-native-clock-flavor-bridge` §3: eine gemeinsame Basisänderung erzeugt
   sie nicht).
2. **Eine nichtskalare Familienzeitantwort.** Der exakte Eliminationskern `D_Δ` ist
   SU(4)-gleichförmig (`WW† = 8 I`); die normierte lineare Familienantwort im
   symmetrischen Quellenzustand ist einheitlich (`source-native-retarded-selection`).
   Die Ward-Wahl von λ_A legt ein Gewicht fest, liefert aber keine
   familienabhängige Zeitkorrelation.
3. **Den Q-Compiler.** Q wird im Wörterbuch nur durch Ähnlichkeit mitgeführt; aus dem
   nativen Vertex folgt er nicht.

Herkunftsgrenze: Der native W-Operator ist ein vorhandener Kandidat. Seine Herleitung
aus dem P1-Kern und seine Identifikation mit dem gefalteten Nahtfermion sind offen.
V1 ist eine Aussage über den nativen Modellraum, nicht über die gefaltete CAR-Quelle.

## Nächste echte Quellenidentifikation

**Korrektur:** Die Forderung „ein Operator, der nicht mit `WW† = 8I` vertauscht" war
falsch formuliert: `WW†` ist skalar, jeder Endomorphismus des 60er-Ausgangs vertauscht
damit. Auf identischen CAR-Moden gibt es außerdem keine Ein-Bein-Wirkung. Die
richtige Frage ist die nach einem **familienabhängigen Relativtransport zwischen den
zwei Zeitpunkten** der bilokalen Austauschstruktur. Das ursprüngliche
Fold-Zeitgesetz liefert einen solchen nichtskalaren Familiengenerator δ_F:
`../source-time-family-generator-20261014`. Für einen lokalen 3+1D-Weyl-Yukawa
braucht es zusätzlich den Lorentz-Spin-/Austausch-Intertwiner; ein symmetrisches
internes Y_C auf denselben zeitgleichen CAR-Moden kontrahiert zu null.
