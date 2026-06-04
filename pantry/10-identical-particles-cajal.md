# CAJAL Figure Report — Chapter 10 — Identical Particles

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Boson/Fermion Statistics Classification by Constituent Fermion Count

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a flat two-column taxonomy diagram. The left column is labeled by an integer parity indicator — "Even constituent fermions" — and the right by "Odd constituent fermions." Below each column heading, a horizontal band separates the header from a vertical list of particle tiles. In the left (even) column, place six tiles: photon (0 fermions), ⁴He atom (6 fermions), ⁸⁷Rb atom (87 fermions, even). In the right (odd) column, place three tiles: electron (1 fermion), proton (3 quarks), ³He atom (5 fermions). Each tile carries only the particle symbol and the constituent count as a numeral; no text is baked in — these are placeholder rectangles. An arrow below the left column points downward into a "Boson" terminus box; an arrow below the right column points into a "Fermion" terminus box. Connect the Boson terminus with a rightward extension showing a schematic BEC pile-up icon (many circles converging onto one level line) and connect the Fermion terminus with a schematic Pauli stack icon (circles filling stacked horizontal lines one per level). All shapes are flat vector rectangles and circles; no shading, no gradients, no realistic detail.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Two-column vertical layout, full height approximately 120 mm.
- `[C — CONTENT]` Left branch: even constituent fermion count → boson statistics; particles: photon (0), ⁴He (6), ⁸⁷Rb (87). Right branch: odd constituent fermion count → fermion statistics; particles: electron (1), proton (3), ³He (5). Terminus icons: bosons → macroscopic ground-state occupation; fermions → one-per-level stack. Relationship labeled: "parity count → statistics class."
- `[O — ORGANIZATION]` Top: single root band "Composite Particle Statistics." Two branches diverge downward: left (even/boson), right (odd/fermion). Particle tiles stack vertically within each branch. Arrowheads point from branch to terminus. BEC icon to the left of boson terminus; Pauli stack icon to the right of fermion terminus.
- `[P — PRESENTATION]` Flat vector. Left branch (boson): Sky Blue `#56B4E9` tile borders, Bluish Green `#009E73` terminus box. Right branch (fermion): Orange `#E69F00` tile borders, Blue `#0072B2` terminus box. Root band: neutral light gray. Uniform 1 pt strokes. White background. No baked text. Okabe-Ito palette only.
- `[E — EXCLUSIONS]` Omit: spin-statistics theorem derivation, anyons, intermediate statistics, Fermi-Dirac vs. Bose-Einstein distribution curves, temperature scales, any force or interaction arrow between particles, the Chandrasekhar mass, Cooper pairs, nuclear substructure beyond quark count.

**BLOCK 3 — NEGATIVE PROMPT:**

nuclear substructure diagrams, quark color charges, feynman vertices, distribution function curves, temperature axis, force arrows, energy level spacing, intermediate statistics, anyon diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Slater Determinant: Swapping Rows Flips the Sign

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a three-panel horizontal sequence illustrating the antisymmetry of the two-by-two Slater determinant. Panel A shows a two-by-two matrix schematic: four rectangular cells arranged in two rows and two columns, with the top row colored Sky Blue and the bottom row colored Orange; a vertical label on the left marks "Particle 1 (row 1)" and "Particle 2 (row 2)." A "det" bracket wraps the matrix. Panel B is a transition panel: a double-headed horizontal arrow labeled "swap particles 1 ↔ 2" connects Panel A to Panel C; the arrow is Orange. Panel C shows the same two-by-two matrix with rows swapped — the top row is now Orange and the bottom row is Sky Blue — wrapped in a "det" bracket, and a "−1 ×" prefactor appears to the left of the bracket. Below each of Panels A and C, a small schematic shows the resulting sign: Panel A has a "+" symbol, Panel C has a "−" symbol. A thin horizontal divider separates the top (matrix swap) narrative from a bottom row showing the key implication: two side-by-side matrices where both rows are the same color (identical columns → identical rows), with a large "= 0" to the right. All cells are blank rectangles; no text baked in.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Three-panel horizontal layout (A, arrow, C) plus an implication row beneath, total height approximately 70 mm.
- `[C — CONTENT]` 2×2 matrix: rows represent particle indices (1, 2), columns represent orbital indices (a, b). Row swap = particle exchange. Determinant sign flips under row swap. Identical columns (φ_a = φ_b) → identical rows → determinant = 0 (Pauli exclusion theorem). Relationship labeled: "row swap → sign flip"; "identical columns → det = 0."
- `[O — ORGANIZATION]` Top strip: Panel A (original matrix) → swap arrow → Panel C (swapped matrix), all aligned horizontally. Sign indicators ("+" / "−") below each panel. Bottom strip: identical-column matrix → "= 0" result, with a bracket or connective line indicating this as the Pauli corollary.
- `[P — PRESENTATION]` Row 1 cells: Sky Blue `#56B4E9`. Row 2 cells: Orange `#E69F00`. Swap arrow: Vermillion `#D55E00`. Sign symbols: Blue `#0072B2`. Identical-column matrix (bottom): both rows Reddish Purple `#CC79A7` to visually flag the special case. Zero result marker: Bluish Green `#009E73`. 1 pt strokes, white background, flat vector.
- `[E — EXCLUSIONS]` Omit: N×N generalization (that is Figure 3), explicit orbital function expressions, normalization prefactor 1/√2, spin degrees of freedom, helium energy levels, any three-particle case.

