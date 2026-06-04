# Chapter 6 — Angular Momentum

## TL;DR

The entire spectrum of angular momentum — eigenvalues $\hbar^2\ell(\ell+1)$ for $\hat{L}^2$ and $m\hbar$ for $\hat{L}_z$, with $m = -\ell, -\ell+1, \ldots, \ell$ — follows from three commutation relations and a non-negativity argument. No differential equation needed. The raising and lowering operators $\hat{L}_\pm$ step between states within a fixed $\ell$ subspace; their termination forces the eigenvalue structure. The same algebra works for spin-1/2 (half-integer $\ell$) because nothing in the derivation requires the angular momentum to live in position space.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember:** State the commutation relations $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ and $[\hat{L}^2, \hat{L}_i] = 0$, and define the raising and lowering operators $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$. *(Bloom: Remember)*
2. **Understand:** Explain why $\hat{L}^2$ and $\hat{L}_z$ can be simultaneously diagonalized, while $\hat{L}_x$ and $\hat{L}_y$ cannot simultaneously have definite values. *(Bloom: Understand)*
3. **Apply:** Use the ladder operators and the termination condition to derive the eigenvalue spectrum $\hbar^2\ell(\ell+1)$ and $m\hbar$ without solving any differential equation. *(Bloom: Apply)*
4. **Apply:** Compute the action of $\hat{L}_\pm$ on a state $|\ell, m\rangle$ using the normalization formula, and construct the matrix representation of $\hat{L}_z$, $\hat{L}_+$, $\hat{L}_-$ for $\ell = 1$. *(Bloom: Apply)*
5. **Evaluate:** Connect the algebraic spectrum back to the spherical harmonics of Chapter 5, and articulate why the algebra allows half-integer $\ell$ while the single-valuedness constraint on the sphere restricts orbital angular momentum to integers. *(Bloom: Evaluate)*

---

## Scene Opening

You built the spherical harmonics in Chapter 5 by solving differential equations — the associated Legendre equation, the azimuthal equation, regularity conditions at the poles. It works, and it gives you the explicit wave functions. But it is, in a sense, more than you need. To find out what values $L^2$ and $L_z$ can take, you do not need to solve any differential equation at all.

Here is the claim: the entire eigenvalue spectrum of angular momentum follows from three lines of operator algebra and one inequality. The values $\hbar^2\ell(\ell+1)$ and $m\hbar$ are not consequences of the specific geometry of the sphere or the specific form of the Legendre equation. They are consequences of the commutation relations

