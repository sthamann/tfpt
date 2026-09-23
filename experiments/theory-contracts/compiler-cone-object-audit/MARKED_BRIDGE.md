# Die markierte Brücke zum vorhandenen Compiler-Gitter

## Ergebnis und Reichweite

Zwischen der hier untersuchten maximalen Ordnung und dem **bereits vorhandenen**
Gaussian-E₈-Gitter des TFPT-Compilers existiert eine explizite ganzzahlige
Isometrie. Sie erhält nicht nur Dimension, Determinante und Wurzelzahl,
sondern gleichzeitig das Skalarprodukt, die Gaussian-Struktur, den
tatsächlichen Familienzyklus und den ausgewählten binären Anker.

Damit ist ein konkreter Rückweg konstruiert:

\[
\text{vorhandenes markiertes Gitter}
\longrightarrow\text{Compiler-Algebra und Anker-Kommutant}
\longrightarrow\text{maximale Ordnung}
\longrightarrow\text{dasselbe markierte Gitter}.
\]

Das ist eine Rekonstruktionsschleife mit erhaltenen Markierungen, keine neue,
unabhängige Herleitung, warum die Natur E₈ auswählen müsste. Die Quelle am
Anfang enthielt dieses Gitter bereits. Eine Isometrie der zugrunde liegenden
Gitter ist außerdem noch keine Gleichsetzung ihrer physikalischen Zustände,
Hamiltonoperatoren, lokalen Felder oder zulässigen Prozesse.

## 1. Tatsächliche Quelle und Konventionen

Die Quelle ist
[`v774_arf_spinor_compiler.py`](../../../verification/v774_arf_spinor_compiler.py),
SHA-256
`3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c`.
Der geprüfte Repository-Basisstand ist
`66b91e40e245569f06ab440ead80f446c9be0ee5`; zusätzlich werden die tatsächlich
importierten Dateien über ihre Hashwerte kontrolliert. Der Commit allein
wäre bei einem nicht sauberen Arbeitsverzeichnis kein ausreichender Quellpin.

Die unveränderte v774-Konstruktion verwendet

\[
L=\{x\in\mathbb Z^8:x\bmod2\in C^*\},\qquad
\langle x,y\rangle_L=\frac{x\cdot y}{2}.
\]

Hier besteht `CSTAR` aus Nullwort, Einswort und den vierzehn im Original
angegebenen Gewicht-vier-Unterstützungen. `constrA_lattice(code)` liefert eine
**Zeilenbasis** `B`, die Koordinatenabbildung `coords`, die Reduktion `label`
modulo \((1+J)L\) und deren Hilfsdaten. Daher lautet die Gram-Matrix dieser
Basis \(G_L=BB^T/2\), nicht \(BB^T\).

Die tatsächlich verwendeten reellen Abbildungen sind

\[
Jx=(-x_1,x_0,-x_3,x_2,-x_5,x_4,-x_7,x_6),
\]
\[
\sigma x=(x_4,x_5,x_0,x_1,x_2,x_3,x_6,x_7).
\]

Insbesondere ist `PI_J` nur die zugrunde liegende Paarvertauschung; die
Minuszeichen in `J_vec` dürfen nicht weggelassen werden. Die Familien- und
Ankerklassen werden mit den originalen Funktionen `label_group` und
`family_anchor_basis` bestimmt, nicht nachträglich passend benannt.

## 2. Zielordnung und einfache Abbildung

Setze in der zweidimensionalen komplexen Darstellung

\[
a=iI,\quad u_1=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
u_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad u_3=u_1u_2,
\]
\[
w=\frac{I+u_1+u_2+u_3}{2},\qquad
P=\begin{pmatrix}1&(1+i)^{-1}\\0&(1+i)^{-1}\end{pmatrix},
\qquad\mathcal M=P M_2(\mathbb Z[i])P^{-1}.
\]

Die Gittermetrik der Ordnung ist
\(\langle A,B\rangle_{\mathcal M}=\Re\operatorname{Tr}(AB^*)\).
Sie ist von der multiplikativen Determinantennorm zu unterscheiden.

Für \(z_j=x_{2j}+ix_{2j+1}\), \(j=0,1,2,3\), definiere zunächst

\[
F(x)=\frac{z_3I+z_0u_1+z_1u_2+z_2u_3}{2}.
\]

Die Quaternionenbasis ist für die reelle Spurmetrik orthogonal und jeder
Basisvektor hat Normquadrat zwei. Folglich gilt für beliebige reelle
Koordinaten, nicht nur für getestete Wurzeln,

