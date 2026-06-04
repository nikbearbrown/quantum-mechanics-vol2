# Chapter 4 — Quantum Dynamics: Time Evolution and the Pictures

## TL;DR

- Probability conservation forces the time-evolution operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ to be unitary; the Schrödinger equation follows by differentiation.
- In the **Schrödinger picture**, states carry all the time dependence: $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$; operators are fixed.
- In the **Heisenberg picture**, operators carry all the time dependence: $\hat{A}_H(t) = \hat{U}^\dagger(t)\hat{A}\hat{U}(t)$; states are frozen at $t = 0$.
- Both pictures give identical expectation values; the choice is computational, not physical.
- The **Heisenberg equation of motion** $i\hbar\,d\hat{A}_H/dt = [\hat{A}_H, \hat{H}]$ is the quantum analog of Hamilton's equations.
- **Ehrenfest's theorem** $d\langle\hat{A}\rangle/dt = (i/\hbar)\langle[\hat{H}, \hat{A}]\rangle$ connects operator dynamics to classical equations of motion.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Derive** $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ from the requirement that probability is conserved, and verify it satisfies the operator Schrödinger equation. *(Apply)*
2. **Evolve** an arbitrary state by expanding in energy eigenstates and attaching phase factors, for both two-level systems and the free particle. *(Apply)*
3. **Switch** between Schrödinger and Heisenberg pictures and verify that expectation values are the same in both. *(Analyze)*
4. **Derive and apply** the Heisenberg equation of motion to compute $\hat{x}_H(t)$ and $\hat{p}_H(t)$ for the free particle and the harmonic oscillator using commutator algebra alone. *(Apply / Analyze)*
5. **State** Ehrenfest's theorem, identify when $\langle\hat{F}\rangle = -\partial V/\partial\langle\hat{x}\rangle$ (the classical limit), and give an example where the approximation fails. *(Evaluate)*

---

## Opening Scene

In 1925, Werner Heisenberg sat on the island of Helgoland, recovering from hay fever and stripped of his visual intuitions about electron orbits. He decided to work only with things he could observe: the frequencies and intensities of spectral lines. He arranged these into arrays of numbers that he multiplied in an unfamiliar way — row times column, not number times number. Within months, Born and Jordan recognized that Heisenberg's "multiplication tables" were matrix multiplication, and that the strange rule giving $xp - px = i\hbar$ was exactly what distinguished his quantum theory from the classical one.

A few months later, Schrödinger derived his wave equation — a partial differential equation for $\psi(x,t)$ that looked nothing like Heisenberg's matrices. The physics community briefly debated which one was right. Schrödinger showed they were mathematically equivalent. But the equivalence is more than a historical curiosity: the two formulations are two *pictures* of the same physics, related by the unitary operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$. In the Schrödinger picture, $\hat{U}(t)$ acts on states. In the Heisenberg picture, it acts on operators. Expectation values — the only observables — come out the same either way.

Understanding both pictures is not academic. The Schrödinger picture is natural for wave equations, boundary-value problems, and numerical simulation. The Heisenberg picture is natural when you want equations of motion for observables, when the problem has classical analogs, and in quantum field theory, where field operators in the Heisenberg picture obey clean dynamical equations that Schrödinger-picture wavefunctionals do not. The two pictures are complementary tools, not competing theories.

---

## Core Development

### The time-evolution operator from probability conservation

The Schrödinger equation did not come from nowhere. It follows from two requirements: probability is conserved, and time evolution is linear.

Let $\hat{U}(t)$ be the operator that advances any state from time $0$ to time $t$:

$$|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle.$$

**Unitarity from probability conservation.** The total probability must be preserved:

$$\langle\psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger(t)\hat{U}(t)|\psi(0)\rangle = \langle\psi(0)|\psi(0)\rangle = 1.$$

This must hold for every initial state, so $\hat{U}^\dagger(t)\hat{U}(t) = \hat{I}$: the time-evolution operator is **unitary**.

**Generator of time translations.** Consider an infinitesimal step $dt$. The most general linear operator that equals $\hat{I}$ at $t = 0$ and is unitary to first order in $dt$ is

$$\hat{U}(dt) = \hat{I} - \frac{i}{\hbar}\hat{H}\,dt,$$

where $\hat{H}$ is some operator. Unitarity to first order requires $\hat{U}^\dagger\hat{U} = (\hat{I} + \frac{i}{\hbar}\hat{H}^\dagger dt)(\hat{I} - \frac{i}{\hbar}\hat{H} dt) = \hat{I} + \frac{i}{\hbar}(\hat{H}^\dagger - \hat{H})dt + O(dt^2) = \hat{I}$, so $\hat{H}^\dagger = \hat{H}$: the generator must be Hermitian. Physical dimensions require the factor $\hbar$; the operator $\hat{H}$ has units of energy and is the **Hamiltonian**.

**Finite time evolution.** Compose infinitesimal steps: $\hat{U}(t) = \lim_{N\to\infty}[\hat{I} - \frac{i}{\hbar}\hat{H}(t/N)]^N$. For time-independent $\hat{H}$ this limit is the matrix exponential:

$$\boxed{\hat{U}(t) = e^{-i\hat{H}t/\hbar}.}$$

**The Schrödinger equation.** Differentiate $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$ with respect to $t$, using $d\hat{U}/dt = (-i\hat{H}/\hbar)\hat{U}$:

