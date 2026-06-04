# Chapter 10 — Identical Particles

## TL;DR

- One symmetry requirement, and the periodic table falls out.
- Identical particles in quantum mechanics are truly indistinguishable: no continuous worldlines, no paint dots, no way to tell particle 1 from particle 2 in principle. The wave function must transform simply under exchange, and the only options are $+1$ (bosons) or $-1$ (fermions).
- The antisymmetric wave function for $N$ fermions is a Slater determinant. Pauli exclusion is a theorem about determinants: two identical columns make it zero.
- The helium spectrum splits into parahelium ($S=0$) and orthohelium ($S=1$) because the Coulomb energy depends on whether the spatial wave function is symmetric or antisymmetric — via the exchange integral $K$, which has no classical analog.
- Hund's first rule is a corollary of antisymmetry, not a separate postulate. So is Pauli exclusion. The periodic table is a theorem about determinants and screened Coulomb potentials.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Explain** (Understand) why quantum-mechanical indistinguishability is a structural constraint, not a practical limitation, and what follows from $[\hat{H}, \hat{P}_{12}] = 0$.
2. **Construct** (Apply) the antisymmetric two-electron wave function and extend it to the $N$-particle Slater determinant.
3. **Derive** (Apply) the Pauli exclusion principle as a property of determinants with identical columns.
4. **Compute** (Analyze) the first-order Coulomb energy splitting $2K$ for the helium 1s2s configuration, identifying the direct ($J$) and exchange ($K$) integrals and explaining why $K > 0$.
5. **Apply** (Evaluate) the composite-particle counting rule to determine whether a given particle is a boson or fermion, and explain the macroscopic consequences (BEC, degeneracy pressure).

---

## Two Families, One Element

Spectroscopists in the early 1920s catalogued the helium spectrum in fine detail. There were two distinct families of spectral lines — one called parahelium, one called orthohelium — with different transition rates, different selection rules, different fine-structure patterns. They looked like spectra of two different elements.

Helium is helium: one nuclear charge of $+2e$, two electrons, one element. It is not two elements. So why two spectral families?

Werner Heisenberg resolved this in 1926. The resolution did not require a new force or a new particle. It required asking a question nobody had thought to ask: when you write down a wave function for two electrons, what does it have to satisfy just from the fact that the electrons are identical?

The answer to that question is what this chapter is about.

---

## What "Identical" Means, and Why It Matters

In classical mechanics, two identical billiard balls can always be tracked individually. Even without painting a dot on one, you could in principle follow both balls through every collision, because their trajectories are continuous. You never lose track of "ball 1" because "ball 1" always has a definite position and velocity.

In quantum mechanics this fails. The wave function $\psi(\vec{r}_1, \vec{r}_2)$ for two electrons spreads each of them over a region of space. The regions overlap. When a detector fires at some position, there is no fact — not just no practical way to determine, but no fact in nature — about which electron triggered it. The labels "1" and "2" we write into the wave function are mathematical bookkeeping: indices on a function. They cannot be cashed out by any measurement in principle.

The Hamiltonian for two identical particles confirms this. For two electrons:

$$\hat{H}(1,2) = \frac{\hat{p}_1^2}{2m_e} + \frac{\hat{p}_2^2}{2m_e} + V(\vec{r}_1) + V(\vec{r}_2) + \frac{e^2}{4\pi\epsilon_0|\vec{r}_1 - \vec{r}_2|}.$$

Swap the subscripts 1 and 2 everywhere: the Hamiltonian is unchanged. $\hat{H}(1,2) = \hat{H}(2,1)$. The physics literally does not distinguish the two labels.

Define the **exchange operator**:

$$\hat{P}_{12}\,\psi(\vec{r}_1, \vec{r}_2) \equiv \psi(\vec{r}_2, \vec{r}_1).$$

Apply it twice: $\hat{P}_{12}^2\,\psi = \hat{P}_{12}\psi(\vec{r}_2, \vec{r}_1) = \psi(\vec{r}_1, \vec{r}_2)$, so $\hat{P}_{12}^2 = \mathbb{1}$. The eigenvalues $\lambda$ of $\hat{P}_{12}$ satisfy $\lambda^2 = 1$, giving only $\lambda = +1$ or $\lambda = -1$.

Since $\hat{H}(1,2) = \hat{H}(2,1)$, we have $[\hat{H}, \hat{P}_{12}] = 0$. The exchange operator commutes with the Hamiltonian. Therefore: (i) energy eigenstates can be chosen to have definite exchange symmetry; (ii) once a state has definite exchange symmetry, it keeps it under time evolution — the symmetry is conserved.

The empirical fact — elevated to a postulate in non-relativistic quantum mechanics — is:

- **Bosons**: $\hat{P}_{12}\psi = +\psi$ (symmetric under exchange). Integer spin: photons, the Higgs boson, $^4$He atoms.
- **Fermions**: $\hat{P}_{12}\psi = -\psi$ (antisymmetric under exchange). Half-integer spin: electrons, protons, neutrons.

