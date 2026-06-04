# Chapter 9 — The Hydrogen Atom

## TL;DR

- Balmer got the numbers right in 1885. Schrödinger got the wave functions too.
- Reduce the two-body problem to one body via the reduced mass. Separate in spherical coordinates: the angular part is the spherical harmonics from Chapter 7; the radial equation is new, and its solution quantizes the energy.
- Bound-state energies: $E_n = -13.6\,\text{eV}/n^2$, with quantum numbers $n \geq 1$, $\ell = 0,\ldots,n-1$, $|m| \leq \ell$ — so $n^2$ orbital states per shell, and $2n^2$ including spin.
- The $r^2$ Jacobian matters: the most-probable radius is $r_\text{mp} = a_0$; the mean radius is $\langle r\rangle = 3a_0/2$. They differ because $P(r)$ is skewed. That difference is evidence against the path picture.
- The $\ell$-degeneracy (all levels at fixed $n$ share one energy) is not generic — it is a signature of the special $\mathfrak{so}(4)$ symmetry of the $1/r$ potential.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Explain** (Understand) why the two-body hydrogen Hamiltonian separates into a center-of-mass piece and a one-body radial problem with reduced mass $\mu$.
2. **Derive** (Apply) the ground-state energy $E_1 = -13.6\,\text{eV}$ and Bohr radius $a_0$ by substituting a trial function into the radial equation and requiring it to hold at every $r$.
3. **Enumerate** (Apply) all allowed $(n, \ell, m)$ combinations for a given $n$, count the orbital and spin degeneracy, and connect the $2n^2$ shell structure to periodic-table row lengths.
4. **Compute** (Analyze) the radial probability density $P(r) = r^2|R_{n\ell}(r)|^2$, locate its peak $r_\text{mp}$ and mean $\langle r\rangle$, and explain why $r_\text{mp} \neq \langle r\rangle$ for the 1s state.
5. **Evaluate** (Evaluate) whether a given transition is electric-dipole allowed using the selection rules $\Delta\ell = \pm 1$, $\Delta m = 0, \pm 1$, and calculate the emitted photon wavelength from $\Delta E = hc/\lambda$.

---

## Four Visible Lines, No Theory

In 1885, a Swiss mathematics teacher named Johann Balmer published a four-page note. He had been looking at four visible spectral lines of hydrogen — red, blue-green, violet, deep violet — and he noticed that their wavelengths fit a formula:

$$\lambda = B\cdot\frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, 6,$$

with $B \approx 364.5$ nm. He had no theory. He had four numbers from a lab notebook and a pattern that fit them exactly — not approximately, exactly — to the precision of the measurements.

That kind of precision does not come from coincidence. The pattern is not a numerical accident; it is a signature of something structural. Balmer had no idea what.

Johannes Rydberg generalized the formula in 1888. The spectral lines of hydrogen satisfy

$$\frac{1}{\lambda} = R_H\!\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right),$$

where $R_H \approx 1.097 \times 10^7\,\text{m}^{-1}$ is the Rydberg constant. This organized multiple spectral series: Lyman (ultraviolet, $n_f = 1$), Balmer (visible, $n_f = 2$), Paschen (near-infrared, $n_f = 3$), Brackett (infrared, $n_f = 4$). All from a single formula. Still no explanation for twenty-eight years.

Bohr gave a partial answer in 1913. He assumed electrons move in circular orbits but can only occupy orbits where the angular momentum is a multiple of $\hbar$: $L = n\hbar$. This ansatz produced the right energies. But why must angular momentum be quantized? Why do orbiting electrons not radiate, as Maxwell's equations demand? Bohr had no answers. The model was a conjecture that happened to produce the right numbers.

Schrödinger, working at an Alpine resort over Christmas 1925, wrote down the wave equation for hydrogen. The energies $-13.6\,\text{eV}/n^2$ fell out again — same numbers as Bohr, but from a calculation with no arbitrary postulates. What also fell out, and what Bohr had absolutely no machinery for, was the complete probability density $|\psi_{n\ell m}(r,\theta,\phi)|^2$: a cloud of probability, not a path. This chapter does that calculation.

![A gallery of hydrogen 2D cross-sections |ψ_{nℓm}(x,0,z)|² for n = 1,2,3, illustrating the variety of orbital shapes produced by one set of quantum numbers](../images/10-the-hydrogen-atom-fig-01.png)
*Figure 9.1 — Gallery of hydrogen orbital cross-sections for n = 1, 2, 3 in the xz-plane.*

---

## One Equation, Two Bodies

A hydrogen atom is a proton (mass $m_p$, position $\vec{r}_p$) and an electron (mass $m_e$, position $\vec{r}_e$) interacting via the Coulomb potential $V = -e^2/(4\pi\epsilon_0|\vec{r}_e - \vec{r}_p|)$. The Hamiltonian is

$$\hat{H} = \frac{\hat{p}_e^2}{2m_e} + \frac{\hat{p}_p^2}{2m_p} - \frac{e^2}{4\pi\epsilon_0|\hat{\vec{r}}_e - \hat{\vec{r}}_p|}.$$

Two particles, six coordinates. But we can reduce this to one body. Introduce the **center-of-mass coordinate** $\vec{R} = (m_p\vec{r}_p + m_e\vec{r}_e)/(m_p + m_e)$ and the **relative coordinate** $\vec{r} = \vec{r}_e - \vec{r}_p$. In these variables the Hamiltonian separates:

