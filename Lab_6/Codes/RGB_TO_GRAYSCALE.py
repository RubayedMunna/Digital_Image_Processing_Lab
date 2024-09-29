import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Method 1: Using the Formula

# Read the RGB image
rgb_image = Image.open('flower.jpg').convert('RGB')
rgb_array = np.array(rgb_image)

# Convert to grayscale using the weighted sum formula
grayscale_image = 0.2989 * rgb_array[:, :, 0] + 0.5870 * rgb_array[:, :, 1] + 0.1140 * rgb_array[:, :, 2]

# Display the grayscale image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image (Formula)')
plt.axis('off')

plt.tight_layout()
plt.show()


# Method 2: Using PIL

# Convert to grayscale using PIL
grayscale_image_pil = rgb_image.convert('L')

# Display the grayscale image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(grayscale_image_pil, cmap='gray')
plt.title('Grayscale Image (PIL)')
plt.axis('off')

plt.tight_layout()
plt.show()
