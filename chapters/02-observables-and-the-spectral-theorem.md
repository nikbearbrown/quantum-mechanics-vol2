# Chapter 2 — Observables, Hermiticity, and the Spectral Theorem

## TL;DR

- Measurement outcomes are real numbers; that single requirement forces every observable to be a Hermitian operator.
- Hermitian operators have real eigenvalues (a four-line proof) and orthogonal eigenstates for distinct eigenvalues (a five-line proof).
- The spectral theorem: every Hermitian operator can be written $\hat{A} = \sum_n a_n|a_n\rangle\langle a_n|$ — a sum of projectors, each weighted by a measurement outcome.
- The Born rule is geometric: $P(a_n) = \langle\psi|\hat{P}_n|\psi\rangle = |\langle a_n|\psi\rangle|^2$ is the squared length of the projection of $|\psi\rangle$ onto the eigenstate $|a_n\rangle$.
- Degeneracy is the one place the proofs fail, and Gram–Schmidt is the fix.

## Learning Objectives

By the end of this chapter you will be able to:

1. **Justify** from first principles why physical observables must be Hermitian operators, without invoking the postulate directly. *(Bloom: Understand)*
2. **Prove** that eigenvalues of a Hermitian operator are real and that eigenstates with distinct eigenvalues are orthogonal. *(Bloom: Analyze)*
3. **State** the spectral decomposition $\hat{A} = \sum_n a_n|a_n\rangle\langle a_n|$ and explain what each factor means physically. *(Bloom: Remember/Understand)*
4. **Apply** the Born rule via projectors to compute measurement probabilities and expectation values in any discrete-spectrum observable. *(Bloom: Apply)*
5. **Diagonalize** a $2\times 2$ Hermitian matrix by hand: write the secular equation, solve for eigenvalues, find and normalize eigenvectors, and verify the spectral decomposition. *(Bloom: Apply)*

---

## Opening: Why $i$ Has to Be There

The momentum operator is $\hat{p} = -i\hbar\,\partial_x$. Students arriving from wave mechanics accept this formula because it works — it gives the right de Broglie relation, it generates the right equations. But almost no one asks: why the $i$? Why not just $\hbar\,\partial_x$?

The answer is that without the $i$, $\hat{p}$ would not be Hermitian. And if $\hat{p}$ is not Hermitian, its eigenvalues are imaginary, which means measuring momentum would return a complex number. A meter stick returning a complex-valued length makes no sense.

Here is the calculation. With $\hat{p} = -i\hbar\,\partial_x$:
$$\langle\phi|\hat{p}\psi\rangle = \int_{-\infty}^\infty \phi^*(x)(-i\hbar)\partial_x\psi(x)\,dx$$

Integrate by parts. The boundary term vanishes (normalizable states go to zero at $\pm\infty$):
$$= \int_{-\infty}^\infty (i\hbar\partial_x\phi^*(x))\psi(x)\,dx = \int_{-\infty}^\infty (-i\hbar\partial_x\phi(x))^*\psi(x)\,dx = \langle\hat{p}\phi|\psi\rangle$$

So $\hat{p}^\dagger = \hat{p}$: Hermitian. Now try $\hat{p}' = \hbar\partial_x$ (no $i$). The same integration gives $\int(\partial_x\phi^*)^*\psi\,dx\cdot\hbar = -\langle\hat{p}'\phi|\psi\rangle$. Anti-Hermitian. Eigenvalues purely imaginary. Momentum is not an imaginary number.

The $i$ is not convention. It is necessity. This chapter explains why, systematically.

---

## Core Development

### Why Observables Must Be Hermitian

A physical observable is a quantity whose measured values are real numbers. That is the requirement — nothing more. If $\hat{A}$ represents an observable, then for any state $|\psi\rangle$, the expectation value

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle$$

must be real. This must hold for *every* state $|\psi\rangle$ — not just some special ones.

Compute what "real" means:

$$\langle\hat{A}\rangle^* = \langle\psi|\hat{A}|\psi\rangle^* = \langle\psi|\hat{A}^\dagger|\psi\rangle$$

The second equality uses the definition of the adjoint: $\langle\phi|\hat{A}\psi\rangle^* = \langle\hat{A}^\dagger\phi|\psi\rangle^* = \langle\psi|\hat{A}^\dagger|\phi\rangle$... more directly, $\langle\psi|\hat{A}|\psi\rangle^* = \langle\hat{A}^\dagger\psi|\psi\rangle = \langle\psi|\hat{A}^\dagger|\psi\rangle$ (using the definition $\langle v|\hat{B}w\rangle = \langle \hat{B}^\dagger v|w\rangle$ and setting $v = w = \psi$, $\hat{B} = \hat{A}$).

For $\langle\hat{A}\rangle$ to be real for all $|\psi\rangle$: $\langle\hat{A}\rangle = \langle\hat{A}\rangle^*$, i.e.,
$$\langle\psi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}^\dagger|\psi\rangle \quad \text{for all }|\psi\rangle$$

