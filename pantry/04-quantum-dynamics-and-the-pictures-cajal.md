# CAJAL Figure Report — Chapter 4 — Quantum Dynamics: Time Evolution and the Pictures

Recommended: 5 figures, Mixed density.

---

## Figure 1 — Time-Evolution Operator: Infinitesimal Step to Finite Unitary

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a horizontal process flowchart showing the three-stage derivation of the time-evolution operator. Stage 1: a square labeled with an identity-plus-infinitesimal structure, annotated to show that probability conservation forces the coefficient operator to be Hermitian. An arrow labeled "compose N steps" leads to Stage 2: a limit notation block representing the matrix exponential, with a brief annotation showing the $N\to\infty$ composition. A second arrow labeled "differentiate with respect to t" leads to Stage 3: a differential equation block pairing the operator with a state ket. Render all three blocks as flat rectangles on a shared horizontal baseline, with two labeled arrows between them. Each block contains only geometric/symbolic placeholder shapes — no text baked into the image. Use Okabe-Ito Sky Blue for Stage 1, Bluish Green for Stage 2, and Orange for Stage 3. Arrows in neutral gray, 1pt uniform stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three sequential stages: (1) infinitesimal step U(dt) — unitarity constraint forces Hermitian generator; (2) finite operator U(t) as matrix exponential via N-step composition; (3) Schrödinger equation as derivative of U(t) acting on state. Relationship arrows: "compose N→∞ steps" (Stage 1→2), "differentiate" (Stage 2→3). Both arrows express logical derivation, not physical process.
- `[O — ORGANIZATION]` Three flat rectangular panels on a single horizontal baseline, left to right. Arrows between panels are labeled with the operation performed. No vertical stacking. Panel widths roughly equal.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette: Stage 1 = Sky Blue `#56B4E9`; Stage 2 = Bluish Green `#009E73`; Stage 3 = Orange `#E69F00`. Arrows = light gray fill with dark gray arrowhead, 1pt stroke. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: energy eigenstates/stationary states (separate concept), Heisenberg picture, interaction picture, any time-dependent Hamiltonian discussion, numerical integration schemes, wavepacket spread.

**BLOCK 3 — NEGATIVE PROMPT:**
three-stage vertical flowchart, curved arrows, energy levels, wavepacket, interference fringes, 3D elements, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Schrödinger vs. Heisenberg Picture: Parallel Structure Diagram

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two vertical columns side by side, representing the Schrödinger picture (left) and the Heisenberg picture (right). Each column has three horizontal layers: a top layer representing the state, a middle layer representing the operator, and a bottom layer representing the expectation value output. In the Schrödinger column: the top layer is highlighted as time-varying (use a gradient arrow or a "clock" icon motif — no text), the middle layer is shaded neutral gray (static). In the Heisenberg column: the top layer is shaded neutral gray (static), the middle layer is highlighted as time-varying. Both columns share an identical bottom layer rendered in Orange to show identical expectation value output. A horizontal double-headed equality symbol connects the two bottom layers. Use Sky Blue for the time-varying state layer, Bluish Green for the time-varying operator layer. Uniform 1pt strokes, flat fill, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two pictures compared: Schrödinger (state time-dependent, operator fixed) vs. Heisenberg (state fixed, operator time-dependent). Shared output: expectation value is identical in both. Unitary transformation U(t) relates the two (shown as an inferred bidirectional connection between the columns — label as inferred). Three conceptual layers per column: state, operator, expectation value.
- `[O — ORGANIZATION]` Two equal-width columns, three horizontal rows. Top row: state; middle row: operator; bottom row: expectation value. Time-varying element highlighted; static element neutral. Equality marker at the bottom row spanning both columns.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: time-varying state = Sky Blue `#56B4E9`; time-varying operator = Bluish Green `#009E73`; static = light gray; shared expectation value output = Orange `#E69F00`. Inferred connecting relation = dashed Reddish Purple `#CC79A7` arrow. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: interaction/Dirac picture (third picture, out of scope here), explicit Hamiltonian form, ladder operators, specific Hamiltonians (harmonic oscillator, free particle), Bloch sphere.

