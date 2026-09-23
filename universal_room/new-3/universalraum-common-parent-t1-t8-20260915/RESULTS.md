# Ergebnisse · universalraum-common-parent-t1-t8-20260915

**TFPT / Universalraum · gemeinsamer Parent T1–T8 · 15. September 2026 · research-only**

## 1. Exakte Replay-Zusammenfassung

Der Replay (`replay.py`, Repository-Root) lief **PASS** ohne jeglichen Skript-,
Test- oder Build-Aufruf durch diese Dokumentation — alle Zahlen stammen aus
`REPLAY.json` und `verification_normal.json` als Quellen.

| Größe | Wert |
|-------|------|
| `status` | **PASS** |
| `toe_complete` | **false** |
| `closed_gate_ids` | **`[]`** (kein Tor geschlossen) |
| `total_exact_checks` | **125** |
| `source_hashes_total` / `source_hashes_verified` | **21 / 21** |
| `byte_identical` (normal vs. `-OO`) | **true** (alle 5 Module) |
| `parent_id` | `tfpt-universalraum-common-parent-t1-t8-20260915:0804f4a5bc73a17f` |

**Aufschlüsselung der 125 exakten Checks** (Methode: Summe der Modul-Own-Checks
plus die 10 Own-Checks des Cross-Gate-Moduls; keine Doppelzählung):

| Modul | `exact_checks` |
|-------|---------------|
| `parent_model.py` | 10 |
| `seam_lift.py` | 52 |
| `gates_t1_t4.py` | 24 |
| `gates_t5_t8.py` | 29 |
| `cross_gate.py` (Own-Checks) | 10 |
| **Summe** | **125** |

Alle fünf Module lieferten `normal_returncode = 0`, `optimized_returncode = 0`,
gültige JSONs und `byte_identical = true`. Die 21 Quell-Hashes (Verträge,
Suite-Module, Universalraum-Quellen inkl. `native_common.py` und `W.npz`)
stimmen exakt mit den deklarierten SHA-256 überein.

**Bedeutung von `status = PASS`:** Checker-Integrität, nicht
Tor-Abschluss. Der `parent_spec.verdict.status_pass_means` lautet ausdrücklich
*„checker integrity only; no gate is moved“*. `PASS` heißt: die Maschine ist
konsistent gelaufen und hat ihre eigenen Checks bestanden — **kein** physikalisches
Tor T1–T8 wurde dadurch geschlossen.

## 2. Eine gemeinsame Parent-Spezifikation — eine Identität

Alle vier fachlichen Module (`parent_model`, `seam_lift`, `gates_t1_t4`,
`gates_t5_t8`) exportieren dieselbe kanonische Parent-Identität

```
tfpt-universalraum-common-parent-t1-t8-20260915:0804f4a5bc73a17f
```

Der Cross-Gate-Check `cross.identical_parent_id_all_modules` bestätigt das.
„Gemeinsamer Parent“ heißt hier: **dieselbe** ausgewählte Mikrostruktur soll
alle acht Tore T1–T8 zugleich tragen — nicht acht getrennte Toy-Modelle. Die
Identität gehört derzeit zu einer **Prüfspezifikation**, nicht zu einem bereits
physikalisch konstruierten Parent. Sie sichert nur: alle Checks reden über
dasselbe deklarierte Objekt.

## 3. Erster Fehlschlag und Korrektur

Der erste Replay-Versuch scheiterte an der behaupteten Inzidenz-Relation
`J^T D L = D`. Die Ursache war zweifach:

1. **Falsche Kanten-Konvention:** Die Inzidenzmatrix `D` wurde mit der
   falschen Orientierung der Kanten `e → e+1` aufgestellt.
2. **Vermischung von Spin-Vorzeichen mit Geometrie:** Die fermionischen
   Lift-Vorzeichen (η = ±1) wurden in die geometrische Inzidenz hineingemischt,
   statt sie als separate, nachgelagerte Wahl zu führen.

