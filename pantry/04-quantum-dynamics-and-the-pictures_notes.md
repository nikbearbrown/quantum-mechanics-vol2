# Research Notes: Chapter 04 — Quantum Dynamics and the Pictures

**Corresponding chapter:** chapters/04-quantum-dynamics-and-the-pictures.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter the student can: (1) construct the time-evolution operator U(t) = e^{-iHt/ℏ} for a time-independent Hamiltonian from first principles; (2) evolve an arbitrary state by expanding in energy eigenstates; (3) switch between the Schrödinger picture (states move, operators fixed) and the Heisenberg picture (operators move, states fixed) and verify the two give identical expectation values; (4) derive and apply the Heisenberg equation of motion dA_H/dt = (i/ℏ)[H, A_H]; (5) state Ehrenfest's theorem and identify when quantum expectation values obey classical equations of motion; (6) identify when each picture is computationally convenient.

---

## A. Conceptual foundations

### 1. The time-evolution operator U(t) = e^{-iHt/ℏ}

**Explanation:** Probability conservation requires U(t) to be unitary. For an infinitesimal step dt, the generator of time translation is the Hamiltonian: U(dt) = 1 − (i/ℏ)H dt. Unitarity forces H to be Hermitian. Iterating the infinitesimal step to finite t gives U(t) = e^{-iHt/ℏ} for time-independent H. The Schrödinger equation i ℏ d|ψ⟩/dt = H|ψ⟩ follows immediately from differentiating U(t)|ψ(0)⟩. Energy eigenstates are stationary: e^{-iHt/ℏ}|E_n⟩ = e^{-iE_n t/ℏ}|E_n⟩; the state merely accumulates a phase, and all expectation values are constant.

**Common misconception:** Students often treat U(t) = e^{-iHt/ℏ} as just a notation and do not verify it actually satisfies the Schrödinger equation for U itself: i ℏ dU/dt = HU. The equation for U is the same structure as the state equation, and it must be derived, not assumed.

**Worked example (from Townsend notes §1.7–1.8):** Two-level system with H = ω₀ Ŝ_x. Initial state |ψ(0)⟩ = |+z⟩. Expand in the eigenbasis of Ŝ_x: |x+⟩ = (|+⟩ + |−⟩)/√2. Apply U(t) = e^{-iω₀ Ŝ_x t/ℏ} to each eigenstate. Result: ⟨S_z(t)⟩ = (ℏ/2) cos ω₀t — a Rabi oscillation. The key step is projecting the initial state onto the eigenbasis of H before applying the phase factors.

**Sources:** Townsend notes §1.7 (time-evolution operator), §1.8 (time-dependence of expectation values); Feiguin notes Ch. 1 §1.7–1.8 (_lib_qmsri-qm-townsend-notes.md); Wikipedia "Schrödinger picture"; Physics LibreTexts "Schrödinger and Heisenberg Pictures."

---

### 2. The Schrödinger picture vs. the Heisenberg picture

**Explanation:** Both pictures give the same physics because all measurable quantities are expectation values ⟨ψ|A|ψ⟩. In the Schrödinger picture, states evolve: |ψ(t)⟩ = U(t)|ψ(0)⟩; operators are fixed. In the Heisenberg picture, states are fixed at their t = 0 values; operators evolve: A_H(t) = U†(t) A U(t). The expectation value is the same in both:
  ⟨ψ(t)|A|ψ(t)⟩ = ⟨ψ(0)|U†(t) A U(t)|ψ(0)⟩ = ⟨ψ(0)|A_H(t)|ψ(0)⟩.
The passage between pictures is an active/passive transformation: U(t) acts on kets in one picture, on operators in the other. Commutation relations are preserved in the passage.

**Common misconception:** Students believe the Heisenberg picture is "harder" or less fundamental. In fact Heisenberg developed it first (matrix mechanics, 1925), and for free fields and harmonic systems it is more natural: the equations of motion for operators in the Heisenberg picture are exactly the classical Hamilton's equations. The Schrödinger picture became dominant for wave-function problems, but the Heisenberg picture is preferred in quantum field theory.

**Worked example:** For a free particle, H = p²/2m. In the Heisenberg picture:
  dp_H/dt = (i/ℏ)[H, p_H] = 0 → p_H(t) = p_H(0) (momentum conserved)
  dx_H/dt = (i/ℏ)[H, x_H] = p_H(0)/m → x_H(t) = x_H(0) + p_H(0)t/m.
These are exactly the classical free-particle equations. The quantum operators obey the same time-dependence as the classical variables.

