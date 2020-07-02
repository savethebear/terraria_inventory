import cv2
import numpy as np

import sys
import os
from helper import *

image = cv2.imread("test_images/inventory_test.png")
print("image dim: {}".format(image.shape))

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Thresholding
lower_bound = 50
upper_bound = 255
_, threshold = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
print("Number of Contours found = " + str(len(contours)))

items = []
for contour in contours:
    # crop image
    bounding_box = contour_bounding_box(contour)
    patch = image[bounding_box[0]:bounding_box[1], bounding_box[2]:bounding_box[3]]

    # check if height and width within range
    target = 59
    pixel_range = 20
    dim = patch.shape
    if (abs(dim[0] - target) <= pixel_range) and (abs(dim[1] - target) <= pixel_range):
        items.append(Item(bounding_box, patch))

if len(items) != 40:
    print("Inventory extraction error...")
    sys.exit(1)

