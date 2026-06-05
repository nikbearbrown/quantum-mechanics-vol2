# Chapter 11 — Capstone: The Atom, Built from Simulations
*How a spectroscopist in 1927 knew the ground state of iron before anyone could explain why.*

The spectroscopist's notebook for iron, 1927.

The page lists hundreds of spectral lines for neutral iron — Fe I — measured to four decimal places in angstroms. Every line is a transition between energy levels, and assigning lines to transitions means knowing the levels. The ground state is established: six electrons in 3d, two in 4s. The term symbol is $^5D_4$. The spectroscopist knows this because Hund told them: maximize total spin, then orbital angular momentum, then determine total angular momentum from the filling fraction.

What the spectroscopist cannot fully explain — what nobody in 1927 could fully explain — is why. Why those rules? Why does iron prefer $^5D_4$ over any other configuration? The Schrödinger equation for 26 electrons repelling each other in the field of a 26-proton nucleus is a partial differential equation in 78 spatial dimensions. Nobody is solving that.

What you do instead is build a model. You pretend each electron moves independently in the average field of the nucleus and all the other electrons. You use hydrogenic wave functions, shifted by an effective nuclear charge that accounts for screening. You fill orbitals in the order that minimizes energy, constrained by Pauli exclusion. You apply Hund's three empirical rules. And it works — astonishingly well — for almost every element in the periodic table.

This chapter is about that model: its physical content, its approximations, where it breaks, and what it predicts. The synthesis is not just knowing the rules. It is building a simulation that applies them, validating its output against real data, and being able to say precisely what approximations you made and why they hold.

Every tool this book has given you is about to be used at once.

