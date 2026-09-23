# Nachgereichter Text B: Korrekturen und ein neuer prüfbarer Feldadapter

Der Text mit 45 Zeilen wurde vollständig gelesen. Seine unveränderte Kopie
steht in `late_sources/attachment_B.txt`, SHA-256
`9aaf5e18cbc6a84d610b88429872df9b69e6078365bfdc8133c8f17e2c1c3801`.
Die für die neue Prüfung maßgebliche `field_dictionary.py` ist gesondert
eingefroren, SHA-256
`a581bacd17c08dd9a766ae439bfe1e8e35e6d30b9509cb9d98053b897d8ecc13`.
Die bereits abgeschlossenen Schatten-Dateien wurden nicht verändert.

## Übernahmeentscheidung

| Aussage im Text | Belastbare Fassung / konkrete Folge |
|---|---|
| 1,44 Milliarden unsichtbare Freiheiten im kleinsten nichttrivialen Sektor | 1444233216 ist die komplexe Kommutantdimension des gewährten Kontrollsatzes X,Nb im N=3-Sektor. Im N=2-Sektor lautet die entsprechende Zahl 3829536. Weder Zahl zählt direkt physische Freiheitsgrade. |
| Mit voller Symmetrie sieben, mit Modenzählern eins; damit nichts Physisches verborgen | Die assoziativen Algebren sind unter den ausdrücklich ergänzten Ressourcen bestimmt. Ein skalarer Kommutant beweist weder vollständige dynamische Lie-Kontrolle noch ausführbare Präparation/Messinstrumente. Ein neuer exakter Spin-1-Gegenzeuge unten trennt diese Aussagen. |
| Die Kontrollfrage ist eine einzige Ja/Nein-Frage | Bereits v1.6.6/7 enthalten Zwischenstufen: einzelner Dunkelprojektor, ein getrennter Casimir, nur SU(4), nur Spin(10). Auch X und Nb unabhängig schalten zu können ist stärker als ein fixes H. |
| Nur beide getrennten Casimire können die drei dunklen Typen unterscheiden | Bereits einer der getrennten Casimire genügt, da seine drei Eigenwerte verschieden sind. Der Gesamtcasimir allein genügt nicht. |
| Der Skalarkanal ist endgültig verboten; Vermittler muss (1,0) sein | Exakt im lokalen, ableitungsfreien Ansatz gleicher Weylhändigkeit mit unverändertem antisymmetrischem W und ohne zusätzliche unabhängige Komponenten. Der symmetrische Kanal trägt dort. Dies ist kein vollständiges Feldwörterbuch jedes möglichen Kontinuumsadapters. |
| Das Lochkomposit besitzt einen brauchbaren Spin-1/2-Projektor | Der angegebene Projektor ist für den **gleichhändigen** Tensorproduktraum korrekt. Für das wörtlich adjungierte Weylfeld ist zunächst die Händigkeit zu klären; die neue exakte Boost-Prüfung unten macht die Konsequenz sichtbar. |
| N=0 modulo vier verkürzt die Grundzustandskonkurrenz auf Singulettsektoren | Die Regel gilt für Singuletts. Erst ein unabhängiger globaler Eindeutigkeitssatz erzwingt für die zusammenhängende halbeinfache Gruppe einen Singulett-Grundzustand. Ohne ihn kann ein tieferes nichtsinguläres, entartetes Multiplett gewinnen. Zudem ist die Liste bosonischer Ladungssektoren nach oben unbeschränkt. |
| 480, 916, 299520/229 sind drei exakte Energiesprossen | Es sind dimensionslose quadrierte Kopplungskoeffizienten, nach Ausklammern von g², keine drei Eigenenergien. Sie stimmen mit dem Anfang der richtigen Voll-H-Lanczoskette überein. |
| Nur die gesamte 33-Sprossen-Leiter fehlt noch | 33 zählt die Bosonzahlstufen k=0,…,32 bei N=64. Eine Zustandsrichtung je Stufe schließt unter H nicht. Schon k=2 hat vier Singuletts; das Rücklaufresiduum besitzt exakt positive Norm 5001523200/229. Die tatsächliche vierte Voll-H-Lanczosdiagonale ist 105168998/26292551·Δ, nicht 4Δ. |
| Ritzüberlappung 39,7 Prozent bestätigt den wahren Grundzustand | Der Wert gehört zum benannten Ritz-Zustand. Ohne Residuum und Spektralabstand ist er keine entsprechende Überlappungsaussage über Ω. Die zitierte Ritzenergie setzt außerdem g/Δ=1/20 voraus. |
| Schwächere Nachbarsektorfloors lassen Grundzustandssatz wieder offen | Sie lassen diese schwächere Sonde offen. Das widerlegt oder ersetzt den stärkeren vorherigen Satz im unveränderten Modellvertrag nicht. |
| Operationssatz und Feldwörterbuch fertig; räumliche Skalierung jetzt freigegeben | Die erforderlichen Ressourcen und der Lorentzadapter sind weiterhin konkrete offene Verbindungen. Die neue gemeinsame Schattenkarte bestimmt deren nächste Prüfung wesentlich genauer als diese pauschale Freigabe. |

