"""
File: image_style_matrix_operations.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates image-style matrix operations using NumPy
and Matplotlib. A matrix is treated as an image for visualization
and transformation.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Create a 10x10 matrix (acts like an image)
# --------------------------------------------------
matrix = np.arange(1, 101).reshape(10, 10)

plt.figure()
plt.title("Original Matrix (Image View)")
plt.imshow(matrix, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 1. Horizontal Flip (Left–Right)
# --------------------------------------------------
h_flip = matrix[:, ::-1]

plt.figure()
plt.title("Horizontal Flip")
plt.imshow(h_flip, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 2. Vertical Flip (Top–Bottom)
# --------------------------------------------------
v_flip = matrix[::-1, :]

plt.figure()
plt.title("Vertical Flip")
plt.imshow(v_flip, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 3. Rotate 180 Degrees
# --------------------------------------------------
rotate_180 = matrix[::-1, ::-1]

plt.figure()
plt.title("180 Degree Rotation")
plt.imshow(rotate_180, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 4. Cropping (Center 4x4 region)
# --------------------------------------------------
crop = matrix[3:7, 3:7]

plt.figure()
plt.title("Cropped Matrix")
plt.imshow(crop, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 5. Thresholding (Binary Image)
# --------------------------------------------------
threshold = matrix > 50

plt.figure()
plt.title("Thresholding (matrix > 50)")
plt.imshow(threshold, cmap="gray")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 6. Masking (Highlight values > 70)
# --------------------------------------------------
masked = np.zeros_like(matrix)
masked[matrix > 70] = matrix[matrix > 70]

plt.figure()
plt.title("Masking (Values > 70)")
plt.imshow(masked, cmap="hot")
plt.colorbar()
plt.show()

# --------------------------------------------------
# 7. Heatmap Visualization
# --------------------------------------------------
plt.figure()
plt.title("Heatmap Representation")
plt.imshow(matrix, cmap="jet")
plt.colorbar()
plt.show()
