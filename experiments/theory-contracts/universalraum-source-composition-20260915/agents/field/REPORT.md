# v1.6.9: Ein minimaler Lorentz-Auslesekanal mit Impuls

## Ergebnis

Die gemischthändige Feldfrage wurde konstruktiv weitergelöst. Für den
sechsdimensionalen Träger `(1,1/2)` existiert mit **genau einem zusätzlichen
Lorentzvektor p** eine explizite Auslese in einen linken Weylspinor.
Innerhalb dieser Polynomialklasse ist sie bis auf Normierung eindeutig;
ohne p ist sie unmöglich. Ihr Rang ist bei jedem von null verschiedenen p
exakt zwei, auch auf dem Lichtkegel.

Die zusätzliche Struktur ist dabei wesentlich. Für zeitartiges p lässt
sich der frühere gleichhändige Projektor kovariant auf den gemischthändigen
Träger übertragen. Für lichtartiges p bleibt die Auslese wohldefiniert,
aber eine nur von p abhängige kovariante rechte Inverse existiert nicht.
Ein zweiter zeitartiger Bezugsvektor q ermöglicht eine solche Inverse.

Der vorgezogene Kinetiktest liefert einen weiteren konkreten Befund:
Wird das Komposit aus einem freien masselosen selbstdualen Feld und einem
freien masselosen Weylfeld gebildet, verschwindet diese Ableitungsauslese
auf deren Bewegungsgleichungen identisch. Die richtige Darstellung allein
erzeugt somit noch keinen nichtverschwindenden Weyl-Pol.

**Status:** Konstruktion und Gegenprüfungen exakt; native Herkunft von p,
q, Feldadapter und Kinetik offen. Es wurde kein räumlicher Träger als aus
W hergeleitet ausgegeben. Alle neuen Dateien liegen ausschließlich in
diesem Arbeitsstrang.

## 1. Präzise zusätzliche Eingabe

Seien V und V̄ die beiden fundamentalen Weylräume. Der neue Vertrag setzt
explizit

\[
 T\in\operatorname{Sym}^2V\otimes\bar V=(1,1/2),
 \qquad P\in V\otimes\bar V=(1/2,1/2).
\]

Für reellen Impuls verwenden wir

\[
 P=\begin{pmatrix}p_0+p_3&p_1-ip_2\\p_1+ip_2&p_0-p_3\end{pmatrix},
 \qquad \det P=p_0^2-\mathbf p^2.
\]

Unter M∈SL(2,C) gilt `P→M P M†` und
`T→(Sym²M⊗M*)T`. Die letztere Gleichung ist ein **angenommener Lorentzadapter**
für das Komposit. Der interne Spin(10)-Spinor und der Lorentzspinor sind
verschiedene Faktoren.

