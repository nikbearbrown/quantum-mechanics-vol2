# CAJAL Figure Report — Chapter 9 — The Hydrogen Atom

Recommended: 5 figures, Mixed density.

---

## Figure 1 — Radial Probability Density P(r) for the 1s State: Two Radii Compared

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single line chart showing the radial probability density P(r) = (4/a₀³) r² e^{−2r/a₀} for the hydrogen ground state, plotted from r = 0 to r = 6a₀. The y-axis starts at zero. The curve rises from zero at the origin, reaches a single peak, then decays asymptotically toward zero. Place a vertical line at the peak (r_mp = a₀) and a second vertical line to its right at a slightly greater radius (⟨r⟩ = 3a₀/2). The region under the curve to the right of the peak should be shaded with a light fill to indicate the long tail pulling the mean above the peak. Both vertical lines are distinct solid colors. The curve itself is a smooth, continuous line. The x-axis represents r in units of a₀; the y-axis represents P(r) in units of a₀⁻¹.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Radial probability density for the hydrogen 1s state: P(r) = (4/a₀³)r²e^{−2r/a₀}. Domain: r ∈ [0, 6a₀]. Range: y-axis from 0 to max(P). Peak at r_mp = a₀ (most-probable radius). Mean at ⟨r⟩ = 3a₀/2 (mean radius). The curve is right-skewed: mean lies to the right of the peak due to the long exponential tail at large r. Tail area (r > r_mp) shaded to indicate >50% probability mass lies outside the peak. Key distinction: this is P(r) = r²|R_{10}|², not |R_{10}|² or |ψ_{100}|². The r² Jacobian factor causes P(0) = 0 even though |ψ_{100}|² is maximum at the origin.

`[O — ORGANIZATION]` Single panel. Horizontal x-axis: r from 0 to 6a₀, zero-anchored. Vertical y-axis: P(r) from 0 upward. Smooth curve. Two vertical marker lines: one at r = a₀ (peak), one at r = 3a₀/2 (mean). Light shading under the curve from r = a₀ to r = 6a₀. The shaded region is filled with semi-transparent hue; the curve line itself remains fully opaque.

`[P — PRESENTATION]` Flat vector. Curve: Blue #0072B2, 2pt solid. Vertical line at r_mp: Bluish Green #009E73, 1.5pt solid. Vertical line at ⟨r⟩: Orange #E69F00, 1.5pt solid. Tail shading: Sky Blue #56B4E9, 20% opacity fill under curve from peak to right edge. Axis lines: light gray, 0.5pt. White background. Y-axis from zero, no 3D, no gradient background.

`[E — EXCLUSIONS]` Omit: |R_{10}|² curve (confusable with P(r) — do not overlay), |ψ_{100}|² 3D plot, radial densities for n=2 or higher states in the same panel, error bars, Bohr orbit circle overlay.

**BLOCK 3 — NEGATIVE PROMPT:**
|R_{10}|² overlay curve, 3D probability density volume, n=2 radial density in same panel, Bohr orbit circle, error bars, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Effective Potential V_eff(r): Coulomb Well vs. Centrifugal Barrier

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line chart with three curves sharing the same axes, plotting V_eff(r) = −e²/(4πε₀r) + ℏ²ℓ(ℓ+1)/(2μr²) for ℓ = 0, 1, and 2 over the domain r ∈ [0.1a₀, 12a₀]. The y-axis spans from a large negative value (deep well near origin) up through zero, zero-anchored is NOT required here since V can be negative — but the zero energy level must be marked as a horizontal reference line. The ℓ = 0 curve descends steeply to −∞ as r → 0 and rises from the well monotonically. The ℓ = 1 and ℓ = 2 curves each show a local minimum at finite r (the centrifugal barrier creates a potential well minimum), with the minimum at larger r for larger ℓ. All three curves approach zero from below as r → ∞. The horizontal zero-energy reference line is shown as a thin dashed line spanning the full domain.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Effective radial potential for hydrogen: V_eff(r) = −e²/(4πε₀r) + ℏ²ℓ(ℓ+1)/(2μr²). Three curves for ℓ = 0, 1, 2. ℓ = 0 (s-states): pure Coulomb well, V_eff → −∞ as r → 0, allowing the wave function to reach the nucleus (hyperfine contact term). ℓ = 1: centrifugal term ∝ 2/(2μr²) creates a local minimum at finite r and suppresses the wave function near the origin. ℓ = 2: centrifugal term ∝ 6/(2μr²) pushes the minimum to larger r. Zero-energy reference line separates bound-state region (E < 0) from continuum. The depth and position of the effective potential minimum determine the radial probability peak.

