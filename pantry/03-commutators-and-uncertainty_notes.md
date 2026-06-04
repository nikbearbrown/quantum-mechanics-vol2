# Research Notes: Chapter 03 — Commutators and Uncertainty

**Corresponding chapter:** chapters/03-commutators-and-uncertainty.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter students can: (1) compute commutators of operators by applying them to a test function; (2) explain why commuting operators have a simultaneous eigenbasis and non-commuting operators do not; (3) derive the canonical commutation relation [x̂, p̂] = iℏ from scratch; (4) state and prove the Robertson generalized uncertainty principle σA σB ≥ |⟨[Â,B̂]⟩|/2; (5) recover σx σp ≥ ℏ/2 as a corollary; and (6) identify the operational meaning of the uncertainty bound — it is a property of the state, not a consequence of measurement disturbance.

---

## A. Conceptual foundations

### A1. Commutators measure the failure of simultaneous diagonalizability

**Explanation.** The commutator of two operators is [Â,B̂] = ÂB̂ − B̂Â. If [Â,B̂] = 0 (they commute), there exists a common orthonormal eigenbasis {|n⟩} such that Â|n⟩ = aₙ|n⟩ and B̂|n⟩ = bₙ|n⟩ simultaneously. In such a state the system has definite values for both A and B: no uncertainty arises from the quantum state (only from classical ignorance of which eigenstate the system is in). If [Â,B̂] ≠ 0, no common eigenbasis exists; for any state |ψ⟩ that is sharp in A (an eigenstate of Â), the spread σB > 0. The commutator is thus the algebraic signature of incompatibility.

**Proof that [Â,B̂] = 0 implies shared eigenbasis (sketch).** Suppose Â|a⟩ = a|a⟩. Apply B̂: B̂(Â|a⟩) = aB̂|a⟩. But ÂB̂ = B̂Â, so Â(B̂|a⟩) = a(B̂|a⟩). Thus B̂|a⟩ is also an eigenstate of Â with eigenvalue a. If a is non-degenerate, B̂|a⟩ ∝ |a⟩, i.e., |a⟩ is an eigenstate of B̂. If a is degenerate, B̂ maps the eigenspace of Â back to itself; diagonalize B̂ within that subspace by Gram–Schmidt.

**Common misconception.** "If [Â,B̂] ≠ 0, you can never measure both A and B." This confuses "cannot simultaneously have definite values" with "cannot measure both in one experiment." You can measure Â on one copy of the state and B̂ on another copy; what you cannot do is find a state with σA = σB = 0. The Robertson bound says the product σA σB has a lower limit set by the state — it does not prevent measurement.

**Worked example.** [Ŝx, Ŝz] for spin-1/2. Using σx = (ℏ/2)[[0,1],[1,0]] and σz = (ℏ/2)[[1,0],[0,−1]]:
[Ŝx, Ŝz] = (ℏ²/4)([[0,1],[1,0]][[1,0],[0,−1]] − [[1,0],[0,−1]][[0,1],[1,0]])
= (ℏ²/4)([[0,−1],[1,0]] − [[0,1],[−1,0]]) = (ℏ²/4)[[0,−2],[2,0]] = −iℏ Ŝy.
(From Townsend notes §1.6, with exact matching computation shown there.)
Since [Ŝx, Ŝz] ≠ 0, Ŝx and Ŝz cannot share an eigenbasis — consistent with the fact that the eigenstates of σz (|↑⟩, |↓⟩) are superpositions in the σx eigenbasis.

**Sources.**
- Primary draft §"Commutators and why they matter" — definition, physical interpretation; the shared eigenbasis theorem stated.
- Townsend notes §1.6 "The generalized uncertainty principle" — the [Ŝx, Ŝz] = −iℏŜy calculation done explicitly.
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2021), §1.4 "Compatible Observables" — proof that [Â,B̂] = 0 iff shared eigenbasis; carefully handles the degenerate case.

---

### A2. The canonical commutation relation [x̂, p̂] = iℏ

**Explanation.** This is the algebraic heart of quantum mechanics. Derive it by applying the commutator to a test function ψ(x):
[x̂, p̂]ψ = x̂(−iℏ∂xψ) − (−iℏ∂x)(xψ)
= −iℏx∂xψ − (−iℏ)(ψ + x∂xψ) [product rule on second term]
= −iℏx∂xψ + iℏψ + iℏx∂xψ
= iℏψ.
Since this holds for all ψ: [x̂, p̂] = iℏ.
This single relation — together with the Schrödinger equation — generates all of non-relativistic quantum mechanics. Dirac recognized it as the quantization rule: replace the classical Poisson bracket {x, p} = 1 with [x̂, p̂]/iℏ = 1.

