# CAJAL Figure Report — Chapter 11 — Capstone: The Atom, Built from Simulations

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Orbital Penetration and Energy Ordering: ℓ-Degeneracy Breaking

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a two-panel comparison schematic. Panel A (left, hydrogen): a single vertical energy axis with three degenerate horizontal level bars at the same height, representing 3s, 3p, and 3d — all at the same energy. A label placeholder box above them indicates this is the degenerate Coulomb case. Panel B (right, multi-electron atom): the same three orbital labels but now split into three non-degenerate horizontal bars, with 3s lowest, 3p in the middle, and 3d highest, arranged on the same vertical energy axis. The energy axis starts at zero (bottom). To the right of Panel B, draw three radial probability density sketches — one for 3s (peaked close to the nucleus, with an inner lobe), one for 3p (intermediate peak), one for 3d (peaked far from nucleus, no inner lobe). Connect each sketch to its corresponding level bar with a short horizontal arrow. Shade the inner nuclear region as a small filled circle at the axis origin. All level bars are flat rectangles; all radial sketches are schematic curve outlines (not filled plots); no text is baked in. Both panels share a common vertical energy baseline.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Two-panel layout (A left, B right) with radial probability sketches attached to Panel B, approximately 90 mm tall.
- `[C — CONTENT]` Panel A: hydrogen — 3s, 3p, 3d all degenerate at the same E_n = −13.6 eV/9 level. Panel B: multi-electron atom — degeneracy broken; E(3s) < E(3p) < E(3d). Mechanism: 3s penetrates to nucleus (inner lobe in radial density), sees less screening; 3d excluded by centrifugal barrier, more screened. Radial density sketches: 3s has appreciable inner-lobe probability; 3d has no inner lobe. Nuclear region: small filled disk at r = 0. Label inferred: "inner-lobe penetration → less screening → lower energy."
- `[O — ORGANIZATION]` Two side-by-side panels with a shared left-edge energy axis. Panel A: three degenerate bars at identical height. Panel B: three bars at different heights. Radial probability sketches to the right of Panel B, horizontally aligned with their corresponding bars. Connecting arrows horizontal, right-pointing.
- `[P — PRESENTATION]` Panel A degenerate bars: light gray (all equal). Panel B: 3s bar = Bluish Green `#009E73` (lowest, most penetrating); 3p bar = Sky Blue `#56B4E9` (middle); 3d bar = Orange `#E69F00` (highest, most screened). Centrifugal barrier lobe absence indicated by a flat zero near r=0 on the 3d curve in Vermillion `#D55E00` — schematic only. Radial sketch curves: Blue `#0072B2`. Nuclear disk: Blue `#0072B2`. Energy axis: light gray. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: numerical energy values, quantitative radial wavefunctions R_{nl}(r), Slater shielding constants, explicit hydrogen Bohr radius scale, 2s/2p comparison (keep to n=3 as the clearest case), fine structure, spin-orbit, other quantum numbers.

**BLOCK 3 — NEGATIVE PROMPT:**

