# Worked Exercises: Quantum Dynamics — Time Evolution and the Pictures

*Chapter 4 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You know the time-evolution operator $\hat U(t) = e^{-i\hat Ht/\hbar}$ is unitary with Hermitian generator $\hat H$, and that a general state evolves by $|\psi(t)\rangle = \sum_n c_n e^{-iE_nt/\hbar}|E_n\rangle$.
- You can move between the Schrödinger picture (time on states, operators fixed) and the Heisenberg picture (state frozen at $t=0$, operators evolve as $\hat A_H(t) = \hat U^\dagger\hat A\hat U$).
- You can apply the Heisenberg equation of motion $i\hbar\,\tfrac{d\hat A_H}{dt} = [\hat A_H,\hat H]$ and Ehrenfest's theorem $\tfrac{d}{dt}\langle\hat A\rangle = \tfrac{i}{\hbar}\langle[\hat H,\hat A]\rangle$.

---

## Part A — Full Worked Example

**What this demonstrates:** That solving dynamics by transforming to the Heisenberg picture turns the equations of motion for operators into the classical equations, and that the canonical commutation relation is preserved at every time.

**The problem:** For the free particle $\hat H = \hat p^2/2m$, derive the Heisenberg-picture operators $\hat p_H(t)$ and $\hat x_H(t)$ using the Heisenberg equation of motion, and verify that $[\hat x_H(t),\hat p_H(t)] = i\hbar$ holds for all $t$.

**The solution:**

**Step 1 — Transform to the Heisenberg picture and write the equation of motion for $\hat p_H$.**
$$i\hbar\,\frac{d\hat p_H}{dt} = [\hat p_H, \hat H] = \left[\hat p_H, \frac{\hat p_H^2}{2m}\right] = 0.$$
*Why:* In the Heisenberg picture all time dependence is carried by the operators via $\hat A_H = \hat U^\dagger\hat A\hat U$; momentum commutes with any function of itself, so its equation of motion is trivially zero.
*Check:* The Heisenberg Hamiltonian equals the Schrödinger one, $\hat H_H = \hat U^\dagger\hat H\hat U = \hat H$, since $\hat H$ commutes with $\hat U = e^{-i\hat Ht/\hbar}$ ✓.

**Step 2 — Integrate to get $\hat p_H(t)$.**
$\dfrac{d\hat p_H}{dt} = 0 \implies \hat p_H(t) = \hat p_H(0) = \hat p$. Momentum is a constant of motion.
*Why:* $[\hat H,\hat p] = 0$ means $\hat p$ is conserved — the quantum version of Noether's theorem, translational symmetry giving momentum conservation.
*Check:* For the free particle the potential is flat, so classically momentum is conserved too — the operator equation reproduces the classical fact.

**Step 3 — Write and solve the equation of motion for $\hat x_H$.**
Using $[\hat x,\hat p^2] = 2i\hbar\hat p$:
$$i\hbar\,\frac{d\hat x_H}{dt} = [\hat x_H, \hat H] = \frac{1}{2m}[\hat x_H,\hat p^2] = \frac{1}{2m}(2i\hbar\hat p_H) = \frac{i\hbar}{m}\hat p_H \implies \frac{d\hat x_H}{dt} = \frac{\hat p_H}{m} = \frac{\hat p}{m}.$$
*Why:* The commutator $[\hat x,\hat p^2] = 2i\hbar\hat p$ converts the bracket into a velocity operator; since $\hat p_H = \hat p$ is constant, the right side is time-independent.
*Check:* Dimensionally $\hat p/m$ is a velocity ✓, matching $d\hat x/dt$.

**Step 4 — Integrate to get $\hat x_H(t)$.**
$$\hat x_H(t) = \hat x(0) + \frac{\hat p}{m}\,t.$$
*Why:* With a constant velocity operator, integration gives the operator analogue of $x = x_0 + v_0 t$ — Newton's first law as an operator identity.
*Check:* At $t = 0$, $\hat x_H(0) = \hat x$, recovering the Schrödinger operator as it must.

**Step 5 — Verify the canonical commutation relation is preserved.**
$$[\hat x_H(t),\hat p_H(t)] = \left[\hat x + \frac{\hat p}{m}t,\ \hat p\right] = [\hat x,\hat p] + \frac{t}{m}[\hat p,\hat p] = i\hbar + 0 = i\hbar.$$
*Why:* The two pictures are related by a unitary transformation, which preserves all algebraic relations — switching pictures cannot change the fundamental commutator.
*Check:* $[\hat x_H(t),\hat p_H(t)] = i\hbar$ independent of $t$ ✓ — exactly what unitarity guarantees.

