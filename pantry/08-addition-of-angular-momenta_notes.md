# Research Notes: Chapter 08 — Addition of Angular Momenta
**Corresponding chapter:** chapters/08-addition-of-angular-momenta.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: state the triangle rule for combining j₁ and j₂ into allowed values of total J; construct the coupled basis states |J,M⟩ for two spin-½ particles explicitly (the singlet and all three triplet states); read a Clebsch–Gordan table and use it to convert between uncoupled |m₁,m₂⟩ and coupled |J,M⟩ bases; and explain why spin–orbit coupling H_so = λL⃗·S⃗ is diagonal in the coupled basis but not in the uncoupled basis. The worked example builds the four coupled states for ½⊗½ = 0⊕1 from scratch using the ladder operator method.

---

## A. Conceptual foundations

### The problem: two angular momenta

When a system has two angular momentum sources — two spins, or a spin and an orbital — two complete orthonormal bases describe the same Hilbert space:

**Uncoupled (product) basis:** |j₁, j₂; m₁, m₂⟩ = |j₁,m₁⟩ ⊗ |j₂,m₂⟩.
- Simultaneous eigenstates of Ĵ₁², Ĵ₂², Ĵ_{1z}, Ĵ_{2z}
- Total z-component: M = m₁ + m₂ (this is exact and always holds)
- Number of states: (2j₁+1)(2j₂+1)
- These are product states; not eigenstates of Ĵ² = (Ĵ₁+Ĵ₂)²

**Coupled basis:** |j₁, j₂; J, M⟩ (often written |J,M⟩ when j₁,j₂ are fixed)
- Simultaneous eigenstates of Ĵ₁², Ĵ₂², Ĵ², Ĵ_z
- J is the total angular momentum quantum number; M its z-component
- Note: Ĵ₁² and Ĵ₂² still commute with everything, so j₁,j₂ are still good quantum numbers; only the z-components lose definite values

Both bases span the same Hilbert space of dimension (2j₁+1)(2j₂+1). The Clebsch–Gordan coefficients are the unitary transformation matrix between them.

Source: Fitzpatrick, *Quantum Mechanics* (UT Austin open course), section "Two Spin One-Half Particles," https://farside.ph.utexas.edu/teaching/qmech/Quantum/node97.html; Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., Ch. 5; CU Boulder PHYS 5250, Lecture 33, https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec33-clebsch-gordan/

### The triangle rule (Clebsch–Gordan series)

The allowed values of J for combining j₁ and j₂ are:
  J = |j₁−j₂|, |j₁−j₂|+1, ..., j₁+j₂
in unit steps. This is the quantum triangle inequality. Each J appears once. Counting states:
  Σ_{J=|j₁−j₂|}^{j₁+j₂} (2J+1) = (2j₁+1)(2j₂+1) ✓

In representation-theoretic notation: j₁ ⊗ j₂ = |j₁−j₂| ⊕ (|j₁−j₂|+1) ⊕ ... ⊕ (j₁+j₂)

Examples:
- ½ ⊗ ½ = 0 ⊕ 1 (1 singlet + 3 triplet states; 4 total = 2×2)
- 1 ⊗ ½ = ½ ⊕ 3/2 (2 + 4 = 6 = 3×2)
- 1 ⊗ 1 = 0 ⊕ 1 ⊕ 2 (1+3+5 = 9 = 3×3)

Source: CU Boulder Lec 33; Fitzpatrick node97; Wikipedia "Clebsch–Gordan coefficients" https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients

### The two spin-½ case explicitly

The uncoupled basis has four states: |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩ (shorthand for |m₁,m₂⟩ = |+½,+½⟩, etc.).

By the triangle rule: J = 0 (singlet) and J = 1 (triplet).

**Constructing the states — ladder operator method:**

Step 1. The maximum M state |J=1, M=1⟩ must be |↑↑⟩ (only one state with M = m₁+m₂ = +1):
  |1,1⟩ = |↑↑⟩

