import cv2
import numpy as np

import sys

def pixel_to_string(pixel):
    return str(pixel[0]) + "," + str(pixel[1]) + "," + str(pixel[2])

image = cv2.imread("inventory_test.png")

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Thresholding
lower_bound = 50
upper_bound = 255
_, threshold = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
print("Number of Contours found = " + str(len(contours)))

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
cv2.imshow('Contours', image) 
cv2.waitKey(0)
cv2.destroyAllWindows() 