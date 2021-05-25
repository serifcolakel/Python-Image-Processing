import cv2

cap = cv2.VideoCapture(0)
# Kayıt yeri
filename = "Data\webcam.avi"
# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
codec = cv2.VideoWriter.fourcc("W", "M", "V", "2")
framerate = 30
resolution = (640, 480)

videoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, -1)#Videoyu ters alıcak
    cv2.imshow("Webcam", frame)
    videoFileOutput.write(frame)
    if cv2.waitKey(1) % 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()