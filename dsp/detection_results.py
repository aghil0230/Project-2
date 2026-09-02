import json
import os
from datetime import datetime

import yaml

from anomaly_detector import (
    compare_signals,
    ANOMALY_LOW,
    ANOMALY_HIGH,
    DETECTION_THRESHOLD
)


# --------------------------------------------------
# Project paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


CONFIG_FILE = os.path.join(
    BASE_DIR,
    "config",
    "config.yaml"
)


SIGNAL_FILE = os.path.join(
    BASE_DIR,
    "data",
    "samples",
    "signal_samples.json"
)


OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "detection_results.json"
)


# --------------------------------------------------
# Load configuration
# --------------------------------------------------

with open(CONFIG_FILE, "r") as file:

    config = yaml.safe_load(file)


# --------------------------------------------------
# Load signals
# --------------------------------------------------

with open(SIGNAL_FILE, "r") as file:

    data = json.load(file)


baseline_signal = data["normal_signal"]

test_signal = data["anomaly_signal"]


# --------------------------------------------------
# Compare signals
# --------------------------------------------------

baseline_energy, test_energy, change = compare_signals(
    baseline_signal,
    test_signal
)


# --------------------------------------------------
# Detection decision
# --------------------------------------------------

if change > DETECTION_THRESHOLD:

    result = "ANOMALY"

    reason = (
        f"Energy increased by {change:.2f}% "
        f"within the monitored frequency band."
    )

else:

    result = "NORMAL"

    reason = (
        f"Energy change of {change:.2f}% "
        f"is below the detection threshold."
    )


# --------------------------------------------------
# Create detection report
# --------------------------------------------------

detection = {

    "timestamp": datetime.now().isoformat(),

    "frequency_band": {
        "low_hz": ANOMALY_LOW,
        "high_hz": ANOMALY_HIGH
    },

    "detection_threshold_percent":
        DETECTION_THRESHOLD,

    "baseline_energy":
        baseline_energy,

    "test_energy":
        test_energy,

    "energy_change_percent":
        change,

    "result":
        result,

    "reason":
        reason
}


# --------------------------------------------------
# Save report
# --------------------------------------------------

with open(OUTPUT_FILE, "w") as file:

    json.dump(
        detection,
        file,
        indent=4
    )


# --------------------------------------------------
# Display report
# --------------------------------------------------

print("AetherHound Detection Report")

print("=" * 50)

print(
    f"Frequency Band : "
    f"{ANOMALY_LOW}-{ANOMALY_HIGH} Hz"
)

print(
    f"Baseline Energy: "
    f"{baseline_energy:.2f}"
)

print(
    f"Test Energy    : "
    f"{test_energy:.2f}"
)

print(
    f"Energy Change  : "
    f"{change:.2f}%"
)

print(
    f"Threshold      : "
    f"{DETECTION_THRESHOLD}%"
)

print(
    f"Result         : "
    f"{result}"
)

print(
    f"Reason         : "
    f"{reason}"
)

print()

print("Detection report saved.")

print(
    "File: data/processed/detection_results.json"
)
