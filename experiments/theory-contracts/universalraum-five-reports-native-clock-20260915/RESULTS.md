# Fünf Berichte: kleinere Clock-Konstruktion und ein direkter Dynamiktest

15. September 2026. Forschungsnotiz, NON-RH; keine Beförderung in Ledger,
Verification-Status, Paper oder Webseite. Keine TOE-Schließung.

## Ergebnis zuerst

Die Berichte liefern brauchbare algebraische Bausteine, aber keine eindeutige
physische Quelle. Drei Punkte sind neu präzisiert:

1. Ein korrigierter C5-Clock mit seinem binären Vierer-Getriebe passt bereits in
   den vorhandenen nativen Raum 16⊗4. Vier zusätzliche 64er-Bänke sind für diese
   Darstellung nicht erforderlich. Die vollständige W-Kovarianz hält exakt.
2. Dieser konkrete 30er-Clock ist nicht zum E8-Coxeter-Lift konjugiert. Außerdem
   sind Galois-Konjugation und geometrische Spiegelung verschiedene Operationen.
3. Für den ursprünglichen Hamiltonoperator bestimmen zwei zentrale Zeit-/Energie-
   Momente einer festgelegten Präparation die beiden Parameter. Ein weiteres
   Moment ist danach eine nicht nachjustierbare Gegenprobe. Das ist ein konkreter
   Prüfanschluss für eine Quelle, keine bereits berechnete TFPT-Quelldynamik.

## 1. Abgleich aller fünf Eingaben

Alle fünf Dokumente wurden vollständig gelesen; ihre Prüfsummen stehen in
`replay.json`. Quelltexte wurden gezielt geprüft. Es erfolgte kein Voll-Replay
aller in den fünf Berichten erwähnten Forschungsprogramme.

| Bericht | Tragend | Korrektur / Grenze |
|---|---|---|
| Sol | Nativer 16⊗4-Raum und SU4-Außenquadrat vermeiden zusätzliche Bänke. | Die Spiegelung muss nicht zwingend antiunitär sein: ein linearer SU4-Lift existiert ebenfalls. Interne Farben sind noch keine geometrisch abgeleiteten Orte. |
| Opus | Innere W-Spiegelungen und nativer μ4-Lift sind brauchbar. | Eine Auswahl unter vier benannten Bankplatzierungen ist kein Eindeutigkeitsbeweis unter allen kovarianten Kompositionen. Die rohe-Seam-Prämisse bleibt in v480 ausdrücklich offen. |
| Kimi 1 | Singulett- und Multiplizitätsanalysen; die ersten radialen Kopplungen 480 und 916. | Die Aussage, das globale N=64-Grundzustandsproblem sei im genannten kleinen Kopplungsfenster noch offen, berücksichtigt das stärkere bereits wiederholte Zertifikat nicht. Schwächere überlappende Schranken widerlegen dieses Zertifikat nicht. |
| Kimi 2 | Endliche C5/F20-Konstruktion und Ordnung-30-Vereinigung. | Der rohe Companion ist in der kanonischen CAR-Metrik nicht unitär. Der vorhandene Sechser-Clock wirkt auf den fünf Spin10-Slots, nicht auf dem A3-Familienfaktor. Ordnung 30 allein identifiziert keinen Coxeter-Lift. |
| Fable | Dieselbe konkrete C5-Idee; hilfreicher Fokus auf ursprüngliche Clock-Struktur. | Gleiche Darstellungs- und Dynamikgrenzen wie Kimi 2. Eine Gruppe mit 240 Elementen ist nicht dadurch die E8-Wurzelstruktur. |

Die diagonale Z4-Klebung ist außerdem von der alleinigen Teilchenzahl-Z4 zu
unterscheiden. Auf (16,4) wirken die Klebungsphasen als i·(−i)=1 und auf (10,6)
als (−1)·(−1)=1. Ein geladenes Feld ist nicht schon deshalb ein Bruch dieser
diagonalen Klebung. Ob ein ladungsübertragendes Instrument nativ ausführbar ist,
bleibt davon unabhängig.

## 2. Der C5-Ansatz ohne vier neue Bänke

In der Normalbasis (ζ,ζ²,ζ⁴,ζ³) ist das Getriebe P ein Viererzyklus und die
Multiplikation mit ζ eine reelle Matrix C mit PCP⁻¹=C². Der erhaltene positive
Gramoperator ist

    H5 = 5 I4 − 11ᵀ,

mit Eigenwerten 1,5,5,5. Mit P0=11ᵀ/4 und Z=P0+√5(I−P0) gilt Z²=H5.
Die Matrix U5=ZCZ⁻¹ ist orthogonal, determinant-eins und von Ordnung fünf.
Das ist eine echte Unitarisierung, nicht nur eine Umbenennung der alten Basis.
Eine Ortsinterpretation der alten Basis wird damit nicht automatisch erhalten.

