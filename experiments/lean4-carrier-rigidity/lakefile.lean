import Lake
open Lake DSL

/--
Per-`lean`-process memory ceiling in MB, handed to Lean as `-M`.

Lake may run independent targets in parallel. Keep a per-process ceiling
for the physical carrier/Standard Model formalization. RH/prime wall
certificates and their serial builder are maintained in prime-front.

Override per invocation, e.g. `lake build -K leanMemoryMb=49152 <target>`,
but only for a build that is known to be serialised.
-/
def leanMemoryMb : String :=
  (get_config? leanMemoryMb).getD "12288"

package «TfptCarrier» where
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩,
    ⟨`autoImplicit, false⟩
  ]
  -- `-M` bounds the elaborator/kernel allocation budget without changing the
  -- emitted olean, so it belongs in `weakLeanArgs`: raising or lowering the
  -- ceiling must not invalidate build traces and force a Mathlib-wide rebuild.
  weakLeanArgs := #["-M", leanMemoryMb]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.29.1"

@[default_target]
lean_lib «TfptCarrier» where
