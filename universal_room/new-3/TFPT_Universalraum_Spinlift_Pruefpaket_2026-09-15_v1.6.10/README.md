# TFPT Spin-Lift-Fortsetzung v1.6.10

Zuerst `RESULTS.md` lesen: ausdrücklich gewählte Viererquelle, genauer Hamiltonvertrag, Beweise und Grenzen. `UPDATE.md` enthält nur die neuen Ergebnisse, `EINFACH.md` erklärt dieselben Resultate anschaulich. Die aktualisierte vollständige Hauptfassung liegt unter `deliverables/`, PDFs unter `output/pdf/`.

## Reproduktion

Python mit NumPy, SciPy, SymPy und mpmath:

    python3 replay.py

Der Runner führt die eigene wissenschaftliche Prüfung normal und optimiert aus, verlangt byteidentische Resultate und wiederholt separat den eingefrorenen historischen Vierintervall-Clock-Zeugen. Quelltexte, Tensorpaket und Provenienz sind unter `sources/` und `frozen_sources.json` enthalten. Der Originalpfad bleibt Herkunftsmetadatum, nicht benötigter Installationspfad. Eine entpackte Kopie kann eigenständig geprüft werden.

Die beiden späten Vorschläge liegen separat als `sources/late_proposal_0.txt` und `sources/late_proposal_1.txt` vor. Ihre Hashes und die 61 zusätzlichen exakten Gegen-/Bestätigungsrechnungen stehen in `late_aspects_normal.json`. Der gemeinsame Replay wiederholt auch `verify_new_aspects.py` normal und optimiert. Die allgemeinen GNS-, modularen und Dimensionsargumente sind in Abschnitt 14 des Forschungsberichts ausgeschrieben.

Die anschließende Auswahlprüfung `verify_reflection_selection.py` wird ebenfalls im Replay ausgeführt. Sie prüft das unverdrehte asymmetrische Gegenmodell und den bedingten Reflexionsselektor aus Abschnitt 15. Die alten v177-/v180-Texte sind für den geometrischen Anschluss eingefroren; ihre vollständigen Behauptungen wurden nicht neu zertifiziert.

Die bereitgestellten Prüfbedingungen schließen Quellenpins, wiederholte Moden-/Vorzeichenprüfungen und rationale Konstanten ein. Der all-Fock-Grundzustandssatz ist ein analytischer Beweis mit endlicher CAR-Grundlage, keine Diagonalisierung des gesamten Fockraums und kein Proof-Assistant-Zertifikat. Die kleinere Kopplung wird nicht mit dem alten Prüfpunkt 1/20 gleichgesetzt.

Die unveränderte externe Arbeit „Gemeinsame Quelle“ und ihr gesamtes Prüfpaket sind separat eingefroren. Deren eigene Reproduktion: das betreffende Quellen-ZIP in einen neuen Ordner entpacken und dort `python3 work/composition/run_all.py` ausführen. Die erfolgreiche externe 614-Bedingungen-Reproduktion ist in `EXTERNAL_REPLAY.json` protokolliert. Der alte vollständige lokale Grundzustandslauf wurde nicht neu ausgeführt; die für diese Runde benötigte Casimir-Identität wurde hingegen neu aus der vollständigen Ein-/Zweifermion-Grundlage bewiesen.

## Dokumente und Grenzen

Das Hauptdokument übernimmt die gesamte v1.6.9-Hauptfassung ohne Textverlust als gekennzeichneten historischen Teil. Der neue Status und seine Kopplungsbereiche stehen davor. Die PDF-Generierung benutzt die vorhandene TFPT-Pandoc/XeLaTeX-Gestaltung; der beigefügte Erzeuger ist ein repo-lokaler Buildhelfer, kein ohne TeX-/Templateinstallation portables Veröffentlichungsprogramm. Die wissenschaftliche Reproduktion ist davon unabhängig.

Nicht geschlossen: Quellenauswahl aus TFPT, ursprünglicher Kopplungswert, physische Raumzeit-/Feldidentifikation, native Präparation/Record, sämtliche vollständigen T1-T8-Gates. Kein Commit, Push oder Webseiten-Update ist Bestandteil dieser Runde.
