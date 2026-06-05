# Chapter 7 — Spin and the Bloch Sphere

The Stern–Gerlach experiment (1922) passes neutral silver atoms through an inhomogeneous magnetic field. The field gradient exerts a force proportional to the component of the magnetic moment along the field axis. Classically the moment orients arbitrarily, so the deposit should form a continuous band. The measured deposit is two discrete spots, with no intensity between them.

The component of the atomic magnetic moment along the field axis takes exactly two values. Reorient the apparatus along any axis and the result is unchanged: two spots, every time.

The result went unexplained for three years. Stern and Gerlach initially read it as confirmation of Bohr–Sommerfeld orbital quantization. That reading fails: silver's valence electron occupies an $s$ orbital with zero orbital angular momentum. The two spots originate from electron intrinsic spin, proposed by Uhlenbeck and Goudsmit in 1925. The measurement preceded the concept needed to interpret it.

---

## Two Values Forces Two Dimensions

Two outcomes along any axis fixes the Hilbert space. The space must support a spin-component operator with exactly two eigenvalues along every direction. The smallest complex vector space meeting that condition is $\mathbb{C}^2$. The dimension is forced by the data, not assumed.

Choose the eigenstates of the $z$-component as basis:

$$|\!\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}.$$

The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$, where $\sigma_x, \sigma_y, \sigma_z$ are the Pauli matrices:

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Four properties follow by direct multiplication. Each matrix squares to the identity: $\sigma_i^2 = I$. Each is traceless. Distinct Pauli matrices anticommute: $\sigma_i\sigma_j + \sigma_j\sigma_i = 0$ for $i \neq j$. They satisfy $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, equivalently $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ — the angular-momentum commutation relations, identical to those of orbital $\hat{L}$. That shared algebra is the reason spin is classified as angular momentum.

The four properties combine into one product rule:

$$\boxed{\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k.}$$

This is the complete Pauli algebra. All spin-½ computations reduce to it.

---

## Why Spin Is Not Rotation

The spinning-ball picture of the electron is ruled out quantitatively. Assume angular momentum $\hbar/2$ from rigid rotation. Take the largest plausible radius, the classical electron radius $r_e \approx 2.82\times10^{-15}$ m (experiment bounds the electron below $10^{-18}$ m; a smaller radius worsens the conclusion). For a uniform solid sphere $I = \frac{2}{5}m_e r_e^2$, and $L = I\omega$ gives equatorial surface speed:

$$v = \omega r_e = \frac{5\hbar}{4m_e r_e} \approx \frac{5\times1.055\times10^{-34}}{4\times9.11\times10^{-31}\times2.82\times10^{-15}} \approx 5.1\times10^{10}\ \text{m/s}.$$

With $c \approx 3.0\times10^8$ m/s, the required surface speed is about $170c$. The picture fails by two orders of magnitude.

Spin is an internal degree of freedom that transforms as a representation of $\mathrm{SU}(2)$ — the $2\times2$ unitary matrices with determinant 1 — under rotations. It is not motion in physical space. Dirac (1928) showed that spin-½ follows from requiring the wave equation to be Lorentz-covariant and first-order in time. Spin is not added by hand; it appears once the correct symmetry is imposed.

**Intrinsic** means: the algebra is that of angular momentum, the carrier is an $\mathrm{SU}(2)$ representation, and the underlying degree of freedom does not correspond to any motion in space.

---

## Spin Along Any Axis

For a unit vector $\hat{n} = (\sin\theta\cos\phi,\,\sin\theta\sin\phi,\,\cos\theta)$, the spin operator along $\hat{n}$ is

$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\hat{n}\cdot\vec{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\\sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$

This matrix is traceless with determinant $-(\hbar/2)^2$, so its eigenvalues are $\pm\hbar/2$ for every $\hat{n}$. The formalism reproduces the experimental result directly: two values, every axis.

The normalized $+\hbar/2$ eigenvector, via half-angle identities:

$$|\hat{n},+\rangle = \cos\!\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\!\tfrac{\theta}{2}|\!\downarrow\rangle.$$

Every pure spin-½ state has this form for some $(\theta, \phi)$. A normalized state carries two complex amplitudes, subject to one normalization constraint and one unobservable global phase: two real parameters remain. Two real parameters parametrize a sphere.

---

## The Bloch Sphere

The pair $(\theta, \phi)$ maps each pure spin-½ state to a point on a unit sphere, the **Bloch sphere**. North pole ($\theta = 0$): $|\!\uparrow\rangle$. South pole ($\theta = \pi$): $|\!\downarrow\rangle$. Equator ($\theta = \pi/2$): equal superpositions $(|\!\uparrow\rangle + e^{i\phi}|\!\downarrow\rangle)/\sqrt{2}$, with $\phi$ around the circle. The correspondence between states and points is one-to-one.

The Born rule has a geometric form. Let the state Bloch vector point at $(\theta_\psi, \phi_\psi)$ and the analyzer at $(\theta_n, \phi_n)$, with $\gamma$ the angle between them:

$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n).$$

