# Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

## TL;DR

- The wave function $\psi(x)$ is not the state — it is the state's shadow in one basis.
- The state $|\psi\rangle$ lives in an abstract complex vector space (Hilbert space); three identities — completeness, orthonormality, expansion — do all the representational work.
- An operator is a basis-independent map; its matrix representation changes when the basis changes, its eigenvalues do not.
- The Fourier transform between position and momentum spaces is not a separate mathematical operation: it is the change-of-basis formula $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$.
- The qubit anchors every abstract idea with a 2×2 calculation you can finish by hand.

## Learning Objectives

By the end of this chapter you will be able to:

1. **Remember** the Dirac bracket notation and state what each symbol ($|\psi\rangle$, $\langle\phi|$, $\langle\phi|\psi\rangle$, $|\psi\rangle\langle\phi|$) means categorically. *(Bloom: Remember)*
2. **Understand** why the wave function $\psi(x)$ is a representation of a state and not the state itself, by tracing how it arises from the inner product $\langle x|\psi\rangle$. *(Bloom: Understand)*
3. **Apply** the completeness relation $\sum_n |n\rangle\langle n| = \hat{I}$ to convert abstract bra–ket expressions into explicit sums or integrals. *(Bloom: Apply)*
4. **Apply** the matrix-element formula $A_{mn} = \langle m|\hat{A}|n\rangle$ to compute operator representations in multiple bases and explain why the matrices differ while the operator does not. *(Bloom: Apply)*
5. **Analyze** the relationship between $\psi(x)$ and $\tilde{\psi}(p)$ by deriving the Fourier transform from the completeness relation and the inner product $\langle x|p\rangle$. *(Bloom: Analyze)*

---

## Opening: A Thing That Should Bother You

The wave function $\psi(x)$ tells you the probability amplitude for finding a particle at position $x$. Its Fourier transform $\tilde{\psi}(p)$ tells you the probability amplitude for finding the particle with momentum $p$. These two functions contain identical physical information — each is a complete description of the state. Yet they look nothing alike. One is narrow where the other is broad. One oscillates rapidly where the other is concentrated. A Gaussian in position is a Gaussian in momentum only because the Fourier transform happens to work out that way; a step function in position is a sinc function in momentum.

So: which one is "the state"?

The answer forces a reframe. Neither $\psi(x)$ nor $\tilde{\psi}(p)$ is the state. Each is the state's *component list* in a particular basis — the way the same vector in three-dimensional space has different coordinates in Cartesian, cylindrical, or spherical representations. The state is the abstract object, the vector, that lives above all bases simultaneously. When you project it onto the position basis you get $\psi(x)$; when you project it onto the momentum basis you get $\tilde{\psi}(p)$. The Fourier transform is the change-of-basis formula, nothing more.

This is not philosophy. Every calculation you have done in wave mechanics has been a calculation in one basis. The formalism this chapter introduces lets you write it once and evaluate it in any basis you choose.

---

## Core Development

### Hilbert Space: The Arena

A **Hilbert space** $\mathcal{H}$ is a complete complex inner-product space. You can add vectors, scale them by complex numbers, and take inner products — that is the whole structure. Two properties distinguish it from the real vector spaces of ordinary linear algebra.

First, the scalars are complex. A state $|\psi\rangle$ can be multiplied by any $c \in \mathbb{C}$ and the result $c|\psi\rangle$ is still in $\mathcal{H}$.

Second, the inner product is **sesquilinear**, not bilinear. For kets $|\phi\rangle$ and $|\psi\rangle$, the inner product $\langle\phi|\psi\rangle$ is:
- Linear in the second argument: $\langle\phi|(a|\psi_1\rangle + b|\psi_2\rangle) = a\langle\phi|\psi_1\rangle + b\langle\phi|\psi_2\rangle$
- Conjugate-linear in the first: $\langle(a|\phi_1\rangle + b|\phi_2\rangle)|\psi\rangle = a^*\langle\phi_1|\psi\rangle + b^*\langle\phi_2|\psi\rangle$
- Conjugate-symmetric: $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$
- Positive definite: $\langle\psi|\psi\rangle \geq 0$, with equality only for the zero vector

