# Chapter 7 — Spin and the Bloch Sphere

In 1922, Otto Stern and Walther Gerlach passed a beam of neutral silver atoms through a magnetic field whose strength varied across space, then collected the atoms on a glass plate. A field that varies in this way pushes on each atom with a force set by the part of its magnetic moment lined up with the field. If classical physics held, those moments could point any which way, and the atoms would arrive spread out into a continuous band. When Stern developed the plate, however, he did not see a band. He saw two spots.

There was no smear, no continuous distribution between them — just two separate marks.

We can read the result directly. Whatever silver atoms carry, the component of their magnetic moment measured along the field direction comes out to one of exactly two values, and the same thing happens no matter which way we orient the apparatus. The experiment leaves no room for doubt, yet it went unexplained for three years. Part of the reason is that Stern and Gerlach believed they were testing the older Bohr–Sommerfeld picture of quantized orbits. The valence electron of silver sits in an $s$ orbital, which carries no orbital angular momentum at all. The two spots therefore came from a property no one had yet proposed: the electron's intrinsic spin, suggested by Uhlenbeck and Goudsmit in 1925. Stern and Gerlach had measured the right answer before anyone knew the right question to ask.

---

## Two Values Forces Two Dimensions

We can turn the experimental result — two values, along any axis — straight into a statement about the Hilbert space. Whatever space spin occupies, it has to let every spin-component operator carry exactly two eigenvalues. The smallest complex vector space able to do that is $\mathbb{C}^2$. We are not guessing here; this is simply the least structure that "two and only two" allows.

We take the eigenstates of the $z$-component as our basis:

$$|\!\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}.$$

The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$, where $\sigma_x, \sigma_y, \sigma_z$ are the Pauli matrices:

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

These matrices have four properties, and we can confirm each one just by multiplying them out. Every one squares to the identity: $\sigma_i^2 = I$. Every one is traceless. Two different Pauli matrices anticommute: $\sigma_i\sigma_j + \sigma_j\sigma_i = 0$ for $i \neq j$. And together they obey the angular-momentum commutation relations: $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, which gives $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ — exactly the algebra that orbital angular momentum $\hat{L}$ obeys. Because the algebra matches, we are justified in calling spin a form of angular momentum.

All four properties collapse into a single multiplication rule:

$$\boxed{\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k.}$$

This one equation contains the entire Pauli algebra, and it is worth committing to memory.

---

## Why Spin Is Not Rotation

Many of us first meet spin imagining a tiny ball turning on its axis, the way a top spins. We can retire that image with a single calculation.

Suppose the electron really does carry angular momentum $\hbar/2$ by physically spinning. Give it the largest radius we can reasonably justify — the classical electron radius $r_e \approx 2.82\times10^{-15}$ m. (Experiments actually constrain the electron to be smaller than $10^{-18}$ m, and a smaller radius only makes the conclusion below more severe.) For a uniform solid sphere, $I = \frac{2}{5}m_e r_e^2$, and $L = I\omega$ gives the speed at the equator:

$$v = \omega r_e = \frac{5\hbar}{4m_e r_e} \approx \frac{5\times1.055\times10^{-34}}{4\times9.11\times10^{-31}\times2.82\times10^{-15}} \approx 5.1\times10^{10}\ \text{m/s}.$$

Light travels at $c \approx 3.0\times10^8$ m/s, so the equator would need to move at roughly $170c$. This is not a small discrepancy we might patch up; the spinning-ball picture misses by two full orders of magnitude.

So what is spin, if not rotation? It is an internal degree of freedom that transforms as a representation of $\mathrm{SU}(2)$ — the group of $2\times2$ unitary matrices with determinant 1 — when we rotate our frame. It corresponds to no motion through physical space. In 1928, Dirac showed that spin-½ emerges automatically once we demand a wave equation that is both Lorentz-covariant and first-order in time. We never insert spin by hand; it is already present the moment we impose the correct symmetries.

So when we call spin **intrinsic**, we mean three things together: its algebra is that of angular momentum, its carrier is an $\mathrm{SU}(2)$ representation, and the degree of freedom underneath corresponds to no motion in space.

---

## Spin Along Any Axis

Choose a unit vector $\hat{n} = (\sin\theta\cos\phi,\,\sin\theta\sin\phi,\,\cos\theta)$. The spin operator measured along $\hat{n}$ is

