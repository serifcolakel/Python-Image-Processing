import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Justi\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("download.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))

#Detecting Chars
hImg, wImg, _ = img.shape
print("hey", _)
y1 = 0
x1 = 0
h1 = 140
w1 = wImg
crop = img[y1:y1+h1, x1:x1+w1]

boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(crop, (x, hImg-y), (w, hImg-h), (0, 255, 255), 1)
    cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255),1)

cv2.imshow("result", crop)
cv2.waitKey(0)





