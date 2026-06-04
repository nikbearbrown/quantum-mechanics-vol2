# Chapter 7 — Spin and the Bloch Sphere

In February 1922, Otto Stern and Walther Gerlach sent a beam of neutral silver atoms through an inhomogeneous magnetic field and caught them on a glass plate. The field gradient exerts a force proportional to the magnetic moment component along the field axis. Classical physics says the moments can point in any direction, so the deposit on the plate should be a smear. Stern developed the plate. He found two spots.

Not a smear. Two distinct spots, nothing in between.

Whatever silver atoms are doing, the component of their magnetic moment along the field axis takes exactly two values. And this is true for any axis you point the apparatus: two spots, always. The experiment is unambiguous, and it sat unexplained for three years — partly because Stern and Gerlach themselves thought they were confirming the old Bohr-Sommerfeld orbital quantization. Silver's valence electron is in an $s$ orbital, which has zero orbital angular momentum. The two spots came from something nobody had proposed yet: intrinsic spin of the electron, hypothesized by Uhlenbeck and Goudsmit in 1925. Stern and Gerlach got the right answer before the right question existed.

---

## Two Values Forces Two Dimensions

The empirical fact — always two values, any axis — points directly to the Hilbert space. Whatever spin lives in, that space must support any spin-component operator with exactly two eigenvalues. The smallest complex vector space that does this is $\mathbb{C}^2$. This is not a guess; it is the minimal structure forced by "two and only two."

Choose the eigenstates of the $z$-component as basis:

$$|\!\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}.$$

The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$, where $\sigma_x, \sigma_y, \sigma_z$ are the Pauli matrices:

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Four facts, all verifiable by direct multiplication. Each squares to the identity: $\sigma_i^2 = I$. Each is traceless. Different Pauli matrices anticommute: $\sigma_i\sigma_j + \sigma_j\sigma_i = 0$ for $i \neq j$. And they satisfy the angular-momentum commutation relations: $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, which means $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ — the same algebra as orbital angular momentum $\hat{L}$. That algebraic coincidence is why "spin" deserves the name angular momentum.

The four facts pack into one multiplication table:

$$\boxed{\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k.}$$

Memorize this. It is the entire Pauli algebra.

---

## Why Spin Is Not Rotation

Many students arrive with a picture: the electron is a tiny ball spinning on its own axis. Kill this picture with a number.

Assume the electron has angular momentum $\hbar/2$ and the spinning-ball picture is true. Take the most generous possible radius — the classical electron radius $r_e \approx 2.82\times10^{-15}$ m (real experiments bound the electron below $10^{-18}$ m, but a smaller radius makes the argument worse). For a uniform solid sphere, $I = \frac{2}{5}m_e r_e^2$, and $L = I\omega$ gives equatorial surface speed:

$$v = \omega r_e = \frac{5\hbar}{4m_e r_e} \approx \frac{5\times1.055\times10^{-34}}{4\times9.11\times10^{-31}\times2.82\times10^{-15}} \approx 5.1\times10^{10}\ \text{m/s}.$$

The speed of light is $c \approx 3.0\times10^8$ m/s. The required equatorial speed is roughly $170c$. The picture is not wrong by a small margin; it is wrong by two orders of magnitude.

So what is spin? An internal degree of freedom that transforms as a representation of $\mathrm{SU}(2)$ — the group of $2\times2$ unitary matrices with determinant 1 — under rotations. Not any motion in physical space. Dirac showed in 1928 that spin-½ falls out of the requirement that the wave equation be Lorentz-covariant and first-order in time. You do not put spin in by hand; it is already there when you insist on the right symmetries.

**Intrinsic** means: the algebra is that of angular momentum, the carrier is an $\mathrm{SU}(2)$ representation, and the underlying degree of freedom does not correspond to any motion in space.

---

## Spin Along Any Axis

Pick a unit vector $\hat{n} = (\sin\theta\cos\phi,\,\sin\theta\sin\phi,\,\cos\theta)$. The spin operator along $\hat{n}$ is

