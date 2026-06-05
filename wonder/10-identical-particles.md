# Chapter 10 — Identical Particles

Spectroscopists in the early 1920s catalogued the helium spectrum in fine detail. They found two distinct families of lines — one called parahelium, one called orthohelium — with different transition rates, different selection rules, different fine-structure patterns. They looked like spectra of two different elements.

Helium is one element: nuclear charge $+2e$, two electrons, nothing else. So why two spectral families?

Werner Heisenberg resolved this in 1926. The resolution did not require a new force or a new particle. It required asking a question nobody had thought to ask: when you write down a wave function for two electrons, what must it satisfy purely because the electrons are identical?

---

## TL;DR

Identical quantum particles cannot be tracked individually — the labels "1" and "2" in the wave function are bookkeeping, not physics. The exchange operator has eigenvalues $\pm 1$; nature assigns $+1$ to bosons and $-1$ to fermions. The Pauli exclusion principle is not a postulate: it is the theorem that a determinant with two identical columns is zero. The helium spectrum splits into two families because antisymmetry, not a spin-spin force, determines whether electrons can share a spatial region.

---

## What Identical Means

In classical mechanics, two identical billiard balls can always be tracked individually. Even without painting a dot on one, you could in principle follow both through every collision — their trajectories are continuous, you never lose track of which is which.

In quantum mechanics this fails completely. The wave function $\psi(\vec{r}_1, \vec{r}_2)$ spreads each electron over a region of space. The regions overlap. When a detector fires at some position, there is no fact in nature — not merely no practical way to determine, but no fact — about which electron triggered it. The labels "1" and "2" we write into the wave function are mathematical bookkeeping. They cannot be cashed out by any measurement.

The Hamiltonian confirms this. For two electrons:

$$\hat{H}(1,2) = \frac{\hat{p}_1^2}{2m_e} + \frac{\hat{p}_2^2}{2m_e} + V(\vec{r}_1) + V(\vec{r}_2) + \frac{e^2}{4\pi\epsilon_0|\vec{r}_1 - \vec{r}_2|}.$$

Swap the subscripts 1 and 2 everywhere: $\hat{H}(1,2) = \hat{H}(2,1)$. The physics does not distinguish the two labels.

Define the exchange operator $\hat{P}_{12}\,\psi(\vec{r}_1, \vec{r}_2) = \psi(\vec{r}_2, \vec{r}_1)$. Apply it twice: $\hat{P}_{12}^2 = \mathbb{1}$. The eigenvalues $\lambda$ satisfy $\lambda^2 = 1$, giving only $\lambda = +1$ or $\lambda = -1$.

Since $\hat{H}(1,2) = \hat{H}(2,1)$, we have $[\hat{H}, \hat{P}_{12}] = 0$: the exchange operator commutes with the Hamiltonian. Energy eigenstates can be chosen with definite exchange symmetry, and that symmetry is conserved under time evolution.

The empirical postulate — confirmed universally and explained by the spin-statistics theorem of relativistic quantum field theory — is:

**Bosons** have symmetric wave functions ($\hat{P}_{12}\psi = +\psi$): integer spin. Photons, the Higgs, $^4$He atoms.

**Fermions** have antisymmetric wave functions ($\hat{P}_{12}\psi = -\psi$): half-integer spin. Electrons, protons, neutrons.

Composite particles inherit their statistics by counting constituent fermions: an even number makes a boson, an odd number makes a fermion. The consequences are dramatic. $^4$He has 6 constituent fermions (even) and becomes superfluid at 2.17 K. $^3$He has 5 (odd), is a fermion, and becomes superfluid only at 2.5 mK — three orders of magnitude colder, from a single parity count.

<!-- → [TABLE: Statistics of common particles — photon spin-1 boson; electron spin-1/2 fermion; proton spin-1/2 fermion (3 quarks); ⁴He spin-0 boson (6 fermions) superfluid 2.17 K; ³He spin-1/2 fermion (5 fermions) superfluid 2.5 mK; ⁸⁷Rb integer boson first dilute-gas BEC 1995] -->

---

## Antisymmetry Built In

For two fermions in single-particle states $\phi_a$ and $\phi_b$, the antisymmetric wave function is:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)\bigr].$$

