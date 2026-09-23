# Narrow source excerpts

The line ranges and SHA-256 values for the complete source files are recorded
in `../source_manifest.json`. The copied text below is evidence only; it does
not add a new ledger claim.

## v2.7, original lines 2942–2978

Source: `archive/TFPT_2.7-final.md` in the manifest.

```text
9     Axion Cosmology and Dark Matter
9.1   Two-Field Structure: Topological vs. QCD Axion
The TFPT axion sector is split into two distinct fields to avoid an internal
contradiction (a single µeV axion cannot remain quasi-static over Hubble times):
                          atop != aQCD,
              L contains c3 atop F F-tilde + aQCD/fa GG-tilde.

Two-Field Axion Structure
  * atop (topological field): ultralight, quasi-static background responsible
    for birefringence; excursion Delta atop = n phi0; time scale cosmological.
  * aQCD (QCD axion): oscillating field forming dark matter with fa fixed by the
    PQ block; time scale tau approximately ma^-1; haloscope observable.
Minimal mixing: the discrete/vanishing mixing limit is adopted as the minimal
model, so no new continuous parameters are introduced.

Why two fields? A single µeV axion oscillates rapidly and averages
birefringence to zero over CMB propagation time. A distinct ultralight atop is
therefore required.
```

## v2.8, original lines 3166–3193

Source: `archive/TFPT_2.8-final.md` in the manifest.

```text
9      Axion Cosmology and Dark Matter
9.1    Two-Field Structure: Topological vs. QCD Axion
The TFPT axion sector is split into two distinct fields to avoid an internal
contradiction (a single µeV axion cannot remain quasi-static over Hubble times):
                           atop != aQCD,
              L contains c3 atop F F-tilde + aQCD/fa GG-tilde.

  * atop (topological field): ultralight, quasi-static background responsible
    for birefringence; cosmological time scale; CMB polarization rotation.
  * aQCD (QCD axion): oscillating field forming dark matter; axion haloscope
    signal on the fast ma^-1 time scale.
Minimal mixing: the discrete/vanishing mixing limit is adopted as the minimal
model, so no new continuous parameters are introduced.

Why two fields? A single µeV axion oscillates rapidly and averages
birefringence to zero over CMB propagation time. A distinct ultralight atop is
therefore required.
```

## Current scoped result

The current report `HERLEITUNG.md` (manifest lines 77–125) gives, under
`K > 0` and a QCD rank-one term, the exact condition

```text
exists v: N^T v = 0 and c^T v != 0
iff c is not in span(N),

g_L^2 = c^T K^-1 c - (c^T K^-1 N)^2/(N^T K^-1 N).
```

Its lines 127–148 show that an explicitly moving minimum contains the source
term `-Lambda4*phi0*sin(theta-phi0*s)*dot(s)`. The source must derive this
driver and its opposite energy flow in a closed realization.
