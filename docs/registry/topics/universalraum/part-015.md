# Universalraum research — part 15

[Topic entry](../universalraum.md) · [Registry entry](../../INDEX.md)

Exact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.

## Urteil

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:27-45](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L27) · `section:971e96d0b0e4252c6f98` · subsection

Ja, ein belastbarer neuer Rechenschritt ist enthalten: Die zuvor fehlende Norm ν5 liegt jetzt mit passendem Quellstand vor. Wir haben ν1 bis ν5 frisch durch die ursprüngliche exakte Spurnetzwerkrechnung reproduziert und daraus unabhängig strengere rationale Ritzgrenzen gewonnen. Die übrigen großen Aussagen des Textes sind teils bereits bekannt, teils durch v1.6.7 korrigiert. Besonders problematisch ist die Vermischun

## 1. ν5 ist jetzt ein Ergebnis, nicht mehr nur eine Programmeinstellung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:46-99](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L46) · `section:751b6eabd39fca269cc8` · subsection

Der v1.6.7-Snapshot hatte zu Recht festgehalten, dass damals norms_by_traces.json und ein abgeschlossener zugehöriger Replay fehlten. Dieser konkrete Quellenstand hat sich geändert. Der neue Checkerhash be72c728e128ae0ef605980a5bae88ea31049e29e2fd17c43167fbd6ad1d0c89 passt jetzt zum Ergebnis; auch der Common-Hash stimmt. Die vorhandenen normalen und optimierten Normausgaben sind byteidentisch. Der gespeicherte JSON-I

## 2. −1,138 ist eine echte bessere Variationsgrenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:100-170](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L100) · `section:0749600b3d2a03e44c1a` · subsection

Die Unterräume aus den normierten bosonweise geordneten Vektoren [formula in source] sind nicht invariant, aber sie sind gültige Variationsräume. Da unterschiedliche k orthogonal sind und H die Bosonzahl höchstens um eins ändert, besitzt die Kompression auf v0, ,v5 exakt

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier
- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v1_e8_glue.py](../../../../verification/v1_e8_glue.py#L1) · explicit_script_identifier
- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)
- [(* ==== v260: one Kummer/K3 carries seam + carrier-16 + E8 (ARCH.K3.01) ==== *) Module[{e8edges, E8, U, L, sig, nodes, marks}, e8edges = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {5, 8}}; E8 = 2 IdentityMatrix[8] - Table[If[i != j && MemberQ[e8edges, Sort[{i, j}]], 1, 0], {i, 8}, {j, 8}]; U = {{0, 1}, {1, 0}}; L = ArrayFlatten[{{U, 0, 0, 0, 0}, {0, U, 0, 0, 0}, {0, 0, U, 0, 0}, {0, 0, 0, -E8, 0}, {0, 0, 0, 0, -E8}}]; sig = {Count[Eigenvalues[N[L]], x_ /; x > 0], Count[Eigenvalues[N[L]], x_ /; x < 0]}; nodes = 2^4; marks = 2^2; checkExact["v260 ARCH.K3.01: one Kummer/K3 surface carries seam + carrier-16 + E8. E8 Cartan even, det 1, " <> "positive-definite (the unique even unimodular pos-def rank-8 lattice); the K3 lattice U^3(+)E8(-1)^2 " <> "has rank 22=b_2, det -1 (unimodular), even, signature (3,19) with E8(-1)^2 an orthogonal summand; the " <> "seam T^2/(z->-z) has 4=|(Z/2)^2| marks (pillowcase); the carrier-16 = Kummer nodes |A[2]|=2^4=16 = " <> "dim S+ = 4x4 = (seam marks)^2. So the v1 glue D5(+)A3+mu4=>E8 is the lattice shadow of one object.", Det[E8] == 1 && AllTrue[Diagonal[E8], EvenQ] && PositiveDefiniteMatrixQ[E8] && Length[L] == 22 && Det[L] == -1 && AllTrue[Diagonal[L], EvenQ] && sig == {3, 19} && nodes == 16 && marks == 4 && nodes == marks^2]; ]; (* ==== v267: QGEO rigidity / minimal-axiom form of QGEO.SYM.01 (QGEO.SYM.02) ==== v262 (alpha_s RG), v263 (seesaw numpy), v264 (DtN FFT), v265 (RG+text guard), v266 (proton RG) are numerical -> Python-only; v267's exact cross-ratio/j core is mirrored here (the DtN/FFT part of v267 stays Python-only). *)](../../../../verification/wolfram/tfpt_readouts_extension.wl#L2032)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)
- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)

## 3. Der Text vermischt drei verschiedene Näherungszustände

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:171-236](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L171) · `section:91cb55a1fd2b0834520c` · subsection

Die neuen kleinen Matrizen wurden unabhängig diagonalisiert. Sie bestätigen die gespeicherten numerischen Ritz-Erwartungswerte, aber nicht deren Umdeutung zu exakten Eigenschaften von Ω.

Explicit source references:

- [verification/v3_em_alpha.py](../../../../verification/v3_em_alpha.py#L1) · explicit_script_identifier
- [verification/v5_e8_cascade.py](../../../../verification/v5_e8_cascade.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v3) electromagnetic closure: alpha^-1 ---- *) M = 41; phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4); F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]]; aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40]; alphaInv = 1/aStar; check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15]; check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12]; (* ---- (v1) E8 glue arithmetic ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L36)
- [experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/CalderonInterface.lean#L1)
- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean#L1)

## Die mittleren Antwortenergien lassen sich ohne riesige Zustandsdateien korrigieren

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:237-276](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L237) · `section:91351fb6a30f88ebb0c8` · subsubsection

Aus den CAR folgen für jeden normierten G-Singulettzustand mit N=64:

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation

## 4. Was bereits überholt ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:277-323](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L277) · `section:90ec09e62f7374419228` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage der Anlage & Prüfung \\ Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt & Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. \\ Mit allen gewährten inneren Kon

## 5. Was daran spannend ist und was als nächstes trägt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:324-340](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L324) · `section:a4a034f9bf291416ebb0` · subsection

Der gute neue Schritt ist die tatsächlich abgeschlossene fünfte Spurnetzwerk-Norm mit der daraus folgenden stärkeren strengen Energie- und Entnahmeschranke. Hinzu kommt unsere kleine CAR-Auswertung, die die geladenen ersten Momente auf den richtigen größeren Ritz-Zustand hebt. Das verbessert nachprüfbar die Rechnung im bestehenden nativen Modell.

