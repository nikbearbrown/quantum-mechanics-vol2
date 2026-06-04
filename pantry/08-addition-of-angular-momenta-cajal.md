# CAJAL Figure Report — Chapter 8 — Addition of Angular Momenta

Recommended: 4 figures, Mechanistic density.

---

## Figure 1 — Two-Basis Decomposition: Uncoupled to Coupled Basis for ½ ⊗ ½

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two vertical columns of labeled state boxes connected by a unitary-arrow fan in the center. Left column: four boxes arranged vertically, representing the four uncoupled product states (both up, up-down, down-up, both down) ordered by M = m₁ + m₂ from top to bottom. Right column: four boxes arranged vertically representing the four coupled states (triplet M=+1, triplet M=0, triplet M=−1, singlet M=0), with the singlet box separated slightly from the three triplet boxes by a gap to indicate a different total-J multiplet. Between the two columns, draw connecting arrows from each uncoupled state to the coupled state(s) it contributes to, with arrow thickness proportional to the squared Clebsch–Gordan coefficient (thick arrows for weight 1, medium arrows for weight 1/2). On the right side, bracket the three triplet boxes together and bracket the singlet box separately. All boxes are flat rectangles; arrows are directional; the layout emphasizes the block structure of the CG matrix.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Basis change for the j₁ = j₂ = ½ system. Uncoupled states: |↑↑⟩ (M=+1), |↑↓⟩ (M=0), |↓↑⟩ (M=0), |↓↓⟩ (M=−1). Coupled states: |1,+1⟩ = |↑↑⟩ (CG coefficient 1); |1,0⟩ = (|↑↓⟩ + |↓↑⟩)/√2 (coefficients 1/√2 from each M=0 uncoupled state); |1,−1⟩ = |↓↓⟩ (coefficient 1); |0,0⟩ = (|↑↓⟩ − |↓↑⟩)/√2 (coefficients ±1/√2). The triplet multiplet (J=1) and singlet (J=0) bracketed separately on the right. Arrow thickness encodes |CG|²: weight 1 → thick, weight 1/2 → thin. Inferred relation: sign difference between the M=0 triplet and singlet CG coefficients is shown by arrow color (positive/negative).

`[O — ORGANIZATION]` Two-column layout with coupling fan in center. Uncoupled column on left, ordered M: +1, 0, 0, −1 top to bottom. Coupled column on right: triplet group (3 boxes) plus a gap plus singlet box (1 box). Connecting arrows cross between columns. Triplet bracket on right spans three boxes; singlet bracket spans one. Dimension count annotation: 4 = 3 + 1 encoded in bracket labels.

`[P — PRESENTATION]` Flat vector. Uncoupled state boxes: light gray fill, Blue #0072B2 outline. Triplet state boxes: Sky Blue #56B4E9 fill. Singlet state box: Reddish Purple #CC79A7 fill. Arrows with positive CG coefficient: Bluish Green #009E73, directional. Arrows with negative CG coefficient: Vermillion #D55E00, directional. Thick arrows (weight 1): 2pt. Thin arrows (weight 1/2): 1pt. Brackets: Orange #E69F00. White background.

`[E — EXCLUSIONS]` Omit: the full numerical CG table matrix layout, j₁ ≠ ½ cases, 3D angular momentum vector diagrams, Wigner 3j-symbols, recoupling coefficients, entanglement measure annotations.

**BLOCK 3 — NEGATIVE PROMPT:**
full numerical CG matrix table, j≠½ coupled-state diagram, 3D vector coupling diagram, Wigner 3j-symbol notation boxes, recoupling diagram, entanglement measure annotation, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Triangle Rule and State Counting: Three Representative Combinations

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-row comparison chart. Each row represents one angular-momentum combination and consists of three elements: a small icon on the left encoding j₁ and j₂ as two circles of sizes proportional to (2j+1), a horizontal segmented bar in the center with one segment per allowed J value (segment width proportional to 2J+1), and a total-count indicator on the right. Row 1: j₁ = j₂ = ½ — bar has two segments for J=0 (width 1) and J=1 (width 3), total 4. Row 2: j₁ = 1, j₂ = ½ — bar has two segments for J=½ (width 2) and J=3/2 (width 4), total 6. Row 3: j₁ = j₂ = 1 — bar has three segments for J=0 (width 1), J=1 (width 3), J=2 (width 5), total 9. Each J-value segment is a distinct Okabe-Ito color. The total-count indicators on the right visually confirm the product (2j₁+1)(2j₂+1) via equal-area matching.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Triangle rule J = |j₁−j₂|, …, j₁+j₂ and state-count verification for three cases. Case 1: ½⊗½ → J=0 (dim 1) + J=1 (dim 3) = 4 = 2×2. Case 2: 1⊗½ → J=½ (dim 2) + J=3/2 (dim 4) = 6 = 3×2. Case 3: 1⊗1 → J=0 (dim 1) + J=1 (dim 3) + J=2 (dim 5) = 9 = 3×3. Horizontal bars encode the dimension (2J+1) of each multiplet as proportional width. Product verification encoded by equality of total bar width with product (2j₁+1)(2j₂+1). Color coding of J values consistent across rows: J=0 always one color, J=1 always another, etc.

