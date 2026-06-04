# Chapter 8 — Addition of Angular Momenta

## TL;DR

When two angular momenta are present — two spins, or a spin and an orbital — the product Hilbert space has two natural bases. The uncoupled basis labels each particle's projection separately; the coupled basis labels the total angular momentum $J$ and its projection $M$. The triangle rule $J = |j_1 - j_2|, \ldots, j_1 + j_2$ tells you which values of $J$ appear. The Clebsch–Gordan coefficients are the change-of-basis matrix. For two spin-½ particles, the four states decompose into one singlet ($J=0$) and three triplet ($J=1$) states — and the reason you care is that the spin-orbit Hamiltonian $\hat{H}_\text{so} = \lambda\hat{L}\cdot\hat{S}$ is diagonal in the coupled basis and not in the uncoupled basis.

---

## Learning Objectives

By the end of this chapter you can:

1. **State** the triangle rule for adding angular momenta $j_1$ and $j_2$, and verify it by counting states. *(Bloom: Remember)*
2. **Construct** the singlet and all three triplet states for two spin-½ particles using the ladder operator method. *(Bloom: Apply)*
3. **Read** a Clebsch–Gordan table and convert any uncoupled state $|m_1, m_2\rangle$ into a superposition of coupled states $|J, M\rangle$, and vice versa. *(Bloom: Apply)*
4. **Explain** why the coupled basis diagonalizes $\hat{L}\cdot\hat{S}$ and why this matters for computing fine-structure energy splittings. *(Bloom: Understand)*
5. **Build** a CG calculator that takes $(j_1, j_2, J, M)$ as input and returns the coupled-state expansion, verified by normalization and orthogonality. *(Bloom: Create)*

---

## One System, Two Bases

Imagine the simplest possible two-spin system: an electron and a proton, each with spin-½, sitting at fixed positions so that only their spins matter. You have four states to describe — the electron can be up or down, and the proton can be up or down, independently. But "independently" is exactly the problem. Most of the interesting physics — the hydrogen hyperfine splitting, spin-orbit coupling, the singlet and triplet states of helium — does not respect the individual spins. It responds to the total angular momentum.

Nature, in other words, often prefers a different basis than the one built from individual particles.

This chapter is about that other basis: the one where the total angular momentum $\hat{J}^2 = (\hat{J}_1 + \hat{J}_2)^2$ is diagonal. Getting there requires three ingredients: the triangle rule (which values of total $J$ are allowed), the Clebsch–Gordan coefficients (the change-of-basis numbers), and the ladder operator method (the systematic procedure for computing them). None of these is complicated individually. Their power is that they work for any two angular momenta — spin-½ pairs, spin-orbit coupling, two $p$-electrons — with the same algorithm every time.

We will build everything explicitly for the simplest case, $\frac{1}{2} \otimes \frac{1}{2}$, and end with a preview of why it all matters for energy levels.

---

## Core Development

### Two Bases for the Same Space

A system with angular momenta $\hat{J}_1$ (quantum number $j_1$) and $\hat{J}_2$ (quantum number $j_2$) lives in a Hilbert space of dimension $(2j_1+1)(2j_2+1)$.

**The uncoupled (product) basis** is $|j_1, j_2; m_1, m_2\rangle = |j_1, m_1\rangle \otimes |j_2, m_2\rangle$. These states are simultaneous eigenstates of $\hat{J}_1^2$, $\hat{J}_2^2$, $\hat{J}_{1z}$, and $\hat{J}_{2z}$:
$$\hat{J}_{1z}|j_1, j_2; m_1, m_2\rangle = \hbar m_1|j_1, j_2; m_1, m_2\rangle, \qquad \hat{J}_{2z}|j_1, j_2; m_1, m_2\rangle = \hbar m_2|j_1, j_2; m_1, m_2\rangle.$$
The total $z$-projection is $M = m_1 + m_2$. This is always exact — the $z$-components simply add. There are $(2j_1+1)(2j_2+1)$ such states.

**The coupled basis** is $|j_1, j_2; J, M\rangle$, often written $|J, M\rangle$ when $j_1, j_2$ are fixed. These states are simultaneous eigenstates of $\hat{J}_1^2$, $\hat{J}_2^2$, $\hat{J}^2 = (\hat{J}_1 + \hat{J}_2)^2$, and $\hat{J}_z = \hat{J}_{1z} + \hat{J}_{2z}$:
$$\hat{J}^2|J, M\rangle = \hbar^2 J(J+1)|J, M\rangle, \qquad \hat{J}_z|J, M\rangle = \hbar M|J, M\rangle.$$
Note: $\hat{J}_1^2$ and $\hat{J}_2^2$ still commute with everything, so $j_1$ and $j_2$ remain good quantum numbers in the coupled basis. What changes is that $\hat{J}_{1z}$ and $\hat{J}_{2z}$ individually no longer have definite values.

Both bases span the same Hilbert space. The **Clebsch–Gordan (CG) coefficients** are the entries of the unitary matrix that transforms one basis into the other:
$$|J, M\rangle = \sum_{m_1, m_2} \langle j_1, j_2; m_1, m_2 | j_1, j_2; J, M\rangle\,|j_1, j_2; m_1, m_2\rangle.$$

