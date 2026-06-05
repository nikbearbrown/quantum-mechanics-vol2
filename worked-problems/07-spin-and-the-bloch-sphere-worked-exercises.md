# Worked Exercises: Spin and the Bloch Sphere
*Chapter 7 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- Spin operators $\hat{S}_i = (\hbar/2)\sigma_i$ and the Pauli algebra $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$, with eigenvalues $\pm\hbar/2$ along any axis.
- The Bloch-sphere state $|\hat{n},+\rangle = \cos\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\tfrac{\theta}{2}|\!\downarrow\rangle$ and the half-angle Born rule $P(+) = \cos^2\tfrac{\gamma}{2}$.
- Larmor precession: $\hat{H} = \tfrac{1}{2}\gamma B_0\hbar\,\sigma_z$, time evolution at $\omega_L = \gamma B_0$, with $\theta_0$ frozen and azimuth $\phi(t) = \phi_0 + \omega_L t$.

---

## Part A — Full Worked Example

**What this demonstrates:** How to read a Bloch-sphere state, apply the half-angle Born rule, and track Larmor precession — confirming that $\langle\hat{S}_z\rangle$ is a constant of motion.

**The problem:** A proton's spin is prepared at Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$. (a) Write the state and find $P(+)$ for measuring $+\hbar/2$ along $\hat{z}$. (b) Place the proton in $B_0 = 1.5$ T and find the Larmor frequency and the time-evolved state. (c) Show $P(+)$ along $\hat{z}$ is unchanged by the precession.

**The solution:**

**Step 1 — Write the Bloch-sphere state using the half-angle parametrization.**
$$|\psi\rangle = \cos\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\phi_0}\sin\tfrac{\theta_0}{2}|\!\downarrow\rangle = \cos\tfrac{\pi}{6}|\!\uparrow\rangle + e^{i\pi/4}\sin\tfrac{\pi}{6}|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$
*Why:* Every pure spin-½ state has this form; the factor $\theta/2$ (not $\theta$) is what makes the parametrization cover the sphere exactly once.
*Check:* $|\cos\tfrac{\pi}{6}|^2 + |\sin\tfrac{\pi}{6}|^2 = \tfrac{3}{4} + \tfrac{1}{4} = 1$ ✓ (normalized).

**Step 2 — Apply the half-angle Born rule for the $\hat{z}$ analyzer.**
The analyzer points at $(\theta_n, \phi_n) = (0, 0)$, so $\cos\gamma = \cos\theta_0\cos 0 + \sin\theta_0\sin 0\cos(\dots) = \cos\theta_0 = \tfrac{1}{2}$, giving $\gamma = \pi/3$. Then
$$P(+) = \cos^2\tfrac{\gamma}{2} = \cos^2\tfrac{\pi}{6} = \frac{3}{4}.$$
*Why:* The probability depends on the *angle between* the state and analyzer Bloch vectors, through the half-angle $\gamma/2$ — using $\cos^2\gamma$ instead would give the wrong answer ($\cos^2(\pi/3) = 1/4$).
*Check:* Direct projection: $|\langle\!\uparrow|\psi\rangle|^2 = |\tfrac{\sqrt{3}}{2}|^2 = \tfrac{3}{4}$ ✓ — the geometric and component computations agree.

**Step 3 — Compute the Larmor frequency at $B_0 = 1.5$ T.**
$$f_L = \frac{\gamma_p}{2\pi}\,B_0 = 42.58\ \text{MHz/T}\times 1.5\ \text{T} = 63.87\ \text{MHz}, \qquad T_L = \frac{1}{f_L} = 15.66\ \text{ns}.$$
*Why:* For a field $\vec{B} = B_0\hat{z}$, the Hamiltonian is diagonal in the $\hat{S}_z$ basis, so the dynamics is a phase advance at $\omega_L = \gamma B_0$ — the operating equation of every MRI scanner.
*Check:* The value $63.87$ MHz is the standard 1.5 T clinical-MRI proton frequency ✓.

