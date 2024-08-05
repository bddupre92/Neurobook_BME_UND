# Chapter 11 Lab Example 2

## Overview
In this lab, we will be simulating hearing loss using MATLAB. The MATLAB script generates sine wave tones at various frequencies, simulates hearing loss using a low-pass filter, and visualizes the results using time-domain plots and frequency spectra. The script also plays the generated tones before and after simulating hearing loss to provide an auditory comparison.

## Requirements
- MATLAB
- Working speakers
- Audio Toolbox MATLAB
- Signal Processing Toolbox

## Steps
First, you want to navigate to the GitHub page for this textbook. Here is the link:
[Neurobook_BME_UND](https://github.com/bddupre92/Neurobook_BME_UND)

After you are in the GitHub, navigate to Chapter 11 Lab Example 2, and you will find a MATLAB file named `chapter_example.m`. You will want to open that file in MATLAB and open it as a new script. Look at the code given. Can you recognize any functions you already know of? Do you see some that you don’t know? Here is a list of the main functions used in this MATLAB script.

### Main Functions Used

#### `sin`
- **Description**: Generates a sine wave.
- **Usage**: `signal = 0.5 * sin(2 * pi * f * t);`
- **Purpose**: To create the sine wave tones at specified frequencies.

#### `butter`
- **Description**: Designs a Butterworth filter.
- **Usage**: `[b, a] = butter(6, cutoff_freq/(fs/2));`
- **Purpose**: To design a low-pass filter to simulate hearing loss.

#### `filter`
- **Description**: Applies a digital filter to a signal.
- **Usage**: `signalHearingLoss = filter(b, a, signal);`
- **Purpose**: To apply the low-pass filter to the generated sine waves.

#### `sound`
- **Description**: Plays a sound.
- **Usage**: `sound(signal, fs);`
- **Purpose**: To play the generated sine wave tones.

#### `pause`
- **Description**: Pauses execution for a specified number of seconds.
- **Usage**: `pause(duration + 0.5);`
- **Purpose**: To allow the sound to finish playing before proceeding.

#### `length`
- **Description**: Returns the length of a vector.
- **Usage**: `length(combinedSignal);`
- **Purpose**: To verify the lengths of the combined signals.

#### `plot`
- **Description**: Creates a 2D line plot.
- **Usage**: `plot((0:length(combinedSignal)-1)/fs, combinedSignal);`
- **Purpose**: To plot the time-domain waveforms of the signals.

#### `fft`
- **Description**: Computes the Fast Fourier Transform (FFT).
- **Usage**: `fftCombinedSignal = fft(combinedSignal);`
- **Purpose**: To compute the frequency spectrum of the signals.

#### `abs`
- **Description**: Returns the absolute value.
- **Usage**: `amplitude = abs(fftCombinedSignal)/N;`
- **Purpose**: To compute the magnitude of the FFT.

#### `xlim`
- **Description**: Sets the x-axis limits for the current axes.
- **Usage**: `xlim([0, max(frequencies)*1.2]);`
- **Purpose**: To limit the x-axis to the relevant frequency range.

#### `xlabel`, `ylabel`, `title`
- **Description**: Labels the x-axis, y-axis, and sets the title of the plot.
- **Usage**: `xlabel('Time (s)');`, `ylabel('Amplitude');`, `title('Time-Domain Waveform of Combined Signal (Normal Hearing)');`
- **Purpose**: To add labels and titles to the plots.

#### `subplot`
- **Description**: Creates axes in tiled positions.
- **Usage**: `subplot(2, 1, 1);`
- **Purpose**: To create multiple plots in a single figure.

#### `disp`
- **Description**: Displays text or variables.
- **Usage**: `disp('Length of combinedSignal:');`
- **Purpose**: To display messages and values in the command window.

This script has four main steps that generate sounds at different frequencies, and then a low-pass filter is used to model how hearing loss affects our ability to hear those sounds. The script then plots time-domain signals and a composite frequency spectrum and combines them with the hearing loss signals so we can compare. Finally, you will hear what the sounds would sound like for someone who is experiencing hearing loss. Here’s how the script does this.

## Step 1: Generate Sounds at Different Frequencies

**Description**: This step generates sine wave tones at specified frequencies and applies a low-pass filter to simulate hearing loss. The original and filtered signals are combined and played.

**Functions Used**:
1. `sin`: Generates the sine wave tones.
   - `signal = 0.5 * sin(2 * pi * f * t);`
2. `butter`: Designs a Butterworth low-pass filter.
   - `[b, a] = butter(6, cutoff_freq/(fs/2));`
3. `filter`: Applies the low-pass filter to the generated sine waves.
   - `signalHearingLoss = filter(b, a, signal);`
4. `sound`: Plays the generated sine wave tones.
   - `sound(signal, fs);`
5. `pause`: Pauses execution to allow the sound to finish playing.
   - `pause(duration + 0.5);`

## Step 2: Plot Time-Domain Signals

**Description**: This step plots the time-domain waveforms of the combined signals for both normal hearing and simulated hearing loss.

**Functions Used**:
1. `plot`: Creates a 2D line plot of the time-domain signals.
   - `plot((0:length(combinedSignal)-1)/fs, combinedSignal);`
2. `xlabel`, `ylabel`, `title`: Labels the x-axis, y-axis, and sets the title of the plot.
   - `xlabel('Time (s)');`, `ylabel('Amplitude');`, `title('Time-Domain Waveform of Combined Signal (Normal Hearing)');`
3. `subplot`: Creates axes in tiled positions for multiple plots in a single figure.
   - `subplot(2, 1, 1);`

## Step 3: Composite Frequency Spectrum

**Description**: This step computes the Fast Fourier Transform (FFT) of the combined signals and plots the frequency spectra for both normal hearing and simulated hearing loss.

**Functions Used**:
1. `fft`: Computes the Fast Fourier Transform of the signals.
   - `fftCombinedSignal = fft(combinedSignal);`
2. `abs`: Computes the magnitude of the FFT.
   - `amplitude = abs(fftCombinedSignal)/N;`
3. `plot`: Creates a 2D line plot of the frequency spectra.
   - `plot(f, amplitude);`
4. `xlabel`, `ylabel`, `title`: Labels the x-axis, y-axis, and sets the title of the plot.
   - `xlabel('Frequency (Hz)');`, `ylabel('Amplitude');`, `title('Composite Frequency Spectrum of Combined Signal (Normal Hearing)');`
5. `xlim`: Sets the x-axis limits for the current axes.
   - `xlim([0, max(frequencies)*1.2]);`
6. `subplot`: Creates axes in tiled positions for multiple plots in a single figure.
   - `subplot(2, 1, 1);`

## Step 4: Play Tones Again at New Amplitudes to Simulate Hearing Loss

**Description**: This step plays the combined signal with simulated hearing loss to provide an auditory comparison of how the tones would sound after applying the hearing loss filter.

**Functions Used**:
1. `sound`: Plays the combined signal with hearing loss.
   - `sound(combinedSignalHearingLoss, fs);`
2. `pause`: Pauses execution to allow the sound to finish playing.
   - `pause(length(combinedSignalHearingLoss)/fs + 1);`

Then you will want to save the script and then click Run. Ensure you have your speakers on your device and the volume is up. You will hear the sounds two times before the script is finished running. You should notice that as the frequencies get higher, they get lower.

## Explanation of Figures

### Figure 1: Time-Domain Signals

![image](https://github.com/user-attachments/assets/c5c82f17-430e-432b-a3aa-5cac7df137f0)


The figure displays the time-domain waveforms of two combined audio signals: one representing normal hearing and the other simulating sensorineural hearing loss. The top plot shows the waveform for normal hearing, where the amplitude remains consistent across the entire duration of approximately 10 seconds. This indicates that the generated sine wave tones, which are concatenated, maintain their integrity without any attenuation. In contrast, the bottom plot illustrates the waveform for the signal with simulated hearing loss. Here, the amplitude diminishes significantly over time, particularly after the initial few seconds. The result is a noticeable decrease in the signal's amplitude, especially for the higher frequencies, which manifests as a progressively weaker waveform. This visual representation effectively highlights the impact of sensorineural hearing loss on audio signals, demonstrating how higher frequencies are diminished, leading to a loss of clarity and intensity in the sound.

### Figure 2: Composite Frequency Spectrum

![image](https://github.com/user-attachments/assets/b2980a45-7d07-46d2-b11e-64e70ad039a7)

The figure illustrates the composite frequency spectra of two combined audio signals: one for normal hearing and the other simulating sensorineural hearing loss. In the top plot, representing normal hearing, there are distinct and relatively uniform peaks at the frequencies where the original sine wave tones were generated—specifically at 100 Hz, 200 Hz, 300 Hz, 400 Hz, 500 Hz, 600 Hz, 700 Hz, 800 Hz, 900 Hz, and 1000 Hz. This indicates that each tone is preserved with its original intensity, reflecting an ideal, undistorted signal where all frequency components are present as expected. In contrast, the bottom plot, representing the signal with simulated hearing loss, shows that the peaks at lower frequencies (100 Hz, 200 Hz, 300 Hz, 400 Hz, and 500 Hz) remain prominent. However, the peaks at higher frequencies (above 500 Hz) are significantly attenuated or almost nonexistent. This attenuation is due to applying a low-pass filter, which mimics the effect of sensorineural hearing loss by reducing the sensitivity to higher frequencies. The comparison between the two plots demonstrates the impact of sensorineural hearing loss on the frequency content of the audio signal, effectively visualizing the loss of higher-frequency components.

This is the conclusion to this lab example.
