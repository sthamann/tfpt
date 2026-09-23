# Vorwaertspruefung der bestehenden Dirac/Kovarianz-Schnittstelle

21. September 2026. Arbeitsfassung, Experiments-Firewall. Keine neue physische Quelle und keine Wiedereroeffnung bestehender Flavor-Claims.

## 1. Bestehendes Ergebnis und die verlangte Richtung

FLAV.QRATIO.01, FLAV.RIGID.02, FLAV.LEPTONC.01 und FLAV.UPOINT.01 behalten ihren typisierten Ledgerstand. PS.DIRAC.03/v258 beweist die bekannte Inversion einer KMS-Kovarianz und prueft sie auch nach Einsetzen vorhandener geladener Massen. Der dort als bedingt markierte Schritt ist eine unabhaengige Bestimmung von C_Sigma und P_F, so dass die **vorwaerts** berechnete Kompression den vorhandenen Diracblock ergibt. Die gleiche Rueckrechnung kann diese Herkunft nicht beweisen.

Der Begriff Kovarianz bezeichnet in den vorhandenen Quellen zwei verschiedene Zustaende: v210 benutzt den reinen Spektralprojektor C=(I+sgn(h))/2; v258 benoetigt fuer seinen endlichen unprojizierten Logarithmus eine treue Kompression 0<C_F<I. Das kann konsistent sein: Die Kompression eines reinen Zustands kann gemischt sein. Die erforderliche Kompression und ihre gemeinsame Zeitwirkung sind aber echte Daten.

## 2. Exakte Kompressionsidentitaet

Sei H ein endlichdimensionaler komplexer CAR-Einteilchenraum, P ein orthogonaler Projektor, Q=I-P und C=C*=C^2 eine reine Kovarianz. Alle folgenden Operatoren C_F=PCP werden auf PH verstanden, dessen Identitaet P ist. Setze B=QCP. Dann

  C_F-C_F^2 = PC(P+Q)CP-PCPCP = PCQCP = B*B.

Damit ist 0<C_F<I genau dann moeglich, wenn B injektiv ist; in endlicher Dimension ist rank B=dim PH und folglich dim QH>=dim PH notwendig. Eine durch den Zustandsprojektor reduzierte Auswahl [P,C]=0 liefert dagegen C_F^2=C_F: Der endliche Logit ist nicht definiert. Insbesondere reicht ein Projektor, der ausschliesslich aus den Spektralprojektoren einer mit C kommutierenden Clock aufgebaut wird, nicht fuer eine treue Kompression.

Gilt zusaetzlich **ohne eine nachtraegliche Odd-Projektion**

  C_F=(I+exp(D/mu))^-1,

so fordert derselbe Quellenanschluss exakt

  B*B = (1/4) sech^2(D/(2mu)).

Dies ist eine notwendige, pruefbare Forderung an vorhandene Kreuzkorrelationen, keine Konstruktion dieser Kreuzkorrelationen aus einem gewuenschten D. Fuer den allgemeineren v258-Ausdruck Pi_odd logit(C_F) bestimmt D allein die rechte Seite nicht.

## 3. Wann die volle Modulaermatrix chirale Diracform hat

Sei gamma=gamma*=gamma^-1 auf PH und K=log(I-C_F)-log(C_F), mit 0<C_F<I. Dann

  gamma K gamma=-K  <=>  gamma C_F gamma=I-C_F.

Beweis: Funktionalkalkuel und logit(1-c)=-logit(c); fuer die Rueckrichtung wird die inverse Funktion logistic angewendet. Eine Odd-Projektion von K kann diese Quellenbedingung nicht ersetzen: Sie entfernt lediglich den geraden Anteil und aendert im Allgemeinen das Spektrum.

## 4. Zustand und wirkliche Zeit gemeinsam pruefen

Sei h=h* der wirkliche, unabhaengig definierte Einteilchengenerator. Auf PH gilt

  P h^2 P - (P h P)^2 = P h Q h P = (Q h P)*(Q h P).

Daher ist P exp(-it h)P fuer alle reellen t eine autonome unitaere Gruppe auf PH genau dann, wenn QhP=0. Notwendigkeit folgt aus der Normerhaltung beziehungsweise dem zweiten Zeitmoment; Hinlaenglichkeit aus der Reduktion von h durch P.

Ist C ein Spektralprojektor **desselben** h, dann folgt aus QhP=0 auch [P,C]=0. Eine exakt autonome Einteilchenkompression der reinen Quelle besitzt somit einen reinen, nicht treuen Zustand. Sie kann nicht gleichzeitig die endliche, treue KMS-Kovarianz fuer den unprojizierten modularen Dirac liefern.

