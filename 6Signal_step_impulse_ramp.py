import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Discrete time axis
n = np.arange(-10, 11, 1)

# Continuous time axis
t = np.linspace(-10, 10, 400)

# Discrete signals
unit_step_d = np.array([1 if i >= 0 else 0 for i in n])
impulse_d = np.array([1 if i == 0 else 0 for i in n])
ramp_d = np.array([i if i >= 0 else 0 for i in n])

# Continuous signals
unit_step_c = np.array([1 if i >= 0 else 0 for i in t])
impulse_c = np.array([1 if np.isclose(i, 0, atol=0.05) else 0 for i in t])  # approximated narrow pulse
ramp_c = np.array([i if i >= 0 else 0 for i in t])

# Pack signals
signals_d = [unit_step_d, impulse_d, ramp_d]
signals_c = [unit_step_c, impulse_c, ramp_c]
titles = ["Unit Step Function", "Impulse Function", "Ramp Function"]
labels = ["Step", "Impulse", "Ramp"]
line_colors = ["blue", "red", "green"]
marker_colors = ["bo", "ro", "go"]  # shorthand

fig, ax = plt.subplots(figsize=(7,4))
ax.set_xlim(-11, 11)
ax.set_ylim(-1, 11)

def update(frame):
    sig_idx = frame // len(n)       # which signal (0,1,2)
    point = frame % len(n) + 1      # number of points to show

    ax.clear()
    ax.set_xlim(-11, 11)
    ax.set_ylim(-1, 11)

    # Update title
    ax.set_title(titles[sig_idx], fontsize=14, fontweight="bold", color=line_colors[sig_idx])

    # Discrete signal (stem)
    x_d = n[:point]
    y_d = signals_d[sig_idx][:point]
    ax.stem(x_d, y_d, basefmt=" ", linefmt=line_colors[sig_idx], markerfmt=marker_colors[sig_idx])

    # Continuous signal (curve)
    x_c = t
    y_c = signals_c[sig_idx]
    ax.plot(x_c, y_c, line_colors[sig_idx], linewidth=2, alpha=0.7)

    # Label on the left side with function name
    ax.text(-10.5, 9.5, labels[sig_idx], fontsize=12, color=line_colors[sig_idx], fontweight="bold", va="top")

# total frames
frames_total = len(n) * len(signals_d)
ani = FuncAnimation(fig, update, frames=frames_total, interval=150, repeat=True)

plt.tight_layout()
plt.show()
