# Chapter 4 — Quantum Dynamics: Time Evolution and the Pictures


## Where the Schrödinger Equation Comes From

The time-evolution operator advances any state from $t = 0$ to time $t$:

$$|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle.$$

Two requirements fix the form of $\hat{U}(t)$ completely.

**First, probability is conserved.** The norm of the state cannot change:

$$\langle\psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger(t)\hat{U}(t)|\psi(0)\rangle = 1.$$

This must hold for every initial state, so $\hat{U}^\dagger(t)\hat{U}(t) = \hat{I}$: the time-evolution operator must be **unitary**.

**Second, time evolution is continuous.** For an infinitesimal step $dt$, the most general unitary operator that equals $\hat{I}$ at $t = 0$ is

$$\hat{U}(dt) = \hat{I} - \frac{i}{\hbar}\hat{H}\,dt,$$

where $\hat{H}$ is some operator. Unitarity to first order requires $\hat{H}^\dagger = \hat{H}$: the generator must be Hermitian. Physical dimensions require the factor $\hbar$; the operator $\hat{H}$ has units of energy and is the Hamiltonian. For time-independent $\hat{H}$, composing infinitesimal steps gives the matrix exponential:

$$\boxed{\hat{U}(t) = e^{-i\hat{H}t/\hbar}.}$$

The Schrödinger equation is not a separate postulate. Differentiate $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$ with respect to $t$:

$$i\hbar\,\frac{d}{dt}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle.$$

It is the statement that $\hat{U}(t)$ satisfies its own differential equation. The Schrödinger equation, stationary states, and energy quantization all follow from unitarity plus a Hermitian generator.

---

## Stationary States and General Time Evolution

If $|\psi(0)\rangle = |E_n\rangle$ is an energy eigenstate with $\hat{H}|E_n\rangle = E_n|E_n\rangle$, then

$$e^{-i\hat{H}t/\hbar}|E_n\rangle = e^{-iE_n t/\hbar}|E_n\rangle.$$

The state picks up a phase but does not change. Every expectation value is constant — a stationary state.

For a general initial state $|\psi(0)\rangle = \sum_n c_n|E_n\rangle$:

$$|\psi(t)\rangle = \sum_n c_n\,e^{-iE_n t/\hbar}|E_n\rangle.$$

Procedure: expand in energy eigenstates, attach phase $e^{-iE_n t/\hbar}$ to each component, reassemble. All dynamics is in the relative phases between energy eigenstates. A single eigenstate has no relative phase — hence stationary. Two or more eigenstates create a beat frequency $(E_m - E_n)/\hbar$ that drives oscillation in every observable.

---

## Worked Example — Rabi Oscillation

**Given.** Spin-½ particle with Hamiltonian $\hat{H} = \omega_0\hat{S}_x = (\omega_0\hbar/2)\sigma_x$. Initial state: $|\!\uparrow\rangle$.

**Find.** $|\psi(t)\rangle$ and $\langle\hat{S}_z\rangle(t)$.

**Solution.**

The eigenstates of $\hat{S}_x$ are $|x\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$ with eigenvalues $\pm\hbar\omega_0/2$. Expand the initial state:

$$|\!\uparrow\rangle = \frac{1}{\sqrt{2}}\bigl(|x+\rangle + |x-\rangle\bigr).$$

Attach phase factors and convert back to the $\hat{S}_z$ basis:

$$|\psi(t)\rangle = \cos\!\left(\frac{\omega_0 t}{2}\right)|\!\uparrow\rangle - i\sin\!\left(\frac{\omega_0 t}{2}\right)|\!\downarrow\rangle.$$

The expectation value of $\hat{S}_z$ oscillates:

$$\langle\hat{S}_z\rangle(t) = \frac{\hbar}{2}\cos(\omega_0 t).$$

**Check.** Population starts in $|\!\uparrow\rangle$, reaches $|\!\downarrow\rangle$ at $t = \pi/\omega_0$, and returns. This is Rabi oscillation — the spin driven by a resonant field oscillates at the Rabi frequency $\omega_0$. The physics is a beat between two energy eigenstates.

