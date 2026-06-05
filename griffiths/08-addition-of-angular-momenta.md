# Chapter 8 — Addition of Angular Momenta
*Why the hydrogen atom's most famous spectral line comes down to a single minus sign.*

The hydrogen 21-centimeter line is the most observed spectral line in radio astronomy. It is the tool with which astronomers map the spiral arms of the Milky Way and detect neutral hydrogen in galaxies billions of light-years away. Its wavelength — precisely 21.106 cm, frequency 1420.405 MHz — is so characteristic that it was engraved on the Voyager probe's golden record as a unit of time and distance that any intelligent civilization might recognize.

The 21-centimeter line arises from a transition between two quantum states of the hydrogen ground state. The electron and proton each have spin-½, and when their spins are parallel the energy is slightly higher than when they are antiparallel. The atom emits the 21-cm photon when the spins flip from parallel to antiparallel — a transition from the triplet state to the singlet state.

The singlet and triplet states are not complicated objects. The triplet is the combination $(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2}$; the singlet is $(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$. They differ by a single minus sign. That single sign changes the total angular momentum from $J = 1$ to $J = 0$, changes the exchange symmetry, and — through the hyperfine Hamiltonian — changes the energy by exactly the amount corresponding to a 21-cm photon.

This chapter constructs those states, explains what they mean, and establishes why the coupled basis is the right one for computing energy splittings.

<!-- → [FIGURE: diagram of the hydrogen hyperfine structure — showing the two energy levels (triplet F=1 and singlet F=0) with the 21-cm photon emitted in the transition; the triplet should be labeled with the three M_F states and their spin configurations; include the frequency 1420.405 MHz and wavelength 21.1 cm] -->

![diagram of the hydrogen hyperfine structure — showing the two energy levels (triplet F=1 and singlet F=0) with the 21-cm photon emitted in…](../images/08-addition-of-angular-momenta-fig-01.png)
*Figure 8.1 — diagram of the hydrogen hyperfine structure — showing the two energy levels (triplet F=1 and singlet F=0) with the 21-cm photon emitted in…*

---

## Two Bases for the Same Space

Start with the simplest two-spin system: two particles, each with spin-½, at fixed positions so only their spins matter. The natural description is uncoupled: particle 1 is either up or down, particle 2 is either up or down, giving four basis states

$$|\!\uparrow\uparrow\rangle, \quad |\!\uparrow\downarrow\rangle, \quad |\!\downarrow\uparrow\rangle, \quad |\!\downarrow\downarrow\rangle.$$

These are eigenstates of $\hat{S}_{1z}$ and $\hat{S}_{2z}$ individually. This is the **uncoupled basis**.

Most of the interesting physics does not care about $\hat{S}_{1z}$ or $\hat{S}_{2z}$ individually. The hyperfine interaction goes as $\hat{S}_e\cdot\hat{S}_p$. Spin-orbit coupling goes as $\hat{L}\cdot\hat{S}$. These Hamiltonians are rotationally invariant — they commute with the total angular momentum $\hat{J} = \hat{J}_1 + \hat{J}_2$, but not with the individual $z$-components. They are diagonal in a different basis.

The **coupled basis** $|J, M\rangle$ consists of simultaneous eigenstates of $\hat{J}^2 = (\hat{J}_1 + \hat{J}_2)^2$ and $\hat{J}_z = \hat{J}_{1z} + \hat{J}_{2z}$:

$$\hat{J}^2|J, M\rangle = \hbar^2 J(J+1)|J, M\rangle, \qquad \hat{J}_z|J, M\rangle = \hbar M|J, M\rangle.$$

Note what $\hat{J}^2$ is: it is $(\hat{J}_1 + \hat{J}_2)^2 = \hat{J}_1^2 + \hat{J}_2^2 + 2\hat{J}_1\cdot\hat{J}_2$. The cross term $2\hat{J}_1\cdot\hat{J}_2$ mixes the individual spins. In the coupled basis, $j_1$ and $j_2$ remain good quantum numbers — $\hat{J}_1^2$ and $\hat{J}_2^2$ commute with everything. What becomes uncertain is the individual $z$-projections $m_1$ and $m_2$.

Both bases span the same four-dimensional space. The **Clebsch–Gordan (CG) coefficients** are the entries of the unitary matrix relating them:

$$|J, M\rangle = \sum_{m_1, m_2}\langle j_1, j_2; m_1, m_2|j_1, j_2; J, M\rangle\,|j_1, j_2; m_1, m_2\rangle.$$

---

## The Triangle Rule

Which values of $J$ can appear when combining $j_1$ and $j_2$? The **triangle rule**:

$$J = |j_1 - j_2|,\; |j_1 - j_2| + 1,\; \ldots,\; j_1 + j_2,$$

in integer steps. Each value appears exactly once.

Before doing any algebra, verify the state count:

$$\sum_{J=|j_1-j_2|}^{j_1+j_2}(2J+1) = (2j_1+1)(2j_2+1).$$

This always holds and is worth checking first. For $\frac{1}{2}\otimes\frac{1}{2}$: $J = 0$ and $J = 1$, giving $(1) + (3) = 4 = 2\times2$. ✓ For $1\otimes\frac{1}{2}$: $J = \frac{1}{2}$ and $J = \frac{3}{2}$, giving $(2) + (4) = 6 = 3\times2$. ✓ For $1\otimes1$: $J = 0, 1, 2$, giving $(1)+(3)+(5) = 9 = 3\times3$. ✓

The representation-theoretic notation: $j_1\otimes j_2 = |j_1-j_2|\oplus(|j_1-j_2|+1)\oplus\cdots\oplus(j_1+j_2)$. For two spin-½ particles: $\frac{1}{2}\otimes\frac{1}{2} = 0\oplus 1$ — the four-dimensional product space decomposes into a one-dimensional singlet and a three-dimensional triplet.

<!-- → [TABLE: three standard combinations with triangle rule — rows: ½⊗½, 1⊗½, 1⊗1; columns: combination, allowed J values, dimensions (2J+1), total dimension, state-count check; this is the reference table for the chapter] -->

---

## Building the States: The Ladder Operator Method

The systematic procedure uses the lowering operator $\hat{J}_- = \hat{J}_{1-} + \hat{J}_{2-}$, which acts on coupled states as

$$\hat{J}_-|J, M\rangle = \hbar\sqrt{(J+M)(J-M+1)}\,|J, M-1\rangle,$$

and on individual spin states as $\hat{J}_{i-}|\!\uparrow\rangle_i = \hbar|\!\downarrow\rangle_i$ and $\hat{J}_{i-}|\!\downarrow\rangle_i = 0$.

The algorithm has four steps, which work for any $(j_1, j_2)$:

**Step 1.** Identify the stretched state $|J_\text{max}, M_\text{max}\rangle = |j_1+j_2, j_1+j_2\rangle$. It equals the unique uncoupled state with $m_1 = j_1$ and $m_2 = j_2$ — no ambiguity.

**Step 2.** Apply $\hat{J}_-$ repeatedly to generate all states within the $J = j_1 + j_2$ multiplet.

**Step 3.** In each $M$-sector, find the state belonging to $J = j_1 + j_2 - 1$ by requiring orthogonality to all states already found in that sector.

**Step 4.** Apply $\hat{J}_-$ to generate the rest of the $J = j_1 + j_2 - 1$ multiplet, then orthogonalize for the next lower $J$, and repeat.

The **Condon–Shortley phase convention** fixes the remaining sign ambiguity: the CG coefficient with the largest $m_1$ value in each coupled state is taken to be positive. Almost universally adopted.

---

## The $\frac{1}{2}\otimes\frac{1}{2}$ Case Explicitly

**State 1: $|1, 1\rangle$.** The only uncoupled state with $M = m_1 + m_2 = +1$ is $|\!\uparrow\uparrow\rangle$:

$$|1, 1\rangle = |\!\uparrow\uparrow\rangle.$$

**State 2: $|1, 0\rangle$.** Apply $\hat{J}_-$ to both sides. Left side: $\hat{J}_-|1,1\rangle = \hbar\sqrt{2}\,|1,0\rangle$. Right side: $(\hat{J}_{1-}+\hat{J}_{2-})|\!\uparrow\uparrow\rangle = \hbar|\!\downarrow\uparrow\rangle + \hbar|\!\uparrow\downarrow\rangle$. Equating:

$$|1, 0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle\right).$$

