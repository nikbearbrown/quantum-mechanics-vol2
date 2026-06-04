# Research Notes: Chapter 02 — Observables and the Spectral Theorem

**Corresponding chapter:** chapters/02-observables-and-the-spectral-theorem.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

By the end of this chapter students can justify from first principles why observables must be represented by Hermitian operators — not as a postulate but as a logical necessity given that measurement outcomes are real. They can prove the two main theorems (real eigenvalues; orthogonal eigenstates for distinct eigenvalues), state the spectral decomposition, use projectors to compute Born-rule probabilities, handle degenerate subspaces by invoking Gram–Schmidt, and diagonalize a concrete 2×2 Hermitian operator by hand.

---

## A. Conceptual foundations

### A1. Why observables must be Hermitian — the physical argument

**Explanation.** A physical observable is a quantity whose measured values are real numbers. If Â represents an observable and |ψ⟩ is any state, the expectation value ⟨Â⟩ = ⟨ψ|Â|ψ⟩ must be real. Reality of the expectation value for every |ψ⟩ is equivalent to the operator condition Â = Â† (Hermitian / self-adjoint). This is not a convention; it is the minimum requirement. The argument: ⟨Â⟩* = ⟨ψ|Â|ψ⟩* = ⟨ψ|Â†|ψ⟩, so ⟨Â⟩ = ⟨Â⟩* for all |ψ⟩ iff Â = Â†.

**Common misconception.** Students treat "observables are Hermitian" as an unexplained postulate handed down from authority. This creates a cargo-cult relationship with the framework — students follow the rule without understanding why any non-Hermitian operator would fail as an observable. The fix: derive it from "measurement outcomes are real," which students accept without question.

**Worked example.** Is the operator Ĝ = [[1, 2i],[−2i, 1]] (in the {|1⟩, |2⟩} basis) an observable? Compute Ĝ† = (Ĝ*)ᵀ = [[1, −2i],[2i, 1]] ≠ Ĝ. Not Hermitian. Compute ⟨1|Ĝ|2⟩ = 2i (complex); this would be a contribution to an expectation value — not guaranteed real. Conclusion: Ĝ cannot represent an observable. Contrast with Ĝ_H = [[1, 2i],[−2i, 1]] — wait, that example fails; use instead  Ĝ_H = [[1, i],[−i, 1]]: Ĝ_H† = [[1, i],[−i, 1]] = Ĝ_H. Hermitian. Expectation values are real.

**Sources.**
- Townsend notes §1.2 "Observables and operators" — exactly this argument: "Because a measurement must yield a real number, we require ⟨O⟩ ∈ ℝ for every state |ψ⟩."
- Primary draft §"Operators and Hermiticity" — "Measurement outcomes are real numbers, so observables must be Hermitian operators. This is not a convention; it is the reason the framework is built this way."
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2021), §1.3 — postulates stated; Hermiticity of observables motivated by reality of eigenvalues.

---

### A2. Real eigenvalues — the proof and why it fails without Hermiticity

**Explanation.** **Theorem.** If Â is Hermitian and Â|a⟩ = a|a⟩, then a ∈ ℝ.
**Proof.** Compute ⟨a|Â|a⟩ two ways:
(i) Â|a⟩ = a|a⟩ ⟹ ⟨a|Â|a⟩ = a⟨a|a⟩ = a (since ⟨a|a⟩ = 1).
(ii) ⟨a|Â = ⟨a|Â† = ⟨Â a| ⟹ ⟨a|Â|a⟩ = ⟨Â a|a⟩ = a*⟨a|a⟩ = a*.
Therefore a = a*, so a ∈ ℝ. If Â were not Hermitian, step (ii) would give a* ≠ a in general — complex eigenvalues, complex measurement outcomes. The proof is four lines; students should memorize the structure.

**Common misconception.** "The eigenvalues of a matrix are always real if its entries are real." False: [[0,1],[−1,0]] has entries ±1 (real) but eigenvalues ±i (imaginary). Hermiticity (not real entries) is what guarantees real eigenvalues. The matrix σy = [[0,−i],[i,0]] has complex entries but real eigenvalues ±1 because it is Hermitian.

**Worked example.** Diagonalize σx = [[0,1],[1,0]].
Secular equation: det(σx − λI) = λ² − 1 = 0 ⟹ λ = ±1 (real, as guaranteed).
For λ = +1: eigenvector (1/√2)(1,1)ᵀ = |+x⟩.
For λ = −1: eigenvector (1/√2)(1,−1)ᵀ = |−x⟩.
Check: σx|+x⟩ = |+x⟩ ✓; σx|−x⟩ = −|−x⟩ ✓.
This example directly from Townsend notes §1.4 (the S⁺ + S⁻ = σx diagonalization).