$$i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle.$$

The Schrödinger equation is not a separate postulate. It is the statement that $\hat{U}(t)$ satisfies its own differential equation.

**Stationary states.** If $|\psi(0)\rangle = |E_n\rangle$ is an energy eigenstate, $\hat{H}|E_n\rangle = E_n|E_n\rangle$, then

$$e^{-i\hat{H}t/\hbar}|E_n\rangle = e^{-iE_n t/\hbar}|E_n\rangle.$$

The state acquires a phase but does not change. Every expectation value is constant: $\langle E_n|\hat{A}|E_n\rangle$ is time-independent. This is a **stationary state**.

**General state evolution.** For $|\psi(0)\rangle = \sum_n c_n|E_n\rangle$:

$$|\psi(t)\rangle = \sum_n c_n\,e^{-iE_n t/\hbar}|E_n\rangle.$$

Computing time evolution amounts to: (1) expand in energy eigenstates, (2) attach phase factors $e^{-iE_n t/\hbar}$ to each coefficient, (3) reassemble. The entire dynamics lives in the relative phases between energy eigenstates.

---

### The Schrödinger picture: worked example

**Two-level system.** Take $\hat{H} = \omega_0\hat{S}_x = (\omega_0\hbar/2)\sigma_x$ with initial state $|\psi(0)\rangle = |\!\uparrow\rangle = |+z\rangle$.

The eigenstates of $\hat{S}_x$ are $|x\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$ with eigenvalues $\pm\hbar\omega_0/2$. Expand $|\!\uparrow\rangle$ in the $\hat{S}_x$ eigenbasis:

$$|\!\uparrow\rangle = \frac{1}{\sqrt{2}}\bigl(|x+\rangle + |x-\rangle\bigr).$$

Attach phase factors:

$$|\psi(t)\rangle = \frac{1}{\sqrt{2}}\bigl(e^{-i\omega_0 t/2}|x+\rangle + e^{+i\omega_0 t/2}|x-\rangle\bigr).$$

Convert back to the $\hat{S}_z$ basis using $|x\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$:

$$|\psi(t)\rangle = \cos\!\left(\frac{\omega_0 t}{2}\right)|\!\uparrow\rangle - i\sin\!\left(\frac{\omega_0 t}{2}\right)|\!\downarrow\rangle.$$

The expectation value of $\hat{S}_z$ oscillates (a **Rabi oscillation**):

$$\langle\hat{S}_z(t)\rangle = \frac{\hbar}{2}\left(\cos^2\!\frac{\omega_0 t}{2} - \sin^2\!\frac{\omega_0 t}{2}\right) = \frac{\hbar}{2}\cos(\omega_0 t).$$

The population starts entirely in $|\!\uparrow\rangle$, sloshes to $|\!\downarrow\rangle$ at $t = \pi/\omega_0$, and returns. This is the physics of NMR: a spin driven by a resonant RF pulse oscillates between up and down at the Rabi frequency.

---

### The Heisenberg picture

Both Schrödinger and Heisenberg pictures must agree on every expectation value:

$$\langle\hat{A}\rangle(t) = \langle\psi(t)|\hat{A}|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger(t)\hat{A}\hat{U}(t)|\psi(0)\rangle.$$

The Schrödinger picture assigns the time dependence to the state: $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$, operators fixed. The **Heisenberg picture** does the opposite: fix the state at its $t = 0$ value and assign all the time dependence to the operator.

**Definition.** The Heisenberg-picture operator is

$$\hat{A}_H(t) = \hat{U}^\dagger(t)\,\hat{A}\,\hat{U}(t),$$

where $\hat{A}$ (no subscript) is the Schrödinger-picture operator. The state in the Heisenberg picture is $|\psi_H\rangle = |\psi(0)\rangle$, frozen forever. Then:

$$\langle\psi_H|\hat{A}_H(t)|\psi_H\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{A}\hat{U}|\psi(0)\rangle = \langle\hat{A}\rangle(t).$$

The two pictures give the same number. They are related by a **unitary transformation** — a change of basis in time.

**What the transformation does to commutators.** Since $\hat{U}$ is unitary, it preserves all algebraic relations. In particular:

$$[\hat{x}_H(t), \hat{p}_H(t)] = \hat{U}^\dagger[\hat{x}, \hat{p}]\hat{U} = \hat{U}^\dagger(i\hbar)\hat{U} = i\hbar.$$

The canonical commutation relation is preserved at all times. This is a necessary consistency check: switching pictures cannot change the fundamental algebra of quantum mechanics.

---

### The Heisenberg equation of motion

Differentiate $\hat{A}_H(t) = \hat{U}^\dagger(t)\hat{A}\hat{U}(t)$ with respect to $t$:

$$\frac{d\hat{A}_H}{dt} = \frac{d\hat{U}^\dagger}{dt}\hat{A}\hat{U} + \hat{U}^\dagger\hat{A}\frac{d\hat{U}}{dt}.$$

From $\hat{U} = e^{-i\hat{H}t/\hbar}$ we have $d\hat{U}/dt = (-i\hat{H}/\hbar)\hat{U}$, and taking the adjoint: $d\hat{U}^\dagger/dt = \hat{U}^\dagger(i\hat{H}/\hbar)$ (using that $\hat{H}$ is Hermitian and $\hat{H}$ commutes with $\hat{U}$ for time-independent $\hat{H}$). Substituting:

