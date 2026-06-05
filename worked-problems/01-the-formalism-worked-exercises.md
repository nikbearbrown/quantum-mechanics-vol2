# Worked Exercises: The Formalism — Hilbert Space, Dirac Notation, and Operators

*Chapter 1 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can read and write Dirac notation: kets $|\psi\rangle$ as vectors, bras $\langle\phi|$ as linear functionals, the scalar bracket $\langle\phi|\psi\rangle$ versus the operator outer product $|\psi\rangle\langle\phi|$.
- You know the inner product is sesquilinear and conjugate-symmetric — $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$, and the bra of $c|\phi\rangle$ is $c^*\langle\phi|$.
- You can manipulate the three identities: completeness $\sum_n|n\rangle\langle n| = \hat{I}$, orthonormality $\langle m|n\rangle = \delta_{mn}$, and expansion $|\psi\rangle = \sum_n c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$.

---

## Part A — Full Worked Example

**What this demonstrates:** That the expectation value of an operator is a basis-independent number, computed either by inserting completeness to get a discrete eigenbasis sum or by working directly in the original basis.

**The problem:** A qubit is prepared in the state $|\psi\rangle = \tfrac{3}{5}|0\rangle + \tfrac{4}{5}|1\rangle$ in the $\sigma_z$ eigenbasis $\{|0\rangle, |1\rangle\}$. Compute $\langle\sigma_x\rangle$ two ways — once by inserting the completeness relation over the $\sigma_x$ eigenbasis, and once by direct matrix evaluation in the $\{|0\rangle,|1\rangle\}$ basis — and confirm the two routes agree.

**The solution:**

**Step 1 — Fix the eigenbasis of the operator.**
The $\sigma_x$ eigenstates are $|+\rangle = \tfrac{1}{\sqrt 2}(|0\rangle + |1\rangle)$ and $|-\rangle = \tfrac{1}{\sqrt 2}(|0\rangle - |1\rangle)$, with eigenvalues $a_+ = +1$ and $a_- = -1$, so $\sigma_x|\pm\rangle = \pm|\pm\rangle$.
*Why:* $\langle\sigma_x\rangle = \sum_n a_n|\langle a_n|\psi\rangle|^2$ requires the eigenstates and eigenvalues of the operator, not of the basis the state is written in.
*Check:* $\langle+|-\rangle = \tfrac{1}{2}(\langle0|+\langle1|)(|0\rangle-|1\rangle) = \tfrac{1}{2}(1-1) = 0$ — orthonormal, as a Hermitian operator's eigenstates must be.

**Step 2 — Expand the state in the eigenbasis (insert completeness).**
Insert $\hat{I} = |+\rangle\langle+| + |-\rangle\langle-|$ to find the coefficients $c_\pm = \langle\pm|\psi\rangle$:
$$c_+ = \langle+|\psi\rangle = \tfrac{1}{\sqrt2}(\langle0|+\langle1|)\left(\tfrac{3}{5}|0\rangle+\tfrac45|1\rangle\right) = \tfrac{1}{\sqrt2}\cdot\tfrac{7}{5}, \qquad c_- = \tfrac{1}{\sqrt2}\left(\tfrac35-\tfrac45\right) = -\tfrac{1}{\sqrt2}\cdot\tfrac15.$$
*Why:* The completeness relation is the computational engine — it converts the abstract state into concrete components in whichever basis makes the calculation transparent.
*Check (normalization):* $|c_+|^2 + |c_-|^2 = \tfrac{1}{2}\cdot\tfrac{49}{25} + \tfrac12\cdot\tfrac{1}{25} = \tfrac{50}{50} = 1.$ The change of basis preserved the norm.

**Step 3 — Apply the spectral expectation formula.**
$$\langle\sigma_x\rangle = a_+|c_+|^2 + a_-|c_-|^2 = (+1)\tfrac{49}{50} + (-1)\tfrac{1}{50} = \tfrac{48}{50} = \tfrac{24}{25}.$$
*Why:* In the eigenbasis the operator is diagonal, so the expectation value is just the eigenvalue-weighted sum of outcome probabilities.
*Check:* $|c_+|^2 = 49/50$ and $|c_-|^2 = 1/50$ are both in $[0,1]$ and sum to 1 — valid probabilities.

