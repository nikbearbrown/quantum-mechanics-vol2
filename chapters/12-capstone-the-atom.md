# Chapter 11 — Capstone — The Atom, Built from Simulations

## TL;DR

- Hydrogenic orbitals are building blocks; screening breaks their energy degeneracy; Pauli exclusion and Hund's rules fill them in order.
- The period structure 2, 8, 8, 18, 18, 32 follows from $2(2\ell+1)$ counting — not numerology, but angular momentum algebra.
- The Madelung (n+ℓ) rule correctly orders orbital filling for most elements, but has no first-principles derivation; roughly 20 exceptions exist, driven by exchange-energy stabilization of half- or fully-filled subshells.
- Hund's third rule is a preview: it needs spin-orbit coupling, which belongs to Volume 3.
- The capstone deliverable is a D3 simulation that fills any atom from Z = 1 to 36, displays Slater $Z_\text{eff}$, outputs the ground-state term symbol, and validates against NIST.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Remember** the Madelung filling sequence and the shielding constants in Slater's rules. *(Bloom: Remember)*
2. **Explain** why the $\ell$-degeneracy of hydrogen breaks in multi-electron atoms, connecting orbital penetration to the breakdown of the $1/r$ Coulomb potential. *(Bloom: Understand)*
3. **Apply** Slater's rules to calculate $Z_\text{eff}$ for any specified orbital of any element through the first transition series. *(Bloom: Apply)*
4. **Analyze** a given electron configuration using all three Hund's rules to derive a ground-state term symbol, and identify where the rules fail (heavy elements, exceptions in the d block). *(Bloom: Analyze)*
5. **Create** a multi-electron atom model by building and validating an orbital-filling D3 simulation against NIST ground-state configurations. *(Bloom: Create)*

---

## Scene Opening

The spectroscopist's notebook for iron, 1927.

The page in front of you lists hundreds of spectral lines for neutral iron — Fe I — measured to four decimal places in angstroms. You are trying to assign each line to a transition between specific energy levels, which means you need the energy levels. You know the ground state must have six electrons in 3d and two in 4s. You know the term symbol is $^5D_4$. You know this because Hund told you: maximize total spin, then orbital angular momentum, then determine total angular momentum from the filling fraction. But where these rules come from — why the atoms follow them, why the ground state is not some other configuration — you cannot fully explain. Not yet.

What you have in front of you is quantum mechanics at the edge of its reach. Hydrogen is solved. Helium is partially solved, variationally, with a screened nuclear charge. Iron has 26 electrons, each repelling every other, moving in the field of a nucleus with 26 protons, and the Schrödinger equation for the full system is a partial differential equation in $26 \times 3 = 78$ spatial dimensions. Nobody is solving that. What you do instead — what every atomist does — is build a model. You pretend each electron moves independently in the average field of the nucleus and the other 25 electrons. You use hydrogenic wave functions, shifted by an effective nuclear charge. You fill orbitals in the order that minimizes energy, constrained by Pauli. You apply three empirical rules attributed to Hund. And it works, astonishingly well, for almost every element in the periodic table.

This chapter is about that model — its physical content, its approximations, where it breaks, and what it predicts. The synthesis is not just knowing the rules; it is building a simulation that applies them, validating the output against real data, and being able to say precisely what approximations you made and why they hold.

You now have every tool this series has given you. Let's use them.

---

## Core Development

### The Central-Field Approximation: Why Hydrogen Is Not Enough

Hydrogen has one electron. The Hamiltonian is

$$\hat{H}_\text{H} = \frac{\hat{p}^2}{2m_e} - \frac{e^2}{4\pi\epsilon_0 r},$$

which has an exact solution: wave functions $\psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$ and energies $E_n = -13.6\,\text{eV}/n^2$. Notice what is missing from $E_n$: the quantum number $\ell$. All $n^2$ states at a given $n$ are degenerate. A $3s$, a $3p$, and a $3d$ orbital all have the same energy in hydrogen. This is the *accidental degeneracy* of the Coulomb potential, arising from the hidden $\mathfrak{so}(4)$ symmetry of the $1/r$ potential that was introduced in Chapter 10.

Add a second electron. The Hamiltonian for helium (Z = 2) is

$$\hat{H}_\text{He} = \frac{\hat{p}_1^2}{2m_e} + \frac{\hat{p}_2^2}{2m_e} - \frac{Ze^2}{4\pi\epsilon_0 r_1} - \frac{Ze^2}{4\pi\epsilon_0 r_2} + \frac{e^2}{4\pi\epsilon_0 |\vec{r}_1 - \vec{r}_2|}.$$

The last term — the electron-electron Coulomb repulsion — destroys the exact solution and, crucially, it destroys the $\ell$-degeneracy. The potential is no longer a pure $1/r$ Coulomb interaction; the $\mathfrak{so}(4)$ symmetry is broken. States with the same $n$ but different $\ell$ are no longer degenerate.

The physical mechanism is **orbital penetration and screening**. A 3s orbital has its radial probability density peaked closer to the nucleus than a 3d orbital with the same $n$ (the centrifugal barrier $\ell(\ell+1)\hbar^2/2m_e r^2$ pushes high-$\ell$ orbitals outward). The inner electrons between the 3s electron and the nucleus are fewer — the 3s penetrates to the core and "sees" more of the bare nuclear charge $Ze$. The 3d electron stays far out and is more heavily screened. More screening means a weaker effective nuclear attraction means higher energy. The result:

$$E(ns) < E(np) < E(nd) < E(nf) \qquad \text{(multi-electron atoms, any } n\text{).}$$

The degeneracy that made hydrogen's levels so tidy is gone. In its place is an energy ordering among subshells within a given $n$, and this ordering is what drives the structure of the periodic table.

