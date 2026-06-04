# CAJAL Figure Report — Chapter 3 — Commutators, Compatibility, and the Generalized Uncertainty Principle

Recommended: 4 figures, Mixed density.

---

## Figure 1 — Canonical Commutation Derivation: Product-Rule Mechanism

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a four-panel horizontal mechanism diagram illustrating the derivation of [x̂, p̂] = iℏ. In the first panel, show two operator-application symbols stacked: x̂ applied then p̂ (order 1). In the second panel, show the reverse: p̂ applied then x̂ (order 2), with a minus sign between the first and second panels. In the third panel, expand the second application (p̂ acting on x·ψ) using the product rule: split into two sub-terms, one being p̂ acting on x (yielding the constant term iℏ) and one being x times p̂ acting on ψ. Use a forking arrow to show the product-rule split. In the fourth panel, show the cancellation of the x·(p̂ψ) terms between orders 1 and 2, leaving a single residual constant-valued circle. Connect panels with directional arrows left to right. Use flat vector, no baked text.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Horizontal multi-panel layout.

`[C — CONTENT]` Four stages: Stage 1 — x̂(p̂·ψ): two nested operation symbols applied in order 1, producing x·(−iℏ ∂ψ). Stage 2 — p̂(x·ψ): two nested operation symbols applied in order 2, triggering a product-rule fork. Stage 3 — Product-rule fork: p̂(x·ψ) splits into [p̂ acting on x] + [x times p̂ acting on ψ]; the first branch produces a constant scalar circle (representing iℏ), the second branch produces x·p̂·ψ. Stage 4 — Cancellation: the x·p̂·ψ terms from Stage 1 and the second branch of Stage 3 cancel (connected by a crossing-out or subtraction arc), leaving only the constant scalar circle from Stage 3 as the result. The final result is a single scalar object (the commutator = iℏ constant). Use fork (→ two branches) for the product rule in Stage 3. Use a subtraction/cancellation mark (crossed arrows or strikethrough line) for the cancellation in Stage 4.

`[O — ORGANIZATION]` Four panels left to right, each with a downward flow within the panel and a rightward progression between panels. Stage 3 is vertically taller (fork into two branches). Stage 4 shows the net after cancellation. Directional arrows: right-pointing between panels; downward within panels. Cancellation shown as a horizontal crossing line through the cancelled term.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. x̂ operator symbol: Sky Blue `#56B4E9`. p̂ operator symbol: Orange `#E69F00`. Product-rule fork arrows: neutral gray. Constant residual iℏ circle (result): Bluish Green `#009E73`. Cancellation mark: Vermillion `#D55E00` strikethrough on the cancelled pair. Background panels: white. Stage borders: light gray rule. Uniform 1 pt strokes. No baked text.

`[E — EXCLUSIONS]` Omit: three-dimensional generalization (δᵢⱼ), higher-order commutators like [x², p], the Robertson/Cauchy-Schwarz step, angular momentum commutators, specific ℏ numerical value, quantization rules. Show only the [x̂, p̂] derivation.

**BLOCK 3 — NEGATIVE PROMPT:**
angular momentum operators, three-dimensional commutators, Robertson inequality diagram, Cauchy-Schwarz inequality, Bloch sphere, wave function profile, energy level diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Robertson Proof: Four-Step Chain (Cauchy-Schwarz to Uncertainty Bound)

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical four-step flowchart, each step a rounded-rectangle node, connected by downward directional arrows. Node 1 shows two abstract vector norm symbols (representing σ_A² and σ_B² as squared norms of shifted operator vectors). Node 2 shows a Cauchy-Schwarz inequality arc: two norm objects on the left side of a ≥ symbol, an inner-product magnitude on the right. Node 3 shows a decomposition split: one inner product on the left of an equals sign, then a symmetric part (rounded capsule) plus an antisymmetric part (angular capsule), connected by a plus sign. The antisymmetric part capsule is visually linked to a commutator symbol. Node 4 shows the dropping of the symmetric term (a strikethrough on it) yielding the final bound: product of two norm objects ≥ half the commutator magnitude. Downward arrows connect nodes 1 → 2 → 3 → 4. Use flat vector, no baked text.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Portrait (vertical) orientation.

