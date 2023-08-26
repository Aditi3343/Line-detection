import cv2
import numpy as np

image = cv2.imread('Road.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

line_image = image.copy()
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('lines_detected.jpg', line_image)
cv2.imshow('Original Image', image)
cv2.imshow('Detection', line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
