# Chapter 7 — Spin and the Bloch Sphere

## TL;DR

Silver atoms hit a glass plate in two spots, not a smear. That single experimental fact forces the existence of a two-dimensional complex Hilbert space, three operators obeying the angular-momentum algebra, and a sphere whose every point is a quantum state. This chapter builds that machinery — the Pauli matrices, the Bloch sphere, Larmor precession — and connects it to the operating principle of every MRI scanner and every qubit in a quantum computer.

---

## Learning Objectives

By the end of this chapter you can:

1. **Remember** the three Pauli matrices and the single identity $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$ that encodes their entire algebra. *(Bloom: Remember)*
2. **Apply** the half-angle parametrization to place any spin-½ state on the Bloch sphere and read off the Born-rule probability $P(+) = \cos^2(\gamma/2)$ for any analyzer direction. *(Bloom: Apply)*
3. **Explain** quantitatively why the spinning-ball picture of spin fails, and what "intrinsic angular momentum transforming as an SU(2) representation" means as a replacement. *(Bloom: Understand)*
4. **Calculate** the Larmor precession frequency for a proton or electron at a given field strength and connect the result to NMR/MRI. *(Bloom: Apply)*
5. **Analyze** a sequential Stern–Gerlach experiment to show that the 50/50 outcome at the third stage is structural — a consequence of operator noncommutativity — not a measurement disturbance artifact. *(Bloom: Analyze)*

---

## Two Spots, No Explanation, Three Years

In February 1922, Otto Stern and Walther Gerlach sent a beam of neutral silver atoms through an inhomogeneous magnetic field and caught them on a glass plate. The field exerts a force on any magnetic moment — the gradient of $\vec{\mu}\cdot\vec{B}$ — and atoms with different moment orientations deflect by different amounts. Classical physics says the magnetic moments can point in any direction, so the plate should show a continuous smear of silver. Stern developed the plate. He found two spots.

Not a smear. Two distinct spots. One above, one below. Nothing in between.

Whatever silver atoms are doing, the component of their magnetic moment along the field axis takes exactly two values, never three, never a continuum. And this turns out to be true for any axis you point: two spots, always. The experiment is unambiguous and strange, and it sat unexplained for three years.

Here is what makes the story more interesting: Stern and Gerlach in 1922 did not know what they had found. They believed they were confirming the old Bohr–Sommerfeld "space quantization" of orbital angular momentum. Silver has the electron configuration $[\text{Kr}]\,4d^{10}5s^1$, with a single valence electron in an $s$ orbital. An $s$ orbital has zero orbital angular momentum — $\ell = 0$ — so it contributes nothing to the magnetic moment. The two spots came from something nobody had proposed yet: the intrinsic spin of the electron, hypothesized by Uhlenbeck and Goudsmit in 1925. Stern and Gerlach got the right answer before the right question had been asked.

This is how physics often goes. The experiment was right. The interpretation waited for a new concept. This chapter builds that concept.

---

## Core Development

### Two Values Means Two Dimensions

The empirical fact — always two values, any axis — points directly to the Hilbert space. Whatever spin lives in, that space must be such that any spin-component operator has exactly two eigenvalues. The smallest complex vector space that supports this is $\mathbb{C}^2$, two-dimensional and complex. This is not a guess; it is the minimal structure forced by "two and only two."

Choose the eigenstates of the $z$-component of spin as the basis:
$$|\!\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}.$$
Any normalized spin state is a linear combination:
$$|\psi\rangle = \alpha|\!\uparrow\rangle + \beta|\!\downarrow\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1.$$
Two complex numbers, one normalization constraint, one unobservable overall phase: two real degrees of freedom. That is the dimension of a sphere. We will come back to the sphere.

The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$, where $\sigma_x, \sigma_y, \sigma_z$ are the **Pauli matrices**:
$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Four facts about these matrices, all verifiable by direct multiplication:

**Fact 1: $\sigma_i^2 = I$ for each $i$.** Check: $\sigma_x^2 = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)^2 = \bigl(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\bigr)$. ✓

**Fact 2: $\mathrm{Tr}(\sigma_i) = 0$ for each $i$.** Read off the diagonals.

**Fact 3: Different Pauli matrices anticommute.** $\sigma_i\sigma_j + \sigma_j\sigma_i = 0$ for $i \neq j$. Compute $\sigma_x\sigma_y = \bigl(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\bigr)$ and $\sigma_y\sigma_x = \bigl(\begin{smallmatrix}-i&0\\0&i\end{smallmatrix}\bigr)$; they sum to zero. ✓

