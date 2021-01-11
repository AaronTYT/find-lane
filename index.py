import cv2
import numpy as np

image = cv2.imread('road.png')
lane_image = np.copy(image)

#convert rgb to gray scale.
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

cv2.imshow("result", gray)
cv2.waitKey(0)