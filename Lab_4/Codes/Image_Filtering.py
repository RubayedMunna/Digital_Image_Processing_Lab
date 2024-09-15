import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import convolve, median_filter, gaussian_filter
import os

def mean_filter(image_array, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd.")
    
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
    filtered_image_array = np.zeros_like(image_array)

    for i in range(3):  # Assuming image_array has 3 channels (RGB)
        filtered_image_array[:, :, i] = convolve(image_array[:, :, i], kernel, mode='reflect')
    
    return filtered_image_array

def apply_median_filter(image_array, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd.")
    
    filtered_image_array = np.zeros_like(image_array)
    
    for i in range(3):  # Assuming image_array has 3 channels (RGB)
        filtered_image_array[:, :, i] = median_filter(image_array[:, :, i], size=kernel_size)
    
    return filtered_image_array

def apply_gaussian_filter(image_array, sigma):
    filtered_image_array = np.zeros_like(image_array)
    
    for i in range(3):  # Assuming image_array has 3 channels (RGB)
        filtered_image_array[:, :, i] = gaussian_filter(image_array[:, :, i], sigma=sigma)
    
    return filtered_image_array

# Load an image using PIL
image_path = 'image.jpg'  # Replace with your image path
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Ensure the image is RGB
if image_array.ndim == 3 and image_array.shape[2] == 3:
    # Apply filters
    mean_filtered_array = mean_filter(image_array, kernel_size=5)
    median_filtered_array = apply_median_filter(image_array, kernel_size=5)
    gaussian_filtered_array = apply_gaussian_filter(image_array, sigma=1.0)
else:
    raise ValueError("The input image is not an RGB image.")

# Create outputs directory in the same directory as the script
output_dir = os.path.join(os.getcwd(), 'outputs')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Convert results back to images
mean_filtered_image = Image.fromarray(np.uint8(mean_filtered_array))
median_filtered_image = Image.fromarray(np.uint8(median_filtered_array))
gaussian_filtered_image = Image.fromarray(np.uint8(gaussian_filtered_array))

# Save the results
mean_filtered_image.save(os.path.join(output_dir, 'mean_filtered_image.jpg'))
median_filtered_image.save(os.path.join(output_dir, 'median_filtered_image.jpg'))
gaussian_filtered_image.save(os.path.join(output_dir, 'gaussian_filtered_image.jpg'))

# Display the images
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image_array)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Mean Filtered Image')
plt.imshow(mean_filtered_array)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Median Filtered Image')
plt.imshow(median_filtered_array)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Gaussian Filtered Image')
plt.imshow(gaussian_filtered_array)
plt.axis('off')

plt.show()
