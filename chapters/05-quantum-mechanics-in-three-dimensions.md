# Chapter 5 — Quantum Mechanics in Three Dimensions

## TL;DR

The three-dimensional Schrödinger equation separates — whenever the potential depends only on distance — into one universal angular equation and one potential-specific radial equation. The angular equation produces the spherical harmonics, the common basis for every central-potential problem from atomic orbitals to the cosmic microwave background. The radial equation reduces to a one-dimensional problem with an effective potential that includes a centrifugal barrier. Everything from hydrogen to nuclear magic numbers flows from this one separation.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember:** Write the 3D time-independent Schrödinger equation in spherical coordinates and identify the orbital angular momentum operator $\hat{L}^2$ in the Laplacian. *(Bloom: Remember)*
2. **Understand:** Explain why a central potential makes the angular equation universal, independent of the specific form of $V(r)$. *(Bloom: Understand)*
3. **Apply:** Carry out the separation of variables and the $u = rR$ substitution to arrive at the radial equation with effective potential. *(Bloom: Apply)*
4. **Analyze:** Distinguish the physics basis $\{Y_\ell^m\}$ (eigenstates of $\hat{L}_z$) from the chemistry orbital basis $\{p_x, p_y, p_z\}$, and identify what each diagonalizes. *(Bloom: Analyze)*
5. **Evaluate:** Interpret the orbital shapes from the first few spherical harmonics, including the significance of the Condon–Shortley phase and the $\phi$-independence of $|Y_\ell^m|^2$. *(Bloom: Evaluate)*

---

## Scene Opening

Open any chemistry textbook to the page on atomic orbitals and you will find beautiful pictures: spheres, dumbbells, four-leaf clovers, a donut. The story told is that electrons "occupy" these shapes. Before you accept this, ask a harder question: *what exactly is the picture showing?*

Is it the wave function $\psi$? The probability density $|\psi|^2$? The angular part only, or the full thing with the radial factor included? Is the shape what the electron *is*, or the distribution of where you would *find* it?

The answers are specific, and they correct something the pictures quietly get wrong. The shapes are the angular probability density $|Y_\ell^m(\theta,\phi)|^2$, not the full wave function. The "p-orbitals" in chemistry are not the $Y_1^{\pm 1}$ states of physics — they are real linear combinations of $Y_1^{\pm 1}$ and $Y_1^0$, chosen because they point conveniently along the Cartesian axes. The complex spherical harmonics physics uses (eigenstates of the $z$-component of angular momentum) and the real combinations chemistry uses (not eigenstates of any component of angular momentum) are different states of the same energy. The pictures are not wrong, exactly, but they are showing you something more specific than they admit.

That is the payoff at the end of this chapter. The path to it begins with a fortunate accident.

---

## Core Development

### The Accident: Central Potentials and Separability

The three-dimensional time-independent Schrödinger equation is

$$-\frac{\hbar^2}{2m}\nabla^2\psi(\vec{r}) + V(\vec{r})\psi(\vec{r}) = E\psi(\vec{r}).$$

In Cartesian coordinates, $\nabla^2 = \partial_x^2 + \partial_y^2 + \partial_z^2$. Three variables, tangled together. For a general potential $V(\vec{r})$, you cannot disentangle them.

The accident is this: the most physically important potentials depend only on the distance $r = |\vec{r}|$, not on direction. The Coulomb potential $-e^2/(4\pi\epsilon_0 r)$ in the hydrogen atom. The confining well in a nucleus. The effective potential between nucleons in a shell-model calculation. All of these are **central potentials** — $V(\vec{r}) = V(r)$ — and for any central potential, the angular part of the Schrödinger equation has a universal solution. You solve it once, in this chapter. Then for hydrogen, you plug in $V(r) = -e^2/(4\pi\epsilon_0 r)$ and solve a one-dimensional radial equation. For the nuclear well, you plug in something else and solve a different one-dimensional radial equation. The angular structure is always the same.

Why does a central potential produce separability? Because $V(\vec{r}) = V(r)$ means the Hamiltonian commutes with all rotations: $[\hat{H}, \hat{L}^2] = [\hat{H}, \hat{L}_z] = 0$. When operators commute, they share a common set of eigenstates. So the energy eigenstates can simultaneously be eigenstates of $\hat{L}^2$ and $\hat{L}_z$ — and that is precisely what the separation of variables produces.

To see the algebra, rewrite the Laplacian in spherical coordinates:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}.$$

The first term is purely radial. The second and third depend only on $\theta$ and $\phi$, and they appear divided by $r^2$. Define the **orbital angular momentum operator**:

$$\hat{L}^2 \equiv -\hbar^2\!\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right].$$

Then the kinetic energy splits cleanly:

$$-\frac{\hbar^2}{2m}\nabla^2 = -\frac{\hbar^2}{2m}\cdot\frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right) + \frac{\hat{L}^2}{2mr^2}.$$

The second term, $\hat{L}^2/(2mr^2)$, is the quantum version of the classical rotational kinetic energy $L^2/(2I)$ with moment of inertia $I = mr^2$. The structures are identical.

---