John Slater noticed in 1929 that this is a $2\times2$ determinant:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\det\begin{pmatrix}\phi_a(1) & \phi_b(1) \\ \phi_a(2) & \phi_b(2)\end{pmatrix}.$$

Swapping particles swaps rows. Swapping rows flips the sign of a determinant. Antisymmetry is now a property of matrix structure, enforced automatically by the algebra.

The construction extends to $N$ fermions. Build the $N\times N$ matrix where entry $(i,j)$ is the $i$-th single-particle orbital evaluated at the $j$-th particle's coordinates. The **Slater determinant** is:

$$\psi(1,\ldots,N) = \frac{1}{\sqrt{N!}}\det\begin{pmatrix}\phi_1(1)&\phi_2(1)&\cdots&\phi_N(1)\\\phi_1(2)&\phi_2(2)&\cdots&\phi_N(2)\\\vdots&&\ddots&\vdots\\\phi_1(N)&\phi_2(N)&\cdots&\phi_N(N)\end{pmatrix}.$$

Swapping any two particles swaps two rows, flipping the sign. The $1/\sqrt{N!}$ is the normalization — all $N!$ terms in the expansion are orthogonal when the $\phi_i$ are orthonormal.

This is the wave function ansatz on which all of computational quantum chemistry is built. Hartree-Fock theory minimizes $\langle\psi|\hat{H}|\psi\rangle$ over the choice of single-particle orbitals $\{\phi_i\}$, with the $N$-electron state constrained to a single Slater determinant. Configuration interaction, coupled-cluster theory, and many density-functional approaches are corrections to or extensions of this starting point.

---

## Pauli Exclusion as a Theorem

Now suppose two of the single-particle orbitals are identical: $\phi_i = \phi_j$ for some $i \neq j$. Two columns of the Slater determinant are identical. A determinant with two identical columns is exactly zero — not approximately zero, not zero in some limit, identically zero everywhere in configuration space.

A wave function that is identically zero cannot be normalized. It is not a state. Two fermions cannot occupy the same single-particle orbital.

This is the **Pauli exclusion principle**. Pauli stated it in 1925 as an empirical rule — no two electrons in an atom can share the same quantum numbers $(n, \ell, m_\ell, m_s)$ — because it explained the periodic table and he could not find a reason to reject it. He received the Nobel Prize in 1945 partly for it. But as he stated it, the rule was a phenomenological postulate with no derivation. Slater showed four years later that it is a theorem about determinants, not an independent assumption.

The determinant form matters because it generalizes. The quantum numbers $(n, \ell, m_\ell, m_s)$ are labels specific to atomic orbitals. In a solid-state system the relevant labels are band indices and crystal momenta — different labels, same physics. The antisymmetry argument survives unchanged in both contexts.

---

## Worked Example — Building the Antisymmetric Two-Electron State

Put both electrons in the 1s spatial orbital of helium, with spin-orbitals $\phi_A = \psi_{100}\chi_\uparrow$ and $\phi_B = \psi_{100}\chi_\downarrow$.

**The Slater determinant:**

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_B(2) - \phi_B(1)\phi_A(2)\bigr] = \psi_{100}(\vec{r}_1)\psi_{100}(\vec{r}_2)\cdot\frac{1}{\sqrt{2}}\bigl[\chi_\uparrow(m_{s1})\chi_\downarrow(m_{s2}) - \chi_\downarrow(m_{s1})\chi_\uparrow(m_{s2})\bigr].$$

The spatial part is symmetric; the spin part is antisymmetric — the spin singlet $|S=0, M_S=0\rangle$. Total: symmetric $\times$ antisymmetric = antisymmetric. ✓

**Attempt to put both electrons in the same spin-orbital**, say $\phi_A = \phi_B = \psi_{100}\chi_\uparrow$:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_A(2) - \phi_A(1)\phi_A(2)\bigr] = 0.$$

Identically zero. Two electrons in the 1s orbital must have opposite spins — not by postulate, but because the determinant with two identical columns is zero.

---

## Helium and the Exchange Integral

