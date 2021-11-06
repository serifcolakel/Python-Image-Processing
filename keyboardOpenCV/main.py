import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


class Button():
    def __init__(self, pos, text, size=[90, 90]):
        self.pos = pos
        self.size = size
        self.text = text


finalText = ""

keyboard = Controller()

#Track Hand
detector = HandDetector(detectionCon=0.8)
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "I", "O", "P"],
    ["A", " S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "X", "C", "V", "B", "N", "M", "/", "."],
    ["https://github.com/serifcolakel"]
    ]

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 10  , 100 * i + 200 ], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    #hand check
    if lmlist:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            #bas parmak ucu indexi
            if x<lmlist[5][0]<x+w and y<lmlist[5][1]<y+h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                #isaret ve orta parmak indexleri mesafesi hesaplanacak ve l ye yazılacak.
                l, _, _ = detector.findDistance(5, 8, img, draw=False)
                #print(l)
                #distance kucuk 30 ise tıklandıgında
                if l<30:
                    keyboard.press(button.text)#button.text'e basacak
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    finalText += button.text
                    sleep(3)

    cv2.rectangle(img, (10, 1), (1280, 31), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, "Text : "+finalText, (60, 26), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    cv2.rectangle(img, (10, 690), (1280, 720), (255, 255, 0), cv2.FILLED)
    cv2.putText(img, "KAPATMAK ICIN Q YA BAS", (60, 715), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()