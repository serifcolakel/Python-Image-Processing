from cv2 import cv2

print("Package Imported")

img = cv2.imread("Data/Lena.jpg")


cv2.imshow("Lena.jpg", img)
cv2.waitKey(0)  # 0 ile ekranda tutabiliriz
