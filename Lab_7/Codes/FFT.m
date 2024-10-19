% List of image files to process
imageFiles = {'moody.jpg', 'baby2.jpg', 'flower.jpg'}; % Add more image file names if needed
numImages = length(imageFiles);
% Create a figure to display the results
figure;
% Loop through each image file
for i = 1:numImages
    % Read the image
    originalImage = imread(imageFiles{i});
    
    % Check if the image has multiple color channels
    if size(originalImage, 3) == 3
        % Perform 2D FFT for each channel individually
        fftImageR = fft2(double(originalImage(:,:,1)));
        fftImageG = fft2(double(originalImage(:,:,2)));
        fftImageB = fft2(double(originalImage(:,:,3)));
        % Shift the zero frequency component to the center for each channel
        fftImageShiftedR = fftshift(fftImageR);
        fftImageShiftedG = fftshift(fftImageG);
        fftImageShiftedB = fftshift(fftImageB);
        % Compute the magnitude spectrum for each channel
        magnitudeSpectrumR = log(1 + abs(fftImageShiftedR)); % Red channel
        magnitudeSpectrumG = log(1 + abs(fftImageShiftedG)); % Green channel
        magnitudeSpectrumB = log(1 + abs(fftImageShiftedB)); % Blue channel
        % Compute the average magnitude spectrum for RGB channels
        magnitudeSpectrumAvg = (magnitudeSpectrumR + magnitudeSpectrumG + magnitudeSpectrumB) / 3;
        
    else
        % Perform FFT on the grayscale image
        fftImage = fft2(double(originalImage));
        fftImageShifted = fftshift(fftImage);
        magnitudeSpectrumAvg = log(1 + abs(fftImageShifted));
    end
    % Display the original image
    subplot(numImages, 2, 2*i-1);
    imshow(originalImage);
    title(['Original Image ', num2str(i)]);
    
    % Display the average magnitude spectrum (log scale)
    subplot(numImages, 2, 2*i);
    imshow(magnitudeSpectrumAvg, []);
    title(['Magnitude Spectrum ', num2str(i)]);
end