"""
Generate all 11 missing figures for quantum-mechanics-vol2.
Run from the images/ directory:
    cd .../images && python3 _generate_missing_figs.py
House style: figsize=(7,3.6), dpi=200, white bg, top/right spines off,
             mathtext labels, descriptive title at top.
No scipy — all special functions implemented with numpy.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.patches import FancyArrowPatch, Arc, FancyBboxPatch
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FIGSIZE = (7, 3.6)
DPI = 200
TAB = plt.rcParams["axes.prop_cycle"].by_key()["color"]   # tab10 colours


def savefig(name):
    path = os.path.join(OUT, name)
    plt.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  wrote {name}")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 2.1  Geometric diagram in a 2-D Hilbert space
# ─────────────────────────────────────────────────────────────────────────────
def fig_02_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.set_aspect("equal")
    ax.set_xlim(-0.15, 1.55)
    ax.set_ylim(-0.15, 1.35)
    ax.axis("off")

    # Basis vectors: |a1> along x, |a2> along y
    a1 = np.array([1.2, 0.0])
    a2 = np.array([0.0, 1.1])
    # State vector |psi>
    psi = np.array([0.75, 0.85])

    arrow_kw = dict(length_includes_head=True, head_width=0.04, head_length=0.04,
                    linewidth=1.5)

    # Basis axes (thin grey)
    ax.annotate("", xy=a1 * 1.15, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="0.6", lw=1.0))
    ax.annotate("", xy=a2 * 1.15, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="0.6", lw=1.0))

    # Projections (dashed drop-lines)
    proj1 = np.array([psi[0], 0.0])
    proj2 = np.array([0.0, psi[1]])
    ax.plot([psi[0], psi[0]], [0, psi[1]], "--", color=TAB[0], lw=1.0, alpha=0.7)
    ax.plot([0, psi[0]], [psi[1], psi[1]], "--", color=TAB[1], lw=1.0, alpha=0.7)

    # Projection vectors P1|psi> and P2|psi>
    ax.annotate("", xy=proj1, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=TAB[0], lw=2.0))
    ax.annotate("", xy=proj2, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=TAB[1], lw=2.0))

    # State vector |psi>
    ax.annotate("", xy=psi, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=2.2))

    # Labels
    fs = 13
    ax.text(psi[0] + 0.05, psi[1] + 0.04, r"$|\psi\rangle$", fontsize=fs, color="k")
    ax.text(a1[0] * 1.17, a1[1] - 0.07, r"$|a_1\rangle$", fontsize=fs, color="0.5")
    ax.text(a2[0] - 0.14, a2[1] * 1.12, r"$|a_2\rangle$", fontsize=fs, color="0.5")
    ax.text(proj1[0] * 0.42, -0.10,
            r"$\hat{P}_1|\psi\rangle$", fontsize=11, color=TAB[0], ha="center")
    ax.text(-0.13, proj2[1] * 0.5,
            r"$\hat{P}_2|\psi\rangle$", fontsize=11, color=TAB[1], ha="right")

    # Origin dot
    ax.plot(0, 0, "ko", ms=4)

    # Annotation: Born rule
    ax.text(1.0, 0.18,
            r"$\mathrm{Prob}(a_1)=\|\hat{P}_1|\psi\rangle\|^2$",
            fontsize=9.5, color=TAB[0],
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=TAB[0], alpha=0.85))
    ax.text(0.05, 1.22,
            r"$\mathrm{Prob}(a_2)=\|\hat{P}_2|\psi\rangle\|^2$",
            fontsize=9.5, color=TAB[1],
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=TAB[1], alpha=0.85))

    ax.set_title("Figure 2.1 — Born rule as geometry in a 2D Hilbert space",
                 fontsize=11, pad=6)
    savefig("02-observables-and-the-spectral-theorem-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 3.1  Three-column: commuting ops, non-commuting ops, CSCO
# ─────────────────────────────────────────────────────────────────────────────
def fig_03_01():
    fig, axes = plt.subplots(1, 3, figsize=FIGSIZE)
    fig.suptitle(
        "Figure 3.1 — Commuting operators share an eigenbasis; non-commuting ones cannot",
        fontsize=10)

    def draw_box(ax, lines, color, title, title_color="k"):
        ax.axis("off")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.add_patch(FancyBboxPatch((0.04, 0.04), 0.92, 0.92,
                                    boxstyle="round,pad=0.02",
                                    linewidth=1.5, edgecolor=color, facecolor="#f8f8ff"))
        ax.text(0.5, 0.92, title, ha="center", va="top", fontsize=9.5,
                color=title_color, fontweight="bold")
        for i, (txt, fs) in enumerate(lines):
            ax.text(0.5, 0.72 - i * 0.175, txt, ha="center", va="center",
                    fontsize=fs)

    # Left: commuting
    draw_box(axes[0],
             [(r"$[\hat{A},\hat{B}]=0$", 11),
              (r"Shared eigenbasis", 9),
              (r"$\hat{A}|a,b\rangle=a|a,b\rangle$", 9),
              (r"$\hat{B}|a,b\rangle=b|a,b\rangle$", 9)],
             TAB[2], "Commuting", TAB[2])

    # Middle: non-commuting
    draw_box(axes[1],
             [(r"$[\hat{A},\hat{B}]\neq 0$", 11),
              (r"No shared eigenbasis", 9),
              (r"$\sigma_A\sigma_B\geq\frac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$", 8.5),
              (r"cannot both be sharp", 9)],
             TAB[3], "Non-commuting", TAB[3])

    # Right: hydrogen CSCO
    draw_box(axes[2],
             [(r"Hydrogen CSCO", 9),
              (r"$\{\hat{H},\hat{L}^2,\hat{L}_z\}$", 11),
              (r"Labels state $|n,\ell,m\rangle$", 9),
              (r"all three commute", 9)],
             TAB[0], r"Example: H atom CSCO", TAB[0])

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    savefig("03-commutators-and-uncertainty-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 3.2  Side-by-side: xp and px orderings, product-rule cancellation
# ─────────────────────────────────────────────────────────────────────────────
def fig_03_02():
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)
    fig.suptitle(
        r"Figure 3.2 — Deriving $[\hat{x},\hat{p}]=i\hbar$: the two orderings side by side",
        fontsize=10)

    highlight = "#ffe066"  # yellow highlight for the extra term

    def panel(ax, title, lines, color):
        ax.axis("off")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.add_patch(FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                                    boxstyle="round,pad=0.02",
                                    lw=1.4, edgecolor=color, facecolor="white"))
        ax.text(0.5, 0.95, title, ha="center", va="top",
                fontsize=10, fontweight="bold", color=color)
        y = 0.80
        for txt, bg in lines:
            fc = highlight if bg else "white"
            ax.text(0.5, y, txt, ha="center", va="center",
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.18", fc=fc, ec="none") if bg else None)
            y -= 0.16

    panel(axes[0], r"$\hat{x}\hat{p}\,\psi$", [
        (r"$= \hat{x}\!\left(-i\hbar\,\partial_x\psi\right)$", False),
        (r"$= -i\hbar\,x\,\partial_x\psi$", False),
        ("", False),
        ("(no extra term)", False),
    ], TAB[0])

    panel(axes[1], r"$\hat{p}\hat{x}\,\psi = \hat{p}(x\psi)$", [
        (r"$= -i\hbar\,\partial_x(x\psi)$", False),
        (r"$= -i\hbar\,\psi - i\hbar\,x\,\partial_x\psi$", False),
        (r"product-rule bonus: $-i\hbar\,\psi$", True),
        (r"$\Rightarrow[\hat{x},\hat{p}]\psi = i\hbar\psi$", False),
    ], TAB[1])

    # Arrow between panels
    fig.text(0.505, 0.50, r"$-$", ha="center", va="center", fontsize=18)

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    savefig("03-commutators-and-uncertainty-fig-02.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 3.3  Bloch sphere colour-map of Robertson bound (ℏ/2)|<S_y>|
# Bloch sphere parameterisation:
#   |ψ> = cos(θ/2)|↑> + e^{iφ} sin(θ/2)|↓>
#   <S_y> = (ℏ/2) sin θ sin φ
#   Robertson bound for [Sx,Sz] = −iℏ Sy: σ_{Sx}σ_{Sz} ≥ (ℏ/2)|<Sy>|
# ─────────────────────────────────────────────────────────────────────────────
def fig_03_03():
    from mpl_toolkits.mplot3d import Axes3D     # noqa: F401

    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_subplot(111, projection="3d")

    # Bloch sphere surface
    u = np.linspace(0, np.pi, 60)     # theta (polar)
    v = np.linspace(0, 2 * np.pi, 80)   # phi (azimuthal)
    U, V = np.meshgrid(u, v)
    X = np.sin(U) * np.cos(V)
    Y = np.sin(U) * np.sin(V)
    Z = np.cos(U)

    # Robertson bound (in units of ℏ/2): |<Sy>| = |sin θ sin φ|
    bound = np.abs(np.sin(U) * np.sin(V))   # ranges 0 → 1

    surf = ax.plot_surface(X, Y, Z, facecolors=plt.cm.RdBu_r(bound),
                           alpha=0.82, linewidth=0, antialiased=True, shade=False)

    # Axes lines
    for vec, lbl, off in [([1.4, 0, 0], r"$x$", (0.05, 0, 0)),
                           ([0, 1.4, 0], r"$y$", (0, 0.07, 0)),
                           ([0, 0, 1.4], r"$z$", (0, 0, 0.07))]:
        ax.quiver(0, 0, 0, *vec, color="0.4", lw=0.8, arrow_length_ratio=0.08)
        ax.text(*(np.array(vec) + np.array(off)), lbl, fontsize=9, color="0.3")

    # Label poles
    ax.text(0, 0, 1.12, r"$|\uparrow\rangle$ $\sigma{=}0$", fontsize=8.5,
            ha="center", color=TAB[1])
    ax.text(0, 0, -1.22, r"$|\downarrow\rangle$ $\sigma{=}0$", fontsize=8.5,
            ha="center", color=TAB[1])
    ax.text(0, 1.18, 0, r"$|{+}y\rangle$ max", fontsize=8.5,
            ha="center", color=TAB[3])
    ax.text(0, -1.22, 0, r"$|{-}y\rangle$ max", fontsize=8.5,
            ha="center", color=TAB[3])

    ax.set_axis_off()

    # Colourbar (manual)
    sm = plt.cm.ScalarMappable(cmap="RdBu_r", norm=plt.Normalize(0, 1))
    sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, shrink=0.55, pad=0.02, aspect=18)
    cb.set_label(r"Robertson bound $\frac{\hbar}{2}|\langle\hat{S}_y\rangle|$ (units $\hbar/2$)",
                 fontsize=8.5)
    cb.set_ticks([0, 0.5, 1.0])
    cb.set_ticklabels(["0 (poles / x-states)", r"$\hbar/4$", r"$\hbar/2$ (y-states)"])

    ax.set_title(r"Figure 3.3 — Robertson bound $\sigma_{S_x}\sigma_{S_z}\geq\frac{\hbar}{2}|\langle\hat{S}_y\rangle|$ on the Bloch sphere",
                 fontsize=9.5, pad=4)
    ax.view_init(elev=22, azim=35)

    savefig("03-commutators-and-uncertainty-fig-03.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 5.1  Schematic: central-potential separation into angular + radial eqs
# ─────────────────────────────────────────────────────────────────────────────
def fig_05_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)

    def box(ax, x, y, w, h, txt, color, fontsize=9):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                    lw=1.5, edgecolor=color, facecolor="#f0f4ff"))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center",
                fontsize=fontsize, color=color)

    # Top box: full Hamiltonian
    box(ax, 2.8, 2.7, 4.4, 1.0,
        r"$\hat{H} = \frac{\hat{p}_r^2}{2m}+\frac{\hat{L}^2}{2mr^2} + V(r)$",
        "k", fontsize=10)

    # Separation arrow
    ax.annotate("", xy=(1.5, 1.8), xytext=(4.0, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1.2))
    ax.annotate("", xy=(8.5, 1.8), xytext=(6.0, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1.2))
    ax.text(5.0, 2.35, "separate", ha="center", fontsize=9, color="0.4",
            style="italic")

    # Left box: angular
    box(ax, 0.15, 0.55, 3.4, 1.25,
        r"Angular equation" + "\n" +
        r"$\hat{L}^2 Y_{\ell m}=\hbar^2\ell(\ell{+}1)Y_{\ell m}$" + "\n" +
        r"(universal — solved once)",
        TAB[2], fontsize=8.5)

    # Right box: radial
    box(ax, 6.45, 0.55, 3.4, 1.25,
        r"Radial equation" + "\n" +
        r"$\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right)+\left[\frac{2mr^2}{\hbar^2}(E{-}V)-\ell(\ell{+}1)\right]R=0$" + "\n"
        r"(depends on $V(r)$)",
        TAB[0], fontsize=7.8)

    # Separation constant label
    ax.text(5.0, 1.75, r"separation constant $\ell(\ell{+}1)$",
            ha="center", fontsize=9, color="0.35")

    ax.set_title("Figure 5.1 — Separating the central-potential Schrödinger equation",
                 fontsize=10.5, pad=4)
    savefig("05-quantum-mechanics-in-three-dimensions-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.1  Three-level hierarchy: CCR → L commutators → [L²,Li]=0 + spectrum
# ─────────────────────────────────────────────────────────────────────────────
def fig_06_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    def hbox(ax, x, y, w, h, txt, color, fontsize=9):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                                    lw=1.6, edgecolor=color, facecolor="#f9f9ff"))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center",
                fontsize=fontsize, color=color)

    # Level 1 — CCR
    hbox(ax, 2.8, 3.55, 4.4, 0.80,
         r"$[\hat{r}_i,\hat{p}_j]=i\hbar\delta_{ij}$  (canonical commutation relations)",
         TAB[4], fontsize=9)

    # Arrow down
    ax.annotate("", xy=(5.0, 2.85), xytext=(5.0, 3.55),
                arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1.3))
    ax.text(5.3, 3.18, r"define $\hat{L}_i=\epsilon_{ijk}\hat{r}_j\hat{p}_k$",
            fontsize=8, color="0.4")

    # Level 2 — L algebra
    hbox(ax, 1.7, 1.95, 6.6, 0.85,
         r"$[\hat{L}_i,\hat{L}_j]=i\hbar\,\epsilon_{ijk}\hat{L}_k$  " +
         r"   $[\hat{L}^2,\hat{L}_i]=0$",
         TAB[0], fontsize=9.5)

    # Arrow down
    ax.annotate("", xy=(5.0, 1.25), xytext=(5.0, 1.95),
                arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1.3))
    ax.text(5.3, 1.58, "ladder argument", fontsize=8, color="0.4")

    # Level 3 — spectrum
    hbox(ax, 1.2, 0.25, 7.6, 0.95,
         r"Spectrum:  $\hat{L}^2|\ell,m\rangle=\hbar^2\ell(\ell{+}1)|\ell,m\rangle$,  " +
         r"$\hat{L}_z|\ell,m\rangle=\hbar m|\ell,m\rangle$,  " +
         r"$\ell=0,\frac{1}{2},1,\ldots$,  $|m|\leq\ell$",
         TAB[2], fontsize=8.8)

    ax.set_title(
        "Figure 6.1 — Hierarchy: canonical commutation relations → angular momentum algebra → spectrum",
        fontsize=9.5, pad=4)
    savefig("06-angular-momentum-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.2  Ladder diagram for ℓ = 2
# Coefficients: L±|ℓ,m> = ℏ √(ℓ(ℓ+1)−m(m±1)) |ℓ,m±1>
# ─────────────────────────────────────────────────────────────────────────────
def fig_06_02():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.axis("off")
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 5.0)

    ell = 2
    ms = list(range(-ell, ell + 1))   # -2,-1,0,1,2
    y_pos = {m: i * 0.9 for i, m in enumerate(ms)}
    x_box = 2.3
    box_h = 0.52
    box_w = 1.4

    # Draw rungs
    for m in ms:
        y = y_pos[m]
        ax.add_patch(FancyBboxPatch((x_box - box_w / 2, y - box_h / 2),
                                    box_w, box_h,
                                    boxstyle="round,pad=0.06",
                                    lw=1.4, edgecolor="k", facecolor="#eef6ff"))
        ax.text(x_box, y, fr"$|2,{m:+d}\rangle$", ha="center", va="center", fontsize=12)

    # Raising (blue) and lowering (red) arrows with coefficients
    for m in ms:
        # Raising arrow: m → m+1
        if m < ell:
            coeff_up = np.sqrt(ell * (ell + 1) - m * (m + 1))
            y0 = y_pos[m] + box_h / 2
            y1 = y_pos[m + 1] - box_h / 2
            ax.annotate("",
                        xy=(x_box + 0.95, y1),
                        xytext=(x_box + 0.95, y0),
                        arrowprops=dict(arrowstyle="-|>", color=TAB[0], lw=1.8))
            ax.text(x_box + 1.55, (y0 + y1) / 2,
                    fr"$\sqrt{{{coeff_up**2:.0f}}}\,\hbar$",
                    va="center", fontsize=9, color=TAB[0])

        # Lowering arrow: m → m-1
        if m > -ell:
            coeff_dn = np.sqrt(ell * (ell + 1) - m * (m - 1))
            y0 = y_pos[m] - box_h / 2
            y1 = y_pos[m - 1] + box_h / 2
            ax.annotate("",
                        xy=(x_box - 0.95, y1),
                        xytext=(x_box - 0.95, y0),
                        arrowprops=dict(arrowstyle="-|>", color=TAB[3], lw=1.8))
            ax.text(x_box - 1.55, (y0 + y1) / 2,
                    fr"$\sqrt{{{coeff_dn**2:.0f}}}\,\hbar$",
                    va="center", ha="right", fontsize=9, color=TAB[3])

    # Top and bottom: grey stub arrows to show termination
    y_top = y_pos[ell] + box_h / 2
    ax.annotate("", xy=(x_box + 0.95, y_top + 0.35), xytext=(x_box + 0.95, y_top),
                arrowprops=dict(arrowstyle="-|>", color="0.75", lw=1.5, ls="--"))
    ax.text(x_box + 1.55, y_top + 0.18, r"$\hat{L}_+|2,+2\rangle=0$",
            fontsize=8, color="0.65")

    y_bot = y_pos[-ell] - box_h / 2
    ax.annotate("", xy=(x_box - 0.95, y_bot - 0.35), xytext=(x_box - 0.95, y_bot),
                arrowprops=dict(arrowstyle="-|>", color="0.75", lw=1.5, ls="--"))
    ax.text(x_box - 1.55, y_bot - 0.18, r"$\hat{L}_-|2,-2\rangle=0$",
            fontsize=8, color="0.65", ha="right")

    # Legend
    up_patch = mlines.Line2D([], [], color=TAB[0], lw=2,
                             label=r"$\hat{L}_+$ (raises $m$)")
    dn_patch = mlines.Line2D([], [], color=TAB[3], lw=2,
                             label=r"$\hat{L}_-$ (lowers $m$)")
    ax.legend(handles=[up_patch, dn_patch], loc="lower right", fontsize=9, framealpha=0.9)

    ax.set_title(r"Figure 6.2 — Ladder operators for $\ell=2$: five rungs, coefficients $\hbar\sqrt{\ell(\ell+1)-m(m\pm1)}$",
                 fontsize=9.5, pad=4)
    savefig("06-angular-momentum-fig-02.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 8.1  Hydrogen hyperfine structure — triplet/singlet, 21-cm photon
# ─────────────────────────────────────────────────────────────────────────────
def fig_08_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    # Energy levels
    E_triplet = 3.2
    E_singlet = 1.2
    lw = 2.2

    # Triplet levels (F=1, three M_F)
    for i, (mf, clr, lbl) in enumerate(
            [(-1, TAB[0], r"$|{\uparrow\downarrow}\rangle-|{\downarrow\uparrow}\rangle)/\sqrt{2}$... no, triplet $M_F=-1$"),
             (0, TAB[0], ""),
             (1, TAB[0], "")]):
        x0 = 2.8 + i * 1.35
        ax.plot([x0, x0 + 1.1], [E_triplet, E_triplet], color=TAB[0], lw=lw)

    # Labels for triplet sub-levels
    for i, (mf, spin_lbl) in enumerate([
            (-1, r"$|\downarrow\downarrow\rangle$"),
            (0,  r"$(|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle)/\sqrt{2}$"),
            (1,  r"$|\uparrow\uparrow\rangle$")]):
        x_c = 3.35 + i * 1.35
        ax.text(x_c, E_triplet + 0.16, fr"$M_F={mf:+d}$",
                ha="center", fontsize=8, color=TAB[0])
        ax.text(x_c, E_triplet - 0.30, spin_lbl,
                ha="center", fontsize=7.2, color=TAB[0])

    # Triplet label
    ax.text(0.25, E_triplet, r"Triplet $F=1$" + "\n" + r"$J=1,\;S_\text{tot}=1$",
            ha="left", va="center", fontsize=9.5, color=TAB[0])

    # Singlet level (F=0)
    ax.plot([3.5, 6.5], [E_singlet, E_singlet], color=TAB[3], lw=lw)
    ax.text(0.25, E_singlet, r"Singlet $F=0$" + "\n" + r"$J=0,\;S_\text{tot}=0$",
            ha="left", va="center", fontsize=9.5, color=TAB[3])
    ax.text(5.0, E_singlet - 0.32,
            r"$(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)/\sqrt{2}$",
            ha="center", fontsize=8, color=TAB[3])

    # Transition arrow
    ax.annotate("", xy=(7.8, E_singlet + 0.05), xytext=(7.8, E_triplet - 0.05),
                arrowprops=dict(arrowstyle="-|>", color="darkorange", lw=2.2))

    # Photon label
    ax.text(8.25, (E_triplet + E_singlet) / 2,
            "21-cm photon\n1420.405 MHz\n$\\lambda=21.1$ cm",
            va="center", fontsize=8.5, color="darkorange",
            bbox=dict(boxstyle="round,pad=0.25", fc="#fff7e6", ec="darkorange", alpha=0.9))

    # Energy gap brace
    ax.annotate("", xy=(7.2, E_singlet), xytext=(7.2, E_triplet),
                arrowprops=dict(arrowstyle="<->", color="0.4", lw=1.2))
    ax.text(7.05, (E_triplet + E_singlet) / 2,
            r"$\Delta E = h\nu$" + "\n" + r"$= 5.87\times10^{-6}$ eV",
            ha="right", va="center", fontsize=7.8, color="0.4")

    ax.set_title(
        "Figure 8.1 — Hydrogen hyperfine splitting: triplet ($F=1$) and singlet ($F=0$), 21-cm line",
        fontsize=10, pad=4)
    savefig("08-addition-of-angular-momenta-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 9.3  Energy levels: hydrogen (ℓ-degenerate) vs sodium (ℓ-split)
# Hydrogen: E_n = -13.6/n² eV  (n=1..4, all ℓ degenerate)
# Sodium:   Approximate E_{nℓ} using quantum-defect values:
#   δ_s≈1.37, δ_p≈0.88, δ_d≈0.01  → E_{nℓ} = -13.6/(n-δ_ℓ)² eV
# ─────────────────────────────────────────────────────────────────────────────
def fig_09_03():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGSIZE, sharey=True)

    Ry = 13.6  # eV

    # --- Hydrogen ---
    for n in range(1, 5):
        E = -Ry / n ** 2
        x_left, x_right = 0.1, 0.9
        ax1.plot([x_left, x_right], [E, E], "k-", lw=1.8)
        # label all subshell letters horizontally
        labels = " ".join(f"{s}" for s in ["s", "p", "d", "f"][:n])
        ax1.text(0.5, E + 0.25, f"$n={n}$  ({labels})", ha="center", fontsize=7.8,
                 color="0.3")

    ax1.set_xlim(-0.1, 1.1)
    ax1.set_ylim(-14.5, 1.5)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.spines["bottom"].set_visible(False)
    ax1.set_xticks([])
    ax1.set_ylabel("Energy (eV)", fontsize=10)
    ax1.set_title("Hydrogen\n(all $\\ell$ degenerate at each $n$)", fontsize=9.5)
    ax1.axhline(0, color="0.7", lw=0.8, ls="--")
    ax1.text(0.5, 0.5, "continuum", ha="center", fontsize=8, color="0.5")

    # --- Sodium — quantum defects ---
    delta = {"s": 1.373, "p": 0.883, "d": 0.010, "f": 0.000}
    colors_l = {"s": TAB[0], "p": TAB[1], "d": TAB[2], "f": TAB[3]}
    x_positions = {"s": 0.15, "p": 0.38, "d": 0.62, "f": 0.85}

    plotted = {}
    for n in range(3, 7):
        for ell_name in ["s", "p", "d", "f"]:
            if {"s": 0, "p": 1, "d": 2, "f": 3}[ell_name] >= n:
                continue
            E = -Ry / (n - delta[ell_name]) ** 2
            x = x_positions[ell_name]
            ax2.plot([x - 0.10, x + 0.10], [E, E],
                     color=colors_l[ell_name], lw=2.0)
            ax2.text(x, E + 0.25, f"$n={n}$", ha="center", fontsize=7,
                     color=colors_l[ell_name])
            plotted[ell_name] = colors_l[ell_name]

    # Mark Na 3p → 3s (D lines)
    E_3s = -Ry / (3 - delta["s"]) ** 2
    E_3p = -Ry / (3 - delta["p"]) ** 2
    ax2.annotate("", xy=(x_positions["s"], E_3s + 0.08),
                 xytext=(x_positions["p"], E_3p - 0.08),
                 arrowprops=dict(arrowstyle="-|>", color="gold", lw=2.0))
    ax2.text(0.28, (E_3s + E_3p) / 2,
             "Na $D$ lines\n589 nm", ha="center", fontsize=7.5,
             color="goldenrod",
             bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="gold", alpha=0.9))

    # Column labels
    for ell_name in ["s", "p", "d"]:
        ax2.text(x_positions[ell_name], 0.9, f"$\\ell=$ {ell_name}",
                 ha="center", fontsize=8.5, color=colors_l[ell_name])

    ax2.set_xlim(-0.05, 1.05)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.spines["bottom"].set_visible(False)
    ax2.set_xticks([])
    ax2.set_title("Sodium\n($\\ell$-degeneracy broken by screening)", fontsize=9.5)
    ax2.axhline(0, color="0.7", lw=0.8, ls="--")

    fig.suptitle(
        "Figure 9.3 — Hydrogen vs. sodium: $\\ell$-degeneracy is special to $1/r$ (Coulomb) potentials",
        fontsize=9.5, y=1.01)
    plt.tight_layout()
    savefig("09-the-hydrogen-atom-fig-03.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 11.1  Iron [Ar]3d⁶4s² — orbital box diagram with Hund's rule filling
# ─────────────────────────────────────────────────────────────────────────────
def fig_11_01():
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    # Draw a single orbital box at (x_center, y_center), with up/dn arrows
    def orbital_box(ax, xc, yc, up=False, dn=False, color_up=TAB[0], color_dn=TAB[3]):
        w, h = 0.62, 0.52
        ax.add_patch(plt.Rectangle((xc - w / 2, yc - h / 2), w, h,
                                   lw=1.4, edgecolor="k", facecolor="white"))
        if up:
            ax.annotate("", xy=(xc - 0.07, yc + h / 2 - 0.07),
                        xytext=(xc - 0.07, yc - h / 2 + 0.07),
                        arrowprops=dict(arrowstyle="-|>", color=color_up, lw=1.8))
        if dn:
            ax.annotate("", xy=(xc + 0.07, yc - h / 2 + 0.07),
                        xytext=(xc + 0.07, yc + h / 2 - 0.07),
                        arrowprops=dict(arrowstyle="-|>", color=color_dn, lw=1.8))

    # 3d orbitals: five boxes, m_ℓ = +2,+1,0,-1,-2
    # Fe: 3d⁶ — 5 spin-up + 1 spin-down (paired into m_ℓ=+2)
    ml_labels = ["+2", "+1", "0", "−1", "−2"]
    y_3d = 2.8
    x_start = 1.8
    x_step = 1.0

    for i, ml in enumerate(ml_labels):
        xc = x_start + i * x_step
        paired = (i == 0)   # sixth electron pairs into m_ℓ=+2
        orbital_box(ax, xc, y_3d, up=True, dn=paired)
        ax.text(xc, y_3d - 0.46, f"$m_\\ell={ml}$", ha="center", fontsize=7.5)

    ax.text(0.7, y_3d, "3d", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(7.5, y_3d, r"$3d^6$", ha="left", va="center", fontsize=11)

    # 4s orbital: two electrons (both filled, paired)
    y_4s = 1.4
    orbital_box(ax, 4.3, y_4s, up=True, dn=True)
    ax.text(0.7, y_4s, "4s", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(7.5, y_4s, r"$4s^2$", ha="left", va="center", fontsize=11)

    # [Ar] core indication
    ax.add_patch(FancyBboxPatch((0.2, 0.55), 9.5, 0.55,
                                boxstyle="round,pad=0.08",
                                lw=1.2, edgecolor="0.6", facecolor="#f5f5f5"))
    ax.text(5.0, 0.83, r"[Ar] core: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6$  ($S=0,\;L=0,\;J=0$)",
            ha="center", va="center", fontsize=9, color="0.45")

    # Quantum number summary
    ax.text(5.0, 4.15,
            r"$S=2$ (four net $\uparrow$),   $L=2$ (sixth $e^-$ in $m_\ell=+2$),"
            r"   $J=L+S=4$   $\Rightarrow$   $^5D_4$",
            ha="center", fontsize=9.5, color=TAB[2],
            bbox=dict(boxstyle="round,pad=0.22", fc="#efffef", ec=TAB[2], alpha=0.9))

    ax.set_title(
        r"Figure 11.1 — Iron $[\mathrm{Ar}]3d^6\,4s^2$ by Hund's rules: term ${}^5D_4$",
        fontsize=10.5, pad=4)
    savefig("11-capstone-the-atom-fig-01.png")


# ─────────────────────────────────────────────────────────────────────────────
# Fig 11.2  Qualitative orbital energy crossing: ε(3d) and ε(4s) vs Z
#   across the first transition series (Z=19 K to Z=36 Kr).
#   Values approximate Hartree-Fock orbital energies (Clementi & Roetti 1974
#   trend): ε(4s) stays roughly flat/slowly falling; ε(3d) drops steeply.
# ─────────────────────────────────────────────────────────────────────────────
def fig_11_02():
    fig, ax = plt.subplots(figsize=FIGSIZE)

    # Approximate HF orbital energies (eV, negative = bound) for first
    # transition series neutral atoms, outermost 4s and 3d.
    # Source: qualitative trend matching Clementi-Roetti / NIST data.
    Z_vals = np.array([19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
    labels  = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]

    # 4s orbital energy (eV): roughly flat around −4 to −5 eV
    E_4s = np.array([-4.34, -5.13, -5.69, -6.10, -6.50, -6.77,
                     -7.09, -7.17, -7.46, -7.72, -7.73, -8.40])

    # 3d orbital energy (eV): drops steeply from near 0 at K to ~-14 at Zn
    E_3d = np.array([-0.12, -1.70, -4.61, -6.82, -8.89, -9.57,
                     -11.30, -12.56, -13.90, -14.80, -15.28, -15.75])

    ax.plot(Z_vals, E_4s, "o-", color=TAB[0], lw=2.0, ms=5, label=r"$\varepsilon(4s)$")
    ax.plot(Z_vals, E_3d, "s-", color=TAB[2], lw=2.0, ms=5, label=r"$\varepsilon(3d)$")

    # Annotate the near-crossing region
    ax.axvspan(19.5, 21.5, alpha=0.10, color="gray")
    ax.text(20.5, -2.2, "near-\ndegenerate", ha="center", fontsize=7.5, color="0.4",
            style="italic")

    # Mark Fe (Z=26)
    fe_idx = list(Z_vals).index(26)
    ax.annotate(r"Fe ($^5D_4$)",
                xy=(26, E_3d[fe_idx]), xytext=(27.5, -10.5),
                arrowprops=dict(arrowstyle="->", color="0.4", lw=1.0),
                fontsize=8.5, color=TAB[2])

    # Mark the ordering reversal for ions
    ax.text(29.0, -6.5,
            "For ions:\n$\\varepsilon(3d)<\\varepsilon(4s)$\n→ 4s removed first",
            fontsize=7.8, color="0.35", ha="center",
            bbox=dict(boxstyle="round,pad=0.22", fc="#f0f0f0", ec="0.7", alpha=0.9))

    for i, (Z, lbl) in enumerate(zip(Z_vals, labels)):
        ax.text(Z, E_4s[i] + 0.5, lbl, ha="center", fontsize=6.5, color=TAB[0])

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel("Atomic number $Z$", fontsize=10)
    ax.set_ylabel("Orbital energy (eV)", fontsize=10)
    ax.legend(fontsize=10, loc="lower left")
    ax.set_title(
        r"Figure 11.2 — $3d$/$4s$ orbital energies across the first transition series",
        fontsize=10, pad=4)

    savefig("11-capstone-the-atom-fig-02.png")


# ─────────────────────────────────────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating figures...")
    fig_02_01()
    fig_03_01()
    fig_03_02()
    fig_03_03()
    fig_05_01()
    fig_06_01()
    fig_06_02()
    fig_08_01()
    fig_09_03()
    fig_11_01()
    fig_11_02()
    print("Done.")
