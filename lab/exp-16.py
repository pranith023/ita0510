import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("ex8.jpg", 0)

# Check if image was loaded
if img is None:
    print("Error: Image not found")
    exit()

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Save edge image
cv2.imwrite("Edges.jpg", edges)

# Display original and edges
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", edges)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()