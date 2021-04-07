import cv2  # opencv kutuphanesi ice aktarildi
import numpy as np  # numpy modulu ice aktarildi
import pytesseract  # yazilarin okunmasi icin tesseract modulu ice aktarildi
import imutils  # belirlenen degerleri bulmasi icin imutils kutuphanesi ice aktarildi

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\licence_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(gray, 6, 250, 250)
edged = cv2.Canny(filtered, 30, 200)
# resim gri formata donusturuldu, kenarlar belirlenip merkezi degerler uzerine bulaniklastirma yapildi (filtered)
# edge ile kenarlar bulundu

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# kontur degerleri bulundu (esik degerine gore kenarlar)
cnts = imutils.grab_contours(contours)  # imutils ile goruntudeki belirli bolgeler bulundu
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]  # bolgeler siralandi ve ilk 10 deger alindi
screen = None  # daha sonra kullanilmak uzere screen tanimlandi

for c in cnts:  # bulunan kontur degerleri icerisinde donuldu ve deneysel degerler ile plaka dortgeni bulundu
    epsilon = 0.018 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        screen = approx  # plakanin kose degerleri screene atandi
        break

mask = np.zeros(gray.shape, np.uint8)  # resim buyuklugunde tuval olusturuldu
new_img0 = cv2.drawContours(mask, [screen], 0, 255, -1)  # bulunan kontru bu resme cizildi ve ici dolduruldu
new_img = cv2.bitwise_and(img, img, mask=mask)  # ve operatoru ile resme aradaki farklara gore resim eklendi

(x, y) = np.where(mask == 255)  # np where ile mask uzerinde rengi beyaz olan kisimlar bulundu
(topx, topy) = (np.min(x), np.min(y))  # bu kisimlar degiskenlere atandi bu sayede sadece plakanın oldugu goruntu
(botx, boty) = (np.max(x), np.max(y))   # ayristirilmis oldu
cropped = gray[topx:botx+1, topy:boty+1]

text = pytesseract.image_to_string(cropped, lang="eng")  # tesseract ile resimdeki karakterler okunmus oldu
print(text)
cv2.imshow("img", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
