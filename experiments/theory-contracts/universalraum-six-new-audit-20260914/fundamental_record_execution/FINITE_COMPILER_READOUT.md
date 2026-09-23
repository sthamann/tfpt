# Die endliche Compilergruppe genügt — ein kleiner bedingter Auslesesatz

14. September 2026. Ergänzt den Herkunftsvertrag in RESULTS.md, ohne ihn als
physikalisch aus den P1/P2-Axiomen hergeleitet auszugeben.

Die bisher verwendete volle kontinuierliche SU(4)-Kovarianz ist für den
effizienten, kantenlokalen Belegungsdetektor stärker als erforderlich. Bereits
die tatsächliche endliche projektive G31-/Zwei-Qubit-Clifford-Gruppe genügt.
Ihre projektive Gleichheit ist ein geerbter Satz aus der gepinnten v783-Quelle;
die neue Rechnung beweist die daraus benötigte Darstellungsaussage.

Auf Anti6 und Sym10 wurden die Tensorquadrate der fünf Generatoren H1,H2,S1,S2
und CNOT exakt gebildet. In beiden Räumen ist die einzige gemeinsame
eindimensionale Konjugationslinie die skalare Identität. Der Prüfer untersucht
sämtliche möglichen Generatorcharaktere, also auch ±i für die Phasengatter.
Nur die gewöhnliche Kommutante zu berechnen wäre unzureichend: Ein einzelner
Krausoperator eines kovarianten Kanals könnte zunächst einen nichttrivialen
Charakter tragen. Diese Möglichkeit wird hier ausdrücklich ausgeschlossen.

Die skalare Kommutante und die exakt erhaltene positive Metrik beweisen
komplexe Irreduzibilität beider Darstellungen. Charaktergetwistete Intertwiner
zwischen ihnen verschwinden wegen der verschiedenen Dimensionen 6 und 10.
Damit kann der leere Krausoperator auch nicht Sym10 nach Anti6 mischen.

Folgerung unter den weiterhin benannten Voraussetzungen:

- exakte Belegungs-POVM;
- Wiederholbarkeit der Belegung;
- ein Krausoperator je aufgezeichnetem Ausgang;
- Kovarianz unter der gesamten endlichen Compilergruppe;
- Kantenlokalität und keine Rückwirkung auf die beiden Zuschauerregister.

Auf den tatsächlich aus nackten Eingängen durch A erreichten Zweigen ist
das Instrument dann der benötigte Paritäts-Lüderskanal, bis auf irrelevante
Zweigphasen. Auf beliebigen leeren Sym10⊕Anti6-Überlagerungen verbleiben zwei
relative Phasen; globale eindeutige Lüderswirkung wird nicht behauptet.

Die physische Auslese, ihre Effizienz und ihre Kovarianz sind weiterhin
Prämissen. Die Aussage schließt eine unnötig starke Symmetrieannahme aus,
nicht die fundamentale Herkunft aller Operationsressourcen.

`finite_compiler_readout.py`: 41 exakte Prüfbedingungen in normalem und
optimiertem Python. Pauli-Symmetrie allein ist als Negativkontrolle nicht
ausreichend (Kommutantdimensionen 6 und 10). Der Beweisschluss einschließlich
der möglichen K0-Mischung wurde unabhängig gegengelesen.
