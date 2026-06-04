# Research Notes: Chapter 10 — Identical Particles

**Corresponding chapter:** chapters/10-identical-particles.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to: (1) construct an antisymmetric two-electron wave function using the Slater determinant formalism; (2) derive the Pauli exclusion principle as a corollary of antisymmetry rather than a separate postulate; (3) compute first-order Coulomb corrections for the helium atom, isolating the direct (J) and exchange (K) integrals; (4) explain the para/orthohelium spectral split and Hund's first rule as consequences of the same exchange mechanism; (5) apply the spin-statistics connection to composite particles.

---

## A. Conceptual foundations

### Indistinguishability

- In classical mechanics, identical particles can be tracked by continuous trajectories ("paint a dot"). In QM, the wave function spreads over configuration space; labels "1" and "2" are bookkeeping, not physical tags. No measurement can distinguish them — not just in practice, but in principle. (_lib_qmsri-08, section "What identical means")
- For two identical particles, the Hamiltonian is symmetric under exchange: $\hat{H}(1,2) = \hat{H}(2,1)$. Therefore $[\hat{H}, \hat{P}_{12}] = 0$.

### Exchange operator and eigenvalues

- Define $\hat{P}_{12}\psi(\vec{r}_1,\vec{r}_2) = \psi(\vec{r}_2,\vec{r}_1)$.
- $\hat{P}_{12}^2 = \mathbb{1}$ forces eigenvalues $\lambda = \pm 1$.
- Since $[\hat{H},\hat{P}_{12}]=0$, energy eigenstates may be chosen with definite exchange symmetry; once chosen, that symmetry is conserved.
- Empirical/postulated: every species has a fixed symmetry forever.
  - Bosons (integer spin): $\hat{P}_{12}\psi = +\psi$
  - Fermions (half-integer spin): $\hat{P}_{12}\psi = -\psi$

### Spin-statistics theorem

- The connection between spin and statistics follows from Pauli's 1940 proof using microcausality in relativistic QFT: integer-spin fields must commute (bosons), half-integer must anticommute (fermions).
- At the non-relativistic level this is accepted as a postulate. The chain of derivation runs: spin-statistics theorem → symmetrization postulate → antisymmetry → Slater determinant → Pauli exclusion. (Both _lib sources are explicit that the deeper proof is unavailable here.)

### Antisymmetric two-particle wave function

For two fermions in single-particle states $\phi_a$, $\phi_b$:
$$\psi_-(1,2) = \frac{1}{\sqrt{2}}[\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)]$$
Written as a 2×2 Slater determinant (Slater 1929): antisymmetry is now a property of the matrix algebra — swapping rows flips determinant sign. (_lib_qmsri-08, section "Antisymmetry built into the wave function")

### N-particle Slater determinant

$$\psi(1,\ldots,N) = \frac{1}{\sqrt{N!}}\det\begin{pmatrix}\phi_1(1) & \cdots & \phi_N(1)\\ \vdots & & \vdots \\ \phi_1(N) & \cdots & \phi_N(N)\end{pmatrix}$$

Swapping any two particles swaps two rows → sign flip → correct antisymmetry for all $N$. The $N=3$ expansion gives six terms with alternating signs (one per permutation weighted by its sign). Hartree-Fock theory — the workhorse of computational quantum chemistry — minimizes $\langle\hat{H}\rangle$ over the single-particle orbitals in this ansatz. (_lib_qmsri-08)

### Pauli exclusion as a corollary

If $\phi_i = \phi_j$ for any $i \neq j$, two columns of the Slater determinant are identical → determinant = 0 → wave function is identically zero → not normalizable → not a state.
- Pauli stated this empirically in 1925; Slater showed in 1929 that it is a theorem about determinants, not an independent postulate.
- The antisymmetry-derived form is more general than the quantum-number form: it survives unchanged in solid-state systems where the relevant labels are band index and crystal momentum, not $(n,\ell,m_\ell,m_s)$.

