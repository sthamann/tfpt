# Unabhängiger Review des stationären thermischen Anschlusses

10. September 2026. **PASS für den deklarierten vollständigen endlichen U(1)-Rotor/CAR-Parent.** Der Satz schließt die konkret bezeichnete Existenzlücke: Die kritische arithmetische Antwort besitzt einen durch stationäre normale Gibbszustände dieses Parents angenäherten stationären Erweiterungszustand. Er wählt keine physikalische Temperatur aus, setzt keine Zeitflüsse gleich und liefert keinen RH-/Faktorisierungsabschluss.

Geprüfter Bericht: `THERMISCHER-ANSCHLUSS.md`, SHA256 `203a4ce4756331b6b1922dfd0450d8a00ef41e6278eeaebf19831344a45015a2`.

## 1. Ganzer physischer Raum und Operationsdefinition

Mit 3N Kanten, N Knoten und verbundenem Graphen besitzt der ganzzahlige Zyklenraum Rang 2N+1. Die drei anderen Kanten der gewählten Plaquette bilden einen Wald; dieser lässt sich im verbundenen Graphen ohne e zu einem Spannbaum ergänzen. Damit ist der Fundamentalzyklus von e genau p. Alle übrigen Fundamentalzyklen besitzen e-Komponente null. Die Identitätsuntermatrix auf den Nichtbaumkanten beweist eine ganzzahlige Basis, nicht nur eine reelle Parametrisierung.

Jede Maskenquelle mit Summe null lässt sich durch ganzzahlige Flüsse auf dem Baum lösen. Dessen e-Komponente ist null. Somit ist q=E_e, die Zerlegung (2) eindeutig und die direkte Summe über genau binom(2N,N) Masken vollständig. Jeder Fundamentalzyklus hat höchstens N Kanten; tr(B*B)≤2N² ist korrekt. Der Schurkomplementkoeffizient ist strikt positiv und höchstens vier.

W und S_m^p lassen die Materiemaske unverändert und verändern die elektrische Divergenz nicht. S_m^p wirkt in diesen Koordinaten als q↦mq, ist daher eine beschränkte Isometrie mit den angegebenen Restklassen als Reichweitenprojektionen. Hier wird keine physisch durch H erzeugte Implementierung von S_m^p behauptet.

## 2. Gibbs-Existenz und Störungsvergleich

Eine positive definite Gitterquadratik mit endlich vielen affinen Verschiebungen hat kompakte Spektralprojektionen unter jeder festen Energie und eine endliche Wärmespur bei jedem β>0. Der Onsitebound 4N und der separat gelesene adjungiert gepaarte Hopbound 101N/192 ergeben tatsächlich C_N=869N/192. Beschränkte selbstadjungierte Störung und Min-Max gewährleisten den gleichen elektrischen Definitionsbereich, kompakten Resolventen, endliche Gibbsnormalisierung und endliche thermische Energie.

Die aktualisierte Entropierichtung D(σ_β||ρ_β) hat das richtige Vorzeichen. Die Differenz der logarithmischen Operatoren ist βV plus eine endliche Konstante; die einzelnen Erwartungen sind unter σ_β ebenfalls wohldefiniert. Die Schranke D≤2βC_N und daraus ||ρ_β−σ_β||₁≤2√(βC_N) sind richtig, ohne eine Kommutationsannahme.

Die live gelesene [Autorenfassung von Watrous, The Theory of Quantum Information, Satz 5.38, gedruckte S. 282–283](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) gibt den genannten Zweiausgangsmessungsbeweis und den Faktor 1/[2 ln 2] bei Logarithmusbasis zwei. Die Umrechnung in natürliche Logarithmen ist korrekt. Der Bericht kennzeichnet die dort endlichdimensionale Fassung ausdrücklich; der Messungs-/Datenverarbeitungsbeweis gilt auch für die hier normalen Dichteoperatoren. Es wird kein endlicher Flusscutoff dafür eingesetzt.

## 3. Uniforme Antwortschranke und explizites Temperaturrezept

Nach Ergänzung in den Querkoordinaten hat der Gaußfaktor den q-Koeffizienten a=(κ/2)Schur(G)>0 mit a≤2κ. Poisson in den d−1 Querkoordinaten liefert die Exponenten 2π² k*(B*B)⁻¹k/(κβ). Aus λ_max(B*B)≤tr(B*B) folgt der angegebene niedrigere Exponent c/β. Die Phasen hängen von q und Maske ab, ihr Betrag ist eins; die Fehlerabschätzung (5) ist deshalb wirklich uniform, nicht nur punktweise in q.

Die Rechteckabschätzung für ein Gitter der Schrittweite m lautet |mΣg−∫g|≤m Var(g). Nach Division durch m ist der absolute Summenfehler höchstens Var(g)=2, unabhängig von m. Daraus folgen die Atomschranke und die Restklassenschranke (6) mit ihren Nennern. Die nachträgliche Normierung eines relativen Fehlers |e|≤R<1 verändert die Verteilung in l1 um höchstens 2R/(1−R); positive Maskenmischungen erhalten dies.

