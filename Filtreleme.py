
from cv2 import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (True):
    ret, bilgisayarKamerasi = kamera.read()

    hsv = cv2.cvtColor(bilgisayarKamerasi, cv2.COLOR_BGR2HSV)

    baslangic_altMavi = np.array([100, 60, 60])
    bitis_ustMavi = np.array([140, 255, 255])

    maskeleme = cv2.inRange(hsv, baslangic_altMavi, bitis_ustMavi)
    filtreli_goruntu = cv2.bitwise_and(
        bilgisayarKamerasi, bilgisayarKamerasi, mask=maskeleme)

    cv2.imshow('Orjinal Goruntu (Bilgisayar Kamerasi)', bilgisayarKamerasi)
    cv2.imshow('Maskeli Goruntu (Bilgisayar Kamerasi)', maskeleme)
    cv2.imshow('Filtrenlemis Goruntu (Bilgisayar Kamerasi)', filtreli_goruntu)

    if cv2.waitKey(2) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()
