# Bestandsaufnahme: sechs Follow-ups und offene Problemfelder

Basierend auf einer systematischen Untersuchung sämtlicher vorhandener Unterlagen (Hauptdokument v1.4, Update v1.4, Follow-up-Katalog sowie den aktuellen mathematischen Ableitungen) folgt hier die Bestandsaufnahme aller sechs zentralen Follow-up-Fragen sowie der weiteren offenen Problemfelder (T1–T8, RH, Kosmologie) — einschließlich der exakt geschlossenen Beweisabschnitte, der harten mathematischen Obstruktionen und der noch verbleibenden Übergänge.

---

## 1. Follow-up 1: Steuerung des Labors (Controller-Herkunft)

### Neu bewiesen / gelöst

**Exakte Kontrollobstruktion durch relative Phase.** Aus einem rein unkontrollierten Blackbox-Zugriff \(U\) lässt sich keine kohärente Kontrolle

\[
\operatorname{c}(U) = \lvert 0\rangle\langle 0\rvert \otimes I + \lvert 1\rangle\langle 1\rvert \otimes U
\]

gewinnen. Für \(U = I\) und \(U' = e^{i\phi}I\) sind die unkontrollierten Kanäle auf Dichtematrizen identisch, die kontrollierten Versionen führen jedoch auf orthogonalen Kontrollzuständen zu messbaren Phasenunterschieden. Ein autonomer Controller benötigt zwingend eine physische Phasenreferenz.

**Endliche autonome Programmeinbettung.** Ein gegebenes diskretes Programm \(U_0, \dots, U_{L-1}\) lässt sich autonom über einen \(L\)-stufigen Schieberegister-Schritt

\[
W = \sum_{j=0}^{L-1} \lvert j+1 \bmod L\rangle\langle j\rvert \otimes U_j
\]

unitär einbetten.

**Reset-Kapazitätsschranke.** Ein zyklischer Reset eines \(d\)-dimensionalen Systems auf einen festen reinen Zustand ohne Entropieabfluss erfordert nach \(k\) Zyklen für beliebige Eingänge einen Umgebungsraum von mindestens Dimension \(d^k\) (für \(N\) Zellen à \(d=256\) mindestens \(8Nk\) Bits Informationskapazität). Ein geschlossenes endliches System kann keinen dauerhaft kostenlosen Reinzustandsreset bereitstellen.

### Was zur vollständigen Lösung noch offen ist

Die native Herleitung sämtlicher Handgriffe (Resonanztransfer, Belegungsprojektion, isolierte Kantenadressierung) direkt aus den algebraischen \(E_8\)-Erzeugenden ohne extern vorgeschriebenes Steuerprotokoll.

---

## 2. Follow-up 2: Auswahl der Vermittlerarchitektur

### Neu bewiesen / gelöst

**Algebraisches Auswahlkriterium über lokale Ladungserhaltung.** Betrachtet man die Modenbasis mit lokalen Ladungen

\[
Q_v = n_f(v) + \sum_m q_{vm} n_m
\]

und Paarübergängen \(T_{e,m} = b_m^\dagger K_e\) (\(e = \{i, j\}\)), so erzwingt

\[
[Q_v, T_{e,m}] = (q_{vm} - \delta_{vi} - \delta_{vj}) T_{e,m} = 0
\]

für alle Vertizes exakt \(q_{vm} = \delta_{vi} + \delta_{vj}\).

Derselbe Vermittlermodus kann nicht zwei disjunkten Kanten gleichzeitig zugeordnet sein. Unter der Bedingung strikt erhaltener lokaler Belegungsladungen \(Q_v\) ist die **kantenlokale Architektur mathematisch zwingend** gegenüber der zellgeteilten Bank ausgewählt.

### Was zur vollständigen Lösung noch offen ist

Der formale Beweis, dass diese Erhaltungsgrößen \(Q_v\) und die diagonale Modenbasis nativ aus den TFPT-Wurzeln folgen und nicht als Wunschannahme postuliert werden.

---

## 3. Follow-up 3: Vierfachentartung des Grundniveaus und Singulettblock

### Neu bewiesen / gelöst

**Exakte Symmetriegruppe.** Der Clebsch-Graph (16 Ecken, 40 Kanten) hat die vollständige Automorphismengruppe \(\mathcal{G} = (\mathbb{Z}_2)^4 \rtimes S_5\) mit Ordnung \(\lvert\mathcal{G}\rvert = 1920\).

**18-Typ-Zerlegung des 24.024-dimensionalen Singuletts.** Die Zerlegung des \(S_{16}\)-Spechtmoduls \((4,4,4,4)\) unter \(\mathcal{G}\) wurde ganzzahlig aufgeschlüsselt. Der triviale Block hat Dimension 28, der größte Multiplizitätsblock Dimension 262.

**Explizite Dimensionsreduktion.** Für das beobachtete Quartett existiert ein exakter hermitescher Projektor \(E_4 = P_H - P_G\) mit \(\operatorname{rank}(E_4) = 108 - 28 = \mathbf{80}\). Die Vierfachheit der Eigenwerte in diesem Block ist exakt symmetrieschützend.

**Vollraumschranken für \(F_{4,\mathrm{edge}}\).** Aus den Inhalten der Young-Tableaux folgt für die Sternterme \(\operatorname{spec}(A_v) \subset \{0, \dots, 8\}\), woraus rigoros \(0 \le F_{4,\mathrm{edge}} \le 896\, I\) folgt.

**Lineare Untergrenze.** Für \(t/\Delta = 1/20\) gilt

\[
H_{\mathrm{tr}} = H_0 + \frac{1}{800} F_{4,\mathrm{edge}} \ge \frac{47}{50} H_0 + \frac{39}{25} I.
\]

Ein zertifizierter nackter Nichtsingulett-Bound \(H_0 \ge 11{,}6\, J\) zusammen mit einer oberen Quartettenergie \(\le 12{,}45\, J\) schließt Nichtsinguletts vollständig aus.

### Was zur vollständigen Lösung noch offen ist

Rationale Intervallzertifizierung (Inertia-Beweis) auf dem reduzierten 80-dimensionalen Block sowie die analytische Beherrschung des Schrieffer-Wolff-Restterms der vollen Mikrodynamik.

---

## 4. Follow-up 4: Robustheit, Clockfehler und gekoppelte Zellen

### Neu bewiesen / gelöst

**9-Faktor-Filter im Eingangsraum.** Da der ideale Eingang \(\chi\), \(\Omega\) und der Echo-Zweig nur fünf der sieben \(M\)-Sektoren besetzen (\(M \in \{0, 1, 3, 4, 5\}\); \(M \in \{2, 6\}\) haben Gewicht 0), genügen im invarianten 352-dimensionalen Raum **9 statt 13 Filterfaktoren**. Die schwache Entwicklungszeit sinkt exakt um \(27{,}18\,\%\) von \(6345{,}66\,\hbar/\Delta\) auf **\(4620{,}61\,\hbar/\Delta\)** bei identischen idealen Rohwahrscheinlichkeiten (\(w^2/6\), \(w^4/6\), \(17w^4/192\)).

**Reine Zeitfehler-Toleranz.**

- Bei synchron mitlaufender Referenzphase genügt ein relativer Zeitfehler \(\lvert u\rvert \le \mathbf{2{,}8061 \cdot 10^{-4}}\) für eine bedingte Präparationsinfidelität \(1 - F_{\mathrm{prep}} \le 10^{-6}\).
- Bleibt die Referenzphase auf dem Nominalwert stehen, verlangt dieselbe Schranke \(\lvert u\rvert \le \mathbf{3{,}9674 \cdot 10^{-5}}\).

**Exakt lösbare verschränkte Referenzfamilie.** Für \(N\) gekoppelte Zellen existiert über \(V_N = \prod \exp[-i\theta A_i A_{i+1}]\) (\(\theta = \pi/8\)) ein streng gapped Modell mit Gap \(2J\) und verschränktem Grundzustand \(\Psi_N\) (Schnittentropie \(0{,}600876\dots\) Bits). Unter lokalen Zyklenfehlern \(\varepsilon\) und Konvergenzrate \(r \approx 0{,}9754\) wird die globale Fehlerfortpflanzung über

\[
1 - F_{\Psi_N} \le N r^m + N \varepsilon \frac{1-r^m}{1-r}
\]

rigoros begrenzt.

### Was zur vollständigen Lösung noch offen ist

Ein geschlossenes Fehlerbudget unter Einschluss nichtkommutierender Hamiltonstörungen, Phasenrauschen und Messfehlern sowie die native Übertragung auf den propagierenden Grenzfall.

---

## 5. Follow-up 5: Gemeinsame Raumzeit, Chiralität und Gravitation (T3, T4, T5, T7)

### Gegenbeweise und Strukturschranken

**T2 (Halbladung).** Auf einer halbzahligen Ladungsleiter bewahren ganzzahlige Shifts die Parität \(\Pi = (-1)^{2Q}\). Eine Halbladungsoperation, die mit \(\Pi\) antikommutiert, kann nicht als Grenzwert ganzzahliger Shifts entstehen.

**T3 (Raumzeit).** Endliche Clebsch-Zellen lassen unterschiedliche Geschwindigkeits- und Überlagerungstensoren zu; eine Ausbreitungskegel-Auswahl auf \(3+1\) Dimensionen folgt nicht automatisch aus dem Graphen.

**T4 (Chiralität).** Drei Nullmoden bei vorgegebenem Fluss 3 beweisen keine Familienauswahl: Fluss 1 und 4 liefern entsprechend 1 bzw. 4 Moden. Vektorartige Paare werden durch den Nettoindex nicht unterdrückt.

**T5 & T7 (Gravitation).** Die exakte gekoppelte Referenzfamilie zeigt, dass stabiler Gap, Verschränkung und Lokalität noch **keinen masselosen Spin-2-Pol** erzeugen. Ein Projektor auf transversale spurlose Tensoren erzeugt keine neuen Energieniveaus unterhalb des spektralen Gaps.

### Was zur vollständigen Lösung noch offen ist

Eine einzige native feldtheoretische Skalierungsfamilie, die gleichzeitig Lorentz-Invarianz, chirale Standardmodell-Fermionen und ein dynamisches Graviton mit universeller Materiekopplung trägt.

---

## 6. Follow-up 6: Gemeinsame Parameter und empirischer Transfer

### Vollständige Ausschlussrechnung für einfaches \(c_3\)-Tuning

In der reinen Inflationsbranche gilt nach Eliminierung von \(N\):

\[
A_s (1 - n_s)^2 = \frac{c_3^7}{6\pi^2}.
\]

Um die ACT-DR6-Zentralwerte (\(n_s = 0{,}9752\), \(\log(10^{10}A_s) = 3{,}062\)) gleichzeitig zu treffen, müsste \(c_3\) von nominal \(1/(8\pi) \approx 0{,}0397887\) um \(-9{,}61\,\%\) auf **\(c_{3,\mathrm{ACT}} \approx 0{,}0359650\)** verschoben werden.

Setzt man dieses geänderte \(c_{3,\mathrm{ACT}}\) in die TFPT-Quellgleichung für die Feinstrukturkonstante ein:

\[
\alpha^3 - 2c_3^3\alpha^2 - \frac{4}{5} \cdot 41\, c_3^6 \log(1/\phi_s) = 0,
\]

so kollabiert der Wert von \(\alpha^{-1} \approx 137{,}0360\) auf **\(\alpha^{-1} \approx 167{,}8033\)**.

**Ergebnis.** Eine einfache isolierte Verschiebung des Parameters \(c_3\) zur Beseitigung der kosmologischen Spannung ist im fixierten Gleichungsvertrag mathematisch ausgeschlossen.

### Flavour-Diagnose

Ein konstanter Skalarüberlapp auf den drei Nullmoden liefert zwingend \(Y_{ab} \propto \delta_{ab}\) (drei identische Massen, keine CKM-Mischung). Eine Hierarchie erfordert nichtkonstante Modenprofile, die bislang nicht aus der Wirkung hergeleitet sind.

---

## 7. Zusammenfassender Lösungsstatus der sechs Follow-ups

| Follow-up | Rigoros neu gelöst | Weiterhin offen |
| --- | --- | --- |
| **1: Controller** | Phasenreferenzobstruktion bewiesen; Schieberegister-Programmeinbettung konstruiert; thermodynamische Worst-Case-Reset-Schranke (\(8Nk\) Bits). | Native Implementierung der Kontrolloperationen aus \(E_8\)-Erzeugenden. |
| **2: Architektur** | Lokale \(Q_v\)-Ladungserhaltung erzwingt kantenlokale Adressierung eindeutig. | Herleitung der \(Q_v\)-Ladungen aus der TFPT-Quelle. |
| **3: Quartett** | \(\mathcal{G} = (\mathbb{Z}_2)^4 \rtimes S_5\) (\(\lvert\mathcal{G}\rvert=1920\)); 18-Typen-Zerlegung; Reduktionsprojektor Rang 80; \(0 \le F_{4,\mathrm{edge}} \le 896\, I\); lineare Nichtsingulett-Schranke (\(H_0 \ge 11{,}6\, J\)). | Rationale Intervallzertifizierung auf dem 80D-Block; mikroskopischer Restterm. |
| **4: Robustheit** | 9-Faktor-Eingangsraumfilter (spart 27,2 % Entwicklungszeit); Zeitfehlertoleranzen (\(2{,}8 \cdot 10^{-4}\) bzw. \(3{,}97 \cdot 10^{-5}\)); gapped gekoppelte Referenzfamilie mit quantifizierter Fehlergrenze. | Vollständiges nichtkommutierendes Rauschbudget; nativer Vielzellen-Kontinuumslimes. |
| **5: Raumzeit & Gravitation** | Strukturelle Schranken: Gapped Verschränkung erzeugt keinen masselosen Spin-2-Pol; Paritätsbarriere für Halbladung; topologische Flussproben. | Native \(3+1\)D-Familie mit Lorentz-Invarianz, chiralem Maß und dynamischem Spin 2. |
| **6: Parameter** | Simultanes \(c_3\)-Tuning schlägt fehl (\(\alpha^{-1} \to 167{,}8\)); Flavour-Entartung bei flachem Higgs-Profil bewiesen. | Gemeinsame konsistente Wirkung mit Strahlungskorrekturen und Flavour-Hierarchie. |

Die nächsten methodischen Schritte konzentrieren sich auf den nunmehr exakt isolierten **80-dimensionalen Quartettblock** (Inertia-Zertifizierung) sowie die algebraische Herleitung der Kontroll- und \(Q_v\)-Operatoren aus der primären \(E_8\)-Struktur.
