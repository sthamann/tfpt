# Unabhängiger Review des kritischen Grenzzustands

10. September 2026. Reviewer: unabhängiger Teilagent `prime_chaos_atlas`.

**Befund: PASS_SCOPED_MATHEMATICAL_REVIEW.** Der allgemeine Grenzbeweis, die bedingte KMS-Prüfung und die ergänzte Approximation mit endlicher elektrischer Energie sind mathematisch korrekt. Es wurde keine tragende Lücke gefunden. Die Existenz der bezeichneten Normzeit bleibt das ausdrücklich genannte bekannte Literaturresultat; ihre Identität mit physischer TFPT-Zeit wird nicht behauptet.

Geprüfte Endstände:

| Datei | SHA-256 |
|---|---|
| `KRITISCHER-GRENZZUSTAND.md` | `bd24c782557c01d0f0d6eb11c7fe30198c488a500e1d95137ff32905bdce5a2d` |
| `check_critical_state.py` | `55e6d183fcdbb6f1a32d78c67996da103457bfd4f3c394600c6a46b2285d22b0` |

Der Bericht und der aktualisierte Checker wurden vollständig gelesen, die nachgereichten Abschnitte über Energie/Topologie, die endliche Boxapproximation und die konkrete lokale Loop-Isometrie ausdrücklich mitgeprüft. Die gespeicherten Beweis-/Checkerpins stimmen. Eine erneute Ausführung des Checkers mit ausschließlich im Speicher abgefangenem Dateischreiben reproduziert das gespeicherte Ergebnis: 144 Monomiale, 20.736 geordnete Paare, Produkt-/Adjunktions-/KMS-Kontrollen sowie die Boxfehler- und Energiekontrollen bestehen. Beweis, Checker und Ergebnisdatei blieben dabei unverändert. Die folgenden allgemeinen Argumente tragen die Schlussfolgerung; die endliche Zahl von Kontrollen tut das nicht allein.

## 1. Konkrete Algebra und CRT-Produkt

Ein Monomial A(a,m,n,b) sendet die ganze Restklasse nq+b auf mq+a. Für das Produkt mit A(c,p,s,d) lautet die Anschlussbedingung nq−pr=c−b. Der angegebene ggT-Test und die Parametrisierung aller ganzzahligen Lösungen sind richtig, auch für negative Verschiebungen und negative Eingangsindizes. Die Ausgangs- und Eingangsperioden werden dadurch mp/g und sn/g, mit den im Bericht angegebenen Offsets.

Das adjungierte Monomial vertauscht Ein- und Ausgangsdaten. Identität, U, U*, S_m und S_m* gehören zum Spann. Damit ist dieser Spann tatsächlich eine *-Unteralgebra, deren Normabschluss genau C*(U,S_m) ist. Es wird kein unzulässiger Sprung zu B(ℓ²(Z)) oder einem von-Neumann-Abschluss benötigt. Unterschiedliche Parametrisierungen derselben partiellen Abbildung sind unproblematisch: Die Zustandsformel wird als Grenzwert tatsächlicher Operatorerwartungen hergeleitet und ist daher unabhängig von der gewählten Schreibweise.

## 2. Allgemeiner schwacher Zustandsgrenzwert

Die Dichteoperatoren ρβ sind für β>1 positiv und haben auf ℓ²(Z) Spur eins. Die Fixpunktgleichung (m−n)q=b−a liefert genau die drei im Bericht unterschiedenen Fälle. Ein einzelner positiver Fixpunkt trägt ein Gewicht k^−β/ζ(β), das gegen null geht. Eine nichttriviale Translation hat keinen Fixpunkt. Eine Restklassenprojektion hat hingegen unendlich viele positive Diagonaleinträge.

Für den kleinsten positiven Restvertreter r gilt der elementare Integralvergleich

    ∫₀∞(r+nx)^−β dx ≤ Σ_{j≥0}(r+nj)^−β
      ≤ r^−β + ∫₀∞(r+nx)^−β dx.

Der Integralwert ist r^(1−β)/(n(β−1)). Für festes n,r ist r^(1−β)=1+O(β−1), und der Summenfehler bleibt beschränkt. Die Restklassensumme hat deshalb genau den Polkoeffizienten 1/n. Mit dem entsprechenden Vergleich für ζ ergibt sich die behauptete Monomialformel δ_(m=n,a=b)/n.

