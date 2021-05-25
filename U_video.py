import cv2

# webcam ile

# 0 ile webcam 1 - 2 - 3 ise ayrı kamera ile alınabilir
# Ayrıca 0 yerine video adresi eklenerek de sabit video alınabilir
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("Data/move.mp4")

while True:
    ret, frame = cap.read()
    # cap okuduysa ret= true cap görüntü okumadıysa ret = False 'dir
    if ret == 0:
        break  # ret == false ise döngüyü kıracak
    frame = cv2.flip(frame, 2)
    cv2.imshow("webcam", frame)
    # waitkey ile 1ms de görüntü alıcak ve q tuşuna basıldığı anda döngüyü kıracak
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()  # görüntüyü sonladırıcaz
cv2.destroyAllWindows()