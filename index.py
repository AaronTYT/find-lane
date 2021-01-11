import cv2
import numpy as np

image = cv2.imread('road.png')
lane_image = np.copy(image)

#convert rgb to gray scale.
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

#reduce noise by applying GaussianBlur to detect proper edges/lines
blur = cv2.GaussianBlur(gray, (5,5),0)

#Find sharp gradient changes within the picture in the range of 50-150.
canny = cv2.Canny(blur, 50, 150)
cv2.imshow("result", canny)
cv2.waitKey(0)