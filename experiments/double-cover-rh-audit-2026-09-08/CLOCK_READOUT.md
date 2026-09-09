# Ein normierter Carrier-/Seam-Readout erhält die vorhandenen Clock-Sektoren

**Weiterführung:** [INTERAKTIONSAUSWAHL.md](INTERAKTIONSAUSWAHL.md) zeigt,
dass genau dieser Raum bereits als Bild der Kopplungsmatrix und als
Träger ihrer thermischen Antwort charakterisiert ist. Eine vorherige
Auswahl aller Carrier-Komponenten ist zu seiner Definition nicht nötig.

8. September 2026. Fortsetzung von
[GEOMETRIE_UND_READOUT.md](GEOMETRIE_UND_READOUT.md).
Lokale Untersuchung der vorhandenen endlichen Quellfamilie; keine Änderungen
am Compiler oder an seinen bisherigen Verifiern, keine Statuspromotion.

**Der Clock-Verlust gehört zum reinen Boundary-Zugriff, nicht zum gesamten
Quellmodell.** Aus dem bereits verwendeten Kanal-Stack lässt sich ein
normierter Readout mit zwölf Majorana-Komponenten bilden. Er erhält die
volle Carrier-Information, die gekoppelte Boundary-Richtung, Dynamik,
Reflexion und sämtliche in der Quelle vorhandenen Clock-Charaktere.

Das ist eine konkrete endliche Zustandsabbildung. Sie ist ein kombinierter
Carrier-/Seam-Zugriff und keine Reparatur des bisherigen reinen Boundary-
Ports. Ihre Identifikation mit dem physikalischen TFPT-Readout oder dem
QWZ-Modell bleibt offen.

## 1. Ausgangspunkt ist eine bereits vorhandene Konstruktion

Die Quelle
[`seam_state_derivation_probe.py`](../tfpt-discovery/seam_state_derivation_probe.py)
ordnet zehn Carrier-Komponenten fünf Paaren zu. Die sechs Boundary-
Komponenten sind drei weitere Paare. Ihr bestehender Stack ist

\[
\mathcal I=\begin{pmatrix}I_2\\I_2\\I_2\end{pmatrix},\qquad
\mathcal I^T\mathcal I=3I_2.
\]

Die Funktion `compress12` verwendet bereits die gleichförmige Boundary-
Richtung und behält die fünf Carrier-Kanäle. Sie extrahiert allerdings
**Duaden-Kopplungsblöcke für Pfaffian-Auswertungen**. Sie mittelt mit dem
Faktor 1/3 und entfernt sämtliche kanaldiagonalen Blöcke. Das ist nicht
dieselbe Operation wie die Einschränkung eines CAR-Zustands.

Auch die endliche Pfaffian-/Spektralstruktur wurde in dieser Quelle bereits
untersucht. Die hier verwendeten kubischen Spektralfaktoren sind deshalb
keine neu entdeckte arithmetische Struktur. Neu in dieser Auditfolge ist
ihre genaue Verbindung mit dem normierten Readout und der zuvor gefundenen
Reflexion.

## 2. Die normierte Abbildung und ihr Bild

Ordne die zwölf Ausgabekomponenten als Boundary-Paar, gefolgt von den fünf
Carrier-Paaren. Die zugehörige Isometrie in den ursprünglichen 16D-Raum ist

\[
W=\begin{pmatrix}
0_{10\times2}&I_{10}\\
\mathcal I/\sqrt3&0_{6\times10}
\end{pmatrix},\qquad W^TW=I_{12}.
\]

Der Projektor auf ihr Bild lautet

\[
P=WW^T=\operatorname{diag}(I_{10},\mathcal I\mathcal I^T/3).
\]

Die Wahl der positiven Normierung ist die isometrische Normierung des
bereits vorhandenen Stacks, kein Anpassen an gewünschte Eigenwerte. Andere
Zustandskanäle mit zusätzlichen Umgebungsdaten werden dadurch nicht
ausgeschlossen; solche Daten wurden hier nicht hinzugefügt.

Für die unveränderten Quellmatrizen \(A,B,O\) und die rationale Reflexion
\(U\) aus dem vorigen Bericht ergibt sich exakt

\[
[P,A]=[P,B]=[P,O]=[P,U]=0,\qquad B(I-P)=0.
\]

Es werden also nur vier Boundary-Komponenten entfernt, die von \(B\)
entkoppelt sind. Die zehn Carrier-Komponenten bleiben vollständig erhalten.

Diese zwölf Dimensionen sind minimal **unter der festen Forderung**, alle
zehn Carrier-Komponenten zu behalten und unter der Kopplung \(B\) invariant
zu sein: Die Matrix aus den Carrier-Vektoren und ihren \(B\)-Bildern hat
exakt Rang zwölf. Dies ist kein Minimalitätssatz über alle denkbaren
Messverfahren. Auf der ungekoppelten Achse wäre diese Erweiterung nicht
erforderlich.

## 3. Zustands- und Dynamikabbildung sind hier gleichzeitig exakt

Definiere