**Fact 4: They satisfy the angular-momentum commutation relations.** $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$. From the calculation above, $[\sigma_x, \sigma_y] = 2i\sigma_z$. Which means $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ — the same algebra you derived for orbital angular momentum $\hat{L}$ in Chapter 6. That algebraic coincidence is not an accident. It is the reason "spin" deserves to be called angular momentum.

The four facts combine into one multiplication table:
$$\boxed{\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k.}$$
This single identity is the entire Pauli algebra. Memorize it.

### Why Spin Is Not Rotation

Many students arrive with a picture: the electron is a tiny ball physically rotating on its own axis, and "spin" names that rotation's angular momentum. Kill this picture now with a number, not a hand-wave.

Assume the electron has angular momentum $\hbar/2$ and the spinning-ball picture is true. Use the most generous possible radius — the classical electron radius:
$$r_e = \frac{e^2}{4\pi\epsilon_0 m_e c^2} \approx 2.82 \times 10^{-15}\ \text{m},$$
defined by setting the electrostatic self-energy equal to $m_e c^2$. Real experiments bound the electron's actual size below $10^{-18}$ m, but we take the most generous radius because a smaller one makes the picture fail worse.

The moment of inertia of a uniform solid sphere is $I = \frac{2}{5}m_e r_e^2$, and $L = I\omega$, so the equatorial surface speed is $v = \omega r_e = Lr_e/I = 5\hbar/(4m_e r_e)$:
$$v = \frac{5 \times 1.055 \times 10^{-34}}{4 \times 9.11 \times 10^{-31} \times 2.82 \times 10^{-15}} \approx 5.1 \times 10^{10}\ \text{m/s}.$$
The speed of light is $c \approx 3.0 \times 10^8$ m/s. The required equatorial speed is roughly $170c$. The picture is not wrong by a small margin. It is wrong by more than two orders of magnitude, and using a smaller radius makes it worse, not better.

So what is spin? An internal degree of freedom that transforms as a representation of $\mathrm{SU}(2)$ — the group of $2\times2$ unitary matrices with determinant 1 — under rotations. It is not any motion in physical space. Paul Dirac showed in 1928 that spin-½ falls out of the requirement that the wave equation be Lorentz-covariant and first-order in time: you do not put spin in by hand; you find it already there when you insist on the right symmetries.

"Spin is intrinsic angular momentum" is true but incomplete unless you say what *intrinsic* means. **Intrinsic** means: the algebra is that of angular momentum, the carrier is an $\mathrm{SU}(2)$ representation, and the underlying degree of freedom does not correspond to any motion in physical space.

### Spin Along Any Axis — the Bloch Sphere

Pick a unit vector $\hat{n} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$. The spin operator along $\hat{n}$ is
$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\hat{n}\cdot\vec{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\\sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$
The eigenvalues: the matrix has trace zero and determinant $-(\hbar/2)^2(\cos^2\theta + \sin^2\theta) = -(\hbar/2)^2$, so the characteristic polynomial gives $\lambda = \pm\hbar/2$. For every axis you point, two values. The formalism delivers exactly what the 1922 experiment found.

The $+\hbar/2$ eigenvector requires the half-angle identities $1 - \cos\theta = 2\sin^2(\theta/2)$ and $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$. Solving and normalizing:
$$|\hat{n},+\rangle = \cos\!\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\!\tfrac{\theta}{2}|\!\downarrow\rangle.$$
The orthogonal eigenstate is $|\hat{n},-\rangle = \sin\!\tfrac{\theta}{2}|\!\uparrow\rangle - e^{i\phi}\cos\!\tfrac{\theta}{2}|\!\downarrow\rangle$.

Notice the half-angle. A spin pointing along $+\hat{x}$ is $\theta = \pi/2$, $\phi = 0$, giving $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ — equal weights on both basis states. This is right: a spin definitely pointing along $\hat{x}$ should give 50/50 when measured along $\hat{z}$. Apply the Born rule and you get exactly that.

The half-angle has a deeper consequence. Rotate the analyzer by $2\pi$ — a full turn in physical space. The angle $\theta$ goes to $\theta + 2\pi$, and $\cos(\theta/2)$ goes to $\cos(\theta/2 + \pi) = -\cos(\theta/2)$; similarly for the sine. The spin state acquires an overall minus sign. Only at $4\pi$ — two full turns — does the state return to itself. This is the **spinor double cover**: spin states live in $\mathrm{SU}(2)$, not in the ordinary rotation group $\mathrm{SO}(3)$. A $2\pi$ rotation that takes every vector in space back to itself takes a spinor to its negative. This was directly observed in neutron interferometry by Rauch et al. (1975) and Werner et al. (1975). [verify]

The parametrization $(\theta, \phi)$ maps every pure spin state to a point on a unit sphere — the **Bloch sphere**. North pole: $|\!\uparrow\rangle$. South pole: $|\!\downarrow\rangle$. Equator: equal superpositions $(|\!\uparrow\rangle + e^{i\phi}|\!\downarrow\rangle)/\sqrt{2}$, with $\phi$ varying around the equator. Every point on the sphere is a spin state; every spin state is a point on the sphere.

The Born rule takes a clean geometric form on the Bloch sphere. If the state is at Bloch angles $(\theta_\psi, \phi_\psi)$ and the analyzer points at $(\theta_n, \phi_n)$, let $\gamma$ be the angle between the two unit vectors:
$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n).$$
The probability of outcome $+\hbar/2$ is
$$\boxed{P(+) = \cos^2\!\tfrac{\gamma}{2}, \qquad P(-) = \sin^2\!\tfrac{\gamma}{2}.}$$
Three checks: state aligned with analyzer ($\gamma = 0$): $P(+) = 1$. Anti-aligned ($\gamma = \pi$): $P(+) = 0$. Perpendicular ($\gamma = \pi/2$): $P(+) = 1/2$. Three correct limits from one formula.