This is equivalent to $\hat{A} = \hat{A}^\dagger$, i.e., $\hat{A}$ is **Hermitian**.

The equivalence in the last step — that $\langle\psi|(\hat{A} - \hat{A}^\dagger)|\psi\rangle = 0$ for all $|\psi\rangle$ implies $\hat{A} = \hat{A}^\dagger$ — follows from the polarization identity: any sesquilinear form that vanishes on the diagonal vanishes everywhere. This is a standard linear algebra result; the point is that the condition "diagonal matrix elements vanish" in fact forces the operator to be zero.

So: observables are Hermitian not by convention, not by postulate from authority, but because measurement outcomes are real. The framework is built to match a physical fact.

### Hermiticity in Matrix Form

In a basis $\{|n\rangle\}$, the adjoint condition $\hat{A} = \hat{A}^\dagger$ becomes the condition on matrix entries:
$$A_{mn} = A_{nm}^*$$

This means: the matrix equals its own conjugate transpose. Off-diagonal entries come in conjugate pairs; diagonal entries are real.

The canonical failure-mode: $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Its plain transpose is $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$ — antisymmetric, not symmetric. Students trained on real linear algebra, where "Hermitian" means "symmetric," write $\sigma_y$ with both off-diagonal entries equal to $i$ and produce a non-Hermitian matrix. The cure: check $A_{12} = A_{21}^*$. Here $A_{12} = -i$ and $A_{21} = i = (-i)^*$. Check passes; $\sigma_y$ is Hermitian.

The diagnostic question: "Is the matrix symmetric?" is wrong for complex operators. The correct question: "Does $A_{mn} = A_{nm}^*$ hold?" — and computing the conjugate transpose, not the plain transpose, is required.

### Real Eigenvalues: The Proof

**Theorem.** If $\hat{A}$ is Hermitian and $\hat{A}|a\rangle = a|a\rangle$, then $a \in \mathbb{R}$.

**Proof.** Compute $\langle a|\hat{A}|a\rangle$ two ways.

*Way 1.* Use $\hat{A}|a\rangle = a|a\rangle$: $\langle a|\hat{A}|a\rangle = a\langle a|a\rangle = a$.

*Way 2.* Use $\hat{A}^\dagger = \hat{A}$ and the definition of the adjoint. Since $\hat{A}$ is Hermitian, $\hat{A}|a\rangle = a|a\rangle$ implies $\langle a|\hat{A} = \langle a|a^*$ (take the bra of both sides, using that bra of $a|a\rangle$ is $a^*\langle a|$). Therefore:
$$\langle a|\hat{A}|a\rangle = a^*\langle a|a\rangle = a^*$$

Equating the two results: $a = a^*$, so $a \in \mathbb{R}$. $\square$

The proof is four lines. Memorize the structure: compute the same sandwich two ways, use Hermiticity to get the conjugate, equate.

**What fails without Hermiticity.** If $\hat{A} \neq \hat{A}^\dagger$, way 2 gives $a^*$ replaced by the eigenvalue of $\hat{A}^\dagger$, which is in general different from $a$. The proof collapses; $a$ need not be real.

**Counterexample.** The matrix $\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ has both eigenvalues equal to 0 (nilpotent), but it is not Hermitian. The matrix $\bigl(\begin{smallmatrix}0&i\\i&0\end{smallmatrix}\bigr)$ has eigenvalues $\pm i$ — purely imaginary, not real. Neither is Hermitian; both illustrate what goes wrong.

### Orthogonality of Eigenstates: The Proof

**Theorem.** If $\hat{A}$ is Hermitian, $\hat{A}|a\rangle = a|a\rangle$, $\hat{A}|a'\rangle = a'|a'\rangle$, and $a \neq a'$, then $\langle a|a'\rangle = 0$.

**Proof.** Compute $\langle a|\hat{A}|a'\rangle$ two ways.

*Way 1.* Act $\hat{A}$ on the ket: $\langle a|\hat{A}|a'\rangle = a'\langle a|a'\rangle$.

*Way 2.* Act $\hat{A}$ on the bra (using Hermiticity and that $a$ is real, established above): $\langle a|\hat{A}|a'\rangle = \langle\hat{A}a|a'\rangle = a\langle a|a'\rangle$.

Equating: $a'\langle a|a'\rangle = a\langle a|a'\rangle$, so $(a' - a)\langle a|a'\rangle = 0$. Since $a' \neq a$, we conclude $\langle a|a'\rangle = 0$. $\square$

The proof requires that $a$ be real (from the previous theorem) — you need $\langle\hat{A}a| = a^*\langle a| = a\langle a|$ in way 2. The two theorems are logically chained.

### Degeneracy: Where the Proof Stops

When $a = a'$ — a **degenerate** eigenvalue — the factor $(a' - a)$ is zero and the proof says nothing. The equation $(0)\langle a|a'\rangle = 0$ is satisfied for any value of $\langle a|a'\rangle$. Two linearly independent eigenstates with the same eigenvalue need not be orthogonal.

