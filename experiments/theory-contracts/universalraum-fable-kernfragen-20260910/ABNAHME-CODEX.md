# Was aus der Zusammenarbeit mit Cursor Fable übernommen wird

10. September 2026. Der ausgewählte Agent **Claude Fable 5.1 1M High** im aktiven Cursor-Fenster `tfpt-theoryv4`, Gespräch `Universal space and problem solving`, erhielt das vollständige relevante Forschungspaket und arbeitete an den vier bezeichneten Kernfragen. Seine eigenen Ergebnisse und Gegenprüfungen sind im Belegpaket als gebundene Versionsstände gesichert.

**Übernommen werden die nachstehend belegten Aussagen. Die ursprünglichen Fable-Beweistexte werden nicht pauschal als richtig übernommen.** Drei getrennte Reviews haben die Dynamik, den Programmoperator sowie Arithmetik und Transformationskosten geprüft. Die korrekten Teile sind in `KONSOLIDIERT.md` mit den eigenen Beweisen zusammengeführt.

## 1. Bestätigte und ergänzende Resultate

| Frage | Konsolidiertes Ergebnis |
|---|---|
| Ist die Viereruhr wirklich im Rotor enthalten? | Ja, mit mitgeführtem ganzzahligem Übertrag. Der elektrische Kreuzterm bleibt notwendig. |
| Kann der Cap in tatsächlichen Feldern dargestellt werden? | Ja, für den genau bezeichneten neutralen Wilson-Code und seine gewählte Präparation. Seine Herkunft aus der ursprünglichen markierten TFPT-Clock ist gesondert offen. |
| Bleibt dieser Code unter H geschlossen? | Nein. Auf dem ursprünglichen 16-Code ist die Austrittsstärke exakt N/96. Für beliebige All-low-Superpositionscodes kommt gegebenenfalls ein positiver elektrischer Varianzterm hinzu. |
| Kann man den Austritt konkret verkleinern? | Fables erste quellenbestimmte Materiebeimischung reduziert ihn im geprüften Viererring nach dem LL2-Fix um mehr als Faktor 418. Es bleibt ein positiver Rest. |
| Kann man die wirklichen zusätzlichen Richtungen aufnehmen? | Unsere explizite 32-Block-Erweiterung erhält H⁰ bis H³; onsite und Zwei-Paar-Kanäle liefern weitere tatsächliche Zustandsrichtungen. |
| Passen logarithmische Primzahlgewichte zu gleichen Restklassen? | Ja, unter der bezeichneten arithmetischen KMS-Zeit. Der kritische Zustand ist auf der konkreten affinen Algebra konstruiert; er ist nicht automatisch der physische TFPT-Zustand. |
| Ist eine endliche Vorbereitung mit Fehlerkosten erhältlich? | Ja. Die zusätzlich konstruierte neutrale Boxmischung erreicht je affiner Grundanfrage Fehler ≤1/(2K+1), bei berechneter endlicher elektrischer Energie. |
| Macht die gemeinsame Schreibweise Faktorisierung kostenlos? | Nein. Der N=91-Transfer funktioniert, einschließlich gezählter Suche und Rücklesung. Ein neuer allgemeiner asymptotischer Vorteil ist nicht bewiesen. |

## 2. Ein gefundener Fehler wurde tatsächlich korrigiert

Fables ursprüngliches `checks.py` mit Hash `a92ba954452f1397c364da1da6e7243d5ec5dff5fead0e5548f14f96becc8e6a` implementierte den LL-Zweilinkterm durch zwei nacheinander ausgeführte Fermionhops. Das führte zu einem zusätzlichen Pauli-Blocker am Zwischenort. Der native Einteilchenkern verlangt stattdessen ein direktes Endpunktbilinear mit beiden Linkverschiebungen.

Der konkrete neutrale Gegenzeuge `(Maske75, Flux0) → (Maske78, Flux(1,1,0,0))` muss die Amplitude **−1/576** tragen. Im alten Prüfer stand null. Der Fehler wurde an Fable zurückgegeben und von ihm in beiden Implementierungen korrigiert.

Der korrigierte `checks.py`-Stand `cd139dddf52d8345b1fa32a6cdb5a2a3308ea734b4412f8f7aeb4061ec78654a` wurde unabhängig gegen den schon vorher eigenständig geschriebenen Endpunktoperator geprüft: **85 exakte Kontrollen, darunter die vollständigen H-Bilder von 37 relevanten Basiszuständen, stimmen.** Die erste Dressingstufe und alle vier rationalen Restleckagen wurden unabhängig reproduziert.

| Codevektor | Restleckage, gerundet | Reduktionsfaktor, gerundet |
|---:|---:|---:|
| 0 | 3.322121917481888·10⁻⁵ | 418.0728231496 |
| 1 | 3.322172930614849·10⁻⁵ | 418.0664034945 |
| 2 | 3.322326147948549·10⁻⁵ | 418.0471233225 |
| 3 | 3.322581587822098·10⁻⁵ | 418.0149838846 |

Das nackte Leck bleibt **1/72**. Die Faktoren sind nur ungefähr gleich; die Ungleichung >418 wurde exakt anhand der Brüche geprüft. Der Ring ist ein bezeichnetes kleines Modell mit der angegebenen beibehaltenen Onsitekonstante, kein vollständiges dreidimensionales TFPT-Gitter.

## 3. Korrigierte mathematische Schlussfolgerungen