### Symmetric wave function (bosons, brief)

Nothing prevents $10^{23}$ bosons in the same state. Bose-Einstein condensation: at low temperature the ground single-particle state becomes macroscopically occupied. First experimental BEC in a dilute gas: Cornell, Wieman, Ketterle (JILA, 1995), $^{87}$Rb at ~170 nK. Nobel Prize 2001.
- Fermions: Pauli node at $\vec{r}_1 = \vec{r}_2$; bosons: enhanced joint probability at $\vec{r}_1 = \vec{r}_2$. Neither is a force — it is a correlation in the joint probability density. The marginal single-particle density is unchanged by exchange statistics.

### Degeneracy pressure and Chandrasekhar mass

The Pauli node prevents electrons in a white dwarf from sharing states. As the star contracts, electrons fill higher-energy states → kinetic energy rises → outward degeneracy pressure. No thermal origin. Chandrasekhar (1931, age 19): relativistic limit at ~$1.4 M_\odot$ above which relativistic degeneracy pressure fails to support gravity → collapse. Nobel Prize 1983. (_lib_qmsri-08, section "Bosons, briefly")

---

## B. Domain examples and cases

### Helium: para vs orthohelium

Two-electron helium has two distinct spectral families known historically as "parahelium" and "orthohelium," appearing in spectroscopy as if two different elements. Heisenberg (1926) resolved this.

The total wave function must be antisymmetric. Spin states decompose into singlet (antisymmetric, $S=0$) and triplet (symmetric, $S=1$). Two allowed antisymmetric total wave functions:
- **Parahelium**: symmetric spatial × antisymmetric spin (singlet). $S=0$.
- **Orthohelium**: antisymmetric spatial × symmetric spin (triplet). $S=1$.

Ground state of helium must be parahelium: attempting the $1s^2$ orthohelium ground state requires an antisymmetric spatial wave function built from two identical 1s orbitals, which vanishes identically (Pauli).

### Direct (J) and exchange (K) integrals for helium 1s2s

First-order perturbation theory for $V_{12} = e^2/(4\pi\epsilon_0|\vec{r}_1-\vec{r}_2|)$:
$$\langle V_{12}\rangle_\pm = J \pm K$$

- $J$ (direct integral): classical Coulomb interaction between two charge densities $|\phi_{1s}|^2$ and $|\phi_{2s}|^2$. A classical physicist could write this.
- $K$ (exchange integral): the cross-term $\int\int\phi^*_{1s}(\vec{r}_1)\phi^*_{2s}(\vec{r}_2)\frac{e^2}{4\pi\epsilon_0 r_{12}}\phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)d^3r_1d^3r_2$. No classical analog; comes entirely from antisymmetrization cross-terms. For real orbitals and positive Coulomb kernel, $K > 0$.

Parahelium 1s2s: $E^{(0)}+J+K$; orthohelium 1s2s: $E^{(0)}+J-K$. Splitting = $2K \approx 0.80$ eV (measurable, large, historically attributed incorrectly to a spin-dependent force).

Mechanism: antisymmetric spatial → electrons avoid $\vec{r}_1 = \vec{r}_2$ → less Coulomb repulsion → lower energy. No spin-dependent force in the Hamiltonian.

### Hund's first rule as a corollary

Higher $S$ → more symmetric spin → more antisymmetric spatial → electrons kept apart → lower Coulomb energy. Hund's first rule (1925 empirical catalogue: highest-$S$ term has lowest energy for a given configuration) is a corollary of antisymmetry, not a postulate. (_lib_qmsri-08; Townsend notes §5.6, Hund's rule example)

### Composite-particle statistics (counting fermions)

Even number of constituent fermions → boson; odd → fermion.
- $^4$He: 2p + 2n + 2e = 6 fermions → boson → superfluid at 2.17 K.
- $^3$He: 5 fermions → fermion → superfluid only at 2.5 mK (requires Cooper pairing). Three orders of magnitude in temperature from a single parity count. (_lib_qmsri-08)

