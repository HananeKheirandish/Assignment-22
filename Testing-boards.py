import cv2

img_board_origin = cv2.imread('hw2/board - origin.bmp', 0)
img_board_test = cv2.imread('hw2/board - test.bmp', 0)
img_board_test = cv2.flip(img_board_test, 1)

result = cv2.subtract(img_board_origin, img_board_test)
result = result * 100

cv2.imshow('output', result)
cv2.imwrite('output3.jpg', result)

cv2.waitKey()