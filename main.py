import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt


# https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html

# On charge l'image.
img = cv2.imread("img/screen.png")
img2 = cv2.imread("img/screen.png",cv2.IMREAD_GRAYSCALE)

# On grise l'image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# on fait un threshold,
# gris, adaptatif  https://kongakura.fr/article/opencv-threshold
th = cv2.adaptiveThreshold(
    imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 71, 17)
cv2.imwrite('output/th.png', th)

# On recherche les contours.
contours, hierarchy = cv2.findContours(
    th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Draw contour
etst = cv2.drawContours(th, contours, -1, (0, 255, 0), 3)

# cv2.imshow("img",etst)
# cv2.waitKey(0)

