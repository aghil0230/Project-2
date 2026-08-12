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

        # Normal 50 Hz signal
        normal_value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        # Simulated abnormal 200 Hz component
        anomaly_value = 0

        if 400 <= i <= 600:
            anomaly_value = 0.8 * math.sin(
                2 * math.pi * 200 * i / samples
            )

        # Background noise
        noise = random.uniform(-0.1, 0.1)

        signal.append(
            normal_value
            + anomaly_value
            + noise
        )

    return signal