quantitative radial wavefunction plots, angular spherical harmonic shapes, 3D orbital lobes, Bohr radius tick marks, numerical energy values baked in, Slater constant tables, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Slater's Rules Grouping and Shielding Constants

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a horizontal strip diagram showing Slater's orbital grouping. The strip runs from left (innermost) to right (outermost) and contains seven labeled group blocks: [1s], [2s,2p], [3s,3p], [3d], [4s,4p], [4d], [4f]. Each block is a flat rectangle with a placeholder label region. Below the strip, draw a shielding contribution diagram for a target electron in the [2s,2p] group: highlight the target group in Sky Blue. To the left of the target, place two contributor blocks — one for the same group and one for the [1s] inner group — each connected to the target group by a short right-pointing arrow. Each arrow has a small rectangular placeholder for the shielding coefficient (0.35 for same group, 0.85 for the next inner shell, 1.00 for deeper shells). To the right of the target, place the outer groups greyed out, indicating their contribution is zero. A separate condensed strip below repeats the same layout for a target electron in the [3d] group, showing all inner groups contributing 1.00 (uniform shielding) and the same-group fraction at 0.35. All group labels and coefficient values are placeholder rectangles; no text is baked in.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Two horizontal strip examples stacked vertically, approximately 80 mm tall.
- `[C — CONTENT]` Slater grouping: [1s], [2s,2p], [3s,3p], [3d], [4s,4p], [4d], [4f] in order. Shielding rules (s/p target): same group = 0.35 (0.30 for 1s partner); next inner shell = 0.85; deeper shells = 1.00; outer groups = 0.00. Shielding rules (d/f target): same group = 0.35; all inner groups = 1.00; outer groups = 0.00. Key distinction: s/p partial penetration (0.85 for n−1 shell) vs. d/f full shielding (1.00 for all inner). Label inferred: "d/f excluded from nucleus by centrifugal barrier → fully screened."
- `[O — ORGANIZATION]` Top: full 7-group strip as reference. Middle: s/p example — target group highlighted, arrows from inner groups with coefficient placeholders, outer groups grayed. Bottom: d/f example — same structure with different coefficient pattern. All strips horizontally aligned.
- `[P — PRESENTATION]` Target group: Sky Blue `#56B4E9`. Same-group shielding arrows: Orange `#E69F00`. n−1 shell arrows (s/p case): Blue `#0072B2`. Deep-shell arrows (1.00 contribution): Bluish Green `#009E73`. d/f inner arrows (all 1.00): Bluish Green `#009E73`. Outer (zero contribution) groups: light gray. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: explicit Z_eff numerical calculations, fluorine/sodium/iron worked examples as separate figures, Hartree-Fock orbital energies, the Madelung filling sequence (that is Figure 3), any atom-specific configurations.

**BLOCK 3 — NEGATIVE PROMPT:**

numerical Z_eff computed values, worked example arithmetic, Hartree-Fock energy levels, Madelung arrow diagram, atomic configuration diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — Madelung Filling Sequence and Period Length Derivation

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a two-part diagram. Part A (left): a diagonal-arrow filling sequence chart showing subshells arranged in a grid. The vertical axis represents increasing principal quantum number n (1 at top to 7 at bottom); the horizontal axis represents ℓ (s=0 at left, p, d, f at right). Plot each subshell as a labeled circle at the corresponding (n, ℓ) grid position. Draw diagonal arrows that sweep from upper-right to lower-left, each arrow collecting the subshells in Madelung order: the first diagonal contains 1s; the second contains 2s; the third contains 2p, 3s; and so on. The arrows are numbered 1, 2, 3, … in sequence. Part B (right): a horizontal bar chart showing period lengths 2, 8, 8, 18, 18, 32. The horizontal axis represents capacity (starts at zero, extends to 32). Each bar is a single horizontal band for one period. The bar for period 1 extends to 2; periods 2 and 3 each extend to 8; periods 4 and 5 each extend to 18; period 6 extends to 32. Each bar is subdivided into colored segments indicating which subshell types (s, p, d, f) contribute. No text is baked in; all labels, numbers, and subshell names are placeholder regions.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Two-part side-by-side layout, approximately 100 mm tall.
- `[C — CONTENT]` Part A: (n, ℓ) grid with circles at each subshell position. Diagonal sweep arrows in Madelung order (lowest n+ℓ first; ties broken by lowest n). Sequence: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p. Part B: bar chart. Y-axis: periods 1–7 (top to bottom). X-axis: capacity, zero-based. Bar segments per period: s segment (capacity 2), p segment (6), d segment (10), f segment (14). Period lengths: 2, 8, 8, 18, 18, 32. Label inferred: "period length = Σ 2(2ℓ+1) over subshells filling in that period."
- `[O — ORGANIZATION]` Part A: grid layout with diagonal arrows sweeping upper-right to lower-left. Part B: horizontal bar chart, one bar per period, bars subdivided by subshell type. Parts A and B separated by a thin vertical divider.
- `[P — PRESENTATION]` Part A circles: s = Blue `#0072B2`; p = Sky Blue `#56B4E9`; d = Orange `#E69F00`; f = Reddish Purple `#CC79A7`. Diagonal arrows: Bluish Green `#009E73`. Part B bars subdivided: s segments = Blue `#0072B2`; p segments = Sky Blue `#56B4E9`; d segments = Orange `#E69F00`; f segments = Reddish Purple `#CC79A7`. Bar chart x-axis starts at zero. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: individual element labels, Madelung exception markers (Cr, Cu) — those belong in Figure 5, energy axis, Slater shielding, Hund's rule content, spin-orbit coupling.

