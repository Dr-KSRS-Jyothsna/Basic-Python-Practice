"""
File: matplotlib_image_cmap.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program reads an image and displays it using Matplotlib
with different colormaps (cmap).
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# --------------------------------------------------
# Read the image
# --------------------------------------------------
img = Image.open("image.jpg")

# Convert image to NumPy array
img_array = np.array(img)

# --------------------------------------------------
# Display original image (RGB)
# --------------------------------------------------
plt.figure()
plt.title("Original Image")
plt.imshow(img_array)
plt.axis("off")
plt.show()

# --------------------------------------------------
# Convert image to grayscale
# --------------------------------------------------
gray_img = img.convert("L")
gray_array = np.array(gray_img)

# --------------------------------------------------
# Display grayscale image
# --------------------------------------------------
plt.figure()
plt.title("Grayscale Image (cmap='gray')")
plt.imshow(gray_array, cmap="gray")
plt.axis("off")
plt.show()

# --------------------------------------------------
# Display image with different colormaps
# --------------------------------------------------
cmaps = ["viridis", "hot", "jet", "plasma", "cool"]

for cmap in cmaps:
    plt.figure()
    plt.title(f"Colormap: {cmap}")
    plt.imshow(gray_array, cmap=cmap)
    plt.axis("off")
    plt.show()