$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\hat{n}\cdot\vec{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\\sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$

This matrix has trace zero and determinant $-(\hbar/2)^2$, so its eigenvalues are always $\pm\hbar/2$, regardless of which direction $\hat{n}$ points. The formalism delivers exactly what the 1922 experiment found: two values, every axis.

The $+\hbar/2$ eigenvector, normalized using half-angle identities:

$$|\hat{n},+\rangle = \cos\!\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\!\tfrac{\theta}{2}|\!\downarrow\rangle.$$

Every pure spin-½ state has this form for some $(\theta, \phi)$. A normalized state has two complex components, one normalization constraint, one unobservable global phase: two real parameters. Two real parameters parametrize a sphere.

---

## The Bloch Sphere

The parametrization $(\theta, \phi)$ maps every pure spin-½ state to a point on a unit sphere — the **Bloch sphere**. North pole ($\theta = 0$): $|\!\uparrow\rangle$. South pole ($\theta = \pi$): $|\!\downarrow\rangle$. Equator ($\theta = \pi/2$): equal superpositions $(|\!\uparrow\rangle + e^{i\phi}|\!\downarrow\rangle)/\sqrt{2}$, with $\phi$ varying around the equator. Every point is a state; every state is a point.

The Born rule takes a clean geometric form. If the state Bloch vector points at $(\theta_\psi, \phi_\psi)$ and the analyzer points at $(\theta_n, \phi_n)$, let $\gamma$ be the angle between them:

$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n).$$

The probability of outcome $+\hbar/2$ is

$$\boxed{P(+) = \cos^2\!\tfrac{\gamma}{2}, \qquad P(-) = \sin^2\!\tfrac{\gamma}{2}.}$$

Three checks: aligned ($\gamma = 0$): $P(+) = 1$. Anti-aligned ($\gamma = \pi$): $P(+) = 0$. Perpendicular ($\gamma = \pi/2$): $P(+) = 1/2$. Three correct limits, one formula.

The half-angle $\gamma/2$ is essential. At $\gamma = \pi/2$, $\cos^2(\pi/2) = 0$ but $\cos^2(\pi/4) = 1/2$. Using $\cos^2\gamma$ instead of $\cos^2(\gamma/2)$ gives zero at the perpendicular, which is wrong.

The half-angle has a deeper consequence. Rotate the analyzer by $2\pi$ — a full turn in physical space. The angle $\theta$ goes to $\theta + 2\pi$, and $\cos(\theta/2)$ becomes $\cos(\theta/2 + \pi) = -\cos(\theta/2)$. The spin state acquires an overall minus sign. Only after $4\pi$ rotation does the state return to itself. This is the **spinor double cover**: spin states live in $\mathrm{SU}(2)$, which wraps twice around the ordinary rotation group $\mathrm{SO}(3)$. A $2\pi$ rotation that takes every vector in space back to itself takes a spinor to its negative. This was directly observed in neutron interferometry by Rauch et al. (1975) and Werner et al. (1975). [verify]

---

## Larmor Precession

A spin in a uniform field $\vec{B} = B_0\hat{z}$ has Hamiltonian

$$\hat{H} = -\vec{\mu}\cdot\vec{B} = \frac{\gamma B_0\hbar}{2}\sigma_z,$$

where $\gamma$ is the gyromagnetic ratio: $\gamma_e/(2\pi) \approx 28.025$ GHz/T for the electron, $\gamma_p/(2\pi) \approx 42.58$ MHz/T for the proton. The Hamiltonian is diagonal in the $\hat{S}_z$ basis, so the time-evolution operator is:

$$\hat{U}(t) = \begin{pmatrix}e^{-i\omega_L t/2}&0\\0&e^{+i\omega_L t/2}\end{pmatrix}, \qquad \omega_L = \gamma B_0.$$

Starting from polar angle $\theta_0$ and azimuth $\phi_0 = 0$:

$$|\psi(t)\rangle = \cos\!\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\omega_L t}\sin\!\tfrac{\theta_0}{2}|\!\downarrow\rangle.$$

The polar angle stays frozen. The azimuth advances at the Larmor frequency: $\phi(t) = \omega_L t$. On the Bloch sphere, the state traces a latitude circle at constant $\theta_0$, precessing around $\hat{z}$. The expectation values:

$$\langle\hat{S}_x\rangle = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t), \qquad \langle\hat{S}_y\rangle = \tfrac{\hbar}{2}\sin\theta_0\sin(\omega_L t), \qquad \langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos\theta_0.$$