The **central-field approximation** — also called the independent-electron model — replaces the full, intractable Hamiltonian with a sum of effective single-electron problems:

$$\hat{H}_\text{eff} = \sum_{i=1}^N \left[\frac{\hat{p}_i^2}{2m_e} + V_\text{eff}(r_i)\right],$$

where $V_\text{eff}(r_i)$ is a spherically symmetric average potential that includes the nuclear attraction and the average Coulomb repulsion from all other electrons. The wave functions remain products of hydrogenic-type orbitals (one per electron), and the $N$-electron state is a Slater determinant of those orbitals. The energies are no longer $-13.6\,\text{eV}/n^2$ but depend on both $n$ and $\ell$.

This approximation ignores **electron-electron correlation** — the fact that the motion of each electron depends on the instantaneous positions of all the others, not just their average density. It also ignores relativistic corrections (spin-orbit coupling, mass-velocity, Darwin term). These corrections are addressed by perturbation theory in Volume 3. For the first 36 elements, the central-field approximation gives configurations that are correct to better than one part in 10 in all cases where the energy ordering is unambiguous.

### Screening and Effective Nuclear Charge

The effective nuclear charge $Z_\text{eff}$ is the net nuclear charge felt by an electron after accounting for the shielding of all other electrons:

$$Z_\text{eff} = Z - \sigma,$$

where $\sigma$ is the **shielding constant**. The variational calculation for helium from Chapter 9 found the prototype: for each 1s electron in helium, the other 1s electron screens the nucleus by $5/16$ of a proton charge, giving $Z_\text{eff} = 2 - 5/16 = 27/16 \approx 1.69$ and a ground-state energy of $-77.4$ eV (experiment: $-79.0$ eV). Slater's rules are a systematic generalization of this idea to all electrons in any atom.

**Slater's rules (1930)** provide a semi-empirical recipe for $\sigma$. [verify: original source is Slater, J.C. (1930). Atomic shielding constants. Phys. Rev. 36, 57–64.]

*Step 1.* Group the orbitals in the order:
$$[1s]\;\; [2s,2p]\;\; [3s,3p]\;\; [3d]\;\; [4s,4p]\;\; [4d]\;\; [4f]\;\; [5s,5p]\;\; \ldots$$

Note that $s$ and $p$ orbitals within the same principal quantum number are grouped together, but $d$ and $f$ are separated.

*Step 2.* Electrons in groups to the right of (higher $n+\ell$ than) the electron of interest contribute **0** to $\sigma$.

*Step 3.* Each other electron in the **same group** contributes **0.35** (except in the [1s] group, where the single companion contributes **0.30**).

*Step 4.* For an **s or p electron**: each electron in the next inner shell ($n-1$) contributes **0.85**; each electron in shells further in ($n-2$ and below) contributes **1.00**.

*Step 5.* For a **d or f electron**: every electron in all inner groups contributes **1.00**.

The physics behind the distinction between s/p and d/f: s and p orbitals penetrate to near the nucleus and see partial nuclear charge through the inner shells (hence 0.85, not 1.00), while d and f orbitals are effectively excluded from the core by the centrifugal barrier and are nearly completely screened by every inner electron (hence 1.00).

#### Worked Slater calculations

**Fluorine (Z = 9), config 1s² 2s² 2p⁵: find $Z_\text{eff}$ for a 2p electron.**

Groups: [1s²] [2s²2p⁵]. The electron of interest is in the [2s,2p] group.
- Same group: 6 other electrons (2s² + 2p⁴ neighbors) × 0.35 = 2.10
- Inner shell [1s]: 2 electrons × 0.85 = 1.70
- $\sigma = 2.10 + 1.70 = 3.80$
- $Z_\text{eff} = 9 - 3.80 = \mathbf{5.20}$

Compare to experiment: the first ionization energy of fluorine is 17.4 eV. From a hydrogen-like atom with $Z_\text{eff} = 5.20$ and $n = 2$: $E = -13.6 \times (5.20)^2 / 4 = -92$ eV. This is the orbital energy, not the ionization energy (which involves relaxation). Slater's rules reproduce experimental ionization energies to within 10–20% — good enough to predict periodic trends correctly.

**Sodium (Z = 11), config 1s² 2s² 2p⁶ 3s¹: find $Z_\text{eff}$ for the 3s electron.**

