import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def linear_interpolation_resize(image_array, new_width, new_height):
    """
    Resize an image using linear interpolation method.
    """
    old_height, old_width, channels = image_array.shape
    resized_image_array = np.zeros((new_height, new_width, channels), dtype=image_array.dtype)
    row_scale = old_height / new_height
    col_scale = old_width / new_width

    for y in range(new_height):
        for x in range(new_width):
            orig_y = y * row_scale
            orig_x = x * col_scale
            y0 = int(orig_y)
            x0 = int(orig_x)
            y1 = min(y0 + 1, old_height - 1)
            x1 = min(x0 + 1, old_width - 1)
            dy = orig_y - y0
            dx = orig_x - x0
            w00 = (1 - dx) * (1 - dy)
            w01 = dx * (1 - dy)
            w10 = (1 - dx) * dy
            w11 = dx * dy

            for c in range(channels):
                pixel_value = (w00 * image_array[y0, x0, c] +
                               w01 * image_array[y0, x1, c] +
                               w10 * image_array[y1, x0, c] +
                               w11 * image_array[y1, x1, c])
                resized_image_array[y, x, c] = pixel_value
    return resized_image_array

def pixel_skipping_resize(image_array, new_width, new_height):
    """
    Resize an image using the pixel skipping method.
    """
    old_height, old_width, channels = image_array.shape
    resized_image_array = np.zeros((new_height, new_width, channels), dtype=image_array.dtype)
    row_scale = old_height / new_height
    col_scale = old_width / new_width

    for y in range(new_height):
        for x in range(new_width):
            src_y = int(y * row_scale)
            src_x = int(x * col_scale)
            resized_image_array[y, x] = image_array[src_y, src_x]
    return resized_image_array

def replicate_resize(image_array, new_width, new_height):
    """
    Resize an image using the replication method.
    """
    old_height, old_width, channels = image_array.shape
    resized_image_array = np.zeros((new_height, new_width, channels), dtype=image_array.dtype)
    row_scale = old_height / new_height
    col_scale = old_width / new_width

    for y in range(new_height):
        for x in range(new_width):
            src_y = int(y * row_scale)
            src_x = int(x * col_scale)
            # Use nearest neighbor replication
            resized_image_array[y, x] = image_array[src_y, src_x]
    return resized_image_array

# Load an image using PIL
image_path = 'rgb-image.jpg'  # Replace with your image path
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: The file {image_path} was not found.")
    exit()

image_array = np.array(image)

# Get and print the original image dimensions
original_height, original_width, _ = image_array.shape
print(f"Original image dimensions: {original_width}x{original_height}")

# Input the new dimensions for resizing
try:
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))
except ValueError:
    print("Error: Please enter valid integer values for width and height.")
    exit()

# Perform the resizing using different methods
resized_image_linear = linear_interpolation_resize(image_array, new_width, new_height)
resized_image_pixel_skip = pixel_skipping_resize(image_array, new_width, new_height)
resized_image_replicate = replicate_resize(image_array, new_width, new_height)

# Convert back to image for saving purposes
Image.fromarray(np.uint8(resized_image_linear)).save('outputs/linear_interpolation_resized.jpg')
Image.fromarray(np.uint8(resized_image_pixel_skip)).save('outputs/pixel_skipping_resized.jpg')
Image.fromarray(np.uint8(resized_image_replicate)).save('outputs/replication_resized.jpg')

# Plot and compare results
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image_array)
plt.axis('off')
plt.text(0.5, -0.1, f"Dimensions: {original_width}x{original_height}", ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)

# Resized using Linear Interpolation
plt.subplot(2, 2, 2)
plt.title('Resized Image using Linear Interpolation')
plt.imshow(resized_image_linear.astype(np.uint8))
plt.axis('off')
plt.text(0.5, -0.1, f"Dimensions: {new_width}x{new_height}", ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)

# Resized using Pixel Skipping
plt.subplot(2, 2, 3)
plt.title('Resized Image using Pixel Skipping')
plt.imshow(resized_image_pixel_skip.astype(np.uint8))
plt.axis('off')
plt.text(0.5, -0.1, f"Dimensions: {new_width}x{new_height}", ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)

# Resized using Replication
plt.subplot(2, 2, 4)
plt.title('Resized Image using Replication')
plt.imshow(resized_image_replicate.astype(np.uint8))
plt.axis('off')
plt.text(0.5, -0.1, f"Dimensions: {new_width}x{new_height}", ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()
