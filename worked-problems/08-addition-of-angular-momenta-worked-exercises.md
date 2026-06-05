# Worked Exercises: Addition of Angular Momenta
*Chapter 8 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The triangle rule $J = |j_1 - j_2|, \dots, j_1 + j_2$ and the state-count identity $\sum_J(2J+1) = (2j_1+1)(2j_2+1)$.
- The uncoupled basis $|m_1, m_2\rangle$ versus the coupled basis $|J, M\rangle$, related by Clebsch–Gordan coefficients, with the selection rule $M = m_1 + m_2$.
- The ladder-operator method ($\hat{J}_- = \hat{J}_{1-} + \hat{J}_{2-}$) and orthogonalization for building coupled states; singlet/triplet and the identity $\hat{L}\cdot\hat{S} = \tfrac{1}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$.

---

## Part A — Full Worked Example

**What this demonstrates:** How the four-step ladder algorithm builds the $\tfrac{1}{2}\otimes\tfrac{1}{2}$ coupled states from scratch, producing the triplet and singlet and the single minus sign behind the 21-cm line.

**The problem:** Two spin-½ particles. Build all four coupled states $|J, M\rangle$ from the uncoupled basis $\{|\!\uparrow\uparrow\rangle, |\!\uparrow\downarrow\rangle, |\!\downarrow\uparrow\rangle, |\!\downarrow\downarrow\rangle\}$, identify the triplet and singlet, and confirm the exchange symmetry of each.

**The solution:**

**Step 1 — Verify the multiplet structure with the state count.**
Triangle rule: $J = |{\tfrac{1}{2}} - {\tfrac{1}{2}}|, \dots, \tfrac{1}{2} + \tfrac{1}{2} = 0, 1$. Dimensions: $(2\cdot 0 + 1) + (2\cdot 1 + 1) = 1 + 3 = 4 = (2)(2)$.
*Why:* Confirming $\sum_J(2J+1) = (2j_1+1)(2j_2+1)$ before any algebra guarantees we are looking for exactly one $J=0$ state and three $J=1$ states.
*Check:* $4 = 4$ ✓ — the coupled basis has the same dimension as the uncoupled basis.

**Step 2 — Identify the stretched state $|1,1\rangle$.**
The only uncoupled state with $M = m_1 + m_2 = +1$ is $|\!\uparrow\uparrow\rangle$:
$$|1,1\rangle = |\!\uparrow\uparrow\rangle.$$
*Why:* The top of the highest multiplet $|J_\text{max}, M_\text{max}\rangle = |j_1+j_2, j_1+j_2\rangle$ must be the unique maximal-$M$ uncoupled state — there is no other state with $M = +1$.
*Check:* It is manifestly symmetric under particle exchange ✓, as the $J=1$ triplet should be.

**Step 3 — Lower with $\hat{J}_-$ to generate the rest of the triplet.**
Apply $\hat{J}_- = \hat{J}_{1-} + \hat{J}_{2-}$ to both sides. Left: $\hat{J}_-|1,1\rangle = \hbar\sqrt{(1+1)(1-1+1)}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle$. Right: $(\hat{J}_{1-}+\hat{J}_{2-})|\!\uparrow\uparrow\rangle = \hbar|\!\downarrow\uparrow\rangle + \hbar|\!\uparrow\downarrow\rangle$. Equate:
$$|1,0\rangle = \frac{1}{\sqrt{2}}\big(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle\big).$$
Lowering once more gives $|1,-1\rangle = |\!\downarrow\downarrow\rangle$.
*Why:* $\hat{J}_-$ steps $M$ down by one while keeping $J$ fixed, so it stays inside the $J=1$ multiplet and assembles the symmetric combination automatically.
*Check:* $|1,0\rangle$ is symmetric under exchange ✓, matching the other triplet members.

**Step 4 — Build the singlet by orthogonality in the $M=0$ sector.**
The remaining state has $M=0$, so $|0,0\rangle = a|\!\uparrow\downarrow\rangle + b|\!\downarrow\uparrow\rangle$. Orthogonality to $|1,0\rangle$ forces $a + b = 0$, hence $b = -a$; normalization gives $a = 1/\sqrt{2}$. Condon–Shortley fixes the coefficient of $|\!\uparrow\downarrow\rangle$ (larger $m_1$) positive:
$$|0,0\rangle = \frac{1}{\sqrt{2}}\big(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle\big).$$
*Why:* The $M=0$ sector is two-dimensional; one combination ($+$) belongs to the triplet, so the orthogonal combination ($-$) must be the singlet.
*Check:* $\langle 1,0|0,0\rangle = \tfrac{1}{2}(1 - 1) = 0$ ✓ — the singlet is orthogonal to the triplet.