$$\hat{H} = \underbrace{\frac{\hat{P}^2}{2M}}_{\text{free CM}} + \underbrace{\frac{\hat{p}^2}{2\mu} - \frac{e^2}{4\pi\epsilon_0 r}}_{\hat{H}_\text{rel}},$$

where $M = m_p + m_e$ is the total mass, $\hat{P}$ is the total momentum, and

$$\mu = \frac{m_p m_e}{m_p + m_e}$$

is the **reduced mass**. The center-of-mass piece describes a free particle drifting through space — uninteresting. All the physics is in $\hat{H}_\text{rel}$, which is a one-body Schrödinger equation in three dimensions.

Because $m_p \approx 1836\,m_e$, the reduced mass $\mu \approx m_e(1 - 1/1836)$ is within 0.05% of $m_e$. For rough numbers we use $\mu = m_e$. For precision spectroscopy the difference matters: Harold Urey discovered deuterium in 1932 by finding a faint second copy of every Balmer line, shifted because deuterium's nucleus is heavier and changes $\mu$. The Balmer $\alpha$ line ($n=3 \to n=2$, nominally 656.3 nm) is shifted by about 1.79 Å between ordinary hydrogen and deuterium — small, but unmistakable to a careful spectroscopist.

The equation to solve is now

$$\left[-\frac{\hbar^2}{2\mu}\nabla^2 - \frac{e^2}{4\pi\epsilon_0 r}\right]\psi(\vec{r}) = E\,\psi(\vec{r}).$$

The potential is spherically symmetric. We know exactly what to do.

---

## Separating the Problem

From Chapter 6 you know that any spherically symmetric Hamiltonian separates in spherical coordinates. Write $\psi(r,\theta,\phi) = R(r)Y_\ell^m(\theta,\phi)$. The angular part gives the spherical harmonics immediately — that result is universal, independent of what $V(r)$ turns out to be. The spherical harmonics know nothing about Coulomb; they know only about the rotation group.

The radial part is where hydrogen lives. Make the substitution $u(r) = rR(r)$ — a standard trick that converts the three-dimensional radial equation into a one-dimensional one. After substituting, the equation becomes:

$$-\frac{\hbar^2}{2\mu}\frac{d^2u}{dr^2} + \underbrace{\left[-\frac{e^2}{4\pi\epsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2\mu r^2}\right]}_{V_\text{eff}(r)}u(r) = E\,u(r).$$

The **effective potential** $V_\text{eff}(r)$ has two pieces:

- **Coulomb well:** $-e^2/(4\pi\epsilon_0 r)$, attractive, pulls the electron toward the nucleus.
- **Centrifugal barrier:** $+\hbar^2\ell(\ell+1)/(2\mu r^2)$, repulsive, diverges as $r \to 0$ for $\ell \geq 1$.

For $\ell = 0$ (s-states), the centrifugal barrier vanishes and the wave function can be nonzero at the nucleus — relevant for hyperfine spectroscopy, where the electron's probability at the nucleus couples to the nuclear magnetic moment. For $\ell \geq 1$ the barrier pushes probability density away from the origin.

The boundary conditions are simply stated: $u(0) = 0$ so that $R = u/r$ stays finite at the origin; $u(r) \to 0$ as $r \to \infty$ so that the wave function is normalizable. These two requirements together quantize the energy.

![V_eff(r) = −e²/(4πε₀r) + ℏ²ℓ(ℓ+1)/(2μr²) for ℓ = 0 and ℓ = 1,2. The centrifugal barrier for ℓ ≥ 1 suppresses the wave function near the nucleus](../images/10-the-hydrogen-atom-fig-02.png)
*Figure 9.2 — Effective potential $V_\text{eff}(r)$ for several values of $\ell$. For $\ell = 0$ the electron can reach the nucleus; for $\ell \geq 1$ the centrifugal barrier creates a minimum at finite $r$.*

---

## The Ground State, Worked All the Way Through

The cleanest way into the hydrogen atom is through the ground state, where the full calculation can be done by hand without invoking the Frobenius series. Set $\ell = 0$: the centrifugal barrier vanishes. The radial equation reduces to

$$-\frac{\hbar^2}{2\mu}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\epsilon_0 r}\,u(r) = E\,u(r).$$

We need a function $u(r)$ that goes to zero at the origin and decays at infinity. The simplest candidate is

$$u(r) = A r\,e^{-r/a},$$

where $a$ is an unknown length and $A$ is a normalization constant. Differentiate twice:

$$u''(r) = Ae^{-r/a}\!\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

Substitute into the radial equation, divide through by $Ae^{-r/a}$, and collect terms by powers of $r$:

$$\underbrace{\left(\frac{\hbar^2}{\mu a} - \frac{e^2}{4\pi\epsilon_0}\right)}_{\text{constant}} + \underbrace{\left(E + \frac{\hbar^2}{2\mu a^2}\right)}_{\text{must vanish}}\cdot r = 0.$$

For this to hold at every $r$, both groupings must independently vanish. From the constant terms:

$$\frac{\hbar^2}{\mu a} = \frac{e^2}{4\pi\epsilon_0} \quad\Longrightarrow\quad a = a_0 \equiv \frac{4\pi\epsilon_0\hbar^2}{\mu e^2} \approx 0.529\,\text{Å}.$$

This is the **Bohr radius** $a_0$. It emerged from the calculation; we did not put it in by hand. From the $r$-coefficient:

$$E = -\frac{\hbar^2}{2\mu a_0^2} = -\frac{\mu e^4}{2(4\pi\epsilon_0)^2\hbar^2} \approx -13.6\,\text{eV}.$$

