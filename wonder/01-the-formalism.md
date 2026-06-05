# Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

Let me hand you a small mystery, the kind that ought to keep you up at night.

Take a single particle moving along a line. The wave function $\psi(x)$ answers one question: how likely are you to find it at position $x$? Now run that wave function through a Fourier transform and you get $\tilde{\psi}(p)$, which answers a different question: how likely are you to find it carrying momentum $p$? Here is the strange part. These two functions know exactly the same things. Each one tells you everything there is to know about the particle. And yet, put them side by side, and they could be perfect strangers. One might be a tight little spike; the other, a sprawling wave that won't stop wiggling. Sometimes — for a Gaussian, say — both come out looking like gentle humps, but that's a coincidence of arithmetic, not a law. Make $\psi$ a sharp step and its momentum twin becomes a sinc function, ringing on forever.

So tell me — which of these two is the particle's *actual* state?

Trick question. Neither is. Here is the thing I want you to hold onto: $\psi(x)$ isn't the state at all. It's a shadow the state casts when you shine the light of the position basis on it. And $\tilde{\psi}(p)$? Same state, different light. The real object — the state, the thing itself — floats above both of those pictures at once. Picture an ordinary arrow pointing somewhere in space. Write its coordinates in a Cartesian grid, then write them again in spherical coordinates. The numbers change completely. The arrow hasn't budged an inch.

Every wave-mechanics calculation you've ever done was secretly a calculation in *one* chosen basis — almost always position. What I'm about to show you is how to write the physics down just once, basis-free, and only afterward decide which basis makes the arithmetic least painful.

---

## The Arena

A **Hilbert space** $\mathcal{H}$ is a complete complex inner-product space. Strip that phrase down to what matters and two words survive: *complex*, and *inner product*. You're allowed to add vectors, scale them by complex numbers, and take inner products of pairs. That's the whole toolkit. Nothing else is promised.

Don't gloss over "complex." It earns its place. Multiply any state by any number $c \in \mathbb{C}$ you like and what you get back is still a perfectly good state. And the inner product carries a subtlety — it's **sesquilinear**, which is a fancy way of saying it behaves linearly in its second slot but flips complex numbers to their conjugates in its first:

$$\langle(a|\phi_1\rangle + b|\phi_2\rangle)|\psi\rangle = a^*\langle\phi_1|\psi\rangle + b^*\langle\phi_2|\psi\rangle.$$

It also refuses to be symmetric. Swap the two arguments and you don't get the same number back — you get its complex conjugate:

$$\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*.$$

Flip the bra and the ket, and a conjugate sneaks in. In an ordinary *real* vector space the inner product doesn't care about order and you can swap to your heart's content. Not here. That little conjugate is the silent culprit behind nearly every sign error you'll make in an adjoint calculation, every place a Hermiticity proof goes sideways. Burn it into memory now and save yourself the grief later.

How big is the space? Could be finite, could be infinite — the machinery doesn't flinch either way. A qubit gets by in $\mathbb{C}^2$, just two dimensions. A particle on a line needs $L^2(\mathbb{R})$, the space of square-integrable complex functions, which is infinite-dimensional. One framework, both cases, no special pleading.

---

## Kets, Bras, and What They Are

The beauty of Dirac's notation is that it won't let you confuse two things that ought to stay separate.

A **ket** $|\psi\rangle$ is a vector living in $\mathcal{H}$. If it helps, picture a column of numbers.

A **bra** $\langle\phi|$ is something else entirely — a machine that eats a ket and spits out a single complex number. Every ket $|\phi\rangle$ comes with a partner bra $\langle\phi|$, defined by the rule $\langle\phi|: |\psi\rangle \mapsto \langle\phi|\psi\rangle$. If the ket was a column, the bra is the row you'd get by transposing it *and* conjugating every entry.

That conjugation isn't optional. The bra belonging to $c|\phi\rangle$ is $c^*\langle\phi|$, complex conjugate and all — and it shows up automatically the moment you take the definition of the inner product seriously.

Now watch the two ways these objects can meet. Write them as $\langle\phi|\psi\rangle$ and you've built a **scalar** — one complex number, done. Write them the *other* way around, $|\psi\rangle\langle\phi|$, and you've built something with completely different DNA: an **operator**, a machine that takes any $|\chi\rangle$ and returns $\langle\phi|\chi\rangle\,|\psi\rangle$. Inner product gives a scalar. Outer product gives an operator. These aren't two flavors of the same thing; they're different species. Mix them up in an equation and you've made two mistakes at once, not one.