Der korrigierte Fixpunktfall ist ebenfalls exakt: Bei m≠n existiert ein diagonaler Ausgang genau dann, wenn (a−b)/(n−m) ganzzahlig ist; dann ist q=b+n(a−b)/(n−m). Es gibt höchstens einen solchen Wert. Alle Monomiale haben Norm höchstens eins. Deshalb kontrolliert (7) zugleich alle einzelnen affinen Monomiale mit denselben Konstanten. Normdichtheit liefert den eindeutigen Limes auf A_p. Uniformität für einzelne Grundanfragen liefert keine Uniformität für beliebige Summen mit unbeschränkter Koeffizientennorm.

In (8) bezahlt jeder der ersten beiden Terme höchstens ε/3. Aus dem dritten folgt y≤ε/(48d), dann R≤ε/(16−ε) und 2R/(1−R)≤ε/(8−ε)<ε/3. Die gesamte Fehlergarantie ist daher ≤ε. Das Rezept ist konservativ, aber endlich und rational berechenbar; es präpariert noch keinen Gibbszustand.

## 4. Explizite Rechtfertigung der Energieasymptotik

Der kurze Min-Max-Verweis im Bericht lässt sich ohne Differenzieren einer bloßen asymptotischen Logspur präzisieren. Sei ν_j≥0 die geordnete elektrische Eigenwertliste und λ_j die H-Liste, mit |λ_j−ν_j|≤C_N. Setze u₀(β)=Σν_j e^(−βν_j)/Z_el. Dann gilt

    e^(−2βC_N) u₀(β)
       ≤ Σν_j e^(−βλ_j)/Z_H
       ≤ e^(2βC_N) u₀(β).

Der Ersatz ν_j↦λ_j verändert den Erwartungswert um höchstens C_N. Ferner unterscheidet Tr(ρ_β H_el) sich von Tr(ρ_β H) um höchstens C_N. Die volle Gitter-Poissonformel, mit ihren weiterhin exponentiell kleinen differenzierten Resten, ergibt βu₀(β)→d/2. Die beiden Vergleiche liefern daher genau βTr(ρ_β H_el)→d/2. Alle Energieerwartungen bei β>0 sind endlich. Ein gleichmäßiger Satz für N→∞ folgt daraus nicht.

## 5. Stationarität, notwendige Singularität und Grenze

Die volle Gibbsfamilie ist H-stationär auf B(H_phys). Die Gleichungen für jeden festen beschränkten Operator und jede feste Zeit bleiben bei schwachen-* Teilnetzgrenzen erhalten. Kompaktheit liefert solche Teilnetze; die zuvor bewiesene eindeutige Restriktion auf A_p ist τ. Weder eine sequentielle Konvergenz auf ganz B(H_phys) noch dessen eindeutiger Gesamtgrenzzustand werden beansprucht. Auch eine Invarianz von A_p unter dem vollen Zeitfluss wird nicht benötigt.

Eine zulässige zusätzliche Schärfung der Formulierung „im Allgemeinen singulär“ ist **notwendig nichtnormal**. Für die Projektion Q_q auf E_e=q gilt Q_q≤P_{m,q mod m}. Jede Erweiterung Φ von τ erfüllt also Φ(Q_q)≤1/m für alle m und damit Φ(Q_q)=0. Da Σ_qQ_q=I stark, ist Φ nicht normal. Sie annihiliert darüber hinaus die kompakten Operatoren: Endlich viele q-Sektoren haben Gewicht null, und jeder endlichrangige Operator lässt sich in Norm durch solche Sektoren approximieren. Weil H kompakten Resolventen hat, hat eine solche Φ keine endliche H-Energie im üblichen durch beschränkte Spektralabschneidungen definierten Sinn.

Dies widerspricht dem All-low-Nichtstationaritätszeugen nicht. Der neue Satz mischt sämtliche zulässigen Materiemasken und verändert damit genau dessen Präparationsvoraussetzung. Er beweist noch keine ursprüngliche Cap-Reinheit, Raumzeit-/Gravitationseigenschaft oder bevorzugte Temperaturroute. Der Geltungsbereich bleibt der ausdrücklich gegebene endliche Parent.

## Kontrolle

`check_thermal.check_all()` wurde durch Import unabhängig ausgeführt, ohne Dateien zu schreiben: **79/79 PASS**, sämtliche Ergebnisfelder identisch zur vorhandenen `thermal-checks.json`. Der Checkerhash ist `f29c89000d5aa2d3027f880c99a5a3c1774cb5f9dfce51be2ccf87e64925efed`. Die Kontrollen ergänzen den hier allgemein geprüften Beweis; eine große Gibbsdichtematrix wurde weder aufgebaut noch als vorbereitet ausgegeben. Keine Originaldatei geändert.
