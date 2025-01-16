import argparse
import numpy as np
import cv2
from skimage.exposure import rescale_intensity

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (roi * kernel).sum()
            output[y - pad, x - pad] = k
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    return output


# Argument parsing to get the image path, defaults to a hardcoded path
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="city_hall.jpg", help="path to input image")
ap.add_argument("-k", "--kernel", default="laplacian", help="kernel to use: laplacian, sobelX, sobelY")
args = vars(ap.parse_args())

# Command the can run scrypt: python ex_nr_3.py --image city_hall.jpg --kernel laplacian
# New command: python ex_nr_3.py --image friends.jpg --kernel laplacian

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

image_path = args["image"]
kernel_name = args["kernel"]
image = cv2.imread(image_path)
kernel = kernels[kernel_name]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
convoleOutput = convolve(gray, kernel)
opencvOutput = cv2.filter2D(gray, -1, kernel)
cv2.imshow("original", gray)
cv2.imshow("{} - convolve".format(kernel_name), convoleOutput)
cv2.imshow("{} - opencv".format(kernel_name), opencvOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()