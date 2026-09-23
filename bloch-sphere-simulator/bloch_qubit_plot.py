import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from fractions import Fraction

# ------------------------------------------------------------
# Interactive Bloch sphere with sliders for P(0) and φ.
# φ is displayed as multiples of π everywhere (title, text, slider value).
# Slider ticks are labeled in π units; the live readout shows nπ/d when possible.
# ------------------------------------------------------------

def bloch_from(p0: float, phi: float):
    p1 = 1.0 - p0
    alpha = np.sqrt(p0)
    beta  = np.exp(1j * phi) * np.sqrt(p1)
    x = 2.0 * np.real(alpha * np.conj(beta))
    y = 2.0 * np.imag(alpha * np.conj(beta))
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x, y, z, p1

def phi_to_pi_string(phi: float, max_den: int = 16) -> str:
    """
    Return φ as a multiple of π using a rational approximation n/d (d ≤ max_den).
    Examples: 0, π/2, 3π/4, 5π/8, 1.13π (fallback).
    """
    ratio = phi / np.pi
    # Snap small negatives to 0 due to slider noise
    if abs(ratio) < 1e-12:
        return "0"
    # Reduce ratio modulo 2 for nicer labels (0..2)
    ratio = ratio % 2.0
    frac = Fraction(ratio).limit_denominator(max_den)
    n, d = frac.numerator, frac.denominator

    if n == 0:
        return "0"
    if d == 1:
        if n == 1: return r"\pi"
        return rf"{n}\pi"
    if n == 1:      return rf"\frac{{\pi}}{{{d}}}"
    return rf"\frac{{{n}\pi}}{{{d}}}"

# --- initial values ---
p0_init  = 0.75
phi_init = 0.0

# --- figure & 3D axes ---
fig = plt.figure(figsize=(7.8, 7.8))
ax = fig.add_subplot(111, projection='3d')

# Sphere mesh
u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, np.pi, 30)
X = np.outer(np.cos(u), np.sin(v))
Y = np.outer(np.sin(u), np.sin(v))
Z = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(X, Y, Z, alpha=0.18, linewidth=0, antialiased=True, shade=True)

# Axes (Z vertical) — colored for clarity
ax.plot([-1, 1], [0, 0], [0, 0], color='tab:orange', lw=2)  # X
ax.plot([0, 0], [-1, 1], [0, 0], color='tab:green',  lw=2)  # Y
ax.plot([0, 0], [0, 0], [-1, 1], color='tab:red',    lw=2)  # Z
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

# Equator landmarks
ax.scatter([ 1, -1,  0,  0], [0, 0, 1, -1], [0, 0, 0, 0], s=35)
ax.text( 1.06,  0.00, 0.00, "+",  fontsize=11)
ax.text(-1.18,  0.00, 0.00, "−",  fontsize=11)
ax.text( 0.00,  1.06, 0.00, "+i", fontsize=11)
ax.text( 0.00, -1.18, 0.00, "−i", fontsize=11)

# Poles |0>, |1>
ax.scatter([0, 0], [0, 0], [ 1, -1], s=35)
ax.text(0.02, 0.02,  1.06, "|0⟩", fontsize=11)
ax.text(0.02, 0.02, -1.18, "|1⟩", fontsize=11)

# Initial vector
x, y, z, p1 = bloch_from(p0_init, phi_init)
vec = ax.quiver(0, 0, 0, x, y, z, linewidth=2.5, color='tab:blue')
tip = ax.scatter([x], [y], [z], s=70, color='tab:blue')

# Limits, aspect, title (φ shown as multiple of π)
ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-1, 1]); ax.set_ylim([-1, 1]); ax.set_zlim([-1, 1])
title = ax.set_title(
    "Bloch sphere: "
    + f"P(0)={p0_init:.2f}, P(1)={1-p0_init:.2f}, "
    + r"$\phi=" + phi_to_pi_string(phi_init) + "$"
)

# Dirac + phi text
dirac = ax.text2D(
    0.03, 0.95,
    fr"$|\psi\rangle=\sqrt{{{p0_init:.2f}}}\,|0\rangle + e^{{i\phi}}\sqrt{{{1-p0_init:.2f}}}\,|1\rangle$",
    transform=ax.transAxes
)
phi_text = ax.text2D(0.03, 0.90, fr"$\phi={phi_to_pi_string(phi_init)}$", transform=ax.transAxes)

# --- sliders ---
plt.subplots_adjust(bottom=0.20)
ax_p0  = plt.axes([0.15, 0.08, 0.70, 0.035])
ax_phi = plt.axes([0.15, 0.03, 0.70, 0.035])

s_p0  = Slider(ax_p0,  "P(0)",    0.0, 1.0,     valinit=p0_init)
s_phi = Slider(ax_phi, r"$\phi$", 0.0, 2*np.pi, valinit=phi_init)

# π-based tick labels across the slider (every π/4)
phi_ticks  = [k * np.pi/4 for k in range(0, 9)]  # 0..2π step π/4
phi_labels = [
    "0", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",
    r"$\pi$", r"$\frac{5\pi}{4}$", r"$\frac{3\pi}{2}$", r"$\frac{7\pi}{4}$", r"$2\pi$"
]
ax_phi.set_xticks(phi_ticks)
ax_phi.set_xticklabels(phi_labels)

# Also override the slider's live numeric readout to π-units
s_phi.valtext.set_text(rf"${phi_to_pi_string(s_phi.val)}$")

def update(_):
    global vec, tip
    p0  = s_p0.val
    phi = s_phi.val
    x, y, z, p1 = bloch_from(p0, phi)

    # redraw vector + tip
    vec.remove(); tip.remove()
    vec = ax.quiver(0, 0, 0, x, y, z, linewidth=2.5, color='tab:blue')
    tip = ax.scatter([x], [y], [z], s=70, color='tab:blue')

    # texts (title & on-figure φ as π string)
    title.set_text(
        "Bloch sphere: "
        + f"P(0)={p0:.2f}, P(1)={1-p0:.2f}, "
        + r"$\phi=" + phi_to_pi_string(phi) + "$"
    )
    dirac.set_text(
        fr"$|\psi\rangle=\sqrt{{{p0:.2f}}}\,|0\rangle + e^{{i\phi}}\sqrt{{{1-p0:.2f}}}\,|1\rangle$"
    )
    phi_text.set_text(fr"$\phi={phi_to_pi_string(phi)}$")

    # live slider value as π string
    s_phi.valtext.set_text(rf"${phi_to_pi_string(phi)}$")

    fig.canvas.draw_idle()

s_p0.on_changed(update)
s_phi.on_changed(update)

plt.show()
