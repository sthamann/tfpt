# Ergebnisse der Fable-Runde (Claude Fable 5.1, 10. September 2026)

Auftrag: BRIEFING.md. Ausgeschriebene Beweise: `PROOF.md`. Exakte Kontrollen:
`python3 -B checks.py` → `checks.json` (normal und `-OO` bytegleich). Quellen mit
SHA-256: `QUELLEN.json`. Keine RH-Aussage, kein Faktorisierungs-Geschwindigkeitsvorteil,
kein TOE-/T1–T8-Abschluss; Quelle und Kopplungen werden nicht aus P1/P2 hergeleitet.

## Ergebnisabsatz in einfachen Worten

Der vorgeschlagene physische Cap (16 Zustände aus zwei Plaquetten-Verschiebern über dem
All-Low-Zustand) ist unter der echten Dynamik nicht geschlossen — und zwar aus einem
einfachen, allgemeinen Grund: Jede Konfiguration mit „alle L besetzt, alle H leer“ kann
unter dem Hamiltonoperator nur eines tun, nämlich ein L-Teilchen in einen H-Nachbarn
hüpfen (Koeffizient b = 1/24). Alle anderen Terme sind durch Pauli blockiert oder
diagonal. Deshalb ist die Leckage exakt b² mal Zahl der gerichteten Links, für **jeden**
Flusscode, unabhängig von seinem Flussinhalt: auf dem kubischen Torus N/96 (Codex-Wert
bestätigt), auf dem Viererring 1/72 (exakt nachgerechnet). Ein endlicher Code mit festem
Materiemuster kann daher nie invariant sein, und mit wachsendem Volumen wird es schlimmer,
nicht besser.

Die konkret nächstgrößere Konstruktion habe ich gebaut: den Cap **durch die Quelle selbst
ankleiden** (Schrieffer–Wolff erster Ordnung, keine gewünschte Antwort eingesetzt). Der
angekleidete Code bleibt exakt orthogonal, trägt 8.7·10⁻⁴ H-Beimischung und leckt nur noch
3.32·10⁻⁵ statt 1.39·10⁻² — Faktor 418, für alle vier Codevektoren gleich. Der Rest kommt
daher, dass das durch die Beimischung erzeugte L-Loch mit dem großen Koeffizienten a = 1/12
weiterhüpft: Die angekleidete Anregung ist beweglich. Ein exakt geschlossener endlicher
Code mit kommutierender Z₄-Markierung existiert deshalb nicht; die Markierungen müssen
mitgeführt werden (Heisenberg-Transport wie in Q057). Das ist die korrigierte, konstruktive
Antwort auf Kandidat B: angekleideter Code + mitgeführte Marken, mit exaktem Fehlervertrag.

Zu den Primzahlen: Die Kreisüberlagerungen z ↦ zᵐ sind auf Plaquettenschleifen tatsächlich
gaugeinvariante Isometrien, komponieren multiplikativ, werden von den Primzahlen erzeugt und
kosten Energie m² (Energie ist quadratisch in der Ladung). Die vier Cuntz-Isometrien
T_r = Uʳ S₄ sind genau die Radixzerlegung des Rotors aus Kandidat A; der dortige Übertrag
ist ein kontrollierter Shift, und der Z₄-Layer hat eine vom Übertragsregister abhängige
Taktfrequenz (Kopplungsterm 8QR, exakte Konjugationsformel). Der scheinbare Widerspruch
„ζ-Gibbs gibt dem 0-mod-4-Sektor 4^{−β}, nicht 1/4“ löst sich exakt: Für β → 1⁺ gehen alle
vier Restklassenmassen gegen 1/4 (Abweichung 0.40 → 5.7·10⁻⁵ von β = 2 bis 1.0001). Der
gleichgewichtete Frobenius-/Cap-Zustand ist genau der kritische Bost–Connes-Zustand
(Haar-Maß auf Ẑ), und die ζ-Gibbs-Restklassenverteilung ist die Familie μ_s des Reports
(§7.1) mit s = β. Arithmetische Zeit (log n) und elektrische Zeit (κE²/2) sind auf dem
Schleifensektor Funktionen derselben Ladung, H_E = (κ/2)e^{2H_log}: gleiche Eigenbasis,
inkompatible Gibbs-Zustände — keine Uhrenumparametrisierung macht sie gleich.

Zu Kandidat D: Die modulare Multiplikation U_a ist die Reduktion der Überlagerung S_a auf
die Z_N-Uhr. Übertrag (A), Überlagerung (C) und U_a (D) sind **eine** Operationsklasse:
flusskontrollierte Schleifenoperationen Σ_Φ |f(Φ)⟩⟨Φ|. Genau diese Klasse enthält der native
Generator nicht (er hat nur W^{±1} mit festen Koeffizienten und Funktionen von E). Für
N = 91, a = 2 braucht U_a 91 verschiedene kontrollierte Schleifenpotenzen oder O(log N)
kontrollierte Multiplikationen mit Zusatzregister — das ist Shor mit identischer
Kostenrechnung. Ein neuer arithmetischer Reader ergibt sich daraus nicht.

