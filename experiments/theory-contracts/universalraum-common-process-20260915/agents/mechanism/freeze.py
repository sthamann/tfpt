"""Freeze the exact, read-only source surface used by the mechanism audit."""
from pathlib import Path
from hashlib import sha256
import json
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCES = {
    "spinor_tensors.npz": "experiments/theory-contracts/universalraum-singlet-observable-20260915/sources/spinor_tensors.npz",
    "native_source.py": "experiments/theory-contracts/universalraum-singlet-observable-20260915/sources/native_source.py",
    "native_common.py": "experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py",
    "operations_commutant.py": "experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/operations_commutant.py",
    "source_clock.py": "experiments/tfpt-discovery/seam_state_derivation_probe.py",
    "clock_adapter.py": "experiments/theory-contracts/compiler-involution-types/checker.py",
    "context_instrument.py": "experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py",
    "relational_kernel.py": "experiments/theory-contracts/compiler-kernel-foundation-20260914/relational_kernel.py",
    "baseline_big_picture.md": "experiments/theory-contracts/universalraum-singlet-observable-20260915/BIG_PICTURE.md",
    "baseline_results.md": "experiments/theory-contracts/universalraum-singlet-observable-20260915/RESULTS.md",
    "baseline_verify_big_picture.py": "experiments/theory-contracts/universalraum-singlet-observable-20260915/verify_big_picture.py",
    "additional_research_paper.md": "/Users/stefanhamann/Documents/TFPT_Universalraum_Forschungspaper_2026-09-15/TFPT_Universalraum_Forschungspaper_2026-09-15.md",
}


def main():
    target = HERE / "inputs"
    target.mkdir(exist_ok=True)
    records = {}
    for name, source in SOURCES.items():
        original, frozen = ROOT / source, target / name
        data = original.read_bytes()
        if frozen.exists() and frozen.read_bytes() != data:
            raise RuntimeError("Refusing to overwrite a different frozen input: " + name)
        if not frozen.exists():
            shutil.copyfile(original, frozen)
        records[name] = {"source": source, "sha256": sha256(data).hexdigest(), "bytes": len(data)}
    encoded = json.dumps(records, indent=2, sort_keys=True) + "\n"
    manifest = HERE / "inputs_manifest.json"
    if manifest.exists():
        previous = json.loads(manifest.read_text())
        if any(records.get(name) != value for name, value in previous.items()):
            raise RuntimeError("Refusing to change an existing manifest entry")
    manifest.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
