## Chapter 8: Lab Example 1

## Overview

In this lab we will generate an interactive eye anatomy image us-ing MATLAB in this lab. You should already have MATLAB in-stalled, however if you don’t, there are instructions on how download it in Chapter 1: Lab Example 1.
## Requirements
•	MATLAB
•	Texture images of the iris, sclera and retina

## Steps
First, go onto the internet and find three images. One of the iris, one of the retina, and one of the sclera. Make sure that these im-ages are saved a .jpg files. For this lab to work correctly, you must know each anatomical component and save the right pic-tures. If you need a refresher on these anatomical components, refer to section 9.2 of this chapter. 

After you have MATLAB open start a new script and go to the GitHub repository at this link:

https://github.com/bddupre92/Neurobook_BME_UND

Navigate Chapter 8: Example 1 code 1 and copy and paste the code into your MATLAB. 

## Script Structure

Generate Unit Sphere
Create a unit sphere to serve as the base for the eye mod-el.

Prepare Figure
Configure the figure properties such as color, axis, and grid.

Main Globe (Sclera)
Define the radius and generate the surface for the main globe representing the sclera.

Iris Sphere
Define the radius and generate the surface for the iris.
Adjust coordinates to properly position the iris on the globe.

Read Images
Load the texture images for the iris, sclera, and retina.
Texture Mapping
Apply the texture images to the corresponding surfaces.
Optionally mirror the images to enhance the definition.

Rotate and View Adjustment
Rotate the main globe for correct orientation.
Adjust the view to display the front of the eye and part of the back.

Interactive Features
Enable interactive manipulation of the view with rotate3d.

Retina Texture
Add a textured surface to represent the retina at the back of the eye.

## Key Functions Used

sphere
Usage: [x, y, z] = sphere();
Purpose: Generates the coordinates for a unit sphere.

surf
Usage: mainGlobe = surf(xm, ym, zm, 'EdgeColor', 'none', 'FaceAlpha', 0.5);
Purpose: Creates a 3D surface plot.

imread
Usage: imgIris = imread(irisImagePath);
Purpose: Reads an image file into MATLAB.

set
Usage: set(mainGlobe, 'FaceColor', 'Texturemap', 'CData', CDglobe, 'FaceAlpha', 0.5);
Purpose: Sets properties for graphics objects.

rotate
Usage: rotate(mainGlobe, [1 0 0], -90);
Purpose: Rotates the graphics object.

view
Usage: view([-1, -1, 0.5]);
Purpose: Sets the viewpoint for the 3D plot.

camorbit
Usage: camorbit(0,0,'camera');
Purpose: Orbits the camera around the scene.

rotate3d
Usage: rotate3d on;
Purpose: Enables interactive 3D rotation of the plot.

## Note
See lines 22, 23, and 24 under 
% Define the paths to the images. 

You will need to make a path to your photos from your computer and paste them here. To create a path to an image, right-click it and select “Copy as Path.” You will then paste that into the MATLAB code. Make sure you have ‘’ around the file path name. You must make sure you’re your images are save in your MATLAB drive and that is where you are creating the path to. If you do not have a MATLAB drive, follow this link to set it up. 

https://www.mathworks.com/products/matlab-drive.html 

Once you have entered your file paths, click run. You should see a figure window pop up with your eyeball inside!

![image](https://github.com/user-attachments/assets/58f53302-c1e3-41bd-b727-7d796639a6c1)

Now we will take this further and look with a different set of eyes. 

Open a new script on MATLAB and got back to the GitHub. Navigate to Chapter 8: Lab Example 1 code 2 and copy and paste the code into a new script.
Description of Differences in Structures and Key Functions

This updated MATLAB script builds upon the previous one by generating and visualizing two 3D eyeballs with different iris tex-tures. Here are the key differences and additions:

## Key Additions and Changes

Multiple Image Paths
The script now includes an additional path for a second iris tex-ture image:
irisImagePath2 = 'iris image 2 path'; % Path to the iris texture image for the second eyeball 

File Existence Checks
The script checks if all specified image files exist, including the second iris image:

if ~isfile(irisImagePath) 
    error('Iris image file not found: %s', irisImagePath); 
end 
Reading Images
The script reads the second iris image in addition to the other im-ages:

try 
    imgIris = imread(irisImagePath); 
catch ME 
    error('Error reading iris image: %s', ME.message); 
end 
Generating Two Eyeballs
Coordinates and surfaces for the second eyeball are generated with a horizontal shift to separate them visually:

% Define the coordinates for the second eyeball 
x_shift = 12; % Adjust as needed 
xm2 = xm + x_shift; 
xi2 = xi + x_shift; 

Surface Generation and Texture Mapping for the Second Eye-ball:
The script creates the main globe, iris, and retina surfaces for the second eyeball:

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

## Summary of Key Functions

isfile
Usage: if ~isfile(irisImagePath2)
Purpose: Checks if a file exists at the specified path. Used to ensure all image files are available before pro-ceeding.

imread
Usage: imgIris2 = imread(irisImagePath2);
Purpose: Reads an image file into MATLAB. Extended to include reading the second iris image.

surf
Usage: mainGlobe2 = surf(xm2, ym, zm, 'EdgeColor', 'none', 'FaceAlpha', 0.5);
Purpose: Creates a 3D surface plot. Used to generate the main globe, iris, and retina surfaces for both eyeballs.

set
Usage: set(mainGlobe2, 'FaceColor', 'Texturemap', 'CData', CDglobe, 'FaceAlpha', 0.5);
Purpose: Sets properties for graphics objects. Used to ap-ply textures to the surfaces of both eyeballs.

rotate
Usage: rotate(mainGlobe2, [1 0 0], -90);
Purpose: Rotates the graphics object. Used to correctly orient both eyeballs.

Use the following images for irisImagePath and irisImpagePath2. 

![image](https://github.com/user-attachments/assets/c5675ab6-bd7a-4b81-b6c8-6386277dde09)


Save them to your MATLAB drive, make an image path, and copy and paste them into the code. Do not forget to copy and paste your image paths for the sclera and the retina. 

Now run your code. You should have a figure box pop up with two eyes in it. If you receive a error code that states ‘XX image file not found’ you have not created the image path correctly and saved it into your MATLAB drive. 
Can you tell me what is off with these two eyes? The right pupil is much smaller than the right eye pupil. Do you know what this is called? You may know about this disorder if you have taken a neuroanatomy class before. Hint: we did not discuss it in this chapter. This is called Horner's syndrome. Horner’s syndrome is a rare neurological syndrome that results from underlying nerve damage from a stroke, tumor, or spinal cord injury. Symptoms of this syndrome include smaller pupils (miosis), drooping eyelids (ptosis), and little to no sweating on the affected side of the face (anhidrosis). To treat this syndrome, some individuals will need the removal of a tumor or appropriate medical treatments. 

