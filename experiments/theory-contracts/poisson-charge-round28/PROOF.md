# Poisson-resummed full charge sum and a certified regulated partition

2026-09-07. NON-RH, unpromoted research. This is a deliberately specified
**subcase**, not a solution of the arbitrary-coupling scalar/charge model.
The scalar decouples: g=u=0. Sections 1-5 first set nu=0; Section 6 also
evaluates a genuine nonzero spatial charge-gradient coupling nu=1/486.
Charge hopping remains nonzero, with the
original eight channels, the original cocycle, all integer charges, and
the original additive hopping constant. No fitted physical parameter is used.

## 1. The precise quantity evaluated

Use the primitive symmetric transfer Q and neutral sector of
[Round27](../full-reference-control-round27/PROOF.md), with L=T=3,
N=27, a=m=beta=1, delta=1/3 and J=1/2592. Thus

    D(n) = (1/(2N)) sum_x n_x^t G n_x,
    H_hop = 48NJ I - J A_sign, theta=48 beta N J=1/2,
    Z = Tr_neutral Q^3.

This is a finite spatial and Euclidean-time regulator, not the unsliced
heat trace. Every site's charge is still in Z^8, subject only to total
charge zero; the scalar coordinates remain in R^27. Z is not a zero-charge
profile contribution or a finite charge-box trace.

At u=0 scalar and charge factors separate exactly. The charge factor is
the trace of a noncommuting hopping/diagonal transfer; it has NOT become
an independent product over sites. Its negative E8 four-hop loop survives.

## 2. Sum every initial charge before summing closed words

For a tuple of slice words whose total displacement closes, write the
sampled profiles as n+s_j, j=1,...,T. Each s_j has total charge zero.
The cocycle exponent is affine in the initial n. Its n-dependent part
at each site is beta_cocycle(sum of local displacements,n_x), which vanishes
for a closed word by bilinearity. The remaining phase epsilon_word is the
actual product obtained by starting at zero, not a sign assigned afterwards.

Write the neutral lattice basis as L0=[I_(N-1); -1^t], so n=L0 z and
z is in Z^(8(N-1)). Set sbar=(1/T)sum_j s_j and b=(sbar_1,...,sbar_(N-1)).
Completion of the square gives the fixed-word charge sum

    epsilon_word exp(-c_word) sum_z exp[-(z+b)^t Qc (z+b)/2],
    c_word = delta/(2N) sum_j ||s_j-sbar||_G^2 >= 0,
    Qc = (beta/N) (I_(N-1)+11^t) tensor G.

The Gram matrix is exactly the repository's matrix: diagonal (4,2,2,2,2,2,2,2),
determinant 1. Its basis is 2e_1, e_1+e_2,...,e_1+e_7, (1,...,1)/2.
These vectors lie in D8 union (D8+(1,...,1)/2), the E8 lattice, and their
covolume is 1. Hence their integer span is E8, and its dual is also E8.
In particular the first hopping channel is NOT a norm-two root.

Poisson summation for this positive Gaussian gives

    C0 exp(-c_word) epsilon_word (1 + dual remainder),
    C0=(2 pi N/beta)^(4(N-1))/N^4,
    dual remainder = sum_(m != 0) exp(-2 pi^2 m^t Qc^-1 m)
                                     exp(2 pi i m^t b).

The sign of the Fourier phase is immaterial after pairing m and -m. The
determinant factor N^4 is essential: det(I+11^t)=N, repeated eight times.
For dual vectors p_1,...,p_(N-1) in E8 and p_N=0,

    m^t Qc^-1 m = (1/beta) sum_(i<j) ||p_i-p_j||^2.

This follows from (I+11^t)^-1=I-11^t/N and the complete-graph identity.
Drop the nonnegative terms with i,j<N, keeping the N-1 edges to p_N=0.
Uniformly in EVERY shift b and thus in every closed word,

    |dual remainder| <= eta(beta,N)
       := Theta_E8(2 pi^2/beta)^(N-1)-1.

The classical E8 theta identity is

    Theta_E8(t)=1+240 sum_(k>=1) sigma_3(k) exp(-2tk).

