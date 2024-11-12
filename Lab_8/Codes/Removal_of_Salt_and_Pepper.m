% Read the image
img = imread('image.jpg'); % Replace with your image file

% Add Salt and Pepper Noise
noisy_img = imnoise(img, 'salt & pepper', 0.10); % Add salt & pepper noise with noise density 0.10

% Check if the image is grayscale or color
if size(noisy_img, 3) == 3
    % If color image, apply median filter to each channel separately
    denoised_img = noisy_img; % Initialize denoised_img with the same size
    for c = 1:3
        denoised_img(:,:,c) = medfilt2(noisy_img(:,:,c), [3 3]); % Apply median filter to each color channel
    end
else
    % If grayscale image, apply median filter directly
    denoised_img = medfilt2(noisy_img, [3 3]); % Apply median filter to grayscale image
end

% Plotting the original, noisy, and denoised images
figure;

subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,2);
imshow(noisy_img);
title('Image with Salt & Pepper Noise');

subplot(2,2,3);
imshow(denoised_img);
title('Denoised Image (Median Filter)');