Step 2. Apply the lowering operator Ĵ₋ = Ĵ_{1−} + Ĵ_{2−} to both sides. Using Ĵ₋|J,M⟩ = ℏ√[(J+M)(J−M+1)]|J,M−1⟩ and Ĵ_{i−}|↑⟩ = ℏ|↓⟩:
  √2 ℏ |1,0⟩ = ℏ|↓↑⟩ + ℏ|↑↓⟩
  |1,0⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩)   [symmetric under exchange]

Step 3. Apply Ĵ₋ again:
  |1,−1⟩ = |↓↓⟩

Step 4. The singlet |0,0⟩ must be orthogonal to |1,0⟩ and have M=0, so it is a superposition of |↑↓⟩ and |↓↑⟩. Orthogonality to (|↑↓⟩+|↓↑⟩)/√2 and normalization give:
  |0,0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩)   [antisymmetric under exchange]

**The four coupled states in full:**

Triplet (J=1), symmetric:
  |1,+1⟩ = |↑↑⟩
  |1, 0⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩)
  |1,−1⟩ = |↓↓⟩

Singlet (J=0), antisymmetric:
  |0, 0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩)

Key properties of the singlet: Ĵ²|0,0⟩ = 0; Ĵ_z|0,0⟩ = 0; antisymmetric under particle exchange (|↑↓⟩ and |↓↑⟩ appear with opposite sign). The singlet has total angular momentum zero — it is rotationally invariant.

Source: Fitzpatrick Table 4 (Clebsch–Gordan for ½+½), https://farside.ph.utexas.edu/teaching/qmech/Quantum/node97.html; Townsend Ch. 5; the Townsend notes in _lib_qmsri-qm-townsend-notes.md at lines ~2294–2424, which give the explicit matrix form and the ortho/parahydrogen application.

### Clebsch–Gordan coefficients

The CG coefficients ⟨j₁,j₂; m₁,m₂ | j₁,j₂; J,M⟩ are the expansion coefficients of the coupled state in the uncoupled basis:
  |J,M⟩ = Σ_{m₁,m₂} ⟨j₁,j₂; m₁,m₂ | J,M⟩ |m₁,m₂⟩
and conversely:
  |m₁,m₂⟩ = Σ_{J,M} ⟨J,M | j₁,j₂; m₁,m₂⟩ |J,M⟩

Properties of CG coefficients (all real in the standard Condon–Shortley convention):
1. Vanish unless M = m₁ + m₂ (selection rule)
2. Vanish unless |j₁−j₂| ≤ J ≤ j₁+j₂
3. Unitary: the table is a square unitary (in fact orthogonal) matrix
4. Phase convention: the coefficient with maximum m₁ (i.e., m₁ = j₁) is taken positive
5. Symmetry under exchange: ⟨j₁,j₂; m₁,m₂ | J,M⟩ = (−1)^{J−j₁−j₂} ⟨j₂,j₁; m₂,m₁ | J,M⟩
6. Symmetry under sign flip: ⟨j₁,j₂; −m₁,−m₂ | J,−M⟩ = (−1)^{J−j₁−j₂} ⟨j₁,j₂; m₁,m₂ | J,M⟩ [so tables often show only M≥0]

**How to read a CG table for ½⊗½:**
- Rows label uncoupled states |m₁,m₂⟩; columns label coupled states |J,M⟩
- The entry at row (m₁,m₂) and column (J,M) is the CG coefficient (often printed as the coefficient squared with a sign)
- Example: the entry for (m₁=+½, m₂=−½) → (J=1,M=0) is 1/√2; for (J=0,M=0) is 1/√2
- The entry for (m₁=−½, m₂=+½) → (J=1,M=0) is 1/√2; for (J=0,M=0) is −1/√2 (the sign distinguishes singlet from triplet)

Source: Fitzpatrick Table 4; CU Boulder Lec 33 (full derivation for 1⊗½ → 3/2⊕½, showing the block-diagonal structure and ladder-operator method in detail).

### Generating CG coefficients: the ladder operator recursion