$$\frac{d\hat{A}_H}{dt} = \hat{U}^\dagger\frac{i\hat{H}}{\hbar}\hat{A}\hat{U} + \hat{U}^\dagger\hat{A}\frac{-i\hat{H}}{\hbar}\hat{U} = \frac{i}{\hbar}\hat{U}^\dagger[\hat{H}, \hat{A}]\hat{U} = \frac{i}{\hbar}[\hat{H}_H, \hat{A}_H].$$

Since $\hat{H}$ commutes with $\hat{U}$ (it is a function of $\hat{H}$), we have $\hat{H}_H = \hat{U}^\dagger\hat{H}\hat{U} = \hat{H}$. Therefore:

$$\boxed{i\hbar\,\frac{d\hat{A}_H}{dt} = [\hat{A}_H,\, \hat{H}].}$$

This is the **Heisenberg equation of motion**. It is an *operator* equation — both sides are operators, not expectation values. Compare it to Hamilton's equations of classical mechanics:

$$\dot{x} = \{x, H\}_\text{Poisson}, \qquad \dot{p} = \{p, H\}_\text{Poisson}.$$

The quantum equation is the classical one with the Poisson bracket $\{f, g\}$ replaced by $[\hat{f}, \hat{g}]/(i\hbar)$. This is Dirac's quantization dictionary, and it works in both directions: a commutator in quantum mechanics becomes a Poisson bracket in the classical limit.

**Conservation law.** If $[\hat{H}, \hat{A}] = 0$, then $d\hat{A}_H/dt = 0$ and $\hat{A}_H(t) = \hat{A}_H(0)$: the observable $A$ is a **constant of motion**. This is the quantum version of Noether's theorem: a symmetry of the Hamiltonian produces a conserved quantity. For the hydrogen atom, $[\hat{H}, \hat{L}^2] = 0$ and $[\hat{H}, \hat{L}_z] = 0$, so total angular momentum squared and its $z$-component are constants of motion.

---

### Worked example: Heisenberg picture for the free particle

**The Hamiltonian.** $\hat{H} = \hat{p}^2/2m$. This is the only term.

**Equation for $\hat{p}_H(t)$.** From the Heisenberg equation:

$$i\hbar\,\frac{d\hat{p}_H}{dt} = [\hat{p}_H, \hat{H}] = [\hat{p}_H, \hat{p}_H^2/2m] = 0,$$

since any operator commutes with a function of itself. Therefore:

$$\hat{p}_H(t) = \hat{p}_H(0) = \hat{p}.$$

Momentum is conserved for the free particle — as expected.

**Equation for $\hat{x}_H(t)$.** Using $[\hat{x}, \hat{p}^2] = \hat{p}[\hat{x},\hat{p}] + [\hat{x},\hat{p}]\hat{p} = 2i\hbar\hat{p}$:

$$i\hbar\,\frac{d\hat{x}_H}{dt} = [\hat{x}_H, \hat{H}] = \left[\hat{x}_H, \frac{\hat{p}_H^2}{2m}\right] = \frac{i\hbar}{m}\hat{p}_H.$$

Dividing by $i\hbar$:

$$\frac{d\hat{x}_H}{dt} = \frac{\hat{p}_H}{m} = \frac{\hat{p}}{m}.$$

Since $\hat{p}_H$ is constant, this is a first-order linear ODE. Integrate:

$$\hat{x}_H(t) = \hat{x}(0) + \frac{\hat{p}}{m}\,t.$$

These are the exact quantum equations of motion for the free particle. Written out, they say: position at time $t$ equals initial position plus $(\text{momentum}/\text{mass}) \times t$. The operators obey Newton's first law precisely.

**What the Schrödinger picture shows instead.** In the Schrödinger picture, the wavepacket $\psi(x,t)$ *spreads* — $\sigma_x$ grows with time even though $\sigma_p$ is constant. The Heisenberg-picture equations describe the motion of the center of the wavepacket; they say nothing about spreading. The two pictures are complementary: one tracks where the packet goes, the other shows how it disperses.

---

### Worked example: Heisenberg picture for the harmonic oscillator

**The Hamiltonian.** $\hat{H} = \hat{p}^2/2m + m\omega^2\hat{x}^2/2$.

**Coupled equations.** Following the same pattern, the Heisenberg equations give:

$$\frac{d\hat{x}_H}{dt} = \frac{\hat{p}_H}{m}, \qquad \frac{d\hat{p}_H}{dt} = -m\omega^2\hat{x}_H.$$

These are two coupled first-order ODEs for operator-valued functions of time. They are *exactly* Hamilton's equations for the classical harmonic oscillator — with operators replacing classical variables.

**Solution.** Differentiate the first equation and substitute the second:

$$\frac{d^2\hat{x}_H}{dt^2} = \frac{1}{m}\frac{d\hat{p}_H}{dt} = -\omega^2\hat{x}_H.$$

This is the simple harmonic oscillator equation. The solution with initial conditions $\hat{x}_H(0) = \hat{x}$ and $\hat{p}_H(0) = \hat{p}$:

$$\hat{x}_H(t) = \hat{x}\cos(\omega t) + \frac{\hat{p}}{m\omega}\sin(\omega t),$$
$$\hat{p}_H(t) = \hat{p}\cos(\omega t) - m\omega\hat{x}\sin(\omega t).$$

The position and momentum operators oscillate at frequency $\omega$ — identical to the classical result. Expectation values therefore oscillate classically regardless of the quantum state (which determines the initial spread but not the oscillation frequency). The Heisenberg picture makes this clean: the operators obey classical dynamics exactly, leaving all quantum effects in the initial state.

**Consistency check.** Verify $[\hat{x}_H(t), \hat{p}_H(t)] = i\hbar$ at all $t$:

$$[\hat{x}_H(t), \hat{p}_H(t)] = \left[\hat{x}\cos\omega t + \frac{\hat{p}}{m\omega}\sin\omega t,\; \hat{p}\cos\omega t - m\omega\hat{x}\sin\omega t\right].$$

Expand using $[\hat{x}, \hat{p}] = i\hbar$ and $[\hat{x}, \hat{x}] = [\hat{p}, \hat{p}] = 0$:

$$= \cos^2(\omega t)[\hat{x}, \hat{p}] + \sin^2(\omega t)\left[\frac{\hat{p}}{m\omega},\,-m\omega\hat{x}\right] = i\hbar\cos^2(\omega t) + i\hbar\sin^2(\omega t) = i\hbar. \checkmark$$

The canonical commutation relation is preserved. This is guaranteed by unitarity of $\hat{U}(t)$ — it is a sanity check, not a coincidence.

**Ladder operators.** Expressed in terms of the creation and annihilation operators $\hat{a} = (m\omega\hat{x} + i\hat{p})/\sqrt{2m\omega\hbar}$ and $\hat{a}^\dagger = (m\omega\hat{x} - i\hat{p})/\sqrt{2m\omega\hbar}$:

$$\hat{a}_H(t) = \hat{a}\,e^{-i\omega t}, \qquad \hat{a}^\dagger_H(t) = \hat{a}^\dagger\,e^{+i\omega t}.$$

The creation operator rotates counterclockwise in the complex plane at frequency $\omega$; the annihilation operator rotates clockwise. Coherent states — eigenstates of $\hat{a}$ — therefore have expectation values $\langle\hat{x}_H(t)\rangle$ and $\langle\hat{p}_H(t)\rangle$ that trace exact classical orbits. This is why coherent states are the "most classical" quantum states of the oscillator.

---

### Ehrenfest's theorem

The Heisenberg equation $d\hat{A}_H/dt = (i/\hbar)[\hat{H}, \hat{A}_H]$ is an operator equation. Taking its expectation value in any state $|\psi\rangle$ (Schrödinger-picture, using the Heisenberg-picture state $|\psi(0)\rangle$):

$$\frac{d}{dt}\langle\hat{A}\rangle = \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle.$$

This is the **generalized Ehrenfest theorem**. It requires no choice of picture — it holds in either.

**Newton's second law for expectation values.** Apply with $\hat{A} = \hat{x}$: $[\hat{H}, \hat{x}] = [\hat{p}^2/2m, \hat{x}] = -i\hbar\hat{p}/m$, so

$$\frac{d\langle\hat{x}\rangle}{dt} = \frac{\langle\hat{p}\rangle}{m}.$$

Apply with $\hat{A} = \hat{p}$: $[\hat{H}, \hat{p}] = [V(\hat{x}), \hat{p}] = i\hbar\,\partial V/\partial x$ (by the same test-function argument as $[\hat{x}, \hat{p}]$ but in reverse), so

$$\frac{d\langle\hat{p}\rangle}{dt} = -\left\langle\frac{\partial V}{\partial x}\right\rangle.$$

This looks like Newton's second law $F = ma$, but with the force evaluated at the *expectation value of position* replaced by the *expectation value of the force*. These are the same only if $\partial V/\partial x$ is linear in $x$ — i.e., for the harmonic oscillator and the free particle. For a general potential:

$$-\left\langle\frac{\partial V}{\partial x}\right\rangle \neq -\frac{\partial V}{\partial\langle x\rangle}.$$

The correction is of order $(\Delta x)^2\,V'''(\langle x\rangle)$: it is small when the wavepacket is narrow relative to the scale on which the force varies. When this condition holds, quantum expectation values obey classical equations of motion. When it fails — for example, near a caustic in a double-well potential — the quantum system departs qualitatively from classical trajectories.

The **classical limit** of quantum mechanics is the limit of narrow wavepackets relative to the scale of variation of the potential, not simply the limit $\hbar \to 0$ (which is technically subtle). Ehrenfest's theorem makes this operational.

---

### When each picture is convenient: a practical guide

| Problem type | Natural picture | Reason |
|---|---|---|
| Wave equation, numerical simulation | Schrödinger | $\psi(x,t)$ is directly computed |
| Equations of motion for observables | Heisenberg | Operators obey ODEs resembling classical mechanics |
| Free particle, harmonic oscillator | Heisenberg | Exact classical-looking solutions for operators |
| Spin precession, NMR | Either | Schrödinger gives $|\psi(t)\rangle$ directly; Heisenberg gives $\langle\vec{S}(t)\rangle$ via vector precession |
| Time-dependent perturbation theory | Interaction (Dirac) | Interaction picture separates free evolution (in operators) from perturbation (in states) |
| Quantum field theory | Heisenberg | Field operators at each spacetime point satisfy local equations of motion |

The **interaction picture** (Dirac picture) is a hybrid: split $\hat{H} = \hat{H}_0 + \hat{H}_1$. Operators evolve under $\hat{H}_0$ (as in the Heisenberg picture for the free part), and states evolve under $\hat{H}_1$ in the rotating frame. This is the starting point for Fermi's golden rule and the Dyson series. It appears explicitly when this volume reaches time-dependent perturbation theory.

---

## Worked Example: Ehrenfest Failure — Spreading in a Double Well

**Setup.** A wavepacket centered at $\langle x\rangle = 0$ with width $\sigma_x$ in a quartic potential $V(x) = -ax^2 + bx^4$ (double well). Near the local maximum at $x = 0$, $\partial^2 V/\partial x^2 = -2a < 0$ (the potential is concave). The Ehrenfest correction to Newton's law involves $V'''$ (vanishes by symmetry at $x = 0$) and $V^{(4)} = 24b$ times $(\Delta x)^2/2$:

