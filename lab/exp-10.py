import cv2

# Read image
image = cv2.imread("ex8.jpg")

# Check if image was loaded
if image is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
width = image.shape[1]
height = image.shape[0]

print("Width:", width)
print("Height:", height)

# Create window
cv2.namedWindow("Original Image")

# Move window to position (100, 100)
cv2.moveWindow("Original Image", 100, 100)

# Display image
cv2.imshow("Original Image", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()