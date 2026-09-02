import json
import os

import numpy as np
import yaml

from fft_analysis import calculate_fft


# --------------------------------------------------
# Load configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CONFIG_FILE = os.path.join(
    BASE_DIR,
    "config",
    "config.yaml"
)


with open(CONFIG_FILE, "r") as file:
    config = yaml.safe_load(file)


# --------------------------------------------------
# Detection configuration
# --------------------------------------------------

SAMPLE_RATE = config["signal"]["sample_rate"]

ANOMALY_LOW = config["detection"]["frequency_band"]["low"]

ANOMALY_HIGH = config["detection"]["frequency_band"]["high"]

DETECTION_THRESHOLD = config["detection"]["threshold_percent"]


# --------------------------------------------------
# Frequency band analysis
# --------------------------------------------------

def analyze_frequency_band(signal):

    """
    Calculate the amount of energy present
    inside the configured frequency band.
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


# --------------------------------------------------
# Compare baseline and test signals
# --------------------------------------------------

def compare_signals(normal_signal, test_signal):

    """
    Compare a test signal against the
    normal baseline.
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

    if baseline == 0:
        percentage_change = 0

    else:
        percentage_change = (
            difference / baseline
        ) * 100

    return (
        baseline,
        test["band_energy"],
        percentage_change
    )


# --------------------------------------------------
# Standalone detector
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("     AetherHound Frequency Detector")
    print("=" * 50)

    print()
    print("Configuration loaded")
    print(
        f"Frequency Band : "
        f"{ANOMALY_LOW}-{ANOMALY_HIGH} Hz"
    )
    print(
        f"Threshold      : "
        f"{DETECTION_THRESHOLD}%"
    )

    # Load signals

    signal_file = os.path.join(
        BASE_DIR,
        "data",
        "samples",
        "signal_samples.json"
    )

    with open(signal_file, "r") as file:
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

    if change > DETECTION_THRESHOLD:

        print("⚠ ANOMALY DETECTED")

    else:

        print("✓ SIGNAL WITHIN BASELINE")

    print("\nAnalysis completed.")