Return to the opening question. Helium's Hamiltonian is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla_1^2 - \frac{\hbar^2}{2m_e}\nabla_2^2 - \frac{2e^2}{4\pi\epsilon_0 r_1} - \frac{2e^2}{4\pi\epsilon_0 r_2} + \underbrace{\frac{e^2}{4\pi\epsilon_0|\vec{r}_1-\vec{r}_2|}}_{V_{12}}.$$

The electron-electron repulsion $V_{12}$ makes this analytically insoluble. Treat it as a perturbation on the exactly-solved two-electron hydrogenic problem.

The total wave function must be antisymmetric. From Chapter 8, two-spin states split into a singlet (antisymmetric, $S = 0$) and a triplet (symmetric, $S = 1$). Pairing with spatial parts:

**Parahelium**: symmetric spatial $\times$ singlet spin. $S = 0$.

**Orthohelium**: antisymmetric spatial $\times$ triplet spin. $S = 1$.

Both total wave functions are antisymmetric. Both are physical. And the helium ground state is necessarily parahelium: the only $1s^2$ spatial wave function is $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)$, which is symmetric, so the spin must be the singlet. The antisymmetric spatial combination $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2) - \phi_{1s}(\vec{r}_2)\phi_{1s}(\vec{r}_1) = 0$ vanishes by Pauli — no $1s^2$ orthohelium ground state exists.

For the 1s2s excited configuration, the two antisymmetric states are:

$$\psi_\pm = \frac{1}{\sqrt{2}}\bigl[\phi_{1s}(\vec{r}_1)\phi_{2s}(\vec{r}_2) \pm \phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\bigr]\times\begin{cases}\chi_\text{singlet} & (+)\\\chi_\text{triplet} & (-)\end{cases}.$$

First-order perturbation theory gives the Coulomb correction:

$$\langle V_{12}\rangle_\pm = J \pm K,$$

where

$$J = \iint |\phi_{1s}(\vec{r}_1)|^2\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}|\phi_{2s}(\vec{r}_2)|^2\,d^3r_1\,d^3r_2$$

is the **direct integral** — the classical Coulomb energy between the two charge densities $|\phi_{1s}|^2$ and $|\phi_{2s}|^2$. A classical physicist could write this down.

$$K = \iint \phi_{1s}^*(\vec{r}_1)\phi_{2s}^*(\vec{r}_2)\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}\phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\,d^3r_1\,d^3r_2$$

is the **exchange integral** — the cross-term generated by antisymmetrization, swapping which electron is "in 1s" and which is "in 2s." It has no classical analog whatsoever. For real orbitals and the positive Coulomb kernel $1/r_{12} > 0$, the integrand of $K$ is non-negative everywhere, so $K > 0$.

Result: parahelium 1s2s has energy $E^{(0)} + J + K$; orthohelium 1s2s has $E^{(0)} + J - K$. Since $K > 0$, orthohelium lies lower by $2K \approx 0.80$ eV — a large, observable splitting.

The mechanism, stated precisely:

$S = 1$ (triplet) requires antisymmetric spatial wave function. The antisymmetric $\psi_-$ vanishes when $\vec{r}_1 = \vec{r}_2$. Electrons in $\psi_-$ stay farther apart on average. Farther apart means less Coulomb repulsion. Lower energy.

Spin determines which spatial symmetry class is required. The spatial wave function determines how close the electrons approach. Proximity determines Coulomb repulsion. No spin-dependent force appears anywhere in this chain. What looked like two spectral families from a spin-spin interaction is entirely a consequence of the antisymmetry requirement and the geometry of wave functions.

---

## Hund's First Rule

In 1925 Friedrich Hund catalogued an empirical regularity: for a given electron configuration in a partially filled subshell, the term with highest total spin has the lowest energy. This is Hund's first rule.

It is not a separate postulate. The mechanism is the exchange integral. Higher $S$ requires a more antisymmetric spatial wave function, which keeps electrons farther apart on average, which reduces Coulomb repulsion. The rule is a corollary of antisymmetry applied to multi-electron atoms.

Oxygen ($1s^2\,2s^2\,2p^4$): the three $2p$ orbitals hold four electrons. Hund's rule says fill each orbital with one electron (parallel spins) before pairing. The ground state has $S = 1$, two unpaired electrons, and is paramagnetic. The $S = 1$ configuration is lower in energy because its antisymmetric spatial wave function keeps the four electrons farther apart. That is why oxygen is a magnet.

