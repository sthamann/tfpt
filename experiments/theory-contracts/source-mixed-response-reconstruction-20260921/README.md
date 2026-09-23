# Gemischte Quellenantwort und bedingte Rekonstruktion

Forschungs-ID: `UR.SOURCE.MIXED_RESPONSE.01` · Gesamtverdict: **PARTIAL**.

Die physischen T1–T8-Gates bleiben offen.

Der mathematische Rekonstruktionssatz gilt unter den in HERLEITUNG.md und algebra/REPORT.md genannten vollständigen Fock-, Ladungs- und Domänenannahmen. D_F=0 ist nach den unteren Operatoridentitäten hinreichend; der Quellenwert ist nicht berechnet. Es erfolgt keine Ledger- oder Paper-Promotion.

- HERLEITUNG.md: Ergebnis, Beweisidee, Zustandsanschluss und Herkunftsgrenze.
- algebra/REPORT.md: voller algebraischer Beweis und Gegenbeispiel ohne Irreduzibilität.
- invariant/REPORT.md: native symmetrieerhaltende Gegenprobe und exakte gefüllte Zustandsnorm.
- source/REPORT.md: Originalquellen und fehlender gemeinsamer Feld-/Zeitanschluss.
- certificate.json und validation_receipt.json: gezielte Rechnung; keine Vollsuite.
- source_pins.json: Hashes der herangezogenen Originalbelege.

Reproduktion: `python3 -B replay.py` oder `python3 -B -OO replay.py` mit NumPy. Beide Aufrufe erzeugen dieselbe JSON-Ausgabe. Der vorhandene Clocknachweis wird per Hash geprüft und als Voraussetzung übernommen, nicht vollständig neu ausgeführt. Die asymptotischen und allgemeinen Aussagen beruhen auf dem ausgeschriebenen Beweis; endliche Rechentests ersetzen ihn nicht.
