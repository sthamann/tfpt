# Universalraum research — part 36

[Topic entry](../universalraum.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Die 128 zusätzlichen Bedingungen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex:30-38](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex#L30) · `section:659df24a89a62a734a06` · section

Der separate Prüfer verify_shadows.py importiert keinen ursprünglichen TFPT- oder RH-Code und keine Nullstellentabellen. Er enthält 126 exakte beziehungsweise symbolische Bedingungen und zwei numerische Kontrollen. Die Nummer der ersten Nullstelle im Eta-Diagramm ist ein ausdrücklich eingesetzter Referenzwert; das Diagramm ist kein eigener Nullstellensuchlauf.

## Zusätzliche Primärliteratur

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex:39-62](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex#L39) · `section:6848da5a76bc1d3d89ae` · section

Die folgenden Quellen wurden zur Erweiterung aufgerufen. Es handelt sich um gezielte Literaturauswahl, nicht um einen vollständigen systematischen Review aller Veröffentlichungen bis September 2026. Eigene Formeln, Gegenbeispiele und Illustrationen sind im Haupttext als solche bezeichnet. Neue Preprints bleiben als Preprints kenntlich. M. V. Berry, J. P. Keating: The Riemann Zeros and Eigenvalue Asymptotics. SIAM Rev

Explicit source references:

- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## Reproduktion der erweiterten Fassung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex:63-64](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/17_schatten_quellen.tex#L63) · `section:44e862561a8b2194a3be` · section

Das aktualisierte Quellpaket enthält beide unabhängigen Prüfer, beide Ergebnisdateien, die zusätzlichen drei Vektorplots, die LaTeX-Diagramme, das RH-Quellenmanifest und die ausgewählten Katalogeinträge. Die fünf neuen Hauptkapitel sind in dieselbe LaTeX-Datei eingebunden; ursprüngliche Textteile wurden nur um Versionshinweise und Querverweise ergänzt. Das fertige PDF wird weiterhin mit LuaLaTeX gebaut. Die beiliegen

## Die sechs neuen Quellen: geprüfte Korrekturen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L1) · `section:27233be87a9673f74e0f` · chapter

No opening prose excerpt; see the source.

## Was gegenüber v1.1 neu ist

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:3-5](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L3) · `section:6385cd9db19aa22b0551` · section

Die sechs zusätzlichen Unterlagen heißen im neuen Quellenregister N1 bis N6; die ursprünglichen S01 bis S11 bleiben unverändert. Ihr Audit trennt exakte endliche Identitäten, numerische Spektren und zusätzliche Modellannahmen. 100 eigene Bedingungen bestanden: 78 exakte beziehungsweise Integritätsprüfungen und 22 numerische. Die anschließende gemeinsame Ausführung hat einen eigenen 231-Bedingungen-Vertrag. Diese Zähl

## Die zentrale Reparatur: Wege nicht zu früh unterscheiden

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:6-28](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L6) · `section:5bc9d0aacdc63094a85b` · section

Setze [formula in source] und [formula in source] . Der Wedge-Kanal besitzt Für [formula in source] verschwindet [formula in source] . Beide geordneten Wege enden im gleichen virtuellen Zustand und interferieren. Orthogonale Records für [formula in source] und [formula in source] ersetzen dies durch [formula in source] : Der antisymmetrische Rang-6-Kanal wird zum Rang-12-Kanal. Bei gleichem Energienenner entsteht ein

## Der erste Schatten wählt die Fortsetzung noch nicht

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:29-35](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L29) · `section:c0e41a6fba1d4ce495da` · section

Mit [formula in source] und [formula in source] ist auf [formula in source] unitär und kollektiv [formula in source] -kovariant. Alle [formula in source] liefern für Materieeingänge denselben ersten blockdephasierten Schatten. Dennoch wirkt [formula in source] dort als [formula in source] , während [formula in source] als [formula in source] wirkt: [formula in source] kehrt als [formula in source] oder als [formula i

## Der allkopplige Zweizellenbeweis

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:36-59](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L36) · `section:e15e155e279e9c8eec11` · section

Für genau zwei vollständige [formula in source] -Zellen und eine positive Brücke gelten die Formeln aus Kapitel

## Vierte Ordnung und unterschiedliche Subtraktionskonventionen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:60-77](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L60) · `section:2aa1af74ff59a1ac5ace` · section

Im ausgewiesenen harmonischen Modell eines geteilten Vermittlers lautet der symmetrische aktive Block Sein niedriger Zweig beginnt mit [formula in source] ; der antisymmetrische mit [formula in source] . Deshalb ist auf dem aktiven [formula in source] -Raum Nach Abzug beider Einzelbondkorrekturen [formula in source] bleibt Beide Schreibweisen sind kompatibel. Eine Konstante auf dem aktiven Sektor ist außerhalb davon 

## Ein exakter Stern-Spektralfilter unter zusätzlichen Ressourcen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:78-90](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L78) · `section:63f4c64732e210245b88` · section

Für [formula in source] gilt Mit [formula in source] und [formula in source] folgen Ein kohärentes Achtzweigregister liefert aus dem früheren Zweisingulett-Eingang [formula in source] Erfolg [formula in source] . Alle acht Ausgänge haben Gewichte [formula in source] . Dies ist eine exakte Alternative zur alten 32-Zweigschaltung. Kontrollierte kontinuierliche Sternpulse und Register bleiben zusätzliche Ressourcen. Erz

## Einfachheit braucht einen Auslesevertrag

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:91-98](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L91) · `section:5e577868641c8c010e69` · section

In der Inzidenzfamilie [formula in source] sind die beiden relevanten Entropien Strikte Konkavität liefert verschiedene Maxima: [formula in source] für Kontexte und [formula in source] für Strahlen. Letzterer Prozess hat Rang 60. Erweitert man den Nachfolgerträger, entstehen symmetrieverträgliche Ränge 15 und 16. Weder maximale Entropie noch minimale Rangzahl wählt die Regel ohne erklärte Klasse. Die passive separate

## Weitere architektonisch wichtige Korrekturen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex:99-113](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/18_audit_v13.tex#L99) · `section:b6eb85a2f386143c59c2` · section

Zwei Singulettläufe finden mindestens vier orthogonale Moden bei [formula in source] über [formula in source] , Residuen unter [formula in source] . Das Dublett ist widerlegt; ein exakter oberer Multiplizitätsbeweis fehlt. -Typen.] 960 gleichgradige Wurzelsummen gehen nach [formula in source] ; gemischt ergeben sich 640 und 192 Summen nach Grad null sowie 64 Cartanfälle. Der vorgeschlagene gemischte Kanal nach [formu

## Eine gemeinsame Ausführung für Record, Präparation und Mehrzeit

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:1-5](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L1) · `section:a119f0430f34dfebca5c` · chapter

