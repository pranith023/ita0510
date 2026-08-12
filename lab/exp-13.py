import cv2
import numpy as np

# Define the points from the original video
roi_points = np.array([
    (150, 200),
    (450, 200),
    (550, 500),
    (50, 500)
])

# Define the destination points
target_points = np.array([
    (0, 0),
    (400, 0),
    (400, 600),
    (0, 600)
])

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(
    roi_points.astype(np.float32),
    target_points.astype(np.float32)
)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply perspective transformation
    dst = cv2.warpPerspective(frame, M, (400, 600))

    # Display original and transformed video
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Transformed Frame", dst)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()