# Entscheidung über die direkte Quellenbrücke: ein Paritätswiderspruch am Grundzustand

15. September 2026 · NON-RH-Forschungsresultat · keine Ledger-/Paper-Beförderung

## 1. Die beantwortete Frage

**Nein: Das vorhandene native Wechselwirkungsmodell ist nicht durch eine
lineare oder Bogoliubov-artige Feldzuordnung mit dem freien gaußschen
Seam-Modell identifizierbar, wenn dieselbe Zuordnung auch den Zustand erhält.**
Der Widerspruch gilt bereits am abgesicherten nativen Grundzustand. Er ist
keine offene numerische Toleranz und benötigt keine räumliche Skalierung.

Am Prüfpunkt g/Δ=1/20 ist die Wahrscheinlichkeit einer ungeraden Fermionzahl

    im nativen Grundzustand:                         exakt 0,
    im Gaußzustand mit derselben vollen Kovarianz:   strikt größer als 47,684946 %.

Das bedeutet nicht, dass jede denkbare Quelle gaußsch ist oder dass TFPT
widerlegt wäre. Ausgeschlossen ist die direkte Identifikation mit der freien
Seam unter gaußschen/linearen Feldoperationen. Nichtlineare Feldwörterbücher,
Erweiterungen der Feldalgebra und nichtgaußsche Quelloperationen sind andere,
hierdurch nicht ausgeschlossene Forschungswege.

## 2. Exakte Voraussetzungen

Wir verwenden unverändert

    H = Δ Nb + g Σ_A (b_A† P_A + P_A† b_A),
    P_A = Σ_(i<j) W_Aij f_j f_i,
    N = Nf + 2 Nb,

mit 64 CAR-Moden, 60 CCR-Moden, Δ>0, g/Δ=1/20 und ohne μN-Term. W ist die
gehashte Originaldatei, hat Rang 60 und WW†=8I. Der bereits konstruierte
Grundzustandssatz liefert ein eindeutiges Ω mit N=64; Ω ist ein
Spin10×SU4-Singulett. Seine volle Wellenfunktion wird dafür nicht benötigt.

Das rationale Grundzustandszertifikat wurde in diesem Lauf normal und mit
Python -OO erneut ausgeführt. Die höheren Momenttabellen stammen aus dem
früher bereits unabhängig geprüften Archiv; sie wurden hier unverändert
eingefroren, nicht vollständig neu enumeriert. Der neue Prüfer wiederholt
zusätzlich die vollständige Zwei-Fermionen-Casimiridentität am Original-W.

Die im Folgenden verwendeten Grundzustandsschranken sind bereits im älteren
Prüfarchiv vorhanden. Neu ist die daraus folgende quantitative Entscheidung
der Gauß-Quellenfrage und die Prüfung der einfachsten Paritätsreparatur.

## 3. Beweis I: Ein einziges Bit unterscheidet die Zustände

### 3.1 Die native Parität ist exakt fest

Aus N=64 folgt auf dem gesamten Grundzustandsvektor

    Nf = 64 − 2 Nb.

Damit hat auch die auf die Fermionen reduzierte Dichtematrix ρF ausschließlich
gerade Fermionzahl. Für den ungeraden Projektor Πodd gilt

    tr(ρF Πodd)=0,             tr(ρF (−1)^Nf)=1.

Das ist eine Aussage über die Fermionen dieses nativen Modells, nicht über
eine beliebige räumliche Teilregion der freien Seam.

### 3.2 Die Zweipunktdaten sind trotzdem nicht die eines leeren/vollen Zustands

Die Einteilchendarstellung V=(16,4) ist irreduzibel. Singulettinvarianz und
Schurs Lemma ergeben

    〈f_i† f_j〉 = ν δij.

Die anomalischen Zweipunktdaten 〈f_i f_j〉 verschwinden, weil diese Operation
die feste Gesamtladung um zwei verändert. Mit x=〈Nb〉 gilt ν=1−x/32.

Zur Schranke für x: Aus der ganzen Fock-Casimiridentität folgt

    A=Σ_A P_A†P_A ≤ (15/2)Nf.