Groups: [1s²] [2s²2p⁶] [3s¹]. The electron of interest is the single 3s.
- Same [3s,3p] group: 0 other electrons (it's alone) × 0.35 = 0
- $n-1$ shell [2s,2p]: 8 electrons × 0.85 = 6.80
- $n-2$ shell [1s]: 2 electrons × 1.00 = 2.00
- $\sigma = 0 + 6.80 + 2.00 = 8.80$
- $Z_\text{eff} = 11 - 8.80 = \mathbf{2.20}$

Sodium's first ionization energy is 5.14 eV. From the Slater model: $E = -13.6 \times (2.20)^2/9 = -7.3$ eV. This overestimates, but the agreement is within a factor of 1.5 — not bad for a calculation with a single number.

**Iron (Z = 26), config [Ar] 3d⁶ 4s²: find $Z_\text{eff}$ for a 3d electron.**

Groups: [1s²] [2s²2p⁶] [3s²3p⁶] [3d⁶] [4s²]. For a 3d electron, all inner groups contribute 1.00.
- Same [3d] group: 5 other 3d electrons × 0.35 = 1.75
- All inner groups: [1s²] + [2s²2p⁶] + [3s²3p⁶] = 2 + 8 + 8 = 18 electrons × 1.00 = 18.00
- $\sigma = 1.75 + 18.00 = 19.75$
- $Z_\text{eff} = 26 - 19.75 = \mathbf{6.25}$

The Hartree-Fock value (Clementi & Roetti 1974) [verify: Clementi, E. & Roetti, C. (1974). Atomic Data Nuclear Data Tables 14, 177.] for a 3d orbital in iron is approximately 6.04 — Slater's rule gives a value about 3.5% too high. This is the level of accuracy to expect.

### The Aufbau Principle and the Madelung Rule

The aufbau principle — fill orbitals in order of increasing energy, one electron at a time, subject to Pauli exclusion and Hund's rules — organizes the building-up of atoms from hydrogen to oganesson. The remaining question is the ordering of subshell energies across atoms.

The empirical answer is the **Madelung rule** (also called the Madelung-Janet-Klechkowski rule or the (n+ℓ) rule):

> Fill subshells in order of increasing $n + \ell$. When two subshells have the same $n + \ell$, fill the one with lower $n$ first.

This gives the sequence:

$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\ 7s,\ 5f,\ 6d,\ 7p,\ \ldots$$

The rule must be stated honestly: **no one has derived the Madelung rule from first principles as of 2026.** The rule was identified empirically by Charles Janet (1929) and Erwin Madelung (1936) and is confirmed computationally for most elements, but no analytic proof from the Schrödinger equation exists. John Carlos Baez, reviewing the problem in 2021, listed it as a genuine open question in quantum mechanics. [verify: Baez, J.C. (2021). "The Madelung Rules," Azimuth blog.] Present the Madelung rule as a pattern that works — not as a derived theorem.

#### Period lengths from $2(2\ell+1)$

Each subshell with angular momentum quantum number $\ell$ contains $2\ell+1$ distinct $m_\ell$ values, and each spatial orbital can hold 2 electrons (one $m_s = +1/2$, one $m_s = -1/2$). Total capacity of a subshell: $2(2\ell+1)$.

| Subshell | $\ell$ | $2(2\ell+1)$ |
|----------|--------|--------------|
| s        | 0      | 2            |
| p        | 1      | 6            |
| d        | 2      | 10           |
| f        | 3      | 14           |

Period lengths follow by adding the subshell capacities as the Madelung sequence fills:

| Period | Subshells filling | Capacity |
|--------|-------------------|----------|
| 1      | 1s                | 2        |
| 2      | 2s, 2p            | 2+6 = 8  |
| 3      | 3s, 3p            | 2+6 = 8  |
| 4      | 4s, 3d, 4p        | 2+10+6 = 18 |
| 5      | 5s, 4d, 5p        | 2+10+6 = 18 |
| 6      | 6s, 4f, 5d, 6p    | 2+14+10+6 = 32 |
| 7      | 7s, 5f, 6d, 7p    | 2+14+10+6 = 32 |

The famous sequence 2, 8, 8, 18, 18, 32 is not numerology. It is the quantum number algebra of angular momentum — the $2(2\ell+1)$ counting — combined with the empirical Madelung ordering. The repeating structure of the periodic table is a consequence of the Schrödinger equation's eigenstates together with the antisymmetrization requirement.

#### The Madelung exceptions: Cr, Cu, and their cousins

The Madelung rule fails for approximately 20 elements in the periodic table. The most important in the first transition series are:

**Chromium (Z = 24):** Madelung predicts [Ar] 3d⁴ 4s². The actual ground-state configuration (from spectroscopy; [verify: NIST Atomic Spectra Database]) is **[Ar] 3d⁵ 4s¹**. One 4s electron has moved into the 3d to give a half-filled 3d subshell.

**Copper (Z = 29):** Madelung predicts [Ar] 3d⁹ 4s². Actual: **[Ar] 3d¹⁰ 4s¹**. One 4s electron has moved into the 3d to give a completely filled 3d subshell.

The mechanism is **exchange-energy stabilization**. By Hund's first rule, a half-filled subshell (all electrons in distinct orbitals with parallel spins) gains extra exchange energy compared to a nearly-half-filled one with a paired electron. The exchange integral $K > 0$; each pair of electrons with parallel spins lowers the energy by $K$. A half-filled 3d (5 electrons, 10 parallel pairs) or fully filled 3d (10 electrons, no unpaired) is disproportionately stabilized. When the 3d–4s gap is small enough, the exchange-energy gain from filling the 3d to half or full exceeds the orbital energy cost of promoting the 4s electron. The Madelung mnemonic does not capture this — it treats orbital energies as fixed, whereas the exchange energy depends on the actual occupation pattern.

Similar exceptions occur in the 4d block: Mo (half-filled 4d⁵), Ru, Rh, Pd, Ag. [verify: Wikipedia, "Aufbau principle," §Exceptions.]

The lesson: use the Madelung rule as a first prediction, then check against NIST for the d-block elements. When you find a discrepancy, the question to answer is: does a half-filled or fully-filled subshell give enough exchange-energy stabilization to overcome the level gap?

### Hund's Three Rules

Once the configuration is established — the list of occupied orbitals and their electron counts — you need to determine which quantum state the atom actually inhabits. Within a given configuration, multiple **terms** (combinations of total $L$, total $S$, total $J$) are possible. Hund's rules select the ground-state term.

**Rule 1 (maximize $S$):** The term with the highest total spin $S$ has the lowest energy.

Mechanism (from Chapter 11): highest $S$ means the most symmetric spin state, which forces the most antisymmetric spatial wave function (to keep the total antisymmetric). The antisymmetric spatial wave function has lower amplitude when two electrons coincide ($\psi \to 0$ as $\vec{r}_1 \to \vec{r}_2$). Electrons that avoid each other see less Coulomb repulsion. Lower Coulomb repulsion means lower total energy. This is the exchange integral mechanism derived in Chapter 11 from the Heisenberg helium analysis.

**Rule 2 (maximize $L$ given $S$):** Among all terms with the same $S$, the one with highest total orbital angular momentum $L$ has the lowest energy.

Mechanism: electrons orbiting in the same sense (high $L$) tend to stay on opposite sides of the atom, again reducing Coulomb repulsion. The argument is of the same type as Rule 1 but less crisp — the spatial correlation is angular rather than radial.

**Rule 3 (determine $J$ from filling fraction):**

- Less-than-half-filled subshell: $J = |L - S|$.
- More-than-half-filled subshell: $J = L + S$.
- Exactly half-filled: $L = 0$ necessarily, so $J = S$.

**Honesty flag for Rule 3:** The mechanism for Rule 3 is spin-orbit coupling — the interaction $\hat{H}_{SO} \sim \lambda \vec{L} \cdot \vec{S}$ between the electron's orbital motion and its spin magnetic moment. For lighter atoms ($Z \lesssim 50$), the coupling constant $\lambda > 0$ when the subshell is less than half-filled and $\lambda < 0$ when more than half-filled; the sign determines which $J$ is lowest. This requires perturbation theory and a careful treatment of the fine structure, which belongs to Volume 3. In this chapter, apply Rule 3 mechanically: the rule works correctly for all elements through the first transition series. The derivation is deferred.

**When Hund's rules fail:** Hund's rules assume the atom is in the *LS coupling* (Russell-Saunders) regime, where electron-electron repulsion $\gg$ spin-orbit coupling. For heavy elements (roughly $Z > 50$), spin-orbit coupling becomes comparable to or larger than the Coulomb term, and the *jj coupling* scheme (individual $j_i = \ell_i + s_i$ combine to give total $J$) is more appropriate. In the jj limit, $L$ and $S$ are not good quantum numbers, and Hund's rules cannot be applied. Even in lighter atoms, Rule 2 is less reliable than Rule 1, and Rule 3 is even less reliable than Rule 2.

---

## Worked Example: Carbon (³P₀) and Iron (⁵D₄)

### Carbon (Z = 6)

**The lesson:** Applying all three Hund's rules to a partially filled 2p subshell.

**Step 1 — Configuration.** Write the ground-state configuration using the Madelung sequence: $1s^2\, 2s^2\, 2p^2$. The 1s and 2s subshells are completely filled (they contribute $L=0$, $S=0$ to the total — filled subshells are spectroscopically inert). The two 2p electrons determine the term symbol.

**Step 2 — Available orbitals.** The 2p subshell has three spatial orbitals: $m_\ell = +1, 0, -1$. Two electrons, each with $m_s = \pm 1/2$.

**Step 3 — Rule 1: Maximize S.** Place the two 2p electrons in different orbitals with parallel spins. We get $m_s = +1/2$ for both. Total spin $S = 1/2 + 1/2 = 1$. Term multiplicity $2S+1 = 3$ (triplet). Pairing them in the same orbital would give $S = 0$ (singlet) — that term is higher in energy by the exchange integral $2K_{2p} \approx 1$ eV.

**Step 4 — Rule 2: Maximize L.** We have electrons in two distinct 2p orbitals with parallel spins. To maximize $M_L = m_{\ell,1} + m_{\ell,2}$, choose $m_\ell = +1$ and $m_\ell = 0$: total $M_L = 1$. This means $L = 1$ (P term). [The full term enumeration confirms that the highest-spin ($S=1$) terms are $^3P$, and among those, $L=1$ is the maximum.]

**Step 5 — Rule 3: Determine J.** Less-than-half-filled (2 electrons in a 6-electron subshell): $J = |L - S| = |1 - 1| = 0$.

**Ground-state term symbol: $^3P_0$.**

**Check against NIST:** The NIST Atomic Spectra Database lists the ground level of carbon as $2s^2 2p^2\,^3P_0$. ✓ [verify: NIST ASD, https://physics.nist.gov/asd]

**The limit — why Rule 3 needs spin-orbit coupling:** The $J = 0$ result comes from Rule 3, which requires the spin-orbit interaction to determine which $J$ sits lowest within the $^3P$ multiplet. The $^3P$ term has $J = 0, 1, 2$; experimentally these are at 0, 16.4, and 43.4 cm⁻¹ above the ground state. Without spin-orbit coupling, all three $J$ levels would be degenerate. The splitting is real and measurable — it is just outside the scope of this volume.

### Iron (Z = 26)

**The lesson:** The same procedure for a more-than-half-filled 3d subshell with a larger-$S$ term.

**Step 1 — Configuration.** Madelung: $[\text{Ar}]\, 3d^6\, 4s^2$. The Ar core and the filled $4s^2$ are spectroscopically inert. The six 3d electrons determine the term.

**Step 2 — Available orbitals.** Five 3d orbitals: $m_\ell = +2, +1, 0, -1, -2$. Six electrons.

**Step 3 — Rule 1: Maximize S.** Fill each of the five 3d orbitals with one spin-up electron (5 electrons, $S = 5/2$). The sixth electron must pair into one of the occupied orbitals (antiparallel). Net $m_s$ sum: $(+1/2) \times 5 + (-1/2) \times 1 = 2$. Total $S = 2$. Multiplicity $2S+1 = 5$ (quintet).

**Step 4 — Rule 2: Maximize L.** Five spin-up electrons contribute $M_L = +2 + 1 + 0 - 1 - 2 = 0$ (a closed half-shell). To maximize $M_L$, place the sixth (spin-down) electron in the $m_\ell = +2$ orbital. Total $M_L = 0 + 2 = 2$. So $L = 2$ (D term).

**Step 5 — Rule 3: Determine J.** More-than-half-filled (6 of 10 3d electrons): $J = L + S = 2 + 2 = 4$.

**Ground-state term symbol: $^5D_4$.**

**Check against NIST:** The NIST Atomic Spectra Database lists the ground level of neutral iron as $3d^6 4s^2\,^5D_4$. ✓ [verify: NIST ASD]

**The 3d/4s subtlety.** Iron's 4s² is correctly listed as filling before 3d by Madelung, and the ground state configuration [Ar]3d⁶4s² holds for neutral iron. But Fe²⁺ is [Ar]3d⁶ — not [Ar]3d⁴4s². When iron is doubly ionized, both 4s electrons are lost before any 3d electrons. This seems paradoxical: if Madelung says 4s fills before 3d, shouldn't 3d be removed first? The resolution: orbital energies depend on the number of electrons. In the neutral atom with 4s² and 3d⁶, the self-consistent 3d and 4s orbital energies are ordered one way. Remove two electrons, and the 3d orbital energy drops relative to 4s. The effective potential changes when the occupation changes. The independent-electron model with fixed Slater $Z_\text{eff}$ does not capture this; the ordering of orbital energies in multi-electron atoms is not a fixed property of the orbital label. [contested: the 3d/4s ordering in transition metal atoms is a recurring source of pedagogical confusion; see e.g. Tsutomu Ogata, J. Chem. Educ. 1986, or more recent discussions in J. Chem. Educ. 88 (2011) 110.]

---

## Common Misconceptions

**1. "The aufbau principle is a law of nature."**
It is an approximate rule derived from the independent-electron model plus the empirical Madelung ordering. The Madelung rule has no first-principles derivation, and it has approximately 20 known exceptions. "Aufbau" is a good first guess; always check against NIST for d-block elements.

**2. "3d always fills after 4s because 3d always has higher energy."**
The relative energy of 3d and 4s orbitals depends on how many electrons are in each. In neutral potassium and calcium, 4s is lower. In neutral iron with a partially filled 3d, they are close. In transition metal cations, 3d is lower. There is no single universal ordering that holds across all occupancies and nuclear charges.

**3. "Hund's rules always give the ground state."**
Hund's rules apply within a single electron configuration, in the LS coupling regime, for ground states. They do not apply to excited states (where intersystem crossings mix configurations), to heavy elements where jj coupling dominates, or to cases where the assumption of a single dominant configuration breaks down. Rule 1 is the most reliable; Rule 2 is good for the first transition series; Rule 3 should be applied with awareness that its derivation (spin-orbit coupling, Volume 3) is deferred.

**4. "The period structure comes from some mysterious pattern."**
No mystery: it is $2(2\ell+1)$, summed over the subshells that fill in each period according to the Madelung sequence. The 2 is from spin (two spin states per spatial orbital), the $(2\ell+1)$ is the number of $m_\ell$ values for angular momentum $\ell$. Both follow from the algebra of angular momentum operators derived in Chapter 7.

**5. "Hund's rule is about a spin-dependent force."**
There is no spin-dependent force at this level of approximation. The mechanism is purely geometric: antisymmetry of the spatial wave function forces electrons with parallel spins to avoid coinciding in space, which reduces Coulomb repulsion. The chain is: spin symmetry → spatial symmetry → electron correlation → Coulomb energy. The word "exchange force" should be avoided; what we have is an exchange-correlation effect in the electrostatic energy. (See Chapter 11 on identical particles.)

---

## Exercises

### Warm-Up

**11.1** Write the ground-state electron configuration of (a) nitrogen (Z = 7), (b) chlorine (Z = 17), (c) manganese (Z = 25) using the Madelung sequence. For each, state the number of unpaired electrons. *(Tests: can apply the Madelung rule for main-group and transition elements)*

**11.2** Compute $Z_\text{eff}$ using Slater's rules for (a) the 2p electron of oxygen (Z = 8), (b) the 4s electron of potassium (Z = 19). Show each step of the grouping and shielding sum. *(Tests: can execute Slater's rules for s, p electrons)*

**11.3** The period structure of the periodic table has lengths 2, 8, 8, 18, 18, 32. Derive each of these numbers from the Madelung filling sequence and the formula $2(2\ell+1)$. State which subshells fill in periods 4 and 6. *(Tests: can connect the period structure to angular momentum counting)*

### Application

**11.4** Apply Hund's rules to oxygen (Z = 8, config 1s² 2s² 2p⁴) to find the ground-state term symbol. Show: (a) which Rule determines $S$ and its value; (b) which Rule determines $L$ and its value; (c) why Rule 3 gives $J = 2$ for a more-than-half-filled subshell; (d) the full term symbol $^{2S+1}L_J$. *(Tests: can apply all three Hund's rules to a more-than-half-filled subshell)*