## Reproduktionsbelege

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:341-368](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L341) · `section:a278949d0f68d35bb6a5` · subsection

late_a/verify.py prüft elf eingefrorene Eingaben, führt die ν1-ν5- Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf. Es gibt 46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische Prüfungen und 10 numerische Konsistenzprüfungen, separat dazu 1239 ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine unabhängigen mathematischen Theoreme.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/results_normal.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moment_audit.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/moments_optimized.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/mechanism/late_a/verify.py#L1) · explicit_file_citation

## Nachtragsprüfung B: Feldprojektor und Lorentz-Händigkeit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex:369-371](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/016-subsection-beweisumfang-label-beweisumfang.tex#L369) · `section:0ce6fc96b738e14f2bf6` · section

No opening prose excerpt; see the source.

## Nachgereichter Text B: Korrekturen und ein neuer prüfbarer Feldadapter

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:1-11](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L1) · `section:d373729a83875aae09ca` · section

Der Text mit 45 Zeilen wurde vollständig gelesen. Seine unveränderte Kopie steht in late_sources/attachment_B.txt, SHA-256 9aaf5e18cbc6a84d610b88429872df9b69e6078365bfdc8133c8f17e2c1c3801. Die für die neue Prüfung maßgebliche field_dictionary.py ist gesondert eingefroren, SHA-256 a581bacd17c08dd9a766ae439bfe1e8e35e6d30b9509cb9d98053b897d8ecc13. Die bereits abgeschlossenen Schatten-Dateien wurden nicht verändert.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_sources/attachment_B.txt](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_sources/attachment_B.txt#L1) · explicit_file_citation

## Übernahmeentscheidung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:12-92](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L12) · `section:dc7f670608079853f25a` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage im Text & Belastbare Fassung / konkrete Folge \\ 1,44 Milliarden unsichtbare Freiheiten im kleinsten nichttrivialen Sektor & 1444233216 ist die komplexe Kommutantdimension des gewährten Kontrollsatzes X,Nb im N=3-Sektor. Im N=2-Sektor lautet die entsprechende Zahl 3829536. Weder Zahl zählt direkt physische Freiheitsgrade. \\ Mit voller Symmetrie sieben, mit Modenzähl

## 1. Neuer exakter Kontrollgegenzeuge

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:93-109](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L93) · `section:c09f8f4ccc5f58fd8b99` · subsection

Die gewöhnlichen drei Spin-1-Matrizen J_x,J_y,J_z auf C³ erfüllen [J_x,J_y]=iJ_z und zyklisch. Bereits J_x und J_z haben ausschließlich skalare gemeinsame Kommutanten. Der dynamische Lie-Raum ist trotzdem nur su(2) mit Dimension drei, nicht su(3) mit Dimension acht. Das wird im neuen Prüfer durch exakte Ränge und alle drei Kommutatoren kontrolliert.

## 2. Was am Spin-1/2-Projektor stimmt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:110-156](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L110) · `section:d99bdbaf221e8a732da1` · subsection

Die Feldquelle verwendet die sechs unnormierten Koordinaten

## 3. Die neue präzise Händigkeitsschranke

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:157-219](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L157) · `section:5a66fcc5ae711cc77875` · subsection

Die eingefrorene Tabelle in field_dictionary.py, Zeile 327, bezeichnet den zweiten Faktor als f dagger (1/2,0). Dafür muss die Feldabbildung explizit festgelegt werden. Für ein tatsächliches adjungiertes linkes Weylfeld gilt dagegen ψ† in (0,1/2). Hermitesche Konjugation vertauscht diese Darstellungen; siehe https://arxiv.org/pdf/0812.1594\#page=9Dreiner, Haber und Martin, Abschnitt 2.

## 4. Konkreter nächster Annahmetest

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:220-256](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L220) · `section:c737a1a2f0b72f64b05d` · subsection

Der Anschlussauftrag ist jetzt endlich und entscheidbar formuliert:

## Reproduktion

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:257-279](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L257) · `section:c6260e25e90627165dc9` · subsection

Benötigt werden nur Python und SymPy. Der separate Lauf verifiziert zwei Quellenpins sowie 36 exakte Bedingungen pro Modus, keine numerischen Bedingungen. Normaler Lauf und -OO ergeben byte-identische JSON-Ausgaben; Warnungen gelten als Fehler und alle Guards bleiben unter Optimierung aktiv. Die vollständigen Matrizen stehen in late_field.normal.json.

Explicit source references:

- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/replay_late_field.py#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json](../../../../experiments/theory-contracts/universalraum-common-process-20260915/agents/shadows/late_field.normal.json#L1) · explicit_file_citation

## Nachtragsprüfung C: fundamentale Reduktion und globale Quelle

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:280-282](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L280) · `section:d3c0a088a5586a2a0ec9` · section

No opening prose excerpt; see the source.

## Nachtrag C: überwiegend bereits abgedeckte fundamentale Reduktion

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:283-285](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L283) · `section:34a1fbf3ae6036ac6c58` · section

No opening prose excerpt; see the source.

## Übernahmeurteil

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:286-307](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L286) · `section:f4e2353eddc385df8327` · subsection

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere Gesprächszusammenfassung. Er bringt keinen neuen H-Term, keine neue Operationsquelle und keinen neuen Transferbeweis. Seine wesentlichen mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendi

Explicit source references:

