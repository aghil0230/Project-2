import json
import numpy as np


SAMPLE_RATE = 1000


def calculate_fft(signal, sample_rate):
    signal_array = np.array(signal)

    number_of_samples = len(signal_array)

    # Perform Fast Fourier Transform
    fft_result = np.fft.fft(signal_array)

    # Calculate corresponding frequencies
    frequencies = np.fft.fftfreq(
        number_of_samples,
        d=1 / sample_rate
    )

    # Calculate magnitude
    magnitude = np.abs(fft_result)

    # Only keep positive frequencies
    positive_frequencies = frequencies[:number_of_samples // 2]
    positive_magnitude = magnitude[:number_of_samples // 2]

    return positive_frequencies, positive_magnitude


def find_dominant_frequency(frequencies, magnitude):
    index = np.argmax(magnitude)

    return frequencies[index], magnitude[index]


if __name__ == "__main__":

    print("=" * 50)
    print("       AetherHound FFT Analysis")
    print("=" * 50)

    # Load previously generated signal data
    with open("data/samples/signal_samples.json", "r") as file:
        data = json.load(file)

    normal_signal = data["normal_signal"]
    anomaly_signal = data["anomaly_signal"]

    # Analyze normal signal
    normal_freq, normal_mag = calculate_fft(
        normal_signal,
        SAMPLE_RATE
    )

    normal_dominant_freq, normal_dominant_mag = \
        find_dominant_frequency(
            normal_freq,
            normal_mag
        )

    # Analyze anomalous signal
    anomaly_freq, anomaly_mag = calculate_fft(
        anomaly_signal,
        SAMPLE_RATE
    )

    anomaly_dominant_freq, anomaly_dominant_mag = \
        find_dominant_frequency(
            anomaly_freq,
            anomaly_mag
        )

    print("\nNormal Signal")
    print("--------------------")
    print(
        f"Dominant Frequency : "
        f"{normal_dominant_freq:.2f} Hz"
    )
    print(
        f"Dominant Magnitude : "
        f"{normal_dominant_mag:.2f}"
    )

    print("\nAnomalous Signal")
    print("--------------------")
    print(
        f"Dominant Frequency : "
        f"{anomaly_dominant_freq:.2f} Hz"
    )
    print(
        f"Dominant Magnitude : "
        f"{anomaly_dominant_mag:.2f}"
    )

    print("\nFFT analysis completed.")