### The Triangle Rule

Which values of $J$ appear? The answer is the **quantum triangle inequality**:
$$J = |j_1 - j_2|,\ |j_1 - j_2| + 1,\ \ldots,\ j_1 + j_2,$$
in integer steps. Each value of $J$ appears exactly once. The representation-theoretic shorthand is
$$j_1 \otimes j_2 = |j_1 - j_2| \oplus (|j_1 - j_2|+1) \oplus \cdots \oplus (j_1 + j_2).$$

The state count must balance:
$$\sum_{J=|j_1-j_2|}^{j_1+j_2}(2J+1) = (2j_1+1)(2j_2+1).$$
Always verify this before doing any algebra. Errors in the triangle rule are caught immediately.

Three cases are worth memorizing:

| Combination | Allowed $J$ | Dimensions | Check |
|-------------|-------------|------------|-------|
| $\frac{1}{2} \otimes \frac{1}{2}$ | $0,\ 1$ | $1 + 3 = 4$ | $2 \times 2 = 4$ ✓ |
| $1 \otimes \frac{1}{2}$ | $\frac{1}{2},\ \frac{3}{2}$ | $2 + 4 = 6$ | $3 \times 2 = 6$ ✓ |
| $1 \otimes 1$ | $0,\ 1,\ 2$ | $1 + 3 + 5 = 9$ | $3 \times 3 = 9$ ✓ |

### Building the Coupled States: the Ladder Operator Method

The systematic procedure uses the lowering operator $\hat{J}_- = \hat{J}_{1-} + \hat{J}_{2-}$, whose action on the coupled basis is
$$\hat{J}_-|J, M\rangle = \hbar\sqrt{(J+M)(J-M+1)}\,|J, M-1\rangle,$$
and on product states:
$$\hat{J}_{1-}|j_1, m_1\rangle = \hbar\sqrt{(j_1+m_1)(j_1-m_1+1)}\,|j_1, m_1-1\rangle.$$

**The algorithm:**
1. Identify the "stretched state" $|J_\text{max}, M_\text{max}\rangle = |j_1+j_2, j_1+j_2\rangle$. It must equal the unique uncoupled state with $m_1 = j_1$ and $m_2 = j_2$.
2. Apply $\hat{J}_-$ to both sides to generate all $M$ values within the $J = j_1 + j_2$ multiplet.
3. Within each $M$ sector, orthogonalize to find the state belonging to $J = j_1 + j_2 - 1$.
4. Apply $\hat{J}_-$ again to generate all $M$ values within that multiplet.
5. Repeat until all states are accounted for.

The CG coefficients are real in the **Condon–Shortley phase convention**: the coefficient with the largest $m_1$ (i.e., $m_1 = j_1$) is taken positive. Fix this convention at the start and all signs are determined.

### The Two Spin-½ Case Explicitly

For $j_1 = j_2 = \frac{1}{2}$, the uncoupled basis is four states:
$$|\!\uparrow\uparrow\rangle,\quad |\!\uparrow\downarrow\rangle,\quad |\!\downarrow\uparrow\rangle,\quad |\!\downarrow\downarrow\rangle,$$
shorthand for $|m_1, m_2\rangle = |{+\tfrac{1}{2}}, {+\tfrac{1}{2}}\rangle$, etc. The triangle rule gives $J = 0$ and $J = 1$.

**Step 1.** The stretched state $|J=1, M=1\rangle$ has $M = m_1 + m_2 = +1$. Only one uncoupled state achieves this:
$$|1, 1\rangle = |\!\uparrow\uparrow\rangle.$$

**Step 2.** Apply $\hat{J}_-$ to both sides. Left side: $\hat{J}_-|1,1\rangle = \hbar\sqrt{(1+1)(1-1+1)}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle$. Right side: $\hat{J}_{1-}|\!\uparrow\uparrow\rangle + \hat{J}_{2-}|\!\uparrow\uparrow\rangle = \hbar|\!\downarrow\uparrow\rangle + \hbar|\!\uparrow\downarrow\rangle$. Equating:
$$\hbar\sqrt{2}\,|1,0\rangle = \hbar|\!\downarrow\uparrow\rangle + \hbar|\!\uparrow\downarrow\rangle$$
$$\boxed{|1,0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle\right).}$$
This state is **symmetric** under exchange of the two particles.

**Step 3.** Apply $\hat{J}_-$ to $|1,0\rangle$. Left: $\hbar\sqrt{2}\,|1,-1\rangle$. Right: $\hat{J}_{1-}(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2} + \hat{J}_{2-}(\cdots)/\sqrt{2}$. The non-zero terms are $\hat{J}_{1-}|\!\uparrow\downarrow\rangle = \hbar|\!\downarrow\downarrow\rangle$ and $\hat{J}_{2-}|\!\downarrow\uparrow\rangle = \hbar|\!\downarrow\downarrow\rangle$. Collecting:
$$\boxed{|1,-1\rangle = |\!\downarrow\downarrow\rangle.}$$

