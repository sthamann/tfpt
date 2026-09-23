# Was Komposition über Primzahllängen beweist

Prüfung der Abschnitte 3, 4, 11, 12 und 17B des Anhangs vom 10. September 2026. **Der logarithmische Längensatz lässt sich vollständig beweisen. Seine zusätzliche Voraussetzung ist die gewöhnliche Größenordnung der Zahlen. Komposition allein lässt dagegen jede Primlänge frei.** Das ist eine Präzisierung des Forschungsprogramms, keine neue RH-Lösung.

## 1. Vollständige Klassifikation

Sei \(\tau:\mathbb N_{>0}\to\mathbb R\) mit

\[
\tau(mn)=\tau(m)+\tau(n)\quad\text{für alle }m,n\ge1.
\]

Dies heißt **vollständig additiv**; bloße Additivität in der Zahlentheorie verlangt die Gleichung nur für teilerfremde Faktoren.

**Satz.** Genau diese Funktionen haben die Form

\[
\boxed{\tau(n)=\sum_{p\text{ prim}}v_p(n)a_p,\qquad a_p\in\mathbb R\text{ beliebig}.}
\]

**Beweis.** \(\tau(1)=2\tau(1)\) ergibt \(\tau(1)=0\). Induktion liefert \(\tau(p^r)=r\tau(p)\). Die eindeutige Primfaktorzerlegung \(n=\prod_pp^{v_p(n)}\) ergibt die Formel mit \(a_p=\tau(p)\). Umgekehrt gilt \(v_p(mn)=v_p(m)+v_p(n)\); deshalb erfüllt jede Wahl der Gewichte die Kompositionsgleichung. Für jedes einzelne \(n\) ist die Summe endlich. ∎

Nichtnegative Längen sind äquivalent zu \(a_p\ge0\); strikt positive Längen für alle \(n>1\) zu \(a_p>0\). Monotonie **unter Teilbarkeit** liefert ebenfalls nur \(a_p\ge0\).

Das konkrete Gegenbeispiel \(a_p=1\) ergibt \(\tau(n)=\Omega(n)\), die Anzahl der Primfaktoren mit Vielfachheit. Es ist vollständig additiv und für \(n>1\) positiv, aber

\[
4<5,\qquad\tau(4)=2>1=\tau(5).
\]

Folglich erzwingen weder Komposition noch Positivität die Längen \(\log p\). Auch eine abstrakte freie kommutative Prozessstruktur unterscheidet ihre Erzeuger zunächst nicht kanonisch: Jede Permutation der Erzeuger ist ein Monoidautomorphismus.

## 2. Welche Zusatzannahme den Logarithmus erzwingt

**Satz.** Ist \(\tau\) zusätzlich nicht fallend in der **gewöhnlichen Zahlenordnung**, also \(m\le n\Rightarrow\tau(m)\le\tau(n)\), dann

\[
\boxed{\tau(n)=c\log n,\qquad c=\tau(2)/\log2\ge0.}
\]

Ist \(\tau\ne0\), so ist \(c>0\). Umgekehrt erfüllen alle diese Funktionen beide Bedingungen.

**Vollständiger Beweis.** Aus \(1\le2\) folgt \(\tau(2)\ge0\). Fixiere \(n\ge2\). Für jedes positive ganze \(k\) setze

\[
b_k=\lfloor k\log_2n\rfloor.
\]

Dann \(2^{b_k}\le n^k<2^{b_k+1}\). Monotonie und vollständige Additivität geben

\[
\frac{b_k}{k}\tau(2)\le\tau(n)
\le\frac{b_k+1}{k}\tau(2).
\]

Beide Grenzen konvergieren zu \(\tau(2)\log_2n\); sogar

\[
|\tau(n)-\tau(2)\log_2n|\le\tau(2)/k.
\]

