"""Exact actual-stress TT inverse-Laplacian locality checks; no repository imports."""
from fractions import Fraction as F
from itertools import product
import json
import sympy as s


class Lattice:
    def __init__(self, lengths=(3, 3, 6)):
        assert lengths in ((3, 3, 6), (6, 6, 6))
        self.lengths = lengths
        self.sites = list(product(*(range(n) for n in lengths)))
        self.size = len(self.sites)
        self.K = s.QQ.algebraic_field(s.I, s.sqrt(3))
        K = self.K
        omega = K.from_sympy((-1 + s.I*s.sqrt(3))/2)
        sixth_root = K.from_sympy((1 + s.I*s.sqrt(3))/2)
        self.roots = tuple(omega if n == 3 else sixth_root for n in lengths)
        self.modes = self.sites
        self.phases = {}
        for k in self.modes:
            self.phases[k] = {x: product_field(K, [self.roots[i] ** (-(k[i]*x[i])) for i in range(3)]) for x in self.sites}

    def step(self, x, i, shift=1):
        y = list(x)
        y[i] = (y[i] + shift) % self.lengths[i]
        return tuple(y)

    def zero(self):
        return {x: F(0) for x in self.sites}

    def stress(self, phi):
        def G(x, i):
            return phi[self.step(x, i)] - phi[x]
        out = {}
        for x in self.sites:
            diag = [G(x,i)*G(self.step(x,i,-1),i)/2-sum((G(x,j)**2+G(self.step(x,j,-1),j)**2)/4 for j in range(3) if j != i) for i in range(3)]
            off = [(G(x,i)+G(self.step(x,j),i))*(G(x,j)+G(self.step(x,i),j))/4 for i,j in ((1,2),(0,2),(0,1))]
            out[x] = diag + off
        return out

    def variation(self, phi, delta):
        combined = self.stress({x: phi[x]+delta[x] for x in self.sites})
        base, change = self.stress(phi), self.stress(delta)
        return {x: [combined[x][j]-base[x][j]-change[x][j] for j in range(6)] for x in self.sites}

    def transform(self, source):
        K = self.K
        nonzero = [[(x,K.convert(source[x][j])) for x in self.sites if source[x][j] != 0] for j in range(6)]
        return {k: [sum((value*self.phases[k][x] for x,value in nonzero[j]), K.zero) for j in range(6)] for k in self.modes}

    def pair_fourier(self, left, right):
        """<left, P_TT ell^-1 right>, raw tensor coords weighted (1,1,1,2,2,2)."""
        K = self.K
        total = K.zero
        for k in self.modes:
            if k == (0,0,0):
                continue
            minus_k = tuple((-k[i]) % self.lengths[i] for i in range(3))
            zz = [self.roots[i] ** k[i] for i in range(3)]
            dd = [z-1 for z in zz]
            dc = [z**-1-1 for z in zz]
            r2 = sum((2-z-z**-1 for z in zz), K.zero)
            # Conjugated left transform comes from opposite momentum: real sources.
            a, b = left[minus_k], right[k]
            def divergence(j, conjugate=False):
                d = dc if conjugate else dd
                # dminus=1-z^-1=-conjugate(dplus).
                dm = [-v for v in (dd if conjugate else dc)]
                return [d[0]*j[0]+dm[2]*j[4]+dm[1]*j[5],
                        d[1]*j[1]+dm[2]*j[3]+dm[0]*j[5],
                        d[2]*j[2]+dm[1]*j[3]+dm[0]*j[4]]
            va, vb = divergence(a, True), divergence(b)
            norm_pair = sum((a[j]*b[j]*(1 if j<3 else 2) for j in range(6)), K.zero)
            div_pair = sum((va[j]*vb[j] for j in range(3)), K.zero)
            da = sum((dd[j]*va[j] for j in range(3)), K.zero)
            db = sum((dc[j]*vb[j] for j in range(3)), K.zero)
            sa, sb = da-r2*sum(a[:3]), db-r2*sum(b[:3])
            total += norm_pair/r2-2*div_pair/r2**2+da*db/r2**3-sa*sb/(2*r2**3)
        return s.simplify(K.to_sympy(total/self.size))

    def pair(self, left, right):
        return self.pair_fourier(self.transform(left), self.transform(right))


