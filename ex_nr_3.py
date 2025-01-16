import argparse
import numpy as np
import cv2
from skimage.exposure import rescale_intensity


# Function to apply convolution using a given kernel
def convolve(image, kernel):
    # Get image dimensions
    (iH, iW) = image.shape[:2]
    # Get kernel dimensions
    (kH, kW) = kernel.shape[:2]
    # Compute padding size (assuming kernel width is odd)
    pad = (kW - 1) // 2
    # Add padding to the image to handle edge cases
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    # Initialize output image with zeros
    output = np.zeros((iH, iW), dtype="float32")

    # Loop over each pixel in the input image
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # Extract region of interest (ROI) centered at the current pixel
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            # Perform element-wise multiplication and sum
            k = (roi * kernel).sum()
            # Assign the result to the corresponding pixel in the output image
            output[y - pad, x - pad] = k

    # Rescale intensity to ensure pixel values fall within the expected range
    output = rescale_intensity(output, in_range=(0, 255))
    # Convert output image to unsigned 8-bit integer format
    output = (output * 255).astype("uint8")
    return output


# Parse command-line arguments to get the image path and kernel type
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="portrait_dog.jpg", help="path to input image")
ap.add_argument("-k", "--kernel", default="laplacian", help="kernel to use: laplacian, sobelX, sobelY")
args = vars(ap.parse_args())

# Define a dictionary of kernels for convolution
kernels = {
    "laplacian": np.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int"),
    "sobelX": np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int"),
    "sobelY": np.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")
}

# Read the input image and kernel from the parsed arguments
image_path = args["image"]
kernel_name = args["kernel"]
image = cv2.imread(image_path)
# Retrieve the selected kernel from the dictionary
kernel = kernels[kernel_name]
# Convert the input image to grayscale for processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply custom convolution
convoleOutput = convolve(gray, kernel)
# Apply OpenCV's built-in convolution for comparison
opencvOutput = cv2.filter2D(gray, -1, kernel)
# Display the original grayscale image
cv2.imshow("original", gray)
# Display the output of the custom convolution function
cv2.imshow("{} - convolve".format(kernel_name), convoleOutput)
# Display the output of OpenCV's convolution function
cv2.imshow("{} - opencv".format(kernel_name), opencvOutput)
# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Command the can run scrypt: python ex_nr_3.py --image city_hall.jpg --kernel laplacian
# New command: python ex_nr_3.py --image friends.jpg --kernel laplacian