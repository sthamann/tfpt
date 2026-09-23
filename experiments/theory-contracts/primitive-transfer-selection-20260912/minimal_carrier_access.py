"""Exact reachability in the already fixed source, with declared added readout."""
import itertools
import json
import sympy as S
import boundary_access as source


def main():
    J, B, O, P = source.source_matrices()
    D = J+B/8
    E = S.eye(16)
    # Boundary seeds are included as their full previously verified dynamical span.
    baseline = S.Matrix.hstack(*P.columnspace())
    powers = [D**k for k in range(16)]
    def reachable(*seeds):
        return S.Matrix.hstack(baseline, *(power*v for v in seeds for power in powers)).rank()
    single = [reachable(E[:,j]) for j in range(10)]
    source.require(single == [14]*6+[12]*4, 'all individual carrier coordinate ranks')
    pairs = []
    for j,k in itertools.combinations(range(10),2):
        rank = reachable(E[:,j], E[:,k])
        expected = 16 if j<6<=k else (14 if k<6 else 12)
        source.require(rank == expected, 'complete two-coordinate classification')
        if rank == 16:
            pairs.append([j,k])
    mixed = E[:,0]+E[:,6]
    source.require(reachable(mixed) == 16, 'one coherent mixed seed reaches all modes')
    source.require(reachable(P*mixed) == 10, 'clock-averaged seed remains blind')
    source.require(reachable(E[:,10]) == 10, 'another boundary coordinate stays blind')
    source.require(reachable() == 10, 'unchanged baseline')
    source.require(source.count == 57, 'declared exact check count')
    print(json.dumps({'checks': source.count, 'source_sha256': source.PIN,
        'source_point': {'alpha': '1', 'g': '1/8'},
        'single_coordinate_ranks': single, 'full_rank_coordinate_pairs': pairs,
        'mixed_seed_indices': [0,6], 'mixed_seed_rank': 16,
        'clock_averaged_seed_rank': 10, 'added_access_TFPT_derived': False,
        'field_reachability_not_state_preparation': True, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
