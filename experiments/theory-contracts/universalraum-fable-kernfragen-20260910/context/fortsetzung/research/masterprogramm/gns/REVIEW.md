# Unabhängiger Gegenreview: GNS, Dynamik und geometrischer Transport

10. September 2026. **PASS: keine offene mathematische Beanstandung im geprüften Umfang.** Der Bericht beweist einen bedingten Transport gegebener Daten. Er behauptet korrekt keine Ableitung der TFPT-Prozessquelle aus GNS. Die empfohlene Präzisierung des geometrischen Definitionsbereichs wurde vom Autor übernommen und anschließend nachgeprüft.

Geprüft wurden `GNS-DYNAMIK-GEOMETRIE.md`, `check_gns.py` und `checks.json`. Die gespeicherten 50 Kontrollen sind konsistent aufgelistet; Datei-Hashes stimmten auch nach der Präzisierung mit dem Prüfer und Bericht überein. Die Suite wurde im Review nicht wiederholt. Final geprüfter Bericht-Hash: `7caa0bf19beffa3e83d76d3a6435bda11d651c3baa046a53f4927e5b1d88925d`; Prüfer-Hash: `4a08a9fddb8a80f446d57b77a4b7a3cbbb5d52d53e839ecf08db817f966ebed2`.

## Bestätigte Aussagen

1. **GNS-Isomorphismus.** Die Definition \(V\pi_0(a)\Omega_0=\pi_1(\Phi(a))\Omega_1\) ist wegen Zustandserhaltung wohldefiniert auf den Nullquotienten und isometrisch. Surjektivität von \(\Phi\) liefert dichtes Bild; Vollständigkeit macht das isometrische Bild geschlossen. Der erhaltene Unitär ist wegen der vorgeschriebenen Wirkung auf zyklischen Vektoren eindeutig. Treue der Zustände ist hierfür nicht nötig. Bei einem bloßen Homomorphismus reicht das Bild nur zum angegebenen zyklischen Teilraum. Der Verweis auf [Landsman, Konstruktion 2.9.4 und Proposition 2.9.5](https://arxiv.org/pdf/math-ph/9807030) wurde an den tatsächlichen Originalstellen abgeglichen.

2. **Dynamik einschließlich Domänen.** Zustandsinvarianz und punktnormstetige Automorphismengruppen genügen für die kanonischen starkstetigen unitären Gruppen. Aus \(VU_0(t)=U_1(t)V\) folgt für jeden Vektor \(\psi\)
   \[
   \frac{U_1(t)V\psi-V\psi}{t}
   =V\frac{U_0(t)\psi-\psi}{t}.
   \]
   Existiert der rechte Grenzwert, existiert der linke; Anwendung von \(V^*\) beweist die Umkehrung. Damit stimmen die vollständigen Generator-Domänen unter \(V\) überein, nicht nur formale Ausdrücke auf einer Testmenge. Die Vorzeichenkonvention \(U(t)=e^{itK}\) ist konsistent.

3. **Positiver Zustand versus positive Energie.** Für den treuen thermischen Zustand auf \(M_2\) ist \(\Omega=\sqrt\rho\) zyklisch im Hilbert–Schmidt-Raum. \(K(E_{ij})=(h_i-h_j)E_{ij}\) liefert tatsächlich \(0,0,+\varepsilon,-\varepsilon\). Der Bericht bezeichnet diese Differenzenergie korrekt als kanonischen GNS-Generator; er verwechselt sie nicht mit einem instabilen materiellen Hamiltonoperator. Positivität des Zustands allein ergibt keine Vakuum-Spektralbedingung.

4. **Diskrete Clock.** Die zwei angegebenen positiven Hamiltonoperatoren haben denselben Ein-Schritt-Unitär und unterschiedliche Halbzeitwirkung auf \(E_{01}\). Der relative Faktor ist exakt \(e^{-i\pi}=-1\). Die beiden erhalten auch die Clockmarke, weil sie mit ihr kommutieren. Das Gegenmodell betrifft ausdrücklich nur die genannten diskreten Daten; zusätzliche TFPT-Relationen wurden nicht als erhalten behauptet.

5. **Geometrischer D ist nicht automatisch ein Algebra-Generator.** Die angegebene Konjugation sendet \(\sigma_z\) korrekt auf **\(+\sigma_y\)**. Sie verlässt die diagonale Algebra. Zugleich gilt dort \(\|[\sigma_x,\operatorname{diag}(a,b)]\|=|a-b|\); der Abstand der beiden reinen Zustände ist deshalb eins. Das ist ein sauberer Gegenzeuge gegen die automatische Identifikation von geometrischem D und interner Automorphismengruppe.

6. **Keine falsche Quelleindeutigkeit.** Eindeutigkeit wird überall auf das vorgegebene Paar \((A,\omega)\), die gewählte Quellenabbildung und gegebenenfalls die zusätzlichen Generatoren begrenzt. Die Auswahl von Algebra, Zustand, physikalischen Relationen, Raumzeit und Dynamik aus TFPT bleibt ausdrücklich offen.

## Erledigte Präzisierung in §6

Die Aussage über Spektraldistanzen ist richtig, wenn die glatten Algebren unter \(\Phi\) tatsächlich vollständig identifiziert sind. Der finale Bericht verlangt nun ausdrücklich

\[
\Phi(A_0^\infty)=A_1^\infty,
\qquad \varphi_1=\varphi_0\circ\Phi^{-1},
\qquad \psi_1=\psi_0\circ\Phi^{-1}.
\]

Die Elemente sollen die jeweiligen Domänen von D erhalten und beschränkte Kommutatoren besitzen. Alternativ verwendet man die maximalen Algebradomänen mit diesen Eigenschaften; deren Bijection folgt direkt aus dem bereits verlangten vollständigen D-Intertwiner. Dann ist \(L_1(\Phi(a))=L_0(a)\), und \(\Phi\) bildet die selbstadjungierten Lipschitz-Einheitsbälle bijektiv aufeinander ab. Also

\[
d_{D_1}(\varphi_1,\psi_1)=d_{D_0}(\varphi_0,\psi_0),
\]

auch bei unendlichem Wert. Eine lediglich gemeinsame **kleinere** Testalgebra rechtfertigte dagegen nicht ohne Zusatzargument die Supremumswerte über unabhängig größere Zielalgebren. Auch diese Grenze ist im finalen Bericht explizit enthalten. Die Präzisierung ist damit erledigt; sie ist kein Gegenbeispiel gegen den korrekt bedingten Satz. Die Hauptdateien wurden vom Reviewer nicht verändert.