## Exakte Zahlen (alle in checks.json)

| Größe | Wert |
|---|---|
| Leckage Flusscode, Viererring (N_dir = 8) | Γ*Γ = 8b² = 1/72 (beide getesteten Codes) |
| Leckage Flusscode, kubischer Torus | 6N b² = N/96 |
| [H_E, S] Ω₀ | 4e·SΩ₀ = (1/50)·SΩ₀ |
| angekleideter Code: Restleckage | 3.3227·10⁻⁵ … 3.3231·10⁻⁵ (Faktor 418.0) |
| davon ein-H / zwei-H / reiner Fluss | 1.81·10⁻⁵ / 1.51·10⁻⁵ / 9·10⁻¹² |
| H-Beimischungsgewicht | 8.70·10⁻⁴ |
| Konjugationsgesetz Z₄-Layer | Ad(L) = L·exp(−itκ(2Eδ+δ²)/2), δ ∈ {1, −3} |
| Überlagerungen | S_mU = UᵐS_m, ES_m = mS_mE, E²S_m = m²S_mE², S_mS_k = S_{mk}, Cuntz T_r |
| ζ-Gibbs mod 4, β = 1.0001 | (0.24997, 0.25006, 0.25000, 0.24998) |
| U₂ auf Z₉₁ | Ordnung 12, Zyklen {1, 3, 12}, F U₂ F* = U₂⁻¹, 91 kontrollierte Shifts |

## Einordnung gegenüber dem Codex-Stand

- Bestätigt: Γ†Γ = 6N b² I₁₆ (Codex) — als allgemeiner Satz für alle Flusscodes bewiesen,
  mit Erklärung (Pauli-Blockade) und unabhängiger exakter Ringkontrolle.
- Neu: der angekleidete Code mit exaktem Restvertrag; die Nicht-Symmetrie der Marken als
  exakte Formel; der Z₄-Layer als gefaserter Faktor; die Identifikation Cap-Zustand =
  kritischer Bost–Connes-/Haar-Zustand = μ₁ des Reports; die gemeinsame Operationsklasse
  „flusskontrollierte Schleifenoperation“ für A, C, D mit Kostenrechnung.
- Konsistenz mit `det-wall-hh-rule` und `TFPT-Globaler-Quellabschluss`: dort Onsite-
  Prämisse ⇒ h_HH = 0 bzw. relative Positivität + Budget ⇒ D = 4I; hier zeigt die
  Leckrechnung, dass der H-Sektor dynamisch nur als angekleidete Buchhaltungsmode auf der
  mobilen L-Bande mitgeführt werden kann — dasselbe Bild von drei Seiten.

## Korrekturen zu meiner früheren Antwort (wie im Briefing verlangt)

- „Faktorisierung ist nicht NP-vollständig“ → korrekt ist: Faktorisierung ist nicht als
  NP-hart bekannt (sie liegt in NP ∩ coNP); ein schneller Faktorisierer würde P vs NP
  nicht entscheiden. Keine allgemein bewiesene Nicht-Vollständigkeit behauptet.
- „Der Universalraum bietet keine Positivitätsquelle für RH“ → präziser: In den geprüften
  Konstruktionen (gcd-Kern, GNS-Transport, Cap, Überlagerungen, physische Normen) wurde
  keine Positivitätsquelle für die signierte Weilform identifiziert; das ist kein Verbot
  künftiger Konstruktionen. Endliche/Fenster-Numerik ist keine Positivitätsquelle.
- „P vs NP ist nicht adressierbar“ → präziser: aus den vorliegenden Codeklassen und
  Ressourcenverträgen folgt keine modellunabhängige Untergrenze; damit ist nichts über
  P vs NP gezeigt, in keiner Richtung.

## Offene Restvoraussetzungen (präzise)

1. Dynamische Auswahl des kritischen Punkts β = 1 aus der Quelle (sonst ist Cap ↔
   Bost–Connes eine kinematische Identifikation).
2. Ein nativer Mechanismus für flusskontrollierte Schleifenoperationen mit kontrollierten
   Kosten; ohne ihn kein Reader jenseits von Order-Finding.
3. Exakt invariante Cap-Erweiterung mit kommutierender Markierung: für feste Materiemuster
   ausgeschlossen; für zeitabhängige/vergrößerte Quellen offen.
4. Onsite-Prämisse der DET-Sorte aus P1/P2 (`det-wall-hh-rule`), äquivalent zu
   Positivität + Budget (`TFPT-Globaler-Quellabschluss`).
5. RH: Fensterinfimum ≤ 10⁻¹² für L ≥ 9/4, konstantes Randgate widerlegt, volle
   Vergleichsform (14) ≡ Fensterpositivität (`odd-window-direct-infimum-20260910`).

## Reproduktion

    cd fable && python3 -B checks.py            # schreibt checks.json
    python3 -B -OO checks.py /tmp/oo.json && cmp checks.json /tmp/oo.json