### Simulation: two-particle symmetry explorer

The lib file (_lib_qmsri-08, "LLM Exercise") provides a complete simulation specification:
- 2D heat map of $|\psi(x_1,x_2)|^2$ for two particles in a 1D infinite well or harmonic oscillator.
- Toggle: boson / fermion / distinguishable.
- Shows Pauli node along $x_1 = x_2$ for fermions; boson clustering on diagonal.
- Marginal one-particle density is identical for all three cases — key pedagogical point.
- Spin extension: enforce total antisymmetry by pairing singlet-symmetric or triplet-antisymmetric.
- Numerical readouts: $\langle(x_1-x_2)^2\rangle$, $P(\text{both in left half})$, etc.
- Six named failure modes to watch (see lib file for full spec).

---

## C. Connections and dependencies

- **Prerequisite:** Ch 6 (spin) — the singlet/triplet decomposition is from there; the pairing of spatial and spin symmetry requires it.
- **Prerequisite:** Ch 7 (hydrogen atom) — hydrogenic orbitals $\phi_{n\ell m}$ are the building blocks for the Slater determinant and for the direct/exchange integrals in helium.
- **Forward to Ch 9 (variational method):** the helium ground-state calculation motivates the variational principle; helium's $Z_\text{eff}$ optimization ($Z_\text{eff} = 27/16 \approx 1.69$, $E \approx -77.5$ eV vs experiment $-79.0$ eV) is the first worked variational calculation.
- **Forward to Ch 10 (this chapter):** Pauli exclusion + hydrogenic orbitals + Hund's rule + screening → the periodic table argument in Ch 11.
- **Forward to condensed matter (future volumes):** the Slater determinant is the foundation of Hartree-Fock; degenerate Fermi systems, band theory, and BCS superconductivity all build from here.
- **Townsend notes (§5):** provides the full algebraic treatment of the $N$-particle case, the Slater determinant with spin, the Hund's rule example with explicit exchange integrals, and the helium variational calculation ($E_V \approx -77.4$ eV from §5.7).

---

## D. Current state of the field

- The Slater determinant as a single-configuration ansatz is the starting point for Hartree-Fock (HF) theory, developed systematically through the 1930s–1960s.
- Post-HF methods (configuration interaction, coupled-cluster, MBPT) systematically include correlation beyond a single Slater determinant.
- Density-functional theory (DFT, Kohn-Sham) replaces the many-body wave function with the electron density and an exchange-correlation functional — the fastest practical method for molecular systems. DFT ground-state energy calculations routinely achieve chemical accuracy (~1 kcal/mol).
- Spin-statistics theorem remains a theorem of relativistic QFT; no purely non-relativistic derivation exists. This is an acknowledged foundational gap (_lib_qmsri-08, "Still puzzling" section).
- Anyons (2D systems) can have intermediate statistics ($e^{i\delta}$ for $0 < \delta < \pi$); this is realized in the fractional quantum Hall effect. Not covered here but worth flagging as the 3D result being special.

---

## E. Teaching considerations

### Sequencing

1. Classical distinguishability → QM indistinguishability (emphasize: no continuous worldlines).
2. Exchange operator → eigenvalue argument ($\lambda^2=1$) → only $\pm 1$ allowed.
3. Symmetrization postulate (bosons/fermions) stated as empirical fact; spin-statistics theorem flagged as needing relativistic QFT.
4. Two-particle Slater determinant derived → extended to $N$ particles.
5. Pauli exclusion derived as a property of determinants (two identical columns → zero).
6. Helium: para/orthohelium symmetry sectors → direct + exchange integrals → Hund's first rule.
7. Bosons briefly (BEC, degeneracy pressure).

### Common misconceptions to address

