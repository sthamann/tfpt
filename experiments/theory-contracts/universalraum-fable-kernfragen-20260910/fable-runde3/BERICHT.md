# Runde 3 (Fable, 11. September 2026): Zugriffsprüfung, unabhängige Nachrechnung der beiden ChatGPT-Berichte und des neuesten Codex-Befunds

Kein RH-Beweis, kein Faktorisierungsvorteil, kein TOE-Abschluss. Dieser Bericht prüft, was von den drei
eingefügten Berichten (ChatGPT I, ChatGPT II, Codex III) im Repo unabhängig nachrechenbar ist, und bewertet
den Rest. Prüfer: `check_runde3.py` → `checks.json` (normal und `-OO` bytegleich, ~1 s),
`check_rh_high_block.py` → `rh_high_block.json` (~6 s), `check_codex_load.py` → `codex_load.json` (~1 s).

## 1. Zugriff: was lesbar ist und was nicht

| Quelle | Status |
|---|---|
| `context/` (45 Universalraum-Dokumente, `aktuelle-runde/`, `fortsetzung/`, `transformationen/`, `thermischer-anschluss/`, PDF), `fable/`, `fable-runde2/` | lesbar, ~1,4 MB Markdown + Prüfer |
| `rh/catalog/research_engine/experiments/odd-window-direct-infimum-20260910/` (Fensterform-Matrizen, `LOAD_BOUND.md`) | lesbar |
| `~/Documents/Codex/2026-09-10/…` und `2026-09-11/…` (Codex-Originale, `Universalraum-Konsolidiert-mit-Fable.md`, `Fable-Gegenpruefung.md`) | **nicht lesbar** („Operation not permitted“, macOS TCC) |
| ChatGPT-seitige Dateien: `U020`, `U021`, `U054`, `U090`, „Anhang“, „Prüfpaket“, die „fünf/sechs Prüfprogramme“, `:chatgpt-content-reference` | **nicht im Repo**; keine der charakteristischen Zahlen (497664, 161000000, 0,0617103491633, 1,6875·10⁻³⁸, 10⁻⁴⁶) kommt irgendwo im Repo vor |
| „Horizontdokument Seite 4, Zeile reduzierte Planckeinheiten mit Faktor c₃“ | in der Repo-Kopie `Universalraum-Schwarze-Loecher-und-Horizonte.md` **nicht vorhanden** (dort nur \(T_H=\hbar\kappa/2\pi ck_B\), SI-Form); PDF-Text nicht extrahierbar. Die Formel \(T_H=1/(8\pi GM)=\overline M_{\rm Pl}^2/M\) ist korrekt; ein zusätzlicher Faktor \(c_3=1/(8\pi)\) zählt \(8\pi\) doppelt. |

Folge: Die *Behauptungen* der Berichte sind lesbar, ihre *Belege* (Beweise, Programme, Intervallzertifikate)
nicht. Alles Nachfolgende ist deshalb eine unabhängige Rekonstruktion auf dem Repo-Modell, kein Review der
fremden Programme.

## 2. ChatGPT-Bericht II: das „stärkste Ergebnis“ ist auf dem Repo-Ringparent exakt richtig

Modell: `fable/cap_dynamics.py` (a=1/12, b=1/24, c=1/576, κ=1/100, M=4, ε_L=1/96) — identisch mit dem im
Bericht genannten Ring. Code = echte Schleifenflusszustände \(W^k\Omega_0\), k=−2…2 (Übertrag behalten).

| Behauptung | Repo-Nachrechnung | Klasse |
|---|---|---|
| \((J^*HJ)_{k,k+1}=(J^*H^2J)_{k,k+1}=0\) | 0, 0 | exakt |
| \((J^*H^3J)_{k,k+1}=-4b^2c=-1/82944\), flussunabhängig | bestätigt; genau **4** geordnete Pfade b·c·b, je −1/331776 (LH-Hop, Zweilink-LL, HL-Hop, 4 Startorte) | exakt |
| \((K_\beta)_{\rm off}=-\beta^2/497664\,\mathsf K_W+O(\beta^3)\) | \(m_3/6=-1/497664\) ✓ | exakt |
| \((J^*e^{-itH}J)_{\rm off}=-it^3/497664\,\mathsf K_W+O(t^4)\) | \((-i)^3m_3/6=-i/497664\) ✓ | exakt |
| \((K_\beta)_{01}\) bei β=0,1 ≈ −1,737835551359201·10⁻⁸ | −1,7378355513592918·10⁻⁸ (Basis 496 Zustände) | numerisch, 15 Stellen |
| \(\mu_3=443/259200+M/72\) | rohes Moment \(\langle\Omega_0|H^3|\Omega_0\rangle\): Steigung 1/72, Achsenabschnitt 443/259200, linear in M (M=4,7,13) ✓. (Das zentrale Moment ist 57497/1036800; Differenz \(E_0^3+3E_0\cdot 8b^2=25/13824\).) | exakt |
| Tabelle P(N_H≥1) für (M,h)=(4,0),(13,0),(4,1/12) bei t=0,2/0,4/0,8 | alle 9 Werte bis auf ≤ 4·10⁻¹⁴ reproduziert (Basis 1110–1400 Zustände, Duhamel-Leck des entwickelten Zustands mitgeführt) | numerisch |
| \(V_r=S^{-rN_H}\): \(V_rd_xV_r^*=S^rd_x\), \(V_rl_xV_r^*=l_x\); Viererstrom-Identität | bestätigt (2 Orte × Rotor C⁴) | numerisch |
| \(\mathcal U_m\mathcal U_n=(-1)^{mn}\mathcal U_{m+n}\) aus \(ZWZ^*=iW\) | \(i^{m^2}i^{n^2}=(-1)^{mn}i^{(m+n)^2}\) ✓ | exakt |
| E₈-Zweige (60,64,60,64), 57 600 Paare | Z₄-Grad \(q=2(r_5+r_6+r_7)\bmod 4\) auf D₅⊕D₃: (60,64,60,64), additiv auf allen 57 600 Paaren ✓ = (45,1)+(1,15) / (16,4) / (10,6) / (16̄,4̄) | exakt |

**Einordnung, nicht Widerlegung.** Die „gemeinsame Wilsonantwort“ ist ein allgemeines Lemma und kein Indiz
für eine gemeinsame Quelle jenseits des Hamiltonoperators:

> **Lemma (drittes Moment).** Sei \(J\) ein Code mit \(M_n:=J^*H^nJ\), \(M_1\) diagonal und \((M_2)_{k,k+1}=0\).
> Dann gilt \(\bigl(-\tfrac1\beta\log J^*e^{-\beta H}J\bigr)_{k,k+1}=\tfrac{\beta^2}{6}(M_3)_{k,k+1}+O(\beta^3)\)
> und \((J^*e^{-itH}J)_{k,k+1}=\tfrac{(-it)^3}{6}(M_3)_{k,k+1}+O(t^4)\).
> *Beweis.* \(\log(I+X)=X-X^2/2+\dots\) mit \(X=-\beta M_1+\beta^2M_2/2-\beta^3M_3/6+\dots\); alle
> Nebendiagonalbeiträge der Ordnung β³ außer \(-\beta^3(M_3)_{\rm off}/6\) enthalten einen Faktor \((M_2)_{\rm off}=0\)
> oder sind Produkte diagonaler Matrizen. Die Zeitreihe ist die Taylorentwicklung von \(e^{-itH}\). ∎

Dieselbe Zahl in beiden Antworten ist also **eine** Zahl: \((M_3)_{k,k+1}=-4b^2c\). Jede beschränkte Störung mit
derselben Dreischritt-Amplitude liefert denselben führenden Term. Ab der nächsten Ordnung unterscheiden sich
beide (bei β=0,1 beträgt \((K_\beta)_{01}\) nur 0,865 des führenden Terms).