**Sources.**
- Townsend notes §1.4 "The eigenvalue problem" — proof of real eigenvalues; the σx example.
- Primary draft §"Operators and Hermiticity" — "If Â|a⟩ = a|a⟩, take the inner product of both sides with ⟨a| and use the Hermitian property to show a = a*."
- Shankar, *Principles of Quantum Mechanics*, 2nd ed. (Springer, 1994), §1.5 — proof stated and the non-Hermitian counterexample made explicit.

---

### A3. Orthogonality of eigenstates with distinct eigenvalues

**Explanation.** **Theorem.** If Â is Hermitian, Â|a⟩ = a|a⟩, Â|a'⟩ = a'|a'⟩, and a ≠ a', then ⟨a|a'⟩ = 0.
**Proof.** Compute ⟨a|Â|a'⟩ two ways:
(i) ⟨a|Â|a'⟩ = a'⟨a|a'⟩.
(ii) ⟨a|Â|a'⟩ = ⟨Âa|a'⟩ = a*⟨a|a'⟩ = a⟨a|a'⟩ (since a is real).
Therefore (a' − a)⟨a|a'⟩ = 0. Since a' ≠ a, we have ⟨a|a'⟩ = 0.
The proof fails when a = a' (degeneracy): both steps are consistent with any value of ⟨a|a'⟩. In the degenerate subspace, Gram–Schmidt orthogonalization must be applied explicitly.

**Common misconception.** "Degenerate eigenstates are automatically orthogonal." They are not — any linear combination of degenerate eigenstates is also an eigenstate with the same eigenvalue. The theorem guarantees that we can *choose* an orthonormal set within each degenerate subspace (by Gram–Schmidt), but the diagonalization does not do it automatically.

**Worked example.** The identity operator Î on a 2D space has both eigenvalues equal to 1 (doubly degenerate). Every vector is an eigenvector. The states |1⟩ = (1,0)ᵀ and |2⟩ = (0,1)ᵀ are orthogonal; so are |+⟩ = (1/√2)(1,1)ᵀ and |−⟩ = (1/√2)(1,−1)ᵀ. Both are valid orthonormal eigenbases. The Gram–Schmidt procedure starting from any two linearly independent vectors produces an orthonormal eigenbasis, but the choice is not unique.

**Sources.**
- Townsend notes §1.4 — proof of orthogonality with exact matching algebra to what is written above; degeneracy handled in the concluding remark.
- Primary draft §"Operators and Hermiticity" — "if Â|a⟩ = a|a⟩ and Â|a'⟩ = a'|a'⟩ with a ≠ a', then ⟨a|a'⟩ = 0."
- Sakurai §1.4 "Eigenkets of Observable" — discusses the degenerate case and the non-uniqueness of the eigenbasis.

---

### A4. The spectral theorem and spectral decomposition

**Explanation.** **Spectral theorem (for finite-dimensional Hermitian operators, or bounded self-adjoint operators on Hilbert space).** Every Hermitian operator Â has a complete orthonormal set of eigenstates {|aₙ⟩} spanning H, and can be written in its spectral decomposition:
Â = Σₙ aₙ |aₙ⟩⟨aₙ|.
Each term Pₙ = |aₙ⟩⟨aₙ| is a **projector** onto the eigenspace with eigenvalue aₙ: Pₙ² = Pₙ, Pₙ† = Pₙ. The Born rule probability P(aₙ) = ⟨ψ|Pₙ|ψ⟩ = |⟨aₙ|ψ⟩|². The spectral decomposition is the coordinate-free statement of diagonalization: Â is diagonal in its own eigenbasis, with the eigenvalues on the diagonal.

**Common misconception.** Students think the spectral decomposition is only useful when you know the eigenstates in advance. In fact, the value is the reverse: the theorem guarantees that eigenstates exist and form a basis, so you can always work in the eigenbasis. Once you know you can expand |ψ⟩ = Σcₙ|aₙ⟩, the Born rule, time evolution, and perturbation theory all follow.

**Worked example.** Diagonalize the 2×2 Hermitian observable Ĥ = ε[[1, e^{−iφ}],[e^{iφ}, −1]] (ε > 0, real).
Secular equation: det(Ĥ − λI) = −ε² − λ² + ε²(e^{iφ}·e^{−iφ}) = −λ² + ε²(1 − 1) ... let's use a cleaner example.

**Worked example (clean).** Diagonalize Ĥ = (ℏω/2)σz = (ℏω/2)[[1,0],[0,−1]].
Eigenvalues: ±ℏω/2. Eigenstates: |+⟩ = |0⟩ = (1,0)ᵀ (eigenvalue +ℏω/2), |−⟩ = |1⟩ = (0,1)ᵀ (eigenvalue −ℏω/2).
Spectral decomposition: Ĥ = (ℏω/2)|0⟩⟨0| − (ℏω/2)|1⟩⟨1|.
Verify: (ℏω/2)[[1,0],[0,0]] − (ℏω/2)[[0,0],[0,1]] = (ℏω/2)[[1,0],[0,−1]] ✓.
Projectors: P₊ = |0⟩⟨0| = [[1,0],[0,0]], P₋ = |1⟩⟨1| = [[0,0],[0,1]]. Check P₊ + P₋ = I ✓.

**Worked example (off-diagonal).** Diagonalize Â = [[2, 1],[1, 2]].
Secular equation: (2−λ)² − 1 = 0 ⟹ λ = 3 or λ = 1.
For λ₁ = 3: (1/√2)(1,1)ᵀ. For λ₂ = 1: (1/√2)(1,−1)ᵀ.
Spectral decomposition: Â = 3·(1/2)[[1,1],[1,1]] + 1·(1/2)[[1,−1],[−1,1]] = (3/2)[[1,1],[1,1]] + (1/2)[[1,−1],[−1,1]].
Verify: sum = [[2,1],[1,2]] ✓.

**Sources.**
- Townsend notes §1.4 and §1.5 — eigenvalue problem and Born rule stated in spectral form; the S⁺ + S⁻ = σx example provides a clean 2×2 diagonalization.
- Primary draft §"Operators and Hermiticity" — spectral theorem stated as "the eigenstates of any Hermitian operator form a complete orthonormal basis"; the spectral decomposition formula given.
- Sakurai §1.4 — the spectral decomposition written as Â = Σₐ a|a⟩⟨a|; projector formalism developed fully.
- Cohen-Tannoudji et al., *Quantum Mechanics*, Vol. I (Wiley, 1977), §EII and §FIII — the most thorough undergraduate-accessible proof of the spectral theorem.

---

### A5. Projectors and the Born rule as geometric projection

**Explanation.** The Born rule P(aₙ) = |⟨aₙ|ψ⟩|² is the squared length of the projection of |ψ⟩ onto the eigenstate |aₙ⟩. The projector Pₙ = |aₙ⟩⟨aₙ| is the operator that implements this projection: Pₙ|ψ⟩ = ⟨aₙ|ψ⟩|aₙ⟩, a ket proportional to |aₙ⟩ with coefficient cₙ = ⟨aₙ|ψ⟩. The probability is ⟨ψ|Pₙ|ψ⟩ = |cₙ|². For degenerate eigenvalue aₙ with multiplicity d, the projector is Pₙ = Σₖ₌₁ᵈ |aₙ,k⟩⟨aₙ,k| and the probability is Σₖ|⟨aₙ,k|ψ⟩|².

**Common misconception.** Students conflate ⟨aₙ|ψ⟩ (a complex amplitude) with P(aₙ) (a real probability). The probability is the *squared modulus* |⟨aₙ|ψ⟩|². This error appears persistently in calculations: students write "the probability of getting aₙ is ⟨aₙ|ψ⟩" and get a complex number, then are confused.

**Worked example.** State |ψ⟩ = (3/5)|0⟩ + (4i/5)|1⟩ measured in the σz eigenbasis. Amplitudes: ⟨0|ψ⟩ = 3/5, ⟨1|ψ⟩ = 4i/5. Probabilities: P(+1) = |3/5|² = 9/25, P(−1) = |4i/5|² = 16/25. Check: 9/25 + 16/25 = 1 ✓. Expectation value: ⟨σz⟩ = (+1)(9/25) + (−1)(16/25) = −7/25.

**Sources.**
- Townsend notes §1.5 "Statistical interpretation" — Born rule stated as P(λᵢ) = |⟨ψᵢ|ψ⟩|².
- Primary draft §"Operators and Hermiticity" — "The probability of getting outcome aₙ when you measure Â on a state |ψ⟩ is |⟨aₙ|ψ⟩|² — the Born rule, stated as a geometric projection."
- Sakurai §1.4 — projector formalism for degenerate eigenvalues treated carefully.

---

## B. Domain examples and cases

**B1. Pauli matrices — all three are 2×2 Hermitian observables.**
σx = [[0,1],[1,0]], σy = [[0,−i],[i,0]], σz = [[1,0],[0,−1]]. Each has eigenvalues ±1 and orthogonal eigenstates. Their spectral decompositions are σz = |+z⟩⟨+z| − |−z⟩⟨−z|, etc. The σy case is the standard check for Hermitian ≠ symmetric (primary draft §"Operators and Hermiticity"): σy's transpose is −σy (antisymmetric), but its conjugate transpose is +σy (Hermitian).

**B2. The momentum operator p̂ = −iℏ∂x — Hermitian on L²(ℝ).**
Hermiticity requires integration by parts plus the boundary condition that ψ(x) → 0 as |x| → ∞ (Townsend notes §1.10). The factor of i in p̂ = −iℏ∂x is what makes it Hermitian; ∂x alone is anti-Hermitian (eigenvalues imaginary). The primary draft gives the full integration-by-parts proof and connects the factor of i to physical necessity.

**B3. The Hamiltonian for the infinite square well — real discrete spectrum.**
Eigenvalues Eₙ = n²π²ℏ²/2mL² (positive, real, non-degenerate). Eigenstates ψₙ(x) = √(2/L) sin(nπx/L) are orthonormal. The spectral decomposition gives Ĥ = Σₙ Eₙ |Eₙ⟩⟨Eₙ|. This is the simplest infinite-dimensional example of the spectral theorem.

**B4. Degenerate 2D harmonic oscillator — degeneracy and the non-uniqueness of eigenbases.**
The 2D harmonic oscillator has energy levels Eₙ = (n+1)ℏω with degeneracy gₙ = n+1. Within each degenerate subspace, any unitary rotation gives an equally valid eigenbasis. This is the pedagogically cleanest example of degeneracy before angular momentum is introduced.

**B5. Non-Hermitian operators and their role.**
The raising and lowering operators S⁺ = |2⟩⟨1|, S⁻ = |1⟩⟨2| are explicitly not Hermitian (Townsend notes §1.2: "S⁺, S⁻ are not Hermitian, so neither can represent an observable"). They appear as building blocks for Hermitian observables: σx = S⁺ + S⁻, σy = i(S⁺ − S⁻). This is the prototype for the ladder-operator technique in angular momentum.

---

## C. Connections and dependencies

**Prerequisites.**
- Ch 01 (The Formalism): Dirac notation, inner products, operator definition, matrix representations, basis expansion.
- Linear algebra: eigenvalue problem, determinant, characteristic polynomial, diagonalization, Gram–Schmidt.

**Unlocks.**
- Ch 03 (Commutators and Uncertainty): the spectral theorem is needed to define "simultaneous eigenbasis" for commuting observables.
- Angular momentum (later): the entire ladder-operator derivation of L² and Lz spectra uses the spectral theorem in the crucial step "because L² commutes with Lz, they share a common eigenbasis."
- Perturbation theory (later): degenerate perturbation theory requires finding the "right" basis within the degenerate subspace — exactly the Gram–Schmidt step of this chapter.
- Measurement theory (if covered): the projector Pₙ becomes the instrument for describing post-measurement state collapse.

**Adjacent chapters.**
- The qubit (Ch 01) provides all the 2×2 examples; Ch 02 formalizes what was done concretely there.
- The hydrogen atom (Ch 07 companion) requires knowing that Ĥ, L², and Lz are mutually commuting Hermitian operators with a shared eigenbasis — this chapter supplies the justification.

---

## D. Current state of the field

**Settled.** Hermitian operators as observables, real eigenvalues, orthogonal eigenstates, spectral decomposition — all completely settled mathematics and physics.

**Nuanced.** The distinction between Hermitian (symmetric) and self-adjoint operators on infinite-dimensional spaces with unbounded operators (like p̂ = −iℏ∂x) requires specifying a domain. The momentum operator on [0,L] with periodic boundary conditions is self-adjoint; on [0,L] with Dirichlet boundary conditions it is not (it has deficiency indices). This is beyond the scope of this chapter but worth a footnote for students heading toward mathematical physics.

**Pedagogical research.**
- Marshman & Singh, "Investigating and improving student understanding of the probability distributions for measuring physical observables in quantum mechanics," Eur. J. Phys. 38, 025705 (2017). https://doi.org/10.1088/1361-6404/aa57d1 — specifically identifies confusion between amplitudes and probabilities as a persistent difficulty.
- Passante et al., "Examining student use of Dirac notation," Phys. Rev. ST Phys. Educ. Res. 11, 020132 (2015). https://doi.org/10.1103/PhysRevSTPER.11.020132

**Key references.**
- Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed. (University Science Books, 2012), §§1.2–1.5.
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2021), §§1.3–1.4.
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge, 2018), §3.3 — accessible proof of the spectral theorem for undergraduates.
- Reed & Simon, *Methods of Modern Mathematical Physics*, Vol. I (Academic Press, 1972) — rigorous treatment of self-adjoint operators for mathematically inclined students.