Aktualisierung v1.5: weniger zusätzliche Steuerung Die hier eingeführte gemeinsame Record-/Präparations-/Mehrzeitausführung lässt sich jetzt bei festem [formula in source] ohne negative Evolutionszeiten anschließen. Endliche Q-Gatezeiten sind unter einem ausdrücklich belegungserhaltenden Gatevertrag mitgerechnet. Wedge-Kopplung, Q, adressiertes An/aus und Reset bleiben zusätzliche Ressourcen; Details in Kapitel

## Eine Konstruktion, aber ein ausdrücklich zusätzlicher Ressourcenvertrag

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:6-10](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L6) · `section:b13a3672fe01b6bc0101` · section

Dieselbe korrigierte Vermittlungsoperation erzeugt jetzt Aufzeichnung, kontrollierte Näherungspräparation und Mehrzeitantwort. Die tatsächlichen Quellprojektoren, Paulioperationen und die Dreierclock wurden benutzt. Ein bereits präpariertes [formula in source] oder ein separater Präparations-Hamiltonoperator wird nicht benötigt.

## Die vollständige Recordoperation

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:11-30](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L11) · `section:b7ca242dbf64e5d55b37` · section

Mit [formula in source] , [formula in source] und [formula in source] gilt Kopiere nur die Vermittlerbelegung, nicht das geordnete Farbwort: Dann ist auf allen 44 Dimensionen Der Vermittler kehrt zurück. Auf Materie und Pointer bleibt [formula in source] , [formula in source] , mit Beide Krausoperatoren gehören zum Instrument; ihre Effekte summieren sich zu [formula in source] . Ein ungemessener Pointer bleibt kohäre

## Ein gemeinsamer Träger und ein fester Schritt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:31-46](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L31) · `section:bbf35c1cb0c9581304cc` · section

Für vier Materieträger und höchstens einen aktiven Vermittler sei Alle sechs [formula in source] wurden auf dem vollen Materieraum rekonstruiert: [formula in source] , [formula in source] , [formula in source] . Andere Vermittlersektoren bleiben bei einer adressierten Operation unverändert. Die Kanten haben orthogonale Ausgänge; verschränkte Zuschauer sind eingeschlossen. Dies ist ein vollständiges sequenzielles Prot

## Quellseitiger Reset ohne vorpräpariertes Zielreservoir

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:47-58](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L47) · `section:024883d05b8c169b8dcb` · section

Rechenbasis- und uniformer Projektor gehören zu den 60 tatsächlichen Quellprojektoren. Die Swap-Identität verwendet dieselben 16 Quell-Paulis: Für Messausgang [formula in source] und Ziel [formula in source] liefert die Bitverschiebung Damit ist [formula in source] . Vier lokale Resets erzeugen [formula in source] sogar aus verschränktem Eingang. Messung und Feedback bleiben Ressourcen, keine hergeleitete kosmologisc

## Wiederholung präpariert den Viererzustand kontrolliert

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:59-87](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L59) · `section:205a849e9c661aaa3b0c` · section

Akzeptiere in jeder Sternrunde die Recordfolge 111: Alle acht ersten Recordfolgen haben Wahrscheinlichkeit [formula in source] . [formula in source] wird erst zur Zielprüfung definiert. Im 24-dimensionalen Raum der verschiedenen Farbanordnungen gilt exakt Dieser Raum trägt die treue reguläre Darstellung von [formula in source] . Die polynomialen Identitäten der Gruppenalgebra gelten daher auch auf allen 256 Materiedi

## Derselbe Filter liest die Mehrzeitantwort aus

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:88-109](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L88) · `section:6b86dbce48e071a54eed` · section

Nach erfolgreicher Präparation folgen lokaler Quelltick [formula in source] , zweimal [formula in source] , Rücknahme [formula in source] und dasselbe [formula in source] -Runden-Filter. Ein ideales kostenloses [formula in source] -Messgerät wird nicht eingesetzt. Protokoll R behält denselben kohärenten Pointer; Protokoll F verwendet beim zweiten Schritt einen frischen. Mit [formula in source] lauten die gemeinsamen 

## Was für eine native Implementierung noch fehlt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:110-118](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L110) · `section:a086e06951fb6f5936f9` · section

Das neue Register ist nicht Clifford: Ein vierqubitiger Pauli hat Spur null oder [formula in source] . Noch konkreter erzeugt der Quellinput [formula in source] genau 13 nichtverschwindende Rechenbasisamplituden. Das ist kein reiner Stabilizerzustand, dessen Trägergröße eine Zweierpotenz ist. Nur Cliffordoperationen, Stabilizer-Hilfszustände und Pauli-Messungen reichen auch mit Feedback nicht aus. Andere Kodierungen 

## Ungelesener Austausch ist keine Kühlung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:119-125](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L119) · `section:01d17811a6df29ed63d0` · section

Alle [formula in source] kommutieren mit [formula in source] ; der ungelesene Kanal erhält das Zielgewicht. Seine einzelnen Dephasierungen sind orthogonale Hilbert–Schmidt-Projektionen. Ein Fixpunkt ihres Zyklus kann bei keinem Schritt Norm verlieren und liegt deshalb im Schnitt der Fixräume: in der Kommutante der [formula in source] -Wirkung. Deren Dimension ist Die spurlose Dimension 3875 identifiziert keinen gleic

## Abnahmetests und T1–T8-Grenze

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex:126-129](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/19_execution_v13.tex#L126) · `section:2a102158cb03538e0db1` · section

Ein nativer Adapter muss [formula in source] , [formula in source] , Kern und Belegung gemeinsam liefern, beim Half-Charge-Feld zusätzlich mit Domänen- und Energiekontrolle. Er muss den 13-Amplituden-Eingang, beide Recordzweige und die Acht-Runden-Echos reproduzieren, einschließlich Hilfszuständen und Fehlerausgängen. Erst anschließend ist eine skalierende Zellfamilie sinnvoll auf Geometrie, Chiralität und Spin 2 zu 

## Versionspaar v1.3: Quellen, Abdeckung und Reproduktion

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L1) · `section:ed96de30a82e85712ac1` · chapter

No opening prose excerpt; see the source.

## Zwei Dokumente mit unterschiedlichen Aufgaben

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:3-7](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L3) · `section:079a9e83111f55be2550` · section

Diese Ausgabe führt das 90-seitige Hauptbuch v1.1 vollständig fort; die kompakte 35-seitige Compiler-Fassung v1.2 ist nicht ihre Basis. Alle ursprünglichen 21 Hauptkapitel und vier Anhänge bleiben zugänglich. Hinzu kommen drei neue Hauptkapitel und dieses Quellenregister.

## Neue Quellen und unveränderte Originale

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:8-18](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L8) · `section:2674cdfc38ac21ad58d7` · section

Die alten IDs S01–S11 bleiben unverändert. N1–N6 bezeichnen die sechs bereits archivierten Konsolidierungen: Fable-Konsolidierung, Sol-Rekonstruktion, kurze Universalraum-Konsolidierung, Q-Audit/U-Regel, TFPT-Rekonstruktion und Sechs-Prüfpunkte-Analyse, jeweils vom 14. September 2026. Originaltexte und Hashes stehen im Sechs-Quellen-Auditpaket.

