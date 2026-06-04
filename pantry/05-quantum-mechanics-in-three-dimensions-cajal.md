# CAJAL Figure Report — Chapter 5 — Quantum Mechanics in Three Dimensions

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Central Potential: Separation of Variables Flow

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a top-down process flowchart with four sequential steps. Step 1: a single wide rectangle representing the full 3D Schrödinger equation in spherical coordinates — show the Laplacian split visually as two sub-regions within the box (a radial sub-region and an angular sub-region), both filled with flat color. Step 2: a product-ansatz diamond indicating the separability condition V = V(r). Step 3: two separate rectangular boxes branching downward — one labeled "angular equation" (left), one labeled "radial equation" (right) — connected to the diamond by forked arrows. An annotation between them reads "[inferred: universal vs. potential-specific]." Step 4: a bottom row showing the angular box leading to a spherical-harmonic symbol shape (circular), and the radial box leading to an effective-potential profile schematic (a curve shape). Use Sky Blue for the angular branch, Bluish Green for the radial branch, Orange for the separation constant node, and Blue for the initial 3D equation box. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Separation of variables for central potential V(r). Stages: (1) 3D TISE in spherical coordinates — Laplacian split into radial and angular parts; (2) product ansatz ψ = R(r)Y(θ,φ), conditioned on V = V(r); (3) separation constant ℓ(ℓ+1) branches into angular eigenvalue equation and radial equation; (4) angular equation produces spherical harmonics (universal); radial equation produces potential-specific solutions with effective potential. Inferred annotation: "universal" for angular output, "potential-specific" for radial.
- `[O — ORGANIZATION]` Vertical top-to-bottom flow. Single box at top (3D equation), diamond separator, two branches below (angular left, radial right), two output shapes at bottom. Separation constant shown as a circular node at the branch point.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: 3D equation = Blue `#0072B2`; separation constant node = Orange `#E69F00`; angular branch = Sky Blue `#56B4E9`; radial branch = Bluish Green `#009E73`. Arrows 1pt neutral gray, arrowheads filled. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: specific potentials (Coulomb, infinite well), spherical Bessel functions, nuclear shell model, CMB connection, radial probability density formula.

**BLOCK 3 — NEGATIVE PROMPT:**
3D orbital shapes, energy level diagram, cross-section plot, wavefunction curve, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Spherical Harmonics Gallery: First Four (ℓ = 0, 1, 2) Angular Probability Densities

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a 2×4 panel grid of polar cross-section plots (eight panels: one for ℓ=0, three for ℓ=1 with m=-1,0,+1, and four for ℓ=2 with m=0,±1,±2). Each panel shows a polar curve r(θ) = |Yₗᵐ(θ,0)|² (the angular probability density at φ=0) as a closed shape centered on a small dot representing the origin, with a faint vertical reference line for the z-axis. The ℓ=0 panel: a circle (uniform). The ℓ=1, m=0 panel: a figure-eight along the z-axis (dumbbell). The ℓ=1, m=±1 panels: torus-cross-section rings (donut cross-sections). Use Blue for ℓ=0, Sky Blue for ℓ=1, Bluish Green for ℓ=2. Each sub-panel is identical in size, flat-filled shape, white background, 1pt stroke.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width (may expand to 120mm for 4-column layout), 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Angular probability density |Yₗᵐ(θ,0)|² as a polar plot for each (ℓ,m): ℓ=0 (m=0: sphere/circle), ℓ=1 (m=0: cos²θ dumbbell; m=±1: sin²θ ring), ℓ=2 (m=0: (3cos²θ-1)² four-lobed; m=±1: sin²θcos²θ; m=±2: sin⁴θ). Each panel includes a faint z-axis reference. Axial symmetry of all panels must be visually evident — all shapes are symmetric about the vertical axis.
- `[O — ORGANIZATION]` Grid layout: row 1 = ℓ=0 (1 panel); row 2 = ℓ=1 (3 panels); row 3 = ℓ=2 (4 panels, or split m=0 and ±1 and ±2 into 3 distinct shapes). Each panel square, same scale. Vertical z-axis reference line in every panel.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: ℓ=0 panels = Blue `#0072B2`; ℓ=1 panels = Sky Blue `#56B4E9`; ℓ=2 panels = Bluish Green `#009E73`. Shape interiors: light tint of panel color at 20% opacity, full-color outline 1pt. z-axis: light gray 0.5pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: chemistry orbital labels (px, py, pz), radial factor R(r), 3D balloon renderings, nodal surface angles, Condon–Shortley phase signs, absolute normalization factors.

