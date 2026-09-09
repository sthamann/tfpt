"""Cubic evaluation of the resummed-leaf target with one explicit M layer.

NON-RH. Bare-low E0 column only; every later M layer has a separate tail.
Integer native grouping is independently checked against Python CAR paths.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import factorial, lcm
from pathlib import Path
import struct
import subprocess
import tempfile

PINS = {
    "checker.py": "eb4045e3fd119c8906f4f1371ba16e6cc766d8c9c7858409d496342dd2a51a63",
    "WORD_RESUMMATION.md": "e74135bf4b854f9efe89853ffd7a6b027494951c8b9a868505dce90ed7da5f78",
    "validation.json": "4ca67cb4410a083d096495b32e3a6ff6be0f6230d8031d5711ba04b9214b252d",
}
HERE = Path(__file__).resolve().parent


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/word-resummation-round46"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round46 pin: "+name)
    spec = importlib.util.spec_from_file_location("r46_bulk_word_parent", folder/"checker.py")
    r46 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r46)
    return (r46, *r46.inherited(root))


def relative_action(word, creates, initial=()):
    """Finite flips from uniform bare-low; parity of a complete odd-side cube.

An even half-width fixes the irrelevant common odd-operator phase.
Unlike an initial-space quotient, this applies the FINAL whole CAR word.
"""
    flips, sign = set(initial), 1
    for (site, species), create in zip(word[::-1], creates[::-1]):
        mode = site, species
        occupied = (species == 0) ^ (mode in flips)
        if occupied == create:
            return None
        if (sum(site)+species+sum(other < mode for other in flips)) % 2:
            sign = -sign
        if mode in flips:
            flips.remove(mode)
        else:
            flips.add(mode)
    return tuple(sorted(flips)), sign


def rotate_output(r45, flips, flux, axis, sign):
    # A canonical word mapping bare filling to this output determines the
    # fermionic rotation cocycle, independently of how the source got here.
    high = tuple(mode for mode in flips if mode[1] == 1)
    low = tuple(mode for mode in flips if mode[1] == 0)
    word, creates = high+low, (True,)*len(high)+(False,)*len(low)
    old = relative_action(word, creates)
    rotated = tuple((r45.rotate_point(site, axis, sign), species) for site, species in word)
    new = relative_action(rotated, creates)
    require(old is not None and new is not None and old[0] == flips, "rotation of a physical bare-output state")
    return (new[0], r45.rotate_flux(flux, axis, sign)), old[1]*new[1]


def build_native(folder):
    executable = Path(folder)/"group_suffix"
    result = subprocess.run(["clang++", "-std=c++17", "-O2", str(HERE/"group_suffix.cpp"), "-o", str(executable)],
                            capture_output=True, text=True)
    require(result.returncode == 0, "native grouping build: "+result.stderr)
    return executable


def write_seed(stream, p):
    stream.write(struct.pack("<q", p["weight"]))
    for site, species in p["word"]:
        stream.write(struct.pack("<4i", *site, species))
    for flux in p["prefixes"]:
        stream.write(struct.pack("<i", len(flux)))
        for edge, value in flux:
            stream.write(struct.pack("<5i", *edge, value))
    for frequencies, sign in zip(p["frequencies"], p["signs"]):
        stream.write(struct.pack("<"+"i"*(len(frequencies)+1), *frequencies, sign))


def group_native(r45, r42, executable, folder, paths, arity, order, steps=1, multiplicity=6):
    require((arity, order) in ((3, 4), (5, 3)) and steps in (0, 1) and multiplicity in (1, 6), "declared native family")
    input_path, output_path = Path(folder)/f"seeds-{arity}.bin", Path(folder)/f"groups-{arity}-{steps}.bin"
    moments, raw, count = [0]*(1 << arity), defaultdict(int), 0
    with input_path.open("wb") as stream:
        stream.write(struct.pack("<I3i", 0x47504654, arity, order, 2 if arity == 3 else 4))
        for p in paths:
            require(p["order"] == order and len(p["word"]) == arity, "uniform raw seeds")
            write_seed(stream, p)
            moment, _ = r45.moment_factors(p["dots"], tuple(r42.length(f) for f in p["prefixes"]))
            species = sum(mode[1] << j for j, mode in enumerate(p["word"]))
            moments[species] += abs(p["weight"])*moment
            raw[p["kind"]] += 1
            count += 1
        stream.write(struct.pack("<q", 0))
    with input_path.open("rb") as stream:
        result = subprocess.run([str(executable), str(output_path), str(steps)], stdin=stream, capture_output=True, text=True)
    require(result.returncode == 0, "native grouping: "+result.stderr)
    cost = json.loads(result.stderr)
    require(cost["seed_records"] == count, "all raw seeds consumed")
    return {"path": output_path, "order": order+steps, "arity": arity, "multiplicity": multiplicity,
            "seed_species_moments": [F(multiplicity*x, 576**order) for x in moments],
            "raw_seed_counts": {k: v*multiplicity for k, v in raw.items()}, "cost": cost,
            "grouped_bytes": output_path.stat().st_size, "seed_bytes": input_path.stat().st_size}


def iter_groups(grouped):
    nfreq = grouped["order"]+1
    with grouped["path"].open("rb") as stream:
        count, = struct.unpack("<Q", stream.read(8))
        require(count == grouped["cost"]["groups"], "group record count")
        for _ in range(count):
            length, = struct.unpack("<i", stream.read(4))
            require(nfreq+2 <= length <= 200, "bounded physical group key")
            key = stream.read(4*length)
            weight, = struct.unpack("<q", stream.read(8))
            require(len(key) == 4*length and weight != 0, "complete nonzero group record")
            yield key[:-4*nfreq], struct.unpack("<"+"i"*nfreq, key[-4*nfreq:]), weight
        require(not stream.read(1), "no trailing group data")


def decode_output(key):
    values = struct.unpack("<"+"i"*(len(key)//4), key)
    n, i = values[0], 1
    flips = tuple((tuple(values[i+4*j:i+4*j+3]), values[i+4*j+3]) for j in range(n))
    i += 4*n
    count, i = values[i], i+1
    flux = tuple((tuple(values[i+5*j:i+5*j+4]), values[i+5*j+4]) for j in range(count))
    require(i+5*count == len(values) and tuple(sorted(flips)) == flips, "physical output key")
    return flips, flux


def compile_groups(r41, r39, grouped, time=F(1), degree=80):
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "phase time/degree")
    absolute = defaultdict(int)
    for _, frequencies, weight in iter_groups(grouped):
        absolute[frequencies] += abs(weight)
    n, den, error, kernels = grouped["order"], 1, F(0), {}
    phase = ((-1, 0), (0, -1), (1, 0), (0, 1))[n % 4]  # -i^n
    for frequencies, weight in sorted(absolute.items()):
        value, tail = r39.simplex_integral(tuple(F(f, 2400) for f in frequencies), time, degree)
        a, b = r41.multiply(phase, value)
        kernels[frequencies] = a/576**n, b/576**n
        den = lcm(den, kernels[frequencies][0].denominator, kernels[frequencies][1].denominator)
        error += F(weight, 576**n)*tail
    integer = {f: (int(a*den), int(b*den)) for f, (a, b) in kernels.items()}
    vector = defaultdict(lambda: (0, 0))
    for key, f, weight in iter_groups(grouped):
        a, b = integer[f]
        vector[key] = r41.add(vector[key], (weight*a, weight*b))
    return {"vector": {key: value for key, value in vector.items() if value != (0, 0)},
            "denominator": den, "numerical_error": grouped["multiplicity"]*error,
            "multiplicity": grouped["multiplicity"], "time": time, "frequency_kernels": len(kernels),
            "arithmetic_error_scope": "bare-low E0 physical column only"}


def species_multiply(vector, matrix, arity):
    out = [F(0)]*len(vector)
    for pattern, weight in enumerate(vector):
        for leg in range(arity):
            old = (pattern >> leg) & 1
            for new in (0, 1):
                target = (pattern & ~(1 << leg)) | (new << leg)
                out[target] += weight*matrix[old][new]
    return out


def suffix_tail(r46, r40, r38, moments, arity, electric_count, time=F(1), retained=1, through=18):
    """All later M layers, with the final M commutator bounded on full Fock.

