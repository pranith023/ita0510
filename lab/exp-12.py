import cv2
import numpy as np

# Read image
img = cv2.imread("ex8.jpg")

# Check if image was loaded
if img is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Source points
src_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

# Destination points
dst_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [int(0.33 * cols), rows - 1],
    [int(0.66 * cols), rows - 1]
])

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply perspective transformation
perspective_img = cv2.warpPerspective(
    img,
    M,
    (cols, rows)
)

# Save transformed image
cv2.imwrite(
    "Perspective_Transformed_Image.jpg",
    perspective_img
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective_img)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()