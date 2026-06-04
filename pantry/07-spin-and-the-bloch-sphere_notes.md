# Research Notes: Chapter 07 — Spin and the Bloch Sphere
**Corresponding chapter:** chapters/07-spin-and-the-bloch-sphere.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: place any spin-½ state on the Bloch sphere using (θ, φ) coordinates; apply the Pauli matrices to compute eigenvalues and expectation values for an arbitrary axis; write down and explain the time-evolution operator for a spin in a uniform magnetic field; calculate the Larmor precession frequency for a proton or electron at a given field strength; and articulate why the spinning-ball picture fails quantitatively. The worked example is the Bloch vector for a given (θ₀, φ₀) and its precession rate ω_L = γB₀.

---

## A. Conceptual foundations

**Two spots demand two dimensions.** The Stern–Gerlach experiment (Stern & Gerlach, Feb 1922) found two discrete impact spots for neutral silver atoms—not a smear. Silver has one unpaired 5s electron (ℓ = 0), so the two spots come from the intrinsic spin of that electron, not orbital angular momentum. Stern and Gerlach did not know this: they thought they were confirming Bohr–Sommerfeld space quantization. The concept of intrinsic spin was supplied by Uhlenbeck and Goudsmit (1925).

**The minimal Hilbert space.** "Always two values, any axis" forces the state space to be ℂ², two-dimensional and complex. Choose eigenstates of Ŝ_z as basis: |↑⟩ = (1,0)ᵀ, |↓⟩ = (0,1)ᵀ. General normalized state: |ψ⟩ = α|↑⟩ + β|↓⟩, |α|² + |β|² = 1. Two complex numbers minus one normalization minus one unobservable global phase = two real degrees of freedom. That is the dimension of a sphere.

**The Pauli matrices.** Spin operators Ŝᵢ = (ℏ/2)σᵢ where:
- σ_x = [[0,1],[1,0]], σ_y = [[0,−i],[i,0]], σ_z = [[1,0],[0,−1]]
- Four key facts: σᵢ² = I; Tr(σᵢ) = 0; σᵢσⱼ = −σⱼσᵢ for i≠j; [σᵢ,σⱼ] = 2iε_{ijk}σₖ
- Full algebra in one identity: σᵢσⱼ = δᵢⱼI + iε_{ijk}σₖ
- These satisfy the same commutation algebra as orbital angular momentum, justifying the name

**Why spin is not rotation.** Using the most generous electron radius (the classical electron radius r_e ≈ 2.82 × 10⁻¹⁵ m), angular momentum L = ℏ/2 requires equatorial surface speed v = 5ℏ/(4m_e r_e) ≈ 5.1 × 10¹⁰ m/s ≈ 170c. A smaller, more realistic electron radius makes this worse. The spinning-ball picture fails by more than two orders of magnitude. Spin is an internal degree of freedom transforming as an SU(2) representation; Dirac (1928) showed it is required by Lorentz covariance combined with first-order quantum dynamics.

**Spin along any axis — the Bloch sphere.** For unit vector n̂ = (sinθcosφ, sinθsinφ, cosθ), the spin operator along n̂ is:
  Ŝ_n̂ = (ℏ/2)[[cosθ, sinθe^{-iφ}],[sinθe^{iφ}, −cosθ]]
Eigenvalues: ±ℏ/2 for every axis (trace zero, det −1 → λ² = 1). The +ℏ/2 eigenstate is:
  |n̂,+⟩ = cos(θ/2)|↑⟩ + e^{iφ}sin(θ/2)|↓⟩
The half-angle parametrization maps every normalized spin state bijectively onto the surface of a unit sphere — the Bloch sphere. North pole = |↑⟩, south pole = |↓⟩, equator = equal-weight superpositions.

**Born rule on the Bloch sphere.** If the state is at (θ_ψ, φ_ψ) and the analyzer at (θ_n, φ_n), the angle γ between their Bloch vectors satisfies:
  cosγ = cosθ_ψ cosθ_n + sinθ_ψ sinθ_n cos(φ_ψ − φ_n)
and P(+) = cos²(γ/2), P(−) = sin²(γ/2). Three checks: γ=0 → P(+)=1; γ=π → P(+)=0; γ=π/2 → P(+)=1/2.

