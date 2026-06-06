# Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

The wave function $\psi(x)$ gives the probability amplitude for finding a particle at position $x$. Its Fourier transform $\tilde{\psi}(p)$ gives the probability amplitude for finding that same particle with momentum $p$. Both functions carry exactly the same physical information — each is a complete description of the quantum state — and yet they can look entirely different from one another. One might be sharply peaked while the other spreads out and oscillates. A Gaussian in position stays Gaussian in momentum, but a step function in position becomes a sinc function in momentum.

Neither representation deserves to be called "the state" in any privileged sense. The wave function $\psi(x)$ is not the state itself. It is what the state looks like when we describe it in one particular basis. The Fourier transform $\tilde{\psi}(p)$ is what that same state looks like in a different basis. The state — the genuine physical object — sits above both descriptions at once. Compare it to a vector in ordinary three-dimensional space: its numerical coordinates differ between Cartesian and spherical systems, but the vector itself does not budge when we switch coordinate systems.

So far, every calculation in wave mechanics has been carried out in a single basis, usually position. The formalism we develop in this chapter lets us write the physics once, in basis-free language, and then evaluate it in whatever basis happens to be convenient.

---

## The Arena

A **Hilbert space** $\mathcal{H}$ is a complete complex inner-product space. The two words that carry the weight are *complex* and *inner product*. In such a space we can add vectors, scale them by complex numbers, and compute inner products. That is the whole structure, and we will not need more.

The word *complex* is doing real work. We can multiply a state by any $c \in \mathbb{C}$ and it remains a valid state. The inner product is **sesquilinear**, which means it is linear in the second argument but conjugate-linear in the first:

$$\langle(a|\phi_1\rangle + b|\phi_2\rangle)|\psi\rangle = a^*\langle\phi_1|\psi\rangle + b^*\langle\phi_2|\psi\rangle.$$

It is also conjugate-symmetric rather than symmetric:

$$\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*.$$

Exchanging the bra and the ket conjugates the answer. In a real vector space the inner product is symmetric and we may swap the two factors freely; in a Hilbert space we cannot. That conjugate sign is the quiet source of countless errors in adjoint calculations and confused steps in Hermiticity proofs, so it pays to learn it thoroughly.

The dimension can be finite or infinite. A qubit lives in $\mathbb{C}^2$. The states of a particle moving along a line live in $L^2(\mathbb{R})$, the space of square-integrable complex functions. The same abstract framework covers both cases without any change.

---

## Kets, Bras, and What They Are

Dirac's notation has the useful property of keeping the different categories of object plainly visible.

A **ket** $|\psi\rangle$ is a vector in $\mathcal{H}$. It is helpful to picture it as a column vector.

A **bra** $\langle\phi|$ is a linear functional on $\mathcal{H}$ — a rule that sends any ket to a complex number. Each ket $|\phi\rangle$ comes paired with a bra $\langle\phi|$, defined by $\langle\phi|: |\psi\rangle \mapsto \langle\phi|\psi\rangle$. It is helpful to picture this as a row vector, the conjugate transpose of the column.

The bra paired with $c|\phi\rangle$ is $c^*\langle\phi|$. That complex conjugate is not an extra rule we have to remember; it follows directly from the definition of the inner product.

The bracket $\langle\phi|\psi\rangle$ is a **scalar**, an ordinary complex number. Written in the opposite order, $|\psi\rangle\langle\phi|$ is an **operator** — the rule that sends any $|\chi\rangle$ to $\langle\phi|\chi\rangle\,|\psi\rangle$. Inner product gives a scalar; outer product gives an operator. These belong to genuinely different categories, and an expression that confuses one for the other is wrong in two ways at the same time.

---

## Three Identities

Choose an orthonormal basis $\{|n\rangle\}$ for $\mathcal{H}$. Three identities then carry us through nearly everything.

**Completeness:**
$$\sum_n |n\rangle\langle n| = \hat{I}.$$

This is nothing more than the number 1, dressed up as an operator. In the continuous position basis it becomes an integral: $\int |x\rangle\langle x|\,dx = \hat{I}$.

**Orthonormality:**
$$\langle m|n\rangle = \delta_{mn}.$$

In the position basis: $\langle x|x'\rangle = \delta(x-x')$.

**Expansion:**
$$|\psi\rangle = \sum_n c_n|n\rangle, \qquad c_n = \langle n|\psi\rangle.$$

The coefficient $c_n$ is the projection of the abstract vector onto the $n$-th basis direction. Switch to a different basis and the numbers change, but the vector itself stays put.

Completeness is the workhorse of the three. Slipping the identity $\hat{I}$ between any two expressions turns abstract inner products into concrete sums or integrals:

$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|n\rangle\langle n|\psi\rangle = \sum_n \phi_n^* \psi_n.$$

In the position basis this reads $\int\phi^*(x)\psi(x)\,dx$. So the abstract inner product and the familiar wave-function overlap integral are simply two faces of the same quantity.