Die normierte direkte Summe der drei Feldkanäle hat weiterhin Norm
8√3 bei Normquadrat 192. Die eingefrorene Feldquelle enthält noch die
bereits korrigierte Addition von drei Normen zu 24; ihr gesamtes grünes
Ergebnis wurde daher nicht als unkritischer Vertrauensbeweis übernommen.

## 1. Neuer exakter Kontrollgegenzeuge

Die gewöhnlichen drei Spin-1-Matrizen J_x,J_y,J_z auf C³ erfüllen
[J_x,J_y]=iJ_z und zyklisch. Bereits J_x und J_z haben ausschließlich
skalare gemeinsame Kommutanten. Der dynamische Lie-Raum ist trotzdem nur
su(2) mit Dimension drei, nicht su(3) mit Dimension acht. Das wird im
neuen Prüfer durch exakte Ränge und alle drei Kommutatoren kontrolliert.

Damit ist die Unterscheidung praktisch: Ein assoziativer Abschluss kann
vollständig sein, während die tatsächlich durch Hamiltonpulse erreichbaren
Unitären eine echte Untergruppe bilden. Für den nativen Kontrollvertrag
braucht es weiterhin die konkret gewährten Generatoren, ihre dynamische
Lie-Algebra und eine ausgeführte Puls-/Instrumentenfolge.

## 2. Was am Spin-1/2-Projektor stimmt

Die Feldquelle verwendet die sechs unnormierten Koordinaten

`(00,0), (00,1), (01,0), (01,1), (11,0), (11,1)`,

wobei `(01)` die Summe `|01>+|10>` bezeichnet. Die korrekte Gram-Matrix ist

\[
 G_6=\operatorname{diag}(1,1,2,2,1,1).
\]

Der neue Prüfer baut den vollständigen Symmetrisierer auf drei Spinorindizes
unabhängig neu auf. Zugleich konstruiert er die direkte Epsilon-Auslese

\[
 C=\begin{pmatrix}0&1&-1&0&0&0\\0&0&0&1&-1&0\end{pmatrix},
 \qquad R=\frac23G_6^{-1}C^T.
\]

Exakt gelten

\[
 CR=I_2,\quad P_{1/2}=RC,\quad
 P_{3/2}=I_6-P_{1/2},\quad
 CP_{3/2}=0,\quad CP_{1/2}=C.
\]

Beide Projektoren sind idempotent, komplementär und haben Rang zwei
beziehungsweise vier. P_{1/2} ist selbstadjungiert bezüglich G_6;
seine nicht symmetrische 6×6-Koordinatenmatrix ist kein Fehler.
Die Epsilon-Auslese und Wiedereinsetzung intertwinen exakt alle drei
sl(2)-Generatoren. Dies liefert eine ausführbare algebraische Extraktionsregel
im **angenommenen gleichhändigen** Raum

\[
 (1,0)\otimes(1/2,0)=(3/2,0)\oplus(1/2,0).
\]

Die Zahl 1/3 ist nur der Ranganteil im isotropen Zustand. Der neue Prüfer
zeigt positive reine Vektoren mit Spin-1/2-Gewicht null und eins. Deshalb
ersetzt der Projektorrang keine Berechnung seines Gewichts im nativen
Grundzustand oder im geladenen Spektralpol.

## 3. Die neue präzise Händigkeitsschranke