**Common misconception.** "The [x̂, p̂] = iℏ is just a definition, not something that can be derived." It is not a definition — it is a consequence of the position and momentum operator representations (x̂ = multiplication by x, p̂ = −iℏ∂x), which are themselves derived from the requirement that p̂ generates translations and has the correct classical limit. Alternatively, it follows from the Fourier-transform relationship between position and momentum eigenbases (Ch. 01). The test-function derivation in the chapter makes all the algebra explicit.

**Worked example.** Verify [x̂², p̂] = 2iℏx̂.
[x̂², p̂]ψ = x²(−iℏ∂xψ) − (−iℏ∂x)(x²ψ)
= −iℏx²∂xψ + iℏ(2xψ + x²∂xψ)
= 2iℏxψ.
So [x̂², p̂] = 2iℏx̂. This illustrates the general rule [x̂ⁿ, p̂] = iℏnx̂ⁿ⁻¹, which is the quantum analogue of the classical Poisson bracket {xⁿ, p} = nxⁿ⁻¹.

**Worked example (from primary draft, Exercise 4.3).** Verify [x̂, p̂] = iℏ and compare with [x̂, ℏ∂x] = −ℏ (if the factor of i were absent from p̂, the commutator would be −ℏ, a real number, and the operator ℏ∂x would be anti-Hermitian with imaginary eigenvalues).

**Sources.**
- Primary draft §"Commutators and why they matter" — full test-function derivation with every step of the product rule explicit.
- Townsend notes §1.6 — [x̂, p̂] = iℏ derived immediately before applying the Robertson formula.
- Sakurai §1.6 "Position, Momentum, and Translation" — derives [x̂, p̂] = iℏ from the translation operator; more foundational approach.
- Griffiths §3.3 — elementary test-function derivation matching the level of this chapter.

---

### A3. The generalized uncertainty principle (Robertson 1929)

**Explanation.** **Theorem (Robertson).** For any two Hermitian operators Â, B̂ and any normalized state |ψ⟩:
σA σB ≥ (1/2)|⟨[Â,B̂]⟩|
where σA² = ⟨Â²⟩ − ⟨Â⟩², and |⟨[Â,B̂]⟩| is the modulus of the expectation value of the commutator.

**Derivation skeleton.**
1. Define Â' = Â − ⟨Â⟩, B̂' = B̂ − ⟨B̂⟩. Then σA² = ⟨Â'²⟩ = ‖Â'|ψ⟩‖², σB² = ‖B̂'|ψ⟩‖².
2. Cauchy–Schwarz: σA²σB² ≥ |⟨ψ|Â'B̂'|ψ⟩|².
3. Write Â'B̂' = (1/2){Â',B̂'} + (1/2)[Â',B̂']. The first (anticommutator) term has real expectation value; the second (commutator) has purely imaginary expectation value (since [Â',B̂'] = [Â,B̂] is anti-Hermitian when Â,B̂ are Hermitian).
4. |⟨Â'B̂'⟩|² = (1/4)|⟨{Â',B̂'}⟩|² + (1/4)|⟨[Â,B̂]⟩|².
5. Drop the first (non-negative) term: σA²σB² ≥ (1/4)|⟨[Â,B̂]⟩|².
6. Take the square root: σA σB ≥ (1/2)|⟨[Â,B̂]⟩|. □

This matches the formulation in Townsend notes §1.6, cited as "Townsend 3.5" in the text: σA σB ≥ |⟨[Â,B̂]⟩/2i| (equivalent, since the commutator of two Hermitian operators is anti-Hermitian and therefore iλ for real λ, so |⟨[Â,B̂]⟩/2i| = |⟨[Â,B̂]⟩|/2).

**Corollary — position-momentum.** Substituting Â = x̂, B̂ = p̂, [x̂,p̂] = iℏ: ⟨[x̂,p̂]⟩ = iℏ (state-independent); |⟨[x̂,p̂]⟩|/2 = ℏ/2. Therefore σx σp ≥ ℏ/2 for every state. This is the Heisenberg uncertainty relation as a theorem.

