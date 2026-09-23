"""Two-edge current-field construction; NOT a microscopic twist-field limit.

Exact finite CAR checks and spectral identities accompany the proof in README.
Numerical partial sums are diagnostics, never evidence of an infinite limit.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    "experiments/theory-contracts/source-half-sector-bridge/checker.py":
        "43d682889f84f83b8a7ba7c5d7bf0ce92913d6310d6ba7243d07c827e6a2218d",
    "experiments/theory-contracts/source-half-sector-bridge/README.md":
        "5fc767e148bff3381f27459df28412fa1b17b604b19c0b34353e7c6314a5403d",
    "experiments/theory-contracts/current-truncation-bridge/README.md":
        "73a74a0c0a433f465ed9bc948296338b8573e0b05423dfcd19f9ee17e74d34cb",
    "experiments/theory-contracts/neutral-current-limit/checker.py":
        "2e4a03cbacc3bc0ed4835facd85e8abce2f2585d717abc56fc2dc57f6b67c136",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_pins(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)


@lru_cache(maxsize=1)
def inherited():
    validate_pins()
    modules = []
    for index, name in enumerate((list(PINS)[0], list(PINS)[3])):
        spec = importlib.util.spec_from_file_location("spacetime_inherited_"+str(index), ROOT/name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    modules[0].validate_pins()
    return tuple(modules)


def coefficients(level, beta=F(1, 4)):
    require(type(level) is int and level >= 0 and beta > 0, "coefficient domain")
    out = [F(1)]
    for n in range(1, level+1):
        out.append(out[-1]*(n-1+beta)/n)
    return out


def vacuum_mask(width, q, edge):
    require(type(width) is int and type(q) is int and width > abs(q), "protected charge window")
    require(edge in ("top", "bottom"), "source edge")
    return sum(1 << (j+width) for j in range(-width, width+1)
               if (j >= 1-q if edge == "top" else j <= q))


def bilinear(mask, dest, src):
    """Apply c_dest^* c_src with the fixed ascending-label CAR convention."""
    if not (mask >> src) & 1:
        return None
    sign = (-1)**((mask & ((1 << src)-1)).bit_count())
    after = mask ^ (1 << src)
    if (after >> dest) & 1:
        return None
    sign *= (-1)**((after & ((1 << dest)-1)).bit_count())
    return after | (1 << dest), sign


def current(state, k, width, edge):
    require(type(k) is int and k != 0, "nonzero current index")
    require(edge in ("top", "bottom"), "source edge")
    out = {}
    shift = k if edge == "top" else -k
    for mask, amplitude in state.items():
        for src in range(2*width+1):
            dest = src+shift
            if 0 <= dest <= 2*width:
                term = bilinear(mask, dest, src)
                if term is not None:
                    target, sign = term
                    out[target] = out.get(target, F(0))+sign*amplitude
    return {mask: amplitude for mask, amplitude in out.items() if amplitude}


def car_levels(level, q=0, edge="top", weights=None):
    """Coherent levels directly in the protected finite-source CAR basis.

    weights[k] is g_k (not g_k squared); the output norm uses g_k squared.
    This checks the sourced LIMIT current algebra, not a finite-N twist.
    """
    require(type(level) is int and level >= 0, "nonnegative CAR level")
    width = abs(q)+level+2
    alpha = F(1, 2) if edge == "top" else F(-1, 2)
    weights = [F(1)]*(level+1) if weights is None else weights
    require(len(weights) > level and all(0 <= w <= 1 for w in weights), "current regulator")
    out = [{vacuum_mask(width, q, edge): F(1)}]
    for n in range(1, level+1):
        state = {}
        for k in range(1, n+1):
            for mask, amplitude in current(out[n-k], -k, width, edge).items():
                state[mask] = state.get(mask, F(0))+alpha*weights[k]*amplitude/n
        out.append({mask: amplitude for mask, amplitude in state.items() if amplitude})
    return width, out


def car_energy(mask, width, r, edge):
    require(r in (1, 3), "source sector")
    sea = vacuum_mask(width, 0, edge)
    sign = 1 if edge == "top" else -1
    return sum(sign*(F(r, 4)-j)*(((mask >> (j+width)) & 1)-((sea >> (j+width)) & 1))
               for j in range(-width, width+1))


def partition_norm(level, alpha=F(1, 2)):
    """Independent oscillator-partition enumeration, including factorial norms."""
    def visit(k, remaining):
        if k > level:
            return F(remaining == 0)
        return sum((alpha*alpha/k)**count/F(math.factorial(count))*visit(k+1, remaining-k*count)
                   for count in range(remaining//k+1))
    return visit(1, level)


def h(p):
    require(isinstance(p, (int, F)) and (2*p).denominator == 1, "half-integer reference charge")
    return p*p-F(1, 2)*p


def transition(p, top, bottom, inverse=False):
    require(type(top) is int and type(bottom) is int and min(top, bottom) >= 0, "oscillator levels")
    delta = F(-1, 2) if inverse else F(1, 2)
    return dict(output_charge=p+delta, output_energy=h(p+delta)+top+bottom,
                frequency=h(p+delta)-h(p)+top+bottom, momentum=bottom-top)


def spatial_coefficient(k, digits=50):
    require(type(k) is int, "integer spatial mode")
    with mp.workdps(digits):
        a = mp.mpf(1)/4
        value = mp.gamma(1-2*a)*mp.gamma(abs(k)+a)/(mp.gamma(a)*mp.gamma(1-a)*mp.gamma(abs(k)+1-a))
        return +value


def spatial_domain_exponent(s, beta=F(1, 4)):
    """Asymptotic summand exponent, not a fitted finite-size classification."""
    require(s >= 0 and beta > 0, "nonnegative energy power and positive vertex weight")
    return 2*s+2*beta-2


def diagonal_moment(cutoff, s=0, sigma=None, p=F(0), inverse=False):
    """Constant spatial smear, normalized Gaussian time smear if sigma is set.

    Squared (1+H)^s norm: Gaussian transform exp(-sigma^2 omega^2/2).
    With sigma=None this is only a partial sum, including at divergent s.
    """
    require(type(cutoff) is int and cutoff >= 0 and s >= 0, "moment domain")
    require(sigma is None or math.isfinite(sigma) and sigma > 0, "positive time width")
    b = 1.0
    result = 0.0
    for n in range(cutoff+1):
        row = transition(p, n, n, inverse)
        temporal = 1.0 if sigma is None else math.exp(-sigma*sigma*float(row["frequency"])**2)
        result += b*b*float(1+row["output_energy"])**(2*s)*temporal
        b *= (n+.25)/(n+1)
    return result


def raw_mode_element(out, inp, lam):
    """<0|a^out exp(lam a*) exp(-lam a) (a*)^inp|0>, real lam."""
    require(type(out) is int and type(inp) is int and min(out, inp) >= 0, "occupation domain")
    return math.factorial(out)*math.factorial(inp)*sum(
        (-lam)**(inp-j)*lam**(out-j)/
        F(math.factorial(inp-j)*math.factorial(out-j)*math.factorial(j))
        for j in range(min(out, inp)+1))


def record():
    bridge, kernel = inherited()
    level = 6
    exact = coefficients(level)
    car_rows = []
    for edge in ("top", "bottom"):
        for q in range(-2, 3):
            width, states = car_levels(level, q, edge)
            norms = [sum(v*v for v in state.values()) for state in states]
            require(norms == exact, "independent CAR coefficient equality")
            for r in (1, 3):
                for n, state in enumerate(states):
                    require(all(car_energy(mask, width, r, edge)-bridge.edge_energy(r, q, edge) == n
                                for mask in state), "actual source excitation energy")
            car_rows.append(dict(edge=edge, relative_charge=q, level_squared_norms=list(map(str, norms))))
    rational = [F(1, 2)**k for k in range(level+1)]
    regulated = kernel.kernel_coefficients([g*g for g in rational], F(1, 4))
    require(regulated == [exact[n]*F(1, 4)**n for n in range(level+1)], "radial regulator")
    for n in range(level+1):
        require(partition_norm(n) == exact[n], "independent oscillator partition")
    return dict(
        status="CONDITIONAL_TWO_EDGE_SPACETIME_CURRENT_FIELD",
        published_base="66b91e40e245569f06ab440ead80f446c9be0ee5", pins=PINS,
        car_level_checks=car_rows,
        spatial_C0=mp.nstr(spatial_coefficient(0), 45),
        spatial_domain_condition="s >= 0: V(f)Omega in D(H^s) iff s < 1/4, nonzero smooth f",
        zero_mode_vacuum_output_energies={"forward": "0", "adjoint": "1/2"},
        conditional_eight_pair_product=dict(
            assumed_independent_pairs=8, beta_per_edge="2",
            single_edge_level_coefficient="n+1",
            spatial_constant_norm_partial_sum="(N+1)(N+2)(2N+3)/6",
            summed_energy_shell_coefficient="binomial(ell+3,3)",
            vacuum_spacetime_decay_sufficient="M > s+2",
            source_channel_selection_proved=False),
        diagonal_partial_sums=[dict(cutoff=n, hilbert=diagonal_moment(n),
                                    critical_quarter=diagonal_moment(n, s=.25),
                                    energy_form=diagonal_moment(n, s=.5)) for n in (100, 1000, 10000)],
        gaussian_time_diagnostics=[dict(inverse=inverse, energy_power=s, sigma=.3,
                                        squared_graph_norm=diagonal_moment(120, s=s, sigma=.3, inverse=inverse))
                                   for inverse in (False, True) for s in (0, .5, 1, 2)],
        limiting_current_finite_core_spacetime_construction=True,
        closability_argument_in_readme=True,
        independent_mathematical_review=False,
        uniform_all_input_energy_bound_proved=False,
        field_word_invariant_domain_proved=False,
        microscopic_intersector_operator_limit_proved=False,
        physical_current_prescription_selected=False,
        locality_proved=False, opposite_edge_removed=False,
        eight_channel_E8_selection=False, T1_T8_closed=[])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(), indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)
