% Step 1: Get User Input for Image File and New Size
% Prompt user for the image file name
imageFileName = input('Enter the image file name (e.g., ''peppers.png''): ', 's');
% Read the image
originalImage = imread(imageFileName);
% Prompt user for the new size
newHeight = input('Enter the new height for resizing: ');
newWidth = input('Enter the new width for resizing: ');
newSize = [newHeight, newWidth]; % New size [height, width]
% Convert to double if needed for better interpolation results
if ~isa(originalImage, 'double')
    originalImage = im2double(originalImage);
end
% Step 2: Resize using Replication Method (Nearest-Neighbor Interpolation)
resizedImageReplication = imresize(originalImage, newSize, 'nearest');
% Step 3: Resize using Linear Interpolation Method (Bilinear Interpolation)
resizedImageLinear = imresize(originalImage, newSize, 'bilinear');
% Step 4: Resize using Pixel Skipping Method
% Pixel skipping involves subsampling
% Calculate the skipping ratio
originalSize = size(originalImage);
rowRatio = originalSize(1) / newSize(1);
colRatio = originalSize(2) / newSize(2);
% Use floor to ensure indices are within bounds
rowSkip = floor(rowRatio);
colSkip = floor(colRatio);
% Generate the resized image by skipping pixels
resizedImagePixelSkipping = originalImage(1:rowSkip:end, 1:colSkip:end, :);
% Adjust size to match exactly if necessary
% Resize pixel skipping result to newSize using imresize if necessary
resizedImagePixelSkipping = imresize(resizedImagePixelSkipping, newSize, 'nearest');
% Step 5: Display the Results
figure;
subplot(2, 2, 1);
imshow(originalImage);
title('Original Image');
subplot(2, 2, 2);
imshow(resizedImageReplication);
title('Resized Image (Replication)');
subplot(2, 2, 3);
imshow(resizedImageLinear);
title('Resized Image (Linear Interpolation)');
subplot(2, 2, 4);
imshow(resizedImagePixelSkipping);
title('Resized Image (Pixel Skipping)');