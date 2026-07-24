import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Two example signals
x = np.array([1, 2, 3, 2, 1])
h = np.array([1, -1, 2])

N = len(x)
M = len(h)
L = N + M - 1  # length of convolution

y = np.convolve(x, h)

# Time indices
n = np.arange(N)
m = np.arange(M)
k = np.arange(L)

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6))
fig.suptitle("Linear Convolution", fontsize=14)

# Input signals
ax1.stem(n, x, linefmt="b-", markerfmt="bo", basefmt=" ")
ax1.stem(m, h, linefmt="g-", markerfmt="go", basefmt=" ")
ax1.set_title("Input Signals: x[n] and h[n]")
ax1.set_xlim(-1, max(N, M) + 5)
ax1.set_ylim(min(x.min(), h.min()) - 1, max(x.max(), h.max()) + 2)
ax1.legend(["x[n]", "h[n]"])
ax1.grid()

# Convolution output
ax2.set_xlim(-1, L + 1)
ax2.set_ylim(y.min() - 1, y.max() + 2)
ax2.set_title("Convolution Output y[n]")
ax2.set_xlabel("n")
ax2.set_ylabel("Amplitude")
ax2.grid()

def update(frame):
    ax2.cla()  # clear previous frame
    ax2.stem(k[:frame+1], y[:frame+1], linefmt="r-", markerfmt="ro", basefmt=" ")
    ax2.set_xlim(-1, L + 1)
    ax2.set_ylim(y.min() - 1, y.max() + 2)
    ax2.set_title("Convolution Output y[n]")
    ax2.set_xlabel("n")
    ax2.set_ylabel("Amplitude")
    ax2.grid()

ani = FuncAnimation(fig, update, frames=L, blit=False, interval=800, repeat=False)

plt.tight_layout()
plt.show()