**Step 4 — Cross-check by direct matrix evaluation.**
In the $\{|0\rangle,|1\rangle\}$ basis $\sigma_x = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ and $|\psi\rangle = \bigl(\begin{smallmatrix}3/5\\4/5\end{smallmatrix}\bigr)$:
$$\langle\psi|\sigma_x|\psi\rangle = \begin{pmatrix}\tfrac35 & \tfrac45\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}\tfrac35\\\tfrac45\end{pmatrix} = \begin{pmatrix}\tfrac35 & \tfrac45\end{pmatrix}\begin{pmatrix}\tfrac45\\\tfrac35\end{pmatrix} = \tfrac{12}{25}+\tfrac{12}{25} = \tfrac{24}{25}.$$
*Why:* The expectation value is a property of the operator and state, not of the basis chosen to represent them; both routes must land on the same real number.
*Check:* The bra coefficients are $(\tfrac35)^* = \tfrac35$ and $(\tfrac45)^* = \tfrac45$ — real here, but the conjugate is what the bra always applies.

**Final answer:** $\langle\sigma_x\rangle = \dfrac{24}{25}$, obtained identically by the eigenbasis route and by direct matrix evaluation.

**What made this work:** The central concept is *basis-independence of the operator*. The state $|\psi\rangle$ is one abstract vector; $\sigma_x$ is one abstract operator; the expectation value $\langle\sigma_x\rangle$ is one number. The completeness relation $\sum|a_n\rangle\langle a_n| = \hat I$ lets us slide between representations without changing anything physical. The naive failure is to compute $\langle\psi|\sigma_x|\psi\rangle$ "in the $\sigma_x$ eigenbasis" but forget to re-express the *state* in that basis — mixing components from two different bases, which is dimensionally a category error. Inserting completeness forces the bookkeeping to be consistent.

**Self-explanation prompt:** In your own words, why does inserting $\hat I = \sum_n|a_n\rangle\langle a_n|$ never change the value of an expression, yet make some calculations vastly easier than others?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same principle — basis-independence of an expectation value, evaluated through the eigenbasis and directly.

**The problem:** A qubit is in the state $|\phi\rangle = \tfrac{1}{\sqrt5}|0\rangle + \tfrac{2}{\sqrt5}|1\rangle$ in the $\sigma_z$ eigenbasis. Compute $\langle\sigma_y\rangle$ two ways: (i) expand $|\phi\rangle$ in the $\sigma_y$ eigenbasis $|{\pm}y\rangle = \tfrac{1}{\sqrt2}(|0\rangle \pm i|1\rangle)$ with eigenvalues $\pm1$, apply the spectral sum $\sum_n a_n|\langle a_n|\phi\rangle|^2$; and (ii) evaluate $\langle\phi|\sigma_y|\phi\rangle$ directly with $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Confirm both give the same real number, and verify your coefficients $|c_{\pm y}|^2$ sum to 1.

**Stuck?** The coefficient is $c_{+y} = \langle +y|\phi\rangle$, and remember the bra of $|+y\rangle = \tfrac{1}{\sqrt2}(|0\rangle+i|1\rangle)$ is $\langle +y| = \tfrac{1}{\sqrt2}(\langle0| - i\langle1|)$ — the $i$ conjugates.

*Instructor note: no solution is provided for Part B. Work it fully, then verify your two routes agree and your probabilities are non-negative and sum to one.*

---

## Part C — Completion Problem

**The problem:** A particle in an infinite square well of width $L$ is prepared in the state $|\psi\rangle = \tfrac{1}{\sqrt2}|E_1\rangle + \tfrac{1}{\sqrt2}|E_3\rangle$, a superposition of the first and third energy eigenstates, where $\hat H|E_n\rangle = E_n|E_n\rangle$ with $E_n = n^2 E_1$. Compute $\langle\hat H\rangle$.

**Step 1 — Identify the eigenbasis and the operator's action on it.**
The states $|E_1\rangle, |E_3\rangle$ are orthonormal energy eigenstates, $\langle E_m|E_n\rangle = \delta_{mn}$, and $\hat H$ is diagonal in this basis with eigenvalues $E_1$ and $E_3 = 9E_1$.
*Why:* In its own eigenbasis the Hamiltonian acts by scaling each component by its eigenvalue — this is what makes the energy basis the natural one for $\langle\hat H\rangle$.