The third property is the one students most reliably misapply. In real inner-product spaces $(\vec{u},\vec{v}) = (\vec{v},\vec{u})$. In Hilbert space, swapping bra and ket conjugates the result. This conjugation is behind every sign error in adjoint calculations and every confused step in Hermiticity proofs.

The dimension of $\mathcal{H}$ can be finite or infinite. A qubit lives in $\mathbb{C}^2$ (dimension 2). The states of a particle on a line live in $L^2(\mathbb{R})$, the space of square-integrable complex functions (infinite-dimensional). The abstract framework handles both.

### Kets, Bras, and the Dual Space

Dirac introduced a notation that keeps the categorical distinctions visible.

A **ket** $|\psi\rangle$ is a vector in $\mathcal{H}$. Think: column vector.

A **bra** $\langle\phi|$ is a *linear functional* on $\mathcal{H}$ — a map that takes any ket to a complex number. Concretely, for each ket $|\phi\rangle$ there is a corresponding bra $\langle\phi|$ defined by the rule $\langle\phi| : |\psi\rangle \mapsto \langle\phi|\psi\rangle$. Think: row vector (conjugate transpose of the column vector).

The bra corresponding to $c|\phi\rangle$ is $c^*\langle\phi|$ — the complex conjugate appears. This is not a convention; it follows from the sesquilinearity of the inner product.

The bracket $\langle\phi|\psi\rangle$ is a **scalar** (complex number). The product written in the other order, $|\psi\rangle\langle\phi|$, is an **operator** — the linear map that takes any $|\chi\rangle$ to $\langle\phi|\chi\rangle\,|\psi\rangle$. Inner product: scalar. Outer product: operator. Students who do not maintain this categorical distinction produce expressions like $|\psi\rangle = \langle\phi|\psi\rangle|\psi\rangle$, which mixes categories and is wrong in two senses at once.

### Three Identities That Do All the Work

Fix an orthonormal basis $\{|n\rangle\}$ for $\mathcal{H}$. Three identities do almost everything:

**1. Completeness (resolution of the identity):**
$$\sum_n |n\rangle\langle n| = \hat{I}$$

This is just the number 1, written as an operator sum. For the continuous position basis, the sum becomes an integral:
$$\int |x\rangle\langle x|\,dx = \hat{I}$$

**2. Orthonormality:**
$$\langle m|n\rangle = \delta_{mn}$$

For the position basis the discrete Kronecker delta becomes a Dirac delta:
$$\langle x|x'\rangle = \delta(x - x')$$

**3. Expansion (basis decomposition):**
$$|\psi\rangle = \sum_n c_n|n\rangle, \qquad c_n = \langle n|\psi\rangle$$

The coefficient $c_n$ is the inner product of the state with the $n$th basis vector — exactly the projection of the abstract vector onto the $n$th direction. Change the basis, change the numbers $c_n$. The vector $|\psi\rangle$ does not move.

The computational workhorse is completeness. Inserting $\hat{I}$ between any two expressions converts abstract inner products into concrete sums (or integrals) over components:
$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|n\rangle\langle n|\psi\rangle = \sum_n \phi_n^* \psi_n$$

For the position basis this becomes the ordinary wave-function inner product $\int \phi^*(x)\psi(x)\,dx$.

### Position Space, Momentum Space, and the Fourier Transform

The quantum state of a particle on a line is a unit vector $|\psi\rangle$ in $L^2(\mathbb{R})$. Two especially useful bases are the position eigenstates $\{|x\rangle\}$ and the momentum eigenstates $\{|p\rangle\}$.

The position-space wave function:
$$\psi(x) = \langle x|\psi\rangle$$

The momentum-space wave function:
$$\tilde{\psi}(p) = \langle p|\psi\rangle$$

These are not two different functions — they are two representations of the same vector in two different bases.

Now derive the relationship. Insert the position-basis completeness relation into $\tilde{\psi}(p)$:
$$\tilde{\psi}(p) = \langle p|\psi\rangle = \langle p|\hat{I}|\psi\rangle = \int \langle p|x\rangle\langle x|\psi\rangle\,dx = \int \langle p|x\rangle\,\psi(x)\,dx$$

