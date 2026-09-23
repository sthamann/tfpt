# Ergebnisse · D4-Torsor als Seam-Schlüssel

Lauf vom 17. September 2026. Normaler und `-OO`-Lauf sind
**byteidentisch**. Checker-Status `PASS`, **134/134 exakte Bedingungen**.
Inhaltliches präregistriertes Verdict: **`PARTIAL`**.

**Keine Statuswirkung:** `closed_gate_ids = []`, `promotion = false`.
MARKS.01, KERNEL.01 und alle T1–T8-Tore bleiben offen.

## 1 · Der einzelne markierte Punkt ist die falsche Zielstruktur

Die vollständige D4-Aktion auf

```
M = Z4 × {+1,-1}
```

hat exakt acht Elemente und wirkt frei transitiv. Es gibt keinen globalen
Fixpunkt und damit keine D4-äquivariante Auswahl eines einzelnen Punkts.
Der Rotationsquotient hat exakt zwei Bahnen; die Spiegelung vertauscht sie.

Das ist ein exakter No-go gegen weitere rein D4-symmetrische Versuche, aus
der rohen Seam unmittelbar einen Basispunkt samt Orientierung auszuwählen.
Eine Lösung von MARKS.01 muss daher entweder

1. die ganze äquivariante Familie tragen,
2. zusätzliche strukturbrechende Daten liefern oder
3. zeigen, dass ein Teil der Markierung reine Eichwahl ist.

Keine dieser drei physikalischen Lesarten folgt bereits aus dem No-go.

## 2 · Vier Basispunkte sind endlich spektral äquivalent

Für alle vier durch die antiperiodische Stationsuhr transportierten
Basispunkte stimmen die geprüften Invarianten exakt:

- Stationsspiegel-Spurpotenzen: jeweils `(0,4,0,4)`;
- Zweinachbar-Quellen-Gramspuren: jeweils `(2,4,8,16)`;
- mark-lokale W-Bank-Metrikspuren: jeweils `(480,3840,30720)`;
- Bankuhr-Spurpotenzen:
  `(0,0,0,-64,0,0,0,64,0,0,0,-256)`;
- `W W^T = 8 I_60`;
- Transfer-Spektrum: exakt `{1, 64/729, 1/729}`.

Damit überlebt die Lesart „Basispunkt als Eichrepräsentant“ diesen
endlichen Test. Bewiesen ist nur unitäre/spektrale Äquivalenz der
transportierten Operatoren, nicht eine physische Eichsymmetrie.

## 3 · D4 ist viel zu schwach, um die Vierbank zu selektieren

Der Raw-Seam-Raum wurde als der tatsächliche volle antiperiodische
256er-Ring typisiert:

```
rho_raw   = R_station ⊗ I_64
sigma_raw = J_station ⊗ F_64,  F_64(q)=63-q.
```

Auf der Vierbankseite:

```
rho_bank   = (R_station ⊗ G_F)^3
sigma_bank = J_station ⊗ S_F.
```

Beide Seiten realisieren exakt dieselbe Ordnung-16-Gruppe mit
`r^8=1`, `r^4=-I`, `s^2=1`, `srs=r^-1`. Für jeden der sechs vorhandenen
Spiegel-Lifts wurde die Charakterformel vollständig ausgewertet:

```
dim Hom_D4(V_raw,V_bank) = 8192
```

und zwar **für alle sechs Lifts identisch**:

```
[8192, 8192, 8192, 8192, 8192, 8192].
```

Der Hom-Raum ist also nicht null, aber um einen Faktor 8192 von der
benötigten Eindeutigkeit entfernt. D4-Kovarianz liefert keine kanonische
Raw-Seam→Vierbank-Abbildung und wählt auch keinen der sechs Lifts.
Gleiche Dimension `256=256` war erwartungsgemäß kein Intertwinerbeweis;
der markierte Seam-Unterraum hat außerdem nur `4·48=192` Moden.

**Erster ungelöster Pfeil:** `intertwiner_nicht_eindeutig`.

## 4 · Der geprüfte Orientierungs-/Pfaffian-Mechanismus ist negativ entschieden

Für `A=T^18` gilt exakt:

- `A^T=-A`;
- `A^2=-I`;
- `tr(A)=tr(-A)=0`;
- Eigenwerte `+i` und `-i` je 128-fach;
- Chiralitätsindex `128-128=0`;
- `det(A)=det(-A)=1`;
- `Pf(-A)=(-1)^128 Pf(A)=Pf(A)`.

Die zwei Pointings `T^18` und `T^6=-T^18` werden durch diese endlichen
Index-, Determinanten- und Pfaffian-Daten nicht unterschieden. Der in der
Präregistrierung formulierte endliche T4-Mechanismus ist damit
**widerlegt**. Ein chiraler Sektor müsste aus zusätzlicher Dynamik,
Randanomalie oder einem anderen wohldefinierten Operator kommen; er steckt
nicht in der bloßen C4-Pointing des 256-Moden-Raums.

## 5 · KERNEL.01 bleibt eine echte fehlende Eingabe

Zulässig reproduziert wurden nur die dimensionslosen Kernel-Invarianten

```
lambda = {1, 64/729, 1/729}
Delta = 6 log(3/2)
mass ratio = log(3)/log(3/2).
```

Der gepinnte Parent führt den Raw-Seam→W-Intertwiner weiterhin als
`false` und physisches `g/Delta` als fehlend. Der Checker meldet deshalb

```
g_delta_from_raw_kernel = NOT_AVAILABLE.
```

Weder der Modellprüfpunkt `1/20` noch `g_car=5` wurde als Kopplung
umetikettiert. Der No-Unit-Satz und QGEO.KERNEL.01 bleiben bindend.

## 6 · Was der Lauf über den gesuchten „Schlüssel“ entscheidet

Der D4-Torsor ist eine korrekte **Umtypisierung** von MARKS.01, aber nicht
der gesuchte universelle Selektor:

- **positiv:** Ein einzelner kanonischer Markierungspunkt ist ausgeschlossen;
  die vier Basispunkte sind in den geprüften endlichen Invarianten
  äquivalent.
- **negativ:** D4 allein lässt einen 8192-dimensionalen Intertwinerraum und
  erzeugt keinen chiralen Orientierungssektor.
- **offen:** Der rohe Kernel liefert weiterhin kein physisches `g/Delta`.

Der kleinste gerechtfertigte nächste Contract ist daher nicht eine weitere
D4-Pointing-Suche. Er muss den 8192-dimensionalen Hom-Raum mit **bereits
nativer zusätzlicher Algebra** schneiden: W-Kovarianz, die
`Spin(10)×SU(4)`-Casimirzerlegung, Clock, Link-Lokalität und
Quellenadjungierung. Der decisive Test lautet:

> Wird der gemeinsame Kommutanten-/Intertwinerraum durch diese unabhängig
> vorhandenen Strukturen exakt eindimensional und enthält er einen
> invertierbaren Vertreter?

Bleibt seine Dimension größer eins, ist auch die
„Compiler-Algebra selektiert den Parent“-Route in dieser Form gekillt.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-d4-torsor-seam-20260917
python3 -B d4_torsor_seam.py > run_normal.json
python3 -B -OO d4_torsor_seam.py > run_optimized.json
cmp run_normal.json run_optimized.json
```

Erwartet: `134/134 Bedingungen`, `status: PASS`, `verdict: PARTIAL`,
Hom-Dimension `8192` für alle sechs Lifts.
