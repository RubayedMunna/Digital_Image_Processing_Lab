% Read the original image
originalImage = imread('baby2.jpg');
% Define a structuring element for dilation
se = strel('disk', 5); % You can adjust the size of the disk
% Initialize an output image
dilatedImage = zeros(size(originalImage), 'like', originalImage);
% Perform dilation on each channel
for channel = 1:size(originalImage, 3)
    dilatedImage(:, :, channel) = imdilate(originalImage(:, :, channel), se);
end
% Create a figure to display the images
figure;
% Display the original image
subplot(1, 2, 1);
imshow(originalImage);
title('Original Image');
% Display the dilated image
subplot(1, 2, 2);
imshow(dilatedImage);
title('Dilated Image');