# Worked Exercises: Identical Particles

*Chapter 10 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The exchange operator $\hat{P}_{12}\psi(\vec{r}_1,\vec{r}_2)=\psi(\vec{r}_2,\vec{r}_1)$, with $\hat{P}_{12}^2=\mathbb{1}$ and eigenvalues $\pm1$: bosons are symmetric ($+1$), fermions are antisymmetric ($-1$).
- The Slater determinant as the antisymmetric $N$-fermion state, and Pauli exclusion as the theorem that a determinant with two identical columns is identically zero.
- The split of two-spin states into the antisymmetric singlet ($S=0$) and symmetric triplet ($S=1$), and the rule total antisymmetric = symmetric spatial × antisymmetric spin, or antisymmetric spatial × symmetric spin.

---

## Part A — Full Worked Example

**What this demonstrates:** how to build the correct antisymmetric two-electron state for the helium $1s2s$ excited configuration, and how the exchange integral $K$ splits parahelium from orthohelium.

**The problem:** For helium in the $1s2s$ configuration, construct the two physically allowed antisymmetric states (parahelium and orthohelium), and use first-order perturbation theory on $V_{12} = e^2/(4\pi\epsilon_0|\vec{r}_1-\vec{r}_2|)$ to show that orthohelium lies below parahelium. Identify the sign and physical meaning of the exchange integral $K$.

**The solution:**

**Step 1 — Antisymmetrize the two-particle state.**
The total wave function must satisfy $\hat{P}_{12}\psi = -\psi$. Pairing each spatial symmetry with the compatible spin state:

$$\psi_\pm = \frac{1}{\sqrt{2}}\bigl[\phi_{1s}(\vec{r}_1)\phi_{2s}(\vec{r}_2) \pm \phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\bigr]\times\begin{cases}\chi_\text{singlet} & (+)\\\chi_\text{triplet} & (-)\end{cases}.$$

*Why:* A symmetric spatial part ($+$) must multiply the antisymmetric singlet; an antisymmetric spatial part ($-$) must multiply the symmetric triplet. Either pairing makes the total antisymmetric.
*Check:* Apply $\hat{P}_{12}$ to $\psi_+$: the spatial part is unchanged, the singlet flips sign, total $\to -\psi_+$. Antisymmetric. ✓

**Step 2 — Name the two states.**
The $(+)$ state is **parahelium** (symmetric spatial × singlet, $S=0$); the $(-)$ state is **orthohelium** (antisymmetric spatial × triplet, $S=1$). Both are physical.

*Why:* These are exactly the two spectral families spectroscopists catalogued in the 1920s — one element, two families, from the antisymmetry requirement alone.
*Check:* The $1s^2$ ground state has only the symmetric spatial part $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)$, so it must be the singlet — there is no $1s^2$ orthohelium, consistent with Pauli.

**Step 3 — Apply first-order perturbation theory.**
The first-order Coulomb correction is $\langle\psi_\pm|V_{12}|\psi_\pm\rangle = J \pm K$, where

$$J = \iint |\phi_{1s}(\vec{r}_1)|^2\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}|\phi_{2s}(\vec{r}_2)|^2\,d^3r_1\,d^3r_2$$

is the **direct integral** (classical Coulomb energy between the two charge clouds), and

$$K = \iint \phi_{1s}^*(\vec{r}_1)\phi_{2s}^*(\vec{r}_2)\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}\phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\,d^3r_1\,d^3r_2$$

is the **exchange integral** — the cross-term from antisymmetrization.

*Why:* The $\pm$ in front of $K$ comes directly from the $\pm$ in $\psi_\pm$; squaring the antisymmetrized state produces a direct term and a sign-carrying cross term.
*Check:* $J$ has a classical interpretation; $K$ has none — it swaps which electron is "in 1s" and which is "in 2s," a purely quantum object.

**Step 4 — Determine the sign of $K$ and order the levels.**
For real orbitals and the positive Coulomb kernel $1/r_{12}>0$, the integrand of $K$ is non-negative everywhere, so $K>0$. Then:

$$E_\text{para} = E^{(0)} + J + K, \qquad E_\text{ortho} = E^{(0)} + J - K.$$

Orthohelium lies lower by $2K \approx 0.80$ eV.

*Why:* The triplet ($S=1$) requires the antisymmetric spatial $\psi_-$, which vanishes at $\vec{r}_1=\vec{r}_2$; the electrons stay farther apart, lowering Coulomb repulsion.
*Check:* The splitting is large and observable, matching the experimental separation of the ortho/para $1s2s$ levels.

**Final answer:** Parahelium $1s2s$ sits at $E^{(0)}+J+K$; orthohelium at $E^{(0)}+J-K$. Since $K>0$, orthohelium is lower by $2K\approx0.80$ eV. The mechanism is geometric, not a spin force: spin fixes the required spatial symmetry, which fixes how close the electrons approach, which fixes the Coulomb energy.

