import cv2
import numpy as np


def nothing(x):  # opencv trackbar olusturmasi icin bos fonksiyon tanimlandi
    pass


img = np.zeros((512, 512, 3), dtype=np.uint8)  # tuval olusturuldu
cv2.namedWindow("trackbar")  # olusturulan traackbarlarin eklenmesi icin pencere olusturuldu

cv2.createTrackbar("R", "trackbar", 0, 255, nothing)  # trackbar olusturuldu par1 isim verdi par2 tuvale ekledi
# par3 trackbar baslangic degeri aldi, par4 trackbar bitis degerini aldi, par5 fonskiyon calismasi icin bos fonk eklendi
cv2.createTrackbar("G", "trackbar", 0, 255, nothing)
cv2.createTrackbar("B", "trackbar", 0, 255, nothing)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch, "trackbar", 0, 1, nothing)

while True:  # trackardaki degerlerin anlik olarak yansitilmasi icin dongu olusturuldu
    cv2.imshow("trackbar", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "trackbar")  # trackbarin pozisyon degerleri alindi
    g = cv2.getTrackbarPos("G", "trackbar")
    b = cv2.getTrackbarPos("B", "trackbar")
    s = cv2.getTrackbarPos(switch, "trackbar")

    if s == 0:  # eger deger 0 ise ciktinin siyah olmasi saglandi
        img[:] = [0, 0, 0]
    else:  # diger durumda ise ciktinin trackbardaki anlik degerler olmasi saglandi
        img[:] = [b, g, r]

cv2.destroyAllWindows()