**BLOCK 3 — NEGATIVE PROMPT:**

element symbols, atomic number labels, exception annotations for Cr/Cu, energy level positions, Slater shielding arrows, 3D bar charts, angled perspective, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — Hund's Three Rules: Mechanism and Hierarchy

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a three-row vertical flowchart, one row per Hund's rule. Each row contains three panels: a microstate icon (left), a mechanism arrow (center), and an energy consequence icon (right). Row 1 (Rule 1, maximize S): the microstate icon shows five orbital boxes in a row, each with a single upward arrow — all parallel spins. The mechanism arrow is labeled with a placeholder rectangle. The energy consequence icon is a two-bar energy diagram with the high-S state lower. Row 2 (Rule 2, maximize L): the microstate icon shows electrons in orbitals at maximal m_ℓ separation, illustrated as occupying the outermost m_ℓ values first. The mechanism arrow is a placeholder. The energy consequence icon is a two-bar diagram with higher-L state lower within the same S manifold. Row 3 (Rule 3, determine J): the microstate icon is split into two sub-cases — a less-than-half-filled box (J = |L−S|) and a more-than-half-filled box (J = L+S), illustrated as two small level fans diverging in opposite directions. A caution flag icon (a triangular placeholder) appears in Row 3 indicating "mechanism requires spin-orbit coupling, deferred." All icons are flat rectangle and circle shapes; no text baked in.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Three-row vertical layout, approximately 110 mm tall.
- `[C — CONTENT]` Rule 1: maximize total S → antisymmetric spatial ψ → electrons avoid r₁=r₂ → lower Coulomb repulsion → lowest energy. Rule 2: maximize total L (given S) → electrons orbit same sense → angular avoidance → lower energy (less crisp than Rule 1). Rule 3: J = |L−S| (less-than-half-filled); J = L+S (more-than-half-filled); mechanism = spin-orbit coupling, flagged as deferred. Reliability ordering: Rule 1 most reliable; Rule 3 least. Label inferred: "Rule 3 mechanism deferred to Volume 3 (spin-orbit coupling)."
- `[O — ORGANIZATION]` Three horizontal rows, one per rule, stacked vertically. Each row: microstate icon (left) → mechanism arrow (center) → energy diagram (right). Caution flag on Row 3 right panel. A reliability gradient indicator on the far right margin (solid bar tapering from thick at Rule 1 to thin at Rule 3).
- `[P — PRESENTATION]` Rule 1 row: Bluish Green `#009E73` (most reliable, foundational). Rule 2 row: Sky Blue `#56B4E9`. Rule 3 row: Orange `#E69F00`, with caution flag in Vermillion `#D55E00`. Mechanism arrows: Blue `#0072B2`. Energy bars (lower state): filled; upper state: hollow. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: LS vs. jj coupling regime diagram (that belongs in Volume 3), explicit term-symbol notation, carbon or iron specific worked example (that is Figure 6), the Madelung filling sequence.

**BLOCK 3 — NEGATIVE PROMPT:**