- [experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt](../../../../experiments/theory-contracts/universalraum-fable-kernfragen-20260910/context/fortsetzung/source-snapshots/user-attachments/39228cf8-f71d-43e6-9a05-4d49d38d721b/pasted-text.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt#L1) · explicit_file_citation

## Was bestätigt und bereits abgedeckt ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex:308-362](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/017-section-nachgereichter-text-b-korrekturen-und-ein-neuer-.tex#L308) · `section:f38b620b19532b46993e` · subsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage & Urteil und Grenze \\ Volle Schur-Antwort T†F(H−E0)T=γF I64 & Richtig bei gruppeninvariantem H und Grundzustand sowie irreduziblem ursprünglichem Entnahmemultiplett. Gilt für die volle beschränkte Spektralfunktion, nicht nur einen dominanten Pol. Schon in v1.6.7 BIG_PICTURE B2 und der eingefrorenen Kurzfassung enthalten. \\ Aus C_rs(t)=δ_rs c(t) folgt kein Ortsindex

## μ=Δ/50: gegen die älteren gepinnten Zertifikate bestätigt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:1-46](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L1) · `section:5792a66a7bd0978511c1` · subsection

Das ältere universalraum-native-ground-response-20260915/ground_replay/weak_coupling_ground_normal.json enthält genau die genannte Grenze: g/Δ=1/20, μ/Δ=1/50 und neuer Grundsektor N=0. Sein SHA-256 ist e1cd19988edd33c6799ec6b80f0a52d56e1a532bfe1b56870623a4efaf06bd0c; dies stimmt mit ground_replay_manifest.json überein. Normaler und optimierter vorhandener Bericht sind weiterhin bytegleich. Der eingetragene Programmpi

Explicit source references:

- [experiments/theory-contracts/universalraum-v16-integrated-20260915/new_checks.json](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/new_checks.json#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-native-ground-response-20260915/ground_replay/weak_coupling_ground_normal.json](../../../../experiments/theory-contracts/universalraum-native-ground-response-20260915/ground_replay/weak_coupling_ground_normal.json#L1) · explicit_file_citation
- [verification/v16_solar_dual_anchor.py](../../../../verification/v16_solar_dual_anchor.py#L1) · explicit_script_identifier
- [experiments/theory-contracts/universalraum-v16-integrated-20260915/RESULTS.md](../../../../experiments/theory-contracts/universalraum-v16-integrated-20260915/RESULTS.md#L1) · explicit_file_citation

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *) qA3 = 3/4; qD5 = 5/4; checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2]; checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0]; s12 = 1/3 - (2/3) qA3 phi0; checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0]; (* ---- (v23) anchor generator a=(1,1,2) ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L88)

## Zwei Präzisierungen bei der Übernahme

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:47-73](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L47) · `section:b93eca81fe8243a88f5a` · subsection

In §7 sollte „ein positiver Unterschied`` durch „eine nichtverschwindende Differenz`` ersetzt werden. Ein negativer signierter Unterschied ist ebenso ein kausaler Interventionsnachweis; genau dies zeigt der neue N=2-Phasenversuch. Die globale Sektorwahl und die Beobachtbarkeit innerhalb eines festen Gesamtsektors getrennt halten. Ein System-Referenz-Vergleich kann relative Ladungsenergien aufdecken; ein Zusatz μN_tot

## Historischer Teil: vollständige Hauptfassung v1.6.7

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:74-81](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L74) · `section:c10f556505c11202e2ba` · section

Die folgende Fassung bleibt wortgetreu erhalten. Den aktuellen Stand liefern die vorangestellten Kapitel v1.6.8. Frühere Aussagen, Fragen und Vorhaben werden dadurch nicht rückwirkend neu bewiesen. Die neue Synthese ist separat vollständig im eingefrorenen Prüfpaket enthalten.

## TFPT / Universalraum: die richtige einfache Kette

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:82-84](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L82) · `section:c170c6f5e92fd7766a40` · section

No opening prose excerpt; see the source.

## Vollständige Konsolidierung v1.6.7 - 15. September 2026

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:85-87](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L85) · `section:7e63fef586adbcf96730` · subsection

No opening prose excerpt; see the source.

## Ergebnis und Leseschlüssel

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:88-134](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L88) · `section:392a638f98c5ff1d697a` · subsubsection

Die zuletzt ergänzte Vogelperspektive steht im Teil B dieser Fassung: Gesucht wird der kleinste gemeinsame beobachtbare Prozess hinter den verschiedenen Ansichten. Ein nativer Rang-60-Kodierer ist bereits vorhanden. Seine Informationsverluste, die minimalen symmetrieverträglichen Dynamiken und der Unterschied zwischen Korrelation und kausalem Eingriff wurden neu berechnet. Das verschiebt die fundamentale Priorität vo

## 1. Das Gesamtbild: Grammatik, Prozess, Zustand, Antwort

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:135-199](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L135) · `section:ab0b1404a7ab5bc52e84` · subsection

TFPTs Compiler beschreibt zunächst eine markierte algebraische Grammatik: welche Bausteine zusammenpassen, welche Symmetrien gelten und welche Zahlen innerhalb dieser Konstruktion folgen. Der Universalraum soll diese Grammatik als einen ausführbaren Prozess realisieren. Der entscheidende Unterschied ist der zwischen einem erlaubten Zusammenhang und einer tatsächlich erzeugten physikalischen Entwicklung.

## 2. Was die beiden neuen Texte beitragen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:200-202](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L200) · `section:39b6c0e1ec60beaf6643` · subsection

No opening prose excerpt; see the source.

## 2.1 Quellenstand und Reproduktionsgrenzen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:203-242](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L203) · `section:aebaaf9f45e2ba20713f` · subsubsection

17 ausgewählte Eingaben wurden mit SHA-256 eingefroren: beide Nutzertexte, die zugehörigen Programme und Ergebnisdateien, der native Tensor sowie die vollständige frühere Fassung mit Prüfpaket. Keine fremde Quelldatei wurde verändert. Die Herkunftsdateien gehören zu parallel fortgeschriebenen Arbeitsständen; Dateipins sind deshalb wichtiger als Versionsnamen allein.

## 2.2 Übernahmeentscheidung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:243-290](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L243) · `section:4dba61194e3f14b294c9` · subsubsection

@ > p( - 2 ) * 0.5000 > p( - 2 ) * 0.5000@ Aussage aus den Eingaben & Entscheidung für v1.6.7 \\ Korrigierter Anfangskommutant 3829536 / 1444233216 & Bestätigt; keine neue Größe gegenüber v1.6.6 \\ Nur SU(4) oder nur Spin(10) als zusätzliche Kontrollen & Übernommen; echte Zwischenstufen statt binärer Verfügbarkeit \\ Volle Gruppe plus alle Modenbesetzungen erzeugt volle Sektoralgebra & Unabhängig bestätigt, ausdrückl

## 3. Vollständig gelöst: der erste verzweigte Singulettbereich

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:291-293](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L291) · `section:d356742f420aa6f8eabd` · subsection

No opening prose excerpt; see the source.

