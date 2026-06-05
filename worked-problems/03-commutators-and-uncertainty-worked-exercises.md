# Worked Exercises: Commutators, Compatibility, and the Generalized Uncertainty Principle

*Chapter 3 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can compute a commutator $[\hat A,\hat B] = \hat A\hat B - \hat B\hat A$, by direct matrix multiplication and using the identity $[\hat A^2,\hat B] = \hat A[\hat A,\hat B] + [\hat A,\hat B]\hat A$.
- You know the canonical commutation relation $[\hat x,\hat p] = i\hbar$, the Pauli/spin algebra (e.g. $[\hat S_x,\hat S_z] = -i\hbar\hat S_y$), and the meaning of compatible vs. incompatible operators.
- You can state and apply the Robertson bound $\sigma_A\sigma_B \geq \tfrac12|\langle[\hat A,\hat B]\rangle|$ and compute a variance $\sigma_A^2 = \langle\hat A^2\rangle - \langle\hat A\rangle^2$.

---

## Part A — Full Worked Example

**What this demonstrates:** That the Robertson bound for a spin pair is state-dependent through $\langle\hat S_y\rangle$, and that you confirm it by independently computing both the bound and the actual standard deviations from the state.

**The problem:** A spin-½ is in the state $|+y\rangle = \tfrac{1}{\sqrt2}(|\!\uparrow\rangle + i|\!\downarrow\rangle)$, the $\hat S_y$ eigenstate. Evaluate the Robertson bound for the pair $\hat S_x, \hat S_z$, compute the actual spreads $\sigma_{S_x}$ and $\sigma_{S_z}$, and determine whether the bound is saturated.

**The solution:**

**Step 1 — Compute the commutator that sets the bound.**
Using $\hat S_i = \tfrac{\hbar}{2}\sigma_i$ and $[\sigma_x,\sigma_z] = -2i\sigma_y$:
$$[\hat S_x,\hat S_z] = \tfrac{\hbar^2}{4}[\sigma_x,\sigma_z] = \tfrac{\hbar^2}{4}(-2i\sigma_y) = -i\hbar\hat S_y.$$
So Robertson reads $\sigma_{S_x}\sigma_{S_z} \geq \tfrac{\hbar}{2}|\langle\hat S_y\rangle|$.
*Why:* The right-hand side of Robertson is fixed by the commutator; here the commutator is itself an operator ($\hat S_y$), so the bound depends on the state through $\langle\hat S_y\rangle$.
*Check (sign):* $[\sigma_x,\sigma_z] = \sigma_x\sigma_z - \sigma_z\sigma_x$; with $\sigma_x\sigma_z = -i\sigma_y$ and $\sigma_z\sigma_x = +i\sigma_y$ this gives $-2i\sigma_y$ ✓ — the canonical sign trap avoided.

**Step 2 — Evaluate $\langle\hat S_y\rangle$ in the given state.**
With $|+y\rangle = \tfrac{1}{\sqrt2}\bigl(\begin{smallmatrix}1\\i\end{smallmatrix}\bigr)$ and $\hat S_y = \tfrac{\hbar}{2}\bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$:
$$\langle\hat S_y\rangle = \tfrac{\hbar}{2}\cdot\tfrac12\begin{pmatrix}1 & -i\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}1\\i\end{pmatrix} = \tfrac{\hbar}{4}\begin{pmatrix}1 & -i\end{pmatrix}\begin{pmatrix}1\\i\end{pmatrix} = \tfrac{\hbar}{4}(1+1) = \tfrac{\hbar}{2}.$$
*Why:* $|+y\rangle$ is the $+\hbar/2$ eigenstate of $\hat S_y$, so its $\hat S_y$ expectation is the eigenvalue $\hbar/2$ — making the bound maximal for this pair.
*Check:* The bra of $|+y\rangle$ is $\tfrac{1}{\sqrt2}(\langle\!\uparrow| - i\langle\!\downarrow|)$, i.e. row $(1, -i)/\sqrt2$ — the $i$ conjugated correctly.

**Step 3 — Apply the Robertson bound.**
$$\sigma_{S_x}\sigma_{S_z} \geq \tfrac{\hbar}{2}\cdot\tfrac{\hbar}{2} = \tfrac{\hbar^2}{4}.$$
*Why:* This is the binding lower bound on the product of spreads, now a concrete number because $\langle\hat S_y\rangle$ is maximal in this state.
*Check:* The bound has units of $\hbar^2$ ✓, matching a product of two angular-momentum spreads.