The spin vector precesses in the $xy$-plane at $\omega_L$ while its $z$-component is conserved. This is Larmor precession — formally identical to classical magnetic moment precession, except what precesses is the probability distribution over measurement outcomes, not a physical pointer.

The numbers are clinically real. For a proton ($\gamma_p/(2\pi) = 42.58$ MHz/T):

<!-- → [TABLE: Proton Larmor frequencies at standard MRI field strengths — 0.5 T open MRI 21.3 MHz; 1.5 T clinical MRI 63.9 MHz; 3.0 T research MRI 127.7 MHz; 7.0 T ultra-high-field 298.1 MHz] -->

The formula $\omega_L = \gamma B_0$ is the operating equation of every MRI scanner, used on millions of patients per year.

---

## What the Sequential Experiment Is Really Saying

Prepare a beam of silver atoms and send it through an $\mathrm{SG}_z$ apparatus. Block the lower output. The surviving atoms are in $|\!\uparrow\rangle$. Send them through an $\mathrm{SG}_x$ apparatus. The $\hat{S}_x$ eigenstates are $|\hat{x},\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$. Since $|\!\uparrow\rangle = (|\hat{x},+\rangle + |\hat{x},-\rangle)/\sqrt{2}$, the Born rule gives $P(\hat{x},\pm) = 1/2$. Block the $|\hat{x},-\rangle$ output. The surviving atoms are in $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. Feed them into a second $\mathrm{SG}_z$. Result: 50/50.

The atoms started definitely spin-up along $\hat{z}$. After an intermediate $\hat{x}$ measurement, they are 50/50 along $\hat{z}$ again.

The tempting interpretation: the $\mathrm{SG}_x$ device disturbed the atoms, scrambling their $z$-component. This is wrong.

The operators $\hat{S}_x$ and $\hat{S}_z$ do not commute: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$. No state can be simultaneously an eigenstate of both. After the $\mathrm{SG}_x$ measurement selects $|\hat{x},+\rangle$, that state simply is not an eigenstate of $\hat{S}_z$ — it has no definite $z$-component, not a definite value that was disturbed by the apparatus. There is nothing there to scramble. The 50/50 at stage three is the Born rule applied to a state that genuinely has no definite $\hat{S}_z$.

A naive hidden-variable picture — each atom carries pre-existing values $(\mu_x, \mu_z)$ that the apparatuses read off — would predict that selecting $\mu_z = +$ at stage one and then $\mu_x = +$ at stage two leaves $\mu_z$ unchanged, so stage three should return $\mu_z = +$ with probability 1. Experiment gives 50/50. Pre-existing definite values for non-commuting observables are inconsistent with the data. The algebra forces this conclusion.

---

## Worked Example — Bloch Vector and Precession

A spin is prepared at Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$. Find the Born-rule probability for $+\hbar/2$ along $\hat{z}$, then place this proton in $B_0 = 1.5$ T and track the precession.

**The state:**

$$|\psi\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i\pi/4}\sin(\pi/6)|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$

**Bloch vector:** $\hat{n}_\psi = (\sin\theta_0\cos\phi_0,\,\sin\theta_0\sin\phi_0,\,\cos\theta_0) = (\sqrt{6}/4,\,\sqrt{6}/4,\,1/2)$. Check: $6/16 + 6/16 + 1/4 = 1$. ✓

**Born-rule probability along $\hat{z}$:** The analyzer is at $(\theta_n, \phi_n) = (0, 0)$, so $\cos\gamma = \cos\theta_0\cdot 1 = 1/2$, giving $\gamma = \pi/3$. Then

$$P(+) = \cos^2(\pi/6) = 3/4.$$

Verify directly: $|\langle\!\uparrow|\psi\rangle|^2 = |\cos(\pi/6)|^2 = 3/4$. ✓

**Larmor precession:** For a proton at $B_0 = 1.5$ T,

$$f_L = \frac{\gamma_p}{2\pi}\cdot B_0 = 42.58\ \text{MHz/T}\times 1.5\ \text{T} = 63.87\ \text{MHz}, \qquad T_L = 15.66\ \text{ns}.$$

The time-evolved state is $|\psi(t)\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin(\pi/6)|\!\downarrow\rangle$. The polar angle stays at $\theta_0 = \pi/3$; the azimuth advances at $\omega_L$. The probability $P(+)$ along $\hat{z}$ is $|\cos(\pi/6)|^2 = 3/4$ at every instant: $\langle\hat{S}_z\rangle$ is a constant of motion.