### Separating Variables

Try the product ansatz $\psi(r,\theta,\phi) = R(r)\,Y(\theta,\phi)$. Substitute into the Schrödinger equation with $V = V(r)$, divide both sides by $RY$, and multiply through by $r^2$. The result is:

$$\frac{1}{R}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) - \frac{2mr^2}{\hbar^2}[V(r) - E] = -\frac{1}{Y}\hat{L}^2 Y\Big/\hbar^2.$$

The left side depends only on $r$; the right side depends only on $(\theta,\phi)$. Each side must equal a constant. Call it $\ell(\ell+1)$. The equation splits into two:

**Angular equation:**
$$\hat{L}^2\,Y(\theta,\phi) = \hbar^2\ell(\ell+1)\,Y(\theta,\phi)$$

**Radial equation:**
$$\frac{1}{R}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) - \frac{2mr^2}{\hbar^2}[V(r) - E] = \ell(\ell+1)$$

The angular equation knows nothing about which central potential you chose. It is an eigenvalue equation for $\hat{L}^2$ on the unit sphere. Its solutions — the spherical harmonics $Y_{\ell m}(\theta,\phi)$ — solve the angular part of every central-potential problem. The radial equation carries $V(r)$. That is where the specific physics lives.

---

### The Angular Equation: What Falls Out

Separate once more: $Y(\theta,\phi) = \Theta(\theta)\Phi(\phi)$. The $\phi$-equation is immediate:

$$\Phi''(\phi) = -m^2\Phi(\phi), \qquad \Phi_m(\phi) = \frac{e^{im\phi}}{\sqrt{2\pi}}.$$

**Single-valuedness** — $\Phi(\phi + 2\pi) = \Phi(\phi)$ — forces $m$ to be an integer. This is the first quantization condition, and it comes from geometry, not from any explicitly imposed rule.

The $\theta$-equation, with the substitution $x = \cos\theta$, becomes the **associated Legendre equation**. Its physically acceptable solutions — those that stay finite at the poles $\theta = 0$ and $\theta = \pi$ (equivalently, at $x = \pm 1$) — are the associated Legendre functions $P_\ell^m(\cos\theta)$. They exist only when $\ell$ is a non-negative integer and $|m| \leq \ell$. These constraints are not imposed by hand. They fall out of the regularity requirement at the poles. The quantization of angular momentum is forced by the boundary conditions on the sphere.

Stitch the pieces together with normalization:

$$Y_{\ell m}(\theta,\phi) = \sqrt{\frac{2\ell+1}{4\pi}\,\frac{(\ell-|m|)!}{(\ell+|m|)!}}\;P_\ell^m(\cos\theta)\,e^{im\phi}.$$

These are the **spherical harmonics**. They are orthonormal on the unit sphere:

$$\int_0^{2\pi}d\phi\int_0^\pi\sin\theta\,d\theta\;Y_{\ell' m'}^{*}\,Y_{\ell m} = \delta_{\ell\ell'}\delta_{mm'},$$

and they form a complete basis for functions on the sphere: any $f(\theta,\phi)$ can be expanded as $f = \sum_{\ell m}c_{\ell m}Y_{\ell m}$.

The first few are worth writing out explicitly, because students meet them in every context from atomic physics to geophysics to cosmology:

- $Y_0^0 = \dfrac{1}{\sqrt{4\pi}}$ — a constant. The s-orbital has no angular structure whatsoever.

- $Y_1^0 = \sqrt{\dfrac{3}{4\pi}}\cos\theta$ — maximal at the poles, zero on the equator. This is the physics $p_z$.

- $Y_1^{\pm 1} = \mp\sqrt{\dfrac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}$ — the minus sign for $m = +1$ is the **Condon–Shortley phase convention**. Note $|Y_1^{\pm 1}|^2 = (3/8\pi)\sin^2\theta$: the probability density is the same for $m = +1$ and $m = -1$, independent of $\phi$.

- $Y_2^0 = \sqrt{\dfrac{5}{16\pi}}(3\cos^2\theta - 1)$ — the $d_{z^2}$ orbital. It has nodal cones at $\cos\theta = \pm 1/\sqrt{3}$, about $54.7°$ from the $z$-axis.

One structural fact to internalize: $|Y_{\ell m}|^2$ is independent of $\phi$ — always. The $\phi$-dependence of $Y_{\ell m}$ lives entirely in the phase $e^{im\phi}$, and the modulus squared kills it. The angular probability density is axially symmetric about the $z$-axis for every spherical harmonic, regardless of $m$.

---

### The Angular Momentum Operators in Position Space

The classical angular momentum $\vec{L} = \vec{r}\times\vec{p}$ becomes, in quantum mechanics:

$$\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \qquad \hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z, \qquad \hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x.$$

In spherical coordinates, the $z$-component simplifies beautifully:

$$\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}.$$

Act on $Y_{\ell m}$. The $\phi$-dependence is $e^{im\phi}$, so:

$$\hat{L}_z\,Y_{\ell m} = -i\hbar\cdot im\cdot e^{im\phi}\cdot(\ldots) = m\hbar\,Y_{\ell m}.$$

