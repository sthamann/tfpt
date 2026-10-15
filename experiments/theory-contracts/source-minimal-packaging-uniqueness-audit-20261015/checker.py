"""Source-pin audit of the minimal-packaging uniqueness claim (no model, no finite lists).

Pins the exact original statements used in PROOF.md; every check is a string or
absence test on the archived source extracts and on the prior contracts.
"""
from pathlib import Path
import json, re

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

ROOT = Path(__file__).resolve().parents[3]
EX = ROOT / "_archive/tfpt-45/source_extracts"
bk = (EX / "01_boundary_kernel_source.tex").read_text()
lines = bk.splitlines()
flat = lambda t: " ".join(t.split())
def at(lo, hi, text):
    return text in flat("\n".join(lines[lo - 1:hi]))

require("U1_uniqueness_only_reduced_587_593", at(587, 593,
        "Uniqueness is then reduced to classification of the final minimized stratum by the one-sided boundary datum up to unitary equivalence."))
require("U1_claimed_uniqueness_646_653", at(646, 653,
        "there exists, up to unitary equivalence, a unique essentialized defect-minimal representative"))
require("U1_cites_reconstruction_theorem_678_683", at(678, 683,
        "the boundary reconstruction theorem identifies the induced one-sided datum up to unitary equivalence."))
alltex = "\n".join(p.read_text() for p in EX.glob("*.tex"))
require("U1_no_labelled_boundary_reconstruction_theorem",
        not re.search(r"\\label\{thm:[^}]*boundary[-_]reconstruction", alltex)
        and "Boundary reconstruction theorem" not in alltex)
require("U1_nearest_reconstruction_starts_from_given_Tbound_94_100", at(94, 100, "Let $\\Tbound$ be as above."))
require("U1_Tbound_contains_B_Sigma_66_80", at(66, 80, "\\Tbound:=(\\mathcal A_+,\\mathcal H_+,D_+,J,\\Gamma,B_\\Sigma)"))
require("U2_corollary_equivalence_615_620", at(615, 620,
        "minimizing over $\\Seedop$ is equivalent to minimizing the essentialized defect filtration in"))
require("U2_functor_only_proof_architecture_516_521", at(516, 521, "\\begin{proof}[Proof architecture]"))
require("U3_OS_Hilbert_space_from_net_517_521", at(516, 521,
        "Reflection positivity and the positive-time net reconstruct the one-sided OS Hilbert space on the collar."))
require("U3_objects_one_sided_tuple_631_643", at(630, 643, "\\mathcal B=(\\mathcal A_+,\\mathcal H_+,D_+,J,\\Gamma)"))
require("U3_dirac_type_collar_631_643", at(630, 643, "$D_+$ is an elliptic Dirac-type operator on a one-sided collar"))
require("U3_commutative_centre_manifold_66_80", at(66, 80, "$Z(\\mathcal A_+)$ is spectrally regular and its Gelfand spectrum is a smooth compact oriented manifold with boundary $M_+$"))
require("U3_reference_sector_declared_640", at(636, 643, "the relative action with respect to the declared reference sector is finite"))
require("U3_functor_output_has_no_net_time_state_509_512", at(505, 512,
        "\\mathfrak T_{\\partial}(\\mathfrak S)=(\\mathcal A_+,\\mathcal H_+,D_+,J,\\Gamma,B_\\Sigma)."))
require("U3_defects_545_558", at(545, 558, "d_0(B)&:=|\\SF(U_\\Sigma)|,") and at(545, 558, "d_3(B)&:=h_\\Sigma^{\\red}(B).")
        and at(545, 558, "d_1(B)&:=\\rankess H_{\\mathrm{prim}}^{\\mathrm{fin}},"))
for w in ("DHR", "superselection", "orbifold", "twisted sector"):
    require(f"U3_no_{w.replace(' ', '_')}_in_boundary_kernel", w.lower() not in bk.lower())
TC = ROOT / "experiments/theory-contracts"
sel = (TC / "source-three-route-closure-20260922/SELECTION.md").read_text()
require("P1_prior_defects_no_uniqueness", "liefern für sich keinen Eindeutigkeitsbeweis für einen vollständigen" in sel)
require("P1_prior_conditional_K_G", "\\text{P1/P2/Clocks}\\stackrel{?}{\\longrightarrow}" in sel)
bls = (TC / "source-boundary-lift-selection-20260922/PROOF.md").read_text()
require("P2_prior_zero_order_not_fixed", "ihre Terme nullter Ordnung sind damit noch nicht eindeutig" in bls)
require("P2_prior_domain_counterexample", "Dieselbe elliptische Klasse allein bedeutet nicht dieselbe konkrete Operatordomäne" in bls)
require("P2_prior_kato_rellich_repair", "**Reparatur für den hier benötigten Anschluss.**" in bls)

res = {"contract": "source-minimal-packaging-uniqueness-audit-20261015", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(res, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
