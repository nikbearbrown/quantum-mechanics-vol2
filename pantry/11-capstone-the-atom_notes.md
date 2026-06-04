# Research Notes: Chapter 11 — Capstone: The Atom

**Corresponding chapter:** chapters/11-capstone-the-atom.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to: (1) use hydrogenic orbitals as building blocks for multi-electron atoms; (2) apply the aufbau principle, Pauli exclusion, and Hund's rules to predict the ground-state electron configuration of any element through the transition metals; (3) calculate approximate effective nuclear charge using Slater's rules; (4) explain the period structure of the periodic table (period lengths 2, 8, 8, 18, 18, 32) from orbital energy ordering; (5) predict the configuration of a specific element (e.g., carbon or iron), check it against NIST data, and defend the approximations made (independent-electron model, hydrogenic orbital shapes, Slater screening) including identifying where they break (the 3d/4s energy ordering subtlety in transition metals).

This is a PROJECT chapter: the synthesis deliverable is a working simulation/visualization of orbital filling that the student builds and validates against known configurations.

---

## A. Conceptual foundations

### Hydrogenic orbitals as building blocks

- In hydrogen, the energy $E_n = -13.6\,\text{eV}/n^2$ depends only on $n$, not on $\ell$: this is the accidental $\mathfrak{so}(4)$ degeneracy of the Coulomb potential (Ch 7/10). All $n^2$ orbitals at a given $n$ are degenerate.
- In a multi-electron atom with nuclear charge $Z$, each electron moves in the field of the nucleus plus the average Coulomb repulsion of the other electrons. The potential is no longer a pure $1/r$ Coulomb potential. The $\mathfrak{so}(4)$ symmetry breaks immediately. States with the same $n$ but different $\ell$ are no longer degenerate: low-$\ell$ orbitals penetrate closer to the nucleus (less shielded by inner electrons) and fall to lower energy.
- Key qualitative result: at any given $n$, $E(ns) < E(np) < E(nd) < E(nf)$. The s orbital penetrates most, is least screened, lowest energy. (_lib_qmsri-08 §"The periodic table"; _lib_qmsri-07 §"The hidden symmetry")
- The forms of the wave functions — $\psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$ — are still approximately hydrogenic in shape, but the energies are shifted. This is the central approximation of the independent-electron (central-field) model.

### Screening and effective nuclear charge

The effective nuclear charge $Z_\text{eff}$ is the net nuclear charge experienced by a valence electron after accounting for the shielding of inner electrons:
$$Z_\text{eff} = Z - \sigma$$
where $\sigma$ is the shielding constant summed from all other electrons.

**Slater's rules (1930)** provide a systematic, semi-empirical recipe for estimating $\sigma$:
1. Group the orbitals in the order: [1s] [2s,2p] [3s,3p] [3d] [4s,4p] [4d] [4f] [5s,5p] ...
2. Electrons to the right of the electron of interest contribute 0 to $\sigma$.
3. Each electron in the same [ns,np] group contributes 0.35 (0.30 for 1s electrons).
4. For an s or p electron: each electron in the shell below (n-1) contributes 0.85; all electrons in lower shells contribute 1.00.
5. For a d or f electron: all electrons inside contribute 1.00.

Example for a 3p electron in sodium (Z=11, config [Ne]3s1 → sodium 3p would be the next): the rule gives specific $Z_\text{eff}$ values that match experimental ionization energies and atomic radii to reasonable accuracy.

The shielding values were derived semi-empirically from atomic spectroscopy data (Slater, 1930). The rules encode the key physics: s and p orbitals penetrate to near the nucleus and see more of Z (lower shielding from inner shells), while d and f orbitals are spatially excluded and are more effectively shielded (inner electrons contribute 1.00, not 0.85). (Sources: LibreTexts §2.6 Slater's Rules; Wikipedia Slater's rules; Journal of Chemical Education, Shielding Percentages, vol 78 p. 635)

**Variational version:** the helium variational calculation ($Z_\text{eff} = Z - 5/16 = 27/16 \approx 1.69$ for helium, giving $E \approx -77.4$ eV vs experiment $-79.0$ eV) is the analytic prototype — one electron screens the other by $5/16$ of a proton charge. Slater's rules are a systematic generalization of this idea. (Townsend notes §5.7)

### The aufbau principle

