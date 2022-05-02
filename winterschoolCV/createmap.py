import random
import cv2
import numpy as np

pic = np.full((20, 20), 255, np.uint8)

for i in range(20):
    for j in range(20):
        if random.random()<0.3:
            pic[i][j] = 0
pic = cv2.resize(pic, (200, 200))

for i in range(200):
    for j in range(200):
        if pic[i][j] > 128:
            pic[i][j] = 255
        else: pic[i][j] = 0

for i in range(7):
    for j in range(7):
        pic[5-i][5-j] = 255
        pic[185-i][185-j] = 255
        pic[5-i][8+j] = 255
        pic[185-i][188+j] = 255
        pic[8+i][8+j] = 255
        pic[188+i][188+j] = 255
        pic[8+i][5-j] = 255
        pic[188+i][185-j] = 255

for i in range(2):
    for j in range(2):
        pic[5+i][5+j] = 128
        pic[185+i][185+j] = 128

cv2.imwrite("winterschoolCV\pic.png", pic)
cv2.imshow("pic.png", pic)
cv2.waitKey(0)