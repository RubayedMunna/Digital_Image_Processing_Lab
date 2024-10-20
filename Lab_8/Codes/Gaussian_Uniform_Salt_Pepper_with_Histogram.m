% Read the image
img = imread('image.jpg'); % Replace with your image file
img = im2double(img); % Convert to double for noise addition

% Gaussian Noise
gaussian_noise = imnoise(img, 'gaussian', 0, 0.01); % mean=0, variance=0.01

% Uniform Noise
uniform_noise = img + (rand(size(img)) - 0.5) * 0.2; % Uniform noise [-0.1, 0.1]

% Salt and Pepper Noise
salt_pepper_noise = imnoise(img, 'salt & pepper', 0.02); % noise density=0.02

% Plotting the original and noisy images
figure;

subplot(3,3,1);
imshow(img);
title('Original Image');

subplot(3,3,4);
imshow(gaussian_noise);
title('Gaussian Noise');

subplot(3,3,7);
imhist(gaussian_noise);
title('Gaussian Noise Histogram');

subplot(3,3,5);
imshow(uniform_noise);
title('Uniform Noise');

subplot(3,3,8);
imhist(uniform_noise);
title('Uniform Noise Histogram');

subplot(3,3,6);
imshow(salt_pepper_noise);
title('Salt & Pepper Noise');

subplot(3,3,9);
imhist(salt_pepper_noise);
title('Salt & Pepper Noise Histogram');