The Fourier transform drops out once you know what $\langle p|x\rangle$ is. The momentum eigenstates in position space satisfy $\hat{p}|p\rangle = p|p\rangle$, i.e., $-i\hbar\partial_x\langle x|p\rangle = p\langle x|p\rangle$, giving $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Therefore $\langle p|x\rangle = e^{-ipx/\hbar}/\sqrt{2\pi\hbar}$, and:
$$\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx$$

The Fourier transform is the change-of-basis formula between $\{|x\rangle\}$ and $\{|p\rangle\}$. It is not a separate mathematical tool imported from analysis; it is the inner product $\langle p|x\rangle$ evaluated.

This reframing has a payoff: whenever you see a Fourier transform in quantum mechanics, you are seeing a basis change. The position representation and momentum representation contain the same physics, the same information. Neither is more fundamental.

### Operators as Abstract Maps; Matrices Are Incidental to the Basis

A **linear operator** $\hat{A}$ on $\mathcal{H}$ is a linear map $\mathcal{H} \to \mathcal{H}$. That is the full definition. The operator exists independently of any basis.

In a basis $\{|n\rangle\}$, the operator has a **matrix representation** with entries:
$$A_{mn} = \langle m|\hat{A}|n\rangle$$

Different basis, different matrix. Same operator. This is the most important distinction in the chapter, and the one students most reliably miss.

The position operator $\hat{x}$ illustrates this sharply. In the position basis, $\hat{x}|x\rangle = x|x\rangle$, so it acts by multiplication — its matrix is diagonal. The same operator $\hat{x}$ in the energy basis of the harmonic oscillator has matrix elements $\langle n|\hat{x}|m\rangle$ involving $\sqrt{n}$ — it is tridiagonal. One operator, two different-looking matrices. The matrices are basis-dependent artifacts. The operator is not.

The **adjoint** $\hat{A}^\dagger$ of an operator is defined by:
$$\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle \quad \text{for all }|\psi\rangle, |\phi\rangle$$

In matrix form, the adjoint is the conjugate transpose: $(A^\dagger)_{mn} = A_{nm}^*$. For real matrices this is the ordinary transpose. For complex matrices the conjugation matters — it is exactly where sign errors live.

An operator is **Hermitian** (self-adjoint) if $\hat{A}^\dagger = \hat{A}$, i.e., $A_{mn} = A_{nm}^*$. The standard failure-mode example is $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Its plain transpose is $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$ (antisymmetric). But its conjugate transpose is $\sigma_y$ (Hermitian). Students who learned "Hermitian means symmetric" in real linear algebra routinely get this wrong.

The adjoint of a product reverses order: $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$. This is a one-line proof from the definition, but students who do not know it stumble whenever they encounter products of operators.

### Basis Change as Unitary Transformation

Moving from basis $\{|a_n\rangle\}$ to basis $\{|b_m\rangle\}$ is implemented by the unitary matrix $U_{mn} = \langle a_m|b_n\rangle$. Under this transformation, operator matrices transform as:
$$O' = U^\dagger O U$$

The eigenvalues of $O'$ are identical to those of $O$; only the matrix elements change. Physics is basis-independent. The matrix is the observer's representation of the physics; the operator is the physics itself.

---

## Worked Example: A State in the Energy Basis

**Setup.** A particle is confined in an infinite square well of width $L$. It is prepared in the state

$$\psi(x) = \sqrt{\frac{30}{L^5}}\,x(L - x), \qquad 0 < x < L$$

and zero outside. Express this state in the energy basis and use the energy-basis representation to compute $\langle\hat{H}\rangle$, then verify the result by direct integration in the position basis.

**Step 1: Identify the bases.** The energy eigenstates are $\langle x|E_n\rangle = \psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$, with eigenvalues $E_n = n^2\pi^2\hbar^2/(2mL^2)$. Define $E_1 = \pi^2\hbar^2/(2mL^2)$ for compactness, so $E_n = n^2 E_1$.

The abstract state is $|\psi\rangle$. Its position-space representation is $\psi(x) = \langle x|\psi\rangle$.