Both the size of the atom and the ground-state energy come out of a single consistency requirement. Normalize: $A = 2/a_0^{3/2}$, so $R_{10}(r) = u(r)/r = (2/a_0^{3/2})e^{-r/a_0}$, and the full ground-state wave function is

$$\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.$$

Spherically symmetric, maximum density at the nucleus, exponential decay in every direction. No ring. No orbit.

---

## Two Radii, and Why They Differ

Here is the calculation that matters most in this chapter, and it is worth going slowly.

The radial probability density — the probability per unit radial distance of finding the electron between $r$ and $r + dr$, after integrating over all angles — is **not** $|R_{10}|^2$. It is

$$P(r) = r^2|R_{10}(r)|^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

The factor $r^2$ comes from the volume element in spherical coordinates: a thin shell at radius $r$ has area $4\pi r^2$, so even though the density $|\psi|^2$ is largest at $r = 0$, the probability of finding the electron near the nucleus is nearly zero because the shell volume at small $r$ is nearly zero. Probability is density times available volume.

**The most-probable radius.** Differentiate $P(r)$ and set the result to zero:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0 \quad\Longrightarrow\quad r_\text{mp} = a_0.$$

**The mean radius.** Integrate $r \cdot P(r)$:

$$\langle r\rangle = \int_0^\infty r\cdot P(r)\,dr = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr.$$

Using $\int_0^\infty r^n e^{-r/b}\,dr = n!\,b^{n+1}$ with $n = 3$ and $b = a_0/2$:

$$\langle r\rangle = \frac{4}{a_0^3}\cdot\frac{3!}{\left(2/a_0\right)^4} = \frac{4}{a_0^3}\cdot\frac{6a_0^4}{16} = \frac{3}{2}a_0.$$

The most-probable radius is $a_0$. The mean radius is $\tfrac{3}{2}a_0$. Two different numbers describing the same distribution.

They differ because $P(r)$ is right-skewed — it has a long tail at large $r$ that pulls the mean to the right of the peak. This is not a numerical detail. It is the direct geometric evidence that the electron's position is described by a probability distribution, not a trajectory. A classical electron on a circular orbit at fixed radius $r_0$ would have $r_\text{mp} = \langle r\rangle = r_0$. There would be only one radius. The fact that $r_\text{mp} \neq \langle r\rangle$ is a fingerprint of wave mechanics built into the ground state of the simplest atom.

Bohr placed the electron at radius $a_0$. Schrödinger says the *peak* of the probability distribution is at $a_0$ — same number — but the mean is larger, and the electron is found outside $a_0$ on more than half of all measurements. The two calculations give the same number for entirely different reasons, and only one of them describes what you would see in the laboratory.

![P(r) = (4/a₀³) r² e^{−2r/a₀} for the 1s state. Peak at r_mp = a₀; mean at ⟨r⟩ = 3a₀/2. The skew is the direct signature of a probability distribution, not a path](../images/10-the-hydrogen-atom-fig-03.png)
*Figure 9.3 — Radial probability density $P(r)$ for the 1s state, with $r_\text{mp}$ and $\langle r\rangle$ marked. The shaded area is the probability of finding the electron outside $r_\text{mp}$, which exceeds 50%.*

---

## The Full Spectrum

The ground state worked out cleanly because we guessed a simple ansatz. For general $(n, \ell)$ the calculation requires a Frobenius series expansion — expand $u(r)$ as a power series, substitute, and demand that the series terminate (otherwise the wave function diverges at large $r$). The series terminates only for specific values of energy, and those values are exactly

$$E_n = -\frac{13.6\,\text{eV}}{n^2}, \qquad n = 1, 2, 3, \ldots$$

The energy depends only on $n$ — not on $\ell$, not on $m$. This is the **Coulomb degeneracy**.

The terminated-series solutions are the associated Laguerre polynomials, and the full radial wave functions are

$$R_{n\ell}(r) = \mathcal{N}_{n\ell}\cdot\left(\frac{r}{a_0}\right)^\ell\cdot e^{-r/(na_0)}\cdot L_{n-\ell-1}^{2\ell+1}\!\!\left(\frac{2r}{na_0}\right),$$

where $\mathcal{N}_{n\ell}$ is a normalization constant and $L_{n-\ell-1}^{2\ell+1}$ is an associated Laguerre polynomial of degree $n - \ell - 1$. The subscript on the polynomial is where the quantum number constraints come from.

**Where the constraints come from.** Three constraints, three distinct sources:

- $n \geq 1$: the Frobenius series terminates only for positive integer $n$. Below $n = 1$ the series fails to terminate and $R(r) \to \infty$ as $r \to \infty$ — not normalizable.
- $\ell \leq n - 1$ (equivalently, $\ell = 0, 1, \ldots, n-1$): the Laguerre polynomial has degree $n - \ell - 1$; a polynomial of negative degree does not exist.
- $|m| \leq \ell$: this comes from Chapter 7 — the angular momentum algebra, unchanged by the specific form of $V(r)$.

**Counting states.** For each $n$, sum over $\ell$:

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2.$$

So each shell $n$ contains $n^2$ orbital states. Including the two spin projections $m_s = \pm\tfrac{1}{2}$ from Chapter 8, each shell holds $2n^2$ states:

| $n$ | Shell label | $n^2$ orbital states | $2n^2$ with spin |
|---|---|---|---|
| 1 | K | 1 | 2 |
| 2 | L | 4 | 8 |
| 3 | M | 9 | 18 |
| 4 | N | 16 | 32 |

