"""Regression for the Monte Carlo family's attainable significance resolution."""
import probe
import numpy as np
# Under the documented two-sided add-one test the floor is 2/(B+1).
B=probe.DEFAULT_REPLICATES if hasattr(probe,'DEFAULT_REPLICATES') else 999
raw=np.full(30,2/(B+1))
assert max(probe.holm(raw)) < .05, f'B={B}: Holm floor {max(probe.holm(raw))} cannot detect even a perfect signal'
print('Monte Carlo resolution regression PASS')
