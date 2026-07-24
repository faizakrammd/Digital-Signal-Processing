import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Time vector and signal
t = np.linspace(0, 1, 100, endpoint=False)   # 100 samples
signal = np.sin(2 * np.pi * 5 * t)           # 5 Hz sine wave

# Setup figure with 2 panels
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))

# --- Top: Time-domain signal ---
ax1.set_title("Time-Domain Signal")
ax1.set_xlim(0, 1)
ax1.set_ylim(-1.2, 1.2)
line, = ax1.plot([], [], 'b-o', markersize=4, lw=2)

# --- Bottom: Array representation ---
ax2.set_title("Array Representation")
ax2.set_xlim(0, len(signal))
ax2.set_ylim(-1.2, 1.2)
markerline, stemlines, baseline = ax2.stem([0], [0])  # dummy init
ax2.set_xlabel("Index (n)")

# Animation function
def update(frame):
    # Update line in time-domain plot
    line.set_data(t[:frame], signal[:frame])
    
    # Update array (stems)
    x = np.arange(frame)
    y = signal[:frame]
    markerline.set_data(x, y)
    
    # Update stemlines (LineCollection expects segments)
    if frame > 0:
        segments = [[(xi, 0), (xi, yi)] for xi, yi in zip(x, y)]
        stemlines.set_segments(segments)
    else:
        stemlines.set_segments([])
    
    return line, markerline, stemlines

# Animate
ani = FuncAnimation(fig, update, frames=len(signal), interval=100, blit=True, repeat=False)

plt.tight_layout()
plt.show()