**BLOCK 3 — NEGATIVE PROMPT:**
3D balloon orbital, chemistry dumbbell labels, radial nodes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Physics Basis vs. Chemistry Basis for ℓ=1: What Each Diagonalizes

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-column comparison panel. Left column header zone: a circular ring shape (axially symmetric about z-axis) representing the physics eigenstates Y₁±¹ — the probability density is a torus centered on z. Right column: a dumbbell shape pointing along the horizontal axis representing the real chemistry orbital p_x — clearly broken axial symmetry about z, two lobes. Between the columns, draw a double-headed horizontal arrow connecting the two representations (inferred unitary transformation). Below each column, place a small indicator: for the left (physics) column, a highlighted checkmark-like element on the "L_z eigenvalue" row; for the right (chemistry) column, a highlighted element on the "spatial direction" row — and a crossed-circle indicator on the "L_z eigenvalue" row showing that p_x is not an L_z eigenstate (negative indicator, use Vermillion). Flat vector, Sky Blue for physics states, Orange for chemistry states, Vermillion for the "not eigenstate" indicator. 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` ℓ=1 subspace: two bases spanning the same Hilbert subspace. Physics basis {Y₁⁻¹, Y₁⁰, Y₁⁺¹}: eigenstates of L̂_z, axially symmetric |Y|², no definite spatial direction. Chemistry basis {p_x, p_y, p_z}: NOT eigenstates of L̂_z, real wave functions, definite spatial direction along Cartesian axes. Inferred relationship: unitary transformation connects the two bases. Indicator that measuring L̂_z on p_x gives ±ħ with equal probability (superposition).
- `[O — ORGANIZATION]` Two equal columns. Each column: one angular shape (torus cross-section or ring for physics; dumbbell for chemistry). Below each shape: a small "L_z diagonal?" indicator (yes/no visual cue) and a "spatial direction?" indicator (no/yes). Central connecting arrow.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: physics state shapes = Sky Blue `#56B4E9`; chemistry state shapes = Orange `#E69F00`; connecting arrow = Reddish Purple `#CC79A7` (inferred transformation); "not eigenstate" indicator = Vermillion `#D55E00`; "eigenstate" indicator = Bluish Green `#009E73`. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: ℓ=2 d-orbitals, radial wavefunctions, magnetic field, Condon–Shortley phase derivation, nuclear shell model.

**BLOCK 3 — NEGATIVE PROMPT:**
3D balloon orbitals, ℓ=2 shapes, energy level diagram, Bloch sphere, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Effective Potential and the Centrifugal Barrier

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line chart with a horizontal axis representing radial distance r (from 0 to ~5 in normalized units) and a vertical axis representing potential energy starting at zero. Plot three curves: (1) the attractive potential V(r) (e.g., a −1/r Coulomb-like curve that dips sharply below zero near the origin), shown in Blue; (2) the centrifugal barrier ħ²ℓ(ℓ+1)/(2mr²) for ℓ=1, shown in Orange, which is positive and diverges near r=0; (3) the effective potential V_eff = V(r) + barrier, shown in Bluish Green, which has a repulsive core, a minimum at some intermediate r, and approaches zero at large r. Mark the minimum of V_eff with a small filled circle in Vermillion. Draw a thin horizontal dashed line in neutral gray at the energy axis value for the ground state energy (a negative value below zero). The y-axis starts at a value below zero and extends to a positive value; include a tick at zero. No grid lines.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three curves on shared axes: V(r) = attractive potential (negative, singular at r=0); centrifugal term ħ²ℓ(ℓ+1)/(2mr²) for ℓ=1 (positive, diverges at r=0); V_eff(r) = sum (has a minimum, repulsive core for ℓ>0). Minimum of V_eff marked. A horizontal reference line at a representative negative energy value (bound state energy). Axes: r from 0 to ~5 arbitrary units; V from below zero to above zero, y-axis includes zero. The centrifugal term is kinetic energy, not potential (label as inferred in the caption).
- `[O — ORGANIZATION]` Single-panel line chart. Horizontal axis: r ≥ 0, ticks at regular intervals. Vertical axis: includes zero, ticks at zero and at a few representative values. Three curves, minimum marker, horizontal energy reference line. No grid lines except the zero line.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: V(r) = Blue `#0072B2`; centrifugal = Orange `#E69F00`; V_eff = Bluish Green `#009E73`. Minimum marker = Vermillion `#D55E00`, filled circle 3pt. Energy reference = light gray dashed 0.5pt. 1.5pt curve stroke, 0.5pt axis. White background. Y-axis starts well below zero. No baked text.
- `[E — EXCLUSIONS]` Omit: ℓ=0 case (no centrifugal term), specific potential form (generic), radial wavefunction u(r) itself, nuclear shell model, spherical Bessel functions.