These are the row lengths of the periodic table. Not numerology — a structural consequence of the three constraints on quantum numbers derived across Chapters 7, 8, and 9.

**Nodes.** A node-counting rule ties the structure together: the total number of nodes in $\psi_{n\ell m}$ is $n - 1$, partitioned into $n - \ell - 1$ **radial nodes** and $\ell$ **angular nodes**. The 2s state ($n=2, \ell=0$) has one radial node and zero angular nodes. The 2p states ($n=2, \ell=1$) have zero radial nodes and one angular node (the cone or plane where $Y_1^m = 0$). Both have the same energy because the count is the same: $n - 1 = 1$ in each case.

**The general mean radius.** A formula that is frequently useful:

$$\langle r\rangle_{n\ell} = \frac{a_0}{2}\bigl[3n^2 - \ell(\ell+1)\bigr].$$

For $(1,0)$: $\langle r\rangle = \tfrac{3}{2}a_0$. ✓ For $(2,0)$: $\langle r\rangle = 6a_0$. For $(2,1)$: $\langle r\rangle = 5a_0$. At fixed $n$, increasing $\ell$ moves the distribution closer to the nucleus — the centrifugal barrier pushes the electron outward, but only at small $r$; the main effect is to shift the peak of $P(r)$ and reduce the mean.

---

## The Shape Question: Complex or Real?

The wave functions $\psi_{n\ell m}$ are complex for $m \neq 0$. They are eigenstates of $\hat{L}_z$ with eigenvalue $m\hbar$. In the $xz$-plane, the $m = \pm 1$ states look like azimuthally symmetric rings — no preferred direction in the plane perpendicular to $\hat{z}$.

The chemistry textbook $p_x$ and $p_y$ orbitals are real linear combinations of $m = \pm 1$:

$$p_x \propto \psi_{21,-1} - \psi_{21,+1} \propto \sin\theta\cos\phi, \qquad p_y \propto i(\psi_{21,-1} + \psi_{21,+1}) \propto \sin\theta\sin\phi.$$

These are the dumbbell shapes pointing along the Cartesian axes — beautiful, and useful for bonding — but they are *not* eigenstates of $\hat{L}_z$. They are superpositions of $m = +1$ and $m = -1$.

Both descriptions span exactly the same subspace of states. Physics prefers the complex eigenstates because they diagonalize $\hat{L}_z$. Chemistry prefers the real combinations because bonding is about directionality. Neither is wrong. The choice is a choice of what to make obvious, and different questions make different things obvious.

---

## The Hidden Symmetry

The Coulomb degeneracy — 2s and 2p sharing $E = -3.4$ eV; 3s, 3p, 3d all at $-1.51$ eV — is not generic. For any central potential, energy depends on $n$ and $\ell$; the $m$-degeneracy is universal (rotational symmetry). The additional $\ell$-degeneracy is special to $V \propto 1/r$.

Classically, this special property manifests as the non-precession of Kepler orbits: an ellipse in a $1/r$ field closes perfectly on itself, returning to the same point. For any other power law the orbit precesses. The classical quantity that is constant precisely because of non-precession is the **Laplace–Runge–Lenz vector**, pointing along the major axis of the ellipse. In quantum mechanics, the three angular-momentum components and three Runge–Lenz components — six operators total — form the Lie algebra $\mathfrak{so}(4)$: rotations in *four* dimensions. Wolfgang Pauli solved hydrogen algebraically using this algebra in 1926, before Schrödinger published the wave-mechanical solution. [verify]

The moment the potential departs from $1/r$, the $\mathfrak{so}(4)$ symmetry breaks and the $\ell$-degeneracy splits. In sodium, ten inner electrons partially screen the nuclear charge, and the effective potential felt by the valence electron is no longer $-1/r$. The 3s level falls below 3p, which falls below 3d. The bright yellow sodium D lines at 589 nm are the $3p \to 3s$ transitions, and they exist *because* sodium's effective potential is not Coulomb. Those lines are spectroscopic evidence of broken $\mathfrak{so}(4)$ symmetry.

---

## Transitions and Selection Rules

Two hydrogen levels separated by energy $\Delta E$ can be connected by emitting a photon of frequency $\omega = \Delta E/\hbar$. The Balmer $\alpha$ line — the $n = 3 \to n = 2$ transition — sits at

$$\lambda = \frac{hc}{\Delta E} = \frac{1240\,\text{eV·nm}}{13.6\times(1/4 - 1/9)\,\text{eV}} = \frac{1240}{1.889} \approx 656.3\,\text{nm}.$$

The experimental value is 656.281 nm — agreement to 0.003%. This is what Balmer's 1885 formula was missing: a derivation.

Not every transition is allowed. A photon carries angular momentum 1, and conservation of angular momentum during emission requires that the electron's orbital angular momentum change by $\pm 1$. The full electric-dipole selection rules — derived by computing the matrix element $\langle\psi_f|\hat{\vec{r}}|\psi_i\rangle$ and requiring it to be nonzero — are

$$\Delta\ell = \pm 1, \qquad \Delta m = 0, \pm 1.$$

The $2s \to 1s$ transition has $\Delta\ell = 0$ and is electric-dipole **forbidden**. It occurs via two-photon emission with lifetime $\approx 0.12$ s, eight orders of magnitude slower than allowed transitions (nanosecond lifetimes). That is not a curiosity; it is what makes the 2s state metastable enough to interrogate in precision spectroscopy.