### Spin in a Magnetic Field — Larmor Precession

A spin in a uniform magnetic field $\vec{B} = B_0\hat{z}$ has Hamiltonian
$$\hat{H} = -\vec{\mu}\cdot\vec{B} = \gamma B_0\hat{S}_z = \frac{\gamma B_0\hbar}{2}\sigma_z,$$
where $\gamma$ is the **gyromagnetic ratio**: $\gamma_e/(2\pi) \approx 28.025$ GHz/T for the electron, $\gamma_p/(2\pi) \approx 42.58$ MHz/T for the proton.

The Hamiltonian is diagonal in the $\hat{S}_z$ basis. The time-evolution operator is therefore diagonal too:
$$\hat{U}(t) = \begin{pmatrix}e^{-i\omega_L t/2}&0\\0&e^{+i\omega_L t/2}\end{pmatrix},$$
where $\omega_L = \gamma B_0$ is the **Larmor frequency**. Starting from a general state at polar angle $\theta_0$ and azimuth $\phi_0 = 0$:
$$|\psi(t)\rangle = \cos\!\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\omega_L t}\sin\!\tfrac{\theta_0}{2}|\!\downarrow\rangle.$$
The polar angle $\theta_0$ does not change. The azimuth advances at rate $\omega_L$: $\phi(t) = \omega_L t$. On the Bloch sphere, the state traces a latitude circle at constant $\theta_0$, precessing around the $\hat{z}$-axis. The expectation values make this explicit:
$$\langle\hat{S}_x\rangle(t) = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t), \qquad \langle\hat{S}_y\rangle(t) = \tfrac{\hbar}{2}\sin\theta_0\sin(\omega_L t), \qquad \langle\hat{S}_z\rangle(t) = \tfrac{\hbar}{2}\cos\theta_0.$$
The vector $(\langle\hat{S}_x\rangle, \langle\hat{S}_y\rangle, \langle\hat{S}_z\rangle)$ has constant magnitude $\hbar/2$ and rotates in the $xy$-plane. This is **Larmor precession** — formally identical to the precession of a classical magnetic moment, except that what precesses is the probability distribution over outcomes, not any physical pointer.

The numbers make this real. Common field strengths and Larmor frequencies for the proton ($\gamma_p/(2\pi) = 42.58$ MHz/T):

| $B_0$ (T) | Setting | $f_L = \omega_L/(2\pi)$ (MHz) | Period $T_L$ (ns) |
|-----------|---------|------------------------------|-------------------|
| 0.5 | Low-field / open MRI | 21.29 | 46.98 |
| 1.5 | Clinical MRI | 63.87 | 15.66 |
| 3.0 | Research MRI | 127.74 | 7.83 |
| 7.0 | Ultra-high-field MRI | 298.06 | 3.35 |

The formula $\omega_L = \gamma B_0$ is not textbook background; it is the operating equation of a medical instrument used on millions of patients per year.

### What the Sequential Experiment Is Really Telling You

