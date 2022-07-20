import cv2
import numpy as np
import sys
from os.path import exists


template = cv2.imread('./questItem/peacekeeper/propane.png')

img_rgb = cv2.imread("C:/Users/mohamed/Desktop/projet_perso/tarkovSorter/img/scav1.png")
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .70

loc = np.where(res >= threshold)
# print(len(loc[0]))
trows,tcols = template.shape[:2]

distinctImage = loc[::-1]
print(distinctImage)

for pt in zip(*loc[::-1]):
    # print(pt)
    pass
    # cv2.rectangle(img_rgb, pt, (pt[0] + tcols, pt[1] + trows), (0, 0, 255), 2)

# cv2.imwrite('dump/result.png', img_rgb)
# cv2.waitKey()

