import cv2
import numpy as np

img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\coins.jpg")
# resimler okundu

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# gri formata donusturuldu

img_blur2 = cv2.medianBlur(gray2, 5)
# resimler yumusatildi

circles = cv2.HoughCircles(img_blur2, cv2.HOUGH_GRADIENT, 1, img2.shape[0] / 4,
                           param1=200, param2=10, minRadius=20, maxRadius=80)  # hough algoritmasi ile daireler bulundu
# par1 giris resmi (gri tonlamalı)
# par2 algılama yöntemidir
# par3 cozunurlugun ters oranı
# par4 algilanan merkezler arasindaki minimum mesafe
# par5 dahili Canny kenar algılayıcısı için üst eşik
# par6 merkez algilama esigi
# par7 algilanacak minimum yaricap
# par8 algılanacak maksimum yaricap

if circles is not None:
    circles = np.uint16(np.around(circles))  # circle degerleri around ile yuvarlanir ve tekrar degiskene atanir
    for i in circles[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)

cv2.imshow("images", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