Prepare a beam of silver atoms and send it through an $\mathrm{SG}_z$ apparatus. Block the lower output. The surviving atoms are in state $|\!\uparrow\rangle$. Send that beam through an $\mathrm{SG}_x$ apparatus. The $\hat{S}_x$ eigenstates are $|\hat{x},\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$, so $|\!\uparrow\rangle = (|\hat{x},+\rangle + |\hat{x},-\rangle)/\sqrt{2}$. Born rule gives $P(\hat{x},+) = P(\hat{x},-) = 1/2$. The beam splits equally.

Block the $|\hat{x},-\rangle$ output. The surviving atoms are in $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. Send them through a second $\mathrm{SG}_z$. Express $|\hat{x},+\rangle$ in the $\hat{z}$ basis: equal superposition of $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$. Born rule: $P(\hat{z},+) = P(\hat{z},-) = 1/2$. The beam splits equally again.

The atoms started definitively spin-up along $\hat{z}$. After an intermediate $\hat{x}$ measurement, they are 50/50 along $\hat{z}$ again. The tempting description: the $\mathrm{SG}_x$ device disturbed the atoms, scrambling their $z$-component. This is the wrong picture.

The operators $\hat{S}_x$ and $\hat{S}_z$ do not commute: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$. No state can be simultaneously an eigenstate of both. After the $\mathrm{SG}_x$ measurement selects $|\hat{x},+\rangle$, that state is not an eigenstate of $\hat{S}_z$ — it has no definite $\hat{z}$ value, not a definite value that was obscured by a clumsy apparatus. There is nothing there to disturb. The 50/50 outcome at the third stage is the Born rule applied to a state that simply does not have a definite $\hat{S}_z$.

A naive hidden-variable picture — each silver atom carries pre-existing definite values $(\mu_x, \mu_y, \mu_z)$ that the SG apparatuses read off without disturbing — would predict that selecting $\mu_z = +$ at stage one and then $\mu_x = +$ at stage two leaves $\mu_z$ unchanged, so stage three should return $\mu_z = +$ with probability 1. Experiment gives 50/50. Pre-existing definite values for non-commuting observables are not consistent with the data.

The spin component along $\hat{z}$ does not exist as a pre-existing property when the system is prepared in a $\hat{x}$ eigenstate. It comes into being at the moment of measurement. The algebra forces this.

### The *g*-Factor, and What "Exactly 2" Actually Means

The Hamiltonian $\hat{H} = \gamma\hat{S}_z B_0$ uses $\gamma = g_e(e/2m_e)$. The Dirac equation predicts $g_e = 2$ exactly. The measured value is
$$g_e \approx 2.00232.$$
The deviation $a_e = (g_e - 2)/2 \approx 0.00116$ is not a failure of Dirac. It is the QED radiative correction from virtual photons dressing the bare electron — the leading term is $a_e \approx \alpha/(2\pi)$, where $\alpha \approx 1/137$ is the fine-structure constant. Agreement between QED theory and experiment extends to 13 significant figures, making it one of the most precisely tested predictions in physics.

When you write $\hat{H} = \gamma B_0\hat{S}_z$, use the experimental $\gamma$, which includes the anomalous correction. The deviation from $g = 2$ is a feature, not a bug — it is a window into the virtual-photon structure of QED.

---

## Worked Example: The Bloch Vector and Its Precession

**The lesson.** A spin-½ particle is prepared in the state with Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$. The analyst measures spin along $\hat{z}$. A proton is then placed in a field $\vec{B} = 1.5\,\hat{z}$ T. Find (a) the Bloch vector components, (b) the Born-rule probability for $+\hbar/2$ along $\hat{z}$, and (c) the precession frequency and the time-evolved state.

**(a) Bloch vector components.** The state is
$$|\psi\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i\pi/4}\sin(\pi/6)|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$
The Bloch vector is $\hat{n}_\psi = (\sin\theta_0\cos\phi_0,\ \sin\theta_0\sin\phi_0,\ \cos\theta_0)$:
$$\hat{n}_\psi = \left(\frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2},\ \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2},\ \frac{1}{2}\right) = \left(\frac{\sqrt{6}}{4},\ \frac{\sqrt{6}}{4},\ \frac{1}{2}\right).$$
Check: $|\hat{n}_\psi|^2 = 6/16 + 6/16 + 1/4 = 3/4 + 1/4 = 1$. ✓

