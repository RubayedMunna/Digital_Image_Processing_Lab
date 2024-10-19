import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
original_image_rgb = cv2.imread('baby2.jpg')

# Check if the image is loaded properly
if original_image_rgb is None:
    print("Error: Could not read the image. Please check the file path.")
    exit()

# Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
original_image_rgb = cv2.cvtColor(original_image_rgb, cv2.COLOR_BGR2RGB)

# Define the structuring element (disk-shaped) for erosion
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Perform erosion on each channel
eroded_image = np.zeros_like(original_image_rgb)
for channel in range(3):
    eroded_image[:, :, channel] = cv2.erode(original_image_rgb[:, :, channel], se)

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(eroded_image)
plt.title('Eroded Image')
plt.show()
