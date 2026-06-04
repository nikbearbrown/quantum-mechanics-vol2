# Research Notes: Chapter 09 — The Hydrogen Atom
**Corresponding chapter:** chapters/09-the-hydrogen-atom.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: reduce the two-body hydrogen problem to a one-body problem using center-of-mass coordinates; separate the Schrödinger equation in spherical coordinates into angular (spherical harmonics from Ch. 5) and radial parts; solve the ground-state radial equation by ansatz and extract the Bohr radius a₀ and ground-state energy E₁ = −13.6 eV; enumerate the quantum numbers (n, ℓ, m) and their constraints; count the n² orbital degeneracy per shell (and 2n² including spin from Ch. 7); compute the radial probability density P(r) = r²|R_{nℓ}(r)|² and find the most-probable and mean radii for the 1s state; and qualitatively describe orbital shapes for low (n,ℓ,m). The worked example is the ground-state 1s state: P(r), r_mp = a₀, ⟨r⟩ = 3a₀/2, and why they differ.

---

## A. Conceptual foundations

**Historical hook.** Balmer (1885) published a formula fitting four visible hydrogen lines with no theory: λ = B·n²/(n²−4), n = 3,4,5,6, B ≈ 364.5 nm. The fit was exact to measurement precision — not approximate. Rydberg generalized it to 1/λ = R_H(1/n_f² − 1/n_i²). Nobody knew why for 28 years. Bohr (1913) derived E_n = −13.6 eV/n² from quantized circular orbits — right numbers, wrong model (no wave functions, no angular momentum substructure, no selection rules, L = nℏ always when Schrödinger says L = ℓℏ with ℓ ≤ n−1). Schrödinger (Christmas 1925, Arosa resort) derived the same energies from the wave equation, and also obtained the complete wave functions ψ_{nℓm}(r,θ,φ) — a richer structure Bohr could not access.

**Two-body reduction.** The hydrogen atom is a proton (mass m_p) and electron (mass m_e) interacting via V = −e²/(4πε₀r). Introducing center-of-mass coordinate R⃗ = (m_p r⃗_p + m_e r⃗_e)/(m_p+m_e) and relative coordinate r⃗ = r⃗_e − r⃗_p, the Hamiltonian separates exactly:
  Ĥ = Ĥ_CM + Ĥ_rel
where Ĥ_CM = P̂²/(2M) (free particle, M = m_p + m_e, uninteresting) and:
  Ĥ_rel = p̂²/(2μ) − e²/(4πε₀r)
with reduced mass μ = m_p m_e/(m_p + m_e) ≈ m_e(1 − m_e/m_p) ≈ m_e(1 − 1/1836).

The isotope shift: deuterium (heavier nucleus) has different μ, hence different a₀ and E_n. Urey discovered deuterium (1932) by finding a faint second copy of each Balmer line, shifted by ~1.79 Å at H_α (656 nm) — directly measuring the reduced mass difference. The isotope shift is real and detectable.

**Spherical symmetry — separation of variables.** The potential V = V(r) is spherically symmetric. Write ψ(r,θ,φ) = R(r) Y_ℓ^m(θ,φ). The angular part Y_ℓ^m is universal (Chapter 5 result, independent of the specific V(r)). The radial part depends on the potential.

**The radial equation.** Substituting u(r) = rR(r) and simplifying:
  −(ℏ²/2μ) d²u/dr² + V_eff(r) u(r) = E u(r)
where the effective potential is:
  V_eff(r) = −e²/(4πε₀r) + ℏ²ℓ(ℓ+1)/(2μr²)
The first term is the Coulomb well (attractive). The second is the centrifugal barrier (repulsive, diverges as r→0). For ℓ=0, the centrifugal barrier vanishes and ψ can be non-zero at the nucleus — relevant for hyperfine spectroscopy. For ℓ≥1, the barrier pushes the probability density away from the origin.

Boundary conditions: u(0) = 0 (so R = u/r stays finite); u(r)→0 as r→∞ (normalizability). These two requirements together quantize the energy.

**The ground state — full calculation by ansatz.** Set ℓ=0. Try u(r) = Ar·e^{−r/a} with unknown a. Substitute into the radial equation; collect constant and linear terms in r:
- Constant: ℏ²/(μa) = e²/(4πε₀) → a = a₀ = 4πε₀ℏ²/(μe²) ≈ 0.529 Å (the Bohr radius falls out)
- Linear in r: E = −ℏ²/(2μa₀²) = −μe⁴/[2(4πε₀)²ℏ²] ≈ −13.6 eV