\[
\Re\operatorname{Tr}(F(x)F(y)^*)=\frac{x\cdot y}{2}.
\]

Ebenso gelten unmittelbar \(F(Jx)=aF(x)\) und
\(F(\sigma x)=wF(x)w^*\): der tatsächlich geerbte innere Zyklus vertauscht
\(u_1,u_2,u_3\) in der richtigen Richtung und fixiert \(I\).

Alle sechzehn Codewörter sowie die zusätzlichen Erzeuger \(2e_k\) haben
Bilder in \(\mathcal M\). Die unten angegebene unimodulare Basismatrix
beweist darüber hinaus Surjektivität auf das ganze Gitter. Es handelt sich
also nicht nur um eine passende Untermenge von 240 Vektoren.

## 3. Den Anker wirklich erhalten

Die originale deterministische Rezeptur liefert als Ankerrepräsentanten

\[
x_A=(0,1,0,1,0,1,0,1).
\]

Die erste Abbildung erfüllt \(F(x_A)=aw\), nicht \(a\). Diese Differenz darf
nicht durch eine Namensgleichsetzung verdeckt werden. Sie lässt sich jedoch
durch eine bereits ganzzahlige, unitäre Operation exakt korrigieren:

\[
\boxed{F_A(x)=F(x)w^*.}
\]

Denn

\[
P^{-1}wP=\begin{pmatrix}1&1\\-1&0\end{pmatrix},\qquad
P^{-1}w^*P=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
\]

Rechtsmultiplikation mit \(w^*\) ist daher ein invertibler ganzzahliger
Gitteroperator. Wegen \(ww^*=I\) erhält er die Metrik. Er kommutiert sowohl
mit Linksmultiplikation durch \(a\) als auch mit \(\operatorname{Ad}_w\).
Somit gelten gemeinsam

\[
F_A(x_A)=a,\qquad F_A(Jx)=aF_A(x),\qquad
F_A(\sigma x)=wF_A(x)w^*.
\]

Der Anker wird bereits als gewählter Repräsentant exakt getroffen, also
insbesondere auch im Quotienten modulo \((1+a)\mathcal M\).

## 4. Nachprüfbares ganzzahliges Zertifikat

Die Zielkoordinaten sind die Real- und Imaginärteile der Einträge von
\(P^{-1}AP\) in Zeilenreihenfolge:
\((E_{11},iE_{11},E_{12},iE_{12},E_{21},iE_{21},E_{22},iE_{22})\),
jeweils nach Konjugation mit \(P\). Zur originalen v774-Zeilenbasis gehört
die folgende Matrix; ihre Spalten sind die Bilder der Quellbasisvektoren:

\[
K_A=\begin{pmatrix}
1&0&1&0&1&0&0&0\\
1&0&0&1&1&0&0&0\\
0&-1&0&0&1&-1&-1&0\\
0&0&-1&0&0&0&0&-1\\
0&0&0&0&0&-1&1&0\\
0&1&0&0&-1&0&0&1\\
1&1&0&0&-1&0&1&0\\
1&1&1&1&0&1&0&1
\end{pmatrix}.
\]

Die exakten Identitäten sind

\[
\det K_A=1,\quad K_A^T G_{\mathcal M}K_A=G_L,\quad
K_AJ_L=J_{\mathcal M}K_A,\quad
K_A\sigma_L=\sigma_{\mathcal M}K_A.
\]

[`marked_lattice_record`](checker.py) berechnet diese Daten erneut aus den
gepinnten Originalhelfern. Zusätzlich werden **alle 240 Wurzeln** verglichen:
16 Vektoren vom Typ \(\pm2e_k\) und 224 Vektoren mit vier Einträgen \(\pm1\)
auf den vierzehn Code-Unterstützungen. Ihre Bilder sind genau die 240
Norm-zwei-Wurzeln der Ordnung. Der tatsächliche Familienzyklus fixiert auf
beiden Seiten zwölf Wurzeln. Die Basissätze beweisen die Identifikation des
gesamten Gitters; die Wurzelprüfung ist eine unabhängige endliche Kontrolle.

## 5. Binäre Form und halbe Phase

Die Quelle verwendet die Gaussian-hermitesche Form

\[
h_L(x,y)=\frac{x\cdot y+i\,x\cdot Jy}{2}.
\]