The connection between spin and statistics — why integer spin forces bosons and half-integer forces fermions — is the **spin-statistics theorem**, proven by Pauli in 1940 using the requirement of microcausality in relativistic quantum field theory. [verify] The proof is not available to us here. We accept it as an empirical fact and note where the deeper explanation lies.

**Composite particles** inherit their statistics by counting constituent fermions: an even number of constituent fermions makes a boson, an odd number makes a fermion. The consequences are dramatic:

- $^4$He: 2 protons + 2 neutrons + 2 electrons = 6 fermions (even) → boson → superfluid at 2.17 K.
- $^3$He: 5 fermions (odd) → fermion → superfluid only at 2.5 mK, requiring Cooper pairs.

Three orders of magnitude in temperature, from a single parity count.

| Particle | Spin | Constituent fermions | Statistics | Key consequence |
|---|---|---|---|---|
| Photon | 1 | 0 (gauge boson) | Boson | Laser (macroscopic occupation of one mode) |
| Electron | 1/2 | 1 | Fermion | Pauli exclusion; chemistry |
| Proton | 1/2 | 3 (quarks) | Fermion | Pauli exclusion in nuclei |
| $^4$He | 0 | 6 | Boson | BEC; superfluid at 2.17 K |
| $^3$He | 1/2 | 5 | Fermion | Superfluid only at 2.5 mK |
| $^{87}$Rb | integer | 87 (even) | Boson | First dilute-gas BEC (Cornell, Wieman, 1995) |

---

## Antisymmetry Built into the Wave Function

For two identical fermions occupying single-particle states $\phi_a$ and $\phi_b$, the antisymmetric wave function is:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)\bigr].$$

Check: $\hat{P}_{12}\psi_-(1,2) = \psi_-(2,1) = -\psi_-(1,2)$. Antisymmetric by inspection.

John Slater noticed in 1929 that this can be written as a $2 \times 2$ determinant:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\det\begin{pmatrix}\phi_a(1) & \phi_b(1) \\ \phi_a(2) & \phi_b(2)\end{pmatrix}.$$

Swapping particles swaps rows. Swapping rows flips the sign of a determinant. Antisymmetry is now a property of the matrix structure — the algebra enforces it automatically.

![Visual derivation of the 2×2 Slater determinant: swapping particle labels swaps rows, and swapping rows multiplies the determinant by −1](../images/11-identical-particles-fig-01.png)
*Figure 10.1 — The antisymmetry of $\psi_-(1,2)$ is a consequence of matrix algebra, not a separately imposed constraint.*

The construction extends to $N$ fermions. Write an $N \times N$ matrix where entry $(i,j)$ is the $i$-th single-particle orbital evaluated at the $j$-th particle's coordinates. The **Slater determinant** is:

$$\psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}} \det\begin{pmatrix} \phi_1(1) & \phi_2(1) & \cdots & \phi_N(1) \\ \phi_1(2) & \phi_2(2) & \cdots & \phi_N(2) \\ \vdots & & \ddots & \vdots \\ \phi_1(N) & \phi_2(N) & \cdots & \phi_N(N) \end{pmatrix}.$$

Swapping any two particles swaps two rows and flips the sign — antisymmetric under any pairwise exchange. The $1/\sqrt{N!}$ is the normalization (the $N!$ terms in the determinant expansion are all orthogonal when the $\phi_i$ are orthonormal).

For $N = 3$, the determinant expands to six terms with alternating signs, one for each permutation of three particle labels weighted by the sign of that permutation:

$$\psi(1,2,3) = \frac{1}{\sqrt{6}}\Bigl[\phi_1(1)\phi_2(2)\phi_3(3) - \phi_1(1)\phi_3(2)\phi_2(3) + \phi_2(1)\phi_3(2)\phi_1(3) - \phi_2(1)\phi_1(2)\phi_3(3) + \phi_3(1)\phi_1(2)\phi_2(3) - \phi_3(1)\phi_2(2)\phi_1(3)\Bigr].$$

This is the wave function ansatz on which all of computational quantum chemistry is built. Hartree-Fock theory minimizes $\langle\psi|\hat{H}|\psi\rangle$ over the choice of single-particle orbitals $\{\phi_i\}$, with the $N$-electron wave function constrained to be a single Slater determinant. Configuration interaction, coupled-cluster theory, and many density-functional approaches are corrections to or generalizations of this starting point.

---

## Pauli Exclusion as a Corollary

Here is the key move. Suppose two of the single-particle orbitals are identical: $\phi_i = \phi_j$ for some $i \neq j$. Then two columns of the Slater determinant are identical. A determinant with two identical columns is exactly zero.

Not approximately zero. Not zero in some limit. Identically zero, everywhere in configuration space.

A wave function that is identically zero cannot be normalized: $\int 0\,d^Nr = 0 \neq 1$. It is not a state. Two fermions simply cannot occupy the same single-particle orbital — the wave function you would write down to represent that situation does not exist.

