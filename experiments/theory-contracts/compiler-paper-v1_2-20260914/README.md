# Gesamtpaper v1.2: versionierter Konsolidierungsexport

Export vom 14. September 2026, **vor** der anschließenden
compiler-single-execution-20260914-Rechnung.

- 35 Seiten; 39 gerenderte Displayformeln.
- Grundlage: Gesamtpaper vom 14. September v1.1 plus vollständiger
  Sechs-Quellen-Konsolidierungsnachtrag. Der alte Zweizellenabschnitt wurde
  durch den allkoppligen Satz ersetzt; ältere PDFs wurden nicht überschrieben.
- TFPT-Basics, Clocks, Standardmodell-Zuordnungen, Vorhersageformeln,
  negative Vergleiche, Evidenzgrenzen und der aktualisierte T1–T8-Vertrag
  sind enthalten.
- 16 Formel-/Wörterbuchprüfungen wurden neu ausgeführt. Der vorausgehende
  Sechs-Quellen-Audit mit 100 Prüfbedingungen wird dokumentiert, nicht durch
  diesen PDF-Export zu einem neuen physikalischen Beweis hochgestuft.
- Alle 35 Seiten wurden gerendert und in Kontaktübersichten geprüft;
  Formelsatz und T1–T8-Tabelle zusätzlich in Einzelansicht. Keine fehlenden
  Schriftglyphen im Layoutcheck.

Quelle: docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_2026-09-14_v1.2.md.
PDF und Provenienzmanifest: output/pdf/tfpt_compiler_universalraum_2026-09-14_v1.2*.
Versionierte bytegleiche PDF- und Markdown-Kopien liegen in Documents.
Das separate 90-seitige Universalraum-Buch bleibt unverändert.

Aufbau: paper_checks.py mit wissenschaftlichem Python ausführen,
build_paper.py mit dem Dokument-Python. Mit Poppler alle Seiten unter dem
expliziten, im Layoutprüfer genannten Verzeichnis rendern, dann
paper_layout_check.py ausführen und Kontaktübersichten visuell prüfen.

Der neue Satz korrigiert insbesondere die irrtümliche Tabelleninterpretation
von Zeilen mit Ket-Notation, die Darstellung der U-Regel und den TOC-Zeilenabstand.
Inhaltliche Evidenzklassen und offene physikalische Nachweise bleiben erhalten.
