import cv2

img = cv2.imread("ex8.jpg")

if img is None:
    print("Error: Image not found")
    exit()

# Rotate clockwise
rotated_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate counterclockwise
rotated_counterclockwise = cv2.rotate(
    img,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)

cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", rotated_clockwise)
cv2.imshow("Counterclockwise Rotation", rotated_counterclockwise)

cv2.imwrite("rotated_clockwise.jpg", rotated_clockwise)
cv2.imwrite("rotated_counterclockwise.jpg", rotated_counterclockwise)

# Press 1 to close
while True:
    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cv2.destroyAllWindows()