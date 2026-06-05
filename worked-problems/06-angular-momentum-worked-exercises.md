# Worked Exercises: Angular Momentum
*Chapter 6 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The angular-momentum commutation relations $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ and the result $[\hat{L}^2, \hat{L}_i] = 0$.
- The ladder operators $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$, their commutators $[\hat{L}_z, \hat{L}_\pm] = \pm\hbar\hat{L}_\pm$, and the normalization $\hat{L}_\pm|\ell,m\rangle = \hbar\sqrt{(\ell\mp m)(\ell\pm m + 1)}\,|\ell, m\pm 1\rangle$.
- The spectrum $\hat{L}^2|\ell,m\rangle = \hbar^2\ell(\ell+1)|\ell,m\rangle$, $\hat{L}_z|\ell,m\rangle = \hbar m|\ell,m\rangle$, with $m = -\ell,\dots,+\ell$.

---

## Part A — Full Worked Example

**What this demonstrates:** How the entire $\ell = 1$ matrix representation, including $\hat{L}^2 = 2\hbar^2 I$, follows from the ladder normalization formula alone — no differential equation required.

**The problem:** In the ordered basis $\{|1,-1\rangle, |1,0\rangle, |1,1\rangle\}$, construct the matrices for $\hat{L}_z$, $\hat{L}_+$, $\hat{L}_-$, then $\hat{L}_x$, and verify $\hat{L}^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z = 2\hbar^2 I$.

**The solution:**

**Step 1 — Write $\hat{L}_z$ from its eigenvalues.**
$\hat{L}_z|1,m\rangle = \hbar m|1,m\rangle$, so the matrix is diagonal with entries $-\hbar, 0, +\hbar$:
$$\hat{L}_z = \hbar\begin{pmatrix}-1 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 1\end{pmatrix}.$$
*Why:* In the eigenbasis of $\hat{L}_z$, the operator is diagonal with its eigenvalues on the diagonal.
*Check:* The trace is $0$, as required for an angular-momentum component (the $m$ values are symmetric about zero).

**Step 2 — Apply the raising operator $\hat{L}_+$ to each basis state.**
Using $\hat{L}_+|\ell,m\rangle = \hbar\sqrt{(\ell - m)(\ell + m + 1)}\,|\ell, m+1\rangle$ with $\ell = 1$:
$$\hat{L}_+|1,-1\rangle = \hbar\sqrt{(1-(-1))(1+(-1)+1)}\,|1,0\rangle = \hbar\sqrt{(2)(1)}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle,$$
$$\hat{L}_+|1,0\rangle = \hbar\sqrt{(1)(2)}\,|1,1\rangle = \hbar\sqrt{2}\,|1,1\rangle, \qquad \hat{L}_+|1,1\rangle = \hbar\sqrt{(0)(3)}\,|1,2\rangle = 0.$$
So
$$\hat{L}_+ = \hbar\sqrt{2}\begin{pmatrix}0 & 0 & 0\\ 1 & 0 & 0\\ 0 & 1 & 0\end{pmatrix}.$$
*Why:* $\hat{L}_+$ steps $m$ up by one; the coefficient $\sqrt{(\ell-m)(\ell+m+1)}$ vanishes exactly at the top rung $m = \ell = 1$.
*Check:* The top-rung annihilation $\hat{L}_+|1,1\rangle = 0$ is built in — the ladder terminates, it does not blow up.

**Step 3 — Take the Hermitian conjugate to get $\hat{L}_-$, then build $\hat{L}_x$.**
$\hat{L}_- = \hat{L}_+^\dagger$ has the $\sqrt{2}$ entries on the super-diagonal:
$$\hat{L}_- = \hbar\sqrt{2}\begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0\end{pmatrix}, \qquad \hat{L}_x = \frac{\hat{L}_+ + \hat{L}_-}{2} = \frac{\hbar}{\sqrt{2}}\begin{pmatrix}0 & 1 & 0\\ 1 & 0 & 1\\ 0 & 1 & 0\end{pmatrix}.$$
*Why:* $\hat{L}_- = (\hat{L}_+)^\dagger$ because $\hat{L}_x, \hat{L}_y$ are Hermitian; $\hat{L}_x = (\hat{L}_+ + \hat{L}_-)/2$ inverts the definitions $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$.
*Check:* $\hat{L}_x$ is real symmetric (Hermitian) ✓, and its diagonal is zero, consistent with $\langle\hat{L}_x\rangle = 0$ in every $\hat{L}_z$ eigenstate.