**Common misconception.** "The uncertainty principle says measuring position disturbs momentum." This is the Heisenberg microscope story — useful intuition but not the theorem. Robertson's result (1929) says nothing about measurement disturbance. It says: prepare N copies of |ψ⟩, measure x̂ on N/2 and p̂ on the other N/2 — no copy is measured twice — and the sample standard deviations satisfy σx σp ≥ ℏ/2. The bound is a property of the state before any measurement takes place. The operational meaning is stated explicitly in the primary draft and Townsend notes §1.6: "This is a derived result of the theory, not a postulate."

**Sources.**
- **Primary source:** Robertson, H. P., "The uncertainty principle," Phys. Rev. 34, 163 (1929). https://doi.org/10.1103/PhysRev.34.163 — the original paper; one page; readable at the undergraduate level.
- Townsend notes §1.6 — cited in the text as "Townsend §3.5"; contains the Schwartz-inequality derivation and the explicit [Ŝx, Ŝz] spin example.
- Primary draft §"Commutators and why they matter" — full Robertson derivation with the anticommutator decomposition spelled out; the "no copy is measured twice" operational language.
- Sakurai §1.4 "The Uncertainty Relation" — derivation using Cauchy–Schwarz; also derives the tighter Schrödinger uncertainty relation retaining the anticommutator term.

---

### A4. Compatible observables and simultaneous eigenbases

**Explanation.** Two Hermitian operators Â and B̂ are **compatible** if [Â,B̂] = 0. Compatible observables can be simultaneously diagonalized: there exists a basis {|n⟩} with Â|n⟩ = aₙ|n⟩ and B̂|n⟩ = bₙ|n⟩. A state |ψ⟩ in a simultaneous eigenstate has definite values for both A and B: σA = σB = 0, consistent with σA σB ≥ 0 (the Robertson bound is trivially zero when [Â,B̂] = 0). In quantum mechanics, exploiting compatible observables is the key to labeling states: the hydrogen atom eigenstates are labeled by (n, l, m) because Ĥ, L², and Lz are mutually commuting.

**Complete set of commuting observables (CSCO).** A CSCO is a maximal set of mutually commuting Hermitian operators whose simultaneous eigenstates are non-degenerate (uniquely labeled by the eigenvalue tuple). For the hydrogen atom without spin: {Ĥ, L², Lz} is a CSCO. Adding spin: {Ĥ, L², Lz, Ŝz} or {Ĥ, J², Jz, L²}. The CSCO concept is one of the most important structural ideas in quantum mechanics.

**Common misconception.** "Two operators commute iff they are proportional." False: σx and σz do not commute; Ĥ and L² for the hydrogen atom do commute even though one involves kinetic + Coulomb energy and the other angular derivatives only. Commutativity is a property of the operator algebra, not of the "type" of operator.

**Worked example.** For a 1D harmonic oscillator, [Ĥ, x̂] ≠ 0 (Ĥ = p̂²/2m + mω²x̂²/2, so [Ĥ, x̂] = [p̂²/2m, x̂] = (1/2m)[p̂², x̂] = (1/2m)(p̂[p̂,x̂] + [p̂,x̂]p̂) = −iℏp̂/m). Since [Ĥ, x̂] ≠ 0, x̂ is not a constant of motion; ⟨x̂⟩ oscillates. By Ehrenfest: d⟨x̂⟩/dt = (i/ℏ)⟨[Ĥ,x̂]⟩ = ⟨p̂⟩/m. On the other hand [Ĥ, N̂] = 0 where N̂ = â†â is the number operator — N̂ is a constant of motion.

**Sources.**
- Townsend notes §1.6 "Operators that commute" — explicit statement and the connection to simultaneous eigenvectors.
- Primary draft §"Commutators and why they matter" — "If they commute, they share a common eigenbasis, and you can simultaneously assign definite values to both observables."
- Sakurai §1.4 "Compatible Observables" — the CSCO concept introduced; hydrogen atom as the main example.

---

### A5. The state-dependence of the uncertainty bound

**Explanation.** Unlike σx σp ≥ ℏ/2 (where the commutator is a c-number so the bound is state-independent), for operators whose commutator depends on the state, the Robertson bound ≥ (1/2)|⟨[Â,B̂]⟩| is state-dependent. This is pedagogically important: the bound is not a fixed number but a function of the state being prepared. For Ŝx and Ŝz: [Ŝx, Ŝz] = −iℏŜy, so σSx σSz ≥ (ℏ/2)|⟨Ŝy⟩|. If the state is an eigenstate of Ŝy, the bound is maximized; if ⟨Ŝy⟩ = 0, the bound is zero (consistent with any product of spreads, including both equal to zero — but the zero bound is not a guarantee of zero spread, only that the bound does not forbid it).