Since sigma_3(k)=k^3 sum_(d|k) d^-3 < 2 k^3, and
sum k^3 q^k=q(1+4q+q^2)/(1-q)^4, an explicit upper bound is

    eta <= [1+480 q(1+4q+q^2)/(1-q)^4]^(N-1)-1,
    q=exp(-4 pi^2/beta).

For beta=1, pi>157/50 implies 4 pi^2>39; e>8/3 implies
q<(3/8)^39. At N=27 the checker proves with rational arithmetic
eta < 3.1*10^-13. This bound includes the entire nonzero dual lattice,
not a finite dual sample. No charge cutoff K is introduced.

Poisson summation and the E8 theta identity are standard, not discoveries
of this project; see [Elkies, lattice theta lectures](https://abel.math.harvard.edu/~elkies/M272.19/sep23.pdf)
and the [explicit coefficient derivation in the MIT theta notes](https://math.mit.edu/~brubaker/Math784/thetafunctions.pdf).
The neutral-site determinant, word-shift bound, and present operator
application are derived here. The arithmetic coefficient formula can also
be read as the weight-four Eisenstein series with q=exp(-2t).

## 3. All closed words through total order three

There are 81 undirected spatial edges on the L3 torus, hence 162 directed
edges per channel. At order two a closed word consists of a hop and its
inverse. There are 1296 such ordered words, all with phase +1.
At order three charge conservation in the independent channel basis
requires one channel throughout and a directed spatial triangle. The torus
has 27 triangles, so there are 27*8*2*3!=2592 ordered closed words.
Their original cocycle phase is +1. No one-hop word closes.

The expansion weight for a slice allocation (k1,k2,k3) is
(delta J)^k/(k1! k2! k3!). For channel p let ell_p=G_pp, and define

    f2_p = exp[-2 ell_p/(9N)], f3_p = exp[-ell_p/(3N)].

Completion of the square in Section 2 and all slice allocations give

    F = 1 + (delta J)^2 sum_p 6N [3/2 + 3 f2_p]
          + (delta J)^3 sum_p 12N [1/2 + 3 f2_p + f3_p].

Two hops in one slice contribute 3/2 and have c_word=0. Two occupied
slices contribute 3 f2_p. For three hops the cases of one, two and three
occupied slices contribute respectively 1/2, 3 f2_p and f3_p. The checker
independently applies the original move function to 104 representative
ordered words and all 1008 slice allocations, then compares their exact
cost/weight histograms with this formula. Spatial counts are enumerated
on the actual 27-site torus. Translation equivalence, NOT independent
execution of 3888 full-lattice words, supplies the multiplicities.

## 4. The scalar factor is exact and rational here

The spatial squared frequencies are lambda=1,4,7,10 with multiplicities
1,6,12,8. For one frequency the normalized primitive T3 Gaussian trace is

    det(L_C3+delta^2 lambda I)^(-1/2)
      = [delta sqrt(lambda)(3+delta^2 lambda)]^-1
      = 27/[sqrt(lambda)(lambda+27)].

This retains the Gaussian heat-kernel normalization; there is no spurious
(2 pi)^(NT/2) or delta power. Since the nontrivial multiplicities are even,

    Zphi = 27^27 / product_lambda [(lambda+27)^mult lambda^(floor(mult/2))]

is a rational number. This formula applies only to this free scalar
subcase and these regulator values, not to the full history-dependent
determinants at u>0.

## 5. A rigorous enclosure for the whole partition, including omitted signs

Set B=exp(-theta) C0 Zphi, R=Z/B. The complete charge-diagonal reference
at zero shift satisfies

    C0 Zphi <= Z_D <= (1+eta) C0 Zphi.

The lower inequality follows because every nonzero dual term at b=0 is
positive. The Round27 pinching theorem therefore gives R>=1. Its absolute
word bound gives for the tail of total order k>=4

    |tail|/B <= (1+eta) h,
    h=sum_(k>=4) theta^k/k! <= theta^4/[24(1-theta/5)]=5/1728.

All retained coefficients are positive, so their zero-dual approximation
error is at most eta F. Consequently

    |R-F| <= eta F + (1+eta) h =: error.

The original negative four-hop loop is inside this rigorously bounded
tail; it is not declared absent, set to zero without error control, or
converted into a positive matrix. All higher words and initial profiles
are included through the absolute bound. This is a controlled expansion,
not an exact finite polynomial for Z.

The checker encloses pi using Machin's identity and rational alternating
arctangent series. It encloses each exp(-x), 0<=x<=1, by two adjacent
alternating Taylor partial sums. Products, powers, comparisons, and output
rounding use exact integer fractions. With F in [Flo,Fhi] and B in [Blo,Bhi],
take error=eta Fhi+(1+eta)h and return

    Z in [Blo(Flo-error), Bhi(Fhi+error)].

The rounded displayed midpoint is checked against both endpoints. Its
relative error against EVERY positive Z in this interval is less than
0.3 percent. Thus the new result is an actually evaluated, complete
infinite-charge regulated partition with an explicit error budget in
this declared subcase, not merely a cutoff-existence theorem.

## 6. Nonzero spatial charge interaction is also evaluated

Keep the same regulator, scalar mass and J, but now set **nu=1/486 > 0**.
The original diagonal charge operator becomes

    D_nu(n) = (1/2) n^t [B_nu tensor G] n,
    B_nu = (1/N)I + nu L_space.

There is a genuine spatial interaction between charges, in addition to
the original signed hopping. No onsite/product replacement is made.
The scalar still decouples because u=0; this does not solve its coupling
to charge. The Gaussian completion and initial-profile phase argument
remain unchanged, but now use the B_nu metric:

    Qc_nu = [L0^t B_nu L0] tensor G,
    c_word,nu = delta/2 sum_j ||s_j-sbar||_(B_nu tensor G)^2,
    C0_nu = (2 pi)^104 / det(L0^t B_nu L0)^4.

The actual spatial Laplacian spectrum is 0,3,6,9 with multiplicities
1,6,12,8. The integer neutral basis has Gram determinant N=27, so

    det(L0^t B_nu L0)
       = 27 (1/27+3nu)^6 (1/27+6nu)^12 (1/27+9nu)^8.

This is checked independently using the full 26-dimensional neutral
matrix and the directly constructed 27-site Laplacian. The zero mode
is omitted from the product because total charge is fixed, not because
the Hilbert space is replaced by a finite sample.

Since B_nu <= (1+9Nnu)B_0, the inverse Gaussian matrix satisfies
Qc_nu^-1 >= Qc_0^-1/(1+9Nnu). Set A=1+9Nnu=3/2. The uniform theta-tail
argument therefore works with q=exp(-4 pi^2/A) < (3/8)^26. Its certified
bound is eta < 1.1*10^-7, still small enough for the same partition budget.

Every retained two- or three-hop profile is neutral on one of the spatial
triangles. On that support the principal spatial Laplacian is 7I-11^t.
Consequently all retained completion costs are multiplied exactly by

    1+7Nnu = 25/18.

Use f2_p^(25/18) and f3_p^(25/18) in F, the new C0_nu and eta, and the
unchanged all-word tail h=5/1728. The same argument as Section 5 encloses
the **whole** original partition at this nonzero coupling with less than
0.3 percent relative error, including rational transcendental and display
error. Its numerical interval is separately recorded in validation.json;
it is not substituted for the nu=0 example or presented as the same number.

## 7. What remains open

The method is especially effective at beta=1 and theta=1/2. Here J is
explicitly chosen small; it is not a coupling derived from TFPT or fitted
to nature. No complexity claim at fixed J and increasing volume follows.
The large entropy factor C0 is evaluated analytically, not removed from Z.

At u>0 the scalar and charge variables no longer separate; after fixing a
scalar trajectory, the Poisson quadratic form depends on that unbounded
trajectory. The uniform tiny dual remainder above cannot simply be
reused. The nonzero-nu construction above handles its quadratic form at
the specified value, not efficient evaluation at arbitrary large nu.
Large total hopping requires higher signed word orders. These, an
interacting continuum, real-time reconstruction, a selected common
microscopic parent, chiral completion and gravity remain open. The
argument is written mathematics with exact regression code, not an
independent proof-assistant certificate or empirical validation.