The general recursion relation (derived from Ĵ_± acting on |J,M±1⟩ and equating to the product-basis expansion) is:
  √[(J∓M)(J±M+1)] ⟨m₁,m₂ | J,M±1⟩
    = √[(j₁±m₁)(j₁∓m₁+1)] ⟨m₁∓1,m₂ | J,M⟩
    + √[(j₂±m₂)(j₂∓m₂+1)] ⟨m₁,m₂∓1 | J,M⟩

Practical algorithm:
1. Start with |J=j₁+j₂, M=j₁+j₂⟩ = |j₁,j₂⟩ (the stretched state; CG coefficient = 1 by convention)
2. Apply Ĵ₋ repeatedly to generate all M values within the highest J multiplet
3. Orthogonalize within each M sector to obtain the next-lower J
4. Repeat

For ½⊗½ this terminates at step 3; for larger j values tables or computer algebra (e.g., sympy.physics.quantum.cg) are standard.

Source: CU Boulder PHYS 5250, Lecture 33, https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec33-clebsch-gordan/

### Why the coupled basis diagonalizes spin-orbit coupling

The spin-orbit Hamiltonian is H_so = λ L⃗·S⃗. Using the identity
  L⃗·S⃗ = (1/2)(Ĵ² − L̂² − Ŝ²)
where Ĵ = L̂ + Ŝ, we have:
  L⃗·S⃗ |J,M; ℓ,s⟩ = (ℏ²/2)[J(J+1) − ℓ(ℓ+1) − s(s+1)] |J,M; ℓ,s⟩

This is an eigenvalue equation in the coupled basis. In the uncoupled |m_ℓ, m_s⟩ basis, L⃗·S⃗ has off-diagonal elements (it couples states with different m_ℓ and m_s while keeping M = m_ℓ + m_s fixed), so the uncoupled basis does not diagonalize H_so.

Consequence: to find the fine-structure energy shifts of hydrogen, we must work in the |J,M⟩ = |n,ℓ,J,M⟩ basis. The first-order energy correction is:
  ΔE_so = (λℏ²/2)[J(J+1) − ℓ(ℓ+1) − s(s+1)]

For the 2p state of hydrogen (ℓ=1, s=½): J = 3/2 (four states) and J = 1/2 (two states) split apart. The J=3/2 level is higher. This is the spin-orbit fine structure — the subject of Vol. 3. The CG decomposition developed in this chapter is the necessary prerequisite.

Source: CU Boulder Lec 33 (spin-orbit of 2p hydrogen, the energy level diagram with j=3/2 and j=1/2 sub-levels); Duke ECE lecture notes, "Chapter 4: Spin-Orbit Coupling — Addition of Angular Momenta," https://people.ee.duke.edu/~jungsang/ECE590_01/LectureNotes4-Rev.pdf; Townsend notes in _lib, lines ~2910–2985.

### The hyperfine case: two spin-½ particles in hydrogen

The hydrogen hyperfine interaction H_hf = A S⃗_e · S⃗_p involves coupling electron spin S=½ to proton spin I=½. The uncoupled basis has four states |m_S, m_I⟩. The coupled-basis decomposition gives F = 0 (singlet) and F = 1 (triplet), where F is the total spin quantum number. The energy eigenvalues:
  E_{F=1} = Aℏ²/4 (triplet, three states degenerate)
  E_{F=0} = −3Aℏ²/4 (singlet)
The singlet-triplet splitting ΔE = Aℏ² corresponds to the 21-cm (1420 MHz) hyperfine line of hydrogen, the most important spectral line in radio astronomy.

The Clebsch–Gordan coefficient table for this case is exactly Table 4 from Fitzpatrick (½⊗½). In the Townsend notes (_lib_qmsri-qm-townsend-notes.md, lines 2943–2987), the 4×4 hyperfine Hamiltonian matrix is diagonalized explicitly and the singlet/triplet identification is made; the CG coefficients appear explicitly as the projection table on lines 2989–2992.