**Step 4 — Compute the actual spreads independently.**
In $|+y\rangle$, $\langle\hat S_x\rangle = \langle\hat S_z\rangle = 0$ (the Bloch vector points along $+\hat y$, with zero $x$ and $z$ components). Since $\sigma_x^2 = \sigma_z^2 = I$, $\langle\hat S_x^2\rangle = \langle\hat S_z^2\rangle = \hbar^2/4$. Therefore
$$\sigma_{S_x}^2 = \tfrac{\hbar^2}{4} - 0 = \tfrac{\hbar^2}{4}, \quad \sigma_{S_z}^2 = \tfrac{\hbar^2}{4}, \quad \sigma_{S_x} = \sigma_{S_z} = \tfrac{\hbar}{2}.$$
*Why:* The variance is $\langle\hat A^2\rangle - \langle\hat A\rangle^2$; with zero means, both spreads equal the maximal $\hbar/2$ — maximal uncertainty in $x$ and $z$ for the state sharp in $y$.
*Check:* $\langle\hat S_x^2\rangle = \hbar^2/4 \geq \langle\hat S_x\rangle^2 = 0$ ✓ — variance non-negative.

**Step 5 — Compare product to bound and test saturation.**
$$\sigma_{S_x}\sigma_{S_z} = \tfrac{\hbar}{2}\cdot\tfrac{\hbar}{2} = \tfrac{\hbar^2}{4} = \text{the bound}.$$
*Why:* The product equals the bound exactly, so the inequality is saturated — the anticommutator term dropped in Step 4 of the Robertson proof vanishes for this state.
*Check:* Product $\tfrac{\hbar^2}{4} \geq$ bound $\tfrac{\hbar^2}{4}$ holds with equality ✓.

**Final answer:** The Robertson bound is $\sigma_{S_x}\sigma_{S_z}\geq\hbar^2/4$, the actual product is $\hbar^2/4$, and the bound is **exactly saturated** at the $\hat S_y$ eigenstate.

**What made this work:** The central concept is the *state-dependence of the Robertson bound* when the commutator is an operator. The bound is not a fixed number like $\hbar/2$ for $\hat x,\hat p$; it tracks $|\langle\hat S_y\rangle|$ across the Bloch sphere. The naive failure is to assume non-commuting observables can never both be uncertain-but-bounded, or to forget that a *maximal* bound is achieved precisely where the state is sharp in the third direction — the state most constrained in $y$ is maximally uncertain in $x$ and $z$. A second naive failure is a sign error in $[\sigma_x,\sigma_z]$, which flips the bound's apparent source.

**Self-explanation prompt:** Why is the Robertson bound *maximized* exactly at the state that is sharp in $\hat S_y$, and what would the bound become at the $\hat S_x$ eigenstate instead?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same principle — a state-dependent Robertson bound for spin, with independent computation of bound and spreads — for a different operator pair and state.

**The problem:** A spin-½ is in the state $|\!\uparrow\rangle$ (the $\hat S_z$ eigenstate, north pole of the Bloch sphere). Consider the pair $\hat S_x, \hat S_y$. (a) Compute $[\hat S_x,\hat S_y]$ and write the Robertson bound in terms of $\langle\hat S_z\rangle$. (b) Evaluate $\langle\hat S_z\rangle$ in this state. (c) State the resulting numerical bound. (d) Compute the actual spreads $\sigma_{S_x}$ and $\sigma_{S_y}$. (e) Determine whether the bound is saturated, binding, or merely satisfied with slack — and interpret what a maximal bound here means geometrically.

