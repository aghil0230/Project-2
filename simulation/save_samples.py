import json

from mock_signal import (
    generate_signal,
    generate_anomaly,
    generate_amplitude_anomaly,
    generate_frequency_shift,
    generate_burst_anomaly
)


# Generate signals

normal_signal = generate_signal()

high_frequency_anomaly = generate_anomaly()

amplitude_anomaly = generate_amplitude_anomaly()

frequency_shift_anomaly = generate_frequency_shift()

burst_anomaly = generate_burst_anomaly()


# Store all signals

data = {
    "normal_signal": normal_signal,
    "anomaly_signal": high_frequency_anomaly,
    "amplitude_anomaly": amplitude_anomaly,
    "frequency_shift_anomaly": frequency_shift_anomaly,
    "burst_anomaly": burst_anomaly
}


# Save signals

with open("data/samples/signal_samples.json", "w") as file:

    json.dump(
        data,
        file,
        indent=4
    )


print("Signal samples saved successfully.")

print("Signals generated:")
print(" - Normal signal")
print(" - High-frequency anomaly")
print(" - Amplitude anomaly")
print(" - Frequency-shift anomaly")
print(" - Burst anomaly")

print()
print("File: data/samples/signal_samples.json")