Symmetric under exchange of the two particles.

**State 3: $|1, -1\rangle$.** Apply $\hat{J}_-$ to $|1,0\rangle$:

$$|1, -1\rangle = |\!\downarrow\downarrow\rangle.$$

**State 4: $|0, 0\rangle$.** Must have $M = 0$, so it is some linear combination $a|\!\uparrow\downarrow\rangle + b|\!\downarrow\uparrow\rangle$. Orthogonality to $|1,0\rangle$ forces $a + b = 0$, so $b = -a$. Normalization gives $a = 1/\sqrt{2}$. The Condon–Shortley convention says the coefficient of $|\!\uparrow\downarrow\rangle$ (which has $m_1 = +\frac{1}{2}$, the larger value) should be positive:

$$|0, 0\rangle = \frac{1}{\sqrt{2}}\!\left(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle\right).$$

Antisymmetric under exchange of the two particles.

Verify orthogonality: $\langle 1,0|0,0\rangle = \frac{1}{2}(1-1) = 0$. ✓

The four states assembled:

| State | Expression | $J$ | $M$ | Exchange symmetry |
|-------|-----------|-----|-----|-------------------|
| $\|1, +1\rangle$ | $\|\!\uparrow\uparrow\rangle$ | 1 | +1 | Symmetric |
| $\|1,\ 0\rangle$ | $\frac{1}{\sqrt{2}}(\|\!\uparrow\downarrow\rangle + \|\!\downarrow\uparrow\rangle)$ | 1 | 0 | Symmetric |
| $\|1, -1\rangle$ | $\|\!\downarrow\downarrow\rangle$ | 1 | −1 | Symmetric |
| $\|0,\ 0\rangle$ | $\frac{1}{\sqrt{2}}(\|\!\uparrow\downarrow\rangle - \|\!\downarrow\uparrow\rangle)$ | 0 | 0 | Antisymmetric |