**Step 4 — Compute $\hat{L}_-\hat{L}_+$ by matrix multiplication.**
$$\hat{L}_-\hat{L}_+ = 2\hbar^2\begin{pmatrix}0 & 1 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0\end{pmatrix}\begin{pmatrix}0 & 0 & 0\\ 1 & 0 & 0\\ 0 & 1 & 0\end{pmatrix} = 2\hbar^2\begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 0\end{pmatrix}.$$
*Why:* This is the operator combination that, added to $\hat{L}_z^2 + \hbar\hat{L}_z$, reconstructs $\hat{L}^2$ from $[\hat{L}_+, \hat{L}_-] = 2\hbar\hat{L}_z$.
*Check:* The bottom-right entry is $0$ because $\hat{L}_+|1,1\rangle = 0$, so $\hat{L}_-\hat{L}_+$ annihilates the top rung.

**Step 5 — Assemble $\hat{L}^2$ and confirm it is $2\hbar^2 I$.**
$$\hat{L}_z^2 = \hbar^2\,\text{diag}(1,0,1), \qquad \hbar\hat{L}_z = \hbar^2\,\text{diag}(-1,0,1).$$
$$\hat{L}^2 = 2\hbar^2\,\text{diag}(1,1,0) + \hbar^2\,\text{diag}(1,0,1) + \hbar^2\,\text{diag}(-1,0,1) = \hbar^2\,\text{diag}(2,2,2) = 2\hbar^2 I.$$
*Why:* $\hat{L}^2 = \ell(\ell+1)\hbar^2 I = 1\cdot 2\,\hbar^2 I$ for $\ell = 1$ — proportional to the identity, so every state in the multiplet has the same $\hat{L}^2$.
*Check:* All three diagonal entries equal $2\hbar^2$ and off-diagonals vanish ✓; matches $\hbar^2\ell(\ell+1)|_{\ell=1} = 2\hbar^2$.

**Final answer:** $\hat{L}^2 = 2\hbar^2 I$ for $\ell = 1$, constructed entirely from the ladder normalization formula and the commutator algebra.

**What made this work:** Nothing here used the associated Legendre equation. The normalization coefficient $\sqrt{(\ell - m)(\ell + m + 1)}$ generated every off-diagonal entry; the identity $\hat{L}^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$ (a consequence of $[\hat{L}_+, \hat{L}_-] = 2\hbar\hat{L}_z$) reassembled $\hat{L}^2$. The fact that $\hat{L}^2 \propto I$ is the matrix-level statement that $\ell$ is the same for the whole multiplet — exactly the algebraic spectrum.

**Self-explanation prompt:** Explain why $\hat{L}^2$ coming out proportional to the identity is the signature that all three states share one value of $\ell$.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same ladder-to-matrix construction, applied to the spin-$\tfrac{1}{2}$ ($\ell = \tfrac{1}{2}$) case, recovering the Pauli matrices.

**The problem:** In the basis $\{|\tfrac{1}{2}, -\tfrac{1}{2}\rangle, |\tfrac{1}{2}, +\tfrac{1}{2}\rangle\}$: (a) build $\hat{L}_z$, $\hat{L}_+$, $\hat{L}_-$ from the normalization formula; (b) construct $\hat{L}_x$ and $\hat{L}_y$; (c) verify $\hat{L}^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z = \tfrac{3}{4}\hbar^2 I$; (d) identify $\hat{L}_i = (\hbar/2)\sigma_i$ and confirm the standard Pauli forms.

Work each step with its own subgoal label, work, *Why:*, and *Check:*, following the five-step backbone of Part A: write $\hat{L}_z$ from eigenvalues → apply $\hat{L}_+$ → conjugate and build $\hat{L}_x, \hat{L}_y$ → compute $\hat{L}_-\hat{L}_+$ → assemble $\hat{L}^2$.

**Stuck?** For $\ell = \tfrac{1}{2}$ the only nonzero ladder action is $\hat{L}_+|\tfrac{1}{2},-\tfrac{1}{2}\rangle = \hbar\sqrt{(1)(1)}\,|\tfrac{1}{2},+\tfrac{1}{2}\rangle = \hbar|\tfrac{1}{2},+\tfrac{1}{2}\rangle$ — the coefficient is exactly $\hbar$, not $\hbar\sqrt{2}$. The top and bottom rungs are annihilated.

*Instructor note: no solution is provided for Part B. Students should produce the full structured solution themselves.*

---

## Part C — Completion Problem

**What this demonstrates:** The ladder-stepping argument that proves $\hat{L}_+$ raises $m$ by one, with the central commutator manipulation left for you.

