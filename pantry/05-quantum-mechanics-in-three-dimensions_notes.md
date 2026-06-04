# Research Notes: Chapter 05 — Quantum Mechanics in Three Dimensions

**Corresponding chapter:** chapters/05-quantum-mechanics-in-three-dimensions.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) write the 3D time-independent Schrödinger equation in spherical coordinates; (2) apply separation of variables to any central potential to produce a universal angular equation and a potential-specific radial equation; (3) identify the angular operator L̂² and explain why its eigenvalues are ℏ²ℓ(ℓ+1); (4) apply the u = rR substitution to cast the radial equation as a 1D Schrödinger equation with an effective potential including the centrifugal barrier; (5) read and interpret the spherical harmonics Y_ℓ^m; (6) distinguish the physics (complex) and chemistry (real) orbital bases and explain what each diagonalizes.

---

## A. Conceptual foundations

### 1. The central-potential accident and separation of variables

**Explanation:** The 3D TISE −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ is generically inseparable. The "accident" is that most physically important potentials are central — V = V(r) — which makes the angular part of ∇² separable from the radial part. In spherical coordinates, ∇² splits into a purely radial term plus (1/r²)L̂², where L̂² is defined as −ℏ²[∂_θ(sinθ ∂_θ)/sinθ + ∂_φ²/sin²θ]. With the product ansatz ψ = R(r)Y(θ,φ), dividing by RY and multiplying by r² separates the equation into a radial ODE (containing V(r)) and an angular PDE (containing only L̂²), with a shared separation constant conventionally written ℓ(ℓ+1). The angular equation Y = ℓ(ℓ+1)Y is potential-independent: it is solved once and the solutions — the spherical harmonics — apply to every central potential.

**Common misconception:** Students think separability requires V = 0. It requires only V = V(r). The Coulomb potential, the nuclear shell-model well, and the 3D harmonic oscillator all separate in spherical coordinates. The phrase "separation of variables" sounds like a trick; it is actually the statement that rotational symmetry of the potential implies [H, L̂²] = [H, L̂_z] = 0.

**Worked example:** Write out the 3D TISE with V(r) = −e²/(4πε₀r) in spherical coordinates. Insert ψ = R(r)Y_ℓ^m. Divide by RY_ℓ^m and collect radial terms on the left, angular on the right. Show each side must equal ℓ(ℓ+1). Write down the two resulting equations and label which depends on the specific potential.

**Sources:** _lib_qmsri-05-quantum-mechanics-in-three-dimensions.md §"The accident" and §"Separating variables"; _lib_qmsri-qm-townsend-notes.md §"A particle in a spherically symmetric potential" (§2).

---

### 2. The angular equation: spherical harmonics and their quantum numbers

**Explanation:** Separating Y(θ,φ) = Θ(θ)Φ(φ) produces the azimuthal equation Φ'' = −m²Φ → Φ_m = e^{imφ}/√(2π). Single-valuedness requires m to be an integer. The polar equation becomes the associated Legendre equation; its solutions P_ℓ^m(cosθ) are regular at the poles only when ℓ is a non-negative integer and |m| ≤ ℓ. These constraints are not imposed by hand — they fall out of regularity requirements. The spherical harmonics are Y_ℓ^m = N_ℓ^m P_ℓ^m(cosθ) e^{imφ}, normalized so ∫|Y_ℓ^m|² dΩ = 1. They are a complete orthonormal basis for functions on the sphere. Key fact: |Y_ℓ^m|² is independent of φ for every ℓ, m (the φ-dependence lives only in the phase e^{imφ}, killed by the modulus squared). The angular probability density is always axially symmetric about the z-axis.

**Common misconception:** The chemistry orbitals p_x, p_y are real linear combinations of Y_1^{±1} that point along the Cartesian axes, but they are NOT eigenstates of L̂_z. Students confuse "real wave function" with "eigenstate of angular momentum." The physics basis (complex Y_ℓ^m) diagonalizes L̂_z; the chemistry basis (real p_x, p_y, p_z) diagonalizes the spatial direction but has no definite L̂_z. Both bases span the same ℓ = 1 subspace.

