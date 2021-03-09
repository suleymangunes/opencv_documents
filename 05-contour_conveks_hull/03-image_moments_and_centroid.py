import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\triangle.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
# goruntu renk degeri gri tonlara donusturuldu ve esik degerine gore karelerin siyah ve beyaz deger olmasi saglandi

moments = cv2.moments(thresh)  # olusan siyah beyaz goruntunun moment degerleri degiskene atandi

x = int(moments["m10"] / moments["m00"])  # moment degerleri ile agirlik merkezinin x ve y koordinati bulundu
y = int(moments["m01"] / moments["m00"])

cv2.circle(img, (x, y), 6, (0, 255, 0), -1)  # bulunan koordinata daire cizildi

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
