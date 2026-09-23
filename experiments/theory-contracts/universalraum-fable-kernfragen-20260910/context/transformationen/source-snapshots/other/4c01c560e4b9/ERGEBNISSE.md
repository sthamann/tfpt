# Verschobene Dreifachechos: abgeschlossene genetische Vergleichssuche

9. September 2026. Die neue Familie verbessert in diesem frischen Test die
alte Dreifachfamilie von 10 auf 15 gelöste Zahlen. Ein Vorteil gegenüber
Zufallssuche, der stärkeren reziproken Kontrolle oder klassischen Verfahren
ist nicht belegt. Kein Faktorierungsdurchbruch und kein Rekordtest.

## Was tatsächlich neu umgesetzt wurde

Aus den neuesten TOE-Ergebnissen zu relativen Wartezeiten entstand die
modulare Familie W(a₁t+b₁)W(a₂t+b₂)W(a₃t+b₃). Die drei additiven
Verschiebungen waren in ad nicht enthalten. Ein exakter Compiler erzeugt
die Spur- und Charakteristikdaten vom Grad höchstens 24. Die Faktoren der
Zielzahlen sind weder Compiler- noch Solver-Eingaben.

Der bewiesene Permutationsquotient reduziert 2730 geordnete Genome auf 455
Tripel mit verschiedenen Geraden; siehe MATHEMATIK.md. Diese gezielte
Entdoppelung verhindert die sechsfache Bewertung derselben drei ggT-Leser.
Weitere mögliche Äquivalenzen bleiben offen. Die algebraischen Operationen
sind keine abgeleitete physikalische Implementierung aus TFPT.

## Auswahl vor Erzeugung der Prüfdaten

Der vollständige Vorabplan steht in PROTOKOLL.md. Auf 16 neuen balancierten
Semiprimen mit 24, 32, 40 und 48 Bit bewerteten ein genetischer und ein
zufälliger Arm jeweils 32 verschiedene Kandidaten. Beide hatten denselben
Kontrollkandidaten als zusätzliche Rückfalloption. Durch gemeinsame Kandidaten
und Cache wurden insgesamt 61 verschiedene Familien tatsächlich berechnet.

Jede Kandidaten-Zahl-Kombination erhielt höchstens 32.768 modulare Produkte.
Die vorher festgelegte Fitness bevorzugte Erfolge ab 40 Bit, danach gewichtete
Gesamterfolge und schließlich niedrigere Gesamtkosten inklusive Fehlschlägen.
Der genetische Arm verwendete acht Anfangsgenome und drei Generationen mit
je acht neuen Ein-Geraden-Mutationen. Der Zufallsarm zog ohne Zurücklegen.

Genetischer Sieger: **W(t−3)W(2t+3)W(3t+1)**.
Zufallssieger: **W(t+3)W(2t+3)W(3t)**.
Beide erzielten 6 von 16 Trainingserfolgen. Die maximalen ganzzahligen
Koeffizientenlängen betragen 225 beziehungsweise 215 Bit. Auswahl, Quellen
und Koeffizienten wurden eingefroren, bevor die 48 Prüfeingaben entstanden.

Die eigentliche Suche kostete 25.058.345 modulare Produkte. Die Summe der
gemessenen statischen Kompilationszeiten beträgt 13,526 Sekunden; der ganze
Suchlauf diagnostisch 23,411 Sekunden. Die logischen Armkosten liegen bei
13.040.698 und 13.278.083 Produkten; gemeinsam gecachte Bewertungen dürfen
nicht zusätzlich als tatsächlich wiederholte Arbeit gezählt werden.

## Frischer Vergleich

48 weitere balancierte Semiprime, je acht mit genau 24, 32, 40, 48, 56 und
64 Bit. Gleiche Zahlen für alle sieben Verfahren, pro Lauf höchstens 65.536
modulare Produkte. Gemeinsamer öffentlicher Parameterstrom für die drei
Dreifachfamilien und die reziproke Kontrolle; getrennte Faktorprüfdatei.
Die Trennung ist funktional, keine behauptete Betriebssystem-Isolation.

| Verfahren | Erfolge / 48 | Erfolge nach Bitzahl 24/32/40/48/56/64 | Produkte über alle 48 Läufe |
|---|---:|---|---:|
| Genetischer Sieger | 15 | 8 / 6 / 1 / 0 / 0 / 0 | 2.449.898 |
| Zufallssieger | 14 | 6 / 7 / 1 / 0 / 0 / 0 | 2.475.103 |
| Alte Dreifachfamilie | 10 | 6 / 3 / 1 / 0 / 0 / 0 | 2.605.282 |
| Reziproke Kollision | 17 | 8 / 6 / 3 / 0 / 0 / 0 | 2.076.931 |
| p−1 | 13 | 6 / 5 / 1 / 0 / 1 / 0 | 2.340.478 |
| Lucas | 17 | 8 / 7 / 1 / 1 / 0 / 0 | 2.043.344 |
| Brent | 40 | 8 / 8 / 8 / 8 / 6 / 2 | 857.376 |

