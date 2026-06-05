# Worked Exercises: Observables, Hermiticity, and the Spectral Theorem

*Chapter 2 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can test the Hermitian condition $A_{mn} = A_{nm}^*$ on a $2\times2$ matrix and distinguish it from plain transpose symmetry.
- You can find eigenvalues from the secular equation $\det(\hat A - \lambda\hat I) = 0$ and use the trace/determinant cross-checks $\sum\lambda_n = \mathrm{Tr}$, $\prod\lambda_n = \det$.
- You know the spectral decomposition $\hat A = \sum_n a_n|a_n\rangle\langle a_n|$, the projector properties ($\hat P_n^2 = \hat P_n$, $\hat P_n^\dagger = \hat P_n$, $\sum_n\hat P_n = \hat I$), and the Born rule $P(a_n) = |\langle a_n|\psi\rangle|^2$.

---

## Part A — Full Worked Example

**What this demonstrates:** That diagonalizing a Hermitian observable produces its complete spectral decomposition, and that the Born rule and the spectral expectation formula then agree with a direct matrix calculation.

**The problem:** Diagonalize the Hermitian observable
$$\hat A = \begin{pmatrix} 1 & 2i \\ -2i & 1 \end{pmatrix},$$
write its spectral decomposition, and use it to compute $\langle\hat A\rangle$ and the measurement probabilities for the state $|\psi\rangle = |0\rangle = \bigl(\begin{smallmatrix}1\\0\end{smallmatrix}\bigr)$. Cross-check the expectation against the direct matrix product.

**The solution:**

**Step 1 — Verify Hermiticity before doing anything else.**
$A_{12} = 2i$ and $A_{21} = -2i = (2i)^* = A_{12}^*$; diagonal entries $1, 1$ are real.
*Why:* Only Hermitian operators are guaranteed real eigenvalues and an orthonormal eigenbasis — the spectral theorem applies only after this check passes.
*Check:* $\hat A^\dagger = \bigl(\begin{smallmatrix}1&2i\\-2i&1\end{smallmatrix}\bigr) = \hat A$. Hermitian confirmed.

**Step 2 — Solve the secular equation for the eigenvalues.**
$$\det(\hat A - \lambda\hat I) = (1-\lambda)^2 - (2i)(-2i) = (1-\lambda)^2 - 4 = 0 \implies 1-\lambda = \pm2,$$
so $\lambda_+ = 3$, $\lambda_- = -1$.
*Why:* The roots of the characteristic polynomial are the possible measurement outcomes; for a Hermitian operator they must be real.
*Check:* $\lambda_+ + \lambda_- = 2 = \mathrm{Tr}(\hat A)$ ✓; $\lambda_+\lambda_- = -3 = \det(\hat A)$ ✓. Both real.

**Step 3 — Solve the homogeneous system for the eigenvectors.**
For $\lambda_+ = 3$: $(\hat A - 3\hat I)|a_+\rangle = 0$ gives the first row $-2x + 2iy = 0 \Rightarrow x = iy$. Normalizing $|x|^2+|y|^2 = 1$ with $y = 1/\sqrt2$:
$$|a_+\rangle = \tfrac{1}{\sqrt2}\begin{pmatrix} i \\ 1\end{pmatrix}.$$
For $\lambda_- = -1$: $2x + 2iy = 0 \Rightarrow x = -iy$, giving $|a_-\rangle = \tfrac{1}{\sqrt2}\bigl(\begin{smallmatrix}-i\\1\end{smallmatrix}\bigr)$.
*Why:* You cannot read eigenvectors off a non-diagonal matrix; you must substitute each eigenvalue and solve the homogeneous system.
*Check (orthogonality):* $\langle a_+|a_-\rangle = \tfrac12(\overline{i}\cdot(-i) + 1\cdot1) = \tfrac12((-i)(-i)+1) = \tfrac12(-1+1) = 0$ ✓ — distinct eigenvalues give orthogonal eigenstates.

**Step 4 — Assemble the spectral decomposition and verify completeness.**
$$\hat A = \lambda_+|a_+\rangle\langle a_+| + \lambda_-|a_-\rangle\langle a_-| = 3\hat P_+ - \hat P_-, \quad \hat P_\pm = |a_\pm\rangle\langle a_\pm|.$$
Explicitly $\hat P_+ = \tfrac12\bigl(\begin{smallmatrix}1 & i\\ -i & 1\end{smallmatrix}\bigr)$ and $\hat P_- = \tfrac12\bigl(\begin{smallmatrix}1 & -i\\ i & 1\end{smallmatrix}\bigr)$.
*Why:* The spectral decomposition encodes everything about the observable — outcomes, the states giving each with certainty, and (via the projectors) the probabilities.
*Check (completeness):* $\hat P_+ + \hat P_- = \tfrac12\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr) = \hat I$ ✓. And $\hat P_+^2 = \hat P_+$ since $\langle a_+|a_+\rangle = 1$.