**BLOCK 3 — NEGATIVE PROMPT:**

algebraic expressions, orbital function notation, N×N matrix generalization, spin arrows, energy level diagram, normalization bracket, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — N×N Slater Determinant Structure

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a single schematic of an N×N matrix wrapped in determinant brackets. The matrix is shown as a grid of rectangular cells. Color the cells in a gradient-free, flat scheme: cells along the main diagonal are highlighted in Sky Blue; off-diagonal cells are light gray. The top row of cells is slightly larger than the others to indicate "particle 1 evaluated at orbital 1, 2, …, N." A row label strip on the left side marks rows as particle indices (1 through N, with an ellipsis row in the middle). A column label strip on the top marks columns as orbital indices (φ₁ through φ_N, with an ellipsis column). The far right shows a vertical brace with "1/√N!" prefactor as a placeholder rectangle (not text). Below the matrix, a schematic implication arrow points to two consequence icons: (a) a two-row-swap sequence (same as Figure 2 condensed) labeled "exchange → −1", and (b) a pair of identical-column highlight cells labeled "two same orbitals → det = 0." All decorative elements are flat rectangles and circles; no text baked in.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Approximately 90 mm tall.
- `[C — CONTENT]` N×N determinant: rows = particle indices 1 to N, columns = orbital indices φ₁ to φ_N. Diagonal cells: φ_i evaluated at particle i. Two structural properties: (1) any row swap → sign flip; (2) two identical columns → determinant zero. Normalization prefactor 1/√N! as a labeled placeholder. Label inferred: "main diagonal = orbital i at particle i."
- `[O — ORGANIZATION]` Central matrix with row-label strip (left) and column-label strip (top). Two consequence icons arranged horizontally below the matrix, connected by downward arrows. Diagonal cells in Sky Blue, off-diagonal in light gray.
- `[P — PRESENTATION]` Diagonal cells: Sky Blue `#56B4E9`. Off-diagonal: light gray `#CCCCCC`. Row/column label strips: Blue `#0072B2`. Consequence icon borders: Bluish Green `#009E73` for the sign-flip case, Vermillion `#D55E00` for the zero case. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: explicit Hartree-Fock equations, configuration interaction, DFT, coupled-cluster, six-term N=3 expansion, helium-specific content, bosonic determinant (permanent), any anti-Hermitian structure.

**BLOCK 3 — NEGATIVE PROMPT:**

