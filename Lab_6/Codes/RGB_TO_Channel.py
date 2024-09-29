import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Read the RGB image
rgb_image = Image.open('flower.jpg').convert('RGB')
rgb_array = np.array(rgb_image)

# Extract the Red, Green, and Blue channels
RedChannel = rgb_array[:, :, 0]
GreenChannel = rgb_array[:, :, 1]
BlueChannel = rgb_array[:, :, 2]

# Display the original RGB image and the individual channels
plt.figure(figsize=(10, 8))

# Display original RGB image
plt.subplot(2, 2, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')
plt.axis('off')

# Display Red channel
plt.subplot(2, 2, 2)
plt.imshow(RedChannel, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

# Display Green channel
plt.subplot(2, 2, 3)
plt.imshow(GreenChannel, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

# Display Blue channel
plt.subplot(2, 2, 4)
plt.imshow(BlueChannel, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.tight_layout()
plt.show()
