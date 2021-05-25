from cv2 import cv2
import numpy as np

img = cv2.imread("Data/Lena.jpg")

print(img.shape)
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])

imgResize = cv2.resize(img, (500, 250))
print(imgResize.shape)
print(imgResize.shape[0])
print(imgResize.shape[1])
print(imgResize.shape[2])

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
#cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
