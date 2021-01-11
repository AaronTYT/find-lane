import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    #convert rgb to gray scale.
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

    #reduce noise by applying GaussianBlur to detect proper edges/lines
    blur = cv2.GaussianBlur(gray, (5,5),0)

    #Find sharp gradient changes within the picture in the range of 50-150.
    canny = cv2.Canny(blur, 50, 150)
    return canny

image = cv2.imread('road.png')
lane_image = np.copy(image)
canny = canny(lane_image)

#show the image from matplotlib library file.
plt.imshow(canny)
plt.show()