---

## E. Teaching considerations

**Lead with the physical argument.** Begin by asking: "What do we require of a quantity that represents a measurement outcome?" Answer: real-valued. Then derive Hermiticity in two lines. This inverts the usual order (postulate first, justify never) and makes the framework feel necessary rather than arbitrary.

**The 2×2 diagonalization as the computational core.** Students should be able to diagonalize any 2×2 Hermitian matrix by hand: write the secular equation (λ² − trace·λ + det = 0), solve the quadratic, substitute back to find eigenvectors, normalize. This takes about 10 minutes and should become fluent before midterm.

**Explicit failure-mode drill on σy.** Have students compute σyᵀ (the plain transpose) and σy† (the conjugate transpose) and state which one equals σy. Then have them verify that σy is Hermitian but not symmetric, and explain the difference for complex matrices. This directly addresses the most common single error in the chapter (identified in primary draft and PER literature).

**Emphasize the spectral decomposition is a sum of projectors.** Â = Σₙ aₙ|aₙ⟩⟨aₙ| is the operator analogue of writing a vector in its basis. Each projector |aₙ⟩⟨aₙ| is a "yes/no" observable: it returns 1 if the system is in |aₙ⟩ and 0 otherwise. Eigenvalues are the possible measurement outcomes; projectors are the "filters" that select them.

