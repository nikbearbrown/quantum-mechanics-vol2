# Chapter 7 — Spin and the Bloch Sphere

In February 1922, Otto Stern and Walther Gerlach fired a beam of neutral silver atoms through a magnetic field with a gradient and let them land on a glass plate. A field gradient pushes on a magnetic moment in proportion to the moment's component along the field axis. Classically a moment can point anywhere, so the atoms should fan out and leave a continuous streak. Stern developed the plate and found two spots — and only two.

Two spots. Nothing in the gap between them.

So the moment's component along the field, whatever silver atoms are up to, takes precisely two values. Turn the apparatus to point along any axis you like and you get the same verdict: two spots. The result is not subtle, and yet it went unexplained for three years — in part because Stern and Gerlach were under the impression they had confirmed the old Bohr–Sommerfeld orbital quantization. They had not. Silver's valence electron sits in an $s$ orbital, with zero orbital angular momentum, so the two spots cannot come from orbital motion at all. They come from intrinsic spin, which Uhlenbeck and Goudsmit would not propose until 1925. The right experiment arrived before anyone had thought of the right question.

---

## Two Values Forces Two Dimensions

The experimental fact does the work. Two values along any axis — that alone fixes the Hilbert space. Spin must live in a space on which every spin-component operator has exactly two eigenvalues, and the smallest complex vector space that can manage that is $\mathbb{C}^2$. Nothing is being assumed here; "two and only two" leaves no smaller option.

Take the eigenstates of the $z$-component as the basis:

$$|\!\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}.$$

