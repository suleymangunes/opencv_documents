import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")

row, col, clr = img.shape  # shape methodu ile resmin sirayla satir, sutun ve renk degeri alindi degiskenlere atandi

img = cv2.resize(img, (int(col*0.5), int(row*0.5)))  # resize fonksiyonu ile yeniden boyutlandirma yapildi
# par1 resmin tutuldugu degisken, par2 boyutlandirma degerleri, sadece integer degerler verilmelidir yada cevrilmelidir

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
