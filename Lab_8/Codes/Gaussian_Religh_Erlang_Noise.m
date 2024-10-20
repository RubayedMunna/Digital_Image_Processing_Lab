% Read the image
img = imread('image.jpg'); % Replace with your image file
img = im2double(img); % Convert to double for noise addition

% Gaussian Noise
gaussian_noise = imnoise(img, 'gaussian', 0, 0.01); % mean=0, variance=0.01

% Rayleigh Noise
rayleigh_noise = img + raylrnd(0.2, size(img)); % scale parameter=0.2

% Erlang Noise (Using Gamma distribution since Erlang is a special case of Gamma)
k = 0.25; % Shape parameter (integer for Erlang)
lambda = 1; % Rate parameter
erlang_noise = img + gamrnd(k, 1/lambda, size(img)); 

% Plotting the original and noisy images
figure;

subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,2);
imshow(gaussian_noise);
title('Image with Gaussian Noise');

subplot(2,2,3);
imshow(rayleigh_noise);
title('Image with Rayleigh Noise');

subplot(2,2,4);
imshow(erlang_noise);
title('Image with Erlang Noise');