**11.5** Chromium (Z = 24) is a Madelung exception. (a) State what the Madelung rule predicts and what the actual ground-state configuration is. (b) Explain in one paragraph, using the exchange integral, why the actual configuration has lower energy. (c) Compute $Z_\text{eff}$ for a 3d electron in the actual configuration [Ar]3d⁵4s¹ using Slater's rules. *(Bloom: Apply+Analyze)*

**11.6** Neutral manganese (Z = 25) has configuration [Ar]3d⁵4s². The ion Mn²⁺ loses two electrons. (a) Identify which electrons are removed and write the configuration of Mn²⁺. (b) Find the ground-state term symbol of Mn²⁺ using Hund's rules. (c) Explain why the order of electron removal (4s before 3d) may seem to contradict the Madelung filling order. *(Bloom: Analyze — the 3d/4s subtlety)*

### Synthesis / Produce

**11.7** **(Produce)** Construct the full term-symbol analysis for vanadium (Z = 23, config [Ar]3d³4s²). List all microstates for the 3d³ configuration (you may use a table with columns $m_\ell$ for each of the three 3d electrons and $m_s$), identify the term with highest $S$, then highest $L$, then determine $J$. Write the ground-state term symbol and verify against NIST. This exercise requires building the full microstate table — it is the procedure, not just the answer. *(Bloom: Create)*

