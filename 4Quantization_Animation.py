import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Continuous sine wave
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t)

# Quantization function
def quantize(x, levels):
    x_min, x_max = -1, 1  # normalized signal
    step = (x_max - x_min) / (levels - 1)
    q_signal = np.round((x - x_min) / step) * step + x_min
    return q_signal

# Setup figure
fig, ax = plt.subplots(figsize=(7,4))
ax.plot(t, signal, 'b', alpha=0.5, label="Original Signal")
(line,) = ax.step([], [], 'r', where='mid', label="Quantized Signal")
ax.set_ylim(-1.2, 1.2)
ax.set_xlim(0, 1)
ax.set_title("Quantization Animation")
ax.legend(loc="lower right")

# Text annotation (moved to top-left)
level_text = ax.text(0.05, 0.9, '', transform=ax.transAxes, 
                     fontsize=14, color="darkred", weight="bold",
                     bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Animation function
def update(frame):
    levels = frame
    q_signal = quantize(signal, levels)
    line.set_data(t, q_signal)
    level_text.set_text(f"Levels = {levels}")
    return line, level_text

# Animate levels from 2 to 32
ani = FuncAnimation(fig, update, frames=range(2, 33), interval=300, blit=True)

plt.tight_layout()
plt.show()
