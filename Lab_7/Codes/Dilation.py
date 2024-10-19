import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the original image
original_image = cv2.imread('baby2.jpg')
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Define a structuring element for dilation
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Perform dilation on each channel
dilated_image = np.zeros_like(original_image_rgb)
for channel in range(3):
    dilated_image[:, :, channel] = cv2.dilate(original_image_rgb[:, :, channel], se)

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(dilated_image)
plt.title('Dilated Image')
plt.show()
