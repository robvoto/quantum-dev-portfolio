import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Bloch sphere point for a qubit with P(0)=0.75, P(1)=0.25
# and a relative phase φ between |0⟩ and |1⟩.
#
# MATH (how x,y,z are computed):
# Let |ψ⟩ = α|0⟩ + β|1⟩ with α,β ∈ ℂ and |α|^2 + |β|^2 = 1.
# Bloch coordinates are given by:
#   x = 2 Re( α β* )
#   y = 2 Im( α β* )
#   z = |α|^2 − |β|^2
#
# If we parameterize α = cos(θ/2), β = e^{iφ} sin(θ/2) then:
#   x = sinθ cosφ,  y = sinθ sinφ,  z = cosθ
# and P(0)=|α|^2 = cos^2(θ/2),  P(1)=|β|^2 = sin^2(θ/2).
# ------------------------------------------------------------

# --- Choose probabilities and phase ---
p0 = 0.75             # P(measure 0)
p1 = 1.0 - p0         # P(measure 1)
phi = 0.0             # relative phase of |1⟩ vs |0⟩; try np.pi/2 to point toward +i

# Amplitudes (α, β). Choose the global phase so α is real and non-negative.
alpha = np.sqrt(p0)                   # amplitude of |0⟩
beta  = np.exp(1j * phi) * np.sqrt(p1)  # amplitude of |1⟩

# Bloch coordinates from amplitudes
x = 2.0 * np.real(alpha * np.conj(beta))
y = 2.0 * np.imag(alpha * np.conj(beta))
z = np.abs(alpha)**2 - np.abs(beta)**2

# (Optional) derive θ from p0 to connect with the sphere angles
theta = 2.0 * np.arccos(np.sqrt(p0))  # because p0 = cos^2(θ/2)

# --- Plot the Bloch sphere ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sphere mesh
u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, np.pi, 30)
X = np.outer(np.cos(u), np.sin(v))
Y = np.outer(np.sin(u), np.sin(v))
Z = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(X, Y, Z, alpha=0.15, linewidth=0, antialiased=True)

# Axes (Z vertical)
ax.plot([-1, 1], [0, 0], [0, 0])   # X
ax.plot([0, 0], [-1, 1], [0, 0])   # Y
ax.plot([0, 0], [0, 0], [-1, 1])   # Z
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z (vertical)")

# Equator landmarks: |+>, |->, |+i>, |-i|  (positions on equator)
ax.scatter([1, -1, 0, 0], [0, 0, 1, -1], [0, 0, 0, 0], s=30)
ax.text( 1.05,  0.00, 0.00, "+",  fontsize=10)   # |+>  (x=+1)
ax.text(-1.15,  0.00, 0.00, "−",  fontsize=10)   # |->  (x=−1)
ax.text( 0.00,  1.05, 0.00, "+i", fontsize=10)   # |+i> (y=+1)
ax.text( 0.00, -1.15, 0.00, "−i", fontsize=10)   # |-i> (y=−1)

# Poles |0>, |1>
ax.scatter([0, 0], [0, 0], [1, -1], s=30)
ax.text(0.02, 0.02,  1.05, "|0⟩", fontsize=10)
ax.text(0.02, 0.02, -1.15, "|1⟩", fontsize=10)

# Your qubit: draw vector and tip
ax.quiver(0, 0, 0, x, y, z, linewidth=2)  # vector from origin to (x,y,z)
ax.scatter([x], [y], [z], s=60)

# Nice aspect/limits
ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-1, 1]); ax.set_ylim([-1, 1]); ax.set_zlim([-1, 1])
ax.set_title("Bloch sphere: P(0)=0.75, P(1)=0.25, φ={:.2f} rad".format(phi))

# Text annotations (use f-string and double braces to keep LaTeX braces literal)
dirac = fr"$|\psi\rangle=\sqrt{{{p0:.2f}}}\,|0\rangle + e^{{i\phi}}\sqrt{{{p1:.2f}}}\,|1\rangle$"
phi_text = fr"$\phi={phi:.2f}\ \mathrm{{rad}}$"
ax.text2D(0.03, 0.95, dirac,    transform=ax.transAxes)
ax.text2D(0.03, 0.90, phi_text, transform=ax.transAxes)

plt.show()
