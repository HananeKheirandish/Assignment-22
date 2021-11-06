import cv2

img = cv2.imread('hw2/Mona_Lisa.jpg', 0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted, (21,21), 0)
inverted_blurred = 255 - blurred

sketch = img / inverted_blurred
sketch = sketch * 255

cv2.imwrite('output6.jpg', sketch)