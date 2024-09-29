% Read the RGB image
rgbImage = imread('flower.jpg'); % Replace with your image file

% Extract the Red, Green, and Blue channels
RedChannel = rgbImage(:,:,1);
GreenChannel = rgbImage(:,:,2);
BlueChannel = rgbImage(:,:,3);

% Display the original RGB image and the individual channels
figure('Position', [100, 100, 800, 600]); % Set figure size

% Display original RGB image
subplot(2, 2, 1);
imshow(rgbImage);
title('Original RGB Image');
axis off;

% Display Red channel
subplot(2, 2, 2);
imshow(RedChannel);
title('Red Channel');
axis off;

% Display Green channel
subplot(2, 2, 3);
imshow(GreenChannel);
title('Green Channel');
axis off;

% Display Blue channel
subplot(2, 2, 4);
imshow(BlueChannel);
title('Blue Channel');
axis off;

% Adjust layout
tight_layout();
