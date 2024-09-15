% Load the image
image = imread('image.jpg');
image_gray = rgb2gray(image);  % Convert to grayscale if needed

% Define the mean filter (5x5 kernel)
mean_filter = fspecial('average', [5 5]);

% Apply the mean filter
mean_filtered = imfilter(image_gray, mean_filter);

% Apply the median filter (5x5 kernel)
median_filtered = medfilt2(image_gray, [5 5]);

% Define the Gaussian filter (5x5 kernel, sigma=1)
gaussian_filter = fspecial('gaussian', [5 5], 1);

% Apply the Gaussian filter
gaussian_filtered = imfilter(image_gray, gaussian_filter);

% Plot all the images in one frame
figure;

% Original image
subplot(2, 2, 1);
imshow(image_gray);
title('Original Image');

% Mean filtered image
subplot(2, 2, 2);
imshow(mean_filtered);
title('Mean Filtered Image');

% Median filtered image
subplot(2, 2, 3);
imshow(median_filtered);
title('Median Filtered Image');

% Gaussian filtered image
subplot(2, 2, 4);
imshow(gaussian_filtered);
title('Gaussian Filtered Image');

% Save the composite figure
saveas(gcf, 'filtered_images_composite.jpg');
