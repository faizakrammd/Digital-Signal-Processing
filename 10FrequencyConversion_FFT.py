import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sampling parameters
Fs = 500          # Sampling frequency in Hz
T = 1             # Duration in seconds
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Signal: sum of two sine waves
f1, f2 = 5, 50    # Frequencies in Hz
x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# FFT setup
N = len(x)
freqs = np.fft.fftfreq(N, 1/Fs)[:N//2]  # Only positive frequencies

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))
ax1.set_title("Time-Domain Signal")
ax1.set_xlim(0, T)
ax1.set_ylim(-1.5, 1.5)
line_time, = ax1.plot([], [], color='b')

ax2.set_title("Frequency-Domain (FFT)")
ax2.set_xlim(0, Fs/2)
ax2.set_ylim(0, 1.2*np.max(np.abs(np.fft.fft(x))))
bars = ax2.bar(freqs, np.zeros(len(freqs)), width=Fs/N, color='m', alpha=0.7)

# Animation update function
def update(frame):
    # Time-domain update
    line_time.set_data(t[:frame], x[:frame])
    
    # Frequency-domain update
    X_frame = np.fft.fft(x[:frame]) if frame > 1 else np.fft.fft(x[:2])
    X_mag_frame = np.abs(X_frame)[:N//2]
    
    # Smoothly grow bars toward target height
    for rect, h in zip(bars, X_mag_frame):
        rect.set_height(rect.get_height() + (h - rect.get_height())*0.2)
    
    return [line_time] + list(bars)

# Animate
ani = FuncAnimation(fig, update, frames=N, interval=20, blit=True, repeat=True)

plt.tight_layout()
plt.show()
