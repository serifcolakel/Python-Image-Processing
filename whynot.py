from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    ret, cam = cap.read()

    hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)

    baslangic_altMavi = np.array([100, 60, 60])
    bitis_ustMavi = np.array([140, 255, 255])

    maskeleme = cv2.inRange(hsv, baslangic_altMavi, bitis_ustMavi)
    filtreli_goruntu = cv2.bitwise_and(
        cam, cam, mask=maskeleme)

    gezici_cekirdek = np.ones((10, 10), np.float32) / 100  # No-1

    cv2.imshow('Orjinal Goruntu (Bilgisayar Kamerasi)', cam)
    cv2.imshow('Maskeli Goruntu (Bilgisayar Kamerasi)', maskeleme)
    cv2.imshow('Filtrenlemis Goruntu (Bilgisayar Kamerasi)', filtreli_goruntu)

    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
