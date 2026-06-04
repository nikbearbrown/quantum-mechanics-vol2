# Chapter 3 — Commutators, Compatibility, and the Generalized Uncertainty Principle

## TL;DR

- The commutator $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ measures the algebraic incompatibility of two observables.
- Commuting operators ($[\hat{A},\hat{B}] = 0$) share a simultaneous eigenbasis; you can assign both observables definite values at once.
- The canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$ is a theorem, derivable in three lines from the operator representations.
- Robertson (1929) proved the generalized uncertainty principle $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ from Cauchy-Schwarz alone — no microscope, no disturbance.
- Substituting $[\hat{x}, \hat{p}] = i\hbar$ recovers $\sigma_x\sigma_p \geq \hbar/2$ as a corollary. The bound is a property of the *state*, not the apparatus.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Define and compute** commutators of operators — including by applying them to a test function — and interpret the result as a measure of incompatibility. *(Remember / Understand)*
2. **Derive** $[\hat{x}, \hat{p}] = i\hbar$ from the position and momentum operator representations, showing each step of the product rule. *(Apply)*
3. **Prove** the Robertson uncertainty principle $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ from the Cauchy-Schwarz inequality, naming each step. *(Analyze)*
4. **Apply** Robertson to a chosen operator pair — including spin components — to derive and numerically evaluate an uncertainty bound. *(Apply)*
5. **Explain** in operational terms why the uncertainty bound is a property of the state, not a consequence of measurement disturbance, and identify at least one common misconception it refutes. *(Evaluate)*

---

## Opening Scene

Imagine measuring the position of an electron to within a nanometer — a genuinely fine measurement by any laboratory standard. You then measure its momentum. Heisenberg's 1927 story says the photon you used to pin down the position kicked the electron and scrambled its momentum. That story is vivid, memorable, and — as a derivation of the uncertainty principle — wrong.

Here is the experiment that refutes it. Prepare a million electrons in *exactly the same state* $|\psi\rangle$. Measure position on 500,000 of them. Measure momentum on the other 500,000. No electron is measured twice. No photon kicks anything. Compute the standard deviations $\sigma_x$ and $\sigma_p$ from the two histograms. Their product satisfies $\sigma_x\sigma_p \geq \hbar/2$.

The bound is there before any measurement begins. It is a property of the state $|\psi\rangle$. The statement "you cannot simultaneously measure position and momentum precisely" is colloquially true but causally backwards. The correct statement is: *no quantum state has $\sigma_x = 0$ and $\sigma_p = 0$ simultaneously*. The algebra of operators forces this. Robertson proved it in 1929 — not from any model of measurement, but from a two-line application of the Cauchy-Schwarz inequality to the commutator $[\hat{x}, \hat{p}] = i\hbar$.

That commutator is where the chapter starts.

---

## Core Development

### What a commutator measures

The **commutator** of two operators $\hat{A}$ and $\hat{B}$ is

$$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}.$$

When $[\hat{A}, \hat{B}] = 0$ we call the operators **compatible**. When $[\hat{A}, \hat{B}] \neq 0$ they are **incompatible**. The names are not decorative.

**Theorem.** *Two Hermitian operators are compatible if and only if they share a complete orthonormal eigenbasis.*

*Proof sketch (non-degenerate case).* Suppose $[\hat{A}, \hat{B}] = 0$ and $\hat{A}|a\rangle = a|a\rangle$. Apply $\hat{B}$ on the left of both sides:

$$\hat{B}\hat{A}|a\rangle = a\hat{B}|a\rangle.$$

But $\hat{B}\hat{A} = \hat{A}\hat{B}$ (they commute), so $\hat{A}(\hat{B}|a\rangle) = a(\hat{B}|a\rangle)$. The vector $\hat{B}|a\rangle$ is itself an eigenvector of $\hat{A}$ with eigenvalue $a$. If the eigenvalue is non-degenerate, the eigenspace is one-dimensional, so $\hat{B}|a\rangle \propto |a\rangle$ — meaning $|a\rangle$ is simultaneously an eigenvector of $\hat{B}$. For degenerate eigenvalues, $\hat{B}$ maps the degenerate subspace into itself; by the spectral theorem for Hermitian operators, $\hat{B}$ can then be diagonalized within that subspace by Gram-Schmidt. In either case, a simultaneous eigenbasis exists. $\square$

