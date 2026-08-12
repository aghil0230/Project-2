import json

from fft_analysis import calculate_fft


SAMPLE_RATE = 1000


# Load signal data
with open("../data/samples/signal_samples.json", "r") as file:
    data = json.load(file)


results = {}


# Analyze both signals
for signal_name in [
    "normal_signal",
    "anomaly_signal"
]:

    frequencies, magnitude = calculate_fft(
        data[signal_name],
        SAMPLE_RATE
    )

    results[signal_name] = {
        "frequencies": frequencies.tolist(),
        "magnitude": magnitude.tolist()
    }


# Save results
with open(
    "../data/processed/fft_results.json",
    "w"
) as file:

    json.dump(results, file)


print("FFT results saved.")
print(
    "File: ../data/processed/fft_results.json"
)
