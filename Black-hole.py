import cv2
import numpy as np

img = [[0 for i in range(5)]for j in range(4)]
for i in range(4):
    for j in range(5):
        img[i][j] = cv2.imread(f'hw2/black hole/{i+1}/{j+1}.jpg', 0)
        row, col = img[i][j].shape

img_without_noise = [0 for i in range(4)]
for i in range(4):
    for j in range(5):
        img_without_noise[i] += img[i][j]//5

result = np.zeros((row*2 , col*2), dtype= np.uint8)
result[0:row, 0:col] = img_without_noise[0]
result[0:row, col:col*2] = img_without_noise[1]
result[row:row*2, 0:col] = img_without_noise[2]
result[row:row*2, col:col*2] = img_without_noise[3]

cv2.imshow('output', result)
cv2.imwrite('output2.jpg', result)

cv2.waitKey()