# Arithmetik in Geometrie übersetzen und die Lösung zurücklesen

Stand: 10. September 2026. Begrenzte, abgeschlossene Faktor-Spur. Originale schreibgeschützt gelesen. Diese Untersuchung liefert eine vollständig ausgeführte klassische Demonstration und präzise Übertragungsregeln; keinen neuen allgemeinen Faktorisierungsalgorithmus und keinen RH- oder P-versus-NP-Beweis.

**Die gewünschte Art von Problemwechsel funktioniert bereits: Eine Zahl wird in eine Familie geometrischer Systeme eingebaut, eine günstige lokale Dynamik erzeugt einen Zeugen, und ein exakter Rückleser liefert einen Faktor. Entscheidend ist, welche Operation in der neuen Darstellung billiger wird.** Der stärkste hier passende Prototyp ist Lenstras elliptische Kurvenmethode (ECM). Die eigenen bisherigen TFPT-Versuche passen in denselben Prüfrahmen.

## 1. Der Vertrag, den eine hilfreiche Transformation erfüllen muss

Für eine Eingabe N mit Bitlänge b genügt eine abstrakte Entsprechung zwischen Zahlen und geometrischen Objekten nicht. Der gesamte Weg benötigt folgende Daten:

| Bestandteil | Konkrete Frage | Notwendiger Nachweis |
|---|---|---|
| Aufbau | Wie entstehen Raum, Operationen und Anfangszustand aus N und öffentlichen Parametern? | Kein Zugriff auf Faktoren, vollständige Teilerlisten oder ungeprüfte vorbereitete Spektren. Aufbaukosten in b. |
| Erhaltene Information | Welche Eigenschaft des ursprünglichen Problems bleibt bei der Abbildung erhalten? | Exakte Identität, Reduktion oder kontrollierter Fehler; für RH zusätzlich die betreffende Positivitätsstruktur, für Faktorisierung die relevanten ganzzahligen Ideale. |
| Dynamik / Algorithmus | Was lässt sich im neuen Raum tatsächlich ausführen? | Konkrete Operationen, nicht nur Existenz einer passenden Basis oder eines Hamiltonoperators. |
| Günstiger Zeuge | Welches erreichbare Ereignis genügt für eine Lösung? | Beweis von Erreichbarkeit oder bezifferte Erfolgswahrscheinlichkeit. Parameterwahl und misslungene Versuche zählen mit. |
| Rückleser | Wie wird daraus der Faktor oder das Beweiszertifikat? | Expliziter Algorithmus mit Ausnahmefällen. Die Rücktransformation darf nicht das ursprüngliche Problem erneut vollständig lösen müssen. |
| Genauigkeit | Wieviel Präzision, Zustandspräparation und Messung wird benötigt? | Fehler unterhalb eines bewiesenen Entscheidungsabstands; Kosten von Verfeinerung und Wiederholungen. |
| Gewinn | Warum ist der vollständige Weg günstiger? | Aufbau + Suche + Entwicklung + Messung + Rücklesen + Zertifizieren, im selben Rechenmodell wie der Vergleich. |

Als Kostenidentität ist daher

\[
C_{\rm gesamt}=C_{\rm Aufbau}+C_{\rm Parameterwahl}+C_{\rm Dynamik}
 +C_{\rm Präzision/Messung}+C_{\rm Rücklesen}+C_{\rm Zertifikat}
\]