$$[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z, \qquad [\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x, \qquad [\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y,$$

and nothing else. Anyone who writes down an object — any object — satisfying these three relations must get the same spectrum. The harmonic oscillator used the same logic in Chapter 3: the spectrum of $\hat{N}$ followed from $[\hat{a}, \hat{a}^\dagger] = 1$ and non-negativity, without solving the Hermite equation. Angular momentum is the same argument in three dimensions.

The payoff of doing it this way is immediate: the algebra allows $\ell$ to be a half-integer, not just an integer. Orbital angular momentum is restricted to integers by the additional requirement that the wave function be single-valued on the sphere. Spin angular momentum has no such wave function — it lives in an abstract Hilbert space with no position-space analog — and the half-integer case is realized. Chapter 8 is spin. This chapter is the algebra that makes it possible.

---

## Core Development

### The Commutation Relations from First Principles

The classical angular momentum $\vec{L} = \vec{r}\times\vec{p}$ becomes, in quantum mechanics, $\hat{\vec{L}} = \hat{\vec{r}}\times\hat{\vec{p}}$, with components:

$$\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \qquad \hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z, \qquad \hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x.$$

The fundamental canonical commutation relations are $[\hat{r}_i, \hat{p}_j] = i\hbar\delta_{ij}$ and $[\hat{r}_i, \hat{r}_j] = [\hat{p}_i, \hat{p}_j] = 0$. From these, compute $[\hat{L}_x, \hat{L}_y]$:

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y,\; \hat{z}\hat{p}_x - \hat{x}\hat{p}_z].$$

Expand into four terms. The only nonzero contributions come from pairs involving one position and one conjugate momentum of the same coordinate:

$$= \hat{y}\hat{p}_x[\hat{p}_z, \hat{z}] + \hat{p}_y\hat{x}[\hat{z}, \hat{p}_z] = \hat{y}\hat{p}_x(-i\hbar) + \hat{x}\hat{p}_y(i\hbar) = i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\hat{L}_z.$$

The other two relations follow by cyclic permutation $x \to y \to z \to x$. The compact form is:

$$\boxed{[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k,}$$

where $\epsilon_{ijk}$ is the Levi-Civita symbol ($\epsilon_{xyz} = 1$, antisymmetric under exchange of any two indices).

Now form $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$ and compute $[\hat{L}^2, \hat{L}_z]$:

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z] + [\hat{L}_z^2, \hat{L}_z].$$

The last term is zero. For the first: $[\hat{L}_x^2, \hat{L}_z] = \hat{L}_x[\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x = \hat{L}_x(-i\hbar\hat{L}_y) + (-i\hbar\hat{L}_y)\hat{L}_x$. For the second: $[\hat{L}_y^2, \hat{L}_z] = \hat{L}_y(i\hbar\hat{L}_x) + (i\hbar\hat{L}_x)\hat{L}_y$. Sum the two:

$$[\hat{L}^2, \hat{L}_z] = -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x) + i\hbar(\hat{L}_y\hat{L}_x + \hat{L}_x\hat{L}_y) = 0.$$

By the same argument (or by symmetry), $[\hat{L}^2, \hat{L}_x] = [\hat{L}^2, \hat{L}_y] = 0$. Therefore:

$$\boxed{[\hat{L}^2, \hat{L}_i] = 0 \quad \text{for } i = x, y, z.}$$

**What this means.** Because $\hat{L}^2$ commutes with every component of $\hat{L}$, there exist states that are simultaneously eigenstates of $\hat{L}^2$ and of any one chosen component — conventionally $\hat{L}_z$. Because $\hat{L}_x$, $\hat{L}_y$, $\hat{L}_z$ do not commute with each other, no state can be simultaneously an eigenstate of two different components. This is not a choice about how to measure; it is a structural consequence of the algebra.

---

### Raising and Lowering Operators

Define:

$$\hat{L}_+ = \hat{L}_x + i\hat{L}_y, \qquad \hat{L}_- = \hat{L}_x - i\hat{L}_y = \hat{L}_+^\dagger.$$

From the fundamental commutators:

$$[\hat{L}_z, \hat{L}_+] = [\hat{L}_z, \hat{L}_x] + i[\hat{L}_z, \hat{L}_y] = i\hbar\hat{L}_y + i(-i\hbar\hat{L}_x) = \hbar(\hat{L}_x + i\hat{L}_y) = \hbar\hat{L}_+.$$

Similarly, $[\hat{L}_z, \hat{L}_-] = -\hbar\hat{L}_-$. And:

$$[\hat{L}_+, \hat{L}_-] = [\hat{L}_x + i\hat{L}_y, \hat{L}_x - i\hat{L}_y] = -i[\hat{L}_x, \hat{L}_y] + i[\hat{L}_y, \hat{L}_x] = -i(i\hbar\hat{L}_z) + i(-i\hbar\hat{L}_z) = 2\hbar\hat{L}_z.$$

These three commutators are the engine of the derivation:

$$[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+, \qquad [\hat{L}_z, \hat{L}_-] = -\hbar\hat{L}_-, \qquad [\hat{L}_+, \hat{L}_-] = 2\hbar\hat{L}_z.$$

Also useful: because $[\hat{L}^2, \hat{L}_\pm] = 0$ (from $[\hat{L}^2, \hat{L}_x] = [\hat{L}^2, \hat{L}_y] = 0$), the ladder operators leave the $L^2$ eigenvalue unchanged.

**The stepping argument.** Suppose $|\ell, m\rangle$ is a simultaneous eigenstate of $\hat{L}^2$ and $\hat{L}_z$:

$$\hat{L}^2|\ell, m\rangle = \lambda|\ell, m\rangle, \qquad \hat{L}_z|\ell, m\rangle = \hbar m|\ell, m\rangle.$$

What is $\hat{L}_z(\hat{L}_+|\ell, m\rangle)$? Use the commutator:

$$\hat{L}_z\hat{L}_+ = \hat{L}_+\hat{L}_z + [\hat{L}_z, \hat{L}_+] = \hat{L}_+\hat{L}_z + \hbar\hat{L}_+.$$

Therefore:

$$\hat{L}_z(\hat{L}_+|\ell, m\rangle) = (\hat{L}_+\hat{L}_z + \hbar\hat{L}_+)|\ell, m\rangle = \hat{L}_+(\hbar m|\ell, m\rangle) + \hbar\hat{L}_+|\ell, m\rangle = \hbar(m+1)(\hat{L}_+|\ell, m\rangle).$$

So $\hat{L}_+|\ell, m\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $\hbar(m+1)$: the raising operator steps $m$ up by 1. By the same logic, $\hat{L}_-|\ell, m\rangle$ is an eigenstate with eigenvalue $\hbar(m-1)$: the lowering operator steps $m$ down by 1. Since $[\hat{L}^2, \hat{L}_\pm] = 0$, the $L^2$ eigenvalue $\lambda$ does not change.

---

### Deriving the Spectrum

**The bound.** Consider the operator $\hat{L}_x^2 + \hat{L}_y^2 = \hat{L}^2 - \hat{L}_z^2$. Since it is a sum of squares of Hermitian operators, its expectation value in any state is non-negative:

$$\langle\hat{L}^2 - \hat{L}_z^2\rangle = \lambda - \hbar^2 m^2 \geq 0, \qquad \text{so} \qquad m^2 \leq \lambda/\hbar^2.$$

The quantum number $m$ is bounded: for fixed $\lambda$, there exists a maximum $m_{\max}$ and a minimum $m_{\min}$.

**Termination at the top.** At $m = m_{\max}$, the raising operator must annihilate the state (otherwise $m$ could step higher, contradicting the bound):

$$\hat{L}_+|\ell, m_{\max}\rangle = 0.$$

Apply $\hat{L}_-$ to both sides and use $\hat{L}^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$ (derived from $[\hat{L}_+, \hat{L}_-] = 2\hbar\hat{L}_z$):

$$\hat{L}^2|\ell, m_{\max}\rangle = (\hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z)|\ell, m_{\max}\rangle = (0 + \hbar^2 m_{\max}^2 + \hbar^2 m_{\max})|\ell, m_{\max}\rangle.$$

So $\lambda = \hbar^2 m_{\max}(m_{\max} + 1)$. Setting $\ell \equiv m_{\max}$:

$$\lambda = \hbar^2\ell(\ell+1).$$

**Termination at the bottom.** The same argument at $m_{\min}$ gives $\lambda = \hbar^2 m_{\min}(m_{\min} - 1)$, so $m_{\min}(m_{\min} - 1) = \ell(\ell+1)$. The two solutions are $m_{\min} = \ell + 1$ (rejected, since $m_{\min} \leq m_{\max} = \ell$) and $m_{\min} = -\ell$. Therefore:

$$m = -\ell, -\ell+1, \ldots, \ell - 1, \ell.$$

**Integer or half-integer?** Starting from $m_{\min} = -\ell$ and stepping up to $m_{\max} = \ell$ requires $2\ell$ integer steps, so $2\ell$ must be a non-negative integer. This means $\ell = 0, \frac{1}{2}, 1, \frac{3}{2}, 2, \ldots$ — integers and half-integers alike.

**The integer restriction for orbital angular momentum.** In coordinate space, $\hat{L}_z = -i\hbar\partial_\phi$ and the eigenfunction is $\Phi_m(\phi) = e^{im\phi}/\sqrt{2\pi}$. Single-valuedness, $\Phi_m(\phi + 2\pi) = \Phi_m(\phi)$, requires $e^{2\pi im} = 1$, so $m$ must be an integer. Therefore $\ell$ must be a non-negative integer for orbital angular momentum. The half-integer values, allowed by the algebra, are realized by spin angular momentum (Chapter 8), which lives in an abstract Hilbert space and has no position-space wave function to constrain.

**Summary.**

$$\boxed{\hat{L}^2|\ell, m\rangle = \hbar^2\ell(\ell+1)|\ell, m\rangle, \qquad \hat{L}_z|\ell, m\rangle = \hbar m|\ell, m\rangle,}$$
$$m = -\ell, -\ell+1, \ldots, \ell, \qquad \ell = 0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \ldots$$

For orbital angular momentum: $\ell = 0, 1, 2, 3, \ldots$ (integers only).

---

### Normalization of the Ladder Operators

$\hat{L}_+|\ell, m\rangle$ is proportional to $|\ell, m+1\rangle$, but we need the proportionality constant. Let $\hat{L}_+|\ell, m\rangle = C_m^+\hbar|\ell, m+1\rangle$. Compute $|C_m^+|^2$ from the norm:

$$|C_m^+|^2\hbar^2 = \langle\ell, m|\hat{L}_-\hat{L}_+|\ell, m\rangle.$$

Use $\hat{L}_-\hat{L}_+ = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z$:

$$= \langle\ell, m|(\hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z)|\ell, m\rangle = \hbar^2[\ell(\ell+1) - m^2 - m] = \hbar^2(\ell - m)(\ell + m + 1).$$

Choosing the phase so that $C_m^+$ is real and positive:

$$\hat{L}_+|\ell, m\rangle = \hbar\sqrt{(\ell - m)(\ell + m + 1)}\;|\ell, m+1\rangle.$$

Since $\hat{L}_- = \hat{L}_+^\dagger$, taking the Hermitian conjugate gives:

$$\hat{L}_-|\ell, m\rangle = \hbar\sqrt{(\ell + m)(\ell - m + 1)}\;|\ell, m-1\rangle.$$

**Checks.** At the top rung $m = \ell$: $(\ell - \ell)(\ell + \ell + 1) = 0$, so $\hat{L}_+|\ell, \ell\rangle = 0$. At the bottom rung $m = -\ell$: $(\ell - \ell)(2\ell + 1) = 0$, so $\hat{L}_-|\ell, -\ell\rangle = 0$. Both termination conditions are satisfied automatically.

---

### The $\ell = 1$ Matrices

For $\ell = 1$, there are three basis states: $|1, -1\rangle$, $|1, 0\rangle$, $|1, 1\rangle$. In this basis, $\hat{L}_z$ is diagonal:

$$\hat{L}_z = \hbar\begin{pmatrix}-1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1\end{pmatrix}.$$

For $\hat{L}_+$, compute each matrix element using the raising formula. The nonzero ones:

$$\hat{L}_+|1,-1\rangle = \hbar\sqrt{(1+1)(1-1+1)}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle,$$
$$\hat{L}_+|1,0\rangle = \hbar\sqrt{(1-0)(1+0+1)}\,|1,1\rangle = \hbar\sqrt{2}\,|1,1\rangle,$$
$$\hat{L}_+|1,1\rangle = 0.$$

So (ordering the rows and columns as $m = -1, 0, +1$):

$$\hat{L}_+ = \hbar\sqrt{2}\begin{pmatrix}0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{pmatrix}, \qquad \hat{L}_- = \hat{L}_+^\dagger = \hbar\sqrt{2}\begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0\end{pmatrix}.$$

From these, recover $\hat{L}_x = (\hat{L}_+ + \hat{L}_-)/2$ and $\hat{L}_y = (\hat{L}_+ - \hat{L}_-)/(2i)$:

$$\hat{L}_x = \frac{\hbar}{\sqrt{2}}\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}, \qquad \hat{L}_y = \frac{\hbar}{\sqrt{2}}\begin{pmatrix}0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0\end{pmatrix}.$$

**Verification.** Compute $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$:

$$\hat{L}_-\hat{L}_+ = 2\hbar^2\begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0\end{pmatrix}\begin{pmatrix}0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{pmatrix} = 2\hbar^2\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}.$$

Adding $\hat{L}_z^2 + \hbar\hat{L}_z = \hbar^2\mathrm{diag}(1,0,1) + \hbar^2\mathrm{diag}(-1,0,1) = \hbar^2\mathrm{diag}(0,0,2)$:

$$\hat{L}^2 = 2\hbar^2\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} = \hbar^2\ell(\ell+1)\mathbf{I}\Big|_{\ell=1}. \checkmark$$

