# Eine konkrete Schnittstelle: die 820 Stromprodukte als Vier-Majorana-Operatoren

21. September 2026 · UR.SOURCE.SYMMETRIC_CAR_INTERFACE.01 · PARTIAL

**Der vollständige positive 820er Produktbereich lässt sich in der vorhandenen freien D8-Fermiondarstellung als ein bestimmter Raum von Vier-Majorana-Operatoren ausschreiben.** Die Abbildung erhält Norm und alle acht internen Cartanladungen. Sie erhält außerdem L0 und damit jeden fest vorgegebenen Generator L0+δQ auf dem gemeinsamen geraden Sektor. Für den bereits verwendeten Viertelholonomie-Generator ist die gesamte Zeitantwort unten explizit angegeben.

Damit ist ein konkreter Teil der verlangten Schnittstelle berechnet. Die erste Voraussetzung bleibt sichtbar: Verwendet wird die bereits dokumentierte markierte D8_1-Realisierung durch 16 freie Majoranas mit gemeinsamem Vakuum, Stressoperator und Bosonisierungs-Konvention. Ihre Herkunft als acht unabhängige komplexe Kanäle aus dem primitiven P1-Nahtkern wird hier nicht hergeleitet. Die 16 Majoranas sind auch nicht die 64 Spinorströme oder bereits die beobachteten Raumzeitfermionen.

## 1. Welche Operatoren die beiden Kanäle tatsächlich sind

Sei V=A⊕B mit A=(10,1) und B=(1,6). Für die 16 Majoranafelder gilt in der freien NS-Darstellung

\[
\{\chi^a_r,\chi^b_s\}=\delta^{ab}\delta_{r,-s},\qquad
\chi^a_r\Omega=0\quad(r>0).
\]

Auf konformem Grad zwei zerfällt die gerade CAR genau in

\[
\mathcal H_{\rm even}[2]=(V\otimes V)\oplus\Lambda^4V,
\qquad 2076=256+1820.
\]

Der erste Anteil besteht aus einem Erzeuger bei −3/2 und einem bei −1/2. Der zweite besteht aus vier Erzeugern bei −1/2. Die beiden Anteile sind im Fock-Vakuum orthogonal.

Unter der festgelegten Spin(10)×Spin(6)-Wirkung findet man

\[
\Lambda^4(A\oplus B)=\Lambda^4A\oplus
(\Lambda^3A\otimes B)\oplus(\Lambda^2A\otimes\Lambda^2B)
\oplus(A\otimes\Lambda^3B)\oplus\Lambda^4B.
\]

Die relevanten Summanden sind genau

\[
\boxed{\mathcal H_{720}=\Lambda^3A\otimes B,\qquad
\mathcal H_{100}=A\otimes(\Lambda^3B)_{10}.}
\]

Es gilt Λ³6=10⊕bar(10); die markierte Chiralität des ursprünglichen F=(16,4) wählt den bezeichneten Zehner. Beide Zieltypen kommen jeweils einmal vor. Im Zweiersektor V⊗V kommt keiner von ihnen vor.

Konkrete Felder sind daher

\[
\mathcal O_{abc;\mu}(z)=:​\chi^a\chi^b\chi^c\chi^{10+\mu}​:(z),
\]

für den 720er Raum, und

\[
\mathcal O_{a;\mu\nu\rho}(z)
=:​\chi^a\,[P_{10}(\chi_B\wedge\chi_B\wedge\chi_B)]_{\mu\nu\rho}​:(z)
\]

für den 100er Raum. In einer orientierten reellen Sechserbasis ist auf Dreiformen *²=−I. Mit der im Checker festgelegten Orientierung lautet P10=(I+i*)/2. Der +e1+e2+e3-Höchstgewichtsvektor fixiert, welcher der beiden konjugierten Zehner gemeint ist. Das Projektorbild hat exakt Dimension zehn; ein freier gewünschter Skalarraum wird nicht ergänzt.

## 2. Die vollständige Basisabbildung

