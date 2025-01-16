import numpy as np  # Import NumPy for numerical operations.
import cv2  # Import OpenCV for image processing.
from matplotlib import pyplot as plt  # Import Matplotlib for plotting.

# Load the image 'city_hall.jpg' in color mode (flag=3).
img = cv2.imread('city_hall.jpg', 3)

# Draw a green rectangle on the image. Top-left corner at (384, 0), bottom-right at (510, 128).
# The rectangle has a thickness of 3 pixels.
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a blue diagonal line from the top-left corner (0, 0) to the bottom-right (511, 511).
# The line has a thickness of 5 pixels.
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a filled red circle with center at (447, 63) and a radius of 63 pixels.
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Write text "OpenCV" on the image at position (10, 500) using the specified font.
# The text is white, has a font scale of 4, thickness of 2, and uses antialiasing.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# Display the modified image using Matplotlib with gray colormap and bicubic interpolation.
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # Hide X and Y axis tick values.
plt.show()

# Create a blank image with dimensions 512x512 and 3 color channels (initialized to black).
img2 = np.zeros((512, 512, 3), np.uint8)

# Get the dimensions of the original image.
height, width, channels = img.shape

# Fill the left half of the blank image with blue (BGR: 255, 0, 0).
img2[:, 0:int(0.5 * width)] = (255, 0, 0)

# Fill the right half of the blank image with green (BGR: 0, 255, 0).
img2[:, int(0.5 * width):width] = (0, 255, 0)

# Display the newly created blank image with two color regions.
plt.imshow(img2)
plt.xticks([]), plt.yticks([])  # Hide X and Y axis tick values.
plt.show()

# Calculate the histogram of pixel intensities for the original image, considering the 0th channel (blue).
# No mask is applied, with 256 bins and an intensity range of [0, 256].
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Display the histogram of pixel intensities using Matplotlib.
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