Die korrekte, exakte Relation lautet für die Kanten `e → e+1`:

```
|J|^T  D  |L|  =  -D
```

mit **Absolutbeträgen** `|J|`, `|L|` (geometrische Reflexionen ohne Spin-Vorzeichen)
und **negativem** Vorzeichen, weil die Reflexion die Orientierung umkehrt, während
die fermionischen Lift-Vorzeichen η = ±1 davon unabhängig bleiben. Nach dieser
Korrektur läuft das Seam-Modul standalone **52/52 PASS**. Die Relation ist im
`parent_spec.derived` als *„induced vertex->edge reflection incidence:
`|J|^T D |L| = -D` for source edges e → e+1; reflection reverses orientation
while fermionic lift signs remain separate“* eingefroren.

## 4. Per-Gate-Status T1–T8

Alle acht Tore stehen auf `status = partial`, `closed_in_package = false`.
Kein Tor wurde geschlossen. Die folgende Tabelle fasst Status, fehlendes
Element und die gekillte Route je Tor zusammen (Quelle:
`verification_normal.json`).

| Tor | Titel | Status | Fehlt (Missing / Open Gaps) | Gekillte Route(n) |
|-----|-------|--------|-----------------------------|-------------------|
| T1 | Ursprung und Auswahl | partial | Origin Selection (welches Primitive fixiert den Ursprung) | derive-primitive-from-target (target-derived mutation) |
| T2 | Half-Charge und E8-Feld | partial | **raw seam → four 64-mode W-bank intertwiner** (offener Blocker, **keine** gekillte Route); Half-Charge; energy/adjoints; scaling limit | same-vertex double seam action (non-commuting) |
| T3 | Gemeinsamer 3+1D-Parent | partial | deklarierte `spatial_dimension` (3+1D-Auswahl) | local-normalization-fixes-chart (Gram-Det unterscheidet sich: detA=1/2, detB=20/27); local-normalization-fixes-spectrum (trA2=9/2, trB2=11/3) |
| T4 | Chirale Materie | partial | native chiral measure; interacting mirror gap (außerhalb des 2D-Rotationsansatzes) | kommutierender Skalarbilinear-Ansatz als chirales Maß; interacting mirror operator im 2D-Rotationsansatz (representation mismatch, **scoped**) |
| T5 | Kontinuum und Dynamik | partial | Kontinuum-/thermodynamischer Limes des nativen Zyklus; operator-state instrument; scattering instrument | naive-cycle-uniform-gap |
| T6 | Parameter und Spektren | partial | gemeinsames normiertes W[J]-Transferfunktional; gauge couplings aus einem W[J]; Massen/Neutrino-Textur aus einem W[J]; eindeutige Lift-Auswahl aus sechs Kandidaten | (keine gekillte Route; Non-Uniqueness-Zeuge) |
| T7 | Gravitation (Spin-2) | partial | dynamical massless spin-2; universal dynamic coupling am Parent | uniform-mediator-as-dynamical-spin-2 |
| T8 | Zustand und Instrumente | partial | state selection functional jenseits der Energy Gap; native state preparation; native instrument channel; native record channel | unique-gs-energy-gap-as-sufficient-selector |

### T1 — Ursprung und Auswahl
Bewiesen: primitive grammar records sind über einem festen Alphabet typisiert;
target-derived mutation wird vom Typisierer zurückgewiesen. Offen bleibt die
**Origin Selection**: welches Primitive den Ursprung fixiert. Die Route
„ableiten vom Ziel her“ ist gekillt, weil sie eine target-derived Mutation
erfordert.

