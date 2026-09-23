# Bestätigung des korrigierten LL2-Operators und des ersten Dressings

10. September 2026. **Der LL2-Implementierungsfehler ist im geprüften neuen Code behoben. Die korrigierten Dressingwerte sind unabhängig exakt bestätigt; die Reduktion liegt für alle vier Vektoren über Faktor 418.**

Gelesene, unverändert gesicherte Stände:

- `checks.py`: SHA-256 `cd139dddf52d8345b1fa32a6cdb5a2a3308ea734b4412f8f7aeb4061ec78654a`, 22.033 Bytes.
- `checks.json`: SHA-256 `2a3f99e1e7e186943ecf3a87306c6b1ecff637b24977232cbb711bb775185801`, 6.533 Bytes.
- `cap_dynamics.py`: SHA-256 `235e7a1fb6add2057a74e43e4fff42c1667aa8c1c7224cb93a225ad8395b5221`, 16.753 Bytes.

## Operator und Gegenzeuge

`apply_H` verwendet jetzt `two_link_hop`: eine Annihilation am Anfangsort, eine Erzeugung am Endort und beide Linkverschiebungen. Das Zwischenorbital wird nicht fermionisch verändert. `cap_dynamics.Graph` implementiert denselben korrigierten Endpunktoperator.

Der ursprüngliche Gauß-kompatible Zeuge `(Maske75, Flux(0,0,0,0))` erhält nach `(Maske78, Flux(1,1,0,0))` nun exakt die Amplitude **−1/576**. Der alte sequenzielle Mutant bleibt bei Amplitude null und ist damit weiterhin ein diskriminierender Gegencheck.

Die aktuellen beiden Implementierungen wurden auf sämtlichen **37 relevanten Basiszuständen** verglichen: den vier nackten Codezuständen, ihrem vollständigen ersten H-Bild und dem ursprünglichen zusätzlichen Gegenzeugen. Auf jedem stimmt das vollständige sparse H-Bild exakt mit dem unabhängig geschriebenen Endpunktoperator des vorigen Reviews überein.

## Erste Dressingstufe

Die komplette erste Dressing- und Residualrechnung wurde aus den gesicherten rationalen Definitionen neu ausgeführt. Ihr Ergebnis stimmt vollständig mit dem gespeicherten korrigierten `checks.json` überein. Alle vier rationalen Residualwerte stimmen außerdem exakt mit der zuvor unabhängig vorhergesagten Korrektur überein. Die separate Graph-Implementierung reproduziert dieselben vier Brüche.

| Codevektor | Restleckage, gerundete Darstellung | Reduktionsfaktor, gerundete Darstellung |
|---:|---:|---:|
| 0 | 3.322121917481888·10⁻⁵ | 418.07282314962214 |
| 1 | 3.322172930614849·10⁻⁵ | 418.06640349448674 |
| 2 | 3.322326147948549·10⁻⁵ | 418.04712332246254 |
| 3 | 3.322581587822098·10⁻⁵ | 418.0149838846499 |

Das nackte Leck bleibt exakt **1/72**. Die Faktoren sind nicht exakt gleich; „etwa Faktor 418“ ist eine zulässige Zusammenfassung. Die Ungleichung **Reduktionsfaktor >418** wurde für alle vier Vektoren anhand ihrer rationalen Werte geprüft. Exakte Brüche und die korrigierte Residualzerlegung stehen in `corrected-code-confirmation.json`.

## Exaktheitslabels

`evidence_classes` unterscheidet jetzt zutreffend rationale Rechnungen, NumPy-Stichproben und mpmath-Numerik. Auch `cap_dynamics.py` benennt seine numerischen Ausgaben gesondert.

**Verbleibende redaktionelle Korrektur:** Der Eingangstext von `checks.py` behauptet weiterhin „All statements are finite/exact model checks“; der globale Ergebnisstatus heißt weiterhin `FABLE_KERNFRAGEN_EXACT_CHECKS`. Diese beiden pauschalen Bezeichnungen widersprechen der nun richtigen Detailklassifikation. Die rational berechneten Dressingwerte sind dadurch nicht betroffen.

## Reproduktion und Reichweite

`python3 check_corrected_code.py` besteht mit **85 exakten Kontrollen**. Verwendet werden nur ausgewählte Definitionen der gebundenen Snapshots und der unabhängige Operator aus dem vorigen Review. Das vollständige Fable-`record()`, NumPy/mpmath-Prüfungen und höhere iterative Dressingstufen wurden nicht ausgeführt.

Dies bestätigt den korrigierten Operator und die erste Dressingstufe auf dem deklarierten Viererring. Es ist keine allgemeine TFPT-Dynamikbestätigung und keine endgültige Abnahme der noch überarbeiteten `PROOF.md`-/`ERGEBNISSE.md`-Aussagen. Fables Originaldateien wurden nicht verändert.
