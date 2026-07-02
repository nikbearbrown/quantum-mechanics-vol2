# Bear's Doodles — Quantum Mechanics, Vol. 2 Video Ideas

*Scouted from the 11 content chapters. Triaged by concept, keeping only ideas where motion teaches the mechanism.*

## Candidate 01 — Why Spin Is Not a Tiny Ball Spinning
- Source: `quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md`
- Production mode: Mixed
- Hook: Spin uses arrows and rotations, but the electron is not a little planet turning in space.
- Core idea: A spin state is a two-outcome quantum direction on the Bloch sphere, and measurement projects that direction rather than revealing a hidden physical rotation.
- Visual object: A Bloch-sphere arrow contrasted with a crossed-out spinning ball.
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: measurement gives two outcomes, vectors can point in directions
- Exclusions: no Pauli-matrix derivation, no Stern-Gerlach hardware history, no spinor representation proof
- Score: 10/10

## Candidate 02 — Why an Electron Cannot Point Fully Along Its Angular Momentum
- Source: `quantum-mechanics-vol2/chapters/06-angular-momentum.md`
- Production mode: Manim visualization
- Hook: Quantum angular momentum has a maximum measured projection, yet the full vector is always longer than that projection.
- Core idea: The vector's total length is set by l(l+1), while any chosen-axis projection tops out at l, so some sideways uncertainty must remain.
- Visual object: A tilted angular-momentum arrow with a maximum z-shadow that never reaches the arrow tip.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: vector length, projection, measurement axis
- Exclusions: no ladder-operator normalization, no commutator proof, no spherical harmonic algebra
- Score: 9/10

## Candidate 03 — Why Measuring Two Compatible Things Feels Like Sorting Twice
- Source: `quantum-mechanics-vol2/chapters/03-commutators-and-uncertainty.md`
- Production mode: Manim visualization
- Hook: Some measurements can be repeated in either order without scrambling each other, while others destroy the sorting you just did.
- Core idea: Compatible observables share eigenstates, so a state can sit in both sorting bins at once; noncommuting observables rotate the bins and force a new split.
- Visual object: Two stacked sorting machines whose slots either align or rotate out of alignment.
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: measurement as sorting, eigenstate as a stable outcome
- Exclusions: no Robertson inequality proof, no abstract domain issues, no full operator algebra
- Score: 9/10

## Candidate 04 — Why Hydrogen Orbitals Are Clouds, Not Orbits
- Source: `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Production mode: Mixed
- Hook: The electron in hydrogen does not circle the proton like a moon, even when the pictures look orbital.
- Core idea: Solving the central-potential wave equation gives stationary probability shapes; the electron's location is a cloud of likelihood, not a path through space.
- Visual object: A circular orbit dissolving into 1s and p-orbital probability clouds.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: probability density, nucleus, wavefunction
- Exclusions: no radial equation derivation, no Laguerre polynomials, no fine structure
- Score: 9/10

## Candidate 05 — Why Identical Electrons Refuse the Same Seat
- Source: `quantum-mechanics-vol2/chapters/10-identical-particles.md`
- Production mode: Mixed
- Hook: Two electrons are so identical that swapping their names changes nothing, and that sameness keeps them from sharing one state.
- Core idea: Fermion wavefunctions change sign under exchange, so putting both electrons in the same state makes the antisymmetric state cancel itself to zero.
- Visual object: Two identical electron seats collapsing to a forbidden zero card when both labels match.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: quantum state, identical particles, sign can cancel
- Exclusions: no Slater determinant formalism beyond the visual cancellation, no helium exchange integral, no full periodic table
- Score: 9/10

## Candidate 06 — Why Adding Two Spins Makes a Triplet and a Singlet
- Source: `quantum-mechanics-vol2/chapters/08-addition-of-angular-momenta.md`
- Production mode: Manim visualization
- Hook: Two spin-half particles do not simply make four unrelated states; three move together and one stands alone.
- Core idea: The coupled basis reorganizes the same four states by total angular momentum, producing a symmetric triplet and an antisymmetric singlet.
- Visual object: Four product-state tiles rearranging into a three-tile triplet stack plus one singlet tile.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: spin up/down, basis change, symmetry
- Exclusions: no Clebsch-Gordan table derivation, no ladder-operator construction details, no spin-orbit application
- Score: 8/10

## Candidate 07 — Why the Fourier Transform Is a Basis Change
- Source: `quantum-mechanics-vol2/chapters/01-the-formalism.md`
- Production mode: Manim visualization
- Hook: Position space and momentum space look like two worlds, but they are the same state described in two bases.
- Core idea: A wavefunction can be expanded in position spikes or momentum waves; the Fourier transform only changes which basis coefficients you read.
- Visual object: One state card rotating between a position-grid basis and a wavelength-stack basis.
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: basis, waves add, momentum relates to wavelength
- Exclusions: no integral-kernel derivation, no rigged Hilbert space, no delta-normalization technicalities
- Score: 8/10

## Candidate 08 — Why Rabi Oscillation Is a Quantum Pendulum
- Source: `quantum-mechanics-vol2/chapters/04-quantum-dynamics-and-the-pictures.md`
- Production mode: Manim visualization
- Hook: Drive a two-level atom at the right frequency and its probability sloshes cleanly between the two states.
- Core idea: Resonant driving continually rotates the state vector, moving probability from ground to excited and back at the Rabi frequency.
- Visual object: A two-level meter sloshing up and down while a Bloch arrow rotates.
- Manim move: slosh
- Short-form fit: Medium
- Prerequisites: two-level system, resonance, probability amplitude
- Exclusions: no rotating-wave approximation derivation, no detuning formula, no interaction-picture machinery
- Score: 8/10

## Candidate 09 — Why Separation of Variables Builds 3D Quantum Shapes
- Source: `quantum-mechanics-vol2/chapters/05-quantum-mechanics-in-three-dimensions.md`
- Production mode: Manim visualization
- Hook: A three-dimensional wave problem becomes solvable by splitting one impossible shape into three linked pieces.
- Core idea: Symmetry lets the wavefunction factor into radial and angular parts, and each part contributes one quantum number to the final shape.
- Visual object: A 3D orbital decomposing into radial rings and angular lobes, then recombining.
- Manim move: split
- Short-form fit: Medium
- Prerequisites: wavefunction, coordinates, multiplication as combining factors
- Exclusions: no full spherical-coordinate Laplacian derivation, no special functions, no normalization constants
- Score: 7/10

## Candidate 10 — Why the Madelung Rule Is a Pattern, Not a Law
- Source: `quantum-mechanics-vol2/chapters/11-capstone-the-atom.md`
- Production mode: Doodle
- Hook: The periodic table looks like electrons fill boxes by a simple rule, until real atoms start cheating.
- Core idea: Screening and electron-electron interactions shift orbital energies, so the filling order is a useful pattern with exceptions rather than a theorem.
- Visual object: Electrons queueing for orbital boxes while some boxes slide up and down.
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: shells, orbitals, electron filling
- Exclusions: no Hartree-Fock calculation, no term symbols, no full transition-metal exception catalog
- Score: 7/10
