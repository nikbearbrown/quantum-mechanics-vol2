# Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

Start with a small irritation.

You already know that $\psi(x)$ gives the amplitude to find a particle at position $x$, and that its Fourier transform $\tilde{\psi}(p)$ gives the amplitude to find that *same* particle carrying momentum $p$. No information is lost going from one to the other; each, by itself, pins down the state completely. And yet the two functions can look like total strangers. One is sharp and localized while the other spreads out and rings. A Gaussian happens to stay a Gaussian under the transform, but that is a coincidence of that one shape — feed in a step and you get a sinc back.

So: which of the two *is* the state?

The honest answer is neither. $\psi(x)$ is not the state — it is what the state looks like once you have committed to the position basis. $\tilde{\psi}(p)$ is what the very same state looks like in the momentum basis. The state itself sits one level up, indifferent to your choice, the way a vector in ordinary space keeps its identity while its Cartesian and spherical coordinates report wildly different numbers. The arrow does not budge when you swap rulers.

Up to now, every wave-mechanics calculation you have done has secretly been a calculation in one fixed basis — usually position. The machinery in this chapter cuts that cord: write the physics once, abstractly, then cash it out in whatever basis makes the arithmetic least painful.

---

## The Arena

A **Hilbert space** $\mathcal{H}$ is a complete complex inner-product space. Two words carry the load: *complex*, and *inner product*. You may add vectors, multiply them by complex numbers, and take inner products. Nothing more is on offer, and nothing more is needed.

That the scalars are complex is not decoration. Any state may be multiplied by an arbitrary $c \in \mathbb{C}$ and remains a perfectly good state. The price is that the inner product is **sesquilinear** — ordinary linearity in the second slot, but conjugate-linearity in the first:

$$\langle(a|\phi_1\rangle + b|\phi_2\rangle)|\psi\rangle = a^*\langle\phi_1|\psi\rangle + b^*\langle\phi_2|\psi\rangle.$$

And it is conjugate-symmetric, not symmetric:

$$\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*.$$

Trade the bra for the ket and you pick up a complex conjugate. Over the reals the inner product is symmetric and the order never matters; here it does. That stray conjugate is the silent author of nearly every sign slip in an adjoint manipulation and every stalled Hermiticity proof. Memorize it.

Dimension is left open — finite or infinite, the framework does not care. A qubit lives in $\mathbb{C}^2$; a particle on a line lives in $L^2(\mathbb{R})$, the square-integrable complex functions. One set of rules covers both.

---

## Kets, Bras, and What They Are

Dirac's notation earns its keep by refusing to let you blur the categories.

A **ket** $|\psi\rangle$ is a genuine vector in $\mathcal{H}$ — picture a column.

A **bra** $\langle\phi|$ is a linear functional: hand it a ket, it returns a complex number. Each ket $|\phi\rangle$ comes paired with a bra $\langle\phi|$, the rule being $\langle\phi|: |\psi\rangle \mapsto \langle\phi|\psi\rangle$. Picture a row — the conjugate transpose of the column.

Note that the bra belonging to $c|\phi\rangle$ is $c^*\langle\phi|$, not $c\langle\phi|$. The conjugate is not something you remember to insert; it is forced on you by the inner product itself.

Now watch the order. The bracket $\langle\phi|\psi\rangle$ is a **scalar**, a single complex number. Reverse the factors and $|\psi\rangle\langle\phi|$ becomes an **operator** — the map sending any $|\chi\rangle$ to $\langle\phi|\chi\rangle\,|\psi\rangle$. Inner product, a number; outer product, an operator. They are not the same kind of thing, and an expression that confuses them is broken twice over.

---

## Three Identities

Pick an orthonormal basis $\{|n\rangle\}$ for $\mathcal{H}$. Almost everything you will ever do reduces to three statements.

**Completeness:**
$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Read this as the number 1 wearing operator clothing. In the continuous position basis the sum becomes an integral: $\int |x\rangle\langle x|\,dx = \hat{I}$.

**Orthonormality:**
$$\langle m|n\rangle = \delta_{mn}.$$