**Sources:** Wikipedia "Heisenberg picture"; Chemistry LibreTexts "The Heisenberg Picture" (Tuckerman); University of Colorado Phys 5250 lecture notes "Heisenberg picture"; Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., Ch. 4.

---

### 3. The Heisenberg equation of motion

**Explanation:** Differentiating A_H(t) = U†(t) A U(t) with respect to t and using i ℏ dU/dt = HU gives:
  i ℏ dA_H/dt = [A_H, H_H] = [A_H, H]
(H commutes with U for time-independent H, so H_H = H). This is the Heisenberg equation of motion. For an operator with no explicit time dependence, this is the complete equation of motion. For the harmonic oscillator, H = p²/2m + mω²x²/2, the equations for x_H and p_H decouple into a pair of coupled first-order ODEs whose solution is:
  x_H(t) = x_H(0) cos ωt + (p_H(0)/mω) sin ωt
  p_H(t) = p_H(0) cos ωt − mω x_H(0) sin ωt.
The quantum operator x_H(t) oscillates at frequency ω, identical to the classical result.

**Common misconception:** Students conflate the Heisenberg equation dA_H/dt = (i/ℏ)[H, A_H] with the generalized Ehrenfest relation d⟨A⟩/dt = (i/ℏ)⟨[H, A]⟩. They are related but distinct. The Heisenberg equation is an operator equation. The Ehrenfest relation is its expectation value, and requires no choice of picture.

**Worked example:** Harmonic oscillator — verify that [x_H(t), p_H(t)] = iℏ at all times (canonical commutation relations are preserved). This is a direct check that U†(t) is unitary.

**Sources:** University of Colorado Phys 5250 notes "Heisenberg picture"; University of Illinois Phys 580 "Heisenberg Representation" PDF; FSU Physics Wiki "The Heisenberg Picture: Equations of Motion for Operators"; Durban/IPPP lecture notes "Solutions: Heisenberg and Schrödinger picture."

---

### 4. The generalized Ehrenfest theorem

**Explanation:** In the Schrödinger picture, for an operator A with no explicit time dependence:
  d⟨A⟩/dt = (i/ℏ)⟨[H, A]⟩.
This is the "generalized Ehrenfest theorem" (Townsend notes §1.8). Applying it with A = x gives d⟨x⟩/dt = ⟨p⟩/m. With A = p gives d⟨p⟩/dt = −⟨∂V/∂x⟩. If the wavepacket is narrow (spatial extent ≪ scale of V variation), ⟨∂V/∂x⟩ ≈ ∂V/∂x|_{⟨x⟩} = −F(⟨x⟩), and Newton's second law holds for the expectation values. The classical limit is the limit of a narrow wavepacket, not of ℏ → 0 per se.