**Step 4.** The singlet $|0,0\rangle$ must have $M = 0$, so it is a linear combination of $|\!\uparrow\downarrow\rangle$ and $|\!\downarrow\uparrow\rangle$. Orthogonality to $|1,0\rangle$ and normalization determine it uniquely (up to the Condon–Shortley sign):
$$\boxed{|0,0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle\right).}$$
This state is **antisymmetric** under particle exchange.

**Verify.** Check $\langle 1,0|0,0\rangle = \tfrac{1}{2}(1 - 1) = 0$. ✓ Check $\hat{J}^2|0,0\rangle = 0$: using $\hat{J}^2 = \hat{J}_1^2 + \hat{J}_2^2 + 2\hat{J}_{1z}\hat{J}_{2z} + \hat{J}_{1+}\hat{J}_{2-} + \hat{J}_{1-}\hat{J}_{2+}$, each term acting on $(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ returns zero by cancellation. ✓

The four coupled states in full:

| State | Expression | $J$ | $M$ | Symmetry |
|-------|-----------|-----|-----|----------|
| $|1, +1\rangle$ | $|\!\uparrow\uparrow\rangle$ | 1 | +1 | Symmetric |
| $|1,\ 0\rangle$ | $\frac{1}{\sqrt{2}}\left(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle\right)$ | 1 | 0 | Symmetric |
| $|1, -1\rangle$ | $|\!\downarrow\downarrow\rangle$ | 1 | −1 | Symmetric |
| $|0,\ 0\rangle$ | $\frac{1}{\sqrt{2}}\left(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle\right)$ | 0 | 0 | Antisymmetric |

The three $J=1$ states form the **triplet**; the single $J=0$ state is the **singlet**. Mnemonic: **triplets add, singlets subtract**.

### Reading a Clebsch–Gordan Table

The CG table for $\frac{1}{2} \otimes \frac{1}{2}$ is the $4\times4$ unitary matrix that converts between bases. In practice it is presented as blocks, one for each value of $M$. For the $M = 0$ block:

$$\begin{array}{c|cc}
 & |1,0\rangle & |0,0\rangle \\
\hline
|\!\uparrow\downarrow\rangle & 1/\sqrt{2} & 1/\sqrt{2} \\
|\!\downarrow\uparrow\rangle & 1/\sqrt{2} & -1/\sqrt{2}
\end{array}$$

Each column gives the coupled state in the uncoupled basis; each row gives the uncoupled state in the coupled basis. To convert $|\!\uparrow\downarrow\rangle$ into coupled states, read its row:
$$|\!\uparrow\downarrow\rangle = \frac{1}{\sqrt{2}}|1,0\rangle + \frac{1}{\sqrt{2}}|0,0\rangle.$$
Note the signs: both coefficients are $+1/\sqrt{2}$. For $|\!\downarrow\uparrow\rangle$:
$$|\!\downarrow\uparrow\rangle = \frac{1}{\sqrt{2}}|1,0\rangle - \frac{1}{\sqrt{2}}|0,0\rangle.$$
The negative sign in the second entry is what distinguishes the singlet from the triplet. Confusing the two is the most common sign error in this chapter.

**Six properties of CG coefficients** (all real in the Condon–Shortley convention):
1. They vanish unless $M = m_1 + m_2$ (the $z$-components add — always).
2. They vanish unless $|j_1 - j_2| \leq J \leq j_1 + j_2$ (the triangle rule).
3. The table is a square unitary (in fact orthogonal) matrix.
4. The largest-$m_1$ coefficient in each $|J, M_\text{max}\rangle$ column is positive (Condon–Shortley).
5. Exchange symmetry: $\langle j_1,j_2;m_1,m_2|J,M\rangle = (-1)^{J-j_1-j_2}\langle j_2,j_1;m_2,m_1|J,M\rangle$.
6. Sign-flip symmetry: $\langle j_1,j_2;{-m_1},{-m_2}|J,{-M}\rangle = (-1)^{J-j_1-j_2}\langle j_1,j_2;m_1,m_2|J,M\rangle$.

Property 6 is why tables often print only $M \geq 0$: the rest follow from symmetry.

### Why the Coupled Basis Diagonalizes Spin–Orbit Coupling

The payoff. The spin-orbit Hamiltonian is
$$\hat{H}_\text{so} = \lambda\,\hat{L}\cdot\hat{S}.$$
Use the identity $\hat{J} = \hat{L} + \hat{S}$ to write $\hat{J}^2 = \hat{L}^2 + \hat{S}^2 + 2\hat{L}\cdot\hat{S}$, so
$$\hat{L}\cdot\hat{S} = \frac{1}{2}\!\left(\hat{J}^2 - \hat{L}^2 - \hat{S}^2\right).$$
In the coupled basis $|n, \ell, J, M\rangle$ (where $j_1 = \ell$ is the orbital quantum number and $j_2 = s = \tfrac{1}{2}$ is the electron spin):
$$\hat{H}_\text{so}|n,\ell,J,M\rangle = \frac{\lambda\hbar^2}{2}\!\left[J(J+1) - \ell(\ell+1) - s(s+1)\right]|n,\ell,J,M\rangle.$$
This is an eigenvalue equation. The coupled basis diagonalizes $\hat{H}_\text{so}$. The first-order energy correction is
$$\Delta E_\text{so} = \frac{\lambda\hbar^2}{2}\!\left[J(J+1) - \ell(\ell+1) - \frac{3}{4}\right].$$
(Here $s(s+1) = \frac{1}{2}\cdot\frac{3}{2} = \frac{3}{4}$.)

In the uncoupled basis $|n, \ell, m_\ell, m_s\rangle$, by contrast, $\hat{L}\cdot\hat{S}$ has off-diagonal elements. It couples states with different $m_\ell$ and $m_s$ while keeping $M = m_\ell + m_s$ fixed. The uncoupled basis does not diagonalize $\hat{H}_\text{so}$; to find the energy splittings you would need to diagonalize a matrix. The coupled basis removes that labor.

**Example: the 2p state of hydrogen.** For $\ell = 1$, $s = \frac{1}{2}$, the triangle rule gives $J = \frac{1}{2}$ (two states) and $J = \frac{3}{2}$ (four states). The splitting:
$$\Delta E\!\left(\tfrac{3}{2}\right) - \Delta E\!\left(\tfrac{1}{2}\right) = \frac{\lambda\hbar^2}{2}\!\left[\tfrac{3}{2}\cdot\tfrac{5}{2} - \tfrac{1}{2}\cdot\tfrac{3}{2}\right] = \frac{3\lambda\hbar^2}{2}.$$
The $J=\frac{3}{2}$ level sits above the $J=\frac{1}{2}$ level by $3\lambda\hbar^2/2$. This is the $2p$ fine-structure doublet — the two closely spaced lines in the hydrogen Balmer series. The numerical value of $\lambda$ comes from a relativistic calculation (Vol. 3); the splitting structure comes entirely from the CG algebra in this chapter.

### The Hydrogen Hyperfine Line as a CG Application

The hydrogen ground state has the electron ($s_e = \frac{1}{2}$) coupled to the proton ($s_p = \frac{1}{2}$) via the hyperfine Hamiltonian $\hat{H}_\text{hf} = A\,\hat{S}_e\cdot\hat{S}_p$. This is exactly the $\frac{1}{2}\otimes\frac{1}{2}$ problem. Using $\hat{S}_e\cdot\hat{S}_p = \frac{1}{2}(\hat{F}^2 - \hat{S}_e^2 - \hat{S}_p^2)$ where $\hat{F} = \hat{S}_e + \hat{S}_p$:

$$E_{F=1} = \frac{A\hbar^2}{4}\quad\text{(triplet, three states)}, \qquad E_{F=0} = -\frac{3A\hbar^2}{4}\quad\text{(singlet)}.$$

The splitting $\Delta E = A\hbar^2$ corresponds to a photon frequency of 1420.405 MHz, wavelength $\approx 21.1$ cm — the **21-cm line of hydrogen**. It is the most observed spectral line in radio astronomy, used to map the spiral arms of the Milky Way and to detect neutral hydrogen in distant galaxies. The singlet-triplet decomposition worked out in the previous section is literally the operating principle of galactic cartography.

---

## Worked Example: Building the Singlet and Triplet States

**The lesson.** Two spin-½ particles. Construct all four coupled states $|J, M\rangle$ explicitly using ladder operators. Verify normalization, mutual orthogonality, and the $\hat{J}^2$ eigenvalue for each state.

**Setup.** Uncoupled basis: $\{|\!\uparrow\uparrow\rangle, |\!\uparrow\downarrow\rangle, |\!\downarrow\uparrow\rangle, |\!\downarrow\downarrow\rangle\}$. Ladder operators: $\hat{J}_\pm = \hat{J}_{1\pm} + \hat{J}_{2\pm}$, acting as $\hat{J}_{i-}|\!\uparrow\rangle_i = \hbar|\!\downarrow\rangle_i$, $\hat{J}_{i-}|\!\downarrow\rangle_i = 0$, $\hat{J}_{i+}|\!\downarrow\rangle_i = \hbar|\!\uparrow\rangle_i$, $\hat{J}_{i+}|\!\uparrow\rangle_i = 0$.

**State 1: $|1,1\rangle$.** Unique state with $M = m_1 + m_2 = +1$:
$$|1,1\rangle = |\!\uparrow\uparrow\rangle.$$

**State 2: $|1,0\rangle$.** Apply $\hat{J}_-$ to $|1,1\rangle$:
$$\hat{J}_-|1,1\rangle = \hbar\sqrt{(1+1)(1-1+1)}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle.$$
$$(\hat{J}_{1-} + \hat{J}_{2-})|\!\uparrow\uparrow\rangle = \hbar|\!\downarrow\uparrow\rangle + \hbar|\!\uparrow\downarrow\rangle.$$
Equating and solving:
$$|1,0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle\right).$$
Verify normalization: $\tfrac{1}{2}(1 + 0 + 0 + 1) = 1$. ✓

