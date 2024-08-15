# Chapter 4: Lab Example 1 

 

Following this step-by-step laboratory exercise using MATLAB to perform the EEG signal processing as illustrated in your example. You will need the Signal Processing Toolbox to complete this lab. By the end of the exercise, you should be able to generate and analyze EEG signals, simulate different brain states, add noise, amplify signals, apply filters, and visualize the results. 

 

## EEG Signal Processing in MATLAB 

 

### Objective 

This exercise aims to understand and analyze EEG signals by generating synthetic EEG signals, simulating different brain states, adding noise, amplifying signals, filtering, and visualizing the results. 

 

### Materials Needed 

- MATLAB software 

- Signal Processing Toolbox 

- Computer with sufficient computational capabilities 

 

### Exercise Instructions 

 

#### Step 1: Set Up the MATLAB Environment 

1. Open MATLAB. 

2. Create a new script and name it `EEG_Signal_Processing.m`. 

 

#### Step 2: Define the Parameters 

 

```matlab 

Fs = 1000; % Sampling frequency in Hz 

T = 10; % Duration of the signal in seconds 

t = 0:1/Fs:T-1/Fs; % Time vector 

``` 

 

#### Step 3: Generate Awake and Drowsy EEG Signals 

 

```matlab 

% Generate awake EEG signal with alpha and beta waves 

awake_alpha_wave = 0.7 * sin(2*pi*10*t); 

awake_beta_wave = 0.5 * sin(2*pi*20*t); 

awake_eeg_signal = awake_alpha_wave + awake_beta_wave; 

 

% Generate normal drowsy EEG signal with lower amplitude alpha and beta waves 

drowsy_alpha_wave = 0.3 * sin(2*pi*10*t); 

drowsy_beta_wave = 0.2 * sin(2*pi*20*t); 

drowsy_eeg_signal = drowsy_alpha_wave + drowsy_beta_wave; 

``` 

 

#### Step 4: Simulate Epileptiform Activity in Drowsy EEG 

 

```matlab 

epileptiform_start = 3; % Time point (in seconds) to start epileptiform activity 

epileptiform_duration = 1; % Duration of epileptiform activity 

epileptiform_amplitude = 1.5; % Amplitude of epileptiform spikes 

 

epileptiform_signal = zeros(size(t)); 

epileptiform_indices = find(t >= epileptiform_start & t < (epileptiform_start + epileptiform_duration)); 

epileptiform_signal(epileptiform_indices) = epileptiform_amplitude * square(2*pi*5*(t(epileptiform_indices)-epileptiform_start)); 

 

drowsy_eeg_with_epileptiform = drowsy_eeg_signal + epileptiform_signal; 

``` 

 

#### Step 5: Add Noise to Simulate Real-World EEG Signals 

 

```matlab 

noise_level = 0.1; 

noisy_awake_alpha = awake_alpha_wave + noise_level * randn(size(t)); 

noisy_awake_beta = awake_beta_wave + noise_level * randn(size(t)); 

noisy_drowsy_alpha = drowsy_alpha_wave + noise_level * randn(size(t)); 

noisy_drowsy_beta = drowsy_beta_wave + noise_level * randn(size(t)); 

noisy_drowsy_with_epileptiform = drowsy_eeg_with_epileptiform + noise_level * randn(size(t)); 

 

% Combine noisy signals 

awakeEEGSignal = noisy_awake_alpha + noisy_awake_beta; 

drowsyEEGSignal = noisy_drowsy_alpha + noisy_drowsy_beta; 

drowsyEEGWithEpileptiformSignal = noisy_drowsy_with_epileptiform; 

``` 

 

#### Step 6: Amplify the Signals 

 

```matlab 

amplificationFactor = 2; 

amplifiedAwakeSignal = awakeEEGSignal * amplificationFactor; 

amplifiedDrowsySignal = drowsyEEGSignal * amplificationFactor; 

amplifiedDrowsyWithEpileptiformSignal = drowsyEEGWithEpileptiformSignal * amplificationFactor; 

``` 

 

#### Step 7: Design and Apply a Low-Pass FIR Filter 

 

```matlab 

Fc = 30;        % Cutoff frequency 

order = 100;    % Filter order 

 

% Design a low-pass FIR filter 

d = designfilt('lowpassfir', 'FilterOrder', order, ... 

               'CutoffFrequency', Fc, 'SampleRate', Fs, ... 

               'DesignMethod', 'window', 'Window', 'hamming'); 

 

% Filter the amplified signals 

filteredAmplifiedAwakeEEG = filter(d, amplifiedAwakeSignal); 

filteredAmplifiedDrowsyEEG = filter(d, amplifiedDrowsySignal); 

filteredAmplifiedDrowsyWithEpileptiformEEG = filter(d, amplifiedDrowsyWithEpileptiformSignal); 

``` 

 