Normalization gives A = 2/a₀^{3/2}, so:
  ψ_{100}(r) = (πa₀³)^{-1/2} e^{−r/a₀}
Spherically symmetric, no preferred direction, maximum density at r=0, exponential decay in all directions.

**The general solution — associated Laguerre polynomials.** For general (n,ℓ), the Frobenius series expansion gives:
  R_{nℓ}(r) = N_{nℓ} · (r/a₀)^ℓ · e^{−r/(na₀)} · L^{2ℓ+1}_{n−ℓ−1}(2r/(na₀))
where N_{nℓ} is a normalization constant and L^{2ℓ+1}_{n−ℓ−1} is an associated Laguerre polynomial of degree n−ℓ−1. The series terminates (necessary for normalizability) only when n−ℓ−1 ≥ 0, i.e., ℓ ≤ n−1.

**Energy spectrum.** The energies depend only on n:
  E_n = −13.6 eV / n², n = 1, 2, 3, ...
This Coulomb degeneracy — that energy does not depend on ℓ — is not generic. It follows from the extra conserved quantity: the quantum Runge–Lenz vector (classically: Kepler orbits do not precess). The six operators {L̂_x, L̂_y, L̂_z, M̂_x, M̂_y, M̂_z} close on the algebra 𝔰𝔬(4) — rotations in four dimensions. Pauli solved hydrogen algebraically using this algebra in 1926, before Schrödinger published the wave-mechanical solution.

When the potential departs from 1/r (e.g., sodium, where inner electrons screen the nucleus), 𝔰𝔬(4) breaks and ℓ-degeneracy splits. The bright sodium D lines at 589 nm are the 3p→3s transition, existing precisely because the effective potential is not Coulomb.

**Quantum number constraints — origins:**
- n ≥ 1: Frobenius series terminates only for positive integer n
- ℓ ≤ n−1 (i.e., ℓ = 0,...,n−1): Laguerre polynomial degree = n−ℓ−1 must be ≥ 0
- |m| ≤ ℓ: angular momentum algebra from Chapter 5 (unchanged)

**Degeneracy counting.** For each n:
  Σ_{ℓ=0}^{n−1} (2ℓ+1) = n² orbital states
Including spin m_s = ±½ from Chapter 7: 2n² states per shell.
  n=1 → 2 states (K shell), n=2 → 8 (L shell), n=3 → 18 (M shell), n=4 → 32 (N shell)
These are the row lengths of the periodic table. Not numerology — a structural consequence of the quantum numbers derived across Chapters 5, 7, and 9.

**Node-counting rule.** Total number of nodes in ψ_{nℓm} = n−1, partitioned into (n−ℓ−1) radial nodes and ℓ angular nodes. Examples:
- 1s: 0 radial + 0 angular = 0 total
- 2s: 1 radial + 0 angular = 1 total
- 2p: 0 radial + 1 angular = 1 total
- 3d: 0 radial + 2 angular = 2 total

**Two radii and why they differ.** The radial probability density (probability per unit radial distance, integrating over all angles) is:
  P(r) = r²|R_{nℓ}(r)|²
For the 1s state: P(r) = (4/a₀³) r² e^{−2r/a₀}

Most-probable radius (peak of P): dP/dr = 0 → r_mp = a₀.
Mean radius: ⟨r⟩ = ∫r·P(r)dr = (4/a₀³) ∫₀^∞ r³ e^{−2r/a₀}dr = (4/a₀³)·(3!/(2/a₀)⁴) = 3a₀/2.

r_mp = a₀ ≠ ⟨r⟩ = 3a₀/2. They differ because P(r) is right-skewed — the long tail at large r pulls the mean above the peak. A classical orbit at fixed radius would have r_mp = ⟨r⟩. The inequality is direct evidence that we have a probability distribution, not a trajectory. Bohr placed the electron at r = a₀; Schrödinger says the peak is at a₀ but the mean is elsewhere.

General formula: ⟨r⟩_{nℓ} = (a₀/2)[3n² − ℓ(ℓ+1)]. For (1,0): 3a₀/2 ✓. For (2,0): 6a₀. For (2,1): 5a₀.

