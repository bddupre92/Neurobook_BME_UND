# Lab Example: Saccades Simulation and Detection

## Overview

This lab focuses on simulating and detecting saccadic eye movements using MATLAB.

Saccades are rapid, ballistic movements of the eyes that shift the point of fixation from one location to another. These movements are the fastest produced by the human body, with peak velocities ranging from 30 to 500 degrees per second and durations typically between 20 to 200 milliseconds, depending on the amplitude. Saccades can be both voluntary, such as when we decide to look at a specific object, and involuntary, occurring reflexively in response to stimuli. Despite their speed, saccades are highly precise, allowing the eyes to land accurately on the intended target. The latency, or the time from the appearance of a stimulus to the initiation of the saccade, is usually around 200 milliseconds.

![image](https://github.com/user-attachments/assets/b715a5c7-1b5a-48ca-b6a3-0a8b431cbc2b)


In the context of eye tracking, saccades are crucial because they help identify periods of fixation when the eyes are relatively still. By analyzing these fixations, researchers and designers can gain insights into what captures and holds a person's attention. The frequency, amplitude, and duration of saccades are also indicators of cognitive load and attentional processes; for instance, increased saccadic activity might suggest higher cognitive processing or searching behavior. In usability studies, understanding gaze patterns and how users shift their gaze can inform improvements in interface design and overall user experience.

In the field of psychophysics, which explores the relationship between physical stimuli and the resulting sensations and perceptions, saccades are integral to understanding visual perception. During saccades, vision is temporarily suppressed—a phenomenon known as saccadic suppression—enabling researchers to study how visual information is integrated across different fixations. Saccadic patterns also provide insights into attention and awareness, revealing how attention is shifted and maintained during various tasks. Additionally, the latency and dynamics of saccades are used in reaction time studies to investigate the timing and coordination of perceptual and motor processes.

Applications of saccadic research span various fields, including neuroscience, marketing, virtual reality, and gaming. In neuroscience, abnormal saccadic movements can indicate neurological conditions such as Parkinson's disease, schizophrenia, and ADHD. In marketing, eye tracking and analysis of saccadic movements help understand consumer behavior, such as how people view advertisements or product placements. In virtual reality and gaming, eye tracking enhances user experiences by allowing systems to respond to where users are looking in real-time. Overall, understanding and analyzing saccades provide valuable insights into attention, perception, cognitive processes, and neurological health, making them a critical component of research and technological applications.

A valuable resource for understanding the background of saccades is available at: [SR Research Blog on Eye Tracking Terminology](https://www.sr-research.com/what-are-saccades/).

In this lab, we will create MATLAB code capable of generating simulated saccades.

## Objectives

- Simulate a series of saccades using MATLAB.
- Detect saccades from simulated data based on eye movement velocity.

## Getting Started

### MATLAB Setup

1. **Clear the Workspace:**
   Begin by clearing your MATLAB workspace and any figures:
   ```matlab
   clear all;
   clf('reset');
   ```

### Simulating Saccades

To simulate a saccade in MATLAB, we need to create a function that models the rapid, ballistic movement of an eye as it shifts focus from one point to another. Saccades are typically characterized by their quick acceleration and deceleration phases, and the dynamics can be approximated using a second-order system.

To simulate a series of saccades, we can modify the previous script to include multiple saccades with varying amplitudes and intervals. Here's an updated version of the script to achieve this:

```matlab
% Simulate a series of saccades in MATLAB

% Parameters
amplitudes = [10, -15, 20, -25, 30]; % amplitudes of the saccades in degrees
durations = [0.05, 0.05, 0.05, 0.05, 0.05]; % durations of the saccades in seconds
intervals = [0.1, 0.15, 0.2, 0.1]; % intervals between saccades in seconds
sampling_rate = 1000; % samples per second

% Total time calculation
total_time = sum(durations) + sum(intervals);
t_total = 0:1/sampling_rate:total_time;

% Time vector and position initialization
eye_position = zeros(size(t_total));
current_time = 0;

% Second-order system parameters (assuming same for all saccades)
zeta = 0.8; % damping ratio

% Loop through each saccade
for i = 1:length(amplitudes)
    % Current saccade parameters
    amplitude = amplitudes(i);
    duration = durations(i);
    omega = 2 * pi / duration; % natural frequency (rad/s)
    
    % Time vector for the current saccade
    t_saccade = 0:1/sampling_rate:duration;
    
    % System transfer function: G(s) = omega^2 / (s^2 + 2*zeta*omega*s + omega^2)
    num = [omega^2];
    den = [1, 2*zeta*omega, omega^2];
    sys = tf(num, den);
    
    % Step response of the system to simulate the saccade
    [y, t_saccade] = step(sys, t_saccade);
    y = y * amplitude; % Scale the response to the desired amplitude
    
    % Update the eye position
    start_idx = find(t_total >= current_time, 1);
    end_idx = start_idx + length(y) - 1;
    eye_position(start_idx:end_idx) = eye_position(start_idx:end_idx) + y';
    
    % Update current time
    current_time = current_time + duration;
    
    % Add interval between saccades if not the last saccade
    if i < length(amplitudes)
        interval = intervals(i);
        current_time = current_time + interval;
    end
end

% Plot the series of saccades
figure;
plot(t_total, eye_position, 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Eye Position (degrees)');
title('Series of Saccades Simulation');
grid on;

% Optional: Save the plot as an image
saveas(gcf, 'series_of_saccades_simulation.png');

% Display the plot
disp('Series of saccades simulation completed.');
```

![image](https://github.com/user-attachments/assets/0fa0046d-5ed7-4e7b-8bf2-3e0ff94541c7)


The script simulates a series of saccades with parameters that define the amplitudes (in degrees), durations (in seconds), and intervals between successive saccades (also in seconds). The simulation operates at a specified sampling rate (samples per second). To compute the total simulation time, the script sums the durations of all saccades and the intervals between them. It initializes a time vector and an eye position array to represent the total simulation period.

Within a loop, the script processes each saccade by defining its natural frequency (omega) and damping ratio (zeta). It computes the step response of a second-order system for each saccade, updates the eye position array with the new saccade data, and adjusts the current time to account for the duration of the saccade and the interval to the next one. Finally, the script plots the eye position over time, visualizing the series of saccades. This allows for adjustment of parameters to match the specific characteristics of the saccades being simulated.

### Detecting Saccades

Now that we can generate saccades, it would be interesting to detect them as well.

To detect saccades in the generated eye position data, we can use a velocity-based method. This involves computing the velocity of the eye position and identifying points where the velocity exceeds a certain threshold, which indicates the occurrence of a saccade.

```matlab
% Saccade detection based on generated data from the previous script

% Parameters for saccade detection
velocity_threshold = 500; % degrees per second

% Compute the velocity of the eye position
eye_velocity = diff(eye_position) * sampling_rate; % velocity in degrees per second
eye_velocity = [0, eye_velocity]; % pad the first element to match the length of eye_position

% Detect saccades based on the velocity threshold
saccade_indices = find(abs(eye_velocity) > velocity_threshold);

% Combine contiguous indices into saccades
saccade_starts = saccade_indices([1, find(diff(saccade_indices) > 1) + 1]);
saccade_ends = saccade_indices([find(diff(saccade_indices) > 1), end]);

% Plot the detected saccades
figure;
plot(t_total, eye_position, 'LineWidth', 2);
hold on;
for i = 1:length(saccade_starts)
    saccade_time = t_total(saccade_starts(i):saccade_ends(i));
    saccade_pos = eye_position(saccade_starts(i):saccade_ends(i));
    plot(saccade_time, saccade_pos, 'r', 'LineWidth', 2);
end
xlabel('Time (s)');
ylabel('Eye Position (degrees)');
title('Detected Saccades');
legend('Eye Position', 'Detected Saccades');
grid on;

% Optional: Save the plot as an image
saveas(gcf, 'detected_saccades.png');

% Display the results
disp('Saccade detection completed.');
disp('Detected saccades:');
for i =

 1:length(saccade_starts)
    fprintf('Saccade %d: Start Time = %.3f s, End Time = %.3f s, Amplitude = %.2f degrees\n', ...
            i, t_total(saccade_starts(i)), t_total(saccade_ends(i)), ...
            eye_position(saccade_ends(i)) - eye_position(saccade_starts(i)));
end
```

![image](https://github.com/user-attachments/assets/b93c9fb5-3214-41e6-bd31-1a9ab482212b)


The script begins by calculating the velocity of the eye position using the `diff` function and scales it by the sampling rate to obtain the velocity in degrees per second. The `eye_velocity` array is then padded with a zero at the start to match the length of the `eye_position` array.

For saccade detection, the script identifies indices where the absolute value of the velocity exceeds the `velocity_threshold`. Contiguous indices are grouped into individual saccades by detecting where the difference between successive indices is greater than one.

The eye position is then plotted with the detected saccades highlighted in red, and the start and end times of each detected saccade are displayed in the console.

Finally, the script prints the start time, end time, and amplitude of each detected saccade. This script should be run after the previous script that generates the saccade data. Adjust the `velocity_threshold` as needed to better match the characteristics of the saccades in your data.
