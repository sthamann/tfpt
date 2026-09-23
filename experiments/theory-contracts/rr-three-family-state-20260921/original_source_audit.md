# Begrenzter Audit: ursprüngliche Nahtquelle gegen den nativen \(W\)-Hamiltonoperator

**Datum:** 21. September 2026  
**Scope:** vorhandene, unveränderte TFPT-Quellen; keine neue Modellwahl, kein Replay, keine Repoänderung.  
**Verdict:** **OFFEN / negativer Herkunftsbefund.** In den geprüften Originalquellen gibt es keine unabhängig definierte **nichtlineare geladene Schwingerfunktion** und kein Variationsprinzip, das sowohl \(g/\Delta\) als auch den Grundzustand des nativen \(H_W\) aus der P1-Nahtquelle auswählt.

## 1. Früheste tragende Formeln

1. **P1 ist ein Zweipunkt-/Randkern-Postulat, kein geladenes Wechselwirkungsfunktional.**  
   `tfpt_1_architecture_e8.tex:159-176` setzt
   \[
   c_3=\frac1{8\pi}
   \]
   und beschreibt einen primitiven reflexionspositiven Randkern mit Einheitswindung und Selbstverkettungsnormierung. Der Text nennt P1 ausdrücklich einen nicht weiter reduzierten Postulat-Eingang. `origin_theory.tex:54-69` hält zusätzlich fest, dass die kontinuierliche Transferphysik \(F_{\rm transfer}\) nicht hergeleitet ist.

2. **Die erste explizite Nahtdynamik bleibt frei und bedingt.**  
   `verification/v156_seam_net_construction.py:16-22` leitet unter der Voraussetzung eines freien Bulks den Dirichlet-zu-Neumann-Operator
   \[
   \Lambda_\Sigma e^{ikx}=|k|e^{ikx}
   \]
   her. `:45-54` erklärt gerade die freie-Bulk-Prämisse und die operatoralgebraische Netzkonstruktion zum offenen analytischen Schritt. Das erzeugt die freie chirale Dispersion, noch keinen Boson-Fermion-Vertex.

3. **Der tatsächliche Operatoranschluss ist offen.**  
   `verification/v177_seam_marking_kernel.py:35-42,130-136` formuliert `QGEO.KERNEL.01` als die noch unbewiesene Operatoridentität
   \[
   C_\Sigma=U^{-1}C_{\mu_4}U,
   \]
   nicht bloß als Spektralgleichheit. `verification/v286_seam_equivalence_contract.py:5-16,34-41,123-143` konzentriert dieselbe Lücke in `SEAM.EQUIV.01`: Rohnahtzustand \(\to\) holomorphes \((E_8)_1\)-Netz. Selbst diese offene Identifikation betrifft Netz, Zustand und modulare Struktur; sie definiert keinen nativen \(W\)-Vertex und keinen Wert von \(g/\Delta\).

4. **Der native Hamiltonoperator tritt später als festgehaltener Modelloperator auf.**  
   `universal_room/new-2/TFPT_Universalraum_Minimale_Fortsetzung_2026-09-15_v1.6.1.md:19-44` schreibt
   \[
   H_W=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),\qquad
   P_A=\sum_{i<j}W_{A,ij}f_jf_i,
   \]
   mit \(WW^\dagger=8I_{60}\), und sagt ausdrücklich, dass Eingang beziehungsweise \(N\)-Sektor vorausgesetzt und nicht physisch präpariert/hergeleitet werden. `experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/RESULTS.md:35-50` übernimmt genau diesen Operator. Der Wert \(g/\Delta=1/20\) ist dort ein untersuchter Prüfpunkt (`:161-176`), kein Ergebnis eines Naht-Extremums.

## 2. Das vorhandene Variationsprinzip beantwortet eine andere Frage

`verification/v196_seam_energy_functional.py:1-32,42-48` definiert
\[
E_{\rm fail}(\rho,\Lambda,\Theta)
=\|[\rho,\Lambda]\|_{\rm HS}^2
+\|\rho^4-I\|_{\rm HS}^2
+\|\Theta\rho\Theta-\rho^{-1}\|_{\rm HS}^2.
\]
Seine Nullstelle prüft genau drei geometrisch/modulare Bedingungen: \(\mu_4\)-Äquivarianz des DtN-Operators, Ordnung vier und RP-Reflexion. Auf dem endlichen \(H^1\)-Block ist die Nullstelle automatisch; die volle Operator-Minimierung bleibt offen (`:27-32,87-91`).

