# Originalterme auf dem neutralen Dublett (korrigierte Fassung)

Anschluss an `UR.SEAM.JOINT_WARD_STATE.01`: `G0 = span(|vac⟩, e^β)`,
`β = p* = (½⁴, −½⁴)`, `K|G0 = 0`, Anfangsdichte `ρ = |vac⟩⟨vac|` aus vollständigen
Ward-Daten.

## Korrektur der Fassung `3049793`

Die Aussage „alle Originalterme wirken auf G0 als null, ein neuer κ-Mischer ist
notwendig" ist **zurückgenommen**. Codex hat sie an fünf Stellen widerlegt; alle fünf
sind hier geprüft:

1. **Keine diagonale Verbindung erzwungen.** `source-boundary-lift-selection/PROOF.md:32–56`
   beginnt mit einer *gegebenen* allgemeinen U(5)-Verbindung. Sie wird nicht aus der
   Windung gewählt; unabhängige Verbindungen und Endomorphismen sind nicht
   beseitigt, Φ ist nicht bestimmt. `source-joint-spin-family-lift/PROOF.md:91–119`
   wählt `E = C³ ⊕ (L ⊕ C)` als **Rechen**repräsentanten (Z. 95: keine physische
   Wahl aus der Diagonalisierung). Ein Bündelsplit erzwingt keine diagonale
   Verbindung.
2. **q-neutral heißt nicht Cartan-neutral.** Alle Cartans kommutieren mit q, ihre
   β-Eigenwerte sind aber nicht alle 0. Codex' Paketfall: `h = diag(1,0,0,0,0)`,
   Minimal-m = (0,−1,−1,0), induzierte Cartanwirkung `y = (e1; e6)`, `Mβ = e1+e4`,
   also `y·Mβ = 1` und `P0 H_{y,0} P0 = diag(0,1)`. Der Checker bestätigt im
   Faltungsrahmen allgemein, dass β im D5-Faktor liegt und D5-Cartans mit
   `y·β ≠ 0` existieren, z. B. y = β/2 mit `y·β = 1`.
3. **M_f ist nicht kanalidentisch.** Für das markenverträgliche `f = cos 4θ` gilt
   `F M_f F* = cos(x/2)·diag((−1)^j)`; im zyklischen Eigenrahmen koppelt das
   k ↔ k+4 (Deck-Partner) und verlässt G0. Zudem ist `Λ = |k| + M_f` in
   `tfpt_research_contracts.tex:474–499` ein Subprinzipal-**Ansatz**; die physische
   Markenlokalität bleibt offen. `archive01:499–521` bestimmt B_Σ aus dem
   gegebenen D_coll, nicht als Identität mit dem DtN-Ansatz.
4. **Stationarität.** Jede selbstadjungierte Kompression `[[E0, κ], [κ*, E1]]` mit
   stationärem |vac⟩ hat κ = 0. Ein notwendiger κA + κ*B-Mischer widerspricht genau
   dieser Prüfbedingung. Ein quellenseitig geliefertes **diagonales** ε kann den
   zusätzlichen Nulleigenzustand anheben, ohne ρ_vac zu ändern; autonome Sprünge
   vom stationären Vakuum entstehen so nicht.
5. **Kein allgemeines No-go aus der Kompression.** P0 O P0 erfasst keine virtuellen
   diagonalen Verschiebungen über `Q = 1 − P0`. Dafür ist
   `P0 O Q (QKQ − E)^{−1} Q O P0` mit tatsächlichem Koeffizienten und angeregtem
   Spektrum nötig. M_f verlässt G0 und kann so beitragen. Das ist **nicht**
   berechnet, weil f selbst nicht aus der Quelle festgelegt ist.

## Was bestehen bleibt [E]

* **E1:** β liegt im D5-(Träger-)Faktor der Clock-Fixalgebra, ist q-neutral und
  orthogonal zum A3-Faktor.
* **E2:** In der unveränderten Quelle tragen alle Operatoren ganzzahlige
  Cartan-Ladungen. Direktes Mischen |vac⟩ ↔ e^β ist dort null.
* **E4:** Der einzige K-neutrale Ladungs-β-Mode ist `J^β_{−1}`.

## Originaldefinitionen von D_coll, A_E und Φ

| Objekt | Originalstelle | festgelegt | nicht festgelegt |
|---|---|---|---|
| D_coll | `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:478–495` | Seed-**Eingabe**: erster Ordnung, elliptisch, reflexionsregulär | der Operator selbst |
| B_Σ | `01_boundary_kernel_source.tex:499–521` | aus D_coll induziert | — |
| `B_{E_a} = σ^μ∇^{(a)}_μ + Φ_a` | `02_carrier_source.tex:1990–2000` | Determinantenklassen `(c₁L₂, c₁L₃) = (1,0)` (`:1960–1974`); `Ind B⁺_{E₂} = 1`, `Ind B⁺_{E₃} = 0`; leichte Nullmode Φ ∈ Γ(E₂) ≅ (1,2)_{1/2} | ∇^{(a)} jenseits der Klasse; Φ_a jenseits von `wind det Φ_a` |
| Familienverbindung | `01_boundary_kernel_source.tex:868`, `02_carrier_source.tex:1698–1720` | flach, `Hol ⊂ SU(3)_F`, nur Klasse [∇_F*] | Vertreter |
| Φ* im starren Tupel | `02_carrier_source.tex:3264, 3283` | „downstream … evaluated on that unique branch" | keine explizite Formel gefunden |
| U(1)-Randphase | Codex `UR.SEAM.V16_OPERATOR_PULLBACK.01` | Viertelphase α entlang q | — |

## Erste nicht festgelegte Quelleneingabe

Eine Wirkung auf G0, ob diagonal oder virtuell, braucht einen Koeffizienten entlang
einer Richtung, die β sieht (`y·β ≠ 0`). Die einzige festgelegte Randphase ist die
Viertelphase entlang q, und die ist β-blind (`q·β = 0`). Die Determinanten-U(1)s
sind nur durch ihre **Chernklassen auf der Normalkugel** festgelegt, nicht durch
ihre **Nahtholonomie** (den Nullmoden-Koeffizienten auf dem Nahtkreis). Unter Codex'
Rahmen `Mβ = e1 + e4` haben die Determinantenrichtungen von E₃ und E₂ jeweils
β-Eigenwert 1.

> **Erste nicht festgelegte Eingabe:** der Nullmoden-Anteil (die Nahtholonomie)
> der Trägerverbindung ∇^{(a)} entlang β-sichtbarer Cartanrichtungen, sowie Φ_a
> über die Determinantenwindung hinaus. Beide sind Teile des Seed-Datums D_coll,
> das das Original als Eingabe führt. Hinzu kommt der Koeffizient f des
> M_f-Ansatzes, dessen Markenlokalität offen ist.

Diese Fassung baut kein ε- oder κ-Modell und behauptet kein Ereignis-No-go.