Earlier M legs use the exact positive species tensor matrix. No l2
isometry of the physical CAR map or initial-null pruning is used.
"""
    time = abs(F(time))
    require(time <= 1 and arity in (3, 5) and electric_count == (arity-1)//2 and retained == 1 and through >= 2,
            "declared all-later-M tail")
    require(len(moments) == 1 << arity and all(x >= 0 for x in moments), "raw species moment vector")
    c = (r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1])
    car = [sum(c[(s >> leg) & 1] for leg in range(arity)) for s in range(1 << arity)]
    v, terms = list(moments), []
    first_car = sum(a*b for a, b in zip(v, car))
    for m in range(1, through+1):
        if m > retained:
            terms.append(sum(a*b for a, b in zip(v, car))*time**(5+m)/factorial(5+m))
        v = species_multiply(v, r40.W, arity)
    leading = sum(v)*arity*c[0]*time**(6+through)/factorial(6+through)
    ratio = arity*r46.MU*time/F(7+through)
    require(ratio < 1, "positive all-M remainder ratio")
    tail = leading/(1-ratio)
    factor = F(1, 100)**electric_count
    return {"upper": factor*(sum(terms)+tail), "series_terms": [factor*x for x in terms],
            "remaining_series_tail": factor*tail, "retained_suffix_M_steps": retained,
            "through": through, "first_M_CAR_moment": first_car, "seed_species_moments": moments,
            "order": 7}


def common_bare_column(r45, r41, linear, sources, suffixes):
    den = lcm(linear["denominator"], *(s["denominator"] for s in sources+suffixes))
    output = defaultdict(lambda: (0, 0))
    def add(key, value, scale):
        a, b = value
        output[key] = r41.add(output[key], (scale*a, scale*b))
    for (mode, flux), value in linear["coefficients"].items():
        step = relative_action((mode,), (False,))
        if step:
            add((step[0], flux), value, step[1]*(den//linear["denominator"]))
    for source in sources:
        scale = den//source["denominator"]
        for (word, flux), value in r45.coefficient_terms(source):
            step = relative_action(word, source.get("creates", r45.CREATES[len(word)]))
            if step:
                add((step[0], flux), value, step[1]*scale)
    for source in suffixes:
        scale = den//source["denominator"]
        for key, value in source["vector"].items():
            flips, flux = decode_output(key)
            if source["multiplicity"] == 1:
                add((flips, flux), value, scale)
            else:
                for axis in range(3):
                    for sign in (-1, 1):
                        rotated, parity = rotate_output(r45, flips, flux, axis, sign)
                        add(rotated, value, scale*parity)
    output = {key: value for key, value in output.items() if value != (0, 0)}
    q = F(sum(a*a+b*b for a, b in output.values()), den*den)
    return {"probability": q, "output_count": len(output),
            "numerical_error": linear["numerical_error"]+sum(s["numerical_error"] for s in sources+suffixes),
            "time": linear["time"], "scope": "bare-low E0 initial column on the full cubic parent"}


def interval(r38, column, ideal, tails):
    error = ideal["upper"]+sum(t["upper"] for t in tails)+column["numerical_error"]
    lo, hi = r38.sqrt_interval(column["probability"])
    out = {"approximate_probability": column["probability"], "high_occupation_lower": max(F(0), lo-error)**2,
           "high_occupation_upper": min(F(1), (hi+error)**2), "total_amplitude_error": error,
           "ideal_electric_error": ideal["upper"], "M_suffix_evaluation_error": sum(t["upper"] for t in tails),
           "configuration_and_arithmetic_error": column["numerical_error"]}
    out["decimal_interval"] = r38.display_interval(out)
    return out


def run(root):
    r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = inherited(root)
    with tempfile.TemporaryDirectory(prefix="tfpt-round47-") as work:
        exe = build_native(work)
        one = group_native(r45, r42, exe, work, r45.one_e_paths(r42, r41, r40), 3, 4)
        two = group_native(r45, r42, exe, work, r45.two_e_paths(r42, r41, r40), 5, 3)
        new = [compile_groups(r41, r39, g) for g in (one, two)]
        tails = [suffix_tail(r46, r40, r38, g["seed_species_moments"], g["arity"], (g["arity"]-1)//2) for g in (one, two)]
        ideal = r46.bound(r45, r43, r42, r41, r40, r38)
        linear = r44.compile_cubic(r38, r44.build_ball(r40, 6))
        old = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40)),
                         r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41)))
        c1 = r45.compile_source(r41, r39, r45.collect(r42, r45.one_e_paths(r42, r41, r40), 4, 1, 6), expand=False)
        c2 = r45.compile_source(r41, r39, r45.collect(r42, r45.two_e_paths(r42, r41, r40), 3, 2, 6), expand=False)
        sources = [old, c1, c2]
        baseline = common_bare_column(r45, r41, linear, sources, [])
        column = common_bare_column(r45, r41, linear, sources, new)
        result = interval(r38, column, ideal, tails)
        here = Path(__file__).resolve().parent
        return r38.encode({"verdict": "EVALUATED_CUBIC_BARE_RESUMMED_TARGET_WITH_EXPLICIT_ALL_LATER_M_TAIL",
            "parent_pins": PINS, "time": F(1), "bare_cubic_readout_executed": True,
            "retained_suffix_M_steps": 1, "all_later_M_layers_bounded": True,
            "new_bulk_Bell_readout_executed": False, "full_electric_dynamics_solved": False,
            "readout": result, "column": column, "old45_column": baseline,
            "ideal_electric_bound": ideal, "suffix_tails": tails,
            "native_groups": [{k: v for k, v in g.items() if k != "path"} for g in (one, two)],
            "phase_kernel_counts": [s["frequency_kernels"] for s in new],
            "representative_output_counts": [len(s["vector"]) for s in new],
            "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                        for name in ("checker.py", "group_suffix.cpp", "BULK_WORD.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=HERE.parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(args.repo), indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