**11.8** **(Apply+)** For the first row transition metals (Z = 21 through Z = 30), make a table of: (a) Madelung-predicted configuration; (b) actual ground-state configuration (from NIST); (c) whether they agree; (d) for disagreements, identify the mechanism (half-filled or fully-filled stabilization). Identify every exception and briefly explain each. *(Bloom: Analyze)*

---

## Still Puzzling

### The Madelung Rule Has No Proof

This bears repeating because it is routinely glossed over in textbooks: the (n+ℓ) rule for the ordering of orbital energies across the periodic table has no analytic derivation from the Schrödinger equation as of 2026. It is a semi-empirical pattern — observed first by Charles Janet in 1929 and formalized by Madelung — that is confirmed by numerical Hartree-Fock calculations across the periodic table but cannot be proved from first principles. John Carlos Baez called this a genuine open problem in a widely-read 2021 survey. [verify: Baez blog]

Why has it resisted proof? The orbital energies are not eigenvalues of a simple 1D potential; they emerge from the self-consistent field of a non-separable $N$-body problem. The (n+ℓ) ordering holds for neutral atoms in their ground states, but it does not hold for ions, and it does not hold for all neutral atoms (the ~20 exceptions). Any proof would need to explain both when it holds and when it fails. Nobody has found a clean argument that does both.