**What made this work:** The chain runs spin → required spatial symmetry → electron separation → Coulomb energy, with no spin-dependent term anywhere in the Hamiltonian. The exchange integral $K$ is the bookkeeping device that captures the energy cost of the antisymmetrization cross-term. Recognizing $K>0$ from the positivity of the integrand is what fixes the sign of the splitting.

**Self-explanation prompt:** No term in the helium Hamiltonian depends on spin. Explain in two sentences how spin nonetheless ends up determining the energy ordering of orthohelium versus parahelium.

---

## Part B — Matched Practice Problem

**What this demonstrates:** the same antisymmetrization-and-exchange machinery applied to a different excited configuration, the $1s2p$ states of helium.

**The problem:** For helium in the $1s2p$ configuration, construct the parahelium and orthohelium states, write the direct integral $J'$ and exchange integral $K'$ in terms of $\phi_{1s}$ and $\phi_{2p}$, determine the sign of $K'$, and state which family lies lower in energy.

**Step 1 — Antisymmetrize the two-particle state.**
Pair symmetric spatial with singlet and antisymmetric spatial with triplet, using $\phi_{1s}$ and $\phi_{2p}$.

**Step 2 — Name the two states.**
Identify which is parahelium and which is orthohelium, with their $S$ values.

**Step 3 — Apply first-order perturbation theory.**
Write $\langle V_{12}\rangle_\pm = J' \pm K'$ with the appropriate integrals for the $1s2p$ orbitals.

**Step 4 — Determine the sign of $K'$ and order the levels.**
Argue the sign of $K'$ from the positivity of the Coulomb kernel and conclude which family is lower.

**Step 5 — State the mechanism.**
Explain why the lower family has the electrons farther apart on average.

**Stuck?** The structure is identical to the worked $1s2s$ case — only the second orbital changes from $\phi_{2s}$ to $\phi_{2p}$. The sign argument for $K'$ is the same: a positive kernel times real orbitals gives a non-negative integrand.

*Instructor note: solution intentionally omitted. Students should reach $K'>0$, orthohelium ($1s2p$, triplet) lower by $2K'$, with the same farther-apart mechanism — and should not assume $K' = K$ numerically since the orbitals differ.*

---

## Part C — Completion Problem

**What this demonstrates:** that attempting to place two fermions in the same spin-orbital makes the Slater determinant vanish identically — Pauli exclusion as a theorem.

**The problem:** Build the two-electron Slater determinant for the helium $1s^2$ ground state, then test what happens if both electrons are assigned the same spin-orbital.

**Step 1 — Set up the spin-orbitals (provided).**
Use $\phi_A = \psi_{100}\chi_\uparrow$ and $\phi_B = \psi_{100}\chi_\downarrow$: same spatial orbital, opposite spin.

**Step 2 — Write the Slater determinant (provided).**

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\det\begin{pmatrix}\phi_A(1) & \phi_B(1) \\ \phi_A(2) & \phi_B(2)\end{pmatrix} = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_B(2) - \phi_B(1)\phi_A(2)\bigr].$$

This factors into a symmetric spatial part $\psi_{100}(\vec{r}_1)\psi_{100}(\vec{r}_2)$ times the antisymmetric singlet spin state.

**Step 3 — Attempt to put both electrons in the same spin-orbital.**
Set $\phi_A = \phi_B = \psi_{100}\chi_\uparrow$ and write out the determinant.
*Your work here:*

*Why (your explanation):*

**Step 4 — Interpret the result.**
State what a vanishing wave function means physically and what constraint it forces on the two 1s electrons.
*Your work here:*

*Why (your explanation):*

**Step 5 — Connect to the general theorem (provided).**
A Slater determinant with two identical columns is identically zero everywhere in configuration space; a wave function that is identically zero cannot be normalized and is not a state. This is the Pauli exclusion principle, derived rather than postulated.

**Final answer:** With opposite spins the $1s^2$ state is a valid antisymmetric singlet; with identical spin-orbitals the determinant is identically zero, so two electrons in 1s must have opposite spins — by theorem, not by postulate.

**Self-explanation prompt:** Pauli stated exclusion in 1925 as an empirical rule about quantum numbers. Slater showed in 1929 it follows from determinants. In one sentence, why is the determinant form more general than the rule about $(n,\ell,m_\ell,m_s)$?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student writes a two-electron state for two electrons occupying distinct orbitals $\phi_a$ and $\phi_b$ and treats it as if antisymmetry were automatic.

**Their solution:**

**Step 1.** Two electrons, one in $\phi_a$ and one in $\phi_b$. Electron 1 goes in $\phi_a$, electron 2 goes in $\phi_b$.

**Step 2.** The state is the product $\psi(1,2) = \phi_a(1)\phi_b(2)$.

**Step 3.** ⚠ This product is a perfectly good two-electron wave function. Check exchange: $\hat{P}_{12}\psi(1,2) = \phi_a(2)\phi_b(1)$, which is just the electrons relabeled and represents the same physics, so the state is acceptable as written.

**Step 4.** Conclusion: $\psi(1,2) = \phi_a(1)\phi_b(2)$ describes the two electrons.

