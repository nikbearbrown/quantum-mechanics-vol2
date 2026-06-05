# Worked Exercises: The Hydrogen Atom

*Chapter 9 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The radial wave function $R_{n\ell}(r)$ and the radial probability density $P(r) = r^2|R_{n\ell}(r)|^2$, where the $r^2$ factor comes from the spherical volume element $4\pi r^2\,dr$.
- The three quantum-number constraints — $n\geq 1$, $\ell\leq n-1$, $|m|\leq\ell$ — and the counting identity $\sum_{\ell=0}^{n-1}(2\ell+1)=n^2$.
- The energy spectrum $E_n = -13.6\,\text{eV}/n^2$ and the Bohr radius $a_0 = 4\pi\epsilon_0\hbar^2/(\mu e^2) \approx 0.529\,\text{Å}$.

---

## Part A — Full Worked Example

**What this demonstrates:** that the "size" of the 1s orbital depends on which question you ask — the most-probable radius $r_\text{mp}$ and the mean radius $\langle r\rangle$ are different numbers because the radial probability density $P(r)$ is right-skewed.

**The problem:** For the hydrogen ground state $\psi_{100}(r) = (\pi a_0^3)^{-1/2}e^{-r/a_0}$, compute both the most-probable radius $r_\text{mp}$ and the mean radius $\langle r\rangle$, and explain why they differ.

**The solution:**

**Step 1 — Build the radial probability density (apply the Jacobian).**
The radial wave function is $R_{10}(r) = 2a_0^{-3/2}e^{-r/a_0}$. The probability of finding the electron in the shell between $r$ and $r+dr$ is

$$P(r) = r^2|R_{10}(r)|^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

*Why:* The quantity you want is not the point density $|\psi_{100}|^2$ but the probability integrated over all angles in a thin shell; the shell volume is $4\pi r^2\,dr$, so the $r^2$ is compulsory.
*Check:* $P(0)=0$ even though $|\psi_{100}(0)|^2\neq 0$ — the shell at the origin has vanishing volume.

**Step 2 — Find the most-probable radius (maximize $P$).**
Differentiate and set to zero:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0.$$

Factor out $2r\,e^{-2r/a_0}$: the surviving root is $1 - r/a_0 = 0$, so

$$r_\text{mp} = a_0.$$

*Why:* The peak of the shell distribution is where adding more shell volume stops outpacing the exponential decay of $|R|^2$.
*Check:* $r=0$ is the other root but it is a minimum ($P=0$ there), so $r_\text{mp}=a_0$ is the genuine maximum.

**Step 3 — Find the mean radius (integrate $r\,P(r)$).**

$$\langle r\rangle = \int_0^\infty r\,P(r)\,dr = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr.$$

Using $\int_0^\infty r^n e^{-r/b}\,dr = n!\,b^{n+1}$ with $b = a_0/2$ and $n=3$:

$$\langle r\rangle = \frac{4}{a_0^3}\cdot 3!\left(\frac{a_0}{2}\right)^4 = \frac{4}{a_0^3}\cdot\frac{6\,a_0^4}{16} = \frac{3}{2}a_0.$$

*Why:* The mean weights every radius by its probability, so the long tail at large $r$ contributes.
*Check:* The general formula $\langle r\rangle_{n\ell} = (a_0/2)[3n^2-\ell(\ell+1)]$ at $(1,0)$ gives $(a_0/2)(3) = \tfrac32 a_0$. Agreement.

**Step 4 — Interpret the gap geometrically.**
$r_\text{mp} = a_0$ and $\langle r\rangle = \tfrac32 a_0$. The mean lies to the right of the peak because $P(r)$ has a long right tail at large $r$ that pulls the average outward.

*Why:* A classical electron on a fixed circular orbit would give $r_\text{mp} = \langle r\rangle = r_0$ — one radius. The split is the fingerprint of a probability distribution rather than a path.
*Check:* The electron is found beyond $a_0$ on more than half of all measurements, consistent with the mean exceeding the peak.

**Final answer:** $r_\text{mp} = a_0$ and $\langle r\rangle = \tfrac{3}{2}a_0$. They differ because $P(r)$ is right-skewed; this is the geometric signature of wave mechanics, not a numerical accident.

**What made this work:** The entire calculation hinged on keeping the $r^2$ Jacobian. Once $P(r) = r^2|R_{10}|^2$ is written correctly, the most-probable radius comes from a derivative and the mean comes from an integral against the standard gamma-function formula. Bohr's $a_0$ reappears as the *peak* of the distribution — the agreement on $r_\text{mp}$ is the numerical coincidence, and the disagreement on $\langle r\rangle$ is the physics Bohr's model could not express.