---

### Connecting to the Spherical Harmonics

Chapter 5 derived the spherical harmonics $Y_{\ell m}(\theta,\phi)$ as solutions to the differential equation $\hat{L}^2 Y = \hbar^2\ell(\ell+1)Y$. The algebraic approach of this chapter reproduces the same eigenvalue structure without solving any differential equation. The connection is explicit.

In coordinate space, the ladder operators take the form:

$$\hat{L}_\pm = \pm\hbar e^{\pm i\phi}\!\left(\frac{\partial}{\partial\theta} \pm i\cot\theta\frac{\partial}{\partial\phi}\right).$$

Acting on $Y_\ell^\ell = \frac{(-1)^\ell}{2^\ell\ell!}\sqrt{\frac{(2\ell+1)!}{4\pi}}\sin^\ell\theta\, e^{i\ell\phi}$ (the highest-weight spherical harmonic), repeated application of $\hat{L}_-$ generates all lower harmonics. For example:

$$\hat{L}_- Y_1^1 = \hbar\sqrt{2}\,Y_1^0 \quad \Longrightarrow \quad Y_1^0 = \frac{1}{\hbar\sqrt{2}}\hat{L}_- Y_1^1 = \sqrt{\frac{3}{4\pi}}\cos\theta. \checkmark$$

