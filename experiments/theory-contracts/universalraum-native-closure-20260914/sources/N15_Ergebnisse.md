# TFPT / Universalraum — Ergebnisse der Schließrunde vom 14. September 2026

**Anlass:** Auftrag „versuche sämtliche Probleme vollständig zu lösen" (Fragen a: vollständige
Rekonstruktion des Universalraums mit TFPT-Anschluss, b: echte Probleme wie RH/Faktorisierung,
c: verbleibende TOE-Probleme).

**Ansatz:** Alles, was endlich und maschinell entscheidbar ist, wurde in dieser Runde
tatsächlich geschlossen — mit exakten, reproduzierbaren Rechnungen. Für den Rest wurden die
exakten Hindernisse mit Zahlen belegt. Kein RH-, Faktorisierungs-, P-vs-NP- oder TOE-Abschluss
wird behauptet. Alle Artefakte liegen in `experiments/` (Firewall); keine Promotion nach
`verification/`, Ledger, Papers oder Website.

**Ort der Artefakte:** `experiments/theory-contracts/universalraum-closure-round-20260914/`
(5 Skripte, 5 Ergebnis-JSONs, alle mit SHA-256 des Prüfers).

---

## 1. Die fünf neuen maschinengeprüften Ergebnisse

### 1.1 [A4] Vollständiger Nichtsingulett-Ausschluss für C16 — das offene Flag geschlossen

**Frage:** Ist der Singulett-Grundzustand des 16-Plätze-Clebsch-Austauschmodells
(H = J·Σₑ Pₑ⁺, 40 Kanten) wirklich der *globale* Grundzustand? Bisher war nur der
Singulettsektor (24 024-dimensional) gerechnet; die anderen SU(4)-Sektoren waren
nicht ausgeschlossen (`full_non_singlet_comparison: false`).

**Was gerechnet wurde:** Der volle Hilbertraum (C⁴)^⊗16 zerfällt in **64 SU(4)-Sektoren**
(Youngdiagramme mit 16 Kästen, ≤ 4 Zeilen). Für jeden Sektor wurden die beiden tiefsten
Eigenwerte des Austausch-Hamiltonoperators auf dem Multiplizitätenraum (Specht-Modul)
bestimmt (dicht bis f = 1 500, Lanczos darüber; Residuen ≤ 1,4·10⁻⁹).

**Exakte Konsistenzanker:**
- Σ_λ d_λ(SU(4)) · f_λ(Specht) = 4¹⁶ = 4 294 967 296 — die Sektorenzerlegung ist vollständig.
- Singulettsektor (4,4,4,4) reproduziert den Anker 11,045398337068436 auf 8,9·10⁻¹⁵.

**Ergebnis:**

| Größe | Wert |
|---|---|
| Globaler Grundzustand | **Singulett (4,4,4,4), E₀/J = 11,045398337068** |
| Erste Anregung (global) | Singulett-**Quartett**, E/J = 11,561762122803 |
| **Volle Modelllücke** | **Δ/J = 0,516363785734** |
| Tiefster Nichtsingulett-Sektor | (5,4,4,3) bei E/J = 12,133537149348 |
| Abstand Singulett → Nichtsingulett | **1,088138812280 J** |

Die fünf tiefsten Nichtsingulett-Sektoren: (5,4,4,3) 12,1335 · (5,5,3,3) 12,3228 ·
(5,5,4,2) 12,8751 · (6,4,3,3) 12,9816 · (6,4,4,2) 13,3133. Die Grundenergie steigt
monoton mit der Unbalanciertheit des Youngdiagramms; der Singulett liegt klar am tiefsten.

**Bedeutung:** Der Grundzustand des C16-Modells ist auf führender Ordnung *bewiesenermaßen*
(numerisch, residuen kontrolliert) der eindeutige Singulett; die Lückenstruktur des
Gesamtmodells ist jetzt vollständig bestimmt. Offen bleiben nur: algebraischer
Multiplizitätsbeweis des Quartetts, ε⁴-Restschranke, CAR-Phasenidentifikation.

*Skript: `nonsinglet_sectors.py` (64/64 Sektoren, 1 032 s).*

### 1.2 [A2] Globaler Vertex-Kohärenzaudit — 16/16 exakte Checks

**Frage:** Ist die reparierte U-Regel (History darf kohärent bleiben) über das ganze
Protokoll hinweg konsistent?

