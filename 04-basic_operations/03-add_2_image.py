import cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
# bos tuvalde daire olusturuldu

rectangle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)
# bos tuvalde dikdortgen olusturuldu

add = cv2.add(rectangle, circle)  # iki tuval birbirine eklendi, piksel sayilari toplandi
# 255 255 255 beyaz oldugu icin beyaz kırmızı toplamı 255 255 255  oldu, kesisim yeri ise 255 0 255 oldu
# bu yuzden pembe rengini aldi. (isleyis bicimi = 250 + 20 = 255)

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()
