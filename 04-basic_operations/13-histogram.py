import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")
b, g, r = cv2.split(img)  # resmin renk degerleri b g e degerlerine atandi
cv2.imshow("img", img)

plt.hist(b.ravel(), 256, [0, 256])  # resimdeki b degerleri ile histogram yapildi
plt.hist(g.ravel(), 256, [0, 256])  # g ve r degerleri de histograma eklendi
plt.hist(r.ravel(), 256, [0, 256])
plt.show()  # histogram gosterildi

cv2.waitKey(0)
cv2.destroyAllWindows()