Die Erweiterung von der dichten Unteralgebra ist ebenfalls gerechtfertigt: Zustände sind gleichmäßig normbeschränkt durch eins. Für ein beliebiges A wählt man ein festes Monomialpolynom P mit ||A−P||<ε. Die unbekannten Grenzwertdifferenzen auf A kosten höchstens 2ε zusätzlich zu der bereits bewiesenen Konvergenz auf P. Dadurch existiert der Grenzwert auf jedem A; Positivität, Linearität und Normierung gehen auf ihn über. Das beweist Konvergenz der ganzen Familie β↓1 in σ(A*,A), nicht nur die Existenz eines Teilnetzgrenzwerts.

Die Haar-Aussage ist korrekt als Einschränkung auf C(Ẑ), den Abschluss periodischer Diagonalobservablen. Sie ist keine Identifikation des ganzen Zustands mit einer rein kommutativen Wahrscheinlichkeitsverteilung.

## 3. Direkte KMS-Identität und deren Fortsetzung

Mit der angenommenen Normzeit ist jedes affine Monomial ein ganzes analytisches Eigenoperator-Element. Das analytische Gewicht bei t=i ist n/m, nicht m/n. Somit lautet die richtige Gleichung

    τ(AB) = τ(B λ_i(A)) = (n/m)τ(BA).

Die allgemeine Periodenbegründung hält auch bei leeren Definitionsbereichen. Haben beide Kompositionen Gesamtsteigung ungleich eins, sind ihre Fixpunktmengen höchstens endlich und beide τ-Werte null. Bei Gesamtsteigung eins sind die Translationsanteile durch die positive Steigung von A miteinander verknüpft: Ist einer nicht null, ist es auch der andere. Ist BA auf einer nichtleeren Restklasse die Identität, bildet A diese Restklasse bijektiv auf die Definitionsrestklasse von AB ab. Daher kann nicht eine Identitätskomposition einseitig leer sein.

Für eine zusätzliche arithmetische Kontrolle des Periodenverhältnisses schreibe m=ut, n=vt mit ggT(u,v)=1. Identitätssteigung verlangt mp=ns, also p=vw, s=uw. Die beiden ggT-Werte sind v·ggT(t,w) beziehungsweise u·ggT(t,w). Aus der CRT-Produktformel ergibt sich damit genau

    Periode(AB)/Periode(BA) = u/v = m/n.

Die reziproken Periodengewichte liefern folglich den KMS-Faktor n/m. Dieser Beweis ist nicht auf die im Checker gewählten kleinen Indizes begrenzt.

Die Fortsetzung auf die ganze Algebra ist zulässig. Für zwei Monomialpolynome ist die Streifenfunktion eine endliche Summe ganzer Exponentialfunktionen. Auf beiden Streifenrändern sind ihre Beträge aufgrund der KMS-Gleichheit durch das Produkt der Operatornormen beschränkt. Normapproximation und der Drei-Linien-Satz liefern die entsprechende beschränkte holomorphe Funktion für beliebige Algebraelemente. Die dichte, zeitinvariante analytische Unteralgebra reicht deshalb für die vollständige 1-KMS-Bedingung aus.

Die Existenz der Punkt-Norm-stetigen Automorphismengruppe auf der konkreten ax+b-Algebra wird ausdrücklich aus dem bekannten Cuntz-Modell übernommen. Der Grenzbeweis setzt weder einen logarithmischen Hamiltonoperator auf dem vollen Rotor-Hilbertraum noch eine Identifikation mit dem elektrischen Hamiltonoperator voraus.

## 4. Nichtnormalität, elektrische Energie und Topologie

Die Restklassen modulo j! fallen für festen Vertreter k stark gegen die Einpunktprojektion |k><k|. Ihre τ-Gewichte 1/j! gehen gegen null. Jeder angenommene normale Dichteoperator für τ hätte daher sämtliche Diagonaleinträge null und könnte nicht Spur eins haben. Das beweist Nichtnormalität in genau dieser Darstellung, ohne die Existenz des positiven algebraischen Zustands oder seiner eigenen GNS-Realisierung in Frage zu stellen.

Die zusätzliche Energieaussage ist richtig: Die positive Summe für Tr(ρβE²) ist ζ(β−2)/ζ(β) ausschließlich für β>3 und divergiert für 1<β≤3. Analytische Fortsetzung der Zetafunktion berechnet dort keine Erwartungsenergie. Diese Grenze betrifft die angegebene ζ-Familie; sie ist kein allgemeiner Ausschluss von Approximationen mit endlicher Energie.