The $1S$–$2S$ two-photon transition in hydrogen has been measured to fifteen significant figures using optical frequency combs. [verify] The ALPHA collaboration at CERN has measured the same transition in antihydrogen — hydrogen made from a positron orbiting an antiproton — and found agreement with ordinary hydrogen at parts-per-trillion precision, a direct test of CPT symmetry. [verify]

![Energy level diagram for hydrogen showing the principal series. Allowed transitions (Δℓ = ±1) shown as solid arrows; the forbidden 2s→1s as a dashed arrow](../images/10-the-hydrogen-atom-fig-04.png)
*Figure 9.4 — Hydrogen energy level diagram. Lyman series ($n_f=1$, UV), Balmer series ($n_f=2$, visible), Paschen series ($n_f=3$, near-IR). The 2s→1s forbidden transition is marked with the two-photon symbol.*

---

## What the Orbital Is Not

Three pictures to be careful about.

**The orbital is not a path.** The 90% isosurface images in chemistry textbooks — dumbbells, cloverleaves, lobes — are not containing walls. The electron does not orbit inside the dumbbell. The dumbbell encloses a region where there is 90% probability of finding the electron on a single position measurement. On 10% of measurements the electron is found outside it. The $r_\text{mp} \neq \langle r\rangle$ calculation is the direct evidence: a path has one radius; a probability distribution has a peak and a mean that need not coincide.

**The Bohr model is not essentially correct.** Bohr gets $E_n = -13.6\,\text{eV}/n^2$ right because hydrogen's $\mathfrak{so}(4)$ symmetry makes the energy depend on a single quantum number, and Bohr's condition $L = n\hbar$ happens to count that quantum number correctly for circular orbits. But Bohr has $\ell = n$ always (maximum angular momentum) while Schrödinger says $\ell = 0, 1, \ldots, n-1$. The 2s state — $\ell = 0$, no angular momentum — is utterly forbidden in Bohr's model, yet perfectly physical and spectroscopically accessible in Schrödinger's. The Bohr model is a numerical accident. This chapter buries it.

**$|\psi|^2$ is not a smeared charge distribution.** The probability density is the distribution of outcomes over many repeated position measurements. The electron remains a point particle. When you fire electrons at hydrogen and measure where they scatter from, the distribution of scattering events converges to $|\psi|^2$ over many trials. The cloud shows where measurements land. It does not show charge sitting continuously in space.

---

## Worked Example: Ground-State Radial Probability and the Two Radii

**The lesson: why $r_\text{mp} \neq \langle r\rangle$.**

The ground-state wave function is $\psi_{100}(r) = (\pi a_0^3)^{-1/2}e^{-r/a_0}$, so the radial wave function is $R_{10}(r) = 2a_0^{-3/2}e^{-r/a_0}$.

**Step 1: Write $P(r)$.**

$$P(r) = r^2|R_{10}(r)|^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

Note that $P(0) = 0$ (the factor of $r^2$ kills it), $P(\infty) = 0$ (the exponential kills it), so $P$ has a maximum somewhere in between.

**Step 2: Find $r_\text{mp}$.**

$$\frac{dP}{dr} = \frac{4}{a_0^3}\!\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0.$$

The exponential is never zero. Factor out $2r$:

$$2r\!\left(1 - \frac{r}{a_0}\right) = 0.$$

Solutions: $r = 0$ (minimum, not maximum) and $r = a_0$ (the maximum). Check the second derivative or argue from context: $r_\text{mp} = a_0$.

**Step 3: Compute $\langle r\rangle$.**

$$\langle r\rangle = \int_0^\infty r\cdot P(r)\,dr = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr.$$

Use $\int_0^\infty r^n e^{-\alpha r}\,dr = n!/\alpha^{n+1}$ with $n = 3$ and $\alpha = 2/a_0$:

$$\langle r\rangle = \frac{4}{a_0^3}\cdot\frac{6}{(2/a_0)^4} = \frac{4}{a_0^3}\cdot\frac{6a_0^4}{16} = \frac{3}{2}a_0.$$

**The result:** $r_\text{mp} = a_0 = 0.529\,\text{Å}$; $\langle r\rangle = \tfrac{3}{2}a_0 = 0.794\,\text{Å}$.

**Step 4: Interpret the difference.**

The function $P(r) = (4/a_0^3)r^2e^{-2r/a_0}$ has a single peak at $r_\text{mp}$ and then a long tail at large $r$ — it is right-skewed. The mean is pulled to the right of the peak by the tail.

Bohr's model predicts both quantities equal to $a_0$: the electron is on a circular orbit at a single well-defined radius, so there is only one number to speak of. Schrödinger's calculation gives $r_\text{mp} = a_0$ — coinciding with Bohr numerically — but the mean $\langle r\rangle$ is different, and the electron has a nonzero probability of being found at any $r > 0$. The agreement at $r_\text{mp}$ is numerical coincidence. The disagreement at $\langle r\rangle$ is the substance.

**The limit: where the ansatz reaches.** We derived the ground state by choosing a single exponential $u(r) = Are^{-r/a}$. This is exact: the $n=1$, $\ell=0$ Laguerre polynomial is a constant, so the exponential is the complete solution. For $n = 2$, the Laguerre polynomial is a first-degree polynomial, contributing a factor $(2 - r/a_0)$ that creates the radial node at $r = 2a_0$. The ansatz method would require us to guess a product of a polynomial and an exponential — possible but tedious for large $n$.

---