**Common misconception.** "When the Robertson bound is zero, both observables can be simultaneously sharp." Not necessarily. The bound [Ŝx,Ŝz] gives zero when ⟨Ŝy⟩ = 0. The state (|+y⟩ + |−y⟩)/√2 has ⟨Ŝy⟩ = 0 but σSx ≠ 0 and σSz ≠ 0 — the bound is zero but the spreads are not. The zero bound means "the Robertson inequality does not constrain the product from below"; it does not mean both spreads are zero.

**Worked example (qubit, from primary draft §"The qubit").** State |+y⟩ = (|0⟩ + i|1⟩)/√2. Compute [σx,σz] = −2iσy, so the Robertson bound for σx and σz is |⟨σy⟩|. In state |+y⟩: ⟨σy⟩ = 1, so σSx σSz ≥ 1. Compute explicitly: ⟨σx⟩ = 0 (|+y⟩ is on the equator at φ = π/2, so sin θ cos φ = sin(π/2)cos(π/2) = 0), ⟨σx²⟩ = 1, so σSx = 1. Similarly σSz = 1. Product = 1 ≥ 1. Bound is saturated. This is the σy eigenstate example from Townsend notes §1.6 generalized from spin components Sx,Sy to σx,σz.

**Sources.**
- Townsend notes §1.6 — [Ŝx,Ŝz] = −iℏŜy example with explicit numerical bound; the state-dependence of the bound.
- Primary draft §"The qubit" — table of Robertson bound values for various qubit states on the Bloch sphere; "the bound is state-dependent, not a fixed number."
- Kennard, E. H., "Zur Quantenmechanik einfacher Bewegungstypen," Z. Phys. 44, 326 (1927). https://doi.org/10.1007/BF01391200 — first proof of σx σp ≥ ℏ/2 (predates Robertson's general theorem by two years).

---

## B. Domain examples and cases

**B1. Angular momentum commutators — preview of Ch. 05.**
[L̂x, L̂y] = iℏL̂z (cyclically). Therefore σLx σLy ≥ (ℏ/2)|⟨L̂z⟩|. In an eigenstate |l,m⟩ of L̂z: ⟨L̂z⟩ = ℏm, so σLx σLy ≥ (ℏ²/2)|m|. The |l,l⟩ state has σLx = σLy = ℏ√(l/2) and the bound is saturated (from Townsend notes §1.11). This previews angular momentum without requiring it.

**B2. Energy–time uncertainty relation — ΔE Δt ≥ ℏ/2.**
This is not derived from the Robertson theorem (time is not an operator in NRQM). It has a different status: Δt is the time for the state to change appreciably; ΔE is the energy spread of the state. It follows from the time-evolution formula |ψ(t)⟩ = Σcₙe^{−iEₙt/ℏ}|Eₙ⟩ and the spread of the energy eigenvalue distribution. Worth flagging as "looks like the Robertson bound, is not."

**B3. Number–phase uncertainty — ΔN Δφ ≥ 1.**
Analogous relation for number of photons and phase of a coherent state. Pedagogically useful as an example of Robertson-style reasoning in a different context; technically subtle (phase is not a Hermitian operator). Reserve for advanced problems.

**B4. σy as the sign-error trap.**
The calculation of [σx, σz] involves σy, which has −i in the (1,2) position and +i in the (2,1) position. Students who write σy = [[0,i],[−i,0]] (the wrong sign, a common LLM and student error identified in the primary draft) get [σx, σz] = +2iσy instead of −2iσy, and subsequent Robertson-bound calculations are wrong. This is the canonical check: compute [σx, σz] explicitly and verify the sign.

**B5. The qubit Robertson bound — saturating the inequality.**
The Robertson bound is saturated (σA σB = (1/2)|⟨[Â,B̂]⟩|) when the anticommutator term in step (4) of the derivation is zero: ⟨{Â',B̂'}⟩ = 0. For the qubit σx and σz, this is satisfied exactly at the σy eigenstates. Students can verify saturation explicitly from the Bloch sphere simulation.

---

## C. Connections and dependencies