**Step 4 — Write the time-evolved state, freezing the polar angle.**
$$|\psi(t)\rangle = \cos\tfrac{\pi}{6}|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin\tfrac{\pi}{6}|\!\downarrow\rangle.$$
*Why:* The diagonal time-evolution operator multiplies the down-component by $e^{i\omega_L t}$ (relative phase), advancing only the azimuth $\phi$; the polar angle $\theta_0$ is fixed because the magnitudes of the two components do not change.
*Check:* At $t = 0$ this reduces to the Step-1 state ✓.

**Step 5 — Confirm $P(+)$ along $\hat{z}$ is a constant of motion.**
$$P(+;t) = |\langle\!\uparrow|\psi(t)\rangle|^2 = |\cos\tfrac{\pi}{6}|^2 = \frac{3}{4} \quad\text{for all } t.$$
*Why:* Only the *relative phase* of the down-component evolves; the up-component magnitude $\cos\tfrac{\pi}{6}$ is untouched, so $\langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos\theta_0$ is conserved.
*Check:* The precession traces a latitude circle at fixed $\theta_0 = \pi/3$, so the $z$-projection is constant — consistent with $[\hat{H}, \hat{S}_z] = 0$ ✓.

**Final answer:** $P(+) = 3/4$ along $\hat{z}$; $f_L = 63.87$ MHz, $T_L = 15.66$ ns; $P(+)$ stays $3/4$ throughout precession because $\langle\hat{S}_z\rangle$ is conserved.

**What made this work:** Two ideas carried the whole problem. First, the half-angle parametrization makes "reading the state" and "applying the Born rule" the same geometric act — the probability is $\cos^2(\gamma/2)$ in the angle between two Bloch vectors. Second, a field along $\hat{z}$ makes $\hat{H}$ diagonal in the $\hat{S}_z$ basis, so precession is pure azimuthal phase advance with the polar angle frozen — which is exactly why $\langle\hat{S}_z\rangle$ is conserved.

**Self-explanation prompt:** Explain why the half-angle $\gamma/2$ (rather than $\gamma$) appears in the Born rule, using the perpendicular case $\gamma = \pi/2$ as your test.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same read-state → Born-rule → precession pipeline, for a state on the equator and an off-axis analyzer.

**The problem:** A proton is prepared on the Bloch equator at $\theta_0 = \pi/2$, $\phi_0 = 0$ (the state $(|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2} = |\hat{x},+\rangle$). (a) Write the state. (b) Find $P(+)$ for an analyzer along $\hat{x}$ and for an analyzer along $\hat{z}$. (c) Place it in $B_0 = 3.0$ T, find $f_L$, and find $\langle\hat{S}_z\rangle$ as a function of time. (d) Find $\langle\hat{S}_x\rangle(t)$ and explain why it oscillates while $\langle\hat{S}_z\rangle$ does not.

Work each step with its own subgoal label, work, *Why:*, and *Check:*, mirroring the five-step backbone of Part A: write the state → apply the half-angle Born rule → compute $f_L$ → write $|\psi(t)\rangle$ with $\theta_0$ frozen → evaluate the conserved versus oscillating expectation values.

**Stuck?** On the equator $\theta_0 = \pi/2$, so $\langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos(\pi/2) = 0$ for all $t$, while $\langle\hat{S}_x\rangle = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t) = \tfrac{\hbar}{2}\cos(\omega_L t)$ — full-amplitude oscillation as the Bloch vector sweeps the equator.

*Instructor note: no solution is provided for Part B. Students should produce the full structured solution themselves.*

---

## Part C — Completion Problem

**What this demonstrates:** Verifying that $\hat{S}_{\hat{n}} = \tfrac{\hbar}{2}\hat{n}\cdot\vec{\sigma}$ has eigenvalues $\pm\hbar/2$ for *any* axis, with the eigenvalue computation left for you.

**The problem:** For $\hat{n} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$, show that $\hat{S}_{\hat{n}} = \tfrac{\hbar}{2}\hat{n}\cdot\vec{\sigma}$ has eigenvalues $\pm\hbar/2$ regardless of direction.