Source: Townsend notes in _lib (lines 2943–2992); Townsend, *A Modern Approach to Quantum Mechanics*, Ch. 5.

### The direct product / direct sum decomposition

In representation-theoretic notation:
  j₁ ⊗ j₂ = |j₁−j₂| ⊕ (|j₁−j₂|+1) ⊕ ... ⊕ (j₁+j₂)

This means the product Hilbert space decomposes into mutually orthogonal invariant subspaces, each labeled by a total-J value. Within each subspace, the ladder operators Ĵ± connect the 2J+1 states but do not connect one subspace to another. This block-diagonal structure is what makes Ĵ² diagonal in the coupled basis.

For ½⊗½: ½⊗½ = 0⊕1. Dimension check: 2×2 = 1+3. ✓
For 1⊗½: 1⊗½ = ½⊕3/2. Dimension check: 3×2 = 2+4. ✓
For 1⊗1: 1⊗1 = 0⊕1⊕2. Dimension check: 3×3 = 1+3+5. ✓

Source: CU Boulder Lec 33 (the direct sum decomposition section, with explicit dimension checks).

---

## B. Domain examples and cases

**Hydrogen 21-cm line.** The F=1→F=0 transition (triplet to singlet) emits at 1420.405 MHz (λ ≈ 21.1 cm). This is the most observed spectral line in radio astronomy — used to map the structure of the Milky Way, detect neutral hydrogen in distant galaxies, and as a universal communication frequency in SETI proposals. It exists because of the singlet-triplet splitting from exactly the ½⊗½ decomposition in this chapter.

**Orthohydrogen and parahydrogen.** H₂ molecules have two proton spins. Triplet spin state (orthohydrogen, I=1) admits only odd rotational states ℓ = 1,3,5,... (because total wave function must be antisymmetric under proton exchange). Singlet spin state (parahydrogen, I=0) admits only even ℓ. The two forms are stable for weeks at room temperature; catalytic interconversion requires a spin-flip mechanism. This example is worked explicitly in the Townsend notes (_lib, lines 2400–2406).

**Spinless-particle analogy.** For two orbital angular momenta ℓ₁=1 and ℓ₂=1 (e.g., two p-electrons), L = 0,1,2 — S, P, D terms. This is the same triangle rule applied to spectroscopic term symbols. Hund's rules about which term has lowest energy are downstream of the spatial symmetry of each L value (the singlet/triplet concept extended to orbital space).

**NMR spin systems.** Coupled proton spin pairs in organic chemistry produce multiplet patterns (doublets, triplets) whose intensities are the squared CG coefficients. The AX spin system (two weakly coupled protons) decomposes as ½⊗½ = 0⊕1; the triplet lines are the F=1 states and the singlet is the F=0 dark state (not directly NMR-active due to symmetry).

**Quantum information: Bell states.** The four coupled states for ½⊗½ are, up to relabeling, the Bell basis:
  |Φ+⟩ = (|00⟩+|11⟩)/√2 ≡ |1,0⟩ (up to basis conventions)
  |Ψ+⟩ = (|01⟩+|10⟩)/√2 ≡ |1,0⟩
  |Ψ−⟩ = (|01⟩−|10⟩)/√2 ≡ |0,0⟩ (the singlet)
The singlet |0,0⟩ is the maximally entangled state used in EPR experiments and quantum key distribution. Its rotational invariance (it looks the same in any measurement basis) is precisely the statement that Ĵ²|0,0⟩ = 0.

---

## C. Connections and dependencies

**Prerequisites:**
- Ch 5 (Angular momentum algebra): [Ĵᵢ,Ĵⱼ] = iℏε_{ijk}Ĵₖ; raising/lowering operators Ĵ±; the fact that Ĵ² and Ĵ_z share eigenstates; the ladder operator action Ĵ±|j,m⟩ = ℏ√[(j∓m)(j±m+1)]|j,m±1⟩. All of this is used directly in the CG construction.
- Ch 7 (Spin): The two-spin system with basis |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩ is the primary worked example of this chapter. Students must be fluent with Pauli matrices and spin eigenvalues.

