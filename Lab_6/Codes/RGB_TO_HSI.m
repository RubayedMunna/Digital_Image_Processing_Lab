% Read the RGB image
rgbImage = imread('flower.jpg'); % Replace with your image file

% Display the original RGB image
figure;
subplot(2, 2, 1);
imshow(rgbImage);
title('Original RGB Image');

% Convert RGB to HSI
hsiImage = rgb2hsi(rgbImage);

% Extract H, S, and I components
H = hsiImage(:,:,1);
S = hsiImage(:,:,2);
I = hsiImage(:,:,3);

% Normalize H, S, and I for display purposes
H_disp = H / 360; % Normalize Hue to [0, 1] for display
S_disp = S; % Saturation is already in [0, 1]
I_disp = I; % Intensity is already in [0, 1]

% Display the HSI components separately

% Display Hue component using 'hsv' colormap
subplot(2, 2, 2);
imshow(H_disp);
colormap(gca, gray); % Apply the hsv colormap to the current axis
colorbar; % Show colorbar to indicate Hue range
caxis([0 1]); % Set the color axis to match [0, 1] (normalized)
title('Hue Component');

% Display Saturation component
subplot(2, 2, 3);
imshow(S_disp);
colormap(gca, gray); % Apply the gray colormap to the current axis
colorbar; % Show colorbar to indicate Saturation range
caxis([0 1]); % Set the color axis to match [0, 1]
title('Saturation Component');

% Display Intensity component
subplot(2, 2, 4);
imshow(I_disp);
colormap(gca, gray); % Apply the gray colormap to the current axis
colorbar; % Show colorbar to indicate Intensity range
caxis([0 1]); % Set the color axis to match [0, 1]
title('Intensity Component');

% Function to convert RGB to HSI
function hsi = rgb2hsi(rgb)
    % Normalize the RGB values
    rgb = double(rgb) / 255; % Normalize to [0, 1]
    R = rgb(:,:,1);
    G = rgb(:,:,2);
    B = rgb(:,:,3);
    
    % Compute Intensity
    I = (R + G + B) / 3;
    
    % Compute Saturation
    min_val = min(min(R, G), B);
    S = 1 - (3 ./ (R + G + B + eps)) .* min_val;
    S(R + G + B == 0) = 0; % Handle zero-intensity case
    
    % Compute Hue
    num = 0.5 * ((R - G) + (R - B));
    den = sqrt((R - G).^2 + (R - B) .* (G - B)) + eps;
    theta = acos(num ./ den);
    H = zeros(size(I));
    H(B <= G) = theta(B <= G);
    H(B > G) = 2 * pi - theta(B > G);
    
    % Convert radians to degrees
    H = H * (180 / pi);
    
    % Normalize H to [0, 360]
    H(H < 0) = H(H < 0) + 360;
    H = mod(H, 360);
    
    % Combine H, S, I into HSI
    hsi = cat(3, H, S, I);
end
