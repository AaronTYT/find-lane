import cv2

image = cv2.imread('road.png')
cv2.imshow("result", image)
cv2.waitKey(0)