The spherical harmonic $Y_{\ell m}$ is simultaneously an eigenstate of $\hat{L}^2$ with eigenvalue $\hbar^2\ell(\ell+1)$ and an eigenstate of $\hat{L}_z$ with eigenvalue $m\hbar$. The integer $m$ with $-\ell \leq m \leq +\ell$ is the **magnetic quantum number**.

The components satisfy the commutation relations:

$$[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z, \qquad [\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x, \qquad [\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y,$$

compactly: $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$. And crucially:

$$[\hat{L}^2, \hat{L}_i] = 0 \quad \text{for } i = x, y, z.$$

This last relation is the reason $\hat{L}^2$ and one component can be simultaneously diagonalized. Their joint eigenstates are the spherical harmonics. The other two components are then necessarily uncertain — a direct consequence of the nonzero commutators between $\hat{L}_x$, $\hat{L}_y$, and $\hat{L}_z$.

> **Chapter 6 boundary note.** The commutation algebra above, and the ladder-operator derivation of the spectrum $\hbar^2\ell(\ell+1)$, are the subject of Chapter 6. Here we state the results; there we derive them purely algebraically, without solving the Legendre equation.

---

### Why $\hbar^2\ell(\ell+1)$, Not $\hbar^2\ell^2$?

Here is a fact that trips up almost everyone the first time. The maximum value of $\hat{L}_z$ in the $\ell$ subspace is $m = \ell$, giving $L_z = \ell\hbar$. But the magnitude of the angular momentum is $\sqrt{\langle L^2\rangle} = \hbar\sqrt{\ell(\ell+1)}$, which is strictly *greater* than $\ell\hbar$ for any $\ell > 0$.

This means the angular momentum vector can never be fully aligned with the $z$-axis. Even in the state $|\ell, m = \ell\rangle$, which has the maximum possible $z$-component, the vector still has transverse components. Geometrically: the angular momentum precesses on a cone. The half-angle is $\arccos(\ell/\sqrt{\ell(\ell+1)})$ — for $\ell = 1$, exactly $45°$.

Why? Because $\hat{L}_x$ and $\hat{L}_y$ cannot both be zero simultaneously. If $L_z = \ell\hbar$ exactly and $L^2 = \hbar^2\ell(\ell+1)$, then $\langle L_x^2\rangle + \langle L_y^2\rangle = \hbar^2\ell(\ell+1) - \ell^2\hbar^2 = \hbar^2\ell$. The transverse components are unavoidably nonzero. Their expectation values are zero, but their variances are not. The Robertson inequality $\sigma_{L_x}\sigma_{L_y} \geq \hbar|\langle L_z\rangle|/2$ enforces a minimum spread.

This kills the Bohr-model picture of an electron orbiting in a definite plane. A definite orbital plane would require a definite direction for $\vec{L}$ — which the angular momentum algebra forbids. The electron has a definite $L^2$ and a definite $L_z$. It does not have a definite $L_x$ or $L_y$. There is no orbital plane. There is a cone.

---

### The Chemistry-Textbook Orbitals

The spherical harmonics $Y_1^{\pm 1}$ are eigenstates of $\hat{L}_z$ with eigenvalues $\pm\hbar$. Their probability densities $|Y_1^{\pm 1}|^2$ are axially symmetric about $z$ — rings around the $z$-axis. There is no definite spatial direction in these states other than the $z$-axis itself.

Chemistry prefers something different: wave functions that point along the Cartesian axes. The real combinations are:

$$p_x = -\tfrac{1}{\sqrt{2}}(Y_1^1 - Y_1^{-1}) \propto \sin\theta\cos\phi,$$
$$p_y = \tfrac{i}{\sqrt{2}}(Y_1^1 + Y_1^{-1}) \propto \sin\theta\sin\phi,$$
$$p_z = Y_1^0 \propto \cos\theta.$$

These are real wave functions with the familiar dumbbell shapes pointing along $x$, $y$, $z$. But act with $\hat{L}_z = -i\hbar\partial_\phi$ on $p_x \propto \sin\theta\cos\phi$:

$$\hat{L}_z(\sin\theta\cos\phi) = -i\hbar\frac{\partial}{\partial\phi}\cos\phi = i\hbar\sin\phi \propto ip_y.$$

The result is $ip_y$, not a multiple of $p_x$. The $p_x$ orbital is *not* an eigenstate of $\hat{L}_z$. It has a definite spatial direction ($\hat{x}$) but no definite $z$-component of angular momentum.

Both bases — the complex $\{Y_1^{-1}, Y_1^0, Y_1^1\}$ and the real $\{p_x, p_y, p_z\}$ — span the same three-dimensional subspace of states with $\ell = 1$. They are related by a unitary transformation; they describe the same physics. Chemistry picks the real basis because the pictures are beautiful. Physics picks the complex basis because $\hat{L}_z$ is diagonal. Neither is more "correct." The mistake is thinking the chemistry pictures *are* the eigenstates of angular momentum. They are not.

---

### The Radial Equation and the Centrifugal Barrier

With $\psi = R(r)Y_{\ell m}$ and the angular part handled, the radial equation has an inconvenient first-derivative term. The substitution $u(r) = rR(r)$ cleans it up. A short calculation gives:

$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u(r) = E\,u(r).$$

This is a **one-dimensional Schrödinger equation** in $u(r)$ on the half-line $r \in [0,\infty)$, with effective potential

$$V_{\text{eff}}(r) = V(r) + \underbrace{\frac{\hbar^2\ell(\ell+1)}{2mr^2}}_{\text{centrifugal barrier}}.$$

The extra term — positive, diverging at $r = 0$, falling off as $1/r^2$ — is the **centrifugal barrier**. For $\ell > 0$, it pushes probability away from the origin. For $\ell = 0$ (s-states), there is no barrier, and the wave function can have finite amplitude at $r = 0$.

One misconception to clear up: the centrifugal barrier is not a force pushing the electron outward. It is a *kinetic energy* contribution — specifically, the angular part of the kinetic energy, which is $\hat{L}^2/(2mr^2)$ evaluated in the eigenstate of $\hat{L}^2$ with eigenvalue $\hbar^2\ell(\ell+1)$. Mathematically it sits where $V(r)$ sits, but physically it is kinetic. The distinction matters when you ask where energy comes from.

Boundary conditions: $u(0) = 0$ to keep $R = u/r$ finite at the origin; $u(r) \to 0$ as $r \to \infty$ for normalizability. The **radial probability density** is:

$$P(r)\,dr = |u(r)|^2\,dr = r^2|R(r)|^2\,dr,$$

the probability of finding the particle at distance between $r$ and $r + dr$ (integrated over all angles).

The $u$-substitution does the key work: a 3D central-force problem is exactly equivalent to a 1D Schrödinger equation with an $\ell$-dependent effective potential. The trade is clean: project onto an angular momentum eigenstate, pay with the centrifugal term.

---

### A Solvable Example: The Spherical Well

Take $V(r) = 0$ for $r < a$ and $V = \infty$ for $r \geq a$. Inside the well, with $k = \sqrt{2mE/\hbar^2}$ and $\rho = kr$, the radial equation reduces to the spherical Bessel equation whose regular solutions are $j_\ell(\rho)$. The boundary condition $u(a) = 0$ means $j_\ell(ka) = 0$, so $ka$ must be the $n$-th zero $\beta_{n\ell}$ of $j_\ell$:

$$E_{n\ell} = \frac{\hbar^2\beta_{n\ell}^2}{2ma^2}.$$

For $\ell = 0$: $j_0(\rho) = \sin\rho/\rho$, zeros at $\rho = n\pi$. So $E_{n,0} = n^2\pi^2\hbar^2/(2ma^2)$ — exactly the 1D infinite-well spectrum. The $\ell = 0$ states of the spherical well, after the $u$-substitution, are literally the 1D infinite-well problem. There is no angular structure; the two problems are identical.

For $\ell = 1$: $j_1(\rho) = \sin\rho/\rho^2 - \cos\rho/\rho$. Its first zero is near $\rho \approx 4.493$, giving $E_{1,1} \approx (4.493/\pi)^2 E_{1,0} \approx 2.05\,E_{1,0}$. The centrifugal barrier raised the first $p$-state above the first $s$-state.

The level ordering — 1s, 1p, 1d, 2s, 1f, 2p, ... — is obtained by sorting the zeros of successive Bessel functions. This is not a curiosity. It is the foundation of the nuclear shell model. Maria Goeppert Mayer and J. Hans D. Jensen showed in 1949 that adding a strong spin-orbit coupling to this potential reproduces the observed nuclear magic numbers 2, 8, 20, 28, 50, 82, 126 — for which they shared the 1963 Nobel Prize in Physics [verify]. The angular machinery of this chapter, applied to a nucleus rather than an atom, predicts which proton and neutron numbers make unusually stable nuclei.

One more point on the spectrum: higher $\ell$ does not universally mean higher energy. For the spherical well it does. For the hydrogen atom (Chapter 10), energies depend only on the principal quantum number $n$, with no $\ell$-dependence — a special "accidental" degeneracy of the $1/r$ Coulomb potential. For the 3D harmonic oscillator, energies depend on $2n_r + \ell$. The angular structure is universal; the ordering of levels is potential-specific.

---

### The Same Mathematics, Much Larger

The spherical harmonics $Y_{\ell m}(\theta,\phi)$ are the universal basis for functions on any sphere. They appear in atomic orbitals (electrons in atoms), in the nuclear shell model (nucleons in nuclei), in the multipole expansion of any electromagnetic field, in the gravitational potential of any nearly-spherical body, and in the cosmic microwave background.

The Planck collaboration reports the CMB's temperature anisotropies — the tiny ripples in the temperature of the sky left over from 380,000 years after the Big Bang — as a power spectrum $C_\ell$, where $\ell$ is the spherical-harmonic index. The first acoustic peak at $\ell \approx 220$ corresponds to the sound horizon of the universe at recombination [verify]. The same $\ell$ that distinguishes s, p, d, f atomic orbitals labels the multipoles of the cosmos. The mathematics is identical. Learning spherical harmonics here is preparation for anything that lives on a sphere.

---

## Worked Example: The Separation and the Radial Equation

**The lesson.** Starting from the 3D TISE with a central potential, carry out the full separation of variables and arrive at the effective 1D radial equation.

**Setup.** Write the Hamiltonian in spherical coordinates:

$$\hat{H} = -\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right)\right] + \frac{\hat{L}^2}{2mr^2} + V(r).$$

Try $\psi = R(r)Y_{\ell m}(\theta,\phi)$. Since $Y_{\ell m}$ is an eigenstate of $\hat{L}^2$ with eigenvalue $\hbar^2\ell(\ell+1)$, acting $\hat{H}$ on $\psi$ gives:

$$\hat{H}\psi = Y_{\ell m}\left[-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}R + V(r)R\right] = E\,R(r)Y_{\ell m}.$$

