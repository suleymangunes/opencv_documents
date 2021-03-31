import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")
img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")

cv2.circle(img2, (300, 300), 100, (0, 0, 255), -1)
diff = cv2.subtract(img, img2)  # subtract iki resmi karsilastirir, ayni olan kisimlari siyaha boyar farkli olan
# olan kisimlari oldugu gibi gosterir
diff = cv2.cvtColor(diff, cv2.COLOR_BGRA2GRAY)  # farkli olan kisimlarin koordinatalarini bulmak icin renk kodu degisti
_, diff = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)  # esik degeri ile farkli kisimlar beyaz olmasi saglandi
contours, ret = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # degerlerin konturleri bulundu

x = contours[0][0][0][0]  # bulunan kontorde ilk pikselin degerinin koordinatlari degiskenlere atandi
y = contours[0][0][0][1]  # yazi yazilmasi icin
cv2.drawContours(img2, contours, 0, (0, 255, 0), 2)  # kontorler cizildi
cv2.putText(img2, "fark 1", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)  # dortgeinin sol ust kosesine yazildi

(x, y, w, h) = cv2.boundingRect(contours[0])  # fonksiyon ile bulunan fark alanini kaplayacak dikdortgenin sol ust
# kosenin koordinati ve dikdortgenin genisligi, yuksekligi bulundu, degiskenlere atandi
cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 4)  # fonksiyon degerleri ile konturu saracak dortgen cizildi

rect = cv2.minAreaRect(contours[0])  # kontoru sinirlayacak minimum alan bulundu dondurdugu degerlerin ilki
# merkez (x, y) koordinatini gosterir, iknici (genişlik, yükseklik), ucuncu dönüş acisini gosterir
box = cv2.boxPoints(rect)  # fonksiyon ile dortgenin 4 kosesi 2 boyutlu liste icinde tutuldu
box = np.int0(box)  # dortgenin cizilmesi icin degerler integere cevrildi
cv2.drawContours(img2, [box], 0, (100, 150, 255), 2)  # kontur cizimi ile kutunun etrafi cizildi
# fark konturunun saran en kucuk dikdortgen cizilmis oldu


(xd, yd), r = cv2.minEnclosingCircle (contours[0])  # konturun etrafini saran minimum cemberin koordinatlari integere
merkez = (int(xd), int(yd))  # cevrilerek merkez degiskenine atandi
r = int(r)  # yaricap degeri icin de ayni islem tekrarlandi
cv2.circle(img2, merkez, r, (150,10,200), 1)  # kontorun etrafini saran minimum cember cizildi

elips = cv2.fitEllipse(contours[0])  # kontorun etrafini saracak minimum elips cizildi
cv2.ellipse(img, elips, (50,50,100), 5)

rows,cols = img.shape[:2]  # en uzun taraftan ekran noyu gecen cizgi cizildi
[vx,vy,x,y] = cv2.fitLine(contours[0], cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(img, (cols - 1, righty), (0 , lefty), (0, 255, 0), 2)

cv2.imshow("diff", diff)
cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
