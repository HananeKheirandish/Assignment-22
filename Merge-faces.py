import cv2
import numpy as np

img1 = cv2.imread('hw2/Amir.jpg', 0)
img4 = cv2.imread('hw2/Parsa.jpg', 0)

img1 = cv2.resize(img1, (500, 500))
img4 = cv2.resize(img4, (500, 500))
r, c = img1.shape

img2 = img1//2 + img4//4
img3 = img1//4 + img4//2

result = np.zeros((r, c*4), np.uint8)
result[0:r, 0:c] = img1
result[0:r, c:c*2] = img2
result[0:r, c*2:c*3] = img3
result[0:r, c*3:c*4] = img4

cv2.imshow('output', result)
cv2.imwrite('putput5.jpg', result)

cv2.waitKey()