# Research Notes: Chapter 11 — Capstone: The Atom, Built from Simulations

**Corresponding chapter:** chapters/12-capstone-the-atom.md
**Generated:** 2026-06-03
**Status:** Full chapter written; notes retained and extended from prior research pass.

---

## Chapter summary (capability built)

Students finish this chapter able to: (1) use hydrogenic orbitals as building blocks for multi-electron atoms; (2) apply the aufbau principle, Pauli exclusion, and Hund's rules to predict the ground-state electron configuration of any element through the transition metals; (3) calculate approximate effective nuclear charge using Slater's rules; (4) explain the period structure of the periodic table (period lengths 2, 8, 8, 18, 18, 32) from orbital energy ordering; (5) predict the configuration and term symbol of a specific element (carbon or iron), check against NIST, and defend the approximations made — including the 3d/4s ordering subtlety in transition metals.

This is a PROJECT chapter: the synthesis deliverable is a working D3 simulation of orbital filling that the student builds and validates against known configurations.

---

## A. Conceptual foundations

### Hydrogenic orbitals as building blocks

- In hydrogen, energy $E_n = -13.6\,\text{eV}/n^2$ depends only on $n$: accidental $\mathfrak{so}(4)$ degeneracy of the Coulomb potential. All $n^2$ orbitals at a given $n$ are degenerate.
- In multi-electron atoms, the $\ell$-degeneracy breaks immediately when the potential departs from $1/r$. Low-$\ell$ orbitals penetrate closer to the nucleus (less screened by inner electrons) and fall to lower energy.
- Key result: at any given $n$, $E(ns) < E(np) < E(nd) < E(nf)$.
- Wave function forms remain approximately hydrogenic in shape; energies are shifted. This is the independent-electron (central-field) model.

### Screening and effective nuclear charge (Slater's rules)

$$Z_\text{eff} = Z - \sigma$$

Slater's empirical grouping: [1s] [2s,2p] [3s,3p] [3d] [4s,4p] [4d] [4f] [5s,5p] ...

Shielding constants:
- Electrons to the right contribute 0.
- Same [ns,np] group: 0.35 each (0.30 for 1s).
- For s/p electron: shell $n-1$ contributes 0.85 each; shells $n-2$ and below contribute 1.00 each.
- For d/f electron: all inner shells contribute 1.00.

Worked examples in chapter: fluorine 2p ($Z_\text{eff} = 5.20$), sodium 3s ($Z_\text{eff} = 2.20$), iron 3d ($Z_\text{eff} = 6.25$).

### The Madelung (n+ℓ) rule — HONESTY FLAG

The Madelung rule (fill in order of increasing $n+\ell$; for equal $n+\ell$ fill lower $n$ first) gives the correct filling sequence for ~80% of elements. **No first-principles derivation from the Schrödinger equation exists as of 2026.** The rule is empirical, confirmed computationally but not analytically proved. State this clearly.

Filling sequence: $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, \ldots$

Period lengths from $2(2\ell+1)$:
- Period 1: 1s → 2
- Period 2: 2s+2p → 8
- Period 3: 3s+3p → 8
- Periods 4,5: s+d+p → 18
- Periods 6,7: s+f+d+p → 32

### Madelung exceptions — HONESTY FLAG

Cr (Z=24): [Ar]3d⁵4s¹ (not [Ar]3d⁴4s²) — half-filled 3d exchange stabilization.
Cu (Z=29): [Ar]3d¹⁰4s¹ (not [Ar]3d⁹4s²) — filled 3d exchange stabilization.
4d-block: Mo, Ru, Rh, Pd, Ag also show exceptions.
Mechanism: exchange-energy gain from half-/fully-filled subshell exceeds 3d/4s gap energy.

### Hund's rules

**Rule 1 (maximize S):** Highest total spin S → lowest energy. Mechanism: exchange integral (derived Ch 11). Term with highest $2S+1$ is lowest.

**Rule 2 (maximize L given S):** Among same-S terms, highest L → lowest energy. Electrons orbiting in the same sense avoid each other → lower Coulomb repulsion.

**Rule 3 (J from L and S) — PREVIEW FLAG:** Less-than-half-filled: $J = |L-S|$. More-than-half-filled: $J = L+S$. Exactly half-filled: $J = S$ (since $L = 0$). Mechanism: spin-orbit coupling $\hat{H}_{so} \sim \lambda\vec{L}\cdot\vec{S}$. Full derivation deferred to Volume 3 (perturbation theory + fine structure). Apply mechanically here.

