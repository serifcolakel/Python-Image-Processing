import cv2

# En boy oranınca resmi bozmadan gösterilecek
def resizewithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    dimension = None
    (h, w) = img.shape[:2]

    if width is not None and height is not None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w * r), height)
    else:
        r = width / float(w)
        dimension = (width, int(h * r))
    return cv2.resize(img, dimension, interpolation=inter)


img = cv2.imread("Data/lambo.jpg")
img1 = resizewithAspectRatio(img, width=None, height=100, inter=cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resize", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()