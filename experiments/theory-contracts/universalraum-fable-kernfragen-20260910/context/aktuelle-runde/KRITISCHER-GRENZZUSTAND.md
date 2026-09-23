# Der kritische Zustand als expliziter Grenzübergang

10. September 2026. Ergänzung zu `ROTOR-BAUSTEIN.md` und kritische Konsolidierung von Fables Theorem 5. Der bekannte arithmetische Gleichgewichtszustand wird hier in der konkreten Rotor-Darstellung konstruiert. Das ist ein mathematischer Anschluss; seine Auswahl durch den physischen TFPT-Parent ist weiterhin nicht hergeleitet.

## 1. Dieselbe konkrete Operatoralgebra, eine bezeichnete Zustandsfolge

Auf ℓ²(Z) gelten U|k⟩=|k+1⟩ und S_m|k⟩=|mk⟩, m≥1. Sei A die von diesen beschränkten Operatoren erzeugte **C*-Algebra**. Für β>1 definiere den normalen Dichteoperator

ρβ = ζ(β)⁻¹ Σ_{k≥1} k⁻β |k⟩⟨k|.

Diese Folge ist auf der positiven Ladungshälfte getragen. Sie ist nicht der Gibbs-Zustand der elektrischen Energie κE²/2. Wir zeigen: Auf A existiert ein eindeutiger weak*-Grenzwert τ, obwohl ρβ keinen normalen Dichteoperatorgrenzwert auf dem vollständigen Rotorraum hat.

Betrachte die partiellen affinen Isometrien

A(a,m,n,b)=U^a S_m S_n* U^−b,   a,b∈Z, m,n≥1.

Sie bilden |nq+b⟩ auf |mq+a⟩ ab und verschwinden außerhalb dieser Restklasse. Ihr linearer Spann ist eine dichte *-Unteralgebra von A. Für den Produktnachweis seien A(a,m,n,b) und A(c,p,s,d) gegeben. Eine nichtleere Schnittmenge der Zwischenrestklassen verlangt

nq+b=pr+c.

Mit g=ggT(n,p) existiert eine Lösung genau dann, wenn g|(c−b). Alle Lösungen sind q=q₀+(p/g)t, r=r₀+(n/g)t. Das Produkt ist dann genau

A(mq₀+a, mp/g, sn/g, sr₀+d).

Bei unlösbarer Kongruenz ist es null; das Adjungierte ist A(b,n,m,a). Die Generatoren selbst sind solche Monomiale. Damit ist die benötigte Dichtheit ohne Annahme über einen größeren Operatorabschluss belegt.

## 2. Der Grenzwert jedes Monomials

Ein Diagonaleintrag des Monomials verlangt

(m−n)q=b−a.

Für m≠n gibt es höchstens einen ganzzahligen q. Sein positiver Eingangsindex liefert höchstens einen Summanden k⁻β/ζ(β), der für β↓1 gegen null geht. Für m=n und a≠b gibt es keinen Diagonaleintrag. Für m=n und a=b ist das Monomial die Projektion auf b modulo n.

Für jede feste Restklasse b modulo n ist

Σ_{k≥1, k≡b (n)} k⁻β = 1/[n(β−1)] + O(1),   β↓1.

Dies folgt unmittelbar durch Vergleich der monotonen Summe über k=r+nj mit ihrem Integral; 1≤r≤n ist der kleinste positive Vertreter. Das Integral ist r^(1−β)/[n(β−1)], und der Summenfehler bleibt beschränkt. Ebenso ζ(β)=1/(β−1)+O(1). Folglich

**τ(A(a,m,n,b)) = 1/n, falls m=n und a=b; sonst 0.**

Die Normen der Zustände sind eins. Konvergenz auf dem dichten linearen Monomialspann erweitert sich daher durch eine uniforme Normapproximation auf jedes Element von A. Der Grenzwert ist positiv, normiert und eindeutig. Dies beweist die weak*-Konvergenz der ganzen Folge β↓1, nicht nur einer ausgewählten Teilfolge.

Auf den periodischen diagonalen Funktionen ist τ das Haar-Maß auf den profiniten ganzen Zahlen: jede Restklasse modulo n hat Gewicht 1/n. Diese Aussage identifiziert eine **Einschränkung** des Zustands; sie macht keinen vollständigen physischen Cap-Zustand mit einer arithmetischen Zustandsrealisierung identisch.

## 3. Auch die arithmetische KMS-Eigenschaft lässt sich direkt prüfen

Die bekannte Normzeit auf A ist λ_t(U)=U, λ_t(S_m)=m^it S_m. Ihre Existenz als Punkt-Norm-stetige Automorphismengruppe ist die bezeichnete ax+b-Konstruktion aus Cuntz, §§3–4. Auf den Monomialen gilt

λ_t(A(a,m,n,b))=(m/n)^it A(a,m,n,b).

Für zwei solche Monomiale A und B prüft man die KMS-Gleichung bei β=1:

