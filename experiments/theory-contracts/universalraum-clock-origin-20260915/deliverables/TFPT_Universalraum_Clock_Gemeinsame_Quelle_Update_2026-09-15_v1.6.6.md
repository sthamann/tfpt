# TFPT / Universalraum — Änderungen v1.6.6

15. September 2026. Kurzes Update gegenüber v1.6.5. Die vollständige
Konsolidierung bewahrt zusätzlich sämtliche älteren Herleitungen.

## Neu bewiesen oder präzisiert

1. **Der Quell-Clock ist ein konkretes Spin(10)-Element.**
   Das ausdrückliche Cliffordwort `S=Ω10 R01 R02 R34=ΠΓ(p)` stimmt auf
   Fermionen, Bosonen und dem ursprünglichen Paartensor mit dem dokumentierten
   Clock überein. Eine bloße Normalisatorbehauptung wird so ersetzt.
2. **Clock und ein getrennter Casimir sind algebraisch kompatibel.**
   Im N=3-Sektor entsteht die assoziative Algebra der Dimension **96** mit
   Kommutantdimension **119597824**; ohne den Casimir waren es 84 und
   240742144. Die Operation ist damit noch nicht physisch verfügbar.
3. **Ein echter kleiner Paartransferzeuge ist konstruiert.**
   Die volle ursprüngliche W-Wechselwirkung plus ein ausdrücklich zusätzlich
   zugelassener Bosonmischer schließt exakt auf vier N=9-Zuständen. Die
   Markenübertragung 57→58 hat eine strenge Wahrscheinlichkeit **>99,3 %**.
   Sie verändert eine innere Farbquantenzahl und ist kein räumlicher
   Transport desselben N=64-Grundzustandslochs.
4. **Die Herkunft dieses Mischers ist jetzt schärfer eingegrenzt.**
   Der Einzelmischer verletzt den ursprünglichen Clock; seine Orbitsumme
   bewahrt den Clock, verletzt aber weiterhin einen gemeinsamen SU(4)-Cartan.
   Beide liegen außerhalb von Alg(H,Nb,G,CSpin,CColor). Ein Ladungsausgleich
   oder ein anderer tatsächlich ursprünglicher Generator wäre nachzuweisen.
5. **Der Ein-Kopie-Vektoradapter scheitert auch nach beliebigem Basiswechsel.**
   Aus `ΓᵀM_A+M_AΓ=0` und den exakt zertifizierten Produktalgebren folgt Γ=0.
   Zusätzliche Dirackomponenten, unabhängige Dubletts und Ableitungsadapter
   werden dadurch nicht ausgeschlossen.
6. **Der Krylov-Nichtschluss ist unabhängig bestätigt.**
   `||w₂||²=5001523200/229`. Die kleine Änderung durch diesen einen Zweig
   ist keine Konvergenz: Der ausgelassene v₄-Zweig dominiert das vollständige
   Ritzresiduum. Die alten Grundzustands-/Polgrenzen bleiben maßgeblich.

## Aus den neuen Texten korrigiert

- Das vorhandene neue Ground-JSON trägt noch den alten, um 229² falschen
  Normwert. Sein PASS und die daraus berechnete Energie werden nicht übernommen.
- Volle Generatoralgebra ist gruppenstabil, nicht punktweise invariant;
  assoziative Dimension ist nicht dynamische Kontrollierbarkeit.
- Es gibt Zwischenverträge 8→14→15→16; die Verfügbarkeit ist nicht binär.
- Reine überlappende Charts erzeugen keinen Link. Im entarteten nativen
  Polraum gilt für jede Chartbasis `K=E_h S`: gemeinsame Phase, keine Bewegung.
- Das Produkt überlappender lokaler Paritäten ist nicht notwendig globale
  Parität. Der vorgeschlagene Kill-Test wird entsprechend ersetzt.
- Reine vollständige Basiswechsel haben triviale Schleifenholonomie.
  Variierende Unterräume können geometrische Phasen liefern, aber nicht
  automatisch einen unitären Transport oder ein dynamisches Eichfeld.
- Ein stationärer Grundzustand entwickelt nur eine globale Phase.
  Ein Orientierungsbit allein liefert kein unabhängiges gleichgeladenes
  Spinordublett. Primitive Schleifen allein sind keine Primzahlen.
- P≠NP würde nicht allein eine exponentielle Laufzeituntergrenze beweisen.

## Nächster gemeinsamer Test

**Eine einzige globale Quelle mit zwei lokalen Einbettungen definieren;
deren CAR-Gram, globale Ladung/Parität, gemeinsamen H und Ω sowie eine
tatsächlich verfügbare aktive Operation angeben. Auf genau diesem Träger
statische Überlappung und zeitabhängige Antwort getrennt berechnen.**

Nur wenn mehr als `K=E_h S` entsteht und die Quelle die Operation ohne
hineingesetzten Hop liefert, ist der entscheidende Anschluss geschafft.
Anschließend den minimalen Feldadapter und erst darauf die räumliche
Skalierung untersuchen. T1–T8, RH und die anderen globalen Fragen bleiben offen.

Der RH-Katalog konnte wegen eines fehlenden registrierten Quellordners und
Paper-Versionsabweichungen nicht als aktuell freigegeben werden. Die
Schleifenprüfung verwendet deshalb verfügbare Originale und explizite
Gegenbeispiele, keine behauptete neue globale Graph-/Beweisfreigabe.