The physical consequence: in a state $|a,b\rangle$ that is simultaneously an eigenstate of $\hat{A}$ (eigenvalue $a$) and $\hat{B}$ (eigenvalue $b$), both observables take definite values. The **complete set of commuting observables (CSCO)** is the maximal collection of mutually commuting Hermitian operators whose joint eigenvalues uniquely label every state. For the hydrogen atom (without spin), $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ is a CSCO: every eigenstate is uniquely labeled by the triple $(n, \ell, m)$ precisely because these three operators mutually commute.

Conversely: if $[\hat{A}, \hat{B}] \neq 0$, no state is simultaneously an eigenstate of both. For any state $|\psi\rangle$ that is sharp in $A$ (meaning $\sigma_A = 0$, i.e., $|\psi\rangle$ is an eigenstate of $\hat{A}$), the spread $\sigma_B > 0$ necessarily. The Robertson theorem will make this quantitative.

---

### The canonical commutation relation

The single most important commutator in quantum mechanics is $[\hat{x}, \hat{p}]$. Derive it by applying both operators in both orders to a test function $\psi(x)$, keeping every step of the product rule visible.

$$[\hat{x}, \hat{p}]\,\psi(x) = \hat{x}\bigl(-i\hbar\,\partial_x\psi\bigr) - (-i\hbar\,\partial_x)(x\psi).$$

The first term: $\hat{x}$ multiplies by $x$, giving $-i\hbar\, x\,\partial_x\psi$.

The second term: $\partial_x$ acts on the product $x\psi$ by the product rule,

$$\partial_x(x\psi) = \psi + x\,\partial_x\psi,$$

so the second term is $-(-i\hbar)(\psi + x\,\partial_x\psi) = i\hbar\,\psi + i\hbar\, x\,\partial_x\psi$.

Sum:

$$[\hat{x}, \hat{p}]\,\psi(x) = -i\hbar\, x\,\partial_x\psi + i\hbar\,\psi + i\hbar\, x\,\partial_x\psi = i\hbar\,\psi.$$

Since this holds for every $\psi$:

$$\boxed{[\hat{x}, \hat{p}] = i\hbar.}$$

This is the **canonical commutation relation**. It follows from the operator representations $\hat{x} = $ multiplication by $x$ and $\hat{p} = -i\hbar\,\partial_x$, which are themselves consequences of requiring that $\hat{p}$ generates translations and has real eigenvalues (see Chapter 2). Every result about position-momentum incompatibility — including the uncertainty principle — is a downstream consequence of this single equation.

Two rapid extensions worth noting. First, in three dimensions: $[\hat{x}_i, \hat{p}_j] = i\hbar\,\delta_{ij}$, and coordinates along different axes commute: $[\hat{x}_i, \hat{x}_j] = 0$, $[\hat{p}_i, \hat{p}_j] = 0$. Second, a quick check of $[\hat{x}^2, \hat{p}]$ by the same method gives $2i\hbar\hat{x}$ — the quantum analog of the classical identity $\{x^2, p\}_\text{Poisson} = 2x$. The pattern $[\hat{x}^n, \hat{p}] = i\hbar\,n\hat{x}^{n-1}$ holds generally, hinting at the Dirac quantization rule: replace the classical Poisson bracket $\{f, g\}$ with $[\hat{f}, \hat{g}]/i\hbar$.

---

### The Robertson uncertainty principle

**Theorem (Robertson, 1929).** *For any two Hermitian operators $\hat{A}$, $\hat{B}$ and any normalized state $|\psi\rangle$,*

$$\sigma_A\,\sigma_B \geq \frac{1}{2}\bigl|\langle[\hat{A}, \hat{B}]\rangle\bigr|,$$

*where $\sigma_A^2 = \langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2$ is the variance of $A$-outcomes on repeated measurements of identically prepared copies of $|\psi\rangle$.*

**Proof.** The derivation has four named steps.

**Step 1 — shift to zero mean.** Define $\hat{A}' = \hat{A} - \langle\hat{A}\rangle$ and $\hat{B}' = \hat{B} - \langle\hat{B}\rangle$. Then $\sigma_A^2 = \langle\hat{A}'^2\rangle = \|\hat{A}'|\psi\rangle\|^2$ and $\sigma_B^2 = \|\hat{B}'|\psi\rangle\|^2$. (Shifting by a constant does not change commutators: $[\hat{A}', \hat{B}'] = [\hat{A}, \hat{B}]$.)