## Evidenz nicht durch Addition aufwerten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:19-30](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L19) · `section:ca281b37b0a7908217a5` · section

L37mmL30mmL83mm Paket&Umfang&Prüfgrenze\\ Basisbuch v1.1&210 Bedingungen&Historische Basisprüfung; nicht erneut vollständig ausgeführt.\\ Schatten v1.1&128 Bedingungen&Historische Erweiterung; alte RH-Aktualitätsgrenze bleibt sichtbar.\\ Sechs-Quellen-Audit&100 eigene&78 exakt/Integrität, 22 numerisch; in dieser Ausgabe redaktionell integriert.\\ Gemeinsame Ausführung&231 eigene exakte&Für Ausgabe v1.3 erneut ausgefü

## Rechen- und Dokumentpakete

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:31-39](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L31) · `section:53b3fb2e34297865007e` · section

Die wissenschaftlichen Pakete liegen unter experiments/theory-contracts/universalraum-six-source-audit-20260914 experiments/theory-contracts/compiler-single-execution-20260914 experiments/theory-contracts/universalraum-paired-release-20260914/new-input-audit Das dritte enthält den neuen endlichen Prüfer, seine Normal-/Optimierungsausgaben und die gesonderte Singulettrechnung. Das Releaseverzeichnis enthält LaTeX, all

## Aktualität und ausdrücklich fehlende Prüfungen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex:40-43](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/20_release_v13.tex#L40) · `section:1a0475d8c3d66f4c0d06` · section

Der RH-Aktualitätslauf scheiterte an einem fehlenden referenzierten Quellenordner. Der konfigurierte separate Faktorgraph ist nicht verfügbar. Die ausgewählte Originalroute r647 und die verfügbaren Beweise wurden gelesen; keine vollständige globale Aktualität wird behauptet. Es wurde kein RH-Abschlussmarker geändert und keine neue arithmetische Kampagne gestartet.

## Zwei weitere Eingaben: Mikrodynamik und deterministische Präparation

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:1-8](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L1) · `section:0f48945f73c6d39427c3` · chapter

Aktualisierung v1.5: ein fester Puls ist nicht ein festes Detuning Die unten gezeigte Schranke eines einzigen verstimmten Pulses bleibt richtig. Eine endliche Folge positiver Pulse mit diskreten Q-abgeleiteten Belegungs-Z-Kicks und zwei Off-Intervallen erreicht dagegen vollständigen phasenrichtigen Transfer. Der fehlende Einzelpuls beweist also kein Verbot einer Kompositfolge. Siehe Kapitel Aktualisierung v1.4 Dieses

## Prüfurteil und Modellgrenze

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:9-13](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L9) · `section:45c6f52e23a5ee394892` · section

Die während der Konsolidierung zusätzlich eingereichten Texte N7 und N8 enthalten neue Resultate, nicht nur Zusammenfassungen. N7 berichtet die vollständige vierte Ordnung eines harten CAR-Referenzmodells, einen mikroskopischen Stern und einen Relaxationskanal. N8 konstruiert einen harten Tensorproduktkandidaten mit globaler Bandschranke und eine deterministische ideale Präparation.

## Zwei richtige unitäre Vertizes, aber nicht derselbe Schritt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:14-34](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L14) · `section:0d61d81c1268a9a4f082` · section

N7 verwendet Dieser Operator ist unitär, aber im Gegensatz zu [formula in source] aus Kapitel Das ist kein Widerspruch, sondern eine verschiedene Phase des Rückwegs. Beim Recordaufbau ist der tatsächliche Adjungierte nötig: [formula in source] reproduziert dieselbe Materie-Aufzeichnung wie [formula in source] , unter Einschluss der Pointertensorfaktoren. Blindes Ersetzen beider [formula in source] durch [formula in s

## Der vollständige vierte-Ordnungs-Operator

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:35-56](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L35) · `section:2c04c314ee8371239dc8` · section

Für [formula in source] lautet der eingereichte Referenzoperator [formula in source] vertauscht die beiden vollständigen Paare. Die 40 Clebsch-Kanten ergeben 40 Einzelkanten-, 160 überlappende und 60 gleichlabelige disjunkte Beiträge. Jede Labelklasse ist ein Matching; gleiche Labels teilen keinen Endpunkt.

## Die neue Singulettantwort ist unabhängig reproduziert

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:57-80](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L57) · `section:eee8fd73a22a4e2140bb` · section

Der gesamte 24024-dimensionale Singulett-Multiplizitätsraum wurde aus Youngs orthogonaler Darstellung aufgebaut. Ein neuer Lauf mit zwölf niedrigen Eigenvektoren ergab Beim zweiten Niveau wurden vier orthogonale Moden gefunden. Die größte Eigenvektorresiduen-Norm des Laufs liegt unter [formula in source] . Das ist eine hochgenaue endliche Rechnung, kein algebraischer oberer Multiplizitätsbeweis.

## Eine globale Bandschranke, aber kein genauer Niedrigenergiefehler

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:81-94](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L81) · `section:09c9febe9236c6814938` · section

N8 definiert 16 harte Ortsfaktoren [formula in source] und sechs Bosonmoden pro Vektorlabel. Bei Gesamtladung [formula in source] ist der Sektor endlich. Für gilt [formula in source] . Denn der antisymmetrische Umwandlungsblock [formula in source] erfüllt [formula in source] und [formula in source] . Die selbstadjungierte Offdiagonalblocknorm ist dieselbe. Daher Der führende Austausch ist dann [formula in source] . D

## Deterministische Präparation im idealen erweiterten Gattermodell

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:95-111](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L95) · `section:96eb48630489f156f280` · section

Für [formula in source] gilt [formula in source] . Definiere [formula in source] mit [formula in source] . Dann In der Basis [formula in source] ist [formula in source] , [formula in source] , [formula in source] . Die unerwünschte Amplitude ist Sie verschwindet für die angegebene Wurzel exakt. Die ideale Phase ist [formula in source] . Es ist eine konkrete Anwendung bekannter https://arxiv.org/abs/quant-ph/0005055Am

## Relaxation: konstruktiv möglich, aber nicht durch Bosonenverlust allein

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:112-132](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L112) · `section:0575e6986f39621ea44c` · section

Gewöhnliche Vermittlerverluste [formula in source] lassen vollständig symmetrische Farbzustände mit Vermittlervakuum dunkel. Auf 16 Trägern hat [formula in source] Dimension [formula in source] . Dieser Raum verhindert einen eindeutigen globalen Attraktor dieser Verlustdynamik.

## Der isolierte mikroskopische Stern: vollständiger kleiner Block

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:133-149](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L133) · `section:8feea4beaf5803235798` · section

Nach einem Paarabbau am Stern ist sein gemeinsamer Mittelpunkt leer; ein zweiter Paarabbau ist unmöglich. Für den geschlossenen Block aus 256 Materie- und 288 Vermittlerzuständen gilt Die untere effektive Matrix ist deshalb exakt Der volle 544-dimensionale Block wurde unabhängig gebaut und diagonalisiert. Bei [formula in source] , [formula in source] sind die niedrige Lücke [formula in source] und das nackte Materieg