### T2 — Half-Charge und E8-Feld
Bewiesen: `J_η` ist für η = ±1 eine Involution (`J² = I`); `L_η` ist eine
orthogonale Involution (`LᴴL = I`); `R_η` ist orthogonale Kovarianz
(`RᵀR = I`). Dieselbe Vertexwirkung auf den Paarbänken lässt bei
Nachbarmischung den exakten Defekt `b²` und erlaubt nur `b=0`; dafür ist die
verschobene Kantenwirkung nötig. **Entscheidender offener Blocker** (keine
gekillte Route, sondern
ein fehlender Beweis): der **raw seam → four 64-mode W-bank intertwiner**.
Fehlend außerdem: Half-Charge, energy/adjoints, scaling limit.

### T3 — Gemeinsamer 3+1D-Parent
Bewiesen: beide Charts teilen dieselbe lokale Normalisierung; der globale
Gram-Determinant unterscheidet sie (`detA = 1/2`, `detB = 20/27`); der
Spektral-Invariant unterscheidet sie (`trA² = 9/2`, `trB² = 11/3`). Damit sind
zwei Routen gekillt: lokale Normalisierung fixiert weder Chart noch Spektrum.
Offen: die **deklarierte 3+1D-Auswahl**.

### T4 — Chirale Materie
Bewiesen: Für **kommutierende skalare Amplituden** verschwindet
`pᵀΣp` bei antisymmetrischem `Σ`. Das ist ausdrücklich keine Aussage über
Grassmann-Fermionfelder, deren antisymmetrische Bilineare nicht so
verschwinden müssen. Im 2D-Rotationsansatz überlebt nur ±I im Zentralisator.
Gekillt sind daher nur der kommutierende Skalarbilinear-Ansatz als chirales
Maß und der interacting mirror im 2D-Rotationsansatz (**scoped**). Offen:
fermionisches chirales Maß und interacting mirror gap außerhalb dieses
Ansatzes.

### T5 — Kontinuum und Dynamik
Bewiesen: `s_min(L) = 1 - cos(π/L)` ist exakt und streng monoton fallend für
L = 1..8; `lim_{L→∞} s_min(L) = 0`; es gibt **keine** uniform positive
untere Schranke. Damit ist die naive-cycle-uniform-gap-Route gekillt. Offen:
Kontinuum-/thermodynamischer Limes, operator-state instrument und scattering
instrument am Parent.

### T6 — Parameter und Spektren
Bewiesen: Die drei dark N=3-Blöcke teilen den Gesamt-Casimir 45
(viertel-normalisiert), besitzen aber paarweise verschiedene
`(C_Spin10, C_SU4)`-Paare. Bei fester Summe hat ihre Variation Rang eins:
Der Summencasimir allein wählt keinen der drei Sektoren. Sechs
clock-inverting slot reflections sind Kandidaten-Lifts,
**keine** eindeutige Auswahl. Der Zeuge ist repräsentationstheoretisch, nicht
an Beobachtungsdaten gefittet. Keine Route gekillt; Closure false wegen
Non-Uniqueness. Offen: gemeinsames normiertes W[J]-Transferfunktional,
gauge couplings / Massen / Neutrino-Textur aus **demselben** W[J], eindeutige
Lift-Auswahl.

### T7 — Gravitation (Spin-2)
Bewiesen: der einzige uniform mediator `(1,0)+(0,1)` ist ein antisymmetrischer
2-Form `B_{μν}` (Helizitäten ±1), **nicht** masseloser Spin-2 `(2,0)+(0,2)`
(Helizitäten ±2). `dim(1,0)=2 ≠ dim(2,0)=3`. Der free spin-2-Zeuge ist
vorgeschrieben/bedingt, nicht dynamisch. Gekillt:
uniform-mediator-as-dynamical-spin-2. Offen: dynamical massless spin-2 und
universal dynamic coupling am Parent.

### T8 — Zustand und Instrumente
Bewiesen: untwisted asymmetric ground margin = `8223/31250 > 0` (exakt,
≈ 0.263136); die untwisted asymmetric frame obstruction `a²-b² = -7/25 ≠ 0`
(mit `a = 3/5`, `b = 4/5`). Damit ist unique-GS-energy-gap-as-sufficient-selector
gekillt: Ein eindeutiger Grundzustand allein wählt Quelle und Lift nicht aus.
Offen:
state selection functional jenseits der Energy Gap; native state, instrument
und record am Parent.