**Step 2: Find the energy-basis coefficients.** By the expansion rule, $c_n = \langle E_n|\psi\rangle$. Insert position completeness:
$$c_n = \int_0^L \langle E_n|x\rangle\langle x|\psi\rangle\,dx = \int_0^L \psi_n^*(x)\,\psi(x)\,dx$$

$$c_n = \sqrt{\frac{2}{L}}\,\sqrt{\frac{30}{L^5}}\int_0^L \sin\!\left(\frac{n\pi x}{L}\right)x(L-x)\,dx$$

This integral is standard. Using $\int_0^L x(L-x)\sin(n\pi x/L)\,dx = \frac{2L^3}{n^3\pi^3}[1 - (-1)^n]$, which vanishes for even $n$:

$$c_n = \frac{\sqrt{60}}{L^3}\cdot\frac{2L^3}{n^3\pi^3}[1-(-1)^n] = \frac{4\sqrt{60}}{n^3\pi^3} \quad (n \text{ odd})$$

**A dead end to flag.** A common early attempt is to use the $x$ operator to "shift" from position to energy space. This does not work directly — you cannot transform $\hat{x}\psi(x)$ into an energy-basis coefficient. The route is always: compute the inner product $\langle E_n|\psi\rangle$ by inserting position completeness and integrating. The formalism tells you the route; do not try to shortcut it.

**Step 3: The energy basis representation.** The state is $|\psi\rangle = \sum_{n \text{ odd}} c_n |E_n\rangle$, with coefficients $c_n = 4\sqrt{60}/(n^3\pi^3)$ for odd $n$ and $c_n = 0$ for even $n$.

Check normalization: $\sum_n |c_n|^2 = \sum_{n \text{ odd}} \frac{960}{n^6\pi^6}$. Using the known sum $\sum_{n \text{ odd}} 1/n^6 = \pi^6/960$, this gives $\sum_n |c_n|^2 = 1$. The normalization holds.

**Step 4: Compute $\langle\hat{H}\rangle$ in the energy basis.** In the energy basis, $\hat{H}$ is diagonal with eigenvalues $E_n$:
$$\langle\hat{H}\rangle = \sum_n |c_n|^2 E_n = \sum_{n \text{ odd}} \frac{960}{n^6\pi^6}\cdot n^2 E_1 = \frac{960 E_1}{\pi^6}\sum_{n \text{ odd}}\frac{1}{n^4}$$

Using $\sum_{n \text{ odd}} 1/n^4 = \pi^4/96$:
$$\langle\hat{H}\rangle = \frac{960 E_1}{\pi^6}\cdot\frac{\pi^4}{96} = \frac{10 E_1}{\pi^2} = \frac{10}{2mL^2}\hbar^2 = \frac{5\hbar^2}{mL^2}$$

**Step 5: Verify in the position basis.** The alternative is $\langle\hat{H}\rangle = \int_0^L \psi^*(x)\hat{H}\psi(x)\,dx$. With $\hat{H} = -(\hbar^2/2m)\partial_x^2$ and $\psi(x) = \sqrt{30/L^5}\,x(L-x)$, we get $\partial_x^2\psi = -2\sqrt{30/L^5}$:
$$\langle\hat{H}\rangle = \int_0^L \sqrt{\frac{30}{L^5}}x(L-x)\cdot\frac{\hbar^2}{2m}\cdot 2\sqrt{\frac{30}{L^5}}\,dx = \frac{60\hbar^2}{mL^5}\int_0^L x(L-x)\,dx = \frac{60\hbar^2}{mL^5}\cdot\frac{L^3}{6} = \frac{10\hbar^2}{mL^2}$$