For position: $\langle x|x'\rangle = \delta(x-x')$.

**Expansion:**
$$|\psi\rangle = \sum_n c_n|n\rangle, \qquad c_n = \langle n|\psi\rangle.$$

The number $c_n$ is just how much of the abstract vector points along the $n$-th basis direction. Pick a different basis and the list of numbers changes; the vector itself never stirs.

The workhorse is completeness. Slip $\hat{I}$ in between two objects and an abstract inner product collapses into an honest sum or integral you can actually evaluate:

$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|n\rangle\langle n|\psi\rangle = \sum_n \phi_n^* \psi_n.$$

In the position basis this is $\int\phi^*(x)\psi(x)\,dx$. So the abstract inner product and the wave-function overlap you have been computing all along are one and the same.

---

## The Fourier Transform Is a Basis Change

A particle on a line is a unit vector $|\psi\rangle$ in $L^2(\mathbb{R})$. Two bases are worth keeping handy: the position eigenstates $\{|x\rangle\}$ and the momentum eigenstates $\{|p\rangle\}$.

Position-space wave function: $\psi(x) = \langle x|\psi\rangle$.

Momentum-space wave function: $\tilde{\psi}(p) = \langle p|\psi\rangle$.

Same vector, two bookkeeping schemes — that is the entire content.

Now slide the position completeness relation into $\tilde{\psi}(p)$:

$$\tilde{\psi}(p) = \langle p|\psi\rangle = \int\langle p|x\rangle\langle x|\psi\rangle\,dx = \int\langle p|x\rangle\,\psi(x)\,dx.$$

Everything hinges on one object, $\langle p|x\rangle$. The momentum eigenstate, written in position space, obeys $\hat{p}|p\rangle = p|p\rangle$, i.e. $-i\hbar\,\partial_x\langle x|p\rangle = p\langle x|p\rangle$, whose solution is $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Conjugating gives $\langle p|x\rangle = e^{-ipx/\hbar}/\sqrt{2\pi\hbar}$, and so:

$$\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx.$$

There is the Fourier transform — not summoned from a textbook on analysis, but extracted from the completeness relation and a single first-order ODE. Wherever a Fourier transform turns up in quantum mechanics, what you are really watching is a change of basis.

The position and momentum pictures hold exactly the same physics; neither outranks the other. You work in whichever one makes the integral surrender faster.

---

## Operators: Abstract Maps, Not Matrices

A **linear operator** $\hat{A}$ is a linear map $\mathcal{H} \to \mathcal{H}$, defined with no reference to any basis whatsoever.

Choose a basis $\{|n\rangle\}$ and the operator acquires a matrix:

$$A_{mn} = \langle m|\hat{A}|n\rangle.$$

New basis, new matrix; throughout, the same operator. This is the distinction the whole chapter turns on.

The position operator $\hat{x}$ makes the point with no room for argument. In the position basis it acts by plain multiplication and its matrix is diagonal. In the energy basis of the harmonic oscillator that identical operator $\hat{x}$ shows up tridiagonal, its entries laced with $\sqrt{n}$. One operator, two matrices that share nothing visually. The matrices are souvenirs of the basis you picked; the operator owes them nothing.

The **adjoint** $\hat{A}^\dagger$ is fixed by:

$$\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle \quad \text{for all }|\psi\rangle, |\phi\rangle.$$

As a matrix this reads $(A^\dagger)_{mn} = A_{nm}^*$ — conjugate, then transpose. An operator is **Hermitian** when $\hat{A}^\dagger = \hat{A}$, i.e. $A_{mn} = A_{nm}^*$. Keep one example permanently loaded: $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Its bare transpose is $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$, antisymmetric and apparently disqualified. But conjugate first and the transpose lands back on $+\sigma_y$ — Hermitian after all. The $i$ is doing the heavy lifting. A matrix can carry complex off-diagonal entries and stay Hermitian, provided $A_{12} = A_{21}^*$. The reflex "Hermitian means symmetric" is a habit imported from real linear algebra, and over the complex numbers it is simply false.

The adjoint also flips product order: $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$ — a one-line consequence of the definition, but you will lean on it every time operators get multiplied.

