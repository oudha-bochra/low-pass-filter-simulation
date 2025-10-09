import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# 1️⃣ Create the signal (Sine wave + Noise)
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 2, 2 * fs, endpoint=False)  # Time axis
signal = np.sin(2 * np.pi * 5 * t)             # Low-frequency signal (5 Hz)
noise = np.sin(2 * np.pi * 50 * t)             # High-frequency noise (50 Hz)
noisy_signal = signal + 0.5 * noise            # Combined signal (with noise)

# 2️⃣ Design a Low-Pass Butterworth Filter
cutoff = 10     # Cutoff frequency (Hz)
order = 4       # Filter order
b, a = butter(order, cutoff / (0.5 * fs), btype='low', analog=False)

# 3️⃣ Apply the filter to the noisy signal
filtered_signal = filtfilt(b, a, noisy_signal)

# 4️⃣ Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal, color='r', label='Noisy Signal')
plt.plot(t, signal, color='g', linestyle='--', label='Original Signal')
plt.title('Original + Noisy Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, color='b', label='Filtered Signal (Low Pass)')
plt.title('After Low Pass Filter')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
