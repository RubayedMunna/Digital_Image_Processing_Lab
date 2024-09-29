import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to convert RGB to HSI
def rgb_to_hsi(rgb):
    # Normalize the RGB values to [0, 1]
    rgb = np.array(rgb, dtype=np.float64) / 255.0
    R = rgb[:, :, 0]
    G = rgb[:, :, 1]
    B = rgb[:, :, 2]
    
    # Compute Intensity
    I = (R + G + B) / 3
    
    # Compute Saturation
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-8)) * min_rgb
    S[R + G + B == 0] = 0  # Handle zero-intensity case
    
    # Compute Hue
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B) * (G - B)) + 1e-8
    theta = np.arccos(num / den)
    H = np.zeros_like(I)
    H[B <= G] = theta[B <= G]
    H[B > G] = 2 * np.pi - theta[B > G]
    
    # Convert radians to degrees and normalize to [0, 360]
    H = np.degrees(H)
    H[H < 0] += 360
    H = H % 360
    
    # Combine H, S, I into HSI
    hsi = np.stack((H, S, I), axis=-1)
    return hsi

# Read the RGB image
rgb_image = Image.open('flower.jpg').convert('RGB')

# Display the original RGB image
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')

# Convert RGB to HSI
hsi_image = rgb_to_hsi(rgb_image)

# Extract H, S, and I components
H = hsi_image[:, :, 0]
S = hsi_image[:, :, 1]
I = hsi_image[:, :, 2]

# Display the HSI components separately

# Display Hue component using a 'hsv' colormap for better visualization
plt.subplot(2, 2, 2)
plt.imshow(H, cmap='gray', vmin=0, vmax=360)  # Set vmin and vmax to match Hue range
plt.title('Hue Component')
plt.colorbar(label='Hue (degrees)')

# Display Saturation component in grayscale
plt.subplot(2, 2, 3)
plt.imshow(S, cmap='gray', vmin=0, vmax=1)
plt.title('Saturation Component')
plt.colorbar(label='Saturation')

# Display Intensity component in grayscale
plt.subplot(2, 2, 4)
plt.imshow(I, cmap='gray', vmin=0, vmax=1)
plt.title('Intensity Component')
plt.colorbar(label='Intensity')

# Show the plot
plt.tight_layout()
plt.show()