$$\frac{d\langle\hat{p}\rangle}{dt} \approx -\frac{\partial V}{\partial\langle x\rangle} - \frac{1}{6}(\Delta x)^2\left\langle\frac{\partial^3 V}{\partial x^3}\right\rangle + \cdots$$

At $\langle x\rangle = 0$, the leading correction vanishes by symmetry, but the wavepacket splits: part tunnels left, part tunnels right. The expectation value $\langle x\rangle$ stays at $0$ — because the wavefunction is symmetric — while the classical particle would fall to one of the two minima. Ehrenfest gives the right answer ($\langle x\rangle = 0$) for the wrong reason: the packet has bifurcated, not stayed at the top. This is the limit of the classical analogy.

**The lesson.** Ehrenfest's theorem is exact as stated. What fails is the interpretation that $\langle\hat{x}\rangle$ follows a classical trajectory. When the wavepacket spreads significantly compared to the scale of potential variation, the expectation value is no longer the same as the position of a classical particle with the same initial conditions.

**The limit.** For the harmonic oscillator, all the corrections $V^{(n)}$ for $n \geq 3$ vanish because the potential is exactly quadratic. Ehrenfest is exact for the oscillator: $\langle\hat{x}(t)\rangle = \langle\hat{x}(0)\rangle\cos\omega t + (\langle\hat{p}(0)\rangle/m\omega)\sin\omega t$ regardless of the initial wavepacket shape. This is one reason the harmonic oscillator is so important: it is the unique potential for which quantum dynamics of expectation values is identical to classical mechanics.

---

## Common Misconceptions

**"The Schrödinger picture is more fundamental than the Heisenberg picture."**
They are unitarily equivalent and describe identical physics. Heisenberg's formulation (matrix mechanics, 1925) is historically earlier than Schrödinger's wave equation (1926). The Heisenberg picture is the preferred language in quantum field theory. Neither is more fundamental.

**"In the Heisenberg picture, the state does not evolve, so nothing is happening."**
The state is fixed, but operators evolve. Observable quantities — expectation values — change with time, computed as $\langle\psi_H|\hat{A}_H(t)|\psi_H\rangle$. "Nothing changes" in the state vector does not mean "nothing observable changes."

**"$d\hat{A}_H/dt = (i/\hbar)[\hat{H}, \hat{A}_H]$ is the same as $d\langle\hat{A}\rangle/dt = (i/\hbar)\langle[\hat{H}, \hat{A}]\rangle$."**
The first is an *operator equation* — both sides are operators. The second is obtained by taking the expectation value of the first. They are related but distinct: the operator equation implies the expectation-value equation, but not vice versa. Students who confuse the two sometimes try to "solve" the Ehrenfest equation for the state, which it does not determine.

**"Ehrenfest's theorem says quantum mechanics reduces to classical mechanics."**
Ehrenfest's theorem says: the expectation value of the force equals the force at the expectation value of position, to leading order in the wavepacket width. Classical mechanics is the approximation in which all wavepackets are sharp. For a nonlinear potential, quantum expectation values and classical trajectories diverge as soon as the wavepacket spreads enough to "feel" the curvature of the force.

**"The time-evolution operator $e^{-i\hat{H}t/\hbar}$ is easy to compute."**
It is, for systems where $\hat{H}$ is diagonal (energy eigenstates known). For most interesting systems, computing $e^{-i\hat{H}t/\hbar}$ is equivalent to solving the Schrödinger equation — nontrivial. The two-level and harmonic-oscillator examples in this chapter are solvable precisely because the eigenbasis is known analytically.

---

## Exercises

### Warm-up

**4.1** Starting from $\hat{U}(dt) = \hat{I} - (i/\hbar)\hat{H}\,dt$, show that $\hat{U}(t+dt) = \hat{U}(dt)\hat{U}(t)$ implies $i\hbar\,d\hat{U}/dt = \hat{H}\hat{U}$. Then differentiate $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$ to recover the Schrödinger equation. State explicitly where the Hermiticity of $\hat{H}$ enters the argument. *(Tests: can derive the Schrödinger equation from the infinitesimal step; understands the role of Hermiticity)*