\[
H_{12}=W^THW,\quad O_{12}=W^TOW,\quad U_{12}=W^TUW.
\]

Da das Bild von \(W\) für diese Operatoren reduzierend ist, gelten

\[
HW=WH_{12},\quad OW=WO_{12},\quad UW=WU_{12}.
\]

Damit bleiben

\[
U_{12}^2=I,\qquad U_{12}H_{12}U_{12}=-H_{12},\qquad
U_{12}O_{12}U_{12}=O_{12}^{-1}
\]

erhalten. Für jeden endlichen thermischen Zustand bei \(\beta>0\) gilt

\[
\boxed{C_{12}=W^TC_\beta W=(I+e^{\beta H_{12}})^{-1}},
\]
\[
\boxed{K(C_{12})=\beta H_{12}=W^TK(C_\beta)W}.
\]

Das widerspricht nicht dem vorigen Gegenbeispiel zur Vertauschbarkeit von
Kompression und Logarithmus: Dort war der kleinere Zweirand-Unterraum nicht
für den Hamiltonian reduzierend. Hier ist genau diese zusätzliche
Voraussetzung bewiesen. Bei endlichem \(\beta\) ist der Zustand treu;
Eigenwerte werden nicht künstlich abgeschnitten.

## 4. Welche Clock-Information jetzt ankommt

Die charakteristische Clock-Gleichung ist

\[
\det(zI-O_{12})=(z-1)^6(z+1)^2(z^2+z+1)^2.
\]

Die sechs C6-Charaktere \(e^{2\pi ir/6}\) besitzen damit folgende
Multiplizitäten:

| r | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Multiplizität | 6 | 0 | 2 | 2 | 2 | 0 |

Die Quelle hatte selbst keine r=1,5-Sektoren. Alle ihre nichttrivialen
Sektoren sind erhalten; entfernt wurden ausschließlich vier Clock-Fixmoden.

Ein direktes Signal ist die mit Clock-Potenzen gewichtete Energiespur:

\[
\operatorname{Tr}(O_{12}^kH_{12})
=(0,6it,-6it,0,6it,-6it),\qquad k=0,\ldots,5.
\]

Sie ist bei nichtverschwindender Kopplung nicht konstant. Der Readout hat
damit rechnerisch nachgewiesenen Zugriff auf die nichttriviale Clock-Struktur.
Dieser Zugriff entsteht durch die mitbeobachteten Carrier-Komponenten,
nicht durch eine neue Wirkung der Clock auf die alte Boundary.

Die vollständigen zwölf Energieeigenwerte sind weiterhin endlich und
explizit beschreibbar:

- Sechs Werte \(\pm(u+t\lambda_j)\), wobei
  \(\lambda_j^3-\lambda_j^2-21\lambda_j+9=0\).
- Vier Werte \(\pm u\pm\sqrt3t\), mit unabhängigen Vorzeichen.
- Zwei Werte \(\pm(u-t)\).

Die letzten sechs Werte gehören zu den vormals unsichtbaren Clock-Sektoren.
Diese endliche Liste ist kein neues Zeta-Spektrum.

Die reine Boundary-Selektion bleibt unverändert: Ein linearer
amplitudenerhaltender Intertwiner von einem Port mit trivialer Clock-Wirkung
kann nur im Clock-Fixraum landen. Das verbietet nicht beliebige globale
invariante Messungen von Sektorbesetzungen; solche Messungen verwenden
andere Observablen als den hier untersuchten Boundary-Port.

## 5. Warum die bestehende Graphverdichtung kein Zustandskanal ist

Zwei getrennte Punkte wurden geprüft:

**Normierung.** Der rohe Mittelungsoperator \(L\) mit Boundary-Block
\(\mathcal I/3\) erfüllt

\[
L^TL=\operatorname{diag}(I_2/3,I_{10})\ne I_{12}.
\]

\(L^TCL\) ist somit nicht die Kovarianz kanonisch normierter neuer CAR-
Generatoren. Die Matrixkompression ist zwar positiv, aber nicht unital.
Auf \(C=I/2\) liefert sie für die Boundary 1/6 statt 1/2. \(W\) behebt
diese konkrete Normierungsfrage. Als physikalischer Kanal müsste ein
anderer Ansatz zusätzliche Rausch-/Umgebungsdaten ausdrücklich angeben.

**Weglassen der kanaldiagonalen Blöcke.** Die vorhandene Funktion
`compress12` tut zusätzlich genau dies. Bereits \(A=I_8\otimes J\) wird
dadurch auf null abgebildet. Für ihre vorgesehene Kopplungsgraph-Auswertung
ist das verständlich; als vollständige Kovarianz wäre es Informationsverlust.

Es existiert sogar ein exaktes positives Gegenbeispiel. Auf drei Carrier-
Paaren setze

\[
R=I_3-\tfrac23\mathbf1\mathbf1^T,\qquad
A_c=\tfrac9{10}(R\otimes J),\qquad C_c=(I+iA_c)/2.
\]

