# D4-Torsor statt ausgezeichneter Seam-Markierung — Präregistrierung

17. September 2026. Endlicher, nichtarithmetischer NON-RH-Theory-Contract.
**Firewall:** keine Änderung und keine Statuswirkung in `verification/`,
`status_ledger.csv`, Papers, Website oder Scorecard. Kein T1–T8-Tor kann
durch diesen Contract geschlossen werden.

## Ausgeführtes Ergebnis

Die nachstehende Präregistrierung wurde unverändert ausgewertet. Normaler
und `-OO`-Lauf sind byteidentisch; **134/134** Bedingungen bestanden.
Inhaltliches Verdict: **`PARTIAL`**. Die Basispunkt-Invarianten stimmen,
aber `dim Hom_D4(V_raw,V_bank)=8192` für jeden der sechs Lifts; der
Intertwiner ist nicht eindeutig. Der geprüfte Orientierungsmechanismus hat
Index 0 und keinen Pfaffian-/Determinantenunterschied. Physisches `g/Delta`
bleibt `NOT_AVAILABLE`. Vollständige Einordnung: [RESULTS.md](RESULTS.md).

## Ausgangspunkt

`universalraum-mu4-pointing-20260917` hat in 41 exakten Bedingungen gezeigt:
Die Seam trägt eine eindeutige normale C4 mit kanonischem `-I`, aber keine
ausgezeichnete Orientierung und keinen ausgezeichneten Basispunkt. Der
Markierungsraum

```
M = Z4 × {+1,-1}
```

ist ein frei-transitiver D4-Torsor. Eine D4-äquivariante Auswahl eines
einzelnen Punkts kann daher nicht existieren.

Dieser Contract prüft vor dem ersten Lauf die schwächere Hypothese:

> Die vier Basispunkte sind Eichrepräsentanten einer D4-äquivarianten
> Seam-Familie. Die zwei Orientierungen könnten getrennte
> paritätskonjugierte Sektoren sein. Der rohe Seam muss dann die Familie
> tragen, nicht einen Punkt auswählen.

## Eingefrorene Quellen

Alle Dateipins werden vor jeder fachlichen Rechnung mit SHA-256 geprüft:

| Quelle | SHA-256 |
|---|---|
| `universalraum-mu4-pointing-20260917/mu4_pointing.py` | `6c15a99722234db4c41a7b859967ea7a7b39d94983121ee0d19af3aec744a032` |
| `universalraum-seam-reflection-lift-20260915/seam_reflection_lift.py` | `300f8670f16727b747244b63b76acf57a030d5f7f51774aef6401cb46338d808` |
| `universalraum-v1.6.9/agents/source/inputs/native_common.py` | `2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994` |
| `universalraum-common-parent-t1-t8-20260915/parent_spec.json` | `f0ac19749175a3f3cb24d419b31b66f060b44d7b0523f8dd8ea75f501d5b33c4` |
| `verification/v56_unique_attractor.py` | `d0870475b4b56dc386935a8845a7494120da713a2f6a60488460faafe63f39fc` |
| `verification/v162_seam_transport_identification.py` | `1d3a80006bcff439f88b83d7f3b64d03a7b8d9cea15308ca7c68fde86beb5225` |
| `universalraum-v16-integrated-20260915/sources/native_tensor.npz` | `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763` |
| `compiler-involution-types/checker.py` | `9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1` |

Keine Beobachtungsdaten gehen ein. Der v1.6.9-Prüfpunkt `g/Delta = 1/20`
ist ausdrücklich kein zulässiger Kernel-Output und wird nicht importiert.

## Eingefrorene Darstellungen

1. **Markierungsraum:** `M = {(b,e) | b in Z4, e in Z2}` mit
   `t(b,e)=(b+1,e)` und `s(b,e)=(-b,1-e)`.