`[O — ORGANIZATION]` Single panel. Horizontal x-axis: r from 0 to 12a₀. Vertical y-axis: V_eff from below zero to above zero; zero energy marked by horizontal dashed reference line. Three curves, each terminating at the left boundary (r = 0.1a₀) to avoid the singularity. ℓ=0 curve descends most steeply at small r; ℓ=1 and ℓ=2 curves show distinct minima at finite r. The three minima are at progressively larger r for larger ℓ.

`[P — PRESENTATION]` Flat vector. ℓ=0 curve: Blue #0072B2, 2pt solid. ℓ=1 curve: Orange #E69F00, 2pt solid. ℓ=2 curve: Bluish Green #009E73, 2pt solid. Zero-energy reference line: light gray, 1pt dashed. Axis lines: light gray, 0.5pt. White background. No baked text; no red-green.

`[E — EXCLUSIONS]` Omit: numerical energy eigenvalue lines (horizontal lines at E_n), actual radial wave functions overlaid, ℓ = 3 or higher curves, comparison to harmonic oscillator or square well, 3D potential energy surface.

**BLOCK 3 — NEGATIVE PROMPT:**
horizontal energy eigenvalue lines, radial wave function curve overlay, ℓ=3 or higher curve, harmonic oscillator comparison curve, square well comparison, 3D surface plot, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Hydrogen Energy Level Diagram with Spectral Series and Selection Rules

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical energy level diagram for hydrogen. The vertical axis represents energy, with the lowest level (n=1) at the bottom and levels n=2, 3, 4, 5 progressively higher, plus a continuum threshold at E=0 at the top. For each n, subdivide horizontally into ℓ sub-levels (ℓ = 0 to n−1 where applicable), with each ℓ column aligned in a separate vertical track labeled by subshell letter (s, p, d, f). Each level is a short horizontal line. Draw transition arrows between levels: solid lines for electric-dipole allowed transitions (Δℓ = ±1), grouping the Lyman series (n → 1), Balmer series (n → 2), and Paschen series (n → 3) by arrow color. Draw one dashed arrow for the forbidden 2s → 1s transition (Δℓ = 0). The arrows are unidirectional (downward, indicating emission). Column tracks share a common energy axis on the left.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Hydrogen energy levels E_n = −13.6 eV/n² for n = 1 to 5, plus continuum (E = 0). For each n: ℓ sub-levels in separate vertical columns for s (ℓ=0), p (ℓ=1), d (ℓ=2), f (ℓ=3). Coulomb degeneracy: all ℓ at fixed n at the same energy. Allowed transitions (Δℓ = ±1): Lyman series (n≥2 → n=1, all p→s transitions), Balmer series (n≥3 → n=2), Paschen series (n≥4 → n=3). Forbidden 2s→1s transition: dashed arrow. Selection rule Δm = 0, ±1 not shown structurally (would require a third dimension). The 2s→1s arrow is labeled with a symbol for two-photon decay (a small doubled arrowhead, no text). Inferred relation: columns for s, p, d, f visually encode ℓ structure even within the same degenerate n shell.

`[O — ORGANIZATION]` Vertical energy axis on far left. Four vertical column tracks for ℓ = 0 (s), 1 (p), 2 (d), 3 (f), each with short horizontal level lines at energies E_n for the applicable n range. Allowed transition arrows slant between adjacent ℓ columns and descend toward lower n. Lyman arrows span from n≥2 p column to n=1 s column. Balmer arrows span n≥3 to n=2. Paschen arrows span n≥4 to n=3. Forbidden 2s→1s dashed arrow descends within the s column. Continuum threshold shown as a dashed horizontal baseline at the top.

