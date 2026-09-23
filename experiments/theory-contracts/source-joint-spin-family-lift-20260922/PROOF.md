# Gemeinsamer Spinor- und Familienlift aus dem TFPT-Träger

22. September 2026 · `UR.SOURCE.JOINT_SPIN_FAMILY_LIFT.01` · **PARTIAL**

## 1. Tatsächlich bearbeiteter Engpass

Der vorige Audit behandelte den internen Spin(10)-Lift des Kandidaten mit ungerader Determinantenklasse. Dieser isolierte Lift existiert über der Normal-Kugel nicht global. Im ursprünglichen E₈-Gefüge gehört der Spinor jedoch zum gemeinsamen Sektor `(16,4)`. Daher muss seine Verklebung zusammen mit dem Familienraum geprüft werden.

Das Ergebnis ist konstruktiv: Für jeden gegebenen unitären Rang-5-Träger lässt sich der gekoppelte globale Träger ohne Wahl eines Quadratwurzelbündels herstellen. Alle Standardmodell-Ladungen und die E₈-Faserprodukte bleiben erhalten. Die zulässigen natürlichen Lifts bilden jedoch eine diskrete Familie. Das kleinste Element ist bis auf Familienpermutation eindeutig, wenn zusätzlich ein bestimmtes Normminimum gefordert wird. Die Auswahl dieses Minimums aus P1 wird durch den vorliegenden Satz nicht bewiesen.

Dies bearbeitet die tatsächliche interne Feldzuordnung. Eine CAR-Quantisierung, ein Zustand und die ursprüngliche physische Zeit werden nicht eingesetzt oder als Ergebnis behauptet. Insbesondere sind keine Zielenergien 3,4,5, kein RR-Zielblock und keine Zielkovarianz Eingaben.

## 2. Warum die ursprüngliche E₈-Verklebung das Minuszeichen tragen kann

Die relevante kompakte Untergruppe ist
\[
K=\frac{\operatorname{Spin}(10)\times SU(4)}{\mathbb Z_4}.
\]
Wähle den zentralen Erzeuger \(z\) von Spin(10) so, dass er auf dem gewählten Halbspinor `16` als \(i\) wirkt. Dann kann der diagonale Kern als
\[
\langle(z,-iI_4)\rangle
\]
geschrieben werden. Er wirkt trivial auf allen Zweigen
\[
(45,1)\oplus(1,15)\oplus(16,4)
\oplus(\overline{16},\overline4)\oplus(10,6).
\]
Zum Beispiel ergeben sich auf `(16,4)` die Faktoren \(i(-i)=1\), auf `(10,6)` die Faktoren \((-1)(-1)=1\). Die konjugierte Wahl des Spinorerzeugers kehrt beide Konventionen gemeinsam um und ändert den folgenden Grad-2-Befund nicht.

