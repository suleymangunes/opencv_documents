import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\j.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # goruntudeki renk degerleri gri tonlara donusturuldu

gray = np.float32(gray)  # olusan renk degerleri ondalikliya cevrildi

corners = cv2.goodFeaturesToTrack(gray, 100, 0.0001, 3)  # koselerin koordinatlari degiskene atandi
# par1 goruntuyu alir, par2 kose sayisini belirler, par3 ve par4 koseler arasi uzakligi belirler

corners = np.int32(corners)  # kose degerleri tam sayiya cevrildi

for corner in corners:  # koseler matris degerinden alinip sirayla cizilmesi icin dongu tanimlandi
    x, y = corner.ravel()  # kose degerlerin tek sirada dizilmesi saglandi, koordinat degerleri degiskene atandi
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # kose noktalarina daire cizildi

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
