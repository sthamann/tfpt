# Runde 2 (Fable): elektrischer Theta-Transfer, Parent-Defekt, fehlender Satz

10. September 2026. Auftrag: `../RUNDE-2.md`. Kontrollen: `python3 -B theta_transfer.py` →
`theta_checks.json` (Laufzeit ≈ 2 s; mpmath-Numerik in A/B, exakte Fractions in C). Quellen und
Hashes: `QUELLEN.json`. **Kein RH-Beweis, keine Positivitätsquelle; A/B sind klassische
Identitäten (Riemann 1859), C ist eine exakte Rechnung am deklarierten Ring-Parent.**

Nicht lesbar (macOS „Operation not permitted“): `/Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/Universalraum-Konsolidiert-mit-Fable.md` und `…/Universalraum-Fable-Gegenpruefung.md`. Die dort genannten vier Restkorrekturen (Normfluss vs. f(E), Normabschluss, S_m-Norm) konnten deshalb nicht wörtlich übernommen werden; sie werden hier nicht bestritten.

## 1. Normalisierung, Konvergenz, Nullmodus, Vorarbeiten

Elektrische Abbildung. Auf einer neutralen Plaquette (Fluss n auf vier Links) ist H_el = (κ/2)·4n² =
2κn². Die Wärmespur ist Tr e^{−βH_el} = Σ_{n∈Z} e^{−2κβn²} = Θ(t) mit πt = 2κβ, also β = πt/(2κ)
(numerisch bis 10⁻¹⁸ geprüft). ψ = (Θ−1)/2 entfernt den Nullflussmodus (n = 0) und identifiziert die
beiden Schleifenorientierungen ±n. Die Jacobi-Inversion Θ(1/t) = √t·Θ(t) (Poisson) ist im Rotor die
Dualität Ladungs-/Windungsbasis (Fourier auf U(1)); sie gilt für den reinen Rotor exakt.

Mellin/ξ. Für Re s > 1 ist ∫_0^∞ ψ(t)t^{s/2}dt/t = π^{−s/2}Γ(s/2)ζ(s). Aufspaltung bei t = 1 und
Inversion auf (0,1) geben π^{−s/2}Γ(s/2)ζ(s) = −1/s − 1/(1−s) + ∫_1^∞[t^{s/2}+t^{(1−s)/2}]ψ(t)dt/t;
das Integral ist wegen ψ(t) = O(e^{−πt}) für **alle** komplexen s absolut konvergent (ganze
Funktion). Mit ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) heben sich die Polterme exakt:
½s(s−1)[−1/s − 1/(1−s)] = ½. Daher

    ξ(s) = 1/2 + s(s−1)/2 · ∫_1^∞ [t^{s/2} + t^{(1−s)/2}] ψ(t) dt/t,   ξ(0) = ξ(1) = 1/2, ξ(s) = ξ(1−s).

Geprüft an s ∈ {0, 1, 1/2, 3, −2, 1/4+3i, 2−5i, 1/2+iγ₁, 1/2+iγ₂}: Abweichung ≤ 6·10⁻²⁴ (Γ-Pole bei
s = 0, −2 über ξ(0) = 1/2 bzw. ξ(s) = ξ(1−s) behandelt); ξ(1/2) = 0.497120778188…; an den ersten
beiden Nullstellen |ξ| < 2·10⁻¹⁸. Normalisierungsbefund für den positiven Kern: mit Riemanns
Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}} gilt **Ξ(z) = ξ(1/2+iz) = 4∫_0^∞ Φ(u)cos(zu)du
= 2∫_{−∞}^{∞}Φ cos** (nicht 2∫_0^∞; der Faktor 2 wurde numerisch aufgedeckt und korrigiert), geprüft bei
z = 0, 5, γ₁ bis 10⁻⁸.

Elektrische Spektralzeta. Σ_{n≠0}(2κn²)^{−s} = 2(2κ)^{−s}ζ(2s): Die Mellin-Transformierte der
Zustandssumme in β ist Γ(s)·2(2κ)^{−s}ζ(2s); die Nullstellen der elektrischen Spektralzeta liegen bei
s = ρ/2, ihre kritische Linie ist Re s = 1/4. Das ist eine Umskalierung, kein neuer Inhalt.

Vorarbeiten im Graphen (rhcat): r116–r171 `toproot_theta_probe` (KILLED, WORLD_BLIND), r131–r174
`thetainf_pin_probe` (MEASURED), r618 (Jensen/Xi-Seite ist RH-äquivalent; E8-Daten RH-neutral),
Kills MELLIN.COFACTOR.* (Laguerre–Pólya-Klasse nicht anwendbar). Nichts hier ist neu gegenüber der
Literatur.

## 2. Parent-Defekt: der niedrigste Wärme-/Momentendefekt, exakt

Schleifenfamilie v_n = W^nΩ₀ (Ring, alle L besetzt, Fluss n auf vier Links). Exakt (Fractions):

    m₁(n) = ⟨v_n,Hv_n⟩ = ε_L N + 2κn²                     (diagonal, der elektrische Wert plus Konstante)
    m₂ᶜ(n) = ⟨v_n,(H−m₁)²v_n⟩ = N_dir b² = 1/72          (Leck-Satz, Flussbasis; unabhängig von n)
    m₃ᶜ(n) = ⟨v_n,(H−m₁)³v_n⟩ = 57497/1036800             (unabhängig von n; = g²·(h₁−h₀)_aa mit g² = 1/72
                                                            und 57497/14400 aus dem Krylov-Block, fable/PROOF Thm 2b)