The three $J=1$ states are the **triplet**. The single $J=0$ state is the **singlet**. Triplets add, singlets subtract.

Now verify that $|0,0\rangle$ really has $J=0$. Since $|0,0\rangle$ is orthogonal to all three $|1,M\rangle$ states and $\hat{J}^2$ commutes with $\hat{J}_z$, any $\hat{J}^2|0,0\rangle$ must lie in the span of $|1,0\rangle$ and $|0,0\rangle$. Computing $\langle 1,0|\hat{J}^2|0,0\rangle = \langle \hat{J}^2 \cdot 1,0|0,0\rangle = 2\hbar^2\langle 1,0|0,0\rangle = 0$. So $\hat{J}^2|0,0\rangle = c|0,0\rangle$ for some constant $c$. From the direct calculation, $c = 0$. The singlet has zero total angular momentum. ✓

<!-- → [TABLE: the four ½⊗½ coupled states — the table above, formatted cleanly with state label, expression in uncoupled basis, J, M, exchange symmetry; this is the definitive reference for the chapter's main result] -->

---

## Reading a CG Table

The Clebsch–Gordan table for the $M=0$ sector of $\frac{1}{2}\otimes\frac{1}{2}$ is:

$$\begin{array}{c|cc}
 & |1,0\rangle & |0,0\rangle \\
\hline
|\!\uparrow\downarrow\rangle & 1/\sqrt{2} & 1/\sqrt{2} \\[4pt]
|\!\downarrow\uparrow\rangle & 1/\sqrt{2} & -1/\sqrt{2}
\end{array}$$

Each column gives a coupled state expanded in the uncoupled basis. To convert $|\!\uparrow\downarrow\rangle$, read its row:

$$|\!\uparrow\downarrow\rangle = \frac{1}{\sqrt{2}}|1,0\rangle + \frac{1}{\sqrt{2}}|0,0\rangle.$$

To convert $|\!\downarrow\uparrow\rangle$:

$$|\!\downarrow\uparrow\rangle = \frac{1}{\sqrt{2}}|1,0\rangle - \frac{1}{\sqrt{2}}|0,0\rangle.$$

The minus sign distinguishes the singlet coefficient from the triplet coefficient. Writing both entries as $+1/\sqrt{2}$ is wrong — the table would be non-unitary.

Six properties of CG coefficients hold for all $(j_1, j_2)$: the coefficient $\langle j_1,j_2;m_1,m_2|J,M\rangle$ vanishes unless $M = m_1 + m_2$ (always exact — $z$-components add); it vanishes unless the triangle rule is satisfied; the table is orthogonal (entries are real in the Condon–Shortley convention); the coefficient with the largest $m_1$ in each $|J, M_\text{max}\rangle$ column is positive; exchange symmetry relates the $(j_1, j_2)$ table to the $(j_2, j_1)$ table by a phase; sign-flip symmetry generates $M < 0$ entries from $M \geq 0$ entries.

---

## Why the Coupled Basis Matters: Spin-Orbit Coupling

The spin-orbit Hamiltonian is $\hat{H}_\text{so} = \lambda\,\hat{L}\cdot\hat{S}$. Use the identity $\hat{J} = \hat{L} + \hat{S}$ to expand:

$$\hat{J}^2 = \hat{L}^2 + \hat{S}^2 + 2\hat{L}\cdot\hat{S} \implies \hat{L}\cdot\hat{S} = \frac{1}{2}\!\left(\hat{J}^2 - \hat{L}^2 - \hat{S}^2\right).$$

In the coupled basis $|n,\ell,J,M\rangle$, every operator on the right side is diagonal:

$$\hat{H}_\text{so}|n,\ell,J,M\rangle = \frac{\lambda\hbar^2}{2}\!\left[J(J+1) - \ell(\ell+1) - s(s+1)\right]|n,\ell,J,M\rangle.$$

This is an eigenvalue equation. The energy correction is just a number. In the uncoupled basis $|n,\ell,m_\ell,m_s\rangle$, by contrast, $\hat{L}\cdot\hat{S}$ has off-diagonal terms coupling states with different $m_\ell$ and $m_s$ while keeping $M = m_\ell + m_s$ fixed. Finding the energy splittings in the uncoupled basis requires diagonalizing a matrix. The coupled basis eliminates that entirely.

For the $2p$ state of hydrogen ($\ell = 1$, $s = \frac{1}{2}$): the triangle rule gives $J = \frac{1}{2}$ (two states) and $J = \frac{3}{2}$ (four states). The splitting is

$$\Delta E\!\left(\tfrac{3}{2}\right) - \Delta E\!\left(\tfrac{1}{2}\right) = \frac{\lambda\hbar^2}{2}\!\left[\tfrac{3}{2}\cdot\tfrac{5}{2} - \tfrac{1}{2}\cdot\tfrac{3}{2}\right] = \frac{3\lambda\hbar^2}{2}.$$

This is the hydrogen $2p$ fine-structure doublet. The ratio $3:1$ between the spacings of the two groups comes entirely from the CG algebra.

---

## The 21-Centimeter Line

Return to where we started. The hydrogen hyperfine Hamiltonian is $\hat{H}_\text{hf} = A\,\hat{S}_e\cdot\hat{S}_p$, where $A$ encodes the magnetic interaction between electron and proton. Using $\hat{F} = \hat{S}_e + \hat{S}_p$ and the same identity:

$$\hat{S}_e\cdot\hat{S}_p = \frac{1}{2}\!\left(\hat{F}^2 - \hat{S}_e^2 - \hat{S}_p^2\right).$$

The $F=1$ triplet has $F(F+1) = 2$, $s_e(s_e+1) = s_p(s_p+1) = \frac{3}{4}$, giving energy $A\hbar^2(2-\frac{3}{4}-\frac{3}{4})/2 = A\hbar^2/4$. The $F=0$ singlet has $F(F+1) = 0$, giving energy $A\hbar^2(0-\frac{3}{4}-\frac{3}{4})/2 = -3A\hbar^2/4$.

The splitting is $\Delta E = A\hbar^2$. For hydrogen, $A\hbar^2 = 5.87\times10^{-6}$ eV, corresponding to $f = 1420.405$ MHz and $\lambda = 21.1$ cm.

The transition from triplet to singlet — from $(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2}$ to $(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ — is the one minus sign that makes the 21-cm line.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the triangle rule and state counting.*
   For $j_1 = 1$, $j_2 = \frac{1}{2}$: (a) list all allowed $J$ using the triangle rule; (b) list the dimension $2J+1$ for each; (c) verify the dimensions sum to $(2j_1+1)(2j_2+1)$. Repeat for $j_1 = j_2 = 1$.
   *Tests: ability to apply the triangle rule and verify state counts before any algebra.*

2. *Difficulty: Warm-up — tests $M = m_1 + m_2$ and the uncoupled basis structure.*
   Write all four uncoupled states $|m_1, m_2\rangle$ for two spin-½ particles and identify $M = m_1 + m_2$ for each. Which values of $M$ appear, and with what multiplicity? Which of the four states cannot appear in any $|J, M\rangle$ with $J = 0$?
   *Tests: structure of the uncoupled basis and the $M$-selection rule before CG coefficients are invoked.*

3. *Difficulty: Warm-up — tests orthogonality of the four coupled states.*
   Using the coupled-state expressions derived in the chapter: (a) verify $\langle 1,1|1,0\rangle = 0$; (b) verify $\langle 1,-1|0,0\rangle = 0$; (c) verify $\langle 1,0|0,0\rangle = 0$. For each calculation, identify which orthogonality mechanism is responsible (different $J$, different $M$, or same-$M$ orthogonality by construction).
   *Tests: command of the coupled-state expressions and understanding of what enforces each orthogonality.*

**Application**

4. *Difficulty: Application — verifies $\hat{J}^2|0,0\rangle = 0$ by direct computation.*
   Expand $\hat{J}^2 = \hat{J}_1^2 + \hat{J}_2^2 + 2\hat{J}_{1z}\hat{J}_{2z} + \hat{J}_{1+}\hat{J}_{2-} + \hat{J}_{1-}\hat{J}_{2+}$ and apply each term to $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$. Show all non-zero intermediate results and confirm the cancellations. Then repeat for $|1,0\rangle$ and confirm $\hat{J}^2|1,0\rangle = 2\hbar^2|1,0\rangle$.
   *Tests: ability to apply $\hat{J}^2$ term by term to a superposition; the cancellations in the singlet are the computational proof that $J = 0$.*

5. *Difficulty: Application — converts an uncoupled state to coupled basis using the CG table.*
   The state $|\Psi\rangle = \frac{1}{2}|\!\uparrow\uparrow\rangle + \frac{1}{\sqrt{2}}|\!\uparrow\downarrow\rangle + \frac{1}{2}|\!\downarrow\downarrow\rangle$. (a) Check normalization. (b) Expand in the coupled basis $\{|1,1\rangle, |1,0\rangle, |1,-1\rangle, |0,0\rangle\}$ by reading the CG table. (c) What is the probability of measuring $J=1$? Of measuring $J=0$? (d) If $J=1$ is measured, what is the post-measurement state?
   *Tests: use of the CG table to expand an arbitrary state; Born rule for composite observables.*

6. *Difficulty: Application — spin-orbit energy splittings.*
   For a $p$-electron coupled to spin-½ ($\ell = 1$, $s = \frac{1}{2}$): (a) apply the triangle rule to find the allowed $J$; (b) compute $\Delta E_\text{so}$ for each $J$ using $\frac{\lambda\hbar^2}{2}[J(J+1) - \ell(\ell+1) - s(s+1)]$; (c) compute the splitting between the two levels in units of $\lambda\hbar^2$; (d) which level is higher in energy for $\lambda > 0$?
   *Tests: direct application of $\hat{L}\cdot\hat{S}$ in the coupled basis; produces the hydrogen 2p fine-structure result.*

7. *Difficulty: Application — the 21-cm line quantitatively.*
   The hyperfine Hamiltonian is $\hat{H}_\text{hf} = A\,\hat{S}_e\cdot\hat{S}_p$. (a) Use the identity $\hat{S}_e\cdot\hat{S}_p = \frac{1}{2}(\hat{F}^2 - \hat{S}_e^2 - \hat{S}_p^2)$ to find $E_{F=1}$ and $E_{F=0}$ in terms of $A$ and $\hbar$. (b) Show the splitting is $\Delta E = A\hbar^2$. (c) The observed frequency is 1420.405 MHz; compute $A$ in SI units. (d) In the triplet state $|1,0\rangle$, what is $\langle\hat{S}_{ez}\rangle$?
   *Tests: uses the CG algebra to derive the hyperfine energies; connects to the most observed spectral line in radio astronomy.*

**Synthesis**

8. *Difficulty: Synthesis — builds the $1\otimes\frac{1}{2}$ coupled states from scratch.*
   For $j_1 = 1$, $j_2 = \frac{1}{2}$: (a) identify the stretched state $|J=\frac{3}{2}, M=\frac{3}{2}\rangle$; (b) apply $\hat{J}_-$ twice to generate $|J=\frac{3}{2}, M=\frac{1}{2}\rangle$ and $|J=\frac{3}{2}, M=-\frac{1}{2}\rangle$; (c) in the $M=\frac{1}{2}$ sector, orthogonalize to find $|J=\frac{1}{2}, M=\frac{1}{2}\rangle$; (d) verify by direct calculation that $\hat{J}^2$ gives eigenvalue $\frac{3}{4}\hbar^2$ on this state. This generates all six CG coefficients for $1\otimes\frac{1}{2}$ from the ladder algorithm alone.
   *Tests: end-to-end execution of the four-step ladder algorithm for a case not worked in the chapter; student must handle three-dimensional spin-1 states.*

9. *Difficulty: Synthesis — rotational invariance of the singlet.*
   Define the $x$-basis states $|\!\rightarrow\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ and $|\!\leftarrow\rangle = (|\!\uparrow\rangle - |\!\downarrow\rangle)/\sqrt{2}$. (a) Express $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$ in terms of $|\!\rightarrow\rangle$ and $|\!\leftarrow\rangle$. (b) Substitute into the singlet $|0,0\rangle = (|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ and show that the result is $(|\!\rightarrow\leftarrow\rangle - |\!\leftarrow\rightarrow\rangle)/\sqrt{2}$ — the same form in the $x$-basis. (c) Explain what this implies about the result of measuring $\hat{S}_{1x}$ and $\hat{S}_{2x}$ on the singlet, and how it differs from the triplet $|1,0\rangle$.
   *Tests: explicit demonstration of rotational invariance; connects the $J=0$ property to correlation structure and anticipates entanglement.*

**Challenge**

10. *Difficulty: Challenge — the singlet as a maximally entangled state.*
    (a) A state $|\Psi\rangle = |\psi_1\rangle\otimes|\psi_2\rangle$ is called a product state. Show that the singlet $(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)/\sqrt{2}$ cannot be written as a product state by assuming $|\psi_1\rangle = a|\!\uparrow\rangle + b|\!\downarrow\rangle$ and $|\psi_2\rangle = c|\!\uparrow\rangle + d|\!\downarrow\rangle$ and showing the system $ac=0$, $ad=1/\sqrt{2}$, $bc=-1/\sqrt{2}$, $bd=0$ has no solution. (b) Suppose particle 1 is measured in the $\hat{S}_{1z}$ basis and the result is $+\hbar/2$. What is the conditional state of particle 2? (c) Suppose instead the measurement is in the $x$-basis and returns $+\hbar/2$ (i.e., $|\!\rightarrow\rangle$). What is the conditional state of particle 2? (d) In both cases the conditional state of particle 2 is determined. What property of the singlet makes this work regardless of which basis is used for particle 1?
    *Tests: non-separability of the singlet; conditional states from measurement; the basis-independence of the perfect anticorrelation, which is the heart of the EPR argument and quantum key distribution.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to obtain derivations, but to probe reasoning, test the limits of the chapter's claims, and build physical intuition.

1. Ask an LLM to explain the triangle rule $J = |j_1-j_2|, \ldots, j_1+j_2$ and to verify the state-count identity $\sum_{J}(2J+1) = (2j_1+1)(2j_2+1)$ for the case $j_1=1$, $j_2=\frac{3}{2}$. Then ask it: is the triangle rule a theorem that can be proved from the ladder operator algebra, or an additional postulate? Ask for the key step in the proof.

2. Ask an LLM to explain the Condon–Shortley phase convention in concrete terms. What exactly is being fixed, and why does a phase ambiguity arise in the first place? Then ask: if you use a different sign convention, does the physics change? What quantities are convention-dependent and what quantities are invariant?

3. The chapter claims that spin-orbit coupling $\hat{L}\cdot\hat{S}$ is diagonal in the coupled basis. Ask an LLM to verify this claim for the specific case of the $2p$ hydrogen state by writing out the $6\times6$ matrix of $\hat{L}\cdot\hat{S}$ in the uncoupled basis $|m_\ell, m_s\rangle$ and showing it has off-diagonal elements, then confirming the same matrix is diagonal in the coupled $|J,M\rangle$ basis. Evaluate whether its matrix is correct.

4. Ask an LLM whether the singlet state is entangled. Ask it to define entanglement precisely and to identify whether the singlet satisfies that definition. Then push: is the triplet $|1,1\rangle = |\!\uparrow\uparrow\rangle$ entangled? What about $|1,0\rangle = (|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle)/\sqrt{2}$? Ask for a systematic criterion to determine entanglement from the form of the state.

5. Ask an LLM to explain the Wigner–Eckart theorem — the next downstream consequence of CG algebra — in terms of what it says about matrix elements of spherical tensor operators. Ask specifically: how does the Wigner–Eckart theorem generate selection rules for electromagnetic transitions (such as $\Delta\ell = \pm1$)? Evaluate whether the connection between the CG algebra of this chapter and the selection rules is made clearly.

---

## References

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Chapter 5.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. Chapter 3.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. II. Wiley. Chapter X.

Condon, E. U., & Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press. (Original source of the phase convention.)

Ewen, H. I., & Purcell, E. M. (1951). Observation of a line in the galactic radio spectrum. *Nature*, 168, 356. (First detection of the 21-cm line.)

---

## Running Project — Build the Atom

**This chapter adds:** the angular-momentum coupling that produces term symbols — couple the open-subshell electrons' orbital and spin angular momenta into total $L$, $S$, and then $J$, the $^{2S+1}L_J$ label and specifically the $J = |L-S| \dots L+S$ that Hund's third rule selects.

A configuration like $[\text{Ar}]3d^6 4s^2$ is not the end of the prediction — the atom-builder must say *which term* is the ground state: iron's $^5D_4$. That requires combining the open $3d^6$ electrons' angular momenta. This chapter supplies the coupling machinery: the triangle rule for allowed $J$, the $M = m_1 + m_2$ selection, and the $\hat J^2 = \hat L^2 + \hat S^2 + 2\hat L\cdot\hat S$ identity that makes $J$ a good quantum number. Chapter 11's Hund Rule 3 then picks $J = |L-S|$ (less than half-filled) or $L+S$ (more than half-filled).

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Coding the triangle rule and the state-count check $\sum_J(2J+1) = (2j_1+1)(2j_2+1)$ — *Why AI works here:* it is a bounded enumeration with an exact arithmetic check you can confirm by hand for $\tfrac12\otimes\tfrac12$.
- Building a microstate enumerator: all $(m_\ell, m_s)$ assignments of $k$ electrons in a subshell respecting Pauli, tracking $M_L=\sum m_\ell$ and $M_S=\sum m_s$ — *Why AI works here:* it is combinatorial bookkeeping; you verify the microstate count is $\binom{2(2\ell+1)}{k}$.

**The tell:** You are using AI well when you have an exact count to check — the dimension identity and the binomial microstate count are both verifiable without the AI.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Selecting the *ground* term from the list of allowed terms — *Why AI fails here:* that is Hund's rules (max $S$, then max $L$, then the half-filling $J$ rule), which Chapter 11 establishes; an LLM asked to "pick the ground term" may apply a half-remembered rule and return the wrong $J$ for a more-than-half-filled shell.
- Trusting an LLM's recalled term symbol for a specific element — *Why AI fails here:* term symbols are exactly the kind of fact LLMs hallucinate fluently (right format, wrong $J$); iron's $^5D_4$ must be *derived* and checked against NIST, not recalled.

**The tell:** If you cannot derive $J$ from the filling fraction without the AI, the AI did the physics that should have been yours.
**Physics-judgment connection:** this trains checking a coupling result against the state-count identity and against a cited spectroscopic value — never accepting a recalled term symbol as ground truth.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a module `coupling.py` that enumerates microstates of an open subshell and extracts the allowed terms (the raw material for Hund's rules).
**Tool:** Claude chat.
**The Prompt:**
```
I am building an atomic-structure simulator. Given an open subshell (l, number
of electrons k), I need to enumerate microstates and find the allowed
term symbols (2S+1)L_J — but NOT yet pick the ground term.

Write a Python module `coupling.py` (numpy + itertools) that:

1. triangle(j1, j2) returning the list of allowed J = |j1-j2|..j1+j2 (integer
   or half-integer steps), and assert sum(2J+1) == (2j1+1)(2j2+1).
2. microstates(l, k): enumerate all ways to place k electrons in the 2(2l+1)
   spin-orbitals of subshell l (each spin-orbital occupied 0 or 1 times, Pauli),
   returning for each microstate (M_L = sum m_l, M_S = sum m_s).
3. allowed_terms(l, k): from the microstate (M_L, M_S) table, extract the set of
   (S, L) terms present (the standard "subtract the box of microstates" method),
   and for each (S, L) list the J values from triangle(L, S).
4. __main__: for p^2 (l=1, k=2) print the allowed terms and assert the set is
   {1S, 3P, 1D}; for d^6 (l=2, k=6) print the allowed terms and confirm 5D is
   among them (this is iron's open shell).

IMPORTANT: do NOT apply Hund's rules or select a ground term — only enumerate
what terms are ALLOWED. The microstate count must equal C(2(2l+1), k).
```
**What this produces:** `coupling.py` — the term-enumeration engine feeding Hund's rules.
**How to adapt:** *Your system:* for large shells the microstate table grows; $d^6$ has $\binom{10}{6}=210$ microstates, still trivial. *ChatGPT/Gemini:* same prompt; ask it to print the $(M_L,M_S)$ table for $p^2$ to inspect. *Claude Project:* keep with the physics core — Chapter 11 layers Hund's rules on top.
**Builds on:** Chapters 6–7's orbital and spin labels (the microstates are assignments of these).  **Next:** Chapter 9 gives the hydrogenic $R_{n\ell}$ with $Z_\text{eff}$ that sets the actual energies these terms attach to.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the coupling/term-enumeration module plus tests on $p^2$ and $d^6$.
**Tool:** Claude Code.
**Skill level:** Advanced
**Setup — confirm:**
- [ ] `subshells.py`, `spin.py` present.
- [ ] `numpy`, `pytest`.
- [ ] CLAUDE.md rules from Chapters 1–7 present.
**The Task:**
```
In build-the-atom/, create coupling.py with triangle(j1, j2), microstates(l, k),
and allowed_terms(l, k).

Create test_coupling.py: (a) triangle(0.5, 0.5) == [0, 1] and the dimension
check passes; (b) the number of p^2 microstates equals C(6, 2) = 15; (c)
allowed_terms(1, 2) yields exactly {1S, 3P, 1D}; (d) allowed_terms(2, 6) (iron's
3d^6) includes the 5D term; (e) the number of d^6 microstates equals C(10,6)=210.

Run `pytest -q` and show output. Do NOT add Hund's-rule selection. Modify no
other module.
```
**Expected output:** `coupling.py`, `test_coupling.py`, passing `pytest`.
**What to inspect:** confirm $p^2 \to \{^1S, ^3P, ^1D\}$ (the textbook result); confirm the microstate counts match the binomials; confirm $^5D$ appears for $d^6$ — this is the term Hund's rules will select for iron.
**If it goes wrong:** the common failure is double-counting microstates (treating electrons as distinguishable), giving $k!$-times too many. Recovery: the microstate count must equal $\binom{2(2\ell+1)}{k}$ — assert it before extracting terms.
**CLAUDE.md / AGENTS.md note:** add — "Term *enumeration* (this module) is separate from ground-term *selection* (Hund's rules, Chapter 11). Never let the enumerator pick a ground state."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `coupling.py` term-enumeration module from R3/R4.
**Validation type:** Code / Structured data
**Risk level:** Medium–High — term enumeration is where LLMs most readily hallucinate; a wrong term set silently breaks the final $^5D_4$ prediction.
**Setup:** use your R3/R4 artifact.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Addition of Angular Momenta
□ Correctness: for p^2, are the allowed terms exactly {1S, 3P, 1D}?
□ Completeness: does the d^6 term set include 5D (iron's eventual ground term)?
□ Scope: did it stay OUT of Hund's-rule selection (enumerate only)?
□ Physics criterion 1: does sum(2J+1) == (2j1+1)(2j2+1) for the triangle rule?
□ Physics criterion 2: does the microstate count equal C(2(2l+1), k)?
□ Failure-mode check: any of —
  - fluent but wrong (recalls a term set instead of deriving it)
  - electrons treated as distinguishable (microstate count too high by k!)
  - M = m1 + m2 selection rule violated
  - half-integer/integer confusion in triangle() for odd electron counts
```
**What to do with findings:** pass → use it, noting the $p^2\to\{^1S,^3P,^1D\}$ match is what made it trustworthy; one fail → fix the Pauli/distinguishability handling and re-run; multiple fails / cannot-determine → derive the $p^2$ terms by hand and rebuild the enumerator against that anchor.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI built the microstate enumerator and term extractor, which I checked against the known $p^2 \to \{^1S,^3P,^1D\}$ result.
> *2:* The AI could not be trusted to *select* the ground term — that is Hund's rules — and I kept that logic out of its hands and out of this module.
**Physics-judgment connection:** validating a coupling enumeration against the exact dimension and microstate-count identities, and refusing recalled term symbols in favor of derived-and-cited ones.