**Example.** The $2\times 2$ identity operator $\hat{I}$ has every vector as an eigenvector with eigenvalue 1. The states $(1,0)^\top$ and $(1,1)^\top/\sqrt{2}$ are both eigenstates with eigenvalue 1 but are not orthogonal.

The remedy is **Gram–Schmidt orthogonalization**: within each degenerate subspace, construct an orthonormal basis by the standard Gram–Schmidt procedure. The theorem guarantees this is possible — a degenerate subspace has a complete orthonormal eigenbasis, just not a unique one.

This matters later: when the hydrogen atom has degenerate energy levels, you must choose a basis within each degenerate subspace. The choice is not arbitrary — a second observable (angular momentum) selects the "right" one. Degeneracy is always a sign that some symmetry is present, and the additional observable that resolves the degeneracy is the observable that generates that symmetry.

### The Spectral Theorem

Combining the two theorems — real eigenvalues, orthogonal eigenstates — with the completeness statement that the eigenstates span the whole Hilbert space gives the **spectral theorem**:

> **Spectral Theorem.** Every Hermitian operator $\hat{A}$ on a finite-dimensional Hilbert space (or bounded self-adjoint operator on an infinite-dimensional one) has a complete orthonormal set of eigenstates $\{|a_n\rangle\}$. The operator can be written in its **spectral decomposition**:
$$\hat{A} = \sum_n a_n\,|a_n\rangle\langle a_n|$$

Each term $\hat{P}_n = |a_n\rangle\langle a_n|$ is a **projector** onto the $n$th eigenspace. Its properties:
- $\hat{P}_n^2 = \hat{P}_n$ (idempotent: projecting twice is the same as once)
- $\hat{P}_n^\dagger = \hat{P}_n$ (Hermitian: projectors are themselves observables)
- $\sum_n \hat{P}_n = \hat{I}$ (completeness: the projectors partition the identity)
- $\hat{P}_m\hat{P}_n = \delta_{mn}\hat{P}_n$ (orthogonality: projectors onto different eigenspaces do not interfere)

The spectral decomposition is the operator analogue of writing a vector in its own eigenbasis: in that basis, the operator is diagonal, with eigenvalues on the diagonal.

**Degenerate case.** If eigenvalue $a_n$ has multiplicity $d > 1$, the corresponding projector is $\hat{P}_n = \sum_{k=1}^d |a_n, k\rangle\langle a_n, k|$, summing over an orthonormal basis for the degenerate subspace. The decomposition still holds; the projector just has rank $d > 1$.

### Projectors and the Born Rule as Geometry

The Born rule $P(a_n) = |\langle a_n|\psi\rangle|^2$ is the squared length of the projection of $|\psi\rangle$ onto $|a_n\rangle$. In projector language:
$$P(a_n) = \langle\psi|\hat{P}_n|\psi\rangle = \|\hat{P}_n|\psi\rangle\|^2$$

This makes the probability a geometric object: the squared norm of the component of $|\psi\rangle$ in the $n$th eigenspace.

The expectation value:
$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \langle\psi|\left(\sum_n a_n\hat{P}_n\right)|\psi\rangle = \sum_n a_n\langle\psi|\hat{P}_n|\psi\rangle = \sum_n a_n P(a_n)$$

The expectation value is the probability-weighted average of eigenvalues. This is exactly the definition of expected value from probability theory — the spectral theorem makes the connection precise.

**The amplitude vs. probability distinction.** The amplitude $\langle a_n|\psi\rangle$ is a complex number $c_n = |c_n|e^{i\theta_n}$. The probability is $|c_n|^2$. Students persistently write "the probability is $\langle a_n|\psi\rangle$" and obtain complex numbers. The probability is the squared modulus: $|\langle a_n|\psi\rangle|^2$. The phase $e^{i\theta_n}$ vanishes in the probability but reappears — crucially — in interference terms when two amplitudes are added before squaring. Keeping the distinction is the difference between quantum and classical probability.

### Functions of Operators

Once you have the spectral decomposition, defining functions of operators is straightforward:
$$f(\hat{A}) = \sum_n f(a_n)\,|a_n\rangle\langle a_n|$$

The time-evolution operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ is defined this way: $\hat{U}(t) = \sum_n e^{-iE_nt/\hbar}|E_n\rangle\langle E_n|$. Every state decomposes into energy eigenstates, each oscillating at its own frequency. The full time evolution is a superposition of these oscillations. The spectral theorem makes this explicit and derivable, not assumed.

---

## Worked Example: Diagonalizing a $2\times 2$ Hermitian Observable

**Setup.** Consider the operator
$$\hat{B} = \begin{pmatrix} 2 & 1+i \\ 1-i & 0 \end{pmatrix}$$

in the basis $\{|1\rangle, |2\rangle\}$. Verify it is Hermitian, find its spectrum and eigenstates, write the spectral decomposition, and use it to compute the probability of each outcome when $\hat{B}$ is measured on the state $|\psi\rangle = (|1\rangle + |2\rangle)/\sqrt{2}$.

