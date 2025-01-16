import cv2  # Importing OpenCV for image processing.

# Read the image file 'city_hall.jpg' in color mode (flag value 3 is equivalent to cv2.IMREAD_COLOR).
img = cv2.imread('city_hall.jpg', 3)

# Create a named window with adjustable size using cv2.WINDOW_NORMAL.
cv2.namedWindow('image_name', cv2.WINDOW_NORMAL)

# Display the loaded image in the created window named 'image_name'.
cv2.imshow('image_name', img)

# Wait indefinitely until a key is pressed.
cv2.waitKey(0)

# Destroy all OpenCV windows to free up resources.
cv2.destroyAllWindows()