---

## The Periodic Table

Three facts combine to produce the structure of the periodic table.

**Screening breaks hydrogenic degeneracy.** In a multi-electron atom, inner electrons partially shield the nuclear charge from outer electrons. Orbitals with low $\ell$ penetrate closer to the nucleus and are less effectively screened; at fixed $n$, low-$\ell$ states lie below high-$\ell$ states. The $n^2$-fold Coulomb degeneracy of hydrogen breaks. The 2s lies below 2p in lithium; the 3d lies above 4s in potassium.

**Pauli exclusion limits occupancy.** Each spin-orbital holds exactly one electron. Each spatial orbital holds at most two — one spin-up, one spin-down — and only with opposite spins. Without this, every electron in every atom would collapse to the 1s orbital. There would be no chemistry.

**Hund's rule fills partially occupied subshells.** Within a subshell, different $m_\ell$ orbitals fill with parallel spins before pairing. The exchange energy stabilizes the high-$S$ configuration.

The Aufbau principle combines all three: fill orbitals in order of increasing energy (lowest $n + \ell$ first, ties broken by lowest $n$), two electrons per orbital, parallel spins first within a subshell. The sequence is $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, \ldots$ Row lengths $2, 8, 8, 18, 18, 32$ follow from $2(2\ell + 1)$ summed over the subshells in each period — twice the orbital degeneracy, the factor of 2 from spin.

About twenty atoms violate the Madelung energy ordering. Chromium ($3d^5\,4s^1$ rather than $3d^4\,4s^2$) and copper ($3d^{10}\,4s^1$ rather than $3d^9\,4s^2$) are the standard examples: exchange-energy stabilization of a half-filled or completely-filled 3d subshell wins against the small 3d-4s energy gap. These are not anomalies; they are cases where Hund's exchange stabilization barely beats the Madelung ordering.

The periodic table is not a catalogue of patterns. It is a theorem about antisymmetric wave functions, screened Coulomb potentials, and first-order perturbation theory.

---

## Bosons, Briefly

Bosons have symmetric wave functions. Nothing prevents any number of them from occupying the same single-particle state. At low temperature and high density, a macroscopic fraction can pile into the lowest-energy state — Bose-Einstein condensation. Cornell and Wieman achieved the first dilute-gas BEC in $^{87}$Rb at JILA in 1995, cooling the atoms to roughly 170 nK. Nobel Prize 2001.

One misconception worth naming: bosons are not attracted to each other and fermions are not repelled by each other in the sense of forces. There is no term in the Hamiltonian encoding exchange statistics. What exists is a correlation in the joint probability density $|\psi(\vec{r}_1, \vec{r}_2)|^2$ from the symmetrization: fermions have a Pauli node at $\vec{r}_1 = \vec{r}_2$ (the antisymmetric wave function vanishes there); bosons have enhanced probability at $\vec{r}_1 = \vec{r}_2$ (the symmetric wave function peaks on the diagonal). The single-particle marginal density $\int|\psi|^2\,d^3r_2$ is identical for bosons, fermions, and distinguishable particles in the same pair of single-particle states. A single-particle detector cannot distinguish them.

The fermion node also holds up dead stars. Electrons in a white dwarf cannot share single-particle states; as the star contracts, electrons are forced into higher-energy states, generating an outward degeneracy pressure with no thermal origin. Chandrasekhar showed in 1931 that this pressure has a relativistic limit at approximately $1.4\,M_\odot$ — above which no equilibrium exists and gravitational collapse is inevitable. He did this calculation at age 19 on a steamship from India to England. Nobel Prize 1983.

---

## The +1 — Simulation Exercise: Two-Particle Symmetry Explorer

The deliverable is a simulation that renders $|\psi(x_1, x_2)|^2$ for two particles in a 1D infinite well, with a toggle for boson / fermion / distinguishable. The Pauli node, bosonic clustering, and the invariance of the marginal density are made visible as the user adjusts the sliders.

### CLAUDE.md Extension

Append this block to your project's `CLAUDE.md`:

