import cv2
import numpy as np
import sys
from os.path import exists

img_rgb = ""

rc = []

def searchImage(item, img, threshold, itemCategory):
    """
    Search an image in the screen and return the rectangle
    :param item: item path
    :param img: screen path
    :threshold: threshold for the item, if None in db, use the default value
    :itemCategory: item category (Quest = 0, Hideout = 1)
    """
    
    if itemCategory == 0:
        color = (0, 0, 255) # red
    elif itemCategory == 1:
        color = (0, 255, 0) # green
    else:
        color = (0, 0, 255)


    if threshold == None:
        threshold = .65
    else:
        threshold =threshold *0.01

    if exists(item) is False:
        print("{} not found".format(item))
        return

    template = cv2.imread(item)

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    # threshold = .65
    loc = np.where(res >= threshold)

    trows,tcols = template.shape[:2]


    for pt in zip(*loc[::-1]):
        rc.append([img_rgb, pt, (pt[0] + tcols, pt[1] + trows), color, 2])
        # cv2.rectangle(img_rgb, pt, (pt[0] + tcols, pt[1] + trows), (0, 0, 255), 2)

    print(item, len(loc[0]))