**Step 1: Check Hermiticity.** The adjoint is $(B^\dagger)_{mn} = B_{nm}^*$. So $(B^\dagger)_{12} = B_{21}^* = (1-i)^* = 1+i = B_{12}$, and $(B^\dagger)_{11} = B_{11}^* = 2^* = 2 = B_{11}$, $(B^\dagger)_{22} = 0$. Check: $B^\dagger = B$. Hermitian.

**Step 2: Secular equation.** The eigenvalues satisfy $\det(\hat{B} - \lambda\hat{I}) = 0$:
$$\det\begin{pmatrix}2-\lambda & 1+i \\ 1-i & -\lambda\end{pmatrix} = -\lambda(2-\lambda) - (1+i)(1-i) = 0$$

Expand: $-2\lambda + \lambda^2 - |1+i|^2 = 0$. Note $|1+i|^2 = (1+i)(1-i) = 2$:
$$\lambda^2 - 2\lambda - 2 = 0 \implies \lambda = \frac{2 \pm \sqrt{4 + 8}}{2} = 1 \pm \sqrt{3}$$

Eigenvalues: $\lambda_+ = 1 + \sqrt{3} \approx 2.73$ and $\lambda_- = 1 - \sqrt{3} \approx -0.73$.

Both are real, as promised by the theorem. A check: $\lambda_+ + \lambda_- = 2 = \text{Tr}(\hat{B})$ and $\lambda_+\lambda_- = 1 - 3 = -2 = \det(\hat{B})$. Both match.

**Step 3: Eigenvectors.** For $\lambda_+$: solve $(\hat{B} - \lambda_+\hat{I})|b_+\rangle = 0$:
$$\begin{pmatrix}1-\sqrt{3} & 1+i \\ 1-i & -1-\sqrt{3}\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix} = 0$$

From the first row: $(1-\sqrt{3})x + (1+i)y = 0$, so $x = \frac{-(1+i)}{\sqrt{3}-1}y$. Rationalize: $\frac{1+i}{\sqrt{3}-1}\cdot\frac{\sqrt{3}+1}{\sqrt{3}+1} = \frac{(1+i)(\sqrt{3}+1)}{2}$.

Let $y = \mathcal{N}$ (normalization constant to be determined). Then $x = -\frac{(1+i)(\sqrt{3}+1)}{2}\mathcal{N}$.

Normalization: $|x|^2 + |y|^2 = 1$. Note $|1+i|^2 = 2$ and $(\sqrt{3}+1)^2 = 4+2\sqrt{3}$:
$$|x|^2 = \frac{2(4+2\sqrt{3})}{4}|\mathcal{N}|^2 = \frac{(4+2\sqrt{3})}{2}|\mathcal{N}|^2 = (2+\sqrt{3})|\mathcal{N}|^2$$

So $(2+\sqrt{3}+1)|\mathcal{N}|^2 = 1$, giving $|\mathcal{N}|^2 = 1/(3+\sqrt{3})$.

The normalized eigenvector:
$$|b_+\rangle = \frac{1}{\sqrt{3+\sqrt{3}}}\begin{pmatrix}-(1+i)(\sqrt{3}+1)/2 \\ 1\end{pmatrix}$$

A dead end to flag: students sometimes try to read eigenvectors directly off the matrix without solving the system. This only works for diagonal matrices. For any non-trivial off-diagonal element, you must substitute the eigenvalue into $(\hat{B} - \lambda\hat{I})|\cdot\rangle = 0$ and solve the homogeneous system.

For $\lambda_-$: the same procedure gives $|b_-\rangle$ orthogonal to $|b_+\rangle$ — check this by computing $\langle b_+|b_-\rangle$ and verifying it is zero.

**Step 4: Spectral decomposition.** With eigenvectors $|b_+\rangle$ and $|b_-\rangle$:
$$\hat{B} = \lambda_+\,|b_+\rangle\langle b_+| + \lambda_-\,|b_-\rangle\langle b_-|$$

Verify: $(\lambda_+|b_+\rangle\langle b_+| + \lambda_-|b_-\rangle\langle b_-|)|b_+\rangle = \lambda_+|b_+\rangle$ ✓ and $\langle b_+|\hat{B}|b_+\rangle = \lambda_+$ ✓.

**Step 5: Born rule probabilities.** The state is $|\psi\rangle = (|1\rangle + |2\rangle)/\sqrt{2}$. The probability of outcome $\lambda_+$:
$$P(\lambda_+) = |\langle b_+|\psi\rangle|^2$$

This requires computing the inner product, which is straightforward given the explicit eigenvector. The answer depends on the normalization worked out above. Let us denote the result symbolically for clarity: $P(\lambda_+) + P(\lambda_-) = 1$ (normalization check), and $\langle\hat{B}\rangle = \lambda_+ P(\lambda_+) + \lambda_- P(\lambda_-) = \langle\psi|\hat{B}|\psi\rangle$. Verify the last equality directly:
$$\langle\psi|\hat{B}|\psi\rangle = \frac{1}{2}\bigl(\langle 1| + \langle 2|\bigr)\begin{pmatrix}2&1+i\\1-i&0\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}/1 \cdot \frac{1}{\sqrt{2}}$$