This is the **Pauli exclusion principle**. Wolfgang Pauli stated it in 1925 as an empirical rule — no two electrons in an atom can share the same quantum numbers $(n, \ell, m_\ell, m_s)$ — because it explained the periodic table and he could not find a reason to reject it. He received the Nobel Prize in 1945 partly for it. But as he stated it, the rule was a phenomenological postulate with no derivation. Slater showed four years later that it is a theorem about determinants, not an independent postulate.

The deeper form matters. The quantum numbers $(n, \ell, m_\ell, m_s)$ are labels for single-particle hydrogenic orbitals, specific to atoms. When you move to a solid-state system, the relevant labels become band indices and crystal momenta — different labels, same physics. The antisymmetry-based form survives unchanged in both contexts.

---

## Worked Example: Building the Antisymmetric Two-Electron State

**The lesson:** construct $\psi_-(1,2)$ for two electrons and show directly that Pauli exclusion is a theorem about determinants.

**Setup.** Let electron 1 have coordinates $(\vec{r}_1, m_{s1})$ and electron 2 have coordinates $(\vec{r}_2, m_{s2})$. Define the spin-orbital — spatial orbital times spin state:

$$\phi_A(\vec{r}, m_s) = \psi_{100}(\vec{r})\cdot\chi_\uparrow(m_s), \qquad \phi_B(\vec{r}, m_s) = \psi_{100}(\vec{r})\cdot\chi_\downarrow(m_s).$$

Both electrons are in the 1s spatial orbital, but with opposite spin projections.

**Step 1: Write the Slater determinant.**

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\det\begin{pmatrix}\phi_A(1) & \phi_B(1)\\\phi_A(2) & \phi_B(2)\end{pmatrix} = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_B(2) - \phi_B(1)\phi_A(2)\bigr].$$

**Step 2: Expand.**

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\psi_{100}(\vec{r}_1)\chi_\uparrow(m_{s1})\cdot\psi_{100}(\vec{r}_2)\chi_\downarrow(m_{s2}) - \psi_{100}(\vec{r}_1)\chi_\downarrow(m_{s1})\cdot\psi_{100}(\vec{r}_2)\chi_\uparrow(m_{s2})\bigr].$$

$$= \psi_{100}(\vec{r}_1)\psi_{100}(\vec{r}_2)\cdot\frac{1}{\sqrt{2}}\bigl[\chi_\uparrow(m_{s1})\chi_\downarrow(m_{s2}) - \chi_\downarrow(m_{s1})\chi_\uparrow(m_{s2})\bigr].$$

The spatial part is symmetric ($\psi_{100}$ is the same function at both positions); the spin part is antisymmetric — the spin singlet $|S=0, M_S=0\rangle$ from Chapter 8. Total wave function: symmetric spatial times antisymmetric spin = antisymmetric total. ✓

**Step 3: Attempt to put both electrons in the same spin-orbital.** Suppose we try $\phi_A = \phi_B = \psi_{100}\chi_\uparrow$. Then:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_A(2) - \phi_A(1)\phi_A(2)\bigr] = 0.$$

The wave function vanishes identically. The state does not exist. Two electrons in the 1s orbital must have opposite spins — not by postulate, but because the determinant with two identical columns is zero.

**The limit of the example:** this derivation uses the specific $(n, \ell, m_\ell, m_s)$ labels of atomic orbitals. In a crystal, the relevant single-particle states are Bloch waves labeled by band index and crystal momentum $\vec{k}$. The Slater determinant and its vanishing-column argument apply identically; the only thing that changes is what we call the orbitals. The result is the Pauli exclusion principle in solid-state physics: each $(\text{band}, \vec{k}, m_s)$ state can hold at most one electron.

---

## Helium and the Exchange Integral

Return to the question that opened this chapter. The helium atom has two electrons in the Coulomb field of a nucleus with charge $+2e$. The Hamiltonian is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla_1^2 - \frac{\hbar^2}{2m_e}\nabla_2^2 - \frac{2e^2}{4\pi\epsilon_0 r_1} - \frac{2e^2}{4\pi\epsilon_0 r_2} + \underbrace{\frac{e^2}{4\pi\epsilon_0|\vec{r}_1 - \vec{r}_2|}}_{V_{12}}.$$

The electron-electron repulsion $V_{12}$ makes this analytically unsolvable. Treat $V_{12}$ as a perturbation on the exactly solved two-electron hydrogenic problem ($Z = 2$ hydrogen-like orbitals).

**Symmetry sectors.** The total wave function must be antisymmetric under exchange. From Chapter 8, the two-spin states decompose into a singlet (antisymmetric, $S = 0$) and a triplet (symmetric, $S = 1$). Pairing:

- **Parahelium**: symmetric spatial $\times$ antisymmetric spin (singlet). $S = 0$. The two spectral families Heisenberg resolved.
- **Orthohelium**: antisymmetric spatial $\times$ symmetric spin (triplet). $S = 1$.

Both are antisymmetric total. Both are physically realizable.

