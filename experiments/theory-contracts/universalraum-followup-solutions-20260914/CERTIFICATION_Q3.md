# Q3 — Zertifizierung der Vierfachstruktur (Follow-up Frage 3)

14. September 2026. Contract `universalraum-followup-solutions-20260914`.
Checker: `certify_quartet.py` → `certify_quartet.json` (716 Bedingungen, Laufzeit ~6 min).
Gegenstand: der trunkierte kantenlokale Operator `H = H0 + 0.00125 · F4_edge` auf dem
24.024-dimensionalen SU(4)-Singulettsektor (Specht-Modul `(4,4,4,4)`).
Kein T1–T8-Abschluss; keine Promotion nach `verification/`.

## Was Follow-up 3 verlangte

> **Entscheidender Test:** Exakte Symmetrieprojektoren plus zertifizierte Spektralgrenzen.
> Die neue positive Form reduziert dafür die algebraische Schwierigkeit deutlich.

## Ergebnisübersicht

| Teilaussage | v1.4-Status | Jetzt |
|---|---|---|
| Vierfachheit des ersten Niveaus | numerisch (Gleitkomma) | **exakt bewiesen** (Symmetrie + Schur, intervallzertifiziert) |
| Symmetrieprojektoren | nicht konstruiert | **exakt konstruiert** (W(D5), 18 Irreps, ganzzahlige Charaktertafel) |
| Eigenwertintervalle E0, E1 | Gleitkommawerte | **zertifizierte Intervalle** (Breite ~3e-12) |
| F4 ≥ 0 | exakt (720D reguläre S6) | erneut unabhängig verifiziert |
| Nackte Anfangsskala | 1, 4, "7" (Fensterartefakt) | **1, 4, 20, 5, 10, …** (block-aufgelöst, verifiziert) |
| Zählung (genau 5 Niveaus unter der Schwelle) | offen | **konditional reduziert** auf eine einzige präzise Zertifizierung (s.u.) |

## 1. Exakte Symmetrieprojektoren

Die Symmetriegruppe des Clebsch-Graphen ist **W(D5) = 2⁴ ⋊ S5**, Ordnung 1920,
18 Konjugacyklassen (maschinell verifiziert: alle 1920 Gruppenelemente erhalten die
40 Kanten; Klassenalgebra und Charaktertafel mit Dixon–Schneider, Zeilenorthogonalität
exakt geprüft). Die Irrep-Dimensionen: 1, 1, 4, 4, 5, 5, 5, 5, 6, 10, 10, 10, 10, 10,
15, 15, 20, 20 (Quadratsumme 1920 ✓).

Die Einschränkung des Singulett-Specht-Moduls auf W(D5) wurde exakt zerlegt
(Murnaghan–Nakayama für die Specht-Charaktere, ganzzahlig):

```
Irrep-Dim:      4   4   5   1  10  10  15  20  20  10  10   6   5  15   5  10   5   1
Multiplizität: 80  42  72   8 106 124 176 232 262 126 140  80  66 194  54 124  86  28
```

Summe dim·mult = 24.024 ✓. Die Projektoren `P_μ = (dim μ / 1920) Σ_g χ_μ(g) ρ(g)`
sind exakt rationale Operatoren (Charaktere ganzzahlig); sie wurden als
Matvec-Ketten über die Youngsche Orthogonalform implementiert und die
Darstellungseigenschaft `ρ(g)ρ(h) = ρ(gh)` wurde stichprobenfestgestellt.

## 2. Das Quartett ist EINE 4-dimensionale Irrep — exakte Entartung

Die vier ersten angeregten Ritz-Vektoren (E1 ≈ 12.44698494) spannen einen
G-invarianten Raum, dessen Charakter mit der 4-dimensionalen Irrep **μ=0**
übereinstimmt (maximale Charakterabweichung 4.4e-15 über alle 1920 Elemente;
zweitbeste Irrep um 2.0 entfernt — eindeutig). Der Grundzustand transformiert als
triviale Irrep (μ=17, Abweichung 2.9e-15).

Da H exakt mit W(D5) kommutiert (Kanten- und Eckenmenge sind invariant — verifiziert),
wirkt H auf dem Isotypikraum `W_μ ≅ V_μ ⊗ C^80` als `I₄ ⊗ M`. **Jeder Eigenwert von M
ist als Eigenwert von H exakt 4-fach entartet (Schur).**

