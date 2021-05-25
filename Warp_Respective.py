import cv2
import numpy as np

img = cv2.imread("Data/cardss.jpg")
width, height = 250, 350
pts1 = np.float32([[50, 100], [200, 190], [100, 300], [500, 300]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Cards", img)
cv2.imshow("Last", imgOut)
cv2.waitKey(0)
