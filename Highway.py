import cv2
import numpy as np

images = []
for i in range(15):
    img = cv2.imread(f'hw2/highway/h{i}.jpg', 0)
    images.append(img)
    row, col = img.shape

results = np.zeros((row, col), np.uint8)
for image in images:
    results += image // 15

cv2.imshow('ourput', results)
cv2.imwrite('output4.jpg', results)

cv2.waitKey()