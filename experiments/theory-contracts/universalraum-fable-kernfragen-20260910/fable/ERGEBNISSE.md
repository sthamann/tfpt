# Ergebnisse der Fable-Runde (Claude Fable 5.1, 10. September 2026) — abschließender korrigierter Stand

Auftrag: `BRIEFING.md`, `UPDATE-1.md`, `UPDATE-2.md`. Beweise und Grenzen: `PROOF.md`. Kontrollen:
`python3 -B checks.py` → `checks.json`, `python3 -B cap_dynamics.py` → `cap_dynamics.json` (normal
und `-OO` bytegleich). Quellen und eigene Artefakte mit SHA-256: `QUELLEN.json`.

Eingearbeitet sind alle Reviews: LL2 (Zwei-Link-Endpunktbilinear, Zeuge −1/576), Theorem 1
(H_diag-Term), μ_s/ζ-Gibbs-Unterscheidung, REVIEW-FABLE-ARITHMETIK, REVIEW-FABLE-DYNAMIK,
REVIEW-FABLE-ZUSATZ (2×2-Modell, Duhamel) sowie die konstruktiven Ergänzungen ERWEITERUNG.md und
KRITISCHER-GRENZZUSTAND.md. Die erste Dressing-Stufe ist von Codex mit 85 exakten Kontrollen bestätigt.

Keine RH-Aussage, kein Faktorisierungs-Geschwindigkeitsvorteil, kein TOE-/T1–T8-Abschluss; Parent,
Wandprämisse, Zustandsauswahl und Zeitidentität werden nicht aus P1/P2 hergeleitet. Ein Ring und zwei
Ringe belegen keine allgemeine TFPT-Dynamik, sondern die dort exakt bewiesenen Identitäten.

## Beweisklassen

Beide JSON-Dateien tragen `evidence_classes`. Exakte Fraction-Belege: Zwei-Link-Zeuge, Leak-Satz mit
Superpositionszeuge, Krylov-Block (Ring), Dressing Ordnung 0–2, Flussfenster-Nenner, Zwei-Plaquetten-Cap,
Radix/Übertrag, σ_K-Box, lokale Überlagerung, Duhamel-Gegenzeuge. numpy: Überlagerungsrelationen,
U₂ auf Z₉₁, Nullraum des invarianten Zustands. mpmath: ζ-Gibbs-Restklassen, L/ζ-Asymmetrie,
elektrische Gibbs-Gewichte mit Poisson-Schranke, ⟨H_E⟩_β. Modellwerte: 2×2-Hilfsmatrix, Duhamel-
Koeffizienten (Wurzeln exakter Einträge). Der frühere pauschale „alles exakt“-Status ist entfernt.

## Ergebnisabsatz in einfachen Worten

**Cap und Dynamik.** Der physische Wilson-Cap existiert im begrenzten Sinn, ist aber nicht
H-invariant. Für All-Low-Codes gilt exakt Γ*Γ = J*H_diag(I−P)H_diagJ + b²N_dir I ≥ b²N_dir I;
Gleichheit genau für H_diag-invariante Codes (Flussbasis): N/96 auf dem Torus, 1/72 auf dem Ring,
1/36 auf zwei Ringen. Superpositionen tragen zusätzlich ihre elektrische Varianz (Ring: 1/72 + 1/10000;
Codex-Torus: 125/96 + 1/10000). Für feste Besetzungsbasiszustände folgt Nichtinvarianz, aber nicht
allgemein ein extensives Leck (Blockmuster: O(L²)). Feste Marken sind nicht stationär
([H_E,S]Ω₀ = (1/50)SΩ₀); mitgeführte Marken sind eine verfügbare exakte Konstruktion, größere
invariante Räume sind nicht ausgeschlossen.

**Zwei quellengebundene Fortsetzungen, konsolidiert.** (1) Codex' exakter Krylov-Block V₁ = (J,η):
Präparation bleibt, Momente 0–3 exakt, H⁴-Fehler g²R*R, nächste Kanäle Z₀ (−I/√24) und η₂ (G₂ > 0);
auf dem Ring habe ich alle Strukturaussagen exakt reproduziert (g² = 1/72, Kopplungsblock, h₁ mit
Konstante 57497/14400 und Nachbarkopplung −1/1152, Momente, H⁴-Defekt, Onsite-Kanal −deg·a·b·N).
(2) Mein Dressing durch die Quelle ändert die präparierte Familie: Leck 1.39·10⁻² → 3.3221·10⁻⁵
(bestätigt) → 8.71·10⁻⁸ (Ordnung 2, nicht unabhängig zertifiziert), Träger 1 → 9 → 54. Das ist eine
Näherung mit Abbruchvertrag ‖(e^{−itH}V − Ve^{−ith})v‖ ≤ |t|·‖R‖, ‖R‖ aus der ganzen Restmatrix:
0.118, 6.0·10⁻³, 3.1·10⁻⁴ (ein einzelner Spaltenwert ist kein Trajektorienbound; Gegenzeuge
reproduziert). Keine Aussage über alle Ordnungen, keine Minimalität. Gültig nur im getesteten
Flussfenster: Δ(E) = (9587 + 24σE)/2400 wird bei σE = −399 zu 11/2400 (b/Δ = 100/11) und wechselt
bei −400 das Vorzeichen.

