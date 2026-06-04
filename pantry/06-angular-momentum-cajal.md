# CAJAL Figure Report — Chapter 6 — Angular Momentum

Recommended: 5 figures, Mechanistic density.

---

## Figure 1 — The Angular Momentum Ladder: Spectrum Derivation by Non-Negativity and Termination

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical ladder diagram for ℓ=2 with five horizontal rungs evenly spaced, representing the five m-values from m=−2 at the bottom to m=+2 at the top. Each rung is a horizontal bar. Between adjacent rungs, draw a pair of arrows: one pointing upward (raising operator L₊) in Sky Blue, one pointing downward (lowering operator L₋) in Orange. At the top rung (m=+2), show the L₊ arrow terminating in a small gray circle (annihilated — null output). At the bottom rung (m=−2), show the L₋ arrow terminating in a small gray circle. On the right side, draw a vertical bracket spanning all rungs with a fixed L² label region (indicating L² is constant throughout the subspace). On the left side, place five small markers — one per rung — representing the L_z eigenvalue, increasing uniformly from bottom to top. Flat vector, Blue for the ladder bars, Sky Blue for L₊ arrows, Orange for L₋ arrows, gray for null termination markers. 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Ladder diagram for ℓ=2: five states |2,m⟩ for m=−2,−1,0,+1,+2. Raising operator L₊ steps m up by 1, unchanged L². Lowering operator L₋ steps m down by 1, unchanged L². Termination: L₊|2,2⟩=0 (top rung, null); L₋|2,−2⟩=0 (bottom rung, null). L² eigenvalue constant across all rungs [inferred: shown as bracket]. L_z eigenvalue varies uniformly (m=−2 to m=+2).
- `[O — ORGANIZATION]` Vertical ladder, five rungs equally spaced. Rung bars horizontal. L₊ arrows between adjacent rungs pointing upward; L₋ arrows between adjacent rungs pointing downward — offset slightly so both are visible simultaneously. Top null termination at top rung. Bottom null termination at bottom rung. Right-side bracket: constant L². Left-side dots: varying L_z.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: rung bars = Blue `#0072B2`; L₊ arrows = Sky Blue `#56B4E9`; L₋ arrows = Orange `#E69F00`; null termination = light gray circles; L² bracket = Bluish Green `#009E73`; L_z markers = light gray dots. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: matrix representations (separate figure), spherical harmonics shapes, coordinate-space forms of L₊/L₋, coupling of two angular momenta, Clebsch-Gordan coefficients.

**BLOCK 3 — NEGATIVE PROMPT:**
matrix grid, spherical harmonic shapes, coordinate axes, 3D cone, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Spectrum Derivation: Non-Negativity Bound and Termination Conditions

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a four-step vertical flowchart. Step 1 (top): a rectangle representing the non-negativity condition — ⟨L_x² + L_y²⟩ ≥ 0 — shown as a shaded box with a "≥ 0" inequality symbol rendered geometrically (an angle bracket or comparison shape). An arrow leads to Step 2: a bounded-range indicator — a horizontal double-ended segment with stops at left and right, indicating m is bounded above and below for fixed L² eigenvalue. Arrow to Step 3: a termination box — a rung shape with a null output arrow (L₊ at the top = 0), leading to an algebraic output shape showing ℏ²ℓ(ℓ+1) as the L² eigenvalue (represented by a filled square with "ℓ(ℓ+1)" shape indicator, no text). Arrow to Step 4: a quantization result box — the allowed m-values shown as equally spaced dots in the range [−ℓ, ℓ] with a "2ℓ steps = integer" indicator (a bracket over the range). Use Blue for the non-negativity step, Orange for the bound step, Sky Blue for the termination step, Bluish Green for the result step. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Four-stage logical derivation: (1) non-negativity of ⟨L_x²+L_y²⟩ → m² ≤ λ/ħ² (bound on m); (2) bounded m → there exists m_max and m_min; (3) termination condition L₊|ℓ,ℓ⟩=0 → λ = ħ²ℓ(ℓ+1); (4) integer constraint: 2ℓ steps from m_min to m_max must be a non-negative integer → ℓ = 0, 1/2, 1, 3/2, ... All relationships are logical derivation (→ arrows), not physical process.
- `[O — ORGANIZATION]` Four rectangular panels stacked vertically with downward derivation arrows between them. Each panel same width. Arrow labels are geometric shapes (not text). Non-negativity symbol in panel 1: an angle bracket or ≥-shape. Bound in panel 2: bounded segment with end-stops. Termination in panel 3: a rung-null combination. Integer result in panel 4: a row of equally spaced dots.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: panel 1 = Blue `#0072B2`; panel 2 = Orange `#E69F00`; panel 3 = Sky Blue `#56B4E9`; panel 4 = Bluish Green `#009E73`. Derivation arrows = neutral gray 1pt. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: explicit commutator calculations, coordinate-space form, position-space wave function restriction to integers (separate from algebraic result), matrix representation.

