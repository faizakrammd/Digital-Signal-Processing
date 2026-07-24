import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate a signal (sum of two sine waves)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2 * np.pi * 5 * t) + 0.6 * np.sin(2 * np.pi * 15 * t)

# Apply FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(X), 1/fs)

# IFFT Reconstruction
x_reconstructed = np.fft.ifft(X).real

# Setup the figure
fig, axs = plt.subplots(3, 1, figsize=(8, 8))
lines = []

# Original signal plot
axs[0].set_title("Original Signal (Time Domain)")
axs[0].set_xlim(0, 1)
axs[0].set_ylim(-2, 2)
line1, = axs[0].plot([], [], 'b')
lines.append(line1)

# FFT Magnitude Spectrum
axs[1].set_title("FFT Magnitude Spectrum")
axs[1].set_xlim(0, 50)  # Show only positive frequencies
axs[1].set_ylim(0, max(abs(X)) * 0.6)
bar_container = axs[1].bar([], [], width=0.5)
lines.append(bar_container)

# IFFT Reconstruction
axs[2].set_title("Reconstructed Signal via IFFT")
axs[2].set_xlim(0, 1)
axs[2].set_ylim(-2, 2)
line3, = axs[2].plot([], [], 'g')
lines.append(line3)

# Animation Update Function
def update(frame):
    # Update original signal line
    line1.set_data(t[:frame], x[:frame])
    
    # Update FFT spectrum bars
    axs[1].cla()
    axs[1].set_title("FFT Magnitude Spectrum")
    axs[1].set_xlim(0, 50)
    axs[1].set_ylim(0, max(abs(X)) * 0.6)
    axs[1].bar(freqs[:frame], abs(X)[:frame], width=1)
    
    # Update IFFT reconstructed signal
    line3.set_data(t[:frame], x_reconstructed[:frame])
    
    return lines

# Animate
ani = FuncAnimation(fig, update, frames=fs, interval=10, blit=False, repeat=True)

plt.tight_layout()
plt.show()