Fill orbitals in order of increasing energy, subject to:
1. **Pauli exclusion**: at most 2 electrons per spatial orbital (one spin-up, one spin-down).
2. **Hund's first rule**: within a degenerate subshell, fill with parallel spins before pairing.

The filling sequence follows the **Madelung rule** (n+ℓ rule): fill in order of increasing $n+\ell$; when two orbitals have the same $n+\ell$, fill the lower-$n$ one first. This gives:
$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\ 7s,\ 5f,\ 6d,\ 7p,\ \ldots$$

Period lengths follow from summing $2(2\ell+1)$ (twice the orbital degeneracy, for spin) over the subshells filling within each period:
- Period 1: 1s → 2 elements
- Period 2: 2s, 2p → 2 + 6 = 8 elements
- Period 3: 3s, 3p → 2 + 6 = 8 elements
- Periods 4 and 5: s + d + p → 2 + 10 + 6 = 18 elements
- Periods 6 and 7: s + f + d + p → 2 + 14 + 10 + 6 = 32 elements
These are not numerology. They are $2(2\ell+1)$ summed over the subshells in each row, and follow from the quantum numbers of the angular momentum algebra. (Sources: Wikipedia Aufbau principle; LibreTexts 5.17; _lib_qmsri-08 §"The periodic table")

### Hund's rules (all three, for this chapter)

**Rule 1 (maximise S):** For a given configuration, the term with highest total spin S has lowest energy. Mechanism: highest S → most symmetric spin → most antisymmetric spatial → electrons avoid each other → lowest Coulomb repulsion. This is the exchange integral argument from Ch 10.

**Rule 2 (maximise L given S):** Among terms with the same S, the highest L has lowest energy. Higher L → electrons move in the same rotational direction → avoid each other → lower Coulomb repulsion. (Less crisp mechanistically than Rule 1, but the physics is the same class of exchange-correlation argument.)