## Begonnenes Follow-up: die Präparation an das Mikromodell anpassen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:150-166](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L150) · `section:8f77f8c6fcfc82b45f37` · section

Für beliebige bekannte Zielüberlappung [formula in source] ist die Fehleramplitude nach zwei angepassten Schritten proportional zu Sie verschwindet bei Die Polynomidentität wurde symbolisch geprüft. Für den angekleideten Stern-Grundzustand und nackten Eingang [formula in source] gilt [formula in source] . Daraus folgt die angepasste Phase Verwendet man bei idealem Zugriff auf den angekleideten Zielprojektor dennoch d

## Begonnenes Follow-up: warum ein einziger fester Puls nicht genügt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:167-177](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L167) · `section:1ab7c6115e03ba5268e9` · section

Bereits der detunierte isolierte Paarblock hat maximale Transferwahrscheinlichkeit Bei [formula in source] , [formula in source] sind das nur [formula in source] . Eine einzelne freie Entwicklung dieses Blocks realisiert daher keinen vollständigen Materie-Vermittler-Tausch [formula in source] .

## Ein kurzer positiver Kontrollkandidat für die nächste Revision

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:178-196](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L178) · `section:2171eb9b53449fc962a9` · section

Das Einzelpuls-Hindernis legt einen konkreten Ausweg nahe, sofern zusätzliche Kontrollen zugelassen werden. Im isolierten resonanten Paar, also bei auf null gesetzter Verstimmung, sei Dann lautet seine exakte Entwicklung Mit dem relativen Viertelphasenpuls [formula in source] gilt Die volle 22-dimensionale Identität ist symbolisch geprüft. Zwei Belegungsphasen und ein resonanter Transfer genügen somit unter diesem Ko

## Arithmetik: bestätigt ist der Vertrag, nicht die offene Lösung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:197-209](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L197) · `section:cc48497db6fe6a499272` · section

Der singuläre Schur-Satz für [formula in source] benötigt [formula in source] , [formula in source] und [formula in source] . Das Gegenbeispiel [formula in source] , [formula in source] , [formula in source] hat negatives Determinant trotz positivem Schurrest. Kompatible positive Blöcke ergeben eine positive dichte Fortsetzung nur für alle Stufen, die tatsächliche Form und passende Stetigkeit. Die Identität der volls

## Die wichtigsten nächsten Fragen, einfach ausgedrückt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex:210-225](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/21_new_inputs_v13.tex#L210) · `section:c2b11e9e664ccad5f2f7` · section

Kann die echte kleine Maschine die nötigen Handgriffe ausführen? Gesucht ist eine kontrollierte Kopplung, die Vermittler hin- und zurückführt und Aufzeichnung erhält. Ein fester freier Puls reicht im geprüften Stern nicht. Abnahme: beide Recordzweige und alle Eingänge, keine versteckten Zielzustände. Können wir den richtigen, angekleideten Zustand auswählen? Die passende Verstärkungsphase ist jetzt berechnet. Es fehl

## Fünf neue Untersuchungen: Abgleich und stärkere Dynamikkontrolle

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L1) · `section:7cd8cbb4d2fd206f26b0` · chapter

No opening prose excerpt; see the source.

## Quellen und drei notwendige Korrekturen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:3-18](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L3) · `section:d40794bf028960810354` · section

Die neuen Originale sind N9 (Fable-Abschlussrunde), N10 (Sol-Runde 2), N11 (Astra-Antwort), N12 (Astra hoch) und N13 (Spark-Gesamtstand). Alle fünf sind unverändert im Quellenpaket archiviert. Ihre internen Arbeitsaufträge sind Forschungsinhalt, keine zusätzlichen Nutzeranweisungen. Der hier ausgeführte Auftrag ist Prüfung, eigene Fortsetzung und anschließende Konsolidierung.

## Lokalität wählt nicht zwischen zwei lokalen Modellen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:19-28](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L19) · `section:b6d182d59e23a5987910` · section

Für [formula in source] Clebsch-Zellen sind drei Architekturen zu unterscheiden: lrrr Zellen&Eine globale Bank&Eine Bank pro Zelle&Eine Bank pro Kante\\ 1&60&60&0\\2&280&120&0\\3&660&180&0\\6&2760&360&0\\ Gezählt werden gleichlabelige disjunkte Paarbeiträge vierter Ordnung. Die Formeln sind [formula in source] , [formula in source] und null. Eine endliche Bank pro Zelle bleibt lokal und extensiv, behält aber die inne

## Bandtrennung bis zum Betriebspunkt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:29-51](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L29) · `section:d730ffd0e316d0a9d542` · section

Im harten C16-Modell mit [formula in source] sei [formula in source] . Die vollständige Enumeration aller 65536 Ortsmengen bestätigt Gewichte [formula in source] heben im Schurtest die Bosonenwurzeln auf. Die Spaltensumme ist höchstens [formula in source] , die Zeilensumme höchstens [formula in source] . Daher Die daraus gebildete achtstufige Vergleichsmatrix hat Diagonale [formula in source] und Nebendiagonale [form

## Der exakte Schurvertrag und seine verbleibende Restlücke

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:52-65](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L52) · `section:47f7712d36292258028e` · section

Für [formula in source] und [formula in source] gilt Dies definiert das endliche allordentliche Problem, ohne seine riesigen Inversen numerisch ausgewertet zu haben. Mit [formula in source] , [formula in source] , [formula in source] , [formula in source] begrenzen zwei Resolventenidentitäten den Rest des energieabhängigen Kerns nach [formula in source] durch Bei [formula in source] reproduziert dies [formula in sour

## Eine einfache positive Darstellung der lokalen vierten Ordnung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:66-78](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L66) · `section:232629cfc470428532d6` · section

Für [formula in source] , [formula in source] und [formula in source] folgt aus [formula in source] und [formula in source] exakt Jeder Clebsch-Stern besteht aus fünf Transpositionen. In der treuen regulären [formula in source] -Darstellung wurde die ganze ganzzahlige Identität [formula in source] auf 720 Dimensionen geprüft. Mit [formula in source] ist sein Spektrum ganzzahlig nichtnegativ; daher ist jeder Summand p

## Neue Diagonalisierung statt bloßer Rayleighkorrektur

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex:79-94](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/22_audit_v14.tex#L79) · `section:436739b0f23468528c1c` · section

Der eigene vollständige Singulettträger reproduziert beide F4-Varianten: lrr &Zellintern geteilt&Pro Kante lokal\\ F4-Grundwert&555,488500364&732,120310942\\ F4 auf ersten vier Moden&583,292038666&708,209322519\\ Gapkoeffizient [formula in source] &13,901769151& [formula in source] \\ Danach wurden die niedrigen Eigenwerte des vollständigen trunkierten Operators [formula in source] neu berechnet: Dimension 24024, ach

## Eigene Fortsetzung: ein gemeinsames kontrolliertes Mikrolabor

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:1-5](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L1) · `section:f1a77702947cfc3b348e` · chapter

