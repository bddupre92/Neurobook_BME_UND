from simulate_eeg import generate_eeg_signals, plot_eeg_signals
from extract_features import extract_features, train_classifier
from generate_output import generate_output_commands

def main():
    num_samples = 1000
    num_signals = 10
    fs = 1000  # Sampling frequency

    # Step 1: Simulate EEG signals
    healthy_signals, depressed_signals = generate_eeg_signals(num_samples, num_signals, fs)
    plot_eeg_signals(healthy_signals, depressed_signals)

    # Step 2: Extract features
    healthy_features = extract_features(healthy_signals)
    depressed_features = extract_features(depressed_signals)

    # Step 3: Train classifier
    clf = train_classifier(healthy_features, depressed_features)
    accuracy = clf.score(np.vstack((healthy_features, depressed_features)), 
                         np.array([0] * len(healthy_features) + [1] * len(depressed_features)))
    print("Classifier accuracy:", accuracy)

    # Step 4: Generate output commands
    all_features = np.vstack((healthy_features, depressed_features))
    commands = generate_output_commands(clf, all_features)
    print("Output Commands:", commands)

if __name__ == "__main__":
    main()
