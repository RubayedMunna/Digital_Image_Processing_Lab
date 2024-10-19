import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
original_image_rgb = cv2.imread('baby2.jpg')
# Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
original_image_rgb = cv2.cvtColor(original_image_rgb, cv2.COLOR_BGR2RGB)

# Define the structuring element (disk-shaped)
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Perform Opening and Closing on each channel
opened_image = np.zeros_like(original_image_rgb)
closed_image = np.zeros_like(original_image_rgb)
for channel in range(3):
    opened_image[:, :, channel] = cv2.morphologyEx(original_image_rgb[:, :, channel], cv2.MORPH_OPEN, se)
    closed_image[:, :, channel] = cv2.morphologyEx(original_image_rgb[:, :, channel], cv2.MORPH_CLOSE, se)

# Display the images
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(opened_image)
plt.title('Opened Image')
plt.subplot(1, 3, 3)
plt.imshow(closed_image)
plt.title('Closed Image')
plt.show()
