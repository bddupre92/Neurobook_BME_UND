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
for i = 1:length(saccade_starts)
    fprintf('Saccade %d: Start Time = %.3f s, End Time = %.3f s, Amplitude = %.2f degrees\n', ...
            i, t_total(saccade_starts(i)), t_total(saccade_ends(i)), ...
            eye_position(saccade_ends(i)) - eye_position(saccade_starts(i)));
end
