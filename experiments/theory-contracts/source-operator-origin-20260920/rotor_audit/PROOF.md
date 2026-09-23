# Exakter Rotor-Audit: Dynamische Quartik-Komponente, kein hergeleiteter Hamiltonterm

**Contract:** `UR.SOURCE.ROTOR_AUDIT.01`  
**Verdict:** `PARTIAL`  
**Positiver exakter Befund:** Der vorhandene Rotor-Parent erzeugt im Doppelkommutator eine nichtgaußsche fermionische Komponente.  
**Beweisgrenze:** Die vorhandenen Quellen leiten daraus keinen statischen quartischen effektiven Hamiltonoperator ab.

## 1. Tatsächlich geprüfter Quelloperator

Auf einer orientierten Kante $0\to1$ enthält der vorhandene Parent

\[
H_E=\frac{\kappa}{2}E^2,\qquad
V_{LL}=a\left(Uc_{L1}^{\dagger}c_{L0}+U^{\dagger}c_{L0}^{\dagger}c_{L1}\right),
\]

mit

\[
[E,U]=U,\qquad a=\frac1{12},\qquad \kappa=\frac1{100}.
\]

Der gepinnte Originalprüfer wertet die CAR-Wirkung für alle 16 Besetzungsmasken der vier wirklichen Moden $L0,L1,H0,H1$ und symbolisches ganzzahliges $E$ aus. Für den Low-Low-Anteil gilt auf dem gemeinsamen invarianten Kern endlich unterstützter Rotorzustände exakt

\[
\begin{aligned}
C_{LL}
&=[V_{LL},[H_E,V_{LL}]]\\
&=\kappa a^2\bigl[n_{L0}+n_{L1}-2n_{L0}n_{L1}
       +2E(n_{L0}-n_{L1})\bigr]\\
&=\kappa a^2\bigl[\tfrac12-2q_{L0}q_{L1}
       +2E(q_{L0}-q_{L1})\bigr],
\end{aligned}
\]

wobei $q_{Lx}=n_{Lx}-\tfrac12$. Damit ist die fermionische Grad-4-Komponente

\[
-2\kappa a^2q_{L0}q_{L1}=-\frac1{7200}q_{L0}q_{L1}.
\]

Auch die Hilbert-Schmidt-Projektion des Doppelkommutators der **vollständigen ursprünglichen Kanten-Hoppingliste** auf $q_{L0}q_{L1}$ hat exakt den Koeffizienten $-1/7200$. Die zusätzlichen Low/High-Hoppings löschen diese Komponente nicht aus. Die angegebene geschlossene Formel ist dagegen die Formel für $C_{LL}$, nicht für den gesamten Kantenoperator.

Das ist eine echte dynamische Algebra-Aussage. Beispielsweise ist $C_{LL}$ die zweite Ableitung bei $s=0$ von

\[
e^{isV_{LL}}H_Ee^{-isV_{LL}}.
\]

Sie sagt ohne einen zusätzlich vorgegebenen Schalt- oder Eliminationsvertrag nicht, dass $C_{LL}$ mit einem bestimmten Koeffizienten als neuer Term in $H$ steht.

## 2. Ladungsaussage

Die zentrierte Low-Besetzung $q_L$ ist nicht die volle Gauß-Ladung. Für die einzelne orientierte Kante lauten die tatsächlichen Nebenbedingungen

\[
G_0=q_{L0}+q_{H0}+E,\qquad
G_1=q_{L1}+q_{H1}-E.
\]

Auf $G_0=G_1=0$ folgt deshalb

\[
q_{L0}q_{L1}=(q_{H0}+E)(q_{H1}-E).
\]

Die Quartik-Komponente ist also auch nach der Gauß-Reduktion nicht ohne Weiteres ein autonomer Low-Low-Kontaktterm. Sie bleibt mit High-Besetzung und Rotorfluss korreliert. Eine zusätzliche kontrollierte Elimination dieser Freiheitsgrade wäre nötig.

Das ursprüngliche Hopping respektiert das Gauß-Gesetz: Beim Transport $0\to1$ sinkt die Materiebesetzung an 0, steigt an 1 und $E$ verschiebt sich passend um $+1$. Der Prüfer erschöpft zusätzlich die sechs Zustände des vollständigen Gauß-neutralen Ein-Kanten-Hilbertraums; die exakte Parent-Wirkung bleibt in diesem Raum.

