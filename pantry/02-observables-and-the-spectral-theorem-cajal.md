# CAJAL Figure Report — Chapter 2 — Observables, Hermiticity, and the Spectral Theorem

Recommended: 4 figures, Mixed density.

---

## Figure 1 — Spectral Decomposition: Operator as Weighted Sum of Projectors

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a horizontal decomposition diagram. On the left, show a single Hermitian operator object (a rounded-rectangle representing Â). An equals sign separates it from the right side, which contains two additive terms. Each term is a weighted projector: a scalar circle (representing the eigenvalue weight) multiplied by a projector object (a flat square with an arrow inside indicating the projection direction). The two terms are separated by a plus symbol. Each projector object has a distinct orientation arrow, pointing in different directions to suggest orthogonal eigenspaces. Use a consistent flat-vector style. The overall read is: one object on the left equals two weighted projector objects on the right. No text baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left: abstract Hermitian operator symbol (single entity). Right: two terms each consisting of a scalar weight (eigenvalue) × projector (outer-product object). Projectors visually represented as square tiles with an interior directional arrow indicating the eigenstate direction. Two projectors are orthogonal: their arrows point in perpendicular directions. The decomposition relation is Â = a₁ P̂₁ + a₂ P̂₂. The eigenvalue weights a₁ and a₂ are shown as abstract scalar circles, not as specific numbers. The completeness sum P̂₁ + P̂₂ = Î is implied by the two projectors exhausting the space (inferred relation—mark by showing them together covering a square background).

`[O — ORGANIZATION]` Left-to-right linear layout: [operator] = [weight₁ × projector₁] + [weight₂ × projector₂]. The two projector tiles sit side by side on the right. Directional arrows inside the projectors are the visual anchors showing orthogonality. Plus sign between terms as a simple symbol. No panel division needed.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Operator object: Blue `#0072B2`. Eigenvalue scalar circles: Orange `#E69F00` (a₁) and Sky Blue `#56B4E9` (a₂). Projector tiles: Bluish Green `#009E73`. Interior eigenstate arrows: White on the Bluish Green tiles. Weight × projector multiplication dot: neutral gray. White background. Uniform 1 pt strokes. No baked text.

`[E — EXCLUSIONS]` Omit: degenerate case (rank > 1 projectors), continuous spectrum / spectral measure, matrix entries, eigenvalue numerical values, wave function profiles, Born rule probability calculation, time evolution. Show the non-degenerate two-term case only.

**BLOCK 3 — NEGATIVE PROMPT:**
degenerate projector (rank > 1), continuous spectrum, matrix grid entries, numerical eigenvalues, wave function curve, Born-rule probability bars, time evolution, unitary operator, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Born Rule as Geometric Projection

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-dimensional vector diagram within a unit-circle boundary. Place a state arrow from the origin to a point on or inside the unit circle. Draw two orthogonal unit-length basis arrows also from the origin, representing two eigenstates of an observable, at perpendicular angles. Drop two perpendicular projection lines from the tip of the state arrow onto each basis arrow. Mark the foot of each projection with a small right-angle symbol. The length of each projection segment should be visually apparent. Below or beside each basis arrow, show a small filled square whose area is proportional to the squared projection length, representing the probability. Use a consistent flat-vector style. No text baked in.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Unit circle boundary (light gray). State vector |ψ⟩: arrow from origin to a point at some angle (not aligned with either basis vector). Two orthogonal eigenstates |a₁⟩ and |a₂⟩: unit arrows along perpendicular axes. Projection from tip of |ψ⟩ onto each eigenstate axis: dotted perpendicular projection lines with right-angle corner markers at the foot. Projection length = amplitude |⟨aₙ|ψ⟩|. Probability panels: two small filled squares beside the respective eigenstate arrows, with areas proportional to |⟨a₁|ψ⟩|² and |⟨a₂|ψ⟩|² respectively. The two squares together should visually sum to the same total (complementarity). All angular and length relationships are geometrically accurate for a representative angle (e.g., state at ~35° from first eigenstate).

`[O — ORGANIZATION]` Centered composition: unit circle at center, two basis arrows along horizontal and vertical directions. State arrow at ~35° from horizontal. Projection lines as dashed or dotted. Probability squares placed adjacent to each axis arrow tip. Right-angle markers at projection feet. Compact, no wasted whitespace.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. State arrow |ψ⟩: Blue `#0072B2`. Eigenstate arrows |a₁⟩, |a₂⟩: Sky Blue `#56B4E9`. Projection lines: light gray dashed. Right-angle markers: neutral gray. Probability square for a₁: Bluish Green `#009E73`. Probability square for a₂: Orange `#E69F00`. Unit circle: light gray 0.5 pt. White background. No baked text.

`[E — EXCLUSIONS]` Omit: expectation value calculation, spectral decomposition formula, time evolution, degenerate eigenspaces, three-dimensional geometry, density matrix, measurement-disturbance language.

