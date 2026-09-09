"""Reuse the frozen ten-suite runner, append the new charged-field suite."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / "microscopic-fourpoint-limit/run_verification.py"
PIN = "5b9f441d8c92d8dd61434f1dac26d61eff1487356b77ad0473dc83b0d2a57dd1"


def main():
    if hashlib.sha256(PREVIOUS.read_bytes()).hexdigest() != PIN:
        raise RuntimeError("frozen regression runner changed")
    spec = importlib.util.spec_from_file_location("charged_regression_runner", PREVIOUS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.SUITES = module.SUITES + (HERE.name,)
    result = module.main()
    # The reused runner owns --output parsing and preserves full transcripts.
    output = Path(sys.argv[sys.argv.index("--output") + 1])
    record = json.loads(output.read_text())
    record["runner_source_sha256"] = PIN
    record["new_artifact_hashes"] = {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in ("checker.py", "test_checker.py", "README.md", "diagnostics.json", "run_verification.py")
    }
    record["independent_mathematical_review"] = False
    record["scope"] = "Written one-source charged CAR proof with regressions; E8 lambda and T1-T8 remain open."
    output.write_text(json.dumps(record, indent=2) + "\n")
    return result


if __name__ == "__main__":
    sys.exit(main())
