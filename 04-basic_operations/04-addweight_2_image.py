import cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
# bos tuvalde daire olusturuldu

rectangle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)
# bos tuvalde dikdortgen olusturuldu

add = cv2.addWeighted(rectangle, 0.7, circle, 0.3, 0)  # iki tuval birbirine eklendi, piksel sayilari oranlandi toplandi
# mavinin degeri 0 0 255 oldugu icin 0.7 ile oranindan 0 0 178.5 kaldi, kirmizinin ise 76 0 0 oldu
# ikinci param saydamlik oranini belirler

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()
