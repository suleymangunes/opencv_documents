import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255  # beyaz tuval olusturuldu

cv2.line(canvas, (150, 150), (400, 400), (255, 255, 0), thickness=6)  # duz cizgi olusturuldu. par1 tuval
# par 2 baslangic, par3 bitis noktasi, par 4, renk par 5 kalinlik

cv2.rectangle(canvas, (50, 200), (150, 250), (255, 0, 255), thickness=-1)  # dikdortgen olusturuldu. par1 tuval
# par2 baslangic, par3 bitis noktasi, par4 renk, par5 kalinlik
cv2.rectangle(canvas, (200, 200), (350, 350), (255, 200, 255), 4)  # thickness yazilmasi zorunlu degildir

cv2.circle(canvas, (250, 100), 50, (0, 255, 255), thickness=-1)  # daire olusturuldu, par1 tuval, par2 merkez noktasi
# par3 yaricap uzunlugu, par4 renk, par5 daire olmasini saglayan yapidir. **(-1 daire, diger degerler cember olusturur)

p1 = (300, 50)  # ucgen ciziminin yapilmasi icin 3 nokta belirlendi
p2 = (450, 100)
p3 = (500, 250)
cv2.line(canvas, p1, p2, (0, 0, 0), 4)  # noktalar arasi cizgi cizildi
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p3, p1, (0, 0, 0), 5)

points = np.array([[[50, 400], [30, 500], [200, 480], [150, 350]]], np.int32)  # dortgen icin koordinatlar belirlendi
cv2.polylines(canvas, [points], True, (0, 255, 0), 5)  # coklu noktalar birlestirrilip dortgen olusturuldu
# par1 tuval, par2 noktalar, par3 seklin kapali olup olmasini belirler, par4 renk, par5 kalinlik

cv2.ellipse(canvas, (400, 450), (80, 40), 0, 0, 360, (255, 0, 255), -1)  # elips olusturuldu. par1 tuval,
# par2 merkez noktasi, par3 uzun ve kisa yaricap, par 4 merkezin acisi, par4 elipsin olusturulacagi kisim
# par5 renk, par6 kalinlik

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