**Spinor double cover.** Rotating the analyzer by 2π sends θ→θ+2π, changing |n̂,+⟩ to −|n̂,+⟩. Only a 4π rotation restores the state. Observable in neutron interferometry. Spin states live in SU(2), not SO(3).

**Larmor precession.** For a uniform field B₀ẑ, the Hamiltonian Ĥ = −μ⃗·B⃗ = γB₀Ŝ_z is diagonal in the |↑⟩,|↓⟩ basis. Time-evolution operator:
  Û(t) = diag(e^{−iω_Lt/2}, e^{+iω_Lt/2}), ω_L = γB₀
Starting from (θ₀, φ₀=0), the state evolves to (θ₀, φ(t)=ω_Lt): the polar angle freezes, the azimuth precesses at ω_L. Expectation values:
  ⟨Ŝ_x⟩(t) = (ℏ/2)sinθ₀cos(ω_Lt), ⟨Ŝ_y⟩(t) = (ℏ/2)sinθ₀sin(ω_Lt), ⟨Ŝ_z⟩(t) = (ℏ/2)cosθ₀
The spin-vector magnitude is constant; only its projection in the xy-plane rotates.

**Gyromagnetic ratios (experimental):**
- Electron: γ_e/(2π) ≈ 28.025 GHz/T
- Proton: γ_p/(2π) ≈ 42.58 MHz/T
- Proton at 1.5 T (clinical MRI): ω_L/(2π) ≈ 63.87 MHz, period ≈ 15.66 ns
- Proton at 3 T (research MRI): ω_L/(2π) ≈ 127.74 MHz

**The anomalous g-factor.** Dirac predicts g_e = 2 exactly. Measured value: g_e ≈ 2.00232. Deviation a_e = (g_e−2)/2 ≈ α/(2π) where α ≈ 1/137: the leading QED radiative correction. Agreement between QED and experiment extends to 13 significant figures. When writing Ĥ = γŜ_zB₀, use experimental γ which includes the anomalous correction.

**Sequential SG measurements.** Start with |↑⟩, pass through SG_x (50/50 split), select |x,+⟩ = (|↑⟩+|↓⟩)/√2, pass through SG_z again → 50/50. The intermediate x-measurement does not "disturb" a pre-existing z-value. [Ŝ_x, Ŝ_z] = −iℏŜ_y ≠ 0, so no state can be simultaneously an eigenstate of both. The 50/50 is structural, not an artifact.

---

## B. Domain examples and cases

**MRI.** Proton gyromagnetic ratio γ_p/(2π) = 42.58 MHz/T is the operating equation of every MRI scanner. Clinical at 1.5 T → 63.87 MHz. Research at 7 T → 298.1 MHz. All follow ω_L = γ_pB₀.

**Quantum computing.** The spin-½ Hilbert space is the qubit. The Bloch sphere is the standard geometric picture of a qubit state. Pauli matrices are the fundamental qubit gates (X, Y, Z); Larmor precession is analogous to single-qubit rotation pulses.

**Neutron interferometry.** The spinor double cover (4π periodicity) was directly observed by Rauch et al. (1975) and Werner et al. (1975) in neutron beam interference experiments where the neutron path length was changed by physical rotation.

**Electron spin resonance (ESR).** At resonance ω = γ_eB₀, a transverse RF field coherently rotates the Bloch vector. The precession picture is exact for the rotating-wave approximation; off-resonance gives nutations on the Bloch sphere.

**Stern–Gerlach history.** The 1922 experiment used silver atoms. Gerlach reportedly sent a postcard to Bohr saying "Bohr was right after all." In fact the experiment confirmed a concept that did not yet exist (intrinsic spin), but Gerlach did not discover this until after Uhlenbeck and Goudsmit published in 1925.

---

## C. Connections and dependencies

**Prerequisite chapters:**
- Vol 1 Ch (Hilbert space) — the ℂ² space and Dirac notation
- Vol 1 Ch (Postulates) — Born rule, measurement, expectation values
- Vol 2 Ch 5 (Angular momentum algebra) — the commutation relations [Ĵᵢ,Ĵⱼ] = iℏε_{ijk}Ĵₖ that spin satisfies
- Vol 2 Ch 6 (Orbital angular momentum) — contrasting spin with orbital ℓ; the fact that ℓ is integer and spin is half-integer

