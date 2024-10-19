% Read the original image
originalImage = imread('moody.jpg');
% Convert the image to double for processing
originalImage = double(originalImage) + 1; % Add 1 to avoid log(0)
% Get the dimensions of the image
[rows, cols, channels] = size(originalImage);
% Initialize output image
outputImage = zeros(size(originalImage));
% Perform homomorphic filtering on each channel
for channel = 1:channels
    % Perform the FFT
    fftImage = fft2(originalImage(:, :, channel));
    fftImageShifted = fftshift(fftImage);
    
    % Get the magnitude and phase
    magnitude = abs(fftImageShifted);
    phase = angle(fftImageShifted);
    
    % Define a Gaussian filter in the frequency domain
    crow = round(rows/2);
    ccol = round(cols/2);
    [x, y] = meshgrid(1:cols, 1:rows);
    sigma = 30; % Standard deviation for Gaussian filter
    gaussianFilter = exp(-((x - ccol).^2 + (y - crow).^2) / (2 * sigma^2));
    
    % Apply the filter to the magnitude
    filteredMagnitude = magnitude .* gaussianFilter;
    
    % Create a new complex image with filtered magnitude and original phase
    homomorphicImage = filteredMagnitude .* exp(1i * phase);
    
    % Perform the inverse FFT
    homomorphicImageShifted = ifftshift(homomorphicImage);
    outputImage(:, :, channel) = ifft2(homomorphicImageShifted);
end
% Take the real part and normalize
outputImage = real(outputImage);
outputImage = mat2gray(outputImage); % Normalize to [0, 1]
% Create a figure to display the images
figure;
% Display the original image
subplot(1, 2, 1);
imshow(uint8(originalImage)); % Convert back to uint8 for display
title('Original Image');
% Display the homomorphic filtered image
subplot(1, 2, 2);
imshow(outputImage);
title('Homomorphic Filtered Image');