$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\hat{n}\cdot\vec{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\\sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$

This matrix has trace zero and determinant $-(\hbar/2)^2$, which forces its eigenvalues to be $\pm\hbar/2$ for any direction $\hat{n}$ we choose. The formalism reproduces precisely what the 1922 experiment showed: two values, every axis.

The $+\hbar/2$ eigenvector, normalized with the half-angle identities, is

$$|\hat{n},+\rangle = \cos\!\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\!\tfrac{\theta}{2}|\!\downarrow\rangle.$$

Every pure spin-½ state takes this form for some pair $(\theta, \phi)$. To see why, count the freedom in a normalized state: two complex components, minus one constraint from normalization, minus one unobservable global phase, leaves two real parameters. And two real parameters are exactly what we need to label points on a sphere.

---

## The Bloch Sphere

The labels $(\theta, \phi)$ send each pure spin-½ state to a point on a unit sphere, which we call the **Bloch sphere**. The north pole ($\theta = 0$) is $|\!\uparrow\rangle$; the south pole ($\theta = \pi$) is $|\!\downarrow\rangle$; the equator ($\theta = \pi/2$) holds the equal superpositions $(|\!\uparrow\rangle + e^{i\phi}|\!\downarrow\rangle)/\sqrt{2}$, with $\phi$ sweeping around it. Every point names a state, and every state names a point.

The Born rule becomes a clean geometric statement on this sphere. Suppose the state's Bloch vector points toward $(\theta_\psi, \phi_\psi)$ and the analyzer points toward $(\theta_n, \phi_n)$. Letting $\gamma$ be the angle between them,

$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n).$$

The probability of the outcome $+\hbar/2$ is then

$$\boxed{P(+) = \cos^2\!\tfrac{\gamma}{2}, \qquad P(-) = \sin^2\!\tfrac{\gamma}{2}.}$$

We can test this against three cases we already understand. When the vectors are aligned ($\gamma = 0$), $P(+) = 1$. When they are anti-aligned ($\gamma = \pi$), $P(+) = 0$. When they are perpendicular ($\gamma = \pi/2$), $P(+) = 1/2$. One formula gives all three correctly.

The half-angle $\gamma/2$ is doing essential work. At $\gamma = \pi/2$ we have $\cos^2(\pi/2) = 0$ but $\cos^2(\pi/4) = 1/2$. If we mistakenly wrote $\cos^2\gamma$ in place of $\cos^2(\gamma/2)$, we would predict zero probability at the perpendicular, which contradicts experiment.

The half-angle also carries a deeper meaning. Suppose we rotate the analyzer by $2\pi$ — one complete turn in physical space. Then $\theta$ advances to $\theta + 2\pi$, and $\cos(\theta/2)$ becomes $\cos(\theta/2 + \pi) = -\cos(\theta/2)$, so the spin state picks up an overall minus sign. Only after a full $4\pi$ rotation does the state come back to itself. This is the **spinor double cover**: spin states live in $\mathrm{SU}(2)$, which wraps around the ordinary rotation group $\mathrm{SO}(3)$ twice. A $2\pi$ rotation that returns every ordinary vector to where it started sends a spinor to its negative. Rauch et al. (1975) and Werner et al. (1975) confirmed this directly with neutron interferometry.

---

## Larmor Precession

A spin sitting in a uniform field $\vec{B} = B_0\hat{z}$ has Hamiltonian

$$\hat{H} = -\vec{\mu}\cdot\vec{B} = \frac{\gamma B_0\hbar}{2}\sigma_z,$$

where $\gamma$ is the gyromagnetic ratio: $\gamma_e/(2\pi) \approx 28.025$ GHz/T for the electron, $\gamma_p/(2\pi) \approx 42.58$ MHz/T for the proton. This Hamiltonian is already diagonal in the $\hat{S}_z$ basis, so the time-evolution operator is simply

$$\hat{U}(t) = \begin{pmatrix}e^{-i\omega_L t/2}&0\\0&e^{+i\omega_L t/2}\end{pmatrix}, \qquad \omega_L = \gamma B_0.$$

Starting from polar angle $\theta_0$ and azimuth $\phi_0 = 0$, the state evolves as

$$|\psi(t)\rangle = \cos\!\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\omega_L t}\sin\!\tfrac{\theta_0}{2}|\!\downarrow\rangle.$$

The polar angle never changes. Only the azimuth moves, advancing at the Larmor frequency: $\phi(t) = \omega_L t$. On the Bloch sphere, the state runs around a circle of constant latitude $\theta_0$, precessing about $\hat{z}$. The expectation values follow:

$$\langle\hat{S}_x\rangle = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t), \qquad \langle\hat{S}_y\rangle = \tfrac{\hbar}{2}\sin\theta_0\sin(\omega_L t), \qquad \langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos\theta_0.$$

The spin vector circles in the $xy$-plane at $\omega_L$ while its $z$-component stays fixed. We call this Larmor precession. It looks formally identical to the classical precession of a magnetic moment, with one important difference: what precesses here is the probability distribution over measurement outcomes, not a physical needle.

These numbers show up in everyday medicine. For a proton ($\gamma_p/(2\pi) = 42.58$ MHz/T):

<!-- → [TABLE: Proton Larmor frequencies at standard MRI field strengths — 0.5 T open MRI 21.3 MHz; 1.5 T clinical MRI 63.9 MHz; 3.0 T research MRI 127.7 MHz; 7.0 T ultra-high-field 298.1 MHz] -->

The relation $\omega_L = \gamma B_0$ is the equation that every MRI scanner runs on, applied to millions of patients each year.

---

## What the Sequential Experiment Is Really Saying