This is how the associated Legendre functions $P_\ell^m$ emerge from the algebra: they are what you get when you apply $\hat{L}_-$ to $\sin^\ell\theta\,e^{i\ell\phi}$ a total of $\ell - m$ times.

**The two approaches are complementary.** The analytic approach (Chapter 5) gives explicit wave functions. The algebraic approach (this chapter) reveals the eigenvalue structure to be purely algebraic, independent of the position-space realization. The algebra works for spin-1/2 (no position-space wave function) for exactly this reason: the commutation relations $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ are identical to $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$, and the entire derivation applies verbatim.

---

### Why $\hat{L}^2\neq\hat{L}_z^2$, Revisited Algebraically

In the state $|\ell, m = \ell\rangle$ — the top of the ladder — the expectation values are:

$$\langle\hat{L}_z\rangle = \hbar\ell, \qquad \langle\hat{L}^2\rangle = \hbar^2\ell(\ell+1).$$

The deficit is $\langle\hat{L}^2\rangle - \langle\hat{L}_z\rangle^2 = \hbar^2\ell$. Since $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$, we get $\langle\hat{L}_x^2\rangle + \langle\hat{L}_y^2\rangle = \hbar^2\ell$. By symmetry, $\langle\hat{L}_x^2\rangle = \langle\hat{L}_y^2\rangle = \hbar^2\ell/2$.

Meanwhile, $\langle\hat{L}_x\rangle = \langle\hat{L}_y\rangle = 0$ in any eigenstate of $\hat{L}_z$ (by the Hermitian character of $\hat{L}_x$, $\hat{L}_y$ and the structure of the matrix elements). So $\sigma_{L_x}^2 = \langle\hat{L}_x^2\rangle - \langle\hat{L}_x\rangle^2 = \hbar^2\ell/2$, giving $\sigma_{L_x} = \hbar\sqrt{\ell/2}$.

The Robertson uncertainty principle for $\hat{L}_x$ and $\hat{L}_y$:

$$\sigma_{L_x}\sigma_{L_y} \geq \frac{1}{2}|\langle[\hat{L}_x, \hat{L}_y]\rangle| = \frac{\hbar}{2}|\langle\hat{L}_z\rangle| = \frac{\hbar^2\ell}{2}.$$

The bound gives $\sigma_{L_x}\sigma_{L_y} \geq \hbar^2\ell/2$, and the actual value is $(\hbar\sqrt{\ell/2})^2 = \hbar^2\ell/2$. The bound is exactly saturated: the maximally aligned state $|\ell, \ell\rangle$ is a minimum-uncertainty state for the transverse components. This is the algebraic version of the geometric fact that the angular momentum precesses on a cone of half-angle $\arccos(\ell/\sqrt{\ell(\ell+1)})$.

---

## Worked Example: Ladder Action and the Spectrum for $\ell = 1$

**The lesson.** For the $\ell = 1$ subspace, compute the action of $\hat{L}_\pm$ on each basis state and verify the commutation relations from the matrices.

**Setup.** The three basis states are $|1, -1\rangle$, $|1, 0\rangle$, $|1, 1\rangle$. From the normalization formula $\hat{L}_\pm|\ell, m\rangle = \hbar\sqrt{(\ell \mp m)(\ell \pm m + 1)}\,|\ell, m\pm 1\rangle$:

$$\hat{L}_+|1,-1\rangle = \hbar\sqrt{2\cdot 1}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle.$$
$$\hat{L}_+|1,0\rangle = \hbar\sqrt{1\cdot 2}\,|1,1\rangle = \hbar\sqrt{2}\,|1,1\rangle.$$
$$\hat{L}_+|1,1\rangle = \hbar\sqrt{0\cdot 3}\,|1,2\rangle = 0. \quad\text{(Top rung — annihilated.)}$$

Similarly for $\hat{L}_-$:

$$\hat{L}_-|1,1\rangle = \hbar\sqrt{2\cdot 1}\,|1,0\rangle = \hbar\sqrt{2}\,|1,0\rangle.$$
$$\hat{L}_-|1,0\rangle = \hbar\sqrt{1\cdot 2}\,|1,-1\rangle = \hbar\sqrt{2}\,|1,-1\rangle.$$
$$\hat{L}_-|1,-1\rangle = 0. \quad\text{(Bottom rung — annihilated.)}$$

**Verify a commutation relation from the matrices.** Check $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$. Using the matrices:

$$\hat{L}_z\hat{L}_+ - \hat{L}_+\hat{L}_z = \hbar\begin{pmatrix}-1\\&0\\&&1\end{pmatrix}\cdot\hbar\sqrt{2}\begin{pmatrix}0\\1\\&1\end{pmatrix} - \hbar\sqrt{2}\begin{pmatrix}0\\1\\&1\end{pmatrix}\cdot\hbar\begin{pmatrix}-1\\&0\\&&1\end{pmatrix}.$$

Working out the $(2,1)$ entry (row 2, column 1 in the $(m=-1,0,+1)$ ordering):

Row 2 of $\hat{L}_z$ is $(0, 0, 0)$; column 1 of $\hat{L}_+$ is $(0, \hbar\sqrt{2}, 0)^T$. Product gives $0$. Row 2 of $\hat{L}_+$ is $(0, 0, \hbar\sqrt{2})$... 

Actually, let us just verify the action on a state. Apply $[\hat{L}_z, \hat{L}_+]$ to $|1, 0\rangle$:

$$\hat{L}_z(\hat{L}_+|1,0\rangle) - \hat{L}_+(\hat{L}_z|1,0\rangle) = \hat{L}_z(\hbar\sqrt{2}|1,1\rangle) - \hat{L}_+(0) = \hbar\sqrt{2}\cdot\hbar|1,1\rangle = \hbar\cdot\hbar\sqrt{2}|1,1\rangle.$$