The probability of outcome $+\hbar/2$ is

$$\boxed{P(+) = \cos^2\!\tfrac{\gamma}{2}, \qquad P(-) = \sin^2\!\tfrac{\gamma}{2}.}$$

Three limits check the formula: aligned ($\gamma = 0$) gives $P(+) = 1$; anti-aligned ($\gamma = \pi$) gives $P(+) = 0$; perpendicular ($\gamma = \pi/2$) gives $P(+) = 1/2$.

The half-angle is required. At $\gamma = \pi/2$, $\cos^2(\pi/2) = 0$ while $\cos^2(\pi/4) = 1/2$. Substituting $\cos^2\gamma$ for $\cos^2(\gamma/2)$ gives zero at the perpendicular, which contradicts measurement.

The half-angle also governs rotation behavior. Rotate the analyzer by $2\pi$ in physical space: $\theta \to \theta + 2\pi$, and $\cos(\theta/2) \to \cos(\theta/2 + \pi) = -\cos(\theta/2)$. The state picks up an overall minus sign. Only a $4\pi$ rotation returns it to itself. This is the **spinor double cover**: spin states transform under $\mathrm{SU}(2)$, which covers the rotation group $\mathrm{SO}(3)$ twice. A $2\pi$ rotation, which is the identity on ordinary vectors, sends a spinor to its negative. The effect was observed in neutron interferometry by Rauch et al. (1975) and Werner et al. (1975).

---

## Larmor Precession

A spin in a uniform field $\vec{B} = B_0\hat{z}$ has Hamiltonian

$$\hat{H} = -\vec{\mu}\cdot\vec{B} = \frac{\gamma B_0\hbar}{2}\sigma_z,$$

where $\gamma$ is the gyromagnetic ratio: $\gamma_e/(2\pi) \approx 28.025$ GHz/T for the electron, $\gamma_p/(2\pi) \approx 42.58$ MHz/T for the proton. The Hamiltonian is diagonal in the $\hat{S}_z$ basis, so the time-evolution operator is

$$\hat{U}(t) = \begin{pmatrix}e^{-i\omega_L t/2}&0\\0&e^{+i\omega_L t/2}\end{pmatrix}, \qquad \omega_L = \gamma B_0.$$

Starting from polar angle $\theta_0$ and azimuth $\phi_0 = 0$:

$$|\psi(t)\rangle = \cos\!\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\omega_L t}\sin\!\tfrac{\theta_0}{2}|\!\downarrow\rangle.$$

The polar angle is constant. The azimuth advances at the Larmor frequency: $\phi(t) = \omega_L t$. On the Bloch sphere the state traces a circle of latitude at fixed $\theta_0$, precessing about $\hat{z}$. The expectation values:

$$\langle\hat{S}_x\rangle = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t), \qquad \langle\hat{S}_y\rangle = \tfrac{\hbar}{2}\sin\theta_0\sin(\omega_L t), \qquad \langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos\theta_0.$$

The spin vector precesses in the $xy$-plane at $\omega_L$ with $\langle\hat{S}_z\rangle$ conserved. This is Larmor precession. It is formally identical to classical magnetic-moment precession, but the precessing quantity is the probability distribution over measurement outcomes, not a physical pointer.

For a proton ($\gamma_p/(2\pi) = 42.58$ MHz/T):

<!-- → [TABLE: Proton Larmor frequencies at standard MRI field strengths — 0.5 T open MRI 21.3 MHz; 1.5 T clinical MRI 63.9 MHz; 3.0 T research MRI 127.7 MHz; 7.0 T ultra-high-field 298.1 MHz] -->

The relation $\omega_L = \gamma B_0$ is the operating equation of every MRI scanner.

---

## What the Sequential Experiment Is Really Saying

