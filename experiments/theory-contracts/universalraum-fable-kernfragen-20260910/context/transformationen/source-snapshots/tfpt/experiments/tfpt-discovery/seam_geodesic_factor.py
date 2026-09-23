#!/usr/bin/env python3
"""Runnable factorisation on the TFPT modular-seam lane.

The N-dependent geometry identified by ``seam_geodesic_infrastructure_probe``
is the reduction cycle of ``sqrt(N)``.  Its useful classical shortcut is
SQUFOF: find a square form in the forward cycle, take its inverse square root,
and follow the new cycle to a symmetry point.  This module turns that probe
into a usable factorisation program:

* deterministic Miller--Rabin for every factor below 2**64;
* multi-multiplier SQUFOF for the geodesic split;
* recursive splitting, including signs, powers, and repeated factors;
* deterministic-seeded Pollard--Brent fallback when SQUFOF is out of range or
  exhausts its budget;
* exact product verification and optional machine-readable traces.

This is a complete practical classical solver, not a new polynomial-time
factoring claim.  E8 supplies fixed TFPT structure but no N-dependent oracle;
the actual N-dependent engine here is the modular-surface geodesic.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass
from math import gcd, isqrt
from typing import Iterable, Sequence


# The standard multiplier family used by mature SQUFOF implementations.  A
# multiplier changes the principal cycle without changing the sought factor:
# the final gcd is always taken with the original N.
SQUFOF_MULTIPLIERS: tuple[int, ...] = (
    1,
    3,
    5,
    7,
    11,
    3 * 5,
    3 * 7,
    3 * 11,
    5 * 7,
    5 * 11,
    7 * 11,
    3 * 5 * 7,
    3 * 5 * 11,
    3 * 7 * 11,
    5 * 7 * 11,
    3 * 5 * 7 * 11,
)

SMALL_PRIMES: tuple[int, ...] = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
)

# This seven-base set is deterministic for unsigned 64-bit integers.
MR_BASES_64: tuple[int, ...] = (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022)
MR_BASES_LARGE: tuple[int, ...] = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)


class FactorizationFailure(RuntimeError):
    """Raised when the selected bounded methods cannot split a composite."""


@dataclass(frozen=True)
class SplitEvent:
    source: int
    factor: int
    cofactor: int
    method: str
    iterations: int
    multiplier: int = 1
    forward_iterations: int = 0
    reverse_iterations: int = 0
    square_root_q: int | None = None

    @property
    def discriminant(self) -> int | None:
        if self.method != "squfof-geodesic":
            return None
        return 4 * self.multiplier * self.source

    def to_dict(self) -> dict[str, int | str | None]:
        row = asdict(self)
        row["discriminant"] = self.discriminant
        return row


@dataclass(frozen=True)
class FactorizationResult:
    input_value: int
    sign: int
    factors: tuple[int, ...]
    events: tuple[SplitEvent, ...]
    elapsed_seconds: float
    verified: bool
    primality_status: str

    @property
    def factor_powers(self) -> dict[int, int]:
        return dict(sorted(Counter(self.factors).items()))

    def to_dict(self) -> dict:
        return {
            "input": self.input_value,
            "sign": self.sign,
            "factors": list(self.factors),
            "factor_powers": self.factor_powers,
            "verified": self.verified,
            "primality_status": self.primality_status,
            "elapsed_seconds": self.elapsed_seconds,
            "events": [event.to_dict() for event in self.events],
        }


def is_probable_prime(n: int) -> bool:
    """Return primality, deterministically for n < 2**64."""
    if n < 2:
        return False
    for prime in SMALL_PRIMES:
        if n % prime == 0:
            return n == prime

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    bases = MR_BASES_64 if n < 2**64 else MR_BASES_LARGE
    for base in bases:
        a = base % n
        if a in (0, 1):
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _nontrivial_gcd(values: Iterable[int], n: int) -> int | None:
    for value in values:
        factor = gcd(abs(value), n)
        if 1 < factor < n:
            return factor
    return None


def _squfof_one_multiplier(n: int, multiplier: int, max_iterations: int) -> SplitEvent | None:
    """Try one SQUFOF principal cycle and return an exact split of n."""
    common = gcd(multiplier, n)
    if 1 < common < n:
        return SplitEvent(n, common, n // common, "multiplier-gcd", 0, multiplier)

    scaled_n = multiplier * n
    root_n = isqrt(scaled_n)
    if root_n * root_n == scaled_n:
        factor = _nontrivial_gcd((root_n,), n)
        if factor is not None:
            return SplitEvent(n, factor, n // factor, "squfof-geodesic", 0, multiplier, square_root_q=root_n)
        return None

    p_previous = root_n
    q_previous = 1
    q = scaled_n - root_n * root_n
    parity_index = 1
    tried_square_roots: set[int] = set()

    for forward in range(1, max_iterations + 1):
        if q <= 0:
            return None
        quotient = (root_n + p_previous) // q
        p = quotient * q - p_previous
        q_next = q_previous + quotient * (p_previous - p)
        p_previous, q_previous, q = p, q, q_next
        parity_index += 1

        # In this continued-fraction indexing only every other Q can be the
        # square form needed by SQUFOF.
        if parity_index % 2:
            continue
        square_root_q = isqrt(q)
        if square_root_q * square_root_q != q:
            continue
        if square_root_q == 1:
            # The principal cycle closed without a proper square form.
            return None
        if square_root_q in tried_square_roots:
            continue
        tried_square_roots.add(square_root_q)

        # Inverse square root form, followed to its ambiguous symmetry point.
        quotient = (root_n - p_previous) // square_root_q
        p_reverse = quotient * square_root_q + p_previous
        q_reverse_previous = square_root_q
        q_reverse = (scaled_n - p_reverse * p_reverse) // square_root_q

        for reverse in range(1, max_iterations + 1):
            if q_reverse <= 0:
                break
            quotient = (root_n + p_reverse) // q_reverse
            p_new = quotient * q_reverse - p_reverse
            q_new = q_reverse_previous + quotient * (p_reverse - p_new)
            if p_new == p_reverse:
                factor = _nontrivial_gcd(
                    (q_reverse, q_reverse_previous, q_reverse // 2, q_reverse_previous // 2),
                    n,
                )
                if factor is not None:
                    return SplitEvent(
                        source=n,
                        factor=factor,
                        cofactor=n // factor,
                        method="squfof-geodesic",
                        iterations=forward + reverse,
                        multiplier=multiplier,
                        forward_iterations=forward,
                        reverse_iterations=reverse,
                        square_root_q=square_root_q,
                    )
                break
            q_reverse_previous, q_reverse, p_reverse = q_reverse, q_new, p_new
    return None


def geodesic_squfof_split(
    n: int,
    *,
    max_iterations: int = 200_000,
    multipliers: Sequence[int] = SQUFOF_MULTIPLIERS,
) -> SplitEvent | None:
    """Split an odd composite using the modular-geodesic SQUFOF route."""
    if n <= 1:
        raise ValueError("SQUFOF requires n > 1")
    if n % 2 == 0:
        return SplitEvent(n, 2, n // 2, "trial-division", 0)
    root = isqrt(n)
    if root * root == n and 1 < root < n:
        return SplitEvent(n, root, root, "perfect-square", 0)
    if max_iterations < 1:
        raise ValueError("max_iterations must be positive")

    for multiplier in multipliers:
        if multiplier < 1 or multiplier % 2 == 0:
            raise ValueError("SQUFOF multipliers must be positive odd integers")
        split = _squfof_one_multiplier(n, multiplier, max_iterations)
        if split is not None:
            return split
    return None


def pollard_brent_split(
    n: int,
    *,
    rng: random.Random,
    max_iterations: int = 1_000_000,
    attempts: int = 32,
) -> SplitEvent | None:
    """Return a non-trivial factor with bounded Pollard rho (Brent batching)."""
    for prime in SMALL_PRIMES:
        if n % prime == 0:
            return SplitEvent(n, prime, n // prime, "trial-division", 0)
    if n <= 1 or is_probable_prime(n):
        return None

    total_iterations = 0
    for _attempt in range(attempts):
        y = rng.randrange(1, n - 1)
        c = rng.randrange(1, n - 1)
        block_size = rng.randrange(32, 257)
        g = 1
        radius = 1
        x = y
        y_saved = y

        while g == 1 and total_iterations < max_iterations:
            x = y
            for _ in range(radius):
                y = (y * y + c) % n
                total_iterations += 1
                if total_iterations >= max_iterations:
                    break

            offset = 0
            product = 1
            while offset < radius and g == 1 and total_iterations < max_iterations:
                y_saved = y
                width = min(block_size, radius - offset, max_iterations - total_iterations)
                for _ in range(width):
                    y = (y * y + c) % n
                    product = product * abs(x - y) % n
                total_iterations += width
                g = gcd(product, n)
                offset += width
            radius *= 2

        if g == n:
            while total_iterations < max_iterations:
                y_saved = (y_saved * y_saved + c) % n
                total_iterations += 1
                g = gcd(abs(x - y_saved), n)
                if g > 1:
                    break
        if 1 < g < n:
            return SplitEvent(n, g, n // g, "pollard-brent", total_iterations)
    return None


def _extract_small_primes(n: int, factors: list[int]) -> int:
    for prime in SMALL_PRIMES:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    return n


def factor_integer(
    value: int,
    *,
    method: str = "auto",
    seed: int = 642,
    max_iterations: int = 1_000_000,
    squfof_bit_limit: int = 62,
) -> FactorizationResult:
    """Completely factor an integer within the selected methods' work budget.

    ``auto`` uses multi-multiplier SQUFOF first for residuals up to the bit
    limit and Pollard--Brent otherwise.  ``squfof`` disables the fallback;
    ``rho`` skips SQUFOF and is useful as an independent control.
    """
    if value == 0:
        raise ValueError("zero has no finite prime factorization")
    if method not in {"auto", "squfof", "rho"}:
        raise ValueError("method must be one of: auto, squfof, rho")
    if max_iterations < 1:
        raise ValueError("max_iterations must be positive")

    wall_start = time.perf_counter()
    sign = -1 if value < 0 else 1
    original = abs(value)
    factors: list[int] = []
    events: list[SplitEvent] = []
    rng = random.Random(seed)
    remaining = _extract_small_primes(original, factors) if original > 1 else original
    stack = [remaining] if remaining > 1 else []

    while stack:
        n = stack.pop()
        if n == 1:
            continue
        if is_probable_prime(n):
            factors.append(n)
            continue

        root = isqrt(n)
        if root * root == n:
            split = SplitEvent(n, root, root, "perfect-square", 0)
        else:
            split = None
            if method in {"auto", "squfof"} and n.bit_length() <= squfof_bit_limit:
                split = geodesic_squfof_split(n, max_iterations=max_iterations)
            if split is None and method in {"auto", "rho"}:
                split = pollard_brent_split(n, rng=rng, max_iterations=max_iterations)

        if split is None:
            raise FactorizationFailure(
                f"could not split composite {n} with method={method} and "
                f"max_iterations={max_iterations}"
            )
        if split.factor <= 1 or split.cofactor <= 0 or split.factor * split.cofactor != n:
            raise AssertionError(f"invalid split produced for {n}: {split}")
        events.append(split)
        stack.extend((split.factor, split.cofactor))

    factors.sort()
    product = 1
    for factor in factors:
        product *= factor
    all_prime = all(is_probable_prime(factor) for factor in factors)
    verified = product == original and all_prime
    deterministic = all(factor < 2**64 for factor in factors)
    primality_status = "deterministic-64-bit" if deterministic else "probable-prime-above-64-bit"
    return FactorizationResult(
        input_value=value,
        sign=sign,
        factors=tuple(factors),
        events=tuple(events),
        elapsed_seconds=time.perf_counter() - wall_start,
        verified=verified,
        primality_status=primality_status,
    )


def _parse_integer(text: str) -> int:
    try:
        return int(text.replace("_", ""), 0)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"not an integer: {text!r}") from exc


def _format_powers(result: FactorizationResult) -> str:
    pieces = []
    if result.sign < 0:
        pieces.append("-1")
    for prime, exponent in result.factor_powers.items():
        pieces.append(str(prime) if exponent == 1 else f"{prime}^{exponent}")
    return " x ".join(pieces) if pieces else str(result.sign)


def _print_human(result: FactorizationResult, trace: bool) -> None:
    print(f"N = {result.input_value}")
    print(f"factorization = {_format_powers(result)}")
    print(f"verified = {'yes' if result.verified else 'no'} ({result.primality_status})")
    print(f"elapsed_seconds = {result.elapsed_seconds:.6f}")
    if trace:
        if not result.events:
            print("trace = no composite split needed")
        for index, event in enumerate(result.events, 1):
            detail = f", multiplier={event.multiplier}, discriminant={event.discriminant}" if event.discriminant else ""
            print(
                f"trace[{index}] {event.source} -> {event.factor} x {event.cofactor} "
                f"via {event.method} ({event.iterations} iterations{detail})"
            )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Factor integers through TFPT's N-dependent modular-geodesic lane, with an exact classical fallback."
    )
    parser.add_argument("integers", nargs="+", type=_parse_integer, metavar="N")
    parser.add_argument("--method", choices=("auto", "squfof", "rho"), default="auto")
    parser.add_argument("--max-iterations", type=int, default=1_000_000)
    parser.add_argument("--squfof-bit-limit", type=int, default=62)
    parser.add_argument("--seed", type=int, default=642)
    parser.add_argument("--trace", action="store_true", help="show each exact composite split")
    parser.add_argument("--json", action="store_true", help="emit a JSON array")
    args = parser.parse_args(argv)

    results: list[FactorizationResult] = []
    try:
        for offset, value in enumerate(args.integers):
            results.append(
                factor_integer(
                    value,
                    method=args.method,
                    seed=args.seed + offset,
                    max_iterations=args.max_iterations,
                    squfof_bit_limit=args.squfof_bit_limit,
                )
            )
    except (ValueError, FactorizationFailure) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps([result.to_dict() for result in results], indent=2, sort_keys=True))
    else:
        for index, result in enumerate(results):
            if index:
                print()
            _print_human(result, args.trace)
    return 0 if all(result.verified for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
