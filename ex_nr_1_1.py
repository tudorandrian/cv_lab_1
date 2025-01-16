import cv2  # Importing OpenCV library for image processing.

# Reading the image file 'city_hall.jpg' in color mode (flag value 3 is equivalent to cv2.IMREAD_COLOR).
img = cv2.imread('city_hall.jpg', 3)

# Displaying the image in a window named 'image_name'.
cv2.imshow('image_name', img)

# Wait indefinitely until a key is pressed.
cv2.waitKey(0)

# Close all OpenCV windows.
cv2.destroyAllWindows()