Aktualisierung v1.5: zwei gültige Präparationsverträge Der unten konstruierte exakt selektive Spektralfilter bleibt gültig unter seinen stärkeren Kontrollannahmen. Kapitel

## Vorzeichen aus E8 und die noch fehlende Quellbasis

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:6-10](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L6) · `section:b08bf31f7918684f9823` · section

Der geordnete Standard-Gittercocycle [formula in source] wurde unabhängig aus einer einfachen E8-Basis aufgebaut. [formula in source] liefert den Kommutatorfaktor, Bilinearität die Cocycle-Identität. Alle 240 Wurzelkoordinaten sind ganzzahlig. Auf den 40 Clebsch-Kanten bestätigt die exakte F2-Elimination Rang 45 für die Antisymmetriegauge der Ortsfarben und Rang 285 für die zusätzliche kantenlokale Vermittlergauge. F

## Ein allordentlicher CAR-/Tensoradapter im Matchingsektor

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:11-29](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L11) · `section:4fcd073e34179a90a9cc` · section

Für ausschließlich kantenlokale Vermittler ohne Hopping sind die lokalen Ladungen erhalten. Aus der vollständig belegten Nullbosonquelle folgt [formula in source] . Besetzte Bosonen bilden deshalb ein Matching: Jede Kante trägt höchstens einen, und zwei besetzte Kanten teilen keinen Endpunkt.

## Der vollständige Stern, nicht nur sein niedriger Schatten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:30-41](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L30) · `section:b245612108968ab3d71c` · section

Die Kopplung [formula in source] zwischen 256 Materie- und 288 Vermittlerzuständen wurde neu aufgebaut. Sie erfüllt [formula in source] . Der volle Hamiltonoperator ist Seine 14 verschiedenen Energien sind sieben niedrige Werte sechs obere [formula in source] für [formula in source] und [formula in source] mit Multiplizität 67. Die niedrigen Multiplizitäten sind [formula in source] ; die sechs oberen wiederholen die 

## Ein exakter endlicher Filter aus wirklichen Entwicklungszeiten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:42-62](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L42) · `section:33c4dbd9d55ba8faa5ea` · section

Für jeden anderen Energiewert [formula in source] setze [formula in source] ist der akzeptierte Krausoperator eines Hadamardtests mit kontrollierter Entwicklung. Alle Faktoren erhalten den Zielzustand, und der [formula in source] -te Faktor löscht den Eigenraum zu [formula in source] . Weil sie Funktionen desselben [formula in source] sind, gilt auf dem ganzen Raum Es ist kein gemeinsames kommensurables Wiederkehrint

## Noch einfacher: die Hülle messen und die Ausbeute mitführen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:63-84](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L63) · `section:7d4ee27b50d562f765fb` · section

Eine ideale kohärente Entkleidung ist für erfolgreiche Zustandspräparation nicht nötig. Nach dem Filter wird die Vermittlerbelegung gemessen. Im leeren Zweig bleibt exakt nacktes [formula in source] . Mit gilt auf nackter Materie Dies ist der gesamte akzeptierte Krausoperator und wurde als volle Matrix geprüft. Aus dem elementaren Zweisingulett [formula in source] mit [formula in source] beträgt die Ausbeute [formula

## Ein vollständiger neuer Präparations- und Echovertrag

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:85-97](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L85) · `section:728b1ab27185e50853a3` · section

Das neue Protokoll beginnt in nacktem [formula in source] , benutzt den mikroskopischen Sternfilter samt Leerbelegungsherald, danach den lokalen Dreierzyklus [formula in source] , zweimal den resonanten Record, den Rücktick und denselben mikroskopischen Filter zur Schlussprüfung. Der Echoanteil wurde im vollständigen 256D-Materieraum gerechnet; wiederholte Farben werden nicht herausprojiziert.

## Feedback: Attraktor, Fehlerboden und unabhängige Zellen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex:98-117](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/23_micro_v14.tex#L98) · `section:bb4444694449ff2fde27` · section

Der neue N11-Kanal ist CPTP, mit [formula in source] und [formula in source] . Wegen [formula in source] und [formula in source] folgt Damit ist [formula in source] der einzige stationäre Zustand. 556 Zyklen garantieren [formula in source] Infidelität. Der unabhängige 256D-Lauf kontrolliert die Gewichtsidentität und Kontraktion in jedem der 556 Schritte. Dies ist nicht der ungelesene unitale Recordkanal mit großer Fi

## Alle Arbeitsfronten: neue Tests und nächste Beweise

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:1-10](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L1) · `section:809a314fe8e6f9788043` · chapter

Aktualisierung v1.5: die aktuelle Frontkarte steht weiter hinten Die folgenden Rechnungen bleiben als v1.4-Befunde erhalten. Kapitel

## T1: Auswahl statt nachträglicher Passung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:11-19](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L11) · `section:df2d867dc25ee357a152` · section

Für den bereits konstruierten Strahlengraphen mit betrachten wir die zulässige Lazy-Walk-Familie [formula in source] , [formula in source] . Ein Eigenwert kann nur bei [formula in source] oder [formula in source] verschwinden. Dort sind die Nullitäten 30 beziehungsweise 5; ansonsten ist der Rang 60. Das liefert einen präzisen Rangvergleich innerhalb dieser Familie, aber keine Auswahl über alle denkbaren Compiler.

## T2: Ein konkreter Anfang der analytischen Naht

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:20-32](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L20) · `section:afb66e6fbb394fae3e9d` · section

In einer ausdrücklich zusätzlich gewählten unitären Bosonreferenz liefert das Ladungsfeld [formula in source] auf dem Vakuum die Koeffizienten Der unabhängige Prüfer rekonstruiert diese Identität für [formula in source] bis Niveau 32. Für einen exponentiell abfallenden Modentest [formula in source] ist Dies ist eine konkrete Vakuumkonstruktion und kein Energieabschätzungsbeweis auf allen Zuständen. Das Ladungsfeld li

## T3: Ein skalierender Raumtest, der seine eigene Grenze zeigt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:33-42](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L33) · `section:4f4015e69b0015ae9c52` · section

Für die deklarierte Produktfamilie [formula in source] ist das Spektrum exakt separierbar: Wir berechnen den Wärmetrace ohne eine riesige Matrix anzulegen und bestimmen [formula in source] . Für [formula in source] , [formula in source] ergibt sich näherungsweise [formula in source] . Geprüft wurden [formula in source] und [formula in source] . Die dreidimensionale Probe beschreibt damit 4.194.304 Produktknoten, ohne

## T4: Chirale Nullmoden werden gebaut, aber nicht als Familien ausgegeben

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:43-54](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L43) · `section:9e9c96c3b219a890fe42` · section

Das einfachste Gitter-Weylsymbol [formula in source] besitzt acht Knoten, je einen an jeder Kombination [formula in source] . Ihre Chiralitäten wechseln; die Summe ist null. Eine anschauliche zweikomponentige Gleichung allein entfernt die zusätzlichen Arten daher nicht. Diskrete Weyl-Walks sind eine mögliche https://arxiv.org/abs/1708.00826Referenzkonstruktion, keine automatische Lösung dieses TFPT-Problems.

