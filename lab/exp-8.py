import cv2

# Read image
img = cv2.imread("ex8.jpg")

# Check if image exists
if img is None:
    print("Error: Image not found")
    exit()

# Resize image
big = cv2.resize(img, None, fx=2, fy=2)
small = cv2.resize(img, None, fx=0.5, fy=0.5)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Bigger", big)
cv2.imshow("Smaller", small)

# Press 1 to exit
while True:
    if cv2.waitKey(0) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()