**(b) Born-rule probability along $\hat{z}$.** The analyzer is at $(\theta_n, \phi_n) = (0, 0)$. The angle $\gamma$ between state and analyzer Bloch vectors satisfies
$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n) = \cos(\pi/3)\cdot 1 + 0 = \frac{1}{2}.$$
So $\gamma = \pi/3$, and
$$P(+) = \cos^2\!\tfrac{\pi}{6} = \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}.$$
Equivalently: $|\langle\!\uparrow|\psi\rangle|^2 = |\cos(\pi/6)|^2 = 3/4$. ✓

**(c) Precession.** For a proton in $B_0 = 1.5$ T:
$$\omega_L = \gamma_p B_0 = 2\pi \times 42.58\ \text{MHz/T} \times 1.5\ \text{T} = 2\pi \times 63.87\ \text{MHz}.$$
The period is $T_L = 1/(63.87\ \text{MHz}) \approx 15.66$ ns. The time-evolved state is
$$|\psi(t)\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin(\pi/6)|\!\downarrow\rangle.$$
The polar angle stays frozen at $\theta_0 = \pi/3$. The azimuth advances: $\phi(t) = \pi/4 + \omega_L t$. The probability $P(+)$ along $\hat{z}$ is $|\cos(\pi/6)|^2 = 3/4$ at every instant — $\langle\hat{S}_z\rangle$ is a constant of motion.

**The limit.** What if $\theta_0 = 0$? The state is $|\!\uparrow\rangle$, already an eigenstate of $\hat{H}$. The phase $e^{i\omega_L t}$ multiplies the zero coefficient of $|\!\downarrow\rangle$ and does nothing observable. No precession. The equatorial ($\theta_0 = \pi/2$) state precesses maximally: $\langle\hat{S}_z\rangle = 0$ always, while $\langle\hat{S}_x\rangle$ and $\langle\hat{S}_y\rangle$ oscillate at full amplitude $\hbar/2$. The Bloch vector traces the equator at 63.87 MHz.

---

## Common Misconceptions

**"The Pauli matrices are the spin operators."** The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$. The Pauli matrices $\sigma_i$ are the dimensionless $2\times 2$ matrices. Eigenvalues of $\sigma_z$ are $\pm 1$; eigenvalues of $\hat{S}_z$ are $\pm\hbar/2$. The distinction matters whenever units appear.

**"$P(+) = \cos^2\gamma$, not $\cos^2(\gamma/2)$."** The half-angle is essential. At $\gamma = \pi/2$ (perpendicular analyzer), $\cos^2(\pi/2) = 0$ but $\cos^2(\pi/4) = 1/2$. The incorrect formula gives $P(+) = 0$ at a perpendicular analyzer, which is wrong: a spin at the equator measured by an equatorial analyzer should give 50/50. The half-angle comes directly from the $\theta/2$ in the eigenstate parametrization.

**"During Larmor precession, $\theta$ changes."** It does not. The Hamiltonian $\hat{H} = (\hbar\omega_L/2)\sigma_z$ is diagonal; $\hat{U}(t)$ only changes the relative phase between $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$. The magnitude of $\langle\hat{S}_z\rangle = (\hbar/2)\cos\theta_0$ is conserved. If your simulation shows the Bloch vector spiraling inward, the time-evolution operator is wrong.

**"The SG_x measurement disturbed the z-spin."** There was no definite z-spin to disturb. After selecting $|\hat{x},+\rangle$, the state is not an eigenstate of $\hat{S}_z$. The noncommutativity $[\hat{S}_x, \hat{S}_z] \neq 0$ means no state can have definite values for both simultaneously. The 50/50 at the third stage is structural, not an artifact of imprecise apparatus.

**"Spin-up means the electron is spinning counterclockwise."** Spin-up ($|\!\uparrow\rangle$) is an eigenstate of $\hat{S}_z$ with eigenvalue $+\hbar/2$. It does not correspond to any physical rotation. The spinning-ball model requires superluminal equatorial speeds and is quantitatively ruled out.

---

## Exercises

### Warm-Up

**7.1** Write down the three Pauli matrices from memory. Verify by direct matrix multiplication: (a) $\sigma_x^2 = I$; (b) $\sigma_x\sigma_y = i\sigma_z$; (c) $\sigma_x\sigma_y + \sigma_y\sigma_x = 0$. State which verifies the anticommutation relation and which verifies the commutation relation.

**7.2** The chapter refutes the spinning-ball picture with a number. Redo the calculation for a proton ($m_p = 1.673 \times 10^{-27}$ kg) with spin $\hbar/2$ and radius equal to the measured proton charge radius $r_p \approx 0.85 \times 10^{-15}$ m, using $I = \frac{2}{5}m_p r_p^2$. Express the result as a multiple of $c$. Is the argument specific to the electron, or does it apply equally to the proton?

