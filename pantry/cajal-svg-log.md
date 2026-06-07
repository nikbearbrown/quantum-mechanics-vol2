## Run: 2026-06-06

# CAJAL SVG Generation Log — Part 1
Generated: 2026-06-06  
Chapters: 01–06 · Book: quantum-mechanics-vol2

---

## Summary

| Metric | Count |
|---|---|
| Total figures parsed | 28 |
| Generated (new SVGs) | 18 |
| Skipped (collision — file exists) | 10 |

---

## Chapter 01 — The Formalism: Hilbert Space, Dirac Notation, and Operators

| File | Figure title | Type | Status |
|---|---|---|---|
| 01-the-formalism-fig-01.svg | State vs. Its Representations (Three-Basis Fan) | diagram | GENERATED |
| 01-the-formalism-fig-02.svg | Completeness Insertion Mechanism (Three-Step Chain) | diagram | GENERATED |
| 01-the-formalism-fig-03.svg | Operator vs. Matrix: Same Operator, Two Bases | diagram | GENERATED |
| 01-the-formalism-fig-04.svg | Energy-Basis Probability Bar Chart (Worked Example Coefficients) | chart | GENERATED |

Generated: 4 · Skipped: 0

---

## Chapter 02 — Observables, Hermiticity, and the Spectral Theorem

| File | Figure title | Type | Status |
|---|---|---|---|
| 02-observables-and-the-spectral-theorem-fig-01.svg | Spectral Decomposition: Operator as Weighted Sum of Projectors | diagram | SKIPPED (02-observables-and-the-spectral-theorem-fig-01.png exists) |
| 02-observables-and-the-spectral-theorem-fig-02.svg | Born Rule as Geometric Projection | diagram | GENERATED |
| 02-observables-and-the-spectral-theorem-fig-03.svg | Hermitian Matrix Structure: Diagonal Real, Off-Diagonal Conjugate Pairs | diagram | GENERATED |
| 02-observables-and-the-spectral-theorem-fig-04.svg | Real vs. Complex Eigenvalues: Effect of Hermiticity | chart | GENERATED |

Generated: 3 · Skipped: 1

---

## Chapter 03 — Commutators, Compatibility, and the Generalized Uncertainty Principle

| File | Figure title | Type | Status |
|---|---|---|---|
| 03-commutators-and-uncertainty-fig-01.svg | Canonical Commutation Derivation: Product-Rule Mechanism | diagram | SKIPPED (03-commutators-and-uncertainty-fig-01.png exists) |
| 03-commutators-and-uncertainty-fig-02.svg | Robertson Proof: Four-Step Chain (Cauchy-Schwarz to Uncertainty Bound) | diagram | SKIPPED (03-commutators-and-uncertainty-fig-02.png exists) |
| 03-commutators-and-uncertainty-fig-03.svg | Robertson Bound on the Bloch Sphere: State-Dependence of the Bound | diagram | SKIPPED (03-commutators-and-uncertainty-fig-03.png exists) |
| 03-commutators-and-uncertainty-fig-04.svg | Compatible vs. Incompatible Observables: Shared Eigenbasis or Not | diagram | GENERATED |

Generated: 1 · Skipped: 3

---

## Chapter 04 — Quantum Dynamics: Time Evolution and the Pictures

| File | Figure title | Type | Status |
|---|---|---|---|
| 04-quantum-dynamics-and-the-pictures-fig-01.svg | Time-Evolution Operator: Infinitesimal Step to Finite Unitary | diagram | GENERATED |
| 04-quantum-dynamics-and-the-pictures-fig-02.svg | Schrödinger vs. Heisenberg Picture: Parallel Structure Diagram | diagram | GENERATED |
| 04-quantum-dynamics-and-the-pictures-fig-03.svg | Rabi Oscillation: Probability vs. Time for a Two-Level System | chart | GENERATED |
| 04-quantum-dynamics-and-the-pictures-fig-04.svg | Heisenberg Equation vs. Hamilton's Equations: Structural Analogy | diagram | GENERATED |
| 04-quantum-dynamics-and-the-pictures-fig-05.svg | Ehrenfest's Theorem: Narrow vs. Wide Wavepacket in Anharmonic Potential | diagram | GENERATED |

Generated: 5 · Skipped: 0

---

## Chapter 05 — Quantum Mechanics in Three Dimensions