**Worked example:** Compute Y_1^1(θ, φ) explicitly. Apply L̂_z = −iℏ ∂_φ and verify the result is +ℏ Y_1^1 (Condon-Shortley phase convention gives a minus sign in the overall normalization, but L̂_z eigenvalue is +ℏ). Then act with L̂_z on p_x ∝ sinθ cosφ and show the result is a multiple of p_y, confirming p_x is not an L̂_z eigenstate.

**Sources:** _lib_qmsri-05 §"The angular equation: what falls out," §"The angular momentum operators," §"The chemistry-textbook orbitals"; _lib_qmsri-qm-townsend-notes.md §1.11 "Angular momentum" and §"Angular momentum in coordinate representation."

---

### 3. The radial equation and the centrifugal barrier

**Explanation:** After separating the angular part, the radial equation is a 2nd-order ODE for R(r). The substitution u(r) = rR(r) converts it exactly to the 1D Schrödinger equation:
  −(ℏ²/2m) d²u/dr² + V_eff(r) u = E u
with V_eff(r) = V(r) + ℏ²ℓ(ℓ+1)/(2mr²).
The centrifugal term ℏ²ℓ(ℓ+1)/(2mr²) is strictly kinetic (it is the angular part of the kinetic energy, not a new force). For ℓ > 0 it diverges at r = 0 and suppresses the wave function near the origin. For ℓ = 0 (s-states), there is no barrier and R(0) can be nonzero. Boundary conditions: u(0) = 0 (to keep R = u/r finite at the origin); u → 0 as r → ∞ (normalizability). The radial probability density is |u(r)|² = r²|R(r)|² — probability per unit radial distance.

**Common misconception:** Students trained on classical mechanics think the centrifugal barrier is a real outward force. It is a kinetic energy contribution — the angular kinetic energy L²/(2mr²) evaluated in the eigenstate of L² with eigenvalue ℏ²ℓ(ℓ+1). Placing it on the same side as V(r) is a notational convenience, not a claim about its physical origin.

**Worked example:** Starting from the radial equation for R(r), carry out the u = rR substitution explicitly. Show the first derivative term ∂_r(r² ∂_r R) produces an extra term that cancels the first-derivative piece, leaving d²u/dr² clean. Identify which term becomes the centrifugal barrier.

**Sources:** _lib_qmsri-05 §"The radial equation and the centrifugal barrier"; _lib_qmsri-qm-townsend-notes.md §"A particle in a spherically symmetric potential"; Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., Ch. 9.

---

### 4. The spherical infinite well: a solvable example connecting to nuclear physics

**Explanation:** Take V = 0 for r < a and V = ∞ for r ≥ a. Inside the well, the radial equation reduces to the spherical Bessel equation with solutions j_ℓ(kr). The boundary condition u(a) = 0 → j_ℓ(ka) = 0 → ka = β_{nℓ} (n-th zero of j_ℓ). Energies: E_{nℓ} = ℏ²β_{nℓ}²/(2ma²). For ℓ = 0: j₀(ρ) = sinρ/ρ, zeros at nπ → E_{n,0} = n²π²ℏ²/(2ma²). This is identical to the 1D infinite-well spectrum; the s-states of the spherical well are exactly the 1D problem. The level ordering (1s, 1p, 1d, 2s, 1f, ...) obtained by sorting zeros of Bessel functions is the foundation of the nuclear shell model; adding spin-orbit coupling then reproduces the observed magic numbers (Goeppert Mayer & Jensen, Nobel 1963).

**Common misconception:** Students expect higher ℓ to always mean higher energy. In the spherical well, yes (centrifugal barrier raises energy). In hydrogen, no — the n-dependent degeneracy makes all ℓ states with the same n degenerate. In the 3D harmonic oscillator, energies depend on 2n_r + ℓ. The angular machinery is universal; the level ordering is potential-specific.

**Worked example:** For the spherical well at ℓ = 1, use j₁(β) = sinβ/β² − cosβ/β. Its first zero is β₁,₁ ≈ 4.493. Compute E_{1,1}/E_{1,0} = (4.493/π)² ≈ 2.05. The first p-state is about twice the energy of the first s-state; the centrifugal barrier raised it.