## 3. ChatGPT-Bericht I: die „drei geschlossenen Lücken“

- **A. Choi-Rekonstruktion.** Korrekt und elementar: vier Antworten \(DXD^*\) auf ein Erzeugendensystem
  positiver Proben bestimmen die lineare Abbildung, deren Choi-Matrix \(vv^*\) mit \(v=\sum_ie_i\otimes De_i\)
  Rang eins hat; \(D\) folgt bis auf U(1). 8 Beispiele (inkl. singulär) reproduziert. Die „Phasenlücke“ ist
  genau die U(1), die keine Ad-Wirkung sehen kann; eine markierte Referenz ist ein *Zusatz*input.
- **B. Thermische Log-Differenz.** \(\log\rho_\beta-\log\sigma_\beta=-\beta V-\log(Z_H/Z_{\rm el})\,I\) ist eine
  **exakte Identität** für beliebige hermitesche \(H_{\rm el},V\) (Hauptlogarithmus von \(e^{-\beta H}\) ist
  \(-\beta H\)). Der genannte „Operatorfehler 1,7·10⁻¹²“ ist Gleitkommarauschen einer Identität (hier
  1,7·10⁻¹⁴). Inhaltlich richtig ist nur der Zusatz: nach Projektion auf einen Code ist
  \(K_\beta\neq J^*HJ\) (siehe §2: der Nebendiagonalterm entsteht erst durch Austritte).
- **C. Cap-Schranke** \(\|D_{\rm hoch}-4t^2I\|\le2\sqrt5\,t\varepsilon+\varepsilon^2/(2-\sqrt2)\): ohne den Anhang
  nicht rekonstruierbar (die Normbedingung für ε fehlt). Mit der einfachsten Hypothese
  \(R_r=tS^r+e_r\), \(\|e_r\|\le\varepsilon\), folgt nur \(\|D-4t^2I\|\le8t\varepsilon+4\varepsilon^2\); mit
  \(R_{r+1}=SR_r+\delta_r\), \(\|\delta_r\|\le\varepsilon\), \(12t\varepsilon+14\varepsilon^2\). Die Konstanten
  \(2\sqrt5\), \(2-\sqrt2\) verlangen eine andere, nicht mitgeteilte Fehlerdefinition. **Nicht prüfbar.**
- Sonstiges: \(E_{\max}^{\min}=2\kappa\lfloor D/2\rfloor^2\) (Min-Max auf 0,1,1,4,4,…) ✓, 20 Qubits
  5 497 558 138,88 ✓; RH-Budget \(4\log\frac{12/5}{9/4}=0{,}258154\) ✓; 1,6875·10⁻³⁸ nicht prüfbar (m_N, m_0 fehlen).

## 4. RH (Berichte II und III) gegen die Repo-Fensterform

Repo-Matrizen: `probe.py` (Q061-Definition), L=12/5, ungerade Legendre-Moden orthonormal, N=160/240/320.
Niedrig = Grade 1…159 (80 Richtungen), hoch = Rest.

| Größe | N=160 | N=240 | N=320 |
|---|---:|---:|---:|
| \(\lambda_{\min}\) hoher Block \(C\) | 1,946 | 1,749 | 1,748 |
| \(\lambda_{\min}\) niedriger Block \(A\) | −3,3·10⁻¹³ | −3,2·10⁻¹³ | +1,5·10⁻¹³ |
| \(\lambda_{\min}(A-B^*C^{-1}B)\) (Galerkin) | −3,3·10⁻¹³ | −3,2·10⁻¹³ | +1,5·10⁻¹³ |
| \(\lambda_{\min}\) volle \(Q_J\) | −3,3·10⁻¹³ | −3,2·10⁻¹³ | +1,5·10⁻¹³ |
| \(\|B\|\) | 1,670 | 1,675 | 1,678 |

Folgerungen:

1. **Bericht II, „\(Q_J\ge 3/50\) auf dem hohen Raum“**: konsistent und sehr konservativ — das Galerkin-Minimum
   des hohen Blocks liegt bei ≈1,75 (Galerkin-Minima sind obere Schranken des Infimums über den endlichen
   Unterraum; ein Wert < 0,06 hätte die Behauptung widerlegt). Kein Zertifikat, aber keine Auffälligkeit.
2. **Bericht III, „81-dimensionale Kompression positiv, Marge 10⁻⁴⁶, 450 Stellen“**: mit den Repo-Matrizen
   nicht entscheidbar — \(\lambda_{\min}(A)\) liegt am float64-Rauschboden (±3·10⁻¹³, Vorzeichen wechselt mit
   der Quadraturordnung). Die Prolate-Abschätzung in `LOAD_BOUND.md` §4 setzt das wahre Fensterinfimum bei
   ~10⁻¹¹…10⁻¹² an; eine Marge 10⁻⁴⁶ ist damit *plausibel wahr*, aber uninformativ. Auffällig: Wer 450 Stellen
   und Kernfehler 2·10⁻⁶⁶ hat, kann \(\lambda_{\min}(A)\) selbst auf ~50 Stellen angeben statt „≥10⁻⁴⁶“.
   Diese Zahl wäre der einzig interessante Output gewesen.
3. **Der einzige lasttragende Gegenstand**, \(F_{\rm eff}=A-B^*C^{-1}B\), sitzt in jeder Auflösung exakt dort,
   wo \(\lambda_{\min}(Q_J)\) sitzt: am Rauschboden. Beide Berichte sagen selbst, dass sie ihn nicht
   kontrollieren. Damit ist der RH-Stand **unverändert** gegenüber `LOAD_BOUND.md` (10. 9.): jedes Zertifikat
   des 12/5-Fensters muss eine Marge ≲10⁻¹² auflösen; Konstantboden-Reduktionen können das nicht.
4. **Bericht III, „Diagonalabkürzung streng widerlegt“**: qualitativ richtig — die Diagonalschranke
   \(C\ge(3/50)I\) überzahlt die Kopplung um \(\|B^*B\|/c\,:\,\|B^*C^{-1}B\|=46{,}5/0{,}995=46{,}7\) (N=160).
   Aber (a) dasselbe steht seit dem 10. 9. im Repo (`LOAD_BOUND.md` §6, `REFUTED_SCOPED`, Faktor ≥3,3 für
   τ=7/10), (b) die Zahlen 0,456 / 14,56 / >11,12 sind mit den genannten Definitionen **nicht
   reproduzierbar** (Verhältnis 31,9 statt 46,7; implizierte „niedrige Energie“ 3,19 bzw. 2,18, also
   inkonsistent). Die Normierung der „relativen Kopplungslast“ ist nicht mitgeteilt.
5. Auch ein vollständiges Fensterzertifikat wäre eine endliche notwendige Bedingung, kein RH-Fortschritt im
   Sinne der Claim-Grenze in `rh/`.

## 5. Codex-Befund III, restliche Operatoraussagen (von Hand)