| File | Figure title | Type | Status |
|---|---|---|---|
| 05-quantum-mechanics-in-three-dimensions-fig-01.svg | Central Potential: Separation of Variables Flow | diagram | SKIPPED (05-quantum-mechanics-in-three-dimensions-fig-01.png exists) |
| 05-quantum-mechanics-in-three-dimensions-fig-02.svg | Spherical Harmonics Gallery: First Four Angular Probability Densities | diagram | SKIPPED (05-quantum-mechanics-in-three-dimensions-fig-02.png and .svg exist) |
| 05-quantum-mechanics-in-three-dimensions-fig-03.svg | Physics Basis vs. Chemistry Basis for ℓ=1 | diagram | SKIPPED (05-quantum-mechanics-in-three-dimensions-fig-03.png and .svg exist) |
| 05-quantum-mechanics-in-three-dimensions-fig-04.svg | Effective Potential and the Centrifugal Barrier | chart | GENERATED |
| 05-quantum-mechanics-in-three-dimensions-fig-05.svg | Angular Momentum Cone: L_z vs. |L| for ℓ=1, m=1 | diagram | GENERATED |
| 05-quantum-mechanics-in-three-dimensions-fig-06.svg | Nuclear Shell Model Level Ordering from Spherical Well | chart | GENERATED |

Generated: 3 · Skipped: 3

---

## Chapter 06 — Angular Momentum

| File | Figure title | Type | Status |
|---|---|---|---|
| 06-angular-momentum-fig-01.svg | The Angular Momentum Ladder: Spectrum Derivation by Non-Negativity and Termination | diagram | SKIPPED (06-angular-momentum-fig-01.png exists) |
| 06-angular-momentum-fig-02.svg | Spectrum Derivation: Non-Negativity Bound and Termination Conditions | diagram | SKIPPED (06-angular-momentum-fig-02.png exists) |
| 06-angular-momentum-fig-03.svg | Integer vs. Half-Integer ℓ: Single-Valuedness Constraint | diagram | SKIPPED (06-angular-momentum-fig-03.png and .svg exist) |
| 06-angular-momentum-fig-04.svg | ℓ=1 Matrix Representations of L_z, L₊, L₋ | diagram | GENERATED |
| 06-angular-momentum-fig-05.svg | Robertson Uncertainty Bound: Transverse Components and Saturation | chart | GENERATED |

Generated: 2 · Skipped: 3

---

## Generation notes

- Rabi oscillation curves (ch04-fig-03): computed with Python — P↑(t)=cos²(ω₀t/2), P↓(t)=sin²(ω₀t/2), 101 points over [0, 2π/ω₀].
- Effective potential (ch05-fig-04): V(r)=−1/r, centrifugal=1/r² (ℓ=1 units), V_eff=sum. Minimum confirmed at r=2, V_eff=−0.25.
- Ehrenfest double-well (ch04-fig-05): V(x)=−x²+0.25x⁴. Minima at x=±√2, V=−1. 121 points per curve.
- Ladder coefficients (ch06-fig-04): nonzero elements are ħ√2 = ħ√(ℓ∓m)(ℓ±m+1) for ℓ=1, m=0→±1. Correct.
- Nuclear shell model (ch05-fig-06): degeneracy 2(2ℓ+1); magic numbers 2, 8, 20 confirmed by cumulation.
- All SVGs: viewBox="0 0 700 420", no width/height attrs, Brutalist palette, fully labeled.
- Collision check performed with bash ls before all writes.
# CAJAL SVG Log — Part 2
Generated: 2026-06-06
Chapters processed: 07, 08, 09, 10, 11
Generator: static SVG (Brutalist palette, Northeastern brand)

---

## Chapter 07 — Spin and the Bloch Sphere

| File | Figure title | Type | Status |
|------|-------------|------|--------|
| 07-spin-and-the-bloch-sphere-fig-01.svg | Bloch Sphere: State Parametrization and Born-Rule Geometry | diagram | GENERATED |
| 07-spin-and-the-bloch-sphere-fig-02.svg | Sequential Stern–Gerlach Experiment: Three-Stage Noncommutativity | diagram | GENERATED |
| 07-spin-and-the-bloch-sphere-fig-03.svg | Larmor Precession: Bloch Vector Tracing a Latitude Circle | diagram | GENERATED |
| 07-spin-and-the-bloch-sphere-fig-04.svg | Stern–Gerlach Outcome: Two Spots vs. Classical Smear | diagram | GENERATED |
| 07-spin-and-the-bloch-sphere-fig-05.svg | Larmor Frequency vs. Field Strength: Proton MRI Operating Points | chart | GENERATED |

Parsed: 5 · Generated: 5 · Skipped: 0

---

## Chapter 08 — Addition of Angular Momenta

| File | Figure title | Type | Status |
|------|-------------|------|--------|
| 08-addition-of-angular-momenta-fig-01.svg | Two-Basis Decomposition: Uncoupled to Coupled Basis for ½⊗½ | diagram | SKIPPED (already exists as .png) |
| 08-addition-of-angular-momenta-fig-02.svg | Triangle Rule and State Counting: Three Representative Combinations | chart | GENERATED |
| 08-addition-of-angular-momenta-fig-03.svg | Ladder Operator Algorithm: Building |1,0⟩ from |1,1⟩ | diagram | GENERATED |
| 08-addition-of-angular-momenta-fig-04.svg | Spin–Orbit Energy Splitting: Coupled Basis Diagonalizes Ĥ_so | diagram | GENERATED |