Hartree-Fock orbital equations, DFT density functional, six-term expansion, bosonic permanent matrix, molecular orbital diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Helium Para/Ortho Energy Splitting: J and K Integrals

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Vertical energy-level diagram, approximately 100 mm tall. Y-axis (energy) starts at a defined zero baseline.
- `[C — CONTENT]` Reference level: unperturbed 1s2s energy E⁽⁰⁾ (horizontal dashed line). Two levels above it: parahelium (1s2s singlet, S=0) at E⁽⁰⁾ + J + K; orthohelium (1s2s triplet, S=1) at E⁽⁰⁾ + J − K. Bracket showing J: distance from E⁽⁰⁾ to midpoint between the two levels. Bracket showing K: half the splitting, labeled 2K ≈ 0.80 eV total. Arrow annotations: "direct integral J (classical analog)" pointing to J bracket; "exchange integral K (no classical analog)" pointing to K bracket. Spin-state icons: singlet shown as two opposite arrows (↑↓) on a shared circle; triplet shown as two parallel arrows (↑↑) on a shared circle, at the left of each level bar. Spatial wave function symmetry icons: "ψ+" (symmetric, node-absent shape) next to parahelium; "ψ−" (antisymmetric, nodal shape) next to orthohelium. Label inferred: "orthohelium lower because antisymmetric spatial wave function keeps electrons apart."
- `[O — ORGANIZATION]` Vertical energy axis (y, zero at bottom, increasing upward). E⁽⁰⁾ dashed baseline. Two horizontal level bars above it. Bracketed annotations on the right side. Spin icons to the left of each bar. Spatial symmetry schematic below each bar.
- `[P — PRESENTATION]` Parahelium bar: Orange `#E69F00` (higher energy). Orthohelium bar: Bluish Green `#009E73` (lower energy). Dashed baseline: light gray. J bracket: Blue `#0072B2`. K bracket: Reddish Purple `#CC79A7`. Spin-icon arrows: Sky Blue `#56B4E9`. 1 pt strokes, flat vector, white background. No baked text. Y-axis starts at zero.
- `[E — EXCLUSIONS]` Omit: fine-structure multiplet splitting within triplet, quantum defect, hyperfine structure, magnetic field effects, the 1s² ground state, numerical values of J and K as baked text, any wavefunction plot (that is Figure 5).

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a vertical energy-level diagram with a single horizontal dashed baseline representing the unperturbed 1s2s reference energy. Above this baseline, place two labeled horizontal level bars. The upper bar (parahelium, singlet) sits at a height J+K above the baseline; the lower bar (orthohelium, triplet) sits at height J−K. On the right side, draw two vertical bracket annotations: one spanning from the baseline to the midpoint between the bars, and one spanning the half-gap from the midpoint to the upper bar. To the left of the upper bar, draw a pair of anti-parallel spin arrows on a shared circular background; to the left of the lower bar, draw a pair of parallel spin arrows. Below each bar, draw a small schematic wavefunction icon — a smooth hump shape (symmetric) below the upper bar, and a shape with a central dip (antisymmetric) below the lower bar. A double-headed vertical arrow on the far right spans both bars and indicates the total gap. All annotations are placeholder rectangle regions; no text is baked in. Bars, arrows, brackets, and icons are all flat vector shapes.

**BLOCK 3 — NEGATIVE PROMPT:**

fine structure multiplet lines, hyperfine splitting, Zeeman levels, numerical axis tick labels, wavefunction probability density plots, radial distribution functions, explicit 3D orbital shapes, baked energy values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 5 — Mechanism: Spatial Symmetry → Electron Avoidance → Lower Coulomb Energy

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a three-step horizontal process flowchart with numbered panels. Panel 1 (leftmost): two overlapping circles representing the probability densities |ψ(r₁)|² and |ψ(r₂)|². In the symmetric case (top sub-panel), the overlap region at r₁ = r₂ is shaded heavily; in the antisymmetric case (bottom sub-panel), the overlap region is visibly absent — a gap along the diagonal. Panel 2 (middle): two schematic electron-pair diagrams side by side. Top: two dot markers (electrons) close together, connected by a short thick line representing high Coulomb repulsion. Bottom: two dot markers far apart, connected by a long thin line representing low Coulomb repulsion. Panel 3 (rightmost): two horizontal energy bars. Top: a higher bar labeled with a "+" marker. Bottom: a lower bar labeled with a "−" marker. A thin down-arrow points from the top bar to the bottom bar, indicating energy lowering. Connecting arrows between panels are straight and point right. A vertical divider separates "symmetric spatial (parahelium)" on the top track from "antisymmetric spatial (orthohelium)" on the bottom track throughout all three panels. No text is baked into any shape.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Three-panel horizontal flow, two tracks (top/bottom), approximately 60 mm tall.
- `[C — CONTENT]` Top track: symmetric spatial wave function ψ₊ → high joint probability at r₁=r₂ → high Coulomb repulsion → higher energy (parahelium). Bottom track: antisymmetric spatial wave function ψ₋ → near-zero joint probability at r₁=r₂ (Pauli node) → low Coulomb repulsion → lower energy (orthohelium). Three sequential causal steps connected by arrows. Relationship labeled: "spatial symmetry → Coulomb overlap → energy"; label inferred: "no spin-spin force involved."
- `[O — ORGANIZATION]` Two horizontal parallel tracks. Three numbered panels across both tracks. Right-pointing arrows between panels. Vertical divider labels the two tracks. Panel 3 shows energy comparison with a vertical gap between top and bottom bars.
- `[P — PRESENTATION]` Top track (symmetric/higher energy): Orange `#E69F00`. Bottom track (antisymmetric/lower energy): Bluish Green `#009E73`. Overlap-region fill: Blue `#0072B2` in top sub-panel, absent (white) in bottom sub-panel. Coulomb repulsion line (thick): Vermillion `#D55E00` in top track; thin light gray in bottom track. Energy bars follow Figure 4 convention. Flat vector, 1 pt strokes, white background.
- `[E — EXCLUSIONS]` Omit: explicit Hamiltonian, spin-orbit coupling, magnetic interactions, direct integral J, exchange integral K formula, numerical energy values, any orbital radial functions.