Primärer vorab festgelegter Vergleich: Genetik gegen reziproke Kontrolle.
14 gemeinsame Erfolge, ein Erfolg nur genetisch, drei nur reziprok,
30 gemeinsame Fehlschläge; exakter zweiseitiger gepaarter Test p=0,625.
Ein Gesamtvorteil der neuen Familie ist damit nicht gezeigt.

Explorativ gegen die alte Dreifachfamilie: fünf zusätzliche Erfolge und kein
verlorener Erfolg, p=0,0625. Gegen Zufall: zwei zusätzliche, ein verlorener
Erfolg, p=1. Diese Daten belegen weder eine verlässliche Überlegenheit der
genetischen Suche noch eine allgemeine Erfolgssteigerung durch Verschiebungen.

Alle 15 Erfolge des genetischen Siegers werden auch von Lucas und Brent
gelöst. Keine der drei Dreifachfamilien löst in diesem Budget einen Fall
mit mindestens 48 Bit. Die ausgeführten Arithmetikkontrollen bis 257 Bit
sind keine Faktorisierungen in dieser Größe. ECM/GNFS wurden hier nicht
verglichen; aus dem kleinen Test folgt keine Rekordnähe.

Der einzige gegenüber dem reziproken Leser zusätzliche genetische Fall ist
2149038103=42961×50023: Genetik benötigt 9799 Produkte, Zufall 30460, die alte
Dreifachfamilie 22068, Lucas 5104 und Brent 637. Dieser Fall ist somit weder
neu gegenüber der alten Dreifachfamilie noch ein klassischer Kostenvorteil.

## Verifikation und Kostenreichweite

Alle 126 ausgegebenen nichttrivialen Faktoren des Holdouts sind geprüft.
Für die drei Dreifachfamilien wurden 144 volle Gaußmatrix-Zeugen unabhängig
von der produktiven quartischen Rekursion nachgerechnet; weitere 96
Begleitmatrix-Zeugen betreffen die reziproke Kontrolle und Lucas. Dazu kommen
18.407 unabhängige skalare Potenzen, 33.983 Kosten-/ggT-Stufen und die
Gesamtproduktabrechnungen. Bei allen 39 erfolgreichen Dreifachläufen ist die
anfängliche Diskriminante zu N teilerfremd.

Der Trainingsprüfer bestätigt alle 976 Kandidatenläufe, 325 ausgegebenen
Trainingsfaktoren, 5836 Stufen, die Fitness und beide Siegerentscheidungen.
Für jede der 61 unterschiedlichen Familien wurde zudem die kompilierte
Charakteristik an einem festen Kontrollpunkt aus der vollen Quelle überprüft.
Hashes belegen die eingefrorenen Quellen und Populationen. Rohdaten und
Prüfprogramme liegen unverändert neben diesem Bericht.

Die gezählten modularen Produkte enthalten die N-abhängige Vorbereitung,
Gaußarithmetik und Auslese. ggT, Inversionen und Additionen sind zusätzlich
erfasst; Produkte allein sind kein vollständiges Bitkosten- oder CPU-Modell.
Statische Initialisierung und Such-/Kompilationskosten müssen in einer
End-to-End-Behauptung hinzugerechnet werden. Brent-Faktoren und aufgezeichnete
Kosten wurden geprüft, aber nicht jede innere Brent-Operation unabhängig
repliziert. Die zufällige Suche wurde nicht als zweite Replikation neu gezogen.

## Neue Arbeitsgrenze

Die aus den aktuellen Quellen abgeleitete Verschiebungsidee ist damit als
kleine, testbare Familie umgesetzt. Der Quotient verbessert die Suchorganisation,
doch der Holdout liefert keinen neuen Leistungsmechanismus gegenüber Lucas.
Für alle übrigen Geometrien wird daraus kein Unmöglichkeitssatz abgeleitet.

Die nächste prüfbare Voraussetzung bleibt ein **billiger N-only-Selektor**:
Er muss ohne Faktoren oder nachträglich bekannte Eigenwertordnungen Parameter
bevorzugen, deren relative Kollision modulo einem unbekannten Faktor früh,
modulo dem anderen spät auftritt. Die Selektionskosten müssen sich im
frischen Gesamtvergleich auszahlen. Eine weitere Mutation derselben Familie
ist erst dann ein stärkerer Ansatz, wenn sie dafür ein messbares Signal nutzt.

Eine alternative strukturelle Suchrichtung sind integral erhaltene
Torsionsdaten, die der rationale RH-Rückvergleich verliert. Vor einer neuen
Kampagne braucht sie eine konkrete, aus N konstruierbare Präsentation und
eine Auslese unterhalb der Kosten einer gewöhnlichen Ordnungs-/ggT-Suche.
Ein abstraktes Torus-, Galois- oder Energieerhaltungsargument allein liefert
diese Abkürzung noch nicht. Der genaue Quellenabgleich steht in
QUELLENABGLEICH.md; die aktuellen Ergebnisse ersetzen keine früheren Belege.
