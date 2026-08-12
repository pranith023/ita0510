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
    [0, int(0.7 * rows)],
    [cols - 1, int(0.7 * rows)]
])

# Find Homography matrix
M, _ = cv2.findHomography(src_points, dst_points)

# Apply Homography transformation
homography_img = cv2.warpPerspective(
    img,
    M,
    (cols, rows)
)

# Save transformed image
cv2.imwrite(
    "transformation_using_Homography_Image.jpg",
    homography_img
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_img)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()