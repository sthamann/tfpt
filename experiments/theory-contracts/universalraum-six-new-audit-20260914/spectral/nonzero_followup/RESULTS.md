# Der ganze 24024D-Singulettsektor ist jetzt spektral zertifiziert

14. September 2026. Modell: kantenlokaler Clebsch-Austausch,
H0/J=20I+X/2, X=Σ_e S_e, Htr/J=H0/J+F4/800 bei epsilon=t/Delta=1/20.
Dieser neue Anschluss bearbeitet ausschließlich die elf zuvor fehlenden
Singuletttypen mit nichttrivialem Translationscharakter. Er verändert die
vorherigen 348D- und 1764D-Zertifikate nicht.

## Abschließender Satz

**Alle 18 Symmetrietypen des vollständigen 24024-dimensionalen
SU(4)-Singuletts sind jetzt kontrolliert.** Im gesamten Singulett besitzt
Htr genau fünf Eigenwerte unter 12,45 J:

- ein einfaches Grundniveau;
- darüber ein exakt vierfaches Niveau;
- alle übrigen Singulett-Eigenwerte liegen strikt über 13,10732519 J.

Die ersten beiden Energien liegen rigoros in

\[
11.960507412<E_0/J<11.960507414,
\]

\[
12.4469215409<E_1/J<12.4470238436.
\]

Die nach außen gerundeten Schranken für den **globalen Singulett-Gap** sind

\[
\boxed{0.4864141269280<(E_1-E_0)/J<0.4865164315432.}
\]

Der Abstand oberhalb des Quartetts zum restlichen Singulettspektrum ist
strikt größer als **0,6603013464568 J**. `complete.json` enthält sämtliche
exakten rationalen Grenzen; die hier gedruckten Dezimalenden sind jeweils
nach außen gerundet.

**Das ist ein vollständiger Singulettsatz, kein Vollraumsatz:** Die anderen
63 SU(4)-Sektoren und der kanonisch passende mikroskopische Rest sind noch
nicht kontrolliert. Auch die native Herkunft des gewählten Wedge-/Kanten-
Hamiltonoperators folgt daraus nicht.

## Die elf neuen, vollständig ausgeschlossenen Typen

Es genügt je ein Repräsentant des Translationscharakterorbits. Bei Gewicht 1
ist die kleine Gruppe S4, bei Gewicht 2 S2×S3. Die Orbitgrößen 5 und 10 sind
in der vollen Trägerdimension berücksichtigt.

| Gewicht | Kleine Darstellung(en) | Multiplizität m | Ganze Trägerdimension | H0/J strikt größer als | Htr/J strikt größer als |
|---|---|---:|---:|---:|---:|
| 1 | (4) | 54 | 270 | 14,0449275 | 14,76223185 |
| 1 | (3,1) | 176 | 2640 | 12,7778645 | 13,57119263 |
| 1 | (2,2) | 124 | 1240 | 13,339095 | 14,0987493 |
| 1 | (2,1,1) | 194 | 2910 | 12,617896 | 13,42082224 |
| 1 | (1,1,1,1) | 72 | 360 | 13,1398395 | 13,91144913 |
| 2 | (2) × (3) | 124 | 1240 | 12,8301855 | 13,62037437 |
| 2 | (2) × (2,1) | 262 | 5240 | 12,2843885 | **13,10732519** |
| 2 | (2) × (1,1,1) | 140 | 1400 | 12,6114225 | 13,41473715 |
| 2 | (1,1) × (3) | 106 | 1060 | 12,9114935 | 13,69680389 |
| 2 | (1,1) × (2,1) | 232 | 4640 | 13,4720985 | 14,22377259 |
| 2 | (1,1) × (1,1,1) | 126 | 1260 | 13,4063425 | 14,16196195 |

Die vollen Trägerdimensionen summieren sich zu **22260**. Zusammen mit den
bereits kontrollierten 1764 Nullimpulsdimensionen ergibt das exakt 24024.
Die schwächste neue Schranke stammt vom 262D-Multiplizitätsblock; auch sie
liegt mit deutlichem Abstand oberhalb der Quartett-Obergrenze.

## Gewichtete Mackey-Projektoren sind exakt konstruiert