**The ground state.** In the 1s2 configuration, both electrons are in $\phi_{1s}$. The symmetric spatial wave function is $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)$ — allowed, paired with the spin singlet. The antisymmetric spatial wave function $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2) - \phi_{1s}(\vec{r}_2)\phi_{1s}(\vec{r}_1) = 0$ vanishes — Pauli. The helium ground state is necessarily parahelium. No orthohelium ground state exists.

**The 1s2s excited configuration.** Take one electron in $\phi_{1s}$ and one in $\phi_{2s}$. Two antisymmetric total states are available:

$$\psi_\pm(\vec{r}_1,\vec{r}_2) = \frac{1}{\sqrt{2}}\bigl[\phi_{1s}(\vec{r}_1)\phi_{2s}(\vec{r}_2) \pm \phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\bigr]\times\begin{cases}\chi_\text{singlet} & (+)\\ \chi_\text{triplet} & (-)\end{cases}.$$

First-order perturbation theory gives the Coulomb energy correction:

$$\langle V_{12}\rangle_\pm = J \pm K,$$

where

$$J = \iint |\phi_{1s}(\vec{r}_1)|^2\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}|\phi_{2s}(\vec{r}_2)|^2\,d^3r_1\,d^3r_2$$

is the **direct integral**: the classical Coulomb energy between two charge densities, one shaped like $|\phi_{1s}|^2$ and one like $|\phi_{2s}|^2$. A classical physicist could write this.

$$K = \iint \phi_{1s}^{*}(\vec{r}_1)\phi_{2s}^{*}(\vec{r}_2)\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}\phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\,d^3r_1\,d^3r_2$$

is the **exchange integral**: the cross-term generated by antisymmetrization, which swaps which electron is "in 1s" and which is "in 2s." It has no classical analog whatsoever. For real orbitals and the positive Coulomb kernel $1/r_{12} > 0$, the integrand of $K$ is everywhere non-negative, so $K > 0$.

The result: parahelium 1s2s has energy $E^{(0)} + J + K$; orthohelium 1s2s has $E^{(0)} + J - K$. Since $K > 0$, orthohelium lies lower by $2K$. The measured splitting is about 0.80 eV — a real, large, observable energy difference.

Historically this splitting seemed to require a spin-dependent force. There is no such force. The Hamiltonian has no term that depends on spin directly. The mechanism runs through geometry:

- $S = 1$ (triplet) → spin part is symmetric → spatial part must be antisymmetric (to make total antisymmetric).
- Antisymmetric spatial wave function $\psi_-$ vanishes along $\vec{r}_1 = \vec{r}_2$.
- Electrons in $\psi_-$ avoid being at the same position → see less Coulomb repulsion → lower energy.

Spin sets the symmetry class of the spatial wave function. The spatial wave function determines how close the electrons approach. How close they approach determines the Coulomb repulsion. No spin-dependent force anywhere in the chain.

![Helium 1s2s energy levels: parahelium (singlet, J+K) lies above orthohelium (triplet, J−K) by 2K ≈ 0.80 eV. The splitting comes from the exchange integral, not a spin-spin force](../images/11-identical-particles-fig-02.png)
*Figure 10.2 — The 1s2s helium energy levels in both symmetry sectors. The $2K$ splitting is the signature of the exchange integral, with no classical analog.*

---

## Hund's First Rule as a Corollary

In 1925 Friedrich Hund catalogued an empirical regularity in atomic spectra: for a given electron configuration in a partially filled subshell, the term with highest total spin $S$ has the lowest energy. This is Hund's first rule.

It is not a separate postulate. The mechanism is the exchange integral, exactly as derived above. Higher $S$ → more symmetric spin state → antisymmetric spatial state enforced → electrons stay farther apart on average → lower Coulomb repulsion → lower energy. The rule is a corollary of antisymmetry applied to multi-electron atoms.

Example: oxygen ($1s^2 2s^2 2p^4$). The $2p$ subshell has three spatial orbitals ($m_\ell = -1, 0, +1$) with four electrons. Hund's rule says: fill each orbital with one electron (parallel spins, maximizing $S$) before pairing. The ground state has $S = 1$ — two unpaired electrons — rather than one pair and one single or two pairs. The $S = 1$ configuration is lower in energy by the exchange integral mechanism. Oxygen's paramagnetism (two unpaired spins) follows directly.

---

## The Periodic Table

Three facts combine to produce the structure of the periodic table. You now have all three.

**Fact one: hydrogenic energy ordering, modified by screening.** In a multi-electron atom, inner electrons partially shield the nuclear charge from outer electrons. Orbitals with low $\ell$ penetrate closer to the nucleus (they have significant probability density near $r = 0$, as Chapter 9 showed) and are less effectively screened. At fixed $n$, low-$\ell$ states lie below high-$\ell$ states: the $n^2$-fold Coulomb degeneracy of Chapter 9 breaks. The 2s lies below 2p in lithium. The 3s lies below 3p, which lies below 3d in sodium.

