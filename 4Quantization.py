import numpy as np
import matplotlib.pyplot as plt

# Continuous signal (sine wave)
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t)

# Quantization function
def quantize(x, levels):
    x_min, x_max = -1, 1  # assume normalized signal
    step = (x_max - x_min) / (levels - 1)
    q_signal = np.round((x - x_min) / step) * step + x_min
    return q_signal

# Quantize with 4 levels and 16 levels
q4 = quantize(signal, 4)
q16 = quantize(signal, 16)

# Plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7,7), sharex=True)

ax1.plot(t, signal, 'b')
ax1.set_title("Original Signal")

ax2.plot(t, signal, 'b', alpha=0.4)
ax2.step(t, q4, 'r', where='mid')
ax2.set_title("Quantized with 4 Levels")

ax3.plot(t, signal, 'b', alpha=0.4)
ax3.step(t, q16, 'g', where='mid')
ax3.set_title("Quantized with 16 Levels")

plt.tight_layout()
plt.show()