**Prerequisites.**
- Ch 01 (The Formalism): operator algebra — ÂB̂ is defined; basis expansion.
- Ch 02 (Observables and the Spectral Theorem): eigenstates, eigenvalues, spectral decomposition — needed for "compatible observables share an eigenbasis."
- Cauchy–Schwarz inequality: ‖u‖·‖v‖ ≥ |⟨u|v⟩| — must be stated and proved or assumed.

**Unlocks.**
- Angular momentum (Ch 04/05 in this volume): [L̂x, L̂y] = iℏL̂z is the algebraic input; all ladder-operator results follow from commutator algebra.
- Ehrenfest theorem and equations of motion: d⟨Â⟩/dt = (i/ℏ)⟨[Ĥ,Â]⟩ + ⟨∂Â/∂t⟩ — the commutator is the generator of time dependence.
- Symmetries and conservation laws: [Ĥ,Â] = 0 iff A is a constant of motion — commutator as the definition of a conserved quantity.
- Constants of motion and selection rules: [Ĥ,L̂z] = 0 ⟹ m is a good quantum number ⟹ selection rules Δm = 0, ±1 for perturbations.

**Adjacent chapters.**
- The qubit (Ch 01, Ch 02): all the explicit commutator examples in this chapter use 2×2 Pauli matrices — same material, deeper layer.
- The CSCO concept built here is the key to labeling hydrogen atom states in Ch 07.
- Perturbation theory (later volume): degenerate perturbation theory requires choosing a basis within the degenerate subspace that diagonalizes the perturbation — this is exactly the "compatible observable" problem.

---

## D. Current state of the field

**Settled.** The Robertson uncertainty principle is a theorem of quantum mechanics — not contested. Its proof, interpretation, and scope are all settled.

**Active research area — uncertainty relations beyond Robertson.** The Robertson bound is not always the tightest possible. The Schrödinger uncertainty relation (retaining the anticommutator term) is tighter:
σA² σB² ≥ (1/4)|⟨{Â',B̂'}⟩|² + (1/4)|⟨[Â,B̂]⟩|².
Beyond this, there is active research (2010s–present) on entropic uncertainty relations:
H(A) + H(B) ≥ log(1/c), where H is Shannon entropy and c = max|⟨aᵢ|bⱼ⟩|² (Maassen–Uffink bound).
- Maassen & Uffink, Phys. Rev. Lett. 60, 1103 (1988). https://doi.org/10.1103/PhysRevLett.60.1103 — the original entropic uncertainty relation.
- Coles et al., "Entropic uncertainty relations and their applications," Rev. Mod. Phys. 89, 015002 (2017). https://doi.org/10.1103/RevModPhys.89.015002 — comprehensive review; accessible for advanced undergraduates.

**Contested — interpretation of the uncertainty principle.**
The "disturbance" interpretation (Heisenberg microscope) is not a theorem. There are "measurement–disturbance" relations (Ozawa 2003; Busch et al. 2013) that formalize the idea rigorously, but they are distinct from the Robertson preparation uncertainty. This distinction matters pedagogically:
- Ozawa, M., "Universally valid reformulation of the Heisenberg uncertainty principle," Phys. Rev. A 67, 042105 (2003). https://doi.org/10.1103/PhysRevA.67.042105
- Busch, Lahti & Werner, "Proof of Heisenberg's error-disturbance relation," Phys. Rev. Lett. 111, 160405 (2013). https://doi.org/10.1103/PhysRevLett.111.160405

**Key references.**
- Robertson (1929) — original.
- Kennard (1927) — first proof of σx σp ≥ ℏ/2.
- Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed. (University Science Books, 2012), §3.5 (cited as "Townsend 3.5" in the notes).
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2021), §1.4.
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge, 2018), §3.5 — clear undergraduate treatment with examples.

---

## E. Teaching considerations

**Start with the disturbance misconception, then demolish it.** Open with Heisenberg's microscope story: locating an electron with a photon kicks it. Students know this story and believe it. Then show them Robertson's 1929 derivation: no photon, no kick, no disturbance — just Cauchy–Schwarz and the commutator. The contrast is memorable.

**The operational meaning is crucial.** The primary draft's "no copy is measured twice" language is exactly right. Emphasize it: prepare N copies, measure A on half, B on the other half, compute sample standard deviations. The bound is already there, set by the state, before any measurement takes place.