````markdown
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
````

### The Simulation Prompt

````
Build me a D3 v7 two-particle symmetry explorer following CLAUDE.md.

SHOW.
Single-particle eigenstates: φ_n(x) = √(2/L) sin(nπx/L).
Two-particle wave functions:
  ψ_boson  = (1/√2)[φ_a(x₁)φ_b(x₂) + φ_b(x₁)φ_a(x₂)]
  ψ_fermion = (1/√2)[φ_a(x₁)φ_b(x₂) − φ_b(x₁)φ_a(x₂)]
  ψ_dist   = φ_a(x₁)φ_b(x₂)
Special case: ψ_fermion = 0 when n_a = n_b. Show status note.

SAY.
Two coupled panels.
  (1) 2D heat map of |ψ(x₁, x₂)|² with diagonal overlay.
  (2) Marginal ρ(x₁) = ∫|ψ(x₁, x₂)|² dx₂ as a line plot. This marginal
      is identical for boson, fermion, and distinguishable at the same
      (n_a, n_b) — the key pedagogical point. Label it clearly.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- Normalization check: ∫∫|ψ|² dx₁ dx₂ = 1.000 per render.
- Color domain recomputed per render.
- Diagonal overlay drawn after (on top of) heat map.
- Add "Spin extension" toggle: singlet pairs with symmetric spatial;
  triplet pairs with antisymmetric spatial. Triplet + n_a = n_b
  shows "Pauli forbidden" status note.

VERIFY.
(a) Fermion n_a=1, n_b=2: Pauli node visible on diagonal.
(b) Fermion n_a=n_b=1: status note shown, heat map blank.
(c) Boson n_a=n_b=1: single peak, diagonal runs through it.
(d) At any (n_a, n_b): marginal line plot is identical for all three modes.
(e) ∫∫|ψ|² = 1.000 for all combinations.
````

### Exploration Tasks

**The Pauli node.** Set fermion, $n_a = 1$, $n_b = 2$. The diagonal is a stripe of zero. Set $n_a = n_b = 1$: the status note appears. Two fermions cannot be in the same orbital — the wave function simply doesn't exist.

**Bosonic clustering.** Switch to boson, $n_a = n_b = 1$. The heat map shows a single peak with the diagonal running through it. Bosons share orbitals without restriction.

**The marginal is exchange-blind.** Set $n_a = 1$, $n_b = 2$. Cycle through boson, fermion, distinguishable and watch the heat map change dramatically while the marginal line plot stays identical. A single-particle detector cannot distinguish the three cases.

**Helium analog with spin extension.** Toggle spin extension. Select singlet, $n_a = n_b = 1$: the symmetric spatial wave function is allowed — parahelium ground state. Select triplet, $n_a = n_b = 1$: Pauli forbidden. For 1s2s ($n_a = 1$, $n_b = 2$): singlet gives symmetric heat map, triplet gives antisymmetric heat map with Pauli node. The energy advantage of orthohelium (electrons farther apart along the off-diagonal) is geometrically visible.

---

## References

- Pauli, W. (1925). "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren." *Zeitschrift für Physik*, 31, 765–783.
- Slater, J.C. (1929). "The Theory of Complex Spectra." *Physical Review*, 34, 1293–1322.
- Heisenberg, W. (1926). "Mehrköperproblem und Resonanz in der Quantenmechanik." *Zeitschrift für Physik*, 38, 411–426.
- Pauli, W. (1940). "The Connection Between Spin and Statistics." *Physical Review*, 58, 716–722.
- Chandrasekhar, S. (1931). "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal*, 74, 81–82.
- Anderson, M.H. et al. (1995). "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science*, 269, 198–201.
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 5.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapter 11.
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 7.

---

## Running Project — Build the Atom

**This chapter adds:** antisymmetry and exclusion — the Slater determinant of one-electron spin-orbitals as the many-electron state, Pauli exclusion as the theorem that no two electrons share a spin-orbital, and the exchange integral $K>0$ that is the mechanism behind Hund's first rule (maximize $S$) and the Cr/Cu anomalies.

