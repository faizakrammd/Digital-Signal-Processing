import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Original signal
f = 15   # Hz
t_cont = np.linspace(0, 1, 1000)
signal_cont = np.sin(2 * np.pi * f * t_cont)

# Sampling rates
fs_high = 50  # Above Nyquist
fs_low = 20   # Below Nyquist

# Setup figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7,6), sharex=True)

# Plot continuous signals
ax1.plot(t_cont, signal_cont, 'b', alpha=0.6)
ax2.plot(t_cont, signal_cont, 'b', alpha=0.6)

ax1.set_title("Correct Sampling (Above Nyquist - 50Hz)")
ax2.set_title("Aliasing (Below Nyquist - 20Hz)")

for ax in (ax1, ax2):
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.2, 1.2)

# Create empty scatter plots for samples
points_high, = ax1.plot([], [], 'ro-')
points_low, = ax2.plot([], [], 'go-')
ax1.legend()
ax2.legend()

# Animation update function
def update(frame):
    # Take samples up to current frame
    t_high = np.arange(0, frame/fs_high, 1/fs_high)
    t_low = np.arange(0, frame/fs_low, 1/fs_low)
    
    y_high = np.sin(2 * np.pi * f * t_high)
    y_low = np.sin(2 * np.pi * f * t_low)
    
    # Update sample markers
    points_high.set_data(t_high, y_high)
    points_low.set_data(t_low, y_low)
    
    return points_high, points_low

# Animate over 1 second (100 frames)
ani = FuncAnimation(fig, update, frames=np.arange(1, 101), interval=100, blit=True)

plt.tight_layout()
plt.show()