- **Diagonal bedeutet nicht unterrauminvariant.** Der Superpositionscode (Ω₀+WΩ₀)/√2 hat auf N=125 zusätzlich zum LH-Leck die elektrische Varianz 1/10000. Die allgemeine Gleichheit ohne diesen Term war zu weit.
- **Erste Beimischung bedeutet nicht vollständiger Abschluss.** Ein kleiner Rest in vier Zuständen beweist weder Minimalität noch, dass jede endliche Dressingordnung scheitert. Bei erlaubtem großen negativem Fluss ist dieselbe Beimischungsformel außerdem nicht mehr klein. Die Bestätigung gilt für das geprüfte Fenster.
- **Ein Zweizustandsmodell liefert keine exakten Volumenprozente des vollen Gitters.** Die später von Fable genannten 6,6% für L=5 und eine Abbruchschwelle bei etwa 1.500 Orten stammen aus einer isolierten 2×2-Hilfsmatrix. Unsere berechneten weiteren Materiekanäle schließen genau diese Reduktion aus. Diese Prozentangaben werden nicht als TFPT-Ergebnisse übernommen. Ebenso benötigt ein einheitlicher Duhamel-Zeitfehler die ganze Residualoperatornorm oder einen bewiesenen Trajektorienbound; eine einzelne anfängliche Leakage-Diagonale reicht nicht.
- **Teilbarkeit legt die Einheitenverteilung nicht fest.** Die positive ζ-Verteilung und die frühere einheiteninvariante μβ-Familie haben für β>1 unterschiedliche Massen in den Restklassen 1 und 3 modulo 4. Ein zusätzliches Haarmittel über die Einheiten verbindet sie. Erst der feste-Modulus-Grenzwert ist bei beiden Haar.
- **Gleiche Marginalen sind keine vollständige Zustandsidentität.** Der Haar-Grenzwert einer Vierermessung beweist nicht die Gleichheit des reinen physischen Caps mit einem ganzen KMS-Zustand. Unser ergänzender Grenzbeweis benennt deshalb die vollständige konkrete Algebra und ihren Zustand.
- **Schwache Konvergenz ist keine uniforme endliche Ressourcenschranke.** Die ζ-Grenzfolge hat für 1<β≤3 unendliche elektrische Erwartungsenergie. Die gesonderte Boxapproximation stellt den endlichen Energie-/Fehlervertrag her; sie ersetzt nicht die physische Zustandsauswahl.
- **Operatoralgebren benötigen eine Topologie.** Mit beschränkten Diagonalfunktionen und U entsteht B(ℓ²Z) im von-Neumann-Abschluss; der Normabschluss der endlichen Shiftalgebra ist kleiner. Der Carry selbst liegt bereits in der endlichen Shiftalgebra.
- **Summanden sind keine allgemeine Gate-Untergrenze.** Die N/ggT(a−1,N) Shift-Summanden einer Normalform zählen nur diese Darstellung. Eine einzelne modulare Multiplikation und eine kontrollierte Exponentiation sind verschiedene Aufgaben. Die bloße Indexreduktion |n⟩→|n modN⟩ ist außerdem kein beschränkter Hilbertraumtransfer.

Alle diese Punkte wurden mit Gegenzeugen oder allgemeinen Beweisen an Fable zurückgegeben. Die konsolidierten eigenen Berichte verwenden die korrigierten Fassungen unabhängig davon, ob eine ältere Fable-Zusammenfassung noch die ursprüngliche Formulierung enthält.

## 4. Herkunft und Abnahmegrenze

Der ursprüngliche Fable-Bericht ist auf Hash `3f131a30611f5fd5f482b422d334e0722e5a0d6d083763d7f39c8a4139b5aa90` gebunden und in `fable-arithmetik-review/` erhalten. Er dient als geprüfte historische Fassung. Die korrigierten Programme und Zahlen liegen in `fable-final/`, einschließlich unabhängiger Bestätigung, Prüfer und Hashmanifest.

Die Detailklassifikation des korrigierten Programms unterscheidet rationale Exaktrechnungen, NumPy-Stichproben und mpmath-Numerik. Im hier geprüften Zwischenstand blieben ein zu pauschaler „alles exakt“-Einleitungssatz und ein entsprechender globaler Statusname stehen. Die Konsolidierung übernimmt dieses pauschale Label nicht.

Höhere iterative Dressingstufen und andere spätere Zusatzexperimente sind nicht Bestandteil der vorliegenden unabhängigen Codebestätigung. Die hier veröffentlichten Zahlen stammen vollständig aus der abgeschlossenen ersten Stufe. Kein Resultat wird aus einem nur laufenden Versuch oder einer nicht geprüften Ausgabe abgeleitet.

Ein ergänzender Review der nächsten Fable-Fassung (`a3036e97420699cc19e5076dbf038c5f6252d1a04168c1764d089576ea00d692`) ist als `REVIEW-FABLE-ZUSATZ.md` mit eigenem Snapshot erhalten. Daraus wurde zusätzlich die einfache **elektrische Korrelation des Caps** bestätigt:

⟨T_bal⟩(t)=½[cos(20κt)+cos(4κt)], mit erster Wiederkehr bei 50π für κ=1/100.

Diese Formel gilt für die rein elektrische Entwicklung; der vollständige Parent erzeugt zusätzlich die Materiekanäle. Unter dem separat vorgegebenen arithmetischen Normfluss ist dagegen die markierte M₄-Algebra punktweise fest. Das ist eine präzise unterschiedliche Antwort beider Flüsse, keine Herleitung ihrer physikalischen Identität und keine Aussage über eine vollständige stationäre Cap-Vektorpräparation.

Der gemeinsame Beitrag besteht damit aus korrigierten konkreten Konstruktionen, reproduzierten Zahlen und ausgeschriebenen Anschlussbeweisen. Ein RH-Beweis, die vollständige TFPT-Auswahl einschließlich Gravitation oder eine neue allgemeine Faktorisierungsabkürzung wurde auch von Fable in dieser Runde nicht geliefert.