**Feeds into:**
- Ch 8 (Addition of angular momenta) — the two spin-½ particles worked example starts here; Bloch vectors for each particle combined into coupled-basis states; singlet/triplet decomposition uses the formalism of this chapter directly
- Ch 9 (Hydrogen atom) — the fourth quantum number m_s = ±½ doubles the degeneracy count; 2n² states per shell
- Vol 3 (Fine structure) — spin-orbit coupling requires expressing Ŝ in the total-J eigenbasis; Larmor precession reappears as precession of both L and S around J
- Vol 3 (Identical particles / Pauli exclusion) — antisymmetry of spin states, singlet/triplet structure for two-electron systems

**Structural note:** The Pauli algebra σᵢσⱼ = δᵢⱼI + iε_{ijk}σₖ is the same algebra used in quantum field theory for Dirac spinors and in condensed matter for topological insulators. This chapter's material scales far beyond its immediate context.

---

## D. Current state of the field

The Bloch sphere formalism is now the universal language for qubit state description in quantum computing (IBM, Google, IonQ all use it in documentation). Larmor precession is the operating principle of NMR/MRI (a multi-billion-dollar medical industry). The anomalous magnetic moment a_e remains one of the most precisely tested predictions in physics (theory and experiment agree to ~13 significant figures as of 2026). Spinor geometry underlies modern topological condensed matter physics (Berry phase, Chern insulators). None of the material in this chapter is historically closed — it is actively used in current research.

---

## E. Teaching considerations

**The half-angle trips people.** Students consistently forget the factor of ½ in cos(θ/2) and compute P(+) = cos²(γ) instead of cos²(γ/2). The check at γ = π/2 (should give P(+) = 1/2, not 0) is the standard diagnostic.

**"Spin is classical rotation" misconception.** The calculation with r_e should be done explicitly in class or homework before introducing the SU(2) picture. Abstract statements ("spin has no classical analog") do not stick; the number 170c sticks.

**Precession vs. what precesses.** Students conflate the precessing Bloch vector with a precessing physical object. Emphasize: what precesses is the probability distribution over future measurement outcomes, not any physical pointer.

**Sequential SG as the key conceptual moment.** The three-stage SG experiment (prepare |↑⟩, measure x, measure z again) should be computed step by step. Students who can explain the 50/50 result without using the phrase "the x-measurement disturbed the z-value" have internalized the chapter.

**Larmor numbers anchor abstraction.** Computing γ_p × 1.5 T → 63.87 MHz makes the formalism feel real. A brief mention that this is the resonance frequency of a 1.5 T clinical MRI scanner pays off student attention.

**Worked example for the chapter (as specified):** Given θ = π/3, φ = π/4, place the state on the Bloch sphere and compute Bloch vector components. Place analyzer along n̂ = (0,0,1) (i.e., ẑ). Compute cosγ = cosθ = 1/2, γ = π/3. P(+) = cos²(π/6) = 3/4. Then switch on B₀ = 1.5 T (proton), ω_L = 2π × 42.58 MHz × 1.5 = 2π × 63.87 MHz. φ(t) = π/4 + ω_L t; θ stays at π/3.

---

## F. Library files relevant to this chapter

- **Primary:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-06-spin.md` — full chapter draft; contains the Pauli algebra, Bloch sphere parametrization, Larmor precession with MRI numbers, sequential SG analysis, anomalous g-factor, all six exercises plus LLM exercise spec. This is a rich near-final source — use it as the structural spine.
- **Supporting:** `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — Townsend Ch. 5 notes on spin-½ system, two-particle spin states (singlet/triplet), which bridges directly into Ch 8.

---

## G. Gaps and flags

- The library draft has placeholder rows in several tables (MRI frequencies, Larmor data); these need actual numbers filled in before drafting (all computable from γ_p/(2π) = 42.58 MHz/T and γ_e/(2π) = 28.025 GHz/T).
- The LLM exercise spec in the library is detailed (five parts). The chapter author should confirm whether to keep the full Monte Carlo extension (Part 4) or move it to a companion resource.
- No explicit discussion of the Bloch sphere as a Poincaré sphere for photon polarization — worth a footnote given the parallels (same mathematics, different physics).
- The library mentions "Chapter 8 will use this when it counts the states available to electrons in an atom" — but in the current vol2 structure, Ch 8 is addition of angular momenta, and identical particles/Pauli exclusion is handled differently. Confirm the internal cross-reference numbering before finalizing.
