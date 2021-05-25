from cv2 import cv2
cap = cv2.VideoCapture(0)
# .set fonksiyonu kameradan elde edilen
# görüntünün değerleri x ve y olarak ayarlanır
# .set(10, 100) ile isede parlaklık ayarlanır
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
for i in range(10):
    print(i)
faceCascade = cv2.CascadeClassifier("Data/haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale()
while (True):
    success, img = cap.read()
    cv2.imshow("Video", img)
    faces = faceCascade(img, )
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