**Rule 3 (J from L and S):** For a less-than-half-filled subshell, $J = |L-S|$ is the ground-state term; for more-than-half-filled, $J = L+S$. Mechanism: spin-orbit coupling $\sim \lambda\, \vec{L}\cdot\vec{S}$; $\lambda > 0$ for lighter atoms, $\lambda < 0$ for heavier, determining which J is lowest. (Only Rule 1 is covered in depth in Ch 10; Rules 2 and 3 are appropriate for introduction in the capstone context, with Rule 3 flagged as needing spin-orbit coupling from later chapters.) (Source: Wikipedia Hund's rules; UCSB lecture notes; Bohrium sciencepedia)

### The 3d/4s ordering subtlety

The Madelung rule says 4s fills before 3d (n+ℓ: 4s has 4+0=4 < 3d has 3+2=5). But after the 3d fills, in some transition metals the 3d and 4s orbital energies are comparable or crossed. This leads to:
- **Chromium** (Z=24): predicted [Ar] 3d⁴4s² by Madelung, actual [Ar] 3d⁵4s¹. The exchange-energy stabilization of a half-filled 3d subshell (maximum multiplicity by Hund's Rule 1) beats the small 3d/4s gap.
- **Copper** (Z=29): predicted [Ar] 3d⁹4s², actual [Ar] 3d¹⁰4s¹. A completely filled 3d subshell similarly gains extra exchange stabilization.

About 20 elements in the periodic table show such exceptions to the simple Madelung scheme. The framework handles them by comparing the exchange-energy gain from filling the d subshell against the cost of promoting an s electron to d; the simple mnemonic does not handle them. (Sources: Wikipedia Aufbau principle §Exceptions; Madelung rule post, John Carlos Baez blog; Sodium Lamp blog on Madelung exceptions; _lib_qmsri-08 §"The periodic table")

The deeper question (why does Madelung hold as often as it does?) is still an open problem in electronic structure theory; no simple first-principles derivation of the Madelung rule from the Schrödinger equation has been established. (Source: Baez, Azimuth blog "The Madelung Rules," 2021)

---

## B. Domain examples and cases

### Worked example 1: Carbon (Z=6)

Configuration: 1s² 2s² 2p². Two electrons in three available 2p orbitals.

Applying Hund's Rule 1: place one electron in each of two different 2p orbitals with parallel spins (both $m_s = +1/2$). Ground-state configuration: 1s² 2s² 2p², with 2p orbitals $(m_\ell = -1, m_s = +1/2)$ and $(m_\ell = 0, m_s = +1/2)$ occupied.

Total spin $S = 1$ (triplet). Total orbital angular momentum: by Hund's Rule 2, maximize $L$ → $L = 1$. This gives the $^3P$ term. Applying Rule 3 (less than half-filled): $J = |L-S| = |1-1| = 0$. Ground-state term symbol: $^3P_0$.

Compare: if the two 2p electrons were paired in the same orbital (violating Hund's Rule 1 by putting both in $m_\ell = -1$, $m_s = \pm 1/2$), the spatial wave function would be symmetric (both in same orbital) and the energy would be higher by approximately $2K_{2p} \approx 1$ eV. The ground-state configuration is lower in energy — this is directly observable in the UV photoelectron spectrum of carbon.

### Worked example 2: Iron (Z=26)

Configuration: [Ar] 3d⁶ 4s². Six electrons in five available 3d orbitals.

Five 3d orbitals: fill each singly with parallel spin (5 electrons, $S=5/2$, $m_s = +1/2$ each), then one more electron must pair into one of the 3d orbitals. Hund's Rule 1 gives maximum $S$ for the remaining 5 parallel-spin electrons; the sixth pairs with one of them. Net $S = (5-1)/2 + 1/2 = 2$, so total $S = 2$ (quintet). By Hund's Rule 2 (maximize $L$): sum the $m_\ell$ values $= +2 + 1 + 0 + (-1) + (-2) + 2 = 2$, so $L = 2$ (D term). More than half-filled (6 of 10 electrons): $J = L+S = 2+2 = 4$. Ground-state term symbol: $^5D_4$. This matches the NIST Atomic Spectra Database entry exactly.

4s² fills before 3d⁶ by the Madelung rule. After filling, iron does not become [Ar] 3d⁶4s² → [Ar] 3d⁷4s¹ or [Ar] 3d⁸; the 4s/3d energy gap at Z=26 is large enough that the Madelung ordering holds for iron (unlike Cr and Cu).

### Simulation: orbital filling visualizer

The capstone project is a student-built simulation. It should show:
1. **Energy level diagram**: show all subshell energies as a function of Z (or for a fixed Z), with Madelung ordering labeled. The 3d/4s crossover near Z=21–23 is visible on such a diagram.
2. **Aufbau filling animation**: for Z from 1 to 36 (or student-chosen), step through each element, place electrons one at a time, and display the resulting configuration.
3. **Hund's rule enforcement**: within each subshell, fill orbitals with parallel spins before pairing.
4. **Output**: for each Z, display the configuration in both full and noble-gas shorthand, the Hund's-rule ground term symbol (Rules 1 and 2; Rule 3 optional), and the predicted $Z_\text{eff}$ from Slater's rules.
5. **Validation check**: compare predicted configuration to known experimental configurations (NIST database or Griffiths/Szabo appendix). Flag any discrepancy (Cr, Cu are the canonical ones in the first transition series).

Existing interactive tools for reference: PhET-style electron configuration builder (Simulations4All), Javalab Electron Configuration, ExploreLearning Gizmos (paywalled), HyperPhysics atomic electron configuration. The student's simulation should go further by computing and displaying Slater $Z_\text{eff}$ alongside the configuration.

---

## C. Connections and dependencies

- **Ch 10 (Identical Particles, this volume):** The entire capstone rests on Ch 10. Slater determinant, Pauli exclusion, and Hund's Rule 1 are all derived there. The capstone applies them.
- **Ch 7 / Ch 9 (Hydrogen atom, 3D QM, this volume):** Hydrogenic orbital shapes and quantum number ranges $(n,\ell,m_\ell,m_s)$ provide the building blocks. The screening argument that breaks Coulomb degeneracy ($\ell$-splitting) connects to the $\mathfrak{so}(4)$ discussion in Ch 7.
- **Ch 9 (Variational principle, this volume):** Hartree-Fock as the variational principle applied to a Slater-determinant ansatz is the systematic theoretical underpinning of the independent-electron model being applied here. The helium variational calculation ($Z_\text{eff} = 27/16$) is the prototype.
- **Future: perturbation theory (Ch 8, this volume):** Spin-orbit coupling (Hund's Rule 3, fine structure, LS vs jj coupling) requires perturbation theory. The capstone should flag this as where Rule 3 will be fully justified.
- **Future: condensed matter (later volumes):** The aufbau principle for atoms becomes the band filling and Fermi energy concept for solids. The analogy is exact: Hund's rule in atoms becomes Stoner criterion for ferromagnetism.
- **Chemistry connection:** The periodic table as recovered here is the same table underlying all of chemistry. Bond formation (Lewis structures, valence, hybridization) rests on the valence electron configurations predicted by the aufbau principle. The capstone is the point where physics explains chemistry.

---

## D. Current state of the field

### Theory

- The independent-electron (central-field) model with the aufbau principle gives correct configurations for ~90% of elements without further computation. For the remainder, more sophisticated methods are needed.
- Hartree-Fock self-consistent field (HF-SCF) is the systematic realization of the idea: minimize $\langle\Psi|\hat{H}|\Psi\rangle$ over a single Slater determinant by solving coupled one-electron equations iteratively until self-consistency. The resulting orbital energies (Koopmans' theorem: orbital energy ≈ ionization energy of that orbital) match experiment to a few percent. (Sources: LibreTexts §9.7 SCF; Fiveable HF study guide)
- Post-HF methods (configuration interaction, coupled-cluster CC-SD(T), many-body perturbation theory) are the current precision tools. CC-SD(T) with large basis sets achieves sub-kcal/mol accuracy for total energies.
- Density functional theory (DFT) is the dominant computational method. It works directly with the electron density $\rho(\vec{r})$ and an exchange-correlation functional $E_{xc}[\rho]$; it sidesteps the $N$-electron wave function entirely. DFT is $O(N^3)$ in system size vs HF's $O(N^4)$. "Chemical accuracy" in DFT is still an active research area.
- The Madelung rule lacks a rigorous derivation from the Schrödinger equation. As of 2026, no complete analytic first-principles proof of the n+ℓ ordering rule exists; it is a semi-empirical pattern confirmed computationally. This is a genuine open problem. (Source: Baez blog, "The Madelung Rules," 2021)

### Experiment and NIST data

- The definitive source for ground-state configurations and term symbols is the NIST Atomic Spectra Database (https://physics.nist.gov/asd). Configurations are experimentally determined from spectroscopic analysis of energy levels. Students should validate their simulation against NIST, not a textbook table (textbooks occasionally contain the configuration as Madelung would predict rather than the experimental value).

### Pedagogy

- Slater's rules, though semi-empirical, are well-studied pedagogically: the 2001 paper in the Journal of Chemical Education (vol 78, p. 635, "Screening Percentages Based on Slater Effective Nuclear Charge as a Versatile Tool for Teaching Periodic Trends") shows they reliably reproduce periodic trends in ionization energy, atomic radius, and electronegativity at the undergraduate level.
- Interactive simulations (Javalab, Simulations4All) exist but lack the Slater $Z_\text{eff}$ display and the physics-derived Hund's-rule term symbol. The student-built simulation in this chapter adds both.

---

## E. Teaching considerations

### This chapter as a capstone

The chapter is explicitly a synthesis PROJECT, not a new-concept chapter. The new material is modest (Hund's Rules 2 and 3, Slater's rules, term symbols) and builds directly on Ch 10. The bulk of the learning is integrative: assemble four concepts from three prior chapters (Pauli, Hund's Rule 1, hydrogenic orbitals, variational screening) into a single coherent model and validate it against real data.

Framing for the student: "You now have all the tools. Let's use them."

### The project rubric (capstone defense)

A student "defends the structure" of their multi-electron atom model by demonstrating they can:
1. Name the approximations: independent electrons, hydrogenic orbital shapes, central-field potential, Slater screening.
2. State what each approximation ignores: electron-electron correlation beyond average-field, relativistic effects (fine structure), configuration mixing.
3. Predict a configuration using the model, compare to NIST, and identify any discrepancy.
4. For a discrepancy (e.g., Cr or Cu), explain the physical mechanism: exchange-energy stabilization of the half-filled or filled d subshell beats the small 3d/4s gap, in a way the Madelung mnemonic does not capture.
5. Describe what the simulation shows: aufbau filling order, energy level diagram with n+ℓ ordering, Hund's-rule filling within subshells.
6. State one quantitative prediction: e.g., Slater $Z_\text{eff}$ for a named orbital of a named element, and compare to the Hartree-Fock $Z_\text{eff}$ from a database.

### Common misconceptions

1. "The aufbau principle is a law of nature." It is an approximate rule derived from the independent-electron approximation and Madelung's semi-empirical ordering. It has ~20 exceptions in the periodic table.
2. "3d fills after 4s because 3d has higher energy, always." The 3d/4s ordering depends on Z and on how many electrons are in the 3d subshell. After the 3d starts filling, the energy comparison changes. In free ions $M^{2+}$, the 3d is lower in energy than 4s, which is why transition metals lose their 4s electrons first when forming dications (e.g., Fe²⁺ is [Ar]3d⁶, not [Ar]3d⁴4s²).
3. "Hund's rule means we always maximize spin first." Hund's rules are applied in sequence (first S, then L, then J), and they assume LS coupling. For heavy elements (Z > ~50), spin-orbit coupling becomes comparable to electron-electron repulsion, LS coupling breaks down, and the rules fail.
4. "The periodic table has exactly 2, 8, 8, 18, 18, 32 elements per period." The counts follow from orbital filling only under the Madelung ordering. The last few periods of the periodic table are less well understood (superheavy elements, relativistic effects).

### Difficulty gradient

- Warm-up: write the electron configuration of Na, Cl, Fe using the aufbau principle. Calculate $Z_\text{eff}$ for the outermost electron of Na using Slater's rules.
- Application: apply Hund's rules to find S, L, J and the term symbol of carbon, oxygen, iron.
- Synthesis (project): build the orbital-filling simulation, predict configurations for Z=1–36, and validate against NIST. Identify and explain the Cr and Cu exceptions.
- Challenge: for the first row transition metals (Z=21–30), plot Slater $Z_\text{eff}$ vs Z for the 3d and 4s electrons and show why the 3d/4s gap varies non-monotonically.

### Simulation specification (basis for the LLM exercise)

A student-built Claude Code project should produce:
- An HTML/D3 visualization (or Python/matplotlib if the student prefers) that accepts an element number Z as input.
- Displays: orbital energy diagram (all subshells up to the filled level, arranged by Madelung n+ℓ ordering); aufbau filling animation (step through electrons, place each in lowest available orbital, enforce Hund's rule within subshells); final configuration in standard notation; Hund's-rule term symbol (at minimum S and $2S+1L$); Slater $Z_\text{eff}$ for the outermost orbital.
- Validation table: compare predicted configuration to NIST ground-state configuration for Z=1–36. Highlight mismatches.
- Suggested CLAUDE.md rules (to be drafted in the chapter): single HTML file; D3 v7; periodic table heatmap option; numeric readouts of $Z_\text{eff}$, configuration, term symbol; flag exceptions to Madelung.

---

## F. Library files relevant to this chapter

- `/pantry/_lib_qmsri-08-identical-particles.md` — the periodic table derivation (§"The periodic table"): three facts (screening-modified energy ordering, Pauli exclusion, Hund's rule) + aufbau principle + Madelung rule + Cr/Cu exceptions. Figures 8.4 (radial probability density comparison, 3s/3p/3d, showing penetration) and 8.5 (aufbau filling diagram for first 18 elements) are directly relevant. The exchange integral as the mechanism for Hund's Rule 1.
- `/pantry/_lib_qmsri-07-the-hydrogen-atom.md` — §"The hidden symmetry": the $\mathfrak{so}(4)$ degeneracy breaking when potential departs from $1/r$; sodium D lines as evidence. §"The full spectrum": hydrogenic orbital formulae for building blocks.
- `/pantry/_lib_qmsri-qm-townsend-notes.md` — §5.7 (The Helium Atom): variational calculation with $Z_\text{eff}$, giving $E_V \approx -77.4$ eV. The prototype Slater screening derivation. §5.6 (Particles with interactions and exchange): exchange integrals and Hund's rule example.
- `/books/physics-quantum-mechanics-sri/pantry/1022201323-...Cohen-Tannoudji-...Fermions-Bosons...txt` — Table of contents: Chapter XIV (Systems of Identical Particles), Complement $A_{XIV}$ (Many-electron atoms, electronic configurations), Complement $B_{XIV}$ (Energy levels of helium, configurations, terms, multiplets). The complement $A_{XIV}$ is directly on-topic for this chapter. OCR quality is partially garbled; use for structural reference only.

### Web sources consulted for this chapter

- Wikipedia, "Aufbau principle" — Madelung rule, exceptions, period structure.
- Wikipedia, "Slater's rules" — shielding constants, empirical derivation, group ordering.
- Wikipedia, "Hund's rules" — all three rules, mechanism, LS coupling regime.
- LibreTexts, §2.6 "Slater's Rules" (Mount Royal University) — worked examples of $Z_\text{eff}$ calculation.
- LibreTexts, §9.7 "Self-Consistent Field Approximation (Hartree-Fock Method)" — SCF procedure, mean-field approximation.
- LibreTexts, §5.17 "Electron Configurations and the Periodic Table" — period lengths from orbital filling.
- John Carlos Baez, Azimuth blog, "The Madelung Rules" (2021) — the open-problem status of the Madelung rule; ~20 exceptions listed.
- J. Chem. Ed. 78 (2001) p. 635 — pedagogical validation of Slater's rules for teaching periodic trends.
- NIST Atomic Spectra Database — canonical source for ground-state configurations and term symbols.
- Simulations4All, Javalab, ExploreLearning Gizmos — existing interactive orbital-filling tools for comparison.

---

## G. Gaps and flags

### Content gaps for the capstone chapter

1. **Slater's rules: worked numerical example needed.** The research gathers the rule structure but no fully worked $Z_\text{eff}$ calculation through the 3d block. The chapter should include at minimum: $Z_\text{eff}$ for the 2p electron of fluorine (Z=9), the 3s electron of sodium (Z=11), and the 3d electron of iron (Z=26), all computed step-by-step with Slater's groups.

2. **Term symbol procedure.** Rules 2 and 3 (maximize L; determine J) require careful exposition beyond Ch 10. The chapter should include a worked procedure: (a) list all distinct microstates for the configuration; (b) find the term with highest S; (c) among those, find highest L; (d) determine J from the half-filling rule. This is standard but takes space. May need a sidebar or appendix.

3. **The 3d/4s crossing in ions.** The statement that Fe²⁺ is [Ar]3d⁶ (not [Ar]3d⁴4s²) is important and testable, but the mechanism (orbital energies shift with occupation number because the effective potential depends on electron density) requires a sentence of explanation that goes slightly beyond the independent-electron model as stated.

4. **Simulation validation data.** The chapter needs either a table (Z=1–36, Madelung prediction vs actual configuration) or a link to the NIST ASD for student validation. Exceptions: Cr (Z=24), Cu (Z=29) are the canonical first-row cases. Full list of exceptions in the 4d block includes Mo, Ru, Rh, Pd, Ag — worth flagging.

5. **Hartree-Fock as the systematic version.** The chapter should name HF as the systematic realization of the approximation being made, describe the self-consistent field iteration in one paragraph, and note that computed HF orbital energies and atomic radii are available in standard tables (e.g., Clementi & Roetti, 1974, for Z=1–54). This tells students where to get validated $Z_\text{eff}$ values to compare against their Slater estimates.

6. **Project rubric.** A formal rubric for the capstone defense needs to be drafted. The structure is outlined in section E above but should be refined to a point-by-point student-facing rubric that can be included in the chapter.

### Flags for the author

- The Madelung rule has no known first-principles derivation as of 2026 (Baez, 2021). This should be stated explicitly in the chapter ("Still puzzling" section analog), in keeping with the intellectual honesty of the series. Do not imply the rule is provable from the Schrödinger equation alone.
- Hund's Rule 3 requires spin-orbit coupling, which is not introduced until a later chapter (perturbation theory / fine structure). The chapter should introduce Rule 3 and flag it as preview material with the derivation deferred. Students can apply it mechanically before understanding the mechanism.
- The Cohen-Tannoudji complement $A_{XIV}$ (multi-electron atoms, electronic configurations) would be the strongest library source for the systematic term-symbol procedure; the file is too garbled to use directly. A clean copy should be sourced.
- The term "exchange force" should be explicitly avoided in the chapter (as in Ch 10): it is a correlation effect, not a force.
- A figure showing energy level ordering vs Z (the "Madelung diagram" — subshell energies as functions of atomic number) is the key visual for this chapter. No such figure is in the current library files. It must be commissioned or generated.
