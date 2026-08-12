import math
import random


def generate_signal(samples=1000, frequency=50):
    signal = []

    for i in range(samples):
        noise = random.uniform(-0.1, 0.1)
        value = math.sin(2 * math.pi * frequency * i / samples)
        signal.append(value + noise)

    return signal


if __name__ == "__main__":
    signal = generate_signal()

    print("AetherHound Mock Signal Generator")
    print("---------------------------------")
    print(f"Samples generated : {len(signal)}")
    print(f"First 10 samples  : {signal[:10]}")
