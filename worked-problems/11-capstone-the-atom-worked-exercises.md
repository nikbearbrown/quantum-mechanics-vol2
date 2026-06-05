# Worked Exercises: Capstone — The Atom

*Chapter 11 of Quantum Mechanics — Volume 2*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The Madelung $(n+\ell)$ rule for filling order — fill increasing $n+\ell$, ties broken by lower $n$ — and the subshell capacity $2(2\ell+1)$.
- Slater's rules for the screening constant $\sigma$ and $Z_\text{eff} = Z - \sigma$, with the grouping $[1s][2s,2p][3s,3p][3d][4s,4p]\dots$ and the constants 0.35 / 0.85 / 1.00 (and 1.00 for all inner electrons of a $d$ or $f$ electron).
- Hund's three rules: maximize $S$, then maximize $L$, then $J = |L-S|$ if less-than-half-filled, $J = L+S$ if more-than-half-filled, $J = S$ if exactly half-filled — yielding the term symbol $^{2S+1}L_J$.

---

## Part A — Full Worked Example

**What this demonstrates:** the complete capstone procedure — establish the configuration by Madelung, then apply all three Hund's rules to derive the ground-state term symbol, validated against NIST.

**The problem:** Derive the ground-state term symbol of iron ($Z=26$, configuration $[\text{Ar}]\,3d^6\,4s^2$) using Hund's three rules, and verify it against the spectroscopic value.

**The solution:**

**Step 1 — Identify the active subshell.**
The Ar core and the filled $4s^2$ are spectroscopically inert (each contributes $L=0,\,S=0$). Only the six $3d$ electrons determine the term.

*Why:* Filled subshells have all $m_\ell$ and $m_s$ occupied, so their angular momenta sum to zero.
*Check:* $3d$ holds $2(2\cdot2+1)=10$ electrons; six is more than half, which will matter for Rule 3.

**Step 2 — Apply Hund's Rule 1 (maximize $S$).**
The five $3d$ orbitals have $m_\ell = +2,+1,0,-1,-2$. Place one spin-up electron in each (five electrons, parallel spins), then the sixth must pair in antiparallel:

$$S = \left(\tfrac12\right)\times5 + \left(-\tfrac12\right)\times1 = 2.$$

Multiplicity $2S+1 = 5$ (quintet).

*Why:* Maximizing $S$ forces the most antisymmetric spatial wave function, keeping electrons farthest apart — the exchange mechanism, not a spin force.
*Check:* You cannot exceed $S=2$ here: five parallel spins is the maximum before Pauli forces the sixth to pair.

**Step 3 — Apply Hund's Rule 2 (maximize $L$).**
The five spin-up electrons fill all $m_\ell$ once, contributing $M_L = 2+1+0-1-2 = 0$. To maximize $M_L$, put the sixth (spin-down) electron in the highest available orbital, $m_\ell = +2$:

$$M_L = 0 + 2 = 2 \;\Rightarrow\; L = 2 \;\;(\text{D term}).$$

*Why:* A closed half-shell of five parallel electrons contributes zero $M_L$; the extra electron sets $L$.
*Check:* $L=2$ is consistent with the D-term label; the letter sequence is S, P, D, F for $L=0,1,2,3$.

**Step 4 — Apply Hund's Rule 3 (determine $J$).**
The $3d$ subshell is more than half-filled (6 of 10), so

$$J = L + S = 2 + 2 = 4.$$

*Why:* The sign of the spin-orbit coupling $\lambda\,\vec{L}\cdot\vec{S}$ reverses past half-filling, maximizing $J$ for more-than-half-filled subshells.
*Check:* If one mistakenly used the less-than-half-filled branch $J=|L-S|=0$, the result would be $^5D_0$ — a diagnostic for the inverted-branch error.

**Step 5 — Assemble and verify the term symbol.**
With $2S+1=5$, $L=2$ (D), $J=4$:

$$\boxed{^5D_4}.$$

*Why:* The term symbol format is $^{2S+1}L_J$.
*Check:* NIST lists the iron ground level as $3d^6\,4s^2\,{}^5D_4$. Agreement. ✓

**Final answer:** Iron's ground-state term is $^5D_4$, derived through max-$S$ (quintet), max-$L$ (D), and the more-than-half-filled branch $J=L+S=4$ — exactly the configuration the 1927 spectroscopist knew before anyone could explain it.