---

## The Heisenberg Picture

Both pictures must agree on every expectation value:

$$\langle\hat{A}\rangle(t) = \langle\psi(t)|\hat{A}|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger(t)\hat{A}\hat{U}(t)|\psi(0)\rangle.$$

The Schrödinger picture assigns all time dependence to the state: $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$, operators fixed. The Heisenberg picture does the opposite: freeze the state at its $t = 0$ value and assign all time dependence to the operator.

**Definition.** The Heisenberg-picture operator is

$$\hat{A}_H(t) = \hat{U}^\dagger(t)\,\hat{A}\,\hat{U}(t).$$

The state in the Heisenberg picture is $|\psi(0)\rangle$, frozen. Then:

$$\langle\psi(0)|\hat{A}_H(t)|\psi(0)\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{A}\hat{U}|\psi(0)\rangle = \langle\hat{A}\rangle(t). \checkmark$$

The two pictures are related by a unitary transformation — a change of basis in time. All algebraic relations are preserved. In particular:

$$[\hat{x}_H(t), \hat{p}_H(t)] = \hat{U}^\dagger[\hat{x}, \hat{p}]\hat{U} = i\hbar.$$

The canonical commutation relation holds at every time. Switching pictures cannot change the fundamental algebra.

---

## The Heisenberg Equation of Motion

Differentiate $\hat{A}_H(t) = \hat{U}^\dagger\hat{A}\hat{U}$ with respect to $t$. Using $d\hat{U}/dt = (-i\hat{H}/\hbar)\hat{U}$ and its adjoint:

$$\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}\hat{U}^\dagger[\hat{H}, \hat{A}]\hat{U} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H],$$

where $\hat{H}_H = \hat{U}^\dagger\hat{H}\hat{U} = \hat{H}$ because $\hat{H}$ commutes with functions of itself. Therefore:

$$\boxed{i\hbar\,\frac{d\hat{A}_H}{dt} = [\hat{A}_H,\, \hat{H}].}$$

This is the **Heisenberg equation of motion** — an *operator* equation. Compare it to Hamilton's classical equations $\dot{x} = \{x, H\}$, $\dot{p} = \{p, H\}$, where $\{f,g\}$ is the Poisson bracket. The quantum equation is the classical one with the Poisson bracket replaced by the commutator divided by $i\hbar$:

$$\{f, g\}_\text{classical} \longleftrightarrow \frac{1}{i\hbar}[\hat{f}, \hat{g}]_\text{quantum}.$$

This is Dirac's quantization dictionary, and it works in both directions.

One immediate consequence: if $[\hat{H}, \hat{A}] = 0$, then $\hat{A}$ is a constant of motion — the quantum version of Noether's theorem.

---

## Worked Example — Free Particle in the Heisenberg Picture

**Given.** $\hat{H} = \hat{p}^2/2m$.

**Find.** $\hat{p}_H(t)$ and $\hat{x}_H(t)$.

**Solution.**

$$i\hbar\,\frac{d\hat{p}_H}{dt} = [\hat{p}_H, \hat{p}_H^2/2m] = 0, \qquad \hat{p}_H(t) = \hat{p}.$$

Momentum is conserved. For position, using $[\hat{x}, \hat{p}^2] = 2i\hbar\hat{p}$:

$$\frac{d\hat{x}_H}{dt} = \frac{\hat{p}_H}{m} = \frac{\hat{p}}{m}.$$

Since $\hat{p}_H$ is constant, integrating directly:

$$\hat{x}_H(t) = \hat{x}(0) + \frac{\hat{p}}{m}\,t.$$

**Check.** The position operator obeys Newton's first law exactly: $x = x_0 + v_0 t$, with operators in place of numbers. In the Schrödinger picture the wavepacket spreads — $\sigma_x$ grows with time. The Heisenberg picture describes only the motion of the expectation value; the two pictures are complementary.

