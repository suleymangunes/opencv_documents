import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # goruntu renk degeri gri tonlarina cevrildi

ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
# esik degerine gore pikselleri siyah beyaz olarak ayarlar

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # contour noktalari belirlendi

cv2.drawContours(img, contours, 1, (0, 0, 255), 3)  # kontorler cizildi, par1 goruntuyu par2 kontur degerleri
# par3 kontorun degeri par4 renk par5 kalinlik

cv2.imshow("contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