Dividing by $Y_{\ell m}$ (which is not zero away from its nodal surfaces):

$$-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]R = E\,R.$$

**The $u$ substitution.** Let $u(r) = rR(r)$, so $R = u/r$. Then:

$$\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) = \frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{d}{dr}\frac{u}{r}\right) = \frac{1}{r^2}\frac{d}{dr}\!\left(r\frac{du}{dr} - u\right) = \frac{1}{r}\frac{d^2u}{dr^2}.$$

Substituting:

$$-\frac{\hbar^2}{2m}\frac{1}{r}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]\frac{u}{r} = E\frac{u}{r}.$$

Multiply through by $r$:

$$\boxed{-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u(r) = E\,u(r).}$$

This is a 1D Schrödinger equation in disguise. The angular problem has been completely absorbed. For each value of $\ell$, this is an independent 1D problem on the half-line with effective potential $V_{\text{eff}}(r)$.

**The limit.** This approach assumes $Y_{\ell m}$ is already known. Chapter 6 will show that the eigenvalue spectrum $\hbar^2\ell(\ell+1)$ follows from the commutation algebra alone — without solving the Legendre equation. The two chapters are complementary: this chapter derives the explicit wave functions (the spherical harmonics); Chapter 6 derives the eigenvalue spectrum algebraically, and generalizes immediately to spin.