## Common Misconceptions

**"The orbital is the electron's path."** The orbital $\psi_{n\ell m}$ is a probability amplitude. The 90% isosurface is not a wall containing the electron. On 10% of measurements the electron is found outside it, and there is nothing wrong with that. A probability distribution is not a trajectory.

**"$P(r)$ peaks at $r = 0$ for the 1s state."** This confuses $|\psi_{100}|^2$ (which does peak at $r=0$) with $P(r) = r^2|\psi_{100}|^2$ (which peaks at $r_\text{mp} = a_0$). The factor $r^2$ accounts for the spherical shell volume and cannot be dropped. Plotting $|R_{n\ell}|^2$ instead of $r^2|R_{n\ell}|^2$ is the single most common error in hydrogen atom calculations.

**"The Bohr model and Schrödinger agree for the energies, so the Bohr model is essentially right."** The energies agree numerically for one specific reason: $\mathfrak{so}(4)$ symmetry makes the energy depend on a single quantum number in both models, and Bohr's angular-momentum quantization happens to count the same number for circular orbits. On every other prediction — wave functions, radial probability densities, selection rules, orbital shapes, the existence of states with $\ell < n-1$ — Bohr fails completely. The energy agreement is a coincidence derived from a symmetry Bohr did not know about.

**"$\Delta m = 0$ means only transitions that do not change $m$ are allowed."** The selection rule is $\Delta m = 0, \pm 1$: all three are allowed, corresponding to the three polarization states of the emitted photon. Only $\Delta m = \pm 2$, etc., are forbidden by dipole selection.

---

## Exercises

### Warm-up

**9.1** The reduced mass of ordinary hydrogen is $\mu = m_pm_e/(m_p + m_e)$, where $m_p \approx 1836\,m_e$. (a) Compute $\mu$ to four significant figures in units of $m_e$. (b) By what fractional amount does using the exact $\mu$ rather than $m_e$ change $a_0 = 4\pi\epsilon_0\hbar^2/(\mu e^2)$? (c) A muonic hydrogen atom replaces the electron with a muon ($m_\mu \approx 207\,m_e$). Compute the muonic Bohr radius $a_0^\mu$ and ground-state energy $E_1^\mu$. By what factors do they differ from ordinary hydrogen?

**9.2** Verify that $\psi_{100}(r) = (\pi a_0^3)^{-1/2}e^{-r/a_0}$ is normalized. Use $\int_0^\infty r^2 e^{-2r/a_0}\,dr = a_0^3/4$. Write the radial probability density $P(r) = r^2|R_{10}(r)|^2$ and verify $\int_0^\infty P(r)\,dr = 1$.

**9.3** List all allowed $(n, \ell, m)$ combinations for $n = 3$. Verify the count gives $n^2 = 9$ orbital states and $2n^2 = 18$ with spin. For each of the three constraints on quantum numbers, write one sentence explaining its mathematical origin.

### Application

**9.4** The 2s radial wave function is $R_{20}(r) = (8a_0^3)^{-1/2}(2 - r/a_0)e^{-r/(2a_0)}$. (a) Find the radial node — the value of $r$ at which $R_{20} = 0$. (b) Find $r_\text{mp}$ for the 2s state by maximizing $P(r) = r^2|R_{20}|^2$. (c) Compute $\langle r\rangle_{2s}$ using $\int_0^\infty r^n e^{-r/b}\,dr = n!\,b^{n+1}$. Do $r_\text{mp}$ and $\langle r\rangle$ still differ? Why?

**9.5** (a) Compute the wavelength of the Lyman $\alpha$ line ($n = 2 \to n = 1$) and confirm it falls in the ultraviolet. (b) Compute the wavelength of the Paschen $\alpha$ line ($n = 4 \to n = 3$) and confirm it falls in the near-infrared. (c) Estimate the isotope shift in nm between ordinary hydrogen and deuterium ($m_d \approx 2m_p$) at the Balmer $\alpha$ line, and explain why Urey could detect it in 1932.

**9.6** For each of the following transitions, state whether it is electric-dipole allowed or forbidden and give the reason: (a) $3p \to 1s$; (b) $3d \to 1s$; (c) $3p \to 2p$; (d) $3d \to 2p$; (e) $2s \to 1s$. For each forbidden transition, name one process through which it can still occur.

**9.7** The general formula $\langle r\rangle_{n\ell} = (a_0/2)[3n^2 - \ell(\ell+1)]$ gives the mean radius for any state. (a) Verify it for $(n,\ell) = (1,0)$ and $(2,0)$. (b) For fixed $n$, does increasing $\ell$ increase or decrease $\langle r\rangle$? Use the centrifugal-barrier picture to explain why. (c) For $(3,2)$, compute $\langle r\rangle$ and compare it to the estimate $r_\text{mp} \approx n^2 a_0$.

### Synthesis

**9.8** The $\mathfrak{so}(4)$ symmetry of hydrogen makes 2s and 2p degenerate. In sodium, the effective potential breaks this degeneracy: the 3s level sits at $-5.14$ eV and 3p at $-3.04$ eV. (a) Without measuring energy, what observable could distinguish 2s from 2p in hydrogen? (b) Compute the wavelength of the sodium $3p \to 3s$ transition. (c) The sodium D line is a doublet at 589.0 nm and 589.6 nm. What interaction splits the 3p level into two? Name the effect.

