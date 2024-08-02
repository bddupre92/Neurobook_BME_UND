% Define constants
mu0 = 4 * pi * 1e-7; % Permeability of free space
num_points = 50; % Number of points in each dimension to calculate the field
 
 
% Define coil parameters
coil_radius = [0.05, 0.05]; % Radii of the coils in meters
coil_center = [0, 0, 0.1; 0, 0, -0.1]; % Centers of the coils in x, y, z
frequencies = [10, 15]; % Frequencies of the coils in Hz
currents = [1, 1]; % Currents in the coils in Amperes
phases = [0, pi/2]; % Phases of the currents in the coils
 
 
% Define the observation grid for the brain model
[x, y, z] = meshgrid(linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points));
 
 
% Simulate baseline neural activity with altered oscillatory patterns for depression
t = 0:0.001:1; % Time vector (1 second)
f_beta = 20; % Frequency of beta oscillations 
p0_beta = [1, 0, 0]; % Initial dipole moment for theta (arbitrary units)
 
 
% Calculate baseline MEG signal with altered oscillatory patterns
meg_baseline_beta = mu0 * (3 * (p0_beta(1) * z) .* z - p0_beta(1)) ./ (4 * pi * (x.^2 + y.^2 + z.^2).^(5/2));
meg_baseline = meg_baseline_beta; % Combine beta components
 
 
% Apply magnetic stimulation (using original coil model)
Bz_total = zeros(size(z)); % Initialize total magnetic field
for coil = 1:length(frequencies)
    Bz = mu0 * currents(coil) * coil_radius(coil)^2 ./ (2 * ((coil_radius(coil)^2 + (z - coil_center(coil,3)).^2).^(3/2)));
    Bz_total = Bz_total + Bz; % Superimpose the fields from each coil
end
 
 
% Simulate post-stimulation neural activity (simplified model)
% Assume the stimulation affects the amplitude of the neural oscillations
meg_post_beta = mu0 * (3 * (1.2 * p0_beta(1) * z) .* z - 1.2 * p0_beta(1)) ./ (4 * pi * (x.^2 + y.^2 + z.^2).^(5/2));
meg_post = meg_post_beta; % Combine alpha and theta components
 
 % Initialize time-varying MEG matrices
meg_baseline_time = zeros(length(t), num_points);
meg_post_time = zeros(length(t), num_points);
 
% Loop over time to simulate MEG for each time point
for i = 1:length(t)
    % Simulate MEG signal at time point i
    meg_baseline_time(i, :) = sin(2 * pi * f_beta * t(i)) * meg_baseline(num_points/2, num_points/2, num_points/2);
    meg_post_time(i, :) = sin(2 * pi * f_beta * t(i)) * meg_post(num_points/2, num_points/2, num_points/2);
end
 
% Choose a plane to visualize, for example z=0 (middle of the brain)
slice_index = num_points / 2; % Assuming num_points is even, this is the middle
meg_baseline_slice = squeeze(meg_baseline(:, :, slice_index));
meg_post_slice = squeeze(meg_post(:, :, slice_index));
 
 
cmin = min(min(meg_baseline_slice(:)), min(meg_post_slice(:)));
cmax = max(max(meg_baseline_slice(:)), max(meg_post_slice(:)));
 
% Plot the baseline magnetic field slice with adjusted color limits
subplot(2, 2, 1);
imagesc(linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points), meg_baseline_slice);
axis square;
title('Baseline Magnetic Field (z=0)');
xlabel('x (m)');
ylabel('y (m)');
colorbar;
clim([cmin cmax]); % Adjust the color scale
 
 
% Plot the post-stimulation magnetic field slice with the same color limits for comparison
subplot(2, 2, 2);
imagesc(linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points), meg_post_slice);
axis square;
title('Post-Stimulation Magnetic Field (z=0)');
xlabel('x (m)');
ylabel('y (m)');
colorbar;
clim([cmin cmax]); % Use the same color scale as the baseline for direct comparison
 
 
% Now plot the central slice of the brain over time
subplot(2, 2, [3, 4]);
plot(t, meg_baseline_time(:, slice_index), 'DisplayName', 'Baseline'); % Plot the central slice over time
hold on; % Hold on to plot both on the same graph
plot(t, meg_post_time(:, slice_index), 'DisplayName', 'Post-Stimulation'); % Plot the central slice over time
hold off;
legend;
title('MEG Signal Over Time');
xlabel('Time (s)');
ylabel('Magnetic Field (T)');