**Your tasks:**
1. Identify the exact step where the error occurs.
2. Explain why a simple product fails the requirement on identical fermions.
3. Write the corrected antisymmetric state and show it satisfies $\hat{P}_{12}\psi = -\psi$.
4. State the general principle being violated.

**Why this error is common:** Students treat the labels "1" and "2" as if they tracked distinguishable particles, so a product state looks adequate; but identical fermions require an antisymmetric state ($\hat{P}_{12}\psi = -\psi$), and the bare product $\phi_a(1)\phi_b(2)$ has no definite exchange symmetry at all.

---

## Part E — Transfer Problem

**What this demonstrates:** the same antisymmetry principle — now applied to multi-electron atoms via Hund's first rule, and to the boson side via exchange-driven correlation.

**The problem:** (a) Oxygen has configuration $1s^2\,2s^2\,2p^4$. Using the exchange mechanism (not a spin force), explain why the ground state has $S=1$ with two unpaired electrons, and why this makes oxygen paramagnetic. (b) Contrast the fermion case with two bosons in the same single-particle state: describe what happens to the joint probability density $|\psi(\vec{r}_1,\vec{r}_2)|^2$ on the diagonal $\vec{r}_1=\vec{r}_2$ for bosons versus fermions.

**Hint (use only if stuck after 10 minutes):** For (a), higher $S$ forces a more antisymmetric spatial wave function, which keeps the four $2p$ electrons farther apart and lowers Coulomb repulsion — this is Hund's first rule as a corollary of antisymmetry. For (b), the antisymmetric (fermion) wave function vanishes at $\vec{r}_1=\vec{r}_2$ (the Pauli node), while the symmetric (boson) wave function peaks there.

**Reflection prompt:**
1. The chapter insists there is "no term in the Hamiltonian encoding exchange statistics." If there is no force, what physically keeps fermions apart and bunches bosons together?
2. The single-particle marginal density $\int|\psi|^2\,d^3r_2$ is identical for bosons, fermions, and distinguishable particles. Why, then, can't a single-particle detector reveal the statistics?

---

## Part F — Interleaved Review

**F1.** *(this chapter)* Write the general $N\times N$ Slater determinant for $N$ fermions and explain, in one sentence each, (i) why swapping any two particles flips the sign and (ii) why duplicating any single-particle orbital gives zero. State the role of the $1/\sqrt{N!}$ prefactor.
*Chapter this draws from: 10*

**F2.** *(previous chapter — The Hydrogen Atom)* The spin-orbitals filling a Slater determinant are built from the hydrogenic orbitals $\psi_{n\ell m}$ of the previous chapter. Using the constraint $|m|\leq\ell$ and the spin label $m_s=\pm\tfrac12$, explain how many distinct spin-orbitals the $n=2$ shell supplies, and connect this to the shell capacity $2n^2$.
*Chapter this draws from: The Hydrogen Atom (Chapter 9)*

**F3.** *(discrimination)* You are given two helium states: (i) $1s^2$ ground configuration, and (ii) $1s2s$ excited configuration. For one, both ortho and para versions exist; for the other, only one does. State which is which and why, citing Pauli.
*Note to instructor: this discrimination problem checks whether the student can tell when both symmetry pairings are available (distinct orbitals, $1s2s$) versus when one is forced to vanish (identical orbitals, $1s^2$, where the antisymmetric spatial combination is zero). Watch for students who claim orthohelium $1s^2$ exists.*

**Closing reflection:** The recurring move this chapter is asking *what symmetry the total state must have* and then reading off the physical consequence — exclusion, exchange splitting, Hund's rule, bosonic bunching. Write two sentences on how the single requirement $\hat{P}_{12}\psi = \pm\psi$ generates all of these without any new force.

---

## Instructor Notes

**Common errors:**
- Writing a simple product state $\phi_a(1)\phi_b(2)$ for identical fermions instead of antisymmetrizing (Part D's misconception).
- Placing two fermions in the same spin-orbital and not recognizing the determinant vanishes (Pauli violation).
- Getting the boson/fermion symmetry backwards — symmetric for fermions or antisymmetric for bosons.

**Signs a student needs to return:**
- Explains Hund's first rule via a "spin-spin force" rather than the exchange integral and spatial antisymmetry — indicates the mechanism chain is not understood.
- Cannot say why orthohelium $1s^2$ does not exist — indicates Pauli exclusion is being applied as a quantum-number rule rather than a determinant theorem.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify the $1s^2$ case in Part C (where the antisymmetric spatial combination simply vanishes) before tackling the $1s2s$ split — the simpler case isolates the symmetry bookkeeping. If a student finishes Part F quickly, have them work the $1s2p$ matched problem (Part B) in full and argue why $K' \neq K$ numerically despite the identical sign argument.

**Domain adaptation note:** The exchange-correlation idea — particles that "avoid" or "bunch" with no force between them — recurs in condensed-matter band theory and in photon bunching/antibunching experiments, so the symmetry argument transfers far beyond atomic physics.
