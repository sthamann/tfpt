# Fortsetzung: Die Quelle liefert Messkontexte — ein eindeutiger bedingter Prozess

13. September 2026. NON-RH. Kein physischer Instrumenten- oder TOE-Beweis.

## 1. Der konkret wieder aufgenommene Befund

Die letzte Runde ließ die Bedeutung der 15 Labels offen. Die präzisere
Antwort steht bereits in **v783**, P0/P1 und P6: Im festgelegten komplexen
Chart entsprechen die 60 Gaussian-E8-Linien den 60 reinen Zwei-Qubit-
Stabilizerstrahlen. Jede der 15 nichttrivialen Quotientenklassen enthält
vier orthogonale Strahlen, also eine vollständige Messbasis.

Die Labels entsprechen hier **15 maximalen Pauli-Messkontexten**, nicht
15 einzelnen Spinorzuständen und auch nicht unter derselben Gruppenwirkung
einfach den 15 einzelnen Pauli-Operatoren. Die Quelle benennt ausdrücklich
eine Punkt-Linien-Dualität; eine gemeinsame Zahl 15 hebt diesen Unterschied
nicht auf. Dieser bekannte Quellenbefund wird nicht als Neuentdeckung verkauft.

Der neue Prüfer `context_instrument.py` berechnet die Originalabschnitte
P0/P1 erneut und konstruiert alle Projektoren aus den **tatsächlichen
240 Wurzeln beziehungsweise ihren 60 Linien**. Die Zuordnung Klasse→Kontext
und sämtliche 225 Einträge der Inzidenzmatrix werden neu überprüft.
Die große Gruppenrechnung P2–P7 wird nicht vollständig wiederholt.

## 2. Die erste Frage hat eine kleine bedingte Lösung

Bezeichne die vier Rang-eins-Projektoren eines Kontextes C mit Pi_(C,s).
Nehmen wir explizit an:

1. Zustände und Messungen erfüllen die übliche endlichdimensionale
   Quantenmechanik einschließlich vollständiger Positivität und Born-Regel.
2. Ein Kontext wird vollständig und scharf gemessen, mit genau diesen vier
   Projektoren als Effekten.
3. Die Messung ist wiederholbar: Unmittelbare Wiederholung im selben
   Kontext liefert sicher dasselbe Ergebnis.

Dann ist die selektive Zustandsänderung **eindeutig**:

\[
\mathcal I_{C,s}(\rho)=\Pi_{C,s}\rho\Pi_{C,s}
=\operatorname{Tr}(\Pi_{C,s}\rho)\Pi_{C,s}.
\]

Beweis, nicht nur Stichprobentest: Für Krausoperatoren A_k eines Ergebnisses
erzwingt sum A_k†A_k=Pi, dass A_k=A_k Pi. Wiederholbarkeit erzwingt
A_k=Pi A_k. Da Pi Rang eins hat, bleibt A_k=c_k Pi und sum|c_k|²=1.
Damit ist die obige Abbildung die einzige Möglichkeit. Zusätzliche
Apparaturfreiheitsgrade sind dadurch nicht eindeutig bestimmt.

