import numpy as np
import random

import cv2

img = cv2.imread('hw2/chess pieces.jpg', 0)

row, col = img.shape

for i in range(row):
    for j in range(col):
        noise = random.randint(0, row)
        if noise % (row//3)  == 0:
            if img[i, j] < 150:
                img[i, j] = 255
            else:
                img[i, j] = 0

cv2.imshow('output', img)
cv2.imwrite('output7.jpg', img)

cv2.waitKey()