**BLOCK 3 — NEGATIVE PROMPT:**
Bloch sphere, wave function plots, energy levels, three-column layout, realistic clock images, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Rabi Oscillation: Probability vs. Time for a Two-Level System

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line chart with horizontal axis representing time (one full cycle from 0 to $2\pi/\omega_0$) and vertical axis representing probability starting at zero. Plot two smooth sinusoidal curves that sum to 1 at all times: one beginning at 1 and descending to 0 then returning (the spin-up population), and one beginning at 0 and rising to 1 then returning (the spin-down population). The two curves are mirror images crossing at 0.5 at the midpoint. Use Sky Blue for the spin-up curve and Bluish Green for the spin-down curve, both with 1.5pt stroke. Mark the half-period midpoint with a small vertical tick on the horizontal axis. Y-axis runs from 0 to 1. No grid lines. Flat vector, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Rabi oscillation for spin-1/2 in a transverse magnetic field (H = ω₀Sₓ). Two probability curves: P↑(t) = cos²(ω₀t/2), P↓(t) = sin²(ω₀t/2). Initial condition P↑(0) = 1. Curves cross at t = π/ω₀ where P = 0.5. Full period shown: 0 to 2π/ω₀. Y-axis from 0 to 1 (probability). Time axis: one labeled tick at the half-period crossing point.
- `[O — ORGANIZATION]` Single-panel line chart. Horizontal axis: time 0 to 2π/ω₀, tick at π/ω₀. Vertical axis: probability 0 to 1 with ticks at 0, 0.5, 1. Two curves on shared axes. No grid lines; use a light horizontal reference line at 0.5 (gray, 0.5pt).
- `[P — PRESENTATION]` Flat vector: P↑(t) = Sky Blue `#56B4E9`; P↓(t) = Bluish Green `#009E73`. 1.5pt curve stroke, 0.5pt axis stroke. White background. No baked text. Y-axis starts at zero.
- `[E — EXCLUSIONS]` Omit: NMR pulse sequences, Bloch sphere trajectory, energy eigenvalues, expectation value of Sz (separate from probability), free particle or harmonic oscillator.

**BLOCK 3 — NEGATIVE PROMPT:**
Bloch sphere, energy level diagram, NMR hardware, 3D trajectory, bar chart, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Heisenberg Equation vs. Hamilton's Equations: Structural Analogy

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-panel comparison layout with a vertical dividing line. Left panel: classical mechanics — show a symbolic representation of the Poisson bracket structure as a bilinear operation on two quantities (represented as labeled ellipses for position-like and momentum-like quantities) with an output arrow. Right panel: quantum mechanics — show the commutator structure as a bilinear operation on two operator boxes with an output arrow. A horizontal double-headed arrow between the panels carries a "replace {,} → [,]/(iħ)" correspondence marker (geometric, no text baked). Both panels use the same schematic layout to emphasize structural parallelism. Use Blue for quantum operators, Orange for classical quantities, and neutral gray for operation symbols. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Structural correspondence between Poisson bracket {A,H} (classical) and commutator [A_H, H]/(iħ) (quantum). Both as bilinear operations: two input objects, one output object representing rate of change. Relationship arrow between panels: Dirac quantization rule (labeled as inferred correspondence). Conservation law: if H commutes with A (quantum) / Poisson bracket vanishes (classical), the quantity is constant — shown as a null-output symbol.
- `[O — ORGANIZATION]` Two equal-width panels separated by a thin vertical rule. Each panel: two input shapes at top, a bracket/operation symbol in the middle, one output shape below. Horizontal correspondence arrow spans the vertical divider. Conservation-law null symbol (gray "×" or circle with line) shown below each panel.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: quantum operators = Blue `#0072B2`; classical quantities = Orange `#E69F00`; operations = light gray; correspondence arrow = Reddish Purple `#CC79A7` (inferred); conservation null = neutral gray. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: specific Hamiltonians, harmonic oscillator or free-particle solutions, Noether's theorem statement, interaction picture, spin precession.

