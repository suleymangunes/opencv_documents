import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\blur.jpg")
img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\median.jpg")
img3 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\bilateral.jpg")
r, c, hc = img.shape
r2, c2, hc2 = img2.shape
r3, c3, hc3 = img3.shape
img = cv2.resize(img, (int(c*2.5), int(r*2.5)))
img2 = cv2.resize(img2, (int(c2*2.5), int(r2*2.5)))
img3 = cv2.resize(img3, (int(c3*2.5), int(r3*2.5)))

blur = cv2.blur(img, (19, 19))  # etraftaki piksellerin ortalamasini alarak bulaniklastirir
# par2 deger 1 yatay renk karisimi deger 2 ise dikey renk karisimi yaparak bulaniklastirir

blur_gaussin = cv2.GaussianBlur(img, (19, 19), 0)  # gauss bulanigkligini giderilmesini saglar
# par2 deger 1 yatay renk karisimi deger 2 ise dikey renk karisimi yaparak bulaniklastirir
# gauss kenarlari bulmadan bulaniklastirir

blur_medyan = cv2.medianBlur(img2, 231)  # parazitleri kaldirmayi saglar, par3 cekirdegin boyutunu belirler

blur_bilateral = cv2.bilateralFilter(img3, 9, 75, 75)  # kenarlari belirler ve merkezi olan degerler
# ile bulanklistirma islemi yapar

cv2.imshow("images", img3)
cv2.imshow("blur", blur_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