Eine echte Feldadjunktion vertauscht linke und rechte Weyldarstellungen.
Ein bloßer Fock-Erzeuger ist dagegen noch kein Feld mit diesen Indizes:
Eine Weylfeldentwicklung enthält sowohl Vernichtungs- als auch Erzeugungsterme
mit passenden Spinorwellenfunktionen. Beide Unterschiede bleiben erhalten;
siehe [Dreiner, Haber und Martin, Abschnitte 2 und 3.1](https://arxiv.org/pdf/0812.1594#page=24).

## 2. Explizite Auslese und Minimalität

Mit ε als alternierender Form lautet die Auslese

\[
 (C_PT)^\alpha=\sum_{\beta,\dot\gamma,\delta,\dot\epsilon}
 T^{\alpha\beta\dot\gamma}\,
 \varepsilon_{\beta\delta}\varepsilon_{\dot\gamma\dot\epsilon}
 P^{\delta\dot\epsilon}.
\]

In der bisherigen unnormierten Reihenfolge
`(00,dot0),(00,dot1),(01,dot0),(01,dot1),(11,dot0),(11,dot1)` und für
`P=[[a,b],[c,d]]` wird daraus die unmittelbar ausführbare Matrix

\[
 C_P=\begin{pmatrix}
 d&-c&-b&a&0&0\\0&0&d&-c&-b&a
 \end{pmatrix}.
\]

Der neue Prüfer zeigt sämtliche sechs infinitesimalen Lorentz-
Intertwining-Gleichungen und vier endliche Transformationen einschließlich
Boost und komplexer Nullrotation. Insbesondere gilt exakt

\[
 C_{MPM^\dagger}(\operatorname{Sym}^2M\otimes\bar M)=M C_P.
\]

Ohne Impuls hat das lineare Intertwining-System auf den zwölf möglichen
Auslesekoeffizienten Rang zwölf: Der Kern ist null. Mit einem Impulsfaktor
hat es auf 48 Koeffizienten Rang 47: Der Lösungsraum ist eindimensional.
Dies bestätigt die Darstellungssumme

\[
 (1/2,1/2)\otimes(1,1/2)
 =(3/2,1)\oplus(3/2,0)\oplus(1/2,1)\oplus(1/2,0).
\]

Die Zielkomponente tritt genau einmal auf. Die Minimalität gilt für
**eine lokale lineare Auslese, polynomial in einem einzigen unabhängigen
Impuls bis zum angegebenen Grad**. Zwei unabhängig zugängliche
Konstituentenimpulse oder zusätzliche Felder erweitern den Vertrag.

## 3. Exakte Ränge und Kerne

Vier Zweierminoren von C_P sind `d²,c²,b²,a²`. Deshalb ist der Rang für
jede von null verschiedene komplexe Matrix P exakt zwei, unabhängig
von `det P`. Alle folgenden Aussagen sind symbolische Identitäten,
keine numerischen Rangschätzungen.

| Impuls | Rang C_P | Kerndimension | Kovarianter Rückweg nur mit P |
|---|---:|---:|---|
| P=0 | 0 | 6 | Nein |
| Zeitartig, P²>0 | 2 | 4 | Explizit vorhanden |
| Lichtartig, P≠0 und P²=0 | 2 | 4 | Exakt ausgeschlossen |
| Raumartig, P²<0 | 2 | 4 | Algebraisch vorhanden; keine positive massive Interpretation behauptet |

Bei `P=m I` sind die Kerngleichungen `T0+T3=0`, `T2+T5=0`.
Eine Basis ist `e1,e4,e0−e3,e2−e5`. Für den Lichtkegelrepräsentanten
`P=diag(1,0)` lautet die Auslese `(T3,T5)` und der Kern
`span(e0,e1,e2,e4)`. Die Indizes sind hier nullbasiert.

### Zeitartiger Rückweg

Eine kovariante Einsetzung ist

\[
 (J_P\chi)^{\alpha\beta\dot\gamma}
 =\chi^\alpha P^{\beta\dot\gamma}+\chi^\beta P^{\alpha\dot\gamma},
 \qquad
 J_P=\begin{pmatrix}
 2a&0\\2b&0\\c&a\\d&b\\0&2c\\0&2d
 \end{pmatrix}.
\]

Die tragende Identität lautet

\[
 C_PJ_P=3\det(P)I_2.
\]

Für `det P≠0` ergeben sich damit

\[
 R_P=\frac{J_P}{3\det P},\qquad
 \Pi_P=\frac{J_PC_P}{3\det P},\qquad
 C_PR_P=I_2,\quad\Pi_P^2=\Pi_P,\quad\operatorname{rank}\Pi_P=2.
\]

Dies verbindet die neue Rechnung unmittelbar mit dem eingefrorenen
gleichhändigen Adapter C_alt,R_alt aus v1.6.8. Für
`S_P=I_3⊗(P εᵀ)` prüft das Programm exakt

\[
 C_P=C_{\rm alt}S_P,\quad
 R_P=S_P^{-1}R_{\rm alt},\quad
 \Pi_P=S_P^{-1}\Pi_{\rm alt}S_P.
\]

Der Impuls liefert also die fehlende Umwandlung des gepunkteten Faktors.
Auf dem zukünftigen zeitartigen Kegel existiert zusätzlich ein positives,
impulsabhängiges Tensor-Skalarprodukt, bezüglich dessen Π_P selbstadjungiert
ist. Es entsteht aus den positiven Faktoren `P⁻¹,P⁻¹,P̄⁻¹`; die Kovarianz
und Selbstadjungiertheit sind geprüft. Dies ist ein positives Skalarprodukt
auf den vorgeschriebenen Impulsfasern, noch keine positive Feldkinetik.

### Was auf dem Lichtkegel scheitert

Bei `det P=0` gilt weiterhin `rank J_P=2`, aber `C_PJ_P=0`.
Der Zähler `J_PC_P` hat Rang zwei und sein Quadrat ist null. Er ist
somit kein Projektor; der massive Ausdruck lässt sich nicht durch bloßes
Einsetzen von P²=0 fortsetzen.

Es fehlt auch nicht nur diese besondere Formel. Für `P=diag(1,0)` fixieren
reelle und imaginäre Nullrotationen den Impuls. Ein kovarianter Rückweg
R müsste beide intertwinen. Subtraktion dieser beiden Gleichungen erzwingt
`(I_3⊗E)R=0`, wobei `E=[[0,1],[0,0]]`. Zugleich faktorisiert C_P durch
`I_3⊗E`; deshalb wäre `C_PR=0`, im Widerspruch zu `C_PR=I_2`.
Das vollständige endliche Gleichungssystem hat Koeffizientenrang zehn
und augmentierten Rang elf. Dies beweist: **Kein linearer Lorentz-
kovarianter Rückweg auf den ganzen Weylraum kann am Nullimpuls nur von P
abhängen.** Ein gewöhnlicher, durch Basiswahl fixierter Rückweg existiert
natürlich, besitzt aber nicht diese Kovarianz.

## 4. Ein expliziter Rückweg mit zusätzlicher Referenz

Ein zweiter Lorentzvektor Q erlaubt

\[
 K_{P,Q}=C_PJ_Q=\sigma I_2+Q\operatorname{adj}P,
 \qquad\sigma=\operatorname{tr}(Q\operatorname{adj}P),
\]

\[
 \det K_{P,Q}=2\sigma^2+\det(P)\det(Q),\qquad
 R_{P,Q}=J_Q K_{P,Q}^{-1}.
\]

Für ein zukünftiges Null-P und ein zukünftiges zeitartiges Q ist σ>0,
also ist der Rückweg endlich. Bei `P=diag(1,0), Q=I` lautet er konkret

\[
 R_{P,Q}=\begin{pmatrix}
 2&0\\0&0\\0&1/2\\1&0\\0&0\\0&1
 \end{pmatrix},\qquad C_PR_{P,Q}=I_2.
\]

Wenn P **und** Q transformiert werden, gilt die volle Lorentz-Kovarianz.
Q kann zum Beispiel einen Beobachter oder eine Präparationsreferenz
beschreiben. Diese zusätzliche Referenz ist aber ein echter Eingang;
ihre Existenz oder Verfügbarkeit wird nicht aus W gewonnen.

Die lokale erste Ableitung C_P darf außerdem nicht mit ihrem Rückweg
verwechselt werden. Die Division durch P² beziehungsweise durch
impulsabhängige Ausdrücke ist im Ortsraum im Allgemeinen nichtlokal.
Auf einer vorgegebenen massiven Massenschale ist P²=m² konstant; diese
Massenschale wäre wiederum eine zusätzliche Kinetikaussage.

## 5. Früher Kinetiktest auf genau diesem Auslesekanal

Die Rang-zwei-Auslese liefert einen Spinor mit zwei komplexen Komponenten.
Die masselose Weylgleichung ist dadurch noch nicht erfüllt. Für nullartiges
P legt `adj(P) C_PT=0` eine weitere unabhängige lineare Bedingung fest.
Der erlaubte T-Unterraum hat dann Dimension fünf, sein Auslesebild
Dimension eins. Das ist zunächst nur eine algebraische Feldgleichungs-
bedingung und keine vollständige Einteilchen-Konstruktion.

Noch entscheidender ist der Test des tatsächlich vorgeschlagenen
Produkts \(T^{\alpha\beta\dot\gamma}=F^{\alpha\beta}\bar\psi^{\dot\gamma}\). Für freie masselose
Konstituenten seien

\[
 P_F=\lambda\bar\lambda^T,\quad
 P_\psi=\mu\bar\mu^T,\quad
 F=\lambda\lambda^T,\quad\bar\psi=\bar\mu.
\]

Beide Impulse sind nullartig. Der Prüfer behandelt alle acht
Spinorkomponenten als unabhängige Symbole und zeigt die Polynomidentität

\[
 \boxed{C_{P_F+P_\psi}(F\otimes\bar\psi)=0.}
\]

Die reale physikalische Einschränkung folgt durch komplexe Konjugation
der gepunkteten Partner. Der Beweis ist zugleich die Leibnizregel:
Der Ableitungsterm auf F verschwindet durch dessen freie Feldstärke-
gleichung, der Term auf ψbar durch dessen freie Weylgleichung.
Die Identität gilt auch für nichtkollineare Impulse. Ein expliziter
Fall besitzt sogar den zeitartigen Gesamtimpuls `P_F+P_ψ=I` und liefert
trotzdem Auslese null.

Damit ist ein klarer positiver Anschlussauftrag übrig: Ein **nichtnuller**
physischer Spinor aus diesem Kanal braucht eine berechnete massive,
wechselwirkende oder außerhalb der Massenschale liegende Quelle, eine
andere Kinetik oder einen anderen ausdrücklich festgelegten Feldadapter.
Ein eingeschobener freier Feldstärke-/Weyl-Vertrag würde an diesem Test
scheitern. Das ist kein Ausschluss des nativen Modenmodells, dessen
Lorentzkinetik noch gar nicht festgelegt ist.

## 6. Ladung und die zwei verschiedenen Komposita

Im nativen U(1)-Vertrag besitzen `f,b` die Ladungen −1,−2 und ihre
Adjungierten +1,+2. Daher gilt unverändert

| Operator | N-Ladung | Bei wörtlicher Feldzuordnung |
|---|---:|---|
| D∼b f† | −1 | Wenn b in (1,0) und f† in (0,1/2), dann gemischthändig; der neue Impulsadapter ist anwendbar |
| χ†∼b†ηf† | +3 | Bei adjungiertem b und f ist `(0,1)⊗(0,1/2)` gleichhändig; der konjugierte alte Algebraadapter ist möglich |
| Impuls oder Ableitung | 0 | Ändert keine dieser Ladungen |

### Die Zuordnung muss zusätzlich den ursprünglichen Vertex bestehen

Die vorige Tabelle ist eine bedingte Fallunterscheidung und noch keine
gemeinsame Lorentz-Deutung des Hamiltonoperators. Fordert man zusätzlich,
dass f **wörtlich ein linkes Weylfeld** ist und `b†ff` ohne Ableitung ein
Lorentzskalar wird, dann muss das als b† bezeichnete **Feld** selbst den
Typ (1,0) tragen. Die Spin-1-Darstellung ist zu ihrer algebraischen
Dualdarstellung äquivalent. Ihre skalare Paarung ist in der symmetrischen
Basis

\[
 \eta_3=\begin{pmatrix}0&0&1\\0&-2&0\\1&0&0\end{pmatrix};
 \qquad L^T\eta_3+\eta_3L=0.
\]

Alle drei Generatorgleichungen werden geprüft. Dagegen besitzt
`(0,1)⊗(1,0)=(1,1)` keinen Skalar; das entsprechende lineare
Invariantensystem hat Rang neun auf neun Koeffizienten.

Unter dieser **zusätzlichen wörtlichen Vertexbedingung** vertauscht
sich die Benennung der zwei Fälle:

- `b†` ist links, sein adjungiertes Feld `b` rechts;
- `D=b f†` ist damit **gleichhändig rechts**. Der konjugierte alte
  C/R-Adapter liest einen rechten Spinor aus;
- `χ†=b†ηf†` ist **gemischthändig** und wird durch den hier konstruierten
  Impulsadapter in einen linken Spinor ausgelesen.

Eine rechte Kompositquelle kann zur rechten Seite einer Weylgleichung
`sigma-bar·partial ψ = Quelle` passen. Diese Kinetik muss allerdings
erst auf derselben Konstruktion gezeigt werden. Umgekehrt führt die
oben angesetzte Wahl `b` selbst links, bei wörtlicher Adjunktion, zu
einem gemischten D, aber nicht zu einem skalaren nackten `b†ff`-Vertex.

Diese zusätzliche Prüfung verhindert, das Feldwörterbuch isoliert an
einem Komposit zu reparieren und dabei den ursprünglichen Vertex zu
verlieren. Da Fock-Modenkoeffizienten nicht bereits vollständige lokale
Felder sind, ist damit keine konsistente Moden-Feld-Abbildung ausgeschlossen.
Sie muss ihre Komponenten und Adjungierten ausdrücklich angeben.

Die innere Metrik η vertauscht keine Lorentzhändigkeit. Die beiden
Komposita haben gleiche Ladung **modulo vier**, aber verschiedene
U(1)-Ladungen, Fockwirkungen und gegebenenfalls Lorentztypen.
Ein neutraler Ableitungsfaktor macht sie nicht identisch. Der frühere
Z4-erhaltende zusätzliche Hamiltonkanal kann sie koppeln; das ist eine
explizite Dynamikerweiterung.

Eine unabhängige Weylkomponente passender Händigkeit und Ladung oder
eine konsistente ladungskonjugierte Feldabbildung bleibt eine Alternative.
Sie muss jedoch mit den nativen CAR, Ladungen und W-Kontraktionen
vereinbar konstruiert werden. Eine punktierte Komponente durch reine
Notation in eine unpunktierte umzubenennen ist kein solcher Adapter.

## 7. Konkrete Voraussetzungen für die globale Quell-Komposition

Die Kompositionssuche erhält aus dieser Rechnung unabhängige, früh
prüfbare Anforderungen — keinen bereits hergeleiteten Raum:

1. **Feldindexvertrag:** Den genauen Operator mit U(1)-Ladung und
   gepunkteten/ungepunkteten Indizes festlegen und zugleich den
   skalaren Vertex einschließlich Adjunktion prüfen. Bei gleicher Händigkeit
   genügt algebraisch der alte C/R-Adapter. Bei gemischter Händigkeit
   wird mindestens ein zusätzliches Lorentzvektorobjekt benötigt.
2. **Herkunft von P:** Falls P aus der Komposition stammen soll, muss
   die Quelle ein neutrales Vierervektor-/Ableitungsobjekt und dessen
   Lorentztransformationsgesetz liefern. Innere 64/60-Labels,
   Bosonzahl, Clock oder ein bloßer Graphabstand erfüllen diese
   Gleichungen nicht durch ihre Bezeichnung. Ein translationsartiger
   Ansatz benötigt darüber hinaus seine konkreten Generatoren.
3. **Gemeinsamer Operator:** Auf derselben Konstruktion die oben
   angegebene C_P-Matrix anwenden und die Intertwining-Gleichung
   einschließlich Boosts prüfen. Am Lichtkegel dürfen Auslese und
   kovarianter Rückweg nicht gleichgesetzt werden; ein Rückweg
   verlangt die nachgewiesene zusätzliche Referenz.
4. **Nichtnulltest nach Kinetik:** Vor jeder Pol- oder Teilchenbehauptung
   das konkrete Matrixelement des Ableitungskomposits berechnen. Der
   freie masselose Produktansatz liefert hier exakt null. Eine
   erfolgreiche Alternative muss diesen Test sichtbar bestehen.
5. **Verbindung zum geladenen nativen Pol:** Referenzzustand, N-Ladung,
   Dispersions-/Massenschalenannahme und spektrales Gewicht müssen
   dieselben sein. Die innere endliche Auslese beweist diese
   Verbindung nicht automatisch.

Die endliche Quell-Kompositions- und Ablaufprüfung kann parallel dazu
fortschreiten. Ein fehlendes P verbietet ihre innere Algebra nicht;
es verhindert nur, diesen Stand schon als vollzogenen gemischthändigen
Lorentz-Ausleseadapter auszugeben.

## Reproduktion und Quellenumfang

```sh
python3 -B replay.py
```

Der eigenständige Lauf benötigt Python und SymPy. Er prüft vier
eingefrorene Quellenpins und **85 exakte Bedingungen je Modus**.
Es gibt keine numerischen Prüfbedingungen. Normal und `-OO` müssen
byte-identische JSON-Dateien liefern; Warnungen gelten als Fehler,
und keine Bedingung verwendet abschaltbare Assertions.

Die v1.6.8-Auslesematrizen werden direkt aus dem eingefrorenen JSON
eingelesen und mit der neuen Konstruktion verbunden. Die frühere
gesamte Feldsuite wird nicht nochmals ausgeführt. Die vollständigen
Matrizen, Rangzeugen und Quellenpins stehen in `results.normal.json`,
die aktuellen Programm- und Ergebnishashes im `replay_manifest.json`.
