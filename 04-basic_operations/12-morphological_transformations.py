import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\j.png", 0)
img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\j2.png", 0)
img3 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\j3.png", 0)
r, c = img.shape
r2, c2 = img.shape
r3, c3 = img.shape
img = cv2.resize(img, (int(c*3), int(r*3)))
img2 = cv2.resize(img2, (int(c2*3), int(r2*3)))
img3 = cv2.resize(img3, (int(c3*3), int(r3*3)))

kernel = np.ones((5, 5), np.uint8)
kernel2 = np.ones((25, 25), np.uint8)

erosion = cv2.erode(img, kernel, iterations=3)  # varsayilan beyaz 1 siyah ise 0'dir,
# erozyon islemini cekirdek etrafindaki tum degerler 1 degil ise yapar, bu sayede cizgi incelir, erozyona ugrar

dilation = cv2.dilate(img, kernel, iterations=2)  # genisleme isleminin yapilmasi icin cekirdek etrafindaki degerlerden
# en az birinin 1 olmasi yeterlidir, bu sayede cizgi genisler, genisleme islemi yapilmis olur

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # gurultunun giderilmesi saglanir, siyahtaki kucuk beyaz .'lar

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # gurultunun giderilmesi saglanir, beyazdaki kucuk siyah .'lar

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # genisleme ile erozyon arasindaki farktir

top_hot = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)  # Girdi görüntüsü ile görüntünün açılması arasındaki farktır

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)
# Giriş görüntüsünün kapanması ile giriş görüntüsünün arasındaki farktır

cv2.imshow("original1", img)
# cv2.imshow("erosion", erosion)
# cv2.imshow("dilation", dilation)
# cv2.imshow("original2", img2)
# cv2.imshow("opening", opening)
# cv2.imshow("original3", img3)
# cv2.imshow("closing", closing)
# cv2.imshow("gradient", gradient)
# cv2.imshow("top hot", top_hot)
cv2.imshow("black hat", black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
