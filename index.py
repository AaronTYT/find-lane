import cv2
import numpy as np
import matplotlib.pyplot as plt

def averaged_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.ployfit((x1, x2),(y1, y2),1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit,axis=0)

def canny(image):
    #convert rgb to gray scale.
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    #reduce noise by applying GaussianBlur to detect proper edges/lines
    blur = cv2.GaussianBlur(gray, (5,5),0)

    #Find sharp gradient changes within the picture in the range of 50-150.
    canny = cv2.Canny(blur, 50, 150)
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255,0,0), 10)
    return line_image

def region_of_interest(image):
    height = image.shape[0]
    triangle = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

image = cv2.imread('road.png')
lane_image = np.copy(image)
canny = canny(lane_image)
cropped_image = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100,  np.array([]), minLineLength=40, maxLineGap=5)
averaged_lines = averaged_slope_intercept(lane_image, lines)
line_image = display_lines(lane_image, lines)   
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
cv2.imshow("result", combo_image)
cv2.waitKey(0)