---

## Worked Example — Harmonic Oscillator in the Heisenberg Picture

**Given.** $\hat{H} = \hat{p}^2/2m + m\omega^2\hat{x}^2/2$.

**Find.** $\hat{x}_H(t)$ and $\hat{p}_H(t)$.

**Solution.**

The Heisenberg equations give:

$$\frac{d\hat{x}_H}{dt} = \frac{\hat{p}_H}{m}, \qquad \frac{d\hat{p}_H}{dt} = -m\omega^2\hat{x}_H.$$

Eliminate $\hat{p}_H$:

$$\frac{d^2\hat{x}_H}{dt^2} = -\omega^2\hat{x}_H.$$

Solve with initial conditions $\hat{x}_H(0) = \hat{x}$, $\hat{p}_H(0) = \hat{p}$:

$$\hat{x}_H(t) = \hat{x}\cos(\omega t) + \frac{\hat{p}}{m\omega}\sin(\omega t),$$
$$\hat{p}_H(t) = \hat{p}\cos(\omega t) - m\omega\hat{x}\sin(\omega t).$$

**Check.** Verify $[\hat{x}_H(t), \hat{p}_H(t)] = i\hbar$ at all $t$: expanding using $[\hat{x},\hat{p}] = i\hbar$ and $\cos^2 + \sin^2 = 1$ gives exactly $i\hbar$. Commutation relation preserved — as unitarity guarantees.

In terms of ladder operators $\hat{a} = (m\omega\hat{x} + i\hat{p})/\sqrt{2m\omega\hbar}$:

$$\hat{a}_H(t) = \hat{a}\,e^{-i\omega t}, \qquad \hat{a}^\dagger_H(t) = \hat{a}^\dagger\,e^{+i\omega t}.$$

Coherent states — eigenstates of $\hat{a}$ — have expectation values tracing exact classical orbits: the most classical quantum states of the oscillator.

---

## Ehrenfest's Theorem

Take the expectation value of the Heisenberg equation:

$$\frac{d}{dt}\langle\hat{A}\rangle = \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle.$$

Apply with $\hat{A} = \hat{x}$: since $[\hat{p}^2/2m, \hat{x}] = -i\hbar\hat{p}/m$,

$$\frac{d\langle\hat{x}\rangle}{dt} = \frac{\langle\hat{p}\rangle}{m}.$$

Apply with $\hat{A} = \hat{p}$: since $[V(\hat{x}), \hat{p}] = i\hbar\,\partial V/\partial x$,

$$\frac{d\langle\hat{p}\rangle}{dt} = -\left\langle\frac{\partial V}{\partial x}\right\rangle.$$

This resembles Newton's second law, but with the force evaluated at the *expectation value of position* replaced by the *expectation value of the force*. These are equal only when $\partial V/\partial x$ is linear in $x$ — the harmonic oscillator and the free particle. For a general potential:

$$-\left\langle\frac{\partial V}{\partial x}\right\rangle \neq -\frac{\partial V}{\partial\langle x\rangle}.$$