`[C — CONTENT]` Step 1 (Shift): Two abstract circles representing ||Â'|ψ⟩||² = σ_A² and ||B̂'|ψ⟩||² = σ_B², the variance as squared norms of shifted-operator vectors. Step 2 (Cauchy-Schwarz): The inequality σ_A² · σ_B² ≥ |⟨Â'B̂'⟩|²—a squared inner product. Step 3 (Decomposition): |⟨Â'B̂'⟩|² split into symmetric anticommutator part (real, labeled as a rounded shape) plus antisymmetric commutator part (imaginary, labeled as an angular shape). These two parts are visually distinct by shape and color. The commutator part carries the [Â, B̂] symbol (abstract, not written out). Step 4 (Drop): The anticommutator shape is crossed out (Vermillion strikethrough), and the remaining term gives σ_A · σ_B ≥ ½|[Â, B̂]|. The final node contains two norm symbols ≥ one half-commutator symbol.

`[O — ORGANIZATION]` Top-to-bottom flowchart, four nodes. Nodes are approximately equal-width rounded rectangles. Each labeled with the step name (abstract shape coding only, no text). Downward single-headed arrows between steps. Step 3 is the widest (decomposition into two terms). Step 4 shows the strikethrough on the left (dropped) term and the surviving term on the right.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Step 1 nodes (variance circles): Blue `#0072B2`. Step 2 (Cauchy-Schwarz): Sky Blue `#56B4E9`. Step 3 anticommutator shape: Orange `#E69F00` (symmetric/real). Step 3 commutator shape: Reddish Purple `#CC79A7` (antisymmetric/imaginary). Strikethrough on anticommutator in Step 4: Vermillion `#D55E00`. Final bound result node: Bluish Green `#009E73`. Arrows: neutral gray. White background. Uniform 1 pt strokes. No baked text.

`[E — EXCLUSIONS]` Omit: specific operator identities (spin, position-momentum), numerical values of ℏ, Bloch sphere, energy level diagram, degenerate case, Schrödinger tighter bound, entropic uncertainty relations.

**BLOCK 3 — NEGATIVE PROMPT:**
Bloch sphere, spin matrices, specific commutator value iℏ, energy level diagram, entropic uncertainty relation, Schrödinger uncertainty bound, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Robertson Bound on the Bloch Sphere: State-Dependence of the Bound

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw an orthographic projection of a sphere (the Bloch sphere) with latitude and longitude guide lines visible as thin curves. Color the surface of the sphere continuously from one color at the equatorial band to another color at the poles, representing the value of |⟨Ŝ_y⟩| = |sin θ sin φ| at each point—brightest at the two equatorial points where φ = π/2 and 3π/2 (the +y and −y poles), fading to the neutral background color at the north and south poles (θ = 0 and θ = π) and at the equatorial points φ = 0 and φ = π. Mark four special points with distinct dot symbols: north pole, south pole, +x equatorial point, +y equatorial point. Use a smooth continuous color gradient across the sphere surface. No baked text.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Square or slightly portrait format.

`[C — CONTENT]` Bloch sphere in orthographic projection. Surface color encodes Robertson bound value |sin θ sin φ| for the Ŝ_x, Ŝ_z pair: maximum (1) at +y and −y equatorial points (θ = π/2, φ = π/2 and 3π/2); zero (0) at north pole, south pole, and at +x/−x equatorial points (φ = 0, π). The color map: zero bound → neutral gray; maximum bound → Reddish Purple `#CC79A7`. Four marked special points: north pole (Ŝ_z eigenstate, zero bound), +x equatorial (Ŝ_x eigenstate, zero bound), +y equatorial (maximum bound, saturated), south pole (zero bound). These four markers are filled circles of distinct color on the sphere surface. Latitude and longitude lines: thin light gray curves.

`[O — ORGANIZATION]` Single sphere centered in the frame. Three visible orthogonal axes (x, y, z) shown as thin gray arrows extending beyond the sphere surface. Sphere surface colored continuously. Four special-point markers are prominent filled circles (≥3 pt diameter). No panel division.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette (adapted for continuous surface coloring). Surface color interpolates: zero → light gray; maximum → Reddish Purple `#CC79A7`. North-pole marker: Blue `#0072B2`. South-pole marker: Blue `#0072B2`. +x equatorial marker: Sky Blue `#56B4E9`. +y equatorial marker: Reddish Purple `#CC79A7` (maximum bound, visually matches surface maximum). Latitude/longitude lines: neutral gray 0.5 pt. Axis arrows: neutral gray 1 pt. White background. No baked text.