**Step 5 — Confirm the singlet has $J=0$ and read off exchange symmetries.**
Since $|0,0\rangle$ is orthogonal to all three $|1,M\rangle$ and $\hat{J}^2$ commutes with $\hat{J}_z$, $\hat{J}^2|0,0\rangle$ lies in the $M=0$ span of $\{|1,0\rangle, |0,0\rangle\}$; the cross term $\langle 1,0|\hat{J}^2|0,0\rangle = 2\hbar^2\langle 1,0|0,0\rangle = 0$, so $\hat{J}^2|0,0\rangle = c|0,0\rangle$ with $c = 0$. The three triplet states are symmetric; the singlet is antisymmetric.
*Why:* "Triplets add, singlets subtract" — the symmetric combinations carry $J=1$, the antisymmetric one carries $J=0$.
*Check:* $J(J+1)\hbar^2 = 0$ for the singlet ✓; the antisymmetric exchange sign matches.

**Final answer:** Triplet $|1,1\rangle = |\!\uparrow\uparrow\rangle$, $|1,0\rangle = \tfrac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)$, $|1,-1\rangle = |\!\downarrow\downarrow\rangle$ (all symmetric, $J=1$); singlet $|0,0\rangle = \tfrac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)$ (antisymmetric, $J=0$).

**What made this work:** The algorithm never guesses. Step 2 pins the stretched state by uniqueness of maximal $M$; Step 3 uses $\hat{J}_-$ to fall through one multiplet; Step 4 uses orthogonality (plus Condon–Shortley) to pull out the next multiplet in the shared $M$-sector. The single minus sign separating singlet from triplet is forced by orthogonality, and it is the same sign that — through the hyperfine Hamiltonian — produces the 21-cm line.

**Self-explanation prompt:** Explain why the $M=0$ sector is exactly where the singlet must be found, and why orthogonality (not the ladder operator) is the tool that extracts it.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same four-step ladder algorithm, applied to $1 \otimes \tfrac{1}{2}$, a case with a three-dimensional spin-1 factor.

**The problem:** Couple $j_1 = 1$ and $j_2 = \tfrac{1}{2}$. (a) Use the triangle rule and state count to find the allowed $J$. (b) Identify the stretched state $|\tfrac{3}{2}, \tfrac{3}{2}\rangle$. (c) Apply $\hat{J}_-$ to generate $|\tfrac{3}{2}, \tfrac{1}{2}\rangle$ and $|\tfrac{3}{2}, -\tfrac{1}{2}\rangle$. (d) In the $M = \tfrac{1}{2}$ sector, orthogonalize to find $|\tfrac{1}{2}, \tfrac{1}{2}\rangle$, and verify $\hat{J}^2$ gives eigenvalue $\tfrac{3}{4}\hbar^2$ on it.

Work each step with its own subgoal label, work, *Why:*, and *Check:*, following the five-step backbone of Part A: state count → stretched state → lower through the top multiplet → orthogonalize for the lower multiplet → confirm the $J$ eigenvalue.

**Stuck?** The stretched state is $|\tfrac{3}{2}, \tfrac{3}{2}\rangle = |m_1 = 1\rangle|m_2 = \tfrac{1}{2}\rangle$. When you apply $\hat{J}_-$, use $\hat{J}_{1-}|1,1\rangle = \hbar\sqrt{2}|1,0\rangle$ for the spin-1 factor and $\hat{J}_{2-}|\!\uparrow\rangle = \hbar|\!\downarrow\rangle$ for the spin-½ factor; the coefficients differ between the two particles.

*Instructor note: no solution is provided for Part B. Students should produce the full structured solution themselves.*

---

## Part C — Completion Problem

**What this demonstrates:** Using the coupled basis to diagonalize spin-orbit coupling, with the eigenvalue arithmetic left for you.

**The problem:** For a $2p$ electron of hydrogen ($\ell = 1$, $s = \tfrac{1}{2}$) with $\hat{H}_\text{so} = \lambda\hat{L}\cdot\hat{S}$, find the energy shift for each allowed $J$ and the splitting between them.