**Self-explanation prompt:** In your own words, why does $P(0)=0$ even though $|\psi_{100}(0)|^2$ is the largest point density anywhere in the atom?

---

## Part B — Matched Practice Problem

**What this demonstrates:** that the $r_\text{mp}\neq\langle r\rangle$ split is not special to the ground state — it persists in excited states with a node.

**The problem:** For the 2s state, $R_{20}(r) = (8a_0^3)^{-1/2}(2 - r/a_0)e^{-r/(2a_0)}$, compute the most-probable radius (the larger maximum of $P(r)$) and the mean radius $\langle r\rangle_{2s}$. Determine whether they still differ.

**Step 1 — Build the radial probability density (apply the Jacobian).**
Write $P(r) = r^2|R_{20}(r)|^2$, keeping every factor.

**Step 2 — Locate the radial node.**
Find where $R_{20}(r)=0$ to understand the structure of $P(r)$ before maximizing.

**Step 3 — Find the most-probable radius (maximize $P$).**
Differentiate $P(r)$, set to zero, and identify the outer maximum (the dominant peak).

**Step 4 — Find the mean radius (integrate $r\,P(r)$).**
Use $\int_0^\infty r^n e^{-r/b}\,dr = n!\,b^{n+1}$ term by term after expanding $(2-r/a_0)^2$.

**Step 5 — Interpret the gap.**
Compare $r_\text{mp}$ and $\langle r\rangle_{2s}$; check $\langle r\rangle$ against the general formula $\langle r\rangle_{n\ell} = (a_0/2)[3n^2-\ell(\ell+1)]$ at $(2,0)$.

**Stuck?** The expansion $(2-r/a_0)^2 = 4 - 4r/a_0 + r^2/a_0^2$ turns the mean-radius integral into a sum of three standard gamma integrals with $b = a_0$.

*Instructor note: solution intentionally omitted. The expected mean is $\langle r\rangle_{2s} = 6a_0$, and the node sits at $r = 2a_0$ — students should arrive at these themselves.*

---

## Part C — Completion Problem

**What this demonstrates:** counting the complete set of allowed states for a shell and confirming the $n^2$ (orbital) and $2n^2$ (with spin) degeneracy.

**The problem:** List all allowed $(n,\ell,m)$ combinations for $n=3$ and verify the orbital and spin-included state counts.

**Step 1 — Apply the constraint on $\ell$ (provided).**
With $n=3$, the rule $\ell\leq n-1$ allows $\ell = 0, 1, 2$. A Laguerre polynomial of degree $n-\ell-1$ cannot have negative degree, which is the origin of this bound.

**Step 2 — Apply the constraint on $m$ (provided).**
For each $\ell$, the rule $|m|\leq\ell$ gives $2\ell+1$ values of $m$. This comes from the angular-momentum algebra of Chapter 6, independent of $V(r)$.

**Step 3 — Enumerate the states.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Count and verify the degeneracy.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Include spin (provided).**
Each orbital state carries $m_s = \pm\tfrac12$, doubling the count. The shell therefore holds $2n^2$ states.

**Final answer:** The $n=3$ shell has $\sum_{\ell=0}^{2}(2\ell+1) = 1+3+5 = 9 = n^2$ orbital states and $2n^2 = 18$ states including spin.

**Self-explanation prompt:** Each of the three constraints ($n\geq1$, $\ell\leq n-1$, $|m|\leq\ell$) comes from a different mathematical source. Name the source of each in one sentence.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes "where the electron is" for the 1s state by maximizing the point density instead of the shell probability.

**Their solution:**

**Step 1.** Ground state: $\psi_{100}(r) = (\pi a_0^3)^{-1/2}e^{-r/a_0}$, so $|\psi_{100}(r)|^2 = (\pi a_0^3)^{-1}e^{-2r/a_0}$.

**Step 2.** The most-probable location is where the probability density is largest.

**Step 3.** ⚠ Maximize $|\psi_{100}(r)|^2 = (\pi a_0^3)^{-1}e^{-2r/a_0}$. Since $e^{-2r/a_0}$ decreases monotonically, the maximum is at $r = 0$. Therefore the electron is most likely found at the nucleus, $r_\text{mp} = 0$.

**Step 4.** Conclusion: the 1s electron is most probably right at the proton.

**Your tasks:**
1. Identify the exact step where the error occurs.
2. Explain why it is wrong in terms of the physical quantity being maximized.
3. Give the corrected calculation and the correct $r_\text{mp}$.
4. State the general rule that prevents this error.

