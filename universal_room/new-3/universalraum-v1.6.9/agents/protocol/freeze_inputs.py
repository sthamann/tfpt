"""Freeze only the source inputs of this bounded v1.6.9 protocol strand."""
from hashlib import sha256
from pathlib import Path
import json
import shutil

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
BASE = REPO / "experiments/theory-contracts/universalraum-common-process-20260915/agents"
SOURCES = {
    "spinor_tensors.npz": BASE / "causal/sources/spinor_tensors.npz",
    "v168_common3.py": BASE / "causal/verify_common3.py",
    "v168_common3.json": BASE / "causal/common3.json",
    "v168_common3.md": BASE / "causal/ADDENDUM_COMMON3.md",
    "v168_causal.md": BASE / "causal/REPORT.md",
    "v168_mechanism.md": BASE / "mechanism/REPORT.md",
    "operations_commutant.py": BASE / "mechanism/inputs/operations_commutant.py",
    "native_common.py": BASE / "mechanism/inputs/native_common.py",
}


def main():
    dest = HERE / "inputs"
    dest.mkdir(exist_ok=True)
    manifest = {}
    for name, original in SOURCES.items():
        data = original.read_bytes()
        target = dest / name
        if target.exists() and target.read_bytes() != data:
            raise RuntimeError("refuse to change existing frozen input " + name)
        if not target.exists():
            shutil.copyfile(original, target)
        manifest[name] = {"source": str(original.relative_to(REPO)), "bytes": len(data),
                          "sha256": sha256(data).hexdigest()}
    (HERE / "inputs_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "FROZEN", "inputs": len(manifest)}, sort_keys=True))


if __name__ == "__main__":
    main()
