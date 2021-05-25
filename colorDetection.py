import cv2
import numpy as np


def empty():
    pass


path = "Data/lambo.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, s_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_or(img, img, mask=mask)
    imgR = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Last", imgResult)
    cv2.imshow("Last_2", imgR)
    cv2.imshow("AA", mask)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