`[P — PRESENTATION]` Flat vector. Energy level lines: Blue #0072B2, 1.5pt. Lyman series arrows: Vermillion #D55E00, 1.5pt solid. Balmer series arrows: Bluish Green #009E73, 1.5pt solid. Paschen series arrows: Orange #E69F00, 1.5pt solid. Forbidden 2s→1s arrow: Blue #0072B2, 1pt dashed. Continuum threshold: light gray, 1pt dashed. Energy axis: light gray, 0.5pt. Vertical column separators: light gray, 0.5pt dashed. White background.

`[E — EXCLUSIONS]` Omit: fine structure splittings within each n level, hyperfine splittings, Zeeman sublevel structure, specific wavelength annotations baked into arrowheads, absorption-spectrum representation (upward arrows), n≥6 levels.

**BLOCK 3 — NEGATIVE PROMPT:**
fine structure splitting within n levels, hyperfine splitting sublabels, Zeeman magnetic sublevel lines, wavelength numbers on arrows, absorption upward arrows, n≥6 levels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Orbital Shape Gallery: 2D Cross-Sections |ψ_{nℓm}|² for n = 1, 2, 3

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a 3-column by 3-row grid of 2D heat-map panels, each showing the xz-plane cross-section of |ψ_{nℓm}(x, 0, z)|² for a representative state at n=1, 2, and 3. Each panel is a square heat map with the same spatial scale (±10a₀ × ±10a₀), colored by probability density using a sequential single-hue Viridis-equivalent scale (low density = dark, high density = light). Top row: n=1, ℓ=0, m=0 (spherical blob). Middle row left: n=2, ℓ=0, m=0 (spherical with one radial node ring); middle center: n=2, ℓ=1, m=0 (dumbbell along z-axis); middle right: n=2, ℓ=1, m=±1 (toroidal azimuthal cross-section). Bottom row: n=3, ℓ=0 m=0; n=3, ℓ=1, m=0; n=3, ℓ=2, m=0 (cloverleaf cross-section). All panels share identical axis extent and color scale reset per panel.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background. Grid of up to 9 panels totaling the 89mm width; individual panels ~26mm square. Color scale sequential, rescaled per panel to [0, max(|ψ|²)] per state.

`[C — CONTENT]` Wave function probability densities |ψ_{nℓm}(x, 0, z)|² at y=0 (xz plane) for representative hydrogen states. n=1: (1,0,0) spherically symmetric blob, maximum at origin. n=2: (2,0,0) spherical with radial node ring at r=2a₀; (2,1,0) dumbbell along ẑ axis with two lobes and nodal plane at z=0; (2,1,±1) azimuthally symmetric ring about ẑ with two lobes in xz cross-section. n=3: (3,0,0) two radial node rings; (3,1,0) three-lobe structure along ẑ; (3,2,0) four-lobe cloverleaf pattern in xz plane. Node count = n−1 in each case.

`[O — ORGANIZATION]` 3×3 grid. Rows correspond to n=1 (top, one panel), n=2 (middle, three panels), n=3 (bottom, three panels). Empty cells in n=1 row are blank (white). Panels are square, equal size, with no gap between adjacent panels. Color scale per panel (not global). No axis tick marks; nucleus position (origin) marked by a faint white crosshair in each panel.

`[P — PRESENTATION]` Flat vector rasterized heat map cells using Viridis-equivalent sequential palette (no rainbow, no red-green): dark purple → blue → cyan → yellow at maximum density. White crosshair at origin: 0.5pt, very faint. Panel borders: light gray, 0.5pt. White background surrounding the grid. Color scale not baked into image; domain rescaled per panel.

`[E — EXCLUSIONS]` Omit: real chemistry orbital labels (p_x, p_y) in same panel as complex eigenstates, 3D isosurface renders, n=4 or higher panels, radial probability P(r) overlaid onto 2D heat map, comparison panels from other atoms (helium, lithium).