**Fact two: Pauli exclusion.** Each spin-orbital holds exactly one electron. Each spatial orbital holds at most two electrons — one with $m_s = +1/2$, one with $m_s = -1/2$ — and only if they have opposite spins (so the combined state is antisymmetric). Without this, every electron in every atom would collapse to the 1s orbital. There would be no chemistry.

**Fact three: Hund's rule.** Within a partially filled subshell, fill different $m_\ell$ orbitals with parallel spins before pairing into the same spatial orbital. The mechanism is the exchange integral: the parallel-spin (high-$S$) configuration lowers the Coulomb energy.

The Aufbau principle combines all three: fill orbitals in order of increasing energy (Madelung rule: lowest $n + \ell$ first, ties broken by lowest $n$), two electrons per orbital (Pauli), parallel spins first within a subshell (Hund). The sequence is $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, \ldots$ Row lengths 2, 8, 8, 18, 18, 32 follow from $2(2\ell+1)$ summed over the subshells in each period — twice the orbital degeneracy, because of spin.

About twenty atoms violate Madelung. Chromium ($3d^5\,4s^1$ instead of the predicted $3d^4\,4s^2$) and copper ($3d^{10}\,4s^1$ instead of $3d^9\,4s^2$) are the standard cases: the exchange-energy stabilization of a half-filled or completely-filled $3d$ subshell wins the competition with the small energy gap between 3d and 4s. These are not anomalies; they are cases where Hund's exchange stabilization beats the Madelung ordering by a small margin.

The periodic table is not a catalogue of empirical facts with a pattern. It is a theorem about antisymmetric wave functions, screened Coulomb potentials, and first-order perturbation theory.

---

## Bosons, Briefly

Bosons have symmetric wave functions. Nothing prevents two — or $10^{23}$ — bosons from occupying the same single-particle state. At low temperature and high density, a macroscopic fraction can pile into the lowest-energy state: **Bose-Einstein condensation**. The first experimental BEC in a dilute gas was achieved at JILA in 1995 by Cornell and Wieman, cooling $^{87}$Rb to about 170 nK; Ketterle independently achieved BEC in Na at MIT shortly after. Nobel Prize 2001. [verify]

One misconception is worth naming here: bosons are not attracted to each other and fermions are not repelled by each other in the sense of forces. There is no term in the Hamiltonian encoding exchange statistics. What exists is a correlation in the joint probability density $|\psi(\vec{r}_1, \vec{r}_2)|^2$ that emerges from symmetrization: fermions show a Pauli node at $\vec{r}_1 = \vec{r}_2$ (the wave function is zero there); bosons show enhanced probability at $\vec{r}_1 = \vec{r}_2$ (the bosonic wave function has a maximum on the diagonal). No force — a correlation. The single-particle marginal density $\int |\psi(\vec{r}_1, \vec{r}_2)|^2\,d^3r_2$ is identical for bosons, fermions, and distinguishable particles in the same pair of single-particle states. A single-particle detector cannot distinguish them.

The fermion correlation — the Pauli node — also holds up dead stars. Electrons in a white dwarf cannot share single-particle states. As the star contracts, electrons are forced into higher-energy states, raising the total kinetic energy and generating an outward **degeneracy pressure** with no thermal origin. Chandrasekhar showed in 1931 that this pressure has a relativistic limit at approximately $1.4\,M_\odot$ — the **Chandrasekhar mass** — above which relativistic electrons cannot prevent gravitational collapse. He did this calculation at age 19 on a steamship from India to England; he received the Nobel Prize for it in 1983. [verify]

A final note on generality: in three spatial dimensions, exchange statistics must be $\pm 1$. In two dimensions, intermediate statistics are possible — $e^{i\theta}$ for $0 < \theta < \pi$ — called anyons. These are realized in the fractional quantum Hall effect. The $\pm 1$ result is special to three (or more) dimensions.

---

## Common Misconceptions

**"Exchange statistics implies a force."** No. The Hamiltonian has no term corresponding to exchange statistics. The effect is a correlation in the joint probability density, not a force. The single-particle marginal density is exchange-statistics-blind.

**"Pauli exclusion is a postulate."** No. It is a theorem about determinants: two identical columns make the Slater determinant — and hence the wave function — identically zero. The postulate is antisymmetry (which itself follows from the spin-statistics theorem, but at the level of this course we take antisymmetry as the fundamental input). Pauli's rule follows from it.

**"Orthohelium has lower energy than parahelium because of a spin-dependent force."** No. The Hamiltonian at this order has no spin-spin interaction between electrons. The energy difference $2K$ is entirely a consequence of the spatial wave function symmetry: the antisymmetric spatial state forces the electrons apart, reducing their Coulomb repulsion. Spin determines which spatial symmetry is required; the spatial wave function determines the energy.

**"Bosons attract each other."** No. The enhanced probability of two bosons being at the same position is a consequence of the symmetric wave function, not of any attractive interaction. There is no force term in the Hamiltonian corresponding to "boson statistics." If you placed bosons in a harmonic trap with no interaction, they would pile up in the ground state because the symmetric wave function is normalized differently than the distinguishable-particle wave function; there is no attraction.

---

## Exercises

### Warm-up

