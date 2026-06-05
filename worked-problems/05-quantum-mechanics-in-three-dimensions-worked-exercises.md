# Worked Exercises: Quantum Mechanics in Three Dimensions
*Chapter 5 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The separation of variables ansatz $\psi(r,\theta,\phi) = R(r)\,Y(\theta,\phi)$ and why a central potential $V(\vec{r}) = V(r)$ permits it.
- The spherical harmonics $Y_\ell^m(\theta,\phi)$ as joint eigenstates of $\hat{L}^2$ (eigenvalue $\hbar^2\ell(\ell+1)$) and $\hat{L}_z$ (eigenvalue $m\hbar$), with $\hat{L}_z = -i\hbar\,\partial_\phi$.
- The $u$-substitution $u(r) = rR(r)$, the effective potential $V_\text{eff}(r) = V(r) + \hbar^2\ell(\ell+1)/(2mr^2)$, and the radial probability density $P(r)\,dr = r^2|R(r)|^2\,dr$.

---

## Part A — Full Worked Example

**What this demonstrates:** How the $u$-substitution converts the 3D radial equation into a 1D Schrödinger equation on the half-line, and how the centrifugal barrier raises the energy of a $p$-state above the corresponding $s$-state in an infinite spherical well.

**The problem:** A particle of mass $m$ is confined to an infinite spherical well, $V(r) = 0$ for $r < a$ and $V = \infty$ for $r \geq a$. Find the ground-state ($\ell = 0$) energy and the lowest $\ell = 1$ energy, and express the latter as a multiple of the former. Use that the first zero of $j_1$ is $\beta_{1,1} \approx 4.493$.

**The solution:**

**Step 1 — Reduce the 3D radial problem to 1D via the $u$-substitution.**
The radial equation, after setting $u(r) = rR(r)$, becomes
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u(r) = E\,u(r),$$
with boundary conditions $u(0) = 0$ and $u(a) = 0$ (the wall).
*Why:* The substitution kills the first-derivative term, leaving a literal 1D Schrödinger equation on $r \in [0,a]$ with the $\ell$-dependent centrifugal barrier folded into $V_\text{eff}$.
*Check:* For $\ell = 0$ the centrifugal term vanishes and we recover the bare 1D infinite well — a known result, so the structure is right.

**Step 2 — Separate the radial and angular content for $\ell = 0$.**
With $V = 0$ inside and $\ell = 0$, the equation is $u'' = -k^2 u$ with $k = \sqrt{2mE/\hbar^2}$, so $u(r) = A\sin(kr) + B\cos(kr)$. The condition $u(0) = 0$ forces $B = 0$.
$$u(r) = A\sin(kr).$$
*Why:* This is identical to the 1D infinite well of width $a$ — the $\ell = 0$ state has no angular structure ($Y_0^0$ is a constant), so the radial problem and the 1D problem coincide.
*Check:* $u(0) = A\sin(0) = 0$ ✓; the solution is regular at the origin.

**Step 3 — Apply the wall boundary condition to quantize $k$.**
$u(a) = A\sin(ka) = 0$ requires $ka = n\pi$, so
$$E_{n,0} = \frac{n^2\pi^2\hbar^2}{2ma^2}, \qquad E_{1,0} = \frac{\pi^2\hbar^2}{2ma^2}.$$
*Why:* The zeros of $j_0(\rho) = \sin\rho/\rho$ sit at $\rho = n\pi$, and $\rho = ka$.
*Check:* This is exactly the 1D infinite-well spectrum $n^2\pi^2\hbar^2/(2ma^2)$ ✓.