**BLOCK 3 — NEGATIVE PROMPT:**
matrix grids, wave function plots, polar diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Integer vs. Half-Integer ℓ: Single-Valuedness Constraint

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-column comparison diagram. Left column: a circle (the unit sphere, representing orbital angular momentum in position space). Around the circle, draw a wavefunction-like oscillating curve that completes exactly an integer number of cycles as φ goes from 0 to 2π — showing that single-valuedness is satisfied. The circle represents the azimuthal single-valuedness constraint. Right column: an abstract rectangular box (representing the abstract Hilbert space of spin — no position-space analog). Show two dots inside connected by a vertical arrow, representing two spin states (up/down), with no circular or φ-dependence. Between the two columns, draw a vertical dividing line and a pair of bracket-symbols: one labeled "integer ℓ only" (left) and one labeled "integer and half-integer ℓ" (right) — no text baked, use symbolic shapes (a row of dots for integers only vs. a row of dots including half-spacing dots for the general case). Use Sky Blue for orbital (position-space) objects, Bluish Green for spin (abstract) objects. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two cases of the angular momentum algebra: (1) orbital angular momentum in position space — e^{imφ} must satisfy Φ(φ+2π) = Φ(φ), forcing m and ℓ to be integers. Represented by a circle with a single-valued wave pattern. (2) Spin angular momentum in abstract Hilbert space — no position-space wave function, no single-valuedness constraint, ℓ=1/2 (and higher half-integers) is realized. Represented by an abstract box with two-level structure. Inferred relationship: the algebraic spectrum (general ℓ) is more general than the orbital case; the integer restriction is an additional physical constraint.
- `[O — ORGANIZATION]` Two columns separated by vertical rule. Left: circle with wavefunction ring and integer-only dot row below. Right: abstract rectangular box with two-level structure and full dot row (integers + half-integers) below. Both at the same vertical height.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: orbital circle = Sky Blue `#56B4E9`; spin box = Bluish Green `#009E73`; integer-only row = Blue `#0072B2`; half-integer dots (additional) = Orange `#E69F00`; dividing rule = light gray. 1pt stroke, white background. No baked text.
- `[E — EXCLUSIONS]` Omit: Pauli matrices, magnetic field, Bloch sphere, specific spin precession, Stern-Gerlach setup.

**BLOCK 3 — NEGATIVE PROMPT:**
Bloch sphere, Stern-Gerlach apparatus, Pauli matrix notation, magnetic field arrows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — ℓ=1 Matrix Representations of L_z, L₊, L₋

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw three 3×3 matrix grids side by side for the ℓ=1 representation. Each grid is a uniform 3×3 table of square cells. For the L_z matrix (left): shade the three diagonal cells in Blue, the off-diagonal cells light gray (zero). The shading intensity of the diagonal cells indicates relative eigenvalue: bottom cell darkest, middle cell white (zero eigenvalue), top cell medium (positive). For the L₊ matrix (center): shade only the two cells on the super-diagonal (above the main diagonal) in Sky Blue; all others light gray. The shading indicates nonzero elements that raise m. For the L₋ matrix (right): shade only the two cells on the sub-diagonal (below the main diagonal) in Orange; all others light gray. Each matrix is framed by a thin border. Below each matrix, place a small schematic indicating its role: a diagonal arrow for L_z, an upward staircase for L₊, a downward staircase for L₋. Flat vector, 1pt stroke, white background.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width (may extend to 120mm for three-matrix layout), 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three 3×3 matrices for ℓ=1 in basis {|1,−1⟩, |1,0⟩, |1,+1⟩}: L_z = ħ·diag(−1, 0, +1) — diagonal, three nonzero elements; L₊ = ħ√2 times matrix with super-diagonal 1s — two nonzero elements; L₋ = ħ√2 times matrix with sub-diagonal 1s — two nonzero elements. Nonzero elements distinguished from zero by shading. Structure of each matrix (diagonal / super-diagonal / sub-diagonal) is the key visual claim. No numerical values baked into image.
- `[O — ORGANIZATION]` Three equal-size 3×3 grids in a horizontal row. Uniform cell size. Shading encodes nonzero (colored) vs. zero (light gray). Role schematic below each matrix: diagonal arrow, upward staircase, downward staircase.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: L_z diagonal = Blue `#0072B2`; L₊ super-diagonal = Sky Blue `#56B4E9`; L₋ sub-diagonal = Orange `#E69F00`; zero cells = light gray at 15% opacity. Matrix border = dark gray 1pt. Role schematics = neutral gray. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: L_x and L_y matrices (derived from L₊/L₋, not shown here), ℓ=2 matrices, numerical matrix element values, Pauli matrix comparison (Chapter 8), 5×5 matrix.

