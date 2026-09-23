# Vorwärtstest: Auswahl aus primitiven Compileroperationen

12. September 2026. Bounded research, keine Paper-/Ledger-Promotion.
Checkout HEAD bei Beginn: `66b91e40e245569f06ab440ead80f446c9be0ee5`;
gemeinsamer Arbeitsbaum mit zahlreichen vorhandenen Fremdänderungen.

## Ergebnis und Herkunft

Zwei konkrete Versuche, Gewichte beziehungsweise Zustand ohne Zielkopplungen
zu gewinnen, scheitern bereits algebraisch. Das ist kein Ausschluss einer
vollständigen TFPT-Quelle und keine Herleitung von H70. Der Code verwendet
keine H70-Kopplungen und benötigt keinen aus H70 erzeugten Zustand.

Gelesene lokale Quellen:

- `origin_theory.tex`, Zeilen 87–102: P1/P2, vier Marken, Riemann–Roch-
  Trägerraum; der Text trennt Arithmetik und physische Identifikation.
- `../compiler-cone-object-audit/ORDER_PROOF.md`, Abschnitte 1 und 3:
  konkrete zweidimensionale Darstellung des rationalen Ankerkommutanten.
- Die vier aktuellen ChatGPT-Berichte wurden in der vorherigen Runde
  verglichen; der jüngste Gesamtbildbericht wurde erneut eingesehen.
  Deren Zertifikatpakete werden hier nicht als unabhängig erneut geprüft
  ausgegeben. Die unten verwendeten Quellmatrizen werden exakt nachgerechnet.

Die Darstellung ist ein vorhandener Teil der Quelle, nicht der vollständige
Vielteilchenraum. Die Auswahlregel Q ist eine neu deklarierte Hypothese,
keine bereits aus P1/P2 bewiesene Vorschrift.

## 1. Tatsächliche Quaternionoperationen: perfekte Einfachheit ist hier trivial

In der dokumentierten Darstellung gilt

    u1 = diag(i,-i), u2 = [[0,1],[-1,0]], u3 = u1 u2,
    w = (I+u1+u2+u3)/2, w^3 = -I.

Teste die einfache positive Vergleichsform

    Q = sum_a alpha_a (I-U_a)^* (I-U_a), alpha_a > 0.

Da uj*=-uj und uj*uj=I, ist jeder Quaternionbeitrag exakt 2I.
Da w+w*=I und w*w=I, ist sein Beitrag I. Deshalb

    Q = [2(alpha_1+alpha_2+alpha_3)+alpha_w] I.

**Keine Wahl dieser positiven Gewichte selektiert in diesem Zweierblock
einen Zustand oder relative Energien.** Bei gleichen Gewichten ergibt sich
7I. T=exp(-tau Q) ist skalar; nach Normierung durch seinen größten Eigenwert
ist T/λ0=I und der zurückgelesene Generator null. Die Voraussetzung eines
einfachen größten Transfer-Eigenwerts ist gerade nicht erfüllt.

Allgemeiner ist für jede Einheitsquaternion U in ihrer SU(2)-Darstellung
U+U*=2 Re(U) I. Daher bleiben Defekte relativ zu +I oder -I skalar.
Das ist klassische Matrixalgebra, kein beanspruchter neuer allgemeiner Satz.

Nichtreelle Vergleichsphasen ändern die Situation. Beispielsweise

    (u1-iI)^*(u1-iI) = diag(0,4).

Damit wird eine Zustandsrichtung gewählt. Aber dieselbe Phase bei u2 wählt
eine andere Richtung: Die Projektorüberlappung ist 1/2. Das Vorhandensein
von i in μ4 entscheidet noch nicht, welchem Prozess welcher Charakter
zuzuordnen ist. Eine solche Zuordnung könnte aus umfassenderen markierten
TFPT-Daten folgen; das wurde hier weder bewiesen noch ausgeschlossen.

Wer u1 und u2 dagegen beide als vollständig zu erhaltende Symmetrien des
Transfers behandelt, erzwingt [T,u1]=[T,u2]=0 und somit T=cI. Der exakte
Kommutatorrang beträgt 3 auf dem vierdimensionalen Matrixraum. Die Rollen
„physische Operation“ und „Symmetrie des Zustands/Transfers“ dürfen daher
nicht ohne Herkunftsnachweis gleichgesetzt werden.

## 2. Kann eine kanonische Gram-Normierung die Gewichte ersetzen?

Ein zweiter Versuch beginnt mit einer gestapelten Defektabbildung d und
ersetzt die freie Metrik auf ihren Antworten durch die Moore–Penrose-Inverse:

    Q_can = d* (d d*)^+ d.