**Degeneracy as a warning sign.** When a spectrum is degenerate, the eigenbasis is not unique. Students need to know this because degenerate perturbation theory will force them to find the "right" basis within the degenerate subspace (using the perturbing Hamiltonian). Plant this flag here.

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-04-formalism-dirac-notation-and-operators.md` — §"Operators and Hermiticity": Hermitian definition, adjoint, spectral theorem, proof of Hermiticity for p̂ (integration by parts), σy as the canonical failure-mode example.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-qm-townsend-notes.md` — §§1.2, 1.4, 1.5: observables, eigenvalue problem (proof of real eigenvalues and orthogonality), statistical interpretation (Born rule).
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-06-spin.md` — downstream chapter; uses the spectral theorem for spin-1/2 observables.
- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/pantry/_lib_qmsri-07-the-hydrogen-atom.md` — downstream; Ĥ, L², Lz spectral decompositions are the payoff of this chapter.

---

## G. Gaps and flags

**Gap — continuous spectrum needs separate treatment.** The spectral theorem as stated here applies cleanly to operators with discrete spectra. The position operator x̂ has a continuous spectrum; its "eigenvalues" are all real numbers and its "eigenstates" are delta functions (not in L²). The spectral theorem generalizes via the spectral measure, but this is technical machinery beyond the chapter's scope. Recommend a brief note: "For operators with continuous spectra (like x̂ and p̂), the spectral decomposition becomes an integral Â = ∫ a |a⟩⟨a| da; the Born rule becomes a probability density P(a) = |⟨a|ψ⟩|² da."

**Gap — no discussion of functions of operators.** f(Â) = Σₙ f(aₙ)|aₙ⟩⟨aₙ| is used constantly (the time-evolution operator e^{−iĤt/ℏ} is the first example). Worth a brief sidebar: once you have the spectral decomposition, defining functions of operators is straightforward.

**Flag — the adjoint of a product.** (ÂB̂)† = B̂†Â† (order reversal) is used in proving orthogonality and in later chapters (ladder operators, etc.). This algebraic fact is not stated explicitly in either the primary draft or the Townsend notes at this stage; add it as a lemma.

**Flag — the Sakurai .txt file** in physics-quantum-mechanics-sri pantry is not usable (corrupted placeholder). Cite Sakurai from published editions only.

**Flag — norm of p̂ψ and domain issues.** The integration-by-parts proof of Hermiticity for p̂ requires ψ(x) → 0 as |x| → ∞. The primary draft notes this correctly. Students should understand this is a physical requirement (normalizability), not an arbitrary mathematical assumption.
