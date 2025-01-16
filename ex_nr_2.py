import cv2  # Import OpenCV for video and image processing.

# Initialize the video capture object to access the default camera (device index 0).
cap = cv2.VideoCapture(0)

while True:
    # Capture each frame from the camera.
    ret, frame = cap.read()

    # Convert the captured frame from BGR (default OpenCV color format) to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale frame in a window named 'frame'.
    cv2.imshow('frame', gray)

    # Break the loop if the 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object to free up resources.
cap.release()

# Close all OpenCV windows.
cv2.destroyAllWindows()