## 3. Kleinster entscheidender Projektionstest

Nimm den in der Quelle zulässigen nackten Zustand

\[
|\Omega\rangle=|L0,L1;E=0\rangle.
\]

Mit dem vollständigen ursprünglichen Termsatz dieser Ein-Kanten-Instanz bei dem deklarierten `ambient_degree=6` ergibt die sparse exakte Wirkung in Einheiten $1/14400$

\[
H|\Omega\rangle
=300|L0,L1;0\rangle
-600|L1,H1;+1\rangle
+600|L0,H0;-1\rangle.
\]

Alle drei Zustände erfüllen $G_0=G_1=0$. Der Unterraum $E=0$ ist jedoch nicht invariant, denn

\[
\|Q_{E\ne0}H|\Omega\rangle\|^2
=2\left(\frac{600}{14400}\right)^2
=\frac1{288}.
\]

Dieser Test trennt die beiden Projektionen:

- Die physikalische Gauß-Projektion beschränkt $H$ auf einen invarianten Sektor, beseitigt die Rotorbewegung aber nicht.
- Die in `local-window-round37` tatsächlich verwendete Projektion $P_K$ auf $|E|\le K$ ist eine endliche Flusskompression $H_{WK}=P_KH_WP_K$ mit Duhamel-/Tail-Fehlergrenze. Sie ist ausdrücklich keine spektrale Niedrigenergie-Elimination.
- Eine Projektion auf $E=0$ ist in der Quelle weder als exakte Dynamik noch als effektiver Hamiltonvertrag angegeben.

Der kleinste elektrische Anregungsabstand ist

\[
\Delta_E=\frac\kappa2=\frac1{200}.
\]

Die vorhandenen Hopping-Skalen sind im Vergleich dazu

\[
\frac a{\Delta_E}=\frac{50}{3},\qquad
\frac{\eta a}{\Delta_E}=\frac{25}{3},\qquad \eta=\frac12.
\]

Für den obigen Zustandsvektor ist sogar

\[
\frac{\|Q_{E\ne0}H|\Omega\rangle\|^2}{\Delta_E^2}=\frac{1250}{9}.
\]

Diese Quotienten zeigen nur: Eine Störungsentwicklung mit der **elektrischen Energie allein** als ungestörtem Lückenoperator ist nicht klein. Sie schließen eine gemeinsame High-/Rotor-Elimination nicht aus. Die Originalquelle enthält außerdem `MASS=4`; diese darf bei der Spektralprüfung nicht weggelassen werden. Der folgende vollständige Test korrigiert ausdrücklich eine zu weit gehende erste Einschätzung.

## 3b. Positiver vollständiger Quellentest mit der vorhandenen Masse 4

Die ursprüngliche Masse 4 liefert im vollständigen Gauß-neutralen Ein-Kantenraum einen kontrollierten tiefsten Spektralblock. Es wurden keine Quellparameter verändert. In der Reihenfolge

```
(L0L1;0), (L0H0;-1), (L1H0;0), (L0H1;0), (L1H1;+1), (H0H1;0)
```

ist H eine exakt rekonstruierte6×6-Matrix. Sei P der Rang-eins-Projektor auf den ersten Zustand, Q=1-P. Dann

\[
E_0=PHP=1/48,\quad \|QHP\|^2=1/288,
\quad QHQ\ge q_{\min}I,\quad q_{\min}=9337/2400.
\]

Die letzte rationale Schranke folgt aus allen fünf Gershgorin-Zeilen des vollständigen Fastblocks, einschließlich Masse 4. Der Abstand zu E0 ist mindestens `9287/2400`, nicht `1/200`.

Für E<q_min ist die Feshbach-Gleichung exakt

\[
H_{\rm eff}(E)=\frac1{48}-v^T(QHQ-E)^{-1}v,
\quad H_{\rm eff}(E)=E,
\]

mit v=QHP. Die rationale Selbstenergie ist

\[
v^T(QHQ-E)^{-1}v=
\frac{-25(E-8)(96E-385)}
{691200E^3-11077056E^2+55503183E-88997855}.
\]

Unterhalb q_min ist `E0-E-self_energy(E)` strikt fallend. Sie besitzt genau einen Nullpunkt, und die exakten Vorzeichentests geben

