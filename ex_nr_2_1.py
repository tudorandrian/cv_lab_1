import cv2

cap = cv2.VideoCapture(0)

# Use H.264 codec and MP4 format for better compatibility
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# Verify VideoCapture and VideoWriter initialization
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

if not out.isOpened():
    print("Error: VideoWriter failed to initialize")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)  # Flip frame vertically
        out.write(frame)  # Write the flipped frame to file
        cv2.imshow('frame', frame)  # Display the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
            break
    else:
        print("Error: Failed to read frame")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
