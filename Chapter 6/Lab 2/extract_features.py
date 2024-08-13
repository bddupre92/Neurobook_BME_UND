import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def extract_features(eeg_signals):
    features = []
    for signal in eeg_signals:
        # Example feature extraction (mean, variance)
        mean = np.mean(signal)
        var = np.var(signal)
        features.append([mean, var])
    return np.array(features)

def train_classifier(healthy_features, depressed_features):
    labels = np.array([0] * len(healthy_features) + [1] * len(depressed_features))
    features = np.vstack((healthy_features, depressed_features))

    clf = make_pipeline(StandardScaler(), SVC(kernel='linear'))
    clf.fit(features, labels)
    return clf

if __name__ == "__main__":
    from simulate_eeg import generate_eeg_signals

    num_samples = 1000
    num_signals = 10
    fs = 1000  # Sampling frequency

    healthy_signals, depressed_signals = generate_eeg_signals(num_samples, num_signals, fs)
    healthy_features = extract_features(healthy_signals)
    depressed_features = extract_features(depressed_signals)

    clf = train_classifier(healthy_features, depressed_features)
    print("Classifier accuracy:", clf.score(np.vstack((healthy_features, depressed_features)), 
                                            np.array([0] * len(healthy_features) + [1] * len(depressed_features))))
