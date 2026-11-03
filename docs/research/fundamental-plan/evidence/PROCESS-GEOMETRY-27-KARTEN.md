# Die27 Websitekarten und das getrennte eingefrorene Register

31. Oktober2026. Quelleninventar aus den unveränderten Dateien. Die Statusangaben unten sind die Originalmetadaten der Website. Diese Tabelle ist keine aktuelle empirische Neubewertung.

Die Website enthält27 Karten:vier numerische Fixpunkte,fünf exakte Identitäten,16 bedingte Aussagen und zwei offene Aussagen. Das eingefrorene Register enthält16 predictions,zwei zugewiesene Texturwerte,zwei bedingte Bänder und zwei ausdrücklich nicht als Vorhersagen geführte Varianten. Die Bestände werden nicht gleichgesetzt.

| Karte | Originalstatus | Gemeinsame Abhängigkeitsklasse | Claim im Original | Originalzeile |
|---|---|---|---|---|
| alpha-em | Numerical fixed point | EM closure | EM.FP.01 | 342 |
| lambda-c | Exact identity | Flavor / residue matrix | FLAV.CKM.01 | 372 |
| flavor-invariants | Exact identity | Flavor / residue matrix | FLAV.R.01 | 400 |
| koide | Conditional | Frontier interface | FR.KOIDE.01 | 430 |
| theta12 | Numerical fixed point | Neutrino transport | FLAV.TH12.01 | 459 |
| theta13 | Exact identity | Neutrino transport | REG.FREEZE.01 | 495 |
| theta23 | Conditional | Neutrino transport | REG.FREEZE.01 | 533 |
| neutrino-ordering | Conditional | Neutrino transport | PRED.LAYER.01 | 561 |
| delta-pmns | Conditional | Neutrino transport | GALOIS.READOUT.01 | 592 |
| strong-cp | Exact identity | Strong-CP closure | PRED.LAYER.01 | 632 |
| mpme | Open / not forced | Frontier interface | FR.MPME.01 | 668 |
| ns | Conditional | Inflation (R²) | COSMO.INF.01 | 697 |
| r-tensor | Conditional | Inflation (R²) | COSMO.INF.01 | 733 |
| as-amplitude | Conditional | Inflation (R²) | COSMO.INF.01 | 770 |
| alpha-s-running | Conditional | Inflation (R²) | in dieser Karte nicht zugeordnet | 806 |
| mu-distortion | Conditional | Inflation (R²) | in dieser Karte nicht zugeordnet | 844 |
| scalaron | Numerical fixed point | Inflation (R²) | GRAV.SCAL.01 | 881 |
| omega-b | Conditional | Scale grammar | COSMO.OMB.01 | 910 |
| eta-b | Conditional | Frontier interface | FR.ETAB.01 | 946 |
| hubble | Conditional | Scale grammar | COSMO.LAM.01 | 983 |
| no-second-higgs | Exact identity | Carrier / Higgs index | EM.BUDGET.01 | 1019 |
| higgs-free-seam | Conditional | Carrier / Higgs index | HIGGS.FREESEAM.01 | 1047 |
| birefringence | Numerical fixed point | Horizon / determinant line | HOR.01 | 1087 |
| axion | Conditional | Frontier interface | FR.DM.01 | 1124 |
| rare-kaon | Conditional | Flavor / residue matrix | FR.RAREKAON.01 | 1164 |
| eht-intercept | Conditional | Horizon / determinant line | HOR.EHT.01 | 1204 |
| hfqpo-tooth | Open / not forced | Frontier interface | in dieser Karte nicht zugeordnet | 1243 |

## Die genaue Regel jeder Karte

### Fine-Structure Constant — Electromagnetic Fixed Point

α⁻¹(0) = 137.035 999 216 8…

Originalformeln:

* `F_{U(1)}(\alpha) = \alpha^3 - 2c_3^3\alpha^2 - \tfrac{4}{5}c_3^6\Big(\textstyle\sum_{f,j}L_{f,j} + N_\Phi\Big)\log\tfrac{1}{\varphi_{\mathrm{seam}}(\alpha)} = 0`
* `\textstyle\sum_{f,j}L_{f,j} + N_\Phi = 41 = 10\,b_1`
* `\alpha^{-1} = 137.035\,999\,216\,8\ldots`

### Cabibbo Angle — Retained Seed

λ_C = 0.22438

Originalformeln:

* `\varphi_0 = \frac{1}{6\pi} + \frac{3}{256\pi^4}`
* `\lambda_C = \sqrt{\varphi_0(1-\varphi_0)} = 0.22438`

### Flavor Residue Invariants

det R = 8, minors (2,3,5), χ_R = t³ − 9t² + 10t − 8