**Step 1 — Write the operator matrix.** (provided)
$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\ \sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$

**Step 2 — Set up the eigenvalue condition via the characteristic equation.** (provided)
Eigenvalues $\lambda$ satisfy $\det(\hat{S}_{\hat{n}} - \lambda I) = 0$, i.e. $\lambda^2 - (\text{tr})\lambda + \det = 0$.

**Step 3 — Compute the trace and determinant of $\hat{S}_{\hat{n}}$.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Solve the characteristic equation for $\lambda$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret.** (provided)
The eigenvalues are $\pm\hbar/2$ independent of $(\theta, \phi)$ — exactly the "two values, every axis" that Stern and Gerlach observed in 1922. The $+\hbar/2$ eigenvector is $|\hat{n},+\rangle = \cos\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\tfrac{\theta}{2}|\!\downarrow\rangle$.

**Final answer:** $\text{tr}\,\hat{S}_{\hat{n}} = 0$, $\det\hat{S}_{\hat{n}} = -(\hbar/2)^2$, so $\lambda = \pm\hbar/2$ for every $\hat{n}$.

**Self-explanation prompt:** Why does the *direction-independence* of the eigenvalues correspond directly to the experimental fact that Stern–Gerlach gives two spots for any orientation of the magnet?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked to write the spin-½ state pointing along the direction $\hat{n}$ with $\theta = \pi/2$, $\phi = 0$ (i.e., along $+\hat{x}$). Their work:

**Step 1.** "The general Bloch state is $|\hat{n},+\rangle = \cos(\theta)|\!\uparrow\rangle + e^{i\phi}\sin(\theta)|\!\downarrow\rangle$."

**Step 2.** Plug in $\phi = 0$: "$|\hat{n},+\rangle = \cos\theta|\!\uparrow\rangle + \sin\theta|\!\downarrow\rangle$."

**Step 3.** ⚠ Plug in $\theta = \pi/2$: "$|\hat{x},+\rangle = \cos(\pi/2)|\!\uparrow\rangle + \sin(\pi/2)|\!\downarrow\rangle = 0\cdot|\!\uparrow\rangle + 1\cdot|\!\downarrow\rangle = |\!\downarrow\rangle$."

**Step 4.** Report: "The spin-up-along-$x$ state is just $|\!\downarrow\rangle$."

**Your tasks:**
1. Identify the error in Step 3 precisely (it originates in Step 1).
2. Write the correct Bloch-sphere state with the half-angle and re-evaluate at $\theta = \pi/2$, $\phi = 0$.
3. Confirm your answer is the known $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$.
4. Verify by checking that your state is the $+\hbar/2$ eigenstate of $\hat{S}_x = \tfrac{\hbar}{2}\sigma_x$.

**Why this error is common:** Students drop the factor of $\tfrac{1}{2}$ and write $\cos\theta, \sin\theta$ instead of $\cos\tfrac{\theta}{2}, \sin\tfrac{\theta}{2}$, which collapses the equator ($\theta = \pi/2$) onto the south pole instead of an equal superposition.

---

## Part E — Transfer Problem

**What this demonstrates:** The same Pauli-algebra reasoning, transferred to the sequential Stern–Gerlach experiment, where non-commutation — not "disturbance" — explains the 50/50 outcome.

**The problem:** A beam of silver atoms passes $\mathrm{SG}_z$; the lower output is blocked, leaving $|\!\uparrow\rangle$. These pass $\mathrm{SG}_x$; the $|\hat{x},-\rangle$ output is blocked, leaving $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. These enter a final $\mathrm{SG}_z$. (a) Compute $P(\hat{x},+)$ for the middle stage starting from $|\!\uparrow\rangle$. (b) Compute the probabilities at the final $\mathrm{SG}_z$. (c) Using $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$, explain why the result is 50/50 and why the "the $\mathrm{SG}_x$ device disturbed the $z$-component" story is wrong.