The atom-builder fills orbitals one at a time, but the *state* is a single antisymmetric object: a Slater determinant. This chapter makes that exact — the determinant vanishes if two columns (spin-orbitals) coincide, which *is* Pauli exclusion, the rule that limits each spin-orbital to one electron. And the exchange integral $K$ that drops out of antisymmetrization is precisely why parallel spins lower the energy — Hund's Rule 1 — and why $\text{Cr}=[\text{Ar}]3d^54s^1$ beats the Madelung prediction. This is the piece that turns a filling list into a physical, exclusion-respecting configuration.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Coding a Slater-determinant builder from a list of $N$ spin-orbital functions (an $N\times N$ matrix evaluated at $N$ coordinates, then `numpy.linalg.det`) — *Why AI works here:* it is matrix construction; you check that swapping two particles flips the sign and that duplicating a spin-orbital gives exactly zero.
- Writing the Aufbau filler that places electrons into spin-orbitals in Madelung order, two per spatial orbital, enforcing exclusion — *Why AI works here:* it is bookkeeping over the capacity table; you verify against known configurations (carbon $1s^22s^22p^2$).

**The tell:** You are using AI well when you have an exact check — a determinant with a repeated column is identically zero, and total electron count must equal $Z$.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding which configuration wins when exchange stabilization competes with orbital energy (Cr, Cu) — *Why AI fails here:* this is a quantitative energy comparison (exchange gain vs. the small $3d$–$4s$ gap); an LLM will often "fix" chromium by recall rather than by comparing $K$-weighted parallel-pair counts, and gets adjacent elements wrong.
- Asserting that Hund's Rule 1 comes from a spin–spin force — *Why AI fails here:* the mechanism is purely the exchange integral and spatial antisymmetry (no spin-dependent force in the Hamiltonian); an LLM that narrates a magnetic spin interaction encodes the wrong physics into your explanation.