And $\hbar\hat{L}_+|1,0\rangle = \hbar\cdot\hbar\sqrt{2}|1,1\rangle$. They agree: $[\hat{L}_z, \hat{L}_+]|1,0\rangle = \hbar\hat{L}_+|1,0\rangle$. $\checkmark$

**Verify $\hat{L}^2$ acting on the middle state.** Use $\hat{L}^2 = \hat{L}_+\hat{L}_- + \hat{L}_z^2 - \hbar\hat{L}_z$:

$$\hat{L}^2|1,0\rangle = \hat{L}_+(\hat{L}_-|1,0\rangle) + \hat{L}_z^2|1,0\rangle - \hbar\hat{L}_z|1,0\rangle$$
$$= \hat{L}_+(\hbar\sqrt{2}|1,-1\rangle) + 0 - 0 = \hbar\sqrt{2}\cdot\hbar\sqrt{2}|1,0\rangle = 2\hbar^2|1,0\rangle = \hbar^2\cdot 1\cdot 2\cdot|1,0\rangle.$$

$\hbar^2\ell(\ell+1) = \hbar^2\cdot 1\cdot 2 = 2\hbar^2$. $\checkmark$

**The limit.** The $\ell = 1$ matrices are the smallest nontrivial case of the angular momentum algebra. They carry the full structure: the ladder terminates at both ends, the commutation relations are satisfied, and $\hat{L}^2 = 2\hbar^2 I$ in the subspace. The next case, $\ell = 2$, has a $5\times 5$ matrix representation and five values of $m$; the $\ell = 1/2$ case has a $2\times 2$ representation — the Pauli matrices of spin-1/2. Chapter 8 develops the spin-1/2 case in detail.

---

## Common Misconceptions

**"The z-axis is special."** It is not. Any axis serves equally well; we choose $\hat{z}$ by convention (and because $\hat{L}_z = -i\hbar\partial_\phi$ is the simplest operator in spherical coordinates). In a magnetic field problem, the "special" axis aligns with $\vec{B}$. In a beam experiment, it aligns with the beam. The choice is always ours.

**"$\ell$ must be an integer by definition."** The algebraic derivation produces $\ell = 0, \frac{1}{2}, 1, \frac{3}{2}, \ldots$ The restriction to integers comes from an additional physical requirement: single-valuedness of the position-space wave function $e^{im\phi}$ under $\phi \to \phi + 2\pi$. For spin, there is no wave function to restrict, and the half-integer case is realized. The algebra is more general than the orbital case.

**"The ladder operators change $\ell$."** They do not. Since $[\hat{L}^2, \hat{L}_\pm] = 0$, applying $\hat{L}_\pm$ to $|\ell, m\rangle$ gives a state with the same $\ell$ and $m \pm 1$. The operators move within the $\ell$-subspace. Operators that change $\ell$ are not part of the angular momentum algebra — they appear in the coupling of two angular momenta (Chapter 9).

**"$\hat{L}_+|\ell, \ell\rangle$ is not zero; it just can't be normalized."** No: $\hat{L}_+|\ell, \ell\rangle = 0$ exactly. The normalization constant $\sqrt{(\ell - \ell)(\ell + \ell + 1)} = \sqrt{0} = 0$. This is not a normalization failure. The state is the zero vector.

**"$\langle\hat{L}_x\rangle \neq 0$ in an eigenstate of $\hat{L}_z$."** In any $\hat{L}_z$ eigenstate, $\langle\hat{L}_x\rangle = \langle\hat{L}_y\rangle = 0$, because the matrix elements of $\hat{L}_x$ and $\hat{L}_y$ connect states with $\Delta m = \pm 1$, and diagonal matrix elements in the $m$-basis are zero. But $\langle\hat{L}_x^2\rangle \neq 0$: the variance is nonzero even though the mean is zero. The expectation value and the uncertainty are not the same thing.

**"The algebra here is different from the harmonic oscillator."** Structurally they are the same. For the harmonic oscillator: $[\hat{a}, \hat{a}^\dagger] = 1$ produces a spectrum indexed by a non-negative integer $n$, with $\hat{a}$ lowering and $\hat{a}^\dagger$ raising. For angular momentum: $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$ produces a bounded spectrum indexed by $m$, with $\hat{L}_-$ lowering and $\hat{L}_+$ raising. Both derive from a single algebraic relation and a non-negativity bound. The harmonic oscillator is unbounded below only because the non-negativity bound is one-sided. Angular momentum is bounded on both sides because $\hat{L}_x^2 + \hat{L}_y^2 \geq 0$ applies symmetrically.

---

## Exercises

### Warm-Up

**6.1** Derive $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ from first principles. Write out $\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y$ and $\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z$. Expand the commutator into four terms and use $[\hat{r}_i, \hat{p}_j] = i\hbar\delta_{ij}$ to evaluate. The calculation should take 4–6 lines. *(Tests: derivation from canonical commutation relations)*

**6.2** From $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$, show that if $\hat{L}_z|\psi\rangle = \hbar m|\psi\rangle$ then $\hat{L}_z(\hat{L}_+|\psi\rangle) = \hbar(m+1)(\hat{L}_+|\psi\rangle)$. State in words what this means physically. *(Tests: ladder-operator stepping argument)*

**6.3** Compute $\hat{L}_+|2, 1\rangle$ and $\hat{L}_-|2, 1\rangle$ explicitly using $\hat{L}_\pm|\ell,m\rangle = \hbar\sqrt{(\ell\mp m)(\ell\pm m+1)}\,|\ell,m\pm 1\rangle$. Verify: (a) $\hat{L}_+|2, 2\rangle = 0$; (b) $\hat{L}_-|2,-2\rangle = 0$; (c) $\langle 2,1|\hat{L}_+^\dagger\hat{L}_+|2,1\rangle = \hbar^2[\ell(\ell+1) - m(m+1)]$. *(Tests: normalization formula, termination conditions)*

