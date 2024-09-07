from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('rubayed_image.jpg')


image_array = np.array(image)


negative_array = 255 - image_array

negative_image = Image.fromarray(negative_array.astype(np.uint8))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_array)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Negative Image')
plt.imshow(negative_array, cmap='gray')
plt.axis('off')
plt.show()
negative_image.save('negative_purple.jpg')
