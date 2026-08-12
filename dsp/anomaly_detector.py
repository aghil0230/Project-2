import json

import numpy as np

from fft_analysis import calculate_fft


SAMPLE_RATE = 1000

# Frequency band used to measure abnormal energy
ANOMALY_LOW = 180
ANOMALY_HIGH = 220


def analyze_frequency_band(signal):
    """
    Calculate the amount of energy present
    inside the selected frequency band.
    """

    frequencies, magnitude = calculate_fft(
        signal,
        SAMPLE_RATE
    )

    band = (
        (frequencies >= ANOMALY_LOW)
        &
        (frequencies <= ANOMALY_HIGH)
    )

    band_energy = np.sum(
        magnitude[band] ** 2
    )

    return {
        "band_energy": float(band_energy),
        "frequencies": frequencies,
        "magnitude": magnitude
    }


def compare_signals(normal_signal, test_signal):
    """
    Compare a test signal against the normal baseline.
    """

    normal = analyze_frequency_band(
        normal_signal
    )

    test = analyze_frequency_band(
        test_signal
    )

    baseline = normal["band_energy"]

    difference = (
        test["band_energy"] - baseline
    )

    percentage_change = (
        difference / baseline
    ) * 100

    return (
        baseline,
        test["band_energy"],
        percentage_change
    )


if __name__ == "__main__":

    print("=" * 50)
    print("     AetherHound Frequency Detector")
    print("=" * 50)

    # Load signals
    with open(
        "../data/samples/signal_samples.json",
        "r"
    ) as file:

        data = json.load(file)

    normal_signal = data["normal_signal"]
    anomaly_signal = data["anomaly_signal"]

    # Compare signals
    baseline, test_energy, change = compare_signals(
        normal_signal,
        anomaly_signal
    )

    print("\nBaseline Signal")
    print("--------------------")

    print(
        f"Frequency Band : "
        f"{ANOMALY_LOW}-{ANOMALY_HIGH} Hz"
    )

    print(
        f"Band Energy    : "
        f"{baseline:.2f}"
    )

    print("\nTest Signal")
    print("--------------------")

    print(
        f"Band Energy    : "
        f"{test_energy:.2f}"
    )

    print(
        f"Energy Change  : "
        f"{change:.2f}%"
    )

    print("\nDetection Result")
    print("--------------------")

    if change > 20:

        print("⚠ ANOMALY DETECTED")

    else:

        print("✓ SIGNAL WITHIN BASELINE")

    print("\nAnalysis completed.")
