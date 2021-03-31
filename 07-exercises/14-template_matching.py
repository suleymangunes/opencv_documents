import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\starwars.jpg")
img = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY)
template = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\starwars2.jpg", 0)
# orjinal resim ve orjinal resimden kesilmis kucuk resim ice aktarildi

w, h = template.shape[:: -1]  # kucuk resmin genislik ve yuksekligi alindi

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)  # fonksiyon ile iki resim arasindaki ortak alan belirdi
location = np.where(result >= 0.90)  # ortak alan degerlerinin threshhold ile koordinat degerleri bulundu
# ancak degerler iki ayri listeden geldigi icin zip fonksiyonu ile degerler ikili tupplelara atandi

for point in zip(*location[:: -1]):  # her point degeri iki degerli tupple degeri olarak tutuldu
    cv2.rectangle(img1, point, (point[0] + w, point[1] + h), (0, 0, 0), 2)  # her point degerine dortgen cizildi

cv2.imshow("img", img1)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