Die Metrik- und Gaussian-Identitäten implizieren
\(h_L(x,y)=\operatorname{Tr}(F_A(x)F_A(y)^*)\). Reduktion modulo \(1+i\)
liefert deshalb dieselbe binäre Form. In der tatsächlich ermittelten
Familien-Anker-Basis ist ihre Matrix

\[
\bar h=\begin{pmatrix}0&1&1&1\\1&0&1&1\\1&1&0&1\\1&1&1&0\end{pmatrix}.
\]

Die Prüfung berechnet diese Basiswerte unmittelbar. Durch Bilinearität gilt
die Gleichheit damit auf allen 256 Paaren der sechzehn Quotientenklassen.
Auch die bisher ausgewählte quadratische Verfeinerung kann entlang dieser
markierten Isometrie transportiert werden; sie wird dadurch nicht zu einer
neuen physikalischen Teilchenklassifikation.

Die Phase \(\zeta=aw^*\) erhält unter der **ankerkorrigierten** Abbildung die
Quotientenklasse \(F_\Sigma\), nicht die Ankerklasse. Denn ihr Urbild ist
\(F^{-1}(a)\), die Gaussian-Rotation des Quellvektors mit unkorrektiertem
Bild \(I\); dessen Klasse ist \(F_\Sigma\). Diese konkrete Zuordnung ist
prüfbar, identifiziert die Phase aber nicht mit einem Seam-Half-Charge-Feld.

## 6. Originalreplay und verbleibende Grenzen

Vor dieser Erweiterung wurde das vollständig gelesene, vom Nutzer gelieferte
`pruefung.py` unabhängig wiederholt. **44 exakte Prüfungen bestanden**; das
Ergebnis stimmte vollständig mit `exakte-ergebnisse.json` überein. Alle zehn
direkten Quellhashes und alle zehn archivierten Quellkopien stimmten mit den
aktuellen Originaldateien überein; die transitiven Schutzprüfungen liefen mit.
Der Programmhash lautet
`7d0b7803aa49aa5f034579d76567e154778386b39b041bcd7b3038778efe9696`.

Der Replay entfernt im Syntaxbaum ausschließlich den zuvor gelesenen
Ausgabeschreibteil ab Originalzeile 167. Er führt die mathematische Rechnung
mit ihren Schutzprüfungen aus, überschreibt aber weder das Originalergebnis
noch die archivierten Dateien. Diese Vorgehensweise ist in
[`replay_original`](checker.py) implementiert. Ein unveränderter Import des
Originalprogramms würde dagegen dessen abschließende Schreiboperationen
ausführen. Für einen ganz neuen Ausgabeort müsste das Original außerdem
seinen Unterordner `quellen` anlegen.

Die Brücke beweist **Existenz**, nicht Eindeutigkeit der Koordinatenabbildung.
Weitere markierungserhaltende Gitterautomorphismen können andere Karten
liefern. Sie identifiziert insbesondere nicht den alten Clifford-Trägerraum
mit den sechzehn Majorana-Moden der Clock-Quelle: Hier wirkt \(a\) durch
Linksmultiplikation auf einem achtreellen-dimensionalen Gitter. Die binäre
Ankerklasse, dieser Gaussian-Operator und eine alte Hilbertraumdarstellung
sind verschiedene Typen von Objekten. Der gemeinsame physikalische Prozess,
ein ausgewählter Zustand, lokale Felder und die Verbindung der Zeitbegriffe
bleiben eigenständige Beweispflichten. Kein T1–T8-Status wird durch diese
Gitterrekonstruktion geschlossen.

Der Erkenntnisgewinn liegt deshalb an einer engeren, aber substanziellen
Stelle: Vorher konnten der positive Kommutant und das Compiler-Gitter nur
als ähnlich strukturierte Objekte nebeneinander stehen. Jetzt liegt eine
konkrete Abbildung vor, unter der sich jedes Gitterelement, die drei
Familienrichtungen und die Quotientenform verfolgen lassen. Eine künftig
vorgeschlagene Operation kann damit auf beiden Seiten berechnet und auf
ihre tatsächliche Verträglichkeit geprüft werden. Dabei darf weder die
Spurmetrik mit der Determinantennorm noch eine zulässige Gitterabbildung mit
einem physikalisch realisierten Zeitentwicklungsschritt vertauscht werden.
Genau diese Unterscheidungen machen den Rückweg als nächsten Prüfschritt
nützlich, ohne die noch fehlende gemeinsame Dynamik vorauszusetzen.
