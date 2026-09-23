# Abschluss Runde 2 (Fable), 10. September 2026

Keine weiteren Rechnungen ausgeführt; Stand = `BERICHT.md`, `theta_transfer.py`, `theta_checks.json`
(Lauf ≈ 2 s). Die vorangegangenen abgebrochenen Läufe waren zu langsame mpmath-Varianten
(`nsum`, unendliches Φ-Integral) und sind durch endliche Summen mit explizitem Abschneidefehler
ersetzt; offen bleibt nichts Numerisches, das für die Aussagen gebraucht würde.

## Eigene konzeptionelle Prüfung des Theta-Transfers (Kurzfassung)

- Elektrische Zustandssumme der neutralen Plaquette = Θ(2κβ/π); Jacobi-Inversion = Ladungs-/
  Windungsdualität; ξ(s) = 1/2 + s(s−1)/2·∫₁^∞[t^{s/2}+t^{(1−s)/2}]ψ dt/t für alle s (Polterme heben
  sich exakt); Normalisierung des positiven Kerns Ξ(z) = 4∫₀^∞Φ(u)cos(zu)du = 2∫_{−∞}^{∞}Φ cos.
  Elektrische Spektralzeta 2(2κ)^{−s}ζ(2s), kritische Linie Re s = 1/4. Alles klassisch.
- **Parent-Defekt (exakt, Ring):** m₁ = ε_LN + 2κn², zentrales m₂ = N_dir b² = 1/72,
  zentrales m₃ = 57497/1036800 = g²(h₁−h₀), beide n-unabhängig. Z_loop(β) = e^{−βε_LN}Θ(2κβ/π)
  ·[1 + β²N_dir b²/2 − β³m₃/6] + O(β⁴): nicht modular, keine ξ-Darstellung; sauberer relativer
  Gegenstand D(β) = Σ_n[⟨v_n,e^{−βH}v_n⟩ − e^{−βm₁(n)}]. Der Nullmodus leckt mit.
- Kein Positivitätsschritt; fehlender Satz: Reellität der Nullstellen von Ξ = 4∫₀^∞Φ cos ⟺ Λ = 0.

## Zum neuen Satz THERMISCHER-ANSCHLUSS.md (Codex)

Die Datei `/Users/stefanhamann/Documents/Codex/2026-09-10/scha/work/universalraum-dynamik-abschluss/THERMISCHER-ANSCHLUSS.md`
(ebenso `rh/THETA-TRANSFER.md`, `rh/REVIEW.md`) ist aus dieser Sitzung nicht lesbar („Operation not
permitted“). Ich beurteile daher nur die mitgeteilte Aussage: normale Gibbszustände des unveränderten
endlichen Parents → Hochtemperaturgrenzgang auf der Loop-affinen Algebra = kritischer arithmetischer
Zustand τ; jeder schwach*-Cluster H-stationär; uniformer Einzelanfragenfehler (7), Temperaturwahl (8).

Konsistenzbefund (kein Gegenbefund): Für den reinen elektrischen Anteil ist dies genau meine Straße
(iv) aus `fable/PROOF.md` Thm 5(e), ausgedehnt von der Diagonalalgebra auf die affinen Monomiale:
A(a,m,n,b) hat für m ≠ n höchstens einen Diagonaleintrag mit Gewicht → 0 (Gaußnormierung ∝ √(βκ)),
für m = n, a ≠ b keinen, für m = n, a = b die Restklassenprojektion mit Gewicht → 1/n (Poisson-Schranke
2Σ_k e^{−π²k²/(8βκ)}). H-Stationarität der Cluster folgt, weil jeder ρ_β stationär ist und Invarianz
für jede feste Observable schwach*-abgeschlossen ist. Ein Widerspruch zu meinen Ergebnissen liegt
nicht vor.

Zwei belegte Grenzen, die beim Lesen des Satzes festzuhalten sind (falls dort nicht schon enthalten):

1. **Produktstruktur statt Cap-Korrelation.** Auf zwei Plaquetten ist der Hochtemperaturgrenzwert auf
   der Loop-affinen Algebra ein Produkt τ⊗τ (die Gaußgewichte faktorisieren asymptotisch; Kopplungs-
   korrekturen sind O(√(βκ))). Damit ist τ⊗τ(S₁S₂⁻¹) = 0, während der präparierte Cap ⟨Ψ,S₁S₂⁻¹Ψ⟩ = 1
   hat (`fable/cap_dynamics.json → two_plaquettes`). Der thermische Anschluss reproduziert die
   Einschleifen-Marginale, nicht die Balancierung zwischen den Schleifen — konsistent mit dem
   Verzicht auf „Capreinheit“, aber als Zahl festgehalten.
2. **Energiekosten des Grenzwegs.** ⟨H_el⟩_β = 1/(2β) pro Rotor wächst im Hochtemperaturgrenzgang
   unbeschränkt, wie beim ζ-Weg (dort unendlich für β ≤ 3). Ein endlicher Fehlervertrag braucht
   deshalb die Temperaturwahl (8) bzw. die σ_K-Box (KRITISCHER-GRENZZUSTAND §5, Energie κK(K+1)/6).

## Quellenstand

Gelesen und gehasht: `QUELLEN.json` (RUNDE-2.md, fable/cap_dynamics.py, fable/PROOF.md,
context/aktuelle-runde/tfpt/ERWEITERUNG.md). Nicht lesbar: die drei genannten Codex-Pfade unter
`~/Documents/Codex/2026-09-10/scha/`. Keine alten Artefakte verändert, keine Indexaktualisierung.