**Stuck?** The angular-momentum/spin commutator you need is $[\hat S_x,\hat S_y] = i\hbar\hat S_z$ (note the sign differs from the worked example's pair). At the north pole, $\langle\hat S_z\rangle$ is the eigenvalue $+\hbar/2$.

*Instructor note: no solution is provided for Part B. Compute the commutator, the bound, and both spreads independently, then decide whether the inequality is saturated or has slack and explain the geometry.*

---

## Part C — Completion Problem

**The problem:** Verify that $\hat L^2$ and $\hat L_z$ are compatible by computing $[\hat L^2,\hat L_z]$, given the angular-momentum commutators $[\hat L_x,\hat L_z] = -i\hbar\hat L_y$ and $[\hat L_y,\hat L_z] = i\hbar\hat L_x$.

**Step 1 — Expand $\hat L^2$ and distribute the commutator.**
$\hat L^2 = \hat L_x^2 + \hat L_y^2 + \hat L_z^2$, and the commutator is linear:
$$[\hat L^2,\hat L_z] = [\hat L_x^2,\hat L_z] + [\hat L_y^2,\hat L_z] + [\hat L_z^2,\hat L_z].$$
*Why:* The third term vanishes since any operator commutes with a function of itself, so only the $x$ and $y$ pieces can contribute.

**Step 2 — Apply the square-commutator identity to the first two terms.**
Using $[\hat A^2,\hat B] = \hat A[\hat A,\hat B] + [\hat A,\hat B]\hat A$:
$$[\hat L_x^2,\hat L_z] = \hat L_x(-i\hbar\hat L_y) + (-i\hbar\hat L_y)\hat L_x = -i\hbar(\hat L_x\hat L_y + \hat L_y\hat L_x).$$
*Why:* This identity converts a commutator of a *square* into single commutators, each of which we know from the angular-momentum algebra.

**Step 3 — [BLANK]** Apply the same identity to $[\hat L_y^2,\hat L_z]$ using $[\hat L_y,\hat L_z] = i\hbar\hat L_x$.
*Your work here:*

*Why (your explanation):*

**Step 4 — [BLANK]** Add the results of Steps 2 and 3 and show they cancel.
*Your work here:*

*Why (your explanation):*

**Step 5 — State the physical consequence.**
Since $[\hat L^2,\hat L_z] = 0$, the two operators are compatible: they share a complete eigenbasis (the spherical harmonics $Y_\ell^m$), and $\ell$ and $m$ can simultaneously label every state. The quantum numbers are forced by commutativity, not chosen by convention.

**Final answer:** $[\hat L^2,\hat L_z] = -i\hbar(\hat L_x\hat L_y + \hat L_y\hat L_x) + i\hbar(\hat L_x\hat L_y + \hat L_y\hat L_x) = 0$ — compatible.

**Self-explanation prompt:** Why does $[\hat L^2,\hat L_z] = 0$ guarantee that $Y_\ell^m$ can be a simultaneous eigenfunction of both operators, and what would go wrong with the labeling if the commutator were nonzero?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student applies the Robertson bound to $\hat S_x$ and $\hat S_z$ for a spin-½ in the state $|\!\uparrow_x\rangle = \tfrac{1}{\sqrt2}(|\!\uparrow\rangle + |\!\downarrow\rangle)$, the $\hat S_x$ eigenstate. Here is their work.

**Step 1 — Identify the commutator.**
$[\hat S_x,\hat S_z] = -i\hbar\hat S_y$, so the bound is $\sigma_{S_x}\sigma_{S_z} \geq \tfrac{\hbar}{2}|\langle\hat S_y\rangle|$. *(Correct.)*

**Step 2 — Evaluate $\langle\hat S_y\rangle$.**
In $|\!\uparrow_x\rangle = \tfrac{1}{\sqrt2}\bigl(\begin{smallmatrix}1\\1\end{smallmatrix}\bigr)$, $\langle\hat S_y\rangle = \tfrac{\hbar}{4}\begin{pmatrix}1&1\end{pmatrix}\bigl(\begin{smallmatrix}-i\\i\end{smallmatrix}\bigr) = \tfrac{\hbar}{4}(-i+i) = 0$. So the bound is $0$. *(Correct.)*

**Step 3 — ⚠ Conclude about the spreads.**
"Since the Robertson bound is zero, the inequality places no constraint, which means both $\hat S_x$ and $\hat S_z$ can be simultaneously sharp in this state: $\sigma_{S_x} = 0$ and $\sigma_{S_z} = 0$."

**Step 4 — Consistency remark.**
"With $\sigma_{S_x} = \sigma_{S_z} = 0$, the product is $0$, which is $\geq 0$, the bound. Everything is consistent." *(The arithmetic $0 \geq 0$ is true — so this step looks self-consistent, but it inherits the false claim from Step 3.)*

**Your tasks:**
1. Identify the precise misconception in Step 3 and state it sharply.
2. Compute the actual $\sigma_{S_z}$ in $|\!\uparrow_x\rangle$ and show it is *not* zero.
3. Explain why a zero Robertson bound is "a silence from the theorem, not a guarantee" — what does a zero bound actually tell you, and what does it not?
4. State the correct values of $\sigma_{S_x}$ and $\sigma_{S_z}$ and confirm the (trivially satisfied) inequality.

**Why this error is common:** Students read a zero lower bound as "both observables can be sharp," but non-commuting observables still cannot be simultaneously sharp in general — a zero bound only means the inequality is not binding for that particular state, and one spread (here $\sigma_{S_z} = \hbar/2$) can remain fully nonzero.

---

## Part E — Transfer Problem

**What this demonstrates:** The same principle — a commutator setting an uncertainty bound — applied to a context outside the chapter: number and phase in a simplified two-level oscillator model, where the operators are not the standard $\hat x,\hat p$ or spin.

**The problem:** Consider two Hermitian observables on a qubit defined by $\hat N = \bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$ (a "number-like" operator with eigenvalues $1,0$) and $\hat\Phi = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr) = \sigma_x$ (a "phase-like" observable). (a) Compute the commutator $[\hat N,\hat\Phi]$. (b) Write the Robertson bound for $\hat N,\hat\Phi$. (c) For the state $|\psi\rangle = \tfrac{1}{\sqrt2}(|0\rangle + |1\rangle)$, evaluate the bound by computing $\langle[\hat N,\hat\Phi]\rangle$. (d) Compute the actual spreads $\sigma_N$ and $\sigma_\Phi$ in this state and check the inequality.