LS vs. jj coupling Feynman diagram, jj coupling level scheme, term symbol notation baked in, spectroscopic term letter labels, worked example atoms, Madelung filling arrows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 5 — Madelung Exceptions: Cr and Cu Exchange Stabilization

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a two-column comparison diagram. Each column represents one element (chromium and copper) and contains two rows: the Madelung-predicted configuration (top row) and the NIST actual configuration (bottom row). Each configuration is depicted as a set of 3d orbital boxes (five boxes in a row) plus a single 4s orbital box to the right, with arrows showing electron filling. In the Madelung-predicted row, chromium shows four filled 3d boxes (↑ ↓ ↑ ↓) and one empty 3d box, with two 4s arrows (↑ ↓). In the actual row, chromium shows five filled 3d boxes (↑ ↑ ↑ ↑ ↑, all parallel) and one 4s box with a single arrow (↑). For copper: Madelung shows nine filled 3d (with one pairing) and two 4s; actual shows ten filled 3d (all paired) and one 4s. A downward energy comparison bar appears to the right of each pair of rows, showing the actual configuration lower in energy than the Madelung prediction by a gap labeled "ΔE_exchange." A small icon at the bottom of each actual-configuration row indicates the stabilization type: a "5/5" symbol for chromium's half-filled subshell and "10/10" for copper's fully-filled subshell — all as placeholder rectangles. No text is baked in.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Two side-by-side element columns, each with two rows (predicted, actual), approximately 90 mm tall.
- `[C — CONTENT]` Chromium (Z=24): Madelung prediction [Ar]3d⁴4s² vs. actual [Ar]3d⁵4s¹. Copper (Z=29): Madelung prediction [Ar]3d⁹4s² vs. actual [Ar]3d¹⁰4s¹. Mechanism: exchange-energy stabilization of half-filled (Cr) or fully-filled (Cu) 3d subshell; each additional parallel-spin pair lowers energy by K > 0. Energy diagram: actual configuration is lower by ΔE_exchange. Label inferred: "exchange stabilization > 3d–4s orbital gap at these Z."
- `[O — ORGANIZATION]` Two columns (Cr left, Cu right). Within each column: top row = Madelung prediction (orbital filling diagram); bottom row = NIST actual. Right of each column: vertical energy comparison bar. Bottom of each actual row: half-filled / fully-filled stabilization icon.
- `[P — PRESENTATION]` Madelung prediction rows: light gray borders. Actual configuration rows: Bluish Green `#009E73` borders (lower energy, correct). Discrepancy highlight: Vermillion `#D55E00` outline on the orbital box that differs between predicted and actual. Energy comparison bars: Blue `#0072B2` for predicted, Bluish Green `#009E73` for actual (lower). Exchange stabilization icon: Orange `#E69F00`. 1 pt strokes, flat vector, white background.
- `[E — EXCLUSIONS]` Omit: other d-block exceptions (Mo, Pd, Ag, etc.), 4d-block content, the 3d/4s crossing energy diagram (that is Figure 6), any s-block or p-block elements, the Slater Z_eff calculation for Cr or Cu.

**BLOCK 3 — NEGATIVE PROMPT:**