## 3.1 Warum vier und nicht eins?

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex:294-360](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/018-subsection-50-gegen-die-lteren-gepinnten-zertifikate.tex#L294) · `section:5a54e89abf080c1fd62c` · subsubsection

Im Ladungssektor N=64 schreiben wir Zustände relativ zur gefüllten Fermionreferenz [formula in source] . Bei k Bosonen gibt es 2k Löcher. Der Singulettbereich auf dieser Stufe liegt in

## 3.2 Nicht nur gezählt: die vier Zustände und ihre Kopplungen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:1-55](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L1) · `section:df239487ba88a28bc899` · subsubsection

In der durch eine Bosonparität äquivalenten Lochdarstellung sei [formula in source] . Alle 108240 von null verschiedenen Koeffizienten von [formula in source] wurden neu berechnet, einschließlich der Boson-Fakultätsnormen. Das ergibt [formula in source] .

Explicit source references:

- [verification/v2_carrier_pascal.py](../../../../verification/v2_carrier_pascal.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [(* ---- (v2) carrier / Pascal ---- *) checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16]; checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)", Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16]; checkExact["N_fam = 3", Nfam == 3]; checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8]; (* ---- (v13) M = 41 budget ---- *)](../../../../verification/wolfram/tfpt_readouts.wl#L50)
- [experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/ArfSpinorCompiler.lean#L1)

## 3.3 Der vollständig bestimmte Sechszustands-Ausschnitt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:56-84](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L56) · `section:d09ccd6e9c184a435bdb` · subsubsection

Die Kompression auf alle Singuletts mit k kleiner oder gleich zwei ist exakt äquivalent zu

## 4. Die richtige einfache Kette: Wiederholung von H

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:85-87](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L85) · `section:5fd0f7c7ae1e792ce761` · subsection

No opening prose excerpt; see the source.

## 4.1 Der Fehler war die Gleichsetzung zweier verschiedener Stufen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:88-111](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L88) · `section:2184b5d5980e35658802` · subsubsection

Die Vektoren [formula in source] sind nach Bosonzahl geordnet. Schon bekannt ist

## 4.2 Die ersten fünf Glieder sind jetzt exakt bestimmt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:112-160](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L112) · `section:8f990094be147bbb3a49` · subsubsection

Für die normierte Lanczos-Basis [formula in source] schreiben wir

Explicit source references:

- [verification/v4_flavor_matrix.py](../../../../verification/v4_flavor_matrix.py#L1) · explicit_script_identifier

Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):

- [experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean](../../../../experiments/lean4-carrier-rigidity/TfptCarrier/YukawaPrimitive.lean#L1)

## 4.3 Zehn vollständige Energiemomente der gefüllten Referenz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:161-206](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L161) · `section:8853e744c11e8e03cea0` · subsubsection

Die Fünfer-Kompression bestimmt [formula in source] für n von 0 bis 9 exakt. Ein Weg, der den nächsten nicht enthaltenen Lanczos-Vektor erreicht und nach F zurückkehrt, benötigt mindestens zehn Schritte. Aus der Tridiagonalität folgt deshalb die angegebene Momentengenauigkeit, ohne die übrige Kette zu erfinden.

## 4.4 Kleine, rigorose Verschärfung der Energiegrenze

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:207-235](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L207) · `section:6b5e01a1f0b7b2d5045a` · subsubsection

Am Prüfpunkt g geteilt durch Delta gleich 1/20 hat die niedrigste Eigenenergie der Fünfer-Kompression die durch rationale Sturm-Zählung zertifizierte Lage

## 5. Vollständig gelöst: die innere bilineare Zerlegung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:236-274](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L236) · `section:13149eabfc476fcff371` · subsection

Die sechs Dimensionen sind 1, 45, 210, 15, 675 und 3150. Der offene Rest ist also nicht mehr unbestimmt:

## 6. Welche Operationen wirklich verfügbar sein müssten

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:275-277](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L275) · `section:3a9e1bdcabd9b1b8e669` · subsection

No opening prose excerpt; see the source.

## 6.1 Die algebraische Frage ist präziser beantwortet

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:278-320](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L278) · `section:c396d51f7a348a5d4f0c` · subsubsection

Im N=3-Sektor bleiben für verschiedene angenommene Operationsalphabete folgende komplexe Kommutantdimensionen:

## 6.2 Warum bloßes Lesen noch keine fehlende Bewegung erzeugt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:321-338](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L321) · `section:6f0cddb427528526467a` · subsubsection

Ohne die zusätzlich gewährten Gruppenkontrollen erhalten X, Nb, der Clock und alle Modenbesetzungen weiterhin mindestens eine nichtskalare Farb-Cartanladung. Jede Komposition dieser Operatoren behält diese Erhaltung. Die alleinige Erlaubnis, mehr Moden zu unterscheiden, hebt das Hindernis also nicht auf.

## 7. Feldwörterbuch: gesicherte Teile und korrigierte Reichweite

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex:339-369](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/019-subsubsection-3-2-nicht-nur-gez-hlt-die-vier-zust-nde-un.tex#L339) · `section:c1061254d29efc0b0f1f` · subsection

Für die unveränderte antisymmetrische Paarmatrix und gleichhändige Weylfelder verschwindet die ableitungsfreie skalare Kontraktion. Die drei symmetrischen Spinortensoren tragen einen nichtverschwindenden Kanal des Typs (1,0), mit konjugiertem Typ (0,1). Das ist am gesamten ursprünglichen Tensor neu geprüft.

## 8. Die fundamentale Frage: was fehlt wirklich?

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:1-3](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L1) · `section:3e66d357266564eeebcb` · subsection

No opening prose excerpt; see the source.

## 8.1 Ein überprüfbarer Unterbestimmtheitssatz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:4-32](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L4) · `section:7f06ec0c70ab2a24d278` · subsubsection

Betrachte bei festem W dieselbe Familie [formula in source] . Alle diese Hamiltonoperatoren besitzen die gleiche innere Quellsymmetrie, dieselbe Ladungserhaltung und denselben kommutierenden endlichen Clock. Dennoch unterscheiden sie sich dynamisch. Schon für dieselbe gefüllte Referenz F ist die dimensionslose Momentenkombination

## 8.2 Der kleinste tragfähige Forschungsansatz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:33-55](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L33) · `section:316f6149d5feb631a72f` · subsubsection