## 5. Checker-PASS vs. physikalischer Tor-Abschluss

Diese beiden Begriffe werden im Paket streng getrennt:

- **Checker-PASS** = das Modul hat seine eigenen endlichen Checks bestanden
  (z. B. „`J² = I` für η = ±1`“, „`s_min(L)` streng fallend“). Es ist ein
  Integritäts- und Konsistenznachweis **innerhalb** der formulierten Pflichten.
- **Physikalischer Tor-Abschluss** (`closed_in_package = true`) = alle
  `required_conditions` des Tores sind durch ausführbare Zeugen erfüllt, und
  die `kill_criteria` greifen nicht. **Kein** Tor erreicht diesen Status.

`status = PASS` auf Modulebene heißt ausdrücklich **nicht**, dass ein Tor
geschlossen ist. `closed_gate_ids = []` und `toe_complete = false` sind die
autoritative Anzeige. Wer `PASS` als Tor-Abschluss liest, liest falsch.

## 6. Entscheidender nächster Satz

Das Paket benennt genau einen entscheidenden, noch unbewiesenen Satz als
Nächsten:

> **Raw seam → four 64-mode W-bank intertwiner.**

Die Seam-Geometrie (v622 NS-Kreis: 16 Majorana-Sites, vier Mark-Bonds, Cuts als
Durchmesser, Straddle = through-mark) induziert die verschobene Kanten-Aktion
`L = R J` mit `L² = I` und die korrekte Inzidenz `|J|ᵀ D |L| = -D`. Die
Brücke von dieser Seam-Geometrie zur **vier-Bank, 64-mode W-Bank** (native
`W`-Tensor mit Shape (60, 2016), 480 Nichtnullen, `W Wᵀ = 8 I₆₀`,
`Σ AᴴA = 15 I₆₄`) ist **nicht bewiesen** und bleibt der offene Blocker für T2.
Ohne diesen Intertwiner sind Half-Charge, E8-Feld, energy/adjoints und scaling
limit nicht ansprechbar.

## 7. Skalierung `s_min → 0` und Implikationen

`T5` liefert die exakte Skalierung `s_min(L) = 1 - cos(π/L)` mit
`lim_{L→∞} s_min(L) = 0` und **keiner** uniform positiven unteren Schranke.
Implikationen:

- Die naive-cycle-uniform-gap-Route ist gekillt: man kann nicht argumentieren,
  ein endlicher Zyklus liefere eine uniforme Lücke, die dann ins Kontinuum
  gehoben wird.
- Jede Kontinuums- oder thermodynamische Limes-Aussage muss den **schwindenden**
  Gap explizit behandeln — nicht ihn verstecken.
- OS-Rekonstruktion / positive Transfer-Operatoren bleiben als **Bindung**
  deklariert (T5-Pflicht), nicht als postulierter Text. Der Limes ist offen.

## 8. Gesamtbefund

- Replay **PASS**, 125 exakte Checks, 21/21 Hashes, normal/-OO byte-identical.
- **0 von 8 Toren geschlossen.** `toe_complete = false`.
- Eine gemeinsame Parent-**Prüfspezifikation** besitzt eine durchgängige
  Identität; ein physikalischer gemeinsamer Parent ist damit nicht konstruiert.
- Ein entscheidender Satz ist als nächster benannt: raw seam → W-Bank
  intertwiner.
- Keine Behauptung, die TOE gelöst zu haben. Keine Statusinflation.

Externe Statuswahrheit bleibt bei `docs/OPEN_PROBLEMS.md` (alle T1–T8 offen)
und `tfpt_research_contracts.tex`. Dieses Paket **promoviert nichts** in die
load-bearing Suite.
