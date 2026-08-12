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
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Construct DLT matrix
A = []

for (x, y), (u, v) in zip(src_points, dst_points):
    A.append([
        -x, -y, -1, 0, 0, 0, x*u, y*u, u
    ])
    A.append([
        0, 0, 0, -x, -y, -1, x*v, y*v, v
    ])

A = np.array(A)

# Solve using Singular Value Decomposition (SVD)
_, _, Vt = np.linalg.svd(A)

# Homography matrix obtained using DLT
H = Vt[-1].reshape(3, 3)

# Normalize matrix
H = H / H[2, 2]

# Apply transformation
dlt_img = cv2.warpPerspective(img, H, (cols, rows))

# Save transformed image
cv2.imwrite("DLT_Transformed_Image.jpg", dlt_img)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", dlt_img)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()