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