Cauchy–Schwarz liefert daher bei g/Δ=1/20

    E/Δ ≥ x − (1/10)√[x(480−15x)].

Die vorhandene fünfstufige Variationsrechnung beweist E/Δ<−9/8. Somit

    (x+9/8)² − x(480−15x)/100 < 0.

Der linke Ausdruck faktorisiert exakt zu

    (4x−3)(92x−135)/320.

Also 3/4<x<135/92 und entsprechend

    2809/2944 < ν < 125/128.

### 3.3 Die gaußsche Referenz macht eine andere eindeutige Vorhersage

Eine fermionische Gaußdichtematrix ist durch die volle Zweipunktkovarianz
bestimmt. Für C=νI und verschwindende anomalische Kovarianz ist sie das
Produkt identischer Einzelmodenzustände:

    γν = ⊗_(i=1)^64 [(1−ν)|0〉〈0| + ν|1〉〈1|].

Daher

    tr(γν (−1)^Nf) = (1−2ν)^64 = (1−x/16)^64,
    tr(γν Πodd) = [1−(1−x/16)^64]/2
                > [1−(61/64)^64]/2
                = 0,476849460831080977… .

Die Produktform und Gauß-Erhaltung durch lineare fermionische Operationen sind
Standardresultate; siehe [Bravyi, Lagrangian representation for fermionic
linear optics](https://arxiv.org/pdf/quant-ph/0404180) und
[Surace–Tagliacozzo, Fermionic Gaussian states](https://arxiv.org/pdf/2111.08343).

Ein einzelnes Ereignis unterscheidet somit die Zustände. Mit der Konvention
D(ρ,σ)=½||ρ−σ||₁ gilt

    D(ρF,γν) > [1−(61/64)^64]/2 > 0,47684946.

**Wichtige Reichweite:** Diese quantitative Schranke gilt für die Gaußreferenz
mit denselben vollständigen Zweipunktdaten, nicht pauschal für die nächste
beliebige Gaußdichtematrix. Die Nicht-Gaußheit von ρF selbst ist dagegen exakt
und basisunabhängig. Sie bleibt auch unter Bogoliubov-Basiswechseln bestehen.

### 3.4 Konsequenz für die Quelle

Die Einschränkung eines gaußschen Zustands auf linear eingebettete CAR-Moden
ist wieder gaußsch. Gaußsche Hilfszustände und gaußerhaltende Kanäle ändern
daran nichts. Sie können ρF deshalb nicht exakt erzeugen. Beliebige Mischungen,
nichtgaußsche Messungen oder nichtlineare Feldabbildungen sind ausdrücklich
nicht von dieser Erhaltungsaussage erfasst.

Der freie Vergleich in `v480_multilocal_four_interval.py` wird aus einer
Zweipunktmatrix konstruiert; seine modulare Entwicklung ist quadratisch.
Die zugehörige freie Mehrintervalltheorie ist die von
[Casini–Huerta](https://arxiv.org/pdf/0903.5284). Ein linearer Feldadapter und
ein passender Clock reichen daher nicht, um den nativen Zustand zu liefern.

## 4. Beweis II: Nur »gerade auswählen« repariert die Quelle ebenfalls nicht

Eine naheliegende minimalistische Reparatur wäre, γν auf gerade Fermionzahl
oder auf bestimmte Zahlen zu projizieren. Dadurch wird die erste Paritäts-
Gegenprobe zwar beseitigt. Die folgende Aussage schließt diese Reparatur als
alleinige Lösung aus.

Jeder ausschließlich von Nf abhängige Zustand ist in jedem Zahlsektor ein
Vielfaches der Identität. Das gilt insbesondere für die symmetrische
Gaußreferenz nach beliebiger Paritäts-/Zahlprojektion und für Mischungen solcher
Projektionen. Es gilt nicht automatisch für beliebige projizierte BCS-Zustände,
kompositfeldabhängige Projektionen oder Erweiterungen der Feldalgebra.

Der Sektor mit zwei Fermionlöchern hat Dimension C(64,2)=2016. Die ursprüngliche
Paarquelle wählt darin nur einen 60-dimensionalen hellen Raum. Mit den aus
f_j f_i|F64〉 stammenden Vorzeichen Dholes ist sein Projektor

    Πhell = Dholes W†W Dholes /8.

Für jeden zahlabhängigen Referenzzustand γnum gilt deshalb

    tr(γnum Πhell) = Probγnum(Nf=62)·60/2016 ≤ 5/168.

Die echte Grundzustandsantwort besitzt dagegen einen strikt größeren hellen
Anteil. Schreibe a0=〈F64|Ω〉 und S1=Q+|F64〉/√480. Der bereits abgesicherte
Komplementwert H|_(F64)perp >−3Δ/4 und E<−9Δ/8 ergeben |a0|²>1/4.
Explizit folgt aus dem Eigenwertproblem

    |a0|² ≥ (E/Δ+3/4)/(2E/Δ+3/4) > 1/4.

Die Projektion derselben Eigenwertgleichung auf F64 liefert

    E a0 = g√480 〈S1|Ω〉,
    |〈S1|Ω〉|² > (9/8)² /(480/400) ·1/4 = 135/512.

Da S1 im hellen Zwei-Loch-Raum liegt,

    tr(ρF Πhell)>135/512,
    D(ρF,γnum)>135/512−5/168 = 2515/10752 > 0,2339.

Diese globale untere Schranke benötigt keine Annahme, dass S1 bereits den
ganzen Einbosonanteil von Ω ausschöpft. Der reine normierte Einpaarzustand S1
liefert nach Ausspuren der Bosonen Πhell/60; bei einem Vergleich innerhalb
dieses Zwei-Loch-Sektors beträgt der Unterschied zur uniformen Referenz
1−60/2016=163/168. Dieser letzte bedingte Vergleich ist keine neue globale
97-Prozent-Schranke für Ω.

**Ergebnis:** Ein Paritätsbit allein erzeugt nicht die W-abhängige Paarstruktur.
Die echte E8-Simple-Current-Erweiterung ist auch nicht bloß diese Zustands-
projektion; sie verändert die Feldalgebra und wird hierdurch nicht widerlegt.

## 5. Unabhängige dynamische und spektrale Kontrollen

### 5.1 Ein echter verbundener Vierpunktterm entsteht sofort

Jede W-Zeile enthält acht disjunkte Fermionpaare. Im N=2-Sektor bilden sie
zusammen mit einem Boson einen invarianten Neuner-Stern. Starte mit einem der
acht Fermionpaare und leerem Boson. Sei p(t) die Wahrscheinlichkeit, dass
dieses Paar noch besetzt ist. Auf diesem Stern gilt für seine beiden Moden

    〈ni〉=〈nj〉=〈ni nj〉=p(t),
    〈f_i† f_j〉=〈f_i f_j〉=0.

Der Wick-Defekt ist daher p(t)(1−p(t)). Aus der genauen Neuner-Matrix folgt

    p(0)=1,  p'(0)=0,  p''(0)=−2g²,
    [Wick-Defekt]''(0)=2g² ≠0.

Eine rein gaußsche Entwicklung aus derselben gaußschen Anfangspräparation
hätte einen identisch verschwindenden Wick-Defekt. Dieser Widerspruch benutzt
keinen Grundzustandsbeweis und gilt für jedes g≠0.

### 5.2 Auch die erste nichttriviale Ladungsspektrallücke ist nicht frei

Der native N=1-Hamiltonoperator ist null auf allen 64 Zuständen. Bei N=2 gilt

    H2 = [[0_(2016), g W†], [g W, Δ I60]].

WW†=8I ergibt das exakte charakteristische Polynom

    det(λI−H2) = λ^1956 (λ²−Δλ−8g²)^60.

Für g≠0 hat H2 also genau 1956 Nullmoden. Ein freier, quadratischer,
ladungsbewahrender Ersatz auf denselben 64 CAR- und 60 CCR-Moden müsste aus
dem N=1-Spektrum 64 Null-Einteilchenenergien besitzen. Dann hätte er bereits
2016 Null-Zweifermionenzustände. Die Multiplizitäten widersprechen sich.

Das schließt eine ladungserhaltende unitäre Isospektralität in dieser freien
Ersatzklasse aus, auch wenn sie nicht als linearer Feldwechsel vorgegeben
wird. Ein Zusatz μN verschiebt die betrachteten N-Sektoren gemeinsam und
behebt den Multiplizitätswiderspruch nicht. Nichtlineare Reduktionen mit neuen
Nebenbedingungen oder neue Hilfsfreiheitsgrade sind nicht von diesem Satz
erfasst.

## 6. Quellenentscheidung statt weiterer Anpassungsrunde

Die zuvor vorgeschlagene Momentenanpassung allein war als nächster Schritt
zu schwach priorisiert: Vor einem solchen Abgleich muss das Feldwörterbuch
überhaupt dieselbe Zustandsklasse zulassen. Für eine direkte lineare Abbildung
der freien Seam-Felder ist diese Voraussetzung jetzt negativ entschieden.

Die Konsequenz lautet:

- Den nativen Hamiltonoperator weiterhin als exakt untersuchtes Modell führen,
  aber seine Gleichsetzung mit einer bloß umetikettierten freien Seam nicht
  weiter durch Clock- oder Zweipunktanpassungen zu verfolgen.
- Die vorhandene E8-Erweiterung nur mit ihren wirklichen Komposit-/Stromfeldern
  untersuchen. Bereits `v469` unterscheidet den freien Majorana-Träger von der
  lokalen bosonischen Erweiterung. Ein Gewicht-eins-Strom ist kein unabhängiger
  CAR-Erzeuger; dies war im vorherigen Außenalgebra-Audit separat widerlegt.
- Eine alternative Brücke muss an derselben Quelle nichtgaußsche Feld- und
  Mehrpunktdaten liefern. Ihre bloße Existenz als abstrakte Zustandsprojektion
  oder als zusätzlicher Modell-Hamiltonoperator genügt nicht.

Dies ist eine abgeschlossene negative Entscheidung der genannten direkten
Quellenklasse, kein universeller Nichtexistenzsatz. Der ursprüngliche rohe
TFPT-Prozess und ein positiver interagierender Feldadapter sind damit noch
nicht konstruiert. Insbesondere sind 3+1D, chirales Maß und dynamischer Spin 2
weiterhin nicht hergeleitet; T1–T8 bleiben offen.

## 7. Reproduktion und Vertrauensgrenzen

`replay.py` friert sieben Eingaben ein, wiederholt das rationale ursprüngliche
Grundzustandszertifikat und führt den neuen Prüfer normal sowie optimiert aus.
Beide Ergebnispaare sind byteidentisch. Der neue Prüfer enthält 125 explizite
Bedingungen einschließlich aller 60 Paarkanäle, Casimir-, Paritäts-, Spektral-
und dynamischer Kontrollen. Die Anzahl zählt Komponentenprüfungen, nicht 125
unabhängige Sätze. Die analytischen Argumente dieses Berichts und die
Gaußzustandsliteratur bleiben Teil der Beweiskette.

Die frühere vollständige Momentenumeration wurde in dieser Runde nicht neu
durchgeführt. Die freien v480/v524/v469-Module wurden für ihre Quellenklasse
gelesen beziehungsweise gezielt eingesehen und eingefroren, nicht komplett
numerisch wiederholt. Keine fremden Quellen oder alten Ergebnisstände wurden
geändert. Die ursprünglichen fünf Nutzerberichte bleiben unverändert.

Bei der Prüferentwicklung war ein Hilfsausdruck zur Überlappungsschranke mit
einem überzähligen Faktor drei eingetragen. Die systematische Fehleranalyse
reproduzierte den Widerspruch, prüfte die rationale Differenz und korrigierte
die Hilfsformel. Die Grundzustandsschranke |a0|²>1/4 und die Paritätsschranke
wurden dadurch nicht verändert. Der korrigierte Ausdruck ist
(8E+9)/(4(8E+3)) für die Differenz zur Schranke 1/4 bei E in Einheiten von Δ.