**Exakt bewiesen (ganzzahlig/symbolisch, 0,65 s):**
1. Unaufgezeichneter Vertex: K†K = I − S auf dem vollen 16-dimensionalen Paarraum, Rang 6.
2. Geordnete History zerstört das: K̃†K̃ = I − D_diag, Rang steigt 6 → 12.
3. Interpolationsformel K̃†K̃ = I − D_diag − η(S − D_diag) exakt für η = 0, 1/2, 1;
   nur η = 1 (kohärent) reproduziert den Vertex.
4. Der reparierte Baustein U_W = [[P₊, −W†],[W, 0]] ist **symbolisch unitär** (22-dim).
5. H₂₂-Spektrum exakt: {0^[10], −j^[6], Δ+j^[6]} mit j = (√(Δ²+4g²) − Δ)/2.
6. H_bad-Grundräume: K₄ → dim 24 bei −6κ; Stern → dim 108 = 4·3³ bei −3κ
   (die falsche History zerstört die Ω-Eindeutigkeit — vollständige Enumeration der 256 Wörter).
7. Clebsch-Vermittlerlabels: 40 Kanten, 10 Vektorlabels, jedes von genau 4 Kanten geteilt;
   **kein 4-Kreislauf erlaubt zwei gegenwärtige Paarungen mit derselben Labelmultimenge**
   (der Vollständigkeitskern der F4-Formel aus der Fortsetzung §5.3).
8. Lokaler Symmetriemechanismus exakt: [Σ hₛ, H] = 0 auf zwei angrenzenden Kanten erzwingt
   hᵢ = hⱼ + c·I (Nullraum 18 = 16 gemeinsame + 2 Kantenskalare) — nach Phasenquotient
   bleibt exakt die kollektive su(4), wie die Fortsetzung §9.1 behauptet.

*Skript: `coherence_audit.py`.*

### 1.3 [A5] Angekleideter Stern vs. idealer Filter — 16/16, inkl. korrigiertem Filter

**Frage:** Der mikroskopische Grundzustand ist angekleidet; der ideale 8-Punkt-Filter
ist kein exakter Filter des mikroskopischen Spektrums. Wie groß ist der Mismatch —
und wie sieht der korrigierte Filter aus?

**Ergebnisse (Δ = 1, t = 0,05):**
- Ideales Sternspektrum {0, 1/2, 1, 3/2, 2, 5/2, 3}·J mit Multiplizitäten
  {1, 30, 45, 40, 15, 90, 35} exakt bestätigt (256-dim).
- Angekleidete Niveaus E(g) = (Δ − √(Δ² + 4t²(6−2g)))/2; **Lücke exakt
  0,00243396875137 statt nacktem J/2 = 0,0025**.
- Nacktes Gewicht des angekleideten Grundzustands: **0,9856429311786321** (1,44 % Verkleidung).
- **Der Mismatch ist jetzt eine Zahl:** zur nackten Filterzeit τ* = 4π/J rephasieren die
  angekleideten Niveaus *nicht* — Restphasenfehler **0,2746 rad** (Kontrolle: nackt rephasiert
  exakt). Abstände in Gap-Einheiten sind irrational (0, 1, 2,00477, 3,01439, 4,02892, …).
- **Korrigierter Filter konstruiert:** das Grad-7-Projektorpolynom p(x) = Π_{g>0}
  (x − E(g))/(E(0) − E(g)) in H_eff projiziert exakt auf den angekleideten Grundzustand —
  Projektorfehler **2,4·10⁻¹⁴**. Der „passend ausgelegte Filter", den die Fortsetzung
  forderte, existiert damit explizit.

*Skript: `dressed_star.py`.*

### 1.4 [T1-Mikro] Das Auswahlprinzip der 60-Strahlen-Regel — 15/15 exakt

**Frage:** Was wählt a = 1/7 in der Inzidenzfamilie K_a = aI + (1−a)(B−I)/6 aus?
(Die v1.3-Präzisierung warnte: Kontextentropie wählt 1/7, Strahlennachfolger-Entropie 1/13.)

**Exakte Ergebnisse:**
- Anker: B² = 4I + 3J₁₅, CCᵀ = 4I, FFᵀ = 12I, CFᵀ = 0, Rang T = 30,
  Spektrum T = {1, (3/7)¹⁵, (2/7)⁹, (−2/7)⁵, 0³⁰} — alles exakt bestätigt.
- H_C(a) = −a log a − (1−a) log((1−a)/6): eindeutiges Maximum bei **a = 1/7** (symbolisch:
  Ableitung null, H″ = −(1/a + 1/(1−a)) < 0 auf (0,1)).
