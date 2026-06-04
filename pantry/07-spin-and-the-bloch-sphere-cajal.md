# CAJAL Figure Report — Chapter 7 — Spin and the Bloch Sphere

Recommended: 5 figures, Mixed density.

---

## Figure 1 — Bloch Sphere: State Parametrization and Born-Rule Geometry

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a unit sphere in isometric three-quarter view with a vertical axis labeled at the top pole and bottom pole. Place a solid directional arrow from the center to a point on the upper hemisphere, defined by polar angle θ measured from the vertical axis and azimuthal angle φ measured around the equatorial plane. Place a second solid directional arrow from the center to a point on the equator, representing the analyzer direction. Mark the angle γ between the two arrows at the center. Divide the sphere with a thin equatorial circle and two faint longitude arcs. Mark the top pole, the bottom pole, and the equatorial band as three distinct regions. Show the angle θ/2 in an inset arc near the state arrow, emphasizing that the Born-rule probability uses the half-angle. All arrows are flat vector with uniform 1pt strokes; poles and equatorial region are filled with distinct Okabe-Ito colors.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Unit sphere representing the pure-state space of a spin-½ system. North pole = |↑⟩ eigenstate of Ŝ_z with eigenvalue +ℏ/2. South pole = |↓⟩ eigenstate with eigenvalue −ℏ/2. Equatorial circle = equal-superposition states (|↑⟩ + e^{iφ}|↓⟩)/√2. State arrow (Bloch vector) defined by spherical angles (θ_ψ, φ_ψ); analyzer arrow defined by (θ_n, φ_n). Angle γ between the two Bloch vectors shown at center. Half-angle θ/2 indicated on the state arrow to signal P(+) = cos²(γ/2). Inferred relation: the geometric angle γ on the sphere directly encodes the Born-rule probability.

`[O — ORGANIZATION]` Isometric three-quarter view; vertical axis is the Ŝ_z quantization axis. State arrow in upper hemisphere, analyzer arrow on or near equator. γ arc drawn between the two arrows at sphere center. Equatorial band shaded as a neutral-gray ring to mark the equal-superposition zone. North and south poles marked with filled circles.

`[P — PRESENTATION]` Flat vector. State arrow: Sky Blue #56B4E9. Analyzer arrow: Orange #E69F00. North pole marker: Bluish Green #009E73. South pole marker: Vermillion #D55E00. Equatorial band: light gray. Sphere outline: Blue #0072B2, 1pt. γ arc and half-angle arc: Reddish Purple #CC79A7, 1pt dashed. White background. No baked text, no red-green.

`[E — EXCLUSIONS]` Omit: mixed states (interior of sphere), density matrix, Wigner function, spin-1 or higher-spin analogues, complex spinor components, SU(2) group manifold labeling, coordinate grid lines beyond equatorial circle and two meridians.

**BLOCK 3 — NEGATIVE PROMPT:**
interior density-matrix blob, mixed-state interior points, spin-1 geometry, Wigner function, complex component arrows, SU(2) fiber bundle notation, coordinate grid crowding, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Sequential Stern–Gerlach Experiment: Three-Stage Noncommutativity

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a horizontal left-to-right process diagram with three rectangular apparatus blocks and two beam-path segments between them. The first apparatus block deflects an incoming beam into two output paths; one path (lower) terminates at a filled stop symbol, the surviving path (upper) continues rightward. The second apparatus block, rotated 90° relative to the first (indicating a perpendicular measurement axis), deflects the surviving beam into two equal paths; one path (lower) terminates at a second stop symbol, the surviving path (upper) continues. The third apparatus block, oriented identically to the first, deflects the surviving beam into two equal-amplitude output paths, both unblocked. Each apparatus block is a simple flat rectangle with one input arrow on the left and two output arrows on the right, separated by angle. Beam paths are single-weight solid lines; stopped paths end in filled circles. The three apparatus blocks are in three distinct Okabe-Ito colors.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Three sequential Stern–Gerlach (SG) apparatuses. SG₁: measures Ŝ_z; two output beams (spin-up and spin-down along z); spin-down beam blocked. SG₂: measures Ŝ_x (perpendicular to SG₁); two output beams (spin-up and spin-down along x); spin-down-along-x beam blocked. SG₃: measures Ŝ_z again; two output beams of equal intensity emerge, demonstrating that the definite Ŝ_z from SG₁ is not preserved through SG₂. The 50/50 outcome at SG₃ follows from [Ŝ_x, Ŝ_z] ≠ 0, not from mechanical disturbance. Beam intensity proportional to path thickness is an inferred visual encoding (not stated numerically in diagram text).

`[O — ORGANIZATION]` Left-to-right flow. SG₁ → blocked lower path + surviving upper path → SG₂ → blocked lower path + surviving upper path → SG₃ → two equal output paths. Apparatus blocks aligned on a shared horizontal baseline. Stop symbols (filled circles) at each blocked exit. Progression marker → at each stage transition.

