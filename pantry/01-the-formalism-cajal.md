# CAJAL Figure Report — Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

Recommended: 4 figures, Mixed density.

---

## Figure 1 — State vs. Its Representations (Three-Basis Fan)

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single abstract vector arrow labeled with a generic state symbol at the center of the composition. From that central vector, draw three diverging projection lines, each terminating at a distinct column-like representation: a smooth continuous wave profile (position-space amplitude function), a second smooth continuous wave profile with different width and oscillation (momentum-space amplitude function), and a vertical bar-chart-style column of discrete values (energy-basis coefficients). Each projection line should be clearly directional, going from the central vector outward to the representation. The three representations sit at roughly equal angular spacing, with the central vector visually dominant. Use flat vector style with a white background. The connection from central object to each peripheral representation should be drawn as a clean solid arrow or projection line. No text baked into the image.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Landscape-compatible if needed.

`[C — CONTENT]` One abstract ket vector (central object). Three projection relationships: (1) projection onto position-basis yielding a position-space wave function (broad smooth curve), (2) projection onto momentum-basis yielding a momentum-space wave function (narrower, faster-oscillating curve), (3) projection onto discrete energy-basis yielding a bar-chart sequence of coefficients. The projections are the inner-product relations ⟨x|ψ⟩, ⟨p|ψ⟩, ⟨E_n|ψ⟩. Each projection is a one-way directed relation (central → peripheral). The three representations must be visually distinct in form: continuous wide curve, continuous narrow/oscillatory curve, discrete bars.

`[O — ORGANIZATION]` Hub-and-spoke layout. Central vector at hub; three representation panels arranged radially at ~120° spacing. Projection arrows point outward from center. No hierarchy implied among the three representations—all are peers. The central vector is largest/most prominent element.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Central ket arrow: Blue `#0072B2`. Position-space curve: Sky Blue `#56B4E9`. Momentum-space curve: Orange `#E69F00`. Energy-basis bars: Bluish Green `#009E73`. Projection arrows: neutral light gray. Uniform 1 pt strokes. White background. No baked text.

`[E — EXCLUSIONS]` Omit: time evolution, Hamiltonian, Schrödinger equation, normalization integrals, specific functional forms (Gaussian, sinc, etc.), Dirac delta functions, the Fourier transform formula, the completeness relation formula, any bra symbol objects, measurement/Born rule. Do not show an actual coordinate axis with tick marks on the wave functions—stylized wave profile shapes only.

**BLOCK 3 — NEGATIVE PROMPT:**
coordinate axes with tick marks, bra vectors, Fourier transform diagram, frequency-domain labeling, time-evolution arrow, measurement collapse, normalization symbols, specific functional waveform labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Completeness Insertion Mechanism (Three-Step Chain)

**Heuristic:** MC | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Depict a horizontal three-panel sequential diagram showing the completeness-insertion technique. In the leftmost panel, show two abstract bracket symbols flanking an empty gap—representing an abstract inner product with a blank in the middle. In the center panel, insert a vertical stack of outer-product objects (a column of paired arrow symbols, representing the identity operator written as a sum of projectors) filling the gap. In the rightmost panel, show the result as a horizontal chain of overlapping bracket pairings—a sequence of connected inner products. Use directional arrows between the three panels to show the progression from left to right. Each panel should be visually distinct but connected by the same horizontal flow. Use flat vector, no text baked in.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.

`[C — CONTENT]` Three-stage horizontal process: Stage 1 — abstract inner product with gap (two abstract bracket objects with space between them). Stage 2 — identity operator inserted: a vertical stack of outer-product pairs filling the gap, representing ∑_n |n⟩⟨n| = Î. Stage 3 — result: a chain of paired inner products, one per basis element, representing ∑_n ⟨φ|n⟩⟨n|ψ⟩. Directed flow arrows connect Stage 1 → Stage 2 → Stage 3. The key visual: the gap being filled by a structured object that then "expands" into a chain.

`[O — ORGANIZATION]` Left-to-right horizontal flow, three roughly equal panels. Inward arrow from Stage 1 into Stage 2 (insertion), outward arrow from Stage 2 into Stage 3 (expansion). Panel separators as light gray vertical rules. The middle panel (identity insertion) visually taller/more prominent to mark it as the active step.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Abstract brackets in Stage 1: Blue `#0072B2`. Identity stack in Stage 2: Reddish Purple `#CC79A7` (composite/bridging object). Chain elements in Stage 3: Sky Blue `#56B4E9` (⟨φ|n⟩ terms) and Bluish Green `#009E73` (⟨n|ψ⟩ terms), alternating in the chain. Flow arrows: neutral gray. Uniform 1 pt strokes. White background. No baked text.

`[E — EXCLUSIONS]` Omit: specific basis types (position, momentum, energy), sigma/integral notation, wave function profiles, bra-ket algebra steps not shown in the three stages, commutator, adjoint operation, matrix elements. Do not show continuous basis (integral version)—discrete sum only.

**BLOCK 3 — NEGATIVE PROMPT:**
position basis eigenstates, momentum eigenstates, wave function curves, integral signs, summation symbols baked in, matrix grid, commutator bracket, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Operator vs. Matrix: Same Operator, Two Bases

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a central abstract operator symbol (a rounded-rectangle or cloud shape representing the operator as a basis-independent object). From this central object, draw two branches downward: one to a diagonal matrix grid on the left, and one to a tridiagonal matrix grid on the right. The diagonal matrix has large filled circles only on the main diagonal (all off-diagonal positions empty or faint). The tridiagonal matrix has filled circles on the main diagonal and the two adjacent diagonals, with empty positions elsewhere. Both matrix grids should have the same overall size. A bidirectional curved arrow between the two matrices at the bottom indicates they represent the same object in different bases. The central operator object connects to both matrices via downward directed arrows. Use flat vector, no baked text.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Portrait orientation.