**Step 5 — Apply the Born rule and cross-check the expectation.**
For $|\psi\rangle = |0\rangle$: $P(\lambda_+) = |\langle a_+|0\rangle|^2 = \bigl|\tfrac{1}{\sqrt2}\overline{i}\bigr|^2 = \tfrac12$, and $P(\lambda_-) = \tfrac12$. Then
$$\langle\hat A\rangle = \lambda_+P(\lambda_+) + \lambda_-P(\lambda_-) = 3\cdot\tfrac12 + (-1)\cdot\tfrac12 = 1.$$
Direct: $\langle0|\hat A|0\rangle = \bigl(\begin{smallmatrix}1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1\\-2i\end{smallmatrix}\bigr) = 1$.
*Why:* The probability is the squared modulus of the amplitude $\langle a_n|\psi\rangle$, not the amplitude itself; the spectral and direct routes must coincide.
*Check:* $P(\lambda_+) + P(\lambda_-) = 1$ ✓; both routes give $\langle\hat A\rangle = 1$, which lies in $[-1, 3]$ ✓.

**Final answer:** Eigenvalues $\lambda_\pm = 3, -1$; spectral decomposition $\hat A = 3\hat P_+ - \hat P_-$; in $|0\rangle$ the probabilities are $\tfrac12, \tfrac12$ and $\langle\hat A\rangle = 1$.

**What made this work:** The central concept is the *spectral theorem*: a Hermitian operator is fully captured by its real eigenvalues and orthonormal projectors. Diagonalizing finds the basis in which the measurement is transparent. The naive failure is to try to read eigenvectors off the matrix directly (only valid for diagonal matrices) or to report $\langle a_n|\psi\rangle$ as the probability — an amplitude, complex, in the Hilbert space — rather than its squared modulus $|\langle a_n|\psi\rangle|^2$, a real frequency of outcomes.

**Self-explanation prompt:** Why does the spectral decomposition $\hat A = \sum_n a_n\hat P_n$ contain strictly more information than just the list of eigenvalues, and where does the extra information live?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same principle — diagonalize a Hermitian observable, build its spectral decomposition, and reconcile the Born-rule expectation with the direct matrix calculation — for a different matrix and state.

**The problem:** Diagonalize the Hermitian observable
$$\hat B = \begin{pmatrix} 2 & 1-i \\ 1+i & 1 \end{pmatrix}.$$
(a) Confirm Hermiticity. (b) Find the eigenvalues and verify them against the trace and determinant. (c) Find and normalize the eigenvectors and verify they are orthogonal. (d) Write the spectral decomposition $\hat B = \lambda_1\hat P_1 + \lambda_2\hat P_2$ and check $\hat P_1 + \hat P_2 = \hat I$. (e) For $|\psi\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, compute the outcome probabilities via the Born rule and confirm $\sum_n a_n P(a_n)$ equals the direct $\langle\psi|\hat B|\psi\rangle$.

**Stuck?** Start with $\det(\hat B - \lambda\hat I) = (2-\lambda)(1-\lambda) - (1-i)(1+i)$ and note $(1-i)(1+i) = |1+i|^2 = 2$ before expanding the quadratic.

*Instructor note: no solution is provided for Part B. Carry out all five parts and verify Hermiticity, the trace/det checks, orthogonality, completeness, and the agreement of the two expectation routes.*

---

## Part C — Completion Problem

**The problem:** Construct the time-evolution operator for the Hamiltonian $\hat H = E_0\sigma_z = E_0\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$ using its spectral decomposition, and evolve $|\psi(0)\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$.

**Step 1 — Write the spectral decomposition of $\hat H$.**
$\hat H$ is already diagonal: $\hat H = E_0|0\rangle\langle0| - E_0|1\rangle\langle1| = E_0\hat P_0 - E_0\hat P_1$, with eigenvalues $E_+ = E_0$ (state $|0\rangle$) and $E_- = -E_0$ (state $|1\rangle$).
*Why:* The energy eigenbasis is where the Hamiltonian acts by simple scaling, so functions of $\hat H$ are built term by term on the projectors.