`[E — EXCLUSIONS]` Omit: state vector arrow (focus is on the surface map, not a specific state), energy level diagram, matrix representation, commutator derivation steps, Cauchy-Schwarz steps, actual σ values (this figure shows the bound magnitude, not the spreads).

**BLOCK 3 — NEGATIVE PROMPT:**
state vector arrow on sphere, energy levels, matrix grid, commutator derivation boxes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Compatible vs. Incompatible Observables: Shared Eigenbasis or Not

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side comparison panels. Left panel (compatible): draw two overlapping sets of directional arrows, all pointing along the same directions, indicating that operator A and operator B share the same set of eigenvectors (each arrow is simultaneously an eigenvector of both). The arrows form one unified grid or fan pattern. Right panel (incompatible): draw two distinct non-overlapping fans of directional arrows at different angles—one fan for operator A's eigenvectors, one fan for operator B's eigenvectors—showing they are rotated relative to each other and have no common directions. A small crossed-lines symbol between the two fans in the right panel indicates incompatibility. Both panels share the same visual scale. A vertical dividing rule separates them. No text baked in.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Left panel (compatible, [Â, B̂] = 0): A single orthonormal set of three eigenvector arrows. Each arrow is drawn in two overlapping colors or as a double-line arrow, indicating it is simultaneously an eigenvector of both Â and B̂. The joint eigenbasis is unique (or at least exists). Right panel (incompatible, [Â, B̂] ≠ 0): Two distinct sets of eigenvector arrows at ~45° relative rotation. One set in one color (Â eigenvectors), one set in another color (B̂ eigenvectors). The two sets do not align. A small X-shaped conflict marker between them. The visual contrast is alignment (left) versus misalignment (right).

`[O — ORGANIZATION]` Two equal-width panels side by side with a thin vertical dividing rule. Both panels show 3 arrow vectors emanating from a common origin. Left panel: arrows shown as dual-color (one color inside, another outside, or alternating stripes) indicating shared ownership. Right panel: one color set slightly above and one color set slightly below/rotated, with small X conflict marker. Both panels same bounding box.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Â eigenvectors: Blue `#0072B2`. B̂ eigenvectors: Orange `#E69F00`. Shared (compatible) arrows: Bluish Green `#009E73` (blend/joint). Conflict marker (right panel): Vermillion `#D55E00`. Dividing rule: neutral gray. White background. Uniform 1 pt strokes. No baked text.

`[E — EXCLUSIONS]` Omit: specific operator names (L², Lz, Sx, Sz, H), commutator formula, Robertson bound, Bloch sphere, quantum numbers n/ℓ/m, degeneracy subspace, matrix grid.

**BLOCK 3 — NEGATIVE PROMPT:**
specific operator labels, quantum number labels, commutator formula, Robertson inequality diagram, Bloch sphere, matrix grid, hydrogen atom energy levels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Canonical Commutation Derivation:** STATIC SUFFICIENT. The four-step product-rule expansion is a logical sequence of algebraic manipulations. While it has multiple steps, the learning target is algebraic structure (how the product rule generates the residual iℏ), and a well-designed static flowchart with clear fork-and-cancel visual notation communicates this fully. The sequence does not involve a continuous transformation below direct observation.

**Figure 2 — Robertson Proof Flowchart:** STATIC SUFFICIENT. The proof is a logical chain of inequalities. Static boxes-and-arrows with color-coded components communicate the four steps without requiring animation. No cyclical or continuously transforming process.

**Figure 3 — Robertson Bound on the Bloch Sphere:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The central learning goal of the chapter is that the Robertson bound is a property of the state, and watching the bound value change continuously as a student drags a state arrow around the Bloch sphere makes this completely visceral—the student can watch the bound rise to maximum at the +y eigenstate, fall to zero at the poles, and track the saturation condition in real time. A short looping animation rotating the state arrow along a latitude circle, while a paired bar chart shows the Robertson bound rising and falling in synchrony, would be uniquely effective. Recommended video for the chapter.

**Figure 4 — Compatible vs. Incompatible Eigenbases:** STATIC SUFFICIENT. The alignment vs. misalignment of two eigenbases is a structural spatial contrast naturally conveyed by a side-by-side static comparison. No temporal process is involved.

**Chapter recommended video:** Figure 3 — Robertson Bound on the Bloch Sphere: State-Dependence of the Bound.