**Kein exakter Volumensatz.** Die Werte 6.6 % (L = 5), 10 %, 29 % und die Schwelle ≈ 1500 Orte sind
Eigenschaften einer isolierten 2×2-Hilfsmatrix (Eigenvektorgewicht 6.5858 %, normierter
Erstordnungsvektor 7.5445 % bei N = 125) und **keine** Gewichte des Parents; ERWEITERUNG beweist
R₁ ≠ 0, also keine invariante Zwei-Niveau-Reduktion. Bewiesen ist nur: Die erste Kopplung der
globalen All-Low-Präparation wächst wie √(N/96).

**Cap-Atmen.** Zwei-Plaquetten-Cap: ΔE = 7/50, Var_el = 17/2500, Var_voll = 389/11250,
‖P[H,T_bal]Ψ‖² = 13/625 (Codex-Werte exakt). Unter H_E allein ⟨T_bal⟩(t) = ½[cos(t/5)+cos(t/25)],
Wiederkehr 50π (vom Zusatzreview bestätigt). Unter dem separat definierten Normfluss ist die markierte
M₄-Algebra punktweise fest — eine Aussage über eingeschränkte Antworten, nicht über den Cap-Vektor
oder eine gemeinsame physische Zeit.

**Zustand.** Auf M₄ ist die Spur der einzige unter Ad(S), Ad(Z) invariante Zustand. Auf der
Restklassenalgebra stimmen überein: Cap-Einschränkung, kritischer ax+b-Zustand (Codex: weak*-Limes der
ζ-Dichten auf der affinen C*-Algebra, 1-KMS), β → 1⁺-Limes der ζ-Gibbs-Restklassen (pro festem
Modulus) und β → 0-Limes der elektrischen Gibbs-Restklassen (bei κ = 1/100 für β ≤ 1 uniform bis
10⁻⁵⁴). Das identifiziert **eingeschränkte** Zustände, nicht den vollen reinen Cap mit dem vollen
kritischen Zustand. Korrekturen: ζ-Gibbs ≠ μ_s bei endlichem β (ω_β(1)−ω_β(3) = L(β,χ₄)/ζ(β) > 0,
Reparatur μ_β = ∫u_*ω_β du); Konvergenz nie gleichmäßig im Modulus (TV-Abstand 1); ⟨H_E⟩_β nur für
β > 3 endlich. Der elektrische Grundzustand ist δ₀, nie Frobenius: Der Cap ist präparations- und
transportpflichtig. Endliche Alternative (Codex §5, exakt reproduziert): σ_K auf −K…K mit
Restklassenfehler ≤ 1/(2K+1) und Energie κK(K+1)/6 (Plaquette 2κK(K+1)/3); die lokale Überlagerung
S_m^{(p)} ist auf dem vollen Flussraum injektiv und gaußerhaltend.

**Radix, Überlagerungen, Uhren.** E² = 16Q² + 8QR + R², U = C·L mit C = U⁴P₀ + (I−P₀) — der Übertrag
liegt in der endlichen Shift/Diagonal-Algebra; W*(L, ℓ^∞(E)) ≅ ℓ^∞(Z; M₄); mit U ist der
von-Neumann-Abschluss B(ℓ²(Z)), der Normabschluss enthält S_m nicht. Überlagerungen: exakte
Relationen, Energie m² nur auf dem reinen Schleifensektor (Ausgangsenergie, kein Kostenvertrag), auf
geladenem Hintergrund Kreuzterm 2(m−1)n⟨ξ,p⟩. Ein echter S_m ist als nichtsurjektive Isometrie nie ein
e^{−itH}. U_a auf Z₉₁: separat konstruierte Permutation, F U_a F* = U_{a⁻¹}, Ordnung 12; 91 Shift-Labels
= Formatkomplexität, keine Gate-Untergrenze; |n⟩ → |n mod N⟩ ist kein beschränkter Transfer; U_a ≠
kontrollierte Exponentiation. Kein neuer Reader, kein Speedup behauptet oder ausgeschlossen.

## Exakte Zahlen