---

## Three Identities

Pin down an orthonormal basis $\{|n\rangle\}$ for $\mathcal{H}$. Almost every manipulation you'll ever do rests on just three statements.

**Completeness:**
$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Look at it the right way and this is nothing but the number 1 — wearing the costume of an operator. When the basis is continuous, the sum becomes an integral: $\int |x\rangle\langle x|\,dx = \hat{I}$.

**Orthonormality:**
$$\langle m|n\rangle = \delta_{mn}.$$

For position eigenstates this sharpens into $\langle x|x'\rangle = \delta(x-x')$.

**Expansion:**
$$|\psi\rangle = \sum_n c_n|n\rangle, \qquad c_n = \langle n|\psi\rangle.$$

Each coefficient $c_n$ measures how much the abstract vector leans in the $n$-th direction. Pick a new basis and every one of those numbers changes — but, as I keep insisting, the vector itself sits perfectly still.

The real workhorse here is completeness, and here's the trick worth memorizing. Slip $\hat{I}$ into any expression — between two pieces of an inner product — and an abstract bracket instantly turns into a concrete sum you can actually compute:

$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|n\rangle\langle n|\psi\rangle = \sum_n \phi_n^* \psi_n.$$

Do the same in the position basis and the sum becomes $\int\phi^*(x)\psi(x)\,dx$. So the lofty abstract inner product and the homely wave-function overlap integral you've computed a hundred times — they were the same object all along.

---

## The Fourier Transform Is a Basis Change

A particle on a line *is* a single unit vector $|\psi\rangle$ sitting in $L^2(\mathbb{R})$. Two bases are worth keeping handy: the position eigenstates $\{|x\rangle\}$ and the momentum eigenstates $\{|p\rangle\}$.

Project onto position and you get the familiar wave function: $\psi(x) = \langle x|\psi\rangle$.

Project onto momentum and you get its momentum-space cousin: $\tilde{\psi}(p) = \langle p|\psi\rangle$.

One vector, two snapshots. Now watch what happens when you slide the position completeness relation into the second one:

$$\tilde{\psi}(p) = \langle p|\psi\rangle = \int\langle p|x\rangle\langle x|\psi\rangle\,dx = \int\langle p|x\rangle\,\psi(x)\,dx.$$

Everything now hinges on a single unknown: what is $\langle p|x\rangle$? A momentum eigenstate, viewed in position space, has to obey $\hat{p}|p\rangle = p|p\rangle$, which in plain language reads $-i\hbar\,\partial_x\langle x|p\rangle = p\langle x|p\rangle$. Solve that little differential equation and out pops $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Conjugate it for the bra-ket the other way and $\langle p|x\rangle = e^{-ipx/\hbar}/\sqrt{2\pi\hbar}$. Drop it back in:

$$\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx.$$

There it is — the Fourier transform. Nobody had to fetch it from a textbook on analysis and bolt it on. It simply fell out: one completeness relation, one differential equation, and the rest is bookkeeping. So here's a lens to carry with you forever — every Fourier transform that turns up in quantum mechanics is a basis change in disguise.

Neither picture, position or momentum, is the "true" one. They hold the very same physics. You reach for whichever makes the integral surrender faster.

---

## Operators: Abstract Maps, Not Matrices

A **linear operator** $\hat{A}$ is a linear map $\mathcal{H} \to \mathcal{H}$. Notice what's missing from that sentence: any mention of a basis. The operator exists before you've chosen one.

Choose a basis $\{|n\rangle\}$ and *then* the operator acquires a matrix:

$$A_{mn} = \langle m|\hat{A}|n\rangle.$$

Pick a different basis and the matrix changes — every entry, possibly beyond recognition. But it's the *same operator*. If you take one idea from this chapter, take that one.

The position operator $\hat{x}$ drives the point home. In the position basis it just multiplies by $x$, so its matrix is diagonal, about as simple as matrices get. Now write that *same* $\hat{x}$ in the energy basis of the harmonic oscillator and you get a tridiagonal mess studded with factors of $\sqrt{n}$. One operator. Two matrices that share almost nothing visually. The matrices are scenery, painted by whatever basis you happened to stand in. The operator behind them never changed.

The **adjoint** $\hat{A}^\dagger$ is fixed by the requirement:

$$\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle \quad \text{for all }|\psi\rangle, |\phi\rangle.$$