\(R^2=I\), daher hat \(C_c\) ausschließlich Besetzungswerte 0,05 und
0,95. Ergänzt um die übrigen Paare ist dies ein treuer C6-invarianter
CAR-Zustand. Entfernt man wie im Graph-Extraktor die kanaldiagonalen
Blöcke, enthält die so missinterpretierte Ausgabekovarianz dagegen die
Eigenwerte **−0,1 und 1,1**. Sie ist kein zulässiger Zustand.

Die normierte Zustandsabbildung \(W^TCW\) bleibt für denselben Eingang
innerhalb des zulässigen Intervalls. Die exakten rationalen Eigenwerte des
Gegenbeispiels wurden im separaten Zertifikatsprüfer bestätigt.

**Folgerung:** Duaden-/Pfaffian-Daten und eine vollständige physikalische
Kovarianz dürfen nicht gleichgesetzt werden. Der ursprüngliche Verifier
wurde nicht geändert; seine beabsichtigte Graph-Auswertung wird durch
dieses Gegenbeispiel nicht widerlegt.

## 6. Was dadurch geschlossen ist und was nicht

Die konkrete Kette

\[
\text{vorhandener Kanal-Stack}
\longrightarrow W
\longrightarrow(C_{12},H_{12},O_{12},U_{12})
\]

ist nun auf dieser endlichen Quelle gemeinsam und exakt konstruiert.
Normierung, Zustandspositivität, dynamische Verträglichkeit, modularer
Readout und Clock-Zugriff wurden nicht an voneinander unabhängigen
Spielmodellen nachgewiesen, sondern an denselben Matrizen.

Der vorherige Markierungswiderspruch bleibt jedoch bestehen:
\(\operatorname{Tr}(P_3B_{12}P_2B_{12}P_BB_{12})=-36\).
Der neue Readout hebt weder diesen Widerspruch noch die notwendige Umkehr
der Familienwirkung auf. Er identifiziert auch keine zusätzliche
QWZ-Holonomie oder einen gemeinsamen physikalischen Zustand beider Modelle.

Für TFPT ist damit die fehlende **endliche Beobachtbarkeit** unter einem
explizit erweiterten Zugriff geschlossen. Die physikalische Auswahl dieses
kombinierten Zugriffs bleibt eine eigene Pflicht. Die zwölf Komponenten
sind eine Ein-Teilchen-/Majorana-Darstellung, nicht die Dimension des
vollständigen Fock-Zustandsraums.

Für RH fehlen nach wie vor eine hergeleitete unendliche arithmetische
Skalenwirkung, die genaue Spuridentifikation und globale Positivität.
Die Clock hat weiterhin feste Ordnung sechs. Ihre vorhandenen 2er- und
3er-Strukturen sind Eingaben dieser Quelle, kein Generator aller Primzahlen.

Für Faktorisierung gibt es keine neue Abhängigkeit von einer zu
faktorisierenden Zahl und keinen gemessenen algorithmischen Vorteil.
Die Erweiterung des Zugriffs ist eine endliche Beobachtbarkeitsreparatur,
kein neuer Faktorisierungsalgorithmus.

Der nächste nicht redundante Vertrag wäre daher eine aus dem physikalischen
Parent abgeleitete Portabbildung auf genau diese gemeinsam verträglichen
Observablen, einschließlich ihrer Markierungs-/Familienwirkung. Für einen
RH-Anschluss muss zusätzlich eine kompatible wachsende arithmetische
Darstellung entstehen. Ein weiterer isolierter endlicher Clock- oder
Determinantentest würde diese Auswahl und Erweiterung nicht ersetzen.

## 7. Reproduktion

```sh
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/clock_readout_probe.py
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/check_readout_certificate.py
```

- [Hauptprobe](clock_readout_probe.py): **22/22 Prüfungen bestanden**.
  [Protokoll](clock_readout.log), [Ergebnisdaten und Quellhashes](clock_readout_results.json).
- [Separater Zertifikatsprüfer](check_readout_certificate.py): bestätigt
  gespeicherte Isometrie und reduzierte Matrizen, Clock-Sektoren und ein
  exakt rationales Positivitätsgegenbeispiel ohne erneute AST-Extraktion der
  Graphfunktion. [Protokoll](readout_certificate.log).
- Zwölf thermische Stichproben: maximaler Kovarianzfehler
  \(7{,}8\cdot10^{-16}\), modularer Fehler \(6{,}8\cdot10^{-14}\).
  Die allgemeinen Aussagen folgen aus den exakten Intertwiner-Identitäten.
- Beide Prüfer teilen den ursprünglichen Compiler-Extraktor. Die Gegenprüfung
  ist keine unabhängige Herleitung der gesamten Quellkonstruktion.
- Bei der ersten Regression war das erwartete Vorzeichen einer Kopplung
  noch in Carrier-zuerst-Reihenfolge formuliert. Der hier benutzte
  Boundary-zuerst-Ausgaberaum hat das entgegengesetzte Blockvorzeichen.
  Korrigiert wurde nur diese Erwartung, nicht die Quellmatrix oder der Readout.
