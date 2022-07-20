import os
import sqlite3
import multipleImginImg as mii
import cv2
from datetime import datetime

con = sqlite3.connect('dbQuestItem.db')
cur = con.cursor()

lvl = 1

os.chdir(r"C:/Users/mohamed/Desktop/projet_perso/tarkovSorter")

mii.img_rgb = cv2.imread(
    "C:/Users/mohamed/Desktop/projet_perso/tarkovSorter/img/scav1.png")
    
'SELECT * FROM item WHERE vendeur = ?', ('*', )
for row in cur.execute('SELECT * FROM item'):
    # print("questItem/{}/{}.png".format(row[1], row[0]))
    mii.searchImage("./questItem/{}/{}.png".format(row[1], row[0]), None, row[6], 0)


for row in cur.execute('SELECT distinct(item), threshold FROM hideout'):
    # print("hideoutItem/{}.png".format(row[0]))
    # print("thershold",row[1])
    mii.searchImage("./hideoutItem/{}.png".format(row[0]), None, row[1],1)


for rectangle in mii.rc:
    cv2.rectangle(*rectangle)

# cv2.imshow('dump/result.png', mii.img_rgb)

cv2.imwrite('dump/{}.png'.format(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")), mii.img_rgb)
cv2.waitKey()