<!-- → [IMAGE: energy-level diagram for iron showing the [Ar]3d⁶4s² configuration with the five 3d orbitals arranged by Hund's rule — four orbitals singly occupied spin-up, one doubly occupied; the sixth electron shown pairing into the highest m_ℓ = +2 orbital; label S = 2, L = 2, J = 4, term ⁵D₄; this is the worked example made visual] -->

![energy-level diagram for iron showing the (Ar)3d⁶4s² configuration with the five 3d orbitals arranged by Hund's rule — four orbitals singly…](../images/11-capstone-the-atom-fig-01.png)
*Figure 11.1 — energy-level diagram for iron showing the (Ar)3d⁶4s² configuration with the five 3d orbitals arranged by Hund's rule — four orbitals singly…*

---

## Why Hydrogen Is Not Enough

Hydrogen has one electron. The Hamiltonian has an exact solution: wave functions $\psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$ and energies $E_n = -13.6\,\text{eV}/n^2$. Notice what is missing from $E_n$: the quantum number $\ell$. All $n^2$ states at a given $n$ are degenerate — a $3s$, $3p$, and $3d$ orbital all have identical energy. This is the accidental degeneracy of the pure Coulomb potential, arising from a hidden SO(4) symmetry of the $1/r$ interaction.

Add a second electron. The helium Hamiltonian is

$$\hat{H}_\text{He} = \frac{\hat{p}_1^2}{2m_e} + \frac{\hat{p}_2^2}{2m_e} - \frac{Ze^2}{4\pi\epsilon_0 r_1} - \frac{Ze^2}{4\pi\epsilon_0 r_2} + \frac{e^2}{4\pi\epsilon_0|\vec{r}_1-\vec{r}_2|}.$$

The last term — electron-electron Coulomb repulsion — destroys the exact solution and, crucially, destroys the $\ell$-degeneracy. The potential is no longer a pure $1/r$ Coulomb interaction; the SO(4) symmetry is broken. States with the same $n$ but different $\ell$ are no longer degenerate.

The physical mechanism is **orbital penetration and screening**. A $3s$ orbital has its radial probability density peaked closer to the nucleus than a $3d$ orbital with the same $n$. The centrifugal barrier $\ell(\ell+1)\hbar^2/2m_er^2$ pushes high-$\ell$ orbitals outward, keeping $3d$ electrons in the outer reaches of the atom where they are heavily shielded by the inner electrons. The $3s$ electron penetrates to the core and sees more of the bare nuclear charge. More nuclear charge seen means lower energy. The result:

$$E(ns) < E(np) < E(nd) < E(nf) \qquad \text{(multi-electron atoms, any } n\text{).}$$

The degeneracy that made hydrogen's levels so tidy is gone. The periodic table is built on its ruins.

The **central-field approximation** — also called the independent-electron model — replaces the full intractable Hamiltonian with a sum of effective single-electron problems:

$$\hat{H}_\text{eff} = \sum_{i=1}^N\!\left[\frac{\hat{p}_i^2}{2m_e} + V_\text{eff}(r_i)\right],$$

where $V_\text{eff}(r_i)$ is a spherically symmetric average potential including nuclear attraction and the mean Coulomb repulsion from all other electrons. Each electron occupies a hydrogenic-type orbital; the $N$-electron state is a Slater determinant of those orbitals. The energies now depend on both $n$ and $\ell$.

This approximation makes four identifiable sacrifices: it ignores electron-electron correlation (the instantaneous positions of all other electrons, not just their average), relativistic corrections (spin-orbit coupling, mass-velocity term, Darwin term), configuration mixing (the true ground state is a superposition of many Slater determinants), and the self-consistency between orbital energies and occupations. For the first 36 elements, the configurations it predicts are correct in all cases where the energy ordering is unambiguous.

---

## Screening and Effective Nuclear Charge

The effective nuclear charge $Z_\text{eff} = Z - \sigma$ is the net nuclear attraction felt by an electron after accounting for the shielding from all the others. The variational calculation for helium from the preceding chapter established the prototype: each $1s$ electron shields the nucleus by $5/16$ of a proton, giving $Z_\text{eff} = 27/16 \approx 1.69$.

**Slater's rules** (1930) generalize this to any electron in any atom. (Slater, J.C. (1930). *Physical Review*, 36, 57–64.)

First, group the orbitals in this order:

$$[1s]\;\;[2s,2p]\;\;[3s,3p]\;\;[3d]\;\;[4s,4p]\;\;[4d]\;\;[4f]\;\;\ldots$$

Note that $s$ and $p$ orbitals at the same $n$ are grouped together, but $d$ and $f$ orbitals are separated from them — this reflects the penetration difference.

Then apply the shielding contributions to the electron of interest:

For an **s or p electron**: each electron in the same group contributes 0.35 (except in the $[1s]$ group, where the companion contributes 0.30); each electron in the $n-1$ shell contributes 0.85; each electron in shells $n-2$ and below contributes 1.00; electrons in higher groups contribute 0.

For a **d or f electron**: each electron in the same group contributes 0.35; every electron in all inner groups contributes 1.00.

The reason $d$ and $f$ electrons use 1.00 for all inner electrons (rather than 0.85 for the $n-1$ shell) is orbital penetration — or rather, the lack of it. The centrifugal barrier prevents $d$ and $f$ electrons from reaching the core, so they are effectively screened by every inner electron.

Three worked calculations establish the pattern:

**Fluorine (Z = 9), 2p electron.** Groups: $[1s^2][2s^22p^5]$. The electron of interest is in the $[2s,2p]$ group. Same-group contribution: 6 electrons $\times$ 0.35 = 2.10. Inner shell $[1s]$: 2 electrons $\times$ 0.85 = 1.70. Total $\sigma = 3.80$. $Z_\text{eff} = 9 - 3.80 = \mathbf{5.20}$.

**Sodium (Z = 11), 3s electron.** Groups: $[1s^2][2s^22p^6][3s^1]$. The 3s electron is alone in its group. Same-group: 0. The $n-1$ shell $[2s,2p]$: 8 electrons $\times$ 0.85 = 6.80. The $n-2$ shell $[1s]$: 2 electrons $\times$ 1.00 = 2.00. Total $\sigma = 8.80$. $Z_\text{eff} = 11 - 8.80 = \mathbf{2.20}$.

**Iron (Z = 26), 3d electron.** Groups: $[1s^2][2s^22p^6][3s^23p^6][3d^6][4s^2]$. For a $d$ electron, all inner groups contribute 1.00. Same $[3d]$ group: 5 electrons $\times$ 0.35 = 1.75. All inner groups: $2 + 8 + 8 = 18$ electrons $\times$ 1.00 = 18.00. Total $\sigma = 19.75$. $Z_\text{eff} = 26 - 19.75 = \mathbf{6.25}$. The Hartree-Fock value is approximately 6.04 — Slater overestimates by about 3.5%. (Clementi & Roetti (1974), *Atomic Data and Nuclear Data Tables* 14, 177.)

<!-- → [TABLE: Slater Z_eff for the outermost electron of every element from H (Z=1) to Kr (Z=36) — columns: Z, element, outermost orbital, Slater σ, Slater Z_eff, HF Z_eff (from Clementi-Roetti), percent error; highlights the trend of Z_eff increasing across each period and the accuracy of Slater's approximation] -->

---

## The Madelung Rule and Where It Comes From (Or Doesn't)

The Madelung rule — also called the $(n+\ell)$ rule — states: fill subshells in order of increasing $n + \ell$; for equal $n+\ell$, fill lower $n$ first. This gives the sequence:

$$1s,\; 2s,\; 2p,\; 3s,\; 3p,\; 4s,\; 3d,\; 4p,\; 5s,\; 4d,\; 5p,\; 6s,\; 4f,\; 5d,\; 6p,\; \ldots$$

This must be stated honestly: **no one has derived the Madelung rule from first principles as of 2026.** The pattern was identified empirically by Charles Janet in 1929 and Erwin Madelung in 1936 and is confirmed by numerical Hartree-Fock calculations for most elements, but no analytic derivation from the Schrödinger equation exists. John Carlos Baez catalogued this as a genuine open problem in a 2021 survey. (Baez, J.C. (2021), "The Madelung Rules," Azimuth blog, Dec 8 2021.) Use the rule as a reliable empirical pattern — not a derived theorem.

The period structure of the periodic table follows by counting subshell capacities. Each subshell holds $2(2\ell+1)$ electrons: $2(2\ell+1)$ is the number of $m_\ell$ values ($2\ell+1$) times the two spin states per orbital. Sum the capacities of the subshells filling in each period:

| Period | Subshells | Capacity |
|--------|-----------|----------|
| 1 | $1s$ | 2 |
| 2 | $2s, 2p$ | $2 + 6 = 8$ |
| 3 | $3s, 3p$ | $2 + 6 = 8$ |
| 4 | $4s, 3d, 4p$ | $2 + 10 + 6 = 18$ |
| 5 | $5s, 4d, 5p$ | $2 + 10 + 6 = 18$ |
| 6 | $6s, 4f, 5d, 6p$ | $2 + 14 + 10 + 6 = 32$ |

The sequence 2, 8, 8, 18, 18, 32 is not numerology. It is the angular momentum algebra $2(2\ell+1)$ combined with the empirical Madelung ordering. The repeating structure of the periodic table is a consequence of the Schrödinger equation's eigenstates together with the antisymmetrization requirement.

**The exceptions.** The Madelung rule fails for approximately 20 elements. In the first transition series, the most important are chromium ($Z = 24$) and copper ($Z = 29$).

Madelung predicts chromium as $[\text{Ar}]\ 3d^4\ 4s^2$. The actual ground-state configuration (from spectroscopy, verified against NIST) is $[\text{Ar}]\ 3d^5\ 4s^1$. One $4s$ electron has moved into the $3d$ to give a half-filled $3d$ subshell.

Madelung predicts copper as $[\text{Ar}]\ 3d^9\ 4s^2$. Actual: $[\text{Ar}]\ 3d^{10}\ 4s^1$. One $4s$ electron has moved into the $3d$ to complete it.

The mechanism is **exchange-energy stabilization**. By Hund's first rule, a half-filled subshell (all electrons in distinct orbitals with parallel spins) gains extra exchange energy over a nearly-half-filled one with a paired electron. Each pair of electrons with parallel spins lowers the total energy by the exchange integral $K > 0$. A half-filled $3d$ (5 electrons, 10 parallel pairs) or fully filled $3d$ is disproportionately stabilized. When the $3d$–$4s$ gap is small enough — as it is near $Z = 24$ and $Z = 29$ — the exchange-energy gain from filling $3d$ to half or full exceeds the orbital energy cost of demoting one $4s$ electron.

The Madelung mnemonic does not capture this because it treats orbital energies as fixed, whereas the exchange energy depends on the actual occupation pattern.

---

## Hund's Three Rules

Once the configuration is established, you need to determine which quantum state the atom occupies. Within a given configuration, multiple **terms** (combinations of total $L$, total $S$, total $J$) are possible. Hund's three rules select the ground-state term.

**Rule 1 (maximize $S$):** The term with the highest total spin $S$ has the lowest energy.

The mechanism is not a spin-dependent force. It is purely geometric: the highest-$S$ state has the most symmetric spin wave function, which forces the most antisymmetric spatial wave function (to keep the total wave function antisymmetric under exchange). An antisymmetric spatial wave function has lower amplitude when two electrons coincide — the electrons avoid each other in space. Electrons that avoid each other see less Coulomb repulsion. Less repulsion means lower energy. The operative quantity is the exchange integral, which appeared in the helium variational calculation: electrons with parallel spins gain exchange energy of order $K > 0$ per pair.

**Rule 2 (maximize $L$ given $S$):** Among all terms with the same $S$, the one with highest total orbital angular momentum $L$ has the lowest energy.

Electrons orbiting in the same rotational sense tend to stay on opposite sides of the atom, again reducing Coulomb repulsion. The argument has the same flavor as Rule 1 but is less crisp; Rule 2 is less reliable than Rule 1, particularly for heavy elements.

**Rule 3 (determine $J$):** Among all terms with the same $S$ and $L$:

- Less-than-half-filled subshell: $J = |L - S|$
- More-than-half-filled subshell: $J = L + S$
- Exactly half-filled: $L = 0$, so $J = S$

The mechanism for Rule 3 is spin-orbit coupling — the interaction $\hat{H}_\text{so} \sim \lambda\vec{L}\cdot\vec{S}$ between the electron's orbital motion and its spin magnetic moment. The sign of $\lambda$ reverses at the half-filling point, which is why $J$ is minimized for less-than-half-filled and maximized for more-than-half-filled subshells. The full derivation requires perturbation theory and belongs to Volume 3. Apply Rule 3 mechanically in this chapter — it is correct for all elements through the first transition series — but know that its justification is being deferred.

**When Hund's rules fail:** Hund's rules assume the LS coupling (Russell-Saunders) regime, where electron-electron repulsion is much larger than spin-orbit coupling. For heavy elements ($Z \gtrsim 50$), spin-orbit coupling becomes comparable to the Coulomb term and jj coupling is the appropriate framework. $L$ and $S$ are no longer good quantum numbers, and Hund's rules cannot be applied. Even within the LS regime, Rule 1 is the most reliable, Rule 2 is good for the first transition series, and Rule 3 should always be flagged as a spin-orbit preview.

---

## Two Worked Examples

### Carbon (Z = 6): $^3P_0$

The ground-state configuration is $1s^2\, 2s^2\, 2p^2$. The filled $1s$ and $2s$ subshells are spectroscopically inert (they contribute $L=0$, $S=0$ to the total). The two $2p$ electrons determine the term.

**Rule 1.** Place both $2p$ electrons in different orbitals with parallel spins: $m_s = +\frac{1}{2}$ for each. Total $S = 1$; multiplicity $2S+1 = 3$ (triplet). Pairing them in the same orbital gives $S = 0$ — that singlet term is higher in energy by the exchange integral $2K_{2p} \approx 1$ eV.

**Rule 2.** Two electrons in distinct $2p$ orbitals, parallel spins. To maximize $M_L = m_{\ell,1} + m_{\ell,2}$, choose $m_\ell = +1$ and $m_\ell = 0$: total $M_L = 1$. So $L = 1$ (P term).

**Rule 3.** Less-than-half-filled (2 electrons in a 6-electron subshell): $J = |L - S| = |1-1| = 0$.

**Term symbol: $^3P_0$.** Verified against NIST: carbon ground level is $2s^2\,2p^2\,^3P_0$. ✓

The $^3P$ multiplet has $J = 0, 1, 2$; experimentally these lie at 0, 16.4, and 43.4 cm$^{-1}$ above the ground state. The splitting comes from spin-orbit coupling — exactly what Rule 3 encodes and what Volume 3 will derive.

### Iron (Z = 26): $^5D_4$

The configuration is $[\text{Ar}]\, 3d^6\, 4s^2$. The Ar core and $4s^2$ are inert. Six $3d$ electrons determine the term.

**Rule 1.** Five $3d$ orbitals: $m_\ell = +2, +1, 0, -1, -2$. Fill each with one spin-up electron (5 electrons, $S = 5/2$). The sixth must pair into one of them (antiparallel). Net: $(+\frac{1}{2})\times5 + (-\frac{1}{2})\times1 = 2$, so total $S = 2$. Multiplicity $= 5$ (quintet).

**Rule 2.** The five spin-up electrons contribute $M_L = 2+1+0+(-1)+(-2) = 0$ (a closed half-shell). To maximize $M_L$, place the sixth (spin-down) electron in the $m_\ell = +2$ orbital. Total $M_L = 0+2 = 2$, so $L = 2$ (D term).

**Rule 3.** More-than-half-filled (6 of 10 $3d$ electrons): $J = L + S = 2 + 2 = 4$.

**Term symbol: $^5D_4$.** Verified against NIST: iron ground level is $3d^6\,4s^2\,^5D_4$. ✓

---

## The 3d/4s Subtlety

Iron's neutral ground state is $[\text{Ar}]\ 3d^6\ 4s^2$. The ion Fe$^{2+}$ is $[\text{Ar}]\ 3d^6$ — not $[\text{Ar}]\ 3d^4\ 4s^2$. When iron is doubly ionized, both $4s$ electrons are removed before any $3d$ electrons.

This seems paradoxical. If Madelung says $4s$ fills before $3d$, shouldn't $3d$ be removed first?

The resolution: orbital energies in multi-electron atoms are not fixed properties of the orbital label. They depend on how many electrons are in every other orbital, because each electron contributes to the effective potential felt by all the others. In the neutral atom with $4s^2$ and $3d^6$, the self-consistent $3d$ and $4s$ orbital energies are ordered one way. Remove two electrons, and the $3d$ energy drops relative to $4s$ — the effective potential changes. The Madelung filling order applies to neutral ground-state atoms; the ionization removal order follows the orbital energies in the ion, which may differ.

The independent-electron model with fixed Slater $Z_\text{eff}$ does not fully capture this crossing, because $Z_\text{eff}$ itself should change with occupation. This is one of the cleaner places where the approximation visibly fails. The quantitative treatment requires self-consistent Hartree-Fock.

<!-- → [FIGURE: schematic energy-level diagram showing how the 3d and 4s orbital energies vary across the first transition series — a qualitative plot of ε(4s) and ε(3d) vs. Z, showing them nearly degenerate near Z = 20 and the 3d sinking relative to 4s as Z increases; annotate the crossing point and note that the ordering for ions differs from neutral atoms] -->

![schematic energy-level diagram showing how the 3d and 4s orbital energies vary across the first transition series — a qualitative plot of…](../images/11-capstone-the-atom-fig-02.png)
*Figure 11.2 — schematic energy-level diagram showing how the 3d and 4s orbital energies vary across the first transition series — a qualitative plot of…*

---

## The Model's Boundaries

What you have built in this chapter and in the simulation is a model with four identifiable approximations:

**Independent electrons.** Each electron moves in the average field of all others; their instantaneous positions are ignored. The true wave function is not a Slater determinant — it has contributions from many configurations. The correlation energy (the energy difference between the true ground state and the HF minimum) is typically a few percent of the total binding energy but matters for chemistry.

**Hydrogenic orbital shapes.** The radial and angular wave functions are hydrogenic, modified only by $Z_\text{eff}$. In reality the orbitals are self-consistently deformed by the full $V_\text{eff}(r)$.

**Central-field potential.** $V_\text{eff}(r)$ is spherically symmetric — the average Coulomb field. Any anisotropy (crystal fields, external fields) is ignored.

**Slater screening.** Slater's rules are a semi-empirical parameterization of $\sigma$ that reproduces orbital energies and ionization energies to 10–20%. The Hartree-Fock values (Clementi and Roetti 1974) are systematically more accurate.

Despite these approximations, the model predicts correct electron configurations for 16 of the 18 elements in the first transition series (Cr and Cu being the exceptions), correct term symbols for all of them, and $Z_\text{eff}$ values within a few percent of the Hartree-Fock benchmark. That is a remarkable return on a model whose central equation is a product of one-electron functions.

The Madelung rule itself has no derivation. Present it as what it is: an empirical pattern that works, with approximately 20 known exceptions, whose first-principles derivation remains an open problem in quantum mechanics as of 2026.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the Madelung filling sequence and unpaired electron count.*
   Write the ground-state electron configuration of (a) nitrogen ($Z = 7$), (b) chlorine ($Z = 17$), (c) manganese ($Z = 25$) using the Madelung sequence. For each, state the number of unpaired electrons.
   *Tests: command of the Madelung order for main-group and transition elements.*

2. *Difficulty: Warm-up — tests Slater's rules for s and p electrons.*
   Compute $Z_\text{eff}$ using Slater's rules for (a) the $2p$ electron of oxygen ($Z = 8$), (b) the $4s$ electron of potassium ($Z = 19$). Show the grouping and each shielding contribution explicitly.
   *Tests: ability to execute Slater's grouping and apply the 0.35/0.85/1.00 constants correctly.*

3. *Difficulty: Warm-up — tests the $2(2\ell+1)$ counting and period structure.*
   The period structure of the periodic table has lengths 2, 8, 8, 18, 18, 32. Derive each from the Madelung filling sequence and the formula $2(2\ell+1)$. State which subshells fill in periods 4 and 6.
   *Tests: connection between the angular momentum counting formula and the macroscopic structure of the periodic table.*

**Application**

4. *Difficulty: Application — tests all three Hund's rules on a more-than-half-filled subshell.*
   Apply Hund's rules to oxygen ($Z = 8$, config $1s^2\,2s^2\,2p^4$) to find the ground-state term symbol. Show: (a) which rule determines $S$ and its value; (b) which rule determines $L$ and the maximum-$M_L$ microstate; (c) why Rule 3 gives $J = 2$ for a more-than-half-filled subshell; (d) the full term symbol $^{2S+1}L_J$. Verify against NIST.
   *Tests: full execution of Hund's three rules for the case opposite to carbon.*

5. *Difficulty: Application — tests the Madelung exception mechanism.*
   Chromium ($Z = 24$) is a Madelung exception. (a) State the Madelung prediction and the actual NIST configuration. (b) Explain in one paragraph, using the exchange integral, why the actual configuration has lower energy. (c) Compute $Z_\text{eff}$ for a $3d$ electron in the actual configuration $[\text{Ar}]\,3d^5\,4s^1$ using Slater's rules.
   *Tests: ability to apply the exchange-energy mechanism to explain a specific exception; Slater calculation in the exception case.*

6. *Difficulty: Application — tests the 3d/4s subtlety.*
   Neutral manganese ($Z = 25$) has configuration $[\text{Ar}]\,3d^5\,4s^2$. The ion Mn$^{2+}$ loses two electrons. (a) Identify which electrons are removed and write the Mn$^{2+}$ configuration. (b) Find the ground-state term symbol of Mn$^{2+}$ using Hund's rules. (c) Explain why the order of electron removal (4s before 3d) may seem to contradict the Madelung filling order.
   *Tests: the filling-vs-removal ordering distinction; Hund's rules for a half-filled subshell.*

**Synthesis**

7. *Difficulty: Synthesis — requires building the full microstate table for a partially filled subshell.*
   Construct the full term-symbol analysis for vanadium ($Z = 23$, config $[\text{Ar}]\,3d^3\,4s^2$). List all microstates for the $3d^3$ configuration in a table with columns $m_\ell$ for each of the three electrons and $m_s$. Identify the term with highest $S$, then highest $L$, then determine $J$. Write the ground-state term symbol and verify against NIST.
   *Tests: building the microstate table from scratch; the full procedure, not just the answer.*

8. *Difficulty: Synthesis — comprehensive survey of the first transition series.*
   For the elements $Z = 21$ through $Z = 30$, make a table with: (a) Madelung-predicted configuration; (b) actual ground-state configuration from NIST; (c) whether they agree; (d) for disagreements, the mechanism (half-filled or fully-filled stabilization). Identify every exception and briefly explain each.
   *Tests: comprehensive application of Madelung with NIST cross-checking; recognizes the exchange-stabilization pattern.*

**Challenge**

9. *Difficulty: Challenge — quantifies the exchange-energy mechanism for chromium.*
   For the two configurations under consideration for chromium — predicted $[\text{Ar}]\,3d^4\,4s^2$ and actual $[\text{Ar}]\,3d^5\,4s^1$ — count the number of parallel-spin electron pairs in the 3d subshell for each. The exchange energy is approximately $E_K = -K \times (\text{number of parallel-spin pairs})$, where $K \approx 0.18$ eV for 3d electrons in Cr. (a) How many parallel-spin pairs does each configuration have? (b) What is the exchange-energy difference in eV? (c) The $3d$–$4s$ energy gap for Cr is approximately 0.2 eV. Is the exchange-energy gain sufficient to explain the exception? (d) Why does this argument not work for titanium ($Z = 22$), which does not show the exception?
   *Tests: quantitative application of the exchange-energy mechanism; identifies why the exception occurs for Cr and not Ti.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to generate the simulation (write that yourself), but to probe the physics, expose the model's limitations, and test the reasoning.

1. Ask an LLM to derive the $2(2\ell+1)$ formula for subshell capacity starting from the quantum numbers $\ell$, $m_\ell$, and $m_s$. Then ask it: does this formula assume anything beyond the Pauli exclusion principle? Could a particle with spin-1 (three spin states) fill a $p$ subshell with $3(2\ell+1) = 9$ electrons? What would the period structure be for such a particle?

2. Ask an LLM to explain the mechanism of Hund's Rule 1 in terms of the exchange integral. The explanation should use the word "antisymmetry" — ask it to trace the chain: parallel spins → symmetric spin function → antisymmetric spatial function → electrons avoid each other → lower Coulomb repulsion → lower energy. If any step is missing or reversed, identify it and ask for a correction.

3. The Madelung rule has no derivation from first principles. Ask an LLM to sketch the closest thing to a derivation that exists — perhaps a heuristic involving the average radial distance of orbitals as a function of $n+\ell$. Then ask: what would a genuine derivation have to explain? Specifically, what would it need to say about the exceptions in the $d$-block?

4. Ask an LLM to compute $Z_\text{eff}$ by Slater's rules for the $3d$ electron of nickel ($Z = 28$, config $[\text{Ar}]\,3d^8\,4s^2$) and for the $4s$ electron of the same atom. Which is larger? What does this tell you about which electron is more tightly bound? Cross-check by comparing to experimental ionization energies.

5. Ask an LLM to explain why Fe$^{2+}$ is $[\text{Ar}]\,3d^6$ and not $[\text{Ar}]\,3d^4\,4s^2$. The explanation should invoke the self-consistent nature of orbital energies — that removing electrons changes the effective potential and thus the orbital energy ordering. If the LLM's explanation is purely about the Madelung rule without mentioning the self-consistency issue, push back.

---

## References

Slater, J. C. (1930). Atomic shielding constants. *Physical Review*, 36, 57–64.

Clementi, E., & Roetti, C. (1974). Roothaan-Hartree-Fock atomic wavefunctions. *Atomic Data and Nuclear Data Tables*, 14, 177–478.

Madelung, E. (1936). *Mathematische Hilfsmittel des Physikers* (3rd ed.). Springer.

Baez, J. C. (2021). The Madelung Rules. *Azimuth* (blog).

Hund, F. (1925). Zur Deutung der Molekelspektren. *Zeitschrift für Physik*, 33, 345–371.

NIST Atomic Spectra Database. https://physics.nist.gov/asd. (Canonical source for ground-state configurations and term symbols; all verification in worked examples.)

Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Chapter 5 and Appendix C.

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books.

Cotton, F. A. (1990). *Chemical Applications of Group Theory* (3rd ed.). Wiley. Chapter 9.

---

## Running Project — Build the Atom

**This chapter integrates:** every per-chapter module into one program that takes an element's $Z$ and returns its ground-state electron configuration, $Z_\text{eff}$ (Slater's rules), and term symbol $^{2S+1}L_J$ — then validates those predictions against cited spectroscopic data, with iron's $^5D_4$ as the golden test.

This is the assembly chapter. The pieces are built:

- **Ch 1** orbital basis $(n,\ell,m_\ell,m_s)$ · **Ch 2** diagonalize/sort orbital energies · **Ch 3** CSCO labeling · **Ch 4** stationarity/conservation
- **Ch 5** central-field $V_\text{eff}$ and radial solver · **Ch 6** $2(2\ell+1)$ capacities · **Ch 7** spin doubling · **Ch 8** term enumeration ($L,S,J$)
- **Ch 9** screened hydrogenic $R_{n\ell}(Z_\text{eff})$ · **Ch 10** Slater determinant, Pauli, parallel-pair count

This chapter adds the two physics layers that were deliberately withheld — **Slater's rules** for $Z_\text{eff}$ and **Hund's three rules + Madelung ordering with the Cr/Cu exchange exceptions** — and wires everything into `build_atom(Z)`. Then it does the thing the whole project was for: checks the output against data it did not fit.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Implementing Slater's rules as a lookup-and-sum over the orbital grouping $[1s][2s,2p][3s,3p][3d][4s,4p]\dots$ with the 0.35/0.85/1.00 constants — *Why AI works here:* it is a rule-table transcription; you check it against the chapter's three worked $Z_\text{eff}$ values (F: 5.20, Na: 2.20, Fe $3d$: 6.25).
- Wiring the modules into a single `build_atom(Z)` pipeline and formatting the report (configuration string, $Z_\text{eff}$, term symbol) — *Why AI works here:* it is integration glue over already-tested components; you check the end-to-end output against carbon ($^3P_0$) and iron ($^5D_4$).
- Building the NIST-comparison harness: load a small reference table and diff predictions against it — *Why AI works here:* it is data plumbing with a clear pass/fail per element.

**The tell:** You are using AI well when you have cited ground truth to diff against — the chapter's worked $Z_\text{eff}$ values, NIST configurations, and NIST term symbols.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding whether a mismatch with NIST is a *bug* or a *known limit of the model* — *Why AI fails here:* Cr and Cu *should* disagree with the plain Madelung prediction, and the $3d$/$4s$ ion-removal subtlety *should* expose the fixed-$Z_\text{eff}$ approximation; an LLM may "fix" these by hard-coding the right answer, hiding exactly the breakdown the project exists to expose.
- Resolving the Cr/Cu anomaly by recall instead of the exchange-energy comparison — *Why AI fails here:* the honest version counts parallel-spin pairs and weighs the exchange gain ($\sim K$ per pair) against the $3d$–$4s$ gap; an LLM that simply outputs $3d^54s^1$ teaches nothing and will misfire on the next ambiguous case.
- Accepting any term symbol the model "knows" for an element — *Why AI fails here:* term symbols are a prime hallucination target (right format, wrong $J$); every one must be derived by Hund's rules and checked against NIST.

**The tell:** If the simulator's agreement with iron's $^5D_4$ came from the AI recalling $^5D_4$ rather than deriving it through max-$S$, max-$L$, more-than-half-filled $J=L+S$, the validation is circular and worthless.
**Physics-judgment connection:** this is the capstone discipline — validate a multi-step prediction against a cited measured value you did not fit, and be able to say precisely *which approximation* each disagreement exposes (central-field, fixed $Z_\text{eff}$, LS-coupling) rather than papering over it.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the two withheld physics layers (Slater's rules, Hund + Madelung-with-exceptions) and the `build_atom(Z)` integration.
**Tool:** Claude Project — this is a multi-file assembly where persistent context over all prior modules helps the model wire them correctly.
**The Prompt:**
```
This Claude Project contains my atomic-structure simulator modules: orbitals.py,
oneelectron.py, csco.py, dynamics_check.py, central_field.py, subshells.py,
spin.py, coupling.py, hydrogenic.py, slater.py. Now assemble the full builder.

Write two new modules plus an integrator:

1. slater_rules.py: z_eff(Z, n, l) implementing Slater's rules — group orbitals
   as [1s][2s,2p][3s,3p][3d][4s,4p][4d][4f]..., apply shielding 0.35 (same group;
   0.30 within 1s), 0.85 (n-1 shell, for s/p electrons), 1.00 (deeper, and ALL
   inner groups for d/f electrons). Return Z - sigma.

2. hund.py: ground_term(l, k) applying Hund's three rules to an open subshell
   (max S; then max L; then J = |L-S| if <half-filled, J = L+S if >half-filled,
   J = S if exactly half-filled). Return the term string (2S+1)L_J.
   Also madelung_config(Z) returning the configuration, WITH the Cr/Cu exchange
   exceptions handled by an explicit exchange-vs-gap comparison (count parallel
   pairs; if a half/full d-shell gain beats the small 3d-4s gap, promote one 4s
   electron) — NOT by hard-coding the answer.

3. build_atom.py: build_atom(Z) returning a dict {config, z_eff_valence,
   term_symbol} by calling the modules. Print a clean report.

VALIDATION REQUIRED in __main__:
  - Assert z_eff for F 2p = 5.20, Na 3s = 2.20, Fe 3d = 6.25 (chapter values).
  - Assert build_atom(6).term_symbol == '3P0' (carbon).
  - Assert build_atom(26) gives config [Ar]3d6 4s2 and term '5D4' (iron, golden).
  - Assert build_atom(8).term_symbol == '3P2' (oxygen).

Do NOT hard-code Cr/Cu or any term symbol — derive everything. Flag, don't hide,
any element where the central-field model disagrees with NIST.
```
**What this produces:** `slater_rules.py`, `hund.py`, `build_atom.py` — the complete simulator with self-validating assertions.
**How to adapt:** *Your system:* keep a small `nist_reference.csv` (Z, config, term) for ~30 elements as the diff target. *ChatGPT/Gemini:* paste the module sources inline since there is no project memory; the prompt is otherwise identical. *Claude Project:* the system prompt should carry the standing rule "derive, never recall, term symbols; flag model breakdowns" so every session inherits it.
**Builds on:** all ten prior modules.  **Next:** R5 runs the full periodic-table validation sweep.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the assembled simulator plus a validation sweep across the first transition series, run and diffed against NIST.
**Tool:** Claude Code (multi-file assembly plus running the validation sweep in the project directory).
**Skill level:** Advanced
**Setup — confirm:**
- [ ] All ten prior modules present and their tests passing in `build-the-atom/`.
- [ ] A `nist_reference.csv` with columns Z, config, term for Z = 1–30 (you supply this from NIST).
- [ ] `numpy`, `scipy`, `pytest`.
- [ ] CLAUDE.md rules from all prior chapters present.
**The Task:**
```
In build-the-atom/, create slater_rules.py (z_eff via Slater's rules), hund.py
(ground_term via Hund's three rules; madelung_config with Cr/Cu handled by an
exchange-vs-gap comparison, NOT hard-coded), and build_atom.py (build_atom(Z)
returning config, z_eff_valence, term_symbol).

Then create validate.py that, for Z = 1..30, calls build_atom(Z), diffs config
and term against nist_reference.csv, and prints a table with columns:
Z, predicted config, NIST config, MATCH?, predicted term, NIST term, MATCH?.
At the end print: total matches, and an explicit list of mismatches with a
one-line reason drawn from {Madelung exception (Cr/Cu), fixed-Z_eff limit,
LS-coupling breakdown}.

Create test_build_atom.py asserting: F 2p z_eff==5.20, Na 3s z_eff==2.20,
Fe 3d z_eff==6.25 (to 0.01); build_atom(6) term=='3P0'; build_atom(26) config
is [Ar]3d6 4s2 and term=='5D4'; build_atom(8) term=='3P2'.

Run `pytest -q`, then run `python validate.py`, and show both outputs. Do not
hard-code term symbols or the Cr/Cu configs.
```
**Expected output:** the three new modules, `validate.py`, a passing test suite, and a printed validation table for Z = 1–30 with iron showing config $[\text{Ar}]3d^64s^2$ and term $^5D_4$ both MATCH.
**What to inspect:** confirm the golden test — iron $^5D_4$ — passes by derivation; confirm Slater $Z_\text{eff}$ for F/Na/Fe match the chapter; inspect the mismatch list: Cr and Cu should appear *only if your exchange comparison failed to promote the $4s$ electron* — if the comparison works, they MATCH and the mismatch list is honest about any remaining LS-coupling cases at higher $Z$.
**What to inspect (physics):** for iron, trace the derivation: $3d^6 \to S=2$ (quintet), $L=2$ (D), more-than-half-filled $\to J=L+S=4$, giving $^5D_4$. If the code returns $^5D_0$ it applied the less-than-half-filled $J=|L-S|$ branch — the half-filling test is inverted.
**If it goes wrong:** the most common failure is the $J$ branch (less-vs-more than half-filled) being reversed, which flips iron to $^5D_0$. Recovery: test `ground_term` on both carbon ($p^2$, less than half, $J=0$) and oxygen ($p^4$, more than half, $J=2$) — these bracket the branch and expose the inversion immediately.
**CLAUDE.md / AGENTS.md note:** add — "Validation is non-negotiable: every `build_atom` prediction is diffed against `nist_reference.csv`. Mismatches are *reported with a physical reason* (Madelung exception, fixed-$Z_\text{eff}$ limit, LS-coupling breakdown), never silently corrected."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the complete `build_atom(Z)` simulator and its validation sweep — the whole project, against cited spectroscopic data.
**Validation type:** Agentic output (multi-module pipeline) + Numerical result + Structured data
**Risk level:** High — this is the deliverable; its credibility rests entirely on agreement with data it did not fit, and on honesty about where it fails.
**Setup:** use your assembled R3/R4 simulator and the NIST reference table. The golden test is iron's $^5D_4$, derived (not recalled).
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Capstone: The Atom
□ Correctness: does build_atom(26) return [Ar]3d6 4s2 and 5D4, DERIVED via
  max-S, max-L, more-than-half-filled J=L+S (not recalled)?
□ Completeness: does the sweep cover Z=1..30 and diff BOTH config and term
  against NIST for every element?
□ Scope: are Cr and Cu handled by an exchange-vs-gap comparison rather than a
  hard-coded special case?
□ Physics criterion 1: do Slater Z_eff values match the chapter (F 2p=5.20,
  Na 3s=2.20, Fe 3d=6.25) to 0.01?
□ Physics criterion 2: are mismatches REPORTED with a physical reason (Madelung
  exception / fixed-Z_eff limit / LS-coupling breakdown), not hidden?
□ Physics criterion 3: carbon=3P0 and oxygen=3P2 (the half-filling J branch is
  correct in both directions)?
□ Failure-mode check: any of —
  - fluent but wrong (term symbol recalled, so agreement with NIST is circular)
  - Cr/Cu hard-coded (the model's honest breakdown is concealed)
  - J half-filling branch inverted (iron comes out 5D0)
  - validation harness reports a match it did not actually compute
  - mismatches silently "corrected" to match NIST
```
**What to do with findings:** pass → the simulator reproduces configurations and ground terms across the periodic table and is honest about its limits; record that the iron $^5D_4$ match came by derivation, which is what makes it trustworthy. One fail (e.g. inverted $J$ branch) → fix and re-run the full sweep, documenting the change. Multiple fails / cannot-determine → the integration is not trustworthy; this is the clearest "When NOT to Use AI" moment in the book — the model assembled plausible code that fakes agreement, and you must re-derive the contested predictions (term symbols, Cr/Cu) by hand against NIST before believing any of it.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI implemented Slater's rules, Hund's-rule term selection, and the integration glue, and ran the Z = 1–30 validation sweep against my NIST reference table.
> *2:* The AI could not be trusted to distinguish a genuine model breakdown (Cr, Cu, the $3d$/$4s$ ion subtlety, LS-coupling at high $Z$) from a bug — judging which disagreements are the *physics* of the central-field approximation, and which are coding errors, was the irreducibly human part.
**Physics-judgment connection:** the capstone verification discipline — validating a complete, multi-step prediction against a cited measured value the model never fit (iron's $^5D_4$), and being able to name exactly which approximation each residual disagreement exposes. That is the whole point: a simulation you can defend, line by line, against the data.
