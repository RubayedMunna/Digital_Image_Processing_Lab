% Read the original image
originalImage = imread('baby2.jpg');
% Define a structuring element for erosion
se = strel('disk', 5); % You can adjust the size of the disk
% Initialize an output image
erodedImage = zeros(size(originalImage), 'like', originalImage);
% Perform erosion on each channel
for channel = 1:size(originalImage, 3)
    erodedImage(:, :, channel) = imerode(originalImage(:, :, channel), se);
end
% Create a figure to display the images
figure;
% Display the original image
subplot(1, 2, 1);
imshow(originalImage);
title('Original Image');
% Display the eroded image
subplot(1, 2, 2);
imshow(erodedImage);
title('Eroded Image')