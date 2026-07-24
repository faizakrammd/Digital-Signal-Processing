import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Example signals
x = [1, 2, 1]
h = [1, -1, 2]

# Linear convolution
y_lin = np.convolve(x, h)

# Circular convolution using FFT
N = max(len(x), len(h))  # take max length
X = np.fft.fft(x, N)
H = np.fft.fft(h, N)
y_circ = np.fft.ifft(X * H).real

# Setup plot
fig, ax = plt.subplots(2, 1, figsize=(6, 6))

# Plot input signals
ax[0].stem(range(len(x)), x, linefmt="b-", markerfmt="bo", basefmt=" ")
ax[0].stem(range(len(h)), h, linefmt="g-", markerfmt="go", basefmt=" ")
ax[0].set_title("Signals: x[n] (blue) and h[n] (green)")

# Configure convolution subplot
ax[1].set_xlim(-1, max(len(y_lin), len(y_circ)))
ax[1].set_ylim(min(min(y_lin), min(y_circ)) - 1,
               max(max(y_lin), max(y_circ)) + 2)
ax[1].set_title("Linear (red) vs Circular (magenta) Convolution")

def update(frame):
    ax[1].cla()
    ax[1].stem(range(len(y_lin[:frame+1])), y_lin[:frame+1], linefmt="r-", markerfmt="ro", basefmt=" ")
    ax[1].stem(range(len(y_circ[:min(frame+1, len(y_circ))])), 
               y_circ[:min(frame+1, len(y_circ))], 
               linefmt="m-", markerfmt="mo", basefmt=" ")
    ax[1].set_xlim(-1, max(len(y_lin), len(y_circ)))
    ax[1].set_ylim(min(min(y_lin), min(y_circ)) - 1,
                   max(max(y_lin), max(y_circ)) + 2)
    ax[1].set_title("Linear (red) vs Circular (magenta) Convolution")

# repeat=True makes it loop forever
ani = FuncAnimation(fig, update, frames=len(y_lin), interval=800, repeat=True)

plt.tight_layout()
plt.show()