**9.9** Consider the superposition $\Psi(r,t) = (1/\sqrt{2})[\psi_{100}e^{-iE_1t/\hbar} + \psi_{210}e^{-iE_2t/\hbar}]$. (a) Show that $|\Psi|^2$ contains a cross-term oscillating at $\omega_{12} = (E_2 - E_1)/\hbar$. Compute $\omega_{12}$ in rad/s and the period $T_{12}$ in femtoseconds. (b) Compute $\langle z\rangle(t)$ and show it oscillates at $\omega_{12}$. (c) Explain in two sentences why the oscillating dipole moment represents the atom in the act of emitting a photon, rather than sitting in either stationary state.

### Challenge

**9.10** The $n^2$ orbital degeneracy follows from $\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$. Prove this identity by induction or by pairing terms. Then: in a hypothetical atom where energy depends on $n_r + \ell + 1$ (with $n_r = n - \ell - 1$ radial nodes), how many orbital states share energy level $N = n_r + \ell + 1$? Compare to hydrogen and explain in one sentence what makes Coulomb degeneracy special.

---

## Still Puzzling

There is one thing I cannot make feel inevitable, and I want to say so honestly.

The Laplace–Runge–Lenz vector is conserved classically because $1/r$ orbits do not precess, and Bertrand's theorem tells you that only $1/r$ and $r^2$ potentials have all bound orbits closed. The quantum $\mathfrak{so}(4)$ degeneracy and the classical closed-orbit property must be the same fact in two languages. The algebra is settled; the commutators are well-defined; the derivation is correct. But I cannot make the connection feel obvious in the sense of "of course it had to be this way." If it ever becomes clear to you, let me know.

A separate question: the hydrogen atom has exact analytic solutions only because the Coulomb potential is exactly $1/r$ and only because there is one electron. Helium has two electrons and no exact solution. The interaction between the electrons breaks the $\mathfrak{so}(4)$ symmetry and makes the problem analytically intractable. Everything in Chapter 10 and beyond is either an approximation scheme or a numerical method. Chapter 9 is the last time exact solutions exist.

---

## The +1 — Simulation Exercise: Hydrogen Orbital Visualizer

You are going to render $|\psi_{n\ell m}(x, 0, z)|^2$ as a 2D heat map, the radial probability density $P(r) = r^2|R_{n\ell}|^2$ with $r_\text{mp}$ and $\langle r\rangle$ marked, and an interactive energy-level diagram with selection-rule checking. Drag the $(n, \ell, m)$ sliders and watch the orbital reorganize. Click a transition to see whether it is allowed.

### Part 1 — CLAUDE.md extension

Append this block to your project's `CLAUDE.md`:

```
## Chapter 9 — Hydrogen Orbital Visualizer Rules

- Single HTML file, single SVG canvas. No three.js, no WebGL.
- Layout: primary heat-map panel (top, ~400 × 400 px), radial probability
  plot directly below it (~400 × 200 px), energy-level diagram on the right
  (~200 × 400 px). Numeric readouts at the very bottom.
- Sliders for (n, ℓ, m) in a left-hand sidebar, plus a dropdown for
  "complex Y_lm" vs. "real chemistry orbitals: p_x, p_y, p_z, d_z², ...".
- Color scale: d3.interpolateViridis, sequential. Domain rescaled per state
  to [0, max(|ψ|²)] on the rendered grid.
- Grid resolution: 200 × 200 pixels covering ±20 a₀ × ±20 a₀ in the xz-plane.
- Radial probability plot marks r_mp (peak) and ⟨r⟩ (mean) with vertical
  lines, labeled.
- Energy-level diagram: horizontal lines at E_n = −13.6/n² eV for n = 1..5,
  spectroscopic labels. Currently selected state is highlighted.
- Numeric readouts (≤ 3 sig figs, monospaced): ⟨r⟩, r_mp, E_n,
  radial nodes (n − ℓ − 1), angular nodes (ℓ), total nodes (n − 1).
- Quantum number sliders enforce constraints: ℓ ∈ [0, n−1], m ∈ [−ℓ, +ℓ].
- No DOM mutation outside the redraw function.
```

### Part 2 — The simulation prompt

```
Build me a D3 v7 hydrogen orbital visualizer following CLAUDE.md.

HOOK. Render |ψ_{nℓm}(x, 0, z)|² for the hydrogen atom as a 2D heat map
in the xz-plane. The user drags sliders for (n, ℓ, m) and the orbital
reorganizes.

UNFOLD. The hydrogen wave function factorizes:
  ψ_{nℓm}(r, θ, φ) = R_{nℓ}(r) Y_{ℓm}(θ, φ),
where R_{nℓ}(r) involves the associated Laguerre polynomial L^{2ℓ+1}_{n−ℓ−1}
and an exponential e^{−r/(n a₀)}, and Y_{ℓm}(θ, φ) is the spherical harmonic.
Set a₀ = 1 internally. Code R_{nℓ}(r) explicitly for (n, ℓ) up to (4, 3).

MECHANISM. Three coupled panels.
  (1) Primary 2D heat map: at each pixel (x, z), compute r = √(x²+z²),
      θ = atan2(x, z), φ = 0. Evaluate |ψ_{nℓm}(r, θ, 0)|² via Viridis.
  (2) Radial probability P(r) = r² |R_{nℓ}(r)|² as a line plot from
      r = 0 to r = 20 a₀. Mark r_mp and ⟨r⟩ with labeled vertical lines.
  (3) Energy-level diagram: horizontal lines at E_n = −13.6/n² eV for
      n = 1..5, spectroscopic labels. Current state highlighted.

SYNTHESIZE. Add a "Transition mode" toggle. Two state selectors:
  |ψ_i⟩ and |ψ_f⟩. Compute ΔE = E_{n_i} − E_{n_f}. Display photon
  wavelength λ = hc/ΔE in nm. Identify the spectral series (Lyman if
  n_f = 1, Balmer if 2, Paschen if 3). Check selection rules Δℓ = ±1,
  Δm = 0, ±1 and flag ALLOWED or FORBIDDEN.

Output a single self-contained HTML file using the D3 v7 CDN.
```