Paare die Majoranas gemäß der markierten komplexen Polarisation zu ψ_k^± mit Cartanladungen ±e_k. Die Standard-Boson-Fermion-Korrespondenz identifiziert die ganzzahlige Gittervertex-Superalgebra mit dieser CAR; ihre gerade D8-Unteralgebra ist die gemeinsame Ecke mit der E8-Quelle. Die Isomorphie ist ein etablierter Satz, hier auf die bezeichnete Produktkarte angewandt; siehe [Yanagida, Boson-fermion correspondence from factorization spaces](https://arxiv.org/abs/1611.06100).

Schreibe p=r+s und v=r−s für zwei der tatsächlichen markierten Halbwurzeln. Für r·s=0 besitzt p genau vier Einträge ±1. Deshalb gilt in einer konsistenten Kokzyklus-Konvention

\[
\mathcal B\mathcal S(r\odot s)
=\sqrt2\,\varepsilon(r,s)\eta_p
\prod_{k\in\operatorname{supp}p}^{\rm geordnet}
\psi_{k,-1/2}^{\operatorname{sgn}p_k}\Omega.
\]

Für r·s=−1 hat p zwei nichtverschwindende Einträge, an Positionen i,j. Der Vektor v ist ausschließlich auf den übrigen sechs Positionen getragen. Damit

\[
\mathcal B\mathcal S(r\odot s)
=\frac{\varepsilon(r,s)\eta_p}{\sqrt2}
\sum_{k\notin\operatorname{supp}p}v_k
\left(\psi_{k,-1/2}^+\wedge\psi_{k,-1/2}^-\wedge
\psi_{i,-1/2}^{p_i}\wedge\psi_{j,-1/2}^{p_j}\right)\Omega.
\]

Die Reihung trägt die tatsächlichen CAR-Vorzeichen. Es entsteht kein Anteil mit einem −3/2-Erzeuger: Der Oszillator v ist zu allen besetzten Impulskoordinaten disjunkt. Für r·s=1 und identische Wurzeln verschwindet die Karte.

Dies ist eine Abbildung aller 2080 Eingänge, keine Existenzbehauptung allein aus Dimensionen. Die direkte Umsetzung besitzt 4000 nichtverschwindende Einträge. Jeder Ausgabekoordinatenvektor liegt nachweislich im 720er oder gewählten 100er Raum. Sämtliche Ladungsblöcke haben genau die ursprüngliche Gram-Matrix mit Spektrum 8^100⊕4^720⊕0^1260.

Die zwei Höchstgewichte machen die Normierung anschaulich. Für p=(1,0,0,0,0,1,1,1) tragen vier orthogonale Strompaare bei; ihre mit ε gewichtete normierte Summe hat Koeffizient 1/2. Nach S/√8 entsteht ein normierter Vier-Fermion-Zustand. Für p=(1,1,1,0,0,1,0,0) tragen zwei Paare bei; der Koeffizient ist 1/√2 und S/2 liefert wieder einen normierten Vier-Fermion-Zustand. Die Gruppenwirkung erzeugt daraus die vollständigen einmaligen Summanden.

Die numerische Phase η_p wird durch die einmal festgelegte Bosonisierung bestimmt. Im endlichen Gram- und Bildtest dürfen ε und die pro Ladung gemeinsame Phase η_p weggelassen werden: Sie konjugieren die Grams unitär. Ein vollständiger erneuter Vergleich aller historischen Chevalley-/Bellphasen wird damit nicht behauptet. Die Erhaltung der vollständigen Operatorprodukte folgt analytisch aus der konsistent gewählten Vertexalgebra-Isomorphie, nicht aus einem bloßen Gramvergleich.

## 3. Ladungen, Zustand und Zeit in derselben Abbildung

Jeder Term des Bildes hat exakt den Impuls p=r+s. Ein zusätzliches Paar ψ_k^+ψ_k^- trägt Ladung null. Deshalb erhält die Karte **alle acht** Cartanladungen Q_k, nicht nur eine Gesamtzahl:

\[
\mathcal B Q_k=Q_k^{\rm CAR}\mathcal B.
\]

Bosonisierung erhält das gemeinsame Vakuum und den Stressoperator. Daher gilt auf der gemeinsamen geraden D8-Ecke für jede feste Cartankombination Q und jeden festen δ

\[
\boxed{\mathcal B(L_0+\delta Q)
=(L_0^{\rm CAR}+\delta Q^{\rm CAR})\mathcal B.}
\]

Das impliziert die gesamte Zeitentwicklung per Funktionalkalkül. Es ist keine Anpassung von Eigenwerten an einen gewünschten Rand-Hamiltonoperator.

Die bisherige mikroskopische Einkanalquelle liefert H=L0−Q/4. Wird der **bereits vorausgesetzte** Achtkanal-Lift mit derselben Holonomie benutzt und Q=ΣQ_k gesetzt, hat das positive 820er Bild die folgende vollständige Antwort:

| Q | Energie E=2−Q/4 | Vielfachheit |
|---:|---:|---:|
| 4 | 1 | 35 |
| 2 | 3/2 | 200 |
| 0 | 2 | 345 |
| −2 | 5/2 | 210 |
| −4 | 3 | 30 |

Diese Energien sind dimensionslose Anregungen dieses bedingten gemeinsamen CAR-Sektors, keine beobachteten Teilchenmassen und keine neu hergeleitete physische Zeitskala. Die Zahl acht unabhängiger Kanäle folgt nicht aus den acht Querzeilen der einzelnen QWZ-Quelle; deren führender Stromrang ist laut vorhandenem Ausschluss eins.

Für eine orthonormale, nach Q aufgelöste Bildbasis O_aΩ lautet die Vakuumantwort exakt

\[
\langle O_a\Omega,e^{-\tau H}O_b\Omega\rangle
=\delta_{ab}\exp[-\tau(2-Q_a/4)].
\]

Ohne Viertelholonomie, unter reinem L0, wird daraus δ_ab e^(−2τ). Für örtliche orthonormale Vier-Majorana-Felder ist die konforme Zweipunktfunktion δ_ab/(z−w)^4, mit dem ersten Feld adjungiert. Allgemeine gemeinsame Mehrzeitantworten sind die Wick/Pfaffian-Summen der zugrunde liegenden Majorana-Kerne unter derselben Zeit. Dies ist eine Operator- und Zustandsabbildung innerhalb der freien Quelle; kein zusätzlicher positiver RR-Block wird verwendet.

Die Rechnung entscheidet die Zeit auf dieser geraden Produktecke. Sie bestimmt nicht die bisher offene relative Zeit der Ramond-Intertwiner oder den vollständigen mikroskopischen DHR-Kovarianzkokzyklus. Zwei Erweiterungen mit derselben NS-Einschränkung können hier weiterhin dieselbe Antwort besitzen.

## 4. Was damit für die physische Schnittstelle entschieden ist

Der 820er Raum ist als Raum bestimmter zusammengesetzter Fermionoperatoren identifiziert. Insbesondere müssen keine 820 unabhängigen neuen skalaren Teilchensorten eingeführt werden. Der alte Bell10-Nachfahrenraum und der 720er Nachbar sind innerhalb dieser bestehenden Darstellung an dieselbe CAR, denselben Zustand und dieselbe bezeichnete Zeit anschließbar.

Der Anschluss legt aber auch den Typ fest: Es handelt sich um **gerade Vier-Fermion-Operatoren der Vektorfelder (10,1)⊕(1,6)**. Es sind keine 64 elementaren ungeraden (16,4)-Felder. Die 64 Eingangsströme sind relativ zur D8-CAR Spinfields/Sektorintertwiner; ihre Paarprodukte kehren in den geraden Sektor zurück.

Auch die Existenz quartischer Operatoren setzt noch keinen quartischen Term in die Energie. Im unveränderten quasifreien Modell bleibt der fundamentale Fermiongenerator quadratisch. Seine amputierten elementaren Wechselwirkungsvertices verschwinden; zusammengesetzte Observablen können trotzdem nichttriviale höhere Korrelatoren besitzen. Eine Hubbard–Stratonovich-Umformung würde erst einen bereits gegebenen Vier-Fermion-Kopplungsterm umschreiben, aber dessen Auswahl oder Stärke nicht aus dieser Produktkarte herleiten.

Der direkte skalare Dreipunkttest ist in dieser vorhandenen Quelle sogar exakt entscheidbar:

\[
\boxed{\langle\Omega,\mathcal O_{820}(x)\,\chi^a(y)\chi^b(z)\Omega\rangle=0.}
\]

Nach Normalordnung können die vier Fermionfaktoren von O820 nur mit äußeren Faktoren kontrahieren; zwei äußere Felder reichen nicht. Das gilt für alle getrennten Orte und Zeiten im gemeinsamen quasifreien Zustand. Dieselbe Null ist bereits vom inneren Darstellungstyp erzwungen: V⊗V enthält keinen der beiden 820er Summanden. Sie ist daher keine numerisch kleine oder wegkalibrierbare Antwort. Der erste mögliche freie Formfaktor hat vier äußere Majoranafelder. Die behauptete skalare Kopplung an zwei **(16,4)-Materiefelder** kann man folglich nicht durch Austausch dieser Beine gegen die schon verfügbaren Vektormajoranas herstellen. Genau die richtige geladene Spinorfeld-Erweiterung bleibt dafür nötig.

Die erste physische Herkunftsfrage liegt deshalb jetzt genauer: Realisiert der ursprüngliche Nahtprozess gerade diese lokale 16-Majorana-Quelle samt markierter Zeit und geladenem Erweiterungssektor, und enthält seine eigene Wirkung einen nichtverschwindenden Koeffizienten für die gefundenen Operatoren? Einen solchen Koeffizienten einzusetzen wäre eine neue Annahme. Für beobachtete chirale Materie bleibt außerdem eine Orts-/Lorentz- und Feldabbildung nötig.

**Die vollständige verlangte physische Schnittstelle ist noch nicht gefunden.** Der hier geschlossene Teil ist ihre explizite innere Produkt-, Zustands- und Zeitabbildung im bestehenden bedingten CAR-Modell. Diese Grenze bleibt Bestandteil des Ergebnisses, statt aus dem gefundenen quartischen Operator bereits einen physikalischen Yukawa-Mechanismus zu machen.

## Abgleich mit dem bereits vorhandenen TFPT-Yukawasektor

**Dieser Kandidatentest öffnet die bestehenden TFPT-Flavor- und Yukawa-Ergebnisse nicht wieder.** Das am 21. September 2026 erneut gelesene Originalledger führt die Quarkverhältnisse unter FLAV.QRATIO.01 und FLAV.RIGID.02 als geschlossen auf dem hergeleiteten Selektorstratum. FLAV.LEPTONC.01 führt die exakten Leptonkoeffizienten (16/7, 4/3, 7/6). FLAV.UPOINT.01 führt die Reduktion der neun geladenen Fermionamplituden auf den gemeinsamen Skalenanker v_geo als [I]+[A]. Das ist eine Wiedergabe des bestehenden, typisierten Ledgerstands; die vorliegende Rechnung liefert keinen neuen unabhängigen Gesamtbeweis dieser Flavor-Herleitungen.

CONTRACT.QFT4D.DIRAC.01 und seine Originalquelle v250 unterscheiden bereits ausdrücklich zwischen den vorhandenen Yukawadaten und der Konsistenz ihres Operatoranschlusses. Nachfolgende PS.DIRAC- und PS.NCG.FLUCT-Claims enthalten weitere positive endliche Operator- und Higgsresultate. Deren bereits erledigte Teilaufgaben werden hier nicht erneut zu offenen Aufgaben erklärt.

Die oben bewiesene Dreipunkt-Null gilt für zwei elementare **Vektor-Majoranafelder** in der bezeichneten freien Quelle. Sie widerlegt weder die TFPT-Yukawadaten noch eine Kopplung an korrekt realisierte Spinor-Materiefelder. Das verbleibende Ziel dieses Quellenzweigs ist daher eine aus dem ursprünglichen Nahtprozess begründete Feld-, Zustands- und Zeitabbildung, die die vorhandene TFPT-Flavorstruktur als physische Kopplung reproduziert. Der 820er Kanal ist daran zu prüfen; er ersetzt die bestehende Herleitung nicht.

## 5. Herkunft, Neuheitsgrenze und Prüfung

Die freie CAR/D8/E8-Korrespondenz ist Standardmathematik und vorhandener TFPT-Bestand. Der Korpus kannte bereits den 100+100-dimensionalen Λ4(16)-Recordbereich sowie einen engeren E8-Stromprodukt/Bell-Anschluss. Hier neu zusammengeführt und vollständig ausgewertet wurden die gesamte 2080→820-Produktkarte, ihre konkrete Vier-Majorana-Basisform, der Ausschluss jedes Zweier-Modenanteils und ihr gemeinsamer Ladungs-/Zeittransport einschließlich der oben angegebenen Viertelholonomie-Antwort.

`checker.py` prüft direkt die ursprüngliche gepinnte 64-Wurzelmenge, sämtliche nichtverschwindenden CAR-Einträge, das Familien-Hodgeprojektorbild, alle Ladungen und Grams sowie die beiden Höchstgewichtsnormalisierungen. Normaler und optimierter Lauf sind identisch. Das unabhängige `CAR_INTERFACE_REVIEW.md` bestätigt den Operatoranschluss und dokumentiert seine Voraussetzungen. Der zusätzliche gemeinsame Hδ-Transport folgt aus dem explizit geprüften Cartantransport und der analytischen stressverträglichen Bosonisierung.

Keine Einsetzung von Gamma, Vaux oder Zielenergien 3,4,5. Keine neue Geometrie oder Wechselwirkung. Keine Paper-/Ledger-Promotion, keine empirische Aussage und kein geschlossenes T1–T8-Gate.
