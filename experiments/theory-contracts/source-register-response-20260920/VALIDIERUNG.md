# Validierung und interner mathematischer Review

Datum: 2026-09-20. Contract: UR.SOURCE.REGISTER_RESPONSE.01.

## Reproduzierter Stand

Die normale und die optimierte Python-Ausführung erzeugen byteidentische
Zertifikate. SHA-256:

`3d87b4383828d318639dc78eb9d91b47d5080b79b3b8162a1328fe25bec3eaba`

Der eigene Checker enthält 62 exakte Kontrollen, 50 numerische Kontrollen
und 15 Herkunftskontrollen. Zusätzlich wurden 22 Kontrollen des gepinnten
Helfers für den Vergleich mit den tatsächlichen Originaldefinitionen
ausgeführt. Diese Zahlen bezeichnen Kontrollanweisungen, keine Anzahl neu
bewiesener physischer Aussagen.

Größter beobachteter numerischer Absolutfehler: ungefähr 1,41×10⁻¹⁴ bei
Toleranz 3×10⁻¹². Verglichen wurden sämtliche Matrixeinträge an sechs Zeiten
t=0, 1/8, 1/2, 1, 5/2 und 7. Hinzufüge-, Entnahme- und beide Disorder-
Antworten verwenden denselben Zeitparameter.

## Inhaltliche Reviewpunkte

1. **Quellidentität:** Masse +1 und nx=3, ny=1 entsprechen exakt dem
   register_hamiltonian der Originaldatei. Der Helfer führt deren ausgewählte
   Definitionen tatsächlich aus; die Dyaden-/Phaseneinträge werden exakt
   rational rekonstruiert und verglichen.
2. **Operatoren:** Die Quelle H_R bleibt fest. Das Feldwörterbuch wird durch
   T geändert, sodass h'_r=u^(-r)h_ru^r die richtige Richtung hat.
   Erzeugen führt r→r−1, Entnehmen r→r+1. D erhält N und führt s→s+1.
3. **Zustand:** Es wird das Minimum über alle Register- und Teilchenzahlsektoren
   bestimmt. Der N=3-Zustand wird nicht nachträglich gewählt. Seine reine
   Dichte wird zusätzlich als dritte äußere Potenz des negativen Projektors
   reproduziert.
4. **Orientierung der Entnahmeantwort:** Die Matrixeinträge sind
   <c_k† Γ(U)c_j>. Die direkte Fockkontrolle transponiert entsprechend die
   Gram-Matrix der entnommenen Vektoren; sie nimmt keine komplexe
   Konjugation der Zeit vor. Die negative Frequenz der retardierten
   Lochantwort wird erst durch K⁻(−t) eingesetzt.
5. **Singuläre Überlappung:** Der Beweis benutzt Adjunkten und geränderte
   Determinanten statt A⁻¹. Ein genau singuläres Kontrollbeispiel hat eine
   nichtverschwindende Antwort und besteht in exakter Arithmetik.
6. **Unabhängige Rechenwege:** Einteilchen-Determinanten, äußere Potenzen und
   direkt aus CAR-Matrizen gebildete Fock-Hamiltonoperatoren stimmen überein.
   Zusätzlich wurde die allgemeine Formel an komplexen, nichtorthogonalen
   Orbitalen und nichtunitärem U exakt geprüft.
7. **Spektralbeweis:** Charakteristisches Polynom, dreizehn exakte Momente
   und teilerfremder Zähler/Nenner beweisen die dreizehn tatsächlichen Pole.
   Die numerischen Residuen sind eine Darstellung und Gegenkontrolle dieses
   exakten endlichen Befunds.
8. **Ursprüngliche Observable:** Der D-Operator bleibt enthalten. Sein
   niedrigstes Spektralgewicht wurde über den exakten negativen Endprojektor
   berechnet und numerisch unabhängig bestätigt.
9. **Neuheit und Grenzen:** Die Determinantenidentität ist Standard. Neu in
   diesem Contract ist ihre Anwendung auf die neu korrelierte konkrete Quelle
   einschließlich des vollständigen endlichen Grundes und des D-Kanals.
   Kein Ursprung des Lifts, keine lokale Wechselwirkung und kein physisches
   T1–T8-Gate werden als geschlossen ausgewiesen.

Der interne Review und die verschiedenen Rechenwege stammen aus derselben
Lane. Das ist **kein unabhängiges Agentenreview** und kein Beweisassistent.
Die andere Lane war beim ersten Snapshot noch ohne ausführbaren Checker und
ohne Zertifikat. Ihr anschließend verfügbarer Checker wurde tatsächlich
normal und optimiert ausgeführt: 183 Kontrollen bestanden, beide Ausgaben
sind byteidentisch mit ihrem Originalzertifikat. Dessen SHA-256 ist
`0a4d0822bd3d35d3ef6249947436aa6efb9e8dc80ecfde057831c148a5abd3c8`.
Die 21 Quellenpins ihres Checkers wurden bei beiden Läufen geprüft. Die
zusätzlichen Herkunftspins stehen in upstream_replay_manifest.json.
Der analytische Bulk-Grenzsatz aus ihrem PROOF-Abschnitt 4a wird im eigenen
Beweis und Ergebnis als übernommener Befund ausdrücklich berücksichtigt.

Die Spektralgrafik wurde aus dem Zertifikat erzeugt und visuell auf Beschriftung,
Achsen, Überlappungen und die Übereinstimmung mit den dargestellten Daten geprüft.