`[P — PRESENTATION]` Flat vector. SG₁ apparatus: Blue #0072B2. SG₂ apparatus: Orange #E69F00. SG₃ apparatus: Blue #0072B2 (same as SG₁, emphasizing it measures the same axis). Surviving beam paths: Sky Blue #56B4E9, 1.5pt. Blocked paths leading to stops: Vermillion #D55E00, 1pt dashed. Stop symbols (filled circles): Vermillion #D55E00. Equal output paths at SG₃: Sky Blue #56B4E9, equal width, both solid. White background.

`[E — EXCLUSIONS]` Omit: classical hidden-variable diagram as a separate parallel panel, magnetic field gradient arrows inside apparatuses, atom trajectories, force vectors, quantum eraser variants, four-stage sequences, SG apparatus for spin-1.

**BLOCK 3 — NEGATIVE PROMPT:**
magnetic field gradient arrows, classical hidden-variable parallel diagram, atom trajectory arcs, force vectors, quantum eraser apparatus, four-stage variant, spin-1 apparatus, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Larmor Precession: Bloch Vector Tracing a Latitude Circle

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a unit sphere in isometric three-quarter view with a vertical magnetic field arrow above the north pole. Place a Bloch vector arrow from the center to a point on the upper hemisphere at fixed polar angle θ₀ from the vertical axis. Show three successive positions of the Bloch vector at equal azimuthal intervals, connected by a dashed circular arc at constant latitude θ₀ — the precession path. The circular arc lies in a horizontal plane cutting the sphere. Show a small curved arrow at the equatorial level indicating the direction of precession (counterclockwise from above for positive gyromagnetic ratio). The vertical axis carries a small arrow indicating the field direction. The Bloch vector's projection onto the vertical axis (proportional to ⟨Ŝ_z⟩) is shown as a vertical dashed line segment from the tip of the vector down to the equatorial plane, constant in length across all three vector positions.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Spin-½ state in uniform field B₀ẑ. Bloch vector at fixed polar angle θ₀ precesses around ẑ at Larmor frequency ω_L = γB₀. Three snapshots of the Bloch vector at azimuths φ = 0, 2π/3, 4π/3 (equally spaced). Latitude circle (precession path) at elevation θ₀. Vertical projection of Bloch vector = ⟨Ŝ_z⟩ = (ℏ/2)cosθ₀ = constant (conserved quantity). Magnetic field arrow above north pole represents B₀ẑ. Precession direction arrow at equatorial level.

`[O — ORGANIZATION]` Isometric three-quarter sphere. Vertical (ẑ) axis prominent. Three Bloch vector arrows equally spaced in azimuth at same θ₀. Latitude dashed arc connecting the three tips. Vertical dashed drop-line from each vector tip to equatorial plane (all equal length). Curved precession-direction arrow near equator.

`[P — PRESENTATION]` Flat vector. Bloch vector arrows: Sky Blue #56B4E9, 1.5pt. Latitude precession arc: Orange #E69F00, 1pt dashed. B₀ field arrow above pole: Blue #0072B2, 1.5pt. Vertical projection drop-lines: Bluish Green #009E73, 1pt dashed. Precession-direction curved arrow: Reddish Purple #CC79A7, 1pt. Sphere outline: light gray, 1pt. White background.

`[E — EXCLUSIONS]` Omit: NMR pulse sequences, rotating frame, relaxation (T1/T2), energy-level diagram, Hamiltonian matrix, multiple particles, spin-echo diagrams.

**BLOCK 3 — NEGATIVE PROMPT:**
NMR pulse sequence diagram, rotating reference frame arrow, T1/T2 relaxation curves, energy-level ladder, multiple-particle spin arrows, spin-echo envelope, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Stern–Gerlach Experimental Outcome: Two Spots vs. Classical Smear

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-panel comparison using a shared vertical axis. Left panel: a continuous vertical smear of silver atoms on a glass plate surface, representing the classical prediction — a smooth gradient stripe from top to bottom. Right panel: two discrete compact spots on the same glass plate surface, positioned symmetrically above and below the center line, representing the actual quantum outcome. Both panels show the same glass plate shape (a thin rectangular slab in isometric view) with the same spatial scale. The smear in the left panel is rendered as a gradient band; the two spots in the right panel are solid filled circles. A thin vertical midline on each plate marks the zero-deflection position. No magnetic field apparatus is shown.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Comparison of classical prediction (continuous deflection smear) with observed quantum outcome (two discrete spots) for silver atoms in an inhomogeneous magnetic field. Silver has a single 5s valence electron with ℓ = 0; the two spots arise from spin-½ intrinsic angular momentum with eigenvalues ±ℏ/2. Left plate: classical outcome — continuous smear from maximum-downward to maximum-upward deflection. Right plate: quantum outcome — two spots, one above and one below center, nothing between. Inferred visual comparison: the spatial separation of the two spots directly encodes the two eigenvalues of Ŝ_z.