Students encountering this for the first time often assume the rule must be derivable — textbooks present it so confidently. It isn't. Noticing that something is empirical when a textbook implies it is fundamental is a scientific skill worth developing.

### The 3d/4s Crossing Problem

The Madelung rule tells you 4s fills before 3d. But orbital energies in multi-electron atoms are not static: they depend on the occupation of every other orbital, because each electron contributes to the effective potential that the others feel. As Z increases across the first transition series, the 3d orbital drops in energy faster than the 4s orbital. Near Z = 20–21, the two are nearly degenerate; by Z = 30, the 3d sits well below 4s in energy for the positive ion.

This means the statement "4s has lower energy than 3d" is correct for neutral K and Ca but incorrect for neutral Cu²⁺ and Fe²⁺. The independent-electron model with fixed Slater $Z_\text{eff}$ does not fully capture this crossing because the $Z_\text{eff}$ itself changes with occupation. This is one of the cleaner examples of where the approximation visibly fails. The quantitative treatment requires self-consistent Hartree-Fock, where the orbital energies are updated at each iteration until the effective potential and the orbitals are mutually consistent.

### Why Do Atoms Have the Electron Configurations They Have, Really?

The full answer is Hartree-Fock theory, or better, post-HF methods (configuration interaction, coupled-cluster). In HF, you minimize $\langle\Psi|\hat{H}|\Psi\rangle$ over all choices of single-particle orbitals $\phi_i$, with the $N$-electron wave function constrained to be a single Slater determinant. The result is a set of coupled one-electron equations (the Fock equations) that are solved iteratively until the orbitals are self-consistent with the effective potential they generate. The orbital energies that emerge from this procedure satisfy Koopmans' theorem: the orbital energy is approximately the ionization energy of that orbital (with a sign flip). Experimental ionization energies validate this at the few-percent level.

Beyond HF: the true ground state is not a single Slater determinant. It has contributions from many configurations — the determinants mix. Configuration interaction (CI) and coupled-cluster (CCSD(T)) methods capture this. Modern DFT (density functional theory) approaches the same ground state by working with the electron density $\rho(\vec r)$ rather than the wave function directly. All of these are beyond this volume but rest on the same foundation: antisymmetric $N$-electron states, built from the single-particle orbital framework introduced here.

---

## The +1 — Simulation Exercise: Build the Periodic Table

This is the capstone +1. The deliverable is `11-atom-builder.html`: a D3 v7 simulation that accepts an atomic number $Z$ (1–36), fills the orbitals according to the Madelung rule with Hund's-rule enforcement within each subshell, displays the Slater $Z_\text{eff}$ for the outermost electron, shows the ground-state term symbol ($S$ and $L$ from Hund's rules 1 and 2; $J$ from rule 3 with a flag that rule 3 requires spin-orbit coupling), and validates against the known NIST configurations. This is a synthesis project — it requires applying every concept from this chapter in a working codebase.

### Part 1 — CLAUDE.md extension

Open your project's CLAUDE.md and append:

```
## Chapter 11 — Atom Builder Rules

- Single HTML file. D3 v7 from CDN. No external assets.
- Input: integer Z from 1 to 36 (slider + text field).
- Panel 1 — Energy level diagram: display all subshells up to the highest
  filled one, arranged vertically by Madelung n+ℓ order. Each subshell is
  a horizontal row of orbital boxes (one box per m_ℓ value). Electrons
  are shown as arrows (↑ or ↓) inside the boxes. The diagram updates as Z
  changes, animating the addition of each electron.
- Panel 2 — Configuration readout: full configuration string (e.g.,
  "1s² 2s² 2p³") and noble-gas shorthand (e.g., "[Ne] 3s² 3p³"). Flag any
  deviation from Madelung prediction by coloring the discrepant subshell red.
- Panel 3 — Term symbol output: show 2S+1, L (as letter), and J. For L,
  display the standard spectroscopic letter (S=0, P=1, D=2, F=3). Flag J
  with "(spin-orbit coupling; see Vol. 3)".
- Panel 4 — Slater Z_eff: show the computed Z_eff for the outermost electron,
  with the step-by-step breakdown (same-group count, n-1 count, n-2 count,
  shielding sum, Z_eff result).
- Validation table: for Z=1–36, show a comparison of predicted configuration
  vs. hard-coded NIST values. Highlight mismatches in red. The mismatches
  for Z=24 (Cr) and Z=29 (Cu) must be flagged and annotated.
- Hund's-rule filling: within each subshell, fill orbitals spin-up first
  (↑↑↑...) until all are singly occupied, then pair (↑↓ in each).
- All redraws through a single redraw(Z) function. No DOM mutation outside.
```