**The test-function derivation of [x̂,p̂] = iℏ must be done by hand, on the board.** Students should be able to reproduce it in 3 minutes. Every step (apply x̂, apply p̂, product rule, cancel terms) must be explicit. This is Exercise 4.3 in the primary draft.

**The Robertson derivation — teach the structure, not just the result.** The four steps (define shifted operators, Cauchy–Schwarz, decompose into symmetric/antisymmetric parts, drop the non-negative term) each have a name and a purpose. Students who know the structure can reconstruct the proof; students who only know the formula cannot.

**The state-dependent bound — use the Bloch sphere.** The qubit example (bound is |⟨σy⟩|, which ranges from 0 at the poles to 1 at the equatorial σy eigenstates) is vivid on the Bloch sphere simulation. A state at the north pole has zero bound (σz eigenstate, σSz = 0, so the product is trivially zero); a state at the equatorial σy eigenstate saturates the bound. The simulation makes this palpable.

**Do not open the measurement-problem door.** The uncertainty principle does not, by itself, say anything about what happens to the state after measurement. That is the measurement problem (collapse, branching, etc.) and belongs in a dedicated discussion. Students who ask "but after I measure x, I know x exactly — doesn't that violate the bound?" should be told: after measurement, the state has changed; the bound applies to the new state, not the old one.

**Flag the CSCO concept explicitly.** Students may not realize that [L², Lz] = 0 is why both l and m are good quantum numbers simultaneously. Draw the line explicitly from "commuting operators share an eigenbasis" to "l and m label the same eigenstate."

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — §"Commutators and why they matter": [x̂,p̂] = iℏ derivation, Robertson uncertainty principle full derivation, the qubit Robertson example with state-dependent bound.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — §1.6 "The generalized uncertainty principle" (cited as Townsend §3.5): Schwartz-inequality derivation, [Ŝx,Ŝz] = −iℏŜy spin example, state with ⟨Ŝy⟩ = 0 giving a vanishing bound; §1.8 "Time-dependence of expectation values" — Ehrenfest theorem as the commutator connection to dynamics; §1.11 "Angular momentum" — [L̂x, L̂y] = iℏL̂z and the uncertainty relation for angular momentum.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-05-quantum-mechanics-in-three-dimensions.md` — downstream; uses [x̂ᵢ, p̂ⱼ] = iℏδᵢⱼ in 3D.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-06-spin.md` — downstream; Pauli commutators [σᵢ, σⱼ] = 2iεᵢⱼₖσₖ are used throughout.

---

## G. Gaps and flags

**Gap — the Cauchy–Schwarz inequality needs a proof or reference.** The Robertson derivation uses ‖u‖·‖v‖ ≥ |⟨u|v⟩| without proof. For students who have not seen it in a linear algebra course, include a one-paragraph proof in a boxed aside or appendix: ‖u − λv‖² ≥ 0 for all λ, choose λ = ⟨v|u⟩/‖v‖², expand, get the result.

**Gap — the dropped anticommutator term.** The Robertson bound drops (1/4)|⟨{Â',B̂'}⟩|², making it weaker than the Schrödinger bound. This is mentioned in primary draft Exercise 4.10 (Challenge). The chapter should at minimum note that the dropped term is non-negative (so the inequality is valid) and that the Schrödinger relation is tighter. The saturation condition (anticommutator term = 0) determines which states saturate the Robertson bound.

**Gap — the CSCO concept is not defined here.** The "complete set of commuting observables" label is used implicitly throughout quantum mechanics but not formally introduced. This chapter is the right place to define it, since it is a direct consequence of the commuting-operators theorem.

**Flag — the [x̂,p̂] = iℏ derivation uses distributions implicitly.** When p̂ acts on x·ψ, the product rule ∂x(xψ) = ψ + x∂xψ requires ψ to be differentiable. For ψ ∈ L²(ℝ) this is not always the case. For this course, the derivation is valid as stated; flag for mathematically careful students that the rigorous version uses the Sobolev space domain of p̂.

**Flag — energy–time uncertainty.** The relation ΔE·Δt ≥ ℏ/2 is commonly cited but does not follow from the Robertson theorem (time is not an observable-operator in NRQM). Add a brief note distinguishing it from the Robertson result. Students will ask.

**Flag — the Sakurai .txt in physics-quantum-mechanics-sri pantry is a corrupted placeholder.** Do not cite it. Use Sakurai from library access (3rd ed., Cambridge, 2021).