**Hint (use only if stuck after 10 minutes):** $[\hat N,\hat\Phi] = \hat N\hat\Phi - \hat\Phi\hat N$; multiply the two $2\times2$ matrices in both orders and subtract. You will find it is anti-Hermitian (its expectation is purely imaginary), exactly as the Robertson proof requires for the commutator of two Hermitian operators.

**Reflection prompt:**
1. The chapter proves $[\hat A,\hat B]$ is anti-Hermitian whenever $\hat A,\hat B$ are Hermitian. How did that show up in the *value* of $\langle[\hat N,\hat\Phi]\rangle$ you computed, and why is that essential for the bound $\tfrac12|\langle[\hat N,\hat\Phi]\rangle|$ to be real?
2. This number/phase pair is a finite-dimensional caricature of the genuine difficulty of defining a phase operator conjugate to particle number. What feature of $\hat x,\hat p$ (whose commutator is a c-number) is *lost* when the commutator is itself an operator?

---

## Part F — Interleaved Review

**Problem F1.** Apply Robertson to $\hat S_x$ and $\hat S_y$ for a general qubit with Bloch vector $(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$. (a) Compute $[\hat S_x,\hat S_y]$. (b) Show the bound is $\tfrac{\hbar^2}{4}|\cos\theta|$. (c) Find where on the Bloch sphere the bound is maximized and where it vanishes.
*Chapter this draws from: Chapter 3.*

**Problem F2.** Take the Hermitian observable $\hat B = \bigl(\begin{smallmatrix}2 & 1+i\\ 1-i & 0\end{smallmatrix}\bigr)$. (a) Verify Hermiticity via $A_{mn} = A_{nm}^*$. (b) Find its eigenvalues from the secular equation and check them against the trace and determinant. (c) Write the spectral decomposition $\hat B = \lambda_+\hat P_+ + \lambda_-\hat P_-$. Then state, in one sentence, why a Hermitian operator is guaranteed real eigenvalues.
*Chapter this draws from: Observables and the Spectral Theorem (Chapter 2).*

**Problem F3.** You are told two observables on a system have $[\hat A,\hat B] = 0$, and asked: "In any state, can both $\hat A$ and $\hat B$ be measured to have definite values simultaneously?"
*Note to instructor: this problem is intentionally ambiguous because the answer depends on a subtlety the student must surface. Commuting operators *share* a complete eigenbasis, so there *exist* simultaneous eigenstates with definite values for both — but not every state is such a simultaneous eigenstate. A strong student distinguishes "a shared eigenbasis exists" (always true for commuting Hermitian operators) from "this particular state has definite values for both" (true only if the state lies in that joint eigenbasis). The discrimination skill is separating the algebraic guarantee from the state-specific claim.*

**Closing reflection:** Across F1–F3, the connective tissue is the commutator deciding what is jointly knowable. F1 quantifies incompatibility ($[\hat S_x,\hat S_y]\neq0$); F2 rests on Hermiticity (real outcomes); F3 turns on compatibility ($[\hat A,\hat B]=0$). How does the commutator function as the single object that determines both *whether* two observables can be simultaneously sharp and *how tightly* they trade off when they cannot?

---

## Instructor Notes

**Common errors:**
- A sign error in the spin/Pauli commutator (e.g. writing $[\sigma_x,\sigma_z] = +2i\sigma_y$), which corrupts the bound's apparent source — the chapter flags this as the canonical sign trap.
- Dropping or mis-stating the factor of $\tfrac12$ in the Robertson bound $\sigma_A\sigma_B \geq \tfrac12|\langle[\hat A,\hat B]\rangle|$.
- Reading a zero Robertson bound as "both observables can be simultaneously sharp," when it only means the inequality is not binding for that state.

**Signs a student needs to return:**
- They claim two non-commuting observables can both have $\sigma = 0$ in some state.
- They cannot reproduce the four named steps of the Robertson proof (shift to zero mean, Cauchy-Schwarz, decompose into anticommutator + commutator, drop the non-negative term).

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify the commutator $[\hat S_x,\hat S_z] = -i\hbar\hat S_y$ by explicit Pauli matrix multiplication before touching the state — separating "what is the bound's source" from "what is its value here." If a student finishes Part F quickly, ask them to find the state on the Bloch sphere that *saturates* the $\hat S_x,\hat S_z$ bound and explain why it is the $\hat S_y$ eigenstate.

**Domain adaptation note:** For a course centered on quantum optics, recast the uncertainty pair as quadratures $\hat X,\hat P$ of a field mode (with squeezed states saturating the bound); for an NMR/spin-resonance course, keep the spin operators but tie the bound's state-dependence directly to the Bloch-sphere orientation set by the pulse sequence.