**Final answer:** $\hat p_H(t) = \hat p$ (conserved) and $\hat x_H(t) = \hat x + \tfrac{\hat p}{m}t$, with $[\hat x_H(t),\hat p_H(t)] = i\hbar$ at all times.

**What made this work:** The central concept is that the *Heisenberg picture puts the dynamics in the operators*, producing operator equations identical in form to classical mechanics. The naive failure is to put the time dependence on the wrong object — attaching $e^{-i\hat Ht/\hbar}$ to operators while also evolving the state, or evolving operators in the Schrödinger picture. Each observable has exactly one home for its time dependence per picture; mixing them double-counts the evolution and breaks the cross-check $\langle\hat A\rangle(t) = \langle\psi(0)|\hat A_H(t)|\psi(0)\rangle = \langle\psi(t)|\hat A|\psi(t)\rangle$.

**Self-explanation prompt:** Why must $[\hat x_H(t),\hat p_H(t)] = i\hbar$ hold at every time, and which single property of $\hat U(t)$ guarantees it without any computation?

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same principle — solving for Heisenberg-picture operators from the equation of motion and confirming the commutation relation is preserved — for a different Hamiltonian.

**The problem:** For the harmonic oscillator $\hat H = \hat p^2/2m + \tfrac12 m\omega^2\hat x^2$: (a) Write the coupled Heisenberg equations for $\hat x_H$ and $\hat p_H$ using the equation of motion. (b) Decouple them into $\tfrac{d^2\hat x_H}{dt^2} = -\omega^2\hat x_H$ and solve with initial conditions $\hat x_H(0) = \hat x$, $\hat p_H(0) = \hat p$. (c) Write $\hat p_H(t)$. (d) Verify $[\hat x_H(t),\hat p_H(t)] = i\hbar$ for all $t$ using $[\hat x,\hat p] = i\hbar$ and $\cos^2 + \sin^2 = 1$. (e) Express $\hat a_H(t)$ in terms of $\hat a$ and a phase, and interpret why coherent states trace classical orbits.

**Stuck?** You will need $[\hat x,\hat p^2] = 2i\hbar\hat p$ for the $\hat x$ equation and $[\hat p,\hat x^2] = -2i\hbar\hat x$ for the $\hat p$ equation. The solution has the form $\hat x_H(t) = \hat x\cos\omega t + \tfrac{\hat p}{m\omega}\sin\omega t$.

*Instructor note: no solution is provided for Part B. Derive both operator solutions, verify the commutator is preserved at all $t$, and interpret the ladder-operator phase rotation.*

---

## Part C — Completion Problem

**The problem:** A spin-½ in a transverse field has $\hat H = \omega_0\hat S_x = \tfrac{\omega_0\hbar}{2}\sigma_x$, with initial state $|\!\uparrow\rangle$. Find $|\psi(t)\rangle$ in the Schrödinger picture and the Rabi oscillation of $\langle\hat S_z\rangle(t)$.

**Step 1 — Diagonalize $\hat H$ and expand the initial state in its eigenbasis.**
The eigenstates of $\hat S_x$ are $|x\pm\rangle = \tfrac{1}{\sqrt2}(|\!\uparrow\rangle \pm |\!\downarrow\rangle)$ with energies $\pm\hbar\omega_0/2$. Expanding:
$$|\!\uparrow\rangle = \tfrac{1}{\sqrt2}(|x+\rangle + |x-\rangle).$$
*Why:* Time evolution is simplest in the energy eigenbasis, where each component just picks up a phase $e^{-iE_nt/\hbar}$.

**Step 2 — Attach the energy phases.**
$$|\psi(t)\rangle = \tfrac{1}{\sqrt2}\bigl(e^{-i\omega_0 t/2}|x+\rangle + e^{+i\omega_0 t/2}|x-\rangle\bigr).$$
*Why:* Each energy eigenstate evolves by its own phase $e^{-iE_nt/\hbar}$ with $E_\pm = \pm\hbar\omega_0/2$; all dynamics lives in the relative phase between the two.

**Step 3 — [BLANK]** Convert $|\psi(t)\rangle$ back to the $\hat S_z$ basis $\{|\!\uparrow\rangle,|\!\downarrow\rangle\}$ and simplify using $|x\pm\rangle = \tfrac{1}{\sqrt2}(|\!\uparrow\rangle\pm|\!\downarrow\rangle)$.
*Your work here:*

*Why (your explanation):*

