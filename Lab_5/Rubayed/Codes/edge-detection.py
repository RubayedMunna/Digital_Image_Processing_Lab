import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('baby2.jpg')  # Replace with your image file
# Convert to RGB (OpenCV loads images in BGR format)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Check if the image is already grayscale
if len(img.shape) == 3:
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to grayscale if it's a color image
else:
    gray_img = img  # Use the image as is if it's already grayscale

# Prewitt Edge Detection
prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitt_edge_x = cv2.filter2D(gray_img.astype(float), -1, prewitt_x)
prewitt_edge_y = cv2.filter2D(gray_img.astype(float), -1, prewitt_y)
prewitt_edge = np.sqrt(prewitt_edge_x**2 + prewitt_edge_y**2)

# Sobel Edge Detection
sobel_x = cv2.Sobel(gray_img.astype(float), cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_img.astype(float), cv2.CV_64F, 0, 1, ksize=5)
sobel_edge = np.sqrt(sobel_x**2 + sobel_y**2)

# Roberts Edge Detection
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])
roberts_edge_x = cv2.filter2D(gray_img.astype(float), -1, roberts_x)
roberts_edge_y = cv2.filter2D(gray_img.astype(float), -1, roberts_y)
roberts_edge = np.sqrt(roberts_edge_x**2 + roberts_edge_y**2)

# Isotropic Edge Detection (Laplacian of Gaussian)
gaussian_blur = cv2.GaussianBlur(gray_img.astype(float), (5, 5), 1)
log_edge = cv2.Laplacian(gaussian_blur, cv2.CV_64F)

# Display results
plt.figure(figsize=(10, 10))
plt.subplot(3, 2, 1); plt.imshow(img.astype(np.uint8)); plt.title('Real Image'); plt.axis('off')
plt.subplot(3, 2, 2); plt.imshow(prewitt_edge, cmap='gray'); plt.title('Prewitt Edge Detection'); plt.axis('off')
plt.subplot(3, 2, 3); plt.imshow(sobel_edge, cmap='gray'); plt.title('Sobel Edge Detection'); plt.axis('off')
plt.subplot(3, 2, 4); plt.imshow(roberts_edge, cmap='gray'); plt.title('Roberts Edge Detection'); plt.axis('off')
plt.subplot(3, 2, 5); plt.imshow(log_edge, cmap='gray'); plt.title('Laplacian of Gaussian Edge Detection'); plt.axis('off')

# Adjust figure properties
plt.suptitle('Edge Detection Methods', fontsize=16)
plt.tight_layout()
plt.show()
