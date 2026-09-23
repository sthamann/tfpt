# TFPT / Universalraum v1.6: integrierte Revision vom 15. September 2026

## Ergebnis

Die markierte maximale Matrixordnung trägt tatsächlich E8. Dieser Beweis lag
bereits seit dem 9. September im Repository und wurde im letzten Status
übersehen. Er wurde jetzt einschließlich Compiler-Abbildung und Clockgrenze
reproduziert. Neu gerechnet sind die inneren Weyl-Walk-Koeffizienten aus
denselben Matrizen sowie eine unabhängige Voll-Fock-Casimir- und Zustandsprüfung.

Das vollständige Hauptbuch v1.5 wird nicht ersetzt oder gekürzt. v1.6 bewahrt
alle 25 Kapiteldateien mit sämtlichen bisherigen Abschnitten und Bildern,
verwebt 13 kontextbezogene Ergänzungen und ergänzt fünf Hauptkapitel plus
Evidenzanhang. Ein separates kurzes Update berichtet nur Änderungen gegenüber
dem PDF v1.5. Die vorläufigen gleich nummerierten Markdown-Texte vom 14.
September werden als Quellen integriert und bleiben unverändert.

## Frische Nachweise

### 1. Markierte Matrixordnung

Mit D=Z[i], P=[[1,1/(1+i)],[0,1/(1+i)]] und M=P M2(D) P^-1 ist
Q(A)=Re Tr_2(A A†) ein positives gerades unimodulares Rang-8-Gitter.
Alle 240 Norm-2-Vektoren sind vollständig erfasst: Diag(G^-1)=2 begrenzt
ihre ganzzahligen Koordinaten auf [-2,2]. 96 sind unitär, 144 haben Rang eins.
Die markierte Isometrie zum tatsächlichen Compiler erhält Anker, komplexe
Struktur und Familienwirkung. Das ist ein vorhandener, jetzt wiederholter
Beweis, keine neue Entdeckung und keine unabhängige physische Herkunft.

Die drei Ordnungen O⊂R⊂M haben additive Indizes 4 und 4 und Gramdeterminanten
256,16,1. Ihre gleiche hermitesche Kegelansicht entscheidet nicht, welche
Operationen ausgeführt werden. q=diag(i,1) gehört zu M, nicht R. Seine native
Bereitstellung ist eine konkrete offene Auswahlfrage.

### 2. Innere Weyl-Amplituden aus dem Compiler

Für die originalen Pauli-Matrizen α_j=-a u_j gilt

    A_ε=(I+ε1 α1)(I+ε2 α2)(I+ε3 α3)/8,
    U(k)=Π_j exp(-i kj αj)=Σ_ε exp(-i ε·k) A_ε.

Alle acht Koeffizienten haben Rang 1 und Q=1/4. Der minimale positive ganze
Faktor in M ist jeweils 4. Beide Laurent-Unitaritätsgleichungen sind für alle
27 Exponenten geprüft. Der lineare Term ist das Weyl-Symbol.

**Ohne Ortsverschiebungen gilt Σ A_ε=I.** Physische Bewegung wird damit noch
nicht aus dem Compiler erzeugt. Auch lineare Kombination, Viertelnormierung,
gerichtete Kontrolle und Hilfsregister müssen als Operationen realisiert sein.

### 3. Voll-Fock-Casimiridentität und Zustandsgegenprobe

Der Tensor W wird unabhängig aus Außenalgebra-Vorzeichen rekonstruiert und
gegen einen SHA-256-gepinnten 60×2016-Tensor geprüft. Die Generatoren von
Spin(10) und SU(4) werden auf alle 2016 Zweifermionenzustände gehoben. Exakt:

    8 W†W + 4 C_Spin10 + 4 C_SU4 - 120 I = 0,
    A=Σ P_A†P_A=(15 Nf - C_Spin10 - C_SU4)/2 ≤ (15/2)Nf.

Die Zwischenkomponenten sind gaußsche ganze Zahlen, größte Magnitude 120.
Wegen normalgeordnetem Grad ≤4 und Prüfung der Sektoren 0,1,2 gilt die
Identität auf dem gesamten fermionischen Fockraum.

Für H=ΔNb+gΣ(b†P+P†b), N=Nf+2Nb und Hμ=H+μN folgt

    Hμ ≥ (μ - 15g²/(2Δ)) Nf + 2μ Nb.

Bei g=Δ/20 und μ=Δ/50 ergibt das Hμ≥ΔN/800. Das leere Vakuum ist der
eindeutige Grundzustand mit Anregungsuntergrenze Δ/800. Bei μ=0 hat bereits
der helle Einpaarsektor E_-=(Δ-sqrt(Δ²+32g²))/2<0. Dieser Gegenvergleich
braucht den gemeldeten großen N=64-Grundzustandsbeweis nicht.

Für [O,N]=0 und denselben präparierten Eingang sind die Heisenbergentwicklungen
unter H und Hμ gleich. Grundzustandspräparation und Ladungswechsel können
unterscheiden. Symmetrie und neutrale Antworten wählen das Vakuum daher nicht
allein. Innerhalb eines fest vorgegebenen N-Sektors ist μN nur eine Konstante;
dieser Vertrag darf nicht mit globaler Grundzustandswahl verwechselt werden.