`[O — ORGANIZATION]` Three rows, one per combination, sharing a common left edge. Left: pair-size icons (two filled circles, radius ∝ 2j+1). Center: segmented horizontal bar, zero-anchored, segments labeled by J value order. Right: dimension-product indicator (a single rectangular block of width equal to the total, showing the product). Rows separated by thin horizontal dividers.

`[P — PRESENTATION]` Flat vector. J=0 segments: Reddish Purple #CC79A7. J=½ segments: Sky Blue #56B4E9. J=1 segments: Blue #0072B2. J=3/2 segments: Orange #E69F00. J=2 segments: Bluish Green #009E73. j₁, j₂ icons: light gray. Product reference block outlines: Blue #0072B2, 1pt dashed. Segment borders: white, 0.5pt. White background.

`[E — EXCLUSIONS]` Omit: actual CG coefficient values inside the bar, cases beyond j=1, 3D angular momentum vector addition triangles, continuous-spectrum bar, error bars, fractional-J extensions beyond j=3/2.

**BLOCK 3 — NEGATIVE PROMPT:**
CG coefficient numbers inside bars, cases j>1, 3D vector addition triangle diagram, continuous probability distribution bar, error bars, fractional-j extensions beyond 3/2, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Ladder Operator Algorithm: Building |1,0⟩ from |1,1⟩

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a four-step vertical flowchart. Step 1 box: a single state icon representing the stretched state |1,1⟩ = |↑↑⟩, with a two-particle configuration symbol (two small filled circles, both in upper position). Step 2: a downward arrow labeled with the lowering operator symbol Ĵ₋, splitting into two descending paths, each ending at a single-particle lowering event — one path lowers particle 1 (|↓↑⟩), the other lowers particle 2 (|↑↓⟩). Step 3: a summation node combining the two paths, with a normalization divisor symbol (√2), yielding the |1,0⟩ state shown as a symmetric combination icon (two equal-weight configurations). Step 4: a symmetry indicator — a double-headed exchange arrow between the two configurations inside the |1,0⟩ box, labeled "S" for symmetric. All boxes are flat rectangles; the two descent paths are curved; the summation node is a filled circle.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Ladder operator derivation of |1,0⟩ from |1,1⟩ for j₁ = j₂ = ½. Step 1: stretched state |J=1, M=1⟩ = |↑↑⟩, unique state with m₁+m₂ = +1. Step 2: Ĵ₋ = Ĵ₁₋ + Ĵ₂₋ acts on |↑↑⟩ — Ĵ₁₋ lowers particle 1 to give |↓↑⟩, Ĵ₂₋ lowers particle 2 to give |↑↓⟩, each with coefficient ℏ. Step 3: equate Ĵ₋|1,1⟩ = ℏ√2|1,0⟩ with ℏ|↓↑⟩ + ℏ|↑↓⟩; solve for |1,0⟩ = (|↑↓⟩ + |↓↑⟩)/√2. Step 4: |1,0⟩ is symmetric under particle exchange (1↔2). Two-particle configuration icons: filled circle = spin-up (upper position), open circle = spin-down (lower position), shown per particle slot.

`[O — ORGANIZATION]` Top-to-bottom flow. Step 1 box at top → lowering operator arrow → two parallel descent arrows to intermediate states → summation node → normalized state box → symmetry annotation. The two descent paths diverge from the lowering arrow and reconverge at the summation node. Each step separated by ≥8mm vertical gap.

`[P — PRESENTATION]` Flat vector. Step 1 box (stretched state): Bluish Green #009E73, 1pt outline. Lowering operator arrow: Blue #0072B2, 1.5pt. Particle-1 descent path: Sky Blue #56B4E9. Particle-2 descent path: Orange #E69F00. Summation node: Reddish Purple #CC79A7 filled circle. Final state box |1,0⟩: Blue #0072B2, 1pt outline. Symmetry exchange arrow: Reddish Purple #CC79A7, 1pt. Configuration icons — spin-up filled circle: Blue #0072B2; spin-down open circle: light gray outline. White background.

`[E — EXCLUSIONS]` Omit: the singlet |0,0⟩ derivation within this figure (separate figure or note), raising operator paths, Clebsch–Gordan numerical table, the Condon–Shortley phase-convention decision diagram, j>½ ladder derivations.