Auch der Totalvariationsbefund stimmt, mit der üblichen Abstandskonvention d_TV=sup_B|μ(B)−ν(B)|. Die abzählbare positive Ganzzahlmenge trägt die ganze diskrete ζ-Masse, aber keine Haar-Masse auf Ẑ. Der Abstand ist daher eins. Für die endlichen Restklassen verteilt man eine zunächst gewählte endliche Menge mit fast voller ζ-Masse auf einen hinreichend großen Modul. Diese Menge beansprucht dort beliebig wenig Haar-Masse; deshalb bleibt das Supremum über alle Moduli ebenfalls eins.

Die Korrektur der endlichen β-Verteilungen ist plausibilitätsunabhängig direkt sichtbar: Die Differenz zwischen den Restklassen 1 und 3 ist eine Summe positiver Paardifferenzen (4j+1)^−β−(4j+3)^−β, normiert mit ζ. Eine einheiteninvariante Verteilung muss diese beiden Restklassen dagegen gleich gewichten. Aus den angegebenen Divisibilitätsgewichten zusammen mit Einheiteninvarianz folgt beim Grenzübergang β↓1 wieder die uniforme Verteilung auf jedem festen Modul.

## 5. Endliche Energie und quantitativ kontrollierte Antworten

Für die uniforme Box σ_K zählt die Spur eines affinen Monomials dessen ganzzahlige Fixpunkte innerhalb des Intervalls. Ein Nichtprojektionsmonomial hat höchstens einen solchen Punkt. Eine Restklasse hat entweder floor((2K+1)/n) oder ceil((2K+1)/n) Treffer. Damit ist die Schranke 1/(2K+1) je Monomial exakt gerechtfertigt, unabhängig von dessen Indizes.

Für O=Σ_j c_jA_j folgt durch die Dreiecksungleichung die angegebene Schranke C/(2K+1), C=Σ_j|c_j|. Ihre Abhängigkeit von einer tatsächlich gegebenen Darstellung ist wesentlich: Eine gute Operatornorm allein liefert nicht automatisch eine kleine Koeffizientensumme. Die je Monomial uniforme Schranke widerspricht deshalb nicht dem fehlenden uniformen Totalvariationsgrenzwert; kompliziertere Vereinigungen von Restklassen können beliebig viele Summanden benötigen.

Die exakte Summe der Quadrate ergibt

    (2K+1)^−1 Σ_{k=−K}^K k² = K(K+1)/3.

Somit sind κK(K+1)/6 für einen Link und 2κK(K+1)/3 für den viergliedrigen Plaquettenstrom richtig. W^kΩ₀ sind orthonormal und Gauss-neutral. Die All-Low-Materie trägt nur die unveränderte diagonale Erwartung ε_LN bei; die aus dem früheren Quellenbeweis bekannten LH-Austritte machen diese Präparation nicht stationär.

Die Wachstumsaussage δ^−2 beschreibt eine hinreichende Energieaufwendung dieser konkreten Wahl K≈C/(2δ) bei festem C. Sie ist keine bewiesene optimale Komplexitätsuntergrenze für die Anfrage. Die Erzeugung der Mischung, die Realisierung der Operationen und die Auswertung bleiben gesonderte Kosten.

Die affine Operation auf dem neutralen Loopsektor kann sogar ausdrücklich innerhalb der vorhandenen großen lokalen Feldalgebra fortgesetzt werden: Für einen markierten Link e mit p_e=1 definiert

    S_m^(p)|E⟩ = |E+(m−1)E_e p⟩

eine lokale Isometrie. Die inverse Teilung ist genau dann möglich, wenn m den neuen Wert E_e teilt. Da div p=0 gilt, bleibt Gauss unverändert. Weiter gilt S_m^(p)W=W^mS_m^(p), und auf E=kp wirkt sie als k→mk. Dies bestätigt den in §5 bezeichneten affinen Loop-Anschluss, ohne aus bloßer Operatorzugehörigkeit Steuerbarkeit oder elektrische Normzeit abzuleiten.

## Endurteil

Der Bericht liefert einen echten konstruktiven Zustandsanschluss: allgemeine schwache Konvergenz auf der konkreten Algebra, direkte KMS-Prüfung unter der ausgewiesenen Normzeit und eine alternative Approximation mit endlicher Energie und benanntem Fehler. Die physische Auswahl durch TFPT, die Gleichsetzung beider Zeitgeneratoren und irgendeine RH- oder Faktorisierungslösung bleiben zutreffend ausdrücklich offen.
