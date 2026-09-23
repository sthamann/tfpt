"""Freeze only the source surface used by this NON-RH composition audit."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCES = {
    "native_source.py": "experiments/theory-contracts/universalraum-singlet-observable-20260915/sources/native_source.py",
    "spinor_tensors.npz": "experiments/theory-contracts/universalraum-singlet-observable-20260915/sources/spinor_tensors.npz",
    "native_common.py": "experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py",
    "source_clock.py": "experiments/tfpt-discovery/seam_state_derivation_probe.py",
    "clock_adapter.py": "experiments/theory-contracts/compiler-involution-types/checker.py",
    "parabolic_source.py": "verification/v566_parabolic_anchor_selfcode.py",
    "ray_source.py": "verification/v783_two_qubit_clifford.py",
    "context_instrument.py": "experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py",
    "record_composition.py": "experiments/theory-contracts/compiler-origin-audit-20260913/record_composition.py",
    "relational_kernel.py": "experiments/theory-contracts/compiler-kernel-foundation-20260914/relational_kernel.py",
    "kernel_results.md": "experiments/theory-contracts/compiler-kernel-foundation-20260914/RESULTS.md",
    "fugen_checker.py": "experiments/theory-contracts/universalraum-fugen-20260914/checker.py",
    "architecture_readme.md": "experiments/theory-contracts/universalraum-v14-F2-architektur-20260914/README.md",
    "architecture_checker.py": "experiments/theory-contracts/universalraum-v14-F2-architektur-20260914/checker.py",
    "bell_composition.py": "experiments/theory-contracts/systematic-origin-audit-20260912/interaction/composition.py",
    "clock_gluing.py": "experiments/theory-contracts/universalraum-keyB-clock-gluing-20260915/clock_gluing.py",
}


def main():
    target = HERE / "inputs"
    target.mkdir(exist_ok=True)
    records = {}
    for name, source in SOURCES.items():
        original, frozen = ROOT / source, target / name
        data = original.read_bytes()
        if frozen.exists() and frozen.read_bytes() != data:
            raise RuntimeError("Refusing to overwrite a changed frozen input: " + name)
        if not frozen.exists():
            shutil.copyfile(original, frozen)
        records[name] = {"source": source, "sha256": sha256(data).hexdigest(), "bytes": len(data)}
    manifest = HERE / "inputs_manifest.json"
    if manifest.exists() and json.loads(manifest.read_text()) != records:
        raise RuntimeError("Refusing to alter an existing source manifest")
    manifest.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"frozen_inputs": len(records)}, sort_keys=True))


if __name__ == "__main__":
    main()