**Step 2 — Read off the coefficients and check normalization.**
$c_1 = \langle E_1|\psi\rangle = \tfrac{1}{\sqrt2}$ and $c_3 = \langle E_3|\psi\rangle = \tfrac{1}{\sqrt2}$, so $|c_1|^2 + |c_3|^2 = \tfrac12 + \tfrac12 = 1$.
*Why:* The squared moduli are the outcome probabilities under the Born rule; they must sum to 1 for $|\psi\rangle$ to be a valid normalized state.

**Step 3 — [BLANK]** Apply the spectral expectation formula $\langle\hat H\rangle = \sum_n |c_n|^2 E_n$ to this state.
*Your work here:*

*Why (your explanation):*

**Step 4 — [BLANK]** State and apply the relevant check: confirm that the result lies strictly between the smallest and largest eigenvalues present in the superposition.
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret the relative-phase structure.**
Because $\langle\hat H\rangle$ depends only on $|c_n|^2$, it is unaffected by any relative phase $e^{i\theta}$ attached to $|E_3\rangle$; the energy expectation of a stationary superposition is phase-blind, even though other observables would oscillate.

**Final answer:** $\langle\hat H\rangle = 5E_1$.

**Self-explanation prompt:** Why is an expectation value over a discrete eigenbasis always a weighted average of eigenvalues, and why does that guarantee it lands between the minimum and maximum eigenvalues?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes $\langle\sigma_z\rangle$ for the un-normalized vector $|\chi\rangle = 2|0\rangle + i|1\rangle$ (written in the $\sigma_z$ eigenbasis), where $\sigma_z|0\rangle = +|0\rangle$ and $\sigma_z|1\rangle = -|1\rangle$. Here is their work.

**Step 1 — Identify outcomes and amplitudes.**
The possible outcomes are $+1$ (for $|0\rangle$) and $-1$ (for $|1\rangle$); the amplitudes are $\langle0|\chi\rangle = 2$ and $\langle1|\chi\rangle = i$. *(Correct.)*

**Step 2 — Form squared moduli.**
$|\langle0|\chi\rangle|^2 = 4$ and $|\langle1|\chi\rangle|^2 = |i|^2 = 1$. *(Correct.)*

**Step 3 — ⚠ Apply the Born rule to get probabilities and the expectation value.**
"$P(+1) = 4$ and $P(-1) = 1$, so $\langle\sigma_z\rangle = (+1)(4) + (-1)(1) = 3.$"

**Step 4 — Sanity statement.**
"Since $\langle\sigma_z\rangle$ should lie in $[-1, +1]$ for $\sigma_z$, and I got $3$, the spin is strongly aligned with $+z$." *(Follows from Step 3, and is stated plausibly — but rests on the Step 3 error.)*

**Your tasks:**
1. Identify the exact physics misconception in Step 3 and state it precisely.
2. Correct the calculation: normalize $|\chi\rangle$ first, then recompute $P(\pm1)$ and $\langle\sigma_z\rangle$.
3. Explain why $P(+1) = 4$ should have been an immediate red flag.
4. Show that once normalized, $\langle\sigma_z\rangle$ falls inside $[-1,+1]$, and state the correct value.

**Why this error is common:** The Born rule $P(a_n) = |\langle a_n|\psi\rangle|^2$ assumes $|\psi\rangle$ is normalized, and students routinely apply it to raw, un-normalized vectors — forgetting that the squared amplitudes are probabilities only after dividing by $\langle\chi|\chi\rangle$.

---

## Part E — Transfer Problem

**What this demonstrates:** The same principle — expectation value as a basis-independent, completeness-mediated quantity — applied to a context not treated in the chapter: a three-state quantum system (a "qutrit").

**The problem:** A qutrit lives in $\mathbb{C}^3$ with orthonormal basis $\{|0\rangle, |1\rangle, |2\rangle\}$. An observable has the action $\hat A|0\rangle = 0$, $\hat A|1\rangle = 2|1\rangle$, $\hat A|2\rangle = -1|2\rangle$ (so this basis is its eigenbasis, eigenvalues $0, 2, -1$). The system is in the state
$$|\psi\rangle = \tfrac{1}{\sqrt6}\bigl(|0\rangle + 2|1\rangle + i|2\rangle\bigr).$$
Compute $\langle\hat A\rangle$ using the spectral sum, verify the state is normalized, and confirm $\langle\hat A\rangle$ lies between the smallest and largest eigenvalues.