Also gilt die Behauptung für jedes \(n\ge2\), ebenso für \(n=1\). Bei \(c=0\) verschwindet \(\tau\) identisch; damit folgt die Nichttrivialitätsaussage. Der Rückweg ist die gewöhnliche Logarithmusregel samt Monotonie. ∎

Es wurde weder RH noch eine Aussage über die Verteilung der Primzahlen verwendet. Der Satz ist bekannt; Erdős bewies 1946 sogar die Variante unter der schwächeren, nur teilerfremden Additivität. Unser Potenzbeweis betrifft ausschließlich den hier benötigten vollständig additiven Fall. [Erdős, Theorem XI, S.17–18](https://www.renyi.hu/~p_erdos/1946-06.pdf).

**Folge für Abschnitt 4:** „Natürliche additive Größe“ muss um die Ordnungsvoraussetzung ergänzt werden. Exakt \(\log p\) statt \(c\log p\) benötigt außerdem eine Normierung, etwa \(\tau(2)=\log2\). Eine physikalische Zeit in Sekunden ist damit noch nicht identifiziert. Das Zahlenmonoid und seine Größenordnung sind bereits arithmetische Eingaben; eine TFPT-Herleitung müsste diese Struktur unabhängig erzeugen.

## 3. Was eine Primorbitliste tatsächlich liefert

Angenommen, alle primitiven Orbits sind bijektiv durch gewöhnliche Primzahlen bezeichnet, genau einer pro \(p\), mit Länge \(\ell_p=\log p\); verwendet werde die ungewichtete Orbit-Zeta. Dann gilt für \(\sigma=\Re s>1\)

\[
\log Z(s)=\sum_p\sum_{r\ge1}\frac{p^{-rs}}r,
\qquad Z(s)=\prod_p(1-p^{-s})^{-1}=\zeta(s).
\]

**Konvergenzbeweis:** Die absolute Doppelsumme ist höchstens
\((1-2^{-\sigma})^{-1}\sum_p p^{-\sigma}\), also endlich. Die endlichen Eulerprodukte expandieren mittels eindeutiger Faktorisierung in die entsprechenden Dirichletreihen; absolute Konvergenz erlaubt den Grenzübergang. Ebenso

\[
-Z'(s)/Z(s)=\sum_{p,r\ge1}(\log p)p^{-rs}.
\]

Der Faktor \(\log p\) entsteht hier exakt beim Differenzieren. Dass er in dieser Formel erscheint, ist daher kein ungeklärtes Phänomen. Die analytische Fortsetzung von \(\zeta\) kann anschließend als bekannter Satz übernommen werden. Eine **geometrische** Fortsetzung, eine passende Spektralidentität und eine unabhängige RH-Grenze folgen aus der Orbitliste nicht.

**Explizite Unterbestimmtheit:** Nimm die disjunkte Vereinigung der Kreise \(\mathbb R/(\log p)\mathbb Z\) und gleichförmige Translation. Jeder Kreis ist genau ein primitiver Orbit der gewünschten Periode. Der Koopmanfluss auf der direkten Summe ihrer \(L^2\)-Räume ist unitär. Sein selbstadjungierter Generator hat auf Kreis \(p\) Eigenwerte \(2\pi k/\log p\), \(k\in\mathbb Z\), insbesondere einen unendlichdimensionalen Nullraum. Seine Resolvente ist nicht kompakt. Damit sind die Perioden und Unitarität realisiert, ohne die benötigte Riemann-Nullstellen-Determinante zu liefern. Diese Konstruktion widerlegt keine RH; sie zeigt die fehlende Schlussverbindung des vorgeschlagenen Ansatzes.

## 4. Präzisierung der übrigen Abschnitte

**Abschnitt 3:** Für eine endliche Matrix gilt
\(-\log\det(I-uT)=\sum_{n\ge1}u^n\operatorname{Tr}(T^n)/n\)
formal und bei genügend kleinem \(|u|\) analytisch. Die Spur zählt Wege nur bei entsprechend konstruierten Übergangsoperatoren; sonst liefert sie gewichtete Antworten. Im unendlichen Fall braucht eine Determinante zusätzliche analytische Voraussetzungen. „Primitive Prozesse“ sind bei nichtkommutativen Wegen nicht automatisch gewöhnliche Primzahlen.

**Abschnitt 11:** Die K4-Formel ist korrekt. Nach ausdrücklich entferntem trivialem Faktor bleiben \(1+u+2u^2\) und die Wurzeln \((-1\pm i\sqrt7)/4\), jeweils mit \(|u|^2=1/2\). Das begründet die konkrete graphische RH. Eine endliche Gegenprobe oder gescheiterte Abschätzung schließt jedoch nur den genau geprüften Ansatz aus, nicht alle künftigen endlichen Abschätzungsverfahren.

**Abschnitt 12:** Orbitlängen sind eine notwendige Spezifikation dieses konkreten Eulerprodukt-Ansatzes, kein vollständiger geometrischer Bauplan. Zusätzlich fehlen korrekte Vielfachheiten, Gewichte, archimedischer Anteil, Definitionsbereiche und globaler Spur-/Positivitätssatz. Berry–Keating benennen bereits Unterschiede der Amplituden und Vorzeichen; die rohe Primreihe auf der kritischen Linie divergiert. [Berry–Keating 1999, Gl.(2.6), (2.17)–(2.18)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf).

Positive gemischte Zyklen sind ein enger Ausschluss: Für \(K=\begin{psmallmatrix}ax&by\\cx&dy\end{psmallmatrix}\), \(x=p^{-s},y=q^{-s}\), enthält \(\operatorname{Tr}K^2/2\) den Term \(bc\,xy\). Bei unabhängigen positiven Gewichten ohne Kompensation passt dessen Länge \(\log(pq)\) nicht in die Primzahlpotenzliste von \(\log\zeta\). Das schließt dieses gekoppelte Modell aus; komplexe oder graduierte Kompensationen wurden damit nicht ausgeschlossen.

**Abschnitt 17B:** „Keinen Beweis gefunden“ ist kein Widerlegungstest. Ein belastbarer negativer Test benötigt einen Widerspruch, einen Gegenzeugen oder einen Nicht-Existenzsatz unter festgelegten Voraussetzungen. Endlich viele passende Primlängen beweisen umgekehrt keine vollständige Orbitidentifikation: Für eine Primzahl \(q\) oberhalb jedes geprüften Inputs stimmt \(\tau_q(n)=\log n+v_q(n)\log2\) dort exakt mit \(\log n\) überein, verletzt aber die Größenmonotonie bei \(q<q+1\), denn \(\log(2q)>\log(q+1)\). Die präzise offene Aufgabe lautet: **Erzeugt die Quelle intrinsisch eine mit dem geordneten Zahlenmonoid kompatible Prozessstruktur und die richtige vollständige arithmetische Antwort?**

## Quellen- und Prüfbereich

Der Nutzeranhang wurde vollständig gelesen; bewertet wurden die beauftragten Abschnitte. Erdős' Originaldefinition, Theorem-XI-Ankündigung und Beweisschluss S.17–18 wurden gelesen; der einfachere Potenzbeweis oben ist vollständig ausgeschrieben. Berry–Keatings Originalstellen zu Konvergenz und Orbitamplituden wurden live abgeglichen. Bost–Connes' Original \(H\epsilon_n=(\log n)\epsilon_n\), S.32–33, bestätigt einen bekannten arithmetisch strukturierten Dynamikfall, keine Herleitung aus unmarkierter Komposition. [Bost–Connes 1995](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf). Die K4- und Mixed-Cycle-Identitäten wurden mit dem vorhandenen vollständigen Transferbeweis abgeglichen. Klassifikation, Sandwichbeweis und Kreiskonstruktion sind mathematische Ableitungen, keine behaupteten neuen Literaturresultate oder TFPT-Beweise.
