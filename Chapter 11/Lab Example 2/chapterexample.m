% Step 1: Generate Sounds at Different Frequencies

% Define parameters
fs = 44100;  % Sampling frequency
duration = 1;  % Duration of each tone in seconds
frequencies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000];  % Array of frequencies

% Initialize an empty array to hold the combined signal
combinedSignal = [];
combinedSignalHearingLoss = [];

% Generate and play sounds at different frequencies
for f = frequencies
    t = 0:1/fs:duration;  % Time vector
    signal = 0.5 * sin(2 * pi * f * t);  % Generate sine wave
    combinedSignal = [combinedSignal, signal];  % Append to combined signal
    
    % Apply a low-pass filter to mimic hearing loss
    cutoff_freq = 500;  % Cutoff frequency for the low-pass filter
    [b, a] = butter(6, cutoff_freq/(fs/2));  % 6th order Butterworth filter
    signalHearingLoss = filter(b, a, signal);
    combinedSignalHearingLoss = [combinedSignalHearingLoss, signalHearingLoss];  % Append to combined signal with hearing loss
    
    % Play the original sound
    sound(signal, fs);
    pause(duration + 0.5);  % Pause to allow the sound to finish playing
end

% Verify the combined signals
disp('Length of combinedSignal:');
disp(length(combinedSignal));
disp('Length of combinedSignalHearingLoss:');
disp(length(combinedSignalHearingLoss));

% Step 2: Plot Time-Domain Signals

figure;
subplot(2, 1, 1);
plot((0:length(combinedSignal)-1)/fs, combinedSignal);
title('Time-Domain Waveform of Combined Signal (Normal Hearing)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(2, 1, 2);
plot((0:length(combinedSignalHearingLoss)-1)/fs, combinedSignalHearingLoss);
title('Time-Domain Waveform of Combined Signal (Hearing Loss)');
xlabel('Time (s)');
ylabel('Amplitude');


% Step 3: Composite Frequency Spectrum

% FFT of the combined signal
N = length(combinedSignal);
fftCombinedSignal = fft(combinedSignal);
f = (0:N-1)*(fs/N);
amplitude = abs(fftCombinedSignal)/N;

% FFT of the combined signal with hearing loss
fftCombinedSignalHearingLoss = fft(combinedSignalHearingLoss);
amplitudeHearingLoss = abs(fftCombinedSignalHearingLoss)/N;

figure;
subplot(2, 1, 1);
plot(f, amplitude);
xlim([0, max(frequencies)*1.2]);  % Limit x-axis to relevant frequency range
title('Composite Frequency Spectrum of Combined Signal (Normal Hearing)');
xlabel('Frequency (Hz)');
ylabel('Amplitude');

subplot(2, 1, 2);
plot(f, amplitudeHearingLoss);
xlim([0, max(frequencies)*1.2]);  % Limit x-axis to relevant frequency range
title('Composite Frequency Spectrum of Combined Signal (Hearing Loss)');
xlabel('Frequency (Hz)');
ylabel('Amplitude');

% Step 4: Play Tones Again at New Amplitudes to Simulate Hearing Loss

disp('Playing combined signal with hearing loss...');
sound(combinedSignalHearingLoss, fs);
pause(length(combinedSignalHearingLoss)/fs + 1);  % Pause to allow the sound to finish playing
