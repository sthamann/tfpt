"""Exact bounded controls, supplemental to the all-integer written proof."""
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parent
results = []


def check(name, condition):
    ok = bool(condition)
    results.append({"check": name, "passed": ok})
    assert ok, name


def omega(n):
    return sum(s.factorint(n).values())


check("positive additive counterexample reverses 4<5", 4 < 5 and omega(4) == 2 and omega(5) == 1)
check("Omega bounded composition controls", all(omega(m*n) == omega(m)+omega(n) for m in range(1, 16) for n in range(1, 16)))

# Verify the sandwich itself using only integer arithmetic; no logarithm floats.
# floor(log_2(n^k)) is exactly bit_length(n^k)-1.
check("integer power sandwiches", all(2**((n**k).bit_length()-1) <= n**k < 2**((n**k).bit_length()) for n in [2, 3, 5, 7, 11, 101] for k in [1, 2, 7, 31]))

q = 101
check("finite exact agreement does not determine later prime weight", all(s.factorint(n).get(q, 0) == 0 for n in range(1, q)) and s.factorint(q)[q] == 1 and s.factorint(q+1).get(q, 0) == 0 and 2*q > q+1)

a,b,c,d,x,y = s.symbols("a b c d x y")
K = s.Matrix([[a*x, b*y], [c*x, d*y]])
check("mixed cycle coefficient bc in trace K^2/2", s.expand(s.trace(K*K)/2).coeff(x, 1).coeff(y, 1) == b*c)
z = (-1+s.I*s.sqrt(7))/4
check("K4 nontrivial pole", s.simplify(1+z+2*z*z) == 0 and s.simplify(z*s.conjugate(z)) == s.Rational(1, 2))

payload = {"scope":"bounded exact algebraic controls; no numerical or formal proof of RH", "all_passed":all(x["passed"] for x in results), "checks":results}
(root/"checks.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
print(json.dumps(payload, ensure_ascii=False, indent=2))