**4.2** For a system with two energy levels $E_1 < E_2$, initial state $|\psi(0)\rangle = (|E_1\rangle + |E_2\rangle)/\sqrt{2}$. (a) Write $|\psi(t)\rangle$ explicitly. (b) Compute $\langle\hat{H}\rangle(t)$. (c) Compute a general observable $\langle\hat{A}\rangle(t)$ in terms of the matrix elements $A_{mn} = \langle E_m|\hat{A}|E_n\rangle$ and the transition frequency $\omega_{12} = (E_2 - E_1)/\hbar$. (d) At what frequency does $\langle\hat{A}\rangle$ oscillate? *(Tests: can apply the general time-evolution formula; identifies the beat frequency)*

**4.3** Verify that $[\hat{x}_H(t), \hat{p}_H(t)] = i\hbar$ for the free particle using $\hat{x}_H(t) = \hat{x} + \hat{p}t/m$ and $\hat{p}_H(t) = \hat{p}$. Which commutators vanish, and why? *(Tests: can execute the commutator calculation in the Heisenberg picture; verifies the fundamental algebra is preserved)*

### Application

**4.4** A spin-$\tfrac{1}{2}$ particle in a magnetic field along $\hat{z}$ has Hamiltonian $\hat{H} = \omega_0\hat{S}_z$. (a) Find the time-evolution operator $\hat{U}(t)$. (b) Evolve the initial state $|\psi(0)\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. (c) Compute $\langle\hat{S}_x\rangle(t)$, $\langle\hat{S}_y\rangle(t)$, $\langle\hat{S}_z\rangle(t)$. (d) Describe the motion geometrically: what does the Bloch vector do? *(Tests: can apply time evolution to a two-level system; connects to Larmor precession)*

**4.5** (Heisenberg picture for the harmonic oscillator) Starting from $[\hat{x}, \hat{p}] = i\hbar$ and $\hat{H} = \hat{p}^2/2m + m\omega^2\hat{x}^2/2$:
(a) Derive $d\hat{x}_H/dt = \hat{p}_H/m$ and $d\hat{p}_H/dt = -m\omega^2\hat{x}_H$ using the Heisenberg equation of motion.
(b) Solve the coupled ODEs to get $\hat{x}_H(t)$ and $\hat{p}_H(t)$ in terms of $\hat{x}_H(0) = \hat{x}$ and $\hat{p}_H(0) = \hat{p}$.
(c) Compute $\langle\hat{x}_H(t)\rangle$ and $\langle\hat{p}_H(t)\rangle$ for an initial coherent state $|\alpha\rangle$ with $\langle\hat{x}\rangle = x_0$ and $\langle\hat{p}\rangle = p_0$.
(d) Compare to the classical harmonic oscillator trajectory $x(t) = x_0\cos\omega t + (p_0/m\omega)\sin\omega t$. *(Tests: can execute the Heisenberg-picture derivation for the oscillator without using energy eigenstates)*

**4.6** Use Ehrenfest's theorem to show that for a particle in a harmonic potential $V(x) = \frac{1}{2}m\omega^2 x^2$, the expectation values $\langle\hat{x}\rangle(t)$ and $\langle\hat{p}\rangle(t)$ satisfy *exactly* the classical equations of motion, regardless of the shape of the initial wavepacket. Why does this argument fail for $V(x) = \lambda x^4$? *(Tests: can apply Ehrenfest to identify when quantum and classical dynamics coincide)*

### Apply+

**4.7** (Switching pictures) In the Schrödinger picture, the state at time $t$ is $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$.
(a) Write the Heisenberg-picture position operator $\hat{x}_H(t)$ and show that $\langle\psi(0)|\hat{x}_H(t)|\psi(0)\rangle = \langle\psi(t)|\hat{x}|\psi(t)\rangle$.
(b) For $\hat{H} = \hat{p}^2/2m$, compute $\hat{x}_H(t)$ and verify: $\langle\hat{x}_H(t)\rangle$ gives the same time dependence as $\langle\hat{x}\rangle(t)$ computed from a Gaussian wavepacket in the Schrödinger picture (the center moves at constant velocity, even as the packet spreads). *(Tests: can perform the picture switch and verify equivalence explicitly)*