**Feeds into:**
- Ch 9 (Hydrogen atom): The quantum numbers (n, ℓ, m) introduced there are the uncoupled-basis labels for the orbital part; spin adds m_s = ±½. When spin-orbit coupling is included (Vol. 3), the coupled-basis labels (n, ℓ, J, M_J) replace the uncoupled (n, ℓ, m_ℓ, m_s).
- Vol. 3 (Fine structure): The main application. L⃗·S⃗ = (Ĵ²−L̂²−Ŝ²)/2 is diagonal in |J,M⟩; fine-structure energy shifts are ΔE = (λℏ²/2)[J(J+1)−ℓ(ℓ+1)−s(s+1)].
- Vol. 3 (Zeeman effect): When both spin-orbit and an external magnetic field are present, we must simultaneously use coupled (for spin-orbit) and uncoupled (for Ĥ_B = μ_B(L̂_z + 2Ŝ_z)) bases. CG coefficients are the translation dictionary. This is illustrated explicitly for 2p hydrogen in CU Boulder Lec 33.
- Vol. 3 (Identical particles): The singlet/triplet decomposition for two electrons determines spatial wave function symmetry (singlet spin → symmetric spatial; triplet spin → antisymmetric spatial). The exchange energy difference between singlet and triplet helium states is computed using these combined wave functions.

---

## D. Current state of the field

CG coefficients are tabulated and computationally accessible. Software tools: Wolfram's `ClebschGordan[{j1,m1},{j2,m2},{J,M}]`, Python's `sympy.physics.quantum.cg.CG`, and Racah algebra packages in nuclear and particle physics. Tables appear in appendices of every major quantum mechanics text (Griffiths, Sakurai, Cohen-Tannoudji).

In contemporary physics: CG coefficients appear in angular momentum selection rules for spectroscopy, in the multipole expansion of electromagnetic radiation, in nuclear and particle physics (isospin coupling, quark model), and in quantum information (entangled-state generation and Bell-inequality tests). The representation-theoretic framework (j₁⊗j₂ = ⊕J) is ubiquitous in group theory applied to physics.

