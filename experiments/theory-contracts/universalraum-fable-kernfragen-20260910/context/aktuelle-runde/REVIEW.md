# Unabhängiger mathematischer Review: Rotor-Baustein

10. September 2026. Reviewer: unabhängiger Teilagent `prime_chaos_atlas`. Vollständige Lektüre von `ROTOR-BAUSTEIN.md`; kein Edit am geprüften Bericht und keine Wiederholung der gesamten nativen Testsuite.

**Befund: PASS_SCOPED_MATHEMATICAL_REVIEW.** Mathematisch tragfähig innerhalb des ausdrücklich angegebenen Modells und der bedingten KMS-Auswahl. Zwei gemeldete sprachliche Präzisierungen wurden vom Autor übernommen und hier am finalen Text geprüft; es verbleibt keine Beanstandung dieses Reviews. Kein Beweis von RH, TFPT-Gesamtauswahl oder effizienter Faktorisierung wird daraus abgeleitet.

Final geprüfter Bericht SHA-256: `e4a50f6ac7dd78e32cd484d5854b08c7134333c27267daad14b8c24f43016195`.

## Prüfumfang und Quellenabgleich

- `ROTOR-BAUSTEIN.md`: vollständig gelesen und die entscheidenden Operatorgleichungen unabhängig auf Basisvektoren bzw. mit dem KMS-Randwert berechnet.
- Native `observable-dynamics/README.md`: vollständig gelesen. Bestätigt den vollen örtlichen beschränkten Rotor/CAR-Baukasten, den Selbstadjungiertheitsrahmen endlicher Volumina, die örtlichen Normgrenzen und deren korrekte fehlende Punkt-Norm-Stetigkeit auf der großen Algebra.
- Native `ground-state-loop-response/README.md`: §§1–3 und Anfang §4 gelesen; §1 bestätigt den angegebenen vollständigen Materie-Hamiltonoperator und seine Koeffizienten. Kein vollständiger Neubeweis der Grundzustandsabschätzungen.
- Historischer `round17_delta_audit.md`: Abschnitt 4 mit den Ganzzahlüberlagerungen, Gauss-Transport, unterschiedlichen Graden und physikalischer Zeitgrenze sowie der übrige angezeigte Auditkontext gelesen. Vorarbeit wird korrekt als solche bezeichnet.
- Cuntz, arXiv:math/0611541v1: Abschnitte 2–4 im Original gelesen. Definition 3.1 und Proposition 4.2 decken den verwendeten additiven Baukasten und die Existenz eines passenden 1-KMS-Zustands. Der Bericht benötigt keine stärkere allgemeine Eindeutigkeit der Zeitentwicklung. Seine eigenen Relationen verwenden die direkt beweisbare Isometriealgebra und keine unzutreffende Adjungiertenkommutation für gleiche Indizes.

Die nativen Quelldateien wurden read-only gelesen; aktuelle Kampagnen oder deren Zähler wurden nicht ausgeführt oder geändert. Literaturresultate werden als solche verwendet, nicht als neue Entdeckungen ausgegeben.

## 1. Radixform, Domains und der vollständige endliche Parent

Die euklidische Division funktioniert auch für negative Ganzzahlen mit dem angegebenen Restbereich. Daher ist V_b tatsächlich eine Basisbijektion auf den ganzen ungeschnittenen Raum. Die Verschiebungsformel berücksichtigt genau den Übertrag am obersten Rest; b-maliges Verschieben ergibt den Quotientenshift. Auch die Formel für S_m enthält den vollständigen Übertrag floor(mr/b). Der operatorielle Z₄-Verschieber L ist korrekt: am Rest 3 verschiebt U^-3 zurück innerhalb desselben Quotienten, sonst wirkt U. L ist unitär und hat Ordnung vier; es wird zutreffend von U unterschieden.

Für E und E² transportiert die Basisbijektion die maximalen diagonalen Domains exakt. Insbesondere ist der neue E²-Ausdruck der maximale diagonale Operator (bq+r)²; es wird kein formales Polynom unbeschränkter Operatoren auf einer zu kleinen Domain als ganzer Hamiltonoperator eingesetzt. Bei endlich vielen Links ist der Materieteil beschränkt und selbstadjungiert; somit bleibt die Domain des vollständigen H diejenige seiner elektrischen Basis. Unitäre Konjugation mit ausdrücklich transportierter Domain rechtfertigt die vollständige Zeitintertwining-Gleichung durch den Spektralsatz.

Die Gaussbedingungen müssen gemeinsam auf beide Register wirken. Der Bericht behauptet korrekt keine unabhängigen physischen Vierer- und Quotientenregister. CAR-Parität und Reihenfolge bleiben erhalten, da die Rotorumindizierung gerade ist und auf den Fermionen die Identität wirkt.

## 2. Unendliche örtliche Kompatibilität ist ausreichend

Für endliche X⊂Y gilt auf den örtlichen Algebren genau

    Φ_Y(A_X ⊗ I) = Φ_X(A_X) ⊗ I.

Die örtlichen unitären Konjugationen liefern damit eine isometrische *-Isomorphie der induktiven quasilokalen Algebren. Ein unendliches Hilbertraum-Tensorprodukt mit zusätzlich gewähltem Vakuum ist dazu nicht erforderlich. Die graduierte CAR-Inklusion ist unverändert.