Insbesondere liegt
\[
(-1,-I_4)=(z,-iI_4)^2
\]
im Kern. Ein Spin-Lift mit Endpunkt \(-1\) kann deshalb durch einen Familienpfad mit Endpunkt \(-I_4\) zu einer geschlossenen Schleife in K werden. Die bekannte globale Untergruppe wird unter anderem in Appendix A bei Distler–Sharpe hergeleitet. [Primärquelle](https://archive.intlpress.com/site/pub/files/_fulltext/journals/atmp/2010/0014/0002/ATMP-2010-0014-0002-a001.pdf).

## 3. Explizite Konstruktion und vollständige Klassifikation der betrachteten Lifts

Sei \(E\) ein unitäres komplexes Rang-5-Bündel, \(D=\det E\). Wir verlangen, dass der Spin(10)-Anteil die übliche reelle Darstellung von U(5) überdeckt. Für diese feste Projektion lässt sich die Quadratwurzel lokal auf der Doppelüberdeckung
\[
\widetilde{U(5)}=\{(g,z):z^2=\det g\}
\]
verwenden. Auf dem Halbspinor wirkt der Lift als
\[
s(g,z)|_{16}=z^{-1}\Lambda^{\rm even}g.
\]
Unter \(z\mapsto-z\) wechselt sein Vorzeichen.

Für ganze Zahlen \(m_1,\ldots,m_4\) mit
\[
\boxed{\sum_{j=1}^4m_j=-2}
\]
definiere die Familienwirkung
\[
A_m(g,z)=\operatorname{diag}
\bigl(z^{2m_1+1},\ldots,z^{2m_4+1}\bigr).
\]
Ihre Determinante ist eins. Der Wechsel \(z\mapsto-z\) multipliziert sie mit \(-I_4\). Daher ist
\[
\boxed{\iota_m(g)=[s(g,z),A_m(g,z)]\in K}
\]
von der lokalen Wurzel unabhängig und ein wohldefinierter Gruppenhomomorphismus. Er kann unmittelbar auf die U(5)-Übergangsfunktionen von E angewandt werden.

Auf `(16,4)` ergibt sich ohne gebrochene Potenzen der globale Träger
\[
\boxed{
W_m=\Lambda^{\rm even}E\otimes
\left(D^{m_1}\oplus D^{m_2}\oplus D^{m_3}\oplus D^{m_4}\right).
}
\tag{1}
Dieser hat Rang 64. Die Quadratwurzel ist im gemeinsamen Träger vollständig verschwunden.

**Klassifikationsumfang.** Dies sind bis auf Familienkonjugation alle kontinuierlichen Homomorphismen dieser Art mit festem gewöhnlichem U(5)-Spinprojektionsanteil. Denn der Lie-Algebrahomomorphismus \(\mathfrak{su}(5)\to\mathfrak{su}(4)\) muss null sein: Ein nichttrivialer Homomorphismus der einfachen Algebra wäre injektiv, was wegen \(24>15\) unmöglich ist. Die Familienwirkung faktorisiert also über den Wurzelkreis z. Seine SU(4)-Gewichte sind ganze \(\ell_j\) mit Summe null. Die erforderliche Wirkung von \(z=-1\) verlangt ungerade \(\ell_j\). Mit \(\ell_j=2m_j+1\) folgt exakt die obige Familie. Allgemeine nichtnatürliche Bündelzuordnungen, zusätzliche Materie oder andere Projektionen liegen außerhalb dieses Satzes.

**Ladungen und Produkte.** Auf dem Standardmodell-Unterträger \(S(U(3)\times U(2))\subset SU(5)\) gilt \(\det g=1\). Die Faktoren \(D^{m_j}\) haben dort keine zusätzliche Hyperladung. Deshalb enthält W genau vier Kopien der ursprünglichen 16 Ladungsgewichte. In den ursprünglichen Ganzzahleinheiten sind die Multiplizitäten
\[
(-4:12),\ (-3:8),\ (0:4),\ (1:24),\ (2:12),\ (6:4).
\]
Die ganze E₈-Verzweigung ist eine Darstellung von K. Daher sind ihre Lie-Produkte und die invariante hermitesche Form beziehungsweise Killingform unter jeder dieser Übergangsfunktionen wohldefiniert. Das ist eine Aussage über Faserprodukte und innere Produkte, noch keine CAR-Feldalgebra oder raumzeitliche Wechselwirkung.

Die Ladungsprüfung betrifft die lokale algebraische SM-Wirkung. Sie behauptet keine globale Reduktion des ungeraden E-Bündels auf ein SU(5)- oder reines SM-Hauptbündel über der Normal-Kugel; dessen Determinantenlinie ist gerade nicht trivial. Das physische Eichbündel und die Bedeutung dieser Normalgeometrie bleiben eigens abzubilden.

Auch die `4` bezeichnet hier den A₃-/SU(4)-Viererträger der E₈-Verklebung. Sie beweist keine vier physikalischen Familien. Das Original unterscheidet diese Verklebung von der SU(3)-Flavorwirkung auf dem dreidimensionalen Homologieraum (`origin_theory.tex:1210–1218`). Die physische Familienzuordnung wird durch (1) noch nicht erledigt.

Da \(c_1(\Lambda^{\rm even}E)=8c_1(E)\), ist
\[
c_1(W_m)=4\cdot8c_1(E)+16\left(\sum_jm_j\right)c_1(E)=0.
\]

## 4. Der kleinste Lift und sein genauer E₈-Sektor

Die ursprüngliche bedingte Clutching-Klasse \((c_1(E_3),c_1(E_2))=(0,1)\) bestimmt auf \(S^2\) bereits die glatte Bündelklasse. Wähle zur Rechnung den Repräsentanten
\[
E=\mathbb C^3\oplus(L\oplus\mathbb C),\qquad c_1(L)=1.
\]
Es wird keine zusätzliche physische Wahl aus der konkreten Diagonalisierung abgeleitet. Der Determinantenloop hat Grad eins. Sein gemeinsamer Lift endet auf der Überdeckung bei \((-1,-I_4)\); als K-Schleife besitzt er die Klasse
\[
2\in\pi_1(K)=\mathbb Z_4.
\]
Er ist damit nicht automatisch der Erzeuger der ursprünglichen viergradigen Clock. Einheitswindung, Liftklasse und Clockwirkung bleiben typverschiedene Daten.

Die Familiengewichte entlang der Determinantenrichtung lauten
\[
\beta_j=m_j+\tfrac12,\qquad \sum_j\beta_j=0.
\]
Jedes Quadrat ist mindestens \(1/4\). Folglich
\[
\sum_j\beta_j^2\ge1,
\]
mit Gleichheit genau für zwei Gewichte \(+1/2\) und zwei \(-1/2\). Bis auf die SU(4)-Weylgruppe bleibt genau
\[
m_A=(0,0,-1,-1).
\]
Der gemeinsame Träger ist dann
\[
\boxed{
W_A=(\Lambda^{\rm even}E)^{\oplus2}
\oplus(\Lambda^{\rm even}E\otimes D^{-1})^{\oplus2}.
}
\tag{2}

Im D₅-Faktor besitzt die primitive U(5)-Clutchingrichtung das Vektorgewicht \(e_{\rm weak}\) mit Normquadrat eins. Im A₃-Faktor ist \((1/2,1/2,-1/2,-1/2)\) ein Gewicht der `6`, ebenfalls mit Normquadrat eins. Das Paar liegt daher im `(10,6)`-Teil des originalen E₈-Gitters und hat Normquadrat zwei: **Es ist eine E₈-Wurzel.** Dieser Anschluss ist insbesondere mit dem ursprünglichen bosonischen/Higgs-Sektor verträglich.

Das Normminimum ist ein mathematisch eindeutiger Zusatzvertrag. Dass der ursprüngliche reflexionspositive Nahtkern gerade dieses Minimum auswählt, ist eine andere Behauptung und wird hier nicht aus dem Wort „primitiv“ gefolgert. Die Rahmenmarkierung und ihre Clock dürfen auch nicht nachträglich passend gewählt werden.

## 5. Warum globale Existenz die tatsächliche Quelle noch nicht auswählt

Der alternative zulässige Lift
\[
m_B=(0,0,0,-2),\qquad
\beta_B=(1/2,1/2,1/2,-3/2)
\]
hat dieselbe ursprüngliche E-Bündelklasse, dieselbe Klasse 2 in K und dieselben SM-Ladungen. Auch er erhält die vollen E₈-Faserprodukte und die invariante Fasergramform. Seine Familiennorm ist aber drei, seine gesamte E₈-Kocharakternorm vier. Beide Kocharakter sind gitterprimitiv: Ihr D₅-Vektoranteil ist \(e_{\rm weak}\), der durch keinen ganzzahligen Faktor \(k\ge2\) teilbar ist und im D₅-Gewichtsgitter bleiben kann. Gitterprimitivität unterscheidet sie somit nicht.

Die Wirkung ihrer Nahtrotation auf alle 248 Komponenten lässt sich exakt unterscheiden:

| Rotationsgewicht | −2 | −1 | 0 | +1 | +2 |
|---|---:|---:|---:|---:|---:|
| Lift A | 1 | 56 | 134 | 56 | 1 |
| Lift B | 14 | 64 | 92 | 64 | 14 |

Insbesondere sind die invarianten Spuren des quadrierten Generators 120 beziehungsweise 240. Die Homomorphismen sind daher auch nicht durch eine E₈-Konjugation identisch. Diese Werte sind **Rotations-/Darstellungsdaten, keine berechneten ursprünglichen physikalischen Zeitenergien**.

Eine zweite, genau begrenzte Gegenprobe zeigt, dass dieselbe Topologie auch nicht denselben geladenen Differentialoperator festlegt. Man versieht die Normal-Kugel für beide Kandidaten mit derselben Standardkomplexstruktur \(\mathbb{CP}^1\) und den entsprechenden holomorphen Linien \(L=\mathcal O(1)\). Dann gilt
\[
W_A=\mathcal O(-1)^{16}\oplus\mathcal O^{32}\oplus\mathcal O(1)^{16},
\]
\[
W_B=\mathcal O(-2)^8\oplus\mathcal O(-1)^8\oplus
\mathcal O^{24}\oplus\mathcal O(1)^{24}.
\]
Beide komplexen Bündel sind glatt von Rang 64 und Grad null; ihre holomorphen Strukturen und zugehörigen Chern-Verbindungen unterscheiden sich. Mit derselben räumlichen Spinlinie \(\mathcal O(-1)\) haben die verdrehten Spin-Diracoperatoren
\[
\dim\ker D_A=16+16=32,\qquad
\dim\ker D_B=24+24=48.
\]
Dies folgt exakt aus \(h^0(\mathcal O(k-1))=\max(k,0)\) und \(h^1(\mathcal O(k-1))=\max(-k,0)\). Der chirale Index ist beide Male null. Diese Gegenprobe prüft ausschließlich die behauptete Eindeutigkeit aus Bündelklasse, Ladungen und Faserprodukten; **sie ist kein Vorschlag einer neuen physischen Kugelzeitquelle und kein Original-TFPT-Spektrum**. Ihr Entscheidungskriterium ist bereits erfüllt: Diese Daten allein bestimmen die geladene Differentialantwort nicht eindeutig.

## 6. Abgleich mit dem tatsächlichen Minimalitätsprinzip

Die Originalarchitektur enthält den gemeinsamen Quotienten ausdrücklich (`tfpt_1_architecture_e8.tex:5325–5336`) und die Normzerlegung des `(10,6)`-Sektors (`5338–5364`). Der ältere Higgs-Clutching-Satz (`_archive/paper-latex/tfpt-42.tex:3900–3978`) gibt die weak-Determinantenklasse an. Er identifiziert deren Kocharakter jedoch nicht mit dem A₃-Gewicht \(\lambda_2\). Auch die primitive K¹-Nahtklasse (`2319–2355`) allein enthält diese Information nicht.

Die originale Minimalität darf hier nicht verkürzt werden: Neben Spektralfluss, Rang und Determinantenklasse enthält sie eine Randnullität. Ein solcher Term könnte grundsätzlich zwischen verschiedenen Lifts unterscheiden, selbst ohne ausdrückliches Normquadrat. Um ihn auszuwerten, braucht man aber den **tatsächlichen** Randoperator auf dem **tatsächlichen** gemeinsamen Feldraum.

Die operative Quellfassung `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:480–520` beginnt bereits mit
\[
(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,[u_\Sigma],\mathcal D_{\rm coll}).
\]
Die Algebra, Zeitwirkung, Zustand und der elliptische Collar-Generator sind dort Eingaben. Aus dem gewählten Collar-Generator soll der tangentiale Operator \(B_\Sigma\) folgen. Seine reduzierte Nullität wird erst danach gezählt (`543–558`). Ein Rekonstruktionssatz nach Lieferung dieses Datensatzes ist noch keine Auswahl genau eines solchen Datensatzes aus der Nahtwindung.

Die oben berechneten Kugel-Dirackerne 32 und 48 dürfen deshalb nicht in den Originalterm \(\dim\ker B_\Sigma\) eingesetzt werden. Sie betreffen andere, ausdrücklich deklarierte Operatoren. Das bloße Fehlen einer Norm in der Defektliste wäre für sich allein ebenfalls kein Beweis gegen jede indirekte Auswahl durch \(B_\Sigma\).

**Eng begrenzte Zusatzkontrolle.** Für die in Abschnitt 5 ausdrücklich gewählten Standard-Chernverbindungen auf \(\mathcal O(k)\) hat der Äquator die Holonomie \((-1)^k\). Ein tangentialer Kreis-Dirac hat dort Frequenzen \(n+k/2+\epsilon\), mit gemeinsamem räumlichem Spinversatz \(\epsilon=0\) oder \(1/2\). Beide W-Kandidaten besitzen 32 gerade und 32 ungerade Liniengrade. Ihre gesamten Kreisspektren sind daher gleich: 32 Kopien des ganzzahligen und 32 des halbzahligen Gitters. Die unaufgelöste Randnullität entscheidet diese Gegenprobe nicht.

Die **nach Ladungen aufgelöste** Antwort unterscheidet sie hingegen. Im ursprünglichen Ladungskanal \(6Y=6\) hat Lift A zwei positive und zwei negative Äquatorholonomien, Lift B vier negative. Dies benennt eine kleine konkrete Vergleichsgröße für einen tatsächlich hergeleiteten geladenen Quelloperator. Es ist keine Behauptung, die Originalquelle besitze eine dieser Holonomien oder ihr Operator sei dieser Äquator-Dirac.

## 7. Die bereits vorhandenen E₈-Korrelatoren werden nicht neu als Herkunft ausgegeben

Der Korpus besitzt bereits die vollständige bedingte Gitterfeldantwort. Für den Gewicht-1-Wurzelstrom im gewählten Kreisvertrag lautet sie
\[
G_{R,a}(\tau)=\frac{e^{a\tau/R}}{4R^2\sinh^2(\tau/(2R))},\qquad\tau>0,
\]
einschließlich eines positiven Spektralmaßes und neutraler Mehrpunkt-Vertexwörter. Quelle: `experiments/theory-contracts/source-local-line-20260920/LOCAL_LIMIT_REVIEW.txt`, insbesondere Abschnitte 1–4. Die geladene Spinorkomponente des reinen E₈-Gitters hat \(h=5/8+3/8=1\), ist also ein bosonisches Stromfeld. Der neue gemeinsame Bündellift macht daraus kein CAR-Fermion.

Ebenso wurde die direkte Umdeutung des unveränderten Stromtensors in einen lokalen gleichen-Feld-Weyl-Yukawaterm bereits geprüft (`source-flavor-origin-20260920/PROOF.txt`, Abschnitt 2): Der antisymmetrische interne Koeffizient trifft auf das symmetrische Lorentzskalarbilinear und verschwindet in genau dieser Lesart. Das ist kein neuer Ausschluss dieser Fortsetzung und keine Widerlegung der algebraischen Flavor-Ausgaben. Andere Feldslots oder Lorentzstrukturen brauchen einen eigenen Herkunftsnachweis.

Die Originalzeile `SEAM.EQUIV.01` im maßgeblichen Ledger bleibt offen: Die Rohnaht ist noch nicht unbedingt als dasselbe E₈-Netz mit demselben Zustand und derselben Zeit rekonstruiert. Die neue globale K-Konstruktion bearbeitet ein konkretes Hindernis auf diesem Weg; sie darf den offenen Pfeil nicht durch Einsetzen des bekannten Zielkorrelators ersetzen.

## 8. Verifikationsumfang

`checker.py` benutzt ausschließlich rationale Gewichte, Außenalgebra-Indizes und exakte Multiplizitäten. Es kontrolliert den diagonalen Z₄-Kern, die Schließung aller 248 Verzweigungskomponenten, die unveränderten Ladungen, beide Rotationsspektren, die E₈-Normidentität und die beschriebenen Kohomologieformeln. Normaler Python-Lauf und `-OO` liefern identische Ergebnisse. Die allgemeinen Existenz- und Klassifikationsaussagen beruhen auf den oben ausgeschriebenen Argumenten, nicht auf einer endlichen Enumeration.

Der entscheidende verbleibende Herkunftsschritt lautet: Welcher der gekoppelten Lifts wird vom tatsächlichen Nahtkern samt markierter Familienclock und Transfer induziert? Falls das Wurzelminimum aus diesem Kern folgt, ist (2) der konkrete interne Träger. Anschließend müssen dessen Feldalgebra, Zustand und physische Zeit vorwärts gewonnen werden. Der vorliegende Satz schließt die globale interne Konsistenz dieses Kandidaten; er schließt die vollständige geladene Quellenfrage oder T1–T8 nicht.

Firewall: Forschungscontract unter `experiments/`; keine Paper-, Ledger-, Website- oder empirische Promotion.
