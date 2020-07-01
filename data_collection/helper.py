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

def crop_image(image, bounding_box):

    pass

class Item:
    def __init__(self, bounding_box, patch):
        self.min_x = bounding_box[0]
        self.max_x = bounding_box[1]
        self.min_y = bounding_box[2]
        self.max_y = bounding_box[3]
        self.patch = patch
