function [healthyPulseControl, depressedPulseControl] = processEEGAndDeterminePulse(healthy_eeg_data, depressed_eeg_data)
    % Define opts structure with all necessary fields before using it
    opts = struct('fs', 500, 'alpha', 2);
    
    % Process healthy EEG data
    healthyPulseControl = processSingleEEG(healthy_eeg_data, opts);
    
    % Process depressed EEG data
    depressedPulseControl = processSingleEEG(depressed_eeg_data, opts);
end

function pulseControl = processSingleEEG(eeg_data, opts)
    % Check if jfeeg function is compatible with MATLAB Coder.
    % If it's not, you would need to replace it with equivalent functionality
    % that is compatible with MATLAB Coder.
    
    % Hjorth Activity, Mobility, Complexity
    f1 = jfeeg('ha', eeg_data, opts);
    f2 = jfeeg('hm', eeg_data, opts);
    f3 = jfeeg('hc', eeg_data, opts);

    % Feature vector for Hjorth features (not used further in this function)
    % hjorth_feat = [f1, f2, f3];

    % Band Power Alpha
    f4 = jfeeg('bpa', eeg_data, opts);
    
    % Tsallis Entropy
    f5 = jfeeg('te', eeg_data, opts);

    % Define threshold values for determining pulseControl
    threshold_activity = 0.1; % Adjust as needed
    threshold_tsallis_entropy = 0.2; % Adjust as needed
    
    % Evaluate the condition for pulse generation
    pulseControl = (f1 > threshold_activity) && (f5 > threshold_tsallis_entropy);
end