### Part 2 — The build prompt

```
Build me a D3 v7 atom builder simulation following CLAUDE.md.

DATA.
The hard-coded NIST ground-state configurations for Z=1–36 are the reference.
Madelung filling order (hardcode this array):
  [1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p]
Capacity array: [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6]
Hund's rule: within each subshell, assign m_s=+1/2 to each electron until
all m_ℓ values are singly occupied, then assign m_s=-1/2.

SHOW — Panel 1 (energy diagram).
For the current Z, display subshells as horizontal rows of orbital boxes.
Each box holds one up-arrow (↑) or up+down-arrow (↑↓). Rows are labeled
with the subshell name (1s, 2s, ...) at left and n+ℓ value at right.
Electrons are placed one by one as Z increases (animate the last-added
electron dropping into its box).

SHOW — Panel 2 (configuration string).
Full configuration string and noble-gas shorthand. For Z=24 and Z=29,
show the NIST actual configuration in green and the Madelung prediction
in grey, annotated "exchange stabilization."

SHOW — Panel 3 (term symbol).
Compute S as (sum of m_s values in open subshell). Compute L from the
m_ℓ values of the open-subshell electrons using the maximum M_L heuristic.
Determine J by Hund's Rule 3 (filling fraction). Display "^{2S+1}L_J".

SHOW — Panel 4 (Slater Z_eff).
Implement Slater's grouping: [1s][2s,2p][3s,3p][3d][4s,4p]...
Apply shielding constants for s/p electron (0.35 same, 0.85 n-1, 1.00 n-2+)
and d/f electron (0.35 same, 1.00 all inner).
Display result to two decimal places.

CONSTRAIN.
- D3 v7 from CDN. Vanilla JS. SVG only for diagrams, HTML for inputs.
- Hard-code NIST configurations for Z=1–36 and show mismatch flags.
- Animation: each new electron enters from the right edge of its box and
  slides to rest. Speed: 200ms per electron.
- The term symbol computation must correctly handle filled subshells
  (S=0, L=0), half-filled subshells (L=0, J=S), and more-than-half-filled
  subshells (J=L+S). Test explicitly at Z=6 (C: ³P₀), Z=8 (O: ³P₂),
  Z=25 (Mn: ⁶S₅/₂), Z=26 (Fe: ⁵D₄).

VERIFY.
Give me these eight checks:
(a) Z=1 (H): config 1s¹, term ²S_{1/2}.
(b) Z=6 (C): config 1s²2s²2p², term ³P₀.
(c) Z=8 (O): config 1s²2s²2p⁴, term ³P₂.
(d) Z=11 (Na): config [Ne]3s¹, Z_eff(3s)=2.20.
(e) Z=24 (Cr): Madelung predicts 3d⁴4s², NIST = 3d⁵4s¹; simulation flags mismatch.
(f) Z=25 (Mn): term ⁶S_{5/2} (half-filled 3d: L=0, S=5/2, J=5/2).
(g) Z=26 (Fe): term ⁵D₄.
(h) Z=29 (Cu): simulation flags mismatch, actual = 3d¹⁰4s¹.

List known failure modes: wrong Hund ordering (spin-down before up),
forgetting that filled subshells contribute L=0, S=0, using Madelung order
for exceptions (Cr, Cu), wrong Slater group for d electrons (not grouped
with s/p of same n), forgetting that Rule 3 is filling-fraction-dependent.
```

### Part 3 — Exploration and validation tasks

**Task 1 — Verify carbon.** Set Z = 6. Read the term symbol. Confirm ³P₀. Change to Z = 7 (nitrogen): confirm ⁴S_{3/2} (half-filled 2p, L=0, J=S=3/2). Change to Z = 8 (oxygen): confirm ³P₂ (more-than-half-filled, J = L+S = 1+1 = 2). This sequence tests Rules 1, 2, and 3 in order.

**Task 2 — The Slater tour.** For Z = 9 (F), Z = 11 (Na), Z = 26 (Fe), read the Slater $Z_\text{eff}$ from the simulation and compare to the values derived in this chapter (5.20, 2.20, 6.25). Any discrepancy larger than 0.01 indicates a bug in the grouping logic.

**Task 3 — The exception check.** Set Z = 24 (Cr). The simulation should flag the mismatch between Madelung prediction and NIST, display the annotation "exchange stabilization," and show the correct [Ar]3d⁵4s¹. Set Z = 29 (Cu) and verify the same for the full 3d¹⁰.

**Task 4 — The periodic table read-out.** Run Z from 1 to 36 using the slider. Watch the energy level diagram fill. Identify the four moments when a new type of subshell appears: 2p (Z=5), 3d (Z=21), 4f does not appear in this range. Explain in your lab notebook why 4f does not fill within the first 36 elements.

**Task 5 — Defend the structure (capstone defense).** Write a 300-word defense of your simulation's atom model. Your defense must:
1. Name the four approximations: independent electrons, hydrogenic orbital shapes, central-field potential, Slater screening.
2. State what each ignores: electron-electron correlation, relativistic corrections (fine structure), configuration mixing.
3. Predict the configuration and term symbol for phosphorus (Z = 15) using your simulation, then verify against NIST.
4. Identify one quantitative prediction: the Slater $Z_\text{eff}$ for the 3d electron of iron, and compare to the Hartree-Fock value (≈ 6.04).
5. Explain the Cr exception using the exchange integral.
6. State where Rule 3 comes from and why its derivation is deferred.