In matrix terms that's the conjugate transpose: $(A^\dagger)_{mn} = A_{nm}^*$. Call an operator **Hermitian** when it equals its own adjoint, $\hat{A}^\dagger = \hat{A}$, which forces $A_{mn} = A_{nm}^*$. Here's the example to keep loaded in the chamber: $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Transpose it plainly and you get $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$ — antisymmetric, looks all wrong. But transpose *and conjugate*, and you land back on $+\sigma_y$ — Hermitian after all. The $i$ pulled the whole thing off. So a matrix can be stuffed with complex off-diagonal entries and still be perfectly Hermitian, provided $A_{12} = A_{21}^*$. The reflex "Hermitian just means symmetric" is a habit from real linear algebra, and in the complex world it will quietly betray you.

One more property worth memorizing: the adjoint flips the order of a product, $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$. The proof is a single line from the definition — but the moment your calculation involves products of operators, you'll lean on it constantly.

Want to move from basis $\{|a_n\rangle\}$ to basis $\{|b_m\rangle\}$? The unitary matrix $U_{mn} = \langle a_m|b_n\rangle$ does the carrying, and operator matrices transform as $O' = U^\dagger O U$. Here's the punchline that ties the whole chapter together: $O'$ and $O$ have *identical eigenvalues*. The physics doesn't care which basis you stood in. The matrix is just your description of the thing; the operator is the thing.

---

## Worked Example — A State in the Energy Basis

Picture a particle trapped in an infinite square well of width $L$, set up in the state

$$\psi(x) = \sqrt{\frac{30}{L^5}}\,x(L-x), \qquad 0 < x < L.$$

The energy eigenstates are $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with eigenvalues $E_n = n^2 E_1$, where $E_1 = \pi^2\hbar^2/(2mL^2)$. We're going to compute $\langle\hat{H}\rangle$ by two different roads and watch them arrive at the same town.

**Energy basis route.** The expansion coefficients are $c_n = \langle E_n|\psi\rangle = \int_0^L\psi_n^*(x)\psi(x)\,dx$. Using the standard integral $\int_0^L x(L-x)\sin(n\pi x/L)\,dx = 2L^3/(n^3\pi^3)\cdot[1-(-1)^n]$, which vanishes for even $n$:

$$c_n = \frac{4\sqrt{60}}{n^3\pi^3} \quad (n \text{ odd}), \qquad c_n = 0 \quad (n \text{ even}).$$

Check normalization: $\sum_{n\,\text{odd}}|c_n|^2 = 960/\pi^6 \cdot \sum_{n\,\text{odd}}1/n^6$. The sum $\sum_{n\,\text{odd}}1/n^6 = \pi^6/960$, so $\sum|c_n|^2 = 1$.

In the energy basis $\hat{H}$ is diagonal, so:

$$\langle\hat{H}\rangle = \sum_{n\,\text{odd}}|c_n|^2 E_n = \frac{960 E_1}{\pi^6}\sum_{n\,\text{odd}}\frac{1}{n^4} = \frac{960 E_1}{\pi^6}\cdot\frac{\pi^4}{96} = \frac{10 E_1}{\pi^2} = \frac{5\hbar^2}{mL^2}.$$

**Position basis route.** With $\hat{H} = -(\hbar^2/2m)\partial_x^2$ and $\partial_x^2\psi = -2\sqrt{30/L^5}$:

$$\langle\hat{H}\rangle = \frac{\hbar^2}{m}\sqrt{\frac{30}{L^5}}\int_0^L x(L-x)\,dx\cdot\sqrt{\frac{30}{L^5}} = \frac{60\hbar^2}{mL^5}\cdot\frac{L^3}{6} = \frac{10\hbar^2}{mL^2}\cdot\frac{1}{2} = \frac{5\hbar^2}{mL^2}.$$

The same number, right on cue. The expectation value couldn't care less which basis you used. One road was a weighted sum over discrete energies; the other was a couple of derivatives and an integral. Different labor, identical answer — and *that* is precisely what we mean when we say the operator lives above any particular basis.

A word of caution about where this trick stops working. Road number one only opened up because we happened to know the eigenstates $\psi_n(x)$ in closed form. Hand me a nastier potential whose eigenstates won't write down on paper, and that route is simply unavailable. The abstract formalism stays exact regardless. Whether you can actually *compute* with it depends on whether you've got a basis you can hold in your hands.

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
