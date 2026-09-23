import os,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=Path(os.environ['TFPT_E6_OUTPUT'])
PINS=json.loads((HERE/'source_pins.json').read_text())
for p,h in PINS.items():
 if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise RuntimeError('source drift '+p)