---

## The Fourier Transform Is a Basis Change

The quantum state of a particle on a line is a unit vector $|\psi\rangle$ in $L^2(\mathbb{R})$. Two convenient bases are the position eigenstates $\{|x\rangle\}$ and the momentum eigenstates $\{|p\rangle\}$.

The position-space wave function is $\psi(x) = \langle x|\psi\rangle$.

The momentum-space wave function is $\tilde{\psi}(p) = \langle p|\psi\rangle$.

These are two representations of one and the same vector — a single state seen in two different bases.

Now insert the position completeness relation into $\tilde{\psi}(p)$:

$$\tilde{\psi}(p) = \langle p|\psi\rangle = \int\langle p|x\rangle\langle x|\psi\rangle\,dx = \int\langle p|x\rangle\,\psi(x)\,dx.$$

All that remains is to identify $\langle p|x\rangle$. The momentum eigenstate, written in position space, obeys $\hat{p}|p\rangle = p|p\rangle$, that is, $-i\hbar\,\partial_x\langle x|p\rangle = p\langle x|p\rangle$, which gives $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Hence $\langle p|x\rangle = e^{-ipx/\hbar}/\sqrt{2\pi\hbar}$, and:

$$\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx.$$

This is the Fourier transform. We did not have to borrow it from analysis; it dropped out of the completeness relation together with one differential equation. Whenever a Fourier transform shows up in quantum mechanics, what we are really watching is a change of basis.

The position and momentum representations hold exactly the same physics. Neither one is more fundamental than the other. We simply work in whichever one makes the calculation easier.

---

## Operators: Abstract Maps, Not Matrices

A **linear operator** $\hat{A}$ is a linear map $\mathcal{H} \to \mathcal{H}$. It exists on its own, with no reference to any basis.

Once we pick a basis $\{|n\rangle\}$, the operator acquires a matrix representation:

$$A_{mn} = \langle m|\hat{A}|n\rangle.$$

A different basis yields a different matrix, but the operator is the same operator. This is the central distinction of the chapter.

The position operator $\hat{x}$ makes the point cleanly. In the position basis, $\hat{x}$ acts by multiplication, so its matrix is diagonal. In the energy basis of the harmonic oscillator, the very same operator $\hat{x}$ has tridiagonal matrix elements involving $\sqrt{n}$. One operator, two matrices that look nothing alike. The matrices are byproducts of the basis we chose; the operator is not.

The **adjoint** $\hat{A}^\dagger$ is defined by:

$$\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle \quad \text{for all }|\psi\rangle, |\phi\rangle.$$

In matrix form, $(A^\dagger)_{mn} = A_{nm}^*$ — the conjugate transpose. An operator is **Hermitian** when $\hat{A}^\dagger = \hat{A}$, that is, when $A_{mn} = A_{nm}^*$. A worthwhile example to keep in mind is $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Its plain transpose is $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$, which is antisymmetric. But its conjugate transpose is $+\sigma_y$, which is Hermitian. The factor of $i$ is what makes the difference. A matrix can carry complex off-diagonal entries and still be Hermitian, provided $A_{12} = A_{21}^*$. The slogan "Hermitian means symmetric" is a habit carried over from real linear algebra, and in the complex case it simply does not hold.

The adjoint reverses the order of a product: $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$. The proof is a single line from the definition, but the rule is essential whenever we manipulate products of operators.

Changing basis from $\{|a_n\rangle\}$ to $\{|b_m\rangle\}$ is carried out by the unitary matrix $U_{mn} = \langle a_m|b_n\rangle$, which transforms operator matrices as $O' = U^\dagger O U$. The eigenvalues of $O'$ match those of $O$ exactly. The physics is basis-independent. The matrix is the observer's description; the operator is the thing being described.

---

## Worked Example — A State in the Energy Basis

Suppose a particle sits in an infinite square well of width $L$, prepared in the state

$$\psi(x) = \sqrt{\frac{30}{L^5}}\,x(L-x), \qquad 0 < x < L.$$

The energy eigenstates are $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with eigenvalues $E_n = n^2 E_1$, where $E_1 = \pi^2\hbar^2/(2mL^2)$. We will compute $\langle\hat{H}\rangle$ by two different routes and watch them agree.

**Energy basis route.** The expansion coefficients are $c_n = \langle E_n|\psi\rangle = \int_0^L\psi_n^*(x)\psi(x)\,dx$. Using the standard integral $\int_0^L x(L-x)\sin(n\pi x/L)\,dx = 2L^3/(n^3\pi^3)\cdot[1-(-1)^n]$, which vanishes for even $n$:

$$c_n = \frac{4\sqrt{60}}{n^3\pi^3} \quad (n \text{ odd}), \qquad c_n = 0 \quad (n \text{ even}).$$

