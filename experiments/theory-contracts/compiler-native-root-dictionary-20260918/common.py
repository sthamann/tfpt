import os,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=Path(os.environ['TFPT_DICTIONARY_OUTPUT'])
PINS=json.loads((HERE/'source_pins.json').read_text())
for source,expected in PINS.items():
 actual=hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
 if actual!=expected:raise RuntimeError('Source drift: '+source)
D=json.loads((ROOT/'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json').read_text())