Switching from a basis $\{|a_n\rangle\}$ to $\{|b_m\rangle\}$ is carried out by the unitary matrix $U_{mn} = \langle a_m|b_n\rangle$, which sends operator matrices to $O' = U^\dagger O U$. The eigenvalues of $O'$ match those of $O$ exactly. The physics is basis-independent. The matrix is your description of the thing; the operator is the thing.

---

## Worked Example — A State in the Energy Basis

What follows is the cleanest demonstration that an expectation value belongs to the operator, not to the basis: compute the same number by two routes that share no intermediate step.

A particle is in an infinite square well of width $L$, prepared in the state

$$\psi(x) = \sqrt{\frac{30}{L^5}}\,x(L-x), \qquad 0 < x < L.$$

The energy eigenstates are $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with eigenvalues $E_n = n^2 E_1$, where $E_1 = \pi^2\hbar^2/(2mL^2)$. Compute $\langle\hat{H}\rangle$ two ways.

**Energy basis route.** The expansion coefficients are $c_n = \langle E_n|\psi\rangle = \int_0^L\psi_n^*(x)\psi(x)\,dx$. Using the standard integral $\int_0^L x(L-x)\sin(n\pi x/L)\,dx = 2L^3/(n^3\pi^3)\cdot[1-(-1)^n]$, which vanishes for even $n$:

$$c_n = \frac{4\sqrt{60}}{n^3\pi^3} \quad (n \text{ odd}), \qquad c_n = 0 \quad (n \text{ even}).$$

Check normalization: $\sum_{n\,\text{odd}}|c_n|^2 = 960/\pi^6 \cdot \sum_{n\,\text{odd}}1/n^6$. The sum $\sum_{n\,\text{odd}}1/n^6 = \pi^6/960$, so $\sum|c_n|^2 = 1$.

In the energy basis $\hat{H}$ is diagonal, so:

$$\langle\hat{H}\rangle = \sum_{n\,\text{odd}}|c_n|^2 E_n = \frac{960 E_1}{\pi^6}\sum_{n\,\text{odd}}\frac{1}{n^4} = \frac{960 E_1}{\pi^6}\cdot\frac{\pi^4}{96} = \frac{10 E_1}{\pi^2} = \frac{5\hbar^2}{mL^2}.$$

**Position basis route.** With $\hat{H} = -(\hbar^2/2m)\partial_x^2$ and $\partial_x^2\psi = -2\sqrt{30/L^5}$:

$$\langle\hat{H}\rangle = \frac{\hbar^2}{m}\sqrt{\frac{30}{L^5}}\int_0^L x(L-x)\,dx\cdot\sqrt{\frac{30}{L^5}} = \frac{60\hbar^2}{mL^5}\cdot\frac{L^3}{6} = \frac{10\hbar^2}{mL^2}\cdot\frac{1}{2} = \frac{5\hbar^2}{mL^2}.$$

The same number drops out. The expectation value does not know which basis you used to extract it. One route was a weighted sum over a discrete spectrum; the other was two derivatives and an integral. Both land on $5\hbar^2/mL^2$ — which is exactly what it means for the operator to live above the basis.

One caveat worth flagging: the energy-basis route demanded the eigenstates $\psi_n(x)$ in closed form. Throw a messier potential at it, one whose eigenstates resist any analytic formula, and that route simply stalls. The formalism stays exact; whether you can *compute* with it is a separate question, decided by which basis you can actually write down.

---

## The +1 — Simulation Exercise

**Deliverable:** `02-hilbert-space-explorer.html`

### CLAUDE.md Amendment

Append the following block to your project's `CLAUDE.md` before running the prompt:

````markdown
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

---

## Running Project — Build the Atom

**This chapter adds:** the state-representation layer — a data structure in which each atomic orbital is an abstract basis ket $|n\ell m_\ell m_s\rangle$ and every operator (energy, $\hat{L}_z$, occupation) is a matrix in that basis, so the rest of the simulator can be written once and evaluated in whatever basis is convenient.