**Step 4 — [BLANK]** Compute $\langle\hat S_z\rangle(t) = \langle\psi(t)|\hat S_z|\psi(t)\rangle$ from the result of Step 3.
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret the result.**
The population starts in $|\!\uparrow\rangle$, sloshes entirely to $|\!\downarrow\rangle$ at $t = \pi/\omega_0$, and returns — Rabi oscillation, the dynamics at the heart of NMR. The oscillation frequency $\omega_0$ is the beat frequency $(E_+ - E_-)/\hbar$ between the two energy eigenstates.

**Final answer:** $|\psi(t)\rangle = \cos\!\tfrac{\omega_0 t}{2}|\!\uparrow\rangle - i\sin\!\tfrac{\omega_0 t}{2}|\!\downarrow\rangle$, with $\langle\hat S_z\rangle(t) = \tfrac{\hbar}{2}\cos(\omega_0 t)$.

**Self-explanation prompt:** Why does a single energy eigenstate never oscillate, while a superposition of two always does — and what sets the oscillation frequency?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked to evolve the state $|\psi(0)\rangle = \tfrac{1}{\sqrt2}(|E_1\rangle + |E_2\rangle)$ under a Hamiltonian with $\hat H|E_n\rangle = E_n|E_n\rangle$, and to compute $\langle\hat A\rangle(t)$ for some observable $\hat A$. Here is their work.

**Step 1 — Set up the evolution.**
A general state evolves as $|\psi(t)\rangle = \sum_n c_n e^{-iE_nt/\hbar}|E_n\rangle$, the Schrödinger picture. *(Correct.)*

**Step 2 — Identify the picture and what carries time.**
"I will use the Schrödinger picture, so the state $|\psi(t)\rangle$ carries the time dependence and the operator $\hat A$ stays fixed." *(Correct.)*

**Step 3 — ⚠ Build the time-evolution operator.**
"The evolution operator is $\hat U(t) = e^{+i\hat Ht/\hbar}$, so $|\psi(t)\rangle = \sum_n c_n e^{+iE_nt/\hbar}|E_n\rangle$. I'll use this to push the state forward in time."

**Step 4 — Evolve and compute.**
"Then $\langle\hat A\rangle(t) = \langle\psi(t)|\hat A|\psi(t)\rangle$ with the phases from Step 3. The cross-term oscillates at $(E_2 - E_1)/\hbar$, which has the right magnitude for a Bohr frequency." *(The oscillation magnitude is plausibly correct, masking the sign error upstream.)*

**Your tasks:**
1. Identify the precise error in Step 3 and write the correct $\hat U(t)$.
2. Explain physically what the wrong sign would mean — what direction in time does $e^{+i\hat Ht/\hbar}$ propagate, and how does it relate to $\hat U^\dagger$?
3. Show that the wrong sign still produces an oscillation at $(E_2 - E_1)/\hbar$, which is why Step 4 *looks* fine — and explain what observable consequence (e.g. the sign of $\langle\hat S_y\rangle$ or the direction of precession) would actually expose it.
4. Write the corrected $|\psi(t)\rangle$ with the proper phases.

**Why this error is common:** The sign in $\hat U(t) = e^{-i\hat Ht/\hbar}$ is fixed by requiring the Schrödinger equation $i\hbar\,\partial_t|\psi\rangle = \hat H|\psi\rangle$; flipping it gives the adjoint $\hat U^\dagger$ (backward evolution), and because $|c_n|^2$ and oscillation *magnitudes* are sign-blind, the mistake hides until a phase-sensitive observable is computed.

---

## Part E — Transfer Problem

**What this demonstrates:** The same principle — the Heisenberg equation of motion and the constant-of-motion criterion $[\hat H,\hat A] = 0$ — applied to a context not worked in the chapter: a two-level system with an energy gap, asking which observables are conserved.

**The problem:** A two-level atom has $\hat H = \tfrac{\hbar\Omega}{2}\sigma_z$ (energy splitting $\hbar\Omega$ between $|0\rangle$ and $|1\rangle$). (a) Use the Heisenberg equation $i\hbar\,\tfrac{d\hat A_H}{dt} = [\hat A_H,\hat H]$ to determine whether $\hat\sigma_z$ is a constant of motion. (b) Do the same for $\hat\sigma_x$, and solve its Heisenberg equation to find $\hat\sigma_{x,H}(t)$. (c) Interpret the result: which observable is conserved, which precesses, and at what frequency? (d) Confirm via Ehrenfest that $\langle\hat\sigma_x\rangle(t)$ oscillates while $\langle\hat\sigma_z\rangle(t)$ is flat.