**BLOCK 3 — NEGATIVE PROMPT:**
three-dimensional sphere, density matrix, Bloch sphere, expectation value formula, degenerate subspace, time evolution, commutator, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Hermitian Matrix Structure: Diagonal Real, Off-Diagonal Conjugate Pairs

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two 3×3 matrix grids side by side. The left grid represents the original matrix A and the right grid represents its conjugate transpose A†. In each grid, mark the cells with color: diagonal cells in one color (real values), upper-off-diagonal cells in a second color, lower-off-diagonal cells in a third color. In the left grid, upper-off-diagonal cells (e.g., position 1,2 and 1,3 and 2,3) are one color; lower-off-diagonal cells are a different color. In the right grid (conjugate transpose), the positions are mirror-swapped with a conjugate symbol indicated by a small asterisk-shaped mark inside the cell (not as text). An equals sign between the two grids indicates the Hermitian condition A = A†. A small check mark or equal-sign indicator on the diagonal of each grid shows the diagonal entries are self-conjugate (real). Use flat vector, no text baked in.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Two 3×3 matrix grids. Left: matrix A. Right: conjugate transpose A†. The Hermitian condition A_mn = A*_nm is visualized by: (1) diagonal cells identical in both grids (real, self-equal), shown in one color; (2) upper-off-diagonal cell in left grid paired by color with lower-off-diagonal cell in right grid (they are conjugates of each other); (3) vice versa. The pairing is shown by matching colors between corresponding cells across the two grids. Conjugation is indicated by a small abstract star/asterisk symbol within paired cells (not typed text). The overall message: the matrix equals its mirror-conjugate.

`[O — ORGANIZATION]` Side-by-side layout: left 3×3 grid, central equals sign, right 3×3 grid. Cells are equal-sized squares. Color-coding: diagonal cells one color across both; upper-triangle cells in left grid paired by color with lower-triangle cells in right grid (same color = conjugate pair). Color pairing: cell (1,2) in A same color as cell (2,1) in A†; cell (1,3) in A same color as cell (3,1) in A†; etc.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Diagonal cells: Orange `#E69F00` in both grids (real, self-paired). Conjugate pair 1 (position 1,2 ↔ 2,1): Sky Blue `#56B4E9`. Conjugate pair 2 (position 1,3 ↔ 3,1): Bluish Green `#009E73`. Conjugate pair 3 (position 2,3 ↔ 3,2): Reddish Purple `#CC79A7`. Grid lines: neutral gray 0.5 pt. Equals sign between grids: neutral gray. White background. No baked text.

`[E — EXCLUSIONS]` Omit: specific matrix values or numbers inside cells, anti-Hermitian or non-Hermitian contrast example, eigenvalue diagram, spectral decomposition, wave function, probability bars. Show only the structural color pattern of the Hermitian condition.

**BLOCK 3 — NEGATIVE PROMPT:**
numerical matrix entries, anti-Hermitian example, non-Hermitian matrix, eigenvalue arrows, probability bars, wave function, spectral decomposition, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Real vs. Complex Eigenvalues: Effect of Hermiticity

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side number-line panels. The left panel shows a horizontal real number line with three discrete point markers placed on it at distinct real positions (representing the real eigenvalues of a Hermitian operator). The right panel shows a two-dimensional complex plane (real axis horizontal, imaginary axis vertical) with three point markers placed off the real axis at positions with nonzero imaginary parts (representing eigenvalues of a non-Hermitian operator). The contrast between all points on the line (left) versus points scattered in the plane (right) is the visual message. A vertical divider separates the two panels. Both panels have the same horizontal axis scale. Use flat vector, no text baked in.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left panel: real number line (horizontal). Three filled circles at positions approximately −1, 0.5, 2 on the line. These represent three real eigenvalues (Hermitian case). Right panel: complex plane with real and imaginary axes. Three filled circles placed off the real axis at positions such as (0.5+1.5i), (−1−0.8i), (1.5+0.3i). These represent eigenvalues with imaginary parts (non-Hermitian case). All markers are identical in size and shape across both panels. The panels share the same x-axis range for comparability. Imaginary axis appears only in the right panel.

`[O — ORGANIZATION]` Two equal-width panels side by side with a thin vertical dividing rule. Left: 1D line only (no y-axis). Right: 2D plane with both axes. Point markers centered on each eigenvalue position. Axis crosshairs as thin gray rules. No gridlines beyond the axes.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Eigenvalue markers in left panel (real): Bluish Green `#009E73`. Eigenvalue markers in right panel (complex): Vermillion `#D55E00` (highlighting the problematic / physically inconsistent case). Axis lines: neutral gray 0.5 pt. Dividing rule: neutral gray. White background. No baked text.

`[E — EXCLUSIONS]` Omit: eigenvectors, probability calculations, the matrix itself, Hermitian vs. anti-Hermitian labeling text, wave functions, spectral decomposition formula, specific numerical values on axes.

**BLOCK 3 — NEGATIVE PROMPT:**
eigenvector arrows, matrix grid, probability bars, wave function curves, anti-Hermitian label, specific axis tick labels as text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Spectral Decomposition:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The key conceptual move is that a single Hermitian operator dissolves into a sum of projectors, each weighted by an eigenvalue—a decomposition that should feel like the operator "disassembling" into orthogonal pieces. An animation that starts with the unified operator object, then progressively reveals each projector term being peeled off (P̂₁ separates, then P̂₂), while weights appear as scalings, makes the constructive/deconstructive nature of the spectral decomposition far more visceral than a static equals sign. Recommended video for the chapter.

**Figure 2 — Born Rule as Geometric Projection:** STATIC SUFFICIENT. The geometric projection in a 2D vector space is inherently static—no temporal process is involved. The static diagram showing the state vector, two eigenbasis arrows, dashed projection lines, and area-proportional probability squares fully communicates the geometric meaning of the Born rule.

**Figure 3 — Hermitian Matrix Structure:** STATIC SUFFICIENT. The color-coded conjugate-pair pattern is a structural pattern best grasped by inspection of both matrices simultaneously. No process or sequence is involved.

**Figure 4 — Real vs. Complex Eigenvalues:** STATIC SUFFICIENT. A side-by-side comparison of two static point distributions (real line vs. complex plane) communicates the contrast immediately. No sequential mechanism requires animation.

**Chapter recommended video:** Figure 1 — Spectral Decomposition: Operator as Weighted Sum of Projectors.
