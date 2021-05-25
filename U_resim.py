import cv2

cv2.namedWindow("image")
img = cv2.imread(
    "Data/Lena.jpg", cv2.IMREAD_GRAYSCALE
)  # 2.parametre olarak 0 da yazılabilir

img2 = cv2.imread("Data/Lena.jpg")
# print(img2)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)  # açılacak resmi küçültüp büyütmeye yarar
img3 = cv2.resize(img2, (640, 480))  # yeniden boyutlandırma
cv2.imshow("image", img2)
cv2.imshow("image3", img3)
cv2.imwrite("Data/Lena1.jpg", img2)  # Resmi klonluyor
cv2.waitKey(0)  # 0 ile ekran da tutar normal de ms cinsinden
cv2.destroyAllWindows()