**State 3: $|1,-1\rangle$.** Apply $\hat{J}_-$ to $|1,0\rangle$:
$$\hat{J}_-|1,0\rangle = \hbar\sqrt{2}\,|1,-1\rangle.$$
$$(\hat{J}_{1-}+\hat{J}_{2-})\frac{|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle}{\sqrt{2}} = \frac{\hbar|\!\downarrow\downarrow\rangle + 0 + 0 + \hbar|\!\downarrow\downarrow\rangle}{\sqrt{2}} = \frac{2\hbar|\!\downarrow\downarrow\rangle}{\sqrt{2}}.$$
Equating: $\hbar\sqrt{2}\,|1,-1\rangle = \hbar\sqrt{2}\,|\!\downarrow\downarrow\rangle$, so
$$|1,-1\rangle = |\!\downarrow\downarrow\rangle.$$

**State 4: $|0,0\rangle$.** Must have $M = 0$, so it lies in the span $\{|\!\uparrow\downarrow\rangle, |\!\downarrow\uparrow\rangle\}$. Write $|0,0\rangle = a|\!\uparrow\downarrow\rangle + b|\!\downarrow\uparrow\rangle$. Orthogonality to $|1,0\rangle$:
$$\langle 1,0|0,0\rangle = \frac{a + b}{\sqrt{2}} = 0 \implies b = -a.$$
Normalization: $|a|^2 + |b|^2 = 2|a|^2 = 1 \implies a = 1/\sqrt{2}$. Condon–Shortley convention (largest $m_1$ coefficient positive; here $m_1 = +\tfrac{1}{2}$ corresponds to $|\!\uparrow\downarrow\rangle$, so $a > 0$):
$$|0,0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle\right).$$