## T5: Was die Band- und Filterergebnisse tatsächlich schließen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:55-59](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L55) · `section:3568c8fc1bbcae6af052` · section

Die in dieser Revision nachgewiesenen äußeren Bandschranken betreffen die ganze harte Einzelle, nicht nur deren Singulett. Die kantenlokale vierte Ordnung ist positiv und ihre niedrigen Eigenwerte wurden als vollständiger trunkierter Operator neu berechnet. Der mikroskopische Filter benutzt alle Energien des 544-dimensionalen Sterns. Damit sind mehrere zuvor nur effektive Bausteine zu kontrollierbaren endlichen Aussa

## T6: Parameter brauchen einen gemeinsamen empirischen Test

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:60-70](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L60) · `section:15346f109af846085b77` · section

Zunächst die Flavourkontrolle: Für dieselben orthonormalen drei Nullmoden auf linker und rechter Seite liefert ein räumlich konstanter Skalarüberlapp [formula in source] . Drei Moden ergeben dann drei gleiche Massen, nicht die beobachtete Hierarchie oder Mischung. Ein zusätzlich gewähltes nichtkonstantes Profil spaltet die Überlappmatrix, führt aber neue Eingaben ein. Das ist ein expliziter Test dafür, dass Modenzähl

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)

## T7: Warum ein Tensorbild noch keine Gravitation ist

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:71-79](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L71) · `section:42f54ee06a97e54458a2` · section

Für freie massive bosonische Moden mit Lücke [formula in source] hat eine normalgeordnete bilineare Tensorobservable im Vakuum Spektralgewicht erst oberhalb der Zweiteilchenschwelle [formula in source] . Die Gitterproben [formula in source] , [formula in source] , bestätigen die Schwelle eins. Ein transversaler, spurloser Projektor besitzt zwar Rang zwei, verschiebt aber keine Energie zu null. Er erzeugt daher aus di

## T8 und die anderen Arbeitsfronten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:80-86](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L80) · `section:e901986c901ffd404a69` · section

Die gemeinsame kontrollierte Ausführung liefert jetzt operative Rohwahrscheinlichkeiten mit bezahlter Präparation, Aufzeichnung und Endprüfung. Sie liefert noch kein physikalisches Quellfunktional, aus dem dieselben Kontrollmöglichkeiten, Zustände, Wirkungen und Observablen folgen. Die fehlende Kante liegt weiter zwischen primitiver Compilerregel und gewähltem Laborvertrag.

## Die acht Tore bleiben einzeln sichtbar

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:87-99](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L87) · `section:54c9e82d4b1c71a5957e` · section

L10mmL65mmL72mm Tor&Neuer substantieller Beitrag&Fehlender vollständiger Nachweis\\ T1&Rang- und Entropievergleich, drei lokal unterschiedliche Vermittlerverträge.&Primitive Auswahl von Zuständen, Alternativen, Phasen und Kopplung.\\ T2&Vakuumkoeffizienten, Sektorparität und Halbladungsschranke.&Native Halbladung mit Definitionsmenge, Energie- und Adjungiertenkontrolle.\\ T3&Skalierende Wärmetrace-Rechnung und gemein

## Sechs nächste Fragen – mit einem klaren Erfolgskriterium

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:100-110](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L100) · `section:56e5c6baba7db2916f0f` · section

Wer bedient das Labor? Aus einer festgelegten Compilerregel kontrolliertes [formula in source] , Resonanz, [formula in source] , Reset und Kantenisolation ableiten. Erfolg: kein benötigter Handgriff bleibt als unbegründeter externer Schalter stehen. Welche Vermittlerarchitektur wird ausgewählt? Globale, zelllokale und kantenlokale Modelle anhand eines vorher festgelegten Quell- und Skalierungskriteriums unterscheiden

## Prüfprovenienz und Reproduzierbarkeit

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex:111-120](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/24_fronts_v14.tex#L111) · `section:c89100599a5cea96d680` · section

Die fünf eingereichten Texte N9–N13 sind unverändert archiviert und einzeln durch SHA-256 gekennzeichnet. Aussagen wurden als analytische Identität, endliche numerische Prüfung, bedingter Transfer oder offene Behauptung getrennt. Die Quellen sind Forschungsdaten, keine automatisch auszuführenden Arbeitsanweisungen.

## Version 1.5: eine einfachere gemeinsame Ausführung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:1-7](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L1) · `section:a23b4f5f8f1cdff67f90` · chapter

Wo wir jetzt stehen Wir können mehrere Teile der kleinen mathematischen Maschine konkreter bauen. Die Aufzeichnung braucht weniger Spezialsteuerung; große endliche Spektren lassen sich durch eine tatsächlich vorhandene Symmetrie verkleinern; eine ausdrücklich gewählte Kette besitzt berechenbare kritische Dynamik. Noch nicht bewiesen ist, dass dieselbe ursprüngliche TFPT-Regel gerade diese Steuerungen, Kopplungen, Zus

## Zwei weitere Eingaben und ihre wirklichen Zusatzinformationen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:8-20](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L8) · `section:0514217bbfb6bfd2b2ff` · section

Die Texte TFPT Universalraum Fortsetzung, 14.09.2026 NEU und TFPT Universalraum Ergebnisse, 14.09.2026 sind mit der v1.4-Grundlage abgeglichen. Ihre unveränderten Originale liegen als N14 und N15 im Quellenpaket. Interne Arbeitsanweisungen werden als Quelleninhalt, nicht als neue Aufträge behandelt.

## Feste Verstimmung, positive Zeiten und ein exakter Record

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:21-45](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L21) · `section:3275a42ff372533551fd` · section

Die beiden Belegungsalternativen besitzen den hellen Hamiltonblock [formula in source] Ein einzelner Puls erreicht bei [formula in source] höchstens [formula in source] Transferwahrscheinlichkeit. Der vorhandene kohärente Belegungszugriff [formula in source] erlaubt aber mit einem separaten Pointer in [formula in source] einen diskreten [formula in source] -Kick. Der Pointer bleibt dabei erhalten. Das ist keine neu a

## Die Rückfolge und ihre bislang gefährliche Sektorphase

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:46-65](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L46) · `section:58e8dcf107bcda129d44` · section

Ein positiver Puls der Dauer [formula in source] ist auf dem hellen Raum nicht genau das Inverse, sondern [formula in source] Die Rückfolge [formula in source] hinterlässt also die aktive Sektorphase [formula in source] . Bei abgeschaltetem [formula in source] korrigiert ein positives Warteintervall [formula in source] die Vermittlerphase. Mit [formula in source] lautet die vollständige, von rechts nach links gelesen

## Endliche Q-Zeiten und wirkliche Präparationskosten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:66-80](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L66) · `section:191e29f3a2cdf8ff2b54` · section

