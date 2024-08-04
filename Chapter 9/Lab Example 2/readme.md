# Chapter 9: Lab Example 2

Saccades are rapid, ballistic movements of the eyes that shift the point of fixation from one location to another. These movements are the fastest produced by the human body, with peak velocities ranging from 30 to 500 degrees per second and durations typically between 20 to 200 milliseconds, depending on the amplitude. Saccades can be both voluntary, such as when we decide to look at a specific object, and involuntary, occurring reflexively in response to stimuli. Despite their speed, saccades are highly precise, allowing the eyes to land accurately on the intended target. The latency, or the time from the appearance of a stimulus to the initiation of the saccade, is usually around 200 milliseconds.

![image](https://github.com/user-attachments/assets/3590680f-0b97-4e51-b34e-902151ee1e00)


In the context of eye tracking, saccades are crucial because they help identify periods of fixation when the eyes are relatively still. By analyzing these fixations, researchers and designers can gain insights into what captures and holds a person's attention. The frequency, amplitude, and duration of saccades are also indicators of cognitive load and attentional processes; for instance, increased saccadic activity might suggest higher cognitive processing or searching behavior. In usability studies, understanding gaze patterns and how users shift their gaze can inform improvements in interface design and overall user experience.

In the field of psychophysics, which explores the relationship between physical stimuli and the resulting sensations and perceptions, saccades are integral to understanding visual perception. During saccades, vision is temporarily suppressed—a phenomenon known as saccadic suppression—enabling researchers to study how visual information is integrated across different fixations. Saccadic patterns also provide insights into attention and awareness, revealing how attention is shifted and maintained during various tasks. Additionally, the latency and dynamics of saccades are used in reaction time studies to investigate the timing and coordination of perceptual and motor processes.

Applications of saccadic research span various fields, including neuroscience, marketing, virtual reality, and gaming. In neuroscience, abnormal saccadic movements can indicate neurological conditions such as Parkinson's disease, schizophrenia, and ADHD. In marketing, eye tracking and analysis of saccadic movements help understand consumer behavior, such as how people view advertisements or product placements. In virtual reality and gaming, eye tracking enhances user experiences by allowing systems to respond to where users are looking in real-time. Overall, understanding and analyzing saccades provide valuable insights into attention, perception, cognitive processes, and neurological health, making them a critical component of research and technological applications.

A valuable resource for understanding the background of saccades is available at: [SR Research Blog on Eye Tracking Terminology](https://www.sr-research.com/eye-tracking-blog/).

## Lab Exercise: Simulating Saccades in MATLAB

In this lab, we will create MATLAB code capable of generating simulated saccades.

### Simulating Saccades

To simulate a saccade in MATLAB, we need to create a function that models the rapid, ballistic movement of an eye as it shifts focus from one point to another. Saccades are typically characterized by their quick acceleration and deceleration phases, and the dynamics can be approximated using a second-order system.

To simulate a series of saccades, we can modify the previous script to include multiple saccades with varying amplitudes and intervals. Here's an updated version of the script to achieve this:

![image](https://github.com/user-attachments/assets/e32a0d23-6ca8-42b7-a912-9fab589dbf62)


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
