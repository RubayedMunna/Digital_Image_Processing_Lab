% Read the image
I = imread('image.jpeg');  % Replace with your image filename

% Convert the image to grayscale if it is in RGB
grayImage = rgb2gray(I);

% Apply edge detection (using Canny edge detector)
edges = edge(grayImage, 'canny');

% Perform the Hough transform
[H, theta, rho] = hough(edges);

% Find peaks in the Hough transform matrix
P = houghpeaks(H, 5, 'threshold', ceil(0.3 * max(H(:))));

% Find and draw lines on the original image
lines = houghlines(edges, theta, rho, P, 'FillGap', 5, 'MinLength', 7);

% Create a figure with multiple subplots
figure;

% Display the original image
subplot(2, 2, 1);
imshow(I);
title('Original Image');

% Display the edge-detected image
subplot(2, 2, 2);
imshow(edges);
title('Edge Detected Image');

% Display the Hough transform matrix
subplot(2, 2, 3);
imshow(imadjust(rescale(H)), 'XData', theta, 'YData', rho, ...
       'InitialMagnification', 'fit');
xlabel('\theta (degrees)');
ylabel('\rho');
axis on;
axis normal;
title('Hough Transform of Edge Image');
colormap(gca, hot);

% Plot the peaks on the Hough transform matrix
hold on;
plot(theta(P(:,2)), rho(P(:,1)), 's', 'color', 'blue');
hold off;

% Display the original image with detected lines
subplot(2, 2, 4);
imshow(I);
title('Detected Lines on Original Image');
hold on;

% Plot each detected line segment
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1), xy(:,2), 'LineWidth', 2, 'Color', 'green');

   % Plot beginnings and ends of lines
   plot(xy(1,1), xy(1,2), 'x', 'LineWidth', 2, 'Color', 'yellow');
   plot(xy(2,1), xy(2,2), 'x', 'LineWidth', 2, 'Color', 'red');
end

hold off;
