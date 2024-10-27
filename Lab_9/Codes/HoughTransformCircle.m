% Read the image
img = imread('Circle_Image.jpg');  % Replace 'Circle_Image.jpg' with your image file

% Check if the image is grayscale or RGB, and convert if necessary
if size(img, 3) == 3
    grayImg = rgb2gray(img);       % Convert to grayscale if the image is RGB
else
    grayImg = img;                 % Image is already grayscale
end

% Set radius range based on expected circle sizes
minRadius = 20;
maxRadius = 150;

% Detect circles using Circular Hough Transform
[centers, radii, metric] = imfindcircles(grayImg, [minRadius maxRadius], ...
                                         'Sensitivity', 0.95, 'EdgeThreshold', 0.1);

% Plot both the original image and the detected circles side-by-side
figure;

% Display the original image
subplot(1, 2, 1);
imshow(img);
title('Original Image');

% Display the image with detected circles
subplot(1, 2, 2);
imshow(img);
title('Detected Circles');
hold on;

% Check if any circles are detected
if ~isempty(centers)
    % Draw circles and mark centers
    viscircles(centers, radii, 'EdgeColor', 'b', 'LineWidth', 1.5);
    plot(centers(:,1), centers(:,2), 'r+', 'MarkerSize', 10, 'LineWidth', 2);
else
    disp('No circles were detected.');
end

hold off;