Für den kanonischen Charakter mit Gewicht w=1 oder 2 ist

\[
\chi_w(f)=\prod_{i=0}^{w-1}f_i,
\qquad P_{\chi_w}=\frac1{16}\sum_f\chi_w(f)\rho(f).
\]

Die vier Translationserzeuger wechseln jeweils Koordinate k und Koordinate
4. Ihr Charaktervorzeichen ist deshalb -1 für k<w, sonst +1. Der Prüfer
realisiert Pχ als Produkt der vier entsprechenden Zweiermittel.

Auf den stabilisierten Koordinaten 1,2,3,4 für w=1 beziehungsweise auf den
beiden Mengen (0,1) und (2,3,4) für w=2 werden primitive Youngsymmetrisierer
e=Spaltenantisymmetrisierer×Zeilensymmetrisierer/Hakenprodukt eingesetzt.
Bei Gewicht 2 kommutieren die beiden Faktoren. Ihre Produkte kommutieren
mit dem gewichteten Translationsmittel.

Der Prüfer verifiziert unabhängig und ganzzahlig:

1. e²=e in der vollständigen kleinen Gruppenalgebra;
2. Spur 1 auf der gewünschten kleinen Irrep, Spur 0 auf jeder anderen;
3. Stabilisierung des gewählten Translationscharakters;
4. den vollständigen Rang von Pχe auf dem 24024D-Spechtmodul mittels einer
   neuen gewichteten Charakterrechnung.

`projectors.json` enthält die elf Ergebnisse und **95 exakte Bedingungen**.
Damit sind die reduzierten Ränge keine nur vorgegebenen numerischen Ziele.
Der größte konstruierte Raum hat tatsächlich 262 Dimensionen und steht für
einen 5240D-isotypischen Träger. Er wurde nicht mit diesem verwechselt.

## Vollständige modulare Blockidentitäten

Für sieben verschiedene Primzahlen nahe 10^8 werden alle elf reduzierten
Matrizen unabhängig aus der rationalen seminormalen Youngdarstellung
konstruiert. Zufällige Spalten dienen nur zur Auswahl eines Basiskandidaten;
sein voller Rang wird durch exakte Pivots bestätigt.

An sämtlichen 24024×m Einträgen werden geprüft:

\[
eB=B,\qquad \rho(T_k)B=\chi_w(T_k)B,\qquad XB=B X_{\rm red}.
\]

Jeder Primmodulsatz enthält **89 explizite Bedingungen**, einschließlich der
Negativkontrolle eines veränderten X-Matrixeintrags. Insgesamt liegen hier
**77 vollständige kleine X-Matrizen**. Bei der größten Matrix werden alle
24024×262=6294288 Einträge der Intertwineridentität geprüft.

Das ganzzahlige 64-Bit-Produkt bleibt sicher: Höchstens 262 Summanden mit
Faktoren kleiner als 10^8 ergeben weniger als 2,62×10^18, unterhalb 2^63.
Die vollständigen Eigenwertpolynome sind für diesen Ausschluss nicht nötig
und wurden hier nicht konstruiert.

## Sechs CRT-Primzahlen und eine unabhängige Kontrolle

Jeder echte reduzierte Block ist bezüglich eines positiven inneren Produkts
selbstadjungiert. Daher gilt für jedes seiner Eigenwerte x

\[
|x|^{32}\le M=\operatorname{tr}X_{\rm red}^{32}.
\]

M ist ganzzahlig: X ist ein ganzzahliger Gruppenalgebraoperator; der rationale
invariante Raum erhält das Schnittgitter mit einem ganzzahligen Spechtgitter.
Aus der schon vorher exakt bewiesenen Singulett-Sternschranke folgt ||X||<=24,
also die vorab festgelegte Rekonstruktionsgrenze

\[
0\le M\le m24^{32}.
\]

Sechs Primzahlen überschreiten zusammen zweimal diese Grenze, selbst bei
m=262. Die CRT-Rekonstruktion von M ist somit eindeutig. Eine siebte, bei der
Rekonstruktion unbenutzte Primzahl bestätigt jeden Momentenwert unabhängig.
Ein veränderter Momentenwert wird von dieser Kontrolle zurückgewiesen.