### Application

**6.4** Write down the $3\times 3$ matrix representations of $\hat{L}_z$, $\hat{L}_+$, and $\hat{L}_-$ for $\ell = 1$ in the basis $\{|1,-1\rangle, |1,0\rangle, |1,1\rangle\}$. From these, construct $\hat{L}_x$ and $\hat{L}_y$. Verify $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ by matrix multiplication. *(Tests: $\ell=1$ matrix representation, verification of commutation relation)*

**6.5** For the state $|\psi\rangle = \frac{1}{\sqrt{2}}|1,-1\rangle + \frac{1}{\sqrt{2}}|1,1\rangle$ (an equal superposition of the top and bottom rungs of the $\ell = 1$ ladder): (a) compute $\langle\hat{L}_z\rangle$; (b) compute $\langle\hat{L}_z^2\rangle$; (c) compute $\sigma_{L_z}$; (d) compute $\langle\hat{L}^2\rangle$ and confirm it equals $2\hbar^2$. *(Tests: expectation values in a superposition state)*

**6.6** For $|\ell = 2, m = 1\rangle$: (a) compute $\langle\hat{L}_x\rangle$ and $\langle\hat{L}_y\rangle$ (argue from matrix element structure); (b) compute $\langle\hat{L}_x^2\rangle$ using $\hat{L}_x = (\hat{L}_+ + \hat{L}_-)/2$ and the ladder formulas; (c) verify the Robertson inequality $\sigma_{L_x}\sigma_{L_y} \geq (\hbar/2)|\langle\hat{L}_z\rangle|$. *(Tests: expectation values of transverse components; Robertson inequality for angular momentum)*

**6.7** In the maximally aligned state $|\ell, \ell\rangle$: (a) compute $\sigma_{L_x}$ and $\sigma_{L_y}$; (b) show that $\sigma_{L_x}\sigma_{L_y} = \hbar^2\ell/2$; (c) confirm the Robertson bound is $\hbar^2\ell/2$ and that the bound is saturated. State in one sentence what "saturated" means geometrically. *(Tests: minimum-uncertainty interpretation of the maximally aligned state)*

### Synthesis

**6.8** The algebraic derivation of the spectrum (raising/lowering, termination, non-negativity) applies verbatim to any set of operators satisfying $[J_i, J_j] = i\hbar\epsilon_{ijk}J_k$. (a) Write down the $2\times 2$ matrices $\hat{J}_z$, $\hat{J}_+$, $\hat{J}_-$ for $\ell = 1/2$. (b) Verify $[\hat{J}_z, \hat{J}_+] = \hbar\hat{J}_+$ from these matrices. (c) These matrices are $\hat{J}_i = (\hbar/2)\sigma_i$ where $\sigma_i$ are the Pauli matrices. Identify $\sigma_z$, $\sigma_+$, $\sigma_-$ from your answer and confirm they match the standard form. *(Tests: extension of the algebra to half-integer case; connection to spin-1/2 and Pauli matrices)*

**6.9** Use the coordinate-space expression $\hat{L}_- = -\hbar e^{-i\phi}(\partial_\theta - i\cot\theta\,\partial_\phi)$ to verify that $\hat{L}_- Y_1^1 = \hbar\sqrt{2}\,Y_1^0$, where $Y_1^1 = -\sqrt{3/(8\pi)}\sin\theta\, e^{i\phi}$ and $Y_1^0 = \sqrt{3/(4\pi)}\cos\theta$. This connects the abstract algebraic formula $\hat{L}_-|\ell, m\rangle = \hbar\sqrt{(\ell+m)(\ell-m+1)}\,|\ell, m-1\rangle$ to the explicit spherical-harmonic wave functions of Chapter 5. *(Tests: coordinate-space form of ladder operators; bridge between algebraic and analytic approaches)*

### Challenge

**6.10** The $\ell = 2$ subspace has basis $\{|2,-2\rangle, |2,-1\rangle, |2,0\rangle, |2,1\rangle, |2,2\rangle\}$. (a) Write down the $5\times 5$ matrix for $\hat{L}_z$. (b) Compute $\hat{L}_+$ by applying the normalization formula to each basis state. (c) Compute $\hat{L}^2 = \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$ and verify it equals $6\hbar^2 I$. (d) For the state $|2,2\rangle$: find the cone half-angle, $\sigma_{L_x}$, $\sigma_{L_y}$, and verify the Robertson bound is saturated. *(Tests: $5\times 5$ matrix construction; cone geometry; Robertson saturation for general $\ell$)*

---

## Still Puzzling

The angular momentum algebra $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ is the Lie algebra of $\mathrm{SU}(2) \cong \mathrm{SO}(3)$. The irreducible representations are labeled by $\ell$ — exactly the quantum number we derived. This is the deeper reason the ladder-operator argument works: it is the representation theory of a compact Lie group, and compact groups always have discrete representations. The spectrum $\hbar^2\ell(\ell+1)$ is not a coincidence of the specific differential operator; it is the eigenvalue structure of the Casimir element of $\mathfrak{su}(2)$. What I find I cannot fully explain to my satisfaction: why does nature attach angular momentum — specifically the spinor representation ($\ell = 1/2$) — to elementary particles, when spin has no classical analog and cannot be imagined as rotation? Dirac's answer is that spin-1/2 falls out of the Lorentz group when you demand a first-order relativistic wave equation. The Lie algebra is $\mathfrak{so}(1,3) \supset \mathfrak{su}(2) \oplus \mathfrak{su}(2)$, and spin is one of the two $\mathfrak{su}(2)$ factors. That is mathematically satisfying. Whether it is conceptually satisfying — whether it explains, or merely organizes — I genuinely do not know.

---

## The +1 — Simulation Exercise: The Angular Momentum Ladder Visualizer

