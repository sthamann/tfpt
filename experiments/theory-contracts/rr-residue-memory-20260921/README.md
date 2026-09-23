# RR-Residuenbrücke und konstante Quellenlinie

Forschungs-ID `UR.RR.RESIDUE.01`. Gesamtverdict **PARTIAL**. Exakte endliche Resultate unter expliziten Voraussetzungen; keine vollständige TFPT-Lösung und keine Ledger-Promotion.

`HERLEITUNG.md` enthält Ergebnis, Beweise und physische Grenzen. Die beiden Prüfberichte ordnen die Residuenrechnung und die bereits bekannte Hodge-/Klebungsgrenze ein. Die vorherigen RR- und Zeitberichte sind als Voraussetzungen beigefügt.

Reproduktion: Python 3 mit NumPy und SymPy. Im Ordner `python3 -B replay.py` ausführen. Beide Prüfungen laufen normal und optimiert; die JSON-Zertifikate müssen bytegleich sein. Die Herkunftsdateien für den Hodge-Test liegen hashgebunden bei. Der Tensor wird im Residuentest nur auf Integrität geprüft, nicht als Beweis einer physikalischen Identifikation verwendet.

Die allgemeine Aussage über alle kompatiblen Logarithmen ist im Text bewiesen. Der Checker bestätigt die verwendeten endlichen Eigenraum- und Matrixidentitäten; er ersetzt keinen formalen Beweisprüfer.

Keine neuen physischen Freiheitsgrade, kein zusätzlicher Hamiltonoperator und keine Identifikation von Sigma_geom mit nativer Sigma2. Die entscheidende offene Aufgabe bleibt der lokale zustands- und zeiterhaltende Quellenanschluss an W.

Die physischen T1–T8-Gates bleiben offen. Dieser Contract schließt keines dieser Gates.