**10.1** Define $\hat{P}_{12}$ and show from $\hat{P}_{12}^2 = \mathbb{1}$ that its eigenvalues can only be $\pm 1$. Then show that $[\hat{H}, \hat{P}_{12}] = 0$ for two identical particles interacting via a potential $V(|\vec{r}_1 - \vec{r}_2|)$, so energy eigenstates can be chosen to have definite exchange symmetry.

**10.2** Write the Slater determinant for two fermions in states $\phi_a$ and $\phi_b$. Verify by direct computation that swapping particles 1 and 2 gives $-\psi_-(1,2)$. Verify that $\langle\psi_-|\psi_-\rangle = 1$ given $\langle\phi_a|\phi_a\rangle = \langle\phi_b|\phi_b\rangle = 1$ and $\langle\phi_a|\phi_b\rangle = 0$.

**10.3** State whether each of the following is a boson or fermion, and give the constituent fermion count: (a) a photon; (b) a $^4$He atom; (c) a $^3$He atom; (d) a proton; (e) a $\pi^+$ meson (quark-antiquark pair, 2 quarks). For (b) and (c), explain in one sentence why the superfluid transition temperatures differ by three orders of magnitude.

### Application

**10.4** The $N = 3$ Slater determinant for fermions in orbitals $\phi_1, \phi_2, \phi_3$ is

$$\psi(1,2,3) = \frac{1}{\sqrt{6}}\det\begin{pmatrix}\phi_1(1)&\phi_2(1)&\phi_3(1)\\\phi_1(2)&\phi_2(2)&\phi_3(2)\\\phi_1(3)&\phi_2(3)&\phi_3(3)\end{pmatrix}.$$

(a) Set $\phi_2 = \phi_3$ and show that $\psi = 0$ identically. (b) Expand the determinant for distinct $\phi_1, \phi_2, \phi_3$ along the first row and write out all six terms with their signs. (c) Verify that swapping particles 1 and 2 gives $-\psi$.

**10.5** (a) Write down the two allowed antisymmetric total wave functions for the helium 1s2s configuration — one for parahelium, one for orthohelium. Identify the spin part (singlet or triplet) and spatial part (symmetric or antisymmetric) in each. (b) Explain why a $1s^2$ orthohelium ground state cannot exist, using the Pauli exclusion argument. (c) Suppose you add a very small spin-orbit coupling $\hat{H}' = \alpha\vec{L}\cdot\vec{S}$ as a perturbation. Would this allow transitions between the parahelium and orthohelium sectors? Why or why not?

**10.6** For the helium 1s2s configuration, $\langle V_{12}\rangle = J \pm K$. (a) Write down the integrals defining $J$ and $K$. (b) Explain in words why $J$ has a classical analog and $K$ does not. (c) For real orbitals $\phi_{1s}$ and $\phi_{2s}$ and the positive kernel $1/r_{12}$, argue from the form of $K$ that $K > 0$. (d) Which state — parahelium or orthohelium — has the lower energy at 1s2s, and by how much?

### Synthesis

**10.7** The ground configuration of oxygen is $1s^2\,2s^2\,2p^4$. (a) Write down the Hund's-rule ground state: which $m_\ell$ orbitals are doubly occupied, which are singly occupied, and what is $S$? (b) Using the exchange-integral argument, explain in three sentences why this configuration has lower Coulomb energy than the alternative with two doubly-occupied $2p$ orbitals and one empty. (c) Is Hund's rule a postulate or a consequence? Cite the mechanism.

**10.8** Two electrons are in the $n_a = 1$, $n_b = 2$ states of a 1D infinite well of width $L$ (single-particle eigenstates $\phi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$). (a) Write the joint probability densities $|\psi_+|^2$, $|\psi_-|^2$, and $|\psi_\text{dist}|^2$ in terms of $|\phi_1(x)|^2$ and $|\phi_2(x)|^2$. (b) Compute the marginal density $\rho(x_1) = \int|\psi(x_1,x_2)|^2\,dx_2$ for each case and show they are equal. (c) Explain why a single-particle measurement cannot distinguish bosons, fermions, or distinguishable particles in the same pair of orbitals. What kind of measurement could?

### Challenge

**10.9** A white dwarf of mass $M$ and radius $R$ is supported against gravity by electron degeneracy pressure. (a) The number of electrons is $N \sim M/m_p$. They occupy the $N$ lowest momentum states in a sphere of volume $V = \frac{4}{3}\pi R^3$ — estimate the Fermi momentum $p_F \sim \hbar N^{1/3}/R$ (up to numerical prefactors). (b) The total non-relativistic kinetic energy scales as $E_\text{kin} \sim N p_F^2/(2m_e)$ and the gravitational energy as $E_\text{grav} \sim -GM^2/R$. Minimize the total over $R$ and show $R \propto M^{-1/3}$: more massive white dwarfs are smaller. (c) In the ultra-relativistic limit $p_F \gg m_ec$, the kinetic energy scales as $E_\text{kin} \sim Ncp_F$. Show both $E_\text{kin}$ and $|E_\text{grav}|$ scale as $1/R$, giving a critical mass above which no equilibrium exists. Estimate that mass in solar masses.

