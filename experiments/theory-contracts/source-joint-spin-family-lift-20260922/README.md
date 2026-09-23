# Gemeinsamer Spinor- und Familienlift

Contract `UR.SOURCE.JOINT_SPIN_FAMILY_LIFT.01`, 22. September 2026. **PARTIAL**.

Der bereits in TFPT vorhandene Quotient `(Spin(10) × SU(4))/Z4` erlaubt einen globalen gemeinsamen `(16,4)`-Träger auch bei ungerader Determinantenklasse. Der isolierte Spin-Lift bleibt ausgeschlossen; im Paar kompensieren sich die Vorzeichen. Die natürliche Familie dieser Lifts ist explizit konstruiert und klassifiziert. Ihr kürzester Vertreter ist eine E8-Wurzel im `(10,6)`-Sektor.

[Beweis und Originalabgleich](PROOF.md) · [unabhängiger mathematischer Review](joint_lift_review.md) · [Audit der tatsächlichen Quellregeln](original_joint_lift_audit.md) · [exakte Kontrollen](results.json)

## Reichweite

Mehrere primitive gemeinsame Lifts erhalten dieselben lokalen Standardmodell-Ladungen und E8-Faserprodukte. Die ursprüngliche Restnullität könnte sie unterscheiden, ist aber noch nicht als konkreter Operator auf diesem gekoppelten Feldraum angegeben. Ihre Auswahl aus dem ursprünglichen Nahtkern, CAR-Felder, Zustand und physische Zeit sind daher nicht hergeleitet. Die Zahlen der CP1-Gegenprobe sind Bulk-Nullmoden und kein ursprüngliches Rand- oder Zeitspektrum.

Der nächste Herkunftsschritt ist die markierte Zuordnung des ursprünglichen Collaroperators zu `B_Sigma(W_m)`, einschließlich Ladungsgradierung und reduziertem Nullraum. Sie muss aus den Originaldaten folgen. Die schon vorhandene E8-Gitterkorrelation erneut einzusetzen würde diesen Schritt nicht liefern.

## Reproduktion

Im Contract-Ordner:

```sh
python3 checker.py
python3 -OO checker.py
```

Nur Python-Standardbibliothek. Die elf in `source_pins.json` bezeichneten lokalen Originaldateien müssen unverändert vorliegen. Die Ausgaben beider Läufe stimmen byteweise mit den gespeicherten Ergebnissen überein. Die Prüfung umfasst rationale Gewichte, alle 248 Verzweigungskomponenten, Ladungen, Normen und bedingte Kohomologie-/Holonomiekontrollen. Allgemeine Existenz und Klassifikation folgen aus dem schriftlichen Beweis, nicht aus endlicher Enumeration.

`validation.json` hält Originalrevision, Prüfer- und Ergebnishash sowie den genauen Reviewumfang fest. Die Hashpins sichern die geprüfte Textfassung; sie ersetzen keinen mathematischen Beweis.

Firewall: Forschungscontract unter `experiments/`; keine Änderung von Paper oder Statusledger, keine empirische Promotion, keine Schließung physischer T1–T8-Gates und keine vollständige TFPT-Lösung.
