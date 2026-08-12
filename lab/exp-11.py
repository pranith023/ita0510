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

# Affine transformation matrix
M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# Apply affine transformation
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Save transformed image
cv2.imwrite("Affine_Transformed.jpg", affine_img)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()