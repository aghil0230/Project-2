import json
from datetime import datetime

from anomaly_detector import compare_signals


with open(
    "../data/samples/signal_samples.json",
    "r"
) as file:

    data = json.load(file)


baseline = data["normal_signal"]
test_signal = data["anomaly_signal"]


normal_energy, test_energy, change = compare_signals(
    baseline,
    test_signal
)


if change > 20:

    result = "ANOMALY"

else:

    result = "NORMAL"


detection = {
    "timestamp": datetime.now().isoformat(),
    "baseline_energy": normal_energy,
    "test_energy": test_energy,
    "energy_change_percent": change,
    "result": result
}


with open(
    "../data/processed/detection_results.json",
    "w"
) as file:

    json.dump(
        detection,
        file,
        indent=4
    )


print("Detection result saved.")
print(
    "File: ../data/processed/detection_results.json"
)