**BLOCK 3 — NEGATIVE PROMPT:**
L_x and L_y matrix grids, ℓ=2 matrix, 5×5 grid, Pauli matrix notation, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Robertson Uncertainty Bound: Transverse Components and Saturation

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a scatter/dot plot with horizontal axis representing ℓ (values 0, 1/2, 1, 3/2, 2) and vertical axis representing an uncertainty product in units of ħ², starting at zero. For each ℓ, plot two quantities as separate markers at the same horizontal position: (1) the Robertson lower bound σ_{Lx}σ_{Ly} ≥ ħ²ℓ/2 as a horizontal dash (the bound), in Vermillion; (2) the actual product σ_{Lx}·σ_{Ly} = ħ²ℓ/2 for the maximally aligned state |ℓ,ℓ⟩, as a filled circle, in Bluish Green. Since the bound is saturated, the circle sits exactly on the dash at each ℓ-value. Connect the filled circles with a smooth Bluish Green line. The y-axis starts at 0. Include a light horizontal reference at y=0. No grid lines except the zero line.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Robertson inequality for L_x, L_y in the maximally aligned state |ℓ,ℓ⟩: bound = ħ²ℓ/2; actual σ_{Lx}σ_{Ly} = ħ²ℓ/2. Both plotted vs. ℓ for ℓ = 0, 1/2, 1, 3/2, 2. Key structural claim: bound is saturated at every ℓ — the maximally aligned state is a minimum-uncertainty state for the transverse components. Y-axis from 0.
- `[O — ORGANIZATION]` Single-panel dot/line chart. Horizontal axis: ℓ values (five points). Vertical axis: uncertainty product in ħ² units, from 0. Two series: lower bound (horizontal dash markers in Vermillion) and actual value (filled circles + connecting line in Bluish Green). Bound and actual coincide at every point — this identity is the visual claim.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito: bound markers = Vermillion `#D55E00`; actual value curve = Bluish Green `#009E73`; connecting line = Bluish Green `#009E73`; zero reference = light gray 0.5pt. 1.5pt line, 4pt filled circle markers. Y-axis from zero. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Robertson inequality for position-momentum (separate uncertainty), specific comparison with non-maximally-aligned states, harmonic oscillator coherent state analog.

**BLOCK 3 — NEGATIVE PROMPT:**
position-momentum uncertainty ellipse, coherent state wavepacket, 3D cone diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Angular momentum ladder diagram:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages with a cyclical return-to-start element. **Recommended video for Chapter 6.** The ladder derivation has a clear directionality — apply L₊ repeatedly, watch m increase one step at a time, hit the null termination at the top rung, then watch L₋ descend back — and the mechanism (the rung-by-rung stepping and both terminations) is the learning target. Animating one full "climb" from m=−ℓ to m=+ℓ and showing the null output at both ends makes the non-negativity argument viscerally concrete. One-line reason: sequential step-by-step animation of the ladder with both null terminations demonstrates why the spectrum must be finite and bounded, which is the chapter's central claim.

**Figure 2 — Spectrum derivation flowchart:** STATIC SUFFICIENT. A logical dependency chart; the four steps are simultaneously available to the reader and benefit from being compared in parallel, not unfolded sequentially.

**Figure 3 — Integer vs. half-integer comparison:** STATIC SUFFICIENT. A structural two-column comparison; no temporal unfolding needed.

**Figure 4 — ℓ=1 matrix representations:** STATIC SUFFICIENT. Three matrix grids; the key insight is the position of nonzero elements (diagonal, super-diagonal, sub-diagonal), which is fully visible in a static grid.

**Figure 5 — Robertson saturation scatter plot:** STATIC SUFFICIENT. A quantitative chart; the saturation of the bound at each ℓ is visible in a single panel with no motion required.
