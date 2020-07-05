import cv2

import sys


def contour_bounding_box(contour):
    max_x = -1
    max_y = -1
    min_x = sys.maxsize 
    min_y = sys.maxsize

    for point in contour:
        coords = point[0]
        if coords[0] < min_y:
            min_y = coords[0]
        if coords[0] > max_y:
            max_y = coords[0]
        if coords[1] < min_x:
            min_x = coords[1]
        if coords[1] > max_x:
            max_x = coords[1]

    return (min_x, max_x, min_y, max_y)


def show_contours(image, contours):
    # -1 signifies drawing all contours 
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('Contours', image)
    cv2.waitKey(0)


def reduce_background_noise(image, redness_target, error):
    # r = 90 - 100
    # gb = 45 - 55
    pass

def ssd(image_a, image_b):
    if (image_a.shape != image_b.shape):
        print("resize needed...")
        return
    
    return numpy.sum((image_a[:, :, 0:3]-image_b[:, :, 0:3])**2)


def compare_icons(image, icons):
    smallest_score = sys.maxsize
    icon_index = -1
    for i in range(len(icons)):
        score = ssd(image, icons[i])
        smallest_score = score if smallest_score > score else smallest_score
    
    return smallest_score, icon_index


class Item:
    def __init__(self, bounding_box, patch):
        self.min_x = bounding_box[0]
        self.max_x = bounding_box[1]
        self.min_y = bounding_box[2]
        self.max_y = bounding_box[3]
        self.patch = patch
