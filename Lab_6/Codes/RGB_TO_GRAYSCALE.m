% Read the RGB image
rgbImage = imread('flower.jpg');

% Method 1: Using the Formula
% Convert to grayscale using the weighted sum formula
grayscaleImage_formula = 0.2989 * rgbImage(:,:,1) + 0.5870 * rgbImage(:,:,2) + 0.1140 * rgbImage(:,:,3);

% Display the original RGB image and grayscale image
figure;
subplot(1, 2, 1);
imshow(rgbImage);
title('Original RGB Image');
axis off;

subplot(1, 2, 2);
imshow(grayscaleImage_formula, []);
title('Grayscale Image (Formula)');
axis off;

% Method 2: Using MATLAB's built-in function
% Convert to grayscale using rgb2gray
grayscaleImage_builtin = rgb2gray(rgbImage);

% Display the grayscale image using built-in function
figure;
subplot(1, 2, 1);
imshow(rgbImage);
title('Original RGB Image');
axis off;

subplot(1, 2, 2);
imshow(grayscaleImage_builtin);
title('Grayscale Image (Built-in)');
axis off;

