% Read the image
img = imread('image.jpg'); % Replace with your image file

% Check if the image is already grayscale, if not, convert it to grayscale
if size(img, 3) == 3
    img = rgb2gray(img); % Convert to grayscale if the image is in color
end

% Add periodic noise (for demonstration purposes)
[M, N] = size(img);
[x, y] = meshgrid(1:N, 1:M);
periodic_noise = 20 * sin(2 * pi * x / 10) + 20 * cos(2 * pi * y / 15);
noisy_img = double(img) + periodic_noise;

% Fourier Transform of the Noisy Image
F = fftshift(fft2(noisy_img));

% Display the Fourier Spectrum
figure;
subplot(2,3,1);
imshow(img, []);
title('Original Image');

subplot(2,3,2);
imshow(noisy_img, []);
title('Image with Periodic Noise');

subplot(2,3,3);
imshow(log(1 + abs(F)), []);
title('Fourier Spectrum of Noisy Image');

% Band Reject Filter Design
band_reject_filter = ones(M, N);
center_freq_x = N/2; % Center frequency in the x direction
center_freq_y = M/2; % Center frequency in the y direction
band_width = 10; % Width of the band to reject

% Create the band reject filter
for u = 1:M
    for v = 1:N
        D = sqrt((u - center_freq_y)^2 + (v - center_freq_x)^2); % Distance from center
        if (D >= 15) && (D <= (15 + band_width)) % Reject the frequencies in the specified band
            band_reject_filter(u, v) = 0;
        end
    end
end

% Apply the Band Reject Filter to the Fourier Transform
filtered_F = F .* band_reject_filter;

% Inverse Fourier Transform to get the denoised image
filtered_img = real(ifft2(ifftshift(filtered_F)));

% Normalize the filtered image for better visualization
filtered_img = mat2gray(filtered_img);

% Plotting the results
subplot(2,3,4);
imshow(log(1 + abs(filtered_F)), []);
title('Filtered Fourier Spectrum');

subplot(2,3,5);
imshow(filtered_img, []);
title('Denoised Image (After Band Reject Filtering)');