**Step 4 — Quantize the $\ell = 1$ state through the spherical Bessel zero.**
For $\ell = 1$ the regular solution is $R(r) \propto j_1(kr)$, and the wall demands $j_1(ka) = 0$, i.e. $ka = \beta_{1,1} \approx 4.493$:
$$E_{1,1} = \frac{\hbar^2\beta_{1,1}^2}{2ma^2}.$$
*Why:* The centrifugal barrier $\hbar^2\ell(\ell+1)/(2mr^2)$ changes the regular solution from $j_0$ to $j_1$, whose first zero lies further out than $\pi$.
*Check:* $\beta_{1,1} \approx 4.493 > \pi \approx 3.142$, so $E_{1,1} > E_{1,0}$, as a repulsive barrier should require.

**Step 5 — Express the $\ell = 1$ energy as a multiple of the ground state.**
$$\frac{E_{1,1}}{E_{1,0}} = \frac{\beta_{1,1}^2}{\pi^2} = \frac{(4.493)^2}{\pi^2} \approx \frac{20.19}{9.87} \approx 2.05.$$
*Why:* Both energies share the prefactor $\hbar^2/(2ma^2)$; only the squared Bessel zero differs.
*Check:* The ratio exceeds 1, confirming the centrifugal barrier pushed the $p$-state above the $s$-state.

**Final answer:** $E_{1,0} = \pi^2\hbar^2/(2ma^2)$ (identical to the 1D infinite well); $E_{1,1} = \beta_{1,1}^2\hbar^2/(2ma^2) \approx 2.05\,E_{1,0}$.

**What made this work:** The $u$-substitution is the entire engine. It turns the awkward 3D radial operator $\frac{1}{r^2}\frac{d}{dr}(r^2\frac{d}{dr})$ into a clean second derivative $\frac{1}{r}\frac{d^2u}{dr^2}$, at the cost of a centrifugal term that records the angular momentum. For $\ell = 0$ that term vanishes and the problem is *literally* the 1D infinite well. For $\ell = 1$ the centrifugal barrier is present and raises the energy by selecting a higher Bessel zero. The angular machinery never had to be re-solved — it lives entirely in the constant $\ell(\ell+1)$.

**Self-explanation prompt:** Explain in your own words why the $\ell = 0$ spherical well is identical to the 1D infinite well, but the $\ell = 1$ well has no 1D analog.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same $u$-substitution and centrifugal-barrier reasoning, applied to a different observable — the radial node structure rather than the energy ratio.

**The problem:** For the same infinite spherical well of radius $a$, consider the $\ell = 0$ states. (a) Write $u_n(r)$ for the $n$th $\ell = 0$ state and find $R_n(r) = u_n(r)/r$. (b) Write the radial probability density $P_n(r)$ and find the radius at which it is maximal for the ground state $n = 1$. (c) Explain, using the $r^2$ factor in $P(r)$, why the most probable radius is *not* at the maximum of $|R(r)|^2$.

Work each step with its own subgoal label, work, *Why:*, and *Check:*, exactly as in Part A. Use the same five-step backbone: reduce via $u$-substitution → separate angular/radial → apply wall condition → build the probability density with the $r^2$ factor → locate the maximum.

**Stuck?** Recall that $P(r)\,dr = r^2|R(r)|^2\,dr = |u(r)|^2\,dr$ — the $r^2$ has already been absorbed into $u$, so for $\ell = 0$ you are finding the maximum of $\sin^2(\pi r/a)$, not of $[\sin(\pi r/a)/r]^2$.

*Instructor note: no solution is provided for Part B. Students should produce the full structured solution themselves.*

---

## Part C — Completion Problem

**What this demonstrates:** Normalizing a spherical harmonic and confirming the $\hat{L}_z$ eigenvalue, with the central algebraic steps left for you to complete.

**The problem:** Verify that $Y_1^0 = \sqrt{3/(4\pi)}\,\cos\theta$ is normalized on the unit sphere and is an eigenstate of $\hat{L}_z = -i\hbar\,\partial_\phi$. Find the eigenvalue.

