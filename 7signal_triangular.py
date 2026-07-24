import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Time axis
t = np.linspace(-10, 10, 1000)

# Triangular signal function
def triangular(t):
    return np.maximum(1 - np.abs(t)/3, 0)  # width = 6, peak = 1

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-1.5, 2)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
(line,) = ax.plot([], [], lw=2)
text = ax.text(-9.5, 1.5, "", fontsize=12, color="blue")
shift_line = ax.axvline(0, color="red", linestyle="--", lw=1, alpha=0)  # invisible initially

# Transformation states
states = [
    ("Original", lambda t: triangular(t), None),
    ("Shift", lambda t: triangular(t - 2), 2),
    ("Scale", lambda t: triangular(0.5 * t), None),
    ("Fold", lambda t: triangular(-t), None),
    ("Shift + Fold", lambda t: triangular(-(t - 2)), 2),
]

def init():
    line.set_data([], [])
    text.set_text("")
    shift_line.set_alpha(0)
    return (line, text, shift_line)

def update(frame):
    state_name, func, shift_pos = states[frame % len(states)]
    y = func(t)
    line.set_data(t, y)

    # Update label text
    text.set_text(state_name)

    # Show shift line if applicable
    if shift_pos is not None:
        shift_line.set_xdata([shift_pos, shift_pos])  # FIXED (needs sequence)
        shift_line.set_alpha(1)
    else:
        shift_line.set_alpha(0)

    return (line, text, shift_line)

# Animation
ani = FuncAnimation(fig, update, frames=len(states), init_func=init,
                    blit=True, repeat=True, interval=2000)

plt.show()
