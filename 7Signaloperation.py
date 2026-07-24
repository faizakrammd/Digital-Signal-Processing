import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a base signal (sinusoid for better visibility)
t = np.linspace(-5, 5, 200)
x = np.sin(t)

# Create transformed versions
x_scaled = 2 * x              # Amplitude Scaling
t_shifted = t - 2             # Time Shifting (right shift by 2)
x_shifted = np.sin(t_shifted)
x_folded = np.sin(-t)         # Time Folding

# All signals and labels
signals = [
    (t, x, "Original Signal"),
    (t, x_scaled, "Scaled Signal (x2)"),
    (t, x_shifted, "Shifted Signal (t-2)"),
    (t, x_folded, "Folded Signal (-t)")
]

colors = ["blue", "green", "orange", "red"]

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-2.5, 2.5)
ax.set_title("Signal Operations: Scaling, Shifting, Folding")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Amplitude")

line, = ax.plot([], [], lw=2)
text = ax.text(-5.5, 2, "", fontsize=12, color="black", bbox=dict(facecolor="white", alpha=0.7, edgecolor="black"))

def init():
    line.set_data([], [])
    text.set_text("")
    return line, text

def update(frame):
    t_vals, x_vals, label = signals[frame]
    line.set_data(t_vals, x_vals)
    line.set_color(colors[frame])
    text.set_text(label)
    return line, text

ani = animation.FuncAnimation(fig, update, frames=len(signals),
                              init_func=init, blit=True, interval=1500, repeat=True)

plt.show()