2. **Roher voller Seam-Ring:** `V_raw = R^256`, geordnet als vier
   aufeinanderfolgende 64er-Blöcke. `rho_raw = R_station ⊗ I64` ist die
   antiperiodische Vierteldrehung mit `rho_raw^4=-I`. Der Spiegel mit
   Zentrum 63 ist die tatsächliche Ringabbildung
   `site -> 63-site (mod 256)` samt antiperiodischem Wrap-Vorzeichen; in
   Blockkoordinaten ist das `sigma_raw = J_station ⊗ F64` mit der
   internen Umkehrung `F64(q)=63-q`, nicht `J_station ⊗ I64`.
3. **Markierter Seam-Unterraum:** vier Intervalle zu je 48 Moden, also
   Dimension 192. Er wird nur zur Typkontrolle verwendet; er wird nicht
   stillschweigend mit der 256-dimensionalen Vierbank identifiziert.
4. **Vierbank-Fermionraum:** `V_bank = R^4 ⊗ R^64` mit der bestehenden
   gemeinsamen Uhr `T=R_station⊗G_F` und Spiegeln `J⊗S_F`.
   Für den Vergleich derselben binären C4-Deckgruppe wird der natürliche
   Ordnung-8-Untergenerator `rho_bank=T^3` verwendet; er erfüllt
   `rho_bank^4=-I`.
5. **Native Paarbank:** der gepinnte Tensor `W` hat Shape `(60,2016)` und
   `W W^T=8 I60`. Seine vorhandene innere Uhr-/Spiegelkovarianz wird
   separat geprüft und nicht mit dem noch offenen Raw-Seam-Intertwiner
   gleichgesetzt.

## Präregistrierte Prüfungen

### A — No-go und Quotient

- Vollständige Enumeration der D4-Aktion auf M.
- `|D4|=8`, freier transitiver Orbit, daher kein globaler Fixpunkt und
  keine D4-äquivariante Abbildung vom Einpunkt-Raum nach M.
- Der Rotationsquotient hat exakt zwei Klassen, entsprechend den zwei
  Orientierungen; Spiegelung vertauscht sie.

### B — Basispunkt als mögliche Eichwahl

Für alle vier Basispunkte werden die Stations-, Vierbank- und
Transfer-Operatoren durch die eingefrorene Rotationswirkung transportiert.
Verglichen werden exakt:

- charakteristische Polynome bzw. ganzzahlige Spurpotenzen,
- Gram-/Casimir-Spektralinvarianten,
- die Multimenge der Transfer-Eigenwerte
  `{1,(2/3)^6,(1/3)^6}`.

Eine Basispunktabhängigkeit einer dieser Größen widerlegt die Eichlesart.
Gleichheit zeigt nur endliche unitäre Äquivalenz, keine physische Eichsymmetrie.

### C — Raw-Seam-zu-Vierbank-Intertwiner

Für die eingefrorenen Ordnung-8-Generatoren und einen festen der sechs
vorhandenen Spiegel-Lifts wird

```
X rho_raw = rho_bank X
X sigma_raw = sigma_bank X
```

als exaktes lineares Intertwinerproblem behandelt. Die Hom-Dimension wird
über endliche Gruppencharaktere berechnet und durch die Generatorrelationen
kontrolliert. Derselbe Test wird für alle sechs Spiegel-Lifts wiederholt.

Der starke Treffer wäre: für jeden zulässigen Lift derselbe
eindimensionale Raum, erzeugt von einer invertierbaren Abbildung, sodass
die feste innere W-Kovarianz kanonisch angefügt werden kann.

- Hom-Dimension `0`: die vorgeschlagene Brücke existiert in dieser
  Typisierung nicht.
- Hom-Dimension `>1`: D4-Kovarianz wählt die Brücke nicht eindeutig.
- Verschiedene Dimensionen für die sechs Lifts: die bereits bekannte
  Lift-Nicht-Eindeutigkeit bleibt load-bearing.