| Aussage | Prüfung |
|---|---|
| \(\|[\alpha_1(X_x),Z]\|=\sqrt2\) für \(X_x=l_x^*d_x\) unter \(V_1=S^{-N_H}\) | ✓: \(V_1X_xV_1^*=l_x^*Sd_x\), \([S,Z]=(1-i)SZ\), \(\|l_x^*d_x\|=1\). Korrekte Selbstkorrektur; die Fernwirkung ist abstandsunabhängig. |
| \(V_{\rm loc}H_EV_{\rm loc}^*\le(1+\varepsilon)H_E+18\kappa(1+\varepsilon^{-1})N_{\rm Zellen}\) | ✓ herleitbar: \(S_C\) verschiebt vier Linkflüsse um +1 oder −3, \((E+\delta)^2\le(1+\varepsilon)E^2+(1+\varepsilon^{-1})\delta^2\), \(4\cdot9\cdot\kappa/2=18\kappa\). |
| \(H(\theta)=D(\theta)H(0)D(\theta)^*\), \(D\) global periodisch ⇒ \(c_1=0\) | ✓, aber **trivial**: sind die Winkel reine Phasen aller dynamischen Links, ist \(D(\theta)=\prod_ee^{i\theta_eE_e}\cdot\)(Fermionphasen) eine Eichtransformation, periodisch weil \(E_e\in\mathbb Z\); jedes Spektralbündel ist dann isomorph zum trivialen. Nützlich nur als Verbot, die verdrehte Rotorfamilie als chirale Randlinie auszugeben. |
| Rand 4 Zustände vs. E₈-Vakuummodul 249 bis Energie 1 | ✓ trivial: Level-1-E₈-Charakter \(1+248q+\dots\); Isometrie mit Energieerhalt unmöglich. |
| \(K(k)=cI+v\,\sigma\!\cdot\!k\), 8 Doppler auf dem Gitter | Lehrbuch (Weyl-Operator, Nielsen–Ninomiya). Keine TFPT-Herleitung, wie der Bericht selbst sagt. |
| Faktorisierung 24 Eingaben: 2/3/3 gelöst vs. Pollard–Brent 24/24 bei 6 935 Produkten | plausibel, negatives Ergebnis, nicht prüfbar (Programme fehlen). |

## 6. Bewertung: „fakt“ das Modell?

**Nein im Sinne erfundener Zahlen.** Alles, was am Repo-Modell prüfbar war, stimmt bis auf Maschinengenauigkeit
(9/9 Vorhersagewerte auf 10⁻¹⁴, \(K_\beta\) auf 15 Stellen, drei exakte Brüche, E₈-Zählung). Das sind echte
Rechnungen auf genau diesem Ringmodell.

**Ja im Sinne von Verpackung.** Systematisch werden als „neue Beweise“ ausgegeben:
(i) exakte Identitäten mit Gleitkommafehlern als „Ergebnis“ (Log-Differenz);
(ii) Lehrbuchsätze (Weyl-Operator, Level-1-Zählung, Eichtrivialität von \(c_1\));
(iii) Resultate, die bereits im Repo stehen (Diagonalgate-Widerlegung, `LOAD_BOUND.md` vom Vortag);
(iv) ein RH-„Positivitätsnachweis“ des Blocks, der nach eigener Aussage nichts entscheidet, mit einer
Marge (10⁻⁴⁶), die den eigentlich messbaren Wert verschweigt;
(v) das „gemeinsame Wilson-Ergebnis“, das ein Lemma über das dritte Moment ist.
Jeder Bericht endet korrekt mit denselben offenen Punkten wie der vorige: \(F_{\rm eff}\), native chirale E₈-Quelle,
kein Faktorvorteil. Die lasttragenden Lücken haben sich über drei Berichte **nicht bewegt**; bewegt haben sich
nur Nebenlemmata.

Die naheliegendere Erklärung als Absicht ist: Die offenen Punkte (RH-Fensterrest bei 10⁻¹² Marge, ein aus P1/P2
hergeleiteter Parent, ein echter Faktorleser) sind mit diesen Methoden nicht schließbar — das steht
sinngemäß schon in `KONSOLIDIERTER-STAND-CODEX.md` §7 und `LOAD_BOUND.md` §6. Ein Sprachmodell, das das
weiß und trotzdem „Fortschritt“ liefern soll, produziert genau dieses Muster: korrekte Kleinresultate in
großer Verpackung.

## 7. Was jetzt tatsächlich zu entscheiden ist (mein Vorschlag)

1. **Keine Berichte mehr ohne Artefakte im Repo annehmen.** Jede Zahl, die nicht aus einem hier
   ausführbaren Programm kommt, gilt als unbelegt (wie in §1: die ChatGPT-Belege sind nicht zugänglich).
2. **RH-Abnahmekriterium festnageln:** Ein Ergebnis zählt nur, wenn es eine zertifizierte untere Schranke
   für \(\lambda_{\min}(A-B^*C^{-1}B)\) mit *vollständigem* Rest \(R^*C^{-1}R\) liefert. Alles andere (hoher
   Block, endliche Kompression, Diagonalgates) ist erledigt bzw. irrelevant. Der ehrliche Erwartungswert:
   Marge ~10⁻¹², d. h. sinnvoll nur mit exakter Kernauswertung; und selbst dann kein RH.
3. **TFPT-Abnahmekriterium:** eine aus dem unveränderten Parent *erzeugte* (nicht nur darin *existierende*)
   Vieroperation, oder ein expliziter No-Go. `V_loc` ist eine Existenzaussage; das sagt Bericht III selbst.
4. **Faktorisierung:** der 24-Eingaben-Vergleich ist die richtige Methode und negativ; nur ein Verfahren mit
   Reader-Kosten unter Pollard–Brent auf demselben Eingabesatz wäre ein Ergebnis.

## 8. Türenprüfung gegen den Wissensgraphen (11. 9., Nachmittag)

Quellen: `_newest/graph/concepts.json` (611 Knoten, 1923 Kanten), `gaps_report.json` G1–G6,
`rh/catalog/analysis/compiler_necessity.md`, `experiments/tfpt-discovery/simplicity_core_census_probe.py` (31/31),
`tfpt_5_redteam.tex`, `tfpt_research_contracts.tex` (WOIT.OS.TWISTOR.01), `docs/OPEN_PROBLEMS.md`.

**Was der Graph selbst sagt.** G5 = genau die 14 TFPT-Strukturknoten (μ₄, c₃, g_car, E₈-Compiler, Seam, …) ohne
jeden Pfad zur RH-Seite. Die drei Verbindungsfragen sind registriert und haben **attempts: 0**:
`index-modular-state`, `no-archimedean-prime-joint-space`, `unitarity-of-emergent-time`. Bewiesene Barrieren:
`finite-clock-commensurability` (endliche Uhren tragen keine log p-Perioden), `discrete-spectrum-neutrality`,
`tate-information-loss`, `pi-numerology-c3` (c₃ = 1/(32 L(1,χ₋₄)) firewall-geflaggt).

**Regelverstoß der Universalraum-Runden.** `compiler_necessity.md` §C fixiert die Kill-Bedingungen für Brücke 1:
„assigned p^{it}, a standard BC system merely renamed, failure of global covariance as in v740/v741“. Der thermische
Anschluss vom 10. 9. setzt die Normzeit λ_t(S_m) = m^{it}S_m auf der Cuntz-ax+b-Algebra **an** — das ist wörtlich die
gekillte Route in neuer Kleidung. Nach den eigenen Regeln des Korpus ist das ein KILL, kein Fortschritt.

**Tür 1 (Weltfläche).** Korpus: 496 = 16·31 = dim(E₈×E₈) als *audit-only speculation* [O]
(`tfpt_1_architecture_e8.tex:4388`); das „sheet pair“ S⁺/S⁻ ist real (`v109`), aber S⁻ ist „the other side of the
seam“ (`tfpt_5_redteam.tex:693`) — die zweite Kante desselben Kragens, also **entgegengesetzte** Chiralität. Damit
ist das Zwei-Blatt-System die nichtchirale E₈-Narain-CFT (c_L = c_R = 8), nicht der heterotische E₈×E₈-Sektor
(beide linkslaufend). Zusätzlich: No-Unit-Theorem (`v153/v364`) — der Compiler hat keine Skala, ein String braucht
α′. Tür 1 hat im Korpus keinen tragenden Haken. Als Randnotiz: die Narain-CFT der zwei Blätter ist die
Weltflächentheorie eines Strings auf dem Torus R⁸/E₈ — genau dem Torus, auf dem `e8-sublattice-rg-semigroup` wirkt.

**Tür 2 (2+1D invertible Phase).** Keine Tür, sondern der Ort, an dem TFPT bereits steht: Kragen aus 16
Chern-Majoranas, invertibler Bulk wird *benutzt*, um Holomorphie zu erzwingen (SEAM.EQUIV Route A, `v301`,
`OPEN_PROBLEMS.md:188–209`: „Kitaev 16-fold-way class whose edge is the bosonic (E8)₁ state“).