\[
0.01996381<E_*<0.01996382.
\]

Für den zugehörigen Eigenvektor gilt

\[
\frac{\|Q\psi\|^2}{\|P\psi\|^2}
\le\frac{1/288}{(9287/2400)^2}
=\frac{20000}{86248369}<\frac1{4000}.
\]

Damit ist eine kontrollierte **Rang-eins-Spektralreduktion** der vorhandenen Quelle tatsächlich möglich. Eine isolierte Spektralprojektion liefert auf diesem Block die exakte skalare Zeitentwicklung mit Energie E*. Das ist ein positiver, eng begrenzter Dynamikbefund.

Er ist noch kein Quartik-Hamiltonian für freie Low-Feldbeine: Der physikalische Ein-Kantenraum ohne High-Besetzung besteht nur aus dem einen Zustand `(L0L1;0)`. Die Gaußbedingung fixiert hier die Materiezahl. Die effektive Wirkung auf diesem Block ist deshalb eine skalare Energieverschiebung; sie identifiziert keinen unabhängigen Dichte-Dichte-Koeffizienten und keine zehnkanalige Randfeldalgebra. Der nackte Fluss-null-Unterraum selbst bleibt nicht invariant.

## 4. Warum der Quartik-Koeffizient kein einzelner Hamiltonterm ist

Schon innerhalb $C_{LL}$ darf die Komponente $-q_{L0}q_{L1}/7200$ nicht isoliert als ganzer Operator gelesen werden. Auf $|L0,L1;E=0\rangle$ verschwindet der vollständige Ausdruck wegen Pauli-Blockierung:

\[
n_{L0}+n_{L1}-2n_{L0}n_{L1}=1+1-2=0.
\]

Die isolierte Quartik-Komponente wäre dort ungleich null; sie wird durch die konstanten und quadratischen Teile exakt kompensiert. Der Koeffizient belegt daher eine nichtgaußsche Komponente der Operatoralgebra, nicht einen allein wirkenden Dichte-Dichte-Term.

Der ursprüngliche Vertrag spezifiziert den exakten Hamiltonoperator und eine kontrollierte endliche Flusskompression. Der neue vollständige Ein-Kanten-Test liefert zusätzlich die obige skalare Spektralreduktion. Ein effektiver statischer **Mehrfeld-Quartikterm** folgt daraus nicht; hierfür fehlen weiterhin ein verbleibender Feldraum, der kontrollierte lokale Transfer und die zugehörige Operatorresolvente.

## 5. Genaue Beweisgrenze

Exakt bewiesen sind:

1. die obige Doppelkommutatoridentität für beliebiges ganzzahliges $E$;
2. die überlebende $q_{L0}q_{L1}$-Komponente $-1/7200$ im vollständigen Kanten-Hopping-Doppelkommutator;
3. die korrekte Gauß-Ladung und ihre Korrelation von Low-, High- und Rotorvariablen;
4. die exakte Nichtinvarianz von $E=0$ bei gleichzeitiger Gauß-Invarianz;
5. das Fehlen einer kleinen rein elektrischen Störgröße, aber eine kontrollierte gemeinsame High-/Rotor-Rang-eins-Spektralreduktion dank der tatsächlich vorhandenen Masse 4.

Nicht hergeleitet sind:

- ein zusätzlicher statischer quartischer Term im ursprünglichen Hamiltonoperator;
- eine kontrollierte Elimination mit einer verbleibenden nichttrivialen lokalen Fermionfeldalgebra oder Spiegelentkopplung;
- eine Abbildung auf die sechzehn Clock-Majoranas oder zehn Boundary-Kanäle;
- Vakuum-, Phasen-, Zustands- oder Quellenauswahl;
- eine vollständige TFPT-Herleitung.

Der Forschungsstand bleibt daher `PARTIAL`: ein exakter nichtgaußscher Dynamik-Ausgang und eine kontrollierte skalare Spektralreduktion sind vorhanden; der Übergang zu einem effektiven lokalen Mehrfeld-Quartikoperator bleibt offen.

## 6. Reproduktion

```bash
python3 check_rotor_audit.py > certificate.json
python3 -OO check_rotor_audit.py > certificate.optimized.json
cmp certificate.json certificate.optimized.json
```

Die gepinnten Originalquellen und SHA-256-Werte stehen in `source_manifest.json` und im Zertifikat.
