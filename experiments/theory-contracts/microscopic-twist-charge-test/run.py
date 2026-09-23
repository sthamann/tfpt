"""Complete bounded replay with explicit finite/analytic scope boundaries."""
import argparse
import hashlib
import json
from pathlib import Path

import checker as c
import mass_window as m
import spectral_flow as s


def record():
    c.validate_pins()
    return dict(
        baseline_commit="66b91e40e245569f06ab440ead80f446c9be0ee5",
        source_pins=c.PINS,
        original_twist=[c.diagnostic(n) for n in (16,32,64)],
        independent_controls=[c.controls(n) for n in (16,32,64)],
        two_forward_original=[c.two_forward(n) for n in (16,32,64)],
        global_polar_carrier=[s.finite_source_carrier(n) for n in (16,32,64,128,256)],
        improved_candidate=[s.replacement_candidate(n) for n in (16,32,64)],
        fundamental_mass_width_audit=m.record(),
        local_code_sha256={name:hashlib.sha256((c.HERE/name).read_bytes()).hexdigest()
                           for name in ("checker.py","spectral_flow.py","mass_window.py","test_checker.py","run.py")},
        full_local_microscopic_half_field=False,
        original_twist_renormalized_smeared_limit_proved=False,
        global_carrier_locality_proved=False,
        global_carrier_source_selection_proved=False,
        eight_marked_channels_derived=False,
        all_T1_T8_remain_open=True)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=json.dumps(record(),sort_keys=True,indent=2)+"\n"
    if args.output: args.output.write_text(result)
    else: print(result,end="")
