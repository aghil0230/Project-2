import json
from datetime import datetime
from anomaly_detector import (
    compare_signals,
    ANOMALY_LOW,
    ANOMALY_HIGH
)

DETECTION_THRESHOLD = 20


with open("data/samples/signal_samples.json", "r") as file:
    data = json.load(file)


baseline_signal = data["normal_signal"]
test_signal = data["anomaly_signal"]


baseline_energy, test_energy, change = compare_signals(
    baseline_signal,
    test_signal
)


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


detection = {
    "timestamp": datetime.now().isoformat(),
    "frequency_band": {
        "low_hz": ANOMALY_LOW,
        "high_hz": ANOMALY_HIGH
    },
    "detection_threshold_percent": DETECTION_THRESHOLD,
    "baseline_energy": baseline_energy,
    "test_energy": test_energy,
    "energy_change_percent": change,
    "result": result,
    "reason": reason
}


with open("data/processed/detection_results.json", "w") as file:
    json.dump(detection, file, indent=4)


print("AetherHound Detection Report")
print("=" * 50)
print(f"Frequency Band : {ANOMALY_LOW}-{ANOMALY_HIGH} Hz")
print(f"Baseline Energy: {baseline_energy:.2f}")
print(f"Test Energy    : {test_energy:.2f}")
print(f"Energy Change  : {change:.2f}%")
print(f"Threshold      : {DETECTION_THRESHOLD}%")
print(f"Result         : {result}")
print(f"Reason         : {reason}")
print()
print("Detection report saved.")
print("File: data/processed/detection_results.json")