**BLOCK 3 — NEGATIVE PROMPT:**

Hamiltonian operator symbols, spin-orbit interaction arrows, radial wavefunction plots, explicit K and J integral expressions, exchange force arrow between electrons, magnetic field vectors, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 6 — Joint Probability Density: Boson vs. Fermion vs. Distinguishable (2D Heat Map Schematic)

**Heuristic:** VG | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw three square panels arranged horizontally, each representing the joint probability density |ψ(x₁, x₂)|² for two particles in a 1D infinite well. Panel A (boson): the density is enhanced along the main diagonal x₁ = x₂ — show this as a region of high-intensity fill centered on the diagonal. Panel B (fermion): the diagonal is a strict zero — a narrow empty band along x₁ = x₂ with density concentrated off the diagonal in two lobes. Panel C (distinguishable): density forms two off-diagonal blobs with intermediate structure, neither enhanced nor depleted along the diagonal. In each panel, the main diagonal (x₁ = x₂) is marked by a thin straight line from corner to corner. Each panel is a square with equal horizontal and vertical axes; the axes represent x₁ and x₂ from 0 to L. Below all three panels, a single narrow marginal-density curve is shown, identical in all three cases, spanning the full width of all three panels — demonstrating that the single-particle marginal is exchange-statistics blind. No text baked in; panel positions and the diagonal line carry all structural information.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Three equal square panels side by side (each ~25 mm), plus a marginal density strip below, total height ~50 mm.
- `[C — CONTENT]` x₁ axis: [0, L]. x₂ axis: [0, L]. Three joint density maps: boson (enhanced on diagonal), fermion (Pauli node on diagonal — zero), distinguishable (no diagonal feature). Shared marginal density ρ(x₁) = ∫|ψ|² dx₂, identical in all three cases. Diagonal line in each panel indicates x₁ = x₂. Label inferred: "marginal density is identical for all three symmetry classes."
- `[O — ORGANIZATION]` Three panels: left = boson, center = fermion, right = distinguishable. Diagonal line within each. Marginal density as a single line plot below all three, aligned to the x₁ axis of the panels above. No shared color axis text.
- `[P — PRESENTATION]` Color intensity within panels: sequential from white (zero) to Blue `#0072B2` (maximum). Diagonal enhancement (boson): Bluish Green `#009E73` intensity peak. Diagonal depletion (fermion): the diagonal band stays white (zero); flanking lobes in Blue `#0072B2`. Distinguishable: intermediate Blue `#0072B2` off-diagonal blobs. Diagonal marker line: Sky Blue `#56B4E9`, 1 pt. Marginal curve: Orange `#E69F00`. Panel borders: light gray. Flat vector, 1 pt strokes, white background.
- `[E — EXCLUSIONS]` Omit: color scale bar with numeric labels, axis tick labels baked in, the ⟨(x₁−x₂)²⟩ numerical readout, spin states, the 1D well walls, any wavefunction amplitude plot (only the squared modulus here).

**BLOCK 3 — NEGATIVE PROMPT:**

wavefunction amplitude (signed) plots, spin-state arrows inside panels, numeric axis labels baked in, color scale bar with numbers, 1D infinite well wall schematic, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Boson/Fermion Taxonomy:** STATIC SUFFICIENT. The classification is a fixed hierarchy with no temporal sequence or cyclical return; a static two-column taxonomy conveys it fully.

**Figure 2 — Row Swap and Sign Flip:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The core conceptual move — particles swapping produces the row-swap operation, which generates the sign flip — is a sequential spatial transformation with a causal chain (exchange → row swap → det sign → antisymmetry). Animating the rows physically swapping and the sign flipping would make the determinant algebra visceral in a way static panels do not. **Recommended video for Chapter 10.**

**Figure 3 — N×N Slater Determinant:** STATIC SUFFICIENT. The N×N generalization is a structural diagram; the scaling argument (any row swap flips the sign) is already captured in Figure 2. No additional temporal element warrants motion here.

**Figure 4 — Para/Ortho Energy Levels:** STATIC SUFFICIENT. An energy-level diagram is a static quantitative display; the spatial and energy relationships are all simultaneous. A time element does not illuminate the splitting.

**Figure 5 — Spatial Symmetry → Coulomb Energy Mechanism:** STATIC SUFFICIENT. The three-step causal chain can be read sequentially as a static flowchart. The mechanism does not involve a cyclical process or a transformation below direct observation; the static panels convey the logic without loss.

**Figure 6 — Joint Probability Density Triptych:** STATIC SUFFICIENT. The three panels are best compared side by side; toggling between them would reduce rather than enhance the comparison. The key insight (identical marginals, different joint densities) is visible in a single glance at the static triptych.
