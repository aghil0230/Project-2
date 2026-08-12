import json

from mock_signal import generate_signal, generate_anomaly


normal_signal = generate_signal()
anomaly_signal = generate_anomaly()


data = {
    "normal_signal": normal_signal,
    "anomaly_signal": anomaly_signal
}


with open("data/samples/signal_samples.json", "w") as file:
    json.dump(data, file)


print("Signal samples saved successfully.")
print("File: data/samples/signal_samples.json")
