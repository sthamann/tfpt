# RR-Trägerclock im nativen W-Prozess

Forschungs-ID `UR.RR.CLOCK.01`, Gesamtverdict **PARTIAL**. Endliche Algebra bestanden; keine vollständige physische TFPT-Lösung und keine Ledger-Promotion.

`HERLEITUNG.md` enthält den Beweis, Zustand und Antwortgrenzen. `ALGEBRA.md` beschreibt den neuen exakten Checker. `QUELLENPRUEFUNG.md` ordnet die Originalverträge ein. `RR_VORAUSSETZUNGEN.md` enthält den vorausgehenden geometrischen Anschluss.

Reproduktion: Python 3 und NumPy; im Ordner `python3 -B replay.py` ausführen. Die Tensorquelle ist beigefügt und hashgebunden. Normale und optimierte Ausführung werden byteweise verglichen. Es werden keine fremden Quellen oder Ledgerdateien verändert.

Der bestehende Grundzustandssatz und die Momentidentitäten sind ausdrücklich importierte, gepinnte Beweise. Die allgemeine Zustands-/Antwortraumargumentation steht im Text; die endliche Matrixprüfung wird nicht als formaler Beweis der vollständigen Theorie ausgegeben.
