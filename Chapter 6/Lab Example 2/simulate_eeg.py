import numpy as np
import matplotlib.pyplot as plt

def generate_eeg_signals(num_samples, num_signals, fs):
    t = np.linspace(0, (num_samples-1)/fs, num_samples)
    healthy_signals = []
    depressed_signals = []

    for _ in range(num_signals):
        if np.random.rand() > 0.5:
            # Depressed condition
            signal = (0.5 * np.sin(2 * np.pi * 10 * t) +
                      0.3 * np.sin(2 * np.pi * 20 * t) +
                      0.2 * np.sin(2 * np.pi * 6 * t) +
                      0.1 * np.sin(2 * np.pi * 2 * t))
            signal += 0.1 * np.random.randn(num_samples)
            depressed_signals.append(signal)
        else:
            # Healthy condition
            signal = (0.4 * np.sin(2 * np.pi * 15 * t) +
                      0.2 * np.sin(2 * np.pi * 25 * t) +
                      0.1 * np.sin(2 * np.pi * 9 * t) +
                      0.3 * np.sin(2 * np.pi * 5 * t))
            signal += 0.1 * np.random.randn(num_samples)
            healthy_signals.append(signal)

    return np.array(healthy_signals), np.array(depressed_signals)

def plot_eeg_signals(healthy_signals, depressed_signals):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(healthy_signals.T)
    plt.title('Healthy EEG Signals')
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.plot(depressed_signals.T)
    plt.title('Depressed EEG Signals')
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    num_samples = 1000
    num_signals = 10
    fs = 1000  # Sampling frequency

    healthy_signals, depressed_signals = generate_eeg_signals(num_samples, num_signals, fs)
    plot_eeg_signals(healthy_signals, depressed_signals)