By the final chapter you will have built a program that takes an element's atomic number $Z$ and predicts its ground-state electron configuration, effective nuclear charge $Z_\text{eff}$, and term symbol, then checks those predictions against real spectroscopic data (iron's $^5D_4$). Everything downstream needs a clean way to *name* and *store* the one-electron states. That is this chapter's job: the orbital basis and the operators that live on it.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Generating the boilerplate that enumerates orbital labels $(n, \ell, m_\ell, m_s)$ and stores them as an ordered list of basis kets — *Why AI works here:* this is pure bookkeeping over known ranges ($\ell \in [0, n-1]$, $m_\ell \in [-\ell, \ell]$, $m_s = \pm\tfrac12$); you can independently verify the count is $2n^2$ per shell.
- Scaffolding a small linear-algebra utility (build a matrix $A_{mn} = \langle m|\hat A|n\rangle$, apply a change of basis $A' = U^\dagger A U$) — *Why AI works here:* it is reformatting standard matrix operations into code, and you can check it against a hand computation on a $2\times2$ Pauli matrix.

**The tell:** You are using AI well when you have an independent way to check the output — here, the subshell capacity $2(2\ell+1)$ and the unitarity check $|\det U| = 1$.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding *which* commuting operators may simultaneously label a state — i.e. choosing the orbital quantum numbers as a complete set — *Why AI fails here:* this is a physics call about which operators commute (Chapter 3's content), not a coding task; an LLM will happily hand you a plausible label set that is not a valid CSCO.
- Asserting that the matrix it built for $\hat{L}_z$ or the energy operator is correct in your chosen basis — *Why AI fails here:* a transposed index or a wrong sign in an off-diagonal element produces a matrix that *looks* Hermitian and runs without error but encodes the wrong physics, and there is no ground truth in the output to flag it.

**The tell:** If you could not explain why the basis labels are the right ones without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.
**Physics-judgment connection:** this trains the habit of checking a constructed matrix against an invariant — Hermiticity ($A_{mn} = A_{nm}^*$), the known eigenvalues ($\pm1$ for Paulis), and basis-independence of those eigenvalues — before trusting that the data structure encodes the operator you meant.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a small Python module `orbitals.py` that enumerates the hydrogenic orbital basis and represents diagonal one-electron operators as matrices over it.
**Tool:** Claude chat (a single self-contained module; no persistent project context needed yet).
**The Prompt:**
```
I am building an atomic-structure simulator over several sessions. This first module
only sets up the orbital basis and operators — no physics approximations yet.

Write a single Python file `orbitals.py` (standard library + numpy only) that:

1. Defines an Orbital data class with fields n, l, m_l, m_s (m_s in {+1/2, -1/2}),
   and a __repr__ that prints spectroscopic notation, e.g. "3d (m_l=+2, up)".
2. Provides enumerate_shell(n) returning all orbitals with that principal quantum
   number, enforcing l in [0, n-1], m_l in [-l, l], m_s in {+1/2, -1/2}.
3. Provides a function ordered_basis(n_max) returning a deterministic ordered list
   of all orbitals up to n_max, which I will use as a fixed basis ordering.
4. Provides matrix_of(operator_fn, basis) that builds the matrix A_{mn} =
   <m|A|n> given a callable returning <m|A|n> for two orbitals, so I can later
   represent L_z (diagonal, eigenvalue m_l*hbar) and an occupation operator.
5. Includes a __main__ block that builds the basis for n_max=3, prints the count,
   and asserts it equals sum over n of 2*n^2 (i.e. 2*(1+4+9) = 28).

Do NOT decide the physical energy ordering of orbitals or apply any screening —
that comes in later modules. Just the basis and the matrix machinery.
Add a docstring noting the subshell capacity is 2*(2l+1).
```
**What this produces:** `orbitals.py` — the basis-and-operators foundation every later module imports.
**How to adapt:** *Your system:* swap `numpy` for plain lists if you want zero dependencies. *ChatGPT/Gemini:* identical prompt; ask for a `pytest` file checking the $2n^2$ count. *Claude Project:* drop this module into a project as a file so later chapters' prompts can reference it as the established basis.
**Builds on:** nothing — this is the foundation.  **Next:** Chapter 2 turns the energy operator into something you diagonalize to *order* these orbitals.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the same `orbitals.py`, but generated and verified inside your project directory with a test that runs.
**Tool:** Claude Code (file creation plus running the test in one place).
**Skill level:** Beginner
**Setup — confirm:**
- [ ] An empty project directory `build-the-atom/` exists.
- [ ] Python 3 with `numpy` installed.
- [ ] A `CLAUDE.md` rule to add (below).
**The Task:**
```
In the directory build-the-atom/, create two files:

- orbitals.py: an Orbital data class (n, l, m_l, m_s), enumerate_shell(n),
  ordered_basis(n_max), and matrix_of(operator_fn, basis). Enforce
  l in [0, n-1], m_l in [-l, l], m_s in {+1/2, -1/2}. Do not impose any
  energy ordering or screening.
- test_orbitals.py: pytest tests asserting (a) shell n has 2*n^2 orbitals;
  (b) ordered_basis(3) has 28 entries; (c) the L_z matrix built via
  matrix_of is diagonal with entries m_l (in units of hbar); (d) that
  matrix equals its own conjugate transpose (Hermitian).

Then run `pytest -q` and show me the output. Do not modify any other files.
```
**Expected output:** `orbitals.py`, `test_orbitals.py`, and a passing `pytest` run (4 tests).
**What to inspect:** confirm the $2n^2$ count by hand for $n=1,2,3$ (2, 8, 18 → 28 total); confirm the $\hat{L}_z$ matrix is diagonal and its diagonal lists the $m_\ell$ values, not the $\ell$ values.
**If it goes wrong:** the most common failure is enumerating $m_\ell$ from $-\ell+1$ or omitting $m_\ell = 0$, giving the wrong count. Recovery: print the orbitals of one shell and check $2\ell+1$ values of $m_\ell$ per subshell before trusting the total.
**CLAUDE.md / AGENTS.md note:** add — "The orbital basis ordering produced by `ordered_basis` is fixed; never reorder it in later modules — all matrices are indexed by it."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `orbitals.py` module and its $\hat{L}_z$ matrix from R3/R4.
**Validation type:** Code
**Risk level:** Low — the logic is bounded enumeration, but a silent index/sign error here propagates into every later chapter, so it is worth catching now.
**Setup:** use your own R3/R4 artifact.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — The Formalism
□ Correctness: does each shell n contain exactly 2*n^2 orbitals?
□ Completeness: does m_l run over all 2l+1 integer values, including 0?
□ Scope: did it add an energy ordering or screening it was told NOT to add?
□ Physics criterion 1: is the L_z matrix diagonal with entries equal to m_l
  (not l), in the fixed basis ordering?
□ Physics criterion 2: does the L_z matrix satisfy A_{mn} = A_{nm}^* (Hermitian)?
□ Failure-mode check: any of —
  - fluent but wrong (runs cleanly, wrong count per subshell)
  - off-by-one in the m_l range (drops m_l=0 or the top rung)
  - l-vs-m_l confusion (diagonal lists l instead of m_l)
  - basis reordered between functions so matrices no longer align
```
**What to do with findings:** pass → use it as your foundation, and note that the $2n^2$ assertion is what made it trustworthy; one fail → fix the enumeration range and re-run the test; multiple fails → drop the AI draft and write the enumeration by hand, it is a dozen lines.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI generated the orbital enumeration and matrix-builder boilerplate, which I used as the project's basis module.
> *2:* The AI could not certify that the basis labels form a valid simultaneous-eigenvalue set — that this is the right *physical* labeling is a CSCO judgment I confirmed myself (Chapter 3).
**Physics-judgment connection:** validating a data structure against a counting invariant ($2n^2$) and an operator invariant (Hermiticity) before building anything on top of it.

---

*Chapter 2 follows: which operators are the right ones to represent physical measurements? The answer is Hermitian operators, and the reason is that measurement outcomes must be real numbers. From that single requirement the spectral theorem follows: every observable has a complete eigenbasis, and the Born rule can be written in terms of it.*