**7.3** For the state $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$, compute: (a) the probability of measuring $\hat{S}_z = +\hbar/2$; (b) $\langle\hat{S}_z\rangle$; (c) $\langle\hat{S}_z^2\rangle$; (d) $\Delta S_z = \sqrt{\langle\hat{S}_z^2\rangle - \langle\hat{S}_z\rangle^2}$. Verify that $\Delta S_z = \hbar/2$ — maximal uncertainty.

### Application

**7.4** A spin is prepared in the state $|\psi\rangle = \cos(\pi/8)|\!\uparrow\rangle + \sin(\pi/8)|\!\downarrow\rangle$ (real coefficients, $\theta = \pi/4$, $\phi = 0$). The analyzer points at $(\theta_n, \phi_n) = (\pi/3, \pi/6)$. (a) Compute $\cos\gamma$ using the dot-product formula. (b) Compute $P(+) = \cos^2(\gamma/2)$. (c) Verify $P(+) + P(-) = 1$.

**7.5** A proton is placed in field $\vec{B} = 1.5\,\hat{z}$ T. The initial state is $|\psi(0)\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ (Bloch angles $\theta_0 = \pi/2$, $\phi_0 = 0$). (a) Write $|\psi(t)\rangle$ using the Larmor time-evolution operator. (b) Compute $\langle\hat{S}_x\rangle(t)$, $\langle\hat{S}_y\rangle(t)$, $\langle\hat{S}_z\rangle(t)$. (c) What is the Larmor frequency in MHz? (d) What is the precession period in nanoseconds?

**7.6** Work through the sequential Stern–Gerlach calculation explicitly. (a) Express $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis $\{|\hat{x},+\rangle, |\hat{x},-\rangle\}$ and state the Born-rule probabilities. (b) After selecting $|\hat{x},+\rangle$, express it in the $\sigma_z$ eigenbasis and state the Born-rule probabilities. (c) State the classical hidden-variable prediction for step (b), and identify which prediction — QM or classical — agrees with experiment.

**7.7** Derive the eigenvalues of $\hat{S}_{\hat{n}} = (\hbar/2)\hat{n}\cdot\vec{\sigma}$ for a general unit vector $\hat{n}$ by computing the characteristic polynomial of the $2\times 2$ matrix. Confirm the eigenvalues are $\pm\hbar/2$ regardless of $\hat{n}$. State in one sentence why this fact directly explains "two spots for any axis."

### Synthesis and Challenge

**7.8** The Robertson uncertainty principle applied to $\hat{S}_x$ and $\hat{S}_z$ gives $\sigma_{S_x}\sigma_{S_z} \geq \frac{1}{2}|\langle[\hat{S}_x, \hat{S}_z]\rangle|$. (a) Compute $[\hat{S}_x, \hat{S}_z]$ using the Pauli algebra. (b) For the state $|\hat{x},+\rangle$, evaluate both sides of the inequality. (c) Is the bound saturated? Find a state on the Bloch sphere that saturates it.

**7.9** (Spinor double cover.) In $|\hat{n},+\rangle = \cos(\theta/2)|\!\uparrow\rangle + e^{i\phi}\sin(\theta/2)|\!\downarrow\rangle$: (a) Show that replacing $\theta \to \theta + 2\pi$ sends the state to $-|\hat{n},+\rangle$. (b) Show that $P(+)$ is the same for $|\hat{n},+\rangle$ and $-|\hat{n},+\rangle$. (c) Describe an experiment that would in principle distinguish them — why must it involve interference?

**7.10** (The anomalous *g*-factor.) The leading QED correction gives $a_e = (g_e - 2)/2 \approx \alpha/(2\pi)$, where $\alpha \approx 1/137$. (a) Compute $\alpha/(2\pi)$ and compare to the measured $a_e \approx 0.00116$. (b) Compute the fractional error in the predicted Larmor frequency for an electron in a 1 T field if you use $g = 2$ instead of $g_e \approx 2.00232$. Is this detectable in a typical ESR experiment? (c) The best measurements of $a_e$ agree with QED theory to about one part in $10^{12}$. What physical quantity must be measured to this precision?

---

## Still Puzzling

The formalism of this chapter is complete. But it raises questions the formalism cannot answer:

**Why half-integer spin at all?** The angular-momentum algebra allows $j = 0, 1/2, 1, 3/2, \ldots$ What determines which values nature uses? The spin-statistics theorem (particles with half-integer spin are fermions and must have antisymmetric states; particles with integer spin are bosons) connects spin to exchange symmetry, but its proof requires relativistic quantum field theory. Accept it as a fact for now; it will matter in Chapter 11 when counting available electron states.

**What does the Bloch sphere look like for spin-1?** A spin-1 system lives in $\mathbb{C}^3$. After removing normalization and overall phase, the state space is the projective plane $\mathbb{C}P^2$ — not a sphere. The Bloch sphere is special to spin-½. For higher spins, no such simple geometric picture exists, though the Husimi representation provides a partial substitute.

**Why does the electron have $g_e \approx 2$ rather than 1?** The Dirac equation gives $g = 2$; non-relativistic classical electrodynamics gives $g = 1$. The factor of 2 is a consequence of the spinor structure of the Dirac equation — it is built into the way the electromagnetic field couples to the Dirac spinor. The $0.00232$ correction beyond 2 then comes from QED. The two layers of explanation are conceptually distinct and historically separated by twenty years.

---

## The +1 — Simulation Exercise: The Bloch Sphere and Larmor Precession

The chapter's deliverable is `07-bloch-larmor.html`: an interactive Bloch sphere with a draggable state vector, a draggable analyzer, a real-time Born-rule probability readout, and a Larmor precession panel driven by a B-field slider.

### Part 1 — CLAUDE.md Extension

Append this block to your project's CLAUDE.md before running the build prompt:

```
## Chapter 7 — Bloch Sphere / Larmor Simulation Rules

- Single HTML file. SVG canvas only. No external assets, no three.js, no WebGL.
- Two coupled panels:
  (1) Bloch sphere (left, ~380 × 380 px): isometric lat/lon grid; two draggable
      arrows — state |ψ⟩ in blue, analyzer n̂ in orange. Numeric readouts of
      (θ_ψ, φ_ψ), (θ_n, φ_n), γ, P(+), P(−).
  (2) Larmor panel (right, ~380 × 260 px): B-field slider (0–7 T), particle
      dropdown (electron / proton), precession-frequency readout in appropriate
      units (GHz for electron, MHz for proton), animated Bloch vector tracing
      a latitude circle. Pause/resume button.
- D3 v7 from CDN. Vanilla JS only.
- All probability arithmetic: P(+) = cos²(γ/2). Never cos²(γ).
- Larmor: closed-form phase advance φ(t) = φ₀ + ω_L · t each animation frame.
  ω_L = γ · B₀, with γ from the dropdown (electron: γ_e/2π = 28.025 GHz/T;
  proton: γ_p/2π = 42.58 MHz/T).
- ⟨S_z⟩ readout must be constant during precession (verify numerically).
- All redraws through a single redraw() function.
```

### Part 2 — The Build Prompt

```
Build a D3 v7 Bloch sphere + Larmor precession simulator following CLAUDE.md.

SHOW.
State |ψ⟩ at Bloch angles (θ_ψ, φ_ψ). Analyzer n̂ at (θ_n, φ_n).
Born-rule probability: P(+) = cos²(γ/2), where
  cos γ = cos θ_ψ cos θ_n + sin θ_ψ sin θ_n cos(φ_ψ − φ_n).

Larmor precession: ω_L = γ · B₀ (γ from particle dropdown), phase advance
  φ_ψ(t) = φ_ψ(0) + ω_L · t. θ_ψ is frozen. ⟨S_z⟩ = (ℏ/2)cos θ_ψ is constant.

SAY.
Produce 07-bloch-larmor.html with two panels:
  (1) Bloch sphere: isometric lat/lon grid. Blue draggable arrow = |ψ⟩.
      Orange draggable arrow = n̂. Live readouts: (θ_ψ, φ_ψ), (θ_n, φ_n),
      γ, P(+), P(−).
  (2) Larmor panel: B₀ slider 0–7 T, particle dropdown (electron/proton),
      f_L readout in GHz or MHz. Animate the blue arrow precessing around ẑ.
      ⟨S_z⟩ readout constant-checks itself each frame.

CONSTRAIN.
- D3 v7 from CDN. SVG only. Vanilla JS.
- Half-angle Born rule: P(+) = cos²(γ/2). Verify at γ = π/2: P(+) = 0.500.
- Larmor: closed-form φ(t), not numerical integration. θ frozen.
- Electron gyromagnetic ratio negative: precession direction must flip relative
  to proton when particle dropdown changes.

VERIFY.
Six checks:
(a) State at north pole, analyzer at north pole: P(+) = 1.00.
(b) Same state, analyzer at south pole: P(+) = 0.00.
(c) Same state, analyzer at equator (any φ_n): P(+) = 0.50.
(d) Proton at B₀ = 1.5 T: f_L = 63.87 MHz, period ≈ 15.66 ns.
(e) During precession, θ_ψ constant, φ_ψ advances linearly with time.
(f) P(+) + P(−) = 1.000 for every analyzer position.
```