- H_R(a) = −a log a − (1−a) log((1−a)/12): eindeutiges Maximum bei **a = 1/13** — *verschieden*.
- **Neue Struktur entdeckt und bewiesen:** Der induzierte Strahlenprozess ist
  W_a = aI + (1−a)R/12 mit **R = 14T − 2I — einer echten Adjazenzmatrix**
  (0/1, symmetrisch, 12-regulär auf 60 Strahlen), Spektrum exakt
  {12^[1], 4^[15], 2^[9], −2^[30], −6^[5]}.
- Daraus die **vollständige Ausnahmemenge in [0,1], bewiesen** (nicht nur abgetastet):
  Rangkollaps genau bei a = λ/(λ−12): **a = 1/7 → Rang 30** (λ = −2, Mult. 30) und
  **a = 1/3 → Rang 55** (λ = −6, Mult. 5); überall sonst Rang 60 (inkl. a = 1/13).

**Konsequenz (präzisiert T1):** „Maximale Entropie" allein wählt *keine* Regel — das
Auswahlprinzip muss die Ausleseklasse deklarieren. Kontextklasse → 1/7 mit Rang-30-Kollaps;
Strahlenklasse → 1/13 mit Rang 60. Die U-Regel kann 1/7 nur über die Kontextauslesung
(oder den Rang-30-Zusammenbruch) begründen.

*Skript: `selection_principle.py`.*

### 1.5 [B1] Die Universalraum→RH-Brücke am echten L*-Objekt — 12/12

**Frage:** Der Vertrag (Gesamtkonstrukt §5, Beilage E) verlangt Q_ζ(g) = ‖Ag‖² für *alle* g,
mit unabhängigem A, gleicher Normierung, gleichen Randtermen, korrekter Nullraumkopplung
und dichter Fortsetzung. Was heißt das konkret — mit Zahlen am echten L*-Objekt des Repos
(flagship z = 16, S = 367, N_w = 184)?

**Ergebnisse:**
1. **Die Wand ist real:** λ_max(E₁₈₄) = 0,99983248 < 1 < λ_max(E₁₈₅) = 1,00003660
   (f64-Reproduktion des versiegelten Rekords).
2. Basisunabhängige Form: Q_n = I − BₙᵀBₙ ist PSD bis zur Halbfüllungstiefe
   (min. Eigenwert +1,675·10⁻⁴) und scheitert einen Grad darüber (−3,66·10⁻⁵).
3. **Randterme sind nicht dekorativ — sie SIND die Kontraktion:** Ohne die archimedischen
   Lag-Beiträge explodiert λ_max auf derselben Tiefe auf **≈ 1,6·10⁴⁹** (statt 0,99983).
   „Dieselben Randterme" ist eine tragende Forderung, keine Formsache.
4. **Die Bildraumbedingung ist exakt, nicht approximativ:** Der ν-seitige Gramblock ist
   ab Tiefe > 104 singulär (Rang 103 bei Tiefe 150 gemessen). Die konsistente Erweiterung
   liegt im Bild (Defekt 1,8·10⁻¹¹); eine *fremde* Spalte hat Defekt 0,56 — und dann macht
   der Nullraum-Hebel (5,7·10⁻²) den erweiterten Block **für jede Wahl des Diagonaleintrags c
   indefinit** (gemessen bei c = 0, 1, 10⁶: stets negative Eigenwerte). Endliche Blöcke eines
   Universalraum-Kandidaten müssen also *exakt* sein und ihre Nullräume korrekt koppeln.
5. **Cholesky ist zirkulär und fortsetzungslos:** Der Faktor aus dem PSD-Block bei N_w
   rekonstruiert Q₁₈₄ auf 5,6·10⁻¹⁶ — und sagt *nichts* über Tiefe 185, wo die Form scheitert.
   Die dichte Fortsetzung trägt die gesamte Arithmetik; der endliche Faktor trägt sie nicht.

**Fazit B1:** Die drei Beilage-E-Anforderungen stehen jetzt jeweils mit einer Zahl am echten
Objekt da. Eine Universalraum-RH-Route braucht: exakte endliche Blöcke + Bildraumkopplung +
die wahre arithmetische Fortsetzung (denselben Randtermen!). Nichts davon ist durch die
bisherigen endlichen E8-/Gram-Identitäten geleistet.

*Skript: `weil_bridge_probe.py` (importiert nur die eigenständigen Dokumentformeln aus
`rh/problem/verify_lstar_instance.py`; KEIN RH-Claim in irgendeine Richtung).*

---

## 2. Was das für die drei Zielfragen bedeutet

### a) Vollständige Rekonstruktion des Raums (inkl. TFPT-Abhängigkeiten)