Dieser endliche Satz schliesst keine lokalen Typ-III-Netze, keine gemischten globalen KMS-Zustaende, keine Kasparov-Produkte und kein approximatives oder wechselwirkendes IR-Matching aus. Er entscheidet nur die bezeichnete direkte orthogonale CAR-Kompression mit exakt erhaltener physischer Zeit. Der modulare Generator eines gemischten Teilzustands ist grundsaetzlich nicht automatisch dessen physischer Zeitgenerator.

Die richtige volle dynamische Groesse ist in dieser Klasse die komprimierte Resolvente

  G_F(z)=P(z-h)^-1P
        =[z-PhP-PhQ(z-QhQ)^-1QhP]^-1

auf dem gemeinsamen Resolventengebiet. Der z-abhaengige Komplementterm darf nicht verschwinden, nur weil man eine endliche Zustandsmatrix ausgelesen hat. Die Feshbach-Schur-Identitaet ist Standardmathematik, keine neue TFPT-Ursprungsherleitung.

## 5. Kontrollierter Grenzwert zum reinen Zustand

Gilt fuer einen festen endlichen Testblock ||C_N-P_0||<=delta_N<1/2 mit P_0^2=P_0 und delta_N->0, dann liegen alle Eigenwerte von C_N in [0,delta_N] oder [1-delta_N,1]. Soweit sie strikt zwischen 0 und 1 liegen, gilt

  |log((1-c)/c)| >= log((1-delta_N)/delta_N) -> unendlich.

Bei exakten Endpunkten ist der Logit bereits undefiniert. Folglich liefert dieser konkrete Grenzprozess bei festem mu>0 keinen endlichen Diracblock. Numerisches Clipping der Eigenwerte waere keine regulaere physische Herleitung. Fuer einen verbleibenden Odd-Anteil kann es formale Ausloeschungen geben; deshalb betrifft der Divergenzsatz den **vollen** Logit und ersetzt nicht die separate Gamma-/Feldpruefung.

## 6. Analytische Anwendung auf die unveraenderte QWZ-Quelle

Der originale rohe Randspinor erfuellt h(theta)r=-sin(theta)r+(1-cos(theta))chi_minus mit orthogonalen normierten Spinoren. Fuer theta=2pi(j-1/4)/N und D_N=N h_N/(2pi) folgen

  d_j=-(N/(2pi)) sin(theta),
  Var_j(D_N)=(N/(2pi))^2 (1-cos(theta))^2.

Die Wahrscheinlichkeit auf der falschen Spektralhaelfte ist durch Var_j/d_j^2=tan^2(theta/2) begrenzt. Translation diagonalisiert die Kovarianz fuer verschiedene Fourierlabels. Im geprueften Fenster {-1,0,1} folgt deshalb delta_N<=tan^2(5pi/(4N)). Fuer N>=8 ist diese Schranke kleiner als1/2 und geht gegen0. Der Satz aus Abschnitt5 beweist die Divergenz des vollen Logits bei festem mu.

Das Argument gilt ebenso fuer jedes andere **festgehaltene endliche vollstaendige Fourierfenster** J aus ganzzahligen Labels: mit M=max_{j in J}|j-1/4| ist delta_N<=tan^2(pi M/N) fuer hinreichend grosses N. Eine andere feste Anzahl solcher Moden aendert diesen Befund nicht. Das ist keine Aussage ueber eine nichtinvariante echte Teilkompression, lokale Unteralgebren, zusammengesetzte Felder oder den bislang fehlenden physischen Materietraeger.

Der ausgeschriebene originale Quellbeweis und die numerischen Kontrollen stehen in native_covariance/RESULT.md. Der allgemeine Fenstersatz ist eine direkte analytische Folgerung derselben pro-Modus-Schranke; er wurde nicht durch eine endliche Auswahl anderer Fenster als 'vollstaendig getestet' ausgegeben.

## 7. Primärliteratur und Neuheitsgrenze

- Ingo Peschel, Calculation of reduced density matrices from correlation functions, https://arxiv.org/abs/cond-mat/0212631 . Die Logitformel rekonstruiert den modularen Einteilchenoperator eines quasifreien reduzierten Zustands; Vorzeichen/Transpose haengen von der Kovarianzkonvention ab.
- Genevieve Dusson, Israel Sigal, Benjamin Stamm, The Feshbach-Schur map and perturbation theory, https://arxiv.org/abs/2105.02058 . Standardgrundlage des resolventen- und energieabhaengigen effektiven Operators.

Die algebraischen Identitaeten sind bekannte lineare Algebra. Gegenstand dieser Runde ist ihre konkrete Anwendung auf den vorhandenen TFPT-Quellenanschluss, mit echten Quelldaten und ohne Einsetzen des Ziel-Yukawablocks. Eine vollstaendige TFPT-Loesung wird nicht behauptet.
