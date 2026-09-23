# TFPT/Universalraum v1.4 — Follow-up Q2: Entscheidungs­matrix der Bauweise

14. September 2026. Maschinengeprüfte Entscheidung zu Q2
(*„Welche Bauweise ist wirklich vorgeschrieben?“* — zellgeteilte Vermittlerbank
vs. kantenlokale Vermittler), gemessen an **identischen** Quellen­anforderungen
R1–R6. Keine T1–T8-, RH- oder Komplexitäts­promotion; keine Veröffentlichung.

Prüfer: `architecture.py` (Standalone Python 3, nur numpy/scipy/sympy).
**31 Bedingungen**, normal/`-OO` bytegleich, `checker_sha256` verifiziert.
Ausgabe: `architecture.json` (indent=2, sort_keys=True).

## 1. Die 6×2-Entscheidungs­matrix

| Anforderung | Zellgeteilte Bank (`cell_shared`) | Kantenlokal (`edge_local`) |
|---|---|---|
| **R1** E8-Diagonal­vorzeichen­adapter (F2) | **fail** · exact — geteilte diagonale ±1-Gauge **unlösbar** (F2-System hat keine Lösung, Rang 84; Seiten-Farb-Antisymmetrie-Rang 45) | **pass** · exact — kantenlokaler Adapter lösbar, Rang **285** (Seiten-Farb-Rang 45) |
| **R2** Mikroskopische Stern­vermittler­zählung (288-dim) | **n/a** · exact — der 288-dim Stern­index ist kantenlokal (pro Arm); die Zellbank trägt 60L label-geteilte innere Paarterme (siehe R3) | **pass** · numerical — 288 = 3×16×6 (pro Arm: 96 = 16×6); Gram-Identität ‖MᵀM − (6I₂₅₆ − 2G)‖ = 0 < 1e−13, G = Σⱼ (I+S₀ⱼ)/2 |
| **R3** E8-adjungierte Wurzel­zählung (Clebsch) | **tension** · exact — 40 Kanten, 10 Labels, 4 Kanten/Label; Sektor (10,6) = 60 = 10×6 Wurzeln legt label-GETEILTE Moden nahe (passend zur Zellbank 60L), aber diagonal F2-obstruiert (R1); nicht­diagonale/komplexe Adapter offen | **pass** · exact — gleiche Graph­fakten; kantenlokale Stern­zählung (288 pro Zelle, R2) ist F2-lösbar (R1); label-geteilte Lesart diagonal obstruiert, bindet aber den Kanten­vertrag nicht |
| **R4** Bandtrennung (exakte rationale LDL-Pivots, ε=1/20) | **pass** · exact — **0.4Δ** zertifiziert; alle 8 Pivots positiv (Fraction-Arithmetik), a²=(80,248,432,544,480,336,224,64) | **pass** · exact — **0.7Δ** zertifiziert; alle 8 Pivots positiv, a²=(80,124,144,136,120,84,56,16); 0.8Δ-Versuch scheitert am 2. Pivot (Negativ­kontrolle, Pivot 2 = −7/20) |
| **R5** Gap-Korrektur ε²-Vorzeichen (zitiert) | **pass** · quoted — Koeffizient **+13.901769151274** (positiv); Quelle `spectrum_followup.json:gap_epsilon2_coefficients[0]` | **pass** · quoted — Koeffizient **−11.955494211502** (negativ); Quelle `spectrum_followup.json:local_gap_epsilon2_coefficients[0]` |
| **R6** F4-Positivität (exaktes 720-dim regülär-S₆-Zertifikat) | **fail** · exact — keine analoge positive lokale F4-Form bekannt; Quartic-Korrektur hat entgegengesetztes Gap-Vorzeichen (R5, +13.90) | **pass** · exact — F4 = Σᵥ Aᵥ(Aᵥ−I) ≥ 0 als Vollraum-Operator; exakt Π₍ₖ₌₀..₁₀₎(A−kI)=0 (int64, größtes Zwischen­glied 18480); Schranke F4 ≥ H₀² − 76H₀ + 1440I |

## 2. R1 — die stärkste Quellen­differenzierung (F2-Systeme)

