% Read the image
img = imread('baby2.jpg'); % Replace 'your_image.jpg' with your image file
% Check if the image is already grayscale
if size(img, 3) == 3
    grayImg = rgb2gray(img); % Convert to grayscale if it's a color image
else
    grayImg = img; % Use the image as is if it's already grayscale
end

% Prewitt Edge Detection
prewitt_x = fspecial('prewitt'); % Horizontal Prewitt filter
prewitt_y = prewitt_x'; % Vertical Prewitt filter
prewitt_edge = sqrt(imfilter(double(grayImg), prewitt_x).^2 + imfilter(double(grayImg), prewitt_y).^2);

% Sobel Edge Detection
sobel_x = fspecial('sobel'); % Horizontal Sobel filter
sobel_y = sobel_x'; % Vertical Sobel filter
sobel_edge = sqrt(imfilter(double(grayImg), sobel_x).^2 + imfilter(double(grayImg), sobel_y).^2);

% Roberts Edge Detection
roberts_x = [1 0; 0 -1]; % Roberts horizontal filter
roberts_y = [0 1; -1 0]; % Roberts vertical filter
roberts_edge = sqrt(imfilter(double(grayImg), roberts_x).^2 + imfilter(double(grayImg), roberts_y).^2);

% Isotropic Edge Detection (Laplacian of Gaussian)
h = fspecial('gaussian', [5 5], 1); % Gaussian filter
smoothedImg = imfilter(double(grayImg), h); % Smooth the image
laplacian = fspecial('laplacian', 0.5); % Laplacian filter
log_edge = imfilter(smoothedImg, laplacian);

% Display results
figure;
subplot(3,2,1); imshow(img); title('Real Image');
subplot(3,2,2); imshow(prewitt_edge, []); title('Prewitt Edge Detection');
subplot(3,2,3); imshow(sobel_edge, []); title('Sobel Edge Detection');
subplot(3,2,4); imshow(roberts_edge, []); title('Roberts Edge Detection');
subplot(3,2,5); imshow(log_edge, []); title('Laplacian of Gaussian Edge Detection');

% Adjust figure properties
sgtitle('Edge Detection Methods');