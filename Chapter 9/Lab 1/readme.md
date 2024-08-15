Here's the content converted into markdown format:

```markdown
# Chapter 9: Lab Example 1

## Overview

In this lab, we will try to run a very simplistic eye-tracking exercise using MATLAB. The code we will use implements the Hough transform algorithm previously touched on as well as an algorithm called Viola-Jones. This algorithm can be used in MATLAB to detect and classify faces, noses, eyes, mouths, and upper body. The base code is inspired and modified from this Github poster:  
[Eyeball Detection](https://github.com/ishitadatta/EyeballDetection).

## Objective

The goal of this laboratory exercise is to understand how to apply eye-tracking algorithms within MATLAB to perform a simplistic eye-tracking exercise using just a built-in webcam.

## MATLAB Setup

Let’s discuss a basic MATLAB code that can accomplish our laboratory exercise goals. Begin by clearing your workspace and any figures with:

```matlab
clear all   
clf('reset');
```

As we discussed in the objectives, we are going to use the built-in webcam from a LG Gram laptop. We can call the webcam using:

```matlab
cam=webcam();
```

Next, we are going to set up some simple identifiers that tell us when the subject is looking right, left, straight, or not found (noface).

```matlab
right = imread('RIGHT.jpg');
left = imread('LEFT.jpg');
noface = imread('no_face.jpg');
straight = imread('STRAIGHT.jpg');
```

In order to detect the face and eyes, we are going to use the Viola-Jones algorithm with:

```matlab
detector = vision.CascadeObjectDetector();
detector1 = vision.CascadeObjectDetector('EyePairSmall');
```

Next, we define the laptop screen dimensions and camera information manually with the following definitions:

```matlab
screenWidthCm = 50;
screenHeightCm = 30;
distanceToCameraCm = 60;
cameraFoV = 60;
```

We need to create an array to store the coordinates of the eye position with respect to time. This data will be collected for 30 seconds. The repeat variable `while true` will let us run a continuous loop of the eye tracking:

```matlab
pupilPositions = [];
startTime = tic;
duration = 30;
repeat = true;
```

Let us now define the loop that will run for the 30-second duration. This portion defines the capture of images, face and eye detection, pupil detection via the Hough transform algorithm, defines bounding boxes, gaze detection, and allows the loop to end:

```matlab
while repeat     
    vid = snapshot(cam);  
    vid = rgb2gray(vid);
    img = flip(vid, 2); 
    
    bbox = step(detector, img); 
      
    if ~isempty(bbox)  
        biggest_box = 1;     
        for i = 1:rank(bbox) 
            if bbox(i, 3) > bbox(biggest_box, 3)
                biggest_box = i;
            end
        end
        faceImage = imcrop(img, bbox(biggest_box, :)); 
        bboxeyes = step(detector1, faceImage); 
         
        subplot(221); subimage(img); hold on; 
        for i = 1:size(bbox, 1)    
            rectangle('position', bbox(i, :), 'lineWidth', 2, 'edgeColor', 'y');
        end
         
        subplot(223); subimage(faceImage);     
                 
        if ~isempty(bboxeyes)  
             
            biggest_box_eyes = 1;     
            for i = 1:rank(bboxeyes) 
                if bboxeyes(i, 3) > bboxeyes(biggest_box_eyes, 3)
                    biggest_box_eyes = i;
                end
            end
             
            bboxeyeshalf = [bboxeyes(biggest_box_eyes, 1), bboxeyes(biggest_box_eyes, 2), bboxeyes(biggest_box_eyes, 3)/3, bboxeyes(biggest_box_eyes, 4)];   
             
            eyesImage = imcrop(faceImage, bboxeyeshalf(1, :));    
            eyesImage = imadjust(eyesImage);    

            r = bboxeyeshalf(1, 4)/4;
            [centers, radii, metric] = imfindcircles(eyesImage, [floor(r-r/4) floor(r+r/2)], 'ObjectPolarity', 'dark', 'Sensitivity', 0.93); 
            [MI] = sort(radii, 'descend');
                 
            eyesPositions = centers;
                 
            subplot(222); subimage(eyesImage); hold on;
            viscircles(centers, radii, 'EdgeColor', 'b');
                  
            if ~isempty(centers)
                pupil_x = centers(1, 1);
                pupil_y = centers(1, 2);
                pupilPositions = [pupilPositions; pupil_x, pupil_y];
                disL = abs(0 - pupil_x);    
                disR = abs(bboxeyes(1, 3)/3 - pupil_x);
                subplot(224);
                if disL > disR + 16
                    subimage(right);
                elseif disR > disL
                    subimage(left);
                else
                    subimage(straight); 
                end
             end          
         end
     else
        subplot(224);
        subimage(noface);
     end
     set(gca, 'XtickLabel', [], 'YtickLabel', []);
     hold off;
     if toc(startTime) > duration
        repeat = false; 
     end
