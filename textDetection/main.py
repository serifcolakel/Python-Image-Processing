import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Justi\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("text.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
# #print(pytesseract.image_to_boxes(img))
hImg, wImg, _ = img.shape
# print("hey", _)
y1 = 0
x1 = 0
h1 = hImg
w1 = wImg
crop = img[y1:y1+h1, x1:x1+w1]
boxes = pytesseract.image_to_boxes(img)
# Harf Harf
# for b in boxes.splitlines():
#      #print(b)
#      b = b.split(' ')
#      print(b)
#      x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#      cv2.rectangle(crop, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)
#      cv2.putText(img, b[0], (x, hImg-y+12), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 255), 1)

#Kelime Kelime
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#           b = b.split()
#           #print(b)
#           if len(b) == 12:
#               x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#               cv2.rectangle(crop, (x, y), (w+x, h+y), (0, 255, 255), 1)
#               cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, .4, (0,255,255),1)
#
# Sadece Sayilar
# cong = r' --oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config=cong)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(crop, (x, y), (w+x, h+y), (0, 0, 255), 1)
#             cv2.putText(crop, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, .4, (0,0,255),1)


# Sayi Sayi
cong = r' --oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=cong)
for b in boxes.splitlines():
     #print(b)
     b = b.split(' ')
     print(b)
     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
     cv2.rectangle(crop, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)
     cv2.putText(img, b[0], (x, hImg-y+12), cv2.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 255), 1)


cv2.imshow("result", crop)
cv2.waitKey(0)