**Hint (use only if stuck after 10 minutes):** After the $\mathrm{SG}_x$ selection the atom is in $|\hat{x},+\rangle$, which is genuinely *not* an eigenstate of $\hat{S}_z$ — it has no definite $z$-component to be disturbed. Decompose $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ and apply the Born rule; you get $P(\uparrow) = P(\downarrow) = 1/2$.

**Reflection prompt:**
1. A hidden-variable model says each atom carries pre-existing $(\mu_x, \mu_z)$ values that the magnets merely read. What would that model predict for the final $\mathrm{SG}_z$, and how does the data refute it?
2. Why is "non-commutation" a deeper explanation than "disturbance" for the same 50/50 result?

---

## Part F — Interleaved Review

**F1 — This chapter.** Verify the spinor double cover: take $|\hat{n},+\rangle = \cos\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\tfrac{\theta}{2}|\!\downarrow\rangle$ and rotate the analyzer by $2\pi$ (i.e., $\theta \to \theta + 2\pi$). Show the state picks up an overall minus sign, and that only a $4\pi$ rotation returns it to itself. Connect this to the half-angle.
*Chapter this draws from: 7*

**F2 — Previous chapter.** From **Angular Momentum**, the spin operators arise as the $\ell = \tfrac{1}{2}$ case of the ladder algebra: $\hat{S}_i = (\hbar/2)\sigma_i$. Starting from the normalization $\hat{L}_+|\tfrac{1}{2},-\tfrac{1}{2}\rangle = \hbar|\tfrac{1}{2},+\tfrac{1}{2}\rangle$ (and the bottom-rung annihilation), reconstruct $\hat{S}_z$, $\hat{S}_+$, $\hat{S}_-$ as $2\times 2$ matrices and confirm $\hat{S}_x = (\hbar/2)\sigma_x$. Verify $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$.
*Chapter this draws from: Angular Momentum*

**F3 — Discrimination.** You are given the equatorial state $(|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ and asked: does it have a definite $\hat{S}_z$, a definite $\hat{S}_x$, both, or neither? Decide, then justify by checking which of $\hat{S}_z$ and $\hat{S}_x$ the state is an eigenstate of.
*Note to instructor: this tests whether students can discriminate "definite along one axis" from "definite along all axes," and whether they understand that having a sharp value along $\hat{x}$ forces indefiniteness along $\hat{z}$ — the structural meaning of non-commuting observables.*

**Closing reflection:** The chapter killed the spinning-ball picture with the number $v \approx 170c$. Write two sentences on what "intrinsic" angular momentum means once rotation in physical space has been ruled out.

---

## Instructor Notes

**Common errors:**
- Dropping the factor of $\tfrac{1}{2}$ in the Bloch state ($\cos\theta$ instead of $\cos\tfrac{\theta}{2}$) (Part D's misconception), which mislocates equatorial states.
- Using $\cos^2\gamma$ instead of $\cos^2(\gamma/2)$ in the Born rule, giving $P(+) = 0$ at the perpendicular instead of $1/2$.
- A sign error in the Pauli algebra $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, propagating to the wrong sign of $\langle\hat{S}_y\rangle$ in precession.

**Signs a student needs to return:**
- They explain the sequential Stern–Gerlach 50/50 result as the apparatus "disturbing" a definite $z$-component.
- They model spin as literal rotation of a charged sphere.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify the three Born-rule limits (aligned $\to 1$, anti-aligned $\to 0$, perpendicular $\to 1/2$) before tackling the precession. If a student finishes Part F quickly, have them compute the electron Larmor frequency at $B_0 = 1$ mT and confirm the precession direction reverses relative to the proton ($\gamma_e < 0$).

**Domain adaptation note:** For a medical-physics or imaging cohort, anchor every precession calculation to MRI field strengths and the $\omega_L = \gamma B_0$ scanner equation; for a quantum-information cohort, frame the Bloch sphere as the single-qubit state space and the half-angle as the source of the $4\pi$ spinor periodicity.