**BLOCK 3 — NEGATIVE PROMPT:**
radial wavefunction overlaid, 3D potential surface, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Angular Momentum Cone: L_z vs. |L|

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a schematic diagram of an angular momentum cone for ℓ=1, m=1. Show a vertical z-axis as a straight line. Draw a cone whose apex is at the origin, opening upward, with its symmetry axis along z. The half-angle of the cone should be 45° (accurate for ℓ=1, m=1). Along the cone surface, draw a dashed circle representing the locus of possible angular momentum vectors. One representative angular momentum vector arrow (fixed length) extends from the origin to a point on the cone surface at 45° to the z-axis. A separate vertical arrow from the origin to the z-axis shows the z-projection only, shorter than the full vector, representing L_z = ħ. The full vector length represents √(ħ²·1·2) = ħ√2, visibly longer than the z-projection. Use Blue for the full vector, Sky Blue for the z-axis projection, and light gray for the cone surface. Flat vector with a 2D oblique schematic style (not 3D perspective distortion), white background, 1pt stroke.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Angular momentum cone for ℓ=1, m=1. Full magnitude √(ħ²ℓ(ℓ+1)) = ħ√2 shown as vector length. z-component L_z = ħ shown as shorter vertical projection. Cone half-angle = arccos(1/√2) = 45°. Dashed circle on cone surface shows indeterminacy of transverse components. Key structural claim: the full vector is strictly longer than its z-projection, the vector cannot align with z.
- `[O — ORGANIZATION]` Single-panel schematic. Vertical z-axis center. Cone drawn symmetrically. One representative L-vector from origin to cone surface. z-projection arrow from origin upward. Dashed equatorial circle on cone surface. Small right-angle marker between z-axis and a transverse component indicator [inferred: transverse components nonzero].
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: full L-vector = Blue `#0072B2`; z-projection = Sky Blue `#56B4E9`; cone surface = light gray at 30% opacity; dashed circle = Reddish Purple `#CC79A7` dashed; z-axis = dark gray 1pt. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: higher ℓ cases in same figure, specific spherical harmonics, Bohr model orbits, chemistry basis, full 3D coordinate frame with x and y axes labeled.

**BLOCK 3 — NEGATIVE PROMPT:**
Bohr orbit ellipse, 3D perspective distortion, coordinate grid, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales.

---

## Figure 6 — Nuclear Shell Model Level Ordering from Spherical Well

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical energy-level diagram showing the ordering of single-particle levels for a spherical infinite well. Plot horizontal line segments at increasing heights representing the levels 1s, 1p, 1d, 2s, 1f, 2p in order of their energies (proportional to the squares of the Bessel function zeros). Each level is a short horizontal bar; mark the degeneracy of each level (the number of particles the level can hold = 2(2ℓ+1)) with a series of small filled circles stacked next to the bar (or implied by bar width). Mark cumulative particle numbers at each filled shell: 2, 8, 20 with small triangular pointers or vertical tick marks on a secondary axis on the right showing cumulative count. Use Blue for s-levels, Sky Blue for p-levels, Bluish Green for d-levels, Orange for f-levels. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Energy levels of 3D infinite spherical well, ordered by Bessel-function zeros: 1s (β₁₀=π), 1p (β₁₁≈4.49), 1d (β₁₂≈5.76), 2s (β₂₀=2π), 1f (β₁₃≈6.99), 2p (β₂₁≈7.73). Degeneracy per level = 2(2ℓ+1). Cumulative counts at shell closures: 2 (after 1s), 8 (after 1p), 20 (after 1d+2s). Energy axis: vertical, unlabeled beyond relative proportionality. Level labels: by shell notation (n, ℓ label shapes only, no text baked). Magic numbers 2, 8, 20 indicated with right-side cumulative markers.
- `[O — ORGANIZATION]` Single vertical axis (energy increasing upward). Each level: horizontal bar segment, width proportional to degeneracy (or explicit dots). Secondary right-side cumulative counter at 2, 8, 20. Levels spaced proportional to actual energy ratios.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: s-levels = Blue `#0072B2`; p-levels = Sky Blue `#56B4E9`; d-levels = Bluish Green `#009E73`; f-levels = Orange `#E69F00`. Magic-number cumulative markers = Vermillion `#D55E00` small triangles. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: spin-orbit splitting (not introduced here), hydrogen atom levels, higher magic numbers 28/50/82, specific Bessel function values, the Coulomb potential.

**BLOCK 3 — NEGATIVE PROMPT:**
spin-orbit coupling arrows, Coulomb potential curve, hydrogen spectrum, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Separation of variables flowchart:** STATIC SUFFICIENT. The flowchart is a logical dependency structure; there is no temporal or causal sequence that animation would clarify.

**Figure 2 — Spherical harmonics polar gallery:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The chapter explicitly discusses the φ-phase rotation as the action of L̂_z: animating the phase e^{imφt} rotating the ℓ=1 harmonics around the z-axis — while showing that |Y|² remains axially symmetric at all times — directly demonstrates why the physics eigenstates have axial symmetry but the real (chemistry) combinations do not. **Recommended video for Chapter 5.** One-line reason: rotating the complex phase e^{imφ} in real time shows that |Y|² is φ-independent while Re(Y) is not, grounding the central claim that the probability density is axially symmetric but the wave function is not.

**Figure 3 — Physics vs. chemistry basis comparison:** STATIC SUFFICIENT. The comparison is structural; the two columns are simultaneously visible and require no temporal unfolding.

**Figure 4 — Effective potential and centrifugal barrier:** STATIC SUFFICIENT. A line chart; the spatial relationship of three curves is fully captured in one panel.

**Figure 5 — Angular momentum cone:** STATIC SUFFICIENT. The cone geometry is a spatial structure; the key insight (vector longer than z-projection) is visible in a single static diagram.

**Figure 6 — Nuclear shell model level ordering:** STATIC SUFFICIENT. An energy-level diagram; the level ordering and cumulative counts are a static hierarchy.