$$= \frac{1}{2}\bigl(\langle 1| + \langle 2|\bigr)\begin{pmatrix}3+i\\1-i\end{pmatrix} = \frac{1}{2}\bigl((3+i) + (1-i)\bigr) = \frac{1}{2}(4) = 2$$

**The lesson.** The spectral decomposition of $\hat{B}$ encodes everything: the possible outcomes ($\lambda_\pm$), the states that give them with certainty ($|b_\pm\rangle$), and the probability of each outcome from any input state via the inner product. Diagonalizing $\hat{B}$ is equivalent to finding the "natural basis" in which the measurement is most transparent.

**The limit.** For a $10\times 10$ Hermitian matrix, the secular equation is a degree-10 polynomial that generally cannot be solved in closed form. Numerical diagonalization is used in practice. The spectral theorem guarantees that eigenvalues exist and are real and that eigenvectors span the space; it does not provide a closed-form formula for them.

---

## Common Misconceptions

**"Observables are Hermitian because the postulate says so."** The postulate is a consequence of a physical requirement, not an unexplained rule. The derivation takes three lines: expectation values must be real, and reality of $\langle\hat{A}\rangle$ for all states implies $\hat{A} = \hat{A}^\dagger$. Understanding the derivation also shows what would happen if we tried to use a non-Hermitian operator as an observable — complex expectation values — which immediately signals the inconsistency.

**"The eigenvalues of a real matrix are always real."** False. The matrix $\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$ has real entries and eigenvalues $\pm i$. Hermiticity (not real entries) is what guarantees real eigenvalues. Conversely, $\sigma_y$ has complex entries and real eigenvalues $\pm 1$ because it is Hermitian.

**"Degenerate eigenstates are automatically orthogonal."** They are not. The orthogonality theorem requires $a \neq a'$; when $a = a'$ the proof gives $0 = 0$, which is vacuously true and tells you nothing. Within a degenerate subspace you choose the orthogonal basis by Gram–Schmidt; the theorem does not do it for you. Students who believe this are blindsided by degenerate perturbation theory.

**"The probability of outcome $a_n$ is $\langle a_n|\psi\rangle$."** No. $\langle a_n|\psi\rangle$ is a complex amplitude $c_n$. The probability is $|c_n|^2$, a non-negative real number. These differ by the modulus squaring, which eliminates the phase. The phase is not observable in a single-observable measurement but is observable in interference terms. Writing "probability = amplitude" is category confusion and produces complex probabilities.

**"The spectral decomposition only works when you know the eigenstates."** It works because the theorem guarantees the eigenstates exist and form a complete set. Whether you can compute them in closed form is a separate question. The expansion $|ψ⟩ = \sum_n c_n|a_n⟩$ holds regardless; the difficulty is practical, not conceptual.

**"$\hat{A} = \hat{A}^\dagger$ means the matrix has real entries."** The condition is $A_{mn} = A_{nm}^*$, which says the matrix equals its own conjugate transpose. Diagonal entries must be real (since $A_{nn} = A_{nn}^*$), but off-diagonal entries can be complex as long as they come in conjugate pairs. A matrix with complex entries can be Hermitian; a matrix with all real entries can fail to be Hermitian if it is not symmetric.

---

## Exercises

### Warm-Up

**2.1** Determine whether each of the following operators is Hermitian, anti-Hermitian ($\hat{A}^\dagger = -\hat{A}$), or neither. (a) $\hat{A} = \bigl(\begin{smallmatrix}1&2i\\-2i&3\end{smallmatrix}\bigr)$. (b) $\hat{B} = \bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr)$. (c) $\hat{C} = \bigl(\begin{smallmatrix}1&1+i\\1-i&-1\end{smallmatrix}\bigr)$. For each Hermitian operator, state the constraint on its diagonal entries. *(Tests: can apply the Hermitian condition $A_{mn} = A_{nm}^*$ to $2\times 2$ complex matrices)*

**2.2** Prove the four-line theorem: if $\hat{A}$ is Hermitian and $\hat{A}|a\rangle = a|a\rangle$, then $a \in \mathbb{R}$. Write the proof in your own words, identifying exactly where Hermiticity is used. Then exhibit a non-Hermitian $2\times 2$ matrix with an imaginary eigenvalue, and show where the proof fails for it. *(Tests: can reproduce and articulate the real-eigenvalue proof; understands the role of Hermiticity)*

**2.3** The state $|\psi\rangle = (3/5)|0\rangle + (4i/5)|1\rangle$ is measured in the $\sigma_z$ eigenbasis. (a) Compute the amplitude for each outcome: $\langle 0|\psi\rangle$ and $\langle 1|\psi\rangle$. (b) Compute the probabilities $P(+1)$ and $P(-1)$. (c) Verify $P(+1) + P(-1) = 1$. (d) Compute $\langle\sigma_z\rangle$ using the spectral sum $\sum_n a_n P(a_n)$ and verify by direct matrix calculation $\langle\psi|\sigma_z|\psi\rangle$. *(Tests: can distinguish amplitude from probability; applies the Born rule correctly; verifies the spectral expectation-value formula)*

