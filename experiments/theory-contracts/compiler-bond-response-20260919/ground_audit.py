"""Independent two-source bond-vacuum audit.

The reconstruction never forms the 3,686,400 dimensional matrix.  It first
Fourier decomposes each 240-root source under the central quarter rotation,
then applies the two local 960 dimensional operators matrix-free in each of
the sixteen 230,400 dimensional charge blocks.

There are two evidence levels in the output:

* ``exact_input_checks`` use Gaussian-integer identities and pinned hashes;
* ``numerical_full_space_audit`` is Hermitian Lanczos with explicit residuals.

The latter is deliberately not advertised as an exact spectral certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh


HERE = Path(__file__).resolve().parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE_REL = Path(
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
SOURCE = REPO / SOURCE_REL
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
LOCAL_CERT_REL = Path(
    "experiments/theory-contracts/"
    "compiler-root-source-backreaction-20260919/spectrum_certificate.json"
)
LOCAL_CERT = REPO / LOCAL_CERT_REL
LOCAL_CERT_SHA256 = "d1e907a341bef81f255ab553e3c6c1db672500ebf6e37411e3a1f7062f5d40d8"
LOCAL_MANIFEST_REL = Path(
    "experiments/theory-contracts/"
    "compiler-root-source-backreaction-20260919/artifact_manifest.json"
)
LOCAL_MANIFEST = REPO / LOCAL_MANIFEST_REL
LOCAL_MANIFEST_SHA256 = "ba2f5bdebce5ef3d59e8e6d4788fc4f784ce7139316e14cb4bd10d232af057e0"


def require(condition: bool, label: str, checks: Counter[str]) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def gaussian_key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    return tuple(
        (int(round(value.real)), int(round(value.imag))) for value in vector
    )


def grouped(values: np.ndarray, tolerance: float = 2e-9) -> list[tuple[float, int]]:
    answer: list[list[float | int]] = []
    for value in np.sort(np.real_if_close(values).real):
        if not answer or abs(value - float(answer[-1][0])) > tolerance:
            answer.append([float(value), 1])
        else:
            answer[-1][1] = int(answer[-1][1]) + 1
    return [(float(value), int(multiplicity)) for value, multiplicity in answer]


EXPECTED_LOCAL_K = {
    0: [(Fraction(-2, 5), 10), (Fraction(-1, 5), 40), (Fraction(0), 600),
        (Fraction(1, 5), 240), (Fraction(2, 5), 70)],
    1: [(Fraction(-3, 10), 20), (Fraction(-1, 6), 36),
        (Fraction(-1, 10), 140), (Fraction(0), 320),
        (Fraction(1, 10), 100), (Fraction(1, 6), 252),
        (Fraction(3, 10), 80), (Fraction(1, 2), 12)],
    2: [(Fraction(-1, 5), 45), (Fraction(-1, 15), 225),
        (Fraction(0), 16), (Fraction(1, 15), 405),
        (Fraction(1, 5), 240), (Fraction(1, 3), 18),
        (Fraction(3, 5), 10), (Fraction(1), 1)],
    3: [(Fraction(-1, 2), 4), (Fraction(-3, 10), 20),
        (Fraction(-1, 6), 108), (Fraction(0), 320),
        (Fraction(1, 10), 260), (Fraction(1, 6), 144),
        (Fraction(3, 10), 100), (Fraction(1, 2), 4)],
}


def build_charge_blocks(rays: list[np.ndarray], checks: Counter[str]) -> list[np.ndarray]:
    root_index = {
        gaussian_key((1j ** phase) * ray): (ray_index, phase)
        for ray_index, ray in enumerate(rays)
        for phase in range(4)
    }
    require(len(root_index) == 240, "sixty rays lift to 240 roots", checks)
    blocks = [np.zeros((960, 960), dtype=np.complex128) for _ in range(4)]
    identity4 = np.eye(4, dtype=np.complex128)
    for ray in rays:
        reflection = identity4 - np.outer(ray, ray.conj()) / 2
        require(np.array_equal(reflection @ reflection, identity4),
                "reflection is an exact involution", checks)
        require(np.array_equal(reflection, reflection.conj().T),
                "reflection is exactly Hermitian", checks)
        permutations = [np.zeros((60, 60), dtype=np.complex128) for _ in range(4)]
        for old, old_ray in enumerate(rays):
            new, phase = root_index[gaussian_key(reflection @ old_ray)]
            for charge in range(4):
                # Convention |ell;q> = 1/2 sum_p i^(pq)|i^p z_ell>.
                permutations[charge][new, old] = (1j) ** (-charge * phase)
        matter = np.kron(reflection, reflection)
        for charge in range(4):
            blocks[charge] += np.kron(permutations[charge], matter) / 60
    for charge, block in enumerate(blocks):
        require(np.array_equal(block, block.conj().T),
                f"charge-{charge} local mean is exactly Hermitian", checks)
    return blocks


def local_spectrum_audit(blocks: list[np.ndarray], checks: Counter[str]) -> dict[str, object]:
    output: dict[str, object] = {}
    for charge, block in enumerate(blocks):
        values = np.linalg.eigvalsh(block)
        observed = grouped(values)
        expected = EXPECTED_LOCAL_K[charge]
        require(len(observed) == len(expected),
                f"charge-{charge} local number of spectral bands", checks)
        require(all(abs(value - float(target)) < 3e-10 and mult == target_mult
                    for (value, mult), (target, target_mult) in zip(observed, expected)),
                f"charge-{charge} local spectrum matches rational target", checks)
        output[str(charge)] = [
            {"K": str(target), "L": str(1 - target), "multiplicity": multiplicity}
            for target, multiplicity in expected
        ]
    return output


def sector_operator(left_mean: np.ndarray, right_mean: np.ndarray) -> LinearOperator:
    dimension = 60 * 60 * 4 * 4 * 4

    def multiply(vector: np.ndarray) -> np.ndarray:
        tensor = vector.reshape(60, 60, 4, 4, 4)
        left_rows = tensor.transpose(0, 2, 3, 1, 4).reshape(960, 240)
        left = (left_rows - left_mean @ left_rows).reshape(60, 4, 4, 60, 4)
        left = left.transpose(0, 3, 1, 2, 4)
        right_rows = tensor.transpose(1, 3, 4, 0, 2).reshape(960, 240)
        right = (right_rows - right_mean @ right_rows).reshape(60, 4, 4, 60, 4)
        right = right.transpose(3, 0, 4, 1, 2)
        return (left + right).reshape(-1)

    return LinearOperator((dimension, dimension), matvec=multiply, dtype=np.complex128)


def lowest_sector_values(
    blocks: list[np.ndarray], checks: Counter[str]
) -> tuple[dict[str, object], list[tuple[float, int, int]]]:
    results: dict[str, object] = {}
    floors: list[tuple[float, int, int]] = []
    rng = np.random.default_rng(20260919)
    dimension = 60 * 60 * 4 * 4 * 4
    for left_charge in range(4):
        for right_charge in range(4):
            operator = sector_operator(blocks[left_charge], blocks[right_charge])
            start = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
            values, vectors = eigsh(
                operator,
                k=4,
                which="SA",
                v0=start,
                tol=2e-11,
                maxiter=600,
            )
            order = np.argsort(values)
            values = values[order]
            vectors = vectors[:, order]
            residuals = [
                float(np.linalg.norm(operator @ vectors[:, column] - values[column] * vectors[:, column]))
                for column in range(4)
            ]
            require(max(residuals) < 2e-8,
                    f"sector {left_charge}{right_charge} Ritz residual", checks)
            key = f"{left_charge},{right_charge}"
            results[key] = {
                "lowest_four": [float(value) for value in values],
                "max_residual": max(residuals),
                "dimension": dimension,
            }
            floors.append((float(values[0]), left_charge, right_charge))
    floors.sort()
    require(all(abs(item[0] - 0.5) < 2e-10 for item in floors[:2]) and
            {item[1:] for item in floors[:2]} == {(1, 2), (2, 1)},
            "exactly the two mirror charge blocks have floor one half", checks)
    require(abs(floors[2][0] - 0.6) < 2e-10 and floors[2][1:] == (2, 2),
            "next charge-block floor is three fifths", checks)
    for key in ("1,2", "2,1"):
        values = results[key]["lowest_four"]
        require(abs(values[0] - 0.5) < 2e-10 and values[1] > 0.699999999,
                f"sector {key} numerical ground is simple and next level at least seven tenths",
                checks)
    return results, floors


def main(output: Path, skip_global: bool) -> None:
    checks: Counter[str] = Counter()
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned source hash", checks)
    require(hashlib.sha256(LOCAL_MANIFEST.read_bytes()).hexdigest() == LOCAL_MANIFEST_SHA256,
            "pinned prior local artifact manifest", checks)
    manifest = json.loads(LOCAL_MANIFEST.read_text())
    require(manifest["spectrum_certificate.json"] == LOCAL_CERT_SHA256,
            "prior manifest pins the exact local spectrum certificate", checks)
    local_cert_hash = hashlib.sha256(LOCAL_CERT.read_bytes()).hexdigest()
    require(local_cert_hash == LOCAL_CERT_SHA256,
            "prior exact local spectrum certificate hash", checks)
    spec = importlib.util.spec_from_file_location("bond_vacuum_source", SOURCE)
    source = importlib.util.module_from_spec(spec)
    require(spec.loader is not None, "source loader exists", checks)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    require(len(rays) == 60, "source has sixty projective rays", checks)
    blocks = build_charge_blocks(rays, checks)
    local = local_spectrum_audit(blocks, checks)

    epsilon_endpoint = Fraction(1, 65)
    schur_gap_coefficient = (
        Fraction(1, 4)
        - Fraction(31, 64) * epsilon_endpoint
        / (Fraction(1, 10) - Fraction(21, 8) * epsilon_endpoint)
    )
    require(schur_gap_coefficient == Fraction(1, 8),
            "conditional Schur gap equals epsilon over eight at endpoint one over sixty-five",
            checks)

    sector_results: dict[str, object] = {}
    floors: list[tuple[float, int, int]] = []
    if not skip_global:
        sector_results, floors = lowest_sector_values(blocks, checks)

    result = {
        "verdict": (
            "NUMERICAL_FULL_SPACE_SUPPORT_EXACT_GLOBAL_CERTIFICATE_STILL_REQUIRED"
            if not skip_global else "EXACT_LOCAL_RECONSTRUCTION_ONLY"
        ),
        "scope": (
            "Pure-permutation J=mu=0 two-source, three-matter model. "
            "No affine-current lift or physical-selection claim."
        ),
        "source": {"path": str(SOURCE_REL), "sha256": SOURCE_SHA256},
        "prior_exact_local_certificate": {
            "path": str(LOCAL_CERT_REL),
            "observed_sha256": local_cert_hash,
            "expected_sha256_in_this_audit": LOCAL_CERT_SHA256,
            "pin_matches": local_cert_hash == LOCAL_CERT_SHA256,
            "manifest_path": str(LOCAL_MANIFEST_REL),
            "manifest_sha256": LOCAL_MANIFEST_SHA256,
            "use": (
                "exact one-bond spectrum provenance only; the global two-bond "
                "Lanczos replay remains numerical"
            ),
        },
        "dimensions": {
            "full": 240 * 240 * 4 * 4 * 4,
            "charge_blocks": 16,
            "each_charge_block": 60 * 60 * 4 * 4 * 4,
            "local_charge_operator": 60 * 4 * 4,
        },
        "source_fourier_convention": (
            "|ell;s>=(1/2) sum_k i^(ks)|i^k z_ell>, source action phase i^(-s q); "
            "the two mirror states occupy sectors (2,1) and (1,2)"
        ),
        "exact_input_checks": {
            "description": (
                "Pinned source plus Gaussian-integer reflection/permutation identities. "
                "The rational local bands are reconstructed by Hermitian diagonalization, "
                "so their independent exact proof remains the pinned CRT certificate."
            ),
            "local_charge_spectra": local,
        },
        "numerical_full_space_audit": {
            "method": "matrix-free Hermitian Lanczos after exact Z4 Fourier decomposition",
            "sectors": sector_results,
            "ordered_sector_floors": [
                {"energy_over_kappa": value, "charges": [left, right]}
                for value, left, right in floors
            ],
            "observed_ground": "1/2 in sectors (1,2) and (2,1), one Ritz vector each",
            "observed_next_floor": "3/5 in sector (2,2)",
            "observed_gap": "1/10",
            "proof_status": "NUMERICAL, not an exact all-space lower-bound certificate",
        },
        "exact_lower_bounds_available_without_global_diagonalization": {
            "single_bond": "L_e >= (2/5)(I-|Omega_e><Omega_e|)",
            "overlapping_packet_cosine": "||Q_1 Q_2||=1/4",
            "unconditional_two_bond_floor": (
                "H0 >= (2/5)(2I-Q_1-Q_2) >= 3/10; this is exact but not sharp"
            ),
            "charge_sector_floor": (
                "Exact local spectra put every sector at or above 1/2 except "
                "the phase-(2,2) sector.  The missing sharp step is the "
                "barSym2 x barSym2 recoupling/complement bound in that sector."
            ),
        },
        "perturbation_decision": {
            "given_compression": (
                "P H_Esum P=(3/2)I and P V P=[[1,-1/8],[-1/8,1]] "
                "give first-order splitting mu/4 when J=mu"
            ),
            "compression_alone_would_be_insufficient": (
                "PWP alone does not prove uniqueness or gap >=mu/8; an exact "
                "off-P residual and reduced-resolvent estimate are also required"
            ),
            "now_supplied_exact_residual_identity": (
                "PBQBP below supplies that estimate conditionally on the exact H0 gap; "
                "the broader earlier chain leakage formula remains unreplayed"
            ),
            "conditional_if_H0_gap_1_over_10_is_exact": {
                "compression": "PBP=(5/2)I-sigma_x/8 for B=H_E1+H_E2+V",
                "leakage_gram": (
                    "PBQBP=(55/64)I+(3/8)sigma_x; parity values 79/64 and 31/64"
                ),
                "schur_gap_bound": (
                    "epsilon/4 - 31 epsilon^2/[64(1/10-21 epsilon/8)]"
                ),
                "consequence": (
                    "gap >= epsilon/8 for epsilon<=1/65, hence for epsilon<=1/200"
                ),
                "status": (
                    "exact conditional perturbation argument; it does not repair the missing "
                    "exact H0 full-space gap certificate"
                ),
            },
        },
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": result["verdict"], "checks": result["checks"]}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "ground_audit.json")
    parser.add_argument("--skip-global", action="store_true")
    arguments = parser.parse_args()
    main(arguments.out, arguments.skip_global)
