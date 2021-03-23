import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\map.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3, 3))
_, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# gri mod\ bulaniklastirma\ esik degeri ile siyah beyaz\ kontur bulma

hull = []  # bulunan kontorlerin indislerini tutacak bos liste tanimlandi

for i in range(len(contours)):  # kontur sayisi kadar donen dongu tanimlandi
    hull.append(cv2.convexHull(contours[i], False))  # kontorun tum indis degerleri listeye eklendi,false indisi sagladi

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype=np.uint8)  # arka plan olusturuldu

for i in range(len(contours)):  # arka plana cizim yapilmasi icin dongu olusturuldu
    cv2.drawContours(bg, contours, i, (255, 0, 0), 3, 8, hierarchy)  # kontor degerleri cizildi
    # cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 8)  # dis bukey degerler cizildi

cv2.imshow("bg", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