end
```

Now that we have defined most of our eye-tracking MATLAB process and data collection, we will normalize the pupil position to the screen dimensions that we previously defined. This enables us to map the gaze position on the screen (roughly). This can be accomplished with the following:

```matlab
if ~isempty(pupilPositions)
    imgWidth = size(vid, 2); 
    imgHeight = size(vid, 1); 

    normalizedPupilX = pupilPositions(:, 1) / imgWidth;
    normalizedPupilY = pupilPositions(:, 2) / imgHeight;

    screenPosX = normalizedPupilX * screenWidthCm;
    screenPosY = (1 - normalizedPupilY) * screenHeightCm; 
end
```

We can utilize a Gaussian kernel to smooth the data that was collected:

```matlab
kernelSize = 25;  
sigma = kernelSize / 5;  

[x, y] = meshgrid(linspace(-kernelSize/2, kernelSize/2, kernelSize), linspace(-kernelSize/2, kernelSize/2, kernelSize));
gaussianKernel = exp(-(x.^2 + y.^2) / (2 * sigma^2));
gaussianKernel = gaussianKernel / sum(gaussianKernel, 'all');  
```

This ends the eye-tracking MATLAB code segment. The commands we called above will detect the face, eyes, pupils, and collect an array of coordinates for their position on the screen. Let’s test the command by running it in MATLAB. It should successfully generate a window that can detect if you are looking left, right, or straight! It should look like Fig. 9.4.

**Figure 9.4: Eye Tracking**

To analyze and process the data one step further, we could try to generate a heatmap that represents a visual estimation of gaze points on the laptop screen, say if you were looking at an image. This plot can be accomplished with:

```matlab
if ~isempty(screenPosX) && ~isempty(screenPosY)
    gridSizeX = 100;  
    gridSizeY = 100;  
    
    [N, Xedges, Yedges] = histcounts2(screenPosX, screenPosY, [gridSizeX, gridSizeY]);
    
    density = N / sum(N, 'all');
    
    smoothedDensity = conv2(density, gaussianKernel, 'same');
    
    [X, Y] = meshgrid(linspace(0, screenWidthCm, gridSizeX), linspace(0, screenHeightCm, gridSizeY));
    
    figure;
    contourf(X, Y, smoothedDensity', 20);  
    colormap('hot');  
    colorbar;  
    title('Smoothed 2D Heatmap of Gaze on Screen');
    xlabel('Screen Width (cm)');
    ylabel('Screen Height (cm)');
    axis equal;  
else
    disp('No screen position data available for heatmap generation.');
end
```

**Figure 9.5: Smoothed 2D Heatmap**

The end results of running this 30-second code could produce a rough estimation of your gaze in a heatmap to the screen dimensions. Alternatively, to following all of the above steps, you can run the provided `eyelab.m` MATLAB file.

To experiment on mapping my gaze while looking at an image, let’s take a full-screen zoom of this chapter’s title image and map my gaze while looking at the title image shown on the right:

**Figure 9.6: Heatmap on Image**

The result, if we were to plot the heatmap as an overlay to the original image (Fig. 9.6) (bottom toolbar cropped out), shows us a rough idea of how my gaze was concentrated on the image.
```

This should work well in markdown format.
