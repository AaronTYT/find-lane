import cv2
import numpy as np

image = cv2.imread('road.png')
lane_image = np.copy(image)

#convert rgb to gray scale.
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

#reduce noise by applying GaussianBlur to detect proper edges/lines
blur = cv2.GaussianBlur(gray, (5,5),0)

cv2.imshow("result", blur)
cv2.waitKey(0)