Der binäre Gear ist R=exp(iπ/4)P. Er liegt in SU4, erfüllt R⁴=−I und
RU5R⁻¹=U5². Mit dem vorhandenen inneren G16 und dessen Vektorlift O10 gilt

    TF = G16 ⊗ U5                 (64 Dimensionen),
    TB = O10 ⊗ Λ²U5              (60 Dimensionen),
    W Λ²TF = TB W.

Die letzte Gleichung wurde auf allen 60×2016 Komponenten geprüft, getrennt in
den rationalen und den √5-Koeffizienten, ohne Rundungstoleranz. Beide Wirkungen
sind unitär; TF hat Ordnung 30 und I16⊗R konjugiert TF auf TF⁷.

Dies erhält den nativen Hamiltonoperator H=ΔNb+g(Q+ + Q−). Im bereits bewiesenen
Grundzustandsvertrag 0<|g|/Δ≤1/20 ist sein eindeutiger Spin10×SU4-Singulett-
Grundzustand deshalb auch unter diesen Gruppenelementen invariant. Der alte
Grundzustandsbeweis wird hier vorausgesetzt, nicht durch endliche Matrixchecks
neu bewiesen. Die Quelle hat diese konkrete C5-Einbettung noch nicht ausgewählt.

## 3. Zwei Spiegelrollen, nicht eine

Die arithmetische Konjugation Q=P² invertiert U5, kommutiert aber mit R.
Eine geometrische Spiegelung J0:e_j↦e_{−j} muss dagegen R invertieren.

Es existieren sowohl der antiunitäre Lift J0K als auch der lineare Lift

    J = diag(1,i,−1,−i) J0 ∈ SU4,
    J²=I,  JRJ=R⁻¹.

Eine allgemeine Schranke erklärt, weshalb die Rollen nicht identifiziert werden
dürfen: Sei C von Ordnung fünf und RCR⁻¹=C². Soll S zusätzlich R invertieren und
die gleiche C5-Untergruppe erhalten, also SCS⁻¹=Cᵘ mit u∈{1,2,3,4}, folgt aus
der konjugierten Relation

    C^(3u) = C^(2u).

Das widerspricht u≠0 modulo fünf. Die geometrische Spiegelung kann die C5-
Untergruppe auf eine andere C5-Untergruppe abbilden; das ist kein Widerspruch
der ganzen Theorie, sondern eine Grenze der behaupteten Identifikation.

## 4. Warum dieser 30er-Clock kein E8-Coxeter-Lift ist

Im vollständigen adjungierten Raum

    248 = 45 + 15 + 60 + 64 + 64bar

ergibt die exakte Charakter-Mittelung über TF folgende Fixraumdimensionen:

| Komponente | 45 | 15 | 60 | 64 | 64bar | Summe |
|---|---:|---:|---:|---:|---:|---:|
| Korrigierter nativer TF | 11 | 3 | 4 | 0 | 0 | 18 |