**What made this work:** The procedure is mechanical once the active subshell is isolated. The two places to slip are Rule 1 (counting the sixth electron's spin-down contribution correctly to get $S=2$, not $S=3$) and Rule 3 (using the more-than-half-filled branch). The validation against NIST is what makes the derivation trustworthy — the term was *derived*, not recalled.

**Self-explanation prompt:** Explain in your own words why the half-filling fraction (6 of 10) determines whether $J=|L-S|$ or $J=L+S$, and what physical interaction Rule 3 is encoding.

---

## Part B — Matched Practice Problem

**What this demonstrates:** the same three-rule procedure on a less-than-half-filled subshell, where Rule 3 takes the opposite branch.

**The problem:** Derive the ground-state term symbol of carbon ($Z=6$, configuration $1s^2\,2s^2\,2p^2$) using Hund's three rules, and verify against NIST.

**Step 1 — Identify the active subshell.**
Determine which electrons are inert and which determine the term.

**Step 2 — Apply Hund's Rule 1 (maximize $S$).**
Place the two $2p$ electrons to maximize total spin and find $S$ and the multiplicity.

**Step 3 — Apply Hund's Rule 2 (maximize $L$).**
Choose the $m_\ell$ values of the two electrons to maximize $M_L$ and read off $L$.

**Step 4 — Apply Hund's Rule 3 (determine $J$).**
The $2p$ subshell holds $2(2\cdot1+1)=6$ electrons; two is less than half. Pick the correct $J$ branch.

**Step 5 — Assemble and verify the term symbol.**
Write $^{2S+1}L_J$ and check against NIST.

**Stuck?** The two $2p$ electrons go in distinct orbitals with parallel spins ($S=1$). For $L$, the highest $M_L$ uses $m_\ell=+1$ and $m_\ell=0$. The less-than-half-filled branch gives $J=|L-S|$.

*Instructor note: solution intentionally omitted. The expected answer is $^3P_0$ (triplet, P, $J=|1-1|=0$), verified against the NIST carbon ground level. Students should not confuse this with iron's $J=L+S$ branch — carbon is below half-filling.*

---

## Part C — Completion Problem

**What this demonstrates:** computing $Z_\text{eff}$ by Slater's rules, including the special handling of a $d$ electron whose inner electrons all contribute 1.00.

**The problem:** Compute $Z_\text{eff}$ for a $3d$ electron of iron ($Z=26$, configuration $[\text{Ar}]\,3d^6\,4s^2$) using Slater's rules, and compare to the Hartree-Fock benchmark.

**Step 1 — Write the Slater grouping (provided).**
Group the orbitals as $[1s^2]\,[2s^2 2p^6]\,[3s^2 3p^6]\,[3d^6]\,[4s^2]$. The electron of interest is in the $[3d]$ group.

**Step 2 — Recall the $d$-electron screening rule (provided).**
For a $d$ (or $f$) electron, each electron in the same group contributes 0.35, and *every* electron in all inner groups contributes 1.00 (not 0.85) — because the centrifugal barrier prevents $d$ electrons from penetrating to the core. Electrons in higher groups (here $4s$) contribute 0.

**Step 3 — Compute the same-group and inner-group contributions.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Sum the screening constant and form $Z_\text{eff}$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Compare to Hartree-Fock (provided).**
The Hartree-Fock value (Clementi & Roetti 1974) is approximately 6.04; Slater overestimates by about 3.5%, illustrating that Slater's rules are a semi-empirical parameterization accurate to 10–20%.

**Final answer:** Same group: $5\times0.35 = 1.75$. Inner groups: $(2+8+8)\times1.00 = 18.00$. So $\sigma = 19.75$ and $Z_\text{eff} = 26 - 19.75 = 6.25$, versus the HF value $\approx 6.04$.

**Self-explanation prompt:** Why do the inner electrons screen a $3d$ electron more effectively (1.00 each) than they would a $3s$ electron at the same $n$ (0.85 for the $n-1$ shell)? Tie your answer to orbital penetration.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student determines the ground-state configuration of chromium ($Z=24$) by filling orbitals in order of increasing principal quantum number $n$ alone.

**Their solution:**

**Step 1.** Chromium has $Z=24$, so 24 electrons to place.

**Step 2.** Start the Ar core: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6$ (18 electrons), leaving 6 to place.

**Step 3.** ⚠ Fill remaining electrons by lowest $n$ first. The $3d$ subshell has $n=3$, lower than $4s$ with $n=4$, so fill $3d$ before $4s$: place all 6 remaining electrons as $3d^6$. Configuration: $[\text{Ar}]\,3d^6$.

**Step 4.** Conclusion: chromium is $[\text{Ar}]\,3d^6$.

**Your tasks:**
1. Identify the exact step where the error occurs.
2. State the correct filling rule and apply it to get the Madelung-predicted configuration.
3. Give the actual NIST configuration of chromium and the mechanism that explains the discrepancy from Madelung.
4. State the general principle that prevents the Step 3 error.

**Why this error is common:** Students fill by $n$ alone instead of by the Madelung $(n+\ell)$ rule, which orders $4s$ ($n+\ell=4$) before $3d$ ($n+\ell=5$); chromium then needs the further exchange-stabilization correction ($[\text{Ar}]\,3d^5\,4s^1$, not the Madelung $[\text{Ar}]\,3d^4\,4s^2$), but the $n$-only error gets even the base configuration wrong.

---

## Part E — Transfer Problem

**What this demonstrates:** the same screening-and-effective-charge principle, now used to compare the binding of two different electrons in the same atom and to reason about ionization.

**The problem:** For nickel ($Z=28$, configuration $[\text{Ar}]\,3d^8\,4s^2$): (a) compute $Z_\text{eff}$ by Slater's rules for a $3d$ electron and for a $4s$ electron. (b) State which electron sees the larger effective charge and what that implies about which is more tightly bound. (c) Explain why neutral nickel fills $4s$ before $3d$ (Madelung) yet the ion Ni$^{2+}$ removes the $4s$ electrons first.

**Hint (use only if stuck after 10 minutes):** For the $3d$ electron, all inner electrons contribute 1.00 and same-group $3d$ electrons contribute 0.35. For the $4s$ electron, the $[3s,3p]$ and $3d$ count as the $n-1$/inner shells at 0.85 and below; the $4s$ companion contributes 0.35. For (c), recall that orbital energies in multi-electron atoms depend on the occupation of *every other* orbital — removing electrons changes $V_\text{eff}$ and re-orders $3d$ versus $4s$.

**Reflection prompt:**
1. Slater's rules treat $Z_\text{eff}$ as fixed for a given orbital label. Why does the Madelung-filling vs. ionization-removal paradox expose exactly this approximation as a limitation?
2. The chapter calls the $3d$/$4s$ crossing "one of the cleaner places where the approximation visibly fails." What more accurate method does it say is required, and why can't fixed-$Z_\text{eff}$ capture the crossing?

---

## Part F — Interleaved Review

**F1.** *(this chapter)* The period lengths of the periodic table are 2, 8, 8, 18, 18, 32. Using the subshell capacity $2(2\ell+1)$ and the Madelung order, state which subshells fill in period 4 and show their capacities sum to 18.
*Chapter this draws from: 11*

**F2.** *(previous chapter — Identical Particles)* Chromium's anomaly ($[\text{Ar}]\,3d^5\,4s^1$ rather than $3d^4\,4s^2$) is explained by exchange-energy stabilization. Using the parallel-spin-pair picture and the exchange integral $K>0$ from the previous chapter, explain in two sentences why a half-filled $3d$ subshell is disproportionately stabilized.
*Chapter this draws from: Identical Particles (Chapter 10)*

**F3.** *(discrimination)* You are given two tasks for iron: (i) "compute $Z_\text{eff}$ for the $3d$ electron," and (ii) "compute $Z_\text{eff}$ for the $4s$ electron." One uses 1.00 for all inner electrons; the other uses 0.85 for the $n-1$ shell. State which is which and why.
*Note to instructor: this discrimination problem checks whether the student applies the $d$/$f$ screening rule (all inner electrons 1.00) versus the $s$/$p$ rule (0.85 for the $n-1$ shell, 1.00 deeper). Watch for students who apply the $d$-electron rule to the $4s$ electron or vice versa.*

**Closing reflection:** This capstone chains together filling order (Madelung), screening ($Z_\text{eff}$), and term selection (Hund) — and then validates against data the model never fit. Write two sentences on why the iron $^5D_4$ result must be *derived* rather than recalled for the validation to mean anything.

---

## Instructor Notes

**Common errors:**
- Filling orbitals by $n$ alone instead of the Madelung $(n+\ell)$ rule (Part D's misconception), e.g. placing $3d$ before $4s$.
- Mis-applying Hund's Rule 3 by using the less-than-half-filled branch $J=|L-S|$ for a more-than-half-filled subshell, flipping iron to $^5D_0$.
- Using the bare nuclear charge $Z$ instead of the screened $Z_\text{eff}$, or applying the $s$/$p$ screening constants (0.85) to a $d$ electron.

**Signs a student needs to return:**
- Cannot explain the chromium/copper exceptions via exchange-energy stabilization and instead memorizes them as "anomalies" — indicates the mechanism is not understood.
- Produces a term symbol but cannot trace it through max-$S$, max-$L$, half-filling-$J$ — indicates the term was recalled, not derived.

**Scaffolding adjustments:** If a student struggles with Part A, have them first complete the carbon matched problem (Part B) with its opposite $J$ branch — carbon and iron bracket the half-filling rule and expose the branch logic. If a student finishes Part F quickly, have them quantify the chromium exception: count parallel-spin pairs in $3d^4\,4s^2$ vs. $3d^5\,4s^1$ and weigh the exchange gain against the $\sim0.2$ eV $3d$–$4s$ gap.

**Domain adaptation note:** The build-validate-then-name-the-failure-mode discipline — derive a multi-step prediction, diff it against data you did not fit, and attribute each residual to a named approximation — transfers to any modeling task, from climate parameterizations to financial risk models.