**Step 2 — Cauchy-Schwarz.** For any two vectors $|u\rangle = \hat{A}'|\psi\rangle$ and $|v\rangle = \hat{B}'|\psi\rangle$,

$$\|u\|^2\|v\|^2 \geq |\langle u|v\rangle|^2,$$

so $\sigma_A^2\,\sigma_B^2 \geq |\langle\psi|\hat{A}'\hat{B}'|\psi\rangle|^2$.

**Step 3 — decompose into symmetric and antisymmetric parts.**

$$\hat{A}'\hat{B}' = \tfrac{1}{2}\{\hat{A}', \hat{B}'\} + \tfrac{1}{2}[\hat{A}', \hat{B}'].$$

The anticommutator $\tfrac{1}{2}\{\hat{A}', \hat{B}'\}$ is Hermitian (its expectation value is real). The commutator $\tfrac{1}{2}[\hat{A}', \hat{B}'] = \tfrac{1}{2}[\hat{A}, \hat{B}]$ is *anti*-Hermitian when $\hat{A}$ and $\hat{B}$ are Hermitian, so its expectation value is purely imaginary. Their squared moduli add without cross-terms:

$$|\langle\hat{A}'\hat{B}'\rangle|^2 = \tfrac{1}{4}\langle\{\hat{A}', \hat{B}'\}\rangle^2 + \tfrac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2.$$

**Step 4 — drop the non-negative term.** The anticommutator term $\tfrac{1}{4}\langle\{\hat{A}', \hat{B}'\}\rangle^2 \geq 0$, so dropping it only weakens the bound:

$$\sigma_A^2\,\sigma_B^2 \geq \tfrac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2.$$

Take the positive square root:

$$\sigma_A\,\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|. \quad\square$$

**Corollary — the Heisenberg uncertainty relation.** Set $\hat{A} = \hat{x}$, $\hat{B} = \hat{p}$. Then $\langle[\hat{x}, \hat{p}]\rangle = \langle i\hbar\rangle = i\hbar$ (a c-number, independent of the state). Therefore:

$$\sigma_x\,\sigma_p \geq \frac{\hbar}{2}.$$

This bound is *state-independent*: it holds for every $|\psi\rangle$ without exception, because $[\hat{x}, \hat{p}] = i\hbar$ is an operator identity rather than an expectation value that could vanish for special states.

**When the bound is state-dependent.** For operators whose commutator is itself an operator (not a c-number), the right-hand side depends on the state through $|\langle[\hat{A},\hat{B}]\rangle|$. The prime example: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$, so

$$\sigma_{S_x}\,\sigma_{S_z} \geq \tfrac{\hbar}{2}|\langle\hat{S}_y\rangle|.$$

At the north pole of the Bloch sphere ($|\!\uparrow\rangle$, a $\hat{S}_z$ eigenstate): $\langle\hat{S}_y\rangle = 0$, the bound is zero, and there is no algebraic obstruction to one of the spreads being zero (indeed $\sigma_{S_z} = 0$). At the equatorial $\hat{S}_y$ eigenstate: $\langle\hat{S}_y\rangle = \hbar/2$, the bound becomes $\hbar^2/4$, and both $\sigma_{S_x}$ and $\sigma_{S_z}$ are forced to be $\hbar/2$, so the product saturates the bound exactly.

A zero Robertson bound does not guarantee zero spread — it only means the inequality is not binding. Students who encounter a state with $\langle[\hat{A},\hat{B}]\rangle = 0$ and conclude "both can be sharp simultaneously" are making the converse error.

**The operational meaning, stated plainly.** Take $N$ independently prepared copies of $|\psi\rangle$. Measure $\hat{A}$ on $N/2$ copies and $\hat{B}$ on the remaining $N/2$. No copy is measured twice. Compute sample standard deviations. Their product obeys $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$. The bound is already there, enforced by the algebra of operators in the state preparation, before any measuring device turns on.

---

### Compatible observables: a worked diagnostic

A rapid test of compatibility: $[\hat{L}^2, \hat{L}_z]$. Compute:

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2,\, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z].$$

