# Kleinster Test des Kreiszeitvertrags am ursprünglichen Transfer

21. September 2026 · `v221_seam_qecc` und `v814_k5_sixstep_transport`

## Ergebnis

Der tatsächlich vorhandene dreidimensionale TFPT-Transfer kann nicht unter
einer gemeinsamen Schrittweite als Einschränkung der euklidischen Zeit

\[
S_\tau=e^{-\tau|h|}
\]

eines einzelnen lokalen Kreisoperators mit einem gleichabständigen
periodischen oder NS-artigen Energiespektrum realisiert werden. Der
entscheidende Widerspruch liegt bereits in seinen zwei exakten
Abklingfaktoren

\[
\lambda_2=\left(\frac23\right)^6,
\qquad
\lambda_3=\left(\frac13\right)^6.
\]

Ihre logarithmischen Energien haben das irrationale Verhältnis

\[
\frac{-\log\lambda_3}{-\log\lambda_2}
=\frac{\log3}{\log(3/2)}\notin\mathbb Q.
\]

Jedes einzelne Kreisgitter mit gemeinsamer Geschwindigkeit und Schrittweite
liefert dagegen rationale Verhältnisse seiner positiven Energien. Das gilt
auch nach freier Fock-Quantisierung, solange keine zusätzlichen
sektorabhängigen Offsets oder Geschwindigkeiten eingeführt werden.

Dies ist kein globaler TFPT-Ausschluss. v221 definiert den Operator als
endlichen Recovery-/Vergessenskanal. Weder v221 noch v814 identifiziert ihn
mit dem physikalischen Einteilchentransfer `exp(-tau |h|)`. Ausgeschlossen
ist genau diese zusätzliche Gleichsetzung im neuen lokalen Kreiszeitvertrag.

## 1. Was die Originale tatsächlich liefern

Der Codegraph führt `v221_seam_qecc.run` auf den dreidimensionalen
Cusp-Gewichtsraum mit den orthogonalen Richtungen

\[
u_1=(1,1,1),\qquad u_2=(1,-1,0),\qquad u_3=(1,1,-2).
\]

v221 konstruiert numerisch den symmetrischen, doppelt-stochastischen
klassischen Kanal

\[
T=\frac13u_1u_1^*+rac{(2/3)^6}{2}u_2u_2^*
  +\frac{(1/3)^6}{6}u_3u_3^*.
\tag{1}
\]

Seine exakte Fassung steht in v814. Dort ist

\[
B=\frac1{18}
\begin{pmatrix}
13&1&4\\
1&13&4\\
4&4&10
\end{pmatrix},
\qquad
\operatorname{spec}B=\left\{1,\frac23,\frac13\right\},
\]

in genau derselben Eigenbasis und

\[
T=B^6=\frac1{4374}
\begin{pmatrix}
1651&1267&1456\\
1267&1651&1456\\
1456&1456&1462
\end{pmatrix}
\tag{2}
\]

bitgenau. v814 typisiert `B` als eingesetzte Sechs-Hand-/Clock-Wurzel und
trennt sie von seinen räumlichen Kandidaten. Die Gleichung (2) macht `B`
nicht automatisch zu einer lokalen physikalischen Zeit auf einem
Feld-Hilbertraum.

## 2. Jeder zugelassene gewichtete Kreisoperator hat Gitterenergie

Im neuen bedingten Randvertrag ist

\[
h=\pm q(\theta)D,
\qquad D=-i\partial_\theta,
\qquad \rho=q^{-1}>0,
\]

auf `L2(S1,rho dtheta)`. Dies umfasst insbesondere die zuvor klassifizierte
Familie

\[
q(\theta)=q_0+a\cos\theta+b\sin\theta,
\qquad q_0>\sqrt{a^2+b^2},
\]

noch bevor die geometrische Vierteldrehung `q` auf eine Konstante reduziert.
Setze

\[
s(\theta)=\int_0^\theta\rho(t)\,dt,
\qquad L=\int_0^{2\pi}\rho(t)\,dt.
\]

Der Variablenwechsel ist unitär von `L2(rho dtheta)` nach `L2([0,L],ds)` und
liefert exakt

\[
qD=-i\partial_s.
\tag{3}
\]

Damit ist für die periodische Spinstruktur

\[
\operatorname{spec}|h|
=\left\{\frac{2\pi}{L}|n|:n\in\mathbb Z\right\},
\tag{4}
\]

und für die antiperiodische/NS-Struktur

\[
\operatorname{spec}|h|
=\left\{\frac{2\pi}{L}|n+\tfrac12|:n\in\mathbb Z\right\}.
\tag{5}
\]

Die Form von `q` ändert die Bogenkoordinate und den gemeinsamen Maßstab,
nicht die Gleichabständigkeit. Nach freier Fock-Quantisierung sind die
Anregungsenergien endliche Summen dieser Werte, also weiterhin rationale
Vielfache einer gemeinsamen Einheit. Periodische Nullmoden ändern nur die
Nullenergie, nicht dieses positive Gitter.