Für jedes endlichdimensionale d ist exakt

    Q_can = P_(ker d)^perp.

Beweis: Schreibe eine Singulärwertzerlegung d=UΣV*. Jeder nichtverschwindende
Singulärwert trägt σ·σ^(-2)·σ=1 bei; Nullwerte bleiben null. Somit werden
alle Stärkenunterschiede entfernt. Das Ergebnis hängt nur vom Kern ab.

Folgen:

- Bei injektivem d wird Q_can=I: keinerlei Zustandsauswahl.
- Bei eindimensionalem Kern wird dessen Zustand ausgewählt, aber sämtliche
  orthogonalen Anregungen haben dieselbe Energie.
- Eine nichttriviale Energielandschaft folgt daraus nicht allgemein.

Als unabhängiger Kontrollbaukasten werden C=diag(1,i) und X=σx verwendet.
Diese beiden Matrizen werden NICHT mit den ursprünglichen Quaternion-
Generatoren identifiziert. Hier ist

    d = stack(I-C, I-X), d*d = [[2,-2],[-2,4]],

mit Eigenwerten 3±sqrt(5): positiver, eindeutiger Grundzustand.
Die kanonische Gram-Normierung verwandelt genau diese Form in I.
Das zusätzliche Aufschreiben des C-Defekts verändert die rohe Form zu
[[2,-2],[-2,6]], die normierte bleibt I.

Diese Redundanzforderung gilt, wenn die zusätzliche Zeile bloß eine weitere
Beschreibung desselben Vergleichs ist. Ist sie ein eigenständiges physisches
Ereignis, darf sie Gewicht tragen; dann muss die Quelle dies unterscheiden.

Eine Regularisierung repariert die Spektralentartung nicht kostenlos:

    d*(dd*+lambda I)^(-1)d = Q(Q+lambda I)^(-1), Q=d*d.

Für lambda>0 ist die Spektralfunktion streng monoton. Sie erhält den
Grundzustand des gegebenen Q, liefert aber weder dessen Herkunft noch den
Wert von lambda; die Invarianz unter redundanter Umgewichtung geht verloren.

Die verwandte kanonische Parseval-Normierung ist bekannte Rahmentheorie,
kein neu identifiziertes Universalobjekt. Literaturkontext:
https://arxiv.org/abs/1705.03437 ; der benötigte endliche Satz ist oben
vollständig bewiesen und nicht von diesem Literaturhinweis abhängig.

## Konsequenz und nächste überprüfbare Frage

Der vollständige Vorwärtsversuch bleibt offen: Eine unabhängig abgeleitete
primitive Maß-/Charaktervorschrift für das Vielteilchenmodell liegt hier
nicht vor. Die zwei Rechnungen begrenzen konkrete Kandidaten, nicht P1/P2.

Der nächste fokussierte Test ist die HERKUNFT einer nichtreellen
Charakterzuordnung: Liefert der markierte Seam samt Spinlift eine eindeutige
Zuordnung U_a -> chi_a, welche die Kompositionsrelationen respektiert?
Eine willkürliche Wahl von chi=i für einen bevorzugten Generator zählt nicht.
Soll chi ein eindimensionaler Charakter der ganzen Quaterniongruppe sein,
gilt zusätzlich chi(-I)=1, da -I ihr Kommutator ist; die spinorielle Wirkung
von -I als -I ist damit nicht durch einen solchen Charakter darstellbar.
Charakter einer Untergruppe und volle spinorielle Darstellung sind getrennte
Möglichkeiten und benötigen eigene, explizite Herkunftsregeln.

Abnahme: Zuerst die zulässigen markierten Daten und Abbildungsregeln
festlegen, erst danach Q/T und seinen ausgewählten Zustand berechnen.
Ein Anschluss an H70 erfordert zusätzlich eine konstruierte Abbildung auf
dessen Zustände und Operatoren. Keine Gleichsetzung unterschiedlicher Räume.

## Reproduktion

`python3 -B check.py` und `python3 -B -OO check.py` führen dieselben exakten
Kontrollen aus. Explizite Fehlerprüfungen statt abschaltbarer assert-Befehle.
Der JSON-Ausdruck enthält den Hash der verwendeten lokalen Quellnotiz und
die weiterhin offenen Herkunfts-/Rekonstruktionsfelder. Die Kontrollliste
ist eine endliche Rechenprüfung; der allgemeine Satz steht ausgeschrieben oben.

Ausgeführt: beide Modi erfolgreich, je 32 exakte Kontrollen; JSON-Ausgaben
im nachfolgenden Vergleich byteidentisch. Verwendeter Quellnotiz-Hash:
`ecece533f22c32b0109ca5ba1c02e98862e3f3821ba4b5a5792442b11c45b085`.