Die eingefrorene Tabelle in `field_dictionary.py`, Zeile 327, bezeichnet
den zweiten Faktor als `f^dagger (1/2,0)`. Dafür muss die Feldabbildung
explizit festgelegt werden. Für ein tatsächliches adjungiertes linkes
Weylfeld gilt dagegen ψ† in (0,1/2). Hermitesche Konjugation vertauscht
diese Darstellungen; siehe [Dreiner, Haber und Martin, Abschnitt 2](https://arxiv.org/pdf/0812.1594#page=9).

In diesem **wörtlichen Feldadjungierten-Fall** ist das Produkt

\[
 (1,0)\otimes(0,1/2)=(1,1/2)
\]

ein irreduzibler Lorentzraum mit komplexer Dimension sechs. Unter der
Rotationsuntergruppe zerfällt er weiterhin in Spin 3/2 und Spin 1/2;
diese beiden Rotationsräume sind aber nicht getrennt boostinvariant.
Der Prüfer verifiziert den skalaren Kommutanten sämtlicher sechs
Generatoren des komplexifizierten Lorentzraums; die beiden unabhängigen
sl(2)-Faktoren wirken als irreduzibles äußeres Tensorprodukt.

Ein konkreter Zeuge genügt bereits. In obiger Basis setze

\[
 J_z=J_z^{(1)}\otimes I_2+I_3\otimes J_z^{(1/2)},\qquad
 K_z=J_z^{(1)}\otimes I_2-I_3\otimes J_z^{(1/2)}.
\]

Bis auf den konventionellen Faktor i ist K_z der Boostgenerator für
entgegengesetzte Händigkeit. Dann gilt exakt

\[
 [P_{1/2},J_z]=0,\qquad
 [P_{1/2},K_z]=
 \begin{pmatrix}
 0&0&0&0&0&0\\
 0&0&4/3&0&0&0\\
 0&-2/3&0&0&0&0\\
 0&0&0&0&2/3&0\\
 0&0&0&-4/3&0&0\\
 0&0&0&0&0&0
 \end{pmatrix}.
\]

Dieser Kommutator hat Rang vier. Der Rotationsprojektor kann deshalb
in diesem Vertrag nicht als Lorentz-kovarianter Weyl-Ausleseprojektor
verwendet werden.

**Das ist kein pauschaler Ausschluss des ursprünglichen Modenkomposits.**
Ein bloßer Fock-Erzeuger f† ist noch kein adjungiertes lokales Weylfeld.
Bereits die übliche linke Weylfeldentwicklung enthält Erzeugungs- und
Vernichtungsterme mit passenden Spinorwellenfunktionen; siehe
[Dreiner, Haber und Martin, Gleichungen 3.1.3–3.1.5](https://arxiv.org/pdf/0812.1594#page=24).
Eine unabhängige oder passend ladungskonjugierte gleichhändige Komponente
kann den gleichhändigen Projektor erhalten. Sie muss aber als konkreter
Adapter mit korrekter Ladung, CAR, W-Kontraktion und Dynamik gezeigt werden.
Aus dem Symbol † allein folgt weder ihr Vorliegen noch ihr Ausschluss.

## 4. Konkreter nächster Annahmetest

Der Anschlussauftrag ist jetzt endlich und entscheidbar formuliert:

1. Den tatsächlichen Feldadapter für `D_r ∼ b f†` beziehungsweise den davon
   verschiedenen `χ† ∼ b†ηf†` hinschreiben: gepunktete/ungepunktete Indizes,
   Ladung, Fourieranteile, erlaubte Zusatzkomponenten.
2. Für genau diesen Adapter alle Rotations- **und Boostgeneratoren** auf
   dem zusammengesetzten Träger berechnen. Ein Kandidat mit Lorentz-Auslese
   C muss `C L_composite = L_Weyl C` erfüllen. Der neue gleiche-/gegengängige
   Test liefert dafür positive und negative Referenzfälle.
3. Die Kontraktion am unveränderten W ausführen und anschließend das
   tatsächliche Matrixelement `C D_r†|Ω>` beziehungsweise den entsprechenden
   Ladungskanal berechnen. Erst dessen normiertes Spektralgewicht kann den
   vorhandenen geladenen Pol mit einem Spin-1/2-Feld verbinden.
4. Falls der wörtlich adjungierte Fall gewählt wird, keinen bloßen
   Rotationsprojektor als Lorentzprojektor verwenden. Ein zusätzlicher
   Impuls-/Ableitungsadapter oder eine andere Händigkeit kann untersucht
   werden, zählt aber als ausdrückliche neue Struktur.

Dieser Test ergänzt die gemeinsame Schattenrekonstruktion: Die dort
bewiesene vollständige innere Tomographie ersetzt die hier fehlende
Lorentz-Intertwining-Abbildung nicht. Umgekehrt definiert ein richtiger
Lorentzprojektor noch kein ausführbares natives Messinstrument.

## Reproduktion

```sh
python3 -B replay_late_field.py
```

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei
Quellenpins sowie **36 exakte Bedingungen pro Modus**, keine numerischen
Bedingungen. Normaler Lauf und `-OO` ergeben byte-identische JSON-Ausgaben;
Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv.
Die vollständigen Matrizen stehen in `late_field.normal.json`.

Das Ergebnis-JSON hat SHA-256
`cfd9e15cec5c2b0ce3de9397614836b16b24b4adb8f6711eb704925589965774`.
Der Prüfer hat SHA-256
`f18e6fd2af7c1a28a81e85654df68fe805e59b1d957801611d2668678550dfc2`.
Die fremde Feldsuite wird nur eingefroren und punktuell unabhängig geprüft,
nicht als vollständig fehlerfreie Gesamtreproduktion ausgegeben.
