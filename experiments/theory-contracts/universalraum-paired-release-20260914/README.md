# Vollständiges Hauptdokument + kurzes Update-Paper, v1.3
14. September 2026. Keine T1–T8-, RH- oder Faktorisierungspromotion.

## Ergebnis

Diese Ausgabe führt das vollständige 90-seitige Universalraum-Buch v1.1 fort.
Die kompakte 35-seitige Compiler-Version v1.2 ist **nicht** ihre Basis.
Die ursprünglichen 21 Hauptkapitel, vier Anhänge und alle Abbildungen bleiben
erhalten; drei neue Hauptkapitel und ein Provenienzanhang kommen hinzu.

- Sechs-Quellen-Audit an den betroffenen Stellen integriert.
- Gemeinsame Record-/Präparations-/Mehrzeit-Ausführung vollständig dokumentiert.
- Beide neuen eingefügten Texte mit ihren unterschiedlichen Modellverträgen
  geprüft und archiviert.
- Vollständige angegebene C16-F4-Singulettantwort unabhängig reproduziert.
- Erste Follow-ups: angepasste Phase für den angekleideten Mikrozustand;
  exakte Grenze eines Einzelpulses; kurzer bedingter resonanter Kontrolladapter.
- T1–T8, native Ressourcenherkunft, höhere Restterme und Nichtsingulettkonkurrenz
  bleiben offen.

## Struktur

- main-v1.3/main.tex: vollständiges Hauptdokument.
- main-v1.3/update.tex: nur Änderungen gegenüber Hauptbuch v1.1.
- main-v1.3/chapters/18_audit_v13.tex: Sechs-Quellen-Audit.
- main-v1.3/chapters/19_execution_v13.tex: gemeinsame endliche Ausführung.
- main-v1.3/chapters/21_new_inputs_v13.tex: neue Eingaben und begonnene Follow-ups.
- main-v1.3/chapters/20_release_v13.tex: Quellen und Evidenzgrenzen.
- source-v1.1/: unveränderte entpackte Basisquellen.
- new-input-audit/sources/: Originaltexte N7/N8 und Beweise N8B.
- new-input-audit/check.py: unabhängiger Prüfer; keine Original-Forschungsimporte.
- new-input-audit/run_checks.py: Normal/-OO-Vergleich und fünf in-memory-Mutanten.
- new-input-audit/singlet_f4.py: neuer 24.024-dimensionaler Singulettlauf.
- TFPT_Followups_2026-09-14_v1.3.md: verständliche priorisierte nächste Fragen.
- build_release.py: PDF-Bau, Abdeckungsprüfung, Rendern und Quellenmanifest.

## Wissenschaftlicher Prüfumfang

891 eigene Bedingungen, darunter alle 832 Matrixspalten der vollständigen
kleinen F4-Vergleichsmodelle und sechs C16-Spalten. Normal/-OO bytegleich,
fünf Negativmutanten werden erkannt. Das sind keine 891 unabhängigen Entdeckungen.
Die allgemeine F4-Pfadklassifikation gilt im erklärten harten Tensorproduktmodell.
Eine native CAR-/Clock-Identifikation wird nicht angenommen.

Separater C16-Lauf: zwölf Singulett-Eigenvektoren, Residuen unter 7e-14.
F4-Grundwert 555.4885003638373; vier projizierte Anregungswerte nahe
583.292038666386. Kein neuer Nichtsingulettvollvergleich, keine algebraische
obere Multiplizitätsschranke, kein kontrollierter höherer Restterm.

Der ältere gemeinsame Ausführungsprüfer wurde erneut ausgeführt:
231 eigene exakte Bedingungen plus 1073 getrennte Quell-Präfixbedingungen,
Normal/-OO bytegleich, fünf Mutanten erkannt. Die historische 210/128-
Basisprüfung und der 100er Sechs-Quellen-Audit wurden nicht pauschal als
in dieser Runde neu ausgeführte Gesamtprüfungen gezählt.

## Reproduktion

Vom Verzeichnis new-input-audit:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 run_checks.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 singlet_f4.py

Vom Releaseverzeichnis:
Bundled-Python build_release.py

Wissenschaft: Python mit NumPy, SymPy, SciPy.
PDF: LuaLaTeX sowie gebündeltes Python mit pypdf/Pillow und Poppler.
Der Build prüft alle alten Kapitel-/Abschnittsüberschriften und die Bytegleichheit
sämtlicher alter Figuren; danach werden alle Seiten gerendert und visuell geprüft.

## Übergabe

Beide PDFs, eine verständliche Follow-up-Datei und das Quellen-/Prüfpaket
werden versioniert nach /Users/stefanhamann/Documents exportiert.
Keine Altversion überschreiben. Maßgebliche Paarregel:
docs/TFPT_PAPER_RELEASE_POLICY.md.

Nicht ausgeführt: neue vollständige Lean/RH-Suite, Hardware, globale empirische
Neuauswertung, Vielzellen-/Raumzeit-/Gravitationsnachweis. Der RH-Aktualitätscheck
scheitert an einem fehlenden Quellenordner; der konfigurierte Faktorgraph fehlt.
Die vorhandene r647-Originalroute und ausgewählte Primärliteratur wurden gelesen.