Parsed: 4 · Generated: 3 · Skipped: 1

---

## Chapter 09 — The Hydrogen Atom

| File | Figure title | Type | Status |
|------|-------------|------|--------|
| 09-the-hydrogen-atom-fig-01.svg | Radial Probability Density P(r) for the 1s State: Two Radii Compared | chart | SKIPPED (already exists as .png + .svg) |
| 09-the-hydrogen-atom-fig-02.svg | Effective Potential V_eff(r): Coulomb Well vs. Centrifugal Barrier | chart | SKIPPED (already exists as .png + .svg) |
| 09-the-hydrogen-atom-fig-03.svg | Hydrogen Energy Level Diagram with Spectral Series and Selection Rules | diagram | SKIPPED (already exists as .png) |
| 09-the-hydrogen-atom-fig-04.svg | Orbital Shape Gallery: 2D Cross-Sections |ψ_{nℓm}|² for n=1,2,3 | diagram | SKIPPED (already exists as .png + .svg) |
| 09-the-hydrogen-atom-fig-05.svg | Shell State Counting: 2n² Degeneracy and Periodic Table Row Lengths | chart | GENERATED |

Parsed: 5 · Generated: 1 · Skipped: 4

---

## Chapter 10 — Identical Particles

| File | Figure title | Type | Status |
|------|-------------|------|--------|
| 10-identical-particles-fig-01.svg | Boson/Fermion Statistics Classification by Constituent Fermion Count | diagram | GENERATED |
| 10-identical-particles-fig-02.svg | Slater Determinant: Swapping Rows Flips the Sign | diagram | GENERATED |
| 10-identical-particles-fig-03.svg | N×N Slater Determinant Structure | diagram | GENERATED |
| 10-identical-particles-fig-04.svg | Helium Para/Ortho Energy Splitting: J and K Integrals | diagram | GENERATED |
| 10-identical-particles-fig-05.svg | Mechanism: Spatial Symmetry → Electron Avoidance → Lower Coulomb Energy | diagram | GENERATED |
| 10-identical-particles-fig-06.svg | Joint Probability Density: Boson vs. Fermion vs. Distinguishable | diagram | GENERATED |

Parsed: 6 · Generated: 6 · Skipped: 0

---

## Chapter 11 — Capstone: The Atom

| File | Figure title | Type | Status |
|------|-------------|------|--------|
| 11-capstone-the-atom-fig-01.svg | Orbital Penetration and Energy Ordering: ℓ-Degeneracy Breaking | diagram | SKIPPED (already exists as .png) |
| 11-capstone-the-atom-fig-02.svg | Slater's Rules Grouping and Shielding Constants | diagram | SKIPPED (already exists as .png) |
| 11-capstone-the-atom-fig-03.svg | Madelung Filling Sequence and Period Length Derivation | diagram | GENERATED |
| 11-capstone-the-atom-fig-04.svg | Hund's Three Rules: Mechanism and Hierarchy | diagram | GENERATED |
| 11-capstone-the-atom-fig-05.svg | Madelung Exceptions: Cr and Cu Exchange Stabilization | diagram | GENERATED |
| 11-capstone-the-atom-fig-06.svg | 3d/4s Orbital Energy Crossing as a Function of Nuclear Charge Z | chart | GENERATED |

Parsed: 6 · Generated: 4 · Skipped: 2

---

## Summary

| Chapter | Parsed | Generated | Skipped |
|---------|--------|-----------|---------|
| 07 — Spin and the Bloch Sphere | 5 | 5 | 0 |
| 08 — Addition of Angular Momenta | 4 | 3 | 1 |
| 09 — The Hydrogen Atom | 5 | 1 | 4 |
| 10 — Identical Particles | 6 | 6 | 0 |
| 11 — Capstone: The Atom | 6 | 4 | 2 |
| **Total** | **26** | **19** | **7** |

All generated figures are static SVG with:
- viewBox="0 0 700 420" (no width/height attrs)
- Brutalist palette: canvas #FFFFFF, ink #2a1a0e, accent #C8102E, grays #787878/#ADADAD
- Typography: EB Garamond titles, Inter body, JetBrains Mono ticks
- ARIA role="img", aria-labelledby, <title>, <desc> (≤280 chars), <metadata> cajal:figure block
- rx="0", no gradients, no shadows, no rounded corners
- Quantitative charts: y-axis zero-anchored where applicable
- Physics accuracy: correct Madelung sequence, correct half-filled/filled subshell counts,
  correct 2×2 Slater determinant, correct Larmor frequency data (f_L = 42.58 MHz/T × B₀),
  correct 3d/4s crossing Z≈22, correct para/ortho helium energy ordering

## Summary
SVGs in images/: 43 · PNGs: 54
PNG conversion: completed, 0 errors (12 collision-violating SVGs removed before conversion; 11 SVGs repaired for XML validity)
