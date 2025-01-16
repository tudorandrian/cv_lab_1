import cv2

# Load the image in color mode.
img = cv2.imread('city_hall.jpg', 3)

# Convert the image to grayscale.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image.
cv2.imwrite('img_gray.jpg', img_gray)