The difference is of order $(\Delta x)^2 V'''(\langle x\rangle)$. When the wavepacket is narrow relative to the scale on which the force varies, the approximation holds and expectation values follow classical trajectories. For the harmonic oscillator, $V^{(n)} = 0$ for all $n \geq 3$: the potential is exactly quadratic. Ehrenfest is exact; the expectation value follows the classical orbit exactly, regardless of initial state.

---

## Which Picture to Use

**Schrödinger picture:** natural when the wave function is needed directly — bound-state problems, numerical simulation, anything involving $\psi(x,t)$.

**Heisenberg picture:** natural for equations of motion of observables — produces operator equations resembling classical mechanics, making the classical limit transparent; clean algebraic solutions for the harmonic oscillator; standard in quantum field theory, where Schrödinger-picture wavefunctionals are unwieldy.

**Interaction picture:** splits $\hat{H} = \hat{H}_0 + \hat{H}_1$; operators evolve under $\hat{H}_0$, states evolve under $\hat{H}_1$ only. Natural language for time-dependent perturbation theory and Fermi's golden rule.

---

## The +1 — Simulation Exercise: Two-Picture Dynamics Explorer

The deliverable is `05-two-pictures.html`: a side-by-side visualization of the Schrödinger and Heisenberg pictures for a spin-½ in a magnetic field, showing the evolving state (Bloch sphere) alongside the evolving expectation values (time series), with a live cross-check that both computations agree.

### Part 1 — CLAUDE.md extension

````markdown
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
````

### Part 2 — The simulation prompt

````
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
(a) B=(0,0,1), θ₀=π/2, φ₀=0: ⟨S_z⟩=0 constant, ⟨S_x⟩ oscillates at ω₀.
(b) B=(1,0,0), θ₀=0 (north pole): state stays at north pole (aligned with
    precession axis), all expectation values constant.
(c) |Bloch vector|²=1 at every frame (normalization).
(d) Schrödinger and Heisenberg ⟨S_z⟩ differ by < 1e-6 at every frame.

Failure modes: Rodrigues drift (normalization check catches it),
  wrong precession axis (check (b) catches it), picture cross-check failure.
````

### Part 3 — Exploration tasks

**Picture equivalence.** Set $\vec{B} = (0,0,1)$, initial state on the equator ($\theta_0 = \pi/2$, $\phi_0 = 0$). Watch the Schrödinger-picture arrow precess around $\hat{z}$ at $\omega_0$. Read $\langle S_z\rangle$ from both panels — identically zero at every frame. This is picture equivalence made visible.

**Stationary state.** Set $\vec{B} = (0,0,1)$, initial state at the north pole ($\theta_0 = 0$). The arrow does not move; $\langle S_z\rangle = \hbar/2$ is a flat line. The initial state is an energy eigenstate of $\hat{H} = \omega_0\hat{S}_z$, so it is stationary.

**Rabi oscillation.** Set $\vec{B} = (1,0,0)$, initial state at the north pole. The field is along $\hat{x}$, not $\hat{z}$. The Bloch vector precesses around $\hat{x}$: $\langle S_z\rangle(t) = (\hbar/2)\cos(\omega_0 t)$ oscillates between $\pm\hbar/2$. This is the Rabi oscillation derived analytically above.

**Ehrenfest for spin.** For a spin in a magnetic field, the Ehrenfest equations for $\langle\vec{S}\rangle$ are exact: $d\langle\vec{S}\rangle/dt = \gamma\langle\vec{S}\rangle \times \vec{B}$ — classical precession. Verify: the length $|\langle\vec{S}\rangle|$ stays constant throughout. This follows from the linearity of the Hamiltonian in the spin operators, the same reason Ehrenfest is exact for the harmonic oscillator.

---

## References

- Heisenberg, W. (1925). Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen. *Zeitschrift für Physik*, **33**, 879. https://doi.org/10.1007/BF01328377
- Born, M., & Jordan, P. (1925). Zur Quantenmechanik. *Zeitschrift für Physik*, **34**, 858. https://doi.org/10.1007/BF01328531
- Schrödinger, E. (1926). Über das Verhältnis der Heisenberg-Born-Jordanschen Quantenmechanik zu der meinen. *Annalen der Physik*, **384**(8), 734. https://doi.org/10.1002/andp.19263840804
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Ch. 4.
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 2.
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §2.1–2.3, §3.6.
- Ehrenfest, P. (1927). Bemerkung über die angenäherte Gültigkeit der klassischen Mechanik innerhalb der Quantenmechanik. *Zeitschrift für Physik*, **45**, 455. https://doi.org/10.1007/BF01329203
- Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. 1. Wiley. Ch. III.

---

## Running Project — Build the Atom

**This chapter adds:** the stationarity test — the predicted ground configuration must be a stationary state of $\hat{H}_\text{eff}$, and the labels that survive as good quantum numbers are exactly the constants of motion (operators commuting with $\hat{H}_\text{eff}$); this chapter adds a check that the simulator's configuration does not evolve and that $\hat{L}^2,\hat{L}_z,\hat{S}_z$ are conserved.

The atom-builder predicts a *ground state* — a stationary configuration. From this chapter: a state evolves only by relative phases between energy eigenstates, and a single energy eigenstate is stationary, so the ground configuration's observables must be time-independent. And $[\hat H_\text{eff},\hat A]=0 \Rightarrow \hat A$ is a constant of motion: this is why $L$, $S$, $J$ (in the LS-coupling regime of Chapter 11) label the *whole atom*, not just a fleeting arrangement. This chapter's piece is the conservation check on the configuration.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Writing $\hat U(t) = \exp(-i\hat H t/\hbar)$ via the spectral decomposition and evolving a state vector — *Why AI works here:* it is the matrix-exponential pattern from Chapter 2's spectral code; you verify it leaves an energy eigenstate's $|\psi|$ unchanged and only adds a phase.
- Generating a Heisenberg-picture check that $\langle\hat A\rangle(t)$ is constant when $[\hat H,\hat A]=0$ — *Why AI works here:* it is a direct numerical instantiation of the Heisenberg equation; the expected output (a flat line) is unambiguous.

**The tell:** You are using AI well when you have an independent check — a stationary state's expectation values must be flat, and $|\langle\psi(t)|\psi(t)\rangle| = 1$ at all times (unitarity).

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding which operators *are* constants of motion for a given $\hat H_\text{eff}$ — *Why AI fails here:* whether $\hat L^2$ commutes with the effective Hamiltonian depends on the central-field assumption being exactly spherical; an LLM will assert conservation without checking the symmetry that grants it, and in the real atom (spin-orbit, non-spherical corrections) that conservation is only approximate.
- Concluding from "expectation values are flat" that the configuration is the true ground state — *Why AI fails here:* stationarity is necessary but not sufficient; *every* eigenstate is stationary, including excited configurations, so flatness alone does not certify you found the lowest energy.

**The tell:** If you cannot say why a quantity is conserved without the AI — naming the symmetry behind it — the AI did the reasoning that should have been yours.
**Physics-judgment connection:** this trains checking a dynamical claim against a conservation law and against unitarity (norm preserved) before believing the simulator reports a stable ground state.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a module `dynamics_check.py` that confirms a configuration is stationary and that the angular-momentum labels are conserved.
**Tool:** Claude chat.
**The Prompt:**
```
I am building an atomic-structure simulator. I have a one-electron Hamiltonian
matrix H (Hermitian) and the angular-momentum matrices L2, Lz from earlier
modules. I want to verify that a ground configuration is a genuine stationary
state and that L2, Lz are constants of motion.

Write a Python module `dynamics_check.py` (numpy only) that:

1. Provides U(H, t) = expm(-1j * H * t) using scipy.linalg.expm (or a spectral
   construction from eigh if you prefer no scipy).
2. Provides is_stationary(H, psi, times) returning True if, for an eigenvector
   psi of H, |<psi|U(t)|psi>| == 1 for all t in times (to 1e-9) and the
   probability distribution |psi_components|^2 is unchanged.
3. Provides conserved(H, A, tol=1e-9) returning True if [H, A] == 0 (so <A> is
   time-independent), and a helper expectation_over_time(H, A, psi, times)
   returning the list of <A>(t) so I can confirm it is flat.
4. __main__: build a 3x3 diagonal H = diag(-1.0, -0.5, 0.2), take psi = the
   ground eigenvector, and show is_stationary is True; then build a diagonal A
   that commutes with H and show expectation_over_time is flat.

Add a comment: stationarity is necessary but NOT sufficient to prove a config is
the *lowest*-energy one (excited eigenstates are stationary too). Do not assign
electrons or rank configurations.
```
**What this produces:** `dynamics_check.py` — confirms time-independence and identifies conserved labels.
**How to adapt:** *Your system:* use the spectral form $\hat U = \sum_n e^{-iE_n t/\hbar}|E_n\rangle\langle E_n|$ to avoid SciPy. *ChatGPT/Gemini:* same prompt; ask for a Rabi-style sanity test (a two-level non-eigenstate *does* oscillate). *Claude Project:* keep alongside the spectral engine.
**Builds on:** Chapter 3's conserved angular-momentum labels.  **Next:** Chapter 5 gives the actual central-field separation that produces the $\hat H_\text{eff}$ whose ground state this chapter certified stationary.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the stationarity/conservation checker plus tests.
**Tool:** Claude Code.
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `oneelectron.py` and `csco.py` in `build-the-atom/`.
- [ ] `numpy` (and `scipy` if you use `expm`).
- [ ] CLAUDE.md rules from Chapters 1–3 present.
**The Task:**
```
In build-the-atom/, create dynamics_check.py with U(H, t), is_stationary(H, psi,
times), conserved(H, A, tol), and expectation_over_time(H, A, psi, times).

Create test_dynamics.py: (a) an eigenvector of a diagonal H is stationary —
norm 1 and flat |components|^2 across times [0, 1, 5, 10]; (b) for a diagonal A
that commutes with diagonal H, <A>(t) is constant to 1e-9; (c) a non-eigenstate
superposition of two levels is NOT stationary (its |components|^2 change).

Run `pytest -q` and show output. Modify no other module.
```
**Expected output:** `dynamics_check.py`, `test_dynamics.py`, passing `pytest`.
**What to inspect:** confirm the eigenstate's component magnitudes are flat (only phases rotate); confirm the superposition test genuinely *fails* stationarity (a check that always passes is a useless check); confirm $\langle\hat A\rangle$ is flat for the commuting operator.
**If it goes wrong:** a common error is comparing complex amplitudes instead of their moduli, so phase rotation falsely reads as "changed." Recovery: compare $|c_n(t)|^2$, not $c_n(t)$ — the global phase is unobservable.
**CLAUDE.md / AGENTS.md note:** add — "A predicted ground configuration must pass `is_stationary`; remember stationarity is necessary, not sufficient — energy ranking happens separately."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `dynamics_check.py` stationarity/conservation module from R3/R4.
**Validation type:** Code / Reasoning chain
**Risk level:** Low–Medium — the check is a guard rail; its danger is a false sense of security if it conflates "stationary" with "ground."
**Setup:** use your R3/R4 artifact.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Quantum Dynamics & the Pictures
□ Correctness: does an eigenstate read as stationary (flat |components|^2)?
□ Completeness: does the suite include a NEGATIVE test (a superposition that
  is correctly flagged non-stationary)?
□ Scope: did it avoid ranking configurations or assigning electrons?
□ Physics criterion 1: is <psi(t)|psi(t)> == 1 at all times (unitarity)?
□ Physics criterion 2: is <A>(t) flat exactly when [H, A] = 0?
□ Failure-mode check: any of —
  - fluent but wrong (compares amplitudes not moduli; phase reads as change)
  - claims conservation without checking [H, A] = 0
  - treats "stationary" as proof of "ground state"
  - missing the negative test, so the check can never fail
```
**What to do with findings:** pass → use it, noting the unitarity check is what made it trustworthy; one fail → fix the modulus comparison and re-run; multiple fails → the module gives false confidence — replace it with a hand-checked version.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI implemented the time-evolution operator and the stationarity/conservation tests.
> *2:* The AI could not determine *which* operators are truly conserved for a real (non-perfectly-spherical) atom, nor that stationarity implies a ground state — both required my physical judgment.
**Physics-judgment connection:** validating a dynamical result against a conservation law and against unitarity — and refusing the tempting inference that "doesn't change" means "is the ground state."

---

*Chapter 5 follows: angular momentum. The commutation relations $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ form a Lie algebra; ladder operators built from them generate the complete spectrum of $\hat{L}^2$ and $\hat{L}_z$ without solving any differential equation. The method is the harmonic oscillator algebra applied to rotational symmetry.*
