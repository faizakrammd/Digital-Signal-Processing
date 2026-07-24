import numpy as np
import matplotlib.pyplot as plt

# Original continuous signal (5 Hz sine wave)
f = 5   # frequency of signal
t_cont = np.linspace(0, 1, 1000)
signal_cont = np.sin(2 * np.pi * f * t_cont)

# High sampling rate (40 Hz) -> above Nyquist
fs_high = 40
t_high = np.arange(0, 1, 1/fs_high)
signal_high = np.sin(2 * np.pi * f * t_high)

# Low sampling rate (6 Hz) -> below Nyquist
fs_low = 6
t_low = np.arange(0, 1, 1/fs_low)
signal_low = np.sin(2 * np.pi * f * t_low)

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7,6), sharex=True)

# High-rate sampling
ax1.plot(t_cont, signal_cont, 'b', label="Continuous")
ax1.stem(t_high, signal_high, linefmt='r-', markerfmt='ro', basefmt=" ", label="Sampled (40 Hz)")
ax1.set_title("Sampling above Nyquist (Accurate)")
ax1.legend()

# Low-rate sampling
ax2.plot(t_cont, signal_cont, 'b', label="Continuous")
ax2.stem(t_low, signal_low, linefmt='g-', markerfmt='go', basefmt=" ", label="Sampled (6 Hz)")
ax2.set_title("Sampling below Nyquist (Distorted)")
ax2.legend()

plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