Unabhängig rekonstruiert aus `phase_car.py:lattice()` (Standard-E8-Gitter­cocycle
ε(m,n) = (−1)^(mᵀBn), 240 Wurzeln, 8 einfache Wurzeln, Gram B-Matrix):

- **Seiten-Farb-Antisymmetrie:** Rang **45** (lösbar). Beide Architekturen
  erfüllen diese gemeinsame Vorbedingung.
- **Geteilte diagonale ±1-Gauge (zellgeteilte Bank):** F2-System **unlösbar**
  (keine Lösung; Rang 84). Das ist die zentrale Obstruktion: eine diagonale
  ±1-Gauge, die gleiche Vermittler­moden über die Kanten einer Zelle teilt,
  verträgt sich nicht mit dem Standard-Gitter­cocycle.
- **Kantenlokaler Adapter:** lösbar, Rang **285**. Pro Kante ein eigener
  ±1-Gauge-Freiheitsgrad; das F2-System ist konsistent.

Dies ist die stärkste Quellen-abgeleitete Unterscheidung: Lokalität allein
wählt nicht (beide Architekturen sind bei fester Zellgröße lokal), aber die
Diagonal-Gauge-Anforderung an den Standard-Cocycle schließt die Zellbank aus.

## 3. R2 — mikroskopische Stern­vermittler (288-dim, kantenlokal)

Rekonstruiert aus `frontier.py:record_and_state` (Mediator-Block). Schlüssel
(j, Materie-mit-0-und-j-geleert, ungeordnetes Paar), j ∈ {1,2,3}:

- **288 = 3 × 16 × 6** pro Zelle, pro Arm: 96 = 16 × 6
  (16 verbleibende Materie-Konfigurationen, 6 ungeordnete Paar-Farben).
- **Gram-Identität:** MᵀM = 6I₂₅₆ − 2G mit G = Σⱼ₌₁..₃ (I+S₀ⱼ)/2,
  numerischer Fehler 0 < 1e−13.

Diese Zählung ist **kantenlokal** (pro Arm). Die zellgeteilte Bank trägt statt
dessen 60L label-geteilte innere Paarterme — R2 als gestellte Anforderung
testet die Kanten­architektur; die Zellbank-Analogie wird in R3 gezählt.

## 4. R3 — E8-adjungierte Wurzeln und die Spannung

Clebsch-Graph (16 Seiten, gerade Parität in {±1}⁵):

- **40 Kanten** (Paare, die in genau 4 Koordinaten differieren),
- **10 Bindungs-Labels** ±eₖ, jedes getragen von **genau 4 Kanten**,
- Sektor (10,6) = **60 = 10 × 6** Wurzeln.

Die Spannung ist jetzt präzise: Die E8-adjungierte Zählung legt **label-geteilte**
Moden (60) nahe, was der zellgeteilten Bank-Zählung (60L) entspricht — aber
genau diese label-geteilte diagonale Gauge ist in R1 F2-obstruiert. Die
mikroskopische Stern­zählung ist **kantenlokal** (288 pro Zelle, R2) und
F2-lösbar. **Nicht-diagonale oder komplexe Adapter bleiben offen** — R3
löst die Spannung nicht nativ auf, sondern benennt sie.

## 5. R4 — Bandtrennung (exakte rationale LDL-Pivots)

Bei |t|/Δ ≤ 1/20, mit Fraction-Arithmetik (keine Gleitkomma-Näherung):

**Zellgeteilt, 0.4Δ** — Pivots alle positiv:
3/5, 17/30, 59/85, 484/295, 4681/1210, 125986/23405, 292286/44995,
5535436/730715. a² = (80, 248, 432, 544, 480, 336, 224, 64).

**Kantenlokal, 0.7Δ** — Pivots alle positiv:
3/10, 4/15, 19/20, 559/190, 23467/5590, 616006/117335, 38644109/6160060,
2818555933/386441090. a² = (80, 124, 144, 136, 120, 84, 56, 16).

**Negativ­kontrolle, kantenlokal 0.8Δ** — scheitert am 2. Pivot (−7/20 ≤ 0).
Beide Architekturen bestehen R4; die Bandtrennung allein wählt nicht, aber der
kantenlokale Satz ist stärker (0.7Δ vs. 0.4Δ).

