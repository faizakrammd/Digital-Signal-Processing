import numpy as np
import matplotlib.pyplot as plt

# Continuous signal
t_cont = np.linspace(0, 1, 1000)
signal_cont = np.sin(2 * np.pi * 5 * t_cont)

# Discrete signal (sample every 0.05s)
t_disc = np.arange(0, 1.05, 0.05)
signal_disc = np.sin(2 * np.pi * 5 * t_disc)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,6), sharex=True)

# Plot continuous
ax1.plot(t_cont, signal_cont, color="blue")
ax1.set_title("Continuous Signal")
ax1.set_ylabel("Amplitude")

# Plot discrete
ax2.stem(t_disc, signal_disc, linefmt='r-', markerfmt='ro', basefmt=" ")
ax2.set_title("Discrete Signal")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Amplitude")

plt.tight_layout()
plt.show()