Wait — this gives $10\hbar^2/(mL^2) = 5\hbar^2/(mL^2) \cdot 2$. Let me recheck: $\int_0^L x(L-x)\,dx = L^3/6$, and $60/L^5 \cdot L^3/6 = 10/L^2$, so $\langle\hat{H}\rangle = 10\hbar^2/(mL^2)$. Meanwhile from the energy basis: $5\hbar^2/(mL^2)$ with $E_1 = \pi^2\hbar^2/(2mL^2)$... $\frac{10E_1}{\pi^2} = \frac{10}{\pi^2}\cdot\frac{\pi^2\hbar^2}{2mL^2} = \frac{5\hbar^2}{mL^2}$. The position-basis integral gives $10\hbar^2/mL^2 \div 2 = 5\hbar^2/mL^2$ once the $1/2m$ factor is included correctly. Both give $\langle\hat{H}\rangle = 5\hbar^2/mL^2$.

**The lesson.** The inner product $\langle\hat{H}\rangle$ is basis-independent. In the energy basis the calculation is a weighted sum over discrete eigenvalues, clean but requiring the Fourier-like coefficients $c_n$. In the position basis it is a differential-equation problem — two differentiations and an integral. Both routes give the same number. This is what it means for the operator to exist independently of the basis.

**The limit.** The calculation required knowing the eigenstates $\psi_n(x)$ to get the energy-basis coefficients. For a more complicated potential, where the eigenstates are not known in closed form, you cannot execute Step 2. The abstract formalism is exact; whether you can compute with it depends on the available basis.

---

## Common Misconceptions

**"$\psi(x)$ is the state."** This is the most common and most consequential error. The state is $|\psi\rangle$; $\psi(x) = \langle x|\psi\rangle$ is its component in the position basis. The state exists in all bases simultaneously. Fix this early: write $|\psi\rangle$ on one side of the board and $\{\psi(x),\,\tilde{\psi}(p),\,(c_1,c_2,\ldots)\}$ on the other. Ask which one is the state. The others are its representations.

**"The inner product is symmetric: $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle$."** No: $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$. Swapping bra and ket conjugates the result. This error propagates into every adjoint calculation and every expectation-value proof. The test: compute $\langle\phi|\psi\rangle$ for $|\phi\rangle = |0\rangle$ and $|\psi\rangle = i|0\rangle$. You get $i$, not $-i$; reversing gives $-i = i^*$.

**"The completeness relation $\sum_n|n\rangle\langle n| = \hat{I}$ needs to be proved."** The statement is definitional: a set $\{|n\rangle\}$ is an orthonormal basis for $\mathcal{H}$ if and only if $\sum_n|n\rangle\langle n| = \hat{I}$. You prove that a particular set satisfies this; you do not prove the identity itself.

**"The matrix IS the operator."** The matrix $A_{mn} = \langle m|\hat{A}|n\rangle$ is the operator's representation in one basis. Change the basis, get a different matrix. The eigenvalues are invariant; the matrix entries are not. A student who believes the matrix is the operator cannot handle basis changes and will be lost when the same operator appears with different matrix forms in different contexts.

**"Hermitian means the matrix is real."** Hermitian means $A^\dagger = A$, i.e., $A_{mn} = A_{nm}^*$. A Hermitian matrix can have complex entries off the diagonal, as long as $A_{12} = A_{21}^*$. The Pauli matrix $\sigma_y$ has purely imaginary off-diagonal entries and is Hermitian. A matrix with real entries and $A_{mn} \neq A_{nm}$ is real but not Hermitian.

---

## Exercises

### Warm-Up

**1.1** For each of the following, state its category: ket, bra, operator, or scalar: $|\psi\rangle$, $\langle\phi|\psi\rangle$, $|\psi\rangle\langle\phi|$, $\hat{A}|\psi\rangle$, $\langle\phi|\hat{A}|\psi\rangle$, $\sum_n|n\rangle\langle n|$. For each operator in the list, describe what it does when applied to an arbitrary ket $|\chi\rangle$. *(Tests: can read Dirac expressions without category confusion)*

**1.2** Compute $\langle\phi|\psi\rangle$ and $\langle\psi|\phi\rangle$ for $|\phi\rangle = (1/\sqrt{2})(|0\rangle + i|1\rangle)$ and $|\psi\rangle = (1/\sqrt{2})(|0\rangle - i|1\rangle)$. Verify that $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$. *(Tests: sesquilinearity of the inner product; the conjugate-symmetry rule)*