| Größe | Wert | Klasse |
|---|---|---|
| Zwei-Link-Zeuge 75→78 | −1/576 (sequenzielle Mutante 0) | exakt |
| Leak Flussbasis: Ring / zwei Ringe / Torus | 1/72 / 1/36 / N/96 | exakt / exakt / Satz |
| Leak Superposition (Ring) / (Codex L=5) | 1259/90000 / 78131/60000 | exakt / Codex |
| [H_E,S]Ω₀ | (1/50)·SΩ₀ | exakt |
| Dressing Ord. 0/1/2 (Ring) | 1.389·10⁻² / 3.32212·10⁻⁵ / 8.7130·10⁻⁸ | exakt (Ord. 1 bestätigt) |
| Duhamel ‖R‖ Ord. 0/1/2 | 0.1179 / 6.02·10⁻³ / 3.08·10⁻⁴ | Wurzel exakter Einträge |
| Nenner bei σE = −399 | Δ = 11/2400, b/Δ = 100/11 | exakt |
| Krylov-Block (Ring): g², h₁−h₀, Nachbarkopplung | 1/72, 57497/14400, −1/1152 | exakt |
| Krylov: Momente 0–3 / H⁴-Defekt | exakt / g²R*R, R*R ≈ 0.038 | exakt |
| Onsite-Kanal ⟨Σd*lJ, HΓJ⟩ | −1/36 = −deg·a·b·N | exakt |
| Cap: ΔE / Var_el / ‖P[H,T_bal]Ψ‖² / Var_voll | 7/50 / 17/2500 / 13/625 / 389/11250 | exakt |
| ⟨T_bal⟩(t) unter H_E | ½[cos(t/5)+cos(t/25)], Wiederkehr 50π | exakt / Float |
| 2×2-Modell N=125 | 6.5858 % (Eigenvektor) / 7.5445 % (1. Ordnung) | Modellwerte |
| invarianter Zustand auf M₄ | Nullraum 1 (Spur) | numpy-Rang |
| ζ-Gibbs mod 4, β=1.0001 / L/ζ bei β=2 | 5.7·10⁻⁵ / 0.5568 | mpmath |
| ⟨H_E⟩_β bei β=4 | (κ/2)ζ(2)/ζ(4) | mpmath |
| elektrische Gibbs mod 4, β=1/10/100/1000 | 0 (40 St.) / 2.2·10⁻⁶ / 0.149 / 0.737 | mpmath |
| σ_K, K=10 | Fehler 4/105 ≤ 1/21, Energie 11/60 (Rotor), 11/15 (Plaquette) | exakt |
| U₂ auf Z₉₁ | Ordnung 12, Zyklen {1,3,12}, 91 Shift-Labels | numpy |

## Korrekturen gegenüber meinen früheren Fassungen

- Zwei-Link-Term als Endpunktbilinear; Dressed-Leak 3.32265·10⁻⁵ → 3.32212·10⁻⁵.
- Theorem 1 mit H_diag-Term; „alle fixed-matter“ → All-Low bzw. Besetzungsbasis ohne Extensivität.
- Kein „kein endliches Dressing beliebiger Ordnung“, keine „kleinste/einzige“ Erweiterung, kein
  Expansionsparameter, keine Volumenprozente oder Abbruchschwelle als Parent-Aussagen.
- Duhamel mit ‖R‖ aus der ganzen Restmatrix statt Spaltenwert.
- Zustände: Koinzidenzen nur auf Restklassenalgebra/M₄; ζ-Gibbs ≠ μ_s bei endlichem β; keine
  Gleichmäßigkeit im Modulus; unendliche elektrische Energie der ζ-Folge für β ≤ 3.
- Übertrag C liegt in der endlichen Shift/Diagonal-Algebra; Topologie der Abschlüsse benannt;
  Shift-Labelzahl ≠ Gate-Untergrenze; Labelmodulo ≠ Hilbertraumtransfer; Energie m² nur auf dem
  reinen Schleifensektor.
- Frühere zu starke Sätze: „Faktorisierung nicht NP-vollständig“ → nicht als NP-hart bekannt;
  „keine Positivitätsquelle für RH“ → in den geprüften Konstruktionen keine identifiziert;
  „P vs NP nicht adressierbar“ → nichts gezeigt, in keiner Richtung.

## Offene Anschlussbedingungen

1. Nativer Mechanismus für Präparation und Erhalt der Frobenius-Cap-Gewichte (Invarianz wählt sie auf
   M₄ aus; F₁, C sind erlaubte Feldoperationen, aber nicht H-erzeugt zu ausgewählter Zeit).
2. Quellseitiger Grund für β = 1-Normzeit; elektrische Zeit und Normzeit sind Funktionen derselben
   Ladung mit inkompatiblen Gibbs-Zuständen und verschiedenem Cap-Verhalten.
3. Invariante Cap-Erweiterung mit kommutierender Markierung: für All-Low-Flusscodes ausgeschlossen,
   sonst offen; Krylov-Block und Dressing sind zwei Fortsetzungen ohne Abschluss-/Minimalitätsbeweis.
4. Native flusskontrollierte Schleifenoperationen mit kontrollierten Kosten.
5. Onsite-/Wandprämisse aus P1/P2 (`det-wall-hh-rule`, `TFPT-Globaler-Quellabschluss`).
6. RH: Fensterinfimum ≤ 10⁻¹² für L ≥ 9/4, konstantes Randgate widerlegt, Vergleichsform (14) ≡
   Fensterpositivität (`odd-window-direct-infimum-20260910`); keine Positivitätsquelle in dieser Runde.

## Reproduktion

    cd fable
    python3 -B checks.py            # checks.json  (~0.3 s)
    python3 -B cap_dynamics.py      # cap_dynamics.json (~4 s; Dressing exakt bis Ordnung 2)
    python3 -B -OO checks.py /tmp/a.json && cmp checks.json /tmp/a.json