**Complex vs. real orbitals.** The m = ±1 states (e.g., ψ_{21,+1} and ψ_{21,−1}) are eigenstates of L̂_z with definite angular momentum but azimuthal symmetry in the xz cross-section. The chemistry textbook p_x, p_y are real linear combinations:
  p_x ∝ ψ_{21,−1} − ψ_{21,+1} ∝ sinθ cosφ
  p_y ∝ i(ψ_{21,−1} + ψ_{21,+1}) ∝ sinθ sinφ
These have the dumbbell shape pointing along Cartesian axes — convenient for bonding — but are not eigenstates of L̂_z. Both bases span the same space. Choice of basis = choice of what to make obvious.

**Electric-dipole selection rules.** A photon carries angular momentum 1. Conservation during emission requires:
  Δℓ = ±1, Δm = 0, ±1
The 2s→1s transition (Δℓ=0) is electric-dipole forbidden. It occurs via two-photon emission with lifetime ≈ 0.12 s — eight orders of magnitude slower than allowed transitions (nanosecond lifetimes). The 1S–2S two-photon transition has been measured to 15 significant figures using optical frequency combs; the ALPHA collaboration at CERN measured the same transition in antihydrogen, testing CPT symmetry at parts-per-trillion precision.

**Three misconceptions to refute explicitly:**
1. The orbital is not a path. The 90% probability isosurface is not a containing wall; the electron is found outside it 10% of the time. r_mp ≠ ⟨r⟩ is the direct evidence.
2. The Bohr model is not essentially correct. It gets E_n right because of 𝔰𝔬(4) symmetry and the coincidence that Bohr's L=nℏ counts the right quantum number for circular orbits. But Bohr has L=nℏ always (ℓ=n always), while Schrödinger says ℓ=0,...,n−1.
3. |ψ|² is not a continuous charge distribution. It is the probability density for finding the electron at a point on a position measurement.

---

## B. Domain examples and cases

**Spectral series.**
- Lyman: n_i→1, UV (Lyman α at 121.6 nm: n=2→1)
- Balmer: n_i→2, visible (H_α at 656.3 nm: n=3→2; the first spectroscopic series discovered)
- Paschen: n_i→3, near-IR
- Brackett: n_i→4, IR
The Balmer α calculation: ΔE = 13.6×(1/4−1/9) = 1.889 eV → λ = hc/ΔE = 1240 eV·nm/1.889 = 656.3 nm. Experimental: 656.281 nm. Agreement to 0.003%.

**Isotope shift and deuterium discovery.** Urey (1932) detected deuterium as a faint shoulder on the Balmer lines. The 1.79 Å shift at H_α arises from the reduced mass difference between H (μ_H) and D (μ_D). This was the first isotope discovered by spectroscopy rather than mass measurement.

**Muonic hydrogen.** Replace electron with muon (m_μ ≈ 207 m_e). Reduced mass ≈ 186 m_e. Bohr radius shrinks by factor 186 to a₀_μ ≈ 0.00285 Å; ground-state energy grows by factor 186 to E₁_μ ≈ −2529 eV. The muon is very close to the nucleus, making muonic hydrogen sensitive to the proton's charge radius. The proton radius puzzle (discrepancy between muonic hydrogen spectroscopy and electron scattering measurements, ~2010–2020) attracted widespread attention; recent measurements have largely resolved the discrepancy.

**Sodium D lines.** The 3p→3s transitions of sodium (589.0 nm and 589.6 nm) exist because the effective potential in sodium is not 1/r (ten inner electrons screen the nucleus), breaking 𝔰𝔬(4) degeneracy and splitting 3s below 3p. The doublet structure (589.0 vs. 589.6 nm) is from spin-orbit splitting within the 3p subshell (J=3/2 and J=1/2 sub-levels of ²P).

**The metastable 2s state.** Lifetime ≈ 0.12 s (two-photon decay). Compare to allowed-transition lifetimes of ~1 ns. The eight-order-of-magnitude difference makes 2s states of H and H-like ions useful for precision spectroscopy. Lamb shift measurements (which demonstrated QED corrections to hydrogen energy levels) used the 2s metastability.