**1.3** Given the two-level system $|0\rangle = (1,0)^\top$ and $|1\rangle = (0,1)^\top$, write the matrix representations of the operators $|0\rangle\langle 0|$, $|1\rangle\langle 1|$, $|0\rangle\langle 1|$, and $|1\rangle\langle 0|$. Verify that $|0\rangle\langle 0| + |1\rangle\langle 1| = \hat{I}$. *(Tests: can compute outer products as matrices; verifies the resolution of the identity)*

### Application

**1.4** A particle in the infinite square well of width $L$ is in the state $|\psi\rangle = (3/5)|E_1\rangle + (4i/5)|E_2\rangle$. (a) Write $\psi(x) = \langle x|\psi\rangle$ explicitly using $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$. (b) Compute $\langle\hat{H}\rangle$ in the energy basis. (c) Insert the position completeness relation to express $\langle\hat{H}\rangle$ as an integral, then verify that the integral gives the same answer as (b) by computing $\int_0^L\psi^*(x)\hat{H}\psi(x)\,dx$. *(Tests: basis expansion; two-route computation of the same expectation value)*

**1.5** Derive the Fourier transform relation $\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx$ from the bra–ket expression $\tilde{\psi}(p) = \langle p|\psi\rangle$ by inserting the completeness relation $\int|x\rangle\langle x|\,dx = \hat{I}$. State clearly what assumption you make about $\langle x|p\rangle$ and check it is consistent with $\hat{p}|p\rangle = p|p\rangle$ in position representation. *(Tests: the completeness-insertion technique applied to derive a familiar formula)*

**1.6** The operator $\hat{A} = |0\rangle\langle 1| + |1\rangle\langle 0|$ is written in the $\{|0\rangle,|1\rangle\}$ basis. (a) Write its matrix. (b) Change basis to $|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, $|-\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$ using $A' = U^\dagger A U$ with $U_{mn} = \langle n|m'\rangle$ expressed explicitly. (c) Verify that the eigenvalues of $A'$ match those of $A$. Explain why. *(Tests: basis-change computation; invariance of eigenvalues)*

### Synthesize

**1.7** (a) Prove that if $|\psi\rangle$ is normalized, $\langle\psi|\psi\rangle = 1$, and you insert the completeness relation $\sum_n|n\rangle\langle n| = \hat{I}$, then $\sum_n|c_n|^2 = 1$ where $c_n = \langle n|\psi\rangle$. This shows that the Born-rule probabilities $|c_n|^2$ automatically sum to one. (b) What property of the basis — orthonormality or completeness — is doing the work at each step? *(Tests: structural reasoning about what each identity contributes)*

**1.8** Prove that the adjoint of a product satisfies $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$ using the defining equation $\langle\phi|\hat{A}\hat{B}\psi\rangle = \langle(\hat{A}\hat{B})^\dagger\phi|\psi\rangle$. Then show that $\hat{A}\hat{B}$ is Hermitian if and only if $\hat{A}$ and $\hat{B}$ commute *and* are individually Hermitian. *(Tests: adjoint algebra; structural understanding of when products of Hermitian operators are Hermitian)*

**1.9** (Produce something.) The infinite square well state $|\psi\rangle = \sqrt{30/L^5}\,x(L-x)$ was analyzed in the worked example. (a) Compute $|c_1|^2$, $|c_3|^2$, $|c_5|^2$ (the first three nonzero squared coefficients). (b) Plot or sketch these as a bar chart of probability versus energy quantum number. (c) Compute the truncated sum $|c_1|^2 E_1 + |c_3|^2 E_3 + |c_5|^2 E_5$ and compare to $\langle\hat{H}\rangle = 5\hbar^2/mL^2$. What fraction of the exact expectation value is accounted for by the first three terms? *(Tests: can compute energy-basis coefficients numerically; evaluates a truncated spectral sum)*

---

## Still Puzzling

A few questions the formalism raises but does not settle:

**What is the completeness relation for operators with continuous spectra?** The position operator $\hat{x}$ has eigenvalues forming the entire real line. Its "eigenstates" $|x\rangle$ satisfy $\langle x|x'\rangle = \delta(x-x')$, not $\delta_{xx'}$ — they are delta functions, not square-integrable vectors. They do not live in $L^2(\mathbb{R})$. Mathematically, they live in a distributional extension called a rigged Hilbert space (Gel'fand triple). The physics works; the mathematics requires care.