zu prüfen. Bei Zufallsverfahren gehören alle erfolglosen Läufe in die erwarteten Gesamtkosten. Ein universell darstellbarer Raum gewährt nicht automatisch eine günstige Implementierung jeder darin existierenden Transformation. Shor stellt diese Uniformitätsforderung bereits ausdrücklich an die Schaltungserzeugung und Gatekoeffizienten. [Shor, §§2–5](https://arxiv.org/pdf/quant-ph/9508027)

## 2. Eine vollständig ausgeführte Übersetzung: ECM

Lenstra ersetzt bei der Faktorisierung die feste multiplikative Gruppe durch die Punktgruppe einer variablen elliptischen Kurve. Die gleiche Rechnung modulo N wirkt gleichzeitig modulo den unbekannten Primteilern. Wird ein Punkt in einer lokalen Gruppe neutral und in einer anderen nicht, kann ein größter gemeinsamer Teiler diese Asymmetrie sichtbar machen. Der Wechsel der Kurve verändert die lokalen Gruppenordnungen und damit ihre Glattheitschancen. Die übliche subexponentielle Laufzeitabschätzung hängt von einer Glattheitsannahme ab; sie ist keine polynomielle Garantie für jede Eingabe. [Lenstra, Einleitung und §2](https://pages.cs.wisc.edu/~cs812-1/Lenstra1987.pdf)

### Aufbau aus der Eingabe

Das neue Demonstrationsprogramm erhält ausschließlich

\[
N=10403,\qquad B\in(10,20,40),\qquad a=1,\ldots,16.
\]

Es wählt P=(2,3) und berechnet b=3²−2³−2a modulo N. Damit liegt P auf der aus N hergestellten Kurve

\[
E_a:\quad y^2=x^3+ax+b\pmod N.
\]

Der erste Versuch ist bereits erfolgreich:

\[
E_1:y^2=x^3+x-1,\qquad P=(2,3),\qquad K=\operatorname{lcm}(1,\ldots,10)=2520.
\]

Der ggT von 4a³+27b²=31 modulo N mit N ist 1. Die Kurve ist deshalb an jedem noch unbekannten Primteiler glatt. Die Faktoren wurden weder für ihre Auswahl noch für die Wahl von K benutzt. Diese Zahl ist ein bewusst kleines Kontrollbeispiel, kein zufälliger Leistungsnachweis und keine Behauptung, dass der Demonstrator seine Faktoren vorher nicht hätte erraten können; der geprüfte Datenfluss liest sie nicht ein.

### Dynamisches Ereignis und exakter Rückweg

Die binäre Multiplikation mit K erreicht zunächst

\[
314P=(5355,4542)\pmod N.
\]

Beim nächsten Schritt 314P+P benötigt die affine Gruppenformel den Nenner

\[
d=2-5355\pmod{10403}=5050.
\]

Dieser Nenner ist keine Einheit:

\[
\gcd(5050,10403)=101,\qquad 10403/101=103.
\]

Damit ist die Faktorisierung bereits vor Beendigung der geplanten K-Multiplikation entdeckt. Division und kleine Primzahlprüfung zertifizieren das Ergebnis. Der Auslöser ist keine Singularität der Kurve, sondern das Versagen einer gemeinsamen affinen Koordinatenkarte an unterschiedlich gelegenen lokalen Punkten.

Erst **nach** diesem Erfolg rekonstruiert ein separater Erklärungsschritt die beiden lokalen Systeme:

| Nachträglich bekannte lokale Welt | Ordnung von P | Größe der Punktgruppe | Wirkung von K=2520 |
|---|---:|---:|---|
| modulo 101 | 105 | 105 | KP=O |
| modulo 103 | 121 | 121 | KP=(79,46), also nicht O |

Die schon aufgetretene Kollision bei 315P ist unmittelbar sichtbar: 314P ist modulo 101 der Gegenpunkt (2,98) zu P=(2,3); modulo 103 sind die x-Koordinaten verschieden. **Ein einziger aus N erzeugter geometrischer Prozess trennt dadurch zwei zunächst verborgene arithmetische Komponenten.** Die Rückrechnung benötigt nur den beobachteten Nenner und N.

### Was diese Demonstration kostet und was sie nicht beweist

Die vollständige Suchspur meldet eine versuchte Kurve, 15 Gruppenaufrufe, 14 ggT-Aufrufe, 12 modulare Inversionen und 42 Punktidentitätsprüfungen. Anfangsaufrufe mit O sind in den 15 enthalten. Dazu kommen die elementare Kurven- und K-Konstruktion. Diese Zähler sind **keine vollständigen Bitkosten**, keine gemessene allgemeine Laufzeit und kein Vergleich gegen optimierte ECM-Bibliotheken. Der unabhängige lokale Gruppenzählungsprüfer läuft erst hinterher und gehört nicht zur Solverinformation; sein eigener Aufwand ist gesondert dokumentiert.

Das Programm ist bewusst beschränkt. Ein erfolgloser Lauf gibt NO_FACTOR_IN_BUDGET zurück. Ein nichttrivialer Diskriminanten-ggT wäre ein früher gültiger Faktor. Eine überall verschwindende Diskriminante oder eine unaufgelöste affine Sonderlage führen zum nächsten Versuch. Vertikale Punktpaare ergeben den globalen Punkt O. Allgemeine kleine Faktoren, Primzahlen, perfekte Potenzen und rekursive Vollfaktorisierung gehören in einen vollständigen Produktionsadapter; diese Demonstration fordert N>3 und ggT(N,6)=1.

Eine zweite Implementierung liest nur die gespeicherte Spur, prüft die Gruppenformeln, alle Nenner, den Faktorzertifikatsweg und den Zwischenmultiplikator 315 erneut. Zusammen mit den folgenden kleinen Übertragungsprüfungen bestehen 79 exakte Kontrollen. Es liegt kein formales Beweisassistent-Zertifikat vor.

## 3. Zwei weitere erfolgreiche Übersetzungsmuster und ihre Kostenstelle

**Ordnungsfindung → Spektrum → Faktor.** Für ggT(a,N)=1 erzeugt a die periodische Folge a^x modulo N. Ein korrekt gefundenes gerades r mit a^r=1 liefert z=a^(r/2); falls z nicht ±1 ist, geben ggT(z−1,N) und ggT(z+1,N) nichttriviale Teiler. Shors Quantenschaltung gewinnt die Periodeninformation mit reversibler modularer Exponentiation, Fouriertransformation und anschließender Kettenbruchrechnung. Ungerade Ordnung, z=−1 und nicht hinreichend informative Messungen erfordern Wiederholungen; Nicht-Einheiten werden vorab durch ggT abgefangen. Die Laufzeit ist polynomial im Quantenmodell. Ein klassischer vollständiger Zustandsvektor oder eine kostenlos angenommene Spektralmessung erbt diesen Gewinn nicht. Das ist kein Beweis von P=NP. [Shor, §5](https://arxiv.org/pdf/quant-ph/9508027)

**Quadratische Formen → geometrische Infrastruktur → Faktor.** Aus N werden reduzierte Formen und der Hauptzyklus zu einer reellen quadratischen Ordnung konstruiert. Reduktion bewegt lokal, Gaußkomposition ermöglicht größere Schritte. Ein geeigneter erreichbarer ambiger Punkt oder Formenkoeffizient kann über ggT einen Faktor liefern. Ein passender Regulator oder ein geeignetes Vielfaches macht bestimmte Ziellagen schnell erreichbar; seine Erzeugung und Präzision bleiben Teil der Aufgabe. In Murru–Salvatori v2 werden arithmetische Operationszahlen ausdrücklich getrennt von Großzahl- und Logarithmuskosten gezählt, und die nichttriviale Auslese hat Bedingungen. Der dort selbst enthaltene Fall N=731 zeigt, dass ein Mittelpunkt lediglich den trivialen Koeffizienten 2 liefern kann. [Murru–Salvatori, Korollar 3.12, Beispiel 3.14 und §5](https://arxiv.org/html/2409.03486v2)

Diese drei Muster erklären, was ein hilfreicher gemeinsamer Nenner leisten kann: **strukturierte Wirkung auf verborgenen lokalen Komponenten, eine selektive Gleichheit/Kollision und ein kurzer arithmetischer Zeuge**. Das ist eine methodische Gemeinsamkeit dieser Faktorisierungswege, keine behauptete Klassifikation sämtlicher mathematischen Lösungsverfahren.

## 4. Was die eigenen ursprünglichen Versuche tatsächlich beitragen

Der lokale Faktorisierungsgraph wurde zuerst abgefragt; Originalresultate und gezielte Quellfunktionen anschließend gelesen. Der Status hatte 26995 erfasste Quellen, keine Lesefehler und keine veralteten kuratierten Einträge. Das sind Suchabdeckung und Frische, keine semantische Prüfung aller Quellen. Die unten genannten alten Laufzahlen wurden aus ihren Originalartefakten gelesen und in dieser Runde nicht neu gebenchmarkt.

### r640: E8-Koeffizienten, Klassengruppe und begrenzte Modulo-Auslese

Die gelesenen Originalfunktionen `s2_delta_is_solution`, `s3_quadratic_character_class_number` und `s5_modcrt_preregistration` halten tatsächlich verschiedene Aussagen auseinander:

- Für N=pq mit verschiedenen Primzahlen bestimmen φ(N) oder σ₃(N) die Faktoren durch explizite elementare Rückrechnung. Im E8-Gitter, mit q-Exponent ||v||²/2, gilt a_N=240σ₃(N). Die Symbolidentität sagt noch nichts über die Kosten, gerade diesen Koeffizienten zu gewinnen.
- Das kleine Klassengruppenexperiment erzeugt sämtliche reduzierten Formen, bestimmt daraus h(−4N) und prüft anschließend Torsions- und Faktorleser. Seine günstige Erfolgsrate bei gegebenem h ist ein Ergebnis dieser endlichen Sammlung. Enumeration und eine günstig samplende allgemeine Klassengruppenimplementierung dürfen nicht durch die Überschrift eines Tests verschwinden.
- Der endgültige Originalstatus lautet NO_SHORTCUT_FOUND für vier implementierte Leser und schließt ausdrücklich eine universelle Dichotomie oder Untergrenze für andere Ansätze aus.

**Zusätzliche Präzisierung dieser Runde:** Das informative Modulo-3-Bit in der letzten Funktion gehört zu **σ₃(N)=a_N/240 als ganzzahlig normiertem Koeffizienten**. Der rohe E8-Koeffizient a_N modulo 3 ist stets null, weil 3 die Zahl 240 teilt. Für N=55 und N=91 ist jeweils N≡1 modulo 3, aber σ₃(N)≡0 beziehungsweise 1; a_N≡0 gilt in beiden Fällen.

Eine Übertragung muss daher erst integral durch 240 teilen, oder beispielsweise a_N modulo 720 bestimmen und dann den durch 240 teilbaren Rest normieren. Im Körper F₃ darf man 240 nicht invertieren. Das widerlegt nicht den normierten Leser; es verhindert eine unzulässige Gleichsetzung zweier Messaufgaben. Das entsprechende Testprogramm prüft die Beispiele exakt.

### Fortsetzung mit bereinigtem E8-Beobachter

Der Originalbericht vom 8. September konstruiert ohne bekannte Faktoren

\[
D_B(q)=\sum_{d>B,\ k>B}d^3q^{dk}.
\]

Für verschiedene Primzahlen p,q>B ist [q^N]D_B=p³+q³. Ein expliziter Rückleser toleriert absoluten Fehler 4N. Das ist ein brauchbarer Entscheidungsabstand. Offen bleibt die günstige Gewinnung des Einzelkoeffizienten einschließlich aller Aliase und Auswertefehler. Die im Bericht ausgeschlossene einfache positive Trapezregel ist nur eine konkrete Auslesemethode. Daraus folgt keine allgemeine Unmöglichkeit einer Fourier-, modularen oder geometrischen Faktorisierungsroute.

### Zertifizierte Regulator-Fortsetzung

Die Weiterentwicklung vom 6. September erzeugt einen Norm-1-Einheitenlogarithmus aus N, zertifiziert ihn und koppelt ihn an den Sprung. Der vollständige Weg gelingt bei N=1254389. Auf dem dort eingefrorenen kleinen Pilot mit neun neuen 20-, 24- und 28-Bit-Eingaben liefert er 3/9 Faktoren, SQUFOF und Rho jeweils 9/9. Die Erzeugungs-, Präzisions-, Sprung- und Fehlversuchskosten sind ausgewiesen. Das belegt eine echte ausführbare Verbindung, aber noch keinen Vorteil.

Insbesondere existiert der physische Faktor nicht automatisch als günstiger Koeffizient an jeder geometrischen Ziellage. Im vollständig gelesenen N=731-Hauptzyklus ergeben sämtliche untersuchten Formenkoeffizienten nur ggT 1 mit N. Der Fakt, dass eine Darstellung einen exakten Regulator besitzt, ersetzt keinen erfolgreichen Rückleser.

### Neuere affine TFPT-Wortfamilien

Die bereits vorhandene Suche vom 9. September führt die konkrete Linie weiter: aus N auswertbare Wortfamilien, exakter Compiler, relative Kollisionsleser, getrennte Parameterwahl und frischer Holdout. Die genetisch gewählte Familie löst 15/48 Fälle, eine reziproke Kontrolle und Lucas jeweils 17/48, Brent 40/48 im festgelegten Budget. Alle genetischen Erfolge werden auch von Lucas und Brent gefunden. Dies ist eine begrenzte negative Leistungsmessung, kein Verbot anderer Familien.

Damit liegt die nächste offene Voraussetzung bereits scharf vor: **Eine aus N billig auswertbare Information muss Parameter auswählen, die eine frühere Kollision modulo einem unbekannten Faktor und eine spätere modulo den anderen wahrscheinlicher machen. Die Auswahl muss ihren Aufwand zurückverdienen.** Eine neue geometrische Bezeichnung allein ändert diese Voraussetzung nicht.

## 5. Exakte Anbindung an die rekonstruierte U/V-Dynamik

Die vorige Runde enthält eine geprüfte Übersetzung der U/V-Wortwirkung über Z[i,1/2] und daher auf jeden ungeraden Modul. Die Basisdeterminante ist −1/16 und somit eine Einheit. Insbesondere bleibt die ganze Wortwirkung erhalten. Bei Charakteristik 3 sind die bereits gekürzten Operatoren zu reduzieren; die ursprüngliche normalisierte Gram-Matrix enthält einen Faktor 1/3 und ist dort nicht direkt reduzierbar.

Für die Faktorauslese ist der folgende elementare Satz nützlich:

**Satz.** Sei R=Z/NZ, S∈GL_d(R) und y=Sx. Dann erzeugen die Koordinaten von x und y dasselbe Ideal in R. Folglich gilt für beliebige ganzzahlige Repräsentanten

\[
\gcd(N,x_1,\ldots,x_d)=\gcd(N,y_1,\ldots,y_d).
\]

**Beweis.** Jede y-Koordinate ist eine R-Linearkombination der x-Koordinaten, also (y)⊆(x). Aus x=S⁻¹y folgt die umgekehrte Inklusion. Die Ideale in Z/NZ entsprechen genau den Teilern von N. Damit stimmen die beiden ggT überein. Für gaußsche Koordinaten werden Real- und Imaginärteile als 2d Koordinaten über R geschrieben; derselbe Beweis gilt. ∎

Für eine fest gewählte einzelne Messfunktion ℓ muss die Übersetzung ebenfalls mitgeführt werden: y=Sx verlangt den Leser ℓS⁻¹, damit ℓx erhalten bleibt. Eine beliebige neue Einzelkoordinate oder euklidische Norm ist nicht automatisch derselbe Faktorleser.

Das neue kleine Prüfbeispiel transformiert den gefundenen ECM-Nennervektor (5050,10100) mit der unimodularen Matrix ((1,2),(3,7)) in (4444,2626) modulo 10403. Beide Koordinatenideale liefern genau den Faktor 101.

Dieser Satz sagt **nicht**, dass ein Basiswechsel niemals beschleunigen kann. Eine Darstellung kann Operationen diagonal, lokal oder dünn besetzt machen und dadurch die Kosten reduzieren. Er sagt präzise, welche arithmetische Information beim richtigen Rücktransport dieselbe bleibt. Beim schon rekonstruierten U/V-Prozess liegt bisher kein neuer günstiger Kollisionsselektor oder neuer effizienter Messzugang allein durch diesen Basiswechsel vor.

## 6. Konsequenz für die Suche nach einem gemeinsamen Raum

Eine belastbare Vereinheitlichung sollte nicht mit „beliebige Transformationen“ beginnen, sondern mit einem Katalog von **ausführbaren Übersetzungen samt erhaltenen Fragen und Kosten**. Für Faktorisierung ist die tragende Information oft die unterschiedliche Reaktion der unbekannten lokalen Faktoren. Bei ECM verbessert die variable Geometrie die Auswahlchance tatsächlich. Bei Ordnungsfindung schafft eine spezifizierte Quantenschaltung einen anderen Zugang zur globalen Periode. Bei den eigenen E8-, Regulator- und U/V-Versuchen sind mathematische Übersetzungen und teilweise vollständige Rückleser schon vorhanden; der effiziente Produzent des richtigen Zeugen bleibt die Arbeit.

Der konkrete nächste Abnahmepunkt lautet deshalb: **N-only-Aufbau einer neuen Familie plus beweisbare oder frische experimentell bestätigte Verbesserung der asymmetrischen Ereignisrate, nachdem Vorbereitung, Suche und Lesen vollständig bezahlt sind.** Für die E8-Koeffizientenroute wäre das alternativ eine zertifizierte Einzelkoeffizientenoperation innerhalb des bekannten Fehlerbudgets mit günstigen Gesamtkosten. Diese Fragen sind konkret genug, um eine neue mathematische Idee als tatsächlichen Fortschritt zu erkennen.

Nachweise: `ecm_demo.py`, `ecm-checks.json`, `transfer_checks.py`, `transfer-checks.json`, `SOURCES.json`. Wiederholung mit Python 3, Standardbibliothek, ohne externe Solver. Die Skripte schreiben ausschließlich die jeweiligen Ergebnisdateien in diesem eigenen Arbeitsordner neu.
