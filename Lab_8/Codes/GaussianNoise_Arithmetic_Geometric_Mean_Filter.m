% Read the image
img = imread('motherboard.png'); % Replace with your image file
img = im2double(img); % Convert to double for better precision

% Add Gaussian Noise to the Image
noisy_img = imnoise(img, 'gaussian', 0, 0.01); % mean=0, variance=0.01

% 3x3 Arithmetic Mean Filter
arithmetic_mean_filter = fspecial('average', [3 3]); % Create a 3x3 averaging filter
arithmetic_filtered_img = imfilter(noisy_img, arithmetic_mean_filter, 'replicate');

% 3x3 Geometric Mean Filter (Custom implementation)
geometric_filtered_img = exp(imfilter(log(noisy_img + eps), ones(3,3), 'replicate') / 9);

% Plotting the original, noisy, and filtered images
figure;

subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,2);
imshow(noisy_img);
title('Image with Gaussian Noise');

subplot(2,2,3);
imshow(arithmetic_filtered_img);
title('Arithmetic Mean Filtered Image');

subplot(2,2,4);
imshow(geometric_filtered_img);
title('Geometric Mean Filtered Image');