Die Makrooperation benötigt 24 On-Pulse, zwei Off-Intervalle und 23 Q-Aufrufe. Q-Gates werden nicht als kostenlos ausgegeben. Falls ein zusätzlich deklarierter Generator [formula in source] die Belegung erhält, kann während Q bei [formula in source] geparkt werden. Zum Beispiel realisiert [formula in source] das gewünschte Q. Ein Q-Zeitfenster wird auf [formula in source] aufgefüllt; die kommutierende Drift verschwin

## Eine wirklich vorhandene Vereinfachung des großen Spektrums

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:81-82](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L81) · `section:9b70ed6f0a2838f268ad` · chapter

No opening prose excerpt; see the source.

## Der Standardblock ist nicht mehr nur angekündigt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:83-91](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L83) · `section:27a9814c0a03a662d252` · section

Auf dem 24024-dimensionalen Spechtraum [formula in source] sei [formula in source] und [formula in source] . Der rationale Projektor [formula in source] besitzt Dimension [formula in source] ; der größere translationsfeste Raum hat Dimension 1764. Die Darstellung [formula in source] erklärt, weshalb dies genau eine Fixlinie je vierdimensionaler Standardkopie isoliert. Auf dem gesamten Isotypieraum ist [formula in sou

## Rationale Intervalle statt nur Dezimalzahlen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:92-107](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L92) · `section:88e0aa84db8a87a5d248` · section

Der ganzzahlige Gruppenalgebraoperator erhält ein Specht-Schnittgitter in seinem rationalen invarianten Teilraum. Daher ist sein charakteristisches Polynom monisch ganzzahlig. Aus [formula in source] folgt die vorab bekannte Koeffizientenabschätzung [formula in source] Siebzehn Primmoduli liefern einen 452-Bit-CRT-Modulus oberhalb der nötigen 428-Bit-Schranke. Eine achtzehnte Primzahl prüft die Rekonstruktion unabhän

## Tableau-Transposition: 80 wird 40

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:108-135](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L108) · `section:43fa7510b64186bec727` · section

Die selbstkonjugierte Youngform besitzt in der orthogonalen Basis die Involution [formula in source] , wobei [formula in source] das Vorzeichen der Zellfolge in Zeilenordnung ist. Die 4-mal-4-Transposition enthält sechs Zelltranspositionen. Damit gelten exakt [formula in source] Alle 1920 Graphautomorphismen sind gerade Trägerpermutationen, also [formula in source] und [formula in source] . Für jeden dieser Automorph

## Vierte Ordnung: was erhalten bleibt und was nicht

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:136-148](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L136) · `section:9edeabb263801ca530a6` · section

Für kantenlokale Vermittler setze [formula in source] und [formula in source] . Dann [formula in source] Die einfache Spiegelung [formula in source] gilt für den korrigierten Hamiltonoperator nicht unverändert. Die G-Blockzerlegung bleibt jedoch richtig. Da [formula in source] ganzzahlige Inhalts-Eigenwerte zwischen 0 und 10 besitzt, folgt [formula in source] Bei [formula in source] bleibt ein garantierter Standardbl

## Wie eine niedrige kritische Dynamik möglich wird

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:149-150](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L149) · `section:b1557653481ba4cce1d7` · chapter

No opening prose excerpt; see the source.

## Die Farbkanäle gemeinsam abschätzen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:151-174](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L151) · `section:ede34bded5644931575a` · section

Für den antisymmetrischen Paarannihilator gilt im harten Materieraum einschließlich Löchern [formula in source] Vier Kanten teilen ein Vermittlerlabel. Operator-Cauchy liefert [formula in source] Somit verbessert sich die C16-Zellbanksumme auf [formula in source] statt der getrennten Farbabschätzung [formula in source] . Eigene Vermittler pro Kante ergeben [formula in source] .

## Ein besonders einfaches Verkleben ist als masselose Route ausgeschlossen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:175-185](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L175) · `section:718039774fdc30d71795` · section

Sei [formula in source] eine endliche Zelle mit eindeutigem Grundzustand [formula in source] , Energie [formula in source] und Gap [formula in source] . Auf einem beliebigen endlichen verbundenen Graphen definiere [formula in source] Jeder Swapterm ist positiv. Mit [formula in source] folgt [formula in source] . Der Produktgrundzustand ist eindeutig. Die gleichförmige Einanregung wird von jedem Swap festgehalten und 

## Der entscheidende Unterschied: innere Kritikalität bei massiven Vermittlern

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:186-219](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L186) · `section:b23abbfff15d1a16a854` · section

Ein anderer ausdrücklich deklarierter Transfer vertauscht nur [formula in source] mit [formula in source] und verschwindet bei zwei besetzten Zellen: [formula in source] Die Zweizellenblöcke beweisen [formula in source] . Auf einem D-regulären Graphen ist deshalb bei [formula in source] der volle Gap genau [formula in source] , wiederum mit gleichförmiger Einanregung als saturierendem Zustand.

## Die Farbentartung lässt sich symmetrisch reparieren

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:220-245](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L220) · `section:f4a3f5f63126bf31ba4a` · section

Mit allen 30 ersten Farben und reinem Transfer können sich auf der offenen Kette die geordneten Farben nicht überholen. Bei N Teilchen entstehen [formula in source] isospektrale Farbfolgen. Das erzeugt extensive Restentropie und ist keine Familienableitung.

## Rechnen, Zeit und ausgeschiedene Information

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:246-247](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L246) · `section:9dbb0eae727cc7d627c5` · chapter

No opening prose excerpt; see the source.

## Aufzeichnung und kohärente Logik benutzen dieselbe Matrix

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:248-257](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L248) · `section:2164a48369f6c3a9ae4d` · section

Ein Pointer-Hadamard verwandelt den Record exakt in einen kontrollierten Ququart-Swap: [formula in source] Kodiert man ein Qubit in den Farben 0 und 2, bleibt das zweite Farbbit null und die Operation ist Fredkin. Mit sauberem Hilfsbit [formula in source] sei [formula in source] . Dann ist [formula in source] genau Toffoli, mit zurückgegebenem [formula in source] .

## Eine autonome Uhr ist konstruierbar, aber sie wählt kein Programm

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:258-268](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L258) · `section:c14f25b3d1f55f826d3e` · section

Für ein vorgegebenes Programm [formula in source] setze [formula in source] , [formula in source] und [formula in source] . Der offene History-Hamiltonoperator mit Links [formula in source] und Laplacediagonalen erfüllt exakt [formula in source] Jedes Programm hat also dasselbe Spektrum [formula in source] , wiederholt mit der Datendimension. Feste Zwischenzeit-Auslesungen unterscheiden die Programme, ihre Eigenwerte

## Half-Charge: ein einfacher Adapter benennt die fehlende Ressource

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:269-279](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L269) · `section:0aabd1270e896de4cd4d` · section

Auf [formula in source] tragen [formula in source] die Ladungen k/2 und l/2. Die bilaterale Verschiebung [formula in source] ist unitär, hat Norm eins und ein explizites Adjungiertes mit umgekehrter Verschiebung. Sie erhält die Gesamtladung, kippt aber die einzelne Systemparität [formula in source] .