**Step 1 — Find the allowed $J$ via the triangle rule.** (provided)
$J = |\ell - s|, \dots, \ell + s = \tfrac{1}{2}, \tfrac{3}{2}$. State count: $(2) + (4) = 6 = (3)(2)$ ✓.

**Step 2 — Write the diagonal form of $\hat{L}\cdot\hat{S}$.** (provided)
$$\hat{L}\cdot\hat{S} = \tfrac{1}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2) \;\Longrightarrow\; \hat{H}_\text{so}|J,M\rangle = \frac{\lambda\hbar^2}{2}\big[J(J+1) - \ell(\ell+1) - s(s+1)\big]|J,M\rangle.$$

**Step 3 — Evaluate the shift for $J = \tfrac{3}{2}$.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Evaluate the shift for $J = \tfrac{1}{2}$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret the splitting.** (provided)
The difference $\Delta E(\tfrac{3}{2}) - \Delta E(\tfrac{1}{2}) = \tfrac{3\lambda\hbar^2}{2}$. The $J=\tfrac{3}{2}$ level sits above $J=\tfrac{1}{2}$ (for $\lambda > 0$). This is the hydrogen $2p$ fine-structure doublet; the splitting structure comes entirely from the CG algebra, while $\lambda$ itself requires a relativistic calculation.

**Final answer:** $\Delta E(\tfrac{3}{2}) = +\tfrac{\lambda\hbar^2}{2}$, $\Delta E(\tfrac{1}{2}) = -\lambda\hbar^2$, splitting $= \tfrac{3\lambda\hbar^2}{2}$, with $J=\tfrac{3}{2}$ higher.

**Self-explanation prompt:** Why is the coupled basis the "right" basis for this problem — what labor does it eliminate compared to the uncoupled basis?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student couples two spin-1 particles ($j_1 = j_2 = 1$) and reports the multiplet structure. Their work:

**Step 1.** Triangle rule: $J$ ranges from $|1 - 1| = 0$ to $1 + 1 = 2$.

**Step 2.** "So $J = 0, 1, 2$."

**Step 3.** ⚠ "The dimensions are $2J+1 = 1, 3, 5$. But the total space is $j_1 \cdot j_2 = 1 \times 1 = 1$-dimensional... that can't be right, so I'll keep only the largest multiplet $J = 2$ (dimension 5) and discard $J = 0$ and $J = 1$ as spurious."

**Step 4.** Report: "$1 \otimes 1 = 2$ only; the coupled space is five-dimensional."

**Your tasks:**
1. Identify the error in Step 3 precisely.
2. Compute the correct total dimension of the product space $(2j_1+1)(2j_2+1)$.
3. Verify the state-count identity $\sum_J(2J+1) = (2j_1+1)(2j_2+1)$ for $1\otimes 1$, showing all three multiplets are required.
4. Write the correct decomposition $1 \otimes 1 = 0 \oplus 1 \oplus 2$ and state its total dimension.

**Why this error is common:** Students compute the product-space dimension as $j_1 \cdot j_2$ (the magnitudes) instead of $(2j_1+1)(2j_2+1)$ (the dimensions), then discard multiplets to force a wrong total — the state-count check exists precisely to catch this.

---

## Part E — Transfer Problem

**What this demonstrates:** The same coupled-basis identity, transferred from spin-orbit coupling to the hydrogen hyperfine interaction that produces the 21-cm line.

**The problem:** The hydrogen ground-state hyperfine Hamiltonian is $\hat{H}_\text{hf} = A\,\hat{S}_e\cdot\hat{S}_p$, coupling the electron and proton spins (both $\tfrac{1}{2}$). With $\hat{F} = \hat{S}_e + \hat{S}_p$: (a) use $\hat{S}_e\cdot\hat{S}_p = \tfrac{1}{2}(\hat{F}^2 - \hat{S}_e^2 - \hat{S}_p^2)$ to find $E_{F=1}$ (triplet) and $E_{F=0}$ (singlet) in terms of $A$ and $\hbar$. (b) Show the splitting is $\Delta E = A\hbar^2$. (c) Given the observed frequency $f = 1420.405$ MHz, identify which state is higher in energy and which spin configuration (parallel or antiparallel) it corresponds to.

**Hint (use only if stuck after 10 minutes):** This is structurally identical to Part C's spin-orbit problem with $\hat{L},\hat{S} \to \hat{S}_e, \hat{S}_p$ and $\hat{J} \to \hat{F}$. The triplet has $F(F+1) = 2$ and the singlet $F(F+1) = 0$; both spins have $s(s+1) = \tfrac{3}{4}$. Triplet energy $A\hbar^2/4$, singlet $-3A\hbar^2/4$.

