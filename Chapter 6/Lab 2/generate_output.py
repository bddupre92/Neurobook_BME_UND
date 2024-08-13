def generate_output_commands(clf, features):
    predictions = clf.predict(features)
    commands = ["Stimulate" if p == 1 else "No Stimulate" for p in predictions]
    return commands

if __name__ == "__main__":
    from simulate_eeg import generate_eeg_signals
    from extract_features import extract_features, train_classifier

    num_samples = 1000
    num_signals = 10
    fs = 1000  # Sampling frequency

    healthy_signals, depressed_signals = generate_eeg_signals(num_samples, num_signals, fs)
    healthy_features = extract_features(healthy_signals)
    depressed_features = extract_features(depressed_signals)

    clf = train_classifier(healthy_features, depressed_features)

    # Combine features for command generation
    all_features = np.vstack((healthy_features, depressed_features))
    commands = generate_output_commands(clf, all_features)
    print("Output Commands:", commands)
