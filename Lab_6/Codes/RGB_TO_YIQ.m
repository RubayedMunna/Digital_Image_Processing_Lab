% Read the RGB image
rgbImage = imread('flower.jpg');

% Convert RGB to YIQ
yiqImage = rgb2yiq(rgbImage);

% Extract Y, I, and Q components
Y = yiqImage(:,:,1);
I = yiqImage(:,:,2);
Q = yiqImage(:,:,3);

% Display all images in a single plot
figure;

% Display original RGB image
subplot(2, 3, 1);
imshow(rgbImage);
title('Original RGB Image');

% Display Y component (luminance)
subplot(2, 3, 2);
imshow(Y, []);
title('Y Component (Luminance)');
colorbar;

% Display I component (in-phase chrominance)
subplot(2, 3, 3);
imshow(I, []);
title('I Component (In-phase Chrominance)');
colorbar;

% Display Q component (quadrature chrominance)
subplot(2, 3, 4);
imshow(Q, []);
title('Q Component (Quadrature Chrominance)');
colorbar;

% Display combined YIQ image (approximated visualization)
subplot(2, 3, 5);
normalized_yiq = mat2gray(yiqImage); % Normalize for display
imshow(normalized_yiq);
title('Combined YIQ Image');

% Function to convert RGB to YIQ
function yiq = rgb2yiq(rgb)
    % Normalize the RGB values to [0, 1]
    rgb = double(rgb) / 255;

    % Define the transformation matrix from RGB to YIQ
    transform_matrix = [0.299, 0.587, 0.114;
                        0.595, -0.274, -0.321;
                        0.211, -0.523, 0.312];

    % Reshape the RGB image to a 2D array of shape (height*width, 3)
    [h, w, ~] = size(rgb);
    rgb_flat = reshape(rgb, [], 3);

    % Apply the transformation matrix
    yiq_flat = rgb_flat * transform_matrix';

    % Reshape the result back to the original image shape
    yiq = reshape(yiq_flat, h, w, 3);
end
