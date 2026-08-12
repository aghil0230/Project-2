import json
import matplotlib.pyplot as plt

from fft_analysis import calculate_fft


SAMPLE_RATE = 1000


# Load signal data
with open("../data/samples/signal_samples.json", "r") as file:
    data = json.load(file)


normal_signal = data["normal_signal"]
anomaly_signal = data["anomaly_signal"]


# Calculate FFT
normal_freq, normal_mag = calculate_fft(
    normal_signal,
    SAMPLE_RATE
)

anomaly_freq, anomaly_mag = calculate_fft(
    anomaly_signal,
    SAMPLE_RATE
)


# Create frequency spectrum
plt.figure(figsize=(10, 5))

plt.plot(
    normal_freq,
    normal_mag,
    label="Normal Signal"
)

plt.plot(
    anomaly_freq,
    anomaly_mag,
    label="Anomalous Signal"
)


plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.title("AetherHound Frequency Spectrum")

plt.legend()
plt.grid(True)

plt.xlim(0, SAMPLE_RATE / 2)

plt.tight_layout()


# Save graph
plt.savefig(
    "../data/processed/frequency_spectrum.png"
)


print("Frequency spectrum saved.")
print(
    "File: ../data/processed/frequency_spectrum.png"
)
