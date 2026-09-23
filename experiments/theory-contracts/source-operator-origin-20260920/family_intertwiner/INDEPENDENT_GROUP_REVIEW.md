# Unabhängige Gruppenprüfung des Familien-Intertwiners

**Prüfumfang:** feste vollständige Produktgruppenwirkung
\(\operatorname{Spin}(10)\times SU(4)\) auf
\[
V=\overline{16}\otimes\bar 4,\qquad
V'=\overline{16}\otimes 4.
\]

**Ergebnis:** Es gibt weder einen von null verschiedenen komplex-linearen
noch einen von null verschiedenen komplex-antilinearen Gruppenintertwiner
\(V\to V'\). Der bisherige familienreine Antilinearitätskandidat prüft nur
den \(SU(4)\)-Faktor und ist auf dem komplexen Tensorprodukt nicht
wohldefiniert.

**Umsetzungsnachtrag:** Die unten beanstandete Vorversion wurde anschließend korrigiert. Die spätere Verstärkung auf die gesamte Operatoralgebra und der Clifford-Folgetest liegen außerhalb dieses unabhängigen Reviews.

## 1. Linearer Intertwiner

Sei \(z_F=iI_4\) der erzeugende Zentralcharakter von \(SU(4)\). Dann wirkt
\(z_F\) auf \(\bar4\) mit \(-i\) und auf \(4\) mit \(+i\). Für einen linearen
Intertwiner \(T\) müsste daher gelten
\[
T(-iv)=+i\,T(v).
\]
Wegen der Linearität ist die linke Seite \(-iT(v)\). Somit ist
\[
2i\,T(v)=0
\]
für jedes \(v\), also \(T=0\).

Dieser Zentralcharaktertest reicht bereits aus. Er stimmt mit dem im
vorhandenen Prüfer gefundenen Rang 16 des linearen
\(\bar4\to4\)-Gleichungssystems überein.

## 2. Antilinearer Intertwiner

Sei \(z_S\) ein Erzeuger des \(\mathbb Z_4\)-Zentrums von
\(\operatorname{Spin}(10)\). In der festgelegten Orientierung wirke er auf
\(\overline{16}\) mit \(+i\). Quelle und Ziel tragen denselben
\(\overline{16}\)-Faktor, also wirkt \(z_S\) auf beiden Räumen mit \(+i\).

Für einen antilinearen Intertwiner \(A\) müsste
\[
A\bigl(\rho_V(z_S)v\bigr)=\rho_{V'}(z_S)A(v)
\]
gelten. Die beiden Seiten sind jedoch
\[
A(iv)=-iA(v),\qquad
\rho_{V'}(z_S)A(v)=+iA(v).
\]
Damit folgt wieder \(A=0\).

Die Aussage hängt nicht von der Orientierung des Zentralgenerators ab.
Beim inversen Erzeuger wirkt auf beiden \(\overline{16}\)-Faktoren \(-i\);
Antilinearität konjugiert diese Phase zu \(+i\), während das Ziel weiterhin
\(-i\) verlangt. Auch dann ist \(A=0\).

Äquivalent gilt
\[
\operatorname{Hom}_{\operatorname{Spin}(10)\times SU(4)}
\bigl(\overline V,V'\bigr)
=
\operatorname{Hom}
\bigl(16\otimes4,\overline{16}\otimes4\bigr)=0.
\]
Ein antilinearer Intertwiner \(V\to V'\) wäre genau ein linearer Intertwiner
\(\overline V\to V'\). Der Spinor-Zentralcharakter schließt ihn aus.

## 3. Fehler im familienreinen Kandidaten

Die Vorschrift
\[
I_{\overline{16}}\otimes K_4:
s\otimes f\longmapsto s\otimes\overline f
\]
definiert über \(\mathbb C\) keine Abbildung auf dem Tensorprodukt. Denn
\((is)\otimes f=s\otimes(if)\), aber die beiden Darstellungen desselben
Tensors würden abgebildet auf
\[
is\otimes\overline f
\quad\text{beziehungsweise}\quad
s\otimes\overline{if}=-is\otimes\overline f.
\]
Sie widersprechen sich für ein nicht verschwindendes Bild.

Globale Koeffizientenkonjugation ist dagegen wohldefiniert, konjugiert aber
beide Faktoren:
\[
\overline{\overline{16}\otimes\bar4}=16\otimes4.
\]
Sie landet daher nicht in
\(\overline{16}\otimes4\).

Damit ist auch die Formulierung, Koeffizientenkonjugation halte den
Spin(10)- beziehungsweise Hyperladungsanteil unverändert, als
Gruppenaussage falsch. In einer reellen diagonalen Cartanbasis können die
notierten Eigenwerte formal gleich aussehen; die zugehörige
Gruppenwirkung ist \(e^{i\theta H}\), und Antilinearität konjugiert die
Phase zu \(e^{-i\theta H}\). Sie kehrt somit die entsprechende
\(U(1)\)-Ladung um.

## 4. Bewertung des vorhandenen Prüfers

Die Prüfungen des \(SU(4)\)-Faktors sind für sich korrekt:
Koeffizientenkonjugation identifiziert antilinear \(\bar4\) mit \(4\), und
der lineare Intertwinerraum ist null. Der Schluss auf einen antilinearen
Intertwiner des vollständigen Produktmoduls ist jedoch ungültig, weil der
\(\operatorname{Spin}(10)\)-Zentralcharakter nicht geprüft wird.

Insbesondere reichen die folgenden Befunde nicht aus, um den
Gruppenintertwiner zu erhalten:

1. das Negieren der drei Familiengewichte bei unveränderten notierten
   D5-Gewichten;
2. die Erhaltung der numerisch ausgewerteten Hyperladungswerte in dieser
   Gewichtsliste;
3. die algebraische Konstruktion support-disjunkter Tensoren \(W_D\),
   \(J_D\) und \(C_{3,D}\).

Diese Rechnungen können eine zusätzliche formal transformierte Kopie
beschreiben. Sie liefern keine lineare oder antilineare Abbildung zwischen
den beiden angegebenen Darstellungen bei fester vollständiger
Produktgruppenwirkung.

## 5. Gültiger enger Scope

Der Ausschluss gilt für das festgehaltene Dictionary mit unveränderter
\(\operatorname{Spin}(10)\times SU(4)\)-Wirkung auf Quelle und Ziel. Er ist
kein allgemeines Verbot anderer Mechanismen.

Insbesondere nicht ausgeschlossen sind:

- ein ausdrücklich definierter \(SU(4)\)-Außenautomorphismus-Twist, der
  die Zielwirkung selbst ändert;
- eine gleichzeitige Konjugation des Spin(10)-Spinors mit entsprechend
  anderem Zielmodul;
- ein anderes globales Gruppenquotient- oder Ladungsdictionary, dessen
  tatsächlich wirkende Zentraluntergruppe neu geprüft wird;
- dynamisch hergeleitete Operatoren oder Zustandsabbildungen, die keine
  Intertwiner der hier fixierten Produktgruppenwirkung sind.

Solche Möglichkeiten sind zusätzliche Strukturen. Sie dürfen nicht als der
hier gesuchte Intertwiner bei fester Gruppenwirkung bezeichnet werden.

**Review-Verdikt:** Die Hypothese ist korrekt. Der stärkere Satz im
vorhandenen PROOF.md, eine familienreine antilineare Darstellungsabbildung
\((\overline{16},\bar4)\to(\overline{16},4)\) existiere, ist für die volle
Produktgruppe zu verwerfen. Korrekt bleibt nur die faktorweise
\(SU(4)\)-Antilinearität sowie deren Verwendung als ausdrücklich
getwistete, zusätzliche Konstruktion.
