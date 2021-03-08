import cv2


img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\mustang.jpg", 0)  # 0 ile gri tonlandi
r, c = img.shape  # resmin satir ve sutundaki piksel sayisi degiskenlere atandi, ekran cozunurlugu
img = cv2.resize(img, (int(c/2), int(r/2)))  # degerler ile resim yeniden boyutlandirildi

ret, th = cv2.threshold(img, 65, 200, cv2.THRESH_BINARY)  # threshold islemi yapildi
# threshold esik degerine gore pikselleri siyah yada beyaz olarak belirler, par2 siyahlarla par3 beyazlarla calisir

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
# resimdeki tum kenar cizgilerini siyaha geri kalan yerleri beyaz yapar

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
# gaussin mean'e gore daha ayrintili islem yapar

cv2.imshow("img", img)
cv2.imshow("thresh", th)
cv2.imshow("thresh2", th2)
cv2.imshow("thresh3", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