Using the identity $[\hat{A}^2, \hat{B}] = \hat{A}[\hat{A},\hat{B}] + [\hat{A},\hat{B}]\hat{A}$ and the angular momentum commutators $[\hat{L}_x, \hat{L}_z] = -i\hbar\hat{L}_y$, $[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$:

$$[\hat{L}_x^2, \hat{L}_z] = -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x), \qquad [\hat{L}_y^2, \hat{L}_z] = i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x).$$

They cancel: $[\hat{L}^2, \hat{L}_z] = 0$. The operators $\hat{L}^2$ and $\hat{L}_z$ are compatible — they share a simultaneous eigenbasis $|{\ell, m}\rangle$, the spherical harmonics. This is why both $\ell$ and $m$ are simultaneously good quantum numbers: not by assumption, but by algebraic necessity.

---

## Worked Example: Uncertainty Bound for Spin-$\tfrac{1}{2}$ in an $\hat{x}$ Eigenstate

**The lesson.** Derive the Robertson bound for $\hat{S}_x$ and $\hat{S}_z$ in the state $|\!\uparrow_x\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$, and verify it is saturated.

**Step 1 — commutator.** Using the Pauli algebra $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$ and $\hat{S}_i = (\hbar/2)\sigma_i$:

$$[\hat{S}_x, \hat{S}_z] = \frac{\hbar^2}{4}[\sigma_x, \sigma_z] = \frac{\hbar^2}{4}(-2i\sigma_y) = -i\hbar\hat{S}_y.$$

**Step 2 — Robertson bound.** $\sigma_{S_x}\sigma_{S_z} \geq \tfrac{1}{2}|\langle[\hat{S}_x, \hat{S}_z]\rangle| = \tfrac{\hbar}{2}|\langle\hat{S}_y\rangle|$.

**Step 3 — evaluate $\langle\hat{S}_y\rangle$ in $|\!\uparrow_x\rangle$.** In matrix form, $|\!\uparrow_x\rangle = \tfrac{1}{\sqrt{2}}\bigl(\begin{smallmatrix}1\\1\end{smallmatrix}\bigr)$:

$$\langle\hat{S}_y\rangle = \frac{\hbar}{2}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\end{pmatrix}\begin{pmatrix}0 & -i\\i & 0\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{\hbar}{4}\begin{pmatrix}1 & 1\end{pmatrix}\begin{pmatrix}-i\\i\end{pmatrix} = \frac{\hbar}{4}(-i + i) = 0.$$

The Robertson bound is $\tfrac{\hbar}{2}\cdot 0 = 0$. The bound is trivially satisfied and places no constraint.

**Step 4 — compute the actual spreads.** $|\!\uparrow_x\rangle$ is an eigenstate of $\hat{S}_x$ with eigenvalue $+\hbar/2$, so $\sigma_{S_x} = 0$.