Zum Vergleich: Das Produkt der acht einfachen E8-Wurzelspiegelungen wurde auf
allen 240 Wurzeln konstruiert. Es hat acht Wurzelorbits der Länge 30 und keinen
Cartan-Fixvektor. Ein E8-Coxeter-Lift hat Ordnung 30; jede dieser Wurzelzyklen
liefert dann genau einen adjungierten Fixvektor, insgesamt acht. Der hier
verwendete Liftsatz ist Proposition 5.1.1 von
[Adams und He, Lifting of elements of Weyl groups](https://arxiv.org/pdf/1608.00510).
Dieser Literaturanschluss ist ein zusätzlicher mathematischer Satz, nicht bloß
ein Ergebnis des endlichen Checkers.

18≠8 schließt Konjugiertheit aus. Dies betrifft den konkret gebauten TF;
andere mögliche E8-Einbettungen werden dadurch nicht ausgeschlossen.

## 5. Der direkte Dynamikanschluss: zwei Momente bestimmen, eines widerlegt

Fixiere im nativen Modell F=|64 Fermionen besetzt; alle Bosonen leer>.
**F ist nicht der wechselwirkende Grundzustand.** Definiere die zentralen
Energiemomente m_n=〈F|(H−〈H〉)^n|F〉; hier ist 〈H〉=0. Sie sind zugleich die
kurzzeitigen Ableitungen der Rückkehramplitude A(t)=〈F|exp(−itH)|F〉, in einer
festen Zeitkonvention mit ℏ=1. Es geht um die komplexe Amplitude, nicht bloß um
die Rückkehrwahrscheinlichkeit, die das ungerade Moment nicht direkt enthält.

Eine unabhängige Berechnung der Fermionzeichen aus dem unveränderten W liefert

    ||Q+ F||² = 480,
    ||Q+² F||² = 439680 = 480·916.

Die zweite Stufe enthält 108240 besetzte Basiszustände. Bosonische Doppel-
besetzungen gehen mit ihrem korrekten Normfaktor zwei ein. Daraus folgen exakt

    m2 = 480 g²,
    m3 = 480 Δ g²,
    m4 = 480 Δ² g² + 670080 g⁴.

Für Δ>0 und g≠0 ist damit das inverse Problem IN DIESER MODELLKLASSE gelöst:

    Δ = m3/m2,
    |g| = √(m2/480),
    (g/Δ)² = m2³/(480 m3²).

Der letzte Ausdruck bleibt unter einer gemeinsamen Änderung der Zeiteinheit
unverändert. Das Vorzeichen von g ist durch Umphasung der Bosonen entfernbar.
Nach den ersten beiden Momenten bleibt für das vierte keine Freiheit:

    m4 = m3²/m2 + (349/120) m2².

Äquivalent in zentralen Kumulanten:

    κ4 = κ3²/κ2 − (11/120) κ2².

Die Konstanten 480 und 916 waren in der radialen Modellanalyse bereits bekannt;
neu ist hier ihre unabhängige direkte Reproduktion und die explizite Reduktion
auf einen inversen Quellenvergleich mit einer zurückgehaltenen Gegenprobe.

Das ist noch KEINE Herleitung von g/Δ aus TFPT. Dafür müssen dieselbe Präparation,
dieselben Feldoperationen und dieselbe Zeit auf der ursprünglichen Quelle
identifiziert und ihre Momente unabhängig berechnet werden. Zwei passende
Momente identifizieren Modellparameter, das vierte kann die Modellzuordnung
widerlegen; selbst vier passende Momente beweisen noch keine Gleichheit aller
Mehrzeitkorrelationen oder aller Feldantworten.

## 6. Ein strenger Grund, nicht noch eine Clock-Auswahl als Dynamik auszugeben

Alle oben genannten Symmetrien erhalten H für jedes Δ und g. Die beiden
Kopplungen g/Δ=1/40 und 1/20 liegen im abgesicherten Grundzustandsfenster und
besitzen dieselben Clock-/W-Symmetrien. Trotzdem ergeben sie in F

    m2/Δ² = 3/10 beziehungsweise 6/5.

Das ist eine vierfach verschiedene Antwort bei gleicher Symmetrie. Die
Grundzustände beider Modelle müssen dabei nicht derselbe Vektor sein; beide
erfüllen aber dieselbe gesicherte eindeutige Singulett-Klassifikation.

Eine zusätzliche direkte Setzung g/Δ=(2/3)^6 wäre auch numerisch nicht harmlos:
64/729>1/20 liegt außerhalb des hier bewiesenen Grundzustandsfensters. Eine Rate,
eine Amplitude und ein Hamilton-Kopplungsverhältnis sind nicht ohne Feld- und
Zeitwörterbuch gleichzusetzen. Daraus folgt kein Nichtexistenzsatz jenseits
dieses Fensters, sondern eine Grenze der verwendbaren Zertifikate.

## 7. Was als Nächstes wirklich entschieden werden muss

Der minimale nächste Quellenvergleich lautet nicht »noch mehr passende Zahlen«,
sondern: Ist F aus dem ursprünglichen Compiler mit festgelegten Feldern und
festgelegter Zeit präparierbar, und welche komplexe Rückkehramplitude erzeugt
derselbe Prozess? Dann m2 und m3 berechnen, Parameter identifizieren und m4
ohne Nachjustierung prüfen. Bei Widerspruch ist genau diese Modellzuordnung
verworfen. Bei Erfolg folgen geladene Mehrzeitantworten und erst danach eine
räumliche Skalierungsfrage. Ein stationärer Grundzustands-Rückkehrkern allein
wäre hierfür ungeeignet: seine zentralen Energiemomente verschwinden.

Die bisherige freie Vierintervall-Kovarianz legt keinen solchen physisch
identifizierten Anfangszustand plus Zeitkern fest. Auch eine modulare Zeit darf
nicht stillschweigend mit der Hamiltonzeit gleichgesetzt werden. Der direkte
Quellenvergleich bleibt deshalb offen; die inverse Modellseite ist nun explizit.

3+1D-Ursprung, chirales Maß, dynamischer Spin 2 und T1–T8 werden nicht geschlossen.

## Reproduktion und eigene Fehlerkontrolle

`replay.py` führt den neuen Clock-Prüfer, den neuen Moment-Prüfer und den
unveränderten fremden Carrier-Prüfer normal sowie mit Python -OO aus. Er hält
alle Eingabeprüfsummen vor/nach den Läufen fest und verlangt identische JSONs.
Die 26 Fremdprüfungen enthalten auch numerische Toleranztests, trotz des Labels
»exact_checks«. Ihre physikalische Prosa ist durch einen PASS nicht bewiesen.

Bei der Entwicklung des Momentprüfers scheiterte zunächst ein struktureller
Formelvergleich: (349 m2³/120+m3²)/m2 und 349 m2²/120+m3²/m2 wurden syntaktisch
statt algebraisch verglichen. Die systematische Fehlerprüfung isolierte die
Ursache; der Test verlangt jetzt exakt verschwindende Differenz. Die zugrunde
liegende Fockrechnung wurde nicht angepasst. Das ist eine Prüferkorrektur,
keine Änderung des mathematischen Resultats.