Build a single-file D3 simulation that displays the $\ell = 1$ angular momentum algebra interactively: the three rungs of the ladder, the action of $\hat{L}_\pm$ as animated arrows between rungs, and the matrix representation updating in real time as the user selects a state. Deliverable: `06-angular-momentum.html`.

### Part 1 — CLAUDE.md Extension

```
## Chapter 6 — Angular Momentum Ladder Simulator Rules

ANGULAR MOMENTUM PHYSICS RULES

1. For ℓ = 0, 1/2, 1, 3/2, 2 (user selects via dropdown):
   - Basis states: |ℓ, m⟩ for m = -ℓ, -ℓ+1, ..., ℓ. Total 2ℓ+1 states.
   - L_z eigenvalues: ℏ*m for each state.
   - L^2 eigenvalue: ℏ^2 * ℓ*(ℓ+1) for all states in the subspace.

2. Ladder operator normalization (exact formula, no approximation):
     L_+ |ℓ, m⟩ = ℏ * sqrt[(ℓ-m)*(ℓ+m+1)] * |ℓ, m+1⟩
     L_- |ℓ, m⟩ = ℏ * sqrt[(ℓ+m)*(ℓ-m+1)] * |ℓ, m-1⟩
   At the top rung (m = ℓ): L_+ gives 0 exactly (coefficient = 0).
   At the bottom rung (m = -ℓ): L_- gives 0 exactly.

3. Matrix elements:
     (L_z)_{m'm} = ℏ*m * δ_{m'm}
     (L_+)_{m'm} = ℏ * sqrt[(ℓ-m)*(ℓ+m+1)] * δ_{m', m+1}
     (L_-)_{m'm} = ℏ * sqrt[(ℓ+m)*(ℓ-m+1)] * δ_{m', m-1}
     L_x = (L_+ + L_-)/2,  L_y = (L_+ - L_-)/(2i)

4. All matrices must satisfy:
     [L_z, L_+] = ℏ L_+     (verify by matrix multiplication at startup)
     [L_z, L_-] = -ℏ L_-    (verify by matrix multiplication at startup)
     [L_+, L_-] = 2ℏ L_z    (verify by matrix multiplication at startup)
     L^2 = L_x^2 + L_y^2 + L_z^2 = ℏ^2 ℓ(ℓ+1) I   (verify)

5. If any verification fails, write an explicit error to the console and
   highlight the failing matrix element in red in the UI.

KNOWN FAILURE MODES:
(a) Off-by-one in ladder normalization: check sqrt argument for each m.
(b) Wrong convention for L_+, L_-: rows vs. columns — L_+ has 1s on the
    super-diagonal (increasing m), L_- on the sub-diagonal.
(c) L^2 not proportional to I: matrix construction bug, probably off-by-one.
(d) Verification at startup skipped: silent bugs in matrix elements.
```

### Part 2 — The Simulation Prompt

```
Build 06-angular-momentum.html following CLAUDE.md.

SHOW.
A vertical ladder diagram (center, ~400 px wide) displaying the 2ℓ+1 rungs
of the angular momentum ladder for the selected ℓ. Each rung is a horizontal
bar labeled |ℓ, m⟩ with a numeric readout of the L_z eigenvalue in units of ℏ.

When the user clicks a rung, highlight it and draw animated arrows to the
adjacent rungs:
  - L_+ arrow (upward, blue): from the selected rung to m+1. Label the
    arrow with the coefficient ℏ*sqrt[(ℓ-m)(ℓ+m+1)] rounded to 3 sig figs.
    If m = ℓ, show the arrow as grayed-out and label "0 (top rung)".
  - L_- arrow (downward, red): from the selected rung to m-1. Label with
    the coefficient ℏ*sqrt[(ℓ+m)(ℓ-m+1)]. If m = -ℓ, gray out.

RIGHT PANEL: matrix display. Show the full (2ℓ+1) × (2ℓ+1) matrices for
L_z, L_+, L_-, L_x, L_y in units of ℏ. When the user has selected a state
|ℓ, m⟩, highlight the corresponding column of L_+ and the corresponding
column of L_- in the display.

BOTTOM STRIP: eigenvalue display.
  ℓ = [value]   m = [value] (of selected rung)
  L^2 = ℏ^2 * ℓ(ℓ+1) = [value] ℏ^2
  L_z = m * ℏ = [value] ℏ
  Cone half-angle = arccos(m / sqrt(ℓ(ℓ+1))) = [value]°   (for m = ℓ)
  Robertson bound: σ_{Lx} σ_{Ly} ≥ (ℏ/2)|m| ℏ = [value] ℏ^2

TOP: ℓ selector (dropdown: 0, 1/2, 1, 3/2, 2).

SAY.
Single self-contained HTML file. D3 v7 from CDN. No other dependencies.
All matrices constructed from the exact ladder formulas — no hard-coded values.
Verification of all four commutation relations runs at startup for every
selected ℓ. Console logs: "All commutation relations verified for ℓ = X" on
success, or the specific failing element on failure.

VERIFY.
At startup, for each ℓ in {0, 1/2, 1, 3/2, 2}:
(a) [L_z, L_+] = ℏ L_+: check all matrix elements within 1e-10.
(b) [L_z, L_-] = -ℏ L_-: same.
(c) [L_+, L_-] = 2ℏ L_z: same.
(d) L^2 = ℏ^2 ℓ(ℓ+1) I: check diagonal, off-diagonal = 0.
(e) For ℓ=1: L_+ applied to |1,1⟩ gives zero vector. L_- applied to
    |1,-1⟩ gives zero vector.
(f) For ℓ=1/2: the 2×2 matrices are (ℏ/2) times the Pauli matrices σ_z,
    σ_+, σ_-.

List known failure modes in an HTML comment at the top of the file.
```

### Part 3 — Exploration Tasks

