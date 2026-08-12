import numpy as np


def analyze_signal(signal):
    signal_array = np.array(signal)

    analysis = {
        "samples": len(signal_array),
        "minimum": np.min(signal_array),
        "maximum": np.max(signal_array),
        "mean": np.mean(signal_array),
        "standard_deviation": np.std(signal_array),
        "energy": np.sum(signal_array ** 2)
    }

    return analysis


if __name__ == "__main__":

    test_signal = np.sin(
        np.linspace(0, 2 * np.pi, 1000)
    )

    result = analyze_signal(test_signal)

    print("AetherHound Signal Analysis")
    print("---------------------------")

    for key, value in result.items():

        if isinstance(value, float):
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")
