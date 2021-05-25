import cv2

url = "http://192.168.1.4:8080/video"
cam = cv2.VideoCapture(url)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("gor yok")
    cv2.imshow("gor", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()