`[O — ORGANIZATION]` Side-by-side panels separated by a vertical gap. Shared horizontal baseline. Both plates same size and orientation. Smear panel on left; spot panel on right. Center-line indicator (thin horizontal tick) on each plate at the zero-deflection position. The two spots on the right plate are equidistant from the center line.

`[P — PRESENTATION]` Flat vector. Classical smear: gradient from light gray at edges to Blue #0072B2 at center band, representing continuous distribution. Upper spot: Bluish Green #009E73, filled circle, 4pt radius. Lower spot: Vermillion #D55E00, filled circle, 4pt radius. Plate bodies: light gray. Center-line ticks: Orange #E69F00, 0.5pt. Panel dividing gap: white. White background.

`[E — EXCLUSIONS]` Omit: magnetic pole pieces, field gradient arrows, beam source, oven, collimator slits, silver atom symbols, multiple species comparisons, spin-1 three-spot analogue.

**BLOCK 3 — NEGATIVE PROMPT:**
magnetic pole pieces, gradient field arrows, beam source oven, collimator slits, atomic symbol labels, spin-1 three-spot diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Larmor Frequency vs. Field Strength: Proton MRI Operating Points

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single horizontal bar chart with four horizontal bars of increasing length, one per row. Each bar represents a clinical or research MRI field strength setting. The x-axis starts at zero and extends to approximately 300 MHz. The y-axis lists the four field-strength settings from bottom to top in increasing order of field strength. Each bar is a solid flat rectangle. A small filled circle at the tip of each bar marks the exact Larmor frequency value. The bars are colored with a single Okabe-Ito hue progressing from lighter to darker as field strength increases, encoded within a single-hue ramp (not a rainbow).

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector SVG/EPS, white background.

`[C — CONTENT]` Proton Larmor frequency f_L = γ_p/(2π) × B₀ at four clinical MRI field strengths. Data from chapter table: B₀ = 0.5 T → f_L = 21.29 MHz; B₀ = 1.5 T → f_L = 63.87 MHz; B₀ = 3.0 T → f_L = 127.74 MHz; B₀ = 7.0 T → f_L = 298.06 MHz. Gyromagnetic ratio γ_p/(2π) = 42.58 MHz/T (proton). Relationship is linear: f_L ∝ B₀.

`[O — ORGANIZATION]` Horizontal bar chart. Y-axis: four rows for the four field-strength settings, ordered from lowest (top row nearest origin) to highest. X-axis: Larmor frequency from 0 to 320 MHz, zero-anchored. Bars extend left-to-right. Tip markers at each bar end. No gridlines beyond the zero baseline.

`[P — PRESENTATION]` Flat vector. Bars: single-hue ramp in Blue family — lightest bar (0.5 T): Sky Blue #56B4E9; darkest bar (7.0 T): Blue #0072B2; intermediate bars interpolated. Tip markers: Orange #E69F00 filled circles, 3pt radius. Axis lines: light gray, 0.5pt. Zero baseline: Blue #0072B2, 1pt. White background. No baked text, no red-green.

`[E — EXCLUSIONS]` Omit: electron gyromagnetic ratio bars, other nuclei (¹³C, ¹⁹F, etc.), 3D bar chart, secondary y-axis for period, error bars, shaded confidence intervals.

**BLOCK 3 — NEGATIVE PROMPT:**
electron gyromagnetic ratio comparison bar, other nuclear species bars, 3D bar extrusion, period secondary axis, error bars, confidence shading, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Bloch Sphere State Parametrization:** STATIC SUFFICIENT. The sphere geometry is a fixed structural map; the learning target is reading off coordinates and applying the Born rule from a static diagram. No transition mechanism is the core learning target.

**Figure 2 — Sequential Stern–Gerlach Experiment:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages where each stage's output state is the input to the next, and the causal logic (operator noncommutativity producing 50/50 at the final stage) is the learning target. A static panel can show all three apparatuses, but the moment-by-moment conditional collapse — state entering SG₂ as definite |↑_z⟩, exiting as |↑_x⟩, then entering SG₃ — is a three-stage causal sequence whose temporal unfolding makes the noncommutativity argument substantially clearer than a side-by-side static layout. **Recommended video for Chapter 7.**

**Figure 3 — Larmor Precession:** STATIC SUFFICIENT. Three snapshot positions on the latitude circle convey the precession path without animation; the key insight (θ frozen, φ advancing) is readable from a static three-snapshot diagram. Transition mechanism is simple circular motion, not the learning target itself.

**Figure 4 — Stern–Gerlach Two-Spot Outcome:** STATIC SUFFICIENT. A two-panel comparison (smear vs. two spots) is a single structural claim, fully readable as a static side-by-side.

**Figure 5 — Larmor Frequency Bar Chart:** STATIC SUFFICIENT. A horizontal bar chart of four data points is a static quantitative lookup; no temporal or process element is present.
