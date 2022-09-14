import numpy as np
import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread('./img/screen.png')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

th = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,3)

_, ctrs, _ = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
im_h, im_w = img.shape
im_area = im_w * im_h
for ctr in ctrs:
    x, y, w, h = cv2.boundingRect(ctr)
    # Filter contours based on size
    if 0.01 * im_area < w * h < 0.1*im_area:
        cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)

plt.imshow(img_rgb, cmap='gray', vmin=0, vmax=255)