For $\hat{S}_z$: the state is the equal superposition $(|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. By the Born rule, $P(S_z = +\hbar/2) = P(S_z = -\hbar/2) = 1/2$. So $\langle\hat{S}_z\rangle = 0$ and $\langle\hat{S}_z^2\rangle = \hbar^2/4$, giving $\sigma_{S_z} = \hbar/2$.

Product: $\sigma_{S_x}\cdot\sigma_{S_z} = 0 \cdot \hbar/2 = 0$. Consistent with the bound $\geq 0$. ✓

**The limit — when does saturation reveal something?** Repeat for the state $|+y\rangle = (|\!\uparrow\rangle + i|\!\downarrow\rangle)/\sqrt{2}$, the $\hat{S}_y$ eigenstate:

$$\langle\hat{S}_y\rangle = +\frac{\hbar}{2}, \quad \text{so the bound becomes } \sigma_{S_x}\sigma_{S_z} \geq \frac{\hbar^2}{4}.$$

In $|+y\rangle$: $\langle\hat{S}_x\rangle = \langle\hat{S}_z\rangle = 0$, and $\langle\hat{S}_x^2\rangle = \langle\hat{S}_z^2\rangle = \hbar^2/4$ (since $\sigma_x^2 = I$), so $\sigma_{S_x} = \sigma_{S_z} = \hbar/2$ and $\sigma_{S_x}\sigma_{S_z} = \hbar^2/4$. The bound is saturated exactly.

**Reading the saturation condition.** The Robertson bound is saturated when the anticommutator term dropped in Step 4 of the proof equals zero: $\langle\{\hat{A}', \hat{B}'\}\rangle = 0$. For the Pauli matrices, this is satisfied exactly at the $\hat{S}_y$ eigenstates. Geometrically on the Bloch sphere: the state that is most constrained in the $y$-direction is maximally uncertain in both $x$ and $z$, and that is precisely the state that saturates the Robertson bound for those two observables.

---

## Common Misconceptions

**"The uncertainty principle says measurement disturbs the system."**
This is Heisenberg's microscope story, not Robertson's theorem. The theorem says nothing about what happens during or after a measurement. It constrains the standard deviations of outcomes on independently prepared copies of a state. No copy needs to be disturbed for the bound to hold. The disturbance interpretation is intuitive but causally backwards.

**"When the Robertson bound is zero, both observables can be simultaneously sharp."**
The Robertson bound is a lower bound on $\sigma_A\sigma_B$. A zero bound ($\langle[\hat{A},\hat{B}]\rangle = 0$ for a particular state) means the bound does not forbid small products — it does not guarantee that any product is zero. The state $(|+y\rangle + |-y\rangle)/\sqrt{2}$ has $\langle\hat{S}_y\rangle = 0$, giving a zero bound for $\hat{S}_x$ and $\hat{S}_z$; yet both $\sigma_{S_x}$ and $\sigma_{S_z}$ are nonzero.

**"$[\hat{x}, \hat{p}] = i\hbar$ is just a definition or a postulate."**
It is neither. It is a theorem: a consequence of the operator representations $\hat{x} = $ multiplication by $x$ and $\hat{p} = -i\hbar\partial_x$, which are themselves derived from requiring that $\hat{p}$ generates translations and produces real eigenvalues. The three-line test-function derivation in this chapter shows this explicitly.

**"Commuting operators are always proportional or of the same 'type'."**
This is false. $\hat{H}$ and $\hat{L}^2$ for the hydrogen atom commute even though one involves kinetic plus Coulomb energy and the other involves angular derivatives only. Commutativity is an algebraic property of the operator structure, not a consequence of physical similarity.

**"The energy-time uncertainty relation $\Delta E\,\Delta t \geq \hbar/2$ follows from Robertson."**
It does not. Time $t$ is a parameter in non-relativistic quantum mechanics, not a Hermitian operator. The energy-time relation has a different meaning: $\Delta t$ is the time for the state to change appreciably, and the relation follows from the time-evolution formula and the energy spread of the state. It looks like Robertson but is derived differently. Flag it when it comes up — the apparent similarity has misled many textbooks.

---

## Exercises

### Warm-up

**3.1** Derive $[\hat{x}, \hat{p}] = i\hbar$ by applying both operators to a test function $\psi(x)$. Show every step of the product rule explicitly. At which step does the constant $i\hbar$ emerge? What would the commutator be if $\hat{p}$ were defined as $\hbar\partial_x$ (no factor of $-i$), and what would be wrong with that definition? *(Tests: can execute the canonical commutation derivation; understands the role of the imaginary unit)*

**3.2** Verify by direct matrix multiplication that $[\sigma_x, \sigma_z] = -2i\sigma_y$ using $\sigma_x = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, $\sigma_z = \bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$, $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Common error: writing $\sigma_y$ with the wrong sign. Verify your $\sigma_y$ is Hermitian ($\sigma_y^\dagger = \sigma_y$) before proceeding. *(Tests: can execute a matrix commutator; checks the canonical sign trap)*

**3.3** The harmonic oscillator Hamiltonian is $\hat{H} = \hat{p}^2/2m + m\omega^2\hat{x}^2/2$. Compute $[\hat{H}, \hat{x}]$ using $[\hat{p}^2, \hat{x}] = \hat{p}[\hat{p}, \hat{x}] + [\hat{p}, \hat{x}]\hat{p}$ and $[\hat{p}, \hat{x}] = -i\hbar$. State what the result implies about $\hat{x}$ as a constant of motion. *(Tests: can compute commutators of composite operators; connects commutator to dynamics)*

### Application

**3.4** For each of the following pairs, state whether they are compatible or incompatible, and justify with the commutator: (a) $\hat{L}^2$ and $\hat{L}_z$; (b) $\hat{L}_x$ and $\hat{L}_y$; (c) $\hat{H}$ and $\hat{L}^2$ for the hydrogen atom. For each incompatible pair, write down the Robertson bound and identify which quantity on the right-hand side determines whether the bound is binding for a particular state. *(Tests: can identify compatible vs. incompatible pairs; can apply Robertson without computing every step from scratch)*

**3.5** Apply the Robertson uncertainty principle to $\hat{A} = \hat{S}_x$ and $\hat{B} = \hat{S}_y$ for a general qubit state with Bloch vector $(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$. (a) Compute $[\hat{S}_x, \hat{S}_y]$. (b) Evaluate the Robertson bound $\tfrac{\hbar}{2}|\langle\hat{S}_z\rangle| = \tfrac{\hbar^2}{4}|\cos\theta|$. (c) Find the Bloch-sphere locus where the bound is maximized. (d) Find the locus where the bound is zero. *(Tests: can apply Robertson to spin; understands the state-dependence of the bound geometrically)*

**3.6** Verify the Cauchy-Schwarz inequality $\|u\|^2\|v\|^2 \geq |\langle u|v\rangle|^2$ for $|u\rangle = \hat{A}'|\psi\rangle$ and $|v\rangle = \hat{B}'|\psi\rangle$ directly by expanding $\|\hat{A}'|\psi\rangle - \lambda\hat{B}'|\psi\rangle\|^2 \geq 0$ for all complex $\lambda$, then choosing $\lambda = \langle v|u\rangle/\|v\|^2$ optimally. (This is the only assumption the Robertson proof makes.) *(Tests: can derive Cauchy-Schwarz from the positivity of norms; strengthens the proof structure)*

### Apply+

**3.7** (Robertson for angular momentum) The commutators of orbital angular momentum are $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$, $[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$, $[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$. (a) Write the Robertson bound for $\hat{L}_x$ and $\hat{L}_y$ in terms of $\langle\hat{L}_z\rangle$. (b) For the state $|{\ell = 1, m = 1}\rangle$: compute $\langle\hat{L}_z\rangle = \hbar$, so the bound is $\sigma_{L_x}\sigma_{L_y} \geq \hbar^2/2$. Verify this is consistent with $\sigma_{L_x}^2 = \sigma_{L_y}^2 = \langle\hat{L}_x^2\rangle = \hbar^2\ell(\ell+1)/2 - \hbar^2 m^2/2 = \hbar^2/2$ (using the fact that in $|1,1\rangle$, $\langle\hat{L}_x\rangle = \langle\hat{L}_y\rangle = 0$). (c) Is the bound saturated? *(Tests: can apply Robertson to orbital angular momentum; connects to the angular momentum eigenvalue structure from Chapter 6)*

### Produce

**3.8** The CSCO (complete set of commuting observables) for the hydrogen atom without spin is $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$. (a) Verify that $[\hat{L}^2, \hat{L}_z] = 0$ using the angular momentum commutation relations (sketch the argument — full algebraic verification not required). (b) Explain in words why the CSCO concept is the reason three quantum numbers $(n, \ell, m)$ simultaneously label each energy eigenstate. (c) Suppose you add the spin operator $\hat{S}_z$ to the list: is $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$ still a CSCO? Justify. *(Tests: produces an explanation connecting abstract commutativity to quantum number labeling — a synthesis, not just calculation)*

---

## Still Puzzling

**What saturates the Robertson bound?** The bound $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ is saturated when the anticommutator term $\langle\{\hat{A}', \hat{B}'\}\rangle = 0$. For Gaussian wave packets in position space, this is satisfied by coherent states — minimum-uncertainty states for $\hat{x}$ and $\hat{p}$ where $\sigma_x\sigma_p = \hbar/2$ exactly. Finding the minimum-uncertainty states for arbitrary operator pairs is a research-level problem in some generality.

**Can the uncertainty principle be tightened?** Yes. The Robertson bound drops the anticommutator term. The **Schrödinger uncertainty relation** (1930) retains it:

$$\sigma_A^2\sigma_B^2 \geq \tfrac{1}{4}|\langle\{\hat{A}', \hat{B}'\}\rangle|^2 + \tfrac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2.$$

The tighter bound reduces to Robertson's when $\langle\{\hat{A}', \hat{B}'\}\rangle = 0$. Beyond this, **entropic uncertainty relations** (Maassen and Uffink, 1988) replace the standard deviation with Shannon entropy: $H(A) + H(B) \geq \log(1/c)$ where $c = \max_{i,j}|\langle a_i|b_j\rangle|^2$. These are tighter for discrete observables and are actively used in quantum cryptography [verify].

**Is the disturbance interpretation completely wrong?** No — it is just not what the Robertson theorem says. Ozawa (2003) and Busch, Lahti, and Werner (2013) derived rigorous *measurement-disturbance* relations that formalize Heisenberg's intuition. These are distinct inequalities from Robertson's preparation uncertainty. The field is active: experiments have tested Ozawa's formulation using neutron spin systems (Erhart et al., 2012) and photons [verify].

---

## The +1 — Simulation Exercise: Robertson Bound Explorer

The chapter's deliverable is `04-commutator-explorer.html`: an interactive D3 visualization that displays the Robertson bound $\tfrac{\hbar}{2}|\langle\hat{S}_y\rangle|$ for $\hat{S}_x$ and $\hat{S}_z$ as a function of the qubit state on the Bloch sphere, alongside the actual product $\sigma_{S_x}\sigma_{S_z}$, so the student can watch the bound rise, fall, and be saturated.

### Part 1 — CLAUDE.md extension

Open your project's CLAUDE.md and append:

```
## Chapter 3 — Commutator Explorer Rules

- Single HTML file, D3 v7 from CDN, SVG canvas only.
- Two coupled panels side by side:
  (1) Bloch sphere (left, ~400×400 px): draggable state arrow at (θ, φ).
      Draw latitude and longitude guide lines. Color the arrow by the
      value of |⟨S_y⟩| / (ℏ/2), from blue (0) to red (1).
  (2) Bar chart (right, ~400×300 px): four bars in two groups:
      Group A: σ_{S_x}, σ_{S_z} (actual standard deviations)
      Group B: Robertson bound ℏ/2 |⟨S_y⟩|, product σ_{S_x}·σ_{S_z}
      Always show product ≥ bound numerically with a label "ratio = X.XX".
- Numeric readouts: θ (degrees), φ (degrees), ⟨S_x⟩, ⟨S_y⟩, ⟨S_z⟩,
  σ_{S_x}, σ_{S_z}, product, Robertson bound.
- Physics must be correct: in ℏ=1 units,
    ⟨S_y⟩ = sin(θ)sin(φ)
    σ_{S_x}^2 = 1/4 - sin²(θ)cos²(φ)/4    [since ⟨S_x⟩ = sin θ cos φ / 2]
    σ_{S_z}^2 = 1/4 - cos²(θ)/4           [since ⟨S_z⟩ = cos θ / 2]
    Robertson bound = |sin(θ)sin(φ)| / 4
- All redraws through a single redraw() function.
```

### Part 2 — The simulation prompt

```
Build me a D3 v7 Commutator Robertson-Bound Explorer following CLAUDE.md.

SHOW.
The qubit state is at Bloch angles (θ, φ). For operators Ŝ_x and Ŝ_z:
  ⟨Ŝ_y⟩ = (ℏ/2) sin θ sin φ
  Robertson bound = (ℏ/2)|⟨Ŝ_y⟩| = ℏ²/4 · |sin θ sin φ|
  σ_{S_x}² = (ℏ/2)² (1 - sin²θ cos²φ)
  σ_{S_z}² = (ℏ/2)² (1 - cos²θ)
  product σ_{S_x}·σ_{S_z} ≥ Robertson bound at all points on the sphere.

SAY.
Produce a single file 04-commutator-explorer.html.
Left panel: Bloch sphere (isometric projection), draggable arrow.
Right panel: grouped bar chart with four quantities (σ_x, σ_z, product,
  bound), updating in real time as the user drags.
  Label: "Ratio = (σ_{S_x}·σ_{S_z}) / Robertson bound". Must be ≥ 1.
  Color the ratio label red when ratio < 1.001 (bound nearly saturated),
  green otherwise.
Bottom strip: numeric table of all expectation values and standard deviations.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS. No three.js.
- Use ℏ = 1 throughout; label axes in units of ℏ.
- All physics computed from (θ, φ) analytically — no numeric integration.
- Verify at startup: at θ=π/2, φ=π/2 (+y eigenstate),
    σ_{S_x} = σ_{S_z} = 1/2,
    Robertson bound = 1/4, ratio = 1.00 (saturated).
  At θ=0 (north pole),
    σ_{S_z} = 0, Robertson bound = 0, ratio = undefined (display "N/A").

VERIFY. Give three checks:
(a) North pole (θ=0): σ_{S_z} = 0, product = 0, bound = 0.
(b) +y eigenstate (θ=π/2, φ=π/2): ratio = 1.00 (saturated).
(c) +x eigenstate (θ=π/2, φ=0): σ_{S_x} = 0, product = 0, bound = 0.

List failure modes:
  - sign error in ⟨S_y⟩ (check (b) catches it)
  - missing sin factor in Robertson bound
  - σ² formula incorrect (verify positivity for all θ, φ)
  - ratio reported as < 1 (impossible — signals a physics error)
```

### Part 3 — Exploration tasks

**Saturate the bound.** Drag the state to $\theta = \pi/2$, $\phi = \pi/2$ (the $\hat{S}_y$ eigenstate). Confirm the ratio reads 1.00. Now drag slowly along the equator: the bound rises and falls as $|\sin\phi|$, reaching zero at $\phi = 0$ and $\phi = \pi$ (the $\hat{S}_x$ eigenstates).

**Zero bound, nonzero spread.** Drag to $\phi = 0$ (the $\hat{S}_x$ eigenstate). Confirm $\sigma_{S_x} = 0$ and the Robertson bound equals zero. Note that $\sigma_{S_z} = 1/2$ — the bound is zero, but one spread is decidedly nonzero. This is the counterexample to "zero bound means both sharp."

**State-independence of $\sigma_x\sigma_p$.** Change the operators to $\hat{x}$ and $\hat{p}$ (a conceptual addition to the prompt). The Robertson bound $\hbar/2$ is state-independent because $[\hat{x},\hat{p}]$ is a c-number. Watch the bar chart: the bound stays at $1/2$ (in $\hbar = 1$ units) for every state.

**Drag along a latitude circle.** Fix $\theta = \pi/3$ and rotate $\phi$ from $0$ to $2\pi$. The bound $|\sin\theta\sin\phi|$ oscillates between $0$ and $|\sin(\pi/3)| = \sqrt{3}/2$. The product $\sigma_{S_x}\sigma_{S_z}$ follows above it, touching the bound only at $\phi = \pi/2$ and $3\pi/2$.

---

## References

Robertson, H. P. (1929). The uncertainty principle. *Physical Review*, **34**, 163. https://doi.org/10.1103/PhysRev.34.163 — the original one-page proof. Readable by an undergraduate with one hour of effort. [verify: open access via APS]

Kennard, E. H. (1927). Zur Quantenmechanik einfacher Bewegungstypen. *Zeitschrift für Physik*, **44**, 326. https://doi.org/10.1007/BF01391200 — first proof of $\sigma_x\sigma_p \geq \hbar/2$, two years before Robertson's general theorem. [verify]

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §3.5: the generalized uncertainty principle; the Schwarz-inequality derivation; the $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$ spin example with explicit state-dependent bound.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.4: compatible observables, the CSCO concept, and the tighter Schrödinger uncertainty relation retaining the anticommutator term.

Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §3.5: elementary undergraduate treatment with worked examples; the "no copy is measured twice" operational language.

Maassen, H., & Uffink, J. B. M. (1988). Generalized entropic uncertainty relations. *Physical Review Letters*, **60**, 1103. https://doi.org/10.1103/PhysRevLett.60.1103 — entropic uncertainty relations, tighter than Robertson for discrete observables. [verify]

Coles, P. J., Berta, M., Tomamichel, M., & Wehner, S. (2017). Entropic uncertainty relations and their applications. *Reviews of Modern Physics*, **89**, 015002. https://doi.org/10.1103/RevModPhys.89.015002 — comprehensive review accessible to advanced undergraduates. [verify: open access on arXiv:1511.04857]

Ozawa, M. (2003). Universally valid reformulation of the Heisenberg uncertainty principle. *Physical Review A*, **67**, 042105. https://doi.org/10.1103/PhysRevA.67.042105 — rigorous measurement-disturbance relations, distinct from Robertson's preparation uncertainty. [verify]

Busch, P., Lahti, P., & Werner, R. F. (2013). Proof of Heisenberg's error-disturbance relation. *Physical Review Letters*, **111**, 160405. https://doi.org/10.1103/PhysRevLett.111.160405 [verify]