Send silver atoms through an $\mathrm{SG}_z$ apparatus and block the lower output. The survivors are in $|\!\uparrow\rangle$. Pass them through an $\mathrm{SG}_x$ apparatus. The $\hat{S}_x$ eigenstates are $|\hat{x},\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$. Since $|\!\uparrow\rangle = (|\hat{x},+\rangle + |\hat{x},-\rangle)/\sqrt{2}$, the Born rule gives $P(\hat{x},\pm) = 1/2$. Block the $|\hat{x},-\rangle$ output; the survivors are in $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. Send these into a second $\mathrm{SG}_z$. The result is 50/50.

The atoms entered definitely spin-up along $\hat{z}$. After an intermediate $\hat{x}$ measurement they are 50/50 along $\hat{z}$.

The disturbance interpretation — that $\mathrm{SG}_x$ scrambled the $z$-component — is incorrect.

$\hat{S}_x$ and $\hat{S}_z$ do not commute: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$. No state is a simultaneous eigenstate of both. After $\mathrm{SG}_x$ selects $|\hat{x},+\rangle$, that state has no definite $\hat{S}_z$ — there is no prior value for the apparatus to scramble. The 50/50 at stage three is the Born rule applied to a state with no definite $\hat{S}_z$.

A hidden-variable model in which each atom carries pre-existing values $(\mu_x, \mu_z)$ predicts that selecting $\mu_z = +$ then $\mu_x = +$ leaves $\mu_z$ intact, so stage three returns $\mu_z = +$ with probability 1. Measurement gives 50/50. Pre-existing definite values for non-commuting observables are inconsistent with the data. The algebra forces this.

---

## Worked Example — Bloch Vector and Precession

**Given.** A spin prepared at Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$.

**Find.** The Born-rule probability for $+\hbar/2$ along $\hat{z}$; then the precession when this proton is placed in $B_0 = 1.5$ T.

**Solution.**

State:

$$|\psi\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i\pi/4}\sin(\pi/6)|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$

Bloch vector: $\hat{n}_\psi = (\sin\theta_0\cos\phi_0,\,\sin\theta_0\sin\phi_0,\,\cos\theta_0) = (\sqrt{6}/4,\,\sqrt{6}/4,\,1/2)$.

Probability along $\hat{z}$: the analyzer is at $(\theta_n, \phi_n) = (0, 0)$, so $\cos\gamma = \cos\theta_0\cdot 1 = 1/2$, giving $\gamma = \pi/3$. Then

$$P(+) = \cos^2(\pi/6) = 3/4.$$

Larmor precession: for a proton at $B_0 = 1.5$ T,

$$f_L = \frac{\gamma_p}{2\pi}\cdot B_0 = 42.58\ \text{MHz/T}\times 1.5\ \text{T} = 63.87\ \text{MHz}, \qquad T_L = 15.66\ \text{ns}.$$

The time-evolved state is $|\psi(t)\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin(\pi/6)|\!\downarrow\rangle$. The polar angle stays at $\theta_0 = \pi/3$; the azimuth advances at $\omega_L$.

**Check.** Norm of the Bloch vector: $6/16 + 6/16 + 1/4 = 1$. ✓ Direct probability: $|\langle\!\uparrow|\psi\rangle|^2 = |\cos(\pi/6)|^2 = 3/4$, matching the geometric result. ✓ During precession $P(+)$ along $\hat{z}$ is $|\cos(\pi/6)|^2 = 3/4$ at all times, confirming $\langle\hat{S}_z\rangle$ is a constant of motion. Limiting cases: at $\theta_0 = 0$ the state is an $\hat{H}$ eigenstate and the phase $e^{i\omega_L t}$ multiplies a zero coefficient — no precession. At $\theta_0 = \pi/2$, $\langle\hat{S}_z\rangle = 0$ always while $\langle\hat{S}_x\rangle$ and $\langle\hat{S}_y\rangle$ oscillate at full amplitude $\hbar/2$; the Bloch vector traces the equator at 63.87 MHz.

---

## The *g*-Factor

The Dirac equation predicts $g_e = 2$ exactly. The measured value is $g_e \approx 2.00232$. The deviation $a_e = (g_e - 2)/2 \approx 0.00116$ is the leading QED radiative correction from virtual photons dressing the electron: $a_e \approx \alpha/(2\pi)$, where $\alpha \approx 1/137$ is the fine-structure constant. QED and experiment agree to thirteen significant figures, among the most precisely tested predictions in physics.

In $\hat{H} = \gamma B_0\hat{S}_z$, use the experimental $\gamma$, which already incorporates the anomalous correction. The departure from $g = 2$ is a measurement of QED virtual-photon structure, not an error to remove.

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

