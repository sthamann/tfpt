"""Generic numerical/algebraic dependencies retained for TFPT.

Extracted by dependency closure from v738_hecke_mod_ramified.py at public commit ba2f0fc.
Function bodies/constants retain their original mathematics. Dedicated Prime
Front checks, claim registration and runner are maintained in prime-front.
This support module makes no independently registered claim.
"""
def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def gnorm(x):
    return x[0] * x[0] + x[1] * x[1]

def gquo_exact(x, d):
    """x / d in Z[i], exact (asserts divisibility)."""
    n = gnorm(d)
    xr = x[0] * d[0] + x[1] * d[1]
    xi = x[1] * d[0] - x[0] * d[1]
    assert xr % n == 0 and xi % n == 0, (x, d)
    return (xr // n, xi // n)

def gquo_round(x, d):
    n = gnorm(d)
    xr = x[0] * d[0] + x[1] * d[1]
    xi = x[1] * d[0] - x[0] * d[1]
    return ((2 * xr + n) // (2 * n), (2 * xi + n) // (2 * n))

def par(z):
    """Z[i] -> F2, the reduction mod (1+i): a+bi |-> (a+b) mod 2 (ring
    homomorphism)."""
    return (z[0] + z[1]) & 1

def sig8(w):
    return (w[4], w[5], w[0], w[1], w[2], w[3], w[6], w[7])

def z_basis_L():
    B = []
    for i in range(6):
        w = [0] * 8
        w[i], w[i + 1] = 2, -2
        B.append(tuple(w))
    w = [0] * 8
    w[6], w[7] = 2, 2
    B.append(tuple(w))
    B.append(tuple([1] * 8))
    return B

def pack(w):
    """Z^8 -> Z[i]^4 via the J-pairing (then J = mult by i, exactly)."""
    return tuple((w[2 * k], w[2 * k + 1]) for k in range(4))

def unpack(z):
    out = []
    for a, b in z:
        out.extend([a, b])
    return tuple(out)

def zi_hnf(rows):
    """Z[i]-Hermite normal form (row style) of a rank-4 generator list in
    Z[i]^4: returns 4 upper-triangular rows (Euclidean gquo_round)."""
    M = [list(r) for r in rows]
    out = []
    for col in range(4):
        pool = [r for r in M if any(r[c] != (0, 0) for c in range(col, 4))]
        M = pool
        while True:
            nz = [r for r in M if r[col] != (0, 0)]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: gnorm(r[col]))
            piv = nz[0]
            for r in nz[1:]:
                q = gquo_round(r[col], piv[col])
                for c in range(4):
                    r[c] = gsub(r[c], gmul(q, piv[c]))
        nz = [r for r in M if r[col] != (0, 0)]
        assert len(nz) == 1, "rank defect in Z[i]-HNF"
        out.append(list(nz[0]))
        M = [r for r in M if r is not nz[0]]
    return out

class Lmodule:
    """L as the free module Z[i]^4 via an explicit triangular Z[i]-basis
    (rows of self.M, in packed Z^8 = Z[i]^4 ambient coordinates)."""

    def __init__(self):
        gens = [list(pack(b)) for b in z_basis_L()]
        self.M = zi_hnf(gens)
        idx = 1
        for k in range(4):
            idx *= gnorm(self.M[k][k])
        self.index = idx

    def to_ambient(self, y):
        """L-coords y (Z[i]^4) -> ambient packed vector sum y_k m_k."""
        out = [(0, 0)] * 4
        for k in range(4):
            for c in range(4):
                out[c] = gadd(out[c], gmul(y[k], self.M[k][c]))
        return tuple(out)

    def coords(self, z):
        """ambient packed vector -> L-coords (asserts membership)."""
        z = list(z)
        y = [(0, 0)] * 4
        for k in range(4):
            y[k] = gquo_exact(z[k], self.M[k][k])
            for c in range(4):
                z[c] = gsub(z[c], gmul(y[k], self.M[k][c]))
        assert all(c == (0, 0) for c in z)
        return tuple(y)

    def w_coords(self, w):
        return self.coords(pack(w))

    def class_of_w(self, w):
        return tuple(par(c) for c in self.w_coords(w))

ALL_V = [tuple((n >> k) & 1 for k in range(4)) for n in range(16)]