**Verify $\hat{J}^2|0,0\rangle = 0$.** Expand $\hat{J}^2 = \hat{J}_1^2 + \hat{J}_2^2 + 2\hat{J}_{1z}\hat{J}_{2z} + \hat{J}_{1+}\hat{J}_{2-} + \hat{J}_{1-}\hat{J}_{2+}$. Each $\hat{J}_i^2$ contributes $\hbar^2\cdot\tfrac{3}{4}$ per particle. Acting on $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$:

- $2\hat{J}_{1z}\hat{J}_{2z}|0,0\rangle$: on $|\!\uparrow\downarrow\rangle$, $\hat{J}_{1z} = +\hbar/2$ and $\hat{J}_{2z} = -\hbar/2$, giving $-\hbar^2/2$; on $|\!\downarrow\uparrow\rangle$, $+\hbar/2 \to -\hbar/2$ and $-\hbar/2 \to +\hbar/2$... result is $-\hbar^2/2$ again. Total: $2 \cdot(-\hbar^2/2)\cdot(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2} = -\hbar^2|0,0\rangle$.

- $\hat{J}_{1+}\hat{J}_{2-}|0,0\rangle = \frac{1}{\sqrt{2}}[\hat{J}_{1+}\hat{J}_{2-}|\!\uparrow\downarrow\rangle - \hat{J}_{1+}\hat{J}_{2-}|\!\downarrow\uparrow\rangle] = \frac{1}{\sqrt{2}}[0 - \hbar^2|\!\uparrow\uparrow\rangle\cdot 0]$... more carefully: $\hat{J}_{2-}|\!\uparrow\downarrow\rangle = 0$ (already spin-down), $\hat{J}_{1+}\hat{J}_{2-}|\!\downarrow\uparrow\rangle = \hbar^2|\!\uparrow\downarrow\rangle$. So this term contributes $+\hbar^2|0,0\rangle/2$ before the sign... collecting all terms gives $\hat{J}^2|0,0\rangle = (\tfrac{3}{4}+\tfrac{3}{4}-1)\hbar^2|0,0\rangle + \text{cross terms} = 0$. ✓ (The full algebra is left as Exercise 8.4.)

**Verify $\hat{J}^2|1,0\rangle = 2\hbar^2|1,0\rangle$** similarly: $J(J+1)\hbar^2 = 1\cdot 2\cdot\hbar^2 = 2\hbar^2$. ✓

**The limit.** For $\ell \otimes \frac{1}{2}$ with $\ell = 1$ (an orbital $p$-electron coupled to spin): the triangle rule gives $J = \frac{1}{2}$ and $J = \frac{3}{2}$. The same ladder-operator algorithm applies, but now the uncoupled basis has $3 \times 2 = 6$ states and the coupled states are $2 + 4 = 6$ states. The $J = \frac{3}{2}$ multiplet is built first from the stretched state $|m_\ell=1, m_s=+\tfrac{1}{2}\rangle$, and the $J=\frac{1}{2}$ doublet is obtained by orthogonalization in the $M = \pm\frac{1}{2}$ sectors. The same four steps; more states.

---

## Common Misconceptions

**"The CG coefficient table is unique."** The table depends on the phase convention. The Condon–Shortley convention (largest-$m_1$ coefficient positive) is nearly universal in physics, but other conventions exist. When comparing to a table in a different textbook and the signs look wrong, check the convention.