- Gerlach, W. and Stern, O. (1922). "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld." *Zeitschrift für Physik*, 9(1), 349–352.
- Uhlenbeck, G.E. and Goudsmit, S. (1925). "Ersetzung der Hypothese vom unmechanischen Zwang durch eine Forderung bezüglich des inneren Verhaltens jedes einzelnen Elektrons." *Naturwissenschaften*, 13(47), 953–954.
- Dirac, P.A.M. (1928). "The quantum theory of the electron." *Proceedings of the Royal Society A*, 117(778), 610–624.
- Rauch, H. et al. (1975). "Verification of coherent spinor rotation of fermions." *Physics Letters A*, 54(6), 425–427.
- Werner, S.A. et al. (1975). "Observation of the phase shift of a neutron due to precession in a magnetic field." *Physical Review Letters*, 35(16), 1053–1055.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapters 3–4.
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §4.4.
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 1.

---

## Running Project — Build the Atom

**This chapter adds:** the spin quantum number — $m_s = \pm\tfrac12$ promotes each spatial orbital $(n,\ell,m_\ell)$ into two *spin-orbitals*, which is the factor of 2 in the subshell capacity $2(2\ell+1)$ and the second degree of freedom Pauli exclusion (Chapter 10) acts on.

The Stern–Gerlach two-valuedness is the simulator's fourth label. A spatial orbital is not a slot for one electron — it is a slot for two, one $m_s=+\tfrac12$ and one $m_s=-\tfrac12$, because spin lives in an independent $\mathbb C^2$. This chapter formalizes that $m_s$ takes exactly two values along any axis, doubling every capacity and completing the $(n,\ell,m_\ell,m_s)$ label that Chapter 11's Aufbau filling consumes.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Extending the orbital data structure so every spatial orbital generates two spin-orbitals ($m_s=\pm\tfrac12$) — *Why AI works here:* it is a doubling of a list; you check that a subshell with $2\ell+1$ spatial orbitals yields $2(2\ell+1)$ spin-orbitals.
- Building the Pauli matrices and the spin-projection operator $\hat S_z = (\hbar/2)\sigma_z$ for sanity checks — *Why AI works here:* the Pauli algebra is fixed and verifiable ($\sigma_i^2=\mathbb 1$, eigenvalues $\pm1$).

**The tell:** You are using AI well when you can check the doubling against the capacity — a $p$ subshell must now expose 6 spin-orbitals, a $d$ subshell 10.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding that spin is an *independent* degree of freedom (not derivable from orbital motion) — *Why AI fails here:* an LLM may "explain" spin as a tiny rotating sphere; the spinning-ball picture is numerically absurd ($v\approx170c$), and treating spin as orbital-derived would wrongly couple $m_s$ to $m_\ell$ in the data model.
- Asserting that the two spin states are along a *fixed* axis — *Why AI fails here:* the two-valuedness holds along *any* axis, and a model that bakes in "up/down only along $z$" will misrepresent the spin space; this is a structural physics call, not a coding choice.

