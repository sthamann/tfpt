"""Exact decomposition of the ENTIRE 24024-dimensional singlet under 2^4:S5.

The dual translation group has three S5 orbits: sizes 1,5,10, with little
groups S5, S4, S2xS3. Character sums give all multiplicity block sizes.
This is a reduction theorem, not a calculation of their eigenvalues.
"""
from itertools import permutations, product
from pathlib import Path
import hashlib, json, math
from checker import graph, char, cycle_type, partitions

_,_,aut=graph();flips=[f for f in product((-1,1),repeat=5) if math.prod(f)==1]
records=[]
for weight,orbit in ((0,1),(1,5),(2,10)):
    if weight==0:
        small_shapes=[(s,) for s in partitions(5)]
        blocks=[tuple(range(5))]
    elif weight==1:
        small_shapes=[(s,) for s in partitions(4)]
        blocks=[tuple(range(1,5))]
    else:
        small_shapes=[(s,t) for s in partitions(2) for t in partitions(3)]
        blocks=[(0,1),(2,3,4)]
    subgroup=[s for s in permutations(range(5))
              if all({s[i] for i in b}==set(b) for b in blocks)]
    for shapes in small_shapes:
        dimension=math.prod(char(shape,(1,)*len(b)) for shape,b in zip(shapes,blocks))
        total=0
        for sigma in subgroup:
            little_character=math.prod(char(shape,cycle_type(tuple(b.index(sigma[i]) for i in b)))
                                       for shape,b in zip(shapes,blocks))
            for f in flips:
                translation_character=math.prod(f[i] for i in range(weight))
                total+=translation_character*little_character*char((4,4,4,4),cycle_type(aut(sigma,f)))
        denominator=16*len(subgroup)
        if total%denominator:
            raise RuntimeError('non-integral little-group multiplicity')
        multiplicity=total//denominator
        if multiplicity<0:
            raise RuntimeError('negative multiplicity')
        records.append({'dual_weight':weight,'momentum_orbit_size':orbit,
            'little_shapes':shapes,'little_irrep_dimension':dimension,
            'full_irrep_dimension':dimension*orbit,
            'multiplicity_block_dimension':multiplicity,
            'isotypic_dimension':multiplicity*dimension*orbit})
if sum(r['isotypic_dimension'] for r in records)!=24024:
    raise RuntimeError('decomposition dimension sum')
result={'singlet_dimension':24024,'block_count':len(records),'blocks':records,
    'sum_multiplicity_block_dimensions':sum(r['multiplicity_block_dimension'] for r in records),
    'largest_multiplicity_block':max(r['multiplicity_block_dimension'] for r in records),
    'eigenvalue_ordering_certified':False,
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('little_group_reduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