**Task 1: The algebra delivers the spectrum.** Select $\ell = 1$. Click the middle rung $|1, 0\rangle$. Read the ladder coefficients: $\hat{L}_+$ gives $\hbar\sqrt{2}$, $\hat{L}_-$ gives $\hbar\sqrt{2}$. Click the top rung $|1, 1\rangle$: the $\hat{L}_+$ arrow is grayed out with coefficient $0$. This is the termination condition — the ladder has a top rung.

**Task 2: Half-integer $\ell$.** Change $\ell$ to $1/2$. The ladder has two rungs: $|1/2, -1/2\rangle$ and $|1/2, +1/2\rangle$. The matrices are $2 \times 2$. Confirm from the matrix display that $\hat{L}_z = (\hbar/2)\mathrm{diag}(-1, +1)$ — this is $(\hbar/2)\sigma_z$. The eigenvalue display shows $\hat{L}^2 = \hbar^2(1/2)(3/2) = (3/4)\hbar^2$. The half-integer case is algebra, not position space.

**Task 3: The cone.** Select $\ell = 2$, click the top rung $|2, 2\rangle$. The bottom strip shows: $L_z = 2\hbar$, $\sqrt{L^2} = \hbar\sqrt{6} \approx 2.45\hbar$, cone half-angle $= \arccos(2/\sqrt{6}) \approx 35.3°$. Select $|2, 0\rangle$: cone half-angle $= 90°$ — the angular momentum is perpendicular to $\hat{z}$.

**Task 4: Robertson bound.** For $\ell = 1$, state $|1, 1\rangle$: Robertson bound is $(\hbar/2)\cdot\hbar = \hbar^2/2$. The actual $\sigma_{L_x}\sigma_{L_y} = (\hbar\sqrt{1/2})^2 = \hbar^2/2$. The bound is saturated: the maximally aligned state is a minimum-uncertainty state for the transverse components.

**Task 5: Commutation verification.** Open the browser console. Confirm the output "All commutation relations verified for ℓ = 1" appears. Change $\ell$ to $3/2$ and confirm the same. If you introduce a deliberate off-by-one error in the ladder normalization, the console should flag which commutator fails.

### Part 4 — Six Failure Modes to Check

**Off-by-one in ladder normalization.** The coefficient for $\hat{L}_+|1, 0\rangle$ is $\hbar\sqrt{1 \cdot 2}$, not $\hbar\sqrt{2 \cdot 1}$ — these happen to be the same, but for $\ell = 2$, $\hat{L}_+|2, 1\rangle = \hbar\sqrt{1 \cdot 4}$. Check $\hat{L}_+|2, 0\rangle$: coefficient is $\hbar\sqrt{2 \cdot 3} = \hbar\sqrt{6}$, not $\hbar\sqrt{5}$ or $\hbar\sqrt{4}$.

**Row/column convention for $\hat{L}_+$.** $\hat{L}_+$ raises $m$, so its $(m', m)$ matrix element is nonzero for $m' = m+1$, i.e., elements on the super-diagonal (in the ordering $m = -\ell, \ldots, \ell$). If rows and columns are swapped, $\hat{L}_+$ will look like $\hat{L}_-$.

**$\hat{L}^2$ not proportional to $I$.** If $\hat{L}_x$ or $\hat{L}_y$ is computed from $\hat{L}_\pm$ with a factor-of-2 error, $\hat{L}^2$ will have the correct eigenvalues on the diagonal but nonzero off-diagonal elements. The commutation relation check will catch this.

**Startup verification skipped.** Bugs in matrix construction are silent without the commutator check. The check is cheap (matrix multiply) and catches all structural errors.

**Cone angle for $m = 0$.** The formula $\arccos(m/\sqrt{\ell(\ell+1)})$ gives $90°$ when $m = 0$, indicating the angular momentum is perpendicular to $\hat{z}$. A common bug: the code uses $\arccos(0/0) = \arccos(\text{NaN})$ when $\ell = 0$. Guard this case: for $\ell = 0$, the cone angle is undefined (there is no angular momentum).

**Half-integer $\ell$ display.** For $\ell = 1/2$ the matrices are $2\times 2$ and the states are $|1/2, -1/2\rangle$, $|1/2, +1/2\rangle$. Confirm the matrix display renders $2 \times 2$ grids, not $3 \times 3$.

---

## References

Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012. Chapter 3 (Angular Momentum), §3.5 (Generalized Uncertainty Principle). [verify] Primary source for the ladder-operator derivation of the angular momentum spectrum in these notes.

Sakurai, J. J., and Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021. Chapter 3. [verify] The angular momentum algebra presented from the abstract Hilbert space perspective; covers the connection to $\mathrm{SU}(2)$ representation theory.

Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994. Chapter 12. [verify] Careful treatment of the algebraic derivation including the proof that $2\ell$ must be an integer.

Condon, E. U., and Shortley, G. H. *The Theory of Atomic Spectra*. Cambridge University Press, 1935. [verify] Original source for the phase convention used in the normalization of $Y_\ell^m$ and the matrix elements of $\hat{L}_\pm$. These conventions propagate through all subsequent atomic-physics calculations.

Cohen-Tannoudji, C., Diu, B., and Laloë, F. *Quantum Mechanics*, Vol. I. Wiley, 1977. Chapter VI. [verify] The commutation-relation approach and the irreducible representations of the rotation group $\mathrm{SO}(3)$ and $\mathrm{SU}(2)$.

*Bridge to Chapter 7: The commutation relations $[\hat{J}_i, \hat{J}_j] = i\hbar\epsilon_{ijk}\hat{J}_k$ apply equally to orbital angular momentum (integer $\ell$, this chapter) and to spin (half-integer $s$, Chapter 7). The two-state Hilbert space of spin-1/2 is the $\ell = 1/2$ case of the algebra you just derived. The Pauli matrices $\hat{S}_i = (\hbar/2)\sigma_i$ are the $2\times 2$ matrix representations you constructed in Exercise 6.8 and Task 2.*