**The tell:** If you cannot explain why parallel spins lower the energy — antisymmetric spatial wavefunction, electrons farther apart, less repulsion — without the AI, the AI did the physics that should have been yours.
**Physics-judgment connection:** this trains checking an antisymmetry construction against its exact zeros (repeated spin-orbital → null state) and grounding every energy-ordering claim in the exchange integral rather than an invented force.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a module `slater.py` that builds Slater determinants, enforces Pauli exclusion, and fills configurations by Aufbau.
**Tool:** Claude chat.
**The Prompt:**
```
I am building an atomic-structure simulator. I need the many-electron layer:
Slater determinants, Pauli exclusion, and Aufbau filling.

Write a Python module `slater.py` (numpy only) that:

1. slater_determinant(orbitals, coords): given N single-particle orbital
   callables and N coordinate points, build the NxN matrix M[i][j] =
   orbital_i(coord_j) and return det(M)/sqrt(N!). Demonstrate that swapping two
   coords flips the sign and that two identical orbitals give exactly 0.
2. fill_configuration(Z, madelung_order): place Z electrons into spin-orbitals
   in the given Madelung subshell order, max 2(2l+1) per subshell, returning the
   configuration string (e.g. '1s2 2s2 2p2' for Z=6) and the list of occupied
   (n,l,m_l,m_s) spin-orbitals. Enforce exclusion (no spin-orbital twice).
3. parallel_pairs(occupied): count pairs of electrons in the SAME subshell with
   the SAME spin (the exchange-stabilization proxy).
4. __main__: fill Z=6 (expect 1s2 2s2 2p2) and Z=10 (expect 1s2 2s2 2p6);
   assert a determinant with a duplicated spin-orbital is 0; print parallel_pairs
   for a half-filled p^3 (expect 3 parallel pairs among the three unpaired up
   spins).

Do NOT resolve the Cr/Cu anomalies here (that needs an exchange-energy
comparison in the capstone). Use the plain Madelung order. Comment that Pauli
exclusion is a THEOREM about determinants, not a separate postulate.
```
**What this produces:** `slater.py` — antisymmetric state construction, exclusion-respecting filling, and the parallel-pair count feeding Hund's Rule 1.
**How to adapt:** *Your system:* the determinant demo can use toy 1D orbitals; the filling logic is what the simulator actually uses. *ChatGPT/Gemini:* same prompt; ask for the oxygen $2p^4$ unpaired-electron count (expect 2). *Claude Project:* keep with the physics core — the capstone adds the Cr/Cu exchange comparison.
**Builds on:** Chapter 9's hydrogenic spin-orbitals (the determinant's columns).  **Next:** Chapter 11 assembles all modules into the full atom-builder and validates against NIST.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the Slater/Aufbau module plus tests on exclusion, configurations, and parallel pairs.
**Tool:** Claude Code.
**Skill level:** Advanced
**Setup — confirm:**
- [ ] `subshells.py`, `spin.py`, `hydrogenic.py` present.
- [ ] `numpy`, `pytest`.
- [ ] CLAUDE.md rules from Chapters 1–9 present.
**The Task:**
```
In build-the-atom/, create slater.py with slater_determinant(orbitals, coords),
fill_configuration(Z, madelung_order), and parallel_pairs(occupied).

Create test_slater.py: (a) a determinant with two identical spin-orbitals is 0
to 1e-12; (b) swapping two coordinates flips the determinant's sign; (c)
fill_configuration(6) == '1s2 2s2 2p2' and total electrons == 6; (d)
fill_configuration(18) == '1s2 2s2 2p6 3s2 3p6'; (e) parallel_pairs for a
half-filled p^3 (3 unpaired parallel spins) == 3.

Run `pytest -q` and show output. Use plain Madelung order; do NOT special-case
Cr or Cu. Modify no other module.
```
**Expected output:** `slater.py`, `test_slater.py`, passing `pytest`.
**What to inspect:** confirm the repeated-orbital determinant is exactly zero (Pauli as a theorem); confirm the sign flip on particle swap; confirm carbon and argon configurations; confirm the parallel-pair count for $p^3$.
**If it goes wrong:** if `fill_configuration` overfills a subshell (e.g. 3 electrons in an $s$ orbital), the capacity guard is missing. Recovery: assert each subshell occupancy $\le 2(2\ell+1)$ and total $=Z$ before returning.
**CLAUDE.md / AGENTS.md note:** add — "The many-electron state is a single Slater determinant; Pauli exclusion is enforced structurally (no spin-orbital occupied twice). Cr/Cu anomalies are handled only in the capstone via exchange-energy comparison."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `slater.py` antisymmetry/filling module from R3/R4.
**Validation type:** Code
**Risk level:** Medium–High — this enforces exclusion and produces the configurations the whole project predicts; a filling bug invalidates every result.
**Setup:** use your R3/R4 artifact.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Identical Particles
□ Correctness: is a determinant with a repeated spin-orbital exactly 0?
□ Completeness: does particle exchange flip the determinant's sign?
□ Scope: did it avoid special-casing Cr/Cu (capstone territory)?
□ Physics criterion 1: does fill_configuration give 1s2 2s2 2p2 for Z=6 and the
  argon configuration for Z=18, with total electrons == Z?
□ Physics criterion 2: does parallel_pairs correctly count same-subshell
  same-spin pairs (the exchange-stabilization proxy)?
□ Failure-mode check: any of —
  - fluent but wrong (exclusion not enforced; subshell overfilled)
  - determinant sign convention dropped (no antisymmetry)
  - Hund Rule 1 explained via a (nonexistent) spin-spin force
  - Cr/Cu hard-coded here instead of derived later
```
**What to do with findings:** pass → use it, noting the repeated-column-zero test is what made it trustworthy; one fail → add the capacity guard and re-run; multiple fails → rebuild the filler against hand-checked carbon/argon configurations.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI built the Slater-determinant constructor and the Aufbau filler, which I checked against the exact repeated-column zero and known configurations.
> *2:* The AI could not be trusted to resolve the Cr/Cu anomalies or to ground Hund's Rule 1 in the exchange integral rather than a spin force — both required my physical judgment.
**Physics-judgment connection:** validating an antisymmetry construction against its exact zeros and electron-count conservation, and insisting every energy-ordering claim trace to the exchange integral.

---

*Chapter 11 follows: scattering theory. Two electrons collide; their antisymmetric wave function produces a correlation in the differential cross-section — the exchange scattering amplitude. Identical-particle statistics makes a measurable difference even in collision experiments.*
