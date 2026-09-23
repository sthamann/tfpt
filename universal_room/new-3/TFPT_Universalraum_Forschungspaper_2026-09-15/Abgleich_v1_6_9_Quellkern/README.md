# TFPT / Universalraum: Quellphase und modulare Zeit

Stand: 15. September 2026, Ergänzung 1.4.

- `TFPT_Gesamtschau_Quellkern_2026-09-15.pdf`: geprüfter Bericht, 15 Seiten.
- Gleichnamige Markdown-Datei: bearbeitbare Fassung.
- `Einfach_erklaert.md`: kurze bildliche Zusammenfassung.
- `Pruefergebnisse_Gesamtschau.json`: 44 eigene Quell-/Kernelbedingungen, 31 eigene ergänzende Bedingungen und Audit des Worker-Replays; Quellen-Guards getrennt.
- `TFPT_Gesamtschau_Pruefpaket_2026-09-15.zip`: eingefrorene Eingaben, Worker-Originalpaket, eigene Prüfer und Resultate.
- `Auslieferung_Gesamtschau.json`: Dateihashes, Dokumentprüfung und Documents-Kopie.

## Beweisumfang

Die eigenen Konstruktionen sind endliche, ausdrücklich bedingte Modelle. Die beiden Regeln aus Paarfidelitäten erhalten nicht automatisch die ganze ursprüngliche Wortalgebra. Der neu geprüfte komplexe Dreierterm zeigt genau diese Grenze. Eine nichttriviale physikalische Zustandsregel, ein autonomer Controller und ein relativistischer Grenzwert wurden nicht hergeleitet.

Das v1.6.9-Originalpaket wurde vollständig erneut ausgeführt und die Ergebnisbytes abgeglichen: 514 exakte Bedingungen, vier numerische Kontrollen; separat 17 native Guards, 1073 Strahl-Guards und 13 kleine CAR-Prüfungen. Der historische v1.6.8-Gesamtlauf und große native Grundzustandsläufe wurden nicht wiederholt.

## Reproduktion der eigenen neuen Rechnungen

Im entpackten Prüfpaket liegen unter `own/` die beiden Prüfer. Sie benötigen Python, NumPy und SymPy. `kernel_inputs/` liegt direkt neben dem Kernelprüfer. Ausführung jeweils normal und mit `-OO -B`; die JSON-Ausgaben müssen innerhalb desselben Prüfers bytegleich sein. Der Kernelprüfer schreibt zusätzlich das vollständige Ganzzahl-Kernelzertifikat. Eine portable Reproduktion aus einer frisch ausgepackten Kopie wurde vor Auslieferung geprüft.

Das Worker-Originalarchiv unter `inputs/` enthält seinen eigenen Replay und Ressourcenvertrag. Es braucht für seinen Replay zusätzlich SciPy. Dokumente und Prüfer benennen ihre jeweiligen Annahmen; bestandene Einzelbedingungen sind kein Vollständigkeitsmaß einer Naturtheorie.