Der rationale Radius r wird anschließend mit r^32>M durch reine
Ganzzahlarithmetik zertifiziert. Daraus folgen X>-rI und H0>20-r/2. Die schon
bewiesenen Operatoruntergrenzen

\[
H_{\rm tr}\ge\frac{47}{50}H_0+\frac{39}{25}I,
\qquad
H_{\rm tr}\ge\frac{93}{100}H_0+\frac{42}{25}I
\]

liefern die Tabellenwerte. Es handelt sich um Untergrenzen des **ganzen
Blocks**, einschließlich bislang unbekannter Eigenvektoren. Der Prüfer
benötigt keine numerische Ritzliste. Eine gegebenenfalls zu schwache
Spurschranke würde als nicht ausgeschlossener Typ ausgegeben; hier besteht
der Ausschluss für alle elf Typen.

## Letzter unabhängiger Zusammenschluss

`complete_replay.py` prüft die Projektorränge, Quellenprüfsummen und
Dimensionsbilanz, rekonstruiert die unbenutzten Kontrollspuren erneut aus
den vollen kleinen Matrizen und wiederholt die rationalen Temple-Rechnungen
sowie die exakten Wurzelzählungen des trivialen 28D-Blocks.

Der Schluss auf genau fünf niedrige Eigenwerte benutzt zusätzlich die schon
bewiesenen zweiten Eigenwertgrenzen des trivialen und des Standardblocks.
Die Minimumsschranke für alle übrigen Typen ist 13,10732519. Damit sind
Einfachheit, Symmetrievielfachheit und globale Ordnung innerhalb des
Singuletts jetzt getrennt begründet und anschließend zusammengeführt.

Der Momentenzertifikatslauf besteht mit **166 Bedingungen**, der abschließende
Gesamtreplay mit **104 Bedingungen**, jeweils normal und mit `-O`.
`complete.json` bezeichnet ausdrücklich nur den Singulettabschluss.

## Was für den nächsten Spektralanschluss noch fehlt

Die Hypothese H0>=11,58 auf allen Nichtsinguletts würde mit der zweiten
affinen Untergrenze Htr>=12,4494 liefern und dadurch auch diese Sektoren
gegenüber dem nun global im Singulett zertifizierten Quartett ausschließen.
**Diese Hypothese ist hier nicht bewiesen.** Die Anzahl der physischen
SU(4)-Youngsektoren beträgt 64, einschließlich des einen Singuletts; die
übrigen 63 sind eine eigene endliche Aufgabe.

Für einen bereits auf genau demselben Singulettträger identifizierten,
graphsymmetrieerhaltenden effektiven Rest R wäre
||R||<0,2432070634640 J eine hinreichende Bedingung, um das isolierte Muster
1+4 zu erhalten. Dies folgt aus den zwei bewiesenen Abständen und Weyl.
Es ist **keine berechnete mikroskopische Restnorm** und ersetzt weder die
effektive Identifikation noch die Kontrolle anderer Materie-/Vermittlerbänder.

## Reproduktion und Dateien

Schnelle Wiedergabe aus den gespeicherten exakten Matrizen:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py projectors
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py certify
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 complete_replay.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 -O complete_replay.py
```

Vollständiger Neubau mit sechs Rekonstruktions- und einer Kontrollprimzahl:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py build --primes 99999989 99999971 99999959 99999941 99999931 99999847 99999839
```

Die sieben voneinander unabhängigen Primmodulläufe wurden auf dem vorhandenen
32-CPU-Rechner parallel ausgeführt. Jeder benötigte etwa 145–147 Sekunden und
endete mit Status 0. Es wurden ausschließlich Dateien im eigenen
`spectral/nonzero_followup`-Ordner erstellt. Keine Fremdänderungen, keine
Commits, keine PDFs, keine laufenden Hintergrundprozesse als unerklärter Rest.

Es handelt sich um computerunterstützte exakte Integer-/Modulararithmetik
unter den angegebenen Standarddarstellungssätzen, nicht um eine neue
Lean-Kernprüfung oder einen bereits geschlossenen TOE-Beweis.
