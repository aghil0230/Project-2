import math
import random


def generate_signal(samples=1000, frequency=50, noise_level=0.1):
    """
    Generate a normal sinusoidal signal with background noise.
    """

    signal = []

    for i in range(samples):

        noise = random.uniform(-noise_level, noise_level)

        value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        signal.append(value + noise)

    return signal


def generate_anomaly(samples=1000, frequency=50):
    """
    Generate the original Week 1 anomaly.

    A 200 Hz component is injected into the normal
    50 Hz signal between samples 400 and 600.
    """

    signal = []

    for i in range(samples):

        normal_value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        anomaly_value = 0

        if 400 <= i <= 600:

            anomaly_value = 0.8 * math.sin(
                2 * math.pi * 200 * i / samples
            )

        noise = random.uniform(-0.1, 0.1)

        signal.append(
            normal_value
            + anomaly_value
            + noise
        )

    return signal


def generate_amplitude_anomaly(samples=1000, frequency=50):
    """
    Generate an amplitude anomaly.

    The signal amplitude becomes significantly larger
    during the middle portion of the signal.
    """

    signal = []

    for i in range(samples):

        amplitude = 1.0

        if 400 <= i <= 600:
            amplitude = 2.5

        value = amplitude * math.sin(
            2 * math.pi * frequency * i / samples
        )

        noise = random.uniform(-0.1, 0.1)

        signal.append(value + noise)

    return signal


def generate_frequency_shift(samples=1000, frequency=50):
    """
    Generate a frequency-shift anomaly.

    The normal signal is 50 Hz, but during the middle
    portion it changes to 80 Hz.
    """

    signal = []

    for i in range(samples):

        current_frequency = frequency

        if 400 <= i <= 600:
            current_frequency = 80

        value = math.sin(
            2 * math.pi * current_frequency * i / samples
        )

        noise = random.uniform(-0.1, 0.1)

        signal.append(value + noise)

    return signal


def generate_burst_anomaly(samples=1000, frequency=50):
    """
    Generate a short high-amplitude burst anomaly.
    """

    signal = []

    for i in range(samples):

        normal_value = math.sin(
            2 * math.pi * frequency * i / samples
        )

        burst = 0

        if 450 <= i <= 500:

            burst = random.uniform(2.0, 3.0)

        noise = random.uniform(-0.1, 0.1)

        signal.append(
            normal_value
            + burst
            + noise
        )

    return signal
