% Read the original image
originalImage = imread('baby2.jpg');
% Define a structuring element
se = strel('disk', 5); % You can adjust the size of the disk
% Initialize output images
openedImage = zeros(size(originalImage), 'like', originalImage);
closedImage = zeros(size(originalImage), 'like', originalImage);
% Perform Opening and Closing on each channel
for channel = 1:size(originalImage, 3)
    openedImage(:, :, channel) = imopen(originalImage(:, :, channel), se);
    closedImage(:, :, channel) = imclose(originalImage(:, :, channel), se);
end
% Create a figure to display the images
figure;
% Display the original image
subplot(1, 3, 1);
imshow(originalImage);
title('Original Image');
% Display the opened image
subplot(1, 3, 2);
imshow(openedImage);
title('Opened Image');
% Display the closed image
subplot(1, 3, 3);
imshow(closedImage);
title('Closed Image');