**Reflection prompt:**
1. The same identity $\hat{X}_1\cdot\hat{X}_2 = \tfrac{1}{2}(\hat{J}^2 - \hat{X}_1^2 - \hat{X}_2^2)$ diagonalized both spin-orbit and hyperfine couplings. What general feature of these Hamiltonians makes the coupled basis the natural one?
2. The chapter says the 21-cm line "comes down to a single minus sign." In terms of the triplet/singlet structure you computed, what is that minus sign and what does it change?

---

## Part F — Interleaved Review

**F1 — This chapter.** Convert the uncoupled state $|\!\downarrow\uparrow\rangle$ to the coupled basis using the $M=0$ CG table $\begin{pmatrix}1/\sqrt{2} & 1/\sqrt{2}\\ 1/\sqrt{2} & -1/\sqrt{2}\end{pmatrix}$ (rows $|\!\uparrow\downarrow\rangle, |\!\downarrow\uparrow\rangle$; columns $|1,0\rangle, |0,0\rangle$). Then, if $\hat{J}^2$ is measured, give the probabilities of $J=1$ and $J=0$.
*Chapter this draws from: 8*

**F2 — Previous chapter.** From **Spin and the Bloch Sphere**, the single-particle $x$-basis states are $|\!\rightarrow\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ and $|\!\leftarrow\rangle = (|\!\uparrow\rangle - |\!\downarrow\rangle)/\sqrt{2}$. Substitute these into the singlet $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ and show it equals $(|\!\rightarrow\leftarrow\rangle - |\!\leftarrow\rightarrow\rangle)/\sqrt{2}$ — the same form in the $x$-basis. What does this say about measuring $\hat{S}_{1x}$ and $\hat{S}_{2x}$ on the singlet?
*Chapter this draws from: Spin and the Bloch Sphere*

**F3 — Discrimination.** You are shown two two-spin states: (i) $|1,0\rangle = (|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2}$ and (ii) $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$. They differ only by a sign. Decide which has $J=1$ and which has $J=0$, which is symmetric and which is antisymmetric under exchange, and which is rotationally invariant — without re-deriving, by recalling the singlet/triplet structure.
*Note to instructor: this tests whether students can discriminate the singlet from the $M=0$ triplet member — two states identical except for one sign — and connect that sign to $J$, exchange symmetry, and rotational invariance simultaneously. Getting the singlet/triplet exchange symmetry backwards is a recurring error.*

**Closing reflection:** The four-step ladder algorithm worked identically for $\tfrac{1}{2}\otimes\tfrac{1}{2}$, $1\otimes\tfrac{1}{2}$, and (in principle) any $(j_1, j_2)$. Write two sentences on why the algorithm is universal — what feature of the angular-momentum algebra guarantees it always terminates correctly.

---

## Instructor Notes

**Common errors:**
- Getting the allowed $J$ range wrong — using $j_1 + j_2$ only, or miscomputing $|j_1 - j_2|$, instead of the full $|j_1 - j_2|, \dots, j_1 + j_2$ (and the related Part D dimension error).
- Miscounting a multiplet dimension by computing the product space as $j_1 \cdot j_2$ rather than $(2j_1+1)(2j_2+1)$.
- Getting the singlet/triplet exchange symmetry backwards (calling the antisymmetric singlet "symmetric," or vice versa).

**Signs a student needs to return:**
- They cannot run the state-count check $\sum_J(2J+1) = (2j_1+1)(2j_2+1)$ to validate a coupling before doing algebra.
- They treat the $M=0$ triplet member and the singlet as interchangeable because "they look almost the same."

**Scaffolding adjustments:** If a student struggles with Part A, have them first do only Steps 1–2 (state count and stretched state) for several $(j_1, j_2)$ pairs before introducing the lowering operator. If a student finishes Part F quickly, have them prove the singlet cannot be written as a product state $|\psi_1\rangle\otimes|\psi_2\rangle$ (the entanglement argument).

**Domain adaptation note:** For an astrophysics cohort, anchor the hyperfine calculation to the 21-cm line and its use in mapping galactic hydrogen; for an atomic-spectroscopy cohort, anchor the spin-orbit calculation to the fine-structure doublets and the $^{2S+1}L_J$ term symbols of Chapter 11.
