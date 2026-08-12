import cv2
import numpy as np

# Read image
img = cv2.imread("ex8.jpg")

# Check if image was loaded
if img is None:
    print("Error: Image not found")
    exit()

# Laplacian mask with negative center coefficient
kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# Apply Laplacian mask
sharpened = cv2.filter2D(img, -1, kernel)

# Save sharpened image
cv2.imwrite("Sharpened_Image.jpg", sharpened)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()