## Reset ist nur vollständig, wenn die Information irgendwo bleibt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:280-288](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L280) · `section:812bfb0148c50385e14b` · section

Ein universeller unitärer Reset von d orthogonalen Eingaben auf denselben reinen Systemzustand muss d orthogonale Umweltzustände erzeugen. Für m unabhängige Eingaben und finale Infidelität höchstens [formula in source] je Ausgang folgt [formula in source] Man startet die Eingaben maximal gemischt und die Umwelt rein. Unitarität erhält die Entropie [formula in source] ; jeder nahezu reine Ausgang hat Entropie höchsten

## Die verbleibenden physikalischen Nachweise nach v1.5

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:289-290](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L289) · `section:649061519ddddb4b24fb` · chapter

No opening prose excerpt; see the source.

## Eine konkrete empirische Hürde statt freier Nachjustierung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:291-317](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L291) · `section:f381981b6542696bc123` · section

Die dokumentierte Massenregel lautet [formula in source] , [formula in source] . Im vollständigen Starobinsky-Potential, mit [formula in source] und [formula in source] , gelten in erster Potential-Slow-Roll-Ordnung [formula in source] Damit erhält man ohne große-N-Abschneidung [formula in source] und die exakte Identität innerhalb dieser Näherung [formula in source] Die betrachtete ACT-Spalte P-ACT-LB2 aus Tabelle 5

## Alle acht Tore mit genauem Rest

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:318-335](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L318) · `section:755f9c59385415ce0682` · section

L13mmL57mmL67mm Tor&Neuer Beitrag&Vollständig fehlender Nachweis\\ T1&Fester-Delta-Record, endliche Q-Zeiten, kohärente Logik&Native Wedge-, Q-, Schalt- und Controllerherkunft aus einer primitiven Quelle\\ T2&Norm- und energiekontrollierter relativer Half-Charge-Adapter&Renormiertes lokales Feld der tatsächlichen Quelle, E8-/Clock-Zuordnung\\ T3&Skalierende Referenzfamilien, exakte Gaps, linearer gefüllter Kettensekt

## Die sechs nächsten Ziele sind jetzt schärfer

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:336-345](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L336) · `section:ffe5c98ef394ea3180e8` · section

Native Bedienung: Für jeden Zugriff des kleineren Recordvertrags ein tatsächliches Quellwort oder eine kontrollierte Approximation liefern. Den ganzen Operator samt Zuschauerphasen prüfen, nicht nur Erfolgsamplituden. Gebundene Zwischenzellkoeffizienten: Transfer, Dichte, chemische Verschiebung und Farbaustausch gemeinsam ableiten. Erst eine lokale dynamische Restkontrolle, dann Kritikalität auf der inneren Skala g b

## RH, Faktorisierung und Hylæan bleiben getrennte Abnahmen

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:346-350](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L346) · `section:51176c1e2c6a0e1d312b` · section

Für RH fehlt weiterhin die Identifikation des tatsächlichen signierten Weil-Objekts mit uniformer Positivität und kontrollierten Grenzresten. Das Clock-Spektrum allein kann dies nicht leisten; seine Unabhängigkeit vom eingeschriebenen Programm ist jetzt konkret bewiesen. Der Gatteranschluss liefert für Faktorisierung eine bedingte Quantenrechenressource, aber keine neue klassische Polynomialzeit oder Lösung von P ver

## Was neu geprüft wurde und was die Prüfzahlen bedeuten

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex:351-358](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/25_revision_v15.tex#L351) · `section:9ecdb34d612cd3598450` · section

Die eigenen Root-Prüfer umfassen 104 Bedingungen, normal und optimiert identisch, mit sechs abgefangenen Fehlermutationen. Die Kontrollfront umfasst 88 Bedingungen einschließlich vollständiger 44D-/88D-Operatoren und rationaler Prozessstatistik. Die Skalierungsfront umfasst 400 Bedingungen und sechs Fehlermutationen. Das Quartettpaket enthält 273 modulare Bedingungen, die vollständige CRT-Rekonstruktion, rationale Wu

## v1.6: Die konsolidierte endliche Ausführung

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex:1-2](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex#L1) · `section:15b57e7607e72c309a84` · chapter

No opening prose excerpt; see the source.

Explicit source references:

- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)

## Was neu in dieses Hauptbuch eingeht

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex:3-5](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex#L3) · `section:60b18d8885c5860d9ca9` · section

Die vorläufigen Markdown-Berichte vom 14. September mit Versionsnummer 1.6 waren noch kein aktualisiertes vollständiges PDF. Dieses Kapitel übernimmt ihre wesentlichen Ergebnisse mit ihren jeweiligen Voraussetzungen. Es ersetzt nicht die früheren Beweise, sondern trennt überholte Engpässe, jetzt gelöste endliche Aufgaben und weiterhin fehlende physische Herkunft. Die großen Spektral- und Kosmologieläufe werden hier a

## Ein einziger erfolgreicher Record erzeugt die Zelle exakt

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex:6-32](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex#L6) · `section:cd1ccf67f76ab8fa53a1` · section

Vier Ququarts werden durch acht Bits kodiert; das erste Bit jedes Ququarts ist niederwertig. Mit dem Swap [formula in source] und [formula in source] sei [formula in source] ist ein Stabilizerzustand. Seine Herstellung aus acht Nullbits benötigt die folgende zeitlich geordnete Schaltung: H auf 0, 1, 2, 5; Z auf 2, 5; CNOT [formula in source] , [formula in source] , [formula in source] , [formula in source] , [formula

Explicit source references:

- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)

## Schlussprüfung und Mehrzeitvergleich ohne versteckte Ausbeute

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex:33-54](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex#L33) · `section:ed64c88e81dded625999` · section

Die adjungierte Vorbereitung liefert eine aus Operationen zusammengesetzte Schlussprüfung. Man fordert einen neuen Record-Ausgang 1, führt die inverse [formula in source] -Schaltung aus und liest acht Nullbits aus. Der erfolgreiche Krausoperator und sein Effekt sind Der Effekt ist nicht als primitive perfekte Messung eingesetzt. Er wird aus der Schaltung berechnet. Die Messung ist destruktiv und akzeptiert selbst [fo

## Optimalität und eine präzise Ressourcengrenze

[experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex:55-74](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/main-v1.6/chapters/26_v16_labor.tex#L55) · `section:7f6891f1dfbb454c4398` · section

Innerhalb der reinen oder gemischten Acht-Bit-Stabilizerzustände gilt Der dokumentierte Beweis reduziert auf einen Vier-Bit-Stabilizercode mit sechs vorzeichenbehafteten Trägern. Unter allen 307 affinen Unterräumen von [formula in source] sind die maximalen Schnittgrößen für Dimension [formula in source] gleich [formula in source] . Die Schranke [formula in source] gilt in jeder Dimension und wird durch [formula in s

Explicit source references:

- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)