### Application

**2.4** Diagonalize $\hat{A} = \bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$. (a) Find the eigenvalues using the secular equation $\lambda^2 - \text{Tr}(\hat{A})\lambda + \det(\hat{A}) = 0$. (b) Find and normalize the eigenvectors. (c) Write the spectral decomposition $\hat{A} = \lambda_1|a_1\rangle\langle a_1| + \lambda_2|a_2\rangle\langle a_2|$ and verify by expanding the outer products and summing. (d) Verify $\hat{P}_1^2 = \hat{P}_1$ and $\hat{P}_1\hat{P}_2 = 0$. *(Tests: can execute the full diagonalization; verifies the projector properties)*

**2.5** An observable has the matrix representation $\hat{M} = \bigl(\begin{smallmatrix}0&e^{i\phi}\\e^{-i\phi}&0\end{smallmatrix}\bigr)$ for some real $\phi$. (a) Verify this is Hermitian. (b) Find the eigenvalues (they should be independent of $\phi$). (c) Find the eigenstates and show they depend on $\phi$. (d) Compute $\langle\hat{M}\rangle$ when the state is $|0\rangle$ and when the state is $(|0\rangle + |1\rangle)/\sqrt{2}$. *(Tests: can diagonalize a general Hermitian matrix with a phase parameter; understands that eigenvalues are $\phi$-independent while eigenstates are not)*

**2.6** (Apply the spectral decomposition to time evolution.) The Hamiltonian is $\hat{H} = E_0\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$. (a) Write the spectral decomposition of $\hat{H}$. (b) Use it to write $e^{-i\hat{H}t/\hbar} = \sum_n e^{-iE_nt/\hbar}|E_n\rangle\langle E_n|$ explicitly as a $2\times 2$ matrix. (c) Evolve the initial state $|\psi(0)\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ to $|\psi(t)\rangle$. (d) Compute $\langle\hat{H}\rangle$ at time $t$ and verify it is constant. *(Tests: can construct functions of operators via the spectral decomposition; verifies energy conservation)*

**2.7** Produce something. A Hermitian operator on a 3D Hilbert space with basis $\{|1\rangle, |2\rangle, |3\rangle\}$ has matrix
$$\hat{G} = \begin{pmatrix}2&0&0\\0&0&1\\0&1&0\end{pmatrix}$$
(a) Verify it is Hermitian. (b) Find all three eigenvalues. (c) Note that two eigenvalues are equal (degenerate). Apply Gram–Schmidt to the degenerate subspace to find two orthonormal eigenstates. (d) Write the full spectral decomposition, including the degenerate projector as a sum of two rank-1 projectors. (e) Compute $\langle\hat{G}\rangle$ for the state $|\psi\rangle = (|1\rangle + |2\rangle + |3\rangle)/\sqrt{3}$ using both the spectral sum $\sum_n a_n P(a_n)$ and the direct matrix product $\langle\psi|\hat{G}|\psi\rangle$. *(Tests: handles the degenerate case; applies Gram–Schmidt; verifies the spectral expectation value in 3D)*

### Synthesize

**2.8** Prove the five-line theorem: if $\hat{A}$ is Hermitian with distinct eigenvalues $a \neq a'$, then $\langle a|a'\rangle = 0$. Then explain in one paragraph why the proof breaks down for degenerate eigenvalues, and why Gram–Schmidt restores an orthonormal basis. *(Tests: can reproduce the orthogonality proof; understands where degeneracy breaks the argument and how to fix it)*

**2.9** Let $\hat{P} = |a\rangle\langle a|$ be a projector onto a normalized eigenstate. Prove (a) $\hat{P}^2 = \hat{P}$, (b) $\hat{P}^\dagger = \hat{P}$, (c) $\text{Tr}(\hat{P}) = 1$, (d) the eigenvalues of $\hat{P}$ are 0 and 1. These four properties characterize a projector. Then state which property corresponds to: (i) "projecting twice gives the same result as once," (ii) "the projector is itself an observable," (iii) "the projector has rank 1," (iv) "the measurement outcome is always 0 or 1." *(Tests: can prove the four projector properties and connect them to physical meaning)*

---

## Still Puzzling

**When is Hermitian not the same as self-adjoint?** For bounded operators on finite-dimensional Hilbert spaces — the setting of this chapter — the two conditions are identical. For unbounded operators like $\hat{p} = -i\hbar\partial_x$ on a half-line $[0,\infty)$, the distinction matters: $\hat{p}$ may satisfy $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$ for all $\phi,\psi$ in its domain (Hermitian) but fail to have the right domain to be self-adjoint. The physical consequence is that the spectrum may not be purely real. For the momentum operator on a half-line with Dirichlet boundary conditions, the self-adjointness fails and the spectrum is empty — a particle bouncing off a wall cannot have a definite momentum in the usual sense.