Für die im nativen Beweis kompatibel definierten endlichen Dynamiken ist

    ||Φ α_t^Λ(A) − Φ α_t^Λ′(A)||
      = ||α_t^Λ(A) − α_t^Λ′(A)||.

Deshalb übertragen sich die dortigen lokalen Normgrenzen einschließlich kompakter Zeituniformität unmittelbar. Ebenso bleibt die fehlende Punkt-Norm-Stetigkeit erhalten. Der Bericht macht zu Recht keinen Sprung zu einem ausgewählten globalen Hamiltonoperator oder einem positivenergetischen Vakuum im unendlichen Volumen.

## 3. Die verlorene Uhrantwort ist ein gültiges Gegenbeispiel im angegebenen Umfang

Unter cE² erhält der Zustand mit festen q und Restüberlagerung 0/1 die relative Frequenz c[(4q+1)²−(4q)²]=c(8q+1). Für q=0,1 und t=π/(8c) ist die Phasendifferenz π; die beiden reduzierten Viererzustände sind orthogonal, obwohl sie anfangs identisch waren. Das widerlegt eine autonome geschlossene Viererbeschreibung dieser elektrischen Ein-Link-Dynamik. Es ist ausdrücklich kein vollständiger quantitativer Zeitvergleich aller interagierenden Materiezustände; der Text benennt die elektrische Teilkonstruktion.

## 4. KMS-Vorzeichen, endliche Gewichte und Existenz

Mit dem im Bericht verwendeten Heisenbergvorzeichen lautet die analytische KMS-Identität ω(x λ_iβ(y))=ω(yx). Setzt man x=S_m* und y=S_m, ergibt sie ω(P_m)=exp(−β ε_m). Das Vorzeichen in (5) ist somit richtig.

Weil U zeitfest ist, liegt es im Zentralisator: ω(U^r A U^-r)=ω(A). Die m vollständigen Restklassenprojektionen haben deshalb gleiches Gewicht; ihre Summe eins erzwingt ε_m=log(m)/β. Dieser Satz benötigt den ausdrücklich vorausgesetzten Eigenoperator-Ansatz und einen β-KMS-Zustand. Er beweist nicht, dass der tatsächliche elektrische Parent diese Voraussetzungen erfüllt. Die bekannte Existenz bei normiertem β=1 wird korrekt als gesondertes Literaturresultat verwendet.

Direkt erhält man für die vier Isometrien T_r=U^r S_4:

    ω(T_r T_s*) = exp(−β ε_4) ω(T_s* T_r) = δ_rs/4.

Das ist die normierte Spur auf M₄. Ihre Restriktion auf die vierdimensionalen diagonalen oder zyklischen kommutativen Unteralgebren ist gleichgewichtet. Genau diese Restriktion kann den vierdimensionalen Frobeniuszustand treffen; die ganze Matrixalgebra hat Dimension 16. Ein solcher kompatibler Zustand widerlegt keine vorangegangene, eng gefasste Gibbs-Mismatch-Aussage über einen anderen normalen Zustand.

## 5. Nichtnormalität und physische Zeitgrenze

Die Restklassen modulo j! bilden eine absteigende Folge, deren Schnitt für festen Restvertreter n innerhalb der Ganzzahlen genau {n} ist. Die zugehörigen Diagonalprojektionen konvergieren daher stark gegen |n><n|. KMS gibt die Gewichte 1/j!. Ein angenommener normaler Dichteoperatorzustand hätte folglich jeden Diagonaleintrag null und könnte nicht Spur eins haben. Der Beweis benötigt keine unbegründete Ausdehnung der Zustandsinvarianz auf sämtliche beschränkten Operatoren.

Dieser Befund betrifft Normalität in der angegebenen Rotorrepräsentation, nicht die Existenz oder Positivität des algebraischen Zustands und seiner eigenen GNS-Realisierung.

Der elektrische Generator erzeugt auf S_m die zustandsabhängige Phase c(m²−1)n². Das logarithmische Eigenoperatorgesetz ist damit auf den festgehaltenen Operationen unvereinbar. Auch U ist unter elektrischer Zeit nicht fixiert. Diese Gegenbeispiele betreffen die unveränderte elektrische Dynamik; der Bericht behauptet keinen allgemeinen Ausschluss jeder anderen, begründet erweiterten Dynamik.

## Erledigte sprachliche Präzisierungen

1. §6 nennt jetzt korrekt die 16 Matrixeinheiten T_rT_s*, statt irrtümlich von vier Matrixeinheiten zu sprechen. Die Rechnung und die Dimensionsabgrenzung waren bereits richtig.
2. §3 beschränkt den Erwartungswertsatz jetzt ausdrücklich auf beschränkte Observablen und erklärt die zusätzlichen Domain- und Existenzbedingungen für unbeschränkte Ausdrücke. Unitärer Transport bewahrt vorhandene Erwartungen; er macht einen zuvor undefinierten Ausdruck nicht definiert.

Beide Änderungen wurden am oben gepinnten Endstand nachgelesen. Die vom Root-Agenten berichteten 59 exakten Kontrollgruppen wurden in diesem unabhängigen Review nicht erneut ausgeführt. Gegenstand dieses Reviews sind die allgemeine Argumentation, ihre Voraussetzungen, die beiden nachgelesenen Änderungen und die richtige Begrenzung ihrer Aussagekraft.