Für eine einzelne Antwortrechnung sollte der relevante Raum nicht von vornherein der gesamte Fockraum sein. Der zyklische Raum der tatsächlichen Operationen auf dem angegebenen Startzustand ist der kleinere Arbeitsraum. Die H-Lanczos-Kette ist eine exakte Darstellung eines solchen Raums. Mehrere Präparationen, Messungen oder Compileroperationen können jedoch einen größeren gemeinsamen Prozessraum verlangen. Ihre Komp

## 9. Aktueller Stand T1 bis T8

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:56-110](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L56) · `section:be988edcf21afe0f230a` · subsection

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

## 10. Die drei nächsten entscheidenden Untersuchungen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:111-143](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L111) · `section:a4b872b85951d6ba1a87` · subsection

Den minimalen Ursprungsvertrag auswählen. Teil B klassifiziert die kleinen symmetrieverträglichen Terme und trennt echte Erweiterungen von einem bloßen Wechsel der Bosonvariablen. Der Compiler muss diese Auswahl und die relativen Parameter begründen. Symmetrie allein tut das noch nicht. Die gemeinsame Schattenkarte am vorhandenen Tensor prüfen. Derselbe Zustand und dieselben Operationen müssen die verschiedenen Ausle

## 11. Reproduktion und Veröffentlichung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:144-167](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L144) · `section:bdfff177be89c539256f` · subsection

Das Prüfpaket enthält sechs neue Python-Prüfer, die eingefrorenen Quellen, die alte und neu wiederholte Kontraktion, Ergebnisdateien, Quellenmanifest und die vollständige v1.6.6 als historische Basis. replay.py prüft alle Pins, beide Python-Modi und die C++-Kontraktion. Die ausgelieferte ZIP wird nach dem Entpacken erneut geprüft.

## Schluss in einem Satz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:168-176](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L168) · `section:ebdef79ffad8067cb4e9` · subsubsection

Die einfache Regel ist vorhanden; ihr erster verzweigter Zustandsbereich und die richtige kleine Rechenkette sind jetzt genauer gelöst. Was noch fehlt, ist die aus dem Ursprung folgende Auswahl und Ausführung dieses Prozesses als dieselbe physikalische Welt.

## Neue Vogelperspektive: derselbe Prozess in verschiedenen Ansichten

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:177-179](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L177) · `section:7c0dc9b5f3800a9b8b0e` · section

No opening prose excerpt; see the source.

## B1. Was sich durch die drei weiteren Texte ändert

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:180-234](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L180) · `section:f617402b6fa30f7c4613` · subsection

Die nachgereichten Texte werden als Vorschläge geprüft, nicht als bewiesene Ergebnisse oder neue Arbeitsanweisungen übernommen. Die stärkste gemeinsame Idee trägt: Innere Identität, Zusammensetzung, Ort, Zeit und Auslese dürfen nicht stillschweigend dasselbe Label erhalten. Eine immer genauere Rechnung innerhalb einer Bank ersetzt diese Verbindungen nicht. Die voranstehenden lokalen Ergebnisse bleiben gültig; die fun

Explicit source references:

- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/runtime_synthesis.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/runtime_synthesis.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/multiplicity_z4.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/multiplicity_z4.txt#L1) · explicit_file_citation
- [experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt](../../../../experiments/theory-contracts/universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt#L1) · explicit_file_citation

## B2. Noethers Frage: Welche Unterschiede kann die Dynamik überhaupt verändern?

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:235-287](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L235) · `section:030e0693c77684ad1988` · subsection

Bei ungebrochener innerer Gruppe G zerfällt ein Zustandsraum als

## B3. Korrelation ist noch kein Eingriff: ein exakt gelöstes Gegenbeispiel

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:288-340](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L288) · `section:bc975c23a1ebffb4e56e` · subsection

Die Kreuzkorrelation startet bei null und verändert sich mit der Zeit. Es gibt dennoch keinerlei Signal von A nach B: Alle A-lokalen Operationen kommutieren mit jedem zeitentwickelten B-lokalen Observablen. Für jedes spurtreue lokale Quanteninstrument bleibt daher die unbedingte B-Statistik unverändert. Eine Konditionierung auf ein Messergebnis in A wäre etwas anderes.

## B4. Die einfachste fehlende Auswahl: Warum genau dieser Hamiltonoperator?

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex:341-364](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/020-subsection-8-die-fundamentale-frage-was-fehlt.tex#L341) · `section:e92954078672cae8e465` · subsection

Die Z4-Idee besitzt einen präzisen Kern. Ein ganzzahliger, auf jedem Grad konstanter Ladungslift mit neutralem Grad null müsste bei den entsprechenden nichtverschwindenden Klammern erfüllen

## B4.1 Zwei zusätzliche Terme am unveränderten Tensor

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:1-84](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L1) · `section:065f7f9e235fca7fedf7` · subsubsection

Der Bosonträger (10,6) besitzt eine symmetrische reelle invariante Paarung eta. In der nativen Gewichtsbasis koppelt sie entgegengesetzte Spin- Vektorgewichte und komplementäre Farbpaare. Es gilt eta Quadrat gleich eins. Damit sind bereits

## B4.2 Eine weitere Vereinfachung: neue Dynamik oder andere Teilchenvariablen?

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:85-133](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L85) · `section:cdad006b6f1b4120a8f6` · subsubsection

Manche scheinbaren Erweiterungen beschreiben nur andere Bosonvariablen. Auf der reellen, phasengleichen Teilfamilie setze man

## B5. Holografie und Schatten: die konkrete native Verbindung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:134-136](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L134) · `section:998fc3c594dafe88d9c3` · subsection

No opening prose excerpt; see the source.

## B5.1 Ein Kodierer ist bereits vorhanden

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:137-171](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L137) · `section:5cac2ec7d752a7986bbb` · subsubsection

Der vorhandene, frisch geprüfte Tensor erfüllt WW dagger gleich 8 I60. Daher ist

## B5.2 Warum das noch kein holografischer Fehlerkorrekturcode ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:172-205](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L172) · `section:7042d1a31ab37cc31ed3` · subsubsection

Für jeden der 64 Fermionmoden wurde die logische Kompression seiner Besetzungsmessung berechnet:

## B5.3 Was mehrere Schatten gemeinsam eindeutig machen können

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:206-260](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L206) · `section:ddcea03d428c4a34887a` · subsubsection

