% Clear workspace and reset figures
clear all;
clf('reset');

% Initialize webcam
cam = webcam();

% Load images for gaze direction indicators
right = imread('RIGHT.jpg');
left = imread('LEFT.jpg');
noface = imread('no_face.jpg');
straight = imread('STRAIGHT.jpg');

% Initialize Viola-Jones detectors for face and eyes
detector = vision.CascadeObjectDetector();
detector1 = vision.CascadeObjectDetector('EyePairSmall');

% Define screen dimensions and camera information
screenWidthCm = 50;
screenHeightCm = 30;
distanceToCameraCm = 60;
cameraFoV = 60;

% Initialize array for storing pupil positions and define loop duration
pupilPositions = [];
startTime = tic;
duration = 30;
repeat = true;

% Main loop for eye tracking
while repeat     
    vid = snapshot(cam);  
    vid = rgb2gray(vid);
    img = flip(vid, 2); 
    
    bbox = step(detector, img); 
      
    if ~isempty(bbox)  
        biggest_box = 1;     
        for i = 1:rank(bbox) 
            if bbox(i,3) > bbox(biggest_box,3)
                biggest_box = i;
            end
        end
        faceImage = imcrop(img, bbox(biggest_box,:)); 
        bboxeyes = step(detector1, faceImage); 
         
        subplot(2,2,1), subimage(img); hold on; 
        for i = 1:size(bbox,1)    
            rectangle('position', bbox(i, :), 'lineWidth', 2, 'edgeColor', 'y');
        end
         
        subplot(2,2,3), subimage(faceImage);     
                 
        if ~isempty(bboxeyes)  
            biggest_box_eyes = 1;     
            for i = 1:rank(bboxeyes) 
                if bboxeyes(i,3) > bboxeyes(biggest_box_eyes,3)
                    biggest_box_eyes = i;
                end
            end
             
            bboxeyeshalf = [bboxeyes(biggest_box_eyes,1), bboxeyes(biggest_box_eyes,2), bboxeyes(biggest_box_eyes,3)/3, bboxeyes(biggest_box_eyes,4)];   
             
            eyesImage = imcrop(faceImage, bboxeyeshalf(1,:));    
            eyesImage = imadjust(eyesImage);    

            r = bboxeyeshalf(1,4)/4;
            [centers, radii, metric] = imfindcircles(eyesImage, [floor(r-r/4) floor(r+r/2)], 'ObjectPolarity', 'dark', 'Sensitivity', 0.93); 
            [M, I] = sort(radii, 'descend');
                 
            eyesPositions = centers;
                 
            subplot(2,2,2), subimage(eyesImage); hold on;
            viscircles(centers, radii, 'EdgeColor', 'b');
                  
            if ~isempty(centers)
                pupil_x = centers(1,1);
                pupil_y = centers(1,2);
                pupilPositions = [pupilPositions; pupil_x, pupil_y];
                disL = abs(0 - pupil_x);    
                disR = abs(bboxeyes(1,3)/3 - pupil_x);
                subplot(2,2,4);
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
        subplot(2,2,4);
        subimage(noface);
    end
    set(gca,'XtickLabel',[],'YtickLabel',[]);
    hold off;
    if toc(startTime) > duration
        repeat = false; 
    end
end

% Normalize pupil position to screen dimensions
if ~isempty(pupilPositions)
    imgWidth = size(vid, 2); 
    imgHeight = size(vid, 1); 

    normalizedPupilX = pupilPositions(:,1) / imgWidth;
    normalizedPupilY = pupilPositions(:,2) / imgHeight;

    screenPosX = normalizedPupilX * screenWidthCm;
    screenPosY = (1 - normalizedPupilY) * screenHeightCm; 
end

% Apply Gaussian smoothing to the data
kernelSize = 25;  
sigma = kernelSize / 5;  

[x, y] = meshgrid(linspace(-kernelSize/2, kernelSize/2, kernelSize), linspace(-kernelSize/2, kernelSize/2, kernelSize));
gaussianKernel = exp(-(x.^2 + y.^2) / (2 * sigma^2));
gaussianKernel = gaussianKernel / sum(gaussianKernel, 'all');  

% Generate heatmap of gaze points
if ~isempty(screenPosX) && ~isempty(screenPosY)
    gridSizeX = 100;  
    gridSizeY = 100;  
    
    [N, Xedges, Yedges] = histcounts2(screenPosX, screenPosY, [gridSizeX gridSizeY]);
    
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