`verification/v200_seam_variational_scan.py:1-27,36-75` variiert nur den Clockwinkel \(\theta\) und findet \(\theta=\pi/2\) im endlichen Charakterblock. Weder Funktional enthält geladene Grassmann-Quellen, ein Vermittlerfeld \(b_A\), den Tensor \(W_{Aij}\), \(g/\Delta\) oder ein Grundzustandsfunktional für \(H_W\). Daher kann sein Minimum diese Daten logisch nicht auswählen.

Die exakte Reihe in `experiments/theory-contracts/source-ground-response-20260920/PROOF.md:97-113`,
\[
\sum_{n\ge0}c_nz^n=(1-z)^{-3},
\]
ist die Norm-Erzeugungsfunktion der Oszillatornachkommen eines bereits festgelegten geladenen Vertexoperators. Sie ist kein Schwingerfunktional über dynamische Felder und besitzt keine Variation, die \(W\), \(g/\Delta\) oder einen Grundzustand festlegt.

## 3. Vorhandene konstruktive Gleichungen und ihre Grenze

Es gibt zwei echte, noch nutzbare Operatoridentitäten, aber keine von ihnen ist die gesuchte Herkunftsgleichung:

* **Quadrat-Hamiltonian:** `...Minimale_Fortsetzung...md:270-313` definiert
  \[
  H_+=\Delta\sum_A(b_A+\lambda P_A)^\dagger(b_A+\lambda P_A),\qquad \lambda=g/\Delta,
  \]
  mit exaktem Kern
  \[
  |\Psi_\eta\rangle=e^{-\lambda\sum_A b_A^\dagger P_A}
  (|0_b\rangle\otimes|\eta_f\rangle).
  \]
  Das ist konstruktiv, aber \(H_+=H_W+(g^2/\Delta)\sum_AP_A^\dagger P_A\), also nicht derselbe Hamiltonoperator. Außerdem ist \(\dim\ker H_+=2^{64}\): Positivität wählt keinen eindeutigen Zustand.

* **Quadratvervollständigung mit chemischem Term:** `:315-336` gibt eine exakte untere Schranke für \(H_\mu=H_W+\mu N\). Die dortige \(\mu_*\)-Formel ist ausdrücklich nur eine hinreichende Schwelle, keine exakte Phasengrenze und kein aus P1 abgeleiteter Parameter. Sie kann einen bereits gewählten Operator kontrollieren, aber weder \(g/\Delta\) noch \(H_W\) erzeugen.

Die spätere tatsächliche Quellenprüfung bestätigt die Herkunftslücke: `experiments/theory-contracts/source-ground-response-20260920/PROOF.md:26-27` nennt \(H_W\) bei \(g/\Delta=1/20\) den **unmodified target**; `:265-270` fordert eine neue quellenseitig hergeleitete Energie-/Feldabbildung samt Zustand. `experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt:247-267` nennt als fehlende Daten Kopplungen, Vorzeichen, Impulsabgleich und gemeinsamen Zustand/Zeit; der vorhandene kompakte Rotor ist ohne genau diese Abbildung kein Anschlussbeweis.

## 4. Kleinster entscheidender nächster Test

Der nächste Test darf erst bei einer **unabhängig aus der Rohnaht definierten** erzeugenden Funktion beginnen,
\[
\mathcal W_\Sigma[\bar\eta,\eta,J]=\log Z_\Sigma[\bar\eta,\eta,J],
\]
wobei \(\eta\) die tatsächlichen geladenen Nahtfelder und \(J_A\) ein aus derselben Quelle definiertes Vermittlerobservable koppelt. Es genügt zunächst der Jet bei verschwindenden Quellen:
\[
D_f=\frac{\delta^2\Gamma_\Sigma}{\delta\bar\psi\,\delta\psi},\qquad
D_b=\frac{\delta^2\Gamma_\Sigma}{\delta b^\dagger\delta b},\qquad
Y_{Aij}=\frac{\delta^3\Gamma_\Sigma}
{\delta b_A^\dagger\delta\psi_j\delta\psi_i}.
\]