### The 3d/4s ordering subtlety (rubric point)

Madelung predicts 4s fills before 3d (n+ℓ: 4s→4, 3d→5). But once 3d starts filling, orbital energies shift with occupation because the self-consistent potential depends on electron density. In transition metal cations (Fe²⁺, Mn²⁺), the 3d sits lower than 4s, so ionization removes 4s electrons first. Fe²⁺ = [Ar]3d⁶, not [Ar]3d⁴4s².

---

## B. Worked examples

### Carbon (Z=6): ³P₀

Config: 1s² 2s² 2p²
Hund 1: S=1 (two parallel spins in 2p)
Hund 2: L=1 (maximize $M_L$: use $m_\ell=+1$ and $m_\ell=0$, total L=1; or by term enumeration, ³P is the highest-spin term with L=1)
Hund 3: less-than-half-filled → J=|L-S|=|1-1|=0
Term: ³P₀

### Iron (Z=26): ⁵D₄

Config: [Ar] 3d⁶ 4s²
3d⁶: five orbitals, fill all singly (S=5/2) then one more pairs → S=2
Hund 2: maximize $M_L = 2+1+0-1-2+2 = 2$ → L=2 (D term)
Hund 3: more-than-half-filled (6/10) → J=L+S=4
Term: ⁵D₄ ✓ (NIST confirmed)

### Slater Z_eff calculations

Fluorine (Z=9, config 1s²2s²2p⁵): for a 2p electron:
- σ = 2×0.35 (same 2p partners) + 2×0.85 (1s electrons) = ... full calculation in chapter

Sodium (Z=11, config 1s²2s²2p⁶3s¹): for the 3s electron:
- σ = 8×0.85 + 2×1.00 = 8.80 → Z_eff = 11-8.80 = 2.20

Iron (Z=26, config [Ar]3d⁶4s²): for a 3d electron:
- σ = 5×0.35 (other 3d) + 18×1.00 (all inside) = 1.75+18 = 19.75 → Z_eff = 6.25

---

## C. Connections and dependencies

- Ch 10/11 (Identical Particles): Slater determinant, Pauli exclusion, exchange integral, Hund's Rule 1.
- Ch 10 (Hydrogen atom): hydrogenic orbital forms, so(4) degeneracy breaking by screening.
- Ch 9 (Variational principle): helium variational Z_eff = 27/16 is the prototype Slater screening.
- Future (Vol. 3): perturbation theory → spin-orbit coupling → Hund's Rule 3, fine structure, LS coupling vs jj coupling.
- Chemistry: bond formation, Lewis structures, hybridization all rest on valence configurations derived here.

---

## D. Sources

- Wikipedia, "Aufbau principle" [verify]
- Wikipedia, "Slater's rules" [verify]
- Wikipedia, "Hund's rules" [verify]
- LibreTexts §2.6 "Slater's Rules" (Mount Royal University) [verify]
- LibreTexts §5.17 "Electron Configurations and the Periodic Table" [verify]
- J. Chem. Ed. 78 (2001) p. 635, "Screening Percentages Based on Slater Effective Nuclear Charge" [verify]
- John Carlos Baez, Azimuth blog, "The Madelung Rules" (2021) [verify]
- NIST Atomic Spectra Database, https://physics.nist.gov/asd
- Griffiths, Introduction to Quantum Mechanics (3rd ed.), Chapter 5 — identical particles, periodic table
- Townsend, A Modern Approach to Quantum Mechanics (2nd ed.), §5.7 helium variational calculation
- Slater, J.C. (1930). Atomic shielding constants. Phys. Rev. 36, 57–64. [verify]
- Clementi, E. & Roetti, C. (1974). Roothaan-Hartree-Fock atomic wavefunctions. Atomic Data Nuclear Data Tables 14, 177. [verify]

---

## E. Flags for author / "Still puzzling" entries

1. **Madelung rule**: no first-principles derivation; empirical; ~20 exceptions. State clearly.
2. **Hund's Rule 3**: requires spin-orbit coupling → Volume 3. Apply mechanically.
3. **3d/4s crossover in ions**: important subtlety for transition metal chemistry; the independent-electron model does not resolve the level ordering unambiguously when the occupations change.
4. **Exchange "force"**: must not be called a force. It is a correlation effect in the Coulomb energy.
5. **LS coupling breakdown**: for Z > ~50, spin-orbit coupling competes with e-e repulsion; jj coupling scheme more appropriate. Hund's rules technically apply only in the LS limit.