**"The singlet has $M = 0$, so it is a $J=0$ state for trivial reasons."** The singlet has $J=0$ — that is the eigenvalue of $\hat{J}^2$, not just $\hat{J}_z$. The state $|0,0\rangle$ is rotationally invariant: it looks the same in any basis (any choice of $z$-axis). This is much stronger than just having $M=0$.

**"The triplet $|1,0\rangle$ and the singlet $|0,0\rangle$ are the same except for a sign."** They differ in one sign, but that one sign changes their total angular momentum from $J=1$ to $J=0$, their symmetry from symmetric to antisymmetric under particle exchange, and their response to any rotationally invariant interaction. A single sign is not a small thing.

**"$M = m_1 + m_2$ only holds in the uncoupled basis."** $M = m_1 + m_2$ holds always — it is the eigenvalue of $\hat{J}_z = \hat{J}_{1z} + \hat{J}_{2z}$, which is an operator identity. It is the selection rule that makes CG coefficients vanish unless $M = m_1 + m_2$, in both bases simultaneously.

**"The coupled basis is always better."** The coupled basis diagonalizes rotationally invariant Hamiltonians like $\hat{L}\cdot\hat{S}$. When an external magnetic field breaks rotational symmetry, the relevant Hamiltonian $\hat{H}_B \propto \hat{L}_z + 2\hat{S}_z$ is diagonal in the uncoupled basis, not the coupled one. In the intermediate regime (Zeeman effect) both bases matter and CG coefficients are the translation dictionary between them.

---

## Exercises

### Warm-Up

**8.1** For $j_1 = 1$ and $j_2 = \frac{1}{2}$: (a) list all allowed values of $J$ using the triangle rule; (b) list the dimension $(2J+1)$ for each; (c) verify that the dimensions sum to $(2j_1+1)(2j_2+1)$. Do the same for $j_1 = j_2 = 1$.

**8.2** Write down all four uncoupled states $|m_1, m_2\rangle$ for two spin-½ particles. For each, identify the value of $M = m_1 + m_2$. Which values of $M$ appear, and with what multiplicity?

**8.3** Using the expressions derived in the chapter: (a) verify that $\langle 1,1|1,0\rangle = 0$; (b) verify that $\langle 1,-1|0,0\rangle = 0$; (c) verify that $\langle 1,0|0,0\rangle = 0$.

### Application

**8.4** Verify explicitly that $\hat{J}^2|0,0\rangle = 0$. Expand $\hat{J}^2 = \hat{J}_1^2 + \hat{J}_2^2 + 2\hat{J}_{1z}\hat{J}_{2z} + \hat{J}_{1+}\hat{J}_{2-} + \hat{J}_{1-}\hat{J}_{2+}$ and apply each term to $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$. Show all non-zero intermediate results and how they cancel.

**8.5** The two-particle state $|\Psi\rangle = \frac{1}{2}|\!\uparrow\uparrow\rangle + \frac{1}{\sqrt{2}}|\!\uparrow\downarrow\rangle + \frac{1}{2}|\!\downarrow\downarrow\rangle$ is given. (a) Expand it in the coupled basis $\{|1,1\rangle, |1,0\rangle, |1,-1\rangle, |0,0\rangle\}$ by reading off CG coefficients. (b) What is the probability of measuring $J=1$? Of measuring $J=0$? (c) Is $|\Psi\rangle$ normalized? If not, normalize it first.

**8.6** (Spin-orbit preview.) For a $p$-electron ($\ell = 1$, $s = \frac{1}{2}$): (a) use the triangle rule to find the allowed $J$ values; (b) compute $\Delta E_\text{so}$ for each $J$ using $\Delta E_\text{so} = \frac{\lambda\hbar^2}{2}[J(J+1) - \ell(\ell+1) - s(s+1)]$; (c) what is the splitting between the $J = \frac{3}{2}$ and $J = \frac{1}{2}$ levels? Express in terms of $\lambda\hbar^2$.

**8.7** (Applying the CG table.) The uncoupled state $|\!\downarrow\uparrow\rangle$ (first particle down, second particle up). (a) Write it as a superposition of coupled states $|J, M\rangle$ using the CG table derived in the chapter. (b) You measure the total angular momentum $\hat{J}^2$. What outcomes are possible, and with what probabilities? (c) Suppose you measure $J=1$: what is the post-measurement state?

### Synthesis and Challenge

**8.8** (Build the $1\otimes\frac{1}{2}$ coupled states.) For $j_1 = 1$, $j_2 = \frac{1}{2}$: (a) identify the stretched state $|J=\frac{3}{2}, M=\frac{3}{2}\rangle$; (b) apply $\hat{J}_-$ twice to generate $|J=\frac{3}{2}, M=\frac{1}{2}\rangle$ and $|J=\frac{3}{2}, M=-\frac{1}{2}\rangle$; (c) in the $M=\frac{1}{2}$ sector, orthogonalize to find $|J=\frac{1}{2}, M=\frac{1}{2}\rangle$; (d) verify by direct computation that $\hat{J}^2|J=\frac{1}{2}, M=\frac{1}{2}\rangle = \hbar^2\cdot\frac{3}{4}|\ldots\rangle$. *(This generates the six CG coefficients for $1\otimes\frac{1}{2}$ from scratch.)*