### Part 3 — Exploration Tasks

**Verify the antipode.** Set state to north pole ($|\!\uparrow\rangle$), analyzer to north pole. Read $P(+) = 1.00$. Rotate analyzer to south pole: $P(+) = 0.00$. Set analyzer to $\theta_n = \pi/3$: predict $P(+) = \cos^2(\pi/6) = 3/4$. Verify.

**Verify the half-angle.** Set state to the equator ($\theta_\psi = \pi/2$). For analyzer along $\hat{z}$ ($\theta_n = 0$), confirm $P(+) = 1/2$. If any equatorial state gives $P(+) = 0$ at $\theta_n = \pi/2$, the half-angle is missing.

**Larmor period.** Proton, $B_0 = 1.5$ T. Read $f_L = 63.87$ MHz, period $\approx 15.66$ ns. Switch to $B_0 = 3.0$ T: period halves. Switch to electron at $B_0 = 1$ mT: $f_L = 28.025$ MHz. Confirm precession direction reverses (electron $\gamma < 0$).

**Frozen polar angle.** Start precession from $\theta_0 = \pi/4$. Let it run for 100 periods. Confirm $\theta_\psi$ has not drifted. If it has, the time-evolution operator has a numerical error.

### Part 4 — Six Failure Modes to Check

**Half-angle dropped.** At $\gamma = \pi/2$, $P(+)$ must be $1/2$, not $0$. If you get $0$, the code uses $\cos^2\gamma$ instead of $\cos^2(\gamma/2)$.

**Wrong $\gamma$ formula.** The dot product in Bloch-vector space: $\cos\gamma = \hat{n}_\psi\cdot\hat{n}_n$, not the angle between the complex spinors.

**Larmor units error.** $\gamma_p/(2\pi) = 42.58$ MHz/T, so $\omega_L = 2\pi \times 42.58 \times 10^6 \times B_0$ rad/s. Dropping the $2\pi$ makes precession $2\pi$ times too slow.

**Wrong electron precession direction.** $\gamma_e < 0$ (electron magnetic moment antiparallel to spin). If electron and proton precess in the same direction, the sign is wrong.

**Polar angle drift.** Only $\phi$ should advance during Larmor precession. $\theta$ is frozen by the diagonal form of $\hat{U}(t)$.

**Normalization failure.** $P(+) + P(-) = 1.000$ for every analyzer position, to floating-point precision.

---

## References

- Stern, O. and Gerlach, W. (1922). "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld." *Zeitschrift für Physik*, 9(1), 349–352. [verify]
- Uhlenbeck, G. E. and Goudsmit, S. (1925). "Ersetzung der Hypothese vom unmechanischen Zwang durch eine Forderung bezüglich des inneren Verhaltens jedes einzelnen Elektrons." *Naturwissenschaften*, 13(47), 953–954. [verify]
- Dirac, P. A. M. (1928). "The quantum theory of the electron." *Proceedings of the Royal Society A*, 117(778), 610–624. [verify]
- Rauch, H., Zeilinger, A., Badurek, G., Wilfing, A., Bauspiess, W., and Bonse, U. (1975). "Verification of coherent spinor rotation of fermions." *Physics Letters A*, 54(6), 425–427. [verify]
- Werner, S. A., Colella, R., Overhauser, A. W., and Eagen, C. F. (1975). "Observation of the phase shift of a neutron due to precession in a magnetic field." *Physical Review Letters*, 35(16), 1053–1055. [verify]
- Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapter 3 (spin), Chapter 4 (time evolution of two-state systems).
- Griffiths, D. J. and Schroeter, D. F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Section 4.4 (spin).
- Sakurai, J. J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 1 (Stern–Gerlach, spin formalism, Pauli matrices).

*Bridge to Chapter 8: Spin is the fourth quantum number. Chapter 8 asks what happens when two spin-½ particles interact — or when a spin couples to orbital angular momentum. The Bloch sphere picture and Pauli algebra built here are the direct inputs. The challenge: the combined system has four states, not two, and we need a new basis — the coupled basis — to handle it.*