Seien Ri festgelegte Mess- oder Reduktionsabbildungen eines gemeinsamen Zustands rho. Für eine endliche, nicht eingeschränkte Zustandsklasse sind alle Zustände aus den Schatten Ri(rho) genau dann unterscheidbar, wenn auf den hermiteschen spurlosen Differenzen gilt

## B5.4 Die drei Wände müssen unterschiedlich geprüft werden

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:261-307](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L261) · `section:5ea80db298148b04d640` · subsubsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Gemeinte Wand & Was sie gegenwärtig bedeutet & Welcher Anschluss fehlt \\ Universalraum & Grenze zwischen gemeinsamem Operatorobjekt und seinen reduzierten Ansichten & Ein gemeinsamer verfügbarer Operationssatz, Zustand und Rekonstruktionsvertrag \\ TFPT & Grenze zwischen interner Compilerstruktur und physikalischer Realisierung & Herleitung der Ausführun

## B6. Die einfachste neue Arbeitsrichtung und ihre Abnahmekriterien

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex:308-369](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/021-subsubsection-b4-1-zwei-zus-tzliche-terme-am-unver-ndert.tex#L308) · `section:5e2722c4b773dffe738f` · subsection

Der plausible übersehene Punkt ist kein weiterer großer Tensor: Wir brauchen die gemeinsame Regel, die festlegt, welche Operationen, Teilchenvariablen und Ansichten tatsächlich dieselbe Ausführung beschreiben. Noethers Symmetrieprüfung sagt, was erhalten bleibt. Die Schattenprüfung sagt, was überhaupt unterscheidbar ist. Der Eingriffstest sagt, was etwas anderes beeinflussen kann. Zusammen sind diese drei kleinen Fra

## B7. Abgleich des zuletzt eingesandten Berichts v1.6.3

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:1-85](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L1) · `section:d58bf41bd62909fdbbde` · subsection

Der sechste Text dieser Runde, „Operationssatz, nativer Grundzustand und Feldwörterbuch``, enthält überwiegend bereits berücksichtigte Befunde: die Kommutantenleiter, das Lochbild, die Normen der ersten Stufen, den nichtverschwindenden Seitenzweig und den verschwindenden Weyl-Skalarkanal. Seine zweite vorgeschlagene Folgeaufgabe wurde inzwischen wesentlich weitergeführt: Alle vier Zwei-Boson-Singuletts sind konstruie

## Historischer Anhang: vollständige Fassung v1.6.6

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:86-94](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L86) · `section:6c6e891c0496b6a29275` · section

Die folgende vollständige Fassung wird unverändert bewahrt. Maßgeblich für den aktuellen Status sind die vorangestellten Kapitel v1.6.7. Ältere Vorhaben, Modellannahmen und Zahlen erhalten dadurch keinen neuen Beweisstatus; die kleinen Energieverschärfungen und die neuen Singulett- und Bilinearergebnisse stehen oben.

## TFPT / Universalraum: Clock, gemeinsame Quelle und tatsächlicher Transport

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:95-98](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L95) · `section:64fffe38c59f934adfa5` · section

No opening prose excerpt; see the source.

## Konsolidierung und eigene Forschungsfortsetzung v1.6.6 - 15. September 2026

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:99-124](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L99) · `section:6573a97655859181058d` · subsection

Ergebnis: Der dokumentierte endliche Clock ist jetzt ausdrücklich als Element der vorhandenen inneren Spin(10)-Symmetrie konstruiert. Dadurch lässt sich die bislang offene gemeinsame Clock-/Casimir-Auslesung exakt bestimmen. Daneben wurde ein kleiner, echter Vierzustandskanal der ursprünglichen Paarwechselwirkung gefunden, der nach Zulassung eines Bosonmischers eine Fermionenmarke überträgt. Die Herkunft dieses Misch

## Leseschlüssel

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:125-145](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L125) · `section:aec12f4656ae2bed82d6` · subsubsection

Exakt: Identität oder mathematische Folgerung im angegebenen Modell. Numerisch: berechneter Näherungswert, ohne zertifizierte Einschließung. Bedingt: exakter Satz erst nach ausdrücklich zusätzlicher Ressource. Offen: fehlende Herleitung oder physikalische Identifikation.

## 1. Die unveränderte gemeinsame Grundlage

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:146-195](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L146) · `section:8c31aa56f7dce07bc808` · subsection

Mit 64 Fermionmoden, 60 Bosonmoden und demselben gepinnten Tensor gilt

## 2. Quellenprüfung der beiden neuen Ergebnisrunden

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:196-198](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L196) · `section:c0d8903f0fb76e1c151e` · subsection

No opening prose excerpt; see the source.

## 2.1 Bestätigte Zerlegung, korrigierte Operationsaussagen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:199-278](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L199) · `section:69587dcaabdec10ff0b4` · subsubsection

Die 944, 31 und 152 mitgelieferten Prüfbedingungen der Symmetrie-, Verfügbarkeits- und Lorentzprogramme sind normal und optimiert byteidentisch reproduziert. Darunter befinden sich neun wörtliche need(True, ...)-Guards mit theoretischen Folgerungen. Sie zählen als ausgeführte Guards, nicht als neun unabhängige Beweise. Die Clock-Normalisatorbehauptung gehörte dazu; Abschnitt 3 ersetzt sie durch eine explizite Konstru

## 2.2 Der Grundzustandsbericht enthält einen Versionskonflikt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:279-333](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L279) · `section:2129499a8d08fa55d5c3` · subsubsection

Der neue Text hat die Nichtschlussnorm bereits korrigiert, das danebenliegende native_ground_state.json stammt jedoch von einer älteren Codefassung. Sein als PASS markierter Wert ist um 229² zu groß; die dortige relative orthogonale Norm ist sogar größer als eins. Der daraus berechnete Ritzwert −1,18826198 wird nicht übernommen.

## 3. Neuer exakter Anschluss: Der Clock liegt bereits in Spin(10)

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:334-336](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L334) · `section:a4581c5dacad414f82c0` · subsection

No opening prose excerpt; see the source.

## 3.1 Ausgangspunkt ist der tatsächliche Quell-Clock

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex:337-353](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/022-subsection-b7-abgleich-des-zuletzt-eingesandten-berichts.tex#L337) · `section:fab89133a699482e0028` · subsubsection

Der gepinnte endliche Compilerpräfix liefert auf fünf Hilfsachsen

## 3.2 Ein ausdrückliches Spinwort

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:1-57](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L1) · `section:a00acff753eb19e57a65` · subsubsection