**The tell:** If you cannot explain why each spatial orbital holds exactly two electrons — two spin states, any axis — without the AI, the AI supplied the physics that should have been yours.
**Physics-judgment connection:** this trains checking the capacity-doubling against the experimentally fixed "two values, every axis," and rejecting any model where $m_s$ is secretly tied to $m_\ell$.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** a module `spin.py` that promotes spatial orbitals to spin-orbitals and supplies $\hat S_z$.
**Tool:** Claude chat.
**The Prompt:**
```
I am building an atomic-structure simulator. Spatial orbitals (n, l, m_l) now
need a spin label to become spin-orbitals.

Write a Python module `spin.py` (numpy only) that:

1. spin_orbitals(spatial_orbitals) taking a list of (n, l, m_l) tuples and
   returning the doubled list of (n, l, m_l, m_s) with m_s in {+1/2, -1/2}.
2. subshell_spin_orbitals(n, l) returning all 2*(2l+1) spin-orbitals of that
   subshell.
3. pauli() returning sigma_x, sigma_y, sigma_z, and Sz() returning (hbar/2)*
   sigma_z with hbar=1; assert each sigma squares to I and has eigenvalues +/-1.
4. A note/assert that the number of spin-orbitals in a subshell equals
   capacity(l) = 2*(2l+1).
5. __main__: build the p subshell (n arbitrary, l=1), print its 6 spin-orbitals,
   and assert the count is 6; do the same for d (l=2) expecting 10.

Comment: spin is an INDEPENDENT degree of freedom in C^2 — m_s is not derived
from m_l, and the two values exist along ANY axis (sigma_n has eigenvalues +/-1
for every direction n). Do not model spin as physical rotation.
```
**What this produces:** `spin.py` — spin-orbital generation plus the spin operators.
**How to adapt:** *Your system:* store $m_s$ as $\pm\tfrac12$ floats or as `'up'/'down'` strings consistently. *ChatGPT/Gemini:* same prompt; ask it to verify $\hat S_{\hat n}$ has eigenvalues $\pm\hbar/2$ for a random axis. *Claude Project:* keep with `subshells.py`.
**Builds on:** Chapter 6's $2\ell+1$ spatial orbitals and capacity.  **Next:** Chapter 8 couples these spins (and orbital $\ell$'s) into the total $L,S,J$ of a term symbol.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the spin-orbital promoter plus capacity tests.
**Tool:** Claude Code.
**Skill level:** Beginner–Intermediate
**Setup — confirm:**
- [ ] `subshells.py` present in `build-the-atom/`.
- [ ] `numpy`, `pytest`.
- [ ] CLAUDE.md rules from Chapters 1–6 present.
**The Task:**
```
In build-the-atom/, create spin.py with spin_orbitals(spatial),
subshell_spin_orbitals(n, l), pauli(), and Sz().

Create test_spin.py: (a) subshell_spin_orbitals for l=1 has 6 entries, for l=2
has 10, matching capacity(l) from subshells.py; (b) each spatial orbital appears
exactly twice (once per m_s); (c) each Pauli matrix squares to I and has
eigenvalues +/-1; (d) S_n = (1/2) n.sigma has eigenvalues +/-1/2 for a random
unit vector n (two values, any axis).

Run `pytest -q` and show output. Modify no other module.
```
**Expected output:** `spin.py`, `test_spin.py`, passing `pytest`.
**What to inspect:** confirm the spin-orbital count equals `capacity(l)` from Chapter 6; confirm every spatial orbital is doubled exactly once; confirm the "two values, any axis" property numerically.
**If it goes wrong:** a frequent bug is generating only $m_s=+\tfrac12$ (forgetting the down state) so capacities revert to $2\ell+1$. Recovery: assert the spin-orbital count is exactly twice the spatial count before proceeding.
**CLAUDE.md / AGENTS.md note:** add — "Spin is independent of orbital motion; $m_s\in\{+\tfrac12,-\tfrac12\}$ along any axis. Each spatial orbital becomes exactly two spin-orbitals."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the `spin.py` spin-orbital module from R3/R4.
**Validation type:** Code / Structured data
**Risk level:** Low–Medium — a missed spin doubling halves every capacity; subtle but fatal to filling.
**Setup:** use your R3/R4 artifact.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Spin & the Bloch Sphere
□ Correctness: does each spatial orbital become exactly two spin-orbitals?
□ Completeness: does the subshell spin-orbital count equal 2*(2l+1)?
□ Scope: is spin modeled as an independent C^2 label (NOT physical rotation,
  NOT derived from m_l)?
□ Physics criterion 1: does each Pauli matrix square to I with eigenvalues +/-1?
□ Physics criterion 2: does S_n have eigenvalues +/-1/2 for an arbitrary axis n?
□ Failure-mode check: any of —
  - fluent but wrong (only the +1/2 state generated)
  - m_s tied to m_l instead of independent
  - two values asserted only along z, not any axis
  - capacity reverts to 2l+1 after the "doubling"
```
**What to do with findings:** pass → use it, noting the capacity match is what made it trustworthy; one fail → add the missing spin state and re-run; multiple fails → rebuild the doubling by hand — it is a list comprehension.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* The AI promoted spatial orbitals to spin-orbitals and built the Pauli/$\hat S_z$ operators.
> *2:* The AI could not be trusted to treat spin as an independent, any-axis degree of freedom rather than a derived rotation — that conceptual call was mine.
**Physics-judgment connection:** validating the spin-orbital count against the $2(2\ell+1)$ capacity and the "two values, every axis" fact, refusing any model that ties $m_s$ to orbital motion.

---

*Chapter 8 follows: spin is the fourth quantum number. When two spin-½ particles interact — or when spin couples to orbital angular momentum — the combined system has four states, not two. The challenge is building the coupled basis from the tensor product of two Bloch spheres. The Clebsch-Gordan coefficients are the translation dictionary between the uncoupled and coupled bases.*