The spin operators are $\hat{S}_i = (\hbar/2)\sigma_i$, where $\sigma_x, \sigma_y, \sigma_z$ are the Pauli matrices:

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Four facts, every one of which you can check by multiplying the matrices yourself. Each squares to the identity: $\sigma_i^2 = I$. Each is traceless. Distinct Pauli matrices anticommute: $\sigma_i\sigma_j + \sigma_j\sigma_i = 0$ for $i \neq j$. And they obey the angular-momentum commutation relations $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$, equivalently $[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$ — the very algebra orbital angular momentum $\hat{L}$ satisfies. Spin earns the name "angular momentum" on the strength of that algebraic coincidence, and nothing else.

The four facts collapse into a single multiplication table:

$$\boxed{\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k.}$$

Commit it to memory. There is nothing more to the Pauli algebra than this.

---

## Why Spin Is Not Rotation

Most students show up with a mental image of a little ball spinning on an axis. One number kills it.

Grant the electron angular momentum $\hbar/2$ and suppose the spinning-ball picture holds. Give it the most generous radius going — the classical electron radius $r_e \approx 2.82\times10^{-15}$ m. (Experiments push the electron's size below $10^{-18}$ m, which only makes things worse.) For a uniform solid sphere, $I = \frac{2}{5}m_e r_e^2$, and $L = I\omega$ hands you the equatorial speed:

$$v = \omega r_e = \frac{5\hbar}{4m_e r_e} \approx \frac{5\times1.055\times10^{-34}}{4\times9.11\times10^{-31}\times2.82\times10^{-15}} \approx 5.1\times10^{10}\ \text{m/s}.$$

Light travels at $c \approx 3.0\times10^8$ m/s. The required surface speed is about $170c$. This is not a picture that is off by a hair; it is off by two orders of magnitude, and it asks the electron's equator to outrun light a hundred and seventy times over.

So what is spin? It is an internal degree of freedom that transforms as a representation of $\mathrm{SU}(2)$ — the $2\times2$ unitary matrices of determinant 1 — under rotations. It is not motion through space of any kind. In 1928 Dirac showed that spin-½ drops out of nothing more than the demand that the wave equation be Lorentz-covariant and first-order in time. You never insert spin by hand; insist on the correct symmetries and it is already waiting for you.

**Intrinsic** means exactly this: the algebra is the angular-momentum algebra, the carrier is an $\mathrm{SU}(2)$ representation, and the degree of freedom underneath corresponds to no motion in space whatsoever.

---

## Spin Along Any Axis

Choose a unit vector $\hat{n} = (\sin\theta\cos\phi,\,\sin\theta\sin\phi,\,\cos\theta)$. The spin operator along $\hat{n}$ is

$$\hat{S}_{\hat{n}} = \frac{\hbar}{2}\hat{n}\cdot\vec{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi}\\\sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}.$$

This matrix is traceless with determinant $-(\hbar/2)^2$, so its eigenvalues are $\pm\hbar/2$ no matter where $\hat{n}$ points. The formalism reproduces the 1922 result on its own: two values, every axis.

The $+\hbar/2$ eigenvector, normalized with the half-angle identities, is

$$|\hat{n},+\rangle = \cos\!\tfrac{\theta}{2}|\!\uparrow\rangle + e^{i\phi}\sin\!\tfrac{\theta}{2}|\!\downarrow\rangle.$$

Every pure spin-½ state takes this form for some $(\theta, \phi)$. Count the freedom: two complex components, minus one normalization condition, minus one global phase nobody can observe, leaves two real parameters. And two real parameters are the coordinates of a sphere.

---

## The Bloch Sphere

The pair $(\theta, \phi)$ sends each pure spin-½ state to a point on the unit sphere — the **Bloch sphere**. North pole ($\theta = 0$): $|\!\uparrow\rangle$. South pole ($\theta = \pi$): $|\!\downarrow\rangle$. Equator ($\theta = \pi/2$): the equal superpositions $(|\!\uparrow\rangle + e^{i\phi}|\!\downarrow\rangle)/\sqrt{2}$, with $\phi$ running around the circle. Every point names a state; every state names a point. The correspondence is perfect.

The Born rule comes out looking geometric. Let the state's Bloch vector point at $(\theta_\psi, \phi_\psi)$ and the analyzer at $(\theta_n, \phi_n)$, and call $\gamma$ the angle between them:

$$\cos\gamma = \cos\theta_\psi\cos\theta_n + \sin\theta_\psi\sin\theta_n\cos(\phi_\psi - \phi_n).$$

Then the probability of getting $+\hbar/2$ is

$$\boxed{P(+) = \cos^2\!\tfrac{\gamma}{2}, \qquad P(-) = \sin^2\!\tfrac{\gamma}{2}.}$$

Check three cases: aligned ($\gamma = 0$) gives $P(+) = 1$; anti-aligned ($\gamma = \pi$) gives $P(+) = 0$; perpendicular ($\gamma = \pi/2$) gives $P(+) = 1/2$. Three limits, all correct, from the one formula.

The half-angle is not decoration. At $\gamma = \pi/2$, $\cos^2(\pi/2) = 0$ while $\cos^2(\pi/4) = 1/2$. Drop the half and you predict zero at the perpendicular, which is flatly wrong.

And the half-angle carries something deeper. Rotate the analyzer through $2\pi$ — one full turn in ordinary space. Then $\theta \to \theta + 2\pi$, and $\cos(\theta/2)$ becomes $\cos(\theta/2 + \pi) = -\cos(\theta/2)$. The state has picked up a minus sign. Only a $4\pi$ rotation brings it back unchanged. This is the **spinor double cover**: spin states live in $\mathrm{SU}(2)$, which wraps around the ordinary rotation group $\mathrm{SO}(3)$ twice. A $2\pi$ rotation that returns every vector in space to itself sends a spinor to its negative. It sounds like a piece of pure mathematics; it was measured directly in neutron interferometry by Rauch et al. (1975) and Werner et al. (1975).

---

## Larmor Precession

A spin in a uniform field $\vec{B} = B_0\hat{z}$ has Hamiltonian

$$\hat{H} = -\vec{\mu}\cdot\vec{B} = \frac{\gamma B_0\hbar}{2}\sigma_z,$$

where $\gamma$ is the gyromagnetic ratio: $\gamma_e/(2\pi) \approx 28.025$ GHz/T for the electron, $\gamma_p/(2\pi) \approx 42.58$ MHz/T for the proton. The Hamiltonian is already diagonal in the $\hat{S}_z$ basis, so the time-evolution operator falls right out:

$$\hat{U}(t) = \begin{pmatrix}e^{-i\omega_L t/2}&0\\0&e^{+i\omega_L t/2}\end{pmatrix}, \qquad \omega_L = \gamma B_0.$$

Start at polar angle $\theta_0$ with azimuth $\phi_0 = 0$:

$$|\psi(t)\rangle = \cos\!\tfrac{\theta_0}{2}|\!\uparrow\rangle + e^{i\omega_L t}\sin\!\tfrac{\theta_0}{2}|\!\downarrow\rangle.$$

The polar angle never moves. The azimuth winds forward at the Larmor frequency, $\phi(t) = \omega_L t$. On the Bloch sphere the state circles a fixed latitude $\theta_0$, precessing about $\hat{z}$. The expectation values are

$$\langle\hat{S}_x\rangle = \tfrac{\hbar}{2}\sin\theta_0\cos(\omega_L t), \qquad \langle\hat{S}_y\rangle = \tfrac{\hbar}{2}\sin\theta_0\sin(\omega_L t), \qquad \langle\hat{S}_z\rangle = \tfrac{\hbar}{2}\cos\theta_0.$$

The spin vector swings around in the $xy$-plane at $\omega_L$ while its $z$-component sits unchanged. That is Larmor precession. Formally it is identical to a classical magnetic moment precessing — but what precesses here is the probability distribution over measurement outcomes, not a physical needle.

The numbers are anything but abstract. For a proton ($\gamma_p/(2\pi) = 42.58$ MHz/T):

<!-- → [TABLE: Proton Larmor frequencies at standard MRI field strengths — 0.5 T open MRI 21.3 MHz; 1.5 T clinical MRI 63.9 MHz; 3.0 T research MRI 127.7 MHz; 7.0 T ultra-high-field 298.1 MHz] -->

The formula $\omega_L = \gamma B_0$ is the equation an MRI scanner runs on, applied to millions of patients a year.

---

## What the Sequential Experiment Is Really Saying

Take a beam of silver atoms through an $\mathrm{SG}_z$ apparatus and block the lower output. What survives is $|\!\uparrow\rangle$. Now send that through an $\mathrm{SG}_x$ apparatus. The $\hat{S}_x$ eigenstates are $|\hat{x},\pm\rangle = (|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt{2}$, and since $|\!\uparrow\rangle = (|\hat{x},+\rangle + |\hat{x},-\rangle)/\sqrt{2}$, the Born rule gives $P(\hat{x},\pm) = 1/2$. Block $|\hat{x},-\rangle$; what survives is $|\hat{x},+\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$. Feed that into a second $\mathrm{SG}_z$. The result: 50/50.

The atoms started out definitely up along $\hat{z}$. One $\hat{x}$ measurement later, they are back to 50/50 along $\hat{z}$.

The natural story is that the $\mathrm{SG}_x$ device jostled the atoms and scrambled their $z$-component. The natural story is wrong.

$\hat{S}_x$ and $\hat{S}_z$ do not commute: $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y \neq 0$. No state is an eigenstate of both at once. Once the $\mathrm{SG}_x$ measurement leaves you holding $|\hat{x},+\rangle$, that state simply is not a $\hat{S}_z$ eigenstate — it has no definite $z$-component to begin with, so there was nothing for the apparatus to disturb. The 50/50 at stage three is the Born rule acting on a state that genuinely possesses no definite $\hat{S}_z$.

A naive hidden-variable picture — each atom secretly carrying values $(\mu_x, \mu_z)$ that the apparatuses merely read off — would say: select $\mu_z = +$ at stage one, then $\mu_x = +$ at stage two, and $\mu_z$ is left untouched, so stage three should give $\mu_z = +$ with certainty. Experiment says 50/50. Pre-existing definite values for non-commuting observables are ruled out by the data. The algebra forces the verdict; there is no wiggle room.

---

## Worked Example — Bloch Vector and Precession

A spin is prepared at Bloch angles $\theta_0 = \pi/3$, $\phi_0 = \pi/4$. We want the Born-rule probability for $+\hbar/2$ along $\hat{z}$, and then, treating this as a proton in $B_0 = 1.5$ T, we follow the precession.

**The state:**

$$|\psi\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i\pi/4}\sin(\pi/6)|\!\downarrow\rangle = \frac{\sqrt{3}}{2}|\!\uparrow\rangle + \frac{e^{i\pi/4}}{2}|\!\downarrow\rangle.$$

**Bloch vector:** $\hat{n}_\psi = (\sin\theta_0\cos\phi_0,\,\sin\theta_0\sin\phi_0,\,\cos\theta_0) = (\sqrt{6}/4,\,\sqrt{6}/4,\,1/2)$. Check: $6/16 + 6/16 + 1/4 = 1$. ✓

**Born-rule probability along $\hat{z}$:** The analyzer sits at $(\theta_n, \phi_n) = (0, 0)$, so $\cos\gamma = \cos\theta_0\cdot 1 = 1/2$ and $\gamma = \pi/3$. Then

$$P(+) = \cos^2(\pi/6) = 3/4.$$

Or read it off directly: $|\langle\!\uparrow|\psi\rangle|^2 = |\cos(\pi/6)|^2 = 3/4$. ✓

**Larmor precession:** For a proton at $B_0 = 1.5$ T,

$$f_L = \frac{\gamma_p}{2\pi}\cdot B_0 = 42.58\ \text{MHz/T}\times 1.5\ \text{T} = 63.87\ \text{MHz}, \qquad T_L = 15.66\ \text{ns}.$$

The state evolves to $|\psi(t)\rangle = \cos(\pi/6)|\!\uparrow\rangle + e^{i(\pi/4 + \omega_L t)}\sin(\pi/6)|\!\downarrow\rangle$. The polar angle holds at $\theta_0 = \pi/3$; only the azimuth advances. So $P(+)$ along $\hat{z}$ stays pinned at $|\cos(\pi/6)|^2 = 3/4$ for all time — $\langle\hat{S}_z\rangle$ is a constant of the motion.

Two limits are worth noting. If $\theta_0 = 0$ the state is already an energy eigenstate; the phase $e^{i\omega_L t}$ multiplies a zero coefficient and nothing precesses. The equatorial case $\theta_0 = \pi/2$ is the other extreme: $\langle\hat{S}_z\rangle = 0$ throughout, while $\langle\hat{S}_x\rangle$ and $\langle\hat{S}_y\rangle$ swing at full amplitude $\hbar/2$, and the Bloch vector races around the equator at 63.87 MHz.

---

## The *g*-Factor

The Dirac equation says $g_e = 2$, exactly. Measurement says $g_e \approx 2.00232$. The discrepancy $a_e = (g_e - 2)/2 \approx 0.00116$ is not Dirac failing. It is the leading QED radiative correction — virtual photons dressing the bare electron — and to lowest order $a_e \approx \alpha/(2\pi)$, with $\alpha \approx 1/137$ the fine-structure constant. QED and experiment agree to thirteen significant figures, which makes this one of the most stringently tested predictions anyone has ever made.

When you write $\hat{H} = \gamma B_0\hat{S}_z$, use the experimental $\gamma$; it already carries the anomalous correction. The departure from $g = 2$ is a window onto the virtual-photon structure of QED, not a blemish to be sanded off.

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
