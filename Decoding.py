import cv2

img1 = cv2.imread('hw2/a.tif', 0)
img2 = cv2.imread('hw2/b.tif', 0)

result = cv2.subtract(img2, img1)

cv2.imshow('output', result)
cv2.imwrite('output1.jpg', result)

cv2.waitKey()