R_ab ist das Produkt zweier reeller Einheitsvektoren der Cliffordalgebra, also ein Spin(10)-Element. Direkt gilt R_ab=i Γ((ab)). Da p=(01)(02)(34) mit rechts zuerst angewandter Permutation, folgt

## 4. Clock und getrennte Casimire lassen sich gemeinsam auslesen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:58-136](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L58) · `section:575ef8be440839620032` · subsection

Weil G aus Spin(10) stammt und auf SU(4) trivial wirkt, kommutiert es mit beiden getrennten Casimiren, auch auf ihren Fockhebungen. Die Frage aus dem neuen Text ist damit auf algebraischer Ebene beantwortet.

## 5. Neuer kleiner Transportzeuge mit tatsächlichen W-Kanälen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:137-216](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L137) · `section:3b915ba44ccd90770c46` · subsection

Ein gemeinsamer Fermion-/Boson-Dreierstern hätte die einfache Identität

## 6. Das Feldwörterbuch: eine Basisänderung allein reicht nicht

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:217-275](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L217) · `section:83d5e7dd6925cb1c5658` · subsection

Der bestätigte Grundfehler bleibt: M_A⊗ε_Lorentz ist symmetrisch und verschwindet als Grassmann-Bilinear. Das betrifft die lokale ableitungsfreie Zuordnung einer gleichhändigen Weylkopie je ursprünglichem Label bei unverändertem antisymmetrischem W. Der nichtverschwindende gleichhändige Kanal trägt (1,0); daraus folgt noch keine gesunde Kinetik.

## 7. Was der nachgereichte Universalraum-Text trägt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:276-278](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L276) · `section:155d1397a7020495c822` · subsection

No opening prose excerpt; see the source.

## 7.1 Eine sinnvolle Hypothese, kein bereits identifiziertes universelles Objekt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:279-300](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L279) · `section:f4b8b2d82627272933a3` · subsubsection

Nichtorthogonale oder überlappende lokale Einbettungen in eine gemeinsame Algebra sind eine ernstzunehmende Alternative zu unabhängigen Banken. Sie können Voraussetzungen der lokalen Paritätsschranke ändern. Das ist ein Forschungsauftrag, kein Widerspruch zur bisherigen Schranke.

## 7.2 Der vorgeschlagene Kill-Test muss korrigiert werden

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:301-312](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L301) · `section:813bdd207e56b625fb6d` · subsubsection

Für unabhängige orthogonale Banken kann Π_AΠ_B deren gemeinsame Parität sein. Für überlappende Unterräume gilt das nicht allgemein; ihre lokalen Paritäten müssen nicht einmal kommutieren. Der Test [U,Π_AΠ_B]=0 ist deshalb im neuen Bild nicht der richtige universelle Test. Stattdessen muss die tatsächliche globale Parität Π_global separat definiert und erhalten werden. Ein nichtverschwindender Kommutator mit einer lok

## 7.3 Der einfachste False-Positive: Ein Signal ohne Bewegung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex:313-358](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/023-subsubsection-3-2-ein-ausdr-ckliches.tex#L313) · `section:bd5a4872fda196bcc130` · subsubsection

Seien a=c1, b=(c1+c2)/√2 auf zwei globalen CAR-Moden und H=ωN. Dann haben die beiden Einteilchen-Chartzustände bereits Überlappung 1/√2. In ihrer nichtorthogonalen Basis ist K=ωS mit einem nichtverschwindenden Offdiagonalelement. Trotzdem bleibt die betreffende Wahrscheinlichkeit zu jeder Zeit genau 1/2. Es wurde nichts transportiert.

## 7.4 Was nicht automatisch folgt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:1-44](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L1) · `section:23130b07cbb342e42089` · subsubsection

Zeit: Für einen Grundzustand ist e \-itH\Ω=e \-itE0\Ω; sein physischer Zustand bleibt gleich. Das ist kein eigener Zeitpfeil. Nichtstationäre Präparation, Korrelationen und Records müssen ausgewiesen werden. Eichfeld: Für bloße Basiswechsel Uxy=Vx†Vy teleskopiert jede geschlossene Holonomie zu I. Echte Krümmung braucht zusätzliche Verbindungs-/Transportdaten oder einen nachgewiesenen Mechanismus. Spin: Zwei Orientier

## 8. T1-T8: gemeinsamer Fortschritt ohne Statusinflation

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:45-95](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L45) · `section:647b51d5509c9a9c81db` · subsection

@ > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333 > p( - 4 ) * 0.3333@ Front & In dieser Revision weitergekommen & Noch erforderlicher Nachweis \\ T1 - Ursprung und Auswahl & Explizite Identität zwischen Quell-Clock und innerer Spinwirkung; Operationsverträge genauer & Primitive Auswahl von P1/P2, Träger, erlaubten Instrumenten und Zustand \\ T2 - Half-Charge/E8-Feld & Bestehender geladener Pol bleibt abgesichert, innere Dar

## 9. Die nächsten drei Arbeiten - klein, gemeinsam und entscheidbar

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:96-129](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L96) · `section:b50f635ff03edfdf0669` · subsection

A. Den gemeinsamen Quellenvertrag wirklich hinschreiben. Zwei lokale Einbettungen, ihr CAR-Gram, globale Parität und Ladung, ursprüngliche Operationen und ein einziges H angeben. Abbruch für eine Kandidatenfassung, wenn sie nur zwei Koordinatenansichten desselben unveränderten Signals umbenennt. Die gemeinsamen Generatoren müssen einen nachweislich neuen Antwortprozess ermöglichen, nicht nur eine andere Beschriftung.

## 10. Belege und Reproduzierbarkeit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:130-151](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L130) · `section:54f4776c1da819c64ef6` · subsection

Die drei Eingangstexte bleiben unverändert im Prüfpaket. Ein Teil-Audit reproduziert die 1127 gelieferten Guards; eigene Programme behandeln Clock/Casimir, Quellenreichweite, direkte Krylov-Kontraktion, basisunabhängige Feldbedingungen, den tatsächlichen Vierzustandskanal und die Überlappungsgegenkontrollen. Exakte und numerische Teile sind in den jeweiligen Ergebnisdateien getrennt markiert. Die abschließenden Zählu