Die zugrunde liegende ideale Messregel und ihre Beziehung zur Kommutativität
sind etablierte Quantenmechanik, siehe
[Busch–Singh, Lüders-Theorem](https://arxiv.org/abs/1304.0054).
Der Beweis leitet die Messpostulate nicht aus TFPT her.

**Negative Kontrolle:** Der Prozess
I_s(rho)=Tr(Pi_s rho) I4/4 besitzt dieselben Born-Effekte, aber eine
Wiederholung liefert das vorherige Ergebnis nur mit Wahrscheinlichkeit 1/4
statt 1. Effekte allein genügen nicht; Wiederholbarkeit ist eine wirkliche
zusätzliche Voraussetzung. Die frühere C15-Mehrdeutigkeit wird damit nicht
rückwirkend widerlegt: Hier ist der Träger und der Instrumentenvertrag enger.

## 3. Der vorhandene Inzidenzkern wird zur Kontextwahl

### Noch direkter: Die Messabbildung steckt in vier ursprünglichen Spiegelungen

Die Quelle enthält nicht nur die vier Strahlen einer Klasse, sondern die
zugehörigen unitären Wurzelspiegelungen R_j=I-2 Pi_j. Für jede ursprüngliche
Klasse gilt exakt

\[
\boxed{\frac14\sum_{j=1}^4 R_j\rho R_j^\dagger
=\sum_{j=1}^4\Pi_j\rho\Pi_j.}
\]

Die rechte Seite ist die Kontextmessung **ohne aufbewahrtes Ergebnis**.
Die linke Seite braucht nur die gleichmäßige Mischung der vier schon
vorhandenen Spiegelungen. Der Prüfer verifiziert die Identität für alle
15 Klassen auf einer vollständigen Operatorbasis, nicht nur für Zustände
oder Spektren. Die ursprüngliche Wurzelreflexion entspricht der in v783
verwendeten Form I-zz†/2 bei z†z=4.

Warum funktioniert diese besonders kurze Formel? Für eine vollständige
Rang-eins-Basis in Dimension d gilt allgemein

\[
\frac1d\sum_j R_j\rho R_j^†
=(1-4/d)\rho+(4/d)\sum_j\Pi_j\rho\Pi_j.
\]

Nur bei d=4 verschwindet der erste Term. Das erklärt die hier beobachtete
Identität; es beweist nicht, dass die Natur Dimension vier deshalb wählt.

Auch die selektiven Zweige lassen sich in einer **bedingten kohärenten
Implementierung** verbinden. Starte mit der Isometrie

\[
V\psi=\frac12\sum_{j=1}^4|j\rangle\otimes R_j\psi.
\]

Ein Auslesen dieses Hilfsregisters liefert vier gleich wahrscheinliche
Reflexionsetiketten, unabhängig von psi. Es ist noch keine Born-Messung
der ursprünglichen Kontextstrahlen. Drehe das Register jedoch vorher mit

\[
W=\tfrac12 J_4-I_4,\quad W^†W=W^2=I,
\]

dann gilt

\[
(W\otimes I)V\psi=\sum_j|j\rangle\otimes\Pi_j\psi.
\]

Jetzt sind die Ergebniswahrscheinlichkeiten die Born-Werte und die Zweige
genau die oben eindeutig bestimmten wiederholbaren Instrumente.
**Auch W ist keine neue frei angepasste Matrix:** Der Strahl
|+_4><+_4|=J4/4 gehört zur originalen 60er-Liste und W ist das Negative
seiner ursprünglichen Wurzelspiegelung.

Damit liegen alle einzelnen Matrizen dieser endlichen Realisierung schon
im Quellbaukasten. Nicht bewiesen sind ein physisch verfügbares kohärentes
Hilfsregister, kontrollierte Anwendung der Spiegelungen, seine Präparation,
die Wahl seiner Auslesebasis oder die Ausführung als Naturdynamik. Die
Gleichheit nichtselektiver Kanäle macht die beiden Ergebnisprotokolle nicht
gleich: Reflexionsetiketten bleiben etwas anderes als Messresultate.

### Kontextwechsel mit dem vorhandenen K

Für zwei Kontexte C,D ist B_DC=1 genau dann, wenn sie mindestens einen
nichttrivialen Pauli-Operator gemeinsam haben; das schließt C=D ein.
Jeder Kontext hat sieben solche Nachfolger.

**Weitere offen deklarierte Annahme:** Diese sieben Kontexte werden als
tatsächlich ausgeführte nächste Messungen gleichmäßig gewählt, entsprechend
dem vorhandenen K=B/7. K beschreibt dann die Wahl der nächsten Messfrage,
nicht schon deren Quantenergebnis.

Nach einem Ergebnis (C,s) bestimmt die wiederholbare Messregel den nächsten
Zustand auf den 60 ursprünglichen Strahlen vollständig:

\[
T_{(D,t),(C,s)}=
\frac{B_{DC}}7\operatorname{Tr}(\Pi_{D,t}\Pi_{C,s}).
\]

Die genaue Rechnung ergibt pro Eingang:

- derselbe Strahl mit Wahrscheinlichkeit 1/7;
- zwölf andere Strahlen mit Wahrscheinlichkeit jeweils 1/14;
- die übrigen 47 mit Wahrscheinlichkeit null.

Das sind nur 13 mögliche Nachfolger. Die 60 Strahlen sind keine neu
angenommene Hilbertraumdimension: Sie liegen im vorhandenen C4 und sind
zwischen verschiedenen Kontexten meist nicht orthogonal. Die 60 Zustände
des hier konstruierten klassischen Prozesses bezeichnen Kontext und Ergebnis.

T ist symmetrisch, zusammenhängend und besitzt positive Diagonale. Deshalb
hat diese endliche bedingte Markovkette eine eindeutige gleichverteilte
stationäre Verteilung auf den 60 Strahlen. Ihre mittlere Dichtematrix ist I4/4.
Das ist kein ausgewähltes physikalisches Vakuum.

## 4. Derselbe Prozess hat zwei exakt geschlossene Beschreibungen

Sei p eine Verteilung auf den 60 Strahlen. Zwei verschiedene Ausgaben sind:

- C p: nur der Kontext, ohne das Messergebnis;
- E p=sum_(C,s) p_(C,s) Pi_(C,s): der mittlere Quantenzustand, ohne Kontextprotokoll.

Der Prüfer beweist **Matrixidentitäten**, also Aussagen für jede Verteilung
und jede Anzahl Schritte:

\[
CT=KC,\qquad ET=\mathcal D E,
\]

mit

\[
\boxed{\mathcal D(\rho)=\frac37\rho+\frac47\frac{I_4}{4}}.
\]

Folglich gilt C T^n=K^n C und E T^n=D^n E für jedes natürliche n.
Die erste Projektion behält die zuvor geprüften alternierenden
Kontextmoden. Die zweite sieht eine glatte Abschwächung aller nichtskalaren
Quantenkomponenten um 3/7 pro Schritt. Die beiden Beschreibungen sind
verschiedene Ausgaben desselben hier bedingt konstruierten Prozesses.

### Warum gerade 3/7 — ohne Zahlenfit

Nach einer vollständigen Kontextmessung liegt rho in der vierdimensionalen
kommutativen Operatoralgebra dieses Kontextes: Identität plus seine drei
Pauli-Komponenten. Für jede dieser Komponenten enthalten genau **drei der
sieben** erlaubten nächsten Kontexte denselben Pauli-Operator. Dort bleibt
sie erhalten; in den anderen Kontexten wird sie durch die Messung gelöscht.
Das ergibt 3/7. Alle 45 Zählungen wurden exakt geprüft.

Die 60 Projektoren spannen linear den gesamten 16-dimensionalen Operatorraum.
Ihre konvexen Mischungen sind aber nur der Stabilizer-Zustandspolytope, nicht
alle Dichtematrizen auf C4. Die geschlossene Formel gilt direkt für die
Zustände nach den deklarierten Kontextmessungen. Bei beliebigem Eingang und
festgelegtem Anfangskontext muss zuerst dessen Messung berücksichtigt werden.
Es wird kein uneingeschränkter Zugriff auf alle Quantenzustände hergeleitet.

### Was die Kontextwahl weiterhin beiträgt

Wählt man stattdessen alle 15 Kontexte gleichmäßig, mit denselben Projektoren
und derselben wiederholbaren Messregel, entsteht die Abschwächung 1/5.
Diese Gegenkontrolle wurde ebenfalls exakt gerechnet. Das ist kein zweites
Modell mit unverändertem K; es zeigt, welche Aussage von der Ausführung des
spezifischen ursprünglichen K abhängt.

Für gleichmäßige Kontextwahl bilden die 60 Effekte Pi_(C,s)/15 eine
informationsvollständige POVM. Vergisst man alle vier Ergebnisse innerhalb
eines Kontextes, bleibt jeweils I4/15. Das Kontextetikett allein trägt dann
keine Information über den Eingangszustand. Messergebnis und Messfrage
dürfen nicht verwechselt werden.

## 5. Was geschlossen ist und was die neue erste offene Stelle ist

**Geschlossen unter den genannten Voraussetzungen:** eindeutige selektive
Instrumente; vollständiger endlicher Übergangsprozess auf den ursprünglichen
Strahlen; exakte Kontext- und Quantenprojektion; eindeutiger stationärer
Zustand dieses endlichen Prozesses. Keine neue Kette, kein optimierter
Hamiltonoperator und keine angepassten Gewichte waren dafür erforderlich.

**Nicht geschlossen:** Dass der mikroskopische TFPT-Ursprung gerade diese
scharfen wiederholbaren Messungen ausführt und seine Inzidenz tatsächlich
als Kontextwahl K realisiert. Der nächste Herkunftssatz müsste aus der
vorhandenen Seam-/Compiler-Dynamik die selektiven Zweige

\[
\rho_C\longmapsto K_{DC}\Pi_{D,t}\rho_C\Pi_{D,t}
\]

einschließlich Ergebniszugriff und Zusammensetzung gewinnen. Eine frei
gewählte Messapparatur, ein beliebiges Stinespring-Hilfssystem oder eine
nach Wunsch aufgeprägte Kontextwahl wäre nur eine Realisierung der
angenommenen Regel, keine Herkunftsableitung.

Physische Zeit, Energie, räumliche Lokalität, geladene Seam-Felder und der
gemeinsame 3+1D-Ursprung bleiben weitere Pflichten. Alle T1–T8 sind offen.
Kein RH-, Faktorisierungs-, P-vs-NP- oder Hylæan-Abschluss folgt daraus.

## 6. Reproduktion und Implementierungshinweis

Aktueller Laufbeleg: **2.638 endliche Guards** im neuen Kontextprüfer,
normal und mit -OO byte-identisch. Zusammen mit den unveränderten beiden
vorherigen Prüfern sind es 10.574 Guards pro Modus. Alle acht gezielten
Mutationen werden am vorgesehenen Guard zurückgewiesen; die drei neuen
verfälschen Übergangsnormierung, Quantenprojektion und Register-Auslesebasis.
[`verification.json`](verification.json) enthält Ergebnisse und aktuelle
Quell-/Skripthashes. `run_checks.py` reproduziert alle drei Prüfungen.

```sh
python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py
python3 -B -OO experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py
```

Die gepinnte Quellfunktion wird im Speicher nach P1 abgeschnitten; ihre
assert-Anweisungen werden dort zu auch unter -OO aktiven Guards gewandelt.
Der ursprüngliche Quelltext wird nicht verändert. Alle ursprünglichen
P0/P1-Prüfergebnisse müssen wahr sein.

Eine erste Projektorprüfung scheiterte an nicht expandierten Gaußschen
Polynomen in SymPy. Die systematische Fehleranalyse belegte Norm vier und
exakt verschwindenden algebraischen Residualterm. Behoben wurde nur die
Normalform vor dem Matrixvergleich; Normierung und mathematische Prüfungen
wurden nicht abgeschwächt. Es wurde keine numerische Toleranz eingeführt.