---

## Still Puzzling

The chain from antisymmetry to the periodic table is clear: antisymmetry → Slater determinant → Pauli exclusion → shell structure + Hund's rule + screening → periodic table. What lies beneath antisymmetry is a harder question.

The spin-statistics theorem — that half-integer spin forces fermions and integer spin forces bosons — was proven by Pauli in 1940 from microcausality: field operators at spacelike separation must commute or anticommute to prevent signaling faster than light. From this he derived that integer-spin fields must commute (bosons) and half-integer-spin fields must anticommute (fermions). I can follow the steps. Whether microcausality is itself a foundational axiom or derivable from something more primitive, I do not know.

What I can say is that every attempt to derive the spin-statistics connection from purely non-relativistic principles has failed, or required assumptions so close to the conclusion that the derivation is circular. This is an acknowledged gap: the connection requires quantum field theory, and no shortcut from non-relativistic quantum mechanics has survived scrutiny.

Accept antisymmetry as the postulate for this course and know where the deeper explanation lives.

---

## The +1 — Simulation Exercise: Two-Particle Symmetry Explorer

You are going to build a simulation that renders the joint probability density $|\psi(x_1, x_2)|^2$ for two particles in a 1D infinite well, with a toggle for boson / fermion / distinguishable. The Pauli node, the bosonic clustering, and the invariance of the marginal density are all made visible as the user drags sliders.

### Part 1 — CLAUDE.md extension

Append this block to your project's `CLAUDE.md`:

```
## Chapter 10 — Two-Particle Symmetry Explorer Rules

- Single HTML file, single SVG canvas. D3 v7 only.
- Layout:
  - Primary 2D heat map of |ψ(x₁, x₂)|² (top, ~400 × 400 px).
  - Marginal one-particle density ρ(x₁) = ∫|ψ(x₁,x₂)|² dx₂ as a line
    plot directly below (~400 × 150 px).
  - Control panel as plain HTML to the right.
- Color scale: d3.interpolateViridis, sequential. Recompute domain per
  state change to [0, max(|ψ|²)].
- Grid: 200 × 200 over (x₁, x₂) ∈ [0, L]² for the infinite well.
- Diagonal x₁ = x₂ drawn as a thin red overlay line.
- Controls: radio buttons {boson, fermion, distinguishable}; sliders for
  n_a ∈ {1,2,3,4,5} and n_b ∈ {1,2,3,4,5}.
- Status text when ψ = 0 (fermion with n_a = n_b):
  "ψ₋ = 0: Pauli forbidden — no such state exists."
- Numeric readouts: ⟨(x₁−x₂)²⟩, max(|ψ|²), P(both in left half).
- No DOM mutation outside the redraw function.
```

### Part 2 — The simulation prompt

```
Build me a D3 v7 two-particle symmetry explorer following CLAUDE.md.

HOOK. Render |ψ(x₁, x₂)|² for two particles in a 1D infinite well as a
2D heat map. Toggle between boson (symmetric), fermion (antisymmetric),
and distinguishable, and watch the Pauli node appear and vanish along x₁ = x₂.

UNFOLD. Single-particle eigenstates in the infinite well of width L:
  φ_n(x) = √(2/L) sin(nπx/L).
Two-particle wave functions:
  ψ_boson = (1/√2)[φ_a(x₁)φ_b(x₂) + φ_b(x₁)φ_a(x₂)]
  ψ_fermion = (1/√2)[φ_a(x₁)φ_b(x₂) − φ_b(x₁)φ_a(x₂)]
  ψ_dist = φ_a(x₁)φ_b(x₂)
Special case: ψ_fermion = 0 when n_a = n_b. Show the status note.

MECHANISM. Two coupled panels.
  (1) 2D heat map of |ψ(x₁, x₂)|² with diagonal overlay.
  (2) Marginal ρ(x₁) = ∫|ψ(x₁, x₂)|² dx₂ as a line plot. This marginal
      is identical for boson, fermion, and distinguishable at the same
      (n_a, n_b) — a key pedagogical point.

SYNTHESIZE. Add a "Spin extension" toggle. When on, the user selects spin
state {singlet, triplet}. Enforce total antisymmetry:
  singlet (antisymmetric spin) ⊗ symmetric spatial → allowed
  triplet (symmetric spin) ⊗ antisymmetric spatial → allowed
  triplet + n_a = n_b → Pauli forbidden, show status note.

Output a single self-contained HTML file using the D3 v7 CDN.
```

### Part 3 — Exploration tasks

**The Pauli node.** Set fermion, $n_a = 1$, $n_b = 2$. The diagonal $x_1 = x_2$ is a stripe of zero — the Pauli node. Set $n_a = n_b = 1$: the status note should display "$\psi_- = 0$: Pauli forbidden." This is the simulation showing directly that two fermions cannot occupy the same single-particle state.

