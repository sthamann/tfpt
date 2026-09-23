# TFPT und der Universalraum: LaTeX- und Reproduktionspaket

Stand: 14. September 2026, Version 1.1. Zusammengestellt für Stefan Hamann.

Die erweiterte Fassung enthält die vollständige Synthese der elf bereitgestellten Unterlagen sowie fünf zusätzliche Hauptkapitel über RH und Primzahlen, Quantenchaos, Quantenphänomene, Dimension, offene Physik und eine gemeinsame Arbeitshypothese. Ein neuer endlicher Modellversuch verbindet arithmetische Multiplikationswege mit einer kohärent messbaren Pauli-Phase. Die Zuordnung der Operationen ist gesetzt; ihre Folgen sind exakt. Ein RH-Beweis oder eine vollständige physikalische Theorie wird nicht behauptet.

## Inhalt

- `main.tex`, `chapters/`, `sources_manifest.tex`: das vollständige Manuskript.
- `figures/`: Vektorplots und PNG-Ansichten; weitere Diagramme stehen als TikZ im Manuskript.
- `input_manifest.json`: Pfade und SHA-256-Werte der elf Originalunterlagen; Originaltexte werden nicht dupliziert.
- `rh_sources.json`, `rh_selected_records.json`: zusätzliche Quellenidentität und ausgewählte Katalogbefunde. Kein vollständiger oder global frisch bestätigter RH-Katalog.
- `verify_synthesis.py`, `verification_results.json`: Ausgangsprüfung mit 210 Bedingungen (209 exakt/symbolisch, eine hochpräzise numerische Kontrolle).
- `verify_shadows.py`, `shadow_verification_results.json`: Erweiterung mit 128 Bedingungen (126 exakt/symbolisch, zwei numerisch).
- `environment_versions.json`, `delivery_check.json`: Umgebung und Auslieferungskontrolle.

## PDF bauen

Benötigt werden LuaLaTeX, KOMA-Script, TikZ, tcolorbox, xurl, die in `main.tex` aufgeführten Standardpakete und die Schriften TeX Gyre Pagella, TeX Gyre Heros und Latin Modern Mono. Im entpackten Verzeichnis ausführen:

```sh
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

Wenn noch geänderte Querverweise gemeldet werden, einen weiteren Lauf ausführen. Ergebnis: `main.pdf`. Ein Neubau kann wegen Zeitstempeln oder PDF-Kennungen andere PDF-Bytes erzeugen; kontrolliert wurden Seitenzahl und extrahierter Text.

## Gegenrechnungen und Diagramme

Benötigt werden Python mit NumPy, SymPy, mpmath und Matplotlib:

```sh
python3 verify_synthesis.py
python3 verify_shadows.py
python3 -OO verify_shadows.py
```

Die Prüfer schreiben ihre Ergebnisdateien und die jeweils zugehörigen Abbildungen in `figures/`. Sie verwenden explizite Fehlerbedingungen statt abschaltbarer Assertions. Für beide Prüfer wurden normaler und optimierter Modus kontrolliert. Die Ergebnisse sind innerhalb des jeweiligen Prüfers bytegleich.

Die neue Eta-Abbildung wertet einen gegebenen Kanal an festen Zeiten aus. Der bekannte Referenzwert nahe 14,1347 wird eingesetzt; dies ist keine neue Nullstellenbestimmung. Die Wärmeausbreitungsbilder sind endliche Modellrechnungen mit vorgegebenen Gitterdimensionen. Das arithmetische Phasenbeispiel prüft ein Fenster bis 12 und ausgewählte normerhaltende Wege, keine globale endliche unitäre Realisierung der Multiplikationsisometrien.

## Abdeckung und Grenzen

Die ursprünglichen 16 Hauptkapitel bleiben erhalten und wurden mit der Erweiterung verknüpft. Es wurde kein vollständiger neuer Repository-, Lean-, RH- oder Hardwarelauf durchgeführt. Die zusätzlich gelesenen RH-Dateien sind ausgewählte Originalabschnitte und Ergebnisdateien. Die globale Aktualitätsprüfung des Forschungskatalogs scheiterte am fehlenden eingebundenen Ordner `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`. Die verfügbaren sieben Haupt-TeX-Dateien entsprachen ihren registrierten Hashes. Einzelne Katalogetiketten werden nicht als eigenständig neu bestätigte Theoreme ausgegeben.

Die 338 Bedingungen der zwei Prüfer zählen keine unabhängigen Entdeckungen oder physikalischen Bestätigungen. Die Fortsetzung unterscheidet mathematische Identitäten, Berichte, numerische Beispiele, zusätzliche Annahmen und offene Auswahl- und Grenzwertprobleme.
