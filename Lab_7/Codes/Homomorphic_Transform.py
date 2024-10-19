import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the original image
original_image = cv2.imread('moody.jpg')
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
original_image_double = np.float64(original_image_rgb) + 1  # Convert to double and avoid log(0)

# Perform homomorphic filtering on each channel
rows, cols, channels = original_image_double.shape
output_image = np.zeros_like(original_image_double)

for channel in range(3):
    # Perform FFT
    fft_image = np.fft.fft2(original_image_double[:, :, channel])
    fft_image_shifted = np.fft.fftshift(fft_image)

    # Get the magnitude and phase
    magnitude = np.abs(fft_image_shifted)
    phase = np.angle(fft_image_shifted)

    # Define a Gaussian filter in the frequency domain
    crow, ccol = rows // 2, cols // 2
    x, y = np.meshgrid(np.arange(cols), np.arange(rows))
    sigma = 30  # Standard deviation for Gaussian filter
    gaussian_filter = np.exp(-((x - ccol) ** 2 + (y - crow) ** 2) / (2 * sigma ** 2))

    # Apply the filter to the magnitude
    filtered_magnitude = magnitude * gaussian_filter

    # Create a new complex image with filtered magnitude and original phase
    homomorphic_image = filtered_magnitude * np.exp(1j * phase)

    # Perform inverse FFT
    homomorphic_image_shifted = np.fft.ifftshift(homomorphic_image)
    output_image[:, :, channel] = np.fft.ifft2(homomorphic_image_shifted).real

# Normalize to [0, 1]
output_image_normalized = cv2.normalize(output_image, None, 0, 1, cv2.NORM_MINMAX)

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(output_image_normalized)
plt.title('Homomorphic Filtered Image')
plt.show()
