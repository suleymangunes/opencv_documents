import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg", 0)
row, col = img.shape

M = np.float32([[1, 0, -50], (0, 1, 60)])  # tasima islemi yapildi, par1 ve par2 nin ilk 2 degeri sabittir
# 3. degerlerden ilki yatay tasima ikincisi dikey tasima yapar, varsayilan + degerler sag ve asagi dogru tasimadir

dst = cv2.warpAffine(img, M, (col, row))  # fonksiyon ile m degerlerinin uygulanacagi degisken olusturuldu

M2 = cv2.getRotationMatrix2D((col/2, row/2), 180, 1.1)  # par2 ile dondurme islemi yapildi par 3 ile yakinlastirma
# islemi yapildi, varsayilan degerler dondurme icin 0 yakinlastirma icin 1'dir

dst2 = cv2.warpAffine(img, M2, (col, row))  # fonksiyon ile m degerlerinin uygulanacagi degisken olusturuldu


cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