1. "Exchange statistics implies a force." No. The Hamiltonian has no term depending on statistics. The effect is a correlation in the joint probability density, invisible in the marginal.
2. "Pauli exclusion is a postulate." No — it is a theorem about determinants. This distinction matters for transferring the concept to solid-state systems.
3. "Orthohelium has a spin-dependent force lowering its energy." No — the mechanism runs through the spatial wave function and the Coulomb integral, with spin setting the symmetry sector.
4. "Bosons attract each other; fermions repel." No. See above.

### Difficulty gradient

- Warm-up: exchange operator eigenvalues, Slater determinant normalization check, composite-particle statistics (straightforward algebraic exercises).
- Application: $N=3$ Slater determinant expansion; helium symmetry sectors; direct and exchange integral setup.
- Synthesis: Hund's rule from exchange mechanism; exchange correlation in joint density vs marginal.
- Challenge: degeneracy pressure and Chandrasekhar mass (order-of-magnitude derivation).

### Simulation entry point

The two-particle symmetry explorer (D3 v7, single HTML file) is described in detail in the lib file. It is the right simulation for this chapter. Key pedagogical tasks: (1) show Pauli node forming/vanishing; (2) demonstrate that the marginal density is exchange-statistics-blind; (3) spin extension to model singlet/triplet helium-like behavior.

---

## F. Library files relevant to this chapter

- `/pantry/_lib_qmsri-08-identical-particles.md` — primary source. Complete narrative treatment of indistinguishability, exchange operator, Slater determinant, Pauli exclusion, helium para/orthohelium, direct and exchange integrals, bosons, degeneracy pressure. Full simulation specification. Exercises from warm-up through challenge.
- `/pantry/_lib_qmsri-07-the-hydrogen-atom.md` — provides hydrogenic orbital forms $\psi_{n\ell m}$, radial wave functions $R_{n\ell}(r)$, and the Bohr radius $a_0$ needed for the direct/exchange integral expressions in helium.
- `/pantry/_lib_qmsri-qm-townsend-notes.md` — §5 (Identical Particles): parallel algebraic treatment, Slater determinant with explicit spin indices (§5.5), Hund's rule example (§5.6 end), and the full helium atom calculation including variational helium (§5.7). Provides cross-check derivations and extends the two-particle case to $N$ particles with permanents (bosons) side-by-side.
- `/books/physics-quantum-mechanics-sri/pantry/1022201323-...Cohen-Tannoudji-...Fermions-Bosons...txt` — Cohen-Tannoudji Vol. III Chapter XIV (Systems of Identical Particles); Complement $A_{XIV}$ (many-electron atoms, electronic configurations); Complement $B_{XIV}$ (energy levels of helium, configurations, terms, multiplets). The file is partially garbled OCR but the table of contents and key structural terms are recoverable. Cross-check for the helium para/orthohelium treatment and energy level nomenclature.

---

## G. Gaps and flags

- **Spin-statistics theorem depth:** both lib sources acknowledge they cannot make the spin-statistics connection feel inevitable from non-relativistic principles. The chapter should name this gap explicitly (as the lib file does in "Still puzzling") rather than pretending the connection is derived.
- **N=3 Slater determinant expansion:** the lib file provides an exercise (Exercise 4) but no worked example. Worth including a half-worked expansion in the chapter body or a margin note.
- **Exchange integral computation for helium:** $J$ and $K$ require hydrogenic radial integrals that are technically involved. The chapter should cite the numerical results ($K \approx 1.2$ eV for 1s2s, $2K \approx 0.80$ eV total splitting) without necessarily reproducing the full evaluation. The integral setup should be shown; the evaluation can be left to exercises or referenced.
- **Anyons flag:** worth one sentence noting that in 2D, intermediate statistics are possible (fractional quantum Hall effect), to prevent students from over-generalizing the $\pm 1$ result.
- **Cohen-Tannoudji OCR quality:** the source file is partially garbled; only table of contents and a few clean passages are usable. Do not cite specific page numbers from it without verifying against a clean copy.