**BLOCK 3 — NEGATIVE PROMPT:**
3D isosurface render, chemistry orbital dumbbell cartoon, n=4+ panels, radial density line plot overlay, other-atom orbital panels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Shell State Counting: 2n² Degeneracy and Periodic Table Row Lengths

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a horizontal stacked bar chart with four horizontal bars, one per shell (n=1 to n=4), each bar divided into ℓ-subshell segments (s, p, d, f) of width 2(2ℓ+1) reflecting both orbital and spin states. Each ℓ-segment is a distinct Okabe-Ito color, consistent across all rows. The total bar length for each n row equals 2n²: 2, 8, 18, 32. At the right end of each bar, a small icon or filled marker indicates the total count 2n². The y-axis lists the shell labels (K, L, M, N) for n = 1 to 4. The x-axis starts at zero. A thin vertical line at the cumulative totals for the first two rows (2 and 8) aligns with familiar periodic-table row lengths.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` State counting per shell for hydrogen: each shell n contains n² orbital states, 2n² with spin. Shell n=1 (K): s subshell only, 2(2·0+1) = 2 states. Shell n=2 (L): s (2) + p (6) = 8 states. Shell n=3 (M): s (2) + p (6) + d (10) = 18 states. Shell n=4 (N): s (2) + p (6) + d (10) + f (14) = 32 states. Segment widths: s = 2, p = 6, d = 10, f = 14 (in units of number of spin states). These are the row lengths of the periodic table: periods 1 (2 elements), 2 (8), 3 (8 — note: period 3 uses only s and p), 4 (18), etc. The diagram shows the quantum-number origin of the counting without claiming period lengths exactly equal 2n² (period 3 is 8, not 18 — the figure encodes only the shell capacity, not the periodic-table period length).

`[O — ORGANIZATION]` Horizontal stacked bar chart. Four rows, n=1 to n=4 from bottom to top (or top to bottom). Y-axis: shell names. X-axis: total states from 0 to 32, zero-anchored. Within each bar, segments stack left to right: s, then p, then d, then f (if present). Total marker at right end of each bar. Vertical reference lines at x=2, x=8 to connect to period row lengths.

`[P — PRESENTATION]` Flat vector. s-subshell segments: Sky Blue #56B4E9. p-subshell segments: Bluish Green #009E73. d-subshell segments: Orange #E69F00. f-subshell segments: Reddish Purple #CC79A7. Total count markers: Blue #0072B2 filled circles, 3pt radius. Vertical reference lines: light gray, 0.5pt dashed. Axis lines: light gray, 0.5pt. White background. Y-axis from zero.

`[E — EXCLUSIONS]` Omit: actual periodic table layout, element symbols, orbital filling order (Aufbau violates the clean shell structure for higher Z), energy scale on y-axis, comparison to 3D atom, quantum defect corrections for many-electron atoms.

**BLOCK 3 — NEGATIVE PROMPT:**
periodic table layout cells, element symbols or atomic numbers, Aufbau filling arrows, energy scale on y-axis, 3D atom orbital layout, quantum defect corrections, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Radial Probability Density P(r):** STATIC SUFFICIENT. A single smooth curve with two vertical markers is a static quantitative diagram. The key conceptual message — that r_mp and ⟨r⟩ differ because P(r) is right-skewed — is fully legible from a static plot.

**Figure 2 — Effective Potential V_eff(r):** STATIC SUFFICIENT. Three static curves on shared axes convey the ℓ-dependent barrier shape as a structural comparison. No temporal or causal stage sequence is involved.

**Figure 3 — Energy Level Diagram with Spectral Series:** STATIC SUFFICIENT. A transition diagram is a classical static figure type; the series groupings and selection rule (allowed vs. forbidden arrows) are fully readable without animation.

**Figure 4 — Orbital Shape Gallery:** VIDEO CANDIDATE. Criterion: transformation below direct observation — the morphological change as (n, ℓ, m) quantum numbers vary is a continuous spatial transformation (spherical 1s → ringed 2s → dumbbell 2p → cloverleaf 3d) whose connection is hard to see across static panels. A video that animates ℓ increasing from 0 to n−1 at fixed n, showing the angular nodes accumulating and the radial nodes decreasing, makes the node-count rule n−1 = (n−ℓ−1) + ℓ viscerally clear in a way a side-by-side panel cannot. **Recommended video for Chapter 9.**

**Figure 5 — Shell State Counting:** STATIC SUFFICIENT. A horizontal stacked bar chart is a static quantitative lookup; no temporal or causal element is present.
