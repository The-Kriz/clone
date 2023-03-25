import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Read a frame from the camera
ret, frame = cap.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Could not read frame from camera")
    exit()

# Display the frame
cv2.imshow("Frame", frame)

# Wait for a key press
cv2.waitKey(0)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