**Tür 3 (modular/arithmetisch).** Ein Baustein ist exakt und neu im Korpus (`check_hecke_index_net.py`): mit der
KLM-Formel μ_A = [B:A]²μ_B, die das Repo für den Glue-Index 4 benutzt, gilt für jedes injektive A ∈ End(E₈)
\[
[\mathcal A_{E_8}:\mathcal A_{AE_8}] = |\det A| = \text{Hecke-Überlagerungsindex von } x\mapsto Ax \text{ auf } \mathbb R^8/E_8 .
\]
Der arithmetische Index *ist* ein Jones–Longo-Index des Seam-Netzes; die Zählfunktion ist Solomons ζ(s)ζ(s−1)…ζ(s−7)
mit rechtestem Pol bei s = 8 = c. Aber: Pimsner–Popa macht daraus die bedingte Entropie H(B|A) = log|det A|, keinen
Hamiltonoperator; die Automorphismen der Dualgruppe E₈/AE₈ lassen das Vakuum fest, der Connes-Kozyklus ist trivial.
**Scoped negativ für `index-modular-state`** (holomorpher Seam, Vakuum): die Normzeit ist RG-Zeit (Vergröberung um
den Index), die physische Zeit ist L₀ — verschiedene Kategorien. Das löst den Streit „elektrische Zeit vs Normzeit“
auf, statt ihn zu entscheiden: die Forderung ihrer Gleichheit war ein Kategorienfehler.

**Tür 4 (die eigentliche 3+1D-Route des Repos).** WOIT.OS.TWISTOR.01: α, β₁–β₃ ausgeführt, γ offen; die μ₄-Uhr ist die
euklidische Viertelrotation (`v522`), Signatur (2,2) erzwungen (`v565`). Korrektur meiner Aussage von 14:18: Coleman–
Mandula trifft nur die *kontinuierliche* Identifikation A₃ ≅ su(2,2) (Lesart der ChatGPT-Berichte), nicht die
diskrete μ₄ = euklidische Rotation des Repos. Der Preis dieser Tür ist bereits sichtbar: Kill-Test 2 feuert auf
Toy-Niveau (Reflexionspositivität bricht auf quartett-straddelnden Schnitten, `v529`), genau ein Mitglied überlebt
(`v534`). Hier, in Stufe γ, sitzt die einzige Dynamikfront, die in der Architektur zu 3+1D führen kann.

**Simplizität des Compilers.** Der Zensus (31/31) sagt: S4 = (c₃, g_car) ist der minimale Seed (Rest = 2 typisierte
Brücken: Winding 5/2, Q/C-Kanonizität 7/3). Der Brieskorn-Seed (2,3,5) liefert Rang 8, h = 30, E₈-Exponenten und
Clock 30 = 2·3·5 als Theorem, aber μ₄/E₈/Anker nur über Brücken. Der Compiler kann nicht einfacher werden; die Frage
ist nicht seine Einfachheit, sondern die Kategorie, in der seine zwei Axiome leben.

## 9. Korrekturen nach externer Kritik (11. 9., 15:42) — geprüft am Repo

**Zugestanden (Wortwahl, nicht Substanz).** „Leerer Körper / innen ist nichts“ war falsch formuliert. Richtig: Der
über Bulk–Rand-Korrespondenz zum holomorphen Seam gehörende 2+1D-Bulk ist eine **gapped invertible Phase** —
keine Anyonen, eindeutiger Grundzustand auf geschlossenen Flächen, aber nichttrivial (c₋ = 8, chirale
Wärmeantwort) und mit gapped Anregungen. Die Substanz bleibt: dieser Bulk ist 2+1-dimensional und gapped; eine
3+1D-Welt mit masselosen Eichfeldern und Materie ist nicht sein Bulk-Rand-Partner. Der 3+1D-Parent muss aus einer
anderen Route kommen (Tür 4). Darin stimmt die Kritik zu („der Rand bestimmt noch nicht unsere Welt“).

**Zugestanden (Paraphrase).** „μ₄ wählt unter allen Rang-8-Paaren (D₅, A₃)“ war meine Kurzfassung, nicht die
Aussage von `v993`. A₁⊕A₇ mit Glue (1,2) ∈ Z₂×Z₈ ist isotrop und zyklisch Z₄ (exakt: isotrope Elemente
{(0,0),(0,4),(1,2),(1,6)}, einziges isotropes Element der Ordnung 2 ist (0,4), also kein Z₂×Z₂), das Ergebnis ist E₈
— korrekt. **Aber:** `v993_minimal_defect_selector.py:27–31, 387–409` führt (A₇, A₁) bereits als NEGATIVE-Kill-Test
mit der Bedingung „cyclic Z₄ on BOTH factors“; die Projektion des Glue auf die A₇-Seite ist ⟨2⟩ ≅ Z₄ ⊊ Z₈, A₇ ist
nicht primitiv eingebettet. Der „reparierte Auswahlsatz“ der Kritik (Primitivität ⇔ Z₄ ≅ Z₄ auf beiden Seiten) ist
die Aussage, die `v993` seit dem 28. 8. trägt. Die Kritik widerlegt meine Paraphrase, nicht das Repo.