def product_field(K, entries):
    result = K.one
    for v in entries:
        result *= v
    return result


def main():
    lat = Lattice()
    profile = (F(1), F(-1), F(0))
    phi = {x: profile[x[0]] for x in lat.sites}
    base_stress = lat.stress(phi)
    assert lat.pair(base_stress,base_stress) == 0
    x, y = (0,0,0), (0,0,3)
    dx, dy = lat.zero(), lat.zero()
    dx[x], dy[y] = F(1), F(1)
    jx, jy = lat.variation(phi, dx), lat.variation(phi, dy)
    second = lat.variation(dx, dy)
    assert all(v == 0 for values in second.values() for v in values)
    hxy = lat.pair(jx, jy)
    assert hxy.is_Rational and hxy != 0

    # Independent projector controls using REALSPACE local complement and a
    # genuine TT tensor. These detect staggered phase or offdiagonal weight errors.
    v = {z: [F(int(z == (0,0,0))), F(2*int(z == (1,0,0))), F(-int(z == (0,1,0)))] for z in lat.sites}
    complement = {}
    for z in lat.sites:
        diag = [v[lat.step(z,i,-1)][i]-v[z][i] for i in range(3)]
        off = [-(v[lat.step(z,j)][i]-v[z][i]+v[lat.step(z,i)][j]-v[z][j])/2 for i,j in ((1,2),(0,2),(0,1))]
        complement[z] = diag+off
    assert lat.pair(complement, complement) == 0
    assert lat.pair(complement, jx) == 0
    trace_source = {z: [F(int(z == (0,0,0)))]*3+[F(0)]*3 for z in lat.sites}
    assert lat.pair(trace_source, trace_source) == 0
    cosine = (F(1),F(1,2),F(-1,2),F(-1),F(-1,2),F(1,2))
    tt_source = {z: [cosine[z[2]],-cosine[z[2]],F(0),F(0),F(0),F(0)] for z in lat.sites}
    assert lat.pair(tt_source,tt_source) == 54  # ||source||^2 / ell(k_z), ell=1.

    def energy_at(configuration):
        stress = lat.stress(configuration)
        return lat.pair(stress,stress)/2
    # Exact four-energy difference: no mixed stress term at this separation,
    # so all odd-odd quartic terms except delta_x delta_y are absent.
    four_energy = sum(sign_x*sign_y*energy_at({z: phi[z]+sign_x*dx[z]+sign_y*dy[z] for z in lat.sites})
                      for sign_x,sign_y in product((-1,1), repeat=2))/4
    assert four_energy == hxy

    # Collective plane derivatives are finite-support sums over nine sites.
    da = {z: profile[z[0]] if z[2] == 0 else F(0) for z in lat.sites}
    db = {z: profile[z[0]] if z[2] == 3 else F(0) for z in lat.sites}
    assert all(v == 0 for values in lat.variation(da,db).values() for v in values)
    plane_hessian = lat.pair(lat.variation(phi,da), lat.variation(phi,db))
    assert plane_hessian.is_Rational and plane_hessian != 0

    # Homogeneous free-matter momentum J_i=-pi^T D_i^c phi:
    # {J_i,R}=dR(phi)[D_i^c phi] at pi=0, q=pTT=0.
    amplitudes = (F(1), F(2), F(-1), F(0), F(1), F(0))
    moving_phi = {z: profile[z[0]]*amplitudes[z[2]] for z in lat.sites}
    sigma = lat.stress(moving_phi)
    derivatives = {}
    for i in range(3):
        direction = {z: (moving_phi[lat.step(z,i)]-moving_phi[lat.step(z,i,-1)])/2 for z in lat.sites}
        derivatives[i] = lat.pair(sigma, lat.variation(moving_phi,direction))
    assert any(v != 0 for v in derivatives.values())
    assert all(v.is_Rational for v in derivatives.values())
    assert derivatives[2] == -s.Rational(568433,87808)
    # Genuine lattice translations still preserve R; infinitesimal central
    # differences are not their one-parameter canonical generator.
    energy = lat.pair(sigma, sigma)/2
    translated = {z: moving_phi[lat.step(z,2)] for z in lat.sites}
    translated_stress = lat.stress(translated)
    assert lat.pair(translated_stress, translated_stress)/2 == energy
    # Free matter energy has zero variation under D_i^c (periodic skewness).
    for i in range(3):
        direction = {z: (moving_phi[lat.step(z,i)]-moving_phi[lat.step(z,i,-1)])/2 for z in lat.sites}
        mass_variation = sum(moving_phi[z]*direction[z] for z in lat.sites)
        gradient_variation = sum((moving_phi[lat.step(z,j)]-moving_phi[z])*(direction[lat.step(z,j)]-direction[z]) for z in lat.sites for j in range(3))
        assert mass_variation == gradient_variation == 0
    # Exact nonzero infrared residue for the actual 3x3 transverse profile.
    uniform_amplitude_variation = lat.variation(phi,phi)
    diagonal_jacobian = [[uniform_amplitude_variation[(ix,0,0)][j] for ix in range(3)] for j in range(3)]
    assert diagonal_jacobian == [[F(-2),F(-2),F(1)], [F(-5,2),F(-5,2),F(-1)], [F(-5,2),F(-5,2),F(-1)]]
    means = [sum(row)/3 for row in diagonal_jacobian]
    residue = 9*(means[0]-means[1])**2/2
    assert residue == F(9,2)
    normalized_residue = residue/(3*sum(v*v for v in profile))
    assert normalized_residue == F(3,4)
    cubic = Lattice((6,6,6))
    cubic_phi = {z: profile[z[0] % 3] for z in cubic.sites}
    cubic_dx, cubic_dy = cubic.zero(), cubic.zero()
    cubic_dx[x], cubic_dy[y] = F(1), F(1)
    cubic_hessian = cubic.pair(cubic.variation(cubic_phi,cubic_dx), cubic.variation(cubic_phi,cubic_dy))
    assert cubic_hessian.is_Rational and cubic_hessian != 0
    assert all(v == 0 for values in cubic.variation(cubic_dx,cubic_dy).values() for v in values)
    cubic_moving_phi = {z: profile[z[0] % 3]*amplitudes[z[2]] for z in cubic.sites}
    cubic_direction = {z: (cubic_moving_phi[cubic.step(z,2)]-cubic_moving_phi[cubic.step(z,2,-1)])/2 for z in cubic.sites}
    cubic_sigma = cubic.stress(cubic_moving_phi)
    cubic_Jz_R = cubic.pair(cubic_sigma,cubic.variation(cubic_moving_phi,cubic_direction))
    assert cubic_Jz_R == 4*derivatives[2] == -s.Rational(568433,21952)
    print(json.dumps({"status":"PASS", "lattice":lat.lengths,
                      "onsite_x":x,"onsite_y":y,"graph_distance":3,
                      "actual_R_mixed_hessian":str(hxy),
                      "four_energy_mixed_difference":str(four_energy),
                      "projector_trace_longitudinal_TT_controls":True,
                      "plane_R_mixed_hessian":str(plane_hessian),
                      "unnormalized_3x3_plane_inverse_laplacian_residue":str(residue),
                      "canonically_normalized_plane_residue":str(normalized_residue),
                      "strict_cubic_6x6x6_onsite_R_hessian":str(cubic_hessian),
                      "strict_cubic_6x6x6_Jz_R_bracket":str(cubic_Jz_R),
                      "moving_background_profile_x":[1,-1,0],
                      "moving_background_amplitudes_z":[1,2,-1,0,1,0],
                      "R_moving_background":str(energy),
                      "J_i_R_brackets":{str(i):str(v) for i,v in derivatives.items()},
                      "discrete_translation_invariance":True,
                      "free_matter_central_difference_invariance":True,
                      "scope":"Exact finite witness; see proof for all-size locality and operational caveats."},indent=2))


if __name__ == "__main__":
    main()