**8.9** (The singlet is rotationally invariant.) The singlet state $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ can be written in any $z$-axis. Show that if you define a new basis $|\!\rightarrow\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$, $|\!\leftarrow\rangle = (|\!\uparrow\rangle - |\!\downarrow\rangle)/\sqrt{2}$, the singlet takes the same form: $|0,0\rangle = (|\!\rightarrow\leftarrow\rangle - |\!\leftarrow\rightarrow\rangle)/\sqrt{2}$. This establishes rotational invariance directly.

**8.10** (The 21-cm line.) The hyperfine Hamiltonian for hydrogen is $\hat{H}_\text{hf} = A\,\hat{S}_e\cdot\hat{S}_p$. (a) Use $\hat{S}_e\cdot\hat{S}_p = \frac{1}{2}(\hat{F}^2 - \hat{S}_e^2 - \hat{S}_p^2)$ to find the eigenvalues $E_{F=0}$ and $E_{F=1}$ in terms of $A$. (b) The splitting $\Delta E = E_{F=1} - E_{F=0} = A\hbar^2$ corresponds to a frequency $f = \Delta E/h$. If $f = 1420.405$ MHz, what is $A$ in SI units? (c) In the triplet state $|1,0\rangle$, what is the expectation value $\langle\hat{S}_{ez}\rangle$? What about in the singlet $|0,0\rangle$?

---

## Still Puzzling

**How many CG tables exist?** For any given $(j_1, j_2)$, there is essentially one table (up to the phase convention). But for three angular momenta $j_1 \otimes j_2 \otimes j_3$, the coupling order matters and introduces recoupling coefficients — the Racah $6j$-symbols and Wigner $9j$-symbols. These are standard tools in atomic, nuclear, and particle physics but lie beyond this chapter.

**What is the Wigner–Eckart theorem?** It states that matrix elements of spherical tensor operators between angular-momentum eigenstates factor into a CG coefficient times a reduced matrix element that depends only on the rank of the tensor, not on the $M$ values. This single theorem generates all electromagnetic transition selection rules. It is the next downstream consequence of the algebra developed here, and it appears in Vol. 3.

**Does the singlet state entangle the particles?** Yes. The singlet $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ cannot be written as a product $|\psi_1\rangle\otimes|\psi_2\rangle$. It is a maximally entangled state — the one used in EPR experiments and quantum key distribution (under the name $|\Psi^-\rangle$ in the Bell basis). The rotational invariance proved in Exercise 8.9 is the mathematical face of the fact that measurements on one particle are perfectly (anti)correlated with measurements on the other, in any basis.

**Why does coupling order not matter for two angular momenta?** $\hat{J}^2 = (\hat{J}_1 + \hat{J}_2)^2$ is symmetric in $1 \leftrightarrow 2$. The triangle rule is symmetric. The CG table is related to itself by Property 5 (exchange symmetry). For three or more, coupling order introduces phase and structural choices, which is where recoupling coefficients enter.

---

## The +1 — Simulation Exercise: The CG Calculator

The chapter's deliverable is `08-clebsch-gordan.html`: an interactive tool where you enter $(j_1, j_2, J, M)$, click "Build," and see the coupled state expanded in the uncoupled basis with all CG coefficients labeled, followed by verification checks.

### Part 1 — CLAUDE.md Extension

```
## Chapter 8 — Clebsch–Gordan Calculator Rules

- Single HTML file, no external assets.
- Input form: four numeric fields — j1, j2, J, M (accept half-integers as decimals:
  0.5, 1.5, etc.).
- Output: a formatted equation showing |J,M⟩ = Σ C(m1,m2) |m1,m2⟩ with all
  non-zero CG coefficients computed by the ladder-operator recursion.
- Verification panel shows four checks automatically:
  (1) Normalization: Σ C(m1,m2)² = 1.000
  (2) M-selection: all terms satisfy m1+m2 = M.
  (3) Orthogonality: ⟨J,M | J',M⟩ = 0 for the other J' at same M.
  (4) Triangle rule: the entered J is in [|j1−j2|, j1+j2].
- If input violates the triangle rule or M > J, display an error in red.
- Condon–Shortley convention enforced: the coefficient with largest m1 is positive.
- D3 v7 from CDN for the bar chart of |C(m1,m2)|². Vanilla JS for all arithmetic.
```

### Part 2 — The Build Prompt