**Hint (use only if stuck after 10 minutes):** You need $[\sigma_x,\sigma_z] = -2i\sigma_y$ and $[\sigma_y,\sigma_z] = 2i\sigma_x$. The $\hat\sigma_x$ equation couples to $\hat\sigma_y$, giving coupled equations whose solution rotates $\hat\sigma_x$ and $\hat\sigma_y$ into each other at frequency $\Omega$.

**Reflection prompt:**
1. The chapter states $[\hat H,\hat A] = 0 \Rightarrow \hat A$ is a constant of motion — "the quantum version of Noether's theorem." Which symmetry of $\hat H = \tfrac{\hbar\Omega}{2}\sigma_z$ is responsible for $\hat\sigma_z$ being conserved?
2. The Heisenberg-picture operators $\hat\sigma_x(t), \hat\sigma_y(t)$ precess just like the classical magnetization in NMR. How is this the spin analogue of the harmonic-oscillator result $\hat x_H(t) = \hat x\cos\omega t + \tfrac{\hat p}{m\omega}\sin\omega t$?

---

## Part F — Interleaved Review

**Problem F1.** For the harmonic oscillator, the Heisenberg ladder operators evolve as $\hat a_H(t) = \hat a\,e^{-i\omega t}$. (a) Derive this from $i\hbar\,\tfrac{d\hat a_H}{dt} = [\hat a_H,\hat H]$ using $[\hat a,\hat H] = \hbar\omega\hat a$. (b) Show $\hat x_H(t) = \hat x\cos\omega t + \tfrac{\hat p}{m\omega}\sin\omega t$ follows. (c) Explain why coherent states (eigenstates of $\hat a$) therefore trace exact classical orbits.
*Chapter this draws from: Chapter 4.*

**Problem F2.** Show that $\hat L_z$ and $\hat H$ commute for a central-potential Hamiltonian, and explain — using the constant-of-motion criterion — why $m_\ell$ is therefore a good quantum number that labels stationary states. Then state, in one sentence, why $[\hat L^2,\hat L_z] = 0$ is what licenses $(\ell, m)$ as a *simultaneous* label.
*Chapter this draws from: Commutators, Compatibility, and the Generalized Uncertainty Principle (Chapter 3).*

**Problem F3.** You are asked: "Does the wave packet of a free particle spread out in time, or does it move rigidly like a classical particle?"
*Note to instructor: this problem is intentionally ambiguous because the answer depends on which picture's question is being asked. The Heisenberg picture says $\hat x_H(t) = \hat x + \tfrac{\hat p}{m}t$ — the operator obeys Newton's first law, so the expectation value's center moves rigidly. The Schrödinger picture says the wave packet spreads, $\sigma_x$ grows with time. Both are true: the center translates classically while the distribution disperses. A strong student recognizes the two pictures are complementary — one tracks where the center goes, the other how the distribution widens — and that the question conflates "motion of the mean" with "evolution of the spread."*

**Closing reflection:** Across F1–F3, the same machinery recurs: the Heisenberg equation of motion, the constant-of-motion criterion, and the complementarity of the two pictures. Which problem most depended on choosing the *right picture* to even pose the question correctly, and what does that say about treating the pictures as tools rather than rivals?

---

## Instructor Notes

**Common errors:**
- Putting the time dependence on the wrong object — evolving operators in the Schrödinger picture or states in the Heisenberg picture, or doing both at once and double-counting.
- A wrong sign in $\hat U(t) = e^{-i\hat Ht/\hbar}$ (writing $e^{+i\hat Ht/\hbar}$), which propagates backward in time and is masked because magnitudes are sign-blind.
- Misapplying the Heisenberg equation — e.g. using $[\hat H,\hat A]$ where the chapter's boxed form is $[\hat A_H,\hat H]$, flipping the sign of the evolution.

**Signs a student needs to return:**
- They cannot say, for a given picture, which object carries the time dependence and which is frozen.
- They conclude a single energy eigenstate oscillates, or that a superposition is stationary.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify $[\hat H,\hat p] = 0$ and conclude momentum conservation *before* tackling $\hat x_H(t)$ — establishing the conserved quantity makes the position integration trivial. If a student finishes Part F quickly, ask them to recompute the free-particle problem in the Schrödinger picture and reconcile the spreading $\sigma_x(t)$ with the rigidly-translating $\langle\hat x\rangle(t)$ from the Heisenberg result.

**Domain adaptation note:** For an NMR/magnetic-resonance course, frame every dynamics problem as Bloch-vector precession and tie the Heisenberg operator equations directly to the rotating-frame equations of motion; for a quantum-optics or field-theory course, emphasize the Heisenberg picture's role in defining time-dependent field operators, the natural language of QFT.