---

## Common Misconceptions

**"The centrifugal term is a force."** It is not. It is the angular kinetic energy $\langle\hat{L}^2\rangle/(2mr^2) = \hbar^2\ell(\ell+1)/(2mr^2)$ evaluated in an angular momentum eigenstate, and written on the right-hand side of the effective potential for notational convenience. Physically it resists localization near the origin, but this resistance is kinetic, not potential.

**"The chemistry p-orbitals are the angular momentum eigenstates."** They are not. The orbitals $p_x \propto \sin\theta\cos\phi$ and $p_y \propto \sin\theta\sin\phi$ are real linear combinations of $Y_1^{\pm 1}$, chosen to point along the Cartesian axes. They do not have a definite value of $L_z$; measuring $\hat{L}_z$ on a $p_x$ state gives $+\hbar$ half the time and $-\hbar$ half the time. The physics basis $\{Y_1^{-1}, Y_1^0, Y_1^1\}$ diagonalizes $\hat{L}_z$; the chemistry basis $\{p_x, p_y, p_z\}$ diagonalizes spatial orientation.

**"$\hat{L}^2$ eigenvalue is $\hbar^2\ell^2$."** This is the classical answer for a particle orbiting in a definite plane with $L_z = \ell\hbar$. The quantum answer is $\hbar^2\ell(\ell+1)$, which is larger by $\hbar^2\ell$. The extra contribution comes from quantum fluctuations in $\hat{L}_x$ and $\hat{L}_y$, which the uncertainty principle forbids from being simultaneously zero.

**"The $u = rR$ substitution is just a trick."** The substitution eliminates the first-derivative term $\frac{2}{r}\frac{dR}{dr}$ that arises from the spherical volume element. Without it, the radial equation does not have the standard 1D Schrödinger form. The substitution is not cosmetic — it converts the equation into a form where 1D intuition applies directly.

**"$|Y_{\ell m}|^2$ depends on $\phi$."** It does not. The $\phi$-dependence of $Y_{\ell m}$ lives in the phase $e^{im\phi}$, which disappears when you take the modulus squared. Every orbital probability density is axially symmetric about the $z$-axis. This seems wrong for $p_x$ (which "points along $x$"), but $p_x$ is not an eigenstate of $\hat{L}_z$ — it has no definite $m$ — so the statement does not apply to it.

---

## Exercises

### Warm-Up

**5.1** Write the full 3D TISE in spherical coordinates for $V(r) = -e^2/(4\pi\epsilon_0 r)$. Without solving anything: (a) identify which terms depend only on $r$ and which depend only on $(\theta,\phi)$; (b) explain why the separation constant is written $\ell(\ell+1)$ rather than just $\lambda$; (c) state the two equations the separation produces. *(Tests: separation of variables, identification of the angular operator)*