τ(AB)=τ(B λ_i(A))=(n/m) τ(BA).

Sind die affinen Kompositionen keine Identität auf einer Restklasse, verschwinden beide Seiten nach §2: eine von eins verschiedene Gesamtsteigung liefert höchstens einen Fixpunkt; eine reine nichttriviale Translation liefert keinen. Sind sie Identitäten, bildet A die Definitionsrestklasse von BA bijektiv auf jene von AB ab. Deren Perioden stehen im Verhältnis m/n. Die Zustandsgewichte sind die reziproken Perioden, also genau im Verhältnis n/m. Leere Definitionsbereiche geben auf beiden Seiten null. Die Gleichung gilt damit auf der dichten, λ-invarianten, aus ganzen analytischen Elementen bestehenden *-Algebra und liefert die 1-KMS-Eigenschaft.

Beispiel A=S_m, B=S_m*: τ(S_mS_m*)=1/m und τ(S_m*S_m)=1. Die erforderliche Gewichtung folgt zugleich aus den m additiven Zweigen, wie im Rotor-Bericht bewiesen.

Das reproduziert in der konkreten Darstellung den bekannten kritischen ax+b-Gleichgewichtszustand. Neu für diese Untersuchung ist der ausgeschriebene Anschluss von den verwendeten ζ-Dichteoperatoren an genau die tatsächlichen Rotor-Monomiale; keine Neuheit des bekannten KMS-Systems wird beansprucht. [Cuntz, Definition 3.1 und Proposition 4.2](https://arxiv.org/pdf/math/0611541)

## 4. Was dabei verloren geht — und was nicht identifiziert werden darf

Der Grenzzustand ist in ℓ²(Z) nicht normal. Für jedes k fallen die Restklassenprojektionen U^k S_{j!}S_{j!}*U^−k stark auf |k⟩⟨k|, während ihre τ-Gewichte 1/j! gegen null gehen. Ein normaler Dichteoperator müsste deshalb auf jedem Basiszustand Diagonalgewicht null haben; seine Spur könnte nicht eins sein. Der Grenzübergang verlagert die Beschreibung in eine andere Zustandsdarstellung. Er ist keine normale Abkühlung auf einen TFPT-Rotorgrundzustand.

Auch die Energiekosten sind konkret: Für H_E=(κ/2)E² gilt

Tr(ρβ H_E)=(κ/2) ζ(β−2)/ζ(β) für β>3,

während die positive definierende Reihe für jedes 1<β≤3 divergiert. Eine analytische Fortsetzung von ζ ersetzt hier keine positive Energiesumme. Die Zustände der betrachteten Folge haben somit in der Nähe des kritischen Punkts bereits einzeln unendliche elektrische Erwartungsenergie. Das ist kein Widerspruch zur Konvergenz auf beschränkten Observablen; es verhindert aber, diese konkrete Folge als Präparation mit endlicher elektrischer Energie auszugeben.

Die Restklassenkonvergenz gilt für jeden **festen** Modul und auf jeder festen Observablen der bezeichneten C*-Algebra. Sie ist nicht gleichmäßig über alle Moduli. Als Maß auf den profiniten ganzen Zahlen ist die diskrete ζ-Verteilung auf der abzählbaren Menge N getragen, die für das atomlose Haar-Maß Maß null hat; ihr Totalvariationsabstand zum Haar-Maß bleibt eins. Für die endlichen Restklassenmaße ist der Supremumsabstand über alle Moduli ebenfalls eins: Wähle zunächst endlich viele positive Zahlen, die beliebig viel ζ-Masse tragen, und danach einen Modul, in dem diese Menge nur einen beliebig kleinen Anteil der Restklassen besetzt.

Für β>1 stimmen ζ-Gibbs und die früher betrachtete einheiteninvariante profinite μβ-Familie **nicht** als ganze Restklassenverteilungen überein. Divisibilitätsgewichte stimmen mit m⁻β überein, bestimmen die Verteilung auf verschiedenen Einheiten aber nicht. Modulo 4 gilt für ζ-Gibbs

ωβ(1)−ωβ(3)=L(β,χ₄)/ζ(β)>0,

während Einheiteninvarianz μβ(1)=μβ(3) erzwingt. Erst im Grenzwert erhalten beide auf jedem festen Modul das Haar-Maß. Diese Korrektur betrifft Fables ursprüngliche Gleichsetzung bei endlichem β; seine konkrete Grenzidee bleibt erhalten.

Die Normzeit ist weiterhin nicht die physische elektrische Zeit. Elektrisch gilt auf |k⟩ für S_m die Frequenz (κ/2)(m²−1)k²; arithmetisch ist sie log m. Der nun konstruierte Zustandsgrenzwert begründet keinen Austausch dieser Generatoren. β=1 ist außerdem kein Beweis über die Zeta-Nullstellen auf Re(s)=1/2.

## 5. Eine nutzbare Alternative mit endlicher Energie und explizitem Fehler

Die ζ-Folge ist nicht die einzige Approximation desselben Zustands. Setze

σ_K=(2K+1)⁻¹ Σ_{k=−K}^K |k⟩⟨k|,   K≥1.

Für jedes affine Monomial aus §1 gilt unmittelbar

**|Tr(σ_K A(a,m,n,b))−τ(A(a,m,n,b))|≤1/(2K+1).**

Beweis: Ein nichttriviales affines Monomial hat höchstens einen Fixpunkt. Bei einer Restklassenprojektion weicht die Zahl ihrer Treffer in einem Intervall der Länge 2K+1 von (2K+1)/n um weniger als eins ab. Dies sind genau die Fälle aus §2. Für eine ausdrücklich gegebene endliche Anfrage O=Σ_j c_j A_j folgt daher

|Tr(σ_K O)−τ(O)|≤(Σ_j |c_j|)/(2K+1).

Damit ist die gewünschte Antwortgenauigkeit quantitativ mit einer endlichen Präparation verbunden. Beispielsweise genügt für eine solche Darstellung mit Koeffizientensumme C und gewünschtem Fehler δ die Wahl 2K+1≥C/δ. Die Zahl der Summanden, die Herstellung der Operationen und die Auswertung der Anfrage bleiben zusätzliche tatsächliche Kosten.

Jeder σ_K hat endliche elektrische Energie:

Tr(σ_K (κ/2)E²)=κK(K+1)/6.

Im tatsächlichen neutralen TFPT-Schleifensektor ersetzt man |k⟩ durch W^kΩ₀ für eine feste Plaquette p mit ∥p∥²=4. Diese Zustände sind orthonormal und erfüllen die Gaußbedingung. Die gemischte Präparation hat dort mittlere elektrische Energie 2κK(K+1)/3; die All-low-Materie liefert nur die unveränderte diagonale Erwartung ε_LN. Die Originalzustände werden nicht als stationär ausgegeben. Für die entsprechend auf diesem Schleifensektor definierten affinen Operationen gilt dieselbe Fehlerabschätzung.

Auch die Überlagerung besitzt eine ausdrückliche lokale Erweiterung auf den ursprünglichen vollen Fluxraum. Markiere einen Link e der Plaquette mit p_e=1 und setze

S_m^(p)|E⟩=|E+(m−1)E_e p⟩.

Diese Basisabbildung ist injektiv, weil die neue markierte Koordinate mE_e ist und anschließend alle übrigen Komponenten rückrechenbar sind. Ihr Bild ist genau die Restklasse E_e≡0 modulo m. Da div p=0, bleibt die Gaußbedingung für jede vorhandene Materiekonfiguration unverändert. Ferner gilt S_m^(p)W=W^mS_m^(p), und die m Bilder von W^rS_m^(p) zerlegen den ganzen Fluxraum. Auf W^kΩ₀ wirkt sie genau als k→mk. Sie ist somit eine konkrete beschränkte lokale Isometrie in der angegebenen großen Rotoralgebra. Das beweist die Operatorzugehörigkeit, nicht ihre Erzeugung mit kontrollierten Kosten aus dem Hamiltonoperator. Die einfache Energieskalierung m² gilt auf dem reinen Schleifensektor; allgemeine zusätzliche Querflüsse erzeugen Kreuzterme.

Das ist ein konkreter Anschluss mit endlichen Mitteln: Man kann festgelegte arithmetische Zustandsantworten durch tatsächliche neutrale Rotorzustände beliebig genau annähern. Die Energiekosten dieser Konstruktion wachsen für festes C wie δ⁻², und die physische Zeitentwicklung bleibt die originale. Es folgt weder ein exakt erreichter normaler KMS-Grenzzustand noch eine effiziente Lösung beliebiger Anfragen. Auch die Auswahl der Präparation und ihre Erzeugung durch erlaubte Steueroperationen werden nicht automatisch vom Parent geliefert.

## 6. Bedeutung für die gemeinsame Konstruktion

Damit ist ein bislang nur benannter arithmetischer Zustandswechsel als genauer mathematischer Grenzübergang verfügbar: positive ζ-Gewichte → affine Rotoralgebra → kritischer KMS-Zustand → gleichgewichtete endliche Restklassen. Die allgemeine Aussage ist schriftlich bewiesen. Der ergänzende diskrete Prüfer kontrolliert die affinen Produktregeln und KMS-Gewichtsidentitäten an exakt rationalen Beispielen; er ersetzt den analytischen Grenzbeweis nicht.

Offen bleibt der physische Auswahlsatz: Warum und durch welchen tatsächlichen TFPT-Prozess sollte genau diese Zustandsfolge beziehungsweise ihr nichtnormaler Grenzzustand maßgeblich werden? Der Zustand ist nun konstruiert. Seine physische Herleitung ist eine zusätzliche Behauptung, für die der derzeitige Parent noch keinen Beweis liefert.