#### Step 8: Apply Zero-Phase Filtering 

 

```matlab 

filteredAmplifiedAwakeEEG_zeroPhase = filtfilt(d, amplifiedAwakeSignal); 

filteredAmplifiedDrowsyEEG_zeroPhase = filtfilt(d, amplifiedDrowsySignal); 

filteredAmplifiedDrowsyWithEpileptiformEEG_zeroPhase = filtfilt(d, amplifiedDrowsyWithEpileptiformSignal); 

``` 

 

#### Step 9: Plotting the Results 

 

```matlab 

% Define a common y-axis range for all plots 

yAxisRange = [-3.5 3.5];  % This range might need adjustment based on actual signal amplitudes 

 

figure; 

% Awake EEG Signals 

subplot(431); 

plot(t, awakeEEGSignal); 

title('Awake EEG Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(434); 

plot(t, amplifiedAwakeSignal); 

title('Amplified Awake Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(437); 

plot(t, filteredAmplifiedAwakeEEG); 

title('Filtered Amplified Awake Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(4310); 

plot(t, filteredAmplifiedAwakeEEG_zeroPhase); 

title('Zero-Phase Filtered Awake Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

% Normal Drowsy EEG Signals 

subplot(432); 

plot(t, drowsyEEGSignal); 

title('Normal Drowsy EEG Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(435); 

plot(t, amplifiedDrowsySignal); 

title('Amplified Drowsy Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(438); 

plot(t, filteredAmplifiedDrowsyEEG); 

title('Filtered Amplified Drowsy Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(4311); 

plot(t, filteredAmplifiedDrowsyEEG_zeroPhase); 

title('Zero-Phase Filtered Drowsy Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

% Drowsy EEG with Epileptiform Activity Signals 

subplot(433); 

plot(t, drowsyEEGWithEpileptiformSignal); 

title('Drowsy EEG with Epileptiform Activity'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(436); 

plot(t, amplifiedDrowsyWithEpileptiformSignal); 

title('Amplified Drowsy with Epileptiform Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(439); 

plot(t, filteredAmplifiedDrowsyWithEpileptiformEEG); 

title('Filtered Amplified Drowsy with Epileptiform Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

subplot(4312); 

plot(t, filteredAmplifiedDrowsyWithEpileptiformEEG_zeroPhase); 

title('Zero-Phase Filtered Drowsy with Epileptiform Signal'); 

xlabel('Time (s)'); 

ylabel('Amplitude'); 

ylim(yAxisRange); 

 

sgtitle('EEG Signals Processing: Awake vs. Normal Drowsy vs. Drowsy with Epileptiform Activity'); 

``` 

 

### Results 

**Top Row: Original EEG Signals** 

 

- **Awake EEG Signal**: Shows the combination of alpha and beta waves. 

- **Normal Drowsy EEG Signal**: Lower amplitude alpha and beta waves indicating a drowsy state. 

- **Drowsy EEG with Epileptiform Activity**: Shows a clear spike at the 3-second mark indicating epileptiform activity. 

 

**Second Row: Amplified EEG Signals** 

 

- **Amplified Awake Signal**: The awake signal is amplified, making the wave patterns more distinct. 

- **Amplified Drowsy Signal**: The drowsy signal is similarly amplified. 

- **Amplified Drowsy with Epileptiform Signal**: Amplified version of the drowsy signal with more pronounced epileptiform spikes. 

 

**Third Row: Filtered Amplified EEG Signals** 

 

- **Filtered Amplified Awake Signal**: High-frequency noise is reduced, but the main characteristics of the awake signal are preserved. 

- **Filtered Amplified Drowsy Signal**: Similar noise reduction is observed. 

- **Filtered Amplified Drowsy with Epileptiform Signal**: Noise reduction while maintaining the epileptiform activity. 

 

**Fourth Row: Zero-Phase Filtered Signals** 

 

- **Zero-Phase Filtered Awake Signal**: Provides a cleaner signal with preserved phase characteristics. 

- **Zero-Phase Filtered Drowsy Signal**: Shows a clear filtered version 

 

 of the drowsy state. 

- **Zero-Phase Filtered Drowsy with Epileptiform Signal**: Cleaned signal showing the epileptiform spikes clearly. 

 

### Conclusion 

The provided MATLAB code and figures demonstrate the steps involved in generating, amplifying, filtering, and visualizing EEG signals. Each stage highlights different aspects of signal processing, showing how noise can be mitigated and important signal characteristics preserved. This exercise is crucial for understanding how EEG data is processed and analyzed in practical applications. 

``` 

 

 