**5.2** Verify $\int|Y_0^0|^2\,d\Omega = 1$ and $\int|Y_1^0|^2\,d\Omega = 1$ by explicit integration. You will need $\int_0^\pi\sin\theta\,d\theta = 2$ and $\int_0^\pi\cos^2\theta\sin\theta\,d\theta = 2/3$. *(Tests: normalization of spherical harmonics)*

**5.3** (a) Show that $|Y_{\ell m}(\theta,\phi)|^2$ is independent of $\phi$ for any $\ell, m$. (b) Evaluate $Y_1^1$ at $(\theta = \pi/2,\, \phi = 0)$ and confirm the value is $-\sqrt{3/(8\pi)}$, not $+\sqrt{3/(8\pi)}$. What goes wrong if you omit the Condon–Shortley phase? *(Tests: axial symmetry, Condon–Shortley convention)*

### Application

**5.4** Verify $\hat{L}_z Y_1^1 = \hbar Y_1^1$ by direct calculation: write out $Y_1^1 = -\sqrt{3/(8\pi)}\sin\theta\,e^{i\phi}$, apply $\hat{L}_z = -i\hbar\partial_\phi$, and confirm the eigenvalue is $+\hbar$. Then verify that $p_x \propto \sin\theta\cos\phi$ is *not* an eigenstate of $\hat{L}_z$ by computing $\hat{L}_z\,p_x$ explicitly. *(Tests: $\hat{L}_z$ eigenvalue equation, physics vs. chemistry basis)*

**5.5** Starting from the radial equation for $R(r)$, apply the substitution $u(r) = rR(r)$ and show explicitly that the result is the 1D Schrödinger equation with $V_{\text{eff}} = V(r) + \hbar^2\ell(\ell+1)/(2mr^2)$. Identify which derivative of $r^2 dR/dr$ produces the centrifugal term. In one sentence, explain why the centrifugal term is kinetic, not potential, energy. *(Tests: $u$-substitution, centrifugal barrier)*

**5.6** For the 3D infinite spherical well of radius $a$: (a) show that the 1s ground-state energy is $E_{1,0} = \pi^2\hbar^2/(2ma^2)$, the same as the 1D infinite well of width $a$; (b) find the energy of the first 1p state using $\beta_{1,1} \approx 4.493$ and express it as a multiple of $E_{1,0}$; (c) explain why the 1s and 1D well results match but the 1p result has no 1D analog. *(Tests: spherical well energies, connection to 1D well)*

**5.7** For the state $|\ell = 2, m = 2\rangle$: (a) compute $\sqrt{\langle L^2\rangle}$ and $L_z$; (b) find the half-angle of the angular momentum cone; (c) find $\sqrt{\langle L_x^2 + L_y^2\rangle}$ in this state; (d) explain why this quantity cannot be zero, using the Robertson inequality for $\hat{L}_x$ and $\hat{L}_y$. *(Tests: $\ell(\ell+1)$ vs. $\ell^2$, angular momentum cone)*

### Synthesis

**5.8** Consider the $p_x$ orbital $\propto \sin\theta\cos\phi$. (a) Express $p_x$ as a linear combination of $Y_1^{-1}$, $Y_1^0$, $Y_1^1$. (b) If you measure $\hat{L}_z$ on an ensemble of particles in state $p_x$, what are the possible outcomes and their probabilities? (c) What is $\langle\hat{L}_z\rangle$ for $p_x$? Does zero expectation value mean zero eigenvalue? Explain. *(Tests: physics vs. chemistry basis, Born rule in angular momentum space)*

**5.9** The nuclear magic numbers 2, 8, 20 (the first three) correspond to filled shells in a spherical well without spin-orbit coupling. Using the level ordering 1s, 1p, 1d, 2s, ... and the degeneracy $2(2\ell+1)$ per level (including both spin orientations): (a) show that filling 1s, 1p, 1d, and 2s gives cumulative counts 2, 8, 18, 20, matching the first three magic numbers; (b) explain why the higher magic numbers (28, 50, ...) require a spin-orbit term. *(Tests: level ordering, nuclear shell model connection)*

### Challenge

**5.10** Define $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$. (a) Show $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$ using $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$. (b) Use this to argue that $\hat{L}_+|Y_{\ell m}\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $(m+1)\hbar$. (c) The descent must terminate at $m = -\ell$ by a non-negativity argument. State the termination condition $\hat{L}_-|Y_{\ell,-\ell}\rangle = 0$ and show it forces $\ell$ to be a non-negative integer — the algebraic derivation of the spectrum without solving the Legendre equation. This problem previews Chapter 6, where the full algebraic derivation is developed. *(Tests: ladder operator algebra, connection between analytic and algebraic approaches)*

---

## Still Puzzling

The accidental degeneracy of the hydrogen atom — energies depending only on $n$, not on $\ell$ — has an explanation: a conserved Runge–Lenz vector and a hidden $\mathrm{SO}(4)$ symmetry of the $1/r$ Coulomb potential [verify]. The same accidental degeneracy in the 3D harmonic oscillator has an $\mathrm{SU}(3)$ explanation. Both are clean and settled mathematically. Bertrand's theorem says the $1/r$ and $r^2$ potentials are the only ones for which all classical bound orbits close. The quantum degeneracy and the classical closed-orbit property must be the same fact in different clothing. The math is done. The conceptual unity — a derivation that makes the connection feel inevitable rather than coincidental — is still, for me, not fully satisfying.