### Part 3 — Exploration tasks

**Verify the 1s headline numbers.** Set $(n, \ell, m) = (1, 0, 0)$. Read off $r_\text{mp}$ and $\langle r\rangle$ from the radial probability plot. Confirm $r_\text{mp} \approx 1.00\,a_0$ and $\langle r\rangle \approx 1.50\,a_0$. These are two different numbers describing one distribution. Look at the heat map: it is a spherical blob. There is no ring at $a_0$.

**Count nodes.** Set $(2, 0, 0)$. The radial probability plot should show two peaks separated by a zero at $r = 2a_0$. Set $(3, 1, 0)$: predict $n - 1 = 2$ total nodes, partitioned as 1 radial + 1 angular. Verify on the simulation.

**The $n^2$ degeneracy.** Switch among $(2,0,0)$, $(2,1,0)$, $(2,1,+1)$, $(2,1,-1)$. All four share $E = -3.4$ eV on the energy diagram. Shapes differ dramatically.

**Compute the Balmer $\alpha$ wavelength.** Transition mode. Set $(n_i, \ell_i, m_i) = (3, 1, 0)$ and $(n_f, \ell_f, m_f) = (2, 0, 0)$. Read the wavelength. Confirm $\lambda \approx 656$ nm. Verify ALLOWED.

**A forbidden transition.** Set $(2, 0, 0) \to (1, 0, 0)$. The simulation should flag FORBIDDEN ($\Delta\ell = 0$). This is the metastable 2s state.

**Real vs. complex orbitals.** Switch the dropdown from "complex $Y_{\ell m}$" to "real chemistry orbitals." Set $(n, \text{sub-shell}) = (2, p)$. Cycle through $p_x, p_y, p_z$ and watch the dumbbells rotate. Switch back to complex and cycle $m = -1, 0, +1$: the $m = 0$ case is identical to $p_z$; the $m = \pm 1$ cases are azimuthally symmetric.

### Part 4 — Extension prompt: time evolution of a superposition

```
Extend the hydrogen visualizer to a "Superposition mode."

The state is (1/√2)[ψ_{100} e^{−i E_1 t/ℏ} + ψ_{210} e^{−i E_2 t/ℏ}].
Animate |ψ(x, 0, z, t)|² in real time with a slowed-down clock.
Display "physical time" alongside the simulation frame number.
The probability density should oscillate between the 1s blob and the
2p_z dumbbell with period T_{12} = 2π / ((E_2 − E_1)/ℏ) ≈ 0.405 fs.
```

### Part 5 — Six failure modes to watch for

**Color-scale domain not reset.** If the Viridis domain is fixed at $n=1$ and not updated, high-$n$ orbitals appear uniformly dark. Recompute per state change.

**Forgetting the $r^2$ Jacobian in $P(r)$.** Plotting $|R_{n\ell}|^2$ instead of $r^2|R_{n\ell}|^2$ makes the 1s density peak at $r = 0$. The error is visible and dramatic.

**Energy formula sign error.** $E_n = -13.6/n^2$, negative. Positive values on the energy diagram mean a sign was dropped.

**Selection rule for $\Delta m$ too strict.** The rule is $\Delta m = 0, \pm 1$ — all three. Not just $\Delta m = 0$.

**Quantum number ranges not enforced.** The combination $(n, \ell, m) = (1, 1, 0)$ requires a Laguerre polynomial of degree $-1$. Constrain the sliders.

**Heat-map coordinate confusion.** For $x < 0$, $\phi = \pi$ not $\phi = 0$. The sign of $x$ must be handled correctly; otherwise the simulation renders a half-orbital.

---

## References

- J. J. Balmer, "Notiz über die Spectrallinien des Wasserstoffs," *Annalen der Physik*, 25, 80 (1885). [verify]
- N. Bohr, "On the Constitution of Atoms and Molecules," *Philosophical Magazine*, 26, 1–25 (1913). [verify]
- E. Schrödinger, "Quantisierung als Eigenwertproblem," *Annalen der Physik*, 79, 361–376 (1926). [verify]
- W. Pauli, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik," *Zeitschrift für Physik*, 36, 336–363 (1926). (Algebraic solution via the Runge–Lenz vector.) [verify]
- H. C. Urey, F. G. Brickwedde, G. M. Murphy, "A Hydrogen Isotope of Mass 2," *Physical Review*, 39, 164 (1932). [verify]
- Griffiths, D. J. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018. Chapter 4.
- Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012. Chapter 10.
- M. H. Levitt, *Spin Dynamics*, Wiley, 2001. (Reduced mass; spectroscopic series.)
- ALPHA Collaboration, "Measurement of the 1S–2S transition frequency in antihydrogen," *Nature*, 541, 506–510 (2017). [verify]
- T. Udem et al., "Absolute optical frequency measurement of the cesium $D_1$ line with a mode-locked laser," *Physical Review Letters*, 82, 3568 (1999). (Optical frequency combs in hydrogen spectroscopy.) [verify]