**Bosonic clustering.** Switch to boson, keep $n_a = n_b = 1$. The wave function is $\phi_1(x_1)\phi_1(x_2)$, perfectly allowed. The heat map shows a single peak and the diagonal runs right through it. Bosons share orbitals without restriction.

**Marginals don't reveal exchange.** Set $n_a = 1$, $n_b = 2$. Cycle through boson, fermion, distinguishable and watch the heat map change dramatically while the marginal line plot stays identical. A single-particle detector cannot distinguish bosons from fermions from distinguishable particles in the same pair of orbitals.

**Compute $\langle(x_1 - x_2)^2\rangle$.** Read the simulation's numerical readout at $n_a = 1, n_b = 2$. Confirm:

$$\langle(x_1 - x_2)^2\rangle_\text{fermion} > \langle(x_1 - x_2)^2\rangle_\text{dist} > \langle(x_1 - x_2)^2\rangle_\text{boson}.$$

Fermions spread; bosons cluster; distinguishable particles split the difference.

**Spin extension and helium-like behavior.** Toggle spin extension. Select singlet, $n_a = n_b = 1$: the simulation shows $\phi_1(x_1)\phi_1(x_2)$ — the helium ground-state analog, allowed. Select triplet, $n_a = n_b = 1$: status note "Pauli forbidden." This is the $1s^2$ orthohelium impossibility made visual.

**The 1s2s helium analog.** Spin extension on, singlet, $n_a = 1$, $n_b = 2$: the heat map is symmetric across the diagonal — parahelium analog. Switch to triplet: the heat map is antisymmetric with a Pauli node — orthohelium analog. The energy advantage of orthohelium (electrons farther apart → less Coulomb repulsion) is geometrically visible.

### Part 4 — Extension prompt: Coulomb interaction

```
Add an interaction term V_int(x₁, x₂) = λ/√((x₁−x₂)² + ε²) with ε = 0.05L
(soft-core regularization). Diagonalize the two-particle Hamiltonian numerically
on a 20×20 grid of single-particle modes. Let the user adjust λ from 0 to 10.

For the fermion 1s2s case: confirm that turning on λ > 0 lowers the
antisymmetric energy relative to the symmetric energy. The splitting at
small λ is approximately 2K·λ — the helium exchange integral, made into
a numerical experiment.
```

### Part 5 — Six failure modes to watch for

**$1/\sqrt{2}$ normalization dropped.** The wave function becomes over-normalized by a factor of 2. Check $\int|\psi|^2 d^2r$ on the grid — if it's near 2 instead of 1, the factor is missing.

**Marginals computed wrong.** $\rho(x_1) = \int|\psi(x_1, x_2)|^2 dx_2$, summed over the $x_2$ axis multiplied by $\Delta x_2$. Verify $\int\rho(x_1)dx_1 = 1$.

**Fermion $n_a = n_b$ case not handled.** The wave function is zero — but displaying "all zero" as a uniform dark color confuses students. Show the status note clearly.

**Color domain not reset between particle types.** The Viridis domain must be recomputed per render; otherwise switching from boson to fermion (which has lower peak density due to the Pauli node) shows incorrectly dark images.

**Diagonal overlay rendered before heat map.** SVG renders later elements on top. Draw the heat map first, then the diagonal overlay — otherwise the red line is hidden beneath the colored rectangles.

**Spin extension fails to enforce total antisymmetry.** A bug where the toggle allows singlet + antisymmetric-spatial, producing a symmetric total wave function. Implement so that singlet always pairs with symmetric spatial and triplet always pairs with antisymmetric spatial.

---

## References

- W. Pauli, "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren," *Zeitschrift für Physik*, 31, 765–783 (1925). (Pauli exclusion as an empirical rule.) [verify]
- J. C. Slater, "The Theory of Complex Spectra," *Physical Review*, 34, 1293–1322 (1929). (Slater determinant; Pauli exclusion as a theorem.) [verify]
- W. Heisenberg, "Mehrköperproblem und Resonanz in der Quantenmechanik," *Zeitschrift für Physik*, 38, 411–426 (1926). (Resolution of para/orthohelium.) [verify]
- W. Pauli, "The Connection Between Spin and Statistics," *Physical Review*, 58, 716–722 (1940). (Spin-statistics theorem from microcausality.) [verify]
- S. N. Chandrasekhar, "The Maximum Mass of Ideal White Dwarfs," *Astrophysical Journal*, 74, 81–82 (1931). (Chandrasekhar mass from electron degeneracy pressure.) [verify]
- M. H. Anderson, J. R. Ensher, M. R. Matthews, C. E. Wieman, E. A. Cornell, "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor," *Science*, 269, 198–201 (1995). (First dilute-gas BEC.) [verify]
- Griffiths, D. J. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018. Chapter 5.
- Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012. Chapter 11.
- Cohen-Tannoudji, C., Diu, B., Laloë, F. *Quantum Mechanics*, Vol. III. Wiley-VCH, 2020. Chapter XIV (Identical Particles). [verify]
- Sakurai, J. J., Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021. Chapter 7.