**Sources:** _lib_qmsri-05 §"A solvable example: the spherical well"; _lib_qmsri-qm-townsend-notes.md §2.

---

### 5. The universality of spherical harmonics

**Explanation:** The Y_ℓ^m appear in atomic orbitals, the nuclear shell model, the multipole expansion of electromagnetic fields, the gravitational potential of any nearly-spherical body, and the CMB angular power spectrum. The Planck collaboration reports CMB temperature anisotropies as C_ℓ (power at multipole ℓ), with the acoustic peak at ℓ ≈ 220. The same mathematical index ℓ that distinguishes s, p, d, f orbitals labels the multipoles of the observable universe. This is not a coincidence — any observable defined on a sphere has a natural expansion in Y_ℓ^m.

**Common misconception:** Students think "spherical harmonics" are a special technique for chemistry. They are the eigenfunctions of any rotationally symmetric operator on a sphere and appear in any problem with spherical symmetry.

**Worked example:** The electric potential of a charge distribution confined to a sphere is Φ(r, θ, φ) = Σ_{ℓm} A_ℓm r^{−(ℓ+1)} Y_ℓ^m(θ,φ) outside the sphere — the multipole expansion. Reading off ℓ = 0 gives the monopole (1/r potential); ℓ = 1 gives the dipole (1/r²). This is the electromagnetic application that preceded quantum mechanics.

**Sources:** _lib_qmsri-05 §"The same mathematics, much larger."

---

## B. Domain examples and cases

- **Atomic orbitals:** ψ = R_{nℓ}(r) Y_ℓ^m(θ,φ). The s-orbital Y_0^0 = 1/√(4π) has no angular structure. The p-orbital Y_1^0 ∝ cosθ is maximal at the poles. The d-orbital Y_2^0 ∝ 3cos²θ − 1 has nodes at the "magic angle" 54.7°.
- **Condon-Shortley phase convention:** Y_1^1 = −√(3/8π) sinθ e^{iφ}. The leading minus sign is the convention. Simulations that omit it produce sign errors in ladder-operator matrix elements.
- **Nuclear shell model:** Spherical-well level ordering (1s, 1p, 1d, 2s, ...) + spin-orbit term reproduces nuclear magic numbers 2, 8, 20, 28, 50, 82, 126.
- **CMB power spectrum:** C_ℓ vs. ℓ is the observational product of the Planck mission. The first acoustic peak at ℓ ≈ 220 encodes the sound horizon at recombination.
- **Accidental degeneracy (flag for Ch. 7):** Hydrogen energies depend only on n = n_r + ℓ + 1, not on ℓ separately. This is due to the hidden SO(4) symmetry of the 1/r potential (conserved Runge-Lenz vector). The 3D harmonic oscillator has SU(3) symmetry and energy 2n_r + ℓ. Neither degeneracy is obvious from the angular machinery alone.

---

## C. Connections and dependencies

- **Depends on:** Ch. 1–3 (Hilbert space, operators, harmonic oscillator), Ch. 4 (time-evolution, separation of variables concept). Students need to be comfortable with 2nd-order ODEs and know what "boundary conditions force quantization" means.
- **Feeds forward to:** Ch. 6 (angular momentum algebra — the algebraic derivation of what this chapter derived analytically), Ch. 7 (hydrogen atom — same radial machinery, Coulomb V(r)), Ch. 8 (identical particles — orbital quantum numbers label many-body states).
- **Parallel to:** The harmonic oscillator (Ch. 3) showed that boundary conditions force quantization in 1D. This chapter is the 3D generalization: regularity at r = 0 and r → ∞ forces both ℓ and n_r to be non-negative integers.
- **Key identity linking chapters 5 and 6:** The angular equation L̂²Y = ℏ²ℓ(ℓ+1)Y appears in Ch. 5 as a result of separation of variables. Ch. 6 will re-derive the spectrum ℏ²ℓ(ℓ+1) purely algebraically, from commutation relations alone, without solving any differential equation.

---

## D. Current state of the field

The mathematics of this chapter is completely settled (Legendre, Laplace, 19th century; quantum application, Schrödinger 1926). Pedagogically active areas:

- **Orbital visualization tools:** Modern computational chemistry courses use real-time interactive 3D orbital displays (D3.js, WebGL-based). The local draft includes a detailed LLM exercise prompt for a single-file D3 simulation of the spherical harmonics. This is state-of-practice for computational pedagogy.
- **Atomic structure and spectroscopy:** The single-electron machinery of this chapter underlies all of atomic spectroscopy. Many-body effects (Ch. 8, perturbation theory Ch. 9–10) are corrections to this baseline.
- **Nuclear structure:** The spherical shell model (this chapter) is the starting point; modern nuclear structure uses the no-core shell model (ab initio) and energy density functionals — active research.

---

## E. Teaching considerations

- **The "accident" framing:** The local draft opens with the question "what exactly is the chemistry orbital picture showing?" This is a strong hook — it creates the need for the formalism before presenting it.
- **Sequencing the angular and radial parts:** Many textbooks introduce the spherical harmonics by solving the angular equation first, then the radial equation. This is correct but can feel like "first solve this equation we are given." The better framing: separation of variables produces the two equations; solve the angular one first because it is universal, then tackle the radial one for each V(r).
- **The u = rR substitution:** This is a standard trick that students often do mechanically without understanding why it works. Emphasize that it eliminates the first-derivative term (because the Laplacian in spherical coordinates has a 2/r ∂_r term from the volume element), producing a clean 1D equation.
- **Condon-Shortley phase:** Flag this convention explicitly. The sign of Y_1^1 (the leading minus) is a source of errors in matrix elements for ladder operators in Ch. 6.
- **Chemistry vs. physics basis:** This is the pedagogical payoff of the chapter. Students who see orbital pictures in chemistry courses often believe the dumbbell shapes ARE the angular momentum eigenstates. The distinction between the two bases (and what each diagonalizes) is a key conceptual outcome.
- **Visualization:** The local draft contains a complete LLM exercise for a D3-based spherical harmonics simulator. This is appropriate for an interactive textbook. The simulation should support both |Y|² (probability density, φ-independent) and Re(Y) (signed wave function, φ-dependent) modes.

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-05-quantum-mechanics-in-three-dimensions.md` — The primary source. A rich, complete prose draft covering: the accident, separation, the angular equation, spherical harmonics (explicit table of first few Y_ℓ^m, Condon-Shortley convention), the angular momentum operators, why L² ≠ (L_z)², chemistry vs. physics orbital basis, the radial equation and centrifugal barrier, the spherical well example, CMB connection. Also contains a detailed LLM simulation exercise.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — §1.11 "Angular momentum" (classical definition, commutation relations) and §2 "A particle in a spherically symmetric potential" (separation in spherical coordinates, central potential Hamiltonian split into radial + L²/2mr² terms, separation to angular and radial equations). Good for concise algebraic reference.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-07-the-hydrogen-atom.md` — Ch. 7 source (not yet mined). The radial equation for the Coulomb potential is the direct sequel.

---

## G. Gaps and flags

1. **No gap in primary material.** The local draft _lib_qmsri-05 is a rich, fully worked narrative. It is among the strongest source files in the pantry.
2. **FLAG — Accidental degeneracy of hydrogen (SO(4)/Runge-Lenz):** The local draft explicitly flags this as "still puzzling" to the author and does not resolve it. The chapter should either include a brief note ("explained by the conserved Runge-Lenz vector; see supplement") or flag it as an open question for the curious student. Do not fabricate an explanation.
3. **FLAG — Normalization of associated Legendre polynomials:** The formula for Y_ℓ^m with the Condon-Shortley phase convention is given correctly in the local draft. Verify against Griffiths (Eq. 4.32) or Townsend before typesetting.
4. **FLAG — Radial probability density:** The local draft defines |u(r)|² as the radial probability density (probability per unit length). Confirm the exact statement: P(r) dr = |u(r)|² dr = r²|R(r)|² dr = |ψ|² r² sinθ dθ dφ dr (integrated over angles). The distinction between r²|R|² and |R|² matters when plotting.
5. **No web research needed:** The chapter content is fully covered by the local draft. The local draft is explicitly written for the textbook and requires no supplement.