**What is the spectral theorem for operators with continuous spectra?** The position operator $\hat{x}$ has eigenvalues forming the entire real line; its "eigenstates" $|x\rangle$ are not square-integrable. The spectral theorem generalizes via the **spectral measure**: $\hat{x} = \int x\,d\hat{P}(x)$, where $d\hat{P}(x) = |x\rangle\langle x|\,dx$ is a projection-valued measure. The Born rule becomes a probability density: $dP = |\langle x|\psi\rangle|^2\,dx = |\psi(x)|^2\,dx$. This is fully rigorous but requires functional analysis to state precisely.

**Why do degenerate levels carry extra structure?** Degeneracy is not a coincidence — it is always associated with a symmetry. The hydrogen atom's energy $E_n$ is independent of $\ell$ and $m_\ell$ because the Hamiltonian commutes with the angular momentum operators. Each additional commuting symmetry generates additional quantum numbers that label the degenerate states. The spectral theorem does not tell you which set of quantum numbers is the "natural" one; that depends on which symmetries are physically relevant.

---

## The +1 — Simulation Exercise

**Deliverable:** `03-spectral-explorer.html`

### CLAUDE.md Amendment

```
## Chapter 2 — Spectral Explorer Rules

- Single HTML file, D3 v7, no external assets.
- Three panels: (1) 2x2 Hermitian matrix builder, (2) eigenvalue/eigenvector display,
  (3) probability bar chart for a user-chosen input state.
- Hermitian constraint enforced: diagonal entries must be real; off-diagonal entry
  A_12 determines A_21 = A_12* automatically. Display as: Re(A_12), Im(A_12).
- Secular equation: display det(A - lambda*I) = lambda^2 - Tr(A)*lambda + det(A) = 0
  with coefficients shown numerically.
- Eigenvalues computed analytically: lambda = (Tr/2) ± sqrt((Tr/2)^2 - det).
  Never use numerical root-finding for 2x2 case.
- Eigenvectors: computed symbolically from (A - lambda*I)|v> = 0, normalized.
  Display as column vectors with Re and Im parts.
- Input state: two sliders for theta (0..pi) and phi (0..2pi) defining
  |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>.
- Born rule bars: P(lambda_1) = |<a1|psi>|^2, P(lambda_2) = |<a2|psi>|^2.
  Verify P1 + P2 = 1 within 1e-9. Display both amplitudes and probabilities.
- Expectation value: display <A> = lambda_1*P1 + lambda_2*P2 and verify against
  <psi|A|psi> computed by matrix multiplication.
- Redraw function: single redraw() on every slider or input change.
```

### The Prompt

```
Build me 03-spectral-explorer.html following CLAUDE.md.

SHOW.
A 2x2 Hermitian matrix A (user-controlled), its spectral decomposition,
and the Born-rule probabilities for a user-chosen state |psi>.

SAY.
Three panels in a single SVG 1200x700:

(1) Matrix builder (left, 400x350):
    Numeric inputs for A_11 (real), A_22 (real), Re(A_12), Im(A_12).
    Display the full matrix as a 2x2 grid with real and imaginary parts.
    Display Tr(A) and det(A).
    Display the secular equation: lambda^2 - Tr*lambda + det = 0.
    Display eigenvalues lambda_1, lambda_2 (always real -- verify at runtime).

(2) Spectral display (middle, 400x350):
    Display eigenvectors |a1> and |a2> as column vectors (Re, Im per entry).
    Display projectors P1 = |a1><a1| and P2 = |a2><a2| as 2x2 matrices.
    Verify P1 + P2 = I by displaying the sum matrix and checking it against I.
    Display A = lambda_1 * P1 + lambda_2 * P2 reconstructed and verify it
    matches the input matrix within 1e-9.

(3) Born rule panel (right, 400x350):
    State selector: theta slider (0..pi) and phi slider (0..2pi).
    Display |psi> = (cos(theta/2), exp(i*phi)*sin(theta/2)) explicitly.
    Display amplitudes <a1|psi> and <a2|psi> as complex numbers.
    Display P(lambda_1) = |<a1|psi>|^2 and P(lambda_2) = |<a2|psi>|^2
    as horizontal bars (blue and orange), labeled with numeric values.
    Display <A> = lambda_1*P1 + lambda_2*P2 and <psi|A|psi> side by side;
    these must match within 1e-9.

CONSTRAIN.
- D3 v7 from CDN, SVG only, vanilla JS.
- Eigenvalues computed analytically from Tr and det, not numerically.
- Probabilities: always |amplitude|^2, not Re(amplitude) or |amplitude|.
  Runtime check: P1 + P2 = 1 within 1e-9, else flash a red warning.
- Verify eigenvalues are real within 1e-9 (imaginary part < 1e-9).
  If not, the Hermitian check has failed -- flag it in red.
- Eigenvectors: normalized to |v|^2 = 1 within 1e-6.
  Verify orthogonality: |<a1|a2>| < 1e-9.

VERIFY.
Six checks after building:
(a) A = [[1,0],[0,-1]] (sigma_z): eigenvalues +1,-1; eigenvectors (1,0),(0,1).
(b) A = [[0,1],[1,0]] (sigma_x): eigenvalues +1,-1;
    eigenvectors (1/sqrt(2),1/sqrt(2)),(1/sqrt(2),-1/sqrt(2)).
(c) A = [[2,1],[1,2]]: eigenvalues 3,1; eigenvectors (1/sqrt(2))(1,1),(1/sqrt(2))(1,-1).
(d) State |psi>=|0> measured in sigma_z: P(+1)=1, P(-1)=0.
(e) State |psi>=(|0>+|1>)/sqrt(2) measured in sigma_z: P(+1)=0.5, P(-1)=0.5.
(f) <A> from spectral sum matches <psi|A|psi> for all test cases within 1e-9.
```