4d block elements, molybdenum or palladium diagrams, 3d/4s energy crossing graph, Slater shielding tables, other exception elements, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 6 — 3d/4s Energy Crossing as a Function of Nuclear Charge Z

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a line chart with horizontal axis representing atomic number Z (range approximately 18 to 30, starting at zero or at Z=18 baseline) and vertical axis representing relative orbital energy (starting at zero). Plot two curves: one for the 4s orbital energy and one for the 3d orbital energy as a function of Z across the first transition series. Both curves decrease (become more negative) as Z increases, but the 3d curve drops faster. The two curves cross at approximately Z = 20–21. To the left of the crossing, the 4s curve is lower (4s more stable for neutral K, Ca). To the right, the 3d curve is lower (3d more stable in the cation region). Mark the crossing point with a small circle. Bracket the crossing region with a horizontal bar indicating "transition series Z = 21–29." Mark two vertical dashed reference lines: one at Z = 24 (Cr exception) and one at Z = 29 (Cu exception). The y-axis starts at zero (or at a defined reference). No text is baked in; all annotations are placeholder rectangles or circles.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single-column 89 mm, 300 DPI, SVG/EPS, white background. Single-panel line chart, approximately 70 mm tall. Y-axis starts at zero (or at a defined common reference energy); x-axis covers Z ≈ 18–30.
- `[C — CONTENT]` Two orbital energy curves: E(4s) and E(3d) as functions of Z for neutral atom. Crossing at Z ≈ 20–21 where 4s and 3d energies are approximately equal. For Z < crossing: 4s below 3d (4s fills first, Madelung consistent). For Z > crossing in cation: 3d below 4s (3d lower in ions). Reference dashes at Z=24 (Cr) and Z=29 (Cu). Bracket at transition series range. Label inferred: "orbital energy ordering is not fixed — it depends on occupation and Z."
- `[O — ORGANIZATION]` Single panel. X-axis: Z, left to right, range 18–30. Y-axis: orbital energy (relative), zero at top or at defined baseline, decreasing downward. Two curves. Crossing circle. Two vertical dashed lines. Horizontal bracket above.
- `[P — PRESENTATION]` 4s curve: Blue `#0072B2`. 3d curve: Orange `#E69F00`. Crossing circle: Bluish Green `#009E73`. Dashed reference lines (Cr, Cu): Reddish Purple `#CC79A7`. Axis lines: light gray. Bracket: Sky Blue `#56B4E9`. 1 pt strokes, flat vector, white background. Y-axis zero baseline clearly marked.
- `[E — EXCLUSIONS]` Omit: ionization energy curves, computed Hartree-Fock numeric values as baked labels, relativistic corrections, 4d and 5d block content, s-block elements, Slater Z_eff shielding diagram.

**BLOCK 3 — NEGATIVE PROMPT:**

ionization energy experimental curves, Hartree-Fock computed value annotations, 4d/5d transition series, relativistic mass-velocity correction curves, Slater Z_eff shielding diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Orbital Penetration and Energy Splitting:** STATIC SUFFICIENT. The comparison between degenerate hydrogen levels and split multi-electron levels is a structural before/after; no sequential causal process requires animation. The static two-panel comparison conveys the mechanism fully.

**Figure 2 — Slater's Rules Grouping:** STATIC SUFFICIENT. The grouping and shielding scheme is a fixed classification hierarchy. A static diagram with annotated arrows for each contribution type is sufficient and more legible than animated sequencing.

**Figure 3 — Madelung Sequence and Period Lengths:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages. The Madelung filling sequence involves a step-by-step diagonal sweep through the (n, ℓ) grid, each step adding a subshell and extending the period-length bar. Animating the diagonal arrow advancing subshell by subshell, with the period-length bar growing in real time, would make the algebraic structure of the periodic table viscerally clear — especially the moment when a d subshell enters and extends a period from 8 to 18. **Recommended video for Chapter 11.**

**Figure 4 — Hund's Three Rules Mechanism:** STATIC SUFFICIENT. The three-row flowchart is a static hierarchy with a fixed logical dependency structure, not a temporal or cyclical process. A well-organized static flowchart conveys the hierarchy of rules and their reliability ordering without loss.

**Figure 5 — Madelung Exceptions (Cr, Cu):** STATIC SUFFICIENT. The comparison is a side-by-side structural contrast between predicted and actual filling; no sequential process or cyclical return is involved.

**Figure 6 — 3d/4s Energy Crossing:** STATIC SUFFICIENT. A line chart comparing two curves across a Z axis is a static quantitative display. The crossing is a structural feature of the graph, not a temporal transition, and is adequately conveyed by a static diagram.