**Antihydrogen spectroscopy (ALPHA at CERN).** Measurement of the 1S–2S two-photon transition in antihydrogen, agreeing with ordinary hydrogen at parts-per-trillion precision. A direct CPT symmetry test using spectral lines that Balmer catalogued in 1885.

---

## C. Connections and dependencies

**Prerequisites:**
- Ch 5 (3D quantum mechanics, spherical harmonics): The angular part Y_ℓ^m is taken unchanged from Ch. 5; the hydrogen chapter contributes only the radial equation. Students must know the spherical harmonic eigenvalue equations and the ladder operator spectrum.
- Ch 7 (Spin): The factor of 2 in 2n² degeneracy comes from m_s = ±½. Without Ch. 7, the degeneracy count gives n² not 2n².
- Ch 8 (Addition of angular momenta): The coupled-basis (n, ℓ, J, M_J) needed for fine structure — not required for this chapter, but the bridge forward should be explicit.

**Feeds into:**
- Vol. 3 (Perturbation theory + fine structure): The gross hydrogen spectrum is the unperturbed Hamiltonian H₀. Perturbations include spin-orbit coupling (H_so = λL⃗·S⃗), the Darwin term (relativistic correction at origin), and the kinetic energy relativistic correction. Together they lift most of the n² orbital degeneracy.
- Vol. 3 (Hyperfine structure): The 21-cm hydrogen line from the hyperfine coupling Ŝ_e·Ŝ_p requires the ½⊗½ singlet/triplet decomposition from Ch. 8 and the fact that ψ_{100} is non-zero at the nucleus.
- Vol. 3 (Zeeman effect): Magnetic field lifts m degeneracy; requires both the hydrogen wave functions and the angular momentum formalism from Chs. 5, 7, 8.
- Vol. 3 (Helium and multi-electron atoms): H provides the single-electron starting point; helium introduces electron-electron repulsion.
- Chemistry (periodic table): The shell structure 2n² directly gives the periodic table row lengths. Hydrogen is the prototype atom from which all of atomic physics is built.

---

## D. Current state of the field

The hydrogen 1S–2S transition is one of the most precisely measured frequencies in physics (measured to 15 significant figures with optical frequency combs). The Rydberg constant is currently determined primarily from hydrogen spectroscopy. The proton charge radius — extracted from both electron and muonic hydrogen spectroscopy — attracted major attention (the "proton radius puzzle") and was largely resolved around 2019–2022 by improved measurements.

The exact analytic solvability of hydrogen (via 𝔰𝔬(4) symmetry) remains a pedagogically important example of accidental degeneracy lifted by symmetry breaking, and continues to appear in formal treatments of quantum field theory (where the hydrogen problem maps onto certain quantum field theory calculations via dimensional regularization). Antihydrogen spectroscopy at CERN tests the CPT theorem at steadily increasing precision.

---

## E. Teaching considerations

**The r²-Jacobian trap.** The single most common error in this chapter: plotting |R_{nℓ}(r)|² instead of P(r) = r²|R_{nℓ}(r)|². The former peaks at r=0 for all s-states; the latter peaks at r_mp = a₀ for the 1s state. Students must see both plotted side-by-side and be asked "which one gives the probability of finding the electron between r and r+dr?"

**r_mp ≠ ⟨r⟩ as the conceptual centerpiece.** This is the chapter's most important single insight: a probability distribution has a peak and a mean that need not coincide. Present this as evidence against the path picture, not just as a calculation. A classical orbit at fixed radius gives r_mp = ⟨r⟩ exactly; the fact that they differ for ψ_{100} is fingerprint evidence of wave mechanics.

**The separation of variables pays off.** Students who struggled with the abstract machinery of Chapter 5 (spherical harmonics) should see the payoff here: all the angular complexity is handled by the Y_ℓ^m already worked out, and the hydrogen chapter contributes only the radial equation. The separation works because V = V(r) — emphasize this.

**Degeneracy structure is pedagogically important.** The fact that 2s and 2p are degenerate (same energy, very different shapes) is strange and requires explanation. The 𝔰𝔬(4) argument (Runge–Lenz vector) is the honest answer; a brief mention at the student's level ("a special extra symmetry of the 1/r potential that doesn't exist for any other power law") is sufficient for this chapter.

