import cv2
import numpy as np
import matplotlib.pyplot as plt

# List of image files to process
image_files = ['moody.jpg', 'baby2.jpg', 'flower.jpg']

# Create a figure to hold all the subplots
plt.figure(figsize=(15, 10))

# Loop through each image file
for i, image_file in enumerate(image_files):
    # Load the image
    original_image = cv2.imread(image_file)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Check if it's a color image
    if original_image_rgb.shape[2] == 3:
        # Perform FFT for each channel
        fft_images = [np.fft.fft2(original_image_rgb[:, :, channel]) for channel in range(3)]
        fft_images_shifted = [np.fft.fftshift(fft_image) for fft_image in fft_images]
        magnitude_spectrum = [np.log(1 + np.abs(fft_shifted)) for fft_shifted in fft_images_shifted]
        magnitude_spectrum_avg = sum(magnitude_spectrum) / 3
    else:
        fft_image = np.fft.fft2(original_image_rgb)
        fft_image_shifted = np.fft.fftshift(fft_image)
        magnitude_spectrum_avg = np.log(1 + np.abs(fft_image_shifted))

    # Plot the original image
    plt.subplot(len(image_files), 2, 2 * i + 1)  # Row: len(image_files), Col: 2, Pos: i*2+1
    plt.imshow(original_image_rgb)
    plt.title(f'Original Image {i+1}')
    plt.axis('off')  # Hide axis

    # Plot the magnitude spectrum
    plt.subplot(len(image_files), 2, 2 * i + 2)  # Row: len(image_files), Col: 2, Pos: i*2+2
    plt.imshow(magnitude_spectrum_avg, cmap='gray')
    plt.title(f'Magnitude Spectrum {i+1}')
    plt.axis('off')  # Hide axis

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