### Exploration Tasks

**Task 1: Hermitian $\neq$ real.** Set $A_{11} = 1$, $A_{22} = 1$, $\text{Re}(A_{12}) = 0$, $\text{Im}(A_{12}) = 1$ (so $A_{12} = i$, $A_{21} = -i$). This is the matrix $\bigl(\begin{smallmatrix}1&i\\-i&1\end{smallmatrix}\bigr)$. Verify the eigenvalues are 2 and 0 — both real, despite the complex entries. The simulator should confirm the Hermitian check passes. Change $\text{Im}(A_{12}) = 1$ to $\text{Im}(A_{12}) = 0$ and $\text{Re}(A_{12}) = 0.5$: this is a real symmetric matrix. Same structure; still Hermitian. The point: Hermiticity is a condition on the pattern of entries, not on whether they are real.

**Task 2: Eigenstates are the "natural basis."** Set $A = \sigma_x = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$. The eigenstates are $|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ and $|-\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$. Set the input state to $|+\rangle$ ($\theta = \pi/2$, $\phi = 0$). Read the Born-rule bars: $P(+1) = 1$, $P(-1) = 0$. The eigenstate gives the outcome with certainty. Now set $\theta = 0$ (the state $|0\rangle$): the bars show $P(+1) = P(-1) = 1/2$. The state has maximal uncertainty about the observable $\sigma_x$.

**Task 3: The spectral sum checks out.** For the observable $\hat{A} = \bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ and state $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, read $\langle\hat{A}\rangle$ from the spectral sum and verify it equals $\langle\psi|\hat{A}|\psi\rangle = (3+1+1+3)/2/2 = 4$. *(Check: $\bigl(\begin{smallmatrix}1/\sqrt{2}&1/\sqrt{2}\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1/\sqrt{2}\\1/\sqrt{2}\end{smallmatrix}\bigr) = (1/2)(3+1+1+3) = 4$.)*

**Task 4: Degenerate case.** Set $A_{11} = 1$, $A_{22} = 1$, $A_{12} = 0$ (the identity matrix $\hat{I}$). The eigenvalues are both 1 (doubly degenerate). The simulator should flag that the eigenvectors are not unique (any two orthonormal vectors will do). Watch how the eigenvector display changes when you perturb $A_{12}$ by $\epsilon$: as $\epsilon \to 0$, the eigenvectors jump discontinuously. This is why degenerate perturbation theory requires special handling — a small perturbation can completely reorganize the eigenbasis.

---

## References

- Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012, §§1.2–1.5. [verify]
- Sakurai, J. J. and Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021, §§1.3–1.4. [verify]
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994, §1.5. [verify]
- Griffiths, D. J. and Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018, §3.3. [verify]
- Cohen-Tannoudji, C., Diu, B. and Laloë, F. *Quantum Mechanics*, Vol. I. Wiley, 1977, Complements $E_{\mathrm{II}}$ and $F_{\mathrm{III}}$. [verify]
- Reed, M. and Simon, B. *Methods of Modern Mathematical Physics*, Vol. I: Functional Analysis. Academic Press, 1972. [verify] (For students pursuing the rigorous treatment of self-adjoint operators.)
- Marshman, E. and Singh, C. "Investigating and improving student understanding of the probability distributions for measuring physical observables in quantum mechanics." *European Journal of Physics* 38, 025705 (2017). https://doi.org/10.1088/1361-6404/aa57d1 [verify]
- Passante, G. et al. "Examining student use of Dirac notation." *Physical Review Special Topics — Physics Education Research* 11, 020132 (2015). https://doi.org/10.1103/PhysRevSTPER.11.020132 [verify]

---

*Bridge to Chapter 3: The spectral theorem tells you what a single observable looks like and what its measurement outcomes are. The next question is: what happens when you have two observables? Can you measure both simultaneously and obtain definite values for each? The answer is yes — if and only if the two operators commute. The commutator $[\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ measures the obstruction. Chapter 3 derives this, and from it the uncertainty principle as a theorem — a consequence of the commutator algebra, not a statement about measurement disturbance.*
