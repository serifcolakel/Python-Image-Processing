import cv2
import numpy as np

img = cv2.imread("Data/Lena.jpg")
img1 = cv2.imread("Data/cards.jpg")

imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img1, img1))

cv2.imshow("Horizontal", imgHorizontal)
cv2.imshow("Vertical", imgVertical)

cv2.waitKey(0)