**4.8** (Constants of motion) Consider the Hamiltonian $\hat{H} = \hat{p}^2/2m + V(\hat{x})$ for a general potential. (a) Show that $[\hat{H}, \hat{p}] = i\hbar\,\partial V/\partial x$ using the same test-function method as for $[\hat{x}, \hat{p}]$. (b) Identify the condition on $V$ for $\hat{p}$ to be a constant of motion. (c) Show that the angular momentum $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$ is a constant of motion for any central potential $V(r)$ by computing $[\hat{H}, \hat{L}_z]$. *(Tests: can derive commutators involving the potential; connects commutator algebra to Noether's theorem)*

### Produce

**4.9** Write a two-page derivation (in complete sentences, not just equations) of the Heisenberg picture: start from the requirement that expectation values must be the same in any picture, define $\hat{A}_H(t)$ to achieve this, derive the Heisenberg equation of motion, and verify that the canonical commutation relation is preserved. Identify the one property of $\hat{H}$ used to simplify $\hat{H}_H = \hat{H}$, and explain what would change if $\hat{H}$ depended explicitly on time. *(Tests: can articulate the logic of the Heisenberg picture in prose as well as equations — a synthesis exercise)*

---

## Still Puzzling

**What happens when $\hat{H}$ depends on time?** The formula $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ requires $\hat{H}$ to be time-independent. For a time-dependent Hamiltonian, the time-ordering operator is required: $\hat{U}(t) = \mathcal{T}\exp(-i\int_0^t\hat{H}(t')dt'/\hbar)$, where $\mathcal{T}$ orders operators with earlier times to the right. This is the starting point for the Dyson series in time-dependent perturbation theory.

**The interaction picture.** When $\hat{H} = \hat{H}_0 + \hat{H}_1$ with $\hat{H}_0$ solvable and $\hat{H}_1$ a small perturbation, neither pure Schrödinger nor pure Heisenberg picture is computationally ideal. The **interaction (Dirac) picture** puts operators in the Heisenberg picture for $\hat{H}_0$ and states in the Schrödinger picture for $\hat{H}_1$ only. The resulting evolution equation for states is $i\hbar\,d|\psi_I\rangle/dt = \hat{H}_{1,I}(t)|\psi_I\rangle$, where $\hat{H}_{1,I}(t) = e^{i\hat{H}_0 t/\hbar}\hat{H}_1 e^{-i\hat{H}_0 t/\hbar}$ is the perturbation in the Heisenberg frame of the free system. This is the natural language for Fermi's golden rule [verify: Townsend Ch. 5, Sakurai §5.5].

**Open quantum systems.** When a quantum system is coupled to an environment (a "bath"), the Heisenberg equation of motion acquires a noise term: the quantum Langevin equation. In the Schrödinger picture, the density matrix evolves under the Lindblad master equation. Both descriptions are active research tools in quantum optics and quantum computing. The two pictures remain equivalent for the expectation values of system operators, but each reveals different physics of the dissipation.

**Can commutation relations be broken by time evolution?** No — unitarity of $\hat{U}(t)$ guarantees that any commutation relation preserved at $t = 0$ is preserved for all $t$. This is a consistency requirement that limits what time-evolution operators can look like, and it is why non-unitary evolutions (which arise for open systems coupled to environments) require special treatment.

---

## The +1 — Simulation Exercise: Two-Picture Dynamics Explorer

The chapter's deliverable is `05-two-pictures.html`: a side-by-side interactive visualization of the Schrödinger and Heisenberg pictures for a spin-$\tfrac{1}{2}$ in a magnetic field, displaying both the evolving state (Bloch sphere, Schrödinger picture) and the evolving operator (expectation value trajectory, Heisenberg picture), confirming they agree.

### Part 1 — CLAUDE.md extension

```
## Chapter 4 — Two-Picture Dynamics Rules

- Single HTML file, D3 v7 from CDN, SVG canvas only.
- Two panels side by side:
  (1) Schrödinger picture (left): Bloch sphere showing the evolving state
      |ψ(t)⟩ as a moving arrow. The state is computed via exact closed-form
      U(t) = exp(−iHt/ℏ) for H = ω₀(B_x σ_x + B_y σ_y + B_z σ_z).
      Use Rodrigues formula: Bloch vector rotates around B̂ at angular
      velocity ω₀|B|. Display (θ(t), φ(t)) numerically.
  (2) Heisenberg picture (right): time-series plot of ⟨S_x⟩(t), ⟨S_y⟩(t),
      ⟨S_z⟩(t) as three colored lines on [0, 4π/ω₀]. Also draw the
      Heisenberg-picture "operator vector" ⟨S(t)⟩ as a point on a separate
      small Bloch sphere (same as the Schrödinger sphere — they are identical).
- Cross-verification label: "Schrödinger ⟨S_z⟩ = Heisenberg ⟨S_z⟩ = X.XXX ℏ"
  Both values computed independently and compared; display red if |diff| > 1e-4.
- Controls: sliders for B_x, B_y, B_z (−1 to 1), ω₀ (0.1 to 10), initial
  (θ₀, φ₀) of the state, and a play/pause/reset button.
- Time step: use requestAnimationFrame with fixed dt = 0.01/ω₀; update
  Bloch angles by the Rodrigues formula (exact, no drift).
```

### Part 2 — The simulation prompt

```
Build me a D3 v7 Two-Picture Dynamics Explorer following CLAUDE.md.

SHOW.
A spin-1/2 in H = ω₀(B_x Ŝ_x + B_y Ŝ_y + B_z Ŝ_z) evolves in time.
Schrödinger picture: |ψ(t)⟩ = U(t)|ψ(0)⟩; the Bloch vector rotates
  around B̂ at angular velocity ω₀|B|.
Heisenberg picture: ⟨A⟩(t) = ⟨ψ(0)|A_H(t)|ψ(0)⟩; computed as
  the same Bloch-vector rotation applied to the initial expectation values.
Both must give identical ⟨S_x⟩(t), ⟨S_y⟩(t), ⟨S_z⟩(t).

SAY.
Produce 05-two-pictures.html.
  Left panel: Bloch sphere (isometric), state arrow precessing. Trail of
    last 200 frames fades from current color to transparent.
  Right panel: three time-series lines (S_x: blue, S_y: green, S_z: red)
    scrolling in a 600×300 plot. A vertical cursor shows "now."
    Below: ⟨S_z⟩ from Schrödinger vs Heisenberg, must match.
  Bottom: slider panel for B_x, B_y, B_z, ω₀, θ₀, φ₀.

CONSTRAIN.
- Use ONLY the Rodrigues rotation formula for time evolution:
    r(t) = r₀ cos(ωt) + (n̂ × r₀) sin(ωt) + n̂(n̂·r₀)(1−cos(ωt))
  where n̂ = B/|B|, ω = ω₀|B|, r₀ is the initial Bloch vector.
  Never accumulate numerical integration errors.
- For the time-series, store the last 400 time-steps and draw with D3 line.
- Cross-check: at each frame compute ⟨S_z⟩ two ways:
    (1) from the Bloch vector z-component (Schrödinger picture)
    (2) from r₀·ẑ cos(ωt) + (n̂×r₀)·ẑ sin(ωt) + (n̂·ẑ)(n̂·r₀)(1−cos(ωt))
         (Heisenberg picture, operators evolved, initial state fixed)
  Label the difference. It must be < 1e-6 at all times.

VERIFY. Give four checks:
(a) B = (0,0,1), θ₀=π/2, φ₀=0: ⟨S_z⟩ = 0 constant, ⟨S_x⟩ oscillates at ω₀.
(b) B = (1,0,0), θ₀=0 (north pole): state stays at north pole (aligned
    with precession axis), all expectation values constant.
(c) |Bloch vector|² = 1 at every frame (normalization).
(d) Schrödinger and Heisenberg ⟨S_z⟩ differ by < 1e-6 at every frame.

Failure modes: Rodrigues drift (normalization check catches it),
  wrong precession axis (check (b) catches it), picture cross-check failure.
```

### Part 3 — Exploration tasks

**Verify picture equivalence.** Set $\vec{B} = (0,0,1)$, initial state on the equator ($\theta_0 = \pi/2$, $\phi_0 = 0$). Watch the Schrödinger-picture arrow precess around $\hat{z}$ at $\omega_0$. Read $\langle S_z\rangle$ from both panels — it must be identically zero at every frame. This is the picture-equivalence check made visual.

**Stationary state.** Set $\vec{B} = (0,0,1)$, initial state at the north pole ($\theta_0 = 0$). The arrow does not move; the time-series $\langle S_z\rangle = \hbar/2$ is a flat line. This is a stationary state: the initial state is an energy eigenstate of $\hat{H} = \omega_0\hat{S}_z$.

**Rabi oscillation.** Set $\vec{B} = (1,0,0)$, initial state at the north pole ($\theta_0 = 0$). The field is along $\hat{x}$, not $\hat{z}$. The Bloch vector precesses around $\hat{x}$: $\langle S_z\rangle(t) = (\hbar/2)\cos(\omega_0 t)$ oscillates between $+\hbar/2$ and $-\hbar/2$. This is the Rabi oscillation derived analytically in the chapter.

**Ehrenfest for spin.** For a spin in a magnetic field, the Hamiltonian is linear in $\hat{S}_z$. The Ehrenfest equations for $\langle\vec{S}\rangle$ are exact:

$$\frac{d\langle\vec{S}\rangle}{dt} = \gamma\langle\vec{S}\rangle \times \vec{B}.$$

This is the classical precession equation for a magnetic moment. Verify: the length $|\langle\vec{S}\rangle|$ is constant throughout the simulation (it should be). The fact that the quantum expectation value precesses exactly as a classical magnetic moment — with no corrections — is a consequence of the linearity of the Hamiltonian in the spin operators, the same reason Ehrenfest is exact for the harmonic oscillator.

---

## References

Heisenberg, W. (1925). Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen. *Zeitschrift für Physik*, **33**, 879. https://doi.org/10.1007/BF01328377 — the original matrix mechanics paper. [verify: open access via Springer Legacy]

Born, M., & Jordan, P. (1925). Zur Quantenmechanik. *Zeitschrift für Physik*, **34**, 858. https://doi.org/10.1007/BF01328531 — recognized Heisenberg's multiplication table as matrix algebra and derived $[\hat{x},\hat{p}] = i\hbar$. [verify]

Schrödinger, E. (1926). Über das Verhältnis der Heisenberg-Born-Jordanschen Quantenmechanik zu der meinen. *Annalen der Physik*, **384**(8), 734. https://doi.org/10.1002/andp.19263840804 — proved the equivalence of matrix mechanics and wave mechanics. [verify]

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Ch. 4: time evolution, two-level Rabi example (Ex. 4.2), and the generalized Ehrenfest theorem (§1.8 in lecture notes). Primary local source.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. Ch. 2 "Quantum Dynamics": definitive graduate reference for $\hat{U}(t)$, the Schrödinger, Heisenberg, and interaction pictures, Ehrenfest's theorem, and the harmonic oscillator in the Heisenberg picture with ladder operators.

Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §2.1–2.3, §3.6: time evolution and Ehrenfest's theorem at the introductory undergraduate level.

Ehrenfest, P. (1927). Bemerkung über die angenäherte Gültigkeit der klassischen Mechanik innerhalb der Quantenmechanik. *Zeitschrift für Physik*, **45**, 455. https://doi.org/10.1007/BF01329203 — the original Ehrenfest paper. [verify]

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1991). *Quantum Mechanics* (Vol. 1). Wiley. Ch. III: the time-evolution postulate and the Schrödinger/Heisenberg pictures in careful mathematical detail. [verify: standard reference]