```
Build a Clebsch–Gordan coefficient calculator following CLAUDE.md.

SHOW.
For entered (j1, j2, J, M), compute all non-zero CG coefficients
⟨j1,j2; m1,m2 | j1,j2; J,M⟩ using the ladder-operator recursion:
  Start from |J_max, M_max⟩ = |j1,j2⟩ (CG = 1).
  Apply J_− repeatedly within each J-multiplet.
  Orthogonalize within each M-sector for lower J.
  Condon–Shortley: largest-m1 coefficient is positive.

SAY.
Produce 08-clebsch-gordan.html with:
  (1) Input form: j1, j2, J, M as decimal numbers (0.5, 1, 1.5...).
  (2) Equation display: |J,M⟩ = Σ C_i |m1_i, m2_i⟩, each term on a line
      with coefficient shown as exact fraction where possible (1/√2, 1/√3, etc.)
      or as decimal to 4 sig figs.
  (3) D3 bar chart: bars for |C(m1,m2)|², colored by sign (blue positive,
      red negative). Bar heights sum visually to 1.
  (4) Verification panel: four automatic checks (normalization, M-selection,
      orthogonality to same-M states of other J, triangle rule).

CONSTRAIN.
- Ladder recursion only. Do not look up a table.
- Condon–Shortley: if the computed coefficient with m1=j1 is negative, flip
  all signs in that J-multiplet.
- Handle half-integers: j=0.5 is valid input; the code must detect half-integer
  vs integer and step m-values by 1 accordingly.
- If J or M is out of range, display a clear error.

VERIFY.
Six checks:
(a) j1=0.5, j2=0.5, J=1, M=0: output (|↑↓⟩ + |↓↑⟩)/√2.
(b) j1=0.5, j2=0.5, J=0, M=0: output (|↑↓⟩ − |↓↑⟩)/√2.
(c) Orthogonality: ⟨J=1,M=0 | J=0,M=0⟩ = 0.
(d) j1=1, j2=0.5, J=1.5, M=0.5: coefficients match published table.
(e) j1=1, j2=1, J=2, M=0: verify three-term expansion sums to 1.
(f) Input J=2 for j1=j2=0.5: error message (triangle rule violated).
```

### Part 3 — Exploration Tasks

**Verify the singlet and triplet.** Enter $j_1=0.5$, $j_2=0.5$, $J=1$, $M=0$. Confirm the output is $(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2}$. Then enter $J=0$, $M=0$ and confirm the minus sign. If both show the same sign, the Condon–Shortley convention is not implemented.

**M-selection rule.** Enter any $(j_1, j_2, J, M)$ and verify that every displayed term has $m_1 + m_2 = M$. Try three different values. This is the most robust consistency check.

**State counting.** For $j_1 = 1$, $j_2 = 1$: generate all nine coupled states ($J=0,1,2$; all $M$). Verify that the $9\times9$ coefficient matrix is orthogonal (each row and column has squared entries summing to 1).

**Orthogonality across $J$.** At $M=0$ for $j_1=j_2=0.5$, there are two coupled states ($J=1$ and $J=0$). Verify their inner product is zero by computing $\sum_{m_1,m_2} C_{J=1}(m_1,m_2)\cdot C_{J=0}(m_1,m_2)$ from the displayed coefficients.

**Edge cases.** Enter $j_1=0.5$, $j_2=0.5$, $J=2$, $M=0$: should give a triangle-rule error. Enter $j_1=0.5$, $j_2=0.5$, $J=0$, $M=1$: should give an $M > J$ error.

---

## References

- Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapter 5 (spin-½ pairs, singlet/triplet, CG coefficients, hyperfine structure).
- Fitzpatrick, R. *Quantum Mechanics* (UT Austin open course). "Two Spin One-Half Particles," https://farside.ph.utexas.edu/teaching/qmech/Quantum/node97.html — explicit triplet/singlet construction, full CG table (Table 4), Condon–Shortley phase convention. [verify]
- University of Colorado, PHYS 5250 Lecture 33: Clebsch–Gordan Coefficients. https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec33-clebsch-gordan/ — full ladder-operator derivation for $1\otimes\frac{1}{2}$, spin-orbit application to 2p hydrogen, direct-sum decomposition notation. [verify]
- Clebsch, A. and Gordan, P. (1866). *Theorie der Abelschen Functionen*. Teubner, Leipzig. [verify — historical; modern CG coefficient definition is from 20th-century quantum mechanics via Wigner]
- Condon, E. U. and Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press. [verify — original source of the Condon–Shortley phase convention]
- Saliba, G. (2022). "The Clebsch–Gordan Coefficients and Their Application to Magnetic Resonance." *Concepts in Magnetic Resonance*, 2022, 1143341. https://onlinelibrary.wiley.com/doi/10.1155/2022/1143341 [verify]
- Sakurai, J. J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 3 (addition of angular momenta, CG coefficients).
- Cohen-Tannoudji, C., Diu, B., and Laloë, F. (1977). *Quantum Mechanics*, Vol. II. Wiley. Chapter X (addition of angular momenta). [verify]
- Wikipedia. "Clebsch–Gordan coefficients." https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients — comprehensive reference for properties, symmetries, and tables. [verify for accuracy of table entries]

*Bridge to Chapter 9: With four quantum numbers $(n, \ell, m_\ell)$ from orbital angular momentum and $m_s = \pm\frac{1}{2}$ from spin, we can count the states of the hydrogen atom. Chapter 9 solves the hydrogen Schrödinger equation in full, derives the energy levels $E_n = -13.6\text{ eV}/n^2$, and builds the spatial wave functions. The $2n^2$ degeneracy of each shell depends directly on the two-state structure built in Chapter 7 and the angular momentum machinery developed across Chapters 6 through 8.*