The MIT open-access paper on CG coefficients and magnetic resonance (Saliba 2022, https://onlinelibrary.wiley.com/doi/10.1155/2022/1143341) gives a pedagogically clear modern presentation oriented toward NMR applications.

---

## E. Teaching considerations

**The "M = m₁ + m₂" anchor.** Students should internalize this selection rule first. Every non-zero CG coefficient in the table satisfies it. It dramatically limits which entries could be non-zero before any calculation.

**Build the ½⊗½ table by hand first.** The worked example should be done with ladder operators, not by looking up the table. The calculation is short (four steps), and doing it cements the method for the harder cases students will encounter later.

**The singlet vs. triplet sign.** The −sign in |0,0⟩ = (|↑↓⟩−|↓↑⟩)/√2 versus the + sign in |1,0⟩ = (|↑↓⟩+|↓↑⟩)/√2 is crucial and regularly confused. The mnemonic: "triplets add, singlets subtract." The sign is enforced by the phase convention (the highest-m₁ coefficient is positive) and by orthogonality.

**Why the coupled basis matters — motivate before the machinery.** The payoff is that L⃗·S⃗ is diagonal in the |J,M⟩ basis. Without this motivation, CG coefficients feel like table-reading busywork. A one-sentence preview of fine structure ("spin-orbit coupling has the Hamiltonian L⃗·S⃗, and this chapter gives you the basis where that Hamiltonian is a matrix of eigenvalues") is enough to lock in student attention.

**State counting as a consistency check.** For every problem, verify (2j₁+1)(2j₂+1) = Σ(2J+1) before doing any algebra. Errors in the triangle rule are caught immediately.

**Worked example (as specified):** Build all four coupled states for ½⊗½ explicitly using the ladder operator method. Verify: (a) each state is normalized; (b) ⟨1,0|0,0⟩ = 0 (orthogonality); (c) Ĵ²|0,0⟩ = 0 (singlet has J=0); (d) Ĵ²|1,0⟩ = 2ℏ²|1,0⟩ (triplet has J=1). Optional extension: show that L⃗·S⃗ operating on the coupled states gives eigenvalues (ℏ²/2)[J(J+1)−3/2], confirming diagonalization.

**LLM exercise suggestion:** Build a CG calculator that takes j₁, j₂, J, M and returns the expansion in the uncoupled basis, verified against a known table. Prompt should include verification checks (normalization, M=m₁+m₂ selection rule, orthogonality between different J states at the same M).

---

## F. Library files relevant to this chapter

- **Primary local source:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — contains the Townsend Ch. 5 material on two spin-½ particles (lines ~2285–2424), the explicit singlet/triplet states and their matrix form, the ortho/parahydrogen application, and the spin-wave-function formalism for the helium exchange energy. Also contains the general coupled/uncoupled basis formalism (lines ~3027–3052) and the Clebsch–Gordan coefficient table as the projection matrix (lines 2989–2992). The hyperfine section (lines 2943–2987) works through the 4×4 matrix diagonalization and identifies the CG coefficients explicitly. This is the richest available local resource for this chapter.
- **Supporting:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-06-spin.md` — provides the spin-½ algebra prerequisites (Pauli matrices, eigenstates) that feed directly into the ½⊗½ construction.

**Web sources used for this chapter:**
- Fitzpatrick (UT Austin), "Two Spin One-Half Particles": https://farside.ph.utexas.edu/teaching/qmech/Quantum/node97.html — explicit triplet/singlet construction, full CG table (Table 4), Condon–Shortley phase convention. Strongest single source for the pure ½⊗½ case.
- CU Boulder PHYS 5250, Lecture 33 (Clebsch–Gordan): https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec33-clebsch-gordan/ — full derivation of CG coefficients for 1⊗½ using ladder operators, phase conventions and recursion, spin-orbit application to 2p hydrogen, direct sum decomposition notation. Best single source for the pedagogical derivation method and the spin-orbit motivation.
- Wikipedia, "Clebsch–Gordan coefficients": https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients — comprehensive reference for properties, symmetries, and tables.
- Saliba (2022), "The Clebsch–Gordan Coefficients and Their Application to Magnetic Resonance," MIT DSpace: https://dspace.mit.edu/bitstream/handle/1721.1/144000/CMRA.2022.1143341.pdf — pedagogically clear modern presentation with NMR applications.

---

## G. Gaps and flags

- **No Cohen-Tannoudji content accessed for this chapter.** The local Cohen-Tannoudji text file path is `/Users/bear/Documents/CoWork/bear-textbooks/books/physics-quantum-mechanics-sri/pantry/1022201323-...Cohen-Tannoudji...txt`. A targeted grep for "Clebsch" and "addition of angular momenta" in that file would likely yield further material (Cohen-Tannoudji Vol. II, Ch. X is entirely devoted to this topic). Recommended before chapter draft.
- **No explicit discussion of Racah coefficients (6j symbols).** These generalize CG coefficients to three coupled angular momenta and appear in nuclear/atomic structure. They are Vol. 3 or graduate-level material — confirm whether a brief mention is wanted here.
- **The Wigner–Eckart theorem** is a consequence of CG coefficients (it expresses how spherical tensor operators couple to angular momentum eigenstates). CU Boulder Lec 33 mentions it is covered "next time." Decide whether to include even a one-paragraph preview, as it makes selection rules for multipole radiation a direct consequence of this chapter's mathematics.
- **Sign conventions.** Different texts use different phase conventions (Condon–Shortley vs. other). The chapter should pick one and state it explicitly; a common student confusion is getting the sign of |0,0⟩ wrong relative to the table they are reading.
- **LLM exercise spec not yet drafted.** This chapter is a natural candidate for a CG calculator exercise (input j₁, j₂, J, M; output expansion; verify orthogonality). The Ch. 7 and Ch. 9 LLM exercise templates from the library files can serve as models.