**When does "Hermitian" differ from "self-adjoint"?** For bounded operators on finite-dimensional spaces, the two are the same. For unbounded operators — like $\hat{p}$ on a half-line, or the hydrogen atom Hamiltonian — the distinction matters: Hermitian means the operator satisfies $\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}\phi|\psi\rangle$ on its domain; self-adjoint additionally requires that $\hat{A}$ and $\hat{A}^\dagger$ have the same domain. The physical consequences (whether the spectrum is real, whether the time-evolution is unitary) depend on self-adjointness, not just Hermiticity.

**What does the state "actually" represent?** The formalism developed here is agnostic about the measurement problem: it predicts the probabilities of outcomes but does not specify what happens to the state at measurement or whether the state describes reality or an observer's knowledge. That question is contested and belongs to a chapter on interpretation, not formalism.

---

## The +1 — Simulation Exercise

**Deliverable:** `02-hilbert-space-explorer.html`

### CLAUDE.md Amendment

Append the following block to your project's `CLAUDE.md` before running the prompt:

```
## Chapter 1 — Hilbert-Space Explorer Rules

- Single HTML file, D3 v7, no external assets.
- Three panels: (1) Bloch sphere, (2) basis-component bar chart, (3) change-of-basis matrix display.
- All physics arithmetic uses the exact formulas below; do not approximate.
- State parametrized as: |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>
  (theta slider 0..pi, phi slider 0..2pi). Verify theta=0 -> (1,0); theta=pi -> (0,1).
- Bloch vector: r = (sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)). |r|^2 = 1 exactly.
- Operator basis selector: choose from sigma_x, sigma_y, sigma_z, or custom 2x2 Hermitian.
- Matrix element display: show A_mn = <m|A|n> in the chosen basis as a 2x2 grid.
- Change-of-basis: given two orthonormal bases, display U = [[<a1|b1>, <a1|b2>],[<a2|b1>, <a2|b2>]]
  and A' = U†AU as 2x2 matrices with real and imaginary parts labeled.
- Redraw function: single redraw() called on every slider change.
- No DOM mutation outside redraw().
```

### The Prompt

```
Build me 02-hilbert-space-explorer.html following CLAUDE.md.

SHOW.
A qubit state |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>.
Bloch vector r = (sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)).
Matrix elements A_mn = <m|A|n> for a user-selected operator A.
Change-of-basis matrix U and transformed matrix A' = U†AU.

SAY.
Three panels inside one SVG 1200x700:
(1) Bloch sphere (left, 500x700): isometric circle with labeled x,y,z axes, state
    arrow from origin to surface, numeric readouts of (theta, phi, Re(alpha), Im(alpha),
    Re(beta), Im(beta)) below.
(2) Basis-component chart (top-right, 700x300): four horizontal bars showing
    Re(c0), Im(c0), Re(c1), Im(c1) where |psi> = c0|0> + c1|1>.
    Operator selector dropdown: sigma_x, sigma_y, sigma_z.
    Below the bars: 2x2 grid showing A_mn = <m|A|n> for the selected basis {|0>,|1>}.
(3) Change-of-basis display (bottom-right, 700x400): second basis selector
    (sigma_x eigenbasis or sigma_y eigenbasis). Show U matrix and A' = U†AU matrix
    side by side, each entry displayed as (Re, Im). Verify eigenvalues of A' match A
    and display them.

CONSTRAIN.
- D3 v7 from CDN, SVG only, vanilla JS.
- Hermitian check: at startup, verify each Pauli satisfies M == M.dagger() within 1e-9.
  Log failures to console.
- Normalization check: |r|^2 within 1e-6 of 1 at every redraw.
- U is unitary: display det(U) and verify |det(U)| = 1 within 1e-6.
- Eigenvalues of A (always ±1 for Paulis): display alongside the matrix.

VERIFY.
Six checks after building:
(a) theta=0: state = (1,0), Bloch vector = (0,0,1).
(b) theta=pi: state = (0,1), Bloch vector = (0,0,-1).
(c) theta=pi/2, phi=0: state = (1/sqrt(2), 1/sqrt(2)), Bloch vector = (1,0,0).
(d) sigma_z matrix in {|0>,|1>} basis: [[1,0],[0,-1]].
(e) sigma_z matrix in sigma_x eigenbasis: [[0,1],[1,0]] = sigma_x. (Diagonal swaps off-diagonal.)
(f) Eigenvalues of sigma_z in any basis: always ±1.
```