---

## The +1 — Simulation Exercise: The Spherical Harmonics Visualizer

Build a single-file D3 simulation that displays $Y_{\ell m}(\theta,\phi)$ in two synchronized panels — a polar cross-section and a pseudo-3D mesh on the sphere — with a toggle between physics (complex) and chemistry (real) conventions, and an animation mode that visualizes the $\phi$-phase rotation generated by $\hat{L}_z$. Deliverable: `05-spherical-harmonics.html`.

### Part 1 — CLAUDE.md Extension

```
## Chapter 5 — Spherical Harmonics Simulator Rules

SPHERICAL HARMONICS PHYSICS RULES

1. Associated Legendre polynomials computed by recurrence (Condon-Shortley):
     P_l^l(x) = (-1)^l * (2l-1)!! * (1-x^2)^(l/2)
     P_{l+1}^l(x) = x * (2l+1) * P_l^l(x)
     (l - m + 1) * P_{l+1}^m(x) = (2l+1)*x*P_l^m(x) - (l+m)*P_{l-1}^m(x)
   Verify Y_1^1 at (theta=pi/2, phi=0) = -sqrt(3/(8*pi)). The minus sign is
   the Condon-Shortley check; if it comes out positive, the phase is wrong.

2. Spherical harmonic:
     Y_l^m = sqrt((2l+1)/(4*pi) * (l-m)!/(l+m)!) * P_l^m(cos theta) * exp(i*m*phi)
   For m < 0: Y_l^{-m} = (-1)^m * conj(Y_l^m).

3. Real combinations (chemistry convention):
     m > 0: Y_{l,m}^real = (1/sqrt(2)) * (Y_l^{-m} + (-1)^m * Y_l^m)
     m = 0: Y_{l,0}^real = Y_l^0
     m < 0: Y_{l,m}^real = (i/sqrt(2)) * (Y_l^m - (-1)^m * Y_l^{-m})
   Verify: m=1 real combination is p_x ~ sin(theta)*cos(phi),
           m=-1 real combination is p_y ~ sin(theta)*sin(phi).

4. Normalization check at startup: Riemann-sum integral of |Y_{lm}|^2 over
   sphere on a 100x100 (theta, phi) grid with sin(theta) measure.
   Result must be 1 within 0.01.

5. Clamp: sqrt_arg = max(0, 1 - x*x) before sqrt in P_l^l to avoid
   floating-point negatives near the poles.

6. Painter's algorithm for 3D sphere: sort ~900 patches by depth (back first),
   render in that order. Without this sort, the orbital looks inside-out.

KNOWN FAILURE MODES:
(a) Condon-Shortley missing: Y_1^1 sign wrong.
(b) Factorial overflow for l > 10: use log-gamma or iterative product.
(c) (1-x^2) negative near poles: clamp.
(d) Painter's algorithm omitted: orbital appears inverted.
(e) Real-combination signs wrong: p_x maximum at -x instead of +x.
```

### Part 2 — The Simulation Prompt

```
Build 05-spherical-harmonics.html following CLAUDE.md.

SHOW.
Display Y_{l m}(theta, phi) in two synchronized panels inside one SVG
(1100 x 650 px):

LEFT PANEL (450 x 500): polar cross-section at phi=0. Plot
  r(theta) = |Y_{l m}(theta, 0)|^2 using d3.lineRadial() with
  d3.curveCardinalClosed. Fill the interior; if Re(Y) mode is on, positive
  lobes blue, negative lobes red; if |Y|^2 mode, single color (teal).
  Draw the +z axis as a vertical reference line.

RIGHT PANEL (500 x 500): pseudo-3D unit sphere, 30 latitude x 30 longitude
  bands (~900 patches). Color each patch by |Y_{lm}|^2 (grayscale-to-color)
  in probability mode, or by sign (blue-red diverging) in Re(Y) mode.
  Orthographic projection, view angles (alpha, beta) draggable.
  Painter's algorithm sort by depth. Add +z axis arrow.

BOTTOM STRIP (1100 x 100): eigenvalue display:
  L^2 = hbar^2 * l(l+1) = [value]   L_z = hbar * m = [value]
  Nodes in theta: [list of nodal-cone angles in degrees]
  m bar: -l to +l, current m highlighted.

TOP STRIP (1100 x 50): controls:
  l selector (0..4), m selector (-l..+l),
  convention toggle (physics/chemistry), display mode (|Y|^2 / Re(Y)),
  right-panel mode (sphere shading / balloon), animate phi-phase toggle.

SAY.
Single self-contained HTML file. D3 v7 from CDN. No other dependencies.

Phi-phase animation: when enabled, replace exp(i*m*phi) by
exp(i*m*(phi - t)) in the right panel. m=0 states are static; |m|=2
states rotate twice as fast as |m|=1. This is the action of L_z as
generator of rotations about z.

VERIFY.
Runtime sanity checks (write to console at startup):
(a) For all (l, m) up to l=4: integral of |Y_{lm}|^2 over sphere = 1 ± 0.01.
(b) Y_1^1 at (pi/2, 0) = -sqrt(3/(8*pi)) within 1e-6. Condon-Shortley check.
(c) Chemistry (l=1, m=1): maximum of |Y|^2 at theta=pi/2, phi=0 (+x direction).

List known failure modes in an HTML comment at the top of the file.
```