**Step 2 — Use the function-of-operator rule to build $\hat U(t)$.**
By $f(\hat H) = \sum_n f(E_n)\hat P_n$ with $f(E) = e^{-iEt/\hbar}$:
$$\hat U(t) = e^{-iE_0t/\hbar}|0\rangle\langle0| + e^{+iE_0t/\hbar}|1\rangle\langle1| = \begin{pmatrix} e^{-iE_0t/\hbar} & 0 \\ 0 & e^{+iE_0t/\hbar}\end{pmatrix}.$$
*Why:* The spectral theorem lets us define any function of a Hermitian operator by applying that function to the eigenvalues — this is exactly how $e^{-i\hat Ht/\hbar}$ is constructed.

**Step 3 — [BLANK]** Apply $\hat U(t)$ to $|\psi(0)\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$ to obtain $|\psi(t)\rangle$.
*Your work here:*

*Why (your explanation):*

**Step 4 — [BLANK]** Compute $\langle\hat H\rangle$ at time $t$ and show it is constant. Then verify $\langle\psi(t)|\psi(t)\rangle = 1$ (unitarity / norm preservation).
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret the dynamics.**
The two components acquire opposite phases $e^{\mp iE_0t/\hbar}$, so the relative phase $e^{2iE_0t/\hbar}$ drives observables like $\langle\sigma_x\rangle$ to oscillate at the Bohr frequency $2E_0/\hbar = (E_+ - E_-)/\hbar$, even though $\langle\hat H\rangle$ itself never changes.

**Final answer:** $|\psi(t)\rangle = \tfrac{1}{\sqrt2}\bigl(e^{-iE_0t/\hbar}|0\rangle + e^{+iE_0t/\hbar}|1\rangle\bigr)$, with $\langle\hat H\rangle = 0$ for all $t$ and norm $1$.

**Self-explanation prompt:** Why does building $\hat U(t)$ from the spectral decomposition guarantee it is unitary without any extra check, and what property of the eigenvalues makes $|e^{-iE_nt/\hbar}| = 1$?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked for the probability of measuring outcome $+1$ when the observable $\sigma_z$ is measured on the state $|\psi\rangle = \tfrac{3}{5}|0\rangle + \tfrac{4i}{5}|1\rangle$, where $\sigma_z|0\rangle = +|0\rangle$, $\sigma_z|1\rangle = -|1\rangle$. Here is their work.

**Step 1 — Identify the eigenstate for outcome $+1$.**
Outcome $+1$ corresponds to eigenstate $|0\rangle$. *(Correct.)*

**Step 2 — Compute the amplitude.**
$\langle0|\psi\rangle = \tfrac35$. *(Correct.)*

**Step 3 — ⚠ State the probability.**
"The probability of measuring $+1$ is the amplitude itself: $P(+1) = \langle0|\psi\rangle = \tfrac35 = 0.6$. Similarly $P(-1) = \langle1|\psi\rangle = \tfrac{4i}{5}$."

**Step 4 — Normalization remark.**
"Adding them, $P(+1) + P(-1) = \tfrac35 + \tfrac{4i}{5}$, which has modulus $1$, so the probabilities are consistent." *(The modulus is indeed 1 — so this step looks like a valid check, but it is reconciling the wrong objects.)*

**Your tasks:**
1. Name the precise misconception in Step 3 and explain the difference between the two objects being conflated.
2. Correct the calculation: compute $P(+1)$ and $P(-1)$ as $|\langle a_n|\psi\rangle|^2$.
3. Explain why getting a complex number for "$P(-1) = \tfrac{4i}{5}$" should have stopped the student immediately.
4. Show that the corrected probabilities are real, non-negative, and sum to 1, and state the correct $P(+1)$.

**Why this error is common:** Writing "the probability is $\langle a_n|\psi\rangle$" and obtaining a complex number is the single most common error in quantum mechanics — it conflates an amplitude (complex, lives in Hilbert space) with a probability (real, non-negative, a frequency of outcomes), which differ by taking the modulus squared.

---

## Part E — Transfer Problem

**What this demonstrates:** The same principle — Hermiticity forcing real eigenvalues and the spectral decomposition organizing measurement — applied to a context outside the chapter's examples: a real symmetric observable built from a graph (the adjacency operator of a two-site system with a self-loop).

**The problem:** Consider the Hermitian operator
$$\hat A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$$
(a real symmetric matrix, so automatically Hermitian). (a) Confirm it is Hermitian. (b) Find its eigenvalues from the secular equation and verify the trace/det checks. (c) Find and normalize the eigenvectors. (d) Write the spectral decomposition. (e) For the state $|\psi\rangle = |0\rangle$, compute the two outcome probabilities and $\langle\hat A\rangle$, and verify against the direct matrix product. The eigenvalues will be irrational — that is fine; the spectral theorem guarantees they are real.