If $\theta_0 = 0$, the state is already an eigenstate of $\hat{H}$; the phase $e^{i\omega_L t}$ multiplies a zero coefficient and produces no precession. The equatorial case $\theta_0 = \pi/2$ gives maximum precession: $\langle\hat{S}_z\rangle = 0$ always, while $\langle\hat{S}_x\rangle$ and $\langle\hat{S}_y\rangle$ oscillate at full amplitude $\hbar/2$ — the Bloch vector traces the equator at 63.87 MHz.

---

## The *g*-Factor

The Dirac equation predicts $g_e = 2$ exactly. The measured value is $g_e \approx 2.00232$. The deviation $a_e = (g_e - 2)/2 \approx 0.00116$ is not a failure of Dirac. It is the leading QED radiative correction from virtual photons dressing the bare electron: $a_e \approx \alpha/(2\pi)$ where $\alpha \approx 1/137$ is the fine-structure constant. Agreement between QED and experiment extends to thirteen significant figures, making it one of the most precisely tested predictions in physics.

When you write $\hat{H} = \gamma B_0\hat{S}_z$, use the experimental $\gamma$, which already includes the anomalous correction. The deviation from $g = 2$ is a window into the virtual-photon structure of QED, not an error to be corrected away.

---

## The +1 — Simulation Exercise

The deliverable is `07-bloch-larmor.html`: an interactive Bloch sphere with draggable state and analyzer vectors, real-time Born-rule probability, and a Larmor precession panel driven by a field-strength slider.

### CLAUDE.md Extension

Append this block to your project's `CLAUDE.md` before building:

````markdown
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
````

### The Build Prompt

````
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
````

### Exploration Tasks

**Verify the antipode.** State at north pole, analyzer at north pole: $P(+) = 1.00$. Rotate analyzer to south pole: $P(+) = 0.00$. Set $\theta_n = \pi/3$: predict $P(+) = \cos^2(\pi/6) = 3/4$. Verify.

**Verify the half-angle.** Set state to equator ($\theta_\psi = \pi/2$), analyzer along $\hat{z}$ ($\theta_n = 0$). Confirm $P(+) = 1/2$. If any equatorial state gives $P(+) = 0$ at a perpendicular analyzer, the half-angle formula is missing.

**Larmor period.** Proton, $B_0 = 1.5$ T: confirm $f_L = 63.87$ MHz, period $\approx 15.66$ ns. Switch to $B_0 = 3.0$ T: period halves. Switch to electron at $B_0 = 1$ mT: $f_L \approx 28$ MHz. Confirm precession direction reverses (electron $\gamma < 0$).

**Frozen polar angle.** Start precession from $\theta_0 = \pi/4$. Run for 100 periods. Confirm $\theta_\psi$ has not drifted. Drift means the time-evolution operator has a numerical error.

---

## References

- Stern, O. and Gerlach, W. (1922). "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld." *Zeitschrift für Physik*, 9(1), 349–352. [verify]
- Uhlenbeck, G.E. and Goudsmit, S. (1925). "Ersetzung der Hypothese vom unmechanischen Zwang durch eine Forderung bezüglich des inneren Verhaltens jedes einzelnen Elektrons." *Naturwissenschaften*, 13(47), 953–954. [verify]
- Dirac, P.A.M. (1928). "The quantum theory of the electron." *Proceedings of the Royal Society A*, 117(778), 610–624. [verify]
- Rauch, H. et al. (1975). "Verification of coherent spinor rotation of fermions." *Physics Letters A*, 54(6), 425–427. [verify]
- Werner, S.A. et al. (1975). "Observation of the phase shift of a neutron due to precession in a magnetic field." *Physical Review Letters*, 35(16), 1053–1055. [verify]
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapters 3–4. [verify]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §4.4. [verify]
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 1. [verify]

---

*Chapter 8 follows: spin is the fourth quantum number. When two spin-½ particles interact — or when spin couples to orbital angular momentum — the combined system has four states, not two. The challenge is building the coupled basis from the tensor product of two Bloch spheres. The Clebsch-Gordan coefficients are the translation dictionary between the uncoupled and coupled bases.*