Die bloße Gleichheit `dim V_raw = dim V_bank = 256` zählt nicht als
Intertwiner. Der markierte 192-Moden-Unterraum ist eine explizite
Negativkontrolle gegen diese Verwechslung.

### D — Orientierung, Index und Determinantenlinie

Für `Gamma_+=-i T^18` und `Gamma_-=-Gamma_+` werden die
Eigenwertmultiplizitäten aus exakten Spur-/Quadratidentitäten bestimmt.
Zusätzlich werden Determinante und die Pfaffian-Skalierungsparität der
reellen schiefsymmetrischen Matrizen `T^18` und `-T^18` exakt geprüft.

Ein `ORIENTATION_SECTOR` verlangt einen nichttrivialen invarianten
Unterschied der beiden Orientierungen. Balancierte Multiplizitäten,
gleiche Determinante und gerade Pfaffian-Skalierungsparität widerlegen
diesen endlichen T4-Mechanismus.

### E — Kernel und g/Delta

Zulässig sind nur die bereits verifizierten dimensionslosen
Kernel-Invarianten

```
lambda = {1,(2/3)^6,(1/3)^6}
Delta = 6 log(3/2)
mass ratio = log(3)/log(3/2).
```

Es existiert in den eingefrorenen Quellen kein roher
Calderón/Seam-Konstruktor, der zugleich physisches `g` und `Delta`
ausgibt. Der Checker muss deshalb `g_delta_from_raw_kernel =
NOT_AVAILABLE` melden und nachweisen, dass weder `1/20` noch `g_car=5`
als Ersatz importiert wurde. `NOT_AVAILABLE` ist kein Fehlschlag der
Rechenintegrität, verhindert aber `TORSOR_REDUCTION`.

## Verdict-Enum

- **`ORIENTATION_SECTOR`** — Basispunkt-Invarianten stimmen, der
  Raw-Seam-Intertwiner ist eindeutig und invertierbar, und ein
  nichttrivialer Orientierungsinvariant existiert. Wegen des offenen
  rohen Kernels weiterhin kein Gate-Abschluss.
- **`TORSOR_REDUCTION`** — Basispunkt-Invarianten stimmen und der
  Intertwiner ist eindeutig; Orientierung bleibt offen. Dieses Verdict
  ist nur zulässig, wenn `g/Delta` aus einem rohen Kernel verfügbar ist.
- **`PARTIAL`** — No-go/Quotient oder einzelne Invarianzen bestehen, aber
  Intertwiner, Orientierung oder Kernelvertrag schließen nicht.
- **`REFUTED`** — Basispunkte liefern verschiedene Invarianten, der Hom-Raum
  ist null, oder die Rechnung benötigt Zielwissen bzw. einen verbotenen
  Modell-Kernel.
- **`KERNEL_VIOLATION`** — ein Pin, eine feste Dimension/Relation oder die
  Firewall wird verletzt.

Das Skriptfeld `status: PASS` bezeichnet ausschließlich bestandene
Checker-Integrität. Das inhaltliche Verdict wird davon getrennt ausgegeben.

## Stopbedingungen und Reproduktion

Der Suchraum wird nach dem ersten Lauf nicht erweitert. Insbesondere werden
keine anderen Potenzen von T, keine ausgewählten Teilräume und keine
zusätzlichen Kernelparameter ausprobiert, um die Hom-Dimension oder
`g/Delta` passend zu machen. Nach zwei fehlgeschlagenen
Implementationshypothesen wird gestoppt.

Ausführung:

```sh
cd experiments/theory-contracts/universalraum-d4-torsor-seam-20260917
python3 -B d4_torsor_seam.py > run_normal.json
python3 -B -OO d4_torsor_seam.py > run_optimized.json
cmp run_normal.json run_optimized.json
```

Erst nach dem Lauf werden exakte Zähler und das Verdict berichtet; danach
darf `RESULTS.md` entstehen.
