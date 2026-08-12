import math
import random


def generate_signal(samples=1000, frequency=50, noise_level=0.1):
    signal = []

    for i in range(samples):
        noise = random.uniform(-noise_level, noise_level)

        value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        signal.append(value + noise)

    return signal


def generate_anomaly(samples=1000, frequency=50):
    signal = []

    for i in range(samples):

        # Normal signal
        value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        # Add a stronger disturbance
        if 400 <= i <= 600:
            value += random.uniform(0.8, 1.2)

        # Normal background noise
        value += random.uniform(-0.1, 0.1)

        signal.append(value)

    return signal


if __name__ == "__main__":

    print("=" * 50)
    print("      AetherHound Signal Simulator")
    print("=" * 50)

    normal_signal = generate_signal()

    anomaly_signal = generate_anomaly()

    print("\nNormal Signal")
    print("--------------------")
    print(f"Samples : {len(normal_signal)}")
    print(f"Minimum : {min(normal_signal):.4f}")
    print(f"Maximum : {max(normal_signal):.4f}")
    print(f"Average : {sum(normal_signal) / len(normal_signal):.4f}")

    print("\nAnomalous Signal")
    print("--------------------")
    print(f"Samples : {len(anomaly_signal)}")
    print(f"Minimum : {min(anomaly_signal):.4f}")
    print(f"Maximum : {max(anomaly_signal):.4f}")
    print(f"Average : {sum(anomaly_signal) / len(anomaly_signal):.4f}")

    print("\nSignal generation completed.")