Check normalization: $\sum_{n\,\text{odd}}|c_n|^2 = 960/\pi^6 \cdot \sum_{n\,\text{odd}}1/n^6$. The sum $\sum_{n\,\text{odd}}1/n^6 = \pi^6/960$, so $\sum|c_n|^2 = 1$.

In the energy basis $\hat{H}$ is diagonal, so:

$$\langle\hat{H}\rangle = \sum_{n\,\text{odd}}|c_n|^2 E_n = \frac{960 E_1}{\pi^6}\sum_{n\,\text{odd}}\frac{1}{n^4} = \frac{960 E_1}{\pi^6}\cdot\frac{\pi^4}{96} = \frac{10 E_1}{\pi^2} = \frac{5\hbar^2}{mL^2}.$$

**Position basis route.** With $\hat{H} = -(\hbar^2/2m)\partial_x^2$ and $\partial_x^2\psi = -2\sqrt{30/L^5}$:

$$\langle\hat{H}\rangle = \frac{\hbar^2}{m}\sqrt{\frac{30}{L^5}}\int_0^L x(L-x)\,dx\cdot\sqrt{\frac{30}{L^5}} = \frac{60\hbar^2}{mL^5}\cdot\frac{L^3}{6} = \frac{10\hbar^2}{mL^2}\cdot\frac{1}{2} = \frac{5\hbar^2}{mL^2}.$$

The two routes give the same number, as they must: the expectation value does not depend on the basis. In the energy basis the work is a weighted discrete sum; in the position basis it is two derivatives and an integral. Both arrive at the same answer, and that is exactly what it means for the operator to exist independently of any basis.

One limitation is worth naming. This calculation leaned on knowing the eigenstates $\psi_n(x)$ in closed form. For a more complicated potential, where the eigenstates cannot be written down analytically, the energy-basis route is no longer available to us. The abstract formalism remains exact; whether we can actually compute with it depends on whether we have a usable basis in hand.

---

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
````

### The Prompt

````
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
(e) sigma_z matrix in sigma_x eigenbasis: [[0,1],[1,0]] = sigma_x.
(f) Eigenvalues of sigma_z in any basis: always ±1.
````

### Exploration Tasks

**Task 1 — The state vs. its shadow.** Set $(\theta, \phi) = (\pi/2, 0)$. The state is $(|0\rangle + |1\rangle)/\sqrt{2}$. Read off $c_0 = c_1 = 1/\sqrt{2}$ in the $\{|0\rangle, |1\rangle\}$ basis. Switch to the $\sigma_x$ eigenbasis. The new coefficients: $c_+ = 1$, $c_- = 0$. The state did not move — it is the $\sigma_x$ eigenstate $|+\rangle$. The component list changed; the abstract vector did not. This is the operator-versus-matrix distinction made visual.

**Task 2 — The matrix changes; eigenvalues do not.** Select $\sigma_z$ and display its matrix in the $\{|0\rangle, |1\rangle\}$ basis: diagonal $\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$. Switch to the $\sigma_x$ eigenbasis: the matrix becomes $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$. Both displays show eigenvalues $\pm 1$. The matrix changed dramatically. The physics did not.

**Task 3 — The Fourier transform as basis change.** Read off the matrix $U$ that converts from the $\sigma_z$ basis to the $\sigma_x$ basis. Note $U_{1j} = 1/\sqrt{2}$ for both $j$; the second row is $1/\sqrt{2}, -1/\sqrt{2}$. This is a $2\times 2$ discrete Fourier matrix. The continuous Fourier transform is the same structure with infinitely many rows and columns.

**Task 4 — Inserting identity.** Set $(\theta, \phi) = (\pi/3, \pi/4)$. The bar chart shows $c_0 = \cos(\pi/6) = \sqrt{3}/2$ and $c_1 = e^{i\pi/4}\sin(\pi/6) = e^{i\pi/4}/2$. Verify $|c_0|^2 + |c_1|^2 = 3/4 + 1/4 = 1$. The completeness relation handles the bookkeeping automatically.

---

## References

- Dirac, P.A.M. *The Principles of Quantum Mechanics*, 4th ed. Oxford University Press, 1958.
- von Neumann, J. *Mathematical Foundations of Quantum Mechanics*. Princeton University Press, 1955.
- Townsend, J.S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012, §§1.1–1.5.
- Sakurai, J.J. and Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021, §§1.2–1.3.
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994, Ch. 1.
- Griffiths, D.J. and Schroeter, D.F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018, §3.1.
- Cataloglu, E. and Robinett, R.W. "Testing the development of student conceptual and visualization understanding in quantum mechanics." *American Journal of Physics* 70, 238 (2002). https://doi.org/10.1119/1.1430386
- Singh, C. and Marshman, E. "Review of student difficulties in upper-level quantum mechanics." *Physical Review Special Topics — Physics Education Research* 11, 020117 (2015). https://doi.org/10.1103/PhysRevSTPER.11.020117