**Common misconception:** Ehrenfest's theorem does NOT say ⟨p⟩ = m d⟨x⟩/dt is Newton's law. The force on the right-hand side is ⟨−∂V/∂x⟩, not −∂V/∂⟨x⟩. These differ by a correction of order (Δx)² × V'''. Only when the wavepacket is narrow relative to the scale of variation of V do the two coincide. For a nonlinear potential (e.g., V = x⁴) the quantum and classical equations of motion differ even at the level of expectation values.

**Worked example:** For a free particle: d⟨x⟩/dt = ⟨p⟩/m, d⟨p⟩/dt = 0. These integrate trivially; the center of the wavepacket moves at constant velocity, but the wavepacket itself spreads. The classical trajectory of the center is exact; the wavepacket dynamics are purely quantum.

**Sources:** Townsend notes §1.8 "Time-dependence of expectation values" (_lib_qmsri-qm-townsend-notes.md); Wikipedia "Ehrenfest theorem"; Physics LibreTexts "Ehrenfest's Theorem" (Fitzpatrick); University of Texas lecture notes (Fitzpatrick, farside.ph.utexas.edu).

---

### 5. When each picture is convenient

**Explanation:** The Schrödinger picture is natural for wave mechanics — when you want ψ(x,t), when boundary conditions are spatial, when numerical integration is involved. The Heisenberg picture is natural when you want equations of motion for observables, when the problem maps onto classical mechanics (free particle, harmonic oscillator, rigid rotor), and in quantum field theory where the mode operators a, a† have clean Heisenberg equations. The interaction picture (Dirac picture) is a hybrid: H = H₀ + H₁, states evolve under H₁ alone (in the frame rotating with H₀), operators evolve freely under H₀. It is the natural setting for time-dependent perturbation theory and Fermi's golden rule; it is the starting point for Dyson series expansion in quantum field theory.

**Common misconception:** The three pictures are often taught as if one is "right" and the others are approximations. They are unitarily equivalent descriptions of the same physics. The choice is computational, not ontological.

**Worked example (role-reversal):** For the harmonic oscillator in the Heisenberg picture, the creation/annihilation operators evolve as a_H(t) = a e^{-iωt} and a_H†(t) = a† e^{+iωt}. The Hamiltonian becomes H = ℏω(a_H†(t) a_H(t) + 1/2) — time-independent, as expected. Coherent states have expectation values of x_H(t) that oscillate exactly classically: the cleanest demonstration that the Heisenberg picture recovers classical dynamics.

**Sources:** Wikipedia "Interaction picture"; Physics LibreTexts "Schrödinger and Heisenberg Pictures" (Kok); Number Analytics "Mastering Interaction Picture"; Townsend 2nd ed. Ch. 4 (Time Evolution).

---

## B. Domain examples and cases

- **Two-level system (spin precession):** H = ω₀ Ŝ_x, explicit Rabi oscillation ⟨S_z(t)⟩ = (ℏ/2) cos ω₀t. The canonical Schrödinger-picture worked example in the Townsend/Feiguin notes.
- **Free particle:** Heisenberg equations give x_H(t) = x₀ + p₀ t/m, p_H(t) = p₀. Wavepacket spreads in Schrödinger picture; center follows classical trajectory (Ehrenfest). The two pictures give the same expectation values but the Heisenberg picture is manifestly Newton's law.
- **Harmonic oscillator:** Heisenberg picture reduces to coupled classical ODEs for x_H, p_H. Solution is exact: x_H(t) oscillates at ω. Ladder operators: a_H(t) = a e^{-iωt}. Coherent states are exact classical oscillators.
- **Neutral particle in a magnetic field (Larmor precession):** H = −γ B·S. Heisenberg equations give angular-momentum operators precessing around B at the Larmor frequency. The expectation value of S traces a classical precessing cone: Ehrenfest is exact here because the Hamiltonian is linear in S.
- **Time-dependent perturbation theory (interaction picture preview):** Conceptually the bridge to Chapter 9 (perturbation theory). The interaction picture will reappear there explicitly.

---

## C. Connections and dependencies

- **Depends on:** Ch. 1–3 (state, operator, eigenvalue, harmonic oscillator ladder operators). Students must be fluent with the commutator [x, p] = iℏ and with the spectral decomposition of H.
- **Feeds forward to:** Ch. 5–6 (3D Schrödinger equation, angular momentum) — both solved in the Schrödinger picture. Heisenberg picture reappears in perturbation theory (Ch. 9–10) and is the natural language for spin precession and magnetic resonance.
- **Cross-connections:** The Heisenberg equation dA/dt = (i/ℏ)[H, A] is structurally identical to the Poisson bracket {A, H} in classical mechanics (correspondence principle). Conservation laws follow from [H, A] = 0 in quantum mechanics exactly as they follow from {H, A} = 0 classically.
- **The three pictures are all present in the Feiguin/Townsend notes** but not labeled explicitly as "pictures." Section 1.8 of the Townsend notes is the Schrödinger-picture Ehrenfest relation; the Heisenberg picture proper is in Townsend Ch. 4.

---

## D. Current state of the field

The three-pictures framework is completely settled. There is no research frontier here; the framework dates to 1925–1930 (Heisenberg, Born, Jordan, Dirac). What is pedagogically active:

- **Open quantum systems:** In the Heisenberg picture, the equation of motion for operators in a system coupled to an environment becomes the quantum Langevin equation (operator + noise term). This connects naturally to the Lindblad master equation in the Schrödinger picture. The Heisenberg picture for open systems has active applications in quantum optics and quantum information.
- **Quantum computing:** Gate operations are unitary operators applied to states (Schrödinger picture). But noise channels, error propagation, and stabilizer codes are more natural in the Heisenberg picture (how errors on operators propagate forward). The Heisenberg picture of quantum error correction is an active area.

---

## E. Teaching considerations

- **Sequencing:** Most introductory courses (Griffiths) introduce the time-evolution operator without naming it as such, and never explicitly introduce the Heisenberg picture. The Feiguin/Townsend course sequence introduces it in the first chapter. For this vol. 2, students arriving from vol. 1 likely know U(t) but may not have seen the Heisenberg picture systematically. A brief one-paragraph reminder of vol. 1's treatment is warranted.
- **The "picture" terminology is confusing:** Students hear "Schrödinger picture" and think it means "the Schrödinger equation" — which belongs to all three pictures. Be explicit: the term refers to which mathematical objects carry the time dependence.
- **Ladder strategy for Heisenberg ODEs:** Teaching students to derive x_H(t) and p_H(t) by commutator algebra alone (no explicit diagonalization) builds fluency that pays off later for angular momentum and field operators.
- **Ehrenfest as a bridge:** The generalized Ehrenfest theorem (d⟨A⟩/dt = (i/ℏ)⟨[H,A]⟩) can be derived without committing to either picture. It is a good midpoint before the full Heisenberg picture.
- **Worked example for assessment:** The harmonic oscillator in the Heisenberg picture (derive x_H(t) from commutator algebra, no use of energy eigenstates) is the standard exam problem at the graduate level.

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — §1.7 (time-evolution operator, derivation from unitarity), §1.8 (Ehrenfest theorem, generalized form, two-level example). This is the primary local source. The Heisenberg picture is named in the references section but not developed at length in the notes themselves.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — Ch. 4 of the vol. 2 draft covers Dirac notation and Hermiticity. This is a companion chapter (operators, adjoint, spectral theorem) that feeds directly into the operator-evolution formalism of this chapter.
- **Sakurai, *Modern Quantum Mechanics* (Sakurai & Napolitano), "Quantum Dynamics" chapter:** The pantry file at `/Users/bear/Documents/CoWork/bear-textbooks/books/physics-quantum-mechanics-sri/pantry/1013701442-...txt` is a stub/placeholder only (no actual text). Sakurai's "Quantum Dynamics" chapter (Ch. 2 in the book) is the canonical graduate reference for U(t), the three pictures, Ehrenfest, and the Heisenberg picture for the harmonic oscillator.
- **Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., Ch. 4:** Referenced in the Feiguin notes; covers time evolution, two-level dynamics (Townsend Ex. 4.2 is the two-level worked example).

---

## G. Gaps and flags

1. **FLAG — Heisenberg picture is thin locally.** The Townsend/Feiguin notes cover U(t) and the Schrödinger-picture Ehrenfest theorem well (§1.7–1.8), but the Heisenberg picture as a distinct picture (A_H(t) = U†AU, the Heisenberg equation of motion) is not explicitly derived in the local sources. Web sources (Colorado, Illinois, FSU) confirm the standard treatment. The chapter author should develop this from scratch or source Sakurai Ch. 2 directly.
2. **FLAG — Sakurai local file is unusable.** The file at `/books/physics-quantum-mechanics-sri/pantry/1013701442-...txt` contains only a stub/spam placeholder, not the actual book text. Sakurai must be accessed through a library or separate source.
3. **FLAG — Interaction picture (Dirac picture) is mentioned in web sources but not covered in local notes.** The chapter outline does not require it, but it should be at least flagged for students as the bridge to perturbation theory. Consider a "Coming attractions" box.
4. **FLAG — No local worked example for the harmonic oscillator in the Heisenberg picture.** The two-level Rabi example is in the Townsend notes; the free-particle and oscillator Heisenberg equations are standard but need to be drafted for the chapter.
5. **Note on chapter numbering:** The existing vol. 2 draft has Ch. 4 as "Formalism: Dirac Notation and Operators." If "Quantum Dynamics and the Pictures" is to be Ch. 4, the chapter ordering needs reconciliation. Confirm TOC before drafting.

---

**Web sources consulted:**
- [Heisenberg picture — Wikipedia](https://en.wikipedia.org/wiki/Heisenberg_picture)
- [Schrödinger picture — Wikipedia](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_picture)
- [The Heisenberg Picture — University of Colorado Phys 5250](https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec10-heisenberg-picture/)
- [The Heisenberg Picture — UCSD 130a notes](https://quantummechanics.ucsd.edu/ph130a/130_notes/node191.html)
- [Schrödinger and Heisenberg Pictures — Physics LibreTexts (Kok)](https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Advanced_Quantum_Mechanics_(Kok)/03:_Schrodinger_and_Heisenberg_Pictures)
- [The Heisenberg Picture: Equations of Motion — FSU Physics Wiki](http://wiki.physics.fsu.edu/wiki/index.php/The_Heisenberg_Picture:_Equations_of_Motion_for_Operators)
- [Heisenberg Representation — University of Illinois Phys 580 PDF](https://courses.physics.illinois.edu/phys580/fa2013/heisenberg.pdf)
- [Ehrenfest's Theorem — Fitzpatrick, UT Austin](https://farside.ph.utexas.edu/teaching/qmech/Quantum/node36.html)
- [Ehrenfest theorem — Wikipedia](https://en.wikipedia.org/wiki/Ehrenfest_theorem)
- [Interaction picture — Wikipedia](https://en.wikipedia.org/wiki/Interaction_picture)
