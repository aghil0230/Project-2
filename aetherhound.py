import subprocess
import sys
from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parent
DSP_DIR = PROJECT_ROOT / "dsp"


print("=" * 50)
print("        AetherHound")
print("        Air-Gapped RF & Acoustic Detector")
print("=" * 50)

print()
print("Starting AetherHound analysis pipeline...")
print()


steps = [
    ("FFT Analysis", DSP_DIR / "fft_analysis.py", PROJECT_ROOT),
    ("Anomaly Detection", DSP_DIR / "anomaly_detector.py", DSP_DIR),
    ("Detection Report", DSP_DIR / "detection_results.py", PROJECT_ROOT),
    ("Frequency Spectrum", DSP_DIR / "plot_spectrum.py", DSP_DIR)
]


for name, script, working_directory in steps:

    print("=" * 50)
    print(f"Running: {name}")
    print("=" * 50)

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(working_directory)
    )

    if result.returncode != 0:
        print()
        print(f"ERROR: {name} failed.")
        sys.exit(1)

    print()
    print(f"{name} completed successfully.")
    print()


print("=" * 50)
print("AetherHound Pipeline Completed")
print("=" * 50)

print()
print("Results:")
print(" - FFT analysis completed")
print(" - Frequency anomaly detection completed")
print(" - Detection report generated")
print(" - Frequency spectrum generated")
print()
print("AetherHound analysis completed successfully.")
