# RR-Dreifamiliensektor und Zustand

**Forschungs-ID:** `UR.RR.THREE_FAMILY_STATE.01`  
**Theorie-Verdict:** `PARTIAL`  
**Endliches Tensorzertifikat:** `PASS`

Der gepinnte native Tensor besitzt nach dem expliziten Hadamard-Basiswechsel einen exakten Dreifamiliensektor mit 48 fermionischen und 30 bosonischen Einteilchenmoden. Die Einschränkung verwendet denselben Tensor `W` und dieselben Parameter `g,Δ`. Der bereits vorhandene schwach gekoppelte Grundzustand liegt dagegen exakt im Sektor `Z=16` und ist orthogonal zu `ker Z`.

Der allgemeine Fock-, Zustands- und Antwortbeweis steht in `HERLEITUNG.md`; er wurde unabhängig mathematisch geprüft, aber nicht in einem formalen Beweisassistenten verifiziert. Der verwendete native Grundzustandssatz wird aus dem bestehenden Contract importiert und hier nicht neu bewiesen.

## Reproduktion

```bash
python3 checker.py > certificate.json
python3 -OO checker.py > certificate_optimized.json
cmp certificate.json certificate_optimized.json
```

Der Rechner verwendet ausschließlich `native_tensor.npz` im selben Ordner und exakte Ganzzahl- beziehungsweise skalierte rationale Arithmetik. Er baut keine Fockraummatrix auf.

## Evidenzformeln

Für den importierten `SU(4)`-invarianten Zustand mit `\bar b=<N_b>` gelten

\[
\nu=1-\frac{\bar b}{32},\qquad
n_b=\frac{\bar b}{60},\qquad
S=15-\frac{7\bar b}{32}.
\]

Der ausgelassene gemischte Anteil hat die exakte quadrierte Norm `S|g|²/3`; eine skalare Neuanpassung `g'` oder ein linearer Einteilchenterm entfernt ihn nicht in der geprüften zeitlokalen nativen Form.

## Dateien

- `HERLEITUNG.md` und `expository.md`: eingefrorener Hauptbeweis.
- `INDEPENDENT_REVIEW.md`: unabhängige mathematische Prüfung.
- `original_source_audit.md`: begrenzter Audit der ursprünglichen Nahtquelle.
- `checker.py`, `certificate.json`, `native_tensor.npz`: portables endliches Replay.
- `contract_index.json`, `source_pins.json`, `manifest.json`: Graph- und Herkunftsmetadaten.

Nicht hergeleitet sind die physische Auswahl von `U`, `g/Δ`, Zustand und Zeit, ein lokaler 3+1D-Anschluss, Standardmodell-Yukawas oder ein Abschluss von T1–T8.
