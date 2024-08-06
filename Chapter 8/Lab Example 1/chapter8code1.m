% Generate a unit sphere and prepare the figure 
[x, y, z] = sphere(); 
hf = figure('Color', 'w'); 
axis equal, grid off, axis off, hold on 

% Define the main globe coordinates and generate the surface 
rMain = 5; 
xm = x * rMain; 
ym = y * rMain; 
zm = z * rMain; 
mainGlobe = surf(xm, ym, zm, 'EdgeColor', 'none', 'FaceAlpha', 0.5); 

% Define the iris sphere and generate the surface 
rIris = 2.5; 
cutoff = ceil(size(x, 1) / 2);  % Calculate to get a half sphere (better result for later texture mapping) 
xi = x(:, cutoff:end) * rIris; 
yi = y(:, cutoff:end) * rIris / 3 + (rMain - rIris) * 1.7; 
zi = z(:, cutoff:end) * rIris; 
irisGlobe = surf(xi, yi, zi, 'EdgeColor', 'none'); 

% Define the paths to the images  
irisImagePath = 'iris image path’;    % Path to the iris texture image 
globeImagePath = 'sclera image path';  % Path to the globe texture image 
retinaImagePath= 'retina image path'; 

%Read the images 
imgIris = imread(irisImagePath); 
imgGlobe = imread(globeImagePath); 
imgRetina = imread(retinaImagePath); 

% (Optional) Mirror the globe image to repeat the pattern (and increase definition) 
CDglobe = [imgGlobe, flip(imgGlobe, 2)]; 

% Mirror the retinas 
CDretina = [imgRetina, flip(imgRetina, 3)]; 
% Apply mapping 
set(mainGlobe, 'FaceColor', 'Texturemap', 'CData', CDglobe, 'FaceAlpha', 0.5); 
set(irisGlobe, 'FaceColor', 'Texturemap', 'CData', imgIris, 'EdgeColor', 'none'); 
% Texture mapping  
rotate(mainGlobe, [1 0 0], -90); 

% Adjust the view to see the front of the eye and some of the back 
view([-1, -1, 0.5]);  % Adjust these values to change the viewing angle 

% Make the image 3D so you can move it around and look at different angles 
camorbit(0,0,'camera'); % Orbit the camera around the scene 
% To enable interactive manipulation of the view, you can use rotate3d 
rotate3d on; 
% Add retina texture to the back of the eye 
rRetina = 4; % Define the radius of the retina 
xr = x * rRetina; 
yr = y * rRetina; 
zr = z * rRetina; 
retina = surf(xr, yr, -zr, 'FaceColor', 'Texturemap', 'CData', imgRetina, 'EdgeColor', 'none'); 