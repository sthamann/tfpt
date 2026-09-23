# F4: Fehler und wachsende, gekoppelte Zellen

14. September 2026. NON-RH. Nur `experiments/theory-contracts`.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

## Firewall

Der unabhängige Zelltest erledigt keine wechselwirkenden Zellen. Exakte
Zeitwahl ist eine starke Ressource. `λ = J` ist der datenfreie
Clebsch-/Superaustausch-Default; `λ ≠ J` braucht Zusatzdaten.

## Unabhängig: bewiesen

CPTP-Attraktor mit einzigem Fixpunkt `Ω`, Rate `r = 0.97542071045`,
Fehlerboden `40.6847 ε`. 556 Zyklen für eine Zelle auf `10⁻⁶`; 890 Zyklen
für 4096 Zellen per Vereinigungsbound, auch bei verschränktem Start.
Ungelesener unitaler Record kühlt nicht (Fixalgebra-Dimension 3876).

Reset: bis zu 8 Farbbits/Zelle, 3 Austauschrecords/Zyklus, 26 kontrollierte
`H`-Aufrufe für Start+Ende. Im Mittel 6,176 Präparationsversuche.

## Gekoppelt: Schranke, Default nicht brauchbar

Exakter Zweizellenblock: Gap `> J/2` für alle getesteten `λ/J` einschließlich
`λ/J → ∞`. Produktzustand-Brücke hat Erwartungswert `5/8` und Varianz `15/64`.

Lieb-Robinson-/Cluster-Störung auf den deklarierten Record-/Filterzeiten
bei Default `λ = J`, `t/Δ = 1/20`:

| Fenster | brauchbar bei `10⁻⁶`? |
|---|---|
| 2 Zellen, 3 Records | nein |
| 2 Zellen, Spektralfilter | nein |
| Kette N=4096, 3 Records | nein |
| Kette N=4096, Spektralfilter | nein |

Grobe Eindeutigkeit stirbt bei N=5, `λ=J`. Default-`J` liegt über der
Spektralfilter-Uhrschranke für Infidelität `10⁻⁶`.

**Status:** `F4_INDEPENDENT_USABLE_COUPLED_DEFAULT_NOT_USABLE`.

Härteste Restressource: Zwischenellentkopplung oder extra Datum `λ ≪ J`
auf den deklarierten Zeiten. 8 Farbbits und `log N` Zyklen sind billig
dagegen. Kein T8-Abschluss.

## Reproduktion

```sh
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
```

Auch mit `-OO`. Quellpins in `checker.py`.