**The Bohr model should be buried here, not before.** Students arrive believing Bohr is approximately right. The chapter's job is to be specific: Bohr gets E_n right for one reason only (a numerical coincidence involving 𝔰𝔬(4) symmetry), and is wrong about almost everything else. The 2s state (ℓ=0, no angular momentum) has no Bohr orbit — it is forbidden in Bohr's model yet perfectly legal and experimentally accessible in Schrödinger's.

**Worked example for the chapter (as specified):** The 1s state.
  (a) Write ψ_{100}(r) = (πa₀³)^{-1/2} e^{-r/a₀}.
  (b) Compute P(r) = r²|R_{10}(r)|² = (4/a₀³) r² e^{-2r/a₀}. Plot schematically: rises from 0, peaks at r_mp, long tail.
  (c) Find r_mp by setting dP/dr = 0: d/dr [r²e^{-2r/a₀}] = 0 → (2r − 2r²/a₀)e^{-2r/a₀} = 0 → r_mp = a₀.
  (d) Compute ⟨r⟩ = (4/a₀³) ∫₀^∞ r³ e^{-2r/a₀} dr = (4/a₀³)·(6a₀⁴/16) = 3a₀/2.
  (e) State the interpretation: r_mp = a₀ is where the probability density is largest; ⟨r⟩ = 3a₀/2 is the average of a measurement over many repeated trials. They differ because P(r) is skewed. A Bohr orbit at a₀ would have both quantities equal.

**LLM exercise (from library file):** Build the hydrogen orbital visualizer — 2D heat map of |ψ_{nℓm}(x,0,z)|² via D3.js, radial probability density P(r) with r_mp and ⟨r⟩ marked, energy level diagram with selection rule check and wavelength calculator. The library draft (_lib_qmsri-07-the-hydrogen-atom.md) contains a detailed four-move prompt spec for Claude Code and six failure modes to watch for.

---

## F. Library files relevant to this chapter

- **Primary:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-07-the-hydrogen-atom.md` — full rich chapter draft. Contains: the two-body reduction with isotope shift; separation of variables; the full ground-state calculation by ansatz; the general Laguerre polynomial solution and quantum number constraints; the two-radii derivation and interpretation; the full spectrum and Balmer calculation; the shape question (complex vs. real orbitals); the hidden 𝔰𝔬(4) symmetry and Runge–Lenz vector; transitions and selection rules (with Lamb shift and ALPHA antihydrogen mention); three misconceptions section; complete LLM exercise spec (five parts + six failure modes); and ten exercises spanning warm-up through challenge.
- **Supporting:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-06-spin.md` — confirms the bridge: "Chapter 7 returns to the hydrogen atom and adds m_s = ±½ to the three quantum numbers derived from orbital angular momentum."

---

## G. Gaps and flags

- **The library draft is essentially complete.** The chapter author's task is primarily structural: decide ordering (start from Balmer story or from the Hamiltonian?), choose which exercises to keep, and integrate forward references to Ch. 8 (addition of angular momenta, needed for fine structure) and Ch. 9 (perturbation theory, where fine structure is actually computed).
- **Internal numbering.** The library draft refers to "Chapter 8" for identical particles — but in the current vol2 structure, Ch. 8 is addition of angular momenta and Ch. 9 is hydrogen. The bridge sentence at the end of the library draft ("Chapter 8: You have solved one-electron hydrogen...the next step is two electrons — helium") was written for a different chapter numbering. This must be updated in the final chapter draft.
- **The 𝔰𝔬(4) symmetry section.** The library draft includes an honest admission: "I cannot make the connection feel obvious... The math is settled. The explanation... is not there for me." Decide whether to keep this intellectual honesty as a pedagogical feature or replace with a more confident treatment.
- **Figures needed.** The library draft references eight figures: V_eff(r), the 1s wave function as a 2D cross-section, P(r) with r_mp and ⟨r⟩ labeled, gallery of |ψ_{nℓm}|² cross-sections, complex vs. real orbital comparison, energy level diagrams with selection rules, misconception-vs-reality comparison, and the Bohr model refutation. These need to be commissioned or generated from the LLM exercise simulator.
- **No explicit treatment of continuous spectrum.** The chapter covers only bound states (E < 0). The continuum (E > 0, scattering states) is mentioned implicitly in selection rules but not developed. Confirm this is intentional for this volume.