**BLOCK 3 — NEGATIVE PROMPT:**
singlet derivation branch, raising operator paths, CG numerical table overlay, Condon–Shortley phase diagram, j>½ ladder steps, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Spin–Orbit Energy Splitting: Coupled Basis Diagonalizes Ĥ_so

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-panel energy-level diagram for the hydrogen 2p state. Left panel: uncoupled basis levels — six horizontal lines at the same height (all degenerate under the Coulomb Hamiltonian), color-coded by (m_ℓ, m_s) pair, with connecting off-diagonal arrows between levels indicating that Ĥ_so has off-diagonal matrix elements in this basis. Right panel: coupled basis levels — two groups of horizontal lines separated by a vertical gap: a lower group of two lines at one energy (J=½, doublet) and an upper group of four lines at a higher energy (J=3/2, quartet). No off-diagonal connecting arrows in the right panel. A vertical double-headed arrow between the two groups in the right panel indicates the energy splitting 3λℏ²/2. Both panels share the same vertical energy axis with a common zero.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` 2p hydrogen fine-structure splitting from spin–orbit Hamiltonian Ĥ_so = λL̂·Ŝ. Uncoupled basis (ℓ=1, s=½): six degenerate states (m_ℓ = −1,0,+1 × m_s = ±½) at the same Coulomb energy. Ĥ_so couples states with different m_ℓ, m_s pairs at fixed M = m_ℓ + m_s — shown as off-diagonal connecting arrows between selected pairs (only those with same M shown). Coupled basis: J=½ doublet (two states, 2J+1=2) at ΔE_so = (λℏ²/2)[¾ − 2 − ¾] = −λℏ²; J=3/2 quartet (four states, 2J+1=4) at ΔE_so = (λℏ²/2)[15/4 − 2 − ¾] = λℏ²/2. Splitting between quartets and doublets: 3λℏ²/2. No off-diagonal matrix elements in coupled basis — the absence of connecting arrows encodes diagonalization.

`[O — ORGANIZATION]` Two vertical panels side by side sharing a common energy axis (vertical). Left panel: six equally spaced short horizontal lines at same height, with selected curving off-diagonal coupling arrows between pairs. Right panel: two groups of horizontal lines at different heights — lower doublet (2 lines, grouped), upper quartet (4 lines, grouped). Double-headed splitting arrow between the two groups. Both panels bounded by thin vertical borders.

`[P — PRESENTATION]` Flat vector. Uncoupled levels: Sky Blue #56B4E9, 1pt, all at same height. Off-diagonal coupling arrows: Orange #E69F00, 0.75pt curved. J=½ doublet lines (right panel): Reddish Purple #CC79A7, 1.5pt. J=3/2 quartet lines (right panel): Bluish Green #009E73, 1.5pt. Splitting double-headed arrow: Blue #0072B2, 1pt. Vertical energy axis: light gray, 0.5pt. White background.

`[E — EXCLUSIONS]` Omit: numerical values of λ, relativistic correction diagrams (Darwin term, mass-velocity), Zeeman effect field arrows, hyperfine structure, magnetic quantum number degeneracy sublabels, 3d or other orbital spin-orbit diagrams in same panel.

**BLOCK 3 — NEGATIVE PROMPT:**
numerical λ values baked as text, Darwin term arrows, Zeeman field arrow, hyperfine splitting levels, 3d orbital spin-orbit panel, magnetic sublevel fine labeling, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Two-Basis Decomposition:** STATIC SUFFICIENT. The CG basis change is a structural mapping; a static two-column fan diagram conveys all connections at once. The learning target is reading off which uncoupled states contribute to each coupled state, not following a temporal process.

**Figure 2 — Triangle Rule State Counting:** STATIC SUFFICIENT. A three-row comparison bar chart is a lookup table; no temporal or causal sequence is involved.

**Figure 3 — Ladder Operator Algorithm:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages (start from stretched state → apply Ĵ₋ → lower each particle independently → sum and normalize → read symmetry) where each stage's output is the input to the next. The algorithm is iterative: the same lowering step is applied again to build |1,−1⟩ and then a different operation (orthogonalization) produces |0,0⟩. A video that runs the algorithm step by step — showing each application of Ĵ₋, the intermediate partial states, and the normalization — makes the generalizability of the method (applicable to any j₁, j₂) clearer than a compressed static flowchart. **Recommended video for Chapter 8.**

**Figure 4 — Spin–Orbit Energy Splitting:** STATIC SUFFICIENT. The two-panel before/after diagram (uncoupled disordered levels → coupled diagonal levels) is a single structural comparison. The absence of off-diagonal arrows in the right panel is the key message, readable statically.