### 4. Physische Statistik und Transportgrenze

Alle 60 hellen Paarzustände haben acht disjunkte Paare auf 16 Moden. Passende
Vierpunktdaten ergeben 1/8 statt des Wick-Wertes 1/64 bei gleichen Zweipunktdaten.
Der Defekt 7/64 ist exakt. Die Zustände sind nicht gaußsch in diesen Moden;
eine nichtlineare Randfeldübersetzung bleibt möglich, ist aber zusätzlich.

Reines Vermittlerhopping zwischen Banken erhält jede lokale Fermionparität.
Einzelne Fermionen können dadurch nicht die Bank wechseln. Das ist eine
algebraische Schranke für diesen Hamiltonvertrag, nicht für alle denkbaren
Quellrealisierungen. Zusätzliche f†_x f_y-Terme sind neue Dynamik und nicht
aus ausschließlich lokal geraden Operationen ableitbar.

## Übernommene, nicht sämtlich frisch wiederholte größere Vorbefunde

- Ein-Record-Präparation P^-03 ξ=-sqrt(3/8)Ω; genaue ξ-Schaltung; destruktive
  Endprüfung mit Effekt (3/8)PΩ; Vier-Record-Rohwerte 9/64 und 153/2048.
- Stabilizeroptimum 3/8 und vollständiger Flagzeuge 15/64; alte Filterfolge
  bleibt korrekt, ist für diesen Eingang aber nicht mehr nötig.
- Vollständiger 24024D-Singulettsektor des kantenlokalen H_tr=H0+F4/800:
  genau fünf Zustände unter 12.45J, Lücke >0.4864141269280J. Keine Schließung
  aller Nicht-Singuletts oder des vollen mikroskopischen Operators.
- Positiver 112D-Dreiplatz-Wedge-Transport und 961D-Zweistern-Kompression;
  ausdrücklich verschiedene Modellverträge, kein bereits gemeinsamer Ursprung.
- Vollständige Fehlversuchs- und Robustheitsrechnung der benannten Ausführung.
- Gemeinsamer Inflationsvergleich M²=c3^7: Amplitude und Neigung treffen die
  gewählten Zentralwerte nicht bei demselben N; Retuning von c3 betrifft auch
  die elektromagnetische Ausgabe. Keine neue vollständige Likelihoodanalyse.
- Große native Grundzustands- und Vierladungsrechnungen der Worker-Eingabe
  bleiben zugeschriebene Quellenresultate, nicht global neu zertifiziert.

## Offene Fronten und nächste Reihenfolge

1. **Natives Operationswort mit echtem Platzwechsel.** Innere Grade,
   Normierung, Hilfsregister und geschlossene Wegprodukte gemeinsam prüfen.
2. **Energie und Zustand desselben Systems auswählen.** μN-Freiheit am
   tatsächlich erlaubten Präparations- und Sektorvertrag entscheiden.
3. **Unverändert skalieren.** Erst dann gemeinsame Ausbreitung, Kegel,
   chiraler Index, Grenzwert und ein eigener dynamischer Spin-2-Nachweis.

T1: Quellen-/Dimensionsauswahl; T2: renormiertes Half-Charge-Feld; T3:
gemeinsamer lokaler 3+1D-Ursprung; T4: chirales Maß; T5: wechselwirkender
Grenzwert; T6: vollständige Eichkopplungs-/Neutrinoauswahl; T7: dynamischer
masseloser Spin 2; T8: physisches Zustands-/Quellfunktional. **Keines der acht
Tore ist vollständig geschlossen.** Keine neue RH-, Faktorisierungs- oder
P-versus-NP-Lösung und keine abgeleitete Hylæan-Fähigkeit.

## Prüf- und Lieferumfang

Fünf Programme normal und unter -OO, jeweils bytegleiche JSON-Ausgaben.
Neuer Prüfer: 279 Guards. Vorhandene native/Weyl/Kompatibilitätsprüfer:
534/149/7369 Guards. Zahlen messen Prüfbedingungen, nicht Entdeckungen.
Der Matrixprüfer enthält Quellenpins und den markierten Clockvergleich.

Dateien: verify_v16.py, new_checks.json, replay.py, replay_manifest.json,
order.json, native.json, weyl.json, compatibility.json, sources.json,
main-v1.6/ und release_manifest.json. Die Replay-Ausführung benötigt den
angegebenen lokalen Repository- und Quellenkontext. Das Paket archiviert
die Eingaben und Prüfskripte, behauptet aber keine vollständige portable
Installation sämtlicher historischen wissenschaftlichen Abhängigkeiten.

Die vollständigen PDF-Quellen sind im Paket enthalten. Vor der Auslieferung
werden alle Seiten gerendert, die neuen Beweis-/Tabellenseiten gezielt geprüft
und sämtliche ursprünglichen Kapiteltexte und Abbildungen auf Erhalt getestet.
