# Liefert ein Originalterm eine Ereigniswirkung auf dem neutralen Dublett?

Anschluss an `UR.SEAM.JOINT_WARD_STATE.01` (Codex, lokal): Mit erhaltener
Komposition C = g², Quellenladung q und Paket nur mit Determinantenanteil folgen die
s-Erweiterung, das Minimalpaket m_A und das neutrale, spektral geflossene
SU(2)₁-Dublett auf `G0 = span(|vac⟩, e^β)` mit `β = p* = (½⁴, −½⁴)` und
`K|G0 = 0`. Vollständige Ward-Daten wählen die Anfangsdichte `ρ = |vac⟩⟨vac|`.

## Ursprüngliche Terme

1. **Hauptsymbol und Subprinzipalteil der Naht-DtN.**
   `Λ_Σ = |k| + M_f`, `⟨n|M_f|n'⟩ = f_{n−n'}`, wobei M_f die Multiplikation mit der
   Krümmung f(θ) ist, skalar in den inneren Indizes. Markenlokal heißt: f hat
   Fourierträger nur auf n ≡ 0 (mod 4).
   Quellen: `tfpt_research_contracts.tex:474–484`, `:491`, `:724–726`;
   `origin_theory.tex:1768–1772`, `:1845`.
   Zweitquantisiert: `M_f ↦ Σ_l f_{4l} J^q_{4l}`, eine Kopplung allein an die
   Ladungsdichte. Bei Z4-invariantem f ist sie auf allen acht Faltungsbögen
   gleich und in den Kanälen diagonal.
2. **Träger-/Familienverbindung (Paket).** `A_W = ρ(A_E)⊗I₄ + I₁₆⊗M_m tr A_E`
   (`source-boundary-lift-selection-20260922/PROOF.md` (1)). Familie nur über die
   Spur, also nur Cartan. Der Träger-Repräsentant ist zerlegt,
   `E = C³ ⊕ (L ⊕ C)` (`source-joint-spin-family-lift-20260922/PROOF.md` §4):
   eine diagonale Verbindung ohne Wurzelkomponenten.
3. **Φ.** `D_{m,Φ} = c∘∇ + Φ` (`source-boundary-lift-selection/PROOF.md:54–56`):
   „Weder S, der Zusatzterm Φ, CAR-Statistik noch ein Quantenzustand werden durch
   (1) neu hergeleitet." Das Original legt **kein** Φ fest.

## Satz E [E]

* **E1:** β liegt im D5-Faktor (Träger) der Clock-Fixalgebra, ist q-neutral und
  orthogonal zum A3-Faktor und zu beiden q-Projektionen. Das gilt für alle acht
  Kleidungen und α = ¼, ¾.
* **E2 – Cartan-Ganzzahligkeit:** Jeder Operator der rohen Quelle, ob
  CAR-Polynom, |k|, M_f, Paketverbindung oder ein Ein-Teilchen-Φ, trägt einen
  ganzzahligen Ladungsvektor n ∈ Z⁸. β ist halbzahlig. Also gilt
  `⟨e^β|O|vac⟩ = 0` für **alle** Originaloperatoren.
* **E3:** Ladungsneutrale Moden `H^y_n` verschieben K um −n. Nur n = 0 bildet G0
  in sich ab, und zwar als `diag(0, y·β)`. Für M_f ist y = q, also
  `M_f|G0 = diag(0, 0) = 0`. Markenlokale Moden n = 4l ≠ 0 verlassen G0.
  Die Paket-Cartanrichtungen sind orthogonal zu β (E1), wirken also ebenfalls
  mit Eigenwert 0.
* **E4:** Moden mit Ladung β, `J^β_n`, verschieben K um `−n + δ·β = −n − 1`. n = −1
  ist der einzige K-neutrale Mode. Jeder K-neutrale Operator mit Ladung β wirkt
  auf G0 als Vielfaches von `A = J^β_{−1}`; z. B. ergibt
  `J^β_0 H^y_{−1}` den Faktor `−(y·β)`. In Kopplungssprache ist A genau
  `∮ z^{−1} J^β(z) dz`: das **Residuum** einer Verbindung entlang der Wurzel β.

**Folgerung.** Alle ursprünglichen Terme (DtN-Hauptsymbol, Subprinzipalteil M_f,
Paketverbindung, jedes Ein-Teilchen-Φ) wirken auf G0 diagonal, M_f sogar als null.
Sie erhalten `ρ = |vac⟩⟨vac|` und erzeugen **keine Ereignisse** auf dem Dublett.

## Erste zusätzlich nötige Wahl

Eine Ereigniswirkung auf G0 verlangt einen Kopplungskoeffizienten κ mit
`H_ev|G0 = κ A + κ̄ B`, also ein Residuum der Trägerverbindung entlang der
Spinorwurzel β ∈ D5. Das ist die Ladungs-β-Wechselwirkung, eine Komponente der
E8-Erweiterung selbst. Kein Original liefert κ: Die Paketverbindung ist zerlegt
und diagonal, M_f ist skalar, Φ ist offen gelassen. Die vorhandenen Fuchs-Residuen
(`tfpt_1_architecture_e8.tex:3510–3517`, Spektrum {0, ⅓, ⅔}) sind die
SU(3)-Flavormonodromie auf H₁ (`origin_theory.tex:1210–1218`), nicht eine
D5-Spinorwurzel.

**Benannte Zusatzwahl:** ein von null verschiedenes Residuum κ der Trägerverbindung
entlang β, dazu seine Phase. Die Quelle müsste dafür eine Kopplung mit
halbzahligen Cartan-Ladungen liefern, die es in der unveränderten CAR-Quelle nicht
gibt (Codex, `UR.SEAM.QUOTIENT_LOCALITY_E8.01`). Ohne neue Quellendaten ist das
Dublett unter allen Originaltermen ein stationärer, nicht angeregter Speicher.
