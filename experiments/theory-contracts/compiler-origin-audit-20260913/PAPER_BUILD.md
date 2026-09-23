# Integriertes Paper: Build und Prüfgrenzen

Quelle: `docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_2026-09-13.md`.
Alle folgenden Befehle laufen im Repository-Wurzelverzeichnis.

1. Mit wissenschaftlicher Python-Umgebung (mpmath, sympy, matplotlib, Pillow):

   `/opt/homebrew/bin/python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/paper_checks.py`

2. Mit ReportLab, Pillow und pypdf, hier im verfügbaren gebündelten Runtime:

   `/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/build_paper.py`

3. Separater Replay der vier endlichen Forschungsaudits:

   `/opt/homebrew/bin/python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/run_checks.py`

4. PDF visuell prüfen:

   `pdftoppm -scale-to 1100 -png output/pdf/tfpt_compiler_universalraum_2026-09-13.pdf tmp/pdfs/tfpt_compiler_universalraum_20260913/page`

Erzeugnisse liegen unter `output/pdf/`: PDF, Zahlentabelle und SHA-256-Manifest.
Formelbilder und extrahierter Text liegen unter `tmp/pdfs/`.
Die beiden Python-Umgebungen werden hier verwendet, weil die wissenschaftlichen
Bibliotheken und die Dokumentbibliotheken in unterschiedlichen vorhandenen
Runtimes installiert sind; es werden keine globalen Pakete installiert.

Die neuen Paperprüfungen sind interne Anomalie-, Formel- und CKM-Kontrollen.
Sie schließen kein T1–T8-Tor. Die vier älteren Audits wurden für diese
Zusammenstellung erfolgreich erneut ausgeführt, normal/optimiert identisch,
11.214 eigene Checks je Modus, elf erkannte Mutanten. Keine fremde Quelle
wurde dafür verändert, kein vollständiger Lean- oder RH-Neubau ausgeführt.

Die empirischen Vergleiche verwenden explizite historische Referenzen:
CODATA 2022, NuFIT 6.0 mit Normalordnung/IC24/SK-atm und Planck 2018.
Insbesondere werden Delta und Gamma im CKM-Teil nicht gleichgesetzt;
die berechnete Differenz beträgt rund 0,037926 Grad.