`[C — CONTENT]` Central object: abstract operator (basis-independent). Left branch: matrix representation in position basis—diagonal structure (filled cells on diagonal only), representing the position operator being multiplicative in position basis. Right branch: matrix representation in energy basis—tridiagonal structure (filled cells on main diagonal and adjacent diagonals), representing the same position operator in the harmonic-oscillator energy eigenbasis. Bottom arc: bidirectional curved arrow connecting the two matrices labeled as "same eigenvalues" (inferred relationship—mark as inferred). Branch arrows: directed downward from central operator to each matrix, labeled as "basis change" (inferred).

`[O — ORGANIZATION]` Hierarchical: single operator at top center; two matrices below at ~45° diverging angles. Bottom arc connecting the two matrices. 4×4 or 5×5 grid cells sufficient to show the sparsity pattern; exact dimension unimportant. Left matrix: position-basis label region (no text). Right matrix: energy-basis label region (no text).

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Central operator object: Blue `#0072B2` fill, 1 pt stroke. Left matrix filled cells: Sky Blue `#56B4E9`. Right matrix filled cells: Orange `#E69F00`. Empty matrix cells: light gray outline only. Branch arrows: neutral gray. Bottom arc arrow: Reddish Purple `#CC79A7` (connecting, composite role). White background. No baked text.

`[E — EXCLUSIONS]` Omit: specific matrix entries or numbers, momentum operator, adjoint or Hermitian condition, eigenvalue equations, unitary transformation formula U†OU, wave function, Bloch sphere, spin operators. Show structural sparsity pattern only—no numerical values in cells.

**BLOCK 3 — NEGATIVE PROMPT:**
numerical matrix entries, eigenvalue equations, unitary rotation symbols, wave function curves, adjoint dagger symbol, spin matrices, momentum operator, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Energy-Basis Probability Bar Chart (Worked Example Coefficients)

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical bar chart with the horizontal axis representing discrete energy quantum numbers (odd integers: 1, 3, 5, 7, 9) and the vertical axis representing probability (squared coefficient magnitude), running from zero at the bottom. Each bar is a solid filled rectangle. The bar heights follow a rapidly decreasing sequence proportional to 1/n^6 for odd n: the n=1 bar is by far the tallest (approximately 0.999 of total probability), the n=3 bar is much shorter (roughly 0.001), and bars for n=5 and beyond are nearly zero (very short stubs). All bars are the same width. The y-axis starts strictly at zero. Show at minimum 5 bars. Use flat vector style, white background, no baked text.

**BLOCK 2 — FULL SCOPE:**

`[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Portrait orientation (taller than wide).

`[C — CONTENT]` Horizontal axis: discrete quantum number n = 1, 3, 5, 7, 9 (odd only; even modes have zero probability and should be absent or shown as absent gaps). Vertical axis: probability |c_n|^2 starting at zero. Bar heights proportional to 960/(n^6 π^6) × π^6 = 960/n^6, normalized so total ≈ 1. Approximate bar values: n=1: ≈0.9986, n=3: ≈0.00137, n=5: ≈0.000154, n=7: ≈0.0000287, n=9: ~negligible. The dominant visual is the steep drop from n=1 to n=3. The chart illustrates that the parabolic state is almost entirely in the ground state.

`[O — ORGANIZATION]` Conventional vertical bar chart. Y-axis from 0 to 1 (or slightly above the tallest bar). X-axis: quantum number positions equally spaced, gaps at even n positions (no bar, just empty space). Bars narrow relative to spacing. No gridlines (or very faint). Axis lines as thin rules.

`[P — PRESENTATION]` Flat vector, Okabe-Ito palette. All bars: Blue `#0072B2`. Axis lines and ticks: neutral gray at 1 pt. Y-axis starts at zero (hard rule). No 3D. No gradients. White background. No baked text.

`[E — EXCLUSIONS]` Omit: energy values on axis (only quantum number n), continuous probability distribution, wave function profile, momentum-space representation, time dependence, any bar for even n, any secondary y-axis, error bars.

**BLOCK 3 — NEGATIVE PROMPT:**
continuous probability curve, wave function overlay, momentum space, even-n bars, energy values on axis, error bars, secondary axis, logarithmic scale, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — State vs. Its Representations:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The conceptual move—a single abstract vector projecting onto three different bases to yield three different-looking but informationally equivalent representations—is precisely the transformation the student needs to internalize. A brief animation showing the single vector fixed at center while three projections "unfold" outward in sequence, then all three held simultaneously, makes the simultaneity and basis-independence visceral in a way a static diagram cannot. Recommended video for the chapter.

**Figure 2 — Completeness Insertion Mechanism:** STATIC SUFFICIENT. The three-stage chain is a logical sequence but not a causal process with continuous motion; a static left-to-right flow diagram communicates the insertion step adequately.

**Figure 3 — Operator vs. Matrix:** STATIC SUFFICIENT. The contrast between two static matrix patterns connected to one central object is naturally conveyed in a side-by-side static diagram. Animation adds nothing beyond what a good static figure shows.

**Figure 4 — Energy-Basis Bar Chart:** STATIC SUFFICIENT. A static bar chart fully encodes the quantitative spectral composition. The steep dominance of n=1 is immediately visible. No sequential or cyclic process is involved.

**Chapter recommended video:** Figure 1 — State vs. Its Representations.