**Jetzt geschlossen/gefestigt:**
- Vertex-Kohärenz global auditiert (A2) — die reparierte U-Regel ist protokollweit konsistent.
- Auswahlprinzip der Strahlenregel exakt vermessen (T1-Mikro) — inklusive der Entdeckung,
  dass R = 14T − 2I die 12-reguläre Strahlengraph-Adjazenz ist.
- C16-Grundzustand und Lücke vollständig bestimmt (A4, führende Ordnung).
- Filter-Dressing quantifiziert und korrigiert (A5).

**Weiter offen (mit präzisem Rest):**
- **A1/T1:** native *Ableitung* der Architektur aus P1+P2 (die Auswahl ist jetzt vermessen,
  aber nicht aus den Axiomen erzwungen).
- **A3:** Vermittler-Lokalität (60 globale Moden vs. lokal pro Zelle) — unentschiedene
  Modellgabel, blockiert jeden Vielzellenlimes.
- **A4-Rest:** ε⁴-Restschranke, algebraischer Quartett-Multiplizitätsbeweis.
- **A6:** CAR-/phasentreuer Adapter zwischen C16-Mikromodell und TFPT-Phasen
  (`CAR_native_phase_equivalence` weiterhin false) — die zentrale offene Brücke.
- **A7/T2:** native chirale E8-Naht mit Skalierung.
- **A8:** die externen Prüfer der Vormittagsrunde (89 Checks, mikroskopische 4. Ordnung)
  gehören weiterhin ins Repo eingepflegt.

### b) Echte Probleme lösen (RH, Faktorisierung, …)

- **RH:** Der Brückenvertrag ist jetzt mit Zahlen am echten L*-Objekt präzisiert (B1).
  Der eigentliche offene Kern bleibt L* (`PRIME.LSTAR.SUBORDINATION.01`, 57/57 gemessen,
  eine Spur ist am dokumentierten Stop). Der Universalraum kann erst beitragen, wenn er
  die *signierte* Differenzform mit denselben Randtermen phasentreu darstellt — gemessene
  Anforderungen siehe 1.5.
- **Faktorisierung:** Die No-go-Resultate stehen (Fourier-Gleichverteilung bewiesen;
  Momenteninversion O(N) = exponentiell). Nichts Neues nötig/möglich ohne ein vollständig
  spezifiziertes kohärentes Verfahren mit Kosten in log N — weiter offen.
- **Realistisch näherliegend:** Hamiltonoperator-Identifikation (Clebsch/Tetramer/Kette
  über die jetzt vollständig bekannten Spektren), Gedächtnisdiagnostik über die Echos,
  deterministische Präparation als Kalibrierung.

### c) Verbleibende TOE-Probleme

Unverändert offen (T1–T8), aber die mikroskopische Basis ist jetzt deutlich fester:
- T5 hat jetzt: vollständige 4. Ordnung + *globalen* Grundzustand und Lücke für C16.
  Nächste Pflichten: ε⁶-Rest, Vielzellen (braucht A3-Entscheidung), Kontinuum.
- T3/T4/T7/T8 und die finalen Fragen (Dunkle Materie/Energie, Baryonasymmetrie, starkes CP,
  schwarze Löcher) bleiben Forschungsfront — keine Session-Schließung möglich, keine behauptet.

---

## 3. Reproduktion

```bash
cd experiments/theory-contracts/universalraum-closure-round-20260914
python3 coherence_audit.py        # 16/16, ~1 s, exakt
python3 dressed_star.py           # 16/16, ~1 s
python3 selection_principle.py    # 15/15, ~4 s, exakt
python3 weil_bridge_probe.py      # 12/12, ~5 s
python3 nonsinglet_sectors.py     # 64/64 Sektoren, ~17 min
```

Jedes Skript schreibt ein gleichnamiges `.json` mit allen Zahlen und dem SHA-256 des
Prüfers; jedes bricht mit Fehler ab, wenn ein Kriterium verletzt ist.

**Gesamtstand nach dieser Runde:** 59 neue benannte Prüfungen bestanden
(16 + 16 + 15 + 12) plus die 64-sektorige vollständige Spektralzerlegung.
Der mikroskopische Kern des Universalraums ist jetzt deutlich fester geschlossen;
die großen offenen Punkte (native Auswahl, Phasenadapter, Vermittlerlokalität,
chirale Naht, L*, Skalierung) sind unverändert offen — jetzt aber mit exakt
vermessenen Eintrittsbedingungen.

*Erstellt 14.09.2026. Forschungsstand, kein begutachteter Abschluss. NON-RH.
Keine Promotion nach verification/, Ledger, Papers oder Website.*
