# Simulation Ideas — quantum-mechanics-vol2

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — Bloch Sphere: Qubit State and Single-Axis Rotation
- Source: `quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: |ψ⟩ = cos(θ/2)|↑⟩ + e^(iφ)sin(θ/2)|↓⟩; Bloch vector (sin θ cos φ, sin θ sin φ, cos θ)
- Concrete numbers: |↑⟩ → north pole; |+⟩=(|↑⟩+|↓⟩)/√2 → equator at φ=0; Hadamard maps |↑⟩ to |+⟩ (rotation by π about (x+z)/√2)
- Visual artifact: 3D sphere with labeled poles (|↑⟩, |↓⟩, |+⟩, |−⟩); Bloch vector rotating continuously from pole to equator
- Two testable predictions: P1: |↑⟩ at north pole (θ=0) → measurement outcome ↑ with probability 1; P2: equatorial state (θ=π/2) → ⟨Z⟩=0 (equal superposition)
- Sim slug: medhavy-vol2-bloch-rotation

---

## Sim-02 — Commutators and Uncertainty: Squeezing One Width Stretches the Other
- Source: `quantum-mechanics-vol2/chapters/03-commutators-and-uncertainty.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: σ_x σ_p ≥ ℏ/2; for Gaussian state σ_x σ_p = ℏ/2 (minimum uncertainty)
- Concrete numbers: Gaussian state σ_x = 1 nm → σ_p = ℏ/2/(1 nm) ≈ 5.27×10⁻²⁶ kg·m/s ≈ 0.33 eV/c; squeeze σ_x to 0.5 nm → σ_p doubles
- Visual artifact: two coupled width bars for x and p; dragging one bar in forces the other to expand; product ℏ/2 stays constant
- Two testable predictions: P1: Gaussian ground state of harmonic oscillator saturates the bound (σ_x σ_p = ℏ/2 exactly); P2: squeezing σ_x by factor 2 doubles σ_p
- Sim slug: medhavy-vol2-uncertainty-squeeze

---

## Sim-03 — Hydrogen Radial Probability: Why 1s Mean ≠ Mode
- Source: `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: P(r) = |R₁₀(r)|² · 4πr² = (4/a₀³) r² e^(−2r/a₀); peak at r=a₀, mean at 3a₀/2
- Concrete numbers: Bohr radius a₀ = 0.0529 nm; peak of P(r) at a₀; ⟨r⟩ = 3a₀/2 = 0.0794 nm
- Visual artifact: P(r) curve with two vertical markers — peak at a₀ (green), mean at 1.5 a₀ (orange); the gap between them is visible
- Two testable predictions: P1: P(r) peaks exactly at a₀ (differentiate P'(r)=0 → r=a₀); P2: ⟨r⟩ = 3a₀/2 from the integral (larger than peak)
- Sim slug: medhavy-vol2-hydrogen-radial
- Note: CROSS-REFERENCE — vox-hydrogen-cloud is an explainer in quantum-mechanics-a-companion-guide. This is the simulation workflow reel; build it.

---

## Sim-04 — Capstone: Atomic Orbital Builder (Screening + Energy Ordering)
- Source: `quantum-mechanics-vol2/chapters/11-capstone-the-atom.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E(nl) depends on both n and l through screening; E(ns) < E(np) < E(nd) for multi-electron atoms; Z_eff from Slater's rules
- Concrete numbers: Na (Z=11): 3s at −5.1 eV, 3p at −3.0 eV; gap ≈ 2.1 eV; Slater Z_eff(3s)≈6.6, Z_eff(3p)≈6.1
- Visual artifact: energy level diagram with l-split shells; change Z and watch Z_eff shift; compare hydrogen (no l-split) vs sodium (clear l-split)
- Two testable predictions: P1: hydrogen n=3 shows 3s=3p=3d all degenerate (SO(4) symmetry); P2: sodium n=3 splits: E(3s) < E(3p) < E(3d) by measurable gaps
- Sim slug: medhavy-vol2-orbital-energies