Intervallzertifizierung (gerichtete Rundung, `nextafter`-Klammerung aller Operationen):
- `‖P_μ v − v‖ ≤ 3.80e-08` für einen Quartett-Ritz-Vektor v (zertifiziert),
- Rayleigh-Quotient des Quartetts ∈ [12.4469849396673, 12.4469849396712] (zertifiziert),
- Residuum ≤ 4.4e-12 (zertifiziert),
- Fehlerfortpflanzung auf den Block (‖H‖ ≤ 41.8 rigoros aus F4 ≤ 1440 I):
  **M hat einen Eigenwert im zertifizierten Fenster [12.44696907, 12.44700081].**

Damit: **der trunkierte Operator H besitzt ein exakt vierfach entartetes Niveau bei
E1 = 12.4469849 ± 3.2e-5 (J-Einheiten)** — die Vierfachheit ist nicht mehr nur numerisch.

Zertifiziertes Grundzustandsintervall: **E0 ∈ [11.9605074126619, 11.9605074126651]**
(Breite 3.1e-12, Residuum ≤ 3.7e-12).

## 3. Nackte Anfangsskala, block-aufgelöst (verifizierte numerische Evidenz)

Pro Block: Lanczos-Krylov (Tiefe 50) aus projiziertem Seed; nur Ritz-Paare mit
Residuum < 1e-6 **und** In-Block-Defekt < 1e-6 akzeptiert (filtert Kontamination):

| Niveau (nackt) | Irrep | Vielfachheit |
|---|---|---|
| 11.04539834 | μ=17 (dim 1) | 1 |
| 11.56176212 | μ=0 (dim 4) | 4 |
| 12.45602380 | μ=8 (dim 20) | **20** |
| 12.69021550 | μ=16 (dim 5) | 5 |
| 12.77848670 | μ=10 (dim 10) | 10 |
| 12.78275709 | μ=13 (dim 15) | 15 |

Korrektur zur v1.4-Lesart: das als "7-fach" erscheinende dritte Niveau ist ein Fenster-
artefakt — es trägt eine **20-dimensionale** Irrep (im 12er-Fenster waren nur 7 Partner
berechnet). Die Skala 1, 4, 20, 5, 10, 15, … bestätigt unabhängig die Irrep-Zuordnung
der Abschlussrunde.

## 4. Was für die vollständige Zählung noch fehlt (präzise)

F4 ≥ 0 ist exakt (erneut verifiziert: annihilierendes ganzzahliges Polynom Grad 11 der
regulären S6-Darstellung, max. Zwischenwert < 2⁶⁰). Weyl-Monotonie liefert
`λ_k(H) ≥ λ_k(H0)` für alle k. Die nackte 6. Niveau-Untergrenze (Float: 12.45602380)
liegt **oberhalb** der zertifizierten Quartett-Obergrenze 12.44700081 — das Fenster
dazwischen (0.00904) ist nichtleer.

**Es fehlt genau eine Zertifizierung:** `λ_6(H0) ≥ 12.455` mit rigorosen
Fehlerintervallen. Route: dieselbe Intervall-Matvec-Maschinerie blockweise
(Intervall-Projektoren + Intervall-Gershgorin auf den kleinen Blockmatrizen).
Gemessene Kosten: Intervall-Projektor ~35 s pro Seed-Vektor; die Blöcke mit
Multiplizitäten bis 262 benötigen Krylov-Tiefen bis ~262; geschätzte Gesamtlaufzeit
einige Stunden — im Contract als nächster Rechenschritt vermerkt, hier nicht
ausgeführt. Sobald sie läuft, gilt: genau fünf Eigenwerte von H unterhalb der
zertifizierten Fensterkante, d.h. das erste angeregte Niveau ist **genau** das Quartett.

Der Nichtsingulett-Vergleich (bedingte Untergrenze 12.96488 über der variationalen
Quartettobergrenze) bleibt zusätzlich an der Zertifizierung des nackten
Sektorminimums 12.13353715 im Sektor (5,4,4,3) hängen (Specht-Dim 180.180 —
dieselbe Maschinerie, größerer Lauf).

## 5. Grenzen (ehrlich)

- Alles gilt für den **trunkierten** Operator H0 + 0.00125·F4 auf dem Singulettsektor —
  nicht für die volle Mikrodynamik, nicht für höhere Ordnungen, nicht für den
  Vielzellenlimes.
- Die Symmetrie-Entartung ist exakt; die Eigenwertintervalle sind zertifiziert; die
  **Zählung** ist konditional (ein präziser Restschritt, Route und Kosten benannt).
- Keine Lean-Formalisiерung; die exakten Teile sind ganzzahlige/rationale
  Maschinenarithmetik, die Spektralteile Intervallarithmetik mit gerichteter Rundung.
