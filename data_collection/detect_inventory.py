import cv2
import numpy as np

import sys
import os
from os import listdir
from os.path import isfile, join
from helper import *

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
TEST_IMAGES_DIR = SCRIPT_DIR + "test_images/"
ITEM_ICONS_DIR = SCRIPT_DIR + "item_icons/"

image = cv2.imread(TEST_IMAGES_DIR + "item_test.png")
print("image dim: {}".format(image.shape))

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Thresholding
lower_bound = 60
upper_bound = 255
_, threshold = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
print("Number of Contours found = " + str(len(contours)))

# preprocess images
RED_RANGE = (50, 60)
BLUE_RANGE = (45, 55)
GREEN_RANGE = (45, 55)



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
        items.append(Item(bounding_box, cv2.resize(patch, (59, 59), interpolation=cv2.INTER_AREA)))

if len(items) != 40:
    print("Inventory extraction error...")
    sys.exit(1)


# load in ground truth icons
icon_files = [f for f in listdir(ITEM_ICONS_DIR) if isfile(join(ITEM_ICONS_DIR, f)) and str(f).endswith(".png")]
icon_images = [cv2.resize(cv2.imread(ITEM_ICONS_DIR + f), (59, 59), interpolation=cv2.INTER_AREA) for f in icon_files]