**Hint (use only if stuck after 10 minutes):** The coefficients are already the components in $\hat A$'s eigenbasis. Compute $|c_n|^2 = |\langle n|\psi\rangle|^2$ for $n = 0,1,2$; the phase $i$ on $|2\rangle$ disappears under the modulus.

**Reflection prompt:**
1. How did the structure of this $\mathbb{C}^3$ problem map onto the $\mathbb{C}^2$ worked example in Part A — what played the role of "eigenbasis," "coefficients," and "eigenvalues"?
2. The chapter says the abstract formalism "handles both finite and infinite dimensions without modification." What single change would turn this qutrit calculation into one for a particle on a line?

---

## Part F — Interleaved Review

**Problem F1.** A qubit is in $|\psi\rangle = \cos\tfrac{\theta}{2}|0\rangle + e^{i\phi}\sin\tfrac{\theta}{2}|1\rangle$ with $(\theta,\phi) = (\pi/3, \pi/4)$. (a) Read off $c_0$ and $c_1$. (b) Verify $|c_0|^2 + |c_1|^2 = 1$ explicitly. (c) Compute $\langle\sigma_z\rangle$ via the spectral sum and confirm it equals $\cos\theta$.
*Chapter this draws from: Chapter 1.*

**Problem F2.** Show that the Pauli matrix $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$ is Hermitian by checking $A_{mn} = A_{nm}^*$ entry by entry, and exhibit explicitly why its *plain* transpose is $-\sigma_y$ while its *conjugate* transpose is $+\sigma_y$. State the one-sentence reason "Hermitian means symmetric" is a wrong habit in the complex case.
*Chapter this draws from: The Formalism (Chapter 1, adjoints and Hermiticity).*

**Problem F3.** You are given the vector $|\chi\rangle = 3|0\rangle - 4|1\rangle$ and asked for "the probability of measuring $+1$." 
*Note to instructor: this problem is intentionally ambiguous — it does not state which observable is measured, nor whether $|\chi\rangle$ is normalized. A strong student will notice both gaps: identify that "$+1$" is meaningless without naming an operator (e.g. $\sigma_z$ vs $\sigma_x$), and that the Born rule requires normalizing $|\chi\rangle$ by $\langle\chi|\chi\rangle = 25$ first. The discrimination skill is recognizing what must be specified before the formalism can produce a number.*

**Closing reflection:** Across F1–F3, the recurring move is the same: pin down the operator, express the state in that operator's eigenbasis, normalize, then square the moduli. Which of the three problems required you to *supply* missing structure rather than just execute, and what does that tell you about reading physics problems critically?

---

## Instructor Notes

**Common errors:**
- Applying the Born rule to an un-normalized state (treating $|\langle a_n|\psi\rangle|^2$ as a probability without dividing by $\langle\psi|\psi\rangle$).
- Forgetting the conjugate in the bra — writing $\langle+y| = \tfrac{1}{\sqrt2}(\langle0| + i\langle1|)$ instead of $\tfrac{1}{\sqrt2}(\langle0| - i\langle1|)$, which corrupts every overlap.
- Mixing components from two different bases when "computing in the eigenbasis" — using the $\sigma_z$-basis coefficients with the $\sigma_x$ eigenvalues.

**Signs a student needs to return:**
- They report a probability greater than 1 or an expectation value outside the eigenvalue range and do not flag it as impossible.
- They cannot state, unprompted, that $\langle\phi|\psi\rangle$ is a scalar while $|\psi\rangle\langle\phi|$ is an operator.

**Scaffolding adjustments:** If a student struggles with Part A, have them first compute only the direct matrix route (Step 4) and confirm the answer, then return to the eigenbasis route (Steps 1–3) with the target number already known. If a student finishes Part F quickly, ask them to redo F1 part (c) for $\langle\sigma_x\rangle$ and predict, before computing, whether the answer depends on $\phi$ (it does) versus $\langle\sigma_z\rangle$ (it does not).

**Domain adaptation note:** For a class emphasizing quantum information, recast every problem in qubit/Bloch-sphere language; for a class emphasizing wave mechanics, replace the discrete sums with position-basis integrals $\int\phi^*(x)\psi(x)\,dx$ to make the continuous completeness relation $\int|x\rangle\langle x|\,dx = \hat I$ concrete.