**Why this error is common:** Students conflate the point density $|\psi|^2$ with the radial probability density $P(r) = r^2|R(r)|^2$, forgetting that the $r^2$ Jacobian from the shell volume $4\pi r^2\,dr$ is mandatory — it is called out in the chapter as the single most common error in hydrogen-atom calculations.

---

## Part E — Transfer Problem

**What this demonstrates:** the same principle — energy differences set photon wavelengths, but only allowed transitions occur — applied to spectral series and selection rules rather than to radial averages.

**The problem:** Consider the hydrogen transitions feeding the Balmer series. (a) Compute the wavelength of the Balmer $\alpha$ line ($n=3\to n=2$) using $E_n = -13.6\,\text{eV}/n^2$ and $hc = 1240\,\text{eV·nm}$. (b) For the candidate decay $3p\to 2s$, state whether it is electric-dipole allowed using $\Delta\ell = \pm1$. (c) For the candidate $2s\to 1s$, state whether it is allowed, and if not, name the process by which the 2s state still decays.

**Hint (use only if stuck after 10 minutes):** The wavelength comes from $\lambda = hc/\Delta E$ with $\Delta E = 13.6\,(1/4 - 1/9)\,\text{eV}$. For selection rules, only $\Delta\ell$ matters for the allowed/forbidden verdict; $\Delta\ell = 0$ is forbidden at electric-dipole order.

**Reflection prompt:**
1. Why does a photon carrying angular momentum 1 force the rule $\Delta\ell = \pm1$ rather than $\Delta\ell = 0,\pm1$?
2. The $2s\to1s$ transition has a lifetime of $\approx 0.12$ s — eight orders of magnitude slower than allowed transitions. Why does this metastability make 2s useful for precision spectroscopy?

---

## Part F — Interleaved Review

**F1.** *(this chapter)* The general mean-radius formula is $\langle r\rangle_{n\ell} = (a_0/2)[3n^2-\ell(\ell+1)]$. Compute $\langle r\rangle$ for the $(2,1)$ and $(2,0)$ states. At fixed $n$, does increasing $\ell$ move the mean radius inward or outward? Explain using the centrifugal-barrier picture.
*Chapter this draws from: 9*

**F2.** *(previous chapter — Spin and Angular Momentum)* The hydrogen wave function $\psi_{n\ell m}$ carries an orbital quantum number $m$ with $|m|\leq\ell$, but the full state of an electron also carries spin $m_s = \pm\tfrac12$. Explain why the shell capacity is $2n^2$ rather than $n^2$, and which chapter supplied the factor of 2.
*Chapter this draws from: Spin and Angular Momentum (Chapter 8)*

**F3.** *(discrimination)* You are given two tasks: (i) "Find the most-probable radius of the 3d state," and (ii) "Find the probability density at the origin for the 3d state." One requires the $r^2$ Jacobian and one does not. State which is which and why.
*Note to instructor: this discrimination problem checks whether the student can tell when $P(r) = r^2|R|^2$ is required (questions about radius/shell probability) versus when the bare $|\psi|^2$ is the right object (questions about point density at a specific location). Watch for students who reflexively apply $r^2$ to everything.*

**Closing reflection:** Across this chapter, the recurring move is asking *which* quantity answers the question — point density or shell probability, energy or wavelength, allowed or forbidden. Write two sentences on how keeping the $r^2$ Jacobian and the $\Delta\ell=\pm1$ rule straight prevents the two most common hydrogen errors.

---

## Instructor Notes

**Common errors:**
- Dropping the $r^2$ Jacobian and reporting $r_\text{mp}=0$ for the 1s state (Part D's misconception).
- Allowing $\ell\geq n$ or $|m|>\ell$ when enumerating states, which inflates the degeneracy count above $n^2$.
- Writing the energy with the wrong sign or power, e.g. $+13.6\,n^2$ eV instead of $-13.6/n^2$ eV.

**Signs a student needs to return:**
- Cannot explain why $P(0)=0$ while $|\psi_{100}(0)|^2\neq 0$ — indicates the shell-volume idea has not landed.
- Computes a Balmer wavelength but cannot say why $2s\to1s$ is forbidden — indicates selection rules are being memorized, not understood.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify normalization $\int_0^\infty P(r)\,dr = 1$ using the gamma-function formula — this rehearses the Jacobian and the integral technique before the maximization. If a student finishes Part F quickly, have them derive the $2s$ result of Part B in full and confirm $\langle r\rangle_{2s} = 6a_0$ against the general formula.

**Domain adaptation note:** The same peak-vs-mean split appears whenever a probability distribution is skewed — in finance (most-likely vs. expected return) or reliability engineering (mode vs. mean time-to-failure) — so the geometric lesson transfers beyond quantum mechanics.