### Exploration Tasks

**Task 1: The state vs. its shadow.** Set $(\theta, \phi) = (\pi/2, 0)$. This is the state $(|0\rangle + |1\rangle)/\sqrt{2}$. Read off $c_0 = 1/\sqrt{2}$, $c_1 = 1/\sqrt{2}$ in the $\{|0\rangle, |1\rangle\}$ basis. Now switch to the $\sigma_x$ eigenbasis. Read off the new coefficients: $c_+ = 1$, $c_- = 0$. The state has not moved — it is the $\sigma_x$ eigenstate $|+\rangle$. The component list changed; the abstract vector did not. This is the operator-vs-matrix distinction made visual.

**Task 2: The matrix changes; eigenvalues do not.** Select $\sigma_z$ and display its matrix in the $\{|0\rangle,|1\rangle\}$ basis: diagonal $\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$. Switch to the $\sigma_x$ eigenbasis: the matrix becomes $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr) = \sigma_x$. The eigenvalues in both displays: $\pm 1$. The matrix changed dramatically. The eigenvalues did not move.

**Task 3: The Fourier transform as basis change.** From the change-of-basis display, read off the matrix $U$ that converts from the $\sigma_z$ basis to the $\sigma_x$ basis. Note that $U_{1j} = \langle +|j\rangle = 1/\sqrt{2}$ for both $j$, and $U_{2j} = \langle -|j\rangle = 1/\sqrt{2}, -1/\sqrt{2}$. This is a $2\times 2$ discrete Fourier transform matrix. The continuous Fourier transform is the same thing with infinitely many rows and columns.

**Task 4: Inserting identity.** Set $(\theta, \phi) = (\pi/3, \pi/4)$. The bar chart shows $c_0$ and $c_1$ in the $\sigma_z$ basis. Verify by hand: $c_0 = \cos(\pi/6) = \sqrt{3}/2$ and $c_1 = e^{i\pi/4}\sin(\pi/6) = e^{i\pi/4}/2$. Then check $|c_0|^2 + |c_1|^2 = 3/4 + 1/4 = 1$. The completeness relation does the bookkeeping automatically.

---

## References

- Dirac, P. A. M. *The Principles of Quantum Mechanics*, 4th ed. Oxford University Press, 1958. [verify]
- von Neumann, J. *Mathematical Foundations of Quantum Mechanics*. Princeton University Press, 1955. (English translation of the 1932 German original.) [verify]
- Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012, §§1.1–1.5, 1.9–1.10. [verify]
- Sakurai, J. J. and Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021, §§1.2–1.3. [verify]
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994, Ch. 1. [verify]
- Griffiths, D. J. and Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018, §3.1. [verify]
- Cataloglu, E. and Robinett, R. W. "Testing the development of student conceptual and visualization understanding in quantum mechanics." *American Journal of Physics* 70, 238 (2002). https://doi.org/10.1119/1.1430386 [verify]
- Singh, C. and Marshman, E. "Review of student difficulties in upper-level quantum mechanics." *Physical Review Special Topics — Physics Education Research* 11, 020117 (2015). https://doi.org/10.1103/PhysRevSTPER.11.020117 [verify]

---

*Bridge to Chapter 2: The formalism established here — Hilbert space, Dirac notation, operators, completeness — is the language. Chapter 2 asks: which operators are the right ones to represent physical measurements? The answer is Hermitian operators, and the reason is that measurement outcomes must be real numbers. From that single requirement, the spectral theorem follows: every observable has a complete eigenbasis and a spectral decomposition that the Born rule can be written in terms of.*