## Anhang A: Quellenprüfung Symmetrie und Verfügbarkeit

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:152-154](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L152) · `section:9f67ee52909b9e8025d3` · section

No opening prose excerpt; see the source.

## Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:155-162](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L155) · `section:a44fbc0812f8307d9880` · section

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1-T8 geschlossen seien.

## 1. Reproduktion

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:163-224](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L163) · `section:0a28a38683110fc6d278` · subsection

Alle drei Programme wurden vollständig gelesen und anschließend in isolierten Kopien ausgeführt. Die relevanten Tensoren wurden an ihre von den unveränderten Programmen erwarteten relativen Orte kopiert. Normaler und optimierter Lauf reproduzieren jeweils die gelieferten Ergebnisdateien byteidentisch, ohne Standardfehlerausgabe:

Explicit source references:

- [experiments/theory-contracts/universalraum-clock-origin-20260915/agents/symmetry_audit/check_scope.py](../../../../experiments/theory-contracts/universalraum-clock-origin-20260915/agents/symmetry_audit/check_scope.py#L1) · explicit_file_citation

## 2. Bestätigte Mathematik

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:225-275](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L225) · `section:8a19c202369cc314cb41` · subsection

Der N=3-Raum zerfällt als Darstellung von Spin(10) × SU(4) in sieben Isotypien. Drei haben Multiplizität zwei, die anderen vier Multiplizität eins. Die zwei Fockteile Λ³(C⁶⁴) und C⁶⁰⊗C⁶⁴ sind jeweils multiplizitätsfrei; der gesamte N=3-Raum ist es ausdrücklich nicht.

## 3. Invarianz und Kovarianz auseinanderhalten

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:276-312](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L276) · `section:7bb22cd4a70d4314ce87` · subsection

Dann gilt A0 ⊂ C, dim A0=14 und dim C=Σ m_i²=16. Jedes Wort aus X und Nb kommutiert mit ρ(G). Nichtzentrale Lie-Erzeuger können deshalb aus diesem Alphabet nicht entstehen. Dieser Ausschluss ist korrekt und bleibt richtig, wenn nur ein fixes H statt zweier unabhängiger Kontrollen gewährt ist.

## 4. Verfügbarkeit ist keine universelle Ja/Nein-Frage

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:313-353](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L313) · `section:759cf6ea27265d6ebcee` · subsection

Ein vorgegebener Hamiltonoperator allein gewährt nicht bereits das unabhängige Schalten von X und Nb. Am erklärten Punkt g/Δ=1/20 besitzt ein fixes H im N=3-Raum acht verschiedene Energien, also nur eine acht-dimensionale kommutative Spektralalgebra. Die großzügigere Annahme unabhängiger Kontrollen X,Nb ergibt 14.

## 5. Der Clock-Satz ist im gelieferten Checker nicht geprüft

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex:354-372](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/024-subsubsection-7-4-was-nicht-automatisch.tex#L354) · `section:011cec9b73c9589be7a9` · subsection

operation_symmetry.py:478 schreibt den Normalisator- und Nichts-hinzufügen-Satz als need(True, ...). Insgesamt enthält diese Datei neun solche als Prüfbedingungen gezählten theoretischen Folgerungen. Einige sind durch die vorausgehende Mathematik gut begründet; der bloße grüne Guard zertifiziert sie jedoch nicht unabhängig.

## 6. Feldtyp: was tatsächlich erzwungen ist

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:1-32](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L1) · `section:aadf543c685fe83f9b63` · subsection

Für ein lokales, ableitungsfreies Bilinear zweier gleichhändiger Weylfelder, das alle 64 inneren Quellenmarken unverändert als unabhängige innere Komponenten und genau den gegebenen antisymmetrischen Tensor W verwendet, gilt

## Konkreter Gegencheck jenseits der ableitungsfreien Klasse

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:33-55](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L33) · `section:cc1572e1bc51f23e766d` · subsubsection

Der allgemeine Satz »ein Vektor verlangt ψ†ψ und scheitert deshalb an der Ladung« ist falsch, sobald Ableitungen zugelassen werden. Beispielsweise ist

## 7. Konsequenz

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:56-67](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L56) · `section:6af98943100615ff2f10` · subsection

Die neuen Quellen verkleinern und präzisieren den endlichen N=3-Operationsraum. Sie schließen weder die physische Verfügbarkeit der Operationen noch den Lorentzadapter. Die sachlich tragfähige Integration übernimmt die Zerlegung, Casimire, 14/16/7 im jeweils erklärten Vertrag sowie den eingeschränkten Feldtypsatz; sie ersetzt die überbreiten Ausschlüsse und die behauptete Programmumkehr durch explizite Bedingungen.

## Anhang B: unabhängige Krylov- und Feldprüfung

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:68-70](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L68) · `section:cafa556b2092f4239e02` · section

No opening prose excerpt; see the source.

## Unabhängige Prüfung: Krylov-Verzweigung und Feldwörterbuch

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:71-81](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L71) · `section:814c46fad019c0a9b346` · section

Arbeitsstand 2026-09-15. Geprüft wird die Anlage 7380c383-f364-4ef8-8066-24aa4d180d85 gegen den Vertrag universalraum-native-operations-ground-response-20260915. Fremde Quellen und Ausgaben wurden nicht verändert. Die hier angegebenen Matrix- und Graphbefunde beziehen sich auf denselben gepinnten Tensor W mit SHA-256 3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763.

## 1. Der neue Nichtschluss ist exakt bestätigt

[documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex:82-121](../../../../documents/experiments--theory-contracts--universalraum-spin-lift-basics-20260915--tmp--pdfs--TFPT_Universalraum_Spinlift_Hauptdokument_2026-09-15_v1.6.10/sections/025-subsection-6-feldtyp-was-tats-chlich-erzwungen.tex#L82) · `section:ba4b2f7292a59b400c07` · subsection

Für v_n=(T†) n F habe ich u=T T† v_2=T v_3 unmittelbar aus den 480 nativen Paaren neu kontrahiert. Das materialisiert nicht die 15.252.960 Komponenten von v₃. Es arbeitet mit 108.240 Komponenten von v₂ und 293.280 nichtverschwindenden Komponenten des Ergebnisses u. Es wurden 45.771.360 zulässige Erzeugungsübergänge und 139.289.760 anschließende Entnahmebeiträge exakt mit ganzzahliger Fermion-Parität und Boson-Multipl