**BLOCK 3 — NEGATIVE PROMPT:**
phase space portrait, energy level diagram, trajectory plots, wavefunction, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Ehrenfest's Theorem: Narrow vs. Wide Wavepacket in an Anharmonic Potential

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-panel side-by-side diagram showing a double-well potential curve (quartic shape, symmetric, with a local maximum at center and two minima symmetrically placed) in both panels. In the left panel, place a narrow Gaussian wavepacket centered at the local maximum; annotate with a single downward arrow representing the classical force direction and a matching arrow for the expectation value of force — they nearly coincide. In the right panel, show a wide wavepacket that has bifurcated: two lobes, one over each well minimum. The expectation value marker (a vertical tick) remains at the center (the original position), while the two probability lobes are displaced to the minima. Use Sky Blue for the wavepacket envelope and Blue for the potential curve. Render the expectation-value tick in Vermillion. Flat vector, white background, 1pt uniform stroke.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Ehrenfest breakdown in a quartic double-well V(x) = -ax² + bx⁴. Left panel: narrow wavepacket at center — Ehrenfest approximation valid (⟨F⟩ ≈ F(⟨x⟩)). Right panel: wide wavepacket bifurcated into two lobes over the two minima — ⟨x⟩ stays at center while the probability distribution has split. Expectation value ⟨x⟩ marked with a vertical tick in both panels. Potential curve identical in both panels.
- `[O — ORGANIZATION]` Two equal-width panels sharing the same horizontal (x) and vertical (V) axes. Potential curve rendered identically in both. Wavepackets as Gaussian-shaped shaded envelopes above the potential baseline. Bifurcated wavepacket in right panel: two symmetric lobes. Expectation-value tick mark at x=0 in both panels.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: wavepacket envelope = Sky Blue `#56B4E9`; potential curve = Blue `#0072B2`; expectation-value tick = Vermillion `#D55E00`. Potential curve: 1.5pt stroke. Wavepacket: 1pt stroke with light fill. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: harmonic oscillator (exact Ehrenfest case), free particle, tunneling dynamics, time evolution sequence, Bloch sphere, operator equations.

**BLOCK 3 — NEGATIVE PROMPT:**
Bloch sphere, energy level diagram, time-series plot, Heisenberg picture operators, 3D potential surface, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Time-evolution operator derivation flowchart:** STATIC SUFFICIENT. The three stages are a logical derivation, not a temporal or physical process. No cyclic return or causal sequence that requires motion to follow.

**Figure 2 — Schrödinger vs. Heisenberg picture parallel structure:** STATIC SUFFICIENT. The comparison is structural. A reader can scan both columns simultaneously; animation adds no causal staging.

**Figure 3 — Rabi oscillation probability curves:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages and transition mechanism is the learning target. The oscillation between spin-up and spin-down is the physical phenomenon; watching the probability transfer in real time, synchronized with the Bloch vector precessing on a sphere, makes the connection between the Schrödinger-picture state and the observable probability concrete in a way a static snapshot cannot. **Recommended video for Chapter 4.** One-line reason: animating P↑(t) and P↓(t) simultaneously with the Bloch vector precession shows the equivalence of picture and expectation value dynamically, which is the chapter's central claim.

**Figure 4 — Classical vs. quantum bracket correspondence:** STATIC SUFFICIENT. The analogy is structural, not temporal; both sides exist simultaneously and the insight is comparative.

**Figure 5 — Ehrenfest breakdown in double well:** STATIC SUFFICIENT. The two panels capture the contrast fully in a single view; the "before and after" is spatial (two panels), not temporal.
