from PIL import Image
import matplotlib.pyplot as plt

# Provide the correct path to your image
image_path = 'FruitBasket.jpg'  # Adjust this if the file is in a different directory
image = Image.open(image_path)

# Display the image
plt.imshow(image)
plt.axis('off')  # Hide axes
plt.show()

