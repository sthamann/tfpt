/-
  CIRoot — GitHub Actions / 16 GB build target for TfptCarrier.
  =============================================================

  Import set = the imports of `TfptCarrier.lean` minus exactly
  `TfptCarrier.WallCertifiedHead` and `TfptCarrier.WallLadderAudit`.

  Those two modules pull in the generated `WallLadder/RungKz*`
  kernel-`decide` certificates. Each rung is documented to need
  21–360 GB and to fail at the lakefile's 12 GB ceiling by design;
  they are built off-CI by `scripts/build_wall_ladder.sh`, and the
  reference-machine full audit lives in `AUDIT_TRANSCRIPT.txt`.

  Kept here, and safe on a 16 GB runner:

    * every non-wall module in the library;
    * `WallLadderChecker` and `WallCofinalComposition` (no rung
      imports; the checker is integer/`decide`-free at this layer);
    * `AxiomCheck`, `AuditCheck`, `AuditContract` (wall `#print axioms`
      / `#check` / `example` lines live in `WallLadderAudit`).

  `scripts/audit.sh --core` builds this module. Check (8) of that
  script asserts the import-set identity so the two roots cannot
  drift. NO RH claim; no proof content lives in this file.
-/

import TfptCarrier.Polarization
import TfptCarrier.InvolutionProjectors
import TfptCarrier.CalderonInterface
import TfptCarrier.CalderonProjector
import TfptCarrier.BoundaryPolarization
import TfptCarrier.MathlibBridge
import TfptCarrier.LatticeRigidityGeneral
import TfptCarrier.Rigidity
import TfptCarrier.OrientedDeterminantCarrier
import TfptCarrier.TraceProjection
import TfptCarrier.DeterminantCharacter
import TfptCarrier.HiggsIndexShadow
import TfptCarrier.HiggsTopForm
import TfptCarrier.HiggsSchemeCohomologyShadow
import TfptCarrier.YukawaRank
import TfptCarrier.YukawaTopForm
import TfptCarrier.YukawaPrimitive
import TfptCarrier.YukawaTrilinearForm
import TfptCarrier.YukawaStageDExistence
import TfptCarrier.BoundaryYukawaKernelInterface
import TfptCarrier.SeamWindingInterface
import TfptCarrier.CarrierData
import TfptCarrier.Hypercharge
import TfptCarrier.GlueUniqueness
import TfptCarrier.SeamDeckClosure
import TfptCarrier.SeamEquivChain
import TfptCarrier.SeamScalingLimit
import TfptCarrier.SeamResidualAxiom
import TfptCarrier.SeamStandardPair
import TfptCarrier.SeamApplicabilityLedger
import TfptCarrier.WallReducedMinuscule
import TfptCarrier.WallRegularSemisimple
import TfptCarrier.SeamRigidityForcing
import TfptCarrier.SeamEdgeChern
import TfptCarrier.BWKeystone
import TfptCarrier.CartanDeterminants
import TfptCarrier.KronheimerMarks
import TfptCarrier.Mu4Commutation
import TfptCarrier.MobiusUniformisation
import TfptCarrier.CohomologyGrading
import TfptCarrier.AnchorLadder
import TfptCarrier.PascalLadder
import TfptCarrier.SpectralGapAttractor
import TfptCarrier.CoxeterPrime2
import TfptCarrier.ParityWeightLaws
import TfptCarrier.CoverEmbedding
import TfptCarrier.LorentzCongruence
import TfptCarrier.G31Orders
import TfptCarrier.G31WordOrders
import TfptCarrier.HammingCode
import TfptCarrier.SquareParity
import TfptCarrier.GaussianCodeBridge
import TfptCarrier.OrbitPacket
import TfptCarrier.QuarticHalf
import TfptCarrier.WatataniIndexFour
import TfptCarrier.ProjectiveHamming
import TfptCarrier.GramCompactness
import TfptCarrier.PositiveDescentMaster
import TfptCarrier.ArfSpinorCompiler
import TfptCarrier.FlavorFeedback
import TfptCarrier.GaussianShells
import TfptCarrier.Sanity
import TfptCarrier.AxiomCheck
import TfptCarrier.AuditCheck
import TfptCarrier.AuditContract