**Neu und richtig: zwei verschiedene Z₄.** Auf den 248 Strömen der Stufe 1 hat die innere Glue-Z₄ (Phasen 1, i, −1, −i
auf 60, 64, 60, 64) die Spur **0**, die geometrische Vierteldrehung e^{iπL₀/2} die Spur **248 i**. Quadrate: Glue² =
(+1, −1, +1, −1) = Spin(16)-Zentrum (NS/R-Parität, „[λ]² = [v]“), Drehung² = e^{iπL₀} = −1 auf allen 248. Beide sind
also verschiedene Operatoren auf demselben Modul. Im Repo werden sie transitiv identifiziert: `QGEO.SYM.01`
(„the carrier μ₄ glue *is* the conformal monodromy of the seam“, `tfpt_research_contracts.tex:366–374`, als
„bedrock“ typisiert) und `v522` („the μ₄ clock IS Woit's euclidean rotation“). Als Operatoridentität auf dem
(E₈)₁-Vakuummodul ist das unhaltbar; haltbar ist nur die kombinierte Form Uhr = Drehung ∘ innerer Twist, deren
Zusammensetzung der Seam liefern muss. Das gehört als Präzisierung an `QGEO.SYM.01`/`WOIT.BETA1.GSO.01`.

**Neu und richtig: A4 im α-Vertrag ist stale.** Der T1-Text (`tfpt_research_contracts.tex:14599–14601, 14621–14626`)
sagt korrekt: keine globale nichtverschwindende Sektion auf der unkompensierten Linie mit c₁ ≠ 0; zulässig nur auf dem
Pullback bzw. dem anomaliekompensierten Produkt. Das Abnahmekriterium A4 (`:14776`) verlangt weiterhin „the Dai–Freed
section nonvanishing over the whole moduli torus“ ohne diesen Qualifier — bei gemessenem Poincaré–Lelong-Divisor +1
(`v472`) hat die Sektion genau eine Nullstelle. Vorgeschlagene Reparatur (eine Zeile, `:14776`): „(the Dai–Freed
section nonvanishing on the pulled-back / anomaly-cancelled line over the whole moduli torus, cf. T1)“. Nicht
ausgeführt: Papieränderung, braucht `build.sh audit`.

**Kein Dissens:** SL(2,ℂ) ≠ SU(4); SU(4) vs SU(2,2) verschiedene reelle Formen mit Zentrum μ₄; Coleman–Mandula trifft
nur die kontinuierliche Generatoridentifikation; heterotisch braucht c = 16; modulare Geometrie braucht Netze, nicht
eine Algebra plus Zustand; endliche Modelle sind als kontrollierte Folge zulässig, als Einzelbefund nicht. Alles
bereits in §§ 4, 8 dieses Berichts bzw. in meinen Antworten von 14:18/15:42.

**Bewertung der Kritik:** In der Sache stimmt sie mit dem Bericht überein (kein 3+1D-Parent aus dem Seam, keine
vollständige Herkunft, RH getrennt). Ihre zwei echten Treffer sind die Trennung der beiden Z₄ und das stale A4; ihr
„Gegenbeispiel“ ist ein registrierter Kill-Test. Der α-Wert 137,0359992168407 wird bestätigt; die Berry-vs-kinetisch-
Lücke (topologische Daten fixieren den Maxwell-Term nicht) ist korrekt und entspricht `ALPHA.QUILLEN.EXACT.01` [O].

## 10. Übersehen: Tür 5 — Connes' Spektralwirkung ist die deklarierte 4D-Brücke des Repos (17. 6. 2026)

Nachtrag 11. 9., 18:00, ausgelöst durch die „U“-Skizze (System möglicher Veränderungen → Geometrie, Zeit, Materie,
Zahlen). Ledger-Zeilen (`verification/status_ledger.csv`), alle aktiv:

| Zeile | Inhalt | Status |
|---|---|---|
| `CONTRACT.QFT4D.01` | „Die natürliche TFPT-Brücke ist keine holographische Vermutung, sondern Connes' Spektralwirkung: **ein** Diracoperator, dessen Tr f(D/Λ) Gravitation **und** Materie-Lagrangian liefert.“ Gravitationshälfte `v36` (R+R²) verifiziert; Materiehälfte Vertrag. | [O] mit [E]-Arithmetik |
| `PS.ALGEBRA.01` | A_F = H_L ⊕ H_R ⊕ M₄(ℂ) (Pati–Salam), 16 = (4,2,1)+(4̄,1,2), exakte Hyperladungen, sin²θ_W = 3/8. Caveat (6): SU(4)_c ⊂ SO(10) = D₅ ist **nicht** der Trägerfaktor A₃ = SU(4)_Familie. | [E]/[O] |
| `PS.DIRAC.02` | volles 96-dim endliches Spektraltripel (3 × 32 = 3 Generationen × Teilchen/Antiteilchen), KO-Dimension 6, 5 von 7 NCG-Axiomen [E]; Orientierbarkeit/Poincaré nur in der CCM-abgeschwächten Form (`PS.NCG.ORIENT.02`). | [E]/[C]/[O] |
| `PS.DIRAC.03` | **D_F ist die modulare/Kovarianz-Induktion des Seam-KMS-Zustands (β = 1), eingeschränkt auf den Träger — kein Posit.** H = log((1−C)C⁻¹), Yukawas = Auslese von C_Σ. | [E]/[C] |
| `QFT4D.RGTEST.01` | Kill-Test der Spektralwirkungsvorhersage g₁=g₂=g₃ an gemessenen Kopplungen: im reinen SM **verfehlt** (1-Loop-Spreizung ≈ 9, 2-Loop ≈ 3,2 bei 1,7·10¹⁴ GeV); „no admissible threshold source; likely falsified unless extended“. | **[X]/[O]** |

Einordnung: Das ist der einzige Ort im Korpus, an dem „Algebra + Zustand → Dynamik“ tatsächlich ausgeführt ist —
der endliche Diracoperator wird aus dem modularen Hamiltonoperator des Seam-Zustands *abgeleitet* (genau das, was die
Berichte vom 10./11. 9. als fehlend bezeichnen). Meine Türenliste (§8) hat diese Brücke nicht geführt; die
Universalraum-Rotorrunden laufen an ihr vorbei. Und sie trägt einen offenen **[X]**: Die erste Datenkonfrontation der
Spektralwirkung scheitert ohne neue Zustände. Das ist der wichtigste offene Befund an der Dynamikfront, den keiner
der eingefügten Berichte nennt.

**Abbildung der „U“-Skizze auf Tür 5.** „Phasentreuer Raum kompositionsfähiger Transformationen mit positiver
Struktur, Maß/Wirkung und Auswahlmechanismus“ = Spektraltripel (A, H, D, J, γ) mit Spektralwirkung; „TFPT als
Kristall von U“ = der endliche Faktor F im fastkommutativen Produkt M × F (der Träger liegt nicht *hinter* einem
Rand, sondern ist Faktor); „Zeit aus dem Zustand“ = Connes–Rovelli (zitiert in `changelog.tex:8173`) bzw. `PS.DIRAC.03`;
„Zahlen aus Komposition“ = Bost–Connes (Kill-Regel in `compiler_necessity.md` §C). Was Tür 5 **nicht** liefert und
die Skizze verlangt: die 3+1 Dimensionen und die Lorentz-Signatur (M⁴ ist Eingabe; Connes' Rekonstruktionssatz läuft
von der kommutativen Algebra zur Mannigfaltigkeit, nicht zur Zahl 4), eine Quantisierung der Spektralwirkung, und
eine Klassifikation ohne die Annahmen KO-6/Irreduzibilität/erste Ordnung. Das „Gesetz, das die gemeinsamen
Korrelationen auswählt“ existiert also als Kandidat — Spektralwirkungsprinzip + Klassifikation endlicher Tripel —
und steht unter [X].

**Bewertung der eingefügten Mathematik (Berichte „Rekonstruktionssatz“).**
- Δ_a = R_a − B_a†G⁻¹B_a = T†a†(I−P)aT: korrekt; identisch mit dem Leck-Satz in `fable/PROOF.md` (Thm 1) und Codex' Γ*Γ;
  Mehroperator-Fassung ist dieselbe Identität je Erzeuger; Eindeutigkeit bis auf Unitäre = GNS. Klassisch (Krylov/Schur).
- „TFPT-Viererblock, Δ = 0 exakt“: für jede 4×4-Matrix mit zyklischem ψ tautologisch (Krylovraum = Gesamtraum).
  „H₅ mit gleichen m₀…m₇, anderem m₈“: Gauß-Quadratur-Exaktheit (n Knoten ↔ Grad 2n−1 = 7). Die konkrete Matrix
  (det = −383/95551488, enthält δ = 383/96 aus `det-wall-hh-rule`) ließ sich nicht lokalisieren; die Dimer-Wand h(A)
  liefert für alle (ε, M) det = −1/47775744 (Faktor 383/2). Für die Aussage irrelevant.
- Z(𝒪)_sa = ℤ·I, a²+b² ≠ 3: trivial bzw. χ₋₄-Zensus (inerte Primzahlen), im Korpus vorhanden.
- „Modularer Fluss von ρ = I/2 trivial ⇒ aus Markensymmetrie entsteht keine Zeit“: für den Zweierblock richtig, für den
  Seam falsch — der Seam-Vakuumzustand ist nicht tracial, K = log((1−C)C⁻¹) ist nichttrivial und wird in `PS.DIRAC.03`
  genau dafür benutzt.
- H₁/H₂-Gegenbeispiele (gleiche Z₄-Uhr, verschiedene Dynamik): richtig, trivial, vom Repo nie bestritten
  („elektrische Uhr ≠ Rotor“, `KONSOLIDIERTER-STAND-CODEX.md` §1).
- Smith-Normalform-Zählung, Bost–Connes-Konstruktion: Standard; BC als *angesetzte* Zeit bleibt Kill (§8).

## 11. „Lös das“: QFT4D.RGTEST.01 mit dem quelleigenen Pati–Salam-Inhalt, 1- und 2-Loop (11. 9., 18:10)

Prüfer: `check_ps_two_step_unification.py` (exakt, 1-Loop, Fractions) und `check_ps_two_loop.py` (RK4, 2-Loop
gauge-only, Machacek–Vaughn-Formel gegen die SM-Einträge b₃₃ = −26, b₂₂ = 35/6, b₂₃ = 12 validiert); beide `-OO`
bytegleich. Eingaben ausschließlich aus dem Repo: α_i⁻¹(M_Z) und SM-Betas (`v246`), Matching (`v248`), erlaubte
Skalare {10, 16, 45}, kein 126 (`PS.E8BRANCH.01`), M_s = c₃^{7/2} M̄_Pl = 3,06·10¹³ GeV (`v249`).

**Korrektur meines Stands von 18:00.** Der [X] von `QFT4D.RGTEST.01` gilt für den *reinen SM-Lauf*. Das Repo hat am
selben Tag (`v249_ps_unification.py`, `PS.RGTEST.01`) die Zweistufe SM → PS → Vereinigung gerechnet, mit
Skalenkoinzidenz M_PS ≈ M_s und einer scharfen Protonzerfalls-Ecke. Meine Rechnung reproduziert v249 ziffergenau
(B_MIN: M_PS = 4,19·10¹³, Λ = 2,43·10¹⁵, 1/α_U = 45,1; B_45: Λ = 5,89·10¹⁵, τ_p = 1,55·10³⁵ a).

| Inhalt oberhalb M_PS (komplexe Skalare) | Loops | M_PS [GeV] | Λ [GeV] | 1/α_U | M_PS/M_s | τ_p [a] (v249-Formel) | > Super-K 2,4·10³⁴ |
|---|---:|---:|---:|---:|---:|---:|---|
| Bidoublet + (4̄,1,2) [v249 B_MIN] | 1 | 4,19·10¹³ | 2,43·10¹⁵ | 45,1 | 1,37 | 4,4·10³³ | nein |
| dito | 2 | 3,69·10¹³ | 1,20·10¹⁵ | 44,4 | 1,21 | 2,5·10³² | nein |
| + (1,1,15) [v249 B_45] | 1 | 4,02·10¹³ | 5,89·10¹⁵ | 45,5 | 1,31 | 1,6·10³⁵ | **ja** |
| dito | 2 | 3,54·10¹³ | 2,77·10¹⁵ | 44,8 | 1,16 | 7,4·10³³ | **nein** |
| volles 16_H + (1,1,15) | 1 / 2 | 5,04 / 4,37·10¹³ | 4,95 / 2,36·10¹⁵ | 44,9 / 44,3 | 1,65 / 1,43 | 7,6·10³⁴ / 3,8·10³³ | ja / nein |
| volles 16_H + (1,1,15) + (1,1,6) | 1 / 2 | 5,04 / 4,37·10¹³ | 6,39 / 2,99·10¹⁵ | 45,0 / 44,4 | 1,65 / 1,43 | 2,1·10³⁵ / 9,9·10³³ | ja / nein |
| Kontrolle 126-Typ (1,3,10), E₈-verboten | 1 / 2 | 5,5·10¹¹ / 1,4·10¹¹ | 1,1·10¹⁶ / 8,0·10¹⁵ | 45,7 / 45,1 | 0,02 / 0,005 | 2·10³⁶ / 5·10³⁵ | ja, aber Koinzidenz verloren |

Strukturelle Beobachtung: Für jeden L↔R-symmetrischen Inhalt (b₂L = b₂R) ist M_PS **inhaltsunabhängig** und nur
durch den SM-Lauf bestimmt (die Bedingung α₂L = α₂R bei M_PS): 5,04·10¹³ (1-Loop), 4,37·10¹³ (2-Loop). Die
Koinzidenz mit der Skalaronskala c₃^{7/2} M̄_Pl (Verhältnis 1,2–1,6) ist also eine Aussage über SM-Daten plus c₃,
nicht über Skalarwahl. Das ist die TFPT-spezifische, falsifizierbare Zahl in diesem Block: die B−L/Seesaw-Skala.

**Ergebnis.** (1) Vereinigung: ja, robust, in allen E₈-erlaubten Inhalten, Λ = 1,1–3,0·10¹⁵ GeV bei 2-Loop.
(2) Skalaronkoinzidenz: überlebt 2-Loop (1,16–1,43; v249 erwartete „~1,0–1,2“). (3) Protonzerfall: **die 1-Loop-
Rettung durch das lichte (15,1,1) hält bei 2-Loop nicht** — Λ halbiert sich, τ_p fällt um Faktor 2,4–6 unter
Super-K, bei allen E₈-erlaubten Inhalten. Das ist die „scharfe Ecke“ aus `v249` §6(c), und bei 2-Loop liegt sie
auf der falschen Seite — innerhalb der Faktor-wenige-Unsicherheit von τ_p-Vorfaktor, Schwellen bei M_PS/Λ und
vernachlässigten Yukawa-Termen, also *disfavoured*, nicht ausgeschlossen. (4) Der Protonzerfalls-Bound greift nur,
wenn SO(10) oberhalb Λ **geeicht** ist (X-Bosonen der Masse Λ); das ist v249's Residuum (a), die „gauging fork“.
Ist SO(10) nicht geeicht, ist Λ nur der Treffpunkt der drei PS-Kopplungen und (3) ist keine Einschränkung.

**Was den Block schließen würde:** (i) 2-Loop mit Yukawa-Termen und Schwellenkorrekturen aus einem bezeichneten
Massenspektrum; (ii) eine kanalaufgelöste τ_p-Rechnung (p → e⁺π⁰) statt des v249-Vorfaktors; (iii) die Entscheidung
der gauging fork aus der Quelle. Kein Marker bewegt; `PS.RGTEST.01` bleibt [E]/[C]/[X] wie eingetragen, ergänzt um
den 2-Loop-Befund.

**Zweite Frage („warum M⁴, warum Lorentz“):** nicht gelöst, von niemandem. Stärkste verfügbare Aussage im Rahmen von
Tür 5: KO-Dimension 6 des endlichen Tripels (`PS.DIRAC.02`) plus die Forderung, Fermionverdopplung durch die
Pfaffian-/Majorana-Wirkung zu beseitigen, erzwingt KO(M × F) ≡ 2 mod 8, also dim M ≡ 4 mod 8 (Barrett 2007; Connes
2006) — eine Einschränkung modulo 8, keine Herleitung von 4. Die Lorentz-Signatur kommt im Repo nur über die
OS-Rekonstruktion (Tür 4, (2,2) erzwungen in `v565`), nicht aus dem Tripel.

## 12. P3-Gate am realen Ringparent: „Bestimmt der Zustand den Generator in der lokalen Klasse?“ (12. 9.)

Prüfer: `check_state_selects_generator.py` (`-OO` bytegleich; Fluss-Cutoff K = 8 und 12 identisch). Modell: der
Repo-Ring (`fable/cap_dynamics.py`), **voller** neutraler Gauss-Sektor (70 Materiemasken × Schleifenfluss, 1190
Zustände), nicht das 70-dim. Ersatzmodell der Vorlage. Operatorklasse 𝒱 = ein selbstadjungierter Operator je
Termtyp der lokalen Grammatik (Koeffizienten nicht benutzt): N_L, N_H, E², T_LL, T_LH, T_LL2, I.
Test: Γ_ij = Re⟨O_iψ,O_jψ⟩ − ⟨O_i⟩⟨O_j⟩, Kern modulo der trivialen Relationen {I, N_L + N_H − 4I = 0 auf dem Sektor}.

| Zustand | Klasse | Nullität mod trivial | λ_min⁺ | Koeff.-Residuum |
|---|---|---:|---:|---:|
| Grundzustand | lokal (7) | **1** | 1,3·10⁻⁶ | 1,4·10⁻¹² |
| 1. Anregung | lokal | 1 | 8,7·10⁻⁴ | 2,7·10⁻¹² |
| Grund + 1. Anregung | lokal | 1 | 1,7·10⁻³ | 2,7·10⁻¹² |
| Produktzustand Ω₀ | lokal | 4 | – | – (scheitert) |
| Grundzustand | + T_HH, + E⁴ | **3** | 2,7·10⁻⁶ | 3,6·10⁻¹³ |
| 1. Anregung | + T_HH, + E⁴ | 2 (+1 fast-null 6·10⁻⁷) | 8,7·10⁻⁴ | 1,2·10⁻⁸ |
| Grundzustand | + H², H³ (Polynomfalle) | 3 | – | – |

**Ergebnis 1 (positiv, ohne Fit):** Aus dem Grundzustand allein, mit T_LL = 1/12 als Normierung, rekonstruiert der
Kern exakt T_LH = 1/24, T_LL2 = 1/576, E² = 1/200 und N_H − N_L = 3,9895833 = 383/96 = M − ε_L (auf 10⁻¹¹). Der
Zustand bestimmt den Generator in der lokalen Klasse eindeutig. Das ist das Gate-Ergebnis „(1) genau die bisherige
Richtung“ der Vorlage — *für die inverse Richtung* (H → ψ → H), also Rekonstruktion, keine Vorhersage (rote Linie 1).

**Ergebnis 2 (negativ, physikalisch relevant):** Erweitert man die Klasse um die nicht im Parent enthaltenen, aber
lokal zulässigen Terme T_HH (HH-Hop) und E⁴, wird der Kern dreidimensional: die Richtungen T_LL + T_HH (Varianz
1,5·10⁻¹³) und E² − E⁴ (2,8·10⁻¹⁰) sind im Grundzustand praktisch null, weil er fast keinen H-Anteil hat und auf
|E| ≤ 1 lebt (dort E⁴ = E²). Auch die erste Anregung (Flussanregung) behebt das nicht. **Die niedrigliegenden
Zustände dieses Parents enthalten keine Information über die HH-Regel und über die Form der elektrischen Energie
oberhalb |E| = 1.** Genau die Prämisse von `det-wall-hh-rule` (HH = 0, onsite) kann also nicht aus dem Grundzustand
kommen; sie braucht Zustände mit Energie ≳ M = 4 oder eine unabhängige Quelle — konsistent mit dem [C] dort.

**Ergebnis 3 (Falle bestätigt):** H², H³ in der Klasse vergrößern den Kern per Konstruktion — die Klasse 𝒱 muss
polynomfrei/lokal *aus der Quelle* begrenzt sein (P1 der Vorlage), sonst ist P3 leer.

**Kondition:** Grundzustand λ_min⁺ = 1,3·10⁻⁶ (Konditionszahl 6·10⁶), Grund + Anregung 1,7·10⁻³. Die Warnung der Vorlage
(schlechte Kondition des reinen Grundzustands) bestätigt sich am Ring.

**Thermische Zustände:** kein Kovarianztest nötig — für ρ = e^{−βH}/Z ist −(1/β) log ρ = H + const exakt (§3B); die
Eindeutigkeit in einer linear unabhängigen Klasse ist dann trivial. Der informative Test ist der Kovarianzkern reiner
Zustände.

**Einordnung der Vorlage (Programm mit Gates).** Methodisch richtig und größtenteils Repo-Praxis: Ledger + typisierte
Prämissen [E]/[C]/[O] + `veri{}` sind die geforderte Auditstruktur; „externally inserted inputs“ heißt im Repo
„typed premises“. Zwei Korrekturen: (a) N_fam = 3 ist Compiler-Output (`v189`: rank H₁(P¹∖μ₄) = 3), nicht Eingabe;
(b) das „Gauging Gate“ ist v249-Residuum (a). Nicht im Repo auffindbar: das 70-dim./17-Operator-Modell, die
Zahlen 2,74·10⁻¹⁴ / 3,54·10⁻⁵, `h + εh³`, `H₇₀ + tF` — ChatGPT-seitig. P0 („primitive Quelle einfrieren“) ist eine
normative Autorenentscheidung; heute primitiv laut Ledger: `AX.P1.01` (c₃), `AX.P2.01` (g_car), μ₄ ⊂ P¹, und —
als *gewählte* Realisierung — das Kragenmodell `v367`. Der „eine Versuch“ (ω, 𝒱 aus der Quelle ohne H) ist heute
nicht ausführbar, weil diese Quelle noch nicht als Spezifikation existiert; das Gate selbst steht mit diesem Prüfer
bereit.

## 13. Manuskript 14. 9. („Vom Compiler zum Prozess mit Aufzeichnung“) und die drei Folgefragen (14. 9., 06:30)

**Prüfung.** Beide Codex-Audits laufen grün und `-OO`-bytegleich: `compiler-origin-audit-20260913/run_checks.py`
(11 214 Prüfungen, 11 zurückgewiesene Mutanten), `compiler-extension-audit-20260914/run_checks.py`. Die 60 Strahlen
sind hash-gepinnt aus `v783`. Damit sind Spektrum {1, 3/7¹⁵, 2/7⁹, −2/7⁵, 0³⁰}, Faktorisierung T = (CᵀBC + FᵀF)/28,
Kontextfamilie K_abc, Präparationsabhängigkeit, Tetramer-Spektrum (0,1),(2,45),(3,40),(4,135),(6,35) und die
Zweizellen-Schranke im Repo maschinell gedeckt; ich habe sie nicht erneut gerechnet. Das Manuskript ist in seiner
Evidenztypisierung sauber (gesetzt/exakt/bedingt/offen) und nennt seine Zusatzannahmen (J, Graph, Präparation).

**Die drei Folgefragen, gerechnet** (`check_cells_and_clock.py`, exakt über Schur–Weyl: H liegt in der
S_n-Algebra, Youngs Orthogonalform je Irrep ≤ 4 Zeilen, SU(4)-Vielfachheit per Hook-Content; kein 65 536-dim.
Eigenproblem).

*Q1 — Folgt die Wechselwirkung aus dem Compiler?* Teilweise, und zwar präzise: Die A₃ = SU(4)-Zerlegung der 248 aus
den echten Wurzeln ist {1: 45, 15: 1, 6: 10, 4: 16, 4̄: 16}. **Sym²(4) = 10 kommt in E₈ nicht vor**, Λ²(4) = 6 (der
(10,6)-Block) schon. Der Tetramer-Paarterm (I+S)/2 ist der Projektor auf Sym²(4), also auf den E₈-fremden
Paarsektor; Nullenergie liegt genau auf dem E₈-nativen antisymmetrischen Paar. Das ist eine Auswahlregel derselben
Art wie `PS.E8BRANCH.01` („E₈ verbietet die 126“): der Compiler legt *Vorzeichen und Struktur* der Austauschkopplung
fest, nicht J, nicht den Graphen, nicht die Cross-Register-CZ. Antwort auf die Tabellenfrage: Die Verbindung steht
als Sektorregel im Regelbuch; die Stärke ist dazugeschrieben.

*Q2 — Veränderung und auslesbare Uhr.* Am Singulett Ω = Λ⁴ℂ⁴ (numerisch verifiziert): A^{⊗4}Ω = det(A)·Ω — die
kollektive Uhr ist unsichtbar. Der relative Tick c auf **einem** Träger liefert ⟨Ω|c₁ⁿ|Ω⟩ = tr(cⁿ)/4 und die
Paarenergie p₁ⱼ = (16 − |tr cⁿ|²)/24 (alle anderen Paare 0). Mit c = iσ, σ³ = I (Familien-3-Zykel, `v774`):
n ≡ 0 mod 3 ⇒ cⁿ = iⁿ·I, p = 0, Rückkehr mit Phase iⁿ; sonst p = (16 − |tr σ|²)/24. Für den Clifford-Lift eines
symplektischen 3-Zykels mit drei festen, paarweise antikommutierenden Paulis ist |tr σ| ∈ {2, 0}, also p ∈ {1/2, 2/3},
⟨H_tet⟩ = 3Jp. **Die sechs Paar-Energietests des Manuskripts lesen die Uhr mit Periode 3 (Ordnung von Ad_σ);
der Übertrag iⁿ mit Periode 12 (Ordnung des Lifts) steht nur im Überlapp und braucht eine Interferenzreferenz.**
Das ist die quantitative Fassung des Hinweises im Manuskript §12.4. Offen bleibt, welcher Lift (|tr σ| = 2 oder 0)
der Quellchart ist — eine Zeile in `v783/v774`, kein neues Prinzip.

*Q3 — Viele gekoppelte Zellen.* Zwei vollständige Tetramer-Zellen + eine Brücke λ (exakt): Grundzustand **für alle
getesteten λ ≤ 6J eindeutig** (Irrep (2,2,2,2), Singulett); Gap 2,00 / 1,92 / 1,82 / 1,59 / 1,38 / 1,34 / 1,21 / 1,00
bei λ = 0 / 0,5 / 1 / 2 / 3 / 3,2 / 4 / 6. Die Manuskript-Schranke 2J − 5λ/8 gilt, ist aber sehr lose (bei λ = 16J/5 =
3,2: Schranke 0, tatsächlich 1,34). Ringe aus Viererketten-Segmenten (nächste Nachbarn, Zwischenkopplung λ): 2 und
3 Zellen, Grundzustand eindeutig, Gap 0,25–0,46, Ein-Anregungs-Band der Breite ≈ 1,7 — **wandernde Anregungen**.

**Die eigentlich neue Brücke (nicht im Manuskript):** Bei λ = J ist der Ring die uniforme SU(4)-Sutherland-Kette.
Exakte Ringe n = 4, 8, 12 liefern Gap·n = 3,700 (n = 8), 3,663 (n = 12) gegen die WZW-Vorhersage
2πv(h+h̄) = 2π·(π/4)·(3/8+3/8) = **3,701**; E₀/n → 0,08773 (Fit) gegen (1+e_P)/2 = 0,08744 mit Sutherlands
e_P = 1 − ½[ψ(1) − ψ(¼)]; aus dem 1/n-Term c_fit = 3,16 gegen **c = 3**. Der uniforme Grenzfall der Trägerkette ist
also numerisch die SU(4)₁-WZW-Theorie — **und (A₃)₁ mit c = 3 ist genau der Familienfaktor des TFPT-Seams**
(c = 8 = 5 + 3, (D₅)₁ ⊗ (A₃)₁ ⊂ (E₈)₁). Die Kette aus Compiler-Trägern mit der E₈-selektierten antisymmetrischen
Austauschregel fließt im uniformen Limes auf den A₃-Teil des Seams. Das ist eine prüfbare Brücke von der Zelle zur
Feldbeschreibung (Affleck 1988 für SU(N)-Ketten; hier für N = 4 gegen die Compiler-Zahlen nachgerechnet). Für
λ < J ist die Kette tetramerisiert und gapped (eindeutiger Grundzustand); λ = J ist der kritische Punkt. **Was daraus
nicht folgt:** der (D₅)₁-Faktor (die 10 + 6 Majoranas des Kragens) und die Verklebung zu (E₈)₁ — dafür müssten die
Trägerketten an die Spinorsektoren (16,4) koppeln; genau diese Kopplung ist der Q1-Rest.

**Welche Follow-ups bringen wirklich weiter (Rangfolge):**
1. **Q1 auf die Brücke anwenden:** Ableitung einer effektiven Träger–Träger-Kopplung aus der E₈-Klammer
   (16,4)⊗(16̄,4̄) → (1,15)+(10,6) (Superaustausch über den Spinorsektor). Erfolg = J und Graph aus Strukturkonstanten
   statt gesetzt; Kill = jede Vorzeichenfreiheit, die Sym²(4) erlaubt.
2. **Q3 skalieren:** n = 16 (vier Zellen) und die Dimerisierungs-/Tetramerisierungsgrenze λ_c(n); Ziel: Gap → 0 nur
   bei λ = J, sonst uniform gapped (Plaquette-Phase). Dann Anschluss der (A₃)₁-Kette an (D₅)₁ prüfen.
3. **Q2 pinnen:** |tr σ| aus der Quellchart (`v783`), dann die Uhrenauslese als Sechs-Paar-Protokoll fixieren; die
   Phasenreferenz für die Periode 12 ist eine benannte Zusatzressource, kein Nebenprodukt.
Nicht weiterführend: weitere Kontextregeln K_abc oder Präparationsprotokolle ohne Quellauswahl — die Familie ist
vollständig klassifiziert (Manuskript §10.1); mehr Punkte im Simplex bringen keine Herkunft.

## 14. Follow-ups Q1–Q3 ausgeführt; Anschlusspaper (14. 9., 07:15)

`check_followups_q1q2q3.py` (22 s, `-OO` bytegleich): **Q1** Hüllensatz — Nullraum der Paar-Antisymmetriebedingungen
hat Dimension 1 (vier Träger, = Ω) und 0 (fünf Träger); alle 960 geordneten (16,4)-Wurzelpaare mit Wurzelsumme
landen in (10,6). **Q2** Der Familien-3-Zykel fixiert 3 Kontexte {IX,XI,XX},{IZ,ZI,ZZ},{XZ,YY,ZX} und 0 Paulis;
|tr(φ·P·c)| = 1 für alle 32 Lifts ⇒ p₁ⱼ = 5/8, ⟨H_tet⟩ = 15J/8, Rückkehrphasen 1, −i, −1, i (n = 0, 3, 6, 9).
**Q3** Offene Ketten n = 8, 12, 16 (Sparse-Young, Irreps bis 180 180): Gap bei λ = J/4: 0,266 / 0,255 / 0,250
(gapped); bei λ = J: 0,176 / 0,127 / 0,100 (∝ 1/n); erste Anregung stets in der Adjungierten (a+1,a,a,a−1) → 15.
Kein Schwellenwert unterhalb λ = J.

Anschlusspaper: `paper/tfpt_anschluss_zellen_seam_2026-09-14.tex` → PDF (7 Seiten), Kopie in
`output/pdf/tfpt_anschluss_zellen_seam_2026-09-14.pdf`. Es fasst §§ 8–14 dieses Berichts zusammen: Hüllensatz,
relative Uhr, Zellenketten und (A₃)₁-Brücke, Zustandsgate, PS-Zweistufe 2-Loop, zwei Präzisierungen, eine Korrektur.
Kein Ledger-, Papier- oder Statuseintrag verändert.

## Reproduktion

    cd fable-runde3
    python3 -B check_runde3.py            # checks.json (~1 s; -OO bytegleich)
    python3 -B check_rh_high_block.py 160 240 320   # rh_high_block.json (~6 s)
    python3 -B check_codex_load.py        # codex_load.json (~1 s)
    python3 -B check_hecke_index_net.py   # hecke_index_net.json (<1 s; -OO bytegleich)
    python3 -B check_ps_two_step_unification.py   # ps_two_step_unification.json (<1 s, exakt)
    python3 -B check_ps_two_loop.py       # ps_two_loop.json (~13 s, RK4 2-Loop)
    python3 -B check_state_selects_generator.py 8   # state_selects_generator.json (<1 s)
    python3 -B check_cells_and_clock.py   # cells_and_clock.json (~4.5 min: Schur-Weyl bis n=12)
    python3 -B check_followups_q1q2q3.py  # followups_q1q2q3.json (~22 s: Sparse-Young bis n=16)
    cd paper && pdflatex tfpt_anschluss_zellen_seam_2026-09-14.tex && pdflatex tfpt_anschluss_zellen_seam_2026-09-14.tex

Abhängigkeiten: `../fable/cap_dynamics.py` (Ringparent), `rh/catalog/research_engine/experiments/odd-window-direct-infimum-20260910/probe.py`
(Fensterform), numpy, scipy. Hashes in `QUELLEN.json`. Keine alten Artefakte, Ledger, Kataloge oder Indizes verändert.