### Part 4 — Project rubric: "Defend the structure"

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| **Simulation correctness** | All 8 NIST checks pass; Cr/Cu flagged; animation smooth | 6–7 checks pass; exceptions identified | 4–5 checks pass; some exceptions missed | <4 checks pass |
| **Slater Z_eff** | Correct for F, Na, Fe within 0.05; step-by-step breakdown displayed | Correct values; breakdown incomplete | Correct grouping, arithmetic error | Wrong grouping |
| **Term symbol** | Correct for C, O, Mn, Fe; Rule 3 flagged as preview | Correct for C and Fe; Rule 3 applied | Rules 1–2 correct; Rule 3 wrong sign | S or L wrong |
| **Defense: approximations** | All four named; what each ignores stated specifically | Three of four named | Two named | One or none |
| **Defense: exceptions** | Cr and Cu explained via exchange integral, quantitatively motivated | Cr or Cu explained; mechanism stated | Exceptions identified but mechanism vague | Exceptions not identified |
| **Defense: where rules come from** | Rule 1 traced to exchange integral (Ch. 11); Rule 3 traced to spin-orbit (Vol. 3 preview) | Both traced, less precisely | One traced | Neither traced |

A passing defense is Proficient or above in all six criteria. The capstone defense is not about having the right answers — it is about knowing which approximations produced them and where they will fail.

### Part 5 — Six failure modes to watch for

**Spin-down before spin-up in Hund filling.** The rule is: fill each orbital spin-up first. If your simulation pairs electrons before all orbitals are singly occupied, Hund's Rule 1 is violated. Test at Z = 7 (N): all three 2p should show ↑ before any shows ↑↓.

**Filled subshells contributing to L or S.** A completely filled subshell has $L = 0, S = 0$. If your term-symbol computation sums $m_\ell$ over all electrons including filled 1s, 2s, etc., the $L$ will be wrong. Only electrons in partially filled subshells contribute.

**Madelung order applied to exceptions.** If the simulation just applies Madelung mechanically without the NIST lookup and mismatch flag, the Cr and Cu configurations will be wrong. The simulation must have the hard-coded NIST table.

**Wrong Slater group for d electrons.** The 3d and 3s,3p electrons are in separate groups. A common bug groups them together (like an s electron), giving wrong shielding. For a 3d electron, all [3s,3p] electrons contribute 1.00, not 0.85.

**Rule 3 sign error.** Less-than-half-filled → $J = |L - S|$. More-than-half-filled → $J = L + S$. Getting the condition backwards gives the wrong $J$ for every case in the second half of the transition series.

**Term symbol letter from $M_L$ not $L$.** The heuristic "take the maximum $M_L$ from among the highest-spin microstates" gives the correct $L$ for simple cases. For configurations with multiple electrons and near-degenerate terms (e.g., 3d⁵ where $L = 0$ by half-filling), verify separately that the $M_L$ calculation has not been confused with $L$.

*Bridge to Volume 3: Everything you have built here — hydrogenic orbitals, Slater screening, Hund's rules — is the zeroth order. Volume 3 applies perturbation theory to the same atoms: spin-orbit coupling gives the $J$-level splittings that Rule 3 predicts without explaining, the fine structure of hydrogen and helium becomes the Lamb shift, and the independent-electron model is upgraded to Hartree-Fock and beyond. The periodic table you built in this chapter is the input to all of that — the structure whose corrections perturbation theory will calculate.*

---

## References

All sources are listed as cited in the text. Sources marked [verify] should be confirmed by the author against primary documents before publication. Sources marked [contested] flag areas of active pedagogical debate.

1. Slater, J.C. (1930). Atomic shielding constants. *Physical Review*, 36(1), 57–64. [verify]

2. Madelung, E. (1936). *Mathematische Hilfsmittel des Physikers* (3rd ed.). Springer. [verify — the n+ℓ rule appears here; attribution is complex; Janet (1929) arguably has priority]

3. Clementi, E. & Roetti, C. (1974). Roothaan-Hartree-Fock atomic wavefunctions. *Atomic Data and Nuclear Data Tables*, 14(3–4), 177–478. [verify — standard source for HF Z_eff values]

4. Baez, J.C. (2021). The Madelung Rules. *Azimuth* (blog). Available at https://johncarlosbaez.wordpress.com/2021/ [verify — documents the open-problem status of the Madelung rule; ~20 exceptions listed]

5. Hund, F. (1925). Zur Deutung der Molekelspektren. *Zeitschrift für Physik*, 33, 345–371. [verify — original empirical statement of Hund's rules from molecular spectra]

6. NIST Atomic Spectra Database. Available at https://physics.nist.gov/asd. [canonical source for ground-state configurations and term symbols; used for all verification in worked examples]

7. Griffiths, D.J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Chapter 5 (identical particles) and Appendix C (electron configurations).

8. Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §5.7 (helium variational calculation, prototype Slater screening).

9. Cotton, F.A. (1990). *Chemical Applications of Group Theory* (3rd ed.). Wiley. Chapter 9 (term symbols and Hund's rules). [verify]

10. Pilar, F.L. (1968). *Elementary Quantum Chemistry*. McGraw-Hill. §8-3 (Slater's rules, worked examples). [verify]

11. Ogata, T. (1986). Why does the 3d subshell fill after the 4s subshell? *Journal of Chemical Education*, 63(8), 698. [verify — one of several papers addressing the 3d/4s ordering pedagogical confusion] [contested]

12. Petrucci, R.H. et al. (2017). *General Chemistry* (11th ed.). Pearson. §8.3 (Slater's rules presented at introductory level; useful pedagogical comparison). [verify]

13. LibreTexts Chemistry, §2.6 "Effective Nuclear Charge" (Mount Royal University). https://chem.libretexts.org. [verify — pedagogical Slater's rules exposition; worked examples at undergraduate level]