Die n-Unabhängigkeit von m₃ᶜ auf dem Ring kommt daher, dass beide Orientierungen jedes Links im
Leckvektor vorkommen und die linearen E-Terme sich paarweise aufheben (dieselbe Beobachtung wie in
ERWEITERUNG §2 für h₁). Damit ist die Rückkehrfunktion der Schleifenfamilie

    Z_loop(β) := Σ_n ⟨v_n, e^{−βH} v_n⟩
              = e^{−βε_L N} Θ(2κβ/π) · [1 + (β²/2)·N_dir b² − (β³/6)·m₃ᶜ] + O(β⁴),

d.h. Θ mal einem n-**unabhängigen** Korrekturfaktor durch Ordnung β³. Der niedrigste Defekt ist die
Ordnung β² mit Koeffizient N_dir b²/2 (Ring 1/144, Torus N/192). Folgen:

- Z_loop ist **nicht modular**: Θ(t)·C(β(t)) erfüllt die Jacobi-Inversion nicht (der LH-Kanal
  koppelt Fluss an Materie und bricht die Ladungs-/Windungsdualität). Es gibt daher keine
  ξ-Darstellung der tatsächlichen Parent-Rückkehrfunktion; nur der reine elektrische Faktor besitzt
  sie.
- Der einzige vollständig definierte relative Gegenstand ist
  D(β) = Σ_n[⟨v_n,e^{−βH}v_n⟩ − e^{−βm₁(n)}] (konvergent: auf endlichem Träger ist H ≥ H_diag − ‖H_hop‖,
  also jeder Summand ≤ e^{−β(E_n−‖H_hop‖)}); D(β) = e^{−βε_LN}Θ(2κβ/π)[(β²/2)N_dir b² − (β³/6)m₃ᶜ] + O(β⁴).
  D misst den Materie-Ausgang; „Θ herausdividieren“ ist jenseits der berechneten Ordnungen keine
  definierte Operation und wird nicht vorgenommen. Keine Positivitätsquelle, keine Subtraktion.
- Auch der Nullmodus leckt (n = 0 mit demselben N_dir b²): Der Vakuumfluss ist im Parent kein
  stationärer Zustand; ψ = (Θ−1)/2 kann im Parent nicht durch „Nullmodus abziehen“ gerechtfertigt
  werden, sondern nur für den reinen elektrischen Faktor.

Torusübertragung: m₂ᶜ = N/96 ist bewiesen (Theorem 1, Flussbasis); m₃ᶜ = g²(4 + κ/2 − 11c) folgt aus
ERWEITERUNG §2, wurde hier nicht auf dem Torus nachgerechnet.

## 3. Schritt zum globalen Positivitäts-/Spektralproblem?

Kein solcher Schritt. Was vorliegt: Φ(u) > 0 (auf dem Gitter u ∈ [0,2] geprüft, klassisch bewiesen),
Φ gerade, Φ(u) = O(e^{9u/2}e^{−πe^{2u}}), Ξ(z) = 4∫_0^∞Φ cos(zu)du. In elektrischer Sprache ist Φ > 0
die Positivität der symmetrisierten Wärmedaten zweiter Ordnung, 4 d/dt[t^{3/2}ψ'(t)] > 0 — sie ist der
klassische **Eingang** in Pólyas Problem, nicht ein Schritt zu dessen Lösung. Positiver Kern und
Funktionalgleichung zusammen liefern Ξ gerade und reell auf R, nichts über die Lage der Nullstellen.

Der exakt fehlende Satz: **Die Kosinustransformierte Ξ(z) = 4∫_0^∞Φ(u)cos(zu)du hat nur reelle
Nullstellen** — äquivalent: die de-Bruijn–Newman-Konstante ist Λ = 0. Bekannt sind Λ ≥ 0
(Rodgers–Tao 2020; aus Λ < 0 folgte eine Störungsstabilität, die falsch ist), Pólyas Resultat, dass
die endlichen Approximationen von Φ reelle Nullstellen-Transformierte haben, und die Turán-Typ-
Ungleichungen für Φ (Csordas–Norfolk–Varga). Alle diese Eigenschaften sind notwendig oder
begleitend, keine ist hinreichend; keine folgt aus dem Rotor, und der Rotor liefert keine zusätzliche
Struktur auf Φ (er liefert exakt Θ und nichts weiter). Endliche Stichproben (ξ an neun Punkten,
Nullstellen γ₁, γ₂) sind Kontrollen der Identitäten und keine Evidenz für RH.

## Ergebnis in einem Absatz

Der elektrische Theta-Transfer ist exakt der klassische Riemann-Transfer: die Zustandssumme der
neutralen Plaquette ist Θ, die Jacobi-Inversion ist die Ladungs-/Windungsdualität, die Mellin-
Transformierte liefert ξ(s) = 1/2 + s(s−1)/2∫_1^∞[…]ψ dt/t für alle s, und der positive Kern
normiert sich zu Ξ = 4∫_0^∞Φ cos. Der vollständige Parent liefert diese Θ nicht: Seine Schleifen-
Rückkehrfunktion ist Θ mal einem durch Ordnung β³ exakt berechneten, n-unabhängigen Korrekturfaktor
(1 + β²N_dir b²/2 − β³m₃ᶜ/6, Ring: 1/144 und 57497/6220800), ist nicht modular und hat keine
ξ-Darstellung; der einzige saubere relative Gegenstand ist D(β). Ein Schritt zur globalen Positivität
existiert in dieser Konstruktion nicht; der fehlende Satz ist die Reellität der Nullstellen der
Kosinustransformierten von Φ (Λ = 0).

## Reproduktion

    cd fable-runde2 && python3 -B theta_transfer.py        # theta_checks.json, ~2 s CPU