Originalformeln:

* `R = \begin{pmatrix} 1 & 3 & 0 \\ 1 & 5 & 2 \\ 2 & 5 & 3 \end{pmatrix}`
* `\det R = 8 = h(D_5), \quad \|R\|_F^2 = 78 = \dim E_6`
* `\chi_R(t) = t^3 - 9t^2 + 10t - 8`

### Koide Relation — Near 2/3

Q = 0.664 (target 2/3 = |ℤ₂|/N_fam)

Originalformeln:

* `Q_{\mathrm{TFPT}} = \frac{\sum_\ell \hat m_\ell}{(\sum_\ell \sqrt{\hat m_\ell})^2} = 0.66446\ldots`
* `Q_\star = \frac{|\mathbb{Z}_2|}{N_{\mathrm{fam}}} = \frac{2}{3}`

### Solar Angle — Seam Misalignment

sin²θ₁₂ = 1/3 − φ₀/2 = 0.3067

Originalformeln:

* `\varepsilon = q(A_3)\,\varphi_0 = \tfrac{3}{4}\varphi_0 = c_3 + 36\,c_3^4`
* `\sin^2\theta_{12}^{\mathrm{seed}} = \tfrac{1}{3} - \tfrac{2}{3}\varepsilon = \tfrac{1}{3} - \tfrac{\varphi_0}{2} = 0.306747`

### Reactor Angle — Seed × Carrier Trace

sin²θ₁₃ = φ₀ e^(−5/6) = 0.0231

Originalformeln:

* `\sin^2\theta_{13} = \varphi_0\,e^{-5/6}`
* `\varphi_0 = \frac{1}{6\pi} + \frac{3}{256\pi^4}`
* `\sin^2\theta_{13} = 0.0231`

### Atmospheric Angle — μτ-Symmetric Limit

sin²θ₂₃ ≈ 1/2 (octant not selected)

Originalformeln:

* `\theta_{23} = 45^\circ \quad (\mu\tau\text{-symmetric limit})`
* `\delta_{\mathrm{CP}} = \tfrac{4\pi}{3} = 240^\circ`

### Mass Ordering & Majorana Branch

Normal ordering, small m_ββ

Originalformeln:

* `\text{normal ordering preferred}`
* `\Sigma m_\nu \gtrsim 0.0586\,\mathrm{eV}\ (\text{NO floor})`
* `J_{\mathrm{PMNS}} = -0.0297`
* `\delta_{\mathrm{PMNS}} = \delta_{\mathrm{CKM}}^{\mathrm{lead}} + \pi = 240^\circ\ (\text{Galois-locked, v320})`

### Leptonic CP Phase — Galois-Locked to the Quark Phase

δ_PMNS = 240° (band 240° ± ~9°)

Originalformeln:

* `\rho = \zeta_6,\quad \delta_{\mathrm{CKM}}^{\mathrm{lead}} = \arg(\rho) = \tfrac{\pi}{3} = 60^\circ`
* `\delta_{\mathrm{PMNS}} = \arg(\rho^4) = |\mu_4|\cdot\delta_{\mathrm{CKM}}^{\mathrm{lead}} = \tfrac{4\pi}{3} = 240^\circ`
* `\rho^4 = -\rho \;\Rightarrow\; \delta_{\mathrm{PMNS}} = \delta_{\mathrm{CKM}}^{\mathrm{lead}} + \pi`

### Strong CP — Neutron-EDM Null

θ_eff = 0 (structural null)

Originalformeln:

* `\arg\det M_u = \arg\det M_d = 0`
* `\theta_{\mathrm{eff}} = 0`

### Proton/Electron Ratio — Not a Compiler Power

m_p/m_e = 1836.15 (explicitly not claimed)

Originalformeln:

* `\frac{m_p}{m_e} = \frac{\text{QCD confinement scale}}{\text{EW electron Yukawa}}`
* `1/(\varphi_0)^2 = 353.7, \quad 1/(\varphi_0)^3 = 6651 \;\text{bracket}\; 1836`

### Scalar Tilt — R² Attractor

n_s = 1 − 2/N★ ∈ [0.960, 0.967] (frozen band)

Originalformeln:

* `n_s = 1 - \tfrac{2}{N_\star}, \qquad N_\star \in [50, 60]\ \text{(frozen band)}`
* `N_\star^{\mathrm{reheating}} = 51.4 \ \Rightarrow\ n_s = 0.9611 \ \text{[P, conditional]}`

### Tensor-to-Scalar Ratio — R² Branch

r = 12/N★² ∈ [0.0033, 0.0048] (frozen band)

Originalformeln:

* `r = \tfrac{12}{N_\star^2} \in [0.0033,\,0.0048], \qquad N_\star \in [50, 60]`
* `N_\star^{\mathrm{reheating}} = 51.4 \ \Rightarrow\ r = 0.0045 \ \text{[P, conditional]}`
* `\text{current bound } r < 0.036\ (\text{BICEP/Keck BK18})`

### Scalar Amplitude — Parameter-Free

A_s = N★² c₃⁷/(24π²) ≈ 2.0×10⁻⁹

Originalformeln:

* `A_s = \frac{N_\star^2}{24\pi^2}\,c_3^7 \approx 2.0\times 10^{-9}`
* `\text{Planck } \simeq 2.1\times 10^{-9}`

### Spectral Running — R² Consistency Relation

α_s = −2/N★² = −r/6 ∈ [−8.0, −5.6]×10⁻⁴ (LO band)

Originalformeln:

* `\alpha_s = \frac{dn_s}{d\ln k} = -\tfrac{2}{N_\star^2} = -\tfrac{r}{6}, \qquad \beta_s = -\tfrac{4}{N_\star^3} \ \text{(leading order)}`
* `\text{exact slow roll: } \alpha_s(51.4) = -7.09\times 10^{-4},\ \beta_s(51.4) = -2.70\times 10^{-5}`

### μ-Distortion — A_s/N★ Branch Discriminator

μ ∈ [1.5, 2.3]×10⁻⁸ (band); 1.6×10⁻⁸ sharp / 2.0×10⁻⁸ profiled

Originalformeln:

* `\mu \approx 2.2 \int P_\zeta(k)\,W_\mu(k)\,d\ln k \ \ (\text{Chluba window, calibrated on the } \Lambda\text{CDM anchor})`
* `\mu(51.4) = 1.6\times 10^{-8},\ \mu(56.1) = 2.0\times 10^{-8},\ \Delta\mu = 3\times 10^{-9}`

### Scalaron Mass — Seam Power

M = c₃^(7/2) M̄ = 3.06×10¹³ GeV

Originalformeln:

* `\frac{M_{\mathrm{scal}}^2}{\bar M_{\mathrm{Pl}}^2} = c_3^{\,\Omega_{\mathrm{adm}} - 10 b_1} = c_3^7`
* `M_{\mathrm{scal}} = 3.06\times 10^{13}\,\text{GeV}`

### Baryon Density — One-Engine Readout

Ω_b = (4π − 1)β_rad = 0.04894

Originalformeln:

* `\Omega_b = (4\pi - 1)\,\beta_{\mathrm{rad}} = 0.04894`
* `\Omega_b h^2 = 0.0222`

### Baryon Asymmetry — Downstream Readout

η_B = 6.1×10⁻¹⁰

Originalformeln:

* `\Omega_b h^2 = 0.0222`
* `\eta_B = 273.9\times 10^{-10}\,\Omega_b h^2 = 6.09\times 10^{-10}`

### H₀ vs Λ — One Exponential Engine

v_EW ∼ e^(−α⁻¹/5), Λ ∼ e^(−2α⁻¹), H₀ ∼ √Λ

Originalformeln:

* `A_{\mathrm{EW}} : A_H : A_\Lambda = 1 : 5 : 10`
* `\frac{\rho_\Lambda}{\bar M_{\mathrm{Pl}}^4} = \frac{3}{4\pi^2}\,e^{-2\alpha^{-1}}`

### No Second Light Higgs Doublet

exactly one seam-even light doublet

Originalformeln:

* `10\,b_1 = 41 = \textstyle\sum_{f,j}L_{f,j} + N_\Phi`
* `N_\Phi = g_{\mathrm{car}} - |\mu_4| = 1`

### Higgs Quartic — Near-Criticality from the Free Seam

λ(M̄_Pl) = 0 and β_λ(M̄_Pl) = 0 (double criticality); m_H band 129–134 GeV

Originalformeln:

* `\lambda(M_{\mathrm{seam}}) = 0, \qquad \beta_\lambda(M_{\mathrm{seam}}) = 0 \ \text{(free chiral } c=8 \text{ fixed point)}`
* `\text{measured } (m_H, m_t) \Rightarrow \lambda(\bar M_{\mathrm{Pl}}) = 0.0024,\ \beta_\lambda \approx 0 \ \text{(2-loop)}`
* `\lambda = \beta_\lambda = 0 \ \text{at } \bar M_{\mathrm{Pl}} \Rightarrow m_H = 133.5\,\mathrm{GeV}\ (\text{band } 129\text{–}134)`

### Cosmic Birefringence — Determinant Line

β_rad = φ₀/(4π) = 0.2424°

Originalformeln:

* `\beta_{\mathrm{rad}} = \frac{\varphi_0}{4\pi} = 0.2424^\circ`
* `\text{ACT DR6: } 0.215^\circ \pm 0.074^\circ\ (0.4\sigma)`

### Axion Dark Matter — Candidate Fixed

m_a ≈ 23.8 µeV, f_a = M_scal/128, g_aγγ coefficient −4c₃

Originalformeln:

* `\theta_i = \pi\,N_{\mathrm{fam}}/g_{\mathrm{car}} = 3\pi/5 = 108^\circ \;\text{(robust spine branch)}`
* `\theta_i = (g_{\mathrm{car}}-2)\pi/g_{\mathrm{car}} = \text{regular pentagon interior angle},\ \cos\theta_i = -1/(2\varphi)`
* `f_a = \frac{M_{\mathrm{scal}}}{2\dim S^+|\mu_4|} = \frac{M_{\mathrm{scal}}}{128}, \quad m_a \approx 23.8\,\mu\text{eV}`
* `g_{a\gamma\gamma} = -4c_3 = -\tfrac{1}{2\pi}, \qquad y^2 = 16c_3^2 = \tfrac{1}{4\pi^2} \approx 0.0253`

### Rare Kaons K → πνν̄ — a live falsification channel

BR(K⁺) = 9.45×10⁻¹¹, BR(K_L) = 3.33×10⁻¹¹

Originalformeln:

* `s_{12}=\lambda_C,\ s_{23}=\tfrac{\varphi_0}{1+\lambda_C},\ s_{13}=\tfrac{\lambda_C^3}{3},\ \delta_{\mathrm{CKM}}=\tfrac{\pi}{3}+3\lambda_C^2`
* `(\bar\rho,\bar\eta)=(0.1374,\,0.3509)\ \Rightarrow\ \lambda_t=V_{ts}^*V_{td}`
* `\mathrm{BR}(K_L)/\mathrm{BR}(K^+)=0.352\ll4.3\ (\text{Grossman–Nir})`

### EHT achromatic polarization intercept

β_BH ∝ 16c₃⁴ · Q_e Q_m / r² (achromatic, 1/r², sign-flipping)

Originalformeln:

* `16\,c_3^4 = \tfrac{1}{256\pi^4} = \tfrac{\delta_{\mathrm{top}}}{3},\quad \delta_{\mathrm{top}}=48c_3^4`
* `\chi_0^{\mathrm{res}} = \chi_0^{\mathrm{obs}} - \chi_0^{\mathrm{GRMHD}}\ (\text{3 nulls})`

### BH HFQPO Third Tooth — the ×1.5 Ladder Search, Now Run: a Well-Powered Null

third tooth at ν₃ = 1.5 ν_u (661.5 / 414 / 252 / 363 Hz); integer harmonics forbidden

Originalformeln:

* `\mathrm{rate}(n) = -6\ln\bigl(1 - \tfrac{n}{N_{\mathrm{fam}}}\bigr),\ N_{\mathrm{fam}} = 3 \Rightarrow \text{consecutive step } \tfrac{3}{2}\ \text{exact}`
* `\nu_3 = \tfrac{3}{2}\nu_u; \quad \text{geometric teeth provably disjoint from integer harmonics } (\Delta \ge \nu_u/6 \ge 26\,\mathrm{Hz})`

## Bereits ausgewerteter gemeinsamer Zusammenhang

Auf dem angegebenen führenden Inflationsast gilt exakt r=3(1−ns)²,alpha_s=−r/6 und As*r=c3^7/(2pi²). Bei festem c3 liegen diese vier Ausgaben auf einer Kurve des gemeinsamen externen N. Statistische Unabhängigkeit von Messungen, Signifikanzen und die ursprüngliche Herkunft sämtlicher Formelannahmen bleiben gesondert zu prüfen. Die früheren R046 bisR048 Korrekturen am Gravitationsconsumer gelten weiter.

Für die20 verschiedenen bereits zugeordneten Claim IDs wurden die vorhandenen Atlas Eingabeannotationensätze abgerufen und getrennt als ungeprüfte Navigation gesichert. Drei Karten haben in dieser Websitezuordnung keine Claim ID. Die Abfrage und ihre automatischen Annotationen sind keine neue Originalquellenprüfung dieser20 Claims. Keine Gesamtzahl unabhängiger physischer Annahmen wird daraus abgeleitet.

Quelle:website/lib/predictions.ts, SHA256 ff0e50900ca86cd104e43c607dc0a917ed7763bdb1e81ddfb3046d027c1e42a7. Eingefrorenes Register:verification/predictions_frozen.json, SHA256 6ab07c898a7dac43df4762f404d528c19ad1306ea8abe91479111281b0df1332.