## 3. Exakter Primfaktorwiderspruch

Angenommen, es gäbe eine Isometrie `J` von dem v221-Raum in den Kreis- oder
freien Fockraum und eine gemeinsame Schrittweite `tau>0` mit

\[
e^{-\tau|h|}J=JT.
\tag{6}
\]

Jedes Eigenpaar von `T` würde dann auf ein Eigenpaar desselben
Kreistransfers abgebildet. Daher müssten für ein `0<a<1` und positive
rationale Gitterexponenten `r,s` gelten

\[
\left(\frac23\right)^6=a^r,
\qquad
\left(\frac13\right)^6=a^s.
\tag{7}
\]

Nach Beseitigung der Nenner würde (7) für positive ganze Zahlen `m,n`

\[
\left(\frac23\right)^{6m}
=\left(\frac13\right)^{6n}
\tag{8}
\]

erzwingen. Die linke Seite hat positive Zweierbewertung `6m`, die rechte
Zweierbewertung null. Das ist unmöglich. Äquivalent: Wäre das
Logarithmusverhältnis `p/q` rational, folgte

\[
2^p=3^{p-q},
\]

im Widerspruch zur eindeutigen Primfaktorzerlegung.

Der Widerspruch ist unabhängig von `tau`, der Randlänge, dem Vorzeichen von
`h` und davon, ob direkt `T` oder die bitgenaue Sechswurzel `B` geprüft wird.

## 4. Schon zwei komprimierte Momente erzwingen den Intertwiner

Man muss (6) nicht voraussetzen. Sei `S=e^(-tau |h|)` ein positiver
selbstadjungierter Transfer, `J` eine Isometrie und `P=JJ*`. Fordere nur

\[
J^*SJ=T,
\qquad
J^*S^2J=T^2.
\tag{9}
\]

Dann ist der Momentdefekt

\[
\begin{aligned}
J^*S(I-P)SJ
&=J^*S^2J-J^*SP SJ\\
&=T^2-(J^*SJ)^2=0.
\end{aligned}
\]

Die linke Seite ist

\[
((I-P)SJ)^*((I-P)SJ)\ge0.
\]

Also `(I-P)SJ=0`: Der Bereich von `J` ist unter `S` invariant und

\[
SJ=JJ^*SJ=JT.
\]

Damit führen bereits die ersten beiden exakt passenden komprimierten
Zeitschritte auf (6) und anschließend in den Primfaktorwiderspruch. Nur den
ersten Schritt zu komprimieren reicht für diese Folgerung nicht.

## 5. Genaue Reichweite

**Ausgeschlossen** ist eine gemeinsame Quellen-/Schrittisometrie für

- den tatsächlichen v221/v814-Transfer mit beiden nichttrivialen Modi;
- einen einzelnen lokalen Kreisoperator der Form `h=±qD` mit periodischer
  oder NS-artiger Spinstruktur;
- dessen gewöhnliche freie Fock-Quantisierung mit einem gemeinsamen
  Energiequant und ohne geladene sektorabhängige Offsets;
- entweder die direkte Intertwinerbedingung (6) oder bereits die beiden
  Momentbedingungen (9).

**Nicht ausgeschlossen** sind zusätzliche Sektoren mit unabhängig
hergeleiteten Energieoffsets, mehrere Geschwindigkeiten, nichtlokale
Hamiltonoperatoren, andere Holonomien, wechselwirkende Spektren oder eine
andere physische Bedeutung des Recovery-Schritts.

Vor allem ist der ursprüngliche Transfer selbst nicht widerlegt. v221 prüft
eine Recovery-/Vergessensrate, und v814 zeigt ihre exakte sechsschrittige
Clock-/Hand-Faktorisierung. Das Ergebnis sagt nur:

> Dieser Recovery-Transfer ist nicht zugleich der Ein-Schritt-Transfer einer
> einzigen gleichabständigen lokalen Kreiszeit unter derselben
> Quellenisometrie.

Die nächste Herkunftsfrage bleibt deshalb typisiert: Entweder muss ein
anderer tatsächlich physischer TFPT-Transfer aus der Quelle gewonnen werden,
oder es muss eine zusätzliche, ursprünglich hergeleitete Beziehung zwischen
Recovery-Schritt und Feldzeit angegeben werden. Die vorhandene Spektrenzahl
allein liefert diese Beziehung nicht.

## Reproduktion

Der kleine Prüfer rekonstruiert `B`, `B^6`, die gemeinsame Eigenbasis und die
beiden Primfaktoren ausschließlich mit rationaler Arithmetik. Er liest die
Originaldateien nur für ihre Hashes und ändert das Repository nicht.