**Präzisierung durch die Hauptprüfung:** Die angezeigten Ableitungen einer vollständigen 1PI-Wirkung sind im Allgemeinen frequenzabhängige, renormierte Vertexfunktionen. Sie sind nicht automatisch der elementare Hamiltonblock C1; auch ihre Hessians liefern ohne Feldnormierung und Zeit-/Domänenvertrag keinen kanonischen Hamiltonoperator. Ein nichtverschwindender zusammengesetzter Dreipunktkorrelator beweist umgekehrt noch keine elementare kubische Wechselwirkung.

Nur wenn aus der Quelle bereits eine zeitlokale kanonische Wirkung samt denselben Feldern, einem kontrollierten Ableitungsvertrag und Zustands-/Randbedingungen hergeleitet ist, kann deren elementarer kubischer Koeffizient unmittelbar gegen gW geprüft werden. Y=0 verwirft dann diesen direkten kubischen Anschluss innerhalb genau dieses Vertrags. Es ist kein Ausschluss nichtlinearer Feldabbildungen oder allgemeiner TFPT-Vervollständigungen. Ein nichtverschwindendes Y und YY-dagger proportional I_60 sind lediglich notwendige Frühfilter für eine Tensoridentifikation; sie wählen den vollständigen Zustand nicht aus.

Der bestehende bedingte Rekonstruktionsvertrag bietet den genaueren Operator-Test: Aus einem unabhängig definierten gemeinsamen Transfer werden auf denselben kanonischen Feldern C1=-K1-prime(0) und C2=-K2-prime(0) berechnet. Gefordert sind C1=gW ungleich null und C2=0 sowie die globalen unteren Operatorantworten, die irreduzible Darstellung und die globale Stabilität. Erst diese Gesamtheit liefert in der dort klassifizierten Form den Generator. Anschließend muss derselbe Quellenzustand geprüft werden. Der Test setzt keine Kenntnis der bereits gewünschten W-Antwort in den Rohtransfer ein.

Damit bleibt das fehlende Datum präzise: **die gemeinsame graduierte Quelle einschließlich Feldalgebra, Zeittransfer und Zustandsregel.** Eine nichtgaußsche erzeugende Funktion kann dieses Datum darstellen; ein isolierter dritter effektiver Jet ersetzt es nicht. Die vorhandenen P1-/QGEO-Gleichungen liefern in dem geprüften Bestand noch keine solche vollständige native Quelle.

## 5. Quellenhashes

* `tfpt_1_architecture_e8.tex` — `ca5460de7fe54d7362dcfbc9d650cc349811d6bada906317baadd7297d2e89eb`
* `origin_theory.tex` — `4a2ac752cf9beb65452d5c1aad3a9dc22b0d3fee24e8247c064ed654f910d95f`
* `verification/v156_seam_net_construction.py` — `2d8d86bbc393eda3d4779017111f2d67a4c94644bab9a37e6b6685e58570a4aa`
* `verification/v177_seam_marking_kernel.py` — `bf6ad1e0d4dd21ca3b66790b004c2d202a67ea1e94a249c4f09437cc4b6a1c09`
* `verification/v196_seam_energy_functional.py` — `fa447e51ca493cc0eb2f011299c1943042dc8fa8f59112276549e0a3f96a0166`
* `verification/v200_seam_variational_scan.py` — `231896f53ae03ef7052af133aad701dab2457f316a8545ee56b05279eb1dc6b4`
* `verification/v286_seam_equivalence_contract.py` — `8f3150d4dd1cd1f90ad7f705f8cf867e935bea7c066167f25d4c56bd55f3ba79`
* `.../universalraum-native-operations-ground-response-20260915/RESULTS.md` — `fa8e33605ebeff86b8438bd52213b3acb0b3edd12a4b9d4eb44ce6d3ec6b37dd`
* `.../TFPT_Universalraum_Minimale_Fortsetzung_2026-09-15_v1.6.1.md` — `6e0a29471506d374ecd386ada2d3a05c8f43cf346568306feeb736586b9256ef`
* `.../source-ground-response-20260920/PROOF.md` — `9f12b1a0e44e1954329f9362c02894776dd79ff20e01328c9af5391c729196c4`
* `.../source-dynamics-selection-20260920/PROOF.txt` — `03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2`
* `.../modular-source-selection-audit-20260917/RESULTS.md` — `2d93e640cb38f69c9f2e633f0f624c169c8637579431ffad464c544a714e14c8`
