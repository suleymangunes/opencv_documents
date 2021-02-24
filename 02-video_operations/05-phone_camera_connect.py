import cv2
import numpy as np
import requests

url = "http://192.168.1.103:8080//shot.jpg"  # anlik goruntu alindi

while True:
    img_resp = requests.get(url)  # urldeki deger degiskene tanimlandi
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)  # goruntu byte formatina cevrildi
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)  # hafizadaki degerin goruntulenebilir hale getirilmesi saglandi
    img = cv2.resize(img, (640, 480))  # goruntu boyutlandirildi

    cv2.imshow("android camera", img)  # goruntu gosterildi

    if cv2.waitKey(10) == 27:  # esc tusuna basilirsa cikilmasi saglandi
        break

cv2.destroyAllWindows()
