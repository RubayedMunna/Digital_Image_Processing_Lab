import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to convert RGB to YIQ
def rgb_to_yiq(rgb_image):
    # Normalize the RGB values to [0, 1]
    rgb_image = np.array(rgb_image, dtype=np.float64) / 255.0
    
    # Define the transformation matrix from RGB to YIQ
    transform_matrix = np.array([[0.299, 0.587, 0.114],
                                 [0.595, -0.274, -0.321],
                                 [0.211, -0.523, 0.312]])
    
    # Reshape the RGB image to a 2D array of shape (height*width, 3)
    h, w, _ = rgb_image.shape
    rgb_flat = rgb_image.reshape(-1, 3)
    
    # Apply the transformation matrix
    yiq_flat = np.dot(rgb_flat, transform_matrix.T)
    
    # Reshape the result back to the original image shape
    yiq_image = yiq_flat.reshape(h, w, 3)
    
    return yiq_image

# Read the RGB image
rgb_image = Image.open('flower.jpg').convert('RGB')

# Convert RGB to YIQ
yiq_image = rgb_to_yiq(rgb_image)

# Extract Y, I, and Q components
Y = yiq_image[:, :, 0]
I = yiq_image[:, :, 1]
Q = yiq_image[:, :, 2]

# Display all images in a single plot
plt.figure(figsize=(15, 10))

# Display original RGB image
plt.subplot(2, 3, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')
plt.axis('off')

# Display Y component (luminance)
plt.subplot(2, 3, 2)
plt.imshow(Y, vmin=0, vmax=1)
plt.title('Y Component (Luminance)')
plt.colorbar(label='Y')
plt.axis('off')

# Display I component (in-phase chrominance)
plt.subplot(2, 3, 3)
plt.imshow(I,  vmin=-0.595, vmax=0.595)  # Using typical I range for display
plt.title('I Component (In-phase Chrominance)')
plt.colorbar(label='I')
plt.axis('off')

# Display Q component (quadrature chrominance)
plt.subplot(2, 3, 4)
plt.imshow(Q,  vmin=-0.522, vmax=0.522)  # Using typical Q range for display
plt.title('Q Component (Quadrature Chrominance)')
plt.colorbar(label='Q')
plt.axis('off')

# Display combined YIQ image (approximated visualization)
plt.subplot(2, 3, 5)
# Normalizing the combined YIQ image to [0, 1] for display
normalized_yiq = (yiq_image - yiq_image.min()) / (yiq_image.max() - yiq_image.min())
plt.imshow(normalized_yiq)
plt.title('Combined YIQ Image')
plt.axis('off')

plt.tight_layout()
plt.show()
