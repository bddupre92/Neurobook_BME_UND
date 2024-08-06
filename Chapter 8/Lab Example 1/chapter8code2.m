% Define the paths to the images in your MATLAB Drive 
irisImagePath = 'iris image 1 path';    % Path to the iris texture image for the first eyeball 
globeImagePath = 'sclera image path';  % Path to the globe texture image 
retinaImagePath = 'retina image path'; % Path to the retina texture image 
irisImagePath2 = 'iris image 2 path'; % Path to the iris texture image for the second eyeball 

% Check if the files exist 
if ~isfile(irisImagePath) 
    error('Iris image file not found: %s', irisImagePath); 
end 
if ~isfile(globeImagePath) 
    error('Globe image file not found: %s', globeImagePath);
end 
if ~isfile(retinaImagePath) 
    error('Retina image file not found: %s', retinaImagePath); 
end 
if ~isfile(irisImagePath2) 
    error('Second iris image file not found: %s', irisImagePath2); 
end 

% Read the images 
try 
    imgIris = imread(irisImagePath); 
catch ME 
    error('Error reading iris image: %s', ME.message); 
end 
try 
    imgGlobe = imread(globeImagePath); 
catch ME 
    error('Error reading globe image: %s', ME.message); 
end 
try 
    imgRetina = imread(retinaImagePath); 
catch ME 
    error('Error reading retina image: %s', ME.message); 
end 
try 

    imgIris2 = imread(irisImagePath2); 
catch ME 
    error('Error reading second iris image: %s', ME.message); 
end 

% Generate a unit sphere and prepare the figure 
[x, y, z] = sphere(); 
hf = figure('Color', 'w'); 
axis equal, grid off, axis off, hold on 

% Define the main globe coordinates and generate the surface for the first eyeball 
rMain = 5; 
xm = x * rMain; 
ym = y * rMain; 
zm = z * rMain; 
mainGlobe1 = surf(xm, ym, zm, 'EdgeColor', 'none', 'FaceAlpha', 0.5); 

% Define the iris sphere and generate the surface for the first eyeball 
rIris = 2.5; 
cutoff = ceil(size(x, 1) / 2);  % Calculate to get a half sphere (better result for later texture mapping) 
xi = x(:, cutoff:end) * rIris; 
yi = y(:, cutoff:end) * rIris / 3 + (rMain - rIris) * 1.7; 
zi = z(:, cutoff:end) * rIris; 
irisGlobe1 = surf(xi, yi, zi, 'EdgeColor', 'none'); 

% (Optional) Mirror the globe image to repeat the pattern (and increase definition) 
CDglobe = [imgGlobe, flip(imgGlobe, 2)]; 

% Mirror the retina image 
CDretina = [imgRetina, flip(imgRetina, 2)]; 

% Apply mapping for the first eyeball 
set(mainGlobe1, 'FaceColor', 'Texturemap', 'CData', CDglobe, 'FaceAlpha', 0.5); 
set(irisGlobe1, 'FaceColor', 'Texturemap', 'CData', imgIris, 'EdgeColor', 'none'); 

% Texture mapping for the first eyeball 
rotate(mainGlobe1, [1 0 0], -90); 

% Adjust the view to see the front of the eye and some of the back for the first eyeball 
view([-1, -1, 0.5]);  % Adjust these values to change the viewing angle 

% Make the image 3D so you can move it around and look at different angles 
camorbit(0, 0, 'camera'); % Orbit the camera around the scene 

% To enable interactive manipulation of the view, you can use rotate3d 
rotate3d on; 

% Add retina texture to the back of the first eye 
rRetina = 4; % Define the radius of the retina for the first eyeball 
xr = x * rRetina; 
yr = y * rRetina; 
zr = z * rRetina; 
retina1 = surf(xr, yr, -zr, 'FaceColor', 'Texturemap', 'CData', imgRetina, 'EdgeColor', 'none'); 

% Define the coordinates for the second eyeball 
x_shift = 12; % Adjust as needed 
xm2 = xm + x_shift; 
xi2 = xi + x_shift; 

% Generate the surface for the second eyeball 
mainGlobe2 = surf(xm2, ym, zm, 'EdgeColor', 'none', 'FaceAlpha', 0.5); 
irisGlobe2 = surf(xi2, yi, zi, 'EdgeColor', 'none'); 

% Apply mapping for the second eyeball with a different iris image 
set(mainGlobe2, 'FaceColor', 'Texturemap', 'CData', CDglobe, 'FaceAlpha', 0.5); 
set(irisGlobe2, 'FaceColor', 'Texturemap', 'CData', imgIris2, 'EdgeColor', 'none'); 

% Texture mapping for the second eyeball 
rotate(mainGlobe2, [1 0 0], -90); 

% Add retina texture to the back of the second eye 
retina2 = surf(xr + x_shift, yr, -zr, 'FaceColor', 'Texturemap', 'CData', imgRetina, 'EdgeColor', 'none'); 