**Hint (use only if stuck after 10 minutes):** The secular equation is $\lambda^2 - \lambda - 1 = 0$, whose roots are the golden ratio and its conjugate, $\lambda_\pm = \tfrac{1\pm\sqrt5}{2}$. Keep them symbolic; you do not need decimals.

**Reflection prompt:**
1. Real symmetric matrices are automatically Hermitian — which part of the Hermitian condition $A_{mn} = A_{nm}^*$ becomes trivial when all entries are real, and why does that not make Hermiticity unnecessary in general?
2. The spectral theorem "guarantees eigenvalues exist and are real but does not provide a formula." Where did that show up here, and how would the situation change for a $10\times10$ version of this matrix?

---

## Part F — Interleaved Review

**Problem F1.** The observable $\hat M = \bigl(\begin{smallmatrix}0 & e^{i\phi}\\ e^{-i\phi} & 0\end{smallmatrix}\bigr)$ for real $\phi$. (a) Verify Hermiticity. (b) Show the eigenvalues are $\pm1$, independent of $\phi$. (c) Find the eigenstates and show they *do* depend on $\phi$. (d) Explain physically why the eigenvalues (measurement outcomes) are $\phi$-independent while the eigenstates (which states give those outcomes with certainty) are not.
*Chapter this draws from: Chapter 2.*

**Problem F2.** Using the three identities of the formalism, show that for any orthonormal basis $\{|n\rangle\}$ and any state $|\psi\rangle$, inserting completeness gives $\langle\psi|\psi\rangle = \sum_n |\langle n|\psi\rangle|^2$. Then state why this expression being $1$ is the normalization condition, and contrast the scalar $\langle\phi|\psi\rangle$ with the operator $|\psi\rangle\langle\phi|$.
*Chapter this draws from: The Formalism (Chapter 1, completeness and the bra/ket category distinction).*

**Problem F3.** You are handed the $2\times2$ matrix $\bigl(\begin{smallmatrix}1 & 1\\ 0 & 2\end{smallmatrix}\bigr)$ and asked: "What are the measurement outcomes and their probabilities for the state $|0\rangle$?"
*Note to instructor: this problem is intentionally ambiguous and partly a trap — the matrix is upper-triangular with real diagonal, so it has real eigenvalues (1 and 2), which tempts a student to treat it as an observable. But it is not Hermitian ($A_{12} = 1 \neq 0 = A_{21}^*$), so its eigenvectors are not orthogonal and the Born-rule machinery does not apply. The discrimination skill is recognizing that real eigenvalues do not certify an observable; only Hermiticity does, and the question as posed has no well-defined probability interpretation.*

**Closing reflection:** Across F1–F3, the load-bearing check appears again and again: is the operator Hermitian? F1 and F2 rest on it implicitly; F3 fails precisely because it is absent. Why is Hermiticity, and not merely "real eigenvalues," the gatekeeper for the entire measurement formalism?

---

## Instructor Notes

**Common errors:**
- Reporting the amplitude $\langle a_n|\psi\rangle$ as the probability instead of $|\langle a_n|\psi\rangle|^2$ — the chapter's named "most common error in quantum mechanics."
- Assuming a non-Hermitian operator with real eigenvalues (e.g. an upper-triangular matrix) is a valid observable with orthogonal eigenstates.
- Trying to read eigenvectors off a non-diagonal matrix without solving the homogeneous system.

**Signs a student needs to return:**
- They obtain a complex or negative "probability" and do not recognize it as impossible.
- They cannot state why eigenvalues of a Hermitian operator must be real (cannot reproduce the four-line $a = a^*$ argument).

**Scaffolding adjustments:** If a student struggles with Part A, give them the eigenvalues and have them verify the trace/det checks first, then only solve for the eigenvectors — separating "find the outcomes" from "find the states." If a student finishes Part F quickly, ask them to construct a non-Hermitian matrix with two real but unequal eigenvalues and show explicitly that its eigenvectors are *not* orthogonal, cementing why Hermiticity is the real requirement.

**Domain adaptation note:** For a quantum-information course, frame every observable as a Pauli combination $\vec a\cdot\vec\sigma$ and connect eigenvalues $\pm|\vec a|$ to measurement on the Bloch sphere; for a chemistry/spectroscopy course, frame the Hermitian matrix as a small effective Hamiltonian whose real eigenvalues are spectral line energies.
