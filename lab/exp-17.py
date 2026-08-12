import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("ex8.jpg", 0)

# Check if image was loaded
if img is None:
    print("Error: Image not found")
    exit()

# Apply Sobel edge detection along X-axis
sobel_x = cv2.Sobel(
    img,
    cv2.CV_8U,
    1,
    0,
    ksize=5
)

# Save result
cv2.imwrite("sobel_x.jpg", sobel_x)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X Edges", sobel_x)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()