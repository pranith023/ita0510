import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("ex8.jpg", 0)

# Check if image was loaded
if img is None:
    print("Error: Image not found")
    exit()

# Sobel along X-axis
sobelx = cv2.Sobel(
    img,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

# Sobel along Y-axis
sobely = cv2.Sobel(
    img,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

# Combine X and Y edges
edges = cv2.addWeighted(
    sobelx,
    0.5,
    sobely,
    0.5,
    0
)

# Convert to 8-bit image before saving/displaying
edges = cv2.convertScaleAbs(edges)

# Save result
cv2.imwrite("Edge_detection.jpg", edges)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY Edge Detection", edges)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()