## 6. R5 — Gap-Korrektur-Vorzeichen (zitiert)

Aus `spectrum_followup.json` (zitiert, nicht neu gerechnet):

- Zellgeteilt: **+13.901769151274** (positiv — Gap öffnet),
- Kantenlokal: **−11.955494211502** (negativ — Gap schließt).

Beide bestehen R5 (die Koeffizienten sind verifizierte Quellenwerte), aber das
Vorzeichen unterscheidet sich. R6 verlangt eine positive lokale F4-Form; nur die
kantenlokale Architektur liefert sie.

## 7. R6 — F4-Positivität (exaktes 720-dim regülär-S₆-Zertifikat)

Rekonstruiert aus `spectral_algebra.py:run`. Für die **kantenlokale** Form:
Aᵥ = Σ_{e∋v}(I−S_e), A = Σ_e E_e. Dann exakt

F4,edge = Σᵥ Aᵥ(Aᵥ − I) ≥ 0

als Vollraum-Operator. Begründung: In der treuen 720-dimensionalen regülären
S₆-Darstellung wurde die ganzzahlige Identität Π₍ₖ₌₀..₁₀₎(A−kI) = 0 exakt
geprüft (int64, größtes Zwischen­glied 18480 < 2⁶⁰). Also A ≥ 0 und sein
Spektrum ganzzahlig 0..10, folglich A(A−I) ≥ 0. Zusätzlich die Schranke
F4,edge ≥ H₀² − 76H₀ + 1440I.

Für die **zellgeteilte Bank** ist keine analoge positive lokale F4-Form bekannt;
ihre Quartic-Korrektur hat das entgegengesetzte Gap-Vorzeichen (R5, +13.90).

## 8. Geltungs­bereich und offene Klassen

Die Entscheidung ist auf die **erklärte Quellen­klasse** beschränkt:
*Standard-diagonaler E8-Gitter­cocycle + mikroskopische Stern­vermittler­zählung
+ positive lokale F4-Anforderung*.

**Offen (nicht durch diese Matrix entschieden):**

- Nicht-diagonale oder komplexe E8-Vorzeichen-Adapter (R3-Spannung),
- nativer Clock-Lift / Transport zur TFPT-Quellbasis,
- thermodynamischer / Vielzell-Wechselwirkungs­limes des Bandabstands,
- kanonischer H6-Rest und zertifizierte nackte C16-Untergrenzen.

## 9. Entscheidungs­block (maschinengeprüft)

> Within the declared source class (standard diagonal E8 cocycle +
> microscopic star mediator counting + positive local F4 requirement),
> the edge-local architecture is selected; the cell-shared bank fails R1
> (F2 obstruction) and lacks R6; locality alone selects neither (both pass
> extensivity); the label-shared reading of the E8 adjoint roots (R3) is
> obstructed for diagonal gauges — native resolution of this tension
> remains open.

Zusammenfassung der Matrix-Ergebnisse (pass/fail/tension/n/a):

- **R1:** cell fail / edge pass — stärkste Differenzierung (F2-Obstruktion).
- **R2:** cell n/a / edge pass — 288-dim Stern ist kantenlokal.
- **R3:** cell tension / edge pass — label-geteilte Lesart diagonal obstruiert.
- **R4:** cell pass (0.4Δ) / edge pass (0.7Δ) — beide trennen; Kante stärker.
- **R5:** cell pass (+13.90) / edge pass (−11.95) — zitiert, Vorzeichen verschieden.
- **R6:** cell fail / edge pass — nur Kante hat positive lokale F4-Form.

Damit wählt die Quellen­klasse die **kantenlokale Architektur**; die
zellgeteilte Bank scheitert an R1 (F2) und R6 (keine positive lokale F4-Form).
Lokalität allein wählt keine der beiden (beide sind extensiv und lokal bei
fester Zellgröße). Die label-geteilte Lesart der E8-adjungierten Wurzeln (R3)
ist für diagonale Gauges obstruiert — die native Auflösung dieser Spannung
bleibt offen.

Prüfer-Hash: `a308903a5d07e5831764b1a461a17b38864e82da18431880c49ba9ac1bb54776`
(31 Bedingungen, normal/`-OO` bytegleich).
