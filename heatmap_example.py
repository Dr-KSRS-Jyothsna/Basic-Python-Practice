"""
File: heatmap_example.py
Author: Dr. K. S. R. S. Jyothsna
Description:
This program demonstrates how to create a heat map using Matplotlib.
A heat map represents data values using colors.
"""

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# Create sample data (2D matrix)
# --------------------------------------------------
data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 60, 30],
    [20, 40, 60, 80]
])

# --------------------------------------------------
# Display heat map
# --------------------------------------------------
plt.figure()
plt.title("Simple Heat Map")
plt.imshow(data, cmap="hot")
plt.colorbar()   # shows value scale
plt.show()
