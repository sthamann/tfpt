/- TFPT scoped ParityWeightLaws: original v590 sheet involution/group identities.
Prime-window sections are maintained in Prime Front; theorem names and proofs below unchanged. -/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

namespace TFPT.Carrier.ParityWeightLaws
/-! ### 4. The sheet involution (v590) -/

/-- The sheet involution selected in v590 (QGEO.INVOL.01). -/
def S0 : Matrix (Fin 3) (Fin 3) ℤ := !![1, -1, 0; 0, -1, 0; 0, 0, -1]

/-- The sheet flow `V = Q diag(0,1,1)` of the compiler `Q`. -/
def V : Matrix (Fin 3) (Fin 3) ℤ := !![0, 1, 0; 0, 2, 0; 0, 2, 1]

theorem S0_involution : S0 * S0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_three]

theorem S0_commutes_V : S0 * V = V * S0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, V, Matrix.mul_apply, Fin.sum_univ_three]

theorem S0_trace : Matrix.trace S0 = -1 := by
  simp [Matrix.trace, S0, Fin.sum_univ_three]

/-! ### 5. The involution group of v590: the concrete (ℤ/2)³ members

The integral `V`-commuting involutions found in v590 form the group
`{±1, ±A, ±B, ±S0}` with the Klein-four relation `A * B = S0`.  We
verify the two further generators and the closure relation; the
completeness of the classification (that these are ALL integral
`V`-commuting involutions) rests on the spectral-projector argument
machine-checked in `v590_involution_existence.py`.
-/

/-- The `ε = (+,+,-)` member: `+1` on the `V`-eigenspaces `{0,1}`. -/
def A : Matrix (Fin 3) (Fin 3) ℤ := !![1, -1, 0; 0, -1, 0; 0, -4, 1]

/-- The `ε = (+,-,+)` member: `+1` on the `V`-eigenspaces `{0,2}`. -/
def B : Matrix (Fin 3) (Fin 3) ℤ := !![1, 0, 0; 0, 1, 0; 0, 4, -1]

theorem A_involution : A * A = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, Matrix.mul_apply, Fin.sum_univ_three]

theorem B_involution : B * B = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, Matrix.mul_apply, Fin.sum_univ_three]

theorem A_commutes_V : A * V = V * A := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, V, Matrix.mul_apply, Fin.sum_univ_three]

theorem B_commutes_V : B * V = V * B := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [B, V, Matrix.mul_apply, Fin.sum_univ_three]

/-- The Klein-four closure: `A · B = S0` — the sheet involution is the
product of the two eigenspace-pair involutions. -/
theorem klein_closure : A * B = S0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A, B, S0, Matrix.mul_apply, Fin.sum_univ_three]

end TFPT.Carrier.ParityWeightLaws