### Part 3 — Exploration Tasks

**Task 1: Axial symmetry.** Set $(\ell, m) = (1, 1)$ in physics convention. In $|Y|^2$ mode, observe that the right-panel shading is axially symmetric about $\hat{z}$ regardless of $\phi$. Switch to Re(Y) mode: the real part has $\cos\phi$ dependence and breaks the symmetry. The modulus squared does not.

**Task 2: The basis swap.** Set $(\ell, m) = (1, 1)$, physics convention. Toggle to chemistry (real) convention. The cross-section changes from a ring (axially symmetric) to a dumbbell pointing along $\hat{x}$. The eigenvalue display confirms the chemistry state is not an eigenstate of $\hat{L}_z$.

**Task 3: $\ell(\ell+1)$, not $\ell^2$.** Set $\ell = 1$. The bottom strip shows $L^2 = 2\hbar^2$, not $\hbar^2$. Compute the cone half-angle: $\arccos(1/\sqrt{2}) = 45°$. For $\ell = 2, m = 2$: $L_z = 2\hbar$, $\sqrt{L^2} = \sqrt{6}\hbar$, cone angle $\arccos(2/\sqrt{6}) \approx 35°$.

**Task 4: $\hat{L}_z$ generates $\phi$-rotation.** Toggle animate phi-phase. For $m = 0$ ($Y_1^0 = p_z$), nothing rotates — no $\phi$ dependence. For $m = 1$, the right panel rotates at rate 1. For $m = 2$, twice as fast. For $m = -1$, opposite direction. This is $e^{-i\hat{L}_z t/\hbar}$ acting visually.

**Task 5: Nodes.** Set $\ell = 2, m = 0$. The bottom strip shows nodal cones at $54.7°$ and $125.3°$. Set $\ell = 4, m = 0$: four nodes. The number of angular nodes in $\theta$ is $\ell - |m|$.

### Part 4 — Six Failure Modes to Check

**Condon–Shortley missing.** $Y_1^1$ at $(\pi/2, 0)$ comes out $+\sqrt{3/(8\pi)}$ instead of $-\sqrt{3/(8\pi)}$. The sign matters for ladder-operator matrix elements in Chapter 6.

**Factorial overflow.** For $\ell > 10$, $(\ell + m)!$ overflows double precision. Cap at $\ell = 10$ or use iterative products.

**Floating-point negative in Legendre.** $(1 - \cos^2\theta)$ can be $-\epsilon$ near the poles; clamp to zero before taking the square root.

**Painter's algorithm omitted.** Patches render in mesh order (back to front reversed), making the orbital look inside-out.

**Real-combination signs wrong.** $p_x$ maximum appears at $-x$ instead of $+x$. Verify against the chemistry convention explicitly.

**Normalization check skipped.** The orbital shape looks right, but the absolute scale is wrong. The console check catches this.

---

## References

Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012. Chapters 9–10. [verify] The primary source for separation of variables and the central-potential formalism in these notes.

Griffiths, D. J., and Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018. Chapter 4. [verify] The standard reference for the derivation of spherical harmonics including the Condon–Shortley phase convention (Eq. 4.32).

Goeppert Mayer, M. "On Closed Shells in Nuclei." *Physical Review* 74, 235 (1948). [verify] The paper establishing the nuclear shell model. The same angular-momentum machinery of this chapter, applied to nuclei, explains magic numbers.

Jensen, J. H. D., Suess, H. E., and Haxel, O. "Modellmäßige Deutung der ausgezeichneten Nucleonenzahlen im Kernbau." *Die Naturwissenschaften* 36, 155 (1949). [verify] Independent derivation of the nuclear shell model; shared the 1963 Nobel Prize in Physics with Goeppert Mayer.

Planck Collaboration. "Planck 2018 Results. V. CMB Power Spectra and Likelihoods." *Astronomy and Astrophysics* 641, A5 (2020). [verify] The CMB angular power spectrum $C_\ell$, whose multipole index $\ell$ is the same index as in the spherical harmonics of this chapter.

Condon, E. U., and Shortley, G. H. *The Theory of Atomic Spectra*. Cambridge University Press, 1935. [verify] The original source for the Condon–Shortley phase convention used in the normalization of $Y_\ell^m$.

*Bridge to Chapter 6: You now have the universal angular machinery in coordinate space. The spherical harmonics $Y_{\ell m}$ solve the angular equation for any central potential. Chapter 6 re-derives the spectrum $\hbar^2\ell(\ell+1)$ and $m\hbar$ purely algebraically — from the commutation relations $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ alone — without solving any differential equation. That algebraic approach generalizes immediately to spin, which has no position-space analog.*
