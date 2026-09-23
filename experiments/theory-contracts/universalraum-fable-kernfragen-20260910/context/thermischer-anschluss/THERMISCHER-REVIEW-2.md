# Unabhängige Prüfung des thermischen Anschlusses: Graph und quantitative Fehler

10. September 2026. Geprüfter Bericht: `THERMISCHER-ANSCHLUSS.md`, SHA-256 `203a4ce4756331b6b1922dfd0450d8a00ef41e6278eeaebf19831344a45015a2`. **Die Graphkonstruktion, der Poissonrest, die über einzelne Anfragen uniforme Fehlerschranke und das rationale Temperaturrezept sind korrekt.** Dieser Review konzentriert sich auf diese algebraischen und quantitativen Schritte; der separate Kollege prüft die funktionalanalytische Gibbs-/Häufungspunktseite.

## 1. Ganze Gauss-Hilbertspace und primitive Koordinate

Die drei übrigen Plaquettenkanten bilden für L≥5 einen einfachen Pfad. Nach Entfernen des vierten Links e bleibt der Torusgraph zusammenhängend. Jeder Wald in einem verbundenen endlichen Graphen lässt sich zu einem Spannbaum erweitern; damit existiert genau der verlangte Baum ohne e und mit diesem Dreikantenpfad. Der Fundamentalzyklus zu e ist die ausgewählte Plaquette, nach Wahl der Orientierung mit p_e=1.

Die integrierte Gaussquelle jeder N-Teilchen-Materiemaske ist null. Eine ganzzahlige Lösung lässt sich entlang des Baumes routen, also mit f_e=0. Die Fundamentalzyklen der übrigen Nichtbaumkanten haben sämtlich e-Komponente null. Fundamentalzyklen liefern eine **ganzzahlige** Basis des ganzzahligen Zyklenkerns, keine bloße reelle Parametrisierung: Ihre Koeffizienten liest man an den jeweils eigenen Nichtbaumkanten ab; nach deren Abzug bleibt ein zyklusfreier Baumfluss und damit null.

Somit ist E=f+qp+Bz eindeutig und vollständig. Insbesondere ist q=E_e eine primitive ganzzahlige Koordinate ohne Kongruenzrestriktion. Die Dimension d=3N−N+1=2N+1 und D=binom(2N,N) stimmen. Für die hier gemeinten m,n≥1 sind q→mq Isometrien mit der üblichen Teilbarkeitsdomäne ihrer Adjungierten. W und S_m erhalten die Gaussbedingung, weil sie nur einen ganzzahligen Zyklenfluss hinzufügen.

Jeder Fundamentalzyklus besteht aus einer Nichtbaumkante und einem einfachen Baumpfad, besitzt also höchstens N Kanten mit Koeffizienten ±1. Deshalb gilt tr(B*B)≤2N². Die volle Gram-Matrix ist positiv definit, und ihr Schurkomplement ist strikt positiv und höchstens p*p=4. Das reicht für alle folgenden Konstanten; ein orthogonaler ganzzahliger Zykluswechsel wird nicht vorausgesetzt.

## 2. Störungsnorm und Poissonkonstante

Auf dem physikalischen Sektor gibt es genau N Fermionen. Da die Onsitewerte zwischen 0 und 4 liegen, beträgt deren Operatornorm höchstens 4N. Mit dem zuvor unabhängig geprüften Hopbound folgt C_N=(4+101/192)N=869N/192. Der Bound betrifft den gesamten physikalischen Raum und benötigt keine all-low-Einschränkung.

Für k=d−1 Z-Koordinaten liefert Poisson zur Gewichtung exp(−βκ z*G_z z/2) den dualen Exponenten −2π² l*G_z^−1 l/(βκ). Aus λ_max(G_z)≤tr G_z≤2N² folgt l*G_z^−1 l≥||l||²/(2N²). Damit ist die Konstante c=π²/(κN²) in (5) konservativ richtig. Verschiebungen und Kreuzterme verändern nur die dualen Phasen, deren Betrag eins ist; der Rest ist deshalb uniform in q und der Materiemaske.

Die eindimensionale Schurkoeffizient ist a=κ·Schur(G)/2≤2κ. Die Abschätzung j²≥1+3(j−1) für j≥1 und das Produkt über k Dualkoordinaten ergeben genau den angegebenen R. Es fehlt weder ein Faktor zwei im Exponenten noch ein Dimensionsfaktor.