**Step 1 — Set up the solid-angle normalization integral.** (provided)
$$\int |Y_1^0|^2\,d\Omega = \int_0^{2\pi}\!\!d\phi \int_0^\pi \frac{3}{4\pi}\cos^2\theta\,\sin\theta\,d\theta.$$

**Step 2 — Separate the $\phi$ and $\theta$ integrals.** (provided)
The $\phi$ integral gives $\int_0^{2\pi}d\phi = 2\pi$. The remaining integral is $\frac{3}{4\pi}\cdot 2\pi \int_0^\pi \cos^2\theta\,\sin\theta\,d\theta$.

**Step 3 — Evaluate the $\theta$ integral and conclude normalization.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Apply $\hat{L}_z$ to $Y_1^0$ and read off the eigenvalue.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Interpret the eigenvalue.** (provided)
Since $Y_1^0$ has no $\phi$-dependence, $\partial_\phi Y_1^0 = 0$, so $\hat{L}_z Y_1^0 = 0$. The state has $m = 0$: a definite zero $z$-component of angular momentum, consistent with $\langle L^2\rangle = 2\hbar^2$ but $L_z = 0$.

**Final answer:** $\int|Y_1^0|^2\,d\Omega = 1$ (normalized); $\hat{L}_z Y_1^0 = 0\cdot Y_1^0$, eigenvalue $m\hbar = 0$.

**Self-explanation prompt:** Why does a state with $\langle L^2\rangle = 2\hbar^2 \neq 0$ have $L_z = 0$? What does this say about where the angular momentum "points"?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student sets up the radial equation for a hydrogen-like $V(r) = -e^2/(4\pi\epsilon_0 r)$ and the $2p$ state ($\ell = 1$). Their work:

**Step 1.** Start from the 3D TISE, assume $\psi = R(r)Y_1^m(\theta,\phi)$, separate variables.

**Step 2.** Apply $u(r) = rR(r)$ to clean up the first-derivative term.

**Step 3.** ⚠ "Since the angular part is already separated off, the radial equation for $u$ is just
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\epsilon_0 r}\,u = E\,u.$$
The angular momentum doesn't enter the radial equation."

**Step 4.** Solve this 1D Coulomb problem and report the spectrum.

**Your tasks:**
1. Identify the error in Step 3 precisely.
2. Write the correct radial equation, including the term that was dropped.
3. Explain physically what the dropped term represents and why it must appear for $\ell = 1$.
4. State what would go wrong with the predicted $2p$ wave function near $r = 0$ if the error were not caught.

**Why this error is common:** After "separating off" the angular part, students think the angular momentum has been fully removed, forgetting that the eigenvalue $\ell(\ell+1)$ survives as the centrifugal term $\hbar^2\ell(\ell+1)/(2mr^2)$ inside the radial equation.

---

## Part E — Transfer Problem

**What this demonstrates:** The same separation-and-effective-potential principle, transferred from a confining well or Coulomb potential to the 3D isotropic harmonic oscillator.

**The problem:** A particle of mass $m$ moves in the 3D isotropic harmonic potential $V(r) = \frac{1}{2}m\omega^2 r^2$. (a) Write the effective radial potential $V_\text{eff}(r)$ for general $\ell$. (b) For $\ell = 0$ versus $\ell = 2$, describe qualitatively how the location of the minimum of $V_\text{eff}$ shifts, and why. (c) The chapter notes that for this potential the energies depend on $2n_r + \ell$. Contrast this $\ell$-dependence with hydrogen (energy depends only on $n$) and the spherical well (higher $\ell$ raises energy). What general lesson does this comparison teach about the relationship between angular structure and level ordering?

**Hint (use only if stuck after 10 minutes):** Write $V_\text{eff}(r) = \frac{1}{2}m\omega^2 r^2 + \hbar^2\ell(\ell+1)/(2mr^2)$ and minimize with respect to $r$; the minimum sits where the rising harmonic term balances the falling centrifugal term. A larger $\ell$ makes the centrifugal wall stronger, pushing the minimum outward.

