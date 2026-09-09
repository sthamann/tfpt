# TFPT-Fortsetzung: neutraler mikroskopischer Grenzwert und Wechselwirkungsherkunft

2026-09-08. Lokal auf b803b7e5. Die physikalischen Quellen und ihre
festgelegten Parameter bleiben unverändert. Kein Commit/Push, kein
Paper-/Webseitenupdate und kein T1–T8-/TOE-/RH-Abschluss.

## 1. Die vorher offene mikroskopische Paarverbindung ist geschlossen

[Vollständiger Beweis](README.md), mit unabhängigem internem Mathematikreview:
Für den bisherigen mass-1-, width-8-, r=1-QWZ-Quellsektor und
delta_N=4N^(-3/4) gilt für den vollständigen normalgeordneten neutralen
Paar-Erwartungswert C_N^circ, gleichmäßig über sämtliche Gitterendpunkte,

```
sup_(a,b) |Z_t² C_N^circ(a,b) - K_t(b-a)| = O(N^-1/16) -> 0.
```

Mit der kontrollierten Gitterinterpolation folgt auch der L1-Grenzwert

```
Z_t² C_N^circ(a,b) -> (1-exp(2pi i(b-a)))^(-1/4).
```

Der analytische Zweig und die Endpunkt-Normierung sind dieselben wie im
vorherigen Current-Vertrag. Es ist nicht nur eine Folge kleiner
Determinanten und nicht nur ein Betrag oder ein getrenntes Randmodell.
Die vollständige Quellenamplitude, ihre komplexe Phase und der Restraum
werden im Beweis berücksichtigt. Die Kernelpositivität bleibt erhalten.

Die drei neu zusammengeführten Teile sind:

| Teil | Ergebnis |
| --- | --- |
| [Tatsächliches J/J-Symbol](../source-current-symbol-match/README.md) | Exakte Halbzellphase und Diagonalkonstante, echte transverse Profile; Operatorfehler O(N^-3/2) |
| Niedriger R-Rest | Nur wirkliche Bottom-Randmoden, kein versteckter zweiter Top-Modus; ideales J/R-Element exakt null durch Spin-Symmetrie |
| Vollständiger Zeitverlauf | Hohe Energieblöcke und Ausflüge der Referenzrahmen bleiben durch explizite Schranken kontrolliert; I_sharp,ref=O(N^-1) |

Die bereits zuvor kontrollierte Energielinearisierung dominiert den
normierten Gesamtfehler mit O(N^-1/16). Eine gemeinsame Halbzelltranslation
verbessert den Vergleich, ohne die normalgeordnete Referenzamplitude zu
ändern. Der physikalische Hamiltonian wurde nicht passend verändert.

Die Schranken haben große Vorfaktoren und sind asymptotische Aussagen,
keine präzisen Fehlerzertifikate für kleine N. Die endlichen Vollquellen-
Historienfehler bei N=8,16,32 sind beispielsweise 0.363/0.162/0.0456;
das sind gewöhnliche Quadraturdiagnostiken, nicht die Beweisgrundlage.

## 2. Clock: welche Rechnung echte Wechselwirkung erzeugen kann

[Quellen-Audit und exakte Algebra](../clock-interaction-provenance/README.md):
Die ursprüngliche 16-Majorana-Dynamik bleibt unter quadratischer Evolution,
stetigem Lie/BCH-Abschluss und regulärer rein fermionischer Gaussian-
Elimination quadratisch. Auch ein nichtnuller Wick-Vierpunktterm ist kein
neuer Wechselwirkungsvertex. Diese konkrete bisher denkbare Ableitungsroute
zum quartischen Clock-Zeugen ist damit ausgeschlossen.

Ein tatsächlich vorhandener anderer Parent liefert dagegen eine passende
Art von Mechanismus: elektrische Rotorenergie und Materietransport.
Mit den dort bereits gesetzten Koeffizienten a=1/12, kappa=1/100 folgt

```
H_E = (kappa/2) E²,
V = a (U c1* c0 + U* c0* c1), [E,U]=U,
[V,[H_E,V]] = kappa a² [n0+n1-2n0 n1+2E(n0-n1)].
```

Der reine Vierfermionen-Anteil ist -(1/7200) q0 q1. Er wurde aus der
vorhandenen gesamten Kantenliste nachgerechnet, nicht als freie Kopplung
eingesetzt. Ursache sind die nichtkommutierenden dynamischen
Transportkoeffizienten. Das ist eine Kommutatorkomponente auf einem
gemeinsamen Kern, noch kein kontrolliert eliminierter effektiver Hamiltonian.

**Weiter fehlend:** Dieser Rotorparent ist noch nicht typgerecht mit der
16-Majorana-Clock identifiziert. Gemeinsame Clock-Ladung, Gauss-Gesetz,
Boundary-Zuordnung und Zustand müssen erhalten und aus der Quelle begründet
sein. Eine bloße Gleichsetzung des Koeffizienten mit g3 oder g4 wäre kein
Nachweis. Bei ausschließlich materiellem O bleibt n3 sogar zentral in der
O-fixen Algebra; das ist eine zusätzliche allgradige Symmetriegrenze.

## 3. Die nächsten beiden lasttragenden Beweise

1. **Vom Zweipunktkern zum Vierpunktprodukt derselben Quelle.** Die aktuelle
   grobe Schranke darf nicht blind vervielfacht werden: Für vier Endpunkte
   ergibt Z_t^4 Aref I_lin mit dem bisherigen M~sqrt N zunächst nur O(1).
   Ein kleineres, weiterhin wachsendes Hilfsfenster oder eine stärker
   lokalisierte Energielinearisierung ist der nächste konkrete Ansatz.
   M~N^(3/8) ist ein gezielt zu prüfender Vergleichsparameter, kein neuer
   physikalischer Parameter. Erst nach Revalidierung aller Schritte folgt
   daraus ein normierter Vierpunkt-Satz. Gemeinsame Felddomänen und
   Austausch/Lokalität bleiben darüber hinaus erforderlich.
2. **Elektrische Transportdynamik mit der Clock verbinden.** Prüfen, welche
   gemeinsame Ladung von Materie und Transportträgern tatsächlich erhalten
   ist und ob der vorhandene Rotorparent dafür eine Quellenabbildung liefert.
   Das zielt auf den konkreten fehlenden Wechselwirkungsmechanismus,
   nicht auf weitere Gaussian-Umschreibungen derselben freien Quelle.

Der Zweipunkt-Satz löst keine vierdimensionale Rekonstruktion, keine
chirale spiegel-freie Materie, Flavour-/Massenwahl oder Spin-2-Gravitation.
Auch acht Kopien des Grenzkerns dürfen wegen seiner Koinzidenzsingularität
nicht ohne neue Distributions- und Quellenidentifikation hochmultipliziert
werden. Der Fortschritt liegt in einer geschlossenen konkreten Teilpflicht
und einer präziser lokalisierten nächsten Verbindung.

## 4. Reproduktion und Integrationsstatus

75 Tests wurden in dieser Runde jeweils normal und optimiert ausgeführt:
27 neue und 48 gezielte Regressionen. [Prüfprotokoll](TEST_RESULTS.md).
Die unabhängigen internen Mathematikreviews sind keine externe Begutachtung
und kein Beweisassistenten-Zertifikat. Alte Quellen, fremde Arbeitszweige
und frühere eingefrorene Forschungsstände wurden erhalten.
