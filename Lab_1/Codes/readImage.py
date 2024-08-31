from google.colab import drive
from PIL import Image
from IPython.display import display
drive.mount("/content/drive", force_remount=True)

# Navigate to your image
img_path = '/content/drive/MyDrive/FruitBasket.PNG'

# Read the image
img = Image.open(img_path)

# Display the image
display(img)