**Reflection prompt:**
1. The angular machinery ($Y_\ell^m$, the centrifugal term) is identical across all three potentials. What, then, is responsible for the differences in level ordering?
2. The chapter calls hydrogen's $\ell$-independence an "accidental" degeneracy from a hidden SO(4) symmetry. Why is the word "accidental" appropriate, given that the harmonic oscillator and spherical well both *do* show $\ell$-dependence?

---

## Part F — Interleaved Review

**F1 — This chapter.** For the state $|\ell = 2, m = 2\rangle$: (a) compute $\sqrt{\langle L^2\rangle}$ and $L_z$; (b) find the half-angle of the angular-momentum cone; (c) compute $\sqrt{\langle L_x^2 + L_y^2\rangle}$ using $\langle L_x^2 + L_y^2\rangle = \langle L^2\rangle - L_z^2$; (d) explain why this transverse quantity cannot be zero.
*Chapter this draws from: 5*

**F2 — Previous chapter.** This chapter relies on the **separation of variables** and the structure of a stationary state. From the formalism, a stationary state $\psi(\vec{r},t) = \psi(\vec{r})e^{-iEt/\hbar}$ has a time-independent probability density. For the hydrogen $2p$ state $\psi_{21m}(\vec{r},t)$, show that $|\psi_{21m}|^2$ is independent of time and also independent of $\phi$. Which factor of the wave function is responsible for each independence?
*Chapter this draws from: the formalism (stationary states and the spectral decomposition)*

**F3 — Discrimination.** You are given two angular states: (i) $Y_1^0 \propto \cos\theta$ and (ii) $p_x \propto \sin\theta\cos\phi$. One is an eigenstate of $\hat{L}_z$ and one is not. Without computing, decide which is which by inspecting the $\phi$-dependence; then confirm by applying $\hat{L}_z = -i\hbar\,\partial_\phi$.
*Note to instructor: this tests whether the student can discriminate the physics basis ($\hat{L}_z$ eigenstates, $e^{im\phi}$ structure) from the chemistry basis (real combinations pointing along Cartesian axes) — a discrimination students routinely fail by assuming any "orbital" is an angular-momentum eigenstate.*

**Closing reflection:** Across this chapter, the angular part was solved *once* and reused for every central potential. Write two sentences on why this universality is a consequence of rotational symmetry rather than of any specific $V(r)$.

---

## Instructor Notes

**Common errors:**
- Dropping the centrifugal term $\hbar^2\ell(\ell+1)/(2mr^2)$ from the radial equation after "separating off" the angular part (Part D's misconception).
- Forgetting the $r^2$ factor in the radial probability density $P(r) = r^2|R(r)|^2$, leading to the wrong "most probable radius."
- Treating the chemistry orbitals $p_x, p_y, p_z$ as $\hat{L}_z$ eigenstates; only the complex $Y_1^m$ are.

**Signs a student needs to return:**
- They write $\hat{L}^2$ eigenvalue as $\hbar^2\ell^2$ rather than $\hbar^2\ell(\ell+1)$, or cannot explain the difference.
- They cannot say why the $\ell = 0$ spherical well coincides with the 1D infinite well.

**Scaffolding adjustments:** If a student struggles with Part A, drop to the pure $\ell = 0$ case first (Steps 2–3 alone) so they see the 1D-well identity before the centrifugal barrier enters. If a student finishes Part F quickly, have them derive the $\ell = 1$ cone half-angle $\arccos(1/\sqrt{2}) = 45°$ and connect it to the Robertson inequality bound for $\hat{L}_x, \hat{L}_y$.

**Domain adaptation note:** For a chemistry-leaning cohort, anchor every appearance of $\ell$ to orbital labels ($s, p, d$) and emphasize the physics-vs-chemistry basis distinction; for a physics/nuclear cohort, lean on the spherical-well level ordering and its connection to the nuclear shell model.