**The problem:** Show that if $\hat{L}_z|\psi\rangle = \hbar m|\psi\rangle$, then $\hat{L}_z(\hat{L}_+|\psi\rangle) = \hbar(m+1)(\hat{L}_+|\psi\rangle)$, and state what this means physically.

**Step 1 — Quote the relevant commutator.** (provided)
$$[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+ \quad\Longrightarrow\quad \hat{L}_z\hat{L}_+ = \hat{L}_+\hat{L}_z + \hbar\hat{L}_+.$$

**Step 2 — State the goal: act with $\hat{L}_z$ on $\hat{L}_+|\psi\rangle$.** (provided)
We want $\hat{L}_z(\hat{L}_+|\psi\rangle)$. Substitute the rearranged commutator from Step 1.

**Step 3 — Carry out the substitution and use $\hat{L}_z|\psi\rangle = \hbar m|\psi\rangle$.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Factor out $\hat{L}_+|\psi\rangle$ to read off the eigenvalue.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret physically.** (provided)
$\hat{L}_+|\psi\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $\hbar(m+1)$: the raising operator climbs the ladder one rung. Because $[\hat{L}^2, \hat{L}_+] = 0$, the value of $\ell$ is unchanged — only $m$ steps up.

**Final answer:** $\hat{L}_z(\hat{L}_+|\psi\rangle) = \hbar(m+1)(\hat{L}_+|\psi\rangle)$; $\hat{L}_+$ raises $m$ by one within a fixed-$\ell$ multiplet.

**Self-explanation prompt:** Why does the commutator $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$ — and not the explicit form of $\hat{L}_+$ — do all the work here?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked for the magnitude of angular momentum and the transverse spread in the state $|\ell = 3, m = 3\rangle$. Their work:

**Step 1.** $L_z = m\hbar = 3\hbar$. Correct.

**Step 2.** "The state has maximum $m$, so the angular momentum points along $z$."

**Step 3.** ⚠ "Therefore the total magnitude is $\sqrt{\langle L^2\rangle} = \sqrt{\hbar^2\ell^2} = \ell\hbar = 3\hbar$, and since the vector points along $z$, the transverse components $L_x$ and $L_y$ are both exactly zero."

**Step 4.** Report: $|L| = 3\hbar$, $\sigma_{L_x} = \sigma_{L_y} = 0$.

**Your tasks:**
1. Identify the error in Step 3 precisely.
2. Compute the correct $\sqrt{\langle L^2\rangle}$ using $\hat{L}^2$ eigenvalue $\hbar^2\ell(\ell+1)$.
3. Compute $\langle L_x^2 + L_y^2\rangle = \langle L^2\rangle - L_z^2$ in this state and show it is nonzero, then find $\sigma_{L_x} = \sigma_{L_y}$.
4. Explain, using the Robertson inequality $\sigma_{L_x}\sigma_{L_y} \geq \tfrac{\hbar}{2}|\langle\hat{L}_z\rangle|$, why the transverse components cannot vanish.

**Why this error is common:** Students conflate $\langle L^2\rangle = \hbar^2\ell(\ell+1)$ with $\hbar^2\ell^2$, which collapses the angular-momentum cone to a vector lying flat along $z$ and falsely sets the transverse spread to zero.

---

## Part E — Transfer Problem

**What this demonstrates:** The same algebra-only spectrum derivation, transferred from orbital $\hat{L}$ to a generic angular momentum $\hat{J}$ and used to explain why half-integer values are allowed for spin but not for orbital motion.

**The problem:** The operators $\hat{J}_x, \hat{J}_y, \hat{J}_z$ satisfy $[\hat{J}_i, \hat{J}_j] = i\hbar\epsilon_{ijk}\hat{J}_k$ — the identical algebra to $\hat{L}$. (a) Run the termination argument: $\hat{J}_+|j, m_\text{max}\rangle = 0$, apply $\hat{J}^2 = \hat{J}_-\hat{J}_+ + \hat{J}_z^2 + \hbar\hat{J}_z$, and show $\langle\hat{J}^2\rangle = \hbar^2 j(j+1)$ with $j = m_\text{max}$. (b) Argue that stepping from $m_\text{min} = -j$ to $m_\text{max} = +j$ requires $2j$ to be a non-negative integer, so $j = 0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \dots$. (c) Explain why orbital angular momentum is restricted to *integer* $\ell$ even though the algebra permits half-integers — what physical condition does orbital $\hat{L}$ obey that abstract $\hat{J}$ need not?

**Hint (use only if stuck after 10 minutes):** The integer restriction for orbital angular momentum comes from single-valuedness of $e^{im\phi}$ under $\phi \to \phi + 2\pi$, which forces $e^{2\pi i m} = 1$. Spin has no position-space wave function and no $\phi$ to be single-valued in, so nothing forbids $j = \tfrac{1}{2}$.

**Reflection prompt:**
1. The spectrum $\hbar^2 j(j+1)$ came entirely from three commutators and one non-negativity inequality. What role, if any, did the sphere or spherical coordinates play?
2. Why is it accurate to say the algebra is "more general" than the orbital case, with the sphere *adding* a constraint rather than the algebra removing one?

---

## Part F — Interleaved Review

**F1 — This chapter.** For $|\ell, \ell\rangle$ (the top rung): (a) compute $\langle\hat{L}_x^2\rangle = \langle\hat{L}_y^2\rangle$ using $\langle\hat{L}^2\rangle - \langle\hat{L}_z^2\rangle$ and the symmetry $\langle\hat{L}_x^2\rangle = \langle\hat{L}_y^2\rangle$; (b) show $\sigma_{L_x}\sigma_{L_y} = \hbar^2\ell/2$; (c) confirm the Robertson bound $\tfrac{\hbar}{2}|\langle\hat{L}_z\rangle| = \hbar^2\ell/2$ is exactly saturated, and state what "saturated" means for the cone.
*Chapter this draws from: 6*

**F2 — Previous chapter.** From **Quantum Mechanics in Three Dimensions**, the coordinate-space ladder operators are $\hat{L}_- = -\hbar e^{-i\phi}(\partial_\theta - i\cot\theta\,\partial_\phi)$. Verify $\hat{L}_- Y_1^1 = \hbar\sqrt{2}\,Y_1^0$, where $Y_1^1 = -\sqrt{3/(8\pi)}\sin\theta\,e^{i\phi}$ and $Y_1^0 = \sqrt{3/(4\pi)}\cos\theta$. Confirm the coefficient $\hbar\sqrt{2}$ matches the abstract normalization $\hbar\sqrt{(\ell+m)(\ell-m+1)}$ for $\ell = 1, m = 1$.
*Chapter this draws from: Quantum Mechanics in Three Dimensions*

**F3 — Discrimination.** You are handed two claims about the state $|2,2\rangle$: (i) "$\hat{L}_x$ and $\hat{L}_z$ are simultaneously sharp because both are angular-momentum components"; (ii) "$\hat{L}^2$ and $\hat{L}_z$ are simultaneously sharp." Decide which claim is true and justify using the commutators $[\hat{L}_x, \hat{L}_z] \neq 0$ versus $[\hat{L}^2, \hat{L}_z] = 0$.
*Note to instructor: this tests whether students can discriminate "two components of $\hat{L}$" (non-commuting, never simultaneously sharp) from "$\hat{L}^2$ and one component" (commuting, simultaneously diagonalizable) — a confusion that recurs whenever students assume any pair of angular-momentum quantities can be measured together.*

**Closing reflection:** This chapter derived the entire spectrum from commutators rather than the Legendre equation. Write two sentences on what the algebraic derivation buys you that the analytic derivation in Chapter 5 cannot.

---

## Instructor Notes

**Common errors:**
- Writing $\langle\hat{L}^2\rangle = \hbar^2\ell^2$ instead of $\hbar^2\ell(\ell+1)$ (Part D's misconception), which wrongly zeroes the transverse spread.
- Off-by-one errors in the ladder coefficient $\sqrt{(\ell\mp m)(\ell\pm m+1)}$, especially failing to get $0$ at the terminating rung.
- Claiming $\hat{L}_x$ and $\hat{L}_z$ can be simultaneously sharp because both are "angular momentum."

**Signs a student needs to return:**
- They allow $m$ values outside the range $-\ell \le m \le +\ell$.
- They cannot explain why the same algebra permits $\ell = \tfrac{1}{2}$ for spin but not for orbital motion.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify a single ladder action ($\hat{L}_+|1,0\rangle = \hbar\sqrt{2}|1,1\rangle$) numerically before assembling full matrices. If a student finishes Part F quickly, send them to the $\ell = 2$ ($5\times 5$) construction and have them confirm $\hat{L}^2 = 6\hbar^2 I$ from the matrices.

**Domain adaptation note:** For students heading toward quantum information, frame the $\ell = \tfrac{1}{2}$ case and the Pauli connection as the bridge to qubits (Chapter 7); for those heading toward spectroscopy, emphasize the matrix elements as the seeds of selection rules.