Let us prepare a beam of silver atoms and send it through an $\mathrm{SG}_z$ apparatus, blocking the lower output. The atoms that survive are in the state $|\!\uparrow\rangle$. Now send them through an $\mathrm{SG}_x$ apparatus. The $\hat{S}_x$ eigenstates are $|\hat{x},\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$, and since $|\!\uparrow\rangle = (|\hat{x},+\rangle + |\hat{x},-\rangle)/\sqrt{2}$, the Born rule gives $P(\hat{x},\pm) = 1/2$. Block the $|\hat{x},-\rangle$ output, leaving atoms in $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. Feed these into a second $\mathrm{SG}_z$. The result splits 50/50.

The atoms began with a definite spin-up along $\hat{z}$. After we measured $\hat{x}$ in between, they came out 50/50 along $\hat{z}$ once more.

It is tempting to say the $\mathrm{SG}_x$ device jostled the atoms and scrambled their $z$-component. That explanation is mistaken.

The operators $\hat{S}_x$ and $\hat{S}_z$ do not commute: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$. No state can be an eigenstate of both at once. Once the $\mathrm{SG}_x$ measurement selects $|\hat{x},+\rangle$, that state simply is not an eigenstate of $\hat{S}_z$ — it carries no definite $z$-component at all, rather than a definite value that the apparatus disturbed. There was nothing to scramble in the first place. The 50/50 split at the third stage is just the Born rule acting on a state that genuinely has no definite $\hat{S}_z$.

Consider the alternative, a naive hidden-variable account in which every atom carries pre-set values $(\mu_x, \mu_z)$ that the apparatuses merely read off. It would predict that selecting $\mu_z = +$ at stage one and then $\mu_x = +$ at stage two leaves $\mu_z$ untouched, so stage three should return $\mu_z = +$ with certainty. Experiment gives 50/50 instead. Pre-existing definite values for observables that do not commute simply cannot match the data, and the algebra makes that unavoidable.

---

## Worked Example — Bloch Vector and Precession

Here we prepare a spin at Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$, compute the Born-rule probability for $+\hbar/2$ along $\hat{z}$, and then place this proton in a field $B_0 = 1.5$ T to follow its precession.

**The state:**

$$|\psi\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i\pi/4}\sin(\pi/6)|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$

**Bloch vector:** $\hat{n}_\psi = (\sin\theta_0\cos\phi_0,\,\sin\theta_0\sin\phi_0,\,\cos\theta_0) = (\sqrt{6}/4,\,\sqrt{6}/4,\,1/2)$. Check: $6/16 + 6/16 + 1/4 = 1$. ✓

**Born-rule probability along $\hat{z}$:** The analyzer is at $(\theta_n, \phi_n) = (0, 0)$, so $\cos\gamma = \cos\theta_0\cdot 1 = 1/2$, giving $\gamma = \pi/3$. Then

$$P(+) = \cos^2(\pi/6) = 3/4.$$

Verify directly: $|\langle\!\uparrow|\psi\rangle|^2 = |\cos(\pi/6)|^2 = 3/4$. ✓

**Larmor precession:** For a proton at $B_0 = 1.5$ T,

$$f_L = \frac{\gamma_p}{2\pi}\cdot B_0 = 42.58\ \text{MHz/T}\times 1.5\ \text{T} = 63.87\ \text{MHz}, \qquad T_L = 15.66\ \text{ns}.$$

The time-evolved state is $|\psi(t)\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin(\pi/6)|\!\downarrow\rangle$. The polar angle holds at $\theta_0 = \pi/3$ while the azimuth advances at $\omega_L$. The probability $P(+)$ along $\hat{z}$ stays at $|\cos(\pi/6)|^2 = 3/4$ for all time, which tells us that $\langle\hat{S}_z\rangle$ is a constant of motion.

Two limiting cases are worth noting. If $\theta_0 = 0$, the state is already an eigenstate of $\hat{H}$, so the phase $e^{i\omega_L t}$ multiplies a coefficient that is zero and nothing precesses. The equatorial case $\theta_0 = \pi/2$ gives the strongest precession: $\langle\hat{S}_z\rangle = 0$ at every instant, while $\langle\hat{S}_x\rangle$ and $\langle\hat{S}_y\rangle$ swing through their full amplitude $\hbar/2$ — the Bloch vector runs around the equator at 63.87 MHz.

---

## The *g*-Factor

The Dirac equation predicts $g_e = 2$ exactly, while the measured value is $g_e \approx 2.00232$. We should not read the gap $a_e = (g_e - 2)/2 \approx 0.00116$ as a flaw in Dirac's theory. It is the leading QED radiative correction, produced by virtual photons that dress the bare electron: $a_e \approx \alpha/(2\pi)$, where $\alpha \approx 1/137$ is the fine-structure constant. QED and experiment agree out to thirteen significant figures here, which makes this one of the most precisely confirmed predictions anywhere in physics.

When we write $\hat{H} = \gamma B_0\hat{S}_z$, we should use the experimental $\gamma$, since it already contains the anomalous correction. The departure from $g = 2$ is not a mistake to be cleaned up; it is a direct view into the virtual-photon structure of QED.

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