## 3. Alle Moduli gleichzeitig – mit dem richtigen Anfrageumfang

Für die verschobene Gaußfunktion g ist TV(g)=2 und sup g=1. Die Rechteckregel auf dem gesamten ganzzahligen Gitter hat daher Fehler höchstens zwei. Für eine Restklasse wird sie auf h(x)=g(r+mx) angewandt; TV(h)=2 und das Integral ist I/m. **Der Fehler bleibt zwei unabhängig von m.** Nach Normierung mit Z≥I−2 ergeben sich 1/(I−2) für ein Atom und (2+2/m)/(I−2)≤4/(I−2) für eine einzelne Restklasse.

Die relative Poissonkorrektur (1+e(q)) mit |e|≤R<1 ändert eine normierte Verteilung in l1 um höchstens 2R/(1−R). Die tatsächlichen positiven Mischungsgewichte der Materiemasken können unverändert benutzt werden; man muss sie nicht ebenfalls approximieren. Die Bounds bleiben deshalb im vollständigen Maskengemisch gültig.

Die affine Operation hat für m≠n höchstens einen festen Basiswert. Er existiert genau bei (n−m)|(a−b) und ist dann q=b+n(a−b)/(n−m). Im ersten Bericht stand noch „genau einen“; das war beispielsweise für (a,m,n,b)=(1,2,4,0) falsch. Der gepinnte Endstand enthält die korrekte Bedingung. Der Fehlerbound benötigte ohnehin nur „höchstens einen“ und bleibt unverändert. Für m=n ist die Diagonale entweder null oder die bezeichnete Restklassenprojektion.

Somit ist (7) tatsächlich uniform über die einzelnen normbeschränkten affinen Grundoperationen. Das bedeutet **keine** uniforme Kontrolle über beliebige Mengenvereinigungen oder Linearkombinationen mit unbeschränkter Koeffizientensumme. Die ausdrücklich genannte Grenze zur profiniten Totalvariation ist richtig. Für jede feste endliche Linearkombination folgt die Behauptung mit dem l1-Koeffizientenfaktor; anschließend erlaubt der Zustandsnormbound den Übergang zum Normabschluss.

## 4. Vollständige Algebra des rationalen Rezepts

Für 0<ε≤1 ergeben die drei rationalen Schranken in (8) jeweils:

1. 4βC_N≤ε²/9, also Gibbs-Störungsfehler höchstens ε/3.
2. I0>12/ε+2 wegen π>3, also Einzelrestklassenfehler höchstens ε/3.
3. y≤βκN²/9≤ε/(48d). Aus y≤1/2 folgt 2y/(1−y³)≤3y. Mit k=d−1 und 3ky<1 gilt (1+3y)^k≤1/(1−3ky), etwa durch die binomische/geometrische Reihe. Daraus folgen R≤ε/(16−ε) und 2R/(1−R)≤ε/(8−ε)≤ε/7.

Die Summe ist sogar höchstens 17ε/21<ε. Sämtliche benötigten Nenner sind positiv, und I0>2 sowie R<1 sind durch dasselbe Rezept gesichert. Die Aussage „Genauigkeit mindestens ε“ ist entsprechend als **Fehler höchstens ε** zu lesen. β kann beispielsweise als das Minimum der drei positiven rationalen Werte gewählt werden; dafür ist keine numerische Auswertung von π oder exp nötig.

`THERMISCHER-REVIEW-2-CHECKS.json` ergänzt den Beweis um 351 exakte Kontrollen: die rationalen Rezeptschritte für zwei zulässige Volumina und vier Genauigkeiten sowie sämtliche affinen Fixpunktfälle mit a,b∈{−2,…,2}, m,n∈{1,…,4}, m≠n. Es wurden keine breiten Graphkampagnen wiederholt und keine Originale verändert.

**Akzeptierter positiver Anschluss:** Der vollständige endliche H-Gibbszustand reproduziert im gewählten Hochtemperaturgrenzgang die angegebenen kritischen Antworten auf der Loop-affinen Algebra, mit expliziter endlicher Einzelanfragen-Fehlerschranke. Die Wahl dieses Grenzgangs, seine physische Präparation, der Energieaufwand und die Identifikation arithmetischer Normzeit mit physikalischer Zeit bleiben eigenständige Voraussetzungen bzw. offene Fragen. Das Ergebnis liefert für sich keinen schnellen Faktorenleser oder globalen RH-Satz.
